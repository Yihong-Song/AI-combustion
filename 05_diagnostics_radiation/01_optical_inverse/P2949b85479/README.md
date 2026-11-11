# Deep learning-based denoising for fast time-resolved flame emission spectroscopy in high-pressure combustion environment

P2949b85479 · 2023 · Combustion and Flame

作者：Taekeun Yoon; Seon Woong Kim; Hosung Byun; Younsik Kim; Campbell D. Carter; Hyungrok Do

- DOI：[原文入口](https://doi.org/10.1016/j.combustflame.2022.112583)
- 分类：光学诊断、反演、烟炱与辐射 / 光谱、图像与层析反演
- JCR：**二级来源报告 Q1/Q2，JCR 版本待官方核实**；报告最佳分区 Q1；版本未知；官方核实：否。
- 阅读深度：已核对元数据与上游 README，尚未完成全文精读。
- 完整期刊论文复现：**尚未验收**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../05_diagnostics_radiation/README.md) · [全局地图](../../../00_literature_map/README.md)

分区线索：[二级来源](https://www.letpub.com/index.php?page=journalapp&view=detail&journalid=1901)。多类别期刊使用报告中的最佳类别作为候选信号，不能解释为所有类别均为 Q1。

## 研究问题

对高压燃烧环境中的快速时间分辨火焰发射光谱进行深度学习去噪。

## 方法与代码所能确认的内容

上游包含 environment.yaml、config.yaml 和 main.py，并在 README 链接 rawdataM.mat 外部数据。比较去噪效果时必须检查谱线峰位、峰面积以及后续反演偏差。

## 复现入口与依赖

按 environment.yaml 单独创建环境，取得 rawdataM.mat 后调整 config.yaml，再审查 main.py。

## 环境与数据

README 使用 Windows Python 3.10.4；数据位于外部 Google Drive，未下载核验。

## 建议验证协议（本库设计）

按实验批次/压力分组留出，比较 SNR、谱线面积、温度或浓度偏差；仅有 PSNR 提升不足以证明测量准确。

## 局限与当前状态

未找到明确许可，保留版本链接和说明，不镜像源代码。外部数据可访问性与许可另行核实。

## 代码溯源

- 仓库：[ytg7146/DU_CNN](https://github.com/ytg7146/DU_CNN)
- 固定提交：`b1024dfb9d61decad1e58e643cc9418715ff47f1`
- 关系证据：`author_implementation_readme_explicit`；来自上游 README，不代表本库已做作者身份独立认证。
- 许可：not_located；收纳状态：`link_only`。
- [代码包卡片](../../../code_packages/ytg7146__DU_CNN/README.md)

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1016/j.combustflame.2022.112583)；本轮整理日期 2026-11-12。完整元数据见同目录 `paper.json`。
