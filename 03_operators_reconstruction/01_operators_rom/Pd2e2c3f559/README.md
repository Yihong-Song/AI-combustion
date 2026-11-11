# Learning transient evolution of multidimensional reacting flows by multiscale Fourier neural operators

Pd2e2c3f559 · 2024 · Proceedings of the Combustion Institute

作者：Hao Zhang; Yuting Weng; Zhiwei Zhao; Dezhi Zhou

- DOI：[原文入口](https://doi.org/10.1016/j.proci.2024.105714)
- 分类：神经算子、降阶与流场重建 / 算子、降阶与超分辨率
- JCR：**二级来源报告 Q1/Q2，JCR 版本待官方核实**；报告最佳分区 Q1；版本未知；官方核实：否。
- 阅读深度：标题与元数据筛选，待摘要/全文复核。
- 完整期刊论文复现：**尚未验收**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../03_operators_reconstruction/README.md) · [全局地图](../../../00_literature_map/README.md)

分区线索：[二级来源](https://www.letpub.com/journal-selector/journal/6861)。多类别期刊使用报告中的最佳类别作为候选信号，不能解释为所有类别均为 Q1。

## 这条记录目前能说明什么

标题和期刊元数据表明它可能属于本方向；本卡不提供未经全文核实的架构、数据量、速度提升或结论。下列内容是该方向的阅读问题与复现设计，不是对本文结果的转述。

## 精读与复现提取清单

1. 明确本文的物理目标：学习的是一个固定网格的映射还是跨输入函数的算子？超分辨率的细节是否由观测约束，还是模型生成？
2. 提取数据生成/测量协议：时序 DNS/LES、参数化一维火焰、低高分辨率配对场。明示插值、滤波和下采样流程，保留物理坐标。
3. 对照原文确认切分：留出完整模拟、参数区间、网格分辨率和几何。若声称零样本分辨率迁移，应另测从未训练的网格。
4. 找到原文表/图及指标定义：场相对 L2、梯度和界面误差、谱、结构函数、守恒、极端放热、长时滚动；仅看 PSNR 或漂亮图像不够。
5. 记录完整依赖、机理/数据许可证、随机种子、设备、训练预算和失败运行。
6. 建立公式—代码对应表，先运行最小基线，再对同一数据切分复现目标图表。

## 代码检索状态

`searched_no_confirmed_match`。DOI 精确 GitHub README 检索会漏掉未写 DOI 的实现；搜到引用也不能认定为本文代码。未确认实现不意味着作者没有开源。

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1016/j.proci.2024.105714)；本轮整理日期 2026-11-12。完整元数据见同目录 `paper.json`。
