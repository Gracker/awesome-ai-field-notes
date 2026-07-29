# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [用 Codex 指挥 ChatGPT Pro：双 Agent 编程工作流](https://mp.weixin.qq.com/s/xspmSmOfa8Ve47VCjmEXLw) ⭐4 · 2026-07-29 — 最强编程 Agent 可能是分工：Codex 管拆解与本地验收，Pro 管深度写码，最终以测试和门禁为准
- [Tools Are Not Islands: Set-Level Tool Retrieval for LLM Agents via Query-Conditioned Hyperedge P...](https://arxiv.org/abs/2607.25718) ⭐5 · 2026-07-28 — 工具检索的打分单位应是集合：HYSET 用查询条件下的超边预测优化联合效用，而不是单工具 top-k
- [Speculate While You Reason: Teaching Agents to Predict Their Next Tool Call via Joint Agent-Spec...](https://arxiv.org/abs/2607.25816) ⭐5 · 2026-07-28 — 工具等待可以同模型投机：Self-Speculating Agent 用 agent/speculator 双模式 + 联合 RL 抬高 next-call Hit@1
- [OpenAI Codex Security (CLI + TypeScript SDK)](https://github.com/openai/codex-security) ⭐5 · 2026-07-28 — Agent 写完代码，安全扫描要进同一条 loop：Codex Security 把 scan 做成可嵌 CI 的部件
- [HiSkill: Empowering LLM Agents with Hierarchical Skill Graphs](https://arxiv.org/abs/2607.25853) ⭐5 · 2026-07-28 — 技能不能只是文案清单：HiSkill 用层次技能图把高层技能接到 AtomicOp，并显式建模分解与恢复
- [The Regression Tax: Decomposing Why Skills Help and Hurt LLM Agents](https://arxiv.org/abs/2607.22520) ⭐5 · 2026-07-28 — 为LLM Agent添加程序性技能通常以平均任务成功率来评估，但这掩盖了一个关键代价：技能也可能导致性能倒退作者在约6000次实验运行中发现三种倒退机制：技能描述渗透（即使未被调用也改变Agent行为）接地偏移（程序步骤覆盖输入解释）验证偏移（程序抑制了Agent本应执行的输出检...
- [Skill Self-Play: Pushing the Frontier of LLM Capability with Co-Evolving Skills](https://arxiv.org/abs/2607.22529) ⭐5 · 2026-07-28 — Skill Self-Play (Skill-SP) 是一个共同进化框架，解决了LLM自我进化中任务多样性与验证可靠性之间的根本矛盾它将Agent技能作为中间层：每个技能在特定场景下提供可验证执行...
- [Our Position on Open-Weights Models](https://www.anthropic.com/news/position-open-weights-models) ⭐5 · 2026-07-28 — Dario Amodei明确Anthropic从未主张禁止开放权重模型，认为不含危险能力的开放权重模型是公共产品Anthropic支持三项措施：(1)限制向中国出售先进芯片并打击走私；(2)打击工业级蒸馏操作.
- [Anatomy of a Frontier Lab Agent Intrusion: A Technical Timeline](https://huggingface.co/blog/agent-intrusion-technical-timeline) ⭐5 · 2026-07-28 — 本周最硬的 Agent 安全材料：机器速度把普通供应链/沙箱弱点变成昂贵的防守问题
- [MemSFT: Mitigating Alignment Tax with an External Parametric Memory](https://arxiv.org/abs/2607.25614) ⭐4 · 2026-07-28 — 领域适配别硬 SFT 整模：MemSFT 用可插拔参数记忆 + router 融合，减 alignment tax 且 memory 可跨 backbone 复用

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 236 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 158 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 93 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 26 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 51 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 35 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 150 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 1567
- 公开展示卡片: 749
- 有全文内容: 665
- 最近 7 天信号: 96
- 输出目录: `dist/`

## 热门标签

`ai-tools`, `llm`, `research`, `openai`, `attention`, `arxiv`, `google`, `anthropic`, `evaluation`, `benchmark`, `optimization`, `claude-code`, `2026`, `gemini`, `workflow`, `agent`, `coding-agent`, `codex`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
