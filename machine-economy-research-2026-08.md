# Machine Economy / 机器经济:全球全景式投资研究报告

**研究截止时间:2026 年 8 月**

**研究性质:产业全景认知地图 + 状态变量识别 + 异动与投资机会监测体系**

---

> 本报告遵循六条研究原则:
> 1. 先建立全貌,再筛选指标;
> 2. 先研究经济活动,再研究技术实现;
> 3. Final Demand 优先于 Internal GMV;
> 4. Economic Autonomy 优先于 Wallet Count;
> 5. Value Creation 不等于 Value Capture;
> 6. 投资研究最终关心的是拐点。

**事实分层标注体系**(全文使用):

- 【事实/已规模化】— 存在真实交易、真实客户或真实收入,有可靠数据证明
- 【商业化中】— 产品已运行且存在真实付费行为,但规模有限
- 【早期】— 存在真实产品/试点/开发者活动,但经济意义尚小
- 【实验】— 技术验证、Demo 或极小规模试验
- 【推演】— 根据技术进步与经济逻辑推导的未来场景

---

## 目录

- [第一部分:定义与坐标系](#第一部分定义与坐标系)
  - 1. Machine Economy 概念史与重新定义
  - 2. 机器经济的核心坐标系
  - 3. 经济自主性光谱(E0–E5)
- [第二部分:经济结构](#第二部分经济结构)
  - 4. 最终需求来自哪里
  - 5. External Revenue 与 Internal Machine GMV
  - 6. Machine Revenue Map(机器如何赚钱)
  - 7. Machine Expenditure Map(机器为什么花钱)
  - 8. 完整 Machine Economy P&L
- [第三部分:现实与未来](#第三部分现实与未来)
  - 9. 截至 2026 年 8 月的 Current Reality Map
  - 10. 未来场景全景(21 个场景)
  - 11. 场景级早期信号
- [第四部分:基础设施与生态](#第四部分基础设施与生态)
  - 12. 基础设施 Stack(L0–L8)
  - 13. 项目生态地图
  - 14. Crypto / Stablecoin 必要性辨析
  - 15. x402 / 链上机器支付数据验证
- [第五部分:价值链与叙事证伪](#第五部分价值链与叙事证伪)
  - 16. 价值链与利润池
  - 17. Value Creation vs Value Capture
  - 18. 未来 5 / 10 / 20 年演进
  - 19. 八大叙事逐项证伪
- [第六部分:监测体系](#第六部分监测体系)
  - 20. Leading / Confirming / Catalyst 指标体系
  - 21. Machine Economy Signal Map
  - 22. 异动等级体系
  - 23. Investment Trigger Map
  - 24. 核心监测仪表盘(Core Monitoring Dashboard)
  - 25. Future Critical Metrics
  - 26. 数据源地图
- [第七部分:最终结论](#第七部分最终结论)
  - 27. 十八个投资问题的直接回答
  - 28. 三张核心地图
  - 29. Machine Economy Monitoring Framework(可执行监测框架)

---

# 第一部分:定义与坐标系

## 1. Machine Economy 概念史与重新定义

### 1.1 概念谱系:六个词各自从哪里来

**Machine-to-Machine (M2M) Economy** 是最老的概念,源于 2000 年代电信业的 M2M 通信(SIM 卡联网设备、远程抄表、车队遥测)。彼时"机器经济"只指机器之间**交换数据**,不涉及机器之间**交换价值**。

**Machine Economy** 作为"机器成为经济主体"的叙事,由 **IOTA(2015 年创立)**首次系统性提出。IOTA 联合创始人 Dominik Schiener 明确写道:"IOTA 被创造的主要原因是成为 Machine Economy 的骨干——我们设想一个机器之间纯粹 M2M 地交易资源(算力、电力、存储、带宽、数据)和服务的未来"(来源:Schiener,A Primer on IOTA,Medium)。2020 年前后,柏林的 Next Big Thing AG 给出了被工业界广泛引用的定义:"由智能、联网且经济独立的设备与机器组成的网络,它们作为自主市场参与者,在几乎无人干预下执行经济交易与其他活动"(来源:IIC Journal of Innovation,《Machine Economy – The New Frontier of Digital Transformation in IoT》,2023 年 1 月)。学术界在 2021 年 PACIS 会议上首次将其概念化(Jöhnk et al., "The Rise of the Machines: Conceptualizing the Machine Economy",拜罗伊特大学)。**这一代"机器经济"叙事的载体是 IoT + DLT + 代币经济学,并在 2018–2022 年基本被证伪**——IoT 设备没有智能,没有决策能力,无法产生真实需求,IOTA 生态至今未形成有意义的机器交易规模。

**Autonomous Economic Agent (AEA)** 由 Fetch.ai 在 2019 年前后提出,指代表所有者进行经济活动的自主软件代理。这个概念比 LLM 时代早了三年,当时缺乏真正的"智能"引擎,同样停留在框架层面。

**Agent Economy / Agentic Economy** 是 2024–2025 年 LLM Agent 浪潮的产物。学术上的正式化标志是**微软研究院 2025 年 5 月的论文《The Agentic Economy》**(Rothschild, Mobius, Hofman et al., arXiv:2505.15799,后被 Communications of the ACM 于 2026 年 1 月转载),它将 agentic economy 定义为"消费者代理与商家服务代理之间进行机器对机器协商的经济领域",并提出核心论断:**当十亿个代理代表十亿消费者面对十亿商家时,稀缺资源从注意力变成信任**。企业界(Conductor、Salesforce 等)则将 Agent Economy 定义为"数字劳动的生产、分发与消费体系"——即 AI 从辅助人类转向独立执行端到端业务流程。

**Agentic Commerce** 是 2025 年下半年由 OpenAI/Stripe(Agentic Commerce Protocol,2025 年 9 月)、Google/Shopify(Universal Commerce Protocol,2026 年 1 月)、Visa(Intelligent Commerce)、Mastercard(Agent Pay)等巨头定义的商业词汇,特指 **AI 代理代表人类完成购物交易**——本质上是电商渠道变革,而非机器成为经济主体。

**Autonomous Commerce** 目前主要被 Crypto 生态(Virtuals 的 Agent Commerce Protocol、x402 生态)使用,指代理之间自主发现、协商、支付、交付的完整闭环。

### 1.2 为什么 2025–2026 年重新快速升温

四个原因叠加:

1. **智能引擎第一次真实存在。** 2015 年的机器经济缺少"会决策的机器";2025 年的 LLM Agent 能读文档、比价格、写代码、调用 API。机器经济的第一性约束(机器没有智能)被部分解除。
2. **支付基础设施在 12 个月内集中出现。** 2025 年 5 月至 2026 年 4 月,x402(Coinbase)、AP2(Google)、ACP(Stripe/OpenAI)、UCP(Shopify/Google)、Trusted Agent Protocol(Visa)、Agent Pay(Mastercard)、AWS Bedrock AgentCore Payments 全部上线——机器经济第一次有了"钱的管道"。
3. **稳定币获得监管合法性。** 美国 GENIUS Act(2025 年 7 月签署)让稳定币从灰色地带变成受监管的支付工具,机构可以合规地给机器配"钱"。
4. **真实收入出现在数字劳动层。** Coding Agent、客服 Agent 第一次产生了数十亿美元量级的真实收入(详见第 9 节),让"机器赚钱"从叙事变成财报科目。

**关键的重新定义**:第一代机器经济(IOTA 时代)以**物理设备**为主体、以 DLT 为核心;第二代(2025–)以**软件智能体**为主体、以 LLM 为核心,支付层反而是可选组件。这个主体的迁移,是理解当前所有数据的前提。

### 1.3 从经济活动出发:什么算机器经济

判断标准不是"是不是机器",而是:**该非人类系统是否在收入、支出、资产、预算、资源配置中的至少一环拥有真实的决策参与度**。据此逐类判断:

| 对象 | 是否属于机器经济 | 判断依据 |
| --- | --- | --- |
| **Coding / Research / Customer Service / Sales Agent** | **是(核心)** | 已产生真实外部收入(按订阅/按结果计费),部分自主消费 API/算力 |
| **Trading Agent** | **是(最成熟)** | 算法交易占美股成交量过半,机器自主决策买卖已数十年,只是不被叫"机器经济" |
| **Shopping / Procurement Agent** | 是(商业化中) | 代表人类做购买决策与支付执行,是 agentic commerce 主战场 |
| **Security / Scientific Agent** | 是(早期) | 有真实产品(如自动漏洞赏金、文献研究代理),收入规模小 |
| **Robotaxi / Autonomous Truck / Drone** | **是(收入侧成立,支出侧未自主)** | 机器直接产生服务收入(Waymo 每周几十万付费订单),但收款、付费均由公司账户完成 |
| **Industrial / Warehouse Robot** | 边缘(工具属性为主) | 多数是 CapEx 设备;RaaS(按任务/小时收费)模式使其部分进入机器经济 |
| **Humanoid** | 尚未(潜在) | 2026 年仍处试点交付,无独立经济行为 |
| **GPU / Server / Storage Node** | 是(作为被交易的资源) | 算力是机器经济中最大宗的"机器卖给机器"的商品,但 GPU 本身无决策权 |
| **API / AI Model** | **是(核心商品)** | 模型 API 是机器经济中最大的支出品类;模型本身是被出售的"智能" |
| **EV / Charging Station** | 边缘→是 | 即插即充(Plug & Charge)是现实中规模最大的"机器自动支付"场景之一,但决策自主性极低(E1 以下) |
| **Smart Meter / 电力自动交易** | 是(被忽视的成熟案例) | 电力批发市场的算法自动竞价(如 Tesla Autobidder)是真实的机器自主交易 |
| **Sensor / Telecom Equipment** | 否(纯工具) | 只产生数据,不参与任何经济决策 |

### 1.4 三层定义

**狭义定义(Crypto 叙事口径)**:拥有链上钱包、能自主发起支付的 AI Agent 之间及其与服务方之间的经济活动。——本报告**不采用**此口径作为主定义,因为它会把机器经济等同于 x402 数据。

**广义定义(经济活动口径)**:一切由非人类系统作为决策参与方的价值创造、交换与分配活动,包括机器提供的劳动/服务收入、机器执行的采购与支付、机器之间的资源交易,不论结算轨道是链上、银行还是内部记账。

**本报告采用的投资研究定义**:

> **机器经济 = 非人类系统在"赚钱(Earn)—花钱(Spend)—管理损益(P&L)—配置资本(Allocate)"四个环节中,自主性持续上升所形成的经济体系。**
>
> 投资研究的对象不是"机器经济的规模",而是**四个环节上自主性迁移的速度、真实收入的规模,以及支撑这一迁移的基础设施中谁能捕获价值**。

---

## 2. 机器经济的核心坐标系

拒绝按项目(Coinbase/x402/Virtuals)组织产业,本报告采用五维坐标系:

> **经济主体(Who) × 收入方式(Earn) × 支出方式(Spend) × 最终需求方(Final Payer) × 经济自主性(Autonomy Level)**

**维度一:经济主体** — 软件智能体(Coding/Research/客服/交易/购物/采购)、物理智能体(Robotaxi/卡车/无人机/机器人)、数字机器资源(模型/GPU/API/数据节点)、基础设施机器(EV/电表/储能)。

**维度二:收入方式** — 出售数字劳动、出售智能(推理)、出售数据、出售算力、出售物理资源、金融损益、代理佣金、Agent-to-Agent 服务、物理任务收入(9 大类,详见第 6 节)。

**维度三:支出方式** — 购买智能、数据、算力、软件/API、金融执行费、实物商品、物理 OPEX、其他机器服务(8 大类,详见第 7 节)。

**维度四:最终需求方** — Consumer / Enterprise / Government / Capital Owner(交易对手盘)/ Advertiser。机器不能是最终需求方(详见第 4 节)。

**维度五:经济自主性** — E0–E5 光谱(第 3 节)。

任何一个"机器经济场景"都是这五个维度上的一个点。例如:"Waymo Robotaxi" =(物理智能体)×(物理任务收入)×(能源+维护 OPEX,公司代付)×(Consumer 付费)×(E2:自主赚钱、不自主花钱)。这个坐标系的价值在于:**它能把 x402 上 $0.001 的 API 调用和 Waymo 一年数亿美元的打车收入放进同一张地图,并立刻看出它们在哪个维度上不同。**

---

## 3. 经济自主性光谱(E0–E5)

机器是否成为经济主体,不看有没有钱包,看它在多大程度上独立完成 **Earn → Spend → P&L → Capital Allocation**。本报告采用六级光谱,并在原框架上增加两个正交修正维度。

### 3.1 六级定义

- **E0 — Human Controlled(工具)**:人决策、人付款、人收款、人管资产。机器只是执行器。绝大多数软件与设备处于此级。
- **E1 — Autonomous Spending(自主花钱)**:机器在人类设定的预算与规则内,自主选择服务、判断价格、完成支付。收入与预算完全来自人类。
- **E2 — Autonomous Earning(自主赚钱)**:机器独立完成任务并获得收入,但收入归属人类账户,支出由人管理。
- **E3 — Autonomous P&L(自主损益)**:机器同时管理收入与成本,在预算内衡量利润,形成独立损益表。
- **E4 — Autonomous Resource Allocation(自主资源配置)**:机器自主决定用哪个模型、买哪份数据、租多少算力、是否调用其他 Agent、是否停止亏损任务——即在生产函数内部做要素配置。
- **E5 — Autonomous Organization(自主组织)**:机器雇佣其他 Agent、分包任务、分配收入、进行资本配置、扩大经营规模——成为"企业"。

### 3.2 两个必须叠加的修正维度

单一光谱容易产生误判,需叠加:

1. **法律与账户归属(Ownership overlay)**:截至 2026 年,**所有**机器的资产在法律上都归属于某个人类实体。所谓 E3/E4 都是"被授权的自主",随时可被撤销。真正的分水岭不是技术能力,而是**授权的持久性与额度**(一次性授权 → 会话授权 → 常设预算 → 独立法人,最后一档 2026 年不存在)。
2. **干预率(Human Intervention Ratio overlay)**:同样是"自主赚钱",Waymo 每万单远程协助次数与一个需要人工审核每笔输出的客服 Agent,经济含义完全不同。自主性应以"每单位经济活动的人工干预次数"连续度量,而非离散分级。

### 3.3 截至 2026 年 8 月各类机器的位置判断

| 机器类型 | 位置 | 判断依据(详细证据见第 9、12 节) |
| --- | --- | --- |
| **Coding Agent** | **E1–E2 之间** | 自主消费算力/API(在人类订阅额度内);按任务/结果收费开始出现,但收入归平台公司 |
| **Trading Agent(传统量化)** | **E4(被忽视的最高水位)** | 算法在授权资金池内自主决策买卖、配置仓位、管理风险,人只设边界——这是存在了 20 年的 E4 |
| **Trading Agent(Crypto AI)** | E1–E3(小规模) | 链上 AI 交易代理管理的真实 AUM 仍小,多数是人类策略的执行皮套 |
| **客服/销售 Agent** | E2 | 按结果收费(per resolution)= 机器劳动被直接定价,但机器不管理任何支出 |
| **Robotaxi** | **E2** | 自主完成服务、直接产生收入;充电/维护/保险全部由公司集中支付,无自主支出 |
| **Autonomous Truck / Drone** | E2(更早期) | 同上,按里程/按配送收费,支出侧零自主 |
| **仓储/工业机器人** | E0–E1 | RaaS 模式下机器"计件挣钱"只是计价方式,决策自主性接近零 |
| **Humanoid** | E0 | 试点交付阶段,无经济行为 |
| **GPU / 算力节点** | E0(商品,非主体) | 被动出租;DePIN 网络中的节点接单是规则执行,非决策 |
| **IoT / EV / 充电** | E1(极窄) | 即插即充是"预授权自动支付",决策空间趋近于零 |
| **电力自动交易系统(如 Autobidder)** | **E4(局部)** | 在批发电力市场自主竞价、套利、配置电池充放——另一个被忽视的成熟 E4 |
| **实验性自主经营体(Project Vend 类)** | E3(实验) | Anthropic Claudius 管理真实小店的收入与进货,二期在监督 Agent 加持下基本消除亏损周(详见 9.4) |

**核心结论**:2026 年机器经济的真实前沿不在 E5 叙事,而在两个具体迁移上:**(a)E0→E1:机器开始在预算内自主花钱(agentic 采购/API 消费);(b)E2→E3:按结果计费的机器劳动开始与其消耗的成本在同一张表上核算。** 同时要认识到:金融交易和电力交易领域早已存在 E4 级机器,证明"高度经济自主"在**规则清晰、结果可即时度量、风险可硬性封顶**的领域最先成立——这是判断其他场景何时突破的最重要先验。

---

# 第二部分:经济结构

## 4. 机器经济的最终需求来自哪里

所有经济活动最终必须存在 Final Demand / Source of Funds。机器可以是生产者、中间商、执行者,但**机器不产生最终需求**——机器没有效用函数,它的"需求"全部是派生需求(derived demand),最终锚定在某个人类主体的支付意愿上。截至 2026 年,机器经济的资金来源结构如下(按真实规模排序):

### 4.1 资金来源分层

**① Enterprise(最大来源,【事实/已规模化】)**。企业为数字劳动付费(Coding Agent、客服 Agent、研究 Agent 的订阅与按结果付费)、为模型 API 付费、为 AI 基础设施付费。模型厂商 2026 年合计数百亿美元量级的收入 run-rate,其中大部分来自企业(详见第 9 节)。这是机器经济目前压倒性的第一资金源。

**② Capital Owner / Trader(第二大来源,【事实/已规模化】但性质特殊)**。交易机器的"收入"来自市场对手盘的亏损或流动性服务费。算法交易占美股成交量过半、占外汇与加密市场更高比例。注意:交易 PnL 是**零和转移**,不是新增最终需求,但它真实地给机器运营者带来收入,并支撑了庞大的机器基础设施(行情数据、低延迟网络、算力)。

**③ Consumer(第三来源,增长最快,【商业化中】)**。消费者为 Robotaxi 付打车费(Waymo/萝卜快跑)、为 AI 订阅付费(ChatGPT/Claude 消费者订阅)、通过 Agent 购物(agentic commerce)。消费端 agentic commerce 2025 假日季开始可测量,但渗透率仍低。

**④ Advertiser / Merchant(潜在的结构性来源,【早期】)**。商家为 Agent 带来的成交支付获客佣金(OpenAI Instant Checkout 抽佣、Perplexity 购物分成)。如果 Agent 成为新的流量入口,广告/佣金预算(全球数千亿美元)会向 Agent 渠道迁移——这是 agentic commerce 的真正商业模式,但 2026 年仍在早期(OpenAI 第一代 Instant Checkout 已于 2026 年 3 月转向,详见 9.6)。

**⑤ Government(极小,【早期】)**。无人机配送医疗物资(Zipline 与政府卫生系统)、自动驾驶的政府补贴与采购、国防自主系统(规模大但属于封闭采购体系,不进入开放机器经济)。

**⑥ Investor(风险资本,特殊类别)**。VC 与代币投资者的资金大量补贴了当前机器经济基础设施(x402 生态、Agent 平台的激励活动)。**必须警惕:由投资者补贴驱动的机器交易量不是最终需求**,它是获客成本,会随融资周期消失。

### 4.2 资金流的典型结构

```text
Enterprise 支付 Agent 服务商 $100(External Revenue,真实新增)
  ↓
Agent 服务商内部:
  支付模型 API $20(机器经济内部转移)
  支付搜索/数据 $5
  支付算力/沙箱 $10
  毛利留存 $65
```

表面上产生了 $35 的"Machine-to-Machine 交易",但整个系统的新增需求只有企业支付的 $100。**机器经济的真实规模 = External Revenue,而不是内部各层交易额的加总。**

---

## 5. External Revenue 与 Internal Machine GMV:统计幻觉的防火墙

这是机器经济研究中最容易出现统计幻觉的地方,必须建立三层核算:

> **External Revenue(外部真实收入)→ Internal Machine Spend(机器间内部交易)→ Net Value Added(净增加值)**

### 5.1 定义与核算规则

- **External Revenue**:机器经济系统从人、企业、政府、外部资本获得的真实收入。判定标准:付款方在系统外,且付款换取了真实效用。
- **Internal Machine Spend**:机器之间的 API/模型/算力/数据/服务支付。它是**中间投入**,类比制造业供应链的中间品交易——供应链每多一层,GMV 翻一倍,但 GDP 只算最终产出。
- **Net Value Added** = External Revenue − 系统从外部购买的投入(电力、人类劳动、硬件折旧)。

### 5.2 为什么这在 2026 年尤其重要

三个现实的统计陷阱:

1. **调用深度膨胀 GMV**。一个 Agent 任务链(Agent A→Agent B→模型→GPU)每加一层,Internal GMV 增加一次,而 External Revenue 不变。x402 类协议让每层调用都变成链上可见的"交易",天然放大总量印象。
2. **激励与投机交易冒充机器需求**。x402 的原始数据中,经 Visa/Artemis 口径调整后,约 89% 的美元交易量和 39% 的交易笔数被识别为 wash trading 与测试活动(原始 $135.7M/1.783 亿笔 → 调整后 $15.0M/1.096 亿笔,2026 年 8 月,来源:Visa/Artemis 调整数据)。PING 等 pay-to-mint 投机代币曾单月贡献约 15 万笔交易、让周度 x402 流量暴增逾 10,000%(来源:Chainalysis,2026 年)。
3. **循环支付(Circular Payments)**。同一主体控制的买卖双方互相支付以刷指标,在有代币激励的生态中系统性存在。

### 5.3 本报告的执行标准

全文凡引用交易量数据,标注三个口径:**原始口径(Raw)/ 调整口径(Adjusted/Organic)/ 外部收入口径(External)**。凡无法区分口径的数据,默认视为原始口径并明确提示不可比。

---

## 6. Machine Revenue Map:机器如何赚钱

九大收入类别,按 2026 年 8 月真实规模排序。

### 6.1 出售数字劳动(当前最大的机器 External Revenue,【事实/已规模化】)

机器完成 Coding、Research、客服、翻译、设计、营销、法务辅助、安全分析等任务并收费。2026 年的关键结构变化是**计价单位的迁移**:

- **按席位订阅(SaaS 逻辑)**:Copilot、Cursor 等,机器仍被当作工具计价;
- **按用量(Token/任务量)**:API 计费、Claude Code 等 usage-based 模式;
- **按结果(Outcome-based,机器劳动被直接定价的标志)**:客服 Agent 按"每解决一单"收费(如 Intercom Fin 每 resolution $0.99、Sierra 按 outcome 定价、Salesforce Agentforce 按对话计费)。**按结果计费的渗透率是"数字劳动市场"是否成立的最重要单一信号。**

已存在"Agent 按任务直接收费"的真实形态,但收费主体仍是运营 Agent 的公司,而非 Agent 本身(E2 特征)。

### 6.2 出售智能 / Inference(第二大类,【事实/已规模化】)

模型即商品:推理、推理链、视觉、语音、垂直模型。模型 API 收入是机器经济中"纯度最高"的机器收入——买方大量本身就是 Agent(机器买智能)。这一层由 OpenAI/Anthropic/Google 高度集中,同时出现了聚合层(OpenRouter)与链上转售层(x402 上最大的服务品类即 AI inference 转售)。

### 6.3 出售数据(【商业化中】)

行情数据(最成熟,Bloomberg/Refinitiv 模式已存在数十年)、链上数据、社交数据、天气/地图/卫星、传感器数据。机器经济带来的增量是两个新问题:(a)**Agent 成为数据的主要买家**后,数据将按调用/按 token 计价(x402 上数据 API 是第二大品类);(b)**机器采集的数据能否形成卖方市场**——DePIN(Hivemapper 地图、DIMO 车辆数据、WeatherXM 气象)是首批实验,真实收入仍极小(详见第 9、13 节)。爬虫经济的重构是 2025–26 的真实拐点:Cloudflare pay-per-crawl 让"AI 读网页"第一次成为可计价交易(【早期】)。

### 6.4 出售算力(【事实/已规模化】,但主体是公司而非机器)

云 GPU/CPU/存储/带宽/沙箱。算力是机器经济最大宗的中间品。"设备自主判断闲置资源并自动出售"在 DePIN 网络(Akash、io.net)中有真实但小规模的实现——节点按规则自动接单属于 E0–E1 的规则执行,尚谈不上自主定价。

### 6.5 出售物理资源(【早期】)

电力(V2G 车辆向电网售电、储能套利)、充电位、停车位、制造产能、仓储容量、运力。**电力是最接近成立的场景**:电池储能的自动交易(Tesla Autobidder 类系统在批发市场自主竞价)已经是真实的、规模化的"机器卖电赚钱"(详见 9.8)。

### 6.6 金融活动(最古老、最大的"机器赚钱",【事实/已规模化】)

做市、套利、流动性提供、借贷、预测市场、财库管理。必须严格区分:**Trading PnL 是零和转移,不计入机器经济的 External Revenue**;但做市与流动性服务收取的价差/费用,本质是向交易者出售"即时性服务",可视为真实服务收入。传统量化基金是机器经济中最成熟的 E4 主体;Crypto AI 交易代理(2024–25 年的 AIXBT 等)绝大多数被证明是叙事皮套,管理的真实 AUM 极小。

### 6.7 商业代理佣金(【早期】,潜在空间最大的品类之一)

Agent 帮用户购物、订旅行、采购 SaaS/保险/金融产品,向商家收取 affiliate/referral/commission。**关键判断:Agent Commerce 的终局更可能是商家支付获客费(类广告模式),而非用户付费**——因为用户侧支付意愿被订阅费封顶,而商家侧的获客预算(全球广告+联盟营销数千亿美元)是现成的、可迁移的。2026 年的现实:OpenAI Instant Checkout 抽佣模式(4% 佣金)首代仅约 12–30 家 Shopify 商家实际上线、ChatGPT 内结账转化率仅为零售商自有网站的约 1/3(沃尔玛口径差 3 倍),2026 年 3 月被迫撤回并转型为"发现渠道"(来源:The Information/CNBC/Forbes,2026 年 3 月);Amazon 诉 Perplexity 案的反转极具标志性——2026 年 3 月 10 日地区法院授予 Amazon 初步禁令,但 **2026 年 8 月 4 日第九巡回上诉法院撤销禁令,裁定 AI 助手是"工具而非人"、访问者是用户本人**(Amazon 已于 8 月 18 日申请全院复审)。这场"Agent 是否有权代表用户访问平台"的法律战,是决定该品类命运的最大变量,且第一回合的司法风向对 Agent 有利。

### 6.8 Agent-to-Agent 服务(【实验】→【早期】)

Agent A 购买 Agent B 的研究/编码/验证/执行能力。Virtuals ACP、Olas Mech marketplace、x402 上的 agent 服务是首批实验。**Agent Labor Market 是否形成的判据不是交易笔数,而是:是否存在一个 Agent 稳定地把从外部客户赚到的钱,花在采购其他 Agent 的服务上(即 A2A External Revenue 传导链)。** 截至 2026 年 8 月,该判据尚无规模化证据(详见第 15 节)。

### 6.9 物理任务收入(【商业化中】,增长最陡)

Robotaxi(Waymo、萝卜快跑、小马智行)、无人配送(Zipline、美团无人机)、无人卡车(Aurora)、RaaS 机器人(按小时/任务计费的仓储与人形机器人)。这是"Robot + Revenue"已经成立、"Robot + Wallet + 自主 OPEX"完全未成立的领域。**Autonomous Economic Machine(机器人自负盈亏)在 2026 年不存在任何真实案例**,但物理任务收入本身已进入数十亿美元量级(详见第 9 节数据)。

---

## 7. Machine Expenditure Map:机器为什么花钱

八大支出类别。核心事实:**2026 年机器支出的绝大部分,仍是人类实体替机器付费(E0);机器在预算内自主选择供应商并支付(E1)只在 API/算力采购中初步出现。**

### 7.1 Intelligence(最大支出品类)

Agent 购买 LLM 推理、embeddings、视觉、语音。模型 API 支出是所有 Agent 的第一大成本项。已出现真实的 E1 行为:Agent 框架根据任务难度自动路由不同价位的模型(model routing),即**机器在自主做"买哪种智能"的采购决策**——这是被低估的、已规模化的机器自主采购。

### 7.2 Data(第二大品类)

搜索 API(Agent 时代搜索从人类入口变成机器中间品)、行情、链上数据、地图、专有数据集。x402 上按调用付费的数据服务是该品类的链上映射。

### 7.3 Compute

GPU/沙箱(Coding Agent 的代码执行环境是新生的真实品类)、云、存储、带宽。

### 7.4 Software / APIs

SaaS、MCP 工具、安全、身份验证、分析。MCP 生态(官方 registry 活跃注册 server 约 22,600 个,2026 年 8 月 19 日全量爬取口径;SDK 月安装量 9,700 万+;但质量高度长尾——仅 53.4% 声明可达远程端点,top 0.1% 的包占 84% 月安装量,来源:独立审计 repo/mcphq.ai/Agent Almanac)让"Agent 调用工具"标准化,但 MCP 本身不含支付——工具货币化需叠加支付层,这正是 x402/ACP/MPP 争夺的位置。

### 7.5 Financial Execution

Gas、swap 费、交易费、跨链费、清算费。交易类 Agent 的主要成本。

### 7.6 Physical Goods(【实验】)

Agent 自主购买食品、零部件、酒店、机票。Project Vend 中 Claudius 真实地进货(自主选品、找供应商、下单);Denso 的 AI 采购代理自 2024 年 8 月起通过 Skyfire 持续进行自主采购(来源:LI.FI/Skyfire,2026)。属于真实但极小规模的实验。

### 7.7 Physical Machine OPEX(【推演】为主,局部【早期】)

机器支付自己的电费、充电、维护、保险、通行费。现状:Robotaxi/机器人车队的 OPEX 全部由公司集中账户支付。**机器何时开始承担自己的 OPEX?**判断:当且仅当(a)机器以独立核算单元运营(RaaS 按台核算利润),且(b)供给侧出现机器可直接调用的自动化服务市场(自动充电桩、自动维保调度)。最早的真实形态可能不是"机器人自己付电费",而是**车队管理系统按车辆颗粒度自动核算与结算 OPEX**——即 E3 先在会计层实现,再下沉到支付层。

### 7.8 Paying Other Machines(A2A 供应链)

```text
Trading Agent → 买行情数据 → 买研究 Agent → 调用 Claude → 租 GPU → 调用执行 Agent → 支付交易费 → 获得 PnL
```

**Agent-to-Agent 供应链正在形成,但形成的位置在企业内部与平台内部**(multi-agent 编排框架内的调用),而不是开放市场——内部调用不产生市场交易,因此链上 A2A 数据远小于真实的 A2A 调用量。这是解读一切 A2A 支付数据时必须记住的结构性偏差。

---

## 8. 完整 Machine Economy P&L

```text
                     FINAL DEMAND
     Enterprise │ Consumer │ Trader对手盘 │ Merchant │ Gov
                          ↓
                   MACHINE REVENUE
   数字劳动 │ 智能/推理 │ 数据 │ 算力 │ 物理任务 │ 佣金 │ 金融服务费
                          ↓
              MACHINE WALLET / ACCOUNT
        (2026 年现实:99% 是公司账户,不是机器账户)
                          ↓
   ────────────────────────────────────────────
                    MACHINE OPEX
    ├─ Intelligence(模型 API)      ← 最大成本项
    ├─ Compute(GPU/沙箱/云)
    ├─ Data(搜索/行情/专有数据)
    ├─ Software/API/工具
    ├─ 其他 Agent 服务               ← 尚在实验
    ├─ Financial Execution(gas/手续费)
    ├─ Energy(电力/充电)            ← 物理机器
    └─ Physical(维护/保险/零件)      ← 全部人类代管
   ────────────────────────────────────────────
                          ↓
              MACHINE OPERATING PROFIT
                          ↓
               CAPITAL ALLOCATION
      (再投资/扩大算力/雇佣更多 Agent —— E4/E5,基本不存在)
```

**截至 2026 年 8 月,哪些机器已形成部分 P&L?**

| 主体 | P&L 完整度 | 说明 |
| --- | --- | --- |
| 量化交易系统 | **收入侧+配置侧完整(E4)** | 自主产生 PnL、自主配置仓位;但基础设施成本由公司管理 |
| 电池储能自动交易(Autobidder 类) | 收入侧完整 | 自主套利赚取价差,资产与成本归公司 |
| 客服/Coding Agent | 成本侧清晰、收入侧按结果计价开始 | 每 resolution 收入 vs 每 resolution 的 token 成本,单位经济学已可核算——**这是最接近真实机器 P&L 的地方** |
| Project Vend 类实验 | 完整但微型(E3 实验) | 真实收入、真实进货成本、真实利润表;二期已基本消除亏损周 |
| Robotaxi | 收入清晰、成本人类代管 | 单位经济学(每英里收入 vs 成本)在公司层面核算,机器无参与 |
| x402 上的 Agent | 支出侧真实、收入侧存疑 | 大量 Agent 只花钱(人类充值)不赚钱;"earning agents"占比是关键缺失数据 |

**结论:机器 P&L 的真实前沿是"单位经济学核算"(unit economics per agent/per robot),而不是"机器拥有钱包"。投资研究应跟踪的是:哪些公司开始按单个 Agent/单台机器公布或核算利润。**

---

# 第三部分:现实与未来

## 9. 截至 2026 年 8 月真实存在的 Machine Economy(Current Reality Map)

本节只列真实活动,每个案例给出:经济主体、收入、支出、Final Payer、自主程度(E 级)、当前规模、证据。

### 9.1 软件 Agent(机器经济最大的 External Revenue 所在)

| 场景 | Economic Agent | 收入 | 支出 | Final Payer | 自主程度 | 当前规模 | 证据(数据+时间+来源) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Coding Agent | Claude Code / Codex / Cursor / Copilot / Devin | 订阅+用量+ACU 按任务 | 模型 API、沙箱算力 | 企业(为主)+个人开发者 | E1–E2 | 生态年化收入保守 $150–250 亿 | Anthropic 全司 run-rate $650 亿+(2026-07,Bloomberg/Reuters,毛收入口径);Claude Code 单产品 $25 亿+ run-rate(2026-02,公司披露);Cursor ARR $20–26 亿(2026-02/06,CNBC/Reuters),2026-08-14 被 SpaceX 以约 $600 亿全股票收购;Copilot 5,000 万用户、转 usage 计费后收入单季环比 +60%(2026-08,微软 FY26Q4 电话会);Cognition ARR $4.9 亿(2026-05,Sacra) |
| 客服 Agent(按结果计费) | Agentforce / Sierra / Fin / Decagon | **per resolution 收费($0.99–2.5/次)** | 模型 API | 企业客服预算 | **E2(机器劳动直接定价)** | 品类 ARR 合计约 $15 亿+ | Agentforce ARR $12 亿、+205% YoY(2026-05,Salesforce FY27Q1 财报);Sierra ARR $2 亿(2026-05/08,Sacra/Newcomer)、估值 $158 亿;Fin 接近 $1 亿 ARR、解决率 65–70%(2026-08,Intercom);AI 解决成本 $1.25–3/次 vs 人工 $12–25/次 |
| 法律/医疗/金融垂直 Agent | Harvey / Abridge 等 | 订阅+平台费 | 模型 API | 企业专业服务预算 | E1–E2 | Harvey 年化收入 $3.5 亿+(2026-07/08,Sacra/The Information)、洽谈 $155 亿估值;Abridge ARR $1 亿+(2025-05,Sacra) | 同左 |
| 交易 Agent(传统) | 量化/HFT/做市系统 | Trading PnL+做市价差 | 行情数据、算力、交易费 | 市场对手盘 | **E4** | 算法交易约占美股成交量 70%(2026-03,行业汇总) | 存在 20 年的最成熟机器经济,规模远超一切 LLM Agent |
| 预测市场 Agent | Polymarket/Kalshi 上的自主交易 bot | Trading PnL | 数据、gas、模型 | 市场对手盘 | E3–E4(小规模) | Polymarket 30%+ 钱包由 AI agent 运行,前 20 名最盈利账户中 14 个是 agent(2026,TurbineFi);两平台月交易量合计约 $240 亿(2026-04) | 全行业 agent 渗透率最高的真实用例 |
| 采购/财务 Agent | Coupa Navi / Ramp Agents / SAP Joule | 软件订阅 | 模型 API | 企业采购/财务预算 | **E1(真实自主支付!)** | Coupa Navi 450+ 客户生产环境;其 Payment Batch Agent 5 周自主执行 14 个付款批次、2,395 笔、共 **$2,010 万**,AI 成本仅 $27(2026,Coupa/Business Wire);Ramp Agent Cards 为每个外部 agent 发放带限额虚拟卡 | 企业侧"机器自主付款"的最硬证据 |
| 购物 Agent | Rufus/Alexa+、ChatGPT 购物、Perplexity | 平台 GMV 拉动+佣金(试验) | 模型推理 | 消费者/商家 | E1 | Rufus 2025 年服务 3 亿+ 用户、归因约 $120 亿增量年化销售(亚马逊 2025Q4 财报);Salesforce 口径:AI 与 agent 影响 2025 假日季全球线上零售的 20%(约 $2,620 亿,influenced 口径);Adobe:GenAI 来源流量 +693% YoY(2026-01) | "影响"已规模化,"全自动成交"仍低个位数 % |
| 自主经营实验 | Anthropic Project Vend(Claudius) | 真实小店销售收入 | 真实进货、定价 | 办公室消费者 | **E3(实验)** | 一期亏损;二期(Sonnet 4/4.5+上级"CEO" agent+流程工具)折扣减少约 80%,自 2025 年 10 月起持续周度盈利,扩至旧金山/纽约/伦敦(2026-06,Anthropic 官方) | 机器自主 P&L 的最重要实证:**无约束会亏钱,加治理结构后可盈利** |

### 9.2 数字基础设施机器(被交易的机器资源)

| 场景 | Economic Agent | 收入 | Final Payer | 自主程度 | 当前规模 | 证据 |
| --- | --- | --- | --- | --- | --- | --- |
| 模型 API(智能出售) | OpenAI/Anthropic/Google 模型 | API 用量收费 | 企业 | 商品(非主体) | 年化超 $1,000 亿 | Anthropic $650 亿 + OpenAI $400 亿 run-rate(2026-07/08,Bloomberg;注意 Anthropic 为毛收入口径需折 20–30%) |
| Token 路由/聚合 | OpenRouter | 抽成 | 开发者/Agent | 商品 | 周处理 25 万亿 tokens(2026-05,公司披露);估值 $13 亿 | 机器经济的"电表";Google 全平台月处理 3,200 万亿 tokens(2026-05,I/O) |
| 去中心化算力 | Aethir / io.net / Akash | 出租 GPU | AI 企业(法币客户为主) | E0–E1 | Aethir ARR 约 $1.5 亿(2026,HTX/Odaily);io.net 累计链上收入 $2,000 万+;Akash ARR 约 $420 万 | DePIN 中真实收入最大板块 |
| 数据 DePIN | Grass / GEODNET / DIMO / Helium | 卖数据/网络服务 | 企业(含 Fortune 100,USDC 付款) | E0–E1 | Grass 2026H1 收入约 $1,700 万(约 20 家企业客户);GEODNET ARR 约 $830 万(客户是机器人/无人机/精准农业——**最纯正的机器客户**);Helium Mobile 单月收入 $250 万(2026-03) | 机器采集数据→卖给企业,已有千万美元级真实法币收入 |
| 链上机器支付轨道 | x402 生态 | facilitator 费+服务收入 | 混合(大量投机/测试) | — | 累计 1.69 亿笔/$4,140 万结算(2026-08-26,agenteconomy.to);**organic 日交易额仅约 $2.8–4 万**(2026-03/05,Artemis/CoinDesk) | 详见第 15 节 |

### 9.3 物理机器(收入已规模化、支出零自主)

| 场景 | Economic Agent | 收入 | 支出(谁付) | Final Payer | 自主程度 | 当前规模 | 证据 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Robotaxi(美国) | Waymo 车队 | 按单打车费 | 充电/维保全部公司 B2B 合同集中支付(Element/Terawatt/Transdev) | 消费者 | E2 | 每周约 50 万付费单(2026-03 至 08 出现平台期)、15 个都会区、约 4,000 辆;年化收入约 $3.55 亿;Other Bets 2026Q2 收入 $3.82 亿/经营亏损 $18 亿 | Waymo/Alphabet Q2 财报;2026-02 融资 $160 亿、估值 $1,260 亿;单车利用率降至约 125 单/周 |
| Robotaxi(中国) | 萝卜快跑 / 小马 / 文远 | 按单打车费 | 公司集中支付 | 消费者 | E2 | 萝卜快跑累计超 2,200 万单、27 城、迪拜/阿布扎比落地(2026-04/05,百度财报);小马 Q2 Robotaxi 收入 $1,210 万、+691% YoY、车队 1,975 辆;文远 Robotaxi 超 1,800 辆、Q2 收入 $3,420 万 | 武汉已单城打平(百度口径);全行业仍深度亏损 |
| Robotaxi(其他) | Tesla / Zoox | 按单收费 | 公司(Tesla 用自家超充内部核算) | 消费者 | E2 | Tesla 累计付费里程近 250 万英里、6 个全商业化城市(2026Q2 股东信);Zoox 2026-08-10 拉斯维加斯开始收费 | 透明度远低于 Waymo |
| 无人卡车 | Aurora / Kodiak | 按载货英里收费(TaaS) | 公司 | 货主企业 | E2 | Aurora 2026H1 收入仅 $300 万、累计无人里程 44 万英里、年底目标 200 辆(对应约 $8,000 万收入 run-rate);Kodiak 35 辆客户自有无人卡车 | 全赛道年收入 <$5,000 万,收入/累计融资比 <1% |
| 无人机配送 | Zipline / 美团 / 丰翼 / Wing / Prime Air | 按配送收费 | 公司 | 商家/消费者/医疗系统 | E2 | Zipline 累计 250 万+ 次配送(2026-07,官方)、估值 $76 亿;美团累计 100 万+ 单、单均成本约 2.3 元(vs 人工 6–8 元)(2026-07,上海低空经济博览会);丰翼累计 154 万架次、**宝安–东莞航线已盈亏平衡** | 中国低空经济 2026 年市场规模预计破 1.06 万亿元(赛迪) |
| 仓储机器人 | Amazon 机器人 / Locus(RaaS) | Amazon 内部降本;Locus 按台月租 $1,990 | 公司 | 企业物流预算 | E0–E1 | Amazon 100 万+ 台机器人、DeepFleet 提升车队效率约 10%(2025-08,Amazon Science);Locus ARR 约 $1.8 亿、17,000+ 台、累计拣选 70 亿次(2026-06,Sacra) | RaaS = 机器按月"领工资",但决策自主性≈0 |
| 人形机器人 | Unitree / 智元 / Figure | 卖本体+租赁+数据 | 公司 | 科研/制造企业 | E0 | 宇树 2026-08-19 科创板上市、2025 年净利 2.88 亿元(**全球罕见已盈利**);智元累计下线 15,000 台(2026-06);Figure 03 在 BMW Spartanburg;2026H1 全球人形机器人出货仅约 1 万余台 | 产业化初期,无经济自主行为 |
| 自动充电/自动计费 | Tesla 超充网络 / Plug&Charge | 自动扣款 | 车主账户自动扣 | 车主 | E1(预授权自动支付) | Tesla 超充 2026Q2:8,704 站、82,357 桩、单季 6,000 万次充电会话全自动认证扣款、配电 2.0 TWh(Tesla Q2 财报);ISO 15118 Plug&Charge 成为新车标配趋势(CEC,2025) | **现实中最大规模的"机器自动支付"** |
| 电力自动交易 | Tesla Autobidder / VPP | 批发市场套利收入 | 资产方 | 电网/电力市场 | **E4(局部)** | Autobidder 运营 65+ 国;Tesla VPP 五大市场合计 2.38 GW 可调度容量、2025 年调度 89,000+ 次(2026-08,pv magazine);V2G 用户年收益 $800–1,500(PG&E 试点) | **机器自主赚钱最成熟、金额最大的领域之一** |
| 机器钱包实验 | peaq / Bosch / Nevermined | 代币激励为主 | 投资者补贴 | — | 实验 | peaq 宣称 335 万+ 机器 ID(官方口径);阿联酋 Machine Economy Free Zone(2025-06);与真实法币现金流脱钩 | 【实验】不构成投资证据 |

### 9.4 Current Reality 的三个结构性结论

1. **机器经济的真实收入呈"哑铃形"**:一端是软件 Agent 的数字劳动(百亿美元级、增速 3–7 倍/年),一端是存在已久但不被叫"机器经济"的机器交易(算法交易、电力自动交易、自动计费网络);中间被热炒的"链上 Agent 经济"organic 规模仅数万美元/日。
2. **收入自主性远远领先支出自主性**。E2(机器赚钱)已规模化,E1(机器花钱)刚在企业采购与 API 消费中萌芽,E3(机器 P&L)只存在于实验(Project Vend)与会计核算颗粒度(RaaS 按台、Robotaxi 按车)中。
3. **没有任何一台物理机器拥有自己的钱包**。所有物理机器的收支都由公司账户完成;最接近"机器付钱"的形态是预授权自动支付(Plug&Charge、超充)——这提示:机器经济的支付演进路径是"授权的自动化",不是"机器的独立"。

---

## 10. 未来 Machine Economy 场景全景(21 个场景)

每个场景给出:机器做什么/谁最终付钱/为什么付/收入与 OPEX/是否需要钱包-稳定币-区块链/成熟度/三大瓶颈(商业/技术/监管),以及"预测成立条件"框架(当前规模/TAM 锚点/5 年与 10 年商业可见性/成立条件/最大不确定性)。**原则:预测成立条件,不预测伪精确数字。**

### 10.1 Digital Labor 群组(Coding / Research / Sales / Marketing / 客服 / Cybersecurity / Scientific)

- **机器做什么**:完成可交付的知识工作;**谁付钱**:企业(压倒性)——因为对标的是 $30–150/小时的人类劳动成本,替代经济性 10–20 倍。
- **收入**:订阅→用量→按结果(客服已过半,coding 因 outcome 难定义仍 hybrid);**OPEX**:模型推理(第一)、沙箱算力、数据/搜索。
- **钱包/稳定币/区块链**:**都不需要**。企业采购走合同+发票+银行轨道;Agent 消耗的是内部授信额度。
- **成熟度**:Coding/客服【事实/已规模化】;Sales SDR【早期且有信任危机】(11x ARR 掺水事件);Cybersecurity(自动漏洞挖掘/响应)【早期】;Scientific(文献研究、实验设计)【早期→实验】。
- **瓶颈**:商业=组织落地能力(MIT NANDA:95% 试点无可测 P&L 回报);技术=长任务可靠性与验收;监管=职业责任(法律/医疗)。

| 维度 | 判断 |
| --- | --- |
| 当前真实规模 | 生态年化收入 $150–250 亿(coding)+客服 $15 亿+,增速 200–600% |
| TAM 锚点 | 全球知识工作薪酬(数万亿美元)的可自动化部分;Sequoia"服务即软件":每 $1 软件对应 $6 服务 |
| 5 年商业可见性 | **高** |
| 10 年商业可见性 | **高** |
| 核心成立条件 | 按结果计费渗透率持续上升;单任务人工干预率持续下降 |
| 最大不确定性 | 模型能力进入平台期;头部集中导致应用层利润被模型层吸走 |

### 10.2 Procurement / 企业自主采购

- 机器在预算与策略内完成寻源、比价、下单、付款。**已有最硬证据**:Coupa Navi 付款 Agent 5 周自主付款 $2,010 万(AI 成本 $27);采购 AI 自主度指数评估全行业为 L1.2–2.4(常规流程无人化、审批留人)。
- 谁付钱:企业(采购本来就要花的钱,Agent 只是执行层);**不需要新钱包/稳定币**——走既有企业银行轨道与虚拟卡(Ramp Agent Cards 模式:每个 agent 一张带限额的 tokenized 虚拟卡,是最现实的"agent 钱包")。
- 成熟度【商业化中】。瓶颈:商业=信任与审计;技术=错误成本高;监管=授权范围的法律界定(UETA 承认电子代理缔约,但无生成式 AI 判例)。
- 5 年可见性**高**;10 年**高**。成立条件:agent 采购错误率低于人工;审批阈值持续上调。最大不确定性:一次高额错误采购事故引发行业收紧。

### 10.3 Shopping / Agentic Commerce(消费端)

- 现实:发现层已规模化(AI 影响 2025 假日季 20% 线上零售、$2,620 亿 influenced 口径,Salesforce),**成交层第一代已失败**(Instant Checkout 撤回;转向"AI 发现+商家自有结账")。
- 终局商业模式更可能是**商家付获客佣金**(广告预算迁移),而非用户付费。Amazon v. Perplexity 上诉判决("工具而非人")为第三方 Agent 打开法律空间。
- 需要钱包吗?消费端**不需要新钱包**——卡组织正在把 agent 装进现有卡体系(Visa Intelligent Commerce/Passkey、Mastercard Agentic Tokens);需要的是**授权凭证(mandate)**而非货币创新。
- 5 年可见性**高**(以"AI 影响的 GMV"计)/ 成交自动化渗透**中**;10 年**高**。成立条件:平台开放访问权(法律战结果)+转化率超过人类自购。最大不确定性:流量既得利益者(Amazon/Google)以封锁或自营 agent 垄断入口。

### 10.4 Trading / Asset Management / Prediction Markets

- 机器交易早已是市场主体(美股 70% 成交量);新边界是(a)零售把执行权交给 agent(Robinhood Agentic Trading 2026-05 beta、Coinbase for Agents:隔离账户+限额),(b)预测市场 agent(Polymarket 30%+ 钱包);(c)DeFi AgentFi 被证伪(全部可验证 TVL 仅约 $2,000–3,200 万,DefiLlama 2026-08)。
- 谁付钱:对手盘(零和)+资管费。区块链**仅在链上市场必要**;传统交易用传统轨道。
- 5 年可见性:零售 agent 执行**中→高**;agent 管理真实 AUM **中**;10 年**高**。成立条件:agent 交易账户的合规框架(SEC/CFTC 尚无专门规则)+可验证业绩记录标准。最大不确定性:一次 agent 引发的闪崩事故触发严监管;AI 基金爆仓(Situational Awareness 基金 2026-07 亏 67%)已展示尾部风险。

### 10.5 Data Economy(数据买卖 + 爬虫经济重构)

- 两条线:(a)Agent 成为数据最大买家(搜索/行情/专有数据按调用计价);(b)内容方向 AI 收费——Cloudflare 数据:自动化请求已占 HTML 流量 57.5%(2026-06,Radar),ClaudeBot 抓取/引荐比可达 11,000:1;Monetization Gateway(2026-07-01 waitlist)把任何网页/API/MCP 调用变成 x402 计费资源。
- 谁付钱:AI 公司(为训练与推理时检索付费)——**这是真实的、新增的 External Revenue 品类**。
- 该场景是**微支付+机器身份的最佳适配场景**:请求量巨大、单价极低(分厘级)、无退款需求、双方都是机器——传统卡轨道在经济上无法承接(约 76% 的 agent 交易金额低于 Visa $0.30 固定费下限)。
- 5 年可见性**高**;10 年**高**。成立条件:2–3 家头部 AI 公司真金白银按量付费(而非一次性 licensing);Cloudflare 类咽喉层的计费默认开启。最大不确定性:大 AI 公司绕过(直接签双边大合同),微支付市场被 licensing 替代。

### 10.6 Compute Economy(算力市场)

- 机器买算力已是最大中间品交易;新增量是(a)agent 工作负载成为去中心化算力的需求来源,(b)"AI 公司向 AI 公司卖算力"的循环(Anthropic 签下 xAI Memphis 300+MW 算力,2026,Bloomberg)。
- DePIN 算力真实但小(Aethir $1.5 亿 ARR 为板块之王);瓶颈是 SLA。**不需要区块链的部分占绝对主导**(超大规模云)。
- 5 年可见性**高**(整体)/DePIN 份额**中**;10 年**高**。成立条件(DePIN):agent 负载对 SLA 不敏感的部分持续增长。最大不确定性:capex 泡沫破裂导致算力过剩、价格崩塌(四大厂 2026 capex 约 $7,400–8,000 亿 ≈ 经营现金流的 99%,Epoch AI/FactSet)。

### 10.7 Energy Economy(能源机器经济)

- 已成立:储能自动交易(Autobidder,E4)、VPP(2.38 GW)、自动充电计费(超充 6,000 万次/季)。将成立:V2G 规模化(万台级→百万台级)、EV 作为分布式电池的自动套利。
- 谁付钱:电网/电力市场(真实、巨大、常年存在的 Final Demand)。**完全不需要区块链**——电力市场有成熟的结算体系;需要的是资产级自动交易软件与聚合商。
- 5 年可见性**高**;10 年**高**。成立条件:电价波动加大(可再生能源占比上升)+双向充电硬件渗透。最大不确定性:电力市场规则对聚合商的准入限制。

### 10.8 Robot Economy(RaaS / 人形 / 服务机器人)

- 现状:RaaS 让机器"按月领工资"(Locus $1,990/台/月;Agility 按订阅;Carbon Robotics $15–25/小时)。机器人自主采购维护/配件【纯愿景】。
- 5 年可见性:RaaS 扩张**高**,人形规模化**中**;10 年:人形+自主 OPEX **中**。成立条件:单台机器人的独立核算成为行业惯例→维保/充电服务市场 API 化→车队系统自动采购。最大不确定性:人形机器人可靠性与成本曲线。

### 10.9 Autonomous Vehicles / Logistics(Robotaxi / 无人卡车 / 无人配送)

- 收入侧【商业化中→规模化】,见 9.3。关键分歧:Waymo 订单出现平台期(50 万单/周维持四个季度)vs 中国玩家收入 +691%(小马)——**单位经济学与扩张速度的赛跑**。
- 5 年可见性**高**(收入)/自主 OPEX **低**;10 年**高**。成立条件(盈利):单车利用率回升+远程协助率下降+保险成本下降。最大不确定性:安全事故与城市准入;Waymo 2027 盈利指引与 Aurora 2028 FCF 指引是两个可证伪的检验点。

### 10.10 Manufacturing / IoT / Machine Resource Markets

- 制造:自主产线是自动化延伸,经济主体仍是工厂(Jensen Huang"全机器人工厂"叙事,属【推演】)。IoT 机器身份+微支付(peaq 类)【实验】。机器资源市场(闲置算力/传感器数据自动出售)【早期】,GEODNET(机器人 RTK 定位服务,ARR $830 万)是最真实样本——**卖给机器的服务**先于**机器卖的服务**成立。
- 5 年可见性**低→中**;10 年**中**。成立条件:机器身份标准(RFC 9421 三路合流已发生)+设备侧自动结算需求真实出现。最大不确定性:IoT 机器经济可能重演 2018 年被证伪的历史。

### 10.11 场景总览矩阵

| 场景 | 当前阶段 | 5 年可见性 | 10 年可见性 | 需要钱包 | 需要稳定币 | 需要区块链 | 传统金融可用 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Coding/数字劳动 | 已规模化 | 高 | 高 | 否 | 否 | 否 | 是 |
| 客服/按结果计费 | 已规模化 | 高 | 高 | 否 | 否 | 否 | 是 |
| 企业自主采购 | 商业化中 | 高 | 高 | 虚拟卡即可 | 否 | 否 | 是(更优) |
| Agentic Shopping | 早期(重构中) | 高 | 高 | 授权凭证 | 否 | 否 | 是(更优) |
| 交易/预测市场 Agent | 已规模化(传统)/早期(链上) | 中高 | 高 | 链上场景需要 | 链上场景是 | 链上场景是 | 传统市场是 |
| 数据/爬虫经济 | 早期 | 高 | 高 | **是** | **是(最适配)** | 是(或类链轨道) | 否(费率不经济) |
| API/机器微支付 | 早期 | 中高 | 高 | 是 | 是 | 是(或 Tempo 类) | 否(费率不经济) |
| 算力市场 | 已规模化(云)/早期(DePIN) | 高 | 高 | DePIN 需要 | DePIN 是 | DePIN 是 | 云是 |
| 能源自动交易 | 已规模化(局部) | 高 | 高 | 否 | 否 | 否 | 是(更优) |
| Robotaxi/物流 | 商业化中 | 高 | 高 | 否 | 否 | 否 | 是 |
| Robot RaaS | 商业化中 | 高 | 中高 | 否 | 否 | 否 | 是 |
| 机器自主 OPEX | 愿景/实验 | 低 | 中 | 是(若成立) | 可选 | 可选 | 部分可用 |
| A2A 开放服务市场 | 实验 | 低→中 | 中 | 是 | 是 | 是 | 否 |
| 人形机器人经济 | 早期(本体销售) | 中 | 中高 | 否 | 否 | 否 | 是 |

---

## 11. 每个场景的最早变化信号(场景级 Signal 体系)

回答统一问题:**"如果该领域正在从实验走向真实经济规模,我最早应该看到什么?"** 按七类信号(Data/Behavioral/Product/Developer/Institutional/Revenue/Regulatory)给出各场景最具判别力的 3–5 个:

**数字劳动(Coding/客服)**
- Revenue:按结果计费收入占比(客服已 >50%,coding 若跨过 20% 即重要拐点);Data:纯 usage 合同占比(现约 9%,Metronome);Behavioral:单任务人工干预率(OpenAI 披露的"委托式任务 token 占比 64%"类指标);Institutional:财报中出现"Agentic Work Units"类经营指标(Salesforce 已开始:单季 38 亿 AWU)。

**企业自主采购**
- Data:agent 自主付款金额与审批阈值(Coupa 类案例的批次金额与频率);Product:虚拟卡产品的 agent 专属发行量(Ramp Agent Cards 放量);Institutional:审计准则/内控框架发布 agent 付款条款;**最早信号:采购审批阈值从"每笔人审"上调到"例外人审"的公司数量**。

**Agentic Shopping**
- Data:agent 完成的 checkout 占电商交易 %(区分 influenced 与 executed 口径);Regulatory:Amazon v. Perplexity 全院复审结果;Product:大平台是否开放官方 agent API(Amazon"预计终将与第三方 agent 合作",Jassy);Behavioral:AI 渠道转化率 vs 官网转化率之比(现约 1/3,反转即拐点)。

**数据/爬虫经济**
- Data:Cloudflare Monetization Gateway 计费请求量与接入域名数;pay-per-crawl 收入;Revenue:头部 AI 公司按量付费给内容方的公开合同;Developer:Apify 类平台的 agent 付费调用量(2 万+ 爬虫 Actor 已接受 agent 支付,2026-07);**最早信号:某家 top AI lab 公布按 token/按次向内容方结算的常设机制**。

**链上机器支付(x402/MPP)**
- Data:organic 日交易额(现 $2.8–4 万)与 **AI agent 买家占比(现仅 1.3%,x402watch)**;Quality:$1+ 交易占 volume 比(49%→95%,Chainalysis,继续观察);Institutional:AWS/Ramp 类企业集成后的 90 天留存(Ramp 2026-08-20 接入是首个企业级实验);**最早信号:AI agent 买家数从 381 → 数千且付费留存 >30 天**。

**交易 Agent**
- Data:agent 隔离账户数(Robinhood/Coinbase)、agent 管理 AUM(可验证口径);Behavioral:人工干预率、自主持仓周期;Regulatory:SEC/CFTC 首个 agent 交易规则或执法案例。

**Robotaxi/物流**
- Data:单车周订单(Waymo 125 单/车/周,回升即拐点)、远程协助率;Revenue:首个公司层面盈利报告(百度武汉单城打平已发生→整体打平是下一个);Institutional:保险费率下降;Catalyst:Waymo 100 万单/周(第三方预测中位数 71 万,2026 底)。

**Robot Economy**
- Data:RaaS 装机量与按台 ARR(Locus 类);Product:维保/充电服务的 API 化产品出现;Revenue:人形机器人从"科研/展演"收入转向"生产任务"收入的占比(宇树收入结构变化是可跟踪样本);**最早信号:某车队/机器人运营商公布"单台机器 P&L"并开放机器自动采购服务**。

**能源机器经济**
- Data:VPP 可调度容量(Tesla 2.38 GW→)、V2G 参与车辆数;Revenue:单车年售电收入($800–1,500 区间是否上移);Product:车企原生 V2G 套餐(Tesla Powershare 首批放电事件 2026 底)。

---

# 第四部分:基础设施与生态

## 12. 机器经济基础设施 Stack(L0–L8)

### L0 — Money(货币层)

| 货币形态 | 2026 年 8 月状态 | 机器经济适配性 |
| --- | --- | --- |
| 稳定币 | 总市值约 $3,030 亿(USDT $1,832 亿/60.4%、USDC $737 亿/25%,2026-08,DefiLlama);调整后月结算量 $1.79 万亿创纪录(2026-06,Visa Onchain Analytics);但**真实支付仅约 $3,900 亿/年、占全球支付 0.02%**(2026-02,McKinsey×Artemis),其中 B2B $2,260 亿、+733% YoY | 微支付/跨境/7×24 最优;无退款争议机制是硬伤 |
| 法币/银行存款 | 企业 agent 支出的绝对主体(合同+发票+虚拟卡) | 企业采购最优 |
| Tokenized Deposits | JPMD 2025-11 在 Base 正式推出(机构邀请制);FDIC 提案给予存款保险(稳定币无);Swift 17 家银行共享账本试点(2026-07) | 银行体系对机器支付的正式回应,**中长期最被低估的轨道** |
| CBDC | BIS Project Agorá 真实价值测试(28 机构、约 80 万瑞郎、结算平均 80 秒,2026-08) | 【实验】 |
| Credit(机器信用) | 不存在;最接近的是虚拟卡额度与 AP2 open mandate | 机器经济成熟的必要条件之一,完全空白 |

GENIUS Act(2025-07-18 签署)核心义务 2027-01-18 才生效,截至 2026 年 8 月**无任何最终规则落地**——稳定币的合规红利仍在"预期"阶段。

### L1 — Settlement(结算层)

区块链(Base、Solana——x402 流量 2026-08 起 Solana 占月度 volume 约 70%;Tempo——Stripe 系 payments-first L1,2026-03-18 主网;Arc——Circle 链,2026-09-16 主网,验证人含 BlackRock/DTCC/Visa/Mastercard)、银行轨道(RTP/FedNow)、卡网络。**结算层的关键事实:卡组织正在双向下注**——Visa 稳定币结算年化 $70 亿(2026-04,占其 $12 万亿+ 总量的 <0.1%,期权性质),同时 Visa/Mastercard 都是 Tempo/Arc 验证人和 x402 Foundation 成员。

### L2 — Payment Protocol(支付协议层)

| 协议 | 发起方 | 工作方式 | 支持资产 | Micropayment | Session | 区块链依赖 | Adoption(2026-08) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **x402** | Coinbase(2025-05)→ x402 Foundation(Linux 基金会,2026-07-14 正式运营,40 成员含 Visa/MA/Amex/Stripe/AWS/Google) | HTTP 402 按请求付款;V2(2025-12)加入钱包身份、API 发现、CAIP 多链与法币兼容 | USDC 主导(99.8%)、EURC、AUSD | **是(最低 $0.000001,Circle Gateway)** | V2 部分支持 | 是(12 链) | 累计 1.69 亿笔/$4,140 万;organic 日 $2.8–4 万;AWS AgentCore 默认支持 |
| **MPP(Machine Payments Protocol)** | Stripe+Tempo(2026-03-18 与主网同日发布) | HTTP 402 + **sessions 原语**(一次授权支出上限、流式扣款,"OAuth for money") | 轨道无关:稳定币/卡(Stripe)/钱包(Visa)/Lightning(Lightspark) | 是 | **是(核心设计)** | 否(rail-agnostic) | 上线目录 100+ 服务;Tempo 链上 MPP 仅 45,274 事件/1,848 付款方(极早期);Anthropic/OpenAI/Shopify 为设计伙伴 |
| **AP2** | Google(2025-09-16,60+ 机构) | Mandates(VC 可验证凭证:Intent/Cart/Payment;v0.2 加入 Human-Not-Present) | 支付无关(含 A2A x402 扩展) | 委托下层 | open mandate 类似 | 否 | 2026-04-28 捐给 FIDO Alliance;无公开交易量,标准竞争阶段 |
| **ACP(Agentic Commerce Protocol)** | Stripe+OpenAI(2025-09-29) | 商家目录+委托支付(SPT) | 卡为主 | 否 | 否 | 否 | Instant Checkout 撤回后转型"发现协议";PayPal 为第二家 PSP |
| **UCP** | Google+Shopify+沃尔玛(2026-01) | 发现→结账→售后全流程 | 卡为主 | 否 | 否 | 否 | 酒店业技术委员会含 Booking/Expedia/万豪/希尔顿 |
| **Visa TAP / Intelligent Commerce** | Visa(2025-04/10) | RFC 9421 HTTP 消息签名的 agent 身份+agent 专用 token+Passkey | 卡 | 否 | 否 | 否 | 2026-07-02 欧洲 live(31 家发卡行);100+ 生态伙伴 |
| **Mastercard Agent Pay** | Mastercard(2025-04) | Agentic Tokens(MDES 扩展)+Web Bot Auth | 卡+稳定币(MTN) | 否 | 否 | 否 | 2026-03 Santander 欧洲首笔 live;Fiserv 大规模收单整合;$18 亿收购 BVNK |

**协议层结论**:(1)HTTP 402 语义成为共识,x402 与 MPP 在 AWS AgentCore 层已互通,碎片化风险下降;(2)身份/授权原语三路合流于 RFC 9421 + mandate 凭证;(3)**协议本身全部免费开源——L2 层没有收费能力,价值外溢到 L0(货币发行)、L3(处理)与 L7(市场)**。

### L3 — Facilitator / Processor

Facilitator 解决的问题:替卖方验证支付、代付 gas、批量结算、对账——即把"链上收款"变成"一行代码"。格局(2026-08,x402.fuchss.app 链上实测):按 30 天结算额 Meridian 43.1%、Coinbase CDP 24.3%、PayAI 17.1%;**按笔数 Coinbase CDP 占 70–93%**(全时段累计结算 $2,860 万第一)。Coinbase 最大的原因:默认设施(协议发起方)+免费额度(每月 1,000 笔后 $0.001/笔)+Base 链主场+CDP 钱包/AgentKit 全家桶捆绑。传统侧对应物:Stripe(收购 Privy 钱包、Bridge 稳定币、Tempo 链,构成"agent 支付全栈")与 Fiserv(Agent Pay 收单)。**Facilitator 费率已定价到 $0.001/笔——这一层从出生起就是商品化的**。

### L4 — Wallet / Account / Authorization

机器如何持有钱与被约束:MPC 钱包(Circle Agent Wallets:2-of-2 MPC+策略引擎+制裁筛查)、TEE+session key(Coinbase Agentic Wallets 2026-02:agent 永不接触主私钥,EIP-7702 权限作用域)、嵌入式钱包(Privy 7,500 万账户,2025-06 被 Stripe 收购;Turnkey 独立,年收入约 $2,250 万,按签名计费)、企业虚拟卡(Ramp Agent Cards:每 agent 一张带限额 tokenized 卡)。**关键数据:EIP-7702 升级账户仅约 2.5 万个(2026-03,blockeden)——链上授权采用与"数亿 agent"叙事相差 4 个数量级**。行业范式已收敛:时限+限额+函数白名单+资产约束+频率限制的 session key。防失控靠三层:钱包策略引擎(硬约束)、支出监控(Bedrock AgentCore 在基础设施层强制限额)、上级 agent 治理(Project Vend 的"CEO agent"实证有效)。

### L5 — Identity / Reputation

- **ERC-8004(Trustless Agents)**:三注册表(Identity/Reputation/Validation)。注册 50.9 万 agent、跨 24 链(2026-08-26,agenteconomy.to),但:日新增仅 28 个;**Validation Registry(zkML/TEE 质押验证——真正 trustless 的部分)仍 unstable 未部署**;质量分层 S/A/B 级仅 1,793 个。**注册量是虚荣指标,有效供给极小。**
- **KYA(Know Your Agent)**:Skyfire KYA 被 Experian 采纳为其 agent 身份层;IMF 2026-04 官方 Note 提出 KYC→KYA 方向;但**没有任何监管机构以 KYA 立规**——目前是自愿治理框架。
- **Web 层收敛**:Cloudflare Web Bot Auth(RFC 9421)被 AWS/Akamai 集成、被 Mastercard Agent Pay 采纳,OpenAI/Browserbase 等已签名请求;Visa TAP 同样基于 RFC 9421。**卡组织、CDN、Crypto 三路在同一密码学原语上合流,是 2026 年基础设施层最重要的收敛事件。**
- **企业内部身份**:Microsoft Entra Agent ID(2026-05 GA,agent 获得与人类并列的目录身份、纳入条件访问)——机器身份的最大规模落地在企业目录,不在链上。

### L6 — Discovery / Communication

MCP(工具调用,活跃注册 server 约 2.26 万,2026-08;已捐 Linux 基金会 Agentic AI Foundation,与 Block/OpenAI 共同发起)≠ 支付协议;A2A(agent 间通信,150+ 组织,Linux 基金会);服务发现:Coinbase x402 Bazaar(2.56 万资源)、MCP registry。**发现层的真实问题是"鬼城率":x402 全网 11.8 万个列出端点中 52% 不可达,仅 3,226 个收款钱包真实收过款**(2026-08,fuchss.app)。

### L7 — Marketplace

Agent 市场(Virtuals ACP:累计 aGDP $4.82 亿但服务收入仅 $450 万、投机/服务比 3,300:1;Olas Mech:35.9 万任务但累计营业额仅 $10.8 万)、API 市场(x402 Bazaar、AWS AgentCore Gateway 的 MCP 付费市场)、算力市场(见 10.6)、数据市场(Grass 等)。**结论:开放 agent 市场全部处于【实验→早期】;真实的"agent 劳动市场"藏在 Upwork MCP server(2026-08-10:AI 工具可直接发职位/发 offer)与企业内部编排中。**

### L8 — Autonomous Commerce(自主商业闭环)

```text
发现需求→搜索供应商→比较质量→比较价格→谈判→付款→调用→验收→评价→再次购买
```

截至 2026 年 8 月的实现度:发现(MCP/Bazaar,已实现但鬼城率高)→比较(价格比较已实现,质量比较靠 8004 声誉,未成熟)→**谈判(基本未实现,无标准)**→付款(x402/MPP 已实现)→调用(MCP 已实现)→**验收(最大缺口:结果验证无标准,zkML/TEE 未成熟)**→评价(8004 Reputation 早期)→复购(留存数据极差,Robinhood Chain agent 活动 30 天 -80%)。**闭环的断点在"谈判"与"验收"——这两步是 Autonomous Commerce 从管道变成市场的关键,也是下一代基础设施创业的真实空间。**

---

## 13. Machine Economy 项目生态地图(项目作为产业结构证据)

| 项目 | 产业层级 | 核心功能 | 当前规模(2026-08) | Revenue Model | Network Effect | Switching Cost | Commoditization Risk |
| --- | --- | --- | --- | --- | --- | --- | --- |
| OpenAI / Anthropic | 智能层 | 模型+Agent 能力 | run-rate $400 亿+/$650 亿+(口径不同) | API 用量+订阅 | 中(数据飞轮存疑) | 中高(工作流嵌入) | 中(开源追赶) |
| Coinbase | L1/L3/L4 | Base 链+CDP facilitator+AgentKit+Bazaar | facilitator 笔数份额 70–93% | 交易费+facilitator 费+托管 | 中 | 中 | **高(费率 $0.001/笔)** |
| Circle | L0/L3/L4 | USDC+Arc 链+Agent Stack(纳米支付/钱包/市场) | USDC $733 亿流通;Q2 收入 $7.01 亿 | 储备利息(主)+链费 | **高(货币网络)** | 高 | 低-中(利率依赖) |
| Stripe | L0–L4 全栈 | ACP+MPP+Tempo+Privy+Bridge+Open Issuance | Tempo 主网+100+ MPP 目录服务 | 支付抽成+发行 | 高(商户网络) | 高 | 低 |
| Tether | L0 | USDT+Plasma/Stable 链 | USDT $1,832 亿;自有链退潮(XPL -93%) | 储备利息 | 高 | 高 | 低 |
| Visa / Mastercard | L2/L5 | TAP/Agent Pay+稳定币结算+验证人席位 | Visa 稳定币结算 $70 亿年化;agent 交易 live 但无规模披露 | 网络费 | **极高** | 极高 | 低 |
| Google | L2/L6 | AP2+A2A+UCP+Gemini | A2A 150+ 组织;AP2 入 FIDO | 云+广告(协议免费) | 高 | 中 | 协议层无收费 |
| Microsoft | L5(身份) | Entra Agent ID+Agent 365+Copilot | Agent 365 GA(2026-05);Copilot 5,000 万用户 | 订阅(按用户) | 高(目录锁定) | **极高** | 低 |
| AWS | L3/L7 | Bedrock AgentCore Payments(x402+MPP 双协议,2026-08-18 GA) | GA 一周,协议中立聚合 | 云用量 | 高 | 高 | 低 |
| Cloudflare | L5/L7(流量咽喉) | Web Bot Auth+Monetization Gateway+Cloudflare Wallets | 自动化流量占 HTML 57.5%;NET Dollar 未发行 | 订阅+计费抽成(未来) | **高(物理咽喉)** | 中 | 低 |
| Virtuals | L7 | Agent 发行+ACP 市场 | aGDP 累计 $4.82 亿;agent 服务收入仅 $450 万;VIRTUAL -87% | 发行抽成+交易费 | 弱(投机驱动) | 低 | 高 |
| Olas | L7 | Mech 市场+Pearl | 日活 agent 431;累计费用 $546 | 协议费 | 弱 | 低 | 高 |
| Skyfire / Catena / Crossmint / Halliday | L4/L5 创业层 | KYA/AI 原生金融/Agent Checkout | Skyfire×Experian;Catena $3,000 万 A 轮(2026-05);Crossmint 支持三大协议 | 按调用/抽成 | 弱→中 | 低 | 高 |
| Turnkey / Privy | L4 | 签名基础设施/嵌入式钱包 | Turnkey 收入约 $2,250 万;Privy 7,500 万账户(Stripe 旗下) | 按签名/按账户 | 中 | 中高 | 中 |
| peaq / IOTA | 机器 L1 | 机器身份+DID | peaq 335 万机器 ID(自报);IOTA 已转向贸易基础设施,市值 $2 亿边缘化 | 链费+代币 | 弱 | 低 | 高 |
| Aethir / io.net / Akash | 算力市场 | 去中心化 GPU | ARR $1.5 亿/$2,000 万累计/$420 万 | 算力抽成 | 中(双边市场) | 低 | 高(算力同质) |
| Grass / GEODNET / DIMO / Helium | 数据/DePIN | 机器数据采集与出售 | Grass H1 $1,700 万;GEODNET ARR $830 万;Helium $250 万/月 | 数据销售分成 | 中(覆盖网络) | 中 | 中 |
| BlockRun | L7(x402 生态) | AI 推理路由+按次 USDC 计费(95 模型) | x402 交易笔数大占比(80%+ 某测量窗口)但无独立收入数据 | 路由加价 | 弱 | 低 | 高 |

---

## 14. Crypto / Stablecoin 必要性辨析(Crypto Necessity Map)

**强反方论证先行**:机器经济当前 >99% 的真实收入(模型 API、数字劳动、Robotaxi、RaaS)从未接触区块链;企业 agent 支出走合同/发票/虚拟卡运转良好;OpenAI/Anthropic 千亿美元级收入全部用传统金融结算。**Machine Economy ≠ Crypto adoption 有大量实证。**

| 必要性等级 | 场景 | 依据 |
| --- | --- | --- |
| **强必要** | 微支付型机器对机器交易(按次 API/爬虫付费/纳米支付) | 约 76% 的 agent 交易金额低于 Visa $0.30 固定费下限——传统轨道**经济上无法承接**;Circle Gateway 支持 $0.000001 且免 gas |
| **强必要** | 无银行准入主体的机器收付(开放 agent 网络、跨境长尾开发者) | agent 无法通过 KYC/KYB 开户;permissionless 是唯一通路 |
| **明显优势** | 跨境 B2B 机器结算 | 稳定币 B2B 支付 $2,260 亿/年、+733% YoY(McKinsey×Artemis)——机器经济可搭车这条已被验证的轨道 |
| **明显优势** | 7×24 可编程结算(escrow、按结果自动分账、A2A 供应链) | 可编程性是智能合约独有;银行轨道无原生等价物 |
| **可有可无** | Agent 钱包与授权 | session key/MPC 与银行虚拟卡+OAuth 均可实现;Ramp Agent Cards 证明传统轨道可做 agent 专属支付工具 |
| **可有可无** | 算力/数据市场结算 | DePIN 用稳定币,云用发票,均运转 |
| **传统金融更优** | 企业采购(需要发票/审计/合同/退款) | UETA 缔约效力+虚拟卡限额+ERP 集成完胜;稳定币无 chargeback、无消费者保护 |
| **传统金融更优** | 消费购物(需要退款/争议/欺诈保护) | Instant Checkout 教训:税务/购物车/退款全是传统电商问题;卡组织 mandate 方案直接复用现有保护 |
| **传统金融更优** | Robotaxi/机器人充电维保(公司集中采购) | B2B 月结合同(Waymo×Element/Terawatt)成本更低、可审计 |
| **传统金融更优** | 受监管金融交易 | 证券/期货必须走持牌轨道 |

**结构性判断**:稳定币/区块链的真实生态位是**"机器长尾微支付 + 跨境 + 可编程分账"**,这是传统轨道在物理上(费率结构)无法进入的区间;其余场景 Crypto 只是可选轨道且常处劣势。**最大的中间变量是 Tokenized Deposits**——若银行代币化存款(JPMD 类)+Tempo 类合规链成熟,"可编程性"将不再是公链专属,稳定币的必要域会被进一步压缩到 permissionless 场景。

---

## 15. x402 / MPP 真实经济活动验证(数据深挖)

### 15.1 多口径数据全景(截至 2026-08-26/27)

| 指标 | 数值 | 口径与来源 |
| --- | --- | --- |
| 累计交易笔数 | 169,242,465 笔 | agenteconomy.to,12 链 18 facilitator,小时级刷新 |
| 累计结算金额 | $4,142 万(另口径 $5,200–5,600 万) | agenteconomy.to vs x402scan/fuchss.app(覆盖差异) |
| 30 天窗口 | 7,541 万笔 / $2,424 万 / 94,060 买家 / 22,000 卖家 | x402.org 官方 dashboard(截至 2026-08-24) |
| 平均/中位单笔 | 均值 $0.26–0.32 / 中位 $0.01–0.015 | Artemis/Forkast/BlockRun/MarkovianProtocol |
| 链分布 | Solana 占月度 volume 约 70%(2026-08 反超 Base);Base 累计笔数最大(8,497 万) | x402scan/Crypto Briefing |
| Tempo MPP | 45,274 事件 / 1,848 付款方 | agenteconomy.to(极早期) |

### 15.2 水分剥离(本报告最重要的数据操作)

四个独立方法学收敛于同一结论:

1. **Visa/Artemis 调整口径**:原始 $1.357 亿/1.783 亿笔 → 调整后 **$1,500 万/1.096 亿笔**——剔除 89% 的美元量、39% 的笔数(2026-08)。
2. **Artemis 逐月估算**:约 50% 交易人工造量;2026-01 时 Solana 上 86% 支付活动 inorganic;**2026-03 真实日 volume 仅约 $2.8 万**(CoinDesk 2026-03-11)——对照 x402 概念代币约 $70 亿总估值。
3. **x402watch 钱包分类**:25.8% volume 为 synthetic;更关键的是买家构成——**10,710 个活跃买家中真正的 AI agent 仅 381 个(1.3%),95% 是人类付费调用 API**(2026-08-05)。**当前 x402 经济主要是 H2M(人付钱给机器),不是 M2M。**
4. **学术测量(arXiv 2607.12575)**:价值 Gini 系数 0.9957;单一 payer→payee 对占全市场结算笔数 66.6%;CDP Bazaar 上 2.5 万个 Base 资源实际仅解析到 811 个收款地址,其中**仅 249 个终生收入 ≥$10,中位终生收入 $3.96**。结论原话:"广告容量与真实使用之间的鸿沟极大,agentic commerce 目前主要是基础设施自检。"

**特殊事件必须单独剔除**:PING(pay-to-mint 投机,2025-10,单周流量 +10,000%)、Ramp 接入(2026-08-20,7 万企业客户,带来 Solana 单周 $330 万——是企业级需求实验而非已证实的 organic 增长,需观察 90 天留存)。

### 15.3 质量改善的正面信号(不应被水分讨论淹没)

- $1+ 交易占 volume 比例从 49%(2025 初)升至 95%(2026 初,Chainalysis)——尘埃在死亡、真实付费在留存;
- 平均票面从 $0.20 升至 $0.30;30 天笔数较峰值 -96.5% 但这是**质量型收缩**;
- 企业级集成密集落地:Stripe 原生 x402(2026-02-10)、AWS AgentCore GA(2026-08-18,x402+MPP 双协议)、Fireblocks Agentic Payments Suite(2026-05-20)、Apify 2 万+ 爬虫 Actor 接受 agent 支付(2026-07)、Ramp(2026-08-20);
- 40 家机构(含四大卡组织成员中的 Visa/MA/Amex)加入 x402 Foundation(2026-07-14)。

### 15.4 判断

> **x402 的 1.69 亿笔交易是"管道压力测试",不是商业收入。** organic 日交易额 $2.8–4 万意味着链上机器支付的真实年化经济规模约 **$1,000–1,500 万**——比 Waymo 一家的年收入小一个数量级,比模型厂商收入小四个数量级。但基础设施标准的收敛速度(12 个月内完成协议/身份/钱包三层标准化,且 Web2 巨头全部下场)显著快于历史上任何一代支付标准——**这是典型的"基建先行"周期:管道过剩、货物稀缺。投资时钟上,现在处于"轨道铺完、等待火车"阶段,监测重点应从管道指标转向货物指标(AI agent 买家数、付费留存、External Revenue)。**

---

# 第五部分:价值链与叙事证伪

## 16. 价值链与利润池(Machine Economy Profit Pool Map)

对每一层回答:收入来源/收费模式/Take Rate/毛利潜力/护城河(网络效应、切换成本、规模经济、数据、分销、监管)/商品化风险/Token 价值捕获,以及**"为什么利润不会被上下游拿走"**。

### 16.1 各层利润池分析

**稳定币发行方(Circle/Tether)** — 收入=储备利息(浮存金模式),Take Rate 实质为无风险利率×流通量;毛利率极高(Tether 为全球人均利润最高的公司之一)。护城河:货币网络效应(USDC 在 x402 结算占 99.8%)+监管牌照(Circle OCC 信托牌照、MiCA 授权;USDT 无 MiCA 授权被逐出 EEA 零售)。风险:利率下行直接压缩利润;tokenized deposits 的银行竞争。**Token 捕获:无需 token,股权即捕获。为什么上下游拿不走:货币是网络效应最强的商品,协议与 facilitator 都必须结算到某种货币——货币层向所有管道收"铸币税"。利润池评级:最高。**

**区块链(Base/Solana/Tempo/Arc)** — 收入=交易费+MEV;机器支付单笔费用趋零(这正是被选中的原因),**单位交易价值捕获极低**,靠量堆积。x402 在 Solana 单周 330 万笔对链收入贡献可忽略。真正价值是**把发行方/交易所的生态锁进来**(Base 之于 Coinbase、Tempo 之于 Stripe、Arc 之于 Circle——三大链全部是"母公司战略资产"而非独立利润池)。Token 捕获:弱(机器支付要求费用趋零,与 token 价值累积根本冲突)。

**支付协议(x402/MPP/AP2)** — **收入=零。全部开源免费,且已捐给中立基金会**(Linux/FIDO)。这是行业刻意的选择:协议收费会阻碍采用。Value creation 巨大、value capture 为零——协议是"公地",利润流向协议之上的实现方。

**Facilitator/Processor(Coinbase CDP/Meridian/PayAI/Stripe)** — 收费 $0.001/笔已见底,格局已多家混战(29 家被追踪)。organic 量 $1,500 万/年 × 0.1% take rate = **全行业年收入 <$2 万**——当前是纯战略卡位。长期看向 Stripe 模式演化(捆绑合规/对账/退款/发票=提高 take rate 到 1–3%),**能否收费取决于能否捆绑合规服务,而非处理本身**。商品化风险:极高。

**钱包/授权(Turnkey/Privy/Circle Wallets/Ramp)** — 按签名/按账户收费;毛利高(纯软件);切换成本中高(密钥迁移+策略配置)。**这一层是"agent 失控风险"的收费点**——风险越大,策略引擎越值钱。企业侧(Ramp Agent Cards、Entra Agent ID)比链上侧空间大一个数量级。商品化风险:中。

**身份/声誉(ERC-8004/KYA/Web Bot Auth)** — 当前无收入模式;长期最佳类比是 Experian/征信局——**Skyfire×Experian 合作揭示了终局:agent 信用局**。若形成,监管护城河+数据飞轮双高;但当前 Validation 层未完成,收费为时过早。**这是"利润池将在但尚未形成"的一层,值得作为期权持有。**

**Marketplace(Bazaar/Virtuals/AWS AgentCore Gateway)** — 抽成模式(App Store 类比,潜在 take rate 15–30%);但当前鬼城率 52%、复购留存极差。**谁能解决"验收"(结果验证)谁才配得上抽成**。若 AWS/微软用云捆绑赢得市场层,独立市场无空间。商品化风险:中(若解决信任则低)。

**模型层(OpenAI/Anthropic/Google)** — 当前机器经济最大现金流($1,000 亿+ run-rate)且 Anthropic 已调整后经营利润转正(2026Q2,Bloomberg)。**但模型层同时是最大 capex 消耗者**(行业 2026 capex $7,400–8,000 亿 ≈ 经营现金流 99%)。定价权取决于前沿能力差距;开源与蒸馏是持续的商品化压力。**为什么利润不会被拿走:目前"智能"是机器经济唯一供不应求的投入品——但这是周期性而非结构性的。**

**数据提供方** — 爬虫经济重构中,Cloudflare 是关键变量:它不拥有内容,却控制计费咽喉(57.5% 自动化流量流经其网络)。**内容方分散无议价权,咽喉层集中有议价权**——利润更可能沉淀在 Cloudflare 类聚合计费层而非单个内容方。

**算力层** — 云:规模经济+锁定,高利润但重资本;DePIN:同质商品+SLA 劣势,take rate 被压缩,**商品化风险最高的一层**。

**Agent 平台/应用层(Sierra/Harvey/Cursor 类)** — 按结果收费给了它们超越 SaaS 的定价空间(对标人类工资而非软件预算);但上游模型费用占 COGS 大头,毛利被模型层挤压(Cursor 类的模型成本问题公开讨论已久)。**护城河=工作流嵌入+领域数据+分销**,不是模型能力本身。估值风险:Sierra 79 倍 P/S、Lovable 26.6 倍——为完美执行定价。

**物理机器运营商(Waymo/Zipline/Locus)** — 重资产+运营护城河(监管牌照、安全记录、地图/网络覆盖);盈利前夜(百度武汉打平、丰翼单航线打平、Zipline 目标单次配送成本 $2–4)。**规模经济与监管准入双护城河,商品化风险最低的一层,但资本回报周期极长。**

### 16.2 利润池总表

| Layer | 收入来源 | Take Rate | 毛利潜力 | 网络效应 | 切换成本 | 商品化风险 | Token 捕获价值? |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 稳定币发行 | 储备利息 | ~利率×流通量 | 极高 | 极高 | 高 | 低-中 | 否(股权捕获) |
| 区块链结算 | 交易费 | 趋零 | 中 | 中 | 中 | 高 | 弱(费用趋零悖论) |
| 支付协议 | 零(开源) | 0 | — | 高(标准) | 高 | — | 无 |
| Facilitator | $0.001/笔 | ~0.1% | 低 | 弱 | 低 | **极高** | 否 |
| 钱包/授权 | 按签名/账户 | — | 高 | 中 | 中高 | 中 | 否 |
| 身份/信用 | 未形成 | — | 潜在极高 | 潜在极高(数据飞轮) | 潜在高 | 低(若形成) | 部分(质押模型) |
| Marketplace | 抽成 | 潜在 15–30% | 高 | 潜在高 | 中 | 中 | 弱 |
| 模型层 | API 用量 | — | 高(但 capex 巨大) | 中 | 中高 | 中 | 否 |
| 数据咽喉(CDN) | 计费抽成 | 潜在 10–30% | 极高 | 高 | 中 | 低 | 否 |
| 算力 | 用量 | — | 云高/DePIN 低 | 中 | 云高/DePIN 低 | DePIN 极高 | 弱 |
| Agent 应用 | 订阅+按结果 | 对标人力成本 | 中高(被模型挤压) | 弱-中 | 中(工作流) | 中 | 否 |
| 物理机器运营 | 服务费 | — | 长期高 | 中(网络密度) | 高(牌照) | **低** | 否 |

---

## 17. Value Creation vs Value Capture

| Layer | Value Creation | Value Capture | Pricing Power | Commoditization Risk |
| --- | ---: | ---: | ---: | ---: |
| 支付协议(x402/MPP/AP2) | **极高**(整个生态的公共品) | **≈零** | 无 | —(已是公地) |
| 稳定币发行 | 高 | **极高** | 中(受利率与竞品约束) | 中 |
| Facilitator | 中 | 极低 | 无($0.001 见底) | 极高 |
| 区块链结算 | 高 | 低 | 低 | 高 |
| 模型层 | **极高** | 高(但被 capex 吞噬) | 高(前沿期)→中(平台期) | 中 |
| 身份/信用 | 高(未来) | 未形成→潜在极高 | 潜在高(征信类比) | 低 |
| 数据咽喉 | 中 | 高 | 高(垄断位置) | 低 |
| Agent 应用 | 高 | 中 | 中高(按结果计价) | 中 |
| 物理机器运营 | 高 | 低(现在)→高(盈利后) | 中(受监管定价约束) | 低 |
| Agent 代币(Virtuals 类) | 低 | 曾极高(投机)→崩塌 | 无 | 已被证伪 |

**三个最重要的错配**:(1)x402 创造了行业标准但一分钱收不到——**做多 x402 生态 ≠ 做多任何 x402 代币**(x402 概念代币 $70 亿估值 vs organic 日 volume $3 万是本周期最大的价值错配);(2)模型层创造最多价值但 capex 吞噬利润——**利润的时间分布后置且不确定**;(3)身份/信用层当前零收入但可能是十年后的 pricing power 之王——**唯一值得用期权思维配置的早期层**。

---

## 18. 未来 5 / 10 / 20 年演进(预测成立条件,标注置信度)

### 2026–2031(高可见度)

- **Agent buying APIs/models/data 成为企业默认架构**——模型路由、数据按调用采购在预算内自主执行【High Confidence】;
- **按结果计费扩展到 coding 与更多知识工作**(客服已过半)【High Confidence】;
- **企业采购的审批阈值持续上调**,"例外人审"成为主流(Coupa 模式扩散)【High Confidence】;
- **Agentic shopping 以"AI 发现+商家结账+商家付佣"模式规模化**,占电商个位数→10%+ influenced 份额【High Confidence】;agent 全自动成交突破 5%【Medium】;
- **Robotaxi 在美中头部城市实现运营盈利**(Waymo 2027 指引、百度扩大打平城市)【Medium-High】;
- **链上机器支付找到第一个真实 PMF**:最可能是爬虫/数据微支付(Cloudflare Monetization Gateway+Apify 路径)【Medium】;
- **Tokenized deposits 进入机器支付**(JPMD 类+Swift 试点转生产)【Medium】;
- **Agent 信用/保险产品出现**(为 agent 交易承保)【Medium】;
- Agent-to-Agent External Revenue 出现可测量规模【Low/Option】。

### 2031–2036(中等可见度)

- **机器 OPEX 自动化**:车队/机器人按台核算并自动采购充电维保,"机器承担自己的 OPEX"在会计与支付层同时实现【Medium】;
- **Agent 劳动市场成型**:跨组织的 agent 雇佣与分包,验收标准(验证层)成熟【Medium】;
- **机器信用体系**:基于 8004 类声誉+历史 P&L 的 agent 授信,机器可以"借钱经营"【Medium-Low】;
- **Robot 经济过拐点**:人形机器人从万台级到百万台级,RaaS 按任务计费成主流【Medium】;
- **能源机器经济全面自动化**:百万台级 V2G、户用电池全部自动交易【Medium-High】;
- 预测市场/资管中 agent 管理的真实 AUM 达百亿美元级【Medium-Low】。

### 2036–2046(长期结构性推演)

- **Autonomous Economic Machine 出现**:机器(或机器集群)以准法人形态运营完整 P&L,人类角色退化为资本所有者与治理者【Low/Option】——前提:法律实体创新(机器 LLC/DAO 类结构)+验收与保险体系成熟;
- **Machine hiring Machine 成为供应链常态**,内部编排外化为市场交易【Medium-Low】;
- **机器最终仍不产生最终需求**——所有机器经济仍锚定人类效用;真正的结构变化是**人类从"劳动者+消费者"变为"资本所有者+消费者"**,收入分配问题(而非技术问题)成为机器经济的最大约束【High Confidence(方向)】。

---

## 19. 八大叙事逐项证伪

### 叙事 1:Agent 数量增长 = Machine Economy 增长

支持:Agentverse 270 万注册 agent、ERC-8004 50.9 万注册。反方:ERC-8004 日新增仅 28 个、S/A/B 级质量 agent 仅 1,793 个;x402 端点 52% 不可达;MCP top 0.1% 包占 84% 安装量。**判断:证伪。注册量是本赛道噪音最大的虚荣指标;有效 agent(有收入或有留存支出的)比注册量小 2–3 个数量级。**

### 叙事 2:x402 Transaction 增长 = 真实商业需求

支持:累计 1.69 亿笔、$1+ 交易占比升至 95%、企业集成密集。反方:四个独立方法学证明 85–95% 活动非 organic;真实日 volume $2.8–4 万;单一 payer-payee 对占 66.6% 笔数。**判断:大部分证伪。管道测试与投机主导;但质量指标改善是真实的,应跟踪 organic 子集而非总量。**

### 叙事 3:Agent 有 Wallet = Agent 成为经济主体

支持:钱包基础设施成熟(MPC/session key/限额)。反方:x402 上真正的 AI agent 买家仅 381 个;有钱包的 agent 绝大多数只花人类充值的钱、无收入、无 P&L;法律上所有资产归属人类实体。**判断:证伪。钱包是必要非充分条件;经济主体的判据是 Earn→Spend→P&L→Allocate,当前无 agent 走完全程(Project Vend 是唯一接近的受控实验)。**

### 叙事 4:Agent-to-Agent Payment = Agent Economy

支持:Olas 1,420 万笔 A2A 链上交易;Virtuals ACP 249 万任务。反方:Olas 累计营业额仅 $10.8 万、协议费 $546;Virtuals agent 服务收入 $450 万 vs 代币换手 $152 亿(1:3,300);A2A 调用的真实主场在企业内部编排(不产生市场交易)。**判断:证伪(作为现状描述)。A2A 支付量当前是激励与测试的函数,不是经济需求的函数。**

### 叙事 5:Stablecoin 是唯一合理的 Agent Payment

支持:x402 结算 99.8% USDC;微支付费率优势真实;7×24。反方:企业 agent 支出 99%+ 走传统轨道且运转良好;卡组织 mandate 方案直接复用现有消费者保护;tokenized deposits 正在补齐可编程性;MPP 本身 rail-agnostic。**判断:证伪。稳定币在微支付/跨境/permissionless 生态位强必要,在其余场景只是选项之一。**

### 叙事 6:Micropayment 一定需要 Blockchain

支持:76% agent 交易低于 Visa 固定费下限;Circle 纳米支付 $0.000001。反方:微支付的历史失败主因是**心理账户成本与聚合替代**(订阅/预付池),不是轨道成本;Stripe MPP 的 sessions(一次授权+流式扣款)证明"聚合后批扣"可在任何轨道实现;内部记账(OpenRouter 预充值)承载了今天绝大多数机器微消费。**判断:部分证伪。需要的是"微计量"(metering),不一定是"微结算"(micro-settlement);区块链只在结算双方互不信任且无中介时必要。**

### 叙事 7:Machine-to-Machine GMV = 新经济价值

支持:无(该叙事在方法论上即错误)。反方:第 5 节的核算框架——内部 GMV 是中间品交易,每加一层调用 GMV 翻倍而 External Revenue 不变。**判断:证伪。永远用 External Revenue → Internal GMV → Net Value Added 三层核算。**

### 叙事 8:AI Agent 会形成独立于人类的经济需求

支持:agent 会为完成任务采购资源(派生需求真实存在且高速增长)。反方:机器没有效用函数;所有 agent 支出向上追溯都终结于某个人类预算;Project Vend 中 Claudius 的"需求"完全由人类顾客定义。**判断:证伪(可见期内)。机器需求 100% 是派生需求。该叙事唯一的合理版本是:机器作为中间需求方的采购规模可以远大于最终需求(类似制造业中间品贸易>最终消费品贸易)——这是真实且可投资的,但与"独立需求"是两回事。**

---

# 第六部分:监测体系

## 20. Leading / Confirming / Catalyst 指标体系

基于全景研究重新判断(而非沿用候选清单),真正有判别力的指标如下。

### A. Leading Indicators(领先指标)

| 指标 | 为什么领先 | 当前读数(2026-08) |
| --- | --- | --- |
| **AI agent 买家数(链上,x402watch 口径)** | 机器自主消费的最直接计数,领先于一切 GMV | 381 个(占买家 1.3%)——基数极低,任何数量级跃迁都是强信号 |
| **按结果计费收入占比(分品类)** | 数字劳动被直接定价 = 机器劳动市场形成的先导 | 客服 >50%;coding <10%(hybrid 为主);纯 usage 合同仅 9% |
| **企业 agent 自主付款的审批阈值与批量金额** | E0→E1 迁移的最硬证据 | Coupa 单批次 $2,010 万级已出现;Ramp Agent Cards 早期访问 |
| **agent 支付的 90 天留存/复购率** | 区分测试与需求的唯一办法 | 极差(Robinhood Chain agent 活动 30 天 -80%);Ramp 集成留存待观察 |
| **单任务人工干预率(头部 agent 产品披露)** | 经济自主性的连续度量 | 零散披露(Codex 占企业 token 64% 是代理变量) |
| **新收入品类首次出现**(某类机器服务收入从 0→$100 万/月) | 品类扩张先于总量扩张 | 爬虫付费(Cloudflare Gateway waitlist)是最近的候选 |
| **agent 专属金融产品发行量**(虚拟卡/隔离账户/保险) | 供给侧为真实需求备货的行为 | Ramp/Robinhood/Coinbase for Agents 均 2026 年上线 |
| **模型 API 中"机器调用占比"**(batch/agent traffic vs 人类会话) | 机器作为客户的直接度量 | 无公开拆分——属"未来关键指标" |

### B. Confirming / Lagging Indicators(确认指标)

- **Organic 链上机器支付 volume**(经 Artemis/x402watch 调整):现 $2.8–4 万/日;
- **头部 Agent 公司收入与利润**:Anthropic/OpenAI run-rate、Agentforce/Sierra/Fin ARR、Anthropic 调整后经营利润(2026Q2 首次转正);
- **Robotaxi 单量与盈利**:Waymo 周单量(50 万平台期)、单车利用率(125 单/周)、百度打平城市数;
- **稳定币真实支付量**(McKinsey×Artemis 口径 $3,900 亿/年)与 B2B 子集($2,260 亿,+733%);
- **RaaS 装机与 ARR**(Locus $1.8 亿);
- **DePIN 法币收入**(Aethir $1.5 亿、Grass $1,700 万 H1);
- **MCP/协议生态的付费转化**(付费 MCP 工具收入,而非 server 数)。

### C. Structural Catalysts(结构性催化剂,离散事件)

| 事件 | 状态 |
| --- | --- |
| AWS 原生机器支付 | **已发生**(AgentCore Payments GA,2026-08-18,x402+MPP 双协议) |
| Stripe MPP 大规模开放 | 已上线(2026-03),规模化待观察 |
| GENIUS Act 细则生效 | 2027-01-18(锁定的最强监管催化剂) |
| Circle Arc 主网(BlackRock/DTCC 验证人) | 2026-09-16 |
| CLARITY Act 参院 cloture 投票 | 2026-09-15 |
| OpenAI 原生 agent 钱包/支付账户 | 未发生(现走 ACP+Stripe)——若发生为 P0 事件 |
| Amazon 开放第三方 agent 官方访问 | 未发生(诉讼中,九巡回已裁"工具而非人") |
| Visa/MA agent 支付公布 GMV | 未发生(只披露"live"无规模)——首次披露即为确认信号 |
| Waymo 100 万单/周 或 首次盈利披露 | 未发生(2027 指引) |
| 首个"机器人自主采购维保"生产案例 | 未发生 |
| 首个大型 API 厂商把按次机器支付设为默认计费 | 未发生 |
| Anthropic IPO(招股书首次披露 agent 经济结构数据) | 传闻 2026 秋 |

---

## 21. Machine Economy Signal Map

| Sector | 当前阶段 | Leading Indicator | Confirming Indicator | Catalyst | Data Source |
| --- | --- | --- | --- | --- | --- |
| 数字劳动(coding/客服) | 已规模化 | 按结果计费占比;干预率 | 头部 ARR/利润;AWU 类财报指标 | Anthropic IPO;coding outcome 计费标准化 | 财报、Sacra、Menlo、Metronome |
| 企业自主采购 | 商业化中 | 审批阈值上调公司数;agent 虚拟卡发行量 | 自主付款金额/季 | ERP 巨头默认开启 agent 付款 | Coupa/SAP/Ramp 披露、审计准则 |
| Agentic shopping | 早期(重构) | AI 渠道转化率 vs 官网比;平台 API 开放 | agent-executed GMV 占比 | Amazon 开放/诉讼终审;假日季数据 | Adobe、Salesforce、Similarweb |
| 链上机器支付 | 早期 | AI agent 买家数(381→?);90 天留存 | organic volume;facilitator 收入 | GENIUS 生效;大平台默认接入 | x402watch、Artemis、Dune `payments.agentic_payments`、agenteconomy.to |
| 数据/爬虫经济 | 早期 | Gateway 计费域名数;AI 公司按量付费合同 | 内容方 AI 收入 | Cloudflare 计费默认开启;top lab 常设结算机制 | Cloudflare Radar、Apify |
| 交易/预测市场 agent | 传统已规模化/链上早期 | agent 隔离账户数;agent AUM | agent PnL 规模;干预率 | SEC/CFTC 首个规则;首次 agent 闪崩 | Robinhood/Coinbase 披露、TurbineFi、DefiLlama |
| Robotaxi/物流 | 商业化中 | 单车利用率;远程协助率;保险费率 | 周单量;城市数;毛利 | Waymo 盈利;事故监管 | CPUC、财报、公司披露 |
| Robot/RaaS | 商业化中 | 按台 P&L 披露;维保 API 化产品 | RaaS ARR;人形出货 | 首个自主 OPEX 案例 | 财报(宇树/智元)、Sacra、IFR |
| 能源机器经济 | 局部已规模化 | V2G 车辆数;户储自动交易渗透 | VPP 容量;单车售电收入 | 车企原生 V2G 全量开放 | Tesla 财报、PG&E/Octopus、pv magazine |
| Agent 身份/信用 | 实验→早期 | 8004 Validation 部署;KYA 监管引用 | 有效 agent 数(质量分层) | 首个 agent 信用产品;监管 KYA 规则 | agenteconomy.to、8004scan、IMF/FinCEN 文件 |

---

## 22. 异动等级体系

不用单一指标阈值,用**多指标共振**定级:

- **Normal(正常)**:总量指标(volume/注册数)波动,organic 子集与留存无变化。例:x402 因单一集成或投机代币单周暴涨——历史上 PING、Robinhood Chain 均属此类。
- **Watch(关注)**:单一 leading 指标出现新行为。例:AI agent 买家数月增 >50%;某品类按结果计费首次出现;某企业公布 agent 自主付款数据;某平台开放 agent API。→ 动作:建立专项数据跟踪。
- **Inflection(拐点)**:**≥3 个 leading 指标同向共振,且 organic 口径同步确认**。例:AI agent 买家数量级跃迁 + 90 天留存转正 + facilitator 收入增长 + 新品类收入 >$100 万/月。→ 动作:启动项目级投资研究。
- **Structural Change(结构变化)**:商业模式或产业结构变化,通常由 Catalyst 触发并被数据确认。例:大平台把 agent 支付设为默认;首个机器自主 OPEX 生产案例;监管确立 agent 责任框架;某层利润池的 take rate 结构性改变。→ 动作:重构赛道配置。

**判别纪律**:任何"volume +30%"类信号必须先过三问——organic 口径是否同步?买家/留存是否同步?能否定位到单一催化剂(若能,降级为 Watch)?

---

## 23. Investment Trigger Map

| Trigger | 为什么重要 | 需要验证什么 | 可能受益方向 | Priority |
| --- | --- | --- | --- | --- |
| Organic 机器支付连续 2 季度加速(organic 口径) | 管道→货物的转换确认 | Artemis/x402watch 口径一致;非单一集成驱动 | 稳定币发行方、钱包/授权层、facilitator 中的合规捆绑者 | **P0** |
| AI agent 买家数与付费留存同时数量级增长 | M2M 经济从 1.3% 占比走向主流 | 买家分类方法学;留存曲线 | 数据/API 卖方、路由层(OpenRouter/BlockRun 类)、微支付基础设施 | **P0** |
| 某大平台(Amazon/OpenAI/Google)开放 autonomous purchasing 默认权限 | Final Demand 入口的闸门打开 | 是否默认开启;佣金结构 | agent 应用层、身份/授权层、商家工具 | **P0** |
| Agent 开始管理真实 P&L(首批公司披露单 agent/单机 P&L) | E2→E3 的产业级迁移 | 核算口径;是否含自主支出权 | Agent 平台、机器保险/信用(新品类) | **P0** |
| 按结果计费在 coding 突破 20% 占比 | 最大品类的定价模式迁移 | Metronome 类合同数据 | outcome 定价基础设施、验收/评测层 | P1 |
| Tokenized deposits 进入机器支付生产环境 | 银行轨道补齐可编程性,重划 Crypto 必要域 | JPMD/Swift 试点转生产的交易量 | 银行技术层;利空纯公链结算叙事 | P1 |
| Robotaxi 首次公司级盈利 | 物理机器经济单位经济学证真 | 含全成本口径(非单城打平) | AV 运营商、车队服务层(充电/维保/保险) | P1 |
| 机器人维保/充电服务 API 化产品出现 | 机器自主 OPEX 的供给侧前提 | 真实调用量 | 车队管理软件、机器服务市场 | P1 |
| Agent-to-Agent External Revenue 首次可测量 | 开放 agent 劳动市场的成立证据 | 交易对手非同一主体;外部客户资金传导 | Agent 市场层、验收/声誉层 | P1 |
| 首个 agent 信用/保险产品规模化 | 机器信用 = E4/E5 的金融前提 | 承保数据、赔付率 | 新品类(agent 征信局) | P1 |
| Visa/MA 首次披露 agent GMV | 传统轨道 agentic 规模首次可测 | 口径(influenced vs executed) | 卡组织、发卡行技术层 | P2 |
| **Volume 增长但买家/钱包数不增长** | **Negative Signal:集中度上升=少数玩家刷量或垄断** | Gini 系数;top pair 占比 | 减仓管道类资产 | P2(风控) |
| Agent 引发的重大事故(错误采购/闪崩/欺诈) | 监管收紧的触发器 | 责任判定结果 | 利好合规/授权层,利空 permissionless 叙事 | P2(风控) |

---

## 24. Core Machine Economy Monitoring Dashboard(收敛为 12 个核心指标)

| # | 指标 | 定义 | 为什么重要 | Leading/Lagging | 数据源 | 更新频率 | 当前可获得性 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | **机器经济 External Revenue 合成指数** | 模型 API 收入+agent 产品 ARR+robotaxi/无人机收入+RaaS ARR 加权 | 唯一的"真实规模"度量(Scale) | Lagging(锚) | 财报/Bloomberg/Sacra | 季 | 高(需自建合成) |
| 2 | **按结果计费收入占比(分品类)** | outcome-based 合同收入/品类总收入 | 数字劳动直接定价渗透(Monetization) | **Leading** | Metronome、各公司定价页、财报 | 季 | 中 |
| 3 | **AI agent 买家数与占比** | 链上机器支付中被分类为 agent 的活跃买家 | M2M 是否真实发生(Quality) | **Leading** | x402watch、Artemis | 周 | 高(基数小) |
| 4 | **Organic 机器支付 volume** | 剔除 wash/测试/激励后的链上机器支付额 | 管道中的真实货物(Scale+Quality) | Confirming | Artemis、Dune curated 表 | 周 | 高 |
| 5 | **agent 支付 90 天留存率** | 首次付费 agent/集成在 90 天后仍活跃的比例 | 区分测试与需求(Quality) | **Leading** | Dune 自建、x402watch | 月 | 低(需自建) |
| 6 | **企业 agent 自主付款金额与审批阈值** | 生产环境中 agent 无人工审批执行的付款额 | E0→E1 迁移速度(Autonomy) | **Leading** | Coupa/Ramp/SAP 披露、案例 | 季 | 低(零散) |
| 7 | **单任务人工干预率(头部产品)** | 每单位 agent 产出的人工介入次数 | 经济自主性的连续度量(Autonomy) | **Leading** | 公司披露(Waymo 协助率、OpenAI token 结构) | 季 | 低 |
| 8 | **新机器收入品类计数** | 单月收入首次突破 $100 万的机器服务新品类 | 场景宽度(Breadth) | **Leading** | 综合监测 | 月 | 中(定性+定量) |
| 9 | **agent 专属金融产品规模** | agent 虚拟卡/隔离账户/钱包的发行与资产量 | 资本为机器备货的程度(Capital) | Leading | Ramp/Robinhood/Coinbase/Circle 披露 | 季 | 中 |
| 10 | **机器支付基础设施采用指数** | AWS/Stripe/卡组织 agent 支付产品的 GA 状态与接入方数 | 基础设施采用(Infrastructure) | Confirming | 官方公告 | 月 | 高 |
| 11 | **Robotaxi 单车经济性** | 单车周订单×客单价 vs 单车周成本 | 物理机器经济的盈利拐点(Scale) | Confirming | CPUC、财报、BusinessModelAnalyst | 季 | 中 |
| 12 | **稳定币 B2B 真实支付量** | McKinsey×Artemis 口径 B2B 子集 | 机器支付可搭乘的合规轨道容量(Infrastructure) | Confirming | Visa Onchain、Artemis、McKinsey | 半年 | 中 |

**覆盖校验**:Scale(1,4,11)/ Quality(3,4,5)/ Breadth(8)/ Autonomy(6,7)/ Monetization(2)/ Infrastructure(10,12)/ Capital(9)。

---

## 25. Future Critical Metrics(今天没有数据、未来必须监测)

| 指标 | 为什么重要 | 今天为什么没有 | 未来如何采集 | 触发记录的产业变化 |
| --- | --- | --- | --- | --- |
| **Autonomous Revenue(机器自主收入)** | E2 的直接度量:无人工介入完成并收款的收入 | 公司不按"自主 vs 辅助"拆分收入 | 财报补充披露;按结果计费系统天然可产出 | 首家公司在财报中拆分披露时立即开始记录 |
| **Machine Operating Profit(机器营业利润)** | E3 的直接度量 | 无机器级损益准则 | RaaS/车队按台核算数据;管理会计准则演化 | 首个"单台/单 agent P&L"公开案例 |
| **Economically Self-Sustaining Agents 计数** | 收入>成本且持续 90 天+ 的 agent 数量,机器经济的"就业人数" | 收入与成本数据分属不同系统 | 平台层(AWS AgentCore 可观测性/Circle)聚合 | agent 平台开始发布生态报告 |
| **Human Intervention Ratio(全行业)** | 自主性光谱的连续读数 | 各公司口径不一且视为商业机密 | 行业基准(类似汽车业 MPI—miles per intervention) | 监管要求披露(AV 行业已有先例:CPUC/DMV) |
| **Agent-to-Agent External Revenue** | 开放 agent 劳动市场的成立判据 | 现有 A2A 数据无法区分同主体循环支付 | 身份层(8004/KYA)成熟后按最终受益人穿透 | 首个跨主体 agent 分包合同公开 |
| **Machine OPEX(机器自付运营成本)** | E1 在物理世界的度量 | 全部由公司集中支付,无机器颗粒度 | 车队管理系统按车结算数据;充电/维保 API 账单 | 维保/充电服务 API 化产品上线 |
| **Robot Autonomous Purchasing 笔数** | 物理机器 E1 的直接计数 | 不存在该行为 | 机器人车队管理平台 | 首个生产案例出现当日 |
| **模型 API 的机器调用占比** | 机器作为客户的份额 | 厂商不拆分 agent vs 人类会话流量 | 厂商披露或 OpenRouter 类中间层估算 | 任一头部厂商首次披露 |

---

## 26. 数据源地图(Machine Economy Data Source Map)

| 数据源 | 能看到什么 | 优势 | 缺陷 | 适合作核心监测? |
| --- | --- | --- | --- | --- |
| **Artemis** | 稳定币/x402 调整后(organic)数据 | 唯一系统性做水分剥离;被 Visa 采用 | 方法学黑箱部分;覆盖限链上 | **是(organic 口径基准)** |
| **x402scan / x402stats** | x402 原始交易/端点/facilitator | 实时、细粒度 | 原始口径含大量水分;各家覆盖不一 | 辅助(原始口径) |
| **agenteconomy.to** | x402/8004/ACP/Olas/MPP 跨协议汇总 | 12 链 18 facilitator 最全;开放 data.json/MCP | 依赖社区 facilitator 注册表 | **是(汇总口径)** |
| **x402watch** | 钱包分类(agent vs 人类 vs synthetic) | **唯一的买家构成数据(agent 占 1.3%)** | 新站,方法学待检验 | 是(质量口径) |
| **Dune(`payments.agentic_payments`)** | x402+MPP 统一 curated 表 | 最规范的跨协议口径 | 只覆盖链上 | **是(主链上口径)** |
| **DefiLlama / Token Terminal** | AgentFi TVL、DePIN 收入、协议费 | 独立可验证 | agent 分类粗;不含链下 | 是(证伪工具:AgentFi TVL 仅 $3,200 万) |
| **Coinbase(CDP/机构研究)** | facilitator 数据、Bazaar 目录 | 一手管道数据 | 利益相关方 | 辅助 |
| **Circle(财报/Gateway)** | USDC 流通、纳米支付、Agent Stack | 上市公司审计数据 | 只见 USDC 生态 | 是(货币层) |
| **Stripe/Tempo** | MPP 目录、Tempo 链数据 | 传统轨道 agent 支付唯一窗口 | 披露极少 | 观察(等待披露) |
| **Visa Onchain Analytics** | 稳定币调整后结算量 | 方法学公开(与 Allium/Artemis 共建) | 半年度级更新 | 是(稳定币基准) |
| **GitHub / npm / PyPI** | 框架采用(SDK 下载、star、MCP server 数) | 开发者行为领先指标 | 下载≠使用;bot 污染 | 辅助(Developer 信号) |
| **公司财报(Alphabet/百度/小马/文远/Aurora/宇树/Salesforce/微软/Circle)** | 物理机器与 agent 产品的审计级收入 | 最高可信度 | 颗粒度粗(Waymo 藏在 Other Bets) | **是(External Revenue 基准)** |
| **Sacra / Menlo / Metronome** | 私有公司 ARR 估算、定价模式合同数据 | 覆盖未上市主体 | 估算口径,误差大 | 是(私有市场) |
| **Cloudflare Radar** | 机器流量结构(57.5% 自动化)、爬虫/引荐比 | 互联网级样本、免费 | 只见其网络 | **是(机器流量基准)** |
| **CPUC/NHTSA/民航局** | Robotaxi/无人机监管级运营数据 | 强制披露、不可粉饰 | 滞后、限特定地区 | 是(物理机器) |
| **Agent Marketplace(Virtuals scan/Olas/Bazaar)** | A2A 交易与任务数据 | 链上可验证 | 激励扭曲严重、自报口径 | 辅助(需水分剥离) |
| **监管文件(OCC/FinCEN/FIDO/IMF/BIS)** | 规则时间表、KYA 方向 | 结构性催化剂的最早来源 | 非量化 | 是(Regulatory 信号) |

**口径一致性警告**:x402 累计 volume 在 agenteconomy.to($4,140 万)、fuchss.app(约 $5,600 万)、Visa/Artemis 原始($1.357 亿)之间相差 3 倍以上,原因是 facilitator 覆盖与链覆盖不同;**任何跨源对比必须锁定同一口径与 as-of 日期,任何单点新闻数字默认不可比**。

---

# 第七部分:最终结论

## 27. 十八个投资问题的直接回答

**1. Machine Economy 到底是什么?(一句话)**
机器经济是非人类系统在"赚钱—花钱—管理损益—配置资本"四个环节上自主性持续上升所形成的经济体系;投资对象是这一迁移的速度、真实外部收入的规模,以及基础设施中能捕获价值的层级。

**2. 今天真正存在的 Machine Economy 有哪些?(只列真实活动)**
① 数字劳动销售(coding/客服/法律 agent,百亿美元级);② 智能销售(模型 API,千亿美元级 run-rate);③ 算法交易与做市(美股 70% 成交量,存在 20 年);④ 电力自动交易与 VPP(Autobidder,E4);⑤ 物理任务收入(Robotaxi/无人机/RaaS,数十亿级、多数亏损);⑥ 自动计费网络(超充/Plug&Charge/售货机/智能电表,机器自动收付款的史前规模);⑦ 企业 agent 自主付款(Coupa 类,刚出现);⑧ 机器数据销售(DePIN 法币收入,千万美元级);⑨ 链上机器微支付(organic 日 $3–4 万,实验期)。

**3. 目前最大的 Machine Revenue 是什么?**
数字劳动+智能销售(模型 API 与 agent 产品),合计年化超 $1,000 亿(Anthropic $650 亿+OpenAI $400 亿 run-rate 为主体,口径需折让)。若把算法交易 PnL 算作机器收入,其规模同样巨大但属零和转移。

**4. 目前最大的 Machine Expenditure 是什么?**
机器(agent)消费的推理算力——模型 API 支出是一切 agent 的第一大成本项;其次是 GPU/沙箱算力与数据/搜索调用。注意:这些支出 99%+ 由人类组织的预算授权,agent 只是消耗者(E1 以下)。

**5. 当前 Machine Economy 最真实的 PMF 在哪里?**
按结果计费的客服 agent(解决成本 $1.25–3 vs 人工 $12–25,解决率 65–70%)与 coding agent(委托式任务占企业 token 64%)——数字劳动以 10–20 倍成本优势替代人类劳动,企业用真金白银投票。物理侧是 Robotaxi 的消费者付费(50 万单/周)与储能自动交易。

**6. 当前最大的伪繁荣在哪里?**
链上 agent 经济的总量指标:x402 的 1.69 亿笔交易(85–95% 非 organic)、50.9 万 ERC-8004 注册(日新增 28 个)、agent 代币估值(x402 概念代币 $70 亿 vs organic 日 volume $3 万;AI agent 代币板块已从 $200 亿跌至 $31 亿,-85%);以及"agent 管理数十亿 AUM"叙事(可验证 AgentFi TVL 仅 $3,200 万)。

**7. 未来最可能首先形成大规模经济活动的 10 个场景?**
① 按结果计费的数字劳动全品类化;② 企业采购/财务的 agent 自主执行;③ AI 发现驱动的电商佣金经济;④ 爬虫/数据按量付费市场;⑤ 模型/算力的 agent 自主路由采购;⑥ Robotaxi 规模盈利;⑦ 无人配送(中国低空经济+Zipline 模式);⑧ 储能/V2G 自动交易的百万台化;⑨ RaaS 按任务计费的机器人车队;⑩ 零售交易执行权向 agent 让渡(隔离账户模式)。

**8. 哪些场景必须使用 Stablecoin/Crypto?**
分厘级机器微支付(爬虫/API 按次)、无银行准入主体的开放 agent 网络、跨境长尾结算、需要可编程分账与 escrow 的 A2A 交易。判据:交易额低于卡组织固定费下限(约 76% 的 agent 交易)或参与方无法通过 KYC/KYB。

**9. 哪些场景传统金融明显更好?**
企业采购(发票/审计/退款)、消费购物(争议/消费者保护)、物理机器 OPEX(B2B 月结)、受监管证券交易、一切需要法律追索的高额交易。

**10. 什么时候 Machine 才真正可以视为"经济主体"?**
四个条件同时满足:(a)获得常设(非会话级)支出授权与预算;(b)收入与成本在同一张机器级损益表上核算;(c)有可追溯的身份与信用记录;(d)存在承接其法律责任的实体结构。截至 2026 年 8 月,没有任何机器同时满足四条;Project Vend 满足 (b) 的实验版。判据不是钱包,是**授权的持久性+损益的完整性**。

**11. 未来 Machine Economy 最大的三个瓶颈?**
① **验收与信任**:结果验证无标准(自主商业闭环断在"谈判"与"验收"两步),人类审计带宽成为物理约束;② **法律责任分配**:没有任何法域为"作为付款人的软件"分配责任,无判例、无专门规则;③ **需求侧真实性**:MIT NANDA 95% 试点无 P&L 回报所代表的组织落地鸿沟——技术供给远超组织消化能力。

**12. 产业链上最可能形成长期 Pricing Power 的层级?**
① 稳定币/货币发行(网络效应+浮存金);② 数据/流量咽喉(Cloudflare 类物理垄断位);③ 身份/信用层(若形成,征信局模式:数据飞轮+监管护城河);④ 物理机器运营(牌照+安全记录+网络密度);⑤ 前沿模型(周期性 pricing power,非结构性)。

**13. 最容易商品化的层级?**
Facilitator/支付处理($0.001/笔已见底)、支付协议本身(开源公地)、去中心化算力(同质商品)、agent 框架(开源竞争,ElizaOS 代币归零是标本)、无差异化的 agent 应用套壳。

**14. 资本市场目前可能高估了什么?**
① 链上 agent 支付的近期规模(narrative/usage 比极度失衡);② agent 应用层的持续独占性(Sierra 79 倍 P/S、Lovable 26.6 倍为完美执行定价,而模型层在挤压其毛利);③ AI capex 的短期回报(capex≈经营现金流 99%);④ "agent 数量"类指标的经济含义;⑤ Robotaxi 的扩张线性(Waymo 单量平台期被忽视)。

**15. 资本市场目前可能低估了什么?**
① 企业采购/财务 agent 的 E1 迁移速度(Coupa 案例几乎无人定价);② 能源机器经济(Autobidder/VPP 是已运转的 E4,无人叫它 agent);③ tokenized deposits 对机器支付格局的重划潜力;④ 身份/信用层的十年期权价值;⑤ 按结果计费对软件业估值范式的冲击(从 seat×价格到劳动替代量×分成);⑥ 中国低空经济与机器人供应链的单位经济学进展(美团单均 2.3 元、宇树盈利上市)。

**16. 如果 Machine Economy 即将进入加速阶段,最早出现的 5 个信号?**
① AI agent 买家数(现 381 个)出现数量级跃迁且 90 天留存转正;② 某头部平台把 agent 自主支付/采购设为默认开启;③ 按结果计费在 coding 类突破 20%;④ 首批公司公布机器级 P&L(单 agent/单机核算);⑤ agent 专属金融产品(虚拟卡/保险/信用)放量。

**17. 如果只能长期跟踪 10 个指标?**
第 24 节仪表盘的 #1(External Revenue 合成指数)、#2(按结果计费占比)、#3(AI agent 买家数)、#4(organic 机器支付)、#5(90 天留存)、#6(企业自主付款金额)、#7(人工干预率)、#8(新品类计数)、#9(agent 金融产品规模)、#11(Robotaxi 单车经济性)。

**18. 未来出现哪些事件时应立即启动专项投资研究?**
见第 23 节 Trigger Map 的四个 P0:organic 机器支付连续两季加速;AI agent 买家数与留存同时数量级增长;大平台开放 autonomous purchasing 默认权限;首批机器真实 P&L 披露。另加三个事件型:Anthropic IPO 招股书(首次审计级 agent 经济数据)、GENIUS 细则生效(2027-01)、Amazon v. Perplexity 终审。

---

## 28. 三张核心地图

### Map 1 — Machine Economy World Map

```text
                        FINAL DEMAND(机器不产生最终需求)
      Enterprise(第一)/ Trader对手盘 / Consumer / Merchant佣金 / Government
                                   │
                                   ↓
                        MACHINE / AGENT(经济主体光谱 E0→E5)
              软件Agent ── 物理Agent ── 数字机器资源 ── 基础设施机器
                     │                                    │
                   EARN                                 SPEND
                     │                                    │
     ┌───────────────┘                                    └───────────────┐
     ↓                                                                    ↓
 数字劳动($150-250亿/年,增速最快)                        Intelligence(模型API,第一大支出)
 智能/推理($1,000亿+ run-rate)                           Compute(GPU/沙箱)
 金融PnL(零和,存在20年,E4)                              Data(搜索/行情/爬虫付费)
 物理任务(Robotaxi/无人机/RaaS,数十亿)                   Software/API/MCP工具
 数据销售(DePIN千万级)                                    Financial Execution(gas/手续费)
 算力出租(云为主)                                         其他Agent服务(实验)
 佣金(agentic commerce,重构中)                           Energy/物理OPEX(全部人类代付)
 能源套利(Autobidder,E4)                                 实物商品(实验:Project Vend/Denso)
     │                                                                    │
     └────────────────────────────┬───────────────────────────────────────┘
                                  ↓
                    MACHINE P&L(2026:仅单位经济学核算存在;
              真实机器损益表 = Project Vend 实验 + RaaS/车队按台核算)
                                  ↓
                Capital Allocation(E4/E5:仅存在于量化交易与电力交易)
                                  ↓
                Reinvestment / Expansion(2026 年不存在,最远推演)
```

### Map 2 — Infrastructure Stack(2026-08 实况标注)

```text
Applications        │ Coding/客服/采购/购物/交易 Agent(收入最厚的一层)
────────────────────┼────────────────────────────────────────────
Marketplace         │ Bazaar/Virtuals/Olas/AgentCore Gateway(鬼城率高,验收未解)
────────────────────┼────────────────────────────────────────────
Discovery / Comm    │ MCP(2.26万server)+ A2A(150+组织)≠ 支付
────────────────────┼────────────────────────────────────────────
Identity/Reputation │ RFC 9421 三路合流(Visa TAP/MA/Cloudflare)+ ERC-8004(验证层未完成)
                    │ + Entra Agent ID(最大规模落地在企业目录)
────────────────────┼────────────────────────────────────────────
Wallet/Authorization│ MPC+session key+限额(Circle/Coinbase/Turnkey)
                    │ + 企业虚拟卡(Ramp Agent Cards)← 被低估的现实路径
────────────────────┼────────────────────────────────────────────
Payment Protocol    │ x402(V2,基金会40成员)/ MPP(sessions)/ AP2(FIDO)
                    │ / ACP(转型发现)/ TAP / Agent Pay ── 全部免费,无利润池
────────────────────┼────────────────────────────────────────────
Facilitator         │ Coinbase CDP/Meridian/PayAI/Stripe($0.001/笔,已商品化)
────────────────────┼────────────────────────────────────────────
Money               │ USDC(机器结算99.8%)/USDT/法币授信/Tokenized Deposits(JPMD,变量)
────────────────────┼────────────────────────────────────────────
Settlement          │ Base/Solana(x402主场)/ Tempo(Stripe)/ Arc(Circle)
                    │ / 银行RTGS+卡网络(agent支出的99%实际所在)
```

### Map 3 — Signal Map(监测流水线)

```text
World Map(第1-8节:主体×收入×支出×最终需求×自主性)
     ↓
Observable Economic Activity(第9节 Reality Map:哪些活动真实存在)
     ↓
Leading Indicators(第20A节:agent买家数/结果计费占比/自主付款阈值/留存/干预率)
     ↓
Confirming Indicators(第20B节:External Revenue/organic volume/头部ARR与利润)
     ↓
Structural Catalysts(第20C节:GENIUS生效/Arc主网/平台开放/IPO披露/判例)
     ↓
Inflection Detection(第22节:≥3个leading共振+organic确认=拐点)
     ↓
Investment Research Trigger(第23节:P0/P1/P2分级启动专项研究)
     ↓
Value Capture Analysis(第16-17节:拐点利好哪一层?该层能否留住利润?)
```

---

## 29. Machine Economy Monitoring Framework(可长期执行)

### 每周看什么

1. **x402watch 的 AI agent 买家数与买家构成**(基数 381,任何跳变都重要);
2. **Dune `payments.agentic_payments` 的 organic 趋势**(锁定口径,剔除单一集成脉冲);
3. 大平台公告流:AWS/Stripe/OpenAI/Google/Visa/MA 的 agent 支付产品动态(结构性催化剂的最早来源);
4. Cloudflare Radar 机器流量结构(爬虫经济的周度读数)。

### 每月看什么

1. agenteconomy.to 跨协议汇总(x402/8004/ACP/Olas/MPP)与留存类自建指标;
2. 头部 agent 公司 ARR 更新(Sacra/媒体:Sierra/Harvey/Cursor/Cognition 类);
3. Ramp/Coupa/Robinhood/Coinbase 的 agent 金融产品数据点;
4. 新收入品类扫描(是否有机器服务品类首次 >$100 万/月);
5. Robotaxi 月度:CPUC 数据、单车利用率、中国玩家单量。

### 每季看什么

1. 财报季全套:Alphabet(Waymo)/微软(Copilot usage)/Salesforce(Agentforce+AWU)/Circle/百度/小马/文远/Aurora/宇树;
2. Visa Onchain/Artemis 稳定币真实支付量(B2B 子集);
3. Metronome 类定价模式合同数据(结果计费占比);
4. 监管时间表推进(GENIUS 细则/CLARITY/EU AI Act/判例)。

### 哪些数据暂时不用看

- ERC-8004 注册总数、Agentverse agent 数、MCP server 总数(虚荣指标,只看质量分层子集);
- agent 代币价格与市值(与基本面已证明脱钩);
- x402 原始累计笔数/volume(只看 organic 与买家构成);
- peaq 类机器 ID 数(自报口径,无现金流锚)。

### 哪些数据噪音极高(使用时必须修正)

- 一切链上总量指标(先过 Artemis/x402watch 水分剥离);
- 私有公司 ARR 传闻(以 Sacra/多源交叉,注意 11x 掺水前科);
- "AI influenced GMV"类口径(与 executed 口径差一个数量级);
- Anthropic/OpenAI run-rate 对比(毛收入 vs 净额记收,差 20–30%)。

### 什么变化发生时立刻提高关注级别

- AI agent 买家数单月 +50% 以上且非单一集成驱动 → Watch→Inflection 候选;
- 任何公司披露机器级 P&L → 立即 Structural 评估;
- 大平台 autonomous purchasing 默认开启 → 立即 P0 研究;
- Volume 涨但买家/钱包不涨 → 负面信号,检查集中度。

### 哪些事件值得建立专项研究

Anthropic IPO 招股书;GENIUS 细则落地(2027-01);Arc 主网后 90 天数据(2026-09 起);Amazon v. Perplexity 终审;首个 agent 信用/保险产品;首个机器人自主 OPEX 案例;Waymo 盈利披露;Ramp x402 集成的 90 天留存(2026-11 可判)。

---

## 结语:本报告的三个最终判断

1. **机器经济是真实的,但它的真实部分不在最热的叙事里。** 真实的机器经济 = 数字劳动($150–250 亿/年生态)+ 智能销售($1,000 亿+ run-rate)+ 物理任务收入(数十亿)+ 存在已久的机器交易(量化/电力);最热的链上 agent 叙事 organic 规模只有数万美元/日。
2. **当前所处位置:管道过剩、货物稀缺、货币先行、信用缺位。** 支付/身份/钱包三层基础设施在 12 个月内完成了历史罕见的标准化收敛(且 Web2 巨头全部下场),但流经管道的真实价值与代币估值脱节两个数量级;验收、信用、法律责任三块拼图完全缺失——它们是下一代基础设施的真实创业与投资空间。
3. **投资时钟的正确姿势:用 External Revenue 定规模,用自主性迁移定阶段,用买家构成与留存定真伪,用价值捕获定标的。** 拐点最早会出现在:AI agent 买家数、按结果计费占比、企业自主付款阈值、90 天留存——而不是任何总量 GMV 指标上。

---

*报告数据截止 2026 年 8 月 27 日。所有关键数据均标注[数据值+时间+来源];私有公司数据多为媒体/研究机构估算口径,已在文中注明;链上数据默认提示原始/organic 口径差异。本报告为产业研究,不构成投资建议。*







