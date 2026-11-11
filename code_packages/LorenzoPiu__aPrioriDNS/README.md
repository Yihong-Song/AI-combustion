# LorenzoPiu/aPrioriDNS

DNS 滤波与 a priori 评估工具；README 指向 PaSR 方法论文，软件论文尚在准备。

- [原始仓库](https://github.com/LorenzoPiu/aPrioriDNS) · [固定版本](https://github.com/LorenzoPiu/aPrioriDNS/tree/19bb0fa13fb068c4bd74bed1f8deae35708514b6)
- 提交：`19bb0fa13fb068c4bd74bed1f8deae35708514b6`
- 许可：**GPL-3.0 (inspect upstream terms)**。
- 收纳状态：`partial_source_snapshot_collected`；执行状态：`not_executed`。
- 本包不自动安装、不自动运行。原始依赖、数据和子模块应在隔离环境逐项检查。

## 关联论文与入口

- [A Data-Driven Approach to Refine the Partially Stirred Reactor Closure for Turbulent Premixed Flames](../../02_turbulence_closure/01_closures_manifolds/P8badc7f206/README.md) — 10.1007/s10494-024-00626-3

[上游 README（固定版本）](https://github.com/LorenzoPiu/aPriori/blob/19bb0fa13fb068c4bd74bed1f8deae35708514b6/README.md)

## 许可证与再分发

[上游许可](https://github.com/LorenzoPiu/aPriori/blob/19bb0fa13fb068c4bd74bed1f8deae35708514b6/LICENSE)；同目录 UPSTREAM_LICENSE.txt 保留原文。依赖、训练数据及权重不自动继承源码许可。

## 获取固定版本

在仓库根目录执行：

```powershell
python tools/fetch_packages.py --package LorenzoPiu__aPrioriDNS
```

下载器仅保存源归档和 SHA-256，不执行上游代码。已附归档时可离线核验；归档不含 Git 历史，子模块和 LFS 数据可能不完整。

完整归档本轮未收纳：`archive exceeds configured byte limit; use pinned upstream download`。这不表示上游未提供代码；固定下载入口仍可使用。

## 部分源码快照

已收纳 [19bb0fa13fb0-source-only.tar.gz](19bb0fa13fb0-source-only.tar.gz)，含 123 个源码/配置/说明/许可文件；SHA-256 `9cadaabd1124f04c1ceb726915ab47366e7397526883315e980c8e37d5d28630`。

这是部分源码，省略大文件、数据、权重、图片和未选中文件，不能直接当作完整发行包或运行成功证据。逐文件 Git blob 与 SHA-256、全部排除路径见 [source_snapshot.json](source_snapshot.json)。
