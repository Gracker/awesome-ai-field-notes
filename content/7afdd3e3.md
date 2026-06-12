# Trace即Evals：Agent迭代的量化闭环

- **来源**：X/Twitter
- **原文链接**：https://x.com/BohuTANG/status/2064540808951574947
- **作者**：BohuTANG
- **日期**：2026-06-12
- **抓取时间**：2026-06-12 12:38

---

上周六分享了「Trace 即 Evals」，聊了一个问题：Agent 改了 prompt、换了模型、加了 tool，到底变好还是变差？
几个关键点：
- Agent 是链式反应，一步偏了后面全偏，只看 pass/fail 没用
- 同任务同模型，换 harness，token 消耗差 3 倍，成本差 67%
- 轨迹存下来才有归因的可能——哪一步选错 tool、哪一步上下文炸了，展开就能看到
- Anthropic、OpenAI这种头部模型公司迭代 agent 靠的就是 trace 驱动的量化闭环，这套方法不该只有大厂能用

Slides 👉 https://t.co/KIcq8KuVTD
