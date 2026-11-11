# Data-based instantaneous conditional progress variable dissipation rate modeling for turbulent premixed combustion

P2fc75bd437 · 2024 · Combustion and Flame

作者：Cristian E. Lacey; Katie VanderKam; Sankaran Sundaresan; Michael E. Mueller

- DOI：[原文入口](https://doi.org/10.1016/j.combustflame.2023.113139)
- 分类：湍流燃烧闭合与流形模型 / 闭合、PDF 与热化学流形
- JCR：**二级来源报告 Q1/Q2，JCR 版本待官方核实**；报告最佳分区 Q1；版本未知；官方核实：否。
- 阅读深度：已核对元数据与上游 README，尚未完成全文精读。
- 完整期刊论文复现：**尚未验收**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../02_turbulence_closure/README.md) · [全局地图](../../../00_literature_map/README.md)

分区线索：[二级来源](https://www.letpub.com/index.php?page=journalapp&view=detail&journalid=1901)。多类别期刊使用报告中的最佳类别作为候选信号，不能解释为所有类别均为 Q1。

## 研究问题

在预混湍流流形模型中预测瞬时条件进度变量耗散率剖面。

## 方法与代码所能确认的内容

README 明确给出作者、题名、Combustion and Flame 卷和文章号，模型输出进度变量空间中 32 点归一化耗散率剖面；输入为滤波进度变量、方差、梯度、应变和其他局部量。

## 复现入口与依赖

先从 tf-gpu.yml 建立旧环境；依 README 的输入列名对齐特征，核对归一化参考点 Lambda_ref=0.5 与模型输出变换。

## 环境与数据

Python、TensorFlow 2.4.1 和固定 Anaconda 环境；训练 DNS 数据、模型文件与特征生成需分别清点。

## 建议验证协议（本库设计）

跨滤波尺度、湍流条件及火焰工况留出；比较剖面与积分误差、条件平均和后验稳定性，避免随机拆分相邻 DNS 体素。

## 局限与当前状态

Clear BSD 许可，包含不授予专利权的条款，保留原文；未执行模型。

## 代码溯源

- 仓库：[cristianlacey/data-based-dissipation-rates](https://github.com/cristianlacey/data-based-dissipation-rates)
- 固定提交：`ed1700e5cb5fcbfbd5bdcd48e615f6c3e9f9445d`
- 关系证据：`author_implementation_readme_explicit`；来自上游 README，不代表本库已做作者身份独立认证。
- 许可：BSD-3-Clause-Clear；收纳状态：`source_archive_collected`。
- [代码包卡片](../../../code_packages/cristianlacey__data-based-dissipation-rates/README.md)

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1016/j.combustflame.2023.113139)；本轮整理日期 2026-11-12。完整元数据见同目录 `paper.json`。
