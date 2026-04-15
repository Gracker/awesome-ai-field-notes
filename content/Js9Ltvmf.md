# gstack: Use Garry Tan's exact Claude Code setup

## English

gstack is an open-source toolkit designed to enhance the capabilities of Claude Code, transforming it into a "virtual engineering team" with specialized roles and workflows. Created by Garry Tan, CEO of Y Combinator, this setup is intended to streamline and standardize AI-assisted software development processes.

### The Tools

gstack features 23 opinionated tools, referred to as "specialist skills" or "slash commands", covering various aspects of the software development lifecycle. Some sources also refer to "28 slash commands" or "8 power tools" within the gstack framework.

The tools serve distinct roles within a development team:

- **CEO**: Product strategy & vision
- **Designer**: Catching AI design inconsistencies
- **Engineering Manager**: Locking architecture, mapping data flow, surfacing edge cases
- **Release Manager**: Shipping code
- **Doc Engineer**: Documenting releases
- **QA Lead**: Real browser testing, finding bugs, generating regression tests
- **Security Officer**: Running OWASP + STRIDE audits

### Key Slash Commands

- `/office-hours`: Acts as a discovery consultant to refine product ideas
- `/plan-ceo-review`: Challenges product scope and provides strategic feedback
- `/plan-eng-review`: Focuses on architectural review and technical approaches
- `/review`: Provides staff engineer-level code reviews
- `/qa`: Launches a Playwright-based Chromium browser to perform real browser testing on staging URLs, identify bugs, and generate regression tests
- `/cso`: Conducts security audits, including OWASP Top 10 and STRIDE threat modeling
- `/ship`: Manages the process of deploying code

### Installation & Compatibility

Installation involves cloning the GitHub repository and running a setup script within Claude Code. The toolkit is MIT licensed and is designed to run within Claude Code, but is also compatible with other AI coding agents like OpenAI Codex CLI, Cursor, and OpenClaw.

Garry Tan claims this setup has significantly increased his coding output, allowing him to ship a substantial amount of code while managing Y Combinator.

**GitHub**: https://github.com/garrytan/gstack

---

## 中文

gstack 是一个开源工具包，旨在增强 Claude Code 的能力，将其转变为具备专业角色和工作流程的"虚拟工程团队"。该工具由 Y Combinator CEO Garry Tan 创建，旨在简化和标准化 AI 辅助软件开发流程。

### 工具集

gstack 包含 23 个"专家技能"工具，也称为斜杠命令，覆盖软件开发生命周期的各个方面。部分资料也提到 gstack 框架内有"28 个斜杠命令"或"8 个强力工具"。

这些工具对应开发团队中的不同角色：

- **CEO**：产品战略与愿景
- **Designer**：捕捉 AI 设计不一致之处
- **Engineering Manager**：锁定架构、映射数据流、暴露边缘用例
- **Release Manager**：发布代码
- **Doc Engineer**：记录发布文档
- **QA Lead**：真实浏览器测试、发现 bug、生成回归测试
- **Security Officer**：运行 OWASP + STRIDE 安全审计

### 核心斜杠命令

- `/office-hours`：充当发现顾问，完善产品想法
- `/plan-ceo-review`：挑战产品范围，提供战略反馈
- `/plan-eng-review`：专注架构审查和技术方案
- `/review`：提供高级工程师级别的代码审查
- `/qa`：启动基于 Playwright 的 Chromium 浏览器，在预发环境进行真实浏览器测试、识别 bug 并生成回归测试
- `/cso`：执行安全审计，包括 OWASP Top 10 和 STRIDE 威胁建模
- `/ship`：管理代码部署流程

### 安装与兼容性

安装方式为克隆 GitHub 仓库并在 Claude Code 中运行设置脚本。该工具包采用 MIT 许可证，除 Claude Code 外还兼容 OpenAI Codex CLI、Cursor 和 OpenClaw 等其他 AI 编码 Agent。

Garry Tan 声称，这套配置显著提升了他的编码产出，在管理 Y Combinator 的同时仍能发布大量代码。

**GitHub**: https://github.com/garrytan/gstack
