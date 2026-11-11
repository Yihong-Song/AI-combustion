# Real-time thermoacoustic data assimilation

P97829e9574 · 2022 · Journal of Fluid Mechanics

作者：A. Nóvoa; L. Magri

- DOI：[原文入口](https://doi.org/10.1017/jfm.2022.653)
- 分类：热声不稳定性预测、辨识与控制 / 预警与系统辨识
- JCR：**JCR 分区待核实**；报告最佳分区 未知；版本未知；官方核实：否。
- 阅读深度：已核对元数据与上游 README，尚未完成全文精读。
- 完整期刊论文复现：**尚未验收**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../04_instability_control/README.md) · [全局地图](../../../00_literature_map/README.md)

## 研究问题

用实时数据同化修正热声模型状态，并结合储备池学习处理模型偏差。

## 方法与代码所能确认的内容

README 声明仓库包含论文制图代码与数据。Part I 为 Rijke 管孪生实验；Part II 结合更高保真数据、数据同化与储备池计算。

## 复现入口与依赖

main.m 按论文图号选择目标图；先检查 Part I 的状态估计，再阅读 Part II 的高保真同化。

## 环境与数据

MATLAB 及代码需要的工具箱；不要将迁移后的 Python romda 默认参数视作本篇原始 MATLAB 配置。

## 建议验证协议（本库设计）

比较开环、仅同化和包含偏差模型的状态/参数误差；保存在线更新频率、噪声设定和计算延迟。

## 局限与当前状态

MIT；本轮归档不运行。维护后的软件另见 andreanovoa/real-time-bias-aware-DA，旧版与新版按版本区分。

## 代码溯源

- 仓库：[MagriLab/Real-time-TA-DA](https://github.com/MagriLab/Real-time-TA-DA)
- 固定提交：`5a4b485429a03596ece3581c36b43264d0308f25`
- 关系证据：`author_implementation_readme_explicit`；来自上游 README，不代表本库已做作者身份独立认证。
- 许可：MIT；收纳状态：`partial_source_snapshot_collected`。
- [代码包卡片](../../../code_packages/MagriLab__Real-time-TA-DA/README.md)

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1017/jfm.2022.653)；本轮整理日期 2026-11-12。完整元数据见同目录 `paper.json`。
