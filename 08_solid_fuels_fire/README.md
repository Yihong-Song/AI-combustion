# 固体燃料、热解与火灾安全

从热分析到火焰图像，研究固体如何分解、着火、放热，以及怎样预测火灾风险。

本目录含 83 条候选。分区与全文状态逐篇标注；自动分类以研究目标优先，交叉方法可在总库检索。

[返回首页](../README.md) · [全局地图](../00_literature_map/README.md) · [方法与范围](../docs/METHODOLOGY.md)

## 核心问题

对象是 TGA 动力学、燃料分类、火蔓延、热释放率还是电池热失控？热解产率与燃烧过程存在联系，但不属于同一验证任务。

## 方法演进与比较

ANN/RF、CRNN/Neural ODE、Bayesian CRNN、视觉模型、多模态时序；金属/固体推进剂单列。

## 数据与物理定义

TGA/DSC、升温速率、气氛、燃料组成、热流与火焰图像；记录原始实验来源与批次。

## 怎样判断模型有效

质量/失重速率、热流、点火时间、HRR 曲线、蔓延速度；安全模型需报告预测区间和漏警，不能只报平均 R2。

## 如何避免数据泄漏

按燃料种类、实验批次、升温速率或火场划分；相同配方多次采样不是独立材料。

## 主要局限与选题问题

热重实验有效动力学存在补偿效应和不可辨识性。材料、尺度和传热条件变化会破坏直接外推。生物油生产类文献作为交叉候选进一步筛选。

## 建议阅读和实践路径

先读 Biomass.jl 的质量作用/Arrhenius 结构，再推进到 Bayesian CRNN；图像 HRR 与数值热解分开验证。

## 细分类与论文索引

分区栏为二级来源线索；Q? 为待核实。代码 ✓ 仅表示论文链接已核对，不表示执行成功。

### [生物质、煤、热解与火灾](01_kinetics_fire/README.md)（77）

| 年份 | 论文 | 分区线索 | 代码 |
|---|---|---|---|
| 2026 | [Prediction of structural evolution during coal pyrolysis with metropolis Monte Carlo and deep learning](01_kinetics_fire/P55a965d011/README.md) | Q1 | 待核对 |
| 2026 | [Investigation on the general predictive model of the kinetic parameters of coal char combustion based on deep neural network](01_kinetics_fire/P7ec179b106/README.md) | Q1 | 待核对 |
| 2026 | [Machine learning and SHapley Additive exPlanations to predict product characteristics from coal and plastic co-pyrolysis](01_kinetics_fire/Pbe54df9ba8/README.md) | Q1 | 待核对 |
| 2026 | [Prediction of NOx emission from a 600 MW coal-fired boiler with deep learning: Plant data learned by Gini index and lightweight convolutional neural network](01_kinetics_fire/P78790ab1f3/README.md) | Q1 | 待核对 |
| 2026 | [Automated machine learning for bio-oil yield prediction from lignocellulosic biomass pyrolysis](01_kinetics_fire/P8ce0569ba0/README.md) | Q1 | 待核对 |
| 2026 | [Surrogate model-integrated deep reinforcement learning for temperature and pyrolysis behavior control in the coal coking process](01_kinetics_fire/Pfcab35802f/README.md) | Q1 | 待核对 |
| 2026 | [Investigation and classification of pore-fracture characteristics in oil shale after high-temperature steam pyrolysis based on machine learning](01_kinetics_fire/Pa0ab805268/README.md) | Q1 | 待核对 |
| 2026 | [CFD analysis of operating parameters and machine learning-aided optimization of reactor performance in a polyethylene pyrolysis fluidized bed](01_kinetics_fire/Pd715d789f0/README.md) | Q1 | ✓ |
| 2026 | [Addressing the nonlinear gas-temperature relationship in coal spontaneous combustion: A machine learning model and its validation](01_kinetics_fire/P97f0ba2687/README.md) | Q1 | 待核对 |
| 2026 | [Predicting and optimizing pyrolysis behaviors of Shendong coal macerals (vitrinite & inertinite) swelled by single and mixed solvents with machine learning](01_kinetics_fire/Pdbf969dad2/README.md) | Q1 | 待核对 |
| 2026 | [Machine learning enhanced time-resolved multi-particle tracking velocimetry in solid fuel particle group combustion](01_kinetics_fire/P677f3e7df2/README.md) | Q? | 待核对 |
| 2026 | [Machine-learning-enabled three-dimensional firebrand transport characterisation: combustion enhancement, morphology and rotational dynamics](01_kinetics_fire/Pdb76fec194/README.md) | Q1 | 待核对 |
| 2026 | [A molecular descriptor-driven machine learning framework for mixed plastic pyrolysis: reactivity prediction and mechanistic insights](01_kinetics_fire/P9120b5e507/README.md) | Q1 | 待核对 |
| 2026 | [Physics-informed thermo-kinetic learning for data-efficient prediction of battery thermal runaway across chemistries](01_kinetics_fire/P07f86c563b/README.md) | Q1 | 待核对 |
| 2026 | [Hierarchical data assimilation for learning pyrolysis and oxidation kinetics from heterogeneous data sources](01_kinetics_fire/P9c031abcb2/README.md) | Q1 | 待核对 |
| 2025 | [Comprehensive thermal-kinetic uncertainty quantification of lithium-ion battery thermal runaway via bayesian chemical reaction neural networks](01_kinetics_fire/P81568f3c50/README.md) | Q1 | ✓ |
| 2025 | [An experimental and modeling study on norbornane pyrolysis aided by chemical information from neural network-assisted molecular dynamics](01_kinetics_fire/P35061649e3/README.md) | Q1 | 待核对 |
| 2025 | [BoilerNet: Deep reinforcement learning-based combustion optimization network for pulverized coal boiler](01_kinetics_fire/P9e4cc96d59/README.md) | Q? | 待核对 |
| 2025 | [Study on biomass and polymer catalytic co-pyrolysis product characteristics using machine learning and shapley additive explanations (SHAP)](01_kinetics_fire/P4ebc1f16a9/README.md) | Q1 | 待核对 |
| 2025 | [Atmosphere-driven mechanisms in biogas residue chemical looping pyrolysis: Insights from kinetic characteristic and machine learning prediction](01_kinetics_fire/P3dadb88d9f/README.md) | Q1 | 待核对 |
| 2025 | [Critical assessment of machine learning prediction of biomass pyrolysis](01_kinetics_fire/P2c514ccc8a/README.md) | Q1 | 待核对 |
| 2025 | [One-step pyrolysis model integrating machine learning predictions for coal gasification simulations using multiphase particle-in-cell method](01_kinetics_fire/Pc3a44a1e49/README.md) | Q1 | 待核对 |
| 2025 | [Research on the migration and transformation law of sulfur in a molten salt heating tire pyrolysis reactor: Experiments and neural network field-driven molecular dynamics simulations](01_kinetics_fire/P7b116d683c/README.md) | Q1 | 待核对 |
| 2025 | [Machine learning prediction of pore structure and nitrogen content of N-doped biochar derived from biomass pyrolysis: Effects of biomass elemental compositions, preparation processes, and preparation methods](01_kinetics_fire/P9d74a6bd73/README.md) | Q1 | 待核对 |
| 2025 | [Feasibility assessment of online coal quality monitoring based on concentrating photothermal rapid combustion: Insights from neural network and explainability analysis](01_kinetics_fire/Pd341a958d0/README.md) | Q1 | 待核对 |
| 2025 | [Optimizing biomass combustion and mitigating potassium induced slag formation with deep learning](01_kinetics_fire/P2faf746f06/README.md) | Q1 | 待核对 |
| 2025 | [Super-resolution reconstruction of scalar fields from the pyrolysis of pulverised biomass using deep learning](01_kinetics_fire/Pd33471dae9/README.md) | Q1 | 待核对 |
| 2024 | [A spatio-temporal temperature prediction model for coal spontaneous combustion based on back propagation neural network](01_kinetics_fire/P875b452f79/README.md) | Q? | 待核对 |
| 2024 | [Machine learning-enabled analysis of product distribution and composition in biomass-coal co-pyrolysis](01_kinetics_fire/P772b607a19/README.md) | Q1 | 待核对 |
| 2024 | [Unraveling pyrolysis mechanisms of lignin dimer model compounds: Neural network-based molecular dynamics simulation investigations](01_kinetics_fire/Pdcdd6680ea/README.md) | Q1 | 待核对 |
| 2024 | [On-line combustion optimization framework for coal-fired boiler combining improved cultural algorithm, deep learning, multi-objective evolutionary algorithm with improved case-based reasoning technology](01_kinetics_fire/Pf5a259503e/README.md) | Q1 | 待核对 |
| 2024 | [Investigation on coal/coal gangue mixtures co-combustion via TG-DSC tests, multicomponent reaction model, and artificial neural network](01_kinetics_fire/Pa55df281e1/README.md) | Q1 | 待核对 |
| 2024 | [A hybrid deep learning modeling based on lumped parameter model of coal-fired circulating fluidized beds for real-time prediction](01_kinetics_fire/P80134270aa/README.md) | Q1 | 待核对 |
| 2024 | [Fuel composition forecasting for waste tires pyrolysis process based on machine learning methods](01_kinetics_fire/P7fc248813d/README.md) | Q1 | 待核对 |
| 2024 | [Enhancing pyrolysis process monitoring and prediction for biomass: A machine learning approach](01_kinetics_fire/P1700e0d3e9/README.md) | Q1 | 待核对 |
| 2024 | [A physics-informed neural network that considers monotonic relationships for predicting NO emissions from coal-fired boilers](01_kinetics_fire/Pec0a4d3ffa/README.md) | Q1 | 待核对 |
| 2024 | [Enhancing biomass Pyrolysis: Predictive insights from process simulation integrated with interpretable Machine learning models](01_kinetics_fire/P6decd800bb/README.md) | Q1 | 待核对 |
| 2024 | [Study of the catalytic pyrolysis mechanism of guaiacol over seaweed-derived carbon catalyst: Based on density function theory and machine learning](01_kinetics_fire/Pcaa2f3d439/README.md) | Q1 | 待核对 |
| 2024 | [Pyrolysis behaviour of ultrafiltration polymer composite membranes (PSF/PET): Kinetic, thermodynamic, prediction modelling using artificial neural network and volatile product analysis](01_kinetics_fire/P027a573fb9/README.md) | Q1 | 待核对 |
| 2024 | [Investigation of sawdust microwave-assisted pyrolysis by machine learning, Part I: Optimization insights by large language models](01_kinetics_fire/Pd52dc296ee/README.md) | Q1 | 待核对 |
| 2024 | [Prediction of unburned carbon and NOx emissions of solid fuel using petrographic UBC index and artificial neural network](01_kinetics_fire/P7b32ac4bc0/README.md) | Q1 | 待核对 |
| 2024 | [Battery safety: Machine learning-based prognostics](01_kinetics_fire/P1490d15be1/README.md) | Q1 | 待核对 |
| 2024 | [Revealing the initial pyrolysis behavior of decalin in an experimental study coupled with neural network-assisted molecular dynamics](01_kinetics_fire/P0d5d5ada55/README.md) | Q1 | 待核对 |
| 2023 | [Physicochemical properties and pyrolysis behavior of petcoke with artificial neural network modeling](01_kinetics_fire/Pa1b4718234/README.md) | Q1 | 待核对 |
| 2023 | [Machine learning-based metaheuristic optimization of an integrated biomass gasification cycle for fuel and cooling production](01_kinetics_fire/P38e5f043a9/README.md) | Q1 | 待核对 |
| 2023 | [Pyrolysis of de-fatted microalgae residue: A study on thermal-kinetics, products’ optimization, and neural network modelling](01_kinetics_fire/Pbc9a85b074/README.md) | Q1 | 待核对 |
| 2023 | [Predicting tobacco pyrolysis based on chemical constituents and heating conditions using machine learning approaches](01_kinetics_fire/Pb50acc5bc4/README.md) | Q1 | 待核对 |
| 2023 | [Accurate determination of homogeneous ignition of single solid fuel particles enabled by machine learning](01_kinetics_fire/P65e70f4529/README.md) | Q1 | 待核对 |
| 2023 | [Comparison of artificial neural network and response surface methodology for evaluation of the predictive capability of bio-oil yield from pyrolysis of Mangifera indica wood sawdust](01_kinetics_fire/P25ffe5954c/README.md) | Q1 | 待核对 |
| 2023 | [Application of machine learning methods for lignocellulose biomass pyrolysis: Activation energy prediction from preliminary analysis and conversion degree](01_kinetics_fire/P625b3e11f6/README.md) | Q1 | 待核对 |
| 2023 | [Co-pyrolysis of oil-based drill cuttings and pinewood sawdust: Thermal behavior, synergistic effect, artificial neural network and empirical reaction model](01_kinetics_fire/Pca1ee36e15/README.md) | Q1 | 待核对 |
| 2023 | [Co-pyrolysis of Azadirachta indica non-edible seed and waste LDPE: Analysis of kinetic models using thermogravimetric analyser and prediction modeling with Artificial Neural Network (ANN)](01_kinetics_fire/P9022f29d87/README.md) | Q1 | 待核对 |
| 2023 | [Machine learning-driven prediction and optimization of monoaromatic oil production from catalytic co-pyrolysis of biomass and plastic wastes](01_kinetics_fire/Pf9158c4d0f/README.md) | Q1 | 待核对 |
| 2023 | [Bayesian optimized multilayer perceptron neural network modelling of biochar and syngas production from pyrolysis of biomass-derived wastes](01_kinetics_fire/Pb410212a79/README.md) | Q1 | 待核对 |
| 2022 | [Autonomous kinetic modeling of biomass pyrolysis using chemical reaction neural networks](01_kinetics_fire/P4cbef1b3c9/README.md) | Q1 | ✓ |
| 2022 | [Combustion and pyrolysis kinetics of Australian lignite coal and validation by artificial neural networks](01_kinetics_fire/Pd5839f0885/README.md) | Q? | 待核对 |
| 2022 | [Predicting co-pyrolysis of coal and biomass using machine learning approaches](01_kinetics_fire/Pddd1f8b7de/README.md) | Q1 | 待核对 |
| 2022 | [Machine learning prediction of bio-oil characteristics quantitatively relating to biomass compositions and pyrolysis conditions](01_kinetics_fire/P689b7ffc78/README.md) | Q1 | 待核对 |
| 2022 | [Machine learning prediction and analysis of commercial wood fuel blends used in a typical biomass power station](01_kinetics_fire/P6e13b9af16/README.md) | Q1 | 待核对 |
| 2022 | [Effects of waste-based pyrolysis as heating source: Meta-analyze of char yield and machine learning analysis](01_kinetics_fire/Pa32c7de2aa/README.md) | Q1 | 待核对 |
| 2022 | [Prediction and evaluation of fuel properties of hydrochar from waste solid biomass: Machine learning algorithm based on proposed PSO–NN model](01_kinetics_fire/P3024483383/README.md) | Q1 | 待核对 |
| 2022 | [Research on the co-pyrolysis of coal slime and cellulose based on TG-FTIR-MS, artificial neural network, and principal component analysis](01_kinetics_fire/P0d850ed4d9/README.md) | Q1 | 待核对 |
| 2022 | [A comparison of machine learning algorithms for estimation of higher heating values of biomass and fossil fuels from ultimate analysis](01_kinetics_fire/P10dac3da4e/README.md) | Q1 | 待核对 |
| 2022 | [Co-pyrolytic interactions, kinetics and products of biomass pyrolysis coke and rapeseed cake: Machine learning, DAEM and 2D-COS analysis](01_kinetics_fire/P9911f0f585/README.md) | Q1 | 待核对 |
| 2022 | [Prediction of coal self-ignition tendency using machine learning](01_kinetics_fire/P2e3db232ed/README.md) | Q1 | 待核对 |
| 2022 | [Machine learning to predict biochar and bio-oil yields from co-pyrolysis of biomass and plastics](01_kinetics_fire/P857fc25539/README.md) | Q1 | 待核对 |
| 2022 | [Active learning-based exploration of the catalytic pyrolysis of plastic waste](01_kinetics_fire/P92264f9a97/README.md) | Q1 | ✓ |
| 2022 | [Co–pyrolysis of de–alkalized lignin and coconut shell via TG/DTG–FTIR and machine learning methods: pyrolysis characteristics, gas products, and thermo–kinetics](01_kinetics_fire/Pd8586b4c1b/README.md) | Q1 | 待核对 |
| 2021 | [Thermodynamics, kinetics, gas emissions and artificial neural network modeling of co-pyrolysis of sewage sludge and peanut shell](01_kinetics_fire/P5a1322fc5e/README.md) | Q1 | 待核对 |
| 2021 | [Investigation of the co-pyrolysis of coal slime and coffee industry residue based on machine learning methods and TG-FTIR: Synergistic effect, kinetics and thermodynamic](01_kinetics_fire/Pbbe2924e9f/README.md) | Q1 | 待核对 |
| 2020 | [Classification of solid fuels with machine learning](01_kinetics_fire/P53dcbe4b04/README.md) | Q1 | ✓ |
| 2020 | [Pyrolysis of biological wastes for bioenergy production: Thermo-kinetic studies with machine-learning method and Py-GC/MS analysis](01_kinetics_fire/P5c34bdff3c/README.md) | Q1 | 待核对 |
| 2020 | [Machine learning for predictive coal combustion CFD simulations—From detailed kinetics to HDMR Reduced-Order models](01_kinetics_fire/Pdd14baf067/README.md) | Q1 | 待核对 |
| 2019 | [A comparison of random forest and support vector machine approaches to predict coal spontaneous combustion in gob](01_kinetics_fire/Pf1021f79aa/README.md) | Q1 | 待核对 |
| 2019 | [Predicting kinetic parameters for coal devolatilization by means of Artificial Neural Networks](01_kinetics_fire/P0b8e2b7d28/README.md) | Q1 | 待核对 |
| 2018 | [Prediction of product distributions in coal devolatilization by an artificial neural network model](01_kinetics_fire/P9dbc7c7b55/README.md) | Q1 | 待核对 |
| 2018 | [ThermalNet: A deep reinforcement learning-based combustion optimization system for coal-fired boiler](01_kinetics_fire/P8e6b5f251a/README.md) | Q1 | 待核对 |

### [金属燃料与固体推进剂](02_metals_propellants/README.md)（6）

| 年份 | 论文 | 分区线索 | 代码 |
|---|---|---|---|
| 2026 | [Machine learning-assisted analysis of ignition and combustion properties in as-milled and annealed Al-Zr composite powders](02_metals_propellants/P524a75ba90/README.md) | Q1 | 待核对 |
| 2026 | [Improving HTPB regression rate models using machine learning](02_metals_propellants/P431322d6d1/README.md) | Q1 | 待核对 |
| 2026 | [Neural Network-Based Accelerated Model for Condensed Combustion Products in Solid Propellant](02_metals_propellants/P8c717b1660/README.md) | Q1 | 待核对 |
| 2025 | [Numerical sensitivity analysis of HTPB counterflow combustion using neural networks](02_metals_propellants/P340d841dc1/README.md) | Q1 | 待核对 |
| 2025 | [Combustion phases of magnesium alloys based on predicted heating rate using machine learning](02_metals_propellants/Pa77d3fc58a/README.md) | Q? | 待核对 |
| 2023 | [Dynamic model and deep neural network-based surrogate model to predict dynamic behaviors and steady-state performance of solid propellant combustion](02_metals_propellants/Pb50b1efdd3/README.md) | Q1 | 待核对 |
