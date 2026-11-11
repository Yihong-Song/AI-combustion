# ECRL/ECNet

燃料性质 QSPR 工具；JOSS 2017 论文描述旧架构，当前 v4 API 以现有文档为准。

- [原始仓库](https://github.com/ECRL/ECNet) · [固定版本](https://github.com/ECRL/ECNet/tree/96ee90820550fad79f96a260a0373ab1098870bb)
- 提交：`96ee90820550fad79f96a260a0373ab1098870bb`
- 许可：**MIT**。
- 收纳状态：`partial_source_snapshot_collected`；执行状态：`not_executed`。
- 本包不自动安装、不自动运行。原始依赖、数据和子模块应在隔离环境逐项检查。

## 关联论文与入口

具体期刊论文对应关系尚未建立；按支撑工具、会议或预印本处理。

[上游 README（固定版本）](https://github.com/ecrl/ecnet/blob/96ee90820550fad79f96a260a0373ab1098870bb/README.md)

## 许可证与再分发

[上游许可](https://github.com/ecrl/ecnet/blob/96ee90820550fad79f96a260a0373ab1098870bb/LICENSE.txt)；同目录 UPSTREAM_LICENSE.txt 保留原文。依赖、训练数据及权重不自动继承源码许可。

## 获取固定版本

在仓库根目录执行：

```powershell
python tools/fetch_packages.py --package ECRL__ECNet
```

下载器仅保存源归档和 SHA-256，不执行上游代码。已附归档时可离线核验；归档不含 Git 历史，子模块和 LFS 数据可能不完整。

完整归档本轮未收纳：`archive exceeds configured byte limit; use pinned upstream download`。这不表示上游未提供代码；固定下载入口仍可使用。

## 部分源码快照

已收纳 [96ee90820550-source-only.tar.gz](96ee90820550-source-only.tar.gz)，含 72 个源码/配置/说明/许可文件；SHA-256 `9fec414c94280a9342ce8ce9e68bf32d987472ad9687624eea674c0fb4cb4cf5`。

这是部分源码，省略大文件、数据、权重、图片和未选中文件，不能直接当作完整发行包或运行成功证据。逐文件 Git blob 与 SHA-256、全部排除路径见 [source_snapshot.json](source_snapshot.json)。
