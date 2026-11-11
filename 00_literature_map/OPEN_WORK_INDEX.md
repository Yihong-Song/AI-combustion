# 逐篇开源工作与可用性索引

更新：2026-11-12。论文–仓库关联、源码归档、许可、数据与执行为不同状态。表中有些是相关工作、教程或组件，有些未找到许可证，不能把表的总行数称为可复现论文数。

[研究路线](RESEARCH_ROADMAP.md) · [全部论文](ALL_PAPERS.md) · [全部包](../code_packages/README.md)

## 统计口径

| 对应关系 | DOI 去重篇数 |
|---|---:|
| `author_implementation_readme_explicit` | 37 |
| `author_related_work_readme_explicit` | 4 |
| `author_supporting_component_readme_explicit` | 2 |
| `author_supporting_tool_readme_explicit` | 1 |
| `author_supporting_tutorial_readme_explicit` | 2 |
| `repository_reference_readme_explicit` | 1 |
| `title_match_repository_readme` | 4 |

已建立关联 51 篇；其中 31 篇的关联包已附完整或部分源码，其余 20 篇保留固定链接。完整包与部分包的数量仍以代码总索引为准。

## 化学动力学代理、缩减与机理发现

| 年份 / DOI | 论文 | 分区线索 | 代码与关系 | 收纳 |
|---|---|---|---|---|
| 2026 / [10.1016/j.cpc.2025.110013](https://doi.org/10.1016/j.cpc.2025.110013) | [DFODE-Kit: Deep learning package for solving flame chemical kinetics with high-dimensional stiff ordinary differential equations](../01_chemistry_kinetics/01_surrogates_reduction/P485814185d/README.md) | ?；官方年度待核 | [deepflame-ai/DFODE-kit](../code_packages/deepflame-ai__DFODE-kit/README.md)<br>author_implementation_readme_explicit | partial_source_snapshot_collected |
| 2026 / [10.1016/j.fuel.2026.138904](https://doi.org/10.1016/j.fuel.2026.138904) | [Enhancing deep learning of ammonia/natural gas combustion kinetics via physics-aware data augmentation and scale separation](../01_chemistry_kinetics/01_surrogates_reduction/P208595837d/README.md) | Q1；官方年度待核 | [deepflame-ai/DFODE-kit](../code_packages/deepflame-ai__DFODE-kit/README.md)<br>author_related_work_readme_explicit | partial_source_snapshot_collected |
| 2025 / [10.1016/j.combustflame.2025.114105](https://doi.org/10.1016/j.combustflame.2025.114105) | [Enforcing physical conservation in neural network surrogate models for complex chemical kinetics](../01_chemistry_kinetics/01_surrogates_reduction/P221bc006b9/README.md) | Q1；官方年度待核 | [tianhanz/DNN-Models-for-Chemical-Kinetics](../code_packages/tianhanz__DNN-Models-for-Chemical-Kinetics/README.md)<br>author_implementation_readme_explicit | partial_source_snapshot_collected |
| 2025 / [10.1016/j.cpc.2025.109802](https://doi.org/10.1016/j.cpc.2025.109802) | [Solving multiscale dynamical systems by deep learning](../01_chemistry_kinetics/01_surrogates_reduction/Pba328f5b75/README.md) | ?；官方年度待核 | [Seauagain/DeePODE](../code_packages/Seauagain__DeePODE/README.md)<br>author_implementation_readme_explicit | partial_source_snapshot_collected |
| 2025 / [10.1063/5.0248582](https://doi.org/10.1063/5.0248582) | [Comprehensive deep learning for combustion chemistry integration: Multi-fuel generalization and a posteriori validation in reacting flow](../01_chemistry_kinetics/01_surrogates_reduction/Pdd9a1fb317/README.md) | ?；官方年度待核 | [deepflame-ai/DFODE-kit](../code_packages/deepflame-ai__DFODE-kit/README.md)<br>author_related_work_readme_explicit | partial_source_snapshot_collected |
| 2024 / [10.1016/j.combustflame.2024.113375](https://doi.org/10.1016/j.combustflame.2024.113375) | [A machine learning method to predict rate constants for various reactions in combustion kinetic models](../01_chemistry_kinetics/01_surrogates_reduction/P2696c5ed02/README.md) | Q1；官方年度待核 | [edwardning/ML_RateConstants](../code_packages/edwardning__ML_RateConstants/README.md)<br>title_match_repository_readme | link_only |
| 2024 / [10.1016/j.proci.2024.105243](https://doi.org/10.1016/j.proci.2024.105243) | [Uncertain lithium-ion cathode kinetic decomposition modeling via Bayesian chemical reaction neural networks](../01_chemistry_kinetics/02_discovery_calibration/P2384b1472e/README.md) | Q1；官方年度待核 | [DENG-MIT/CRNN](../code_packages/DENG-MIT__CRNN/README.md)<br>author_implementation_readme_explicit | partial_source_snapshot_collected |
| 2023 / [10.1016/j.cpc.2023.108842](https://doi.org/10.1016/j.cpc.2023.108842) | [DeepFlame: A deep learning empowered open-source platform for reacting flow simulations](../01_chemistry_kinetics/01_surrogates_reduction/P9b9c10a9d8/README.md) | ?；官方年度待核 | [deepflameCFD/deepflame-dev](../code_packages/deepflameCFD__deepflame-dev/README.md)<br>author_related_work_readme_explicit | source_archive_collected |
| 2023 / [10.1063/5.0167110](https://doi.org/10.1063/5.0167110) | [Deep learning dynamical latencies for the analysis and reduction of combustion chemistry kinetics](../01_chemistry_kinetics/01_surrogates_reduction/P0afc85ab6a/README.md) | ?；官方年度待核 | [lmcastellanos/Deep-learning-dynamical-latencies-for-the-analysis-and-reduction-of-combustion-chemistry-kinetics](../code_packages/lmcastellanos__Deep-learning-dynamical-latencies-for-the-analysis-and-reduction-of-combustion-chemistry-kinetics/README.md)<br>title_match_repository_readme | link_only |
| 2022 / [10.1016/j.combustflame.2022.112279](https://doi.org/10.1016/j.combustflame.2022.112279) | [Adaptive global pathway selection using artificial neural networks: A-priori study](../01_chemistry_kinetics/02_discovery_calibration/P4a2b5d4efc/README.md) | Q1；官方年度待核 | [ctftamu/SL-GPS](../code_packages/ctftamu__SL-GPS/README.md)<br>author_implementation_readme_explicit | partial_source_snapshot_collected |
| 2022 / [10.1016/j.combustflame.2022.112319](https://doi.org/10.1016/j.combustflame.2022.112319) | [A multi-scale sampling method for accurate and robust deep neural network to predict combustion chemical kinetics](../01_chemistry_kinetics/01_surrogates_reduction/P88f8a69095/README.md) | Q1；官方年度待核 | [tianhanz/DNN-Models-for-Chemical-Kinetics](../code_packages/tianhanz__DNN-Models-for-Chemical-Kinetics/README.md)<br>author_implementation_readme_explicit | partial_source_snapshot_collected |
| 2020 / [10.1016/j.combustflame.2019.09.010](https://doi.org/10.1016/j.combustflame.2019.09.010) | [Adaptive chemistry via pre-partitioning of composition space and mechanism reduction](../01_chemistry_kinetics/01_surrogates_reduction/P8c8c05b2bc/README.md) | Q1；官方年度待核 | [gdalessi/adaptiveChemistry](../code_packages/gdalessi__adaptiveChemistry/README.md)<br>author_implementation_readme_explicit | link_only |
| 2020 / [10.1016/j.combustflame.2020.06.008](https://doi.org/10.1016/j.combustflame.2020.06.008) | [Chemistry reduction using machine learning trained from non-premixed micro-mixing modeling: Application to DNS of a syngas turbulent oxy-flame with side-wall effects](../01_chemistry_kinetics/01_surrogates_reduction/Pe1482ded9f/README.md) | Q1；官方年度待核 | [beroudiauxa/ORCh_2023](../code_packages/beroudiauxa__ORCh_2023/README.md)<br>author_related_work_readme_explicit | partial_source_snapshot_collected |
| 2020 / [10.1021/acs.energyfuels.0c03211](https://doi.org/10.1021/acs.energyfuels.0c03211) | [Exploring the Chemical Space of Linear Alkane Pyrolysis via Deep Potential GENerator](../01_chemistry_kinetics/03_molecular_potentials/Pebb206703b/README.md) | Q1；官方年度待核 | [tongzhugroup/mddatasetbuilder](../code_packages/tongzhugroup__mddatasetbuilder/README.md)<br>author_supporting_component_readme_explicit | source_archive_collected |
| 2020 / [10.1038/s41467-020-19497-z](https://doi.org/10.1038/s41467-020-19497-z) | [Complex reaction processes in combustion unraveled by neural network-based molecular dynamics simulation](../01_chemistry_kinetics/03_molecular_potentials/P4a48f472f5/README.md) | ?；官方年度待核 | [tongzhugroup/mddatasetbuilder](../code_packages/tongzhugroup__mddatasetbuilder/README.md)<br>author_supporting_component_readme_explicit | source_archive_collected |

### DFODE-Kit: Deep learning package for solving flame chemical kinetics with high-dimensional stiff ordinary differential equations

**研究问题：** 用神经网络替代详细燃烧化学的刚性 ODE 积分，同时保留与 CFD 的接口。

**实际入口：** dfode_kit/cli/main.py；config → init → run-case → sample → augment → label → train；先阅读 docs 中 data-workflow 与各命令说明。

**依赖与数据：** Python、Cantera、HDF5、模型训练依赖；运行 CFD 案例还需 OpenFOAM、DeepFlame 及本机路径配置。归档不代表外部求解器、机理或全量训练数据齐备。

**当前边界：** GPL-3.0。当前提交经过重构，需与论文发表时版本对照；本轮收录，不执行训练。

### Enhancing deep learning of ammonia/natural gas combustion kinetics via physics-aware data augmentation and scale separation

**研究问题：** 改善氨/天然气燃烧化学学习中状态覆盖与不同时间尺度的处理。

**实际入口：** 从 augment、label、train 三个命令及数据变换配置入手；逐项比对原文的状态扰动、筛选准则与尺度分离方式。

**依赖与数据：** 同 DFODE-kit 的基础依赖；另需原文所用氨/天然气机理、混合物定义、训练状态与后验反应流算例。

**当前边界：** 关联类型为 related work，不能计为全文实验已打包；与 DFODE 软件论文共享一个包。

### Enforcing physical conservation in neural network surrogate models for complex chemical kinetics

**研究问题：** 在复杂化学动力学神经代理中强制物理守恒，降低迭代时状态漂移。

**实际入口：** modelclass.py 与 ZeroDAutognition.py 是定位模型和零维验证的起点；逐个追踪守恒层和推理变换。

**依赖与数据：** Python/Fortran 双实现；机理、组分顺序和时间步必须一致。

**当前边界：** 尚未执行论文实验；守恒不自动保证化学准确、正性或未知机理可迁移。

### Solving multiscale dynamical systems by deep learning

**研究问题：** 用多尺度状态采样和神经时间推进器处理刚性动力学，包含燃烧应用。

**实际入口：** pred.py dryrun、onestep_plot、evolution、export；训练入口 train.py。

**依赖与数据：** 上游示例环境含 Cantera 2.6、PyTorch、mpi4py/OpenMPI；Windows 与旧环境需额外适配。

**当前边界：** README 中速度提升为作者声明，本库未验证，不录为本库实测；作为跨领域方法单独标注其燃烧应用边界。

### Comprehensive deep learning for combustion chemistry integration: Multi-fuel generalization and a posteriori validation in reacting flow

**研究问题：** 评估燃烧化学神经积分器跨燃料泛化及耦合反应流后的实际表现。

**实际入口：** 沿 canonical_cases、数据生成/增广/标注及 training 配置查找各燃料设置，再核对 DeepFlame 的模型部署接口。

**依赖与数据：** Python/Cantera/DeepFlame/OpenFOAM 及每个燃料的机理；不能把换用新机理所得实验写作原文复现。

**当前边界：** 只确认相关软件关系，尚未核验完整原文实验；多个燃料不能重复计为多篇论文。

### A machine learning method to predict rate constants for various reactions in combustion kinetic models

**研究问题：** 利用反应表示学习预测燃烧反应速率常数。

**实际入口：** rxnfp_schwaller/generate_rxnfp.py 和 fine_tune.py。

**依赖与数据：** README 使用 Python 3.7；反应指纹相关依赖需隔离，避免直接混入当前基线环境。

**当前边界：** 未发现许可，链接收纳。预测速率常数还需经过机理级点火/火焰速度验证。

### Uncertain lithium-ion cathode kinetic decomposition modeling via Bayesian chemical reaction neural networks

**研究问题：** 用 Bayesian CRNN 表征锂电正极分解动力学的不确定性，属于燃烧安全交叉方向。

**实际入口：** 选择 cathode UQ 对应子目录的 Julia 项目与数据，避免误跑通用 Case 1–5。

**依赖与数据：** 不同子项目 Julia 环境不同；上游 cathode 新环境与原 CRNN 环境不可混用。

**当前边界：** 同一 CRNN 仓库关联多篇论文，按论文计数与按包计数需分开；未执行采样。

### DeepFlame: A deep learning empowered open-source platform for reacting flow simulations

**研究问题：** 构建深度学习与传统反应流求解耦合的开源平台。

**实际入口：** 先检查上游安装文档、bashrc、求解器和 tutorials，再选择一个与论文版本一致的典型反应流案例。

**依赖与数据：** 兼容的 OpenFOAM、Cantera、LibTorch、编译器和 MPI；旧提交的环境不能直接用本机 OpenFOAM 13 替代。

**当前边界：** 部分网络权重上游说明需向作者申请；固定主分支不是自动等同论文发布版本。未执行本论文算例。

### Deep learning dynamical latencies for the analysis and reduction of combustion chemistry kinetics

**研究问题：** 学习低维动力学潜变量，用于燃烧化学的分析和缩减。

**实际入口：** 先读取数据及预处理说明，再依次核对训练、流形表征、PCA 比较和外推算例。

**依赖与数据：** 外部 Zenodo 数据需另取并保留版本；运行环境需从各目录核实。

**当前边界：** 未找到明确源码许可。Physics of Fluids 的 JCR 证据在本轮未核实，因此列入分区待核实。

### Adaptive global pathway selection using artificial neural networks: A-priori study

**研究问题：** 以 ANN 近似全局路径选择结果，实现随热化学状态变化的动态机理缩减。

**实际入口：** tests/ 与 src/slgps/mech_train.py；converth5ToPb.ipynb 面向 OpenFOAM 集成。运行前检查当前目录与相对机理路径。

**依赖与数据：** Cantera 3、TensorFlow 2、networkx、pandas、scikit-learn、NumPy。旧 h5 模型与当前 Keras 之间可能需要版本适配。

**当前边界：** 论文标题明确为 a priori。不能仅凭分类或离线测试声称任意 CFD 中已验证；继承 GPS 的第三方许可亦需保留。

### A multi-scale sampling method for accurate and robust deep neural network to predict combustion chemical kinetics

**研究问题：** 通过多尺度采样提升详细化学神经网络代理对热化学状态空间的覆盖。

**实际入口：** ZeroDAutognition.py、modelclass.py、FortranDNN_Module.F、Chem/、Model/。

**依赖与数据：** 需逐脚本检查 Python/Fortran、Cantera、网络框架和模型文件；大数据不自动下载。

**当前边界：** 与 2025 年守恒论文共用一个仓库，包数只计一次。当前提交同时包含多篇工作的演化内容，不能自动视为 2022 原始版本。

### Adaptive chemistry via pre-partitioning of composition space and mechanism reduction

**研究问题：** 将热化学组成空间分区并配置局部缩减机理，降低 CFD 化学计算量。

**实际入口：** SPARC 对 laminarSMOKE/edcSMOKE 的扩展；先建立传统化学基准，再查看组成空间分类和局部机理选择接口。

**依赖与数据：** OpenFOAM、laminarSMOKE/edcSMOKE、所需缩减机理及分类器；OpenMORe 是相关降阶工具，版本应单独固定。

**当前边界：** 未定位许可证，只保留固定链接。预分区误差与局部机理误差需要分开归因。

### Chemistry reduction using machine learning trained from non-premixed micro-mixing modeling: Application to DNS of a syngas turbulent oxy-flame with side-wall effects

**研究问题：** 从非预混微混合模型生成训练状态，缩减合成气湍流氧燃烧化学。

**实际入口：** 按 ORCh 环境与案例说明定位采样、缩减和 ANN/CNN 模块；先核对同一合成气机理与微混合设置。

**依赖与数据：** 旧 Cantera 2.4、SUNDIALS、Eigen、OpenCV、MPI、HDF5 及编译工具，路径集中配置，历史环境需隔离。

**当前边界：** BSD-3-Clause；相关工作引用不代表原文训练数据和全部 DNS 案例已收纳。

### Exploring the Chemical Space of Linear Alkane Pyrolysis via Deep Potential GENerator

**研究问题：** 以自动化数据构建与并发学习推进燃烧神经网络势训练。

**实际入口：** dpgen init_reaction reaction.json machine.json；机器配置连接 LAMMPS、datasetbuilder 与 Gaussian，后续训练按 DP-GEN 文档执行。

**依赖与数据：** 需要单独固定 DP-GEN、DeePMD-kit、LAMMPS 与量子化学软件版本；本包归档不包含全部外部工具、轨迹或计算资源。

**当前边界：** 与 2020 Nature Communications 工作共用一个支撑包，只计一个包；该映射来自 README 后续工作说明，尚未复现本文图表。

### Complex reaction processes in combustion unraveled by neural network-based molecular dynamics simulation

**研究问题：** 为燃烧反应分子动力学的神经网络势构建量子化学参考数据。

**实际入口：** datasetbuilder → qmcalc → preparedeepmd → dp train train.json；具体参数见固定版本 README。

**依赖与数据：** LAMMPS/ReaxFF 轨迹、Gaussian 16 量子化学计算、DeePMD-kit 及相应运行环境；Gaussian 使用权限与计算资源需单独解决。

**当前边界：** 本库未计算量子化学数据或训练势函数；README 的运行时描述不是实测。代码许可、Gaussian 与原始轨迹的数据许可分别记录。

## 湍流燃烧闭合与流形模型

| 年份 / DOI | 论文 | 分区线索 | 代码与关系 | 收纳 |
|---|---|---|---|---|
| 2026 / [10.1080/13647830.2026.2621012](https://doi.org/10.1080/13647830.2026.2621012) | [Data-based filtered dissipation rate modelling for multi-modal turbulent combustion: evaluating a priori model generalizability](../literature/adjacent/P2bf9290361/README.md) | Q3；官方年度待核 | [cristianlacey/data-based-multi-modal-filtered-dissipation-rates](../code_packages/cristianlacey__data-based-multi-modal-filtered-dissipation-rates/README.md)<br>author_implementation_readme_explicit | link_only |
| 2025 / [10.1007/s10494-024-00626-3](https://doi.org/10.1007/s10494-024-00626-3) | [A Data-Driven Approach to Refine the Partially Stirred Reactor Closure for Turbulent Premixed Flames](../02_turbulence_closure/01_closures_manifolds/P8badc7f206/README.md) | ?；官方年度待核 | [LorenzoPiu/aPrioriDNS](../code_packages/LorenzoPiu__aPrioriDNS/README.md)<br>author_supporting_tool_readme_explicit | partial_source_snapshot_collected |
| 2025 / [10.1016/j.engappai.2024.109821](https://doi.org/10.1016/j.engappai.2024.109821) | [a priori uncertainty quantification of reacting turbulence closure models using Bayesian neural networks](../02_turbulence_closure/01_closures_manifolds/P71c16d5cb2/README.md) | Q1；官方年度待核 | [NatLabRockies/mluq-prop](../code_packages/NatLabRockies__mluq-prop/README.md)<br>title_match_repository_readme | partial_source_snapshot_collected |
| 2024 / [10.1016/j.combustflame.2023.113139](https://doi.org/10.1016/j.combustflame.2023.113139) | [Data-based instantaneous conditional progress variable dissipation rate modeling for turbulent premixed combustion](../02_turbulence_closure/01_closures_manifolds/P2fc75bd437/README.md) | Q1；官方年度待核 | [cristianlacey/data-based-dissipation-rates](../code_packages/cristianlacey__data-based-dissipation-rates/README.md)<br>author_implementation_readme_explicit | source_archive_collected |
| 2021 / [10.1016/j.proci.2020.06.263](https://doi.org/10.1016/j.proci.2020.06.263) | [An a priori evaluation of a principal component and artificial neural network based combustion model in diesel engine conditions](../02_turbulence_closure/01_closures_manifolds/P15efd785db/README.md) | Q1；官方年度待核 | [deepakdalakoti/PCA-ANN](../code_packages/deepakdalakoti__PCA-ANN/README.md)<br>repository_reference_readme_explicit | link_only |

### Data-based filtered dissipation rate modelling for multi-modal turbulent combustion: evaluating a priori model generalizability

**研究问题：** 在多模态湍流燃烧流形模型中闭合混合分数、交叉及进度变量的滤波耗散率。

**实际入口：** 按 tf-gpu.yml 与 README 输入定义读取模型，分别核对 chi_ZZ、chi_ZLambda 和 chi_LambdaLambda 的符号、尺度和过滤定义。

**依赖与数据：** TensorFlow 2.4.1 的独立环境、适配的 DNS/流形数据和预处理；未确认训练数据全量可用。

**当前边界：** 当前二级分区线索为 Q3，保留在相邻附录，不计入 Q1/Q2。未定位许可文件，仅固定链接。

### A Data-Driven Approach to Refine the Partially Stirred Reactor Closure for Turbulent Premixed Flames

**研究问题：** 基于 DNS 数据改进预混湍流火焰的 PaSR 闭合，并为数据处理提供可追溯工具。

**实际入口：** 从 Field3D 的数据读取、滤波和 compute_reaction_rates 示例开始，核对普通/Favre 滤波与 LFR 源项定义。

**依赖与数据：** README 给出 NumPy、SciPy、Matplotlib、Cantera、PyCSP、findiff 等；旧发行名 aPrioriDNS、新名 apriori，需固定提交与对应文档。

**当前边界：** GPL-3.0；未执行论文实验。aPriori/aPrioriDNS 为更名相关入口，按已收纳的固定仓库卡计一次，避免重复计包。

### a priori uncertainty quantification of reacting turbulence closure models using Bayesian neural networks

**研究问题：** 用贝叶斯神经网络估计预混湍流闭合预测及认知/随机不确定度。

**实际入口：** 从项目安装和模型/训练配置开始，核对变分推断、网络参数分布与预测采样；Python 3.10 环境为上游建议。

**依赖与数据：** 项目 Python 依赖与 HPC/MPI 配置需依固定提交核查；预混 DNS 数据及预处理不因源码可见而视为齐备。

**当前边界：** BSD-3-Clause-Clear；先验不确定度表现不能直接证明后验 LES 安全或模型已校准。

### Data-based instantaneous conditional progress variable dissipation rate modeling for turbulent premixed combustion

**研究问题：** 在预混湍流流形模型中预测瞬时条件进度变量耗散率剖面。

**实际入口：** 先从 tf-gpu.yml 建立旧环境；依 README 的输入列名对齐特征，核对归一化参考点 Lambda_ref=0.5 与模型输出变换。

**依赖与数据：** Python、TensorFlow 2.4.1 和固定 Anaconda 环境；训练 DNS 数据、模型文件与特征生成需分别清点。

**当前边界：** Clear BSD 许可，包含不授予专利权的条款，保留原文；未执行模型。

### An a priori evaluation of a principal component and artificial neural network based combustion model in diesel engine conditions

**研究问题：** 在柴油机条件下，对 PCA 与人工神经网络结合的燃烧模型进行先验评价。

**实际入口：** 根目录 PCA-ANN.ipynb、helper_functions.py 与 neural_networks.py。

**依赖与数据：** README 未给出完整环境；应从 notebook 导入、数据读取和辅助脚本逐项提取依赖，未执行。

**当前边界：** 未定位许可，仅链接。这里的实现关系为 README 明确引用，强度不同于作者声明提供全文复现实验。

## 神经算子、降阶与流场重建

| 年份 / DOI | 论文 | 分区线索 | 代码与关系 | 收纳 |
|---|---|---|---|---|
| 2024 / [10.1016/j.cma.2023.116674](https://doi.org/10.1016/j.cma.2023.116674) | [Learning stiff chemical kinetics using extended deep neural operators](../03_operators_reconstruction/01_operators_rom/P98c59b685b/README.md) | Q1；官方年度待核 | [somdattagoswami/Approximating-StiffKinetics](../code_packages/somdattagoswami__Approximating-StiffKinetics/README.md)<br>author_implementation_readme_explicit | link_only |

### Learning stiff chemical kinetics using extended deep neural operators

**研究问题：** 用扩展深度神经算子近似多时间尺度的刚性化学动力学。

**实际入口：** 先检查 AE-DeepONet 示例与各方法子目录，按原文例题建立初值、时间采样、编码器及算子输入的映射。

**依赖与数据：** 各子目录的框架与依赖需独立提取；Cantera 数据重生成必须固定机理、初始工况与采样。

**当前边界：** 完整数据不可得；未定位许可，只提供固定链接。不能把有限示例运行当作全文结果。

## 热声不稳定性预测、辨识与控制

| 年份 / DOI | 论文 | 分区线索 | 代码与关系 | 收纳 |
|---|---|---|---|---|
| 2026 / [10.1016/j.proci.2026.106547](https://doi.org/10.1016/j.proci.2026.106547) | [Deep learning for continuous lead-time prediction of thermoacoustic instabilities in an annular combustor](../04_instability_control/01_prediction_identification/P51fe566a45/README.md) | Q1；官方年度待核 | [Predictive-Intelligent-Systems-Lab/TTE-TAI-PROCI-paper](../code_packages/Predictive-Intelligent-Systems-Lab__TTE-TAI-PROCI-paper/README.md)<br>author_implementation_readme_explicit | source_archive_collected |
| 2024 / [10.1016/j.cma.2023.116502](https://doi.org/10.1016/j.cma.2023.116502) | [Inferring unknown unknowns: Regularized bias-aware ensemble Kalman filter](../04_instability_control/01_prediction_identification/P0783e678e5/README.md) | Q1；官方年度待核 | [MagriLab/rBA-EnKF](../code_packages/MagriLab__rBA-EnKF/README.md)<br>author_implementation_readme_explicit | source_archive_collected |
| 2024 / [10.1017/jfm.2024.1052](https://doi.org/10.1017/jfm.2024.1052) | [A real-time digital twin of azimuthal thermoacoustic instabilities](../04_instability_control/01_prediction_identification/P0e5f9b5e09/README.md) | ?；官方年度待核 | [andreanovoa/real-time-bias-aware-DA](../code_packages/andreanovoa__real-time-bias-aware-DA/README.md)<br>author_implementation_readme_explicit | partial_source_snapshot_collected |
| 2024 / [10.1103/physrevfluids.9.103902](https://doi.org/10.1103/physrevfluids.9.103902) | [Data-driven computation of adjoint sensitivities without adjoint solvers: An application to thermoacoustics](../04_instability_control/02_control/P9903dd056c/README.md) | ?；官方年度待核 | [MagriLab/Adjoint-ESN](../code_packages/MagriLab__Adjoint-ESN/README.md)<br>author_implementation_readme_explicit | link_only |
| 2023 / [10.1103/physrevfluids.8.103201](https://doi.org/10.1103/physrevfluids.8.103201) | [Hard-constrained neural networks for modeling nonlinear acoustics](../04_instability_control/01_prediction_identification/Pa68d424897/README.md) | ?；官方年度待核 | [MagriLab/HCTA](../code_packages/MagriLab__HCTA/README.md)<br>author_implementation_readme_explicit | partial_source_snapshot_collected |
| 2022 / [10.1017/jfm.2022.653](https://doi.org/10.1017/jfm.2022.653) | [Real-time thermoacoustic data assimilation](../04_instability_control/01_prediction_identification/P97829e9574/README.md) | ?；官方年度待核 | [MagriLab/Real-time-TA-DA](../code_packages/MagriLab__Real-time-TA-DA/README.md)<br>author_implementation_readme_explicit | partial_source_snapshot_collected |
| 2021 / [10.1016/j.jsv.2021.116083](https://doi.org/10.1016/j.jsv.2021.116083) | [Robust identification of flame frequency response via multi-fidelity Gaussian process approach](../04_instability_control/01_prediction_identification/P67741bfd8c/README.md) | Q1；官方年度待核 | [ShuaiGuo16/Multi-Fidelity-ML](../code_packages/ShuaiGuo16__Multi-Fidelity-ML/README.md)<br>author_implementation_readme_explicit | link_only |

### Deep learning for continuous lead-time prediction of thermoacoustic instabilities in an annular combustor

**研究问题：** 从环形燃烧室压力信号连续预测距离热声失稳还有多久。

**实际入口：** synthetic_gen.py 生成轨迹；label_exp_onset.py 标注实验起振；trans_train.py、lstm_train.py、XGBoost_train.py 对照；common.py 与 preprocess_mod.py 核对标签和窗口。

**依赖与数据：** Python≥3.10、PyTorch、SciPy、pandas、scikit-learn、XGBoost；实验数据入口 Zenodo 23091955 已定位，未下载验证。

**当前边界：** MIT；合成轨迹多种子不是多篇复现。原论文正式训练与实验零样本结果尚未执行。

### Inferring unknown unknowns: Regularized bias-aware ensemble Kalman filter

**研究问题：** 在热声等动力系统同化中，同时处理状态不确定性与未知模型偏差。

**实际入口：** 先读仓库 Erratum.pdf 与实现，再定位热声配置；新维护版入口为 andreanovoa/real-time-bias-aware-DA。

**依赖与数据：** 固定旧版依赖与对应实验设置；新版 API、模块布局和默认参数已变化，不能混用。

**当前边界：** MIT。README 明说原文式(15)–(16)有排版错误，仓库及勘误为更正依据；必须在复现报告中说明。

### A real-time digital twin of azimuthal thermoacoustic instabilities

**研究问题：** 为环形燃烧室方位热声不稳定性构建随观测更新的数字孪生。

**实际入口：** 先定位 v1.0，再核对 examples/thermoacoustics 及相应配置；当前 tutorials 的热声章节用于理解软件。

**依赖与数据：** Python 项目环境及 romda 所列 biasda/dynamodels 等依赖；实验信号和结果目录可能从外部取得，需逐项核实。

**当前边界：** MIT；主分支固定提交与论文 v1.0 不同，正式复现须补 v1.0 的准确提交。未执行。

### Data-driven computation of adjoint sensitivities without adjoint solvers: An application to thermoacoustics

**研究问题：** 在缺少完整伴随求解器时，用数据模型估计热声系统目标量的参数敏感度。

**实际入口：** tutorial_rijke.ipynb 从数据生成、训练、验证到敏感度计算；src 中独立脚本与配置支撑批量实验。

**依赖与数据：** 依赖与配置从固定提交提取；保留 Rijke 管参数、时间离散和扰动幅值，Lorenz 教程用于理解代码。

**当前边界：** 未定位明确根许可证，链接收纳；相同仓库还对应会议论文，会议不计作 JCR 期刊。

### Hard-constrained neural networks for modeling nonlinear acoustics

**研究问题：** 从有限压力测点重建非线性声场与热声速度场，并外推振荡。

**实际入口：** python -m hcta.rijke_galerkin.generate 生成合成数据；python -m hcta.experiment --config_path src/configs/config.yml 运行；figures 中脚本对应论文图。

**依赖与数据：** 按项目依赖安装独立 Python 环境；作者另提供 Zenodo 10021355 数据与 figure_data 配置/权重。数据链接已定位，本轮未下载。

**当前边界：** MIT。README 明说图 13/14 的模型数据未打包，需要重做 robustness_sensor.py 与 robustness_noise.py 扫描。

### Real-time thermoacoustic data assimilation

**研究问题：** 用实时数据同化修正热声模型状态，并结合储备池学习处理模型偏差。

**实际入口：** main.m 按论文图号选择目标图；先检查 Part I 的状态估计，再阅读 Part II 的高保真同化。

**依赖与数据：** MATLAB 及代码需要的工具箱；不要将迁移后的 Python romda 默认参数视作本篇原始 MATLAB 配置。

**当前边界：** MIT；本轮归档不运行。维护后的软件另见 andreanovoa/real-time-bias-aware-DA，旧版与新版按版本区分。

### Robust identification of flame frequency response via multi-fidelity Gaussian process approach

**研究问题：** 融合低成本宽带识别与高保真谐波识别，提高火焰频率响应估计的鲁棒性。

**实际入口：** MatlabScripts 中 BroadbandForcing、HarmonicForcing、Ref_FIR、SNR1_gain 与 SNR1_phase，按论文章节定位制图代码。

**依赖与数据：** MATLAB 与高斯过程相关依赖、输入/热释放信号；README 谐波频率采用离散网格是实现选择，需与原文核对。

**当前边界：** 未定位许可证，仅链接；火焰传递函数误差还需传播至稳定性分析。

## 光学诊断、反演、烟炱与辐射

| 年份 / DOI | 论文 | 分区线索 | 代码与关系 | 收纳 |
|---|---|---|---|---|
| 2026 / [10.1016/j.combustflame.2026.115082](https://doi.org/10.1016/j.combustflame.2026.115082) | [Neural refractive index primitives for flame field reconstruction using background-oriented schlieren](../05_diagnostics_radiation/01_optical_inverse/Pc2b8d1f214/README.md) | Q1；官方年度待核 | [Weihu22/Neural-Implicit-Reconstruction-for-BOS](../code_packages/Weihu22__Neural-Implicit-Reconstruction-for-BOS/README.md)<br>author_implementation_readme_explicit | link_only |
| 2026 / [10.1016/j.proci.2026.106166](https://doi.org/10.1016/j.proci.2026.106166) | [Integrated neural network approach for autonomous sensitivity analysis and optimization of sectional soot kinetic modeling](../05_diagnostics_radiation/03_soot_formation/Pe31f2bea9d/README.md) | Q1；官方年度待核 | [cfx18/NN4Soot](../code_packages/cfx18__NN4Soot/README.md)<br>title_match_repository_readme | link_only |
| 2026 / [10.1016/j.proci.2026.106476](https://doi.org/10.1016/j.proci.2026.106476) | [Physics-informed neural network WSGG model for radiative heat transfer in H2O–CO2–NH3 gas mixtures relevant to ammonia combustion](../05_diagnostics_radiation/02_radiation_soot/P69b4098fb3/README.md) | Q1；官方年度待核 | [TaoRen-Rad/WSGG-H2O-CO2-NH3](../code_packages/TaoRen-Rad__WSGG-H2O-CO2-NH3/README.md)<br>author_implementation_readme_explicit | source_archive_collected |
| 2025 / [10.1016/j.proci.2025.105821](https://doi.org/10.1016/j.proci.2025.105821) | [SAGE: A machine learning model for primary particle segmentation in TEM images of soot aggregates](../05_diagnostics_radiation/01_optical_inverse/P56771c427a/README.md) | Q1；官方年度待核 | [comp-comb/SAGE](../code_packages/comp-comb__SAGE/README.md)<br>author_implementation_readme_explicit | partial_source_snapshot_collected |
| 2023 / [10.1016/j.combustflame.2022.112583](https://doi.org/10.1016/j.combustflame.2022.112583) | [Deep learning-based denoising for fast time-resolved flame emission spectroscopy in high-pressure combustion environment](../05_diagnostics_radiation/01_optical_inverse/P2949b85479/README.md) | Q1；官方年度待核 | [ytg7146/DU_CNN](../code_packages/ytg7146__DU_CNN/README.md)<br>author_implementation_readme_explicit | link_only |
| 2022 / [10.1016/j.fuel.2022.125508](https://doi.org/10.1016/j.fuel.2022.125508) | [Data-driven discovery of heat release rate markers for premixed NH3/H2/air flames using physics-informed machine learning](../05_diagnostics_radiation/01_optical_inverse/Pd9de613208/README.md) | Q1；官方年度待核 | [SrijithSreekumar/Heat_Realease_Rate_intergrated_with_physics_constrained_neural_network](../code_packages/SrijithSreekumar__Heat_Realease_Rate_intergrated_with_physics_constrained_neural_network/README.md)<br>author_implementation_readme_explicit | link_only |
| 2021 / [10.1016/j.jqsrt.2021.107628](https://doi.org/10.1016/j.jqsrt.2021.107628) | [A machine learning based full-spectrum correlated k-distribution model for nonhomogeneous gas-soot mixtures](../05_diagnostics_radiation/02_radiation_soot/Pe01c5a5aac/README.md) | ?；官方年度待核 | [ZY-LHY/Machine_learning_based_FSCK_model_soot](../code_packages/ZY-LHY__Machine_learning_based_FSCK_model_soot/README.md)<br>author_implementation_readme_explicit | partial_source_snapshot_collected |

### Neural refractive index primitives for flame field reconstruction using background-oriented schlieren

**研究问题：** 利用神经隐式表示从背景纹影观测重建三维折射率及火焰场。

**实际入口：** step1_InitBOSLAB.m → step2_Compile.m → step3_generate_phantom1_synthetic_data.m → PYTHON/NIR-BOS/main_BOS.py。

**依赖与数据：** MATLAB、NVIDIA GPU/CUDA、environment.yml；当前上游明确不支持纯 CPU。

**当前边界：** PolyForm Noncommercial 属可见源代码且限制商业使用，不能标为 OSI 开源。作者警告 CGLS 参考实现正反投影不匹配；该警告不等同于 NIR-BOS 本身有同一问题。本库仅提供链接。

### Integrated neural network approach for autonomous sensitivity analysis and optimization of sectional soot kinetic modeling

**研究问题：** 对分段烟炱动力学模型进行快速敏感度分析和参数优化。

**实际入口：** scripts/01_train_from_config.py 到 05_run_optimization.py；reproduce_all.py 和跳过预训练入口；先检查 configs 与数据列定义。

**依赖与数据：** requirements.txt、PyTorch 模型及数据/预训练目录；文件是否包含实际全部数据和权重尚待清点。

**当前边界：** README 声称 MIT，但固定提交未定位许可文件，因此只保留链接。出版版与 under-review 代码的对应待核。

### Physics-informed neural network WSGG model for radiative heat transfer in H2O–CO2–NH3 gas mixtures relevant to ammonia combustion

**研究问题：** 为含 NH3 的 H2O–CO2 参与性气体建立 PINN-WSGG 辐射模型。

**实际入口：** python test.py；输入 data/profiles.npy、data/results.npy 和 PINN_WSGG/data/wsgg.json，输出 test_case.png。

**依赖与数据：** 先核对 requirements.txt；主要为 NumPy/SciPy/Matplotlib，实际以固定提交为准。README 的 your-username 克隆命令为占位符，应使用本库记录的真实仓库地址。

**当前边界：** 明确 MIT 许可；本库已执行固定版本作者演示，实测与适配见 C01。仅验证预训练推理演示，尚未重训，也未复现原文目标表格；作者更广泛的验证结论仍不能当作本库实测。

### SAGE: A machine learning model for primary particle segmentation in TEM images of soot aggregates

**研究问题：** 从烟炱 TEM 图像自动分割初级颗粒，减少人工形貌测量负担。

**实际入口：** SAGE_train.ipynb 训练/微调；SAGE_ANALYZE.ipynb 推理、模型比较及颗粒几何量提取；权重从 Releases 或 notebook 下载。

**依赖与数据：** requirements.yml 的独立环境、Mask R-CNN 依赖、对应分割数据和权重。上游使用 Tesla K80，现代 TensorFlow/CUDA 版本需另核。

**当前边界：** GPL-3.0；源码许可不自动覆盖权重与图像。原 README 的兼容性建议不是本库实际验证。

### Deep learning-based denoising for fast time-resolved flame emission spectroscopy in high-pressure combustion environment

**研究问题：** 对高压燃烧环境中的快速时间分辨火焰发射光谱进行深度学习去噪。

**实际入口：** 按 environment.yaml 单独创建环境，取得 rawdataM.mat 后调整 config.yaml，再审查 main.py。

**依赖与数据：** README 使用 Windows Python 3.10.4；数据位于外部 Google Drive，未下载核验。

**当前边界：** 未找到明确许可，保留版本链接和说明，不镜像源代码。外部数据可访问性与许可另行核实。

### Data-driven discovery of heat release rate markers for premixed NH3/H2/air flames using physics-informed machine learning

**研究问题：** 寻找 NH3/H2/air 预混火焰中可用于推断热释放率的组分标记。

**实际入口：** 根目录含 Data_preprocessing、PIML_mass_fraction、PIML_molar_fraction、Gradient_output_to_input、Sensitivity_analysis、Evaluation 及重构误差分析目录。

**依赖与数据：** 分别核对质量/摩尔分数输入、数据预处理和模型框架版本；README 未提供完整的一键运行环境。

**当前边界：** 未定位许可，仅固定链接；未执行。基于机理生成数据的相关性不能直接证明实验测量的标记鲁棒性。

### A machine learning based full-spectrum correlated k-distribution model for nonhomogeneous gas-soot mixtures

**研究问题：** 用紧凑模型预测燃烧气体与烟炱混合物的全谱相关 k 分布。

**实际入口：** Main.f90 → make → ./rhs → python plot.py；先核对温度、压力、组分和烟炱体积分数的单位及范围。

**依赖与数据：** GNU Fortran、make 与 Python 绘图依赖；训练表格和原始光谱数据库不因推理模块公开而自动齐备。

**当前边界：** MIT；README 也列 2020 前作作为背景，不将当前气体–烟炱模块当作前作完整实现。未运行。

## 物理信息学习与可微燃烧求解

| 年份 / DOI | 论文 | 分区线索 | 代码与关系 | 收纳 |
|---|---|---|---|---|
| 2025 / [10.1016/j.combustflame.2025.113964](https://doi.org/10.1016/j.combustflame.2025.113964) | [FlamePINN-1D: Physics-informed neural networks to solve forward and inverse problems of 1D laminar flames](../06_physics_informed/01_forward_inverse/P1cf521f2c6/README.md) | Q1；官方年度待核 | [CAME-THU/FlamePINN-1D](../code_packages/CAME-THU__FlamePINN-1D/README.md)<br>author_implementation_readme_explicit | partial_source_snapshot_collected |
| 2023 / [10.1016/j.proci.2022.09.059](https://doi.org/10.1016/j.proci.2022.09.059) | [Physics-informed graph neural networks for predicting cetane number with systematic data quality analysis](../06_physics_informed/01_forward_inverse/Pad01f0053d/README.md) | Q1；官方年度待核 | [BioE-KimLab/CNpred](../code_packages/BioE-KimLab__CNpred/README.md)<br>author_implementation_readme_explicit | link_only |
| 2022 / [10.1063/5.0086649](https://doi.org/10.1063/5.0086649) | [Physics-informed neural networks and functional interpolation for stiff chemical kinetics](../06_physics_informed/01_forward_inverse/P42f2fcf650/README.md) | ?；官方年度待核 | [mariodeflorio/Stiff-Chemical-Kinetics](../code_packages/mariodeflorio__Stiff-Chemical-Kinetics/README.md)<br>author_implementation_readme_explicit | link_only |

### FlamePINN-1D: Physics-informed neural networks to solve forward and inverse problems of 1D laminar flames

**研究问题：** 用物理信息神经网络求解一维层流火焰正问题和逆问题。阅读时应区分简化化学与详细化学，以及自由传播与对冲火焰的边界条件。

**实际入口：** 先从 Case 1 开始，核对 1S_CH4_MP.yaml；再推进至 Case 2 和 Case 3。使用固定提交中的实际目录名。

**依赖与数据：** 需 Cantera 和上游各算例的神经网络依赖；README 未提供统一完整环境锁。机理应通过本地数据路径加载，避免覆盖系统安装中的 Cantera 数据。

**当前边界：** 已核实论文—仓库关系、提交和 MIT 许可，尚未执行原始训练。不能把下游 Bratu 示例当作本论文复现。

### Physics-informed graph neural networks for predicting cetane number with systematic data quality analysis

**研究问题：** 用物理信息图神经网络预测十六烷值，并分析标签质量的影响。

**实际入口：** 先核对仓库中数据与训练入口，按上游要求安装 tensorflow==2.5.0、nfp==0.3.0 和 RDKit。

**依赖与数据：** 旧 TensorFlow/nfp 组合需独立旧 Python 环境；不建议在 Python 3.13 基线环境直接安装。

**当前边界：** 未定位到源码许可，仅链接收纳。线上预测服务是否仍可用未验证。

### Physics-informed neural networks and functional interpolation for stiff chemical kinetics

**研究问题：** 在刚性化学初值问题中比较物理约束神经解法与传统积分器。

**实际入口：** 按固定仓库各例题脚本核对初值、时间区间、分段策略和特征数；先与同精度传统 ODE 参考解对照。

**依赖与数据：** 从各脚本导入和作者环境提取依赖；例题性质与详细燃烧化学的外推范围需全文确认。

**当前边界：** 未定位许可，仅链接；标为方法基础，不能以通用 ROBER 等小系统充当详细燃烧论文复现。

## 发动机、燃烧器与复杂推进系统设计

| 年份 / DOI | 论文 | 分区线索 | 代码与关系 | 收纳 |
|---|---|---|---|---|
| 2025 / [10.1016/j.combustflame.2025.114026](https://doi.org/10.1016/j.combustflame.2025.114026) | [A machine learning based approach for statistical analysis of detonation cells from soot foils](../07_engineering_design/03_supersonic_detonation/Peb8f5d8782/README.md) | Q1；官方年度待核 | [vanshs1/ML_DetonationCells_SootFoil](../code_packages/vanshs1__ML_DetonationCells_SootFoil/README.md)<br>author_implementation_readme_explicit | partial_source_snapshot_collected |
| 2022 / [10.1016/j.combustflame.2022.112286](https://doi.org/10.1016/j.combustflame.2022.112286) | [Co-optimized machine-learned manifold models for large eddy simulation of turbulent combustion](../07_engineering_design/02_control_optimization/Pe07d955e64/README.md) | Q1；官方年度待核 | [NatLabRockies/cmlm](../code_packages/NatLabRockies__cmlm/README.md)<br>author_implementation_readme_explicit | partial_source_snapshot_collected |
| 2021 / [10.1038/s41467-021-21331-z](https://doi.org/10.1038/s41467-021-21331-z) | [Learning dominant physical processes with data-driven balance models](../07_engineering_design/03_supersonic_detonation/P3fe49a4002/README.md) | ?；官方年度待核 | [dynamicslab/dominant-balance](../code_packages/dynamicslab__dominant-balance/README.md)<br>author_implementation_readme_explicit | partial_source_snapshot_collected |
| 2021 / [10.1177/14680874211019345](https://doi.org/10.1177/14680874211019345) | [Deep reinforcement learning for dynamic control of fuel injection timing in multi-pulse compression ignition engines](../literature/adjacent/Pd9e3925a87/README.md) | Q3；官方年度待核 | [NatLabRockies/MPRL](../code_packages/NatLabRockies__MPRL/README.md)<br>author_implementation_readme_explicit | source_archive_collected |

### A machine learning based approach for statistical analysis of detonation cells from soot foils

**研究问题：** 从烟膜图像自动分割爆轰胞格并统计尺寸与面积，减少人工量取。

**实际入口：** package.list、config.py、main_sootFoilSeg.py；example/ 含 case 10a。

**依赖与数据：** 上游建议 Python 3.9+；CellPose 预训练权重和图像数据的许可也应单独记录。

**当前边界：** LGPL-2.1 许可已定位；未执行分割。预处理改善不能只靠一张示例图判断。

### Co-optimized machine-learned manifold models for large eddy simulation of turbulent combustion

**研究问题：** 将热化学状态压缩到低维流形，并联合优化流形表示和输出重构，用于湍流燃烧 LES。

**实际入口：** get_strained_data.py → gen_trn_tst_data.py → train_models_strained_flames_raw.py → plot_strained.py。上游说明首个示例已附部分预处理数据。

**依赖与数据：** Python、Cantera、PyTorch、pandas、NumPy、scikit-learn、Matplotlib、SHERPA；DRM19 与 HyChem Jet-A 机理需另取。检查 use_GPU 和旧机理格式兼容。

**当前边界：** README 对部分源项损失的正确性亦保留说明，使用时需审查具体提交。仓库收纳不等于 Pele 耦合结果已复现。

### Learning dominant physical processes with data-driven balance models

**研究问题：** 从方程项数据识别不同区域的主导物理平衡，并在旋转爆轰简化模型中解释反应与输运竞争。

**实际入口：** 先阅读 Burgers 的解释性 notebook，再定位 Rotating detonation engine analogue；生成 RDE 数据需 pyclaw。

**依赖与数据：** scikit-learn、NumPy、SciPy、Matplotlib、seaborn；pyclaw 用于 RDE 数值数据，其他例题可能需要 pymech 或 MATLAB。

**当前边界：** MIT；期刊正式版与预印本对应以题名核对，燃烧案例仅是跨领域方法论文的一部分。

### Deep reinforcement learning for dynamic control of fuel injection timing in multi-pulse compression ignition engines

**研究问题：** 通过强化学习选择多次喷射压燃发动机的喷油时刻。

**实际入口：** scripts/ppo-example 下以 python ../main.py --fname input.toml 启动；先阅读 environment.yaml 和环境模型。

**依赖与数据：** 按 environment.yaml 建独立环境，检查发动机模型、机理和数值依赖；README 的 nosetests 是上游测试入口，本轮未执行。

**当前边界：** Apache-2.0；仿真训练收益不等于真实发动机闭环验证，JCR 年份/类别仍待确认。

## 固体燃料、热解与火灾安全

| 年份 / DOI | 论文 | 分区线索 | 代码与关系 | 收纳 |
|---|---|---|---|---|
| 2026 / [10.1016/j.fuel.2026.138977](https://doi.org/10.1016/j.fuel.2026.138977) | [CFD analysis of operating parameters and machine learning-aided optimization of reactor performance in a polyethylene pyrolysis fluidized bed](../08_solid_fuels_fire/01_kinetics_fire/Pd715d789f0/README.md) | Q1；官方年度待核 | [LitaoZhu201703/Machine-learning-aided-optimization-of-polyethylene-pyrolysis](../code_packages/LitaoZhu201703__Machine-learning-aided-optimization-of-polyethylene-pyrolysis/README.md)<br>author_implementation_readme_explicit | link_only |
| 2025 / [10.1016/j.cej.2025.160402](https://doi.org/10.1016/j.cej.2025.160402) | [Comprehensive thermal-kinetic uncertainty quantification of lithium-ion battery thermal runaway via bayesian chemical reaction neural networks](../08_solid_fuels_fire/01_kinetics_fire/P81568f3c50/README.md) | Q1；官方年度待核 | [DENG-MIT/CRNN](../code_packages/DENG-MIT__CRNN/README.md)<br>author_implementation_readme_explicit | partial_source_snapshot_collected |
| 2022 / [10.1016/j.combustflame.2022.111992](https://doi.org/10.1016/j.combustflame.2022.111992) | [Autonomous kinetic modeling of biomass pyrolysis using chemical reaction neural networks](../08_solid_fuels_fire/01_kinetics_fire/P4cbef1b3c9/README.md) | Q1；官方年度待核 | [DENG-MIT/Biomass.jl](../code_packages/DENG-MIT__Biomass.jl/README.md)<br>author_implementation_readme_explicit | source_archive_collected |
| 2022 / [10.1016/j.fuel.2022.125340](https://doi.org/10.1016/j.fuel.2022.125340) | [Active learning-based exploration of the catalytic pyrolysis of plastic waste](../08_solid_fuels_fire/01_kinetics_fire/P92264f9a97/README.md) | Q1；官方年度待核 | [yureel/GandALF](../code_packages/yureel__GandALF/README.md)<br>author_implementation_readme_explicit | source_archive_collected |
| 2020 / [10.1016/j.fuel.2020.117066](https://doi.org/10.1016/j.fuel.2020.117066) | [Classification of solid fuels with machine learning](../08_solid_fuels_fire/01_kinetics_fire/P53dcbe4b04/README.md) | Q1；官方年度待核 | [furkanelmaz/SolidFuelClassification](../code_packages/furkanelmaz__SolidFuelClassification/README.md)<br>author_implementation_readme_explicit | link_only |

### CFD analysis of operating parameters and machine learning-aided optimization of reactor performance in a polyethylene pyrolysis fluidized bed

**研究问题：** 用机器学习辅助优化聚乙烯热解过程，属于燃烧上游热转化的相邻应用。

**实际入口：** 先检查仓库文件与论文补充材料，确定训练入口、输入工况、目标产物及评价协议。

**依赖与数据：** README 未给出完整可复现环境；依赖和数据要求待逐文件核实。

**当前边界：** 未定位许可，仅固定链接；尚未执行，也不能仅凭仓库题名声称训练数据和权重齐备。

### Comprehensive thermal-kinetic uncertainty quantification of lithium-ion battery thermal runaway via bayesian chemical reaction neural networks

**研究问题：** 将 Bayesian CRNN 用于锂电热失控的热—动力学不确定度传播。

**实际入口：** 从对应 cathode/thermal runaway 子项目、项目环境与输入数据开始，按论文识别具体图表。

**依赖与数据：** Julia 子项目环境；采样/优化设置和计算预算需从论文及配置核对。

**当前边界：** 扩展到电池安全范围，不能与气相火焰精度直接横向排名。尚未执行论文结果。

### Autonomous kinetic modeling of biomass pyrolysis using chemical reaction neural networks

**研究问题：** 由热重分析数据自动建立生物质热解/氧化动力学，减少依赖专家预设反应路径。

**实际入口：** 从固定提交中的 Project.toml 和示例脚本建立 Julia 环境，再核对 TGA 数据、升温速率和残余质量定义。

**依赖与数据：** Julia 与上游 Project/Manifest；应为该仓库单独创建项目环境。不能用另一 CRNN 分支的 Julia 环境直接替代。

**当前边界：** TGA 有效反应网络不是唯一微观基元机理。小尺度热分析拟合不能直接证明大尺度火灾预测正确。

### Active learning-based exploration of the catalytic pyrolysis of plastic waste

**研究问题：** 用主动学习选择塑料催化热解实验，减少寻找合适工况所需的实验数量。

**实际入口：** GandALF.py 与 GandAlF.csv；先核对数据列、目标函数方向、采集函数和初始样本。

**依赖与数据：** README 给出 Python 3.6+、NumPy、SciPy、scikit-learn、pandas、GPy 和 GPyOpt；旧依赖需单独环境。

**当前边界：** MIT 许可已定位；尚未运行。基于已有表格的回放与真实在线选点应分别报告，不能将热解产物优化直接等同低排放燃烧。

### Classification of solid fuels with machine learning

**研究问题：** 根据燃料表征数据对固体燃料进行分层分类。

**实际入口：** main.py 调用 training.py 与 testing.py；README 说明默认读取预训练分类器，重训需要切换对应代码。

**依赖与数据：** 依赖版本应从脚本导入补齐；Excel 数据、特征含义和预训练文件兼容性需另核。

**当前边界：** 未定位许可，代码和数据仅保留固定链接。pkl 是可执行序列化格式，不在本库自动加载。未执行原文训练。

## 氢氨燃料、着火与燃料性质预测

| 年份 / DOI | 论文 | 分区线索 | 代码与关系 | 收纳 |
|---|---|---|---|---|
| 2026 / [10.1016/j.fuel.2026.138835](https://doi.org/10.1016/j.fuel.2026.138835) | [BayeSAF: Emulation and design of sustainable alternative fuels via Bayesian inference and descriptors-based machine learning](../09_fuels_properties/01_hydrogen_ammonia_properties/Pfa457cec99/README.md) | Q1；官方年度待核 | [JacopoLib/BayeSAF](../code_packages/JacopoLib__BayeSAF/README.md)<br>author_implementation_readme_explicit | link_only |
| 2025 / [10.1021/acs.energyfuels.4c06147](https://doi.org/10.1021/acs.energyfuels.4c06147) | [Advancing Sustainable Aviation Fuel Design: Machine Learning for High-Energy-Density Liquid Polycyclic Hydrocarbons](../09_fuels_properties/01_hydrogen_ammonia_properties/Pca19045ded/README.md) | Q1；官方年度待核 | [dkrijal100/Dataset-and-script-used-in-model-development](../code_packages/dkrijal100__Dataset-and-script-used-in-model-development/README.md)<br>author_implementation_readme_explicit | link_only |

### BayeSAF: Emulation and design of sustainable alternative fuels via Bayesian inference and descriptors-based machine learning

**研究问题：** 由目标性质反推可持续航空燃料的替代混合物组成，并表达组成的不确定性。

**实际入口：** 先从固定提交 README 的示例、数据说明和环境文件确定性质预测与后验推断入口，再检查具体实验配置。

**依赖与数据：** 依赖、数据库和采样配置以固定提交为准；数据权利与代码使用条件须分别核查。

**当前边界：** Prosperity Public License 3.0 限制商业使用，不是 OSI 开源；本库仅保留来源和固定链接，未运行或验证配方的实际燃烧性能。

### Advancing Sustainable Aviation Fuel Design: Machine Learning for High-Energy-Density Liquid Polycyclic Hydrocarbons

**研究问题：** 预测高能量密度液态多环烃性质，为可持续航空燃料设计提供分子筛选依据。

**实际入口：** 从上游数据集和建模脚本开始，核对分子标识、单位、重复分子和训练/测试划分。

**依赖与数据：** 以固定版本脚本导入和环境说明为准，未执行训练；外部 AFProp 数据的使用许可另核。

**当前边界：** 未找到源码许可，仅链接收纳。README 引用 Fuel 2021 DOI 10.1016/j.fuel.2021.121437 作为数据来源，不能把本仓库归作那篇论文的原始实现。

## 综述、数据集与共性方法

| 年份 / DOI | 论文 | 分区线索 | 代码与关系 | 收纳 |
|---|---|---|---|---|
| 2022 / [10.1016/j.jaecs.2022.100087](https://doi.org/10.1016/j.jaecs.2022.100087) | [BLASTNet: A call for community-involved big data in combustion machine learning](../10_reviews_methods/01_reviews_datasets/P42e1959567/README.md) | Q1；官方年度待核 | [blastnet/kaggle_tutorials](../code_packages/blastnet__kaggle_tutorials/README.md)<br>author_supporting_tutorial_readme_explicit | link_only |
| 2022 / [10.1016/j.pecs.2022.101010](https://doi.org/10.1016/j.pecs.2022.101010) | [Combustion machine learning: Principles, progress and prospects](../10_reviews_methods/01_reviews_datasets/Pb73c9cc517/README.md) | Q1；官方年度待核 | [IhmeGroup/CombML_Tutorials](../code_packages/IhmeGroup__CombML_Tutorials/README.md)<br>author_supporting_tutorial_readme_explicit | link_only |

### BLASTNet: A call for community-involved big data in combustion machine learning

**研究问题：** 让研究者能读取、理解并利用 BLASTNet 的三维可压缩反应流数据。

**实际入口：** 按上游 Open on Kaggle 入口定位 notebook，检查数据集版本后才运行；也可从本库 BLASTNet Python 客户端卡定位数据访问工具。

**依赖与数据：** Kaggle 运行环境、对应 BLASTNet 数据与各自许可；未登录运行，也未下载大规模 DNS 数据。

**当前边界：** 教程未定位明确源码许可，仅保留固定链接。该期刊的二级分区表存在疑点，分区继续待核实。

### Combustion machine learning: Principles, progress and prospects

**研究问题：** 为理解燃烧机器学习的主要范式提供可阅读的入门实现。

**实际入口：** 按上游目录逐个读取监督/无监督 notebook 与强化学习接口，先核对输入特征和示例数据。

**依赖与数据：** 各教程导入与环境需要单独核对；没有统一依赖锁文件的地方保留待办。

**当前边界：** 未定位许可文件，链接收纳；不把通用课堂例子计为燃烧 Q1 论文复现。

## 本轮未强行建立论文关联的线索

- DENG-MIT/Inference_ConstV_EMs：README 明确要求邮件申请源码，不能把公开介绍页计为已收纳实现。
- lz1025/AL-GA-combustion：README 的论文题名未匹配唯一 DOI，作为工具保留。
- THGLab/H2Combustion_AL：燃烧主动学习源码可收纳，具体论文对应待核。
- REALM、GBCT：预印本/开发中工作；数据与权重的承诺不等于已提供。
- G-PARC、流场三维重建和热声制冷 COP：本轮查看后未确认直接燃烧研究，不放入燃烧核心论文列表。
- 同一 ORCh/DFODE/CRNN 工具被多篇文章引用时，按关系类型逐篇说明，代码包只计一个。
