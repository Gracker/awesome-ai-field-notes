# 真·万字长文:可能是全网最晚的chatgpt技术总结

> 原文链接: https://zhuanlan.zhihu.com/p/613698929

---
​

目录

最近[ChatGPT](https://zhida.zhihu.com/search?content_id=224509142&content_type=Article&match_order=1&q=ChatGPT&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzY4OTk1MzUsInEiOiJDaGF0R1BUIiwiemhpZGFfc291cmNlIjoiZW50aXR5IiwiY29udGVudF9pZCI6MjI0NTA5MTQyLCJjb250ZW50X3R5cGUiOiJBcnRpY2xlIiwibWF0Y2hfb3JkZXIiOjEsInpkX3Rva2VuIjpudWxsfQ.04GZ09eCT5JcR66yNZd1ncBka9RaRw1zwqK_0FTgqvE&zhida_source=entity)可以说是火遍了全世界，作为由知名人工智能研究机构[OpenAI](https://zhida.zhihu.com/search?content_id=224509142&content_type=Article&match_order=1&q=OpenAI&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzY4OTk1MzUsInEiOiJPcGVuQUkiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyMjQ1MDkxNDIsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.xozkBlOZR56_s5_5XEdsB5AUaC7yZC-I-MWM4eeAwuA&zhida_source=entity)于2022年11月30日发布的一个[大型语言预训练模型](https://zhida.zhihu.com/search?content_id=224509142&content_type=Article&match_order=1&q=%E5%A4%A7%E5%9E%8B%E8%AF%AD%E8%A8%80%E9%A2%84%E8%AE%AD%E7%BB%83%E6%A8%A1%E5%9E%8B&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzY4OTk1MzUsInEiOiLlpKflnovor63oqIDpooTorq3nu4PmqKHlnosiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyMjQ1MDkxNDIsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.au_foYJabv6LPxyh-Ff1jVQBvwZPWM_mDrh_zM2YxAw&zhida_source=entity)，他的核心在于能够理解人类的自然语言，并使用贴近人类语言风格的方式来进行回复。模型开放使用以来，在人工智能领域引起了巨大的轰动，也成功火出了技术圈。从数据上看，ChatGPT用户数在5天内就达到了100万，2个月就达到了1亿；另外，在很多非人工智能领域，已经有机构在尝试用ChatGPT去做一些智能生成的事。例如财通证券发布了一篇由ChatGPT生成的行业研报，从研报的可读性和专业性上来看，虽然在细节上有很多需要推敲的地方，但是整体框架内容已经比较成熟。对于其他内容生产者来说，应用ChatGPT也能够提升个人的生产效率。

ChatGPT的强大能力是显而易见的，但对于人工智能领域不太熟悉的人，对这种黑盒的技术仍然会担忧或者不信任。恐惧通常来自于不了解，因此本文将为大家全面剖析ChatGPT的技术原理，尽量以简单通俗的文字为大家解惑。

通过本文，你可以有以下收获：

1、知道ChatGPT是什么

2、ChatGPT有哪些核心要素

3、ChatGPT能做哪些事

4、ChatGPT不能做哪些事

## ChatGPT是什么？

上文说到ChatGPT实际上是一个大型语言预训练模型（即Large Language Model，后面统一简称LLM）。什么叫LLM？LLM指的是利用大量文本数据来训练的语言模型，这种模型可以产生出强大的语言关联能力，能够从上下文中抽取出更多的信息。其实语言模型的研究从很早就开始了，随着算力的发展和数据规模的增长，语言模型的能力随着模型参数量的增加而提升。下图分别展示了LLM在参数量和数据量上的进化情况，其中数据量图例展示的是模型在预训练过程中会见到的token数量，对于中文来说一个token就相当于一个中文字符。

![](https://pica.zhimg.com/v2-0bcf6b0d4881daf0d198b5d29d0c081a_1440w.jpg)

https://www.vinayiyengar.com/2022/08/04/the-promise-and-perils-of-large-language-models/

![](https://pic3.zhimg.com/v2-7857b9e1e9fbe7de5b01c120cbe134e4_1440w.jpg)

https://babylm.github.io/

为什么语言模型的参数量和数据量会朝着越来越大的方向发展呢？在早些时间的一些研究已经证明，随着参数量和训练数据量的增大，语言模型的能力会随着参数量的指数增长而线性增长，这种现象被称为Scaling Law（下图左例）。但是在2022年之后，随着进来对大模型的深入研究，人们发现当模型的参数量大于一定程度的时候，模型能力会突然暴涨，模型会突然拥有一些突变能力（Emergent Ability，下图右例），如推理能力、零样本学习能力等（后面均会介绍）。

![](https://pica.zhimg.com/v2-de7661c3a003aa9ae1b006e67d396610_1440w.jpg)

https://franxyao.github.io/blog.html

ChatGPT真正强大的地方在于他除了能够充分理解我们人类的问题需求外，还能够用流畅的自然语言进行应答，这是以前的语言模型不能实现的。下面，本文将ChatGPT一分为二，分别从GPT和Chat两个维度来介绍ChatGPT的机理。**值得说明的是：当前OpenAI并未放出ChatGPT相关的训练细节和论文，也没有开源代码，只能从其技术BLOG上获取其大致的训练框架和步骤，因此本文介绍的内容将根据后续实际发布的官方细节而更新。**

## GPT

GPT全称Generative Pre-training [Transformer](https://zhida.zhihu.com/search?content_id=224509142&content_type=Article&match_order=1&q=Transformer&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzY4OTk1MzUsInEiOiJUcmFuc2Zvcm1lciIsInpoaWRhX3NvdXJjZSI6ImVudGl0eSIsImNvbnRlbnRfaWQiOjIyNDUwOTE0MiwiY29udGVudF90eXBlIjoiQXJ0aWNsZSIsIm1hdGNoX29yZGVyIjoxLCJ6ZF90b2tlbiI6bnVsbH0.LvoCnBpODeOXn9Ct5a54610O_qup6FAnmXyUQ7lthIU&zhida_source=entity)，由Google在2018年提出的一种预训练语言模型。他的核心是一个Transformer结构，主要基于注意力机制来建模序列中不同位置之间的关联关系，最后可用于处理序列生成的任务。通过使用大量的文本数据，GPT可以生成各种各样的文本，包括对话、新闻报道、小说等等。上面提到了很多次语言模型，这里简单给出语言模型主要的涵义：

给定已知的token序列N\_t（对中文来说是字符，对英文来说可能是单词或者词根），通过语言模型来预测t+1位置上的token是什么。实际上模型输出的是所有token在t+1位置上的概率向量，然后根据概率最大的准则选择token。大家在使用ChatGPT的时候，一定有发现机器人在生成回复的时候是一个字一个字的顺序，背后的机制就是来自于这边。

![](https://pic1.zhimg.com/v2-5ed78513ca523d19b5964bc3832bd132_1440w.jpg)

cs224n（https://web.stanford.edu/class/cs224n/slides/cs224n-2023-lecture11-prompting-rlhf.pdf）

对语言模型来说，可能大家之前更熟悉的是[BERT](https://zhida.zhihu.com/search?content_id=224509142&content_type=Article&match_order=1&q=BERT&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzY4OTk1MzUsInEiOiJCRVJUIiwiemhpZGFfc291cmNlIjoiZW50aXR5IiwiY29udGVudF9pZCI6MjI0NTA5MTQyLCJjb250ZW50X3R5cGUiOiJBcnRpY2xlIiwibWF0Y2hfb3JkZXIiOjEsInpkX3Rva2VuIjpudWxsfQ.cc3eFKtUksrhR_qTbXUQRecnwKWiCxGfFNdKF7m48vM&zhida_source=entity)，BERT是Google在2018年发布的一种双向语言模型，发布后，其在不同语言理解类任务（如文本分类，信息抽取，文本相似度建模）中都达到了当期时间节点的最好效果。BERT与上述语言模型的机理有所不同，其训练任务相当于让模型去做完形填空任务（官方称为Masked Language Model任务，下文简称MLM)，并不是遵循文本一个接一个预测的顺序，其模型机制与人类沟通表达的习惯不太符合。图中左半部分是BERT的示意图，右半部是GPT的示意图，Trm为一个Transformer模型组件，E为输入的token序列，T为模型生成的token序列。其中，实线部分为该位置的Trm能够看到哪些其他位置token的上下文知识。可以看到，对于BERT来说，每个位置上的Trm都能看到任意位置的上下文知识，因此其在具体的自然语言理解任务上会有不错的效果。而GPT则是遵循传统语言模型的模式，例如index=1位置的Trm是无法看到index>1的知识的，因此它在自然语言理解任务上的效果不如BERT，但是在生成任务上会更符合人类的直觉。业界把BERT中的MLM模式称为自编码形式(auto-encoding)，把GPT的模式称为自回归形式（auto-regressive）。

![](https://pic4.zhimg.com/v2-1fb69ffdadb580ed049230cc2e660537_1440w.jpg)

https://arxiv.org/abs/2302.09419

大家从BERT和GPT的对比中可以看到，BERT在语言理解上似乎更具优势，那为何现在ChatGPT的模型基座是GPT呢？这就涉及到最近两年逐渐清晰的NLP任务大一统趋势了。

## NLP任务大一统

基于MLM训练范式得到的BERT模型虽然在很多语言理解类任务上有不错的效果下游任务，之后整个业界在处理NLP任务的时候通常会遵循预训练模型→下游任务finetune的流程：

![](https://picx.zhimg.com/v2-6b2b64c9d15771c69bb4c3fedfe14e1f_1440w.jpg)

这种方式与传统的training from scratch相比，对下游任务数据的需求量更少，得到的效果也更优。不过，上述方式还是存在一些问题：

1.  处理一个新的任务就需要标注新的语料，对语料的需求比较大，之前已经做过的任务语料无法高效利用。即使是信息抽取下面的不同任务（如实体识别和关系抽取两个任务）也无法通用化。
2.  处理一个新的任务需要针对任务特性设计整体模型方案，虽然BERT模型的底座已经确定，但还是需要一定的设计工作量。例如文本分类的任务和信息抽取的任务的模型方案就完全不同。

对于要走向通用人工智能方向的人类来说，这种范式很难达到通用，对每个不同任务都用单独的模型方案和数据来训练显然也是低效的。因此，为了让一个模型能够尽量涵盖更多的任务，业界尝试了几种不同的路径来实现这个目标。

-   对BERT中的MLM进行改造，如引入一些特殊的Mask机制，使其能够同时支持多种不同任务，典型的模型如UniLM（[https://arxiv.org/abs/1905.03197）](https://link.zhihu.com/?target=https%3A//arxiv.org/abs/1905.03197%25EF%25BC%2589)
-   引入额外的Decoder，将BERT优化改造成能做生成式的模型，典型的工作有BART（[https://arxiv.org/abs/1910.13461](https://link.zhihu.com/?target=https%3A//arxiv.org/abs/1910.13461)），T5（[https://arxiv.org/pdf/1910.10683.pdf](https://link.zhihu.com/?target=https%3A//arxiv.org/pdf/1910.10683.pdf)），百度的UIE（将任务设计生成text-to-structure的形式实现信息抽取的大一统 ）。我对T5比较熟悉，之前也写过相关的分析，这个工作算是比较早地尝试将不同任务通过文本生成的方式进行大一统。如图所示，T5训练时直接输入了不同下游NLP任务的标注数据，通过在原始文本的前端添加任务的提示文本，来让模型学习不同任务的特性。如翻译任务可以是”translate English to German”,分类任务可以是跟具体分类目标有关如”cola sentence”,也可以是一种摘要任务”summarize”。

> 怎么样，是不是觉得跟ChatGPT的模式有相似的地方？

这种方式可以同时利用多种NLP任务相关的公开数据集，一下子就把预训练任务从语言模型扩展到了更多任务类型中，增强了模型的通用性以及对下游任务的理解能力。

![](https://pic2.zhimg.com/v2-f75225d30ef7b3b51e22d0651b1662e9_1440w.jpg)

T5数据构建实例

-   除了上面两种方式外，还有其他改造BERT的方法就不穷举了，如苏神通过Gibbs采样来实现BERT模型的文本生成等。（[https://kexue.fm/archives/8119](https://link.zhihu.com/?target=https%3A//kexue.fm/archives/8119)）

虽然有很多大一统的路径，但是OpenAI一直坚持着GPT的方向不断演化着，2019年他们发布了GPT2，这个模型相对于GPT来说，主要是扩大了参数量，扩大了训练语料，在构建语料的时候隐式地包含了multitask或者multidomain的特质，最后在二阶段验证模型的时候并不是直接做有监督的finetune，而是继续用下游数据做无监督的训练，最后的效果居然还不错，证明了只要模型够大，就能学到足够的知识用于处理一些下游任务。从它的论文名字就可以看出来与其核心思想：[Language models are unsupervised multitask learners](https://link.zhihu.com/?target=https%3A//cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) 。不过彼时，BERT及其各种变种在领域中的应用还是更广的，真正让GPT系列模型惊艳众人的工作还是要数2020年发布的[GPT-3](https://zhida.zhihu.com/search?content_id=224509142&content_type=Article&match_order=1&q=GPT-3&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzY4OTk1MzUsInEiOiJHUFQtMyIsInpoaWRhX3NvdXJjZSI6ImVudGl0eSIsImNvbnRlbnRfaWQiOjIyNDUwOTE0MiwiY29udGVudF90eXBlIjoiQXJ0aWNsZSIsIm1hdGNoX29yZGVyIjoxLCJ6ZF90b2tlbiI6bnVsbH0.9Y9xpEjnfXSXg6RkGbOGK_T_SBV2-_IgEB-SQgbLCL0&zhida_source=entity)模型。（[https://arxiv.org/abs/2005.14165](https://link.zhihu.com/?target=https%3A//arxiv.org/abs/2005.14165)）

## GPT-3

首先，说几个跟GPT-3相关的数字：

![](https://pic2.zhimg.com/v2-d7928e3b0c1a0a73a6c97066f612427d_1440w.png)

OpenAI训练初版的GPT-3，比GPT-2整整用了**15**倍的语料，同时模型参数量扩展了**100多倍**。这么多资源的投入，使得GPT-3成为了一个“庞然巨物”，其产生的效果也是惊人的。除了在很多NLP的任务上有着很不错的指标外，其本身也产生了一种前所未有的能力——**[In-context learning](https://zhida.zhihu.com/search?content_id=224509142&content_type=Article&match_order=1&q=In-context+learning&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzY4OTk1MzUsInEiOiJJbi1jb250ZXh0IGxlYXJuaW5nIiwiemhpZGFfc291cmNlIjoiZW50aXR5IiwiY29udGVudF9pZCI6MjI0NTA5MTQyLCJjb250ZW50X3R5cGUiOiJBcnRpY2xlIiwibWF0Y2hfb3JkZXIiOjEsInpkX3Rva2VuIjpudWxsfQ.W69jChMfvqzCyDkPkib4MVFoLE3AqqWW-ejXB7Oo848&zhida_source=entity)**。

## 何为**In-context learning**？

简单来说，就是模型在不更新自身参数的情况下，通过在模型输入中带入新任务的描述与少量的样本，就能让模型”学习”到新任务的特征，并且对新任务中的样本产生不错的预测效果。这种能力可以当做是一种小样本学习能力。可以参考下图的例子来理解：其中，task description和examples用来帮助模型学习新任务，最后的Prompt用来测试模型是否学会了。

![](https://pic1.zhimg.com/v2-70607f9aec9f18dfa075e8881ff34116_1440w.jpg)

与传统的小样本学习范式还是有所不同，之前主流的小样本学习范式以Meta-learning为主，通过将训练数据拆成不同的小任务进行元学习。在学习的过程中，模型的参数是一直在变化的，这是最大的一个不同点。

那不更新参数的小样本学习有什么好处呢？

对于大模型来说，这可是极佳的特性。因为大模型的微调成本通常都极为庞大，很少有公司能够具备微调训练的资源。因此，如果能够通过In-context learning的特性，让大模型快速学习下游任务，在相对较小的成本下（对大模型进行前向计算）快速完成算法需求，可以大大提升技术部门的生产力。

In-context learning的效果固然惊艳，但是对于一些包含复杂上下文或者需要多步推理的任务仍然有其局限性，这也是业界一直以来致力于让人工智能拥有的能力——推理能力。那么大模型具有推理能力吗？对于GPT-3来说，答案是可以有，但有一定的限制。我们先来看看它有的部分。

还记得文章开头提到的大模型的涌现能力吧，In-context正是属于当模型参数量达到一定程度后，突然出现的能力之一。那么除此以外，还有什么能力是涌现的呢？答案就是——[Chain-of-thought](https://zhida.zhihu.com/search?content_id=224509142&content_type=Article&match_order=1&q=Chain-of-thought&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzY4OTk1MzUsInEiOiJDaGFpbi1vZi10aG91Z2h0IiwiemhpZGFfc291cmNlIjoiZW50aXR5IiwiY29udGVudF9pZCI6MjI0NTA5MTQyLCJjb250ZW50X3R5cGUiOiJBcnRpY2xlIiwibWF0Y2hfb3JkZXIiOjEsInpkX3Rva2VuIjpudWxsfQ.Pb3iWWVtmglJ3_6VEC_l3MG_sIFFjBfOeWHcOniroGk&zhida_source=entity)，即思维链能力。

## 怎么理解**In-context learning**？

GPT-3拥有的In-context learning能力可以说有很大程度来自于其庞大的参数量和训练数据，但是具体能力来源仍然难以溯源。不过，最近已经有一些论文专门针对其进行了研究，如清华大学、北京大学和微软的研究员共同发表了一篇论文：[https://arxiv.org/abs/2212.10559](https://link.zhihu.com/?target=https%3A//arxiv.org/abs/2212.10559)，探索了GPT作为一个语言模型，可以视作是一个元优化器，并可将In-context learning理解为一种隐性的微调。

## 何为Chai**n-of-thought（COT）**？

实际上是对输入的Prompt采用Chain-of-thought的思想进行改写。传统的Prompt中，对于一个复杂或者需要多步计算推导的问题样例，会直接给出答案作为In-context learning的学习范例与新任务的测试样例输入到大模型中。这样做往往不能得到正确的结果，如图所示：（[https://arxiv.org/pdf/2205.11916.pdf](https://link.zhihu.com/?target=https%3A//arxiv.org/pdf/2205.11916.pdf)）

![](https://pica.zhimg.com/v2-9058ca86bf30f91c362e9a478fd37474_1440w.jpg)

然而，当我们将上述问题范例中的答案再细化一些，对推到出答案的每一个步骤都写出来，再将测试样例一起输入到模型中，此时模型居然能够正确回答了，而且也能够参照范例中的样例进行一定的推理，如图所示：

![](https://pica.zhimg.com/v2-ef69c6f8d7ee056f0f7aed9c56dd0b40_1440w.jpg)

上述的模型输入中，还带有可参考的问题范例，还属于小样本的范畴。诡异的是，有人使用了一种匪夷所思的方法，让其具备了零样本的推理能力：在问题样例的答案中增加一句Let’s think step by step. 然后模型居然能够回答出之前不能回答的问题。

![](https://pic4.zhimg.com/v2-3d63b91a561947117309c4ceb426f201_1440w.jpg)

当然，上图中模型并未直接给出一个简洁的答案，而是给出了推导答案的步骤，论文中则是将上述output与输入模型的Prompt拼在一块，再次输入模型，最终得到了简洁的答案输出：

![](https://pic1.zhimg.com/v2-55648bad9ed7dfe186b232fc599c4a82_1440w.jpg)

既然大模型具备了COT的特性，那么就能说明它具备了推理能力了吗？答案是不确定的。因为在更多的复杂逻辑推理类任务或者计算任务上，大模型还是无法回答。简单来说就是他可以做一些简单的小学应用题，但是稍微复杂一点的问题它就是在瞎猜了。具体的例子可以参考这篇论文中的分析：[https://arxiv.org/abs/2208.05051](https://link.zhihu.com/?target=https%3A//arxiv.org/abs/2208.05051)

## Chain-of-Thought能力来自于哪儿？

上一小节在介绍COT特性的时候，都是统一用GPT-3来代表。其实，\*\*原始的GPT-3版本中并没有显著地发现其具备COT特性。\*\*对于大众来说，像是chatGPT突然就有了这样的能力。其实，在chatGPT出来之前，openAI对GPT-3做了很多迭代优化工作。而GPT-3的COT特性就是在这些迭代优化中逐渐展现。但不可否认的是，目前仍然没有确定性的结论说明COT特性来自于具体哪些迭代优化。有些观点说是通过引入强化学习，有些观点则是说通过引入了指令微调的训练方式，也有些观点说是通过引入庞大的代码预训练语料，使得模型从代码逻辑中学习到了相应知识。推测的方式则是根据不同时间节点上的模型版本能力差进行排除法，虽然目前我们受限于技术能力只能从这些蛛丝马迹中去发现一些端倪，但仍然具有一定的借鉴意义。具体的推理过程本文不会重复，感兴趣的可以参考如下博客：[https://franxyao.github.io/blog.html](https://link.zhihu.com/?target=https%3A//franxyao.github.io/blog.html)。

## [Instruction-Tuning](https://zhida.zhihu.com/search?content_id=224509142&content_type=Article&match_order=1&q=Instruction-Tuning&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzY4OTk1MzUsInEiOiJJbnN0cnVjdGlvbi1UdW5pbmciLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyMjQ1MDkxNDIsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.lZ50vRM7q7aNZeHheBVUE1EV0V1kUfuMRA4dPSGl5tM&zhida_source=entity)与RLFH技术

虽然对于大模型突变能力的来源还不能轻易下结论，但是在其迭代优化过程中，引入的一些技术确实提升了（更准确得说是激活）大模型的能力。根据OpenAI的技术博客所述，ChatGPT的训练方式主要参考了InstructGPT（[https://arxiv.org/abs/2203.02155](https://link.zhihu.com/?target=https%3A//arxiv.org/abs/2203.02155)），而InstructGPT主要涉及了两个核心的技术实现：指令微调（Instruction-Tuning）以及基于人工反馈的强化学习（Reinforcement learning from Human Feedback)，下面将对其进行介绍。

### Instruction-Tuning

Instruction-Tuning（下称指令微调）技术，最早来自于谷歌Deepmind的Quoc V.Le团队在2021年发表的论文《Finetuned Language Models Are Zero-Shot Learners》([https://arxiv.org/abs/2109.01652](https://link.zhihu.com/?target=https%3A//arxiv.org/abs/2109.01652))。在说指令微调前，必须得先介绍下21年初开始业界开始关注的Prompt-learning范式。2021年4月，我在InfoQ的架构师大会上做了一次技术演讲，分享了我们在Prompt上的一些研究实践，如下图所示：

![](https://pic3.zhimg.com/v2-2642c7f021794407a5d131d1019f700a_1440w.jpg)

Prompt-learning最早来自于论文《Exploiting Cloze Questions for Few Shot Text Classification and Natural Language Inference》（[https://arxiv.org/abs/2001.07676](https://link.zhihu.com/?target=https%3A//arxiv.org/abs/2001.07676)），当时把里面的范式简称为PET（Pattern-exploiting Training）。其核心思想为将不同类型的自然语言理解任务与BERT预训练中的掩码语言模型任务进行转化靠拢。例如对于图中的实体情感分类任务，本身其分类标签是一个三维的空间。我通过设置一个prompt提示文本模板：由此可见，英伟达的舆情是{}，同时设计一个锚点，将原始分类目标的空间映射到语言模型中的子空间{正/负/中}，通过预测锚点位置的token间接得到情感标签。这种方式的优点在于能够将下游任务与语言模型在预训练任务中的训练范式达成一致，减少下游任务在模型学习迁移过程中的知识损失，在小样本的场景下比普通的Finetune模式会有更好的效果。Prompt-learning实际上是一种语言模型能够股泛化不同任务的方式，从广义层面上来看，可以有多种实现方式，例如上面的PET，本文之前提到的T5模型，以及初版的GPT-3等。指令微调实际上也可以算作是广义Prompt-learning中的一种实现方式（个人愚见）。它的核心思想是尽可能收集不同类型的自然语言处理任务（包括理解和生成），并使用自然语言设计对应的任务指令，让模型试图理解不同任务的指令与特性，最终通过语言模型生成的方式完成不同任务的训练，指令微调实例如下图所示：

![](https://pic2.zhimg.com/v2-3677d30007e6c7e3d29d9ce7720d5961_1440w.jpg)

那么指令微调与BERT、T5、GPT-3等Prompt方式有什么区别呢？

![](https://pic3.zhimg.com/v2-0ce4f9cb492bf58fb112750dc11836f0_1440w.jpg)

1.  BERT类的Prompt设计与掩码语言模型任务相关，Prompt模板和锚点要与任务对应，需要一定量的标注样本进行小样本训练。
2.  T5的Prompt更像是在预训练时对不同语言任务的数据打上了不同的标记，让模型对语言任务有了初步的理解，但是不够深入，无法应用在零样本的场景。
3.  GPT-3的Prompt中，会基于在模型训练过程中见过的数据，更像是让模型将Prompt中的文本进行续写。这种方式可以帮助模型更好地理解用户输入的内容，并产生更准确和自然的输出。但其在零样本场景下效果仍然不佳。
4.  指令微调技术使用Prompt来为模型提供一系列指令或者命令，这些指令或命令会告诉模型应该如何进行特定任务的处理。与GPT-3中的Prompt不同，指令微调中的Prompt是针对特定任务和特定的模型进行设计的，相当于是指导模型如何完成任务。指令微调技术提升了模型的零样本学习能力。模型对于未见过的任务也能够理解并尝试处理。在GPT-3后续的迭代版本中，加入了指令微调后，即使在Prompt中不引入带标注的样本，模型也能够比较好的理解需求并得到不错的效果。

> 目前公开开源的模型FLAN T5就是在T5模型基础上进行了指令微调的训练，相较于那些动辄几百亿、几千亿参数的大模型来说，这个模型的参数量已经足够亲民，可以作为个人研究或者业务实现的strong baseline

在ChatGPT公开后，各种五花八门的Prompt层出不穷。有让其作为一个linux终端的，有让其作为一个二次元猫娘的，也有让他写武侠小说的。感觉上ChatGPT可以做任何事情，只要你的脑洞足够大。这种通才特质有很大一部分要归功于指令微调。只要我们设计的Prompt指令足够清晰完整，模型总能够理解我们要干什么，并尽量按照我们的需求去完成任务。**我认为这是其有别于过往大模型的重要特性之一**。

### 深度强化学习简述

指令微调技术固然强大，但是其本身也存在一定的缺点：

1.  一些开放性的生成性语言任务并不存在固定正确的答案。因此在构建指令微调的训练集时，就无法覆盖这些任务了。
2.  语言模型在训练的时候，对于所有token层面的错误惩罚是同等对待的。然而在文本生成时，有些token生成错误是非常严重的，需要加权惩罚。换句话说，语言模型的训练任务目标与人类的偏好存在gap。

综上，我们需要模型能够学习如何去满足人类的偏好，朝着人类满意的更新模型参数。因此，我们就需要引入人类对模型的奖惩方法（Reward）作

... (内容已截断，原文更长)