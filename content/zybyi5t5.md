# Context Engineering for AI Agents: Lessons from Building Manus

## English

Context Engineering for AI Agents: Lessons from Building Manus

This post shares the local optima Manus arrived at through our own "SGD". If you're building your own AI agent, we hope these principles help you converge faster.

The core idea behind context engineering is to design a system that delivers the right information and tools, in the appropriate format, for an LLM to successfully complete a task.

### The File System as Ultimate Context

Manus treats the file system as an unlimited, persistent context that the agent can directly operate on, mitigating issues of information loss that can arise from aggressive context compression or truncation.

### Avoiding "Lost-in-the-Middle" Issues

To combat LLMs drifting off-topic or forgetting goals in long contexts, Manus constantly rewrites its "todo list" into the end of the context. This keeps the global plan within the model's recent attention span, helping to maintain focus without requiring architectural changes.

### Stable Prompt Prefixes and Append-Only Context

Maintaining a consistent prompt prefix and an append-only context are highlighted as fundamental practices in context engineering for AI agents.

### Constrained Action Selection

Manus employs a context-aware state machine to manage tool availability, masking token logits during decoding to prevent or enforce the selection of specific actions based on the current context, thereby reducing schema violations and hallucinated actions.

### Leveraging KV-Cache

Contexts with identical prefixes can utilize KV-cache to significantly reduce time-to-first-token (TTFT) and inference costs, especially in agent systems where the input-to-output token ratio can be highly skewed.

### Challenges with Few-Shot Prompting

In agent systems, few-shot prompting can sometimes lead to models mimicking past behaviors even when they are no longer optimal, particularly in tasks involving repetitive decisions.

### Hierarchical Action Space

To address context confusion and hallucinated parameters with a large number of tools, Manus utilizes a hierarchical action space. This involves providing the model with a small set of core tools (Level 1) and using these tools (like `bash`) to access more specialized utilities (Level 2), keeping tool definitions out of the primary context window.

## 中文

Context Engineering for AI Agents: Lessons from Building Manus

本文分享了Manus通过自身"SGD"（随机梯度下降）所达到的局部最优经验。如果您正在构建自己的AI代理，我们希望这些原则能帮助您更快地收敛。

上下文工程的核心思想是设计一个系统，以适当的格式提供正确信息和工具，使LLM能够成功完成任务。

### 文件系统作为终极上下文

Manus将文件系统视为无限的持久上下文，代理可以直接操作它，从而减轻了激进上下文压缩或截断可能导致的信息丢失问题。

### 避免"迷失中间"问题

为了对抗LLM在长上下文中偏离主题或忘记目标，Manus不断将"待办事项列表"重写到上下文末尾。这使全局计划保持在模型的近期注意力范围内，帮助保持专注，而不需要架构更改。

### 稳定的提示前缀和仅附加上下文

保持一致的提示前缀和仅附加上下文被认为是AI代理上下文工程的基本实践。

### 受限的动作选择

Manus采用上下文感知状态机来管理工具可用性，在解码期间屏蔽token logits，以根据当前上下文阻止或强制执行特定动作的选择，从而减少模式违规和幻觉动作。

### 利用KV-Cache

具有相同前缀的上下文可以利用KV-cache显著减少首次令牌时间（TTFT）和推理成本，特别是在输入输出令牌比率可能高度倾斜的代理系统中。

### 少样本提示的挑战

在代理系统中，少样本提示有时会导致模型模仿过去的行为，即使这些行为不再是最佳的，特别是在涉及重复决策的任务中。

### 层次化动作空间

为了处理大量工具导致的上下文混乱和幻觉参数，Manus利用层次化动作空间。这涉及为模型提供一小组核心工具（Level 1），并使用这些工具（如`bash`）访问更专业的实用工具（Level 2），将工具定义保持在主上下文窗口之外。