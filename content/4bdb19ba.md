# Meganeura: Portable GPU Training and Inference through Vulkan and Metal

- **ID**: 4bdb19ba
- **原文链接**: https://arxiv.org/abs/2608.01563
- **PDF**: https://arxiv.org/pdf/2608.01563v1
- **作者**: Dzmitry Malyshau
- **日期**: 2026-08-03
- **更新**: N/A
- **分类**: infra
- **来源类型**: paper
- **标签**: vulkan, metal, gpu-compiler, train-to-deploy, android-xr, portability
- **质量评分**: 4/5
- **抓取时间**: 2026-08-17T23:51:34+08:00

---

## 中文导读

验证“单个紧凑原生编译器能否同时覆盖训练与部署推理”：类型化静态图、自动微分、优化器、checkpoint、内存规划与运行时，全部经 Vulkan/Metal 降低到消费级 GPU。五个匹配工作负载与 PyTorch 在 NVIDIA/AMD 独显、AMD APU、Apple silicon、Intel 核显上对比，严格 f32 与验证过的 fast path 分离、前向反向独立过门。裁剪后二进制 13 MiB；附 Android XR 实机案例——Meganeura 训练的解码器迁入 Adreno/OpenXR 应用并与图形共享 command queue。若该路线持续兑现，端侧 train-to-deploy 栈有去厂商化空间。

## 为什么值得关注

Vulkan/Metal 单编译器打通 train-to-deploy：13 MiB 二进制，Android XR 实机迁移案例。

**收录理由**：含 Android XR/Adreno/OpenXR 实机案例的跨厂商 GPU 栈验证，端侧 train-to-deploy 去厂商化路线图

## Abstract

Training and deployed inference often cross export, conversion, and platform-specific runtime boundaries. Meganeura asks whether one compact native compiler can span both phases on consumer GPUs. Its typed static graph, automatic differentiation, optimizer, checkpoint, memory planner, and runtime lower specialized programs through Vulkan and Metal. We compare five matched workloads with PyTorch on NVIDIA and AMD discrete GPUs, an AMD APU, Apple silicon, and an Intel iGPU. The protocol separates strict f32 from validated fast paths and gates forward and backward independently. Forty-eight of 50 device-workload-mode cells pass both gates; the other two share one unresolved backward-reference disagreement on a newly supported APU. In strict f32, Meganeura wins 12 of 20 GPU-referenced minimal-latency cells and has a median valid training gap of 1.8x. On the discrete AMD GPU, four of five inference workloads are within 1.10x of compiled ROCm PyTorch and three training workloads are faster. Under accelerated contracts, the worst training gap is 4.6x. Compilation takes 0.1-2.4 seconds versus 6-96 seconds for torch.compile on supported GPU paths; the stripped binary is 13 MiB. Dispatch profiles localize the largest gaps to convolution derivatives and attention backward. A physical Android XR case study transfers a Meganeura-trained decoder into an Adreno/OpenXR application sharing the graphics queue. The results show that general consumer graphics APIs can support a compact shared train-to-deploy stack at useful, sometimes vendor-competitive performance. The measured gaps point to kernel coverage, scheduling, and arithmetic policy rather than an identified API limitation.

## 元数据

- arXiv ID: 2608.01563
- 主分类: cs.LG
- 分类: cs.LG, cs.DC, cs.PL
- 评论: 18 pages, 4 figures, 10 tables

> Obsidian 证据：`OpenClaw定时任务/论文流水线/2026-08-17-论文流水线.md`（2026-08-17 周度回顾）；元数据抓取自 opencli arxiv paper 2608.01563（2026-08-17）。
