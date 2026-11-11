# DFODE-Kit: Deep learning package for solving flame chemical kinetics with high-dimensional stiff ordinary differential equations

P485814185d · 2026 · Computer Physics Communications

作者：Han Li; Ke Xiao; Yangchen Xu; Haoze Zhang; Zhenyi Chen; Runze Mao; Zhi X. Chen

- DOI：[原文入口](https://doi.org/10.1016/j.cpc.2025.110013)
- 分类：化学动力学代理、缩减与机理发现 / 代理与缩减
- JCR：**JCR 分区待核实**；报告最佳分区 未知；版本未知；官方核实：否。
- 阅读深度：已核对元数据与上游 README，尚未完成全文精读。
- 完整期刊论文复现：**尚未验收**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../01_chemistry_kinetics/README.md) · [全局地图](../../../00_literature_map/README.md)

## 研究问题

用神经网络替代详细燃烧化学的刚性 ODE 积分，同时保留与 CFD 的接口。

## 方法与代码所能确认的内容

固定 README 把本篇列为 DFODE-kit 软件论文，给出生成典型火焰、采样、数据增广、Cantera 标注及训练的连续工作流。输入热化学状态与短时间步输出必须按模型配置核对，不能将点火延迟回归当作化学积分器。

## 复现入口与依赖

dfode_kit/cli/main.py；config → init → run-case → sample → augment → label → train；先阅读 docs 中 data-workflow 与各命令说明。

## 环境与数据

Python、Cantera、HDF5、模型训练依赖；运行 CFD 案例还需 OpenFOAM、DeepFlame 及本机路径配置。归档不代表外部求解器、机理或全量训练数据齐备。

## 建议验证协议（本库设计）

按独立反应器轨迹和火焰工况划分数据；比较温度/组分轨迹、着火与放热、守恒误差、长时积分和后验 CFD 稳定性，计入数据生成与模型装载成本。

## 局限与当前状态

GPL-3.0。当前提交经过重构，需与论文发表时版本对照；本轮收录，不执行训练。

## 代码溯源

- 仓库：[deepflame-ai/DFODE-kit](https://github.com/deepflame-ai/DFODE-kit)
- 固定提交：`bc65e84bc7644675b9996e3eea08f0d38cbceaad`
- 关系证据：`author_implementation_readme_explicit`；来自上游 README，不代表本库已做作者身份独立认证。
- 许可：GPL-3.0 (inspect upstream terms)；收纳状态：`partial_source_snapshot_collected`。
- [代码包卡片](../../../code_packages/deepflame-ai__DFODE-kit/README.md)

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1016/j.cpc.2025.110013)；本轮整理日期 2026-11-12。完整元数据见同目录 `paper.json`。
