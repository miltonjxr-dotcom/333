# 如何链上查准 ERC-8004

**问题**：现在 8004 到底有多少、有没有在用。  
**不是**：把 24 条链的注册数加总，当成「五十万个 Agent」。

全景稿里的 50.9 万 / 质量分层约 1,793，来自仪表盘（agenteconomy / Dune `7881124`，截至 2026-08-26）。那是**电话簿行数**，不是经济活动。链上要自己数，而且要分三张表。

---

## 1. 先立口径

8004 是三个独立合约，不是一个 NFT：

| 表 | 主网地址（CREATE2，多链相同） | 回答什么 | 主网状态 |
| --- | --- | --- | --- |
| Identity | `0x8004A169FB4a3325136EB29fA0ceB6D2e539a432` | 谁登记了身份 | 已上线。ERC-721，name=`AgentIdentity`，symbol=`AGENT` |
| Reputation | `0x8004BAa17C55a88189AE136b182e5fdA19dE9b63` | 有没有被别人打过分 | 已上线 |
| Validation | 官方 Explorer 写 **mainnet pending**（TEE 流程未定） | 有没有第三方验收 | 测试网：`0x8004Cb1BF31DAf7788923b405b754f57acEB4272`。有人会扫 `0x8004Cc8439f36fd5F9F049D9fF86523Df6dAAB58`，以**事件为准**，不要看到 bytecode 就当验收层活了 |

一个 Agent 的真名是：

```text
eip155:{chainId}:0x8004A169FB4a3325136EB29fA0ceB6D2e539a432:{agentId}
```

`agentId` = ERC-721 `tokenId`，**不是**钱包地址。同一地址在 Base 和 BNB 上都可以是 `agentId=1`（部署者常见）。**跨链相加 ≠ 独立主体。**

测试网地址不同：Identity `0x8004A818…BD9e`，Reputation `0x8004B663…8713`。主网测试网不要混。

---

## 2. 为什么仪表盘会不准

2026-08-28 当场用 `ownerOf` 对过（Identity，主网）：

| 链 | 链上最高仍存在的 agentId（08-28 10:31 UTC） | agenteconomy 08-26 | 差什么 |
| --- | --- | --- | --- |
| BNB | 311,259 | 299,326 | 仪表盘滞后，且 BNB 一家就占「全球」六成 |
| Base | 73,285 | 70,113 | 滞后两天，量级对。近 2000 块 mint 5、反馈 2、验收 0 |
| Ethereum | **50,547** | **68,231** | 仪表盘**多算了约 1.8 万**。`ownerOf(68231)` 已 revert |

另外：`totalSupply()` **revert**（不是 Enumerable）。Basescan「token supply」如果乱显示，不要信。准确计数只能靠事件或 `ownerOf`。

---

## 3. 链上怎么数（从准到省）

### A. 身份存量（推荐捷径，先验证连续性）

`register()` 按序 mint。先抽查：`ownerOf(1)` 成功、`ownerOf(max+1)` revert，中间抽两三个也在，才能把「最大 tokenId」当成存量上界。

```bash
# 需要 foundry。以 Base 为例。
cast call 0x8004A169FB4a3325136EB29fA0ceB6D2e539a432 \
  "ownerOf(uint256)(address)" 1 --rpc-url https://mainnet.base.org

cast call 0x8004A169FB4a3325136EB29fA0ceB6D2e539a432 \
  "tokenURI(uint256)(string)" 1 --rpc-url https://mainnet.base.org
```

本目录 `python3 erc8004-tracking/query.py` 会对 Base / ETH / BNB 做二分 `ownerOf`。

**坑**：若某条链上 ID 有空洞，二分会低估。用 B 对一下最近 mint 的 tokenId 是否贴近二分结果。

### B. 身份流量（准，费 RPC）

从该链 Identity **部署块**起扫 mint。不要扫全链 `Transfer`。

```text
topic0 = keccak256("Transfer(address,address,uint256)")
       = 0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef
topic1 = 0x000…000          # from = address(0)
address = Identity Registry
```

`tokenId` 在 `topics[3]`。这是人口普查的金标准（[erc8004-base-census](https://huggingface.co/datasets/rsoft-latam/erc8004-base-census-jun2026) 也是这么干的）。

也有 `Registered(uint256,string,address)`，topic0：

```text
0xca52e62c367d81bb2e328eb795f7c7ba24afb478408a26c0e201d155c449bc4a
```

公开 RPC 对大区间 `eth_getLogs` 会 413。按 2k–10k 块切，或用带 archive 的节点。

部署块（Identity，主网，来自官方 Explorer `chains.yml`）：

| 链 | chainId | 部署块 |
| --- | --- | --- |
| Ethereum | 1 | 24,339,871 |
| Base | 8453 | 41,663,783 |
| BNB | 56 | 79,027,268 |

### C. 声誉（这才是「有没有人用」）

不要读「注册数」。扫 Reputation 的 `NewFeedback`：

```text
0x6a4a61743519c9d648a14e6493f47dbe3ff1aa29e7785c96c8326a205e58febc
```

然后算：

1. 事件条数  
2. 独立 `agentId` 数（`topics[1]`）  
3. 独立 `clientAddress` 数（`topics[2]`）  
4. 单 agent 占比（Base 上曾有一个 agent 吃掉反馈的约 2/3，内部钱包互评，不是市场）

合约禁止 owner/operator **自反馈**，但拦不住同一应用的马甲互评。`getSummary(agentId, clientAddresses, …)` 要求传入非空客户列表，**没有「全局平均分」这种 view**。

单点抽查：

```text
getClients(uint256 agentId) -> address[]
```

`len(getClients(id)) > 0` 才算「链上有过声誉」。全景里「质量分层 ~1,793」接近这个量级的过滤，不是 50 万。

### D. 验收（现在基本是空的）

官方：Validation **主网未作为规范层开放**。  
链上：Base 近约 2000 块 `ValidationRequest` / `ValidationResponse` = 0。二次收敛的判断不变——闭环断在验收，不断在注册。

若要自己盯，事件：

```text
ValidationRequest  0x530436c3634a98e1e626b0898be2f1e9980cc1bd2a78c07a0aba52d0a48a5059
ValidationResponse 0xafddf629e874ccc3963b6a888c477bd464a6c8525024fc88759ea3b2326349ae
```

---

## 4. 每周若只看四个数

8004 在研究里是**降权指标**。真要盯，只记这些，记在本目录快照里，不要写进决策：

1. **Base / ETH 的 max agentId**（BNB 当噪音分母，单独列）  
2. **近 7 日 mint 数**（Transfer from 0）  
3. **近 7 日 NewFeedback：事件数、独立 agent、独立 client、Top1 占比**  
4. **ValidationRequest 是否仍接近 0**

`1` 涨、`3` 不动 = 电话簿在膨胀。`3` 的独立 client 涨且 Top1 下降，才值得把 8004 从噪音里拿出来。

不要采：跨链总和、Agentverse 数、把 `tokenURI` 里写了 MCP 就当成在跑。

---

## 5. 仪表盘怎么当校对、不当真理

| 源 | 用途 | 限制 |
| --- | --- | --- |
| 本脚本 `query.py` | 当场 `ownerOf` + 近窗事件 | 公共 RPC 会限流；大窗 logs 要自己切 |
| [agenteconomy ERC-8004](https://agenteconomy.to) / Dune `7881124` | 看链分布、日增 | 会把 24 链加总；ETH 已出现 vis-à-vis `ownerOf` 的高估 |
| QuickNode 8004 Explorer | 文档、ABI、部署块 | Agents API 走 x402 付费；Validation 主网标注 pending |
| 8004scan / 类似 NFT 浏览器 | 看单个 token | 不要拿页面「total」当 census |

规范：https://eips.ethereum.org/EIPS/eip-8004  
合约与地址：https://github.com/erc-8004/erc-8004-contracts  

---

## 6. 和 x402 / MPP 追踪的关系

8004 注册 **不是** x402 买家，也不是 MPP payer。身份表膨胀，不能解释 PayAI 百万笔（那是 BlockRun），也不能解释 Tempo 近 7 日 1–3 个 payer。交叉时只做一件事：某个 `agentId` 的 `agentWallet` / owner，是否出现在 x402scan 买家或 Tempo payer 里。对不上就写对不上。
