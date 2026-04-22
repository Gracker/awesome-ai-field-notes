# langchain-ai/agents-from-scratch: Build an email assistant with human-in-the-loop and memory

来源: https://github.com/langchain-ai/agents-from-scratch
官方文档: https://github.com/langchain-ai/agents-from-scratch

## 概述

该仓库是一个"从零构建 Agent"的实战指南，以构建一个 Gmail 接入的"环境感知"（ambient）邮件助手为最终目标。分为 4 个章节，每章配有 Jupyter Notebook 和对应的 `src/email_assistant` 目录代码。从 Agent 基础开始，逐步递进到 Agent 评估、人在回路（Human-in-the-Loop），最终到记忆系统，最终组合成一个可部署的 Agent。

## 四个章节

### Section 1: Agent 基础
- Notebook: `notebooks/agent.ipynb`
- Code: `src/email_assistant/email_assistant.py`
- 内容：构建邮件助手，结合邮件分类步骤与处理邮件的 Agent，可看到 LangGraph 的完整实现。

### Section 2: Agent 评估
- Notebook: `notebooks/evaluation.ipynb`
- 内容：使用 pytest 和 LangSmith Evaluate API 运行评估，包括 LLM-as-a-judge、工具调用评估和分类决策评估。

### Section 3: Human-in-the-Loop
- Notebook: `notebooks/hitl.ipynb`
- Code: `src/email_assistant/email_assistant_hitl.py`
- 内容：添加人在回路，允许用户审查特定工具调用（如发送邮件、安排会议）。使用 [Agent Inbox](https://github.com/langchain-ai/agent-inbox) 作为人机交互界面。

### Section 4: Memory
- Notebook: `notebooks/memory.ipynb`
- Code: `src/email_assistant/email_assistant_hitl_memory.py`
- 内容：添加记忆功能，使用 [LangGraph Store](https://langchain-ai.github.io/langgraph/concepts/memory/#long-term-memory) 持久化记忆，使 Agent 能够从用户反馈中学习并适应偏好。

## 环境要求

- Python 3.11+
- OpenAI API Key
- LangSmith API Key（用于追踪和评估）

## 安装（推荐 uv）

```bash
uv sync --extra dev
source .venv/bin/activate
```

## 测试

```bash
# 运行所有测试
python tests/run_all_tests.py

# 运行所有 notebook 测试
python tests/test_notebooks.py
pytest tests/test_notebooks.py -v
```

## LangMem 集成

添加 [LangMem](https://langchain-ai.github.io/langmem/) 管理记忆：
- 管理背景记忆集合
- 添加可查找事实的记忆工具

## 核心价值

1. **完整可运行的 Agent 实战项目**：从基础到生产级 Agent 的完整路径
2. **LangGraph 最佳实践**：展示了 LangGraph 中 agent、evaluation、HITL、memory 的标准用法
3. **评估驱动开发**：内置测试框架和 LangSmith 追踪
4. **可扩展**：Email Assistant 的原则可应用于其他领域的 Agent
