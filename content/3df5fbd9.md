# Introducing Claude Fable 5.1 and Claude Mythos 5.1

- **ID**: 3df5fbd9
- **原文链接**: https://www.anthropic.com/claude-fable-and-mythos-5-1
- **作者**: Anthropic
- **日期**: 2026-09-01
- **抓取时间**: 2026-09-02T15:31:00Z
- **分类**: models
- **来源类型**: article
- **语言**: zh
- **标签**: claude, fable, mythos, efs, release-notes
- **质量评分**: 4/5

---

## 中文导读

Anthropic 9 月 1 日发的两个 Claude 5.1 变体其实是同一个底层模型只差 safeguard：Mythos 5.1 只走 trusted access 通道给网安和生命科学，Fable 5.1 全面开放价格消息更重要cache read 降价让典型任务比 5 代便宜约 25%，高度 agentic 工作流最多便宜 45%，这一刀主要砍在反复喂 prompt 的 agent 路径上数据方面推 Enterprise Frontier Safeguards (EFS)，把语料存在客户自己云里，做到 zero data retention 等价的同时不丢对抗能力基准上 Terminal-Bench-Science 从 Fable 5 的 24.7% 跳到 52.6%，AutomationBench 17.1% 升到 31.4%，OSWorld 2.0 strict 从 36.1% 升到 41.7%

## 一句话点评

Anthropic 9 月 1 日发的两个 Claude 5.

---

## English Abstract / Summary

Anthropic introduces Claude Fable 5.1 and Claude Mythos 5.1, the same underlying model with different safeguard tiers: Fable 5.1 is generally available, Mythos 5.1 is gated through trusted access for cybersecurity and life sciences. Cache read pricing cuts typical costs ~25% versus Fable 5 and up to ~45% on highly agentic workflows. Enterprise Frontier Safeguards (EFS) stores data in customer-controlled cloud while preserving adversarial-defense quality, equivalent to zero data retention. Terminal-Bench-Science jumps from 24.7% (Fable 5) to 52.6%, AutomationBench from 17.1% to 31.4%, OSWorld 2.0 strict from 36.1% to 41.7%.

---

## Obsidian Notes

- 由 `daily-intake-evening` 2026-09-02 cron 从当日 Obsidian 摘要（论文流水线 / AK-RSS / ClawFeed / X 书签消化）发现并入库存量阶段。
- 中文导读与判断均锚定在条目已有摘要、源页面正文、作者、日期与分类信息；未补充源页面之外的实验细节。
