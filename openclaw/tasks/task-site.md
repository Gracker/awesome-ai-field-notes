# OpenClaw Task: 站点重新生成 (Site)

## 目标
从 entries.json 重新生成 VitePress 站点、README、stats。

## 触发条件
- entries.json 有实质性变更（新增/修改/归档条目）
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
- `site-src/` 目录已更新（index.md + 6 分类页 + entry/ 详情页）
- `site-src/.vitepress/config.ts` 已自动生成
- `npm run build` 已通过，Cloudflare Pages 使用同一条生成 + VitePress 构建链路
- `README.md` 统计摘要已更新
- `metadata/stats.json` 已更新

## 提交
```bash
git add -A
git commit -m "[openclaw] site: regenerate from entries.json"
git push origin main
```
