# Physics-informed neural network WSGG model for radiative heat transfer in H2O–CO2–NH3 gas mixtures relevant to ammonia combustion

P69b4098fb3 · 2026 · Proceedings of the Combustion Institute

作者：Jiaxin Wang; Wei Chen; Tao Ren

- DOI：[原文入口](https://doi.org/10.1016/j.proci.2026.106476)
- 分类：光学诊断、反演、烟炱与辐射 / 辐射与烟炱辐射诊断
- JCR：**二级来源报告 Q1/Q2，JCR 版本待官方核实**；报告最佳分区 Q1；版本未知；官方核实：否。
- 阅读深度：已核对元数据与上游 README，尚未完成全文精读。
- 论文原始指标复现：**未执行**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../05_diagnostics_radiation/README.md) · [全局地图](../../../00_literature_map/README.md)

已执行作者演示：[命令、数值和适配记录](../../../reproductions/C01_wsgg_author_demo/README.md)；尚未重训或对照原文表格。

分区线索：[二级来源](https://www.letpub.com/journal-selector/journal/6861)。多类别期刊使用报告中的最佳类别作为候选信号，不能解释为所有类别均为 Q1。

## 研究问题

为含 NH3 的 H2O–CO2 参与性气体建立 PINN-WSGG 辐射模型。

## 方法与代码所能确认的内容

README 说明使用预训练 wsgg.json，结合一维 RTE 求解器，将辐射热损失与逐线 LBL 参考比较。

## 复现入口与依赖

python test.py；输入 data/profiles.npy、data/results.npy 和 PINN_WSGG/data/wsgg.json，输出 test_case.png。

## 环境与数据

先核对 requirements.txt；主要为 NumPy/SciPy/Matplotlib，实际以固定提交为准。README 的 your-username 克隆命令为占位符，应使用本库记录的真实仓库地址。

## 建议验证协议（本库设计）

比较局部辐射源项、热流和积分能量误差；零附近相对误差会发散，需同时给绝对或整体归一化误差。

## 局限与当前状态

明确 MIT 许可；本库已执行固定版本作者演示，实测与适配见 C01。仅验证预训练推理演示，尚未重训，也未复现原文目标表格；作者更广泛的验证结论仍不能当作本库实测。

## 代码溯源

- 仓库：[TaoRen-Rad/WSGG-H2O-CO2-NH3](https://github.com/TaoRen-Rad/WSGG-H2O-CO2-NH3)
- 固定提交：`0ed02920a2ea9dbea0c60db02fd51b4695cf6260`
- 关系证据：`author_implementation_readme_explicit`；来自上游 README，不代表本库已做作者身份独立认证。
- 许可：MIT；收纳状态：`source_archive_collected`。
- [代码包卡片](../../../code_packages/TaoRen-Rad__WSGG-H2O-CO2-NH3/README.md)

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1016/j.proci.2026.106476)；本轮整理日期 2026-11-11。完整元数据见同目录 `paper.json`。
