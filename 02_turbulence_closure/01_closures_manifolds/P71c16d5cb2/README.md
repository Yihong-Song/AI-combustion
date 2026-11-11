# a priori uncertainty quantification of reacting turbulence closure models using Bayesian neural networks

P71c16d5cb2 · 2025 · Engineering Applications of Artificial Intelligence

作者：Graham Pash; Malik Hassanaly; Shashank Yellapantula

- DOI：[原文入口](https://doi.org/10.1016/j.engappai.2024.109821)
- 分类：湍流燃烧闭合与流形模型 / 闭合、PDF 与热化学流形
- JCR：**二级来源报告 Q1/Q2，JCR 版本待官方核实**；报告最佳分区 Q1；版本未知；官方核实：否。
- 阅读深度：已核对元数据与上游 README，尚未完成全文精读。
- 完整期刊论文复现：**尚未验收**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../02_turbulence_closure/README.md) · [全局地图](../../../00_literature_map/README.md)

分区线索：[二级来源](https://www.letpub.com/journal-selector/journal/2513)。多类别期刊使用报告中的最佳类别作为候选信号，不能解释为所有类别均为 Q1。

## 研究问题

用贝叶斯神经网络估计预混湍流闭合预测及认知/随机不确定度。

## 方法与代码所能确认的内容

README 引用 arXiv:2402.18729，题名与 Crossref 期刊版一致；明确以亚滤波进度变量耗散率为目标。保留预印本到正式版配置核对待办。

## 复现入口与依赖

从项目安装和模型/训练配置开始，核对变分推断、网络参数分布与预测采样；Python 3.10 环境为上游建议。

## 环境与数据

项目 Python 依赖与 HPC/MPI 配置需依固定提交核查；预混 DNS 数据及预处理不因源码可见而视为齐备。

## 建议验证协议（本库设计）

除均方误差外，比较预测区间覆盖、校准、域外不确定度与区间宽度；按独立火焰和滤波尺度划分。

## 局限与当前状态

BSD-3-Clause-Clear；先验不确定度表现不能直接证明后验 LES 安全或模型已校准。

## 代码溯源

- 仓库：[NatLabRockies/mluq-prop](https://github.com/NatLabRockies/mluq-prop)
- 固定提交：`a4e0ae008fc6edb343967388bab5c7166dd98944`
- 关系证据：`title_match_repository_readme`；来自上游 README，不代表本库已做作者身份独立认证。
- 许可：BSD-3-Clause-Clear；收纳状态：`partial_source_snapshot_collected`。
- [代码包卡片](../../../code_packages/NatLabRockies__mluq-prop/README.md)

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1016/j.engappai.2024.109821)；本轮整理日期 2026-11-12。完整元数据见同目录 `paper.json`。
