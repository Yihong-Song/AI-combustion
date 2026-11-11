# Robust identification of flame frequency response via multi-fidelity Gaussian process approach

P67741bfd8c · 2021 · Journal of Sound and Vibration

作者：Shuai Guo; Camilo F. Silva; Wolfgang Polifke

- DOI：[原文入口](https://doi.org/10.1016/j.jsv.2021.116083)
- 分类：热声不稳定性预测、辨识与控制 / 预警与系统辨识
- JCR：**二级来源报告 Q1/Q2，JCR 版本待官方核实**；报告最佳分区 Q1；版本未知；官方核实：否。
- 阅读深度：已核对元数据与上游 README，尚未完成全文精读。
- 完整期刊论文复现：**尚未验收**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../04_instability_control/README.md) · [全局地图](../../../00_literature_map/README.md)

分区线索：[二级来源](https://www.letpub.com/journal-selector/journal/5164)。多类别期刊使用报告中的最佳类别作为候选信号，不能解释为所有类别均为 Q1。

## 研究问题

融合低成本宽带识别与高保真谐波识别，提高火焰频率响应估计的鲁棒性。

## 方法与代码所能确认的内容

README 明确列题名、作者与 Journal of Sound and Vibration；多保真 Gaussian Process 聚合低/高保真响应，并展示实验台数据。

## 复现入口与依赖

MatlabScripts 中 BroadbandForcing、HarmonicForcing、Ref_FIR、SNR1_gain 与 SNR1_phase，按论文章节定位制图代码。

## 环境与数据

MATLAB 与高斯过程相关依赖、输入/热释放信号；README 谐波频率采用离散网格是实现选择，需与原文核对。

## 建议验证协议（本库设计）

固定计算/实验预算比较单保真与融合策略，分别看增益、相位误差及置信区间；保留不同噪声比与频率留出。

## 局限与当前状态

未定位许可证，仅链接；火焰传递函数误差还需传播至稳定性分析。

## 代码溯源

- 仓库：[ShuaiGuo16/Multi-Fidelity-ML](https://github.com/ShuaiGuo16/Multi-Fidelity-ML)
- 固定提交：`3cf5f232cedd21e60cdb159f03d094380a814863`
- 关系证据：`author_implementation_readme_explicit`；来自上游 README，不代表本库已做作者身份独立认证。
- 许可：not_located；收纳状态：`link_only`。
- [代码包卡片](../../../code_packages/ShuaiGuo16__Multi-Fidelity-ML/README.md)

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1016/j.jsv.2021.116083)；本轮整理日期 2026-11-12。完整元数据见同目录 `paper.json`。
