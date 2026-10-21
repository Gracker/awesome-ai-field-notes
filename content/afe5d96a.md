# Voxtral 3: Voice Agent SDK & Speech Models in 50+ Languages

- **ID**: afe5d96a
- **原文链接**: https://mistral.ai/news/voxtral-3
- **作者**: Mistral AI
- **日期**: 2026-10-21
- **分类**: agents
- **来源类型**: product
- **标签**: voice-agent, speech, tts, asr, mistral, tool-use
- **质量评分**: 4/5
- **抓取时间**: 2026-10-21T12:28:13.218278+00:00

---

## 中文导读

Mistral 发布 Voxtral 3：面向 50+ 语言的实时多轮语音智能体 SDK 与语音模型家族，同时要满足四件事——跨口音的准确转写、带情感自适应的自然语音合成、对所听内容的推理，以及打通工作流的深度工具集成。发布演示里 agent 直接转写法语转诊信、调用 get_referral、用英文向病人复述并经 book_appointment 完成预约。转写侧 Voxtral Small Transcribe 3 覆盖 50 种语言（含 24 种欧盟官方语言及多个低资源亚洲/印度语系语言），在多语转写、说话人分离与上下文偏置上标称 SOTA，官方口径超过 Whisper、Scribe v2 与 Gemini 3.5 Transcribe；Mini 转写为 4B 参数、$0.0035/分钟；Realtime 转写 35+ 语言、延迟低于 500ms，原生端点预测。TTS 侧 Voxtral Mini TTS 3 支持 35+ 语言 50+ 方言，$13/百万字符，按上下文自动调情感/语速/重音，30 分钟样本即可做 Pro Voice 音色适配。部署走 EU 托管 API 或自建，保数据主权。

## 为什么值得关注

语音 agent 进到下一层：50+ 语言实时对话里直接长出工具调用，演示一条龙是法语转诊信→get_referral→英文复述→book_appointment。对做呼叫中心、语音助手与免手 copilot 的团队，转写/TTS/agent SDK 一次到位，且 EU 托管或自部署两条路线都可控音频去留。

## 关键信息

- 发布方：Mistral AI
- 原文：https://mistral.ai/news/voxtral-3
- Voxtral Small Transcribe 3：50 语言转写/说话人分离/上下文偏置（FLEURS 45、cpWER、Earnings-22 keyphrase recall，对标 Whisper、Scribe v2、Gemini 3.5 Transcribe）
- Voxtral Mini Transcribe 3：4B 参数，$0.0035/min
- Voxtral Realtime Transcribe 3：35+ 语言，sub-500ms 延迟，原生端点预测
- Voxtral Mini TTS 3：35+ 语言 / 50+ 方言，$13/1M 字符，情感/语速/重音显式指令跟随，30+ 分钟样本音色克隆
- Pro Voice：30 分钟音频复现说话人特质、情感幅度与说话风格（跨语言）
- 部署：EU 托管 API 或自部署，音频处理位置与留存可控

## English Summary

Voxtral 3 introduces a cutting\-edge voice agent SDK and state\-of\-the\-art speech models designed for real\-time, multi\-step conversations across 50+ languages. It combines accurate transcription, natural speech synthesis with emotional adaptability, and deep tool integration for seamless workflow automation. Available via Mistral’s EU\-hosted API or self\-deployment, it ensures data sovereignty while delivering low\-latency, human\-like interactions for contact centers, virtual assistants, and hands\-free copilots.

## Obsidian Notes

- 内容由 `opencli web read` 抓取 Mistral 发布页全文生成，导读与关键信息均锚定在页面明示事实（模型、参数、定价、延迟、部署方式）上。
