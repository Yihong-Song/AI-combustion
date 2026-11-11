# Inferring unknown unknowns: Regularized bias-aware ensemble Kalman filter

P0783e678e5 · 2024 · Computer Methods in Applied Mechanics and Engineering

作者：Andrea Nóvoa; Alberto Racca; Luca Magri

- DOI：[原文入口](https://doi.org/10.1016/j.cma.2023.116502)
- 分类：热声不稳定性预测、辨识与控制 / 预警与系统辨识
- JCR：**二级来源报告 Q1/Q2，JCR 版本待官方核实**；报告最佳分区 Q1；版本未知；官方核实：否。
- 阅读深度：已核对元数据与上游 README，尚未完成全文精读。
- 完整期刊论文复现：**尚未验收**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../04_instability_control/README.md) · [全局地图](../../../00_literature_map/README.md)

分区线索：[二级来源](https://www.letpub.com/journal-selector/journal/1988)。多类别期刊使用报告中的最佳类别作为候选信号，不能解释为所有类别均为 Q1。

## 研究问题

在热声等动力系统同化中，同时处理状态不确定性与未知模型偏差。

## 方法与代码所能确认的内容

README 明确指定本文 DOI，并说明正则化偏差感知集合 Kalman 方法的实现及勘误。该通用方法在本库按热声应用阅读。

## 复现入口与依赖

先读仓库 Erratum.pdf 与实现，再定位热声配置；新维护版入口为 andreanovoa/real-time-bias-aware-DA。

## 环境与数据

固定旧版依赖与对应实验设置；新版 API、模块布局和默认参数已变化，不能混用。

## 建议验证协议（本库设计）

同一观测噪声和集合预算下比较不校正偏差、普通 EnKF 与正则偏差校正，报告状态误差、偏差估计和稳定性。

## 局限与当前状态

MIT。README 明说原文式(15)–(16)有排版错误，仓库及勘误为更正依据；必须在复现报告中说明。

## 代码溯源

- 仓库：[MagriLab/rBA-EnKF](https://github.com/MagriLab/rBA-EnKF)
- 固定提交：`641e422240f360300dcbd6fe6d543da358ece74c`
- 关系证据：`author_implementation_readme_explicit`；来自上游 README，不代表本库已做作者身份独立认证。
- 许可：MIT；收纳状态：`source_archive_collected`。
- [代码包卡片](../../../code_packages/MagriLab__rBA-EnKF/README.md)

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1016/j.cma.2023.116502)；本轮整理日期 2026-11-12。完整元数据见同目录 `paper.json`。
