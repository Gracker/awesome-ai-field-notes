## English

# How we built our multi-agent research system

**Source:** Anthropic Engineering Blog
**URL:** https://www.anthropic.com/engineering/multi-agent-research-system
**Published:** Jun 13, 2025

## Architecture: Orchestrator-Worker Pattern

Lead agent plans research process, spawns subagents that explore different aspects in parallel. Subagents operate with their own context windows — enables compression of findings for the lead agent.

## Key Benefits

- **Multi-agent outperformed single-agent by 90.2%** on internal research eval (Opus 4 lead + Sonnet 4 subagents)
- **Token usage explains 80%** of variance in BrowseComp evaluation
- **Parallel tool calling cut research time by up to 90%**

## Prompt Engineering Lessons

1. **Think like your agents** — build simulations with exact prompts/tools, watch step-by-step
2. **Teach the orchestrator how to delegate** — objective, output format, tools/sources guidance, task boundaries
3. **Scale effort to query complexity** — simple: 1 agent + 3-10 calls; comparison: 2-4 agents + 10-15 calls; complex: 10+ agents with clear divisions
4. **Tool design is critical** — bad tool descriptions send agents down wrong paths; each tool needs distinct purpose and clear description
5. **Let agents improve themselves** — Claude 4 models can be excellent prompt engineers; testing agent improved MCP tool descriptions → 40% decrease in task completion time
6. **Start wide, then narrow** — agents default to overly specific queries; counter by prompting for short broad queries first, then progressively narrow
7. **Guide the thinking process** — extended thinking as controllable scratchpad for planning

## Why Multi-Agent Works

Three factors explain 95% of performance variance in browsing agent evaluations:
1. Token usage (80% of variance)
2. Number of tool calls
3. Model choice

Multi-agent architectures effectively scale token usage for tasks that exceed single agent limits. Latest Claude models act as large efficiency multipliers on token use.

## Tradeoffs

- Agents use ~4× more tokens than chats
- Multi-agent systems use ~15× more tokens than chats
- Not suited for tasks requiring shared context or many dependencies between agents
- Best for high-value tasks with heavy parallelization, information exceeding single context windows, and many complex tools


## 中文

# 我们如何构建多 Agent 研究系统

**来源：** Anthropic 工程博客
**链接：** https://www.anthropic.com/engineering/multi-agent-research-system
**发布日期：** 2025年6月13日

## 架构：编排器-工作者模式

主 agent 规划研究过程，生成在多个方向并行探索的子 agent。子 agent 拥有自己的上下文窗口 — 允许对发现进行压缩后汇报给主 agent。

## 主要优势

- **多 Agent 在内部研究评估中超出单 Agent 90.2%**（Opus 4 主 + Sonnet 4 子）
- **Token 使用解释了 BrowseComp 评估中 80% 的方差**
- **并行工具调用将研究时间缩短多达 90%**

## 提示工程经验

1. **像 agent 那样思考** — 用精确的提示/工具构建模拟，一步步观察
2. **教编排器如何委托** — 目标、输出格式、工具/来源指导、任务边界
3. **根据查询复杂度调整投入** — 简单：1 agent + 3-10 次调用；比较：2-4 agents + 10-15 次调用；复杂：10+ agents 且分工明确
4. **工具设计至关重要** — 糟糕的工具描述会让 agent 走错路；每个工具需要明确用途和清晰描述
5. **让 agent 自我改进** — Claude 4 模型可以成为出色的提示工程师；测试 agent 改进了 MCP 工具描述 → 任务完成时间减少 40%
6. **先宽后窄** — agent 默认使用过于具体的查询；通过提示先做简短宽泛查询，然后逐步收窄来对抗
7. **引导思维过程** — 扩展思考作为可控制的草稿纸用于规划

## 多 Agent 为何有效

浏览 agent 评估中 95% 的性能方差来自三个因素：
1. Token 使用（80% 的方差）
2. 工具调用次数
3. 模型选择

多 Agent 架构有效地为超出单个 agent 限制的任务扩展 token 使用。最新 Claude 模型在 token 使用上充当大型效率倍增器。

## 权衡

- Agent 比聊天多使用约 4 倍的 token
- 多 Agent 系统比聊天多使用约 15 倍的 token
- 不适用于需要共享上下文或 agent 之间有很多依赖的任务
- 最适合高价值任务：高度并行化、超过单个上下文窗口的信息量、众多复杂工具

