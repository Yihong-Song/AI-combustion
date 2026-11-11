# A reinforcement-learning-augmented liquid-fueled reactor network model for predicting lean blowout in gas turbine combustors

P3ecd14877e · 2026 · Proceedings of the Combustion Institute

作者：Philip John; Eloghosa Ikponmwoba; Pinaki Pal; Opeoluwa Owoyele

- DOI：[原文入口](https://doi.org/10.1016/j.proci.2026.106463)
- 分类：发动机、燃烧器与复杂推进系统设计 / 控制与多目标设计
- JCR：**二级来源报告 Q1/Q2，JCR 版本待官方核实**；报告最佳分区 Q1；版本未知；官方核实：否。
- 阅读深度：标题与元数据筛选，待摘要/全文复核。
- 完整期刊论文复现：**尚未验收**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../07_engineering_design/README.md) · [全局地图](../../../00_literature_map/README.md)

分区线索：[二级来源](https://www.letpub.com/journal-selector/journal/6861)。多类别期刊使用报告中的最佳类别作为候选信号，不能解释为所有类别均为 Q1。

## 这条记录目前能说明什么

标题和期刊元数据表明它可能属于本方向；本卡不提供未经全文核实的架构、数据量、速度提升或结论。下列内容是该方向的阅读问题与复现设计，不是对本文结果的转述。

## 精读与复现提取清单

1. 明确本文的物理目标：预测/优化目标是什么，约束来自哪里？发动机排放回归、几何优化、喷雾与超声速燃烧需要不同保真度与验证手段。
2. 提取数据生成/测量协议：台架测量、CFD 参数扫描、喷雾图像、壁压与烟膜；保留工况、传感器、重复试验和数据来源。
3. 对照原文确认切分：按负荷、转速、喷油策略或几何留出，超参数选择使用训练内验证；重复试验归入同组。
4. 找到原文表/图及指标定义：效率/油耗、NOx/CO/烟炱、压损、稳定裕度、推力与不确定度；优化必须报告高保真复核结果，不能只报代理预测的最优点。
5. 记录完整依赖、机理/数据许可证、随机种子、设备、训练预算和失败运行。
6. 建立公式—代码对应表，先运行最小基线，再对同一数据切分复现目标图表。

## 代码检索状态

`searched_no_confirmed_match`。DOI 精确 GitHub README 检索会漏掉未写 DOI 的实现；搜到引用也不能认定为本文代码。未确认实现不意味着作者没有开源。

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1016/j.proci.2026.106463)；本轮整理日期 2026-11-12。完整元数据见同目录 `paper.json`。
