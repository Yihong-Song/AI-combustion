# Physics-informed neural networks and functional interpolation for stiff chemical kinetics

P42f2fcf650 · 2022 · Chaos: An Interdisciplinary Journal of Nonlinear Science

作者：Mario De Florio; Enrico Schiassi; Roberto Furfaro

- DOI：[原文入口](https://doi.org/10.1063/5.0086649)
- 分类：物理信息学习与可微燃烧求解 / 正逆问题与可微求解
- JCR：**JCR 分区待核实**；报告最佳分区 未知；版本未知；官方核实：否。
- 阅读深度：已核对元数据与上游 README，尚未完成全文精读。
- 完整期刊论文复现：**尚未验收**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../06_physics_informed/README.md) · [全局地图](../../../00_literature_map/README.md)

## 研究问题

在刚性化学初值问题中比较物理约束神经解法与传统积分器。

## 方法与代码所能确认的内容

README 明确列本文 DOI，组合 Theory of Functional Connections 与 Extreme Learning Machines 得到 X-TFC；属于刚性动力学方法基础，不预设全部例题都是真实火焰。

## 复现入口与依赖

按固定仓库各例题脚本核对初值、时间区间、分段策略和特征数；先与同精度传统 ODE 参考解对照。

## 环境与数据

从各脚本导入和作者环境提取依赖；例题性质与详细燃烧化学的外推范围需全文确认。

## 建议验证协议（本库设计）

同误差容限下比较各物种、快瞬态、残差与总耗时，报告失败区间；随机特征多种子只计一个方法实验。

## 局限与当前状态

未定位许可，仅链接；标为方法基础，不能以通用 ROBER 等小系统充当详细燃烧论文复现。

## 代码溯源

- 仓库：[mariodeflorio/Stiff-Chemical-Kinetics](https://github.com/mariodeflorio/Stiff-Chemical-Kinetics)
- 固定提交：`4dfbf580c0a2d5c3136f17e0cdbd45a03e9f959e`
- 关系证据：`author_implementation_readme_explicit`；来自上游 README，不代表本库已做作者身份独立认证。
- 许可：not_located；收纳状态：`link_only`。
- [代码包卡片](../../../code_packages/mariodeflorio__Stiff-Chemical-Kinetics/README.md)

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1063/5.0086649)；本轮整理日期 2026-11-12。完整元数据见同目录 `paper.json`。
