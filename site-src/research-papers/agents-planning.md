# Agent与规划

Agents & Planning — 12 条活跃资源

### [∇-Reasoner: LLM Reasoning via Test-Time Gradient Descent in Latent Space](#) 
 (2026-03-11) | ⭐⭐⭐⭐⭐ 5/5 | 🇨🇳

**LLM 推理能力增强的新方法**

## 一、核心问题

### 1.1 研究背景
大语言模型（LLM）的推理能力日益重要，但：
- **训练成本高**：扩大模型规模需要巨额算力
- **性能瓶颈**：传统方法（CoT、ToT）性能趋于饱和
- **效率问题**：零阶搜索方法（如Best-of-N）样本效率低
- **奖励稀疏**：长推理链中奖励信号难以传播

### 1.2 核心问题
**如何在不重新训练模型的情况下，通过测试时优化显著提升LLM推理能力？**

关键子问题：
1. 能否利用梯度信息而非仅奖励值？
2. 如何在离散token空间中进行可微优化？
3. 推理时优化与训练时优化的联系是什么？

## 二、创新点

…
 `gui` `on-device` `fine-tuning` `coding` `llm` `paper` `reinforcement-learning` `reasoning`

---
### [Chain-of-Tools - 在冻结 LLM 的 CoT 推理中利用海量未见工具](https://arxiv.org/pdf/2503.16779) 
 (2026-03-13) | ⭐⭐⭐⭐⭐ 5/5 | 🇨🇳

**LLM 推理能力增强的新方法**

**论文：** Chain-of-Tools: Utilizing Massive Unseen Tools in the CoT Reasoning of Frozen Language Models

**arXiv：** 2503.16779v1

**精读日期：** 2026-03-13

---

## 一、核心问题

**研究问题：**

如何让大型语言模型（LLMs）在链式思维（CoT）推理过程中高效地利用大量外部工具，包括训练时未见过的工具？

**子问题：**

1. **效率问题：** 如何在拥有大量工具（数千个）时高效选择合适的工具？
2. **泛化问题：** 如何处理训…
 `fine-tuning` `coding` `agent` `tool-use` `llm` `paper` `reinforcement-learning` `reasoning`

---
### [LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/) 
 (2025-03-21) | ⭐⭐⭐⭐⭐ 5/5 | 🌐

**Agent 领域必读经典综述，Lilian Weng 的文章至今仍是最好的入门基石**

Lilian Weng 的经典综述文章，系统阐述以 LLM 为核心的自主 Agent 系统架构。三大核心组件：Planning（任务分解、自我反思，涵盖 CoT、ToT、ReAct、Reflexion、CoH、AD 等方法）、Memory（短期上下文学习、长期向量存储）、Tool Use（API 调用、代码执行、外部知识访问）。文章深入分析了每种方法的原理和适用场景，包括多 Agent 协作框架。该文是 Agent 领域被引用最多的综述之一，适合作为系统性理解 Agent 设计的入门基石。
 `LLM-agent` `planning` `memory` `tool-use` `ReAct` `Reflexion` `Chain-of-Hindsight` `Lilian-Weng`

---
### [论证型人机决策（Deliberative Human-AI Decision Making）](https://arxiv.org/abs/2603.15946v1) 
by @**：Stylianos Loukas Vasileiou, Antonio Rago, Francesca Toni, William Yeoh (2026-03-22) | ⭐⭐⭐⭐ 4/5 | 🇨🇳

**LLM 推理能力增强的新方法**

论文试图解决什么问题？

1. AI 系统的黑箱问题：LLMs 的推理过程不透明，难以验证和信任
2. 计算论证的可扩展性问题：传统 CA 依赖手工知识工程，难以应用于开放域
3. 人机协作的失衡：当前 AI 要么完全自动化决策，要么只是提供解释，缺乏真正的协作
4. 高风险领域的可信度：在医学、法律等领域，AI 必须提供可争议、可审查的推理

核心洞察：计算论证（CA）与大语言模型（LLMs）的融合可以实现一个新范式——论证型人机决策制定，其中 AI 与人类共同推理，而不是为人类推理。
 `obsidian` `safety` `fine-tuning` `agent` `llm` `paper` `reinforcement-learning` `reasoning`

---
### [SkillRL 智能体进化](#) 
 (2026-03-14) | ⭐⭐⭐ 3/5 | 🇨🇳

**LLM Agent 记忆机制的深入研究**

Q1：这项研究要解决什么问题？

核心问题：LLM 智能体无法从历史经验中学习
1. 记忆效率低下：存储原始轨迹 Token 消耗大（15K+ tokens/episode）
2. 缺乏抽象能力：无法从具体案例中提取通用规则
3. 无法持续改进：每次任务从零开始，重复犯错

Q2：为什么这个问题重要？

对 AI 研究：
- 当前 LLM 智能体"昙花一现"（无长期记忆）
- 与人类学习方式差距大（人类会积累技能）
- 通往 AGI 的必经之路（持续学习能力）

---
核心收获

1. 技能抽象优于原始记忆：Token 减少 62%，性能提升 15.3%
2. 递归进化至关重要：性能随迭代持续提升
3. 分层组织有效：通用技能提供战略指导
4. 失败教训有价值：减少 68% 的重复失败

对高爷的建议

1. SmartPerf + SkillRL：集成到 SmartPerf 项目
2. Android 性能优化智能体：自动性能诊断和优化
3. 技术博客选题：
   - "SkillRL：让 LLM 智能体学会'刻意练习'"
   - "从论文到实战：SkillRL 在 Androi…
 `obsidian` `agent` `llm` `paper` `reinforcement-learning` `reasoning` `memory` `ai`

---
### [多智能体共识机制研究](https://arxiv.org/abs/2603.01213) 
by @**: arXiv (cs.MA, cs.LG) (2026-03-26) | ⭐⭐⭐ 3/5 | 🇨🇳

**多智能体协作方向的前沿探索**

当前基于 LLM 的多智能体系统能够可靠地达成共识吗？在存在恶意智能体的情况下，共识机制是否鲁棒？

这篇论文研究了一个基础问题：当多个 LLM 智能体需要达成一致决策时，它们能否可靠地完成这一任务？特别是在存在可能破坏共识的拜占庭智能体的情况下。

---
| 模型 | 群体大小 | 有效共识率 | 平均轮次 |
|------|---------|----------|---------|
| Qwen3-8B | N=4 | 15.8% | - |
| Qwen3-14B | N=4 | 46.6% | - |
| Qwen3-14B | N=8 | 67.4% | - |
| Qwen3-14B | N=16 | 33.3% | 29.0 |

解读:
- 即使没有拜占庭智能体，有效共识率也低于 70%
- 群体规模增大，性能下降（从 N=4 的 46.6% 降至 N=16 的 33.3%）
- 较大模型（14B）显著优于较小模型（8B）

关键发现 2: 提示内容影响活跃性

| 提示变体 | 有效共识率 | 平均轮次 |
|---------|----------|----…
 `analysis` `safety` `agent` `llm` `paper` `2026-03-26` `multi-agent` `survey`

---
### [UI-Voyager: 自进化 GUI 智能体](https://arxiv.org/abs/2603.24533) 
by @**: Zichuan Lin 等（腾讯混元） (2026-03-27) | ⭐⭐⭐ 3/5 | 🇨🇳

**GUI 自动化智能体的创新实践**

移动 GUI 智能体在训练中面临两个根本性挑战：1）失败轨迹学习效率低——失败轨迹占绝大多数但未被有效利用；2）长程任务的信用分配模糊——轨迹级稀疏奖励（成功/失败）无法告知智能体哪一步做错了。
 `gui` `on-device` `agent` `UI-Voyager：基于失败经验自进化的` `android` `research` `llm` `reinforcement-learning`

---
### [SWE-Bench Mobile: Can Large Language Model Agents Develop Industry-Level Mobile Applications?](#) 
by @明确计划添加 Kotlin 任务，届时可对比 iOS/Android 平台差异。 (2026-04-01) | ⭐⭐⭐ 3/5 | 🇨🇳

**工具调用能力的新探索**

当前最强的 LLM 编码 Agent 能否胜任工业级移动应用开发？它们在真实产品需求、多模态输入、大规模代码库上表现如何？
 `tools` `on-device` `coding` `agent` `llm` `paper` `reasoning` `ai`

---
### [Act While Thinking (PASTE)](#) 
by @- 重叠（LLM 思考期间并行执行工具）提升 10x 以上——说明推测执行确实将原本串行的工具调用前移了 (2026-04-03) | ⭐⭐⭐ 3/5 | 🇨🇳

**工具调用能力的新探索**

LLM Agent 串行执行"LLM 推理 → 工具调用"循环，工具执行占总时间 35%-61%。LLM 持有昂贵资源却被迫等待外部工具返回结果，造成严重的延迟瓶颈和资源浪费。
 `safety` `agent` `tool-use` `llm` `paper` `reinforcement-learning` `reasoning` `multi-agent`

---
### [PROV-AGENT: Provenance-Based AI Agent](#) 
by @**：Souza et al. (ORNL/Argonne National Lab) (2026-04-08) | ⭐⭐⭐ 3/5 | 🇨🇳

**工具调用能力的新探索**

Agentic workflow 中，AI agent 会 hallucinate 或推理错误，且错误会在 agent 间传播（一个 agent 的输出作为另一个的输入）。传统 provenance 技术无法捕获 agent 特有的元数据（prompts、responses、decisions）与 workflow 上下文的关联。该论文要解决的核心问题是：如何将 AI agent 行为纳入端到端 workflow provenance，实现可追溯、可审计、可复现的 agentic workflow？

---
 `gui` `agent` `android` `llm` `paper` `reasoning` `multi-agent`

---
### [Decoding the Configuration of AI Coding Agents: Insights from Claude Code Projects](#) 
by @完成，虽经两位作者审核确认，但主观偏差难以完全排除。 (2026-04-09) | ⭐⭐⭐ 3/5 | 🇨🇳

**工具调用能力的新探索**

Agentic code assistants（Claude Code、Codex、Jules）是 2024 年兴起的新一代 AI 编程工具，能自主完成端到端软件工程任务。但这类工具的行为和效果高度依赖配置文件（Claude.md），目前缺乏对这类配置文件的结构、内容和最佳实践的系统性研究。
 `coding` `agent`

---
### [Paper摘要：基于强化学习的AI Agent调整内核configuration选项](https://mp.weixin.qq.com/s?__biz=Mzk0NzcwMTUwNQ==&mid=2247484774&idx=1&sn=0023092ce8a595928fddc60dd1c7a296) 
 (2026-02-03) | ⭐⭐⭐ 3/5 | 🇨🇳

**RL Agent 调内核 config 的学术尝试，技术新颖但脱离工程实际**

论文 OS-R1 提出用 RL Agent 自动配置 Linux 内核 18000+ configuration 选项。Rule-Guided Agent 设计，两阶段训练（Warm-up + Exploration），3000+ 配置样本数据集。在 Nginx/PostgreSQL/Redis 上取得性能提升。但生产环境极少为调优重编译内核，严重脱离工程实际。
 `OS-R1` `强化学习` `Linux内核` `kernel-tuning` `AI-agent`

---