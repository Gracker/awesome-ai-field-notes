# CAGE: Certified Authorization under Typed-Return Uncertainty for Tool-Using Agents

> Source: https://arxiv.org/abs/2607.29190
> Authors: Blaise Delattre, Cong Wang, Yang Cao
> Published: 2026-07-31
> Categories: cs.AI
> PDF: https://arxiv.org/pdf/2607.29190
> Fetched: 2026-11-28T04:20:23Z via opencli arxiv paper 2607.29190 -f json (metadata backfill)

## Abstract

Tool-using LLM agents act on typed tool returns, records pairing provenance and categorical fields with numerical values. Runtime permission gates generally authorize the observed return and action, leaving the decision unprotected against small errors in how the return was bound to its source. We ask whether a candidate action stays authorized over a declared neighborhood of plausible correctly bound returns: one admissible binding fault plus bounded numerical drift. We prove that certifying the categorical and numerical channels separately does not compose: perturbations that are safe on each channel alone can jointly turn the same action unsafe. CAGE certifies this joint neighborhood directly, enumerating the discrete branches exactly and certifying the continuous perturbation within each branch. Across synthetic, policy-as-code, regulatory, and real-transaction settings, CAGE removes the in-budget false allows that accurate pointwise gates admit, while keeping a useful fraction of decisions autonomous. When the policy is executable, CAGE-Exact certifies the policy itself; otherwise CAGE-Lip and CAGE-RS certify a learned gate under an explicit, measured fidelity assumption.

## Key Findings

- Runtime permission gates generally authorize the observed tool return and action, leaving decisions unprotected against small errors in how the return was bound to its source.
- The core question: does a candidate action stay authorized over a declared neighborhood of plausible correctly bound returns - one admissible binding fault plus bounded numerical drift?
- Impossibility result: certifying the categorical and numerical channels separately does not compose; perturbations safe on each channel alone can jointly make the same action unsafe.
- CAGE certifies the joint neighborhood directly rather than per-channel, covering typed tool returns that pair provenance and categorical fields with numerical values.
- Code released at github.com/tdsai-lab/cage-agent-authorization (per the paper comment).

## 中文概要

工具型 agent 的运行时权限门通常只对"观察到的工具返回+动作"做逐点授权，返回与来源的绑定一旦出小错，决策就失去保护CAGE 把问题定义为：在一个可声明的邻域内（一次可接受的绑定错误+有界数值漂移），动作是否始终处于授权范围论文证明分类通道与数值通道分开认证并不可复合各自安全的扰动叠加后可使同一动作越权；CAGE 直接认证联合邻域：离散分支精确枚举分支内连续扰动界定（策略可执行用 CAGE-Exact，否则 CAGE-Lip/CAGE-RS 在实测保真假设下认证学习到的门）在合成policy-as-code监管与真实交易场景中，CAGE 消除了逐点门会放行的预算内误授权，同时保住可用的自动化比例

## Note

Code: https://github.com/tdsai-lab/cage-agent-authorization
