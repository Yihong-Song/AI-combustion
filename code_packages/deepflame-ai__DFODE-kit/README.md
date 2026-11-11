# deepflame-ai/DFODE-kit

论文对应与入口见关联论文卡。

- [原始仓库](https://github.com/deepflame-ai/DFODE-kit) · [固定版本](https://github.com/deepflame-ai/DFODE-kit/tree/bc65e84bc7644675b9996e3eea08f0d38cbceaad)
- 提交：`bc65e84bc7644675b9996e3eea08f0d38cbceaad`
- 许可：**GPL-3.0 (inspect upstream terms)**。
- 收纳状态：`partial_source_snapshot_collected`；执行状态：`not_executed`。
- 本包不自动安装、不自动运行。原始依赖、数据和子模块应在隔离环境逐项检查。

## 关联论文与入口

- [DFODE-Kit: Deep learning package for solving flame chemical kinetics with high-dimensional stiff ordinary differential equations](../../01_chemistry_kinetics/01_surrogates_reduction/P485814185d/README.md) — 10.1016/j.cpc.2025.110013
- [Enhancing deep learning of ammonia/natural gas combustion kinetics via physics-aware data augmentation and scale separation](../../01_chemistry_kinetics/01_surrogates_reduction/P208595837d/README.md) — 10.1016/j.fuel.2026.138904
- [Comprehensive deep learning for combustion chemistry integration: Multi-fuel generalization and a posteriori validation in reacting flow](../../01_chemistry_kinetics/01_surrogates_reduction/Pdd9a1fb317/README.md) — 10.1063/5.0248582

[上游 README（固定版本）](https://github.com/deepflame-ai/DFODE-kit/blob/bc65e84bc7644675b9996e3eea08f0d38cbceaad/README.md)

## 许可证与再分发

[上游许可](https://github.com/deepflame-ai/DFODE-kit/blob/bc65e84bc7644675b9996e3eea08f0d38cbceaad/LICENSE)；同目录 UPSTREAM_LICENSE.txt 保留原文。依赖、训练数据及权重不自动继承源码许可。

## 获取固定版本

在仓库根目录执行：

```powershell
python tools/fetch_packages.py --package deepflame-ai__DFODE-kit
```

下载器仅保存源归档和 SHA-256，不执行上游代码。已附归档时可离线核验；归档不含 Git 历史，子模块和 LFS 数据可能不完整。

完整归档本轮未收纳：`archive exceeds configured byte limit; use pinned upstream download`。这不表示上游未提供代码；固定下载入口仍可使用。

## 部分源码快照

已收纳 [bc65e84bc764-source-only.tar.gz](bc65e84bc764-source-only.tar.gz)，含 99 个源码/配置/说明/许可文件；SHA-256 `946ae6234ac2636a845292ad4c3c9201ce5d572af17888916cfa833371106568`。

这是部分源码，省略大文件、数据、权重、图片和未选中文件，不能直接当作完整发行包或运行成功证据。逐文件 Git blob 与 SHA-256、全部排除路径见 [source_snapshot.json](source_snapshot.json)。
