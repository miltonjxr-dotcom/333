# Meme 研究 · 第三轮:同一 Attention 下的 Winner Selection

> 子课题:当一个注意力事件在极短时间内催生几十到几百个相似 Token 时,市场如何从近似候选中选出少数 Winner?分化之前是否存在可观测、可量化、可被 Codex 验证的差异?
> 方法:案例适格性筛选 → 逐案例时间线与 T* → 跨案例共性 → 可验证假设。不做大规模数据抓取。
> 纪律:Winner 特征 ≠ Winner 原因;价格上涨后的 Volume/Buyer/KOL 增长先假设为结果;Unknown ≠ External;Initial Trigger 无法确认就写 unresolved。
> 撰写日期:2026-08-20。前两轮见 `meme-market-mechanism-research.md`、`meme-research-round2-audit.md`。

---

## A. Case Selection

### A.1 候选案例适格性评估

| 案例 | Attention Source 明确 | 短时大量竞争 Token | Launch Time 接近 | 多个真实交易 Candidate | 无初始官方 CA | Winner/Loser 明显 | 外生干预 | 历史数据可得 | Codex 可重建 | 判定 |
|---|---|---|---|---|---|---|---|---|---|---|
| BROCCOLI(CZ 狗,2025-02) | 高(单条推文,分钟级) | 高(BSC ~300 + SOL ~480) | 高(揭晓后分钟级) | 是 | 是(CZ 明确不发官方币) | 高 | 中-高(BNB 流动性计划裁决,但过程本身可研究) | 高(BSC/Four.meme) | 高 | **入选** |
| NEIRO(Kabosu 家新犬,2024-07) | 高(Sato 推文) | 高(SOL+ETH 多版本) | 高(主要四版同日部署) | 是 | 是(狗主人明确切割) | 高(且**两次反超**) | 高(Ansem 喊单、Binance 上币——但干预本身是研究对象) | 高(Bubblemaps 已有取证) | 高 | **入选(信息量最大)** |
| KEKIUS(Musk 改名,2024-12-31) | 高(改名时刻精确) | 高(SOL/ETH/Base 大量仿盘) | 低(**胜者早于事件 2.5 周发射**——本身是发现) | 是 | 是(Musk 从未指定 CA) | 高 | 中(Musk 改回名字导致崩盘,属注意力源本身波动) | 高 | 高 | **入选(在位者激活型)** |
| MOODENG(河马走红,2024-09) | 中(病毒式渐进,无单一时刻) | 中(多链多版本+兄弟姐妹币) | 低(注意力爬坡数周) | 是 | 是 | 高 | 中(后期 Binance/Coinbase 上币) | 高(pump.fun) | 高 | **入选(渐进注意力对照)** |
| PNUT(松鼠事件,2024-11) | 高 | 中 | 高 | 是 | 是 | 高 | 高(Musk 转发+Binance 快速上币,干预极早且强) | 高 | 高 | 备选:适合 Codex 批量复现,本轮不深挖(与 MOODENG 同型但干预更早) |
| LUCE(梵蒂冈吉祥物,2024-10) | 高 | 中 | 中 | 是 | 是 | 中 | 低 | 中 | 中 | 备选:结构可用但公开取证少,深挖性价比低 |
| GHIBLI(GPT 吉卜力风潮,2025-03) | 低(多日扩散型趋势,无单一时刻) | 高 | 低(发射分散) | 是 | 是 | 中 | 低 | 中 | 中 | 不入选:事件簇边界模糊,T0 不可定义 |
| BOSS / Ibiza Final Boss(2025) | 中 | 中 | 中 | 是 | 是 | 中 | 未核实 | 低(公开链上取证少) | 中 | 不入选:本轮可得材料不足以重建时间线 |
| ASTEROID(2024 YR4 新闻,2025-02) | 中(新闻多次反复) | 低 | 低 | 弱 | 是 | 低(无明显大 Winner) | 低 | 低 | 低 | 不入选:注意力未有效转化,属"事件级失败"样本(另有价值,不属本题) |

### A.2 最终选择与类型覆盖

入选 4 案:**BROCCOLI**(A 型:明确事件/名字揭晓,crypto 原生人物)、**NEIRO**(B 型:动物/传承事件,含两次反超,信息量最大)、**KEKIUS**(C 型:crypto 原生人物信号,在位者激活)、**MOODENG**(B2 型:非 crypto 原生渐进病毒)。类型覆盖了"瞬时揭晓 vs 预告-激活 vs 渐进爬坡"三种注意力时间结构——这个维度后来被证明是关键变量(见 C)。

BROCCOLI 按本轮边界修正:主要研究 **BSC/Four.meme 内部 Candidate vs Candidate**,不再做 BSC vs Solana 跨链比较(Narrative–Chain Fit 混杂,CZ 事件天然绑定 BSC)。同理,NEIRO 的链间迁移(SOL→ETH)只作背景,重点比较**同链内**候选。

---

## B. 案例复盘

### B.1 BROCCOLI(2025-02-13,BSC 内部)

- **Event:** CZ 揭晓爱犬名 "Broccoli"(11:12 ET),明确不发官方币,暗示可能交易成功版本、BNB Foundation 可能支持。揭晓前 3 小时有预告(催生猜名抢跑盘 CLEO/BROWNIE/PERRY,揭晓即全灭)。
- **Candidate Set:** Four.meme 上 ~300 个 Broccoli 主题代币,绝大多数数分钟内死亡;进入有效竞争约 2–3 个;最终两强:Broccoli "714" 与 BROCCOLI "F2B"。
- **Competition Timeline:** T0+3min 大量候选交易;T0+2h 领先者触及 ~$400M 市值(2 小时 $220M 成交);T+5~6 天两强并存;02-19 BNB Chain 流动性计划评分并列、以成交量决胜判 714 胜,伴随社区对评分口径的争议。
- **Winner / Runner-up / Losers:** Winner=714;Runner-up=F2B(长期并存后被制度性裁决压制);Effective Losers=最初 2 小时内冲高回落的数个候选;Fast Failures=数百个(典型特征:deployer 自铸大仓、mint 后数分钟即卖,如 0x392eb 案例)。
- **Earliest Observable Divergence:** T0+2h 内市值/成交份额已呈数量级分层(粒度受限于公开报道,分钟级需重建)。失败侧更早:deployer 即时出货在 mint 后几分钟就可观测。
- **Possible Initial Trigger:** unresolved。领先者最初 15–30 分钟为什么是它(whale?deployer 信誉?名称/图片精确度?随机性?)公开材料无法区分。
- **Cause vs Consequence:** 均匀狙击税(狙击合约同块买走每个新盘 50%,获利 $10M+)对候选间胜负无判别力——寄生负载在事件内是常数,不是选择变量。两强长期并存说明纯市场份额领先**不足以**完成最终协调;外生权威(平台评分)才完成对称性破缺,且裁决依据(成交量优势)本身是市场变量——权威放大而非取代市场信号。
- **What We Don't Know:** 714 与 F2B 首小时买家结构差异;两强并存期间份额动量是否早已预示裁决方向;瞬时十亿级市值印记中自成交占比。
- **Data Quality:** 高。BSC 全链可重建,事件边界清晰。

### B.2 NEIRO(2024-07-27 起,双链、两次反超)

- **Event:** Kabosu(DOGE 原型犬)主人 Sato 宣布收养新犬 Neiro(07 月下旬推文);"DOGE 继承者"叙事即时成立;狗主人随后明确与所有代币切割。
- **Candidate Set:** 大量 NEIRO 代币;四个主要版本同日(07-27)部署:两个 Solana(更早)、两个 Ethereum(21:14 UTC "first Neiro" 与 22:19 UTC "Neiro ETH")。
- **Competition Timeline(浓缩):**
  1. **Solana 局:** 首个达 $100M 的 NEIRO 在 Solana,但 dev 多钱包控盘,12 小时内获利 $3.3M(合并关联后 $5.7M+);随后 KOL Ansem 转而背书一个微市值、结构更干净的 SOL 版本 → 后者 10 倍,$80M 领先者崩盘(**反超 #1**);最终两个 SOL 版本都归于沉寂。
  2. **Ethereum 局:** "Neiro ETH"(22:19 部署)发射时 **78% 供给被同步狙击**、分散到 400 钱包掩护出货(Bubblemaps 取证;两日内卖出 $4M+,一周 $6.5M,仍持 66%),借 KOL 网络成为总领先者,峰值 $280M。"first Neiro"(21:14 部署)dev 跑路后社区接管(CTO),数周维持 ~$15M 弱势横盘。
  3. **09-16 Binance 现货上线 $15M 的 CTO 版**("the first NEIRO on Ethereum"):CTO 版 24 小时 +700~1000% 至 $178M,insider 版 -37%(**反超 #2**)。上币公告前有未标记地址提前建仓 CTO 版,浮盈 $500k+(公告前的知情资金流)。
- **Winner / Runner-up / Losers:** 最终 Winner=CTO 版(交易所背书);中期 Winner 后转 Loser=insider 版(结构性合法性缺陷被引爆);早期 Winner 后转 Loser=SOL 控盘版;Fast Failures=其余大量版本。
- **Earliest Observable Divergence:** 每一局内部,领先者在 1–2 日内确立;但**领先不稳定**——本案的核心信息是反超的结构:两次反超的受益者都是"结构更干净/更有正统性主张"的落后候选,两次触发器都是外生协调权威(顶级 KOL、交易所)。
- **Possible Initial Trigger:** 各局最初领先的成因 unresolved(insider 版靠 78% 控盘+KOL 网络点火是已知的,但为什么它而不是别的 insider 盘,不可考)。反超的触发器则完全明确(Ansem 推文时刻、Binance 公告时刻)。
- **Cause vs Consequence:** 本案最有价值的因果证据:(a) 市值/成交领先**不是**稳定的 Schelling 锚——$80M 和 $120M 的领先者都被翻转;(b) 权威选择受益者时使用的判据是**事前可观测的结构与正统性特征**("first"、CTO/社区化、更干净的筹码结构)——即筹码结构通过"合法性通道"因果地影响终局,而不仅是通过卖压通道;(c) 公告前的异常吸筹是协调事件的领先信号(知情流)。
- **What We Don't Know:** insider 版 KOL 网络的构成与报酬(链下);Binance 选择 CTO 版的内部决策依据;若无交易所干预,insider 版能否靠持续做盘维持领先(反事实不可得)。
- **Data Quality:** 高。Bubblemaps 已完成关键取证,双链数据可重建,时间戳精确。

### B.3 KEKIUS(2024-12-31,在位者激活)

- **Event:** 两段式注意力:12-13 Musk 回帖 "Kekius Maximus 😂"(弱信号,2900 万浏览);12-31 Musk 改 X 用户名+头像为 Kekius Maximus(强信号);01-01 改回(注意力源撤回)。
- **Candidate Set:** 弱信号后数日内出现第一批 KEKIUS 币(ETH 版创建于 12-14;另有自称 12-10 的 SOL "$KM",其"最早"主张来自项目自宣,存疑);12-31 强信号后 Solana/ETH/Base 上大量新仿盘涌现。
- **Competition Timeline:** 12-14 ETH KEKIUS 创建,至 12-31 前累积 ~$12M 市值与数万 holder(已有池子、图表、持仓结构);12-31 强信号后该在位者 30 倍冲至 $380M 峰值,同时"大量 Solana 新仿盘未获得同等成功"(当时报道原话);01-01 Musk 改回名字,1 小时内 -75%。
- **Winner / Runner-up / Losers:** Winner=12-14 的 ETH 在位者;Losers=12-31 当天的全部新发射(几乎无一跑出);特殊 Loser=Winner 自己在注意力源撤回后单小时崩 75%(注意力单点依赖风险)。
- **Earliest Observable Divergence:** 强信号时刻即分化——资金几乎立刻流向在位者而非新发射,分钟级可观测。
- **Possible Initial Trigger:** 在位者的胜出机制较清晰(唯一有存量流动性、holder、可验证历史的候选=天然焦点);但**为什么是 ETH 的 12-14 版而不是其他弱信号期发射的版本**成为在位焦点,unresolved(候选间的弱信号期竞争无公开记录)。
- **Cause vs Consequence:** 本案干净地展示:当注意力有"预告→激活"结构时,Stage 0 的竞争其实发生在**弱信号期**;强信号时刻的海量新发射在结构上已经迟到——它们面对的不是平等起跑线,而是一个已有 $12M 市值的在位者。"发射时间接近"这一适格标准在此类事件中系统性不成立,这本身是发现。
- **What We Don't Know:** 弱信号期(12-13~12-31)各候选的份额演化;在位者期间是否有操盘方维护(约 $12M 市值维持 2.5 周,是自然留存还是做市,未知——**不把 Unknown 当 External**)。
- **Data Quality:** 中-高。ETH 主线清晰;弱信号期的候选集重建需 Codex;"最早"主张存在冲突记录。

### B.4 MOODENG(2024-09-11 起,渐进病毒 + 先发在位)

- **Event:** 泰国动物园小河马 Moo Deng 7 月出生,9 月上中旬开始病毒式走红,9 月下旬达到主流媒体级热度(无单一引爆时刻,注意力爬坡数周)。
- **Candidate Set:** SOL 主版本(09-11 pump.fun 发射)、ETH 版($7.5M)、Base 版、其他 SOL 仿盘、兄弟姐妹币(Moo Toon、Moo Waan,全部失败)。
- **Competition Timeline:** 09-11 主版本发射(此时热度尚在早期);09-26 破 $100M(从零到 $100M 期间竞品从未接近);9 月底峰值 ~$338M;后获 Binance/Coinbase 上币二次拉升。
- **Winner / Runner-up / Losers:** Winner=SOL 主版本(全程无有效挑战者);Losers=后发的各链仿盘与衍生币(在 Winner 已确立后发射,从未进入竞争)。
- **Earliest Observable Divergence:** 不锐利——Winner 在注意力峰值到来**之前**就已是最大在位者;后发者始终无份额。与 KEKIUS 同构:胜出发生在注意力曲线早段,峰值期只是兑现。
- **Possible Initial Trigger:** unresolved。09-11~09-20 期间它如何压过同期其他早期 MOODENG(如果存在),公开材料没有候选集层面的记录;其 X 粉丝页运营质量被事后引用为原因,但这是典型的"知道 Winner 后找优点",不采信为因果。
- **Cause vs Consequence:** 注意力渐进型事件中,"先发+在注意力爬坡期存活"近乎决定胜负;后发仿盘的失败不需要用质量解释——它们发射时协调已完成。兄弟姐妹币(不同名字、蹭同一 IP)全灭,提示焦点收敛在"精确名称"上,外延叙事无法分流焦点。
- **What We Don't Know:** 发射后前 10 天的候选集与份额演化(是否曾有同名竞争者被淘汰);早期买家中操盘/外部结构(MEXC 材料提到"早期数分钟 insider 吸筹常见",但无本币种的具体取证)。
- **Data Quality:** 中-高。pump.fun 数据可重建;竞争过程的公开取证最少,深挖依赖 Codex。

---

## C. Cross-case Findings

### C.0 前置发现:三阶段划分成立,但需要加一个"第 -1 阶段"

Stage 0(海量发射→存活)/ Stage 1(存活→候选集)/ Stage 2(候选集→主导者)的划分在瞬时揭晓型事件(BROCCOLI、NEIRO)中成立且决定因素确实不同。但 KEKIUS 与 MOODENG 揭示:**当注意力是"预告→激活"或"渐进爬坡"结构时,真正的选择发生在注意力峰值之前的弱信号期(Stage -1:在位者形成)**;峰值时刻的海量发射整体上是结构性迟到者。因此事件必须先按**注意力时间结构**分型:瞬时型(竞争在 T0 后分钟-小时内)、预告型与渐进型(竞争在弱信号期,峰值只是兑现)。这是本轮相对前两轮最重要的新变量:**发射时间相对注意力曲线的位置,而不是相对其他候选的先后。**

### C.1 为什么大量 Token 连 Candidate Set 都进不了?

跨案例一致的三个淘汰机制(按证据强度排序):
1. **结构性迟到**(KEKIUS 12-31 新盘、MOODENG 后发仿盘、BROCCOLI 揭晓后第 N 百个):发射于协调已完成或在位者已存在的时点。这解释了失败者的大多数,且完全不需要"质量"解释。
2. **Deployer 即时抽取**(BROCCOLI 0x392eb 型:自铸大仓、数分钟内开卖):等价于向市场宣告本候选无人护盘,观测上是最早的 Fast-Failure 信号。
3. **无点火资本**:没有任何主体出资制造初始市场(池子从未获得足以进入任何排序界面的活动)。多数当日死亡盘属此类。[推断,与第一轮 F1 一致;逐盘验证需 Codex]

### C.2 为什么少数 Candidate 能进一步跑出来?

- 瞬时型事件中:进入候选集需要**早期点火(常为操盘资本)+ 一个可辩护的正统性主张**(精确名称/图片、"first"、社区化)。NEIRO insider 版证明纯操盘资本+KOL 网络足以把候选推到 $280M——**操盘驱动可以走很远**;但同案也证明这种领先携带合法性负债。
- 预告/渐进型事件中:进入候选集 ≈ 在弱信号期发射并存活到激活时刻(在位者资格)。
- 两型共同点:候选集规模极小(300→2~3;数百→1),且候选席位在极短窗口内锁定。

### C.3 为什么几个强势版本最后又继续分化(或长期并存)?

案例给出比第一轮 Schelling 叙述更具体的机制:**市场份额领先本身不是稳定的协调锚;当候选间存在"正统性争议"时,多均衡长期并存(714/F2B、双 NEIRO),直到外生协调权威(交易所上币、顶级 KOL、平台评分)完成对称性破缺。** 三案中所有最终收敛都由权威事件触发,无一由纯市场过程完成。权威的裁决依据部分是市场变量(BROCCOLI 以成交量决胜),部分是正统性变量(Binance 选"first"、Ansem 选"干净")——即权威放大市场与结构信号,而非随机指定。

### C.4 为什么某些 Early Winner 会被反超?

NEIRO 两次反超给出一致结构:**早期领先者的筹码结构缺陷(高度狙击/控盘、持续内部释放)构成"合法性攻击面";当存在一个结构更干净、有正统性主张的落后候选时,协调权威的介入会把市场重新协调到挑战者上。** 反超的触发时刻外生且不可预测,但**受益者的身份事前可从结构特征预测**;且 NEIRO 案中权威公告前出现了对挑战者的异常知情吸筹(可观测的领先信号)。这把第一轮"筹码结构通过卖压通道起作用"的机制扩展了一条新通道:**筹码结构 → 合法性 → 协调易手风险**。早期领先 + 脏结构 + 存在干净挑战者 = 反超高危组合。

### C.5 对本轮总问题的直接回答

同一 Attention 下,市场的选择是一个**分阶段、可被少数外生事件重置的协调过程**:(1) 候选资格在注意力曲线早段以"发射时点 + 点火资本 + deployer 行为"锁定;(2) 候选集内的早期领先由相对份额动量与正统性主张共同确立(初始触发常不可考);(3) 最终收敛几乎总由协调权威完成,权威偏好可从结构特征事前预测。**最早可实时观测的信号(按时序):** 发射时点相对注意力曲线的位置 → deployer 首小时行为(自铸即卖=淘汰)→ 早期相对新资金份额动量 → 候选的正统性特征组合(精确名称、first 主张、筹码干净度)→ 对沉寂候选的异常知情吸筹(权威事件前兆)。

---

## D. 最值得 Codex 验证的 Hypotheses(7 条)

**WH1|注意力曲线位置决定候选资格**
- Hypothesis:Winner 不成比例地发射于注意力曲线的首个弱信号处;注意力峰值后发射的候选几乎从不获胜;"发射越早越好"在弱信号前不成立(过早=无注意力可接)。
- Mechanism:C.0 的 Stage -1;在位者是激活时刻的天然焦点。
- Observable Proxy:发射时间戳 − 事件首信号时间戳(推文/新闻可精确到分钟);候选在峰值时刻的存量流动性与 holder。
- Leading/Coincident:Leading(发射时刻即定)。
- Data Availability:高(链上时间戳 + 事件时间线)。
- Main Confounder:幸存者偏差(弱信号期发射者大多也死了——必须以"弱信号期发射的全体"为分母,而非只看 Winner);事件首信号时刻的界定主观性。
- Codex Feasibility:高。
- Expected Value:高——若成立,单变量即可淘汰事件内大部分候选。

**WH2|Deployer 首小时行为的一票否决**
- Hypothesis:deployer(及其 1 跳资金关联钱包)在首小时内净卖出的候选,进入候选集的概率趋近于零;deployer 持仓静止是候选资格的必要非充分条件。
- Mechanism:即时抽取=公开宣告无人护盘(C.1;BROCCOLI 失败者共性;第二轮 CH2 的确认与扩展)。
- Observable Proxy:deployer 系钱包首小时净流(仅需 1 跳聚类)。
- Leading/Coincident:Leading(相对候选集形成)。
- Data Availability:高。
- Main Confounder:deployer 通过未识别钱包出货(保守偏误方向,可接受)。
- Codex Feasibility:高。
- Expected Value:高——最便宜的 Stage 0 过滤器。

**WH3|相对新资金份额动量(控制动量后的独立性检验)**
- Hypothesis:事件簇内 T0+15~60min 的新资金份额动量预测 Stage 1 入围与 Stage 2 领先;且在控制同期价格动量、市值排名、流动性排名后仍保留独立信息(若不保留,明确降级为动量影子)。
- Mechanism:份额动量是协调收敛过程的实时投影(第二轮 P1-1 的事件版,加上本轮第十点要求的反方检验)。
- Observable Proxy:候选级分钟净流 ÷ 事件簇总净流;对照:价格动量分位数。
- Leading/Coincident:待判定——本假设的核心就是判定它是 Leading 还是 Coincident。
- Data Availability:高(纯 DEX 数据,零聚类)。
- Main Confounder:价格动量的机械耦合(AMM 中净流与价格同源)——需用"份额 vs 簇内排名变化"的正交化设计。
- Codex Feasibility:高。
- Expected Value:高——是第二轮核心假设的严格化版本,证伪价值与证实价值同样大。

**WH4|筹码结构的两阶段效应(候选期无害,争议期致命)**
- Hypothesis:高狙击/控盘份额不阻碍候选成为早期领先者(NEIRO insider 版 78% 照样登顶),但显著提高"存在干净挑战者条件下"的反超风险;结构变量的预测力条件于竞争格局,而非无条件负面。
- Mechanism:C.4 合法性通道——脏结构是攻击面,只在有人攻击时兑现。
- Observable Proxy:发射块狙击占比、bundle 份额(高置信层);竞争格局=候选集内是否存在结构干净且存活的第二名。
- Leading/Coincident:Leading(对反超事件)。
- Data Availability:中(需发射块重建+基础聚类)。
- Main Confounder:干净挑战者的"存在"与权威介入可能共因(权威制造了挑战者的存活)。
- Codex Feasibility:中。
- Expected Value:高——直接修正第一轮"控盘双面性"为可检验的条件形式。

**WH5|协调权威事件的可预测受益者 + 前兆资金流**
- Hypothesis:(a) 交易所上币/顶级 KOL 背书/平台计划等权威事件发生时,受益者可由事前正统性特征预测(first 主张、CTO/社区状态、更干净筹码、更精确名称);(b) 权威公告前,受益候选出现异常吸筹(知情流),幅度与随后的份额易手正相关。
- Mechanism:C.3/C.4;权威放大结构信号;知情者提前行动(NEIRO 上币前 $500k 浮盈地址)。
- Observable Proxy:(a) 候选正统性特征编码 + 权威事件清单;(b) 沉寂候选(份额低位横盘)的净流异常检测。
- Leading/Coincident:(a) 条件预测;(b) Leading(相对公告)。
- Data Availability:(a) 中(事件清单需人工);(b) 高。
- Main Confounder:(b) 中的异常吸筹可能是巧合或操盘自导;样本内权威事件数量有限(统计力问题)。
- Codex Feasibility:中。
- Expected Value:中-高——(b) 若成立是全研究中最接近可交易的信号之一。

**WH6|多 Winner 并存的结构条件**
- Hypothesis:候选集内存在两个各自拥有不同正统性主张的候选(如"最早" vs "最大")且无权威介入时,双强并存显著延长;首个权威事件后集中度跳升。Winner-takes-all 不是默认结局,而是权威事件的产物。
- Mechanism:C.3;正统性争议维持多均衡。
- Observable Proxy:候选集 HHI(集中度)时间序列 × 权威事件时间戳。
- Leading/Coincident:结构描述型(为 WH5 提供环境变量)。
- Data Availability:高。
- Main Confounder:权威介入本身可能被并存格局吸引(双向因果——用事件研究法围绕公告时刻切断)。
- Codex Feasibility:高。
- Expected Value:中——主要价值是校正"强制单 Winner"的建模错误。

**WH7|资金持续性区分候选集内的守擂与掉队**
- Hypothesis:候选集成员中,第二、三批新资金批次不衰减者守住份额;批次衰减但价格仍在高位者随后掉队(Effective Loser 的领先识别)。
- Mechanism:第二轮 P1-5 在事件竞争场景的应用;掉队先于价格显现于资金批次。
- Observable Proxy:批次化新钱包净流(1 跳过滤)。
- Leading/Coincident:Leading 候选。
- Data Availability:高。
- Main Confounder:Sybil 批次伪造;批次划分参数敏感性。
- Codex Feasibility:高。
- Expected Value:中-高。

### 优先级与删减说明

按"证伪杠杆/成本"排序:WH1、WH2、WH3 最先(纯时间戳与 DEX 数据,能推翻本轮一半结论);WH7 随后(1 跳聚类);WH4、WH5、WH6 需要结构编码与事件清单,排第二梯队。原候选变量中:**Narrative–Chain Fit** 不单列假设(样本内它只在 CZ/BNB 事件中明确起作用,且已通过案例边界修正规避——作为 Context Variable 记录);**Initial Whale Impulse** 并入 WH3 的份额动量(单独的 whale 识别在事件早期分钟级窗口内与大额净流不可区分);**Operator Dependence 的完整版**(Operator-driven→Market-driven 转换)保留在第二轮 P1-2,不在事件场景重复。

---

*本文件为第三轮子课题研究;总体框架见第一轮,变量可行性与优先级框架见第二轮。三轮结论冲突时,以更晚轮次为准。*
