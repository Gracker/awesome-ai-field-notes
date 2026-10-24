# Adaptive Skill Granularity for Coding Agents: Runtime Routing and Macro-to-Micro Recovery

- **ID**: ce9ec04f
- **原文链接**: https://arxiv.org/abs/2610.31461
- **PDF**: https://arxiv.org/pdf/2610.31461
- **作者**: Dingxuan Zhang, Yanhui Jiang, Jun Wang, Hefeng Zhou
- **日期**: 2026-10-22
- **更新**: 2026-10-22
- **分类**: coding
- **来源类型**: paper
- **标签**: coding-agents, skill-library, action-abstraction, failure-recovery
- **质量评分**: 4/5
- **抓取时间**: 2026-10-24 04:22 UTC

---

## 中文导读

编码代理把流程打包成可复用技能后，运行时仍要决定用原始工具调用宏技能还是"宏起步微回退"的混合执行这是已有技能研究基本没碰的运行时控制问题论文把技能粒度当成动作抽象策略：特征化粒度控制器按任务结构执行状态和宏技能失败动态路由，配有限状态恢复执行器做宏到微的显式回退在验证器定义成功的确定性协议上评估宏采用率失败恢复路由匹配转移正确性等过程指标：固定宏执行在匹配时高效错配时脆弱，运行时路由加显式回退能恢复固定粒度解决不了的受控宏失败技能库应被视为可控可验证可恢复的执行抽象，而不只是可检索资源

## 为什么值得关注

编码代理的技能粒度应当运行时路由：宏失败自动回退微级恢复，技能库从检索资源升级为可控执行抽象 Relevance for field notes: treats skill granularity as a runtime action-abstraction policy for coding agents - fixed macro execution is efficient but brittle under mismatch, while routing with an explicit finite-state macro-to-micro recovery recovers controlled macro failures that fixed granularity leaves unresolved.

## 关键信息

- 论文标题: Adaptive Skill Granularity for Coding Agents: Runtime Routing and Macro-to-Micro Recovery
- 作者: Dingxuan Zhang, Yanhui Jiang, Jun Wang, Hefeng Zhou
- arXiv: https://arxiv.org/abs/2610.31461
- 发布时间: 2026-10-22
- arXiv 分类: cs.AI, cs.SE
- 关联标签: coding-agents, skill-library, action-abstraction, failure-recovery

## English Abstract

Reusable skills allow large language model agents to package task-specific procedures, tool affordances, and execution guidance into modular units. Prior work has largely studied how agents retrieve, compose, or synthesize skills before execution. In coding agents, however, execution poses an additional runtime control problem: the same task may be solved through primitive tool calls, macro skills, or hybrid execution that starts with a macro and falls back to micro-level recovery. We introduce Adaptive Skill Granularity, a framework that treats skill granularity as an action-abstraction policy conditioned on task structure, execution state, and macro-skill failures. The system combines a feature-based granularity controller and a finite-state recovery executor. We evaluate the framework with a deterministic coding-agent protocol using verifier-defined success, total cost, and process metrics such as macro adoption, failure recovery, route match, and transition correctness. Results show that fixed macro execution is efficient when applicable but brittle under mismatch, while runtime routing and explicit macro-to-micro recovery improve robustness and recover controlled macro failures that fixed-granularity execution leaves unresolved. Our findings suggest that skill libraries for coding agents should be treated not only as retrievable resources, but also as controllable, verifiable, and recoverable execution abstractions.

## English Summary

Reusable skills let coding agents package procedures and tool guidance into modular units, but execution adds a runtime control problem prior work ignores: the same task may go through primitive tool calls, macro skills, or hybrid execution with macro-to-micro fallback. Adaptive Skill Granularity treats granularity as an action-abstraction policy conditioned on task structure, execution state, and macro failures, pairing a feature-based controller with a finite-state recovery executor. On a deterministic protocol with verifier-defined success and process metrics, fixed macro execution is efficient when applicable but brittle under mismatch, while runtime routing plus explicit macro-to-micro recovery improves robustness and recovers controlled macro failures that fixed granularity leaves unresolved. Skill libraries are controllable, verifiable, recoverable execution abstractions.

## Obsidian Notes

- Fetched 2026-10-24 04:22 UTC via `opencli arxiv paper 2610.31461 -f json`; page grounded in arXiv title/authors/abstract/dates/categories only.
- Chinese body anchors on the entry's summary_zh; no experimental details beyond the abstract were added.
