# deepflameCFD/deepflame-dev

OpenFOAM/Cantera/LibTorch 反应流框架；README 的部分 DNN 权重需向作者申请，不能保证直接运行。

- [原始仓库](https://github.com/deepflameCFD/deepflame-dev) · [固定版本](https://github.com/deepflameCFD/deepflame-dev/tree/29529093a73717fcac676f1f1ceed24c0cc932c7)
- 提交：`29529093a73717fcac676f1f1ceed24c0cc932c7`
- 许可：**GPL-3.0 (inspect upstream terms)**。
- 收纳状态：`source_archive_collected`；执行状态：`not_executed`。
- 本包不自动安装、不自动运行。原始依赖、数据和子模块应在隔离环境逐项检查。

## 关联论文与入口

- [DeepFlame: A deep learning empowered open-source platform for reacting flow simulations](../../01_chemistry_kinetics/01_surrogates_reduction/P9b9c10a9d8/README.md) — 10.1016/j.cpc.2023.108842

[上游 README（固定版本）](https://raw.githubusercontent.com/deepflameCFD/deepflame-dev/29529093a73717fcac676f1f1ceed24c0cc932c7/README.md)

## 许可证与再分发

[上游许可](https://raw.githubusercontent.com/deepflameCFD/deepflame-dev/29529093a73717fcac676f1f1ceed24c0cc932c7/LICENSE)；同目录 UPSTREAM_LICENSE.txt 保留原文。依赖、训练数据及权重不自动继承源码许可。

## 获取固定版本

在仓库根目录执行：

```powershell
python tools/fetch_packages.py --package deepflameCFD__deepflame-dev
```

下载器仅保存源归档和 SHA-256，不执行上游代码。已附归档时可离线核验；归档不含 Git 历史，子模块和 LFS 数据可能不完整。

已收纳文件：[29529093a737.tar.gz](29529093a737.tar.gz)；大小 7714325 bytes；SHA-256 `42b519be3f18f9fc0532b4a02799ffe2eee156c546119b20635dcdb0f0bded0f`。

## 部分源码快照

已收纳 [29529093a737-source-only.tar.gz](29529093a737-source-only.tar.gz)，含 160 个源码/配置/说明/许可文件；SHA-256 `d2a1e2761fa057737d1e1648fe4e6a762fa74ba674fd72a878ba8f3793e59bf2`。

这是部分源码，省略大文件、数据、权重、图片和未选中文件，不能直接当作完整发行包或运行成功证据。逐文件 Git blob 与 SHA-256、全部排除路径见 [source_snapshot.json](source_snapshot.json)。
