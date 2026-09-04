# Agent Economy Monitor — 完整方案（供外部审核）

**As-of:** 2026-09-03  
**Audience:** 另一套模型 / 研究员审核本监测框架  
**Status:** 投资研究用操作规范，不是预测、不是 TAM  
**Constraint:** 只使用**免费**数据；Dune 与 Codex 月额度有限，禁止当日更清洗器  
**Repo:** 本文件是独立可读的完整方案。实现细节以同目录其他文档为准。

审核时请先读「0. 要你审什么」，再打分。不要用「再加一张总表」或「直接采用某网站 real%」作为改进建议，除非能说明它如何通过第 3 节的分母测试。

---

## 0. 要你审什么

请对下面六件事给出 **同意 / 反对 / 需改口径**，并指出自相矛盾处：

1. **两个市场、两个分母**（替代 vs 创造）是否应成为加密侧监测的先验？
2. **Service Spend ≠ 质量美元 ≠ T0** 的三层分母是否够硬？ACP「$500 本金 / $1 费」是否被真正挡住？
3. **同层 + 同经济事件 + 同计量单位才能同表**（x402/MPP/L402 一表；OpenAI ACP 是授权不是商务；Virtuals ACP 不进支付表；Gateway 不是第六条链）是否正确？
4. **免费桌**把 Unique Buyers / Repeat 标成 **null**、禁止绿灯，是否过于保守，还是唯一诚实做法？
5. **数据源分工**（日更 JSON vs 周看 Artemis vs 日常 0 次 Dune、黄灯 ≤3、月 IC ≤2）是否浪费了本可免费得到的信息？
6. **投资表达**写成 Potential Expressions / 条件化受益映射（USDC=份额指标；CRCL/COIN=conditional beneficiary；VIRTUAL 仍要 M1 门 / M2 杀）是否仍把监测和荐股混在一起？

请不要审「文笔」或「再做一个全市场 GDP」。任何首页美元都**不能加总成 Agent Economy GDP**。

### 外部审核（2026-09-03）已收，三处硬口径已改

外部审核对上一版六问：**同意 3 / 需改口径 3 / 反对 0**。主方向成立；最大硬伤不是数据少，而是 proxy 被写成真值。本文件已按审核改：

| # | 审核 | 本文件处理 |
| --- | --- | --- |
| 1 两个市场 | **同意** | 保持为**研究分区**，不是两个可直接计算的数字分母 |
| 2 三分法 | **需改口径** | 定义保留（挡住 ACP $500 本金）；免费桌 **Observed Service Spend = null**，禁止 F_sku USD + MPP 笔数 |
| 3 同层同表 | **需改口径** | 原则收紧；OpenAI ACP **只在 Layer 2**；Virtuals ACP 的 job/fee/notional 不同表 |
| 4 Buyers / Repeat = null | **同意** | 保持；`organic_user` 不得填 Unique Buyers |
| 5 日更 / 周看 / Dune | **同意** | 保持额度分层 |
| 6 核心书 USDC/CRCL/COIN | **需改口径** | 降为条件化受益映射；USDC 不是 CRCL/COIN 同性质的资本利得表达 |

已知空洞 7 条审核全部**接受**（F_sku 必须降级为 covered SKU proxy；T3/T4 是目标定义不是当前连续可观测指标）。

---

## 1. 问题与先验

### 1.1 监测目标

不是回答「Agent 火不火」。是尽早抓住**机器支付真实体制变化**，同时不被刷量、memo、铸币、代币反射所呼叫。

四个问题，固定顺序：

1. 独立买家有没有向**具名卖方**支付**可交付物的标价**？
2. 对手方集合是在**变宽**，还是同一集群加转？
3. 链下需求（推理 loop、SDK、新 SKU）有没有同向？
4. 有没有**可投资表达**（轨、稳定币、facilitator、股权），还是只有代币？

(1) 失败 → 忽略。(1) 过 (2) 不过 → 记作运营活动。(1)(2)(3) 过 → 研究事件。价格只确认，不触发。

### 1.2 两个市场

| 市场 | 谁在付钱 | 天花板 | 加密先吃哪块 |
| --- | --- | --- | --- |
| **替代** Substitution | 人让 agent 去买零售/票务 | 现有消费支出 | 规则与授权（AP2/TAP/拒付），不是 x402 笔数 |
| **创造** Creation | 机器买 API / 数据 / 推理 / 别的机器 | 劳动力与 token 成本 | **结算与身份**；本监测偏这一侧 |

封闭花园（支付宝「3 亿笔」、平台内购物助手 GMV）不当开放机器支付。咨询机构 $200B–$5T TAM 分母混乱，只当叙事风险。

### 1.3 Goodhart

支付笔数是被激励的指标：facilitator 补贴 gas、自成交、战役可在一周内打出千万级「agent payments」。

**工作假阳性（必须能挡住）：**

- **2026-08 x402：** 月约 1790 万笔 vs 6–7 月约 480–600 万笔，但仅约 **$43.7 万** 体积（均价约 $0.025）。日笔数 8-30 至 9-02 曾到 120–190 万后回落。→ 战役，最多黄灯。
- **Tempo MPP：** 累计约 4.57 万事件，仅 **384 `Settled`**，独立收款方约 90。监控事件会发明一个不存在的市场。

**法医标尺（数量级，不是日更）：**

| 来源 | 窗口 | 原始 | 调后 / 地板 |
| --- | --- | --- | --- |
| Visa × Artemis | 至 2026-04-21 | 1.783 亿笔 / $1.357 亿 | 1.096 亿笔 / **$1500 万**（约丢掉 89% 美元） |
| Ling et al. arXiv:2607.12575 | Base 280 天 | 1.367 亿笔 / $4410 万 | C1 虚构 ~21%；C2 集群内 ~64%；C3 未归因 ~15%；**具名下限 ~$18.8 万**，上限 ~$2030 万 |

结论：同一市场可以同时有「organic 仍是七成」和「独立具名服务支出六位数」。选网站 = 选分母。

---

## 2. 分层：同层才能同表

### 2.1 功能轴 vs 场所轴

```
功能                              场所
支付协议  x402 / MPP / L402       结算网络  Base / Solana / Tempo / Arc / Lightning
商务编排  Virtuals ACP / UCP / Masumi
身份      ERC-8004 / TAP          批处理    Circle Gateway  ← overlay，不是第六条链
授权      AP2 / OpenAI Agentic Commerce Protocol / Verifiable Intent
```

**同层 + 同经济事件 + 同计量单位，才能同表比较。** 名字撞车不是同行。

- 链和支付协议**平级**，不是父子。x402 跑在 Base **和** Solana；Tempo 上主要是 MPP。
- A2A×x402 是授权层进入 x402 的适配器，不是第四个支付协议。
- Google AP2 / OpenAI **Agentic Commerce Protocol** / Virtuals **ACP** 名字会撞；OpenAI ACP 是结账**授权**（Layer 2），Virtuals ACP 是 job **编排**（Layer 3）。Virtuals 的 completed job / fee / notional 不能因为也叫 ACP 就和授权协议放一起。

### 2.2 Layer 1 支付协议（唯一可日更同表的三人）

| 协议 | 结法 | 资产 | 可比较单位 |
| --- | --- | --- | --- |
| **x402**（Coinbase 孵化，Linux Foundation） | 每请求链上 HTTP 402 | Base/Solana 等上的 USDC | T3/T4 USD，独立收款方 |
| **MPP**（Stripe + Tempo） | 会话/通道，批量 Settled | Tempo USDC + 法币 SPT | **仅 `Settled` USD** 与独立收款方 |
| **L402**（Lightning Labs） | 发票 + macaroon | BTC sats | 已付发票折美元 |

禁止：x402 原始笔数 vs MPP `ChannelOpened` vs L402 challenge 次数。

暂不进表（有 spec、无稳定体量）：s402 / U402 / v402、IETF draft、lobster.cash。

### 2.3 其他层各自一张表

| 层 | 同行 | 单位 |
| --- | --- | --- |
| 0 身份 | ERC-8004、Visa TAP、Mastercard KYA 类 | 后来**付过钱**的可识别 agent，不是 NFT mint（2026-09 注册约 54.9 万，是铸币指标） |
| 2 授权 | AP2 mandate、**OpenAI Agentic Commerce Protocol**（结账 allowance）、Verifiable Intent | 签发 / 撤回 / 执行 |
| 3 商务 | Virtuals ACP、Masumi、UCP。**不含** OpenAI ACP | **完结 job / 放款**，不是 memo（Virtuals 累计 memo 已超 1200 万）。fee ≠ notional |

绿灯只在**层内**（例如 MPP 从 x402 抢 USD 份额）。跨层同时动是旁证，不是加总 GDP。

### 2.4 结算网络 vs Gateway

GMV **只落在最终结算网一次**：Base、Solana、Tempo、Arc（**2026-09-16 公开主网前不当 GMV**）、Lightning。

**Circle Gateway** = 链下聚单、链上净额（EIP-3009 一类）。同一笔可打标 Gateway + Base；表 1 用**列**记「该网 Service Spend 里经 Gateway 净额的 %」，禁止把 Gateway USD 加进 Base，禁止当第六条链。

Polygon / BNB 等：尾部，仅 Service Spend 突然冒头时展开。

---

## 3. 分母：三种美元 + T0–T4

### 3.1 三种经济类型（比「质量美元」更硬）

落笔前必须盖一个戳。盖不上 → 不进表 0。

| 类型 | 含义 | 例子 | 去向 |
| --- | --- | --- | --- |
| **Service Spend** | 机器付了**服务标价** | x402 T3 具名 SKU；MPP 用量 `Settled`；L402 已付发票 | 表 0/1/2，**唯一 GMV** |
| **Principal / notional** | 本金、托管、交易名义 | ACP job 入金 $500 去交易、协议费 $1；agent 钱包 DEX | 表 3 两列：fee vs notional |
| **Plumbing** | 为了以后能付而搬家 | MPP TopUp / 开通道、facilitator 备货、Gateway 对**已入账**支出的净额 | 资金/运维序列，不是 GDP |

Allium `is_agent_economy_circulation`（若将来有账本）= 「别把 ACP 循环当自成交洗掉」。**Circulation ≠ Service Spend。** $500 本金不得进表 0。

### 3.2 x402 质量阶梯（定义，免费桌日更算不出 T3/T4）

| 阶 | 定义 | 用途 |
| --- | --- | --- |
| **T0** | 所有被标成 x402 的 transfer | 战役探测器 |
| **T1** | 去掉自付、零金额、24h 按比例退回；**ACP 流通整表踢出支付 GMV** | 卫生，不是表 0 |
| **T2** | 去掉 facilitator 集群自结、资金同源闭环 | 接近 Visa/Artemis adjusted |
| **T3** | T2 ∩ 活目录具名 origin/category | 具名服务下限 |
| **T4** | T3 ∩ 买家 30d 内 ≥3 个 UTC 日且 ≥5 笔 T3，非 facilitator EOA | 复购地板 |

IC 理想主序列：T4 USD 与 T3 unique payees。广度好：付款方和收款方一起升。集约差：美元升、独立买家降或 top1% 升。

**Visa 通用链上洗量规则（30 天 >1000 笔或 >$1000 万剔地址）禁止套到 x402**，会杀掉合法微支付。

Allium 自己也不打高频买家（那是 x402 正常形态）和 A→B→C 环。故厂商 `NOT is_inorganic` 仍只是 T1。

### 3.3 老板屏口径（定义 vs 免费桌）

| KPI | 有逐笔账本时 | **本桌（免费）必须怎么填** | 量纲 |
| --- | --- | --- | --- |
| **Observed Service Spend** | T3 USD + MPP **usage Settled USD** + L402 paid | **null**。没有账本、MPP 饲料没有 Settled **美元**时禁止填 | USD |
| **x402 covered SKU spend proxy** | （不是 Spend） | F_sku 24h 有类目目录切片。**不是** x402 Service Spend | USD |
| **MPP settled paid events** | （不是 Spend） | `Settled` **笔数**。禁止与 F_sku 美元相加 | count |
| **MPP settled USD** | MPP 用量 Settled 美元 | 饲料给出才填，否则 **null** | USD |
| Paid Tx (quality) | 上述对应笔数 | 有 Observed Spend 才填；否则 F_sku txs 与 Settled **分列** | count |
| Unique Buyers | T3 独立付款方 | **每天 null**。`organic_user` 是残差类 | — |
| Repeat Buyer Rate | T4/T3 | **每天 null** | — |
| Unique Sellers | T3 named | 目录 last_seen 7d、非 placeholder/other、去掉 virtuals/ACP URL | count |

Buyers / Repeat 两个 null 是正常诚实。**Observed Service Spend 也是 null**：表 0 不能叫「真服务支出已测到」。禁止用模型把 null 编成数。禁止把 F_sku 美元与 MPP 笔数加总（量纲错误）。

闸门：Observed Spend、F_sku、MPP Settled 笔数、catalog sellers 都不动 → 只扫表 6。仅 T0 笔数动 → 战役。均价 <$0.05 且笔数暴增 → 战役。F_sku 单类目 ≥50% → covered-SKU 集群，直到抽样。

---

## 4. 周报层级（从大到小）

**总盘（Observed Spend 常为 null + 分列代理）→ 结算网络 + 支付协议（并列）→ 协议×网络 →（有标签才）需求类型 → 商务编排（fee ≠ notional；OpenAI 结账 ACP 不在此表）→ 身份 → 主体 → 规则**

下层仅在上层动了、或每周 10 分钟扫描时打开。同行 = 同层 + 同经济事件 + 同单位。

| 表 | 问题 | 行 | 列 / 规则 |
| --- | --- | --- | --- |
| 0 | 真服务支出有没有动 | — | Observed Spend **null**；F_sku USD 与 MPP 笔数分列；Buyers/Repeat **null** |
| 1 | 钱落在哪条最终结算网 | Base / Solana / Tempo / Arc / Lightning | Service Spend、份额、sellers、WoW；**Gateway % 是列** |
| 2 | 信封换了没 | x402 / MPP / L402 | Spend、份额、质量 Paid Tx、Buyers、Repeat、Sellers |
| 2×1 | 交叉 | 单元格 | x402×Base vs Solana；MPP≈Tempo |
| 2b | 增量买了什么 | Inference / Data / Compute / Other API / Unknown | 仅表 0 动且有标签；Unknown 下降才是信号 |
| 3 | 完结生意 | Virtuals ACP、Masumi | job 数、**fee**、**notional**、对手方。丢 memo。`VIRTUAL` 仅完结单动才碰 |
| 4 | 身份 | 8004 等 | 带支付证明的反馈；mint 不进会 |
| 5 | 谁在赚钱 | facilitator / top payee | 不是第一屏 |
| 6 | 规则日历 | 事件 | Arc 2026-09-16、AP2 撤回、拒付归因、公约 |

---

## 5. 免费桌数据栈（硬约束）

### 5.1 原则

**买不起账本。白嫖已发布提取。自己只做解释。不建 402 索引。Codex 不当清洗器。**

日更 $0。Dune：日 0 次；无黄灯周 0 次；月 IC ≤2；黄灯升级 ≤3。禁止重跑 agenteconomy 已付费的 `queryId`（7895747、7881006、6731879、7881007、7881124、7881008、7931767、6166650）。OpenRouter Data API 不日打（与推理共用额度）。x402watch HTTP 60 次/时，日更改读 GitHub CC0。

### 5.2 日更（脚本已实现）

| 作业 | 读什么 | 产出 |
| --- | --- | --- |
| `scripts/tripwire.py` | `https://agenteconomy.to/data.json` | T0 笔数 z、均价塌缩、MPP Settled/事件、ACP memo vs senders。**只许黄灯** |
| `scripts/free_quality_panel.py` | 同上 + `printmoneylab/x402watch-data` | `observed_service_spend_usd: null`、covered-SKU proxy（F_sku）、MPP Settled 笔数、`mpp_settled_usd: null`、7d named sellers。T3/T4 **null**。`quality_available: false` |
| `scripts/weekly_pack.py` | 上两源 + npm + x402-list | **自动填表 0**（markdown）。Artemis / rankings 仍人工。Dune=0 |

禁止从 F1 或 T0 回填 T3。快照合同：`schemas/daily_quality_snapshot.schema.json`。

### 5.3 周看（不日爬、无 JSON dump 的不进脚本）

| 源 | URL | 岗位 |
| --- | --- | --- |
| **Artemis Agentic Payments** | https://www.artemis.ai/sectors/agentic-payments | **调后第一屏**：Real vs Gamed、MPP 支付类型、x402 类目/链/facilitator。Visa 同族启发式。无公开 dump。禁止引用「x402+MPP 合计笔数」。兄弟页 `/asset/x402` 可能 502，**先打开本页** |
| Visa×Artemis 研报 | Visa PDF | keep-rate 校准 |
| x402scan（Merit） | https://www.x402scan.com | 目录 + 原始 30d；API 常 402 |
| Bazaar | CDP discovery API | 具名目录 |
| x402-list | `/api/v1/facilitators` CC BY 4.0 | facilitator **USDC settler 下限**，自称非全市场；Virtuals settler 累计可到数百万，ACP 形态 |
| npm `x402` | 下载量 | 开发者漏斗 |
| OpenRouter rankings | 页面 | 推理旁证 |

### 5.4 明确不收

再开 Dune 仪表盘（与 JSON 同族 T0；facilitator 名录会过期）、x402.org 静态 30 天（曾核实为写死 HTML）、DefiLlama x402 当 GMV（还标成 DEX volume）、发行人统计（BlockRun 可占索引笔数 80%+）、付费探针、Allium、8004 铸币浏览器、另一个也叫 x402scan 的 MCP 包装。

### 5.5 权威按问题，不按网站名气

| 问题 | 第一源 | 永不 |
| --- | --- | --- |
| T0 爆了没 | agenteconomy 均价+笔数 | x402.org 静态 30d |
| 调后美元动了没 | Artemis sector 页 | 把 Dune+scan+list 加总 |
| 钱买了什么 | x402watch 24h 类目 | facilitator 体积 |
| 谁收租 | x402-list settler | T0 笔数份额 |
| 卖方是否活 | Bazaar + scan + HTTP **402=活** | 8004 mint |
| 独立具名 Service Spend | **没有日更公开序列** | 任何首页总数 |

三家都从 facilitator 白名单长出来的数 = **一次测量被转载**。

### 5.6 2026-09-03 同日对照（说明分母，不作目标）

| 镜头 | 规模 |
| --- | --- |
| agenteconomy 累计 | 1.81 亿笔 / $4160 万 |
| 2026-08 T0 | 1790 万笔 / $43.7 万 |
| x402scan 30d | 2495 万笔 / $144 万（BlockRun ~1589 万笔 / $20.7 万） |
| x402watch 30d「real」 | $70.9 万 |
| x402-list 仅 Coinbase settler 30d | $66.1 万 |
| DefiLlama 30d / 累计 | $111 万 / $3290 万 |
| Visa 调后累计（4 月快照） | $1500 万 |
| 论文具名下限 | ~$18.8 万 |

agenteconomy 同一 JSON 里 USDC 占比 98.46% 的分母只有 **4.7 万笔**（Base + 活 facilitator 名录），对比 8 月 T0 1790 万笔 → **范围错误**，不是美元垄断证据。

---

## 6. 如何审计网站清洗（不信 real%）

证据梯：链上抽样 > 目录 HTTP 402 > 战役回测 > 法医数量级 > 跨源不一致 > 厂商 real%。

`scripts/audit_cleaners.py` 2026-09-03 免费跑分（Dune=0）：

| 检查 | 结果 |
| --- | --- |
| MPP 单位 | **过**：Settled 384 / 事件 45688 |
| T0 战役可见 | **过**：8 月笔数 3×，均价 $0.040→$0.025 |
| USDC 份额范围 | **失败**（见上） |
| x402watch 峰值是否跟笔数 | **过**：8-26 的 30d real $53.5 万→$39.4 万，未跟 3× 笔数 |
| x402watch 标签稳定 | **失败**：8-26 至 8-31 wash $9.9 万→$47，real $39 万→$67 万（改标签） |
| 松紧 vs 法医 | **失败**：keep ~87% vs Visa ~11% vs 具名 ~0.4% |
| organic_user | **失败**：占买家 97.7%，不能当 Unique Buyers |
| 24h SKU 集中 | **警告**：token_data 占 F_sku 77%（$325 里 $251） |
| 目录存活 | **过**：抽样 URL 中 HTTP 402 算活着 |

结论：agenteconomy 当 T0/MPP **饲料及格**；x402watch 能挡一点笔数刷量，**当 GMV 不及格**。Artemis 是周看调后方向，方法不透明，仍非 T3。

月度可选 1 条窄 Dune：7 天、一条链、前 20 收款地址，手标 named/ACP/自付。不要让 Codex 给 3 万 endpoint 打标。

---

## 7. 警报与绿灯

黄灯 = 绊线（15 分钟）。绿灯 = 研究事件。

**免费桌：日更脚本禁止发绿灯。** 绿灯需要 ≤3 条 Dune 的逐笔抽样 + 下列 2-of-3，且至少一票来自结算或市场，不是价格：

1. 质量：T4 USD 7d z≥2 或 T3/T2 美元份额跳 ≥10pp  
2. 广度：T3 payees z≥1.5 且 payers 不降，top1% 不升  
3. 旁证：OpenRouter cli-agent z≥2，或 ≥3 个新具名 origin 活过 72h，或 MPP Settled payees +30% **且** T3 也升  

硬否决：T0 笔数 ≥2× 而 T2 USD <+20%；新量 >50% 来自一个 facilitator 且买家 <20 EOA；代币篮子 +30% 而 T3/T4 不动；目录存活下降。

黄灯例子：T0 z≥3；均价腰斩且笔数升；MPP 事件 ≫ Settled；ACP memo 翻倍 senders 不动；F_sku 单类 ≥50%。

稳定 ID 见 `config/alert_rules.yaml`（S1 需求脉冲、S5 洗量陷阱、C1 链轮转必须用质量美元份额、M2 memo 剧场等）。

---

## 8. 节奏与升级

| 时钟 | 谁 | 做什么 |
| --- | --- | --- |
| 每日 UTC 06:30 | 脚本 | tripwire + free_quality_panel；Dune=0；Codex=0 |
| 本地 08:00 15 分钟 | 分析师 | 读黄灯与 F_sku；杀 S5 |
| 每周 45 分钟 | PM+分析师 | 表 0 代理、Artemis sector、scan 30d vs T0、list facilitator、npm、rankings |
| 每月 | IC | 论题；`audit_cleaners.py`；可选 ≤2 Dune |
| 黄灯升级 | 分析师 | ≤3 Dune 后停 |
| 事件 | 任何人 | L 序列（授权撤回、归因拒付、错买判决、Arc 主网、L5 谁持钥） |

升级 SOP：T+0 分类战役 vs 真脉冲；T+4h SKU 与聚类；T+24h 选**一个**表达；T+72h 两页备忘录（变了什么、质量、能否在停止补贴 gas 后存活、表达与仓位、**杀死条件**）。无表达则记「看到了，不可投」。

---

## 9. 潜在表达 / 条件化受益映射（监测下游，不是输入，不是核心书）

监测顺序不变：先判断真实支付 → 广度 → 链下需求 → **最后**才问有没有可投资表达。下面不是预设仓位。没有表达是允许的结果。

| 若质量门过了… | 候选受益 | 不是这个 | 杀死 / 不要当核心 |
| --- | --- | --- | --- |
| Base 上具名 SKU Service Spend（S1） | COIN、CRCL — **conditional beneficiary** | 随机 agent ERC-20 | 没有 S1 就不要从 T0 做 Circle/Coinbase 研究 |
| C1：质量美元份额（不是笔数份额）翻到 Solana | SOL — **conditional** | 日笔数翻转 | 只看笔数的「Solana flip」 |
| 质量机器支付的 USDC 占比 | **份额指标**，不是 long-USDC 资本利得袖 | Circle 全链上体积 | USDC ≠ CRCL/COIN 同性质表达 |
| Facilitator 分成 / HHI（S6） | 该主体的代币/股权（若有） | 「x402 协议币」 | 旧 facilitator 的马甲 |
| Virtuals **完结 job + 对手方变宽**（M1） | `VIRTUAL`，小仓 | 所有 VIRTUAL 配对 agent 币 | **M2 memo 剧场** 或 senders 30d 不动 |
| L1–L4 规则 / 替代 | V、MA、持牌 PSP、保险 | 链上 beta | — |

TAO/VVV 跟推理旁证，不是支付轨。不要把 VIRTUAL 配对的长尾 agent 币当监测输入。

L5：钱在谁钱包里决定谁赔。AWS AgentCore 等产品把钱包留在 Coinbase/Stripe Privy 一侧是结构事实，需盯「谁持钥」变更（L6）。

---

## 10. 论题作废（90 天）

- T4 30d <$5 万且 T3 payees 30d <50（需求从未离开运营集群）— 免费桌用「长期只有战役形态 + 抽样仍无名卖方」作为代理杀死条件  
- 永远只有 T0 能被做成增长曲线  
- T2 仍全是 facilitator 内部  
- 替代侧用积分/闭园吃掉微支付，公共结算变成实现细节  
- 大 L5（AWS/Stripe/Coinbase）链下净额，链上 402 无剩余租金  

---

## 11. 已知空洞（请审核人重点打）

1. **没有日更 T3/T4。** 免费桌 Observed Spend / Buyers / Repeat 为 null。若你认为必须日更复购，请给出**不烧 Dune、不建索引**的算法，否则应同意 null。  
2. **F_sku 覆盖窄。** 只能称 **covered SKU proxy**，绝不能代表 x402 Service Spend。2026-09-03 24h 仅约 $325，且 77% 在 token_data，与 T0 月 $43.7 万、scan 30d $144 万不可比。  
3. **Artemis 不可机读。** 周看依赖人工读图；与 F_sku 对不上时没有自动和解。不能因为写了 Real/Gamed 就自动升级成 T3。  
4. **Gateway % 目前无免费序列。** Schema 可留，当前值 **null**。不能为了填表找另一个近似 USD 比例。  
5. **ACP fee vs notional** 规范有，公开 JSON 仍主要是 memo/senders。只能监控活动度，不能声称已看到 ACP 真实经济规模。  
6. **绿灯在免费桌几乎发不出来** — 这是设计，不是 bug。False negative > false positive。若你认为应放绿灯，请说明用哪一分母。  
7. Allium SQL 仅作 T3 定义存档，**不调度**。因此 **T3/T4 是目标定义，不是当前连续可观测指标。**

---

## 12. 仓库地图

| 路径 | 内容 |
| --- | --- |
| `docs/agent-economy-monitoring-playbook.md` | 论题、T0–T4、警报、SOP |
| `docs/weekly-cascade.md` | 周报层级 |
| `docs/protocol-layer.md` | 同层看板 |
| `docs/data-cleaning.md` | 免费清洗政策 |
| `docs/source-landscape.md` | 网站普查 keep/ignore |
| `docs/cleaner-audit.md` | 清洗审计方法 |
| `config/quota.yaml` `sources.yaml` `alert_rules.yaml` `watchlist.yaml` | 配额、源岗位、阈值、条件化表达（不是核心书） |
| `scripts/tripwire.py` `free_quality_panel.py` `weekly_pack.py` `audit_cleaners.py` | 日黄灯、F 代理、周表 0 自动填、月审计 |
| `sql/optional_paid_allium_x402_quality_panel.sql` | 付费账本定义，不跑 |
| `schemas/daily_quality_snapshot.schema.json` | 日快照 |

---

## 13. 给审核 AI 的最短复述

本方案监测**创造侧机器结算质量**，不监测「AI 购物」叙事。GMV 只允许 **Service Spend**；本金和 plumbing 分列。免费桌 **Observed Service Spend = null**；F_sku 只是 covered SKU proxy；MPP Settled 在没有美元时只报笔数，二者不得相加。支付协议只有 x402 / MPP `Settled` / L402。OpenAI Agentic Commerce Protocol 是 **Layer 2 结账授权**；Virtuals ACP 是 Layer 3 商务编排；Gateway 是叠加不是第六条链。同表要求：同层 + 同经济事件 + 同单位。质量阶梯 T0–T4 是**目标定义**，不是当前连续可观测指标。运行约束为免费：日更只消费 agenteconomy JSON 与 x402watch CC0；周看 Artemis sector 页；Dune 日常 0 次、黄灯 ≤3、月 IC ≤2。网站 `real%` 不是准确度。老板屏 Buyers / Repeat 强制 null。投资侧是 **Potential Expressions / 条件化受益映射**，不是核心书 USDC/CRCL/COIN。任何把首页美元加总成 Agent Economy GDP 的改法，视为审核失败。
