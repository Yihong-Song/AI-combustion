# Data-based filtered dissipation rate modelling for multi-modal turbulent combustion: evaluating a priori model generalizability

P2bf9290361 · 2026 · Combustion Theory and Modelling

作者：Cristian E. Lacey; Bruno S. Soriano; Martin Rieth; Michael E. Mueller; Jacqueline H. Chen

- DOI：[原文入口](https://doi.org/10.1080/13647830.2026.2621012)
- 分类：湍流燃烧闭合与流形模型 / 闭合、PDF 与热化学流形
- JCR：**二级来源报告 Q3/Q4，不纳入 Q1/Q2 候选主集**；报告最佳分区 Q3；版本未知；官方核实：否。
- 阅读深度：已核对元数据与上游 README，尚未完成全文精读。
- 完整期刊论文复现：**尚未验收**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../02_turbulence_closure/README.md) · [全局地图](../../../00_literature_map/README.md)

分区线索：[二级来源](https://www.letpub.com/journal-selector/journal/1904)。多类别期刊使用报告中的最佳类别作为候选信号，不能解释为所有类别均为 Q1。

## 研究问题

在多模态湍流燃烧流形模型中闭合混合分数、交叉及进度变量的滤波耗散率。

## 方法与代码所能确认的内容

README 明确列本文 DOI 与 TensorFlow 模型，面向三类耗散率闭合；题名中的 a priori 泛化检验不能解释为后验 LES 验证。

## 复现入口与依赖

按 tf-gpu.yml 与 README 输入定义读取模型，分别核对 chi_ZZ、chi_ZLambda 和 chi_LambdaLambda 的符号、尺度和过滤定义。

## 环境与数据

TensorFlow 2.4.1 的独立环境、适配的 DNS/流形数据和预处理；未确认训练数据全量可用。

## 建议验证协议（本库设计）

按燃烧模态和完整模拟留出，对比各源项、交叉项符号、未见状态误差和物理可实现性。

## 局限与当前状态

当前二级分区线索为 Q3，保留在相邻附录，不计入 Q1/Q2。未定位许可文件，仅固定链接。

## 代码溯源

- 仓库：[cristianlacey/data-based-multi-modal-filtered-dissipation-rates](https://github.com/cristianlacey/data-based-multi-modal-filtered-dissipation-rates)
- 固定提交：`77f216e703d1d97edfc16a981d4046c2da97db14`
- 关系证据：`author_implementation_readme_explicit`；来自上游 README，不代表本库已做作者身份独立认证。
- 许可：not_located；收纳状态：`link_only`。
- [代码包卡片](../../../code_packages/cristianlacey__data-based-multi-modal-filtered-dissipation-rates/README.md)

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1080/13647830.2026.2621012)；本轮整理日期 2026-11-12。完整元数据见同目录 `paper.json`。
