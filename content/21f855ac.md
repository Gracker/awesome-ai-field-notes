# Anthropic 将开源对齐工具 Petri 捐赠给 Meridian Labs，发布 v3 版本

---

**英文原文：**

In October 2025, we launched Petri, an open-source toolbox of alignment tests that can be applied to any large language model. Petri, which was developed as part of our Anthropic Fellows program, can be used to rapidly and easily test AI models for concerning tendencies like deception, sycophancy, and cooperation with harmful requests. It's part of our efforts to develop alignment tools that are open and useful for the whole AI development community.

**中文翻译：**

2025 年 10 月，我们推出了 Petri，这是一个开源的对齐测试工具箱，可应用于任何大型语言模型。Petri 是我们 Anthropic Fellows 计划的一部分，用于快速、便捷地测试 AI 模型是否存在欺骗、谄媚和配合有害请求等令人担忧的倾向。这是我们为开发开放且对整个 AI 行业有益的对齐工具所做的努力之一。

---

**英文原文：**

Petri has been part of our alignment assessment for every Claude model since Claude Sonnet 4.5. It compares how the new model behaves across a range of alignment-relevant scenarios that are simulated by a separate "auditor" model. A further "judge" model then scores the resulting transcripts for misaligned behaviors.

**中文翻译：**

自 Claude Sonnet 4.5 以来，Petri 已成为每个 Claude 模型对齐评估的一部分。它通过一个独立的"审计员"模型模拟一系列对齐相关场景，比较新模型在各场景中的行为表现。再由一个"评判员"模型对生成的对话记录进行评分，检测不对齐行为。

---

**英文原文：**

We've been pleased to see Petri being used by external organizations: for example, the UK's AI Security Institute (AISI) made it a major part of how they evaluate models for their propensity to sabotage AI research.

**中文翻译：**

我们很高兴看到外部组织也在使用 Petri：例如，英国 AI 安全研究院（AISI）将其作为评估模型破坏 AI 研究倾向的主要工具。

---

**英文原文：**

We're now updating Petri to its third version. Here are some of the biggest changes:

- **Adaptability.** Petri 3.0 involves major architectural changes that allow users to adapt it to more uses, in particular by splitting the auditor model and the target model into separate components that can be tweaked separately.
- **Realism.** Despite the fact that alignment researchers try to make tests appear realistic, a model can often deduce from various artificialities in the setup that it's actually part of a test. An add-on to Petri, which we're calling "Dish," makes the setup far more realistic.
- **Depth.** We've now integrated Petri with our other open-source alignment tool, Bloom, which can perform much more in-depth assessments of specific chosen behaviors.

**中文翻译：**

我们正在将 Petri 更新至第三版。以下是一些主要变化：

- **适应性。** Petri 3.0 包含重大架构变更，允许用户将其适配到更多场景，特别是将审计员模型和目标模型拆分为可独立调整的独立组件。
- **真实性。** 尽管对齐研究人员试图让测试看起来真实，但模型往往能通过设置中的各种人工痕迹推断出自己正在接受测试。我们为 Petri 开发了一个名为"Dish"的附加组件，使设置变得更加真实。
- **深度。** 我们现已将 Petri 与另一个开源对齐工具 Bloom 集成，后者能对特定选定行为进行更深入的评估。

---

**英文原文：**

We're also giving Petri a new home. We have handed over its development to Meridian Labs, an AI evaluation nonprofit. This move—similar to when we donated the Model Context Protocol (MCP) to the Linux Foundation—will help ensure that Petri remains independent of any AI lab, so that its results will be seen as neutral and credible by those across the industry and beyond.

**中文翻译：**

我们还为 Petri 找到了一个新归属。我们已将其开发工作移交给 AI 评估非营利组织 Meridian Labs。此举类似于我们此前将模型上下文协议（MCP）捐赠给 Linux 基金会，将有助于确保 Petri 独立于任何 AI 实验室，使整个行业及更广泛领域认为其结果是中立和可信的。

---

**英文原文：**

As part of Meridian Labs, Petri joins other tools like Inspect and Scout, building a technology stack that is open to labs, independent researchers, and governments alike, at a time when reliable tests of AI model behavior matter more than ever.

**中文翻译：**

作为 Meridian Labs 的一部分，Petri 与其他工具（如 Inspect 和 Scout）并肩工作，构建了一个对实验室、独立研究人员和政府均开放的技术栈。在 AI 模型行为可靠测试比以往任何时候都更重要的时代，这是一个重要的进步。
