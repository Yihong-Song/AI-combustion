# Data-driven discovery of heat release rate markers for premixed NH3/H2/air flames using physics-informed machine learning

Pd9de613208 · 2022 · Fuel

作者：Cheng Chi; Srijith Sreekumar; Dominique Thévenin

- DOI：[原文入口](https://doi.org/10.1016/j.fuel.2022.125508)
- 分类：光学诊断、反演、烟炱与辐射 / 光谱、图像与层析反演
- JCR：**二级来源报告 Q1/Q2，JCR 版本待官方核实**；报告最佳分区 Q1；版本未知；官方核实：否。
- 阅读深度：已核对元数据与上游 README，尚未完成全文精读。
- 完整期刊论文复现：**尚未验收**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../05_diagnostics_radiation/README.md) · [全局地图](../../../00_literature_map/README.md)

分区线索：[二级来源](https://www.letpub.com/index.php?page=journalapp&view=detail&journalid=2950)。多类别期刊使用报告中的最佳类别作为候选信号，不能解释为所有类别均为 Q1。

## 研究问题

寻找 NH3/H2/air 预混火焰中可用于推断热释放率的组分标记。

## 方法与代码所能确认的内容

README 明确给出本文 DOI，说明以物理信息机器学习建立组分标记与热释放率的非线性关系。不能把这种物理约束回归自动等同求解 PDE 的 PINN。

## 复现入口与依赖

根目录含 Data_preprocessing、PIML_mass_fraction、PIML_molar_fraction、Gradient_output_to_input、Sensitivity_analysis、Evaluation 及重构误差分析目录。

## 环境与数据

分别核对质量/摩尔分数输入、数据预处理和模型框架版本；README 未提供完整的一键运行环境。

## 建议验证协议（本库设计）

按温度、配比和火焰工况留出，比较源项幅值、峰位和积分热释放；加入测量噪声和可实际观测组分约束。

## 局限与当前状态

未定位许可，仅固定链接；未执行。基于机理生成数据的相关性不能直接证明实验测量的标记鲁棒性。

## 代码溯源

- 仓库：[SrijithSreekumar/Heat_Realease_Rate_intergrated_with_physics_constrained_neural_network](https://github.com/SrijithSreekumar/Heat_Realease_Rate_intergrated_with_physics_constrained_neural_network)
- 固定提交：`6ff2c190cce651be71999b80ee70ff37c645631e`
- 关系证据：`author_implementation_readme_explicit`；来自上游 README，不代表本库已做作者身份独立认证。
- 许可：not_located；收纳状态：`link_only`。
- [代码包卡片](../../../code_packages/SrijithSreekumar__Heat_Realease_Rate_intergrated_with_physics_constrained_neural_network/README.md)

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1016/j.fuel.2022.125508)；本轮整理日期 2026-11-12。完整元数据见同目录 `paper.json`。
