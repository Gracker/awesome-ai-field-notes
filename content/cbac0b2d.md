# Rethinking Cross-Tokenizer On-Policy Distillation: From Alignment Coverage to Supervision Reliability

- **ID**: cbac0b2d
- **原文链接**: https://arxiv.org/abs/2610.08448
- **PDF**: https://arxiv.org/pdf/2610.08448
- **作者**: Bingxi Hou, Guochao Jiang, Guofeng Quan, Weiqing Li, Wenfeng Feng, Guohua Liu, Yuewei Zhang
- **日期**: 2026-10-06
- **更新**: 2026-10-06
- **分类**: models
- **来源类型**: paper
- **标签**: distillation, on-policy, tokenizer, reverse-kl, arxiv
- **质量评分**: 4/5
- **抓取时间**: 2026-10-07T15:55:28Z

---

## 中文导读

On-Policy Distillation（OPD）用老师对模型自己生成的反馈来训练学生，但师生 tokenizer 不同时，对齐要同时在序列层和词表层做。这篇论文问的问题是：把对齐覆盖面做大，真的能改善学习吗？在三对异构师生组合、数学推理与代码生成两个任务上，作者的发现是：严格的 1:1 对齐组在词表错配可观的情况下就已经覆盖了绝大部分学生生成 token；在蒸馏前从学生采样的回答上，共享词表在严格对齐位置几乎保留了老师与学生的全部概率质量。由此推出的实用结论是：把 reverse KL 限制在每个严格位置的『学生自选共享词表 top-16 子集』上，准确率与全共享词表 OPD 相当，还优于被评测的跨 tokenizer 基线。蒸馏信号的设计重点应从『对齐覆盖面』转向『监督可靠性』。

## 为什么值得关注

HF 日榜第一（110 赞）：跨 tokenizer 蒸馏这个具体工程痛点第一次被系统测量，top-16 子集 reverse KL 是可以直接抄的配方；对做异构模型蒸馏的团队是即用型结论。

## 关键信息

- 论文标题：Rethinking Cross-Tokenizer On-Policy Distillation: From Alignment Coverage to Supervision Reliability
- 作者：Bingxi Hou, Guochao Jiang, Guofeng Quan, Weiqing Li, Wenfeng Feng, Guohua Liu, Yuewei Zhang
- arXiv：https://arxiv.org/abs/2610.08448
- 发布时间：2026-10-06
- arXiv 分类：cs.CL, cs.AI
- 关联标签：distillation, on-policy, tokenizer, reverse-kl, arxiv

## English Abstract

On-Policy Distillation (OPD) trains a student on its own generations using teacher feedback. With different tokenizers, comparing teacher and student predictions requires alignment at both sequence and vocabulary levels. In this paper, we examine whether expanding this alignment coverage improves learning. Across three heterogeneous teacher--student pairs on mathematical reasoning and code generation, strict 1:1 groups already cover most student-generated tokens despite substantial vocabulary mismatch. On responses sampled from the students before distillation, the shared vocabulary retains nearly all teacher and student probability mass at strictly aligned positions on average. Restricting reverse KL to a student-selected top-16 subset of the shared vocabulary at each strict position achieves accuracy comparable to full shared-vocabulary OPD, outperforming the evaluated cross-tokenizer baselines.

## English Summary

Cross-tokenizer OPD does not need maximal alignment coverage: strict 1:1 groups already cover most student tokens, and restricting reverse KL to a student-selected top-16 shared-vocabulary subset per position matches full shared-vocab OPD while beating cross-tokenizer baselines.

## Obsidian Notes

- 内容由 `opencli arxiv paper` 拉取 arXiv 元数据与摘要生成。
- 中文导读与价值判断锚定在摘要的作者、日期、分类与实验设置上，未补充摘要之外的实验细节。
- 现代站点生成器按 `content/{entry.id}.md` 查找内容页；本文件写入 canonical content 目录，而不是 `openclaw/content/`。