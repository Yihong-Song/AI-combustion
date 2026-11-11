# 氢氨燃料、着火与燃料性质预测

从分子结构或工况预测着火、火焰速度和燃料性质，为低碳燃料选择提供依据。

本目录含 42 条候选。分区与全文状态逐篇标注；自动分类以研究目标优先，交叉方法可在总库检索。

[返回首页](../README.md) · [全局地图](../00_literature_map/README.md) · [方法与范围](../docs/METHODOLOGY.md)

## 核心问题

目标是微观分子性质、混合燃料指标还是工况相关燃烧响应？相同模型名称不意味着相同输入或适用范围。

## 方法演进与比较

QSPR/分子指纹、GNN、随机森林、集成学习、物理引导特征与迁移学习。氢/氨领域需特别关注压力和掺混比例覆盖。

## 数据与物理定义

实验/机理计算点火延迟、层流火焰速度、十六烷值/辛烷值、物性与分子结构。实验标签和模拟标签应分开标记。

## 怎样判断模型有效

物理单位 MAE 与相对/对数误差、scaffold 外推、置信区间、极端工况失败；不同点火定义不能混合比较。

## 如何避免数据泄漏

整分子/化学家族/燃料组合留出；工况预测按温压区间分组。先去除相同分子的别名与重复数据。

## 主要局限与选题问题

小数据、异质测量、对氢/氨燃料的命名混淆、模拟机理自身偏差。图模型加入物理信息仍可能无法外推至未见化学家族。

## 建议阅读和实践路径

B01 建立可执行工况代理，再阅读 CNpred 的分子图与数据质量问题，最后分析氢氨新工况的分布外测试。

## 细分类与论文索引

分区栏为二级来源线索；Q? 为待核实。代码 ✓ 仅表示论文链接已核对，不表示执行成功。

### [低碳燃料、着火与分子性质](01_hydrogen_ammonia_properties/README.md)（42）

| 年份 | 论文 | 分区线索 | 代码 |
|---|---|---|---|
| 2026 | [Transfer learning for cetane number prediction in fuel mixtures with explainable interaction analysis](01_hydrogen_ammonia_properties/P2e07ea6c6c/README.md) | Q1 | 待核对 |
| 2026 | [A structured framework for predicting sustainable aviation fuel properties using liquid-phase FTIR and machine learning](01_hydrogen_ammonia_properties/P075228d526/README.md) | Q1 | 待核对 |
| 2026 | [A GWO-GA-EL neural network approach for predicting the laminar burning velocity of RP-3 aviation kerosene and its blends](01_hydrogen_ammonia_properties/Pb1beec5415/README.md) | Q1 | 待核对 |
| 2026 | [BayeSAF: Emulation and design of sustainable alternative fuels via Bayesian inference and descriptors-based machine learning](01_hydrogen_ammonia_properties/Pfa457cec99/README.md) | Q1 | ✓ |
| 2026 | [Data-Driven Modeling of Laminar Flame Speed in Ammonia–Oxygenated Fuel Blends Using Machine Learning](01_hydrogen_ammonia_properties/P5b20f7bd23/README.md) | Q1 | 待核对 |
| 2025 | [Predictions of heat of combustion and formation by interpretable machine learning algorithms](01_hydrogen_ammonia_properties/P464116e6c7/README.md) | Q1 | 待核对 |
| 2025 | [Non-equilibrium exergy analysis and artificial neural network prediction for ammonia-diesel dual-fuel combustion: Strategies for minimizing exergy loss](01_hydrogen_ammonia_properties/Pfbb92a1349/README.md) | Q1 | 待核对 |
| 2025 | [In silico estimation of density, vapor pressure, distillation curve, and octane numbers of gasoline fuels using machine learning](01_hydrogen_ammonia_properties/Pae77b13ef2/README.md) | Q1 | 待核对 |
| 2025 | [Hybrid physics-machine learning model for multispecies and temperature inference from FTIR spectra: Application to ammonia flames](01_hydrogen_ammonia_properties/Pfff37b2d22/README.md) | Q1 | 待核对 |
| 2025 | [Advancing Sustainable Aviation Fuel Design: Machine Learning for High-Energy-Density Liquid Polycyclic Hydrocarbons](01_hydrogen_ammonia_properties/Pca19045ded/README.md) | Q1 | ✓ |
| 2024 | [Learning to predict sustainable aviation fuel properties: A deep uncertainty quantification viewpoint](01_hydrogen_ammonia_properties/P707f25a3c5/README.md) | Q1 | 待核对 |
| 2024 | [Prediction of HHV of fuel by Machine learning Algorithm: Interpretability analysis using Shapley Additive Explanations (SHAP)](01_hydrogen_ammonia_properties/P2c753c4445/README.md) | Q1 | 待核对 |
| 2024 | [Advancing C5+ hydrocarbons fuels production: An interpretable machine learning framework for Co-catalyzed syngas conversion](01_hydrogen_ammonia_properties/P41925c935a/README.md) | Q1 | 待核对 |
| 2024 | [Prediction of hydrocarbons ignition performances using machine learning modeling](01_hydrogen_ammonia_properties/Pd2aa5fcd18/README.md) | Q1 | 待核对 |
| 2024 | [Combustion condition predictions for C2-C4 alkane and alkene fuels via machine learning methods](01_hydrogen_ammonia_properties/P2199c41d85/README.md) | Q1 | 待核对 |
| 2024 | [Towards a machine learning model to predict the laminar flame speed of fuel blends and vented gases in lithium-ion batteries](01_hydrogen_ammonia_properties/P841baac9f9/README.md) | Q1 | 待核对 |
| 2024 | [Ensemble predictions of laser ignition with a hybrid stochastic physics-embedded deep-learning framework](01_hydrogen_ammonia_properties/P6d766fee4f/README.md) | Q1 | 待核对 |
| 2023 | [Large eddy simulations of ammonia-hydrogen jet flames at elevated pressure using principal component analysis and deep neural networks](01_hydrogen_ammonia_properties/P8fd896f3f6/README.md) | Q1 | 待核对 |
| 2023 | [Laminar Flame Speed modeling for Low Carbon Fuels using methods of Machine Learning](01_hydrogen_ammonia_properties/P33f1c2fa8c/README.md) | Q1 | 待核对 |
| 2023 | [Eco-friendly de-lignified and raw Celosia argentea waste solid biofuel: Comparative studies and machine learning modelling](01_hydrogen_ammonia_properties/Pcbeaff8e58/README.md) | Q1 | 待核对 |
| 2023 | [Assessment of machine learning algorithms for predicting autoignition and ignition delay time in microscale supercritical water oxidation process](01_hydrogen_ammonia_properties/Pad5ba5d0c7/README.md) | Q1 | 待核对 |
| 2023 | [Predicting octane number from species profiles: A deep learning model](01_hydrogen_ammonia_properties/P49dfb5b4bf/README.md) | Q1 | 待核对 |
| 2022 | [Prediction of ignition delay times of Jet A-1/hydrogen fuel mixture using machine learning](01_hydrogen_ammonia_properties/P8cbbfe9d39/README.md) | Q1 | 待核对 |
| 2022 | [Investigation on the ignition delay prediction model of multi-component surrogates based on back propagation (BP) neural network](01_hydrogen_ammonia_properties/Pff2455c140/README.md) | Q1 | 待核对 |
| 2022 | [Synergistic effect analysis on sooting tendency based on soot-specialized artificial neural network algorithm with experimental and numerical validation](01_hydrogen_ammonia_properties/P0d7a73aa81/README.md) | Q1 | 待核对 |
| 2022 | [Molecular graph-based deep learning method for predicting multiple physical properties of alternative fuel components](01_hydrogen_ammonia_properties/P12ef9fa7b1/README.md) | Q1 | 待核对 |
| 2022 | [Numerical study on the blending of excellent anti-knock fuel using artificial neural network](01_hydrogen_ammonia_properties/P2e5a83b5c8/README.md) | Q1 | 待核对 |
| 2022 | [Kinematic viscosity estimation of fuel oil with comparison of machine learning methods](01_hydrogen_ammonia_properties/P6aab98682c/README.md) | Q1 | 待核对 |
| 2022 | [A comprehensive neural network model for predicting flash point of oxygenated fuels using a functional group approach](01_hydrogen_ammonia_properties/P30ad2edc85/README.md) | Q1 | 待核对 |
| 2022 | [A machine learning model for predicting threshold sooting index (TSI) of fuels containing alcohols and ethers](01_hydrogen_ammonia_properties/P525b1d160f/README.md) | Q1 | 待核对 |
| 2022 | [Ensemble learning directed classification and regression of hydrocarbon fuels](01_hydrogen_ammonia_properties/P825644bebc/README.md) | Q1 | 待核对 |
| 2022 | [Experimental analysis and data-driven machine learning modelling of the minimum ignition temperature (MIT) of aluminium dust](01_hydrogen_ammonia_properties/P8ed80fd8fa/README.md) | Q1 | 待核对 |
| 2021 | [Exploring the fuel structure dependence of laminar burning velocity: A machine learning based group contribution approach](01_hydrogen_ammonia_properties/P72c0e610a0/README.md) | Q1 | 待核对 |
| 2021 | [Prediction of Gasoline Blend Ignition Characteristics Using Machine Learning Models](01_hydrogen_ammonia_properties/Pf4aa58d981/README.md) | Q1 | 待核对 |
| 2020 | [A machine learning framework for drop-in volume swell characteristics of sustainable aviation fuel](01_hydrogen_ammonia_properties/P3d7d8226c2/README.md) | Q1 | 待核对 |
| 2020 | [Machine learning regression based group contribution method for cetane and octane numbers prediction of pure fuel compounds and mixtures](01_hydrogen_ammonia_properties/P33e576ee86/README.md) | Q1 | 待核对 |
| 2020 | [A new method of diesel fuel brands identification: SMOTE oversampling combined with XGBoost ensemble learning](01_hydrogen_ammonia_properties/Pa38f4b66be/README.md) | Q1 | 待核对 |
| 2019 | [Machine learning-assisted early ignition prediction in a complex flow](01_hydrogen_ammonia_properties/P1f4503d807/README.md) | Q1 | 待核对 |
| 2019 | [Viscosities of some fatty acid esters and biodiesel fuels from a rough hard-sphere-chain model and artificial neural network](01_hydrogen_ammonia_properties/P93d8a75bae/README.md) | Q1 | 待核对 |
| 2019 | [Predicting sooting tendencies of oxygenated hydrocarbon fuels with machine learning algorithms](01_hydrogen_ammonia_properties/P645288cebf/README.md) | Q1 | 待核对 |
| 2019 | [Laminar burning velocity of hydrogen and carbon-monoxide enriched natural gas (HyCONG): An experimental and artificial neural network study](01_hydrogen_ammonia_properties/P20daa66f2a/README.md) | Q1 | 待核对 |
| 2019 | [Experimental study of premixed hydrogen enriched natural gas under an alternating-current (AC) electric field and application of support vector machine (SVM) on electric field assisted combustion](01_hydrogen_ammonia_properties/P4f8d094add/README.md) | Q1 | 待核对 |
