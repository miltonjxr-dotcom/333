# Weekly cascade: large categories → smaller tables

Monitor top-down. A lower table is opened only if the table above moved, or once a week as a 10-minute scan.
Never mix rows that answer different questions.

This file is the weekly pack. Quality definitions live in [`agent-economy-monitoring-playbook.md`](agent-economy-monitoring-playbook.md). Free-desk sources and Dune/Codex caps: [`data-cleaning.md`](data-cleaning.md).

**Fill 表 0 automatically:** `python3 scripts/weekly_pack.py`. Do not build a Dune dashboard. The leftover is ~10 minutes on pages with no JSON dump (Artemis, OpenRouter).

---

## Review of the four-point critique (keep / change / reject)

An external review scored this cascade ~8/10 and asked for four changes. Verdict: **keep the spine; do not add tables; fix the denominator.** Point-by-point:

| # | Claim | Verdict | Why |
| --- | --- | --- | --- |
| 1 | 表 0 不要只看「总质量美元」；拆 **Service Spend** vs **资金划转/交易本金** | **Accept, and tighten.** This is the highest-value fix. ACP “trade $500, fee $1” must never print as $500 Agent Economy GMV. | Our T3/T4 already tries to get *independent named payments*, not *what was bought*. Quality ≠ economic type. A clean T3 transfer can still be escrow principal, channel funding, or inventory float. Table 0’s one number was therefore still a GMV trap. |
| 2 | Gateway 不应和 Base / Solana 完全并列；GMV 只能算一次 | **Accept.** | Gateway is **batching / netting infrastructure** on top of a settlement network (today mainly Base). Same dollar may be tagged Gateway **and** Base. Putting Gateway as a GMV *row* next to Base double-counts or invents a sixth chain. |
| 3 | 支付协议表增加 Repeat Buyers / Repeat Rate | **Accept as a column, reject as a new idea.** | T4 already *is* repeat. The cascade just forgot to put it on 表 2. Repeat on **raw** x402 is gamed (same bot, every day). Repeat is T3/T4 only. |
| 4 | 增加「钱买了什么」轻量分类（Data / Inference / Execution / API） | **Accept as a drill-down, reject as a required weekly layer.** | The PMF question is right. The data is not. Most T3 payees have no durable SKU label; a mandatory 需求类型 table will be filled with guesses. Open it only on the **increment** of Service Spend, and keep `Unknown`. |

What the review got slightly wrong:

- **ACP $500 is not how 表 0 currently breaks.** Virtuals sits on 表 3, not in the payment sum. The real leak is: (a) someone later “unifies” ACP escrow into machine GMV, (b) x402/MPP still count **principal-sized** transfers that are not a SKU price, (c) Allium’s ACP carve-out (`is_agent_economy_circulation`) correctly *keeps* those flows out of “inorganic,” which is the opposite of “not GMV.” Circulation ≠ service.
- **「Paid Tx」不能进老板屏如果不加质量门。** Raw paid tx is the August 2026 Goodhart metric (~17.9M txs / ~$437k). Boss **Paid Tx** = T3 (or MPP `Settled`, or L402 paid), never T0.
- **下一步「不是再加表」是对的。** 需求类型若升格成和结算网络平级的一层，就是再加表。PMF 用下钻，不用新雷达。

---

## Two axes (do not flatten into one list)

```
功能 (what)                         场所 (where the money sits)
────────────────────────────────    ────────────────────────────
支付协议  x402 / MPP / L402         结算网络  Base / Solana / Tempo / Arc / Lightning
商务编排  Virtuals ACP / UCP / Masumi   批处理层  Circle Gateway  ← overlay，不是第六条链
身份      ERC-8004 / TAP
授权      AP2 / OpenAI Agentic Commerce Protocol / Verifiable Intent
```

**同层 + 同经济事件 + 同计量单位，才能同表比较。**  
Base 不是 x402 的下级：x402 也跑在 Solana 上；Tempo 上主要是 MPP。  
Gateway 也不是和 Base 平级的场所：它是结算网络上的聚单/净额层。  
OpenAI **Agentic Commerce Protocol** 是结账授权（Layer 2），Virtuals **ACP** 是 job 编排（Layer 3）——同名 ACP 不能同表。

### Settlement networks (表 1 rows — GMV lives here, once)

| 结算网络 | 它是什么 | 上面主要跑什么 | 2026-09 状态 |
| --- | --- | --- | --- |
| **Base** | Coinbase L2 | x402、Virtuals ACP、8004 | 机器支付主场 |
| **Solana** | L1 | x402 | 笔数可翻 Base，仍要用质量美元比 |
| **Tempo** | Stripe 相关结算链 | MPP | 已主网；看 `Settled` 不是开通道 |
| **Arc** | Circle L1，USDC 当 gas | 计划中的 agent finance / x402 类纳米支付 | 公开主网 2026-09-16，此前不当 GMV |
| **Lightning** | 比特币二层 | L402 | 份额小，但和 x402 同层 |

Polygon / BNB / 其他 EVM：尾部，只在 Service Spend 突然冒头时展开。

### Overlay (not a GMV row)

| 层 | 它是什么 | 怎么进表 | 禁止 |
| --- | --- | --- | --- |
| **Circle Gateway** | 链下聚单、链上净额结算（EIP-3009 一类），给 x402 做批量结 | 表 1 的**列**：该网络 Service Spend 里有多少 % 经 Gateway 净额；可同时打标 Gateway + Base | 把 Gateway USD 加进 Base USD；把 Gateway 当成第六条结算网络 |

同一笔 Service Spend：结算网络算一次，Gateway 只记「怎么结的」。

---

## Three dollars (the split 表 0 was missing)

Before summing anything, stamp every machine-adjacent USDC flow with **one** economic type. If you cannot stamp it, it is not 表 0.

| Type | What it is | Examples | Where it belongs |
| --- | --- | --- | --- |
| **Service Spend** | Machine paid a **price** for a delivered (or billed) service | x402 T3 named SKU; MPP `Settled` that is usage; L402 paid invoice for an API | **表 0 / 表 1 / 表 2** — the only GMV |
| **Principal / notional** | Capital posted, traded, or escrowed; fee is a slice | Virtuals ACP job funded $500 to trade, $1 protocol fee; agent-wallet DEX size; job escrow | **表 3** as two columns: notional vs fee. Never fold notional into 表 0 |
| **Plumbing** | Money moved so that a later payment can happen | MPP `TopUp` / channel open, facilitator inventory, Gateway batch that is netting already-counted spend, USDC transfers between agent wallets | Funding / ops series. Not GMV, not “agent GDP” |

Allium note: `is_agent_economy_circulation` on ACP-like flow means “this is not the self-deal wash filter.” It does **not** mean “this is Service Spend.” Do not promote circulation into 表 0.

---

## Boss first screen (表 0 — 1 分钟)

问题：这周有没有更多**真实机器服务支出**？在免费桌上，诚实答案往往是「Observed Service Spend 仍为 null」。

**Observed Service Spend**（定义）：x402 T3 USD + MPP **usage Settled USD** + L402 paid。没有逐笔账本、且 MPP 饲料没有 Settled **美元**时，该格必须是 **null**。禁止把代理加总进这一格。

| 格 | 免费桌填写 | 量纲 | 不是这个 |
| --- | --- | --- | --- |
| **Observed Service Spend** | **null** | USD | F_sku；T0 vol；x402watch 30d real；F_sku 美元 **加** Settled 笔数 |
| **x402 covered SKU spend proxy** | F_sku 24h USD（有类目标签的目录切片） | USD | x402 Service Spend；机器 GDP |
| **MPP settled paid events** | `Settled` **笔数** | count | 与 F_sku 美元相加；`ChannelOpened` |
| **MPP settled USD** | 饲料给出用量美元才填，否则 **null** | USD | 用笔数冒充美元 |
| **Paid Tx (quality)** | 有 Observed Spend 才填对应笔数；否则只报 F_sku txs 与 MPP Settled **分列** | count | T0 笔数（战役探测器，另格） |
| **Unique Buyers** | **null** | — | `organic_user` 人数 |
| **Repeat Buyer Rate** | **null** | — | T0 连打 |
| **Unique Sellers (catalog proxy)** | last_seen 7d、非 placeholder、去掉 ACP URL | count | T3 named payees |

辅看：T0 均价。均价塌到 <$0.05 且 T0 笔数暴增 → 战役。F_sku 单类目 ≥50% → covered-SKU 集群，不是 S1。

闸门：两个 null（Buyers / Repeat）是正常的。**Observed Service Spend 为 null 时，表 0 的标题不得写成「真服务支出已测到」。** 打开表 1/2 看的是代理是否动，不是 GMV 已证实。

- Observed Spend、F_sku、MPP Settled 笔数、catalog sellers **都不动** → 只扫表 6。
- 仅 T0 笔数动、F_sku 与 Settled 不动 → 战役。
- Unique Buyers / Repeat **不能**用来判断复购。

---

## Weekly pack (看表顺序 = 从大到小)

### 表 1 — 结算网络（5 分钟）

问题：Observed Service Spend（若仍为 null：则是哪条轨上的 **labeled proxy**）去了哪条**最终结算**轨？

行（只这些）：Base、Solana、Tempo、Arc（上线后）、Lightning。  
列：Observed Service Spend（常 null）、或 **标明** 的链上代理（周看 Artemis adjusted 链份额 / scan 原始份额，不得写成 Spend）；catalog sellers；WoW。  
**Overlay 列（不是行）：** Gateway-netted % — 无序列则 **null**，不准用别的美元比例顶上。

异动：某条链 Service Spend 份额连续变化（Solana 吃 Base、Tempo/Arc 从 0 变成可测）。  
质量门过了之后，才问条件化 L5 映射（Base↔COIN，Arc↔CRCL，Solana↔SOL）。这不是预设核心书。  
Gateway % 升：Circle 批处理在抢单笔链上费，**不**额外加 GMV。

### 表 2 — 支付协议（5 分钟，与表 1 同级）

问题：信封换了没有？复购是不是真的？

行：x402、MPP、L402。  
列：Observed Service Spend（常 null）、质量 Paid Tx（分列，不与美元相加）、Unique Buyers（常 null）、Repeat（常 null）、Unique Sellers。  
交叉（表 2×1，仍是连接器不是新层）：协议 × 结算网络。x402 的 covered-SKU proxy 与 MPP Settled **笔数**分列，量纲不同。

异动：MPP 或 L402 从可忽略变成两位数份额；某协议 Repeat Rate 与 Spend 同向变。  
禁止：x402 笔数 vs MPP `ChannelOpened`；把 Gateway 写成第四个支付协议。

### 表 2b — 需求类型 / SKU（仅当 covered-SKU proxy 或 Observed Spend 动了，且有标签）

问题：增量美元买的是什么？PMF 在哪一类？

这不是每周必开的一层。没有标签就写 `Unknown`，不要编。

建议桶（互斥，一笔一个；覆盖率低时不要假装精细）：

| 桶 | 典型 | 投资含义 |
| --- | --- | --- |
| **Inference** | LLM / 路由 / agent loop tokens | 路由器、GPU、推理 API |
| **Data** | 检索、爬取、专用数据集 | 数据卖方、索引 |
| **Compute / execution** | GPU 时、沙箱、工具运行 | 执行层，不是「又一次 API 调用」的同义词 |
| **Other API** | 有名但非上述三类的 HTTP 服务 | 长尾工具 |
| **Unknown** | T3 但目录无类目 | 默认桶；Unknown 占比下降本身才是信号 |

禁止：把 ACP「执行一单生意」塞进这一表（那是表 3）；用这一表的行去加总出第二个 GMV。

### 表 3 — 商务编排（仅当表 0 动了，或 Virtuals/代币先跳）

问题：有没有更多「完结的一单生意」？**费**是多少，**本金**是多少？

行：Virtuals ACP、Masumi；（UCP 有公开完结单再加）。  
**不要**把 OpenAI Agentic Commerce Protocol 放进本表——那是 Layer 2 结账**授权**，与 job 编排不是同一经济事件。  
列：**完结 job 数**、**Fee / take**、**Notional / escrow**、独立对手方。丢掉 memo。无 fee/notional 公开数时，只报 senders/memos **活动度**，不得声称已测到 ACP 经济规模。

规则：Notional 可以很大；老板屏和表 0 **只可以引用 Fee**，除非备忘录明确在写「托管规模」。  
`$500` 本金 + `$1` 服务费 → Service Spend = `$1`（若费是买编排服务），Notional = `$500`。  
异动才碰 `VIRTUAL`。完结单不动、memo 或代币先跳 → 注意力，不升级。

### 表 4 — 身份（周扫，默认不占会）

带支付证明的 8004 反馈、独立运营商。Mint 数不进会。

### 表 5 — 主体（从表 1–3 点进去）

Facilitator 份额、Top payee、是否 named 目录还活着、该 payee 的需求类型（若有）。  
这里才出现「谁在赚钱」，不是第一张表。

### 表 6 — 规则 / 日历（每次周会最后 3 分钟）

Arc 主网（2026-09-16）、AP2 撤回原语、拒付归因、公约。无则写无。

---

## 决策规则

| 本周只动了… | 打开 | 不打开 |
| --- | --- | --- |
| 表 0 Observed Spend / covered-SKU / Settled 笔数 / catalog sellers | 表 1 + 表 2（代理须标明） | 不必深挖表 5 |
| 仅 Repeat Rate（Spend 不动） | 脚注：老客加码 | 当采用 |
| 仅某条结算网络份额 | 该网上的协议交叉；看 Gateway % | 别的链的主体 |
| 仅 Gateway %（Spend 不动） | 一句「结法变了」 | 新 GMV |
| 仅 MPP/x402 份额 | Tempo vs Base 交叉 | Virtuals |
| 表 0 动了且目录有类目 | 表 2b 看增量 SKU | 没有标签就不要开 |
| 仅 Virtuals 完结单 | 表 3 的 fee vs notional；表 5 对手方 | 把 notional 加进表 0 |
| 仅代币 / 仅原始笔数 | 表 6 + 一句「未证实」 | 整份采用备忘录 |

从上到下：

**总盘（Observed Spend 常为 null + 分列代理）→ 结算网络 + 支付协议（并列）→ 协议×网络交叉 →（有标签才）需求类型 → 商务编排（fee ≠ notional；OpenAI 结账 ACP 不在此表）→ 身份 → 主体 → 规则**

每一张表内部的行必须是同类。链和协议永远分两张表。Gateway 永远是结算网络上的列，不是行。
