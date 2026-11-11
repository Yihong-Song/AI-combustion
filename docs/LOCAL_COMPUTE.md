# 本机 GPU 与复现环境核验

核验日期：2026-11-12。

最新安排：用户要求先扩充论文与开源工作，复现留待次日服务器；因此暂停 GPU 环境安装和新训练。本文件保留已观测事实，不能把安装文档支持写作本机 GPU 训练实测通过。

本机有 **AMD Radeon RX 9060 XT** 独立显卡，另有 Intel 集显。此前只检查了 PyTorch 的 CUDA 状态；`False` 不代表没有 GPU。Windows 当前科研 Python 为 3.13.9、`torch 2.13.0+cpu`，因此现有这个环境确实只运行 CPU。

## 观测与边界

| 项目 | 实际观测 |
|---|---|
| 独立显卡 | AMD Radeon RX 9060 XT，Windows 驱动 32.0.31044.16 |
| CPU / RAM | 32 逻辑 CPU，约 68.3 GB RAM |
| 当前 PyTorch | 2.13.0+cpu，未编入 CUDA/HIP |
| WSL | 已有 Ubuntu 26.04、WSL2，存在 `/dev/dxg` |
| WSL ROCm | 发现发行版提供的 HIP 7.1 运行库，未确认 GPU 训练可用 |
| 实际训练 | C02 先使用 CPU 完成训练；不能标成 GPU 实测 |

Windows CIM 的 AdapterRAM 字段可能截断，不以该字段声称真实显存容量。使用支持的运行时识别后再记录设备总显存。

## 官方安装路径的版本差异

旧 [Radeon Windows 7.2.1 限制页](https://rocm.docs.amd.com/projects/radeon-ryzen/en/latest/docs/limitations/limitationsrad.html) 写明不支持 ML 训练，仅 Python 3.12。该站已提示文档迁移，不能把旧限制泛化为 AMD GPU 或所有后续版本不能训练。

当前 [统一 ROCm 安装页](https://rocm.docs.amd.com/en/latest/install/rocm.html) 列出 RX 9060 XT / gfx1200，提供 Python 虚拟环境安装方法；[ROCDXG 仓库说明](https://github.com/ROCm/librocdxg) 已迁往 rocm-systems，并列出 Ubuntu 26.04 的 WSL 路径。应结合具体发布版、驱动和 PyTorch wheel 验证，不能只凭旧页面或型号列表保证全部训练操作可用。

优先使用独立环境，避免覆盖现有可运行的 CPU 基线依赖。只有以下实测全部通过，才把对应论文任务切到 GPU：

1. 框架报告设备名与显存，确认使用独显。
2. 矩阵乘法与 CPU 结果在声明的精度/容差内一致。
3. 小网络完整前向、反向与优化器更新。
4. PINN 的二阶自动微分及 float64 数值校验。
5. 小规模真实训练对照，记录精度、速度、内存与异常。

若环境不支持某些高阶梯度或双精度，按任务保留 CPU/服务器路径；不能把模型改为低精度后仍声称完全相同的数值协议。
