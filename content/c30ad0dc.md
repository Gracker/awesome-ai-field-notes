---
id: c30ad0dc
title: Apertus 1.5: From Open Text Models to Open Multimodal Reasoners
url: https://arxiv.org/abs/2610.15542
source: Hermes 定时任务/AI-前沿一手源/2026-10-16-AI前沿一手源_Nemotron35-RuleTrek-SwarmRSI.md
added_date: 2026-10-17
category: models
quality_score: 4
---

# Apertus 1.5: From Open Text Models to Open Multimodal Reasoners

> 原文链接: https://arxiv.org/abs/2610.15542

## 要点 (中文)

公共机构全开源路线的 Apertus 家族从文本扩展到多模态推理。8B/70B 分别在 4T/2T 额外 token 上续训，新增图像与音频理解，上下文扩四倍至 262,144；多模态经 tokenizer 引入，语言模型头保持文本、架构不变。thinking 是聊天模板旗标而非独立模型，8B 数学推理最多提升 20 分。8B 在知识、指令跟随与文化基准上领先同级全开源模型，指令跟随超过包括开放权重在内的所有对比模型；继续只训公开数据、追溯尊重爬虫 opt-out，权重、数据配方、评测套件以宽松许可开放。

## Key claims (English)

Apertus 1.5 extends the fully open Apertus family to multimodal reasoning: continued pretraining on 4T (8B) / 2T (70B) tokens adds image and audio understanding and a 262,144-token context, with multimodality entering through the tokenizer. Thinking is a chat-template flag lifting math reasoning by up to 20 points on the 8B; the 8B leads fully open peers on knowledge and instruction following and surpasses all compared models including open-weight ones.

## Obsidian 证据摘录

> Apertus 1.5（34）— 公共机构路线的开源文本模型族扩到多模态推理；强调 documented data / 开放基础设施叙事。publishedAt 页述 2026-10-11。
> —— Hermes 定时任务/AI-前沿一手源/2026-10-16-AI前沿一手源_Nemotron35-RuleTrek-SwarmRSI.md

## 原文抓取

arXiv abstract page (submitted 11 Oct 2026)

Authors: Project Apertus: Yixuan Xu (1), Yassine Turki (2), Vinko Sabolčec (2), Valentina Pyatkin (1), Tommy Chu (2), Sven Najem-Meyer (2), Sean F. Carroll (2), Robert Smith (1), Raphael Kreft (1), Oscar Alessandro Tazza (1), Oleg Lavrovsky (2), Nicola Irmiger (1), Matteo Santelmo (2), Marian Schneider (1), Juan García Giraldo (2), Hanna Yukhymenko (1), Eduard Ďurech (1), Davit Melikidze (1), Dani Tamayo (2), Bettina Messmer (2), Aryan Ahadinia (2), Anunay Yadav (2), Allen Huang (2), Ahmad Fraij (1), Alessandro Bombarda (2), Alex Padula (1), Alexander Hägele (2), Alexander Sternfeld (3), Anna Hedström (1), Anna Kosovskaia (1), Arthur Wuhrmann (2), Arundhati Balasubramaniam (1), Badr Al Mahouri (2), Barna Pasztor (1), Bartosz Szostakiewicz (1), Bich Ngoc Doan (2), Bryan Schmid (4), Burak Sezen (1), Camille Challier (2), Clément Charmillot (2), Dana Shayakhmetova (2), Daniel Perruchoud (4), David Brüggemann (5), David Isztl (6), Elia Palme (6), Emma Anastassova (2), Fabian Bösch (6), Faruk Zahiragić (2), Fawzi Roberto Mohamed (6), Fiona Panicali (4), Florian Kolly (2), Flynn Guerra (4), Francesco Monti (2), Frederike Lübeck (1), Gennaro Oliva (6), Haofeng Yang (1), Haoliang Shang (1), Helen El Khoury (2), Henrique Mendonça (6), Jannis Vamvas (7), Jérome Landolt (4), Jessica Lam (1), Jingchun Xiao (1), Jonathan Coles (6), Joshua Oyebanji (2), Khanh Nguyen (2), Konstantinos Pitas (1), Lasse B. Strand (1), Li Mi (1), Loïc Deslarzes (2), Lorenzo Baggi (1), Lorenzo Noci (1), Luca Baumann (1), Luca Sartori (1), Lukas Drescher (6), Marco De Negri (1), Marco Passerini (6), Mark Klein (6), Marko Stojanovic (2), Martin Majsec (2), Matin Ansaripour (2), Mattea Busato (2), Mauro Pellonara (2), Max Neuwinger (1), Michael Graber (4), Michal Tešnar (1), Michelle Wastl (7), Miguel Gila (6), Mikolaj Boronski (2), Morgane Magnin (2), Moritz Reihs (1), Mukhammadali Sayfiddinov (1), Nathan Ranchin (1 and 2), Nicolas Cuveillier (2), Oscar Wohlfahrt (2), Qianqian Zou (5), Rada Kamysheva (1), Rita Sevastjanova (1), Roman Machacek




  
         (8), Sebastian Keller (6), Simon Matrenok (2), Simon Pierre (2), Stefano Schuppli (6), Suei-Wen Chen (1), Szabina Horváth-Mikulas (2), Taliesin Perez (2), Thilo Spinner (1), Thomas Kleine Buening (1), Tim Robinson (6), Tymoteusz Kwiecinski (1), Vilém Zouhar (1), Vinzenz Thoma (1), Xiaozhe Yao (1), Yannick Metz (1), Yuhei Fukuhara (2), Yusif Askari (2), Zixuan Chen (1), Alexander Ilic (1), Ana Klimovic (1), Andreas Krause (1), Andrei Kucharavy (3), Elliott Ash (1), Joost VandeVondele (6), Martin Rajman (2), Mennatallah El-Assady (1), Thomas Schulthess (6), Timo Kehrer (8), Torsten Hoefler (1), Antoine Bosselut (2), Martin Jaggi (2), Imanol Schlag (1) ((1) ETH Zurich, (2) EPFL, (3) HES-SO Valais-Wallis, (4) FHNW, (5) SDSC, (6) CSCS, (7) University of Zurich, (8) University of Bern)
Subjects: 

Language models are becoming infrastructure, and infrastructure built in the open, by public institutions, on documented data, is the alternative to dependence on a few providers; Apertus shows this is viable at scale. Apertus 1.5 extends the fully open Apertus family from text to multimodal reasoning. Continued pretraining of the Apertus 1.0 models, on 4T additional tokens for the 8B and 2T for the 70B, adds image and audio understanding and extends the context window fourfold to 262,144 tokens; multimodality enters through the tokenizer, the language-model head remains restricted to text, and the architecture is unchanged. Supervised finetuning, long-context finetuning, reinforcement learning with verifiable rewards, and preference alignment complete the released models. Thinking is a flag of the chat template rather than a separate model, and lifts mathematical reasoning by up to 20 points on the 8B model. The released models improve over their predecessors on nearly every benchmark; among fully open models of its class, the 8B leads on knowledge, instruction following, and cultural benchmarks, and its instruction following surpasses all compared models, including open-weight ones. On image and audio understanding, a first for the family, the models are competitive with fully open multimodal models, strongest on document understanding and long-form and lower-resource speech recognition, while specialized vision and audio models remain ahead on perception and transcription of English and other high-resource languages. As in Apertus 1.0, we train only on openly available data, respect crawler opt-outs retroactively, and exclude restrictively licensed material. We release the model weights, data preparation and training recipes, and evaluation suites under permissive licenses; openness extends to values, with the Apertus charter guiding alignment stages published alongside the models.
