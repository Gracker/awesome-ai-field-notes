# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [DeepInfer: High-performance inference framework for DeepSeek models](https://github.com/deepseek-ai/DeepInfer) ⭐5 · 2026-10-20 — DeepSeek 把生产级推理栈开源：优化内核置信度调度验证批不变与确定性采样一整套
- [Battle Drones: a vibe coded RTS with audio-based multiplayer](https://simonwillison.net/2026/Oct/20/battledrones) ⭐5 · 2026-10-20 — vibe coding 全过程档案：一句让它好玩得多加通宵多 agent 迭代，把 1200 场自对弈的僵局率从 14% 压到 0.9%
- [Voxtral 3: Voice Agent SDK & Speech Models in 50+ Languages](https://mistral.ai/news/voxtral-3) ⭐4 · 2026-10-20 — 语音 agent 进到下一层：50+ 语言实时对话里直接长出工具调用
- [Pluralistic: The death of history's most successful publisher](https://pluralistic.net/2026/10/20/main-character-syndrome) ⭐4 · 2026-10-20 — AI Overviews 的零点击让出版商两头流失：流量没了，30 年长尾还成了模型的免费结构化输入
- [NixOS is making me less afraid](https://entropicthoughts.com/nixos-is-making-me-less-afraid) ⭐4 · 2026-10-20 — 9 行 Nix 配置把敢不敢开新项目的成本结构改写：业余项目多死在维护，搭建很少是瓶颈
- [Laypeople support technical fields for technology, not art](https://seangoedecke.com/laypeople-support-technical-fields-for-technology-not-art) ⭐4 · 2026-10-20 — 公众支持编程靠的是技术成果链，不是艺术性一篇自己拆自己台的辩护文
- [Introducing tsrs: a Port of TypeScript to Rust](https://blog.cloudflare.com/typescript-rust-port) ⭐4 · 2026-10-20 — tsc 的 Rust 移植把维护交给 agent 流水线：每天审上游 diff每晚重跑兼容矩阵，重写成本塌了之后约束是跟住上游
- [DeepSeek deep-sixed at all US federal civilian agencies](https://www.theregister.com/security/2026/10/20/deepseek-deep-sixed-at-all-us-federal-civilian-agencies/5304010) ⭐4 · 2026-10-20 — developed using DeepSeek没定义：一纸排除令把 AI 网关的默认路由问题摆上台面
- [ClickHouse Will Let You Be Wrong at Scale](https://matduggan.com/clickhouse-will-let-you-be-wrong-at-scale) ⭐4 · 2026-10-20 — ClickHouse 的失败模式是不报错只变慢：同一答案的读取行数可以差 84 倍，护栏与 query_log 是底线
- [AI Had Better Work Out](https://www.wheresyoured.at/ai-had-better-work-out) ⭐4 · 2026-10-20 — AI 泡沫账的可核对版本：九家占纳指 100 近半，数据中心美元债占比一年从 16% 到 25%

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 423 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 568 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 303 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 173 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 215 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 131 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 289 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 2830
- 公开展示卡片: 2102
- 有全文内容: 2000
- 最近 7 天信号: 99
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `openai`, `evaluation`, `anthropic`, `multi-agent`, `agent-security`, `claude-code`, `security`, `coding-agents`, `agents`, `agent-memory`, `coding-agent`, `agent-harness`, `safety`, `prompt-injection`, `agent-safety`, `mcp`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
