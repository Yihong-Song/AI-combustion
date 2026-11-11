# 如何继续扩充与复现

本库保留候选和核验状态，数量随证据增长。增加一篇论文不等于增加一个成功复现；同一仓库关联多篇文章也只计一个代码包。

## 下载后的离线使用

克隆后即可阅读方向、逐篇卡片、BibTeX、CSV 和实验结果。`00_literature_map/explorer.html` 内置目录数据，直接用浏览器打开，不访问外部脚本。相对路径论文链接需要保留仓库目录结构。GitHub 网页不执行这个 HTML。

```powershell
python tools/validate.py
python tools/build_catalog.py
python tools/build_overview.py
python tools/validate.py
python tools/check_offline_rebuild.py
```

校验的 Python 端仅使用标准库；文件清单由 Git 取得，因此需安装 Git 并在克隆目录内执行。若原始检索缓存不在本机，建库器从已发布的 `catalog/papers.json` 重建；许可证使用包中保留的原文。发现过期分类文件时校验会失败，应核对 DOI 后移除旧卡片，再生成索引。建库器不会擅自清理用户写的笔记。

离线重建检查会将可发布文件复制到临时目录，在没有忽略缓存的情况下执行两个建库器，逐文件比较字节，再自动清理临时目录。运行前应等所有下载和文件编辑结束，避免把同时新增的归档误判为重建差异。结果见 `evidence/offline_rebuild.json`。

## 扩充一轮检索

1. 安装 `requirements-tools.txt`。运行 `discover.py`、`expand_search.py`、`expand_depth.py`、`add_key_papers.py`，保留 URL、时间和失败记录。原始大缓存被 Git 忽略，发布的检索式与排除表位于 `evidence/screening.json`。
2. 运行 `screen.py`；检查边界主题与重复 DOI。现有脚本主要依赖题名，下一步需要摘要、全文和前后向引文检索。不要为了增加数量把无关能源论文纳入。
3. 运行 `search_paper_code.py`；DOI 命中可能只是引用。逐个阅读上游 README，与 DOI、题名和作者声明对照，再编辑 `literature/curation.json`。没有许可的代码只保留固定链接。
4. 用 `enrich_upstream.py --repo owner/repository` 取得提交、README 和许可。官方 JCR 记录应填写年度、类别、排名、分区及证据；没有官方版本时继续标待核实，不能用 SJR 替换。
5. 运行两个建库器、下载选定归档，再重新建库使统计与文件一致。最后运行校验，人工复核新增条目。

网络重试应有边界。速率限制、下载体积超限与数据需申请是不同原因。5 MiB 仅是本库下载器的默认限制，不说明上游文件不可访问。

## 收纳代码

```powershell
python tools/fetch_packages.py --package TaoRen-Rad__WSGG-H2O-CO2-NH3
python tools/collect_source_subset.py --package CAME-THU__FlamePINN-1D
```

第一条收纳固定提交的完整 GitHub 源归档；它仍可能缺 LFS、子模块或外部数据。第二条只收纳部分源码/配置/说明/许可，明确列出每个省略路径，不能充当完整可运行分发。两者均记录 SHA-256；部分源码额外验证 Git blob 哈希。下载工具不执行上游文件。

## 从演示走向论文复现

先选择原文一张表或一幅图，提取完整设置，再审查源代码。每篇应独立环境，记录数据版本、机理、物性、单位、边界、随机种子、设备和总预算。基准训练/测试切分与原文不同时，应叫独立基线或改编实验。

目前 B01/B02 是独立基线，C01 是固定提交的作者推理演示，均不是原始论文指标复现。C01 预存的 LBL 参考来自作者，本库未独立计算。校验器从保存的预测 CSV 重算误差，可以检测结果文件不一致，但不能证明物理模型正确，也不能从离散 CSV 验证 B02 自动微分残差。

后续优先路线：C01 多工况辐射验证 → FlamePINN 的简化正逆问题 → SL-GPS 的自燃与组分筛选 → CMLM 的流形代理 → CRNN 的不确定度 → DeepFlame 的后验 CFD。每一步以数据、依赖和目标图表实际可获得为前提。

[返回首页](../README.md) · [证据等级](METHODOLOGY.md) · [复现协议](REPRODUCTION_PROTOCOL.md)
