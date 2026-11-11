# 化学动力学代理、缩减与机理发现

把每个网格里昂贵的化学计算变快，同时尽量保留点火、放热和污染物的正确性。

本目录含 99 条候选。分区与全文状态逐篇标注；自动分类以研究目标优先，交叉方法可在总库检索。

[返回首页](../README.md) · [全局地图](../00_literature_map/README.md) · [方法与范围](../docs/METHODOLOGY.md)

## 核心问题

学习的是反应速率、一步时间推进、低维流形还是未知反应网络？四种输出对应不同误差和稳定性要求。

## 方法演进与比较

传统 MLP/RF 代理 → 多尺度采样与分区网络 → 守恒约束时间推进器 → CRNN/Neural ODE 可解释机理 → KAN 与反应网络神经算子。另一条分子尺度路线用神经网络势和主动学习连接量子化学参考与反应分子动力学；它学习能量/力，不等同于直接拟合宏观反应源项。不要把名称新颖直接当作精度更高的证据。

## 数据与物理定义

零维定容/定压轨迹、一维预混/对冲火焰、DNS 热化学状态、实验点火与火焰速度。每条记录必须保留机理版本、组分顺序、压力单位、时间步与反应器约束。分子势分支使用原子构型、总能量和原子力，需要量子化学方法、基组、自旋/电荷、元素类型与单位。

## 怎样判断模型有效

log10 点火延迟 MAE、火焰速度误差、温度/重要和痕量组分误差、元素及总质量守恒、非负性、长时滚动稳定性；加速比包含采样、转换、传输和回退开销。分子势另报每原子能量与原子力误差、MD 能量漂移、反应路径及产物统计，不能直接与宏观源项代理横向排名。

## 如何避免数据泄漏

按完整轨迹、初始温压当量比或反应家族留出。同一轨迹的相邻时刻高度相关，随机按行分割会严重高估泛化。分子势应留出反应路径与构型分布，并检查主动学习选择标准是否使用测试信息。

## 主要局限与选题问题

状态空间覆盖不足、刚性、微量组分跨数量级、守恒与非负性不自动兼得、单步准确但长时间漂移。零维成功还需要一维及 CFD 耦合验证。

## 建议阅读和实践路径

先运行 B01 点火代理理解数据链路，再读多尺度采样与 SL-GPS，随后比较守恒代理、CMLM 和 CRNN。

## 细分类与论文索引

分区栏为二级来源线索；Q? 为待核实。代码 ✓ 仅表示论文链接已核对，不表示执行成功。

### [代理与缩减](01_surrogates_reduction/README.md)（80）

| 年份 | 论文 | 分区线索 | 代码 |
|---|---|---|---|
| 2026 | [Development of A Lightweight Neural Network for Predicting Reaction Rates in RANS Simulations of Flame-Wall Interactions](01_surrogates_reduction/P797d45d886/README.md) | Q? | 待核对 |
| 2026 | [Formation-consumption neural networks for efficient chemical kinetics modeling](01_surrogates_reduction/P321781fe9a/README.md) | Q1 | 待核对 |
| 2026 | [Direct uncertainty quantification of high-dimensional combustion kinetic models through deep reinforcement learning](01_surrogates_reduction/Pe95368f134/README.md) | Q1 | 待核对 |
| 2026 | [Machine learning-aided high-throughput screening of oxygen carriers for chemical looping combustion with balanced reactivity and stability](01_surrogates_reduction/Pbf6ce7a555/README.md) | Q1 | 待核对 |
| 2026 | [A machine learning method to predict rate constants in ammonium dinitramide combustion kinetic model](01_surrogates_reduction/P390d25fa95/README.md) | Q1 | 待核对 |
| 2026 | [Autonomous adaptive solver selection for chemistry integration via reinforcement learning](01_surrogates_reduction/P28d9416995/README.md) | Q1 | 待核对 |
| 2026 | [DFODE-Kit: Deep learning package for solving flame chemical kinetics with high-dimensional stiff ordinary differential equations](01_surrogates_reduction/P485814185d/README.md) | Q? | ✓ |
| 2026 | [Fast predictions of plasma-assisted NH3/air combustion based on model downscaling and machine learning coupled with kinetics mechanism](01_surrogates_reduction/Pa7d7788e74/README.md) | Q1 | 待核对 |
| 2026 | [Enhancing deep learning of ammonia/natural gas combustion kinetics via physics-aware data augmentation and scale separation](01_surrogates_reduction/P208595837d/README.md) | Q1 | ✓ |
| 2026 | [A Machine learning based analysis for ignition strategies and mechanisms of High-Efficiency renewable methanol combustion: Diesel-Piloted and turbulent jet ignition engines](01_surrogates_reduction/P9f6050c1e1/README.md) | Q1 | 待核对 |
| 2026 | [Reinforcement learning based control of packed bed reactors for chemical looping combustion](01_surrogates_reduction/Pceaba239a5/README.md) | Q1 | 待核对 |
| 2026 | [Self evolving neural network methodology for chemical kinetics reduction](01_surrogates_reduction/Pfcbb195899/README.md) | Q1 | 待核对 |
| 2026 | [A semi-supervised learning technique for the region-wise simplification of chemical kinetics: Application to Hydrogen–Ammonia flames](01_surrogates_reduction/P80f8e8a6ec/README.md) | Q1 | 待核对 |
| 2026 | [Adaptive learning of data assimilated combustion reaction model](01_surrogates_reduction/P1923271e69/README.md) | Q1 | 待核对 |
| 2026 | [Exploring long range dynamics using neural network potentials: From recrossing coefficients to roaming](01_surrogates_reduction/Pe1ed973c10/README.md) | Q1 | 待核对 |
| 2026 | [Entropy-constrained machine learning with residual data augmentation for modeling chemical kinetics](01_surrogates_reduction/Pdb52d836dd/README.md) | Q1 | 待核对 |
| 2026 | [Data-driven model for reduced combustion chemistry via Bayesian Optimization](01_surrogates_reduction/Pcc9e30dbae/README.md) | Q1 | 待核对 |
| 2026 | [Uncovering flame physics with machine learning: Application to the reaction rate in hydrogen flames](01_surrogates_reduction/Pe05015d6f5/README.md) | Q1 | 待核对 |
| 2026 | [A physics-constrained machine learning approach for complex-fuel reaction kinetics modeling](01_surrogates_reduction/P0877a129c0/README.md) | Q1 | 待核对 |
| 2026 | [A deep neural network as surrogate model for chemistry integration of a detailed soot mechanism](01_surrogates_reduction/Pe3a428757b/README.md) | Q1 | 待核对 |
| 2025 | [Optimization of ammonia/methane mixture combustion kinetic model based on Artificial Neural Network](01_surrogates_reduction/P3b53c7a9b7/README.md) | Q1 | 待核对 |
| 2025 | [Efficient machine learning method for supercritical combustion: Predicting real-fluid properties and chemical ODEs](01_surrogates_reduction/P85ba45f243/README.md) | Q1 | 待核对 |
| 2025 | [Extended Fourier Neural Operators to learn stiff chemical kinetics under unseen conditions](01_surrogates_reduction/Pa9a5eeffba/README.md) | Q1 | 待核对 |
| 2025 | [Machine learned compact kinetic model for liquid fuel combustion](01_surrogates_reduction/P7ff18f54f4/README.md) | Q1 | 待核对 |
| 2025 | [Enforcing physical conservation in neural network surrogate models for complex chemical kinetics](01_surrogates_reduction/P221bc006b9/README.md) | Q1 | ✓ |
| 2025 | [An improved machine learning method for thermochemistry tabulation, with application to LES-PDF simulations of piloted diffusion and swirl-bluff-body stabilised flames with NOx formation](01_surrogates_reduction/P8dbe436315/README.md) | Q1 | 待核对 |
| 2025 | [Machine learning tabulation of thermochemistry for the PAH mechanism and applications to laminar and turbulent sooting flames](01_surrogates_reduction/Padb758adc8/README.md) | Q1 | 待核对 |
| 2025 | [Deep learning based combustion chemistry acceleration method for widely applicable NH 3 / H 2 turbulent combustion simulations](01_surrogates_reduction/P08013518eb/README.md) | Q1 | 待核对 |
| 2025 | [A data-driven sparse learning approach to reduce chemical reaction mechanisms](01_surrogates_reduction/P172de76b36/README.md) | Q1 | 待核对 |
| 2025 | [Machine learning-driven prediction of NH2-n-alkane reactions for constructing high-precision ammonia-macromolecule hydrocarbon combustion models](01_surrogates_reduction/P8081d51403/README.md) | Q1 | 待核对 |
| 2025 | [Solving multiscale dynamical systems by deep learning](01_surrogates_reduction/Pba328f5b75/README.md) | Q? | ✓ |
| 2025 | [Machine learning-enhanced combustion modeling for predicting laminar burning velocity of ammonia-hydrogen mixtures using improved reaction mechanisms](01_surrogates_reduction/P7d5713cedb/README.md) | Q? | 待核对 |
| 2025 | [A machine learning assisted upscaling method for the Arrhenius kinetic model, with application to the in-situ conversion process](01_surrogates_reduction/P84968467ad/README.md) | Q1 | 待核对 |
| 2025 | [Kinetic study of the combustion process in internal combustion engines: A new methodological approach employing an artificial neural network](01_surrogates_reduction/Pfd9f1a9db0/README.md) | Q1 | 待核对 |
| 2025 | [Theoretical kinetics and back-propagation neural network model for H-abstraction by NO2 in C3-C5 esters combustion](01_surrogates_reduction/P534cb4401b/README.md) | Q1 | 待核对 |
| 2025 | [Data-driven optimization of turbulent kinetic energy and tumble-y in combustion engines: A comparative study of machine learning models](01_surrogates_reduction/Pba4fd3e63c/README.md) | Q1 | 待核对 |
| 2025 | [Artificial neural network chemistry solving for high-pressure hydrogen–air combustion](01_surrogates_reduction/Pc5709d73ae/README.md) | Q1 | 待核对 |
| 2025 | [Recombination of NH2 with alkyl radicals: VRC-TST rate constants from neural network potentials](01_surrogates_reduction/P3cc2153f99/README.md) | Q1 | 待核对 |
| 2025 | [Meta-learning innovates chemical kinetics: An efficient approach for surrogate model construction](01_surrogates_reduction/Pb7052d2c66/README.md) | Q1 | 待核对 |
| 2025 | [Physics-informed neural networks for reacting flows: Species reconstruction with finite rate chemistry from sparse and noisy velocity measurements](01_surrogates_reduction/Pf7aa2ff833/README.md) | Q1 | 待核对 |
| 2025 | [Comprehensive deep learning for combustion chemistry integration: Multi-fuel generalization and a posteriori validation in reacting flow](01_surrogates_reduction/Pdd9a1fb317/README.md) | Q? | ✓ |
| 2024 | [Neural network potential-based molecular investigation of pollutant formation of ammonia and ammonia-hydrogen combustion](01_surrogates_reduction/Pbda1f68659/README.md) | Q1 | 待核对 |
| 2024 | [A novel machine learning based lumping approach for the reduction of large kinetic mechanisms for plasma-assisted combustion applications](01_surrogates_reduction/Pe2ef6cec2e/README.md) | Q1 | 待核对 |
| 2024 | [A machine learning method to predict rate constants for various reactions in combustion kinetic models](01_surrogates_reduction/P2696c5ed02/README.md) | Q1 | ✓ |
| 2024 | [CRK-PINN: A physics-informed neural network for solving combustion reaction kinetics ordinary differential equations](01_surrogates_reduction/P76e6e98211/README.md) | Q1 | 待核对 |
| 2024 | [Machine learning tabulation of thermochemistry for turbulent dimethyl ether (DME) flames](01_surrogates_reduction/P1750eb86fe/README.md) | Q1 | 待核对 |
| 2024 | [A Hessian-based transfer learning approach for artificial neural networks based chemical kinetics with a sparse dataset](01_surrogates_reduction/P1c31a7c1bc/README.md) | Q1 | 待核对 |
| 2024 | [Physics-informed neural networks coupled with flamelet/progress variable model for solving combustion physics considering detailed reaction mechanism](01_surrogates_reduction/P07c89aa3a3/README.md) | Q? | 待核对 |
| 2023 | [Neural network approach to response surface development for reaction model optimization and uncertainty minimization](01_surrogates_reduction/P2cedc559c3/README.md) | Q1 | 待核对 |
| 2023 | [Kinetics parameter optimization of hydrocarbon fuels via neural ordinary differential equations](01_surrogates_reduction/P182de72e21/README.md) | Q1 | 待核对 |
| 2023 | [Machine learned compact kinetic models for methane combustion](01_surrogates_reduction/P0e0adcb60c/README.md) | Q1 | 待核对 |
| 2023 | [Machine learning rate constants of hydrogen abstraction reactions between ester and H atom](01_surrogates_reduction/P34e9feffe7/README.md) | Q1 | 待核对 |
| 2023 | [Multi-target active subspaces generated using a neural network for computationally efficient turbulent combustion kinetic uncertainty quantification in the flamelet regime](01_surrogates_reduction/P6bc37c4021/README.md) | Q1 | 待核对 |
| 2023 | [Simulation of turbulent premixed flames with machine learning - tabulated thermochemistry](01_surrogates_reduction/P24d8134e6f/README.md) | Q1 | 待核对 |
| 2023 | [Multi-fidelity neural network for uncertainty quantification of chemical reaction models](01_surrogates_reduction/P9d4bda4b10/README.md) | Q1 | 待核对 |
| 2023 | [DeepFlame: A deep learning empowered open-source platform for reacting flow simulations](01_surrogates_reduction/P9b9c10a9d8/README.md) | Q? | ✓ |
| 2023 | [Numerical simulation of nitric oxide (NO) emission for HCNG fueled SI engine by Zeldovich’, prompt (HCN) and nitrous oxide (N2O) mechanisms along with the error reduction novel sub-models and their classification through machine learning algorithms](01_surrogates_reduction/P1f29247c44/README.md) | Q1 | 待核对 |
| 2023 | [Large-Eddy Simulation of flameless combustion with neural-network driven chemistry](01_surrogates_reduction/P2f39d7d9ef/README.md) | Q? | 待核对 |
| 2023 | [SGS Reaction rate modelling for MILD combustion based on machine-learning combustion mode classification: Development and a priori study](01_surrogates_reduction/Pc764b9805b/README.md) | Q1 | 待核对 |
| 2023 | [Kinetic subspace investigation using neural network for uncertainty quantification in nonpremixed flamelets](01_surrogates_reduction/P51d30d09e0/README.md) | Q1 | 待核对 |
| 2023 | [Deep learning dynamical latencies for the analysis and reduction of combustion chemistry kinetics](01_surrogates_reduction/P0afc85ab6a/README.md) | Q? | ✓ |
| 2022 | [Species reaction rate modelling based on physics-guided machine learning](01_surrogates_reduction/P200e0cdc46/README.md) | Q1 | 待核对 |
| 2022 | [An improved approach towards more robust deep learning models for chemical kinetics](01_surrogates_reduction/Pb3cc3a43d0/README.md) | Q1 | 待核对 |
| 2022 | [A multi-scale sampling method for accurate and robust deep neural network to predict combustion chemical kinetics](01_surrogates_reduction/P88f8a69095/README.md) | Q1 | ✓ |
| 2022 | [Integrated machine learning-quantitative structure property relationship (ML-QSPR) and chemical kinetics for high throughput fuel screening toward internal combustion engine](01_surrogates_reduction/Pc1cd187f21/README.md) | Q1 | 待核对 |
| 2022 | [Study of NOx emission for hydrogen enriched compressed natural along with exhaust gas recirculation in spark ignition engine by Zeldovich’ mechanism, support vector machine and regression correlation](01_surrogates_reduction/P2c2a51cbc5/README.md) | Q1 | 待核对 |
| 2022 | [Estimating flashpoints of fuels and chemical compounds using hybrid machine-learning techniques](01_surrogates_reduction/Pfca5e9bc41/README.md) | Q1 | 待核对 |
| 2022 | [Towards predicting liquid fuel physicochemical properties using molecular dynamics guided machine learning models](01_surrogates_reduction/P881c53af7a/README.md) | Q1 | 待核对 |
| 2021 | [On-the-fly artificial neural network for chemical kinetics in direct numerical simulations of premixed combustion](01_surrogates_reduction/P41be2ef313/README.md) | Q1 | 待核对 |
| 2021 | [Machine learning tabulation of thermochemistry in turbulent combustion: An approach based on hybrid flamelet/random data and multiple multilayer perceptrons](01_surrogates_reduction/P73837c97dc/README.md) | Q1 | 待核对 |
| 2021 | [Machine learning-quantitative structure property relationship (ML-QSPR) method for fuel physicochemical properties prediction of multiple fuel types](01_surrogates_reduction/P8f8c343976/README.md) | Q1 | 待核对 |
| 2021 | [Machine learning for detailed chemistry reduction in DNS of a syngas turbulent oxy-flame with side-wall effects](01_surrogates_reduction/Pc1d610eadb/README.md) | Q1 | 待核对 |
| 2020 | [Adaptive chemistry via pre-partitioning of composition space and mechanism reduction](01_surrogates_reduction/P8c8c05b2bc/README.md) | Q1 | ✓ |
| 2020 | [Facilitating Bayesian analysis of combustion kinetic models with artificial neural network](01_surrogates_reduction/P053b0d3181/README.md) | Q1 | 待核对 |
| 2020 | [A machine learning methodology for improving the accuracy of laminar flame simulations with reduced chemical kinetics mechanisms](01_surrogates_reduction/Pcb8889dfbd/README.md) | Q1 | 待核对 |
| 2020 | [Chemistry reduction using machine learning trained from non-premixed micro-mixing modeling: Application to DNS of a syngas turbulent oxy-flame with side-wall effects](01_surrogates_reduction/Pe1482ded9f/README.md) | Q1 | ✓ |
| 2020 | [Data-driven selection of stiff chemistry ODE solver in operator-splitting schemes](01_surrogates_reduction/Pb5572b591e/README.md) | Q1 | 待核对 |
| 2020 | [Artificial neural network based chemical mechanisms for computationally efficient modeling of hydrogen/carbon monoxide/kerosene combustion](01_surrogates_reduction/Pdf5048757a/README.md) | Q1 | 待核对 |
| 2019 | [Training convolutional neural networks to estimate turbulent sub-grid scale reaction rates](01_surrogates_reduction/P0cc52e57f1/README.md) | Q1 | 待核对 |
| 2018 | [Investigation on Kinetic Parameters of Combustion and Oxy-Combustion of Calcined Pet Coke Employing Thermogravimetric Analysis Coupled to Artificial Neural Network Modeling](01_surrogates_reduction/Paddc96176d/README.md) | Q1 | 待核对 |

### [机理发现与参数校准](02_discovery_calibration/README.md)（17）

| 年份 | 论文 | 分区线索 | 代码 |
|---|---|---|---|
| 2026 | [Experimental study of NH3/H2/n-heptane combustion and reduced mechanism optimization via a CNN-augmented neural network and the L-SHADE algorithm](02_discovery_calibration/Peed6ec9a06/README.md) | Q1 | 待核对 |
| 2026 | [Decoding the complex reaction network of nitromethane combustion via neural network potential molecular dynamics simulation](02_discovery_calibration/Pa9958b88eb/README.md) | Q1 | 待核对 |
| 2026 | [Machine learning assisted particle swarm optimization of NH3/H2 combustion mechanism for laminar flame speeds](02_discovery_calibration/P4b22fd271e/README.md) | Q1 | 待核对 |
| 2026 | [Kolmogorov–Arnold Chemical Reaction Neural Networks for learning pressure-dependent kinetic rate laws](02_discovery_calibration/P336cbbe5b6/README.md) | Q1 | 待核对 |
| 2026 | [A Reaction-network-informed Neural Operator for generalizable combustion chemistry integration](02_discovery_calibration/P001dd197d5/README.md) | Q1 | 待核对 |
| 2025 | [EM-HyChem: Bridging molecular simulations and chemical reaction neural network-enabled approach to modelling energetic material chemistry](02_discovery_calibration/P2f1fa993a2/README.md) | Q1 | 待核对 |
| 2025 | [Thermal decomposition kinetics of plastic mixtures (PE/PVC and PE/PP) based on chemical reaction neural networks](02_discovery_calibration/P1537a87267/README.md) | Q1 | 待核对 |
| 2025 | [Two-stage optimization for chemical kinetic mechanisms with improved deep reinforcement learning](02_discovery_calibration/P7914f61dc1/README.md) | Q1 | 待核对 |
| 2024 | [Parameter estimation of distributed activation energy models via chemical reaction neural network](02_discovery_calibration/P88f10f3641/README.md) | Q1 | 待核对 |
| 2024 | [Combining genetic algorithm and deep learning to optimize a chemical kinetic mechanism of ammonia under high pressure](02_discovery_calibration/Pac323b3216/README.md) | Q1 | 待核对 |
| 2024 | [Uncertain lithium-ion cathode kinetic decomposition modeling via Bayesian chemical reaction neural networks](02_discovery_calibration/P2384b1472e/README.md) | Q1 | ✓ |
| 2024 | [Robust mechanism discovery with atom conserving chemical reaction neural networks](02_discovery_calibration/Pde62c31740/README.md) | Q1 | 待核对 |
| 2024 | [Artificial neural network-based Hamiltonian Monte Carlo for high-dimensional Bayesian Inference of reaction kinetics models](02_discovery_calibration/P4e3d2e99e2/README.md) | Q1 | 待核对 |
| 2022 | [Adaptive global pathway selection using artificial neural networks: A-priori study](02_discovery_calibration/P4a2b5d4efc/README.md) | Q1 | ✓ |
| 2021 | [A new skeletal mechanism for simulating MILD combustion optimized using Artificial Neural Network](02_discovery_calibration/Pef5148c3a8/README.md) | Q? | 待核对 |
| 2021 | [A New Global Mechanism for MILD Combustion Using Artificial-Neural-Network-Based Optimization](02_discovery_calibration/P687ac34d46/README.md) | Q1 | 待核对 |
| 2020 | [Optimization of the Global Reaction Mechanism for MILD Combustion of Methane Using Artificial Neural Network](02_discovery_calibration/Pe8385041a9/README.md) | Q1 | 待核对 |

### [神经网络势、反应分子动力学与主动学习](03_molecular_potentials/README.md)（2）

| 年份 | 论文 | 分区线索 | 代码 |
|---|---|---|---|
| 2020 | [Exploring the Chemical Space of Linear Alkane Pyrolysis via Deep Potential GENerator](03_molecular_potentials/Pebb206703b/README.md) | Q1 | ✓ |
| 2020 | [Complex reaction processes in combustion unraveled by neural network-based molecular dynamics simulation](03_molecular_potentials/P4a48f472f5/README.md) | Q? | ✓ |
