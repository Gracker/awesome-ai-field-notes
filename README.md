# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [git --end-of-options 背后的参数注入安全边界](https://nesbitt.io/2026/07/21/end-of-options.html) ⭐4 · 2026-07-21 — 包装 Git 的安全边界不能只靠 --，不可信 ref 要显式结束选项解析
- [Graph Engineering：Agent 执行图工程的旧内核新名字与建模边界](https://godofgpt.com/entry/80df7c07/) ⭐4 · 2026-07-21 — 把 Agent 连成图之前，先说明箭头语义状态契约和终止条件
- [Whos Afraid of Chinese Models?](https://stratechery.com/2026/whos-afraid-of-chinese-models) ⭐4 · 2026-07-20 — 评估 AI 模型竞争时，比 token 标价更该看完整系统的智能成本
- [The biggest MCP spec update ships July 28: What changes for AI agent authentication](https://workos.com/blog/mcp-2026-spec-agent-authentication) ⭐4 · 2026-07-20 — MCP 新规范的方向是少隐藏 session，多显式状态标准授权和网关可治理性
- [Rewriting Bun in Rust](https://bun.com/blog/bun-in-rust) ⭐4 · 2026-07-20 — Bun 迁 Rust 是生产级 coding agent 工程样板，重点在审查和失败回收
- [Overtraining as the path to human-like AI](https://seangoedecke.com/overtraining-as-the-path-to-human-like-ai) ⭐4 · 2026-07-20 — Overtraining 路线的争议点不在口号，而在用长训练赌更深层泛化
- [Coding agents make cheap reverse engineering more worthwhile](https://simonwillison.net/2026/Jul/20/cheap-reverse-engineering) ⭐3 · 2026-07-20 — Coding Agent 的实际冲击之一，是把不值得写的小自动化变成值得试
- [Claude Code uses Bun written in Rust now](https://simonwillison.net/2026/Jul/19/claude-code-in-bun-in-rust) ⭐3 · 2026-07-19 — Agent 工具链的基础设施升级，最好做到用户几乎无感但性能变好
- [AI Mania Is Eviscerating Global Decision-Making](https://ludic.mataroa.blog/blog/ai-mania-is-eviscerating-global-decision-making) ⭐4 · 2026-07-18 — 企业 AI 狂热最危险的地方，是奖励看起来用了 AI而不是真实交付
- [When Does Muon Help Agentic Reinforcement Learning?](https://arxiv.org/abs/2607.16169) ⭐4 · 2026-07-17 — 论文比较 Muon 与 AdamW 在稀疏奖励 agentic RL 后训练中的表现：在 ALFWorld + Qwen2.5-0.5B-Instruct 设置下，Muon 只作用于 hidden weight matrices 时...

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 218 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 111 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 70 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 16 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 39 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 27 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 151 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 1450
- 公开展示卡片: 632
- 有全文内容: 548
- 最近 7 天信号: 15
- 输出目录: `dist/`

## 热门标签

`ai-tools`, `llm`, `research`, `openai`, `attention`, `google`, `anthropic`, `optimization`, `2026`, `gemini`, `claude-code`, `agent`, `digest`, `benchmark`, `论文工具`, `security`, `workflow`, `evaluation`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
