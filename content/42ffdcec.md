# Claude Code 2.1.322 users report stray copyright reminders from a botched system prompt

- **ID**: 42ffdcec
- **原文链接**: https://www.reddit.com/r/ClaudeCode/comments/1xssfs1/21322_anthropics_copyright_paranoia_is_leaking/
- **作者**: r/ClaudeCode
- **日期**: null（原帖具体日期未核实）
- **分类**: coding
- **来源类型**: article
- **标签**: claude-code, system-prompt, copyright, community, release-behavior
- **质量评分**: 3/5
- **抓取时间**: 2026-11-12T15:45:39Z

---

## 中文导读

r/ClaudeCode 帖（约 565 赞、92 评）：升到 Claude Code 2.1.322 后模型反复提到收到版权提醒却说不清来源，追问后出现类似 <ip_reminder> 的自动提醒片段，社区归因于 system prompt 变更引入。与同一版号上传出的 Vertex fast mode 相对照：正式版号持平不等于日用无新行为。若本机在 2.1.322 且警告莫名其妙，先对照该帖并检查异常 system/reminder 段，不要直接当业务侵权处理；是否已在后续版本修掉待官方说明。

## 为什么值得关注

提示词层变更成为日用事故的直接案例：行为摩擦先于版本号出现，排查看 system 段而不是猜业务违规。

## 关键信息 / 证据摘录

- 证据源：last30days 社区简报 2026-11-12「可发帖素材 2」；Reddit 指标约 565 赞 / 92 评。
- 帖内关键描述：升级后模型反复提及收到版权提醒、说不清来源；追问后出现类似 <ip_reminder> 的自动提醒片段。
- 关联同窗帖：r/ClaudeCode「Reverse Engineer anything」约 511 赞 / 88 评，同日前后出现。

## English Summary

An r/ClaudeCode thread (~565 upvotes, 92 comments) reports that after upgrading to Claude Code 2.1.322, the model repeatedly mentions receiving copyright reminders it cannot explain; on follow-up, fragments resembling an automatic <ip_reminder> appear, which the community attributes to a botched system-prompt change. Read alongside the Vertex fast-mode reports on the same version number, this shows version-frozen releases can still ship user-visible behavior changes. If your local 2.1.322 sessions show inexplicable copyright warnings, compare against the thread and inspect anomalous system/reminder segments rather than treating it as a licensing violation; whether it is fixed in a later tag remains unconfirmed.

## Obsidian Notes

- 内容获取路径：last30days 社区简报 / 本地 DeepResearch 材料作为证据源，正文事实逐条对应上述摘录；原文页未直接抓取的部分已在证据行标注。
- 现代站点生成器按 `content/42ffdcec.md` 查找内容页；本文件写入 canonical content 目录。
