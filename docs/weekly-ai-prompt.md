# 每周丢给 AI 的固定提示词（复制下面「提示词」整段）

自动化引擎是 **本仓库 Python**，不是 Dune，不是 Codex。  
Dune 很方便，但方便的是**看别人已经跑完的图**；每周自己点 Run 会烧额度，并容易把未清洗笔数当成采用。

适合：Cursor Agent / 任何能跑终端或能 `curl` 的模型。每周触发一次，把输出存成周记即可。

---

## 提示词（从这里复制到文末）

```
你是 agent economy 免费桌的周更助手。目标不是估算「Agent 经济 GDP」，而是：这周像不像刷量、洗过之后的支付有没有变方向、要不要开研究。

仓库在当前工作区。按顺序做，不要发挥。

1) 跑自动化（必须）：
   python3 scripts/weekly_pack.py
   把完整 markdown 贴进回复。不要改格子里的 null。不要把 F_sku 美元和 MPP Settled 笔数相加。不要把任何首页美元写成 Service Spend。

2) 人工页（你有浏览器就打开并各写一句「升/平/降」；没有浏览器就列出 URL 让我看）：
   - https://www.artemis.ai/sectors/agentic-payments
     只看 Real vs Gamed（不要引用 x402+MPP 合计笔数）、链份额、MPP 是否在 Settled 而不是开通道。这不是 T3。
   - https://openrouter.ai/rankings
     agent/推理用量是否同向。
   - 可选：https://www.x402scan.com 30d 原始目录是否和 T0 笔数对得上。

3) 只准输出下面五句周记（可附在脚本表后面）。第 4 句默认不要写成「开研究」。
   1. 像不像刷量：
   2. 洗过后的支付方向（Artemis Real）：
   3. 链下同向（npm 已在脚本里；OpenRouter）：
   4. 本周决策：忽略 / 记运营活动 / 开研究
   5. 仓位：无
   没有「具名服务在卖、且对手方变多」之前，第 5 句必须是「无」。

4) Dune（默认禁止）：
   不要执行任何 Dune SQL，不要刷新仪表盘，不要重跑这些 queryId：
   7895747, 7881006, 6731879, 7881007, 7881124, 7881008, 7931767, 6166650
   这些已经被 https://agenteconomy.to/data.json 公开发布。再跑是重复付费。
   只有第 4 句是「开研究」、且脚本黄灯 + Artemis 对不上时，才允许最多 3 条窄查询，主题只能是「近 7 天谁在收钱」，跑完停止。不准做成每周仪表盘。

5) Codex / 大模型清洗：禁止给服务目录打标，禁止编造 T3 美元。你只解释脚本和页面，不生产新 GMV。
```

---

## Dune 怎么「方便」地用（推荐）

每周：打开已经跑好的公共结果，**不要点 Run**。

- 数据已经在 `agenteconomy.to/data.json`（脚本在读）
- 洗过的方向在 Artemis 那一页

只有 AI 周记写了「开研究」时，你自己在 Dune 里新建一次性查询，例如「某链、近 7 天、按收款地址汇总 USDC，取 top 20」。那是抽检，不是周更。仓库里的 `sql/optional_paid_allium_x402_quality_panel.sql` 是付费账本定义，**不要**拿到 Dune 当每周作业。

---

## 没有本仓库时

仍可让 AI `curl`：

- `https://agenteconomy.to/data.json`
- `https://raw.githubusercontent.com/printmoneylab/x402watch-data/main/data/` 下当天的 `category-benchmarks-YYYY-MM-DD.json`

口径规则不变：Spend / 买家 / 复购保持空；笔数不当采用。
