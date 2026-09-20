# 去重报告 · 2026-09-21 (weekly-maintain-dedup)

## 总览
- 条目数: 2377 -> 2377（不变，仅 URL 修复 + related 补齐）
- Active: 1732（本周 intake 新增 99 条），Archived: 606，score-pending: 39
- 上次周维护: 2026-09-14，当时基线 2278；本周净增 99
- 内容页: 1409，展示卡片: 1501（pre-run 一致）

## 本轮扫描结果

### 1. 硬 normalized-URL 重复
active-vs-active 1 组：`ed4dc19a` vs `ffd9dfec`（LessWrong Astra and Fable 同 URL），已于 2026-09-14 由 5d8/63d4 提交（5d596a8 前身）双向 related 修复，两条摘要视角不同（本站编译 vs 转载角度），按保守原则保留，无需再处理。11 组 active+archived 已解决形态与上周一致。

### 2. active 无 URL 影子条目
0 个（与前两周一致，无漂移）。

### 3. 同 URL 不同形态真实重复（1 组，本轮补链）
- `d74a7da1` (yoshuabengio.org/en/blog/why-are-ai-agents-lying-cheating-and-coordinating, 2026-09-13, score 5)
- `ae1c0b14` (yoshuabengio.org/en/publication/why-are-ai-agents-lying-cheating-and-coordinating, 2026-09-15, score 5)
- 同一篇 Bengio 文章的 blog 路径与 publication 路径两种形态，`normalized_url_key()` 不归一站点内路径差异所以硬去重漏过。两侧内容页均 grounded 非空（3333B / 1015B），摘要侧重不同（机制论证 vs 事件综述），保留两条、补双向 `related`，不归档不合并。

### 4. 同标题 active 双胞胎
精确同标题 active 组 16 组（上周 12 组 + 本周新增 Bengio 组、LessWrong 组）。其余 13 组均为"同一事件多来源/一人多名"弱证据且早已双向 related，维持现状。新增组仅上节 Bengio 一组需动作，LessWrong 组即第 1 节已解决形态。

### 5. URL 尾部粘贴残渣修复（6 条，本轮主要动作）
本周扫描发现 7 条 active 条目 URL 带爬取/粘贴残渣（尾部 `*`、`',`、截断路径）。逐条核对本地 content 页 + 搜索/opencli grounding + HTTP 状态后修复：
- `miovnhlw`（[译] AI计算民主化 第七部分）：原 URL 为截断的微信 conference/share 爬取页（content 页实为"未知错误"死页）。标题与 Modular 官方博客 Part 7 精确对应，修复为 `https://www.modular.com/blog/democratizing-ai-compute-part-7-what-about-triton-and-python-edsls`（HTTP 200）。
- `na4z0qvz`（AI编程工具 System Prompt 大合集）：去尾部 `*`，GitHub 仓库 URL（HTTP 200）。
- `cz2bo7ig`（Gates: AI is about to completely change...）：去尾部 `*`。gatesnotes.com 对 curl 403（bot 墙，content 页当年抓取即 Access Denied），搜索索引确认 `gatesnotes.com/AI-agents` 为该文 canonical 路径。
- `5hv63unh`（yibie Shipping at Inference Speed）：去尾部 `*`，X 状态 URL（HTTP 200）。
- `ppnqbbb5`（做AI产品两年实操经验）：去尾部 `*`，微信短链（HTTP 200）。
- `98kzc8ih`（Shuyi Medium 新书）：去尾部 `*`，Medium 403 为标准 bot 墙，URL 为 canonical Medium 格式。
以上仅改 `url` 字段，条目数不变，无删除无归档。

### 6. 标记待人工（1 条，未修复）
- `z8jjvpnw`：URL 为微信前端 JS 资源 `mmbizappmsg/.../mprdev-0.2.5.js`（尾部 `',`），content 页内容即该 JS + "环境异常"验证页，标题为 ID 派生占位 `Z8Jjvpnw`。真实文章无法从本地内容或搜索恢复，按 skill 决策规则不猜测修复，挂起待人工。建议后续删除或人工补真实 URL。

### 7. 微信 4-key 跨标题碰撞（延续待人工）
- `yzi1wbrv` vs `z1jgz9it` 仍共享同一 4-key tuple，按 guard 不归一不合并，继续挂起。
- 说明：本周扫描将 19 条微信短链 `/s/<hash>` 形态误报为"空 4-key 碰撞"——短链本就不含 `__biz/mid/idx/sn` 参数，属审计脚本口径问题，非数据问题，已排除。

### 8. 其他
- active URL 多 https:// / CJK 内嵌 / 图片 CDN 占位：0 条
- entry id 重复：0；缺 title/score：0
- 空双摘要 active 条目 52 条（上周口径 185 条，趋势回落）

## 验证
- `data/entries.json`: dict 结构，entries=2377=total_entries，本地=HEAD=origin/main=2377
- 仅 `url` 字段 6 处修复 + `related` 字段 +2 引用，条目数不变，无 status/归档操作
- `scripts/validate-schema.py` 与 `scripts/generate-site.py` 见下方回执

## 待人工确认
- [ ] `z8jjvpnw` JS 资源 URL，无法恢复真实文章
- [ ] 微信 `yzi1wbrv` vs `z1jgz9it` 跨标题碰撞（延续）

## 变更文件
- `data/entries.json`（url 修复 6 处 + related +2 引用）
- `metadata/stats.json`（last_updated 时间戳）
- `openclaw/logs/dedup-report-2026-09-21.md`（本报告）
