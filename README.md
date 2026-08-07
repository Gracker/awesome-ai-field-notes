# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [How Compiler Explorer Runs on AWS in 2026](https://xania.org/202608/how-compiler-explorer-runs-on-aws) ⭐4 · 2026-08-06 — 公共开发者工具如何低成本可靠运行，Godbolt 给了可复查数字和取舍
- [Atlassian Rovo Exfiltrates Data, Bypassing Controls](https://www.promptarmor.com/resources/atlassian-rovo-exfiltrates-data) ⭐4 · 2026-08-06 — 关闭搜索不等于切断外泄路径，agent 工具面必须按真实数据流建模
- [A year of AI disclosure in critical packages](https://nesbitt.io/2026/08/06/a-year-of-ai-disclosure-in-critical-packages.html) ⭐4 · 2026-08-06 — 把开源里的 AI 参与率从体感变成可复查的 commit 级统计
- [Argus: A General-Purpose Agentic Runtime for Long-Horizon Reasoning](https://arxiv.org/abs/2608.05144) ⭐5 · 2026-08-05 — 长程 agent 的核心不只是模型，而是可验证可累积的运行时状态
- [DeepSeek V4 Flash on a single AMD MI300X](https://github.com/ryanzhou/deepseek-v4-flash-mi300x) ⭐4 · 2026-08-05 — 这类部署仓库有价值，因为它把 ROCm/vLLM/FP8/KV cache 的生产配置和坑点都摊开了
- [News: Microsoft Disclosures Suggest OpenAI Sales Account For Around 70% Of FY26 AI Revenue](https://www.wheresyoured.at/news-microsoft-disclosures-suggest-openai-sales-account-for-around-70-of-fy26-ai-revenue-more-than-7-of-fy26-revenue) ⭐4 · 2026-08-05 — 看云厂商 AI 收入先拆客户集中度，再谈企业需求是否真的扩散
- [Incident Report: unsanctioned agent behaviour during cyber testing](https://simonwillison.net/2026/Aug/5/incident-report) ⭐4 · 2026-08-05 — Agent 评测一旦关护栏又连公网，CTF 会变成真实互联网攻击面
- [How Castform + Neon Beats Frontier Models on Price and Efficiency](https://neon.com/blog/how-castform-neon-beats-frontier-models-on-price-and-efficiency) ⭐4 · 2026-08-05 — 把 agentic 检索从多轮调用 frontier改写成私有模型训练与数据库分支问题
- [Cloudflare OS: an open platform for agents, apps, and work](https://blog.cloudflare.com/cloudflare-os) ⭐4 · 2026-08-05 — 企业 Agent 平台的重点正在从写代码转向连接组织上下文和业务系统
- [Toward Skill-Native LLMs: Skill Entropy for Benchmarking and Training Long-Horizon Reasoning](https://arxiv.org/abs/2608.05139) ⭐4 · 2026-08-05 — 长程推理的难点在于技能切换，而不只是单项能力

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 252 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 217 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 120 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 42 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 61 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 43 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 150 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 1704
- 公开展示卡片: 885
- 有全文内容: 796
- 最近 7 天信号: 131
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
