# Official Claude Code Extension Compromise: Security Advisory

- **原文链接**: https://phorion.io/blog/offical-claude-code-vsx-compromise/
- **作者**: Phorion
- **日期**: 2026-10-30
- **分类**: agents
- **来源类型**: article
- **标签**: supply-chain, vscode-extension, ssh-backdoor, cursor, claude-code
- **质量评分**: 5/5
- **抓取时间**: 2026-10-31T00:04:04Z

---

## 中文导读

Phorion 披露 Cursor Marketplace 上的官方 Claude Code for VS Code 扩展 2.1.313 被植入后门：extension.js 注入的 IIFE 在模块加载时执行，无需用户交互，写入注释为 svc-telemetry 的 Ed25519 SSH 后门公钥，带三平台持久化并回传主机侦察信息，Cursor 已下架该版本；macOS 上因未提权执行 systemsetup -getremotelogin 报错但退出码为 0，脚本误判跳过开启 SSH，未开 SSH 的 Mac 入侵路径断链，但密钥与持久化仍落地；排查按公钥指纹而非注释串。

## 为什么值得关注

Claude Code 生态的真实供应链事件：IDE 扩展权限等于用户权限，用 Cursor/Claude Code 的团队都需排查 2.1.313。

## 关键信息

- 标题: Official Claude Code Extension Compromise: Security Advisory
- 作者/来源: Phorion
- 链接: https://phorion.io/blog/offical-claude-code-vsx-compromise/
- 发布时间: 2026-10-30
- 关联标签: supply-chain, vscode-extension, ssh-backdoor, cursor, claude-code

## Source Highlights

- Phorion detected a backdoor in the official Claude Code for VS Code extension bundle on the Cursor Marketplace (version 2.1.313) that drops a persistent SSH backdoor across macOS, Linux, and Windows. Cursor removed the release from its marketplace and pulled NPM and VS Code versions of 2.1.313 from their registries.
- The compromised extension.js starts with an injected IIFE prepended to the minified bundle; it imports child_process, fs, os, path, http, and crypto and executes as soon as Node loads the file, before the normal activate callback — no user interaction required.
- Stage 1 prepares SSH access: it creates ~/.ssh, appends an attacker-controlled Ed25519 public key to authorized_keys with a svc-telemetry comment, and sets 0700/0600 permissions. For hunting, check the public-key fingerprint rather than relying on the comment string.
- On macOS the enable-SSH step is broken by a likely oversight: systemsetup -getremotelogin is run without root, prints an administrator-access error and exits 0, so the script — which only enables SSH when the output is exactly Off — skips enablement entirely. On hosts without SSH already running the inbound path breaks, though keys and persistence still land.
- Extensions run with the permissions of the IDE and the user, so a backdoored extension gets immediate access to local files, source code, and developer tooling the moment its module loads. Organisations should review environments for Claude Code for VSCode 2.1.313 and engage incident response where found.

## English Summary

Phorion reports a backdoored build of the official Claude Code for VS Code extension (2.1.313) distributed via the Cursor Marketplace: an injected IIFE in extension.js runs on module load — no user interaction needed — installs an Ed25519 SSH backdoor (authorized_keys comment svc-telemetry) with persistence logic for macOS, Linux, and Windows, and beacons host reconnaissance. Cursor has pulled 2.1.313 from its marketplace, NPM, and the VS Code marketplace. On macOS the implant's enable-SSH step checks systemsetup -getremotelogin without root, which errors and exits 0, so the script skips enablement on hosts without SSH already running — keys and persistence still land. Hunters should match key fingerprints, not the comment string. Extensions run with IDE and user permissions, giving immediate access to source code and developer tooling.

## Obsidian Notes

- 内容由 `opencli web read` 抓取原文公告生成，锚定在感染链、SSH 部署步骤、macOS 提权 bug 与下架信息等正文事实。
- 关联条目: content/bf5aaab6.md（external-scan 2026-10-31 运行生成）
