# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [I spent $266 and four AI models to own my Amazon Fire tablet](https://ericpardee.github.io/fire-hd-ownership) ⭐4 · 2026-08-24 — 一位有 20 年从4e1a经验和信息安全背景的工程师，记录从亚马逊手里夺回 Fire HD 10（2021）真正所有权的全部成本：$114 的平板 + $266 的 AI 开支平板被持有 REBOOT/SHUTDOWN 权限的亚马逊服务反复强制关机，禁用受保护包失败.
- [A Syncthing and SQLite Gotcha](https://borretti.me/article/a-syncthing-and-sqlite-gotcha) ⭐4 · 2026-08-23 — rename 只改目录项到 inode 的映射：讲透了文件明明更新长驻进程却读不到的幽灵 bug
- [The New MCP Roadmap](https://blog.modelcontextprotocol.io/posts/mcp-roadmap) ⭐5 · 2026-08-22 — MCP 官方维护者发布新版路线图，盘点 2026-07-28 规范已落地的进展：协议层 session 与初始化握手已移除，服务端可无状态横向扩展（SEP-2575/2567）；客户端可先调 server/discover 了解版本与能力；列表结果可缓存（SEP-2549）...
- [Overview of AppFunctions (Android AI)](https://developer.android.com/ai/appfunctions) ⭐4 · 2026-08-22 — Android 16+ 把应用能力注册为 agent 可编排工具的官方机制，移动端 MCP 等价物，Gemini 集成私有预览中
- [DeepSeek 官方文档：deepseek-v4-flash-vision-exp 视觉模型使用指南](https://api-docs.deepseek.com/guides/vision) ⭐4 · 2026-08-22 — DeepSeek 官方 API 文档上线 deepseek-v4-flash-vision-exp 视觉模型：支持图文混合输入，可做图像描述截图文字读取与图表分析.
- [More than just code review](https://simonwillison.net/2026/Aug/22/more-than-just-code-review) ⭐3 · 2026-08-22 — agent 时代的核心技能：自信下达指令，再自信验证落地；逐行人审只是手段之一
- [A quote from Linus Torvalds](https://simonwillison.net/2026/Aug/22/linus-torvalds) ⭐3 · 2026-08-22 — 一线内核调试实录：AI 多次说无解，被倔强的人类推着继续干到了底
- [深度拆解：新一代智能体手机的路线之争](https://mp.weixin.qq.com/s?__biz=Mzk0NDcwNTc1OQ%3D%3D&mid=2247483912&idx=1&sn=2282e48602310b1a5829fd8dc9f73867) ⭐4 · 2026-08-21 — 智能体手机三阵营架构对照：Skill 深改 OS MCP 语义原子操作GUI 看屏点击，代价各不相同
- [Why shaming people about AI slop isn't enough to stop Big AI](https://anildash.com/2026/08/21/ai-slop-and-shame) ⭐4 · 2026-08-21 — 羞耻已被 Big AI 定价进获客成本；真正有效的抵制是递上肯定性替代品，而不是更响地骂
- [My agent.md to improve LLM-assisted code quality](https://fabiensanglard.net/agent.md/index.html) ⭐4 · 2026-08-21 — 把每个 session 重复口述的代码风格固化成 agent.md 注入 prompt，并公开全文拿来就用的 agent 协作 playbook

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 243 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 290 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 154 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 74 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 95 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 70 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 128 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 1959
- 公开展示卡片: 1054
- 有全文内容: 973
- 最近 7 天信号: 113
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
