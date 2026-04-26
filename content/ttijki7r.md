# MCP协议深度解读：技术创新正以前所未有的速度突破

> 公众号: 腾讯技术工程
> 发布时间: 1970-01-01 08:33:45
> 原文链接: https://mp.weixin.qq.com/s?__biz=MjM5ODYwMjI2MA==&mid=2649792738&idx=1&sn=337f992522daacb8eb68bd61043ac255

---
![Image](images/img_001.gif)

作者：rian

> OpenAI 官宣全面支持MCP协议，至此MCP已得到业界广泛的认可。正逐步成为AI应用架构的基础协议。做为AI应用架构的USB-C,MCP原理是怎样的？对实际业务又有何影响呢？本文以MCP原理解读及业务实践为切入点，探索AI应用架构在业务领域落地的路径。

### 一、技术背景

大模型很长时间面临认知边界和工具使用的双重约束：其知识体系受限于预训练阶段的静态数据沉淀并缺少完成任务的工具。而传统Function Call存在先天性的不足：线性指令执行机制带来的性能瓶颈与异构接口标准带来的兼容性瓶颈。这种局面在 Anthropic 2024.11 发布 Model Context Protocol 后得到改变——该协议重新定义了大语言模型与现实世界的交互范式。

#### **1\. Function Call vs MCP**

Function Call，标杆开源项目是 Langchain Tools，它提供了"All In One"的工具箱，号称大模型的瑞士军刀。

而MCP的设计思路则不同，它遵循微内核架构的设计理念：定义架构和协议标准。号称工具调用的USB-C标准。

![Image](images/img_002.png)

标准发布后开源生态活跃，MCP 官方及三方组件累计已达到4000+

官方MCPServer：[GitHub - modelcontextprotocol/servers: Model Context Protocol Servers](https://github.com/modelcontextprotocol/servers)

基于这一框架，大语言模型突破了原有束缚：动态语义对齐机制将**工具理解准确率提升至新量级**，指令编排引擎则实现了**高并发任务的智能调度**。MCP通过标准化接口的语义映射能力，**将离散的API调用转化为具备上下文感知的协作指令集。**

#### 2\. MCP Timeline

**2024年11 月 24 日**

-   **Anthropic 发布 MCP 协议**人工智能公司 Anthropic 首次提出 **MCP（Model Control Protocol）**，旨在为无法直接修改底层逻辑的 Agent（如 Cursor、Claude 桌面端等）提供工具调用标准。协议允许用户为第三方 Agent 动态接入自定义工具，无需开发者介入。


**2024年12月**

-   Claude + MCP 应用案例涌现 技术社区出现首批基于Claude 3.5 + MCP 的应用案例，例如通过MCP协议实现Claude与本地文件系统、数据库的自动化交互。开发者工具Cursor同期发布MCP适配版本，验证了该协议在多工具协作场景的可行性。


**2025年3月初**

-   MCP生态进入规模化应用阶段 企业级应用：Block、Apollo等企业通过集成MCP实现跨系统数据调度，业务流程响应速度提升数倍；开发者工具：Cline、Windsurf 等工具原生支持MCP协议。


**2025年3月11日**

-   LangChain 官方发布核心辩论文章 LangChain 联合创始人 Harrison Chase 与 LangGraph 负责人 Nuno Campos 围绕 MCP 展开激辩。**40% 参与者支持 MCP 成为未来标准。**（33% 的人表示观望）。


![Image](images/img_003.png)

**2025年3月12日**

-   开源社区复现 Manus 技术方案 开发者社区组织线上分享会，探讨如何基于 MCP 协议复现 Anthropic 的 **Manus 框架**（一种多 Agent 协作系统），进一步推动协议落地应用。


解读：Manus 产品形态上让人眼前一亮。而在 Manus 发布之前，完成特定领域任务的AI Agent 已经投入实际的生产工作（如AI编码工具Cursor、Cline）。Manus 的关键词是 "通用、复杂任务"。

**2025年3月17日**

-   Anthropic推出的MCP协议新传输方案"Streamable HTTP“。

-   该方案彻底重构了通信机制。解决了原HTTP+SSE方案在连接恢复性、服务器负载及双向通信方面的核心瓶颈。


![Image](images/img_004.png)

PR已于3.24合入。

解读：1. 按需建立流式通道：会话初始化阶段仅需常规HTTP请求，当检测到需要持续交互（如工具执行进度反馈）时，服务器自动触发SSE升级机制。2. 无状态运行支持: 服务器无需长期维护连接状态，处理完请求即可释放资源，适合Serverless架构。

**2025年3月27日**

-   OpenAI宣布支持MCP协议。


![Image](images/img_005.png)

#### **3\. MCP Roadmap**

2025H1 MCP官方计划支持以下能力：

1.  **Remote MCP Support:**


OAuth2授权&鉴权能力、服务注册与发现、无状态操作（支持serverless场景）

2.  **Distribution & Discovery:**


Package管理、沙箱环境（通过隔离提升安全性）、MCP Server注册表

3.  **Agent Support:**


分层代理系统：通过命名空间与拓扑感知支持多级代理树结构。

交互式工作流：优化跨代理层级的权限管理、用户信息请求及输出定向（用户而非模型）。

流式结果：支持长任务实时结果推送，提升响应效率。

4.  **Broader Ecosystem:**


开放标准共建：推动社区主导的标准制定，鼓励AI厂商平等参与治理，满足多样化应用需求。多模态支持：拓展音频、视频等非文本格式的兼容性。

这些都是MCP 架构工程化落地很需要的能力。

### 二、初步验证

纸上得来终觉浅，了解到MCP概念后，我使用 Cline（VSCode插件）体验了MCP Server开发、配置和使用的过程。

#### 1\. 开发 MCP Server

这里使用 Claude Sonnet 大模型和MCP模板快速实现了几个MCP Server：openweather：基于openwheather api 查询天气信息。note-sqlite：使用 sqlite 保存、查询笔记。

MCP Server 需要实现大模型友好的接口定义，核心的接口是：

**接口名称**

**功能描述**

`list_tools`

返回工具清单及JSON Schema描述（含权限说明）

`call_tool`

执行工具调用（需参数验证）

`list_resources`

返回可访问资源列表（文件路径/API端点）

`read_resource`

获取指定资源内容（支持分页）

`list_resource_templates`

提供动态资源模板

#### 2\. 配置 MCP Server

将开发好的MCP Server 添加到Cline插件的MCP Server配置文件。

![Image](images/img_006.png)

#### 3\. MCP Host 执行任务

在Cline对话框输入任务："查询并记录天气"。任务执行情况如下：

**3.1. 意图识别与任务分解**

Cline 将用户prompt 和可用工具列表作为入参传递给LLM，LLM执行意图识别与任务分解。

![Image](images/img_007.png)

可以看到，大模型将任务分解为两个主要步骤：

1.  使用openweather 获取深圳天气数据 2. 使用note-sqlite 保存天气数据


在此步骤大模型的输出是：任务执行的工作流（查询天气->保存笔记）及Tool Call参数。

**3.2. 查询天气数据**

Cline 根据大模型返回的工作流及Tool Call参数，调用get\_current\_weather 查询天气信息：

![Image](images/img_008.png)

**3.3. 数据处理与格式化**

Cline 将"查询天气"的结果加入到上下文中传递给大模型，大模型将其转化为调用save\_note工具的参数。

![Image](images/img_009.png)

**3.4. 记录天气数据**

Cline 使用大模型返回的 Tool Call 参数调用save\_note工具保存笔记：

![Image](images/img_010.png)

**3.5. 结果呈现**

Cline 将"保存笔记"的结果加入到上下文传递给大模型，大模型返回任务总结：

![Image](images/img_011.png)

为了验证大模型对**同类工具的选择机制，**我又开发、配置了一个weather-sqlite 服务，专门用于记录天气信息。

![Image](images/img_012.png)

在查询网天气信息后，在note-sqlite和weather-sqlite 都可用的前提下，选择了后者用于保存天气信息。以下是大模型给出的决策理由：

![Image](images/img_013.png)

### 三、原理解析

接下来看一下大模型和MCP工具集是如何协同完成用户特定任务的。

#### 1\. 核心架构

![Image](images/img_014.gif)

**1\. MCP Host** （如Claude Desktop、Cursor IDE、Cline）**可以看做是一个AI Agent**。调用LLM执行意图识别，制定任务计划。然后调用MCP Server 完成任务流中的一个一个子任务。同时负责管理与用户的会话。

**2\. MCP Server 即大模型友好的工具集**。通过类似OAS标准的Schema标注，让大模型能很好地理解工具的功能范围及使用方法。MCP Server需要有安全控制机制，以保障接口/资源不被越权访问。

**3\. MCP Client** **即通信中间件。**MCP Client 是MCP Host 引用的组件，负责与MCP Server 建立连接，并处理 JSON-RPC/SSE 等协议交互。

#### 2\. 交互流程

这里花了一点时间完整地探究了一下Cline 完整地梳理了Cline 处理用户请求的流程。主要涉及两个阶段：

![Image](images/img_015.png)

**初始化阶段：**

MCP Host启动时基于配置与MCP Server 建立连接，获取并缓存工具/资源的元数据描述（如接口定义JSON Schema）。

**任务处理阶段**：

MCP Host调用大模型做意图识别和任务规划。大模型结合用户prompt及上下文信息、可用工具列表动态规划任务流程并适配 Tool Call 参数。该阶段采用ReAct循环机制，当参数不完整或输出结果置信度低于阈值时启动用户协同修正流程。

#### 3\. 技术关键点

这里展开说一些关键技术细节

**3.1 统一语义空间**

MCP Server通过 Schema（类 [OAS3](https://swagger.io/specification/)标准） 明确定义工具的能力范围及接口字段（包含类型、校验规则及自然语言描述等）。

下面是一个示例Schema：

![Image](images/img_016.png)

可以看到接口定义了两个字段：city 和 days。两个字段均有明确的描述信息和校验规则。接口自身的功能描述信息也有在Schema中标注。

大模型基于用户意图动态规划工具调用指令流。并根据上下文信息、工具的 Input Schema 生成调用参数。实现自然语言与工具调用的语义对齐。

**3.2 双向通讯协议**

通过双向通讯机制MCP Host 不仅可以通过RPC调用工具集，还可以实时感知工具和资源的变更。目前支持STDIO、Streamable HTTP两种通讯协议。覆盖了本地进程间通讯和远端通讯的场景。

![Image](images/img_017.png)

日志/文件处理是一个典型的应用场景。

**3.3 微内核架构**

得益于MCP微内核架构，任何支持 MCP 的 AI 应用（MCP Host）均可直接配置并使用应用市场的MCP Server（官方、三方），无需预编码适配。类似于 USB 设备插入即用。

Cline MCP Server配置文件示例：

![Image](images/img_018.png)

### 四、业务探索

为了探索AI应用架构在QQ机器人场景落地的路径。我遵循MCP提供的思路，搭建了一个的AI Agent DEMO机器人。

#### 1\. DEMO制作

机器人基于MCP协议接入工具集，基于大模型的意图识别和动态规划能力完成用户任务的过程，采用ReAct模式迭代处理用户任务，直至任务完成。

共涉及3个服务：MCP Host（即机器人服务端）和2个MCP Server（包含查询天气的工具、制定行程计划的工具）。

验证截图如下：

![Image](images/img_019.jpeg)

机器人首先提示用户补全信息，然后调用MCP Server工具集完成了"查询天气 -> 制定行程"的任务流程。最后调用大模型输出了任务总结。

由于token成本的原因，demo机器人未开放体验。

#### 2\. 架构推演

实际业务场景中智能体需要响应用户各种各样的请求，比如：搜索、画图、拍照解题、文档处理等等。单Agent架构难以支撑，难以扩展。我们把目光投向了时下热度很高的Multi-Agent架构。

### **引入Multi-Agent架构**

我们调研了：LangManus、OpenManus、OWL、Tars等完整产品形态的开源框架。同时也调研了一些更轻量的后台框架，比如[eino](https://github.com/cloudwego/eino/) 。这些框架在这些框架有一些共同点：引入了多Agent动态协同、上下文管理、任务流编排与执行等能力。核心逻辑都采用了ReAct模式进行循环迭代。都引入一套处理特定任务的工具集（如搜索、文档处理），同时支持MCP扩展。

这里基于调研的结论及对开源框架的理解画了一下 Multi-Agent的架构示意图：

![Image](images/img_020.png)

这里不展开说。后续会发专项文章。敬请期待。

### **解决大模型应用开发的痛点**

大模型给应用开发带来了很大的便利：

-   基于语义的文本处理能力：能够理解和生成人类语言，处理非结构化的内容语义关系

-   动态决策能力：能够基于上下文进行推理和判断，做出相应的行为决策


但大模型提供良好泛化能力的同时也引入了一些痛点，那就是**准确性**和**稳定性**

典型 case

**准确性** ：用户希望使用AI Agent的P图功能，在发送图片给Agent后，又说"卡通风格"。而AI Agent 出戏了回复了一段文字解释了卡通风格。大模型没有理解到用户处于画图的流程中。

**稳定性**：用户输入"我明天去第比利斯旅行，请帮我制定一个4天旅行计划"。可能存在大模型第一次规划的任务流程和第二次不一致的情况，比如：第一次"调用工具查询天气 -> 调用工具制定行程计划"，第二次"询问用户当地的天气情况- > 调用工具制定行程计划"。

可以从算法和工程两个维度来改进。这里主要探讨**工程化的提升手段/措施**：

1.  提升意图识别准确性的工程化手段


1.1 精细化提示词管理、上下文管理，为大模型提供必要准确的信息。

1.2 通过任务质量Agent 收集低置信度意图识别结果。完成反馈与修正流程。

2.  提升任务流规划稳定性的工程化手段


2.1. （参考eino框架的思路）开发者预先定义执行图的结构和可能的路径，固化某些业务的处理流程，而大模型在运行时根据任务内容动态决定具体走哪条路径。这种设计既保证了系统的结构化和可控性，又提供了足够的灵活性来处理各种复杂任务。

2.2. 复杂流程处理上：增加按照用户响应判断是否跳出任务的处理过程的逻辑或步骤。

抛砖引玉。这里简单聊了一下我在探索AI应用架构落地过程中遇到的一些问题和思考。

### 五、总结与展望

写这篇文章加实践探索先后花了2周左右的时间。这段时间MCP生态活跃。我也不断在更新文章第一章节的Timeline。

我深切地感受到技术创新正以前所未有的速度进行着。同时也意识到技术创新给业务生态带来的无限可能：

各个行业可以基于MCP协议开放工具（比如购买机票、预订外卖），参与AI工业革命的进程。

智能体应用（手机APP、桌面端或网页）可以基于MCP开放生态接入的海量工具构建业务形态。比如：用户发出的自然语言指令，智能体应用借助外部服务/工具完成用户任务（比如用户："帮我购买8月份去格鲁吉亚旅游的低价往返机票"。智能体应用：首先提供机票查询结果，然后在用户确认后购买机票，并设定日程提醒）

后续会持续分享AI应用架构在QQ业务场景落地的实践。欢迎大家来交流。

### 附录

#### **安利一下**

目前，QQ的AI能力已进入内测阶段。官方AI伙伴「小Q」完成全新升级：通过接入混元大模型与DeepSeek模型，新增深度思考与联网搜索能力，可提供更专业的综合信息服务。其功能覆盖AI识图、AI绘图、AI写作等多元场景，同时QQ搜索已整合AI技术，支持多模型自由切换，助你高效获取全网信息。

感兴趣的用户可申请内测资格，加入官方测试群与AI爱好者深度交流。

https://docs.qq.com/form/page/DZWhjSUZoUGppRm9u

小Q机器人:

![Image](images/img_021.jpeg)

QQ机器人开放平台： [https://bot.q.qq.com/wiki/develop/api-v2/](https://bot.q.qq.com/wiki/develop/api-v2/)

QQAI交流群:

![Image](images/img_022.png)

#### 参考资料

MCP 官网：https://modelcontextprotocol.io/introduction

MCP Roadmap https://modelcontextprotocol.io/development/roadmap

官方 MCP Server： [https://github.com/modelcontextprotocol/servers/](https://github.com/modelcontextprotocol/servers/)

Awesome MCP Servers https://mcpservers.org/

图解「模型上下文协议（MCP）」https://segmentfault.com/a/1190000046385557

![Image](images/img_023.gif)

![Image](images/img_024.png)