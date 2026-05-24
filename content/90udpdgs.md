# LLM Powered Autonomous Agents（基于大语言模型的自主智能体）

## 英文原文

Building agents with LLM (large language model) as its core controller is a cool concept. Several proof-of-concepts demos, such as AutoGPT, GPT-Engineer and BabyAGI, serve as inspiring examples. The potentiality of LLM extends beyond generating well-written copies, stories, essays and programs; it can be framed as a powerful general problem solver.

## 中文翻译

以大语言模型（LLM）作为核心控制器来构建智能体是一个很有意思的概念。几个概念验证演示，如 AutoGPT、GPT-Engineer 和 BabyAGI，是很有启发性的例子。LLM 的潜力远不止生成优美的文案、故事、论文和程序；它可以被框架为一个强大的通用问题解决器。

---

## 英文原文

In a LLM-powered autonomous agent system, LLM functions as the agent's brain, complemented by several key components:
- Planning: Subgoal and decomposition - The agent breaks down large tasks into smaller, manageable subgoals, enabling efficient handling of complex tasks. Reflection and refinement: The agent can do self-criticism and self-reflection over past actions, learn from mistakes and refine them for future steps.
- Memory: Short-term memory is in-context learning. Long-term memory provides the agent with the capability to retain and recall information over extended periods, often by leveraging an external vector store and fast retrieval.
- Tool use: The agent learns to call external APIs for extra information that is missing from the model weights, including current information, code execution capability, access to proprietary information sources.

## 中文翻译

在基于 LLM 的自主智能体系统中，LLM 作为智能体的大脑，配合几个关键组件：
- 规划：子目标和分解——智能体将大任务分解为更小、可管理的子目标，从而高效处理复杂任务。反思和改进：智能体可以对过去的行为进行自我批评和自我反思，从错误中学习并为未来步骤进行改进。
- 记忆：短时记忆是上下文学习。长时记忆为智能体提供在较长时间内保留和回忆信息的能力，通常通过利用外部向量存储和快速检索来实现。
- 工具使用：智能体学习调用外部 API 来获取模型权重中缺失的额外信息，包括当前信息、代码执行能力、对专有信息源的访问。

---

## 英文原文

Task decomposition can be done (1) by LLM with simple prompting like "Steps for XYZ.\n1.", "What are the subgoals for achieving XYZ?", (2) by using task-specific instructions; e.g. "Write a story outline." for writing a novel, or (3) with human inputs.
Tree of Thoughts (Yao et al. 2023) extends CoT by exploring multiple reasoning possibilities at each step. It first decomposes the problem into multiple thought steps and generates multiple thoughts per step, creating a tree structure.

## 中文翻译

任务分解可以 (1) 通过 LLM 用简单提示如"XYZ 的步骤。\n1."、"实现 XYZ 的子目标是什么？"，(2) 使用任务特定指令；例如为写小说使用"写一个故事大纲。"，或 (3) 通过人类输入。
思维树（Tree of Thoughts，Yao et al. 2023）通过在每一步探索多种推理可能性来扩展思维链。它首先将问题分解为多个思维步骤，并在每一步生成多个思维，创建树状结构。

---

## 英文原文

Self-reflection is a vital aspect that allows autonomous agents to improve iteratively by refining past action decisions and correcting previous mistakes. ReAct (Yao et al. 2023) integrates reasoning and acting within LLM by extending the action space to be a combination of task-specific discrete actions and the language space. The prompt template incorporates explicit steps for LLM to think: Thought: ... Action: ... Observation: ... (Repeated many times)
Reflexion (Shinn & Labash 2023) is a framework to equip agents with dynamic memory and self-reflection capabilities to improve reasoning skills.

## 中文翻译

自我反思是一个关键方面，允许自主智能体通过改进过去的行动决策和纠正先前错误来迭代改进。ReAct（Yao et al. 2023）通过将行动空间扩展为任务特定离散动作和语言空间的组合，将推理和行动整合在 LLM 中。提示模板包含 LLM 思考的明确步骤：Thought: ... Action: ... Observation: ...（重复多次）
Reflexion（Shinn & Labash 2023）是一个为智能体配备动态记忆和自我反思能力以提高推理能力的框架。

---

## 英文原文

The external memory can alleviate the restriction of finite attention span. A standard practice is to save the embedding representation of information into a vector store database that can support fast maximum inner-product search (MIPS). To optimize the retrieval speed, the common choice is approximate nearest neighbors (ANN) algorithm to return approximately top k nearest neighbors to trade off a little accuracy lost for a huge speedup.
Common ANN algorithms include LSH (Locality-Sensitive Hashing), ANNOY, HNSW, and FAISS.

## 中文翻译

外部记忆可以缓解有限注意力跨度的限制。一个标准做法是将信息的嵌入表示保存到向量存储数据库中，以支持快速最大内积搜索（MIPS）。为了优化检索速度，通常的选择是近似最近邻（ANN）算法，返回大约 top k 个最近邻，以微小的精度损失换取巨大的速度提升。
常见的 ANN 算法包括 LSH（局部敏感哈希）、ANNOY、HNSW 和 FAISS。
