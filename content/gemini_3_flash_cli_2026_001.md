# Gemini 3 Flash Now Available in Gemini CLI: Pro-grade Coding Performance

> **ID:** `gemini_3_flash_cli_2026_001`  
> **Author:** Google AI  
> **Source:** <https://developers.googleblog.com/gemini-3-flash-is-now-available-in-gemini-cli/>  
> **Date:** 2026-04-30  
> **Category:** coding-agents/tools  
> **Quality Score:** 4  
> **Tags:** Gemini 3 Flash, CLI, coding performance, SWE-bench, agentic coding, 2026  
> **Fetched:** 2026-06-07 20:30:34  
> **One-liner:** Gemini 3 Flash重新定义了CLI工具的性能标准，在保持低成本的同时提供接近Pro级的编码能力  
> **摘要 (zh):** Gemini 3 Flash现已可在Gemini CLI中使用，提供接近Gemini 3 Pro的专业级编码性能，具有低延迟和低成本特性。该模型在SWE-bench验证中达到76%的分数，显著优于2.5 Pro版本，改进了自动路由和代理编码能力。特别适合高频率开发任务，能够处理复杂代码生成、大上下文窗口（如处理1000条注释的PR）和快速生成负载测试脚本。  

---

## English (Original)

# Gemini 3 Flash is now available in Gemini CLI
> 原文链接: https://developers.googleblog.com/gemini-3-flash-is-now-available-in-gemini-cli/

---

![GeminiCLI\_Gemini3Flash\_1920x1080](images/img_001.png)

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

![GeminiCLI\_model\_selector](images/img_002.png)

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

---

## 中文翻译

_等待人工或后续流水线翻译。_
