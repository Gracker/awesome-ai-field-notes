# WeAct: Dynamic Weight Switching as Agent Actions

- **ID**: c1bc0b4e
- **原文链接**: https://arxiv.org/abs/2610.26847
- **PDF**: https://arxiv.org/pdf/2610.26847v2
- **作者**: Rui Shi, Xunjian Yin, Jiacheng Sang, Zichuan Liu, Shuyan Zhou
- **日期**: 2026-10-19
- **更新**: 2026-10-20
- **分类**: agents
- **来源类型**: paper
- **标签**: agents, lora, adapters, continual-learning, long-horizon
- **质量评分**: 4/5
- **抓取时间**: 2026-10-21T12:28:13.218278+00:00

---

## 中文导读

长程 agent 要从交错轨迹里学异质能力：更新共享参数学新能力会损害已有能力（灾难性遗忘），而轨迹推进的不同阶段需要的能力又不同，常规联合训练与静态 adapter 合并在整个执行期锁死一套参数。WeAct（Weight-level Internal Actions）在冻结骨干上训练能力专属 LoRA，并把 adapter 选择挂进 agent 动作空间——内部动作走模型原生 tool-calling 接口，在同一共享上下文里按需组合能力。8 个 deep-research 基准上，Qwen3-32B 加 WeAct 平均准确率比全量微调对照高 6.2%（算力更省），比最强静态 LoRA 合并方法高 27.5%。WeAct 还支持模块化持续适配：新增一个代码计算 adapter 扩能力、更新已有写作 adapter 提报告质量，骨干与其余 adapter 都不动。

## 为什么值得关注

把换 LoRA 做成 agent 动作：能力专属适配器进原生工具调用空间，同一上下文按需组合；8 个深研基准上对最强静态 LoRA 合并 +27.5%，对全量微调 +6.2% 且算力更省，还能只动单个 adapter 做持续适配。做 agent 能力栈的值得看它的动作空间设计。

## 关键信息

- 论文标题: WeAct: Dynamic Weight Switching as Agent Actions
- arXiv: https://arxiv.org/abs/2610.26847
- PDF: https://arxiv.org/pdf/2610.26847v2
- 发布时间: 2026-10-19
- 备注: 24 pages, 14 figures, 12 tables, including references and appendices
- arXiv 分类: cs.LG, cs.AI, cs.CL
- 关联标签: agents, lora, adapters, continual-learning, long-horizon

## English Abstract

Long-horizon agents must learn heterogeneous capabilities from interleaved trajectories. Updating shared parameters to learn new capabilities can degrade previously acquired ones, resulting in catastrophic forgetting. As a trajectory unfolds, different stages may require different capabilities, yet conventional joint training and static adapter merging maintain a fixed parameter configuration throughout execution. We introduce WeAct (Weight-level Internal Actions), which trains independent capability-specific LoRA adapters over a frozen backbone and adds adapter selection to the agent's action space. These internal actions use the model's native tool-calling interface for on-demand capability composition in a shared context. Across eight deep-research benchmarks, Qwen3-32B with WeAct improves average accuracy by 6.2% relative to full fine-tuning counterparts despite using less compute, and by 27.5% relative to the strongest static LoRA-merging method. WeAct also supports modular continual adaptation, by adding a new code computation adapter to expand the agent's capabilities and updating the existing writing adapter to improve report quality. Both updates leave the backbone and other adapters unchanged, supporting modular continual adaptation in agents.

## English Summary

Long-horizon agents learn heterogeneous capabilities from interleaved trajectories, but updating shared parameters causes catastrophic forgetting, and joint training or static adapter merging locks one parameter configuration for the whole run. WeAct (Weight-level Internal Actions) trains capability-specific LoRA adapters over a frozen backbone and adds adapter selection to the agent's action space via the model's native tool-calling interface, composing capabilities on demand in a shared context. Across eight deep-research benchmarks, Qwen3-32B with WeAct improves average accuracy by 6.2% over full fine-tuning with less compute and by 27.5% over the strongest static LoRA-merging method; capabilities can be extended (a new code-computation adapter) or refreshed (an updated writing adapter) without touching the backbone or other adapters.

## Obsidian Notes

- 内容由 `opencli arxiv paper 2610.26847` 拉取 arXiv 元数据与摘要生成。
- 中文导读与价值判断均锚定在条目已有摘要、论文摘要、作者、日期与分类信息上；未补充论文摘要之外的实验细节。
