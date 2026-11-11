# Active learning-based exploration of the catalytic pyrolysis of plastic waste

P92264f9a97 · 2022 · Fuel

作者：Yannick Ureel; Maarten R. Dobbelaere; Oğuzhan Akin; Robin John Varghese; César G. Pernalete; Joris W. Thybaut; Kevin M. Van Geem

- DOI：[原文入口](https://doi.org/10.1016/j.fuel.2022.125340)
- 分类：固体燃料、热解与火灾安全 / 生物质、煤、热解与火灾
- JCR：**二级来源报告 Q1/Q2，JCR 版本待官方核实**；报告最佳分区 Q1；版本未知；官方核实：否。
- 阅读深度：已核对元数据与上游 README，尚未完成全文精读。
- 论文原始指标复现：**未执行**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../08_solid_fuels_fire/README.md) · [全局地图](../../../00_literature_map/README.md)

分区线索：[二级来源](https://www.letpub.com/index.php?page=journalapp&view=detail&journalid=2950)。多类别期刊使用报告中的最佳类别作为候选信号，不能解释为所有类别均为 Q1。

## 研究问题

用主动学习选择塑料催化热解实验，减少寻找合适工况所需的实验数量。

## 方法与代码所能确认的内容

上游明确链接 Fuel 论文，提供高斯过程与实验选点流程。建议的下一个实验条件不等于已完成物理实验验证。

## 复现入口与依赖

GandALF.py 与 GandAlF.csv；先核对数据列、目标函数方向、采集函数和初始样本。

## 环境与数据

README 给出 Python 3.6+、NumPy、SciPy、scikit-learn、pandas、GPy 和 GPyOpt；旧依赖需单独环境。

## 建议验证协议（本库设计）

用相同初始样本和实验预算比较随机选点、网格/专家策略与主动学习，跨种子报告最优目标随实验次数的变化。

## 局限与当前状态

MIT 许可已定位；尚未运行。基于已有表格的回放与真实在线选点应分别报告，不能将热解产物优化直接等同低排放燃烧。

## 代码溯源

- 仓库：[yureel/GandALF](https://github.com/yureel/GandALF)
- 固定提交：`8acf416139af0247da1080dcfbb930826ccb4125`
- 关系证据：`author_implementation_readme_explicit`；来自上游 README，不代表本库已做作者身份独立认证。
- 许可：MIT；收纳状态：`source_archive_collected`。
- [代码包卡片](../../../code_packages/yureel__GandALF/README.md)

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1016/j.fuel.2022.125340)；本轮整理日期 2026-11-11。完整元数据见同目录 `paper.json`。
