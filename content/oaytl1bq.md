# 使用 ADK 与全新 Interactions API 构建 Agent

> 英文原文：https://developers.googleblog.com/en/building-agents-with-the-adk-and-the-new-interactions-api/
> 翻译：AI Field Notes 自动翻译

---

> **EN:** Building agents with the ADK and the new Interactions API

---

![The Agentic experience: Is MCP the right tool for your AI future?](images/img_001.png)

AI 开发领域正在经历一场范式转变——从无状态的请求-响应循环，转向有状态的、多轮交互的 Agent 工作流。随着 [**Interactions API**](https://blog.google/technology/developers/interactions-api) 的 Beta 版发布，Google 提供了一个专门为这一新时代设计的统一接口——一个同时通往原始模型和全托管的 [**Gemini Deep Research Agent**](https://blog.google/technology/developers/deep-research-agent-gemini-api) 的单一入口。

> **EN:** The landscape of AI development is shifting from stateless request-response cycles to stateful, multi-turn agentic workflows. With the beta launch of the Interactions API, Google is providing a unified interface designed specifically for this new era—offering a single gateway to both raw models and the fully managed Gemini Deep Research Agent.

对于已经在使用 **Agent 开发套件（ADK）** 和 **Agent2Agent（A2A）** 协议的开发者来说，这引出了一个令人兴奋的问题：_这个新 API 如何融入我现有的技术栈？_

> **EN:** For developers already working with the Agent Development Kit (ADK) and the Agent2Agent (A2A) protocol, this raises an exciting question: How does this new API fit into my existing ecosystem?

答案有两层含义。Interactions API 既可以作为现有 `generateContent` 推理 API 端点的替代方案，也是一种强大的基础组件，可以在你_现有_的 Agent 框架_内部_使用。

> **EN:** The answer is two-fold. The Interactions API acts as both an alternative to the existing `generateContent` inference API endpoint and as a powerful primitive you can use within an existing agent framework.

本文将探讨两种主要的集成模式：

> **EN:** In this post, we'll explore two primary patterns for integration:

1.  **为 ADK Agent 提供动力：** 使用 Interactions API 作为自定义 Agent 的推理引擎。
2.  **透明桥接：** 通过 Interactions API，以标准远程 A2A Agent 的方式与内置 Agent（如 Gemini Deep Research Agent）协作。

> **EN:** 1. Powering your ADK Agents: Using the Interactions API as the inference engine for your custom agents. 2. The Transparent Bridge: Collaborating with built-in agents (like Gemini Deep Research Agent) at standard remote A2A agents using the Interactions API.

![gfd-blog-banner-interactions-api-adk-a2a](images/img_002.jpg)

---

## 模式一：使用 ADK 与 Interactions API 编写 Agent

当你使用 [ADK（Agent 开发套件）](https://google.github.io/adk-docs/) 构建 Agent 时，需要一个像 Gemini 这样能生成思考、计划、工具调用和响应的 LLM。在此之前，这些工作由 `generateContent` 处理。

> **EN:** When you build an agent using the ADK (Agent Development Kit), you need a LLM like Gemini which generates the thoughts, plans, tool calls and responses. Previously, this was handled by `generateContent`.

全新的 Interactions API 为复杂状态管理提供了原生接口。将推理调用升级为使用这个新端点后，你的 ADK Agent 将获得专为 Agent 循环设计的能力。

> **EN:** The new Interactions API offers a native interface for complex state management. By upgrading your inference calls to use this new endpoint, your ADK agents gain access to capabilities designed specifically for agentic loops.

### 为什么要切换？

> **EN:** Why switch?

-   **统一模型与 Agent 访问：** 同一个 API 端点既可用于标准模型（model="gemini-3-pro-preview"），也可用于内置的 Gemini Agent（agent="deep-research-pro-preview-12-2025"）。
-   **简化状态管理：** 你可以选择使用 `previous_interaction_id` 将对话历史管理卸载到服务器端，从而减少 ADK Agent 中的样板代码。
-   **后台执行：** 该 API 通过后台执行模式支持长时间运行的任务（如 Deep Research Agent 执行的那些任务）。设置 `background=True` 后，API 会立即返回一个交互 ID，并将推理循环转移到服务器端。这允许客户端断开连接而不必担心超时，并异步轮询端点以获取最终输出。
-   **原生思考处理：** API 明确地将"思考"与最终响应分开建模，使你的 ADK Agent 能够更有效地处理推理链。

> **EN:**
> - **Unified Model & Agent Access:** The same API endpoint works for a standard model (model="gemini-3-pro-preview") or a built-in Gemini agent (agent="deep-research-pro-preview-12-2025").
> - **Simplified State Management:** You can optionally offload conversation history management to the server using `previous_interaction_id`, reducing the boilerplate code in your ADK agent.
> - **Background Execution:** The API supports long-running tasks (such as those performed by the Deep Research agent) via a background execution mode. By setting `background=True`, the API immediately returns an interaction ID and offloads the reasoning loop to the server. This allows the client to disconnect without hitting timeouts and asynchronously poll the endpoint to retrieve the final output.
> - **Native Thought Handling:** The API explicitly models "thoughts" separate from final responses, allowing your ADK agent to process reasoning chains more effectively.

### 代码示例

> **EN:** How it looks

不再需要管理原始消息列表并将其发送给 `generateContent`，你的 ADK Agent 可以维护一个指向服务器端状态的更轻量级指针。

> **EN:** Instead of managing a raw list of messages and sending them to `generateContent`, your ADK agent can maintain a lighter-weight pointer to the server-side state.

```python
from google.adk.agents.llm_agent import Agent
from google.adk.models.google_llm import Gemini
from google.adk.tools.google_search_tool import GoogleSearchTool

root_agent = Agent(
    model=Gemini(
        model="gemini-2.5-flash",
        use_interactions_api=True,
    ),
    name="interactions_test_agent",
    tools=[
        GoogleSearchTool(bypass_multi_tools_limit=True),
        get_current_weather,
    ],
)
```

分步说明请参阅完整的 [ADK + Interactions API 示例](https://github.com/google/adk-python/tree/main/contributing/samples/interactions_api)。

> **EN:** For step by step instructions see the full [ADK sample with the Interactions API](https://github.com/google/adk-python/tree/main/contributing/samples/interactions_api).

这种模式让你将控制流和路由逻辑保留在 ADK 内部，同时将上下文管理和推理状态的重任委托给 Interactions API。

> **EN:** This pattern allows you to keep the control flow and routing logic within the ADK while delegating the heavy lifting of context management and inference state to the Interactions API.

我们通常将 API 内部的循环称为"内环"，将 Agent 代码中的循环称为"外环"，这个新 API 让你对两者都有了更多控制权。

> **EN:** We often describe an inner loop (inside the API) and an outer loop (in your agent code), and this new API gives you more control over both.

---

## 模式二：将 Interactions API Agent 作为远程 A2A Agent 使用

这正是 **Agent2Agent（A2A）** 协议互操作性大放异彩的地方。

> **EN:** This is where the interoperability of the Agent2Agent (A2A) protocol shines.

如果你已有 A2A 客户端或 Agent 生态系统，你可能希望它们能够调用全新的 **Gemini Deep Research Agent**。以往，集成新的第三方 API 需要编写自定义包装器或适配器。

> **EN:** If you have an existing ecosystem of A2A clients or agents, you might want them to consult the new Gemini Deep Research Agent. Historically, integrating a new third-party API would require writing a custom wrapper or adapter.

通过全新的 **`InteractionsApiTransport`**，我们将 [A2A 协议](https://a2a-protocol.org/latest/) 的接口直接映射到了 Interactions API 的接口上。它"讲"A2A。这意味着你可以将 Interactions API 端点视为另一个远程 A2A Agent。你现有的客户端无需知道它们正在与一个 Google 托管的 Agent 对话——它们只需看到一张 `AgentCard` 并照常发送消息即可。

> **EN:** With the new `InteractionsApiTransport`, we have mapped the A2A protocol surface directly onto the Interactions API surface. It "speaks" A2A. This means you can treat an Interactions API endpoint as just another remote A2A agent. Your existing clients don't need to know they are talking to a Google-hosted agent; they just see an `AgentCard` and send messages as usual.

### 桥接原理

> **EN:** How the Bridge Works

`InteractionsApiTransport` 层执行到 A2A 的翻译：

> **EN:** The `InteractionsApiTransport` layer performs a translation to A2A:

-   **A2A** **`SendMessage`** → **Interactions** **`create`**
-   **A2A** **`Task`** → **Interaction ID**
-   **A2A** **`TaskStatus`** → **Interaction Status**（例如，`IN_PROGRESS` 映射到 `TASK_STATE_WORKING`）

> **EN:** A2A `SendMessage` → Interactions `create`; A2A `Task` → Interaction ID; A2A `TaskStatus` → Interaction Status (e.g., `IN_PROGRESS` maps to `TASK_STATE_WORKING`)

注意：A2A 推送通知、A2A 扩展和 Interactions API 回调在此映射中暂不支持。

> **EN:** Note: A2A push notifications, A2A extensions, and Interactions API callbacks are not yet supported in this mapping.

### 代码示例：透明集成

> **EN:** Code Example: The Transparent Integration

要使用此功能，只需用新的传输层配置你的 A2A 客户端工厂，并创建一张指向你要使用的模型或 Agent 的卡片。

> **EN:** To use this, simply configure your A2A client factory with the new transport and create a card that points to the model or agent you want to use.

```python
from interactions_api_transport import InteractionsApiTransport
from a2a.client import ClientFactory, ClientConfig

client_config = ClientConfig()
client_factory = ClientFactory(client_config)
InteractionsApiTransport.setup(client_factory)

card = InteractionsApiTransport.make_card(
    url="https://generativelanguage.googleapis.com",
    agent="deep-research-pro-preview-12-2025"
)
card = InteractionsApiTransport.make_card(
    url="https://generativelanguage.googleapis.com",
    model="gemini-3-pro-preview",
    request_opts={
        "generation_config": { "thinking_summaries": "auto" }
    }
)
client = client_factory.create(card)

async for event in client.send_message(new_text_message("Research the history of Google TPUs")):
    print(event)
```

### 为什么这很重要

> **EN:** Why this matters

这种方式让 Interactions API 对你的开发者体验"透明"。你无需重构多 Agent 系统，即可立即访问像 Deep Research 这样强大的新工具。

> **EN:** This approach makes the Interactions API "transparent" to your developer experience. You gain immediate access to powerful new tools like Deep Research without refactoring your multi-agent system.

最棒的是，它开箱即用。

> **EN:** And the best part, it just works.

-   **无需学习新 SDK：** 你的 A2A 客户端代码保持不变。
-   **流式支持：** 传输层处理流式事件的映射，让你从 Agent 获得实时更新。
-   **配置嵌入：** 我们使用 A2A 扩展在 `AgentCard` 内部传递特定配置（如 `thinking_summaries`），同时不破坏标准协议。

> **EN:**
> - **No new SDKs to learn:** Your A2A client code stays the same.
> - **Streaming Support:** The transport handles mapping streaming events, so you get real-time updates from the agent.
> - **Configuration Smuggling:** We use A2A extensions to pass specific configurations (like `thinking_summaries`) inside the `AgentCard` without breaking the standard protocol.

---

## 结论

Gemini Interactions API 代表了 AI 通信建模方式的一次重大飞跃。无论你是使用任何框架（如 ADK）从头构建自定义 Agent，还是通过 A2A 将现有 Agent 连接在一起，这组新能力都值得你从今天开始探索。

> **EN:** The Gemini Interactions API represents a major step forward in how we model AI communication. Whether you are building custom agents from scratch using any framework like the ADK or connecting existing agents together via A2A, this is a new set of capabilities to start exploring today.

将 API 既视为卓越的推理引擎，又视为合规的远程 Agent，你可以以最小的摩擦快速扩展 Agent 网格的能力。在接下来的几周内，期待更多 ADK 和 A2A 相关资源发布，帮助开发者采用这一新 API。

> **EN:** By treating the API as both a superior inference engine and a compliant remote agent, you can rapidly expand the capabilities of your agentic mesh with minimal friction. Expect many more ADK and A2A resources over the next few weeks to help developers adopt this new API.

## 立即开始

-   阅读 [Gemini Interactions API 公告](https://blog.google/technology/developers/interactions-api) 及[文档](https://ai.google.dev/gemini-api/docs/interactions)
-   阅读 [Gemini Deep Research Agent 公告](https://blog.google/technology/developers/deep-research-agent-gemini-api) 及[文档](https://ai.google.dev/gemini-api/docs/deep-research)
-   查看 [ADK 变更日志](https://github.com/google/adk-python/blob/main/CHANGELOG.md)、[文档](https://google.github.io/adk-docs/) 和 [ADK + Interactions API 示例](https://github.com/google/adk-python/tree/main/contributing/samples/interactions_api)
-   查看[使用 Interactions API 的 A2A 示例](https://github.com/a2aproject/a2a-samples/tree/interactions-api/samples/python/transports/interactions_api)
