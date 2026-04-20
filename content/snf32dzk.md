# LLM-Powered GUI Agents in Phone Automation: Surveying Progress and Prospects

> 原文链接: https://www.preprints.org/manuscript/202501.0413/v1

---

# LLM-Powered GUI Agents in Phone Automation: Surveying Progress and Prospects

> 原文链接: https://www.preprints.org/manuscript/202501.0413/v1

---
Version 1

Submitted:

05 January 2025

Posted:

06 January 2025

You are already at the latest version

######

Abstract

With the rapid rise of large language models (LLMs), phone automation has undergone transformative changes. This paper systematically reviews LLM-driven phone GUI agents, highlighting their evolution from script-based automation to intelligent, adaptive systems. We first contextualize key challenges, (i) limited generality, (ii) high maintenance overhead, and (iii) weak intent comprehension, and show how LLMs address these issues through advanced language understanding, multimodal perception, and robust decision-making. We then propose a taxonomy covering fundamental agent frameworks (single-agent, multi-agent, plan-then-act), modeling approaches (prompt engineering, training-based), and essential datasets and benchmarks. Furthermore, we detail task-specific architectures, supervised fine-tuning, and reinforcement learning strategies that bridge user intent and GUI operations. Finally, we discuss open challenges such as dataset diversity, on-device deployment efficiency, user-centric adaptation, and security concerns, offering forward-looking insights into this rapidly evolving field. By providing a structured overview and identifying pressing research gaps, this paper serves as a definitive reference for researchers and practitioners seeking to harness LLMs in designing scalable, user-friendly phone GUI agents. Project Homepage: github.com/PhoneLLM/Awesome-LLM-Powered-Phone-GUI-Agents

###### Keywords:

phone automation

;  large language models

;  GUI agents

;  traditional methods

;  LLMs in phone automation

;  frameworks

;  perception

;  brain

;  action

;  multi-agent framework

;  Plan-Then-Act Framework

;  prompt engineering

;  training-based methods

;  datasets

;  benchmarks

;  challenges

;

future directions

######

Subject:

[Computer Science and Mathematics](/subject/browse/computer-science-and-mathematics)  -   [Artificial Intelligence and Machine Learning](/subject/browse/computer-science-and-mathematics/artificial-intelligence-and-machine-learning)

## 1\. Introduction

The core of phone GUI automation is to simulate human interactions with phone interfaces programmatically, thereby accomplishing a series of complex tasks. Phone automation is widely applied in areas such as application testing and shortcut instructions, aiming to enhance operational efficiency or free up human resource Azim and Neamtiu (2013); Degott et al. (2019); Koroglu et al. (2018); Li et al. (2019); Pan et al. (2020). Traditional phone automation often relies on predefined scripts and templates, which, while effective, tend to be rigid and inflexible when facing complex and variable user interfaces and dynamic environment Arnatovich and Wang (2018); Deshmukh et al. (2023); Nass (2024); Nass et al. (2021); Tramontana et al. (2019). These methods can be viewed as early forms of agents, designed to perform specific tasks in a predetermined manner.

An agent, in the context of computer science and artificial intelligence, is an entity that perceives its environment through sensors and acts upon that environment through actuators to achieve specific goals Guo et al. (2024); Jin et al. (2024); Li et al. (2024c); Wang et al. (2024c). Agents can range from simple scripts that execute fixed sequences of actions to complex systems capable of learning, reasoning, and adapting to new situations Huang et al. (2024); Jin et al. (2024); Wang et al. (2024c). Traditional agents in phone automation are limited by their reliance on static scripts and lack of adaptability, making it challenging for them to handle the dynamic and complex nature of modern mobile interfaces.

Building intelligent autonomous agents with abilities in task planning, decision-making, and action execution has been a long-term goal of artificial intelligence Albrecht and Stone (2018). As artificial intelligence technologies have advanced, the development of agents has progressed from these traditional agents Anscombe (2000); Dennett (1988); Shoham (1993) to AI agents Gao et al. (2018); Inkster et al. (2018); Poole and Mackworth (2010) that incorporate machine learning and decision-making capabilities. These AI agents can learn from data, make decisions based on probabilistic models, and adapt to changes in the environment to some extent. However, they still face limitations in understanding complex user instructions Amershi et al. (2014); Luger and Sellen (2016) and managing highly dynamic environment Christiano et al. (2017); Köhl et al. (2019).

With the rapid development of LLMs like the GPT series Achiam et al. (2023); Brown (2020); Radford (2018a); Radford et al. (2019), agents based on these models have exhibited powerful capabilities in numerous fields Boiko et al. (2023); Dasgupta et al. (2023); Dong et al. (2024); Hong et al. (2023); Li et al. (2023a); Park et al. (2023); Qian et al. (2023, 2024a); Wang et al. (2023c); Xia et al. (2023). As illustrated in [Figure 1](#preprints-145259-f001), there are key differences between conversational LLMs and LLM-based agents. While conversational LLMs primarily focus on understanding and generating human language—engaging in dialogue, answering questions, summarizing information, and translating language—LLM-based agents extend beyond these capabilities by integrating perception and action components. This integration enables them to interact with the external environment through multimodal inputs, such as visual data from user interfaces, and perform actions that alter environmental states Hong et al. (2023); Qian et al. (2024a); Wang et al. (2023c). By combining perception, reasoning, and action, these agents can parse intricate instructions, formulate operational commands, and autonomously perform highly complex tasks, bridging the gap between language understanding and real-world interactions Guo et al. (2024); Li et al. (2024c); Xi et al. (2023).

Applying LLM-based agents to phone automation has brought a new paradigm to traditional automation, making operations on phone interfaces more intelligent Hong et al. (2024); Song et al. (2023b); Zhang et al. (2023a); Zheng et al. (2024). **LLM-powered phone GUI agents are intelligent systems that leverage large language models to understand, plan, and execute tasks on mobile devices by integrating natural language processing, multimodal perception, and action execution capabilities.** On smartphones, these agents can recognize and analyze user interfaces, understand natural language instructions, perceive interface changes in real time, and respond dynamically. Unlike traditional script-based automation that relies on coding fixed operation paths, these agents can autonomously plan complex task sequences through multimodal processing of language instructions and interface information. They have strong adaptability and flexible pathways, greatly improving user experience by understanding human intentions, performing complex long-chain planning, and executing tasks automatically, thereby improving efficiency in a wide range of scenarios, including not only phone automated testing but also executing complex tasks such as configuring intricate phone settings Wen et al. (2024), navigating maps Wang et al. (2024a,b), and facilitating online shopping Zhang et al. (2023a).

Clarifying the development trajectory of phone GUI agents is crucial. On one hand, with the support of large language models Achiam et al. (2023); Brown (2020); Radford (2018a); Radford et al. (2019), phone GUI agents can significantly enhance the efficiency of phone automation scenarios, making operations more intelligent and no longer limited to coding fixed operation paths. This enhancement not only optimizes phone automation processes but also expands the application scope of automation. On the other hand, phone GUI agents can understand and execute complex natural language instructions, transforming human intentions into specific operations such as automatically scheduling appointments, booking restaurants, summoning transportation, and even achieving functionalities similar to autonomous driving in advanced automation. These capabilities demonstrate the potential of phone GUI agents in executing complex tasks, providing convenience to users and laying practical foundations for AI development.

With the increasing research on large language models in phone automation Liu et al. (2024c); Lu et al. (2024b); Wang et al. (2024a,b); Wen et al. (2024, 2023); Zhang et al. (2024b), the research community’s attention to this field has grown rapidly. However, there is still a lack of dedicated systematic surveys in this area, especially comprehensive explorations of phone automation from the perspective of large language models. Given the importance of phone GUI agents, the purpose of this paper is to fill this gap by systematically summarizing current research achievements, reviewing relevant literature, analyzing the application status of large language models in phone automation, and pointing out directions for future research.

To provide a comprehensive overview of the current state and future prospects of LLM-Powered GUI Agents in Phone Automation, we present a taxonomy that categorizes the field into three main areas: Frameworks of LLM-powered phone GUI agents, Large Language Models for Phone Automation, and Datasets and Evaluation Methods [Figure 2](#preprints-145259-f002). This taxonomy highlights the diversity and complexity of the field, as well as the interdisciplinary nature of the research involved.

Unlike previous literature reviews, which primarily focus on traditional phone automated testing methods, most existing surveys emphasize manual scripting or rule-based automation approaches without leveraging LLMs Arnatovich and Wang (2018); Deshmukh et al. (2023); Nass (2024); Nass et al. (2021); Tramontana et al. (2019). These traditional methods face significant challenges in coping with dynamic changes, complex user interfaces, and the scalability required for modern applications. Although recent surveys have explored broader areas of multimodal agents and foundation models for GUI automation, such as Foundations and Recent Trends in Multimodal Mobile Agents: A Survey Wu et al. (2024), GUI Agents with Foundation Models: A Comprehensive Survey Wang et al. (2024f), and Large Language Model-Brained GUI Agents: A Survey Zhang et al. (2024a), these works primarily cover general GUI-based automation and multimodal applications.

However, a dedicated and focused survey on the role of large language models in phone GUI automation remains absent in the existing literature. This paper addresses the above-mentioned gap by systematically reviewing the latest developments, challenges, and opportunities in LLM-powered phone GUI agents, thereby offering a more targeted exploration of this emerging domain. Our main contributions can be summarized as follows:

-   **A Comprehensive and Systematic Survey of LLM-Powered Phone GUI Agents.** We provide an in-depth and structured overview of recent literature on LLM-powered phone automation, examining its developmental trajectory, core technologies, and real-world application scenarios. By comparing LLM-driven methods to traditional phone automation approaches, this survey clarifies how large models transform GUI-based tasks and enable more intelligent, adaptive interaction paradigms.

-   **Methodological Framework from Multiple Perspectives.** Leveraging insights from existing studies, we propose a unified methodology for designing LLM-driven phone GUI agents. This encompasses framework design (e.g., single-agent vs. multi-agent vs. plan-then-act frameworks), LLM model selection and training (prompt engineering vs. training-based methods), data collection and preparation strategies (GUI-specific datasets and annotations), and evaluation protocols (benchmarks and metrics). Our systematic taxonomy and method-oriented discussion serve as practical guidelines for both academic and industrial practitioners.

-   **In-Depth Analysis of Why LLMs Empower Phone Automation.** We delve into the fundamental reasons behind LLMs’ capacity to enhance phone automation. By detailing their advancements in natural language comprehension, multimodal grounding, reasoning, and decision-making, we illustrate how LLMs bridge the gap between user intent and GUI actions. This analysis elucidates the critical role of large models in tackling issues of scalability, adaptability, and human-like interaction in real-world mobile environment.

-   **Insights into Latest Developments, Datasets, and Benchmarks.** We introduce and evaluate the most recent progress in the field, highlighting innovative datasets that capture the complexity of modern GUIs and benchmarks that allow reliable performance assessment. These resources form the backbone of LLM-based phone automation, enabling systematic training, fair evaluation, and transparent comparisons across different agent designs.

-   **Identification of Key Challenges and Novel Perspectives for Future Research.** Beyond discussing mainstream hurdles (e.g., dataset coverage, on-device constraints, reliability), we propose forward-looking viewpoints on user-centric adaptations, security and privacy considerations, long-horizon planning, and multi-agent coordination. These novel perspectives shed light on how researchers and developers might advance the current state of the art toward more robust, secure, and personalized phone GUI agents.

By addressing these aspects, our survey not only provides an up-to-date map of LLM-powered phone GUI automation but also offers a clear roadmap for future exploration. We hope this work will guide researchers in identifying pressing open problems and inform practitioners about promising directions to harness LLMs in designing efficient, adaptive, and user-friendly phone GUI agents.

## 2\. Development of Phone Automation

The evolution of phone automation has been marked by significant technological advancements Kong et al. (2018), particularly with the emergence of LLMs Achiam et al. (2023); Brown (2020); Radford (2018a); Radford et al. (2019). This section explores the historical development of phone automation, the challenges faced by traditional methods, and how LLMs have revolutionized the field.

#### 2.1. Phone Automation Before the LLM Era

Before the advent of LLMs, phone automation was predominantly achieved through traditional technical methods Amalfitano et al. (2014); Azim and Neamtiu (2013); Kirubakaran and Karthikeyani (2013); Kong et al. (2018); Linares-Vásquez et al. (2017); Zhao et al. (2024). This subsection delves into the primary areas of research and application during that period, including automation testing, shortcuts, a

...（正文已截断，原文长度：217301字符）