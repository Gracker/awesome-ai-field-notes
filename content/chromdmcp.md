# Chrome DevTools MCP：专为 AI 编程 Agent 打造的 Chrome 开发者工具集成

> 源文：Chrome DevTools for coding agents  
> 来源：GitHub - ChromeDevTools/chrome-devtools-mcp  
> 原文语言：英文

## 简介

Chrome DevTools for Agents（chrome-devtools-mcp）让你的编程 Agent（如 Gemini、Claude、Cursor 或 Copilot）能够控制并检查实时 Chrome 浏览器。它作为 Model Context Protocol（MCP）服务器使用，向 AI 编程助手开放 Chrome DevTools 的全部能力，实现可靠的自动化、深度调试和性能分析。

## 核心能力

- **性能洞察**：使用 Chrome DevTools 录制跟踪记录，提取可操作的性能洞察
- **高级浏览器调试**：分析网络请求、截取屏幕截图、检查浏览器控制台消息（带 Source Map 的堆栈跟踪）
- **可靠自动化**：使用 Puppeteer 自动化 Chrome 操作，并自动等待操作结果

chrome-devtools-mcp 将浏览器实例的内容暴露给 MCP 客户端，使其能够检查、调试和修改浏览器或 DevTools 中的任何数据。

## 环境要求

- Node.js v20.19 或更高版本
- Chrome 当前稳定版或更新版本
- npm

## 快速配置

将以下配置添加到你的 MCP 客户端：

```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": ["-y", "chrome-devtools-mcp@latest"]
    }
  }
}
```

## Slim 模式

如果只需要基本的浏览器任务，可以使用 `--slim` 模式：

```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": ["-y", "chrome-devtools-mcp@latest", "--slim", "--headless"]
    }
  }
}
```

## 支持的 IDE/Agent 平台

chrome-devtools-mcp 已支持众多主流 AI 编程工具：

| 平台 | 安装方式 |
|------|----------|
| Claude Code | `claude mcp add chrome-devtools --scope user npx chrome-devtools-mcp@latest` |
| Gemini CLI | `gemini mcp add chrome-devtools npx chrome-devtools-mcp@latest` |
| Cursor | 按钮安装或手动配置 |
| Windsurf | MCP 配置指南 |
| Copilot/VS Code | 插件安装或 MCP 服务器安装 |
| Codex | `codex mcp add chrome-devtools -- npx chrome-devtools-mcp@latest` |
| Cline | 按文档配置 |
| Factory CLI | `droid mcp add chrome-devtools "npx -y chrome-devtools-mcp@latest"` |
| JetBrains AI Assistant / Junie | MCP 配置界面添加 |
| Kiro | MCP 配置 |
| Katalon Studio | 通过 MCP 代理连接 |
| Warp | AI MCP 服务器设置中添加 |

## 隐私与数据收集

- 性能工具可能将跟踪 URL 发送到 Google CrUX API 以获取真实用户体验数据
- Google 默认收集使用统计（如工具调用成功率、延迟和环境信息）
- 可通过 `--no-usage-statistics` 标志禁用
- 也可通过设置 `CHROME_DEVTOOLS_MCP_NO_USAGE_STATISTICS` 或 `CI` 环境变量禁用
- 默认会定期检查 npm 注册表更新，可通过 `CHROME_DEVTOOLS_MCP_NO_UPDATE_CHECKS` 禁用

## 输入自动化工具（10 个工具）

- click
- drag
- 以及其他浏览器自动化操作

## 验证安装

在 MCP 客户端中输入以下提示来检查是否正常工作：

```
Check the performance of https://developers.chrome.com
```

MCP 服务器应该在浏览器实例运行时自动启动浏览器。

## 官方支持声明

chrome-devtools-mcp 正式支持 Google Chrome 和 Chrome for Testing。其他基于 Chromium 的浏览器可能可用，但不保证。

---

**注意**：Chrome DevTools MCP 将浏览器内容暴露给 MCP 客户端。请勿分享敏感或个人信息。
