# Verifiable Agentic Traffic Class: A Policed Quality-of-Service Mechanism for Agentic AI Traffic, Evaluated from Simulation to Real-Kernel Adversarial Testing

> Source: https://arxiv.org/abs/2611.14211
> Authors: Naveen Babu Narayanan Nair, Sajay Kurup
> Published: 2026-11-10
> Categories: cs.LG, cs.AI, cs.NI
> PDF: https://arxiv.org/pdf/2611.14211v1
> Comments: 20 pages, 3 figures, 15 tables; submitted to IEEE Access; code and data at doi:10.5281/zenodo.23865136

## Abstract (condensed)

Software agents built on LLMs generate traffic unlike human web traffic, yet routers have no class for it and cannot verify a sender's claim to be an agent. The paper proposes the **Verifiable Agentic Traffic Class (VATC)**, combining three mechanisms:

1. **Reserved DSCP declaration** — a Differentiated Services Code Point value declaring agent traffic
2. **Router-side verification classifier** — demotes flows whose behavior contradicts the declaration to a class served *after* best-effort traffic
3. **Rate-limited priority queue** — bounds the damage any verified agent class can inflict

Compared against static DiffServ (trusts the marking) and fq_codel (per-flow fair queuing) in two simulators and on a real Linux kernel.

## Key Results

- **Steady load:** VATC matches DiffServ.
- **Constructed burst (simulation, assuming immediate verdict):** mean agent queuing delay cut **98%** vs DiffServ, at a 12% increase in human delay; most of the gain comes from having a separate class, not from verification.
- **Spoofed flood (real kernel):** the rate limit held human latency **11x below** DiffServ's.
- **Without verification, the baseline wins:** DiffServ and a tightly configured fq_codel give legitimate agents *lower* latency than VATC — verification only pays off under adversarial traffic.
- **Live four-feature classifier:** demoted all 20 bulk-shaped spoofers and served agents 0.30 ms — but missed six spoofers that copied the agent traffic pattern.
- **Timing feature fragility:** under emulated network delay, the classifier's timing feature stopped separating agent from human flows.
- **Why it matters in practice:** for real agent harnesses on a congested link, router queueing took **13%–63% of task time**, depending on harness and assumed model latency.
- **Stated limitation:** traffic was synthetic or sandbox-scale.

## 中文概要

LLM Agent 的流量形态与人类明显不同，但路由器既没有对应的流量类别，也无法验证发送方自称的 agent 身份。论文提出 VATC：用保留 DSCP 值声明 agent 流量，路由器侧分类器把与声明矛盾的流降级到 best-effort 之后服务，再叠加限速优先队列。在两套模拟器与真实 Linux 内核上对比静态 DiffServ 与 fq_codel：稳态负载下相当；模拟突发中 agent 平均排队延迟较 DiffServ 降 98%（人类延迟仅增 12%），收益主要来自独立类别本身；内核伪造洪泛下限速把人类延迟压到 DiffServ 的 1/11。无验证时 DiffServ 与调紧的 fq_codel 反而给合法 agent 更低延迟——验证只在对抗流量下有价值。在线四特征分类器降级了全部 20 个成批形态伪造者（agent 延迟 0.30 ms），但漏掉 6 个模仿 agent 模式的伪造流；引入网络延迟后时序特征失效。拥塞链路上路由排队占真实 agent 任务耗时的 13%–63%。实验流量均为合成或沙箱规模。
