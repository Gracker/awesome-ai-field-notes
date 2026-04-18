# DeerFlow - Deep Exploration and Efficient Research Flow

DeerFlow 是一个开源的超级 Agent 框架，通过编排子 Agent、记忆和沙箱来处理各种任务——由可扩展的技能驱动。

2026年2月28日，DeerFlow 2.0 在 GitHub Trending 排名第一。

## 核心定位

DeerFlow (Deep Exploration and Efficient Research Flow) is an open-source super agent harness that orchestrates sub-agents, memory, and sandboxes to do almost anything — powered by extensible skills.

版本 2.0 是完全重写，与 v1 版本无任何共享代码。

## 核心特性

- **多模型支持**：强烈推荐使用 Doubao-Seed-2.0-Code、DeepSeek v3.2 和 Kimi 2.5
- **InfoQuest 集成**：字节跳动自研的智能搜索和爬虫工具集
- **沙箱模式**：安全隔离的执行环境
- **MCP Server 支持**：Model Context Protocol 服务器
- **LangSmith/Langfuse 追踪**：完整的执行追踪能力
- **子 Agent 编排**：灵活的多 Agent 协作架构
- **长期记忆**：持久化记忆系统

## 部署配置

### 硬件需求

| 部署场景 | 最低配置 | 推荐配置 | 说明 |
|----------|----------|----------|------|
| 本地评估 / make dev | 4 vCPU, 8GB RAM, 20GB SSD | 8 vCPU, 16GB RAM | 适合一到两个开发者使用轻量会话 |
| Docker 开发 / make docker-start | 4 vCPU, 8GB RAM, 25GB SSD | 8 vCPU, 16GB RAM | 镜像构建和绑定挂载需要更多资源 |
| 长期运行服务器 / make up | 8 vCPU, 16GB RAM, 40GB SSD | 16 vCPU, 32GB RAM | 共享使用、多 Agent 运行或重沙箱工作负载 |

### 快速启动

```bash
# 克隆仓库
git clone https://github.com/bytedance/deer-flow.git
cd deer-flow

# 运行设置向导
make setup

# 运行诊断检查
make doctor
```

### Docker 部署（推荐）

```bash
# 仅首次运行或镜像更新时
make docker-init

# 启动服务
make docker-start

# 停止服务
make docker-stop
```

### 本地开发

```bash
# 检查前置条件
make check

# 安装依赖
make install

# 启动开发服务
make dev
```

## 启动模式

DeerFlow 支持多种启动模式：

- **Dev / Prod**：dev 启用热重载；prod 使用预构建前端
- **Standard / Gateway**：Standard 模式使用独立的 LangGraph 服务器；Gateway 模式（实验性）将 Agent 运行时嵌入 Gateway API

| 模式 | 本地开发 | Docker Dev | Docker Prod |
|------|----------|------------|-------------|
| Dev | `make dev` | `make docker-start` | — |
| Dev + Gateway | `make dev-pro` | `make docker-start-pro` | — |
| Prod | `make start` | — | `make up` |
| Prod + Gateway | `make start-pro` | — | `make up-pro` |

## 技能系统（Skills）

DeerFlow 内置可扩展的技能系统，包括：

- **搜索技能**：集成 InfoQuest 智能搜索
- **沙箱技能**：安全的代码执行环境
- **记忆技能**：短期/长期记忆管理
- **文件系统技能**：动态上下文发现和计划持久化
- **工具设计**：MCP 工具构建

## 安全建议

⚠️ 不当部署可能引入安全风险。请确保：
- 使用沙箱模式隔离不可信代码
- 限制 bash 访问权限
- 配置适当的文件写入限制
- 定期更新到最新版本

## 相关链接

- 官网：https://deerflow.tech
- GitHub：https://github.com/bytedance/deer-flow
- 趋势追踪：https://trendshift.io/repositories/14699

---

来源：[bytedance/deer-flow](https://github.com/bytedance/deer-flow)
