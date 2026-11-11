# 神经算子、降阶与流场重建

从少量状态、低分辨率场或参数，预测完整流场及其演化，减少重复高保真模拟。

本目录含 13 条候选。分区与全文状态逐篇标注；自动分类以研究目标优先，交叉方法可在总库检索。

[返回首页](../README.md) · [全局地图](../00_literature_map/README.md) · [方法与范围](../docs/METHODOLOGY.md)

## 核心问题

学习的是一个固定网格的映射还是跨输入函数的算子？超分辨率的细节是否由观测约束，还是模型生成？

## 方法演进与比较

POD/PCA、自编码器、Koopman、DeepONet、FNO/F-FNO、PINO、生成模型和 flow matching。分别检查边界、几何、分辨率和时间推进方式。

## 数据与物理定义

时序 DNS/LES、参数化一维火焰、低高分辨率配对场。明示插值、滤波和下采样流程，保留物理坐标。

## 怎样判断模型有效

场相对 L2、梯度和界面误差、谱、结构函数、守恒、极端放热、长时滚动；仅看 PSNR 或漂亮图像不够。

## 如何避免数据泄漏

留出完整模拟、参数区间、网格分辨率和几何。若声称零样本分辨率迁移，应另测从未训练的网格。

## 主要局限与选题问题

训练分布之外的边界/机理可能失败；生成模型产生的高频细节未必真实；部分工具只有预印本或数据需申请。

## 建议阅读和实践路径

先读降阶和数据表示，再从同网格预测推进到跨参数、跨分辨率和多步演化。POD-PINO 仅列工具线索，不能预设其已发表 Q1。

## 细分类与论文索引

分区栏为二级来源线索；Q? 为待核实。代码 ✓ 仅表示论文链接已核对，不表示执行成功。

### [算子、降阶与超分辨率](01_operators_rom/README.md)（11）

| 年份 | 论文 | 分区线索 | 代码 |
|---|---|---|---|
| 2026 | [RFNO-PINN: A Physics-Informed Neural Operator for Predicting Multi-Species Combustion Dynamics](01_operators_rom/P38d6e70b6e/README.md) | Q1 | 待核对 |
| 2026 | [MG-ANN: An online extension of reduced-order modeling with continual learning for turbulent reacting flows](01_operators_rom/Pe8845825fd/README.md) | Q1 | 待核对 |
| 2026 | [Error control of uncertainty-aware neural network-coupled binary trees for manifold-based combustion models](01_operators_rom/Pcc65cb53e0/README.md) | Q1 | 待核对 |
| 2026 | [Generate reacting flow fields with flow matching neural operators on high-resolution grids](01_operators_rom/P8514c23cfb/README.md) | Q1 | 待核对 |
| 2025 | [Single-snapshot-based dynamical mode prediction of a flickering flame via a Fourier-neural-operator network](01_operators_rom/P09e21465b5/README.md) | Q? | 待核对 |
| 2024 | [A co-kurtosis PCA based dimensionality reduction with nonlinear reconstruction using neural networks](01_operators_rom/P5277d1faad/README.md) | Q1 | 待核对 |
| 2024 | [Learning transient evolution of multidimensional reacting flows by multiscale Fourier neural operators](01_operators_rom/Pd2e2c3f559/README.md) | Q1 | 待核对 |
| 2023 | [Investigation of the generalization capability of a generative adversarial network for large eddy simulation of turbulent premixed reacting flows](01_operators_rom/P1ecbf73e07/README.md) | Q1 | 待核对 |
| 2022 | [Efficient premixed turbulent combustion simulations using flamelet manifold neural networks: A priori and a posteriori assessment](01_operators_rom/Pda27917d2f/README.md) | Q1 | 待核对 |
| 2021 | [Using physics-informed enhanced super-resolution generative adversarial networks for subfilter modeling in turbulent reactive flows](01_operators_rom/Pf8b971ed35/README.md) | Q1 | 待核对 |
| 2019 | [Direct mapping from LES resolved scales to filtered-flame generated manifolds using convolutional neural networks](01_operators_rom/Pc11b176f24/README.md) | Q1 | 待核对 |

### [一般反应流重建](02_general_flow_reconstruction/README.md)（2）

| 年份 | 论文 | 分区线索 | 代码 |
|---|---|---|---|
| 2024 | [Acceleration of the complex reacting flow simulation with a generalizable neural network based on meta-learning](02_general_flow_reconstruction/P760d912715/README.md) | Q1 | 待核对 |
| 2024 | [An integrated framework for accelerating reactive flow simulation using GPU and machine learning models](02_general_flow_reconstruction/P036f632de4/README.md) | Q1 | 待核对 |
