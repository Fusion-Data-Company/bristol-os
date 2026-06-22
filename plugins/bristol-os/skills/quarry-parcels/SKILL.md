---
name: quarry-parcels
description: Get parcel data on any property — owner, mailing address, absentee flag, zoning, units, year built, sqft, acreage, and value — from Bristol's Quarry engine. This is the default way to answer ANY "who owns this," "pull the parcel," "what's the zoning," "what's it worth," or property-owner question. No map, no key, no paid service — just the data, returned and dropped into the one-pager.
---

# Quarry — Parcel Data

Bristol's own parcel engine. When anyone asks about a property, **this is where the answer comes from** — not a paid lookup site, not a map they have to click. Claude queries it and returns the facts.

## HARD LAW
If they ask for parcel data, **just get it and give it to them.** Don't open a map, don't explain how, don't ask them to do anything. Run the query, read back the answer, and put it in the one-pager/deal folder.

## How (Claude runs this; user does nothing, no key needed)
```bash
# by address (auto-geocodes, free)
python bristol-os/skills/quarry-parcels/quarry_lookup.py --address "381 Mallory Station Rd, Franklin TN"
# by coordinates
python bristol-os/skills/quarry-parcels/quarry_lookup.py --lat 36.16 --lng -86.78
# everything in a map area (returns a list — no map shown)
python bristol-os/skills/quarry-parcels/quarry_lookup.py --bbox "-86.90,35.90,-86.80,35.97" --limit 200
```
The base URL is baked in; **parcel lookups need no key and cost nothing.** It returns JSON — owner, mailing address, absentee flag, county, APN, acreage, lot sqft, zoning, year built, building sqft, units, and value.

## What to do with the result
- Read it back in plain English ("This parcel is owned by 616 Church LLC — an absentee owner mailing to Cleveland, OH; 0.09 acres, zoned Downtown Code, appraised at $X").
- **Drop it straight into the site one-pager** (`bristol-os/templates/site-one-pager.md`) owner/zoning/value fields, and save to the deal folder.
- Cite "Quarry" + the date.
- If it returns null, say the parcel wasn't found — never invent it.

## Owner contact (skip-trace, optional)
Quarry can also return the owner's phone/email. Run with `--skiptrace`:
```bash
python bristol-os/skills/quarry-parcels/quarry_lookup.py --skiptrace --address "123 Main St, Nashville TN"
python bristol-os/skills/quarry-parcels/quarry_lookup.py --skiptrace --apn 0123456789
```
Returns up to 2 phones + 2 emails with confidence. This draws on Bristol's Quarry account.

## Feeds
- **site-selection / one-pager:** owner, zoning, units, acreage, value.
- **investor-sourcing / owner outreach:** owner + mailing address (+ contact via `--skiptrace`).
- **market-comp-analysis:** `--bbox` to inventory nearby parcels.
