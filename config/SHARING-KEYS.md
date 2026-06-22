# How Bristol shares its API keys with the team

The keys are **Bristol's** — Bristol owns them, stores them, and rotates them. They do **not** go in this public repo (anything public is scraped and revoked within minutes). The repo carries the code; the keys travel on a private pipe to each machine. Three ways, pick by who:

## 1. One-click connectors — for the office (Sam, David, staff)
No files, no repo. In the Claude desktop app:
**Settings → Connectors → [the tool] → Connect → a box pops up → paste the Bristol key (or log in) → done.**
- The key is stored inside that person's Claude app.
- The **same Bristol key works for everyone** — hand each person the key through a private channel (below) and they paste it once.
- Best for: Tavily, Exa, and any other first-party connector. This is the lowest-friction path for non-technical staff.

## 2. Shared private folder or vault — for anyone running the power rig
For the MCP servers (FRED, Census, SEC, etc.) that use `config/.env`:
1. Put the filled `.env` in a place only Bristol can see:
   - a **restricted Bristol Google Drive / Dropbox folder**, or
   - a **shared 1Password / Bitwarden vault** item (best practice).
2. Each person copies that `.env` into their `bristol-os/config/` folder.
3. They run `bash config/setup.sh` and restart Claude.
- Best for: a couple of power users. Keys never leave Bristol's own storage.

## 3. Private keys repo — for you + technical helpers
- Keep `.env` in a **private** GitHub repo (e.g. `bristol-os-private`) and add Sam/David as collaborators.
- They `git clone` it (requires a GitHub login — fine for technical users, not for basic staff).
- Best for: Rob and anyone comfortable with GitHub.

## Shared key vs. per-person key
- Free tiers are rate-limited **per key**. One shared Bristol key is fine to start.
- If usage grows (several people researching heavily at once), issue a separate key per person from the same provider account and give each person their own `.env`. Same setup, just a different key string.

## Recommendation
| Who | Pipe | Tools they get |
|---|---|---|
| Office staff (Sam, David, most) | **Connectors (#1)** | Web search + Tavily/Exa one-click |
| Power user (Rob, a helper) | **Vault/Drive (#2)** + `setup.sh` | Full MCP rig: FRED, Census, SEC, Maps, etc. |
| Backup/secure store | **Private repo (#3)** | Source of truth for the key file |

> This file intentionally contains **no keys**. The real keys live in Bristol's vault/Drive/connectors.
