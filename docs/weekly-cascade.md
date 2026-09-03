# Weekly cascade: large categories → smaller tables

Monitor top-down. A lower table is opened only if the table above moved, or once a week as a 10-minute scan.
Never mix rows that answer different questions.

This file is the weekly pack. Quality definitions live in [`agent-economy-monitoring-playbook.md`](agent-economy-monitoring-playbook.md).

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
商务编排  Virtuals ACP / UCP / …    批处理层  Circle Gateway  ← overlay，不是第六条链
身份      ERC-8004 / TAP
授权      AP2 / Verifiable Intent
```

**链和支付协议是平级的两大类，不是上下级。**  
Base 不是 x402 的下级：x402 也跑在 Solana 上；Tempo 上主要是 MPP。  
Gateway 也不是和 Base 平级的场所：它是结算网络上的聚单/净额层。

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

问题：这周有没有更多**真实机器服务支出**，以及需求是否在复购、供给是否在变宽？

五个数，全部来自 Service Spend，全部带质量门。没有第六个「再加一个总美元」。

| 指标 | 定义（本周） | 核心意义 | 不是这个 |
| --- | --- | --- | --- |
| **Service Spend** | x402 T3 USD + MPP `Settled` USD that is usage + L402 paid，折美元。T4 USD 作底（更严） | 真实机器服务支出 | T0 体积；ACP 本金；Gateway 再加一遍；Circle 全链 USDC |
| **Paid Tx** | 上述 Service Spend 对应的笔数 | 真实付费次数 | 原始 x402 txs、MPP 全事件、ACP memos |
| **Unique Buyers** | T3（及 MPP/L402 等价）独立付款方 | 需求方数量 | T0 unique from；同一 facilitator 集群 |
| **Repeat Buyer Rate** | T4 buyers / T3 buyers（30d 窗口与 playbook T4 定义一致） | 是否形成真实复购，而非测试/激励刷量 | 未过滤的「连着打了两天」 |
| **Unique Sellers** | T3 独立收款方（named / live catalog） | 供给生态规模 | 一次性 mint 型 payee、facilitator 自收 |

辅看（同一屏脚注，不当第六个老板 KPI）：均价/票档、周环比。均价塌到 <$0.05 且 Paid Tx 暴增 → 战役，Service Spend 不动也当「未采用」。

闸门：

- 五个数都不动 → 下面只扫表 6，写「无」。
- Service Spend 或 Unique Sellers 动了 → 必开表 1 和表 2。
- 只有 Paid Tx 动、Service Spend 不动 → 记战役，不往下当采用。
- Repeat Buyer Rate 升而 Unique Buyers 跌 → 集约（老客户加码），不是生态变宽。
- Unique Buyers 升而 Repeat → 0、均价极低 → 空投/测试，不是 PMF。

---

## Weekly pack (看表顺序 = 从大到小)

### 表 1 — 结算网络（5 分钟）

问题：Service Spend 去了哪条**最终结算**轨？

行（只这些）：Base、Solana、Tempo、Arc（上线后）、Lightning。  
列：Service Spend、份额%、Unique Sellers、WoW。  
**Overlay 列（不是行）：** Gateway-netted % of that network’s Service Spend。Arc 上线后若 Gateway 也结 Arc，同样是列，不是新行。

异动：某条链 Service Spend 份额连续变化（Solana 吃 Base、Tempo/Arc 从 0 变成可测）。  
这是区块空间 / L5 的表达（COIN–Base，CRCL–Arc，SOL，Tempo）。  
Gateway % 升：Circle 批处理在抢单笔链上费，**不**额外加 GMV。

### 表 2 — 支付协议（5 分钟，与表 1 同级）

问题：信封换了没有？复购是不是真的？

行：x402、MPP、L402。  
列：Service Spend、占机器服务支出份额、Paid Tx（质量门）、Unique Buyers、Repeat Buyer Rate、Unique Sellers。  
交叉（表 2×1，仍是连接器不是新层）：协议 × 结算网络（x402 在 Base vs Solana；MPP 几乎只有 Tempo）。

异动：MPP 或 L402 从可忽略变成两位数份额；某协议 Repeat Rate 与 Spend 同向变。  
禁止：x402 笔数 vs MPP `ChannelOpened`；把 Gateway 写成第四个支付协议。

### 表 2b — 需求类型 / SKU（仅当表 0 的 Service Spend 动了，且有标签）

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

行：Virtuals ACP、Masumi；（UCP / OpenAI ACP 有公开数再加）。  
列：**完结 job 数**、**Fee / take**（协议或平台抽成）、**Notional / escrow**（账户里转过的本金，单独列）、独立对手方。丢掉 memo。

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
| 表 0 Service Spend / Unique Sellers | 表 1 + 表 2 | 不必深挖表 5 |
| 仅 Repeat Rate（Spend 不动） | 脚注：老客加码 | 当采用 |
| 仅某条结算网络份额 | 该网上的协议交叉；看 Gateway % | 别的链的主体 |
| 仅 Gateway %（Spend 不动） | 一句「结法变了」 | 新 GMV |
| 仅 MPP/x402 份额 | Tempo vs Base 交叉 | Virtuals |
| 表 0 动了且目录有类目 | 表 2b 看增量 SKU | 没有标签就不要开 |
| 仅 Virtuals 完结单 | 表 3 的 fee vs notional；表 5 对手方 | 把 notional 加进表 0 |
| 仅代币 / 仅原始笔数 | 表 6 + 一句「未证实」 | 整份采用备忘录 |

从上到下：

**总盘（Service Spend 五 KPI）→ 结算网络 + 支付协议（并列）→ 协议×网络交叉 →（有标签才）需求类型 → 商务编排（fee ≠ notional）→ 身份 → 主体 → 规则**

每一张表内部的行必须是同类。链和协议永远分两张表。Gateway 永远是结算网络上的列，不是行。
