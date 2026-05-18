---
id: 2aef58dd
title: "用 MCP + Claude Code 搭建 AI Agent 工作流实战"
url: https://x.com/petergyang/status/2046961520970777029
source: X (petergyang)
quality_score: 5
tags: ['MCP', 'Claude Code', 'AI Agent', '工作流', '实战']
fetched_at: 2026-05-18T04:47:00Z
---

## 核心观点

**如果说 Claude Code 是一个优秀的打字员和测试员，那么加上 MCP（Model Context Protocol）则是让 Claude 真正拥有了外部感官和手脚——它不再局限于当前项目的代码文件。**

---

## 中文版

### 什么是 MCP

MCP（Model Context Protocol）是 Anthropic 提出的模型上下文协议，让 Claude Code 可以**连接外部工具和数据源**，突破项目代码文件的边界。

**核心能力：**
- 文件系统访问（超出当前目录）
- API 调用（执行 HTTP 请求）
- 数据库查询
- 代码库分析和搜索
- 自动化工作流执行

### 典型架构

```
用户需求 → Claude Code（大脑） → MCP Server（连接外部工具）
                                    ├── 文件系统 MCP
                                    ├── GitHub MCP
                                    └── 数据库 MCP
```

### 实战步骤

#### 第一步：安装 MCP SDK

```bash
npm install @modelcontextprotocol/sdk
```

#### 第二步：创建 MCP Server

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("my-agent")

@mcp.tool()
def search_codebase(query):
    return search_results(query)
```

#### 第三步：在 Claude Code 中连接

在 Claude Code 的 MCP 配置中添加 server：

```json
{
  "mcpServers": {
    "my-agent": {
      "command": "python",
      "args": ["mcp_server.py"]
    }
  }
}
```

#### 第四步：设计 DAG 记忆管理系统

对于复杂的 Agent 工作流，推荐使用 DAG-based 记忆管理：
- **节点**：每个任务步骤的结果
- **边**：步骤之间的依赖关系
- **好处**：避免重复执行，支持任务恢复，历史可追溯

### MCP 的最佳实践

1. **工具要原子化**：每个 MCP 工具只做一件事
2. **错误处理要健壮**：外部 API 可能失败，需要优雅降级
3. **安全第一**：需要严格的权限控制
4. **日志要详细**：Agent 的决策路径需要完整记录

### 应用场景

- **代码审查自动化**：MCP 连接 GitHub，自动 review PR
- **数据分析 Agent**：MCP 连接数据库，用自然语言查询
- **跨项目工作流**：MCP 连接多个代码仓库

---

## English Version

### What is MCP

MCP (Model Context Protocol) enables Claude Code to connect to external tools and data sources, breaking free from project code file boundaries.

**Core Capabilities:**
- Filesystem access (beyond current directory)
- API calls (execute HTTP requests)
- Database queries
- Codebase analysis and search
- Automated workflow execution

### Architecture

```
User Request → Claude Code (Brain) → MCP Server (External Tools)
                                    ├── Filesystem MCP
                                    ├── GitHub MCP
                                    └── Database MCP
```

### Practical Steps

1. Install MCP SDK: `npm install @modelcontextprotocol/sdk`
2. Create MCP Server with `@mcp.tool()` decorators
3. Connect in Claude Code via JSON config
4. Design DAG-based memory management for complex workflows

### Best Practices

1. Keep tools atomic
2. Robust error handling with graceful degradation
3. Security-first with strict permissions
4. Detailed logging for debugging

### Use Cases

- Automated code review (GitHub MCP)
- Data analysis agents (Database MCP)
- Cross-project workflows (multiple repos)