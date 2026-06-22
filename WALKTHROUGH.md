# Bristol OS — What happens, minute by minute

This is exactly what a Bristol team member (say, David) experiences from the moment he opens Cowork and runs your command. He types nothing technical and configures nothing.

---

## The one thing he does
1. Opens the **Claude desktop app** and starts Cowork.
2. Pastes this and hits enter:

> **Install Bristol OS for me. Fetch this file and follow every instruction in it exactly, then walk me through setup step by step in plain English: https://raw.githubusercontent.com/Fusion-Data-Company/bristol-os/main/START-HERE.md**

That's the whole ask of him. Everything below, Claude does.

---

## Minute 0–1 — It greets him and sets up silently
- Claude reads START-HERE, says a one-line hello ("Setting up Bristol OS — give me a couple minutes, you don't need to do anything"), and asks him to pick a folder (or uses the one that's connected). That folder becomes his Bristol workspace.
- In the background it pulls the whole pack from GitHub into a `bristol-os/` folder, and **decodes the baked-in keys** to `bristol-os/keys.env`. He never sees a key or a command.

## Minute 1–2 — It speaks
- Claude loads the keys and **plays a spoken welcome in Bristol's voice** (ElevenLabs, "Sarah"): *"Hi, and welcome to Bristol OS. I'm your research and analysis partner… there's nothing for you to install or configure. Just tell me what you're trying to figure out, and I'll do the research and build the document."*
- Because he's **David**, Claude recognizes him and uses his **pre-built profile** — so it already knows he's the CIO who runs site selection, feasibility, and capital. It barely has to ask anything.

## Minute 2–3 — It writes his brain file
- Claude writes his personalized **CLAUDE.md** into the workspace (who he is, Bristol's deal criteria, his markets, how he likes deliverables) and tells him in one sentence what it is: *"That's your permanent briefing — I read it every time so you never re-explain yourself. I keep it updated."*

## Minute 3–4 — It builds his live tracker
- Claude creates his **Deal Tracker** — a live visual board pinned in the sidebar — and says: *"I made you a live Deal Tracker; click any card to update a deal and it saves itself."* He didn't build or find anything.

## Minute 4–6 — It proves it on something real
- Claude does a real task end to end, then shows the result. Default: it **pulls a real parcel** for a site he cares about — *"That parcel at [address] is owned by [LLC], an absentee owner mailing to [city]; 0.4 acres, zoned [X], appraised at [$]."* — and drops it into a clean **one-pager with a Bristol infographic**. It saves the file to the deal folder and adds the deal to the tracker.
- No map opened. No paid lookup. No key. Just the answer.

## Minute 6+ — He just talks
From here he says things in plain English and Claude **does them** (never tells him how):
- *"Who owns this parcel and what's it worth?"* → Quarry answers instantly.
- *"Is Franklin a good submarket for 260 units? Give me a one-pager."* → site read + infographic, saved.
- *"Pull rent comps and build a market study."* → comp table + study + chart.
- *"Research my underwriting assumptions — taxes, insurance, construction."* → sourced ranges (FRED/Census + web).
- *"Turn this into an IC memo."* → Word memo with the deal-snapshot infographic.
- *"What's on my plate?"* → spoken status + the tracker.
- *"Make me more powerful."* → Claude sets up any optional tool for him.

## Every time he opens the folder after that
- Claude loads keys and **speaks a short status** — greets him by name, says what's ready and the one thing that needs a next step — then waits for what he needs, and does it.

---

## What's powering it (he never sees any of this)
- **Parcels/owners:** Bristol's Quarry engine (key-free).
- **Research/market/macro:** web + Tavily, Exa, FRED, Census, Alpha Vantage, Firecrawl (keys baked in).
- **Voice:** ElevenLabs.
- **Deliverables:** Word/Excel/PDF/PowerPoint + Bristol infographics, all zero-setup.
- **Tracking:** the live Deal Tracker artifact.
- **The rule over all of it:** if Claude can do it, it does it and tells him what it did.
