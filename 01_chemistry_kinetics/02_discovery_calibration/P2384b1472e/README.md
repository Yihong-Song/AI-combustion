# Uncertain lithium-ion cathode kinetic decomposition modeling via Bayesian chemical reaction neural networks

P2384b1472e · 2024 · Proceedings of the Combustion Institute

作者：Benjamin C. Koenig; Huaibo Chen; Qiaofeng Li; Peng Zhao; Sili Deng

- DOI：[原文入口](https://doi.org/10.1016/j.proci.2024.105243)
- 分类：化学动力学代理、缩减与机理发现 / 机理发现与参数校准
- JCR：**二级来源报告 Q1/Q2，JCR 版本待官方核实**；报告最佳分区 Q1；版本未知；官方核实：否。
- 阅读深度：已核对元数据与上游 README，尚未完成全文精读。
- 完整期刊论文复现：**尚未验收**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../01_chemistry_kinetics/README.md) · [全局地图](../../../00_literature_map/README.md)

分区线索：[二级来源](https://www.letpub.com/journal-selector/journal/6861)。多类别期刊使用报告中的最佳类别作为候选信号，不能解释为所有类别均为 Q1。

## 研究问题

用 Bayesian CRNN 表征锂电正极分解动力学的不确定性，属于燃烧安全交叉方向。

## 方法与代码所能确认的内容

CRNN README 将其列为 cathode UQ 研究，基于早期 DSC 正极热稳定性工作扩展。

## 复现入口与依赖

选择 cathode UQ 对应子目录的 Julia 项目与数据，避免误跑通用 Case 1–5。

## 环境与数据

不同子项目 Julia 环境不同；上游 cathode 新环境与原 CRNN 环境不可混用。

## 建议验证协议（本库设计）

除质量/热流误差，还需比较后验区间、预测区间覆盖率和多模态参数可辨识性。

## 局限与当前状态

同一 CRNN 仓库关联多篇论文，按论文计数与按包计数需分开；未执行采样。

## 代码溯源

- 仓库：[DENG-MIT/CRNN](https://github.com/DENG-MIT/CRNN)
- 固定提交：`4a17819c5bd4a65d6a9da9e72115b536d644350e`
- 关系证据：`author_implementation_readme_explicit`；来自上游 README，不代表本库已做作者身份独立认证。
- 许可：MIT；收纳状态：`partial_source_snapshot_collected`。
- [代码包卡片](../../../code_packages/DENG-MIT__CRNN/README.md)

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1016/j.proci.2024.105243)；本轮整理日期 2026-11-12。完整元数据见同目录 `paper.json`。
