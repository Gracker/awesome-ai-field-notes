---
title: 'Context Engineering for AI Agents: Lessons from Building Manus'
sidebar: false
---

::: info
[← 返回AI编程](/coding)
:::

# Context Engineering for AI Agents: Lessons from Building Manus

> 从 Manus 构建经验总结的 Agent 上下文工程方法论

🔗 [原文链接](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus?s=09) | 🌐 | ⭐⭐⭐⭐ 4 ⭐4 4/5 📅 2026-04-10

`agent` `[]` `llm` `prompt`

---

## English
# Context Engineering for AI Agents: Lessons from Building Manus

2025/7/18 --Yichao 'Peak' Ji

At the very beginning of the Manus project, my team and I faced a key decision: should we train an end-to-end agentic model using open-source foundations, or build an agent on top of the in-context learning abilities of frontier models?

Back in my first decade in NLP, we didn't have the luxury of that choice. In the distant days of BERT (yes, it's been seven years), models had to be fine-tuned—and evaluated—before they could transfer to a new task. That process often took weeks per iteration, even though the models were tiny compared to today's LLMs. For fast-moving applications, especially pre–PMF, such slow feedback loops are a deal-breaker. That was a bitter lesson from my last startup, where I trained models from scratch for open information extraction and semantic search. Then came GPT-3 and Flan-T5, and my in-house models became irrelevant overnight. Ironically, those same models marked the beginning of in-context learning—and a whole new path forward.

That hard-earned lesson made the choice clear: Manus would bet on context engineering. This allows us to ship improvements in hours instead of weeks, and kept our product orthogonal to the underlying models: If model progress is the rising tide, we want Manus to be the boat, not the pillar stuck to the seabed.

Still, context engineering turned out to be anything but straightforward. It's an experimental science—and we've rebuilt our agent framework four times, each time after discovering a better way to shape context. We affectionately refer to this manual process of architecture searching, prompt fiddling, and empirical guesswork as "Stochastic Graduate Descent". It's not elegant, but it works.

This post shares the local optima we arrived at through our own "SGD". If you're building your own AI agent, I hope these principles help you converge faster.

### Design Around the KV-Cache

## 中文
# AI 代理的上下文工程：构建 Manus 的经验教训

2025/7/18 --纪一超‘巅峰’

在 Manus 项目之初，我和我的团队面临一个关键决定：我们应该使用开源基础训练端到端代理模型，还是在前沿模型的上下文学习能力之上构建代理？

回到我进入 NLP 的第一个十年，我们并没有这样的奢侈选择。在 BERT 的遥远岁月（是的，已经过去了七年），模型必须经过微调和评估才能转移到新任务。尽管与当今的法学硕士相比，该模型很小，但该过程每次迭代通常需要数周时间。对于快速移动的应用程序，尤其是 PMF 之前的应用程序，如此缓慢的反馈循环会破坏交易。这是我上一次创业的惨痛教训，当时我从头开始训练模型以进行开放信息提取和语义搜索。然后出现了 GPT-3 和 Flan-T5，我的内部模型一夜之间变得无关紧要。讽刺的是，这些相同的模型标志着情境学习的开始——以及一条全新的前进道路。

这个来之不易的教训让他做出了明确的选择：马努斯将把赌注押在上下文工程上。这使我们能够在数小时而不是数周内完成改进，并使我们的产品与底层模型保持正交：如果模型进展是不断上涨的潮流，我们希望 Manus 成为船，而不是粘在海底的柱子。

尽管如此，上下文工程却被证明并不是一件简单的事。这是一门实验科学，我们已经重建了代理框架四次，每次都是在发现了更好的方式来塑造环境之后。我们亲切地将这种架构搜索、快速摆弄和经验猜测的手动过程称为“随机研究生下降”。它并不优雅，但很有效。

这篇文章分享了我们通过自己的“SGD”得出的局部最优值。如果您正在构建自己的人工智能代理，我希望这些原则可以帮助您更快地收敛。

### 围绕 KV 缓存进行设计

## English
If I had to choose just one metric, I'd argue that the KV-cache hit rate is the single most important metric for a production-stage AI agent. It directly affects both latency and cost. To understand why, let's look at how a typical agent operates:

After receiving a user input, the agent proceeds through a chain of tool uses to complete the task. In each iteration, the model selects an action from a predefined action space based on the current context. That action is then executed in the environment (e.g., Manus's virtual machine sandbox) to produce an observation. The action and observation are appended to the context, forming the input for the next iteration. This loop continues until the task is complete.

As you can imagine, the context grows with every step, while the output—usually a structured function call—remains relatively short. This makes the ratio between prefilling and decoding highly skewed in agents compared to chatbots. In Manus, for example, the average input-to-output token ratio is around 100:1.

Fortunately, contexts with identical prefixes can take advantage of KV-cache, which drastically reduces time-to-first-token (TTFT) and inference cost—whether you're using a self-hosted model or calling an inference API. And we're not talking about small savings: with Claude Sonnet, for instance, cached input tokens cost 0.30 USD/MTok, while uncached ones cost 3 USD/MTok—a 10x difference.

From a context engineering perspective, improving KV-cache hit rate involves a few key practices:

1.Keep your prompt prefix stable. Due to the autoregressive nature of LLMs, even a single-token difference can invalidate the cache from that token onward. A common mistake is including a timestamp—especially one precise to the second—at the beginning of the system prompt. Sure, it lets the model tell you the current time, but it also kills your cache hit rate.

2.Make your context append-only. Avoid modifying previous actions or observations. Ensure your serialization is deterministic. Many programming languages and libraries don't guarantee stable key ordering when serializing JSON objects, which can silently break the cache.

3.Mark cache breakpoints explicitly when needed. Some model providers or inference frameworks don't support automatic incremental prefix caching, and instead require manual insertion of cache breakpoints in the context. When assigning these, account for potential cache expiration and at minimum, ensure the breakpoint includes the end of the system prompt.

## 中文
如果我必须只选择一个指标，我认为 KV 缓存命中率是生产阶段 AI 代理最重要的指标。它直接影响延迟和成本。要了解原因，让我们看看典型代理的运作方式：

收到用户输入后，代理将通过一系列工具使用来完成任务。在每次迭代中，模型根据当前上下文从预定义的操作空间中选择一个操作。然后在环境（例如 Manus 的虚拟机沙箱）中执行该操作以产生观察结果。操作和观察被附加到上下文中，形成下一次迭代的输入。这个循环一直持续到任务完成。

正如您可以想象的那样，上下文随着每一步而增长，而输出（通常是结构化函数调用）仍然相对较短。与聊天机器人相比，这使得代理中的预填充和解码之间的比率高度倾斜。例如，在 Manus 中，平均输入与输出令牌比率约为 100:1。

幸运的是，具有相同前缀的上下文可以利用 KV 缓存，这大大减少了首次令牌时间 (TTFT) 和推理成本 - 无论您是使用自托管模型还是调用推理 API。我们谈论的并不是小额节省：例如，对于 Claude Sonnet，缓存的输入令牌成本为 0.30 美元/MTok，而未缓存的输入令牌成本为 3 美元/MTok，相差 10 倍。

从上下文工程的角度来看，提高KV缓存命中率涉及几个关键实践：

1.保持提示符前缀稳定。由于 LLM 的自回归性质，即使是单个令牌差异也可能使该令牌之后的缓存失效。一个常见的错误是在系统提示符的开头包含时间戳（尤其是精确到秒的时间戳）。当然，它可以让模型告诉您当前时间，但它也会降低您的缓存命中率。

2.使您的上下文仅附加。避免修改以前的行动或观察。确保您的序列化是确定性的。许多编程语言和库在序列化 JSON 对象时不保证稳定的键顺序，这可能会悄悄破坏缓存。

3.在需要时显式标记缓存断点。某些模型提供程序或推理框架不支持自动增量前缀缓存，而是需要在上下文中手动插入缓存断点。分配这些时，请考虑潜在的缓存过期，并至少确保断点包括系统提示的结尾。

## English
Additionally, if you're self-hosting models using frameworks like vLLM, make sure prefix/prompt caching is enabled, and that you're using techniques like session IDs to route requests consistently across distributed workers.

### Mask, Don't Remove

As your agent takes on more capabilities, its action space naturally grows more complex—in plain terms, the number of tools explodes. The recent popularity of MCP only adds fuel to the fire. If you allow user-configurable tools, trust me: someone will inevitably plug hundreds of mysterious tools into your carefully curated action space. As a result, the model is more likely to select the wrong action or take an inefficient path. In short, your heavily armed agent gets dumber.

A natural reaction is to design a dynamic action space—perhaps loading tools on demand using something RAG-like. We tried that in Manus too. But our experiments suggest a clear rule: unless absolutely necessary, avoid dynamically adding or removing tools mid-iteration. There are two main reasons for this:

1.In most LLMs, tool definitions live near the front of the context after serialization, typically before or after the system prompt. So any change will invalidate the KV-cache for all subsequent actions and observations.

2.When previous actions and observations still refer to tools that are no longer defined in the current context, the model gets confused. Without constrained decoding, this often leads to schema violations or hallucinated actions.

To solve this while still improving action selection, Manus uses a context-aware state machine to manage tool availability. Rather than removing tools, it masks the token logits during decoding to prevent (or enforce) the selection of certain actions based on the current context.

In practice, most model providers and inference frameworks support some form of response prefill, which allows you to constrain the action space without modifying the tool definitions. There are generally three modes of function calling (we'll use the Hermes format from NousResearch as an example):

## 中文
此外，如果您使用 vLLM 等框架进行自托管模型，请确保启用前缀/提示缓存，并且您使用会话 ID 等技术在分布式工作人员之间一致地路由请求。

### 面膜，请勿摘除

随着您的代理拥有更多功能，其操作空间自然会变得更加复杂 - 简而言之，工具的数量会呈爆炸式增长。最近MCP的流行只会火上浇油。如果您允许用户配置工具，请相信我：有人将不可避免地将数百种神秘工具插入您精心策划的操作空间中。因此，模型更有可能选择错误的操作或采取低效的路径。简而言之，你的全副武装的特工会变得更加愚蠢。

自然的反应是设计一个动态的动作空间——也许使用类似 RAG 的东西按需加载工具。我们在马努斯也尝试过。但我们的实验提出了一个明确的规则：除非绝对必要，否则避免在迭代中动态添加或删除工具。造成这种情况的主要原因有两个：

1.在大多数LLM中，工具定义在序列化后位于上下文的前面附近，通常在系统提示符之前或之后。因此，任何更改都会使所有后续操作和观察的 KV 缓存失效。

2.当以前的操作和观察仍然引用当前上下文中不再定义的工具时，模型会变得混乱。如果没有受约束的解码，这通常会导致模式违规或幻觉行为。

为了解决这个问题，同时仍然改进操作选择，Manus 使用上下文感知状态机来管理工具可用性。它不是删除工具，而是在解码期间屏蔽令牌逻辑，以防止（或强制）基于当前上下文选择某些操作。

在实践中，大多数模型提供程序和推理框架都支持某种形式的响应预填充，这允许您在不修改工具定义的情况下约束操作空间。函数调用一般有以下三种模式（以NousResearch的Hermes格式为例）：

## English
•Auto – The model may choose to call a function or not. Implemented by prefilling only the reply prefix: assistant

•Required – The model must call a function, but the choice is unconstrained. Implemented by prefilling up to tool call token: assistant

•Specified – The model must call a function from a specific subset. Implemented by prefilling up to the beginning of the function name: assistant{"name": “browser_

Using this, we constrain action selection by masking token logits directly. For example, when the user provides a new input, Manus must reply immediately instead of taking an action. We've also deliberately designed action names with consistent prefixes—e.g., all browser-related tools start with browser_, and command-line tools with shell_. This allows us to easily enforce that the agent only chooses from a certain group of tools at a given state without using stateful logits processors.

These designs help ensure that the Manus agent loop remains stable—even under a model-driven architecture.

### Use the File System as Context

Modern frontier LLMs now offer context windows of 128K tokens or more. But in real-world agentic scenarios, that's often not enough, and sometimes even a liability. There are three common pain points:

1.Observations can be huge, especially when agents interact with unstructured data like web pages or PDFs. It's easy to blow past the context limit.

## 中文
•自动——模型可以选择是否调用函数。通过仅预填回复前缀来实现：assistant

•必需——模型必须调用函数，但选择不受限制。通过预填工具调用token来实现：assistant

• 指定——模型必须调用特定子集中的函数。通过预填充到函数名称开头来实现：assistant{"name": “browser_

使用此功能，我们通过直接屏蔽 token logits 来限制操作选择。例如，当用户提供新输入时，Manus 必须立即回复而不是采取操作。我们还特意设计了具有一致前缀的操作名称，例如，所有与浏览器相关的工具都以 browser_ 开头，命令行工具以 shell_ 开头。这使我们能够轻松强制代理仅在给定状态下从一组特定工具中进行选择，而不使用有状态 Logits 处理器。

这些设计有助于确保 Manus 代理循环保持稳定——即使在模型驱动的架构下也是如此。

### 使用文件系统作为上下文

现代前沿法学硕士现在提供 128K 令牌或更多的上下文窗口。但在现实世界的代理场景中，这通常是不够的，有时甚至是一种负担。常见的痛点有以下三个：

1.观察结果可能很大，尤其是当代理与网页或 PDF 等非结构化数据交互时。突破上下文限制很容易。

## English
2.Model performance tends to degrade beyond a certain context length, even if the window technically supports it.

3.Long inputs are expensive, even with prefix caching. You're still paying to transmit and prefill every token.

To deal with this, many agent systems implement context truncation or compression strategies. But overly aggressive compression inevitably leads to information loss. The problem is fundamental: an agent, by nature, must predict the next action based on all prior state—and you can't reliably predict which observation might become critical ten steps later. From a logical standpoint, any irreversible compression carries risk.

That's why we treat the file system as the ultimate context in Manus: unlimited in size, persistent by nature, and directly operable by the agent itself. The model learns to write to and read from files on demand—using the file system not just as storage, but as structured, externalized memory.

Our compression strategies are always designed to be restorable. For instance, the content of a web page can be dropped from the context as long as the URL is preserved, and a document's contents can be omitted if its path remains available in the sandbox. This allows Manus to shrink context length without permanently losing information.

While developing this feature, I found myself imagining what it would take for a State Space Model (SSM) to work effectively in an agentic setting. Unlike Transformers, SSMs lack full attention and struggle with long-range backward dependencies. But if they could master file-based memory—externalizing long-term state instead of holding it in context—then their speed and efficiency might unlock a new class of agents. Agentic SSMs could be the real successors to Neural Turing Machines.

### Manipulate Attention Through Recitation

If you've worked with Manus, you've probably noticed something curious: when handling complex tasks, it tends to create a todo.md file—and update it step-by-step as the task progresses, checking off completed items.

## 中文
2.即使窗口在技术上支持它，模型性能在超过一定的上下文长度后往往会下降。

3.即使使用前缀缓存，长输入也很昂贵。您仍然需要支付传输和预填充每个令牌的费用。

为了解决这个问题，许多代理系统实施上下文截断或压缩策略。但过于激进的压缩不可避免地会导致信息丢失。问题是根本性的：智能体本质上必须根据所有先前状态来预测下一步行动，而您无法可靠地预测十步后哪些观察可能会变得至关重要。从逻辑的角度来看，任何不可逆的压缩都会带来风险。

这就是为什么我们将文件系统视为 Manus 中的最终上下文：大小不受限制，本质上是持久的，并且可以由代理本身直接操作。该模型学习按需写入和读取文件——文件系统不仅用作存储，还用作结构化的外部化内存。

我们的压缩策略始终设计为可恢复的。例如，只要保留 URL，就可以从上下文中删除网页的内容；如果文档的路径在沙箱中仍然可用，则可以省略文档的内容。这使得 Manus 能够缩短上下文长度，而不会永久丢失信息。

在开发此功能时，我发现自己在想象状态空间模型 (SSM) 在代理环境中如何有效工作。与 Transformers 不同，SSM 缺乏充分的关注，并且与远程向后依赖作斗争。但如果他们能够掌握基于文件的记忆——将长期状态外化，而不是将其保存在上下文中——那么他们的速度和效率可能会解锁一类新的智能体。 Agentic SSM 可能是神经图灵机的真正继承者。

### 通过背诵控制注意力

如果您使用过 Manus，您可能会注意到一些奇怪的事情：在处理复杂任务时，它往往会创建一个 todo.md 文件，并随着任务的进展逐步更新它，检查已完成的项目。

## English
That's not just cute behavior—it's a deliberate mechanism to manipulate attention.

A typical task in Manus requires around 50 tool calls on average. That's a long loop—and since Manus relies on LLMs for decision-making, it's vulnerable to drifting off-topic or forgetting earlier goals, especially in long contexts or complicated tasks.

By constantly rewriting the todo list, Manus is reciting its objectives into the end of the context. This pushes the global plan into the model's recent attention span, avoiding "lost-in-the-middle" issues and reducing goal misalignment. In effect, it's using natural language to bias its own focus toward the task objective—without needing special architectural changes.

### Keep the Wrong Stuff In

Agents make mistakes. That's not a bug—it's reality. Language models hallucinate, environments return errors, external tools misbehave, and unexpected edge cases show up all the time. In multi-step tasks, failure is not the exception; it's part of the loop.

And yet, a common impulse is to hide these errors: clean up the trace, retry the action, or reset the model's state and leave it to the magical "temperature". That feels safer, more controlled. But it comes at a cost: Erasing failure removes evidence. And without evidence, the model can't adapt.

In our experience, one of the most effective ways to improve agent behavior is deceptively simple: leave the wrong turns in the context. When 

[...]
