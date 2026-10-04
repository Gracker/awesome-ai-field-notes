# 去重报告 · 2026-10-05 (weekly-maintain-dedup)

## 总览
- 条目数: 2591 -> 2591（不变；本轮 0 合并、0 归档、0 URL 修复、0 新增标记，纯扫描周）
- 上周基线: 2466（2026-09-28），本周 intake 净增 +125；其中 added_date > 2026-09-28 的 active 新条目 111 条全部纳入本轮扫描
- Active: 1946（上周 1821），Archived: 606，score-pending: 39
- 展示卡片 1865 / 内容页 1774 / 7 频道，与 pre-run 一致（本轮未新增条目和内容页）
- 时效归档扫描: active 且 added_date > 180 天且 score ≤ 3 的 article/x_post = 0 条，无归档动作

## 本轮扫描结果

### 1. 硬 normalized-URL 重复
- 全库同 normalized-URL 组共 12 组：active-vs-active 1 组，active+archived 已解决形态 11 组（同上周）。
- active-vs-active 仍为 `ed4dc19a` vs `ffd9dfec`（LessWrong Astra and Fable，同 URL 不同 score 3/4），双向 related 已存在，两条为不同抓取视角，按保守原则继续维持现状（连续第三周）。

### 2. 本周新增条目（111 条 active）重复检查
- 与全库 normalized-URL 碰撞: 0 组新增（append_entries 的 duplicate-url/duplicate-title 拦截正常）。
- 标题相似度 fuzzy 扫描（title_key SequenceMatcher ≥ 0.88，跨全库 active）: 0 对。本周无近重复标题流入。

### 3. 同标题 active 双胞胎
- 精确同标题 active 组 16 组（上周 14 组），全部 16 组均已双向 related；0 组需补链，0 组三胞胎。

### 4. 影子条目（无 URL 且 local_path 指向同标题 URL 条目）
- 0 条（06-2026 影子批量归档后连续保持 0）。
- active 无 URL 条目共 194 条（与上周口径一致），均为 6 月初批量导入的旧类目（local_path 指向站点外 Obsidian 笔记），属 local-path 校验职责，非重复，不处理。

### 5. 微信 4-key 跨标题碰撞
- `yzi1wbrv` vs `z1jgz9it`：仍共享同一 (__biz, mid, idx, sn) tuple（corrupt crawl URL 案例），按跨标题碰撞 guard 继续挂起待人工，不 canonicalize、不合并（连续第三周）。

### 6. 可疑 URL（active）
- 多 https:// / CJK 内嵌 / 尾部残渣 / 未 trim / 非法 scheme：0 条。

### 7. 完整性
- entry id 重复: 0；缺 title: 0；缺 score: 0；related 悬挂引用: 0
- entries=2591=total_entries，dict 结构合法

## 标记待人工（延续，非本轮新增）
- [ ] `z8jjvpnw`：URL 已按本地转储修复为真实文章参数，标题仍为占位 `Z8Jjvpnw`，需人工补标题（或确认文章已 404 后处理）
- [ ] 微信 `yzi1wbrv` vs `z1jgz9it` 跨标题 4-key 碰撞（延续）

## 验证
- `scripts/validate-schema.py`: 2591 条，0 错误，58 警告（历史 summary_zh 过短，非本轮引入；上周 55 条，差值来自本周新增条目自身的短摘要警告，均非错误）
- `npm run build`: 成功，1865 展示卡片 / 1774 内容页 / 7 频道（与 pre-run 一致，无新增页面为预期）
- 条目数基线: 本地 = HEAD = origin/main = 2591（提交前校验）
- `data/entries.json` 本轮零写入；openclaw/content/ 无游离文件

## 变更文件
- `openclaw/logs/dedup-report-2026-10-05.md`（本报告）
- `metadata/stats.json`（构建时间戳）
- `data/entries.json` 无变化（count 2591 不变）
