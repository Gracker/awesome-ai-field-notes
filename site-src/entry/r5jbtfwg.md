---
title: 'Airbnb’s Page Performance Score on Android | by Luping Lin | The Airbnb Tech Blog | Dec, 2021 | Medium'
sidebar: false
---

::: info
[← 返回学习资源](/learning)
:::

# Airbnb’s Page Performance Score on Android | by Luping Lin | The Airbnb Tech Blog | Dec, 2021 | Medium

> Android × AI 交叉领域收藏

🔗 [原文链接](https://medium.com/airbnb-engineering/airbnbs-page-performance-score-on-android-f9fd5e733e) | 🌐 | ⭐⭐⭐⭐ 4 ⭐4 4/5 📅 2026-04-10

`Android`

---

## English

# Airbnb’s Page Performance Score on Android

![Luping Lin]()
Luping Lin7 min read·Dec 17, 2021

--

Listen

Share

Part 4 of our series on Airbnb’s Page Performance Score.

Luping Lin

![]()

Airbnb’s home grown Page Performance Score (PPS) is designed to capture the rich, complex realities of performance by collecting a multitude of user-centric performance metrics and formulating them into one single 0-100 score. In this post we will deep dive into how we define and implement these metrics on Android. Make sure you read the overview blog post first to familiarize yourself with our PPS metrics and formula.

# Instrumentation

## Universal Page Tracking System

The entire customer journey on Airbnb is divided into different pages, each of which has its own measured PPS. In order to support this page-based performance tracking system, we built a standardized infrastructure that enables engineers to configure pages representing their features.

On Android a page is associated with a Fragment. Each fragment must provide a LoggingConfig object specifying a page name, which can later be retrieved whenever the page name needs to be referenced. We collect performance data throughout the fragment’s lifecycle, and only emit the logging event when the fragment is paused.

A universal PageName enum is used to uniquely identify each page, and is referenced across all platforms to consistently represent each page in our user journey.

## Capturing Wait Time Perceived by Users

A key differentiator of our new Page Performance Score (PPS) is that it measures wait time that users can see. While our early measurement effort (mentioned in our overview blog post), which was based on the commonly known Time To Interactive (TTI) metric, measures code execution time and length of asynchronous calls. For example, PPS measures how long a user sees the loading indicators on screen, while TTI measures how long it takes for a network request to return results and how long it takes to build the view models. We believe PPS more closely reflects performance experienced by our users.

In order to capture visually perceived wait time, we needed all views with a loading state to implement an API that reports their loading state changes. We created a simple interface called LoadableView.

We provide primitives such as a base ViewGroup, a base TextView, and a base ImageView, all of which implement the LoadableView interface. Our developers simply need to inherit from these primitives for their views to be automatically instrumented.

One challenge was that we needed to keep track of a view’s visibility because if a view is not at least 10% visible on the screen we don’t want to include its loading time in our measurement. The computation of the percentage of visibility of every view is both frequent and recursive. Furthermore, most of our views are in a RecyclerView and we must ensure their visibility is updated correctly on each scroll event, while keeping the RecyclerView performant. We devised algorithms to reduce the frequency and complexity of these calculations, including caching the visibility states within the RecyclerView.

# Metric Implementation

## Time to First Layout (TTFL)

TTFL measures how long a user has to wait before seeing any content on the screen. TTFL starts at fragment initialization and ends at the first onGlobalLayout event after the fragment is laid out, at which point the system has finished inflating, measuring, and laying out the fragment’s view hierarchy.

A slow TTFL often indicates that the fragment’s view hierarchy is overly complicated, or the UI thread is preoccupied with unnecessary tasks during fragment initialization.

## Time to Initial Load (TTIL)

TTIL measures how long a user sees loading indicators (excluding media loading which is measured separately) before meaningful content is displayed on screen. TTIL starts at fragment initialization like TTFL, and ends when no more views on screen are in a loading state. If a screen (Fragment) is static or cached we don’t show a loading indicator. In that scenario TTIL would be the same as TTFL.

A slow TTIL often reveals opportunities in improving network latency or client rendering time. For network latency we look for slow backend services, large payloads, unutilized cache, or a less optimized data parser. For rendering time we try to follow best practices in using the RecyclerView, avoid doing heavy or recursive computation when building view models, and reduce over drawing, etc.

As mentioned above, views with a loading state can inherit from base primitives with built-in LoadableView implementations. The API automatically reports the view’s loading state changes to our logging framework. We use a simple counter that increments when a view enters loading state and decrements when the data is loaded. When the counter is 0, we know that there are no more loading views on screen.

This GIF demonstrates TTFL (marked when the gray background with the Airbnb logo is shown) and TTIL (marked when the loading dots are replaced by meaningful content).

![]()

## Main Thread Hangs (MTH)

Users experience screen freezes, lags, and stutters when ui frames take too long to render. Each android device has a target frame refresh rate based on the device’s capacity. However when the main thread is too busy, the device renders slower than the frame rate it’s capable of. We define a MTH as whenever any frame takes more than twice the system’s frame refresh rate to render.

Frequent MTHs indicate that the main thread might be overloaded. Heavy operations or computations should be moved off the UI thread or delayed until contents are rendered.

MTH is calculated using FrameMetrics reported by the Android system. We obtain the frame refresh rate from the system and use it to calculate the threshold for the thread hangs. We then listen for system callbacks to receive FrameMetrics, if the frame duration is above our threshold, we record the delta (frameDuration - hangThreshold) as a hang.

## Additional Load Time (ALT)

ALT measures any wait time that occurs after the initial load, such as waiting for list paginations or for content to be updated after a Save button is pressed. ALT starts whenever a view enters the loading state after TTIL has already been marked, and ends when no more loading views are shown. ALT can start and end multiple times, each time is recorded as a separate ALT.

Opportunities to improve ALT often lie in predicting and prefetching additional content. The overall PPS can also be improved by balancing how much content to load in initial load vs additional loads.

This GIF demonstrates ALT (marked when the loading indicator at the bottom is replaced by paginated content loaded from the network).

![]()

## Rich Content Load Time (RCLT)

RCLT measures how long a user sees a placeholder or a loading indicator until an image, a video, or some rich media content is fully displayed. ImageView and other rich media containers implement the same LoadableView API to report loading state changes to the PPS logger.

To improve RCLT, we look to reduce image size, improve image caching, optimize image formats and serving, strategically schedule loading rich content that is not yet on screen, and select performant streaming libraries, etc.

This GIF demonstrates RCLT (marked when the place holders are replaced with actual images loaded from the network).

![]()

# Conclusion

We successfully built an instrumentation framework on Android to capture much richer and user-centric performance metrics, guided by the same design principles in Airbnb’s Page Performance Score across web and native platforms. On top of this framework and the data collected, we built out dashboards to monitor performance across the entire app, set up automatic alerts targeting page owners, streamlined performance goal setting at team and org levels, and systematically tracked and mitigated performance regressions.

In 2022, we plan to improve the granularity and accuracy of our instrumentations such as measuring tap responsiveness, better differentiating performance during scrolling, and providing primitives with built-in performance optimizations. We will also devote resources to build tooling to improve debuggability, and enable early regression detection and prevention via synthetic testing.

PPS gives our engineers and data scientists better insights and more ways to improve our products. It also strengthens our Commitment to Craft culture. We hope that you apply these learnings in your organization as well.

## Appreciations

Thank you to everyone who has helped build PPS on Android: Eli Hart, Charles Xue, Nick Miller, Andrew Scheuermann, Antonio Niñirola, Josh Nelson, Aditya Punjani, Josh Polsky, Jean-Nicolas Vollmer, Wensheng Mao and everyone else who helped along the way.

Interested in working at Airbnb? Check out these roles:
Staff Android Engineer
Senior Android Engineer 
Senior Android Engineer
Android Engineer, Special Projects

## 中文

**Airbnb Android 页面性能评分（PPS）**

Airbnb 自研的页面性能评分（PPS）旨在通过收集多种以用户为中心的性能指标并将其汇总为单一的 0-100 分数，来捕捉性能的丰富性和复杂性。本文深入解析了 PPS 在 Android 上的定义和实现方式。

**检测**

整个 Airbnb 客户旅程被划分为不同的页面，每个页面都有自己独立的 PPS 评分。在 Android 上，页面与 Fragment 相关联，每个 Fragment 必须提供一个 LoggingConfig 对象来指定页面名称。

**用户感知的等待时间**

PPS 的关键差异化在于它测量的是用户可以看到的等待时间。PPS 测量用户在屏幕上看到加载指示器的持续时间，而传统 TTI 指标测量的是代码执行时间和异步调用长度。

**LoadableView 接口**

为了捕获视觉上感知的等待时间，所有具有加载状态的视图都需要实现一个报告其加载状态变化的 API。Airbnb 创建了一个名为 LoadableView 的简单接口，并提供了 Base ViewGroup、Base TextView 和 Base ImageView 等基元，它们都实现了 LoadableView 接口。

**指标实现**

TTFL（首次布局时间）：测量用户看到屏幕上任何内容所需的时间。
TTIL（初始加载时间）：测量用户看到加载指示器到显示有意义内容的时间。
MTH（主线程挂起）：当任何帧渲染耗时超过系统帧刷新率两倍时触发。
ALT（额外加载时间）：初始加载后发生的任何等待时间，如列表分页。
RCLT（富内容加载时间）：用户看到占位符到图片、视频或其他富媒体完全显示的时间。

**结论**

Airbnb 在 Android 上成功构建了一套检测框架，基于与其他平台相同的 PPS 设计原则，捕获了更丰富、以用户为中心的性能指标。
