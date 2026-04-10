---
title: 'DeerFlow 2.0: ByteDance 开源超级 Agent 运行底座'
sidebar: false
---

::: info
[← 返回智能体](/agents)
:::

# DeerFlow 2.0: ByteDance 开源超级 Agent 运行底座

> 字节跳动的超级 Agent 底座，LangGraph 重写，支持子 Agent 并行编排

🔗 [原文链接](https://github.com/bytedance/deer-flow) | @Bytedance | 🌐 | ⭐⭐⭐⭐ 4 ⭐4 4/5 📅 2026-04-10

`deer-flow` `bytedance` `langgraph` `langchain` `super-agent` `sub-agent`

---

English | [中文](/bytedance/deer-flow/blob/main/README_zh.md) | [日本語](/bytedance/deer-flow/blob/main/README_ja.md) | [Français](/bytedance/deer-flow/blob/main/README_fr.md) | [Русский](/bytedance/deer-flow/blob/main/README_ru.md)

/bytedance/deer-flow/blob/main/backend/pyproject.toml
/bytedance/deer-flow/blob/main/Makefile
/bytedance/deer-flow/blob/main/LICENSE

https://trendshift.io/repositories/14699

On February 28th, 2026, DeerFlow claimed the 🏆 #1 spot on GitHub Trending following the launch of version 2. Thanks a million to our incredible community — you made this happen! 💪🔥

DeerFlow (Deep Exploration and Efficient Research Flow) is an open-source super agent harness that orchestrates sub-agents, memory, and sandboxes to do almost anything — powered by extensible skills.

 deer-flow-720p.mp4

Note
DeerFlow 2.0 is a ground-up rewrite. It shares no code with v1. If you're looking for the original Deep Research framework, it's maintained on the [1.x branch](https://github.com/bytedance/deer-flow/tree/main-1.x) — contributions there are still welcome. Active development has moved to 2.0.

https://deerflow.tech

Learn more and see real demos on our [official website](https://deerflow.tech).

https://private-user-images.githubusercontent.com/1003147/564581194-2ecc7b9d-50be-4185-b1f7-5542d222fb2d.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzU4MzQ3ODgsIm5iZiI6MTc3NTgzNDQ4OCwicGF0aCI6Ii8xMDAzMTQ3LzU2NDU4MTE5NC0yZWNjN2I5ZC01MGJlLTQxODUtYjFmNy01NTQyZDIyMmZiMmQucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDQxMCUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjA0MTBUMTUyMTI4WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9N2UwYTQxN2IwMzA3MWFmODk5MzA5ODkwYTQ2ODc3N2FiYzdlOWRhNzljZmZkNzc2NWQwNzcyMTUwYjQ0NTE1ZiZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.yzLFH173RGr8bTSpIBRURnZGu0QKg8InYK0Jek7v1hs

- We strongly recommend using Doubao-Seed-2.0-Code, DeepSeek v3.2 and Kimi 2.5 to run DeerFlow

- [Learn more](https://www.byteplus.com/en/activity/codingplan?utm_campaign=deer_flow&utm_content=deer_flow&utm_medium=devrel&utm_source=OWO&utm_term=deer_flow)

- [中国大陆地区的开发者请点击这里](https://www.volcengine.com/activity/codingplan?utm_campaign=deer_flow&utm_content=deer_flow&utm_medium=devrel&utm_source=OWO&utm_term=deer_flow)

DeerFlow has newly integrated the intelligent search and crawling toolset independently developed by BytePlus--[InfoQuest (supports free online experience)](https://docs.byteplus.com/en/docs/InfoQuest/What_is_Info_Quest)

https://docs.byteplus.com/en/docs/InfoQuest/What_is_Info_Quest

- [🦌 DeerFlow - 2.0](#-deerflow---20)

[Official Website](#official-website)

- [Coding Plan from ByteDance Volcengine](#coding-plan-from-bytedance-volcengine)

- [InfoQuest](#infoquest)

- [Table of Contents](#table-of-contents)

- [One-Line Agent Setup](#one-line-agent-setup)

- [Quick Start](#quick-start)

[Configuration](#configuration)

- [Running the Application](#running-the-application)

[Deployment Sizing](#deployment-sizing)

- [Option 1: Docker (Recommended)](#option-1-docker-recommended)

- [Option 2: Local Development](#option-2-local-development)

- [Advanced](#advanced)

[Sandbox Mode](#sandbox-mode)

- [MCP Server](#mcp-server)

- [IM Channels](#im-channels)

- [LangSmith Tracing](#langsmith-tracing)

- [Langfuse Tracing](#langfuse-tracing)

- [Using Both Providers](#using-both-providers)

- [From Deep Research to Super Agent Harness](#from-deep-research-to-super-agent-harness)

- [Core Features](#core-features)

[Skills & Tools](#skills--tools)

[Claude Code Integration](#claude-code-integration)

- [Sub-Agents](#sub-agents)

- [Sandbox & File System](#sandbox--file-system)

- [Context Engineering](#context-engineering)

- [Long-Term Memory](#long-term-memory)

- [Recommended Models](#recommended-models)

- [Embedded Python Client](#embedded-python-client)

- [Documentation](#documentation)

- [⚠️ Security Notice](#%EF%B8%8F-security-notice)

[Improper Deployment May Introduce Security Risks](#improper-deployment-may-introduce-security-risks)

- [Security Recommendations](#security-recommendations)

- [Contributing](#contributing)

- [License](#license)

- [Acknowledgments](#acknowledgments)

[Key Contributors](#key-contributors)

- [Star History](#star-history)

If you use Claude Code, Codex, Cursor, Windsurf, or another coding agent, you can hand it the setup instructions in one sentence:

Help me clone DeerFlow if needed, then bootstrap it for local development by following https://raw.githubusercontent.com/bytedance/deer-flow/main/Install.md

That prompt is intended for coding agents. It tells the agent to clone the repo if needed, choose Docker when available, and stop with the exact next command plus any missing config the user still needs to provide.

- Clone the DeerFlow repository
git clone https://github.com/bytedance/deer-flow.git
cd deer-flow

- Run the setup wizard
From the project root directory (deer-flow/), run:
make setup
This launches an interactive wizard that guides you through choosing an LLM provider, optional web search, and execution/safety preferences such as sandbox mode, bash access, and file-write tools. It generates a minimal config.yaml and writes your keys to .env. Takes about 2 minutes.
The wizard also lets you configure an optional web search provider, or skip it for now.
Run make doctor at any time to verify your setup and get actionable fix hints.
Advanced / manual configuration: If you prefer to edit config.yaml directly, run make config instead to copy the full template. See config.example.yaml for the complete reference including CLI-backed providers (Codex CLI, Claude Code OAuth), OpenRouter, Responses API, and more.

Manual model configuration examples
models:
 - name: gpt-4o
 display_name: GPT-4o
 use: langchain_openai:ChatOpenAI
 model: gpt-4o
 api_key: $OPENAI_API_KEY

 - name: openrouter-gemini-2.5-flash
 display_name: Gemini 2.5 Flash (OpenRouter)
 use: langchain_openai:ChatOpenAI
 model: google/gemini-2.5-flash-preview
 api_key: $OPENROUTER_API_KEY
 base_url: https://openrouter.ai/api/v1

 - name: gpt-5-responses
 display_name: GPT-5 (Responses API)
 use: langchain_openai:ChatOpenAI
 model: gpt-5
 api_key: $OPENAI_API_KEY
 use_responses_api: true
 output_version: responses/v1

 - name: qwen3-32b-vllm
 display_name: Qwen3 32B (vLLM)
 use: deerflow.models.vllm_provider:VllmChatModel
 model: Qwen/Qwen3-32B
 api_key: $VLLM_API_KEY
 base_url: http://localhost:8000/v1
 supports_thinking: true
 when_thinking_enabled:
 extra_body:
 chat_template_kwargs:
 enable_thinking: true
OpenRouter and similar OpenAI-compatible gateways should be configured with langchain_openai:ChatOpenAI plus base_url. If you prefer a provider-specific environment variable name, point api_key at that variable explicitly (for example api_key: $OPENROUTER_API_KEY).
To route OpenAI models through /v1/responses, keep using langchain_openai:ChatOpenAI and set use_responses_api: true with output_version: responses/v1.
For vLLM 0.19.0, use deerflow.models.vllm_provider:VllmChatModel. For Qwen-style reasoning models, DeerFlow toggles reasoning with extra_body.chat_template_kwargs.enable_thinking and preserves vLLM's non-standard reasoning field across multi-turn tool-call conversations. Legacy thinking configs are normalized automatically for backward compatibility. Reasoning models may also require the server to be started with --reasoning-parser .... If your local vLLM deployment accepts any non-empty API key, you can still set VLLM_API_KEY to a placeholder value.
CLI-backed provider examples:
models:
 - name: gpt-5.4
 display_name: GPT-5.4 (Codex CLI)
 use: deerflow.models.openai_codex_provider:CodexChatModel
 model: gpt-5.4
 supports_thinking: true
 supports_reasoning_effort: true

 - name: claude-sonnet-4.6
 display_name: Claude Sonnet 4.6 (Claude Code OAuth)
 use: deerflow.models.claude_provider:ClaudeChatModel
 model: claude-sonnet-4-6
 max_tokens: 4096
 supports_thinking: true

Codex CLI reads ~/.codex/auth.json

- Claude Code accepts CLAUDE_CODE_OAUTH_TOKEN, ANTHROPIC_AUTH_TOKEN, CLAUDE_CODE_CREDENTIALS_PATH, or ~/.claude/.credentials.json

- ACP agent entries are separate from model providers — if you configure acp_agents.codex, point it at a Codex ACP adapter such as npx -y @zed-industries/codex-acp

- On macOS, export Claude Code auth explicitly if needed:

eval "$(python3 scripts/export_claude_code_oauth.py --print-export)"

API keys can also be set manually in .env (recommended) or exported in your shell:

OPENAI_API_KEY=your-openai-api-key
TAVILY_API_KEY=your-tavily-api-key

Use the table below as a practical starting point when choosing how to run DeerFlow:

Deployment target
Starting point
Recommended
Notes

Local evaluation / make dev
4 vCPU, 8 GB RAM, 20 GB free SSD
8 vCPU, 16 GB RAM
Good for one developer or one light session with hosted model APIs. 2 vCPU / 4 GB is usually not enough.

Docker development / make docker-start
4 vCPU, 8 GB RAM, 25 GB free SSD
8 vCPU, 16 GB RAM
Image builds, bind mounts, and sandbox containers need more headroom than pure local dev.

Long-running server / make up
8 vCPU, 16 GB RAM, 40 GB free SSD
16 vCPU, 32 GB RAM
Preferred for shared use, multi-agent runs, report generation, or heavier sandbox workloads.

- These numbers cover DeerFlow itself. If you also host a local LLM, size that service separately.

- Linux plus Docker is the recommended deployment target for a persistent server. macOS and Windows are best treated as development or evaluation environments.

- If CPU or memory usage stays pinned, reduce concurrent runs first, then move to the next sizing tier.

Development (hot-reload, source mounts):

make docker-init # Pull sandbox image (only once or when image updates)
make docker-start # Start services (auto-detects sandbox mode from config.yaml)

make docker-start starts provisioner only when config.yaml uses provisioner mode (sandbox.use: deerflow.community.aio_sandbox:AioSandboxProvider with provisioner_url).

Docker builds use the upstream uv registry by default. If you need faster mirrors in restricted networks, export UV_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple and NPM_REGISTRY=https://registry.npmmirror.com before running make docker-init or make docker-start.

Backend processes automatically pick up config.yaml changes on the next config access, so model metadata updates do not require a manual restart during development.

Tip
On Linux, if Docker-based commands fail with permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock, add your user to the docker group and re-login before retrying. See [CONTRIBUTING.md](/bytedance/deer-flow/blob/main/CONTRIBUTING.md#linux-docker-daemon-permission-denied) for the full fix.

Production (builds images locally, mounts runtime config and data):

make up # Build images and start all production services
make down # Stop and remove containers

Note
The LangGraph agent server currently runs via langgraph dev (the open-source CLI server).

Access: [http://localhost:2026](http://localhost:2026)

See [CONTRIBUTING.md](/bytedance/deer-flow/blob/main/CONTRIBUTING.md) for detailed Docker development guide.

If you prefer running services locally:

Prerequisite: complete the "Configuration" steps above first (make setup). make dev requires a valid config.yaml in the project root (can be overridden via DEER_FLOW_CONFIG_PATH). Run make doctor to verify your setup before starting.
On Windows, run the local development flow from Git Bash. Native cmd.exe and PowerShell shells are not supported for the bash-based service scripts, and WSL is not guaranteed because some scripts rely on Git for Windows utilities such as cygpath.

- Check prerequisites:
make check # Verifies Node.js 22+, pnpm, uv, nginx

- Install dependencies:
make install # Install backend + frontend dependencies

- (Optional) Pre-pull sandbox image:
# Recommended if using Docker/Container-based sandbox
make setup-sandbox

- (Optional) Load sample memory data for local review:
python scripts/load_memory_sample.py
This copies the sample fixture into the default local runtime memory file so reviewers can immediately test Settings > Memory.
See [backend/docs/MEMORY_SETTINGS_REVIEW.md](/bytedance/deer-flow/blob/main/backend/docs/MEMORY_SETTINGS_REVIEW.md) for the shortest review flow.

- Start services:
make dev

- Access: [http://localhost:2026](http://localhost:2026)

DeerFlow supports multiple startup modes across two dimensions:

- Dev / Prod — dev enables hot-reload; prod uses pre-built frontend

- Standard / Gateway — standard uses a separate LangGraph server (4 processes); Gateway mode (experimental) embeds the agent runtime in the Gateway API (3 processes)

Local Foreground
Local Daemon
Docker Dev
Docker Prod

Dev
./scripts/serve.sh --dev
make dev
./scripts/serve.sh --dev --daemon
make dev-daemon
./scripts/docker.sh start
make docker-start
—

Dev + Gateway
./scripts/serve.sh --dev --gateway
make dev-pro
./scripts/serve.sh --dev --gateway --daemon
make dev-daemon-pro
./scripts/docker.sh start --gateway
make docker-start-pro
—

Prod
./scripts/serve.sh --prod
make start
./scripts/serve.sh --prod --daemon
make start-daemon
—
./scripts/deploy.sh
make up

Prod + Gateway
./scripts/serve.sh --prod --gateway
make start-pro
./scripts/serve.sh --prod --gateway --daemon
make start-daemon-pro
—
./scripts/deploy.sh --gateway
make up-pro

Action
Local
Docker Dev
Docker Prod

Stop
./scripts/serve.sh --stop
make stop
./scripts/docker.sh stop
make docker-stop
./scripts/deploy.sh down
make down

Restart
./scripts/serve.sh --restart [flags]
./scripts/docker.sh restart
—

Gateway mode eliminates the LangGraph server process — the Gateway API handles agent execution directly via async tasks, managing its own concurrency.

In standard mode, DeerFlow runs a dedicated [LangGraph Platform](https://langchain-ai.github.io/langgraph/) server alongside the Gateway API. This architecture works well but has trade-offs:

Standard Mode
Gateway Mode

Architecture
Gateway (REST API) + LangGraph (agent runtime)
Gateway (REST API) + async agent execution
Gateway mode eliminates the LangGraph server process — the Gateway API handles agent execution directly via async tasks, managing its own concurrency.

In standard mode, DeerFlow runs a dedicated [LangGraph Platform](https://langchain-ai.github.io/langgraph/) server alongside the Gateway API. This architecture works well but has trade-offs:

Standard Mode
Gateway Mode

Architecture
Gateway (REST API) + LangGraph (agent runtime)
Gateway (REST API) + async agent execution
