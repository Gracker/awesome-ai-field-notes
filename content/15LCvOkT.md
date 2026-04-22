# OWL: Optimized Workforce Learning for General Multi-Agent Assistance

来源: https://github.com/camel-ai/owl/blob/main/README_zh.md

## 概述

OWL（Optimized Workforce Learning）是 CAMEL-AI 推出的前沿多智能体协作框架，旨在通过动态智能体交互实现跨多领域的任务自动化。该项目在 GAIA 基准测试中取得 58.18 平均分，在开源框架中排名第一。

## 核心功能

- **多搜索引擎支持**：维基百科、Google、DuckDuckGo、百度、博查等实时信息检索
- **多模态处理**：支持视频、图片、语音处理
- **浏览器操作**：基于 Playwright 的页面滚动、点击、输入、下载、历史回退
- **文件解析**：Word、Excel、PDF、PowerPoint 内容提取
- **代码执行**：Python 代码编写与解释器运行
- **丰富工具包**：涵盖 ArxivToolkit、AudioAnalysisToolkit、CodeExecutionToolkit、DalleToolkit、ExcelToolkit、GitHubToolkit、GoogleMapsToolkit、ImageAnalysisToolkit、MathToolkit、NetworkXToolkit、NotionToolkit、OpenAPIToolkit、SearchToolkit、VideoAnalysisToolkit、WeatherToolkit、BrowserToolkit 等
- **MCP 集成**：标准化 AI 与工具/数据源的交互协议
- **网页界面**：基于 Gradio 的本地交互界面

## 架构特点

OWL 基于 CAMEL-AI Framework 构建，采用 Society of Agents 模式，通过多智能体分工协作完成复杂任务。支持多种 LLM 后端（OpenAI GPT-4+、Claude、Qwen、DeepSeek、Gemini 等），但文档明确指出其他模型在复杂任务上可能表现明显较差。

## 安装与使用

```bash
git clone https://github.com/camel-ai/owl.git
cd owl
pip install uv && uv venv .venv --python=3.10
source .venv/bin/activate
uv pip install -e .
python examples/run.py
```

支持 Docker 部署，提供 docker-compose 一键启动。

## 技术亮点

- GAIA 基准测试开源框架第一（58.18 分）
- MCP（Model Context Protocol）工具包集成
- 完整的多智能体交互与通信协议
- 支持 Sandbox 环境隔离执行

## 许可证

Apache 2.0
