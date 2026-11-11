# Comprehensive deep learning for combustion chemistry integration: Multi-fuel generalization and a posteriori validation in reacting flow

Pdd9a1fb317 · 2025 · Physics of Fluids

作者：Han Li; Ruixin Yang; Yangchen Xu; Min Zhang; Runze Mao; Zhi X. Chen

- DOI：[原文入口](https://doi.org/10.1063/5.0248582)
- 分类：化学动力学代理、缩减与机理发现 / 代理与缩减
- JCR：**JCR 分区待核实**；报告最佳分区 未知；版本未知；官方核实：否。
- 阅读深度：已核对元数据与上游 README，尚未完成全文精读。
- 完整期刊论文复现：**尚未验收**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../01_chemistry_kinetics/README.md) · [全局地图](../../../00_literature_map/README.md)

分区线索：[二级来源](https://www.letpub.com/journal-selector/journal/6673)。多类别期刊使用报告中的最佳类别作为候选信号，不能解释为所有类别均为 Q1。

## 研究问题

评估燃烧化学神经积分器跨燃料泛化及耦合反应流后的实际表现。

## 方法与代码所能确认的内容

README 在 Multi-fuel generalization and a posteriori validation 小节明确列出本文。当前工具提供数据与训练管线，但本文各燃料模型、权重和 CFD 验证配置是否完整需逐文件确认。

## 复现入口与依赖

沿 canonical_cases、数据生成/增广/标注及 training 配置查找各燃料设置，再核对 DeepFlame 的模型部署接口。

## 环境与数据

Python/Cantera/DeepFlame/OpenFOAM 及每个燃料的机理；不能把换用新机理所得实验写作原文复现。

## 建议验证协议（本库设计）

按燃料与独立流场留出，分别报告逐步拟合与长时后验结果，保持化学时间步、误差控制与硬件相同。

## 局限与当前状态

只确认相关软件关系，尚未核验完整原文实验；多个燃料不能重复计为多篇论文。

## 代码溯源

- 仓库：[deepflame-ai/DFODE-kit](https://github.com/deepflame-ai/DFODE-kit)
- 固定提交：`bc65e84bc7644675b9996e3eea08f0d38cbceaad`
- 关系证据：`author_related_work_readme_explicit`；来自上游 README，不代表本库已做作者身份独立认证。
- 许可：GPL-3.0 (inspect upstream terms)；收纳状态：`partial_source_snapshot_collected`。
- [代码包卡片](../../../code_packages/deepflame-ai__DFODE-kit/README.md)

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1063/5.0248582)；本轮整理日期 2026-11-12。完整元数据见同目录 `paper.json`。
