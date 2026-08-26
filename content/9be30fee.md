# The Interaction Tax: When Communication Erases Diversity in Multi-Agent Teams

- **ID**: 9be30fee
- **原文链接**: https://arxiv.org/abs/2608.23541
- **PDF**: https://arxiv.org/pdf/2608.23541v1
- **作者**: S, u, m, m, e, r,  , E, u, n, h, y, u, n, g,  , A, n, n, ,,  , H, a, o, k, u, n,  , L, i, u, ,,  , C, h, e, n, h, a, o,  , T, a, n
- **日期**: 2026-08-24
- **更新**: 2026-08-24
- **分类**: agents
- **来源类型**: paper
- **标签**: multi-agent, diversity, interaction-tax, icml-2026, llm-debate
- **质量评分**: 5/5
- **抓取时间**: 2026-08-26T04:27:05Z

---

## 中文导读

多智能体 LLM 交互到底帮不帮忙，文献结论互相矛盾这篇 ICML 2026 论文给出关键区分：不是所有通信都等价不同模型家族会找到结构不同的解，但只要 agent 互相读到完整输出，一轮之内提案就趋同，把用多模型的初衷多样性抹掉了，作者称之为 interaction tax在 11 个带验证器打分的优化任务等预算对比下，完整解交互是弱默认；独立生成提案可避开这种坍缩；完整解交互的主要效果是让 agent 贴住它看到的第一个解；critique 只在被违反规则易于 LLM 定位和修复时有效结论：多智能体性能更多取决于交换什么信息何时交换，而非 agent 数量

## 为什么值得关注

> ICML 2026：多智能体互看完整解会让提案一轮内趋同；独立生成再共享对的信息，才是等预算下的默认最优

对设计多智能体系统的从业者，这篇 ICML 2026 论文给出可操作的默认策略：等预算下先独立生成再选择性共享信息，避免整解互读导致一轮内提案趋同；通信结构应被视为需要付税的设计选择，而非默认打开。

## 关键信息

- 论文标题: The Interaction Tax: When Communication Erases Diversity in Multi-Agent Teams
- 作者: S, u, m, m, e, r,  , E, u, n, h, y, u, n, g,  , A, n, n, ,,  , H, a, o, k, u, n,  , L, i, u, ,,  , C, h, e, n, h, a, o,  , T, a, n
- arXiv: https://arxiv.org/abs/2608.23541
- 发布时间: 2026-08-24
- arXiv 分类: c, s, ., M, A, ,,  , c, s, ., A, I
- 备注: 14 pages, 3 figures. Accepted at ICML 2026 (PMLR 306)
- 关联标签: multi-agent, diversity, interaction-tax, icml-2026, llm-debate

## English Abstract

Does multi-agent LLM interaction help or hurt? Some work reports gains from debate (Du et al., 2024), critique loops (Chen et al., 2025), and mixture-of-agents synthesis (Wang et al., 2025), while other work finds that interaction adds cost without improving quality under equal budgets (Tran & Kiela, 2026; Xu et al., 2026; Jarrett et al., 2025), or that independent sampling already captures multi-agent gains (Li et al., 2024). We argue this contradiction partly reflects a missing distinction, because not all multi-agent communication is equal. Different model families find structurally different solutions, but when agents read each other's complete outputs, their proposals converge within one round, erasing the diversity that motivates using multiple models. We call this the interaction tax. We test 11 verifier-scored optimization tasks under matched budgets and find that full-solution interaction is a weak default. Independent proposal generation avoids this collapse. Full-solution interaction mainly makes agents stay close to the first solution they see instead of trying different approaches, and critique helps only if the violated rule is easy for the LLM to find and fix. These results suggest that multi-agent performance depends less on the number of agents than on the information they exchange, and interaction helps only when agents share the right information at the right time.

## English Summary

Does multi-agent LLM interaction help or hurt? Prior work is contradictory. The authors argue this partly reflects a missing distinction: not all multi-agent communication is equal. Different model families find structurally different solutions, but when agents read each other's complete outputs, their proposals converge within one round, erasing the diversity that motivates using multiple models the interaction tax. Across 11 verifier-scored optimization tasks under matched budgets, full-solution interaction is a weak default; independent proposal generation avoids the collapse. Full-solution interaction mainly makes agents stay close to the first solution they see, and critique helps only when the violated rule is easy for the LLM to find and fix. Multi-agent performance depends less on the number of agents than on what information is exchanged, and when.

## Obsidian Notes

- 内容由 `opencli arxiv paper` 拉取 arXiv 元数据与摘要生成。
- 中文导读与价值判断锚定在条目已有摘要、论文摘要、作者、日期与分类信息上；未补充论文摘要之外的实验细节。
- 本页由 AAIF content-fetcher 定时任务生成（2026-08-26），仅新增内容页，未改动 entries.json。
