# A machine learning based full-spectrum correlated k-distribution model for nonhomogeneous gas-soot mixtures

Pe01c5a5aac · 2021 · Journal of Quantitative Spectroscopy and Radiative Transfer

作者：Ya Zhou; Chaojun Wang; Tao Ren; Changying Zhao

- DOI：[原文入口](https://doi.org/10.1016/j.jqsrt.2021.107628)
- 分类：光学诊断、反演、烟炱与辐射 / 辐射与烟炱辐射诊断
- JCR：**JCR 分区待核实**；报告最佳分区 未知；版本未知；官方核实：否。
- 阅读深度：已核对元数据与上游 README，尚未完成全文精读。
- 完整期刊论文复现：**尚未验收**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../05_diagnostics_radiation/README.md) · [全局地图](../../../00_literature_map/README.md)

## 研究问题

用紧凑模型预测燃烧气体与烟炱混合物的全谱相关 k 分布。

## 方法与代码所能确认的内容

README 明确引用本文，说明将机器学习模型导出为可独立调用的 Fortran 模块；输入物理状态在 Main.f90 修改，输出 32 个求积点的 k 分布。

## 复现入口与依赖

Main.f90 → make → ./rhs → python plot.py；先核对温度、压力、组分和烟炱体积分数的单位及范围。

## 环境与数据

GNU Fortran、make 与 Python 绘图依赖；训练表格和原始光谱数据库不因推理模块公开而自动齐备。

## 建议验证协议（本库设计）

先对同状态的 FSCK 表格比较 k 分布，再比较热流/辐射源项及非均匀气体–烟炱火焰；不能把压缩率当作辐射精度。

## 局限与当前状态

MIT；README 也列 2020 前作作为背景，不将当前气体–烟炱模块当作前作完整实现。未运行。

## 代码溯源

- 仓库：[ZY-LHY/Machine_learning_based_FSCK_model_soot](https://github.com/ZY-LHY/Machine_learning_based_FSCK_model_soot)
- 固定提交：`12fea0f160bcb2f4e32a586ae66ffe3b7b71775a`
- 关系证据：`author_implementation_readme_explicit`；来自上游 README，不代表本库已做作者身份独立认证。
- 许可：MIT；收纳状态：`partial_source_snapshot_collected`。
- [代码包卡片](../../../code_packages/ZY-LHY__Machine_learning_based_FSCK_model_soot/README.md)

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1016/j.jqsrt.2021.107628)；本轮整理日期 2026-11-12。完整元数据见同目录 `paper.json`。
