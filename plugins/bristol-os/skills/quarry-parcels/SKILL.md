---
name: quarry-parcels
description: Look up parcel data (owner of record, mailing address, absentee-owner flag, zoning, units, year built, building sqft, acreage, and assessed value) from Bristol's Quarry engine. Use when the user asks "who owns this," "pull the parcel," "what's the zoning/owner on this address," "is the owner absentee," or wants parcel facts for a site or an area. PARCEL DATA ONLY — not skip-trace.
---

# Quarry Parcels

Bristol's own parcel engine (22.8M-parcel corpus + Regrid click-to-identify). Turns an address, a point, or a map area into hard parcel facts. This is the fastest path to **who owns a site and what's allowed on it**.

## What it returns (rich record from `/api/parcels/at`)
Owner name(s), situs address, **mailing address + absentee-owner flag**, county/state, APN, acreage, lot sqft, **use & zoning** (description + type), year built, building sqft, **units**, stories, beds/baths, and **valuation**.

## Config (baked into Bristol OS keys — no pasting)
- `QUARRY_BASE_URL` — the Quarry API base (e.g. `https://quarry.fusiondataco.com`)
- `QUARRY_API_KEY` — a Quarry API key (`qk_...`)
Both live in the Bristol OS keys file the installer wrote; they load automatically.

## How to run
Use the bundled helper (Claude runs this for the user — they never type anything):
```bash
# by address (auto-geocodes, free, via OpenStreetMap)
python bristol-os/skills/quarry-parcels/quarry_lookup.py --address "381 Mallory Station Rd, Franklin TN"
# by coordinates
python bristol-os/skills/quarry-parcels/quarry_lookup.py --lat 35.93 --lng -86.84
# everything in a map area
python bristol-os/skills/quarry-parcels/quarry_lookup.py --bbox "-86.90,35.90,-86.80,35.97" --limit 200
```
It prints the parcel JSON. Read it back to the user in plain English and save it to the deal folder.

## How it feeds the other plays
- **site-selection:** pull owner, zoning, units, acreage, value for a candidate parcel → straight into the site one-pager.
- **investor-sourcing (owner research):** owner of record + mailing address + absentee flag = the legitimate, public-record owner lookup. Hand Bristol the owner; do not pursue personal/consumer contact data.
- **market-comp-analysis:** use `--bbox` to inventory nearby parcels (use, units, vintage) for the competitive picture.

## Boundaries (important)
- **Parcel data only.** This skill does NOT call Quarry's skip-trace (phone/email) endpoints. Bristol OS surfaces ownership and property facts from public records, not consumer contact data. (See `bristol-os/docs/data-ethics-and-fair-housing.md`.)
- Cite Quarry as the source + the date pulled. If a parcel returns null, say so — don't guess.
- Quarry's data is "not for FCRA-regulated purposes" (no tenant/credit/employment screening) — keep use to development/acquisition research.

## If it's not configured yet
If `QUARRY_BASE_URL`/`QUARRY_API_KEY` aren't set, tell the user Quarry isn't connected yet and that Rob needs to (1) make the API reachable and (2) drop in a Quarry API key — then it works with no other change.
