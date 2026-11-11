# 光学诊断、反演、烟炱与辐射

让光谱和图像提供更可靠的温度、组分和三维场信息，并加速参与性介质辐射计算。

[返回全景](../README.md) · [方向技术说明](../../05_diagnostics_radiation/README.md)

## 物理目标与评价逻辑

观测算子是什么？相机图像、谱线、纹影位移与温度/浓度之间的关系不同，不能把图像分类模型直接当作定量诊断。

温度/浓度偏差与不确定度、谱峰面积、重投影误差、三维真值误差；辐射报告热流/源项和积分能量；烟炱报告体积分数及粒径统计。

## 方法与数据

CNN 去噪、层析重建、神经隐式表示、PINN 反演、WSGG/FSCK 神经代理、烟炱生成模型。实验反演与数值辐射代理分开评价。

标定后光谱/图像、相机几何、LBL 参考与合成投影；记录噪声模型、光学厚度、波段、视角和燃料组成。

## 风险与阅读路线

有限视角不可辨识、标定误差、烟炱自吸收及域差异。NIR-BOS 有非商业许可；DU_CNN 无明确许可；这些状态必须保留。

从前向观测模型入手，再比较解析/迭代方法与神经反演；辐射可从 WSGG-H2O-CO2-NH3 的轻量验证开始。

## 光谱、图像与层析反演

| 年份 | 论文 | 方向 | 分区状态 | 代码 |
|---|---|---|---|---|
| 2026 | [Resolution-invariant temperature and species field reconstruction using factorized Fourier neural operator (F-FNO) for turbulent jet flames](../../05_diagnostics_radiation/01_optical_inverse/P90fd45dab0/README.md) | 光学诊断、反演、烟炱与辐射 | provisional_q1_q2 | 待核对 |
| 2026 | [Neural refractive index primitives for flame field reconstruction using background-oriented schlieren](../../05_diagnostics_radiation/01_optical_inverse/Pc2b8d1f214/README.md) | 光学诊断、反演、烟炱与辐射 | provisional_q1_q2 | 已核对链接 |
| 2026 | [Deep learning segmentation of thermo-diffusively unstable premixed spherical flames](../../05_diagnostics_radiation/01_optical_inverse/Pccc416d6c9/README.md) | 光学诊断、反演、烟炱与辐射 | provisional_q1_q2 | 待核对 |
| 2026 | [A new deep learning method for temperature determination from CPP fs-CARS spectra](../../05_diagnostics_radiation/01_optical_inverse/Pfd68034a90/README.md) | 光学诊断、反演、烟炱与辐射 | provisional_q1_q2 | 待核对 |
| 2026 | [Identifying and mapping flare plume species using hyperspectral imaging and machine learning](../../05_diagnostics_radiation/01_optical_inverse/P81be5ecc3b/README.md) | 光学诊断、反演、烟炱与辐射 | provisional_q1_q2 | 待核对 |
| 2026 | [Quantitative electric field diagnostics in plasma-flame interaction via machine-learning-assisted inverse E-FISH](../../05_diagnostics_radiation/01_optical_inverse/Pc33c29fd49/README.md) | 光学诊断、反演、烟炱与辐射 | provisional_q1_q2 | 待核对 |
| 2026 | [In-cylinder knock diagnostics of a spark-ignition engine using deep learning-based optical flow and flame luminosity](../../05_diagnostics_radiation/01_optical_inverse/P69aa6cc376/README.md) | 光学诊断、反演、烟炱与辐射 | provisional_q1_q2 | 待核对 |
| 2026 | [Chemiluminescence-driven machine learning models for combustion sensing in cyclonic reactors](../../05_diagnostics_radiation/01_optical_inverse/P52fe6f3fb9/README.md) | 光学诊断、反演、烟炱与辐射 | provisional_q1_q2 | 待核对 |
| 2025 | [Denoising neural network for low-light imaging of acoustically coupled combustion](../../05_diagnostics_radiation/01_optical_inverse/Pf4e7cf10c2/README.md) | 光学诊断、反演、烟炱与辐射 | provisional_q1_q2 | 待核对 |
| 2025 | [Unsupervised neural-implicit laser absorption tomography for quantitative imaging of unsteady flames](../../05_diagnostics_radiation/01_optical_inverse/P517be61bbe/README.md) | 光学诊断、反演、烟炱与辐射 | provisional_q1_q2 | 待核对 |
| 2025 | [Self-supervised combustion state diagnosis using a noise-augmented generative adversarial network and flame image sequences](../../05_diagnostics_radiation/01_optical_inverse/P0c63e9e6b2/README.md) | 光学诊断、反演、烟炱与辐射 | provisional_q1_q2 | 待核对 |
| 2025 | [Prediction of combustion pressure with deep learning using flame images](../../05_diagnostics_radiation/01_optical_inverse/Pe2ed142c69/README.md) | 光学诊断、反演、烟炱与辐射 | provisional_q1_q2 | 待核对 |
| 2025 | [Real-time analysis of flame chemiluminescence spectra for equivalence ratio and gas composition using neural network approaches](../../05_diagnostics_radiation/01_optical_inverse/P862951f47b/README.md) | 光学诊断、反演、烟炱与辐射 | pending_jcr | 待核对 |
| 2025 | [SAGE: A machine learning model for primary particle segmentation in TEM images of soot aggregates](../../05_diagnostics_radiation/01_optical_inverse/P56771c427a/README.md) | 光学诊断、反演、烟炱与辐射 | provisional_q1_q2 | 已核对链接 |
| 2025 | [Cross domain fault diagnosis in internal combustion engines using multisensor data with transfer federated and transformer based federated transfer learning](../../05_diagnostics_radiation/01_optical_inverse/Pe94377b2b8/README.md) | 光学诊断、反演、烟炱与辐射 | pending_jcr | 待核对 |
| 2025 | [Aero-engine combustion flame segmentation via Vision Transformer](../../05_diagnostics_radiation/01_optical_inverse/P327ef4ffb3/README.md) | 光学诊断、反演、烟炱与辐射 | pending_jcr | 待核对 |
| 2024 | [Machine learning based technique for outlier detection and result prediction in combustion diagnostics](../../05_diagnostics_radiation/01_optical_inverse/P92e39e0dd8/README.md) | 光学诊断、反演、烟炱与辐射 | pending_jcr | 待核对 |
| 2024 | [Machine learning-based prediction of swirl combustor operation from flame imaging](../../05_diagnostics_radiation/01_optical_inverse/P787f82787c/README.md) | 光学诊断、反演、烟炱与辐射 | provisional_q1_q2 | 待核对 |
| 2024 | [Multi-speciation in shock tube kinetics using deep neural networks and cavity-enhanced absorption spectroscopy](../../05_diagnostics_radiation/01_optical_inverse/P67a96f84e4/README.md) | 光学诊断、反演、烟炱与辐射 | provisional_q1_q2 | 待核对 |
| 2024 | [PENTAGON: Physics-enhanced neural network for volumetric flame chemiluminescence tomography](../../05_diagnostics_radiation/01_optical_inverse/P3ebceccfd6/README.md) | 光学诊断、反演、烟炱与辐射 | pending_jcr | 待核对 |
| 2023 | [Deep learning-based denoising for fast time-resolved flame emission spectroscopy in high-pressure combustion environment](../../05_diagnostics_radiation/01_optical_inverse/P2949b85479/README.md) | 光学诊断、反演、烟炱与辐射 | provisional_q1_q2 | 已核对链接 |
| 2023 | [Multi-speciation in shock tube experiments using a single laser and deep neural networks](../../05_diagnostics_radiation/01_optical_inverse/Pec912f329e/README.md) | 光学诊断、反演、烟炱与辐射 | provisional_q1_q2 | 待核对 |
| 2023 | [Detection of slight variations in combustion conditions with machine learning and computer vision](../../05_diagnostics_radiation/01_optical_inverse/P205f01358c/README.md) | 光学诊断、反演、烟炱与辐射 | provisional_q1_q2 | 待核对 |
| 2023 | [Random forest classifier and neural network for fraction identification of refuse-derived fuel images](../../05_diagnostics_radiation/01_optical_inverse/P526fe71fb8/README.md) | 光学诊断、反演、烟炱与辐射 | provisional_q1_q2 | 待核对 |
| 2023 | [A supervised machine learning technique for combustion diagnosis using a vibration sensor signal](../../05_diagnostics_radiation/01_optical_inverse/Pfbd8583acd/README.md) | 光学诊断、反演、烟炱与辐射 | provisional_q1_q2 | 待核对 |
| 2023 | [Predicting real-time fire heat release rate by flame images and deep learning](../../05_diagnostics_radiation/01_optical_inverse/P70b5e8ccbc/README.md) | 光学诊断、反演、烟炱与辐射 | provisional_q1_q2 | 待核对 |
| 2022 | [Data-driven discovery of heat release rate markers for premixed NH3/H2/air flames using physics-informed machine learning](../../05_diagnostics_radiation/01_optical_inverse/Pd9de613208/README.md) | 光学诊断、反演、烟炱与辐射 | provisional_q1_q2 | 已核对链接 |
| 2021 | [Prediction of combustion state through a semi-supervised learning model and flame imaging](../../05_diagnostics_radiation/01_optical_inverse/Pf4fca88ca3/README.md) | 光学诊断、反演、烟炱与辐射 | provisional_q1_q2 | 待核对 |
| 2021 | [Online dynamic prediction of potassium concentration in biomass fuels through flame spectroscopic analysis and recurrent neural network modelling](../../05_diagnostics_radiation/01_optical_inverse/Pac30907733/README.md) | 光学诊断、反演、烟炱与辐射 | provisional_q1_q2 | 待核对 |
| 2021 | [Extracting information overlap in simultaneous OH-PLIF and PIV fields with neural networks](../../05_diagnostics_radiation/01_optical_inverse/Pe254b41d35/README.md) | 光学诊断、反演、烟炱与辐射 | provisional_q1_q2 | 待核对 |
| 2021 | [Using deep neural networks to diagnose engine pre-ignition](../../05_diagnostics_radiation/01_optical_inverse/P038c349561/README.md) | 光学诊断、反演、烟炱与辐射 | provisional_q1_q2 | 待核对 |
| 2020 | [Combustion stability monitoring through flame imaging and stacked sparse autoencoder based deep neural network](../../05_diagnostics_radiation/01_optical_inverse/P92c45b121f/README.md) | 光学诊断、反演、烟炱与辐射 | provisional_q1_q2 | 待核对 |
| 2020 | [Limited-projection volumetric tomography for time-resolved turbulent combustion diagnostics via deep learning](../../05_diagnostics_radiation/01_optical_inverse/Pf9b2805ec8/README.md) | 光学诊断、反演、烟炱与辐射 | provisional_q1_q2 | 待核对 |
| 2019 | [Artificial neural network regression model to predict flue gas temperature and emissions with the spectral norm of flame image](../../05_diagnostics_radiation/01_optical_inverse/P957b6e7e23/README.md) | 光学诊断、反演、烟炱与辐射 | provisional_q1_q2 | 待核对 |
| 2019 | [Three-dimensional rapid flame chemiluminescence tomography via deep learning](../../05_diagnostics_radiation/01_optical_inverse/P7ee84c5222/README.md) | 光学诊断、反演、烟炱与辐射 | pending_jcr | 待核对 |

## 辐射与烟炱辐射诊断

| 年份 | 论文 | 方向 | 分区状态 | 代码 |
|---|---|---|---|---|
| 2026 | [Time-resolved three-dimensional temperature field reconstruction of soot flames using physics-informed neural networks](../../05_diagnostics_radiation/02_radiation_soot/P3ab0a17fd1/README.md) | 光学诊断、反演、烟炱与辐射 | provisional_q1_q2 | 待核对 |
| 2026 | [Emulating non-gray gas radiative heat transfer in combustion scenarios by machine learning method](../../05_diagnostics_radiation/02_radiation_soot/P1b32df0983/README.md) | 光学诊断、反演、烟炱与辐射 | pending_jcr | 待核对 |
| 2026 | [Physics-informed neural network WSGG model for radiative heat transfer in H2O–CO2–NH3 gas mixtures relevant to ammonia combustion](../../05_diagnostics_radiation/02_radiation_soot/P69b4098fb3/README.md) | 光学诊断、反演、烟炱与辐射 | provisional_q1_q2 | 已核对链接 |
| 2026 | [Efficient modelling of non-grey radiation in a swirl turbulent ammonia flame using compensatory physics-informed neural networks](../../05_diagnostics_radiation/02_radiation_soot/Pab211520a3/README.md) | 光学诊断、反演、烟炱与辐射 | provisional_q1_q2 | 待核对 |
| 2026 | [Attention on fire: An attention-enhanced deep learning model for flame radiation prediction](../../05_diagnostics_radiation/02_radiation_soot/P68250a69d8/README.md) | 光学诊断、反演、烟炱与辐射 | provisional_q1_q2 | 待核对 |
| 2026 | [Multispectral infrared imaging and physics-informed neural network retrieval of soot and gas fields using an SVD-based surrogate radiative model](../../05_diagnostics_radiation/02_radiation_soot/P7eb5c4153b/README.md) | 光学诊断、反演、烟炱与辐射 | provisional_q1_q2 | 待核对 |
| 2026 | [Soot maturity evolution in a periodically-forced diffusion flame via neural network assisted inversion](../../05_diagnostics_radiation/02_radiation_soot/P55f5b0796b/README.md) | 光学诊断、反演、烟炱与辐射 | provisional_q1_q2 | 待核对 |
| 2024 | [Simultaneous soot parameters fields predictions accuracy improvements in laminar sooting flames from soot radiation measurements — a multi-task learning approach](../../05_diagnostics_radiation/02_radiation_soot/Pe4e9537482/README.md) | 光学诊断、反演、烟炱与辐射 | pending_jcr | 待核对 |
| 2024 | [Surrogate modeling for radiative heat transfer using physics-informed deep neural operator networks](../../05_diagnostics_radiation/02_radiation_soot/P64c5379f89/README.md) | 光学诊断、反演、烟炱与辐射 | provisional_q1_q2 | 待核对 |
| 2023 | [3-D soot temperature and volume fraction reconstruction of afterburner flame via deep learning algorithms](../../05_diagnostics_radiation/02_radiation_soot/P417d575996/README.md) | 光学诊断、反演、烟炱与辐射 | provisional_q1_q2 | 待核对 |
| 2023 | [A study on application of machine-learning on DBI soot diagnostics](../../05_diagnostics_radiation/02_radiation_soot/P22d5f2bce7/README.md) | 光学诊断、反演、烟炱与辐射 | provisional_q1_q2 | 待核对 |
| 2021 | [A machine learning based full-spectrum correlated k-distribution model for nonhomogeneous gas-soot mixtures](../../05_diagnostics_radiation/02_radiation_soot/Pe01c5a5aac/README.md) | 光学诊断、反演、烟炱与辐射 | pending_jcr | 已核对链接 |

## 烟炱生成及 PAH

| 年份 | 论文 | 方向 | 分区状态 | 代码 |
|---|---|---|---|---|
| 2026 | [Integrated neural network approach for autonomous sensitivity analysis and optimization of sectional soot kinetic modeling](../../05_diagnostics_radiation/03_soot_formation/Pe31f2bea9d/README.md) | 光学诊断、反演、烟炱与辐射 | provisional_q1_q2 | 已核对链接 |
| 2023 | [Exploring soot inception rate with stochastic modelling and machine learning](../../05_diagnostics_radiation/03_soot_formation/Pec757f1481/README.md) | 光学诊断、反演、烟炱与辐射 | provisional_q1_q2 | 待核对 |
| 2023 | [A machine learning framework to predict the aggregation of polycyclic aromatic compounds](../../05_diagnostics_radiation/03_soot_formation/P1e00a3c235/README.md) | 光学诊断、反演、烟炱与辐射 | provisional_q1_q2 | 待核对 |
| 2021 | [Machine learning-assisted soot temperature and volume fraction fields predictions in the ethylene laminar diffusion flames](../../05_diagnostics_radiation/03_soot_formation/Pbfb3185409/README.md) | 光学诊断、反演、烟炱与辐射 | pending_jcr | 待核对 |
