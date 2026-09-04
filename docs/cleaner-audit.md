# How to audit third-party cleaners (free desk)

You cannot “confirm” that a website’s GMV is T3 Service Spend without a transfer-level ledger. What you *can* do, for $0 plus at most one Dune sample a month, is **score each source on the claim it actually makes**.

A dashboard `real_volume_pct = 88%` is not evidence. It is the vendor’s own denominator.

```
Ground truth (high → low)
  1. On-chain sample: this tx is 402, self-pay or not, named payee or not
  2. Live HTTP resource behind a catalog row
  3. Campaign backtest (Aug 2026): did “cleaned USD” follow the junk tx spike?
  4. Published forensics (Visa×Artemis, Ling et al.) as a *scale* check
  5. Cross-source divergence (inconsistency ≠ truth, but kills a series)
  6. Vendor self-reported organic %  ← not evidence
```

Codex is not an auditor. Relabeling 34k endpoints with a model reproduces x402watch’s error class.

Run: `python3 scripts/audit_cleaners.py` (no Dune, no API keys). Monthly, or after a yellow.

---

## Score each site for a different job

| Source | Its actual claim | Audit that claim | Do not audit as |
| --- | --- | --- | --- |
| **agenteconomy.to** | “Here is Dune T0 + MPP event types + ACP memos” | Decode coverage, freshness, **units** (`Settled` vs events), sample vs universe (read `meta.queries` / `tokenSplit.note`) | A washer. It mostly isn’t one. |
| **x402watch-data** | “Here is real vs wash under *our* 9 labels” | Tightness vs forensics, **stability** of real USD through a known campaign, residual `organic_user`, SKU concentration, catalog liveness | T3/T4 Service Spend |
| **Dune dashboards** (chriscen / hashed) | Same as agenteconomy if that JSON is their output | Don’t re-run. Check `lastCostCredits` and `executedAt`. If the JSON lags, the dashboard lags. | Independent confirmation of x402watch |
| **Visa×Artemis / Ling et al.** | One-time forensic census | Use as **benchmark**, not a live series | Today’s GMV |

---

## Tests (all free except D6)

### A. Unit hygiene (agenteconomy / MPP)

- MPP: `Settled / totalEvents`. If the site charts events, it fails. If it *exposes* `byType.Settled` so we can ignore the rest, it **passes as a feed**, even if the UI is noisy.
- ACP: memos vs unique senders. Memo-only headline fails.
- x402: ticket = vol/txs. Collapse + tx spike = campaign (S5), not a cleaner failure on T0 — T0 is supposed to show junk.

### B. Coverage / universe mismatch

If two numbers from the *same* JSON imply different universes, neither is “the market.”

Worked: 2026-09-03 `x402.tokenSplit.totalPayments` = **46,783** (note: trailing 30d, Base, live facilitator registry) while August T0 txs = **17.9M**. The 98.46% USDC share is a **restricted sample**, not economy-wide. That is an accuracy finding about *scope*, not about USDC.

### C. Campaign backtest (x402watch vs T0) — the important free test

August 2026 is labeled junk in our playbook: txs ~3× July, USD only ~1.8×, ticket $0.040 → $0.025.

Pull CC0 `buyer-labels-YYYY-MM-DD.json` `real_vs_wash_30d`:

| If through the campaign… | Verdict on x402watch as GMV |
| --- | --- |
| 30d **real USD** tracks T0 **txs** | Fail — followed Goodhart |
| real USD tracks T0 **USD** or stays flat/down at the tx peak | Pass on *tx* inflation; still not T3 |
| **wash USD collapses** and real USD jumps a few days later | Fail **stability** — labels were reclassified, not a market |

This is cheaper and more honest than arguing about their methodology PDF.

### D. Tightness vs published forensics

Same window is impossible; we only check **order of magnitude**.

| Benchmark | Keep-rate (USD) | Implication |
| --- | --- | --- |
| Visa×Artemis ~2026-04 | adj ~$15M / raw ~$135.7M ≈ **11%** | Serious washer |
| Ling et al. Base 280d named floor | ~$188k / $44.1M ≈ **0.4%** | Named independent floor |
| Ling C3 ceiling | ~$20.3M / $44.1M ≈ **46%** | Not-provably-fake upper |
| x402watch `real / total` on a 30d dump | often **75–90%** | Product bias: false negatives. **Unsuitable as 表 0** |

If F1 keep-rate stays in the 80s while forensics sit at 11% or 0.4%, the site is not “wrong about its own labels”; it is **wrong as a proxy for Service Spend**.

### E. Residual class (x402watch buyers)

`organic_user` is the default when signals don’t fire. If it is **>90% of buyers**, Unique Buyers derived from that file is meaningless. That is an accuracy finding on **breadth KPIs**, not on USD.

### F. Catalog liveness (SKU / sellers)

Sample ~8 non-placeholder `resource_url`s with `last_seen` in 7d. HEAD/GET, 5s timeout. A named live 402 endpoint supports the *directory*. It does **not** prove the USD next to that row is independent demand.

### G. Optional Dune sample (≤1 query, monthly)

Do **not** clone agenteconomy `queryId`s. Write a **narrow** query: 7-day window, one chain, top 20 `to_address` by USD, plus `from=to` share.

Hand-label those 20: named API / ACP / unknown / self-pay. Compare to x402watch catalog category for the same seller. That audits **head of the distribution**, not the tail that dominates tx count.

---

## What “accurate enough” means for this desk

| We need | Accurate enough if | Kill the series if |
| --- | --- | --- |
| T0 tripwire | agenteconomy daily txs/vol move with public Dune charts | JSON `executedAt` stale >48h or ticket math breaks |
| MPP | `Settled` present and ≪ events | Only `ChannelOpened` is shown |
| SKU mix (表 2b) | 24h category USD exists; top-1 share is visible | We treat 24h $325 as machine GDP |
| 表 0 Service Spend | Transfer sample or T3 | x402watch 30d real USD or T0 vol |
| Repeat / unique buyers | Buyer×day panel | `organic_user` headcount |

---

## Script output

`scripts/audit_cleaners.py` emits the scorecard. It does not mint a single “accuracy %”. A cleaner can pass MPP units and fail tightness in the same run — that is the correct report.
