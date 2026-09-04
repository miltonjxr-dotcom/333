# Agent Economy Monitor

Institutional monitoring stack for the on-chain **agent economy**.

The goal is not to watch “AI agent” narrative volume. It is to detect **real regime changes** in machine payments, identity, and agent-to-agent commerce — then escalate those into research before the market prices them.

| Layer | Role |
| --- | --- |
| [`docs/REVIEW-PACK.md`](docs/REVIEW-PACK.md) | **完整方案（给外部 AI 审核）**：先验、分层、分母、免费栈、审计、警报、空洞 |
| [`docs/weekly-ai-prompt.md`](docs/weekly-ai-prompt.md) | 每周丢给 AI 的固定提示词（Python 周更，不是 Dune） |
| [`docs/data-cleaning.md`](docs/data-cleaning.md) | Free desk: consume published JSON/CC0; Dune/Codex are rationed; no Allium |
| [`docs/source-landscape.md`](docs/source-landscape.md) | Census of Artemis / x402scan / x402-list / Dune / etc. — keep vs ignore |
| [`config/sources.yaml`](config/sources.yaml) | Machine-readable source roles (not a GMV union) |
| [`docs/cleaner-audit.md`](docs/cleaner-audit.md) | How to score website washers without trusting `real %` |
| [`scripts/audit_cleaners.py`](scripts/audit_cleaners.py) | Monthly free scorecard (Dune=0, Codex=0) |
| [`docs/protocol-layer.md`](docs/protocol-layer.md) | Same-layer boards: payment protocols (x402 / MPP / L402) are one board |
| [`docs/agent-economy-monitoring-playbook.md`](docs/agent-economy-monitoring-playbook.md) | Investment thesis, quality definition, alert catalog, escalation SOP |
| [`config/quota.yaml`](config/quota.yaml) | Dune monthly caps; Codex not for ETL |
| [`config/alert_rules.yaml`](config/alert_rules.yaml) | Machine-readable thresholds |
| [`config/watchlist.yaml`](config/watchlist.yaml) | Potential expressions / conditional beneficiaries (not a core book) |
| [`scripts/weekly_pack.py`](scripts/weekly_pack.py) | **Weekly 表 0 auto-fill** (markdown). Human leftover: Artemis / rankings (~10 min) |
| [`scripts/free_quality_panel.py`](scripts/free_quality_panel.py) | Daily F-proxies (yellow only; T3/T4 null) |
| [`scripts/tripwire.py`](scripts/tripwire.py) | Public T0 tripwire (unconfirmed; never a buy signal) |
| [`sql/optional_paid_allium_x402_quality_panel.sql`](sql/optional_paid_allium_x402_quality_panel.sql) | T3/T4 definition only — not scheduled |
| [`schemas/daily_quality_snapshot.schema.json`](schemas/daily_quality_snapshot.schema.json) | Daily snapshot contract |

## Weekly (mostly automatic)

```bash
python3 scripts/weekly_pack.py
```

Fills 表 0 from free JSON (agenteconomy + x402watch + npm + x402-list). Observed Spend / Buyers / Repeat stay null. Then spend ~10 minutes on the Artemis page linked in the output. Do not build a Dune dashboard.

**交给 AI 每周跑：** 把 [`docs/weekly-ai-prompt.md`](docs/weekly-ai-prompt.md) 里的提示词整段贴给 Cursor Agent（或任何能跑终端的模型）。自动化是 Python，不是 Dune。Dune 只在周记写了「开研究」时最多抽 3 条。

## Rule that pays for the whole system

**Never treat raw x402 transaction count as adoption.**

August 2026 is the worked example: ~17.9 million settlements and only ~$437k of volume. That is a campaign, not an economy. The playbook is built so that pattern cannot page the desk as a “breakout.”
