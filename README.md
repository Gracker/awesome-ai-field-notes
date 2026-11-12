# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [ChatGPT Desktop can forward your local SSH agent to remote machines (~217 points)](https://news.ycombinator.com/item?id=50422628) ⭐4 · 2026-11-12 — HN 帖（约 217 分79 评）：为减少确认弹窗，ChatGPT Desktop 可能把本机 SSH agent 转发到远程机器.
- [HN thread claims OpenAI silently re-enables model training on Codex chats (~535 points)](https://news.ycombinator.com/item?id=50352757) ⭐3 · 2026-11-12 — HN 帖（约 535 分163 评）称 OpenAI 似乎在静默重开 Codex 对话的模型训练评论中 u/chriskanan 说自己过去关过训练请求也批过，后来发现又被打开；其他人建议签 ZDR开高级账号安全锁死分享或自建推理.
- [Claude Code 2.1.322 users report stray copyright reminders from a botched system prompt](https://www.reddit.com/r/ClaudeCode/comments/1xssfs1/21322_anthropics_copyright_paranoia_is_leaking) ⭐3 · 2026-11-12 — r/ClaudeCode 帖（约 565 赞92 评）：升到 Claude Code 2.
- [ChatGPT and Codex now draw on a shared usage allowance (~236 points on HN)](https://news.ycombinator.com/item?id=50320588) ⭐3 · 2026-11-12 — OpenAI Help 文与 HN 讨论（约 236 分175 评）确认 Chat 与 Codex 走同一套用量额度（allowance）评论抱怨 token 定义不透明（u/jwr）.
- [Introducing AlphaProof Code: a breakthrough in verifying complex software at depth](https://deepmind.google/blog/introducing-alphaproof-code) ⭐5 · 2026-11-11 — DeepMind AlphaProof Code 形式化验证 Signal 协议代码：600 万行 Lean，四周完成
- [Gemini Decisions API: Fast, calibrated multimodal decisions](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api) ⭐5 · 2026-11-11 — Google 推出 Gemini Decisions API，由新模型 gemini-decision-1 驱动，面向封闭集决策原语：工具选择策略检查模型路由上下文分级单次多模态输入（文本/图像/音频/视频/PDF...
- [T3 Code metering parity: 1.6-1.7x 5h burn traced to entrypoint, fix landed in v0.1.7, docs still...](https://github.com/pingdotgg/t3code) ⭐4 · 2026-11-11 — T3 Code 是 MIT 协议的多 harness 编排控制面（自带订阅）社区实测同 workload 下 Claude 5h 烧速约为直连 TUI 的 1.
- [United Airlines bans AI agents from booking flights on behalf of travelers](https://www.cbsnews.com/news/united-airlines-bans-ai-agents-booking-flights) ⭐4 · 2026-11-11 — 美联航宣布禁止第三方个人 AI agent 代旅客订票：共享账户凭证（含支付信息）会暴露敏感数据可能造成误购改账户或误用里程，且 agent 代办值机等操作可能违反联邦规定（如行李需旅客本人当面确认无违禁品）美联航在自有数字平台并经旅行社与聚合渠道限制未授权 AI agent.
- [Codex 0.167.2 makes incremental tool updates the default on Google Cloud Vertex](https://github.com/openai/codex/releases/tag/rust-v0.167.2) ⭐3 · 2026-11-11 — openai/codex 在 11-11 把 Latest 从 0.
- [PSA: Fable on Pro consumes limits about 4x faster than Opus](https://www.reddit.com/r/ClaudeCode/comments/1xt1eo1/psa_for_pro_users_trying_fable_this_week_it_uses) ⭐3 · 2026-11-11 — Pro 试 Fable 额度消耗约 4x Opus：per-token 便宜不等于任务账单便宜

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 519 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 701 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 374 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 222 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 266 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 147 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 244 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 3248
- 公开展示卡片: 2473
- 有全文内容: 2357
- 最近 7 天信号: 192
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `openai`, `evaluation`, `claude-code`, `anthropic`, `multi-agent`, `agent-security`, `coding-agents`, `agents`, `security`, `agent-memory`, `coding-agent`, `kv-cache`, `agent-harness`, `open-weights`, `codex`, `mcp`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
