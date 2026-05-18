# 每日入库报告 · 2026-05-18 (Evening)

## 执行概况

- **时间**: 2026-05-18 20:00 (Asia/Shanghai)
- **模式**: 晚间入库（完整流程，含 git push）
- **Phase 1**: 扫描最近 24h 新增/修改内容
- **Phase 2-4**: 0 条新条目入库（全部已存在）
- **Phase 5**: 站点生成 + git push 完成

## 发现

### intake/ 目录
intake/ 目录为空，无待处理素材。

### Obsidian 最近 24h AI 相关文件
本轮扫描共发现 6 个 openclaw/content/ 文件（含 5 个已入库 X 内容 + 1 个 openclaw/README.md 变动），经逐一比对，均已存在于 entries.json：

| ID | 标题 | 来源 | 状态 |
|----|------|------|------|
| 2aef58dd | 用 MCP + Claude Code 搭建 AI Agent 工作流实战 | X | ✅ 已入库（2026-04-26） |
| 5c7a3ee4 | Karpathy：本地 Demo 到线上产品，DevOps 是最难的部分 | X | ✅ 已入库（2026-04-25） |
| 698e1058 | 神经符号 AI 解 RAG 规模化失效 | X | ✅ 已入库（2026-04-20） |
| e5f6g7h8 | Google 推出 Gemini 3.1 Flash TTS | X | ✅ 已入库（2026-04-25） |
| q7r8s9t0 | tibo_maker 复盘：从 9 个失败产品到 5 个 AI 产品月入 100 万美元 | X | ✅ 已入库（2026-05-02） |
| openclaw/README.md | — | 元数据 | ⏭️ 无效内容 |

**结论**: 本轮扫描周期内无新增 AI 条目入库。

## 修复

本轮发现并修复 1 个致命问题（null quality_score 阻塞验证脚本）：

| ID | 修复内容 |
|----|---------|
| dffcaef8 | `Introducing GPT-5` → quality_score: null → 3, status: active → score-pending |

该条目在 2026-05-18 早间入库时因原文抓取失败，quality_score 未被正确设置，导致 `validate-schema.py` 运行时 TypeError。已通过 pipeline_utils.save_entries_data() 修复，并成功 push。

## 验证结果

- **entries.json**: 975 条总条目，✅ 格式正确
- **Schema 校验**: ✅ 975 条, 0 错误, 2 警告（活跃 URL 重复 2 对）
- **站点生成**: ✅ 成功（579 display cards, 500 content pages, 7 channels）
- **git push**: ✅ bd3936e

## 当前 entries.json 概况

```
Total: 975 entries
Active: 615 | Score-pending: 95 (含 dffcaef8) | Archived: 266
本轮新增: 0（修复: 1）
分类分布: coding(185), agents(127), learning(120), models(112),
          industry(75), infra(71), ai-tools(67), uncategorized(59), ...
```

## git push 验证

- **push 前**: entries.json 条目数 = 975（与 HEAD 一致）
- **修复后**: 条目数 = 975（不变，仅修改字段）
- ✅ 推送前检查通过

## 下一步

- **Morning Intake (2026-05-19 08:00)**: 扫描最新内容
- **注意事项**: 抓取失败的条目必须确保 quality_score 正确设置（避免再入 score-pending）