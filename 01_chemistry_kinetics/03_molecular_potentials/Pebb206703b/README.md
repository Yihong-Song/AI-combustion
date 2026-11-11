# Exploring the Chemical Space of Linear Alkane Pyrolysis via Deep Potential GENerator

Pebb206703b · 2020 · Energy & Fuels

作者：Jinzhe Zeng; Linfeng Zhang; Han Wang; Tong Zhu

- DOI：[原文入口](https://doi.org/10.1021/acs.energyfuels.0c03211)
- 分类：化学动力学代理、缩减与机理发现 / 神经网络势、反应分子动力学与主动学习
- JCR：**二级来源报告 Q1/Q2，JCR 版本待官方核实**；报告最佳分区 Q1；版本未知；官方核实：否。
- 阅读深度：已核对元数据与上游 README，尚未完成全文精读。
- 论文原始指标复现：**未执行**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../01_chemistry_kinetics/README.md) · [全局地图](../../../00_literature_map/README.md)

分区线索：[二级来源](https://www.letpub.com/journal-selector/journal/2498)。多类别期刊使用报告中的最佳类别作为候选信号，不能解释为所有类别均为 Q1。

## 研究问题

以自动化数据构建与并发学习推进燃烧神经网络势训练。

## 方法与代码所能确认的内容

README 将此 DOI 明确标为后续工作，说明 MDDatasetBuilder 已集成到 DP-GEN 的反应初始化流程；随后可继续并发学习。

## 复现入口与依赖

dpgen init_reaction reaction.json machine.json；机器配置连接 LAMMPS、datasetbuilder 与 Gaussian，后续训练按 DP-GEN 文档执行。

## 环境与数据

需要单独固定 DP-GEN、DeePMD-kit、LAMMPS 与量子化学软件版本；本包归档不包含全部外部工具、轨迹或计算资源。

## 建议验证协议（本库设计）

报告每轮新增标注构型、模型偏差准则、总量子化学成本与未见反应场景的独立测试；比较固定数据和主动学习预算。

## 局限与当前状态

与 2020 Nature Communications 工作共用一个支撑包，只计一个包；该映射来自 README 后续工作说明，尚未复现本文图表。

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

元数据来源：[Crossref](https://api.crossref.org/works/10.1021/acs.energyfuels.0c03211)；本轮整理日期 2026-11-11。完整元数据见同目录 `paper.json`。
