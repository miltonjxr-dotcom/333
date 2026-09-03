# Agent Economy Monitor

Institutional monitoring stack for the on-chain **agent economy**.

The goal is not to watch “AI agent” narrative volume. It is to detect **real regime changes** in machine payments, identity, and agent-to-agent commerce — then escalate those into research before the market prices them.

| Layer | Role |
| --- | --- |
| [`docs/protocol-layer.md`](docs/protocol-layer.md) | Which protocols to watch (x402, Virtuals ACP ≠ Google AP2) |
| [`docs/agent-economy-monitoring-playbook.md`](docs/agent-economy-monitoring-playbook.md) | Investment thesis, quality definition, alert catalog, escalation SOP |
| [`config/alert_rules.yaml`](config/alert_rules.yaml) | Machine-readable thresholds |
| [`config/watchlist.yaml`](config/watchlist.yaml) | Coverage universe and how to express a view |
| [`sql/allium_x402_quality_panel.sql`](sql/allium_x402_quality_panel.sql) | Allium quality panel (the only GMV that matters) |
| [`scripts/tripwire.py`](scripts/tripwire.py) | Public-data tripwire (unconfirmed; never a buy signal) |
| [`schemas/daily_quality_snapshot.schema.json`](schemas/daily_quality_snapshot.schema.json) | Daily snapshot contract |

## Rule that pays for the whole system

**Never treat raw x402 transaction count as adoption.**

August 2026 is the worked example: ~17.9 million settlements and only ~$437k of volume. That is a campaign, not an economy. The playbook is built so that pattern cannot page the desk as a “breakout.”
