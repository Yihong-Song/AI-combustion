# Physics-informed graph neural networks for predicting cetane number with systematic data quality analysis

Pad01f0053d · 2023 · Proceedings of the Combustion Institute

作者：Yeonjoon Kim; Jaeyoung Cho; Nimal Naser; Sabari Kumar; Keunhong Jeong; Robert L. McCormick; Peter C. St. John; Seonah Kim

- DOI：[原文入口](https://doi.org/10.1016/j.proci.2022.09.059)
- 分类：物理信息学习与可微燃烧求解 / 正逆问题与可微求解
- JCR：**二级来源报告 Q1/Q2，JCR 版本待官方核实**；报告最佳分区 Q1；版本未知；官方核实：否。
- 阅读深度：已核对元数据与上游 README，尚未完成全文精读。
- 完整期刊论文复现：**尚未验收**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../06_physics_informed/README.md) · [全局地图](../../../00_literature_map/README.md)

分区线索：[二级来源](https://www.letpub.com/journal-selector/journal/6861)。多类别期刊使用报告中的最佳类别作为候选信号，不能解释为所有类别均为 Q1。

## 研究问题

用物理信息图神经网络预测十六烷值，并分析标签质量的影响。

## 方法与代码所能确认的内容

上游明确链接论文与 nfp 图学习库，提供在线预测入口。分子级预测应区分新分子、相似同系物和混合燃料。

## 复现入口与依赖

先核对仓库中数据与训练入口，按上游要求安装 tensorflow==2.5.0、nfp==0.3.0 和 RDKit。

## 环境与数据

旧 TensorFlow/nfp 组合需独立旧 Python 环境；不建议在 Python 3.13 基线环境直接安装。

## 建议验证协议（本库设计）

使用 scaffold 或化学家族切分；报告 MAE、标签来源差异、重复分子和不确定度校准。

## 局限与当前状态

未定位到源码许可，仅链接收纳。线上预测服务是否仍可用未验证。

## 代码溯源

- 仓库：[BioE-KimLab/CNpred](https://github.com/BioE-KimLab/CNpred)
- 固定提交：`a7c4d4eda5913f367ad84ac3c4f6b14b1dd30d7c`
- 关系证据：`author_implementation_readme_explicit`；来自上游 README，不代表本库已做作者身份独立认证。
- 许可：not_located；收纳状态：`link_only`。
- [代码包卡片](../../../code_packages/BioE-KimLab__CNpred/README.md)

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1016/j.proci.2022.09.059)；本轮整理日期 2026-11-12。完整元数据见同目录 `paper.json`。
