# DeepFlame: A deep learning empowered open-source platform for reacting flow simulations

P9b9c10a9d8 · 2023 · Computer Physics Communications

作者：Runze Mao; Minqi Lin; Yan Zhang; Tianhan Zhang; Zhi-Qin John Xu; Zhi X. Chen

- DOI：[原文入口](https://doi.org/10.1016/j.cpc.2023.108842)
- 分类：化学动力学代理、缩减与机理发现 / 代理与缩减
- JCR：**JCR 分区待核实**；报告最佳分区 未知；版本未知；官方核实：否。
- 阅读深度：已核对元数据与上游 README，尚未完成全文精读。
- 完整期刊论文复现：**尚未验收**。
- [统一方法与证据等级](../../../docs/METHODOLOGY.md) · [方向说明](../../../01_chemistry_kinetics/README.md) · [全局地图](../../../00_literature_map/README.md)

## 研究问题

构建深度学习与传统反应流求解耦合的开源平台。

## 方法与代码所能确认的内容

DFODE-kit 的 Related papers 明确列此 DOI 对应的平台论文，并链接 DeepFlame。已固定的旧 deepflameCFD README 则给出平台引用而未列最终 DOI，因此保留生态相关实现关系，等待发表版与具体提交对齐。

## 复现入口与依赖

先检查上游安装文档、bashrc、求解器和 tutorials，再选择一个与论文版本一致的典型反应流案例。

## 环境与数据

兼容的 OpenFOAM、Cantera、LibTorch、编译器和 MPI；旧提交的环境不能直接用本机 OpenFOAM 13 替代。

## 建议验证协议（本库设计）

在相同网格、数值格式和化学误差阈值下，对比传统积分与 DNN 耦合的物理量、求解失败率和全链路耗时。

## 局限与当前状态

部分网络权重上游说明需向作者申请；固定主分支不是自动等同论文发布版本。未执行本论文算例。

## 代码溯源

- 仓库：[deepflameCFD/deepflame-dev](https://github.com/deepflameCFD/deepflame-dev)
- 固定提交：`29529093a73717fcac676f1f1ceed24c0cc932c7`
- 关系证据：`author_related_work_readme_explicit`；来自上游 README，不代表本库已做作者身份独立认证。
- 许可：GPL-3.0 (inspect upstream terms)；收纳状态：`source_archive_collected`。
- [代码包卡片](../../../code_packages/deepflameCFD__deepflame-dev/README.md)

## 待完成的学术核验

- 官方 JCR 年份、类别、排名与分区证据。
- 原文数据范围、训练/测试切分、主要定量结论、消融与误差条。
- 代码—论文版本一致性，数据及预训练权重是否齐全。
- 论文指标同口径复现及差异分析。

元数据来源：[Crossref](https://api.crossref.org/works/10.1016/j.cpc.2023.108842)；本轮整理日期 2026-11-12。完整元数据见同目录 `paper.json`。
