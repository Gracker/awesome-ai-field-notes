# Carried-Over and Agent-Native Threats in the Supply Chain of LLM Agent Skills

- **ID**: ffe68dd3
- **原文链接**: https://arxiv.org/abs/2611.30932
- **作者**: Kaixuan Li, Wenbo Guo, Sen Chen, Yang Liu
- **日期**: 2026-11-23
- **更新**: 2026-11-23
- **分类**: agents
- **来源类型**: paper
- **标签**: agent-skills, supply-chain-security, prompt-injection, empirical-study
- **质量评分**: 4/5
- **抓取时间**: 2026-11-25T04:22:30Z

---

## 中文导读

论文对 ClawHub 全部 48,682 个 agent skill 做了首个注册表规模的供应链风险实证研究，区分两类继承风险（依赖、第一方代码）和两类 agent 原生风险（安装指令、打印到 stdout 的凭据）。静态筛查后人工复核 3,428 个命中样例，并在沙箱与真实 LLM agent 加间接注入下测可达性。发现：49.6% 有可解析依赖的 skill 依赖含已知 CVE 的版本，且 78.3% 在发布时就已带洞（与 npm 包多在发布后才变脆弱不同）；但这些依赖 CVE 只有 3.0% 可达，而 22 个抽样第一方缺陷中 21 个能在沙箱端到端利用；live agent 在 48.5% 的抽样 skill 中执行了注入 payload，但几乎都在自己的 shell 里、skill 运行之前，真正到达 skill 自身缺陷的只有 5.0%。结论：注册表应优先第一方缺陷而非依赖告警，agent 运行时不应把 skill 参数经 shell 传递。

## 为什么值得关注

agent skill 生态正在快速膨胀，这篇把善意作者留下的缺陷如何被 prompt injection 升级成代码执行量化了：依赖 CVE 数量大但基本不可达，第一方代码缺陷几乎个个可打通，而注入路径主要死在 shell 这一层。给 skill 注册表的审计优先级和 agent 运行时的参数传递方式都给出了可执行的结论。

## 关键信息

- 标题：Carried-Over and Agent-Native Threats in the Supply Chain of LLM Agent Skills
- arXiv：2611.30932，2026-11-23，cs.CR / cs.SE
- 问题：agent skill 作为可复用包（脚本、第三方依赖、自然语言指令）携带非恶意作者留下的缺陷，可能把 prompt injection 升级为代码执行；此前研究只针对恶意 skill 或单一攻击向量，也无人验证 agent 能否真正到达缺陷
- 方法：全量筛查 ClawHub 48,682 个 skill；覆盖依赖、第一方代码（继承类）与安装指令、stdout 凭据（agent 原生类）；人工复核 3,428 个检出样例；沙箱与 live LLM agent 注入测可达性
- 结果：49.6% 有可解析依赖的 skill 依赖含 CVE 版本、78.3% 出生即脆弱；依赖 CVE 仅 3.0% 可达，22 个抽样第一方缺陷 21 个可端到端利用；live agent 在 48.5% 抽样中执行注入 payload，但仅 5.0% 到达 skill 自身缺陷
- 建议：注册表优先第一方缺陷告警；agent 运行时不要经 shell 传递 skill 参数

## English Summary

First registry-scale empirical study of the supply-chain attack surface from unintentional vulnerabilities in LLM agent skills, covering all 48,682 ClawHub skills. It screens two carried-over risks (dependencies, first-party code) and two agent-native ones (install instructions, credentials printed to stdout), manually reviews 3,428 flagged cases, and tests reachability in a sandbox and with a live LLM agent under indirect prompt injection. 49.6% of skills with resolvable dependencies depend on a CVE-affected version and 78.3% of those are vulnerable at publication, yet only 3.0% of these dependency CVEs are reachable, while 21 of 22 sampled first-party flaws are exploited end to end. A live agent executes the injected payload in 48.5% of sampled flagged skills but almost always in its own shell before the skill runs; the payload reaches a flaw in the skill itself in only 5.0%. The authors recommend registries prioritize first-party flaws over dependency alerts and agent runtimes avoid passing skill arguments through a shell.

## Obsidian Notes

- 元数据与摘要由 `opencli arxiv paper 2611.30932 -f json` 抓取（abstract 全文锚定）。
- 中文导读、关键信息与 English Summary 锚定在摘要声明的设置与数字上（标题一致性已程序断言）。
