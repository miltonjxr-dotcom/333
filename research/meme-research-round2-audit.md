# Meme 市场机制研究 · 第二轮:严格复核与实操收敛

> 目的:审计第一轮理论,判断哪些真正站得住、哪些只是逻辑漂亮、哪些可以可靠量化、哪些值得下一阶段 Codex 投入。不再扩张理论。
> 纪律:理论变量与 Observable Proxy 分开;可计算与可预测分开;Leading/Coincident/Lagging 分开;不确定的地方明确写"不知道"。
> 撰写日期:2026-08-20(第一轮报告见 `meme-market-mechanism-research.md`)

---

## A. Executive Verdict(8 条)

**V1|站得住:庄 = 协同经济实体网络;Stock/Flow 区分;"庄家卖出不必然利空、吸收才是分岔"。** 这三条逻辑 Strong、证据 Partial-Strong(MELT/Pine/UCL/Bubblemaps),且都能落到可操作的观测上——前提是把实体识别限制在高置信层(见 V4)。

**V2|需要降级:D>R 是恒等式不是 Alpha;G>1(Reflexivity Gain)是抽象语言不是可估参数;Critical Gates 与"共识化"是叙事脚手架不是指标。** 第一轮最大的问题是把"帮助理解的会计恒等式"与"可产生超额收益的可测变量"混在了一起。价格上涨当然等价于净流入为正——这不含信息;信息只可能来自**比价格更早观测到流入的结构变化**(谁在买、来自哪里、第几波)。凡是要用未来数据或价格本身才能计算的量(吸收率、增益、共识化),一律不得作为 Early 信号。

**V3|最大的研究风险:Entity Clustering 误差 + 选择效应 + Point-in-time 违规。** 三者任何一个失控都会让全部结论作废。对策分别是:第一阶段只用高置信实体关系(deployer 直接出资、创建块接收、同 bundle/同 tx);所有假设检验必须带匹配对照组(arXiv 2607.02795 的安慰剂教训);所有指标必须用当时区块数据重建,禁止用今天的标签(smart money 名单、集群图)回溯贴到历史上——那是最隐蔽的未来函数。

**V4|本轮最重要的新认识之一:完整实体聚类不是第一阶段的前置条件。** 高置信层(deployer 资金图 1 跳、创建块、同块狙击、直接转账)工程成本低、误差可控,足以定义一个"已知内部人"子集;把其余全部当作"未知/外部"虽然会漏(CEX 中转、预埋钱包、链下协同),但**漏检的方向是把内部人误判为外部人,即对"外部接棒"假设是保守偏误**——假设在带偏误的数据上仍成立,则真实效应更强。Cheap falsification first 路线成立。

**V5|本轮最重要的新认识之二:同事件竞争(Relative Share)可能是最便宜、最干净的检验场。** 同一注意力事件下的几十个同名代币天然控制了 beta、叙事、注意力总量,是现成的自然实验;BROCCOLI 案例显示胜负在 1–2 小时内就基本可观测(份额分化),而且完全不需要实体聚类就能计算 Volume/Liquidity/Buyer Share Momentum。这应该是 Codex 的第一个战场。

**V6|Buyer Diffusion 审查结论:四层中 Money(quote 加权净流入)和 Persistence(后续批次是否持续到来)最有价值且最易量化;Breadth(人头数)单独使用接近无价值;Independence 第一阶段只做资金独立(1 跳 funding 检查),信息源独立性推迟。** "External Capital Diffusion(分批次的外部资金扩散)"确实比 Buyer Growth 更接近我们要研究的对象,正式替换。

**V7|Absorption 重新定位:它是状态确认与 Exit/Risk 指标,不是 Early Filter。** 定义上它只能在内部释放发生之后被观测。第一轮把 T/D 写成通用状态变量是对的,但必须明确:它对"该不该进"无用,对"该不该继续持有/该不该跑"可能非常有用。

**V8|"伪造成本 ≈ 信息价值"降级为数据质量与指标筛选原则,不是预测理论。** 难伪造 ≠ 领先:已实现净流入极难伪造但与价格同步(coincident)。既难伪造又可能领先的变量只有一小类:**知情者的行为流**(内部净释放、LP 的深度操作、成本结构变化)——因为它们揭示私有信息。筛选逻辑应是"先按伪造成本过滤掉垃圾,再按领先性排序",两步不能合并。

### 附:第一轮七个核心观点的逐项审计

| # | 观点 | 理论逻辑 | 已有证据 | 因果倒置风险 | 恒等式还是 Alpha | 交易价值 | 处置 |
|---|---|---|---|---|---|---|---|
| 1 | 外部资金接替操盘资金 = 硬拉→真实扩张的分界 | Strong | Partial(无直接研究;UCL 间接支持) | 低(但边界近恒等式:需求持续=外部在买。Alpha 只来自**领先于价格**观测到接棒的结构) | 边界恒等式,操作化后有 Alpha 空间 | 高(若便宜 proxy 成立) | 保留,P1(操作化为 External Buy Share 趋势) |
| 2 | Attention ≠ Demand,转化才关键 | Strong | Strong(Barber-Odean;UCL 因果证据) | 低 | 理论正确,但 Attention 数据链下、昂贵、难 point-in-time | 直接量化:低;间接(用链上新钱包流做转化的影子):中 | 理论保留,量化 Deferred |
| 3 | Stock=风险暴露,Flow=时间信息 | Strong | Partial(传统内部人交易文献类比;UCL 显示 creator/sniper 利润来自卖出行为) | 低 | Alpha 候选(Flow 揭示私有信息) | 高(Risk/Exit 侧) | 保留,P1 |
| 4 | Buyer Diffusion 是反身性投影;Buyer Count ≠ Demand | Strong | Partial | 中(买家增长可能是价格的结果——必须以"份额/批次领先性"设计检验) | Alpha 候选 | 中-高 | 保留,重构为 External Capital Diffusion,P1 |
| 5 | 庄家卖出不必然利空,吸收是分岔 | Strong | Partial(案例级) | 低,但**注意恒等式陷阱**:"卖出且价格没跌"若用同期价格定义吸收,则是同义反复。必须用释放窗口的流量比预测**后续**窗口 | 操作化后是 Alpha 候选 | 高(Exit 侧) | 保留,P1,限定为非-Early |
| 6 | Reflexivity / Coordination / Winner-takes-most | Strong | Partial(结构性+案例;组件已证) | 高(Schelling Point 的原因与结果极易混淆,见 F) | G>1 不可估,删;相对份额动量是可测替身 | 中-高(事件内竞争场景) | 机制保留;量化改走 Relative Share 路线,P1 |
| 7 | 庄 = 协同实体网络而非单钱包 | Strong | Strong(MELT 36.5% bundled;Bubblemaps;Pine) | 低 | 定义,非假设 | 作为数据结构:必要 | 保留;第一阶段仅高置信层 |

---

## B. Core Mechanism(4 条,可验证表述)

**M1|跑出来 = 在注意力窗口内,外部新资金的到达速度持续压过低成本筹码的变现速度。** 可验证内核:用高置信内部人子集划分买卖流后,"外部买入份额的趋势"和"内部净释放速率"应分别正/负预测后续窗口的价格与存活——且预测力应强于价格动量本身(否则它只是价格的影子)。

**M2|同一注意力事件下,需求不是分给所有候选者,而是通过协调博弈收敛到极少数焦点;收敛发生在极早期且主要由相对份额驱动。** 可验证内核:事件簇内,早期(分钟级)Volume/Liquidity/新买家**份额动量**对最终胜者的判别力,应显著高于任何绝对量;且胜者通常不是最早发射者(先发优势弱于焦点收敛)。BROCCOLI 支持此表述(见 F)。

**M3|失败的主导模式随阶段切换:早期死于"没被看见/没被选中"(注意力与协调),中期死于"外部接棒失败"(反身性未点火),后期死于"内部释放压过吸收"(供给)。** 可验证内核:三组变量(份额动量 / 外部买入份额趋势 / 内部释放-吸收比)各自只在对应阶段有预测力,跨阶段混用则预测力消失——这本身就是可证伪的结构性预言。

**M4|知情者的行为流是最不可伪造且唯一必然领先于其自身后果的信号。** 内部人卖出必然发生在崩盘式分发的因果链上游;可验证内核:高置信内部集群的净卖出**加速度**对未来大幅回撤的提前量 > 任何价格/成交量类信号;而其持仓量(Stock)在控制 Flow 后无增量预测力。

(第一轮 M3"注意力上的协调博弈"并入 M2;"流量比恒等式"不再单列为机制——它是会计框架,不是假设。)

---

## C. Practical Feasibility Table

只保留值得讨论的变量。Observable:Direct/Proxy/VeryHard;其余维度用 H/M/L。"文字高级但难量化"的变量单独标注 ⚠。

| 变量 | 经济含义 | Observable | Best Practical Proxy | Proxy Error | Point-in-time | Leading? | 操纵抗性 | 实体依赖 | 历史数据 | 实时可行 | 工程成本 | 增量价值 | Priority |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| External Buy Share(外部买入份额) | 买压中来自"非已知内部人"的比例及趋势 | Proxy | 1 −(高置信内部集群+同块 sniper 的买入占比);辅以钱包年龄/资金来源 1 跳检查 | M(漏检内部人→保守偏误,方向可控) | 是 | **Leading 候选**(相对价格) | H | M(仅高置信层) | M | M | M | **H** | **P1** |
| Insider Net Release(内部净释放) | 已知内部集群的净卖出速率/加速度 | Proxy | deployer 资金图 1 跳 + 创建块接收者 + 同块狙击者的净卖出流 | M | 是 | Leading(对回撤) | **H**(伪装卖出=真卖出) | M | M | M | M | **H** | **P1** |
| Release/Absorption 比(T/D) | 内部释放窗口内,外部流入对卖压的承接 | Proxy | 释放窗口内:内部净卖出 ÷ 外部净买入;预测**后续**窗口 | M | 是(注意:只在释放发生后存在) | 状态确认 + Exit | H | M | M | M | M | H(仅持仓管理) | **P1**(限 Exit/确认) |
| External Capital Diffusion(分批次外部资金扩散) | 新增 quote 资金是否分批持续到来 | Proxy | 按到达时间分批的新钱包 quote 净流入;批间隔与批规模衰减率 | M(Sybil;用资金来源 1 跳过滤) | 是 | Leading 候选 | M | L-M | M | M | M | **H** | **P1** |
| Relative Share Momentum(事件内份额动量) | 同事件候选者间 Volume/新买家/流动性份额的变化速度 | **Direct** | 事件簇内各 token 的份额时间序列(纯 DEX 数据) | **L** | 是 | **Leading 候选**(对胜负) | M(份额可刷,但刷量者同时抬高自己成本) | **L(无需聚类)** | **E** | E | **L** | **H** | **P1** |
| Liquidity/Depth Dynamics | 深度增长与市值增长的匹配度;LP 行为 | Direct | 池储备序列;LP 添加/撤出事件 | L | 是 | 混合(LP 撤出=Leading 风险信号) | H(LP 操作成本高) | L | E | E | L | M-H | **P1**(Risk 侧) |
| Effective Float / Cost Basis | 持仓成本分布 = 潜在卖压地形 | Proxy | 逐钱包交易史重建成本基础分布(无需聚类) | M(钱包≠人,但分布层面可用) | 是 | 中期 Leading(阻力结构) | H | **L** | M | M | M | M | P2 |
| Sniper/Parasite Load | 非协同低成本持仓的税负 | Proxy | 前 N 块买入者持仓及清仓速度;区分 deployer 关联(Pine 方法) | M | 5 是 | 早期结构变量 | M | M(1 跳即可) | M | M | M | M(见 F:事件内为均匀税,判别力存疑) | P2 |
| Manufactured→Real Conversion(伪信号后转化差) | 操纵活动后外部真实流入的边际变化 | Proxy | 洗量/自成交识别(flip-score)+ 之后外部净流入变化 | M-H | 是 | Leading 候选(点火判别) | M | M | M | M | M-H | M | P2 |
| Market Beta | 板块级风险偏好乘数 | Direct | SOL/板块资金净流、launchpad 总量 | L | 是 | 条件变量(非信号) | H | L | E | E | L | M(作为分层变量必须有) | P1(作为控制变量) |
| ⚠ Attention Conversion | 注意力→资本转化率 | VeryHard | 社交提及时序 × 链上新钱包流(需链下数据+归因) | **H,潜在致命**(社交数据缺口、时间戳不可靠、KOL 删帖) | 部分 | 理论 Leading,实测未知 | L | M | **Hard** | Hard | **H** | 未知 | **Deferred** |
| ⚠ Multi-operator Structure | 多庄并存的抢跑风险 | VeryHard | 需要中置信聚类(共同行为模式)才能区分"多个集群" | H(聚类边界误差直接改变结论) | 部分 | 中期 | H | **H** | Hard | Hard | H | 未知 | **Deferred** |
| ⚠ Reflexivity Gain(G 作为数值) | 环路增益 | VeryHard | 无可靠估计;任何单数值都是虚假精确 | 致命 | — | — | — | — | — | — | — | — | **Delete**(概念保留,数值删除) |
| ⚠ Market Consensus / 共识化 | 筹码结构相变完成 | VeryHard | 只能事后弱操作化(内部份额低+价格韧性) | H | 否(本质上滞后) | Lagging | — | H | Hard | — | H | L(交易上太晚) | **Delete**(作为指标) |
| Buyer/Holder Count 类 | 人头计数 | Direct | — | 对"需求"而言 H(Sybil) | 是 | Coincident 至 Lagging | **L** | L | E | E | L | **L**(在 quote 流之后无增量——本身是待验证的负假设) | Downgrade |

**"文字高级但难量化"点名:** Reflexivity Gain、Market Consensus、Attention Conversion(直接形式)、Multi-operator Structure、以及第一轮的"信息源独立性"。这五个是第一轮最漂亮的语言和现实量化能力之间落差最大的地方。

---

## D. Priority 1:最值得 Codex 立即验证(6 项)

**P1-1|事件内相对份额动量预测胜者**
- Hypothesis:同一注意力事件簇内,早期窗口的 Volume/新买家/流动性**份额动量**对最终胜者的判别力显著高于同期绝对量与发射先后顺序。
- Mechanism:协调博弈收敛(M2)——参与者在猜别人会选哪个 CA,份额变化是收敛过程本身的实时投影。
- Operational Definition:事件簇 = 时间窗 + 名称/元数据相似度聚合的候选集;每 token 每分钟计算三类份额及其一阶差;"胜者" = 事件后 T 时刻存活且市值份额第一(T 取多档,避免单一定义)。
- Data Requirement:仅 DEX/launchpad 交易与池数据;无需任何实体聚类。
- Entity Clustering Dependency:**无**。
- 适用阶段:Early Filter + Transition(事件场景)。
- 预测窗口:5 min–3 h。
- 最大误判来源:事件簇构造错误(把不同注意力池混为一簇);份额被单一大户交易短暂扭曲。
- 为什么现在验证:全表中成本最低、实体依赖为零、且直接检验 M2;若相对份额不比绝对量强,第一轮的协调博弈框架被便宜地证伪。

**P1-2|外部买入份额趋势判别"硬拉 vs 真实扩张"**
- Hypothesis:拉升期间,来自"非已知内部人、非同块狙击"钱包的买入份额持续上升的代币,后续存活/升级概率显著更高;份额停滞的拉升大概率是燃料驱动。
- Mechanism:M1/G3——外部接棒是反身性点火的定义性证据。
- Operational Definition:已知内部人 = deployer 资金图 1 跳 + 创建块接收者 + 同块买入者(Pine 高置信方法);外部买入份额 = 其余钱包买入 quote 占比,取拉升窗口内趋势斜率。
- Data Requirement:交易流 + deployer 出入金 1 跳;点时可得。
- Entity Clustering Dependency:**仅高置信层**(低成本)。漏检偏误方向保守(V4)。
- 适用阶段:Transition Signal。
- 预测窗口:30 min–6 h。
- 最大误判来源:操盘方用未被 1 跳识别的新钱包注资(CEX 中转);把独立老练交易者误当"外部散户"。
- 为什么现在验证:这是第一轮核心观点 1 的直接检验,且是全框架中"恒等式→Alpha"转化最关键的一环;失败则框架需大修。

**P1-3|内部净释放 Flow 优于 Stock(风险侧主假设)**
- Hypothesis:高置信内部集群的净卖出速率与加速度对未来大幅回撤的预测力显著高于其持仓比例;控制 Flow 后 Stock 无增量。
- Mechanism:M4——行为揭示私有信息;Stock 是公共知识。
- Operational Definition:内部集群同 P1-2;净卖出流按窗口聚合,一阶+二阶;对照变量为同时点持仓占比。
- Data Requirement:同 P1-2 + 持仓快照。
- Entity Clustering Dependency:仅高置信层。
- 适用阶段:Risk / Exit。
- 预测窗口:10 min–6 h(回撤事件)。
- 最大误判来源:一次性 rug(无渐进卖出,Flow 无预警——需 LP 撤出事件单独覆盖);内部人通过场外/转账先移仓再卖。
- 为什么现在验证:Stock/Flow 是第一轮最强主张之一,检验便宜,结论直接决定后续数据管道把钱花在快照还是流上。

**P1-4|释放-吸收比的分岔(Exit/确认侧)**
- Hypothesis:内部释放窗口内 T/D 受控(释放被外部流入承接)的代币,**后续**窗口的存活与继续上涨概率显著高于 T/D 失控者;该比值优于释放量绝对值。
- Mechanism:M1/M3 后期——"庄家卖出不必然利空"的严格版。
- Operational Definition:释放窗口 = 内部净卖出超过基线的连续时段;T/D = 窗口内内部净卖出 ÷ 外部净买入;**用窗口结束后的前向收益/存活做因变量**(严禁用同期价格定义吸收,避免同义反复)。
- Data Requirement:同 P1-3。
- Entity Clustering Dependency:仅高置信层。
- 适用阶段:状态确认 + Risk/Exit。**明确不是 Early Filter。**
- 预测窗口:释放窗口后 1–24 h。
- 最大误判来源:接盘方是另一个未识别的协同实体(换庄不是分发);释放窗口切分的任意性。
- 为什么现在验证:直接检验第一轮观点 5;对实盘持仓管理价值最高的单一假设。

**P1-5|外部资金扩散的批次持续性**
- Hypothesis:按到达批次划分的新钱包 quote 净流入中,第二、三批的规模不衰减(或衰减慢)的代币,持续性显著更好;该变量优于 Buyer/Holder Count 且后者在控制它之后无增量预测力(负假设一并检验)。
- Mechanism:M1+M2——反身性的输出就是后续批次;人头数是它的劣质影子。
- Operational Definition:新钱包 = 该 token 首次出现的买家,过资金来源 1 跳过滤(排除 deployer 系与已知批量 funding 源);按首次买入时间分批;批间规模比作为衰减率。
- Data Requirement:交易流 + 钱包首现时间 + funding 1 跳。
- Entity Clustering Dependency:低(1 跳过滤)。
- 适用阶段:Early→Transition。
- 预测窗口:15 min–6 h。
- 最大误判来源:工业化 Sybil 的 funding 源在 1 跳外(CEX 提币直发);批次划分对参数敏感。
- 为什么现在验证:同时检验一个正假设(扩散)和一个高价值负假设(人头计数无增量)——负假设若成立,可以立刻从所有下游产品里删掉 holder/buyer count,节约大量后续注意力。

**P1-6|深度动态与 LP 行为的风险信息**
- Hypothesis:(a) 市值上台阶而池深不同步增长,预测更大回撤;(b) 大 LP 的撤出/迁移事件是一次性 rug 类失败的唯一系统性领先信号(补 P1-3 的盲区)。
- Mechanism:G5/F6——深度错配噎死行情;流动性控制是抽取的前置动作(LIBRA 手法)。
- Operational Definition:池储备与市值的增长率比;LP 添加/移除事件流。
- Data Requirement:池状态序列 + LP 事件;完全公开、无聚类。
- Entity Clustering Dependency:无(LP 地址与 deployer 的 1 跳关联可选做增强)。
- 适用阶段:Risk / Exit。
- 预测窗口:分钟级(LP 事件)至数小时(深度错配)。
- 最大误判来源:迁移到更深场所前的正常过渡(CEX 上线、池升级)被误判为撤出。
- 为什么现在验证:数据最干净、工程最便宜的风险信号;与 P1-3 组合覆盖渐进式与一次性两类退出。

---

## E. Deferred / Downgrade / Delete

### Deferred(理论重要,当前条件不足)
- **Attention Conversion(直接量化)**:需要可靠的社交时序数据与归因;时间戳、删帖、私域(TG 群)不可见都是硬伤。等 P1-1/P1-2 确认链上侧框架后,再决定是否值得买社交数据。
- **Multi-operator Structure(多庄抢跑)**:需要中置信聚类才能区分"几个集群",聚类边界误差会直接翻转结论。理论上是 F5 类失败的关键,但第一阶段测不起。
- **信息源独立性**(买家来自不同 KOL/社群):需要 KOL-wallet attribution,成本最高的数据工程之一。第一阶段用资金独立性(1 跳)替代——V6 判断这已足够启动。
- **Effective Float / Cost Basis 分布**:不依赖聚类(逐钱包交易史即可),但工程量中等且更多作用于中期阻力结构而非小时级决策。P2 排队,不删。
- **Manufactured→Real Conversion**:机制有 UCL 因果证据支持,但洗量识别(flip-score)在 point-in-time 下的稳定性未知,且只覆盖 4% 项目的稀缺行为。作为 P2 观察变量。

### Downgrade(可观察,但大概率只是辅助/Coincident)
- **Buyer/Holder Count 及其增速**:降为 P1-5 的对照变量。若负假设成立则进一步降为纯展示指标。
- **绝对 Volume、Buy/Sell Ratio**:Coincident 且污染重;仅保留在份额计算的分母里。
- **Sniper/Parasite Load(事件内场景)**:BROCCOLI 显示狙击合约对**每个**候选统一征税(同块买走 50%),均匀税负不产生截面判别力;deployer 关联的自狙击仍保留判别价值(进 P1-2 的内部人定义)。单币种场景的寄生税假设(第一轮 H10)降为 P2。
- **Smart Money 跟随**:选择效应已被安慰剂检验重创;仅作为事后归因工具,不进预测变量。
- **Graduation Speed、钱包年龄、KOL 计数**:全部 Coincident 或已被 Goodhart 化;钱包年龄仅保留在外部买入份额的过滤器里。

### Delete(不可测、滞后、或信息增量极低)
- **Reflexivity Gain 的数值估计**:任何 G 的单一数字都是虚假精确。概念保留在叙事层,变量删除;其可测残影已由 P1-5(批次衰减率)承接。
- **"Market Consensus / 共识化"作为指标**:本质滞后(确认时行情早已走完),交易价值≈0。保留为长期存活的事后定义。
- **D>R 作为被检验假设**:恒等式不可证伪。删除;其分解成分(P1-2/3/4)才是假设。
- **Critical Gates 作为指标体系**:G1–G6 是诊断叙事,不是变量。仅 G3(→P1-2)与 G6(→P1-4)有可测化身,其余不再出现在量化讨论中。
- **静态 Top10 集中度作为独立信号**:未聚类的地址集中度既测不准 Stock 也不含 Flow 信息;由"高置信内部持仓+其净流"完全替代。

---

## F. Real Case:BROCCOLI / CZ Dog Event(2025-02-13)

案例适格性:注意力来源单一且明确(CZ 推文)、无官方 CA、数百个同名候选、多版本获得真实交易、胜负分化清晰。缺陷(如实声明):公开报道只有小时级粒度,分钟级份额序列需 Codex 重建;最终收敛受到一个外生制度事件(BNB Chain 流动性扶持计划评分)的干预,不是纯市场选择——但这本身是重要发现而非噪声。判断:**可用,且是目前能找到的最干净的同注意力池竞争案例。**

### Actual Timeline(极简)

| 时间(ET,2025-02) | 事件 |
|---|---|
| 02-13 上午(揭晓前 ~3h) | CZ 预告将发狗照。抢跑期:CLEO、BROWNIE、PERRY 等"猜名"代币冲至数百万美元市值 |
| 02-13 11:12 | CZ 揭晓 "Broccoli",声明不发官方币,但暗示"可能交易成功的那些"、BNB Foundation 可能支持 → 猜名代币瞬间崩溃 |
| 11:15 起 | BSC(Four.meme ~300 个)与 Solana(Pump.fun ~480 个)同时涌现候选;多个代币在极薄池上打出十亿美元级市值瞬时值后立即崩塌 |
| ~11:15–13:00 | 一个狙击合约对 Four.meme 每个新 Broccoli 同块买入 50%,累计获利 $10M+(均匀寄生税) |
| ~13:00(T+2h) | BSC 领先者触及 ~$400M 市值、2 小时 $220M 成交;Solana 最强者仅 ~$5M 市值(却有 $56M 成交)——链级焦点已收敛到 BSC |
| 02-18–19 | BNB Chain Meme 流动性扶持计划评分:两个幸存 Broccoli(714 vs F2B)并列,以成交量决胜,714 获官方流动性注入,伴随社区争议 |

来源:[Decrypt](https://decrypt.co/305834/binance-founder-cz-dog-name-meme-coins)、[CoinDesk](https://www.coindesk.com/business/2025/02/13/cz-s-dog-made-a-killing-for-one-memecoin-creator-and-murdered-everyone-else)、[The Block](https://www.theblock.co/post/340880/sniper-reportedly-nets-10-million-amid-broccoli-memecoin-frenzy-following-czs-dog-reveal)、[Cointelegraph](https://www.tradingview.com/news/cointelegraph:83bdef60b094b:0-dog-eat-dog-drama-erupts-in-bnb-chain-s-broccoli-token-showdown/)

### Earliest Observable Divergence

1. **第一层分化(分钟级,链选择):** 需求几乎立刻向 BSC 集中,尽管 Solana 候选更多(480 vs 300)。焦点线索是公开且事前可读的:CZ/BNB 的身份绑定 + "BNB Foundation 可能支持"的暗示。**这是 Leading 信息(揭晓时刻即可用),且与后续资金份额一致。** Solana 侧 $56M 成交只堆出 $5M 市值——高换手、零留存,纯 PvP 特征,与 BSC 侧形成可观测对照。
2. **第二层分化(~2 小时内,BSC 内部):** 领先者与其余候选的市值/成交份额在 T+2h 已呈数量级差距($400M vs 其余归零或个位数百万)。报道给出的失败者特征:deployer 自铸大仓 + 数分钟内开卖(0x392eb 案例,mint 后 2 分钟卖出)——**内部释放过早是可观测的 Early 淘汰信号**,与 P1-3 方向一致。
3. **第三层分化(数天,714 vs F2B):** 纯市场未能完成最终收敛(两强并存),由平台评分这一**外生协调装置**裁决。含义:Schelling 收敛可以长时间不完全,外部权威(平台、上所、名人转发)常是最后的对称性破缺器——这类事件本身是可监控的 Leading 信号类别。

Leading / Coincident / Lagging 初判(基于可得粒度,待 Codex 重建验证):链级焦点线索 = Leading;早期份额动量 = Leading 候选(粒度不足,unclear);deployer 早期释放 = Leading(负向);Volume/市值绝对量 = Coincident;KOL 讨论、"官方"叙事 = 多为 Lagging(报道显示 KOL 集中讨论发生在领先者确立后)。**Initial trigger(BSC 领先者最初 15 分钟为什么是它):unresolved——公开材料无法区分"最早的 whale 买入"、"deployer 信誉/结构差异"还是随机性,这正是需要链上重建回答的问题。**

### What We Still Don't Know

- 领先者最初 15–30 分钟的买家结构(外部份额、批次、是否有关键 whale)——无公开数据;
- 714 与 F2B 长期并存期间的份额动量是否早已预示官方裁决方向(还是评分真正改变了均衡);
- 均匀狙击税(50% 同块)对各候选的实际浮筹差异——狙击者对不同候选的清仓时点可能不同,这会造成截面差异,未验证;
- 十亿美元级瞬时市值印记有多少来自自成交/自拉(数据未重建)。

### Codex Hypotheses(跨事件验证,4 条)

- **CH1:** 事件簇内,T+15~60min 的成交/新买家份额动量对最终胜者的判别力 > 同期绝对量与发射时间先后。(P1-1 的事件版)
- **CH2:** 事件簇内,deployer 系钱包在首小时内的净卖出(自铸即卖)几乎完全排除该候选获胜;反之,deployer 持仓静止是幸存的必要非充分条件。
- **CH3:** 胜者通常**不是**最早发射的候选;发射时间与获胜概率的关系弱或非单调(先发优势 < 焦点收敛)。
- **CH4:** 存在可编码的"焦点线索"(名称精确匹配、链与事件主体的绑定、平台/权威的早期互动)时,资金份额向线索指向的候选收敛显著更快;无线索事件的收敛更慢、更易多头并存(714/F2B 型)。
- **CH5(负假设):** 事件内均匀施加的狙击税负(同块狙击占比)对候选间胜负无判别力;仅 deployer 关联狙击有判别力。

---

## G. Codex Research Roadmap(Cheap falsification first)

**Phase 0|事件簇 + 纯 DEX 数据(最便宜,先行):**
构建注意力事件簇(名称/元数据/时间窗匹配,不需要任何实体识别)→ 验证 CH1–CH5 与 P1-1、P1-6(a)。同时跑 P1-5 的负假设(holder/buyer count 在 quote 流之后无增量)。
**证伪杠杆:若相对份额动量不优于绝对量、或人头计数仍有稳健增量,第一轮框架的 M2 与指标降级结论被便宜推翻,后续投入全部重新评估。**

**Phase 1|高置信内部人层(1 跳 funding + 创建块 + 同块):**
在 Phase 0 存活的样本框架上加入廉价实体标注 → 验证 P1-2(外部接棒)、P1-3(Flow>Stock)、P1-4(T/D 分岔)、CH2、P1-6(b)。全程用匹配对照设计(按发射时段、初始规模、事件内配对)防选择效应;全程 point-in-time(当时区块重建,禁用回溯标签)。
**证伪杠杆:若外部买入份额趋势不预测存活,M1 的可操作版失败——这是整个框架的核心赌注。**

**Phase 2|仅在 Phase 1 成立后:中置信聚类与结构变量。**
多跳 funding 图、Jito bundle、行为聚类 → Multi-operator Structure、寄生税的单币种版本、成本基础分布、Manufactured→Real 转化差。每个变量先在小样本上评估聚类误差的敏感性,再决定是否全量。

**Phase 3|最后且可选:链下注意力数据。**
只为 Phase 1–2 中幸存且明确需要转化率测量的假设购买/爬取社交时序;KOL-wallet attribution 只在 P1-4 的"接盘方身份"问题被证明关键时才启动。

资源原则:Phase 0 预计消耗全部预算的一小部分,却能推翻或确认框架的一半;任何时候不要为尚未在便宜数据上存活的假设建设昂贵管道。

---

*第一轮完整理论推导与文献综述见 `research/meme-market-mechanism-research.md`;本文件为其审计与收敛结果,两者结论冲突时以本文件为准。*
