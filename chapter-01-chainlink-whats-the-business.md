# 第 1 章　Chainlink 到底是什么生意

> **回答**：它卖什么，它在做哪类基础设施业务。
>
> **标签约定**：[事实]=一手/可链上核验来源；[合理推断]=基于事实的综合判断；[待验证假设]=二手来源出现但未能独立核验，不进入估值输入。
>
> **数据截止**：2026-04-21。当前市况锚点：LINK ≈ $8.60–9.39，市值 ≈ $6.6–6.9B，流通 ≈ 727M/1B（72.7%），距 2021-05-10 ATH $52.70 回撤约 83%。

---

## 1.0 本章 BLUF（先结论）

Chainlink 在商业本质上是一家**链上金融的「中间件路由与证明层」公司**——它不生产专有数据、不持有结算最终性、不提供订阅式终端工作流，而是把**链下价格/NAV/储备证明/消息**以一套标准接口、用一张节点网络「路由+证明+传送」进去链上合约，或把**链上消息/代币**在多链之间「路由+证明+传送」出去。[合理推断]

**一句话总结**：**Chainlink ≈ 加密原生的 SWIFT + 极轻量的 MSCI/S&P 数据授权层**——SWIFT 是核心经济体、MSCI/S&P 是期权（SVR、DataLink、PoR）。用 Bloomberg 终端或 DTCC SIFMU 做类比会系统性高估其定价权。[合理推断]（见 1.3 / 1.5）

**必须同时持有的三个锚点**：

1. **营收上**，按 DefiLlama 可审计口径年化约 $55–75M[事实]，其中 **>90% 来自 Data Feeds/Requests** 这一条产品线；CCIP、Data Streams、SVR、VRF、Automation、Functions、PoR、CRE 合计贡献 **个位数百万美元年化**（SVR 是唯一可审计新营收模板，9 个月累计 $16M MEV 回收、$5.6M 给 Chainlink 生态）。[事实]
2. **业务形态上**，Chainlink 的核心交付不是"代币经济学"、不是"TVS \$17T 保护"、不是"机构采纳路线图"，而是**「谁付费、付多少、为什么离不开」的单一提问**——在这个提问下，真正付钱的是 Aave / Compound / Synthetix / GMX / Jupiter 等少数 DeFi 协议，机构合作方在 2026-04 前**没有任何一家公开披露过付给 Chainlink 的费用金额**。[事实]
3. **定价权上**，Chainlink 对「Value Secured \$100B+」只收约 $55–75M 年化（实证 take rate < 10 bps），与 SWIFT 量级一致；**价值承载极大、价值捕获极小**是中间件宿命，也是 Chainlink 议价权实测低的结构原因。[合理推断]

本章回答「它卖什么」，不回答「它值多少」（第 10 章）、不回答「代币能否吃到协议成功」（第 7 章）、也不回答「合规怎么办」（第 9 章）。

---

## 1.1 项目简介

Chainlink（以下简称 CL）由 Sergey Nazarov、Steve Ellis 于 2017 年创立，起源是 2014 年 SmartContract.com 与 2017 年原始白皮书提出的「去中心化预言机网络」构想。2017-09 通过 ICO 发行 LINK，硬顶 1B，原始分配 35% 公开销售 / 35% 节点&生态 / 30% 公司。2019-05 主网上线；2020–2021 年随 DeFi Summer 完成第一轮协议级采纳（Aave、Compound、Synthetix 是 Data Feeds 首批付费客户）。[事实]

2020 年以来在技术叙事上的四次切换值得在第 3 章审计：
1. 2020–2021：从「预言机」切向「Chainlink 2.0 Hybrid Smart Contracts」愿景文档（2021-04 白皮书）；
2. 2022–2023：Staking v0.1/v0.2、CCIP 主网、SWIFT 跨链试点；
3. 2024–2025：机构 RWA 路线（DTCC Smart NAV、Fidelity International + Sygnum、UBS DTA、ANZ、SBI、Mastercard/Swapper、21X、J.P. Morgan Kinexys）；
4. 2025：Economics 2.0 完整化（Payment Abstraction 2025-03、Chainlink Reserve 2025-08、SVR live 2025-03）。

公司侧：Chainlink Labs（商业实体）+ Chainlink Foundation（基金会/非流通钱包控制方）。**自 2017 ICO 之后，Chainlink Labs 没有任何公开定价的股权融资记录**（Tracxn / Crunchbase / Forge / EquityZen 查证均仅此一轮），资金来源事实上依赖基金会非流通钱包自 2022-08 起系统化向 Binance / 做市商的批量转入。[事实]——这一点在第 3 章展开，但已足以构成本章的定性前提：**Chainlink 是一个"9 年故事 + 24 个月真实代币学机制"的标的**，其业务介绍必须先剥离营销口径才能看清。

**先剔除不属于"生意"本身的四类误导口径**：

- ❌ **"保护了 \$17T 交易价值 / TVS \$100B+"**——这是 Total Value Secured 营销指标，不是营收、不对应任何经济价值传导。[合理推断] 在本章和估值章都**不应作为锚点**。
- ❌ **"CCIP 月度 \$18B 成交、累计 \$75B"**——仅见于 openpr.com 赞助稿与 TAUX 推广软文，未被任何独立 dashboard 验证。[待验证假设] **降级，不进估值输入**。
- ❌ **"Mastercard 3B+ 持卡人"**——2025-06-24 通过 Swapper Finance / zerohash / Shift4 / XSwap 上线的是**针对少数合作方的 on-ramp rail**，不是 3B 持卡人全量。[待验证假设]
- ❌ **"1,000+ 合作方"生态 logo 墙**——其中绝大多数是 SCALE/BUILD **代币补贴换集成**的营销项目，不产生可归因费用。[合理推断]

---

## 1.2 核心产品全景

先给结论版表（保留并扩展框架原表，按 **营收贡献** 而非公告时间排序，数据截止 2026-04）：

| 层级 | 产品 | 年化可审计费用 | 首批 / 代表付费客户 | 定性判断 |
| --- | --- | --- | --- | --- |
| **Core（现金牛）** | **Data Feeds / Requests** | **$55–70M**[事实，DefiLlama combined $74.56M、requests-only $58.8M 交叉取保守值 ~$60M] | Aave / Compound / Synthetix（2020–21） | **真正的营收支柱，占总可审计费用 >90%**；9 年里的唯一"现金牛" |
| **Enhancement（正在验证）** | **SVR**（Secondary Value Recapture） | **$2–3M TTM 并增长**[事实，Aave blog + Chaos Labs + Chainlink 2026-03-28 推文三方交叉；9 个月累计回收 MEV $16M、Chainlink 生态分成 $5.6M、近月度 $1.5–2M] | Aave V3 Ethereum（扩至 Arbitrum / Base 后加速） | **唯一完全可审计的新营收模板**；take rate ≈ MEV 事件 × 40% × 35%（头 6 月 65/35 → 后 60/40） |
| | **Data Streams** | 单位数 $M 估算（未独立披露） | GMX V2 / Synthetix / Jupiter perps / Lighter | **pull-based，正面对阵 Pyth**；GMX V2 把协议费 1.2% 分给 Chainlink providers[事实]；但高频衍生品主战场（Hyperliquid）已选 Pyth，结构性被切 |
| | **CCIP** | **< $2M 年化**（DefiLlama 累计 $603K，2023-07 主网至 2026-04；生态 dashboard 累计转账量 \$1.66B / 2025-02）[事实] | Synthetix xERC20 / Aave GHO / Coinbase cbBTC / BUIDL 分配 | **营销叙事 >> 实际费用**。take rate ~0.3–3.6 bps；消息费 ~$0.09/msg 与 SWIFT $0.07–0.10 同量级；CCIP 月度 $18B 叙事为 [待验证假设] |
| | **CCIP v1.6** | 增量营收未独立披露 | 2025-05-19 主网，首次支持 Solana | 架构从 lane → chain，与 Coinbase wrapped assets 同步；仍计入 CCIP 合口径 |
| | **Proof of Reserve** | 最小（不独立披露） | TUSD / 21Shares / BitGo / 多数 RWA 发行方 | **合规护城河工具**，不是费用工具；多数用量通过 SCALE 项目抵扣 |
| **Optionality（沉寂 / 未商业化 / 叙事品）** | **VRF** | **$170 年化** [事实，DefiLlama] | 游戏 / NFT Mint | 依赖 GameFi 景气，事实上已 dormant |
| | **Automation / Keepers** | **~$0** [事实，DefiLlama] | DeFi 触发器 | 已内嵌 Payment Abstraction 充当成本后端，不作为前端产品 |
| | **Functions** | 极小 | 少数 SCALE 链项目 | 未独立成商业产品 |
| | **CRE**（Runtime Environment） | 未商业化，试点阶段 | Swift/DTCC 企业行动编排试点 | [合理推断] 是 2021 "Hybrid Smart Contracts" 愿景的**重命名/工程化**，非新产品 |
| | **DECO / FSS / Town Crier** | $0 | — | 2020 年收购 / 公告，至 2026-04 **无命名生产客户**；DECO 被吸收为 CRE 的隐私子系统；FSS 事实上由 SVR 降级替代；Town Crier 已静默退场 |
| **不是产品（是机制）** | **Payment Abstraction** | N/A（属捕获侧机制，不是前端 SKU） | 为其他产品的费用 → LINK 通道 | 2025-03 上线，2025-08 Reserve 启动后成为闭环；**本章不计入产品矩阵**，在第 7 章作为需求侧机制分析 |

**表外关键数据（2026-04 锚点）**：

- DefiLlama Chainlink combined fees 年化 **$74.56M**；requests-only 年化 **$58.8M**。口径差异（combined 包含一些 off-chain 附加费）下取保守可信值 **~$60M**。[事实]
- SVR 累计 MEV 回收 $16M / 9 个月 / Chainlink 生态分成 $5.6M；Aave 分成初始 6 个月 65/35，后转 60/40。[事实]
- CCIP DefiLlama 累计 fees $603,065（2023-07 主网上线至 2026-04，DefiLlama 年化当前标记 "deprecated/0"）；生态 dashboard 累计转账 $1.66B（2025-02 snapshot）。**没有任何公开数据支持 Q1 2026 月度 $18B 成交、累计 $75B 这类数字；这些只出现在 openpr 赞助稿与 TAUX 推广软文，降级为 [待验证假设]**。

### 1.2.1 从矩阵可以读出的四条硬事实

1. **Chainlink 本质是一家「Data Feeds 公司 + 一个正在跑通的新模板（SVR）」**。CCIP / Data Streams / VRF / Automation / Functions / PoR / CRE / Payment Abstraction 这 8 条产品线合计对年化费用的贡献**小于 Data Feeds 单独一条的 10–20%**。[合理推断]
2. **"一 dApp 一预言机" 时代已经结束**。Morpho 预言机中立化、Aave 保留 fallback、Maker/Sky 改用 Chronicle、Hyperliquid 选 Pyth/自研、BUIDL 上游用 Securitize+RedStone、Figure 自建链——Chainlink 在**高频衍生品、代币化基金 NAV、专业化借贷市场**三个细分赛道**正在被专业化选手切走**。Data Feeds 这个现金牛并非结构性安全。[合理推断]
3. **机构合作方到 2026-04 为止没有一家披露过付费金额**（SWIFT / DTCC / UBS / Fidelity / ANZ / Mastercard / SBI / J.P. Morgan Kinexys / 21X 均无公开费用线条）。**唯一 Tier 4 (Production live) 是 Fidelity International + Sygnum**，但代币化仓位仅 $50M、费用未披露、合理推断近零或象征性。[事实 + 合理推断]（见 1.4 与第 6 章机构合作 Tier 表）
4. **增长信号是对的，但规模错配严重**：Reserve 累积从 2025 年 10 月的 80–90K LINK/周 加速到 2026 年初的 125–137K LINK/周（Cryptonews 综合链上 dashboard，[合理推断] 中等质量）——**即 7x 增速**——但绝对量仍是**月均 ~383K LINK ≈ $3.5M / 月 / $42–45M 年化**，与 Foundation 非流通钱包历史月均释放 4–6M LINK（$40–60M+ /月）**差一个量级**。[合理推断]

---

## 1.3 业务本质判断：数据服务 / 中间件 / 基础设施网络

把 Chainlink 套进 TradFi 类比是本章最容易走偏的动作。先看 take rate 与规模的实证对照表：

| 层次 | 对比实体 | take rate on value | 年化费用规模 | 与 Chainlink 的关系 |
| --- | --- | --- | --- | --- |
| 结算 / 登记（零 take rate 公用事业） | DTCC | ~0.0007 bps | $2.49B EBITDA $609M | **不类比**：无 SIFMU 地位、无结算最终性 |
| 消息路由（低 take rate 合作社） | SWIFT | ~0.07 bps（~$0.08/msg） | ~€0.85–1B | **最贴切单一类比** |
| **Chainlink CCIP 消息** | — | ~$0.09/msg（与 SWIFT 同量级） | ~$0–2M | — |
| **Chainlink CCIP token 转移** | — | **6.3–7 bps on notional**（与 MSCI 级别相当） | <$2M（量太小） | **transitional，不可持续**（见下） |
| 指数授权 | MSCI | ~1.25 bps on $6.4T linked AUM | ~$800M | **不类比**：无指数 IP、无万亿 AUM 授权 |
| 评级 | S&P / Moody's | 1–7 bps on issuance | 各 $4B+ | **不类比**：无 NRSRO 牌照、无 issuer-pays 特许 |
| 订阅终端 | Bloomberg | N/A（seat 模型） | ~$10–11B | **不类比**：无 $28K/seat、无终端 workflow、无 chat network effect |
| 交易 / 清算 | ICE / LSEG | 0.5–5 bps on notional | $5–10B | **不类比**：无交易所许可、无清算最终性 |

### 1.3.1 为什么是 SWIFT，不是 Bloomberg / MSCI / DTCC

把 Chainlink 归为 **"加密原生的 SWIFT"**，理由四条：[合理推断]

1. **功能同构**：Chainlink **不产生**专有数据或评级，只**传输 + 证明**。Data Feeds 是从链下到链上的路由；CCIP 是跨链消息路由；PoR 是储备状态的证明路由；SVR 是清算订单流的路由（MEV 回收是路由顺位的副产品）。SWIFT 同样不是支付系统，而是 FI 间的安全消息标准。
2. **单位经济同量级**：CCIP 每消息费率（非 ETH lane 约 $0.09）与 SWIFT $0.07–0.10/msg 吻合到同一数量级——**这种吻合不是巧合，它反映两者在消息层的经济模型被技术标准化压缩至同一水平**。没有任何其他 TradFi 类比能达到这种吻合度。
3. **治理叙事同构**：Chainlink 对外定位为 "decentralized oracle network"；SWIFT 是 11,500 家金融机构的合作社。**都号称"中立基础设施"**，对应**低 take rate 的合作社式经济模型**。
4. **规模差距不是模型差距**：SWIFT 13.4B 消息/年，CCIP 累计消息量目前在 1–10M 量级。**这是天花板问题，不是赛道问题**。

### 1.3.2 "SWIFT + 轻 MSCI/S&P" 的三条升级路径

如果 Chainlink 要把经济模型从纯 SWIFT 往 MSCI/S&P 层轻度升级，可走三条路，但可行性差异极大：[合理推断]

| 路径 | 可行性 | 理由 | 营收上限估计 |
| --- | --- | --- | --- |
| **SVR 扩展至全 DeFi 借贷市场** | **高**（模板已验证） | Aave 已跑通；跨协议可复用；take rate 14% 结构化 | 上限受限于 DeFi 清算 OEV 总池，乐观估计 ~$50–100M/年 to Chainlink 生态 |
| **CRE 企业 workflow 编排** | 中 | 类 middleware 叙事，可绑定 DTCC 企业行动 | 与企业销售深度耦合，非 token-native 传导 |
| **Data Streams / DataLink 订阅** | **低** | 数据不是 Chainlink 原创，是 routing；面对 Bloomberg / Refinitiv / Pyth Pro 直接竞争 | 未独立披露营收，推测 <$5M 年化 |

**结论**：Chainlink 最可能的演化路径是 **SWIFT 式核心 + 极少数 MSCI 式 SKU（S&P Stablecoin Stability Assessments、Coinbase DataLink 为方向信号）**。但**核心经济体仍是 SWIFT**，不应用 Bloomberg P/S 乘数估值。[合理推断]——这一结论直接否定了第一版备忘录中"$125–165 收敛点估值"所隐含的 Bloomberg/MSCI 类比权重。

### 1.3.3 一个关键的结构性警告

CCIP 当前 6.3–7 bps 的跨链转账 take rate **大概率不可持续**。[合理推断]

历史上消息层 take rate 被压缩至接近 0（SWIFT、DTCC、Fedwire 均 < 0.001 bps）。一旦 CCIP 成交规模扩大，来自 **LayerZero、Wormhole、IBC、银行自建桥**的竞争将把 take rate 压至 <1 bps 的 messaging 层水平。**Chainlink 的 revenue 上行只能来自 volume scaling，不来自 price**——这是第 10 章估值的核心边界条件。

---

## 1.4 控制点 vs 可替代插件

把产品矩阵换个视角重切一次：**Chainlink 在哪些客户关系里是"控制点"（switching cost 高、议价权强）？在哪些里是"可替代插件"（有多个等价竞品、客户可一周内切换）？**

### 1.4.1 控制点（高 switching cost，议价权存在）

| 产品 × 客户类型 | 为什么是控制点 | 证据强度 |
| --- | --- | --- |
| **Data Feeds × 老牌 DeFi 蓝筹（Aave / Compound / Synthetix）** | 7 年集成历史、$100B+ TVS 无事故、7×24 节点网络的**运营信誉**难以在短期内被新竞品追上；更换预言机需要社区治理投票、需要审计、需要重构清算逻辑 | [事实]：7 年无重大预言机攻破事件 |
| **PoR × RWA 发行方（TUSD / 21Shares / BitGo）** | PoR 作为合规叙事的一部分，**品牌即合规**；RWA 发行方倾向选最"知名"的 PoR 提供方 | [合理推断] |
| **SVR × Aave** | SVR 模板在 Aave 的**治理绑定 + 分成合约**决定了这是一个长期多年关系；复制到其他借贷协议是 commercial question，不是 technical | [事实]：Aave V3 Ethereum / Arbitrum / Base 扩散中 |
| **Data Feeds / CCIP × SCALE 补贴链** | Moonbeam / Moonriver / Metis 等通过 SCALE 合同获得补贴期服务，短期内切换成本高 | [合理推断]；补贴期后留存率是跟踪指标 |

### 1.4.2 可替代插件（低 switching cost，议价权弱或无）

| 产品 × 客户类型 | 为什么是插件 | 证据 |
| --- | --- | --- |
| **Data Streams × 高频衍生品（Hyperliquid / Jupiter perps）** | Pyth 的 pull-based 延迟与成本模型在高频场景下结构性更优；Hyperliquid 选 Pyth/自研，Jupiter 用 Pyth | [事实]：Messari State of Pyth Q3 2025 份额上升；Chainlink 在此赛道份额下降 |
| **Data Feeds × 专业化借贷（Morpho / Maker/Sky）** | **Morpho 预言机中立化**（任何预言机均可接入）；**Maker/Sky 使用 Chronicle**（MakerDAO 自建）；**Aave 保留 fallback**——三例均表明蓝筹 DeFi 正在**去 Chainlink 依赖**作为架构原则 | [事实] |
| **代币化基金 NAV × RWA 上游** | **BUIDL 用 Securitize + RedStone**；**Figure / Provenance 自建链**；**Ondo 自建 DVN**——**RWA 上游不把 Chainlink 当默认层** | [事实]：截至 2026-04 上游市场结构未逆转 |
| **CCIP × 机构跨链消息** | **LayerZero 2026-02-10 宣布 Zero L1 + DTCC / ICE / Google Cloud / Citadel Securities / ARK / Tether 战略投资**；DTCC 同时脚踏两船——机构"独占通道"叙事被实质性稀释 | [事实]：Fortune / CoinDesk / BusinessWire 三方确认 |
| **CCIP × DEX-to-DEX 跨链** | LayerZero 在消息量 / 费用上领先 CCIP **1–2 个数量级**；Wormhole 免费 | [事实]：DefiLlama / LayerZeroScan |
| **VRF × 游戏 / NFT** | 年化 $170——本质已是 dormant 产品，不是 switching cost 问题，是 demand 问题 | [事实]：DefiLlama |

### 1.4.3 控制点 vs 插件的三个结论

1. **Chainlink 真正的"控制点"只剩三块**：Data Feeds × DeFi 蓝筹（旧护城河）、SVR × Aave（新模板）、PoR × 合规叙事（品牌工具）。**这三块合计占当前可审计营收的绝大部分**，也是估值锚点。[合理推断]
2. **Chainlink 在所有"新赛道"的身份都是插件**：机构跨链（CCIP vs LayerZero）、高频衍生品（Data Streams vs Pyth）、代币化基金 NAV（vs Securitize + RedStone）、清算与 MEV 扩展（vs API3 OEV Share）。**在新赛道里没有任何一个是 Chainlink 独占或 Chainlink 主导**。[合理推断]
3. **护城河类型是"品牌护城河强、经济护城河弱"**——这一判断在第 8 章展开，但本章的矩阵已经能给出实证：take rate < 10 bps 是经济护城河弱的直接指标；而 DTCC / SWIFT / CFTC 顾问委员会 / ISO 27001 / SOC 2 是品牌护城河强的直接指标。**两者并不矛盾，但也不能互相替代**。

---

## 1.5 一句话定义

**Chainlink 是加密原生的 SWIFT——一个低 take rate、高 Value Secured、品牌护城河强于经济护城河的金融消息/证明路由层，叠加一个跑通中的 MEV 价值回收模板（SVR）和一批尚未产生可审计营收的机构合作期权。**

**展开三条副定义**，供全报告其他章节反复调用：

1. **按营收**：Chainlink ≈ "Data Feeds（现金牛，$55–70M）+ SVR（新模板，$2–3M TTM 并增长）+ 一批 Optionality（合计个位数百万美元）"。[事实]
2. **按经济模型**：Chainlink ≈ "SWIFT 式消息层核心（< 1 bps 天花板）+ 极少数 MSCI/S&P 式订阅 SKU（SVR、DataLink、PoR）的期权"。[合理推断]
3. **按市场位置**：Chainlink 在**存量 DeFi 蓝筹**里是**控制点**，在**所有新增赛道**（机构跨链、高频衍生品、代币化 NAV、OEV 共享）里是**可替代插件**。[合理推断]

---

## 附注：本章拒绝的五个叙事（这些是常见陷阱）

在进入第 2 章之前，先把以下**五个需被明确驱逐出本报告估值输入**的叙事集中标注，后续章节不再重复论证：

1. ❌ **"Chainlink 保护了 \$17T / \$100B+ 交易价值"** → TVS ≠ 营收，不对应任何经济价值传导。[合理推断]
2. ❌ **"CCIP 月度 \$18B 成交 / 累计 \$75B"** → 仅见营销稿件，未被独立 dashboard 验证。[待验证假设]
3. ❌ **"Mastercard 3B+ 持卡人"** → 是 TAM 不是使用量；实际是针对少数合作方的 on-ramp rail。[待验证假设]
4. ❌ **"1,000+ 合作方生态"** → 绝大多数是 SCALE/BUILD 代币补贴换集成的营销项目，非费用生成器。[合理推断]
5. ❌ **"Chainlink 是 Web3 基础设施 / 去中心化预言机领军者"** → 等于什么都没说；本报告不使用此类 tautology。[合理推断]

---

## 本章与后续章节的衔接

- **→ 第 2 章**：本章给出"Chainlink 卖什么"，第 2 章回答"它在链上金融利润池中拿哪一层价值"——承接 1.3 的 TradFi 类比，继续向外部化（利润分层、议价能力、生态位扩张边界条件）。
- **→ 第 3 章**：本章提到"2017 后无第二轮股权融资"、"基金会钱包批量释放"，第 3 章承接为资本路径与承诺-交付审计的独立章。
- **→ 第 4 章**：本章的产品矩阵表里标注的 ~273M 非流通 LINK，在第 4 章展开为释放节奏、基金会行为、净供给压力的独立分析（与第 7 章价值捕获严格分开）。
- **→ 第 6 章**：本章的产品矩阵是**定性轮廓**；第 6 章的产品矩阵是**按营收、按采用质量、按飞轮闭合**的深化版，并扩展到"机构合作：公告 → 试点 → 生产 → 营收"的完整 Tier 表。
- **→ 第 10 章**：本章否定 Bloomberg/MSCI 类比、肯定 SWIFT 类比这一定性判断，是第 10 章拒绝使用 Bloomberg P/S 乘数的前置条件。
