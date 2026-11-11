# A real-time digital twin of azimuthal thermoacoustic instabilities

P0e5f9b5e09 · 2024 · Journal of Fluid Mechanics

作者：Andrea Nóvoa; Nicolas Noiray; James R. Dawson; Luca Magri

- DOI：[原文入口](https://doi.org/10.1017/jfm.2024.1052)
- 分类：热声不稳定性预测、辨识与控制 / 预警与系统辨识
- JCR：**JCR 分区待核实**；报告最佳分区 未知；版本未知；官方核实：否。
- 阅读深度：已核对元数据与上游 README，尚未完成全文精读。
- 完整期刊论文复现：**尚未验收**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../04_instability_control/README.md) · [全局地图](../../../00_literature_map/README.md)

## 研究问题

为环形燃烧室方位热声不稳定性构建随观测更新的数字孪生。

## 方法与代码所能确认的内容

固定 README 的 Journal papers 明确列本文 DOI，并指定 v1.0 发布版；当前代码已重构为 romda，提供物理模型、ESN 偏差模型及同化方法。

## 复现入口与依赖

先定位 v1.0，再核对 examples/thermoacoustics 及相应配置；当前 tutorials 的热声章节用于理解软件。

## 环境与数据

Python 项目环境及 romda 所列 biasda/dynamodels 等依赖；实验信号和结果目录可能从外部取得，需逐项核实。

## 建议验证协议（本库设计）

按不同实验爬升或工况留出，比较模态幅值、方位结构、参数后验、预测提前量与实时计算成本。

## 局限与当前状态

MIT；主分支固定提交与论文 v1.0 不同，正式复现须补 v1.0 的准确提交。未执行。

## 代码溯源

- 仓库：[andreanovoa/real-time-bias-aware-DA](https://github.com/andreanovoa/real-time-bias-aware-DA)
- 固定提交：`10d0a01fae5adf3c5e659231e9d4c0c2e68bce6a`
- 关系证据：`author_implementation_readme_explicit`；来自上游 README，不代表本库已做作者身份独立认证。
- 许可：MIT；收纳状态：`partial_source_snapshot_collected`。
- [代码包卡片](../../../code_packages/andreanovoa__real-time-bias-aware-DA/README.md)

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1017/jfm.2024.1052)；本轮整理日期 2026-11-12。完整元数据见同目录 `paper.json`。
