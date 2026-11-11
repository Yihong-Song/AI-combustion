# Learning dominant physical processes with data-driven balance models

P3fe49a4002 · 2021 · Nature Communications

作者：Jared L. Callaham; James V. Koch; Bingni W. Brunton; J. Nathan Kutz; Steven L. Brunton

- DOI：[原文入口](https://doi.org/10.1038/s41467-021-21331-z)
- 分类：发动机、燃烧器与复杂推进系统设计 / 超声速燃烧与爆轰
- JCR：**JCR 分区待核实**；报告最佳分区 未知；版本未知；官方核实：否。
- 阅读深度：已核对元数据与上游 README，尚未完成全文精读。
- 完整期刊论文复现：**尚未验收**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../07_engineering_design/README.md) · [全局地图](../../../00_literature_map/README.md)

## 研究问题

从方程项数据识别不同区域的主导物理平衡，并在旋转爆轰简化模型中解释反应与输运竞争。

## 方法与代码所能确认的内容

README 明确链接同题预印本，提供多物理例题；第七项是旋转爆轰发动机的 Majda–Burgers 简化模型。燃烧方向只对应这个子例，其余例题属于通用方法背景。

## 复现入口与依赖

先阅读 Burgers 的解释性 notebook，再定位 Rotating detonation engine analogue；生成 RDE 数据需 pyclaw。

## 环境与数据

scikit-learn、NumPy、SciPy、Matplotlib、seaborn；pyclaw 用于 RDE 数值数据，其他例题可能需要 pymech 或 MATLAB。

## 建议验证协议（本库设计）

检验聚类/稀疏识别的稳定性、噪声敏感度和物理分区解释；不能把简化模型结果推广为详细多组分爆轰验证。

## 局限与当前状态

MIT；期刊正式版与预印本对应以题名核对，燃烧案例仅是跨领域方法论文的一部分。

## 代码溯源

- 仓库：[dynamicslab/dominant-balance](https://github.com/dynamicslab/dominant-balance)
- 固定提交：`41ac6d2e1feccb8f3a71591d4d1f9dcbfcd1e299`
- 关系证据：`author_implementation_readme_explicit`；来自上游 README，不代表本库已做作者身份独立认证。
- 许可：MIT；收纳状态：`partial_source_snapshot_collected`。
- [代码包卡片](../../../code_packages/dynamicslab__dominant-balance/README.md)

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1038/s41467-021-21331-z)；本轮整理日期 2026-11-12。完整元数据见同目录 `paper.json`。
