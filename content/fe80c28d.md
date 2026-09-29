# Anthropic 详解 Managed Agents：大脑与手的解耦架构

---

**英文原文：**

A running topic on the Engineering Blog is how to build effective agents and design harnesses for long-running work. A common thread across this work is that harnesses encode assumptions about what Claude can't do on its own. However, those assumptions need to be frequently questioned because they can go stale as models improve.

**中文翻译：**

工程博客的一个持续性话题是如何构建有效的 Agent 并为长时间运行的任务设计 Harness。这项工作的共同点是：Harness 编码了关于 Claude 自身无法完成什么的假设。然而，这些假设需要经常被质疑，因为随着模型能力的提升，它们可能变得过时。

---

**英文原文：**

We expect harnesses to continue evolving. So we built Managed Agents: a hosted service in the Claude Platform that runs long-horizon agents on your behalf through a small set of interfaces meant to outlast any particular implementation—including the ones we run today.

**中文翻译：**

我们预计 Harness 将继续演进。因此我们构建了 Managed Agents：这是 Claude Platform 的一项托管服务，通过一组小型接口代您运行长时间跨度的 Agent，这些接口的设计旨在超越任何特定实现——包括我们目前运行的这些。

---

**英文原文：**

Building Managed Agents meant solving an old problem in computing: how to design a system for "programs as yet unthought of." Decades ago, operating systems solved this problem by virtualizing hardware into abstractions—process, file—general enough for programs that didn't exist yet. The abstractions outlasted the hardware.

**中文翻译：**

构建 Managed Agents 意味着解决计算领域的一个古老问题：如何为一个"尚未被想到的程序"设计系统。几十年前，操作系统通过将硬件虚拟化为抽象概念（进程、文件）来解决这个问题——这些抽象概念足够通用，能够容纳尚不存在的程序。这些抽象概念比硬件更持久。

---

**英文原文：**

## Don't adopt a pet

We started by placing all agent components into a single container, which meant the session, agent harness, and sandbox all shared an environment. But by coupling everything into one container, we ran into an old infrastructure problem: we'd adopted a pet. In the pets-vs-cattle analogy, a pet is a named, hand-tended individual you can't afford to lose, while cattle are interchangeable. In our case, the server became that pet; if a container failed, the session was lost.

**中文翻译：**

## 不要养"宠物"

我们最初将所有 Agent 组件放在一个容器中，这意味着会话、Agent Harness 和沙箱共享同一个环境。但通过将所有内容耦合到一个容器中，我们遇到了一个古老的基础设施问题：我们养了一只"宠物"。在"宠物 vs. 牛群"的类比中，宠物是一个有名字、需要人工照料的个体，你承受不起失去它；而牛群则是可互换的。在我们的案例中，服务器成了那只宠物——如果容器失败，会话就会丢失。

---

**英文原文：**

The solution we arrived at was to decouple what we thought of as the "brain" (Claude and its harness) from both the "hands" (sandboxes and tools that perform actions) and the "session" (the log of session events). Each became an interface that made few assumptions about the others, and each could fail or be replaced independently.

**中文翻译：**

我们得出的解决方案是将"大脑"（Claude 及其 Harness）与"手"（执行操作的沙箱和工具）以及"会话"（会话事件的日志）解耦。每一个都成为一个接口，对其他组件的假设很少，并且每一个都可以独立失败或被替换。

---

**英文原文：**

**The security boundary.** In the coupled design, any untrusted code that Claude generated was run in the same container as credentials—so a prompt injection only had to convince Claude to read its own environment. The structural fix was to make sure the tokens are never reachable from the sandbox where Claude's generated code runs.

**中文翻译：**

**安全边界。** 在耦合设计中，Claude 生成的任何不受信任的代码都在与凭证相同的容器中运行——因此提示注入只需说服 Claude 读取自己的环境。结构性修复方案是确保令牌永远无法从 Claude 生成代码运行的沙箱中访问到。

---

**英文原文：**

## The session is not Claude's context window

Long-horizon tasks often exceed the length of Claude's context window, and the standard ways to address this all involve irreversible decisions about what to keep. In Managed Agents, the session provides this same benefit, serving as a context object that lives outside Claude's context window. The interface, getEvents(), allows the brain to interrogate context by selecting positional slices of the event stream.

**中文翻译：**

## 会话不是 Claude 的上下文窗口

长时间跨度的任务通常会超出 Claude 上下文窗口的长度，而标准的解决方案都涉及关于保留什么的不可逆决策。在 Managed Agents 中，会话提供了同样的功能，作为存在于 Claude 上下文窗口之外的上下文对象。接口 getEvents() 允许"大脑"通过选择事件流的positional切片来查询上下文。

---

**英文原文：**

## Many brains, many hands

Decoupling the brain from the hands solved one of our earliest customer complaints. That dead time is expressed in time-to-first-token (TTFT), which measures how long a session waits between accepting work and producing its first response token. Using this architecture, our p50 TTFT dropped roughly 60% and p95 dropped over 90%.

**中文翻译：**

## 多脑、多手

将大脑与手解耦解决了我们最早的客户投诉之一。空闲时间用首 token 时间（TTFT）来表达，它衡量会话在接受工作到产生第一个响应 token 之间等待的时间。使用这种架构后，我们的 p50 TTFT 下降了约 60%，p95 下降了超过 90%。

---

**英文原文：**

We also wanted the ability to connect each brain to many hands. In practice, this means Claude must reason about many execution environments and decide where to send work—a harder cognitive task than operating in a single shell.

**中文翻译：**

我们还希望能够将每个大脑连接到多个"手"。在实践中，这意味着 Claude 必须对多个执行环境进行推理，并决定将工作发送到哪里——这比在单个 shell 中操作更是一项认知挑战。

---

**英文原文：**

## Conclusion

Managed Agents is a meta-harness, unopinionated about the specific harness that Claude will need in the future. Rather, it is a system with general interfaces that allow many different harnesses. We designed the interfaces so that these can be run reliably and securely over long time horizons. But we make no assumptions about the number or location of brains or hands that Claude will need.

**中文翻译：**

## 结论

Managed Agents 是一个元 Harness，对 Claude 未来需要什么具体 Harness 没有预设立场。相反，它是一个具有通用接口的系统，允许许多不同的 Harness 共存。我们设计了这些接口，使它们能够在长时间跨度内可靠且安全地运行。但我们对 Claude 需要的"大脑"或"手"的数量和位置没有任何假设。
