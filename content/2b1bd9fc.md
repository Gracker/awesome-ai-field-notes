# LoopVQ: Sub 1-bit KV Cache Quantization for Looped Transformers

- **原文链接**: https://arxiv.org/abs/2611.05304
- **PDF**: https://arxiv.org/pdf/2611.05304
- **作者**: Minsoo Cheong, Sungjoo Yoo
- **日期**: 2026-11-03
- **更新**: 2026-11-03
- **分类**: models
- **来源类型**: paper
- **标签**: kv-cache, quantization, looped-transformers, memory
- **质量评分**: 4/5
- **抓取时间**: 2026-11-05T00:01:20Z

---

## 中文导读

arXiv 2611.05304（11-03，cs.LG/cs.AI/cs.CL）处理 looped transformer 的 KV 缓存瓶颈：同一组层在多个 loop step 上重复应用，参数量省了，但每个 step 各存一套 KV，缓存随 loop 数线性增长成为主内存瓶颈。作者观察到 KV 缓存沿 loop 轴高度冗余、各 step 对量化敏感度差异大，据此提出 LoopVQ，把 KV 缓存压到 sub-1-bit 量化。

## 为什么值得关注

LoopVQ 把 looped transformer 的 KV 缓存压到 sub-1-bit：循环轴冗余 + 分 step 敏感度差异是关键

looped 架构是参数效率路线的代表，KV 缓存正是其部署短板；sub-1-bit KV 若成立会改变其长上下文成本结构。

## 关键信息

- 原文链接: https://arxiv.org/abs/2611.05304
- arXiv 2026-11-03 | cs.LG, cs.AI, cs.CL
- PDF: https://arxiv.org/pdf/2611.05304
- 作者: Minsoo Cheong, Sungjoo Yoo
## English Abstract

Looped transformers are a parameter-efficient alternative to standard transformers for language modeling. By reapplying the same layers across multiple loop steps, recent looped language models match the performance of non-looped models several times their size. While this architecture effectively reduces parameter memory, each loop step still stores its own keys and values, so the key-value (KV) cache grows linearly with the number of loop steps and becomes the main memory bottleneck. We observe that the KV cache of looped models is highly redundant along the loop axis and that the loop steps differ substantially in their sensitivity to quantization. Based on these observations, we propose $\textbf{LoopVQ}$, a KV cache vector quantization method for looped transformers that codes channels of multiple loop steps jointly, and fine-tunes the codebooks to match the output of the full-precision model. At 0.5 bits per element, LoopVQ outperforms existing KV cache vector quantization methods for standard LLMs on general, long chain-of-thought reasoning, and long-context retrieval tasks with Ouro and Huginn models. Its design is orthogonal to these methods, and combined with TaSQ, it retains much of the BF16 accuracy even at 0.25 bits per element. We also implement LoopVQ in SGLang, where it nearly halves the decode latency at a 32K-token context and raises the peak serving throughput by up to $4.3\times$ and $6.1\times$ on the 1.4B and 2.6B Ouro models compared to the BF16 baseline.

## English Summary

LoopVQ: Sub 1-bit KV Cache Quantization for Looped Transformers (arXiv 2611.05304, Nov 3, cs.LG/cs.AI/cs.CL; Minsoo Cheong, Sungjoo Yoo). Looped transformers reapply the same layers across loop steps, matching much larger non-looped models while saving parameters, but each loop step stores its own keys and values, so the KV cache grows linearly with loop steps and becomes the main memory bottleneck. The authors observe the cache is highly redundant along the loop axis and that loop steps differ substantially in quantization sensitivity, and propose LoopVQ to push KV cache quantization below 1 bit.

## Obsidian Notes

- 内容由 `opencli arxiv paper` 拉取的 arXiv 元数据与摘要生成；中文导读与价值判断锚定在摘要、作者、日期与分类信息上，未补充摘要之外的事实。
