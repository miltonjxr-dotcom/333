# Machine Economy：推特上已有的优质内容

不是原创分析。只收录能持续产出、且能把洗量和真实机器支付分开的账号与帖子。

## 优先跟的账号

| 账号 | 为什么跟 |
|------|----------|
| [@OnchainLu](https://x.com/OnchainLu) Lucas Shin | 这条线的数据源头。Artemis 时期做 x402 洗量过滤，现在 Merit Systems。几乎所有“真实 vs 刷量”数字都从他流出。 |
| [@nlevine19](https://x.com/nlevine19) Noah Levine, a16z crypto | 用他的数字，不用他的叙事。把 Bloomberg $24M 压到洗量后 $1.6M；headless merchant 这个说法也是他的。 |
| [@jeff_weinstein](https://x.com/jeff_weinstein) Stripe | 机器支付产品负责人。x402 接入 Stripe、MPP 发布都从这里出。协议方，不是数据方。 |
| [@CoinbaseDev](https://x.com/CoinbaseDev) | x402 协议官方。看产品发布，不要当成交证据。 |
| [@merit_systems](https://x.com/merit_systems) | x402scan / AgentCash。OnchainLu 现在在这里。 |
| [@cuysheffield](https://x.com/cuysheffield) Visa | Visa CLI 接 x402/MPP 商户。卡网络怎么进机器支付。 |
| [@lookx402](https://x.com/lookx402) | Base 上 x402 异常告警（巨鲸、连刷、集中度）。现场观察，不是研报。 |
| [@flovia402](https://x.com/flovia402) | 给 API 卖家看：agent 从哪来、哪条支付轨有留存。Stripe MPP 比赛第一。 |

## 值得读的帖（按时间）

1. **x402 协议发布** — [@CoinbaseDev, 2025-05-06](https://x.com/CoinbaseDev/status/1919784224170889696)  
   HTTP 402 变成稳定币支付层。起点，不是现状。

2. **x402 Bazaar** — [@CoinbaseDev, 2025-09-09](https://x.com/CoinbaseDev/status/1965445897489428869)  
   机器怎么发现可付费 API。他们自己把这叫 machine economy 的 bootstrap。

3. **x402scan 上线** — [@merit_systems, 2025-10-09](https://x.com/merit_systems/status/1976324182062530935)  
   后来几乎所有链上统计都从这里取。

4. **2025-12 全量普查** — [@bc1beat, 2026-01](https://x.com/bc1beat/status/2007180567436255725)  
   6300 万笔 / $7.5M；引用 Artemis：47% 笔数是刷榜，只占金额 14%。报告：[blockrun.ai](https://blockrun.ai/state-x402-2025.pdf)

5. **Stripe 机器支付** — [@jeff_weinstein, 2026-02-10](https://x.com/jeff_weinstein/status/2021331763960873058)  
   为什么 agent 用不了虚拟卡：微额、24/7、HTTP 原生、最终性。MPP 后续也从他发出。

6. **agentic commerce 地图** — [@OnchainLu, 2026-02-18](https://x.com/OnchainLu/status/2024217641729032475)  
   当时的项目盘点，提交本身也走 x402（$1）。

7. **本周可付费 agent 服务** — [@OnchainLu](https://x.com/OnchainLu/status/2079236172078100900)  
   他现在的日常形态：只列 pay-per-use、能当场调的端点。看现场供给，不看估值。

8. **Cloudflare / Linux Foundation** — [@0xJeff, 2026-08](https://x.com/0xJeff/status/2084887484631302174)  
   标准已经出 CT、进 Linux Foundation；需求仍小、基础设施超前。这句判断和 Artemis 数据一致。

## 长文（不在推特，但是同一批人写的）

- Lucas Shin, [Machine Economy 2030](https://research.artemis.ai/p/machine-economy-2030) — 洗量后的真实图
- a16z, [The honest number behind AI agent payments](https://a16zcrypto.com/posts/article/ai-agent-payments-honest-number/) — 从 @nlevine19 的帖长出来的
- Tokenized Ep.83, [The Headless Merchant Economy](https://newsletter.tokenizedpod.com/p/ep-83-the-headless-merchant-economy) — @nlevine19 + @cuysheffield
