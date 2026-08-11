# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [Shared Code Between Package Managers](https://nesbitt.io/2026/08/11/package-manager-library-reuse.html) ⭐4 · 2026-08-11 — 包管理器最大的攻击面,是它们都在复用同一批解析器
- [The bureaucratic AI arms-race is mutually assured destruction](https://pluralistic.net/2026/08/10/deep-state-wopr) ⭐5 · 2026-08-10 — 当服务系统主要优化反欺诈，它就不再是服务系统，而是拒付系统
- [Muse Glimmer: 30B Open Agentic Model for Local Agent Workflows](https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model) ⭐5 · 2026-08-10 — Meta 超级智能实验室发布 Muse Glimmer，一个 300 亿参数的开源模型 (Apache 2.
- [Addy Osmani 2026 LLM coding workflow: spec-first, chunked, human-supervised](https://x.com/yibie/status/2085536770758996033) ⭐5 · 2026-08-10 — 模型越能写代码，人的规格上下文和审查越不能省
- [Needle 2: 14MB Agentic LLM for Phones, Wearables, and Microcontrollers](https://cactuscompute.com/needle) ⭐4 · 2026-08-10 — Needle 2 是一个 45M 参数的代理型 LLM，通过从预训练开始的 2-bit Cactus Quants 量化压缩至 14MB，面向低于 200 美元的边缘设备（手机可穿戴树莓派微控制器）采用 Simple Attention Network 架构...
- [Watch out for cache read costs](https://martinalderson.com/posts/watch-out-for-cache-read-costs) ⭐4 · 2026-08-10 — agent 长上下文的真账单在缓存读取,不在输入输出
- [Open-source is NOT the same as open-weight](https://garymarcus.substack.com/p/open-source-is-not-the-same-as-open) ⭐4 · 2026-08-10 — open-weight 是发蛋糕不开配方,开源才给整条流水线
- [Humanising LLM Outputs is Dumb](https://kuber.studio/blog/Reflections/Humanising-LLM-Outputs-is-Actually-Dumb) ⭐4 · 2026-08-10 — agent 之间传散文案,等于把排错信息先压一遍
- [Docker Sandboxes: Sandboxes for Coding Agents](https://www.docker.com/products/docker-sandboxes) ⭐4 · 2026-08-10 — agent 隔离从权限判断挪到运行环境,代价是启动 microVM
- [Ante: Ghost in your shell](https://github.com/AntigmaLabs/ante) ⭐4 · 2026-08-10 — 15MB Rust 单文件 coding agent,资源占用比 Claude Code 低一个数量级

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 259 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 231 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 128 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 47 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 65 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 48 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 150 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 1748
- 公开展示卡片: 928
- 有全文内容: 844
- 最近 7 天信号: 75
- 输出目录: `dist/`

## 热门标签

`llm`, `ai-tools`, `research`, `benchmark`, `arxiv`, `evaluation`, `openai`, `attention`, `anthropic`, `google`, `coding-agent`, `claude-code`, `coding-agents`, `security`, `optimization`, `agent-security`, `agent-memory`, `2026`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
