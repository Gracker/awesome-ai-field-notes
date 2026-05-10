# Gemini 3 Flash is now available in Gemini CLI

Gemini 3 Flash 现已在 Gemini CLI 中可用

---

## English

DEC. 17, 2025

Gemini 3 Flash is now available in Gemini CLI, supporting high-frequency workflows common to terminal-based work. Gemini 3 Flash achieves a SWE-bench Verified score of 78% for agentic coding, outperforming not only the 2.5 series, but also Gemini 3 Pro. Gemini 3 Flash was built to be highly efficient, pushing the Pareto frontier of quality vs. cost and speed and is available in preview at less than a quarter the cost of Gemini 3 Pro. With two of our best models powering Gemini CLI, speed no longer has to mean compromising quality.

## Start using Gemini 3 Flash with Gemini CLI

Starting today, most paid tier customers of Gemini CLI have access to both Gemini 3 Pro and Gemini 3 Flash, including:

- All non-business customers of Google AI Pro or AI Ultra
- Users who have access using a paid API key through Google AI or Vertex
- Gemini Code Assist users that have been enabled by their cloud admin for preview models

For free tier users:

- We've onboarded everyone who signed up to the previously available waitlist, so please check your email for details
- If you were not on our waitlist, we're rolling out additional access gradually to ensure the experience remains fast and reliable, so stay tuned for more details, or view our docs to learn about your options for access now

Get started by upgrading Gemini CLI version to the latest version (0.21.1):

```bash
npm install -g @google/gemini-cli@latest
```

After you've confirmed your version is 0.21.1 or later, run /settings, then toggle the setting "Preview features" to true. Once you've enabled preview features, run /model to select Gemini 3.

This release brings the full capabilities of the Gemini 3 family to your terminal. You can rely on Gemini CLI's intelligent auto-routing to reserve Gemini 3 Pro for highly complex reasoning, or use the manual selector to dedicate a specific model to all of your tasks. The significant reasoning improvements in Gemini 3 Flash allow you to execute prompts that previously required slower Pro-tier models, at a lower cost.

## Build anything in the terminal with improved agentic coding

Gemini 3 Flash raises the performance floor of your coding sessions with strong performance in reasoning, tool use, and multimodal capabilities.

### Generate a ready-to-deploy app with 3D graphics

We used Gemini 3 Pro in Gemini CLI to build a 3D Voxel simulation of the Golden Gate Bridge, treating the prompt as both a creative brief and a technical specification. But can Gemini 3 Flash do the same?

Previously, generating this level of functional code in a single pass was a job more suited for Pro models. Gemini 2.5 Flash, for example, often struggled with this complexity, resulting in broken logic. While Gemini 3 Pro's state-of-the-art reasoning creates a more visually appealing result, Gemini 3 Flash can still handle the task with precision, demonstrating that a rapid prototyping tool doesn't have to compromise code quality.

### Improve your daily work

The true test of a development assistant is how it handles the high-volume, practical tasks you execute throughout the day. Gemini 3 Flash outperforms 2.5 Pro while being 3x faster at a fraction of the cost (based on Artificial Analysis benchmarking).

### Action code changes from large context windows

Managing large codebases often involves sifting through hundreds of comments on a pull request to find the single actionable item. This requires a model capable of holding a massive context window without losing track of specific instructions.

In this demo, Gemini 3 Flash processes a simulated pull request thread containing 1,000 comments. It successfully cuts through pages of "bikeshedding" to locate a single critical request regarding a timeout adjustment. Gemini CLI then applies the precise update to the configuration file on the first try. This demonstrates the model's ability to distinguish signal from noise and execute accurate edits within massive context windows.

### Simulate realistic user traffic for stress testing

Validating your backend infrastructure requires traffic that mimics actual user behavior, but writing custom load-testing scripts that handle concurrency and specific user journeys is often time consuming. These types of tasks are well suited for Gemini 3 Flash, reducing syntax hallucinations and failure loops, while still providing fast responses.

In this demo, Gemini CLI is used to stress-test a web application hosted on Cloud Run. Gemini 3 Flash generates a Python script using asyncio to simulate concurrent users across three distinct scenarios: "Successful Order," "Payment Failed," and "Inventory Timeout." When the initial execution returns protocol errors, the model instantly analyzes the traceback and patches the script. This allows you to launch a comprehensive load test and observe the resulting metrics in your Cloud Run dashboard in seconds.

## Stay in the flow longer

Gemini 3 Flash provides a new performance baseline for high-frequency development tasks in the terminal. By raising the performance floor and integrating with Gemini CLI's auto-routing, it aims to help you work faster and more efficiently. Whether you are building a new prototype or managing complex infrastructure, you now have a development assistant capable of keeping up with your pace of work.

Update your Gemini CLI today to the latest version to start building faster — at a lower cost per token — with Gemini 3 Flash.

---

## 中文

2025年12月17日

Gemini 3 Flash 现已在 Gemini CLI 中可用，支持终端工作中常见的高频工作流。Gemini 3 Flash 在代理编码任务中取得了 78% 的 SWE-bench Verified 分数，不仅超越了 2.5 系列，也超越了 Gemini 3 Pro。Gemini 3 Flash 以高效为核心，优化了质量、成本与速度的帕累托边界，目前预览版价格不到 Gemini 3 Pro 的四分之一。有了这两款最强模型为 Gemini CLI 提供动力，速度不再意味着牺牲质量。

## 开始在 Gemini CLI 中使用 Gemini 3 Flash

即日起，大多数 Gemini CLI 付费用户均可使用 Gemini 3 Pro 和 Gemini 3 Flash，包括：

- 所有非商业用途的 Google AI Pro 或 AI Ultra 用户
- 通过 Google AI 或 Vertex 使用付费 API 密钥的用户
- 已由云管理员启用预览模型访问权限的 Gemini Code Assist 用户

免费用户：

- 我们已将为数不多的内测名单用户全部加入，请查收邮件了解详情
- 如果你不在内测名单中，我们将逐步开放更多访问权限，以确保体验依然快速可靠，敬请期待更多详情，或查阅文档了解当前可用的访问方式

请将 Gemini CLI 升级至最新版本（0.21.1）开始使用：

```bash
npm install -g @google/gemini-cli@latest
```

确认版本为 0.21.1 或更高后，运行 /settings，然后将"预览功能"开关设置为 true。启用预览功能后，运行 /model 选择 Gemini 3。

此次发布将 Gemini 3 全系列能力带入你的终端。你可以让 Gemini CLI 的智能自动路由为高度复杂推理任务预留 Gemini 3 Pro，也可以手动选择特定模型来处理所有任务。Gemini 3 Flash 在推理能力上的显著提升，使你能够以更低的成本执行此前需要更慢的 Pro 级别模型才能完成的提示。

## 使用增强的代理编码能力在终端中构建任何内容

Gemini 3 Flash 以强大的推理、工具使用和多模态能力，提升了你的编码会话性能基线。

### 生成可部署的 3D 图形应用

我们曾在 Gemini CLI 中使用 Gemini 3 Pro 构建了金门大桥的 3D Voxel 仿真，将提示词同时作为创意简报和技术规格。但 Gemini 3 Flash 能做到吗？

此前，生成这种级别的功能性代码通常需要 Pro 级别的模型。以 Gemini 2.5 Flash 为例，面对这种复杂度往往力不从心，最终生成的代码逻辑破碎。虽然 Gemini 3 Pro 的前沿推理能力能带来更美观的视觉效果，但 Gemini 3 Flash 依然能够精确完成这项任务，证明快速原型工具不必在代码质量上妥协。

### 提升你的日常工作

开发助手真正的考验在于如何处理你整天执行的大量高实用性任务。根据 Artificial Analysis 的基准测试，Gemini 3 Flash 在速度提升 3 倍、成本仅为几分之一的情况下，性能优于 2.5 Pro。

### 从大上下文窗口中处理代码变更

管理大型代码库通常需要在数百条 PR 评论中筛选出唯一可操作的条目。这要求模型能够持有巨大的上下文窗口，同时不丢失特定指令。

在这个演示中，Gemini 3 Flash 处理了一条包含 1000 条评论的模拟 PR 讨论。它成功穿越了成页的"无效争论"，定位到关于超时调整的单一关键请求。Gemini CLI 随后一次性精确更新了配置文件。这展示了模型在巨大上下文窗口中区分信号与噪音，并执行精确编辑的能力。

### 模拟真实用户流量进行压力测试

验证后端基础设施需要模拟真实用户行为的流量，但编写处理并发和特定用户旅程的自定义负载测试脚本通常非常耗时。这类任务非常适合 Gemini 3 Flash，能够减少语法幻觉和失败循环，同时依然提供快速响应。

在这个演示中，Gemini CLI 被用来对托管在 Cloud Run 上的 Web 应用进行压力测试。Gemini 3 Flash 使用 asyncio 生成 Python 脚本来模拟三个不同场景的并发用户："成功下单"、"支付失败"和"库存超时"。当初次执行返回协议错误时，模型立即分析回溯信息并修补脚本。这让你能够快速启动全面的负载测试，并在 Cloud Run 仪表板中观察结果指标。

## 保持更长的心流状态

Gemini 3 Flash 为终端中的高频开发任务设定了新的性能基线。它通过提升性能下限并与 Gemini CLI 的自动路由集成，旨在帮助你更快、更高效地工作。无论你是在构建新原型还是管理复杂基础设施，你现在拥有了一个能够跟上你工作节奏的开发助手。

今天就将 Gemini CLI 更新到最新版本，开始以更低的每 token 成本——使用 Gemini 3 Flash 更快地构建。