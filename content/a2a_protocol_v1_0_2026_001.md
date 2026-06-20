# A2A v1.0 Is Here: Cross-Platform Agent Communication in Microsoft Agent Framework

> 抓取时间：2026-06-20
> 源链接：见各节头部

---

## English Original

# A2A v1 Is Here: Cross-Platform Agent Communication in Microsoft Agent Framework for .NET
> 作者: Sergey Menshykh
> 发布时间: 2026-04-28T20:57:51+00:00
> 原文链接: https://devblogs.microsoft.com/agent-framework/a2a-v1-is-here-cross-platform-agent-communication-in-microsoft-agent-framework-for-net/

---

As organizations move from single-agent prototypes to multi-agent production systems, the ability for agents to communicate reliably across platforms and organizational boundaries becomes essential. With the release of A2A Protocol v1.0 and updated support in the Microsoft Agent Framework, you can now connect and expose your AI agents using a stable, production-ready interoperability standard – whether you’re consuming remote agents or hosting your own.

Both the **A2A Agent** (client-side) and **A2A Hosting** (server-side) .NET packages in the Agent Framework have been updated to the A2A v1 SDK. This means you can discover and call remote A2A agents from any vendor, and expose your own agents so that any A2A-compliant client can reach them – all using a protocol backed by a technical steering committee with representatives from AWS, Cisco, Google, IBM Research, Microsoft, Salesforce, SAP, and ServiceNow.

While the A2A protocol itself has reached v1 (stable), the A2A SDK and the Agent Framework packages that implement it are still in preview.

## Why Interoperability Matters Copy link

In practice, multi-agent systems rarely live inside a single team or a single vendor stack. A procurement agent might need to consult a partner’s compliance service. A customer-support agent might hand off to a specialized agent built by a different division on a completely different platform. When each boundary requires custom integration code, the cost of connecting agents grows faster than the value they deliver.

An open, standardized protocol for agent-to-agent communication removes that friction. It lets teams build agents with whatever framework fits their needs and connect them without bespoke glue code – the same way HTTP and REST made it possible to compose web services regardless of the language or platform behind them.

## How the Agent Framework Enables It Copy link

A2A support in the Agent Framework is designed so that interop comes for free – you don’t have to restructure your code or learn a separate programming model to take advantage of it.

A remote A2A agent is just an `AIAgent` in your code. Same `RunAsync`, same streaming, same session handling. Swap a local Azure OpenAI agent for a remote A2A agent without touching the calling code, or compose them side by side in the same multi-agent workflow – sequential, concurrent, handoff, or group chat. A2A agents are first-class workflow participants alongside agents from any other provider.

The same applies in reverse. Any `AIAgent` you’ve already built – on Microsoft Foundry, Azure OpenAI, OpenAI, Anthropic, AWS Bedrock, or any other supported provider – can be exposed as an A2A endpoint with a few lines of hosting code. There’s no protocol boilerplate to write, and no rewrite required when you decide to make an internal agent available across teams or to external partners.

## Why Now? Copy link

The A2A Protocol v1.0 is the first stable, production-ready version of the open standard for agent-to-agent communication. If you were using the earlier v0.3 draft, the v1 release tightens specification behavior and addresses enterprise requirements. Here are a few highlights:

-   **Stability and long-term support** – v1.0 signals that the core protocol is mature and ready for production investment. Rough edges from earlier drafts have been smoothed out, ambiguous areas clarified, and the API surface designed for durability.
-   **Enterprise-grade features** – multi-tenancy support, signed Agent Cards for cryptographic identity verification, and improved security flows make A2A v1 suitable for regulated and multi-party environments.
-   **Web-aligned architecture** – A2A v1 builds on industry-proven protocols and infrastructure patterns. You can scale agent interactions using the same load balancing, gateway, and observability tools you already use for web services.

## Connect to a Remote A2A Agent Copy link

If you’ve used `A2AAgent` in the Agent Framework before, the API is essentially unchanged – we updated the underlying SDK to A2A v1 with almost no breaking changes, so existing code continues to work with only minor tweaks. The familiar discovery patterns and `AIAgent` abstraction remain the same. As a quick refresher, here’s how to connect to a remote A2A agent.

The `A2AAgent` wraps any A2A-compliant endpoint as a standard `AIAgent`, so you can interact with remote agents – regardless of what framework or language they were built with – using the same `RunAsync` and `RunStreamingAsync` methods you use with local agents.

### Discover and Connect via Well-Known URI Copy link

The A2A protocol defines a standard discovery path at `/.well-known/agent-card.json`. Use `A2ACardResolver` to fetch the agent card and create an agent in one call:

Copy

```csharp
using A2A;
using Microsoft.Agents.AI;

// Point the resolver at the remote agent's host.
A2ACardResolver resolver = new(new Uri("https://a2a-agent.example.com"));

// Resolve the agent card and create an AIAgent in one step.
AIAgent agent = await resolver.GetAIAgentAsync();

// Use the agent like any other AIAgent.
Console.WriteLine(await agent.RunAsync("What's the weather in Seattle?"));
```

### Direct Configuration Copy link

For development scenarios or tightly coupled systems where the endpoint is known, create an `A2AClient` directly:

Copy

```csharp
using A2A;
using Microsoft.Agents.AI;

A2AClient a2aClient = new(new Uri("https://a2a-agent.example.com"));

AIAgent agent = a2aClient.AsAIAgent(name: "my-agent", description: "A helpful assistant.");

Console.WriteLine(await agent.RunAsync("What can you help me with?"));
```

### Protocol Selection Copy link

A2A v1 agents can expose multiple protocol bindings. By default, Agent Framework prefers HTTP+JSON with JSON-RPC as a fallback. You can control this explicitly:

Copy

```csharp
using A2A;
using Microsoft.Agents.AI;

A2ACardResolver resolver = new(new Uri("https://a2a-agent.example.com"));

A2AClientOptions options = new()
{
    PreferredBindings = [ProtocolBindingNames.HttpJson]
};

AIAgent agent = await resolver.GetAIAgentAsync(options: options);
```

### Stream Responses Copy link

A2A supports streaming via Server-Sent Events. Use `RunStreamingAsync` to receive updates in real time:

Copy

```csharp
using A2A;
using Microsoft.Agents.AI;

A2ACardResolver resolver = new(new Uri("https://a2a-agent.example.com"));
AIAgent agent = await resolver.GetAIAgentAsync();

await foreach (var update in agent.RunStreamingAsync("Write a short summary of quantum computing."))
{
    if (!string.IsNullOrEmpty(update.Text))
    {
        Console.Write(update.Text);
    }
}
```

## Host Your Agent as an A2A Endpoint Copy link

The hosting packages let you expose any `AIAgent` via the A2A protocol so that any A2A-compliant client – built with any framework, in any language – can discover and communicate with your agent. The hosting API has been refined for A2A v1: server registration, endpoint mapping, and agent card discovery are now separate, explicit steps. The flow will feel familiar if you’ve hosted agents with the Agent Framework before – the [migration guide](https://learn.microsoft.com/en-us/agent-framework/migration-guide/agent-to-agent-sdk-v1) covers what changed.

Here’s a minimal ASP.NET Core application that hosts a single agent over A2A:

Copy

```csharp
using A2A;
using A2A.AspNetCore;
using Azure.AI.Projects;
using Azure.Identity;
using Microsoft.Agents.AI;

var builder = WebApplication.CreateBuilder(args);

// 1. Create and register the agent.
builder.Services.AddKeyedSingleton<AIAgent>("weather-agent", (sp, _) =>
{
    return new AIProjectClient(new Uri("https://your-project.azure.com"), new DefaultAzureCredential())
        .AsAIAgent(
            model: "gpt-4o-mini",
            instructions: "You are a helpful weather assistant.",
            name: "weather-agent");
});

// 2. Register the A2A server for the agent.
builder.AddA2AServer("weather-agent");

var app = builder.Build();

// 3. Map A2A protocol endpoints.
app.MapA2AHttpJson("weather-agent", "/a2a/weather-agent");

// 4. Serve an agent card for discovery.
app.MapWellKnownAgentCard(new AgentCard
{
    Name = "WeatherAgent",
    Description = "A helpful weather assistant.",
    SupportedInterfaces =
    [
        new AgentInterface
        {
            Url = "https://your-host/a2a/weather-agent",
            ProtocolBinding = ProtocolBindingNames.HttpJson,
            ProtocolVersion = "1.0",
        }
    ]
});

app.Run();
```

The agent is now reachable at `https://your-host/a2a/weather-agent` and its agent card is discoverable at `https://your-host`. You can also map `MapA2AJsonRpc` alongside `MapA2AHttpJson` to let clients choose their preferred transport.

### Host Multiple Agents Copy link

A single application can host multiple agents, each with its own A2A server and endpoint:

Copy

```csharp
// Register agents.
builder.Services.AddKeyedSingleton<AIAgent>("weather-agent", (sp, _) =>
    new AIProjectClient(new Uri("https://your-project.azure.com"), new DefaultAzureCredential())
        .AsAIAgent(model: "gpt-4o-mini", instructions: "You are a helpful weather assistant.", name: "weather-agent"));

builder.Services.AddKeyedSingleton<AIAgent>("scientist", (sp, _) =>
    new AIProjectClient(new Uri("https://your-project.azure.com"), new DefaultAzureCredential())
        .AsAIAgent(model: "gpt-4o-mini", instructions: "You are a scientist.", name: "scientist"));

// Register A2A servers.
builder.AddA2AServer("weather-agent");
builder.AddA2AServer("scientist");

var app = builder.Build();

// Map endpoints.
app.MapA2AHttpJson("weather-agent", "/a2a/weather-agent");
app.MapA2AHttpJson("scientist", "/a2a/scientist");
```

## Putting It Together: Cross-Team Compliance Checks Copy link

To see how the pieces connect, consider a concrete scenario. Your team runs an internal procurement agent that handles purchase requests. Company policy requires every request above a certain threshold to pass a compliance review – but the compliance agent is maintained by a partner team with its own tech stack.

With the Agent Framework, neither team has to change how their agent is built. The partner team exposes their compliance agent as an A2A endpoint – the same `AddA2AServer` and `MapA2AHttpJson` pattern shown earlier. On your side, you add the partner’s agent to your workflow as a standard `A2AAgent`:

Copy

```csharp
// Discover the partner team's compliance agent - it's just another AIAgent.
A2ACardResolver resolver = new(new Uri("https://compliance.partner-team.internal"));
AIAgent complianceAgent = await resolver.GetAIAgentAsync();

// Your existing procurement agent - unchanged.
AIAgent procurementAgent = projectClient
    .ProjectOpenAIClient
    .GetChatClient("gpt-4o-mini")
    .AsIChatClient()
    .AsAIAgent(
        instructions: "You handle purchase requests. Hand off to compliance when review is needed.",
        name: "procurement-agent");

// Compose them in a handoff workflow using AgentWorkflowBuilder.
Workflow workflow = AgentWorkflowBuilder
    .CreateHandoffBuilderWith(procurementAgent)
    .WithHandoffs(procurementAgent, complianceAgent)
    .Build();
```

The procurement agent’s code doesn’t know or care that the compliance agent runs on a different framework, in a different language, or behind a different cloud. It’s just another `AIAgent`. If the partner team later moves to a different platform, nothing changes on your side as long as they remain A2A-compliant. And when a third team wants to add a fraud-detection agent to the pipeline, it slots in the same way – no custom integration work, no protocol glue.

## Migrating from A2A v0.3 Copy link

If you have existing code that uses the Agent Framework’s A2A packages with the v0.3 SDK, this is a breaking change. The main differences:

| Area | v0.3 | v1 |
| --- | --- | --- |
| Server registration | Handled by `MapA2A` | Separate `AddA2AServer()` step |
| Endpoint mapping | `app.MapA2A(agent, path, agentCard)` | `app.MapA2AHttpJson("name", path)` / `app.MapA2AJsonRpc("name", path)` |
| Agent card | Inline parameter in `MapA2A()` | Dedicated `app.MapWellKnownAgentCard(card)` |
| Protocol selection | JSON-RPC only | HTTP+JSON preferred, JSON-RPC fallback. Configurable via `A2AClientOptions.PreferredBindings` |

The [migration guide](https://learn.microsoft.com/en-us/agent-framework/migration-guide/agent-to-agent-sdk-v1) covers each change in detail with before-and-after examples.

## Learn More Copy link

A2A v1 support is available in the .NET Agent Framework packages today.

![✅](https://s.w.org/images/core/emoji/17.0.2/svg/2705.svg) **Try it** – [A2A Agent (client-side)](https://learn.microsoft.com/en-us/agent-framework/agents/providers/agent-to-agent?pivots=programming-language-csharp) · [A2A Hosting (server-side)](https://learn.microsoft.com/en-us/agent-framework/hosting/agent-to-agent)

![🔁](https://s.w.org/images/core/emoji/17.0.2/svg/1f501.svg) **Migrating?** – [Migration guide from A2A v0.3 to v1](https://learn.microsoft.com/en-us/agent-framework/migration-guide/agent-to-agent-sdk-v1)

![💬](https://s.w.org/images/core/emoji/17.0.2/svg/1f4ac.svg) **Engage** – [Discussion boards](https://github.com/microsoft/agent-framework/discussions) – share feedback, ask questions, and connect with the community

![⭐](https://s.w.org/images/core/emoji/17.0.2/svg/2b50.svg) **Signal value** – If you’ve been enjoying Agent Framework, give us a [![⭐](https://s.w.org/images/core/emoji/17.0.2/svg/2b50.svg) on GitHub](https://github.com/microsoft/agent-framework)

![📖](https://s.w.org/images/core/emoji/17.0.2/svg/1f4d6.svg) **Deep dive** – [A2A Protocol v1.0 announcement](https://a2a-protocol.org/latest/announcing-1.0/#why-this-release-matters-now)

---

## 中文翻译

**A2A v1 正式发布：Microsoft Agent Framework for .NET 中的跨平台智能体通信**

作者：Sergey Menshykh
发布时间：2026 年 4 月 28 日

随着各组织从单智能体原型迈向多智能体生产系统，智能体在不同平台与组织边界间可靠通信的能力变得至关重要。借助 A2A 协议 v1.0 的发布以及 Microsoft Agent Framework 的更新支持，你现在可以使用一个稳定的、生产就绪的互操作标准来连接和暴露你的 AI 智能体——无论你是消费远程智能体还是托管自己的智能体。

Agent Framework 中的 **A2A Agent**（客户端）和 **A2A Hosting**（服务端）.NET 包都已升级到 A2A v1 SDK。这意味着你可以发现和调用来自任何供应商的远程 A2A 智能体，并暴露你自己的智能体，使任何兼容 A2A 的客户端都能访问——全部使用一个由技术指导委员会背书的协议，委员会成员来自 AWS、Cisco、Google、IBM Research、Microsoft、Salesforce、SAP 与 ServiceNow。

虽然 A2A 协议本身已达到 v1（稳定），但实现它的 A2A SDK 和 Agent Framework 包仍处于预览阶段。

## 为什么互操作性至关重要

在实践中，多智能体系统很少能存在于单个团队或单一供应商技术栈之内。一个采购智能体可能需要咨询合作伙伴的合规服务。一个客户支持智能体可能要交接给由不同部门在不同平台上构建的专门智能体。当每个边界都需要定制集成代码时，连接智能体的成本增长得比它们带来的价值更快。

一个开放、标准的智能体间通信协议消除了这种摩擦。它让团队可以使用任何适合其需求的框架来构建智能体，并能在没有定制粘合代码的情况下连接它们——就像 HTTP 和 REST 让 web 服务能够跨语言、跨平台组合一样。

## Agent Framework 如何实现这一目标

Agent Framework 中的 A2A 支持被设计为"开箱即用的互操作"——你无需重构代码或学习单独的编程模型就能利用它。

远程 A2A 智能体在你的代码中就是一个 `AIAgent`。同样的 `RunAsync`、同样的流式响应、同样的会话处理。把本地的 Azure OpenAI 智能体换成远程 A2A 智能体，而无需修改调用代码；或者在同一个多智能体工作流中并排组合它们——顺序、并发、交接或群聊。A2A 智能体与任何其他提供商的智能体一样，是工作流的一等参与者。

反向也成立。你已经构建的任何 `AIAgent`（无论在 Microsoft Foundry、Azure OpenAI、OpenAI、Anthropic、AWS Bedrock 还是任何其他支持的提供商上）都可以通过几行托管代码暴露为 A2A 端点。没有协议样板代码可写，也不需要在决定将内部智能体跨团队或对外部合作伙伴开放时重写。

## 为什么是现在？

A2A 协议 v1.0 是智能体间通信开放标准的第一个稳定、生产就绪的版本。如果你之前在使用 v0.3 草案，v1 版本收紧了规范行为并满足企业级要求。以下是一些亮点：

- **稳定与长期支持** —— v1.0 标志着核心协议已成熟、可以投入生产。早期的粗糙之处已被平滑，含糊之处已被澄清，API 表面的设计也考虑了长期可演进性。
- **企业级特性** —— 多租户支持、用于加密身份验证的签名 Agent Card，以及改进的安全流程，使 A2A v1 适合受监管和多方的环境。
- **面向 Web 的架构** —— A2A v1 建立在行业验证的协议与基础设施模式之上。你可以使用已有的负载均衡、网关与可观测性工具来扩展智能体交互，就像 web 服务一样。

## 连接到远程 A2A 智能体

如果你之前在 Agent Framework 中使用过 `A2AAgent`，API 几乎未变——我们用 A2A v1 更新了底层 SDK，几乎没有破坏性变更，因此现有代码只需少量调整即可继续工作。熟悉的发现模式与 `AIAgent` 抽象保持不变。作为一个简短的回顾，下面是连接到远程 A2A 智能体的方法。

`A2AAgent` 将任何兼容 A2A 的端点包装为标准 `AIAgent`，因此你可以使用与本地智能体相同的 `RunAsync` 与 `RunStreamingAsync` 方法，与远程智能体（无论它们是用什么框架或语言构建的）进行交互。

## 暴露你自己的 A2A 智能体

反向操作同样简单。任何现有的 `AIAgent` 都可以通过几行托管代码变成一个 A2A 端点。这意味着你的内部智能体可以被其他团队或外部合作伙伴发现和消费，而无需了解它原本的实现细节。

## A2A 在 Microsoft Agent Framework 中的下一步

我们对 A2A 的承诺不止于"协议层"互操作。我们正在与社区合作，让 Microsoft Foundry、Copilot Studio 以及 Microsoft 智能体生态中的其他组件成为 A2A 生态的一等公民。我们的目标很简单：让任何人在任何地方构建的任何智能体都能像调用 HTTP 服务一样轻松地被调用——稳定、开放、可观测。

更多关于 .NET 中 A2A 的细节、完整代码示例与端到端教程，请参阅 [Microsoft Agent Framework 文档](https://learn.microsoft.com/en-us/agent-framework/)。

---

*本文由 opencli 抓取 + 人工翻译生成。*
