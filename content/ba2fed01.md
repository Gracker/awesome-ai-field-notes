# Measuring Real-World Prompt Injection Attacks in LLM-based Resume Screening

- **ID**: ba2fed01
- **原文链接**: https://arxiv.org/abs/2605.28999
- **PDF**: https://arxiv.org/pdf/2605.28999
- **作者**: Mohan Zhang, Yuqi Jia, Zhen Tan, Steven Jiang, Neil Zhenqiang Gong, Tianlong Chen, Dawn Song
- **日期**: 2026-05-27
- **更新**: 2026-05-27
- **分类**: agents
- **来源类型**: paper
- **标签**: arxiv, paper, prompt-injection, real-world, measurement, resume-screening
- **质量评分**: 5/5
- **抓取时间**: 2026-09-21T04:30Z

---

## 中文导读

- 这是第一份对真实 LLM 应用里 prompt injection 的系统化测量，对象是简历筛选：数据来自 hireEZ 多年累积的约 20 万份真实简历，不是构造数据集。

- 方法上先做专用检测器，小规模人工验证显示高精度、优于通用 SOTA 检测器，再跑全量分析。

- 三个测量结论：约 1% 的简历含隐藏 prompt injection；此类注入简历的占比在过去一两年明显上升；90% 以上的注入 prompt 不使用显式指令。

- 已发表于 USENIX Security 2026，代码与 artifacts 开源（github.com/UNITES-Lab/resume-injection-measurement），可作为检测侧基线。

## 为什么值得关注

基于 20 万真实简历的首份 LLM 简历筛选 prompt injection 大规模测量：约 1% 中招，过去两年明显上升

## 关键信息

- 论文标题：Measuring Real-World Prompt Injection Attacks in LLM-based Resume Screening
- 作者：Mohan Zhang, Yuqi Jia, Zhen Tan, Steven Jiang, Neil Zhenqiang Gong, Tianlong Chen, Dawn Song
- arXiv：https://arxiv.org/abs/2605.28999
- 发布时间：2026-05-27
- arXiv 分类：cs.CR, cs.AI, cs.CL, cs.LG
- 关联标签：arxiv, paper, prompt-injection, real-world, measurement, resume-screening

## English Abstract

LLMs are vulnerable to prompt injection attacks. However, this vulnerability has been primarily demonstrated conceptually in academic studies or through a few anecdotal case studies. Its prevalence and impact in real-world LLM-based applications are largely unexplored. In this work, we present the first systematic study of prompt-injection attacks in a widely used application: LLM-based resume screening. Our analysis is based on approximately 200K real-world resumes collected over multiple years by hireEZ. We first design tailored methods to detect prompt injection in resumes. Manual validation on a small-scale dataset demonstrates that our detectors achieve high precision and outperform state-of-the-art general-purpose detectors. We then apply our detector to the full resume dataset and conduct a comprehensive measurement study of real-world prompt injection attacks. Our analysis reveals several intriguing findings: approximately 1% of resumes contain hidden prompt injections; the prevalence of such injected resumes has increased noticeably over the past one to two years; and more than 90% of injected prompts do not use explicit instructions. These results provide the first evidence of large-scale prompt injection in real-world LLM-based applications and lay the groundwork for future studies to understand and mitigate such attacks.

## English Summary

LLMs are vulnerable to prompt injection attacks. However, this vulnerability has been primarily demonstrated conceptually in academic studies or through a few anecdotal case studies. Its prevalence and impact in real-world LLM-based applications are largely unexplored. In this work, we present the first systematic study of prompt-injection attacks in a widely used application: LLM-based resume screening. Our analysis is based on approximately 200K real-world resumes collected over multiple years by hireEZ. We first design tailored methods to detect prompt injection in resumes. Manual validation on a small-scale dataset demonstrates that our detectors achieve high precision and outperform state-of-the-art general-purpose detectors. We then apply our detector to the full resume dataset and conduct a comprehensive measurement study of real-world prompt injection attacks. Our analysis reveals several intriguing findings: approximately 1% of resumes contain hidden prompt injections; the prevalence of such injected resumes has increased noticeably over the past one to two years; and more than 90% of injected prompts do not use explicit instructions. These results provide the first evidence of large-scale prompt injection in real-world LLM-based applications and lay the groundwork for future studies to understand and mitigate such attacks.

## Obsidian Notes

- 内容由 `opencli arxiv paper 2605.28999 -f json` 拉取 arXiv 元数据与摘要生成。
- 中文导读与价值判断均锚定在条目已有摘要、论文摘要、作者、日期与分类信息上；未补充论文摘要之外的实验细节。
