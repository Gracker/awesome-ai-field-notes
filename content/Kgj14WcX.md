---
title: "Android CLI: Build Android apps 3x faster using any agent"
source: "rss"
category: "tech"
feed: "rss_android_developers_blog_33800553"
group: "Articles/Android 开发者/Android Developers Blog"
url: "http://android-developers.googleblog.com/2026/04/build-android-apps-3x-faster-using-any-agent.html"
published: "2026-04-16T17:00:00Z"
captured_at: "2026-04-17T03:02:22+08:00"
tags: ["rss", "rss/tech", "rss/Articles"]
---
# Android CLI: Build Android apps 3x faster using any agent
原文链接：<http://android-developers.googleblog.com/2026/04/build-android-apps-3x-faster-using-any-agent.html>
来源：rss_android_developers_blog_33800553｜Articles/Android 开发者/Android Developers Blog
发布时间：2026-04-16T17:00:00Z
抓取时间：2026-04-17 03:02:22

---

Title: Android CLI: Build Android apps 3x faster using any agent

URL Source: http://android-developers.googleblog.com/2026/04/build-android-apps-3x-faster-using-any-agent.html

Markdown Content:
[![Image 1](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiSxFmgZy6aUj2hWhz_Q7GYVfVjlVJ5kTKte7b_GfNnV6Bde-1UDSBiOmDuq7sEPHJX4SULxETyP5DYjBh9NKGJ8TDfJD4kvUJYHPpVGE44k0Tw9EkH3-jCTChnTLvc-TeGH1PWPhdpXRtn6ly0iAkQ5dIS9wHXsWAVuv0wPzumJ41YhYqdcia5DmnOOWs/s16000/hours-CLI_Dark-Blogger@2x.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiSxFmgZy6aUj2hWhz_Q7GYVfVjlVJ5kTKte7b_GfNnV6Bde-1UDSBiOmDuq7sEPHJX4SULxETyP5DYjBh9NKGJ8TDfJD4kvUJYHPpVGE44k0Tw9EkH3-jCTChnTLvc-TeGH1PWPhdpXRtn6ly0iAkQ5dIS9wHXsWAVuv0wPzumJ41YhYqdcia5DmnOOWs/s8419/hours-CLI_Dark-Blogger@2x.png)

As Android developers, you have many choices when it comes to the agents, tools, and LLMs you use for app development. Whether you are using Gemini in Android Studio, Gemini CLI, Antigravity, or third-party agents like Claude Code or Codex, our mission is to ensure that high-quality Android development is possible everywhere.

Today, we are introducing a new suite of [Android tools and resources for agentic workflows](http://d.android.com/tools/agents) — **Android CLI** with **Android skills** and the **Android Knowledge Base**. This collection of tools is designed to eliminate the guesswork of core Android development workflows when you direct an agent’s work outside of Android Studio, making your agents more efficient, effective, and capable of following the latest recommended patterns and best practices.

Whether you are just starting your development journey on Android, are a seasoned Android developer, or managing apps across mobile and web platforms, building your apps with the latest guidance, tools, and AI-assistance is easier than ever. No matter which environment you begin with these resources, you can always transition your development experience to Android Studio—where the state-of-the-art tools and agents for Android development are available to help your app experience truly shine.

## (Re)Introducing the Android CLI

Your agents perform best when they have a lightweight, programmatic interface to interact with the Android SDK and development environment. So, at the heart of this new workflow is a revitalized Android CLI. The new Android CLI serves as the primary interface for Android development from the terminal, featuring commands for environment setup, project creation, and device management—with more modern capabilities and easy updatability in mind.

![Image 2](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhoTdXwtVvAkXKpJkFXWz5-kJFAVniISQ2L9MbTSaMU4A5-wlpDHXpwJwFNc4-wTPkC9k_H2dnEsWUWVeeKxBEikTv1mDNhm18H3wvd53Zo5Z4uzu7AnHoNKIxz_9Op6_6kAJyuo-do6oDviIlrNcIZ49X5wLz79OdSvx6Ru0SDb403WA3-u-3WbLd-jz4/w640-h414/android-create-project.gif)

_The create command makes an Android app project in seconds._

In our internal experiments, Android CLI improved project and environment setup by reducing LLM token usage by more than **70%**, and tasks were completed **3X faster** than when agents attempted to navigate these tasks using only the standard toolsets.

Key capabilities available to you include:

*   **SDK management:** Use `android sdk install` to download only the specific components needed, ensuring a lean development environment.
*   **Snappy project creation:** The `android create` command generates new projects from official templates, ensuring the recommended architecture and best practices are applied from the very first line of code.
*   **Rapid device creation and deployment:** Create and manage virtual devices with `android emulator` and deploy apps using `android run`, eliminating the guesswork involved in manual build and deploy cycles.
*   **Updatability:** Run `android update` to ensure that you have the latest capabilities available.

![Image 3](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhpB1xUU8XmJKqlmou9A8lwdo9ZP_RZpjgX-MTjobIQD6h_IwzwsNMPxX-vnGDrWIJGrAiJ3DTw1qOyoGLWmkdhYdlBNyQseY3zrvR0Y5BA7In-CmCbIz5_F1D_HBoBcdWUbHGGeb59I_Db2Q8XRX7fNuNY7vK2cPBrlPHISSJ0vP3ZLNe7vYorXLCbSkQ/w640-h388/android-run-short.gif)

_Android CLI can create a device, run your app on it, and make it easier for agents to navigate UI._

While Android CLI will empower your agentic development flows, it’s also been designed to streamline CI, maintenance, and any other scripted automation for the increasingly distributed nature of Android development. [Download](https://d.android.com/tools/agents) and try out the Android CLI today!

## Grounding LLMs with official Android Skills

Traditional documentation can be descriptive, conceptual, and high-level. While perfect for learning, LLMs often require precise, actionable instructions to execute complex workflows without using outdated patterns and libraries.

To bridge this gap, we are launching the **Android skills GitHub repository**. Skills are modular, markdown-based (`SKILL.md`) instruction sets that provide a technical specification for a task and are designed to trigger automatically when your prompt matches the skill's metadata, saving you the hassle of manually attaching documentation to every prompt.

Android skills cover some of the most common workflows that some Android developers and LLMs may struggle with—they help models better understand and execute specific patterns that follow our best practices and guidance on Android development.

In our initial release, the repository includes skills like:

*   Navigation 3 setup and migration.
*   Implementing edge-to-edge support.
*   AGP 9 and XML-to-Compose migrations.
*   R8 config analysis, and more!

If you’re using Android CLI, you can browse and set up your agent workflow with our growing collection of skills using the `android skills` command. These skills can also live alongside any other skills you create, or third-party skills created by the Android developer community. Learn more about getting started with [Android skills](http://d.android.com/tools/agents/android-skills).

_[![Image 4](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEieOsGKPV8IWBw6gr6\_lQNapUMgaBl9pds0N8i-VamNCA3Sa7Klpz3DZJGJBZYw12pBAH0Xzypo6z4ujF16rK8wcQkKenJ5z5w4Rmx7pCGEo-paWnmdVm64DURt8r6o\_DhZactfiKApRsVeGilvbotWpCMNrY6xfLv2hHuE8TIoiluIGkemrPReKbFdi2Y/w640-h390/gemini\_cli\_skills\_demo.gif)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEieOsGKPV8IWBw6gr6\_lQNapUMgaBl9pds0N8i-VamNCA3Sa7Klpz3DZJGJBZYw12pBAH0Xzypo6z4ujF16rK8wcQkKenJ5z5w4Rmx7pCGEo-paWnmdVm64DURt8r6o\_DhZactfiKApRsVeGilvbotWpCMNrY6xfLv2hHuE8TIoiluIGkemrPReKbFdi2Y/s1720/gemini\_cli\_skills\_demo.gif)_

_Install Android skills via the Android CLI to make your agent more effective and efficient._

## The latest guidance via the Android Knowledge Base

The third component we are launching today is the **Android Knowledge Base**. Accessible through the `android docs` command and already available in the latest version of Android Studio, this specialized data source enables agents to search and fetch the latest authoritative developer guidelines to use as relevant context.

_[![Image 5](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhaUMd35EkvnwxfIZGlqRc961d9mfYaR4Fj5FWH4QZgMc4Nmip4VnbRtz8a94XJUkfU3OfAsXyPJbOzc6ZFjnCMLbQDLYF7Abwn-eYRJxfQzjesIYsT-GzSHHK7BefCYyoG\_r-sXCuGrN3N2-5BD8vHXi1jiY6nxqjsJVOk7k\_zQeymsXZxXJGLazYl0Mc/w640-h414/android-docs.gif)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhaUMd35EkvnwxfIZGlqRc961d9mfYaR4Fj5FWH4QZgMc4Nmip4VnbRtz8a94XJUkfU3OfAsXyPJbOzc6ZFjnCMLbQDLYF7Abwn-eYRJxfQzjesIYsT-GzSHHK7BefCYyoG\_r-sXCuGrN3N2-5BD8vHXi1jiY6nxqjsJVOk7k\_zQeymsXZxXJGLazYl0Mc/s960/android-docs.gif)_

_The Android Knowledge Base ensures agents have the latest context, guidance, and best practices for Android._

By accessing the frequently updated knowledge base, agents can ground their responses in the most recent information from Android developer docs, Firebase, Google Developers, and Kotlin docs. This ensures that even if an LLM's training cutoff is a year old, it can still provide guidance on the latest frameworks and patterns we recommend today.

## Android Studio: The ultimate destination for premium apps

In addition to empowering developers and agents to handle project setup and boilerplate code, we’ve also designed these new tools and resources to make it easier to transition to Android Studio. That means you can start a prototype quickly with an agent using Android CLI and then open the project in Android Studio to fine-tune your UI with visual tools for code editing, UI design, deep debugging, and advanced profiling that scale with the growing capabilities of your app.

_[![Image 6](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgY2zZ9qSUFIGHwcQTuzv0AVfn3brHhtlswBI4xcTYeWe2q1lAxliPZB8rEipSJJh6TBkRRLscjcSDDkDATz-lOAduKsPHQAnmrEVExGvLUTyiCe5vcjevioP5w\_D7Ra4CkfHzp2LJjwTUkmBVL2DaKgZBGmDf0Fp97HuD9chWqEkw\_EKf1JGIio7XkSAw/w640-h414/android\_studio.gif)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgY2zZ9qSUFIGHwcQTuzv0AVfn3brHhtlswBI4xcTYeWe2q1lAxliPZB8rEipSJJh6TBkRRLscjcSDDkDATz-lOAduKsPHQAnmrEVExGvLUTyiCe5vcjevioP5w\_D7Ra4CkfHzp2LJjwTUkmBVL2DaKgZBGmDf0Fp97HuD9chWqEkw\_EKf1JGIio7XkSAw/s960/android\_studio.gif)_

And when it is time to build a high-quality app for large-scale publication across various device types, our agent in Android Studio is here to help, while leveraging the latest development best practices and libraries. Beyond the powerful Agent and Planning Modes for active development, we have introduced an AI-powered New Project flow, which provides an entry point to rapidly prototyping your next great idea for Android.

[![Image 7](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjKwNpNC5C4U6dSTNgcALp7tO4a1MyAl-d-pk5fGngCvZdhPHGb8iudfb73t3s5rln5wrckxOly6hACWyuOUuVOcDADVVg9MZtaS58_d4q-O-63fLftSnbU_u89lKF7p8LXDKx4kEmzKzzz_Mokjf53JLzBNhkgky1JgJDziJ6icJhFjXy1PlFdEd1ni4U/s16000/Workout-app.gif)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjKwNpNC5C4U6dSTNgcALp7tO4a1MyAl-d-pk5fGngCvZdhPHGb8iudfb73t3s5rln5wrckxOly6hACWyuOUuVOcDADVVg9MZtaS58_d4q-O-63fLftSnbU_u89lKF7p8LXDKx4kEmzKzzz_Mokjf53JLzBNhkgky1JgJDziJ6icJhFjXy1PlFdEd1ni4U/s1920/Workout-app.gif)

These built-in agents make it simple to extend your app ideas across phones, foldables, tablets, Wear OS, Android Auto, and Android TV. Equipped with full context of your project’s source code and a comprehensive suite of debugging, profiling, and emulation tools, you have an end-to-end, AI-accelerated toolkit at your disposal.

## Get started today

Android CLI is available in preview today, along with a growing set of Android skills and knowledge for agents. To get started, head over to [d.android.com/tools/agents](http://d.android.com/tools/agents) to download Android CLI.