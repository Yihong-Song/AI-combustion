# 热声不稳定性预测、辨识与控制

识别火焰放热与声波之间的正反馈，在振荡扩大前预警或采取控制。

本目录含 27 条候选。分区与全文状态逐篇标注；自动分类以研究目标优先，交叉方法可在总库检索。

[返回首页](../README.md) · [全局地图](../00_literature_map/README.md) · [方法与范围](../docs/METHODOLOGY.md)

## 核心问题

任务是当前状态分类、未来提前量预测、火焰传递函数辨识还是闭环控制？这些任务不能共用一个模糊的准确率。

## 方法演进与比较

声压/图像特征、CNN-LSTM、递归图、reservoir computing、物理信息 RNN、模型自由/离线强化学习和实时 FPGA 部署。

## 数据与物理定义

同步压力、速度、热释放代理和控制信号；保留采样频率、同步误差、操作条件变化及振荡起始定义。

## 怎样判断模型有效

提前量、误报/漏报、按实验统计的 PR-AUC、概率校准；辨识用增益/相位；控制用压力 RMS、执行器能量、约束违背与恢复时间。

## 如何避免数据泄漏

整次试验或整台燃烧器留出，滑动窗口须设置时间隔离区；不能让同一事件相邻窗口跨训练测试。

## 主要局限与选题问题

操作条件漂移、传感器延迟、观测代理偏差和控制策略的分布外动作。离线策略回报不等于真实燃烧器闭环验证。

## 建议阅读和实践路径

先定义不稳定性与预警提前量，再读 flame dynamics 辨识，最后比较控制策略和跨装置验证。

## 细分类与论文索引

分区栏为二级来源线索；Q? 为待核实。代码 ✓ 仅表示论文链接已核对，不表示执行成功。

### [预警与系统辨识](01_prediction_identification/README.md)（21）

| 年份 | 论文 | 分区线索 | 代码 |
|---|---|---|---|
| 2026 | [Upscaling very low-resolution chemiluminescence images for predicting a marker of the thermoacoustic source term using machine learning](01_prediction_identification/P02a7acbe36/README.md) | Q1 | 待核对 |
| 2026 | [Monitoring thermoacoustic instability: A comparative analysis of feature-based and end-to-end deep learning approaches](01_prediction_identification/P4fe20073fb/README.md) | Q? | 待核对 |
| 2026 | [Zero-shot prediction of thermoacoustic instability precursors via phase-space reconstruction and CNN-based recurrence learning](01_prediction_identification/P37098298f6/README.md) | Q1 | 待核对 |
| 2026 | [A generalizable deep learning model for thermoacoustic instability real-time prediction: FPGA implementation and cross-engine validation](01_prediction_identification/P94dd924461/README.md) | Q1 | 待核对 |
| 2026 | [Deep learning for continuous lead-time prediction of thermoacoustic instabilities in an annular combustor](01_prediction_identification/P51fe566a45/README.md) | Q1 | ✓ |
| 2025 | [Convolutional neural network-based multi-modal detection model for combustion instability in swirling flames](01_prediction_identification/Pdb69202380/README.md) | Q1 | 待核对 |
| 2025 | [Hybrid modeling of thermoacoustic oscillations: Integrating signal processing and machine learning for accurate detection](01_prediction_identification/P8d5a254dc2/README.md) | Q? | 待核对 |
| 2024 | [Inferring unknown unknowns: Regularized bias-aware ensemble Kalman filter](01_prediction_identification/P0783e678e5/README.md) | Q1 | ✓ |
| 2024 | [Learning thermoacoustic interactions in combustors using a physics-informed neural network](01_prediction_identification/P6b42fbab14/README.md) | Q1 | 待核对 |
| 2024 | [From abstraction to design: Interpretable tree-based machine learning for stable thermoacoustic system layout](01_prediction_identification/P8248bbed04/README.md) | Q1 | 待核对 |
| 2024 | [A real-time digital twin of azimuthal thermoacoustic instabilities](01_prediction_identification/P0e5f9b5e09/README.md) | Q? | ✓ |
| 2023 | [Physics-informed recurrent neural networks for linear and nonlinear flame dynamics](01_prediction_identification/Pead10cb821/README.md) | Q1 | 待核对 |
| 2023 | [Pre-trained combustion model and transfer learning in thermoacoustic instability](01_prediction_identification/P622ff7c3cf/README.md) | Q? | 待核对 |
| 2023 | [Hard-constrained neural networks for modeling nonlinear acoustics](01_prediction_identification/Pa68d424897/README.md) | Q? | ✓ |
| 2022 | [Physics-aware neural network flame closure for combustion instability modeling in a single-injector engine](01_prediction_identification/Pc15a3753cb/README.md) | Q1 | 待核对 |
| 2022 | [Real-time thermoacoustic data assimilation](01_prediction_identification/P97829e9574/README.md) | Q? | ✓ |
| 2021 | [Detection of precursors of combustion instability using convolutional recurrent neural networks](01_prediction_identification/P455fdff4f1/README.md) | Q1 | 待核对 |
| 2021 | [A comprehensive investigation of LSTM-CNN deep learning model for fast detection of combustion instability](01_prediction_identification/Pb3f87b5e85/README.md) | Q1 | 待核对 |
| 2021 | [Robust identification of flame frequency response via multi-fidelity Gaussian process approach](01_prediction_identification/P67741bfd8c/README.md) | Q1 | ✓ |
| 2021 | [Early detection of thermoacoustic instabilities in a cryogenic rocket thrust chamber using combustion noise features and machine learning](01_prediction_identification/Pcdae18b5cb/README.md) | Q? | 待核对 |
| 2019 | [Early detection of thermoacoustic combustion oscillations using a methodology combining statistical complexity and machine learning](01_prediction_identification/P74cbb6fbf7/README.md) | Q? | 待核对 |

### [主动控制与强化学习](02_control/README.md)（6）

| 年份 | 论文 | 分区线索 | 代码 |
|---|---|---|---|
| 2026 | [Offline reinforcement learning for mitigating thermoacoustic instabilities in a laminar premixed flame](02_control/P284e852930/README.md) | Q? | 待核对 |
| 2025 | [Numerical and experiment investigations on control of combustion instability for a dual-swirl burner using deep reinforcement learning](02_control/P3b136f113b/README.md) | Q1 | 待核对 |
| 2025 | [Deep reinforcement learning for adaptive control of thermoacoustic instabilities in a lean-premixed methane/hydrogen/air combustor](02_control/P56e9d099db/README.md) | Q1 | 待核对 |
| 2024 | [Controlling thermoacoustic instability of a laminar premixed flame with deep reinforcement learning and neural autoregressive models](02_control/Pfc1d464246/README.md) | Q1 | 待核对 |
| 2024 | [Data-driven computation of adjoint sensitivities without adjoint solvers: An application to thermoacoustics](02_control/P9903dd056c/README.md) | Q? | ✓ |
| 2023 | [Adaptive phase shift control of thermoacoustic combustion instabilities using model-free reinforcement learning](02_control/P1695126aae/README.md) | Q1 | 待核对 |
