# The Last Mile to the Real World: agent-native primitives as reusable building blocks

- **ID**: c2aaea20
- **来源链接**: https://arxiv.org/abs/2611.07461
- **PDF**: https://arxiv.org/pdf/2611.07461
- **arXiv 分类**: cs.CL, cs.AI, cs.LG, cs.MA, cs.SE
- **作者**: Haibo Jin, Peng Kuang, Xiaopeng Yuan, et al.
- **原文日期**: 2026-11-05
- **分类**: agents
- **来源类型**: paper
- **标签**: agent-harness, terminal-bench, primitives, real-world-tasks
- **质量评分**: 4/5
- **抓取时间**: 2026-11-10T15:44:12Z

---

## 中文导读

前沿模型配上自家 harness 在真实任务基准上仍吃力：Terminal-Bench 4.0 上 GPT-5.6 Sol+Codex 37.3%、Claude Opus 5+Claude Code 51.8%。论文把失败集中点命名为「最后一公里」——资源够到了，却用不上：现有方案只把资源放进可达范围，把应用能力留给调用方，每个 harness 都重造一遍。提出 agent-native primitives：给资源配上驻留 LLM，在上下文里完成应用并与其他 primitive 通信，作为可复用积木，配套 HEELO harness 框架。

## 为什么值得关注

把 agent 真实任务失败的结构性原因从「模型不够强」转向「应用能力没有沉淀」：够到资源与真正用上资源之间缺一层可复用积木。与并行小团队（2611.09798）的结论互补——真实任务成功率的提升来自结构化拆解，而不只是更大的模型或更长的思考。

## 关键信息

- Terminal-Bench 4.0 页述数字：GPT-5.6 Sol+Codex 37.3%、Claude Opus 5+Claude Code 51.8%
- 失败集中点：从「够到资源」到「真正用上」的最后一公里；每个 harness 重造应用能力
- 方案：agent-native primitives——资源自带驻留 LLM，在上下文应用并与其它 primitive 通信；配套 HEELO 框架
- arXiv 2611.07461，2026-11-05，cs.CL/cs.AI/cs.LG/cs.MA/cs.SE；HF 日榜 27 赞

## English Abstract

How can an agent handle a real-world task end to end? Frontier models with their own harnesses still fall short on real-world benchmarks: on Terminal-Bench 4.0, GPT-5.6 Sol with Codex resolves 37.3% of the tasks and Claude Opus 5 with Claude Code 51.8%. These tasks fail at the step from reaching a resource to applying it, which we call the last mile to the real world. Existing approaches put the resource within reach but leave the competence to apply it with the caller, so each harness rebuilds that competence. We introduce agent-native primitives, reusable units that equip a resource with a resident LLM that applies it in context and communicates with other primitives, and HEELO (Harness En...).

## English Summary

Frontier models with their own harnesses still fall short on real-world benchmarks: on Terminal-Bench 4.0, GPT-5.6 Sol with Codex resolves 37.3% and Claude Opus 5 with Claude Code 51.8%. The paper names the failure concentration the last mile: tasks fail at the step from reaching a resource to applying it. Existing approaches put the resource within reach but leave the competence to apply it with the caller, so every harness rebuilds it. Agent-native primitives attach a resident LLM to a resource that applies it in context and communicates with other primitives as reusable building blocks, with the HEELO harness framework. Complementary to parallel-agent-teams findings: real-task gains come from structure, not just bigger models.
