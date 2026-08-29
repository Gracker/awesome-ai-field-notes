# Persona-Execution Separation: An Architecture Pattern for Evolving LLM Agents under Execution Audit

- **ID**: ea4fa68e
- **原文链接**: https://arxiv.org/abs/2608.27427
- **PDF**: https://arxiv.org/pdf/2608.27427v1
- **作者**: Yisen Xi
- **日期**: 2026-08-27
- **更新**: 2026-08-27
- **分类**: agents
- **来源类型**: paper
- **标签**: agents, architecture, audit, dlp, arxiv
- **质量评分**: 4/5
- **抓取时间**: 2026-08-29T12:59:16+08:00

---

## 中文导读

Persona-Execution Separation（PES，arXiv 2608.27427，36 页，2026-08-27）处理治理型组织中 LLM 智能体的一个结构矛盾：人格（指令/语气/自我呈现）需要自由演化，执行（有状态、被审计的工作）必须保持可追溯，而单一信任域无法廉价地兼得两者。PES 把人格与执行放进不同信任域，用受治理的契约桥连接：人格单宿且可漂移；执行无面孔且被审计；状态摘要可返回，数据体留在限制域（分级 DLP 例外除外），身份保持连续；审批矩阵、DLP 与审计约束跨越这条边界。论文给出代表性不可区分性下的论证：满足自由漂移、执行可追溯、解耦三目标的任何单域机制，最终都会重新引入类型化变更对象、外部闸门与稳定审计锚点——即以更高耦合成本重建 PES。附一个受监管数字员工平台的开发/试点案例（一个月内五项决策、各带被否备选），机制检查发现人格扰动下执行侧无重校验等缺口，并确认隔离靠的是架构规则而非偶然接线。

## 为什么值得关注

把"人格可漂移、执行可审计"从口号落成可检查的架构规则：对要在合规环境里跑多用户 agent 的团队，契约桥、审批矩阵与分级 DLP 是可以直接对照自查的清单；不可分性论证则说明绕开这套结构的替代方案最终只是它的劣化版。

## 原文（抓取存档·节选）

```markdown
> Abstract (arXiv 2608.27427, v1 2026-08-27, comment: 36 pages)

Large language model (LLM) agents in governed organizations must let the persona (instructions, tone, self-presentation) evolve freely, while keeping execution (stateful, audited work) traceable. A single trust domain does not satisfy both cheaply. We present Persona-Execution Separation (PES): persona and execution reside in different trust domains, connected by a governed contract bridge. The persona is singly-homed and may drift; execution is faceless and audited. Status summaries may return; data bodies remain in the restrictive domain except a graded data-loss-prevention (DLP) exception; identity stays continuous. An approval matrix, DLP, and audit enforce the crossing. PES follows from three goals---free drift, execution traceability, and decoupling. Under LLM representational indistinguishability, any single-domain mechanism that meets all three must re-introduce typed change objects, an external gate, and a stable audit anchor: PES rebuilt at higher coupling cost. A development/pilot case in a regulated digital-employee platform records five decisions over one month, each with a rejected alternative. A mechanism check on the shipped implementation found no execution-side re-validation under persona perturbation (five model configurations) and no persona fingerprint on hard-asserted fields. A probe of a recovered pre-separation build found the governed execution path decoupled from the persona by omission, not by construction; a later wiring change could reverse that isolation, which PES makes an audited architectural rule. The pattern applies when multi-user deployment, execution audit, and expected persona churn hold jointly.
```

## Obsidian Notes

- 内容由 `opencli arxiv paper 2608.27427 -f json` 拉取 arXiv 元数据与摘要生成。
- 中文导读与价值判断均锚定在条目已有摘要、论文摘要、作者、日期与分类信息上；未补充论文摘要之外的实验细节。
