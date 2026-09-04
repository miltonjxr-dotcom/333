# Source landscape — who counts the agent economy

There is no single authoritative “agent economy website.” The denominator disagrees by **three orders of magnitude** (Visa×Artemis adjusted ~$15M vs raw ~$136M vs named-service floor ~$0.19M). Adding more dashboards without assigning each a **job** just reprints T0.

Filter used here: **free**, **schema-stable or eyeball-cheap**, **does not burn Dune/Codex**, **does not get summed into 表 0**.

Live cross-check 2026-09-03 (do not freeze as targets):

| Lens | Window | Tx / USD | What it is |
| --- | --- | --- | --- |
| agenteconomy T0 | cumulative | 181.2M / $41.6M | Dune facilitator-attributed raw |
| agenteconomy T0 | Aug 2026 | 17.9M / $437k | Campaign month |
| x402scan | trailing 30d | 24.95M / $1.44M | Indexer; registered/discovered sellers |
| x402watch F1 | trailing 30d | — / $709k “real” | Loose washer (crawlers in) |
| x402-list facilitators | trailing 30d USDC | Coinbase settler $661k alone | Settler-address floor, not GMV |
| DefiLlama x402 | 30d / cumulative | — / $1.11M · $32.9M | Mis-tagged as “DEX volume” |
| Visa×Artemis adj. | May 2025–2026-04-21 | 109.6M / $15.0M | Best public **adjusted** snapshot |
| Ling et al. named floor | Base 280d | — / ~$188k | Forensic lower bound |

x402scan 30d featured: BlockRun ~15.9M txs / ~$207k on Solana — **tx share ≠ Service Spend**. That is the Goodhart pattern in a catalog.

---

## Keep (operating)

### Daily — already wired

| Source | URL | Job | Not |
| --- | --- | --- | --- |
| **agenteconomy.to** | `https://agenteconomy.to/data.json` | T0 pulse; MPP `Settled`; ACP senders; 8004 mints; **already-run** Dune (`hashed`, `thechriscen`, `ax1research`, …) | Washer; 表 0 |
| **x402watch-data** | GitHub CC0 daily dump | 24h SKU mix; their real/wash (F1, too loose); live catalog rows | T3 GMV |

Do **not** clone those Dune `queryId`s. The JSON is the free extract.

### Weekly eyeball (no extra Dune)

| Source | URL | Job | Caveat |
| --- | --- | --- | --- |
| **Artemis Agentic Payments (canonical)** | [`https://www.artemis.ai/sectors/agentic-payments`](https://www.artemis.ai/sectors/agentic-payments) | **Weekly #1 wash-adjusted eyeball.** Same Visa-partnered heuristics as the Apr-2026 report. Charts: Real vs Gamed (x402+MPP), unique merchants, USDC mix, **adjusted** volume by chain / facilitator / **category**, and **MPP by payment type** (the public version of our `Settled` vs channel split). | Charts are JS-rendered — **no public JSON dump**, so not a daily job. Heuristics proprietary (self-deal / test; a cited seller rule is ≥3 adjusted txs from ≥2 unique buyers). **Not T3** and not Service Spend. Headline “cumulative transactions across x402 and MPP” **mixes units** — read the protocol breakdown, don’t quote the combined count. Sibling asset page `app.artemisanalytics.com/asset/x402` is the same family; it 502’d on 2026-09-03 — **use this sector URL first**. Snowflake share is paid. |
| **Visa × Artemis report** | Visa thought-leadership PDF | Calibration of keep-rate (~89% of raw USD dropped as of 2026-04-21) | Not a daily API |
| **x402scan** (Merit) | `https://www.x402scan.com` | Seller/facilitator **directory** + raw indexed 30d; who is in the Bazaar | Mixed windows (30d vs “24h”); HTTP APIs often **402**; not wash-adjusted. Home 30d $1.44M vs T0 $41.6M cumulative is coverage, not “truth.” |
| **Coinbase Bazaar / CDP discovery** | `https://api.cdp.coinbase.com/platform/v2/x402/discovery/resources` | Upstream **named catalog** (T3 join key if we ever sample) | Discovery ≠ settlement quality |
| **x402-list.com** | `https://x402-list.com/api/v1/facilitators` | Facilitator **USDC settler-address** 7d/30d floor (CC BY 4.0); table 5 rents | Self-described **floor, not ecosystem total**. Virtuals all-time ~$3.0M on their settler is **ACP-shaped**, not Service Spend. 24h fields are UTC-day-so-far, not trailing 24h. |
| **npm `x402`** | npm download API | D3 developer funnel | CI noise |
| **OpenRouter rankings** | `https://openrouter.ai/rankings` | D1 eyeball | No daily Data API |

### Monthly / escalation

| Source | Job |
| --- | --- |
| Ling et al. arXiv:2607.12575 | Named-floor vs C3 ceiling |
| `scripts/audit_cleaners.py` | Score **our** two daily feeds |
| Optional 1 Dune sample | Top 20 payees, 7d, one chain — not a new dashboard |

---

## Do not add to the weekly pack

| Source | Why drop |
| --- | --- |
| Extra **Dune** boards (`hashed_official/x402-analytics`, `thechriscen/x402-payment-analytics`, `dune/x402-facilitators`, `ax1research` Base agentic, `adrian0x`, …) | Same T0 family as agenteconomy. Facilitator address lists **go stale** (Gökhan: community catalogs ~10% of x402scan volume). Each refresh burns credits. |
| **x402.org** “Last 30 Days” | Documented as **hard-coded static HTML** (~2026-06-24), not a live counter. Most-quoted junk denominator. |
| **DefiLlama `/protocol/x402`** | Volume-only adapter; UI calls it DEX volume. Useful as a *third T0-ish* number, not a washer. Don’t weekly unless Artemis is down *and* T0 jumped. |
| **PayAI / Dexter / BlockRun / Heurist own stats** | Issuer. BlockRun can be 80%+ of indexed txs. |
| **OrbitX402, x402scout, 402utils, agent-exchange catalogs** | Directories or **paid** x402 APIs. Don’t pay to measure. |
| **ChainWard** | Base agent-wallet / ACP labels, not Layer-1 GMV |
| **8004scan / ERC-8004 mint boards** | Identity mints; already ignore as GMV |
| **Allium agents tables** | Paid warehouse — out of scope |
| **x402gle / Dexter wash explorer** | Interesting method (~93% wash cited Jul-2026); not a stable free dump like x402watch-data |
| **Gökhan live JSON** | Research pipeline on Dune (~22 credits/day in *their* budget). Don’t fork. Read the memo; don’t ingest as a second T0. |
| Second “x402scan” (ACHIVX / other MCP wrappers) | Name collision. Merit `x402scan.com` is the explorer. Don’t mix. |

---

## Authority is per question

| Question | First source | Second source | Never |
| --- | --- | --- | --- |
| Did T0 explode (campaign)? | agenteconomy daily txs + ticket | x402scan 30d txs vs USD | x402.org static 30d |
| Is wash-adjusted USD moving? | [Artemis sector page](https://www.artemis.ai/sectors/agentic-payments) | Visa report + our F1 as *loose* check | Combined x402+MPP tx count; summing Dune + scan + list |
| What did 24h dollars buy? | x402watch category dump | x402scan featured sellers (qualitative) | Facilitator volume |
| Who takes facilitator rent? | x402-list settler 30d | x402scan facilitator page | T0 tx share |
| Is the seller real/live? | Bazaar + x402scan + HTTP 402 probe | x402-list provenance (`imported:bazaar`) | 8004 mints |
| MPP / ACP / 8004 | agenteconomy native units | — | Mixing with x402 USD |
| Independent named Service Spend | Still **not published live** | Dune sample of named payees | Any homepage total |

**Rule:** same number from three sites that all sit on facilitator allowlists is **one** measurement, echoed. x402-list vs hashed Dune vs scan can **diverge on purpose** (settler floor vs stale registry vs discovered sellers). Divergence is a coverage signal, not a third GMV.

---

## What we will not do

- Daily scrape of Artemis / x402scan / DefiLlama (no stable public dump comparable to x402watch-data; scan APIs 402).
- Sum Coinbase $661k (list) + scan $1.44M + watch $709k into “quality USD.”
- Treat DefiLlama or scan 30d as Artemis-adjusted.
- Add another Dune dashboard because it looks official.
