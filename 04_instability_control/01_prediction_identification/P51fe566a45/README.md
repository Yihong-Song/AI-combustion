# Deep learning for continuous lead-time prediction of thermoacoustic instabilities in an annular combustor

P51fe566a45 · 2026 · Proceedings of the Combustion Institute

作者：Géraud Ponchet de Langlade; Mustafa A. Mohamad

- DOI：[原文入口](https://doi.org/10.1016/j.proci.2026.106547)
- 分类：热声不稳定性预测、辨识与控制 / 预警与系统辨识
- JCR：**二级来源报告 Q1/Q2，JCR 版本待官方核实**；报告最佳分区 Q1；版本未知；官方核实：否。
- 阅读深度：已核对元数据与上游 README，尚未完成全文精读。
- 完整期刊论文复现：**尚未验收**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../04_instability_control/README.md) · [全局地图](../../../00_literature_map/README.md)

分区线索：[二级来源](https://www.letpub.com/journal-selector/journal/6861)。多类别期刊使用报告中的最佳类别作为候选信号，不能解释为所有类别均为 Q1。

## 研究问题

从环形燃烧室压力信号连续预测距离热声失稳还有多久。

## 方法与代码所能确认的内容

README 明确对应本文，比较因果 Transformer、单向 LSTM 与 XGBoost；说明按完整合成轨迹切分，并进行实验数据零样本评价。上游给出的轨迹数和种子仅作为配置线索，未由本库重算。

## 复现入口与依赖

synthetic_gen.py 生成轨迹；label_exp_onset.py 标注实验起振；trans_train.py、lstm_train.py、XGBoost_train.py 对照；common.py 与 preprocess_mod.py 核对标签和窗口。

## 环境与数据

Python≥3.10、PyTorch、SciPy、pandas、scikit-learn、XGBoost；实验数据入口 Zenodo 23091955 已定位，未下载验证。

## 建议验证协议（本库设计）

整条实验爬升/轨迹留出，统一起振定义、输入窗口、时间单位与提前量；报告误差随失稳距离变化、跨随机种子及假警率。

## 局限与当前状态

MIT；合成轨迹多种子不是多篇复现。原论文正式训练与实验零样本结果尚未执行。

## 代码溯源

- 仓库：[Predictive-Intelligent-Systems-Lab/TTE-TAI-PROCI-paper](https://github.com/Predictive-Intelligent-Systems-Lab/TTE-TAI-PROCI-paper)
- 固定提交：`f6f07bed28fc350a698a56012796ca7a16abe626`
- 关系证据：`author_implementation_readme_explicit`；来自上游 README，不代表本库已做作者身份独立认证。
- 许可：MIT；收纳状态：`source_archive_collected`。
- [代码包卡片](../../../code_packages/Predictive-Intelligent-Systems-Lab__TTE-TAI-PROCI-paper/README.md)

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1016/j.proci.2026.106547)；本轮整理日期 2026-11-12。完整元数据见同目录 `paper.json`。
