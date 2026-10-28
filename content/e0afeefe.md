# SEMA-Auto: Sighted and Efficient Multi-Turn Attack with Autonomy

- **ID**: e0afeefe
- **原文链接**: https://arxiv.org/abs/2610.35743
- **PDF**: https://arxiv.org/pdf/2610.35743
- **作者**: Mingqian Feng, Xiaodong Liu, Weiwei Yang, Chenliang Xu, Jialin Song, Qiyao Ma, Chengquan Guo, Carolyn Buractaon, Christopher White, Jianfeng Gao
- **日期**: 26 Oct 2026
- **更新**: N/A
- **分类**: models
- **来源类型**: paper
- **标签**: jailbreak, multi-turn-attack, red-teaming, reinforcement-learning, llm-safety
- **质量评分**: 4/5
- **抓取时间**: 2026-10-28T04:32:09Z

---

## 中文导读

微软多轮越狱攻击器 SEMA-Auto：读取受害者回复成功后自主终止会话，无需在环评估器两阶段训练（合成自举微调建立攻击目标与终止决策概念，决策监督强化学习联合优化越狱奖励与逐轮终止决策）后，在多数据集/受害者/裁判上取得 SOTA 攻击成功率且轮数几乎最少：AdvBench 对 DeepSeek-V4-Flash 达 76.0% ASR@1（平均 3.0 轮）；对 GPT-5.4Claude-Haiku-4.5GPT-6-Astra 等安全强化前沿模型，HarmBench 平均 59.6% ASR@1，超此前 SOTA 13.8 个百分点

## 为什么值得关注

微软多轮越狱攻击器 SEMA-Auto：读取受害者回复成功后自主终止会话，无需在环评估器两阶段训练（合成自举微调建立攻击目标与终止决策概念，决策监督强化学习联合优化越狱奖励与逐轮终止决策）后.

Extra grounding: code released at https://github.com/microsoft/SEMA; subject cs.CL.

## 关键信息

- 论文标题：SEMA-Auto: Sighted and Efficient Multi-Turn Attack with Autonomy
- 作者：Mingqian Feng, Xiaodong Liu, Weiwei Yang, Chenliang Xu, Jialin Song, Qiyao Ma, Chengquan Guo, Carolyn Buractaon, Christopher White, Jianfeng Gao
- arXiv：https://arxiv.org/abs/2610.35743
- PDF：https://arxiv.org/pdf/2610.35743
- 发布时间：26 Oct 2026
- 更新时间：N/A
- arXiv 分类：Computation and Language (cs.CL)
- 关联标签：jailbreak, multi-turn-attack, red-teaming, reinforcement-learning, llm-safety

## English Abstract

Existing jailbreak attackers fall into two classes: static planners fix their single- or multi-turn adversarial plans in advance, remaining simple but losing sight of the victim's replies, wasting turns and limiting transferability; interactive generators read each victim reply to generate the next-turn attack but require in-loop evaluators for success signals or hints, incurring substantial costs and inflated performance. Bridging this gap, we propose SEMA-Auto, a sighted and efficient multi-turn attacker with autonomy, interacting with the victim model and terminating the session by itself upon success. To stabilize its behaviors and boost its capabilities, SEMA-Auto is trained in two stages. Synthetic bootstrap tuning installs the notion of attack targets and conforming decisions by fine-tuning the base model with bootstrapped trajectories. Decision-supervised reinforcement learning then optimizes two objectives jointly yet separately, reinforcing the attack with higher jailbreak reward while supervising the decision at each turn against an absolute target. Our method achieves state-of-the-art (SOTA) attack success rates (ASR) across multiple datasets, victims, and judges, outperforming all static and interactive baselines, within almost the fewest turns, demonstrating both effectiveness and efficiency. For example, SEMA-Auto performs a 76.0% ASR@1 within an average of 3.0 turns against DeepSeek-V4-Flash on AdvBench, while the best static baseline is 54.8% with fixed 7 turns and the best interactive baseline is 43.8% in 3.7 turns. Against safety-hardened frontier models, GPT-oss-120B, GPT-5.4, Claude-Haiku-4.5, and GPT-6-Astra, our counter-trained attacker achieves an average 59.6% ASR@1 on HarmBench, 13.8% over prior SOTA. Our code is available at: https://github.com/microsoft/SEMA

## English Summary

Multi-turn jailbreak attacker that reads victim replies yet needs no in-loop evaluator: SEMA-Auto interacts with the victim and terminates the session itself upon success. Two-stage training: synthetic bootstrap tuning installs attack targets and termination decisions, then decision-supervised RL jointly reinforces jailbreak reward and per-turn stop decisions. It sets SOTA attack success rates across datasets, victims, and judges with almost the fewest turns: 76.0% ASR@1 in an average 3.0 turns against DeepSeek-V4-Flash on AdvBench (best static baseline 54.8% at fixed 7 turns; best interactive 43.8% in 3.7). Against safety-hardened frontier models (GPT-oss-120B, GPT-5.4, Claude-Haiku-4.5, GPT-6-Astra) it averages 59.6% ASR@1 on HarmBench, 13.8 points over prior SOTA. Code: github.com/microsoft/SEMA.

## Obsidian Notes

- 内容获取路径：优先尝试 `opencli arxiv paper 2610.35743 -f json`，遇 arXiv API HTTP 429 后改由 arXiv abs 页面元数据与摘要回填。
- 中文导读与价值判断锚定在条目已有摘要、来源元数据/原文段落、作者、日期与分类信息上；未补充摘要之外的实验细节。
- 本文件写入 canonical content 目录（content/e0afeefe.md），现代站点生成器按 entry id 查找内容页。
