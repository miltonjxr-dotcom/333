# Weekly cascade: large categories → smaller tables

Monitor top-down. A lower table is opened only if the table above moved, or once a week as a 10-minute scan.
Never mix rows that answer different questions.

## Two axes (do not flatten into one list)

```
功能 (what)                         场所 (where the money sits)
────────────────────────────────    ────────────────────────────
支付协议  x402 / MPP / L402         链/结算场所  Base / Solana / Tempo / Arc / Lightning / Gateway
商务编排  Virtuals ACP / UCP / …    （协议可以跨链；链上可以跑多个协议）
身份      ERC-8004 / TAP
授权      AP2 / Verifiable Intent
```

**链和支付协议是平级的两大类，不是上下级。**  
Base 不是 x402 的下级：x402 也跑在 Solana 上；Tempo 上主要是 MPP，不是「一条更小的 x402」。  
每周先看「钱在哪条场所、用哪种信封」，再往下拆名字。

场所（当前需要进表的）：

| 场所 | 它是什么 | 上面主要跑什么 | 2026-09 状态 |
| --- | --- | --- | --- |
| **Base** | Coinbase L2 | x402、Virtuals ACP、8004 | 机器支付主场 |
| **Solana** | L1 | x402 | 笔数可翻 Base，仍要用质量美元比 |
| **Tempo** | Stripe 相关结算链 | MPP | 已主网；看 `Settled` 不是开通道 |
| **Arc** | Circle L1，USDC 当 gas | 计划中的 agent finance / x402 类纳米支付 | 公开主网 2026-09-16，此前不当 GMV |
| **Lightning** | 比特币二层 | L402 | 份额小，但和 x402 同层 |
| **Circle Gateway** | 链下聚单、链上净额结算 | 给 x402 做批量结 | 场所，不是又一个支付协议 |

Polygon / BNB / 其他 EVM：尾部，只在质量美元突然冒头时展开。

## Weekly pack (看表顺序 = 从大到小)

### 表 0 — 总盘（1 分钟）

问题：这周机器支付有没有真的动？

一个数：全场所 **质量美元** 之和（x402 的 T3/T4 + MPP `Settled` + L402 已付，折美元）。  
周环比、均价、独立收款方合计。

- 不动 → 下面只扫一眼表 6 事件，写「无」。
- 动了 → 必开表 1 和表 2。
- 只有原始笔数动、质量美元不动 → 记战役，不往下当采用。

### 表 1 — 场所 / 链（5 分钟）

问题：钱去了哪条轨？

行：Base、Solana、Tempo、Arc（上线后）、Lightning、Gateway。  
列：质量美元、份额%、独立收款方、WoW。

异动：某条链质量美元份额连续变化（例如 Solana 吃 Base、或 Tempo/Arc 从 0 变成可测）。  
这是区块空间 / L5 的表达（COIN–Base，CRCL–Arc，SOL，Tempo）。

### 表 2 — 支付协议（5 分钟，与表 1 同级、紧接着看）

问题：信封换了没有？

行：x402、MPP、L402。  
列：质量美元、占机器支付份额、独立收款方。  
交叉：协议 × 场所（x402 在 Base vs Solana；MPP 几乎只有 Tempo）。

异动：MPP 或 L402 从可忽略变成两位数份额。  
禁止：x402 笔数 vs MPP `ChannelOpened`。

### 表 3 — 商务编排（仅当表 0 动了，或 Virtuals/代币先跳）

问题：有没有更多「完结的一单生意」？

行：Virtuals ACP、Masumi；（UCP / OpenAI ACP 有公开数再加）。  
列：完结 job / 放款美元、独立对手方。丢掉 memo。

异动才碰 `VIRTUAL`。完结单不动、memo 或代币先跳 → 注意力，不升级。

### 表 4 — 身份（周扫，默认不占会）

带支付证明的 8004 反馈、独立运营商。Mint 数不进会。

### 表 5 — 主体（从表 1–3 点进去）

Facilitator 份额、Top payee、是否 named 目录还活着。  
这里才出现「谁在赚钱」，不是第一张表。

### 表 6 — 规则 / 日历（每次周会最后 3 分钟）

Arc 主网（2026-09-16）、AP2 撤回原语、拒付归因、公约。无则写无。

## 决策规则

| 本周只动了… | 打开 | 不打开 |
| --- | --- | --- |
| 表 0 质量美元 | 表 1 + 表 2 | 不必深挖表 5 |
| 仅某条链份额 | 该链上的协议交叉 | 别的链的主体 |
| 仅 MPP/x402 份额 | Tempo vs Base 交叉 | Virtuals |
| 仅 Virtuals 完结单 | 表 5 里 ACP 对手方 | 支付协议战争 |
| 仅代币 / 仅笔数 | 表 6 + 一句「未证实」 | 整份采用备忘录 |

从上到下：总盘 → 场所和支付协议（两大类并列）→ 商务 → 身份 → 名字 → 规则。  
每一张表内部的行必须是同类。链和协议永远分两张表，用交叉表连接，不合并成一列「Base、x402、VIRTUAL、8004」。
