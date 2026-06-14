# OpenClaw Automation

这个目录保存 God of GPT / AI Field Notes 的自动化任务、数据维护脚本和兼容入口。

## 当前生产链路

1. 日常 intake / community review 写入 `../data/entries.json` 和 `../content/*.md`
2. 所有新条目写入前必须走 `scripts/pipeline_utils.py`
3. 站点生成入口统一为 `npm run build`
4. 旧入口 `python3 scripts/generate-site.py` / `python3 openclaw/scripts/generate-site.py` 会转到现代静态站生成器
5. Cloudflare Pages 发布 `../dist`

## 当前数据

- 原始条目: 826
- 公开展示卡片: 123
- 有全文内容: 60
- 最近 7 天信号: 91

## 关键脚本

- `scripts/pipeline_utils.py`: intake 共享清洗、去重、分类归一、日期规范
- `scripts/generate-modern-site.py`: 生成 God of GPT 现代静态站
- `scripts/generate-site.py`: 兼容旧任务的现代站入口
- `scripts/validate-schema.py`: 数据结构校验
- `scripts/weekly-maintain.py`: 周维护和低信号挂起
- `scripts/weekly-dedup.py`: URL 与标题去重

不要再把 `site-src` / VitePress 当生产主链路。
