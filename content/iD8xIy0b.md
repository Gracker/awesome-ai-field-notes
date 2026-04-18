---
id: "7444674216445611799"
cubox_url: https://cubox.pro/web/card/7444674216445611799
url: https://mp.weixin.qq.com/s?__biz=MzkyMjE3ODMwNw==&mid=2247485600&idx=1&sn=24deb11e6d44263d059aeaac5ad157bf&chksm=c050e28d3809571e02879e042a022bc07722d243c8ca1d07c7cec97d9184b010bcc2001115f3&mpshare=1&scene=1&srcid=041701LvfCoJlF7bItVxuPJr&sharer_shareinfo=dda6fc24204cc011112c075f4c81f840&sharer_shareinfo_first=dda6fc24204cc011112c075f4c81f840
tags: []

---
# Mobicom-26论文|移动和车载系统上大型应用冷启动的内存调度框架

Mobicom-26论文|移动和车载系统上大型应用冷启动的内存调度框架

[Read in Cubox](https://cubox.pro/web/card/7444674216445611799)  
[Read Original](https://mp.weixin.qq.com/s?__biz=MzkyMjE3ODMwNw==&mid=2247485600&idx=1&sn=24deb11e6d44263d059aeaac5ad157bf&chksm=c050e28d3809571e02879e042a022bc07722d243c8ca1d07c7cec97d9184b010bcc2001115f3&mpshare=1&scene=1&srcid=041701LvfCoJlF7bItVxuPJr&sharer_shareinfo=dda6fc24204cc011112c075f4c81f840&sharer_shareinfo_first=dda6fc24204cc011112c075f4c81f840)  

---

***点击蓝字***


*关注我们*


人机物融合智能计算


本公众号由西北工业大学"智能感知与计算工信部重点实验室"，"陕西省嵌入式系统技术重点实验室"联合创建，面向人机物融合智能计算系统，聚焦学科前沿最新发展，关注产学研协同融合，发布领域内学术动态。


成果概括


针对现代手机在GB级别大型应用条件下，应用启动慢且多任务体验差的问题。我们发现，尽管多任务处理使得系统运行时行为变得复杂，但每个应用的文件访问模式仍然是可预测的 。挑战在于如何利用这种可预测性：即在不耗尽内存的前提下进行预加载，在不抵消预加载收益的前提下进行回收，以及为了保留后台存活能力而进行选择性查杀 。为此，我们提出了 AppFlow，一种基于预测的系统级调度器，它集成了"选择性文件预加载器"、"自适应内存回收器"和"上下文感知进程查杀器"，将 GB 级应用的冷启动延迟降低了 66.5%（例如从 2秒降至 690毫秒），并在长达 100 天的测试中使 95% 的启动维持在 1秒以内，显著提升了响应速度和多任务体验 。本工作已被The 32nd Annual International Conference on Mobile Computing and Networking (Mobicom-26)录用。


**简介**


随着移动技术的发展，端侧大模型（如Qwen2.5, Gemma）、富媒体编辑应用（CapCut）和3D游戏（PUBG）等GB级大应用已成为主流。然而，移动设备和车载系统的内存资源有限，会导致应用冷启动时间长和多任务并发数受限的问题。现有研究存在以下局限性:

* 预加载： 能够通过减少I/O阻塞来加速应用冷启动过程，但现有预加载方法平等处理所有预加载对象，无法在低内存开销的同时实现高效预加载，且预加载数据易被内存回收机制抵消，从而使预加载失效。

<!-- -->

* 内存回收： 通过回收已分配内存来满足新内存申请，但文件页-匿名页的交替回收模式回收效率较低，且易将预加载内存页错误回收，导致应用启动时延增加。

本文主要贡献：

* 提出面向GB级大应用的冷启动与多任务优化方案： 针对端侧大模型（On-device LLMs）、大型游戏等GB级应用，解决了在内存受限设备上"快速冷启动"与"后台多任务存活"之间的内在冲突。

<!-- -->

* 设计系统级内存调度框架 AppFlow：利用应用文件访问模式的可预测性，统筹设计了选择性文件预加载、自适应内存回收和上下文感知进程查杀三个模块，实现了预加载与回收机制的协同优化。

<!-- -->

* 显著提升启动速度与系统响应性：在Pixel智能手机和车载系统上的实验表明，AppFlow将GB级应用的冷启动延迟降低了 66.5%，并在长达100天的真实使用测试中，使 95% 的启动和重启动保持在 1秒（用户体验临界点） 以内。


AppFlow 框架设计


AppFlow 是一个系统级的内存调度框架，基于"虽然多任务行为复杂，但单个应用的文件访问模式具有可预测性"这一洞察，通过三个核心组件实现协同优化。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F741LpYibcibNfUmiaMVGnMVcoJx5cgpUrhYEbDce36GZMbu6mbwGiaG3u9OQdWb9piaaL015n3BrZBick3Hx4MESluVw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D0)


**1. 选择性细粒度文件预加载**

针对GB级应用启动时I/O碎片化严重的问题，AppFlow 采用了分阶段策略：

* 启动前（Before-launch）：频率优先。 预加载体积小但访问频率极高的小文件（\<128KB）。研究发现小文件虽然只占总大小的3%，但占据了91%的I/O请求。预加载它们能以极小的内存代价消除大量随机I/O阻塞。

<!-- -->

* 启动中（During-launch）：吞吐量优先。 针对大文件，使用大块I/O进行流式加载，最大化I/O带宽利用率。

<!-- -->

* 动态决策： 利用背包问题求解器（Knapsack solver）在毫秒级时间内计算最优的预加载阈值。

**2. 自适应内存回收器**

传统的内存回收机制在文件页（File-backed）和匿名页（Anonymous）之间平均分配，效率低下。AppFlow 引入了页类型感知的回收策略：

* 解耦回收策略：

  效率优先模式（Efficiency-first）： 在高内存压力（如冷启动）下，优先回收文件页（无需回写Flash，速度快），迅速释放内存以消除分配阻塞。

  再平衡模式（Rebalancing）： 压力缓解后，回收匿名页以平衡内存结构。

<!-- -->

* 预加载保护（Preload-aware Retention）： 这是一个关键创新。回收器会识别并跳过刚刚被"预加载器"加载进来的页面，防止"刚加载就被回收"的无效I/O，打破了预加载与回收之间的干扰。

**3. 上下文感知进程查杀器**

当内存回收不足以满足需求时，系统需要查杀进程。AppFlow 摒弃了传统的LRU（最近最少使用）暴力查杀：

* 针对"膨胀"应用： 优先查杀长时间运行且内存占用膨胀（Bloated）的后台应用。这些应用重启后内存占用会回归基线，查杀它们能获得最大的"净内存收益"。

<!-- -->

* 保护"最近"应用： 避免查杀刚使用过的应用，因为它们被再次访问的概率极高。


**实验验证**


**1. 实验设置**

* 平台： Google Pixel 8 (8GB/6GB), Pixel 7, 车载树莓派 4B (Android 15)。

<!-- -->

* 工作负载：

  GB级大应用： Qwen2.5 (LLM), Gemma (VLM), PUBG (游戏), TikTok (媒体)。

  基线方法： Android OS 原生机制、Paralfetch (SOTA预加载)、Acclaim (SOTA回收) 及其组合。

**2. 结果分析**


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F741LpYibcibNfUmiaMVGnMVcoJx5cgpUrhYfD6xWCRfey0UMB1py2AUnyEgIJRX8dpqjxwQ28SXKLyVt0FZBbzMTQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D1)

冷启动时延减少33.7% \~ 55.7%

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F741LpYibcibNfUmiaMVGnMVcoJx5cgpUrhYxR2rt7icIzOZKL3FLCtRdFUvRiaCNJ97BLSXcYHEia04hFibRcultmibZNg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D2)

后台多任务并发数提升1.85倍

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F741LpYibcibNfUmiaMVGnMVcoJx5cgpUrhYR2cbphprSul1ToRqd6clv967YFKicFDFSiagIME5Eia2fsO5H1N8AbZjQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%23imgIndex%3D3)

真实使用负载中，冷启动时延降低23%，冷启动数量降低32.4%

**性能对比** :

* 冷启动延迟降低：在不同内存配置和负载下，AppFlow 相比 Android OS 平均降低了 33.7% \~ 57% 的冷启动延迟。

* 多任务体验提升：与 Android OS 相比，AppFlow 多保留1.85倍的后台应用程序（即从7/17个增加到13/17个），多任务平均启动时间减少37.6%。

* 真实负载验证：在包含60+应用、10000+次切换的真实轨迹测试中，AppFlow 将平均冷启动延迟降低了 23%，冷启动数量减少了 32.4%。


结论与未来工作


**1. 结论**

AppFlow 针对移动端和车载系统日益增长的GB级大应用挑战，提出了一套软硬结合的系统级解决方案。通过选择性预加载加速I/O，自适应回收消除分配阻塞并保护预加载数据，以及上下文感知查杀维护多任务体验，AppFlow成功在受限内存条件下提升了用户体验。

**2. 未来工作**

当前工作主要关注应用级启动加速，在未来的工作中，我们将结合用户行为预测，从以应用为单位的预加载和回收转向以活动为单位的预加载和回收，以进一步加速启动。


该成果由李晓晨（西北工业大学在读博士）、刘思聪（西北工业大学副教授）、郭斌（西北工业大学教授）、欧阳煜（西北大学在读学士）、伍峰民（西北工业大学在读博士）、徐源（西北工业大学在读硕士）和於志文（哈尔滨工程大学教授、西北工业大学教授）合作完成，"AppFlow: Memory Scheduling for Cold Launch of Large Apps on Mobile and Vehicle Systems"被The 32nd Annual International Conference on Mobile Computing and Networking录用。


欢迎海内外高校与企业学者前来交流与合作，也欢迎优秀的人才和同学加入我们实验室大家庭。


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2F741LpYibcibNejE0QtByxy99Y4skVIBIZGnrJeTt6v3rlnyceeSzkNhPGuDKmfIGia8z0y8ibVibjJZUyWQkYk8BG4g%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%23imgIndex%3D4)


**扫描二维码 ｜** **关注我们**



