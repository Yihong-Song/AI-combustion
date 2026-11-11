# 物理信息学习与可微燃烧求解

把守恒方程和边界条件加入模型，使稀疏数据下的正问题和逆问题更有物理约束。

本目录含 10 条候选。分区与全文状态逐篇标注；自动分类以研究目标优先，交叉方法可在总库检索。

[返回首页](../README.md) · [全局地图](../00_literature_map/README.md) · [方法与范围](../docs/METHODOLOGY.md)

## 核心问题

约束写在网络结构、损失函数、可微求解器还是后处理投影中？应区分软约束、硬约束和数值离散误差。

## 方法演进与比较

PINN、硬边界变换、分域/自适应残差采样、可微 ODE/PDE 与反向参数估计。刚性反应常需要尺度变换或降阶。

## 数据与物理定义

方程、机理、热输运性质、边界条件和少量观测；无监督残差点本身也是实验设计的一部分。

## 怎样判断模型有效

独立细网格的解误差、方程残差、边界误差、逆参数误差、噪声鲁棒性、失败种子和总训练成本。

## 如何避免数据泄漏

残差训练点与验证点分开，逆问题保留未用于拟合的工况/观测。不能只报告训练残差。

## 主要局限与选题问题

小残差不必然给出正确分支；损失尺度和导数精度影响优化。Bratu 有多解，B02 仅检验 lambda=1 的下分支。

## 建议阅读和实践路径

先跑 B02 核对导数与边界，再进入 FlamePINN-1D 简化火焰，最后加入详细化学和反演。

## 细分类与论文索引

分区栏为二级来源线索；Q? 为待核实。代码 ✓ 仅表示论文链接已核对，不表示执行成功。

### [正逆问题与可微求解](01_forward_inverse/README.md)（10）

| 年份 | 论文 | 分区线索 | 代码 |
|---|---|---|---|
| 2026 | [Physics-informed machine learning for discovering robust heat release rate detectors in ammonia-hydrogen combustion](01_forward_inverse/P0a22c037eb/README.md) | Q1 | 待核对 |
| 2026 | [A study of hybrid physics-informed neural networks models of one-dimensional ethylene premixed sooting flame](01_forward_inverse/P88154545ab/README.md) | Q1 | 待核对 |
| 2026 | [Dual-wavelength neural reconstruction of soot volume fraction, temperature and maturity in inverse and normal diffusion flames](01_forward_inverse/Pb2b19cf1c0/README.md) | Q1 | 待核对 |
| 2026 | [Impact of sustainable aviation fuels on soot properties: A physics-informed neural network enhanced in-situ characterization](01_forward_inverse/P1118c4b3ec/README.md) | Q1 | 待核对 |
| 2025 | [FlamePINN-1D: Physics-informed neural networks to solve forward and inverse problems of 1D laminar flames](01_forward_inverse/P1cf521f2c6/README.md) | Q1 | ✓ |
| 2025 | [A physics-informed machine learning approach for predicting dynamic behavior of reacting flows with application to hydrogen jet flames](01_forward_inverse/Pc3e1b50927/README.md) | Q1 | 待核对 |
| 2024 | [Reconstructing soot fields in acoustically forced laminar sooting flames using physics-informed machine learning models](01_forward_inverse/Pd19bb828b9/README.md) | Q1 | 待核对 |
| 2023 | [Application of a physics-informed neural network to solve the steady-state Bratu equation arising from solid biofuel combustion theory](01_forward_inverse/Pb552d55f67/README.md) | Q1 | 待核对 |
| 2023 | [Physics-informed graph neural networks for predicting cetane number with systematic data quality analysis](01_forward_inverse/Pad01f0053d/README.md) | Q1 | ✓ |
| 2022 | [Physics-informed neural networks and functional interpolation for stiff chemical kinetics](01_forward_inverse/P42f2fcf650/README.md) | Q? | ✓ |
