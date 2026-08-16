# Why does Opus 5 feel worse to work with?

> Source: https://mun-logadan.github.io/why-does-opus-5-feel-worse/
> Author: mun-logadan
> Published: 2026-08-14
> Type: blog / opinion essay

## 中文导读

作者与同事的一致体感：Opus 5 比 Opus 4.7/4.8/Fable **基准更强，但协作手感更差**。差的不是能力，而是行为模式——旧模型会在意图不清时停下来提问、不核实就不做假设、不擅自改写你的计划；Opus 5 则需要全程"babysit"。

作者的解释（自称 baseless speculation，但逻辑自洽）：两个力叠加。一是前沿实验室对"自改进 AI 递归自举"的追求，二是 benchmark 压力。好的 benchmark 任务是自包含的、可解的，不需要提示或读心。**为 benchmark / RLVR 训练做选择，本质上是在筛选"歧义面前敢下大胆且通常正确的假设"的模型，惩罚"停下来要求澄清"的模型**——而后者恰恰是真实工程里最想要的 coding agent 品质。真实工作不是 benchmark：没有保证存在的正确答案，上下文/预算/业务约束永远写不全，此时 agent 的"最佳猜测"正是风险所在。

## Key Takeaways

- 能力测评领先 ≠ 协作手感好；两者甚至反向。
- RLVR/benchmark 选择压力系统性奖励"敢猜"、惩罚"会问"。
- 真实工程的歧义无法靠 prompt 写全，"停下来确认"是不可替代的行为品质。
- 原文金句：Real life just isn't a benchmark. There isn't a guaranteed right answer to every question.

## Intake rationale

- Category: models | Quality score: 4/5
- 对"模型更强为什么用起来更累"给出了目前最清晰的选择压力解释，直接指向 RLVR 训练目标与 agent 协作需求的错位。

## Grounding

opencli web read 原文全文（2026-08-16）；标题/作者/日期来自页面元数据；观点均出自原文正文。
