# beroudiauxa/ORCh_2023

ORCh 化学优化/缩减框架，README 明确列化学缩减及 ANN/CNN 相关工作。旧 Cantera 2.4、SUNDIALS、OpenCV、MPI 和编译依赖复杂；不直接混装当前环境。BSD-3-Clause。

- [原始仓库](https://github.com/beroudiauxa/ORCh_2023) · [固定版本](https://github.com/beroudiauxa/ORCh_2023/tree/1a1b5175078340cbd4585f0ef597a821aa262de4)
- 提交：`1a1b5175078340cbd4585f0ef597a821aa262de4`
- 许可：**BSD-3-Clause**。
- 收纳状态：`partial_source_snapshot_collected`；执行状态：`not_executed`。
- 本包不自动安装、不自动运行。原始依赖、数据和子模块应在隔离环境逐项检查。

## 关联论文与入口

- [Chemistry reduction using machine learning trained from non-premixed micro-mixing modeling: Application to DNS of a syngas turbulent oxy-flame with side-wall effects](../../01_chemistry_kinetics/01_surrogates_reduction/Pe1482ded9f/README.md) — 10.1016/j.combustflame.2020.06.008

[上游 README（固定版本）](https://github.com/beroudiauxa/ORCh_2023/blob/1a1b5175078340cbd4585f0ef597a821aa262de4/README.md)

## 许可证与再分发

[上游许可](https://github.com/beroudiauxa/ORCh_2023/blob/1a1b5175078340cbd4585f0ef597a821aa262de4/LICENSE)；同目录 UPSTREAM_LICENSE.txt 保留原文。依赖、训练数据及权重不自动继承源码许可。

## 获取固定版本

在仓库根目录执行：

```powershell
python tools/fetch_packages.py --package beroudiauxa__ORCh_2023
```

下载器仅保存源归档和 SHA-256，不执行上游代码。已附归档时可离线核验；归档不含 Git 历史，子模块和 LFS 数据可能不完整。

完整归档本轮未收纳：`archive exceeds configured byte limit; use pinned upstream download`。这不表示上游未提供代码；固定下载入口仍可使用。

## 部分源码快照

已收纳 [1a1b51750783-source-only.tar.gz](1a1b51750783-source-only.tar.gz)，含 160 个源码/配置/说明/许可文件；SHA-256 `b7b5d43436e4c9d94111b2e66c74f571eb7a722c915225c2138a4e620246333f`。

这是部分源码，省略大文件、数据、权重、图片和未选中文件，不能直接当作完整发行包或运行成功证据。逐文件 Git blob 与 SHA-256、全部排除路径见 [source_snapshot.json](source_snapshot.json)。
