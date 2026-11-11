# dynamicslab/dominant-balance

数据驱动主导平衡识别，包含旋转爆轰发动机的 Majda–Burgers 简化模型。其余海流/神经元示例仅为通用背景；燃烧实验需明确选择 RDE 子例。MIT。

- [原始仓库](https://github.com/dynamicslab/dominant-balance) · [固定版本](https://github.com/dynamicslab/dominant-balance/tree/41ac6d2e1feccb8f3a71591d4d1f9dcbfcd1e299)
- 提交：`41ac6d2e1feccb8f3a71591d4d1f9dcbfcd1e299`
- 许可：**MIT**。
- 收纳状态：`partial_source_snapshot_collected`；执行状态：`not_executed`。
- 本包不自动安装、不自动运行。原始依赖、数据和子模块应在隔离环境逐项检查。

## 关联论文与入口

- [Learning dominant physical processes with data-driven balance models](../../07_engineering_design/03_supersonic_detonation/P3fe49a4002/README.md) — 10.1038/s41467-021-21331-z

[上游 README（固定版本）](https://github.com/dynamicslab/dominant-balance/blob/41ac6d2e1feccb8f3a71591d4d1f9dcbfcd1e299/README.md)

## 许可证与再分发

[上游许可](https://github.com/dynamicslab/dominant-balance/blob/41ac6d2e1feccb8f3a71591d4d1f9dcbfcd1e299/LICENSE)；同目录 UPSTREAM_LICENSE.txt 保留原文。依赖、训练数据及权重不自动继承源码许可。

## 获取固定版本

在仓库根目录执行：

```powershell
python tools/fetch_packages.py --package dynamicslab__dominant-balance
```

下载器仅保存源归档和 SHA-256，不执行上游代码。已附归档时可离线核验；归档不含 Git 历史，子模块和 LFS 数据可能不完整。

完整归档本轮未收纳：`archive exceeds configured byte limit; use pinned upstream download`。这不表示上游未提供代码；固定下载入口仍可使用。

## 部分源码快照

已收纳 [41ac6d2e1fec-source-only.tar.gz](41ac6d2e1fec-source-only.tar.gz)，含 27 个源码/配置/说明/许可文件；SHA-256 `f0d26f415303e80c0b9939c8d081c5ce7814b9edfc3bdcbc5c38cb5f86fc624a`。

这是部分源码，省略大文件、数据、权重、图片和未选中文件，不能直接当作完整发行包或运行成功证据。逐文件 Git blob 与 SHA-256、全部排除路径见 [source_snapshot.json](source_snapshot.json)。
