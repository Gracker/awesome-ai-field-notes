# Trace 即 Evals：Agent 迭代的量化闭环

- **ID**: `7afdd3e3`
- **Author**: Bohu (@BohuTANG)
- **Source URL**: https://x.com/BohuTANG/status/2064540808951574947
- **Original Date**: Wed Jun 10 02:51:00 +0000 2026
- **Category**: agents
- **Quality Score**: 4/5
- **Fetched**: 2026-07-08T04:25:15
- **Engagement**: 110 likes / 19 RTs / 8 replies / 130 bookmarks / 19179 views

---

## 中文

> Source: <https://x.com/BohuTANG/status/2064540808951574947>

上周六分享了「Trace 即 Evals」，聊了一个问题：Agent 改了 prompt、换了模型、加了 tool，到底变好还是变差？
几个关键点：
- Agent 是链式反应，一步偏了后面全偏，只看 pass/fail 没用
- 同任务同模型，换 harness，token 消耗差 3 倍，成本差 67%
- 轨迹存下来才有归因的可能——哪一步选错 tool、哪一步上下文炸了，展开就能看到
- Anthropic、OpenAI这种头部模型公司迭代 agent 靠的就是 trace 驱动的量化闭环，这套方法不该只有大厂能用

Slides 👉 https://bohutang.me/talks/2026-trace-is-evals/

Slides: <https://bohutang.me/talks/2026-trace-is-evals/>

---

## English Summary

Bohu shared a talk titled "Trace 即 Evals" addressing how to evaluate agent improvements when prompts, models, or tools change. Key takeaways:

- **Agent 评估不能只看 pass/fail**：链式反应里一步偏了，后面全偏；只看 pass/fail 无法定位。
- **同任务同模型，换 harness 成本差 67%**：token 消耗可差 3 倍，harness 选型是隐藏的大成本杠杆。
- **轨迹（trace）是归因的基础设施**：把每一步选了什么 tool、上下文为什么炸了都落库，才能事后展开定位。
- **trace 驱动的量化闭环不只是大厂专利**：Anthropic、OpenAI 头部迭代 agent 的方法学，应当被中小团队也用上。

Slides: <https://bohutang.me/talks/2026-trace-is-evals/>

---

*Entry ID: 7afdd3e3*
*抓取时间: 2026-07-08T04:25:15*
