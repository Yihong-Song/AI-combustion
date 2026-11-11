# DENG-MIT/CRNN

通用化学反应网络发现及 Bayesian cathode 子项目；不同子项目环境不同。

- [原始仓库](https://github.com/DENG-MIT/CRNN) · [固定版本](https://github.com/DENG-MIT/CRNN/tree/4a17819c5bd4a65d6a9da9e72115b536d644350e)
- 提交：`4a17819c5bd4a65d6a9da9e72115b536d644350e`
- 许可：**MIT**。
- 收纳状态：`partial_source_snapshot_collected`；执行状态：`not_executed`。
- 本包不自动安装、不自动运行。原始依赖、数据和子模块应在隔离环境逐项检查。

## 关联论文与入口

- [Comprehensive thermal-kinetic uncertainty quantification of lithium-ion battery thermal runaway via bayesian chemical reaction neural networks](../../08_solid_fuels_fire/01_kinetics_fire/P81568f3c50/README.md) — 10.1016/j.cej.2025.160402
- [Uncertain lithium-ion cathode kinetic decomposition modeling via Bayesian chemical reaction neural networks](../../01_chemistry_kinetics/02_discovery_calibration/P2384b1472e/README.md) — 10.1016/j.proci.2024.105243

[上游 README（固定版本）](https://raw.githubusercontent.com/DENG-MIT/CRNN/4a17819c5bd4a65d6a9da9e72115b536d644350e/README.md)

## 许可证与再分发

[上游许可](https://raw.githubusercontent.com/DENG-MIT/CRNN/4a17819c5bd4a65d6a9da9e72115b536d644350e/LICENSE)；同目录 UPSTREAM_LICENSE.txt 保留原文。依赖、训练数据及权重不自动继承源码许可。

## 获取固定版本

在仓库根目录执行：

```powershell
python tools/fetch_packages.py --package DENG-MIT__CRNN
```

下载器仅保存源归档和 SHA-256，不执行上游代码。已附归档时可离线核验；归档不含 Git 历史，子模块和 LFS 数据可能不完整。

完整归档本轮未收纳：`archive exceeds configured byte limit; use pinned upstream download`。这不表示上游未提供代码；固定下载入口仍可使用。

## 部分源码快照

已收纳 [4a17819c5bd4-source-only.tar.gz](4a17819c5bd4-source-only.tar.gz)，含 41 个源码/配置/说明/许可文件；SHA-256 `ade9cf24507eba88f4ec366e8b1fa30cfa9a47e0020130d5f3d4142e36195889`。

这是部分源码，省略大文件、数据、权重、图片和未选中文件，不能直接当作完整发行包或运行成功证据。逐文件 Git blob 与 SHA-256、全部排除路径见 [source_snapshot.json](source_snapshot.json)。
