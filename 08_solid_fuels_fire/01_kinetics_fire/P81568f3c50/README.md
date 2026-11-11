# Comprehensive thermal-kinetic uncertainty quantification of lithium-ion battery thermal runaway via bayesian chemical reaction neural networks

P81568f3c50 · 2025 · Chemical Engineering Journal

作者：Benjamin C. Koenig; Peng Zhao; Sili Deng

- DOI：[原文入口](https://doi.org/10.1016/j.cej.2025.160402)
- 分类：固体燃料、热解与火灾安全 / 生物质、煤、热解与火灾
- JCR：**二级来源报告 Q1/Q2，JCR 版本待官方核实**；报告最佳分区 Q1；版本未知；官方核实：否。
- 阅读深度：已核对元数据与上游 README，尚未完成全文精读。
- 论文原始指标复现：**未执行**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../08_solid_fuels_fire/README.md) · [全局地图](../../../00_literature_map/README.md)

分区线索：[二级来源](https://www.letpub.com/index.php?page=journalapp&view=detail&journalid=1639)。多类别期刊使用报告中的最佳类别作为候选信号，不能解释为所有类别均为 Q1。

## 研究问题

将 Bayesian CRNN 用于锂电热失控的热—动力学不确定度传播。

## 方法与代码所能确认的内容

README 明确列出本文为 cathode UQ 系列工作。模型不确定性传播与单条实验曲线拟合应分别评价。

## 复现入口与依赖

从对应 cathode/thermal runaway 子项目、项目环境与输入数据开始，按论文识别具体图表。

## 环境与数据

Julia 子项目环境；采样/优化设置和计算预算需从论文及配置核对。

## 建议验证协议（本库设计）

校准与验证实验分离，报告预测区间覆盖、热失控起始条件和敏感性；不只比较后验均值。

## 局限与当前状态

扩展到电池安全范围，不能与气相火焰精度直接横向排名。尚未执行论文结果。

## 代码溯源

- 仓库：[DENG-MIT/CRNN](https://github.com/DENG-MIT/CRNN)
- 固定提交：`4a17819c5bd4a65d6a9da9e72115b536d644350e`
- 关系证据：`author_implementation_readme_explicit`；来自上游 README，不代表本库已做作者身份独立认证。
- 许可：MIT；收纳状态：`partial_source_snapshot_collected`。
- [代码包卡片](../../../code_packages/DENG-MIT__CRNN/README.md)

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1016/j.cej.2025.160402)；本轮整理日期 2026-11-11。完整元数据见同目录 `paper.json`。
