# 去重报告 · 2026-08-31 (weekly-maintain-dedup)

## 总览
- 条目数: 2068 → 2068（不变，归档制去重）
- Active: 1445 → 1423（-22），Archived: 584 → 606（+22），score-pending: 39 不变
- 上次周维护: 2026-08-24（本轮新增 112 条，全部通过 URL/标题/占位符检查，无可疑条目）

## 自动处理

### 1. 硬 URL 重复（11 组，全部已解决，0 组需要动作）
全部 11 组 normalized-URL 重复均为 active:1 + archived:1 组合（历史去重残留），不存在 active-vs-active 重复。无需处理。

### 2. 影子重复归档（22 条，本轮核心）
2026-06-07 与 06-13 两个批次遗留的"影子条目"：active、无 URL、summary 为空、`local_path` 直接指向同名 URL 孪生条目的内容页。本轮全部通过三重验证后归档（status → archived，保留条目与文件，未删除）：
- 验证条件：影子 active 无 URL + `title_key` 与孪生完全一致（或标题为孪生 ID 的占位符变体）+ 孪生有独立非空内容页
- 18 条标题一致影子 → 5a50bb51/klbtvlqs、7ca13420/9cbi80c7、3f437cab/efaw158d、222a298f/kgj14wcx、1590d703/ac4974b2、8e74b8ff/mckwifwe、f914b546/tr-xhkl-、b0f5dcae/8lwuhhmb、625b7c17/4abfo505、4af3e80d/xlkfmlwp、d507e746/6e1u2aox、9ccb84b8/230879f0、c08ed99d/zo5tepps、34f1efae/de6541bc、895d4c8a/f8f64796ed、f62abc25/aefa6b15、a3baf0e7/5870a0c3、24339048/f7612873
- 4 条占位符标题影子（标题即孪生 ID，已人工核对页面主题一致）→ b6cadf9d/a2a_protocol_v1_0_2026_001（A2A v1.0）、db85d2ef/a09cdbbd（@alliekmiller 推文）、b5f5f327/gpt55_release_2026_001（GPT-5.5 发布）、3d923e32/claude_opus_47_mythos_2026_001（Claude Opus 4.7 发布）
- 每对写入双向 `related` 互链，影子 `local_path_valid: false`
- score 吸收：22 对中影子与孪生分数均相等（3 vs 3 或 4 vs 5），无需分数吸收

### 3. related 软关联（新增 1 组，不合并）
- Gemini 3.1 Flash TTS: X 发布推 `b37b2087` ↔ Google 官方博客 `abea8210`（同一发布的两个来源，双向互链）

### 4. X 时间戳模板 URL（69 条）
`/status/YYYYMMDDHHMMSS_002` 模板形态 URL 共 69 条，全部为 2026-08-24 已归档条目，本轮无新增 active 实例。无需处理。

### 5. 微信 URL
- 4-key 多条目组 7 组：6 组为"active 孪生 + archived 影子"已解决形态；`z1jgz9it` vs `yzi1wbrv` 跨标题碰撞组维持上周结论（疑抓取 URL 损坏），继续挂人工，不做规范化/合并

## 待人工确认
- [ ] `z1jgz9it`（Google I/O 2024）vs `yzi1wbrv`（Claude Code 浏览器自动化）共享同一 __biz/mid/idx/sn 四元组（延续 2026-08-24，未自动处理）
- [ ] 6 组双 URL 同标题软重复（Auto Mode、Boris Cherny、Claude vs OpenAI、Prompt Engineering、GPT Image 2 库、OpenAI Agents SDK 等）为不同来源视角，建议维持 related 关联现状，不合并

## 验证
- `data/entries.json`: dict 结构，entries=2068=total_entries，本地=HEAD=origin/main=2068 ✅
- 条目数不变（2068→2068），仅 status/related/updated_date/local_path_valid 字段变更；non-shadow 条目零变更（diff 隔离验证）✅
- `scripts/validate-schema.py`: 0 错误 / 66 警告（HEAD 内容同样为 66，本轮去重新增 0 警告；+1 来自上周后新入库条目）✅
- 站点重建: 成功，展示卡片 1198→1194（-4 = 4 个占位符影子退出展示；18 个标题一致影子在上周生成器已按空摘要过滤，不在卡片集内），内容页 1112→1108（-4 = 4 个占位符影子自有页面）✅
- 内容文件全部保留在磁盘，未删除任何文件 ✅
