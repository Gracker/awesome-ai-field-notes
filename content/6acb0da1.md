# Open-source is NOT the same as open-weight

> Source: <https://garymarcus.substack.com/p/open-source-is-not-the-same-as-open>
> Author: Gary Marcus  
> Original date: 2026-08-10  
> Captured: 2026-08-11 (AAIF daily-intake-evening)

## 中文摘要

作者用 ML pipeline 高亮图说明 open-weight 只交付成品模型,看不到训练数据、预处理细节、超参与算法。下游既不能改配方、不能剔除 Reddit 数据、也不能审计偏见——监管、研究、社区三方面都拿不到能力。Zuckerberg 自己分得清,但 NYT 没分,业界长期被“伪开源”误导。

## English Summary

Gary Marcus uses an ML pipeline diagram to argue that open-weight only delivers the finished model — no training data, no preprocessing details, no hyperparameters, no algorithm. Downstream users cannot change the recipe, strip out Reddit data, or audit bias. Zuckerberg makes the distinction, but NYT and the industry still conflate open-weight with open-source.

## 一句话

> open-weight 是发蛋糕不开配方,开源才给整条流水线

## Source Body Excerpt

# Open-source is NOT the same as open
> 作者: Gary Marcus
> 发布时间: 2026-08-10T15:27:42.642Z
> 原文链接: https://garymarcus.substack.com/p/open-source-is-not-the-same-as-open

---

# Open-source is NOT the same as open-weight

### How The New York Times just bungled this one, and why it matters, immensely

[

![Gary Marcus's avatar](https://substackcdn.com/image/fetch/$s_!Ka51!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F8fb2e48c-be2a-4db7-b68c-90300f00fd1e_1668x1456.jpeg)

](https://substack.com/@garymarcus)

[Gary Marcus](https://substack.com/@garymarcus)

Aug 10, 2026

281

93

43

Share

[

![X avatar for @GaryMarcus](https://substackcdn.com/image/fetch/$s_!GPK6!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fpbs.substack.com%2Fprofile_images%2F2048405471900606464%2FkPeRHI2z.jpg)

Gary Marcus@GaryMarcus

Sad to see the @nytimes confuse open-source (fully transparent) with open-weight models (less transparent; no access eg to training data). The new Meta model is open-weight but not open-source. NYT got it wrong. It is time for both the media and the public to learn this

![](https://substackcdn.com/image/fetch/$s_!A6mp!,w_520,h_520,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fpbs.substack.com%2Fmedia%2FHPXTRJ8aEAASL00.jpg)

![](https://substackcdn.com/image/fetch/$s_!ExR8!,w_520,h_520,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fpbs.substack.com%2Fmedia%2FHPXTRJObQAANXnS.jpg)

1:26 PM · Aug 10, 2026 · 3.29K Views

* * *

9 Replies · 4 Reposts · 43 Likes

](https://x.com/garymarcus/status/2086806296532255072?s=61)

It’s no exaggeration to say that [open-source software](https://en.wikipedia.org/wiki/Open-source_software) — in which the complete _source_ code is available to anyone — has changed the world and accelerated software development.

But _open-source_ and _open-weight_ are [two very different things](https://opensource.org/ai/open-weights), and too many people —this morning it was editors and writers at _The New York Times_ among others—are failing to distinguish the two.

The essence of open-source is twofold: transparency and customizability. If you want to know how something works, you look at the code. You can change literally anything about that code (“forking” a new version of that code, for example, if you want to make a different version). All of this is fantastic for the community, and that is why open-_source_ has been such a dynamic force. It’s called open-source because you release the _source_ code of the final product. Open-_weight_ doesn’t do that.

Open-weight piggybacks onto all the great press that open-source has but offers few of the advantages. Open-weight models are NOT fully customizable, and not transparent. They are the _product_ of machine learning (the _weights_ of a trained neural network), but not the whole thing, from soup to nuts. That means you can run them (or “posttrain” them), but, crucially, users can’t customize or improve them to remotely the same degree (more about that in a second), and outsiders can’t investigate them to nearly the same degree. You also can’t build community in the same way.

If pigeons are “just rats with better PR”, open-weights is open-source with all the good press but far fewer advantages.

Understanding all this requires a basic familiarity with the life cycle of a machine learning model. Let’s start with a simplified sketch I have snarfed (and modified) from [geeksforgeeks.org](https://www.geeksforgeeks.org/machine-learning/steps-to-build-a-machine-learning-model/). The highlighting, which I will explain in a moment, is mine.

(Not shown is “[post training](https://aiwiki.ai/wiki/post-training)”, in which people try to align and bend trained “base” models to their will. That’s all you can do with an open-weight model; I will give you examples of what you can’t do in a moment.)

[

![](https://substackcdn.com/image/fetch/$s_!trEZ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcad88757-c700-4aff-9d57-7b261f954026_774x354.jpeg)

](https://substackcdn.com/image/fetch/$s_!trEZ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcad88757-c700-4aff-9d57-7b261f954026_774x354.jpeg)

When someone releases an open-weight model they are releasing the (highlighted) candidate model \[also sometimes known as a base model\]—which is the _output_ of a complex process—_not_ the full pipeline that generated that model. You can adapt that candidate model, but you can’t rebuild it or investigate it to your liking, the way you could with a true open-source model, such as AllenAI’s [Olmo](https://allenai.org/olmo) or Nvidia’s [Nemotron](https://developer.nvidia.com/topics/ai/nemotron), which truly is what it says on the tin: “open weights, training data, and recipes.”

In contrast, when people release _open-weight_ models, they are not revealing the [Full Monty](https://www.phrases.org.uk/meanings/full-monty.html). They are _not_ releasing the raw data; they are _not_ revealing how they preprocessed that data; and they are _not_ revealing the exact algorithms and parameters that they used in training. (For those who can stand yet one more loose metaphor, it’s like they are releasing a cake, but not the recipe; you can add icing on top, and maybe some fruit or hot fudge too, but you can’t change the raw ingredients that went into the cake itself.)

All this makes a world of difference, to developers who might use the systems, to regulators, to scientists, and ultimately to the world.

For developers, let’s say you have a hypothesis that you could make a safer AI if you delete all of the Reddit data from training. Sorry, out of luck: in an open-weight system (as opposed to a truly open-source system) you can’t change the training data at all, and in fact you can’t even _see_ the training data. Or let’s say you would like to train a model on legal reasoning and recognize that common law and statutory law are different. To reduce confusion in the system you would like to filter out the common law stuff before training; again you are out of luck. Or suppose you would like to use Big Company’s training process purely on your own data, rather than on whatever random stuff they scraped from the web. Nope, can’t do that either. (Nor can you share the results of any of those experiments with the community, since you can’t run them in the first place.)

Or say you are a regulator, and you would like to know how much bias there is towards white males in the training data. Sorry, can’t look at that, either. What kinds of instructions are there relevant to bioweapons? Again, nope.

Are you a scientist? Want to investigate how much of what the model does is regurgitation and how much extends beyond the training data, which is arguably the central question in AI? Sorry, out of luck there, too. Those who _released_ the open-weight model could do that, since they are privy to all these details that are actually closed, but you can’t. Or maybe you just want to know whether the answers to your favorite benchmarks are actually already in the training data? Nope, can’t look at that, either.

All of this is unfortunate. It means that developers often can’t really use the open-weight models (despite the hype) to develop what they want; scientists can’t use them to test a lot of key hypotheses, and regulators can’t peer inside the process.

Furthermore, if you wanted to know how much of the training data was copyrighted, you can’t look at that either — which is perhaps part of why none of the big companies want to release true open-source, and instead settle for open-weight, getting nearly all of the positive press without actually helping the community nearly as much.

§

What prompted me to finally write about this?

Meta just released an open-weight model. To his credit, Zuckerberg himself got the terminology right here:

[

![X avatar for @finkd](https://substackcdn.com/image/fetch/$s_!tYZP!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fpbs.substack.com%2Fprofile_images%2F77846223%2Fprofile.jpg)

Mark Zuckerberg@finkd

Releasing Muse Code in beta today. It's a terminal coding agent that takes on complete software engineering tasks across large repos: planning changes, writing code, validating the results. Powered by Muse Spark 1.2, a coding-focused model update.

![](https://pbs.substack.com/media/HO-xetQW0AAvupU.jpg)

7:09 PM · Aug 5, 2026 · 2.87M Views

* * *

1.34K Replies · 1.28K Reposts · 14.6K Likes

](https://x.com/finkd/status/2085080750034940201?s=61)

But the Times did not:

[

![](https://substackcdn.com/image/fetch/$s_!f0rH!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F244e47cd-40f7-439c-b7d8-d8e1e2a5bf19_1202x964.jpeg)

](https://substackcdn.com/image/fetch/$s_!f0rH!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F244e47cd-40f7-439c-b7d8-d8e1e2a5bf19_1202x964.jpeg)

Putting scares quotes around open-source does not make an open-weight model more open. And although one can post-train[1](#footnote-1) Meta’s new model, readapting it to some degree, for all the reasons I just described, it can’t be freely modified, nor used for proper science. You can’t do any of the modifications I described above. And you can’t figure out how the model got to be the way it is in the first place.

§

Zuckerberg knows perfectly well the difference between open-weight and open-source. A few weeks ago he was extolling the value of open-source:

But also played bait and switch with another tweet here:

[

![X avatar for @finkd](https://substackcdn.com/image/fetch/$s_!tYZP!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fpbs.substack.com%2Fprofile_images%2F77846223%2Fprofile.jpg)

Mark Zuckerberg@finkd

Open source is a positive and important force for both empowering people and preventing centralization. Proud to support this.

![X avatar for @satyanadella](https://substackcdn.com/image/fetch/$s_!si98!,w_20,h_20,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fpbs.substack.com%2Fprofile_images%2F1221837516816306177%2F_Ld4un5A.jpg)

Satya Nadella @satyanadella

Open-weight models are essential to a healthy AI ecosystem. Together with others across our industry, we are outlining a path for open-weight models to strengthen American competitiveness and expand economic opportunity, while protecting national security. https://t.co/Tr0sAzAxTD

7:13 PM · Jul 24, 2026 · 8.29M Views

* * *

1.22K Replies · 1.97K Reposts · 25.4K Likes

](https://x.com/finkd/status/2080733191237771648?s=61)

And then today he released a model that is NOT open-source, hoping you wouldn’t notice the difference between the two. And, sadly, the Times didn’t.

I implore them, and everyone else, for the love of Turing, please don’t confuse open-weight with open-source.

P.S. Bonus analogy; pick your favorite:

[

![X avatar for @vsistla](https://substackcdn.com/image/fetch/$s_!JfLT!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fpbs.substack.com%2Fprofile_images%2F1273119744275681282%2FJy7y-Avp.jpg)

Vamsi Sistla@vsistla

Open weights similar to compiled binary - you cannot see the source code and internal guts. It's like calling a river "open source" because you're free to swim in it. Access is not the same as knowing the watershed that feeds it.

![X avatar for @GaryMarcus](https://substackcdn.com/image/fetch/$s_!GPK6!,w_20,h_20,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fpbs.substack.com%2Fprofile_images%2F2048405471900606464%2FkPeRHI2z.jpg)

Gary Marcus @GaryMarcus

Sad to see the @nytimes confuse open-source (fully transparent) wi

[...content truncated for storage size]
