# Bristol OS

**Turn Claude into a research-and-analysis teammate for Bristol Development Group — in one paste, no setup, no subscriptions, no command line.**

Bristol OS installs itself by telling Claude to read its own instructions. A team member pastes one message into the Claude desktop app; Claude pulls the pack, interviews them, writes them a personalized `CLAUDE.md`, teaches them how it works, and runs a real research task live.

---

## ✅ How to install (give this to anyone at Bristol)

1. Open the **Claude desktop app**.
2. Paste this message and send it:

> **Install Bristol OS for me. Fetch this file and follow every instruction in it exactly, then walk me through setup step by step in plain English: https://raw.githubusercontent.com/Fusion-Data-Company/bristol-os/main/START-HERE.md**

3. Answer Claude's questions. That's it — Claude does the rest (about 5–10 minutes).

There is nothing to download, no account to create, and no code to run. The free version works with the web search already built into Claude.

---

## What it gives each person
- A personalized **CLAUDE.md** so Claude always knows their role, their deals, and how Bristol works.
- Seven research **plays** (skills): deep research, site selection, market & comp analysis, investor & owner sourcing, underwriting research, deal memos, and deal-pipeline tracking.
- Plain-English coaching on what it can do and how to use it.
- Optional, guided upgrades for deeper research (Tavily, Exa, Apollo, Yardi Matrix, and more).

## What it deliberately won't do
- It won't invent numbers — everything is sourced and dated, and it says when it can't verify something.
- It follows **Fair Housing** and **data-ethics** rules automatically (no consumer skip-tracing; public records + licensed business data only).
- It informs decisions; it doesn't give legal, tax, securities, or investment advice.

## Tools & repos it can pull in
Bristol OS ships a fully-configured **tool catalog** and a **verified GitHub pack**:
- `catalog/TOOL-CATALOG.md` — every recommended connector (research, real estate, finance, investor/owner, docs, CRM, PM), tiered into *zero-cost defaults* vs *paid power-ups*, each mapped to the play it powers.
- `catalog/GITHUB-PACK.md` — ~30 verified public repos (Anthropic skills, MCP directories, real-estate/Census/SEC/FRED/Maps MCP servers, doc generators). Every repo confirmed live via the GitHub API with real star counts; archived ones flagged.

Two paths, on purpose: **basic users** get one-click first-party connectors only; **Rob / a technical helper** gets the full open-source power setup. Nobody non-technical is ever asked to touch a command line.

## What's in this repo
```
START-HERE.md            ← the installer Claude reads and executes
templates/CLAUDE.md.template
onboarding/              ← interview + connector setup + tool guide
catalog/                 ← TOOL-CATALOG.md + GITHUB-PACK.md
plugins/bristol-os/skills/   ← 8 plays (7 research + knowledge-packs)
templates/               ← memo, market study, one-pager, folder structure
docs/                    ← "what is a CLAUDE.md", how-to, ethics & Fair Housing
.claude-plugin/marketplace.json  ← optional, for Claude Code users
```

## Privacy
This repository contains **no secrets and no Bristol data**. Each person's information and their `CLAUDE.md` are generated and stored only on their own computer — never uploaded here.

---
*Built for Bristol Development Group · Franklin, TN · v1.0*
