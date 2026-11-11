# 代码优先阅读路线

先看许可与数据，再看入口。表中有作者实现、组件、教程、相关工作与题名匹配；详细关系见论文卡。除 C01 作者推理演示与 C02 预印本单工况外，未执行训练；完整期刊论文复现仍未验收。建议顺序：轻量辐射 → FlamePINN → SL-GPS/CMLM → CRNN → 后验 CFD。受限或缺许可的代码保留固定链接。

[详细研究路线](RESEARCH_ROADMAP.md) · [逐篇入口和数据可用性](OPEN_WORK_INDEX.md)

| 年份 | 论文 | 方向 | 分区状态 | 代码 |
|---|---|---|---|---|
| 2026 | [DFODE-Kit: Deep learning package for solving flame chemical kinetics with high-dimensional stiff ordinary differential equations](../01_chemistry_kinetics/01_surrogates_reduction/P485814185d/README.md) | 化学动力学代理、缩减与机理发现 | pending_jcr | 已核对链接 |
| 2026 | [Enhancing deep learning of ammonia/natural gas combustion kinetics via physics-aware data augmentation and scale separation](../01_chemistry_kinetics/01_surrogates_reduction/P208595837d/README.md) | 化学动力学代理、缩减与机理发现 | provisional_q1_q2 | 已核对链接 |
| 2026 | [Data-based filtered dissipation rate modelling for multi-modal turbulent combustion: evaluating a priori model generalizability](../literature/adjacent/P2bf9290361/README.md) | 湍流燃烧闭合与流形模型 | adjacent_q3_q4 | 已核对链接 |
| 2026 | [Deep learning for continuous lead-time prediction of thermoacoustic instabilities in an annular combustor](../04_instability_control/01_prediction_identification/P51fe566a45/README.md) | 热声不稳定性预测、辨识与控制 | provisional_q1_q2 | 已核对链接 |
| 2026 | [Neural refractive index primitives for flame field reconstruction using background-oriented schlieren](../05_diagnostics_radiation/01_optical_inverse/Pc2b8d1f214/README.md) | 光学诊断、反演、烟炱与辐射 | provisional_q1_q2 | 已核对链接 |
| 2026 | [Integrated neural network approach for autonomous sensitivity analysis and optimization of sectional soot kinetic modeling](../05_diagnostics_radiation/03_soot_formation/Pe31f2bea9d/README.md) | 光学诊断、反演、烟炱与辐射 | provisional_q1_q2 | 已核对链接 |
| 2026 | [Physics-informed neural network WSGG model for radiative heat transfer in H2O–CO2–NH3 gas mixtures relevant to ammonia combustion](../05_diagnostics_radiation/02_radiation_soot/P69b4098fb3/README.md) | 光学诊断、反演、烟炱与辐射 | provisional_q1_q2 | 已核对链接 |
| 2026 | [CFD analysis of operating parameters and machine learning-aided optimization of reactor performance in a polyethylene pyrolysis fluidized bed](../08_solid_fuels_fire/01_kinetics_fire/Pd715d789f0/README.md) | 固体燃料、热解与火灾安全 | provisional_q1_q2 | 已核对链接 |
| 2026 | [BayeSAF: Emulation and design of sustainable alternative fuels via Bayesian inference and descriptors-based machine learning](../09_fuels_properties/01_hydrogen_ammonia_properties/Pfa457cec99/README.md) | 氢氨燃料、着火与燃料性质预测 | provisional_q1_q2 | 已核对链接 |
| 2025 | [Enforcing physical conservation in neural network surrogate models for complex chemical kinetics](../01_chemistry_kinetics/01_surrogates_reduction/P221bc006b9/README.md) | 化学动力学代理、缩减与机理发现 | provisional_q1_q2 | 已核对链接 |
| 2025 | [Solving multiscale dynamical systems by deep learning](../01_chemistry_kinetics/01_surrogates_reduction/Pba328f5b75/README.md) | 化学动力学代理、缩减与机理发现 | pending_jcr | 已核对链接 |
| 2025 | [Comprehensive deep learning for combustion chemistry integration: Multi-fuel generalization and a posteriori validation in reacting flow](../01_chemistry_kinetics/01_surrogates_reduction/Pdd9a1fb317/README.md) | 化学动力学代理、缩减与机理发现 | pending_jcr | 已核对链接 |
| 2025 | [A Data-Driven Approach to Refine the Partially Stirred Reactor Closure for Turbulent Premixed Flames](../02_turbulence_closure/01_closures_manifolds/P8badc7f206/README.md) | 湍流燃烧闭合与流形模型 | pending_jcr | 已核对链接 |
| 2025 | [a priori uncertainty quantification of reacting turbulence closure models using Bayesian neural networks](../02_turbulence_closure/01_closures_manifolds/P71c16d5cb2/README.md) | 湍流燃烧闭合与流形模型 | provisional_q1_q2 | 已核对链接 |
| 2025 | [SAGE: A machine learning model for primary particle segmentation in TEM images of soot aggregates](../05_diagnostics_radiation/01_optical_inverse/P56771c427a/README.md) | 光学诊断、反演、烟炱与辐射 | provisional_q1_q2 | 已核对链接 |
| 2025 | [FlamePINN-1D: Physics-informed neural networks to solve forward and inverse problems of 1D laminar flames](../06_physics_informed/01_forward_inverse/P1cf521f2c6/README.md) | 物理信息学习与可微燃烧求解 | provisional_q1_q2 | 已核对链接 |
| 2025 | [A machine learning based approach for statistical analysis of detonation cells from soot foils](../07_engineering_design/03_supersonic_detonation/Peb8f5d8782/README.md) | 发动机、燃烧器与复杂推进系统设计 | provisional_q1_q2 | 已核对链接 |
| 2025 | [Comprehensive thermal-kinetic uncertainty quantification of lithium-ion battery thermal runaway via bayesian chemical reaction neural networks](../08_solid_fuels_fire/01_kinetics_fire/P81568f3c50/README.md) | 固体燃料、热解与火灾安全 | provisional_q1_q2 | 已核对链接 |
| 2025 | [Advancing Sustainable Aviation Fuel Design: Machine Learning for High-Energy-Density Liquid Polycyclic Hydrocarbons](../09_fuels_properties/01_hydrogen_ammonia_properties/Pca19045ded/README.md) | 氢氨燃料、着火与燃料性质预测 | provisional_q1_q2 | 已核对链接 |
| 2024 | [A machine learning method to predict rate constants for various reactions in combustion kinetic models](../01_chemistry_kinetics/01_surrogates_reduction/P2696c5ed02/README.md) | 化学动力学代理、缩减与机理发现 | provisional_q1_q2 | 已核对链接 |
| 2024 | [Uncertain lithium-ion cathode kinetic decomposition modeling via Bayesian chemical reaction neural networks](../01_chemistry_kinetics/02_discovery_calibration/P2384b1472e/README.md) | 化学动力学代理、缩减与机理发现 | provisional_q1_q2 | 已核对链接 |
| 2024 | [Data-based instantaneous conditional progress variable dissipation rate modeling for turbulent premixed combustion](../02_turbulence_closure/01_closures_manifolds/P2fc75bd437/README.md) | 湍流燃烧闭合与流形模型 | provisional_q1_q2 | 已核对链接 |
| 2024 | [Learning stiff chemical kinetics using extended deep neural operators](../03_operators_reconstruction/01_operators_rom/P98c59b685b/README.md) | 神经算子、降阶与流场重建 | provisional_q1_q2 | 已核对链接 |
| 2024 | [Inferring unknown unknowns: Regularized bias-aware ensemble Kalman filter](../04_instability_control/01_prediction_identification/P0783e678e5/README.md) | 热声不稳定性预测、辨识与控制 | provisional_q1_q2 | 已核对链接 |
| 2024 | [A real-time digital twin of azimuthal thermoacoustic instabilities](../04_instability_control/01_prediction_identification/P0e5f9b5e09/README.md) | 热声不稳定性预测、辨识与控制 | pending_jcr | 已核对链接 |
| 2024 | [Data-driven computation of adjoint sensitivities without adjoint solvers: An application to thermoacoustics](../04_instability_control/02_control/P9903dd056c/README.md) | 热声不稳定性预测、辨识与控制 | pending_jcr | 已核对链接 |
| 2023 | [DeepFlame: A deep learning empowered open-source platform for reacting flow simulations](../01_chemistry_kinetics/01_surrogates_reduction/P9b9c10a9d8/README.md) | 化学动力学代理、缩减与机理发现 | pending_jcr | 已核对链接 |
| 2023 | [Deep learning dynamical latencies for the analysis and reduction of combustion chemistry kinetics](../01_chemistry_kinetics/01_surrogates_reduction/P0afc85ab6a/README.md) | 化学动力学代理、缩减与机理发现 | pending_jcr | 已核对链接 |
| 2023 | [Hard-constrained neural networks for modeling nonlinear acoustics](../04_instability_control/01_prediction_identification/Pa68d424897/README.md) | 热声不稳定性预测、辨识与控制 | pending_jcr | 已核对链接 |
| 2023 | [Deep learning-based denoising for fast time-resolved flame emission spectroscopy in high-pressure combustion environment](../05_diagnostics_radiation/01_optical_inverse/P2949b85479/README.md) | 光学诊断、反演、烟炱与辐射 | provisional_q1_q2 | 已核对链接 |
| 2023 | [Physics-informed graph neural networks for predicting cetane number with systematic data quality analysis](../06_physics_informed/01_forward_inverse/Pad01f0053d/README.md) | 物理信息学习与可微燃烧求解 | provisional_q1_q2 | 已核对链接 |
| 2022 | [Adaptive global pathway selection using artificial neural networks: A-priori study](../01_chemistry_kinetics/02_discovery_calibration/P4a2b5d4efc/README.md) | 化学动力学代理、缩减与机理发现 | provisional_q1_q2 | 已核对链接 |
| 2022 | [A multi-scale sampling method for accurate and robust deep neural network to predict combustion chemical kinetics](../01_chemistry_kinetics/01_surrogates_reduction/P88f8a69095/README.md) | 化学动力学代理、缩减与机理发现 | provisional_q1_q2 | 已核对链接 |
| 2022 | [Real-time thermoacoustic data assimilation](../04_instability_control/01_prediction_identification/P97829e9574/README.md) | 热声不稳定性预测、辨识与控制 | pending_jcr | 已核对链接 |
| 2022 | [Data-driven discovery of heat release rate markers for premixed NH3/H2/air flames using physics-informed machine learning](../05_diagnostics_radiation/01_optical_inverse/Pd9de613208/README.md) | 光学诊断、反演、烟炱与辐射 | provisional_q1_q2 | 已核对链接 |
| 2022 | [Physics-informed neural networks and functional interpolation for stiff chemical kinetics](../06_physics_informed/01_forward_inverse/P42f2fcf650/README.md) | 物理信息学习与可微燃烧求解 | pending_jcr | 已核对链接 |
| 2022 | [Co-optimized machine-learned manifold models for large eddy simulation of turbulent combustion](../07_engineering_design/02_control_optimization/Pe07d955e64/README.md) | 发动机、燃烧器与复杂推进系统设计 | provisional_q1_q2 | 已核对链接 |
| 2022 | [Autonomous kinetic modeling of biomass pyrolysis using chemical reaction neural networks](../08_solid_fuels_fire/01_kinetics_fire/P4cbef1b3c9/README.md) | 固体燃料、热解与火灾安全 | provisional_q1_q2 | 已核对链接 |
| 2022 | [Active learning-based exploration of the catalytic pyrolysis of plastic waste](../08_solid_fuels_fire/01_kinetics_fire/P92264f9a97/README.md) | 固体燃料、热解与火灾安全 | provisional_q1_q2 | 已核对链接 |
| 2022 | [BLASTNet: A call for community-involved big data in combustion machine learning](../10_reviews_methods/01_reviews_datasets/P42e1959567/README.md) | 综述、数据集与共性方法 | pending_jcr | 已核对链接 |
| 2022 | [Combustion machine learning: Principles, progress and prospects](../10_reviews_methods/01_reviews_datasets/Pb73c9cc517/README.md) | 综述、数据集与共性方法 | provisional_q1_q2 | 已核对链接 |
| 2021 | [An a priori evaluation of a principal component and artificial neural network based combustion model in diesel engine conditions](../02_turbulence_closure/01_closures_manifolds/P15efd785db/README.md) | 湍流燃烧闭合与流形模型 | provisional_q1_q2 | 已核对链接 |
| 2021 | [Robust identification of flame frequency response via multi-fidelity Gaussian process approach](../04_instability_control/01_prediction_identification/P67741bfd8c/README.md) | 热声不稳定性预测、辨识与控制 | provisional_q1_q2 | 已核对链接 |
| 2021 | [A machine learning based full-spectrum correlated k-distribution model for nonhomogeneous gas-soot mixtures](../05_diagnostics_radiation/02_radiation_soot/Pe01c5a5aac/README.md) | 光学诊断、反演、烟炱与辐射 | pending_jcr | 已核对链接 |
| 2021 | [Learning dominant physical processes with data-driven balance models](../07_engineering_design/03_supersonic_detonation/P3fe49a4002/README.md) | 发动机、燃烧器与复杂推进系统设计 | pending_jcr | 已核对链接 |
| 2021 | [Deep reinforcement learning for dynamic control of fuel injection timing in multi-pulse compression ignition engines](../literature/adjacent/Pd9e3925a87/README.md) | 发动机、燃烧器与复杂推进系统设计 | adjacent_q3_q4 | 已核对链接 |
| 2020 | [Adaptive chemistry via pre-partitioning of composition space and mechanism reduction](../01_chemistry_kinetics/01_surrogates_reduction/P8c8c05b2bc/README.md) | 化学动力学代理、缩减与机理发现 | provisional_q1_q2 | 已核对链接 |
| 2020 | [Chemistry reduction using machine learning trained from non-premixed micro-mixing modeling: Application to DNS of a syngas turbulent oxy-flame with side-wall effects](../01_chemistry_kinetics/01_surrogates_reduction/Pe1482ded9f/README.md) | 化学动力学代理、缩减与机理发现 | provisional_q1_q2 | 已核对链接 |
| 2020 | [Exploring the Chemical Space of Linear Alkane Pyrolysis via Deep Potential GENerator](../01_chemistry_kinetics/03_molecular_potentials/Pebb206703b/README.md) | 化学动力学代理、缩减与机理发现 | provisional_q1_q2 | 已核对链接 |
| 2020 | [Complex reaction processes in combustion unraveled by neural network-based molecular dynamics simulation](../01_chemistry_kinetics/03_molecular_potentials/P4a48f472f5/README.md) | 化学动力学代理、缩减与机理发现 | pending_jcr | 已核对链接 |
| 2020 | [Classification of solid fuels with machine learning](../08_solid_fuels_fire/01_kinetics_fire/P53dcbe4b04/README.md) | 固体燃料、热解与火灾安全 | provisional_q1_q2 | 已核对链接 |

[全部代码与支撑工具](../code_packages/README.md) · [复现协议](../docs/REPRODUCTION_PROTOCOL.md)
