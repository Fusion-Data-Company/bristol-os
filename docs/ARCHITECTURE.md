# Bristol OS — Architecture

## The idea
A **public GitHub repo carries the machinery**; **secrets and personal data never live in it** (they're encoded or local). A team member pastes one message; Claude fetches `START-HERE.md`, writes a personalized workspace on their machine, and from then on behaves as Bristol OS in that folder.

## Repo layout
```
START-HERE.md            the installer Claude reads and executes
INSTALL.md / README.md   human entry points
plugins/bristol-os/
  .claude-plugin/        plugin.json (+ marketplace.json at root) for the Claude Code path
  skills/                the "plays" — each a SKILL.md (+ helper scripts)
templates/               CLAUDE.md, memo / market-study / one-pager / infographic / tracker / Excel model / intake / sources
profiles/                roster.md + per-person CLAUDE.md profiles (Sam, David)
reference/               underwriting-model, property-data-dictionary, bristol-portfolio, rigor-standard
catalog/                 TOOL-CATALOG (connectors) + GITHUB-PACK (verified repos)
brand/STYLE.md           the look of every deliverable
docs/                    this documentation
config/                  baked keys (encoded), power-layer MCP config, setup.sh, sharing-keys
memory/                  persistent memory (per-user records written at onboarding)
```

## What happens on install
1. Pull the pack into the user's `bristol-os/` workspace and **decode the baked keys** to `bristol-os/keys.env` (research + parcels + voice — no pasting).
2. **Identify the person** (account email/name → `profiles/roster.md`; else ask) and write their `CLAUDE.md` + `memory/<slug>.md`.
3. Build their **Deal Tracker** artifact, speak a welcome, run a real task to prove it.
4. **Ask what tools Bristol uses** (`connect-tools`) and connect them or set an export path; capture Bristol actuals for calibration.

## The governing behavior: V1 → V2 → V3 (`deal-evolution`)
Every analysis auto-evolves from one prompt: **draft (V1) → self-critique → harden (V2) → finalize (V3)** to the **[rigor standard](../reference/rigor-standard.md)** (IRR, yield-on-cost untrended/trended, spread over cost of capital, debt yield, replacement-cost basis, base/downside/upside, local-accuracy mandate). The user asks once; Claude delivers the final. Output is tuned per person — Sam gets brevity = distilled rigor; David gets the full model + every source.

## Two install paths
- **Desktop / Cowork (default, non-technical):** the one-paste bootstrap above. Keys baked in; connectors one-click.
- **Claude Code (technical):** `/plugin marketplace add Fusion-Data-Company/bristol-os` (the repo is also a plugin marketplace).

## Data & trust
- Parcels via Bristol's **Quarry** engine (key-free). Research via FRED/Census/Tavily/Exa/Firecrawl (baked keys). Optional pro feeds (CoStar/Yardi) connected per-user via `connect-tools`.
- **Citations everywhere** (`docs/CITATIONS.md`): every figure backlinks to a `sources.md`; estimates labeled; numbers reconcile across model/memo/deck/one-pager.

## Privacy
Per-user `CLAUDE.md`, `memory/`, and any Bristol data stay on the user's machine — never committed to the public repo (`.gitignore` enforces it).
