# Agent Economy Monitoring Playbook

Version: 2026-09-03  
Audience: crypto / fintech investment desk  
Status: operating spec, not a forecast

This playbook exists to catch **real** agent-economy regime changes early enough to research them, without letting wash volume, meme mints, or token reflexivity page the desk.

It is built on a prior conclusion that still holds: **Agentic Commerce is two markets with two denominators.** Substitution (humans letting an agent shop) is a rules-and-trust problem. Creation (machines paying for APIs, data, compute, other agents) is a settlement-and-identity problem. Crypto captures the second market first. Monitoring must therefore be biased toward **machine settlement quality**, not toward “AI shopping” headlines.

---

## 0. Design thesis

Payment volume in the agent economy is a **Goodhart metric**. Facilitators sponsor gas, operators loop value through themselves, and a pay-to-mint meme can print tens of millions of “agent payments” in a week. Visa × Artemis already discarded ~89% of raw x402 dollar volume as wash or test as of April 2026. A later forensic census bounded genuinely independent named-service flow as low as the mid-six figures.

So the desk does not monitor “how hot is agentic.” It monitors four questions, in this order:

1. Did **independent buyers** pay **named sellers** for something that can be delivered?
2. Did the set of counterparties **broaden**, or did the same cluster just run harder?
3. Did an **off-chain demand** series (inference loops, SDKs, new SKUs) move with it?
4. Is there an **investable expression** (rail, stablecoin, facilitator, marketplace, equity) — or only a token?

A move that fails (1) is ignored. A move that passes (1) but fails (2) is logged as operator activity. A move that passes (1)+(2)+(3) is a research incident. Price is confirmatory, never the trigger.

---

## 1. What this desk refuses to treat as a signal

| Noise | Why it fools people | What we do instead |
| --- | --- | --- |
| Raw x402 tx count | Gas-subsidized, campaign-driven, Goodhart | USD volume after quality tiers T3/T4 |
| ERC-8004 registration count | Cheap identity NFTs, mostly spam mints | Reputation events that attach an x402 payment proof |
| Virtuals ACP memo count | A memo is a lifecycle step, not a sale | Unique counterparties + completed/settled jobs |
| Tempo MPP event count | Channel open/close dominate; settlements are rare | `Settled` events only, plus unique payees |
| Agent-token mcap / tweet volume | Attention market, not machine GDP | Use as *lagging* sentiment after a quality alert |
| Alipay “3亿笔” / closed-loop assistant GMV | In-garden shopping helpers, not open agent payment | Track only if a **cross-platform** payment appears |
| Consultant TAM ($200B–$5T) | Different denominators; all are mostly substitution | Ignore for sizing; use for narrative risk only |
| Unattributed chargeback “AI growth” | No public series yet tags disputes as agent-initiated | Watch for the **first** attributed series — that is the signal |

Worked false positive: **August 2026 x402**. Public monthly data shows ~17.9M txs versus ~4.8–6.0M in June/July, but only ~$437k of volume (avg ticket ≈ $0.024). Daily txs then printed 1.2M–1.9M on Aug 30–Sep 2 before collapsing. Under this playbook that is a **yellow tripwire at most**, and it fails the confirmation gate.

Worked structural tell: **Tempo MPP**. Cumulative ~45.7k events, but only **384 `Settled`**. Unique payees ≈ 90. Monitoring events would invent a market that does not exist. Monitoring `Settled` would not.

---

## 2. Coverage map: six radars, two clocks

The agent economy is not one time series. Keep native units. Never sum x402 settlements + ACP memos + 8004 mints into a single “agent GDP.”

```
Demand clock (leading)          Settlement clock (coincident)
OpenRouter tokens / agent apps  x402 T3/T4 USD
SDK downloads (x402, CDP)       Tempo MPP Settled
New named 402 endpoints         Virtuals completed jobs
                                USDC into agent wallets

Identity clock (lagging-quality) Rules clock (slow, high impact)
ERC-8004 reputation + proofs     Authorization revocation primitive
KYA directories (Visa/MA)        First agent-overreach judgment
                                 China convention enforcement
                                 AI liability insurance pricing
```

| Radar | Native unit | Primary KPI | Investable if it breaks |
| --- | --- | --- | --- |
| **R1 Demand** | tokens, apps, downloads | OpenRouter agent-app tokens; reasoning-model share | Inference routers, GPU, API gateways |
| **R2 Settlement quality (Layer 1 only)** | USDC | T3/T4 x402 USD vs MPP `Settled` USD vs L402 paid; unique payees; share among the three | USDC, Base/Solana/Tempo, facilitators |
| **R3 Identity** | reputation events | 8004 feedback with payment proof / unique operators | KYA, agent wallets, reputation graphs |
| **R4 Marketplace** | completed jobs | Virtuals unique senders + settled jobs, not memos | `VIRTUAL` only after quality, still reflexive |
| **R5 Rails / capital** | chain share, float | Adjusted-volume chain flip; USDC share of machine payments | SOL vs BASE, CIRCLE, COIN, Tempo |
| **R6 Rules / liability** | events | Revocation primitive; first attributed chargeback; court on *wrong purchase* | V / MA, licensed PSPs, insurers |

Crypto gets paid on R2–R5. Equities get paid on R5–R6. R1 is the earliest warning that R2 *might* follow. Token charts are not a radar.

---

## 3. Quality definition: the only GMV that matters

Quality tiers answer **who paid whom without washing**. They do **not** answer **whether the dollars were a service price or capital in transit**. Table 0 of the weekly pack is **Service Spend**, not “all quality USDC that touched an agent.”

| Economic type | Include in Service Spend? | Typical miss |
| --- | --- | --- |
| Named SKU / usage settlement (x402 T3, MPP `Settled` usage, L402 paid invoice) | Yes | — |
| Job escrow, trading notional, agent-wallet DEX size (ACP $500 to trade, $1 fee) | **No** — fee may be Service Spend; notional stays on the commerce board | Counting Allium `is_agent_economy_circulation` as GMV |
| Channel top-up, facilitator inventory, Gateway netting of already-counted spend | **No** | Double-counting Gateway + Base |

Circle Gateway is an overlay on a settlement network, not a sixth GMV venue. Repeat buyers are T4 / T3, never T0. SKU mix (inference / data / compute / other API) is a drill-down when the catalog has labels — not a second GMV.

On the **free desk**, T4/T3 are not computed daily. IC looks at F-proxies in [`data-cleaning.md`](data-cleaning.md) and must keep Unique Buyers / Repeat Rate **null** until a Dune sample exists. See [`weekly-cascade.md`](weekly-cascade.md).

### 3.1 x402 four-tier filter

T0–T4 are the **definition** of quality. They are not a daily feed on this desk (no Allium; Dune credits are rationed). Operating source: agenteconomy.to JSON + x402watch-data CC0 dumps. Dune is escalation only (`config/quota.yaml`).

Field meanings (Allium / any transfer-level warehouse — not used daily):

- `from_address` = buyer
- `to_address` = seller
- `transaction_from_address` = facilitator / relayer

| Tier | Definition | Use |
| --- | --- | --- |
| **T0 Raw** | Every labeled x402 transfer | Sanity check only |
| **T1 Hygiene** | Drop `from = to`, zero-value, self-pay / 24h return; hold ACP circulation out of Service Spend | Not computed daily on the free desk. Allium flags are paid-only. |
| **T2 Non-internal** | Drop closed loops and facilitator-cluster self-settlement (buyer and seller share a funder, or both are relayer EOAs) | Visa/Artemis-style adjusted |
| **T3 Named** | T2 **and** seller sits in `x402_servers` with a live origin / category | Lower bound of “someone sold a thing with a name” |
| **T4 Repeat** | T3 **and** buyer active on ≥3 distinct UTC days in trailing 30d, ≥5 T3 txs, not a facilitator EOA | Durable demand floor |

**Primary series the IC looks at:** T4 USD (7d and 30d) and T3 unique payees (7d).  
**Secondary:** T3 USD share of T2; top-1% buyer share of T2; facilitator HHI; chain share of T2 USD (not of T0 txs); ticket mix (`<$0.10`, `$0.10–1`, `$1–10`, `>$10`).

Extensive vs intensive:

- **Extensive (good):** unique T3 payers **and** unique T3 payees both rising with T3/T4 USD.
- **Intensive (not adoption):** T2/T3 USD rising while unique payers fall or top-1% share rises. That is a cluster running a batch job.

### 3.2 Other protocols: do not import x402’s unit

| Protocol | Count this | Do not count this |
| --- | --- | --- |
| Tempo MPP | `Settled` (+ `TopUp` as funding, separately) | `ChannelOpened` / `ChannelClosed` / `ChannelExpired` |
| Virtuals ACP | Unique senders, unique counterparties, jobs that reach a terminal settled state | Cumulative memos (12M+ is mostly history) |
| ERC-8004 | Reputation / validation events; fraction with payment proof; unique registrant EOAs | Total agents registered (548k+ is a mint metric) |
| Olas | Service / agent txs on live chains, unique operators | Headline weekly txs without operator concentration |
| USDC | Share of T2 x402; Circle Agent Stack **paid services** count; Arc agent-finance usage after mainnet | Circle’s $14T+ on-chain volume (that is trading + transfers) |

### 3.3 Snapshot contract

Every UTC day persist one row matching `schemas/daily_quality_snapshot.schema.json`. T3/T4 stay **null** (`quality_available: false`). Fill `free_proxy` from `scripts/free_quality_panel.py`. Do **not** backfill T3 from F1 or T0.

---

## 4. Confirmation gate: 2-of-3 before research time is spent

A **yellow** alert is a tripwire. A **green** alert is a research incident. Green requires **2 of these 3** on the same 7-day window, with at least one coming from R2 or R4 (on-chain settlement / marketplace), not from price:

1. **Quality:** T4 USD 7d z-score ≥ 2.0 **or** T3 named USD share of T2 jumps ≥ 10 percentage points.
2. **Breadth:** unique T3 payees 7d z-score ≥ 1.5 **and** unique T3 payers not falling. Top-1% buyer share of T2 must not be rising.
3. **Corroboration:** OpenRouter `cli-agent` / agent-harness app tokens 7d z ≥ 2.0, **or** ≥3 new named x402 origins that remain live 72h, **or** MPP `Settled` unique payees +30% WoW from a tiny base **with** T3 x402 also up.

Hard vetoes (alert dies even if 2-of-3 prints):

- T0 txs up ≥ 2× WoW while T2 USD up < 20%.
- New volume is >50% one facilitator **and** that facilitator’s buyers cluster to <20 EOAs.
- Token mcap of the agent basket up ≥ 30% 7d with T3/T4 USD unchanged.
- Catalog liveness (live 402 challenge / listed origins) falling.

Yellow (tripwire only): public T0 or agenteconomy.to daily txs z ≥ 3, or any single radar z ≥ 2.5, without the gate. Yellow pages a 15-minute scan, not a memo.

---

## 5. Alert catalog

IDs are stable. Thresholds live in `config/alert_rules.yaml`. Tune quarterly; do not retune because a token ripped.

### 5.1 Settlement (R2) — highest expected value

| ID | Name | Trigger | Why it matters | First research question |
| --- | --- | --- | --- | --- |
| S1 | Real demand pulse | T4 USD 7d z≥2.0 **and** unique T3 payees z≥1.5 | Independent machines paying named services | Which SKU categories? Inference / data / compute / A2A? |
| S2 | Supply appearance | New named origins ≥5 in 7d, still live at 72h, T3 USD >$1k combined | Seller side is what has not grown | Is this a real catalog or another mint/faucet? |
| S3 | Market broadening | Top-1% T2 buyer share −10pp over 14d while T2 USD flat or up | The article’s “dozens of back offices” thesis breaks | Can this still be a few institutions with more wallets? |
| S4 | Ticket-mix regime | `$1+` share of T2 USD +15pp in 30d, txs not required to rise | Category shift, not death (Nov-25 → 2026 already did this once) | Are we leaving micropay theater for real invoices? |
| S5 | Wash trap | T0 txs +100% WoW, T2 USD <+20% | Campaign / PING-class event | Do not write a bull memo. Map the campaign, then stop. |
| S6 | Facilitator dispersion | Facilitator HHI −0.08 in 14d and a new name ≥10% T2 USD | Infra rents may be spreading | Is the new name solvent, licensed, or a Sybil of an old one? |

### 5.2 Rails (R5)

| ID | Name | Trigger | Why it matters |
| --- | --- | --- | --- |
| C1 | Chain rotation | A non-leading chain holds ≥40% of **T2 USD** for 3 consecutive days | Settlement share, not tx share. Solana already flipped **daily txs** in Aug 2026; that is not enough. |
| C2 | Stablecoin break | USDC share of T2 x402 <95% for 7d | Machine reserve asset is no longer a monopoly. Size the substitute. |
| C3 | Wallet float | Identified agent-wallet USDC (CDP / Privy / 8004-linked) 7d z≥2.5 | L5 money is moving even if payments lag. |

### 5.3 Demand (R1)

| ID | Name | Trigger | Why it matters |
| --- | --- | --- | --- |
| D1 | Agent-loop inference | OpenRouter app rankings, `subcategory=cli-agent` (and named harnesses: Claude Code, OpenClaw, Codex, Kiro) 7d tokens z≥2.0 | Machines in a loop are the leading indicator for micropay |
| D2 | Reasoning mix | Reasoning models’ share of OpenRouter tokens +10pp in 30d | Longer loops → more tool calls → more paid endpoints |
| D3 | SDK pull-through | npm/PyPI weekly downloads for `x402`, CDP agent wallets, `@coinbase/agentkit` z≥2.5 | Developers, not speculators |

D-series alone is **never** green. It only upgrades an S-series yellow.

### 5.4 Identity & marketplace (R3, R4)

| ID | Name | Trigger |
| --- | --- | --- |
| I1 | Reputation with money | 8004 feedback events with payment proof 7d z≥2.0 and unique operators (not token IDs) z≥1.5 |
| I2 | Registration spam | 8004 daily mints z≥3 with I1 flat → ignore, optionally short reflexive agent-id tokens |
| M1 | ACP is becoming commerce | Unique ACP senders 7d +50% **and** memos/sender not exploding (anti-spam) |
| M2 | Memo theater | Memos +100% WoW, unique senders <+10% → ignore |

### 5.5 Rules (R6) — event-driven, no z-score

These are rare and usually more important than a volume spike.

| ID | Event | Research implication |
| --- | --- | --- |
| L1 | AP2 / ACP / TAP ships **clean revocation** of issued-but-unexecuted mandates | Substitution-side bottleneck starts to clear |
| L2 | First card-network chargeback series **attributed** to agents | Liability priced; insurance and TAP-compliant tokens re-rate |
| L3 | First court opinion on **wrongful purchase / ultra vires**, not CFAA access (Perplexity already answered access) | Legal vacuum starts to close |
| L4 | China convention enforcement action against a non-licensed agent payor | Closed-loop advantage vs open-loop risk |
| L5 | Circle Arc mainnet agent-finance usage after 2026-09-16 | New L5 venue; do not count testnet |
| L6 | AWS / Stripe / Coinbase change who holds keys on AgentCore-class products | L5 responsibility map moved |

### 5.6 Price overlay (never primary)

| ID | Rule |
| --- | --- |
| P1 | Agent-token basket +25% 7d **with** S1/S3/M1 → position sizing question, not discovery |
| P2 | Basket +25% 7d **without** T3/T4 confirmation → attention trade, desk does not “do agent research” |
| P3 | CIRCLE / COIN / MA gap vs basket: equities following quality, tokens following Twitter — trade the lag, don’t confuse it with thesis |

---

## 6. Data stack and cadence

This desk is **free-only**. Spec: [`data-cleaning.md`](data-cleaning.md). Quotas: [`config/quota.yaml`](../config/quota.yaml).

Short version: **do not buy a ledger; do not spend Dune daily; do not use Codex as a washer.** Consume published JSON/CC0 dumps. Own the interpretation. T3/T4 stay definitional until a capped Dune sample exists.

### 6.1 Sources (operating)

| Need | Source | Cost | Freshness |
| --- | --- | --- | --- |
| T0 pulse, MPP `Settled`, ACP memos/senders, 8004 mints | `https://agenteconomy.to/data.json` | Free (they spent the Dune credits) | Hourly |
| SKU mix, 30d real/wash, live catalog | GitHub `printmoneylab/x402watch-data` CC0 | Free raw/git | Daily ~04:00 UTC |
| SDK corroboration | npm download API for `x402` | Free | Weekly |
| Inference corroboration | [openrouter.ai/rankings](https://openrouter.ai/rankings) eyeball | Free page | Weekly |
| Wash-adjusted live (eyeball) | Artemis x402 terminal | Free page; outage-tolerant | Weekly |
| Catalog / facilitator floor | x402scan; Bazaar discovery; x402-list `/api/v1/facilitators` | Free; scan APIs may 402 | Weekly |
| Transfer-level sample | Our Dune, **only** on yellow/monthly | Credits, capped | Rare |
| Rules / markets | CourtListener, 公约, CoinGecko | Free | Event / real-time |

Do **not** daily: Allium, our Dune clones of their `queryId`s, OpenRouter Data API, x402watch HTTP (60 req/h). Optional paid SQL lives in `sql/optional_paid_allium_x402_quality_panel.sql` and is not scheduled.

### 6.2 Cadence

| Clock | Who | Output |
| --- | --- | --- |
| 06:30 UTC daily | `scripts/tripwire.py` + `scripts/free_quality_panel.py` | Snapshot JSON; **yellow only**; Dune queries = 0 |
| 08:00 local, 15 min | Analyst | Read yellow + 24h SKU mix; kill S5; **no green** |
| Weekly, 45 min | PM + analyst | F_sku trend, MPP Settled, ACP senders, npm, rankings page, **Artemis if up**, x402scan 30d vs T0, x402-list facilitator floor; tokens vs F-proxies |
| Monthly | IC | Thesis review; `scripts/audit_cleaners.py`; optional ≤2 Dune queries |
| Yellow escalation | Analyst | ≤3 Dune queries, then stop |
| Event | Anyone | L-series |

### 6.3 Tripwire vs quality

`scripts/tripwire.py` sees T0. `scripts/free_quality_panel.py` adds F-proxies. Both may emit **yellow**. Both are **forbidden to emit green**. Green needs a transfer-level sample under the Dune cap, plus the 2-of-3 gate. Codex is not part of this clock.

---

## 7. Escalation SOP (when a green alert fires)

Time-box. The edge is *earlier research*, not a longer Twitter thread.

**T+0 (30 min)**  
Classify: S1/S2/S3 vs S5. If S5, write a three-line “campaign note” and stop.  
On the free desk: read F_sku 24h mix + tripwire. If still unexplained, **at most 3 Dune queries** for top payees/payers (see `config/quota.yaml`). Do not ask Codex to invent T3.  
Check vetoes.

**T+4h**  
SKU map: is this inference, data, compute, content, or A2A subcontracting?  
New origins: live 402 challenge? Human-readable product? Price list?  
Breadth: wallet clustering (shared funder) — if 20 payers collapse to 3 clusters, demote to yellow.  
Corroboration: OpenRouter apps, SDK, Circle/AWS changelog.

**T+24h**  
Investable expression (pick one primary):

| If the break is… | Expression | Do not express via |
| --- | --- | --- |
| Named API/compute SKUs on Base/Solana | USDC float / CIRCLE, COIN (Base + CDP wallets), SOL if C1 on **T2 USD** | Random agent ERC-20s |
| Facilitator rents spreading or concentrating | The facilitator’s token/equity if any; otherwise infrastructure names | x402 “protocol token” (there isn’t a rent-bearing one) |
| Virtuals completed jobs + unique counterparties | `VIRTUAL`, small, with a kill if M2 returns | Every agent token that pairs to VIRTUAL |
| Identity/reputation with payment proofs | Agent-wallet / KYA names | 8004 mint coins |
| Rules (L1–L4) | V / MA / licensed PSPs / insurers | On-chain beta |

**T+72h**  
Two-page memo, fixed headings: what changed; quality vs wash; durability (would it survive gas no longer being sponsored?); expression and size; **kill criteria**; what would make us increase.

If no expression exists, that is an acceptable outcome. Log “watched, uninvestable” so the desk does not keep rediscovering it.

---

## 8. How the desk is allowed to get paid

Picks and shovels, in order of how cleanly they map to a real S1:

1. **Reserve asset and L5:** USDC, Circle Agent Stack, Coinbase CDP / Privy-class agent wallets. These sit on the money.
2. **Blockspace that actually settles T2 USD:** Base first historically; Solana only after C1 on quality volume, not on tx count.
3. **Facilitators and merchant catalogs:** where take-rate can appear. Treat concentration as both a risk and a moat.
4. **Marketplace coordination:** `VIRTUAL` is the cleanest public-crypto expression of agent *launch + routing*, and also the most reflexive. Size as a satellite, not the core book.
5. **Authorization / liability (traditional finance):** Visa as authorization infrastructure, Mastercard as multi-rail settlement + BVNK, Stripe as execution. These move on L-series and on substitution, not on x402 tweets.

Core book vs satellite: core is (1)+(2)+L5 equities. Satellite is (4) and long-tail agent tokens. Long-tail tokens are not a monitoring input; they are a *downstream bet* after S1/M1.

---

## 9. Kill criteria / thesis invalidation

Stop treating “agent economy” as a live crypto book if any of these hold for 90 days:

- T4 USD 30d below $50k and unique T3 payees 30d below 50 (demand never graduated from operator clusters).
- T0 remains the only series that can be made to look like growth (permanent Goodhart).
- USDC share of T2 stays high but **all** of T2 is still facilitator-internal — rails without customers.
- Substitution (human shopping) captures machine micropay via credits/wallets and never touches public settlement.
- A major L5 holder (AWS / Stripe / Coinbase) internally nets agent spend so that on-chain 402 becomes an implementation detail with no surplus for public crypto.

None of these are predicted. They are the off switches.

---

## 10. Daily analyst checklist (print this)

- [ ] T3/T4 USD 7d vs 30d trend (not T0 txs)
- [ ] Unique T3 payers / payees; top-1% share; facilitator HHI
- [ ] Ticket mix; avg ticket on T2 (Aug-26 style collapse = campaign)
- [ ] Chain share of **T2 USD**
- [ ] New named origins still live?
- [ ] OpenRouter cli-agent / harness tokens
- [ ] MPP `Settled` (ignore opens)
- [ ] ACP unique senders (ignore memo spikes)
- [ ] 8004 reputation-with-proof (ignore mint spikes)
- [ ] Any L-series headline?
- [ ] Did tokens already move? If yes, we are late unless quality just printed

If every box is “unchanged,” do not produce commentary. Silence is a feature.
