# 代码收纳与许可证

每个包在 `code_packages/<owner>__<repo>/` 记录来源、固定提交、许可证原文、论文关系与执行状态。`catalog/code_packages.json` 是统一清单。固定提交防止未来默认分支变动；SHA-256 验证本次实际下载的字节。GitHub 重新生成归档时压缩字节未必相同，提交仍是源码身份，需同时检查版本和文件内容。

## 三种收纳方式

1. 明确可再分发的 MIT / BSD / Apache / GPL / LGPL：保留原始许可；优先附小型源归档，大包保留不可变下载入口，或附明确标注的部分源码快照。
2. 未定位许可：只保留链接、元数据和中文解读，不镜像源文件。
3. 非商业等受限许可：明确记录，不标为 OSI 开源。本轮 NIR-BOS 是 PolyForm Noncommercial，BayeSAF 是 Prosperity Public License 3.0，均仅提供链接。

许可证原文属于上游；本库没有对其重新授权。第三方依赖、化学机理、实验数据、图片和模型权重需要各自检查。软件 GPL/LGPL 的义务不会因为用于科研而消失。

## 下载

```powershell
python -m pip install -r requirements-tools.txt
python tools/fetch_packages.py
python tools/fetch_packages.py --package TaoRen-Rad__WSGG-H2O-CO2-NH3
python tools/fetch_packages.py --all-licensed --max-mb 20
python tools/build_catalog.py
python tools/build_overview.py
```

默认选择优先包并限制每个归档 5 MiB；超过上限、网络失败或没有许可的包保留清晰状态。`archive.json` 记录下载 URL、时间、字节数、SHA-256 和错误。下载器不解压和执行，不含 Git 历史；Git LFS 文件和子模块可能只有指针。

部分源码快照由 `collect_source_subset.py` 生成；单文件至多 200000 bytes，总源文件至多 2000000 bytes，至多 160 个文件。所选源码、配置、README 与许可逐文件验证 Git blob 哈希，`source_snapshot.json` 保留排除路径。该快照不能视为完整上游发行包；数据、权重、大文件及未选中文件类型可能缺失。完整归档与部分源码在统计中分开计数。

## 运行前检查

按论文卡核对入口、机理、权重、数据路径和版本。`.pt`、pickle 等序列化文件只在来源可信的环境加载。运行后应记录实际命令、环境、输出、错误和对照。仅脚本正常退出并不等于论文结论复现。

DeepFlame 的部分权重需申请；DU_CNN 的数据位于外部网盘；CNpred 依赖旧 TensorFlow/nfp；NIR-BOS 需要 MATLAB/CUDA；POD-PINO 的发表/数据状态未核实。这些限制在各包/论文卡保留，不标成开箱即用。

## 原创内容与上游内容

本库新写的索引、中文说明、工具和独立基线与上游源归档分开存放。没有擅自替用户选择一个覆盖所有内容的统一许可证；对外再分发时请遵守各上游许可，若要明确授权本库原创部分，可后续另行决定。
