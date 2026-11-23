# Realized versus Population Reliability: Anytime-Valid Self-Consistency Certification under Correlated Reasoning

- **ID**: ecae9dde
- **原文链接**: https://arxiv.org/abs/2611.26592
- **PDF**: https://arxiv.org/pdf/2611.26592v1
- **作者**: Terence D. Agbeyegbe, Toneukarin G. Agbeyegbe
- **日期**: 2026-11-19
- **更新**: 2026-11-19
- **分类**: models
- **来源类型**: paper
- **标签**: anytime-valid, e-process, self-consistency, statistical-guarantee, correlated-sampling
- **质量评分**: 4/5
- **抓取时间**: 2026-11-23T04:21:29Z

---

## 中文导读

自一致性认证把重复采样当序列证据，e-process 过阈值即停，默认各 rollout 条件独立该假设不成立：推理流因共享前缀或跨 prompt 异质性正相关，被认证的假设随之改变，不只是证书效率随机效应模型下零假设分裂为 realized null（本次信念）与 population null（平均行为）：标准 betting e-process 只对 realized 有效，单元内有效样本量饱和，多采救不回 population 有效性；prompt 级 e-process 可救，最优每 prompt 一采Haiku 4.5 实验：GSM8K 差距休眠，AIME 上单单元规则在名义 0.05 下 24% 越界，prompt 级保持 0.00对 c17db9bd 所属路线是正确性修正

## 为什么值得关注

rollout 相关性会让自一致性证书认错假设：AIME 上 24% 越界，prompt 级 e-process 才保 population 有效性。

自一致性证书的标准构造假设 rollout 条件独立，而推理流通过共享前缀等机制正相关。论文证明相关性改变的不只是效率，而是被认证的假设本身：GSM8K 上差距沉睡，AIME 上 nominal ε=0.05 时单单元规则在 24% 的 prompt 上越界，prompt 级 e-process 则守住（0.00）——这是可靠性声明解释边界的纠偏结果。

## 关键信息

- 论文标题：Realized versus Population Reliability: Anytime-Valid Self-Consistency Certification under Correlated Reasoning
- 作者：Terence D. Agbeyegbe, Toneukarin G. Agbeyegbe
- arXiv：https://arxiv.org/abs/2611.26592
- 发布时间：2026-11-19
- arXiv 分类：stat.ME, cs.AI, cs.LG
- 关联标签：anytime-valid, e-process, self-consistency, statistical-guarantee, correlated-sampling

## English Abstract

Self-consistency certification treats repeated sampling from a language model as sequential evidence accumulation and stops when an anytime-valid e-process crosses a threshold, guaranteeing finite-sample Type I error control by Ville's inequality. Prior constructions assume sampled rollouts are conditionally independent. We show this assumption fails in practice: reasoning streams are positively correlated through shared reasoning prefixes or across-prompt heterogeneity, changing not merely certificate efficiency but the hypothesis certified. Modeling dependence via a per-unit latent state (the random-effects / intraclass-correlation structure) induces exchangeable, equi-correlated increments with correlation $ρ$. Correlation splits the single null into a realized null about the drawn belief and a population null about average model behavior, which coincide only when $ρ=0$. We show: (i) the standard betting e-process remains anytime-valid for the realized null, not the population null; (ii) read as a population-null test, a suitable mixture has asymptotic crossing probability at least $π=P(μ(Z)>0)$, potentially exceeding nominal $ε$; (iii) the within-unit mean's effective sample size saturates at $1/ρ$, so extra within-unit rollouts cannot restore population validity; and (iv) a prompt-level e-process restores population validity, with optimal allocation at one rollout per prompt under a pure rollout budget. Simulations and Claude Haiku 4.5 rollouts confirm this regime dependence: on GSM8K ($\hatρ=0.435$, $\hatθ=+0.96$) the gap is dormant, whereas on AIME ($\hatρ=0.480$, $\hatθ=-0.15$) the single-unit rule crosses on 24% of prompts at nominal $ε=0.05$, while the prompt-level procedure declines (0.00). This correctness result identifies which reliability claim an anytime-valid certificate actually supports under dependence.

## English Summary

Anytime-valid self-consistency certification accumulates repeated LLM sampling and stops via an e-process threshold, assuming conditionally independent rollouts. That assumption fails: reasoning streams correlate positively through shared prefixes or across-prompt heterogeneity, changing not just certificate efficiency but which hypothesis is certified. Under a random-effects dependence model, the null splits into a realized null (the drawn belief) and a population null (average behavior). The standard betting e-process stays valid only for the realized null; within-unit effective sample size saturates, so extra rollouts cannot restore population validity; a prompt-level e-process restores it, one rollout per prompt. On Claude Haiku 4.5 the gap is dormant on GSM8K; on AIME the single-unit rule crosses on 24% of prompts at nominal 0.05, where the prompt-level procedure stays at 0.00.

## Obsidian Notes

- 内容由 `opencli arxiv paper` 拉取 arXiv 元数据与摘要生成。
- 中文导读与价值判断均锚定在条目已有摘要、论文摘要、作者、日期与分类信息上；未补充论文摘要之外的实验细节。
