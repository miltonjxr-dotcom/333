# BlockRun 一周用户追踪

**窗口**：2026-08-28 → 2026-09-04  
**问题**：调用 BlockRun 的是谁、买什么、是不是真 Agent、会不会留下。  
**不是**：把 PayAI 百万笔当成「百万用户」。

---

## 1. 先立口径

观察两个入口，不要混：

| 入口 | 链 / facilitator | 为什么必须看 |
| --- | --- | --- |
| `sol.blockrun.ai` | Solana · PayAI + Figment | PayAI 笔数的 ~99% 来自这里 |
| `blockrun.ai` | Base · 主要 Coinbase | 买家更多（30 日约 383 vs Solana 约 45），用来对照「是不是只有农场」 |

**一笔「用户」= 一个付款地址（payer），不是一次 HTTP 请求。**  
x402scan 的 Buyer / Server 在 Solana 上会标反，每天第一件事是核对：这个地址是收款还是付款。判断：USDC 余额是否被扫走、是否与 BlockRun treasury 相同、对手方是分散还是单一。

---

## 2. 每天采什么（15 分钟）

跑 `python3 blockrun-tracking/snapshot.py`，再用浏览器/WebFetch 补 x402scan 页面数字（站点是前端渲染，脚本拿不到表）。

写入当日 `snapshots/YYYY-MM-DD.json`，缺的字段标 `null`，不要用总量笔数填洞。

| 字段 | 来源 | 用来干什么 |
| --- | --- | --- |
| PayAI last24h / last7d 笔数 | `facilitator.payai.network/discovery/stats` | 分母 |
| `sol.blockrun.ai` 24h 笔数、金额、买家数 | x402scan server 页 | 分子、集中度 |
| `blockrun.ai` Base 同上 | x402scan | 对照 |
| PayAI 24h 买家数 / 卖家数 | x402scan facilitator/payAI | 是不是「一户打满」 |
| Top 10 payer：地址、24h 笔数、金额、对手方数 | x402scan buyers + Solana RPC | 画像原料 |
| 新地址 vs 昨天已出现 | 自建地址表 | 留存 |
| 主 endpoint（chat vs 其它） | x402scan resources / BlockRun 文档 | 买的是什么 |
| 顶流钱包：账户年龄、USDC、SOL、签名间隔、失败率 | Solana RPC | 人 / 脚本 / 基础设施 |

**不要采**：ERC-8004 注册、x402 原始累计、PayAI 自己的 `50K+` 分桶（已证明和链上日百万笔冲突）。

---

## 3. 地址怎么分类（每天打标签）

每个进入 Top 20 的付款地址，只打一类：

| 标签 | 判据 | 画像含义 |
| --- | --- | --- |
| **基础设施 / 网关** | 秒级连发、对手方=1、余额接近 0 或即时扫走、14 分钟内上万笔 | 不是「用户」，是 router / loadgen / 商户热钱包 |
| **脚本农场** | 多地址同模式、同金额、同 endpoint、互相转 gas | 激励或压测 |
| **终端 Agent** | 中低频、chat completions、有间隔、余额够付几天、或同时打 Nansen/其它 API | 真需求候选 |
| **一次性试用** | 生涯 <20 笔、之后不再出现 | 集成测试 |
| **无法判定** | 数据不够 | 保持未知 |

打完后算四个数（每天都算，不要等周末）：

1. **Top1 笔数占比**、Top5 占比  
2. **买家数**（Solana / Base 分开）  
3. **D1 留存**：昨天出现的地址今天是否还在  
4. **客单** = volume / tx（Solana 当前约 $0.011）

---

## 4. 一周要证伪的假设

今天（2026-08-28）已经看到的事实，当先验，用 7 天打：

| ID | 假设 | 怎样算成立 | 怎样算被打脸 |
| --- | --- | --- | --- |
| H1 | Solana BlockRun 是极少数机器钱包，不是用户群 | 30 日买家维持几十个；Top1>70% 笔数 | 买家数上到数百且 Top1<30% |
| H2 | PayAI 日笔数 ≈ BlockRun Solana | 占比持续 ≥90% | 占比掉到 50% 以下且买家变分散 |
| H3 | 付费 SKU 仍是 chat completions | 能观测到的调用里 chat ≥90% | 图/搜索/预测占到可观份额 |
| H4 | Base 比 Solana 更「像人」 | Base 买家数稳定高于 Solana 一个数量级、客单更高或更散 | 两边 Gini 一样高 |
| H5 | 顶流地址是基础设施不是消费者 | 持续秒级连发、余额空、无其它消费 | 出现稳定日活、多服务采购、可解释的任务节奏 |

---

## 5. 第七天交什么（用户画像）

不要写成「AI Agent 在买推理」。按标签出 3–4 张卡片，每张必须有人数、笔数占比、金额占比、留存、一个代表地址：

1. **基础设施层**（网关/热钱包/压测）  
2. **高频脚本**  
3. **终端使用**（若存在；没有就写「本周未观测到」）  
4. **一次性**

另附一张对照：Solana vs Base。结论只允许三种：真需求 / 压测与路由 / 数据不足。

---

## 6. 执行

- 每日：跑脚本 + 补 x402scan 数字 + 给 Top 地址打标签 + commit  
- 第 7 日：写 `persona-week1.md`，停掉日报  
- 本目录 `snapshots/` 是唯一原始记录；`log.md` 只记异常（买家数跳变、新的第二名、PayAI 占比下滑）
