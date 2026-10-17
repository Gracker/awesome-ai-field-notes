# The Right Memory in the Wrong Context：长期代理记忆的检索可采信性验证

> Source: https://arxiv.org/abs/2610.07309
> Content fetched: 2026-10-17T12:25:00+08:00
> Grounding: opencli arxiv paper (HTTP 429) -> arxiv.org/abs page via opencli web read

## 一句话
长期记忆代理会检索出「相关但不可采信」的记忆（属他人、违政策、状态不匹配）；该框架对每个记忆-查询对做三态判定，命名空间过滤在不损害域内排名的前提下把 top-20 anchor 召回从 0.432 提到 0.533

## 关键信息
- arXiv ID: 2610.07309
- English title: The Right Memory in the Wrong Context: Verifying Retrieval Admissibility in Long-Term Agent Memory
- Authors: Zi Wang, Xingqiao Wang, Emmanuel Addai, Devika Ambekar, Xiaowei Xu
- Submitted/Published: 2026-10-05
- Subjects: cs.AI, cs.IR, cs.MA
- PDF: https://arxiv.org/pdf/2610.07309v1
- Tags: agent-memory, security, retrieval, governance
- Quality score: 4

## 中文摘要
长期记忆代理可能检索出相关但不可采信的信息：属于其他主体、违反策略或生命周期状态不匹配，而召回率与答案准确率都无法揭示这类风险。论文提出检索可采信性验证框架，对每个记忆-查询对给出 admissible/inadmissible/unresolved 三态判定，在匹配必要证据召回率的条件下比较路由方案，并把记忆 ID 追踪到 prompt 暴露与目标级泄露。对 RHELM、MemOps 两个公开基准冻结排序的 top-20 再分析（3,767 条查询）显示：命名空间过滤不损害信任域内排名，anchor 召回 0.432→0.533，80% 召回可行性 0.237→0.311，相似度精确评估减少 98.3%；1,523 组配对案例中命名空间路由伴随 0.053–0.068 的判准率提升（观察性结论）；16 个受控暴露场景中仅一组读者的 95% 置信区间排除零（+0.156, 95% CI [0.031, 0.312]）。

## English Summary
Long-term-memory agents can retrieve information that is relevant yet inadmissible - owned by another principal, violating policy, or reflecting an incompatible lifecycle state - and neither recall nor final-answer accuracy reveals this. The paper introduces a retrieval-admissibility verification framework assigning each memory-query pair one of three statuses (admissible, inadmissible, unresolved), comparing routes at matched required-evidence recall with bounds for unresolved cases, and tracking memory IDs through prompt exposure. A post-hoc top-20 reanalysis of frozen rankings from RHELM and MemOps (3,767 queries) shows within-namespace scores unchanged while top-20 anchor recall rises from 0.432 to 0.533, 80% recall feasibility from 0.237 to 0.311, and exact similarity evaluations drop 98.3%. Across 1,523 paired cases, namespace routing is associated with judged-accuracy gains of 0.053-0.068 across three readers (observational). In 16 controlled exposure scenarios, only one of four reader-specific 95% confidence intervals excludes zero for relevant-inadmissible literal disclosure (+0.156, 95% CI [0.031, 0.312]). Results motivate separate verification of candidate support, admissibility, prompt exposure, and answer disclosure.

## Why it matters
指出 recall/accuracy 双指标会掩盖越权记忆暴露的风险，并给出可验证的评测协议（三态判定 + 匹配召回比较 + 暴露追踪）；对多用户/多租户 agent 记忆系统，这是一套可直接落地的治理与评测设计。

## arXiv Abstract
Long-term-memory agents can retrieve relevant information that is inadmissible for the current request because it belongs to another principal, violates policy, or reflects an incompatible lifecycle state. Recall and final-answer accuracy do not reveal this: a route can appear safe by missing required evidence, while a correct answer may follow inadmissible prompt exposure. We introduce a retrieval-admissibility verification framework that assigns each memory-query pair one of three statuses (admissible, inadmissible, or unresolved), compares routes at matched required-evidence recall with bounds for unresolved cases, and tracks memory IDs through prompt exposure while linking exposure to target-level disclosure. We evaluate its stages on separate, non-pooled populations. A post-hoc top-20 reanalysis of frozen rankings from two public long-term-memory benchmarks, RHELM and MemOps, covers 3,767 queries. All released anchors lie within trusted query namespaces; with within-namespace scores unchanged, off-namespace filtering cannot lower their ranks. Top-20 anchor recall increases from 0.432 to 0.533, 80% recall feasibility from 0.237 to 0.311, and exact similarity evaluations decrease by 98.3%. In a frozen 72-case development diagnostic, a released-metadata reference preserves required evidence, whereas neither text-only verifier detects violations under the 1% required-anchor false-denial limit. Across 1,523 paired benchmark-native cases, namespace routing is associated with judged-accuracy gains of 0.053-0.068 across three readers; recall also changes, so this comparison is observational. In 16 controlled exposure scenarios, only one of four reader-specific 95% confidence intervals excludes zero for relevant-inadmissible literal disclosure (+0.156, 95% CI \[0.031, 0.312\]). Results motivate separate verification of candidate support, admissibility, prompt exposure, and answer disclosure.

## Source Metadata
```json
{
  "id": "2610.07309",
  "title": "The Right Memory in the Wrong Context: Verifying Retrieval Admissibility in Long-Term Agent Memory",
  "authors": "Zi Wang, Xingqiao Wang, Emmanuel Addai, Devika Ambekar, Xiaowei Xu",
  "abstract": "Long-term-memory agents can retrieve relevant information that is inadmissible for the current request because it belongs to another principal, violates policy, or reflects an incompatible lifecycle state. Recall and final-answer accuracy do not reveal this: a route can appear safe by missing required evidence, while a correct answer may follow inadmissible prompt exposure. We introduce a retrieval-admissibility verification framework that assigns each memory-query pair one of three statuses (admissible, inadmissible, or unresolved), compares routes at matched required-evidence recall with bounds for unresolved cases, and tracks memory IDs through prompt exposure while linking exposure to target-level disclosure. We evaluate its stages on separate, non-pooled populations. A post-hoc top-20 reanalysis of frozen rankings from two public long-term-memory benchmarks, RHELM and MemOps, covers 3,767 queries. All released anchors lie within trusted query namespaces; with within-namespace scores unchanged, off-namespace filtering cannot lower their ranks. Top-20 anchor recall increases from 0.432 to 0.533, 80% recall feasibility from 0.237 to 0.311, and exact similarity evaluations decrease by 98.3%. In a frozen 72-case development diagnostic, a released-metadata reference preserves required evidence, whereas neither text-only verifier detects violations under the 1% required-anchor false-denial limit. Across 1,523 paired benchmark-native cases, namespace routing is associated with judged-accuracy gains of 0.053-0.068 across three readers; recall also changes, so this comparison is observational. In 16 controlled exposure scenarios, only one of four reader-specific 95% confidence intervals excludes zero for relevant-inadmissible literal disclosure (+0.156, 95% CI \\[0.031, 0.312\\]). Results motivate separate verification of candidate support, admissibility, prompt exposure, and answer disclosure.",
  "published": "2026-10-05",
  "updated": "2026-10-05",
  "primary_category": "cs.AI",
  "categories": "cs.AI, cs.IR, cs.MA",
  "comment": "",
  "pdf": "https://arxiv.org/pdf/2610.07309v1",
  "url": "https://arxiv.org/abs/2610.07309"
}
```
