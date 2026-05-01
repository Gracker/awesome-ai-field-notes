# Google Gemini 如何加速 Android 开发？近些年，基于大模型的人工智能发展迅猛，OpenAI 有 Ch

> 发布时间: 2025-02-17T03:05:27.000Z
> 原文链接: https://juejin.cn/post/7472037829506383906

---






# Google Gemini 如何加速 Android 开发？

[朱涛的自习室](/user/2119514149637032/posts)

2025-02-17 3,049 阅读6分钟

专栏：

沉思录

已关注

> 往期文章：
>
> [《00. 文章合集目录》](https://juejin.im/post/6844904191089999886 "https://juejin.im/post/6844904191089999886")
>
> [《10. 揭秘 Compose 原理》](https://juejin.cn/post/7103336251645755429 "https://juejin.cn/post/7103336251645755429")
>
> [《2 小时入门 Jetpack Compose》](https://juejin.cn/post/7105939934527094798 "https://juejin.cn/post/7105939934527094798")
>
> [《深入理解 Jetpack Lifecycle（原理篇）》](https://juejin.cn/post/7470916546283864115 "https://juejin.cn/post/7470916546283864115")

你好，我是朱涛。今天我们来聊聊 AI 和 Android 开发。近些年，基于大模型的人工智能发展迅猛，OpenAI 有 ChatGPT，国内有 Deepseek。然后，我因为和 Google 接触比较多，有幸成为了 Gemini 的第一批使用者，这些年一直用下来，感觉也非常不错。

Android Studio 在最新的版本迭代中，也在积极引入 Gemini 来强化它的 AI 辅助功能。我收到 Android 团队的推广邮件后，第一时间就下载体验了起来。

现在我来跟大家简单介绍下 Android Studio 的 AI 辅助功能，以及我的使用体验。

## 第一步：下载 Android Studio 预览版 & 配置

![image.png](images/img_001.jpg)

最新的 Android Studio 版本是 Meerkat，也就是我们熟悉的“蒙哥”。

![image.png](images/img_002.jpg)

接着，打开 Android Studio，我们就可以开始配置 Gemini 了。具体路径是：**View > Tool Windows > Gemini**；

![image.png](images/img_003.jpg)

这时候，会要求你登录自己的 Google 账户。

![image.png](images/img_004.jpg)

当前 Gemini AI 辅助功能还处于 preview 阶段，我们是可以免费试用的。需要注意的是，由于 Gemini 服务是由 Google 提供的，我们在国内使用需要通过**科学上网**的途径。

Google 还是非常注重隐私的，在你完成账号登录后，会让你选择：隐私模式；

![image.png](images/img_005.jpg)

如果你对 AI 编程工具不熟悉，上面的几个选项可能会让你懵掉，我来简单解释下：

-   第一个选项：Gemini 默认会访问你所有工程里的代码文件，通过理解你的工程，可以让 Gemini 的回答更加精确；我个人是不推荐选第一个的；
-   第二个选项：每次打开新的工程，都会询问。
-   第三个选项：不访问工程任何代码文件。

我个人是使用的**第二个选项**：每个工程都询问我。

那么，什么样的工程可以让 Gemini 访问所有的代码文件呢？我的理解是：

-   如果整个代码工程都属于你，并且你说了算，并且你愿意让 Gemini 访问你的代码，那就可以开启；
-   如果代码工程不属于你，比如是公司的项目，那么**千万不要**开启这个功能；

配置完这个选项后，我们就可以开始体验 AI 辅助编程了。

## 上手体验

Gemini 集成到 Android Studio 后，可以为我们做什么呢？

### 简单问答：

首先，从 Gemini 默认界面可以看到。它是一个对话模式的 UI，如果你用过 ChatGPT 对这个应该就不会感到陌生。在大模型领域，我们向 AI 提问，被称作：“Prompt”，中文一般叫做“提示词”。

![image.png](images/img_006.jpg)

可以看到，默认情况下，官方给我们提供了一些示例“提示词”。

这属于最基础的功能，如果要以问答的方式来跟 Gemini 交流，并不一定非要在 Android Studio 里面，我们在网页里一样可以。

我们来看一下 Gemini 在 Android Studio 当中独家的功能吧。

### AI 智能诊断

当我们的 Android 工程在 sync 或者编译过程中遇到报错，我们最常的做法就是拷贝报错日志，然后去网页里找答案。

有了 Gemini 后，我们可以直接点击：“Ask Gemini”。

举个例子，我在写教程的过程中，用的 HelloWorld 工程在 Sync 的时候遇到了问题。

![image.png](images/img_007.jpg)

我点击“Ask Gemini”以后，它立马就诊断出了原因，并且给出了详细的解决方法：清空缓存+重启。

我清空缓存后，问题也顺利得到了解决，点赞！

![image.png](images/img_008.jpg)

## 快捷入口

Gemini 集成到 Android Studio 后最大的优势，就是可以灵活的在右键菜单里访问。

针对一段代码，我们可以选中，然后让 AI 为我们解释，也可以让 AI 帮我们改进。

在我们写代码的时候，给变量起名字有时候也很头疼，这件事就交给 AI 吧。

![image.png](images/img_009.jpg)

Google 把 Gemini 深度集成到 AS 当中后，这些功能都可以非常方便的访问了。这里我就不对这些小功能一一演示了。

这里我拿一个问题来考考 Gemini 吧，问题不算难，但对 AI 还是挑战性的，我们来看看 Gemini 能做到什么程度。

### 考考 Gemini：代码改进

kotlin

 体验AI代码助手

 代码解读

复制代码

`// Can you identify the problem with this code and suggest improvements? class User {     var name: String?     var age: Int?     var address: String? }`

Gemini 返回结果非常快，立马分析出了这段代码中的问题：

vbnet

 体验AI代码助手

 代码解读

复制代码

`Problems with the Current Code Nullability: The use of nullable types (String?, Int?) implies that a User object might not have a name, age, or address. While this might be valid in some scenarios, it often leads to the following problems: Lack of Initialization: The properties are declared but not initialized. This means they will have a null value by default, making the nullability issue even more prominent. Mutability: While the need for var (mutable) is not inherently a problem, it's worth considering whether these properties need to be mutable. If a user's name, age, or address rarely or never changes after creation, using val (immutable) might be a better choice. Immutability can simplify reasoning about your code and avoid unexpected side effects.`

针对上面的问题，Gemini 也立马给出了两个可选的改进方向：

第一个是：确保空安全 + 默认值；

![image.png](images/img_010.jpg)

第二个是：确保空安全 + 限制不变性；

![image.png](images/img_011.jpg)

熟悉 Kotlin 的同学肯定知道这不是完美答案，但总体也能打个 70 分了。

然后，我又尝试给了下提示，让 Gemini 往 Data Class 的方向思考。

![image.png](images/img_012.jpg)

这时候 Gemini 卡壳了……只是扔给我了一堆的参考链接。这不太应该，我猜测 Android Studio 接入的 Gemini 还不是 Google 家的最强版本，于是尝试套取它的信息。

![image.png](images/img_013.jpg)

可以看到，目前 Android Studio 里用的还是 Gemini 1.5 Pro，希望能让我早日用上 Gemini 2.0~

## 总结 & 警告

现阶段，我们人类距离 AGI 的终极目标还有一段距离，但 AI 已经可以帮我们完成一些简单的任务了。如果将一些初级的编程任务交给 AI，AI 也可以帮我们完成的很好。

但从我目前观察到的情况来说，不管是 Android Studio 的 Gemini，还是业界最强的 Cursor，这些 AI 工具都无法胜任中高级编程任务。但也许，在不远的未来，就会有足够牛逼的 AI 编程机器人出现了。

不管怎么样，我们作为 Android 程序员，现阶段去积极了解和使用 Gemini，也是个非常不错的事情。毕竟我们没有额外的使用成本(不花钱，用起来也不费劲)。虽然 Gemini 现阶段还比不上经验丰富的程序员，但有的时候它确实可以给我一些惊喜，让人眼前一亮。

最后，如果你打算在 Android 项目中尝试 AI 辅助功能，除了我在前面提到的问题外，你还需要提防 AI 有时候会：**一本正经的胡说八道**。

所以，`对于 AI 生成的代码，你一定要小心 review 再合并到工程里`。

好啦，今天的内容就到这了，后续我应该还会出一期专门的 AI 编程工具评测文章，到时候我们来看看 Gemini 的上限到底在哪里。

我们下一篇文章再见啦~