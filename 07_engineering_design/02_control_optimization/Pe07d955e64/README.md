# Co-optimized machine-learned manifold models for large eddy simulation of turbulent combustion

Pe07d955e64 · 2022 · Combustion and Flame

作者：Bruce A. Perry; Marc T. Henry de Frahan; Shashank Yellapantula

- DOI：[原文入口](https://doi.org/10.1016/j.combustflame.2022.112286)
- 分类：发动机、燃烧器与复杂推进系统设计 / 控制与多目标设计
- JCR：**二级来源报告 Q1/Q2，JCR 版本待官方核实**；报告最佳分区 Q1；版本未知；官方核实：否。
- 阅读深度：已核对元数据与上游 README，尚未完成全文精读。
- 论文原始指标复现：**未执行**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../07_engineering_design/README.md) · [全局地图](../../../00_literature_map/README.md)

分区线索：[二级来源](https://www.letpub.com/index.php?page=journalapp&view=detail&journalid=1901)。多类别期刊使用报告中的最佳类别作为候选信号，不能解释为所有类别均为 Q1。

## 研究问题

将热化学状态压缩到低维流形，并联合优化流形表示和输出重构，用于湍流燃烧 LES。

## 方法与代码所能确认的内容

README 提供 strained premixed flame、autoignition、premixed flame 三条数据—训练—制图路线，且预期对接 Pele 求解器。流形重构误差与 CFD 耦合稳定性属于不同层次证据。

## 复现入口与依赖

get_strained_data.py → gen_trn_tst_data.py → train_models_strained_flames_raw.py → plot_strained.py。上游说明首个示例已附部分预处理数据。

## 环境与数据

Python、Cantera、PyTorch、pandas、NumPy、scikit-learn、Matplotlib、SHERPA；DRM19 与 HyChem Jet-A 机理需另取。检查 use_GPU 和旧机理格式兼容。

## 建议验证协议（本库设计）

按应变率/压力/燃料划分训练测试，比较组分、温度、流形源项及完整 LES 的统计量；与 PCA 和传统 flamelet 表比较内存与推理成本。

## 局限与当前状态

README 对部分源项损失的正确性亦保留说明，使用时需审查具体提交。仓库收纳不等于 Pele 耦合结果已复现。

## 代码溯源

- 仓库：[NatLabRockies/cmlm](https://github.com/NatLabRockies/cmlm)
- 固定提交：`6b3f1da4065a96bdff30cd42638e43600c8dceb7`
- 关系证据：`author_implementation_readme_explicit`；来自上游 README，不代表本库已做作者身份独立认证。
- 许可：BSD-3-Clause；收纳状态：`partial_source_snapshot_collected`。
- [代码包卡片](../../../code_packages/NatLabRockies__cmlm/README.md)

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1016/j.combustflame.2022.112286)；本轮整理日期 2026-11-11。完整元数据见同目录 `paper.json`。
