# A multi-scale sampling method for accurate and robust deep neural network to predict combustion chemical kinetics

P88f8a69095 · 2022 · Combustion and Flame

作者：Tianhan Zhang; Yuxiao Yi; Yifan Xu; Zhi X. Chen; Yaoyu Zhang; Weinan E; Zhi-Qin John Xu

- DOI：[原文入口](https://doi.org/10.1016/j.combustflame.2022.112319)
- 分类：化学动力学代理、缩减与机理发现 / 代理与缩减
- JCR：**二级来源报告 Q1/Q2，JCR 版本待官方核实**；报告最佳分区 Q1；版本未知；官方核实：否。
- 阅读深度：已核对元数据与上游 README，尚未完成全文精读。
- 论文原始指标复现：**未执行**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../01_chemistry_kinetics/README.md) · [全局地图](../../../00_literature_map/README.md)

分区线索：[二级来源](https://www.letpub.com/index.php?page=journalapp&view=detail&journalid=1901)。多类别期刊使用报告中的最佳类别作为候选信号，不能解释为所有类别均为 Q1。

## 研究问题

通过多尺度采样提升详细化学神经网络代理对热化学状态空间的覆盖。

## 方法与代码所能确认的内容

README 提供 Python 和 Fortran 推理实现、自燃测试及 DME 数据说明。DME 输入输出各为 350 万 × 41，输出对应 1e-6 s 时间推进；这里记录的是作者 README 的说明，未实测数据完整性。

## 复现入口与依赖

ZeroDAutognition.py、modelclass.py、FortranDNN_Module.F、Chem/、Model/。

## 环境与数据

需逐脚本检查 Python/Fortran、Cantera、网络框架和模型文件；大数据不自动下载。

## 建议验证协议（本库设计）

比较单步误差和多步滚动的点火延迟、组分守恒；用未参与采样的完整温压当量比条件测试。

## 局限与当前状态

与 2025 年守恒论文共用一个仓库，包数只计一次。当前提交同时包含多篇工作的演化内容，不能自动视为 2022 原始版本。

## 代码溯源

- 仓库：[tianhanz/DNN-Models-for-Chemical-Kinetics](https://github.com/tianhanz/DNN-Models-for-Chemical-Kinetics)
- 固定提交：`bc07e5a210ba357b8a5350b460a751a68a002174`
- 关系证据：`author_implementation_readme_explicit`；来自上游 README，不代表本库已做作者身份独立认证。
- 许可：Apache-2.0；收纳状态：`partial_source_snapshot_collected`。
- [代码包卡片](../../../code_packages/tianhanz__DNN-Models-for-Chemical-Kinetics/README.md)

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1016/j.combustflame.2022.112319)；本轮整理日期 2026-11-11。完整元数据见同目录 `paper.json`。
