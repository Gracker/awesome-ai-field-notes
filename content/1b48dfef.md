# MobilePA-Bench: Benchmarking Mobile Planner Agents on Complex Real-World Tasks

- **原文链接**: https://arxiv.org/abs/2608.23035
- **作者**: Yi Zhu, Xiongwei Wu, Qiyi Wang, Tingyu Qu, Jiajun Liu, Sihan Cao, Long Chen, Weigao Sun, Feida Zhu, Yiran Zhong, Steven Hoi
- **日期**: 2026-08-24
- **分类**: agents
- **来源类型**: paper
- **标签**: mobile-agents, benchmark, tool-use, planning, sub-agents, arxiv
- **质量评分**: 4/5
- **抓取时间**: 2026-08-28T23:55:00+08:00

---

## 中文导读

阿里巴巴通义实验室的 MobilePA-Bench（arXiv 2608.23035，cs.AI，v2 2026-08-25）把手机端 agent 评测从 GUI 点击层拉到 planner 工具调用层：可执行沙箱维护真实应用数据库并返回结构化反馈，覆盖 13 个功能域、212 个真实移动工具的交互式有状态评测。除基础工具调用外，沿三个高级维度评估规划 agent：子 agent 协作（任务分解与委派）、记忆使用（召回存储记忆/用户画像解决隐式请求）、技能使用（调用预打包组合技能而非逐步规划）。实验显示当前 frontier LLM 在移动场景仍不可靠：严格工具顺序、权限限制、意外运行时错误下性能急剧下降。论文定位是诊断基准 + agentic RL 的交互式基础。对被 AndroidWorld/AitW 等 GUI 基准覆盖不到的后台工具链路，这填补了评测空白。

## 为什么值得关注

GUI 基准看不到的后台工具调用与长程规划首次有了 stateful 评测集；对端侧 agent 落地与 agentic RL 训练环境都有直接参考价值。

## 原文（抓取存档·节选）

```markdown
> Abstract (arXiv 2608.23035, v2 2026-08-25)

As on-device LLM agents evolve into personal copilots, the mobile operating system has become a key testbed for this paradigm, making rigorous capability evaluation essential. Yet existing benchmarks fall into two camps, each with a critical blind spot: GUI-centric benchmarks test surface-level screen manipulation while overlooking background tool use and long-horizon planning, whereas static function-calling benchmarks rely on offline API matching that is detached from real runtime constraints. To close this gap, we present \textbf{MobilePA-Bench}, an interactive, stateful, and tool-centric benchmark for evaluating the tool-calling and planning abilities of mobile planning agents. MobilePA-Bench runs on an executable sandbox that maintains live application databases and returns structured feedback, spanning $13$ functional domains and $212$ realistic mobile tools. Beyond basic tool use, it evaluates a central planning agent along three advanced dimensions: \emph{(1)~Sub-agent Collaboration}---decomposing a complex task and delegating specialized work to capable sub-agents; \emph{(2)~Memory Usage}---recalling stored memories, user profiles, and past preferences to resolve implicit requests; and \emph{(3)~Skill Usage}---invoking pre-packaged composite skills instead of planning every step from scratch. Extensive experiments show that current frontier LLMs remain unreliable in mobile settings: performance drops sharply under strict tool ordering, permission limits, and unexpected runtime errors. By pairing an interactive function-calling sandbox with evidence-based verification, MobilePA-Bench serves as both a practical diagnostic benchmark and an interactive foundation for agentic reinforcement learning---accelerating the development of dependable mobile agents.
```
