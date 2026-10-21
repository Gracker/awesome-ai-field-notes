# LatComm: Reusable Context Compression for Latent Communication between Large Language Models

- **ID**: ceaf5f6f
- **原文链接**: https://arxiv.org/abs/2610.26840
- **PDF**: https://arxiv.org/pdf/2610.26840v1
- **作者**: Huawei Lin, Jinting Liu, Tan Yu, Weijie Zhao
- **日期**: 2026-10-19
- **更新**: 2026-10-19
- **分类**: models
- **来源类型**: paper
- **标签**: context-compression, latent-communication, cross-attention, multi-llm, efficiency
- **质量评分**: 4/5
- **抓取时间**: 2026-10-21T12:28:13.218278+00:00

---

## 中文导读

多 LLM 系统常常多个问题共用一份上下文；上下文以文本在模型间传递时，接收端每个问题都要把全部 token 重算一遍。要省掉这笔开销，上下文表示必须同时紧凑、跨问题可复用、能被另一个 LLM 读取，而已有的压缩与 latent communication 方法各自只占其一。LatComm 把编码与读取解耦：上下文不带问题先编码一次，接收端再按题选取要读的内容。冻结的编码器 LLM 把上下文压成定长 latent 包，发给另一个冻结的接收 LLM，后者用 cross-attention 读取、门控由其 prompt 计算。12 个选择题 QA 数据集上，平均准确率比单向量基线最高提升 10.2 分；QuALITY 上接收端输入省 57 倍，读同一篇文章答完多题快 3 倍。

## 为什么值得关注

LLM 间通信改走 latent 包：一次编码、按题读取，接收端输入省 57 倍、同文章多题快 3 倍；编码器与接收器是两个不同的冻结模型，跨模型可读这点让它在多 LLM 流水线里能直接套用，省的是真实重复预填成本。

## 关键信息

- 论文标题: LatComm: Reusable Context Compression for Latent Communication between Large Language Models
- arXiv: https://arxiv.org/abs/2610.26840
- PDF: https://arxiv.org/pdf/2610.26840v1
- 发布时间: 2026-10-19
- 备注: 17 pages, 9 figures, 11 tables. Under Review
- arXiv 分类: cs.CL, cs.AI
- 关联标签: context-compression, latent-communication, cross-attention, multi-llm, efficiency

## English Abstract

Systems that combine several large language models (LLMs) often use one context for many questions. When the context is passed between models as text, the receiving model processes all of its tokens again for every question. Avoiding this cost requires a context representation that is compact, reusable across questions, and readable by a different LLM. Existing compression and latent communication methods each provide only some of these properties. We introduce LatComm, a Latent Communication interface that provides all three by separating encoding from reading: the context is encoded once without the question, and the receiver selects what to read for each question. A frozen context encoder LLM compresses the context into a fixed-size packet and sends it to a different frozen receiver LLM, which reads the packet through cross-attention, with gates computed from its prompt. On 12 multiple-choice question-answering datasets, LatComm improves average accuracy over single-vector baselines by up to 10.2 points. On QuALITY, it reduces the receiver's input by 57x and answers the questions of an article 3x faster.

## English Summary

Multi-LLM systems that pass context as text force the receiver to reprocess every token for each new question. LatComm separates encoding from reading: a frozen context-encoder LLM compresses the context once, question-free, into a fixed-size latent packet; a different frozen receiver LLM reads it through cross-attention with gates computed from its own prompt, selecting per question what to read. On 12 multiple-choice QA datasets LatComm improves average accuracy over single-vector baselines by up to 10.2 points; on QuALITY it cuts the receiver's input 57x and answers an article's questions 3x faster.

## Obsidian Notes

- 内容由 `opencli arxiv paper 2610.26840` 拉取 arXiv 元数据与摘要生成。
- 中文导读与价值判断均锚定在条目已有摘要、论文摘要、作者、日期与分类信息上；未补充论文摘要之外的实验细节。
