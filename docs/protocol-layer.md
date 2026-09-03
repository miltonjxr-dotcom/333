# Protocol monitoring by layer

A watchlist is only valid if every row is a peer: same job, comparable unit.
Do not put ERC-8004 next to x402. Do not add Virtuals ACP into the payment-protocol board.

## Layer 1 — Payment / settlement protocols (the crypto daily board)

Question these protocols all answer: **how does the machine actually move money after it has decided to pay?**

| Protocol | Settlement style | Asset | Production weight (2026-09) | Native unit to compare |
| --- | --- | --- | --- | --- |
| **x402** | Per-request on-chain (HTTP 402) | USDC on Base/Solana/etc. | Dominant | T3/T4 USD, unique payees |
| **MPP** | Session / channel, batch `Settled` | USDC on Tempo + fiat SPT + Lightning ext. | Early | `Settled` USD, unique payees |
| **L402** | Per-request, Lightning invoice + macaroon | BTC sats | Older, smaller agent footprint | Paid invoices / sats, unique payees |

These three can share one dashboard. Convert everything to **USD received by independent sellers**. Never compare x402 raw txs to MPP `ChannelOpened` or L402 challenge counts.

Not on this board yet (same *idea*, no durable volume):

- s402, U402, v402 — HTTP-402 forks / supersets, specs exist, not a second GMV series
- IETF `draft-httpauth-payment` — wire-format politics, weekly
- lobster.cash — OpenClaw-specific envelope on existing rails

Masumi escrow is **not** this layer (it is job+escrow, closer to Virtuals ACP).

Comparable KPIs for Layer 1 only:

1. Quality USD (x402 T3/T4 vs MPP Settled vs L402 paid)
2. Unique payees (breadth)
3. Average ticket / mix
4. Share of machine-payment USD (x402 vs MPP vs L402)
5. Rail (Base / Solana / Tempo / Lightning) — **settlement network**, GMV once
6. Repeat buyer rate (T4 buyers / T3 buyers), not raw-tx repeat
7. Circle Gateway as **% of that rail’s Service Spend that was netted**, never as a fourth protocol or a sixth chain

## Other layers — each gets its own board

### Layer 0 — Identity / trust

Peers: ERC-8004, Visa TAP / Agent Directory, Mastercard KYA-style agent identity.
Unit: identifiable agents that later *pay*, not NFT mints.

### Layer 2 — Authorization

Peers: Google AP2 mandates, OpenAI ACP allowances, Mastercard Verifiable Intent.
Unit: issued / revoked / executed mandates. A2A×x402 is an **adapter** from this layer into Layer 1 — count it as “x402 with mandate metadata”, never as a fourth payment protocol.

### Layer 3 — Commerce / job orchestration

Peers: Virtuals ACP, UCP, OpenAI ACP (checkout), Masumi jobs.
Unit: completed jobs / checkouts with funds released, not memos.

Run Layer 1 daily. Run 0 / 2 / 3 on their own cadence. A green alert is intra-layer (MPP taking USD share from x402). Cross-layer coincidence is corroboration, not a summed GMV.
