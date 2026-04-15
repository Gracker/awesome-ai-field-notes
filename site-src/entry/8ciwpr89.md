---
title: 'Android Studio  的 AI  Agent 有什么特别？未来会有惊艳什么功能？'
sidebar: false
---

::: info
[← 返回智能体](/agents)
:::

# Android Studio  的 AI  Agent 有什么特别？未来会有惊艳什么功能？

> 关于 AI Agent 的收藏文章

🔗 [原文链接](https://mp.weixin.qq.com/s?__biz=Mzg3NTA3MDIxOA==&mid=2247495598&idx=1&sn=14cd8f9ec25389d6dac961161e02c8dd&chksm=cfa670e94d62461ea809888f491246dc145a67e574325e765a86b94094dddb3757373348a788&mpshare=1&scene=1&srcid=01045ZRrXGuhBGBbkwMFi6ZQ&sharer_shareinfo=72c66741b7649e58bdab5c63ff574369&sharer_shareinfo_first=72c66741b7649e58bdab5c63ff574369) | 🌐 | ⭐⭐⭐⭐ 4 ⭐4 4/5 📅 2026-01-04

`Agent` `Prompt Engineering` `Android` `MCP`

---

# Android Studio  的 AI  Agent 有什么特别？未来会有惊艳什么功能？

> 公众号: GSYTech
> 发布时间: 1970-01-01 08:33:46
> 原文链接: https://mp.weixin.qq.com/s?__biz=Mzg3NTA3MDIxOA==&mid=2247495598&idx=1&sn=14cd8f9ec25389d6dac961161e02c8dd&chksm=cfa670e94d62461ea809888f491246dc145a67e574325e765a86b94094dddb3757373348a788

---
相信大家都在之前的 《Android Studio Otter 2 Feature 发布》已经了解过，为什么这是一个比较值得更新的 Android Studio 版本，与此同时，谷歌也和我们展示了未来（Canary）全新的 AI Agent 有什么特别之处。

对于一个 AI Agent 来说，最重要的有三个基础概念：**工具 (Tools)**、**上下文 (Context)**和 **MCP (模型上下文协议)**，而大多数人对于它们的理解，可能还比较片面。

比如工具 ，**实际上 AI Agent 不只是一个聊天场景，更多是 Agent 通过“工具”来执行任务**，而不是单纯用来做文本回复，最重要的是，Agent 不会将整个代码库发送给模型，毕竟这太浪费 token ，而且还慢，事实上它只是根据用户的 Prompt（提示词），自行决定调用哪些工具 。

比如一般内置的有包括 `Find Files`（查找文件）、`read_file`（读取文件）、`version_lookup`（版本查询）、`gradle_sync`等等，例如：

> ❝
>
> 开发者询问：“主题在哪里定义？”，Agent 会推断并使用 `Find Files`搜索 `theme.kt`，而不是扫描所有文件 ![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/j9CXw3c38v7YgbtR7uv8361oUaVxEavFf5gEkq5rndWz7xakwPickuvppPxGly4l1pZntTNskV5n9yZKr9dBFGQ/640?wx_fmt=png&from=appmsg#imgIndex=0)

你也可以通过收入 `/tools`让 AI 展示现在存在的工具：

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/j9CXw3c38v7YgbtR7uv8361oUaVxEavFXtoP93qiaVvBUJdMjvvVBAaQ3pEI0s0qJlyQmLqle2sZ7ed93YkOWibg/640?wx_fmt=png&from=appmsg#imgIndex=1)

另外的工具就是 \*\*Android 知识库 (Knowledge Base)\*\*：为了解决大模型数据滞后的问题，例如不知道最新的 Navigation 3 API 等场景，Android Studio 集成了 `search_android_docs`工具，它允许 Agent 搜索 Android 文档、Firebase 和 Kotlin 的最新资料等。

> ❝
>
> 所以官方建议，**需要是可以在 Prompt 中加上“check the docs”（检查文档），增加触发工具执行的概率**。

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/j9CXw3c38v7YgbtR7uv8361oUaVxEavF6ytVNKh1pBCnsEO5fTBaJicOJHHyicPGxEFFpSyLpaHPnliaacBs7tpiaQ/640?wx_fmt=png&from=appmsg#imgIndex=2)

> ❝
>
> 有了知识库之后，以后就算不更新 Android Studio ，AI 也可以通过最新知识库获取到最新的 API 和文档。

而对于 (MCP - Model Context Protocol)，作为模型上下文协议 ，**它属于扩展能力，可以让开发者连接外部服务**，比如和 Figma 集成，连接本地运行的 Figma MCP 服务器，开发者可以直接在 IDE 中要求 Agent “截取我在 Figma 中选中的内容并转换当前屏幕”，从而打通设计与开发的流程 ：

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/j9CXw3c38v7YgbtR7uv8361oUaVxEavFl3LNQ4pVVdUOeHk1UtWZ4kkS4wJnn6wxovTsLBbibusIOKcHxv2ZWAw/640?wx_fmt=png&from=appmsg#imgIndex=3)![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/j9CXw3c38v7YgbtR7uv8361oUaVxEavFVv1p8OSjNibkchxOQzpO7ibNwdpD7uf2QhYKQXSpucu0ALcZHD69o1ibw/640?wx_fmt=png&from=appmsg#imgIndex=4)![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/j9CXw3c38v7YgbtR7uv8361oUaVxEavFmqEiciaibvpoIfYEUXTszD3icf0tiaGC8pg5fic3oBzDaldFqmEeo4oW4wjg/640?wx_fmt=png&from=appmsg#imgIndex=5)

而 Context 则是用于智能感知， Agent 能够自动获取项目名称、当前打开的文件等信息作为上下文 ，而一般开发过程中，推荐用户添加自己的规则或者偏好，避免 AI 过度自我发挥，例如：

-   **agents.md**：团队共享的标准文件，可以在其中定义项目架构（如 Hilt）、代码风格或业务描述，Agent 会在执行任务时读取文件保持一致性

-   **层级结构**：Agent 会从当前目录向上递归查找所有 `agents.md`文件，允许在不同模块（如 data 模块）定义不同层级的上下文


![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/j9CXw3c38v7YgbtR7uv8361oUaVxEavFoia5k99rialrkkTftKtZef9wWBXM0DDaia2R6s1CV1iaUyUABG1ehBRsbQ/640?wx_fmt=png&from=appmsg#imgIndex=6)![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/j9CXw3c38v7YgbtR7uv8361oUaVxEavFKIKZY4857mAnU8cXBTxqia05ScFCCn79r8dAxaM0Geuia1eL6I0g1StQ/640?wx_fmt=png&from=appmsg#imgIndex=7)

而官方也演示了覆盖从“从零创建”到“微调完善”的 UI 开发全流程，注意这里用的也是 Canary 版本：

-   通过自然语言 Prompt 生成完整的应用原型，Agent 会先生成一个计划（包含库和工具），用户确认后，它会生成 ViewModels、Compose UI 代码甚至单元测试

    ![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/j9CXw3c38v7YgbtR7uv8361oUaVxEavFhNul8GNAupg1icricrYWBGTMOYSXxDF4pDrAxx8uicIiamsLQhNEicZa8Lg/640?wx_fmt=png&from=appmsg#imgIndex=8)![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/j9CXw3c38v7YgbtR7uv8361oUaVxEavFuxzLQJCNmarjWqpA71KruWvJ8ibOKL6U3tM4dibFiajvvBN8dG5Q3PHtA/640?wx_fmt=png&from=appmsg#imgIndex=9)

-   之后用户可以将 UI 截图拖入会话，Agent 会分析并生成对应的 Jetpack Compose 代码 ，这个过程它会尝试重用现有组件，如果缺少资源（如特定图标），它甚至会尝试生成新的 Vector Drawable![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/j9CXw3c38v7YgbtR7uv8361oUaVxEavFfmNcibmfYF5bVDcVt515IXQLxehkAxrETWnMOskjo2Qv8xhDy49ro0g/640?wx_fmt=png&from=appmsg#imgIndex=10)

    ![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/j9CXw3c38v7YgbtR7uv8361oUaVxEavFadibIdV6o2eZv04uibvsicfbK4rTFVeG8ZcZ29AtvNrt6kYTYYXz4lMEA/640?wx_fmt=png&from=appmsg#imgIndex=11)![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/j9CXw3c38v7YgbtR7uv8361oUaVxEavFjVUrHUJ6WEAzEQhbtKiagyr7jJeMz1YEn5tvJp9tfKSicORMU4v6bdJg/640?wx_fmt=png&from=appmsg#imgIndex=12)

-   接着就是代码分析与修复，利用 IDE 现有的 Lint 和静态分析能力，通过 AI 自动修复问题（如未使用的导入、弃用的 API），避免运行耗时的 Gradle 构建 ![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/j9CXw3c38v7YgbtR7uv8361oUaVxEavFtOU2y0rjRrvWwCw7ibmPtibfVlH9HQsty45iaCbAf73dVU95SA5wdxqzQ/640?wx_fmt=png&from=appmsg#imgIndex=13)

-   然后是 UI 匹配，当现有组件需要根据新设计图进行迭代时使用，用户上传新设计图，Agent 会分析差异并自动调整现有代码从而匹配新设计 ![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/j9CXw3c38v7YgbtR7uv8361oUaVxEavFZjibp4jEz1rVaxpm7XWzNSDqyibJbxonYWGlR1n0afuR7Aq8Zh5wZmAw/640?wx_fmt=png&from=appmsg#imgIndex=14)

-   然后是预览，Agent 会调用 `Render Compose Preview`工具在聊天窗口中直接渲染预览，从而验证修改是否正确且可编译 ![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/j9CXw3c38v7YgbtR7uv8361oUaVxEavFGuRnvookaj8CjrmVVJCfYSicpcwawgcVwSIFemp5Kqq9Psc2Nf7zJqg/640?wx_fmt=png&from=appmsg#imgIndex=15)

-   接着就是通过自然语言指令修改 UI，比如输入“左对齐设置、增大字体、添加柔和的渐变背景”，Agent 会将这些指令转化为代码修改

-   最后结合 UI Check 模式（用于检测可访问性、屏幕适配等问题），当 UI Check 检测到“颜色对比度不足”时，用户可以点击“Fix with AI”，Agent 会自动寻找合适的颜色代码并修复该可访问性问题，最后重新运行检查以确保问题已解决 ![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/j9CXw3c38v7YgbtR7uv8361oUaVxEavFg1AkR1UAbVKrWibOdsaVxx7x4jM9c43JfPR3NtOx93mgg9ibjHCnCliaQ/640?wx_fmt=png&from=appmsg#imgIndex=16)![image-20251223112251073](https://mmbiz.qpic.cn/sz_mmbiz_png/j9CXw3c38v7YgbtR7uv8361oUaVxEavF0E96VjWEx0Wp4HF7aaGxuib12HKrU3FR6w4UeHUjWPmsJug3G2iaVyTg/640?wx_fmt=png&from=appmsg#imgIndex=17)


可以看到，未来的 Android Studio Agent 会有更加丰富的多模态处理能力，比如更好的设计稿理解，图片理解，可以做到设计图和现有 UI 的差异识别并进行改动，甚至直接生成预览效果，同时还支持 UI 检测等，对于 Android 开发者来说，以后也许真的就是动动嘴皮子而已。

> ❝
>
> 对于 android 开发者来说， AI Agent 的 Android Studio 体验实际会比 antigravity 更好？

# 参考链接

https://www.youtube.com/watch?v=jTlW8JeCClA
