# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [融合eBPF与AI技术的微架构能效分析](https://mp.weixin.qq.com/s?__biz=MzI3NzA5MzUxNA%3D%3D&mid=2664620532&idx=1&sn=ac6637ded8c26a15f729d8b4ae26d87a) ⭐4 · 2026-05-06 — 小米用 eBPF+AI+6 Agent 闭环做移动端微架构能效分析，Task 级功耗归因+自动因果链推理，短视频场景 CPU 功耗降 15-20%
- [Boris Cherny：Claude Code 之后，写代码正在变成管理 Agent](https://mp.weixin.qq.com/s?__biz=Mzk1NzgxMjQ0OA%3D%3D&mid=2247494723&idx=1&sn=7aa816280ecdd6fdf8338b41081a6f03) ⭐4 · 2026-05-06 — Claude Code 创建者 Boris Cherny 自曝 2026 年零手写代码日合并 150 PR，用 Loop 模式让 Agent 全自动运维，真正的护城河在组织流程改造而非技术
- [用龙虾等 Agent 访问知识星球](https://mp.weixin.qq.com/s?__biz=Mzg5NDY4ODM1MA%3D%3D&mid=2247486078&idx=1&sn=cb5170477c39569acdec51bf2d14e04d) ⭐3 · 2026-05-06 — 知识星球推出官方 AI Skill，npm 安装后 Agent 可查内容搜帖子出报告，权限由星主控制默认关闭
- [imsg CLI 0.6+0.7：iMessage 私有 API 桥接器正式落地](https://x.com/steipete/status/2051905175355351440) ⭐5 · 2026-05-05 — iMessage 私有 API CLI 面世，OpenClaw 生态再添利器
- [AI 产品原型生成提示词：3 层上下文框架（功能 + 视觉 + 数据）](https://x.com/petergyang/status/2051306144199737508) ⭐3 · 2026-05-05 — 目前最实用的 AI 原型生成提示词模板，三层结构有效避免 slop 感
- [AI 五层蛋糕：从能源到应用，构建全栈者将定义下一个工业时代](https://x.com/nvidia/status/2051419469180981439) ⭐3 · 2026-05-05 — 理解 AI 产业竞争格局的最佳框架，底层才是真正价值所在
- [MCP-Flow: 自动构建大规模 MCP 工具数据集，让 0.6B 模型在工具调用上超越 GPT-4o](https://arxiv.org/abs/2510.24284) ⭐4 · 2026-05-04 — 0.6B 小模型微调后在 MCP 工具调用上全面超越 GPT-4o，证明小模型+数据工程才是正确方向
- [Greg Brockman 详解 Codex 验证创业想法的 Skill](https://x.com/gdb/status/2050972114077843772) ⭐4 · 2026-05-04 — Codex Skill：用AI压力测试创业想法，快速暴露核心假设漏洞
- [Supercharging LLM inference on Google TPUs: Achieving 3X speedups with diffusion-style speculati...](https://developers.googleblog.com/supercharging-llm-inference-on-google-tpus-achieving-3x-speedups-with-diffusion-style-speculative-decoding/) ⭐4 · 2026-05-04 — DFlash 块扩散推测解码将 TPU LLM 推理速度提升 3 倍，验证成本近乎恒定，瓶颈转向草稿质量
- [Google Gemini Embedding 2 多模态嵌入模型](https://x.com/GoogleAI/status/2049903687016063456) ⭐5 · 2026-05-03 — Google原生多模态嵌入模型：支持视频和视觉分析

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 111 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 145 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 166 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 31 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 41 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 47 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 42 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 909
- 公开展示卡片: 583
- 有全文内容: 497
- 最近 7 天信号: 108
- 输出目录: `dist/`

## 热门标签

`agent`, `llm`, `claude`, `ai-tools`, `openclaw`, `coding`, `paper`, `openai`, `reasoning`, `claude-code`, `mcp`, `codex`, `multi-agent`, `memory`, `anthropic`, `workflow`, `Agent`, `prompt`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
