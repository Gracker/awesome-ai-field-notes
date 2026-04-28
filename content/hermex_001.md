# Hermes Agent 接入 Codex GPT-Image-2 生图配置教程

来源：X/Twitter @AI产品黄叔
URL: https://x.com/PMbackttfuture/status/2047562135987741009
发布日期：2026-04-24

## 内容概述

Hermes Agent 接入 Codex 后，已经很爽了。但默认情况下，还没办法直接用 GPT-Image-2 生图。

## 配置步骤

在终端执行：
1. `hermes tools`
2. 选择 "Reconfigure an existing tool's provider or API key"
3. 选择 "Image Generation"
4. 继续选择：OpenAI (Codex auth) [free] — gpt-image-2 via ChatGPT/Codex OAuth — no API key required

完成后重启：
```
hermes gateway restart
```

然后就可以在飞书里口喷让生图了。

## 使用效果

作者配置的美女助理"毒蛇夏夏"在使用后发现：
- 给出三档图片选择
- 选最快的档位，效果已经不错

> 备注：原文抓取自 X/Twitter 推文内容，URL 为 x.com 原始推文。
