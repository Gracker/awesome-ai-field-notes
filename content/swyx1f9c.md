# 【双语】swyx 洞察：AI 开发工具 Top 1% 和 Bottom 99% 的构建方式完全不同

来源：https://x.com/swyx/status/1932125643384455237

---
## English


Original Tweet by swyx:

the most headfucky thing about building/investing in ai devtools is that the top 1% of ai applications are building compeltely differently than the bottom 99%

both are correct and good and usecase appropriate and the only people who are guaranteed to fail are those who try to bullshit you that you can cleverly engineer around this fact and grow from small to ultralarge with the exact same arch/stack

Top Replies:

- "This is so true. The stack that gets you to your first 100 users is almost never the one that gets you to 10 million."
- "mirrors what we saw in early mobile, top apps (Instagram, Uber) built custom infrastructure while 99% used standard SDKs. trap is that many 'horizontal' AI dev tools are actually targeting the 99% but pricing for the 1%. Smart ones will either go deep on enterprise (like Datadog did) or own the hobbyist→startup funnel (GitHub model)."
- "like trying to build shovels for gold miners, but the only ones finding gold are using lasers, not shovels."
- "build like the 1% when you're in the 99%. the right tool for the job is always the one that ships."
- "can you say more about what the differences are?" → "one example is open model usage. very unnecessary for most, very necessary for top tier"
- "shipping is the only moat"
- "We saw this problem early on, which is why we built Jenova AI with an intelligent model router. Instead of locking you into one provider, it automatically picks the best model for the job from OpenAI, Anthropic, Google, etc."
- "Some concerns become real at scale." 


---

## 中文


原文推文 by swyx：

关于构建/投资 AI 开发工具，最让人头疼的事情是：前 1% 的 AI 应用与后 99% 的构建方式完全不同。

两者都是正确的、好的、适合用例的。唯一注定会失败的人是那些骗你说可以聪明地工程化绕过这一事实、并用完全相同的架构/技术栈从小型发展到超大型的人。

热门回复：

- "确实如此。让你获得第一批 100 个用户的技术栈，几乎从来不是帮你达到 1000 万用户的那一个。"
- "这与早期移动互联网如出一辙，顶级应用（Instagram、Uber）构建了定制基础设施，而后 99% 使用标准 SDK。陷阱在于很多'横向'AI 开发工具实际上针对的是 99% 却按 1% 的价格收费。聪明的做法是要么深耕企业市场（像 Datadog 那样），要么占据 hobbyist→startup 的漏斗（GitHub 模式）。"
- "就像试图为淘金者造铲子，但真正找到黄金的人用的是激光，不是铲子。"
- "在 99% 时用 1% 的方式构建。正确的工具始终是能交付的那个。"
- "能详细说说差异吗？" → "一个例子是开放模型使用。对大多数来说完全没必要，对 top tier 来说非常必要。"
- "交付才是唯一的护城河。"
- "我们早期就看到了这个问题，这就是为什么我们用智能模型路由器构建了 Jenova AI。不是锁定你使用某一个提供商，而是自动从 OpenAI、Anthropic、Google 等中选择最佳模型来完成任务。"
- "有些问题在规模上才会变得真实。" 