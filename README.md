# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [深度拆解：新一代智能体手机的路线之争](https://mp.weixin.qq.com/s?__biz=Mzk0NDcwNTc1OQ%3D%3D&mid=2247483912&idx=1&sn=2282e48602310b1a5829fd8dc9f73867) ⭐4 · 2026-08-21 — 智能体手机三阵营架构对照：Skill 深改 OS MCP 语义原子操作GUI 看屏点击，代价各不相同
- [体验完 DeepSeek Harness，我打算放弃开发了两年的客户端](https://x.com/sagacity/status/2090327717149618343) ⭐3 · 2026-08-21 — DSH 生态拐点信号：多个独立 ops 在体验后停掉自研客户端转向插件开发，果但强但尚早
- [Training a 125M model to autocomplete piano on-device](https://simedw.com/2026/08/20/midi-autocomplete) ⭐4 · 2026-08-20 — 个人项目复盘：125M 参数 transformer 在 iPhone 15 上实时自动补全钢琴演奏（约108 音符/秒），MIDI 表示与数据清洗是关键收益
- [The actual epistemic crisis](https://pluralistic.net/2026/08/20/epistemic-void) ⭐4 · 2026-08-20 — 把 deepfake 危机从技术问题重框为权力结构问题：纯 provenance/水印方案救不了已被企业收购的把关体系
- [Ornith-1.5: From Self-Scaffolding to Self-Improvement](https://ornith.ai/ornith_1_5.html) ⭐4 · 2026-08-20 — 开源模型 Ornith-1.5：自脚手架升级为端到端自我改进循环，397B MoE 智能体与编码基准对标 Claude Opus 4.8
- [Malicious Rust crate arrayref runs a build-time payload](https://safedep.io/arrayref-proc-macro1-rust-build-time-malware) ⭐4 · 2026-08-20 — Rust 供应链实弹：维护者账号被入侵后 yank 旧版强迫升级，arrayref 0.3.10 构建期下载执行二进制，附完整 IoC
- [Huzzah: pseudocode prompts as a persistent alternative to coding-agent chats](https://www.danielvaughn.dev/posts/huzzah) ⭐4 · 2026-08-20 — Show HN 实验性编辑器：用持久化伪代码声明替代易失的命令式长文提示，重建人机意图的中心权威
- [Don't paste the AI, please](https://dontpastetheai.com/) ⭐4 · 2026-08-20 — 被广泛传播的社交礼仪站点：别把未读的 LLM 回答直接粘给提问的人，对方也有同样的工具
- [ChatGPT search now uses the site: operator at scale](https://simonwillison.net/2026/Aug/20/chatgpt-search-now-uses-the-siteoperator-at-scale) ⭐4 · 2026-08-20 — 间接测量揭开 ChatGPT Search 形态变化：site: 占比从 0.5% 跳到 1617%，AI 搜索已是高比例精确筛选的 fanout 工具
- [Cerebras CS-4: rack-scale wafer inference, up to 30x faster than GPUs](https://www.cerebras.ai/cs4) ⭐4 · 2026-08-20 — Cerebras 发布 CS-4：三片 WSE-3 Turbo 机柜级推理系统，宣称比 GPU 快至 30 倍每瓦 10T+ 参数模型 1000+ tokens/s

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 302 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 280 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 145 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 69 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 92 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 66 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 138 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 1928
- 公开展示卡片: 1092
- 有全文内容: 1012
- 最近 7 天信号: 150
- 输出目录: `dist/`

## 热门标签

`llm`, `arxiv`, `ai-tools`, `benchmark`, `research`, `evaluation`, `openai`, `anthropic`, `attention`, `google`, `security`, `coding-agent`, `multi-agent`, `claude-code`, `agent-memory`, `agent-security`, `open-source`, `coding-agents`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
