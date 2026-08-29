# WikiSkill: Compiling Agent Experience into Persistent Knowledge for Skill Evolution

- **ID**: c07cfbc0
- **原文链接**: https://arxiv.org/abs/2608.27454
- **PDF**: https://arxiv.org/pdf/2608.27454v1
- **作者**: Liyan Tang, Cyrus Rashtchian, Chun-Sung Ferng, Andrew Tomkins, Da-Cheng Juan, Tu Vu
- **日期**: 2026-08-27
- **更新**: 2026-08-27
- **分类**: agents
- **来源类型**: paper
- **标签**: agents, skill-evolution, experience-reuse, arxiv
- **质量评分**: 4/5
- **抓取时间**: 2026-08-29T12:59:16+08:00

---

## 中文导读

WikiSkill（arXiv 2608.27454，cs.AI，2026-08-27）把智能体技能演化与持久知识库（wiki）绑定共同演化：将原始执行经验、沉淀知识、可执行技能三者分离，经验持续合并进 wiki，后续技能更新在其之上构建——解决的是"指导技能发展的洞见散落在优化历史里、难以跨迭代复用"的问题。跨多基准、多模型，WikiSkill 一致超越 SOTA 技能演化方法，并在多数模型-基准组合上优于无技能基线。两个关键发现：技能演化与模型规模互补——大模型从演化技能中获益更多，而小模型带技能可以反超显著更大的裸模型；演化出的技能可跨模型乃至跨模型家族迁移，他模型演化出的技能甚至能优于自演化技能。消融实验确认 wiki 的持久知识积累是技能演化有效性的关键。

## 为什么值得关注

给 agent 技能体系补上了"知识底座"这一层：技能不再是散落在优化历史里的洞见，而是可积累、可迁移的持久资产；"小模型带技能反更大裸模型"与"他模型技能可优于自演化"两条结论对技能共享和团队级技能库建设都有直接影响。

## 原文（抓取存档·节选）

```markdown
> Abstract (arXiv 2608.27454, v1 2026-08-27)

Agent skills package specialized knowledge and workflows into reusable resources that extend AI agent capabilities. Recent work automatically discovers such skills from agent experience, which enables agents to progressively adapt through interaction. However, the insights that guide skill development typically remain scattered across optimization histories, limiting their systematic reuse across iterations. We introduce WikiSkill, a framework that co-evolves agent skills with a persistent knowledge base (wiki). At a high level, WikiSkill separates raw execution experience, accumulated knowledge, and executable skills, while continuously consolidating experience into the wiki, which subsequent skill updates can build on. Across diverse benchmarks and models, WikiSkill consistently outperforms state-of-the-art skill-evolution methods and improves over no-skill baselines in most model-benchmark settings. We find that skill evolution complements model scaling: larger models generally benefit more from evolved skills, while smaller models with skills can outperform substantially larger models without them. We also find that evolved skills transfer effectively across models and model families, and skills evolved by other models can outperform self-evolved skills. Finally, our ablation studies confirm that persistent knowledge accumulation in the wiki is critical for effective skill evolution. These results demonstrate the benefits of systematically accumulating and refining agent experience for developing reusable and transferable skills.
```

## Obsidian Notes

- 内容由 `opencli arxiv paper 2608.27454 -f json` 拉取 arXiv 元数据与摘要生成。
- 中文导读与价值判断均锚定在条目已有摘要、论文摘要、作者、日期与分类信息上；未补充论文摘要之外的实验细节。
