# Machine learning-enabled analysis of product distribution and composition in biomass-coal co-pyrolysis

P772b607a19 · 2024 · Fuel

作者：Alireza Shafizadeh; Hossein Shahbeik; Shahin Rafiee; Zahra Fardi; Keikhosro Karimi; Wanxi Peng; Xiangmeng Chen; Meisam Tabatabaei; Mortaza Aghbashlo

- DOI：[原文入口](https://doi.org/10.1016/j.fuel.2023.129464)
- 分类：固体燃料、热解与火灾安全 / 生物质、煤、热解与火灾
- JCR：**二级来源报告 Q1/Q2，JCR 版本待官方核实**；报告最佳分区 Q1；版本未知；官方核实：否。
- 阅读深度：标题与元数据筛选，待摘要/全文复核。
- 论文原始指标复现：**未执行**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../08_solid_fuels_fire/README.md) · [全局地图](../../../00_literature_map/README.md)

分区线索：[二级来源](https://www.letpub.com/index.php?page=journalapp&view=detail&journalid=2950)。多类别期刊使用报告中的最佳类别作为候选信号，不能解释为所有类别均为 Q1。

## 这条记录目前能说明什么

标题和期刊元数据表明它可能属于本方向；本卡不提供未经全文核实的架构、数据量、速度提升或结论。下列内容是该方向的阅读问题与复现设计，不是对本文结果的转述。

## 精读与复现提取清单

1. 明确本文的物理目标：对象是 TGA 动力学、燃料分类、火蔓延、热释放率还是电池热失控？热解产率与燃烧过程存在联系，但不属于同一验证任务。
2. 提取数据生成/测量协议：TGA/DSC、升温速率、气氛、燃料组成、热流与火焰图像；记录原始实验来源与批次。
3. 对照原文确认切分：按燃料种类、实验批次、升温速率或火场划分；相同配方多次采样不是独立材料。
4. 找到原文表/图及指标定义：质量/失重速率、热流、点火时间、HRR 曲线、蔓延速度；安全模型需报告预测区间和漏警，不能只报平均 R2。
5. 记录完整依赖、机理/数据许可证、随机种子、设备、训练预算和失败运行。
6. 建立公式—代码对应表，先运行最小基线，再对同一数据切分复现目标图表。

## 代码检索状态

`searched_no_confirmed_match`。DOI 精确 GitHub README 检索会漏掉未写 DOI 的实现；搜到引用也不能认定为本文代码。未确认实现不意味着作者没有开源。

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1016/j.fuel.2023.129464)；本轮整理日期 2026-11-11。完整元数据见同目录 `paper.json`。
