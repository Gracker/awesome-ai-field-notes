# Codex CLI 0.167.0: agent command center, backend switching with draft retention

- **ID**: e2baf2e1
- **来源**: https://github.com/openai/codex/releases/tag/rust-v0.167.0
- **发布**: 2026-11-06（Latest，0.166.0 → 0.167.0，tag `rust-v0.167.0`）
- **抓取**: gh release body，2026-11-07

## 摘要

Codex 正式版 0.167.0 新增 `codex agents --no-daemon` 指挥台与会话选择器未读标记；终端切换已连接后端时保留草稿；本地图片附件可预览；登录流程加 "Sign in another way" 与 `gcp_setup_wizard`（Vertex）；`/experimental` 可启用系统代理；审批弹窗打开时可直接在 transcript 展开 patch。

## New Features（节选）

> - Open the agent command center with `codex agents --no-daemon`. The command center and session picker now mark unread results
> - Switch between connected backends from the terminal session picker and keep your drafts when switching
> - Preview local image attachments while composing on supported terminals, and open viewed local images from clickable transcript paths
> - Find API key and cloud provider options under "Sign in another way." Enable `gcp_setup_wizard` to set up Google Cloud Vertex AI with Application Default Credentials or a credential file
> - Opt into macOS or Windows system proxy settings from `/experimental`
> - Expand patch details directly in the transcript while an approval prompt is open

## Bug fixes 要点

- 切换 model provider 后已保存 chat 保持可见；无法恢复的 chat 仍可读 transcript 并准备可编辑 prompt 续跑。
- 自动上下文压缩开始计入失败响应的保留输出与缺失 token 用量的响应。

## 中文要点

- 指挥台 + 未读标记把「同时跑多个 agent」的日用面搬进终端；换后端保草稿降低多后端切换成本。
- Pre-release 头已到 0.169.0-alpha.2，与正式版分开看待。

## 证据与来源

- `Hermes 定时任务/last30days/2026-11-07-ai-coding-agents-brief.md`
