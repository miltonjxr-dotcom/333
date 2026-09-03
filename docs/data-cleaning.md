# Data cleaning — free desk only

Constraint: **no paid warehouse (no Allium).** Dune credits and Codex quota are scarce. Daily jobs must be $0 and must not classify 30k+ endpoints with a model.

**Buy nothing. Free-ride published extracts. Own the *interpretation*, not a second indexer.**

```
Free, unlimited daily              Scarce (budgeted)                 Do not do
──────────────────────────────     ──────────────────────────────    ────────────────────
agenteconomy.to/data.json          Dune: max a few queries/month     Re-run their query IDs
x402watch-data (GitHub, CC0)       Codex: memos only, never ETL      LLM-label 34k services
npm download counts (weekly)       OpenRouter rankings: eyeball      Private 402 indexer
CoinGecko / public IR              or 1 API call/week if you         Visa whale filters
x402watch API: avoid; 60 req/h     already have a free key
```

T3/T4 remain the **definition** of Service Spend. On this desk they are **not a daily series**. Without transfer-level rows you cannot compute unique T3 buyers, T4 repeat, facilitator-cluster T2, or fee vs $500 ACP notional. Pretending x402watch `real_volume` is T3 is how 表 0 gets lied to.

How to score a website’s washer without trusting `real %`: [`cleaner-audit.md`](cleaner-audit.md) and `python3 scripts/audit_cleaners.py`.

Which public sites exist and which we refuse to ingest: [`source-landscape.md`](source-landscape.md).

---

## Quota rules

### Dune — treat credits like a research option, not a feed

agenteconomy.to already executes the hashed/chriscen queries and publishes JSON. Their `meta.queries.*.lastCostCredits` on 2026-09-03 was ~10 + 5 + 4 + … **per refresh**. Forking those `queryId`s (7881006, 7895747, 7881007, 7881124, …) is lighting the monthly budget for numbers we already have for free.

| Cadence | Dune |
| --- | --- |
| Daily | **0 queries.** Read `https://agenteconomy.to/data.json`. |
| Weekly | **0 queries** unless a yellow flag is open. Prefer screenshots of *already-run* public dashboards (view is free). |
| Monthly IC | Optional: 1–2 **narrow** queries (top 20 payees for a 7d window, or 8004 proofs). Write the SQL first; estimate credits; then run once. |
| Yellow escalation | Cap **3 queries** for that incident. Sample, don’t backfill a warehouse. |

Never: daily scheduled Dune, “just in case” refreshes, or re-aggregating ACP memos that are already in the JSON.

### Codex — not a washer

x402watch already used models to assign categories. Doing it again burns Codex (or any LLM) quota to reproduce a worse catalog.

| Allowed | Forbidden |
| --- | --- |
| One monthly memo pass after a real yellow | Daily “classify these endpoints” |
| Reading a 20-row Dune sample | Pair-level wash labels (use x402watch CC0) |
| Editing this repo’s deterministic scripts | Asking Codex to invent T3 USD |

OpenRouter **app** named Codex (a harness on rankings) is unrelated. Do not poll OpenRouter Data API daily; it wants an API key and shares rate limits with inference. Weekly eyeball [openrouter.ai/rankings](https://openrouter.ai/rankings) (CC BY 4.0) is enough for D1.

---

## What each free source actually is

| Source | Cost | Grain | What it is | 表 0? |
| --- | --- | --- | --- | --- |
| **agenteconomy.to** | Free JSON | Ecosystem T0 + MPP byType + ACP memos/senders + 8004 mints | Someone else’s Dune output | No. Yellow + MPP `Settled` + ACP senders |
| **x402watch-data** daily CC0 | Free git/raw | Service catalog + 24h **category** USD/tx + 30d real/wash USD + buyer **label counts** | Their “real” (crawlers still in); **no per-tx ledger**, often **no per-service USD** | No. F-proxies and SKU mix only |
| **x402watch HTTP API** | Free, 60 req/h | Same as above, live | Easy to blow the rate limit; GitHub dump is enough | Don’t use daily |
| **Dune (our account)** | Credits | Whatever we write | Transfer-level *sample* | Only on escalation |
| **Ling et al. / Visa×Artemis** | Free to read | Historical snapshots | Calibration | Not a feed |
| **Allium** | Paid | Transfer-level T1 flags | Out of scope | — |

Worked numbers on **2026-09-03** (do not freeze these as targets; they show the gap):

- agenteconomy T0: ~181M txs / ~$41.6M cumulative; Sep-26 month-to-date ~3.37M txs / ~$38.5k (avg ticket ~$0.011).
- x402watch 30d `real_volume_usdc` ~$709k vs `wash_volume_usdc` ~$54 — filter is extremely conservative (false-negative bias). `organic_user` ≈ 36k buyers is the **default unlabeled bucket**, not Unique Buyers.
- x402watch 24h category volume ~$325, of which `token_data` ~$251. That 24h SKU mix is the only free **「钱买了什么」** series. It is not T3.

---

## Free production path (what we actually run)

```
Daily (scripts/tripwire.py + scripts/free_quality_panel.py)
  agenteconomy.to/data.json
       → T0 txs/vol/ticket (yellow only)
       → MPP Settled / unique payees (native unit)
       → ACP memos vs senders (M2)
       → 8004 mint count (ignore as GMV)
  GitHub x402watch-data  (buyer-labels + category-benchmarks; services.gz if counting live sellers)
       → F1: 30d real_volume_usdc          (their real, too loose)
       → F1w: 30d wash + developer USD     (sanity)
       → F_sku: 24h USD by category        (PMF drill, 表 2b)
       → F_sellers: services last_seen 7d with a non-placeholder category
       → Repeat Buyer Rate: UNKNOWN        (needs transfers; leave null)

Weekly
  npm downloads for `x402` (and agentkit if needed)
  OpenRouter rankings page (no API)
  CoinGecko VIRTUAL — satellite only

Monthly / yellow
  At most a few Dune credits: top payees, chain USD not tx, or 8004 proofs
  Codex: write the memo, do not relabel the chain
```

SQL in [`sql/optional_paid_allium_x402_quality_panel.sql`](../sql/optional_paid_allium_x402_quality_panel.sql) is a **definition of T3/T4**, not an operating job.

---

## Map boss KPIs onto what we can actually see

| Boss KPI | Free proxy | Honest hole |
| --- | --- | --- |
| **Service Spend** | x402watch 24h category USD **plus** MPP `Settled` if the feed gives a size; never + ACP notional | 24h SKU USD is a **subset** of indexed services, not machine GDP. 30d `real_volume` is an upper-ish F1, still not Service Spend |
| **Paid Tx** | 24h `total_tx` by category; MPP Settled count | Not T3 paid tx. T0 txs remain the wash trap |
| **Unique Buyers** | **null** daily | Label counts ≠ unique demand. `organic_user` is a residual class |
| **Repeat Buyer Rate** | **null** daily | T4 needs a buyer×day panel |
| **Unique Sellers** | Count of catalog rows `last_seen` in 7d, category not `premium_placeholder` / `other` | Directory size, not independent T3 payees |

表 0 on the free desk is therefore **four numbers + two explicit nulls**, all stamped `quality_available: false` for T3/T4. A week where F_sku jumps because `token_data` printed $250 is a **campaign/cluster note**, not S1 green.

Drop Virtuals ACP URLs (`virtuals.io`, `acp-x402`) from seller counts when using the services dump. Their 30d real USD still **includes** whatever x402watch called real on those hosts — F1 is not ACP-clean. That is a known bias; do not “fix” it with Codex.

---

## Green vs yellow (free desk)

- Daily scripts may emit **yellow** only (same as tripwire).
- **Green is forbidden** until a transfer-level sample (Dune, ≤3 queries) supports named sellers + breadth. Then it is still a *sample*, not a warehouse T3.
- If Allium or another paid ledger appears later, it is a new product decision — not the current path.

---

## What we will not build

- A private 402 indexer “because Allium is paid.” Public RPC at this tx rate is not free in practice (rate limits, Solana history).
- Daily Dune clones of agenteconomy query IDs.
- Daily OpenRouter Data API.
- Daily x402watch HTTP (use the CC0 dump; 60 req/h is for ad-hoc).
- LLM relabeling of the catalog.
- Publishing F1 30d real USD as Agent Economy GMV.
