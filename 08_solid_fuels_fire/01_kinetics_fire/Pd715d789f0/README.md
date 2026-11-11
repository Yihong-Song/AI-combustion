# CFD analysis of operating parameters and machine learning-aided optimization of reactor performance in a polyethylene pyrolysis fluidized bed

Pd715d789f0 · 2026 · Fuel

作者：Ling Qin; Lianyong Zhou; Zhongmei Li; He Lei; Li-Tao Zhu

- DOI：[原文入口](https://doi.org/10.1016/j.fuel.2026.138977)
- 分类：固体燃料、热解与火灾安全 / 生物质、煤、热解与火灾
- JCR：**二级来源报告 Q1/Q2，JCR 版本待官方核实**；报告最佳分区 Q1；版本未知；官方核实：否。
- 阅读深度：已核对元数据与上游 README，尚未完成全文精读。
- 论文原始指标复现：**未执行**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../08_solid_fuels_fire/README.md) · [全局地图](../../../00_literature_map/README.md)

分区线索：[二级来源](https://www.letpub.com/index.php?page=journalapp&view=detail&journalid=2950)。多类别期刊使用报告中的最佳类别作为候选信号，不能解释为所有类别均为 Q1。

## 研究问题

用机器学习辅助优化聚乙烯热解过程，属于燃烧上游热转化的相邻应用。

## 方法与代码所能确认的内容

固定版本 README 给出题名和明确 DOI；没有足够实现说明支持具体架构、数据切分或定量结论的转述。

## 复现入口与依赖

先检查仓库文件与论文补充材料，确定训练入口、输入工况、目标产物及评价协议。

## 环境与数据

README 未给出完整可复现环境；依赖和数据要求待逐文件核实。

## 建议验证协议（本库设计）

按实验批次与未见工况留出，比较代理误差和独立物理实验验证；优化建议与实测改进分开记录。

## 局限与当前状态

未定位许可，仅固定链接；尚未执行，也不能仅凭仓库题名声称训练数据和权重齐备。

## 代码溯源

- 仓库：[LitaoZhu201703/Machine-learning-aided-optimization-of-polyethylene-pyrolysis](https://github.com/LitaoZhu201703/Machine-learning-aided-optimization-of-polyethylene-pyrolysis)
- 固定提交：`01a6b60c669e321a02eb7b04441734d0152ed48b`
- 关系证据：`author_implementation_readme_explicit`；来自上游 README，不代表本库已做作者身份独立认证。
- 许可：not_located；收纳状态：`link_only`。
- [代码包卡片](../../../code_packages/LitaoZhu201703__Machine-learning-aided-optimization-of-polyethylene-pyrolysis/README.md)

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1016/j.fuel.2026.138977)；本轮整理日期 2026-11-11。完整元数据见同目录 `paper.json`。
