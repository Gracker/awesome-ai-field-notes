# Contrastive Discovery: Open-Ended Scientific Discovery over Competing Explanations

- **ID**: aba4cacb
- **原文链接**: https://arxiv.org/abs/2611.14514
- **PDF**: https://arxiv.org/pdf/2611.14514
- **作者**: Ziang Liu, James J. Kim, Yijia Dai, Jennifer J. Sun
- **日期**: 2026-11-10
- **更新**: 2026-11-10
- **分类**: agents
- **来源类型**: paper
- **标签**: scientific-discovery, hypothesis-testing, contrast-sets, agents
- **质量评分**: 4/5
- **抓取时间**: 2026-11-12T15:45:39Z

---

## 中文导读

多数科学发现 agent 逐点检验假设：证据推翻 h 只说明 h 不成立，不说明哪个替代解释成立。论文改用「对比集」——一个问题配互斥且穷尽的竞争解释，每个实验按其对全集合信念的重分配打分，信念集中于单一解释时问题解决。同一证据下 89% 的大信念偏移逐点候选是拒绝，对比集把其中 73% 解析到具体替代；用对比集引导搜索，同等实验预算下比逐点 surprisal 多解决 67% 的问题；38 名专家盲评在 78% 的已解决问题上选择同一解释。

## 为什么值得关注

对 agent 假设检验设计的直接批评与替代：把提议单元从单假设换成竞争解释集合，改动只在提议与打分单元，现有 agent 可直接复用。

## 关键信息

- 论文标题：Contrastive Discovery: Open-Ended Scientific Discovery over Competing Explanations
- 作者：Ziang Liu, James J. Kim, Yijia Dai, Jennifer J. Sun
- arXiv：https://arxiv.org/abs/2611.14514
- 发布时间：2026-11-10
- arXiv 分类：c; s; .; A; I; ,;  ; c; s; .; C; L; ,;  ; c; s; .; L; G
- 关联标签：scientific-discovery, hypothesis-testing, contrast-sets, agents
- 备注：AI 前沿一手源 2026-11-12 笔记共同锚定；中文导读与价值判断均以 arXiv 摘要为准，未补充摘要之外的实验细节。

## English Abstract

LLM agents are increasingly used for open-ended, data-driven scientific discovery, yet most of them evaluate hypotheses pointwise, testing an empirical claim $h$ only against its complement $\neg h$. When evidence rejects $h$, the agent learns that one explanation is unlikely but not which alternative the evidence supports. To recover that alternative, we introduce Contrastive Discovery, which replaces the single hypothesis with a contrast set, a scientific question paired with mutually exclusive and collectively exhaustive competing explanations. Each experiment is scored by how its evidence redistributes belief across the set, and the question is resolved when belief concentrates on one explanation. Because contrast sets change only the unit an agent proposes and scores, an existing agent can use them to re-evaluate evidence it has already collected or to guide its search. Across six domains, $89\%$ of the pointwise candidates with the largest belief shifts are rejections. On the same evidence, contrast sets resolve $73\%$ of these candidates to a specific alternative. When contrast sets guide search, the agent resolves $67\%$ more questions than pointwise surprisal under the same experiment budget. In a blinded study, $38$ human experts chose the same explanation on $78\%$ of resolved questions and on $82\%$ of questions where the pointwise agent rejected its hypothesis and stopped. Together, these results support explicit competing explanations as a way for discovery agents to resolve more scientific questions from the same evidence and validation budget.

## English Summary

Most LLM discovery agents evaluate hypotheses pointwise: when evidence rejects a claim h, the agent learns one explanation is unlikely but not which alternative the evidence supports. Contrastive Discovery replaces the single hypothesis with a contrast set - a scientific question paired with mutually exclusive and collectively exhaustive competing explanations. Each experiment is scored by how its evidence redistributes belief across the set, and the question resolves when belief concentrates on one explanation. Across six domains, 89% of pointwise candidates with the largest belief shifts are rejections, and contrast sets resolve 73% of those to a specific alternative on the same evidence; with contrast sets guiding search, the agent resolves 67% more questions under the same experiment budget. In a blinded study, 38 human experts chose the same explanation on 78% of resolved questions.

## Obsidian Notes

- 内容获取路径：`opencli arxiv paper 2611.14514 -f json` 一次成功，以元数据+摘要回填。
- 现代站点生成器按 `content/aba4cacb.md` 查找内容页；本文件写入 canonical content 目录，而不是 `openclaw/content/`。
