# Gemini on Android, The story so far

> 作者: https://www.linkedin.com/in/iurysouza/
> 发布时间: 2024-10-17T17:39:24Z
> 原文链接: https://iurysouza.dev/gemini-on-android/

---
![Gemini on Android, The story so far](/static/3e82cf97be766f82819dcb3fcb1a554f/d56fe/gemini-android-cover.png)

# Here we go again

Right. Another article about AI. I’m sure you’ve read enough about it so far, but chances are that if you landed here, you have at least some vague interest in it. I, for one, am very interested on the tech and with the direction this is going, especially with what has just started to roll out. FYI: if I say AI in this article, I probably mean [LLM](https://en.wikipedia.org/wiki/Large_language_model).

# On-Device LLMs are here!

Google just [announced](https://android-developers.googleblog.com/2024/10/gemini-nano-experimental-access-available-on-android.html) their Android AICore beta program, and with it, we finally got access to Gemini Nano with AI Edge SDK via AICore. Did Android smartphones just got smarter? Well.. kinda.

  ![AICore Beta Program](/static/0cba80e463bffc7fe1088c011170e100/d2d21/ai-core-beta-crop.png)

AICore Beta Program

Now, honestly, this is nothing short of amazing. The thing is that we’re on 2024, and so overwhelmed with information that it is sometimes hard to appreciate just how incredible this last paragraph reads. Especially if you’re sceptic (and rightfully so) about all the AI bros selling snake oil out there, but I digress.

It was just in November 2022 that OpenAI released ChatGPT-3.5, the first version to become wildly popular, and here we are now, less than two years later, with a somewhat comparable model running **ON DEVICE!**

But how did we get here?

# Android 🤝 LLMs - Quick Recap

  ![AI at the core](/static/b2748a5c12926680016334b7cf71423d/0516a/ai-at-the-core.jpg)

AI at the core

This story started back in 2023 with the Pixel 8 lineup, the first smartphones to ship with [Google Tensor](https://blog.google/products/pixel/google-tensor-g3-pixel-8/) processors that were good enough for LLM inference.

This enabled the devices to run LLMs locally, though initially limited to just a handful of apps and features, like smart replies and the recorder transcript summarization. There was a program that you could enroll to get access to Gemini Nano, but that was kinda restrictive. So no open access yet.

![Transcript Summarization](/a3195d2670b5ad5587ef158768647e8c/pixel-8-summary.webp)

![Pixel 8 Improved Voice Model](/60406d1c83c25e3c44113da747a9d0b6/pixel-voice.webp)

> But of course, on-device generative AI is really complex: 150 times more complex than the most complex model on Pixel 7 just a year ago. Tensor G3 is up for the task, with its efficient architecture co-designed with Google Research.
>
> [Source](https://blog.google/products/pixel/google-tensor-g3-pixel-8/)

# Generative AI SDK

A few months later, around December last year, Google started gearing up and stealthily releasing the [Generative AI SDK](https://github.com/google-gemini/generative-ai-android), which made it easier to play with the Gemini API. This one was **not running on device**, though.

It was still very limited, and clearly not a lot of resources were put into it. Heck, it was not really announced anywhere. Besides, it was still blocked in a lot of countries (Europe) by that time.

That happened right around the time I was building my first Gen AI app. You can read more about that here: [Building an AI Audio Guide - Part 1](../prototyping-an-ai-app-part-1/) . I was mainly targeting OpenAI’s API back then, but I was able easily hook up Gemini using that SDK. Quality was still not there yet, but it worked.

# Vertex AI for Firebase

Fast forward another six months, and we’re at Google I/O Connect 2024. Now, a joint venture with [Vertex AI](https://cloud.google.com/vertex-ai?hl=en) and [Firebase](https://firebase.google.com/) was announced. Vertex AI is Google’s Cloud solution for AI products and now, app clients could tap into it without having to deal with GCP.

What I got from this was that while the Generative AI SDK was OK for prototyping, Firebase Gen AI was meant to be a secure and more robust channel for production use.

# Any Local LLMs Yet?

During that same _Connect_ event, Google announced that Android would soon open up access to core APIs for on-device LLM inference. Some architecture diagrams were shown about this new AI Core thing. But still nothing for us devs to play with.

Then, a couple of months later, the Pixel 9 family was launched with more Gen AI stuff and a slightly better Chip in terms of raw performance, but with a new TPU (Tensor Processing Unit) for faster LLM inference, [reportedly](https://9to5google.com/2024/08/19/google-tensor-g4-pixel-9-interview/) at 45 tokens (which is pretty decent) per second now. Also, it’s interesting to notice that these devices shipped with min 16GB RAM out of which [3GB reserved](https://www.androidauthority.com/tested-pixel-9-pro-ai-ram-3472624/) just for LLM inference.

> Pro models lock 3GB RAM exclusively for AICore and the Tensor’s TPU.

Yes, you read that right. Almost 20% of device memory reserved for AI. Also, you should expect multiple GBs of model data stored locally (more about that later). This should not be taken lightly. They mean business!

Ok, so _finally_, on October 1st, [**Gemini Nano with Google AI Edge SDK**](https://developer.android.com/ai/gemini-nano/experimental) was open for us devs 🎉. Well, at least for _beta_ testing.

> Gemini Nano experimental access is designed for developers seeking to test enhancement of their apps with cutting-edge on-device AI capabilities.

# Gemini Nano

The Gemini Nano model is specifically optimized for on-device use, which means that it can runs completely locally.

[Nano](https://deepmind.google/technologies/gemini/nano/) is the smallest of the Gemini lineup, with [Flash](https://deepmind.google/technologies/gemini/flash/), [Pro](https://deepmind.google/technologies/gemini/pro/) and [Ultra](https://deepmind.google/technologies/gemini/ultra/) being the other ones. It is the most efficient version and because of that it needs to be much smaller, with Nano-1 and Nano-2 models being only 1.8B and 3.25B parameters, respectively. For comparison, Gemini 1.5 Pro has 1.5 trillion - with a T (note that these things don’t exactly scale linearly though). Due to this size difference it had to make some compromises, but still managed to perform remarkably well.

How? Quoting straight from the [Gemini paper](https://arxiv.org/pdf/2312.11805#page=20.45):

> The power of Nano lies in its training process, which involves “distilling” knowledge from the larger Gemini models. This approach allows Nano to deliver substantial computational power in a smaller form factor, making AI more personal and accessible.

This model is not as general as the other ones. Being smaller, is better suited for some specific tasks, also quoting the paper:

> These models excel in summarization and reading comprehension tasks with per-task fine-tuning.

You can see these features in action on some of the new Pixel apps like the [AI Weather Report](https://www.androidpolice.com/google-new-ai-weather-summaries/) of the new Pixel Weather App and the [Pixel Screenshots](https://store.google.com/intl/en/ideas/articles/pixel-screenshots/) app.

To get started with it you have to enrol on the beta program. This will enable you to update the AICore app which comes installed on the Pixel 8 and 9. After that you can start using the SDK.

_Note: I’m purposefully skipping the [MediaPipe LLM](https://ai.google.dev/edge/mediapipe/solutions/genai/llm_inference) Inference API, released early 2024, because using it is more involved and requires us to manually push models (non Gemini) to the device. I’ll try to revisit it later._

# What’s next?

Welcome to the new normal. Some people loathe it, but this has been an open secret for years. This vision of a shift from a mobile-first to an AI-first world was [announced](https://blog.google/technology/ai/making-ai-work-for-everyone/) by Sundar himself back in 2017 and I can only see it accelerating.

  ![The Big Shift](/static/921d4e86a85576fd1d22cd8c174df492/5c837/shift-mobile-first-ai-first.png)

The Big Shift

I could write another article just about this vision and what it means for mobile dev, especially us Android Developers, which for years were used to be in the very center of everything Google announced (remember IO 2018?) and now are left feeling a bit alienated by these changes. But let’s do that another time. For now, I’ll just say that mobile is still the platform. AI will be just another tool in our belt.

This was a just a short recap of how we got here, I’m trying to keep these in a shorter format, so I’ll have to wrap this up. But if you’re interested in learning more, like and subscribe 😛.

I’m currently playing with the Nano model on the Pixel 9 and hope to put together some of my notes into another article about my first impressions and some ideas of how you can try implementing LLM based features on **any** device.

[#ai](/tags/ai/)[#gemini](/tags/gemini/)[#android](/tags/android/)