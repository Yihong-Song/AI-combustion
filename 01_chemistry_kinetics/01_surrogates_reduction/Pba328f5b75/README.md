# Solving multiscale dynamical systems by deep learning

Pba328f5b75 · 2025 · Computer Physics Communications

作者：Junjie Yao; Yuxiao Yi; Liangkai Hang; Weinan E; Weizong Wang; Yaoyu Zhang; Tianhan Zhang; Zhi-Qin John Xu

- DOI：[原文入口](https://doi.org/10.1016/j.cpc.2025.109802)
- 分类：化学动力学代理、缩减与机理发现 / 代理与缩减
- JCR：**JCR 分区待核实**；报告最佳分区 未知；版本未知；官方核实：否。
- 阅读深度：已核对元数据与上游 README，尚未完成全文精读。
- 完整期刊论文复现：**尚未验收**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../01_chemistry_kinetics/README.md) · [全局地图](../../../00_literature_map/README.md)

## 研究问题

用多尺度状态采样和神经时间推进器处理刚性动力学，包含燃烧应用。

## 方法与代码所能确认的内容

README 将 EMCS 描述为范围估计、Monte Carlo 采样和演化扩充三阶段；提供 dryrun、单步、轨迹及 TorchScript 导出入口。

## 复现入口与依赖

pred.py dryrun、onestep_plot、evolution、export；训练入口 train.py。

## 环境与数据

上游示例环境含 Cantera 2.6、PyTorch、mpi4py/OpenMPI；Windows 与旧环境需额外适配。

## 建议验证协议（本库设计）

在同一硬件和容差下比较端到端时间、长时轨迹、误差累积和回退策略。

## 局限与当前状态

README 中速度提升为作者声明，本库未验证，不录为本库实测；作为跨领域方法单独标注其燃烧应用边界。

## 代码溯源

- 仓库：[Seauagain/DeePODE](https://github.com/Seauagain/DeePODE)
- 固定提交：`3ef423405f6d0d76e62d4f3a162e99a5e679ba82`
- 关系证据：`author_implementation_readme_explicit`；来自上游 README，不代表本库已做作者身份独立认证。
- 许可：Apache-2.0；收纳状态：`partial_source_snapshot_collected`。
- [代码包卡片](../../../code_packages/Seauagain__DeePODE/README.md)

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1016/j.cpc.2025.109802)；本轮整理日期 2026-11-12。完整元数据见同目录 `paper.json`。
