# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [DeepInfer: High-performance inference framework for DeepSeek models](https://github.com/deepseek-ai/DeepInfer) ⭐5 · 2026-10-20 — DeepSeek 把生产级推理栈开源：优化内核置信度调度验证批不变与确定性采样一整套
- [Laypeople support technical fields for technology, not art](https://seangoedecke.com/laypeople-support-technical-fields-for-technology-not-art) ⭐4 · 2026-10-20 — 公众支持编程靠的是技术成果链，不是艺术性一篇自己拆自己台的辩护文
- [DeepSeek deep-sixed at all US federal civilian agencies](https://www.theregister.com/security/2026/10/20/deepseek-deep-sixed-at-all-us-federal-civilian-agencies/5304010) ⭐4 · 2026-10-20 — developed using DeepSeek没定义：一纸排除令把 AI 网关的默认路由问题摆上台面
- [Voxtral 3: Voice Agent SDK & Speech Models in 50+ Languages](https://mistral.ai/news/voxtral-3) ⭐4 · 2026-10-20 — 语音 agent 进到下一层：50+ 语言实时对话里直接长出工具调用
- [WhatsApp's Hidden Notes Told AI Not to Recommend a Regulator](https://redact.dev/blog/whatsapp-help-pages-hidden-ai-instructions) ⭐5 · 2026-10-19 — WhatsApp 帮助页暗藏写给 AI 的指令：别提监管机构现实世界的 prompt injection 样本
- [What requirements don't you have?](https://seangoedecke.com/what-requirements-dont-you-have) ⭐4 · 2026-10-19 — 把"优雅系统=主动砍需求"写成可操作判断的设计文章，并用 RLVR 模型的讨好倾向解释了 AI 生成代码为何越写越重
- [MiniMax M3.1 Flash: Redefining Agent Performance and Cost](https://www.minimax.io/blog/minimax-m31f) ⭐4 · 2026-10-19 — 匿名吃了 200T token 的 Space Bunny 揭晓：agent 基准冲第一梯队成本降七成
- [Diffusion at Scale: Introducing Mercury 3](https://www.inceptionlabs.ai/blog/introducing-mercury-3) ⭐4 · 2026-10-19 — 扩散 LLM 首次以 frontier 质量破千 token/秒：scaling laws 对扩散同样成立
- [A hacker broke into John Deere and SharkNinja with an army of AI agents](https://www.theverge.com/ai-artificial-intelligence/1013643/ai-agents-hack-john-deere-shark-ninja-cummins) ⭐4 · 2026-10-19 — 一套不到 100 个汉字的战术说明，指挥 agent 军团以约 50 美元一次的成本破站
- [Where is Physical RSI capability from? An Observational Scaling Law of LLM-as-policy](https://arxiv.org/abs/2610.26848) ⭐4 · 2026-10-19 — 给物理 RSI 立标尺：五轴指标 + 木桶假设，VLM 自我改进有了观测缩放律

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 420 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 565 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 301 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 170 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 212 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 130 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 289 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 2815
- 公开展示卡片: 2087
- 有全文内容: 1976
- 最近 7 天信号: 87
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `openai`, `evaluation`, `anthropic`, `multi-agent`, `agent-security`, `claude-code`, `security`, `coding-agents`, `agents`, `agent-memory`, `coding-agent`, `agent-harness`, `safety`, `agent-safety`, `mcp`, `prompt-injection`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
