# 第 2 章　Chainlink 在链上金融中的位置与利益地位

> **回答**：它在整个链上金融体系里占哪一层，拿哪一层价值。
>
> **本章核心命题**：把"生态位"真正**外部化**——不从 Chainlink 自己视角看"我们覆盖了哪些合作方"，而从链上金融产业链**其他五类玩家**（发行人 / 交易撮合 / 协议 / 公链 / 机构）的视角，看 Chainlink 在他们的利润与成本结构中**拿哪一层、几 bps 的价值**。
>
> **数据截止**：2026-04-21。

---

## 2.0 本章 BLUF

### 2.0.1 一张图看清 Chainlink 的位置

把链上金融利润池由上游到下游摊开，Chainlink 的位置在**中间件层**，并且**在该层内部也不是独占者**：

| 层级 | 主要参与方 | 年化营收 / 收益规模 | 占利润池比重 | 本章第几节展开 |
|---|---|---|---|---|
| **① 发行人层**（稳定币、RWA、代币化基金） | Circle、Tether、BlackRock BUIDL、Franklin、Ondo、Securitize | **数十亿至逾 $100 亿美元**[第三方聚合] | **最大单层** | §2.4 |
| **② 交易撮合层** | CEX（Binance、Coinbase）、DEX（Uniswap 前端、Hyperliquid） | CEX **~$10B+**、DEX **$1–2B**[第三方聚合] | 大单层 | §2.2、§2.5 |
| **③ 协议 / 应用层** | Aave、Morpho、Sky/Maker、GMX、Jupiter、Synthetix 等 | 合计 **~$500M–1B** 协议营收[第三方聚合] | 中等 | §2.2 |
| **④ 基础设施 / 中间件层（Chainlink 所处）** | **Chainlink ~$55–75M**、Pyth ~$1–5M、LayerZero ~$数千万级[第三方聚合] | **整层总和低于两位数亿美元** | §2.1、§2.5、§2.6 |
| **⑤ 公链 / L1 L2 层** | Ethereum、Solana、Arbitrum、Base、Optimism、Polygon、众多 SCALE 链 | L1/L2 直接 fee / MEV 另计 | §2.3 |

### 2.0.2 本章的三条结论

1. **[研究判断] Chainlink 处于"价值承载极大、价值捕获极小"的结构性位置**。对链上金融 Value Secured $100B+、TVS 巨额流量只取 <10 bps 的实证 take rate——这与 TradFi 的 SWIFT 非常像（SWIFT 对全球 $150T+ 跨境消息流只收约 €1B 费用），与 Bloomberg / MSCI / DTCC 都**不类比**。这是"生意位置"的宿命，不是"产品不够好"的问题。
2. **[研究判断] 议价能力的高低在不同对手方之间差异巨大**——对蓝筹低频 DeFi 蓝筹（Aave / Compound / Synthetix）有较强锁定、对 SCALE 补贴链是"补贴方"而非收费方、对机构合作方**目前几乎没有议价能力**（0 条公开付费披露）。本章要说清楚这三类对手方上 Chainlink 的定价权差异，而不是给出单一议价能力评级。
3. **[研究判断] 生态位扩张到"基础设施网络"一层需要同时满足三个边界条件**：(a) 消息层 take rate 在 LayerZero 竞争下不被压到 <1 bps；(b) SVR 从 Aave 扩散到 Compound / Spark / Morpho / Gearbox 至少 2–3 家；(c) 机构合作方中至少有 1 家（最可能是 DTCC H2 2026 controlled production）出现**公开可审计的付费披露**。三条全部失败则 Chainlink 被锁定在 "SWIFT 量级中间件" 天花板；任一条成功则打开向 "SWIFT + 轻量 MSCI/S&P" 混合的空间；三条同时成功才支持"基础设施网络"定位——目前**三条都未出现标志性拐点信号**。

### 2.0.3 本章不回答什么（边界复述）

| 问题 | 归属 |
|---|---|
| 代币供给 / 基金会释放 / 净供给方程 | 第 4 章 |
| 协议收入如何传导到 LINK 需求、Reserve、Payment Abstraction | 第 7 章 |
| 监管对机构合作商业化节奏的影响 | 第 9 章 |
| 2027–2028 牛市估值点位与 TradFi 乘数敏感度 | 第 10 章 |
| 产品形态与商业成熟度分层 | 第 1 章（已完成） |

本章只回答**"它在链上金融产业链中的位置与议价能力"**。

---

## 2.1 在链上金融利润池中的位置

### 2.1.1 链上金融五层利润池的定性排序

先把五层利润池**不加任何对 Chainlink 的价值判断**地排序，完全从外部价值创造视角看：[研究判断 + 第三方聚合]

**第 1 层 · 发行人（RWA 发行方 & 稳定币）** — 年化利润池**数十亿美元**
- Circle 2024 revenue ~$1.7B（USDC reserve income）
- Tether 2024 reported profit ~$13B（reserve yields）
- BlackRock BUIDL / Franklin / Ondo / Securitize 合计管理费收入规模在**数亿美元**级，并快速增长
- 利润来源：储备金利差、管理费、发行费

**第 2 层 · 交易 / 撮合** — 年化利润池**逾百亿美元**
- CEX 手续费 ~$10B+（Binance、Coinbase、OKX 等）
- DEX ~$1–2B（Uniswap 前端 + Hyperliquid + GMX + Jupiter 合计）
- 利润来源：spread、手续费、清算费

**第 3 层 · 协议 / 应用** — 年化利润池**~$500M–$1B**
- Aave / Morpho / Sky / Ethena / MakerDAO 系
- GMX / dYdX / Synthetix 衍生品系
- 利润来源：利率差、杠杆费、funding rate

**第 4 层 · 基础设施 / 中间件（Chainlink 所处）** — 年化利润池**<$2 亿美元**
- Chainlink ~$55–75M
- Pyth ~$1–5M
- LayerZero 数千万美元级
- Wormhole、Chronicle、RedStone、API3 合计小规模
- 利润来源：数据 / 消息 / 执行 / 合规路由费

**第 5 层 · 公链 / L1 L2** — 年化价值**自成一类**（交易费 + MEV + 发行），本章仅讨论它与 Chainlink 的协同而非本身规模。

### 2.1.2 核心图景：三个数量级差距

把上面五层压到一张图上，只看规模：

```
发行人     | ████████████████████████████████ (数十亿 - 百亿+)
交易撮合   | █████████████████████████ (百亿+)
协议       | ██████████ (亿级)
中间件     | █ (不到 2 亿)         ← Chainlink 整层都挤在这里
公链       | (另计)
```

**[研究判断] 这张图支持两条必须内化的结论**：

- **结论一（纵向）**：Chainlink 整个**所在层**的利润池比上游发行人层、交易层小**1–2 个数量级**。这不是 Chainlink 与具体竞品之间的份额问题，是**整个中间件赛道在链上金融利润池中的占比问题**。
- **结论二（横向）**：即使在已经很小的中间件层内部，Chainlink 仍是**份额领先者**（按 fees 计占中间件层 >50%），但 **LayerZero 的消息量是 CCIP 的 1–2 个数量级**[第三方聚合：DefiLlama / LayerZeroScan]——**按 fees 领先，但按 volume 被领先**。这个二元事实决定了 Chainlink 未来的竞争必须从"fees per unit"转向"unit volume"。

### 2.1.3 与 TradFi 最准确的对标：SWIFT

把链上金融的中间件层放到 TradFi 语境里做量级校准（**仅作量级锚，不作估值模型基础**，后者归第 10 章）：[研究判断 + 第三方聚合]

| TradFi 参照 | 年化费用规模 | 所承载的价值流 | 实证 take rate | 与 Chainlink 的相似度 |
|---|---|---|---|---|
| **SWIFT** | **~€0.85–1B** | **$150T+ 跨境流** | **~0.07 bps / ~$0.08/msg** | **最高**：低 take rate 合作社式消息路由 |
| DTCC | $2.49B revenue、$609M EBITDA | $3000T+ 结算 | ~0.0007 bps | 低（无 SIFMU / 无结算最终性） |
| MSCI | ~$800M index licensing | $6.4T linked AUM | ~1.25 bps | 低（无指数 IP） |
| S&P / Moody's | 各 $4B+ | 发行量 $10T+ | 1–7 bps on issuance | 低（无 NRSRO） |
| Bloomberg | ~$10–11B | seat 订阅 | N/A | 低（无终端 workflow） |
| ICE / LSEG | 各 $5–10B | 交易 notional $ 千亿级 | 0.5–5 bps | 低（无交易所许可） |

**[研究判断] Chainlink 在链上金融利润池中的位置，与 SWIFT 在 TradFi 跨境支付利润池中的位置最接近**：承载全球级价值流但只取极低 take rate、合作社式治理叙事、消息/证明层功能定位。**但这不是估值类比** —— SWIFT 是合作社（微利 / cost recovery），Chainlink 是代币化网络 + 营利 Labs 混合结构，经济学驱动力不同。**本章把 SWIFT 类比定位为"生态位定性锚"，不定位为"乘数估值模板"**。（估值处理留给第 10 章。）

**这一判断**[研究判断]**同时否定两种极端误判**：
- ❌ "Chainlink 是 DeFi 的 Bloomberg" — 忽略 Chainlink 不产生专有数据、没有终端订阅锁定、没有 chat network effect
- ❌ "Chainlink 是 Web3 的 DTCC" — 忽略 Chainlink 没有 SIFMU 地位、没有结算最终性、没有监管特许

### 2.1.4 【待补证据】

- 2024 / 2025 两个财年五层利润池的逐层独立核验（目前依赖 Token Terminal / DefiLlama 聚合，需与 Messari State of Finance Q4 2025 / Q1 2026 交叉）
- 中间件层内部 Chainlink / LayerZero / Pyth / Wormhole 按 volume-weighted 与 fees-weighted 两个维度的份额时间序列（2023–2026 月度）
- SWIFT 2024 / 2025 年报中对 RTP / ISO 20022 数字化项目收入单独分拆的数据（若可得）

---

## 2.2 与 DeFi 协议的关系与替换成本

第 1 章 §1.4 从 Chainlink 自身视角给出了"控制点 vs 插件"矩阵。本节**反向**——从 **DeFi 协议视角**看"如果我是 Aave / Morpho / Maker 的风险委员会，我为什么用 Chainlink、我什么时候会换、我换的代价是什么"。

### 2.2.1 DeFi 协议为什么用 Chainlink：三类真实动因

[研究判断 + 官披]

1. **历史路径依赖（最重要）**：Aave / Compound / Synthetix 在 2020–2021 年选择 Chainlink 是因为**当时没有其他成熟的去中心化价格预言机**；切换需要完整重构清算逻辑 + 社区治理投票 + 新增审计。**这不是"Chainlink 比竞品好"，而是"2020 年的 Chainlink 是唯一可选项"**——这一条在 2026 年讨论 Chainlink 护城河时必须承认。
2. **运营记录（第二重要）**：7 年 $100B+ TVS **无重大预言机攻破事件**[研究判断 + 社区共识]，是任何新进入者最难在短期内追上的资产——新预言机要在一个蓝筹协议中从 0 建立这种信誉至少需要 2–3 年无事故运行。
3. **合规 / 品牌叙事（第三重要）**：当 DeFi 协议想吸引机构资金或面对监管时，"我用 Chainlink" 是最低成本的合规叙事——类似"我用 AWS" 在 TradFi。

### 2.2.2 已经发生的三种"去 Chainlink 化"形态

**[官披 + 研究判断] 这是本节最需要被 buy-side 重视的部分**——2024–2026 年蓝筹 DeFi 出现了三种**结构性去 Chainlink 依赖**的架构决策，且**都不是因为 Chainlink 产品出了问题，而是架构哲学问题**：

| 形态 | 代表协议 | 架构决策 | 对 Chainlink 的含义 |
|---|---|---|---|
| **① 多预言机 fallback** | Aave V3 / V4 | 保留 Chainlink 为主，但架构层面允许 fallback 到其他 oracle | Chainlink 仍是 primary，但**不是 sole**——定价权边际下降 |
| **② 预言机中立化** | Morpho Blue | 协议层面设计为"任何预言机皆可接入"，由 market creator 选择 | Chainlink 从 **必选项 → 可选项**；市占率成为商业竞争结果而非架构默认 |
| **③ 主动替换** | Maker / Sky → Chronicle | Chronicle 是 MakerDAO 内部孵化的 oracle，2023–2024 完整替换 Chainlink | **最强的去 Chainlink 信号**——蓝筹 DeFi 原生协议**用自建方案替换** Chainlink |

**[研究判断] 这三种形态在 2022 年前都不存在**。它们在 2023–2026 间的出现说明：**蓝筹 DeFi 对"单一外部预言机依赖"的架构风险偏好已经实质变化**。Chainlink 在新一轮蓝筹协议（Morpho、Ethena 等）中**不再是默认集成**。这一架构哲学转变**比任何新竞品（Pyth、RedStone）的单点切入都更具长期威胁**。

### 2.2.3 替换成本的量化刻度

对具体单一协议，把"替换 Chainlink"的真实成本按量级分档：[研究判断]

| 成本项 | Aave（已集成 7 年，$45B+ TVL） | 新蓝筹（Morpho、Ethena，2–3 年内选型） | 新小协议 |
|---|---|---|---|
| 工程工时 | 6–12 个月跨团队 | 1–3 个月 | 数周 |
| 清算风控重验证 | 复杂（涉及坏账模型） | 中等（模块化设计） | 低 |
| 社区治理流程 | 链上提案 + 多轮投票 + 审计 | 同上但流程更轻 | DAO 内部决定 |
| 品牌 / 市场沟通成本 | 高（易引发 FUD） | 中 | 低 |
| **综合切换成本** | **高（接近结构性锁定）** | **中等（可比选）** | **低（近似插件）** |

**[研究判断] 一个反直觉的推论**：Chainlink 对**已有蓝筹**的锁定是**"向后看"的**（基于历史集成 + 信誉积累），对**新蓝筹**的锁定是**"向前争取的"**（架构中立化环境下的公平竞争）。这意味着 Chainlink 在新一代蓝筹（Morpho、Ethena、Lighter、Hyperliquid 等）中的表现**不能简单外推自 Aave 的锁定**——**在新一代蓝筹中，Chainlink 正在失去结构性优势**。

### 2.2.4 SVR × Aave 是否"重塑"了这层关系

SVR（Secondary Value Recapture）是 2025 年出现的新现象，值得单独问：**它是否把 Chainlink 与 Aave 的关系从"供应商"升级到了"利润分成合伙人"？** [研究判断]

- **是的一面**：SVR 结构让 Chainlink 从 Aave 清算事件中直接分成（初始 6 个月 65/35 → 后期 60/40），**这是 Chainlink 9 年来首次以协议共治结构获得 Aave 收入的一部分**。9 个月 Chainlink 生态分成 $5.6M、近月度 $1.5–2M[第三方聚合：Aave blog + Chaos Labs + Chainlink 官推三方交叉]。
- **不是的一面**：SVR 合约仍由 Aave 治理控制；Aave 可以随时通过治理提案调整分成比例或切换到竞品（API3 的 OEV Share 已在 **Compound** 治理论坛活跃竞标）；SVR 不是 Chainlink 对 Aave 的**结构性议价提升**，而是**双方共建的一次新分配机制**——对 Chainlink 是增量，对 Aave 是 MEV 回收工具。
- **[研究判断] 正确定性**：SVR × Aave 是**可复制模板的起点**（如果扩散到 Compound / Spark / Morpho / Gearbox）或**一次 pilot 结束**（如果止步于 Aave 一家）。**2026–2027 这个问题的答案直接决定 Chainlink 与 DeFi 协议关系能否从"供应商"升级为"利润共享合伙人"**——这是 §2.6 边界条件之一。

### 2.2.5 【待补证据】

- Morpho Blue 上线以来（2024-01 至今）market creator 对各预言机的选择分布（Dune 可查）
- 任一蓝筹协议治理论坛关于 "切换预言机"的投票历史与工程工时预估
- Aave 2024–2026 任何提及将 Chainlink 分成比例从 65/35 → 60/40 → 更低的治理提案草案
- API3 OEV Share 在 Compound 治理论坛的竞标进度
- Ethena / Lighter / Hyperliquid 等 2024 后新蓝筹的预言机选型决策文档

---

## 2.3 与公链的关系（SCALE 等）

这一层在既有研究中经常被忽略，但它是 Chainlink **"向下游公链要补贴"还是"向下游公链收费"**的基本盘问题。[研究判断]

### 2.3.1 SCALE 计划是什么（官方产品事实）

[官披] Chainlink SCALE（Sustainable Chainlink Access for Layer 1s and Enhanced chains）是 2022-07 推出的计划。本质：**公链（L1/L2）向 Chainlink 支付一笔多年期代币补贴**（通常是公链原生代币），换取 Chainlink 在该链上**免费或低成本部署主要预言机服务**。已知参与方包括 Moonbeam、Moonriver、Metis、Avalanche、Fantom 等。

**这是一种与 DeFi 直接付费模式完全相反的关系**：在 DeFi 层 Chainlink 是收费方；在 SCALE 公链层 Chainlink 是**被补贴方**。

### 2.3.2 为什么公链愿意补贴 Chainlink

[研究判断]
1. **冷启动需求**：新 L2 / alt L1 在没有 Chainlink 接入前，其上 DeFi 协议要么无法启动、要么必须接受显著更弱的预言机方案。Chainlink 接入是一种**生态完整性信号**。
2. **合规叙事**：公链想吸引机构或 RWA 部署，"Chainlink 已在本链"是一条重要合规叙事。
3. **代币交换而非现金**：公链用**自身原生代币**补贴，现金成本为 0；但这等于把公链代币价值稀释一部分给 Chainlink。

### 2.3.3 对 Chainlink 的意义与局限

**意义**[研究判断]：
- SCALE 计划让 Chainlink 在**营收规模极小的情况下**维持了**最广的链覆盖**（30+ 条链），形成"产品广度"叙事的基础
- 补贴代币构成 Chainlink Labs / Foundation 资产负债表中的**非 LINK 加密资产储备**（规模未披露）

**局限**[研究判断]：
- SCALE 公链**通常不是 DeFi 流量的主要产生方**。Arbitrum 和 Base（CCIP 费用主产地，Q1 2024 合计占 CCIP 费用 52%[第三方聚合]）**不是 SCALE 公链**；SCALE 公链的实际 DeFi 流量大多不活跃。
- 补贴期结束后的**留存率未披露**。Moonbeam、Metis 等 SCALE 链在补贴期结束后是否能产生可持续费用，是结构性未知。**这是 Chainlink 链覆盖数据的真实含金量测试**。
- SCALE 补贴的经济实质是"**Chainlink 拿公链代币作为收入的一部分**"——如果这些代币价值在 2022–2026 熊市中大幅缩水，则 Chainlink 的有效补贴收入**被持仓 mark-to-market 损失严重稀释**[研究判断]。

### 2.3.4 与主流链（Ethereum / Solana / Arbitrum / Base）的关系定性

这四条链是 Chainlink **真正的 DeFi 费用主产地**[第三方聚合]，关系形态与 SCALE 公链完全不同：

- **Ethereum**：Chainlink 的原始主战场，fees 大头；Chainlink 不向 Ethereum 付费、也不收 Ethereum 补贴——是**共生中立关系**。
- **Solana**：CCIP v1.6（2025-05-19）首次进入非 EVM 链[官披]，但 Solana 生态的主要预言机仍是 Pyth（Pyth 诞生于 Solana）——Chainlink 在 Solana 是**后进入挑战者**，结构上弱势。
- **Arbitrum / Base**：CCIP 费用主产地，SVR 扩展的首选 L2。**Base 与 Coinbase 关联性**使得 Chainlink 与 Coinbase 机构业务（cbBTC 等）形成间接绑定。
- **Optimism / Polygon / Avalanche**：中等流量，不属于最核心。

### 2.3.5 生态位判断：Chainlink 是公链的"中立插件"而非"控制点"

[研究判断] **Chainlink 对公链没有议价能力**。证据：
- 公链可以拒绝 Chainlink（Solana 大部分 DeFi 用 Pyth、Sui 生态多样化、Hyperliquid 自建）
- 公链可以补贴竞品（RedStone、Pyth 都在与公链签类似 SCALE 的协议）
- 公链升级协议不需要 Chainlink 许可

**反过来**，Chainlink 对公链也没有下游锁定：Chainlink 节点可以停止支持任一链、Chainlink 产品可以在任一链上部署或撤销。

**这是一种典型的"双向中立"关系**——对估值含义是：**不要把"Chainlink 覆盖 30+ 链"当作链相关收入的稳定来源**，这更像"地理覆盖广度"，不是"地理锁定深度"。

### 2.3.6 【待补证据】

- SCALE 各参与公链补贴期结束的具体时间点与续约状态
- Chainlink Labs / Foundation 持有的非 LINK 加密资产储备规模（包括 SCALE 补贴代币）
- Moonbeam / Metis / Moonriver 等 SCALE 链补贴期结束后实际 Chainlink 产品留存率
- Solana 生态中 Chainlink Data Streams vs Pyth 的份额时间序列（2025–2026）

---

## 2.4 与机构 / RWA 的关系形态

这是全报告中**叙事最热、商业证据最薄**的区域，也是第 2 章**最需要外部化、最需要 buy-side 纪律**的小节。

### 2.4.1 "机构合作"的三种层次必须分清

[研究判断] Chainlink 与机构的关系至少有三种本质不同的层次，混淆会直接导致估值误判：

| 层次 | 含义 | 代表案例 | 对营收的含义 |
|---|---|---|---|
| **A · 技术集成** | Chainlink 产品在机构系统中作为技术栈一部分部署 | DTCC Smart NAV 使用 Chainlink CCIP | **不等于付费**；可能是 PoC 阶段免费部署 |
| **B · 商业生产** | 机构使用 Chainlink 承载真实客户资金流 | Fidelity International + Sygnum（$50M Matter Labs 国库） | **可能象征性付费或接近零费**；规模未披露 |
| **C · 规模化付费** | 机构 10-K / 年报披露对 Chainlink 的付费线条 | **目前零案例** | **真正可审计的机构营收** |

**[研究判断 + 公开检索] 截至 2026-04，没有任何一家机构合作方进入 C 层**。SWIFT、DTCC、UBS、Fidelity International、ANZ、Mastercard、SBI、J.P. Morgan Kinexys、21X 的公开年报 / 季报 / 10-K 中**无 Chainlink 付费线条**。这是本节的**锚**。

### 2.4.2 已有合作的 Tier 分层（外部视角）

按"从机构客户视角看，他们付出了什么、锁定了什么"重新整理（而非从 Chainlink 视角罗列合作方名单）：[研究判断 + 官披]

| 机构 | 实质性质 | 机构付出 | 机构锁定程度 | 商业化 Tier |
|---|---|---|---|---|
| **SWIFT** | 2022 起多次 CCIP 试点；2025 Sibos Phase 2 "Corporate Actions" 产业联合体；2025 Business Challenge 获奖 | 技术团队时间 + 试点场地 | 极低（同期与 LayerZero 通过 DTCC 间接接触） | **Tier 2 (PoC/pilot)**[研究判断] |
| **DTCC Smart NAV** | 2024-05 试点；2025 Sibos Phase 2 企业行动；SEC No-Action Letter 下 H2 2026 controlled production | 合作关系 + SEC 合规文件 | 中（三年期 controlled pilot，仅 DTC 参与者） | **Tier 3 / 3.5 (Pre-production, controlled)**[研究判断 + 官披] |
| **Fidelity International + Sygnum** | 2024-07 NAV feed 正式运行；底层仓位为 Sygnum $50M Matter Labs 国库投入 Fidelity $6.9B Liquidity Fund | 少量开发对接 | 低（单一小规模 tokenized 仓位） | **Tier 4 (Production live, 但 $50M notional)**[研究判断] |
| **UBS Project Guardian** | MAS sandbox 试点；Sibos 2025 DTA 标准首采 | 合规 sandbox 时间 | 极低 | **Tier 2 (PoC)**[研究判断] |
| **ANZ e-HKD** | 跨链 CCIP 试点 | 技术团队时间 | 极低 | **Tier 2 (PoC)**[研究判断] |
| **SBI Digital Markets** | 2025 声明 "exclusive infrastructure" | 声明级合作 | 未披露 | **Tier 1-2 (Announcement/PoC)**[研究判断] |
| **Mastercard / Swapper Finance** | 2025-06 on-ramp rail 上线；"3B+ cardholders" 为 TAM 不是使用量 | 商务对接 | 极低 | **Tier 2-3 (小众 on-ramp)**[研究判断 + 官披] |
| **J.P. Morgan Kinexys** | Kinexys + Ondo Chain + Chainlink 跨链 DvP 试点 | 试点技术资源 | 低 | **Tier 2-3 (PoC → Pre-production)**[研究判断] |
| **21X (Germany)** | MiCA 监管代币化交易所集成 | 合作关系 | 低 | **Tier 2 (PoC)**[研究判断] |

**[研究判断] 这张表读出两个外部化的判断**：

1. **机构合作的"路径斜率"不是线性向上的**。SWIFT 从 2022 年第一次试点到 2026 年，四年后仍在 Tier 2；**合作停留时间远长于早期市场预期**。这不是 Chainlink 的问题，是**机构代币化本身的采纳速度问题**——但它直接压制了估值模型中"机构营收爆发"的时点假设。
2. **机构不独占 Chainlink**。DTCC / ICE / Citadel Securities 在 2026-02 同时投资 LayerZero Labs（Zero L1）[官披 + 第三方媒体：Fortune / CoinDesk / BusinessWire]。**机构的态度是"双押"而非"站队"**——这是对"机构独占通道"叙事的直接证伪。

### 2.4.3 机构为什么选 Chainlink：三条真实动因

[研究判断] 剥离营销话术，机构选择 Chainlink 的真实动因只有三条：

1. **合规摩擦最低**：Chainlink Labs 长期与监管沟通（CFTC 顾问委员会席位、SEC Project Crypto、多次 SEC Corp Fin 声明覆盖）、有 ISO 27001 + SOC 2 认证[官披]。对机构法务团队而言，**选 Chainlink 不需要向内部风险委员会多做 6 个月合规解释**。
2. **品牌风险最低**：Chainlink 是加密中最"安全"的机构选择——7 年无重大事故 + 品牌认知度 + 媒体曝光度。**选 Chainlink 出事也不会被内部问责**。
3. **不涉及代币持仓**：机构不需要为了使用 Chainlink 持有 LINK（Payment Abstraction 之后任意代币付费），这降低了内部代币持仓合规障碍——这一点在 2025 年 Payment Abstraction 上线后才成立[官披]。

**这三条都是"最低阻力"型理由，不是"最高价值"型理由**。这意味着**机构对 Chainlink 的付费意愿天然偏低**——他们选 Chainlink 是因为"不用它更麻烦"，不是因为"用它能赚更多钱"。这个动因结构直接预测了机构合作 C 层（规模化付费）的到来会**慢而稳，不快而大**。

### 2.4.4 DTCC H2 2026 是本小节最重要的观察窗

[研究判断 + 官披] DTCC Smart NAV 2026 H2 进入 SEC No-Action Letter 覆盖下的 controlled production pilot（三年期，仅 DTC 参与者可用，覆盖 Russell 1000 股票、主要 ETF、美债等高流动性资产）是**机构合作从 Tier 3 → Tier 3.5 的关键节点**，也是**机构采纳→营收传导的第一次真实测试**。

**三个观察点**（2026 H2 至 2027 H1 逐条跟踪）：

1. **付费结构**：定额 license / per-call / DTC 参与者代付 / Chainlink Labs 直接收费 —— 四种模式对 Chainlink 的会计与税务结构影响完全不同
2. **规模**：DTCC 三年 pilot 是否会把 Chainlink 营收从 $60M 推到 $100M 量级
3. **披露**：DTCC 是否会在任一期财报或 investor day 中披露 Chainlink 付费线条——如果不披露，意味着**即使 Tier 4 也不会自动转化为可审计营收**

### 2.4.5 【待补证据】

- DTCC No-Action Letter 原文（SEC.gov/divisions/corpfin/cf-noaction）与付费结构相关条款
- DTCC 2026 Q3 / Q4 投资者交流中是否披露 Chainlink 付费
- 任一 SWIFT member / DTC participant 在其年报中披露加密基础设施付费的前例
- LayerZero Zero L1 上线（~2026-10/11）后，DTCC 是否把 Smart NAV 流量分流到 Zero
- Sygnum / Fidelity International 任一季报中 Matter Labs tokenized 产品的费用线条
- SBI Digital Markets "exclusive infrastructure" 的排他条款文本

---

## 2.5 利益地位与议价能力

本节把 §2.2–§2.4 的分类合并为一张"议价能力矩阵"，给出 Chainlink 对**五类对手方**的议价能力评级。[研究判断]

### 2.5.1 五类对手方的议价能力矩阵

| 对手方 | Chainlink 相对议价能力 | 核心证据 | take rate 实证 |
|---|---|---|---|
| **蓝筹低频 DeFi（Aave / Compound / Synthetix）** | **中等偏强** | 7 年集成、$100B+ TVS、切换成本高 | Data Feeds 类请求年化 $55–70M 来自此类客户占主要 |
| **新一代蓝筹 DeFi（Morpho / Ethena / Lighter）** | **中等** | 架构中立化，Chainlink 与 Pyth / RedStone / Chronicle 公平竞争 | 按客户定价，无溢价 |
| **高频衍生品（Hyperliquid / Jupiter / GMX）** | **弱** | Pyth pull 模型结构优势，Chainlink 是后进入 | Data Streams 规模小、未独立披露 |
| **RWA 发行方（BUIDL / Franklin / Ondo / Securitize）** | **极弱** | 上游发行方**未把 Chainlink 当默认层**（BUIDL 用 Securitize+RedStone、Ondo 自建 DVN、Figure 自建链） | 基本零付费 |
| **机构合作方（SWIFT / DTCC / UBS / Fidelity / 其他）** | **零到极弱** | **0 家公开披露付费**；合作是"合规摩擦最低"而非"最高价值" | 目前无可审计付费 |
| **公链（SCALE 补贴链）** | **反向议价**（Chainlink 拿补贴） | SCALE 下 Chainlink 是被补贴方 | 负 take rate（Chainlink 收公链代币补贴） |
| **公链（Ethereum / Solana / Arbitrum / Base）** | **无议价关系** | 共生中立，无锁定、无补贴 | N/A |

### 2.5.2 "take rate 极低 ≠ 定价权极低"这一常见误判的纠正

[研究判断] 一个需要辩证处理的点：Chainlink 实证 take rate <10 bps，这**表面上**读作"议价能力弱"。但必须澄清：

- **对单一 DeFi 协议客户**，Chainlink 的 take rate 实际上是 **协议提议 → Chainlink 接受** 的定价结构（客户在风险委员会提议 oracle 预算，Chainlink 接受或不接受），不是 Chainlink 主动定价。在这个结构下，take rate 低反映的是**整个预言机赛道的客户议价强势**，不是 Chainlink 特别弱。
- **与 SWIFT / DTCC 等 TradFi 低 take rate 基础设施一致**——消息层 / 路由层 take rate 历史上就是被压缩到 <1 bps 的（§2.1.3）。**这是位置宿命，不是 Chainlink 个例**。
- **对蓝筹 DeFi 老客户**，Chainlink 能维持当前费率说明**竞品并未给出更便宜 / 等质的替代**——这反而是"软定价权"的存在证据。

**结论**：Chainlink 的议价能力**不是"极弱"，是"极度不均匀"**——对蓝筹老客户中等偏强，对新客户与机构接近零，对公链是反向议价。**用单一议价能力评级讨论 Chainlink 会系统性产生误判**。

### 2.5.3 定价权升级的两条路径与各自可行性

[研究判断] Chainlink 要从"SWIFT 量级 take rate" 升级到"MSCI/S&P 量级 take rate"，理论上只有两条路径：

| 路径 | 机制 | 当前可行性 | 上限 |
|---|---|---|---|
| **① 把 SVR 模式复制到 MEV 回收以外的价值分成场景** | 从清算 MEV 扩展到前置跑动保护、批量拍卖、抢跑排序 | 中（技术可行，商业谈判难） | DeFi OEV 总池，乐观 $50–100M/年 Chainlink 生态分成 |
| **② 通过 CRE 把自己从"数据中间件"抬升到"企业工作流运行时"** | 机构代币化 end-to-end 编排，绑定 DTCC / SWIFT / UBS | 低-中（商业采纳速度慢） | 理论上数亿美元级，但需 5–7 年 |

**[研究判断] 两条路径都不是"当前可观测的加速状态"**。SVR 仍止步于 Aave 一家；CRE 仍在试点阶段无独立付费。**2026–2027 定价权升级的关键观察点**：SVR 能否从 Aave 扩散到至少第二家蓝筹借贷协议 + CRE 能否在 DTCC H2 2026 pilot 中出现付费迹象。两条任何一条成功都会让本小节的议价能力矩阵重估；两条同时失败则 Chainlink 被锁定在当前 take rate 结构内。

### 2.5.4 【待补证据】

- SVR 从 Aave 扩散到第二家蓝筹的治理进度
- CRE 在 DTCC / SWIFT 试点中是否有付费条款
- 任一 DeFi 协议与 Chainlink 的合同条款披露（通常为机密，需通过治理论坛反推）
- Chainlink Labs 对"预言机赛道客户议价强势"的任何公开陈述

---

## 2.6 生态位扩张的边界条件

本节把前五节合并为**三个可观测的边界条件**——它们的达成度决定 Chainlink 从"SWIFT 量级中间件"向"SWIFT + 轻量 MSCI/S&P 混合基础设施网络"升级的可能性。这是本章的**收束**，也是第 10 章估值情景分化的关键输入。

### 2.6.1 边界条件 A：消息层 take rate 能否守住

**阈值**[研究判断]：CCIP take rate 在 LayerZero / Wormhole / IBC / 银行自建桥竞争下不被压到 **<1 bps**（TradFi 消息层长期均衡水平）。

**当前状态**：CCIP 实证 take rate 6.3–7 bps on notional、~$0.09/msg；LayerZero 免费或极低 fee 模式、Wormhole 免费[第三方聚合]。**LayerZero 在消息量上领先 CCIP 1–2 个数量级**。

**观察信号**：
- 任何 CCIP 主动降费提案（2026 H2 – 2027）
- LayerZero Zero L1 上线（~2026-10/11）后 DTCC / ICE 的流量分配结果
- CCIP 在非 EVM 链（Solana）的 take rate 能否维持

**失败的代价**：Chainlink CCIP 变成"volume scaling only, no pricing power"的纯规模生意——与 SWIFT 一致，但无 SWIFT 的 13.4B 消息/年规模。

### 2.6.2 边界条件 B：SVR 能否扩散

**阈值**[研究判断]：SVR 从 Aave 一家扩散到 Compound / Spark / Morpho / Gearbox **至少 2–3 家**在 2026 年内。

**当前状态**：SVR 仅在 Aave V3 Ethereum / Arbitrum / Base 部署；API3 OEV Share 已在 **Compound** 治理论坛竞标[研究判断 + 第三方]。

**观察信号**：
- Compound / Spark / Morpho 的 SVR vs API3 OEV 治理投票结果
- Chainlink 官方对 SVR 扩散的季度进度披露
- SVR 月度 Chainlink 生态分成从 $1.5–2M 是否突破 $5M

**失败的代价**：SVR 被锁定为"Aave 单协议 pilot"，无法转化为可复制的价值分成模板；Chainlink 失去从"SWIFT 式 take rate" 向"MSCI 式 take rate" 升级的主要路径。

### 2.6.3 边界条件 C：机构合作能否从 Tier 3 → Tier 4

**阈值**[研究判断]：**至少 1 家**机构合作方在 2027 年底前出现**公开可审计的 Chainlink 付费披露**（最可能候选：DTCC H2 2026 controlled production）。

**当前状态**：0 家。Fidelity International + Sygnum 是 Tier 4 (Production live) 但规模 $50M、付费未披露。

**观察信号**：
- DTCC 2026 Q3 / Q4 / 2027 Q1 / Q2 投资者沟通中是否出现 Chainlink 付费线条
- SWIFT 2026 / 2027 年报中 Corporate Actions 项目收入分拆
- 任一 DTC 参与者 / SWIFT member 在其年报中披露加密基础设施付费

**失败的代价**：机构合作永久停留在"采纳证据"阶段，不转化为"商业化验证"；估值模型中"机构营收爆发"的时点假设被永久推后。**这是三个边界条件中对估值影响最大的一个**。

### 2.6.4 三边界条件的组合情景

[研究判断] 三个边界条件的组合决定生态位扩张的四种情景：

| 情景 | A 消息层 | B SVR 扩散 | C 机构 Tier 4 | 生态位定性 | 估值含义（归第 10 章） |
|---|---|---|---|---|---|
| 全部失败 | take rate 压至 <1 bps | 止步 Aave | 零付费 | **锁定在 SWIFT 量级中间件** | 熊情景基准 |
| 仅 B 成功 | take rate 压缩 | 扩散到 2–3 家 | 零付费 | SWIFT + MEV 专业化 | 基准情景 |
| 仅 C 成功 | take rate 压缩 | 止步 Aave | DTCC 付费披露 | SWIFT + 单一机构现金流 | 基准情景偏乐观 |
| B + C 同时成功 | take rate 部分守住 | 扩散 + 机构付费 | ≥1 家 Tier 4 | **SWIFT + 轻量 MSCI/S&P 混合基础设施** | 牛情景基础 |
| A + B + C 全部成功 | take rate 守住 + B + C | — | — | **真·基础设施网络** | 超级牛情景基础 |

**[研究判断] 当前（2026-04）三个边界条件都未出现标志性拐点信号**。这是本章对第 10 章的**最直接输入**：**任何主情景假设都必须明确列出 A/B/C 三条边界条件的哪一条假设已经成立**，不能默认成立。

### 2.6.5 【待补证据】

- CCIP 月度 take rate 时间序列（2023-07 主网上线至今，DefiLlama + 官方 dashboard 交叉）
- LayerZero / Wormhole 月度 take rate 对照时间序列
- SVR 扩散的季度进度（Compound / Spark / Morpho / Gearbox / 其他）
- DTCC / SWIFT / UBS / Fidelity International 2026–2027 每季度对 Chainlink 提及的内容审计

---

## 本章与后续章节的衔接

- **→ 第 3 章**：本章指出 Chainlink Labs / Foundation / Network 三主体的"利益地位"差异（Labs 可以从机构合作中获得现金流、Foundation 通过释放 LINK 获得现金流、LINK 持有人既不拿 Labs 股权也不拿 Foundation 裁量权）——这一结构性错位由第 3 章展开。
- **→ 第 4 章**：§2.3 提到 SCALE 补贴代币构成 Foundation 资产负债表中的非 LINK 储备，这与第 4 章 LINK 代币供给分析的边界需要在第 4 章厘清。
- **→ 第 5 章**：§2.2–§2.4 的"需求真实性"定性（蓝筹历史依赖 / 架构中立化 / 机构试点疲劳）由第 5 章"真实需求与场景分层"深化为定量。
- **→ 第 6 章**：§2.4 的机构合作 Tier 分层表在第 6 章扩展为"公告 → 试点 → 生产 → 营收"四档，并对每个合作加营收预测栏。
- **→ 第 7 章**：本章不讨论 Chainlink 的议价能力如何转化为 LINK 代币需求——这是第 7 章的任务。本章只给出"议价能力矩阵"作为第 7 章的输入。
- **→ 第 8 章**：本章 §2.2.2 的三种"去 Chainlink 化"形态是第 8 章"护城河衰减"的直接证据。
- **→ 第 9 章**：本章 §2.4 的"机构不独占 Chainlink、DTCC/ICE 同时投 LayerZero"是第 8、9 章共同的论据。
- **→ 第 10 章**：**§2.6 的三个边界条件（A/B/C）直接决定第 10 章的情景分化**。第 10 章的熊 / 基 / 牛 / 超级牛情景必须与本章 §2.6.4 的情景表一一对应。

---

## 附注 · 本章【待补证据】全局汇总

| # | 证据缺口 | 归属小节 | 对生态位判断的影响 |
|---|---|---|---|
| 1 | 2024–2025 五层利润池逐层独立核验 | §2.1 | 定位基础 |
| 2 | 中间件层 fees-weighted vs volume-weighted 份额时间序列 | §2.1 | 份额判断 |
| 3 | Morpho Blue market creator 预言机选择分布 | §2.2 | 新蓝筹锁定力 |
| 4 | Aave 任何 SVR 分成比例调整提案 | §2.2 | SVR 议价能力 |
| 5 | Ethena / Lighter / Hyperliquid 预言机选型文档 | §2.2 | 新蓝筹锁定力 |
| 6 | SCALE 各参与链补贴期结束时间与续约 | §2.3 | 链覆盖含金量 |
| 7 | Chainlink Labs / Foundation 非 LINK 加密资产储备规模 | §2.3 | SCALE 经济实质 |
| 8 | Solana 生态 Data Streams vs Pyth 份额 | §2.3 | 非 EVM 链地位 |
| 9 | DTCC No-Action Letter 原文与付费条款 | §2.4、§2.6 | 机构 Tier 4 前景 |
| 10 | DTCC 投资者日 / 季报中的 Chainlink 付费披露 | §2.4、§2.6 | 机构 C 层到达概率 |
| 11 | LayerZero Zero L1 上线后 DTCC / ICE 流量分配 | §2.4、§2.6 | 机构独占叙事 |
| 12 | SVR 扩散的季度进度 | §2.5、§2.6 | 定价权升级路径 B |
| 13 | CCIP 月度 take rate 时间序列 | §2.6 | 消息层 take rate 守住可能性 |
| 14 | 任一 DeFi / 机构合同条款披露 | §2.5 | 议价能力实证 |

**第 2 章不承担解决这 14 条缺口的任务；第 5、6、8 章必须分别标注"本章能解决哪几条"**。
