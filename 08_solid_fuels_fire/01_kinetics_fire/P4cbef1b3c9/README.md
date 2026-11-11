# Autonomous kinetic modeling of biomass pyrolysis using chemical reaction neural networks

P4cbef1b3c9 · 2022 · Combustion and Flame

作者：Weiqi Ji; Franz Richter; Michael J. Gollner; Sili Deng

- DOI：[原文入口](https://doi.org/10.1016/j.combustflame.2022.111992)
- 分类：固体燃料、热解与火灾安全 / 生物质、煤、热解与火灾
- JCR：**二级来源报告 Q1/Q2，JCR 版本待官方核实**；报告最佳分区 Q1；版本未知；官方核实：否。
- 阅读深度：已核对元数据与上游 README，尚未完成全文精读。
- 论文原始指标复现：**未执行**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../08_solid_fuels_fire/README.md) · [全局地图](../../../00_literature_map/README.md)

分区线索：[二级来源](https://www.letpub.com/index.php?page=journalapp&view=detail&journalid=1901)。多类别期刊使用报告中的最佳类别作为候选信号，不能解释为所有类别均为 Q1。

## 研究问题

由热重分析数据自动建立生物质热解/氧化动力学，减少依赖专家预设反应路径。

## 方法与代码所能确认的内容

README 说明将质量作用定律和 Arrhenius 规律嵌入 CRNN，再用 neural ODE 预测 TGA 残余质量；演示对象为纤维素热解和氧化。

## 复现入口与依赖

从固定提交中的 Project.toml 和示例脚本建立 Julia 环境，再核对 TGA 数据、升温速率和残余质量定义。

## 环境与数据

Julia 与上游 Project/Manifest；应为该仓库单独创建项目环境。不能用另一 CRNN 分支的 Julia 环境直接替代。

## 建议验证协议（本库设计）

留出完整升温速率或氧浓度条件，比较质量曲线和失重速率曲线；同时检验参数可辨识性、不同初始化得到的网络结构。

## 局限与当前状态

TGA 有效反应网络不是唯一微观基元机理。小尺度热分析拟合不能直接证明大尺度火灾预测正确。

## 代码溯源

- 仓库：[DENG-MIT/Biomass.jl](https://github.com/DENG-MIT/Biomass.jl)
- 固定提交：`d4909dfc750d2a063ba5e4a851bf5dffd4021e23`
- 关系证据：`author_implementation_readme_explicit`；来自上游 README，不代表本库已做作者身份独立认证。
- 许可：MIT；收纳状态：`source_archive_collected`。
- [代码包卡片](../../../code_packages/DENG-MIT__Biomass.jl/README.md)

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1016/j.combustflame.2022.111992)；本轮整理日期 2026-11-11。完整元数据见同目录 `paper.json`。
