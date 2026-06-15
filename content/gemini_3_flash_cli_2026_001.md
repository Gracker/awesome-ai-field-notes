# Gemini 3 Flash Now Available in Gemini CLI: Pro-grade Coding Performance

- **来源**：Google Developers Blog
- **原文链接**：https://developers.googleblog.com/gemini-3-flash-is-now-available-in-gemini-cli/
- **作者**：Google AI
- **原始日期**：2026-04-30
- **抓取时间**：2026-06-15
- **质量评分**：4
- **抓取方式**：opencli web read

---

## English (Original)

![GeminiCLI\_Gemini3Flash\_1920x1080](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/GeminiCLI_Gemini3Flash_1920x1080.original.png)

Gemini 3 Flash is now available in Gemini CLI, supporting high-frequency workflows common to terminal-based work. [Gemini 3 Flash](https://blog.google/products/gemini/gemini-3-flash) achieves a SWE-bench Verified score of 78% for agentic coding, outperforming not only the 2.5 series, but also Gemini 3 Pro. Gemini 3 Flash was built to be highly efficient, pushing the Pareto frontier of quality vs. cost and speed and is available in preview at less than a quarter the cost of Gemini 3 Pro. With two of our best models powering Gemini CLI, speed no longer has to mean compromising quality.

## Start using Gemini 3 Flash with Gemini CLI

Starting today, [most](https://geminicli.com/docs/get-started/gemini-3/) paid tier customers of Gemini CLI have access to both Gemini 3 Pro and Gemini 3 Flash, including:

-   All non-business customers of Google AI Pro or AI Ultra
-   Users who have access using a paid API key through Google AI or Vertex
-   Gemini Code Assist users that have been [enabled by their cloud admin](https://geminicli.com/docs/get-started/gemini-3/#administrator-instructions) for preview models

For free tier users:

-   We’ve onboarded everyone who signed up to the previously available waitlist, so please check your email for details
-   If you were not on our waitlist, we’re rolling out additional access gradually to ensure the experience remains fast and reliable, so stay tuned for more details, or view our [docs](https://geminicli.com/docs/get-started/gemini-3/) to learn about your options for access now

Get started by upgrading Gemini CLI version to the latest version (0.21.1):

```plaintext
npm install -g @google/gemini-cli@latest
```

Plain text

Copied

After you’ve confirmed your version is 0.21.1 or later, run `/settings`, then toggle the setting “**Preview features”** to **true**. Once you’ve enabled preview features, run `/model` to select Gemini 3.

![GeminiCLI\_model\_selector](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/GeminiCLI_model_selector.original.png)

This release brings the full capabilities of the Gemini 3 family to your terminal. You can rely on Gemini CLI’s intelligent auto-routing to reserve Gemini 3 Pro for highly complex reasoning, or use the manual selector to dedicate a specific model to all of your tasks. The significant reasoning improvements in Gemini 3 Flash allow you to execute prompts that previously required slower Pro-tier models, at a lower cost.

## Build anything in the terminal with improved agentic coding

Gemini 3 Flash raises the performance floor of your coding sessions with strong performance in reasoning, tool use, and multimodal capabilities.

#### Generate a ready-to-deploy app with 3D graphics

We used Gemini 3 Pro in Gemini CLI to [build a 3D Voxel simulation of the Golden Gate Bridge](https://developers.googleblog.com/5-things-to-try-with-gemini-3-pro-in-gemini-cli/), treating the prompt as both a creative brief and a technical specification. But can Gemini 3 Flash do the same?

Previously, generating this level of functional code in a single pass was a job more suited for Pro models. Gemini 2.5 Flash, for example, often struggled with this complexity, resulting in broken logic. While Gemini 3 Pro's state-of-the-art reasoning creates a more visually appealing result, Gemini 3 Flash can still handle the task with precision, demonstrating that a rapid prototyping tool doesn't have to compromise code quality.

<video src="https://storage.googleapis.com/gweb-developer-goog-blog-assets/original_videos/Demo_1_Golden_Gate_Flash_studio.mp4" controls poster="https://storage.googleapis.com/gweb-developer-goog-blog-assets/original_videos/wagtailvideo-kebocq7h_thumb.jpg"></video>

## Improve your daily work

The true test of a development assistant is how it handles the high-volume, practical tasks you execute throughout the day. Gemini 3 Flash outperforms 2.5 Pro while being 3x faster at a fraction of the cost (based on [Artificial Analysis](https://artificialanalysis.ai/models/gemini-3-flash-reasoning) benchmarking).

#### Action code changes from large context windows

Managing large codebases often involves sifting through hundreds of comments on a pull request to find the single actionable item. This requires a model capable of holding a massive context window without losing track of specific instructions.

In this demo, Gemini 3 Flash processes a simulated pull request thread containing 1,000 comments. It successfully cuts through pages of "bikeshedding" to locate a single critical request regarding a timeout adjustment. Gemini CLI then applies the precise update to the configuration file on the first try. This demonstrates the model’s ability to distinguish signal from noise and execute accurate edits within massive context windows.

<video src="https://storage.googleapis.com/gweb-developer-goog-blog-assets/original_videos/Gemini_3_Flash_Gemini_CLI_Demo2_PR_analysis.mp4" controls poster="https://storage.googleapis.com/gweb-developer-goog-blog-assets/original_videos/wagtailvideo-efmuti5v_thumb.jpg"></video>

#### Simulate realistic user traffic for stress testing

Validating your backend infrastructure requires traffic that mimics actual user behavior, but writing custom load-testing scripts that handle concurrency and specific user journeys is often time consuming. These types of tasks are well suited for Gemini 3 Flash, reducing syntax hallucinations and failure loops, while still providing fast responses.

In this demo, Gemini CLI is used to stress-test a web application hosted on Cloud Run. Gemini 3 Flash generates a Python script using `asyncio` to simulate concurrent users across three distinct scenarios: "Successful Order," "Payment Failed," and "Inventory Timeout." When the initial execution returns protocol errors, the model instantly analyzes the traceback and patches the script. This allows you to launch a comprehensive load test and observe the resulting metrics in your Cloud Run dashboard in seconds.

<video src="https://storage.googleapis.com/gweb-developer-goog-blog-assets/original_videos/Gemini_3_Flash_Gemini_CLI_Demo3_Traffic_Sim.mp4" controls poster="https://storage.googleapis.com/gweb-developer-goog-blog-assets/original_videos/wagtailvideo-bn9deub8_thumb.jpg"></video>

## Stay in the flow longer

Gemini 3 Flash provides a new performance baseline for high-frequency development tasks in the terminal. By raising the performance floor and integrating with Gemini CLI’s auto-routing, it aims to help you work faster and more efficiently. Whether you are building a new prototype or managing complex infrastructure, you now have a development assistant capable of keeping up with your pace of work.

Update your Gemini CLI today to the latest version to start building faster — at a lower cost per token — with Gemini 3 Flash.

## 中文摘要

Gemini 3 Flash 现已可在 Gemini CLI 中使用，提供接近 Gemini 3 Pro 的专业级编码性能，同时具备低延迟与低成本特性。该模型在 SWE-bench Verified 上达到 78% 的智能编码得分，显著优于 2.5 Pro，改进了自动路由与代理编码能力。特别适合高频开发任务，能够处理复杂代码生成、超大上下文窗口（如处理 1000 条评论的 PR）与快速生成负载测试脚本。

## 中文翻译

Gemini 3 Flash 现已在 Gemini CLI 中可用，专为终端场景下的高频工作流打造。Gemini 3 Flash 在 SWE-bench Verified 上达到 78% 的智能编码得分，不仅超过 2.5 系列，也高于 Gemini 3 Pro。模型设计上追求极致效率，把质量–成本–速度的帕累托前沿向外推进，预览价格不到 Gemini 3 Pro 的四分之一。Gemini CLI 内部署了两款最强模型，速度不再以牺牲质量为代价。

### 立即开始使用 Gemini 3 Flash

大多数 Gemini CLI 付费用户今日起即可同时使用 Gemini 3 Pro 与 Gemini 3 Flash，包括：

- 所有非企业版 Google AI Pro / AI Ultra 用户
- 通过 Google AI 或 Vertex 付费 API Key 访问的用户
- 由云管理员启用了预览模型的 Gemini Code Assist 用户

免费用户方面：之前已加入候补名单的用户都已开通，请查收邮件；未加入候补名单的用户将分批开放，可关注文档。

**升级到 0.21.1**：npm install -g @google/gemini-cli@latest。确认版本后运行 /settings，把 Preview features 切到 true，再用 /model 选择 Gemini 3。

### 在终端里构建一切——智能编码能力提升

Gemini 3 Flash 在推理、工具调用与多模态方面显著抬高了编码会话的性能底线。

**生成可直接部署的 3D 图形应用**：之前用 Gemini 2.5 Flash 单次生成这种复杂度的功能性代码常常失败，而 Gemini 3 Pro 能产生视觉上更精致的结果。Gemini 3 Flash 也能精准完成任务，证明快速原型工具不必妥协代码质量。

### 改善日常工作

真正的开发助手考验在于日常高频的实际任务。Gemini 3 Flash 比 2.5 Pro 更强，速度快 3 倍，成本仅几分之一（依据 Artificial Analysis 基准）。

**在超长上下文中执行代码变更**：管理大型代码库常常需要在 PR 的几百条评论里筛出唯一可执行的项。Gemini 3 Flash 在演示中处理了 1000 条评论的模拟 PR 线程，精准定位超时调整的关键请求，并在首次尝试就把更新应用到配置文件。

**为压测模拟真实用户流量**：在演示中 Gemini 3 Flash 用 Python asyncio 模拟三种并发场景（成功下单、支付失败、库存超时）压测 Cloud Run 上的 Web 应用。初次执行返回协议错误时，模型即时分析 traceback 并打补丁脚本——几秒内即可启动完整压测。

### 长时间保持心流

Gemini 3 Flash 为终端高频开发任务提供了新的性能基线。通过抬高性能底线并接入 Gemini CLI 的自动路由，让开发者工作更快、更高效。无论是在构建新原型还是管理复杂基础设施，现在都有一款能跟上你节奏的开发助手。

立即升级 Gemini CLI，以更低 token 成本与 Gemini 3 Flash 一同更快构建。

---

*本文件由 AAIF Content Fetcher 自动抓取并双语整理。原文版权归原作者所有。*
