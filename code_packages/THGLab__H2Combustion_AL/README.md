# THGLab/H2Combustion_AL

氢燃烧反应的主动学习与 NewtonNet 分子势工具。入口 script/demo/md_demo.py；训练使用 md/active_learning/active_learning.py 与 YAML，含 HPC 本地路径。论文 DOI 尚未确认；MIT。

- [原始仓库](https://github.com/THGLab/H2Combustion_AL) · [固定版本](https://github.com/THGLab/H2Combustion_AL/tree/a42833dac8d9f671393527f07d7335fe16c23300)
- 提交：`a42833dac8d9f671393527f07d7335fe16c23300`
- 许可：**MIT**。
- 收纳状态：`partial_source_snapshot_collected`；执行状态：`not_executed`。
- 本包不自动安装、不自动运行。原始依赖、数据和子模块应在隔离环境逐项检查。

## 关联论文与入口

具体期刊论文对应关系尚未建立；按支撑工具、会议或预印本处理。

[上游 README（固定版本）](https://github.com/THGLab/H2Combustion_AL/blob/a42833dac8d9f671393527f07d7335fe16c23300/README.md)

## 许可证与再分发

[上游许可](https://github.com/THGLab/H2Combustion_AL/blob/a42833dac8d9f671393527f07d7335fe16c23300/LICENSE)；同目录 UPSTREAM_LICENSE.txt 保留原文。依赖、训练数据及权重不自动继承源码许可。

## 获取固定版本

在仓库根目录执行：

```powershell
python tools/fetch_packages.py --package THGLab__H2Combustion_AL
```

下载器仅保存源归档和 SHA-256，不执行上游代码。已附归档时可离线核验；归档不含 Git 历史，子模块和 LFS 数据可能不完整。

完整归档本轮未收纳：`archive exceeds configured byte limit; use pinned upstream download`。这不表示上游未提供代码；固定下载入口仍可使用。

## 部分源码快照

已收纳 [a42833dac8d9-source-only.tar.gz](a42833dac8d9-source-only.tar.gz)，含 49 个源码/配置/说明/许可文件；SHA-256 `9c93ec3759ece547a92047fe4469d8a95c09186f8b3a6fbc727452b2bdc5ae88`。

这是部分源码，省略大文件、数据、权重、图片和未选中文件，不能直接当作完整发行包或运行成功证据。逐文件 Git blob 与 SHA-256、全部排除路径见 [source_snapshot.json](source_snapshot.json)。
