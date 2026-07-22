# Harness Handbook: Making Evolving Agent Harnesses Readable,Navigable, and Editable

- source_url: https://arxiv.org/abs/2607.13285
- source_type: paper
- platform: arxiv
- author: Ruhan Wang, Yucheng Shi, Zongxia Li, Zhongzhi Li, Yue Yu, Junyao Yang, Kishan Panaganti, Haitao Mi, Dongruo Zhou, Leoweiliang
- original_date: 2026-07-14
- added_date: 2026-07-22
- arxiv_id: 2607.13285
- arxiv_categories: cs.AI, cs.SE
- pdf_url: https://arxiv.org/pdf/2607.13285v1
- category: agents
- tags: agent-harness, behavior-localization, code-navigation, harness-evolution, arxiv
- quality_score: 4

## 摘要（中文）

现代 AI agent 能力不仅取决于基座模型，也取决于 harness（构造 prompt、管理状态、调用工具、协调执行）。模型、API、环境与需求持续变化时 harness 必须不断修改，而修改前的核心瓶颈是行为定位：生产 harness 体量大、耦合紧、行为分散，修改请求描述“应做什么”，仓库却按文件/模块组织，代码搜索与长上下文仍无法自动完成行为到代码的映射。本文提出 Harness Handbook：经静态分析与 LLM 辅助结构化从代码库自动合成的行为中心表示，将每个行为链接到对应源码；并提出 Behavior-Guided Progressive Disclosure（BGPD），引导 agent 从高层行为逐步披露到实现细节，并对照当前源码校验候选位点。在两个开源 harness 的多样修改请求上，Handbook 辅助规划提升行为定位与改动计划质量，减少 planner token，对分散位点、少执行路径与跨模块交互收益最大。结论：复杂 agentic 系统的演进不仅依赖生成编辑，更依赖判定编辑落点。

## Summary (English)

The capability of a modern AI agent depends not only on its foundation model but also on its harness, which constructs prompts, manages state, invokes tools, and coordinates execution. As models, APIs, environments, and requirements evolve, the harness must be continually modified. Before such a change can be made, a developer or coding agent must identify all code locations that implement the target behavior. This is difficult because production harnesses are large, tightly coupled, and behaviorally distributed, while modification requests describe what the system should do and repositories are organized by files and modules. Code search, repository indexing, and long-context processing ease inspection, but still leave this behavior-to-code mapping to be recovered by hand. Behavior localization is therefore a central bottleneck in harness evolution. We introduce the Harness Handbook, a behavior-centric representation synthesized automatically from a harness codebase via static analysis and LLM-assisted structuring, linking each behavior to its corresponding source. We also introduce Behavior-Guided Progressive Disclosure (BGPD), which guides agents from high-level behaviors to relevant implementation details and verifies candidate locations against the current source. On diverse modification requests from two open-source harnesses, Handbook-Assisted planning improves behavior localization and edit-plan quality while using fewer planner tokens, with the largest gains on scattered sites, rarely executed paths, and cross-module interactions. Evolving complex agentic systems thus depends not only on generating edits, but also on determining where those edits should be made.

## One-liner

Harness Handbook 用静态分析+LLM 自动合成行为中心地图，配合 BGPD 把 harness 演进从“会改”推进到“知道改哪里”。

## 原文 / 元数据抓取

# Harness Handbook: Making Evolving Agent Harnesses Readable,Navigable, and Editable
> 作者: Ruhan Wang, Yucheng Shi, Zongxia Li, Zhongzhi Li, Yue Yu, Junyao Yang, Kishan Panaganti, Haitao Mi, Dongruo Zhou, Leoweiliang
> 原文链接: https://arxiv.org/abs/2607.13285
> PDF: https://arxiv.org/pdf/2607.13285v1
> 发布时间: 2026-07-14
> 更新时间: 2026-07-14
> 分类: cs.AI, cs.SE

---

The capability of a modern AI agent depends not only on its foundation model but also on its harness, which constructs prompts, manages state, invokes tools, and coordinates execution. As models, APIs, environments, and requirements evolve, the harness must be continually modified. Before such a change can be made, a developer or coding agent must identify all code locations that implement the target behavior. This is difficult because production harnesses are large, tightly coupled, and behaviorally distributed, while modification requests describe what the system should do and repositories are organized by files and modules. Code search, repository indexing, and long-context processing ease inspection, but still leave this behavior-to-code mapping to be recovered by hand. Behavior localization is therefore a central bottleneck in harness evolution. We introduce the Harness Handbook, a behavior-centric representation synthesized automatically from a harness codebase via static analysis and LLM-assisted structuring, linking each behavior to its corresponding source. We also introduce Behavior-Guided Progressive Disclosure (BGPD), which guides agents from high-level behaviors to relevant implementation details and verifies candidate locations against the current source. On diverse modification requests from two open-source harnesses, Handbook-Assisted planning improves behavior localization and edit-plan quality while using fewer planner tokens, with the largest gains on scattered sites, rarely executed paths, and cross-module interactions. Evolving complex agentic systems thus depends not only on generating edits, but also on determining where those edits should be made.

## Obsidian intake evidence excerpt

该内容文件由 AAIF content-fetcher 根据 active/high-score entry 与 OpenCLI arXiv 元数据补齐。

- entry_id: 2dea0b4e
- title: Harness Handbook: Making Evolving Agent Harnesses Readable,Navigable, and Editable
- source: https://arxiv.org/abs/2607.13285
- existing_summary_zh: 主张 agent 能力强依赖可演进 harness，而修改瓶颈在行为代码位置映射；提出由静态分析与 LLM 结构归纳自动合成的行为中心 Harness Handbook，并以 BGPD 引导从高层行为逐步披露到实现并校验位点在两个开源 harness 的多样修改请求上，辅助规划提升行为定位与改动计划质量减少 planner token，对分散位点与跨模块交互收益最大收录理由：把 harness 工程从会改推进到知道改哪里，补齐 agent 系统演进的关键缺口
