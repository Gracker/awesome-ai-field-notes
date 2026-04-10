# 提示技术

Techniques — 3 条活跃资源

### [像 Rust Arena Allocator 一样管理上下文](https://x.com/blackanger/status/2027345330505924638) 
by @blackanger (2026-02-28) | ⭐⭐⭐⭐⭐ 5/5 | 🇨🇳

**Agent 上下文管理 = Rust Arena Allocator：append-only、空间局部性、批量释放**

将 Agent 上下文管理类比 Rust Arena Allocator：预留大块连续内存→每次分配指针向前推→所有分配连续排列→整块一起释放。Agent 上下文窗口就是一块有限的、昂贵的内存空间。Prompt Engineering 的核心不是写好文字，而是内存管理。Arena 的核心特性（Append-only、空间局部性、批量释放）直接对应 Agent 上下文设计原则。Pruning 和 RAG 是技巧不是原则。
 `context-management` `rust` `arena-allocator` `agent-design` `prompt-engineering`

---
### [Agent-Skills-for-Context-Engineering：面向上下文工程的开放技能库](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) 
by @泊舟 (2026-02-24) | ⭐⭐⭐⭐ 4/5 | 🌍

**上下文工程的开放技能库，按需加载、平台无关**

面向"上下文工程"的开放技能库，管理模型看到的全部输入（系统提示、工具定义、检索文档、消息历史、工具输出）。核心原则：按需加载（启动只加载技能索引，命中任务才加载全文）、保留高信号信息压缩低价值 token。方法平台无关，可迁移到 Claude Code、Cursor 等框架。示例覆盖多 Agent 协作、LLM 评审体系、长期记忆系统。
 `context-engineering` `skills` `agent` `claude-code` `cursor` `lost-in-the-middle`

---
### [How to master prompt engineering](https://x.com/EXM7777/article/2011800604709175808) 
by @Machina (2026-02-26) | ⭐⭐⭐⭐ 4/5 | 🌐

**Prompt 工程的本质是精确的意图建模，不是文字技巧**

核心观点：prompt 工程不是写好的文字，而是精确知道自己想要什么。差距在于你脑中的模糊想法 vs 你能精确表达的程度。文章覆盖了从心理模型到输出精度的完整方法论，强调"看不见的工作"——在坐下来提示之前，先建立清晰的意图模型。
 `prompt-engineering` `mental-model` `precision` `structure`

---