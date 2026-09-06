# Infini Memory: Maintainable Topic Documents for Long-Term LLM Agent Memory

- **ID**: acb1f56c
- **原文链接**: https://arxiv.org/abs/2606.10677
- **PDF**: https://arxiv.org/pdf/2606.10677
- **作者**: Suozhao Ji, Baodong Wu, Zehao Wang, Lei Xia, Qingping Li, Ruisong Wang, Wenbo Ding, Zhenhua Zhu, Boxun Li, Guohao Dai, Yu Wang
- **日期**: 2026-06-09
- **更新**: 2026-06-09
- **分类**: infra
- **来源类型**: paper
- **标签**: agent-memory, long-term-memory, topic-documents, retrieval, memoryagentbench, arxiv
- **质量评分**: 4/5
- **抓取时间**: 2026-09-06 12:21 UTC

---

## 中文导读

Infini Memory：把智能体长期记忆组织成可维护的主题文档现有记忆系统把观察存成孤立记录摘要或索引片段，导致证据聚合事实修订与记忆维护都困难；该架构把记忆视为主题结构化文本每个主题文档是一个语义单元，负责收集相关证据保存元数据并随时间修订事实；新观察先进缓冲区，再周期性合并成连贯文本上下文；推理时通过迭代式工具调用让 LLM 反复读取记忆而非单步检索；MemoryAgentBench 上验证

## 为什么值得关注

长期记忆别存成碎片：按主题维护可修订的文档单元，缓冲合并 + 迭代式读取，证据聚合与事实修订都有了载体

## 关键信息

- 论文标题：Infini Memory: Maintainable Topic Documents for Long-Term LLM Agent Memory
- 作者：Suozhao Ji, Baodong Wu, Zehao Wang, Lei Xia, Qingping Li, Ruisong Wang, Wenbo Ding, Zhenhua Zhu, Boxun Li, Guohao Dai, Yu Wang
- arXiv：https://arxiv.org/abs/2606.10677
- 发布时间：2026-06-09
- arXiv 分类：cs.AI, cs.CL
- 关联标签：agent-memory, long-term-memory, topic-documents, retrieval, memoryagentbench, arxiv

## English Abstract

Long-term LLM agents need persistent memory that can track changing facts and provide relevant evidence across sessions. Existing memory systems often store observations as isolated records, summaries, or indexed fragments, which makes evidence aggregation, fact revision, and memory maintenance difficult. We propose Infini Memory, a maintainable text-based persistent memory architecture that treats agent memory as topic-structured documents. Each topic document serves as a semantic unit for collecting related evidence, preserving metadata, and revising facts over time. New observations are first staged in a buffer and periodically consolidated into coherent textual contexts. At inference time, an agentic retrieval procedure lets the LLM read memory through iterative tool calls rather than a single retrieval step. On MemoryAgentBench, Infini Memory achieves 64.7% overall score. Ablations show that topic-structured maintenance and iterative evidence inspection improve complementary aspects of long-term memory use.

## English Summary

Long-term LLM agents need persistent memory that can track changing facts and provide relevant evidence across sessions. Existing memory systems often store observations as isolated records, summaries, or indexed fragments, which makes evidence aggregation, fact revision, and memory maintenance difficult. We propose Infini Memory, a maintainable text-based persistent memory architecture that treats agent memory as topic-structured documents. Each topic document serves as a semantic unit for collecting related evidence, preserving metadata, and revising facts over time. New observations are first staged in a buffer and periodically consolidated into coherent textual contexts. At inference time, an agentic retrieval procedure lets the LLM read memory through iterative tool calls rather than a single retrieval step. On MemoryAgentBench, Infini Memory achieves 64.7% overall score. Ablations show that topic-structured maintenance and iterative evidence inspection improve complementary aspects of long-term memory use.

## Obsidian Notes

- 内容由 `opencli arxiv paper` 拉取 arXiv 元数据与摘要生成。
- 中文导读与价值判断均锚定在条目已有摘要、论文摘要、作者、日期与分类信息上；未补充论文摘要之外的实验细节。
