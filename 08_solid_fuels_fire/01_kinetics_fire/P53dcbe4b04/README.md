# Classification of solid fuels with machine learning

P53dcbe4b04 · 2020 · Fuel

作者：Furkan Elmaz; Barkın Büyükçakır; Özgün Yücel; Ali Yener Mutlu

- DOI：[原文入口](https://doi.org/10.1016/j.fuel.2020.117066)
- 分类：固体燃料、热解与火灾安全 / 生物质、煤、热解与火灾
- JCR：**二级来源报告 Q1/Q2，JCR 版本待官方核实**；报告最佳分区 Q1；版本未知；官方核实：否。
- 阅读深度：已核对元数据与上游 README，尚未完成全文精读。
- 论文原始指标复现：**未执行**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../08_solid_fuels_fire/README.md) · [全局地图](../../../00_literature_map/README.md)

分区线索：[二级来源](https://www.letpub.com/index.php?page=journalapp&view=detail&journalid=2950)。多类别期刊使用报告中的最佳类别作为候选信号，不能解释为所有类别均为 Q1。

## 研究问题

根据燃料表征数据对固体燃料进行分层分类。

## 方法与代码所能确认的内容

README 声明仓库为本文补充材料，提供分层分类训练/测试流程。根目录有 Dataset.xlsx 及多个预训练 pkl 文件。

## 复现入口与依赖

main.py 调用 training.py 与 testing.py；README 说明默认读取预训练分类器，重训需要切换对应代码。

## 环境与数据

依赖版本应从脚本导入补齐；Excel 数据、特征含义和预训练文件兼容性需另核。

## 建议验证协议（本库设计）

按来源或燃料家族留出，报告各层混淆矩阵、宏平均 F1 和类不平衡；区分燃料类别识别与燃烧性能预测。

## 局限与当前状态

未定位许可，代码和数据仅保留固定链接。pkl 是可执行序列化格式，不在本库自动加载。未执行原文训练。

## 代码溯源

- 仓库：[furkanelmaz/SolidFuelClassification](https://github.com/furkanelmaz/SolidFuelClassification)
- 固定提交：`70d23189d625a02b81019f6a60bd5769142b8d2f`
- 关系证据：`author_implementation_readme_explicit`；来自上游 README，不代表本库已做作者身份独立认证。
- 许可：not_located；收纳状态：`link_only`。
- [代码包卡片](../../../code_packages/furkanelmaz__SolidFuelClassification/README.md)

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1016/j.fuel.2020.117066)；本轮整理日期 2026-11-11。完整元数据见同目录 `paper.json`。
