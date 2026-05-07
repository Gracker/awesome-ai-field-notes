# 5 things to try with Gemini 3 Pro in Gemini CLI
# 在 Gemini CLI 中尝试 Gemini 3 Pro 的 5 种玩法

> 原文链接: https://developers.googleblog.com/5-things-to-try-with-gemini-3-pro-in-gemini-cli
> 原文作者: Google Developer Blog

---

![GeminiCLI_Gemini3_1920x1080](images/img_001.png)

**Gemini 3 Pro is now available in Gemini CLI**
**Gemini 3 Pro 现已登陆 Gemini CLI**

---

We've integrated [**Gemini 3 Pro**](https://blog.google/products/gemini/gemini-3), our most intelligent model, directly into Gemini CLI to unlock a new level of performance and productivity in the terminal. This powerful combination delivers state-of-the-art reasoning for executing better commands, enhances support for complex engineering work through agentic coding, and enables smarter, more tailored workflows via advanced tool use.

**EN:** We've integrated Gemini 3 Pro, our most intelligent model, directly into Gemini CLI to unlock a new level of performance and productivity in the terminal. This powerful combination delivers state-of-the-art reasoning for executing better commands, enhances support for complex engineering work through agentic coding, and enables smarter, more tailored workflows via advanced tool use.

**ZH:** 我们已将 Google 最智能的模型 Gemini 3 Pro 直接集成到 Gemini CLI 中，在终端解锁更高水平的性能和生产力。这一强大组合提供最先进的推理能力以执行更优质的命令，通过代理编码增强对复杂工程工作的支持，并通过高级工具使用实现更智能、更定制化的工作流程。

---

We are rolling out access gradually to ensure the experience remains fast and reliable.
**EN:** We are rolling out access gradually to ensure the experience remains fast and reliable.
**ZH:** 我们正在逐步开放访问权限，以确保体验保持快速和可靠。

- Gemini 3 Pro is available starting now in Gemini CLI for [**Google AI Ultra**](https://one.google.com/intl/en/about/google-ai-plans/) subscribers (Google AI Ultra for Business access is on the roadmap) and for those who have access via paid **Gemini API key.**
- **EN:** Gemini 3 Pro is available starting now in Gemini CLI for Google AI Ultra subscribers and for those who have access via paid Gemini API key.
- **ZH:** Gemini 3 Pro 即日起向 Google AI Ultra 订阅者和通过付费 Gemini API key 获得访问权限的用户提供 Gemini CLI 访问。

- For **Gemini Code Assist Enterprise** users, access is coming soon.
- **EN:** For Gemini Code Assist Enterprise users, access is coming soon.
- **ZH:** Gemini Code Assist Enterprise 用户即将获得访问权限。

- **All other users,** including Google AI Pro, Gemini Code Assist Standard, and free tier users can join the [waitlist here](https://forms.gle/ospXWr8SRTg73eBA8) to [get access as it becomes available](https://goo.gle/enable-preview-features).
- **EN:** All other users, including Google AI Pro, Gemini Code Assist Standard, and free tier users can join the waitlist to get access as it becomes available.
- **ZH:** 所有其他用户，包括 Google AI Pro、Gemini Code Assist Standard 和免费用户，都可以加入等待名单，在开放时获得访问权限。

---

## Start using Gemini 3 Pro with Gemini CLI
## 开始在 Gemini CLI 中使用 Gemini 3 Pro

If you're a Google AI Ultra subscriber or have a paid Gemini API key, get started immediately by upgrading your Gemini CLI version to **0.16.x**:
**EN:** If you're a Google AI Ultra subscriber or have a paid Gemini API key, get started immediately by upgrading your Gemini CLI version to 0.16.x.
**ZH:** 如果你是 Google AI Ultra 订阅者或拥有付费 Gemini API key，立即升级 Gemini CLI 版本到 0.16.x 开始使用：

```shell
npm install -g @google/gemini-cli@latest
```

Shell

Copied

After you've confirmed your version, run `/settings`, then toggle **Preview features** to **true**. Gemini CLI will now default to Gemini 3 Pro.

**EN:** After you've confirmed your version, run /settings, then toggle Preview features to true. Gemini CLI will now default to Gemini 3 Pro.

**ZH:** 确认版本后，运行 /settings，然后将 Preview features 切换为 true。Gemini CLI 现在将默认使用 Gemini 3 Pro。

...

(Full article continues with 5 practical examples: 3D graphics generation, UI sketch to code, shell commands, documentation generation, and Cloud Run debugging)

---

Here are 5 practical ways you can tap into Gemini 3 Pro in Gemini CLI to accelerate development and bring your biggest ideas to life.
**EN:** Here are 5 practical ways you can tap into Gemini 3 Pro in Gemini CLI to accelerate development and bring your biggest ideas to life.
**ZH:** 以下是你可以在 Gemini CLI 中利用 Gemini 3 Pro 加速开发、实现最大胆想法的 5 种实用方法。

---

## 1. Build anything in the terminal with improved agentic coding
## 1. 通过改进的代理编码在终端中构建任何内容

Gemini 3 Pro excels at coding because of its ability to synthesize disparate pieces of information, including text, images, and code, and follow complex, creative instructions. It understands the intent behind your idea, allowing you to go from a rough concept to a functional starting point in a single step.

**EN:** Gemini 3 Pro excels at coding because of its ability to synthesize disparate pieces of information, including text, images, and code, and follow complex, creative instructions.
**ZH:** Gemini 3 Pro 擅长编码，因为它能够综合包括文本、图像和代码在内的不同信息，并遵循复杂、创造性的指令。

**3. Generate complex shell commands with natural language**
**3. 用自然语言生成复杂的 shell 命令**

With Gemini CLI, the power of the UNIX command line is available directly through natural language. No need to memorize the obscure syntax and every flag of UNIX commands, simply have Gemini 3 Pro translate your intent and execute it for you.

**EN:** With Gemini CLI, the power of the UNIX command line is available directly through natural language.
**ZH:** 通过 Gemini CLI，UNIX 命令行的强大功能可直接通过自然语言使用，无需记住晦涩的语法和每个标志。

---

## 5. Debug performance issue in a live Cloud Run service
## 5. 调试线上 Cloud Run 服务的性能问题

Gemini 3 Pro can orchestrate complex workflows across different services that hold your team's context. The improved tool use means it can plan and execute multi-step tasks that require gathering information from several sources—like observability, security, and source control—to solve a single problem.

**EN:** Gemini 3 Pro can orchestrate complex workflows across different services that hold your team's context.
**ZH:** Gemini 3 Pro 可以在持有团队上下文的不同服务之间编排复杂的工作流程。

---

## Learn more today
## 立即了解更多

These examples are just the start. The real potential isn't in running these specific commands, but in how Gemini 3 Pro can adapt to your unique challenges whether you're optimizing daily shell commands, tackling substantial engineering work, or building a workflow personalized to your team's tools.

**EN:** These examples are just the start.
**ZH:** 这些例子只是开始。真正的潜力不在于运行这些特定命令，而在于 Gemini 3 Pro 如何适应你的独特挑战。

Visit the [Gemini CLI website](https://geminicli.com/), and share your own examples on social with #GeminiCLI. We can't wait to see what you build.
**EN:** Visit the Gemini CLI website and share your own examples on social with #GeminiCLI.
**ZH:** 访问 Gemini CLI 网站，并在社交媒体上分享你的示例，记得带上 #GeminiCLI。期待看到你的作品。
