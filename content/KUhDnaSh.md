# 【有嘴就能做开发】Cursor——AI编辑器 使用详解

> 作者: unknown
> 发布时间: 编辑于 2025-03-01 23:45・浙江
> 原文链接: https://zhuanlan.zhihu.com/p/27335614120

---
## 概述

![](https://pic4.zhimg.com/v2-e16ddecead14b9bf72ee911ae24568b3_1440w.jpg)

https://www.cursor.com

## [Cursor](https://zhida.zhihu.com/search?content_id=254489801&content_type=Article&match_order=1&q=Cursor&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzY0MjkwMzQsInEiOiJDdXJzb3IiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNTQ0ODk4MDEsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.SrjK7L1u0BnnIjTmWmULRA8KKDBawJPHrOnX39I_mOU&zhida_source=entity)是什么？

Cursor是一款优秀的AI代码编辑器，它内置了[Deepseek-R1](https://zhida.zhihu.com/search?content_id=254489801&content_type=Article&match_order=1&q=Deepseek-R1&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzY0MjkwMzQsInEiOiJEZWVwc2Vlay1SMSIsInpoaWRhX3NvdXJjZSI6ImVudGl0eSIsImNvbnRlbnRfaWQiOjI1NDQ4OTgwMSwiY29udGVudF90eXBlIjoiQXJ0aWNsZSIsIm1hdGNoX29yZGVyIjoxLCJ6ZF90b2tlbiI6bnVsbH0.EXFpSax-zjNwJu4X2jl2OeAheT3zvt53IFLxQ5Vr4G8&zhida_source=entity)、[GPT-4](https://zhida.zhihu.com/search?content_id=254489801&content_type=Article&match_order=1&q=GPT-4&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzY0MjkwMzQsInEiOiJHUFQtNCIsInpoaWRhX3NvdXJjZSI6ImVudGl0eSIsImNvbnRlbnRfaWQiOjI1NDQ4OTgwMSwiY29udGVudF90eXBlIjoiQXJ0aWNsZSIsIm1hdGNoX29yZGVyIjoxLCJ6ZF90b2tlbiI6bnVsbH0.g4938J58ojJcK_HQ6Fmd63IAwTcpaHXHWVom4d8ECz8&zhida_source=entity)、[Claude](https://zhida.zhihu.com/search?content_id=254489801&content_type=Article&match_order=1&q=Claude&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzY0MjkwMzQsInEiOiJDbGF1ZGUiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNTQ0ODk4MDEsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.rHRCTTVBdQUaJbuN35zxk8G03FaawgnGUy6rS1UdlrM&zhida_source=entity)等AI模型。

简单说，就是：

**Cursor = VS Code编辑器 + AI大模型 + Cursor功能特性**（代码补全、文件编辑等）

它可以：

-   **智能补全代码**
-   **解释代码**
-   **定位Bug**
-   **AI大模型问答**
-   **文本编辑**

更重要的是，它可以：

-   **根据自然语言，生成代码**

这一点，非常利好“不懂编程，但是有开发想法”的人。

## 发展历程

![](https://pica.zhimg.com/v2-30d29dd10e7afdc908460e51abb83d2e_1440w.jpg)

-   2022年，4位在麻省理工学院相识的朋友：Aman、Avrid、Michael、Sualeh，创立了一家名为[Anyshpere](https://zhida.zhihu.com/search?content_id=254489801&content_type=Article&match_order=1&q=Anyshpere&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzY0MjkwMzQsInEiOiJBbnlzaHBlcmUiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNTQ0ODk4MDEsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.AkaSZnLNdVh9qnHvX9jZ6vOOo30STlvZxkZP2Mq0L7o&zhida_source=entity)的公司，目标是开发由AI驱动的代码编辑器。
-   2023年1月，Cursor正式发布。
-   同年，获得了由[OpenAI创业基金](https://zhida.zhihu.com/search?content_id=254489801&content_type=Article&match_order=1&q=OpenAI%E5%88%9B%E4%B8%9A%E5%9F%BA%E9%87%91&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzY0MjkwMzQsInEiOiJPcGVuQUnliJvkuJrln7rph5EiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNTQ0ODk4MDEsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.c6nFpErTeW2qTjDQb6evzCQL07KcbQLNactNf4BqAlw&zhida_source=entity)领投的800万美元种子轮融资。
-   2024年，随着生成式AI技术的迅猛发展，Cursor凭借极简的交互方式和高效的代码生成能力，吸引了大量用户。
-   同年，Anyshpere完成6000万美元的A轮融资，公司估值达到4亿美金。
-   2025年1月，Anyshpere再次获得1.05亿美元的B轮融资，公司估值增长到26亿美元

## 相关轶事

-   2024年，[Cloudflare](https://zhida.zhihu.com/search?content_id=254489801&content_type=Article&match_order=1&q=Cloudflare&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzY0MjkwMzQsInEiOiJDbG91ZGZsYXJlIiwiemhpZGFfc291cmNlIjoiZW50aXR5IiwiY29udGVudF9pZCI6MjU0NDg5ODAxLCJjb250ZW50X3R5cGUiOiJBcnRpY2xlIiwibWF0Y2hfb3JkZXIiOjEsInpkX3Rva2VuIjpudWxsfQ.Hjp5ShdJbWCjVpRZzL3t6siuIZsL6AVFfy6-tNDVXiQ&zhida_source=entity)副总裁的年仅8岁的女儿，通过网络主播，使用Cursor在45分钟内就开发了一款聊天机器人，这场直播吸引了180万观众的围观。

![](https://pica.zhimg.com/v2-161bcd93790367b13412e94757e57c58_1440w.jpg)

-   前特斯拉驾驶负责人[Andrej Karpathy](https://zhida.zhihu.com/search?content_id=254489801&content_type=Article&match_order=1&q=Andrej+Karpathy&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzY0MjkwMzQsInEiOiJBbmRyZWogS2FycGF0aHkiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNTQ0ODk4MDEsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.2-US9bDxRkwTyGE12by3XkBsZdrABbDsaqw03QoSO5c&zhida_source=entity)，曾多次发布推文，对Cursor给予了极高的赞誉。

![](https://picx.zhimg.com/v2-bd8f7661120296f519676a491f0f085d_1440w.jpg)

由此可以看出：_**Cursor，有点东西！**_

## 案例演示

## 用嘴写一个《小恐龙》跑酷Demo

使用自然语言的描述，让Cursor做一个静态网页的游戏Demo：

```text
我想做一个静态网页的游戏Demo，这个游戏：
- 类似Chrome浏览器没网络时的小恐龙跳跃障碍物的游戏
- 游戏背景为白色
- 小恐龙颜色为灰色
- 障碍物有地面的、有空中的
- 小恐龙跳跃，采用重力加速度的是实现方式，
  起跳时给予一定的初速度，受重力加速度影响，
  在空中速度减慢，减为零后，加速下落，回到地面
```

![动图封面](https://pic1.zhimg.com/v2-c0f8bd6bfa3e333ba7972e27f394ff74_b.jpg)

## 用嘴生成[Unity C#](https://zhida.zhihu.com/search?content_id=254489801&content_type=Article&match_order=1&q=Unity+C%23&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzY0MjkwMzQsInEiOiJVbml0eSBDIyIsInpoaWRhX3NvdXJjZSI6ImVudGl0eSIsImNvbnRlbnRfaWQiOjI1NDQ4OTgwMSwiY29udGVudF90eXBlIjoiQXJ0aWNsZSIsIm1hdGNoX29yZGVyIjoxLCJ6ZF90b2tlbiI6bnVsbH0.cS3EtwB94e5_aaEYg_BIxnkKU-T_OQqLmCuzWTTerVA&zhida_source=entity)脚本

一个场景，里面有一个平面、一个角色、一个相机，让Cursor生成一个脚本来控制角色和镜头的移动：

![](https://pic2.zhimg.com/v2-51eb867b5ef4a8900fda87863b275517_1440w.jpg)

告诉Cursor生成C#脚本的需求：

```text
这是一个Unity项目工程，使用Unity 2021.3.6f1开发，现在有一个场景：
- 一个Plane
- 一个相机
- 一个Cpasule胶囊体，表示玩家角色

现在需要一个C#脚本，它可以控制角色移动和镜头旋转：
- 按键盘控制角色按照自己的朝向的前后移动、左右旋转：
  W，角色前进；
  S，角色后退；
  A，角色向左旋转；
  D：角色向右旋转

- 相机放在角色眼睛的位置，鼠标上下移动，控制相机旋转：
  鼠标向上移动，相机朝向天空，
  鼠标向下移动，相机朝向地面，
  鼠标的左右移动不会影响角色和相机的旋转

- 请把角色移动、旋转，镜头俯仰角速度等参数暴露出来，方便调整

请在Assets/Scripts目录下编写脚本（如果没有文件夹，就新建一个）
```

生成脚本后，添加到胶囊体上：

![](https://pic2.zhimg.com/v2-9926de309af968c57ef30a14de3cade9_1440w.jpg)

运行后的游戏画面：

![动图封面](https://pic3.zhimg.com/v2-30f6a6cb93600695e398bfd99e7e1224_b.jpg)

## 核心功能

## Cursor Tab

Cursor Tab是手写代码过程中，使用最高频的一个功能。

写代码时，Cursor会基于当前光标的位置推断出你接下来要写的代码内容。

下面是我在Unity中新建的一个代码文件，当我把光标放到两个大括号之间，按下回车时，Cursor就会基于我的光标位置推断出接下来要写的代码。

![动图封面](https://pic4.zhimg.com/v2-0aada49a0b4df7dd0df0b66cd256bca3_b.jpg)

Cursor会像输入法的联想功能一样，联想出你接下来想要编写的内容。如果接受，只需要按键盘的`Tab`键，代码就会自动生成，然后Cursor会基于新的光标位置推断新的内容。

![动图封面](https://pica.zhimg.com/v2-1e944da2d6803f1ad3a6ceff133baec8_b.jpg)

如果不接受，只需按照自己的想法继续敲代码即可。Cursor会基于新的光标位置，推断下一步的联想。

![动图封面](https://pic1.zhimg.com/v2-3db2278d90efb4b1c9cd2c7db4acffa2_b.jpg)

在上下文代码逻辑比较完整的情况下，Cursor对代码的联想一般比较准确。

所以大多数时间里，你会频繁地按Tab键采用Cursor联想的代码，这也是前面提到的`Tab Tab Tab`的来源。

![](https://pica.zhimg.com/v2-690447ab0b3c05a2046255c406cb3686_1440w.jpg)

## 聊天窗口：Chat

Chat聊天窗，是“**用嘴写代码**”时，最核心、最重要的一个功能。

Chat聊天框分为3种模式，分别为：**Ask**、**Edit**、**Agent**。

![](https://pic3.zhimg.com/v2-ff49bcc8870485945516446dd4e2e322_1440w.jpg)

### Ask

Ask模式，类似你使用Deep Seek app来聊天的功能。它侧重于对你的提问进行解答。

![](https://pic4.zhimg.com/v2-fbed88865a353b5f39af42e4cf125c7d_1440w.jpg)

平时开发时，可以把它当作：

-   **思维发散**的工具，辅助你设计一些创新的游戏设计
-   **技术咨询**的工具，告知你要实现这样的功能，需要用到哪些技术
-   **代码解释**的工具，复制一段代码到聊天框，让Cursor告诉你这段代码的逻辑，帮你排查代码是否有Bug
-   **提高效率**的工具，一些机械式的编码工作，一些不太熟悉的编码工作，可以让Cursor帮你写

-   案例：之前做Demo，找了一个第三方特效插件，有一个Shader用的是内置渲染管线的写法，让Cursor把这份Shader转为URP渲染管线的写法

-   （其他任何你能想到让Cursor去做的功能）

### Edit

Edit模式，可以理解为增强版的Ask模式。相比之下，Edit模式增加了直接修改项目文件、代码的功能。

举个例子，我分别在Ask模式和Edit模式下，给AI提了相同的问题：

```text
一个简单跑酷游戏的赛道生成逻辑怎么写
```

Ask模式，生成了C#代码以及文字描述：

![](https://pic1.zhimg.com/v2-571def49c256fb418dad5d6b4057bf12_1440w.jpg)

Edit模式，则是直接修改了代码文件，并给出了文字描述：

![](https://pic3.zhimg.com/v2-39b00489e502403ab9c417518faf7550_1440w.jpg)

Edit模式，更适合在需求明确的情况下，让Cursor AI直接参与到项目工作流中，也就是前面提到的——“用嘴写代码”。

当然AI生成的代码还是需要人去评估的，这些代码生成后，对应的文件处于“待保存”的状态。

你需要一个文件一个文件、一行代码一行代码地去过一遍：

-   符合要求的代码，保留——“√ Accept”
-   不满足要求的代码，还原——“× Reject”

你可以在AI的回答中选择是否使用生成的代码：

![](https://pic3.zhimg.com/v2-b8fc62562ce4e469cede2756dd6e5dcc_1440w.jpg)

也可以在聊天窗口的代码修改总览中选择是否采纳代码：

![](https://picx.zhimg.com/v2-0ec16a8825fb62242619991fd32c4caf_1440w.jpg)

也可以在生成的代码文件中，做更精细化的采纳判断：

![动图封面](https://pic2.zhimg.com/v2-1dc48b902a7e95561983ce0286e18133_b.jpg)

那么，如果你**不会写代码**，该怎么用这个功能？

很简单，无脑点`Accept All`采纳所有生成的代码，然后运行起来看看，不符合效果的，继续向AI提出修改意见，直到代码的运行符合预期。

文章一开始的案例演示，用的就是这种方式。

### Agent

Agent模式，可以理解为增强版的Edit模式。

除了Edit的功能，它还可以：

-   根据搜索内容的关联性，搜索相关的代码
-   调用[MCP服务器](https://zhida.zhihu.com/search?content_id=254489801&content_type=Article&match_order=1&q=MCP%E6%9C%8D%E5%8A%A1%E5%99%A8&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzY0MjkwMzQsInEiOiJNQ1DmnI3liqHlmagiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNTQ0ODk4MDEsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.BfQHeGJpEwYnYjFK6wluU8T5Tz-pgQeeoCIjRioICCg&zhida_source=entity)，接入其他AI工具，比如：文生图
-   运行终端（命令行）指令
-   自动从网上搜索最新的内容

因为Agent模式比Edit模式更强大，逻辑更复杂，所以Agent模式的执行速度会比Edit模式慢很多，但是回答的质量也高很多。

什么情况下使用Agent模式？

-   有编码需求的前提下，

-   如果你不是很懂代码

-   无脑选择Agent模式来生成代码；

-   如果你是程序员

-   如果要生成的代码需要分模块才能理清楚

-   选择Agent模式，交给AI来托管

-   如果只是生成一些简单的逻辑

-   选择Edit模式，精细化操控

## 更精细化地代码编辑：Ctrl + K

`Ctrl K`其实是一个Edit模式的内嵌聊天窗口。

你可以把光标定位到文件的某一行，在内嵌窗口中输入你希望AI生成的代码逻辑：

![动图封面](https://pic4.zhimg.com/v2-37fd34d0850039cf1a8148a26355cff1_b.jpg)

或是想修改、完善某段代码：

![动图封面](https://pic4.zhimg.com/v2-696f7ffd4eae2a2e882fb2dba38077fd_b.jpg)

## 模型切换

Cursor支持了近20款大模型，点`设置（齿轮图标）`\-`Models`，可以看到它支持的所有大模型：

![](https://pic2.zhimg.com/v2-c1d73b6582a80105d7ce18af7e4b91f1_1440w.jpg)

上图已勾选的大模型，作为日常使用时下来菜单可以选择的模型：

![](https://pic3.zhimg.com/v2-405d734c7ff846cc57e6fc4b84d451a6_1440w.jpg)

我个人平时会使用`Claude-3.7-sonnet`、`Deepseek R1`、`GPT-4o`这几个模型，

-   Claude-3.7-sonnet：在软件工程领域比较优秀，一般会配合`Edit模式`用于代码生成。
-   Deepseek R1、GPT-4o：这两个模型大家比较熟悉，它们在综合领域比较优秀，一般配合`Ask模式`用于常规的问答。

大家也可以根据自己的喜好，在不同模式下选择倾向的模型。

下面这张图是各大模型在不同领域的综合表现：

![](https://pic1.zhimg.com/v2-fa1bffec8efd08015c7cbec06f3c41d6_1440w.jpg)

https://www.anthropic.com/claude/sonnet

## @：让AI更懂你

平时项目组内沟通，经常会就一个问题，出现“鸡同鸭讲”的情况，这个时候只要掏出纸和笔，根据问题画出示意图，就很容易把问题聊清楚。

人与人尚且如此，更何况人与AI。为了让AI更懂你，Cursor也需要这套“纸和笔”——引用功能`@`。

只要在Chat聊天框中输入`@`符号，就会唤醒一个功能菜单，根据菜单的类别，告诉AI：“我们现在在聊的是这个东西”。（而“这个东西”，我们称之为“上下文”，下同）

![](https://pic1.zhimg.com/v2-a7738430e85612e6460e1c0fcdef46e6_1440w.jpg)

下面，就一些常用的引用功能，做一一讲解。

### Files & Folders

选择某个文件或文件夹，可以选择多个。

也可以从左侧的文件管理器中直接拖拽文件或文件夹到聊天窗口。

![](https://pic4.zhimg.com/v2-a3fa324034f47426b9f784d8775aa913_1440w.jpg)

使用场景：

-   引用代码文件：让AI解释某个代码类的作用。
-   引用长文本内容：让AI阅读这份文件后，概括总结这份文件讲了什么。
-   引用某个文件夹：让AI在某个文件目录下编辑、创建一些文本内容、代码

### Code

根据官方文档解释，`@Code`是引用某个代码片段，但实际用起来很迷惑：

![](https://pic2.zhimg.com/v2-74bdbc96db07e7babb9336edf989ed73_1440w.jpg)

个人更推荐直接到某个代码文件，鼠标选中某段代码，按快捷键`Ctrl`+`L`，把代码引用到聊天窗口：

![动图封面](https://pic4.zhimg.com/v2-8e8badc0acaf116fe5ed0b9a8272fa6f_b.jpg)

使用场景：

-   让AI排查这段代码的Bug
-   让AI解释这段代码的逻辑
-   让AI修改、优化这段代码的逻辑

### Docs

引用文档，这里的“文档”，一般指的是代码的接口文档，比如：Unity的API文档。

![](https://pic2.zhimg.com/v2-e7b7ca84a78ad9481144d9d420f37d77_1440w.jpg)

在聊天框内输入`@Docs`，按回车，会出现很多Cursor内置的官方文档：

![](https://pic2.zhimg.com/v2-d51ea3174999d2f5fd0949fce460f061_1440w.jpg)

你也可以点`+ Add new doc`，添加其他文档，比如：Python。

![](https://pic4.zhimg.com/v2-257aae18e4edf5028c022838a3c605d9_1440w.jpg)

按回车，Cursor就会解析这个链接，识别出这是一个Python文档：

![](https://picx.zhimg.com/v2-82cb5117d0728a34a9e7f28af2bf3af7_1440w.jpg)

添加后再`@Python`，你就可以在输入框里询问任何Python相关的问题，或者让AI基于这个Python文档，写一个Python应用：

![](https://pic3.zhimg.com/v2-4930e85ba0a43af2b5e382865ab0d100_1440w.jpg)

> 添加文档链接，请注意：
> 如果**没有**以\`/\`结尾，Cursor只会索引这一个链接网页里的内容
> 比如：[https://docs.python.org/3.13](https://link.zhihu.com/?target=https%3A//docs.python.org/3.13)
> 如果输入链接的路径以'/'结尾，Cursor除了索引这个链接文档的内容外，还会索引这个文档链接下所有的子页面和子目录。
> 比如：[https://docs.python.org/3.13/](https://link.zhihu.com/?target=https%3A//docs.python.org/3.13/)

说到链接，如果你想让AI基于某个链接里的内容作为上下文，可以直接输入`@`+链接地址。

比如：

![](https://pic2.zhimg.com/v2-5c8ff62e8ecf84668b9ca8008ba1ac83_1440w.jpg)

### Web

`@Web`与Deep Seek里的`联网搜索`类似，大模型的数据具有时效性，一些比较新的内容还是需要去上网才能找到。

比如：

![](https://pic2.zhimg.com/v2-26b405357f95f82c6c346248de180e0f_1440w.jpg)

点击AI回复中的链接可以直接跳转网页。

### Git

`@Git`用于检索以Git托管的工程，Cursor可以用这个指令检索某次提交。输入`@Git`回车，会唤醒Git提交列表：

![](https://picx.zhimg.com/v2-c111e4d2da4fdddbe0e0de769908d6dd_1440w.jpg)

使用场景：

-   查看某次提交的具体内容

![](https://picx.zhimg.com/v2-17e5b96fc7617082a58336f8a1041d8f_1440w.jpg)

-   选择多个提交记录，让AI对比这几次提交的差异

![](https://pic3.zhimg.com/v2-321238c7f7b0239833b61d16c2c01b80_1440w.jpg)

### Summarized Composers

这是一个做复杂项目时非常有用的一个功能，它可以引用之前某次让AI修改代码逻辑的聊天记录。

输入`@Summarized Composers`回车，会唤醒之前让AI生成过代码的聊天列表。

![](https://pic1.zhimg.com/v2-cebd5f2d2caca9323fa1fc0a8051dc28_1440w.jpg)

你可以在当前聊天窗，与AI聊天聊了很多内容的情况下，快速引用之前某一次代码的修改，让AI找回那时候的记忆。

它在保持聊天上下文的**延续性**上起着比较大的作用。

### Codebase（已弃用，内置到Agent模式下）

这个功能在`0.46.7`版本已经找不到了，后来发现它内置到了Agent模式下，也就是：Agent模式默认是默认开启这个功能的。

所以虽然弃用，依然需要拿出来讲一讲。

Codebase，顾名思义，“以代码为本”。向AI提问时输入`@Codebase`，AI会通读一遍整个项目的代码，然后以此为上下文，对提问进行解答。

这个过程中，Cursor一共做了4件事：

-   **收集**：扫描项目中重要的代码文件、代码块
-   **排序**：根据提问的内容，对收集到的代码进行排序，整理成上下文，内容越相关，排序越靠前
-   **推理**：基于上下文进行思考
-   **生成**：给出回答

每次打开项目，Cursor会自动采集项目代码。这个采集过程在`设置（齿轮图标）`\-`Features`\-`Codebase indexing`里面可以看到，我们也可以点`Resync Index`，手动让Cursor采集代码。

![](https://pica.zhimg.com/v2-94d01c0514be83df3b84d9fbb01034a2_1440w.jpg)

`Codebase indexing`会将本地的代码分割成一小块、一小块的语言数据，然后发送到Cursor的服务器上，Cursor会使用OpenAI的Embedding API进行嵌入，然后加上这些文件的相对路径，一并存到远端的矢量数据库中。这样可以利用索引来提高答复的质量。

根据`Codebase indexing`的描述，Cursor会把代码处理成元数据后再上传云端，不会直接把源代码上传。如果担心项目中一些比较私密的文件被上传，比如：keystore、代码中的私钥等，Cursor提供了`Ignore`功能。

### Cursor Ignore

经常使用Git托管代码的同学都知道，项目中有一个`.gitignore`文件，里面可以输入正则表达式，符合表达式要求的文件、路径，不会被上传到远端。

![](https://pic2.zhimg.com/v2-1a32935be1b2b22ede5a44bbee8d793b_1440w.jpg)

Cursor是尊重`.gitignore`的，符合`.gitignore`的文件不会被收集、上传到Cursor服务器。

如果还有额外的文件不希望被上传，Cursor提供了`.cursorignore`功能。

在项目根目录，创建名为`.cursorignore`的文件，里面按照`.gitignore`的规则添加额外不希望上传的文件即可：

![](https://pic1.zhimg.com/v2-6ddc772d82fc46428df84bd781aec208_1440w.jpg)

如果是比较大的项目，有很多文件是与代码分析没关系的，这些文件如果被Cursor采集、排序，会严重拖慢`Codebase Indexing`速度。所以在项目工程维护一份`.cursorignore`是很有必要的。

新版本似乎新加了`.cursorindexingignore`，相比`.cursorignore`，作用范围更限定：

![](https://pic3.zhimg.com/v2-f22d8199d02ad018d898f3f7d7fc4394_1440w.jpg)

### Cursor Rules

“无规矩，不成方圆”，给AI设定一些规规，可以避免AI做出一些偏离预期的行为。

Cursor是支持这些规则的制定的，从一开始安装Cursor开始。

在第一次进入Cursor界面中，有一个`Language for AI`的输入选项，当输入`中文`后，Cursor AI的所有回复内容都变成了中文。

![](https://pic2.zhimg.com/v2-bd3f1957b2609989a31c452dbc5de283_1440w.jpg)

Cursor的规则设置，可以分为3种颗粒度：

-   基于设备的全局规则
-   基于整个项目的规则
-   自定义规则，用到哪个，引用哪个（`@Cursor Rules`功能）

### 基于设备的全局规则

前面提到的“用中文回答”就是基于设备的全局规则。

它在`设置`\-`Rules`\-`User Rules`模块：

![](https://pic2.zhimg.com/v2-6d3961f5c52f1b684e28bb707d497405_1440w.jpg)

规则的设定内容很泛，可以是：

-   **与项目相关的**

![](https://pic2.zhimg.com/v2-71a377fa248b04dc8a56416589016141_1440w.jpg)

让AI知道，项目的开发环境、开发语言，这样在之后让AI实现相关逻辑代码时，它会更加倾向于用Unity引擎，使用C#或Lua语言来编写代码。

-   **与项目本身无关的**，比如：Git提交规则

有时，我会让AI直接帮我提交代码到Git，AI会给出Git提交指令，我只需要点指令右上角的`Run`，AI就会自动在命令行敲出这些指令，这样就可以提交代码。

![](https://pica.zhimg.com/v2-0d81e014c38804b605036856c511f3ba_1440w.jpg)

但是我希望最后一行指令`git push origin your-branch-name`，直接改用`git push`，所以加入了这一规则：

![](https://pic3.zhimg.com/v2-b604c049760e8c72514077c8c46f483e_1440w.jpg)

此后，AI给出的git push指令就会变成简单的`git psuh`：

![](https://pica.zhimg.com/v2-05da4f2b31940b13293263c350a908b0_1440w.jpg)

### 自定义规则

在`Rules for AI`的下方，有一个`Project Rules`，在里面可以自定义添加规则：

![](https://pic3.zhimg.com/v2-ecc084e2d4b87f632283682e4ef58bda_1440w.jpg)

规则的填写格式，包括：**描述**、**匹配**、规则内容。

![](https://pic3.zhimg.com/v2-fc78a4fe501493ca9256c5f69d42909c_1440w.jpg)

-   **描述**：描述规则的内容，自己看看用的
-   **匹配**：可以设定这些文档适用于什么格式、什么文件目录下，当使用`@Files & Folders`时，会根据引用的内容，判断是否使用这个规则文档
-   **规则内容**：用自然语言编写，什么格式文本都可以

制定好规则后，聊天框输入`@Cursor Rules`回车，选择某一条规则，AI就会基于这份规则来约束自己的行为：

![](https://pic4.zhimg.com/v2-8acca64971663b0104f856bf3719c567_1440w.jpg)

聊天框输入内容

![](https://pic1.zhimg.com/v2-255fedff08db834690ef654509aab65a_1440w.jpg)

AI思考过程，会考虑规则

![](https://picx.zhimg.com/v2-62ccc150421ab9d9c87ab22eda36c3bf_1440w.jpg)

AI执行结果，遵循规则

### 基于项目的规则

基于项目的规则，需要在项目根目录创建`.cursorrules`文件，文件内容用自然语言编写，可以是任意格式的文本。对AI提问时，无需`@Cursor Rules`，AI默认会遵循这套规则。

![](https://pic3.zhimg.com/v2-836cfa2f292d8aab6af9e727aa35862e_1440w.jpg)

> **注意：**
> `.cursorrules`功能之后会被移除，官方推荐使用“基于项目的规则”。
> For backward compatibility, you can still use a **`.cursorrules`** file in the root of your project. **We will eventually remove .cursorrules in the future**, so we recommend migrating to the new Project Rules system for better flexibility and control.

## Cursor的使用技巧

## AI乱改代码问题的解决思路

网上经常会刷到，网友使用Cursor时，AI把之前生成好的、可以稳定运行的代码给改坏了。

下面提一下这个问题的解决思路，对“**用嘴写代码**”的同学们应该会很有帮助。

这个问题可以拆分成3个步骤进行解决：**预防**、**检测**、**回滚**。

### 预防

预防，就是避免让AI生成自己不想要的代码。

换种说法，就是：**怎么向AI提问，让AI完全理解我们的诉求**。

有以下几种策略：

-   **让AI复述需求**

在聊天框输入需求之后，加上一句：

`请先复述一遍我的需求，先不要修改代码，确保你真正理解我的需求。`

然后基于AI的回复，确认AI的理解和需求完全一致时，再让AI生成代码。

-   **限定影响范围**

让AI生成代码时，尽可能引用相关的文件、文件夹，限定AI生成、修改代码的文件范围。

哪怕AI生成了错误的代码，也可以让影响降到最小。

-   **拆解并细化需求**

AI善于执行明确的指令，太泛、太模糊的指令会让AI思维发散，从而生成偏离期望的代码。

举个例子，让AI做一个Unity中控制角色移动的脚本。

```text
请生成一个控制角色的脚本
这是一个Unity项目工程，使用Unity 2021.3.6f1开发，现在有一个场景：
- 一个Plane
- 一个相机
- 一个Cpasule胶囊体，表示玩家角色

现在需要一个C#脚本，它可以控制角色移动和镜头旋转：
- 按键盘控制角色按照自己的朝向的前后移动，
  左右旋转：W，角色前进；S，角色后退；A，角色向左旋转；D：角色向右旋转

- 相机放在角色眼睛的位置，鼠标上下移动，控制相机旋转：
  鼠标向上，相机朝向天空，鼠标向下移动，相机朝向地面
  鼠标的左右移动不会影响角色和相机的旋转

- 请把角色移动、旋转，镜头俯仰角速度等参数暴露出来，方便调整

重复一遍你对这个需求的理解，先不要修改代码，确保你的理解是正确的。
```

-   **引导与修正**

AI在知识领域非常强大，但是在自然语言的沟通理解上，尤其是中文，还远远没能达到一名成年人的理解水准。

即使是两名智力正常的程序与策划，也依然会出现开发内容与项目需求有偏差的情况，所以在AI思考方向有偏差时，要及时修正、加以引导。

必要时，可以将自己对问题的思考策略告知AI，也可以附上一些引用、链接等，帮助AI更好地理解我们的需求。

### 检测

这一点，在Edit那一节有提到过。

在Edit模式下，AI可以一次性帮我们编写很多代码文件，你需要自己去判断这些代码是否符合预期，从而判断代码是否采用。

![](https://pic2.zhimg.com/v2-46641f1ec72df59a61c1e2cc5dee0f2f_1440w.jpg)

生成新的代码文件

![动图封面](https://pic2.zhimg.com/v2-1dc48b902a7e95561983ce0286e18133_b.jpg)

在已有代码文件基础上补充需求

不熟悉编程的同学，可以`Accept All`，运行后根据结果，告知AI哪些地方不符合预期，期望的预期是怎么样的，以此来一步步把代码修改成自己想要的样子。

### 回滚

回滚，是一个追悔的功能。

如果误点了`Accept All`，但是代码逻辑又不是自己想要的，可以找到代码生成前的那一次提问，点`Checkpoint`旁边的`Restore`把代码回滚到修改前的状态：

![](https://pic3.zhimg.com/v2-6c939c8d157d912daf3a6bfc43339884_1440w.jpg)

遵循这3个步骤，可以让AI乱改代码的可能性降到最低。

即使你不会写代码，也可以让AI写出符合你心意的代码。

## Cursor的整体使用思路

-   **需求分析、整理成档：**

-   用`Ask`模式，找AI把需求聊透，并记录成文档，以便后续引用，让AI快速理解。

-   **编写代码、按需选模式**：

-   程序员：用`Edit`模式编写简单的代码逻辑，借助`Agent`模式编写复杂模块的代码逻辑
-   门外汉：无脑用Agent模式。

-   **使用引用、制定规则**：

-   高效使用`@`引用功能
-   合理制定规范，让AI的回答更精准。

-   **模型选择**：

-   编码用`Claude-xxx-sonnet`
-   聊需求用`Deep Seek R1`、`ChatGPT-4o`。

## 【抛砖】添加MCP Server：让Cursor如虎添翼

MCP（Model Context Protocol），模型上下文协议，由Anthorpic（训练Claude模型的那个公司）推出的开放标准协议。

它为开发者提供了一个强大的工具，可以在**数据源**和**AI驱动工具**之间建立安全的双向连接。

打比方：

AI —— 电脑、主机；

MCP —— USB协议；

MCP Server —— 各种USB设备；

给Cursor添加各种MCP Server，就好比给主机插上键盘、鼠标、扬声器，让主机的功能更丰富。

在`设置`\-`MCP`\-`MCP Servers`中，可以添加新的MCP服务器，让Cursor拥有更强大的功能，比如：文生图。

![](https://picx.zhimg.com/v2-7431b55efa8b2bc5b3dbabe12990d3d9_1440w.jpg)

![](https://pic4.zhimg.com/v2-0dc6f6ee823f22e841b95797c7c99cc9_1440w.jpg)

MCP相关推荐阅读：

-   [https://www.youtube.com/watch?v=oAoigBWLZgE](https://link.zhihu.com/?target=https%3A//www.youtube.com/watch%3Fv%3DoAoigBWLZgE)
-   [https://zhuanlan.zhihu.com/p/25728705136](https://zhuanlan.zhihu.com/p/25728705136)
-   Cursor接入文生图，相关文章：

-   [https://aibook.ren/archives/mcp\-server-for-cursor](https://link.zhihu.com/?target=https%3A//aibook.ren/archives/mcp-server-for-cursor)
-   [https://github.com/fengin/image\-gen-server](https://link.zhihu.com/?target=https%3A//github.com/fengin/image-gen-server)
-   [https://github.com/sarthakkimtani/mcp-image-gen](https://link.zhihu.com/?target=https%3A//github.com/sarthakkimtani/mcp-image-gen)

MCP服务器市场，里面可以找到很多其他网友搭建的MCP服务器：

-   [https://glama.ai/mcp/servers](https://link.zhihu.com/?target=https%3A//glama.ai/mcp/servers)
-   [https://smithery.ai/](https://link.zhihu.com/?target=https%3A//smithery.ai/)
-   [https://cursor.directory/](https://link.zhihu.com/?target=https%3A//cursor.directory/)
-   [https://www.lmsystems.ai/marketplace](https://link.zhihu.com/?target=https%3A//www.lmsystems.ai/marketplace)

但是大部分都连接不上，感兴趣的同学也可以自己本地搭建。

## 白嫖

很多好用的AI模型，免费用户是无法使用的，只有Pro用户才有资格。

虽然官方给了14天的免费Pro试用，但是一些比较好的AI模型，调用次数是有上限的。

次数用完了，哪怕你还有试用期限，Chat聊天窗口也没办法使用哪些大模型。

当然，**_我们强烈建议购买Cursor的正版授权，以支持开发者_：**

![](https://pic4.zhimg.com/v2-7e55ecd323e799843ad4aef59f5581a9_1440w.jpg)

但我们同样_**抱有学习和研究的心态**_，来合理地使用官方给免费用户提供的Pro版本试用体验，来进行理论上没有时间限制的试用，也就是——_**白嫖**_。

![](https://pic3.zhimg.com/v2-7263aace1d12ac9413662177049063c8_1440w.jpg)

新注册的账号，有为期14天的Pro版本体验时长，150次优质模型的调用次数。

如果我们一直注册新的账号，就可以一直体验Pro版本。所以白嫖的思路是：重复地注册新的账号。

这里有3种方法：

-   重复创建、删除账号
-   使用临时邮箱
-   使用无限邮箱

## 重复创建、删除账号

当优质大模型使用次数用完时，可以在Cursor官网的账户设置中删除自己的账号，然后用这个账号邮箱重新注册Cursor账号。

![](https://picx.zhimg.com/v2-faeb5bf0bc22ba13865d92c62f0d449b_1440w.jpg)

## 使用临时邮箱

进入临时邮箱平台：[https://temp-mail.org/zh/](https://link.zhihu.com/?target=https%3A//temp-mail.org/zh/)。

![](https://pic4.zhimg.com/v2-698762b8d9cd042396d90754d3664e0f_1440w.jpg)

每次打开这个网页，都会有新的临时邮箱生成出来，这个优先可以临时接收验证码之类的邮件。

每次Cursor Pro资格到期后，可以用临时邮箱注册新的账号继续试用。

## 使用无限邮箱

进入无限邮的网站：[https://2925.com/](https://link.zhihu.com/?target=https%3A//2925.com/)。并注册一个真实的邮箱：

![](https://pica.zhimg.com/v2-5ae9023740acc32015ee6f1a6480f39a_1440w.jpg)

注册的邮箱会作为`主邮箱`，只要我们在注册Cursor的时候，输入的邮箱在主邮箱后面加上后缀，就可以用主邮箱来接收附属邮箱的收件。

![](https://pic3.zhimg.com/v2-47404d65a4c5365beba987eebba1d678_1440w.jpg)

![](https://pica.zhimg.com/v2-b19da92049a524c79f0868cf5682e480_1440w.jpg)

## 刷新机器码

当注册新账号次数过多时，Cursor会根据设备的机器码，禁用当前设备体验Pro版本：

![](https://pic4.zhimg.com/v2-9b3f1acf0209744f0763cd8edb203f8d_1440w.jpg)

此时可以进入这个链接，找到修改机器码的方法：[https://github.com/yuaotian/go-cursor-help/blob/master/README\_CN.md](https://link.zhihu.com/?target=https%3A//github.com/yuaotian/go-cursor-help/blob/master/README_CN.md)

![](https://picx.zhimg.com/v2-9b44bf9f9bee016951d45466af362edf_1440w.jpg)

**_富贵险中求。_**刷新机器码，是一种有风险的操作。

如果你当前的设备购买了其他正版的软件，而那个软件也是基于机器码的话，修改机器码这个操作很可能导致其他软件的正版授权没办法继续使用。

再次强烈声明：

_**强烈建议购买Cursor的正版授权！**_

## References

-   Cursor AI 发展历程

[https://www.youtube.com/watch?v=EnRgdKgOKV4](https://link.zhihu.com/?target=https%3A//www.youtube.com/watch%3Fv%3DEnRgdKgOKV4)

-   Cursor使用教程系列

[https://www.bilibili.com/video/BV1yorUYWEGD](https://link.zhihu.com/?target=https%3A//www.bilibili.com/video/BV1yorUYWEGD)

-   Cursor官方文档

[https://docs.cursor.com/](https://link.zhihu.com/?target=https%3A//docs.cursor.com/)