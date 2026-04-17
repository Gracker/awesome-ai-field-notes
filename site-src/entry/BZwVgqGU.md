---
title: '微信正式发布多模态大模型POINTS1.5'
sidebar: false
---

::: info
[← 返回基础设施](/infra)
:::

# 微信正式发布多模态大模型POINTS1.5

> Cubox 收藏 — 微信正式发布多模态大模型POINTS1.5

🔗 [原文链接](https://mp.weixin.qq.com/s?__biz=MjM5ODYwMjI2MA==&mid=2649787907&idx=1&sn=e37095afd62e779e0d2b0b6356201b80&chksm=bf24d99626cf63fb1cf142d6740b5321f0853a1de019f1210500b7f57fd948c0b1a87feb0251&mpshare=1&scene=1&srcid=1214l9Q9sgMr56MjXRxwjfGh&sharer_shareinfo=8eed771cea5ad1691bbb03ff4506784c&sharer_shareinfo_first=8eed771cea5ad1691bbb03ff4506784c) | 🇨🇳 | ⭐⭐⭐⭐ 4 ⭐4 4/5 📅 2024-12-14

---

# 吴恩达：从 Agent 到 Agentic Workflow ，AI 的未来何去何从？

- **来源**：微信公众号
- **作者**：AI技能
- **原文链接**：https://mp.weixin.qq.com/s?__biz=MjM5ODYwMjI2MA==&mid=2649787907&idx=1&sn=e37095afd62e779e0d2b0b6356201b80

> 公众号: AI技能
> 发布时间: 1970-01-01 08:33:44
> 原文链接: https://mp.weixin.qq.com/s?__biz=MjM5NTg1ODg1OA==&mid=2459542397&idx=1&sn=e376ce196a41955734c48377cbc3cc18&chksm=b19f13b886e89aaec7ecb3f44f1de1300473b38346d6f8f54e8f87f4655cd87512eee06bae05&mpshare=1&scene=1&srcid=0623gOaBbHwBnL5vGTxNPHdK&sharer_shareinfo=11ba2c0c5006ec0d14971ced1c09c9c7&sharer_shareinfo_first=17a9447775b586d79d49eeec9285c317

---
_关注 **AI 技能**，开启智能生活！__![Image](images/img_001.png)_

# 摘要

> 本文《AI 的未来何去何从？关于具有代理能力的系统》深入探讨了由 Andrew Ng 提出的具有代理能力的系统概念，强调这种系统通过迭代、自我改进的过程超越传统 AI 方法。

文章概述了具有代理能力系统的关键组成部分，如反思、使用工具、规划和多代理协作，并提供了创建用于生成 Medium 帖子想法的 AI 代理的逐步指南。该过程涉及设置代理类、制定详细的反应提示、创建工具/动作功能，并通过所有动作自动化代理，展示了 AI 的思考、规划和执行任务的潜力，无需人为干预。

观点

Andrew Ng 的观点表明，具有代理能力的系统代表了 AI 能力的重大飞跃，超越了一次性提示，转向更自主和迭代的问题解决方式。作者认为，由于具有代理能力的工作流能够从问题中恢复并通过迭代过程提高性能，因此它们更为优越。预期将出现“具有代理能力的时刻”，届时 AI 的独立思考、规划和执行任务的能力将被广泛认可和利用。

文章对 AI 代理的潜力表示热情，不仅在机器人流程自动化中，而且在各个领域都突出了它们的灵活性和适应性。作者对具有代理能力系统的可扩展性充满信心，认为可以通过分解复杂任务并分配给专门的代理来有效管理。

“今年，AI 代理工作流将推动 AI 的巨大进步” —— Andrew Ng

# 正文

我最近观看了 Andrew Ng 关于《 Andrew Ng’s talk on AI agents》。受到他的洞见启发，我希望更好地理解 AI 代理。

在这篇文章中，我们将了解什么是具有代理能力的系统以及如何从头开始构建一个简单的具有代理能力的系统。

**什么是具有代理能力的工作流，为什么它更好？**

代理的概念已经存在一段时间了。这里有什么新东西吗？在他的演讲中，Andrew Ng 解释了使用反思、工具使用、规划和多代理协作等设计模式的具有代理能力的系统，这些系统的表现超过了零次提示的结果。

正如 Andrew Ng 在他的帖子中澄清的那样，代理并不是一次性提示模型（零次射击）。相反，它是一个自主的实体，给定高级指令，计划、使用工具并执行多个迭代步骤以达成目标。

代理可以用于机器人流程自动化，例如，但它的意义远大于此。当我们看到一个 AI 能够在没有任何人为干预的情况下思考、规划并执行任务时，我们将体验到“具有代理能力的时刻”。

这里的关键是，我们不告诉代理要做什么，而是由它自己决定采取哪些行动来完成任务。

由于具有代理能力的工作流让 AI 迭代工作，它们可以

从自身问题中恢复——这反过来又可以带来性能的巨大提升。


GPT3.5 与具有代理能力的工作流表现优于 GPT4。来源：Andrew Ng

**具有代理能力系统的关键组成部分**

具有代理能力的系统通常是能够完成以下所有事情的代理：

反思：分析自己的输出并识别改进的领域的代理。工具使用：访问和利用工具以增强自己能力的代理。规划：提前思考、考虑多个选项并做出明智决策的代理。多代理协作：共同解决复杂问题的多个代理。


什么使一个工作流“具有代理能力”或“非代理能力”？首先，代理与环境互动。在上面的示例中，这意味着它将提出问题、获取输入、提出后续问题、获取更多输入，一点一点地创建整个文章。更传统的“非代理能力”的方式，将从单一提示开始，模型将创建单一输出。模型没有获取新信息的机会。

通过雇用代理团队，可以使具有代理能力的工作流更加复杂。复杂任务被分解为子任务，由潜在的不同角色执行——例如软件工程师、产品经理、设计师、质量保证工程师等——并让不同的代理完成不同的子任务。

有趣的是，在多代理协作中，每个代理可以是不同的或相同的语言模型，但你以不同的方式提示它们。

**从头开始构建 AI 代理**

为了演示，我将构建一个 AI 代理来生成我的 Medium 帖子的想法。为此，我将向 AI 提供动作，包括: (1) 从 Google 趋势获取与 AI 代理主题相关的数据，(2) 分析见解，(3) 为我的 Medium 帖子提出想法。

**步骤 1：设置代理**

在此步骤中，我们将创建一个代理类来管理与两个角色的对话：用户和助理。该类包括处理消息和使用 OpenAI 的 API 生成响应的方法。我们将随时间跟踪对话。

在下面的代码中，我们通过定义一个呼叫者和执行方法，初始化代理，并确保我们可以轻松地向代理发送消息，代理将记录并传递它。

```
class Agent:    # initialize    def __init__(self, system=""):        self.system = system        self.messages = []        if self.system:            self.messages.append({"role": "system", "content": system})    # call    def __call__(self, message):        self.messages.append({"role": "user", "content": message})        result = self.execute()        self.messages.append({"role": "assistant", "content": result})        return result    #execute    def execute(self):        completion =  openai.ChatCompletion.create(                        model="gpt-4o",                         temperature=0,                        messages=self.messages)        return completion.choices[0].message.content
```

**步骤 2：设置 React 提示**

我们希望创建一个考虑特定系统消息的反应代理——我们的提示。

我们在这一步做的是创建一个详细的提示，解释思考、行动、暂停和观察的循环，并输出答案。

这个过程模仿了当我们让 AI 思考并观察以回答任务时具有代理能力的工作流的关键组成部分。

```
prompt = """You run in a loop of Thought, Action, PAUSE, Observation.At the end of the loop you output an Answer.Use Thought to describe your thoughts about the question you have been asked.Use Action together with an input to run one of the actions available to you - then return PAUSE.Action input should be the Observation from the previous Action.Observation will be the result of running those actions on those inputs.Your available actions are:generate_and_execute_pytrend_code: <key word>Create the pytrend code to get the related keywords from Google Trends for the given keywords, execute the code returns the data.analyze_trends_data: <table of top words related to trending topics>Analyze the trends table data and returns a summary of the insights from the data.generate_medium_post_ideas: `trend_summary`Generates Medium post ideas based on the trend summary.Example session:Question: What are the related keywords for the search term "AI agent"?Thought: I should generate and execute the pytrend code to fetch related topics or keywords for AI agent.Action: generate_and_execute_pytrend_code: AI agentPAUSEObservation: 0              Artificial intelligence                   Field of study  1001                    Intelligent agent                            Topic  902                       Software agent                            Topic  703                   Multi-agent system             Programming paradigm  65 Thought: I should analyze the trends data to get a summary of the insights.Action: analyze_trends_data: 0              Artificial intelligence                   Field of study  1001                    Intelligent agent                            Topic  902                       Software agent                            Topic  703                   Multi-agent system             Programming paradigm  65 PAUSEObservation: `trend_summary`Thought: I should generate Medium post ideas based on the trend summary.Action: generate_medium_post_ideas: `trend_summary`PAUSEObservation: `medium_post_ideas`Answer: The trending topics are `trend_summary` and here are some Medium post ideas: `medium_post_ideas`""".strip()
```

**步骤 3. 创建工具/动作功能**

现在我们需要为代理提供提示中指定的工具。在这一步中，我们将实现可提供给代理的可用动作。在每个动作函数中，我们描述哪个动作做什么。对于每个动作，我们使用不同的提示调用 API。在这种情况下，我使用相同的 LLM 模型（GPT-4o），但你可以选择为不同的动作调用不同的 LLM。

```
def generate_and_execute_pytrend_code(keyword):    def fetch_related_trending_topics(keyword):        # Initialize pytrends        pytrends = TrendReq(hl='en-US', tz=360)                # Build the payload with the specified topic        pytrends.build_payload([keyword], cat=0, timeframe='now 7-d', geo='', gprop='')                # Fetch related topics        related_topics = pytrends.related_topics()                # Extract top related topics        if keyword in related_topics and 'top' in related_topics[keyword]:            top_related_topics = related_topics[keyword]['top']            return top_related_topics        else:            return None        # usage    related_trending_topics = fetch_related_trending_topics(keyword)    return related_trending_topicsdef analyze_trends_data(trends_data):    analysis_prompt = f"""    You are an AI assistant.     Analyze and summarize the following insight: {trends_data}    """        response = openai.ChatCompletion.create(        model="gpt-4o",        messages=[{"role": "system", "content": analysis_prompt}],        temperature=0    )        return response.choices[0].message['content']def generate_medium_post_ideas(trend_summary):    analysis_prompt = f"""    You are a technical content writer. Based on the analysis     from the Google trend data for the given keyword and its     trend summary, you will generate topic ideas for Medium post.    The trend_summary is as follows:    =======    {trend_summary}    =======        """        response = openai.ChatCompletion.create(        model="gpt-4o",        messages=[{"role": "system", "content": analysis_prompt}],        temperature=0    )        return response.choices[0].message['content']
```

然后，我们将创建一个名为 known\_actions 的字典，将动作名称映射到函数。这允许代理根据提示中指定的动作动态调用适当的函数。代理选择采取哪些动作，这是它经过思考过程的

结果：

```
# Known actions dictionaryknown_actions = {    "generate_and_execute_pytrend_code": generate_and_execute_pytrend_code,    "analyze_trends_data": analyze_trends_data,    "generate_medium_post_ideas": generate_medium_post_ideas,
```

**步骤 4：通过所有动作自动化代理**

在下面我们定义了具有代理能力的工作流的思考循环。查询函数中的循环管理用户与代理的互动。它从初始化代理和处理用户问题开始。在每次迭代中，代理生成响应，识别响应中的任何动作（可用于它）并执行 known\_actions 字典中的相应函数。然后使用生成的观察结果更新下一个提示。此过程持续进行指定的轮数或直到不再识别出进一步的动作为止：

```
# Regex for action selectionaction_re = re.compile('^Action: (\w+): (.*)$')# Function to query and handle actionsdef query(question, keyword, max_turns=5):    # initialize the agent    i = 0    bot = Agent(prompt)    next_prompt = question    observation = ""    # run through the loop for max_turn - numbers of times the agent thinks and responds    while i < max_turns:        i += 1        # interaction with the agent, it produces the output        result = bot(next_prompt)        # identify actions        actions = [            action_re.match(a)             for a in result.split('\n')             if action_re.match(a)        ]                if actions:            # if there is an action to run            action, action_input = actions[0].groups()            if action not in known_actions:                raise Exception(f"Unknown action: {action}")            if action == "generate_and_execute_pytrend_code":                observation = known_actions[action](keyword)            else:                observation = known_actions[action](action_input)                        print("Observation:", observation)            next_prompt = f"Observation: {observation}"        else:            return# usagekeyword = "AI Agent"question = "Give me some ideas for Medium posts related to the topic 'AI agent'."query(question, keyword)
```

这里是输出。正如您所见，代理从它的思考开始，这决定了它采取的动作，最终输出答案：

```
Thought: To generate Medium post ideas related to AI agent, I need to first fetch the trending topics and related queries from Google Trends for the keyword "AI agent". Then, I can analyze the trends data and generate relevant post ideas.Action: generate_and_execute_pytrend_code: "AI agent"                           topic_title                       topic_type  0              Artificial intelligence                   Field of study  1                    Intelligent agent                            Topic  2                       Software agent                            Topic  3                               create                            Topic  4                         Intelligence                            Topic  5                            Vertex AI                            Topic  6   Generative artificial intelligence                            Topic  7                                 Data                            Topic  8                               OpenAI  Artificial intelligence company  9                            LangChain                            Topic  10                  Multi-agent system             Programming paradigm  11                            Learning                            Topic  12   Application programming interface                 Type of software  13                         Real Estate                            Topic  14                  Software framework                            Topic  15                  Real Estate Broker                       Occupation  16                             Chatbot                            Topic  17                              Python             Programming language  18                    Machine learning                   Field of study  19                           Knowledge                            Topic  20                            Software                            Topic  21                          Automation                            Topic  22                  Agent architecture                            Topic  23                            Database                 Type of software  24                           Structure                            Topic  Thought: I have received the trending topics data related to AI agents. The next step is to analyze this data to summarize the trends.Action: analyze_trends_data: PAUSEObservation: This dataset provides insights into trending topics related to AI and related fields over the past week. The data includes the following key elements:### Key Observations:- **Top Trending Topic**: "Artificial intelligence" is the most popular topic with a score of 100.- **Diverse Topics**: The list includes a variety of topics such as "Intelligent agent," "Software agent," "Generative artificial intelligence," "OpenAI," "LangChain," "Multi-agent system"."- **Categories**: Topics span multiple categories including fields of study, types of software, occupations, and programming paradigms.Thought: I have a summary of the trending topics related to AI and its various subfields. The next step is to generate Medium post ideas based on this trend summary.Action: generate_medium_post_ideas: `trends_data`Observation: Based on the provided trend summary, here are some topic ideas for Medium posts specifically related to the keyword "Artificial Intelligence":1. **"Intelligent Agents: The Future of Autonomous Decision-Making"**   - Delve into the concept of intelligent agents, their architecture, and real-world applications. Highlight how they are being used in industries like finance, healthcare, and customer service.2. **"LangChain: Revolutionizing AI Development with Modular Components"**   - Introduce LangChain, its features, and how it simplifies the development of AI applications. Provide examples and case studies of successful implementations.3. **"Vertex AI: Google's Comprehensive AI Platform for Developers"**   - Provide an overview of Vertex AI, its capabilities, and how it compares to other AI platforms. Include a step-by-step guide on getting started with Vertex AI.4. **"Multi-Agent Systems: Coordinating Intelligent Agents for Complex Tasks"**   - Explain the concept of multi-agent systems and their applications in solving complex problems. Discuss coordination strategies and real-world examples.5. **"Chatbots and Automation: Enhancing Customer Experience with AI"**   - Explore the role of chatbots in customer service and how automation is improving efficiency. Highlight successful chatbot implementations and best practices.
```

这种设置允许代理通过不同的动作过程生成 Medium 帖子想法。我提供给代理的唯一事物是它可以采取的可用动作。我没有告诉它执行动作的顺序。代理决定首先从 Google 趋势中获取趋势数据，分析数据，然后生成相关的内容想法。

您也可以通过在工作流中添加更多关键动作来否决代理产生的输出，以获得更好的输出。

# 结论

恭喜！您现在已经掌握了如何构建自己的代理。

我们在这篇帖子中使用的示例非常简单，但您绝对可以使用相同的原则构建复杂的代理。我很好奇听到您的代理，让我在评论中知道！

> 原文：
> https://levelup.gitconnected.com/where-is-ai-headed-it-is-about-agents-802c79ed2637

如喜欢本文，请点击右上角，把文章分享到朋友圈
如有想了解学习的技术点，请留言给若飞安排分享

**·END·**


**因公众号更改推送规则，请点“在看”并加“星标”第一时间获取精彩技术分享**


进ChatGPT群请加若飞，暗号 “gpt”
