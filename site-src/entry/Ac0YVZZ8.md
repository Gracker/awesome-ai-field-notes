---
title: 'The 2025 AI Engineering Reading List'
sidebar: false
---

::: info
[← 返回学习资源](/learning)
:::

# The 2025 AI Engineering Reading List

> Cubox 收藏 — The 2025 AI Engineering Reading List

🔗 [原文链接](https://www.latent.space/p/2025-papers) | 🌐 | ⭐⭐⭐⭐ 4 ⭐4 4/5 📅 2025-01-04

---

# The 2025 AI Engineering Reading List

## English
The 2025 AI Engineer Reading List. We picked 50 paper/models/blogs across 10 fields in AI Eng: LLMs, Benchmarks, Prompting, RAG, Agents, CodeGen, Vision, Voice, Diffusion, Finetuning. If you're starting from scratch, start here.

## 中文
2025 年 AI 工程师阅读清单。我们在 AI 工程的 10 个领域中精选了 50 篇论文/模型/博客：LLM、基准测试、提示工程、RAG、Agent、代码生成、视觉、语音、扩散模型、微调。如果你从零开始，从这里起步。

## English
Discussions on X, LinkedIn, YouTube. Also: Meet AI Engineers in person! Applications closing soon for attending and sponsoring AI Engineer Summit NYC, Feb 20-21.

## 中文
讨论在 X、LinkedIn、YouTube 上进行。另外：面对面认识 AI 工程师！AI Engineer Summit NYC（2 月 20-21 日）的参会和赞助申请即将截止。

## English
The picks from all the speakers in our Best of 2024 series catches you up for 2024, but since we wrote about running Paper Clubs, we've been asked many times for a reading list to recommend for those starting from scratch at work or with friends. We started with the 2023 a16z Canon, but it needs a 2025 update and a practical focus.

## 中文
我们"2024 精选"系列中所有演讲者的推荐可以帮你补上 2024 年的课，但自从我们写了关于运行论文俱乐部的文章以来，很多人要求我们为那些在工作或与朋友一起从零开始学习的人推荐一份阅读清单。我们从 2023 年的 a16z 经典清单开始，但它需要更新到 2025 年并聚焦实用性。

## English
Here we curate "required reads" for the AI engineer. Our design goals are: pick ~50 papers (~one a week for a year), optional extras. Arbitrary constraint. tell you why this paper matters instead of just name drop without helpful context. Be very practical for the AI Engineer; no time wasted on Attention is All You Need, bc 1) everyone else already starts there, 2) most won't really need it at work.

## 中文
在这里我们为 AI 工程师策划了"必读清单"。我们的设计目标是：挑选约 50 篇论文（一年大约每周一篇），加上可选的额外阅读。这是一个人为的约束。告诉你为什么这篇论文重要，而不是仅仅列个名字却没有有用的上下文。对 AI 工程师来说要非常实用；不在《Attention is All You Need》上浪费时间，因为 1) 其他人已经从那里开始了，2) 大多数人在工作中并不真正需要它。

## English
We ended up picking 5 "papers" per section for:

## 中文
我们最终每个板块挑选了 5 篇"论文"：

## English
**Section 1: Frontier LLMs**
GPT1, GPT2, GPT3, Codex, InstructGPT, GPT4 papers. Self explanatory. GPT3.5, 4o, o1, o3, GPT4.5 have launch events and system cards instead.
Claude 3 / 4 and Gemini 1 / 2.5 to understand the leading labs. You should also know Claude 3.5 Sonnet and Gemini 2.0 Flash/Flash Thinking. Also Gemma 2 & 3 (you can read the PyTorch re-implementation).
LLaMA 1, Llama 2, Llama 3 papers to understand the leading open models. You can also view Mistral 7B, Mixtral and Pixtral as a branch on the Llama family tree. More recently China models have overtaken: Kimi K-2 and Qwen 3.
DeepSeek V1, Coder, Math (esp GRPO), MoE, V2, V3, R1 papers.
Post Training Survey Papers like this MBZUAI one, this one, and others.

## 中文
**第一部分：前沿 LLM**
GPT1、GPT2、GPT3、Codex、InstructGPT、GPT4 论文。不言自明。GPT3.5、4o、o1、o3、GPT4.5 有发布会和技术报告卡代替。
Claude 3/4 和 Gemini 1/2.5 来理解领先的实验室。你还应该了解 Claude 3.5 Sonnet 和 Gemini 2.0 Flash/Flash Thinking。以及 Gemma 2 & 3（可以阅读 PyTorch 重新实现）。
LLaMA 1、Llama 2、Llama 3 论文来理解领先的开源模型。你也可以将 Mistral 7B、Mixtral 和 Pixtral 视为 Llama 家族树上的一个分支。最近中国模型已经超越了：Kimi K-2 和 Qwen 3。
DeepSeek V1、Coder、Math（特别是 GRPO）、MoE、V2、V3、R1 论文。
后训练综述论文，如 MBZUAI 的这篇、这篇以及其他。

## English
You can both use and learn a lot from other LLMs, this is a vast topic. Bonus picks: In particular, BERTs are underrated as workhorse classification models - see ModernBERT / NeoBERT for the state of the art, and ColBERT for applications. (1.5hr video) Compare architectures of the various open models from Ahead of AI. Honorable mentions of LLMs to know: AI2 (Olmo, Molmo, OlmOE, Tülu 3, Olmo 2), Grok (esp Grok 3), Amazon Nova, Yi, Reka, Cohere, Nemotron, Microsoft Phi, HuggingFace SmolLM (esp SmolLM 3), Apple Intelligence - mostly lower in ranking or lack papers.

## 中文
你可以从其他 LLM 中同时使用和学习到很多东西，这是一个庞大的话题。额外推荐：特别是 BERT 作为分类模型的实用性被低估了——参见 ModernBERT/NeoBERT 了解最前沿，以及 ColBERT 的应用。（1.5 小时视频）Ahead of AI 对比各种开源模型的架构。值得了解的 LLM 荣誉提名：AI2（Olmo、Molmo、OlmOE、Tülu 3、Olmo 2）、Grok（特别是 Grok 3）、Amazon Nova、Yi、Reka、Cohere、Nemotron、Microsoft Phi、HuggingFace SmolLM（特别是 SmolLM 3）、Apple Intelligence——大多排名较低或缺乏论文。

## English
Research to know: If time allows, we recommend the Scaling Laws literature: Kaplan, Chinchilla, Emergence / Mirage, Post-Chinchilla laws. As of July 2025, Kimi K-2/Moonshot and Muon is also strongly recommended.

## 中文
需要了解的研究：如果时间允许，我们推荐缩放定律相关文献：Kaplan、Chinchilla、Emergence/Mirage、Post-Chinchilla laws。截至 2025 年 7 月，Kimi K-2/Moonshot 和 Muon 也强烈推荐。

## English
In 2025, the frontier (o1, o3, R1, QwQ/QVQ, f1) will be very much dominated by reasoning models, where Sebastian Raschka currently has the best literature review. The basic knowledge is Let's Verify Step By Step, s1, STaR (core to xAI), and Noam Brown's talks/podcasts. Most practical knowledge is accumulated by outsiders (LS talk) and tweets.

## 中文
在 2025 年，前沿模型（o1、o3、R1、QwQ/QVQ、f1）将很大程度由推理模型主导，Sebastian Raschka 目前有最好的文献综述。基础知识是 Let's Verify Step By Step、s1、STaR（xAI 的核心）以及 Noam Brown 的演讲/播客。大部分实用知识由外部人士积累（LS 演讲）和推文。

## English
**Section 2: Benchmarks and Evals**
MMLU paper - the main knowledge benchmark, next to GPQA and BIG-Bench. In 2025 frontier labs use MMLU Pro, GPQA Diamond, and BIG-Bench Hard.
MRCR paper - evaluating long context, used by OpenAI over MuSR, LongBench, BABILong, and RULER. Fixing the overused Needle in a Haystack.
MATH paper - a compilation of math competition problems. Frontier labs focus on FrontierMath, AMO and subsets of MATH: MATH level 5, AIME, AMC10/AMC12.
IFEval paper - the leading instruction following eval. See also Facebook's Multi-IF, COLLIE and Scale MultiChallenge, which has now overtaken MT-Bench.
ARC AGI challenge - a famous abstract reasoning "IQ test" benchmark that has lasted far longer than many quickly saturated benchmarks.

## 中文
**第二部分：基准测试与评估**
MMLU 论文——主要的知识基准，与 GPQA 和 BIG-Bench 并列。2025 年前沿实验室使用 MMLU Pro、GPQA Diamond 和 BIG-Bench Hard。
MRCR 论文——评估长上下文，OpenAI 使用它而非 MuSR、LongBench、BABILong 和 RULER。修复了被过度使用的"大海捞针"测试。
MATH 论文——数学竞赛问题的合集。前沿实验室关注 FrontierMath、AMO 以及 MATH 的子集：MATH level 5、AIME、AMC10/AMC12。
IFEval 论文——领先的指令遵循评估。另见 Facebook 的 Multi-IF、COLLIE 和 Scale MultiChallenge，后者现已超越 MT-Bench。
ARC AGI 挑战——一个著名的抽象推理"智商测试"基准，比许多快速饱和的基准持续了更长时间。

## English
This is a moving and often gamed target - May 2025 update here. We covered many of these in Benchmarks 101 and Benchmarks 201, while our Carlini, LMArena (warning!), and Braintrust covered private, arena, and product evals (read LLM-as-Judge - and Rubrics -and Applied LLMs essay). Benchmarks are linked to Datasets.

## 中文
这是一个不断变化且经常被博弈的目标——2025 年 5 月更新在这里。我们在 Benchmarks 101 和 Benchmarks 201 中涵盖了其中很多内容，而我们的 Carlini、LMArena（注意！）和 Braintrust 涵盖了私有、竞技场和产品评估（阅读 LLM-as-Judge 以及 Rubrics 和 Applied LLMs 文章）。基准测试与数据集相关联。

## English
The bigger picture is that benchmarks saturate increasingly quickly, and there is a sense that the whole approach is getting dated and new approaches are needed.

## 中文
更大的图景是，基准测试越来越快地被饱和，人们感觉整个方法正在过时，需要新的方法。

## English
**Section 3: Prompting, ICL & Chain of Thought**
Note: The GPT3 paper ("Language Models are Few-Shot Learners") should already have introduced In-Context Learning (ICL) - a close cousin of prompting. We also consider prompt injections required knowledge — Lilian Weng, Simon W.
The Prompt Report paper - a survey of prompting papers (podcast).
Chain-of-Thought paper - one of multiple claimants to popularizing Chain of Thought, along with Scratchpads and Let's Think Step By Step.
Tree of Thought paper - introducing lookaheads and backtracking (podcast).
Prompt Tuning paper - you may not need prompts - if you can do Prefix-Tuning, adjust decoding (say via entropy), or representation engineering.
Automatic Prompt Engineering paper - it is increasingly obvious that humans are terrible zero-shot prompters and prompting itself can be enhanced by LLMs. The most notable implementation of this is in the DSPy paper/framework.

## 中文
**第三部分：提示工程、ICL 与思维链**
注意：GPT3 论文（《Language Models are Few-Shot Learners》）应该已经介绍了上下文学习（ICL）——提示工程的近亲。我们还认为提示注入是必备知识——Lilian Weng、Simon W。
The Prompt Report 论文——提示工程论文的综述（播客）。
Chain-of-Thought 论文——推广思维链的多个声称者之一，与 Scratchpads 和 Let's Think Step By Step 并列。
Tree of Thought 论文——引入前瞻和回溯（播客）。
Prompt Tuning 论文——你可能不需要提示——如果你可以做 Prefix-Tuning、调整解码（比如通过熵），或者表征工程。
Automatic Prompt Engineering 论文——越来越明显的是，人类作为零样本提示者很糟糕，而提示工程本身可以被 LLM 增强。最著名的实现是 DSPy 论文/框架。

## English
More survey papers on reasoning (slides). Prompting and Context Engineering is one area where reading disparate papers may not be as useful as having more practical guides - we recommend Lilian Weng, Eugene Yan, and Anthropic's Prompt Engineering Tutorial and AI Engineer Workshop.

## 中文
更多推理方面的综述论文（幻灯片）。提示工程和上下文工程是一个领域，阅读零散的论文可能不如有更多实用指南有用——我们推荐 Lilian Weng、Eugene Yan 以及 Anthropic 的 Prompt Engineering Tutorial 和 AI Engineer Workshop。

## English
**Section 4: Retrieval Augmented Generation**
Introduction to Information Retrieval - a bit unfair to recommend a book, but we are trying to make the point that RAG is an IR problem and IR has a 60 year history that includes TF-IDF, BM25, FAISS, HNSW and other "boring" techniques.
2020 Meta RAG paper - which coined the term. The original authors have started Contextual and have coined RAG 2.0. Modern "table stakes" for RAG — HyDE, chunking, rerankers, multimodal data are better presented elsewhere.
MTEB paper - known overfitting that its author considers it dead, but still de-facto benchmark. Many embeddings have papers - pick your poison - SentenceTransformers, OpenAI, Nomic Embed, Jina v3, cde-small-v1, ModernBERT Embed - with Matryoshka embeddings increasingly standard.
GraphRAG paper - Microsoft's take on adding knowledge graphs to RAG, now open sourced. One of the most popular trends in RAG in 2024, alongside of ColBERT/ColPali/ColQwen (more in the Vision section).
RAGAS paper - the simple RAG eval recommended by OpenAI. See also Nvidia FACTS framework and Extrinsic Hallucinations in LLMs - Lilian Weng's survey of causes/evals for hallucinations (see also Jason Wei on recall vs precision).

## 中文
**第四部分：检索增强生成（RAG）**
Introduction to Information Retrieval——推荐一本书有点不公平，但我们是想表达 RAG 是一个信息检索问题，而 IR 有 60 年的历史，包括 TF-IDF、BM25、FAISS、HNSW 和其他"无聊"的技术。
2020 年 Meta RAG 论文——创造了这个术语。原作者创办了 Contextual 并创造了 RAG 2.0。现代 RAG 的"基本要求"——HyDE、分块、重排序器、多模态数据在其他地方有更好的呈现。
MTEB 论文——已知的过拟合，其作者认为它已经死了，但仍然是事实上的基准。许多嵌入模型有论文——各取所需——SentenceTransformers、OpenAI、Nomic Embed、Jina v3、cde-small-v1、ModernBERT Embed——其中 Matryoshka embeddings 越来越成为标准。
GraphRAG 论文——微软在 RAG 中添加知识图谱的方案，现已开源。2024 年 RAG 中最流行的趋势之一，与 ColBERT/ColPali/ColQwen 并列（更多在视觉部分）。
RAGAS 论文——OpenAI 推荐的简单 RAG 评估。另见 Nvidia FACTS 框架和 Extrinsic Hallucinations in LLMs——Lilian Weng 关于幻觉原因/评估的综述（另见 Jason Wei 关于召回率与精确度的讨论）。

## English
RAG is the bread and butter of AI Engineering at work in 2024, so there are a LOT of industry resources and practical experience you will be expected to have. LlamaIndex (course) and LangChain (video) have perhaps invested the most in educational resources. You should also be familiar with the perennial RAG vs Long Context debate.

## 中文
RAG 是 2024 年工作中 AI 工程的基本功，因此有大量的行业资源和实践经验是你需要掌握的。LlamaIndex（课程）和 LangChain（视频）也许在教育资源上投入最多。你还应该熟悉长期存在的 RAG 与长上下文之争。

## English
**Section 5: Agents**
SWE-Bench (our pod) & SWE-Lancer - after adoption by Anthropic, Devin and OpenAI, probably the highest profile agent benchmark today (vs WebArena or SWE-Gym). Technically a coding benchmark, but more a test of agents than raw LLMs. See also SWE-Agent, SWE-Bench Multimodal and the Konwinski Prize. For Tool-Agent-User interaction there is TauBench for Airlines and Retail and GAIA.
ReAct paper (our podcast) - ReAct started a long line of research on tool using and function calling LLMs, including Gorilla and the BFCL Leaderboard. Of historical interest - Toolformer and HuggingGPT.
MemGPT paper - one of many notable approaches to emulating long running agent memory, adopted by ChatGPT and LangGraph. Versions of these are reinvented in every agent system from MetaGPT to AutoGen to Smallville.
Voyager paper - Nvidia's take on 3 cognitive architecture components (curriculum, skill library, sandbox) to improve performance. More abstractly, skill library/curriculum can be abstracted as a form of Agent Workflow Memory.
Anthropic on Building Effective Agents (talk version) - just a great state-of-2024 recap that focuses on the importance of chaining, routing, parallelization, orchestration, evaluation, and optimization. See also Lilian Weng's Agents (ex OpenAI), Shunyu Yao on LLM Agents (now at OpenAI) and Chip Huyen's Agents.

## 中文
**第五部分：Agent**
SWE-Bench（我们的播客）和 SWE-Lancer——在被 Anthropic、Devin 和 OpenAI 采用后，可能是当今最高调的 agent 基准（相比 WebArena 或 SWE-Gym）。技术上是一个编码基准，但更多是对 agent 的测试而非原始 LLM。另见 SWE-Agent、SWE-Bench Multimodal 和 Konwinski Prize。对于工具-Agent-用户交互，有航空和零售领域的 TauBench 以及 GAIA。
ReAct 论文（我们的播客）——ReAct 开启了工具使用和函数调用 LLM 的长线研究，包括 Gorilla 和 BFCL Leaderboard。历史兴趣——Toolformer 和 HuggingGPT。
MemGPT 论文——模拟长时间运行的 agent 记忆的多种值得注意的方法之一，被 ChatGPT 和 LangGraph 采用。这些的变种在每个 agent 系统中都被重新发明，从 MetaGPT 到 AutoGen 到 Smallville。
Voyager 论文——Nvidia 对 3 个认知架构组件（课程、技能库、沙箱）来提高性能的方案。更抽象地说，技能库/课程可以抽象为一种 Agent 工作流记忆的形式。
Anthropic 关于构建有效 Agent 的文章（演讲版本）——一个很好的 2024 年状态总结，聚焦于链接、路由、并行化、编排、评估和优化的重要性。另见 Lilian Weng 的 Agents（前 OpenAI）、Shunyu Yao 关于 LLM Agents 的文章（现 OpenAI）以及 Chip Huyen 的 Agents。

## English
We covered many of the 2024 SOTA agent designs at NeurIPS, and you can find more readings in the UC Berkeley LLM Agents MOOC. Note that we skipped bikeshedding agent definitions, but if you really need one, you could use mine.

## 中文
我们在 NeurIPS 上涵盖了许多 2024 年最先进的 agent 设计，你可以在 UC Berkeley LLM Agents MOOC 中找到更多阅读材料。注意我们跳过了关于 agent 定义的争论，但如果你真的需要一个，可以用我的。

## English
**Section 6: Code Generation**
The Stack paper - the original open dataset twin of The Pile focused on code, starting a great lineage of open codegen work from The Stack v2 to StarCoder.
Open Code Model papers - choose from DeepSeek-Coder, Qwen2.5-Coder, or CodeLlama. Many regard 3.5 Sonnet as the best code model but it has no paper.
HumanEval/Codex paper - This is a saturated benchmark, but is required knowledge for the code domain. SWE-Bench is more famous for coding now, but is expensive/evals agents rather than models. Modern replacements include Aider, Codeforces, IOI, BigCodeBench, LiveCodeBench and SciCode.
AlphaCodeium paper - Google published AlphaCode and AlphaCode2 which did very well on programming problems, but here is one way Flow Engineering can add a lot more performance to any given base model.
CriticGPT paper - LLMs are known to generate code that can have security issues. OpenAI trained CriticGPT to spot them, and Anthropic uses SAEs to identify LLM features that cause this, but it is a problem you should be aware of.

## 中文
**第六部分：代码生成**
The Stack 论文——The Pile 的原始开源数据集兄弟，专注于代码，开启了从 The Stack v2 到 StarCoder 的伟大开源代码生成谱系。
开源代码模型论文——从 DeepSeek-Coder、Qwen2.5-Coder 或 CodeLlama 中选择。许多人认为 3.5 Sonnet 是最好的代码模型，但它没有论文。
HumanEval/Codex 论文——这是一个饱和的基准，但代码领域的必备知识。SWE-Bench 现在在编码方面更出名，但成本高/评估的是 agent 而非模型。现代替代方案包括 Aider、Codeforces、IOI、BigCodeBench、LiveCodeBench 和 SciCode。
AlphaCodeium 论文——Google 发布了 AlphaCode 和 AlphaCode2，在编程问题上表现很好，但这里是 Flow Engineering 可以为任何基础模型大幅提升性能的一种方式。
CriticGPT 论文——LLM 生成的代码可能存在安全问题，这是众所周知的。OpenAI 训练了 CriticGPT 来发现这些问题，Anthropic 使用 SAE 来识别导致此问题的 LLM 特征，但这是一个你应该意识到的问题。

## English
CodeGen is another field where much of the frontier has moved from research to industry and practical engineering advice on codegen and code agents like Devin are only found in industry blogposts and talks rather than research papers.

## 中文
代码生成是另一个前沿已经从研究转向产业的领域，关于代码生成和像 Devin 这样的代码 agent 的实用工程建议只能从行业博客和演讲中找到，而非研究论文。

## English
**Section 7: Vision**
Non-LLM Vision work is still important: e.g. the YOLO paper (now up to v11, but mind the lineage), but increasingly transformers like DETRs Beat YOLOs too.
CLIP paper - the first successful ViT from Alec Radford. These days, superceded by BLIP/BLIP2 or SigLIP/PaliGemma, but still required to know.
MMVP benchmark (LS Live) - quantifies issues with CLIP. Multimodal versions of MMLU (MMMU), and SWE-Bench do exist. See also MathVista and CharXiv.
Segment Anything Model and SAM 2 paper (our pod) - the very successful image and video segmentation foundation model. Pair with GroundingDINO.
Early fusion research: Contra the cheap "late fusion" work like LLaVA (our pod), early fusion covers Meta's Flamingo, Chameleon, Apple's AIMv2, Reka Core, et al. In reality there are at least 4 streams of visual LM work.

## 中文
**第七部分：视觉**
非 LLM 的视觉工作仍然重要：例如 YOLO 论文（现在已到 v11，但注意其谱系），但越来越多的 transformer 如 DETR 也在击败 YOLO。
CLIP 论文——Alec Radford 的第一个成功的 ViT。如今已被 BLIP/BLIP2 或 SigLIP/PaliGemma 取代，但仍然需要了解。
MMVP 基准（LS Live）——量化了 CLIP 的问题。MMLU 的多模态版本（MMMU）和 SWE-Bench 确实存在。另见 MathVista 和 CharXiv。
Segment Anything Model 和 SAM 2 论文（我们的播客）——非常成功的图像和视频分割基础模型。与 GroundingDINO 搭配使用。
早期融合研究：对比廉价的"后期融合"工作如 LLaVA（我们的播客），早期融合涵盖 Meta 的 Flamingo、Chameleon、Apple 的 AIMv2、Reka Core 等。实际上至少有 4 条视觉 LM 工作的流派。

## English
Much frontier VLM work these days is no longer published (the last we really got was GPT4V system card and derivative papers). We recommend having working experience with vision capabilities of 4o (including finetuning 4o vision), Claude 3.5 Sonnet/Haiku, Gemini 2.0 Flash, and o1. Others: Pixtral, Llama 3.2, Moondream, QVQ.
OCR is an important subset workhorse functionality of vision, so you may wish to check out Mistral OCR and VLM Run.

## 中文
如今许多前沿 VLM 工作不再发表（我们真正拿到的最后一个是 GPT4V 技术报告卡及其衍生论文）。我们推荐具有 4o（包括微调 4o 视觉）、Claude 3.5 Sonnet/Haiku、Gemini 2.0 Flash 和 o1 的视觉能力的工作经验。其他：Pixtral、Llama 3.2、Moondream、QVQ。
OCR 是视觉的一个重要子集功能，因此你可能希望查看 Mistral OCR 和 VLM Run。

## English
**Section 8: Voice**
Whisper paper - the successful ASR model from Alec Radford. Whisper v2, v3 and distil-whisper and v3 Turbo are open weights but have no paper.
AudioPaLM paper - our last look at Google's voice thoughts before PaLM became Gemini. See also: Meta's Llama 3 explorations into speech.
NaturalSpeech paper - one of a few leading TTS approaches. Recently v3.
Kyutai Moshi paper - an impressive full-duplex speech-text open weights model with high profile demo. See also Hume OCTAVE.
OpenAI Realtime API: The Missing Manual - Again, frontier omnimodel work is not published, but we did our best to document the Realtime API.

## 中文
**第八部分：语音**
Whisper 论文——Alec Radford 的成功 ASR 模型。Whisper v2、v3、distil-whisper 和 v3 Turbo 是开源权重但没有论文。
AudioPaLM 论文——在 PaLM 成为 Gemini 之前，我们对 Google 语音思考的最后一次深入了解。另见：Meta 的 Llama 3 语音探索。
NaturalSpeech 论文——几种领先的 TTS 方法之一。最近出了 v3。
Kyutai Moshi 论文——一个令人印象深刻的全双工语音-文本开源权重模型，有高调的演示。另见 Hume OCTAVE。
OpenAI Realtime API：缺失的手册——再说一次，前沿全能模型的工作没有发表，但我们尽最大努力记录了 Realtime API。

## English
We do recommend diversifying from the big labs here for now - try Daily, Livekit, Vapi, Assembly, Deepgram, Fireworks, Cartesia, Elevenlabs etc. See the State of Voice 2024. While NotebookLM's voice model is not public, we got the deepest description of the modeling process that we know of. Historical interest: wav2vec (see Snipd pod)

## 中文
我们确实推荐在这里从大实验室之外多元化选择——试试 Daily、Livekit、Vapi、Assembly、Deepgram、Fireworks、Cartesia、Elevenlabs 等。参见 State of Voice 2024。虽然 NotebookLM 的语音模型不公开，但我们得到了我们所知的对建模过程最深入的描述。历史兴趣：wav2vec（见 Snipd 播客）。

## English
With Gemini 2.0 also being natively voice and vision multimodal, the Voice and Vision modalities are on a clear path to merging in 2025 and beyond.

## 中文
随着 Gemini 2.0 也原生支持语音和视觉多模态，语音和视觉模态在 2025 年及以后显然在走向融合。

## English
**Section 9: Image/Video Diffusion**
Latent Diffusion paper - effectively the Stable Diffusion paper. See also SD2, SDXL, SD3 papers. These days the team is working on BFL Flux [schnell|dev|pro].
DALL-E / DALL-E-2 / DALL-E-3 paper - OpenAI's image generation.
Consistency Models paper - this distillation work with LCMs spawned the quick draw viral moment of Dec 2023. These days, updated with sCMs or DMDs.
Sora blogpost - text to video - no paper of course beyond the DiT paper (same authors), but still the most significant launch of the year, with many open weights competitors like OpenSora. Lilian Weng survey here.
Autoregressive image generation is all the rage this year for Gemini, 4o, and Llama's Native Image Gen.
More Image/Video work is done in Startups now. See Ideogram, Recraft, Reve Image, Pika, Playground, Genmo and Chinese models like Wan 2.1 and Kling.

## 中文
**第九部分：图像/视频扩散模型**
Latent Diffusion 论文——实际上就是 Stable Diffusion 论文。另见 SD2、SDXL、SD3 论文。如今该团队正在开发 BFL Flux [schnell|dev|pro]。
DALL-E/DALL-E-2/DALL-E-3 论文——OpenAI 的图像生成。
Consistency Models 论文——这项与 LCM 的蒸馏工作催生了 2023 年 12 月的快速绘画病毒式传播。如今已更新为 sCMs 或 DMDs。
Sora 博客文章——文生视频——当然除了 DiT 论文（同一作者）之外没有论文，但仍然是年度最重要的发布，有许多开源权重的竞争者如 OpenSora。Lilian Weng 的综述在这里。
自回归图像生成今年在 Gemini、4o 和 Llama 的原生图像生成中成为热门。
更多图像/视频工作现在在创业公司中进行。参见 Ideogram、Recraft、Reve Image、Pika、Playground、Genmo 以及中国模型如 Wan 2.1 和 Kling。

## English
We also highly recommend familiarity with ComfyUI (we were first to interview). Text Diffusion (Mercury/Inception is SOTA) and Music Diffusion are niche for now. For historical interest: DALL-E / DALL-E-2 / DALL-E-3 paper - OpenAI's image generation, and Imagen / Imagen 2 / Imagen 3 paper - Google's image gen.

## 中文
我们还强烈推荐熟悉 ComfyUI（我们是最早采访的）。文本扩散（Mercury/Inception 是最先进的）和音乐扩散目前是小众领域。历史兴趣：DALL-E/DALL-E-2/DALL-E-3 论文——OpenAI 的图像生成，以及 Imagen/Imagen 2/Imagen 3 论文——Google 的图像生成。

## English
**Section 10: Finetuning**
LoRA/QLoRA paper - the de facto way to finetune models cheaply, whether on local models or with 4o (confirmed on pod). FSDP+QLoRA is educational.
DPO paper - the popular, if slightly inferior, alternative to PPO, now supported by OpenAI as Preference Finetuning.
ReFT paper - instead of finetuning a few layers, focus on features instead.
Orca 3/AgentInstruct paper - see the Synthetic Data picks at NeurIPS but this is a great way to get finetune data.
RL/Reasoning Tuning papers - RL Finetuning for o1 is debated, but Let's Verify Step By Step and Noam Brown's many public talks give hints for how it works.

## 中文
**第十部分：微调**
LoRA/QLoRA 论文——低成本微调模型的事实标准，无论是对本地模型还是 4o（在播客中确认）。FSDP+QLoRA 很有教育意义。
DPO 论文——流行的、虽然略逊于 PPO 的替代方案，现在被 OpenAI 作为偏好微调支持。
ReFT 论文——不微调几层，而是专注于特征。
Orca 3/AgentInstruct 论文——参见 NeurIPS 的合成数据推荐，但这是获取微调数据的好方法。
RL/推理微调论文——o1 的 RL 微调存在争议，但 Let's Verify Step By Step 和 Noam Brown 的多次公开演讲给出了其工作原理的线索。

## English
We recommend going thru the Unsloth notebooks and HuggingFace's How to fine-tune open LLMs for more on the full process. This is obviously an endlessly deep rabbit hole that, at the extreme, overlaps with the Research Scientist track.

## 中文
我们推荐过一遍 Unsloth notebooks 和 HuggingFace 的 How to fine-tune open LLMs 来了解更多完整流程。显然这是一个无底洞，在极端情况下与研究科学家路线重叠。
