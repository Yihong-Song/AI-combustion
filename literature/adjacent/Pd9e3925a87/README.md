# Deep reinforcement learning for dynamic control of fuel injection timing in multi-pulse compression ignition engines

Pd9e3925a87 · 2021 · International Journal of Engine Research

作者：Marc T Henry de Frahan; Nicholas T Wimer; Shashank Yellapantula; Ray W Grout

- DOI：[原文入口](https://doi.org/10.1177/14680874211019345)
- 分类：发动机、燃烧器与复杂推进系统设计 / 控制与多目标设计
- JCR：**二级来源报告 Q3/Q4，不纳入 Q1/Q2 候选主集**；报告最佳分区 Q3；版本未知；官方核实：否。
- 阅读深度：已核对元数据与上游 README，尚未完成全文精读。
- 完整期刊论文复现：**尚未验收**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../07_engineering_design/README.md) · [全局地图](../../../00_literature_map/README.md)

分区线索：[二级来源](https://www.letpub.com/journal-selector/journal/3727)。多类别期刊使用报告中的最佳类别作为候选信号，不能解释为所有类别均为 Q1。

## 研究问题

通过强化学习选择多次喷射压燃发动机的喷油时刻。

## 方法与代码所能确认的内容

README 明确列本论文题名、作者与 International Journal of Engine Research，提供发动机环境和 PPO 示例；奖励、动作和状态定义需要从输入配置与原文逐项确认。

## 复现入口与依赖

scripts/ppo-example 下以 python ../main.py --fname input.toml 启动；先阅读 environment.yaml 和环境模型。

## 环境与数据

按 environment.yaml 建独立环境，检查发动机模型、机理和数值依赖；README 的 nosetests 是上游测试入口，本轮未执行。

## 建议验证协议（本库设计）

相同发动机模型、初始状态与动作预算比较规则控制及优化基线；同时考察热效率、排放、约束违反和跨工况稳定性。

## 局限与当前状态

Apache-2.0；仿真训练收益不等于真实发动机闭环验证，JCR 年份/类别仍待确认。

## 代码溯源

- 仓库：[NatLabRockies/MPRL](https://github.com/NatLabRockies/MPRL)
- 固定提交：`d54229e8290d5229b3ae9971ca75a07e7386c5c4`
- 关系证据：`author_implementation_readme_explicit`；来自上游 README，不代表本库已做作者身份独立认证。
- 许可：Apache-2.0；收纳状态：`source_archive_collected`。
- [代码包卡片](../../../code_packages/NatLabRockies__MPRL/README.md)

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1177/14680874211019345)；本轮整理日期 2026-11-12。完整元数据见同目录 `paper.json`。
