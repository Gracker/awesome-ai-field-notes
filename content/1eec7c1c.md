# TRIM: Reducing AI-Generated CodeSlop via Agent Trajectory Minimization

- source_url: https://arxiv.org/abs/2607.18161
- source_type: paper
- platform: arxiv
- author: Alex Mathai, Shobini Iyer, Aleksandr Nogikh, Petros Maniatis, Franjo Ivancic, Junfeng Yang, Baishakh...
- original_date: 2026-07-20
- added_date: 2026-07-22
- arxiv_id: 2607.18161
- arxiv_categories: cs.SE, cs.AI, cs.OS
- pdf_url: https://arxiv.org/pdf/2607.18161v1
- category: coding
- tags: coding-agents, codeslop, trajectory-minimization, code-quality, trim, arxiv
- quality_score: 4

## 摘要（中文）

指出 coding agent 最终补丁臃肿主因是搜索轨迹中残留的试探性编辑与废弃假设（CodeSlop），并提出 TRIM：通过最小化 agent 轨迹间接削减冗余，跨多种 agent scaffold 将 CodeSlop 降低约 17.9%32.9%，性能回归可忽略，验证成本约为 Delta Debugging 类基线的一半收录理由：把AI 生成代码越写越胀落到可度量现象与可落地后处理算法，对长期 agent 维护代码库有直接工程价值

## Summary (English)

Coding agents are increasingly used to accelerate code generation in many downstream tasks, such as fixing bugs, building applications, and prototyping. However, despite their value as coding assistants, agent-generated code tends to be larger and more verbose than the corresponding human-written implementation. In this work, we show that the cause lies in the agent's own search process: while iterating toward a passing solution, an agent accumulates speculative edits, abandoned hypotheses, and temporary changes that persist into the final patch. This may seem harmless for a single patch, but the problem compounds as agents take responsibility for ever-larger portions of a codebase-a codebase that was once minimal and well-maintained slowly accumulates redundancy faster than it can be cleaned up, drifting to a state that is harder to maintain. Given the magnitude of this problem, we take a step towards alleviating this issue. First, we formally define this phenomenon as CodeSlop-the residual and functionally unnecessary edits commonly seen in AI-generated code. We then introduce our algorithm TRIM (Trajectory-guided Redundancy Identification and Minimization). Rather than minimizing CodeSlop directly, TRIM instead minimizes agent trajectories. As we show empirically, this indirect technique of minimizing CodeSlop is highly effective: TRIM cuts CodeSlop by 17.9%-32.9% across agentic scaffolds, with negligible performance regression. TRIM is also highly efficient, requiring roughly half the validation cost of algorithmic baselines such as Delta Debugging.

## One-liner

指出 coding agent 最终补丁臃肿主因是搜索轨迹中残留的试探性编辑与废弃假设（CodeSlop），并提出 TRIM：通过最小化 agent 轨迹间接削减冗余，跨多种 agent scaffold 将 CodeSlop 降低约 17.

## 原文 / 元数据抓取

# TRIM: Reducing AI-Generated CodeSlop via Agent Trajectory Minimization
> 作者: Alex Mathai, Shobini Iyer, Aleksandr Nogikh, Petros Maniatis, Franjo Ivancic, Junfeng Yang, Baishakhi Ray
> 原文链接: https://arxiv.org/abs/2607.18161
> PDF: https://arxiv.org/pdf/2607.18161v1
> 发布时间: 2026-07-20
> 更新时间: 2026-07-20
> 分类: cs.SE, cs.AI, cs.OS

---

Coding agents are increasingly used to accelerate code generation in many downstream tasks, such as fixing bugs, building applications, and prototyping. However, despite their value as coding assistants, agent-generated code tends to be larger and more verbose than the corresponding human-written implementation. In this work, we show that the cause lies in the agent's own search process: while iterating toward a passing solution, an agent accumulates speculative edits, abandoned hypotheses, and temporary changes that persist into the final patch. This may seem harmless for a single patch, but the problem compounds as agents take responsibility for ever-larger portions of a codebase-a codebase that was once minimal and well-maintained slowly accumulates redundancy faster than it can be cleaned up, drifting to a state that is harder to maintain. Given the magnitude of this problem, we take a step towards alleviating this issue. First, we formally define this phenomenon as CodeSlop-the residual and functionally unnecessary edits commonly seen in AI-generated code. We then introduce our algorithm TRIM (Trajectory-guided Redundancy Identification and Minimization). Rather than minimizing CodeSlop directly, TRIM instead minimizes agent trajectories. As we show empirically, this indirect technique of minimizing CodeSlop is highly effective: TRIM cuts CodeSlop by 17.9%-32.9% across agentic scaffolds, with negligible performance regression. TRIM is also highly efficient, requiring roughly half the validation cost of algorithmic baselines such as Delta Debugging.

## Obsidian intake evidence excerpt

该内容文件由 AAIF content-fetcher 根据 active/high-score entry 与 OpenCLI arXiv 元数据补齐。

- entry_id: 1eec7c1c
- title: TRIM: Reducing AI-Generated CodeSlop via Agent Trajectory Minimization
- source: https://arxiv.org/abs/2607.18161
- existing_summary_zh: 指出 coding agent 最终补丁臃肿主因是搜索轨迹中残留的试探性编辑与废弃假设（CodeSlop），并提出 TRIM：通过最小化 agent 轨迹间接削减冗余，跨多种 agent scaffold 将 CodeSlop 降低约 17.9%32.9%，性能回归可忽略，验证成本约为 Delta Debugging 类基线的一半收录理由：把AI 生成代码越写越胀落到可度量现象与可落地后处理算法，对长期 agent 维护代码库有直接工程价值
