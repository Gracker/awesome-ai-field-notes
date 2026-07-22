# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [OpenAI and Hugging Face partner to address security incident during model evaluation](https://openai.com/index/hugging-face-model-evaluation-security-incident) ⭐5 · 2026-07-21 — OpenAI 披露：在关闭生产级网络攻击拒答的内部网安能力评测中，含 GPT-5.
- [git --end-of-options 背后的参数注入安全边界](https://nesbitt.io/2026/07/21/end-of-options.html) ⭐4 · 2026-07-21 — 包装 Git 的安全边界不能只靠 --，不可信 ref 要显式结束选项解析
- [Graph Engineering：Agent 执行图工程的旧内核新名字与建模边界](https://godofgpt.com/entry/80df7c07/) ⭐4 · 2026-07-21 — 把 Agent 连成图之前，先说明箭头语义状态契约和终止条件
- [Kimi K3 is competitive with Fable; Kimi K3 + Fable is SoTA](https://fireworks.ai/blog/kimik3-fable) ⭐4 · 2026-07-21 — Fireworks 在约 1030 个真实 agent 任务（SWE终端运维算法多语言法律等）上对比开源 Kimi K3 与闭源 Fable 5：二者路由约 93% 准确率，长 agent 环上最高可比单用 Fable 便宜约 50.
- [LLMs and Agentic AI Systems for Smart Grids: A Tutorial on Architectures and Applications](https://arxiv.org/abs/2607.18147) ⭐5 · 2026-07-20 — 智能电网场景下的 LLM/agent 教程：主张 solver-grounded 原则数值结果须来自可信工具并通过显式校验才可上报...
- [Automated Discovery Has No Universally Superior Harness](https://arxiv.org/abs/2607.18235) ⭐5 · 2026-07-20 — 系统分解 OpenEvolve/TTT-Discover 类自动发现 harness，在 12 组模型-问题对超 310 万次 LLM rollout 上评估 30 种预算对齐变体，发现没有固定 harness 能跨设置稳定领先，OpenEvolve 变体整体常弱于更简单方案.
- [Whos Afraid of Chinese Models?](https://stratechery.com/2026/whos-afraid-of-chinese-models) ⭐4 · 2026-07-20 — 评估 AI 模型竞争时，比 token 标价更该看完整系统的智能成本
- [The biggest MCP spec update ships July 28: What changes for AI agent authentication](https://workos.com/blog/mcp-2026-spec-agent-authentication) ⭐4 · 2026-07-20 — MCP 新规范的方向是少隐藏 session，多显式状态标准授权和网关可治理性
- [Rewriting Bun in Rust](https://bun.com/blog/bun-in-rust) ⭐4 · 2026-07-20 — Bun 迁 Rust 是生产级 coding agent 工程样板，重点在审查和失败回收
- [Overtraining as the path to human-like AI](https://seangoedecke.com/overtraining-as-the-path-to-human-like-ai) ⭐4 · 2026-07-20 — Overtraining 路线的争议点不在口号，而在用长训练赌更深层泛化

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 222 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 115 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 71 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 16 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 39 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 28 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 150 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 1459
- 公开展示卡片: 641
- 有全文内容: 549
- 最近 7 天信号: 23
- 输出目录: `dist/`

## 热门标签

`ai-tools`, `llm`, `research`, `openai`, `attention`, `google`, `anthropic`, `optimization`, `2026`, `arxiv`, `gemini`, `claude-code`, `agent`, `digest`, `evaluation`, `benchmark`, `论文工具`, `security`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
