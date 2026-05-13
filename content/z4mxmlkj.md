# Building AI Agents with Google Gemini 3 and Open Source Frameworks

> 原文链接: https://developers.googleblog.com/building-ai-agents-with-google-gemini-3-and-open-source-frameworks/

---
![BuildingWAgents-Gemini3_Wagtial_RD1-V01](images/img_001.png)

The world of AI agents is rapidly evolving from simple chatbots to sophisticated, (semi)-autonomous systems that can make complex decisions in the real-world. This week, we introduced **Gemini 3 Pro Preview**, our most powerful agentic model designed to act as the core orchestrator for these advanced workflows.

We worked extensively with open-source partners to integrate and test the model. This post covers the new agentic features in Gemini 3 and how to start building next-generation agents using open source frameworks, including [LangChain](https://www.langchain.com/), [AI SDK by Vercel](https://ai-sdk.dev/), [LlamaIndex](https://www.llamaindex.ai/), [Pydantic AI](https://ai.pydantic.dev/), and [n8n](https://n8n.io/).

## Why Gemini 3 for your Agents?

Gemini 3 introduces features designed to give developers granular control over cost, latency, and reasoning depth, making it the most capable foundation for agents yet:

-   **Control Reasoning with thinking\_level:** Adjust the logic depth on a per-request basis. Set thinking\_level to **high** for deep planning, bug finding, and complex instruction following. Set it to **low** for high-throughput tasks to achieve latency comparable to Gemini 2.5 Flash with superior output quality.
-   **Stateful Tool Use via Thought Signatures:** The model now generates encrypted "Thought Signatures" representing its internal reasoning before calling a tool. By passing these signatures back in the conversation history, your agent retains its exact train of thought, ensuring reliable multi-step execution without losing context.
-   **Adjustable Multimodal Fidelity:** Balance token usage and detail with media\_resolution. Use **high** for analyzing fine text in images, **medium** for optimal PDF document parsing, and **low** to minimize latency for video and general image descriptions.
-   **Large Context Consistency:** Combined with thought signatures, the large context window mitigates "reasoning drift," allowing agents to maintain consistent logic over long sessions.

## Agentic Open Source Ecosystem: Day 0 Support

We’ve collaborated side-by-side with the open-source community to ensure libraries are ready to tap into Gemini 3 immediately. Here are some of the top frameworks offering Day 0 support.

### LangChain

![langchain](images/img_002.png)

[LangChain](https://www.langchain.com/) provides an agent engineering platform and open-source frameworks, [LangChain](https://www.langchain.com/langchain) and [LangGraph](https://www.langchain.com/langgraph) for millions of Developers. By representing workflows as graphs, developers can build stateful, multi-actor AI agents that leverage Gemini and Gemini embedding models directly.

_"The new Gemini model is a strong step forward for complex, agentic workflows — especially for those who need sophisticated reasoning and tool use. We’re excited to support it across LangChain and LangGraph so developers can easily build and deploy reliable agents from day one.” - Harrison Chase, LangChain_

Get started with [LangChain for Gemini](https://python.langchain.com/docs/integrations/chat/google_generative_ai/).

### AI SDK by Vercel

![ai-sdk](images/img_003.png)

The [AI SDK](https://ai-sdk.dev/docs/introduction) is a TypeScript toolkit designed to help developers build AI-powered applications and agents with React, Next.js, Vue, Svelte, Node.js, and more. Using the Google provider, developers can implement features such as text streaming, tool use or structured generation with Gemini 3.

_“Our internal benchmarking of Gemini 3 Pro showed immense improvements in reasoning and code generation, with almost a 17% increase in success rate over Gemini 2.5 Pro placing it in the top 2 of the Next.js leaderboard. We are thrilled to support this new level of capability Day 0 in the AI SDK, AI Gateway and v0.” — Aparna Sinha, Vercel_

Get started with the [AI SDK](https://ai-sdk.dev/providers/ai-sdk-providers/google-generative-ai) by Vercel.

### LlamaIndex

![LlamaIndex](images/img_004.png)

[LlamaIndex](https://www.llamaindex.ai/) is a specialized framework for building knowledge agents using Gemini connected to your data. This includes tools across agent workflow orchestration, data loading, parsing, extraction, and indexing with both LlamaIndex open-source tooling and LlamaCloud.

_“In our early access testing, Gemini 3 Pro outperformed previous generations in handling complex tool calls and maintaining context. It provides the high-accuracy foundation developers need to build reliable knowledge agents that interact with their own data.” - Jerry Liu, LlamaIndex_

Get started with [LlamaIndex](https://docs.llamaindex.ai/en/stable/examples/llm/gemini/).

### Pydantic AI

![pydantic-ai](images/img_005.png)

[Pydantic AI](https://ai.pydantic.dev/) is a framework for building type-safe agents in Python. It supports Gemini models directly, allowing developers to leverage Python type hints to define agent schemas. This ensures that agent workflows produce predictable, type-correct data suitable for integration into downstream production systems.

_“Combining Gemini 3’s advanced reasoning with Pydantic AI’s type safety provides the reliability developers need for production agents. We are thrilled to have validated the integration to offer full library support on Day 0.” - Douwe Maan_

Get Started with [Pydantic](https://ai.pydantic.dev/models/google/).

### n8n

![n8n](images/img_006.png)

[n8n](https://n8n.io/) is a workflow automation platform that enables technical and non-technical teams to build AI agents without writing code. With Gemini 3 Pro, n8n brings the power of advanced reasoning to operations, marketing, and business teams.

_“Gemini 3 brings the power of advanced reasoning to everyone, not just software engineers. By integrating this model into n8n, we are enabling non-developers to build sophisticated, reliable agents that can transform their daily operations without writing a single line of code.”_ — Angel Menendez

Get started with [n8n](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgooglegemini/).

### **Best Practices and Next Steps**

Ready to upgrade? Follow these guidelines to ensure your agents run successfully on Gemini 3:

-   **Simplify Prompts:** Stop using complex "Chain of Thought" prompt engineering. Rely on the thinking\_level parameter to handle reasoning depth natively.
-   **Keep Temperature at 1.0:** Do not lower the temperature. Gemini 3’s reasoning engine is optimized for 1.0; lowering it may cause looping or degraded performance in complex tasks.
-   **Handle Thought Signatures:** You must capture the [thoughtSignature](https://ai.google.dev/gemini-api/docs/thought-signatures) from the model response and pass it back. This is enforced for Function Calling; missing signatures will result in API errors.
-   **Optimize Visual Tokens:** Set media\_resolution\_medium for PDFs (quality saturates here to save tokens) and reserve high only for dense details in images.
-   **Review the Guide:** Read the full [Gemini 3 Developer Guide](https://ai.google.dev/gemini-api/docs/gemini-3) for critical details on migration, rate limits, and new API parameters.