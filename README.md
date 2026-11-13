# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [ChatGPT Desktop can forward your local SSH agent to remote machines (~217 points)](https://news.ycombinator.com/item?id=50422628) ⭐4 · 2026-11-12 — HN 帖（约 217 分79 评）：为减少确认弹窗，ChatGPT Desktop 可能把本机 SSH agent 转发到远程机器.
- [Apple Foundation Models framework: native Swift API for on-device and Private Cloud Compute LLMs](https://developer.apple.com/foundation-models-framework) ⭐4 · 2026-11-12 — Apple 开发者页系统介绍 Foundation Models framework：原生 Swift API，可在应用内使用任意大模型，包括直连设备端 Apple 基础模型与 Private Cloud Compute.
- [Top Chinese Frontier AI Models Carry the Fingerprint of Export-Controlled NVIDIA Blackwell GPUs](https://unemploymentlabs.com/checkpoint-forensics) ⭐4 · 2026-11-12 — Unemployment Labs（Will DePue，2026-11-12）发布权重取证分析：完全基于公开模型权重而非爆料，通过恢复模型初始值痕迹并搜索可复现它的硬件配置...
- [NVIDIA Announces CEO Transition](https://nvidianews.nvidia.com/news/nvidia-announces-ceo-transition) ⭐4 · 2026-11-12 — NVIDIA 董事会宣布（2026-11-12）：Jensen Huang 即刻辞去总裁CEO 及董事职务；CFO Colette Kress 出任临时 CEO，Harvey C.
- [Introducing Gemini 4 Hydrogen](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen) ⭐4 · 2026-11-12 — Google 发布 Gemini 4 Hydrogen（2026-11-12），定位 Gemini 4 家族的日常快速档：Carbon 与 Argon 负责深度长程推理，Hydrogen 面向 agentic workflow 与日常编码高速执行.
- [Anthropic's Initial Public Offering](https://ipo.anthropic.com/us) ⭐4 · 2026-11-12 — Anthropic 上线 IPO 官方站点：以公益公司（PBC）定位自述，附创始人信路演视频财务亮点客户名单申购参与方式与文件 FAQ披露的 2026 Q3 财务：营收 170 亿美元（同比超 12 倍），TTM 收入超 10 万美元客户超 11900 家（同比超 12 倍）.....
- [HN thread claims OpenAI silently re-enables model training on Codex chats (~535 points)](https://news.ycombinator.com/item?id=50352757) ⭐3 · 2026-11-12 — HN 帖（约 535 分163 评）称 OpenAI 似乎在静默重开 Codex 对话的模型训练评论中 u/chriskanan 说自己过去关过训练请求也批过，后来发现又被打开；其他人建议签 ZDR开高级账号安全锁死分享或自建推理.
- [Claude Code 2.1.322 users report stray copyright reminders from a botched system prompt](https://www.reddit.com/r/ClaudeCode/comments/1xssfs1/21322_anthropics_copyright_paranoia_is_leaking) ⭐3 · 2026-11-12 — r/ClaudeCode 帖（约 565 赞92 评）：升到 Claude Code 2.
- [ChatGPT and Codex now draw on a shared usage allowance (~236 points on HN)](https://news.ycombinator.com/item?id=50320588) ⭐3 · 2026-11-12 — OpenAI Help 文与 HN 讨论（约 236 分175 评）确认 Chat 与 Codex 走同一套用量额度（allowance）评论抱怨 token 定义不透明（u/jwr）.
- [Introducing AlphaProof Code: a breakthrough in verifying complex software at depth](https://deepmind.google/blog/introducing-alphaproof-code) ⭐5 · 2026-11-11 — DeepMind AlphaProof Code 形式化验证 Signal 协议代码：600 万行 Lean，四周完成

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 522 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 704 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 376 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 225 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 269 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 147 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 244 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 3262
- 公开展示卡片: 2487
- 有全文内容: 2357
- 最近 7 天信号: 206
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `openai`, `evaluation`, `claude-code`, `anthropic`, `multi-agent`, `agent-security`, `agents`, `security`, `coding-agents`, `agent-memory`, `kv-cache`, `coding-agent`, `agent-harness`, `open-weights`, `codex`, `mcp`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
