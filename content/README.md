# Content Directory

存放文章全文内容，每篇文章一个 `.md` 文件，文件名为 entry ID。

## 文件格式

中文文章：
```markdown
正文段落1...

正文段落2...
```

英文文章（双语）：
```markdown
## English

Original paragraph 1...

## 中文

翻译段落1...
```

## 自动生成

由 AAIF Content Fetcher cron 任务自动抓取和翻译，无需手动维护。
