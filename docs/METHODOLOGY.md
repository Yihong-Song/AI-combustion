# 检索、证据与纳入方法

整理截止：2026-11-12。主要检索窗口为 2018-01-01 至截止日；必要的更早方法通过代码工具卡补充。这里只采用 **JCR / Journal Impact Factor 类别分区**，不把中科院分区、SJR、JCI 或影响因子高低换算成 JCR。

## 先读这个边界

本库是可追溯的文献候选库、代码索引和实验起点，**不是已完成全文精读的系统综述，也没有证明穷尽所有文献**。候选论文数、具有代码的论文数、代码包数、实际运行数、原文指标复现数是五种不同统计。OA 全文、公开 GitHub 和有合法再分发许可也不是同一条件。

本轮没有取得可验证年份的 Clarivate JCR 官方条目，因此“官方已确认 Q1/Q2”数为 0。LetPub 的 JIF 分区表作为二级线索保存；无法辨明 JCR 版本时留空，不能从网页访问日期或其他年份推断版本。主目录中的 Q1/Q2 均为**待官方核实的候选**。

## 研究范围

- 反应动力学、湍流燃烧、热声、诊断、辐射、燃料性质、发动机/燃烧器、喷雾与爆轰。
- 生物质热解、煤、火灾、电池热失控作为相邻热转化/安全方向，逐篇复核与燃烧的联系。
- 通用可微化学、Neural ODE、数据访问软件以支撑工具形式收纳；会议和预印本不赋 JCR 分区。
- 按用户范围排除全球/大区域野火扩散、遥感火点、灾情及气候分析；保留实验室火焰、反应机理、建筑火灾及装置研究。标题含这些词而被排除的记录保存原因供复核。
- 排除明确的燃料电池、制氢生产、燃烧后碳捕集、与燃烧无关的加氢脱硫/脱氮及部分综合能源系统。
- 自动标题筛选仍可能纳入生物油生产、燃料材料等边界文章；候选身份不等于最终纳入。`catalog/papers.json` 的 screening 字段保留此限制。

## 检索通道与可复查记录

1. Crossref 元数据：宽检索与燃烧核心期刊 ISSN 限定检索，关键词包括 machine learning、neural network、physics informed、neural operator、transformer、GNN、reinforcement learning、flame tomography、chemical kinetics 等。
2. GitHub：领域关键词仓库检索、逐 DOI 的 README 精确搜索、研究组代码及 README 引用追溯。
3. JCR 线索：LetPub 的 **Quartiles By JIF** 区块；保存期刊身份、类别、排名、分区、来源 URL 和时间。
4. 直接 DOI 补充：对上游明确引用、但宽检索遗漏的核心工作查询 Crossref DOI 端点。

具体查询 URL、时间、返回量和排除原因见 [screening.json](../evidence/screening.json)。逐 DOI 代码搜索在 `evidence/code_search/`；上游版本证据在 `evidence/upstream/`；期刊证据在 `evidence/journals/`。原始网页/README 缓存不进入 Git，避免复制大量版权正文；可从记录中的固定 URL 复查。

检索包含每次请求的数量上限，未对每一查询完整翻页；Fuel 的一次深度检索遇到 HTTP 429。Crossref 覆盖、索引延迟、题名关键词与期刊白名单都会造成遗漏。没有在标题写 AI、摘要才说明方法或仅在补充材料开放代码的工作可能漏掉。未使用 Web of Science/Scopus 完整检索导出，因此不宣称 PRISMA 意义的完整系统检索。

## 去重与分类

DOI 转小写后精确去重；一文多次命中只计一次。ID 为 DOI 的 SHA-256 前 10 位加 P，便于路径稳定且控制 Windows 路径长度。出版年份采用 Crossref `published` 字段，可能与在线年份、卷期年份及 DOI 中年份不同，引用前应核对出版商。

分类优先看物理任务，再看方法。PINN、算子、CNN 等跨方向方法可用总库题名搜索；自动分类不是作者对文章的正式定位。已核对论文可以在 `literature/curation.json` 中覆盖分类。同一个代码仓库对应多篇论文时，论文分别计数、包只计一次。

## 分区分层

| 状态 | 含义 | 使用方式 |
|---|---|---|
| provisional_q1_q2 | 二级来源报告最佳 JIF 类别 Q1/Q2，但版本及官方证据不完整 | Q1/Q2 候选，不作已认证清单 |
| pending_jcr | 未取得有效分区，期刊身份不匹配或表格可疑 | 单独待核实，不能默认为 Q1 |
| adjacent_q3_q4 | 二级来源报告 Q3/Q4 | 从候选主目录移入相邻附录 |

多类别期刊没有唯一不随类别变化的分区。例如同一期刊可在机械工程 Q1、能源与燃料 Q2/Q3。这里的“最佳类别”只是候选筛选规则，不能说它在 Energy & Fuels 一定为一区。正式定稿应选定一个 JCR 版本，逐类列出，并说明采用最佳类别还是燃烧相关类别。历史论文不自动拥有发表当年的相同分区。

Applications in Energy and Combustion Science 的二级表存在与其他期刊类别/排名相似的可疑情况，本轮保持 pending。Combustion Science and Technology 与 Combustion Theory and Modelling 的当前二级线索为 Q3，故不计入 Q1/Q2 候选。

## 阅读深度与结论强度

| 等级/字段 | 已完成内容 | 不能声称 |
|---|---|---|
| title_screen_only_fulltext_pending | 题名、作者、期刊、DOI、分类候选 | 已精读、已核实架构和文章结论 |
| metadata_and_upstream_readme | 以上内容及上游 README—论文对应、入口/依赖线索 | 已完成全文审查或原文复现 |
| source_archive_collected | 固定提交源码归档、许可证与 SHA-256 | 数据权重齐全、可直接运行 |
| smoke/demo executed | 指定命令执行和产物已核验 | 训练结果或原文表格已复现 |
| independent baseline executed | 自行设计的透明基线，实际运行 | 对应论文原始实验已复现 |
| paper metrics reproduced | 相同数据/切分/指标/预算下原文图表对照 | 需实际比较表和偏差分析后才使用 |

论文卡中的“建议验证协议”是本库设计，非原文声称的实验。没有全文证据时不填造数据量、超参数、加速倍数、SOTA 排名或研究空白。

## 论文—代码关系

- `author_implementation_readme_explicit`：上游明确写本论文及 DOI/题名；保留固定 README 来源。未对 GitHub 账户与作者身份做独立认证。
- `author_related_work_readme_explicit`：作者软件生态的 Related papers 明确列该论文，或后续工具 README 明确相关引用；不等于本篇全部实验代码已提供。
- `title_match_repository_readme`：题名相符但未见明确 DOI 归属，证据较弱。
- `supporting_tool`：有用的支撑软件，不假定是某篇期刊的完整官方实现。
- `author_supporting_component_readme_explicit` / `author_supporting_tool_readme_explicit`：README 明确连接论文，但仅确认数据构建、通用处理等组件，不能当作完整实验代码。
- `author_supporting_tutorial_readme_explicit`：论文关联的数据教程，不是目标模型的训练复现。
- `repository_reference_readme_explicit`：仓库明确引用 DOI，但没有独立的作者归属或完整实验声明；证据低于明确补充材料。
- `search_hits_unverified`：DOI 搜到仓库，但可能只是参考文献；不能当作作者代码。
- `searched_no_confirmed_match`：这一种搜索没有确认结果，不能据此宣布“未开源”。

已发现 DeepLearningFire 等搜索命中只是引用目标论文，未建立其为原文实现的关系，因此不作为该论文代码收纳。

BioOil-Automation 明确引用 Fuel 10.1016/j.fuel.2021.122812 作为二手建模的数据来源，也不归作该文的作者实现。MDDatasetBuilder 则明确连接两篇神经势/主动学习工作，但只作为数据构建组件收纳。

## 维护与复现

```powershell
python tools/discover.py
python tools/expand_search.py
python tools/expand_depth.py
python tools/add_key_papers.py
python tools/screen.py
python tools/search_paper_code.py
python tools/build_catalog.py
python tools/build_overview.py
python tools/validate.py
```

请求有本地缓存；不要为相同 URL 无限制重试。上游检视和下载分开，下载不自动执行。科研复现使用各论文独立环境，不把旧 TensorFlow、Julia、OpenFOAM 与当前 Python 基线环境混装。

未来精读时，每文补齐：研究假设、实验对象/边界、数据来源、公式—代码映射、指标定义、对照与消融、误差/置信区间、计算预算、失败条件、适用域，以及原文页码/表号和代码行对应证据。
