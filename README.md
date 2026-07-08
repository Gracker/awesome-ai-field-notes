# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [MetaSkill-Evolve: Recursive Self-Improvement of LLM Agents via Two-Timescale Meta-Skill Evolutio...](https://arxiv.org/abs/2607.05297) ⭐4 · 2026-07-08 — 现有自改进 Agent 只改进任务技能（做什么），而把如何改进的元技能写死论文提出 MetaSkill-Evolve...
- [LLM-as-a-Verifier: A General-Purpose Verification Framework](https://arxiv.org/abs/2607.05391) ⭐4 · 2026-07-08 — 本文把验证（verification）识别为 LLM 的一个新扩展轴，并提出 LLM-as-a-Verifier 通用验证框架，用打分 token 期望生成连续分数...
- [EvoAgentBench: Benchmarking Agent Self-Evolution via Ability Transfer](https://arxiv.org/abs/2607.05202) ⭐4 · 2026-07-08 — EvoAgentBench 把 Agent 自进化评测从单轮解题准确率推向过程级能力迁移：从执行轨迹里抽取 trace-grounded 的 Abilities，规范成可复用的操作单元...
- [DSpark: Confidence-Scheduled Speculative Decoding with Semi-Autoregressive Generation](https://arxiv.org/abs/2607.05147) ⭐4 · 2026-07-08 — DSpark 把并行草稿生成与按置信度调度验证统一在同一个投机解码框架里：半自回归主干配合轻量串行模块保留块内依赖以缓解 suffix decay，验证长度则根据前缀存活概率与引擎吞吐画像动态调整在 DeepSeek-V4 在线服务上，相比生产基线 MTP-1...
- [AgentGym2: Benchmarking Large Language Model Agents in De-Idealized Real-World Environments](https://arxiv.org/abs/2607.05174) ⭐4 · 2026-07-08 — 现有 Agent 评测多为理想化玩具环境，掩盖了真实部署中的噪声缺工具和需求不全AgentGym2 直接用真实端到端业务需求构造任务实例，要求 Agent 能执行完整流程能主动探索发现新工具能在噪声与欠规格输入下保持稳健15 个专有与开源模型测试显示...
- [Reason, Reward, Refine: Step-Level Errors Corrections with Structured Feedback for Physics Reaso...](https://arxiv.org/abs/2607.05199) ⭐3 · 2026-07-08 — 小语言模型做物理推理时错误会沿步骤向前传播论文提出 step-level 奖励框架：先定位首次推理错误，再生成针对性结构化反馈，并带 KL 正则的策略梯度训练模型自修...
- [OptiAgent: End-to-End Optimization Modeling via Multi-Agent Iterative Refinement](https://arxiv.org/abs/2607.05346) ⭐3 · 2026-07-08 — OptiAgent 接收自然语言描述的运筹学问题，多 Agent 协同产出可执行求解器代码它把建模阶段放在核心位置，由专门 Agent 抽取决策变量与约束...
- [Measuring Harness-Induced Belief Divergence in Multi-Step LLM Agents](https://arxiv.org/abs/2607.04528) ⭐5 · 2026-07-07 — 本文把 harness 从评测 "实现细节" 重新定位为实验变量：在任务环境底层 LLM 全部固定时，harness 也能改变 agent 多步下的"信念"作者提出 belief-rollout 诊断...
- [Weak-to-Strong Generalization via Direct On-Policy Distillation](https://arxiv.org/abs/2607.05394) ⭐4 · 2026-07-07 — 本文把 RLVR 当作一个跨模型的隐式奖励信号来迁移：先在算力廉价的小模型上跑 RL，再把 RL 前后策略分布对数比作为密集奖励蒸馏到更大的学生模型上作者提出 Direct-OPD 在学生 on-policy 状态上施加教师"RL 引起的策略位移"...
- [MRMS: A Multi-Resolution Memory Substrate for Long-Lived AI Agents](https://arxiv.org/abs/2607.04617) ⭐4 · 2026-07-07 — 本文提出多分辨率记忆基底 MRMS，沿"表征轴时间轴"组织 agent 记忆表征轴覆盖结构化记录向量表征图关系，时间轴覆盖短程轨迹中程抽象长程语义承诺核心约束是"结构化-向量-图"三路同步：结构化记录决定资格，向量支持召回，图关系再裁决支持矛盾与覆盖...

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 229 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 126 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 77 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 19 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 44 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 33 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 139 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 1196
- 公开展示卡片: 667
- 有全文内容: 592
- 最近 7 天信号: 59
- 输出目录: `dist/`

## 热门标签

`ai-tools`, `llm`, `research`, `openai`, `attention`, `google`, `anthropic`, `optimization`, `2026`, `gemini`, `claude-code`, `benchmark`, `agent`, `digest`, `论文工具`, `claude`, `open-source`, `enterprise`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
