# Adaptive global pathway selection using artificial neural networks: A-priori study

P4a2b5d4efc · 2022 · Combustion and Flame

作者：Rohit Mishra; Aaron Nelson; Dorrin Jarrahbashi

- DOI：[原文入口](https://doi.org/10.1016/j.combustflame.2022.112279)
- 分类：化学动力学代理、缩减与机理发现 / 机理发现与参数校准
- JCR：**二级来源报告 Q1/Q2，JCR 版本待官方核实**；报告最佳分区 Q1；版本未知；官方核实：否。
- 阅读深度：已核对元数据与上游 README，尚未完成全文精读。
- 完整期刊论文复现：**尚未验收**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../01_chemistry_kinetics/README.md) · [全局地图](../../../00_literature_map/README.md)

分区线索：[二级来源](https://www.letpub.com/index.php?page=journalapp&view=detail&journalid=1901)。多类别期刊使用报告中的最佳类别作为候选信号，不能解释为所有类别均为 Q1。

## 研究问题

以 ANN 近似全局路径选择结果，实现随热化学状态变化的动态机理缩减。

## 方法与代码所能确认的内容

先在零维自燃轨迹上运行自适应 GPS 生成标签，再训练物种选择网络。README 默认两隐层宽度 16 和 8，训练后输出 .h5，并提供转冻结图的路线。

## 复现入口与依赖

tests/ 与 src/slgps/mech_train.py；converth5ToPb.ipynb 面向 OpenFOAM 集成。运行前检查当前目录与相对机理路径。

## 环境与数据

Cantera 3、TensorFlow 2、networkx、pandas、scikit-learn、NumPy。旧 h5 模型与当前 Keras 之间可能需要版本适配。

## 建议验证协议（本库设计）

比较缩减物种数、点火延迟、重要组分和总体时间；物种选择准确率不足以证明动力学准确。需按整条轨迹留出。

## 局限与当前状态

论文标题明确为 a priori。不能仅凭分类或离线测试声称任意 CFD 中已验证；继承 GPS 的第三方许可亦需保留。

## 代码溯源

- 仓库：[ctftamu/SL-GPS](https://github.com/ctftamu/SL-GPS)
- 固定提交：`647aee6b92ff45c9a9b0d57ea3ed49d272ec4083`
- 关系证据：`author_implementation_readme_explicit`；来自上游 README，不代表本库已做作者身份独立认证。
- 许可：GPL-3.0 (inspect upstream terms)；收纳状态：`partial_source_snapshot_collected`。
- [代码包卡片](../../../code_packages/ctftamu__SL-GPS/README.md)

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1016/j.combustflame.2022.112279)；本轮整理日期 2026-11-12。完整元数据见同目录 `paper.json`。
