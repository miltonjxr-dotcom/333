# Data cleaning: buy extraction, own the denominator

Question: call a website’s “cleaned” GMV, or build a private washer?

**Neither.** Buy the *ledger*. Own *Service Spend*. Public dashboards are tripwires. Vendor “organic” flags are T1 hygiene, not 表 0.

```
Buy                          Own (this desk)
──────────────────────────   ────────────────────────────────────
Chain extract / 402 decode   Economic type: Service vs notional vs plumbing
Facilitator + server names   T2 cluster / closed-loop beyond 24h A↔B
T1: self-pay, 24h return     T3 named live catalog ∩ Service Spend
SKU / category *labels*      T4 repeat on T3 (not on T0)
MPP event dump               `Settled` only; fee vs escrow on ACP
                             Gateway as overlay %, GMV once
```

Do **not** stand up a private x402 indexer on day one. Allium already decoded transfers and tagged facilitators/servers. Engineering time goes to T2–T4, Service Spend stamps, and alerts — not to re-parsing HTTP 402 logs.

---

## Why a website number cannot be 表 0

Every public cleaner answers a *different* question, and none of them is “independent machines paid a service price.”

| Source | What it actually filters | Headline you will see | Use | Forbidden |
| --- | --- | --- | --- | --- |
| **agenteconomy.to** / most Dune | Little or nothing (T0) | Tx count, raw USD | Yellow tripwire (`scripts/tripwire.py`) | Green; 表 0 |
| **Allium `x402_transfers_adjusted` `WHERE NOT is_inorganic`** | Self-pay **or** proportional stablecoin return within 24h; **Virtuals ACP is carved back in** as `is_agent_economy_circulation` | “Organic x402” | **T1 input** | Treat as Service Spend. ACP $500 notional survives this gate on purpose. High-frequency buyers and A→B→C rings are **deliberately unflagged**. |
| **x402watch `real_volume`** | Pair labels; `ai_agent` / `organic_user` / even `analytics_bot` and `verifier` count as “real”; bias to false negatives | ~74% “real volume” (dashboard, 2026-08) | Seller/SKU labels; wash *suspects* | 表 0. Looser than Visa×Artemis (~11% of raw USD kept, Apr-2026 snapshot) and far looser than Ling et al. named-service floor. |
| **Visa × Artemis adjusted** | Research snapshot, not a daily API | ~$15M / 109.6M vs raw ~$135.7M / 178.3M (as of ~2026-04-21) | Calibration / cite | Production series. Do **not** import Visa Onchain Analytics’ *general* adjusted-volume rule (drop addresses with >1000 txs or >$10M / 30d) — that rule is for DEX wash and **kills legitimate x402 micropay**. |
| **Ling et al. arXiv:2607.12575** | C1 fictitious / C2 cluster-internal / C3 unattributed; named-catalog floor vs ceiling | Base 280d: 136.7M settlements / $44.1M; ~21% C1, ~64% C2, ~15% C3; named floor ~$188k vs ceiling ~$20.3M | Gold **methodology** | Not a feed. Pipeline promised post-publication; still not a desk SLA. |

The gap is the point: **T1 “organic” can still be 70%+ of raw, while independent named Service Spend can be mid-six figures.** Calling any one website is choosing their denominator, not ours.

Allium’s own docs: high-frequency buyers are the intended x402 pattern; triangular wash is unflagged. That is correct for a *vendor hygiene flag* and insufficient for an *IC GMV*.

---

## Rule by layer (make vs buy)

### Buy: extraction and names

| Buy this | From | Why not DIY |
| --- | --- | --- |
| Every x402 transfer + USD | Allium `crosschain.agents.x402_transfers` (and `_adjusted`) | Decoding 402 across Base/Solana is a data-vendor job. |
| Facilitator roster | `x402_facilitators` | Shared industry list; 15-of-15 agreement with x402scan on Solana fee-payers in the paper. |
| Seller catalog (origin, category) | `x402_servers` + x402watch / x402scan **as labels** | Catalog is a directory problem. We join it; we do not scrape it into GMV. |
| Inference corroboration | OpenRouter Data API | Off-chain demand clock; not settlement. |
| Public T0 pulse | agenteconomy.to `data.json` | Cheap yellow. Already wired. |

If Allium is down: **leave quality fields null** (`quality_available: false`). Do not substitute x402watch `real_volume` or Dune raw into 表 0.

### Own: the investment definition

These are not on any vendor dashboard. This is the washer.

1. **Economic type stamp** (required before sum)  
   - Drop `is_agent_economy_circulation` from Service Spend (ACP notional/treasury loops).  
   - MPP: `Settled` usage only; `TopUp` / `ChannelOpened` = plumbing.  
   - ACP board: fee vs escrow, never unified.  
   - Gateway: overlay % on a settlement network, GMV once.

2. **T2 non-internal** on top of Allium T1  
   Drop facilitator-EOA as buyer or seller; later: shared-funder clustering. Allium will not do this for you.

3. **T3 named ∩ live catalog ∩ Service Spend**  
   Join servers with a live origin. Category from vendor is a *label* for 表 2b, not a second GMV.

4. **T4 repeat** = T3 buyer, ≥3 UTC days / 30d, ≥5 T3 txs, not facilitator EOA.  
   Never compute repeat on T0 or on x402watch `ai_agent`.

5. **Units for non-x402**  
   MPP and L402 have no Allium T3. Own the event filter even if the *feed* is public.

### Borrow, do not crown: x402watch

Use it for:

- Category / SKU hints when 表 0 moved (表 2b).
- `suspected_wash` / `self_test` as **extra T2 suspects** (OR with our cluster filter).
- Dispute that a named seller is a farm.

Do not use `real_volume_pct` as Service Spend. Their “real” includes crawlers and analytics bots by design (false-negative bias). That is a product choice for ranking *services*, not for sizing an economy.

---

## Production path (x402)

```
x402_transfers                         → T0 sanity (never publish)
     │
x402_transfers_adjusted
  NOT is_inorganic
  NOT is_agent_economy_circulation     → T1 hygiene, ACP held out of 表 0
     │
drop facilitator EOA as buyer/seller   → T2
     │
inner join live named servers          → T3 Service Spend
     │
repeat-buyer window                    → T4 floor
```

SQL: [`sql/allium_x402_quality_panel.sql`](../sql/allium_x402_quality_panel.sql).

When T3 USD and Allium “organic” USD diverge, **believe T3**. The wedge is C2 clusters + ACP circulation + unnamed servers — exactly what 表 0 is supposed to refuse.

---

## What we will not build

- A second 402 log indexer “because we don’t trust Allium decode.” Trust-but-verify a sample of tx hashes against an explorer; do not re-extract the chain.
- A weekly job that publishes x402watch or agenteconomy USD as GMV “until Allium lands.”
- Visa-style whale filters on micropay.
- Summing Dune ACP memos + x402 organic + 8004 mints into “agent GDP.”

Build later only if: Allium T1 misses a wash class that hits 表 0 for two consecutive weeks, **and** we can specify the rule in SQL on Allium rows (cluster funder, ring, Gateway double-count). That is still “own the filter,” not “own the chain.”
