# 浅谈 Agent、MCP、OpenAI Responses API

**来源**: 微信公众号
**原文链接**: https://mp.weixin.qq.com/s?__biz=MzIzNjE2NTI3NQ==&mid=2247489654&idx=1&sn=6e3820486124182688ebfeb296b395af&chksm=e933ade78907c108f8ca19416a225107a2679c2882d7a88366c8ad812d738da54c647ba740fb&mpshare=1&scene=1&srcid=03124z9ByYy482nSTotR3dqO

---

今天本想写篇关于 OpenAI Responses API 的文章，但近期 AI 热门话题挺多，感觉有必要简单聊聊。

Agent、MCP 近期频繁出现在大众视野，近日，OpenAI 又宣布推出 Responses API 助力开发者。术语名词越来越多，脑子明显感觉不够用了...

- AI Agent 是一个更广泛的概念，它通常指能够自主行动的智能实体（执行一系列复杂多步骤任务直出结果）。
- MCP 是一种大模型上下文开放协议，旨在标准化 LLM 与外部系统的集成，从而增强 AI Agent 的功能。
- OpenAI Responses API 是一个具体的 API，它提供了一种便捷调用 OpenAI 大模型能力的方式（如 web 搜索、文件搜索、内置工具等），来构建用户自己的 Agent。
关于 AI Agent 这里还有一张 E2B/awesome-ai-agents[1] 整理的高逼格图片，虽有半年时间未更新了，但也足以看出 Agent 生态的庞大。

近期热点

去年，由 Cognition 团队开发的全球首个 AI 软件工程师 Devin[2] 引爆 AI 社区，只需用户下达指令，Devin 就可自主完成开发、调试、部署等各种开发任务。而最近出圈的 Manus[3] 则号称“全球首个通用 Agent”，可以帮助用户完成各种复杂任务直出结果（不知道有多人被邀请码割韭菜了）。Manus 的出圈甚至带火了一些另类开源项目，如 OpenManus[4]（Manus 的非官方开源版）、BrowserUse[5] 等。

📌 BrowserUseBrowserUse 是将 AI 代理与浏览器连接起来的最简单方法，它通过为浏览器自动化提供强大而简单的界面，使 AI 代理可以访问网站执行数据抓取、表单填写和网站导航等任务。

如果对 Agent 开发相关内容感兴趣，以下官方示例或代码可引导你快速开始：

- Anthropic Quickstarts[6]：一系列项目代码，旨在帮助开发者快速开始使用 Anthropic API 构建应用程序。每个快速入门都提供了一份基础代码，你可以在此基础上轻松构建或自定义来满足特定需求。
- Computer Using Agent Sample App[7]：使用 OpenAI API 构建计算机使用代理（CUA）。
Agent 的火爆让 MCP 再次回归到用户视野，如果还不了解 MCP，可以看看我之前写的《深度解析：Anthropic MCP 协议》。简单来说：Anthropic 的模型上下文协议（Model Context Protocol）是一种标准化的开放协议，允许 AI 模型连接并访问外部数据源和工具，使 AI 应用程序更具交互性且能够感知周围环境。

目前支持 MCP 的应用有：Claude Desktop[8]、Cursor[9]、Zed[10]、Cline[11]、Continue[12] 等。

📌 MCPModel Context Protocol (MCP) 是 Anthropic 推出的一种新系统，用于增强 AI 模型的功能。它是一个标准化的开放协议，能够让 AI 模型（如 Claude）在不需要针对每项新集成编写自定义代码的情况下，就能连接到数据库、API、文件系统以及其他工具。

MCP 遵循一种 客户端-服务器 模型，包含以下三个关键组件：

- Host：Host 运行 MCP Client。如 Claude 之类的 AI 桌面端应用（非网页版），提供了 AI 交互的环境，使其能够访问各种工具和数据源。
- MCP Client：这是 AI 模型（如 Claude）内部的组件，使其能与 MCP Server 通信。如 AI 模型需要从 PostgreSQL 获取数据，MCP Client 会将请求格式化为结构化消息并发送给 MCP Server。
- MCP Server：充当将 AI 模型连接到外部系统（如 PostgreSQL、Google Drive 或某个 API）的中间人。如：Claude 要分析来自 PostgreSQL 的销售数据，PostgreSQL 的 MCP Server 就是 Claude 与数据库之间的连接器。
MCP 有五个核心构造（也被称为基本单元），它们分别属于客户端和服务器端：

- 对于客户端而言，核心构造是 Roots（安全文件访问）和 Sampling（向 AI 请求协助完成任务，例如生成数据库查询）。
- 对于服务器而言，核心构造包括 Prompts（指示 AI 的指导信息）、Resources（AI 可引用的数据对象）以及 Tools（AI 可调用的函数，例如运行数据库查询）。
如果以上描述对你来说有点抽象，我还整理了 @mattpocockuk[13] 对 MCP 的解释：模型上下文协议（MCP）旨在简化大型语言模型（LLM）与外部 API 的集成过程，解决传统方法中需要大量“粘合代码”的问题。由于各种服务（如 Slack、GitHub）都有独特的 API，将 LLM 与它们连接通常需要繁琐的定制代码。MCP 通过引入一个中间层，即 MCP 服务器，标准化了 LLM 与外部资源的交互。具体来说，MCP 系统由三个关键部分组成：

- MCP 服务器
- 负责与实际的 API 进行通信，执行诸如发送 Slack 消息或获取 GitHub 仓库等操作。
- 可以部署在远程服务器或本地系统上。
- MCP 客户端
- 与 MCP 服务器通信，并可以同时连接到多个服务器，从而实现对不同服务的集成。
- 使得 LLM 能够通过统一的接口访问各种外部功能。
- MCP 协议
- 作为客户端和服务器之间的通用语言，确保它们能够相互理解和交互。
- 它提供了一种标准化的方式，使得 LLM 能够调用 MCP 服务器提供的“工具”。
通过这种方式，MCP 消除了对大量定制代码的需求，使得 LLM 能够更快速、更灵活地集成新功能。用户可以“购买”或部署现成的 MCP 服务器，从而快速增强 LLM 的功能。这种架构提供了一种流畅、无摩擦的体验，类似于使用 USB 接口将不同设备连接在一起。总而言之，MCP 通过标准化 LLM 与外部资源的交互方式，极大地提升了 LLM 应用的功能性和可扩展性。

OpenAI Agent Tools

近日，OpenAI 针对开发者发布了构建智能体新工具（New tools for building agents[14]）。在此之前，就已推出过 DeepResearch[15] 和 Operator[16] 等智能体解决方案（更强的搜索推理、多模态人机交互及安全性改进等），为模型构建 Agent 处理复杂多步任务奠定了基础。

开发者将模型诸多能力通过 API 集成进应用投入生产时，常需要多次提示迭代和自定义编排逻辑，缺乏有效的可视化调试工具及一些常用内置功能。为了解决此痛点，OpenAI 推出一系列全新 API 和工具，让开发者和企业可以更轻松的构建可靠 Agent。

- Responses API：融合集成了 Chat Completions API 的简单性和 Assistants API 的工具使用能力。
- 内置工具：包括网络搜索（web search）、文件搜索（file search）和计算机使用（computer use）。
- Agents SDK：可用于编排单 Agent 或多 Agent 工作流。
- 集成化可观测性工具：可跟踪和检查 Agent 工作流的执行过程。
这些新增功能将核心 Agent 逻辑、编排以及交互所需的工作大幅简化，让开发者能更快地开始构建 Agent。未来数周和数月内，还将不断引入更多功能和工具，进一步降低在 OpenAI 平台上构建 Agent 的难度。

Responses API 简介

Responses API 是 OpenAI 为利用内置工具构建 Agent 推出的新 API 原语。它结合了 Chat Completions[17] 的易用性和 Assistants API[18] 的工具调用能力。随着模型能力不断演进，Responses API 能为开发者构建具备 Agent 能力的应用提供更灵活的基础。借助 Responses API 的单次调用，开发者可通过多次模型调用与工具使用，解决愈发复杂的任务。

📌 API 原语在计算机编程中，API 原语（API primitive）指的是一种最基础或最核心的 API 设计元素，或者说“原生的 API 组件”。它是用来支持更高层次功能或框架的最底层抽象和接口。简单来说，此处的 “API 原语”就是为构建和扩展 Agent 提供的底层基础功能或调用入口，开发者可以在此之上进一步封装、组合、定制，从而搭建出更丰富、更复杂的应用场景。

目前，Responses API 支持内置工具有网络搜索、文件搜索和计算机操作等。这些工具结合在一起，可以让模型与真实世界连通。Responses API 除了带来一系列易用性提升，还包括统一基于 “item” 的设计、更简单的多态式用法、直观的流式事件，以及如 response.output_text 等开发者工具辅助方法，可轻松获取模型输出。该 API 也使 OpenAI 存储数据变得简单，方便开发者借助可追踪和评测等功能来评估 Agent 性能（如果你正在使用 OpenRouter[19] 之类的第三方 API 聚合商，则不一定支持此功能）。值得注意的是：即使这些数据存储在 OpenAI 上，OpenAI 默认也不会使用业务数据对模型进行训练。该 API 现已对所有开发者开放，并不额外收取费用，仅按照官网定价标准计费（了解更多 Responses API docs[20]）。

对现有 API 的影响

Chat Completions API 依然是使用最广泛的 API，将继续向其引入新的模型与功能。若开发者不需要内置工具，可继续使用 Chat Completions。OpenAI 会在确保新功能不依赖内置工具或多次模型调用的前提下，不断向 Chat Completions 新增模型。不过，Responses API 是 Chat Completions 的增强版，拥有同等优异的性能，且具备更多特性。因此，对新集成来说，推荐直接使用 Responses API。

在 Assistants API 测试版期间，OpenAI 收集了大量开发者反馈，并将其中的关键改进引入到 Responses API，使其更灵活、快速、易用。目前正努力让 Responses API 在功能上全面覆盖 Assistants API，包括对 Assistant-like 和 Thread-like 对象的支持，以及对 Code Interpreter 工具的支持。完成功能对齐后，会正式发布 Assistants API 的弃用通知，目标时间是 2026 年中。弃用后会提供迁移指南，帮助大家无缝保留数据并迁移应用。在正式发布弃用消息前，会继续为 Assistants API 提供新模型。请注意，Responses API 将是未来在 OpenAI 平台构建 Agent 的主线。

Responses API 的内置工具

网络搜索

开发者可借助 gpt-4o 和 gpt-4o-mini 模型，通过网络搜索工具快速获取实时答案，同时附上清晰且相关的引用链接。Responses API 中的网络搜索可与其他工具或函数调用结合使用：

// JavaScript 代码示例

const response = await openai.responses.create({
    model: "gpt-4o",
    tools: [ { type: "web_search_preview" } ],
    input: "What was a positive news story that happened today?",
});

console.log(response.output_text);
在 OpenAI 的早期测试中，许多应用场景都对实时网络信息提出了迫切需求，如购物助手、研究型智能代理以及旅游预订代理等。以 Hebbia[21] 为例，该公司致力于为资产管理、私募股权、信贷以及法律行业提供高效的搜索解决方案，旨在帮助用户从海量的公共与私有数据集中快速提取具有实际价值的洞察。为此，Hebbia 在其研究流程中深度集成了实时搜索功能，从而显著丰富了市场情报的上下文信息，并持续提升了分析的精准度和准确性。

在 SimpleQA[22] 基准上（用于衡量 LLM 对简短事实性问题的回答准确度），GPT‑4o search preview 和 GPT‑4o mini search preview 分别达到 90% 和 88% 的准确率。

通过集成网络搜索工具，OpenAI API 能够生成带有来源链接的响应，这些链接指向新闻文章、博客等，为用户提供了便捷的详细信息查阅途径，同时也为内容提供者带来了新的流量机会。为了确保网站或发布者的内容能够被 OpenAI 的网络搜索结果收录，建议参考 OpenAI 站点收录说明（Overview of OpenAI Crawlers[23]）。

# Overview of OpenAI Crawlers: https://platform.openai.com/docs/bots
# 以下内容用于指导 OpenAI 的各个机器人如何访问您的网站
# 请注意：更新 robots.txt 后可能需要约 24 小时生效

# ------------------------------
# OAI-SearchBot
# 用途：用于搜索，将您的网站链接呈现在 ChatGPT 的搜索结果中，不用于爬取用于训练生成式 AI 模型的内容。
# 完整的 user-agent 字符串: "OAI-SearchBot/1.0; +https://openai.com/searchbot"
# 已公布的 IP 地址列表: https://openai.com/searchbot.json
User-agent: OAI-SearchBot
Allow: /

# ------------------------------
# ChatGPT-User
# 用途：用于 ChatGPT 和 Custom GPTs 中的用户操作。帮助回答问题并附带来源链接，不用于自动爬取或生成式 AI 模型训练。
# 完整的 user-agent 字符串: "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; ChatGPT-User/1.0; +https://openai.com/bot"
# 已公布的 IP 地址列表: https://openai.com/chatgpt-user.json
User-agent: ChatGPT-User
Allow: /

# ------------------------------
# GPTBot
# 用途：用于爬取可能用于训练生成式 AI 基础模型的内容。禁止 GPTBot 表示您不希望内容用于训练生成式 AI 模型。
# 完整的 user-agent 字符串: "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; GPTBot/1.1; +https://openai.com/gptbot"
# 已公布的 IP 地址列表: https://openai.com/gptbot.json
User-agent: GPTBot
Disallow: /
目前，该搜索工具已在 Responses API 中以预览版的形式向所有开发者开放。此外，OpenAI 还为 Chat Completions API 提供了专门优化的模型，包括 gpt-4o-search-preview 和 gpt-4o-mini-search-preview，以满足不同的搜索需求。这些模型的定价分别为每千次查询 $30 和 $25。

开发者可通过 OpenAI Playground[24] 进行试用，或通过查阅文档 Web search[25] 获取更详细的使用指南。

文件搜索

开发者现在能够利用经过改进的文件搜索工具，从大规模文档集合中高效检索所需信息。该工具支持多种文件类型，并具备查询优化、元数据过滤以及自定义重排等功能，从而能够快速且准确地返回检索结果。通过 Responses API，开发者仅需编写少量代码即可实现集成，以下是一个示例：

// JavaScript 代码示例

const productDocs = await openai.vectorStores.create({
    name: "Product Documentation",
    file_ids: [file1.id, file2.id, file3.id],
});

const response = await openai.responses.create({
    model: "gpt-4o-mini",
    tools: [{
        type: "file_search",
        vector_store_ids: [productDocs.id],
    }],
    input: "What is deep research by OpenAI?",
});

console.log(response.output_text);
文件搜索工具适用于广泛的实际业务场景，例如：

- 客户支持智能代理：快速查阅常见问题解答（FAQ），以提供即时帮助。
- 法律助手：协助专业人士搜索相关案例，提高法律研究效率。
- 编程助手：便于开发者查询技术文档，加速软件开发进程。
以 Navan[26] 为例，该公司在其 AI 驱动的旅行预订代理中集成了文件搜索功能，从而能够快速从知识库文章（如公司差旅政策）中提取精确答案。该工具预置的查询优化与重排功能，使得 Navan 无需进行额外的配置即可构建强大的检索增强生成（RAG）流水线。此外，通过为每个用户群体创建专属的向量存储，系统能够根据用户的权限和角色提供更加个性化的答案，从而显著节省了客户和员工的时间，并确保了信息的准确性。

此文件搜索工具通过 Responses API 向所有开发者开放，定价为每千次查询 $2.5，文件存储费用为 $0.1/GB/天（前 1GB 免费）。该工具也可继续在 Assistants API 中使用。此外，OpenAI 还为 Vector Store API 对象新增了一个搜索端点，以便在其他应用和 API 中利用检索功能，可在 File search[27] 文档或 Playground 进一步了解细节。

计算机操作（CUA）

为了让 Agent 能执行计算机环境中的任务，开发者现可在 Responses API 中使用由 Computer-Using Agent（CUA）模型驱动的计算机操作工具（computer use tool）。这个预研模型已经在 Operator 中得到应用，并在多个相关基准测试中取得了显著成绩，例如在 OSWorld[28] 上实现了 38.1% 的成功率，在 WebArena[29] 上达到了 58.1%，在 WebVoyager[30] 上更是高达 87%。

CUA 工作原理图，了解更多 Computer-Using Agent[31]

在 Responses API 中使用计算机操作工具时，模型会生成相应的鼠标和键盘操作指令。开发者可以在自己的环境中将这些指令直接映射为可执行的命令，从而实现计算机的自动化操作。以下是一个示例代码：

// JavaScript 代码示例

const response = await openai.responses.create({
    model: "computer-use-preview",
    tools: [{
        type: "computer_use_preview",
        display_width: 1024,
        display_height: 768,
        environment: "browser",
    }],
    truncation: "auto",
    input: "I'm looking for a new camera. Help me find the best one.",
});

console.log(response.output);
该工具可用于自动化浏览器操作场景，例如 Web 应用的质量保证测试或遗留系统数据录入流程。例如，Unify[32] 可利用此工具访问原本缺乏 API 的信息（如在线地图），为地产管理公司确认某业务地址是否扩张，再据此触发后续的精准外联。又如 Luminai[33] 利用该工具在大型企业中自动化操作繁琐的工作流程，替代过去难以实现的传统机器人流程自动化 (RPA)。

在将 CUA 扩展到本地操作系统之前，OpenAI 已对 Operator 进行了大量安全测试和红队演练，聚焦在滥用、防范模型错误及前沿风险三大领域。面对在本地操作系统上的更多操作风险，也进行了额外的安全评估与红队演练，并向开发者提供相应的安全保障措施，包括针对提示注入的防护、敏感操作确认提示、环境隔离工具以及对潜在政策违规的检测。然而，需要注意的是，模型在非浏览器环境下仍有出现错误的可能。目前在 OSWorld 基准上，CUA 的表现为 38.1%，并不适合完全无人工监督场景。更多有关这方面的安全性信息，可参见更新后的 system card[34]。

自即日起，计算机操作工具在 Responses API 中作为预研功能向部分使用门槛（tiers 3-5）开发者开放。使用价格为每百万输入 token 收费 $3、输出 token 收费 $12。可在文档 Computer use[35] 中查看详情。

Agents SDK

除了为 Agent 提供核心逻辑与工具支持，使其在完成任务时更有效，开发者还需要编排这些 Agent 的工作流。全新的开源 Agents SDK[36] 旨在简化多 Agent 工作流的编排，并在之前 Swarm[37] 项目的基础上做了重大改进。Swarm 作为一款实验性 SDK，曾被开发者社区广泛采用并成功部署于多个客户场景。SDK 主要改进包括：

- Agents：可轻松配置 LLM，包含清晰的指令与内置工具。
- Handoffs：在多个 Agent 之间智能传递控制权。
- Guardrails：可配置的输入、输出安全检查。
- Tracing & Observability：可视化 Agent 执行过程，便于调试和性能优化。
# Python 代码示例

from agents import Agent, Runner, WebSearchTool, function_tool, guardrail

@function_tool
def submit_refund_request(item_id: str, reason: str):
    # Your refund logic goes here
    return"success"

support_agent = Agent(
    name="Support & Returns",
    instructions="You are a support agent who can submit refunds [...]",
    tools=[submit_refund_request],
)

shopping_agent = Agent(
    name="Shopping Assistant",
    instructions="You are a shopping assistant who can search the web [...]",
    tools=[WebSearchTool()],
)

triage_agent = Agent(
    name="Triage Agent",
    instructions="Route the user to the correct agent.",
    handoffs=[shopping_agent, support_agent],
)

output = Runner.run_sync(
    starting_agent=triage_agent,
    input="What shoes might work best with my outfit so far?",
)
Agents SDK 适用于多种场景，包括客户支持自动化、多步研究、内容生成、代码审查和销售线索挖掘。例如，Coinbase[38] 仅用数小时就基于 Agents SDK 原型并上线了 AgentKit[39]，让 AI Agent 能与加密钱包及链上活动无缝互动。他们通过将自有 Developer Platform SDK 的操作集成进 Agent 中，快速实现了一个强大的 Agent 原型。又例如，Box[40] 利用 Agents SDK 配合网络搜索工具，为企业提供针对其在 Box 中存储的大量非结构化数据以及公共互联网信息的搜索、查询与摘要功能，既能获取实时信息，也能保证内部权限与安全策略。

Agents SDK 可与 Responses API 及 Chat Completions API 搭配使用，也能与其他提供 Chat Completions 风格 API 的模型配合使用。目前该 SDK 提供 Python 版本，Node.js 版本即将推出。详情可参见官方文档 agents docs[41]。

在设计 Agents SDK 时，OpenAI 也从社区的一些优秀项目中汲取了灵感，例如 Pydantic[42]、Griffe[43] 和 MkDocs[44] 等。

结语

网上有很多无脑吹 Agent 的，各种震惊，声称要取代人类！技术迭代快速发展的成果不可否认，但它们仍面临巨大挑战，如大模型上下文长度限制、Token 指数级消耗、AI 返回结果的正确性等等。

从 Devin 到 OpenAI Operator、再到最近比较出圈的 Manus，可以看到 Agent 都在加速放大 AI 的能力。 Agent 的概念很棒，完全自主规划路径提供复杂任务解决方案的智能体更棒，但当它们陷入程序死循环或在错误路径上越走越远时，还是需要“人”把它再次拉回来...

References

[1]E2B/awesome-ai-agents: https://github.com/e2b-dev/awesome-ai-agents

[2]Devin: https://devin.ai

[3]Manus: https://manus.im

[4]OpenManus: https://github.com/mannaandpoem/OpenManus

[5]BrowserUse: https://github.com/browser-use/browser-use

[6]Anthropic Quickstarts: https://github.com/anthropics/anthropic-quickstarts

[7]Computer Using Agent Sample App: https://github.com/openai/openai-cua-sample-app

[8]Claude Desktop: https://claude.ai/download

[9]Cursor: https://www.cursor.com

[10]Zed: https://github.com/zed-industries/zed

[11]Cline: https://github.com/cline/cline

[12]Continue: https://github.com/continuedev/continue

[13]@mattpocockuk: https://x.com/mattpocockuk/status/1897742389592440970

[14]New tools for building agents: https://openai.com/index/new-tools-for-building-agents

[15]DeepResearch: https://openai.com/index/introducing-deep-research

[16]Operator: https://openai.com/index/introducing-operator

[17]Chat Completions: https://platform.openai.com/docs/api-reference/chat

[18]Assistants API: https://platform.openai.com/docs/api-reference/assistants

[19]OpenRouter: https://openrouter.ai

[20]Responses API docs: https://platform.openai.com/docs/quickstart?api-mode=responses

[21]Hebbia: https://www.hebbia.com

[22]SimpleQA: https://openai.com/index/introducing-simpleqa

[23]Overview of OpenAI Crawlers: https://platform.openai.com/docs/bots

[24]OpenAI Playground: https://platform.openai.com/playground/chat

[25]Web search: https://platform.openai.com/docs/guides/tools-web-search

[26]Navan: https://navan.com

[27]File search: https://platform.openai.com/docs/guides/tools-file-search

[28]OSWorld: https://os-world.github.io

[29]WebArena: https://webarena.dev

[30]WebVoyager: https://arxiv.org/abs/2401.13919

[31]Computer-Using Agent: https://openai.com/index/computer-using-agent

[32]Unify: https://www.unifygtm.com

[33]Luminai: https://www.luminai.com

[34]system card: https://openai.com/index/operator-system-card

[35]Computer use: https://platform.openai.com/docs/guides/tools-computer-use

[36]Agents SDK: https://github.com/openai/openai-agents-python

[37]Swarm: https://github.com/openai/swarm

[38]Coinbase: https://www.coinbase.com

[39]AgentKit: https://replit.com/t/coinbase-developer-platform/repls/CDP-AgentKit-Agents-SDK-Quickstart/view#README.md

[40]Box: https://www.box.com

[41]agents docs: https://platform.openai.com/docs/guides/agents

[42]Pydantic: https://pydantic.dev

[43]Griffe: https://mkdocstrings.github.io/griffe

[44]MkDocs: https://www.mkdocs.org
