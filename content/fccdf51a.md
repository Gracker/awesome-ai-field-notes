# AudioScript: local real-time bilingual captions with sherpa-onnx

- **ID**: fccdf51a
- **原文链接**: https://x.com/GitHub_Daily/status/2113601349330055221
- **作者**: @GitHub_Daily
- **日期**: 2026-10-23
- **分类**: coding
- **来源类型**: x-post
- **标签**: speech-to-text, local-models, translation, desktop-app
- **质量评分**: 3/5
- **抓取时间**: 2026-10-24 (Asia/Shanghai)，grounded in vault full-text sources

---

## 中文导读

@GitHub_Daily 推荐 niyongsheng/AudioScript（Rust + Tauri 2 桌面工具）：监听系统声音输出，实时转写成文字再翻译成中文，以双语悬浮字幕浮在屏幕上，定位是讯飞同传的免费平替。识别用 sherpa-onnx 流式 zipformer 中英双语小模型，内置权重从官方包 474 MB 剪裁到 58 MB（encoder int8 41 MB + decoder fp32 13 MB + joiner int8 3.1 MB）；翻译走 CTranslate2 int8 opus-mt，每方向 76 MB。全本机运行、音频不上传、断网可用。

## 为什么值得关注

推文说「内置模型只有 58 MB」只算了识别那一半——两个方向的翻译模型装下来约 164 MiB，加 ASR 合计约 220 MiB。经仓库 SPEC 核对的决定手感的数字：M 系列 CPU 单句翻译 70–77 ms（beam=1），但冷启动到首字实测 1.25–2.2 s，超了作者自定的 200 ms 预算；稳态 80 秒偏差 −165±6 ms 无累积漂移。只翻 final 不翻 partial，按 0.8 s 静音断句、最长句 8 s。macOS 跨全屏置顶依赖 macos-private-api，上不了 Mac App Store，只能走 GitHub Releases；Linux 是二等支持（GNOME Wayland 不可用）。当字幕工具用，别当同传。

## 关键信息

- 仓库：niyongsheng/AudioScript，Rust + Tauri 2，MIT，2026-10-14 建仓，158 星 / 31 fork
- 模型：sherpa-onnx zipformer 中英双语（58 MB）+ CTranslate2 opus-mt int8（76 MB/方向）
- 延迟：70–77 ms/句（M 系列、beam=1）；冷启动首字 1.25–2.2 s（预算 200 ms 未达标）
- 断句：静音 0.8 s / 最长 8 s；只翻 final
- 分发：v0.2.10（2026-10-23）macOS 仅 aarch64 dmg；Intel 需自编译

## English Summary

GitHub_Daily highlights niyongsheng/AudioScript, a Rust + Tauri 2 desktop app that listens to system audio, transcribes it with sherpa-onnx's streaming zipformer zh-en model (~58 MB bundled), and translates via CTranslate2 int8 opus-mt (76 MB per direction) - fully on-device, positioned as a free substitute for iFlytek simultaneous interpretation. Details verified against the repo SPEC: 70-77 ms per-sentence translation on M-series CPUs, but 1.25-2.2 s cold-start-to-first-caption against the author's own 200 ms budget; only final (not partial) segments get translated, segmented on 0.8 s trailing silence; macOS always-on-top over fullscreen needs the macos-private-api, so it cannot ship on the Mac App Store. 158 stars; v0.2.10 (Oct 23) ships an aarch64 dmg only - a caption tool, not simultaneous interpretation.

## Obsidian Notes

- Vault sources: `X 文章/2026-10-24-1244-GitHub_Daily-AudioScript-声稿.md` (opencli twitter article) + `OpenClaw定时任务/X书签消化/2026-10-24-X书签消化.md` (GitHub API / README / docs/SPEC.md v2.1 / model-catalog.json 事实核对记录).
- Fetched 2026-10-24 via the evening intake pipeline; entry appended through pipeline_utils with URL dedup precheck.
