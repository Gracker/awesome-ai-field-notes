---
title: "How we built our multi-agent research system"
source: "https://www.anthropic.com/engineering/multi-agent-research-system"
category: "agents/frameworks"
tags: ["ai", "multi-agent", "research", "anthropic"]
date: "2026-05-26"
quality_score: 4
---

# How we built our multi-agent research system

> 原文：[Anthropic Engineering Blog](https://www.anthropic.com/engineering/multi-agent-research-system) | 抓取时间：2026-05-27

---

## 多 agent 系统的好处

> **EN:** Benefits of a multi-agent system.

Research 工作涉及开放性问题和难以提前预测所需步骤的情况。Research 本质上要求灵活性来 pivot 或探索 tangential connections，因为调查过程中会发现 leads。

搜索的本质是压缩：从大量语料中提炼洞察。Subagents 通过在独立上下文窗口中并行运行，促进压缩——同时探索问题的不同方面，然后为 lead research agent 凝聚最重要的 tokens。

一旦 intelligence 达到阈值，多 agent 系统就成为扩展性能的关键方式。

### 性能数据

> **EN:** Performance data.

我们的内部评估显示：**多 agent 研究系统比单 agent Claude Opus 4 好 90.2%**。

三个因素解释了 [BrowseComp](https://openai.com/index/browsecomp/) 评估中 95% 的性能差异：
1. **Token 使用量**（解释了 80% 的差异）
2. 工具调用次数
3. 模型选择

---

## 研究系统的架构

> **EN:** Architecture overview for Research.

```
User Query → LeadAgent → Subagents (并行)
                     ↓
              Memory (保存计划)
                     ↓
              LeadResearcher (综合结果)
                     ↓
              CitationAgent (处理引用)
                     ↓
              Final Report
```

**关键设计原则：**

1. **LeadResearcher 分析查询，制定策略**
2. **Subagents 并行搜索不同方面**
3. **每个 Subagent 独立执行 Web 搜索，使用 interleaved thinking 评估工具结果**
4. **LeadResearcher 综合结果并决定是否需要更多研究**
5. **足够的论文收集后，退出研究循环并传递给 CitationAgent**

---

## Prompt 工程关键原则

> **EN:** Prompt engineering and evaluations for research agents.

### 1. 像你的 agent 一样思考

> **EN:** Think like your agents.

要迭代 prompts，必须了解其效果。我们使用 Console 模拟 exact prompts and tools，然后观察 agent 逐步工作。

### 2. 教 orchestrator 如何 delegate

> **EN:** Teach the orchestrator how to delegate.

每个 subagent 需要：
- **Objective**（目标）
- **Output format**（输出格式）
- **Guidance on tools and sources**（工具和来源指导）
- **Clear task boundaries**（清晰的任务边界）

### 3. 根据查询复杂度缩放 effort

> **EN:** Scale effort to query complexity.

| 简单事实查找 | 直接比较 | 复杂研究 |
|:---:|:---:|:---:|
| 1 agent, 3-10 次工具调用 | 2-4 subagents, 10-15 次调用/个 | 10+ subagents，明确分工 |

### 4. 工具设计和选择至关重要

> **EN:** Tool design and selection are critical.

Agent-tool 接口和 human-computer 接口一样重要。我们给 agent 明确的启发法：

- 首先检查所有可用工具
- 将工具使用与用户意图匹配
- 使用 Web 搜索进行广泛外部探索
- 优先使用专业工具而非通用工具

### 5. 让 agent 改进自己

> **EN:** Let agents improve themselves.

我们发现 Claude 4 模型可以成为优秀的 prompt engineers。我们创建了一个 tool-testing agent——当给出有缺陷的 MCP 工具时，它尝试使用工具然后重写工具描述以避免失败。

这个过程使任务完成时间 **减少了 40%**。

### 6. 从宽开始，然后缩小

> **EN:** Start wide, then narrow down.

Agent 通常 default to 过于冗长和具体的查询，只返回很少结果。我们通过提示 agent 从短而宽的查询开始，然后评估有什么可用的，再逐步缩小范围。

### 7. 引导思考过程

> **EN:** Guide the thinking process.

Extended thinking mode 可以作为可控的 scratchpad。Lead agent 使用 thinking 来计划其方法，评估哪些工具适合任务，确定查询复杂度和 subagent 数量，并定义每个 subagent 的角色。

### 8. 并行工具调用转变速度和性能

> **EN:** Parallel tool calling transforms speed and performance.

两种并行化：
1. Lead agent 并行生成 3-5 个 subagents（而非串行）
2. Subagents 并行使用 3+ 个工具

这些变化使复杂查询的研究时间 **减少了高达 90%**。

---

## Agent 的有效评估

> **EN:** Effective evaluation of agents.

### 立即开始小样本评估

> **EN:** Start evaluating immediately with small samples.

在早期 agent 开发中，变化往往有巨大影响。一个 prompt 调整可能将成功率从 30% 提高到 80%。效果这么大，只需要几个测试用例就能看出变化。

### LLM-as-judge 评估

> **EN:** LLM-as-judge evaluation scales when done well.

我们使用 LLM judge 评估每个输出：
- **Factual accuracy**（事实准确性）
- **Citation accuracy**（引用准确性）
- **Completeness**（完整性）
- **Source quality**（来源质量）
- **Tool efficiency**（工具效率）

### 人工评估捕捉自动化遗漏的内容

> **EN:** Human evaluation catches what automation misses.

人类测试者发现边缘情况：
- 不寻常查询上的 hallucinated 答案
- 系统失败
- 微妙的来源选择偏差

例如，我们早期 agent 一致选择 SEO 优化的内容农场而非权威但排名较低的来源（如学术 PDF 或个人博客）。

---

*原文包含 architect 图表，详见 [Cookbook patterns](https://platform.claude.com/cookbook/patterns-agents-basic-workflows)*
