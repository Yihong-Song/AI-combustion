# Deep learning dynamical latencies for the analysis and reduction of combustion chemistry kinetics

P0afc85ab6a · 2023 · Physics of Fluids

作者：Luisa Castellanos; Rodolfo S. M. Freitas; Alessandro Parente; Francesco Contino

- DOI：[原文入口](https://doi.org/10.1063/5.0167110)
- 分类：化学动力学代理、缩减与机理发现 / 代理与缩减
- JCR：**JCR 分区待核实**；报告最佳分区 未知；版本未知；官方核实：否。
- 阅读深度：已核对元数据与上游 README，尚未完成全文精读。
- 论文原始指标复现：**未执行**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../01_chemistry_kinetics/README.md) · [全局地图](../../../00_literature_map/README.md)

分区线索：[二级来源](https://www.letpub.com/journal-selector/journal/6673)。多类别期刊使用报告中的最佳类别作为候选信号，不能解释为所有类别均为 Q1。

## 研究问题

学习低维动力学潜变量，用于燃烧化学的分析和缩减。

## 方法与代码所能确认的内容

README 列出 optimization_process、training、manifold_characterization、PCA_comparison 和 extrapolation_cases，并给出 Zenodo 数据 DOI 10.5281/zenodo.10034264。

## 复现入口与依赖

先读取数据及预处理说明，再依次核对训练、流形表征、PCA 比较和外推算例。

## 环境与数据

外部 Zenodo 数据需另取并保留版本；运行环境需从各目录核实。

## 建议验证协议（本库设计）

比较重构误差、潜空间动力学和长期积分；PCA 对照需要相同潜维数和相同数据切分。

## 局限与当前状态

未找到明确源码许可。Physics of Fluids 的 JCR 证据在本轮未核实，因此列入分区待核实。

## 代码溯源

- 仓库：[lmcastellanos/Deep-learning-dynamical-latencies-for-the-analysis-and-reduction-of-combustion-chemistry-kinetics](https://github.com/lmcastellanos/Deep-learning-dynamical-latencies-for-the-analysis-and-reduction-of-combustion-chemistry-kinetics)
- 固定提交：`d37979971ffa7ceede3cccd5a15a52a9c209a51c`
- 关系证据：`title_match_repository_readme`；来自上游 README，不代表本库已做作者身份独立认证。
- 许可：not_located；收纳状态：`link_only`。
- [代码包卡片](../../../code_packages/lmcastellanos__Deep-learning-dynamical-latencies-for-the-analysis-and-reduction-of-combustion-chemistry-kinetics/README.md)

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1063/5.0167110)；本轮整理日期 2026-11-11。完整元数据见同目录 `paper.json`。
