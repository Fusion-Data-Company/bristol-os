# Bristol OS — Optional Research Upgrades (click-by-click)

> Claude: Bristol OS already works with Claude's built-in web search. These are OPTIONAL upgrades for deeper research. Only walk the person through one if they ask. Explain in plain English; do the technical parts for them where possible. All of these are added in the Claude desktop app under **Settings → Connectors** (a.k.a. Capabilities), and each requires the person to log in once — that part only they can do.

## How connectors work (say this)
> "A 'connector' plugs an outside research tool into me so I can pull deeper data. You add it once in Settings, log in once, and then I can use it forever. I'll point you to exactly where to click."

## Tier 1 — Deeper web research (free tiers, recommended first)
**Tavily** — an AI research engine that searches the web and hands me clean, cited results.
1. Go to **tavily.com**, sign up (free), and copy your API key from the dashboard.
2. In Claude desktop: **Settings → Connectors → Add/Browse**, find **Tavily**, click **Connect**, paste the key (or sign in if it offers OAuth).
3. Done — tell me "Tavily is connected" and I'll start using it for deep research.

**Exa** — neural web search, great for finding niche sources.
1. Go to **exa.ai**, sign up, copy your API key.
2. Claude desktop → **Settings → Connectors**, find **Exa**, **Connect**, paste the key.

## Tier 2 — Investor & business-contact research
Use these for capital-partner / LP research and legitimate B2B contact info (not consumer data).
- **Apollo**, **Lusha**, **Harmonic** — find and enrich business contacts and companies.
- **CB Insights** — private-company and investor intelligence.
Each: Claude desktop → **Settings → Connectors** → find it → **Connect** → sign in with that service's account.

## Tier 3 — Professional real estate data (only if Bristol subscribes)
**Yardi Matrix** — multifamily market intelligence, property search, and owner lookup. This is the strongest real estate data source if Bristol has a subscription.
1. Confirm Bristol has a Yardi Matrix login.
2. Claude desktop → **Settings → Connectors** → find **Yardi Matrix** → **Connect** → sign in with the Bristol Yardi credentials.
3. Tell me it's connected and I'll use it for site selection, comps, and owner research.

> Note: CoStar / RealPage don't have a direct Claude connector today. If Bristol uses them, I'll lean on web research + Yardi (if connected) and you can paste exports from those tools to me anytime.

## After connecting anything
Tell Claude what you connected so it can update your `CLAUDE.md` "connected tools" line and start using it.
