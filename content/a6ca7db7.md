# MAServeBench: Benchmarking Multi-Agent LLM Serving Systems with Hierarchical Collaboration Workloads

- **原文链接**: https://arxiv.org/abs/2610.40293
- **PDF**: https://arxiv.org/pdf/2610.40293
- **作者**: Shengxuan Qiu, Haochen Huang, Shuzhang Zhong, Zizhuo Fu, Zebin Yang, Jianming Tong, Meng Li
- **日期**: 2026-10-29
- **更新**: 2026-10-29
- **分类**: infra
- **来源类型**: paper
- **标签**: serving, benchmark, multi-agent, hardware
- **质量评分**: 4/5
- **抓取时间**: 2026-11-01T12:26:45Z

---

## 中文导读

LLM 多 agent 系统把一次用户请求拆成相互依赖的模型与工具操作：这些操作在不同时刻才就绪，并随 agent 协作、交换结果而消耗不断演化的上下文，形成变化的并发、计算与显存需求模式，在 serving 硬件上暴露出与独立请求不同的瓶颈。论文指出，要基准测试这些效应，必须捕捉生成 serving 负载的协作规则，而不只是执行期间观察到的请求。MAServeBench 把多 agent 协作当作 LLM serving 与硬件评估中可配置的工作负载维度：可组合阶段刻画文档化 MAS 工作流中 agent 如何协作与交换上下文，因此即使任务输入与工具不变，原生执行也能生成不同负载；Hierarchical Semantic Traces 保留实际发生的操作与依赖，支持在固定工作量下做可复现的比较；任务级测量把这些负载接到 serving 执行与 GPU/NPU 硬件行为上，解释为什么 serving 效率并不总能转化为任务按时完成。基准代码已在 GitHub 开源。

## 为什么值得关注

把多 agent 协作规则做成可配置的 serving 负载维度，任务级测量揭示 serving 效率与任务按时完成并不等价.

对做 LLM serving 与推理硬件评估的人，它补的是按独立请求测吞吐与时延看不到的那一层：真实 MAS 部署的负载形态由协作规则决定，正是摘要所说的“执行期间观察到的请求之外”的部分；任务级测量进一步解释了 serving 效率与任务按时完成之间的错位来自哪里。

## 关键信息

- 论文标题: MAServeBench: Benchmarking Multi-Agent LLM Serving Systems with Hierarchical Collaboration Workloads
- 作者: Shengxuan Qiu, Haochen Huang, Shuzhang Zhong, Zizhuo Fu, Zebin Yang, Jianming Tong, Meng Li
- arXiv: https://arxiv.org/abs/2610.40293
- 发布时间: 2026-10-29
- arXiv 分类: cs.MA
- 关联标签: serving, benchmark, multi-agent, hardware

## English Abstract

Large language model (LLM)-based multi-agent systems (MAS) coordinate specialized agents to solve complex tasks, turning each user request into interdependent model and tool operations. Unlike independent requests, these operations become ready at different times and consume evolving context as agents coordinate and exchange results. This creates changing patterns of concurrency, computation, and memory demand that can expose different bottlenecks in LLM serving hardware. Yet benchmarking these effects requires capturing the collaboration rules that generate serving workloads, beyond the requests observed during execution. We present MAServeBench, a benchmark that treats multi-agent collaboration as a configurable dimension of serving workloads for LLM serving and hardware evaluation. Its composable stages capture how agents coordinate and exchange context in documented MAS workflows, enabling native executions to generate different workloads even when task inputs and tools remain unchanged. Hierarchical Semantic Traces preserve realized operations and dependencies for reproducible comparisons of legal release constraints at fixed work. Task-linked measurements connect these workloads to serving execution and GPU/NPU hardware behavior, revealing why serving efficiency does not always translate into timely task completion. The benchmark code is available at https://github.com/ShengxuanQiu/MAServeBench.

## English Summary

Multi-agent LLM systems turn each user request into interdependent model and tool operations that become ready at different times and consume evolving context as agents coordinate, creating changing patterns of concurrency, computation, and memory demand that expose different bottlenecks in serving hardware. MAServeBench treats multi-agent collaboration as a configurable dimension of serving workloads: composable stages capture coordination rules from documented MAS workflows so native executions generate different workloads even when task inputs and tools are unchanged; Hierarchical Semantic Traces preserve realized operations and dependencies for reproducible comparison at fixed work; task-linked measurements connect workloads to serving execution and GPU/NPU hardware behavior, revealing why serving efficiency does not always translate into timely task completion....

## Obsidian Notes

- 内容由 `opencli arxiv paper` 拉取 arXiv 元数据与摘要生成。
- 中文导读与价值判断均锚定在条目已有摘要、论文摘要、作者、日期与分类信息上；未补充论文摘要之外的实验细节。
