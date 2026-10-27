# Building Reasoning Models from the Ground Up: A Full Video Course

- **ID**: d1a3b4fa
- **原文链接**: https://magazine.sebastianraschka.com/p/building-reasoning-models
- **作者**: Sebastian Raschka
- **日期**: 2026-10-24
- **分类**: learning
- **来源类型**: article
- **标签**: reasoning-models, pytorch, course, rl-vr, distillation, qwen3
- **质量评分**: 4/5
- **抓取时间**: 2026-10-27T12:26:48Z

---

## 中文导读

Sebastian Raschka 发布免费视频课：8 集超 11 小时，从零用 Python/PyTorch 手写一个推理模型，配套其新书 Build a Reasoning Model (From Scratch)。课程从一个小型预训练 Qwen3 出发，亲手实现评估、推理时扩展、可验证奖励强化学习与蒸馏；前段 CPU 可跑，训练部分建议 GPU。他用引擎类比定位概念：推理模型是引擎（经 RL 后训练与可选推理扩展升级的 LLM），agent harness 是外围机械，负责上下文管理与工具接入——理解现代 LLM 智能体仍要从推理模型入手。材料自成体系，不强制先修他的 Build an LLM 课程。

## 为什么值得关注

Raschka 免费 11 小时视频课：从 Qwen3 手写推理模型的评估、推理扩展、RL 与蒸馏。对想穿透「reasoning effort / RLVR / 蒸馏」这些名词的工程师，这是目前最完整的从代码层理解推理模型的公开材料；视频 3 把数学验证器同时用作 MATH-500 评估器和 RL 奖励信号的设计，正是当前 RLVR 实践的最小可复现样本。

## 关键信息

- 课程规模: 8 集视频，超 11 小时编码内容，免费发布于 Ahead of AI (Substack)
- 起点模型: 预训练 Qwen3 0.6B（不自训基座，聚焦推理方法本身）
- 先修要求: 熟悉 Python 与 PyTorch；前代课程 Build a Large Language Model (From Scratch) 推荐但不强制
- 算力: 前期文本生成与评估可在 CPU 完成，后期训练建议 GPU；第 1 集讲环境搭建与硬件选择
- 视频 1: 动机与代码环境（uv 安装依赖、CUDA/Apple Silicon 检查、远程 GPU + VS Code）
- 视频 2: 加载基座模型、文本生成与 KV caching（流式生成、torch.compile、速度对比）
- 视频 3: 数学答案验证器（答案抽取→规范化→等价性判定），用于 MATH-500 评估，后续兼作 RLVR 奖励信号
- 视频 4: 推理时扩展——采样与 self-consistency（保持权重不变改进答案）
- 后续视频: 按课程大纲继续覆盖强化学习（可验证奖励）与蒸馏
- 配套书: Build a Reasoning Model (From Scratch)（Manning / Amazon，印刷版彩色）
- 概念速览替代: 作者在 LinkedIn Learning 的 90 分钟 AI Reasoning Models 课程

## English Summary

Sebastian Raschka published a free 8-video, 11+ hour course that builds a reasoning model from the ground up in Python/PyTorch, accompanying his book "Build a Reasoning Model (From Scratch)". Starting from a small pre-trained Qwen3 model, the videos implement evaluation, inference-time scaling, reinforcement learning with verifiable rewards, and distillation by hand, with early examples runnable on CPU and later training practical on a GPU. He frames the stack with an engine analogy: the reasoning model is the engine (an LLM upgraded via RL post-training and optional inference scaling), while the agent harness is the machinery around it handling context management and tool access - so reasoning models remain the core of understanding modern LLM agents. Early lectures cover environment setup, loading Qwen3 with KV caching and torch.compile, building a math-answer verifier evaluated on MATH-500 that later doubles as the RLVR reward signal, and inference-time scaling via sampling and self-consistency. Prerequisites are Python and PyTorch; the materials stand alone from his earlier "Build a Large Language Model (From Scratch)" course.

## 原文摘录 (Excerpts)

> Eight videos and over 11 hours of coding, covering evaluation, inference-time scaling, reinforcement learning, and distillation in Python and PyTorch.

> The reasoning-from-scratch videos focus on a small pre-trained Qwen3 model, where we implement the reasoning methods ourselves in Python and PyTorch. Starting with a pre-trained model lets us focus on the interesting part: evaluation, inference-time scaling, reinforcement learning, and distillation.

> A reasoning model then functions as the engine inside an agent harness, where the agent harness is a software or tooling framework around the LLM/reasoning model to tackle even more challenging problems.

> In this lecture, we build a math-answer verifier step by step, from answer extraction to normalization and checking mathematical equivalence. We then use it to evaluate the model on MATH-500. [...] The verifier also has a second job later in the series: providing the reward signal for reinforcement learning with verifiable rewards (RLVR).

## Obsidian Notes

- 内容抓取自文章正文（opencli web read 导航被拒，改用 curl 拉取 Substack 页面 HTML 后解析文本；JSON-LD 缺失，元数据以页面正文为准）。导读与价值判断锚定在文章正文、条目已有摘要与标签上；视频 5-8 的分集细节未在可见正文中逐条展开，仅按课程副标题所述范围（RL 与蒸馏）描述。
