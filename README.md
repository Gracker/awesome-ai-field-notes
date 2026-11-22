# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [Why output caching doesn't work](https://seangoedecke.com/why-output-caching-doesnt-work) ⭐4 · 2026-11-21 — 把缓存输出的收益上限算成个位数百分比，顺带解释了强模型为什么总账更便宜做 token 选型直接可用
- [Vibecoding an inference chip](https://ankitg.me/blog/vibecoding-inference-chip) ⭐4 · 2026-11-21 — Codex智能体在AWS F2 FPGA上搭出Qwen风格MoE推理，实测6.43->213 tokens/s
- [Re: Riemann](https://borretti.me/article/re-riemann) ⭐4 · 2026-11-21 — 与其说是数学新闻，不如说是一份研究者被自己工具超越的第一人称证词证明未经独立验证，先当立场文献读
- [Lean/Mathlib communities certify Alpge's 17M-line Riemann Hypothesis proof](https://leanprover-community.github.io/blog/posts/riemann-hypothesis) ⭐4 · 2026-11-21 — 1700 万行 Lean 库通过陈述/编译/对应性/内核四条独立标准拿到社区认证，AI 协作但未裁定比例
- [Introducing Frostbite: A new CPU architecture discovered, designed, and verified end-to-end by A...](https://architectlabs.com/blog/frostbite) ⭐4 · 2026-11-21 — Architect Labs的AI零先验端到端设计出interaction nets ISA的通用CPU Frostbite
- [Inkling 2 Mini: a fast, powerful model that runs on your laptop](https://thinkingmachines.ai/news/inkling-2-mini) ⭐4 · 2026-11-21 — Thinking Machines发布Inkling 2 Mini：循环中间层的26.4B MoE，开放权重可本地跑
- [宝玉解读 Anthropic 代码审查分享：事故当考题50 轮教训与风险分级](https://x.com/dotey/status/2123555597387813050) ⭐4 · 2026-11-20 — 比原文博客多出三块实操：事故 PR 当考题建评测50 轮跑飞的收敛教训按改动而非作者定签字人数
- [House report: Cursor plans to explore phasing out PRC open-weight models](https://www.cnbc.com/2026/11/20/cursor-chinese-ai-models-geopolitical-risk.html) ⭐4 · 2026-11-20 — explore 是政策建议不是 changelog：Composer 2 的 Kimi 底座与第三方模型表要分层看
- [Combatting adversarial distillation](https://openai.com/index/combatting-adversarial-distillation) ⭐4 · 2026-11-20 — 54.0%0.2% 的提取成功率是自家红队自测数字，工程细节（tool-call 参数覆盖推理绑定会话）比结论更可复用
- [Codex CLI 0.171.0: GPT-6.2 Sol becomes default, TUI workspace on by default](https://github.com/openai/codex/releases/tag/rust-v0.171.0) ⭐3 · 2026-11-20 — 默认模型与默认 UI 信息架构同时切换的版本升级后审批面和上下文可见性都会变，值得升级前后各截一张默认项

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 571 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 758 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 415 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 245 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 302 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 153 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 244 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 3464
- 公开展示卡片: 2688
- 有全文内容: 2566
- 最近 7 天信号: 191
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `openai`, `evaluation`, `claude-code`, `anthropic`, `agents`, `multi-agent`, `agent-security`, `coding-agents`, `security`, `agent-memory`, `kv-cache`, `mcp`, `coding-agent`, `open-weights`, `agent-safety`, `codex`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
