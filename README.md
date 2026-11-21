# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [Why output caching doesn't work](https://seangoedecke.com/why-output-caching-doesnt-work) ⭐4 · 2026-11-21 — 把缓存输出的收益上限算成个位数百分比，顺带解释了强模型为什么总账更便宜做 token 选型直接可用
- [Vibecoding an inference chip](https://ankitg.me/blog/vibecoding-inference-chip) ⭐4 · 2026-11-21 — Codex智能体在AWS F2 FPGA上搭出Qwen风格MoE推理，实测6.43->213 tokens/s
- [Re: Riemann](https://borretti.me/article/re-riemann) ⭐4 · 2026-11-21 — 与其说是数学新闻，不如说是一份研究者被自己工具超越的第一人称证词证明未经独立验证，先当立场文献读
- [Introducing Frostbite: A new CPU architecture discovered, designed, and verified end-to-end by A...](https://architectlabs.com/blog/frostbite) ⭐4 · 2026-11-21 — Architect Labs的AI零先验端到端设计出interaction nets ISA的通用CPU Frostbite
- [Inkling 2 Mini: a fast, powerful model that runs on your laptop](https://thinkingmachines.ai/news/inkling-2-mini) ⭐4 · 2026-11-21 — Thinking Machines发布Inkling 2 Mini：循环中间层的26.4B MoE，开放权重可本地跑
- [Combatting adversarial distillation](https://openai.com/index/combatting-adversarial-distillation) ⭐4 · 2026-11-20 — 54.0%0.2% 的提取成功率是自家红队自测数字，工程细节（tool-call 参数覆盖推理绑定会话）比结论更可复用
- [Codex CLI 0.171.0: GPT-6.2 Sol becomes default, TUI workspace on by default](https://github.com/openai/codex/releases/tag/rust-v0.171.0) ⭐3 · 2026-11-20 — 默认模型与默认 UI 信息架构同时切换的版本升级后审批面和上下文可见性都会变，值得升级前后各截一张默认项
- [Claude Code v2.1.330: Enterprise Admin Console sign-in and easel](https://github.com/anthropics/claude-code/releases/tag/v2.1.330) ⭐3 · 2026-11-20 — 企业 admin 登录与本地 hooks/CLAUDE.md 的冲突面第一次被官方串起来managed settings 的优先级坑值得先读文档再升级
- [What is the Generalized Riemann Hypothesis?](https://www.johndcook.com/blog/2026/11/20/grh) ⭐3 · 2026-11-20 — 给当天的 AI 证明声明配上强度阶梯：RH 只是 GRH 取常数特征的特例，读声明前先看这篇
- [Token fraud is here and it's BAD (YouTube)](https://simonwillison.net/2026/Nov/20/token-fraud-is-here-and-its-bad) ⭐3 · 2026-11-20 — 免费额度变成可倒卖商品的直接后果：关掉试用层，而盗用提示词顺手成了模型指纹的采样源

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 568 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 754 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 412 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 242 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 301 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 153 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 244 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 3450
- 公开展示卡片: 2674
- 有全文内容: 2552
- 最近 7 天信号: 177
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `openai`, `evaluation`, `claude-code`, `anthropic`, `multi-agent`, `agents`, `agent-security`, `coding-agents`, `security`, `agent-memory`, `kv-cache`, `mcp`, `coding-agent`, `open-weights`, `codex`, `prompt-injection`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
