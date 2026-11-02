# Every Token Needs Its Own Teacher: Multi-teacher Adaptive On-policy Self-distillation

- **ID**: 4e8afe1d
- **原文链接**: https://arxiv.org/abs/2610.40574
- **PDF**: https://arxiv.org/pdf/2610.40574
- **作者**: Yifu Luo , Chuang Ma , Zeyu Chen , Enkelejda Kasneci , Qi Chen , Gjergji Kasneci
- **日期**: 2026-10-29
- **更新**: N/A
- **分类**: models
- **来源类型**: paper
- **标签**: post-training, self-distillation, token-level, teacher-selection, math-reasoning
- **质量评分**: 4/5
- **抓取时间**: 2026-11-02T04:23:43Z

---

## 中文导读

OPSD（在线策略自蒸馏）用特权参考构造 teacher 做后训练，但现有方法要么全程固定 teacher，要么只在响应间调整参考暴露作者用 teacher 干预预实验证明：同一响应内每个 token 的 teacher 偏好不同，可通过多数投票加 KL 选择为每个 token 找到更优 teacherMTA-OPSD 首次做 token 级自适应：维护候选 teacher 池，训练中每个 token 自选偏好 teacherQwen3 在数学推理上平均较基座最高 +5.9，稳定超过既有 OPSD 变体，代码已开源

## 为什么值得关注

OPSD（在线策略自蒸馏）用特权参考构造 teacher 做后训练，但现有方法要么全程固定 teacher，要么只在响应间调整参考暴露作者用 teacher 干预预实验证明：同一响应内每个 token 的 teacher 偏好不同.

该文于 2026-10-29 提交 arXiv（分类：Computation and Language (cs.CL)），备注：Preprint。 条目已有的中文导读与英文摘要均以此页元数据为锚，不引入摘要之外的实验细节。

## 关键信息

- 论文标题：Every Token Needs Its Own Teacher: Multi-teacher Adaptive On-policy Self-distillation
- 作者：Yifu Luo , Chuang Ma , Zeyu Chen , Enkelejda Kasneci , Qi Chen , Gjergji Kasneci
- arXiv：https://arxiv.org/abs/2610.40574
- 发布时间：2026-10-29
- arXiv 分类：Computation and Language (cs.CL)
- 关联标签：post-training, self-distillation, token-level, teacher-selection, math-reasoning

## English Abstract

On-policy Self-distillation (OPSD) has proven effective for post-training large language models by constructing a teacher conditioned on privileged references. However, existing approaches keep the teacher fixed either throughout training by consistently exposing it to the full reference, or within each response by adaptively varying partial reference exposure only across responses. In this paper, we argue that neither of them is sufficient. Instead, every token needs its own teacher, as the teacher preference can vary token by token within the same response. Through a teacher-intervention pilot study, we validate that the teacher preference differs across tokens, and reveal that a preferred teacher can be identified for each token through majority voting and KL-based selection. Motivated by these findings, we propose Multi-teacher Adaptive On-policy Self-Distillation (MTA-OPSD), the first token-level adaptive OPSD method. Our method constructs a multi-teacher pool consisting of candidate teachers, and enables every token to adaptively select its preferred teacher during training. Experiments with Qwen3 models on mathematical reasoning tasks show that MTA-OPSD consistently outperforms existing OPSD approaches with an average gain of up to $+5.9$ over the base model, highlighting the importance of adapting teacher supervision at the token level. The code is available at this https URL .

## English Summary

Multi-teacher Adaptive On-policy Self-Distillation (MTA-OPSD) extends on-policy self-distillation for LLM post-training by letting every token pick its own teacher. OPSD builds a teacher conditioned on privileged references, but prior methods keep the teacher fixed either across training or only across responses. A teacher-intervention pilot study shows teacher preference actually varies token by token within a single response, and a preferred teacher can be identified per token via majority voting and KL-based selection. MTA-OPSD maintains a pool of candidate teachers and lets each token adaptively select its preferred teacher during training. On mathematical reasoning with Qwen3 models it consistently outperforms existing OPSD approaches, with average gains of up to +5.9 over the base model. Code is released on GitHub.

## Obsidian Notes

- 内容获取路径：优先尝试 `opencli arxiv paper 2610.40574 -f json`；arXiv API 返回 HTTP 429，改由 arXiv abs 页面元数据与摘要回填。
- 中文导读与价值判断均锚定在条目已有摘要、论文摘要、作者、日期与分类信息上。
- 现代站点生成器按 `content/{entry.id}.md` 查找内容页；本文件写入 canonical content 目录，而不是 `openclaw/content/`。
