## English
# Launching Claude Managed Agents

Anthropic 发布 Claude Managed Agents：预构建的可配置 Agent 运行底座，运行在托管基础设施上。三大核心概念：Agent（版本化配置）、Environment（沙盒模板）、Session（有状态运行）。四种用法：事件触发、定时、即发即忘、长时间任务。架构上将"大脑"（Claude+调度框架）、"手"（沙盒工具）、"记忆"（会话日志）解耦，支持独立故障恢复。

## 核心概念

- **Agent**：版本化配置
- **Environment**：沙盒模板
- **Session**：有状态运行

## 使用模式

1. **事件触发**：响应外部事件
2. **定时**：按时间计划执行
3. **即发即忘**：快速任务执行
4. **长时间任务**：持续运行的任务

## 架构特点

将大脑、手、记忆三层解耦，支持独立故障恢复。

## 典型案例

Notion、Sentry、Atlassian、Rakuten 等已接入使用。


## 中文
（翻译待补）
