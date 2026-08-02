# IFCMemoryBench: 评测 BIM 信息检索中 LLM Agent 的长期记忆能力

> Source: https://arxiv.org/abs/2607.26072
> Content fetched: 2026-08-02T12:19:15+08:00
> Grounding: opencli arxiv paper

## 一句话
IFCMemoryBench 在 BIM 领域提供 143 个多会话记忆任务，将记忆评测分解为摄入/检索/利用三环节

## 关键信息
- arXiv ID: 2607.26072
- English title: IFCMemoryBench: Evaluating Long-Term Memory of LLM-Based Agents in BIM Information Retrieval
- Authors: Changyu Du, Alexander Vosseler, Filippo Mazza, André Borrmann
- Submitted/Published: 2026-07-13
- Updated: 2026-07-13
- Subjects: cs.IR, cs.AI
- PDF: https://arxiv.org/pdf/2607.26072v1
- Tags: agent-memory, benchmark, bim, long-term-memory, domain-specific
- Quality score: 4

## 中文摘要
IFCMemoryBench 是一个在建筑信息模型（BIM）工作流中评测 LLM Agent 长期记忆的基准它含有 19 个项目4,016 个先前会话中的 143 个多会话任务，每个任务在早期对话中植入缺失的项目上下文，后续探针问题需结合记忆上下文与实时 IFC 查询才能回答评测框架将记忆性能分解为摄入检索和利用三个环节，同时测量答案质量和系统级指标

## English Summary
IFCMemoryBench is a benchmark for evaluating long-term memory in LLM-based agents within Building Information Modelling (BIM) workflows. It contains 143 multi-session tasks across 19 projects and 4,016 prior sessions, derived from incomplete-information questions in IFC-Bench v2. Each task seeds missing project context across earlier conversations and later asks a probe question answerable only by combining remembered context with live IFC queries. The evaluation framework decomposes memory performance into ingestion, retrieval, and utilization, measuring both answer quality and system-level metrics.

## Why it matters
IFCMemoryBench 在 BIM 领域提供 143 个多会话记忆任务，将记忆评测分解为摄入/检索/利用三环节

## arXiv Abstract
Long-term memory is becoming a core capability of LLM-based agents, but existing evaluations largely test conversational recall in open-domain or persona-grounded settings. We argue that a stronger test is whether an agent can reuse information from prior sessions while acting over a live, structured, domain-specific environment. We study this problem in Building Information Modelling (BIM), a professional engineering workflow where agents must query large IFC models while also relying on project specifications, client decisions, and engineering conventions often discussed in conversation but absent from the model. We introduce IFCMemoryBench, a benchmark for evaluating long-term memory in LLM-based BIM information retrieval. IFCMemoryBench contains 143 multi-session tasks across 19 projects and 4,016 prior sessions, derived from incomplete-information questions in IFC-Bench v2. Each task seeds missing project context across earlier conversations and later asks a probe question that can be answered only by combining remembered context with live IFC queries. Our evaluation framework decomposes memory performance into ingestion, retrieval, and utilization, and measures both answer quality and memory quality with expert-validated LLM judges. We evaluate representative vector-, graph-, and file-based memory systems. The strongest system achieves only 32.4% answer accuracy under a deployment-realistic ingestion scope, and remains below 60% under oracle-filtered ingestion or a stronger probe agent. Analysis shows that current general-purpose memory systems often retrieve topically relevant context but store project knowledge as incomplete or fragmented facts. These results reveal a domain-transfer gap in agent memory and suggest that reliable professional agents require domain-aware memory representations linking conversations, project knowledge, and structured model entities.

## Source Metadata
```json
{
  "id": "2607.26072",
  "title": "IFCMemoryBench: Evaluating Long-Term Memory of LLM-Based Agents in BIM Information Retrieval",
  "authors": "Changyu Du, Alexander Vosseler, Filippo Mazza, André Borrmann",
  "abstract": "Long-term memory is becoming a core capability of LLM-based agents, but existing evaluations largely test conversational recall in open-domain or persona-grounded settings. We argue that a stronger test is whether an agent can reuse information from prior sessions while acting over a live, structured, domain-specific environment. We study this problem in Building Information Modelling (BIM), a professional engineering workflow where agents must query large IFC models while also relying on project specifications, client decisions, and engineering conventions often discussed in conversation but absent from the model. We introduce IFCMemoryBench, a benchmark for evaluating long-term memory in LLM-based BIM information retrieval. IFCMemoryBench contains 143 multi-session tasks across 19 projects and 4,016 prior sessions, derived from incomplete-information questions in IFC-Bench v2. Each task seeds missing project context across earlier conversations and later asks a probe question that can be answered only by combining remembered context with live IFC queries. Our evaluation framework decomposes memory performance into ingestion, retrieval, and utilization, and measures both answer quality and memory quality with expert-validated LLM judges. We evaluate representative vector-, graph-, and file-based memory systems. The strongest system achieves only 32.4% answer accuracy under a deployment-realistic ingestion scope, and remains below 60% under oracle-filtered ingestion or a stronger probe agent. Analysis shows that current general-purpose memory systems often retrieve topically relevant context but store project knowledge as incomplete or fragmented facts. These results reveal a domain-transfer gap in agent memory and suggest that reliable professional agents require domain-aware memory representations linking conversations, project knowledge, and structured model entities.",
  "published": "2026-07-13",
  "updated": "2026-07-13",
  "primary_category": "cs.IR",
  "categories": "cs.IR, cs.AI",
  "comment": "KDD 2026 Workshop on Evaluation and Trustworthiness of Agentic AI",
  "pdf": "https://arxiv.org/pdf/2607.26072v1",
  "url": "https://arxiv.org/abs/2607.26072"
}
```
