# Sleep-time Compute: Beyond Inference Scaling at Test-time

- **ID**: 86b4fbde
- **原文链接**: https://arxiv.org/abs/2504.13171
- **PDF**: https://arxiv.org/pdf/2504.13171v1
- **作者**: Kevin Lin, Charlie Snell, Yu Wang, Charles Packer, Sarah Wooders, Ion Stoica, Joseph E. Gonzalez
- **日期**: 17 Apr 2025
- **更新**: 17 Apr 2025
- **分类**: agents
- **来源类型**: paper
- **标签**: sleep-time-compute, inference-cost, test-time-compute, amortization, llm-serving
- **质量评分**: 4/5
- **抓取时间**: 2026-10-28T15:46:42Z

---

## 中文导读

测试时扩算是 LLM 解难题的关键配料，但带来高延迟与推理成本。sleep-time compute 让模型在查询到来前离线「思考」上下文：预判用户可能问什么、预计算有用的量，显著降低测试时算力。在改造的 Stateful GSM-Symbolic 与 Stateful AIME 上，同等准确率所需测试时算力降约 5 倍；扩大 sleep-time 计算还能再提准确率最高 13%/18%。把 sleep-time 计算摊到同一上下文的多条相关查询后，单查询平均成本再降 2.5 倍。分析显示查询可预测性与该法有效性高度相关，并给出真实 agentic SWE 任务案例。

## 为什么值得关注

测试时扩算是 LLM 解难题的关键配料，但带来高延迟与推理成本。sleep-time compute 让模型在查询到来前离线「思考」上下文：预判用户可能问什么、预计算有用的量，显著降低测试时算力。在改造的 Stateful GSM-Symbolic 与 Stateful AIME...

Extra grounding: arXiv v1 submitted 17 Apr 2025; subjects cs.AI, cs.CL.

## Obsidian 摘要摘录

> 摘自 Agent实践探索 2026-10-28：

这与 Letta 的 sleep-time compute 论文（arXiv:2504.13171）方向一致：把推理挪到用户离线的空档，同等准确率下测试时算力省约 5 倍，相关查询摊薄后单次成本再降 2.5 倍。

## 关键信息

- 论文标题：Sleep-time Compute: Beyond Inference Scaling at Test-time
- 作者：Kevin Lin, Charlie Snell, Yu Wang, Charles Packer, Sarah Wooders, Ion Stoica, Joseph E. Gonzalez
- arXiv：https://arxiv.org/abs/2504.13171
- PDF：https://arxiv.org/pdf/2504.13171v1
- 发布时间：17 Apr 2025
- 更新时间：17 Apr 2025
- arXiv 分类：Artificial Intelligence (cs.AI); Computation and Language (cs.CL)
- 备注：Code and data released at: https://github.com/letta-ai/sleep-time-compute
- 关联标签：sleep-time-compute, inference-cost, test-time-compute, amortization, llm-serving

## English Abstract

Scaling test-time compute has emerged as a key ingredient for enabling large language models (LLMs) to solve difficult problems, but comes with high latency and inference cost. We introduce sleep-time compute, which allows models to "think" offline about contexts before queries are presented: by anticipating what queries users might ask and pre-computing useful quantities, we can significantly reduce the compute requirements at test-time. To demonstrate the efficacy of our method, we create modified versions of two reasoning tasks - Stateful GSM-Symbolic and Stateful AIME. We find that sleep-time compute can reduce the amount of test-time compute needed to achieve the same accuracy by ~ 5x on Stateful GSM-Symbolic and Stateful AIME and that by scaling sleep-time compute we can further increase accuracy by up to 13% on Stateful GSM-Symbolic and 18% on Stateful AIME. Furthermore, we introduce Multi-Query GSM-Symbolic, which extends GSM-Symbolic by including multiple related queries per context. By amortizing sleep-time compute across related queries about the same context using Multi-Query GSM-Symbolic, we can decrease the average cost per query by 2.5x. We then conduct additional analysis to understand when sleep-time compute is most effective, finding the predictability of the user query to be well correlated with the efficacy of sleep-time compute. Finally, we conduct a case-study of applying sleep-time compute to a realistic agentic SWE task.
