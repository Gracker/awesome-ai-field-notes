# OpenClaw Task: 站点重新生成 (Site)

## 目标
从 `data/entries.json` 重新生成 VitePress 站点、README、stats。

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
- `site-src/` 目录已更新（index.md + 顶层分类页 + entry/ 详情页）
- `site-src/.vitepress/config.ts` 已自动生成
- `npm run build` 已通过，Cloudflare Pages 使用同一条生成 + VitePress 构建链路
- `README.md` 统计摘要已更新
- `metadata/stats.json` 已更新

## 约束
- `site-src/` 的 Markdown 页面完全由 `scripts/generate-site.py` 生成，禁止手写页面或保留旧分类体系页面
- 页面日期必须直接显示 `YYYY-MM-DD`，禁止显示“今天/昨天/今日/昨日”等相对日期
- `site-src/entry/` 是 ignored 构建产物，Cloudflare 会现场生成，不要强行提交

## 提交
```bash
git add -A
git commit -m "[openclaw] site: regenerate from entries.json"
git push origin main
```
