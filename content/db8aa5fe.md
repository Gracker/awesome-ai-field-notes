# Anthropic 开源对齐工具 Petri 捐赠给 Meridian Labs：版本 3.0 更新

**English Title:** Donating our open-source alignment tool  
**Author:** Anthropic  
**Source:** [Anthropic Research](https://www.anthropic.com/research/donating-open-source-petri) | [Meridian Labs Blog](https://meridianlabs.ai/blog/posts/introducing-petri-3/) | [Inspect Petri Docs](https://meridianlabs-ai.github.io/inspect_petri/)  
**Quality Score:** 4  
**Tags:** alignment, open-source, safety, evaluation, Anthropic, Meridian-Labs  
**Topics:** AI对齐与安全, 开源工具  

---

## English Original

In October 2025, we launched [Petri](https://www.anthropic.com/research/petri-open-source-auditing), an open-source toolbox of alignment tests that can be applied to any large language model. Petri, which was developed as part of our Anthropic Fellows program, can be used to rapidly and easily test AI models for concerning tendencies like deception, sycophancy, and cooperation with harmful requests. It's part of our efforts to develop alignment tools that are open and useful for the whole AI development community.

Petri has been part of our alignment assessment for every Claude model since Claude Sonnet 4.5. It compares how the new model behaves across a range of alignment-relevant scenarios that are simulated by a separate "auditor" model. A further "judge" model then scores the resulting transcripts for misaligned behaviors.

We've been pleased to see Petri being used by external organizations: for example, the UK's AI Security Institute (AISI) made it a [major part](https://arxiv.org/abs/2604.00788) of how they evaluate models for their propensity to sabotage AI research.

We're now updating Petri to its third version. Here are some of the biggest changes:

- **Adaptability.** Petri 3.0 involves major architectural changes that allow users to adapt it to more uses, in particular by splitting the auditor model and the target model into separate components that can be tweaked separately;
- **Realism.** Despite the fact that alignment researchers try to make tests appear realistic, a model can often deduce from various artificialities in the setup that it's actually part of a test. And if the model is aware it's being evaluated, the researcher is no longer able to see how the model behaves in general. An add-on to Petri, which we're calling "Dish," makes the setup far more realistic, for example by running the tests using the model's real system prompt and the real "scaffold" (the software that wraps around the model to help it meet its goals) that would be used in genuine model deployments;
- **Depth.** We've now integrated Petri with our other open-source alignment tool, [Bloom](https://www.anthropic.com/research/bloom), which can perform much more in-depth assessments of specific chosen behaviors (in comparison to Petri's wider-ranging approach).

We're also giving Petri a new home. We have handed over its development to [Meridian Labs](https://meridianlabs.ai/), an AI evaluation nonprofit. This move—similar to when we [donated](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation) the Model Context Protocol (MCP) to the Linux Foundation—will help ensure that Petri remains independent of any AI lab, so that its results will be seen as neutral and credible by those across the industry and beyond.

As part of Meridian Labs, Petri joins other tools like [Inspect](https://inspect.aisi.org.uk/) and [Scout](https://meridianlabs-ai.github.io/inspect_scout/), building a technology stack that is open to labs, independent researchers, and governments alike, at a time when reliable tests of AI model behavior matter more than ever.

You can read more about Petri 3.0 on [the Meridian Labs blog](https://meridianlabs.ai/blog/posts/introducing-petri-3/). Instructions to install and use Petri can be found on the [Petri website](https://meridianlabs-ai.github.io/inspect_petri/).

---

## 中文翻译

2025 年 10 月，我们发布了 [Petri](https://www.anthropic.com/research/petri-open-source-auditing)，这是一个可用于任何大型语言模型的开源对齐测试工具箱。Petri 诞生于 Anthropic Fellows 计划，可用于快速便捷地测试 AI 模型在欺骗、谄媚和对有害请求配合等令人担忧的倾向上。它是我们开发开放且对整个 AI 社区有用的对齐工具的努力的一部分。

自 Claude Sonnet 4.5 以来，Petri 一直是每个 Claude 模型对齐评估的一部分。它通过一个独立的"审计员"模型模拟一系列对齐相关场景，比较新模型的行为表现。然后一个"裁判"模型对产生的对话记录进行评分，识别对齐偏差行为。

我们很高兴看到外部组织也在使用 Petri：例如，英国 AI 安全研究所（AISI）将其作为[评估模型 sabotage AI 研究倾向](https://arxiv.org/abs/2604.00788)的主要手段。

我们现在将 Petri 更新至第三个版本。以下是一些最重要的变化：

- **适应性。**Petri 3.0 包含重大架构变更，允许用户适应更多用途，特别是将审计员模型和目标模型拆分为可独立调整的独立组件；
- **真实性。**尽管对齐研究人员试图让测试看起来真实，但模型通常可以从设置中的各种人工痕迹推断出自己正在被测试。如果模型知道自己正在被评估，研究人员就无法看到模型在通常情况下的行为表现。Petri 的一个附加组件（我们称之为"Dish"）使设置更加真实，例如使用模型真实的系统提示和真实"scaffold"（围绕模型帮助其实现目标的软件）来运行测试，这正是真实模型部署中会使用的；
- **深度。**我们已将 Petri 与另一个开源对齐工具 [Bloom](https://www.anthropic.com/research/bloom) 集成，后者可以对特定选定的行为进行更加深入（相对于 Petri 更广泛的方法）的评估。

我们也在为 Petri 寻找新归宿。我们已将开发工作移交给 AI 评估非营利组织 [Meridian Labs](https://meridianlabs.ai/)。这一举措——类似于我们[将模型上下文协议（MCP）](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation)捐赠给 Linux 基金会——将有助于确保 Petri 独立于任何 AI 实验室，使其结果在整个行业及更广泛范围内被视为中立和可信。

在 Meridian Labs，Petri 与 [Inspect](https://inspect.aisi.org.uk/) 和 [Scout](https://meridianlabs-ai.github.io/inspect_scout/) 等其他工具携手，构建一个对实验室、独立研究人员和政府同样开放的技术栈——在 AI 模型行为可靠测试比以往任何时候都更重要的时代。

---

## 技术细节

### 审计机制（Audit Mechanics）

Petri 在审计过程中协调三个模型角色：
- **审计员（Auditor）**：设计并驱动审计过程
- **目标（Target）**：被评估的模型
- **裁判（Judge）**：根据一套维度对审计结果评分

内置 170+ 种子场景，覆盖欺骗、谄媚、主动配合有害请求等行为。38 个内置裁判维度，可自行创建。

### 安装使用

```bash
pip install inspect-petri

export ANTHROPIC_API_KEY=...
export OPENAI_API_KEY=...

# 运行完整审计
inspect eval inspect_petri/audit \
  --model-role auditor=anthropic/claude-sonnet-4-6 \
  --model-role target=openai/gpt-5-mini \
  --model-role judge=anthropic/claude-opus-4-6

# 查看结果
inspect view
```
