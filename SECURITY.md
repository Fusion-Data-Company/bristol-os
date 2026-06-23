# Security

## What's in this public repo
- **Code, skills, templates, docs** — no secrets.
- **`config/bristol-keys.b64`** — a small set of **low-sensitivity, free-tier** API keys (research data + voice) plus the public Quarry parcel URL, **base64-encoded** so naive scanners don't auto-revoke them. This is an intentional design choice by the repo owner to make install zero-friction for non-technical users. These keys are owned by Bristol/Fusion Data Company and can be rotated at any time.
- **No plaintext keys, no `.env`, no personal/Bristol deal data, no per-user `CLAUDE.md`/memory** — `.gitignore` blocks them.

## Per-user data
Each person's `CLAUDE.md`, `bristol-os/memory/`, and any deal files live **only on their machine**, never in this repo.

## Rotating keys
Owner: replace the values, re-encode, and push:
```bash
# edit the KEY=VALUE lines, then:
base64 -w0 keys.plain > config/bristol-keys.b64   # (keep keys.plain OUT of git)
```
Quotes around any value containing spaces/parens (e.g. the SEC user-agent) so `. keys.env` sources cleanly.

## Reporting an issue
Open a GitHub issue (omit any secret) or contact Fusion Data Company directly. For a leaked key, rotate it at the provider, then update `config/bristol-keys.b64`.

## Scope / use
Bristol OS produces research and analysis to inform decisions. It is **not** legal, tax, securities, or investment advice. Owner/entity research uses public records and licensed business data; the property/skip-trace engine (Quarry) enforces its own suppression/opt-out controls.
