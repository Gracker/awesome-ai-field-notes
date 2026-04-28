# 浅谈Claude Skills，Github已经5.2k Star了
> 公众号: 刘聪NLP
> 发布时间: 1970-01-01 08:33:45
> 原文链接: https://mp.weixin.qq.com/s?__biz=Mzg5MTU1NTE1OQ==&mid=2247496737&idx=1&sn=9629efe206466651a83311ad13742c58&chksm=ce92906609f4ad8d313e63d9f3a9cfa60bfa76a6c8ede08a0a0a7f10b51d867e62a5e4b3c69a&mpshare=1&scene=1&srcid=1020vw7J0m2UAIZgijWryasu&sharer_shareinfo=9e560ff6c7b0019f73b2284efd091348&sharer_shareinfo_first=9e560ff6c7b0019f73b2284efd091348
---
`https://www.zhihu.com/question/1962512846630941008/answer/1963073531265913943 （已授权） `
说个暴论，AI Agent想要落地，需要的只有强大的模型基座，什么Skill、MCP、...都只是添头，通过代码很容易实现。
Agent的核心驱动力永远是LLM本身。
其他所有东西说白了都是在给这个不那么可靠的大脑搭建脚手架，做工程化的约束。
但比起最近OpenAI开始搞颜色，A社搞搞Skill还是值得肯定的...
## 所以，Claude Skills到底是什么？
一句话说清楚：Skill就是一个标准化的文件夹，用来打包Agent完成特定任务所需的知识和工具。
你可以把它理解成给模型的说明书或标准作业程序（SOP，或者之前比较火的概念：SPEC的增强版）。
Anthropic这次不仅发布了概念，还直接开源了一个GitHub仓库，里面包含了所有20个左右的官方Skill的源码示例。
`https://github.com/anthropics/skills `
这才是最有价值的地方，它把理论落到了代码上：
![A社官方开源的Skill仓库，包含十几个Skill示例](images/img_001.png)
A社官方开源的Skill仓库，包含十几个Skill示例
一个Skill文件夹通常包含这几部分：
SKILL.md ：核心文件，必须存在。里面用YAML写元数据（名字、描述），用Markdown写详细的指令，告诉Claude在什么情况下、以及如何使用这个Skill。
scripts/ ：存放可执行的Python、Shell脚本。比如PDF处理Skill里，就有fill\_fillable\_fields.py这种确定性极强的代码。
references/ ：存放参考文档。比如API文档、数据库Schema、公司政策等，这些是给Claude看的知识库。
assets/ ：存放资源文件。比如PPT模板、公司Logo、React项目脚手架等，这些是Claude在执行任务时直接使用的文件，而不是阅读的。
![Claude Skill 文件夹结构](images/img_002.png)
Claude Skill 文件夹结构
所以说：
一个Skill = 任务说明书 SKILL.md + 工具代码 (scripts) + 专业知识 (references) +素材资源(assets)。
它把完成一个特定任务所需的一切都打包好了，本质上就是一种代码和资源的组织方式，一种约定优于配置的理念。
## 它的精髓：为上下文窗口减负
这部分是ClaudeSkills设计的精髓，也是它和简单RAG/MCP/FunctionCalling的最大区别。它就是一套聪明的，为了节省上下文窗口而设计的分层加载策略。
既然是分层策略，那么有哪几层？
![分层策略](images/img_003.png)
分层策略
第一层：元数据（Name + Description）。这部分信息非常简短，会常驻在Claude的脑海里。当用户提出一个任务时，Claude会快速扫描所有可用Skill的描述，判断哪个可能相关。这是第一道筛选，成本极低。
第二层：SKILL.md。当Claude认为某个Skill相关时，它才会去加载SKILL.md里的详细指令。这部分内容告诉Claude完成任务的具体步骤、应该遵循的规则、以及如何使用文件夹里的其他资源。这步的上下文消耗中等。
第三层：脚本和参考文档。只有当SKILL.md里的指令明确要求，或者Claude在执行中判断需要时，它才会去读取scripts/里的代码或references/里的文档。这步的上下文消耗是按需的，避免了一次性把所有东西都塞进去。
这个机制的好处显而易见，极大地节省了宝贵的上下文窗口 。它先凭经验判断用哪个SOP，然后翻开SOP照着做，遇到具体问题再查阅附录或工具手册。这套逻辑，我们用代码当然也能实现，但Skills把它标准化了。
## 它和MCP是什么关系
MCP是一种通信协议。它定义了Agent（客户端）如何与一个暴露了工具的服务（服务端）进行标准化的交流。它解决的是Agent与外部工具如何对话的问题。
Claude Skills是一种能力封装格式。它定义了Agent自身应该具备哪些知识、工作流和内部工具。它解决的是Agent如何思考和行动的问题。
Skill里的知识可以指导Agent如何更有效地去使用一个遵循MCP协议的工具。一个Agent完全可以加载一个Skill，然后根据Skill里的指令，去调用一个远程的MCP服务器。
![Claude Skills与MCP的关系](images/img_004.png)
Claude Skills与MCP的关系
所以你看，它俩不是替代关系，而是正交的、可以组合的。 MCP负责连接，Skills负责驱动。一个解决通信标准，一个解决能力封装。
## 这套东西，对我们开发者有什么用？
回到开头的观点，既然这玩意儿本质上就是一堆文件夹和代码，我们开发者能从中得到什么？
最大的价值是：Anthropic把他们在生产环境中打磨出的一套Agent能力管理的设计模式开源了 。我们完全可以把这个模式借鉴过来，用在自己的Agent体系里，不管你用的是Qwen、Deepseek，还是别的模型。
![一个不错的设计模式，解耦、模块化的Skills](images/img_005.png)
一个不错的设计模式，解耦、模块化的Skills
当你的Agent能力越来越多时，怎么管理？一个几千行的System Prompt？一个包含几十个工具函数的大杂烩文件？这些都很难维护。
而Skills提供了一种解耦的、模块化的方案 。你团队里的Agent不再是依赖一个巨大的、难以维护的 system\_prompt.txt，而是一个由几十个标准化的Skill文件夹组成的能力库，每个Skill都可以独立版本控制、测试和迭代。
## 举个栗子
比如你可以为你的公司创建一个数据分析工具，起名为：internal-analytics-skill，里面包含：
SKILL.md：指导Agent如何查询公司内部数据仓库。
scripts/generate\_report.py：一个固定的Python脚本，用于生成标准格式的周报。
references/db\_schema.md：数据仓库的Schema文档。
assets/report\_template.docx：周报的Word模板。
当有新的Agent实例加入时，你只需要让它加载这个Skill，它就立刻学会了如何做数据分析，而不需要重新训练或编写复杂的Prompt。
所以说呀，Claude Skills本身不是什么黑科技。它最大的启示还是：AI Agent的未来，一半靠模型，另一半靠工程。
