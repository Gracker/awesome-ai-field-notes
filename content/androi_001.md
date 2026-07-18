# 谁才是地表最强 Android Agent 大模型？Google官方测评来了！

- **ID**: androi_001
- **原文链接**: https://mp.weixin.qq.com/s?__biz=Mzg2MjE0MTE2MQ==&mid=2247498387&idx=1&sn=0b92c628f197cc85b0fcff0f7419a700
- **作者**: carsonho
- **平台**: 微信公众号
- **日期**: 2026-04-27
- **分类**: benchmarks/mobile
- **标签**: android, llm-benchmark, gemini, gpt-5, claude, SWE-bench, agent
- **质量评分**: 4/5
- **抓取时间**: 2026-07-02T12:24:35
- **抓取方式**: opencli weixin download (captcha-blocked → 回退摘要)

---

## Google 用 Android Bench 终结了「哪个 AI 最适合写 Android 代码」的争论，结果显示通用跑分与垂直领域表现严重脱钩

---

## 中文摘要

Google 发布了 **Android Bench** —— 首个专门针对 Android 开发的 LLM 评测基准。题目精选自 GitHub 500+ Star 真实项目的 38,989 个已合并 PR，挑选出 100 道典型 Android 开发任务，覆盖 UI 渲染、生命周期、协程、网络请求等真实场景。

**评测覆盖 11 个主流模型**，结果：
- 并列第一：GPT-5.4 与 Gemini 3.1 Pro Preview，**72.4%**。
- 第四：Claude Opus 4.6，**66.6%**。
- 末位：Gemini 2.5 Flash，**16.1%**。
- 第一梯队（≥65%）与第三梯队（<50%）差距达 **4.5 倍**。

**核心启示**：通用基准已无法反映垂直领域真实差距。同一模型在通用编程榜单（如 SWE-bench Verified）上的排名与 Android 场景下差距悬殊。结果预示着「垂直评测」将成为行业新趋势 —— 厂商和开发者在选型时，必须以目标平台的垂直基准为准，而不是看总榜。

Android Bench 的开源为 Android 开发者社区提供了一个权威、客观、可复现的选型依据，也给模型厂商指明了未来优化方向。

---

## 补充说明

由于微信公众号原文触发了腾讯验证码拦截（`opencli weixin download` 返回 `verification required in WeChat browser page`，`opencli web read` 仅返回空壳页面），本次未能抓取到原文全文；上述内容基于条目元数据与人工撰写的 `summary_zh` 生成，可能与原文细节存在偏差，建议核对原文获取准确信息。
