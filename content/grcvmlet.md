# Scaling Managed Agents：解耦大脑与双手

## 英文原文

Building Managed Agents meant solving an old problem in computing: how to design a system for "programs as yet unthought of." Decades ago, operating systems solved this problem by virtualizing hardware into abstractions—process, file—general enough for programs that didn't exist yet. The abstractions outlasted the hardware. The read() command is agnostic as to whether it's accessing a disk pack from the 1970s or a modern SSD. The abstractions on top stayed stable while the implementations underneath changed freely.
Managed Agents follow the same pattern. We virtualized the components of an agent: a session (the append-only log of everything that happened), a harness (the loop that calls Claude and routes Claude's tool calls to the relevant infrastructure), and a sandbox (an execution environment where Claude can run code and edit files). This allows the implementation of each to be swapped without disturbing the others.

## 中文翻译

构建托管智能体（Managed Agents）意味着解决计算领域的一个古老问题：如何为一个"尚未被想到的程序"设计系统。几十年前，操作系统通过将硬件虚拟化为抽象——进程、文件——来解决这个问题，这些抽象对尚未存在的程序也足够通用。抽象比硬件更持久。read() 命令不知道它访问的是 1970 年代的数据磁盘组还是现代 SSD。上层的抽象保持稳定，而下层的实现可以自由变化。
托管智能体遵循相同的模式。我们将智能体的组件虚拟化：会话（所有发生事件的仅追加日志）、harness（调用 Claude 并将 Claude 的工具调用路由到相关基础设施的循环）和沙盒（ Claude 可以运行代码和编辑文件的执行环境）。这允许交换每个的实现而不干扰其他组件。

---

## 英文原文

We started by placing all agent components into a single container, which meant the session, agent harness, and sandbox all shared an environment. But by coupling everything into one container, we ran into an old infrastructure problem: we'd adopted a pet. In the pets-vs-cattle analogy, a pet is a named, hand-tended individual you can't afford to lose, while cattle are interchangeable. In our case, the server became that pet; if a container failed, the session was lost.
The solution we arrived at was to decouple what we thought of as the "brain" (Claude and its harness) from both the "hands" (sandboxes and tools that perform actions) and the "session" (the log of session events). Each became an interface that made few assumptions about the others, and each could fail or be replaced independently.

## 中文翻译

我们最初将所有智能体组件放入单个容器，这意味着会话、智能体 harness 和沙盒共享一个环境。但通过将所有内容耦合到一个容器中，我们遇到了一个古老的基础设施问题：我们养了一只"宠物"。在宠物与牛群的类比中，宠物是一个被命名、由专人照料的个体，你不能失去它，而牛群是可互换的。在我们的案例中，服务器成为了那只宠物；如果容器失败，会话就会丢失。
我们得出的解决方案是将我们所谓的"大脑"（Claude 及其 harness）与"双手"（执行操作的沙盒和工具）和"会话"（会话事件的日志）解耦。每一个都成为一个对其他很少假设的接口，并且每一个都可以独立失败或替换。

---

## 英文原文

Decoupling the brain from the hands meant the harness no longer lived inside the container. It called the container the way it called any other tool: execute(name, input) → string. The container became cattle. If the container died, the harness caught the failure as a tool-call error and passed it back to Claude. If Claude decided to retry, a new container could be reinitialized with a standard recipe: provision({resources}). We no longer had to nurse failed containers back to health.
The security boundary. Any untrusted code that Claude generated was run in the same container as credentials—so a prompt injection only had to convince Claude to read its own environment. The structural fix was to make sure the tokens are never reachable from the sandbox where Claude's generated code runs. For Git, we use each repository's access token to clone the repo during sandbox initialization and wire it into the local git remote. Git push and pull work from inside the sandbox without the agent ever handling the token itself.

## 中文翻译

将大脑与双手解耦意味着 harness 不再存在于容器内。它像调用任何其他工具一样调用容器：execute(name, input) → string。容器变成了牛群。如果容器死亡，harness 将失败作为工具调用错误捕获并传回给 Claude。如果 Claude 决定重试，可以用标准配方重新初始化新容器：provision({resources})。我们不再需要将失败的容器护理回健康状态。
安全边界。任何 Claude 生成的不可信代码都在与凭证相同的容器中运行——所以提示注入只需要说服 Claude 读取其自身环境。结构性的修复是确保令牌永远不会从 Claude 生成的代码运行的沙盒中访问。对于 Git，我们在沙盒初始化期间使用每个仓库的访问令牌克隆仓库，并将其接入本地 git remote。Git push 和 pull 从沙盒内部工作，而智能体本身从不处理令牌。

---

## 英文原文

Long-horizon tasks often exceed the length of Claude's context window, and the standard ways to address this all involve irreversible decisions about what to keep. In Managed Agents, the session provides a benefit of serving as a context object that lives outside Claude's context window. The interface, getEvents(), allows the brain to interrogate context by selecting positional slices of the event stream. Any fetched events can also be transformed in the harness before being passed to Claude's context window. These transformations can include context organization to achieve a high prompt cache hit rate and context engineering.

## 中文翻译

长期任务通常会超过 Claude 上下文窗口的长度，标准的解决方法都涉及关于保留什么的不可逆决策。在托管智能体中，会话提供了作为存在于 Claude 上下文窗口之外的上下文对象的好处。接口 getEvents() 允许大脑通过选择事件流的位置切片来查询上下文。任何获取的事件也可以在传入 Claude 上下文窗口之前在 harness 中转换。这些转换可以包括上下文组织以实现高提示缓存命中率和上下文工程。

---

## 英文原文

Decoupling the brain from the hands means that containers are provisioned by the brain via a tool call only if they are needed. So a session that didn't need a container right away didn't wait for one. Inference could start as soon as the orchestration layer pulled pending events from the session log. Using this architecture, our p50 TTFT (time-to-first-token) dropped roughly 60% and p95 dropped over 90%. Scaling to many brains just meant starting many stateless harnesses, and connecting them to hands only if needed.

## 中文翻译

将大脑与双手解耦意味着容器只在需要时由大脑通过工具调用配置。因此，不需要立即使用容器的会话不必等待它。推理可以在编排层从会话日志中拉取待处理事件时立即开始。使用这种架构，我们的 p50 TTFT（首 token 时间）下降了约 60%，p95 下降了超过 90%。扩展到多个大脑只需要启动许多无状态的 harness，并根据需要将它们连接到双手。
