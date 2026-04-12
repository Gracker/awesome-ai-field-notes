## English

## How to set up OpenClaw Agents that actually get better Over Time

To set up OpenClaw Agents that improve over time, as highlighted by Shubham Saboo and various OpenClaw resources, the key lies in establishing robust memory management, feedback mechanisms, and a structured agent architecture. The core idea is that while the underlying language model might remain the same, the agent's *context* and *knowledge* evolve through continuous interaction and structured feedback.

### 1. Foundational Setup and Architecture

**Install OpenClaw:** Begin by installing the OpenClaw framework.

**Modular File Separation:** Avoid cramming everything into a single configuration file. Instead, use separate Markdown files for different aspects of your agent. This improves manageability, reduces token usage by loading only relevant context, and simplifies debugging.

- `SOUL.md`: Defines the agent's full personality, identity, role, and operating principles. This is a crucial file.
- `IDENTITY.md`: A concise business card for the agent, including its name, role, and vibe.
- `USER.md`: Contains user-specific preferences, background, and context that shapes the agent's behavior. Every agent should read this.
- `AGENTS.md`: Defines the agent's architecture, roles, and session startup routine, including memory management rules.
- `MEMORY.md`: Tracks ongoing state and accumulates knowledge. This is where distilled, permanent learning entries reside.

**Start Simple:** Begin with one agent and one repetitive daily task. Get this working reliably before adding complexity.

**Cron Jobs:** Set up cron jobs to automate tasks, allowing agents to perform work independently and continuously.

### 2. Implementing Continuous Improvement (Learning Over Time)

**Feedback Mechanisms:**
- **Specific Feedback:** Provide direct and specific feedback to the agent. Crucially, ensure this feedback is saved into a *memory file* rather than just the chat.
- **Next-State Signals:** OpenClaw-RL leverages "next-state signals" from every agent interaction as implicit evaluations and training data.

**Memory Management:**
- **Daily Logs:** Daily logs serve as raw material. Review these logs regularly to identify recurring corrections and distill them into permanent entries in `MEMORY.md`.
- **Iterative Refinement:** Expect initial outputs to be mediocre. Continuous feedback and refinement of `SOUL.md` and memory files will lead to improved performance.

Shubham Saboo, a Google project manager, is a prominent advocate and practitioner of building autonomous AI agents with OpenClaw.


## 中文

## 如何设置真正能随时间变好的 OpenClaw Agents

正如 Shubham Saboo 和各种 OpenClaw 资源所强调的，关键在于建立强大的内存管理、反馈机制和结构化的代理架构。核心思想是，虽然底层语言模型可能保持不变，但代理的*上下文*和*知识*通过持续的交互和结构化的反馈而不断演变。

### 1. 基础设置和架构

**安装 OpenClaw：** 首先安装 OpenClaw 框架。

**模块化文件分离：** 避免将所有内容塞入单个配置文件。相反，为代理的不同方面使用单独的 Markdown 文件。这提高了可管理性，通过仅加载相关上下文来减少令牌使用，并简化调试。

- `SOUL.md`：定义代理的完整个性、身份、角色和操作原则。这是关键文件。
- `IDENTITY.md`：代理的简洁名片，包括其名称、角色和风格。
- `USER.md`：包含用户特定的偏好、背景和塑造代理行为的上下文。每个代理都应该读取这个文件。
- `AGENTS.md`：定义代理的架构、角色和会话启动例程，包括内存管理规则。
- `MEMORY.md`：跟踪正在进行的状态并累积知识。这是提炼的永久性学习条目所在的位置。

**从简单开始：** 从一个代理和一个重复的日常任务开始。在添加复杂性之前，使其可靠地工作。

**Cron 作业：** 设置 cron 作业来自动化任务，允许代理独立和持续地执行工作。

### 2. 实现持续改进（随时间学习）

**反馈机制：**
- **具体反馈：** 向代理提供直接和具体的反馈。关键是确保将此反馈保存到*内存文件*中，而不仅仅是聊天。
- **下一状态信号：** OpenClaw-RL 利用来自每个代理交互的下一状态信号作为隐式评估和训练数据。

**内存管理：**
- **日常日志：** 日常日志作为原材料。定期检查这些日志以识别重复的校正，并将它们提炼到 `MEMORY.md` 中的永久条目。
- **迭代改进：** 期望初始输出平庸。对 `SOUL.md` 和内存文件的持续反馈和改进将导致性能改善。

Shubham Saboo，Google 的项目经理，是使用 OpenClaw 构建自主 AI 代理的主要倡导者和实践者。