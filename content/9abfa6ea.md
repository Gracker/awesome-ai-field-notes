# Harness^2: Recursive Agent Harnessing for an Open World

- **ID**: 9abfa6ea
- **原文链接**: https://arxiv.org/abs/2610.14224
- **PDF**: https://arxiv.org/pdf/2610.14224
- **作者**: Ruiyao Xu, Yanfei Chen, et al.
- **日期**: 2026-10-09
- **分类**: agents
- **来源类型**: paper
- **标签**: recursive-self-improvement, agent-harness, tool-use, open-world
- **质量评分**: 3/5
- **抓取时间**: 2026-11-15T15:43:33Z

---

## 中文导读

LLM agent 的能力不只取决于模型，也取决于执行 harness。递归自改进（RSI）可以自动演化 harness，但开放世界部署有两难：任务在设计期未见、测试期新颖，没有 ground-truth verifier 可靠指导在线改动；RSI 过程又高度任务特化、难以泛化。Harness² 用两级递归应对：任务级递归用对比式 Propose-Probe-Compose 在无 verifier 下可靠引导 harness 编辑，可并行或串行扩展；harnessing 级递归从编辑记录中提取经验更新一个持续改进 harness。三个专业基准、四个模型-harness 配置上，单步即让 GLM-5 与 Gemini 3.5 Flash 超基线：WorkBuddy-Bench 最高 +11.5 分、JobBench +4.5 分、LAB +11.8 pp。

## 为什么值得关注

把「改脚手架」从手工经验变成两级递归框架，且不依赖 ground-truth verifier——与依赖 verifier 的 RSI 路线互补；对日常调 agent harness 的人，Propose-Probe-Compose 是否能缩成一个本地 loop 值得直接实验。

## 关键信息

- 论文标题：Harness^2: Recursive Agent Harnessing for an Open World
- 作者：Ruiyao Xu, Yanfei Chen, et al.
- arXiv：https://arxiv.org/abs/2610.14224
- 发布时间：2026-10-09
- arXiv 分类：c, s, ., A, I, ,,  , c, s, ., C, L, ,,  , c, s, ., L, G
- 关联标签：recursive-self-improvement, agent-harness, tool-use, open-world

## English Abstract

LLM agents' capabilities depend not only on their underlying models but also on their execution harnesses. Recursive self-improvement (RSI) offers a promising approach to automatically evolve these harnesses. However, deploying RSI in open-world settings still faces two critical challenges. First, open-world tasks are typically unseen during the harness design phase and novel at test time, leaving no ground-truth verifiers to reliably guide online harness edits. Second, the RSI process remains highly task-specific and fails to generalize to novel scenarios. We introduce Harness^2, a plug-and-play, recursive agent harnessing framework that addresses these challenges through two connected levels of recursion. Task-level recursion refines the current task's harness using a contrastive Propose-Probe-Compose step that reliably guides edits without ground-truth verifiers, and can be scaled further via parallel or sequential recursion. Harnessing-level recursion then extracts experience from these edits to update a continual improvement harness, enabling the agent to better adapt to future tasks. Across three professional benchmarks and four model-harness configurations, a single step consistently improves GLM-5 and Gemini 3.5 Flash over their base harnesses, yielding gains of up to 11.5 points on WorkBuddy-Bench, 4.5 points on JobBench, and 11.8 percentage points on LAB, with further gains as the task-level recursion budget increases.

## English Summary

LLM agent capability depends on execution harnesses as much as models. Recursive self-improvement (RSI) can evolve harnesses automatically, but open-world deployment faces two gaps: tasks unseen at design time leave no ground-truth verifiers to guide online edits, and RSI remains task-specific. Harness^2 answers with two recursion levels: task-level recursion refines the harness via a contrastive Propose-Probe-Compose step that guides edits without verifiers, scalable by parallel or sequential recursion; harnessing-level recursion distills experience from those edits into a continual-improvement harness. Across three professional benchmarks and four model-harness configs, one step lifts GLM-5 and Gemini 3.5 Flash over base harnesses: up to +11.5 points on WorkBuddy-Bench, +4.5 on JobBench, +11.8 pp on LAB.

## Obsidian Notes

- 内容获取路径：`opencli arxiv paper 2610.14224 -f json` 拉取 arXiv 元数据与摘要生成。
- 中文导读与价值判断均锚定在已抓取的原文/摘要/元数据上；未补充来源之外的细节。
- 现代站点生成器按 `content/<entry.id>.md` 查找内容页；本文件写入 canonical content 目录，而不是 `openclaw/content/`。
