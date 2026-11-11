# 物理信息学习与可微燃烧求解

把守恒方程和边界条件加入模型，使稀疏数据下的正问题和逆问题更有物理约束。

[返回全景](../README.md) · [方向技术说明](../../06_physics_informed/README.md)

## 物理目标与评价逻辑

约束写在网络结构、损失函数、可微求解器还是后处理投影中？应区分软约束、硬约束和数值离散误差。

独立细网格的解误差、方程残差、边界误差、逆参数误差、噪声鲁棒性、失败种子和总训练成本。

## 方法与数据

PINN、硬边界变换、分域/自适应残差采样、可微 ODE/PDE 与反向参数估计。刚性反应常需要尺度变换或降阶。

方程、机理、热输运性质、边界条件和少量观测；无监督残差点本身也是实验设计的一部分。

## 风险与阅读路线

小残差不必然给出正确分支；损失尺度和导数精度影响优化。Bratu 有多解，B02 仅检验 lambda=1 的下分支。

先跑 B02 核对导数与边界，再进入 FlamePINN-1D 简化火焰，最后加入详细化学和反演。

## 正逆问题与可微求解

| 年份 | 论文 | 方向 | 分区状态 | 代码 |
|---|---|---|---|---|
| 2026 | [Physics-informed machine learning for discovering robust heat release rate detectors in ammonia-hydrogen combustion](../../06_physics_informed/01_forward_inverse/P0a22c037eb/README.md) | 物理信息学习与可微燃烧求解 | provisional_q1_q2 | 待核对 |
| 2026 | [A study of hybrid physics-informed neural networks models of one-dimensional ethylene premixed sooting flame](../../06_physics_informed/01_forward_inverse/P88154545ab/README.md) | 物理信息学习与可微燃烧求解 | provisional_q1_q2 | 待核对 |
| 2026 | [Dual-wavelength neural reconstruction of soot volume fraction, temperature and maturity in inverse and normal diffusion flames](../../06_physics_informed/01_forward_inverse/Pb2b19cf1c0/README.md) | 物理信息学习与可微燃烧求解 | provisional_q1_q2 | 待核对 |
| 2026 | [Impact of sustainable aviation fuels on soot properties: A physics-informed neural network enhanced in-situ characterization](../../06_physics_informed/01_forward_inverse/P1118c4b3ec/README.md) | 物理信息学习与可微燃烧求解 | provisional_q1_q2 | 待核对 |
| 2025 | [FlamePINN-1D: Physics-informed neural networks to solve forward and inverse problems of 1D laminar flames](../../06_physics_informed/01_forward_inverse/P1cf521f2c6/README.md) | 物理信息学习与可微燃烧求解 | provisional_q1_q2 | 已核对链接 |
| 2025 | [A physics-informed machine learning approach for predicting dynamic behavior of reacting flows with application to hydrogen jet flames](../../06_physics_informed/01_forward_inverse/Pc3e1b50927/README.md) | 物理信息学习与可微燃烧求解 | provisional_q1_q2 | 待核对 |
| 2024 | [Reconstructing soot fields in acoustically forced laminar sooting flames using physics-informed machine learning models](../../06_physics_informed/01_forward_inverse/Pd19bb828b9/README.md) | 物理信息学习与可微燃烧求解 | provisional_q1_q2 | 待核对 |
| 2023 | [Application of a physics-informed neural network to solve the steady-state Bratu equation arising from solid biofuel combustion theory](../../06_physics_informed/01_forward_inverse/Pb552d55f67/README.md) | 物理信息学习与可微燃烧求解 | provisional_q1_q2 | 待核对 |
| 2023 | [Physics-informed graph neural networks for predicting cetane number with systematic data quality analysis](../../06_physics_informed/01_forward_inverse/Pad01f0053d/README.md) | 物理信息学习与可微燃烧求解 | provisional_q1_q2 | 已核对链接 |
