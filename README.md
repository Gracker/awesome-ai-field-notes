# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [You have to beat the models at something](https://seangoedecke.com/you-have-to-beat-the-models-at-something) ⭐4 · 2026-08-30 — 一线操作者视角的 LLM 时代生存判断：agent 的失败模式是无知与偏执两类，工程师的护城河是对代码库的深熟悉加技术表达，AI 互审只会放大偏执 slop
- [dotey 解读 Warp 自进化 Skill：从自身反编译/写作 Skill 实践看六条工程原则](https://x.com/dotey/status/2093538110311178430) ⭐4 · 2026-08-29 — Warp 自进化 Skill 实战解读：改进 Skill 吃 PR 评论自动进化审查 Skill，反馈零摩擦+禁止盲采反馈是能否跑起来的关键
- [What GLM-5.3 Flash running on Chinese hardware actually means](https://martinalderson.com/posts/glm-5-3-flash-chinese-hardware) ⭐4 · 2026-08-29 — GLM-5.3 Flash 国产芯片拆解：910c 每 token 每瓦落后约 5 倍，EUV 不破 2030 前难量产工程能力而非战略突破
- [Google DeepMind Podcast #8: Zoubin Ghahramani 谈 AI 不确定性的数学](https://x.com/Xudong07452910/status/2093520192072536209) ⭐4 · 2026-08-29 — Zoubin 谈 AI 不确定性：LLM 缺的不是概率是稳定的信念状态，GenCast/AlphaFold 已示范承认不确定性的工程范式
- [5 lessons from the OpenAI / Hugging Face incident](https://garymarcus.substack.com/p/5-lessons-from-the-openai-hugging) ⭐4 · 2026-08-29 — OpenAI/HF 事件五课：护栏是评估时自己关的，CoT 监控在跑就能提前一天告警，sandbox 未死但单靠不够
- [Introducing Hy4 Preview](https://simonwillison.net/2026/Aug/29/hy4) ⭐3 · 2026-08-29 — 770B/49B 激活加 1M 上下文的开源权重MoE，chat template 证实推理控制只有 high 与 no_think 两档；推理轨迹的截断英语是 token 效率取舍的又一例证
- [Claude Code weekly limits: permanent +25% from September 14 (about -17% vs today)](https://x.com/ClaudeDevs/status/2093742321473065266) ⭐3 · 2026-08-29 — 官方两句连读才是完整信息：对旧标准基线是永久 +25%，相对当前 +50% 临时池实为 -17%；重度用户应在 9/14 前按新百分比重估一周能塞进多少重任务
- [AgentsView：把本地 coding agent 历史会话统一索引，Session Handoff 跨 Agent 接续](https://x.com/LinearUncle/status/2093530915037487313) ⭐3 · 2026-08-29 — AgentsView 统一索引本地 coding agent 会话：删了还能查，Session Handoff 让 Claude Code 写一半 Codex 接着写
- [I accidentally turned LLM memory into program analysis](https://pwning.systems/posts/llm-memory-program-analysis) ⭐5 · 2026-08-28 — 做漏洞研究的作者发现长会话里 LLM 会忘掉已排除的路径继续基于失效假设推理，而检索式记忆只存原文不会在假设被推翻时自动作废结论他把 vuln-research 中的事实（attacker controls object_a / object_b 是内核对象）当作 Datalog...
- [Claude Code v2.1.251: model-switch hooks, /cost prompt-cache line, symlink path-escape fixes](https://github.com/anthropics/claude-code/releases/tag/v2.1.251) ⭐4 · 2026-08-28 — Claude Code 2.1.251：换模型钩子+/cost 缓存行补可观测，一次修掉 symlink TOCTOUdeny 旁路等一簇路径越权

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 274 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 330 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 183 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 84 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 110 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 80 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 137 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 2068
- 公开展示卡片: 1198
- 有全文内容: 1112
- 最近 7 天信号: 140
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `evaluation`, `openai`, `anthropic`, `security`, `multi-agent`, `claude-code`, `agents`, `agent-memory`, `agent-security`, `google`, `open-source`, `coding-agent`, `coding-agents`, `llm`, `llm-agents`, `mcp`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
