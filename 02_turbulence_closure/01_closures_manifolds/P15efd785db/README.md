# An a priori evaluation of a principal component and artificial neural network based combustion model in diesel engine conditions

P15efd785db · 2021 · Proceedings of the Combustion Institute

作者：Deepak K. Dalakoti; Armin Wehrfritz; Bruno Savard; Marc S. Day; John B. Bell; Evatt R. Hawkes

- DOI：[原文入口](https://doi.org/10.1016/j.proci.2020.06.263)
- 分类：湍流燃烧闭合与流形模型 / 闭合、PDF 与热化学流形
- JCR：**二级来源报告 Q1/Q2，JCR 版本待官方核实**；报告最佳分区 Q1；版本未知；官方核实：否。
- 阅读深度：已核对元数据与上游 README，尚未完成全文精读。
- 论文原始指标复现：**未执行**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../02_turbulence_closure/README.md) · [全局地图](../../../00_literature_map/README.md)

分区线索：[二级来源](https://www.letpub.com/journal-selector/journal/6861)。多类别期刊使用报告中的最佳类别作为候选信号，不能解释为所有类别均为 Q1。

## 研究问题

在柴油机条件下，对 PCA 与人工神经网络结合的燃烧模型进行先验评价。

## 方法与代码所能确认的内容

README 直接引用本 DOI，说明进行燃烧数据 PCA 与神经网络拟合。该引用关系支持收纳，但短 README 不足以证明完整原文实验齐备。

## 复现入口与依赖

根目录 PCA-ANN.ipynb、helper_functions.py 与 neural_networks.py。

## 环境与数据

README 未给出完整环境；应从 notebook 导入、数据读取和辅助脚本逐项提取依赖，未执行。

## 建议验证协议（本库设计）

统一潜维数和输入变量，比较 PCA 重构与反应源项误差，按完整工况和滤波尺度留出；先验结果需进一步检验后验稳定性。

## 局限与当前状态

未定位许可，仅链接。这里的实现关系为 README 明确引用，强度不同于作者声明提供全文复现实验。

## 代码溯源

- 仓库：[deepakdalakoti/PCA-ANN](https://github.com/deepakdalakoti/PCA-ANN)
- 固定提交：`54f48ff9ea8e88a21216de06641c77b829b394f6`
- 关系证据：`repository_reference_readme_explicit`；来自上游 README，不代表本库已做作者身份独立认证。
- 许可：not_located；收纳状态：`link_only`。
- [代码包卡片](../../../code_packages/deepakdalakoti__PCA-ANN/README.md)

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1016/j.proci.2020.06.263)；本轮整理日期 2026-11-11。完整元数据见同目录 `paper.json`。
