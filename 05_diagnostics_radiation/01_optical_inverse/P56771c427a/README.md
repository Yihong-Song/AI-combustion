# SAGE: A machine learning model for primary particle segmentation in TEM images of soot aggregates

P56771c427a · 2025 · Proceedings of the Combustion Institute

作者：Timothy P. Day; Khaled Mosharraf Mukut; Luke Klacik; Ryan O’Donnell; James Wasilewski; Somesh P. Roy

- DOI：[原文入口](https://doi.org/10.1016/j.proci.2025.105821)
- 分类：光学诊断、反演、烟炱与辐射 / 光谱、图像与层析反演
- JCR：**二级来源报告 Q1/Q2，JCR 版本待官方核实**；报告最佳分区 Q1；版本未知；官方核实：否。
- 阅读深度：已核对元数据与上游 README，尚未完成全文精读。
- 完整期刊论文复现：**尚未验收**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../05_diagnostics_radiation/README.md) · [全局地图](../../../00_literature_map/README.md)

分区线索：[二级来源](https://www.letpub.com/journal-selector/journal/6861)。多类别期刊使用报告中的最佳类别作为候选信号，不能解释为所有类别均为 Q1。

## 研究问题

从烟炱 TEM 图像自动分割初级颗粒，减少人工形貌测量负担。

## 方法与代码所能确认的内容

README 明确列题名与 DOI。基于 Mask R-CNN，先使用合成 TEM 图像训练，再以人工标注真实图像微调；列出 SAGE0/1/2 与 COCO 初始化对照。

## 复现入口与依赖

SAGE_train.ipynb 训练/微调；SAGE_ANALYZE.ipynb 推理、模型比较及颗粒几何量提取；权重从 Releases 或 notebook 下载。

## 环境与数据

requirements.yml 的独立环境、Mask R-CNN 依赖、对应分割数据和权重。上游使用 Tesla K80，现代 TensorFlow/CUDA 版本需另核。

## 建议验证协议（本库设计）

按图像来源和烟炱类型留出，比较实例分割精度、颗粒尺度分布、重叠颗粒和人工标注不确定度；合成与真实数据分开报告。

## 局限与当前状态

GPL-3.0；源码许可不自动覆盖权重与图像。原 README 的兼容性建议不是本库实际验证。

## 代码溯源

- 仓库：[comp-comb/SAGE](https://github.com/comp-comb/SAGE)
- 固定提交：`04ac7006840838da7e1d53c8546360f8afe23a1e`
- 关系证据：`author_implementation_readme_explicit`；来自上游 README，不代表本库已做作者身份独立认证。
- 许可：GPL-3.0 (inspect upstream terms)；收纳状态：`partial_source_snapshot_collected`。
- [代码包卡片](../../../code_packages/comp-comb__SAGE/README.md)

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1016/j.proci.2025.105821)；本轮整理日期 2026-11-12。完整元数据见同目录 `paper.json`。
