# A machine learning method to predict rate constants for various reactions in combustion kinetic models

P2696c5ed02 · 2024 · Combustion and Flame

作者：Ning Li; Sanket Girhe; Mingzhi Zhang; Bingjie Chen; Yingjia Zhang; Shenghua Liu; Heinz Pitsch

- DOI：[原文入口](https://doi.org/10.1016/j.combustflame.2024.113375)
- 分类：化学动力学代理、缩减与机理发现 / 代理与缩减
- JCR：**二级来源报告 Q1/Q2，JCR 版本待官方核实**；报告最佳分区 Q1；版本未知；官方核实：否。
- 阅读深度：已核对元数据与上游 README，尚未完成全文精读。
- 论文原始指标复现：**未执行**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../01_chemistry_kinetics/README.md) · [全局地图](../../../00_literature_map/README.md)

分区线索：[二级来源](https://www.letpub.com/index.php?page=journalapp&view=detail&journalid=1901)。多类别期刊使用报告中的最佳类别作为候选信号，不能解释为所有类别均为 Q1。

## 研究问题

利用反应表示学习预测燃烧反应速率常数。

## 方法与代码所能确认的内容

README 标题与论文相符，提供反应指纹生成与微调入口。这里的论文—仓库关系来自标题匹配，强度低于作者明确 DOI 声明。

## 复现入口与依赖

rxnfp_schwaller/generate_rxnfp.py 和 fine_tune.py。

## 环境与数据

README 使用 Python 3.7；反应指纹相关依赖需隔离，避免直接混入当前基线环境。

## 建议验证协议（本库设计）

按反应家族和化学结构留出，而非随机拆分相似反应；速率常数需明确温度、压力、单位及对数底。

## 局限与当前状态

未发现许可，链接收纳。预测速率常数还需经过机理级点火/火焰速度验证。

## 代码溯源

- 仓库：[edwardning/ML_RateConstants](https://github.com/edwardning/ML_RateConstants)
- 固定提交：`ce8d0cdd6fc7dd8ff9018e80b72eaf089b7deaba`
- 关系证据：`title_match_repository_readme`；来自上游 README，不代表本库已做作者身份独立认证。
- 许可：not_located；收纳状态：`link_only`。
- [代码包卡片](../../../code_packages/edwardning__ML_RateConstants/README.md)

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1016/j.combustflame.2024.113375)；本轮整理日期 2026-11-11。完整元数据见同目录 `paper.json`。
