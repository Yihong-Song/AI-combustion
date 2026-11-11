# Enforcing physical conservation in neural network surrogate models for complex chemical kinetics

P221bc006b9 · 2025 · Combustion and Flame

作者：Tinghao Wang; Yuxiao Yi; Junjie Yao; Zhi-Qin John Xu; Tianhan Zhang; Zheng Chen

- DOI：[原文入口](https://doi.org/10.1016/j.combustflame.2025.114105)
- 分类：化学动力学代理、缩减与机理发现 / 代理与缩减
- JCR：**二级来源报告 Q1/Q2，JCR 版本待官方核实**；报告最佳分区 Q1；版本未知；官方核实：否。
- 阅读深度：已核对元数据与上游 README，尚未完成全文精读。
- 完整期刊论文复现：**尚未验收**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../01_chemistry_kinetics/README.md) · [全局地图](../../../00_literature_map/README.md)

分区线索：[二级来源](https://www.letpub.com/index.php?page=journalapp&view=detail&journalid=1901)。多类别期刊使用报告中的最佳类别作为候选信号，不能解释为所有类别均为 Q1。

## 研究问题

在复杂化学动力学神经代理中强制物理守恒，降低迭代时状态漂移。

## 方法与代码所能确认的内容

仓库 README 将本 DOI 列为对应工作，并同时给出 2022 多尺度采样论文。实际守恒算子、变量转换及训练约束须从论文和具体脚本核对，不能只根据标题推断实现。

## 复现入口与依赖

modelclass.py 与 ZeroDAutognition.py 是定位模型和零维验证的起点；逐个追踪守恒层和推理变换。

## 环境与数据

Python/Fortran 双实现；机理、组分顺序和时间步必须一致。

## 建议验证协议（本库设计）

报告元素/总质量守恒残差、负组分出现率、长时轨迹误差和同硬件端到端时间，增加无守恒约束消融。

## 局限与当前状态

尚未执行论文实验；守恒不自动保证化学准确、正性或未知机理可迁移。

## 代码溯源

- 仓库：[tianhanz/DNN-Models-for-Chemical-Kinetics](https://github.com/tianhanz/DNN-Models-for-Chemical-Kinetics)
- 固定提交：`bc07e5a210ba357b8a5350b460a751a68a002174`
- 关系证据：`author_implementation_readme_explicit`；来自上游 README，不代表本库已做作者身份独立认证。
- 许可：Apache-2.0；收纳状态：`partial_source_snapshot_collected`。
- [代码包卡片](../../../code_packages/tianhanz__DNN-Models-for-Chemical-Kinetics/README.md)

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1016/j.combustflame.2025.114105)；本轮整理日期 2026-11-12。完整元数据见同目录 `paper.json`。
