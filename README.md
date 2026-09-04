# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [GPT-6 Astra 上线门：model idAPI 价目与 computer-use 数字](https://developers.openai.com/api/docs/models/gpt-6-astra) ⭐4 · 2026-09-04 — OpenAI Devs 官方模型页给出 GPT-6 Astra 完整上线路径：model id 为 gpt-6-astra，定价 Input $10 / Output $50 每百万 token，Cached input $1.00Cache writes $12.50...
- [Codex rust-v0.153.2：插件 marketplace断线重连与 Astra Fast 文案修正](https://github.com/openai/codex/releases/tag/rust-v0.153.2) ⭐4 · 2026-09-03 — openai/codex rust-v0.153.2（2026-09-03 23:53 UTC，121.3k stars）的实质功能集中在 v0.153.0：Vim 模式支持 u 撤销与 Ctrl+R 重做并保留粘贴/附件...
- [Claude Code v2.1.260：全屏 diff 旁栏 + prompt-cache miss 原因说明](https://github.com/anthropics/claude-code/releases/tag/v2.1.260) ⭐4 · 2026-09-03 — anthropics/claude-code v2.1.260（2026-09-03 23:48 UTC，144k stars）发布说明要点：全屏模式下 /diff 在对话旁栏打开未提交改动；/cost 与状态行的 prompt_cache 字段会写明缓存 miss 的可能原因....
- [陈梓立：Agentic Coding 时代，什么是核心竞争力？](https://mp.weixin.qq.com/s?__biz=MzA4NTM4NDc4NQ%3D%3D&mid=2247546058&idx=1&sn=29bf169d86c161ec077d20bd862e8d97&chksm=9e047ff25e2c268c3373e60328f3d7587a106da4d2ad7efe3176d943a48fe6011560feebd2ea) ⭐4 · 2026-09-03 — 陈梓立在 KAIYUANSHE 9 月 3 日文章里围绕Agentic Coding 时代什么是核心竞争力给出三条判断：（1）AI 写代码的价值边界取决于模型是否覆盖你的日常工作基线.
- [Google Antigravity ToS：第三方 harness 仍封官方 headless 路径仍开](https://news.ycombinator.com/item?id=49548452) ⭐4 · 2026-09-03 — HN 讨论串 49548452 摘出 Antigravity 现网 ToS 关键句：'Using third party software, tools, or services to access the Service (e.g....
- [SafeEvolve: Harness-Policy Co-Evolution from Agent Experience for Safety Alignment](https://arxiv.org/abs/2609.02786) ⭐4 · 2026-09-02 — 论文指出 LLM Agent 的表现由基座模型与 harness 共同决定，安全风险同时存在于最终回复与多步执行轨迹中...
- [Post-Training Language Models for Gold-Medal Performance in Coding Competitions](https://arxiv.org/abs/2609.02849) ⭐4 · 2026-09-02 — NVIDIA 团队的竞赛编程端到端专精管线：2.
- [Discriminative World Models for Web Agents](https://arxiv.org/abs/2609.02885) ⭐4 · 2026-09-02 — 论文针对网页 Agent 测试时动作选择中的世界模型训练错配问题：现有世界模型用监督式下一状态预测（生成 HTML/AXTree 快照）训练.
- [Run cloud agents on machines you manage Cursor Self-Hosted Machines](https://cursor.com/blog/self-hosted-machines) ⭐4 · 2026-09-02 — Cursor 博文 2026-09-02 推出 Self-Hosted Machines：loop 与推理仍在 Cursor 云端，但 agent 实际执行落在企业自己管理的 worker / 池上.
- [Red Alert: OpenAI is poised to cross an AI safety redline](https://garymarcus.substack.com/p/red-alert-openai-is-poised-to-cross) ⭐4 · 2026-09-02 — Gary Marcus 9 月 2 日就 The Information 当天爆料做的快评：OpenAI 在 Astra 模型里尝试一种叫 "recurrent depth" 的新推理技术，让模型"思维"过程更接近神经隐喻（neuralese）.

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 286 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 352 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 196 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 92 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 122 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 86 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 137 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 2145
- 公开展示卡片: 1271
- 有全文内容: 1184
- 最近 7 天信号: 134
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `evaluation`, `openai`, `anthropic`, `agent-security`, `claude-code`, `security`, `multi-agent`, `agent-memory`, `agents`, `open-source`, `coding-agent`, `google`, `coding-agents`, `llm`, `safety`, `agent-harness`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
