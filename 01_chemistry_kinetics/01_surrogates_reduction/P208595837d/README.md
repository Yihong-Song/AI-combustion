# Enhancing deep learning of ammonia/natural gas combustion kinetics via physics-aware data augmentation and scale separation

P208595837d · 2026 · Fuel

作者：Ke Xiao; Yangchen Xu; Han Li; Zhi X. Chen

- DOI：[原文入口](https://doi.org/10.1016/j.fuel.2026.138904)
- 分类：化学动力学代理、缩减与机理发现 / 代理与缩减
- JCR：**二级来源报告 Q1/Q2，JCR 版本待官方核实**；报告最佳分区 Q1；版本未知；官方核实：否。
- 阅读深度：已核对元数据与上游 README，尚未完成全文精读。
- 完整期刊论文复现：**尚未验收**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../01_chemistry_kinetics/README.md) · [全局地图](../../../00_literature_map/README.md)

分区线索：[二级来源](https://www.letpub.com/index.php?page=journalapp&view=detail&journalid=2950)。多类别期刊使用报告中的最佳类别作为候选信号，不能解释为所有类别均为 Q1。

## 研究问题

改善氨/天然气燃烧化学学习中状态覆盖与不同时间尺度的处理。

## 方法与代码所能确认的内容

DFODE-kit 固定 README 在 Physics-aware data augmentation and scale separation 部分明确列出本文题名、作者、Fuel 卷和文章号。该证据确认同一软件生态的相关工作，不保证论文的增广配置与尺度分离消融完整包含在当前默认流程。

## 复现入口与依赖

从 augment、label、train 三个命令及数据变换配置入手；逐项比对原文的状态扰动、筛选准则与尺度分离方式。

## 环境与数据

同 DFODE-kit 的基础依赖；另需原文所用氨/天然气机理、混合物定义、训练状态与后验反应流算例。

## 建议验证协议（本库设计）

在固定数据预算下分别消融物理筛选、增广和尺度分离；独立保留混合比、压力及温度，比较痕量组分、守恒和滚动误差。

## 局限与当前状态

关联类型为 related work，不能计为全文实验已打包；与 DFODE 软件论文共享一个包。

## 代码溯源

- 仓库：[deepflame-ai/DFODE-kit](https://github.com/deepflame-ai/DFODE-kit)
- 固定提交：`bc65e84bc7644675b9996e3eea08f0d38cbceaad`
- 关系证据：`author_related_work_readme_explicit`；来自上游 README，不代表本库已做作者身份独立认证。
- 许可：GPL-3.0 (inspect upstream terms)；收纳状态：`partial_source_snapshot_collected`。
- [代码包卡片](../../../code_packages/deepflame-ai__DFODE-kit/README.md)

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1016/j.fuel.2026.138904)；本轮整理日期 2026-11-12。完整元数据见同目录 `paper.json`。
