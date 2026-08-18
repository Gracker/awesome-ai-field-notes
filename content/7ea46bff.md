# What Twelve LLM Agent Benchmark Papers Disclose About Themselves: A Pilot Audit and an Open Scoring Schema

- **ID**: 7ea46bff
- **原文链接**: https://arxiv.org/abs/2605.21404
- **PDF**: https://arxiv.org/pdf/2605.21404v1
- **作者**: Mahdi Naser Moghadasi, Faezeh Ghaderi
- **日期**: 2026-05-20
- **更新**: 2026-05-20
- **分类**: learning
- **来源类型**: paper
- **标签**: benchmark, reproducibility, meta-science, audit, arxiv
- **质量评分**: 4/5
- **抓取时间**: 2026-08-18T05:28:55Z

---

## 中文导读

动机来自常见挫败：两篇论文在同一个基准上用同一个模型名报告结果却相互矛盾，而已发表的产物无法判断原因在脚手架采样设置子集还是评估器版本作者逐维阅读并记录 12 篇知名 LLM agent 基准论文对自身评测运行的披露情况：设计了五字段审计模式（基准身份harness 规范推理设置成本报告失败分解），编写含试点评分边界案例的代码本，应用于 12 篇经典论文（8 篇 agent4 篇经典静态基准）8 篇 agent 基准论文平均审计分 0.38/1.0，静态基准 0.66；最大缺口在成本（无一篇以任何形式披露推理成本）与 harness 规范（无一篇完整披露评估环境的内容寻址容器镜像）以 JSON Schema 发布审计模式Markdown 发布代码本CSV 发布原始评分表；评分为单人单轮，多人审计是作者认定的下一步

## 为什么值得关注

12 篇 agent 基准论文的披露审计：平均 0.38/1.0，无一篇以任何形式披露推理成本

该论文发表于 2026-05-20，作者为 Mahdi Naser Moghadasi, Faezeh Ghaderi，arXiv 分类 cs.LG；以上判断基于论文摘要所述内容。

## 关键信息

- 论文标题： What Twelve LLM Agent Benchmark Papers Disclose About Themselves: A Pilot Audit and an Open Scoring Schema
- 作者： Mahdi Naser Moghadasi, Faezeh Ghaderi
- arXiv： https://arxiv.org/abs/2605.21404
- 发布时间： 2026-05-20
- arXiv 分类： cs.LG
- 备注： Pilot audit of 12 LLM agent benchmark papers; schema, codebook, and per-paper scoring sheet released. Submission to IEEE Big Data 2026
- 关联标签： benchmark, reproducibility, meta-science, audit, arxiv

## English Abstract

We read twelve well-known LLM agent benchmark papers and recorded, dimension by dimension, what each paper actually says about how its evaluation was run. The motivation came from a familiar frustration: two papers will report results on the same benchmark with the same model name and disagree, and you cannot tell why -- the scaffold, the sampling settings, the subset, or the evaluator version. In many cases the published artifact does not let you answer. This paper is an implementation report on the attempt. We designed a small audit schema (five fields: benchmark identity, harness specification, inference settings, cost reporting, failure breakdown), wrote a scoring codebook with the boundary cases we hit during pilot scoring, applied it to twelve canonical papers (eight agent, four classical static), and recorded what we saw. We score the disclosure of an agent run, not its correctness, and make no claim that disclosure implies a trustworthy result. The mean audit score across the eight agent-benchmark papers is 0.38 (out of 1.0), and across the four classical static benchmarks 0.66; the largest gap is on cost (none of the eight agent benchmark papers disclose inference cost in any form) and on harness specification (none fully disclose a content-addressed container image of the evaluation environment). We release the schema as a JSON Schema file, the codebook as a Markdown document, and the raw scoring sheet as a CSV. The scoring was performed by a single auditor in one pass; a multi-rater audit is the natural next step, and we discuss what we think it would change.

## English Summary

Motivated by the familiar frustration that two papers report results on the same benchmark with the same model name and disagree, with no way to tell whether the scaffold, sampling settings, subset, or evaluator version explains it, the authors read twelve well-known LLM agent benchmark papers and recorded dimension by dimension what each actually says about how its evaluation was run. They designed a five-field audit schema (benchmark identity, harness specification, inference settings, cost reporting, failure breakdown), wrote a scoring codebook with boundary cases, and applied it to twelve canonical papers (eight agent, four classical static)....

## Obsidian Notes

- 内容由 `opencli arxiv paper` 拉取 arXiv 元数据与摘要生成。
- 中文导读与价值判断均锚定在条目已有摘要、论文摘要、作者、日期与分类信息上；未补充论文摘要之外的实验细节。
