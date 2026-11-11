# gdalessi/OpenMORe

热化学空间降阶与聚类工具，适合自适应化学与流形建模。许可原文和对应论文需分别核对；属于支撑软件。

- [原始仓库](https://github.com/gdalessi/OpenMORe) · [固定版本](https://github.com/gdalessi/OpenMORe/tree/101ca4b461f7b25b55cbed05e6724702774eec43)
- 提交：`101ca4b461f7b25b55cbed05e6724702774eec43`
- 许可：**MIT**。
- 收纳状态：`partial_source_snapshot_collected`；执行状态：`not_executed`。
- 本包不自动安装、不自动运行。原始依赖、数据和子模块应在隔离环境逐项检查。

## 关联论文与入口

具体期刊论文对应关系尚未建立；按支撑工具、会议或预印本处理。

[上游 README（固定版本）](https://github.com/gdalessi/OpenMORe/blob/101ca4b461f7b25b55cbed05e6724702774eec43/README.md)

## 许可证与再分发

[上游许可](https://github.com/gdalessi/OpenMORe/blob/101ca4b461f7b25b55cbed05e6724702774eec43/LICENSE.txt)；同目录 UPSTREAM_LICENSE.txt 保留原文。依赖、训练数据及权重不自动继承源码许可。

## 获取固定版本

在仓库根目录执行：

```powershell
python tools/fetch_packages.py --package gdalessi__OpenMORe
```

下载器仅保存源归档和 SHA-256，不执行上游代码。已附归档时可离线核验；归档不含 Git 历史，子模块和 LFS 数据可能不完整。

完整归档本轮未收纳：`archive exceeds configured byte limit; use pinned upstream download`。这不表示上游未提供代码；固定下载入口仍可使用。

## 部分源码快照

已收纳 [101ca4b461f7-source-only.tar.gz](101ca4b461f7-source-only.tar.gz)，含 36 个源码/配置/说明/许可文件；SHA-256 `7f6c3ced71e0ad16544d1b6533d5bc1f575e9c22ef2a51028684a0317bac9afb`。

这是部分源码，省略大文件、数据、权重、图片和未选中文件，不能直接当作完整发行包或运行成功证据。逐文件 Git blob 与 SHA-256、全部排除路径见 [source_snapshot.json](source_snapshot.json)。
