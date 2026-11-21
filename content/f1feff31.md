# MedChemBench is a new benchmark for AI reasoning in medicinal chemistry

- 作者: OpenAI (@OpenAI)
- 发布: 2026-11-20
- 原文: https://x.com/OpenAI/status/2123856316187975756
- 抓取时间: 2026-11-21 (Asia/Shanghai) · opencli twitter thread

---

> MedChemBench is a new benchmark for AI reasoning in medicinal chemistry.
>
> It shows the progress our frontier models have made in their ability to help scientists use AI to identify promising drug candidates.

（官方正文页 openai.com/index/introducing-medchembench/ 对本机直接抓取被导航拒绝；以上为 @OpenAI 官方帖全文，opencli twitter thread 抓取。）

## 关键读数（官方帖讨论区引用的官方文档数字）

- xhigh 档 GPT-6.2 Astra 得分 84.5%，仅比 GPT-6 Astra 高 1.2 分。
- 每题单次尝试（single attempt），不给工具，不做新实验。
- 官方承认无法排除对已发表论文的先验记忆（prior exposure）。
- 分项覆盖结构重建、推理、候选选型、性质预测四个组件；结构重建强，选型与数值预测弱。

## 边界

- 测的是受约束的推理能力，不声称发现新药。
- 与第三方另一套 rubric（「<50% leaderboard」）勿混表。

---

> Obsidian 证据: Hermes 定时任务/X-每日简报/2026-11-20-X-seeds_Claude330-Codex0171-MedChemBench.md（分项与官方边界）
