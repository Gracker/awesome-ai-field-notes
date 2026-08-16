# 去重报告 · 2026-08-17 (weekly-maintain-dedup)

## 总览
- 条目数: 1830 → 1830（不变，本次采用「归档去重」而非删除）
- Active: 1564 → 1236（-328），Archived: 9 → 337（+328），score-pending: 257 不变
- 站点重新生成: 1009 → 994 展示卡片，918 → 914 内容页

## 自动处理
- URL 重复（同一 URL 双 active）: 1 组 → `hqm6txq4` 归档（保留 `8wchcs0s`）
- 影子重复（无 URL、标题与带 URL 孪生完全一致、local_path 指向孪生内容文件）: 326 条 → 归档并互链 related
  - 其中 11 条仅标题匹配，已用内容文件交叉验证（文件含孪生标题/URL）
  - 其中 4 条高分影子（3248af72/10c3345d/61e1f044/855101d8，score 4-5）：分数已并入保留的带 URL 孪生条目（ba595150/af94b63c/dba5fe77/60e94298），孪生均有独立内容页 → 内容页 -4 属预期去重语义
- 微信 URL 规范化: 71 条（去除 chksm/mpshare/scene/srcid/sharer 追踪参数，保留 __biz/mid/idx/sn）
- 微信 sn 尾部 `%2A` 粘贴伪影修复: 1 条
- 垃圾测试条目: `test-2026-06-08`（Test AI Content，假 URL）→ 归档（未删除）

## 待人工确认
- [ ] 跨标题 URL 冲突（未自动处理，两侧内容为不同文章，疑有一方抓取 URL 损坏）:
  - `z1jgz9it` "Google I/O 2024" vs `yzi1wbrv` "Claude Code 浏览器自动化" 共享同一 __biz/mid/idx/sn（__biz 属刘小排r，z1jgz9it 的 URL 疑为错误抓取；其内容页标题为 Google I/O 文章）
- [ ] 同标题多 URL（7 组）: prompt engineering、Claude vs OpenAI 编程文、Boris Cherny 访谈（中译 vs 原文）、OpenAI Agents SDK、Auto Mode 默认化、GPT Image 2 prompt 库 等 — 多为中英/不同来源视角，建议保留并靠 related 关联，不建议合并
- [ ] 标题相似仅弱证据 1 条: `b995a05a` vs `89fa848ed0d4`（2026 AI 编程 Agent 分水岭/Harness 详解）

## 验证
- `data/entries.json`: dict 结构，entries=1830=total_entries ✅
- `scripts/validate-schema.py`: 0 错误；警告 67 → 65（改善） ✅
- 站点生成成功: 994 卡片 / 914 内容页 / 7 频道 ✅
- 内容页 -4 全部为「高分影子归档、保留孪生」的正确去重语义，孪生均active且有独立内容页 ✅
