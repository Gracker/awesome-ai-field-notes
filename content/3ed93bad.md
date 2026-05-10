# Human–AI Collaboration for Scaling Agile Regression Testing: An Agentic-AI Teammate from Manual to Automated Testing

**来源：** arXiv / ESEC/FSE 2026 Industry Track
**原文链接：** https://arxiv.org/abs/2603.08190
**发表时间：** 2026-03-09（arXiv在线：2026-04-13）

---

## 核心问题

在大型工业软件开发组织（如西门子旗下的Hacon公司）中，Agile/Scrum团队面临一个持续性瓶颈：人工编写的测试规格（test specifications）积累速度远远快于团队将其转化为自动化脚本的能力。尽管CI/CD管道已成熟，82-87%的回归测试仍是人工执行，阻碍了快速反馈和可持续交付。论文研究的问题是：**将一个Agentic AI系统引入Agile测试工程工作流，能否提升生产力、脚本质量，并实现有效的人机协作？**

## 创新点

1. **静默AI队友模式（Silent AI Teammate）：** 不同于实时对话式Copilot，该系统以异步批处理方式运行，在每个sprint开始前生成候选自动化脚本，让工程师在sprint周期内审阅，不打断正在进行的开发活动。这种设计非常契合Agile团队节律。

2. **Generator-Evaluator-Reporter三角色多Agent架构：** 系统内嵌三类专业Agent：Generator基于RAG从历史规格-脚本对中生成候选脚本；Evaluator在Jenkins环境中执行并分析日志，评估语法正确性、语义等价性和覆盖率；Reporter将结果整合为结构化摘要和执行报告，输出至MLflow用于可追溯性。三角色各司其职，迭代有界。

3. **RAG驱动的测试脚本生成：** 使用检索增强生成从已有的规格-脚本对知识库中提取相似案例，提升生成质量并降低幻觉风险。这对于工业级、领域知识密集的测试场景尤为重要。

4. **明确的人类主导治理机制：** Agent的自主权有严格边界——无权将脚本直接加入回归套件，所有输出必须经人工批准。Artifact均记录在案，确保合规和问责。

## 关键实验数据

**实验设计：** 4周周期，5名测试工程师，61个测试规格（覆盖6个功能领域，复杂度2-18步/案例，story point 3-8，输入清晰度评级A-D）。

- **代码复用率：** Artifact比较显示，AI生成的代码中平均30-50%被工程师直接保留无需修改。这表明AI提供了实质性的"起点加速"。
- **脚本质量分布（49个脚本）：** 15个完全重写，20个重大修改，13个中等修改，1个轻微修改。主要问题包括：硬编码数据（31/49），冗余import（29/49），未使用对象（23/49），缺失或错误的验证逻辑（>30案例）。

## 局限

1. **外部效度受限：** 仅在一家公司、一个5人小团队、特定脚本集上评估。
2. **输入规格质量依赖：** 系统效果高度依赖测试规格的完整性和清晰度。测试规格设计用于人类阅读，AI的逐字解析会暴露人类测试员直觉上能绕过的模糊地带。
3. **人类审阅不可替代：** 大部分生成脚本需要中等到重大修改才能符合维护性和领域特定期望（"technically correct but contextually inappropriate"）。
4. **评估周期较短：** 4周周期可能不足以暴露长期维护问题。

## 对 AI 工程实践的启示

1. **Spec-Driven Development是Agent落地的前提：** 要让AI生成高可用脚本，必须先建立清晰、完整、无歧义的规格文档标准。
2. **"Silent Teammate"模式比实时对话更适合后台批处理场景：** 异步预生成候选Artifact的模式比实时对话式Copilot更适合sprint驱动的工程节奏。
3. **Human-in-the-loop必须设计为一级公民而非外挂：** Agent无权单方面合入、强制人工审阅、Artifact追溯——这类治理机制应成为所有企业级Agentic AI系统的默认架构。
4. **代码复用率30-50%是衡量AI生成脚本可用性的有效先行指标：** 低于此阈值说明领域知识库（RAG base）需要扩展或规格质量需要提升。

---

**标签：** #paper #agent #testing #agile #human-ai-collaboration #rag #fse2026
