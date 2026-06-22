---
name: deep-research
description: Go deep on any question across many sources and return a cited, decision-ready briefing. Use when the user asks to "research," "look into," "go deep on," "find out everything about," or needs a sourced answer to a non-trivial question — markets, regulations, competitors, costs, trends, people/companies, or any topic where a single web result isn't enough.
---

# Deep Research

Turn a plain-language question into a thorough, source-cited briefing. This is the research engine the other Bristol plays lean on.

## When to use
The user wants more than a quick answer: "research the Nashville multifamily market," "what's happening with construction costs," "look into this developer," "find everything on this incentive program."

## Tools, in order of preference
1. **Tavily / Exa connectors** if connected (`tavily_research`, `tavily_search`, `web_search_exa`) — deepest, cleanest.
2. **Claude's built-in web search** — always available, the zero-setup default.
3. **Yardi Matrix / finance connectors** if the question is real estate or market data and they're connected.
4. The bundled `deep-research` skill if present in the user's Claude.
If only built-in search is available, still do the full method below — just rely on web search.

## Method
1. **Clarify the decision.** One sharp question if scope is unclear: what decision will this inform, and how deep do they need it? Then proceed.
2. **Decompose** the question into 4–8 sub-questions. State them.
3. **Fan out:** search each sub-question. Prefer primary and authoritative sources (government data, company filings, official market reports, reputable trade press). Note the date of every source.
4. **Triangulate:** confirm important facts across 2+ independent sources. Flag anything you can only find once as "single-source — verify."
5. **Adversarially check:** actively look for data that contradicts the emerging answer. Note disagreements rather than smoothing them over.
6. **Synthesize** into the output format below. Lead with the answer.
7. **Cite everything** with source + date. Never present an unsourced number as fact.

## Output (save to the workspace, e.g. `research/<topic>-<date>.md`)
- **Bottom line** — the answer in 3–5 sentences.
- **Key findings** — the important points, each with a source and date.
- **What's uncertain / contested** — gaps, conflicting data, single-source items.
- **So what for Bristol** — implications for the deal/market/decision at hand.
- **Sources** — list with links and dates.

## Guardrails
- If you can't verify a claim, say so. Do not fabricate figures, comps, dates, or names.
- Public and licensed sources only (see `bristol-os/docs/data-ethics-and-fair-housing.md`).
- Distinguish fact (sourced) from estimate (your reasoning) — label estimates.
