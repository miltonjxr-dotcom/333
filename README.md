# Agent Economy Monitor

Institutional monitoring stack for the on-chain **agent economy**.

The goal is not to watch “AI agent” narrative volume. It is to detect **real regime changes** in machine payments, identity, and agent-to-agent commerce — then escalate those into research before the market prices them.

| Layer | Role |
| --- | --- |
| [`docs/weekly-cascade.md`](docs/weekly-cascade.md) | Weekly pack: Service Spend (not notional) → networks + protocols → SKU drill → commerce |
| [`docs/data-cleaning.md`](docs/data-cleaning.md) | Free desk: consume published JSON/CC0; Dune/Codex are rationed; no Allium |
| [`docs/protocol-layer.md`](docs/protocol-layer.md) | Same-layer boards: payment protocols (x402 / MPP / L402) are one board |
| [`docs/agent-economy-monitoring-playbook.md`](docs/agent-economy-monitoring-playbook.md) | Investment thesis, quality definition, alert catalog, escalation SOP |
| [`config/quota.yaml`](config/quota.yaml) | Dune monthly caps; Codex not for ETL |
| [`config/alert_rules.yaml`](config/alert_rules.yaml) | Machine-readable thresholds |
| [`config/watchlist.yaml`](config/watchlist.yaml) | Coverage universe and how to express a view |
| [`scripts/free_quality_panel.py`](scripts/free_quality_panel.py) | Daily F-proxies (yellow only; T3/T4 null) |
| [`scripts/tripwire.py`](scripts/tripwire.py) | Public T0 tripwire (unconfirmed; never a buy signal) |
| [`sql/optional_paid_allium_x402_quality_panel.sql`](sql/optional_paid_allium_x402_quality_panel.sql) | T3/T4 definition only — not scheduled |
| [`schemas/daily_quality_snapshot.schema.json`](schemas/daily_quality_snapshot.schema.json) | Daily snapshot contract |

## Rule that pays for the whole system

**Never treat raw x402 transaction count as adoption.**

August 2026 is the worked example: ~17.9 million settlements and only ~$437k of volume. That is a campaign, not an economy. The playbook is built so that pattern cannot page the desk as a “breakout.”
