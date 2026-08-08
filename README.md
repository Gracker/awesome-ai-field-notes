# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [My LLM coding workflow going into 2026](https://addyosmani.com/blog/ai-coding-workflow) ⭐5 · 2026-08-07 — AI 编码越强，规格上下文测试和责任边界越要前置
- [TencentDB Agent Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) ⭐4 · 2026-08-07 — 团队级 agent 记忆的核心是把经验治理成可复用资产
- [Introducing Agent Plugins](https://vercel.com/blog/introducing-agent-plugins) ⭐5 · 2026-08-06 — Agent Plugins 把 Skills 和 MCP 的可移植部分收敛到一个最小包格式
- [How Compiler Explorer Runs on AWS in 2026](https://xania.org/202608/how-compiler-explorer-runs-on-aws) ⭐4 · 2026-08-06 — 公共开发者工具如何低成本可靠运行，Godbolt 给了可复查数字和取舍
- [Atlassian Rovo Exfiltrates Data, Bypassing Controls](https://www.promptarmor.com/resources/atlassian-rovo-exfiltrates-data) ⭐4 · 2026-08-06 — 关闭搜索不等于切断外泄路径，agent 工具面必须按真实数据流建模
- [A year of AI disclosure in critical packages](https://nesbitt.io/2026/08/06/a-year-of-ai-disclosure-in-critical-packages.html) ⭐4 · 2026-08-06 — 把开源里的 AI 参与率从体感变成可复查的 commit 级统计
- [Argus: A General-Purpose Agentic Runtime for Long-Horizon Reasoning](https://arxiv.org/abs/2608.05144) ⭐5 · 2026-08-05 — 长程 agent 的核心不只是模型，而是可验证可累积的运行时状态
- [Toward Skill-Native LLMs: Skill Entropy for Benchmarking and Training Long-Horizon Reasoning](https://arxiv.org/abs/2608.05139) ⭐4 · 2026-08-05 — 长程推理的难点在于技能切换，而不只是单项能力
- [OctoLong: Mid-Training On Cross-Repository Code Contexts Enhances Long-Context Modeling](https://arxiv.org/abs/2608.05141) ⭐4 · 2026-08-05 — 代码 agent 的长上下文能力，需要跨仓库依赖语料来训练
- [DeepSeek V4 Flash on a single AMD MI300X](https://github.com/ryanzhou/deepseek-v4-flash-mi300x) ⭐4 · 2026-08-05 — 这类部署仓库有价值，因为它把 ROCm/vLLM/FP8/KV cache 的生产配置和坑点都摊开了

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 252 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 222 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 121 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 42 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 61 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 43 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 150 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 1710
- 公开展示卡片: 891
- 有全文内容: 804
- 最近 7 天信号: 119
- 输出目录: `dist/`

## 热门标签

`llm`, `ai-tools`, `research`, `benchmark`, `evaluation`, `openai`, `arxiv`, `attention`, `anthropic`, `google`, `optimization`, `agent-security`, `claude-code`, `security`, `coding-agents`, `coding-agent`, `2026`, `agent-memory`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
