# Complex reaction processes in combustion unraveled by neural network-based molecular dynamics simulation

P4a48f472f5 · 2020 · Nature Communications

作者：Jinzhe Zeng; Liqun Cao; Mingyuan Xu; Tong Zhu; John Z. H. Zhang

- DOI：[原文入口](https://doi.org/10.1038/s41467-020-19497-z)
- 分类：化学动力学代理、缩减与机理发现 / 神经网络势、反应分子动力学与主动学习
- JCR：**JCR 分区待核实**；报告最佳分区 未知；版本未知；官方核实：否。
- 阅读深度：已核对元数据与上游 README，尚未完成全文精读。
- 完整期刊论文复现：**尚未验收**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../01_chemistry_kinetics/README.md) · [全局地图](../../../00_literature_map/README.md)

## 研究问题

为燃烧反应分子动力学的神经网络势构建量子化学参考数据。

## 方法与代码所能确认的内容

README 明确列出 Nature Communications 本文；MDDatasetBuilder 从 LAMMPS 轨迹和可选键文件提取构型，生成量子化学输入，再准备 DeePMD 训练数据。该包是数据构建环节，不是论文全部反应 MD 工作流。

## 复现入口与依赖

datasetbuilder → qmcalc → preparedeepmd → dp train train.json；具体参数见固定版本 README。

## 环境与数据

LAMMPS/ReaxFF 轨迹、Gaussian 16 量子化学计算、DeePMD-kit 及相应运行环境；Gaussian 使用权限与计算资源需单独解决。

## 建议验证协议（本库设计）

按反应路径和构型分布留出，比较能量/原子力误差、域外构型、反应事件及产物统计，不能只看随机构型测试的力误差。

## 局限与当前状态

本库未计算量子化学数据或训练势函数；README 的运行时描述不是实测。代码许可、Gaussian 与原始轨迹的数据许可分别记录。

## 代码溯源

- 仓库：[tongzhugroup/mddatasetbuilder](https://github.com/tongzhugroup/mddatasetbuilder)
- 固定提交：`52e6edf860128e9624ec11a1cb8703327d014679`
- 关系证据：`author_supporting_component_readme_explicit`；来自上游 README，不代表本库已做作者身份独立认证。
- 许可：LGPL-3.0 (inspect upstream terms)；收纳状态：`source_archive_collected`。
- [代码包卡片](../../../code_packages/tongzhugroup__mddatasetbuilder/README.md)

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1038/s41467-020-19497-z)；本轮整理日期 2026-11-12。完整元数据见同目录 `paper.json`。
