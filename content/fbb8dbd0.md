# Spool: Low-Latency Streaming Inference for Hybrid Vision-Language Models

- **ID**: fbb8dbd0
- **原文链接**: https://arxiv.org/abs/2611.23228
- **PDF**: https://arxiv.org/pdf/2611.23228v1
- **作者**: Rui Ning, Om Chabra, Hari Balakrishnan
- **日期**: 2026-11-17
- **更新**: 2026-11-17
- **分类**: infra
- **来源类型**: paper
- **标签**: inference, streaming, vlm, sliding-window, gdn
- **质量评分**: 4/5
- **抓取时间**: 2026-11-19T12:23:46Z

---

## 中文导读

视觉无障碍代理、机器人等应用要在有界帧窗口（如最近两分钟）内低延迟回答视频问题；注意力与 GDN 等线性循环层交织的混合 VLM 维护滑窗代价高，因为循环层把全部历史压进共享状态，过期帧通常要把整窗重跑一遍才能清除。作者观察到循环更新对状态是仿射的、系数依赖输入，每帧效果可表示为可结合复合的变换；Spool 免训练地缓存每帧状态变换并随窗口推进高效复合，无需重放主干即从每层循环状态精确移除过期帧，配合专用数据结构与 GPU kernel 控制开销。五个开源混合 VLM、四个视频推理基准共 20 组测试中 p95 首 token 延迟全部最低，较两个 vLLM 基线中更快者几何平均降低 6.6 倍，准确率平均还提高 2.3 个百分点。

## 为什么值得关注

混合注意力+线性 RNN 架构流式部署的核心痛点是“如何从循环状态里清理历史”；把每帧效果建模为可复合仿射变换、免训练做精确滑窗，是可直接复用的 infra 工程结果，且延迟与精度同时受益。

arXiv 2026-11 推理系统研究：作者 Rui Ning、Om Chabra、Hari Balakrishnan，针对 hybrid VLM 在 vLLM 下的滑窗重放瓶颈给出训练免改造方案。

## 关键信息

- 论文标题：Spool: Low-Latency Streaming Inference for Hybrid Vision-Language Models
- 作者：Rui Ning, Om Chabra, Hari Balakrishnan
- arXiv: https://arxiv.org/abs/2611.23228
- 发布时间：2026-11-17
- arXiv 分类：cs.CV, cs.LG
- 关联标签：inference, streaming, vlm, sliding-window, gdn

## English Abstract

Applications such as visual accessibility agents and robotics require answering questions about recent video content promptly, over a bounded window of past frames (e.g., the last two minutes). Hybrid vision-language models (VLMs), which interleave attention with linear recurrent layers such as Gated DeltaNet (GDN), are attractive for this setting, but maintaining a sliding window is expensive. The reason is that recurrent layers combine all past frames into a shared state, so expiring old frames normally requires re-running the entire window through the model. We observe that the recurrent update is affine in the state with input-dependent coefficients, so the effect of each frame can be captured as a transformation that composes associatively. We present Spool, a training-free framework that caches per-frame state transformations and composes them efficiently as the window advances, removing expired frames from each recurrent layer's state without replaying frames through the backbone. Removal is exact within each layer; as with key-value eviction in attention, expired frames can retain residual influence through the cached inputs computed by earlier layers. We design a dedicated data structure and GPU kernels to achieve low caching and composition overhead. Across five open-source hybrid VLMs and four video reasoning benchmarks, Spool achieves the lowest p95 time-to-first-token in all 20 model-benchmark tests, reducing it by a geometric mean of $6.6\times$ over the faster of two recent vLLM baselines, while improving accuracy by 2.3 percentage points on average.

## English Summary

Hybrid VLMs that interleave attention with linear recurrent layers like Gated DeltaNet suit streaming video QA over bounded windows, but sliding windows are expensive: recurrent layers fold all past frames into one shared state, so expiring frames normally means replaying the whole window. Spool exploits that the recurrent update is affine in the state with input-dependent coefficients, so each frame's effect is a transformation that composes associatively. Training-free, it caches per-frame state transformations and composes them as the window advances, removing expired frames from each recurrent layer's state without replaying them. Across five open hybrid VLMs and four video benchmarks, Spool has the lowest p95 time-to-first-token in all 20 model-benchmark tests — 6.6x geometric-mean lower than the faster of two vLLM baselines — while improving accuracy 2.3 points on average.

## Obsidian Notes

- 内容由 `opencli arxiv paper` 拉取 arXiv 元数据与摘要生成。
- 中文导读与价值判断均锚定在条目已有摘要、论文摘要、作者、日期与分类信息上；未补充论文摘要之外的实验细节。
