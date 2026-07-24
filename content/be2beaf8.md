# Train the Model, Not the Reader: Decodability Supervision for Verifiable Activation Explanations

- **ID**: be2beaf8
- **原文链接**: https://arxiv.org/abs/2607.20379
- **PDF**: https://arxiv.org/pdf/2607.20379
- **作者**: Hiskias Dingeto
- **日期**: 2026-07-22
- **标签**: interpretability, ai-safety, activation-explanations, evaluation, arxiv
- **质量评分**: 4/5
- **抓取时间**: 2026-07-24T23:34:25+08:00
- **本地证据**: OpenClaw定时任务/论文流水线/2026-07-24-论文流水线.md

---

## 中文解读

论文质疑用 activation reconstruction score 评价自然语言解释是否 faithful：在 Qwen-2.5-7B verbalizer 上，重构分数高于随机但只有约 2% 的具体断言真正影响重构，说明指标更多衡量大意而不是事实。作者提出 grounded-vs-true cross、evaluator swap 和 RECAP，把解释评估推进到可验证断言层面。

## 为什么值得关注

解释型模型评估不能只看 reconstruction score，应该检查每条自然语言断言是否可被独立 probe 验证。

## English Summary / Abstract

Natural-language autoencoders score explanations of hidden activations by reconstruction: an explanation is deemed faithful if the activation can be regenerated from it. The test is structurally insensitive to individual false claims: if flipping a claim does not change the reconstruction, the claim is never penalized. We show the test is passed in two ways, neither faithful. On a released Qwen-2.5-7B verbalizer, explanations reconstruct well above chance while ~2% of specific claims are reconstruction-dependent, so the score tracks gist, not specific facts. Under exact synthetic ground truth, the standard recipe develops co-adapted private codes (false wording the reconstruction depends on) in 5/5 runs, and fixes that leave the target model unchanged do not help. We contribute two audit protocols, the grounded-vs-true cross and the evaluator swap, and RECAP (Readable Encodings via Co-trained Auxiliary Predictors): linear heads trained alongside the target model to keep designated content decodable. On RECAP-trained sandbox models, fresh verbalizers state the designated content truly and the codes vanish, at a +0.001-nat cost. This replicates on a pretrained Pythia-160M: the content becomes reliably probe-decodable, though a fresh verbalizer conveys it only in part (truth 0.44-0.46 vs a near-zero control). For interpretability, high reconstruction does not certify individual claims. For AI safety, RECAP makes designated internal content independently checkable against probes rather than asserted by prose a model can game: an independent probe scores the verbalizer's true claims above its false ones (AUC 0.96, vs 0.82 without RECAP). Against an adversary that edits an explanation to maximize the reconstruction score while lying (suppressing ~87% of its lie penalty), the RECAP probe still flags the lies (AUC 0.95) while the control probe collapses to chance (0.51).

## Obsidian evidence excerpt

```text
按 Android 17 / API 37 封顶，未纳入 Android 18 / API 38+。

## 今日精选
1. **Train the Model, Not the Reader**：解释忠实度不能只看重构分数，论文给了审计协议和 RECAP 训练方向，适合做一次精读。
2. **PyroDash**：小模型在 token 级决定是否向大模型求助，给出了成本/准确率两个运行点，适合跟 agent 成本控制放在一起看。
3. **License Laundering in AI Supply Chains**：把 Hugging Face 数据集、模型到 GitHub 应用的许可证传递问题量化到 232270 条链，适合做 AI 工程治理材料。

## 今日论文速报
- **Train the Model, Not the Reader: Decodability Supervision for Verifiable Activation Explanations**（Hiskias Dingeto，arXiv:2607.20379，2026-07-22）  
  链接: https://arxiv.org/abs/2607.20379  
  方向: interpretability / AI safety。论文质疑“解释能重构 activation”这一评价方式：摘要报告只有约 2% 的具体断言对重构有依赖，因此分数更像在衡量大意而不是单条事实。作者提出 grounded-vs-true cross、evaluator swap 和 RECAP，让指定内部内容能被 probe 独立检查。

- **PyroDash: Cost-Efficient Token-Level Small-Large Language Model Collaborative Inference**（Niqi Lyu et al.，arXiv:2607.20327，2026-07-22）  
  链接: https://arxiv.org/abs/2607.20327  
  方向: 低成本推理 / small-large collaboration。小模型在生成过程中发出控制 token，决定是否把 query 与部分 reasoning trace 交给冻结大模型。摘要给出的结果是：lambda=0.05 时平均准确率 64.04%，比 LLM-only baseline 高 6.36 个百分点，成本降低 20.4%；lambda=0.6 时 LLM token ratio 为 1.90%，每个样本 0.012 次 LLM 调用，总成本从 49.36 美元降到 1.78 美元。

- **Don't Trust the Label: License Laundering in AI Supply Chains**（James Jewitt et al.，arXiv:2607.20300，2026-07-22）  
  链接: https://arxiv.org/abs/2607.20300  
  方向: AI supply chain / software engineering。作者追踪 232270 条 dataset 到 model 到 appli
```
