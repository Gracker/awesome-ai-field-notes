# Write a Toy VPN in Rust

**中文翻译：**
# 用 Rust 写一个玩具 VPN

---

> 作者: Yiran Sheng
> 发布时间: 2023-12-17
> 原文链接: https://t.co/WrzXZR9mxi

**中文翻译：**
> 作者：Yiran Sheng
> 发布时间：2023-12-17
> 原文链接：https://t.co/WrzXZR9mxi

---

---
[](/)[](https://github.com/yiransheng)

**中文翻译：**
---
主页链接与 GitHub 个人资料链接。

---

# Write a Toy VPN in Rust

**中文翻译：**
# 用 Rust 写一个玩具 VPN

---

#### Yiran Sheng

**中文翻译：**
#### Yiran Sheng

---

#### 12/17/2023

**中文翻译：**
#### 2023 年 12 月 17 日

---

-   [Introduction and Motivation](#introduction-and-motivation)
-   [The First Step](#the-first-step)
    -   [Preliminaries: Environment Setup](#preliminaries-environment-setup)
    -   [Proof of Concept](#proof-of-concept)
    -   [The Way Packets Flow](#the-way-packets-flow)
    -   [Basic Types](#basic-types)
    -   [Two main loops](#two-main-loops)
    -   [Put it All Together](#put-it-all-together)
-   [Let’s Epoll](#lets-epoll)
    -   [Quick Preview](#quick-preview)
    -   [Epoll Basics](#epoll-basics)
    -   [Understanding `epoll_event`](#understanding-epoll_event)
    -   [Handling Callbacks in Rust](#handling-callbacks-in-rust)
    -   [The `Poll` Wrapper](#the-poll-wrapper)
    -   [Revised `Device` Type](#revised-device-type)
    -   [Port Reuse](#port-reuse)
    -   [The Startup and the Handlers](#the-startup-and-the-handlers)
    -   [That’s all and the Final Code](#thats-all-and-the-final-code)
-   [Many Peers](#many-peers)
    -   [Project Overview](#project-overview)
    -   [Peer Identities](#peer-identities)
    -   [The Dual Purposes of `AllowedIPs`](#the-dual-purposes-of-allowedips)
    -   [`Peer` Selection](#peer-selection)
    -   [The Protocol](#the-protocol)
    -   [Delegation of Responsibilities: `Peer` vs. `Device`](#delegation-of-responsibilities-peer-vs.-device)
    -   [Driving the State Machine](#driving-the-state-machine)
    -   [Parse Configurations](#parse-configurations)
    -   [Updated `main` function](#updated-main-function)
-   [Test Drive](#test-drive)
-   [Multithreading](#multithreading)
    -   [Epoll One Last Time](#epoll-one-last-time)
-   [Conclusion: Insights and Reflections](#conclusion-insights-and-reflections)
    -   [Further Readings](#further-readings)

**中文翻译：**
-   [引言与动机](#introduction-and-motivation)
-   [第一步](#the-first-step)
    -   [准备工作：环境搭建](#preliminaries-environment-setup)
    -   [概念验证](#proof-of-concept)
    -   [数据包的流动方式](#the-way-packets-flow)
    -   [基础类型](#basic-types)
    -   [两个主循环](#two-main-loops)
    -   [整合起来](#put-it-all-together)
-   [来用 Epoll 吧](#lets-epoll)
    -   [快速预览](#quick-preview)
    -   [Epoll 基础](#epoll-basics)
    -   [理解 `epoll_event`](#understanding-epoll_event)
    -   [在 Rust 中处理回调](#handling-callbacks-in-rust)
    -   [`Poll` 包装器](#the-poll-wrapper)
    -   [修改后的 `Device` 类型](#revised-device-type)
    -   [端口复用](#port-reuse)
    -   [启动流程与处理器](#the-startup-and-the-handlers)
    -   [就这些，以及最终代码](#thats-all-and-the-final-code)
-   [多个 Peer](#many-peers)
    -   [项目概览](#project-overview)
    -   [Peer 身份](#peer-identities)
    -   [`AllowedIPs` 的双重用途](#the-dual-purposes-of-allowedips)
    -   [`Peer` 选择](#peer-selection)
    -   [协议](#the-protocol)
    -   [职责委派：`Peer` vs. `Device`](#delegation-of-responsibilities-peer-vs.-device)
    -   [驱动状态机](#driving-the-state-machine)
    -   [解析配置](#parse-configurations)
    -   [更新后的 `main` 函数](#updated-main-function)
-   [试运行](#test-drive)
-   [多线程](#multithreading)
    -   [最后再看一次 Epoll](#epoll-one-last-time)
-   [结论：洞见与反思](#conclusion-insights-and-reflections)
    -   [延伸阅读](#further-readings)

---

## Introduction and Motivation

**中文翻译：**
## 引言与动机

---

I started using `wireguard` some five years ago. Touted as simple and user-friendly, I quickly realized its learning curve was steeper than expected. The labyrinth of networking concepts and system tools seemed like voodoo magic to me. This experience was one of many that steered me towards Rust, a language that promised more clarity in the often murky waters of low-level system networking and programming. While I’ve grown comfortable with Rust as a system programming language, yet the domain itself remained somewhat mystical. For example, the inner workings of `wireguard` seemed like a well-kept secret, leaving me wondering how it managed to create an alternative Internet and the roles of those `iptables` incatations in its `PostUp`. My curiosity was reignited when I stumbled upon Jon Gjengset (jonhoo)’s [Implementing TCP in Rust](https://www.youtube.com/watch?v=bzja9fQWzdA) stream. His discussion about the `tun` interface was an eye-opener. Despite years as a web engineer and countless encounters with `wg0`, I was oblivious to this concept. Jonhoo’s explanation was a revelation, and suddenly, the pieces began to fall into place.

**中文翻译：**
我大约五年前开始使用 `wireguard`。它常被宣传为简单、用户友好，但我很快发现它的学习曲线比预期陡得多。各种网络概念和系统工具交织在一起，像某种巫术一样让我摸不着头脑。也正是这类经历推动我转向 Rust：在低层系统网络和编程这片常常浑浊的水域里，Rust 承诺带来更多清晰性。虽然我已经习惯把 Rust 当作系统编程语言来使用，但这个领域本身依然多少带着神秘感。比如，`wireguard` 的内部工作机制看起来像一个被严密守护的秘密，让我一直好奇它究竟如何创建出一张“替代互联网”，以及 `PostUp` 里那些 `iptables` 咒语到底扮演什么角色。后来我偶然看到 Jon Gjengset（jonhoo）的 [Implementing TCP in Rust](https://www.youtube.com/watch?v=bzja9fQWzdA) 直播，兴趣又被重新点燃。他关于 `tun` 接口的讨论让我大开眼界。尽管我做了多年 Web 工程师，也无数次见过 `wg0`，却一直不知道这个概念。Jonhoo 的解释像一次启示，许多碎片突然开始拼到一起。

---

Motivated by this newfound understanding, I decided to dive deeper into lower-level network programming through a practical approach: creating a simplified version of `wireguard`, focusing on packet routing and bypassing the complexities of security and VPN protocols. Though the project was small, the journey was packed with enlightening moments and intriguing detours. This led to my decision to document the process, naming the project `wontun`.

**中文翻译：**
在这次新理解的推动下，我决定用一种实践方式更深入地探索低层网络编程：创建一个简化版的 `wireguard`，专注于数据包路由，并绕开安全和 VPN 协议中的复杂部分。项目虽然不大，但整个过程充满了让人豁然开朗的时刻，也有不少有趣的岔路。于是我决定把这个过程记录下来，并把项目命名为 `wontun`。

---

![](data:image/png;base64,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

**中文翻译：**
这是一段内嵌 PNG 图片的 base64 数据。由于任务要求只截取原文前 15000 个字符，这里的图片数据在截断点处结束；它不是自然语言正文，因此不做逐字翻译。

---
