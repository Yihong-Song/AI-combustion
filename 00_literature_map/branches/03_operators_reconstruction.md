# 神经算子、降阶与流场重建

从少量状态、低分辨率场或参数，预测完整流场及其演化，减少重复高保真模拟。

[返回全景](../README.md) · [方向技术说明](../../03_operators_reconstruction/README.md)

## 物理目标与评价逻辑

学习的是一个固定网格的映射还是跨输入函数的算子？超分辨率的细节是否由观测约束，还是模型生成？

场相对 L2、梯度和界面误差、谱、结构函数、守恒、极端放热、长时滚动；仅看 PSNR 或漂亮图像不够。

## 方法与数据

POD/PCA、自编码器、Koopman、DeepONet、FNO/F-FNO、PINO、生成模型和 flow matching。分别检查边界、几何、分辨率和时间推进方式。

时序 DNS/LES、参数化一维火焰、低高分辨率配对场。明示插值、滤波和下采样流程，保留物理坐标。

## 风险与阅读路线

训练分布之外的边界/机理可能失败；生成模型产生的高频细节未必真实；部分工具只有预印本或数据需申请。

先读降阶和数据表示，再从同网格预测推进到跨参数、跨分辨率和多步演化。POD-PINO 仅列工具线索，不能预设其已发表 Q1。

## 算子、降阶与超分辨率

| 年份 | 论文 | 方向 | 分区状态 | 代码 |
|---|---|---|---|---|
| 2026 | [RFNO-PINN: A Physics-Informed Neural Operator for Predicting Multi-Species Combustion Dynamics](../../03_operators_reconstruction/01_operators_rom/P38d6e70b6e/README.md) | 神经算子、降阶与流场重建 | provisional_q1_q2 | 待核对 |
| 2026 | [MG-ANN: An online extension of reduced-order modeling with continual learning for turbulent reacting flows](../../03_operators_reconstruction/01_operators_rom/Pe8845825fd/README.md) | 神经算子、降阶与流场重建 | provisional_q1_q2 | 待核对 |
| 2026 | [Error control of uncertainty-aware neural network-coupled binary trees for manifold-based combustion models](../../03_operators_reconstruction/01_operators_rom/Pcc65cb53e0/README.md) | 神经算子、降阶与流场重建 | provisional_q1_q2 | 待核对 |
| 2026 | [Generate reacting flow fields with flow matching neural operators on high-resolution grids](../../03_operators_reconstruction/01_operators_rom/P8514c23cfb/README.md) | 神经算子、降阶与流场重建 | provisional_q1_q2 | 待核对 |
| 2025 | [Single-snapshot-based dynamical mode prediction of a flickering flame via a Fourier-neural-operator network](../../03_operators_reconstruction/01_operators_rom/P09e21465b5/README.md) | 神经算子、降阶与流场重建 | pending_jcr | 待核对 |
| 2024 | [A co-kurtosis PCA based dimensionality reduction with nonlinear reconstruction using neural networks](../../03_operators_reconstruction/01_operators_rom/P5277d1faad/README.md) | 神经算子、降阶与流场重建 | provisional_q1_q2 | 待核对 |
| 2024 | [Learning transient evolution of multidimensional reacting flows by multiscale Fourier neural operators](../../03_operators_reconstruction/01_operators_rom/Pd2e2c3f559/README.md) | 神经算子、降阶与流场重建 | provisional_q1_q2 | 待核对 |
| 2023 | [Investigation of the generalization capability of a generative adversarial network for large eddy simulation of turbulent premixed reacting flows](../../03_operators_reconstruction/01_operators_rom/P1ecbf73e07/README.md) | 神经算子、降阶与流场重建 | provisional_q1_q2 | 待核对 |
| 2022 | [Efficient premixed turbulent combustion simulations using flamelet manifold neural networks: A priori and a posteriori assessment](../../03_operators_reconstruction/01_operators_rom/Pda27917d2f/README.md) | 神经算子、降阶与流场重建 | provisional_q1_q2 | 待核对 |
| 2021 | [Using physics-informed enhanced super-resolution generative adversarial networks for subfilter modeling in turbulent reactive flows](../../03_operators_reconstruction/01_operators_rom/Pf8b971ed35/README.md) | 神经算子、降阶与流场重建 | provisional_q1_q2 | 待核对 |
| 2019 | [Direct mapping from LES resolved scales to filtered-flame generated manifolds using convolutional neural networks](../../03_operators_reconstruction/01_operators_rom/Pc11b176f24/README.md) | 神经算子、降阶与流场重建 | provisional_q1_q2 | 待核对 |

## 一般反应流重建

| 年份 | 论文 | 方向 | 分区状态 | 代码 |
|---|---|---|---|---|
| 2024 | [Acceleration of the complex reacting flow simulation with a generalizable neural network based on meta-learning](../../03_operators_reconstruction/02_general_flow_reconstruction/P760d912715/README.md) | 神经算子、降阶与流场重建 | provisional_q1_q2 | 待核对 |
| 2024 | [An integrated framework for accelerating reactive flow simulation using GPU and machine learning models](../../03_operators_reconstruction/02_general_flow_reconstruction/P036f632de4/README.md) | 神经算子、降阶与流场重建 | provisional_q1_q2 | 待核对 |
