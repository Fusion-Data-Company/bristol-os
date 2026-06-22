---
name: deal-pipeline
description: Track deals across stages and produce status updates. Use when the user says "track this deal," "what's in my pipeline," "update the status on [deal]," "give me a pipeline summary," or wants an overview of what's moving.
---

# Deal Pipeline

Keep a simple, living record of Bristol deals and produce clean status updates.

## When to use
"Add this to my pipeline," "what's in the pipeline," "update [deal] to underwriting," "give me a pipeline summary for Monday."

## Where it lives
A single file: `bristol-os/pipeline.md` in the workspace. Create it on first use.

## Stages (Bristol deal lifecycle)
`Sourced → Screening → Underwriting → IC/Approval → Capital Raise → Closing → Development → Lease-up → Stabilized → Disposition/Refi`

## For each deal track
- Name / location / product & units
- Stage + date entered stage
- Owner (who at Bristol is driving it)
- Next action + due date
- Key open items / blockers
- Link to the deal folder and latest memo

## Operations
- **Add:** append a new deal row/section.
- **Update:** move stage, log the change with a date, update next action.
- **Summary:** produce a grouped-by-stage overview, highlight what's stalled (no movement / overdue next action) and what needs a decision.
- Whenever another play produces a deliverable for a deal, note it on that deal's pipeline entry.

## Output
- Updated `pipeline.md`, plus a readable summary when asked (e.g., a Monday update grouped by stage with a "needs your attention" section at top).

## Guardrails
- Keep it factual — reflect only what the user tells you or what's in the deal folders.
- This is internal tracking; keep it in the workspace, never anywhere public.
