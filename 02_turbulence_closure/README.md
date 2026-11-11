# 湍流燃烧闭合与流形模型

大涡模拟看不清所有小火焰结构，需要模型补上未解析尺度对反应和混合的影响。

本目录含 24 条候选。分区与全文状态逐篇标注；自动分类以研究目标优先，交叉方法可在总库检索。

[返回首页](../README.md) · [全局地图](../00_literature_map/README.md) · [方法与范围](../docs/METHODOLOGY.md)

## 核心问题

目标是滤波反应率、标量耗散率、PDF/FDF、混合时间尺度，还是火焰面褶皱？必须先说明滤波算子与可用输入。

## 方法演进与比较

MLP/PCA-ANN、CNN 空间闭合、条件概率建模、物理约束 GAN、solver-in-the-loop 训练。后验耦合比离线拟合更接近最终用途。

## 数据与物理定义

DNS 三维瞬时场、空间滤波结果、LES 解析量；可结合 BLASTNet 与 aPrioriDNS。保存滤波核、核宽、Favre/普通滤波、网格间距和化学机理。

## 怎样判断模型有效

源项条件均值、联合 PDF、标量耗散、火焰位置与刷厚、热释放率、能谱、LES 稳定性和总体成本；相关系数不足以取代物理量。

## 如何避免数据泄漏

按 DNS 工况、独立时间段和燃料划分；空间相邻小块不得随机跨集合。另测未见滤波宽度、Ka/Da/Re。

## 主要局限与选题问题

a priori 优秀不保证 a posteriori 稳定。滤波和边界处理不一致会造成标签偏差；氢火焰差异扩散和热扩散不稳定性增加迁移难度。

## 建议阅读和实践路径

先理解滤波反应率定义，再读早期 CNN/PDF 论文和 CMLM，最后看在线耦合与误差控制。

## 细分类与论文索引

分区栏为二级来源线索；Q? 为待核实。代码 ✓ 仅表示论文链接已核对，不表示执行成功。

### [闭合、PDF 与热化学流形](01_closures_manifolds/README.md)（24）

| 年份 | 论文 | 分区线索 | 代码 |
|---|---|---|---|
| 2026 | [Generalizable deep learning for sub-filter PDF of thermo-diffusively unstable lean hydrogen flames at varying Ka numbers](01_closures_manifolds/Pfb33a20719/README.md) | Q1 | 待核对 |
| 2026 | [Physics-informed neural networks for modeling turbulent combustion](01_closures_manifolds/P4f012c3c1a/README.md) | Q1 | 待核对 |
| 2026 | [Deep learning driven uncertainty quantification analysis for combustion modeling of turbulent non-premixed jet flames](01_closures_manifolds/P09f5ec6647/README.md) | Q? | 待核对 |
| 2026 | [Solver-in-the-loop training of deep learning closures for large-eddy simulation of turbulent premixed jet flames](01_closures_manifolds/P2f92fd224f/README.md) | Q1 | 待核对 |
| 2025 | [A Data-Driven Approach to Refine the Partially Stirred Reactor Closure for Turbulent Premixed Flames](01_closures_manifolds/P8badc7f206/README.md) | Q? | ✓ |
| 2025 | [Neural network-augmented eddy viscosity closures for turbulent premixed jet flames](01_closures_manifolds/P6c7bc45f38/README.md) | Q1 | 待核对 |
| 2025 | [Neural network-based 3D reconstruction of temperature and velocity for turbulent flames from 2D measurements](01_closures_manifolds/P5829fd4f5a/README.md) | Q1 | 待核对 |
| 2025 | [A TVD neural network closure and application to turbulent combustion](01_closures_manifolds/P26d7efc82b/README.md) | Q? | 待核对 |
| 2025 | [Machine learning-based prediction of species mass fraction and flame characteristics in partially premixed turbulent jet flame](01_closures_manifolds/Pb8ed01f292/README.md) | Q? | 待核对 |
| 2024 | [Reconstructing temperature fields from OH distribution and soot volume fraction in turbulent flames using an artificial neural network](01_closures_manifolds/Pc3ae0f1897/README.md) | Q1 | 待核对 |
| 2024 | [Flame lift-off detector based on deep learning neural networks](01_closures_manifolds/P9d8c588bd0/README.md) | Q1 | 待核对 |
| 2024 | [High-resolution reconstruction of turbulent flames from sparse data with physics-informed neural networks](01_closures_manifolds/P2098eae71a/README.md) | Q1 | 待核对 |
| 2024 | [Augmenting filtered flame front displacement models for LES using machine learning with a posteriori simulations](01_closures_manifolds/P47b7416a64/README.md) | Q1 | 待核对 |
| 2023 | [A-priori and a-posterior studies of filtered probability density function models and NO formation prediction in turbulent stratified premixed combustion using machine learning](01_closures_manifolds/Pbe94ab8213/README.md) | Q1 | 待核对 |
| 2023 | [Towards a generalised artificial neural network for sub-grid filtered density function closure in turbulent combustion](01_closures_manifolds/Pa35bd06872/README.md) | Q? | 待核对 |
| 2023 | [High-resolution reconstruction and a-priori modeling of turbulent flames in the context of large eddy simulation using the convolutional neural network](01_closures_manifolds/P6f1fd016ed/README.md) | Q1 | 待核对 |
| 2022 | [Investigation of deep learning methods for efficient high-fidelity simulations in turbulent combustion](01_closures_manifolds/P02ef93d20e/README.md) | Q1 | 待核对 |
| 2022 | [Machine learning assisted modeling of mixing timescale for LES/PDF of high-Karlovitz turbulent premixed combustion](01_closures_manifolds/Pdcd74f2e1d/README.md) | Q1 | 待核对 |
| 2021 | [Application of machine learning for filtered density function closure in MILD combustion](01_closures_manifolds/P61b14f06d3/README.md) | Q1 | 待核对 |
| 2021 | [Deep learning-based model for progress variable dissipation rate in turbulent premixed flames](01_closures_manifolds/P932b0f3071/README.md) | Q1 | 待核对 |
| 2021 | [An a priori evaluation of a principal component and artificial neural network based combustion model in diesel engine conditions](01_closures_manifolds/P15efd785db/README.md) | Q1 | ✓ |
| 2020 | [Combustion regime identification from machine learning trained by Raman/Rayleigh line measurements](01_closures_manifolds/Pc9957bf0fb/README.md) | Q1 | 待核对 |
| 2020 | [A deep learning framework for hydrogen-fueled turbulent combustion simulation](01_closures_manifolds/Pc40a564122/README.md) | Q1 | 待核对 |
| 2019 | [Deep learning for presumed probability density function models](01_closures_manifolds/P8e35309a6a/README.md) | Q1 | 待核对 |
