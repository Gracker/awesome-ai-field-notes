# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [I spent $266 and four AI models to own my Amazon Fire tablet](https://ericpardee.github.io/fire-hd-ownership) ⭐4 · 2026-08-24 — 一位有 20 年从4e1a经验和信息安全背景的工程师，记录从亚马逊手里夺回 Fire HD 10（2021）真正所有权的全部成本：$114 的平板 + $266 的 AI 开支平板被持有 REBOOT/SHUTDOWN 权限的亚马逊服务反复强制关机，禁用受保护包失败.
- [Armin Ronacher: Anger, Anxiety and Agency](https://lucumr.pocoo.org/2026/8/24/anger-anxiety-agency) ⭐4 · 2026-08-24 — 焦虑是可以保留的生产性状态，愤怒是常错位的代理信号
- [The summer of open weights: 够用的智能以十分之一价格普及](https://martinalderson.com/posts/the-summer-of-open-weights) ⭐4 · 2026-08-23 — agentic 编码不再离不开 frontier 智能，token 效率成了新的竞争力维度
- [Jerry Liu: two-pass document processing is the default for agent harnesses](https://x.com/jerryjliu0/status/2091564183922077885) ⭐4 · 2026-08-23 — 一程优化 recall 二程优化 precision，全量 VLM OCR 是最贵的错误默认
- [Drew Breunig: Fable & The End of the Free Lunch](https://www.dbreunig.com/2026/08/23/fable-the-end-of-moore-s-law.html) ⭐4 · 2026-08-23 — agentic coder 经济学从 all-in frontier 切换到按成本质量路由的拐点
- [A Syncthing and SQLite Gotcha](https://borretti.me/article/a-syncthing-and-sqlite-gotcha) ⭐4 · 2026-08-23 — rename 只改目录项到 inode 的映射：讲透了文件明明更新长驻进程却读不到的幽灵 bug
- [The New MCP Roadmap](https://blog.modelcontextprotocol.io/posts/mcp-roadmap) ⭐5 · 2026-08-22 — MCP 官方维护者发布新版路线图，盘点 2026-07-28 规范已落地的进展：协议层 session 与初始化握手已移除，服务端可无状态横向扩展（SEP-2575/2567）；客户端可先调 server/discover 了解版本与能力；列表结果可缓存（SEP-2549）...
- [Overview of AppFunctions (Android AI)](https://developer.android.com/ai/appfunctions) ⭐4 · 2026-08-22 — Android 16+ 把应用能力注册为 agent 可编排工具的官方机制，移动端 MCP 等价物，Gemini 集成私有预览中
- [DeepSeek 官方文档：deepseek-v4-flash-vision-exp 视觉模型使用指南](https://api-docs.deepseek.com/guides/vision) ⭐4 · 2026-08-22 — DeepSeek 官方 API 文档上线 deepseek-v4-flash-vision-exp 视觉模型：支持图文混合输入，可做图像描述截图文字读取与图表分析.
- [Armin Ronacher: Fast and Hard Code](https://lucumr.pocoo.org/2026/8/22/fast-hard-code) ⭐4 · 2026-08-22 — 语言学习摩擦被抹平后，快且小的技术栈叙事重新赢得开发者

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 243 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 294 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 156 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 75 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 97 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 71 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 128 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 1969
- 公开展示卡片: 1064
- 有全文内容: 983
- 最近 7 天信号: 123
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `evaluation`, `openai`, `anthropic`, `security`, `google`, `multi-agent`, `claude-code`, `coding-agent`, `agent-memory`, `agent-security`, `coding-agents`, `llm-agents`, `mcp`, `llm`, `open-source`, `agents`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
