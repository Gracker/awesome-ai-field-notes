# When "Must" Becomes "Maybe": Constraint Weakening in LLM Agent Workflows

- **ID**: cfd2ef03
- **原文链接**: https://arxiv.org/abs/2608.24569
- **PDF**: https://arxiv.org/pdf/2608.24569v1
- **作者**: Yiheng Sun, Huifei Wang, Yancheng Zhu, Zhenyu Li, Zebin Zhao, Yifan Yuan
- **日期**: 2026-08-25
- **更新**: 2026-08-25
- **分类**: agents
- **来源类型**: paper
- **标签**: agents, multi-agent, handoff, safety, arxiv
- **质量评分**: 4/5

---

## 中文导读

多角色多阶段 agent 流水线里，上游状态被持续改写成摘要、计划、工单、交接笔记等中间语言工件。本文量化一个此前很少被量化的问题：工件在话题上保留了某条件，但条件已从「执行前必须解决的要求」降格成「仅供参考的信息」。用安全阻塞项做受控实验（每源状态有明确前置、权限、回退、后果），在上游识别正确的前提下改变交接方式，共 1,296 个受控 episode：直接原样交接保住全部阻塞项；压缩、计划吸收、趋同、所有权推让、先例替换都会把硬约束降格——普通交接压缩下失效率 100.0%、出现禁止动作 54.2%；补全四个状态字段后保存率回到 100.0%、禁止动作归零；下游再加验证可消除禁止动作，但工件本身仍以 95.3% 比例失活——语义在场和操作绑定是两个变量。

## 为什么值得关注

交接压缩会让硬约束静默降格：普通压缩 100% 失效+54.2% 禁止动作；四字段完整+下游验证是可直接搬走的协议修复

## English Abstract

Large language model (LLM) agents coordinate complex tasks through multi-role and multi-stage workflows. Upstream state is repeatedly transformed into intermediate language artifacts, such as summaries, plans, tickets, memories, and handoff notes, from which downstream components act. For action-constraining state, topical retention is insufficient: an artifact may mention an unresolved condition while changing it from a requirement that must be resolved before execution into information that may merely inform the next action. We study this action-binding role as operational state preservation. Safety blockers provide a controlled instance because each source state has an explicit prerequisite, authority, fallback, and execution consequence. We condition on correct upstream identification, vary the handoff transformation, and evaluate an executor restricted to the resulting artifact. Across 1,296 controlled synthetic episodes, direct-handoff controls preserve every blocker, whereas compression, plan assimilation, convergence, ownership deferral, and precedent substitution repeatedly turn binding state into caveats or non-binding considerations. Normal handoff compression produces 100.0% deactivation and 54.2% forbidden action. Restoring all four state fields raises preservation to 100.0% and reduces forbidden action to 0.0%. Fixed-artifact interventions further separate preservation from containment: downstream verification eliminates forbidden action while artifact deactivation remains 95.3%. These results identify a state-transmission failure between information extraction and action. Handoff transformations can retain state content while weakening its constraints on downstream action. Semantic availability does not guarantee operational preservation.

## Obsidian Notes

- Metadata and abstract fetched via `opencli arxiv paper 2608.24569 -f json` (2026-08-27); response parsed list-or-dict tolerant.
- 1,296 episode 受控实验；四字段=prerequisite/authority/fallback/consequence。
- 中文导读与价值判断锚定在论文摘要上，未补充摘要之外的实验细节。
