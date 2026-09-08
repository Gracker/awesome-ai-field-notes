# Molecular Dj Vu: Frontier LLMs Verbatim-Retrieve Published Property Values

> Source: https://arxiv.org/abs/2609.05381
> Authors: Matthias Busch, Marius Tacke, Sviatlana V. Lamaka, Mikhail L. Zheludkevich, Christian J. Cyron, Roland C. Aydin, Christian Feiler
> Published: 2026-09-04
> Categories: cs.AI
> PDF: https://arxiv.org/pdf/2609.05381v1

## Abstract

Large language models (LLMs) are increasingly evaluated on molecular property benchmarks, but accuracy cannot distinguish a model that predicts a property from one that retrieves a published number. We audit 22 frontier models on 12 regression benchmarks for verbatim retrieval and find that it is widespread but relatively benchmark-specific: on five datasets more than $50\%$ of the LLMs show verbatim retrieval, while on the remaining datasets it appears only in isolated cells. We run our experiments at two reasoning levels and find that reasoning changes retrieval. The same experiments, on the same molecules and with the same prompt, are flagged $89\%$ more often at the higher reasoning level than at the lowest one. Finally, we test a way to interrupt retrieval in our most contaminated cases, and find that the strongest models in some cases still recognise a combination of transformed SMILES strings and original labels. Furthermore, suppressing retrieval moves the prediction errors of the different models closer together in relative terms, while their differing use of verbatim retrieval spreads them apart. This indicates that the general predictive capability of an LLM is not determined solely by the amount of memorised values. This work provides an overview of the amount and depth of verbatim retrieval in molecular regression benchmarks using LLMs.

## Key Findings

- **Audit:** 22 frontier models × 12 regression benchmarks for molecular property prediction.
- **Verbatim retrieval is widespread but benchmark-specific:** On 5 datasets, more than 50% of models show verbatim retrieval; on the remaining datasets it appears only in isolated cells.
- **Reasoning level matters:** Same prompt, same molecules — higher reasoning level flags verbatim retrieval **89% more often** than the lowest level.
- **Robustness test:** Trying to interrupt retrieval (SMILES transformations + original labels) — strongest models still recognise the original label combination in some cases.
- **Effect on errors:** Suppressing retrieval moves the prediction errors of different models closer together; preserving retrieval spreads them apart — verbatim memorisation is a major driver of cross-model divergence, but general predictive capability is not determined by it alone.

## 中文概要

本文审计 22 个前沿模型在 12 个分子属性回归基准上的“原文追记”现象。发现：宝闻物森希般追记在某些数据集上广泛存在（有5 个数据集超过 50% 模型出现字面担查），但在其余数据集上仅为孤立点；推理强度改变会改变追记行为，高推理下同一提示同一分子上被标记的次数低推理多 89%；在最严重的污染数据集中用 SMILES 变换方式试图拦截，最强模型仍能识别原始标签；拑除追记后不同模型预测误差被拉近，说明追记是被验证不同模型表现差异的主要贡献者之一，但预测能力本身不能等同于记忆量。
