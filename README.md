# x402 protocol settlement snapshot

Protocol-level x402 / MPP counts only (not DEX or raw chain traffic).

Snapshot date: **2026-09-08**. Compiled file: `data/x402-snapshot-2026-09-08.json`.

## What was measured

- **Main market:** [agenteconomy.to/data.json](https://agenteconomy.to/data.json) — Dune facilitator-attributed x402 settlements.
- **MPP:** same dump, Tempo channel events (not 1 API call = 1 tx).
- **Robinhood (`eip155:4663`):** not in Dune / Artemis / x402scan / CDP / PayAI. Counted on-chain via the x402 Exact Permit2 proxy and facilitator relayers.

x402scan’s own stats API returns HTTP 402, so it was not used as a bulk source.

## Cumulative x402 by chain (indexed, table as-of 2026-08-19)

| Chain | Txs | Share of indexed table |
| --- | ---: | ---: |
| Base | 84,969,790 | 51.65% |
| Solana | 48,235,859 | 29.32% |
| Polygon | 29,472,684 | 17.92% |
| BNB | 910,185 | 0.55% |
| Celo | 760,020 | 0.46% |
| Other 7 chains | 162,442 | 0.10% |

Total txs on 2026-09-08: **185,851,240** ($41.7M). About **21.3M txs after 2026-08-19 are not allocated by chain** in this table.

Sep 1–7 indexed x402 txs: **7,766,212**.

## Robinhood

Not in the table above. Native scan:

- Canopy official relayer: 21 all-time settlements, last pay **2026-07-13**, discovery `calls7d = 0`.
- Unlisted Exact-proxy settler `0xc231248d…`: **11,750** address txs; 49/50 latest proxy `settle()` calls are USDG ($0.38 in that page).
- Does not change the Base / Solana / Polygon ranking.

Refresh public JSON with `python3 scripts/fetch_x402_snapshot.py`.
