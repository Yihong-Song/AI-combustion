# A Data-Driven Approach to Refine the Partially Stirred Reactor Closure for Turbulent Premixed Flames

P8badc7f206 · 2025 · Flow, Turbulence and Combustion

作者：Lorenzo Piu; Arthur Péquin; Rodolfo S. M. Freitas; Salvatore Iavarone; Heinz Pitsch; Alessandro Parente

- DOI：[原文入口](https://doi.org/10.1007/s10494-024-00626-3)
- 分类：湍流燃烧闭合与流形模型 / 闭合、PDF 与热化学流形
- JCR：**JCR 分区待核实**；报告最佳分区 未知；版本未知；官方核实：否。
- 阅读深度：已核对元数据与上游 README，尚未完成全文精读。
- 完整期刊论文复现：**尚未验收**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../02_turbulence_closure/README.md) · [全局地图](../../../00_literature_map/README.md)

## 研究问题

基于 DNS 数据改进预混湍流火焰的 PaSR 闭合，并为数据处理提供可追溯工具。

## 方法与代码所能确认的内容

固定 README 显式链接本文 DOI，说明 Field3D/Scalar3D、滤波、源项计算和可视化等功能。当前软件是通用工具，不能据此断言论文所有训练和优化设置都已打包。

## 复现入口与依赖

从 Field3D 的数据读取、滤波和 compute_reaction_rates 示例开始，核对普通/Favre 滤波与 LFR 源项定义。

## 环境与数据

README 给出 NumPy、SciPy、Matplotlib、Cantera、PyCSP、findiff 等；旧发行名 aPrioriDNS、新名 apriori，需固定提交与对应文档。

## 建议验证协议（本库设计）

比较条件源项误差、未见滤波尺度与物理工况；先验 DNS 拟合之后还需要后验 LES 稳定性评价。

## 局限与当前状态

GPL-3.0；未执行论文实验。aPriori/aPrioriDNS 为更名相关入口，按已收纳的固定仓库卡计一次，避免重复计包。

## 代码溯源

- 仓库：[LorenzoPiu/aPrioriDNS](https://github.com/LorenzoPiu/aPrioriDNS)
- 固定提交：`19bb0fa13fb068c4bd74bed1f8deae35708514b6`
- 关系证据：`author_supporting_tool_readme_explicit`；来自上游 README，不代表本库已做作者身份独立认证。
- 许可：GPL-3.0 (inspect upstream terms)；收纳状态：`partial_source_snapshot_collected`。
- [代码包卡片](../../../code_packages/LorenzoPiu__aPrioriDNS/README.md)

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1007/s10494-024-00626-3)；本轮整理日期 2026-11-12。完整元数据见同目录 `paper.json`。
