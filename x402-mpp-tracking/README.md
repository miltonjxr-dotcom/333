# x402 + MPP 周度群体追踪

**问题**：每周在 x402 和 MPP 上付钱的，主要是哪些群体。  
**不是**：把两轨 GMV 加总，也不是把百万笔当成百万用户。

BlockRun 日报（`blockrun-tracking/`，08-28 → 09-04）继续单独跑。本包是**全轨道、周频、看人**；那边是**一个商户、日频、看集中度**。不要互相覆盖。

---

## 1. 先立口径

观察三条轨，数字永远分列，禁止相加。

| 轨 | 单位 | 公开窗口 | 看不见什么 |
| --- | --- | --- | --- |
| **A. x402 原始结算** | 笔数、USDC、$、buyer/seller 地址 | x402scan、PayAI `discovery/stats` | 人 vs Agent；organic |
| **B. x402 洗后目录** | 买家标签、品类 $、real volume % | x402watch API（免费 landing / wash-report / categories） | Solana BlockRun 火枪（日约百万笔 / 约 $2 万，几乎不进这本目录） |
| **C. Tempo MPP** | 通道事件、payer/payee 地址 | `agenteconomy.to/data.json` → `tempoMpp` | 美元；Stripe 卡 / SPT 链下 session |

**一笔「用户」= 一个付款地址（或一条 MPP session），不是一次 HTTP 请求。**

三条轨回答的不是同一个「谁」：

| 分母 | 2026-08-28 基线在说什么 |
| --- | --- |
| **按笔数** | x402 ≈ Solana BlockRun 基础设施 / loadgen（PayAI 24h 笔数约 99% 来自 `sol.blockrun.ai`，买家个位数） |
| **按金额（原始结算）** | 仍是 BlockRun 量级（24h 约 $2 万），客单约 $0.011 |
| **按独立买家（洗后目录）** | x402watch 30 日活跃买家 11,475，其中 `organic_user` 10,798（约 94%），`ai_agent` 仅 190 |
| **按洗后目录的 $ / 笔** | 目录 24h 只有约 **$377 / 7,084 笔**——搜索品类笔数里 `ai_agent` 可到 95%，和「买家数 94% 是人」同时成立 |
| **MPP** | 累计 1,849 payer / 90 payee / 45,320 事件；**近 7 日只有 133 事件、每天 1–5 个 payer**。`Settled` 累计仅 384（<1%） |

所以每周必须交**三句话**，缺一句就算没做完：

1. 按笔数，主要群体是谁  
2. 按金额，主要群体是谁  
3. 按独立付款方，主要群体是谁  

x402watch 的 `organic_user` 默认标签 =「没触发更强信号」，不是 KYC 过人。`ai_agent` = 多服务、金额变异、活跃 ≥7 天的启发式，会把「人开的多服务钱包」和真 LLM 买家混在一起。

---

## 2. 群体怎么分

先用 x402watch 的 9 标签（已经在跑，不要另造一套），再映射到研究报告里的经济角色。同一地址在不同服务上可以不同标签；全局标签是 tx 加权多数。

| 经济角色 | 操作标签 | 怎么认 | 算不算「真需求」 |
| --- | --- | --- | --- |
| 基础设施 / 网关 / loadgen | `infra_gateway`（自打，x402watch 常漏） | 秒级连发、对手方≈1、余额被扫光、BlockRun / Figment 火枪 | 否。是路由或压测 |
| 有机人类 H2M | `organic_user` | 默认；单服务、金额散、不像农场 | 候选。要看复购和客单 |
| AI Agent 买家 | `ai_agent` | ≥4 品类、≥5 卖家、金额 CV>0.3、活跃≥7 天 | 候选。仍可能是人的热钱包 |
| 数据 API 采购 | 品类：`token_data` / `wallet_analytics` / `financial_data` / `nft_data` | 跟第三章「机器买数据」 | 高价值候选 |
| 搜索 / 工具 API | 品类：`search_engine` / `ai_search` / `ai_inference` | Exa 一类无 key 按次 | 形状对，看留存 |
| 开发者压测 | `developer` / `self_test` / `owner_test` | 单服务爆发、14 天内、或商户自测白名单 | 否 |
| 刷量 / 激励 | `suspected_wash`；PING；单买家亚分循环 | 同金额、同窗启动、vanity 簇 | 否 |
| 爬虫 / 目录 | `verifier` / `analytics_bot` | 周期拉取、1–5 个服务 | 弱。是计量不是买家 |
| 交易所热钱包 | `exchange_user` | 标签白名单 | 中转，不是终端 |
| MPP 开通道不结算 | `mpp_session_only` | `ChannelOpened`/`Closed` 远大于 `Settled`/`TopUp` | 集成测试候选 |
| MPP 真结算 | `mpp_settled` | `Settled` 或有 USD 披露 | 真需求候选 |
| 双轨用户 | `dual_rail` | 同一地址或同一产品本周同时出现在 x402 与 Tempo | 领先信号 |

**禁止**：用 x402watch 的买家数去解释 PayAI 的百万笔；用 MPP 事件数去对 x402 的美元。

---

## 3. 每周五采什么（约 45 分钟）

定时：UTC 周五 10:00（`x402-mpp-weekly-cohorts`）。先跑脚本，再补 JS 渲染的页面。

```bash
python3 x402-mpp-tracking/snapshot.py
```

写入 `snapshots/YYYY-MM-DD.json`。缺字段留 `null`，不要用另一轨的数字填洞。

| 字段 | 来源 | 用来干什么 |
| --- | --- | --- |
| PayAI 24h / 7d 笔数 | `facilitator.payai.network/discovery/stats` | 原始结算分母 |
| x402scan：PayAI / Coinbase / Figment 24h 笔数、$、买家、卖家 | x402scan facilitator 页（前端渲染） | 集中度；BlockRun 占比 |
| `sol.blockrun.ai` / `blockrun.ai` 24h | x402scan server 页；可复用当日 `blockrun-tracking` 快照 | 火枪是否还在 |
| x402watch landing-stats | `GET /api/v1/landing-stats` | 活跃买家、real volume % |
| x402watch 30 日标签 | `GET /api/v1/wash-report` → `label_distribution` | **独立买家**构成（主表） |
| x402watch 品类 24h | `GET /api/v1/categories` | **金额 / 笔数**构成；注意品类标签份额 ≠ 全局买家份额 |
| Tempo MPP | `agenteconomy.to/data.json` → `tempoMpp` | 事件类型、近 7 日 payer/payee |
| Stripe / MPP 商户披露 | 新闻、Stripe blog、Tempo 官方 | 链下轨有没有露头 |
| 双轨重叠 | 手工：本周 x402 顶流服务名 vs MPP payee | 有没有人同时用两根管子 |

**不要采**：ERC-8004 注册、mppscan.com 头条（注册噪音，不与 Tempo RPC 的 4 万事件混用）、PayAI 的 `50K+` 分桶、x402 原始累计终身笔数。

抄一份 `week-template.md` → `week-YYYY-MM-DD.md`，填完三句话再 commit。

---

## 4. 记分卡（每周都填，不要等月末）

x402：

1. **买家数构成**（wash-report 30 日）：`organic_user` / `ai_agent` / `developer`+`self_test` / 其它  
2. **金额构成**（categories 24h 与 7 日均值）：Top 5 品类 $ 份额 + 该品类 `real_volume_pct` + 该品类标签份额  
3. **原始结算集中度**：PayAI 笔数里 BlockRun 估计占比；PayAI 24h 独立买家数  
4. **W7 留存**：本周 wash-report 活跃买家 vs 上周快照（能对上地址再算；对不上就只记 `ai_agent` 人数和 `organic_user` 人数的周环比）  
5. **客单分裂**：BlockRun 客单 vs x402watch 目录客单（后者 = `total_volume_24h / total_tx_24h`）

MPP：

1. 近 7 日事件合计、日均 payer、日均 payee（不要用累计 1,849 假装本周有这么多人）  
2. `Settled+TopUp` / 总事件  
3. 累计 payer 周增量（本周累计 − 上周累计）  
4. Stripe 链下：有披露写数字，没有写「未见」

对照：

- x402watch 目录 24h $  vs  x402scan 原始 24h $（量级差多少倍）  
- 本周是否出现 `dual_rail`

---

## 5. 每周要盯的假设

| ID | 假设 | 怎样算还成立 | 怎样算被打脸 |
| --- | --- | --- | --- |
| W1 | x402 **笔数**仍是基础设施，不是用户群 | PayAI 24h 买家 ≪ 笔数；BlockRun 占比 ≥80% | 买家数上到数百+且 BlockRun 占比 <50% |
| W2 | x402 **独立买家**仍是 H2M | `organic_user` ≥90% 的 30 日买家；`ai_agent` 仍是数百量级 | `ai_agent` 数量级跳到数千且 7 周留存不塌 |
| W3 | 洗后目录的真 $ 仍是数据/搜索，不是聊天火枪 | Top $ 品类落在 token_data / search / analytics；chat/loadgen 不进目录 | 目录 $ 突然被单一测试品类或 PING 占满 |
| W4 | 目录里「按笔数的 Agent」≠「按人数的 Agent」 | search 等品类标签份额 `ai_agent` ≫ 全局买家份额 | 两者收敛（要么人都变成多服务，要么搜索也变成人） |
| W5 | MPP 本周仍是通道生命周期，不是结算市场 | `Settled` 份额 <5%；近 7 日日均 payer 个位数 | Settled 连续两周抬升，或 Stripe 披露真实商户 session |
| W6 | 两轨用户基本不重叠 | 找不到 dual_rail | 同一产品或地址稳定出现在两边 |

异动定级沿用全景报告：volume 涨但买家不涨 = 集中度或刷量，标 **负信号**。单一集成脉冲（Ramp、PING、BlockRun 新枪）标 **Watch**，不要升级成拐点。

---

## 6. 交什么

每周五一份 `week-YYYY-MM-DD.md`，正文不超过一页：

- 三句话（笔数 / 金额 / 独立付款方），x402 与 MPP 分开写  
- 记分卡数字（从上节抄，不要叙述化）  
- 相对上周：哪个群体在长、哪个在死  
- 诚实缺数：Stripe 链下、内部 A2A、真 Agent vs 人开的钱包、x402watch 是否仍漏掉 BlockRun

不要写「AI Agent 在买推理」，除非品类 `ai_inference` 的 $ 和买家同时能对上。

---

## 7. 和别的追踪的关系

| 包 | 频率 | 回答 |
| --- | --- | --- |
| `blockrun-tracking/` | 日 | 这一个商户的枪是谁在打 |
| **本包** | 周 | x402 全市场 + Tempo MPP，群体是否从基础设施换成 H2M / Agent / 数据采购 |
| 二次收敛第五章 | 季度回顾 | organic 日 $、Agent 买家数量级、Stripe 披露 |

本包不改研究稿章节。数字进这里；只有连续 ≥3 周同向、且不是单商户脉冲，才考虑回写二次收敛的监测句。
