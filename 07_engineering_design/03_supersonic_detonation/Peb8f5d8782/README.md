# A machine learning based approach for statistical analysis of detonation cells from soot foils

Peb8f5d8782 · 2025 · Combustion and Flame

作者：Vansh Sharma; Michael Ullman; Venkat Raman

- DOI：[原文入口](https://doi.org/10.1016/j.combustflame.2025.114026)
- 分类：发动机、燃烧器与复杂推进系统设计 / 超声速燃烧与爆轰
- JCR：**二级来源报告 Q1/Q2，JCR 版本待官方核实**；报告最佳分区 Q1；版本未知；官方核实：否。
- 阅读深度：已核对元数据与上游 README，尚未完成全文精读。
- 完整期刊论文复现：**尚未验收**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../07_engineering_design/README.md) · [全局地图](../../../00_literature_map/README.md)

分区线索：[二级来源](https://www.letpub.com/index.php?page=journalapp&view=detail&journalid=1901)。多类别期刊使用报告中的最佳类别作为候选信号，不能解释为所有类别均为 Q1。

## 研究问题

从烟膜图像自动分割爆轰胞格并统计尺寸与面积，减少人工量取。

## 方法与代码所能确认的内容

README 说明利用 CellPose 类分割工具，比较预处理前后结果；这是爆轰图像计量任务，区别于直接预测爆轰流场。

## 复现入口与依赖

package.list、config.py、main_sootFoilSeg.py；example/ 含 case 10a。

## 环境与数据

上游建议 Python 3.9+；CellPose 预训练权重和图像数据的许可也应单独记录。

## 建议验证协议（本库设计）

与盲法人工标注比较胞格宽度、分布和漏检；以整张烟膜作为独立样本，避免图块泄漏。

## 局限与当前状态

LGPL-2.1 许可已定位；未执行分割。预处理改善不能只靠一张示例图判断。

## 代码溯源

- 仓库：[vanshs1/ML_DetonationCells_SootFoil](https://github.com/vanshs1/ML_DetonationCells_SootFoil)
- 固定提交：`4ad20d49d657d2c5f78de4d87c77e581fb446df7`
- 关系证据：`author_implementation_readme_explicit`；来自上游 README，不代表本库已做作者身份独立认证。
- 许可：LGPL-2.1 (inspect upstream terms)；收纳状态：`partial_source_snapshot_collected`。
- [代码包卡片](../../../code_packages/vanshs1__ML_DetonationCells_SootFoil/README.md)

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1016/j.combustflame.2025.114026)；本轮整理日期 2026-11-12。完整元数据见同目录 `paper.json`。
