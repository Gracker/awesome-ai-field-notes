---
title: 'Waza：AI 时代工程师的 8 个核心技能工具集'
sidebar: false
---

::: info
[← 返回AI编程](/coding)
:::

# Waza：AI 时代工程师的 8 个核心技能工具集

> 一套面向 AI 时代工程师的 8 技能工具集，覆盖思考到维护全流程

🔗 [原文链接](https://x.com/HiTw93/status/2041053321851789629) | @HiTw93 | 🇨🇳 | ⭐⭐⭐⭐ 4 ⭐4 4/5 📅 2026-04-06

`openclaw` `skills` `agent` `engineering` `workflow` `context-engineering`

---

# Waza：AI 时代工程师的 8 个核心技能工具集

## 基本信息
- **ID**: 7n5hkzn5
- **来源**: x (HiTw93)
- **原始日期**: 2026-04-06
- **分类**: coding
- **标签**: openclaw, skills, agent, engineering, workflow, context-engineering
- **质量评分**: 4

---

## English

WORKING PAPER

GPTs are GPTs: An Early Look at the Labor Market Impact Potential
of Large Language Models

arXiv:2303.10130v5 [econ.GN] 21 Aug 2023

Tyna Eloundou1 , Sam Manning1,2 , Pamela Mishkin∗1 , and Daniel Rock3
1 OpenAI
2 OpenResearch
3 University of Pennsylvania

August 22, 2023

Abstract
We investigate the potential implications of large language models (LLMs), such as Generative Pretrained Transformers (GPTs), on the U.S. labor market, focusing on the increased capabilities arising from
LLM-powered software compared to LLMs on their own. Using a new rubric, we assess occupations based
on their alignment with LLM capabilities, integrating both human expertise and GPT-4 classifications.
Our findings reveal that around 80% of the U.S. workforce could have at least 10% of their work tasks
affected by the introduction of LLMs, while approximately 19% of workers may see at least 50% of their
tasks impacted. We do not make predictions about the development or adoption timeline of such LLMs.
The projected effects span all wage levels, with higher-income jobs potentially facing greater exposure to
LLM capabilities and LLM-powered software. Significantly, these impacts are not restricted to industries
with higher recent productivity growth. Our analysis suggests that, with access to an LLM, about 15%
of all worker tasks in the US could be completed significantly faster at the same level of quality. When
incorporating software and tooling built on top of LLMs, this share increases to between 47 and 56%
of all tasks. This finding implies that LLM-powered software will have a substantial effect on scaling
the economic impacts of the underlying models. We conclude that LLMs such as GPTs exhibit traits of
general-purpose technologies, indicating that they could have considerable economic, social, and policy
implications.

1

Introduction

As shown in Figure 1, recent years, months, and weeks have seen remarkable progress in the field of generative
AI and large language models (LLMs). While the public often associates LLMs with various iterations of the
Generative Pre-trained Transformer (GPT), LLMs can be trained using a range of architectures, and are not
limited to transformer-based models (Devlin et al., 2019). LLMs can process and produce various forms of
sequential data, including assembly language, protein sequences and chess games, extending beyond natural
language applications alone. In this paper, we use LLMs and GPTs somewhat interchangeably, and specify in
our rubric that these should be considered similar to the GPT-family of models available via ChatGPT or
the OpenAI Playground (which at the time of labeling included models in the GPT-3.5 family but not in the
GPT-4 family). We examine LLMs with text- and code-generating abilities, use the term "generative AI" to
additionally include modalities such as images or audio, and use "LLM-powered software" to cover tools built
on top of LLMs or that combine LLMs with other generative AI models.
∗ Corresponding author (pamela@openai.com). Authors contributed equally and are listed alphabetically.

WORKING PAPER

Figure 1: Taken directly from GPT-4 Technical Report (OpenAI, 2023b). To get a sense of how quickly
model capabilities are progressing – consider the jump in exam performance between GPT-3.5 and GPT-4
(OpenAI, 2023b).
Our study is motivated less by the progress of these models alone though, and more by the breadth,
scale, and capabilities we’ve seen in the complementary technologies developed around them. The role of
complementary technologies remains to be seen, but maximizing the impact of LLMs appears contingent
on integrating them with larger systems (Bresnahan, 2019; Agrawal et al., 2021). While the focus of our
discussion is primarily on the generative capabilities of LLMs, it is important to note that these models can
also be utilized for various tasks beyond text generation. For example, embeddings from LLMs can be used
for custom search applications, and LLMs can perform tasks such as summarization and classification where
the context may be largely contained in the prompt.
To complement predictions of technology’s impacts on work and provide a framework for understanding
the evolving landscape of language models and their associated technologies, we propose a new rubric
for assessing LLM capabilities and their potential effects on jobs. This rubric (A.1) measures the overall
exposure of tasks to LLMs, following the spirit of prior work on quantifying exposure to machine learning
(Brynjolfsson et al., 2018; Felten et al., 2018; Webb, 2020). We define exposure as a proxy for potential
economic impact without distinguishing between labor-augmenting or labor-displacing effects. We employ
human annotators and GPT-4 itself as a classifier to apply this rubric to occupational data in the U.S. economy,
primarily sourced from the O*NET database.1 2
To construct our primary exposure dataset, we collected both human annotations and GPT-4 classifications,
using a prompt tuned for agreement with a sample of labels from the authors. We observe similar agreement
1This is distinct from recent social science research that makes use of LLMs to simulate human behavior (Horton, 2023; Sorensen
et al., 2022)
2While our exposure rubric does not necessarily tie the concept of language models to any particular model, we were strongly
motivated by our observed capabilities of GPT-4 and the suite of capabilities we saw in development with OpenAI’s launch partners
(OpenAI, 2023b).

WORKING PAPER

levels in GPT-4 responses and between human and machine evaluations, when aggregated to the task level.
This exposure measure reflects an estimate of the technical capacity to make human labor more efficient;
however, social, economic, regulatory, and other determinants imply that technical feasibility does not
guarantee labor productivity or automation outcomes. Our analysis indicates that approximately 19% of jobs
have at least 50% of their tasks exposed when considering both current model capabilities and anticipated
tools built upon them. Human assessments suggest that only 3% of U.S. workers have over half of their tasks
exposed to LLMs when considering existing language and code capabilities without additional software or
modalities. Accounting for other generative models and complementary technologies, our human estimates
indicate that up to 49% of workers could have half or more of their tasks exposed to LLMs.
Our findings consistently show across both human and GPT-4 annotations that most occupations exhibit
some degree of exposure to LLMs, with varying exposure levels across different types of work. Occupations
with higher wages generally present with higher exposure, a result contrary to similar evaluations of overall
exposure to machine learning (Brynjolfsson et al., 2023). When regressing exposure measures on skillsets
using O*NET’s skill rubric, we discover that roles heavily reliant on science and critical thinking skills show
a negative correlation with exposure, while programming and writing skills are positively associated with
LLM exposure. Following Autor et al. (2022a), we examine barriers to entry by "Job Zones" and find that
occupational exposure to LLMs weakly increases with the difficulty of job preparation. In other words,
workers facing higher (lower) barriers to entry in their jobs tend to experience more (less) exposure to LLMs.
We further compare our measurements to previous efforts documenting the distribution of automation
exposure in the economy and find broadly consistent results. Most other technology exposure measures we
examine are statistically significantly correlated with our preferred exposure measure, while measures of
manual routineness and robotics exposure show negative correlations. The variance explained by these earlier
efforts (Acemoglu and Autor, 2011a; Frey and Osborne, 2017; Brynjolfsson et al., 2018; Felten et al., 2018;
Webb, 2020; Brynjolfsson et al., 2023), along with wage controls, ranges from 60 to 72%, indicating that 28
to 40% of the variation in our AI exposure measure remains unaccounted for by previous technology exposure
measurements.
We analyze exposure by industry and discover that information processing industries (4-digit NAICS)
exhibit high exposure, while manufacturing, agriculture, and mining demonstrate lower exposure. The
connection between productivity growth in the past decade and overall LLM exposure appears weak, suggesting
a potential optimistic case that future productivity gains from LLMs may not exacerbate possible cost disease
effects (Baumol, 2012; Aghion et al., 2018). 3
Our analysis indicates that the impacts of LLMs like GPT-4, are likely to be pervasive. While LLMs
have consistently improved in capabilities over time, their growing economic effect is expected to persist and
increase even if we halt the development of new capabilities today. We also find that the potential impact of
LLMs expands significantly when we take into account the development of complementary technologies.
Collectively, these characteristics imply that Generative Pre-trained Transformers (GPTs) are general-purpose
technologies (GPTs).4 (Bresnahan and Trajtenberg, 1995; Lipsey et al., 2005).
(Goldfarb et al., 2023) argue that machine learning as a broad category is likely a general-purpose
technology. Our evidence supports a wider impact, as even subsets of machine learning software meet the
criteria for general-purpose technology status independently. This paper’s primary contributions are to provide
a set of measurements of LLM impact potential and to demonstrate the use case of applying LLMs to develop
such measurements efficiently and at scale. Additionally, we showcase the general-purpose potential of LLMs.
If "GPTs are GPTs," the eventual trajectory of LLM development and application may be challenging for
3Baumol’s cost disease is a theory that explains why the cost of labor-intensive services, such as healthcare and education,
increases over time. This happens because wages for skilled workers in other industries increase, but there is no corresponding
increase in productivity or efficiency in these service industries. Therefore, the cost of labor in these industries becomes relatively
more expensive compared to other goods and services in the economy.
4For the remainder of the paper we spell out general-purpose technologies when it is used outside of stating "GPTs are GPTs."

WORKING PAPER

policymakers to predict and regulate. As with other general-purpose technologies, much of these algorithms’
potential will emerge across a broad range of economically valuable use cases, including the creation of new
types of work (Acemoglu and Restrepo, 2018; Autor et al., 2022a). Our research serves to measure what is
technically feasible now, but necessarily will miss the evolving impact potential of the LLMs over time.
The paper is structured as follows: Section 2 reviews relevant prior work, Section 3 discusses methods
and data collection, Section 4 presents summary statistics and results, Section 5 relates our measurements to
earlier efforts, Section 6 discusses the results, and Section 7 offers concluding remarks.

2

Literature Review

2.1

The Advancement of Large Language Models

In recent years, generative AI models have gained significant attention from both the artificial intelligence
(AI) research community and the general public, due to their ability to tackle a wide array of complex
language-based tasks. The progress in these models’ abilities has been fueled by multiple factors, including
increased model parameter count, greater training data volume, and enhanced training configurations (Brown
et al., 2020; Radford et al., 2019; Hernandez et al., 2021; Kaplan et al., 2020). Broad, state-of-the-art LLMs,
such as LaMDA (Thoppilan et al., 2022) and GPT-4 (OpenAI, 2023b), excel in diverse applications like
translation, classification, creative writing, and code generation—capabilities that previously demanded
specialized, task-specific models developed by expert engineers using domain-specific data.
Concurrently, researchers have improved the steerability, reliability, and utility of these models using
methods like fine-tuning and reinforcement learning with human feedback (Ouyang et al., 2022; Bai et al.,
2022). These advancements enhance the models’ ability to discern user intent, rendering them more
user-friendly and practical. Moreover, recent studies reveal the potential of LLMs to program and control
other digital tools, such as APIs, search engines, and even other generative AI systems (Schick et al., 2023;
Mialon et al., 2023; Chase, 2022). This enables seamless integration of individual components for better
utility, performance, and generalization. At their limit, these trends suggest a world where LLMs may be
capable of executing any task typically performed at a computer.
Generative AI models have mostly been deployed as modular specialists, performing specific tasks such as
generating images from captions or transcribing text from speech. However, we argue that it is essential to view
LLMs as versatile building blocks for creating additional tools. Developing these tools and integrating them
into systems will require time and possibly significant reconfiguration of existing processes across various
industries. Nevertheless, we are already witnessing emerging adoption trends. Despite their limitations,
LLMs are increasingly being integrated into specialized applications in fields like writing assistance, coding,
and legal research. These specialized applications then allow businesses and individuals to adopt LLMs into
their workflows.
We emphasize the significance of these complementary technologies, partly because out-of-the-box
general-purpose LLMs may continue to be unreliable for various tasks due to issues such as factual inaccuracies,
inherent biases, privacy concerns, and disinformation risks (Abid et al., 2021; Schramowski et al., 2022;
Goldstein et al., 2023; OpenAI, 2023a). However, specialized workflows—including tooling, software, or
human-in-the-loop systems—can help address these shortcomings by incorporating domain-specific expertise.
For example, Casetext offers LLM-based legal research tools that provide lawyers with quicker and more
accurate legal research results, utilizing embeddings and summarization to counter the risk that GPT-4 could
provide inaccurate details about a legal case or set of documents. GitHub Copilot is a coding assistant that
employs LLMs to generate code snippets and auto-complete code, which users can then accept or reject based
on their expertise. In other words, while it’s true that on its own GPT-4 does not "know what time it is," it’s
easy enough to give it a watch.

WORKING PAPER

Furthermore, a positive feedback loop may emerge as LLMs surpass a specific performance threshold,
allowing them to assist in building the very tooling that enhances their u

## 中文

（英文原文已提供，完整翻译需要人工处理）


---

*本文由 AI Field Notes 自动抓取并翻译整理*
