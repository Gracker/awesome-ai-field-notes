# Agent Skills for Context Engineering

A comprehensive, open collection of Agent Skills focused on context engineering principles for building production-grade AI agent systems. These skills teach the art and science of curating context to maximize agent effectiveness across any agent platform.

## 核心概念

Context engineering is the discipline of managing the language model's context window. Unlike prompt engineering, which focuses on crafting effective instructions, context engineering addresses the holistic curation of all information that enters the model's limited attention budget: system prompts, tool definitions, retrieved documents, message history, and tool outputs.

The fundamental challenge is that context windows are constrained not by raw token capacity but by attention mechanics. As context length increases, models exhibit predictable degradation patterns: the "lost-in-the-middle" phenomenon, U-shaped attention curves, and attention scarcity. Effective context engineering means finding the smallest possible set of high-signal tokens that maximize the likelihood of desired outcomes.

## 技能体系

### 基础技能（Foundational Skills）

| 技能 | 描述 |
|------|------|
| context-fundamentals | Understand what context is, why it matters, and the anatomy of context in agent systems |
| context-degradation | Recognize patterns of context failure: lost-in-middle, poisoning, distraction, and clash |
| context-compression | Design and evaluate compression strategies for long-running sessions |

### 架构技能（Architecture Skills）

| 技能 | 描述 |
|------|------|
| multi-agent-patterns | Master orchestrator, peer-to-peer, and hierarchical multi-agent architectures |
| memory-systems | Design short-term, long-term, and graph-based memory architectures |
| tool-design | Build tools that agents can use effectively |
| filesystem-context | Use filesystems for dynamic context discovery, tool output offloading, and plan persistence |
| hosted-agents | Build background coding agents with sandboxed VMs, pre-built images, multiplayer support, and multi-client interfaces |

### 优化技能（Optimization Skills）

| 技能 | 描述 |
|------|------|
| context-optimization | Apply compaction, masking, and caching strategies |
| latent-briefing | Share task-relevant orchestrator state with workers via task-guided KV cache compaction |
| evaluation | Build evaluation frameworks for agent systems |
| advanced-evaluation | Master LLM-as-a-Judge techniques: direct scoring, pairwise comparison, rubric generation, and bias mitigation |

### 项目技能（Project Skills）

| 技能 | 描述 |
|------|------|
| project-development | Design and build LLM projects from ideation through deployment |

### 认知技能（Cognitive Skills）

| 技能 | 描述 |
|------|------|
| bdi-mental-states | Transform external RDF context into agent mental states (beliefs, desires, intentions) using formal BDI ontology patterns |

## 技能触发词（Skill Triggers）

| 技能 | 触发词 |
|------|------|
| context-fundamentals | "understand context", "explain context windows", "design agent architecture" |
| context-degradation | "diagnose context problems", "fix lost-in-middle", "debug agent failures" |
| context-compression | "compress context", "summarize conversation", "reduce token usage" |
| context-optimization | "optimize context", "reduce token costs", "implement KV-cache" |
| latent-briefing | "KV cache compaction between agents", "worker KV memory handoff", "latent briefing" |
| multi-agent-patterns | "design multi-agent system", "implement supervisor pattern" |
| memory-systems | "implement agent memory", "build knowledge graph", "track entities" |
| tool-design | "design agent tools", "reduce tool complexity", "implement MCP tools" |
| filesystem-context | "offload context to files", "dynamic context discovery", "agent scratch pad" |
| hosted-agents | "build background agent", "create hosted coding agent", "sandboxed execution" |
| evaluation | "evaluate agent performance", "build test framework", "measure quality" |
| advanced-evaluation | "implement LLM-as-judge", "compare model outputs", "mitigate bias" |
| project-development | "start LLM project", "design batch pipeline", "evaluate task-model fit" |
| bdi-mental-states | "model agent mental states", "implement BDI architecture", "transform RDF to beliefs" |

## 示例系统

### digital-brain-skill
Personal operating system for founders and creators. Complete Claude Code skill with 6 modules, 4 automation scripts.
使用的技能：context-fundamentals, context-optimization, memory-systems, tool-design, multi-agent-patterns, evaluation, project-development

### x-to-book-system
Multi-agent system that monitors X accounts and generates daily synthesized books.
使用的技能：multi-agent-patterns, memory-systems, context-optimization, tool-design, evaluation

### llm-as-judge-skills
Production-ready LLM evaluation tools with TypeScript implementation, 19 passing tests.
使用的技能：advanced-evaluation, tool-design, context-fundamentals, evaluation

### book-sft-pipeline
Train models to write in any author's style. Includes Gertrude Stein case study with 70% human score on Pangram, $2 total cost.
使用的技能：project-development, context-compression, multi-agent-patterns, evaluation

## 核心原则

Each skill is structured for efficient context use. At startup, agents load only skill names and descriptions. Full content loads only when a skill is activated for relevant tasks. These skills focus on transferable principles rather than vendor-specific implementations. The patterns work across Claude Code, Cursor, and any agent platform that supports skills or allows custom instructions.

## 关键特点

- **渐进式披露**（Progressive Disclosure）：3级加载（SKILL.md → MODULE.md → data files）
- **模块隔离**（Module Isolation）：6个独立模块（identity, content, knowledge, network, operations, agents）
- **只追加内存**（Append-Only Memory）：JSONL files with schema-first lines for agent-friendly parsing
- **自动化脚本**（Automation Scripts）：4个整合工具（weekly_review, content_ideas, stale_contacts, idea_to_draft）

---

来源：[muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering)
