# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [Overview of AppFunctions (Android AI)](https://developer.android.com/ai/appfunctions) ⭐4 · 2026-08-22 — Android 16+ 把应用能力注册为 agent 可编排工具的官方机制，移动端 MCP 等价物，Gemini 集成私有预览中
- [DeepSeek 官方文档：deepseek-v4-flash-vision-exp 视觉模型使用指南](https://api-docs.deepseek.com/guides/vision) ⭐4 · 2026-08-22 — DeepSeek 官方 API 文档上线 deepseek-v4-flash-vision-exp 视觉模型：支持图文混合输入，可做图像描述截图文字读取与图表分析.
- [深度拆解：新一代智能体手机的路线之争](https://mp.weixin.qq.com/s?__biz=Mzk0NDcwNTc1OQ%3D%3D&mid=2247483912&idx=1&sn=2282e48602310b1a5829fd8dc9f73867) ⭐4 · 2026-08-21 — 智能体手机三阵营架构对照：Skill 深改 OS MCP 语义原子操作GUI 看屏点击，代价各不相同
- [Why shaming people about AI slop isn't enough to stop Big AI](https://anildash.com/2026/08/21/ai-slop-and-shame) ⭐4 · 2026-08-21 — 羞耻已被 Big AI 定价进获客成本；真正有效的抵制是递上肯定性替代品，而不是更响地骂
- [My agent.md to improve LLM-assisted code quality](https://fabiensanglard.net/agent.md/index.html) ⭐4 · 2026-08-21 — 把每个 session 重复口述的代码风格固化成 agent.md 注入 prompt，并公开全文拿来就用的 agent 协作 playbook
- [体验完 DeepSeek Harness，我打算放弃开发了两年的客户端](https://x.com/sagacity/status/2090327717149618343) ⭐3 · 2026-08-21 — DSH 生态拐点信号：多个独立 ops 在体验后停掉自研客户端转向插件开发，果但强但尚早
- [Which Eviction Policy Should an LLM Cache Use? A Systematic Study Across Workloads, Capacities...](https://arxiv.org/abs/2608.20280) ⭐4 · 2026-08-20 — 用统一协议 (CLEVER) 系统评测语义缓存驱逐策略：FIFO/LRU/LFU/ARC/GDSF/流式 SISO/语义冗余度，覆盖 3 个查询语料 3 种容量 2 种编码器共 18 个设置没有任何策略比 LFU 高出 0.
- [Phantom Gains: Auditing Self-Improvement Against a Measured Null](https://arxiv.org/abs/2608.20290) ⭐4 · 2026-08-20 — 对自我改进评估的方法学审计：三轮 rank-32 LoRA 自训练 (Qwen3-8B) 与走完全相同管线的冻结对照做差分，识别出 7 种测量失效，任何一种在缺少对照时都会反转结论例如单一 greedy decode 的能力账本会把批处理推理伪影当成能力变化...
- [Pandora's AI Model Routing Box: Efficient Allocation with Costly Value Estimation](https://arxiv.org/abs/2608.20316) ⭐4 · 2026-08-20 — 把多专家 LLM 系统该把查询路由给谁形式化为带昂贵检验的经典 Pandora's Box 问题：廉价估计器（嵌入预测）快而噪，精确估计器（带检索/部分推理的微调模型）准而贵在高斯信号模型下推导出闭式 value-of-information 表达式...
- [MidTool: Mid-training Data Synthesis for Agentic Tool Use](https://arxiv.org/abs/2608.20314) ⭐4 · 2026-08-20 — MidTool 是面向 agentic tool use 的 mid-training 开放语料构建管线：融合大规模网页PDF代码数据与来自真实工具 APIMCP 技能文档落地工作流的合成监督...

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 303 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 285 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 147 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 72 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 93 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 68 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 138 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 1942
- 公开展示卡片: 1106
- 有全文内容: 1026
- 最近 7 天信号: 151
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
