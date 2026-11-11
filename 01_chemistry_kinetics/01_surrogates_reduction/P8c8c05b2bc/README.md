# Adaptive chemistry via pre-partitioning of composition space and mechanism reduction

P8c8c05b2bc · 2020 · Combustion and Flame

作者：Giuseppe D’Alessio; Alessandro Parente; Alessandro Stagni; Alberto Cuoci

- DOI：[原文入口](https://doi.org/10.1016/j.combustflame.2019.09.010)
- 分类：化学动力学代理、缩减与机理发现 / 代理与缩减
- JCR：**二级来源报告 Q1/Q2，JCR 版本待官方核实**；报告最佳分区 Q1；版本未知；官方核实：否。
- 阅读深度：已核对元数据与上游 README，尚未完成全文精读。
- 完整期刊论文复现：**尚未验收**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../01_chemistry_kinetics/README.md) · [全局地图](../../../00_literature_map/README.md)

分区线索：[二级来源](https://www.letpub.com/index.php?page=journalapp&view=detail&journalid=1901)。多类别期刊使用报告中的最佳类别作为候选信号，不能解释为所有类别均为 Q1。

## 研究问题

将热化学组成空间分区并配置局部缩减机理，降低 CFD 化学计算量。

## 方法与代码所能确认的内容

README 的 How to cite 明确列本文题名和卷页，说明实现 OpenFOAM 求解器的在线分类与自适应化学配置；分类器和局部机理构建需与原文对照。

## 复现入口与依赖

SPARC 对 laminarSMOKE/edcSMOKE 的扩展；先建立传统化学基准，再查看组成空间分类和局部机理选择接口。

## 环境与数据

OpenFOAM、laminarSMOKE/edcSMOKE、所需缩减机理及分类器；OpenMORe 是相关降阶工具，版本应单独固定。

## 建议验证协议（本库设计）

比较分类开销、机理切换、点火/火焰特性与 CFD 总耗时；在未见热化学区域记录回退与失败。

## 局限与当前状态

未定位许可证，只保留固定链接。预分区误差与局部机理误差需要分开归因。

## 代码溯源

- 仓库：[gdalessi/adaptiveChemistry](https://github.com/gdalessi/adaptiveChemistry)
- 固定提交：`391004914401dc2f887c280640a898f88041d7c9`
- 关系证据：`author_implementation_readme_explicit`；来自上游 README，不代表本库已做作者身份独立认证。
- 许可：not_located；收纳状态：`link_only`。
- [代码包卡片](../../../code_packages/gdalessi__adaptiveChemistry/README.md)

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1016/j.combustflame.2019.09.010)；本轮整理日期 2026-11-12。完整元数据见同目录 `paper.json`。
