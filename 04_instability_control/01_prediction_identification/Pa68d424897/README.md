# Hard-constrained neural networks for modeling nonlinear acoustics

Pa68d424897 · 2023 · Physical Review Fluids

作者：Defne E. Ozan; Luca Magri

- DOI：[原文入口](https://doi.org/10.1103/physrevfluids.8.103201)
- 分类：热声不稳定性预测、辨识与控制 / 预警与系统辨识
- JCR：**JCR 分区待核实**；报告最佳分区 未知；版本未知；官方核实：否。
- 阅读深度：已核对元数据与上游 README，尚未完成全文精读。
- 完整期刊论文复现：**尚未验收**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../04_instability_control/README.md) · [全局地图](../../../00_literature_map/README.md)

## 研究问题

从有限压力测点重建非线性声场与热声速度场，并外推振荡。

## 方法与代码所能确认的内容

README 明确对应 Physical Review Fluids 论文，利用硬约束和软约束把声学结构加入神经网络；提供极限环、准周期和混沌 Rijke 管数据生成方案。

## 复现入口与依赖

python -m hcta.rijke_galerkin.generate 生成合成数据；python -m hcta.experiment --config_path src/configs/config.yml 运行；figures 中脚本对应论文图。

## 环境与数据

按项目依赖安装独立 Python 环境；作者另提供 Zenodo 10021355 数据与 figure_data 配置/权重。数据链接已定位，本轮未下载。

## 建议验证协议（本库设计）

按传感器数、噪声与未见动力学状态评估；比较完整压力/速度场、时间外推、频谱及硬约束消融，不能只看训练点拟合。

## 局限与当前状态

MIT。README 明说图 13/14 的模型数据未打包，需要重做 robustness_sensor.py 与 robustness_noise.py 扫描。

## 代码溯源

- 仓库：[MagriLab/HCTA](https://github.com/MagriLab/HCTA)
- 固定提交：`50bb41720424a732b28f06adf684e593c98fa0c7`
- 关系证据：`author_implementation_readme_explicit`；来自上游 README，不代表本库已做作者身份独立认证。
- 许可：MIT；收纳状态：`partial_source_snapshot_collected`。
- [代码包卡片](../../../code_packages/MagriLab__HCTA/README.md)

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1103/physrevfluids.8.103201)；本轮整理日期 2026-11-12。完整元数据见同目录 `paper.json`。
