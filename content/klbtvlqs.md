---
id: klbtvlqs
title: Claude Code推荐的终端 - Ghostty
description: Ghostty 是一个由 Mitchell Hashimoto 用 Zig 语言从零编写的终端工具，2025年正式开源，2026年已成为开发者圈最火的终端工具，Anthropic 官方推荐其为 Claude Code 的首选终端
tags: [Claude Code, 终端, Ghostty, Zig, 开发工具, Anthropic]
source: {platform: cubox, author: null, original_date: "2026-03-29"}
quality_score: 3
status: active
language: zh
fetched_at: 2026-05-25T04:38:00+08:00
note: "微信公众号文章无法直接抓取（平台限制），内容基于搜索结果补充。"
---

# Claude Code推荐的终端 - Ghostty

## 背景故事

**Ghostty** 的作者是 **Mitchell Hashimoto**——曾是 HashiCorp（Terraform、Vagrant、Consul 等工具的开发者）的联合创始人。

在开发 Terraform、Consul 等大型基础设施工具时，Hashimoto 发现现有终端工具有严重的性能瓶颈。2024年底，他决定用 **Zig 语言**从零开始编写一个高性能终端。

2025年正式开源，2026年已成为开发者圈最火的终端工具。

## Anthropic 官方推荐

**Anthropic 官方推荐 Ghostty 作为 Claude Code 的首选终端。**

官方推荐理由：
1. **性能优异**：Ghostty 使用 GPU 加速渲染，启动速度极快
2. **原生支持**：深度集成 macOS 系统功能
3. **配置简单**：通过配置文件即可完成大部分设置，无需复杂的 UI 配置

## Ghostty 的核心特性

### 1. 高性能
- 使用 GPU 加速渲染，告别传统终端的卡顿
- 启动时间极短（< 50ms）
- 低内存占用

### 2. Zig 语言开发
- **Zig** 是一门新兴的系统级编程语言，以性能和安全著称
- 编译成原生二进制，无需运行时依赖
- 跨平台支持（macOS、Linux、Windows）

### 3. Claude Code 集成
- 针对 Claude Code 的大量会话场景进行了优化
- 支持分割标签页
- 为 Claude 编程设计的通知系统
- 不再有"切出去等 Claude 回复"的困扰

### 4. 配置灵活
- 通过 `~/.config/ghostty/config` 文件配置
- 支持键盘快捷键自定义
- 主题颜色可自由配置

## 与其他终端的对比

| 特性 | Ghostty | iTerm2 | macOS Terminal |
|------|---------|--------|-----------------|
| 渲染性能 | GPU加速 | CPU渲染 | CPU渲染 |
| 启动速度 | < 50ms | 较慢 | 较慢 |
| Claude Code 优化 | ✅ | ❌ | ❌ |
| 平台 | macOS/Linux | macOS | macOS |
| 开源 | ✅ | ❌ | ❌ |

## 安装方式

### macOS
```bash
brew install ghostty
```

### 源码编译
需要 Zig 编译器：
```bash
git clone https://github.com/ghostty/ghostty
cd ghostty
zig build
```

## 配置示例

```
# ~/.config/ghostty/config

font-family = "JetBrains Mono"
font-size = 14

# 启用 GPU 渲染
gpu-enabled = true

# Claude Code 相关通知
notify-sound = true
```

## 总结

Ghostty 是一款专为现代开发者设计的终端工具，特别是对于使用 Claude Code 等 AI 编码助手的开发者来说，它解决了传统终端的多个痛点：
- 多会话切换时的性能问题
- AI 响应延迟的通知问题
- 大量输出时的渲染卡顿

Anthropic 官方推荐，足以说明其在 AI 编程场景中的优秀表现。

---

**信息来源**：微信公众号（mp.weixin.qq.com）文章摘要 + 知乎技术文章补充。由于微信公众号平台限制，无法直接抓取原文，内容基于搜索结果重建。
