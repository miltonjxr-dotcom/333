# NEAR AI 业务与发展研究：从「用户拥有的智能」到机密计算云

> 视角：产业研究员 / 加密与 AI 交叉赛道分析  
> 方法：以官方产品、博客、文档与公开合作为主，辅以第三方报道交叉核验；叙事与可验证事实分开写  
> 撰写时间：2026 年 9 月  
> 覆盖窗口：2024 年 11 月 NEAR AI Research Hub 启动，至 2026 年 8 月 Intel Trust Authority 集成  
> 目标：把 NEAR AI 是什么、卖什么、怎么赚钱、走到哪一步，用尽量少的行话讲清楚

---

## 执行摘要（先说结论）

1. **NEAR AI 不是又一个聊天机器人品牌，也不是 NEAR 公链本身。** 它是 Illia Polosukhin 创办的 AI 研究与产品公司，核心卖点是：**把大模型推理和 AI Agent 放进硬件加密的「保险箱」里跑，并给出可独立核验的证明。** 口号是 *user-owned, verifiable AI*（用户拥有的、可验证的智能）。

2. **它要解决的真实痛点很朴素：企业和个人不敢把最值钱的数据交给 ChatGPT 这类云端模型。** 普通「隐私模式」只是合同承诺；NEAR AI 用 Intel TDX + NVIDIA Confidential Computing，让提示词在使用中也保持加密，连机房运维、GPU 供应商和 NEAR AI 自己都读不到明文。每条请求还能拿到硬件签名的 attestation（证明）。

3. **产品已经从「训练下一个开源大模型」转到「机密推理基础设施」。** 2024 年底他们曾宣布要做 1.4 万亿参数开源模型；到 2025 年底至 2026 年，真正落地的是 NEAR AI Cloud（机密推理云）、Private Chat、IronClaw（安全 Agent 运行时）、Confidential GPU Marketplace、Agent Market，以及用质押 NEAR 换算力额度的计费方式。训练超级模型仍是长期叙事，但当前商业动作集中在 **推理、Agent、合规和企业销售**。

4. **商业模式是「机密版 OpenAI API」叠加「Agent 运行时」和「链上经济」。** 开发者把现有 OpenAI SDK 的 `base_url` 换成 `https://cloud-api.near.ai/v1` 就能用；按 token 付费，也可质押 NEAR 换月度额度。企业侧卖预留 GPU、私有模型、SLA 和本地/VPC 部署。链上侧，Agent Market 用 NEAR Intents 让 Agent 发单、竞价、结算。

5. **客户叙事已经从加密圈扩到浏览器、机器人、企业和政府，但仍处早期商业化。** 已公开的生产或试点对象包括 Brave Nightly、OpenMind、Phala、Venice AI、Abound、Corbits，以及百慕大政府。公司自称这些合作方累计覆盖超 1 亿用户——这是**合作方自身用户规模**，不是 NEAR AI 的付费用户数。2026 年仍在招聘首任销售与商务总监，说明 GTM（go-to-market，走向市场）还在搭骨架。

6. **和 NEAR 公链的关系是「同一愿景下的两层」：** NEAR AI 提供机密智能；NEAR Protocol 提供跨链交易、身份和结算（Intents、Chain Signatures）。Illia 把两者合称为 *unified commerce layer*：资产流动 + Agent 交易共用一层。Intents 手续费回购 NEAR，是协议层面的价值捕获；NEAR AI 云服务则是另一条收入线，尚未看到经审计的独立收入披露。

7. **当前阶段可以概括为：技术栈基本成型、标杆客户开始出现、规模化收入仍待验证。** 最硬的资产是创始人出身（Transformer 论文共同作者）、硬件级机密计算、Intel 独立验证、以及 OpenAI 兼容的落地路径。最大的风险是：机密计算有性能与生态成本、NVIDIA Inception 不是独家战略投资、Agent 市场仍偏演示、以及「用户拥有」最终仍依赖 Intel / NVIDIA 芯片信任根。

---

## 一、先分清三个容易混在一起的名字

读 NEAR AI 之前，先把三个实体分开，后面所有产品才说得通。

| 名字 | 它是什么 | 和用户的关系 |
| --- | --- | --- |
| **NEAR Protocol** | 分片公链，主打账户抽象、跨链 Intents、Chain Signatures | 转账、跨链兑换、Agent 结算发生在这里 |
| **NEAR Foundation** | 支持生态的基金会 | 法务、市场、部分安全与增长资源，公开页面写明「NEAR AI is supported by key contributors from NEAR Foundation」 |
| **NEAR AI** | 独立的 AI 研究、工程与产品公司，官网 [near.ai](https://near.ai/) | 真正卖机密推理、Agent 运行时和相关云服务的主体 |

一句话：**链负责「钱怎么转、意图怎么成交」；NEAR AI 负责「模型怎么在看不见明文的情况下思考和行动」。** 两者共享创始人和叙事，但采购合同、API 密钥和 SLA 面向的是 NEAR AI 这套云产品。

---

## 二、它从哪来：为什么是这个人、这条链在做这件事

### 2.1 创始人背景决定了叙事可信度

Illia Polosukhin 是 2017 年 Google 论文 *Attention Is All You Need* 的共同作者之一。这篇论文提出的 Transformer，是后来 GPT、Claude、Gemini 的共同祖先。他离开 Google 后与人共同创立 NEAR——最初是为了解决区块链的吞吐和可用性，而不是做聊天机器人。

这件事之所以重要，不是因为「名人光环」，而是因为：

- 他对大模型的能力边界和数据饥渴有第一手认识；
- 他同时拥有一条已经上线、能做跨链结算的公链；
- 他把「AI 该被谁拥有」定义成产品原则，而不是营销口号。

公开团队页（[near.ai/company](https://near.ai/company)）显示：创始人 Illia Polosukhin；CPO & GM George Zeng；产品负责人 Sergey Astretsov；AI 负责人 Cameron Dennis；工程负责人 Pierre Le Guen 等。NEAR Foundation 一侧还有产品市场、法务和信息安全负责人作为支持贡献者。2026 年公开招聘过 Sales & Business Development Director，直接向 CCO Matt Kummell 汇报，说明商业化组织仍在从 0 到 1。

### 2.2 2024：先讲「用户拥有的 AI」，再宣布训练超级模型

2024 年 4 月前后，NEAR 宣布成立 NEAR AI 实验室和孵化器，定位 *User-Owned AI*：模型、数据和智能不应被少数闭源公司垄断。WIRED 当时把 Illia 的立场概括为：用开源 + 加密协议，把问责写进技术本身。

2024 年 11 月曼谷 Redacted 大会上，团队更进一步：启动 **NEAR AI Research Hub**，宣称要做约 **1.4 万亿参数** 的开源前沿模型（当时约合 Meta Llama 的 3.4 倍），用竞赛式众包从 5 亿参数模型开始、分七阶段放大。Illia 当时对训练成本的公开口径约 **1.6 亿美元**，设想用代币融资，再用推理收入回报贡献者。

这一阶段的关键判断是：

> 他们最初想同时打「做更大的开源模型」和「用区块链协调训练」。  
> 后来真正跑通、能对外卖的，是第二条路上更落地的分支：**机密推理（private inference）**。

这并不意味着 1.4T 计划被官方宣布取消，但 2025–2026 年的产品发布几乎全部围绕 TEE 推理、Agent 和 GPU 市场，而不是公布该巨型模型的训练进度。对观察者而言，应把它视为**长期研究叙事**，把 Cloud / IronClaw 视为**当前业务**。

### 2.3 2025：把「保险箱芯片」做成基础设施

2025 年 1 月，NEAR AI 与 Phala Network 合作开源了第一块 TEE 基础设施 SDK：用 Intel TDX（CPU 侧隔离虚拟机）和 NVIDIA GPU TEE（GPU 侧机密计算）保护推理过程。目标很明确——先让 Agent 的输入输出可证明是私密的，再谈更复杂的训练与微调。

2025 年 12 月 3 日，**NEAR AI Cloud** 和 **Private Chat** 正式发布。这是从研究原型走到「可以换 URL 就用」的云产品的分水岭。

---

## 三、用大白话讲清它到底在卖什么

### 3.1 今天的 AI，其实是「把日记本交给陌生人保管」

用 ChatGPT、Claude、Gemini 时，你的问题、客户名单、合同草稿、病历摘要，都会以明文或服务商可解密的形式进入对方服务器。对方承诺「不用于训练」「有隐私模式」，但这是**政策与合同**，不是物理隔离。

对企业来说，这意味着：

- 法务和 CISO（首席信息安全官）不敢放行最有价值的数据；
- 自建机房能规避风险，但成本高、周期长（NEAR AI 自己的口径：自建机密计算基础设施约 **500 万美元 + 6 个月** 才能服务第一条请求）；
- 结果是：AI 用在写邮件和做 PPT 上很猛，用在核心业务数据上很慢。

NEAR AI 的生意，就是把这句话变成产品：

> **「你可以像用 OpenAI 一样调用模型，但能证明我（以及机房管理员）都没看见你的数据。」**

### 3.2 TEE：把计算放进硬件保险箱

**TEE（Trusted Execution Environment，可信执行环境）** 可以想成 CPU/GPU 里的一间上锁房间：

1. 你的提示词在自己设备上加密后送进去；
2. 只有房间里的密钥能解开，模型在房间里思考；
3. 答案再加密送出来；
4. 芯片给一张「印章」——attestation quote——证明：这确实是正版 Intel/NVIDIA 硬件、跑的是声明过的代码、内存对外不可读。

NEAR AI Cloud 用的是：

- **Intel TDX**：在 CPU 上做机密虚拟机，宿主机操作系统、hypervisor 都读不到内存；
- **NVIDIA Confidential Computing**：在 GPU 上把推理过程也封起来。

官网把流程写成四步：你加密请求 → 在 TEE 里跑 → 硬件签名证明 → 你自己核验。核验接口示例：`/v1/attestation/report?model={model_name}`。

2026 年 8 月又补了一层：**Intel Trust Authority**。以前「谁运营机器，谁核验证据」，对企业审计来说仍是循环论证；现在证据交给 Intel 的独立验证服务，发出 Intel 签名的 JWT token。信任链从「云厂商自己说了算」挪到「造芯片的那家公司背书」，这对 GDPR、HIPAA、SOC 2 场景更有说服力。

### 3.3 它明确不承诺什么

深入浅出也要说边界：

- TEE **不是**数学上的零知识证明那么强。它依赖芯片厂商的实现、固件和侧信道防护。Intel SGX 历史上就有过侧信道问题；TDX 是更新一代，仍不是「物理上不可能泄露」。
- 「连 NEAR AI 自己都看不见」成立的前提是：密钥在客户端、镜像可复现、attestation 被真正校验。如果调用方不校验证明，隐私就退回「相信供应商」。
- 对闭源前沿模型（OpenAI / Anthropic / Google），NEAR AI 走的是 **TEE 里的安全网关 + 可选 PII 脱敏**，提供的是「隐身模式」：供应商看到请求来自网关，对不上具体用户；这与「模型权重也在 TEE 里、供应商完全零知识」不是同一档保证。开源权重模型（Qwen、DeepSeek、GLM 等）才是完整机密推理。

---

## 四、产品矩阵：一层云，上面挂了五样东西

可以把 NEAR AI 想成一座「机密机房」，上面长出面向不同买家的入口。

```text
                    用户 / 企业 / 政府 / Agent
                               |
          +--------------------+--------------------+
          |                    |                    |
     Private Chat        OpenAI 兼容 API        IronClaw Agent
     (普通人聊天)         (开发者换 URL)         (24/7 助手)
          |                    |                    |
          +--------------------+--------------------+
                               |
                        NEAR AI Cloud
              Intel TDX + NVIDIA GPU TEE + 证明
                               |
              Confidential GPU Marketplace（供给侧）
                               |
                    NEAR 链：Intents / 质押 / 结算
                               |
                         Agent Market
```

### 4.1 NEAR AI Cloud：机密推理云（主产品）

- 定位：给企业、政府和 AI 应用跑敏感推理。
- 兼容：完整对接 OpenAI API 形态，Python / JS 官方 SDK 改 `base_url` 即可。网关为 `https://cloud-api.near.ai/v1`，也可直连某个模型的 TEE 端点以降低延迟。
- 能力：Chat Completions、工具调用、结构化输出、Embeddings、图像、语音转写、Files、Conversations、Web Search 等。
- 性能口径（2025 年 12 月发布会）：额外延迟约 **5–10%**，单租户约 **100 QPS**；支持流式、KV cache、模型常驻。
- 模型：官网页展示约 **52** 个可调用模型，其中约 **12** 个在 TEE 内机密托管。目录以开源权重为主，例如 DeepSeek V4 Flash、GLM 5.x、Kimi K2.6/K3、Qwen 3.x 系列。也提供 Anthropic / OpenAI / Google 的网关路径。
- 价格形态：按 token 的 pay-as-you-go；企业计划含预留容量、私有模型、量价、SLA、本地或 VPC。示例（2026 年 9 月官网页公开价，美元 / 百万 token，会变动）：

| 模型 | 上下文 | 输入 / 输出 |
| --- | --- | --- |
| DeepSeek V4 Flash | 1048K | $0.17 / $0.35 |
| GLM 5.3 Flash | 1048K | $0.075 / $0.25 |
| Qwen 3.6 35B A3B FP8 | 262K | $0.17 / $1.10 |
| Qwen3.8 27B | 262K | $0.44 / $3.30 |
| Kimi K3 | 1048K | $3.30 / $16.50 |

第三方聚合站（llmpricing.dev）同期收录约 37 个标价模型，说明目录在快速膨胀，**报价应以 [cloud.near.ai](https://cloud.near.ai/) 实时目录为准**。

### 4.2 Private Chat：给普通人的「可证明隐私」聊天

入口：[private.near.ai](https://private.near.ai/welcome)（发布稿链接如此）。体验接近 ChatGPT，底层仍是 Cloud 的开源模型 + TEE。场景文案包括情感咨询、理财规划等——即「你最不想被用来训练或泄露的对话」。

这是获客和品牌层，不是主要收入层。它的战略意义是：让「可验证隐私」从白皮书变成一个能点开的产品。

### 4.3 IronClaw：安全优先的 Agent 运行时

2026 年 2 月 23 日 NEARCON 首次推出，2026 年 7 月 27 日发布 **IronClaw 1.0**。官网把它写成：连接你的工具、跑工作流、不用人盯着的 AI Agent；默认安全、开源、面向真实业务。

用大白话：现在满地都是「能帮你订机票、改代码、管邮箱」的 Agent。它们有一个共同弱点——**思考、行动、密钥、上网缠在同一个进程里**。提示词注入成功，密钥就可能被骗走。

IronClaw 的设计是把这团乱麻拆开：

- **决策**（模型）和 **行动**（工具调用）分开，中间有一层他们称为 **guard** 的检查点；
- 凭证放在加密保险库，密钥默认一次性、不进模型上下文；
- 工具在沙箱里跑（官方早期表述是 Wasm；开源实现讨论里还有 gVisor、`network=none`、由宿主机注入 API Key 的 model proxy）；
- 敏感操作要人批准，而不是先做再汇报；
- 状态持续 checkpoint，中断后从断点续跑，而不是整段任务作废；
- CLI、Web、Slack、Telegram 共用同一套记忆和安全规则。

能力口径（官方、同一基座模型 `deepseek-v4-flash`）：

| 基准 | 测什么 | IronClaw 分数 | 官方对比 |
| --- | --- | --- | --- |
| PinchBench | 147 项真实任务（日程、邮件、代码、调研、文件） | 93.5% | 约领先第二名 4 分 |
| ClawBench | 140+ 真实网站上的多步操作（拦截最终提交） | 88.6% | 场均 83.3%，领先第二名约 4.7 分 |
| OfficeQA | Databricks 出品，近百年美国财政公报、约 8.9 万页 | 76.4% | 比 Hermes 约少 12% 错误，比 OpenClaw 约少 15% |

2026 年 5 月与 FailSafe 发布 **AttackBench**：用会自适应的 LLM 攻击手测 Agent 框架。结论是行业通病是「相信工具返回的字段」（field-content trust）；IronClaw 违规最少，写指令类攻击上差距最大。这是**有利于产品的评测**，应视为厂商与合作方数据，不是监管认证。

部署上，NEAR Foundation 和 NEAR AI 内部已全员使用；支持多租户（技能可在组织内共享，管理员默认看不到个人工作区）和单租户完全隔离。2026 年 7 月时，老实例还不能一键升级到 1.0。

试用入口：[agent.near.ai](https://agent.near.ai)

### 4.4 Confidential GPU Marketplace：把闲置 GPU 卖给不敢上公有云的人

同样在 NEARCON 2026 推出。逻辑是双边市场：

- **需方**：金融、医疗、政府等不能把 PHI/PII/涉密数据交给普通公有云（因为运维理论上能看传输中或内存中的数据）；
- **供方**：GPU 机房常有 **30–40%** 空闲，但接不到受监管负载。

Marketplace 让作业在 TEE 加密飞地里执行，主机 OS、GPU 运营商、NEAR AI 都被密码学挡在外面；官方称每条请求 **30 秒内** 返回硬件签名证明。长期路线图叫 **DCML（Decentralized Confidential Machine Learning）**：机密计算从 NEAR 自有机房，扩展成链上协调的去中心化算力网。Illia 在 Bankless 访谈中承认：目前主要还是自有 GPU 冷启动，第三方加入涉及 SLA 和质量问题，市场仍在长出来。

### 4.5 Agent Market：让 Agent 像接私活一样做生意

2026 年 2 月 4 日发布，入口 [market.near.ai](https://market.near.ai)。流程：

1. 你用自然语言发任务（代码审查、调研、买数据集、跑腿取件），带预算；
2. Agent 竞价，资金进托管；
3. 执行后提交交付物和校验哈希，用 NEAR 结算；
4. 有争议则由 dispute agent 裁决。

它把 **NEAR Intents** 从「跨链兑换」扩展到「通用意图」：用户只说要什么结果，协议去匹配执行者。兼容 OpenClaw、Claude、Codex 等框架。这是最接近「Agent 经济」的产品，也是目前**最难用公开数据验证规模**的一层——更像协议实验，而不是已经有 GMV 披露的市场。

---

## 五、商业模式：钱从哪来、NEAR 代币扮演什么角色

### 5.1 三条收入线索

**（1）云推理：按 token 卖机密计算**  
这是最像传统 AI 云的一条。开发者按量付费；企业买预留 GPU、私有模型、合规支持。差异化不在「更聪明的模型」（模型大多是别人的开源权重），而在 **同一调用体验 + 硬件级隐私证明**。

**（2）Agent 托管：按席位/并行 Agent 数卖运行时**  
IronClaw 托管是订阅逻辑。2026 年 7 月起可用质押代替信用卡。

**（3）协议与代币：质押换额度，Intents 吃手续费**  
这是加密原生的一条，把 NEAR 从「链上 Gas」变成「AI 算力预付凭证 + 结算货币」。

### 5.2 质押付费（2026 年 7 月 30 日）

官方把「加密 AI 栈里最中心化的一环」说成是账单：一开云账号就要绑卡。Staking for NEAR AI 的设计是：

- **锁仓 NEAR，不花本金**，换成月度 AI 额度；
- 解除质押，额度停止，本金取回。

两种换算：

| 用途 | 公式（当时政策） | 例子 |
| --- | --- | --- |
| Agent 托管（Starter / Basic / Pro） | 质押量 ÷ 100 = 每月美元额度 | 质押 500 NEAR → 每月 $5 额度；至少 50 NEAR 可在约 30 秒内部署第一个 Agent |
| 机密推理 | 用质押**收益**（本金 × 价格 × APY）换成算力，而不是花掉本金 | 额度按秒累积 |

托管档位以 NEAR 计价，价格波动大时调整区间，让美元等效成本相对稳定。这是产品设计，不是收益率承诺。

### 5.3 和 NEAR 协议经济的咬合

NEAR AI 官方写过：工作负载增长会拉动结算、验证和激励，从而让 **NEAR 成为这朵 AI 云的原生资产**。并行的是协议层 **Intents fee switch**（约 2026 年 2 月打开）：跨链意图交易的手续费用于回购 NEAR。第三方仪表盘在 2026 年 7 月前后出现过累计 Intents 成交额约 230 亿美元、毛手续费约 3800 万美元量级的报道。那是 **NEAR 协议** 的收入，不要直接记成 NEAR AI 公司营收。

正确的叠法是：

- Agent 调用机密模型 → 可能给 Cloud 付费（法币或质押）；
- Agent 跨链换汇、支付、履约 → 走 Intents，协议收手续费、回购 NEAR；
- GPU 供给方未来可能质押/被质押，用收益覆盖托管。

这是一套**自洽的代币叙事**。是否已经形成「AI 推理收入大到能看见」的公司财报，公开信息里还没有。

### 5.4 目标客群与销售动作

招聘启事把早期客户画像写得很清楚：

- 买家：CISO、工程 VP、基础设施负责人、AI/ML 负责人；
- 行业：金融、保险、法律科技、AI 基建、机器人、网络安全；
- 动作：冷启动 outbound、在 Attio 里建 CRM、30–90 天内推动金融/保险/机器人方向的试点。

这说明 2026 年的商业化阶段是：**设计伙伴已经有了，标准化销售机器还在建。**

---

## 六、客户与合作：哪些已经是生产，哪些还是发布会

以下按「可核对的公开表述」分层，避免把 Logo 墙当成收入。

### 6.1 产品设计伙伴 / 生产集成（公司自己点名）

| 对象 | 类型 | 公开要点 | 阅读时要注意 |
| --- | --- | --- | --- |
| **Brave Nightly** | 隐私浏览器实验通道 | Leo 助手增加基于 NVIDIA TEE 的机密选项，早期实验用 DeepSeek V3.1 | 是 **Nightly**，不是全量稳定版 Brave |
| **OpenMind** | 机器人操作系统 | 实时自主系统上的私有推理 | 属垂直场景，不是大众 C 端 |
| **Phala Network** | 机密云 / TEE 合作方 | 从 SDK 到生产负载 | 既是供应商生态，也是客户 |
| **Venice AI** | 消费级隐私 AI | 2026 年 3 月加入可验证加密推理，含 TEE / E2EE 等模式 | 隐私档位分多档，并非所有流量都走 NEAR TEE |
| **Abound** | 企业/金融相关（官方客户墙） | 官方与新闻稿多次并列 | 公开细节少于上述几家 |
| **Corbits** | 团队共享 Agent 工作区 | 2026 年 7 月原生接入私有推理 + IronClaw，动作上链可审计 | 偏企业协作，适合讲合规故事 |
| **百慕大政府** | 公共部门 | 2026 年 5 月 13 日 SALT 论坛宣布；先给公务员做处理敏感公民数据的安全助手 | 是主权 AI 标杆，但是**起步原型**，不是全国系统替换 |

2025 年 12 月发布稿还有一句：**这些平台累计服务全球超过 1 亿消费者与企业用户。** 统计口径是合作方覆盖面（Brave 等本身体量大），用来证明「机密计算扛过了真实流量」，**不能理解成 NEAR AI 月活过亿**。

### 6.2 硬件与标准组织

- **NVIDIA Inception**（2026 年 1 月 13 日）：创业加速项目，给技术支持、工具和 GPU 资源。**不是股权投资，不是独家供应协议。** 对标 ICP、Akash、Bittensor 时，它是「站队 NVIDIA 机密计算路线」的信号，放大解读会失真。
- **Intel Trust Authority**（2026 年 8 月 12 日）：独立 attestation 验证，企业采购故事明显增强。
- 官网自称 Confidential Computing Consortium 成员。

### 6.3 政府叙事为什么被单独强调

百慕大 2018 年就做了较完整的数字资产监管框架，2026 年把同一「先发监管」姿态延伸到公共部门 AI。总理 David Burt 的表态核心是：选 NEAR AI 是因为保护发生在架构层。Illia 的表态是：公务员把个人数据交给 AI 时，基础设施商也不该看见。

对 NEAR AI 来说，政府单子的价值首先是**背书和合规话术**，其次才是合同金额（金额未披露）。

---

## 七、和 NEAR 公链怎么拼成一张图

只看 NEAR AI 会觉得它是「带证明的 GPU 云」；叠上链，才是他们自称的 **Agent 经济操作系统**。

| 组件 | 作用 | 类比 |
| --- | --- | --- |
| NEAR AI Cloud / TEE | Agent 怎么「想」且不泄密 | 脑子 + 保密室 |
| IronClaw | Agent 怎么安全地「动手」 | 手脚 + 门禁 |
| Chain Signatures | 一个 NEAR 账户能签 BTC/ETH 等链上交易 | 万能钥匙，不用传统跨链桥 |
| NEAR Intents | 只说目标，求解器网络去成交 | 把「我要到巴黎」交给旅行社，而不是自己订每段机票 |
| Agent Market | Agent 之间发单、竞价、托管、仲裁 | 自由职业市场 |
| $NEAR | Gas、质押换算力、意图结算、回购 | 电费 + 预付卡 + 股本叙事 |

Illia 在 *The Unified Commerce Layer* 里把 Intents 从 DeFi 扩成「所有商业活动的中立基础设施」：法币、RWA、Agent 用工都可以是一条意图。Agent Market 是这条理论的产品化试点。

对投资或生态研究，需要分开跟踪两组指标：

1. **NEAR AI 业务指标**：机密推理 token 量、付费租户、预留 GPU、IronClaw 部署数、企业续约；
2. **NEAR 协议指标**：Intents 成交额、手续费、回购、活跃账户。

目前公开世界里，第 2 组数据更多；第 1 组几乎只有案例和产品发布。

---

## 八、发展时间线（到 2026 年 8 月）

| 时间 | 事件 | 阶段含义 |
| --- | --- | --- |
| 2017 | Illia 参与 Transformer 论文 | 技术出身 |
| 2018–2023 | 做 NEAR 公链 | 先有结算层，后有 AI 层 |
| 2024 年 4 月前后 | 宣布 NEAR AI 实验室 + 基金会 AI 孵化投资 | 战略转向 User-Owned AI |
| 2024 年 11 月 10 日 | Research Hub；1.4T 开源模型计划；app.near.ai 竞赛 | 研究叙事高峰 |
| 2025 年 1 月 19 日 | 与 Phala 开源 TEE SDK | 基础设施开工 |
| 2025 年 12 月 3 日 | Cloud + Private Chat；Brave Nightly / OpenMind / Phala | **产品化元年** |
| 2026 年 1 月 13 日 | 加入 NVIDIA Inception | 硬件生态站队 |
| 2026 年 2 月 4 日 | Agent Market | 意图从交易走向劳务 |
| 2026 年 2 月 23 日 | NEARCON：IronClaw、GPU Marketplace、多模态 | 全栈首次凑齐 |
| 2026 年 5 月 7 日 | AttackBench（与 FailSafe） | 用安全评测做差异化 |
| 2026 年 5 月 13 日 | 百慕大政府合作 | 公共部门样板 |
| 2026 年 7 月 15 日 | Corbits 集成 | 企业多用户 Agent |
| 2026 年 7 月 27 日 | IronClaw 1.0 + 三项基准领先 | 运行时定版 |
| 2026 年 7 月 30 日 | 质押换 AI 额度 | 账单链上化 |
| 2026 年 8 月 12 日 | Intel Trust Authority | 独立验证闭环 |

2026 年上半年路线图（2025 年 12 月发布会）：多模态模型、探索可携带的私有记忆、继续 DCML。2 月 NEARCON 已宣布文本/图像/语音统一执行环境，以及「完全机密 / 网关匿名」两档隐私。可携带记忆是否大规模上线，截至 2026 年 9 月仍应视为进行中。

---

## 九、竞争格局：它到底在跟谁抢

NEAR AI 同时踩在三条赛道上，对标对象不一样。

### 9.1 机密计算 / 私有推理云

对手包括：各大云的机密虚拟机（Azure Confidential Computing、GCP Confidential VMs、AWS Nitro Enclaves）、Phala、以及各类「隐私 LLM API」。NEAR AI 的差异是：**专门为 LLM 推理封装成 OpenAI 兼容 API + 每请求 attestation +（现在）Intel 独立验证**，而不是让客户自己拼 TEE 集群。

风险：超大规模云厂商一旦把「带证明的模型 API」做成默认选项，垂直创业公司的窗口会变窄。NEAR AI 的反制是开源可审计镜像、以及和链上身份/结算绑死——这只对「本来就在加密或强合规」的客户有粘性。

### 9.2 去中心化 AI 网络

常被放在一起比较的有 Bittensor（激励网络）、Akash（去中心化 GPU 租赁）、ICP（链上托管与计算）、Gensyn / Together 等训练或推理网络。NEAR AI 当前**并不是靠代币挖矿协调十万矿工**，而是自有机密 GPU + 正在打开的供给市场。它打的是「企业买得下手」的合规，不是「最便宜的散户算力」。

### 9.3 Agent 框架与助手

OpenClaw、各类开源 harness、Claude/Codex 生态、以及企业内部 Copilot。IronClaw 选择的战场是 **安全架构和基准分数**，而不是先拼插件数量。Agent Market 则多了一层「能收钱」的协议，这是 Web2 Agent 公司通常没有的。

### 9.4 一句话定位

> 在「模型谁最聪明」上，NEAR AI 不正面硬刚 OpenAI；  
> 在「算力谁最便宜」上，也不硬刚中心化云和纯 DePIN；  
> 它抢的是：**敏感数据终于能进 AI 的那一截——以及 Agent 开始替人持有密钥、转账、调用内部工具时，必须有的那层硬件级隔离。**

---

## 十、长期技术愿景：DCML 和「私人记忆」

官方把 Cloud 写成通往 **Decentralized Confidential Machine Learning** 的一步。完整图景大致是：

1. **现在**：机密推理（inference）。输入输出可证私密。  
2. **下一步**：私有、可携带的记忆（portable memory），让个人或企业的长期上下文跟着用户走，而不是锁在某一家聊天产品里。  
3. **更远**：机密微调 / 协作学习——例如两家医院在互不交出病历的前提下提高模型质量；或数据所有者允许别人的代码在自己硬件上跑，双方都看不见对方的原始数据。  
4. **供给侧**：GPU 市场从 NEAR 自有机房变成多方供给，用质押和 SLA 约束质量。

2024 年的 1.4T 模型竞赛，逻辑上仍可接在「开源前沿模型 + TEE 内可货币化推理」上：模型能赚钱，贡献者才能持续投入。但训练万亿参数模型需要高带宽互联，去中心化训练的工程难度被联合创始人 Alex Skidanov 公开承认过。因此更现实的近两年路径是：**先把推理和 Agent 做成生意，再决定是否自训前沿模型。**

---

## 十一、怎么判断它做得好不好（监测框架）

下面这些比看代币价格更接近业务本身。

**产品与技术**

- 机密模型数量 / 总目录占比是否上升（官网页曾写 12 / 52）；
- 是否默认对每条请求做 attestation，以及 Intel ITA token 是否成为企业合同标配；
- IronClaw 是否出现第三方（非官方基准）安全审计；
- GPU Marketplace 是否公布外部供给方数量和利用率。

**商业化**

- 付费云客户从「Logo」变成可重复的行业案例（金融、保险、法律、政府）；
- Brave 是否从 Nightly 进入稳定版；
- 百慕大是否从公务员助手扩到面向市民的服务；
- 是否披露 ARR、token 消耗量或预留 GPU 规模——目前没有。

**生态与代币（间接）**

- 质押用于 AI 的 NEAR 数量；
- Agent Market 的成交笔数、争议率、重复发单率；
- Intents 成交额中，能归因到 Agent 而非人工交易的比例（现在几乎分不清）。

**风险信号**

- 长期只见发布会、不见续约；
- 自建 GPU 一直转不出去，市场空转；
- 出现 TEE 侧信道或 attestation 实现事故；
- 销售组织迟迟搭不起来，企业试点停在 POC。

---

## 十二、风险、争议与需要保持冷静的地方

1. **叙事领先于收入。** 全栈故事完整，公开财务几乎空白。这在加密 + AI 交叉领域很常见，做研究时要把「产品能演示」和「生意能规模化」分成两件事。  
2. **信任根仍在芯片巨头。** 「用户拥有」在社会意义上成立，在密码学意义上仍信任 Intel / NVIDIA 的硅和固件。ITA 让验证独立了，没有取消这个前提。  
3. **NVIDIA Inception 易被媒体写成「英伟达战略合作」。** 它是创业者计划。  
4. **1.4T 模型与当前产品线之间存在战略漂移。** 不是丑闻，但是观察重点：资源是继续砸训练，还是全部转向推理云。  
5. **Agent 经济的法律与产品都极早。** 「争议由 Agent 裁决、未来取代法庭」是愿景句，监管、责任归属、幻觉导致的错误支付都还没有被市场检验。  
6. **基准测试由项目方发布。** PinchBench / ClawBench / AttackBench 有方法说明，但仍需外部复现。  
7. **「1 亿用户」是生态覆盖，不是 NEAR AI DAU。**  
8. **性能与成本。** 官方称额外延迟 5–10%，对聊天可接受，对高频交易式 Agent 未必。机密 GPU 相对普通推理更贵，企业买的是合规，不是更低的 token 价。  
9. **竞争窗口。** 一旦 OpenAI / Anthropic / 主流云给出可审计的机密推理，NEAR AI 必须靠「开源权重 + 链上结算 + Agent 运行时」这一整包，而不是单靠 TEE 本身。

---

## 十三、深入浅出的总图：如果只记一张关系

把整件事缩成日常生活：

- 你请了一位特别能干的助理（大模型 / IronClaw）；  
- 你把保险柜钥匙、网银 U 盾、客户名单都交给他（Agent 要干活就必须碰秘密）；  
- 普通公司的做法是：助理坐在大厅里办公，保安承诺不偷看；  
- NEAR AI 的做法是：给助理一间上锁的玻璃房，芯片厂商在门上贴封条，你能检查封条是不是原装；  
- 助理出去办事（跨链转账、调用 API）走 NEAR 这条「统一商务层」；  
- 其他助理要接你的私活，去 Agent Market 竞价，用 NEAR 结账。

**今天已经建成的是玻璃房和封条（Cloud + ITA），以及一个比较谨慎的助理骨架（IronClaw）。**  
**正在招商的是更多机房隔间（GPU Marketplace）和助理之间的劳务市场（Agent Market）。**  
**还没被公开数字证明的是：有多少企业愿意为此持续付钱。**

---

## 十四、资料与入口

**官网与产品**

- 公司与产品总览：<https://near.ai/>
- 公司与团队：<https://near.ai/company>
- 机密推理云：<https://cloud.near.ai/>
- 开发文档：<https://docs.near.ai>
- API：<https://docs.near.ai/api> ，网关 `https://cloud-api.near.ai/v1`
- Private Chat：<https://private.near.ai/welcome>
- IronClaw：<https://agent.near.ai>
- Agent Market：<https://market.near.ai>
- NEAR 官方 AI 页：<https://www.near.org/ai>

**按时间排列的关键官方博客**

- 2025-01-19 [Building Next-Gen NEAR AI Infrastructure with TEEs](https://near.ai/blog/building-next-gen-near-ai-infrastructure-with-tees)
- 2025-12-03 [Introducing NEAR AI Cloud & Private Chat](https://near.ai/blog/introducing-near-ai-cloud-private-chat)
- 2026-01-13 [NEAR AI Joins NVIDIA Inception](https://near.ai/blog/near-ai-joins-nvidia-inception-program)
- 2026-02-04 [Introducing NEAR AI Agent Market](https://near.ai/blog/introducing-near-ai-agent-market)
- 2026-02-23 [IronClaw, Confidential GPU Marketplace, Multimodal](https://near.ai/blog/near-ai-launches-ironclaw-confidential-gpu-marketplace-and-multimodal-confidential-inference)
- 2026-05-07 [AttackBench](https://www.near.ai/blog/ai-agents-have-a-security-problem-were-fixing-it)
- 2026-05-13 [Government of Bermuda](https://www.near.ai/blog/government-of-bermuda-ai-powered-public-services)
- 2026-07-15 [Corbits 集成](https://near.ai/blog/corbits-integrates-near-ai)
- 2026-07-27 [IronClaw 1.0](https://near.ai/blog/introducing-ironclaw-1-0)
- 2026-07-30 [Staking for NEAR AI](https://near.ai/blog/staking-for-near-ai)
- 2026-08-12 [Intel Trust Authority](https://near.ai/blog/near-ai-cloud-integrates-intel-trust-authority)

**创始人与战略长文**

- Illia Polosukhin, *The Unified Commerce Layer*：<https://ilblackdragon.substack.com/p/the-unified-commerce-layer>
- Bankless 访谈：NEAR’s New Token Utility and AI Economy

**需要打折阅读的信息**

- 加密媒体对 NVIDIA Inception、价格短线行情的解读；
- 「100 million users」「only purpose-built blockchain for AI」等营销句；
- 2024 年 1.4T 模型的媒体标题（计划，非已交付）。

---

## 附录：术语表

| 术语 | 意思 |
| --- | --- |
| TEE | 芯片里的隔离执行区，运行中的数据对外加密 |
| Attestation | 硬件出具的、可核验的「我是真芯片、跑的是这段代码」证明 |
| TDX | Intel 的机密虚拟机技术 |
| Confidential Computing | 数据在使用中（in use）也保持加密，不只是存盘和传输 |
| DCML | NEAR AI 提出的去中心化机密机器学习路线 |
| OpenAI-compatible | 接口长得像 OpenAI，改 Base URL 就能迁移 |
| IronClaw | NEAR AI 的开源安全 Agent 运行时 |
| NEAR Intents | 用户/Agent 只表达结果，求解器网络负责执行和跨链路由 |
| Chain Signatures | NEAR 账户可为其他链签名，减少传统跨链桥 |
| User-Owned AI | 数据、模型运行和智能代理应被用户控制，而不是平台单方面托管 |

---

*本报告基于 2026 年 9 月可公开核验的网页与报道整理，产品价格、模型目录和客户范围变化很快。涉及投资或采购决策时，应以官方文档、合同和法律意见为准。*
