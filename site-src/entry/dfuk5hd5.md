---
title: 'Chain-of-Tools - 在冻结 LLM 的 CoT 推理中利用海量未见工具'
sidebar: false
---

::: info
[← 返回学习资源](/learning)
:::

# Chain-of-Tools - 在冻结 LLM 的 CoT 推理中利用海量未见工具

> LLM 推理能力增强的新方法

🔗 [原文链接](https://arxiv.org/pdf/2503.16779) | 🇨🇳 | ⭐⭐⭐⭐⭐ 5 ⭐5 5/5 📅 2026-03-13

`fine-tuning` `coding` `agent` `tool-use` `llm` `paper` `reinforcement-learning` `reasoning`

---

## Chain-of-Tools: 在冻结 LLM 的 CoT 推理中利用海量未见工具

### 中文

**标题**: Chain-of-Tools: 在冻结 LLM 的 CoT 推理中利用海量未见工具

**作者**: MengsongWu, TongZhu, HanHan, XiangZhang, WenbiaoShao, WenliangChen
**机构**: 苏州大学，苏州市学士街1号，215006
**邮箱**: {mswumsw,tzhu7,hhan,xzhangxzhang23,wbshao}@stu.suda.edu.cn, wlchen@suda.edu.cn

**摘要**：
为LLM代理配备外部工具是一个合理的解决方案。这就是工具学习（Tool Learning）任务要研究的问题：如何让LLM更好地在推理过程中使用工具？工具学习可以进一步拓展大型语言模型（LLMs）的使用场景。然而，大多数现有方法要么需要微调模型，使其只能使用训练数据中看到的工具，要么将工具演示添加到提示中，效率较低。

在本文中，我们提出了一种新的工具学习方法Chain-of-Tools。它充分利用了冻结语言模型的强大语义表征能力来完成工具调用。Chain-of-Tools在包含海量未见工具的大型灵活工具池中进行CoT推理。特别是，为了验证我们在大规模未见工具场景中的方法有效性，我们构建了一个新的数据集SimpleToolQuestions。我们在两个数值推理基准（GSM8K-XL和FuncQA）和两个知识问答基准（KAMEL和SimpleToolQuestions）上进行了实验。实验结果表明，我们的方法优于基线方法。我们还识别出模型输出中对于工具选择至关重要的维度，增强了模型的可解释性。

### English

**Title**: Chain-of-Tools: Utilizing Massive Unseen Tools in the CoT Reasoning of Frozen Language Models

**Authors**: MengsongWu, TongZhu, HanHan, XiangZhang, WenbiaoShao, WenliangChen
**Affiliation**: SoochowUniversity,ShiziStreet1,215006Suzhou,China
**Email**: {mswumsw,tzhu7,hhan,xzhangxzhang23,wbshao}@stu.suda.edu.cn, wlchen@suda.edu.cn

**Abstract**:
Equipping LLM agents with external tools is a reasonable solution. That's what the Tool Learning (Qin et al., 2023a) task investigates: how to make LLMs better utilize tools in the process of reasoning? Tool learning can further broaden the usage scenarios of large language models (LLMs). However, most of the existing methods either need to finetune that the model can only use tools seen in the training data, or add tool demonstrations into the prompt with lower efficiency.

In this paper, we present a new Tool Learning method Chain-of-Tools. It makes full use of the powerful semantic representation capability of frozen LLMs to finish tool calling in the input CoT reasoning with a huge and flexible tool pool which may contain unseen tools. Especially, to validate the effectiveness of our approach in the massive unseen tool scenario, we construct a new dataset SimpleToolQuestions. We conduct experiments on two numerical reasoning benchmarks (GSM8K-XL and FuncQA) and two knowledge-based question answering benchmarks (KAMEL and SimpleToolQuestions). Experimental results show that our approach performs better than the baseline. We also identify dimensions of the model output that are critical in tool selection, enhancing the model interpretability.

---

## 1. 引言

### 中文

自主智能体系统的发展（Wang et al., 2024; Xi et al., 2023），由大型语言模型（LLMs）的实际应用推动（Achiam et al., 2023），已成为学术界和工业界的热门焦点。得益于LLM的涌现能力（Wei et al., 2022a; Zhao et al., 2023），能够全面综合地思考问题，LLM代理在多轮对话中可能会给出出色的分步解决方案。尽管LLM擅长逻辑推理和分解问题，但它无法完成许多特定任务，如计算数学公式或绘画。为了扩展应用场景，为LLM代理配备外部工具是一个合理的解决方案。这就是工具学习（Tool Learning）（Qin et al., 2023a）任务要研究的问题：如何让LLM更好地在推理过程中使用工具？

工具学习可以进一步拓展大型语言模型（LLMs）的使用场景。然而，大多数现有方法要么需要微调模型，使其只能使用训练数据中看到的工具，要么将工具演示添加到提示中，效率较低。ToolkenGPT（Hao et al., 2024）引入了一种方法，它只微调额外的工具令牌嵌入，而不损害原始模型，但它仍然无法使用未见工具。

基于上下文学习的工具学习：上下文学习（Brownetal.,2020）是LLMs最突出的能力之一。在ICL的帮助下，模型在许多任务的少样本场景中的性能得到了显著提升。ICL已成为LLMs广泛使用的基本技巧。

### English

### 1. Introduction

The development of autonomous agent systems (Wang et al., 2024; Xi et al., 2023), propelled by real-world applications (Achiam et al., 2023) of Large Language Models (LLMs), has become a popular focus in both academic and industry communities. Benefit from LLM's emergent ability (Wei et al., 2022a; Zhao et al., 2023) to think questions comprehensively and integratedly, LLM agent may give brilliant step-by-step solutions during multiple-turn chat with users. DespiteLLM is expert in logical reasoning and breaking down problems, it can't accomplish a lot of specific tasks like calculating math formulas or drawing paintings. In order to extend the application scenarios, equip LLM agent with external tools is a reasonable solution. That's what the Tool Learning (Qin et al., 2023a) task investigates: how to make LLMs better utilize tools in the process of reasoning?

Tool learning can further broaden the usage scenarios of large language models (LLMs). However, most of the existing methods either need to finetune that the model can only use tools seen in the training data, or add tool demonstrations into the prompt with lower efficiency. ToolkenGPT (Hao et al., 2024) introduces a method which only fine-tunes extra tool-token embeddings without hurting the original model, but it still can't use unseen tools.

In-Context Learning based Tool Learning: In-context learning (Brown et al., 2020) is one of the most prominent capabilities of the LLMs. With the help of ICL, the model performance in the few-shot scenario of many tasks has improved dramatically. ICL has become a basic trick in the wide usage of LLMs.
