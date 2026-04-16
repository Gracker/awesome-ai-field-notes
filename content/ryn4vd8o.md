# Karpathy 最新方法论：把 LLM 当编译器用，知识管理该换个思路了

> 公众号: Vibe编码
> 发布时间: 1970-01-01 08:33:46
> 原文链接: https://mp.weixin.qq.com/s?__biz=Mzk4ODkzOTY3MA==&mid=2247484735&idx=1&sn=6c93e0c324588762e10a99e915a04678

---
2026 年 4 月 3 日，Andrej Karpathy 在 X 上发了一篇长帖 "LLM Knowledge Bases"，同步放出了 GitHub Gist。他说自己最近消耗的 token，大部分已经不是在写代码，而是在整理知识。这篇帖子在技术圈引发了大量讨论，Lex Fridman、Obsidian CEO、DAIR.AI 创始人都在下面跟帖回应。

它解决的问题很真实：我们每个人手里都有一堆散落的文章、论文、笔记，但从来没人把它们真正"编译"过。与其人类用RAG的方式去整理和利用知识，不如让LLM分层理解索引和导航，每个人都可以用自己的方法论和需求建立一套属于自己的LLM知识库。

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/XAlD4zm7VYdQzHy81F0cmRMkvh2f4eHxrgWqUvTzQkI5ulSUeNyBHqZrYAkiabfyibRzudqLLjLqicYr8BcrXZEXXricAYicBIuXpzibGzawA2wibk/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=0)

## Karpathy 说了什么

Karpathy 提出了一个类比：**把 LLM 当成编译器，把你的原始资料当成源代码，把生成的 Wiki 当成可执行文件。**

具体来说，他设计了一个三层目录结构：

-   **raw/**

     存放所有原始素材，论文、文章、代码、数据集，只增不改，作为唯一的事实来源

-   **wiki/**

     是 LLM 的编译产物，结构化的 Markdown 文件，带有交叉引用和反向链接

-   **output/**

     存放查询结果、幻灯片、可视化图表等衍生输出


整个工作流程分四步走：

**摄入（Ingest）**：用 Obsidian Web Clipper 把网页剪藏成 Markdown，论文和代码直接丢进 raw/ 目录。

**编译（Compile）**：LLM 读取原始文档，提取关键概念，为每个概念生成独立的 Wiki 页面，建立 `[[wikilinks]]` 交叉引用，自动维护一个 index.md 做全局目录。这里有个比较巧妙的设计：编译是增量的，每次只处理新增的文档，不需要全量重跑。

**查询（Query）**：直接向 LLM 提问，它沿着 Wiki 的链接结构导航，综合多个页面给出回答。查询结果会自动写回 Wiki，所以每次提问都在给知识库"添砖加瓦"。

**健康检查（Lint）**：借鉴代码 linting 的思路，LLM 定期扫描 Wiki，查找矛盾、补充缺失、发现新的概念连接。

Karpathy 的原话是："维护知识库最繁琐的部分不是阅读或思考，而是簿记工作。"他的方案就是让 LLM 把所有簿记工作接管了。

这个方法在大约 100 篇文章、40 万字的规模下运行得很好，LLM 通过自维护的 index.md 文件就能高效定位信息，不需要向量数据库。

## 知识编译 vs RAG：到底区别在哪

很多人第一反应是：这跟 RAG 有什么不同？区别其实挺大的。

RAG 的工作方式是**查询时实时检索**：用户提问 → 向量搜索找到相关片段 → 拼给 LLM 生成回答。整个过程是临时的，查完就散了。

Karpathy 的方法是**提前编译**：文档进来时就被 LLM 消化、整理、归类，生成结构化的 Wiki 页面。查询时 LLM 面对的是一个已经组织好的知识网络，概念之间的关系通过 backlinks 显式表达。

这里有一个 RAG 的结构性盲点：向量数据库知道两个文本片段语义接近，但它不知道这两段话是互相矛盾的，还是一个已经被新发现推翻了的旧结论。DEV Community 上有人总结得很到位——向量搜索理解"相似性"，但不理解"结构"。

维度

知识编译

RAG

处理时机

提前编译

查询时检索

知识表示

结构化 Markdown + 显式链接

向量嵌入 + 隐式相似度

透明度

每条信息可追溯到具体文件

向量嵌入是黑盒

适用规模

个人/团队级（~40 万字）

企业级（百万级文档）

知识积累

查询结果自动回写

查完即丢

不过要说清楚，这两个方案解决的是不同规模的问题。Karpathy 自己也承认，他的方法在 40 万字规模下表现好，但你要是有百万级文档的企业场景，还是得上 Agentic RAG。2026 年的最佳实践大概是这样：个人研究用知识编译，小团队用长上下文加提示缓存，企业级上 Agentic RAG 加混合检索。

## 社区怎么看

这条帖子引来的讨论质量相当高。

Lex Fridman 说他在用类似的工作流，还做了扩展：让 LLM 生成动态 HTML 页面用来交互式筛选数据，甚至会在跑步前生成一个临时的迷你知识库，跑步时用语音模式跟它聊。这个用法我觉得很有启发性。

DAIR.AI 的 Elvis Saravia 也确认了这个模式的价值，他自己开发了 qmd 工具做语义 Markdown 索引。

创业者 Vamshi Reddy 说了一句很直接的话："Every business has a raw/ directory. Nobody's ever compiled it. That's the product." Karpathy 对此表示认同，说这里面确实有一个"incredible new product"的机会。

但批评声音同样尖锐。

有人提出了**认知完整性**的问题：如果 Wiki 里的重要声明没有绑定来源、置信度和时效性，系统可能会退化成"看着很有说服力但实际上并不靠谱的知识库"。这个担忧很合理，尤其是当 LLM 自己在做编译和 linting 的时候，谁来校验 LLM 的判断？

还有人吐槽实施门槛："It requires you to be Andrej Karpathy to set it up." 目前这套东西是一堆 CLI 工具、自制搜索引擎、Obsidian 插件和大量提示工程的组合，离产品化还有距离。

Obsidian CEO Kepano 的回应很务实。他建议把个人精选的知识库和 AI 生成的内容分开放，用两个独立的 Vault，防止 AI 内容污染你手工整理的高质量笔记。他还开源了 obsidian-skills 项目，教 AI Agent 正确使用 Obsidian 的文件格式。这个**知识库分离原则**我觉得很重要，实际操作中很容易忽略。

## 这事儿跟我们有什么关系

如果你在用 Claude Code、Cursor 或者 GitHub Copilot，你可能已经在做类似的事了。

CLAUDE.md 文件，写在项目根目录下，告诉 Claude 这个项目的背景、约定和规范。Cursor Rules，按需加载的项目级指令。Copilot Instructions，同样的思路。这些东西放在 Karpathy 的架构里看，它们就是 **Schema Layer** 的实现——定义 Wiki 结构和规范的配置层。

MCP（Model Context Protocol）则对应知识库的统一访问接口。你可以把编译好的知识库通过 MCP Server 暴露出去，让任何支持 MCP 的 AI 客户端都能查询。

实际用下来，感觉 Karpathy 描述的这个范式正在以碎片化的方式渗透进我们的日常工具链。我们给 AI 写规则文件、维护项目文档、配置 Agent 的行为，本质上都是在做"知识编译"——把散落的项目知识整理成 LLM 能高效消费的结构化格式。

一个具体的案例：有 VC 团队用这套方法做竞争情报分析，把原来需要两周的尽职调查压缩到了三天。他们把行业报告、公司财报、新闻稿全部丢进 raw/，让 LLM 编译成结构化的竞品 Wiki，然后直接在上面做查询和交叉比对。

## 趋势判断

Karpathy 自己说了："I think there is room here for an incredible new product instead of a hacky collection of scripts." DVC 创始人 Dmitry Petrov 也在 LinkedIn 上说 "LLM knowledge bases are suddenly everywhere"。

我判断接下来会发生几件事：

**知识编译会产品化。** 目前的实现门槛太高，但需求是真实的。2026 到 2027 年大概率会出现专门做这个的创业公司。

**每个 Agent 都会有持久化知识层。** 现在的 Agent 基本是无状态的，对话结束就什么都忘了。知识编译提供了一种让 Agent 拥有长期记忆的方式，而且是结构化的、可审计的记忆。

**Markdown 会继续巩固作为 AI 原生格式的地位。** 人类能读、LLM 能处理、Git 能版控、不绑定任何工具。Karpathy 整套架构的基石就是纯文本 Markdown。

**RAG 不会死，但会分层。** 个人和小团队用知识编译，企业用 Agentic RAG，两者最终可能融合：知识编译做预处理，RAG 做大规模服务。

还有一个有意思的方向：Karpathy 暗示，当 Wiki 经过反复 linting 变得足够干净后，它本身就是一个完美的训练集——可以拿来微调更小的专用模型，把知识从外部文件"内化"到模型权重里。这等于是从知识编译到 fine-tuning 的自然过渡。

## 总结

Karpathy 这篇帖子最打动我的一点是，他精准地说出了个人知识管理的痛点：人类放弃维护 Wiki，是因为维护负担的增长速度永远快于从中获得的价值。LLM 可以接管所有的"簿记"工作，让你只负责选择读什么、问什么问题。

这个方法适合谁？如果你的日常工作涉及大量阅读和信息整合——研究者、分析师、技术写作者、产品经理——它值得一试。从一个具体的研究课题开始，先积累二三十篇文章，让 LLM 帮你编译，体验一下"查询即贡献"的循环。

当然它也有明确的局限：规模天花板、认知完整性风险、实施门槛高。但作为一种思维方式，"编译知识"比"检索知识"这个转变，我认为抓住了一些真实的东西。我们花在整理笔记上的时间，LLM 确实可以替我们干了。