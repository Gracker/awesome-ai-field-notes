---
title: 'Agent-Skills-for-Context-Engineering：面向上下文工程的开放技能库'
sidebar: false
---

::: info
[← 返回学习资源](/learning)
:::

# Agent-Skills-for-Context-Engineering：面向上下文工程的开放技能库

> 上下文工程的开放技能库，按需加载、平台无关

🔗 [原文链接](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | @泊舟 |  | ⭐⭐⭐⭐ 4 ⭐4 4/5 📅 2026-04-10

`context-engineering` `skills` `agent` `claude-code` `cursor` `lost-in-the-middle`

---

A comprehensive, open collection of Agent Skills focused on context engineering principles for building production-grade AI agent systems. These skills teach the art and science of curating context to maximize agent effectiveness across any agent platform.

[DeepWiki: Learn more here](https://deepwiki.com/muratcankoylan/Agent-Skills-for-Context-Engineering)

Context engineering is the discipline of managing the language model's context window. Unlike prompt engineering, which focuses on crafting effective instructions, context engineering addresses the holistic curation of all information that enters the model's limited attention budget: system prompts, tool definitions, retrieved documents, message history, and tool outputs.

The fundamental challenge is that context windows are constrained not by raw token capacity but by attention mechanics. As context length increases, models exhibit predictable degradation patterns: the "lost-in-the-middle" phenomenon, U-shaped attention curves, and attention scarcity. Effective context engineering means finding the smallest possible set of high-signal tokens that maximize the likelihood of desired outcomes.

This repository is cited in academic research as foundational work on static skill architecture:

"While static skills are well-recognized [Anthropic, 2025b; Muratcan Koylan, 2025], MCE is among the first to dynamically evolve them, bridging manual skill engineering and autonomous self-improvement."

— [Meta Context Engineering via Agentic Skill Evolution](https://arxiv.org/pdf/2601.21557), Peking University State Key Laboratory of General Artificial Intelligence (2026)

These skills establish the foundational understanding required for all subsequent context engineering work.

Skill
Description

[context-fundamentals](/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/main/skills/context-fundamentals)
Understand what context is, why it matters, and the anatomy of context in agent systems

[context-degradation](/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/main/skills/context-degradation)
Recognize patterns of context failure: lost-in-middle, poisoning, distraction, and clash

[context-compression](/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/main/skills/context-compression)
Design and evaluate compression strategies for long-running sessions

These skills cover the patterns and structures for building effective agent systems.

Skill
Description

[multi-agent-patterns](/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/main/skills/multi-agent-patterns)
Master orchestrator, peer-to-peer, and hierarchical multi-agent architectures

[memory-systems](/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/main/skills/memory-systems)
Design short-term, long-term, and graph-based memory architectures

[tool-design](/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/main/skills/tool-design)
Build tools that agents can use effectively

[filesystem-context](/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/main/skills/filesystem-context)
Use filesystems for dynamic context discovery, tool output offloading, and plan persistence

[hosted-agents](/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/main/skills/hosted-agents)
NEW Build background coding agents with sandboxed VMs, pre-built images, multiplayer support, and multi-client interfaces

These skills address the ongoing operation and optimization of agent systems.

Skill
Description

[context-optimization](/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/main/skills/context-optimization)
Apply compaction, masking, and caching strategies

[evaluation](/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/main/skills/evaluation)
Build evaluation frameworks for agent systems

[advanced-evaluation](/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/main/skills/advanced-evaluation)
Master LLM-as-a-Judge techniques: direct scoring, pairwise comparison, rubric generation, and bias mitigation

These skills cover the meta-level practices for building LLM-powered projects.

Skill
Description

[project-development](/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/main/skills/project-development)
Design and build LLM projects from ideation through deployment, including task-model fit analysis, pipeline architecture, and structured output design

These skills cover formal cognitive modeling for rational agent systems.

Skill
Description

[bdi-mental-states](/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/main/skills/bdi-mental-states)
NEW Transform external RDF context into agent mental states (beliefs, desires, intentions) using formal BDI ontology patterns for deliberative reasoning and explainability

Each skill is structured for efficient context use. At startup, agents load only skill names and descriptions. Full content loads only when a skill is activated for relevant tasks.

These skills focus on transferable principles rather than vendor-specific implementations. The patterns work across Claude Code, Cursor, and any agent platform that supports skills or allows custom instructions.

Scripts and examples demonstrate concepts using Python pseudocode that works across environments without requiring specific dependency installations.

This repository is a Claude Code Plugin Marketplace containing context engineering skills that Claude automatically discovers and activates based on your task context.

Step 1: Add the Marketplace

Run this command in Claude Code to register this repository as a plugin source:

/plugin marketplace add muratcankoylan/Agent-Skills-for-Context-Engineering

Step 2: Install the Plugin

Option A - Browse and install:

- Select Browse and install plugins

- Select context-engineering-marketplace

- Select context-engineering

- Select Install now

Option B - Direct install via command:

/plugin install context-engineering@context-engineering-marketplace

This installs all 13 skills in a single plugin. Skills are activated automatically based on your task context.

Skill
Triggers On

context-fundamentals
"understand context", "explain context windows", "design agent architecture"

context-degradation
"diagnose context problems", "fix lost-in-middle", "debug agent failures"

context-compression
"compress context", "summarize conversation", "reduce token usage"

context-optimization
"optimize context", "reduce token costs", "implement KV-cache"

multi-agent-patterns
"design multi-agent system", "implement supervisor pattern"

memory-systems
"implement agent memory", "build knowledge graph", "track entities"

tool-design
"design agent tools", "reduce tool complexity", "implement MCP tools"

filesystem-context
"offload context to files", "dynamic context discovery", "agent scratch pad", "file-based context"

hosted-agents
"build background agent", "create hosted coding agent", "sandboxed execution", "multiplayer agent", "Modal sandboxes"

evaluation
"evaluate agent performance", "build test framework", "measure quality"

advanced-evaluation
"implement LLM-as-judge", "compare model outputs", "mitigate bias"

project-development
"start LLM project", "design batch pipeline", "evaluate task-model fit"

bdi-mental-states
"model agent mental states", "implement BDI architecture", "transform RDF to beliefs", "build cognitive agent"

This repository is listed on the [Cursor Plugin Directory](https://cursor.directory/plugins/context-engineering).

The .plugin/plugin.json manifest follows the [Open Plugins](https://open-plugins.com) standard, so the repo also works with any conformant agent tool (Codex, GitHub Copilot, etc.).

To use a single skill without installing the full plugin, copy its SKILL.md directly into your project's .claude/skills/ directory:

# Example: add just the context-fundamentals skill
mkdir -p .claude/skills
curl -o .claude/skills/context-fundamentals.md  https://raw.githubusercontent.com/muratcankoylan/Agent-Skills-for-Context-Engineering/main/skills/context-fundamentals/SKILL.md

Available skills: context-fundamentals, context-degradation, context-compression, context-optimization, multi-agent-patterns, memory-systems, tool-design, filesystem-context, hosted-agents, evaluation, advanced-evaluation, project-development, bdi-mental-states

Extract the principles and patterns from any skill and implement them in your agent framework. The skills are deliberately platform-agnostic.

The [examples](/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/main/examples) folder contains complete system designs that demonstrate how multiple skills work together in practice.

Example
Description
Skills Applied

[digital-brain-skill](/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/main/examples/digital-brain-skill)
NEW Personal operating system for founders and creators. Complete Claude Code skill with 6 modules, 4 automation scripts
context-fundamentals, context-optimization, memory-systems, tool-design, multi-agent-patterns, evaluation, project-development

[x-to-book-system](/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/main/examples/x-to-book-system)
Multi-agent system that monitors X accounts and generates daily synthesized books
multi-agent-patterns, memory-systems, context-optimization, tool-design, evaluation

[llm-as-judge-skills](/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/main/examples/llm-as-judge-skills)
Production-ready LLM evaluation tools with TypeScript implementation, 19 passing tests
advanced-evaluation, tool-design, context-fundamentals, evaluation

[book-sft-pipeline](/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/main/examples/book-sft-pipeline)
Train models to write in any author's style. Includes Gertrude Stein case study with 70% human score on Pangram,  total cost
project-development, context-compression, multi-agent-patterns, evaluation

Each example includes:

- Complete PRD with architecture decisions

- Skills mapping showing which concepts informed each decision

- Implementation guidance

The [digital-brain-skill](/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/main/examples/digital-brain-skill) example is a complete personal operating system demonstrating comprehensive skills application:

- Progressive Disclosure: 3-level loading (SKILL.md → MODULE.md → data files)

- Module Isolation: 6 independent modules (identity, content, knowledge, network, operations, agents)

- Append-Only Memory: JSONL files with schema-first lines for agent-friendly parsing

- Automation Scripts: 4 consolidated tools (weekly_review, content_ideas, stale_contacts, idea_to_draft)

Includes detailed traceability in [HOW-SKILLS-BUILT-THIS.md](/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/main/examples/digital-brain-skill/HOW-SKILLS-BUILT-THIS.md) mapping every architectural decision to specific skill principles.

The [llm-as-judge-skills](/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/main/examples/llm-as-judge-skills) example is a complete TypeScript implementation demonstrating:

- Direct Scoring: Evaluate responses against weighted criteria with rubric support

- Pairwise Comparison: Compare responses with position bias mitigation

- Rubric Generation: Create domain-specific evaluation standards

- EvaluatorAgent: High-level agent combining all evaluation capabilities

The [book-sft-pipeline](/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/main/examples/book-sft-pipeline) example demonstrates training small models (8B) to write in any author's style:

- Intelligent Segmentation: Two-tier chunking with overlap for maximum training examples

- Prompt Diversity: 15+ templates to prevent memorization and force style learning

- Tinker Integration: Complete LoRA training workflow with  total cost

- Validation Methodology: Modern scenario testing proves style transfer vs content memorization

Integrates with context engineering skills: project-development, context-compression, multi-agent-patterns, evaluation.

Each skill follows the Agent Skills specification:

skill-name/
├── SKILL.md # Required: instructions + metadata
├── scripts/ # Optional: executable code demonstrating concepts
└── references/ # Optional: additional documentation and resources

See the [template](/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/main/template) folder for the canonical skill structure.

This repository follows the Agent Skills open development model. Contributions are welcome from the broader ecosystem. When contributing:

- Follow the skill template structure

- Provide clear, actionable instructions

- Include working ex
