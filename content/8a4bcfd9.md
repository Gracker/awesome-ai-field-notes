> Source: [Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models](https://arxiv.org/abs/2510.04618) · platform: arxiv · authors: Qizheng Zhang, Changran Hu, Shubhangi Upasani, Boyuan Ma, Fenglu Hong, Vamsidhar Kamanuru, Jay Rainton, Chen Wu, Mengmeng Ji, Hanchen Li, Urmish Thakker, James Zou, Kunle Olukotun · date: 2025-10-06

## TL;DR（中文摘要）

ACE（Stanford/SambaNova 等）把上下文当作可进化的 playbook 处理：生成、反思、策展三个模块化环节做增量式结构化更新，避免 Dynamic Cheatsheet 类全量重写带来的 brevity bias 与 context collapse。AppWorld 上 +10.6%、金融推理 +8.6%，还能在没有标注监督时靠执行反馈适配，适配延迟和 rollout 成本显著低于离线基线。论文记录的 context collapse 案例里，一次 LLM 全量重写把 18282 token、66.7% 准确率的 context 塌缩成 122 token、57.1%，低于 63.7% 的不适配基线。对 agent 记忆系统的直接启示：经验库应长成 append-only 加去重的局部编辑，而不是周期性全量重写。

## Summary (English)

ACE treats contexts as evolving playbooks refined through modular generation, reflection, and curation with structured incremental updates, countering the brevity bias and context collapse of full-rewrite approaches. It gains +10.6% on agents and +8.6% on finance reasoning, adapts without labeled supervision using natural execution feedback, and matches the top production agent on the AppWorld leaderboard with a smaller open-source model.

## 入库依据

opencli arxiv paper 2510.04618 拉取摘要与作者；摘要明确给出 +10.6%/+8.6% 与无监督适配结论；context collapse 数字（18282→122 tokens）来自本地精读笔记 OpenClaw定时任务/Agent实践探索/2026-09-17-Agent实践探索.md 对论文实验的引用。

## 补充

Agentic Context Engineering (ACE), Stanford / SambaNova 等团队, arXiv:2510.04618, first posted 2025-10-06, revised 2026-03-29, cs.LG/cs.AI/cs.CL.
