# MAP-Graph: Provenance-Aware Shared Memory for Multi-Agent Workflows

> Source: https://arxiv.org/abs/2608.10509
> Author: Yiqi Wang, Zihao Yan, Jiaqi Zhang, Zhangkai Wu, Mingkai Zheng, Zequn Sun, Yanming Zhu, Taotao Cai
> Original date: 2026-08-11
> Added by: AAIF daily-intake-evening 2026-08-13

## 摘要
MAP-Graph 把 multi-agent workflow 中的 agent、source、memory、claim、action 建成 typed execution graph，并把 provenance 变成运行时控制信号：lineage tracing、permission-ineligible record exclusion、semantic similarity × path trust reranking、risk-sensitive action gate。2,700 个合成任务上达到 94.96% task success。

## English Summary
Shared memory helps language-model agents reuse information across long workflows, yet relevant evidence may not be admissible for a particular agent or action. Because restrictions propagate through derivations, summaries can conceal private, poisoned, untrusted, or revoked sources, enabling unauthorized reads or unsafe actions. Existing approaches provide semantic retrieval, scoped access, or lineage tracking, but do not clearly separate hard authorization from graded trust or adapt evidence requirements to action risk. We introduce MAP-Graph, a provenance-aware memory layer that represents agents, sources, memories, claims, and actions in a typed execution graph. It traces ancestry, excludes permission-ineligible records, reranks eligible memories by semantic similarity and multiplicative path trust, and applies a risk-sensitive gate before action execution while retaining affected lineage for audit. On a controlled benchmark of 2,700 synthetic tasks per method across three domains, MAP-Graph achieves 94.96\% overall task success, 72.70\% exact decision accuracy, and 90.22\% in the clean setting, where success requires a correct \textsc{Allow} rather than a safe intervention. Ablations isolate the roles of permission filtering, path trust, and action gating, while transfer tests with two additional backbones preserve the exact-decision and access-control advantages. These results support provenance as an operational control signal, rather than only post-hoc audit metadata, within the evaluated setting.

## 入库理由
- quality_score: 5
- category: agents
- tags: multi-agent, shared-memory, provenance, risk-gate, agent-safety
- one_liner: MAP-Graph 把 provenance 从事后审计变成 multi-agent memory 的运行时安全门。

## Obsidian evidence excerpt
```markdown
idian/OpenClaw定时任务/论文流水线/2026-08-13-论文流水线.md`
- Evidence: `/Users/gracker/.hermes/evidence/paper-pipeline/2026-08-13/`

## 今日论文速报

今天 arXiv recent 覆盖 `cs.AI / cs.CL / cs.LG / cs.CV / cs.RO / cs.MA` 六个分类共 254 篇去重提交。本轮最有信号的方向是 **Agent 记忆与自演化基础设施**——多条线从不同角度在做同一件事：把"retrieve-only"换成"compile + skill + provenance"。`SkillZip / Muscle Memory / GeoForge / MAP-Graph / EvoMem` 形成今天的"memory 范式切换"主线；`Self-Evolving GUI Grounding` + `SPIEval` 把这条主线拉到 GUI/移动端；`ReRound / Gated VLA-Cache` 提供 on-device 推理的量化与缓存路径。安全侧一条新的攻击面：`Trajectory Backdoor Attack` 直接攻击 self-evolving skill 的可信演化管道。

1. **SkillZip: Evaluation-Free Skill Compression for Self-Evolving Agents by Discovering Reusable Structure** — arXiv:2608.11079。把 self-evolving agent 累积的 skill 当成"typed contract"——名字/描述/工作流/工具契约/输出字段/例外规则——用 typed minimum description-length 目标一次性压缩：重复规则 state once at scope，重复动作序列 factor into shared procedure，例外保留为 explicit exceptions。Zip-on-Write 模式支持 incremental 演化不重放任务。压缩率高、保留 unique rare rules by construction。
   来源：https://arxiv.org/abs/2608.11079

2. **Muscle Memory for Agents: Compile not Merely Retrieve** — arXiv:2608.08995。主张把"反复出现的用户意图"编译成 purpose-built specialist agent，而不是 retrieve-then-orchestrate。Harvest→Analyze→Augment→Evaluate 四阶段管线，从对话历史中分别挖出 behavioral pattern 和 task pattern，发出的 specialist 配 two-stage trigger matching。90 held-out scenario 上 specialist 触发时 88.9% 胜率，+2.05 personalisation gain，accuracy 损失仅 -0.28（1-4 scale）。
   来源：https://arxiv.org/abs/2608.08995

3. **GeoForge: Non-Parametric Self-Evolving Agents for Earth-Observation Reasoning** — arXiv:2608.10494。Training-free self-evolving 框架，把完成的轨迹压成结构化 nonparametric execution state——Workflow Graph Memory（全局操作顺序）+ Action-Level Experiences（局部纠错）+ Adapted Skill SOP（程序与数据约束）。执行、蒸馏、复用三段循环里 backbone LLM 不变。多个 geospatial benchmark 上同时拉高 task accuracy 和 tool-use trajectory quality。
   来源：https://arxiv.org/abs/2608.10494

4. **MAP-Graph: Provenance-Aware Shared Memory for Multi-Agent Workflows** — arXiv:2608.10509。把 agent、source、memory、claim、action 全部建模成 typed execution graph：lineage tracing + permission-ineligible record exclusion + semantic similarity × multiplicative path trust reranki
```

## arXiv metadata / abstract
- arXiv id: 2608.10509
- authors: Yiqi Wang, Zihao Yan, Jiaqi Zhang, Zhangkai Wu, Mingkai Zheng, Zequn Sun, Yanming Zhu, Taotao Cai
- published: 2026-08-11
- updated: 2026-08-11
- categories: cs.AI, cs.MA
- PDF: https://arxiv.org/pdf/2608.10509v1

Shared memory helps language-model agents reuse information across long workflows, yet relevant evidence may not be admissible for a particular agent or action. Because restrictions propagate through derivations, summaries can conceal private, poisoned, untrusted, or revoked sources, enabling unauthorized reads or unsafe actions. Existing approaches provide semantic retrieval, scoped access, or lineage tracking, but do not clearly separate hard authorization from graded trust or adapt evidence requirements to action risk. We introduce MAP-Graph, a provenance-aware memory layer that represents agents, sources, memories, claims, and actions in a typed execution graph. It traces ancestry, excludes permission-ineligible records, reranks eligible memories by semantic similarity and multiplicative path trust, and applies a risk-sensitive gate before action execution while retaining affected lineage for audit. On a controlled benchmark of 2,700 synthetic tasks per method across three domains, MAP-Graph achieves 94.96\% overall task success, 72.70\% exact decision accuracy, and 90.22\% in the clean setting, where success requires a correct \textsc{Allow} rather than a safe intervention. Ablations isolate the roles of permission filtering, path trust, and action gating, while transfer tests with two additional backbones preserve the exact-decision and access-control advantages. These results support provenance as an operational control signal, rather than only post-hoc audit metadata, within the evaluated setting.
