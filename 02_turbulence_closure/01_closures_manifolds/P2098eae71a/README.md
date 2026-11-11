# High-resolution reconstruction of turbulent flames from sparse data with physics-informed neural networks

P2098eae71a · 2024 · Combustion and Flame

作者：Shiyu Liu; Haiou Wang; Jacqueline H. Chen; Kun Luo; Jianren Fan

- DOI：[原文入口](https://doi.org/10.1016/j.combustflame.2023.113275)
- 分类：湍流燃烧闭合与流形模型 / 闭合、PDF 与热化学流形
- JCR：**二级来源报告 Q1/Q2，JCR 版本待官方核实**；报告最佳分区 Q1；版本未知；官方核实：否。
- 阅读深度：标题与元数据筛选，待摘要/全文复核。
- 完整期刊论文复现：**尚未验收**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../02_turbulence_closure/README.md) · [全局地图](../../../00_literature_map/README.md)

分区线索：[二级来源](https://www.letpub.com/index.php?page=journalapp&view=detail&journalid=1901)。多类别期刊使用报告中的最佳类别作为候选信号，不能解释为所有类别均为 Q1。

## 这条记录目前能说明什么

标题和期刊元数据表明它可能属于本方向；本卡不提供未经全文核实的架构、数据量、速度提升或结论。下列内容是该方向的阅读问题与复现设计，不是对本文结果的转述。

## 精读与复现提取清单

1. 明确本文的物理目标：目标是滤波反应率、标量耗散率、PDF/FDF、混合时间尺度，还是火焰面褶皱？必须先说明滤波算子与可用输入。
2. 提取数据生成/测量协议：DNS 三维瞬时场、空间滤波结果、LES 解析量；可结合 BLASTNet 与 aPrioriDNS。保存滤波核、核宽、Favre/普通滤波、网格间距和化学机理。
3. 对照原文确认切分：按 DNS 工况、独立时间段和燃料划分；空间相邻小块不得随机跨集合。另测未见滤波宽度、Ka/Da/Re。
4. 找到原文表/图及指标定义：源项条件均值、联合 PDF、标量耗散、火焰位置与刷厚、热释放率、能谱、LES 稳定性和总体成本；相关系数不足以取代物理量。
5. 记录完整依赖、机理/数据许可证、随机种子、设备、训练预算和失败运行。
6. 建立公式—代码对应表，先运行最小基线，再对同一数据切分复现目标图表。

## 代码检索状态

`searched_no_confirmed_match`。DOI 精确 GitHub README 检索会漏掉未写 DOI 的实现；搜到引用也不能认定为本文代码。未确认实现不意味着作者没有开源。

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1016/j.combustflame.2023.113275)；本轮整理日期 2026-11-12。完整元数据见同目录 `paper.json`。
