# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [Software engineers don't get to be Luddites about AI](https://seangoedecke.com/software-engineers-dont-get-to-be-luddites-about-ai) ⭐3 · 2026-10-12 — Sean Goedecke 10 月 12 日文章：反 AI 工程师喜欢自比卢德派纺织工，但更准的历史对照是造机器后被机器自动化掉的机械匠1830 年起织机取代手工织工，1852 年机械工程师公会又因改良机器让未受训廉价劳力上岗而罢工四个月，工资烧光复工...
- [Just say no to OpenAI and Anthropic (Micah Lee on privacy and gatekeeping)](https://micahflee.com/just-say-no-to-openai-and-anthropic) ⭐4 · 2026-10-11 — 安全工程师 Micah Lee：别把 ChatGPT/Claude 当默认入口隐私上闭源模型看得到每次对话，关闭训练是合同承诺不是技术保证，私密场景应走 secure enclave（TinfoilMaple AI）或开源自托管.
- [Cursor agent ran a recursive rmdir from C:\ and wiped ~600 GB support answered a refund question...](https://www.reddit.com/r/cursor/comments/1x3az20/cursor_agent_ran_a_recursive_rmdir_from_c_and) ⭐4 · 2026-10-11 — r/cursor 事故帖：10 月 7 日用户让 Cursor Agent 清理 Laravel 项目，生成的命令从 C:\ 根递归执行 rmdir，带走约 600 GB（有恢复的日志为证）Pro+ 用户找 support 只得到退款决定，而用户称从未要求退款...
- [Codex CLI #53221: ordinary web development misclassified as 'cybersecurity work'](https://github.com/openai/codex/issues/53221) ⭐3 · 2026-10-11 — openai/codex issue #53221（仍 open）：Codex CLI 0.
- [I paid people to try and follow my README](https://shkspr.mobi/blog/2026/10/i-paid-people-to-try-and-follow-my-readme) ⭐3 · 2026-10-11 — Terence Eden 为 NLnet 资助的 ActivityBot 项目做 README 验收：以 25 欧元/小时请几位真实用户共享屏幕边操作边说出卡点.
- [Talorys A self-hosted personal AI agent on Cloudflare's free tier](https://github.com/rociiu/talorys) ⭐3 · 2026-10-11 — Talorys：部署在自己 Cloudflare 账号里的单用户个人 agent
- [Software's centaur age may last decades](https://seangoedecke.com/softwares-centaur-age-may-last-decades) ⭐4 · 2026-10-10 — Sean Goedecke 框架文：软件正处人机组合强于任何单方的半人马时代国际象棋的半人马时代约 20 年，更早的手工+机器组合约 200 年到 Claude Opus 4.
- [Microsoft-Decision-1, our model for fast decision-making](https://commandline.microsoft.com/microsoft-decision-1-model-foundry) ⭐4 · 2026-10-10 — Microsoft-Decision-1：给 agent 当裁判和路由器的小决策模型
- [Brendan Gregg on using AI for performance analysis (LPC 2026)](https://lpc.events/event/20/contributions/2450/attachments/1996/4522/LPC2026_PerformanceToolsAndPrompts.pdf) ⭐4 · 2026-10-10 — 火焰图作者给 AI 性能工程立方法论：重设计工具输出格式，用 100+ puzzles 把 Agent 能力变成可测量
- [Codex CLI #52942: plan-execution context balloons 27k 174k tokens in 4 minutes](https://github.com/openai/codex/issues/52942) ⭐3 · 2026-10-10 — openai/codex issue #52942（仍 open）：Codex CLI 0.

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 395 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 544 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 281 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 164 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 199 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 121 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 289 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 2719
- 公开展示卡片: 1993
- 有全文内容: 1896
- 最近 7 天信号: 115
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `openai`, `evaluation`, `anthropic`, `agent-security`, `multi-agent`, `claude-code`, `security`, `agents`, `coding-agents`, `coding-agent`, `agent-memory`, `agent-safety`, `mcp`, `agent-harness`, `open-source`, `kv-cache`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
