# Combustion machine learning: Principles, progress and prospects

Pb73c9cc517 · 2022 · Progress in Energy and Combustion Science

作者：Matthias Ihme; Wai Tong Chung; Aashwin Ananda Mishra

- DOI：[原文入口](https://doi.org/10.1016/j.pecs.2022.101010)
- 分类：综述、数据集与共性方法 / 综述与开放数据
- JCR：**二级来源报告 Q1/Q2，JCR 版本待官方核实**；报告最佳分区 Q1；版本未知；官方核实：否。
- 阅读深度：已核对元数据与上游 README，尚未完成全文精读。
- 完整期刊论文复现：**尚未验收**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../10_reviews_methods/README.md) · [全局地图](../../../00_literature_map/README.md)

分区线索：[二级来源](https://www.letpub.com/journal-selector/journal/6930)。多类别期刊使用报告中的最佳类别作为候选信号，不能解释为所有类别均为 Q1。

## 研究问题

为理解燃烧机器学习的主要范式提供可阅读的入门实现。

## 方法与代码所能确认的内容

README 明确要求引用本综述，提供监督、无监督学习教程与 Q-learning 接口。教程服务理解方法，不构成综述中所有论文的复现。

## 复现入口与依赖

按上游目录逐个读取监督/无监督 notebook 与强化学习接口，先核对输入特征和示例数据。

## 环境与数据

各教程导入与环境需要单独核对；没有统一依赖锁文件的地方保留待办。

## 建议验证协议（本库设计）

先说明学习任务、切分、基线和指标，再用它作为阅读具体燃烧论文的概念支撑。

## 局限与当前状态

未定位许可文件，链接收纳；不把通用课堂例子计为燃烧 Q1 论文复现。

## 代码溯源

- 仓库：[IhmeGroup/CombML_Tutorials](https://github.com/IhmeGroup/CombML_Tutorials)
- 固定提交：`f00cca1d03dd3fa115ab0ee3d6644a2710e126c0`
- 关系证据：`author_supporting_tutorial_readme_explicit`；来自上游 README，不代表本库已做作者身份独立认证。
- 许可：not_located；收纳状态：`link_only`。
- [代码包卡片](../../../code_packages/IhmeGroup__CombML_Tutorials/README.md)

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1016/j.pecs.2022.101010)；本轮整理日期 2026-11-12。完整元数据见同目录 `paper.json`。
