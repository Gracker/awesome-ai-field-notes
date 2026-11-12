# Continual-ARC: Measuring Skill Acquisition over a Working Lifetime

- **ID**: baab05ce
- **原文链接**: https://arxiv.org/abs/2611.14505
- **PDF**: https://arxiv.org/pdf/2611.14505v1
- **作者**: Daniel Lenton
- **日期**: 2026-11-10
- **更新**: 2026-11-10
- **分类**: agents
- **来源类型**: paper
- **标签**: continual-learning, agent-harness, arc-agi, benchmark, memory
- **质量评分**: 4/5
- **抓取时间**: 2026-11-12T12:28:46Z

---

## 中文导读

Continual-ARC 把三个 ARC-AGI 版本拼成一条终身任务流：旧任务在休眠间隔后带全新实例回归，新任务同时持续到来，任务本身不需要领域知识。每个实例上学习者可以付费购买示例、提交答案或在 harness 内行动，错误提交允许重试但同样计费，得分按消耗掉的反馈预算比例计算；由于允许学习者在实例之间保留任意状态，记忆型（agent harness）与权重型学习第一次被放在同一尺度比较。流结束后冻结学习者，在见过的任务新实例上测记忆、在未见过的任务上测泛化。作者用带/不带持久化的 agent harness（Qwen3.5-9B、GLM-5.3 Flash）对照两个 prompting floor、一个程序归纳方法和把 GLM-5.3 Flash 蒸馏进 Qwen3.5-9B 权重的做法，结果：harness 持久化若无显式专家指引基本不改善记忆；大多数 harness 方法仍学不过一个只缓存每个任务示例的 prompting floor；没有任何 harness 方法在未见任务上获益，而权重型学习有实质收益。

## 为什么值得关注

条目一句话：Continual-ARC 用三个 ARC-AGI 版本构成终身任务流，让记忆型（agent harness）与权重型学习在同一尺度比较。对 agent 记忆与技能库路线这是一个偏冷水的信号：在按反馈预算计分的公平尺度下，纯 harness 记忆目前跑不过最朴素的示例缓存，泛化收益目前只出现在权重侧。代码与运行记录已开源（unifyai/continual-arc），基准本身可复用。

## 关键信息

- 论文标题：Continual-ARC: Measuring Skill Acquisition over a Working Lifetime
- 作者：Daniel Lenton
- arXiv：https://arxiv.org/abs/2611.14505
- PDF：https://arxiv.org/pdf/2611.14505v1
- 发布时间：2026-11-10
- arXiv 分类：cs.LG
- 备注：51 pages, 13 figures. Code and run records: https://github.com/unifyai/continual-arc
- 关联标签：continual-learning, agent-harness, arc-agi, benchmark, memory

## English Abstract

Agent harnesses have emerged as a promising mechanism for continual learning, alongside test-time parametric learning. However, the current benchmarks have several limitations: they generally focus on a single applied domain, serve each instance only once, and assume a single family of learner, so memory-based and weight-based systems are rarely compared on the same scale. We propose Continual-ARC, a lifelong stream built from the three ARC-AGI editions, whose tasks need no domain knowledge. The same tasks return after dormant gaps with fresh instances, while new tasks keep arriving. On each instance, the learner may pay for demonstrations, submit answers, or act inside the harness, with retries permitted on incorrect submissions, which are paid for. Each instance is scored based on the share of this feedback budget consumed. Since a learner may keep anything between instances, memory-based and weight-based systems are scored on the same scale. After the stream, the learner is frozen and tested on fresh instances of the tasks it met, which measures memorization, and on unseen tasks, which measures generalization. We run an agent harness with frozen weights, with and without persistence, on Qwen3.5-9B and GLM-5.3 Flash, comparing them with two prompting floors, a program-induction method and Qwen3.5-9B's weights trained to imitate GLM-5.3 Flash. Persistence in the harness generally does not improve memorization unless provided with explicit expert guidance. Most harness-based methods still learn less than a floor that simply caches each task's demonstrations, across all models we tested. No harness-based method gains on unseen tasks, whereas weight-based learning shows substantial gains. This opens the door to future weight-based continual learning that could teach models to drive harnesses in new domains.

## English Summary

Continual-learning benchmarks assume one domain, one-shot instances, and one learner family, so memory-based agent harnesses and weight-based learners are rarely compared on the same scale. Continual-ARC is a lifelong stream built from the three ARC-AGI editions: tasks return after dormant gaps while new tasks keep arriving; learners may pay for demonstrations or submit answers with paid retries, each scored by feedback budget consumed. After the stream, learners are frozen and tested on fresh instances of seen tasks (memorization) and on unseen tasks (generalization). Experiments with frozen-weight harnesses on Qwen3.5-9B and GLM-5.3 Flash: persistence rarely improves memorization without expert guidance, most harness methods learn less than a simple demonstration-caching floor, and none gains on unseen tasks while weight-based learning shows substantial gains.

## Obsidian Notes

- 内容由 opencli arxiv paper 拉取 arXiv 元数据与摘要生成。中文导读与价值判断均锚定在条目已有摘要、论文摘要、作者、日期与分类信息上；未补充论文摘要之外的实验细节。
