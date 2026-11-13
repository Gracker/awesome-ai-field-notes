# Start and Restore GPU Workloads in Seconds with NVIDIA Snapshot

- **ID**: a93eb8df
- **原文链接**: https://developer.nvidia.com/blog/start-and-restore-gpu-workloads-in-seconds-with-nvidia-snapshot/
- **作者**: Ron Kahn, Dan Feigin, Oz Bar-Shalom, Ekin Karabulut, Schwinn Saereesitthipitak (NVIDIA)
- **日期**: 2026-11-10
- **更新**: N/A
- **分类**: infra
- **来源类型**: article
- **标签**: nvidia, inference, snapshot, cold-start, gpu, kubernetes
- **质量评分**: 3/5
- **抓取时间**: 2026-11-13T15:45:09+00:00

---

## 中文导读

NVIDIA 开源 Snapshot：Kubernetes 上 GPU 工作负载的 checkpoint/restore 系统，捕获完全初始化的 CPU+GPU 内存状态。官方数字：推理副本 3.6–42.7 秒上线，比分钟级冷启动快 8–36 倍；支持张量/数据/专家/解码上下文并行，MoE 模型 checkpoint 最高 1TB（8 卡）；checkpoint 创建 15 秒–5.5 分钟，每种受测配置里 checkpoint+restore 总时间都短于一次冷启动。agent 评测农场、突发扩容、故障拉起都吃冷启动，这篇给的是可直接核对的数字表。

## 为什么值得关注

推理副本秒级恢复把 agent 评测农场与突发扩容的冷启动成本打下来：先读官方 3.6–42.7s 表，再对存储后端与并行方式。

中文导读与价值判断锚定在条目已有摘要与抓取到的原文/摘要、作者、日期与分类信息上；未补充源材料之外的实验细节。

## 关键信息

- 标题：Start and Restore GPU Workloads in Seconds with NVIDIA Snapshot
- 作者：Ron Kahn, Dan Feigin, Oz Bar-Shalom, Ekin Karabulut, Schwinn Saereesitthipitak (NVIDIA)
- 链接：https://developer.nvidia.com/blog/start-and-restore-gpu-workloads-in-seconds-with-nvidia-snapshot/
- 发布时间：2026-11-10
- 关联标签：nvidia, inference, snapshot, cold-start, gpu, kubernetes

## English Summary

NVIDIA Snapshot is an open-source checkpoint/restore system for GPU workloads on Kubernetes that captures fully initialized CPU and GPU memory state. Restoring an inference replica takes 3.6-42.7 seconds across tested configurations - 8x to 36x faster than minutes-long cold starts. It supports tensor, data and expert parallelism plus decode context parallelism for large MoE models, with checkpoints up to 1 TB across eight GPUs; checkpoint creation runs 15 seconds to 5.5 minutes, and checkpoint-plus-restore beats a single cold start in every tested configuration.

## 原文摘录 / Evidence Excerpts

NVIDIA Snapshot is an open-source checkpoint and restore system for GPU workloads on Kubernetes that captures fully initialized CPU and GPU memory state. Restoring from a Snapshot artifact brings inference replicas online in 3.6 to 42.7 seconds across tested configurations, delivering 8x to 36x speedups over cold starts that take minutes.

The system supports multi-GPU workloads using tensor parallelism, data and expert parallelism, and decode context parallelism for large mixture-of-experts models with checkpoints up to 1 TB across eight GPUs. Checkpoint creation takes 15 seconds to 5.5 minutes depending on model size, and the combined checkpoint-plus-restore time is shorter than a single cold start in every tested configuration.

---

## 证据来源

curl 直接抓取 NVIDIA Technical Blog（2026-11-13，272KB HTML）。作者署名与日期（Nov 10, 2026, By Ron Kahn, Dan Feigin, Oz Bar-Shalom, Ekin Karabulut and Schwinn Saereesitthipitak）来自页面原文。
