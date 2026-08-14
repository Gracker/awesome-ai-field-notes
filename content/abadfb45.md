# Introducing Grok 4.6

- **ID**: abadfb45
- **原文链接**: https://x.ai/news/grok-4-6
- **作者**: xAI
- **日期**: 2026-08-12
- **分类**: models
- **来源类型**: article
- **标签**: grok, xai, agentic-coding, frontier-model
- **质量评分**: 4/5
- **抓取时间**: 2026-08-14T12:20:00Z

---

## 中文导读

xAI 发布 Grok 4.6，以 Grok 4.5 为基底，重点优化长期运行的 agent 与更有野心的交互式/视觉工作：能在多步任务中保持专注——研究主题、分析信息、跨代码库工作、把想法变成完整的应用或工作产物。在 Artificial Analysis Intelligence Index（九项基准的复合分）上与 GPT-5.6 Sol 持平。训练侧：比 Grok 4.5 更长的补充训练（精选模型生成数据 + 高质量工程数据 + 改进的优化器与训练配方）；用 Grok 4.5 跨 reasoning effort、agent harness 与领域重生成 SFT trajectory 并用模型检查过滤问题轨迹；RL 阶段覆盖知识工作、通用编码及内核优化、Web 开发、CAD 等领域环境。产品侧：即日起上线 Cursor 与 Grok Build，API 起价 $2/M 输入、$6/M 输出（fast 变体两倍价），首周在 Grok Build 与 Cursor 内提供 2x 包含用量。

## 为什么值得关注

当前 frontier 竞争的焦点已明显转向"长期 agent + 交互/视觉工作"：Grok 4.6 的发布叙事几乎全部围绕多步任务保持力、自我测试与验证、一次成型的视觉/交互首版。训练配方上"用上一代强模型重生成 SFT 轨迹 + 大量领域化 agentic RL（内核优化/CAD/Web）"是值得跟踪的工程模式。

## 官方 Evals（x.ai 发布页，Grok 4.6 High vs 对照）

| 基准 | Grok 4.6 High | Grok 4.5 High | GPT-5.6 Sol Max | Fable 5 Max |
|---|---|---|---|---|
| AA Intelligence Index | 61 | 56 | 61 | 62 |
| GDPVal-AA v2 | **1753** | 1526 | 1728 | 1741 |
| CursorBench v3.2 | 69.9% | 66.7% | 67.2% | **70.5%** |
| DeepSWE v1.1 | 65.9% | 54% | **73%** | 70% |
| FrontierCode v1.1 (Extended) | 61.3% | 56.6% | 60.6% | **63.6%** |
| APEX-Agents | 57.5% | 47.1% | 56.7% | **59.2%** |
| Terminal-Bench v3.0 | 26% | 15.7% | **34.6%** | 34.1% |
| APEX-SWE | 56.4% | 53.6% | — | **58.8%** |
| AA-Briefcase | **1577** | 1313 | 1502 | 1574 |
| Harvey LAB (Vals) | **15.8%** | 12.9% | 2.5% | 11.3% |

注：官方口径为"每项评测最佳分数加粗；第三方模型分数取自其自报或公开结果"。Terminal-Bench 与 DeepSWE 上仍明显落后 GPT-5.6 Sol。

## 训练要点（官方描述）

1. **补充训练加长**：curated model-generated data（推理与高级技术概念）+ 高质量工程数据 + 改进优化器与训练配方，为后续 SFT/RL 打底。
2. **SFT 轨迹重生成**：用 Grok 4.5 跨 reasoning effort、agent harness、领域（STEM、软件工程、知识工作）重生成 SFT trajectory，并用基于模型的检查过滤问题轨迹。
3. **Agentic RL 任务面扩大**：知识工作、通用编码，以及内核优化、Web 开发、计算机辅助设计（CAD）等领域专用环境。

## 产品与定价

- 渠道：Cursor、Grok Build、API（SpaceXAI API），以及 OpenRouter、Vercel、Cloudflare 等伙伴。
- 定价：$2/M 输入 token，$6/M 输出 token；fast 变体两倍价。
- 首周在 Grok Build 与 Cursor 内 2x 包含用量。

## 来源

- 原文：https://x.ai/news/grok-4-6 （Aug 12, 2026，由 `opencli web read` 全文抓取）
- 中文导读与要点均锚定在发布页可见内容；未补充发布页之外的推测。

## Obsidian Notes

- 内容由 `opencli web read --url https://x.ai/news/grok-4-6` 抓取官方发布页生成。
- Evals 数字来自发布页表格；对照模型分数为官方转引的"自报或公开结果"。
