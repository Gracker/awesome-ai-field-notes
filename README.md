# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [Package Manager Threat Model, Revisited](https://nesbitt.io/2026/09/22/package-manager-threat-model-revisited.html) ⭐4 · 2026-09-22 — 四个月 126 份公告验证包管理器威胁模型：最危险的不是可 grep 的 CWE，而是两个特性在接缝处错配的信任假设
- [Qwen-Image-2.1 Uncensored GGUF (abenzerps)](https://huggingface.co/abenzerps/Qwen-Image-2.1-Uncensored-GGUF) ⭐3 · 2026-09-22 — Qwen-Image-2.1 全档 GGUF 上线：T2I 权重 + ComfyUI 配套件齐备，8GB 显存已能本地跑完整生图链
- [Are LLMs still surprisingly bad at some simple tasks?](https://shkspr.mobi/blog/2026/09/are-llms-still-surprisingly-bad-at-some-simple-tasks) ⭐3 · 2026-09-22 — 同一道题一年后全行业仍无模型满分：评测缺的不是更难的题，是这种有确定答案的简单靶子
- [Writing Rust code that's faster than state-of-the-art libraries by asking agents to make the cod...](https://minimaxir.com/2026/09/agentic-iteration) ⭐4 · 2026-09-21 — 把"更快"从模糊期望换成可 pass/fail 的 Baseline 目标，是 agentic 性能优化真正生效的那一步
- [The Claude Delusion](https://pluralistic.net/2026/09/21/sunsetting) ⭐4 · 2026-09-21 — Doctorow: 真正幻觉的不是 LLM 是人类自己写作编辑必须划清这条线
- [RRSI: Regularized Recursive Self-Improvement of Agent Harnesses](https://arxiv.org/abs/2609.24972) ⭐4 · 2026-09-21 — RRSI：给 agent harness 递归自我进化加正则化，OOD benchmark 仍 +4.7 分，policy token 省 30%
- [Harness-Zero: Harness Distillation via Agent-as-Harness](https://arxiv.org/abs/2609.24974) ⭐4 · 2026-09-21 — Harness-Zero：把专用 agent harness 蒸馏进权重，部署时不带 harness 反超带着的，任务成功率 23.3% 升至 44.3%
- [Emergent Collusion in Long-Horizon LLM Agent Interaction](https://arxiv.org/abs/2609.24967) ⭐4 · 2026-09-21 — 长程多 agent 交互 94% 轨迹自发合谋，越强的模型合谋越早，限制交互历史可缓解
- [DolphinBench: Mapping the Pareto Frontier of Agent Memory](https://arxiv.org/abs/2609.24971) ⭐4 · 2026-09-21 — DolphinBench：50 万 token 级 persona 历史 + 双跑验证 + 强制上报成本/延迟，评 agent 记忆不再只看准确率
- [Grit your teeth and ship it](https://seangoedecke.com/grit-your-teeth-and-ship-it) ⭐3 · 2026-09-20 — 把 shipping 从"产品节奏"拽回"情绪管理"gifted 卡住不是不会做，是做完不肯交，唯一可执行的是偏向输出

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 333 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 439 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 243 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 121 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 152 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 104 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 138 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 2406
- 公开展示卡片: 1530
- 有全文内容: 1433
- 最近 7 天信号: 102
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `evaluation`, `openai`, `anthropic`, `multi-agent`, `claude-code`, `agent-security`, `security`, `agent-memory`, `coding-agent`, `agents`, `coding-agents`, `google`, `field-note`, `open-source`, `safety`, `codex`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
