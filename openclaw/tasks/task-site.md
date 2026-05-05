# OpenClaw Task: 站点重新生成 (Site)

## 目标
从 `data/entries.json` 重新生成 God of GPT 现代静态站、README、stats。

## 触发条件
- `data/entries.json` 有实质性变更（新增/修改/归档条目）
- content/ 目录有新增全文
- 每周维护完成后

> 注意：日常由 Content Fetcher 和 Daily Intake 自动触发 rebuild + push。
> 此任务仅在需要单独重建时手动调用。

## 执行流程

```bash
cd <仓库路径>
npm run build
```

## 验证
- `dist/` 目录已生成（首页、频道页、详情页、归档、专题、搜索索引、sitemap）
- `npm run build` 已通过，Cloudflare Pages 输出目录为 `dist`
- `README.md` 统计摘要已更新
- `metadata/stats.json` 已更新

## 约束
- 生产站入口是 `openclaw/scripts/generate-modern-site.py`
- 兼容旧任务的 `scripts/generate-site.py` / `openclaw/scripts/generate-site.py` 也必须转到现代静态站生成器
- 不要再把 VitePress / `site-src` 当主站生成链路
- 页面日期必须直接显示 `YYYY-MM-DD`，禁止显示“今天/昨天/今日/昨日”等相对日期
- `dist/` 是 ignored 构建产物，Cloudflare 会现场生成，不要强行提交

## 提交
```bash
git add -A
git commit -m "[openclaw] site: regenerate from entries.json"
git push origin main
```
