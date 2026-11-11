# Integrated neural network approach for autonomous sensitivity analysis and optimization of sectional soot kinetic modeling

Pe31f2bea9d · 2026 · Proceedings of the Combustion Institute

作者：Feixue Cai; Patrizia Crepaldi; Andrea Nobili; Matthew J. Cleary; Zhuyin Ren; Assaad R. Masri; Tiziano Faravelli

- DOI：[原文入口](https://doi.org/10.1016/j.proci.2026.106166)
- 分类：光学诊断、反演、烟炱与辐射 / 烟炱生成及 PAH
- JCR：**二级来源报告 Q1/Q2，JCR 版本待官方核实**；报告最佳分区 Q1；版本未知；官方核实：否。
- 阅读深度：已核对元数据与上游 README，尚未完成全文精读。
- 完整期刊论文复现：**尚未验收**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../05_diagnostics_radiation/README.md) · [全局地图](../../../00_literature_map/README.md)

分区线索：[二级来源](https://www.letpub.com/journal-selector/journal/6861)。多类别期刊使用报告中的最佳类别作为候选信号，不能解释为所有类别均为 Q1。

## 研究问题

对分段烟炱动力学模型进行快速敏感度分析和参数优化。

## 方法与代码所能确认的内容

README 题名与 Crossref 期刊文章吻合，列出 MLP 预测粒径分布、自动微分、主动子空间及软谷值分析。README 仍写 under review，因此保留题名匹配关系，不提升为已确认最终发表版官方代码。

## 复现入口与依赖

scripts/01_train_from_config.py 到 05_run_optimization.py；reproduce_all.py 和跳过预训练入口；先检查 configs 与数据列定义。

## 环境与数据

requirements.txt、PyTorch 模型及数据/预训练目录；文件是否包含实际全部数据和权重尚待清点。

## 建议验证协议（本库设计）

比较各粒径箱误差、双峰谷位置、敏感度置信区间和参数拟合；按独立参数区域及实验工况留出。

## 局限与当前状态

README 声称 MIT，但固定提交未定位许可文件，因此只保留链接。出版版与 under-review 代码的对应待核。

## 代码溯源

- 仓库：[cfx18/NN4Soot](https://github.com/cfx18/NN4Soot)
- 固定提交：`d06d5cf026d62f0f61338d6ad6650c6532a211f2`
- 关系证据：`title_match_repository_readme`；来自上游 README，不代表本库已做作者身份独立认证。
- 许可：not_located；收纳状态：`link_only`。
- [代码包卡片](../../../code_packages/cfx18__NN4Soot/README.md)

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1016/j.proci.2026.106166)；本轮整理日期 2026-11-12。完整元数据见同目录 `paper.json`。
