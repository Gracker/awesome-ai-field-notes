# FlashRT: Agent Harness for Guiding Agents to Deploy Real-Time Multimodal Applications

- source_url: https://arxiv.org/abs/2607.18171
- source_type: paper
- platform: arxiv
- author: Krish Agarwal, Zhuoming Chen, Yanyuan Qin, Zhenyu Gu, Atri Rudra, Beidi Chen
- original_date: 2026-07-20
- added_date: 2026-07-22
- arxiv_id: 2607.18171
- arxiv_categories: cs.LG
- pdf_url: https://arxiv.org/pdf/2607.18171v1
- category: agents
- tags: agent-harness, real-time, multimodal, serving, coding-agents, flashrt, arxiv
- quality_score: 4

## 摘要（中文）

实时多模态应用（语音 agent、交互视频生成等）把异构模型组成管线，高效部署需要针对放置、流式与模型内并行的应用特定决策。现有 serving 与自动并行编译器变换有限、工作负载假设固定，新应用往往仍需手写高效实现。FlashRT 是一种 agent harness，引导通用 coding agent 把开发者写的简单参考实现抬升为可在时延/吞吐间权衡的优化多 GPU 部署。其 chain-of-program 多阶段流程：将参考实现变换为捕获数据依赖与持久状态作用域的 IR，经顺序解释器校验，再做静态分析识别候选变换；随后在测量门控优化环中迭代实现、验证与基准测试，产出覆盖不同硬件预算的有效部署。在视频世界模型与多模态 LLM 等应用上，NVIDIA B200 最高约 70× 时延下降与 2.8× 吞吐提升；AMD MI355X 上匹配峰值时延降幅并将峰值吞吐提升至 3.6×，显示在专家优化尚不成熟的平台上 agent 驱动优化更具可扩展性。对 Qwen3-Omni text-to-audio，相对 AMD 上专家 vLLM-Omni 实现响应时延再降 65%。

## Summary (English)

Real-time multimodal applications, including voice agents and interactive video generation, compose heterogeneous models into pipelines whose efficient deployment requires application-specific decisions about placement, streaming, and intra-model parallelism. Existing serving systems and auto-parallelism compilers commit to limited transformations and fixed workload assumptions, so achieving high performance on a new application requires hand-crafting an efficient implementation. We present FlashRT, an agent harness that guides coding agents to lift simple developer-written reference implementations into optimized multi-GPU deployments that flexibly weigh target metrics like latency and throughput. Using a new chain-of-program paradigm, FlashRT directs a generic coding agent through a multi-pass transformation process where an agent transforms the reference into an intermediate representation (IR) to capture data dependencies and persistent-state scopes, validates this IR via a sequential interpreter, and performs static analyses to identify candidate transformations. Then, the agent iteratively implements, verifies, and benchmarks each candidate under a measurement-gated optimization loop to produce effective deployments that span different hardware budgets. Across various applications, including video world models and multimodal LLMs, FlashRT converts reference implementations into highly efficient deployments, delivering up to ~70x latency reduction and 2.8x throughput improvement on NVIDIA B200 GPUs. On AMD MI355X GPUs, FlashRT matches the peak latency reduction while increasing peak throughput improvement to 3.6x, demonstrating that agent-driven optimization can be more scalable on platforms with less mature expert optimization. In fact, for Qwen3-Omni text-to-audio inference, FlashRT reduces response latency by 65% compared to the expert vLLM-Omni implementation on AMD MI355X.

## One-liner

FlashRT 以 chain-of-program harness 引导 coding agent，把参考实现抬升为多 GPU 实时多模态部署，最高约 70× 时延下降。

## 原文 / 元数据抓取

# FlashRT: Agent Harness for Guiding Agents to Deploy Real-Time Multimodal Applications
> 作者: Krish Agarwal, Zhuoming Chen, Yanyuan Qin, Zhenyu Gu, Atri Rudra, Beidi Chen
> 原文链接: https://arxiv.org/abs/2607.18171
> PDF: https://arxiv.org/pdf/2607.18171v1
> 发布时间: 2026-07-20
> 更新时间: 2026-07-20
> 分类: cs.LG

---

Real-time multimodal applications, including voice agents and interactive video generation, compose heterogeneous models into pipelines whose efficient deployment requires application-specific decisions about placement, streaming, and intra-model parallelism. Existing serving systems and auto-parallelism compilers commit to limited transformations and fixed workload assumptions, so achieving high performance on a new application requires hand-crafting an efficient implementation. We present FlashRT, an agent harness that guides coding agents to lift simple developer-written reference implementations into optimized multi-GPU deployments that flexibly weigh target metrics like latency and throughput. Using a new chain-of-program paradigm, FlashRT directs a generic coding agent through a multi-pass transformation process where an agent transforms the reference into an intermediate representation (IR) to capture data dependencies and persistent-state scopes, validates this IR via a sequential interpreter, and performs static analyses to identify candidate transformations. Then, the agent iteratively implements, verifies, and benchmarks each candidate under a measurement-gated optimization loop to produce effective deployments that span different hardware budgets. Across various applications, including video world models and multimodal LLMs, FlashRT converts reference implementations into highly efficient deployments, delivering up to ~70x latency reduction and 2.8x throughput improvement on NVIDIA B200 GPUs. On AMD MI355X GPUs, FlashRT matches the peak latency reduction while increasing peak throughput improvement to 3.6x, demonstrating that agent-driven optimization can be more scalable on platforms with less mature expert optimization. In fact, for Qwen3-Omni text-to-audio inference, FlashRT reduces response latency by 65% compared to the expert vLLM-Omni implementation on AMD MI355X.

## Obsidian intake evidence excerpt

该内容文件由 AAIF content-fetcher 根据 active/high-score entry 与 OpenCLI arXiv 元数据补齐。

- entry_id: 5e9f2abf
- title: FlashRT: Agent Harness for Guiding Agents to Deploy Real-Time Multimodal Applications
- source: https://arxiv.org/abs/2607.18171
- existing_summary_zh: FlashRT 以 agent harness 引导通用 coding agent，把开发者写的参考实现经 chain-of-program 多阶段变换（IR静态分析测量门控优化环）提升为多 GPU 实时多模态部署；在视频世界模型与多模态 LLM 等应用上最高约 70 延迟下降2.83.6 吞吐提升，并在 AMD 平台相对专家实现也取得优势收录理由：展示 harness+coding agent 可规模化替代手写 serving 优化，是实时多模态落地的强工程样板
