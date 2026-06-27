# A2A v1.0 协议全面落地：150+ 组织支持，AI 代理互操作进入生产阶段

- **ID**: a2a_protocol_v1_0_2026_001
- **原文链接**: https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year （原 URL https://agent-to-agent.org/v1-0-release 当前指向未上线页面，已回退至 Linux Foundation 官方公告）
- **作者**: Linux Foundation / A2A Standards Consortium
- **日期**: 2026-04-09
- **分类**: agents
- **标签**: A2A, Agent-to-Agent, 协调协议, 标准化, v1.0, Linux-Foundation
- **质量评分**: 5/5
- **抓取时间**: 2026-06-27T20:40:00

---

## 中文翻译

### 概览

**2026 年 4 月 9 日，旧金山** —— 由 Linux 基金会托管的 A2A（Agent-to-Agent，代理对代理）协议项目，在其一周年节点宣布了重大采用里程碑：超过 150 家组织支持该标准，深度集成到 Google、Microsoft 和 AWS 平台，并在多个行业投入生产部署。

A2A 在不到一年的时间内，从初步发布演进为生产就绪的开放标准，实现无缝的代理对代理通信。垂直应用涵盖供应链、金融服务、保险和 IT 运维等领域，组织使用 A2A 在不同工具、厂商和环境间协调自主系统。

这种快速采用反映了面向代理架构的更广泛转变。随着软件系统更加独立运行，协同成为瓶颈。A2A 通过提供通用语义模型和版本协商机制来解决这一瓶颈，标准化代理如何发现、通信和相互交易，而无需绑定在单一厂商的生态中。

> "AI 代理只有具备协作能力才有价值，150 多家组织采用 A2A 凸显了人们对开放、可互操作协议的广泛热情，"Google Cloud 商业应用平台副总裁兼总经理 Rao Surapaneni 表示，"这种势头迅速将该项目推向了生产就绪阶段，使不同的 AI 系统能够跨环境协同工作，避免那些常常阻碍其扩展的孤立定制连接。"

### 更新与采用

A2A 的发展势头在 1.0 版（首个稳定规范）发布后加速。更新引入了多协议支持、企业级多租户、现代化安全流以及面向早期采用者的明确迁移路径，消除了生产部署的关键障碍。特性包括用于加密身份验证的**签名 Agent Cards** 和支持常见安全与负载均衡模式的 **Web 对齐架构**，以实现高规模可靠性。此外，基于不同平台（LangGraph、CrewAI 等）构建的异构代理现在能够协同工作、委派子任务，并在不共享内部记忆的情况下协调复杂工作流。

云厂商也通过将 A2A 直接嵌入平台来强化这一势头。Microsoft 将 A2A 集成到 Azure AI Foundry 和 Copilot Studio，AWS 通过 Amazon Bedrock AgentCore Runtime 添加支持。这些集成使 A2A 成为云上构建代理系统的默认标准。

该协议也已从通信领域扩展到经济协调。**Agent Payments Protocol (AP2)** 的推出支持安全的代理驱动交易，60 多家支付和金融服务的组织已经支持该计划。此外，UCP 通过其 AP2 授权扩展完全兼容 AP2，使其能够捕获用户购买同意的强加密证据。这将 A2A 扩展到需要交易完整性的高信任度、受监管环境。

### 生态规模

自 2025 年 4 月以来，支持组织数量从 50 多家增长到 150 多家 —— 包括 AWS、Cisco、Google、IBM、Microsoft、Salesforce、SAP 和 ServiceNow。核心仓库已超过 22,000 颗 GitHub Star，SDK 生态系统从单一的 Python 实现扩展到五种生产就绪语言，包括 JavaScript、Java、Go 和 .NET。

在标准层面，A2A 与 **Model Context Protocol (MCP)**（同样是 Linux 基金会项目）形成互补。A2A 定义代理如何跨越组织边界相互通信和协调，而 MCP 定义代理如何连接内部工具和数据源。二者共同构成了跨技术栈、无需单一平台方法的可互操作多代理系统的基础层。

展望未来，A2A 路线图包括互操作性规范、注册表工作的整合、扩展的测试与工具、安全与部署最佳实践。

凭借稳定的规范、内置的云支持以及不断增长的企业应用，A2A 正在从早期采用阶段演变为现代 AI 和分布式系统架构的核心组件。

### 行业引用

- **Luca Muscariello（Cisco 杰出工程师）**："A2A 是使代理对代理通信可靠且可互操作的句法层。最令人兴奋的是这仅仅是个开始 —— 在将代理互联网变成行星规模现实方面有巨大的机会。"

- **Todd Segal（Google 杰出工程师）**："A2A 为个人、团队和领域专属代理提供了在任何平台上无缝协作的安全基础。"

- **Darrel Miller（Microsoft 合作伙伴 API 架构师）**："A2A 背后的势头凸显了开放、可互操作标准对于实现多代理协作的重要性。Microsoft 期待与 Linux 基金会社区继续合作。"

### 进一步了解

- 访问 [a2a-protocol.org](http://a2a-protocol.org)
- 查看 [技术规范](https://a2a-protocol.org/)
- 查看 [GitHub 仓库](https://github.com/a2aproject/A2A)
- 报名 [DeepLearning.AI 短课程](https://goo.gle/dlai-a2a)
- 参考 [教程与示例](https://a2a-protocol.org/latest/tutorials/) 或 [SDK 参考](https://a2a-protocol.org/latest/sdk/)

*来源：The Linux Foundation, 2026-04-09*

## English Original

# A2A Protocol Surpasses 150 Organizations, Lands in Major Cloud Platforms, and Sees Enterprise Production Use in First Year

> Source: The Linux Foundation press release, April 9, 2026. The originally cited URL `https://agent-to-agent.org/v1-0-release` is currently parked on Squarespace and not serving the announcement, so the canonical press release is used here as the fallback.

**SAN FRANCISCO – April 9, 2026** – The A2A (Agent-to-Agent) Protocol project, hosted by the Linux Foundation, today announced major adoption milestones at its one-year mark, with more than 150 organizations supporting the standard, deep integration across Google, Microsoft and AWS platforms, and active production deployments across multiple industries.

In less than a year, A2A has moved from initial release to a production-ready open standard for seamless agent-to-agent communication. Vertical adoption spans supply chain, financial services, insurance, and IT operations, where organizations use A2A to coordinate autonomous systems across tools, vendors, and environments.

This rapid uptake reflects a broader shift toward agent-based architectures. As software systems operate more independently, coordination becomes the bottleneck. A2A removes that bottleneck by providing a common semantic model and version negotiation that standardize how agents discover, communicate, and transact with each other, without being locked into a single vendor's ecosystem.

> "AI agents are only as useful as their ability to collaborate, and the adoption of A2A by more than 150 organizations underscores the widespread enthusiasm for an open, interoperable protocol," said Rao Surapaneni, Vice President and General Manager of Business Applications Platform, Google Cloud.

### Updates and Adoption

A2A's momentum accelerated with the release of version 1.0, its first stable specification. The update introduced multi-protocol support, enterprise-grade multi-tenancy, modernized security flows, and a defined migration path for early adopters. Features include **Signed Agent Cards** for cryptographic identity verification and a **web-aligned architecture** that supports familiar security and load-balancing patterns. Diverse agents built on platforms like LangGraph or CrewAI are now able to work together, delegate sub-tasks, and coordinate complex workflows without sharing internal memory.

Cloud providers reinforced that momentum by embedding A2A directly into their platforms. Microsoft integrated A2A into Azure AI Foundry and Copilot Studio, and AWS added support through Amazon Bedrock AgentCore Runtime. These integrations position A2A as a default standard for building agent-based systems in the cloud.

The protocol has also expanded beyond communication into economic coordination. The introduction of the **Agent Payments Protocol (AP2)** enables secure, agent-driven transactions, with more than 60 organizations across payments and financial services already supporting the initiative.

### Ecosystem Scale

Since April 2025, the number of supporting organizations has grown from more than 50 to over 150 — including AWS, Cisco, Google, IBM, Microsoft, Salesforce, SAP, and ServiceNow. The core repository has surpassed 22,000 GitHub stars, and the SDK ecosystem has expanded from a single Python implementation to five production-ready languages, including JavaScript, Java, Go, and .NET.

A2A is complementary to the **Model Context Protocol (MCP)**, another Linux Foundation project. A2A defines how agents communicate and coordinate with each other across organizational boundaries, while MCP defines how agents connect to internal tools and data sources. Together they form a foundational layer for interoperable, multi-agent systems that work across different technology stacks without requiring a single-platform approach.

Looking ahead, the A2A roadmap includes an interoperability specification, consolidation of registry efforts, expanded testing and tooling, and security and deployment best practices.

### Supporting Quotes

- **Luca Muscariello, Distinguished Engineer, Cisco**: "A2A has emerged as the syntactic layer that makes agent-to-agent communication reliable and interoperable. What's most exciting is that this is just the beginning."
- **Todd Segal, Distinguished Engineer, Google**: "A2A provides the secure foundation for personal, team, and domain-specific agents to work together seamlessly across any platform."
- **Darrel Miller, Partner API Architect, Microsoft**: "The momentum behind A2A underscores the importance of open, interoperable standards for enabling multi-agent collaboration."

### About the A2A Protocol

The Agent-to-Agent (A2A) Protocol is an open standard that enables AI agents to discover, communicate, and transact with each other across different frameworks, vendors, and platforms. Originally developed by Google, the project is now hosted by the Linux Foundation. For more information, visit [a2a-protocol.org](http://a2a-protocol.org).

*Source: The Linux Foundation, April 9, 2026*
