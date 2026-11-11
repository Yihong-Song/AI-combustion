# Data-driven computation of adjoint sensitivities without adjoint solvers: An application to thermoacoustics

P9903dd056c · 2024 · Physical Review Fluids

作者：Defne E. Ozan; Luca Magri

- DOI：[原文入口](https://doi.org/10.1103/physrevfluids.9.103902)
- 分类：热声不稳定性预测、辨识与控制 / 主动控制与强化学习
- JCR：**JCR 分区待核实**；报告最佳分区 未知；版本未知；官方核实：否。
- 阅读深度：已核对元数据与上游 README，尚未完成全文精读。
- 完整期刊论文复现：**尚未验收**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../04_instability_control/README.md) · [全局地图](../../../00_literature_map/README.md)

## 研究问题

在缺少完整伴随求解器时，用数据模型估计热声系统目标量的参数敏感度。

## 方法与代码所能确认的内容

README 明确列出本文，使用参数化 ESN，并为 Rijke 管引入热声时滞结构；另有 Lorenz 63 通用示例，不能把它独立算作燃烧论文。

## 复现入口与依赖

tutorial_rijke.ipynb 从数据生成、训练、验证到敏感度计算；src 中独立脚本与配置支撑批量实验。

## 环境与数据

依赖与配置从固定提交提取；保留 Rijke 管参数、时间离散和扰动幅值，Lorenz 教程用于理解代码。

## 建议验证协议（本库设计）

对比解析/数值伴随和有限差分，分别评估状态预测与目标函数梯度；跨参数检验梯度方向、幅值和优化效果。

## 局限与当前状态

未定位明确根许可证，链接收纳；相同仓库还对应会议论文，会议不计作 JCR 期刊。

## 代码溯源

- 仓库：[MagriLab/Adjoint-ESN](https://github.com/MagriLab/Adjoint-ESN)
- 固定提交：`8483399d9cae3b9ee83e03fc84107feb0d9e86ad`
- 关系证据：`author_implementation_readme_explicit`；来自上游 README，不代表本库已做作者身份独立认证。
- 许可：not_located；收纳状态：`link_only`。
- [代码包卡片](../../../code_packages/MagriLab__Adjoint-ESN/README.md)

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1103/physrevfluids.9.103902)；本轮整理日期 2026-11-12。完整元数据见同目录 `paper.json`。
