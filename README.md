# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [DeepSeek V4 Flash on a single AMD MI300X](https://github.com/ryanzhou/deepseek-v4-flash-mi300x) ⭐4 · 2026-08-05 — 这类部署仓库有价值，因为它把 ROCm/vLLM/FP8/KV cache 的生产配置和坑点都摊开了
- [Keyv and friends compromised in active Shai-Hulud supply chain attack](https://www.aikido.dev/blog/keyv-and-friends-compromised-in-npm-supply-chain-attack) ⭐5 · 2026-08-04 — 这次 npm 事件说明供应链攻击已从单包投毒升级成凭据窃取后的自动传播链
- [Introducing Shieldstral.](https://mistral.ai/news/shieldstral) ⭐4 · 2026-08-04 — Shieldstral 的看点是把 guardrail 从固定分类器变成运行时可改 policy 的二元问答模型
- [brew install actions/checkout](https://nesbitt.io/2026/08/04/brew-install-actions-checkout.html) ⭐4 · 2026-08-04 — 把 GitHub Actions 当包管理器看，才能补上依赖树锁定审查和 attestation
- [New release of LLM adds support for reasoning traces, OpenAI Responses, server-side tools, and s...](https://simonwillison.net/2026/Aug/4/new-release-of-llm) ⭐4 · 2026-08-04 — LLM 0.32 把命令行 LLM 从发 prompt推进到 reasoningtoolsMCP 和日志都可审计的工具层
- [SWE-Touch: Benchmarking Coding Agents When Users Touch the Code](https://arxiv.org/abs/2608.02499) ⭐5 · 2026-08-03 — SWE-Touch benchmarks coding agents under user code edits in shared workspaces.
- [Magnet: Detecting Cross-Session AI Misuse Through Capability Accumulation](https://arxiv.org/abs/2608.02518) ⭐5 · 2026-08-03 — Magnet detects AI misuse assembled across otherwise benign agent sessions.
- [Structured Memory for Edge Language Models: Persistent Context and Corpus Retrieval via O(1) SSM...](https://arxiv.org/abs/2608.02560) ⭐4 · 2026-08-03 — PRECOG injects precomputed SSM states to make edge RAG prefill O(1).
- [RoMeRL: Balancing Feedback Coverage and the Memory-Reward Trap in Self-Evolving Agent Memory via...](https://arxiv.org/abs/2608.02508) ⭐4 · 2026-08-03 — RoMeRL reduces reward contamination in self-evolving agent memory.
- [Right Answer, Wrong Method: Shortcut Hacking Misleads the Evaluation of LLM Reasoning on Frontie...](https://arxiv.org/abs/2608.02442) ⭐4 · 2026-08-03 — 科学推理评测不能只看答案对不对，还要识别模型是否用捷径绕过了目标推导

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 251 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 203 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 115 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 39 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 60 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 42 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 150 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 1679
- 公开展示卡片: 860
- 有全文内容: 776
- 最近 7 天信号: 114
- 输出目录: `dist/`

## 热门标签

`llm`, `ai-tools`, `research`, `benchmark`, `openai`, `arxiv`, `evaluation`, `attention`, `anthropic`, `google`, `optimization`, `coding-agents`, `coding-agent`, `agent-security`, `security`, `claude-code`, `2026`, `agent-memory`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
