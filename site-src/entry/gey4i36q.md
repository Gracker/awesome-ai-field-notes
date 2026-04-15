---
title: 'OpenClaw 运行报错指南（上篇）'
sidebar: false
---

::: info
[← 返回学习资源](/learning)
:::

# OpenClaw 运行报错指南（上篇）

> OpenClaw macOS 运行报错排查指南，覆盖 Gateway 全链路

🔗 [原文链接](https://x.com/lijiuer92/status/2026639705933328582) | @李韭二 | 🇨🇳 | ⭐⭐⭐⭐ 4 ⭐4 4/5 📅 2026-02-27

`openclaw` `troubleshooting` `gateway` `macos` `debug`

---

## OpenClaw 运行报错指南与故障排除

在使用 OpenClaw 过程中遇到错误是常见情况，本指南将帮助您系统地排查并解决 OpenClaw 运行时可能遇到的各种问题。

**一、通用故障排除步骤**

当遇到 OpenClaw 报错时，建议按照以下顺序进行排查：

1.  **运行诊断工具 `openclaw doctor`**
    这是排查 OpenClaw 问题的首要步骤。`openclaw doctor` 命令能够自动检测配置缺失、端口冲突、认证失效等大多数常见问题。如果 `openclaw doctor` 报告可修复的问题，您可以直接运行 `openclaw doctor --fix` 尝试自动修复。

2.  **检查服务状态**
    *   使用 `openclaw status` 检查 OpenClaw 的整体服务状态。
    *   使用 `openclaw gateway status` 检查 Gateway 服务的运行状态。正常情况下，`Runtime` 应显示 `running`，`RPC probe` 应显示 `ok`。

3.  **实时查看日志**
    运行 `openclaw logs --follow` 命令可以实时查看系统和 Gateway 的日志输出，这对于定位问题的具体原因至关重要。

4.  **访问 Web 控制面板 (Dashboard)**
    访问 `http://127.0.0.1:18789` (默认端口) 可以打开 OpenClaw 的 Web 控制台，可视化地查看 Gateway 运行状态、各通道连接状态以及最近的请求/响应记录。

5.  **尝试重启 Gateway**
    对于许多莫名其妙的问题，执行 `openclaw gateway restart` 命令重启 Gateway 服务可能就能解决。

6.  **备份配置并升级版本**
    在进行任何配置更改前，建议备份配置文件，例如：`cp ~/.openclaw/openclaw.json ~/.openclaw/openclaw.json.bak`。如果您使用的版本较旧，某些报错可能是已修复的 bug，尝试执行 `npm update -g openclaw` 升级到最新版本可能解决问题。

**二、常见错误类型及解决方案**

以下是 OpenClaw 常见报错及其对应的解决方案：

1.  **安装与命令找不到问题**

    *   **`openclaw: command not found` 或 `不是内部或外部命令`**
        *   **原因**: `npm` 全局安装的 `bin` 目录未加入系统 `PATH` 环境变量。
        *   **解决方案**:
            *   确认是否已安装：`npm list -g openclaw`。
            *   找到 `npm` 全局 `bin` 目录：`npm config get prefix`。
            *   将 `bin` 目录添加到 `PATH` 环境变量中。例如，对于 Linux/macOS 用户，可以将其添加到 `~/.bashrc` 或 `~/.zshrc` 文件中，然后运行 `source ~/.bashrc` 或 `source ~/.zshrc`。
            *   在 Windows 上，确保 `%AppData%\npm` 出现在您的系统 `PATH` 环境变量中。
            *   或者直接使用 `npx openclaw` 代替 `openclaw` 命令。

    *   **`npm install` 权限错误 (EACCES)**
        *   **原因**: `npm` 全局目录的权限不正确，当前用户没有写入权限。
        *   **解决方案**: 避免使用 `sudo npm install -g`。推荐使用 `nvm` (Node Version Manager) 来管理 Node.js 版本和 `npm` 权限，或者手动修改 `npm` 全局目录的权限。

    *   **`npm install failed` 或 `协议冲突`**
        *   **原因**: OpenClaw 的部分依赖包使用 HTTP 协议，而新安装的 `npm` 默认强制要求 HTTPS 协议，导致下载失败。
        *   **解决方案**: 在终端执行 `npm config set strict-ssl false` 取消 `npm` 对 HTTPS 的强制限制。

    *   **`Node.js 版本不兼容\** (`engine node is incompatible`)**
        *   **原因**: OpenClaw 对 Node.js 版本有严格要求，通常需要 Node.js 22+ (部分文档提及 22.14.0+，macOS 需要 22.16.0+，或推荐 24.x)。
        *   **解决方案**: 使用 `nvm` (Node Version Manager) 升级或切换 Node.js 版本。例如：`nvm install 22 && nvm use 22`。

2.  **Gateway/服务启动问题**

    *   **服务无法启动 (`Runtime: stopped`) 或启动后立即退出**
        *   **原因 A: 端口被占用 (`EADDRINUSE`)**: OpenClaw 默认使用 18789 端口，如果该端口已被其他进程占用，会导致启动失败。
        *   **解决方案 A**:
            *   查看占用端口的进程：`lsof -i :18789`。
            *   杀死占用进程：`kill -9 <PID>`。
            *   或者在配置文件中修改端口：`~/.openclaw/openclaw.json` 中设置 `gateway: { port: 18790 }`。
        *   **原因 B: 缺少 `gateway.mode` 配置**: `openclaw.json` 中未设置 `gateway.mode=local`，导致 Gateway 无法初始化。
        *   **解决方案 B**: 运行 `openclaw config set gateway.mode local`。
        *   **原因 C: 配置文件 Schema 校验失败**: OpenClaw 对配置文件有严格的 Schema 校验，任何未知键或类型错误都会阻止 Gateway 启动。
        *   **解决方案 C**: 查看日志 (`openclaw logs | grep config`) 获取具体校验错误，并重置错误键名：`openclaw config unset <错误的键名>`。

    *   **`API Key 无效` / `API 调用失败` / `401/403` (Unauthorized/Forbidden)**
        *   **原因**: API Key 配置错误、权限不足或未设置。
        *   **解决方案**: 检查 API Key 和 Base URL 是否正确。对于 401 错误，可能需要执行 `openclaw models auth setup-token` 进行设置。

    *   **`HTTP 429` (长上下文速率限制 / Too Many Requests)**
        *   **原因**: 启用了 100 万 Token 上下文 (`context1m`) 但 API Key 对应的账户等级不满足条件，或达到 API 调用频率限制。
        *   **解决方案**:
            *   等待 60 秒后重试。
            *   配置备用模型以实现自动故障转移，避免单一 API Key 限流影响服务。
            *   调整上下文长度设置。

3.  **其他常见问题**

    *   **`DNS resolution failed` (日志中大量网络错误)**
        *   **原因**: Docker 容器内部的 DNS 解析问题，或者代理地址配置错误 (例如代理软件未开启或端口不正确)。
        *   **解决方案**: 检查 Docker 容器的网络配置和代理设置。

    *   **`Gateway Token` 必须设置吗？**
        *   **说明**: Gateway Token 是访问 OpenClaw Gateway 的认证凭证。如果不设置，任何知道 Gateway 地址的人都能连接并发送消息。建议进行设置以增强安全性。

    *   **升级后失效**
        *   **原因**: 版本升级后，配置 `schema` 可能发生变化，导致旧配置文件中的键名或格式在新版本中失效。
        *   **解决方案**: 运行 `openclaw doctor --fix` 尝试自动修复，或者根据最新文档更新配置文件。

    *   **响应速度慢**
        *   **解决方案**: 考虑使用更快的模型。

希望这份指南能帮助您解决 OpenClaw 运行中的各种报错问题。如果在排查过程中仍然无法解决，建议携带完整的错误信息、`openclaw --version`、`openclaw status --all` 的输出以及您最近的操作，前往 OpenClaw 官方社区或 GitHub Issues 寻求帮助。
