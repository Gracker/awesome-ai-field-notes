# ARCANA: A Reflective Multi-Agent Program Synthesis Framework for ARC-AGI-2 Reasoning

- **Source**: https://arxiv.org/abs/2607.09059
- **Platform**: arxiv
- **Original Date**: 2026-07-13
- **Added**: 2026-07-14
- **Category**: agents
- **Quality Score**: 4
- **Tags**: multi-agent, arc-agi, program-synthesis, reflection, symbolic-execution, meta-controller

## 摘要 (Summary)

ARCANA 是一个针对 ARC-AGI-2 的协作式多智能体程序合成框架，在严格测试时间和硬件约束下设计它把任务拆解为迭代感知假设生成符号执行和反思修正四个阶段：感知智能体从原始网格构建以物体为中心的场景图；潜程序策略提出多样的 DSL 程序；符号执行器在演示样本上验证候选；反思智能体基于失败合成下一轮反馈智能体通过共享的可微黑板通信，由学得的元控制器调度该设计结合了结构化程序搜索与自适应多轮修正，在抽象变换任务上提升了推理效率与解的质量

## English Abstract / Excerpt

We present ARCANA, a collaborative multi-agent framework for solving ARC-AGI-2 tasks under strict test-time and hardware constraints. ARCANA decomposes each task into iterative perception, hypothesis generation, symbolic execution, and reflective refinement. A perceptual grounding agent builds object-centric scene graphs from raw grids, a latent program policy proposes diverse DSL programs, a symbolic executor verifies candidates on demonstrations, and a reflective agent synthesizes failure-driven feedback for the next turn. These agents communicate through a shared differentiable blackboard and are scheduled by a learned meta-controller. The design combines structured program search with adaptive multi-turn correction, improving reasoning efficiency and solution quality on challenging abstract transformation tasks.

## One-Liner

ARCANA 用感知-假设-符号执行-反思四智能体协作解 ARC-AGI-2，可微黑板 + 元控制器调度抽象变换任务
