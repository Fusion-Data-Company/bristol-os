---
name: quarry-parcels
description: Bristol's own Quarry engine — parcel data AND skip-trace. Look up a parcel (owner, mailing address, absentee flag, zoning, units, year built, sqft, acreage, value) and skip-trace the owner for a current phone and email. Use when the user asks "who owns this," "pull the parcel," "get me the owner's number/contact," "skip-trace this owner," "trace everyone on this block," or wants owner contact for acquisition outreach.
---

# Quarry — Parcels + Skip-Trace

Bristol's parcel intelligence engine (22.8M-parcel corpus + Regrid click-to-identify + skip-trace orchestrator). Turns an address, a point, an APN, or a map area into the owner, the property facts, and a contactable phone + email.

## Config (baked into Bristol OS keys — no pasting)
- `QUARRY_BASE_URL` — Quarry API base (e.g. `https://quarry.fusiondataco.com`)
- `QUARRY_API_KEY` — Quarry API key (`qk_...`)
Loaded automatically from the Bristol OS keys file. Claude runs the helper; the user types nothing.

## 1) Parcel lookup (no credits)
Returns owner name(s), situs address, **mailing address + absentee-owner flag**, county/state, APN, acreage, lot sqft, **use & zoning**, year built, building sqft, **units**, stories, beds/baths, **valuation**.
```bash
python bristol-os/skills/quarry-parcels/quarry_lookup.py --address "381 Mallory Station Rd, Franklin TN"
python bristol-os/skills/quarry-parcels/quarry_lookup.py --lat 35.93 --lng -86.84
python bristol-os/skills/quarry-parcels/quarry_lookup.py --bbox "-86.90,35.90,-86.80,35.97" --limit 200
```

## 2) Skip-trace (owner phone + email — charges 1 Quarry credit per trace)
Resolves the owner (from APN, name, address, or a dropped pin), then returns up to **2 ranked phones + 2 ranked emails** with confidence.
```bash
python bristol-os/skills/quarry-parcels/quarry_lookup.py --skiptrace --address "123 Main St, Nashville TN"
python bristol-os/skills/quarry-parcels/quarry_lookup.py --skiptrace --name "Jane Owner" --state TN
python bristol-os/skills/quarry-parcels/quarry_lookup.py --skiptrace --apn 0123456789
```
For a block/area: pull parcels with `--bbox` first, confirm with the user, then trace the ones they pick (the engine also supports bulk up to 25).

## How Quarry behaves (operational facts to relay)
- **1 credit per skip-trace.** Don't bulk-trace a whole list without the user's OK — tell them the count and the credit cost first.
- **Suppression is automatic.** Quarry scrubs every trace against its opt-out / Delete Act / Daniel's Law suppression list; a suppressed target returns `suppressed` (no charge) — report that outcome plainly, don't try to route around it.
- **Engine can take a minute**; a trace may come back `running` with a job id and finish on a follow-up poll (the helper handles this).
- **Not for FCRA-regulated use** (no tenant/credit/employment screening) — Quarry's own term. Bristol's use is acquisition/owner outreach, which is fine.

## How it feeds the other plays
- **site-selection:** owner, zoning, units, acreage, value for a candidate parcel → site one-pager.
- **investor-sourcing / owner outreach:** owner of record + mailing address + skip-traced phone/email = a ready contact for an acquisition approach.
- **market-comp-analysis:** `--bbox` to inventory nearby parcels (use, units, vintage).

## Output handling
- Read results back in plain English; save to the deal folder; cite "Quarry" + the date pulled.
- If a lookup/trace returns null/no-hit, say so — never invent an owner, number, or email.
- If `QUARRY_BASE_URL`/`QUARRY_API_KEY` aren't set, tell the user Quarry isn't connected yet (Rob: make the API reachable + drop in a key).
