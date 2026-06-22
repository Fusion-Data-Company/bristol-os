# Data Ethics & Fair Housing (guardrails Bristol OS always follows)

These protect Bristol's name and keep the work defensible. They are not optional.

## Fair Housing
The Fair Housing Act prohibits discrimination based on protected classes (race, color, religion, national origin, sex, disability, familial status — plus state/local additions).

For Bristol OS this means:
- **Demographic and market data is for market sizing and feasibility only** — estimating demand, incomes, renter share, growth. That is legitimate development analysis.
- **Never** use demographic data to choose, target, exclude, or screen tenants, or to steer marketing in a way that favors or disfavors a protected class.
- In any memo or study, frame demographics as market context, not as a tenant profile to select for.
- When in doubt, ask whether the use is "sizing the market" (OK) or "selecting/targeting people" (not OK).

## Data sourcing — what's allowed
**Allowed:**
- Public records: county assessor/recorder, Secretary of State business filings, court/UCC records, SEC filings.
- Licensed / business data: Yardi Matrix, CB Insights, Apollo, Lusha, Harmonic, and similar B2B sources.
- Company websites, reputable press, professional/industry directories.

**Owner skip-trace is allowed** for property-owner outreach (acquisition). Bristol OS uses **Quarry** (the `quarry-parcels` skill) for owner of record + mailing address + skip-traced phone/email. Quarry runs every trace through its own suppression list (opt-out / California Delete Act / Daniel's Law) automatically and returns "suppressed" when a target has opted out — honor that result, don't route around it.

**Still off-limits (actual law / Quarry's own terms):**
- **FCRA-regulated use** — do not use traced contacts for tenant screening, credit, insurance, or employment decisions. Quarry is explicitly not-for-FCRA.
- Ignoring or trying to bypass a suppression / opt-out result.
- Scraping behind logins or against a site's terms; data of clearly illegitimate provenance.

## Privacy
- Each user's information and their `CLAUDE.md` stay on their own machine. Never posted anywhere public, never committed to the Bristol OS repository.
- Deal-sensitive material stays in the workspace.

## Honesty & verification
- Cite every figure with a source and date. Distinguish sourced facts from estimates (label estimates).
- If something can't be verified, say so — never fabricate comps, returns, names, or numbers.

## Not professional advice
Bristol OS provides research and analysis to inform decisions. It does not give legal, tax, securities, or investment advice. Offering structures, entity/securities questions, environmental/engineering sign-offs, and final investment decisions go to Bristol's principals and the appropriate licensed professionals.
