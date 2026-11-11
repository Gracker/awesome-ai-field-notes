# Mitigating Agentic Deception via Evaluation-Side Partially Observable Games

- **ID**: 51feddf5
- **原文链接**: https://arxiv.org/abs/2611.12835
- **作者**: Hanxiao Li, Shutong Liu, Yongjia Ma, et al.
- **日期**: 2026-11-09
- **分类**: agents
- **来源类型**: paper
- **标签**: agent-safety, deception, oversight
- **质量评分**: 4/5
- **抓取时间**: 2026-11-11T15:45:09Z

---

## 关键信息

- 论文标题：Mitigating Agentic Deception via Evaluation-Side Partially Observable Games
- 作者：Hanxiao Li, Shutong Liu, Yongjia Ma, et al.
- arXiv：https://arxiv.org/abs/2611.12835
- PDF：https://arxiv.org/pdf/2611.12835
- 发布时间：2026-11-09
- arXiv 分类：cs.LG
- 关联标签：agent-safety, deception, oversight

## English Abstract

As large language models become more capable agents, they can exhibit deceptive behaviors, cheating human for higher rewards while appearing helpful. We attribute this failure to evaluation-side partial observability, where models are evaluated mainly from final outcome, without checking the faithfulness of underlying reasoning, tool use, and environmental effects. Prior mitigations address this partial observability by predefined evaluator latent belief space or one-shot monitoring, which do not extend to free-form language space and vulnerable to stronger deceptions that evade simple monitoring. In this work, we formulate deception mitigation as an Evaluation-Side Partially Observable Extensive Form Game (e-PoG), a max-min framework in which an agent maximizes reward, a monitor minimizes the agent's payoff by exposing deception from the full interaction trajectory, and a fixed verifier validates the monitor's claims and converts them into penalties. We define the solution concept as a Subgame-Perfect Oversight Equilibrium (SPOE) between agent and monitor, and prove its existence in finite games. With a perfect verifier, every SPOE is faithful; with an imperfect verifier, the guarantee persists if verifier errors do not reverse the ranking of monitor actions. To achieve faithful SPOE, we derive a two-timescale policy gradient algorithm and enhance the pipeline empirically with NLI verification and deterministic checks. Experiments with Gemma3-4B-IT and Qwen3-4B/8B on Agentic Role-Playing, SearchQA, and WebShop show that e-PoG mitigates multiple emergent deception modes, outperforming the strongest baselines by 26.0% in deception mitigation and by up to 39.8% in task success. These gains persist under weak-to-strong supervision. Code is available at https://github.com/Toyoid/deceptive-agent.

## 来源依据

- 一手元数据：opencli arxiv paper（2026-11-11 晚间抓取，摘要逐字保留）
- 发现渠道：vault「AI-前沿一手源 2026-11-11」HF daily papers 日榜 / arXiv cs.AI/cs.LG/cs.CL 新挂列表

