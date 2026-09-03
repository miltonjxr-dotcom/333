# Protocol-layer watchlist (crypto desk)

Names collide. This file is the canonical mapping for the monitor.

## Three different things called "ACP"

| Acronym | Full name | Owner | Layer | On this desk? |
| --- | --- | --- | --- | --- |
| **ACP (Virtuals)** | Agent Commerce Protocol | Virtuals Protocol | On-chain A2A job / escrow / memo | **P1 daily** |
| **ACP (OpenAI)** | Agentic Commerce Protocol | OpenAI + Stripe + Meta | Off-chain merchant checkout | P2 weekly spec |
| ACP (IBM, historical) | Agent Communication Protocol | IBM → merged into A2A | Messaging | Ignore |

**AP2 is not Virtuals.** AP2 = Google Agent Payments Protocol (authorization mandates, now at FIDO).

Virtuals ACP v2 (Apr 2026) also claims to be the reference implementation of **ERC-8183** (proposed Ethereum standard for agent commerce). Monitor the on-chain jobs, not the ERC number.

## Layers (compose, do not pick a winner)

```
Identity / trust     ERC-8004, Visa TAP, Mastercard Verifiable Intent
Authorization        Google AP2 (mandates), ACP-OpenAI allowances
Commerce / checkout  UCP, ACP-OpenAI, Virtuals ACP (jobs)
Settlement           x402, MPP (Stripe/Tempo)
Transport / tools    MCP, A2A          ← not payment; do not page on these
```

An agent can use AP2 to prove permission, Virtuals ACP or UCP to negotiate the job, and x402 or MPP to move USDC. Volume on one layer is not volume on another.

## P1 — daily, on-chain (this is the crypto book)

| Protocol | Native unit to count | Kill-noise rule | Why it is on the book |
| --- | --- | --- | --- |
| **x402** | T3/T4 USDC, not raw txs | Wash trap S5 | Only HTTP-native stablecoin rail with scale |
| **Virtuals ACP** | Unique counterparties + terminal jobs / escrow releases | Ignore memo spikes (M2) | Only public A2A commerce runtime with a token (`VIRTUAL`) |
| **MPP** | `Settled` (+ unique payees) | Ignore ChannelOpened | Stripe/Tempo session rail; 384 Settled vs 45k events as of 2026-09-03 |
| **ERC-8004** | Reputation/validation with payment proof | Ignore registration mints | Identity that can bind to x402 proofs |
| **A2A x402 extension** | x402 txs that carry AP2 mandate metadata, if labeled | If unlabeled, it is just x402 | Bridge from Google authorization into crypto settlement |

## P2 — weekly spec / adoption (moves equities and standards, rarely tokens)

| Protocol | Watch for | Expression |
| --- | --- | --- |
| **Google AP2** | Revocation of issued-but-unexecuted mandates; mandate volume if any public telemetry | V/MA/UCP stack, not a token |
| **UCP** | Merchant / Shopify adoption vs ACP-OpenAI | Substitution-side checkout standard |
| **ACP (OpenAI/Stripe)** | Instant Checkout share; MoR language; 4% take | OpenAI/Stripe, not crypto GMV |
| **Visa TAP** | Agent directory, agent score, TAP-compliant dispute shift | Visa |
| **Mastercard Verifiable Intent** | Intent-bundle in disputes; BVNK settlement overlap | MA |
| **ERC-8183** | If it becomes the canonical job/escrow ABI beyond Virtuals | Then ACP-Virtuals is a vendor, not the standard |

## P3 — event only

Alipay ACT / AHA (closed loop), Circle Agent Stack / Arc, Rain Agentic Payments Alliance notes, China 自律公约 enforcement.

## Do not put on the payment-protocol board

MCP (tools), A2A core (messaging), Olas (agent network, not a payment standard), Masumi (Cardano escrow, too small unless T3-equivalent USD appears).
