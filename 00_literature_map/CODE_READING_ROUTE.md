# 代码优先阅读路线

先看许可与数据，再看入口。表中链接已核对，但原始训练未执行。建议顺序：轻量辐射演示 → FlamePINN 简化算例 → SL-GPS 自燃 → CMLM 预存数据 → Bayesian CRNN → 详细化学/CFD。受限或缺许可的代码只保留链接。

| 年份 | 论文 | 方向 | 分区状态 | 代码 |
|---|---|---|---|---|
| 2026 | [Neural refractive index primitives for flame field reconstruction using background-oriented schlieren](../05_diagnostics_radiation/01_optical_inverse/Pc2b8d1f214/README.md) | 光学诊断、反演、烟炱与辐射 | provisional_q1_q2 | 已核对链接 |
| 2026 | [Physics-informed neural network WSGG model for radiative heat transfer in H2O–CO2–NH3 gas mixtures relevant to ammonia combustion](../05_diagnostics_radiation/02_radiation_soot/P69b4098fb3/README.md) | 光学诊断、反演、烟炱与辐射 | provisional_q1_q2 | 已核对链接 |
| 2026 | [CFD analysis of operating parameters and machine learning-aided optimization of reactor performance in a polyethylene pyrolysis fluidized bed](../08_solid_fuels_fire/01_kinetics_fire/Pd715d789f0/README.md) | 固体燃料、热解与火灾安全 | provisional_q1_q2 | 已核对链接 |
| 2026 | [BayeSAF: Emulation and design of sustainable alternative fuels via Bayesian inference and descriptors-based machine learning](../09_fuels_properties/01_hydrogen_ammonia_properties/Pfa457cec99/README.md) | 氢氨燃料、着火与燃料性质预测 | provisional_q1_q2 | 已核对链接 |
| 2025 | [Enforcing physical conservation in neural network surrogate models for complex chemical kinetics](../01_chemistry_kinetics/01_surrogates_reduction/P221bc006b9/README.md) | 化学动力学代理、缩减与机理发现 | provisional_q1_q2 | 已核对链接 |
| 2025 | [Solving multiscale dynamical systems by deep learning](../01_chemistry_kinetics/01_surrogates_reduction/Pba328f5b75/README.md) | 化学动力学代理、缩减与机理发现 | pending_jcr | 已核对链接 |
| 2025 | [A Data-Driven Approach to Refine the Partially Stirred Reactor Closure for Turbulent Premixed Flames](../02_turbulence_closure/01_closures_manifolds/P8badc7f206/README.md) | 湍流燃烧闭合与流形模型 | pending_jcr | 已核对链接 |
| 2025 | [FlamePINN-1D: Physics-informed neural networks to solve forward and inverse problems of 1D laminar flames](../06_physics_informed/01_forward_inverse/P1cf521f2c6/README.md) | 物理信息学习与可微燃烧求解 | provisional_q1_q2 | 已核对链接 |
| 2025 | [A machine learning based approach for statistical analysis of detonation cells from soot foils](../07_engineering_design/03_supersonic_detonation/Peb8f5d8782/README.md) | 发动机、燃烧器与复杂推进系统设计 | provisional_q1_q2 | 已核对链接 |
| 2025 | [Comprehensive thermal-kinetic uncertainty quantification of lithium-ion battery thermal runaway via bayesian chemical reaction neural networks](../08_solid_fuels_fire/01_kinetics_fire/P81568f3c50/README.md) | 固体燃料、热解与火灾安全 | provisional_q1_q2 | 已核对链接 |
| 2025 | [Advancing Sustainable Aviation Fuel Design: Machine Learning for High-Energy-Density Liquid Polycyclic Hydrocarbons](../09_fuels_properties/01_hydrogen_ammonia_properties/Pca19045ded/README.md) | 氢氨燃料、着火与燃料性质预测 | provisional_q1_q2 | 已核对链接 |
| 2024 | [A machine learning method to predict rate constants for various reactions in combustion kinetic models](../01_chemistry_kinetics/01_surrogates_reduction/P2696c5ed02/README.md) | 化学动力学代理、缩减与机理发现 | provisional_q1_q2 | 已核对链接 |
| 2024 | [Uncertain lithium-ion cathode kinetic decomposition modeling via Bayesian chemical reaction neural networks](../01_chemistry_kinetics/02_discovery_calibration/P2384b1472e/README.md) | 化学动力学代理、缩减与机理发现 | provisional_q1_q2 | 已核对链接 |
| 2023 | [Deep learning dynamical latencies for the analysis and reduction of combustion chemistry kinetics](../01_chemistry_kinetics/01_surrogates_reduction/P0afc85ab6a/README.md) | 化学动力学代理、缩减与机理发现 | pending_jcr | 已核对链接 |
| 2023 | [Deep learning-based denoising for fast time-resolved flame emission spectroscopy in high-pressure combustion environment](../05_diagnostics_radiation/01_optical_inverse/P2949b85479/README.md) | 光学诊断、反演、烟炱与辐射 | provisional_q1_q2 | 已核对链接 |
| 2023 | [Physics-informed graph neural networks for predicting cetane number with systematic data quality analysis](../06_physics_informed/01_forward_inverse/Pad01f0053d/README.md) | 物理信息学习与可微燃烧求解 | provisional_q1_q2 | 已核对链接 |
| 2022 | [Adaptive global pathway selection using artificial neural networks: A-priori study](../01_chemistry_kinetics/02_discovery_calibration/P4a2b5d4efc/README.md) | 化学动力学代理、缩减与机理发现 | provisional_q1_q2 | 已核对链接 |
| 2022 | [A multi-scale sampling method for accurate and robust deep neural network to predict combustion chemical kinetics](../01_chemistry_kinetics/01_surrogates_reduction/P88f8a69095/README.md) | 化学动力学代理、缩减与机理发现 | provisional_q1_q2 | 已核对链接 |
| 2022 | [Data-driven discovery of heat release rate markers for premixed NH3/H2/air flames using physics-informed machine learning](../05_diagnostics_radiation/01_optical_inverse/Pd9de613208/README.md) | 光学诊断、反演、烟炱与辐射 | provisional_q1_q2 | 已核对链接 |
| 2022 | [Co-optimized machine-learned manifold models for large eddy simulation of turbulent combustion](../07_engineering_design/02_control_optimization/Pe07d955e64/README.md) | 发动机、燃烧器与复杂推进系统设计 | provisional_q1_q2 | 已核对链接 |
| 2022 | [Autonomous kinetic modeling of biomass pyrolysis using chemical reaction neural networks](../08_solid_fuels_fire/01_kinetics_fire/P4cbef1b3c9/README.md) | 固体燃料、热解与火灾安全 | provisional_q1_q2 | 已核对链接 |
| 2022 | [Active learning-based exploration of the catalytic pyrolysis of plastic waste](../08_solid_fuels_fire/01_kinetics_fire/P92264f9a97/README.md) | 固体燃料、热解与火灾安全 | provisional_q1_q2 | 已核对链接 |
| 2022 | [BLASTNet: A call for community-involved big data in combustion machine learning](../10_reviews_methods/01_reviews_datasets/P42e1959567/README.md) | 综述、数据集与共性方法 | pending_jcr | 已核对链接 |
| 2021 | [An a priori evaluation of a principal component and artificial neural network based combustion model in diesel engine conditions](../02_turbulence_closure/01_closures_manifolds/P15efd785db/README.md) | 湍流燃烧闭合与流形模型 | provisional_q1_q2 | 已核对链接 |
| 2020 | [Exploring the Chemical Space of Linear Alkane Pyrolysis via Deep Potential GENerator](../01_chemistry_kinetics/03_molecular_potentials/Pebb206703b/README.md) | 化学动力学代理、缩减与机理发现 | provisional_q1_q2 | 已核对链接 |
| 2020 | [Complex reaction processes in combustion unraveled by neural network-based molecular dynamics simulation](../01_chemistry_kinetics/03_molecular_potentials/P4a48f472f5/README.md) | 化学动力学代理、缩减与机理发现 | pending_jcr | 已核对链接 |
| 2020 | [Classification of solid fuels with machine learning](../08_solid_fuels_fire/01_kinetics_fire/P53dcbe4b04/README.md) | 固体燃料、热解与火灾安全 | provisional_q1_q2 | 已核对链接 |

[全部代码与支撑工具](../code_packages/README.md) · [复现协议](../docs/REPRODUCTION_PROTOCOL.md)
