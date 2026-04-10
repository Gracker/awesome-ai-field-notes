# OpenClaw Task: 站点重新生成 (Site)

## 目标
从 entries.json 重新生成 mdbook 站点和 README。

## 触发条件
- entries.json 有实质性变更（新增/修改/归档条目）
- 每周维护完成后

## 执行流程

```bash
cd /tmp/awesome-ai-field-notes
python3 scripts/generate-site.py
```

## 验证
- `site-src/` 目录已更新
- `README.md` 统计摘要已更新
- `metadata/stats.json` 已更新

## 提交
```bash
git add -A
git commit -m "[openclaw] site: regenerate from entries.json"
git push
```
