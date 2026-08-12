# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [Nvidia's Risky Business](https://stratechery.com/2026/nvidias-risky-business) ⭐5 · 2026-08-12 — 把 1873 年铁路泡沫和今天的 AI 资本支出摆在一起：算力已经从产品变成可证券化的资产类别
- [Don't Look Up AI 泡沫的下一站](https://www.wheresyoured.at/dont-look-up) ⭐5 · 2026-08-12 — UBS / Wells / Barclays / Deutsche 数据同向：70%-90% 算力收入靠 VC 为 Anthropic / OpenAI 续命
- [Pluralistic: Model collapse Temperature Zero for Culture](https://pluralistic.net/2026/08/12/insurance-value-of-biodiversity) ⭐4 · 2026-08-12 — 把 model collapse = performativity = placelessness 三个词压成同一个机制，让非 AI 读者也能拿走
- [OTel Isn't Going Well (And I Made A Spreadsheet About It)](https://matduggan.com/otel-isnt-going-well-and-i-made-a-spreadsheet-about-it) ⭐4 · 2026-08-12 — 把 OTel 进度慢从感觉变成证据：binary stability gate + 极大 scope + 极少 maintainer 三件套共振
- [I Put GitHub Copilot Behind a MITM Proxy. Here's What I Found](https://www.lighthousenewsletter.com/p/i-put-github-copilot-behind-a-mitm) ⭐4 · 2026-08-12 — 在 VS Code 启动阶段用 mitmproxy 抓出 Copilot 完整 OAuth / 模型发现 / MCP / repo context 请求矩阵
- [Google Search Is Dying. What Comes Next Is Worse](https://thewalrus.ca/google-search-is-dying) ⭐4 · 2026-08-12 — AI overview + 链接腐烂 + Reddit 投毒 + Internet Archive 败诉串成一条公共记忆基础设施塌方链
- [Apple Silicon and macOS VMs: 11-16x Faster LLM Inference with llama.cpp](https://github.com/trycua/cua/blob/main/blog/gpu-passthrough-macos-vms.md) ⭐4 · 2026-08-12 — macOS guest 里加一层 Metal shim 让 llama.cpp 走对路径：吞吐追到裸金属 99%
- [Modular 26.5: Mojo 1.0 is here](https://www.modular.com/blog/modular-26-5-mojo-1-0-is-here) ⭐3 · 2026-08-12 — Mojo 1.0 把多套并立语法收敛到 var / Pointer / 统一定义 lambda，并首次承诺向后兼容
- [Stolen Thoughts: Decoded Reasoning Traces From Frontier LLMs](https://stolen-thoughts.com/) ⭐5 · 2026-08-11 — 直接解码出来的 GPT-5 / Claude Opus 4.7 / Sonnet 4.6 推理痕迹，把对齐失效论文压成可读目录
- [Shared Code Between Package Managers](https://nesbitt.io/2026/08/11/package-manager-library-reuse.html) ⭐4 · 2026-08-11 — 包管理器最大的攻击面,是它们都在复用同一批解析器

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 265 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 234 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 128 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 51 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 71 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 48 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 150 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 1767
- 公开展示卡片: 947
- 有全文内容: 863
- 最近 7 天信号: 92
- 输出目录: `dist/`

## 热门标签

`llm`, `ai-tools`, `research`, `benchmark`, `arxiv`, `evaluation`, `openai`, `attention`, `anthropic`, `google`, `security`, `coding-agent`, `claude-code`, `coding-agents`, `optimization`, `agent-security`, `agent-memory`, `2026`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
