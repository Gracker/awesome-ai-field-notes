# Same Request, Different Answer: Quantization Amplifies Cache-Induced Divergence in LLM Serving

- **ID**: ee3cd5f7
- **原文链接**: https://arxiv.org/abs/2609.04748
- **PDF**: https://arxiv.org/pdf/2609.04748
- **作者**: Aditi Patodiya
- **发布日期**: 2026-09-04
- **条目分类**: infra
- **来源类型**: paper
- **标签**: llm-serving, prefix-cache, quantization, reproducibility, agent-eval
- **质量评分**: 5/5
- **简评作者**: openclaw
- **抓取时间**: 2026-09-09 (UTC+8)

---

## 中文导读

Prefix caching 是开源推理引擎默认开的优化，复用相同前缀的 KV 张量。但论文测出它对可复现性的代价随量化加深：固定模型、解码参数、种子、请求顺序，串行 batch=1 跑 80 episode 的多轮 agentic tool-use 任务，开启 cache 时 16-bit 下 36.2% episode 改变 agent 轨迹，4-bit 下飙到 75.0%；关闭 cache 在所有 4 个 weight format 下 800 episode 都 bit-identical（其他非确定性源 ≤0.5%）。结论：cache state 默认不重置是 LLM serving 的隐含坑，做 agent 评估不修这个坑就会出现'同一个模型同一个 benchmark 跑出两个结论'的尴尬。

## 为什么值得关注

Prefix cache 默认不重置是 LLM serving 的隐含坑：4-bit 下 75% episode 改变 agent 轨迹，做 agent 评估不修这个会闹笑话。

要点摘录：

- 来源：arXiv 论文页面元数据 + 摘要
- 标签：llm-serving, prefix-cache, quantization, reproducibility, agent-eval
- 日期：2026-09-04

## 关键信息

- 标题：Same Request, Different Answer: Quantization Amplifies Cache-Induced Divergence in LLM Serving
- URL：https://arxiv.org/abs/2609.04748
- 抓取日期：2026-09-09

## English Abstract / Excerpt

Prefix caching reuses KV tensors across requests sharing a prompt prefix and ships enabled by default. The paper measures its reproducibility cost and finds it rises sharply with quantization: holding model, decoding, seed, and request order fixed, an 80-episode multi-turn agentic tool-use workload changed trajectory on 36.2% of episodes at 16-bit and 75.0% at 4-bit; with caching disabled, 800 episodes were bit-identical across all four weight formats (other non-determinism ≤0.5%). The takeaway: cache state not being reset by default is an implicit landmine in LLM serving; agent evaluators that ignore it will see 'two answers from the same model on the same benchmark'.
