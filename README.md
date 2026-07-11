# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [Remember When It Matters: Proactive Memory Agent for Long-Horizon Agents](https://arxiv.org/abs/2607.08716) ⭐5 · 2026-07-11 — Proactive Memory Agent 把被动检索改为持续整理 + 主动暴露，对抗长程任务中的"行为状态衰减"
- [From Prompts to Contracts: Harness Engineering for Auditable Enterprise LLM Agents](https://arxiv.org/abs/2607.08028) ⭐5 · 2026-07-11 — 把企业 LLM 智能体从 prompt 原型重构为可审计 harness：确定性围栏 + 答案契约 + 重建执行轨迹的运行时架构
- [When LLMs Agree, Are They Right? Auditing Self-Consistency and Cross-Model Agreement as Confiden...](https://arxiv.org/abs/2607.08065) ⭐4 · 2026-07-11 — 质疑 LLM-as-judge 的一致性假设：模型自一致 / 跨模型一致并不等于正确，并给出企业评测管线的审计补丁
- [The Illusion of Equivalency: Statistical Characterization of Quantization Effects in LLMs](https://arxiv.org/abs/2607.08734) ⭐4 · 2026-07-11 — 提出 correctness agreement 度量量化模型的决策级行为变化，揭示 PTQ 评测中普遍存在的"等效幻觉"
- [Compete Then Collaborate: Frontier AI Teachers Build a Verifiable Curriculum to Improve a Coding...](https://arxiv.org/abs/2607.08255) ⭐4 · 2026-07-11 — 四家前沿模型先竞争再协作产出可验证编程课程，规避单教师评委偏置，显著提升小模型 coding 蒸馏上限
- [CausalDS: Benchmarking Causal Reasoning in Data-Science Agents](https://arxiv.org/abs/2607.08093) ⭐4 · 2026-07-11 — CausalDS 把因果推理 + 数据科学 agent 统一在同一基准：结构化数据生成 完整工具循环，指出现瓶颈在因果变量选择而非工具使用
- [Agentic Neural Architecture Search](https://arxiv.org/abs/2607.07984) ⭐4 · 2026-07-11 — Agentic NAS 让 LLM agent 负责跨任务生成候选架构，NAS 引擎负责算力受限下的精细搜索，显著降低冷启动成本
- [MetaSkill-Evolve: Recursive Self-Improvement of LLM Agents via Two-Timescale Meta-Skill Evolutio...](https://arxiv.org/abs/2607.05297) ⭐4 · 2026-07-08 — 现有自改进 Agent 只改进任务技能（做什么），而把如何改进的元技能写死论文提出 MetaSkill-Evolve...
- [LLM-as-a-Verifier: A General-Purpose Verification Framework](https://arxiv.org/abs/2607.05391) ⭐4 · 2026-07-08 — 本文把验证（verification）识别为 LLM 的一个新扩展轴，并提出 LLM-as-a-Verifier 通用验证框架，用打分 token 期望生成连续分数...
- [EvoAgentBench: Benchmarking Agent Self-Evolution via Ability Transfer](https://arxiv.org/abs/2607.05202) ⭐4 · 2026-07-08 — EvoAgentBench 把 Agent 自进化评测从单轮解题准确率推向过程级能力迁移：从执行轨迹里抽取 trace-grounded 的 Abilities，规范成可复用的操作单元...

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 229 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 140 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 79 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 23 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 44 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 33 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 139 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 1220
- 公开展示卡片: 687
- 有全文内容: 612
- 最近 7 天信号: 61
- 输出目录: `dist/`

## 热门标签

`ai-tools`, `llm`, `research`, `openai`, `attention`, `google`, `anthropic`, `optimization`, `2026`, `claude-code`, `gemini`, `benchmark`, `agent`, `digest`, `enterprise`, `claude`, `multi-agent`, `论文工具`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
