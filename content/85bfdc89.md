# Anthropic 开源对齐工具 Petri 捐赠给 Meridian Labs，继续独立发展

> 原文：[Anthropic - Donating our open-source alignment tool](https://www.anthropic.com/research/donating-open-source-petri) | 评分：4

## 原文 / English

In October 2025, Anthropic launched Petri, an open-source toolbox of alignment tests that can be applied to any large language model. Petri was developed as part of the Anthropic Fellows program and can be used to rapidly and easily test AI models for concerning tendencies like deception, sycophancy, and cooperation with harmful requests.

### How Petri Works

Petri has been part of Anthropic's alignment assessment for every Claude model since Claude Sonnet 4.5. It compares how the new model behaves across a range of alignment-relevant scenarios simulated by a separate "auditor" model. A further "judge" model then scores the resulting transcripts for misaligned behaviors.

### Petri 3.0 Updates

**Adaptability**
Petri 3.0 involves major architectural changes that allow users to adapt it to more uses, by splitting the auditor model and the target model into separate components that can be tweaked separately.

**Realism**
An add-on called "Dish" makes the setup far more realistic—for example, by running the tests using the model's real system prompt and the real "scaffold" that would be used in genuine model deployments.

**Depth**
Petri has been integrated with Anthropic's other open-source alignment tool, Bloom, which can perform much more in-depth assessments of specific chosen behaviors.

### New Home: Meridian Labs

Anthropic has handed over Petri's development to Meridian Labs, an AI evaluation nonprofit. This move is similar to when Anthropic donated the Model Context Protocol (MCP) to the Linux Foundation. As part of Meridian Labs, Petri joins other tools like Inspect and Scout, building a technology stack open to labs, independent researchers, and governments alike.

Petri is also being used by the UK's AI Security Institute (AISI), which made it a major part of how they evaluate models for their propensity to sabotage AI research.

---

## 中文

2025 年 10 月，Anthropic 推出了 Petri，这是一套可应用于任何大型语言模型的开源对齐测试工具箱。Petri 作为 Anthropic Fellows 计划的成果，可用于快速简便地测试 AI 模型的欺骗性、谄媚性和配合有害请求等令人担忧的倾向。

### Petri 工作原理

自 Claude Sonnet 4.5 以来，Petri 一直是 Anthropic 每版 Claude 模型对齐评估的组成部分。它通过一个独立的"审计员"模型模拟一系列与对齐相关的场景，比较新模型在各场景中的行为表现。再由一个"裁判"模型对生成的对话记录评分，识别错位行为。

### Petri 3.0 更新

**适应性**
Petri 3.0 进行了重大架构调整，允许用户更灵活地适配多种用途——将审计员模型和目标模型拆分为独立组件，可分别微调。

**真实性**
一个名为"Dish"的插件大幅提升了测试的真实感，例如使用模型真实的系统提示词和真实部署中使用的"脚手架"（scaffold）来运行测试。

**深度**
Petri 已与 Anthropic 另一开源对齐工具 Bloom 集成，后者可对特定选定行为进行更深入细致的评估。

### 新归宿：Meridian Labs

Anthropic 已将 Petri 的开发工作移交给 AI 评估非营利组织 Meridian Labs。此举类似于此前 Anthropic 将模型上下文协议（MCP）捐赠给 Linux 基金会。在 Meridian Labs 旗下，Petri 与 Inspect、Scout 等工具并肩，共同构建面向实验室、独立研究人员和政府机构的开放技术栈。

Petri 同时也被英国 AI 安全研究院（AISI）采用，作为评估模型破坏 AI 研究倾向的主要工具。

---
*来源：[Anthropic - Donating our open-source alignment tool](https://www.anthropic.com/research/donating-open-source-petri) | 工具：Petri 3.0 / Meridian Labs*
