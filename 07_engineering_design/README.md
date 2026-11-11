# 发动机、燃烧器与复杂推进系统设计

用代理、优化和控制在效率、排放、稳定性和成本之间寻找可用工况。

本目录含 74 条候选。分区与全文状态逐篇标注；自动分类以研究目标优先，交叉方法可在总库检索。

[返回首页](../README.md) · [全局地图](../00_literature_map/README.md) · [方法与范围](../docs/METHODOLOGY.md)

## 核心问题

预测/优化目标是什么，约束来自哪里？发动机排放回归、几何优化、喷雾与超声速燃烧需要不同保真度与验证手段。

## 方法演进与比较

树模型、MLP、时序模型、贝叶斯优化、多目标优化、强化学习、可解释性分析。响应面和优化算法应分别设置对照。

## 数据与物理定义

台架测量、CFD 参数扫描、喷雾图像、壁压与烟膜；保留工况、传感器、重复试验和数据来源。

## 怎样判断模型有效

效率/油耗、NOx/CO/烟炱、压损、稳定裕度、推力与不确定度；优化必须报告高保真复核结果，不能只报代理预测的最优点。

## 如何避免数据泄漏

按负荷、转速、喷油策略或几何留出，超参数选择使用训练内验证；重复试验归入同组。

## 主要局限与选题问题

优化器容易利用代理误差。相关性和 SHAP 不能单独证明因果；不同排放基准氧含量、干湿基和单位不可直接比较。

## 建议阅读和实践路径

先做有物理单位的基线预测，再加入不确定度与约束，最后做高保真闭环验证。爆轰胞格分割作为独立计量子任务。

## 细分类与论文索引

分区栏为二级来源线索；Q? 为待核实。代码 ✓ 仅表示论文链接已核对，不表示执行成功。

### [性能与排放](01_performance_emissions/README.md)（25）

| 年份 | 论文 | 分区线索 | 代码 |
|---|---|---|---|
| 2026 | [Computational analysis and deep learning forecasting of biogas-driven free-piston linear alternator combustion for livestock waste electrification](01_performance_emissions/Pab40983a78/README.md) | Q1 | 待核对 |
| 2026 | [Machine learning-based prediction of combustion behavior in HCCI engines using hydrogen-rich fuels](01_performance_emissions/P6a616b0e23/README.md) | Q1 | 待核对 |
| 2026 | [Machine learning assisted evaluation of emission characteristics in oxy-fuel combustion for a supercritical CO2 power cycle](01_performance_emissions/Pb39b66bdf4/README.md) | Q? | 待核对 |
| 2026 | [Machine learning based prediction of TOPSIS scores for internal combustion engine performance and emissions](01_performance_emissions/Pd301e41d92/README.md) | Q? | 待核对 |
| 2025 | [Waste to energy: Enhancing biogas utilization in dual-fuel engines using machine learning based prognostic analysis](01_performance_emissions/Pa5219ef61f/README.md) | Q1 | 待核对 |
| 2025 | [Helicopter turboshaft engines combustion chamber monitoring neural network method](01_performance_emissions/Pd5381ecb9b/README.md) | Q? | 待核对 |
| 2024 | [An emission predictive system for CO and NOx from gas turbine based on ensemble machine learning approach](01_performance_emissions/Pe28e2bf4f1/README.md) | Q1 | 待核对 |
| 2024 | [Assessment of ammonia-diesel fuel blends on compression ignition engine performance and emissions using machine learning techniques](01_performance_emissions/P27505fa842/README.md) | Q1 | 待核对 |
| 2024 | [Evaluating the feasibility of machine learning algorithms for combustion regime classification in biodiesel-fueled homogeneous charge compression ignition engines](01_performance_emissions/Pbca0bf1c15/README.md) | Q1 | 待核对 |
| 2024 | [Deep convolutional autoencoders for the time–space reconstruction of liquid rocket engine flames](01_performance_emissions/P7d07f3a167/README.md) | Q1 | 待核对 |
| 2024 | [Machine learning-driven screening of fuel additives for increased spark-ignition engine efficiency](01_performance_emissions/Pefc8dc6d89/README.md) | Q1 | 待核对 |
| 2023 | [Machine learning algorithms for a diesel engine fuelled with biodiesel blends and hydrogen using LSTM networks](01_performance_emissions/Pf37b81ce0c/README.md) | Q1 | 待核对 |
| 2023 | [A hybrid deep neural network model for NOx emission prediction of heavy oil-fired boiler flames](01_performance_emissions/P652827a18a/README.md) | Q1 | 待核对 |
| 2023 | [A Machine Learning Approach for Carbon di oxide and Other Emissions Characteristics Prediction in a Low Carbon Biofuel-Hydrogen Dual Fuel Engine](01_performance_emissions/P11f207ab6b/README.md) | Q1 | 待核对 |
| 2023 | [Applying physics-informed enhanced super-resolution generative adversarial networks to turbulent premixed combustion and engine-like flame kernel direct numerical simulation data](01_performance_emissions/P06c9e592c9/README.md) | Q1 | 待核对 |
| 2022 | [An ensemble deep learning model for exhaust emissions prediction of heavy oil-fired boiler combustion](01_performance_emissions/Pc52eb56359/README.md) | Q1 | 待核对 |
| 2022 | [Comparison and implementation of machine learning models for predicting the combustion phases of hydrogen-enriched Wankel rotary engines](01_performance_emissions/Pf74c335045/README.md) | Q1 | 待核对 |
| 2022 | [Machine learning based predictive modelling of micro gas turbine engine fuelled with microalgae blends on using LSTM networks: An experimental approach](01_performance_emissions/P4b0d59cf45/README.md) | Q1 | 待核对 |
| 2021 | [Convolutional neural network-based deep transfer learning for fault detection of gas turbine combustion chambers](01_performance_emissions/P3bd95ea3fe/README.md) | Q1 | 待核对 |
| 2021 | [Machine Learning of ignition delay times under dual-fuel engine conditions](01_performance_emissions/Pb6e28c9d51/README.md) | Q1 | 待核对 |
| 2021 | [Investigation of cycle-to-cycle variations in a spark-ignition engine based on a machine learning analysis of the early flame kernel](01_performance_emissions/Pb38c1251ee/README.md) | Q1 | 待核对 |
| 2020 | [Prediction of hydrogen-added combustion process in T-GDI engine using artificial neural network](01_performance_emissions/P16185ba518/README.md) | Q1 | 待核对 |
| 2020 | [In-cylinder soot concentration measurement by Neural Network Two Colour technique (NNTC) on a GDI engine](01_performance_emissions/Pe09696c80d/README.md) | Q1 | 待核对 |
| 2019 | [Neural network prediction of cycle-to-cycle power variability in a spark-ignited internal combustion engine](01_performance_emissions/Pd596d5abbb/README.md) | Q1 | 待核对 |
| 2018 | [Study on influencing factors of prediction accuracy of support vector machine (SVM) model for NOx emission of a hydrogen enriched compressed natural gas engine](01_performance_emissions/P256842181d/README.md) | Q1 | 待核对 |

### [控制与多目标设计](02_control_optimization/README.md)（18）

| 年份 | 论文 | 分区线索 | 代码 |
|---|---|---|---|
| 2026 | [Machine learning-enabled wide-condition combustion behavior and optimization for oxygen-enriched ammonia-fueled Wankel rotary engines](02_control_optimization/Pb31e5867e2/README.md) | Q1 | 待核对 |
| 2026 | [Machine learning-based multi-objective optimization of NH3/H2 combustion under H2O/N2 dilution with consideration of flame instability](02_control_optimization/P19c7402975/README.md) | Q? | 待核对 |
| 2026 | [Boiler combustion optimization via offline reinforcement learning with an ensemble high-dimensional environment](02_control_optimization/P9066b88693/README.md) | Q? | 待核对 |
| 2026 | [Machine learning-based prediction and optimization of performance and emission characteristics in CI engines fueled by pumpkin seed biodiesel with thermal barrier coating and cerium oxide nanoparticles](02_control_optimization/P52135718f6/README.md) | Q1 | 待核对 |
| 2026 | [Multi-objective optimization for a spark ignition methanol marine engine based on multi-task learning and NSGA-II](02_control_optimization/P82746f89ba/README.md) | Q1 | 待核对 |
| 2026 | [Machine learning-assisted optimization of thermodynamics and combustion in hydrogen argon power cycle engines](02_control_optimization/Pcd07b2bc67/README.md) | Q1 | 待核对 |
| 2026 | [Adaptive neural network controller for CA50 optimization under multiple constraints in hydrogen internal combustion engines](02_control_optimization/Pedb6ebb213/README.md) | Q1 | 待核对 |
| 2026 | [A reinforcement-learning-augmented liquid-fueled reactor network model for predicting lean blowout in gas turbine combustors](02_control_optimization/P3ecd14877e/README.md) | Q1 | 待核对 |
| 2026 | [Progress variable optimization using encoder-residual neural networks for supercritical and transcritical flames](02_control_optimization/Pff53004340/README.md) | Q1 | 待核对 |
| 2025 | [Research on multi-objective optimization control of diesel engine combustion process based on model predictive control-guided reinforcement learning method](02_control_optimization/Pe2316c22a7/README.md) | Q? | 待核对 |
| 2024 | [Optimized synthetic data and semi-supervised learning for Derived Cetane Number prediction](02_control_optimization/P538e035aa8/README.md) | Q1 | 待核对 |
| 2023 | [Surrogate modeling of parameterized multi-dimensional premixed combustion with physics-informed neural networks for rapid exploration of design space](02_control_optimization/Pa3f1a46d39/README.md) | Q1 | 待核对 |
| 2023 | [Multi-objective optimization for combustion, thermodynamic and emission characteristics of Atkinson cycle engine using tree-based machine learning and the NSGA II algorithm](02_control_optimization/Pd34d501d6b/README.md) | Q1 | 待核对 |
| 2022 | [Co-optimized machine-learned manifold models for large eddy simulation of turbulent combustion](02_control_optimization/Pe07d955e64/README.md) | Q1 | ✓ |
| 2022 | [Low NOx combustion optimization based on partial dimension opposition-based learning particle swarm optimization](02_control_optimization/P9ae7d9c405/README.md) | Q1 | 待核对 |
| 2022 | [Application of machine learning to optimize the combustion characteristics of RCCI engine over wide load range](02_control_optimization/P077e579089/README.md) | Q1 | 待核对 |
| 2020 | [Machine learning enabled high-throughput screening of hydrocarbon molecules for the design of next generation fuels](02_control_optimization/Pf939553d43/README.md) | Q1 | 待核对 |
| 2020 | [Optimization of diesel engine operating parameters fueled with palm oil-diesel blend: Comparative evaluation between response surface methodology (RSM) and artificial neural network (ANN)](02_control_optimization/P2531341519/README.md) | Q1 | 待核对 |

### [超声速燃烧与爆轰](03_supersonic_detonation/README.md)（15）

| 年份 | 论文 | 分区线索 | 代码 |
|---|---|---|---|
| 2026 | [A POD-driven deep learning prediction model for supersonic combustion](03_supersonic_detonation/P6d962991e9/README.md) | Q1 | 待核对 |
| 2026 | [Flow field reconstruction of rotating detonation combustors via neural implicit representation](03_supersonic_detonation/Pbd625108a2/README.md) | Q1 | 待核对 |
| 2026 | [ZND-guided low-dimensional manifold sampling for artificial-neural-network-accelerated simulation of oblique detonation](03_supersonic_detonation/Pe513fb1e6d/README.md) | Q1 | 待核对 |
| 2025 | [Supersonic combustion flow field reconstruction in a scramjet based on deep learning method](03_supersonic_detonation/Pa078cd1e31/README.md) | Q1 | 待核对 |
| 2025 | [A machine learning based approach for statistical analysis of detonation cells from soot foils](03_supersonic_detonation/Peb8f5d8782/README.md) | Q1 | ✓ |
| 2025 | [Stabilization analysis and mode recognition of kerosene supersonic Combustion: A deep learning approach based on Res-CNN-β-VAE](03_supersonic_detonation/P662969d2d0/README.md) | Q1 | 待核对 |
| 2025 | [Spatiotemporal prediction of scramjet combustion based on simpler yet better video prediction neural network](03_supersonic_detonation/Pad9ee054b6/README.md) | Q? | 待核对 |
| 2025 | [Combustion mode time-series prediction in rotating detonation combustor based on predictor of encoder transformer](03_supersonic_detonation/P9fa3854611/README.md) | Q? | 待核对 |
| 2024 | [Physics-informed recurrent super-resolution generative reconstruction in rotating detonation combustor](03_supersonic_detonation/Pcf48c42d36/README.md) | Q1 | 待核对 |
| 2023 | [Flame development prediction of supersonic combustion flow based on lightweight cascaded convolutional neural network](03_supersonic_detonation/Pc05a3456cd/README.md) | Q? | 待核对 |
| 2023 | [Reconstructing the flame in supersonic combustion flow by using the distribution of the wall pressure based on deep learning](03_supersonic_detonation/P88fd4d65bd/README.md) | Q? | 待核对 |
| 2023 | [Predicting combustion behavior in rotating detonation engines using an interpretable deep learning method](03_supersonic_detonation/P22eaaf5068/README.md) | Q? | 待核对 |
| 2022 | [A reconstruction method of detonation wave surface based on convolutional neural network](03_supersonic_detonation/P16bb712d58/README.md) | Q1 | 待核对 |
| 2021 | [Learning dominant physical processes with data-driven balance models](03_supersonic_detonation/P3fe49a4002/README.md) | Q? | ✓ |
| 2020 | [Reconstructing cellular surface of gaseous detonation based on artificial neural network and proper orthogonal decomposition](03_supersonic_detonation/P88108ab606/README.md) | Q1 | 待核对 |

### [喷雾、液滴与喷注](04_sprays_injection/README.md)（16）

| 年份 | 论文 | 分区线索 | 代码 |
|---|---|---|---|
| 2026 | [A deep neural kernel approach with balanced clustering for flamelet modeling of spray flames](04_sprays_injection/P2bcf4ea592/README.md) | Q1 | 待核对 |
| 2026 | [Experimental study on spray characteristics of aviation kerosene Air-Water-Assisted injection system based on neural network algorithm](04_sprays_injection/P9602c6d49c/README.md) | Q1 | 待核对 |
| 2026 | [A reinforcement-learning framework for the control of fuel-vapour stratification via oscillating electric fields](04_sprays_injection/P79d980352b/README.md) | Q1 | 待核对 |
| 2025 | [Combustion machine learning of superheated butanol atomization in optical GDI engine](04_sprays_injection/P326fa83027/README.md) | Q? | 待核对 |
| 2024 | [Advancing Fuel Spray Characterization: A Machine Learning Approach for Directly Injected Gasoline Fuel Sprays](04_sprays_injection/P07dc4fd051/README.md) | Q1 | 待核对 |
| 2024 | [Machine learning assisted characterisation and prediction of droplet distributions in a liquid jet in cross-flow](04_sprays_injection/P28e31e035e/README.md) | Q1 | 待核对 |
| 2023 | [A machine learning framework for evaluating the biodiesel properties for accurate modeling of spray and combustion processes](04_sprays_injection/P51a46d5be1/README.md) | Q1 | 待核对 |
| 2023 | [Artificial neural network models for phase equilibrium predictions under engine trans/supercritical spray conditions](04_sprays_injection/Paca26f23b3/README.md) | Q1 | 待核对 |
| 2023 | [Simulation and neural network analysis of spreading the oblique fuel jet impinging onto concave walls](04_sprays_injection/P33cbfc19d8/README.md) | Q1 | 待核对 |
| 2022 | [Efficient modeling of the filtered density function in turbulent sprays using ensemble learning](04_sprays_injection/Pad34191301/README.md) | Q1 | 待核对 |
| 2022 | [An estimation method of the fuel mass injected in large injections in Common-Rail diesel engines based on system identification using artificial neural network](04_sprays_injection/P1b1127c217/README.md) | Q1 | 待核对 |
| 2022 | [Spray characteristics of diesel, biodiesel, polyoxymethylene dimethyl ethers blends and prediction of spray tip penetration using artificial neural network](04_sprays_injection/P55aa0561c4/README.md) | Q? | 待核对 |
| 2021 | [Machine-learning enabled prediction of 3D spray under engine combustion network spray G conditions](04_sprays_injection/P6e3db03fab/README.md) | Q1 | 待核对 |
| 2021 | [Conditional scalar dissipation rate modeling for turbulent spray flames using artificial neural networks](04_sprays_injection/P8e74145581/README.md) | Q1 | 待核对 |
| 2020 | [Application of artificial neural network and response surface methodology for predicting and optimizing dual-fuel CI engine characteristics using hydrogen and bio fuel with water injection](04_sprays_injection/Pd7c465cef0/README.md) | Q1 | 待核对 |
| 2019 | [Hydraulic dynamics in split fuel injection on a common rail system and their artificial neural network prediction](04_sprays_injection/P8d69fb2d31/README.md) | Q1 | 待核对 |
