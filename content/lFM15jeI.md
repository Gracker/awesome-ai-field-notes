# 提示艺术：PromptPerfect 提示优化器测试体验（一）

> 原文链接: https://zhuanlan.zhihu.com/p/611970732

---

# 提示艺术：PromptPerfect 提示优化器测试体验（一）

> 原文链接: https://zhuanlan.zhihu.com/p/611970732?utm_medium=social&utm_oi=27871238160384&utm_psn=1617109692114690048&utm_source=we

---
​

目录

看到jina发布了[PromptPerfect](https://zhida.zhihu.com/search?content_id=224125024&content_type=Article&match_order=1&q=PromptPerfect&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzY4MzgxMDMsInEiOiJQcm9tcHRQZXJmZWN0IiwiemhpZGFfc291cmNlIjoiZW50aXR5IiwiY29udGVudF9pZCI6MjI0MTI1MDI0LCJjb250ZW50X3R5cGUiOiJBcnRpY2xlIiwibWF0Y2hfb3JkZXIiOjEsInpkX3Rva2VuIjpudWxsfQ.FfTuRW8fG1qqw7qW2WkNC_Idv8jJgFJ4-Jvlvd0Ps-8&zhida_source=entity)，专为[大型语言模型](https://zhida.zhihu.com/search?content_id=224125024&content_type=Article&match_order=1&q=%E5%A4%A7%E5%9E%8B%E8%AF%AD%E8%A8%80%E6%A8%A1%E5%9E%8B&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzY4MzgxMDMsInEiOiLlpKflnovor63oqIDmqKHlnosiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyMjQxMjUwMjQsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.0D0QqHXI57xP55wqtRDwElKcVRc2xd-qeizooNbrUG4&zhida_source=entity) (LLM)、[大型模型](https://zhida.zhihu.com/search?content_id=224125024&content_type=Article&match_order=1&q=%E5%A4%A7%E5%9E%8B%E6%A8%A1%E5%9E%8B&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzY4MzgxMDMsInEiOiLlpKflnovmqKHlnosiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyMjQxMjUwMjQsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.pL1SadvZuufSaFaqbczdvZwCLLamdbJ5PXexjJRtvrM&zhida_source=entity) (LM) 和 [LMOps](https://zhida.zhihu.com/search?content_id=224125024&content_type=Article&match_order=1&q=LMOps&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzY4MzgxMDMsInEiOiJMTU9wcyIsInpoaWRhX3NvdXJjZSI6ImVudGl0eSIsImNvbnRlbnRfaWQiOjIyNDEyNTAyNCwiY29udGVudF90eXBlIjoiQXJ0aWNsZSIsIm1hdGNoX29yZGVyIjoxLCJ6ZF90b2tlbiI6bnVsbH0.tOFf--mfIqqS-8uot0iVgDSc6B_hgFypXLdlR1hPUag&zhida_source=entity) 设计的提示优化器。

[](https://link.zhihu.com/?target=https%3A//promptperfect.jinaai.cn/)

## 1 PromptPerfect是啥

尖端工具简化了提示工程，自动优化您对 [ChatGPT](https://zhida.zhihu.com/search?content_id=224125024&content_type=Article&match_order=1&q=ChatGPT&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzY4MzgxMDMsInEiOiJDaGF0R1BUIiwiemhpZGFfc291cmNlIjoiZW50aXR5IiwiY29udGVudF9pZCI6MjI0MTI1MDI0LCJjb250ZW50X3R5cGUiOiJBcnRpY2xlIiwibWF0Y2hfb3JkZXIiOjEsInpkX3Rva2VuIjpudWxsfQ.gmVoOl6kRCShtI-BRcsih_ZO0gg9uTEtseywI3W2Zd4&zhida_source=entity)、[GPT-3.5](https://zhida.zhihu.com/search?content_id=224125024&content_type=Article&match_order=1&q=GPT-3.5&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzY4MzgxMDMsInEiOiJHUFQtMy41IiwiemhpZGFfc291cmNlIjoiZW50aXR5IiwiY29udGVudF9pZCI6MjI0MTI1MDI0LCJjb250ZW50X3R5cGUiOiJBcnRpY2xlIiwibWF0Y2hfb3JkZXIiOjEsInpkX3Rva2VuIjpudWxsfQ.yNeA713SwBLoeknQdsB7e3CFbBZbvNuA-TW0IhVOXm0&zhida_source=entity)、[DALLE](https://zhida.zhihu.com/search?content_id=224125024&content_type=Article&match_order=1&q=DALLE&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzY4MzgxMDMsInEiOiJEQUxMRSIsInpoaWRhX3NvdXJjZSI6ImVudGl0eSIsImNvbnRlbnRfaWQiOjIyNDEyNTAyNCwiY29udGVudF90eXBlIjoiQXJ0aWNsZSIsIm1hdGNoX29yZGVyIjoxLCJ6ZF90b2tlbiI6bnVsbH0.ATy4zDT8yW5kV16GwReaJsUuBwei0rMJhkAs1bJZtpw&zhida_source=entity) 和 [StableDiffusion](https://zhida.zhihu.com/search?content_id=224125024&content_type=Article&match_order=1&q=StableDiffusion&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzY4MzgxMDMsInEiOiJTdGFibGVEaWZmdXNpb24iLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyMjQxMjUwMjQsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.xWXxCKTY3yqseulbMYFFIWQmUCYCEE43REKe-SNSKwI&zhida_source=entity) 模型的提示。无论您是提示工程师、内容创建者还是 AI 开发人员，PromptPerfect 都能让提示优化变得简单易行。凭借其直观的界面和强大的功能，PromptPerfect 释放了 LLM 和 LM 的全部潜力，每次都能提供高质量的结果。告别 AI 生成的低质量内容，并使用 PromptPerfect 来提示完美！

![](https://pic3.zhimg.com/v2-6b96ebe9ec4c450d98b7bd0a96c3a490_1440w.jpg)

几个应用场景：

![](https://pica.zhimg.com/v2-691d60454d28743cc270fd71f335d946_1440w.jpg)

![](https://pic3.zhimg.com/v2-f4de1f3a0f1f2a5d1d95d5c4dba7757c_1440w.jpg)

## 2 试用

登陆界面后，选模型 + 选插件+写提示词

![](https://pica.zhimg.com/v2-914785544eb3e5dbd16e3e11c4327190_1440w.jpg)

![](https://pic2.zhimg.com/v2-e1f9afcfd28ce8a751b09e227823ece3_1440w.jpg)

来看一个例子：

```text
# 笔者自己写的提示词
帮助写一篇介绍promptperfect的知乎文章，PromptPerfect 可以优化任何使用语言模型进行文本生成和分析的模型的提示；生成的内容需要中文

# PromptPerfect改之后的提示词：

Your task is to write a Chinese language article introducing PromptPerfect. Your response should provide an overview of the capabilities of PromptPerfect, focusing on its ability to optimize prompts for any text generation and analysis model using language models. The article should be written in clear and concise Chinese, with attention to detail and accuracy.

Please note that your article should explain how PromptPerfect can help improve the quality of generated content by optimizing prompts for language models. It should also discuss the various features and benefits of using PromptPerfect, such as increased flexibility and creativity in generated content. Additionally, you should focus on providing examples that illustrate how PromptPerfect can be used effectively in different scenarios.
```

直观感受：

提示词描述更加具体和写实，甚至提示本身就是在构成接下来文章的大纲

输出是一个卡片：

【优化了什么？】这个模块，实现了【原句子】-> 【优化句子】，到底差别在哪 ，讲得还头头是道，感觉比优化器PromptPerfect本身更让我觉得有意思。

![](https://pic4.zhimg.com/v2-6d7fd724009f6bab64b49a7e2385752b_1440w.jpg)

![](https://picx.zhimg.com/v2-f2a4f4894a0abeacf47dce27f5045a5b_1440w.jpg)

## 3 建议

我测试的是chatgpt，从提示词的内容来看，建议产品流程中加一个中间过渡环节，用户可以再次DIY一下提示词，体验流程可以是：

用户输入提示词 -> PromptPerfect生成提示词（大纲） -> 用户再改一遍大纲 -> 最终生成

其他：

-   我想看到中文提示词，貌似不太行（自问自答：选项中勾选“固定提示语言“）
-   误点没法取消，浪费了学分

编辑于 2023-03-08 09:28・上海

[

ChatGРТ

](//www.zhihu.com/topic/27042831)

[

提示工程

](//www.zhihu.com/topic/26376864)

[

阿里云 ×OpenClaw 7\*24小时“AI”助理！

让“AI”干活，解放自己！查看详情让“AI”干活，解放自己！ 查看详情

![用户头像](images/img_008.webp)

阿里云的广告

](https://click.aliyun.com/m/1000409721/?spu=biz%3D0%26ci%3D3681403%26si%3Dc11341ac-6a6c-4b1e-831f-b5e914f2f130%26ts%3D1776665308%26zid%3D1629)

​赞同 84​​6 条评论​374 ​29

​分享

​申请转载​

​