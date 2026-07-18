# Deceptive Grounding: Entity Attribution Failure in Clinical Retrieval-Augmented Generation

- **Source**: https://arxiv.org/abs/2607.09349
- **Platform**: paper
- **Original Date**: 2026-07-13
- **Added**: 2026-07-14
- **Category**: infra
- **Quality Score**: 4
- **Tags**: rag, clinical-ai, entity-attribution, deceptive-grounding, factuality, adversarial-eval, faithfulness

## 摘要 (Summary)

检索增强生成（RAG）评估通常只检查模型陈述是否事实性地基于检索到的文档，但不检查检索到的证据是否归属于正确的实体临床 RAG 响应可以在零幻觉近乎完美的 faithfulness以及真实引用的同时，把药物 Y 的临床证据呈现为所查询药物 X 的证据论文将这种失败称为 deceptive grounding（DG），它对 faithfulness幻觉和引用三类自动检查都不可见，因为每条陈述都来自真实文档，只是关于错误的实体研究在 13 个模型上做控制因子化基准，发现在对抗条件下 DG 率高达 887%，医学/生物医学微调模型峰值 86.7%结果表明，领域专门化反而放大了 DG 风险，RAG 评估必须增加实体归属检查才能可靠支撑临床决策

## English Abstract / Excerpt

Retrieval-augmented generation evaluation checks whether model claims are factually grounded in retrieved documents. It does not check whether retrieved evidence is attributed to the correct entity. A clinical RAG response can pass every automated check (zero hallucinations, near-perfect faithfulness, real citations) while presenting drug Y's clinical evidence as evidence about queried drug X. We term this deceptive grounding (DG): a failure invisible to faithfulness, hallucination, and citation checks because every claim is sourced from a real document, about the wrong entity. Using a controlled factorial benchmark across 13 models, we find DG rates spanning 8-87% at peak adversarial conditions. Medical and biomedical fine-tuned models reach up to 86.7%; domain specialization amplifies DG risk, motivating entity-attribution checks for clinical RAG.

## One-Liner

Deceptive Grounding：临床 RAG 可以零幻觉/真实引用却把药物 Y 的证据归于药物 X，对抗条件下 13 模型 DG 率达 8–87%
