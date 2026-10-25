# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [Introducing Kimi K3.1 Pro](https://www.kimi.ai/blog/kimi-k3-1-pro) ⭐4 · 2026-10-24 — Kimi K3.1 Pro：最强 3T 级开源权重模型，1M 上下文；开源版主动清除网络攻击数据，攻击能力被刻意压到前沿之下
- [Claude Duet: proactive agent research preview powered by Opus 5.5](https://claude.com/product/claude-duet) ⭐4 · 2026-10-23 — Claude Duet 研究预览：早晨简报加消息派活，云端自己持续干活，敏感操作先审批，Opus 5.5 驱动
- [Software is slow because of bad design, not slow languages](https://seangoedecke.com/software-is-slow-because-of-bad-design-not-slow-languages) ⭐4 · 2026-10-23 — 软件慢在设计不在语言：让 agent profile 找热点改设计，比翻译成 Rust 有用
- [RMSNorm](https://www.gilesthomas.com/2026/10/rmsnorm) ⭐4 · 2026-10-23 — RMSNorm 省 3d-1 次加减只快 2.5%，大头是融合 kernel 的 10-11%
- [One Small Bug](https://nesbitt.io/2026/10/23/one-small-bug.html) ⭐4 · 2026-10-23 — Claude Code 自审仓库挖出 Miri 缓存泄密与 .claude/settings.json 注入，作者结论是先收回 agent 提交权
- [Kimi K3.1 Pro: Simon Willison's first look at pricing and benchmarks](https://simonwillison.net/2026/Oct/23/kimi-k31-pro) ⭐4 · 2026-10-23 — Kimi K3.1 Pro API 首测：$2/$10 定价对齐 GPT-6.1 Sol，AA 55 分为开放权重模型新高
- [TorchTPU: PyTorch backend for Google TPUs (google-pytorch/torch_tpu)](https://github.com/google-pytorch/torch_tpu) ⭐3 · 2026-10-23 — Google 官方开源 PyTorch TPU 后端：ATen kernel 加 XLA 编译缓存加 torch.compile，训练/推理栈开源竞争再加一子
- [AudioScript: local real-time bilingual captions with sherpa-onnx](https://x.com/GitHub_Daily/status/2113601349330055221) ⭐3 · 2026-10-23 — AudioScript：sherpa-onnx+CTranslate2 全本机双语字幕，稳态 70ms 但冷启动 2 秒超预算
- [EpiSEM-Bench: Evaluating Safety and Evidence Recovery in LLM Agents under Missing Evidence](https://arxiv.org/abs/2610.31650) ⭐4 · 2026-10-22 — 证据缺失让"每句都真"的代理照样执行禁令动作：300 对任务的可执行基准测安全边界与证据恢复，十模型差异显著
- [Causal Chain of Thought: Mitigating Attention Leakage via Context Isolation](https://arxiv.org/abs/2610.31639) ⭐4 · 2026-10-22 — CoT 解释可能是事后合理化：把推理拆成隔离上下文的 DAG每节点只看因果父节点，因果敏感度 +12~21pp

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 436 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 584 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 310 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 185 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 222 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 133 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 289 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 2887
- 公开展示卡片: 2159
- 有全文内容: 2052
- 最近 7 天信号: 129
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `openai`, `evaluation`, `anthropic`, `multi-agent`, `agent-security`, `claude-code`, `security`, `coding-agents`, `agents`, `agent-memory`, `coding-agent`, `prompt-injection`, `agent-harness`, `agent-safety`, `kv-cache`, `safety`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
