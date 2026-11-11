# BLASTNet: A call for community-involved big data in combustion machine learning

P42e1959567 · 2022 · Applications in Energy and Combustion Science

作者：Wai Tong Chung; Ki Sung Jung; Jacqueline H. Chen; Matthias Ihme

- DOI：[原文入口](https://doi.org/10.1016/j.jaecs.2022.100087)
- 分类：综述、数据集与共性方法 / 综述与开放数据
- JCR：**JCR 分区待核实**；报告最佳分区 Q1；版本未知；官方核实：否。
- 阅读深度：已核对元数据与上游 README，尚未完成全文精读。
- 论文原始指标复现：**未执行**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../10_reviews_methods/README.md) · [全局地图](../../../00_literature_map/README.md)

分区线索：[二级来源](https://www.letpub.com/index.php?page=journalapp&view=detail&journalid=30136)。多类别期刊使用报告中的最佳类别作为候选信号，不能解释为所有类别均为 Q1。

## 研究问题

让研究者能读取、理解并利用 BLASTNet 的三维可压缩反应流数据。

## 方法与代码所能确认的内容

BLASTNet 教程 README 明确要求引用本文，提供 Kaggle notebook 入口；这是数据教程和使用支撑，不是某个目标模型的完整复现。

## 复现入口与依赖

按上游 Open on Kaggle 入口定位 notebook，检查数据集版本后才运行；也可从本库 BLASTNet Python 客户端卡定位数据访问工具。

## 环境与数据

Kaggle 运行环境、对应 BLASTNet 数据与各自许可；未登录运行，也未下载大规模 DNS 数据。

## 建议验证协议（本库设计）

记录数据版本、物理单位、网格和时间采样；模型评估按独立模拟或时间块留出，不能随机拆相邻体素。

## 局限与当前状态

教程未定位明确源码许可，仅保留固定链接。该期刊的二级分区表存在疑点，分区继续待核实。

## 代码溯源

- 仓库：[blastnet/kaggle_tutorials](https://github.com/blastnet/kaggle_tutorials)
- 固定提交：`1618a463475a82f49674f6fd2614672b173f80e5`
- 关系证据：`author_supporting_tutorial_readme_explicit`；来自上游 README，不代表本库已做作者身份独立认证。
- 许可：not_located；收纳状态：`link_only`。
- [代码包卡片](../../../code_packages/blastnet__kaggle_tutorials/README.md)

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1016/j.jaecs.2022.100087)；本轮整理日期 2026-11-11。完整元数据见同目录 `paper.json`。
