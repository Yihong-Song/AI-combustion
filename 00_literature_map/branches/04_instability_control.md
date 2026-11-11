# 热声不稳定性预测、辨识与控制

识别火焰放热与声波之间的正反馈，在振荡扩大前预警或采取控制。

[返回全景](../README.md) · [方向技术说明](../../04_instability_control/README.md)

## 物理目标与评价逻辑

任务是当前状态分类、未来提前量预测、火焰传递函数辨识还是闭环控制？这些任务不能共用一个模糊的准确率。

提前量、误报/漏报、按实验统计的 PR-AUC、概率校准；辨识用增益/相位；控制用压力 RMS、执行器能量、约束违背与恢复时间。

## 方法与数据

声压/图像特征、CNN-LSTM、递归图、reservoir computing、物理信息 RNN、模型自由/离线强化学习和实时 FPGA 部署。

同步压力、速度、热释放代理和控制信号；保留采样频率、同步误差、操作条件变化及振荡起始定义。

## 风险与阅读路线

操作条件漂移、传感器延迟、观测代理偏差和控制策略的分布外动作。离线策略回报不等于真实燃烧器闭环验证。

先定义不稳定性与预警提前量，再读 flame dynamics 辨识，最后比较控制策略和跨装置验证。

## 预警与系统辨识

| 年份 | 论文 | 方向 | 分区状态 | 代码 |
|---|---|---|---|---|
| 2026 | [Upscaling very low-resolution chemiluminescence images for predicting a marker of the thermoacoustic source term using machine learning](../../04_instability_control/01_prediction_identification/P02a7acbe36/README.md) | 热声不稳定性预测、辨识与控制 | provisional_q1_q2 | 待核对 |
| 2026 | [Monitoring thermoacoustic instability: A comparative analysis of feature-based and end-to-end deep learning approaches](../../04_instability_control/01_prediction_identification/P4fe20073fb/README.md) | 热声不稳定性预测、辨识与控制 | pending_jcr | 待核对 |
| 2026 | [Zero-shot prediction of thermoacoustic instability precursors via phase-space reconstruction and CNN-based recurrence learning](../../04_instability_control/01_prediction_identification/P37098298f6/README.md) | 热声不稳定性预测、辨识与控制 | provisional_q1_q2 | 待核对 |
| 2026 | [A generalizable deep learning model for thermoacoustic instability real-time prediction: FPGA implementation and cross-engine validation](../../04_instability_control/01_prediction_identification/P94dd924461/README.md) | 热声不稳定性预测、辨识与控制 | provisional_q1_q2 | 待核对 |
| 2026 | [Deep learning for continuous lead-time prediction of thermoacoustic instabilities in an annular combustor](../../04_instability_control/01_prediction_identification/P51fe566a45/README.md) | 热声不稳定性预测、辨识与控制 | provisional_q1_q2 | 待核对 |
| 2025 | [Convolutional neural network-based multi-modal detection model for combustion instability in swirling flames](../../04_instability_control/01_prediction_identification/Pdb69202380/README.md) | 热声不稳定性预测、辨识与控制 | provisional_q1_q2 | 待核对 |
| 2025 | [Hybrid modeling of thermoacoustic oscillations: Integrating signal processing and machine learning for accurate detection](../../04_instability_control/01_prediction_identification/P8d5a254dc2/README.md) | 热声不稳定性预测、辨识与控制 | pending_jcr | 待核对 |
| 2024 | [From abstraction to design: Interpretable tree-based machine learning for stable thermoacoustic system layout](../../04_instability_control/01_prediction_identification/P8248bbed04/README.md) | 热声不稳定性预测、辨识与控制 | provisional_q1_q2 | 待核对 |
| 2023 | [Physics-informed recurrent neural networks for linear and nonlinear flame dynamics](../../04_instability_control/01_prediction_identification/Pead10cb821/README.md) | 热声不稳定性预测、辨识与控制 | provisional_q1_q2 | 待核对 |
| 2023 | [Pre-trained combustion model and transfer learning in thermoacoustic instability](../../04_instability_control/01_prediction_identification/P622ff7c3cf/README.md) | 热声不稳定性预测、辨识与控制 | pending_jcr | 待核对 |
| 2022 | [Physics-aware neural network flame closure for combustion instability modeling in a single-injector engine](../../04_instability_control/01_prediction_identification/Pc15a3753cb/README.md) | 热声不稳定性预测、辨识与控制 | provisional_q1_q2 | 待核对 |
| 2021 | [Detection of precursors of combustion instability using convolutional recurrent neural networks](../../04_instability_control/01_prediction_identification/P455fdff4f1/README.md) | 热声不稳定性预测、辨识与控制 | provisional_q1_q2 | 待核对 |
| 2021 | [A comprehensive investigation of LSTM-CNN deep learning model for fast detection of combustion instability](../../04_instability_control/01_prediction_identification/Pb3f87b5e85/README.md) | 热声不稳定性预测、辨识与控制 | provisional_q1_q2 | 待核对 |

## 主动控制与强化学习

| 年份 | 论文 | 方向 | 分区状态 | 代码 |
|---|---|---|---|---|
| 2026 | [Offline reinforcement learning for mitigating thermoacoustic instabilities in a laminar premixed flame](../../04_instability_control/02_control/P284e852930/README.md) | 热声不稳定性预测、辨识与控制 | pending_jcr | 待核对 |
| 2025 | [Numerical and experiment investigations on control of combustion instability for a dual-swirl burner using deep reinforcement learning](../../04_instability_control/02_control/P3b136f113b/README.md) | 热声不稳定性预测、辨识与控制 | provisional_q1_q2 | 待核对 |
| 2025 | [Deep reinforcement learning for adaptive control of thermoacoustic instabilities in a lean-premixed methane/hydrogen/air combustor](../../04_instability_control/02_control/P56e9d099db/README.md) | 热声不稳定性预测、辨识与控制 | provisional_q1_q2 | 待核对 |
| 2024 | [Controlling thermoacoustic instability of a laminar premixed flame with deep reinforcement learning and neural autoregressive models](../../04_instability_control/02_control/Pfc1d464246/README.md) | 热声不稳定性预测、辨识与控制 | provisional_q1_q2 | 待核对 |
| 2023 | [Adaptive phase shift control of thermoacoustic combustion instabilities using model-free reinforcement learning](../../04_instability_control/02_control/P1695126aae/README.md) | 热声不稳定性预测、辨识与控制 | provisional_q1_q2 | 待核对 |
