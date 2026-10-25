# God of GPT

> AI 信息导航站 — 每天从 OpenClaw 自动采集的数据中，筛出真正值得看的模型、Agent、AI 编程、基础设施、产品商业和研究信号。

## 最新精选 Top 10

- [Hermes 定时任务一周执行复盘：1001 次运行 89 次失败，故障集中在两个惯犯](https://godofgpt.com/entry/6d0f2633/) ⭐3 · 2026-10-25 — 89 次失败里 67 次来自两个任务：先分清代码错与容量墙，重试才不会越攒越多
- [DeepSeek-V4.1-Flash-1017 八天采用读数：HF 下载 7.3 万点赞 2.8 倍，11-01 起 Search/Fetch 计费](https://api-docs.deepseek.com/quick_start/pricing) ⭐3 · 2026-10-25 — HF 八天读数只量自托管拉权重：下载 07.3 万点赞 10572828；API 侧要等 11-01 Search/Fetch 计费窗开启才见分晓
- [Introducing Kimi K3.1 Pro](https://www.kimi.ai/blog/kimi-k3-1-pro) ⭐4 · 2026-10-24 — Kimi K3.1 Pro：最强 3T 级开源权重模型，1M 上下文；开源版主动清除网络攻击数据，攻击能力被刻意压到前沿之下
- [Claude Duet: proactive agent research preview powered by Opus 5.5](https://claude.com/product/claude-duet) ⭐4 · 2026-10-23 — Claude Duet 研究预览：早晨简报加消息派活，云端自己持续干活，敏感操作先审批，Opus 5.5 驱动
- [Software is slow because of bad design, not slow languages](https://seangoedecke.com/software-is-slow-because-of-bad-design-not-slow-languages) ⭐4 · 2026-10-23 — 软件慢在设计不在语言：让 agent profile 找热点改设计，比翻译成 Rust 有用
- [RMSNorm](https://www.gilesthomas.com/2026/10/rmsnorm) ⭐4 · 2026-10-23 — RMSNorm 省 3d-1 次加减只快 2.5%，大头是融合 kernel 的 10-11%
- [One Small Bug](https://nesbitt.io/2026/10/23/one-small-bug.html) ⭐4 · 2026-10-23 — Claude Code 自审仓库挖出 Miri 缓存泄密与 .claude/settings.json 注入，作者结论是先收回 agent 提交权
- [Kimi K3.1 Pro: Simon Willison's first look at pricing and benchmarks](https://simonwillison.net/2026/Oct/23/kimi-k31-pro) ⭐4 · 2026-10-23 — Kimi K3.1 Pro API 首测：$2/$10 定价对齐 GPT-6.1 Sol，AA 55 分为开放权重模型新高
- [Brotli CVE-2026-111497（Node2ShellHTTP2Shell）：CVSS 9.2 越界写，PyPI 包自动解码即暴露](https://www.aikido.dev/blog/python-packages-vulnerable-node2shell-brotli-cve-2026-111497) ⭐4 · 2026-10-23 — OpenAI 二月修进源码但没有 release 带上：br 自动解码让 urllib3/httpx/aiohttp 装包即暴露，advisory 库至今未映射 PyPI 包
- [TorchTPU: PyTorch backend for Google TPUs (google-pytorch/torch_tpu)](https://github.com/google-pytorch/torch_tpu) ⭐3 · 2026-10-23 — Google 官方开源 PyTorch TPU 后端：ATen kernel 加 XLA 编译缓存加 torch.compile，训练/推理栈开源竞争再加一子

## 频道导航

| 频道 | 展示条目 | 说明 |
|---|---:|---|
| 模型与实验室 | 435 | GPT、Claude、Gemini、开源模型、模型能力边界。 |
| Agent 与自动化 | 585 | Agent 框架、MCP、A2A、工具调用、长期任务。 |
| AI 编程 | 310 | IDE、CLI、代码审查、工程工作流、开发者效率。 |
| 基础设施 | 186 | 推理、RAG、微调、评测、多模态、芯片和端侧部署。 |
| 产品与商业 | 223 | AI 产品、大厂战略、融资、监管、市场结构。 |
| 研究与学习 | 133 | 论文、课程、提示工程、长文、方法论。 |
| 工具与项目 | 245 | 可直接尝试的工具、开源项目、产品更新和资源库。 |

## 当前数据

- 原始条目: 2890
- 公开展示卡片: 2117
- 有全文内容: 2014
- 最近 7 天信号: 129
- 输出目录: `dist/`

## 热门标签

`arxiv`, `benchmark`, `openai`, `evaluation`, `anthropic`, `multi-agent`, `agent-security`, `claude-code`, `security`, `coding-agents`, `agents`, `agent-memory`, `coding-agent`, `prompt-injection`, `agent-harness`, `safety`, `agent-safety`, `kv-cache`

## 自动化约定

- 结构化数据源: `data/entries.json`
- 正文内容源: `content/*.md`
- 共享清洗入口: `openclaw/scripts/pipeline_utils.py`
- 站点生成入口: `npm run build` 或 `python3 scripts/generate-site.py`
- Cloudflare Pages 输出目录: `dist`

由 OpenClaw 每日自动维护；前台展示会过滤低信号、重复、非 AI、摘要不可读的条目。
