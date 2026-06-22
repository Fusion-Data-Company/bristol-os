#!/usr/bin/env python3
"""
Quarry parcel lookup for Bristol OS.
Pulls parcel data (owner, address, zoning, units, year built, value, absentee flag)
from Rob's Quarry engine. PARCEL DATA ONLY — no skip-trace.

Reads from environment (baked into the Bristol OS keys file):
  QUARRY_BASE_URL   e.g. https://quarry.fusiondataco.com   (no trailing slash)
  QUARRY_API_KEY    a Quarry API key (qk_...)

Usage:
  python quarry_lookup.py --address "381 Mallory Station Rd, Franklin TN"
  python quarry_lookup.py --lat 35.93 --lng -86.84
  python quarry_lookup.py --bbox minLng,minLat,maxLng,maxLat [--limit 100]
"""
import os, sys, json, argparse, urllib.parse, urllib.request

BASE = (os.environ.get("QUARRY_BASE_URL") or "").rstrip("/")
KEY = os.environ.get("QUARRY_API_KEY") or ""


def _get(path):
    if not BASE or not KEY:
        sys.exit("Quarry not configured: set QUARRY_BASE_URL and QUARRY_API_KEY (baked into Bristol OS keys).")
    req = urllib.request.Request(BASE + path, headers={"Authorization": f"Bearer {KEY}", "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, json.load(r)
    except urllib.error.HTTPError as e:
        body = e.read().decode()[:300]
        if e.code == 401:
            sys.exit("Quarry auth failed (401): the QUARRY_API_KEY is invalid or revoked.")
        if e.code == 404:
            return 404, {"parcel": None}
        sys.exit(f"Quarry error {e.code}: {body}")
    except Exception as e:
        sys.exit(f"Could not reach Quarry at {BASE} ({e}). Is the API public / URL correct?")


def geocode(address):
    """Free geocode via OpenStreetMap Nominatim (no key)."""
    url = "https://nominatim.openstreetmap.org/search?" + urllib.parse.urlencode(
        {"q": address, "format": "json", "limit": 1})
    req = urllib.request.Request(url, headers={"User-Agent": "BristolOS/1.0 (parcel lookup)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.load(r)
    if not data:
        sys.exit(f"Could not geocode address: {address}")
    return float(data[0]["lat"]), float(data[0]["lon"])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--address")
    ap.add_argument("--lat", type=float)
    ap.add_argument("--lng", type=float)
    ap.add_argument("--bbox", help="minLng,minLat,maxLng,maxLat")
    ap.add_argument("--limit", type=int, default=100)
    ap.add_argument("--zoom", type=int, default=17)
    a = ap.parse_args()

    if a.bbox:
        mnLng, mnLat, mxLng, mxLat = [float(x) for x in a.bbox.split(",")]
        q = urllib.parse.urlencode({"minLng": mnLng, "minLat": mnLat, "maxLng": mxLng,
                                    "maxLat": mxLat, "limit": a.limit})
        _, out = _get(f"/api/parcels/bbox?{q}")
        print(json.dumps(out, indent=2)); return

    lat, lng = (a.lat, a.lng)
    if lat is None or lng is None:
        if not a.address:
            sys.exit("Provide --address, or --lat and --lng, or --bbox.")
        lat, lng = geocode(a.address)
        print(f"# geocoded '{a.address}' -> {lat},{lng}", file=sys.stderr)

    # /api/parcels/at returns the rich record (zoning, units, year built, value, absentee, etc.)
    q = urllib.parse.urlencode({"lat": lat, "lng": lng, "zoom": a.zoom})
    _, out = _get(f"/api/parcels/at?{q}")
    if not out.get("parcel"):
        # fall back to corpus point lookup
        q2 = urllib.parse.urlencode({"lat": lat, "lng": lng})
        _, out = _get(f"/api/parcels/point?{q2}")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
