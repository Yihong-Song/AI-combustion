# Chemistry reduction using machine learning trained from non-premixed micro-mixing modeling: Application to DNS of a syngas turbulent oxy-flame with side-wall effects

Pe1482ded9f · 2020 · Combustion and Flame

作者：Kaidi Wan; Camille Barnaud; Luc Vervisch; Pascale Domingo

- DOI：[原文入口](https://doi.org/10.1016/j.combustflame.2020.06.008)
- 分类：化学动力学代理、缩减与机理发现 / 代理与缩减
- JCR：**二级来源报告 Q1/Q2，JCR 版本待官方核实**；报告最佳分区 Q1；版本未知；官方核实：否。
- 阅读深度：已核对元数据与上游 README，尚未完成全文精读。
- 完整期刊论文复现：**尚未验收**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../01_chemistry_kinetics/README.md) · [全局地图](../../../00_literature_map/README.md)

分区线索：[二级来源](https://www.letpub.com/index.php?page=journalapp&view=detail&journalid=1901)。多类别期刊使用报告中的最佳类别作为候选信号，不能解释为所有类别均为 Q1。

## 研究问题

从非预混微混合模型生成训练状态，缩减合成气湍流氧燃烧化学。

## 方法与代码所能确认的内容

ORCh README 的 ANN/CNN 相关工作明确列本文；工具包含化学优化、缩减与神经学习流程，但该 2023 版本不是已确认的 2020 论文快照。

## 复现入口与依赖

按 ORCh 环境与案例说明定位采样、缩减和 ANN/CNN 模块；先核对同一合成气机理与微混合设置。

## 环境与数据

旧 Cantera 2.4、SUNDIALS、Eigen、OpenCV、MPI、HDF5 及编译工具，路径集中配置，历史环境需隔离。

## 建议验证协议（本库设计）

独立留出壁面与混合状态，对比详细化学、传统缩减和学习缩减，报告火焰/壁面相互作用、组分和热释放。

## 局限与当前状态

BSD-3-Clause；相关工作引用不代表原文训练数据和全部 DNS 案例已收纳。

## 代码溯源

- 仓库：[beroudiauxa/ORCh_2023](https://github.com/beroudiauxa/ORCh_2023)
- 固定提交：`1a1b5175078340cbd4585f0ef597a821aa262de4`
- 关系证据：`author_related_work_readme_explicit`；来自上游 README，不代表本库已做作者身份独立认证。
- 许可：BSD-3-Clause；收纳状态：`partial_source_snapshot_collected`。
- [代码包卡片](../../../code_packages/beroudiauxa__ORCh_2023/README.md)

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1016/j.combustflame.2020.06.008)；本轮整理日期 2026-11-12。完整元数据见同目录 `paper.json`。
