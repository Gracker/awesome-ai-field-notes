# TRACE: Rollout-Guided Quantization-Aware Training for FP4 Reinforcement Learning of MoE Language Models

- **ID**: d82f3ffa
- **原文链接**: https://arxiv.org/abs/2610.07767
- **PDF**: https://arxiv.org/pdf/2610.07767
- **作者**: Xin Wang, Hao Yu, Zhengyang Zhuge, Bochao Mao, Zheng Li, Junda Feng, Yuyan Luo, Yi Zhang, Yizhong Cao, Mi Zhang, Dayiheng Liu, Jianwei Zhang
- **日期**: 2026-10-06
- **更新**: 2026-10-06
- **分类**: models
- **来源类型**: paper
- **标签**: quantization, fp4, reinforcement-learning, moe, rollout, arxiv
- **质量评分**: 4/5
- **抓取时间**: 2026-10-07T15:55:28Z

---

## 中文导读

RL 后训练的大头开销在 rollout 生成，所以低精度 rollout 是自然的省法；但现有 FP4 RL 方法的共同缺陷是把训练路径与 rollout 路径的量化精度各自独立优化，而不是直接压小两条量化执行路径之间的偏差。TRACE（Train-Rollout Quantization Alignment via Compact GuidancE）的做法是 rollout 引导的量化感知训练：用 rollout 侧的量化结果指导训练侧的 FP4 舍入决策，直接缩小 train-rollout discrepancy；再用量化信息缓存方案选择性保留深层的尾数与 scale 信息，压低 rollout 指引带来的存储与通信开销。在四个大规模 MoE 模型、推理/编码/长程 RL 任务上：FP4 权重+激活+FP4 KV cache 的联合 rollout 达到与 BF16 rollout 相当的 RL 性能，rollout 最高 5.4x 加速，且最终 FP4 性能明显好于对 BF16 训练策略做事后 FP4 量化。

## 为什么值得关注

FP4 rollout 追平 BF16 RL 性能是这个方向的实用门槛：5.4x rollout 加速加『事后量化不如训练时对齐』的对照结论，对 RL 训练基础设施的成本结构有直接参考价值。

## 关键信息

- 论文标题：TRACE: Rollout-Guided Quantization-Aware Training for FP4 Reinforcement Learning of MoE Language Models
- 作者：Xin Wang, Hao Yu, Zhengyang Zhuge, Bochao Mao, Zheng Li, Junda Feng, Yuyan Luo, Yi Zhang, Yizhong Cao, Mi Zhang, Dayiheng Liu, Jianwei Zhang
- arXiv：https://arxiv.org/abs/2610.07767
- 发布时间：2026-10-06
- arXiv 分类：cs.LG, cs.CL
- 关联标签：quantization, fp4, reinforcement-learning, moe, rollout, arxiv

## English Abstract

Reinforcement learning (RL) for post-training large language models (LLMs) incurs substantial computation and memory overhead during rollout generation, which motivates low-precision rollout for efficient RL training. However, existing FP4 RL methods suffer from a key limitation: they primarily optimize quantization accuracy on the training and rollout paths independently rather than directly reducing the discrepancy between the two quantized execution paths. In this work, we propose TRACE (Train-Rollout Quantization Alignment via Compact GuidancE), an FP4 quantization framework for RL training of Mixture-of-Experts (MoE) language models that addresses the limitation of existing FP4 RL methods. TRACE incorporates rollout-guided quantization-aware training that uses rollout-side quantization outcomes to guide training-side FP4 rounding decisions, directly reducing train-rollout discrepancy. Moreover, TRACE adopts an efficient quantization-information caching scheme that selectively retains mantissa and scale information from deeper layers to reduce the storage and communication overhead introduced by rollout guidance. We evaluate TRACE on four large-scale MoE language models across reasoning, coding, and long-horizon RL tasks. Our results demonstrate that TRACE enables joint FP4 weight/activation and FP4 KV-cache rollout with RL performance comparable to BF16 rollout, while achieving up to 5.4x rollout speedup and strong final FP4 performance compared with post-hoc FP4 quantization of BF16-trained policies.

## English Summary

TRACE aligns FP4 quantization across training and rollout paths via rollout-guided QAT plus quantization-information caching; on four large MoE models it matches BF16 RL performance with FP4 weights/activations/KV-cache rollout, up to 5.4x rollout speedup, and beats post-hoc FP4 quantization.

## Obsidian Notes

- 内容由 `opencli arxiv paper` 拉取 arXiv 元数据与摘要生成。
- 中文导读与价值判断锚定在摘要的作者、日期、分类与实验设置上，未补充摘要之外的实验细节。
- 现代站点生成器按 `content/{entry.id}.md` 查找内容页；本文件写入 canonical content 目录，而不是 `openclaw/content/`。