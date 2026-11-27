# A Bias in Disguise: Tiny Gradient Edits Stop a Small Language Model's Thinking Loops and Complement a Frontier Model's Weight Edit

- **ID**: dde555db
- **原文链接**: https://arxiv.org/abs/2611.33133
- **PDF**: https://arxiv.org/pdf/2611.33133v1
- **作者**: Hussamuddin Syed
- **日期**: 2026-11-24
- **更新**: 2026-11-24
- **分类**: models
- **来源类型**: paper
- **标签**: weight-edit, reasoning, qwen, math
- **质量评分**: 4/5
- **抓取时间**: 2026-11-26T04:20:26Z

---

## 中文导读

Qwen3.5-0.8B 在思考模式下极少闭合 think 块：4k token 预算内 MATH-500 仅 1-2 题完成，准确率 15.4%本文为 GPT-6 Astra 无梯度改 13.1 万权重的演示补上梯度基线，并将两种编辑组合：只微调梯度最大的 140-139750 个权重（50 条样本即可，单卡数分钟），4k 预算思考模式成绩提到 39.0-45.5%梯度集中在前三层最近平常的通道；模型无偏置项，编辑等效于向残差流加三个固定向量Astra 编辑复现 52.1%；梯度编辑在 16k 以内各预算更优；两者半强度叠加达 62.2%，比单用 Astra 高 10 分

## 为什么值得关注

Top-gradient weight edits fix Qwen3.5-0.8B thinking loops and stack with a frontier model's weight edit to 62.2% MATH-500

为被广泛讨论的无梯度改权重演示补上缺失的梯度基线，并把两种编辑叠加到 62.2%；梯度集中在前三层最近平常通道、编辑等效于向残差流加三个固定向量的发现，把大改动的有效自由度压缩到极小。

## 关键信息

- 论文标题：A Bias in Disguise: Tiny Gradient Edits Stop a Small Language Model's Thinking Loops and Complement a Frontier Model's Weight Edit
- 作者：Hussamuddin Syed
- arXiv：https://arxiv.org/abs/2611.33133
- 发布时间：2026-11-24
- arXiv 分类：cs.LG, cs.CL
- 关联标签：weight-edit, reasoning, qwen, math

## English Abstract

Qwen3.5-0.8B rarely finishes reasoning in thinking mode: at a 4,096-token budget only 1 or 2 of 500 MATH-500 answers close their think block (two seeds), and accuracy is 15.4%. A recent demonstration had GPT-6 Astra edit 131,072 of the model's weights without gradients and reported MATH-500 rising from 7.9% to 48.1% at a 32,768-token budget. We provide the missing gradient baseline, then combine the two edits. Fine-tuning only the 140 to 139,750 weights with the largest gradient, on the model's own correct answers to MATH training problems, raises thinking-mode MATH-500 at 4k tokens to 39.0-45.5% after 2-9 minutes of training on one GPU; 50 training examples suffice, and 1,398 random positions give only 16.3%. The gradient concentrates the edit on the most nearly constant channel of each of the first three layers. Because the model has no bias terms, an edit confined to those channels acts as a constant vector added to the residual stream: adding three fixed vectors to the unedited model matches the accuracy of such an edit. Under the Astra protocol (32k tokens, presence penalty 1.5), the Astra edit scores 52.1% (finished and correct) in our reproduction and our full-strength edits reach 45.6-45.7%, but ours win at every budget up to 16k tokens (39.5% against 6.7% at 4k). The two edits are complementary. The Astra edit plus our 139,750-weight edit at half strength scores 62.2% at 32k, 10 points above the Astra edit alone (p = 3e-9), with half as many tokens; our half-strength edit alone scores 46.7%.

## English Summary

Qwen3.5-0.8B rarely closes its think block in thinking mode: within a 4,096-token budget only 1-2 of 500 MATH-500 answers finish, at 15.4% accuracy. It supplies the missing gradient baseline to the widely discussed demo where GPT-6 Astra edited 131,072 weights without gradients, then combines both edits. Fine-tuning only the 140-139,750 largest-gradient weights on the model's own correct answers lifts 4k thinking-mode MATH-500 to 39.0-45.5% after minutes on one GPU; 50 examples suffice while 1,398 random positions give only 16.3%. The gradient concentrates on the most nearly constant channel of the first three layers, so with no bias terms the edit acts as three fixed vectors added to the residual stream. The Astra edit reproduces at 52.1%; stacked at half strength with the gradient edits they reach 62.2% at 32k tokens, 10 points above the Astra edit alone.

## Obsidian Notes

- 内容由 `opencli arxiv paper` 拉取 arXiv 元数据与摘要生成。
- 中文导读与价值判断均锚定在条目已有摘要、论文摘要、作者、日期与分类信息上；未补充论文摘要之外的实验细节。
