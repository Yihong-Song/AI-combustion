# BayeSAF: Emulation and design of sustainable alternative fuels via Bayesian inference and descriptors-based machine learning

Pfa457cec99 · 2026 · Fuel

作者：Jacopo Liberatori; Davide Cavalieri; Matteo Blandino; Mauro Valorani; Pietro Paolo Ciottoli

- DOI：[原文入口](https://doi.org/10.1016/j.fuel.2026.138835)
- 分类：氢氨燃料、着火与燃料性质预测 / 低碳燃料、着火与分子性质
- JCR：**二级来源报告 Q1/Q2，JCR 版本待官方核实**；报告最佳分区 Q1；版本未知；官方核实：否。
- 阅读深度：已核对元数据与上游 README，尚未完成全文精读。
- 完整期刊论文复现：**尚未验收**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../09_fuels_properties/README.md) · [全局地图](../../../00_literature_map/README.md)

分区线索：[二级来源](https://www.letpub.com/index.php?page=journalapp&view=detail&journalid=2950)。多类别期刊使用报告中的最佳类别作为候选信号，不能解释为所有类别均为 Q1。

## 研究问题

由目标性质反推可持续航空燃料的替代混合物组成，并表达组成的不确定性。

## 方法与代码所能确认的内容

README 明确链接 Fuel 论文，描述 Bayesian 混合物反演；其中 992 种化合物、7 类烃、11 项整体性质和 7 项温度相关性质为上游说明，本库未独立核验数据。

## 复现入口与依赖

先从固定提交 README 的示例、数据说明和环境文件确定性质预测与后验推断入口，再检查具体实验配置。

## 环境与数据

依赖、数据库和采样配置以固定提交为准；数据权利与代码使用条件须分别核查。

## 建议验证协议（本库设计）

将性质拟合误差、后验区间覆盖和混合物可辨识性分开评价；在未参与校准的燃料与温度上验证。

## 局限与当前状态

Prosperity Public License 3.0 限制商业使用，不是 OSI 开源；本库仅保留来源和固定链接，未运行或验证配方的实际燃烧性能。

## 代码溯源

- 仓库：[JacopoLib/BayeSAF](https://github.com/JacopoLib/BayeSAF)
- 固定提交：`d7e3b4b8f65085d9d7afa1e6c3b126f6e63edc30`
- 关系证据：`author_implementation_readme_explicit`；来自上游 README，不代表本库已做作者身份独立认证。
- 许可：Prosperity-3.0.0 (noncommercial; not OSI)；收纳状态：`link_only`。
- [代码包卡片](../../../code_packages/JacopoLib__BayeSAF/README.md)

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1016/j.fuel.2026.138835)；本轮整理日期 2026-11-12。完整元数据见同目录 `paper.json`。
