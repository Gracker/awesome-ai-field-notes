# ReTrace: Distilling Tool-Using Agents into Planner-Free Workflows

- **ID**: d8eb7a8e
- **原文链接**: https://arxiv.org/abs/2611.14492
- **PDF**: https://arxiv.org/pdf/2611.14492
- **作者**: Kaiyuan Hou, Yang Ping Kuo, Indranil Bhattacharya, Rohith Nama, Arushi Gupta, Carlos D. Castillo, Prathap Ramachandra, Xiaofan Jiang, Francesco Carbone
- **日期**: 2026-11-10
- **更新**: 2026-11-10
- **分类**: agents
- **来源类型**: paper
- **标签**: agents, workflow, sop-automation, agent-distillation, cost
- **质量评分**: 4/5
- **抓取时间**: 2026-11-12T04:22:28Z

---

## 中文导读

ReTrace 把"LLM agent 每步都要调一次模型"的 SOP 执行过程固化成可复用工作流：agent 每次工具调用都会写下推理说明，ReTrace 从中提取每一步背后的触发条件，跨多次运行合并成紧凑规则文档，再编译成由代码（而非 LLM）选择下一步的可执行工作流；只有最后编译阶段依赖编排平台，规则文档本身可移植到不同平台。生产平台 79 个流程上完成率 93.8%（agent 96.8%），单任务成本低 24%；tau2-Bench 成功率 75.8%（agent 80.6%），耗时从 170 秒降到 1.3 秒；SOP-Bench 8 个流程上不经修复落后 few-shot 生成（80.6% vs 83.6%），经标注训练失败的修复轮反超到 87.8%，0.40 秒/任务（agent 85.5% 需 46.6 秒）。

## 为什么值得关注

agent distillation 的关键原料不是轨迹本身，而是 agent 写下来的"为什么"。

工具调用序列只记录了动作，回答不了"什么条件下该走这一步"；ReTrace 的做法是直接读 agent 每步的推理说明来抽条件，再跨运行合并成规则文档。这给出一个可操作的 SOP 固化配方：对确定性流程，代码化工作流用千分之一量级的时延（170s→1.3s）换 3 个点以内的完成率损失，成本降 24%。SOP-Bench 的对照同时划出了边界——只靠 few-shot 让 LLM 直接生成规则文档不够（80.6% 落后），必须用标注过的训练失败跑修复轮才能反超到 87.8%。

## 关键信息

- 论文标题：ReTrace: Distilling Tool-Using Agents into Planner-Free Workflows
- 作者：Kaiyuan Hou, Yang Ping Kuo, Indranil Bhattacharya, Rohith Nama, Arushi Gupta, Carlos D. Castillo, Prathap Ramachandra, Xiaofan Jiang, Francesco Carbone
- arXiv：https://arxiv.org/abs/2611.14492
- 发布时间：2026-11-10
- arXiv 分类：cs.AI; cs.LG; cs.MA
- 关联标签：agents, workflow, sop-automation, agent-distillation, cost
- 备注：生产平台实测 + tau2-Bench + SOP-Bench 三个场景；修复轮（repair rounds）对最终完成率影响显著

## English Abstract

Business process automation runs the same Standard Operating Procedure (SOP) again and again on new inputs. Large Language Model (LLM) agents can follow an SOP written in natural language, but they call an LLM to choose every step of every run, which adds latency and cost at scale. We present ReTrace, which turns an SOP and a few logged agent runs into a reusable workflow in which code, not an LLM, selects the next step. The agent's reasoning, the explanation it writes with each tool call, often states why it took an action; the tool calls alone do not. ReTrace extracts the condition behind each step, merges these conditions across runs into a compact rule document, and generates an executable workflow from it. Only this last stage depends on the platform, so rule documents can be compiled for different orchestration platforms. On 79 procedures from our production platform, ReTrace workflows reach 93.8% completion, against 96.8% for the agent, at 24% lower cost per task. On tau2-Bench, they reach 75.8% task success (agent: 80.6%) and run in 1.3s instead of 170s; three rounds of repair on training failures lift k=2 workflows from 66.7% to 81.2%. On eight SOP-Bench procedures, ReTrace without repair trails few-shot generation (80.6% vs. 83.6%), but repair from labeled training failures lifts it to 87.8% at 0.40s per task, compared to 85.5% in 46.6s for the agent.

## English Summary

LLM agents can follow natural-language SOPs but call an LLM at every step, adding latency and cost at scale. ReTrace turns an SOP plus a few logged agent runs into a reusable workflow where code, not an LLM, selects the next step: it extracts the condition behind each step from the agent's written reasoning, merges conditions across runs into a compact rule document, and compiles that document into executable workflows for different orchestration platforms. On 79 procedures from a production platform, ReTrace reaches 93.8% completion (agent: 96.8%) at 24% lower cost per task; on tau2-Bench 75.8% task success (agent: 80.6%) running in 1.3s instead of 170s; on SOP-Bench, repair rounds lift it to 87.8% at 0.40s per task vs 85.5% at 46.6s for the agent.

## Obsidian Notes

- 内容获取路径：`opencli arxiv paper 2611.14492 -f json` 一次成功，以元数据+摘要回填。
- 中文导读与价值判断均锚定在论文摘要、作者、日期与分类信息上；未补充论文摘要之外的实验细节。
- 现代站点生成器按 `content/d8eb7a8e.md` 查找内容页；本文件写入 canonical content 目录，而不是 `openclaw/content/`。
