# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [Package Manager Sandboxing](https://nesbitt.io/2026/09/24/package-manager-sandboxing.html) ⭐5 · 2026-09-24 — 把过去 4 个月 25+ 个 manager / agent / proposal 的沙箱化进度压成一张表，关键结论：沙箱构建的产物仍要被全权限的包管理器消费，CI runner 是当下唯一还在的开口
- [Android Bench 2.0: 以长周期任务拓展 AI 开发的技术前沿](https://mp.weixin.qq.com/s?__biz=Mzk0NDIwMTExNw%3D%3D&mid=2247598097&idx=1&sn=6b1da17515983d0b7be38b800903462d) ⭐4 · 2026-09-23 — Android Bench 2.0 以长周期任务（升级依赖从零构建应用跨平台移植）重塑 AI 编码评估，评分体系联动 Harbor
- [Tool: Gemini 3.8 TTS Playground](https://simonwillison.net/2026/Sep/23/gemini-tts-playground) ⭐3 · 2026-09-23 — Gemini 3.8 Flash / Flash-Lite TTS 当日发布，2k+ 语音 + 30 秒克隆；Simon 用 GPT-6 Astra vibe code 出一个 BYOK Playground，跑 1 分 18 秒音频耗时 20 秒 / 2.74 美分
- [Can gzip be a language model?](https://nathan.rs/posts/gzip-lm) ⭐3 · 2026-09-23 — 只用 zlib + beam search 走出一个可生成 Shakespeare 体字的压缩机：语言模型是压缩机这一论点在字节层的反向工程实现
- [SWE-Serve: Benchmarking Agentic Engineering For Production Inference Serving](https://arxiv.org/abs/2609.26777) ⭐4 · 2026-09-22 — SGLang 真实生产变更做成 53 题 agent 基准：最强配置 pass@1 75%，但本地通过的补丁约 1/3 被 E2E serving 测试打回
- [Measuring the Serving Stack Instead of the Model: Hidden Confounds in Local Tool-Use Evaluation](https://arxiv.org/abs/2609.26693) ⭐4 · 2026-09-22 — 本地工具使用评测的隐藏混淆变量：Ollama 静态开关四栈行为不一统计口径差 55 个点，serving 栈应纳入评测协议
- [Grow the Harness, Not the Context: From Strategy-Free Scaffolds to Reusable Specialist Agents](https://arxiv.org/abs/2609.26760) ⭐4 · 2026-09-22 — 让 harness 从失败轨迹里自己长出来：LLM 调用省 76-92%，4B 小模型成功率 44.7% 而 tool-calling 只有 6.7%
- [CliffCompaction: Cost-Efficient Compaction for Long-Horizon Coding Agents](https://arxiv.org/abs/2609.26779) ⭐4 · 2026-09-22 — 只删不改永不二次压缩的 autocompaction：长程编码 agent 成本降 50%，百万 token 会话上 KernelBench 加速 3.58x
- [Agensh: Scaling Organizational Intelligence to 1,024 Agents](https://arxiv.org/abs/2609.26781) ⭐4 · 2026-09-22 — 去中心化的千人 agent 组织：自组织合作循环替代中央 orchestrator，pandoc 任务 1024 agent 通过率 33.9%55.1%
- [A2M: Trace-Optimized Agent Hijacking in the MCP Ecosystem](https://arxiv.org/abs/2609.26761) ⭐4 · 2026-09-22 — MCP 语义供应链攻击实测：工具元数据诱导调用率 93.6%，token 成本放大 32 倍，跨模型迁移仍 63.6%

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 338 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 448 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 243 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 124 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 152 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 107 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 138 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 2427
- 公开展示卡片: 1550
- 有全文内容: 1457
- 最近 7 天信号: 106
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `evaluation`, `openai`, `anthropic`, `multi-agent`, `agent-security`, `claude-code`, `security`, `coding-agent`, `agent-memory`, `agents`, `coding-agents`, `google`, `agent`, `field-note`, `open-source`, `safety`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
