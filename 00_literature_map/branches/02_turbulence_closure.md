# 湍流燃烧闭合与流形模型

大涡模拟看不清所有小火焰结构，需要模型补上未解析尺度对反应和混合的影响。

[返回全景](../README.md) · [方向技术说明](../../02_turbulence_closure/README.md)

## 物理目标与评价逻辑

目标是滤波反应率、标量耗散率、PDF/FDF、混合时间尺度，还是火焰面褶皱？必须先说明滤波算子与可用输入。

源项条件均值、联合 PDF、标量耗散、火焰位置与刷厚、热释放率、能谱、LES 稳定性和总体成本；相关系数不足以取代物理量。

## 方法与数据

MLP/PCA-ANN、CNN 空间闭合、条件概率建模、物理约束 GAN、solver-in-the-loop 训练。后验耦合比离线拟合更接近最终用途。

DNS 三维瞬时场、空间滤波结果、LES 解析量；可结合 BLASTNet 与 aPrioriDNS。保存滤波核、核宽、Favre/普通滤波、网格间距和化学机理。

## 风险与阅读路线

a priori 优秀不保证 a posteriori 稳定。滤波和边界处理不一致会造成标签偏差；氢火焰差异扩散和热扩散不稳定性增加迁移难度。

先理解滤波反应率定义，再读早期 CNN/PDF 论文和 CMLM，最后看在线耦合与误差控制。

## 闭合、PDF 与热化学流形

| 年份 | 论文 | 方向 | 分区状态 | 代码 |
|---|---|---|---|---|
| 2026 | [Generalizable deep learning for sub-filter PDF of thermo-diffusively unstable lean hydrogen flames at varying Ka numbers](../../02_turbulence_closure/01_closures_manifolds/Pfb33a20719/README.md) | 湍流燃烧闭合与流形模型 | provisional_q1_q2 | 待核对 |
| 2026 | [Physics-informed neural networks for modeling turbulent combustion](../../02_turbulence_closure/01_closures_manifolds/P4f012c3c1a/README.md) | 湍流燃烧闭合与流形模型 | provisional_q1_q2 | 待核对 |
| 2026 | [Deep learning driven uncertainty quantification analysis for combustion modeling of turbulent non-premixed jet flames](../../02_turbulence_closure/01_closures_manifolds/P09f5ec6647/README.md) | 湍流燃烧闭合与流形模型 | pending_jcr | 待核对 |
| 2026 | [Solver-in-the-loop training of deep learning closures for large-eddy simulation of turbulent premixed jet flames](../../02_turbulence_closure/01_closures_manifolds/P2f92fd224f/README.md) | 湍流燃烧闭合与流形模型 | provisional_q1_q2 | 待核对 |
| 2025 | [A Data-Driven Approach to Refine the Partially Stirred Reactor Closure for Turbulent Premixed Flames](../../02_turbulence_closure/01_closures_manifolds/P8badc7f206/README.md) | 湍流燃烧闭合与流形模型 | pending_jcr | 已核对链接 |
| 2025 | [Neural network-augmented eddy viscosity closures for turbulent premixed jet flames](../../02_turbulence_closure/01_closures_manifolds/P6c7bc45f38/README.md) | 湍流燃烧闭合与流形模型 | provisional_q1_q2 | 待核对 |
| 2025 | [Neural network-based 3D reconstruction of temperature and velocity for turbulent flames from 2D measurements](../../02_turbulence_closure/01_closures_manifolds/P5829fd4f5a/README.md) | 湍流燃烧闭合与流形模型 | provisional_q1_q2 | 待核对 |
| 2025 | [A TVD neural network closure and application to turbulent combustion](../../02_turbulence_closure/01_closures_manifolds/P26d7efc82b/README.md) | 湍流燃烧闭合与流形模型 | pending_jcr | 待核对 |
| 2025 | [Machine learning-based prediction of species mass fraction and flame characteristics in partially premixed turbulent jet flame](../../02_turbulence_closure/01_closures_manifolds/Pb8ed01f292/README.md) | 湍流燃烧闭合与流形模型 | pending_jcr | 待核对 |
| 2024 | [Reconstructing temperature fields from OH distribution and soot volume fraction in turbulent flames using an artificial neural network](../../02_turbulence_closure/01_closures_manifolds/Pc3ae0f1897/README.md) | 湍流燃烧闭合与流形模型 | provisional_q1_q2 | 待核对 |
| 2024 | [Flame lift-off detector based on deep learning neural networks](../../02_turbulence_closure/01_closures_manifolds/P9d8c588bd0/README.md) | 湍流燃烧闭合与流形模型 | provisional_q1_q2 | 待核对 |
| 2024 | [High-resolution reconstruction of turbulent flames from sparse data with physics-informed neural networks](../../02_turbulence_closure/01_closures_manifolds/P2098eae71a/README.md) | 湍流燃烧闭合与流形模型 | provisional_q1_q2 | 待核对 |
| 2024 | [Augmenting filtered flame front displacement models for LES using machine learning with a posteriori simulations](../../02_turbulence_closure/01_closures_manifolds/P47b7416a64/README.md) | 湍流燃烧闭合与流形模型 | provisional_q1_q2 | 待核对 |
| 2023 | [A-priori and a-posterior studies of filtered probability density function models and NO formation prediction in turbulent stratified premixed combustion using machine learning](../../02_turbulence_closure/01_closures_manifolds/Pbe94ab8213/README.md) | 湍流燃烧闭合与流形模型 | provisional_q1_q2 | 待核对 |
| 2023 | [Towards a generalised artificial neural network for sub-grid filtered density function closure in turbulent combustion](../../02_turbulence_closure/01_closures_manifolds/Pa35bd06872/README.md) | 湍流燃烧闭合与流形模型 | pending_jcr | 待核对 |
| 2023 | [High-resolution reconstruction and a-priori modeling of turbulent flames in the context of large eddy simulation using the convolutional neural network](../../02_turbulence_closure/01_closures_manifolds/P6f1fd016ed/README.md) | 湍流燃烧闭合与流形模型 | provisional_q1_q2 | 待核对 |
| 2022 | [Investigation of deep learning methods for efficient high-fidelity simulations in turbulent combustion](../../02_turbulence_closure/01_closures_manifolds/P02ef93d20e/README.md) | 湍流燃烧闭合与流形模型 | provisional_q1_q2 | 待核对 |
| 2022 | [Machine learning assisted modeling of mixing timescale for LES/PDF of high-Karlovitz turbulent premixed combustion](../../02_turbulence_closure/01_closures_manifolds/Pdcd74f2e1d/README.md) | 湍流燃烧闭合与流形模型 | provisional_q1_q2 | 待核对 |
| 2021 | [Application of machine learning for filtered density function closure in MILD combustion](../../02_turbulence_closure/01_closures_manifolds/P61b14f06d3/README.md) | 湍流燃烧闭合与流形模型 | provisional_q1_q2 | 待核对 |
| 2021 | [Deep learning-based model for progress variable dissipation rate in turbulent premixed flames](../../02_turbulence_closure/01_closures_manifolds/P932b0f3071/README.md) | 湍流燃烧闭合与流形模型 | provisional_q1_q2 | 待核对 |
| 2021 | [An a priori evaluation of a principal component and artificial neural network based combustion model in diesel engine conditions](../../02_turbulence_closure/01_closures_manifolds/P15efd785db/README.md) | 湍流燃烧闭合与流形模型 | provisional_q1_q2 | 已核对链接 |
| 2020 | [Combustion regime identification from machine learning trained by Raman/Rayleigh line measurements](../../02_turbulence_closure/01_closures_manifolds/Pc9957bf0fb/README.md) | 湍流燃烧闭合与流形模型 | provisional_q1_q2 | 待核对 |
| 2020 | [A deep learning framework for hydrogen-fueled turbulent combustion simulation](../../02_turbulence_closure/01_closures_manifolds/Pc40a564122/README.md) | 湍流燃烧闭合与流形模型 | provisional_q1_q2 | 待核对 |
| 2019 | [Deep learning for presumed probability density function models](../../02_turbulence_closure/01_closures_manifolds/P8e35309a6a/README.md) | 湍流燃烧闭合与流形模型 | provisional_q1_q2 | 待核对 |
