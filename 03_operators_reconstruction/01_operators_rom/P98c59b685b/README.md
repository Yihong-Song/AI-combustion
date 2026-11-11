# Learning stiff chemical kinetics using extended deep neural operators

P98c59b685b · 2024 · Computer Methods in Applied Mechanics and Engineering

作者：Somdatta Goswami; Ameya D. Jagtap; Hessam Babaee; Bryan T. Susi; George Em Karniadakis

- DOI：[原文入口](https://doi.org/10.1016/j.cma.2023.116674)
- 分类：神经算子、降阶与流场重建 / 算子、降阶与超分辨率
- JCR：**二级来源报告 Q1/Q2，JCR 版本待官方核实**；报告最佳分区 Q1；版本未知；官方核实：否。
- 阅读深度：已核对元数据与上游 README，尚未完成全文精读。
- 完整期刊论文复现：**尚未验收**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../03_operators_reconstruction/README.md) · [全局地图](../../../00_literature_map/README.md)

分区线索：[二级来源](https://www.letpub.com/journal-selector/journal/1988)。多类别期刊使用报告中的最佳类别作为候选信号，不能解释为所有类别均为 Q1。

## 研究问题

用扩展深度神经算子近似多时间尺度的刚性化学动力学。

## 方法与代码所能确认的内容

README 明确写本论文题名、作者与期刊，AE-DeepONet 文件夹提供有限 Example 3 数据；完整数据上游明确尚未提供，可用 Cantera 重建实验。

## 复现入口与依赖

先检查 AE-DeepONet 示例与各方法子目录，按原文例题建立初值、时间采样、编码器及算子输入的映射。

## 环境与数据

各子目录的框架与依赖需独立提取；Cantera 数据重生成必须固定机理、初始工况与采样。

## 建议验证协议（本库设计）

按初始条件及轨迹留出，检验快慢尺度、尖峰、长期组分守恒，比较相同数据预算下常规 DeepONet 与扩展方案。

## 局限与当前状态

完整数据不可得；未定位许可，只提供固定链接。不能把有限示例运行当作全文结果。

## 代码溯源

- 仓库：[somdattagoswami/Approximating-StiffKinetics](https://github.com/somdattagoswami/Approximating-StiffKinetics)
- 固定提交：`a7e90624cbf96d103559f613257e8e17ee104609`
- 关系证据：`author_implementation_readme_explicit`；来自上游 README，不代表本库已做作者身份独立认证。
- 许可：not_located；收纳状态：`link_only`。
- [代码包卡片](../../../code_packages/somdattagoswami__Approximating-StiffKinetics/README.md)

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1016/j.cma.2023.116674)；本轮整理日期 2026-11-12。完整元数据见同目录 `paper.json`。
