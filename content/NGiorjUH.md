# OpenAI Agents SDK

来源: https://github.com/openai/openai-agents-python
文档: https://openai.github.io/openai-agents-python/

## 概述

OpenAI Agents SDK 是一个轻量但强大的多智能体工作流框架，支持 OpenAI Responses API、Chat Completions API 以及 100+ 其他 LLM（通过 OpenAI 兼容接口）。

## 核心概念

### Agents
配置了指令、工具、Guardrails 和 Handoffs 的大语言模型。

### Sandbox Agents
预配置了在容器环境中工作的智能体，适用于需要检查文件、运行命令、应用补丁的长时间任务。

```python
from agents import Runner
from agents.run import RunConfig
from agents.sandbox import Manifest, SandboxAgent, SandboxRunConfig
from agents.sandbox.entries import GitRepo
from agents.sandbox.sandboxes import UnixLocalSandboxClient

agent = SandboxAgent(
    name="Workspace Assistant",
    instructions="Inspect the sandbox workspace before answering.",
    default_manifest=Manifest(
        entries={"repo": GitRepo(repo="openai/openai-agents-python", ref="main")}
    ),
)

result = Runner.run_sync(
    agent,
    "Inspect the repo README and summarize what this project does.",
    run_config=RunConfig(sandbox=SandboxRunConfig(client=UnixLocalSandboxClient())),
)
```

### Agents as Tools / Handoffs
委托给其他 Agent 处理特定任务。

### Tools
支持函数调用、MCP（Model Context Protocol）和 Hosted Tools。

### Guardrails
可配置的输入/输出验证安全检查。

### Human in the Loop
内置的人机交互机制。

### Sessions
跨 Agent 运行的自动对话历史管理。

### Tracing
内置的 Agent 运行追踪，支持查看、调试和优化工作流。

### Realtime Agents
使用 gpt-realtime-1.5 构建语音 Agent，支持完整 Agent 功能。

## 安装

```bash
# 使用 uv（推荐）
uv init
uv add openai-agents

# 或使用 pip
python -m venv .venv && source .venv/bin/activate
pip install openai-agents
```

可选依赖：
- `pip install 'openai-agents[voice]'` - 语音支持
- `pip install 'openai-agents[redis]'` - Redis Session 支持

要求：Python 3.10+

## 核心特性

- **Provider Agnostic**：不绑定 OpenAI，支持 100+ LLM
- **Sandbox Agents**：支持在隔离环境中执行复杂长时任务
- **内置 Tracing**：开箱即用的运行追踪
- **Realtime 支持**：语音 Agent 开发能力
- **Guardrails**：输入/输出安全验证

## 相关项目

- [Agents SDK JS/TS](https://github.com/openai/openai-agents-js)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Pydantic](https://docs.pydantic.dev/latest/)
- [LangChain](https://github.com/langchain-ai/langchain)
