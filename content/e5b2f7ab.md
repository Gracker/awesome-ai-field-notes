# Does a model's stated reason for rejecting a candidate do any work?

> 原文链接: https://arxiv.org/abs/2609.30151
> 作者: Archit Rastogi
> 发布时间: 2026-09-24
> 源: arXiv外部扫描 (2026-09-28)

---

## 摘要

arXiv 2609.30151（LLM4XAI 2026 oral）把"模型拒绝某候选时引用的那条事实"当作可独立检验的声明：在 2WikiMultihopQA 上挑出被模型点名的"缺失事实"，再把一条真实语料句子插回 rival 的 profile 重新用 greedy decoding 提问控制项同时安排同长度不相关句子插同一处以及把这两条句子插到一个模型从未点名的第三个选项上最大规模的一轮实验中，6 个开源模型在"named 位置补回 named fact"时对手选项被改向的幅度显著高于无关控制（odds ratio 3.57 [1.54, 8.26]，Holm p=0.0210），并对单模型 drop-out 鲁棒；而同一事实放在"无人点名"的选项处不再显著（Holm p=0.2428）最强信号其实是无关句的位置效应：相同无关句在 named rival 处比在第三选项处改向幅度更大（Holm p=0.0008）内容效应被协同候选提及关系模板和流畅度差异部分解释，作者主张这是一条"以内容对比为界的效应"

## English Summary

arXiv 2609.30151 (LLM4XAI 2026 oral) tests whether a model's stated reason for rejecting a rival is a load-bearing claim: on 2WikiMultihopQA, supplying the named fact at the profile the model named moves its choice more than an irrelevant length-matched control (OR 3.57 [1.54, 8.26], Holm p=0.0210) across 6 open models, while the same fact at a third option the model never mentioned does not clear correction. The strongest single contrast is positional rather than content the identical irrelevant sentence moves the choice more at the named rival than at the third option (Holm p=0.0008).

## 为什么值得关注

把 LLM 的拒绝理由当成可证伪命题：2WikiMultihopQA 上"named 位置 + named fact"显著改向，位置而非内容才是最强信号

## 信息源

- https://arxiv.org/abs/2609.30151
