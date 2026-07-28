# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [The Regression Tax: Decomposing Why Skills Help and Hurt LLM Agents](https://arxiv.org/abs/2607.22520) ⭐5 · 2026-07-28 — 为LLM Agent添加程序性技能通常以平均任务成功率来评估，但这掩盖了一个关键代价：技能也可能导致性能倒退作者在约6000次实验运行中发现三种倒退机制：技能描述渗透（即使未被调用也改变Agent行为）接地偏移（程序步骤覆盖输入解释）验证偏移（程序抑制了Agent本应执行的输出检...
- [Skill Self-Play: Pushing the Frontier of LLM Capability with Co-Evolving Skills](https://arxiv.org/abs/2607.22529) ⭐5 · 2026-07-28 — Skill Self-Play (Skill-SP) 是一个共同进化框架，解决了LLM自我进化中任务多样性与验证可靠性之间的根本矛盾它将Agent技能作为中间层：每个技能在特定场景下提供可验证执行...
- [Our Position on Open-Weights Models](https://www.anthropic.com/news/position-open-weights-models) ⭐5 · 2026-07-28 — Dario Amodei明确Anthropic从未主张禁止开放权重模型，认为不含危险能力的开放权重模型是公共产品Anthropic支持三项措施：(1)限制向中国出售先进芯片并打击走私；(2)打击工业级蒸馏操作.
- [TRACE-ROUTER: Task-Consistent and Adaptive Online Routing for Agentic AI](https://arxiv.org/abs/2607.22465) ⭐4 · 2026-07-28 — TRACE-Router解决了Agent工作流中每次调用独立路由与任务级结果之间的不匹配问题它在任务准入时通过上下文赌博机一次性分配模型，将后续所有调用固定到同一后端，并使用终端奖励联合考虑准确率和延迟更新策略在tau2-Bench上高出7-8个准确率点...
- [From Isolated Tasks to Structured Capabilities: A Multilayer Taxonomy for Large Language Models](https://arxiv.org/abs/2607.22182) ⭐4 · 2026-07-28 — 提出一个包含14个能力域和91个子技能的多层分类体系，覆盖原始层构建层和整合层，以人类认知科学而非LLM架构为指导作者筛选了ACLAAAIICML和NeurIPS在2023-2025年间发表的31505篇论文，映射了其中15934篇LLM论文研究注意力集中在语言语义能力(22.
- [CausalForge: A Formally Grounded, Self-Improving Agentic Framework for Automated Research in Cau...](https://arxiv.org/abs/2607.22511) ⭐4 · 2026-07-28 — CausalForge结合了Causalean（一个包含7035条机器检查声明的Lean因果推断证明库）和CausalSmith（一个自我改进的Agent流水线，可选题提出结果形式化陈述构造证明并提交人类审查）因为机器检查证明只能验证形式陈述与假设一致...
- [即将到来的 Loop: coding agent 之上的 harness loop 正在成为第二层接口](https://x.com/yibie/status/2075435834581668088) ⭐5 · 2026-07-27 — harness loop 正在改变 coding agent 的工作方式：人写 loop，loop 驱动模型
- [The Reverse Information Paradox: AI 时代的企业 IP 风险从卖方泄密反过来了](https://x.com/satyanadella/status/2076323181154230284) ⭐5 · 2026-07-27 — AI 时代的信息悖论反转：买方在付费使用的同时，还付出了更宝贵的专有知识
- [Own the Outer Loop: Agent 工程的 Quality / Verdict / Answerability 框架](https://x.com/addyosmani/status/2074927530482835916) ⭐5 · 2026-07-27 — Agent 工程三支柱：Quality（质量证据）Verdict（裁决）Answerability（可解释性）
- [睡眠计算: Agent 运行痕迹的离线记忆巩固模式](https://x.com/yibie/status/2075457839481708960) ⭐4 · 2026-07-27 — Agent 记忆新模式：热路径只记录，离线 GeneratorReflectorCurator 提炼经验

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 233 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 151 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 88 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 25 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 48 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 34 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 150 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 1547
- 公开展示卡片: 729
- 有全文内容: 639
- 最近 7 天信号: 77
- 输出目录: `dist/`

## 热门标签

`ai-tools`, `llm`, `research`, `openai`, `attention`, `arxiv`, `google`, `anthropic`, `evaluation`, `benchmark`, `optimization`, `2026`, `claude-code`, `gemini`, `coding-agent`, `workflow`, `agent`, `digest`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
