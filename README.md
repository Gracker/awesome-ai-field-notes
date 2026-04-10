# AI Field Notes — AI 领域精选资源库

> 一个 **有观点、有评分、可被 Agent 消费** 的 AI 领域资源导航。由 OpenClaw 每日自动更新。

## 和 Awesome List 的区别

| 维度 | 传统 Awesome List | 本项目 |
|------|------------------|--------|
| 评价 | 无 | 每条带中文点评 + 质量评分 |
| 筛选 | 靠自己翻 | score ≥ 3 才展示，1-2 分仅存档 |
| 机器可读 | Markdown 难解析 | `entries.json` 结构化数据，Agent 可直接消费 |
| 生命力 | 创建即废弃 | OpenClaw 每日维护：死链检测、stars 刷新、时效归档 |
| 语言 | 英文为主 | 中英双语，中文 one_liner 对中文开发者友好 |

## 质量评分标准

| 分数 | 含义 | 标准 |
|------|------|------|
| ⭐⭐⭐⭐⭐ 5 | 必读 | 里程碑级内容，改变了行业认知或实践方式 |
| ⭐⭐⭐⭐ 4 | 优秀 | 高质量原创，有独到洞察或完整实现 |
| ⭐⭐⭐ 3 | 值得一看 | 信息准确、有参考价值，但缺少独特视角 |
| — | 2 分以下 | 仅在 `entries.json` 中存档，不在本站展示 |

## 分类导航

<!-- AUTO-GENERATED: 由 generate-site.py 从 entries.json 渲染，勿手动编辑 -->
📊 **191** 条资源 | **191** 条本周新增 | 更新: 2026-04-10

| 分类 | 活跃数 | 分类 | 活跃数 |
|------|--------|------|--------|
| 🧠 模型与厂商 | 3 | 🤖 Agent 框架 | 44 |
| 🔗 Agent 协议 | 4 | 🖥️ Agent 操作系统 | 9 |
| 💻 AI 编程 | 45 | 📊 评测与排行 | 1 |
| 📚 RAG 与知识系统 | 3 | ⚡ 推理与部署 | 5 |
| 🔧 微调与训练 | 0 | ✨ 提示工程 | 6 |
| 🎨 多模态AI | 0 | 📱 AI 产品 | 3 |
| 🌍 行业与战略 | 24 | 📝 重要论文 | 13 |
| 📖 教程与学习 | 16 | | |

### ⭐ 本周精选 Top 10

- [搞懂缓存机制，从Gemma4到Claude Code省80%Token](https://x.com/MinLiBuilds/status/2041178722230030384) by @MinLiBuilds — 从 KV 缓存原理到 Claude Code 实战，系统讲透 token 省钱机制 `kv-cache` `claude-code` `token-optimization` `transformer` `caching` 🇨🇳
- [Launching Claude Managed Agents](https://x.com/RLanceMartin/status/2041927992986009773) by @RLanceMartin — Anthropic 官方托管 Agent 基础设施，大脑/手/记忆三层解耦架构 `claude` `managed-agents` `anthropic` `agent-sdk` `infrastructure` 🌐
- [THE 2028 GLOBAL INTELLIGENCE CRISIS](https://www.citriniresearch.com/p/2028gic) by @Citrini — AI 经济死亡螺旋的情景推演：幽灵 GDP 与人类智能替代螺旋 `ai-economy` `unemployment` `ghost-gdp` `saas` `automation` 🌍
- [OpenClaw + Codex/ClaudeCode Agent Swarm: The One-Person Dev Team](https://x.com/elvissun/status/2025920521871716562) by @Elvis — 一人开发团队的 Agent Swarm 实战：OpenClaw 编排 + 多模型协作 `openclaw` `codex` `claude-code` `agent-swarm` `orchestration` 🌐
- [过了个年，AI 圈变天了？但没人告诉你为什么](https://x.com/op7418/article/2026520431700881816) by @歸藏 — 2026 年初 AI 变化的四层拆解：大脑/手脚/组织/进化，数据飞轮加速运转 `ai-trends` `agent` `model-evolution` `data-flywheel` `2026` 🇨🇳
- [2026年AI趋势观察：模型飞轮、应用爆发与个人发展](https://mp.weixin.qq.com/s/D98rfJX1NZmAD4xxs1h-Xg?scene=1) by @向阳乔木 — 2026 AI 趋势全景：模型飞轮加速，应用爆发，创作门槛消失 `ai-trends` `model-flywheel` `agent` `multimodal` `career` 🇨🇳
- [Pi: The Minimal Agent Within OpenClaw](https://lucumr.pocoo.org/2026/1/31/pi/) by @Armin Ronacher — OpenClaw 底层 Pi 的极简哲学：让 Agent 自己扩展自己 `pi` `openclaw` `coding-agent` `mcp` `session-tree` 🌐
- [我的 Obsidian 不是笔记软件，是操作系统](https://x.com/UncleJAI/article/2026929169511362928) by @Uncle J — 非程序员用 Obsidian + Claude Code 搭建的完整个人操作系统 `obsidian` `claude-code` `automation` `file-over-app` `personal-os` 🇨🇳
- [科学家的消亡 / AI 会终结科学，还是会引发一场新的革命？](https://x.com/indigox/article/2026911299494449635) by @indigo — 从科学哲学角度追问：AI 能执行方法，但科学不仅仅是方法 `ai-science` `philosophy` `consciousness` `alphaFold` `scientific-method` 🇨🇳
- [The third era of AI software development](https://x.com/mntruell/article/2026736314272591924) by @Michael Truell — Cursor CEO 定义 AI 编码第三时代：云 Agent 自主完成长任务 `cursor` `cloud-agent` `coding-eras` `tab-to-agent` `software-development` 🌐
<!-- /AUTO-GENERATED -->

## 数据结构

所有数据存储在 [`data/entries.json`](data/entries.json)，每条记录：

```json
{
  "id": "V1StGXR8_Z5jdHi6B-myT",
  "title": "项目/文章标题",
  "url": "https://...",
  "category": "agent-frameworks/orchestration",
  "tags": ["langchain", "production"],
  "source_type": "github",
  "language": "en",
  "added_date": "2026-04-10",
  "updated_date": null,
  "one_liner": "目前最实用的多 Agent 编排框架，生产就绪",
  "quality_score": 4,
  "status": "active",
  "github_stars": 95000,
  "related": ["Xk7Hd83f_Wp9Qm2L-abc"]
}
```

## 贡献

- 提交新资源 → 开 [Issue](../../issues/new/choose)
- 纠错 / 评分异议 → 开 [Issue](../../issues/new/choose)
- 详见 [CONTRIBUTING.md](CONTRIBUTING.md)

## 关于 AI 辅助

本项目使用 [OpenClaw](https://github.com/openclaw/openclaw) 自动维护：
- OpenClaw 负责：数据采集、去重、分类、stars 刷新、死链检测、README 生成
- 人工负责：**one_liner 点评**（核心壁垒）、quality_score 评分、最终审核

## License

[CC BY-NC-SA 4.0](LICENSE)
