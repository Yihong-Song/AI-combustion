# FlamePINN-1D: Physics-informed neural networks to solve forward and inverse problems of 1D laminar flames

P1cf521f2c6 · 2025 · Combustion and Flame

作者：Jiahao Wu; Su Zhang; Yuxin Wu; Guihua Zhang; Xin Li; Hai Zhang

- DOI：[原文入口](https://doi.org/10.1016/j.combustflame.2025.113964)
- 分类：物理信息学习与可微燃烧求解 / 正逆问题与可微求解
- JCR：**二级来源报告 Q1/Q2，JCR 版本待官方核实**；报告最佳分区 Q1；版本未知；官方核实：否。
- 阅读深度：已核对元数据与上游 README，尚未完成全文精读。
- 论文原始指标复现：**未执行**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../06_physics_informed/README.md) · [全局地图](../../../00_literature_map/README.md)

分区线索：[二级来源](https://www.letpub.com/index.php?page=journalapp&view=detail&journalid=1901)。多类别期刊使用报告中的最佳类别作为候选信号，不能解释为所有类别均为 Q1。

## 研究问题

用物理信息神经网络求解一维层流火焰正问题和逆问题。阅读时应区分简化化学与详细化学，以及自由传播与对冲火焰的边界条件。

## 方法与代码所能确认的内容

上游 README 明确列出三组算例：简化自由传播预混火焰、详细自由传播预混火焰、详细对冲预混火焰。PINN 将控制方程残差和边界约束引入训练；具体损失权重、无量纲化与逆参数需逐项对照论文和脚本。

## 复现入口与依赖

先从 Case 1 开始，核对 1S_CH4_MP.yaml；再推进至 Case 2 和 Case 3。使用固定提交中的实际目录名。

## 环境与数据

需 Cantera 和上游各算例的神经网络依赖；README 未提供统一完整环境锁。机理应通过本地数据路径加载，避免覆盖系统安装中的 Cantera 数据。

## 建议验证协议（本库设计）

先用同机理 Cantera 一维火焰作参考，比较温度/组分剖面、层流火焰速度、边界误差；逆问题还须报告参数误差与观测噪声敏感性。

## 局限与当前状态

已核实论文—仓库关系、提交和 MIT 许可，尚未执行原始训练。不能把下游 Bratu 示例当作本论文复现。

## 代码溯源

- 仓库：[CAME-THU/FlamePINN-1D](https://github.com/CAME-THU/FlamePINN-1D)
- 固定提交：`f7c0c0c3dc9b75d41d0bb090d265650a67999c45`
- 关系证据：`author_implementation_readme_explicit`；来自上游 README，不代表本库已做作者身份独立认证。
- 许可：MIT；收纳状态：`partial_source_snapshot_collected`。
- [代码包卡片](../../../code_packages/CAME-THU__FlamePINN-1D/README.md)

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1016/j.combustflame.2025.113964)；本轮整理日期 2026-11-11。完整元数据见同目录 `paper.json`。
