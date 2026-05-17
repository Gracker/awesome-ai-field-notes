---
id: "7454790739105417566"
cubox_url: https://cubox.pro/web/card/7454790739105417566
url: https://mp.weixin.qq.com/s?__biz=MzAwNjQwNzU2NQ==&mid=2650409319&idx=1&sn=0301eb71a592e20188e071a238fcd9c8&chksm=8222999a5eed208711b2f5f89f707b69653c30e6dadc5929c334d76f8672c88c03ac3fcfe438&mpshare=1&scene=1&srcid=0514ulWLE9O3RgtiREdgDCdf&sharer_shareinfo=96d35eb8fefd8c4ed08965ad419983bc&sharer_shareinfo_first=39bf1e0b908ed7068fd4c924be1dce38
tags: []

---
# Agent Memory 架构解析：过去的信息，凭什么影响未来？

Agent Memory 麻烦的地方，是过去的信息到底以什么方式影响未来。

[Read in Cubox](https://cubox.pro/web/card/7454790739105417566)  
[Read Original](https://mp.weixin.qq.com/s?__biz=MzAwNjQwNzU2NQ==&mid=2650409319&idx=1&sn=0301eb71a592e20188e071a238fcd9c8&chksm=8222999a5eed208711b2f5f89f707b69653c30e6dadc5929c334d76f8672c88c03ac3fcfe438&mpshare=1&scene=1&srcid=0514ulWLE9O3RgtiREdgDCdf&sharer_shareinfo=96d35eb8fefd8c4ed08965ad419983bc&sharer_shareinfo_first=39bf1e0b908ed7068fd4c924be1dce38)  

---

架构师（JiaGouX）

我们都是架构师！  
架构未来，你来不来？

![](https://image.cubox.pro/cardImg/2e5qapdplhtb36pkfe4nw7io8tvhaapel2p4rpys2d7i53470r?imageMogr2/quality/90/ignore-error/1)

**架构师**

专业架构师，专注高质量架构干货分享。三高架构（高可用、高性能、高稳定）、大数据、机器学习、Java架构、系统架构、分布式架构、人工智能等的架构讨论交流，以及结合互联网技术的架构调整，大规模架构实战分享。欢迎有想法、乐于分享的架构师交流学习。

130篇原创内容

<br />

公众号  

，

*** ** * ** ***

最近几篇，我们一直在绕着同一件事往下看。

先是 [Cursor 的 Harness 复盘](https://mp.weixin.qq.com/s?__biz=MzAwNjQwNzU2NQ==&mid=2650409236&idx=1&sn=71ae43ca6ec5b3cb1f82c258b1542271&scene=21#wechat_redirect)，让我印象比较深的一点是：Agent 真进了生产，一次回答有多聪明只是表层，后面还要看能不能评估、能不能观测、出问题能不能回滚、迭代时能不能持续调优。

然后是[上下文操作权](https://mp.weixin.qq.com/s?__biz=MzAwNjQwNzU2NQ==&mid=2650409293&idx=1&sn=28327b5f4426c9f2060dfda8a19161c4&scene=21#wechat_redirect)。从 Claude Code 的 agentic search，到上下文窗口、工具输出、子代理隔离，问题慢慢变成：哪些信息进当前工作集，哪些留在窗口外，什么时候再取回来。

再往后看[长周期 Agent](https://mp.weixin.qq.com/s?__biz=MzAwNjQwNzU2NQ==&mid=2650409301&idx=1&sn=11fd501a836542bcccc7b4fec03fb43e&scene=21#wechat_redirect)，又多了一层：一个任务跑了几个小时，跨了几个上下文窗口，最后留下来的"现场"，能不能让下一个 Agent、下一个模型、甚至下一个人接着干。

这条线顺下去，绕不开 Memory。

更早一点写 Clawdbot 内存架构《[记住不难，想起才难](https://mp.weixin.qq.com/s?__biz=MzAwNjQwNzU2NQ==&mid=2650408224&idx=1&sn=c6b910eefd2f8ffeb845c0a716af1ef3&scene=21#wechat_redirect)》的时候，就已经碰到过这个问题。当时的重点还落在 Markdown 文件、混合检索、压缩前刷新这些抓手上。回头看，那只是第一层。

把 Memory 放进 Agent Harness 之后，我现在更关心另一个问题：

**过去的信息，凭什么继续影响未来？**

这听着有点绕，放到工程现场里就很具体。

一个 Agent 记住用户喜欢 TypeScript，本身是好事。可如果这条偏好来自半年前一个原型项目，今天用户正在维护的是 Python 数据管道，它还死抱着那条记忆不放，就会坏事。

一个 Agent 记住"上次这个方案没成"，也可能有用。但如果上次失败是环境没装好，而不是方案本身有问题，这条记忆每被读出来一次，就会把后面的任务往错路上带一次。

Memory 做不好，很多时候并不会显式报错。

模型还是会答得很顺，只是它已经被旧的、错的、过期的经验牵着走了。

*** ** * ** ***

## 太长不看

*
  • 把 Agent Memory 直接理解成聊天记录、长上下文或对话摘要，都会漏掉最麻烦的一层。
*
  • Session 解决当前会话连续性，Memory 解决跨会话、跨任务、跨时间的可更新经验。
*
  • Profile 可以看成 Memory 的一个消费视图；Policy 属于外部规则，不能让 Memory 随便改写。
*
  • Memory 的主链路可以压成三件事：写入、管理、读取。
*
  • 生产级 Memory 至少要覆盖任务、环境和 Agent 自己的失败经验，用户偏好只是其中一类。
*
  • 写入的动作，是给某些历史分配未来影响力。
*
  • 读取的动作，是把合适的历史转成当前任务的约束。
*
  • 管理环节最容易被低估：冲突、衰减、遗忘、版本、权限、审计，最后都会找上门。
*
  • 对 Coding Agent 来说，最稳的第一步通常是人能读、Agent 能改、系统能审计的工作区文件。
*
  • Memory 一旦可写，就变成持久化攻击面。被提示注入污染的 memory，会在未来会话里继续生效。
*
  • 值得做的 Memory，会让 Agent 在一个具体任务域里少重复犯错，也更能理解约束变化；至于"更懂你"，反而是靠后的一层。

*** ** * ** ***

## 先别急着把 Memory 当数据库

很多团队第一次做 Agent Memory，第一反应是上数据库。

建一张表，存用户偏好、历史对话、任务摘要，再挂一个向量检索。需要的时候搜一下，拼进 prompt，模型就"记得"了。

这个版本能跑，也确实能解决一部分问题。但它很快会撞上几个麻烦。

第一，存进去的不一定都该长期影响未来。

用户今天随口说"先别管测试"，到底是当下赶时间，还是长期偏好？Agent 上次总结"这个接口不稳定"，是事实，还是一次错误环境下的误判？这些东西如果不带来源、作用域和时间，一旦被存成"记忆"，后面就很难再分清。

第二，搜出来的不一定适合当前任务。

用户问"帮我改缓存策略"，语义上最接近的，可能是上次讨论 Redis 的那段对话。可最后会改变设计选择的，也许是三个月前一次大促压测失败记录，或者团队规则里"不允许引入新中间件"的那条约束。相似，不代表适合拿来用。

第三，Memory 会过期。

偏好会变，项目会变，团队规则会变，模型能力也会变。一个不能遗忘的系统，最后会被自己的旧经验拖住。

后来我会把 Agent Memory 看成 Harness 里的一层控制面。只按存储层理解，会漏掉最麻烦的部分。

存储只回答"东西放哪儿"。

Memory 要回答的，至少是这一串：

*
  • 什么值得写入；
*
  • 以什么身份写入；
*
  • 在什么范围内有效；
*
  • 什么时候降低权重；
*
  • 和旧记忆冲突时听谁的；
*
  • 被污染或写错后怎么回滚；
*
  • 用户能不能查看、修改、删除。

这些问题，没一个是数据库本身能回答的。说到底，它们都落在治理上。


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FFnx2G2wYdEKRgUaRiaJWZwKKA1J5TyeDp9icvAAWR8J3mczribn4X9aX7JJMs9tpO0W1rtjn5qPnv5OU07uT7HeH0KDCOtOjiawEHhBPdGXNutg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D0)

Agent Memory 的控制闭环

*Memory 不能只看"存进去"。写入、管理、读取之后，还要能把错误反馈回记忆层。*

*** ** * ** ***

## 先把几个边界切清楚

聊 Memory 之前，得先把几个容易被混在一起的词分开。

**上下文窗口只是当前工作集。**

上下文窗口承担的是 Agent 当前这一轮推理的工作集。当前任务需要哪些文件、工具输出、计划、错误信息，就临时放进去。它的目标，是让这一轮模型调用可解。长期保存全部历史，不该压在这层。

长上下文能提高带宽，但不会自动帮你建模。把过去几十次会话全塞进去，模型面对的就是一堆未经结构化的信号，它既要在里面找信息，又要完成任务，两个负担叠在一起，效果未必比短上下文稳。我们之前聊《[AI 编程的下一场架构迁移](https://mp.weixin.qq.com/s?__biz=MzAwNjQwNzU2NQ==&mid=2650409293&idx=1&sn=28327b5f4426c9f2060dfda8a19161c4&scene=21#wechat_redirect)》时也说过类似意思：上下文的难点不在长度，难在谁来决定哪些东西进、哪些东西留在外面。

**Session 管当前会话。**

Session 管的是当前会话的连续性。对话历史、工具调用、阶段性计划、刚跑完的测试输出，都属于短期状态。它们有时会被提炼进长期记忆，但不能直接等同于长期记忆。

**Profile 是一个消费视图。**

Profile 里可能有名字、角色、语言偏好、常用技术栈。这些当然有用，但它只是一份低维快照。一个 Agent 真要理解你，光记住"你喜欢 Go"还不够。它还得知道这个偏好在哪类项目里成立、什么时候你会为了生态放弃它。

**Policy 要单独放。**

Policy 管的是允许和禁止：权限、安全、合规、预算上限。Memory 可以记录"某条规则在哪儿见过"，也可以提醒当前任务要遵守它，但不能自己去改写规则。

如果 Agent 的记忆能把"禁止访问生产库"悄悄改写成"必要时可以访问"，学习能力再强也没用，系统边界已经先坏了。

我会把 Memory 的边界压成一句话：

**Memory 是跨会话持续存在、可被更新和审计，并且会影响未来决策的结构化历史。**

前半句说"历史"，后半句才是麻烦所在：它会影响未来决策。

*** ** * ** ***

## 记忆不能只围着用户偏好转

"Agent Memory"这个词一出来，很多人下意识会先想到用户偏好。

用户喜欢什么语言、常用什么框架、沟通要详细还是简短、选型保守还是愿意试新东西。

这些当然要记。

但只盯着这一类，Memory 很容易被做成一个加强版用户画像。它能让回答更贴身，未必能让 Agent 更可靠。

放到工程任务里，至少还有三类东西，重要程度不输用户偏好。

一类是任务记忆。

这次需求已经确认了什么、哪些方案被否过、哪个文件是当前真版本、哪些承诺还没完成、哪些测试跑过。之前那篇聊长时间 Agent 时也说过：长任务经常输在这里。Agent 没有忘记用户是谁，却忘了事情已经推进到哪一步。

第二类是环境记忆。

仓库结构、团队规则、API 约束、部署方式、CI 特点、线上事故背景，这些都属于环境。Agent 如果不记环境，每次进项目都像第一次：先猜目录，再猜命令，再猜边界。

第三类是自我记忆。

它上次试过什么、哪个工具在这个仓库里不稳定、哪条推断后来被证明是错的、哪类任务最好先开一个独立的子代理。这些谈不上"人格"，更接近一个工程系统的运行经验。

把这三类和用户偏好放在一起看，Memory 的目标就清楚多了。

这里的目标不在于复制一个人，也不需要给 Agent 做一份花哨履历。

我会把它看成一件更朴素的事：把"用户怎么想、任务到哪了、环境怎么变、我自己哪里容易错"这几条线，整理成未来任务可以使用的约束。

也正因为如此，Memory 的写入不能太随意。

用户偏好、任务状态、环境事实、自我反省，更新机制完全不一样。偏好会漂移、任务会完成、环境会变更、自我反省本身就可能是错的。把它们混在同一个 memory 字段里，后面一定难管。

*** ** * ** ***

## 摘要只能算一步

很多产品最早做 Memory，都是从 summary 开始的。

会话结束时总结一下：用户偏好什么、这次做了什么、下次要注意什么。下次再把摘要拼回去。

这当然有用。

OpenAI Agents SDK 的 memory 文档里也有类似的思路：prior runs 的经验会沉淀到 sandbox workspace 文件里，未来一次 run 先拿到一段短摘要，再按需搜索更详细的 memory 文件和 rollout summaries。

但这里有个边界得说清楚。

摘要只是 memory pipeline 里的一个动作，不能直接等同于 Memory。

摘要的问题在于，它天然偏向留结论。

"用户偏好 TypeScript。"

"上次方案 A 失败。"

"这个项目测试需要 Redis。"

这些话很省 token，也很适合下次快速读取。麻烦在于，结论背后的形成过程被压掉了。

用户偏好 TypeScript，是因为团队规范、个人习惯，还是因为当前项目已经用 React？方案 A 失败，是因为思路不对、实现不完整，还是环境缺依赖？Redis 是所有测试都需要，还是只有集成测试需要？

这些细节在一段短摘要里特别容易掉。

生产级 Agent 更怕的是另一种情况：它记住了结论，却不知道这个结论在什么条件下成立。

Memory 的最小单元，最好别只是一段自然语言摘要。再小也得带上几类元信息：

*
  • 内容：这条记忆到底说了什么；
*
  • 类型：事件、用户声明、Agent 推断、外部约束、未完成承诺；
*
  • 来源：来自用户、工具观察、代码仓库、文档，还是 Agent 自己推断；
*
  • 作用域：项目级、用户级、团队级、当前任务级；
*
  • 置信度：尤其是推断类记忆，不能和用户明确声明混在一起；
*
  • 时间：何时产生，何时被确认，多久没再用过；
*
  • 状态：仍然有效、待确认、已过期、被撤销。

这些字段有一个很具体的用处。

以后出问题时，至少能问得清：到底是哪条旧经验，影响了这次决策。

*** ** * ** ***

## 写入：给过去一张未来通行证

Memory 的第一道关，先看什么值得存。

我会把写入这一步，理解成一次预算分配。

预算不光是存储空间。还包括未来的检索成本、上下文成本、注意力成本、冲突管理成本。更要紧的是：这条信息以后能不能影响决策，影响到什么程度。

看起来有用的信息，也不一定都该写进长期记忆。

比如用户连续三次要"解释详细一点"，这可能值得记一笔。但如果这三次都发生在学习新框架的阶段，就不能泛化成"用户永远喜欢长解释"。更稳的写法是：
> 在学习陌生技术时，用户更愿意先看完整推理和取舍说明。

加上作用域，意思就清楚多了。

再比如 Agent 调试时发现某个命令失败，也不该直接写成"这个命令不可用"。它可能只是当前机器没装依赖，或者路径配错了。更合适的是把它当作一次观察来记录：
> 今天在当前工作区跑 X 失败，错误是 Y。原因未确认。

这条信息以后可以帮排查，但还够不上全局规则。

写入链路最容易犯的错，是把假设写成事实。

这件事在[长周期 Agent](https://mp.weixin.qq.com/s?__biz=MzAwNjQwNzU2NQ==&mid=2650409301&idx=1&sn=11fd501a836542bcccc7b4fec03fb43e&scene=21#wechat_redirect) 里尤其危险。一个 Agent 误判"继续优化已经没有意义"，写进 progress log；下一个 Agent 启动后读到这一句，很可能把它当成前人已经验证过的事实。再跑几轮，错误假设就长成了团队共识。

我自己会给 memory write 立几条比较朴素的小规矩：

*
  • 用户明确说过的话，按 assertion 存；
*
  • 工具和环境观察到的结果，按 event 或 observation 存；
*
  • Agent 自己归纳出来的，只能按 belief 存；
*
  • 未验证原因必须保留"未确认"状态；
*
  • 涉及权限、安全、预算的内容，只能引用 policy，memory 自己不能生成 policy；
*
  • 任何标榜"长期有效"的偏好，都得带 scope。

规则看着不性感，但能挡住很多后患。

*** ** * ** ***

## 读取：先找约束，再找材料

传统 RAG 的读取方式，很容易让人以为 Memory 就等于 retrieve(query)。

用户问个问题，系统拿这句话去搜相似内容，取 top-k，塞进上下文。

放在知识问答里，这条路够用。但放在 Agent Memory 里，常常不够。

因为该影响当前任务的那段历史，未必和用户当前的问题长得像。

用户一句"帮我重构一下支付模块"，相似度最高的记忆可能是上次也在聊支付模块。但这次怎么做，可能要先看这些约束：

*
  • 团队之前明确说过不能改数据库表；
*
  • 上次事故和退款幂等有关；
*
  • 用户偏好先加测试再重构；
*
  • 当前仓库里支付模块由另一个团队维护；
*
  • 这个项目的 CI 对慢测试很敏感。

这些记忆的表面语义可能离"重构支付模块"很远，但它们才是决定动作的人。

读取这一步，别只从 query 出发，也要从任务上下文出发。

先弄清当前任务受什么约束，再去找对应的记忆。

这和之前那篇《[AI 编程的下一场架构迁移](https://mp.weixin.qq.com/s?__biz=MzAwNjQwNzU2NQ==&mid=2650409293&idx=1&sn=28327b5f4426c9f2060dfda8a19161c4&scene=21#wechat_redirect)》里说的是同一条主线：Agent 已经开始在运行循环里判断当下需要什么上下文。Memory 的 read path，也该沿着这个方向设计。

OpenAI 文档里的 progressive disclosure 就是一个比较顺手的方向：先给一小段 memory summary，让 Agent 知道大概有哪些历史；跟当前任务相关，再搜索 memory index；确实需要细节，再打开对应的 rollout summary。

这比一上来把历史全塞进去，稳很多。

Anthropic 的 managed agents memory 也值得看一下。它把 memory store 直接挂载成 session 容器里的一个目录，Agent 用标准文件工具读写。这个设计没把 memory 做成神秘黑箱，反而让它回到工程师最熟悉的那套东西：路径、权限、版本、审计。

这两家的做法放在一起看，方向其实很接近：

**Memory 越往生产走，越像一份可逐步展开、可被工具操作、可被人审查的工作区资产。向量库接口只是其中一个入口。**

*** ** * ** ***

## 管理：最容易被低估，也最决定长期质量

写入和读取都比较容易被看见。

最容易被低估的，是中间的 manage 环节。

写进去只是开始。Memory 会冲突，会过期，会被错误总结污染，也会被提示注入攻击。

先说冲突。

用户去年说"我不喜欢 ORM"，今年在新项目里要求用 Prisma。简单写成"以最新为准"，其实会丢掉很多信息。更稳的处理方式，是把上下文差异保留下来：也许他在老系统里讨厌 ORM，是因为历史包袱太重；在新项目里愿意用，是因为团队需要更快出原型。

Memory 系统如果只留一条"用户喜欢 / 不喜欢 ORM"，就太粗了。

再说衰减。

很多偏好都有半衰期。用户上个月赶 deadline 时说"少解释，直接给代码"，不等于他长期就不想看解释。项目早期允许破坏性调整，也不代表上线后还能随便改接口。

遗忘也该被当成能力来设计。

MemoryAgentBench 这类 benchmark 已经把 selective forgetting 当成一项能力来考。LongMemEval 也把 knowledge updates 和 abstention 放进长期记忆评估里。这和工程直觉是一致的：系统不能只会想起，还得知道旧信息什么时候不该再用，什么时候该承认自己不知道。

最后是安全。

Anthropic managed agents memory 文档里有句提醒很值得单独拎出来：如果 agent 处理的是不可信输入，而 memory store 又是可写的，提示注入完全可能把恶意内容写进 memory。后面的 session 再读出来，就会被当成可信历史用。

这比普通的 prompt injection 更麻烦。

普通注入大多只污染当前会话。Memory 注入会跨会话留下来。

Memory 一旦可写，就要按持久化数据和执行上下文来对待：

*
  • read-only 和 read-write store 要分开；
*
  • 共享资料库默认只读；
*
  • 用户级、项目级、团队级 memory 分开生命周期；
*
  • 每次写入要有版本；
*
  • 关键 memory 要能人工 review；
*
  • 用户能查看、修改、删除；
*
  • 被撤销的 memory 不能继续进入默认读取链路；
*
  • 处理网页、邮件、第三方文档这类不可信输入时，默认不要让它直接写长期记忆。

这已经是系统边界问题。

*** ** * ** ***

## 几条路线，不必急着站队

把外面几个系统放一起看，会发现 Memory 没有一条银弹路线。

Letta 的思路很典型：把 memory 分成上下文里的 core memory 和窗口外的 archival memory。core memory 是小而重要、始终可见的块；archival memory 放大量历史，需要时再查。重点放在管理上：什么该常驻，什么该外置。

Mem0 走的是另一条产品化路线。它强调一层可接入的长期记忆，最近又引入 Memory Decay：旧记忆不会被删除，但搜索时会按新鲜度做软降权。动作不大，却点出一个很现实的问题：记忆越多，旧信息越容易和当前任务抢注意力。衰减这一步，是在给"现在"一点优先级。

Zep / Graphiti 更偏图结构。它把对话和业务数据整理成时间感更强的知识图谱，保留实体、关系和事件。它擅长回答"谁和谁在什么时候发生了什么关系"这一类问题，尤其是企业场景里的客户、项目、合同、组织关系。

再看我们之前写过的 Clawdbot，路线就朴素得多：Markdown 文件、每日记忆、MEMORY.md、混合检索、压缩前刷新。它不华丽，但人能看、能改、能备份、能用 git 管。

这些路线看着差异很大，背后绕的都是同一组取舍：


路线

强项

容易踩的坑

core memory

稳定、低延迟、每轮都可见

太大就污染上下文

archival memory / vector store

容量大、接入快、适合语义召回

旧事实、近义误召回和来源不清

temporal graph

擅长关系、时间和演化

成本、抽取质量和图维护复杂

file-based memory

可读、可审计、可版本化

关系查询和自动整理能力弱

self-managed memory

能随模型能力一起进步

弱模型会把记忆管坏

这里不用急着给"哪种 Memory 架构最好"下结论。

更接近工程现实的说法是：先看你的 Agent 到底要记什么。

只是项目规则，文件就够了。

是用户偏好，结构化 key-value 加版本可能更稳。

是客服、销售、医疗、法务这种长期关系，时间图谱会更有价值。

是 Coding Agent 的长任务现场，GOAL.md、PROGRESS.md、DECISIONS.md 这类工作区文件，往往比一上来接一个复杂记忆平台更有用。

架构设计别从工具清单开始。

它是从信息的生命周期开始的。

*** ** * ** ***

## 放到 Coding Agent，该怎么落地

如果是做 Coding Agent，我不太建议一上来就搭一个很重的"长期记忆平台"。

更稳的做法，是先把 memory 分成几层。

第一层是当前工作集。

这部分在上下文窗口里，服务的是当前推理。包括正在改的文件、当前计划、刚跑出的错误、下一步动作。它不需要长期保存，只要短期准确。

第二层是工作区文件。

AGENTS.md、CLAUDE.md、GOAL.md、PROGRESS.md、DECISIONS.md、KNOWN_ISSUES.md 这些。它们人能读、Agent 能读、git 能追踪，最适合承载项目规则、当前目标、已确认决策、任务进度、已知坑点。

之前聊长时间 Agent 时也提过：长任务能不能续上，靠的是目标证据、状态证据、决策证据、验证证据。这些东西放进工作区文件，比藏在某段会话摘要里要靠谱得多。前面几次讲 CLAUDE.md、AGENTS.md 和项目规则时，其实也是同一条思路：能进 git、能过 review 的规则，比临时塞进上下文的指令更值得依赖。

第三层是 memory store。

这里放跨 session、跨任务的经验。用户偏好、团队约定、工具稳定性、项目历史、常见失败路径。它需要索引、权限、版本和删除机制。

第四层是事件日志。

工具调用、测试结果、失败原因、用户反馈、回滚记录，都可以进事件日志。事件日志不一定每次都读进上下文，但它是复盘和评估的基础。

这四层别混在一起。


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FFnx2G2wYdEIsFEibU8ttHiabEKYbovXP3MkXtjJLtogJCOLWRv4Q0tFqtWxkBVJibLibgfLARtAIeKedZsOic10jWTHXUx8CBzIaaaIEF62gNHHw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D1)

Coding Agent 的四层记忆落点

我会用一个很土的判断方法：


信息类型

更适合放哪里

当前任务下一步

上下文窗口 / PROGRESS.md

项目长期规则
AGENTS.md
/ CLAUDE.md

已确认架构取舍
DECISIONS.md
/ ADR

用户长期偏好

memory store

某次失败的完整日志

event log / artifact

未验证猜测

progress observation，标记未确认

安全和权限规则

policy 系统，只允许 memory 引用

文件名倒不是重点。

重点是让每类信息有自己的生命周期。

当前工作集可以很快消失；项目规则要能版本化；用户偏好要能被修正；事件日志要可追溯；安全策略不能被 Agent 自己的记忆悄悄改写。

这样做的好处，是系统不会把所有历史都搅成一锅粥。

*** ** * ** ***

## "人能看懂"，是 Memory 的硬指标

Chappy Asel 在 X 上有一条关于 Agent Memory 的长帖，把现在的路线粗分成几类：数据库、图、文件系统、自管理。

这几条路线都值得看。

数据库路线接入快；图路线适合处理实体关系和时间变化；文件系统路线简单、可复制、可审计；自管理路线赌的是模型自己越来越会整理上下文。

读完之后，我倒没有急着判断哪条路线会赢。

更有意思的是，几个系统都在往同一个方向收敛：

*
  • 只靠向量通常不够，还会混合关键词、语义、图关系、文件路径；
*
  • 需要一小层 always-loaded context，让 Agent 知道自己大概知道什么；
*
  • 记忆最好是人能读的，别只存在 embedding 里；
*
  • read-write loop 要能闭上：读完、行动、评估之后，还能把经验写回去。

这几条里，"人能读"特别容易被低估。

因为 Memory 一旦出错，人要能查得动。

Agent 为什么老是选这个库？它从哪儿学到的？这条偏好是谁说的？是不是已经过期？为什么它一直绕开某条方案？用户要求删除之后，系统是不是还在偷偷引用？

如果答案只藏在向量库和隐式权重里，调试会非常痛苦。

这几年我越来越偏爱 plain markdown、git history、versioned memory store 这类朴素设计。它们不一定最性感，但工程上好解释、好审计、好回滚。

Memory 系统早期，别急着追求"像人一样记忆"。

先做到"像工程系统一样能查账"。

*** ** * ** ***

## 最难啃的是共享记忆

单个 Agent 的 Memory 已经够复杂。

到了多 Agent、团队级、组织级，事情会更麻烦。

一个 Agent 写入"方案 A 失败"，另一个 Agent 可能写入"方案 A 在新约束下可行"。一个 reviewer 坚持某条架构规则必须守住，一个 implementer 发现现实代码里全是例外。多个 Agent 同时读写同一份 memory store，冲突一抓一大把。

到这一步，Memory 已经进入组织知识系统的范畴。

需要处理的问题大致包括：

*
  • 谁有权写团队级 memory；
*
  • 哪些 memory 必须 review 之后才能生效；
*
  • 同一事实的不同版本怎么保留；
*
  • 冲突是覆盖、并存，还是按 scope 分流；
*
  • 被删除的个人信息怎么保证不再被召回；
*
  • 不同项目的规则怎么避免互相污染；
*
  • Agent 自己的失败经验能不能进入共享 memory。

这些问题听起来像知识管理，但它们会直接落到 Agent 行为上。

以前团队文档写错，最多是人读错。现在 memory 写错，Agent 会跟着执行错。

差别就在这里。

*** ** * ** ***

## 一个最小可用的 Memory 设计

如果今天让我给一个 Coding Agent 团队提建议，我会先建议它做一个很小的版本。

不必一上来就上全局知识图谱，也不必把所有聊天都向量化。

先把下面几件事做了：

1.
   1. 把长期规则放进可版本化文件

项目规则、命令约定、测试前置条件、代码风格、禁用动作，先落进 AGENTS.md、CLAUDE.md 或类似文件。让它们进 git、过 code review，别只活在某一次会话里。

1.
   2. 把任务状态写成可接管的证据

长任务至少要有目标、非目标、验收标准、进度、决策、验证记录。别只靠聊天续命。

1.
   3. 给 memory 加类型和作用域

至少区分用户声明、环境观察、Agent 推断、团队规则引用、未完成承诺。每条都带 scope，别默认全局有效。

1.
   4. 默认让共享 memory 只读

处理外部网页、邮件、issue、第三方文档这一类时，别让 Agent 随手写长期记忆。需要写入的，先写到草稿或待确认区。

1.
   5. 让用户和维护者能看见

Memory 要能浏览、搜索、编辑、删除。关键写入要能追溯来源。

1.
   6. 把错误反馈回 memory 层

如果 Agent 因为某条旧记忆做错了，别只改这一次回答。要回到 memory 层去标记：这条记忆过期了、作用域错了，或者来源不可靠。

1.
   7. 评估别只看 recall

除了"能不能想起"，还要测能不能更新、能不能拒答、能不能忘掉、能不能处理偏好漂移。

这套东西看起来不像"智能体黑科技"。

但它更接近一个生产系统该有的样子。

*** ** * ** ***

## 写在最后

以前聊 Agent，我们常常从一个公式起步：

模型、工具、规划、记忆、循环。

这个说法有用，但现在看下来，已经不够细了。

因为这几个词每往下拆一层，都是一套系统。

工具往下拆，会牵出权限、错误分类、重试和审计。

规划往下拆，要说明目标、约束、验收和回滚。

记忆往下拆，就会碰到这个问题：哪些过去可以继续进入未来。

这大概就是我越来越觉得 Memory 值得单独拆出来聊的原因。

它表面上在解决"Agent 忘了我是谁"。真进了生产，它解决的是另一件事：系统怎么把经验沉淀下来，又不被旧经验绑架。

能记住，当然重要。

但更要紧的是，记住之后还能修正、能遗忘、能追责。

做不到这一点，Memory 越强，Agent 可能越固执。

最后想收在一个很朴素的判断上：

**Agent Memory 麻烦的地方，是过去的信息到底以什么方式影响未来。**

把这件事想清楚，再去聊数据库、图谱、向量、文件、self-management，顺序会更稳一点。

*** ** * ** ***

## 参考来源

*
  • Memory for Autonomous LLM Agents: Mechanisms, Evaluation, and Emerging Frontiers：https://arxiv.org/abs/2603.07670
*
  • What Happens Inside Agent Memory? Circuit Analysis from Emergence to Diagnosis：https://arxiv.org/abs/2605.03354
*
  • LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory：https://arxiv.org/abs/2410.10813
*
  • Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions：https://arxiv.org/abs/2507.05257
*
  • OpenAI Agents SDK: Agent memory：https://openai.github.io/openai-agents-js/guides/sandbox-agents/memory/
*
  • Anthropic Managed Agents: Using agent memory：https://platform.claude.com/docs/en/managed-agents/memory
*
  • Claude Code: How Claude remembers your project：https://code.claude.com/docs/en/memory
*
  • Letta: Introduction to Stateful Agents：https://docs.letta.com/guides/core-concepts/stateful-agents
*
  • Letta: Archival memory：https://docs.letta.com/guides/ade/archival-memory
*
  • Mem0: Introducing Memory Decay：https://mem0.ai/blog/introducing-memory-decay-in-mem0
*
  • Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory：https://arxiv.org/abs/2504.19413
*
  • Zep: Understanding the Graph：https://help.getzep.com/v2/understanding-the-graph
*
  • Zep: A Temporal Knowledge Graph Architecture for Agent Memory：https://arxiv.org/abs/2501.13956
*
  • LoCoMo：https://github.com/snap-research/locomo
*
  • Chappy Asel: Agent Memory, Nine Frameworks, Four Bets：https://x.com/chappyasel/status/2041527719700369756

如喜欢本文，请点击右上角，把文章分享到朋友圈

如有想了解学习的技术点，请留言给若飞安排分享

**因公众号更改推送规则，请点"在看"并加"星标"第一时间获取精彩技术分享**

**·END·**

```
**相关阅读：**
 
 
* https://mp.weixin.qq.com/s?__biz=MzAwNjQwNzU2NQ==&mid=2650408930&idx=1&sn=2fd7f3701ae8688e7720f80bb8296936&scene=21#wechat_redirect


 
* https://mp.weixin.qq.com/s?__biz=MzAwNjQwNzU2NQ==&mid=2650408900&idx=1&sn=93bbae7c90fc03fb510f450c6fee97e0&scene=21#wechat_redirect


 
* https://mp.weixin.qq.com/s?__biz=MzAwNjQwNzU2NQ==&mid=2650408891&idx=1&sn=639dc4a7c8482f6e1ac04d8d53c63459&scene=21#wechat_redirect


 
 

<!-- -->

 
* https://mp.weixin.qq.com/s?__biz=MzAwNjQwNzU2NQ==&mid=2650408877&idx=1&sn=d27eb9e99ed526e342df775f0291cb2e&scene=21#wechat_redirect


 
* https://mp.weixin.qq.com/s?__biz=MzAwNjQwNzU2NQ==&mid=2650408884&idx=1&sn=6a2fa56f70f15cdd75eb5c2b12e687ef&scene=21#wechat_redirect


 
* https://mp.weixin.qq.com/s?__biz=MzAwNjQwNzU2NQ==&mid=2650408870&idx=1&sn=ba53595a44ab55396b36795fbc78791b&scene=21#wechat_redirect


 
* https://mp.weixin.qq.com/s?__biz=MzAwNjQwNzU2NQ==&mid=2650408860&idx=1&sn=b882b2ee97e3f798fea96e68d27c7071&scene=21#wechat_redirect


 
* https://mp.weixin.qq.com/s?__biz=MzAwNjQwNzU2NQ==&mid=2650408848&idx=1&sn=aabf785116e9849dbd301a4f7c477181&scene=21#wechat_redirect


 
* https://mp.weixin.qq.com/s?__biz=MzAwNjQwNzU2NQ==&mid=2650408832&idx=1&sn=ef00408738c853ea2e94be58c0612e51&scene=21#wechat_redirect


 
* https://mp.weixin.qq.com/s?__biz=MzAwNjQwNzU2NQ==&mid=2650408200&idx=1&sn=2f2cce7dfcbdb0766eac3590f777a17b&scene=21#wechat_redirect


 
* https://mp.weixin.qq.com/s?__biz=MzAwNjQwNzU2NQ==&mid=2650408189&idx=1&sn=7d4f7a442a22af37f95c46ff1048a3df&scene=21#wechat_redirect


 
*  
   https://mp.weixin.qq.com/s?__biz=MzAwNjQwNzU2NQ==&mid=2650408183&idx=1&sn=0b6f1437465d3a61118db688cc889b17&scene=21#wechat_redirect 

 
*  
   https://mp.weixin.qq.com/s?__biz=MzAwNjQwNzU2NQ==&mid=2650408169&idx=1&sn=7bba1377a31ffa0ce68932935c8d923a&scene=21#wechat_redirect 

 
*  
   https://mp.weixin.qq.com/s?__biz=MzAwNjQwNzU2NQ==&mid=2650408161&idx=1&sn=85aaff6f2f779e53b6ae9c5e1f003269&scene=21#wechat_redirect 

 
*  
   https://mp.weixin.qq.com/s?__biz=MzAwNjQwNzU2NQ==&mid=2650408141&idx=1&sn=e1e64ad73d25414957aa5206ca969fc3&scene=21#wechat_redirect 

 
*  
   https://mp.weixin.qq.com/s?__biz=MzAwNjQwNzU2NQ==&mid=2650408153&idx=1&sn=d33b48464de93a2573a0a0cb025ada9e&scene=21#wechat_redirect 

 
*  
   https://mp.weixin.qq.com/s?__biz=MzAwNjQwNzU2NQ==&mid=2650408128&idx=1&sn=1b6c640de61986d1364847bffb2cd28f&scene=21#wechat_redirect 

 
*  
   https://mp.weixin.qq.com/s?__biz=MzAwNjQwNzU2NQ==&mid=2650408114&idx=1&sn=29a754281cd07c16b6191c6d146c5837&scene=21#wechat_redirect 

 
*  
   https://mp.weixin.qq.com/s?__biz=MzAwNjQwNzU2NQ==&mid=2650408107&idx=1&sn=905552d68f5b174fd9548360bdea4448&scene=21#wechat_redirect 

 
*  
   https://mp.weixin.qq.com/s?__biz=MzAwNjQwNzU2NQ==&mid=2650408084&idx=1&sn=82f274ba084f9c289e2d141aad0c088b&scene=21#wechat_redirect 

 
*  
   https://mp.weixin.qq.com/s?__biz=MzAwNjQwNzU2NQ==&mid=2650408076&idx=1&sn=f139e90d699b528e80e79c558eed42ee&scene=21#wechat_redirect 

 
*  
   https://mp.weixin.qq.com/s?__biz=MzAwNjQwNzU2NQ==&mid=2650408028&idx=1&sn=3a8571a9fa0bd5d7e59cd66fc6187b3e&scene=21#wechat_redirect 

 
 

<!-- -->

 
```


> 版权申明：内容来源网络，仅供学习研究，版权归原创者所有。如有侵权烦请告知，我们会立即删除并表示歉意。谢谢!


**架构师**

我们都是架构师！

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz%2FsXiaukvjR0RB58TtkIHwhn4lpsqLnZgian9d5tr1BibP7XpibGTFFib1nq9YuYq209XZUEfCOqMzepDOBbN9KD9wMSg%2F640%3Fwx_fmt%3Djpeg%26wxfrom%3D5%26wx_lazy%3D1%26tp%3Dwebp%23imgIndex%3D2)


****关注** 架构师(JiaGouX)，添加"星标"**

**获取每天 AI 技术干货，一起成为牛逼架构师**

**AI/Agent群请** **加若飞：** **1321113940** **进群**

投稿、合作、版权等邮箱：**admin@137x.com**



