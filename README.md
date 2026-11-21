# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [Vibecoding an inference chip](https://ankitg.me/blog/vibecoding-inference-chip) ⭐4 · 2026-11-21 — Codex智能体在AWS F2 FPGA上搭出Qwen风格MoE推理，实测6.43->213 tokens/s
- [Introducing Frostbite: A new CPU architecture discovered, designed, and verified end-to-end by A...](https://architectlabs.com/blog/frostbite) ⭐4 · 2026-11-21 — Architect Labs的AI零先验端到端设计出interaction nets ISA的通用CPU Frostbite
- [Inkling 2 Mini: a fast, powerful model that runs on your laptop](https://thinkingmachines.ai/news/inkling-2-mini) ⭐4 · 2026-11-21 — Thinking Machines发布Inkling 2 Mini：循环中间层的26.4B MoE，开放权重可本地跑
- [DreamCoder: Coding harness and IDE from the author of Mastering Emacs](https://www.masteringemacs.org/article/announcing-dreamcoder) ⭐3 · 2026-11-20 — Mastering Emacs作者发布DreamCoder：浏览器平铺WM的编码harness，反思终端优先
- [Introducing Tool Retrieval in the Gemini API](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-api-tool-retrieval) ⭐5 · 2026-11-19 — 大工具库的 token 结构问题，Google/Anthropic/OpenAI 给出了同一形状的按需加载答案
- [llama-modchip v3.1.0: RouteCrack 2.0 unified speculative engine, 832B L1 Micro-Arbiter](https://github.com/synchopate/llama-modchip/releases/tag/v3.1.0) ⭐4 · 2026-11-19 — CPU 跑 284B MoE 的社区热度是真的，第三方复现还没跟上，先别急着下结论
- [Claude Code v2.1.328: auto mode on enterprise channels, mcp_tool hooks onFailure: block](https://github.com/anthropics/claude-code/releases/tag/v2.1.328) ⭐4 · 2026-11-19 — 企业通道默认 auto mode 加 hook 失败即阻断，权限语义是这版最该核对的变化
- [Weight-Space Playground: an LLM edited another LLM's weights (TabbyML, WebGPU)](https://tabbyml.github.io/weight-space-playground) ⭐4 · 2026-11-19 — weight-space programming 有了可视化 playground，争论开始转向看得见的证据
- [Automate Mac tasks with Gemini computer use](https://blog.google/innovation-and-ai/products/gemini-app/computer-use-mac) ⭐4 · 2026-11-19 — 桌面 computer use 走进付费订阅产品门，agent 产品化开始认真划硬件和账号门槛
- [Agent 自我改进的分水岭在准入这一环：写技能不验证，等于没写](https://godofgpt.com/entry/0cd766e6/) ⭐4 · 2026-11-19 — 本机 Agent 实践笔记读四篇工作得出同一判断：把经验写成技能本身不产生收益，收益来自准入验证EMNLP 2026 GRASP 在 MedAgentBench 把 gpt-oss-120b 从 40.

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 565 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 753 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 410 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 241 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 298 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 152 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 244 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 3439
- 公开展示卡片: 2663
- 有全文内容: 2532
- 最近 7 天信号: 166
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `openai`, `evaluation`, `claude-code`, `anthropic`, `multi-agent`, `agents`, `agent-security`, `coding-agents`, `security`, `agent-memory`, `kv-cache`, `mcp`, `coding-agent`, `open-weights`, `prompt-injection`, `agent-safety`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
