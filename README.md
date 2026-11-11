# AI + Combustion｜燃烧人工智能文献与代码库

面向燃烧、反应流和热安全研究的中文研究入口：按 **物理方向 → 子方向 → 论文** 组织文献，收纳可追溯的代码，并保留真实实验结果。优先关注新方法，同时保留理解新方法需要的经典路线。

**整理日期：2026-11-11。只采用 JCR 分区。** 本轮没有取得版本明确的官方 JCR 记录，因此以下是候选库，不能把全部条目称为“已确认一区/二区”。多数论文仍处于题名/元数据筛选阶段；详细状态见每张论文卡。

## 本轮规模与完成度

| 项目 | 数量 | 解释 |
|---|---:|---|
| 检索命中 / DOI 去重记录 | 3775 / 2692 | 保留检索式、时间与排除原因 |
| AI×燃烧及相邻热转化候选 | 428 | 不是全部已精读或有代码 |
| 2024–2026 年候选 | 238 | 年份来自 Crossref published |
| 二级来源报告 Q1/Q2 | 368 | JCR 版本待官方核实 |
| 分区待核实 | 49 | 单独排队，不默认 Q1 |
| 二级来源 Q3/Q4 附录 | 11 | 不纳入候选主目录 |
| 已核对论文—代码链接 | 27 | 含实现、支撑组件及教程，关系逐篇区分 |
| 代码/支撑工具仓库 | 52 | 一仓库多文只计一个包 |
| 明确可再分发许可 / 已附源归档 | 29 / 16 | 其余为固定链接或许可受限 |
| 已附部分源码快照 | 13 | 不包含完整数据/权重，另记数量 |
| 已执行独立基线 / 原文指标复现 | 2 / 0 | 不将独立基线冒充论文复现 |
| 已执行作者演示 | 1 | 固定版本和原始数据推理，未重训 |

统计源：[stats.json](catalog/stats.json)。这是有检索边界的一轮整理，没有数量上限，但也没有证明覆盖所有文献。OA 论文、可见源码、有许可代码、数据权重齐备和复现成功分别记录。

## 从哪里开始

1. **快速建立全景**：[思维导图和阅读路线](00_literature_map/README.md)，再看 [方法×物理问题矩阵](00_literature_map/METHOD_PROBLEM_MATRIX.md)。
2. **找论文**：[全部论文索引](00_literature_map/ALL_PAPERS.md)、[2024–2026 新文献](00_literature_map/RECENT_2024_2026.md)、[本地交互检索页](00_literature_map/explorer.html)。交互页下载后用浏览器打开，GitHub 页面本身只显示源码。
3. **找可操作的代码**：[代码包清单](code_packages/README.md) 和 [已核对论文代码路线](00_literature_map/CODE_READING_ROUTE.md)。
4. **跑透明的最小实验**：[B01 氢气点火代理](reproductions/B01_hydrogen_ignition/README.md) 与 [B02 Bratu PINN](reproductions/B02_bratu_pinn/README.md)。
5. **开展正式复现**：先读 [复现协议](docs/REPRODUCTION_PROTOCOL.md)，明确原文图表、数据、切分和指标，再推进训练。

初次接触这些方法，可先读 [术语、指标与论文阅读指南](docs/GLOSSARY.md)，理解 PINN、LES、神经算子和误差数字的实际含义。

已执行的上游期刊代码：[C01 氨燃烧 PINN-WSGG 辐射演示](reproductions/C01_wsgg_author_demo/README.md)，含逐点数值、误差定义和适配说明。

## 大方向导航

| 目录 | 研究问题 | 候选数 |
|---|---|---:|
| [化学动力学代理、缩减与机理发现](01_chemistry_kinetics/README.md) | 把每个网格里昂贵的化学计算变快，同时尽量保留点火、放热和污染物的正确性。 | 96 |
| [湍流燃烧闭合与流形模型](02_turbulence_closure/README.md) | 大涡模拟看不清所有小火焰结构，需要模型补上未解析尺度对反应和混合的影响。 | 24 |
| [神经算子、降阶与流场重建](03_operators_reconstruction/README.md) | 从少量状态、低分辨率场或参数，预测完整流场及其演化，减少重复高保真模拟。 | 13 |
| [热声不稳定性预测、辨识与控制](04_instability_control/README.md) | 识别火焰放热与声波之间的正反馈，在振荡扩大前预警或采取控制。 | 18 |
| [光学诊断、反演、烟炱与辐射](05_diagnostics_radiation/README.md) | 让光谱和图像提供更可靠的温度、组分和三维场信息，并加速参与性介质辐射计算。 | 47 |
| [物理信息学习与可微燃烧求解](06_physics_informed/README.md) | 把守恒方程和边界条件加入模型，使稀疏数据下的正问题和逆问题更有物理约束。 | 9 |
| [发动机、燃烧器与复杂推进系统设计](07_engineering_design/README.md) | 用代理、优化和控制在效率、排放、稳定性和成本之间寻找可用工况。 | 73 |
| [固体燃料、热解与火灾安全](08_solid_fuels_fire/README.md) | 从热分析到火焰图像，研究固体如何分解、着火、放热，以及怎样预测火灾风险。 | 83 |
| [氢氨燃料、着火与燃料性质预测](09_fuels_properties/README.md) | 从分子结构或工况预测着火、火焰速度和燃料性质，为低碳燃料选择提供依据。 | 42 |
| [综述、数据集与共性方法](10_reviews_methods/README.md) | 先建立全局坐标，再沿具体物理问题阅读；数据和评价协议同模型一样重要。 | 12 |

每个方向的 README 包括核心问题、方法演进、数据、评价指标、切分、局限和建议阅读顺序。子方向目录包含论文列表；每篇 `README.md` 与 `paper.json` 保存 DOI、作者、来源、分区状态、代码证据和复现待办。交叉方法用交互页检索；自动分类需在精读时继续修订。

## 目录结构

```text
00_literature_map/              全景图、矩阵、逐方向文献表、交互浏览器
01_chemistry_kinetics/          方向 → 子方向 → DOI 稳定 ID → README/paper.json
02_turbulence_closure/ ...      其余九个研究方向
code_packages/                 固定提交、许可、包说明与可收纳源归档
reproductions/                 独立基线/后续复现实验、原始输出与环境
catalog/                       JSON、UTF-8 CSV、BibTeX、期刊与统计
literature/curation.json        人工核对的代码论文说明与分类覆盖
literature/adjacent/            Q3/Q4 线索附录，不计入主方向候选
evidence/                      检索、排除、分区、上游与代码搜索证据
docs/                          范围、许可、方法与复现规范
tools/                         检索、建库、下载、校验和维护脚本
```

## 本地使用

```powershell
git clone https://github.com/Yihong-Song/AI-combustion.git
cd AI-combustion
python -m pip install -r requirements-tools.txt
python tools/validate.py
python tools/fetch_packages.py
```

离线重建、扩充检索和逐文复现步骤见 [维护指南](docs/MAINTENANCE.md)；[本地校验报告](evidence/validation.json)记录实际检查范围。

科学基线需另装 `requirements-baselines.txt`。历史代码应使用各自环境，不能将旧 TensorFlow、Julia、OpenFOAM 依赖混装在同一环境。源归档只下载不自动运行。

## 数据下载与引用

- [papers.csv](catalog/papers.csv) / [papers.json](catalog/papers.json)：全部候选和完整状态。
- [Q1/Q2 二级线索候选](catalog/q1_q2_provisional.csv) / [分区待核实](catalog/pending_jcr.csv) / [Q3/Q4 附录](catalog/adjacent_q3_q4.csv)。
- [BibTeX](catalog/references.bib)：用于导入文献管理器，题名、作者、年份仍需在投稿前核对出版商；保留候选注记。
- [期刊分区证据表](00_literature_map/JCR_EVIDENCE.md)：逐期刊保留类别与来源。

引用研究结论时应引用原论文，使用代码时按上游要求引用论文并遵守许可。本库没有转载付费全文，没有将二级分区网页当作官方证明。

## 当前局限与后续维护

题名筛选会漏掉摘要才出现 AI 的论文，也会保留需进一步审查的热解/燃料性质边界条目。Crossref、GitHub、分区网页覆盖有限，网络失败和查询数量上限均会造成遗漏。已核对代码论文的说明主要依据元数据和 README，尚未完成全部原文精读。当前不应将本库直接作为“所有 Q1/Q2 文献”或全面系统综述的结论依据。

下一阶段优先补官方 JCR 版本、全文提取、数据与权重核验，然后按同口径协议复现目标图表。[方法全文](docs/METHODOLOGY.md) · [代码收纳与许可](docs/CODE_COLLECTION.md) · [建设记录](PLAN.md)。
