# Information Abundance Paradox: Long-Context Training Undermines Parametric Knowledge

- **ID**: 94afd5cf
- **原文链接**: https://arxiv.org/abs/2608.12218
- **PDF**: https://arxiv.org/pdf/2608.12218v2
- **作者**: Arda Uzunoglu, Benjamin Van Durme, Daniel Khashabi
- **日期**: 2026-08-12
- **更新**: 2026-08-13
- **分类**: models
- **来源类型**: paper
- **标签**: long-context, parametric-knowledge, training-dynamics, information-abundance, cs.cl, cs.cl-cs.ai
- **质量评分**: 4/5
- **抓取时间**: 2026-08-14T04:19:48Z

---

## 中文导读

论文提出信息丰富惨论：long-context 训练会推动模型从参数化记忆转向上下文查询，在某些任务上反而低于短上下文训练让训练上下文越长越好这一隐含假设受到挑战

## 为什么值得关注

信息丰富惨论：long-context 训练可能抵消参数化记忆，让某些任务变差

## 关键信息

- 论文标题：Information Abundance Paradox: Long-Context Training Undermines Parametric Knowledge
- 作者：Arda Uzunoglu, Benjamin Van Durme, Daniel Khashabi
- arXiv：https://arxiv.org/abs/2608.12218
- 发布时间：2026-08-12
- arXiv 分类：cs.CL, cs.AI
- 关联标签：long-context, parametric-knowledge, training-dynamics, information-abundance, cs.cl, cs.cl-cs.ai

## English Abstract

Large language models are increasingly trained and deployed with long contexts that span documents, code repositories, and interaction histories. This scaling reflects the implicit assumption that training on longer contexts will only help the model by exposing it to richer evidence. We challenge this view by studying how the context window shapes a model's mode of learning, shifting it between parametric internalization and contextualization. We propose the Information Abundance Paradox, which hypothesizes that abundant relevant information in the training context can reduce the incentive to encode that information parametrically, thereby increasing reliance on context. In pretraining with long documents, increasing the context window improves language modeling, natural language understanding, and closed-book MCQA only up to an intermediate optimum, after which performance consistently declines. In supervised fine-tuning, more task-relevant train-time context improves performance with supporting context, but reduces robustness when context is absent or misleading at test time. Our analysis suggests that this behavior arises when longer context provides a lower complexity solution. Mechanistically, training with informative context shifts gradient pressure from feed-forward networks, often linked to parametric knowledge, toward attention modules, and causal interventions show that this shift increases reliance on context during inference. Overall, these findings support the Information Abundance Paradox and suggest that scaling toward near-infinite context is not simply a matter of supplying more data, even when high-quality long-context data is abundant.

## English Summary

The paper argues that training on long contexts shifts the model from parametric internalization toward contextual retrieval, with measurable drops on some knowledge-intensive tasks. The 'information abundance paradox' challenges the implicit assumption that longer training contexts only help.

## Obsidian Notes

- 内容由 `opencli arxiv paper` 拉取 arXiv 元数据与摘要生成。
- 中文导读与价值判断均锚定在条目已有摘要、论文摘要、作者、日期与分类信息上；未补充论文摘要之外的实验细节。
