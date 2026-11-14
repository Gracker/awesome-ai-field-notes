# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [First Strike](https://geohot.github.io//blog/jekyll/update/2026/11/13/first-strike.html) ⭐3 · 2026-11-13 — 把电力当 AI 能力的约束条件算地缘：卖芯片换电厂是长策，ASI 先发制人被认真讨论本身才是最坏的信号
- [A More Predictable Release Cycle for MCP](https://blog.modelcontextprotocol.io/posts/mcp-release-cycle) ⭐3 · 2026-11-13 — MCP 有了可排期的冻结点：一年两版2027-03-30 打头，未就绪提案顺延不拖版server 作者把迁移从跟规范变成排期
- [Claude Code v2.1.323: experimental Code Mode and plugin.json engines version ranges](https://github.com/anthropics/claude-code/releases/tag/v2.1.323) ⭐4 · 2026-11-12 — 编码 agent 的工具调用开始换形状：Code Mode 用 JS 批量调工具插件生态第一次有版本区间门槛，升级前先核对插件兼容与后台会话归属
- [Apple Foundation Models framework: native Swift API for on-device and Private Cloud Compute LLMs](https://developer.apple.com/foundation-models-framework) ⭐4 · 2026-11-12 — Apple 开发者页系统介绍 Foundation Models framework：原生 Swift API，可在应用内使用任意大模型，包括直连设备端 Apple 基础模型与 Private Cloud Compute.
- [Top Chinese Frontier AI Models Carry the Fingerprint of Export-Controlled NVIDIA Blackwell GPUs](https://unemploymentlabs.com/checkpoint-forensics) ⭐4 · 2026-11-12 — Unemployment Labs（Will DePue，2026-11-12）发布权重取证分析：完全基于公开模型权重而非爆料，通过恢复模型初始值痕迹并搜索可复现它的硬件配置...
- [NVIDIA Announces CEO Transition](https://nvidianews.nvidia.com/news/nvidia-announces-ceo-transition) ⭐4 · 2026-11-12 — NVIDIA 董事会宣布（2026-11-12）：Jensen Huang 即刻辞去总裁CEO 及董事职务；CFO Colette Kress 出任临时 CEO，Harvey C.
- [Introducing Gemini 4 Hydrogen](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen) ⭐4 · 2026-11-12 — Google 发布 Gemini 4 Hydrogen（2026-11-12），定位 Gemini 4 家族的日常快速档：Carbon 与 Argon 负责深度长程推理，Hydrogen 面向 agentic workflow 与日常编码高速执行.
- [ChatGPT Desktop can forward your local SSH agent to remote machines (~217 points)](https://news.ycombinator.com/item?id=50422628) ⭐4 · 2026-11-12 — HN 帖（约 217 分79 评）：为减少确认弹窗，ChatGPT Desktop 可能把本机 SSH agent 转发到远程机器.
- [Anthropic's Initial Public Offering](https://ipo.anthropic.com/us) ⭐4 · 2026-11-12 — Anthropic 上线 IPO 官方站点：以公益公司（PBC）定位自述，附创始人信路演视频财务亮点客户名单申购参与方式与文件 FAQ披露的 2026 Q3 财务：营收 170 亿美元（同比超 12 倍），TTM 收入超 10 万美元客户超 11900 家（同比超 12 倍）.....
- [Metal Sandbox: Isolated Execution and Command Scheduling for GPU Coding Agents on Apple Silicon](https://arxiv.org/abs/2611.17294) ⭐4 · 2026-11-12 — Metal Sandbox 解决 Apple Silicon 上 GPU kernel 生成 agent 的训练/评测基建问题：agent 会话在模型请求开发命令GPU 执行间交替，GPU 大部分时间闲置方案给每个 agent 独立工作区受限文件访问和原生命令执行...

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 527 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 711 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 379 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 227 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 274 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 150 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 244 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 3287
- 公开展示卡片: 2512
- 有全文内容: 2389
- 最近 7 天信号: 211
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `openai`, `evaluation`, `claude-code`, `anthropic`, `multi-agent`, `agent-security`, `coding-agents`, `agents`, `security`, `agent-memory`, `coding-agent`, `kv-cache`, `open-weights`, `mcp`, `codex`, `agent-harness`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
