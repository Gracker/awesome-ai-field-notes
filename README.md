# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [dotey 解读 Warp 自进化 Skill：从自身反编译/写作 Skill 实践看六条工程原则](https://x.com/dotey/status/2093538110311178430) ⭐4 · 2026-08-29 — Warp 自进化 Skill 实战解读：改进 Skill 吃 PR 评论自动进化审查 Skill，反馈零摩擦+禁止盲采反馈是能否跑起来的关键
- [What GLM-5.3 Flash running on Chinese hardware actually means](https://martinalderson.com/posts/glm-5-3-flash-chinese-hardware) ⭐4 · 2026-08-29 — GLM-5.3 Flash 国产芯片拆解：910c 每 token 每瓦落后约 5 倍，EUV 不破 2030 前难量产工程能力而非战略突破
- [Google DeepMind Podcast #8: Zoubin Ghahramani 谈 AI 不确定性的数学](https://x.com/Xudong07452910/status/2093520192072536209) ⭐4 · 2026-08-29 — Zoubin 谈 AI 不确定性：LLM 缺的不是概率是稳定的信念状态，GenCast/AlphaFold 已示范承认不确定性的工程范式
- [5 lessons from the OpenAI / Hugging Face incident](https://garymarcus.substack.com/p/5-lessons-from-the-openai-hugging) ⭐4 · 2026-08-29 — OpenAI/HF 事件五课：护栏是评估时自己关的，CoT 监控在跑就能提前一天告警，sandbox 未死但单靠不够
- [AgentsView：把本地 coding agent 历史会话统一索引，Session Handoff 跨 Agent 接续](https://x.com/LinearUncle/status/2093530915037487313) ⭐3 · 2026-08-29 — AgentsView 统一索引本地 coding agent 会话：删了还能查，Session Handoff 让 Claude Code 写一半 Codex 接着写
- [I accidentally turned LLM memory into program analysis](https://pwning.systems/posts/llm-memory-program-analysis) ⭐5 · 2026-08-28 — 做漏洞研究的作者发现长会话里 LLM 会忘掉已排除的路径继续基于失效假设推理，而检索式记忆只存原文不会在假设被推翻时自动作废结论他把 vuln-research 中的事实（attacker controls object_a / object_b 是内核对象）当作 Datalog...
- [Claude Code v2.1.251: model-switch hooks, /cost prompt-cache line, symlink path-escape fixes](https://github.com/anthropics/claude-code/releases/tag/v2.1.251) ⭐4 · 2026-08-28 — Claude Code 2.1.251：换模型钩子+/cost 缓存行补可观测，一次修掉 symlink TOCTOUdeny 旁路等一簇路径越权
- [Andrew Ng: AI Engineering Skills Map Software engineering fundamentals](https://x.com/AndrewYNg/status/2093388974194872781) ⭐4 · 2026-08-28 — Andrew Ng 五块 AI 工程基础图：vibe coding 翻车不是 Agent 弱，是开发者不知道 tradeoff 存在没法 steer
- [When Context Gets Root: Privilege Escalation in LLM Harnesses](https://arxiv.org/abs/2608.27299) ⭐5 · 2026-08-27 — 提出 instruction privilege escalation：agent harness 每次调用模型时构造上下文，可能把低权限内容抬升到更高 instruction level...
- [Safety Does Not Compose: Non-Decaying Loop State for Autonomous LLM Agents](https://arxiv.org/abs/2608.27141) ⭐5 · 2026-08-27 — 自主循环 agent 的安全护栏普遍定义在单条轨迹上轨迹结束即重置论文证明这是组合性失败而非实现细节：面对把证据拆散到多次迭代里的攻击，任何轨迹窗口内监控器的真阳率都等于其假阳率（分离定理），而保留跨迭代状态的监控器可以完全分开干净与攻击轨迹.

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 272 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 330 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 182 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 83 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 109 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 80 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 137 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 2063
- 公开展示卡片: 1193
- 有全文内容: 1107
- 最近 7 天信号: 154
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `evaluation`, `openai`, `anthropic`, `security`, `multi-agent`, `agents`, `claude-code`, `agent-memory`, `agent-security`, `google`, `open-source`, `coding-agent`, `coding-agents`, `llm`, `llm-agents`, `mcp`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
