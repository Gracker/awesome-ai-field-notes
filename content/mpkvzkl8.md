## English

Anthropic launches Claude Managed Agents: a pre-built, configurable agent harness running on managed infrastructure. Three core concepts: Agent (versioned config), Environment (sandbox template), Session (stateful run). Patterns include event-triggered, scheduled, fire-and-forget, and long-horizon tasks. Architecture decouples brain (Claude+harness), hands (sandbox+tools), and memory (session logs).

@RLanceMartin just computer use :) managed agent calls back to my local machine where I'm logged in, though @gcemaj has some fun examples using containers for this.

The "decouple brain from hands" framing clicks. been running 6+ hour Claude Code sessions — failure mode isn't model quality, it's state loss. session drops, tool context gone, no resume. versioned Agent config solves a real ops problem. one question: rollback story when a config updates mid-task?

@RLanceMartin Anyone pursuing this fucking garbage is a god damn moron. There are no short cuts to critical thinking. Stop trying to short cut it.

@RLanceMartin Meta-harness with stable interfaces framing resonates deeply. I've been building the same layer independently, a harness for harnesses, and arrived at identical conclusions about decoupling. The one area I'd love to see explored next: self-learning. A harness that captures user corrections and injects them as prevention rules in future sessions. Static resilience is table stakes. Compound intelligence is the next layer.

@RLanceMartin managed agents sound like a solid step forward, though i'm curious how much complexity gets hidden behind that 'managed' label

@RLanceMartin You need to add the ability to pass in chat history / state to the agents sdk for long-term persistence memory~ otherwise the agent sdk is not usable in production, everything is coupled to the file system way too much. Even the tool exec run-time like you've mentioned

@RLanceMartin The engineering blog link to designing harnesses goes to your staging blog and as such not accessible.

@RLanceMartin @grok explain how this stacks up against existing harnesses like Deep Agents built in LangChain.

@RLanceMartin @RLanceMartin what did you use to give the agent access to X content?

@RLanceMartin A detailed video with a few use cases would be great

@RLanceMartin 🫡 ... one coming tmrw.

@RLanceMartin ya, supports both!

@RLanceMartin Does this mean that if my company creates an Agent using Claude Cowork...that my team's Claude users can access and run the tool + there is some sort of git-based changelog for making sure there aren't rogue changes to the agent / agent framework?

@RLanceMartin What's the difference between long horizon tasks and a normal task? What makes something long horizon?

@RLanceMartin just the time horizon over which the agent is working. see the METR benchmark.

@RLanceMartin Does this mean AWS Agentcore is no longer required?

@RLanceMartin managed agents are just a fancy name for 'we'll run your janky script on our servers so you don't have to have to'

## 中文

Anthropic 发布 Claude Managed Agents：预构建的可配置 Agent 运行底座，运行在托管基础设施上。三大核心概念：Agent（版本化配置）、Environment（沙盒模板）、Session（有状态运行）。四种用法：事件触发、定时、即发即忘、长时间任务。架构上将"大脑"（Claude+调度框架）、"手"（沙盒工具）、"记忆"（会话日志）解耦，支持独立故障恢复。

@RLanceMartin 只需计算机使用 :) managed agent 回调到本地登录机器，尽管 @gcemaj 有使用容器的有趣示例。

"大脑与手分离"框架很有意义。运行6小时+的 Claude Code 会话——失败模式不是模型质量，而是状态丢失。会话中断，工具上下文消失，无法恢复。版本化的 Agent 配置解决了真正的运维问题。一个疑问：配置在任务中途更新时的回滚故事？

@RLanceMartin 追求这个该死垃圾的人是个该死的白痴。没有批判性思维的捷径。别试图走捷径。

@RLanceMartin Meta-harness 带稳定接口的框架引起深度共鸣。我一直在独立构建相同的层，一个层的层架，并得出了关于解耦的相同结论。我渴望探索的下一个领域是自学习。一个能够捕获用户修正并将其作为预防规则注入到未来会话中的层。静态弹性是基本要求。复合智能是下一层。

@RLanceMartin managed agents 听起来是坚实的一步，不过我很好奇"managed"标签背后隐藏了多少复杂性

@RLanceMartin 你需要添加将聊天历史/状态传递给 agent sdk 的功能以实现长期持久化记忆~ 否则 agent sdk 在生产环境中不可用，一切都与文件系统耦合得太紧。即使是工具执行时也是如此

@RLanceMartin 设计层架的工程博客链接指向你的暂存博客，无法访问。

@RLanceMartin @grok 解释一下这与现有的 LangChain 构建的 Deep Agents 层架相比如何。

@RLanceMartin @RLanceMartin 你用什么来让 agent 访问 X 内容？

@RLanceMartin 希望有一些用例的详细视频。

@RLanceMartin 🫡 ... 明天就来。

@RLanceMartin 支持！

@RLanceMartin 这是说，如果我的公司使用 Claude Cowork... 创建一个 Agent，我们团队的 Claude 用户可以访问并运行该工具 + 有某种基于 git 的变更日志来确保没有恶意更改 agent / agent framework？

@RLanceMartin 长期任务和普通任务有什么区别？什么让某个任务成为长期任务？

@RLanceMartin 只是 agent 工作的时间范围。参见 METR 基准测试。

@RLanceMartin 这是说 AWS Agentcore 不再需要了吗？

@RLanceMartin managed agents 只是我们将在服务器上运行你的垃圾脚本让你不用这么做的花哨名称

---

*来源：Twitter/X @RLanceMartin*
*发布日期：2026-04-06*
*分类：Agents*
