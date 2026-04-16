## English

This project implements a Model Context Protocol (MCP) integration between AI agent (Cursor, Claude Code) and Figma, allowing AI agent to communicate with Figma for reading designs and modifying them programmatically.

## 中文

这个项目实现了AI代理（Cursor、Claude Code）和Figma之间的模型上下文协议（MCP）集成，允许AI代理与Figma通信以读取设计并编程修改它们。

## English

Project Structure:
- src/talk_to_figma_mcp/ - TypeScript MCP server for Figma integration
- src/cursor_mcp_plugin/ - Figma plugin for communicating with Cursor
- src/socket.ts - WebSocket server that facilitates communication between the MCP server and Figma plugin

## 中文

项目结构：
- src/talk_to_figma_mcp/ - 用于Figma集成的TypeScript MCP服务器
- src/cursor_mcp_plugin/ - 用于与Cursor通信的Figma插件
- src/socket.ts - 促进MCP服务器和Figma插件之间通信的WebSocket服务器

## English

Installation Steps:
1. Install Bun if you haven't already:
   ```bash
   curl -fsSL https://bun.sh/install | bash
   ```
2. Run setup, this will also install MCP in your Cursor's active project:
   ```bash
   bun setup
   ```
3. Start the Websocket server:
   ```bash
   bun socket
   ```
4. Install Figma plugin from [Figma community page](https://www.figma.com/community/plugin/1485687494525374295/cursor-talk-to-figma-mcp-plugin)

## 中文

安装步骤：
1. 如果尚未安装Bun：
   ```bash
   curl -fsSL https://bun.sh/install | bash
   ```
2. 运行设置，这也会在您的Cursor活动项目中安装MCP：
   ```bash
   bun setup
   ```
3. 启动WebSocket服务器：
   ```bash
   bun socket
   ```
4. 从[Figma社区页面](https://www.figma.com/community/plugin/1485687494525374295/cursor-talk-to-figma-mcp-plugin)安装Figma插件

## English

Key Features:
- Complete MCP server implementation with 30+ tools
- Bidirectional communication between AI agents and Figma
- Support for design reading, modification, and annotation
- Bulk text replacement functionality
- Component instance override propagation
- Export capabilities for various formats

## 中文

主要功能：
- 包含30多种工具的完整MCP服务器实现
- AI代理和Figma之间的双向通信
- 支持设计读取、修改和注释
- 批量文本替换功能
- 组件实例覆盖传播
- 多种格式的导出功能

## English

Usage Workflow:
1. Add server to Cursor MCP configuration
2. Start WebSocket server
3. Install and run Figma plugin
4. Join communication channel
5. Use AI agent to interact with Figma through MCP tools

## 中文

使用工作流：
1. 将服务器添加到Cursor MCP配置
2. 启动WebSocket服务器
3. 安装并运行Figma插件
4. 加入通信频道
5. 使用AI代理通过MCP工具与Figma交互

## English

Contributions:
- Bulk text replacement by [@dusskapark](https://github.com/dusskapark)
- Instance override propagation by [@dusskapark](https://github.com/dusskapark)
- MIT License

## 中文

贡献者：
- 批量文本替换功能由[@dusskapark](https://github.com/dusskapark)贡献
- 组件实例覆盖传播由[@dusskapark](https://github.com/dusskapark)贡献
- MIT许可证

## English

For more information, check the [GitHub repository](https://github.com/grab/cursor-talk-to-figma-mcp) and the [demo video](https://www.linkedin.com/posts/sonnylazuardi_just-wanted-to-share-my-latest-experiment-activity-7307821553654657024-yrh8).

## 中文

更多信息，请查看[GitHub仓库](https://github.com/grab/cursor-talk-to-figma-mcp)和[演示视频](https://www.linkedin.com/posts/sonnylazuardi_just-wanted-to-share-my-latest-experiment-activity-7307821553654657024-yrh8)。
