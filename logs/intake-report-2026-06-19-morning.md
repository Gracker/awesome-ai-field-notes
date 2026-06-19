# 每日入库报告 · 2026-06-19 (Morning)

## 执行概况

- **时间**: 2026-06-19 08:17 (Asia/Shanghai)
- **模式**: 早晨入库（增量模式，跳过 git push）
- **Phase 1**: 扫描最近 24h 新增/修改内容
- **Phase 2-4**: 0 条新条目入库（2 个候选已跳过）
- **Phase 5**: 站点生成成功
- **结果**: 无 entries.json 写盘触发，无 dist 内容增量

## 发现

### intake/ 目录
intake/ 目录为空（仅 `.gitkeep`），无待处理素材。

### Obsidian 最近 24h AI 相关文件（content/）
扫描窗口：2026-06-18 08:14 — 2026-06-19 08:14，共发现 9 个 content/ 文件被修改。

| ID | 文件 | 状态 | mtime | 大小 | 原因 |
|----|------|------|-------|------|------|
| ✅ | a2a_protocol_v1_0_2026_001.md | 已入库 | 2026-06-18 12:26 | 1109B | 已被 entries 引用 (`b6cadf9d`) |
| ✅ | a09cdbbd.md | 已入库 | 2026-06-18 12:26 | 1503B | 已被 entries 引用 (`db85d2ef`) |
| ✅ | gpt55_release_2026_001.md | 已入库 | 2026-06-18 12:25 | 34171B | 已被 entries 引用 (`b5f5f327`) |
| ✅ | claude_opus_47_mythos_2026_001.md | 已入库 | 2026-06-18 12:25 | 36824B | 已被 entries 引用 (`3d923e32`) |
| ✅ | mcp_framework_2026_001.md | 已入库 | 2026-06-18 21:03 | 307570B | 已被 entries 引用 (`mcp_framework_2026_001`) |
| ⏭️ | **46097a5e.md** | 跳过（重复） | 2026-06-18 21:03 | 96458B | 标题/URL 已存在于 entries (`46097a5e` + `6b5fef67`) |
| ✅ | mcp_2026_roadmap_001.md | 已入库 | 2026-06-18 21:03 | 151094B | 已被 entries 引用 (`mcp_2026_roadmap_001`) |
| ⏭️ | **10c3345d.md** | 跳过（重复） | 2026-06-18 12:25 | 6587B | 标题已存在于 entries (`10c3345d`，local_path=`content/af94b63c.md`) |
| ✅ | baoyu_ai_strategy_2026_001.md | 已入库 | 2026-06-18 21:03 | 14595B | 已被 entries 引用 (`baoyu_ai_strategy_2026_001`) |

**跳过原因（统一为 URL/标题去重命中）**：

- `46097a5e.md` 内容是 juejin 文章《什么 AI 写 Android 最好用？官方做了一个基准测试排名》的 Juejin 抓取存档（HTML/JS 残留较多），URL `https://juejin.cn/post/7614897667961143347` 已被 entries `46097a5e`（local_path=`content/6b5fef67.md`）和 `6b5fef67`（local_path=`manual_002.md`）同时引用。append_entries 会被 normalized_url_key 去重拦截为 `duplicate-url`。
- `10c3345d.md` 内容是 Gemma 4 12B 多模态模型的 X 推文存档（@demishassabis），但 entries 已存在 id=`10c3345d`，local_path 指向 `content/af94b63c.md`。append_entries 会被 title_key 去重拦截为 `duplicate-title`。
- 两个文件都属于「已有条目的备用本地存档」，未触发新增。

### 标题相似度 / URL 重复检查
- 全量扫描 entries.json，2 个 orphan 文件的 URL/标题均命中现有条目，无新增候选。

## 当前 entries.json 概况

```
Total: 889 entries
  - active (raw): 615
  - active (display): 180
  - score-pending: 274
  - archived: 0
本轮新增: 0
```

## 验证结果

- **validate-schema.py**: ✅ 0 新错误，1 错误 + 13 警告（全部为既有遗留）
  - 既有 ID 重复：`6eae3a5b`（2 条 score-pending 占位条目，标题为空 → 历史遗留）
  - 既有 URL 重复：`https://juejin.cn/post/7614897667961143347`（即 `46097a5e` 与 `6b5fef67`，来自不同批次的同文章入库）
  - 既有平台/分类告警：13 条为历史 platform/category 字段值不在合法枚举内
- **entries.json 结构**: ✅ dict 格式完整（`{"entries": [...], "last_updated": "2026-06-19", "total_entries": 889}`）
- **未触发 entries.json 写盘**：本轮 0 新增，无需 `append_entries` 调用（沿用 Jun 12 morning 报告的 same-pattern）
- **站点生成 (`npm run build` / `python3 openclaw/scripts/generate-site.py`)**: ✅ 成功
  - 180 display cards（与上轮一致）
  - 89 content pages（与上轮一致）
  - 7 channels（与上轮一致）
- **git push**: ⏭️ 跳过（由 Evening Intake 统一推送）

## 修改但未提交的文件

```
modified:   README.md                          (历史累积，未变更)
modified:   data/entries.json                  (历史累积，本轮未写盘)
modified:   entries.json                       (历史累积)
modified:   metadata/stats.json                (历史累积)
modified:   openclaw/README.md                 (历史累积)
```

## 下一步

- **Evening Intake (20:00)**: 扫描当日新内容并完成 git push
- **建议人工 review 的遗留数据问题**（不在本 morning intake 范围内）：
  - ID 重复 `6eae3a5b`（两条 score-pending，标题均为 `...`）— 疑似早期占位入库
  - URL 重复 juejin 文章 — 两条 active 条目并存（`46097a5e` / `6b5fef67`），建议保留质量更高、字段更完整的一条
  - 13 条历史 platform/category 字段告警 — 候选项中出现 `industry`/`openai`/`personal_blog`/`hackernews` 等非标准平台值
