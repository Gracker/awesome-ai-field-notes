# (Note Tweet)

- **来源**：X/Twitter
- **原文链接**：https://x.com/chenchengpro/status/2042082446871818746
- **作者**：chenchengpro
- **日期**：2026-04-06
- **抓取时间**：2026-04-12 12:06

---

| title | author | content | url |
| --- | --- | --- | --- |
| (Note Tweet) | chenchengpro | Claude Code 有个 5 小时重置机制，意味着你可以通过定时任务来卡重置节点，让每个工作时段都从满血状态开始。

设置只要三步：

1）打开 https://t.co/lfGbFsSmP2
2）选 Custom，输入 5 7,12,17,22 * * *
3）点 Create

这样每天 7:05、12:05、17:05、22:05 会自动触发一次对话，重置 5 小时倒计时。对应的就是上午、下午、傍晚、深夜四个时段，每段都能用满 token 额度。

关键是这个任务跑在云端，本地不用开电脑，比 crontab 优雅。

via @MinLiBuilds | https://x.com/chenchengpro/status/2042082446871818746 |

