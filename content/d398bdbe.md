# Aggron: Aggressive Compression of Agentic KV Caches during Head-of-Line Stalls in the Request Queue

- **ID**: d398bdbe
- **原文链接**: https://arxiv.org/abs/2611.26435
- **PDF**: https://arxiv.org/pdf/2611.26435v1
- **作者**: Rishabh Ravi, Tony Hong, Chen Wang, Yue Zhu, Mengmei Ye, Hubertus Franke, Fan Lai, Josep Torrellas
- **日期**: 2026-11-19
- **更新**: 2026-11-19
- **分类**: infra
- **来源类型**: paper
- **标签**: infra, serving, kv-cache, agents, compression
- **质量评分**: 4/5
- **抓取时间**: 2026-11-22T00:02:11Z

---

## 中文导读

智能体请求是多轮长程序，KV 缓存逐轮增长，服务容量被缓存内存卡住；现有上下文压缩往往等缓存越过阈值再一次性总结大段历史，同引擎执行时会与在线请求争抢算力和内存；Aggron 改为逐轮总结并只压缩 KV 缓存的部分片段，保持总结请求轻量, 精度不掉；当对应智能体请求因队头阻塞停在主队列时，从独立的 Summarization Queue 发起总结，复用阻塞期间闲置的算力与内存，且只在预测总结能在请求恢复执行前完成时才触发；与最先进的异步总结相比，高负载下 P99 程序延迟降低 27-31%，吞吐提升 1.34-1.40 倍

## 为什么值得关注

Aggron 逐轮压缩智能体 KV 缓存并借队头阻塞的空闲算力跑总结，高负载 P99 延迟降 27-31%，吞吐提升 1.34-1.40 倍

以上判断锚定论文摘要本身，具体数字与说法可在下方 English Abstract 中对照验证。

## 关键信息

- 论文标题：Aggron: Aggressive Compression of Agentic KV Caches during Head-of-Line Stalls in the Request Queue
- 作者：Rishabh Ravi, Tony Hong, Chen Wang, Yue Zhu, Mengmei Ye, Hubertus Franke, Fan Lai, Josep Torrellas
- arXiv：https://arxiv.org/abs/2611.26435
- 发布时间：2026-11-19
- arXiv 分类：cs.DC, cs.AR
- 关联标签：infra, serving, kv-cache, agents, compression

## English Abstract

LLM agents run long, multi-turn programs whose contexts grow at every step, and serving them is limited by KV cache capacity. To alleviate this limitation, systems use context compression techniques, which typically wait until the KV cache crosses a large threshold and then summarize large spans of history at once, either in the background while the agent progresses or on the critical path. These summarizations can be done using the same model running on the same engine, or using the same or a different model running on extra hardware. When running on the same engine, summarization competes with the requests being served for both compute and memory capacity. To maximize the cost-effectiveness of summarization, this paper presents a new serving system called {\em Aggron}. Aggron summarizes agentic requests at every turn and selectively summarizes only certain parts of the KV cache. As a result, Aggron retains accuracy and keeps summarization requests lightweight. Moreover, Aggron launches summarization requests from a separate {\em Summarization Queue} while the corresponding agentic request whose KV cache we want to compress is stalled in the main request queue due to head-of-line stalls. The Summarization queue utilizes compute and memory capacity left over by the head-of-line stalls in the main queue. Further, to maximize efficiency, the server issues summarizations only when it predicts that they can complete before the corresponding agentic request will finally execute. In our evaluation, we compare Aggron to state-of-the-art asynchronous summarization. At high load, Aggron reduces P99 program latency by $27$--$31\%$, and raises throughput by $1.34$--$1.40\times$.

## English Summary

Agentic LLM requests run long multi-turn programs whose KV caches grow every turn, and serving capacity is bounded by KV cache memory. Existing context compression waits for a large cache threshold and then summarizes large history spans at once, competing with live requests for compute and memory on the same engine. Aggron summarizes agentic requests at every turn and selectively compresses only parts of the KV cache, keeping summarization lightweight. It launches summarization jobs from a separate Summarization Queue while the owning request is stalled in the main queue by head-of-line blocking, reusing compute and memory the stall leaves idle, and issues a summarization only when it predicts the job finishes before the request resumes. Versus state-of-the-art asynchronous summarization, Aggron cuts P99 program latency 27-31% at high load and raises throughput 1.34-1.40x.

## Obsidian Notes

- 内容由 `opencli arxiv paper` 拉取 arXiv 元数据与摘要生成。
- 中文导读与价值判断均锚定在条目已有摘要、论文摘要、作者、日期与分类信息上；未补充论文摘要之外的实验细节。
