# Neural refractive index primitives for flame field reconstruction using background-oriented schlieren

Pc2b8d1f214 · 2026 · Combustion and Flame

作者：Xinyi Lu; Wei Hu; Zizhou Liao; Zheng Wang; Yue Zhang; Jingxuan Li

- DOI：[原文入口](https://doi.org/10.1016/j.combustflame.2026.115082)
- 分类：光学诊断、反演、烟炱与辐射 / 光谱、图像与层析反演
- JCR：**二级来源报告 Q1/Q2，JCR 版本待官方核实**；报告最佳分区 Q1；版本未知；官方核实：否。
- 阅读深度：已核对元数据与上游 README，尚未完成全文精读。
- 完整期刊论文复现：**尚未验收**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../05_diagnostics_radiation/README.md) · [全局地图](../../../00_literature_map/README.md)

分区线索：[二级来源](https://www.letpub.com/index.php?page=journalapp&view=detail&journalid=1901)。多类别期刊使用报告中的最佳类别作为候选信号，不能解释为所有类别均为 Q1。

## 研究问题

利用神经隐式表示从背景纹影观测重建三维折射率及火焰场。

## 方法与代码所能确认的内容

上游描述 MATLAB 几何/合成数据、Python NIR-BOS 训练、自定义 CUDA 射线积分及 hash/Fourier 编码。

## 复现入口与依赖

step1_InitBOSLAB.m → step2_Compile.m → step3_generate_phantom1_synthetic_data.m → PYTHON/NIR-BOS/main_BOS.py。

## 环境与数据

MATLAB、NVIDIA GPU/CUDA、environment.yml；当前上游明确不支持纯 CPU。

## 建议验证协议（本库设计）

检验相机几何、噪声、有限视角和非径向布置；分别比较观测重投影误差和三维场误差。

## 局限与当前状态

PolyForm Noncommercial 属可见源代码且限制商业使用，不能标为 OSI 开源。作者警告 CGLS 参考实现正反投影不匹配；该警告不等同于 NIR-BOS 本身有同一问题。本库仅提供链接。

## 代码溯源

- 仓库：[Weihu22/Neural-Implicit-Reconstruction-for-BOS](https://github.com/Weihu22/Neural-Implicit-Reconstruction-for-BOS)
- 固定提交：`344ccaf19b5fcecb9494e75e125d137682feb4a9`
- 关系证据：`author_implementation_readme_explicit`；来自上游 README，不代表本库已做作者身份独立认证。
- 许可：PolyForm-Noncommercial-1.0.0；收纳状态：`link_only`。
- [代码包卡片](../../../code_packages/Weihu22__Neural-Implicit-Reconstruction-for-BOS/README.md)

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1016/j.combustflame.2026.115082)；本轮整理日期 2026-11-12。完整元数据见同目录 `paper.json`。
