# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [用 Codex 指挥 ChatGPT Pro：双 Agent 编程工作流](https://mp.weixin.qq.com/s/xspmSmOfa8Ve47VCjmEXLw) ⭐4 · 2026-07-29 — 最强编程 Agent 可能是分工：Codex 管拆解与本地验收，Pro 管深度写码，最终以测试和门禁为准
- [WorkOS MCP: Manage your WorkOS account from any AI agent](https://workos.com/blog/management-mcp-server) ⭐4 · 2026-07-29 — Agent 能管 SSO/用户/审计，但铸钥模拟登录密钥字段默认不准进上下文
- [Superlogical](https://mitchellh.com/writing/superlogical) ⭐4 · 2026-07-29 — Hashimoto 新公司从终端多路复用器起手：人类agentCI生产共用持久 session
- [Some thoughts about Anthropic's new cryptanalysis results](https://blog.cryptographyengineering.com/2026/07/29/some-notes-about-anthropics-new-results) ⭐4 · 2026-07-29 — HAWK 被腰料有实际意义，AES 加速远未破实装；瓶颈已从能不能转到人能不能验
- [Self-hosting Kimi K3: 20% more hardware cost, 20% better task resolution](https://aistack.imec-int.com/blog/gpu-self-hosting) ⭐4 · 2026-07-29 — K3 自托管贵 20%慢 8 倍，但任务解决率高 24 个百分点；附 TCO 长尾数据
- [Tools Are Not Islands: Set-Level Tool Retrieval for LLM Agents via Query-Conditioned Hyperedge P...](https://arxiv.org/abs/2607.25718) ⭐5 · 2026-07-28 — 工具检索的打分单位应是集合：HYSET 用查询条件下的超边预测优化联合效用，而不是单工具 top-k
- [Speculate While You Reason: Teaching Agents to Predict Their Next Tool Call via Joint Agent-Spec...](https://arxiv.org/abs/2607.25816) ⭐5 · 2026-07-28 — 工具等待可以同模型投机：Self-Speculating Agent 用 agent/speculator 双模式 + 联合 RL 抬高 next-call Hit@1
- [SkillGate: Cost Efficient Runtime Malicious Skill File Detection in Coding Agents](https://arxiv.org/abs/2607.25619) ⭐5 · 2026-07-28 — skill 文件是新的供应链攻击面：regex+LLM 双层网关拦截恶意 skill，token 省 77%
- [OpenAI Codex Security (CLI + TypeScript SDK)](https://github.com/openai/codex-security) ⭐5 · 2026-07-28 — Agent 写完代码，安全扫描要进同一条 loop：Codex Security 把 scan 做成可嵌 CI 的部件
- [HiSkill: Empowering LLM Agents with Hierarchical Skill Graphs](https://arxiv.org/abs/2607.25853) ⭐5 · 2026-07-28 — 技能不能只是文案清单：HiSkill 用层次技能图把高层技能接到 AtomicOp，并显式建模分解与恢复

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 238 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 171 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 97 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 28 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 51 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 35 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 150 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 1588
- 公开展示卡片: 770
- 有全文内容: 686
- 最近 7 天信号: 111
- 输出目录: `dist/`

## 热门标签

`ai-tools`, `llm`, `research`, `openai`, `attention`, `arxiv`, `benchmark`, `google`, `evaluation`, `anthropic`, `optimization`, `claude-code`, `2026`, `coding-agent`, `gemini`, `workflow`, `agent-security`, `agent`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
