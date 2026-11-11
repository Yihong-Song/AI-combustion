# Advancing Sustainable Aviation Fuel Design: Machine Learning for High-Energy-Density Liquid Polycyclic Hydrocarbons

Pca19045ded · 2025 · Energy & Fuels

作者：Dilip Rijal; Vladislav Vasilyev; Feng Wang

- DOI：[原文入口](https://doi.org/10.1021/acs.energyfuels.4c06147)
- 分类：氢氨燃料、着火与燃料性质预测 / 低碳燃料、着火与分子性质
- JCR：**二级来源报告 Q1/Q2，JCR 版本待官方核实**；报告最佳分区 Q1；版本未知；官方核实：否。
- 阅读深度：已核对元数据与上游 README，尚未完成全文精读。
- 完整期刊论文复现：**尚未验收**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../09_fuels_properties/README.md) · [全局地图](../../../00_literature_map/README.md)

分区线索：[二级来源](https://www.letpub.com/journal-selector/journal/2498)。多类别期刊使用报告中的最佳类别作为候选信号，不能解释为所有类别均为 Q1。

## 研究问题

预测高能量密度液态多环烃性质，为可持续航空燃料设计提供分子筛选依据。

## 方法与代码所能确认的内容

README 明确对应本篇 2025 Energy & Fuels 论文，称包含 AFProp 净燃烧热 437 条、密度 486 条及模型脚本；数据量尚未逐条去重核验。

## 复现入口与依赖

从上游数据集和建模脚本开始，核对分子标识、单位、重复分子和训练/测试划分。

## 环境与数据

以固定版本脚本导入和环境说明为准，未执行训练；外部 AFProp 数据的使用许可另核。

## 建议验证协议（本库设计）

采用分子骨架或化学家族留出，比较 MAE/RMSE、外推误差和性质联合筛选结果；避免随机划分近同系物造成高估。

## 局限与当前状态

未找到源码许可，仅链接收纳。README 引用 Fuel 2021 DOI 10.1016/j.fuel.2021.121437 作为数据来源，不能把本仓库归作那篇论文的原始实现。

## 代码溯源

- 仓库：[dkrijal100/Dataset-and-script-used-in-model-development](https://github.com/dkrijal100/Dataset-and-script-used-in-model-development)
- 固定提交：`e3e648e701ecd45745432e10b25bdbbf972e2c62`
- 关系证据：`author_implementation_readme_explicit`；来自上游 README，不代表本库已做作者身份独立认证。
- 许可：not_located；收纳状态：`link_only`。
- [代码包卡片](../../../code_packages/dkrijal100__Dataset-and-script-used-in-model-development/README.md)

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1021/acs.energyfuels.4c06147)；本轮整理日期 2026-11-12。完整元数据见同目录 `paper.json`。
