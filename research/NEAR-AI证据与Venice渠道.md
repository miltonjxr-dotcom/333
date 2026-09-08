# NEAR AI 发展得怎样：只采信可核对证据

> 问题：AI 方向实际进展如何？客户与合作有哪些**可独立核验**的材料？Venice 作为渠道客户具体怎么运转？  
> 原则：合作方自己域名上的公告 > 母公司/政府官网 > 双方联名稿里对方高管的直接引语 > NEAR 单方面博客。没有公开的收入、调用量和付费席位。  
> 日期：2026 年 9 月

---

## 先给判断（避免被 Logo 墙带跑）

**产品是真的，生意规模几乎不可见。** Cloud API、文档、模型目录、attestation 接口都在线上；Brave、Venice 在**自己的官网**写了正在用 NEAR AI 的 TEE。这比「加密项目发一篇合作稿」硬得多。

**但几乎没有任何可审计的业务数字：** 没有 ARR、没有机密推理的 token 量、没有付费租户数、没有 IronClaw 生产部署数、没有 GPU 市场成交量。所谓「1 亿用户」是合作方（尤其是 Brave 浏览器）自己的覆盖面，不是跑在 NEAR TEE 里的人数。

**进展 locates 在「设计伙伴 + 试点 + 可选功能」阶段，不是规模化收入阶段。** 最硬的生产集成是 Brave Nightly 里的一个实验模型和 Venice Pro 里的 TEE/E2EE 档；企业/政府多为试点或论坛宣布。百慕大政府官网写的是 **NEAR Foundation 的养老金计算器试点 / 公共服务基础设施伙伴**，措辞比 NEAR AI 自己的新闻稿更窄、更谨慎。

---

## 一、证据怎么分级（后面表格都按这个读）

| 等级 | 含义 | 怎么用 |
| --- | --- | --- |
| **A. 对方官网** | 合作方自己的域名，不经过 NEAR | 最高。可以当作「对方承认在用或在试」 |
| **B. 对方母公司 / 政府 / 正式通讯稿** | 如泰晤士报、gov.bm、PR Newswire | 高。承认合作存在；细节仍可能是宣传 |
| **C. NEAR 博客里的对方引语** | 有姓名职务，但原文在 near.ai | 中。通常经授权，但范围、是否生产以对方域名为准 |
| **D. 仅 NEAR 叙述** | 无对方域名对应页 | 低。当叙事，不当业绩 |
| **E. 媒体转述** | 加密媒体、二手综述 | 只作线索，数字不采信，除非能回溯到 A/B |

**至今没有的（因此不能用来判断「生意大不大」）：**

- NEAR AI 公司收入、毛利、付费客户数
- 机密推理 token / QPS 的独立仪表盘
- 质押用于 AI 的 NEAR 数量
- 合同金额（对比：百慕大把 Paradise Mobile 的数字化合同 **207 万美元** 登在政府公报上，NEAR 相关项没有同等公示）
- Intel.com / NVIDIA.com 上点名 NEAR AI 的产品级新闻稿（NVIDIA Inception 是创业者计划，不是供应合同）

可独立打开的产品层证据（证明「东西在」而不是「卖了多少」）：

- 云：<https://cloud.near.ai/>（公开价目、OpenAI 兼容网关）
- 文档：<https://docs.near.ai>
- 证明接口（NEAR 文档）：`/v1/attestation/report?model={model_name}`
- IronClaw 开源仓库：<https://github.com/nearai/ironclaw/>

---

## 二、合作方一张表（按可信度，不按宣传热度）

### A 级：对方自己的网站写了 NEAR AI

#### 1. Brave（浏览器 Leo）— 最硬的生产向集成

| 项 | 内容 |
| --- | --- |
| 对方原文 | [brave.com/blog/browser-ai-tee/](https://brave.com/blog/browser-ai-tee/)（2025-11-20） |
| 署名 | 隐私研究员 Ali Shahin Shamsabadi；创始人兼 CEO **Brendan Eich** |
| 对方怎么写 | Leo 用 **NEAR AI 的 NVIDIA TEE** 做可验证隐私；用户可选带标签的 DeepSeek V3.1；Brave 代为校验 attestation，界面显示绿色已验证 |
| 范围（对方原话） | **仅 Brave Nightly**（测试/开发通道），**仅 DeepSeek V3.1**，供早期实验；「计划根据反馈扩展到更多模型」 |
| 尚未发生（对方原话） | 全量稳定版；用户在浏览器内自己复验全链路；他们还在评估 TEE 的性能开销 |
| 不能推出的结论 | 不能把 Brave 数千万～上亿级安装量算成 NEAR 的 AI 用户。Nightly 是很小的子集，TEE 又只是 Leo 里的一个模型选项 |

这是目前**唯一**同时满足「对方顶级域名 + 写明 NEAR AI + 写明已向用户提供开关」的消费级案例。它证明集成真实，也证明仍是实验通道。

#### 2. Venice AI — 明确把 NEAR AI Cloud 列为 TEE 供应商之一

| 项 | 内容 |
| --- | --- |
| 对方原文 | [venice.ai/privacy](https://venice.ai/privacy)；[venice.ai/blog/venice-launches-end-to-end-encrypted-ai](https://venice.ai/blog/venice-launches-end-to-end-encrypted-ai)（2026-03-18） |
| 对方怎么写 | TEE / E2EE 推理跑在外部伙伴的硬件飞地里，**「currently NEAR AI Cloud and Phala Network」**；Pro 功能；文末链到 `docs.near.ai` |
| 范围 | 不是 Venice 的默认模式。默认是 Anonymous / Private。TEE 与 E2EE 要 **Venice Pro** |
| 供应商结构 | **双源**：NEAR AI Cloud **和** Phala，不是独家 |
| 模型（对方列出、同时支持 TEE 与 E2EE） | Venice Uncensored 1.1、GLM 5 / 4.7 / 4.7 Flash、Qwen3.5 122B、Qwen3 30B、Qwen3 VL、Gemma 3 27B、GPT OSS 20B/120B、Qwen 2.5 7B 等开源权重。**不是** Anonymous 档里的 GPT/Claude 闭源前沿模型 |
| 创始人引语 | Erik Voorhees 在 NEAR 博客（C 级载体）称 NEAR 的机密推理让 Venice 的理念「可密码学验证」 |

Venice 自己的隐私页甚至有 FAQ 标题 *Who are the TEE & E2EE model providers?*——产品结构上，NEAR 是**批发算力的两家里的一家**。第二节专门拆这条链路。

#### 3. Phala Network — 既是共建方，也是 Venice 的另一家 TEE 供应商

| 项 | 内容 |
| --- | --- |
| 对方原文 | [phala.com/posts/venice-ai-phala-tee-verifiable-private-ai](https://phala.com/posts/venice-ai-phala-tee-verifiable-private-ai) |
| 对方怎么写 | Venice 的 TEE/E2EE **跑在 Phala 的机密计算网络上**；用 dstack 编排 |
| 与 NEAR 的关系 | 2025-01 NEAR 博客：与 Phala **合作开源 TEE SDK**，供 NEAR AI Hub / Cloud 使用。这是**基础设施共建**，不是「Phala 向 NEAR Cloud 买推理」的客户关系 |
| 注意 | NEAR 2025-12 把 Phala 和 Brave、OpenMind 并列成「live customers」。Phala 自己的 Venice 稿并不说自己是 NEAR Cloud 的买家。更干净的表述：**同行 + 早期技术伙伴 + 在 Venice 上的竞合供给** |

### B 级：政府官网 / 母公司新闻 / 正式通讯稿

#### 4. 百慕大政府 — 有官网，但比 NEAR 稿更窄

三份 **gov.bm** 一手材料，不要混成「政府已全面上线 NEAR AI」：

| 时间 | 政府原文 | 实际承诺 |
| --- | --- | --- |
| 2025-05-08 | [Premier 会见 Near AI](https://www.gov.bm/articles/premier-burt-meets-global-finance-and-technology-leaders-digital-finance-forum) | **会谈**：探讨 AI 与数字身份，支持政务与旅游工具。不是合同 |
| NearCon 访旧金山之后 | [NearCon 成果](https://www.gov.bm/articles/premier-highlights-outcomes-nearcon-visit-san-francisco) | 与 **NEAR Foundation** 开始 **试点**：给公务员用的**养老金计算聊天机器人**；若成功再考虑税务门户 |
| 2026-05-29 议会陈述 | [Advancing Digital Finance](https://www.gov.bm/articles/advancing-digital-finance-bermuda) | 论坛宣布之一：「**The NEAR Foundation announced support for Bermuda as an infrastructure partner for AI-powered public services.**」一句，无金额、无系统名、无上线日期 |

对比 NEAR AI 自己 2026-05-13 的稿（SALT 论坛）：写的是公务员处理**敏感公民数据**的安全助手，模型跑在 NEAR AI Cloud，并引总理 Burt 与 Illia 的话。这些**细节没有出现在上述 gov.bm 文本里**。

另：百慕大真正公示金额的数字化主合同是 Paradise Mobile（Google Cloud / Abacus），公报 [GN01072026](https://www.gov.bm/theofficialgazette/notices/gn01072026) 约 **207 万美元**（2025-12 至 2027-12）。**没有找到同等格式的 NEAR AI 采购公示。**

结论：百慕大与 NEAR 生态的关系是**官方承认的试点 / 论坛层面的基础设施伙伴**，不是已披露预算的全国系统替换。

#### 5. Abound（泰晤士报集团）— 母公司报纸 + 通讯稿承认合作，产品是「发布/分阶段」，不是已公布的交易量

| 项 | 内容 |
| --- | --- |
| 对方侧 | [Times of India 2026-04-07](https://timesofindia.indiatimes.com/business/india-business/abound-launches-ai-financial-autopilot-for-nris-in-partnership-with-near-ai/articleshow/130090515.cms)；PR Newswire / Morningstar 转载 2026-04-06 |
| 对方怎么写 | Abound 发布 AI Financial Autopilot，**与 NEAR AI 合作**；用 **IronClaw**，动作可验证、可追溯；CEO Nishkaam Mehta 直接引语 |
| Abound 自己的用户数字（在这些稿里） | 超 **80 万** NRI 用户；汇款量稿件间不一致（30 万 vs 50 万美元级，原文即有 $300M / $500M 两种写法）——这是 **Abound 存量业务**，不是 Autopilot 已经经手的金额 |
| 状态 | 「launch / unveiled / full rollout planned for April 6」+ Fintech Times 写 **phased**（先智能汇款）。没有独立数据证明有多少用户真正让 Agent 自动汇款 |
| NEAR 侧补充（C） | IronClaw 托管 + 经印度 Account Aggregator 连银行；NEAR 管 Agent 托管和推理，Abound 管 UX 和客户 |

这是目前**最像「企业渠道客户」的金融案例**，证据等级低于 Brave/Venice（没有 abound 产品域名上的技术文档被检索到），但高于纯加密媒体。

### C 级：主要出现在 NEAR 博客

#### 6. OpenMind（机器人 OS）

- NEAR 稿引 CEO Jan Liphardt；并有免责声明：**Illia 个人是 OpenMind 的投资人**。
- 公开的 [docs.openmind.org](https://docs.openmind.org/) 检索中**未出现** NEAR AI / TEE 集成页。
- 因此：合作宣布存在，**生产是否已打进默认机器人镜像，无法从对方文档确认。** 利益关系需要打折阅读。

#### 7. Corbits（团队 Agent 工作区）

- 仅见 NEAR 2026-07-15 博客「集成已 live」。未找到 corbits 官方域名上的对应长文。
- 加密媒体写过「11.5 万 agents」之类数字，**未回溯到 Corbits 或 NEAR 的一手报表**，本文不采用。

### D 级：不要当成客户

| 名字 | 实际是什么 |
| --- | --- |
| NVIDIA Inception | 创业加速计划（工具/GPU 资源），非独家、非股权 |
| Intel Trust Authority | NEAR Cloud **调用 Intel 的独立验证 SaaS**。Intel 官网列举的 CSP 集成是 Azure / GCP / IBM 等；**未找到 intel.com 点名 NEAR 的新闻稿**。技术上合理，公关上是 NEAR 单方面宣布「接上了 Intel 的产品」 |
| 「100 million users」 | NEAR 2025-12 稿：Brave 等平台**累计服务**超 1 亿。统计的是合作方体量 |

---

## 三、用这些证据，AI 方向「到底怎么样」

把宣传翻译成可辩护的状态：

**1. 技术交付：中等偏强，且可点开。**  
从 2025 年 1 月与 Phala 的 SDK，到 12 月 Cloud 上线，到 2026 年 IronClaw、质押付费、接 Intel ITA，产品节奏是连续的。Brave 工程师愿意写进官方博客，说明 attestation 链路至少过了另一家安全向公司的审查。

**2. 商业化：早期，且数字空窗。**  
2026 年仍在招第一任销售总监（公开招聘）。已证实的「钱从用户口袋进 NEAR AI」路径，公开可见的是：Cloud 按 token 标价、Venice Pro 可能间接贡献推理费、质押换额度。**没有任何一张表告诉你这些路径加起来有多大。**

**3. 客户质量：有品牌、缺用量。**  
Brave、Venice、泰晤士报系 Abound、百慕大政府——品牌很好看。但 Brave 是 Nightly 单模型；Venice 是付费档的可选模式且与 Phala 分流；Abound 是刚发布的 Autopilot；百慕大是养老金机器人试点 + 一句论坛宣布。这是**标杆狩猎成功、规模化未证明**。

**4. 和公链 AI 叙事不要混账。**  
Intents 成交额、手续费回购是 **NEAR Protocol** 的公开叙事，不是 NEAR AI Cloud 的发票。研究 AI 生意时，应要求「机密推理 / Agent 托管」自己的数字；目前没有。

**5. 和 2024 年 1.4T 开源大模型计划。**  
那是研究叙事。2025–2026 可核对的交付全部是推理与 Agent。没有对方或第三方证实该巨型模型已训成。

一句话：**AI 方向在「把机密推理做成别人愿意写进官网的功能」上是往前走的；在「这已经是一门很大的生意」上，公开证据不够支撑。**

---

## 四、Venice 作为渠道客户：仔细拆

「渠道客户」在这里的意思不是 Venice 给 NEAR 拉代理商，而是：

> **Venice 面向人卖隐私 AI；当用户点选「可验证隐私」档时，Venice 把推理请求转发给 NEAR AI Cloud（或 Phala）这个批发商。**  
> 终端用户感觉自己在用 Venice，不一定知道底层 GPU 在谁家。NEAR 吃的是这一档的推理账单，不是 Venice 的全部 DAU，也不是 VVV 的市值。

### 4.1 角色分工

```text
用户（聊天、图像、API）
        │
        │  只看到 venice.ai / App
        ▼
┌─────────────────────────────────────┐
│ Venice                              │
│ · 账号、Pro 订阅、VVV/DIEM 额度     │
│ · 对话存在用户设备                  │
│ · 代理转发、选模型、四档隐私 UI     │
│ · 审查策略、目录、客服              │
└─────────────────────────────────────┘
        │
        │  仅当模型档 = TEE 或 E2EE
        ▼
   ┌────┴────┐
   ▼         ▼
NEAR AI    Phala
Cloud      机密网络
（飞地推理）（飞地推理）
```

Venice 官方：[privacy 页](https://venice.ai/privacy) 写死了「external TEE partners (**NEAR AI Cloud and Phala Network**)」。  
Phala 官方：[自己的稿](https://phala.com/posts/venice-ai-phala-tee-verifiable-private-ai) 说 Venice 的 TEE/E2EE **跑在 Phala 网络上**。  
NEAR 官方：2026-03-19 稿宣布与 Venice 集成，引 Voorhees。

三方对「Venice 在卖可验证隐私、算力外包」没有矛盾。矛盾点只有营销口径：每家都容易让人以为自己是唯一底座。**一手材料是双源。**

### 4.2 四档隐私里，NEAR 只出现在后两档

Venice 自己画的光谱（原文结构）：

| 档 | 谁默认能用 | 提示词在谁那里明文出现 | NEAR 在不在链路里 |
| --- | --- | --- | --- |
| **Anonymous** | 全体 | 闭源实验室（GPT/Claude/Gemini 等）看得见内容；Venice 藏身份 | **不在。** 这是传统代理 |
| **Private**（默认） | 全体 | Venice 自有 GPU 或零保留伙伴，靠合同 | **通常不在。** 这是 Venice 自己的私有/ZDR 推理 |
| **TEE** | **Pro** | 只在飞地内解密；请求仍过 Venice 代理（故能保留搜索、记忆等） | **在，或在 Phala** |
| **E2EE** | **Pro** | 设备上加密，过 Venice 时仍是密文，只在飞地打开 | **在，或在 Phala**；功能更少（无搜索/记忆） |

所以：

- Venice 的**大部分会话**（Anonymous 用最强闭源模型，Private 用自家/ZDR）**根本不经过 NEAR**。
- NEAR 只在用户愿意付 Pro、并主动选 TEE/E2EE 开源模型时进场。
- 即便进场，还要和 Phala **分流**。公开材料没有「NEAR 占 TEE 流量百分之几」。

这和超市进货很像：Venice 是店；货架上大部分商品来自别的厂家（OpenAI 等、Venice 自己的机房）；NEAR 和 Phala 是「有机认证专柜」的两个供货商。专柜可以很有品牌价值，占销售额的比例完全是另一件事——而那一比例**没有披露**。

### 4.3 一次 TEE / E2EE 请求实际经过哪

按 Venice 博客 + NEAR 文档能核对的步骤：

**TEE 档（功能完整、隐私次强）**

1. 用户在 Venice 选带 TEE 标记的模型。  
2. 提示词经 TLS 到 Venice 代理（Venice 说不落盘；你仍须信任代理这一跳）。  
3. Venice 把作业调度到 NEAR 或 Phala 的飞地。  
4. 飞地内解密、推理、再加密返回。  
5. 附带 attestation；Venice 在回复旁给验证图标。  
6. NEAR 文档允许调用方到 Intel/NVIDIA 服务核验。

**E2EE 档（隐私最强、功能最残）**

1. 浏览器里先加密。  
2. Venice 代理看到的是密文。  
3. 只在 NEAR 或 Phala 的飞地里解密。  
4. 因此 Venice 不能做需要看见明文的搜索、记忆。  
5. NEAR 文档链：`docs.near.ai/cloud/guides/e2ee-chat-completions`。

对 NEAR 来说，这正是 Cloud 的设计用法：**不拥有消费者品牌，只当可证明的推理后端。**

### 4.4 钱和代币怎么走（能说清的部分）

- 用户付给 **Venice**：Pro 订阅，和/或质押 VVV 铸 DIEM 拿每日 API 额度。这是 Venice 的账。  
- Venice 作为开发者，应再向 **NEAR Cloud / Phala** 按推理付费（按 token 或合约价）。**单价、是否包月、NEAR 在双源里的份额，均未公开。**  
- **VVV 涨跌 ≠ NEAR AI 收入。** 代币是 Venice 的准入/额度层；NEAR 是底层 GPU。把 VVV 市值算进 NEAR AI 生意是账户错误。

### 4.5 对「渠道」两个字的准确理解

| 说对了 | 说错了 |
| --- | --- |
| Venice 是 NEAR Cloud 的**应用层分发** | Venice 所有用户都在用 NEAR |
| 对方官网点名 NEAR AI Cloud | NEAR 是 Venice 唯一 TEE 供应商 |
| 证明「有人愿意把可验证隐私做成付费功能」 | 已证明这条渠道贡献了可观收入 |
| 开源模型的机密托管有真实出口 | 闭源 GPT/Claude 的流量也进了 NEAR 飞地（Anonymous 档明确不进） |

和 Brave 对比更能看清渠道类型：

- **Brave**：浏览器厂商在自己的助手里接 NEAR，用户甚至可能没听过 Venice；渠道是 **Leo 的一个模型开关**，免费实验，Nightly。  
- **Venice**：隐私 AI 品牌把 NEAR 做成 **Pro 的升级档**，和 Phala 并列，面向愿意为更强隐私付钱的人。

Brave 证明「安全公司认技术」；Venice 证明「有消费产品把技术标成 SKU」。两者都还不是「用量报表」。

---

## 五、若你要自己跟进，只盯这些可核对动作

比看 NEAR 再发一篇稿更有信息量：

1. Brave 是否把 TEE 从 Nightly 做到 Release，模型是否超过 DeepSeek 一个。看 [brave.com/blog](https://brave.com/blog/)。  
2. Venice privacy 页是否仍写 NEAR **and** Phala；Pro 是否变成默认。看 [venice.ai/privacy](https://venice.ai/privacy)。  
3. 百慕大是否出现 **PATI 合同金额** 或议会陈述里的系统上线，而不是论坛一句。看 gov.bm。  
4. Abound / TOI 是否报道 Autopilot **使用数据**（自动汇款笔数），而不是再发一次发布会。  
5. NEAR 是否首次披露 Cloud 的 token 或付费租户——至今没有。  
6. OpenMind 文档是否出现 NEAR 端点——至今没有。

---

## 关键一手链接

- Brave：<https://brave.com/blog/browser-ai-tee/>  
- Venice 隐私架构：<https://venice.ai/privacy>  
- Venice TEE/E2EE 发布：<https://venice.ai/blog/venice-launches-end-to-end-encrypted-ai>  
- Phala × Venice：<https://phala.com/posts/venice-ai-phala-tee-verifiable-private-ai>  
- 百慕大 NearCon 试点：<https://www.gov.bm/articles/premier-highlights-outcomes-nearcon-visit-san-francisco>  
- 百慕大 2026-05-29 议会：<https://www.gov.bm/articles/advancing-digital-finance-bermuda>  
- 百慕大数字化主合同（对照用）：<https://www.gov.bm/theofficialgazette/notices/gn01072026>  
- 泰晤士报 / Abound：<https://timesofindia.indiatimes.com/business/india-business/abound-launches-ai-financial-autopilot-for-nris-in-partnership-with-near-ai/articleshow/130090515.cms>  
- NEAR × Venice（C 级）：<https://www.near.ai/blog/near-ai-launches-ironclaw-confidential-gpu-marketplace>  
- NEAR Cloud 产品页：<https://cloud.near.ai/>
