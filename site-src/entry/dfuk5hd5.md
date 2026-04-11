---
title: 'Chain-of-Tools - 在冻结 LLM 的 CoT 推理中利用海量未见工具'
sidebar: false
---

::: info
[← 返回学习资源](/learning)
:::

# Chain-of-Tools - 在冻结 LLM 的 CoT 推理中利用海量未见工具

> LLM 推理能力增强的新方法

🔗 [原文链接](https://arxiv.org/pdf/2503.16779) | 🇨🇳 | ⭐⭐⭐⭐⭐ 5 ⭐5 5/5 📅 2026-04-10

`fine-tuning` `coding` `agent` `tool-use` `llm` `paper` `reinforcement-learning` `reasoning`

---

Chain-of-Tools: Utilizing Massive Unseen Tools in the CoT Reasoning of
|     |            |     |     |             | Frozen Language | Models       |            |     |     |
| --- | ---------- | --- | --- | ----------- | --------------- | ------------ | ---------- | --- | --- |
|     | MengsongWu |     |     |             | TongZhu         | HanHan       | XiangZhang |     |     |
|     |            |     |     | WenbiaoShao |                 | WenliangChen |            |     |     |
SoochowUniversity,ShiziStreet1,215006Suzhou,China
{mswumsw,tzhu7,hhan,xzhangxzhang23,wbshao}@stu.suda.edu.cn, wlchen@suda.edu.cn
|     |     | Abstract |     |     |     | pingLLMagentwithexternaltoolsisareasonable |     |     |     |
| --- | --- | -------- | --- | --- | --- | ------------------------------------------ | --- | --- | --- |
solution. That’swhattheToolLearning(Qinetal.,
Toollearningcanfurtherbroadentheusagesce-
|                                    |     |     |     |     |      | 2023a)taskinvestigates: |     | howtomakeLLMsbetter |     |
| ---------------------------------- | --- | --- | --- | --- | ---- | ----------------------- | --- | ------------------- | --- |
| nariosoflargelanguagemodels(LLMs). |     |     |     |     | How- |                         |     |                     |     |
5202 raM 12  ]LC.sc[  1v97761.3052:viXra
utilizetoolsintheprocessofreasoning?
evermostoftheexistingmethodseitherneed
| to finetune |     | that the | model | can | only use tools |     |     |     |     |
| ----------- | --- | -------- | ----- | --- | -------------- | --- | --- | --- | --- |
UserQuery
| seen | in the | training | data, | or add | tool demon- |     |     |     |     |
| ---- | ------ | -------- | ----- | ------ | ----------- | --- | --- | --- | --- |
strationsintothepromptwithlowerefficiency. What's the weather like at my destination tomorrow?
| In this | paper, | we  | present | a new | Tool Learn- |     |     |     |     |
| ------- | ------ | --- | ------- | ----- | ----------- | --- | --- | --- | --- |
Agent
| ingmethodChain-of-Tools. |     |     |     | Itmakesfulluse |     |     |     |     |     |
| ------------------------ | --- | --- | --- | -------------- | --- | --- | --- | --- | --- |
Generateoutputtexttokenbytoken.
ofthepowerfulsemanticrepresentationcapa-
|                                         |     |     |     |     |     | Answerthefollowingquestionstepbystep. |     |     | prompt |
| --------------------------------------- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | ------ |
| bilityoffrozenLLMstofinishtoolcallingin |     |     |     |     |     | (RelevantICLDemos)                    |     |     |        |
input
CoT reasoning with a huge and flexible tool Question: What's the weather like at my
|      |       |             |     |        |              | destinationtomorrow? |     |           | output              |
| ---- | ----- | ----------- | --- | ------ | ------------ | -------------------- | --- | --------- | ------------------- |
| pool | which | may contain |     | unseen | tools. Espe- |                      |     |           |                     |
|      |       |             |     |        |              | Answer: Tomorrow     | you | will take | part in toolcalling |
cially, to validate the effectiveness of our ap- NLPconference,Shanghai.Theweatherin result
| proach       | in the | massive |         | unseen          | tool scenario, | Shanghaiwillbesunny… |     |            |     |
| ------------ | ------ | ------- | ------- | --------------- | -------------- | -------------------- | --- | ---------- | --- |
| we construct |        | a new   | dataset | SimpleToolQues- |                |                      |     | Schedule() |     |
Weather()
| tions. | Weconductexperimentsontwonumer- |     |     |     |     |     |     |     |     |
| ------ | ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
icalreasoningbenchmarks(GSM8K-XLand Whenever a token is to be generated,
determine whether to call atoolhere?
FuncQA)andtwoknowledge-basedquestion
|                                            |     |     |     |     |     | ToolJudge |     |     | Generatenexttoken.# |
| ------------------------------------------ | --- | --- | --- | --- | --- | --------- | --- | --- | ------------------- |
| answeringbenchmarks(KAMELandSimple-        |     |     |     |     |     |           |     | NO  |                     |
| ToolQuestions).Experimentalresultsshowthat |     |     |     |     |     |           | YES |     |                     |
ourapproachperformsbetterthanthebaseline. ToolCalling Weather:sunny Addinanswer.#
Wealsoidentifydimensionsofthemodelout-
Reply
| put that | are   | critical          | in tool | selection, | enhanc-      |        |       |     |     |
| -------- | ----- | ----------------- | ------- | ---------- | ------------ | ------ | ----- | --- | --- |
|          |       |                   |         |            |              | Answer | sunny |     |     |
| ing the  | model | interpretability. |         |            | Our code and |        |       |     |     |
data are available at: https://github.com/ Thought Tomorrow you will take part in NLP
|     |     |     |     |     |     |     | conference, | Shanghai. | The weather in |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --------- | -------------- |
fairyshine/Chain-of-Tools.
Shanghaiwillbesunny.Haveaniceday!
ToolCalling
1 Introduction
POST1 Schedule(date:tomorrow)
GET1 NLPconference,Shanghai
| The development |     | of  | autonomous |     | agent systems |     |     |     |     |
| --------------- | --- | --- | ---------- | --- | ------------- | --- | --- | --- | --- |
(Wang et al., 2024; Xi et al., 2023), propelled by POST2 Weather(location:Shanghai,date:tomorrow)
GET2 weather:sunnytemperature:18-26℃
| real-world | applications |     | (Achiam |     | et al., 2023) of |     |     |     |     |
| ---------- | ------------ | --- | ------- | --- | ---------------- | --- | --- | --- | --- |
Large Language Models (LLMs), has become a Figure 1: The ideal tool calling procedure.Take the
popularfocusinbothacademicandindustrycom-
inputquery"What’stheweatherlikeatmydestination
munities. Benefit from LLM’s emergent ability tomorrow?"asanexample.
(Weietal.,2022a;Zhaoetal.,2023)tothinkques-
tionscomprehensivelyandintegratedly,LLMagent TherearetwokindsoftypicalmethodsforTool
may give brilliant step-by-step solutions during Learning. (1) Fine-tuning based methods like
multiple-turnchatwithusers. DespiteLLMisex- API-Bank (Li et al., 2023) and ToolLLM (Qin
pertinlogicalreasoningandbreakingdownprob- et al., 2023b) can efficiently and precisely call
lems,itcan’taccomplishalotofspecifictaskslike toolswhichhavebeenseenduringtraining,while
calculatingmathformulasordrawingpaintings. In the general capabilities of LLMs such as emer-
order to extend the application scenarios, equip- gent ability and Chain of Thought (CoT) might

be influenced by fine-tuning (Wei et al., 2022b). alsobecomputedfromtheirdescriptionforflexible
ToolkenGPT(Haoetal.,2024)introducesamethod retrieval. What’s more, since the LLM is frozen,
whichonlyfine-tunesextratool-tokenembeddings itsCoTreasoningabilityremainsunaffected.
without hurting the original model, but it still Contributionsofthispaperarelistedasfollow-
| can’t use | unseen | tools. | (2) | In-context | learning |     |     |     |     |     |     |
| --------- | ------ | ------ | --- | ---------- | -------- | --- | --- | --- | --- | --- | --- |
ing:
(ICL)basedmethodslikeHuggingGPT(Shenetal.,
2024)andAgentBench(Liuetal.,2023)areflexi- • ThenewToolLearningmethodCoToolscan
bletocallunseentoolswithICLprompt,whileit utilizemassiveunseentoolsefficientlyinthe
is less efficient in reasoning when given massive process of CoT reasoning with the frozen
tools. TheabovemethodsinTable1haveshowna LLM.Itfullyexploresthegenerationcapabil-
certainsuccessinutilizingtoolsintheLLMagents. ityandthesemanticrepresentationcapability
However,wearguethattheLLMagentshouldbe of the LLM for better Tool Learning proce-
capableofefficientlymanagingalargeamountof dure. Unseentoolscanbeeasilyequippedfor
tools and fully utilizing unseen ones during the toolselectionwiththeirdetaileddescriptions
CoT reasoning, as many new tools may emerge withoutintroducingexternalretriever.
dailyinreal-worldapplicationscenarios.
|     |     |     |     |     |     | • We | construct | the dataset | SimpleToolQues- |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --------- | ----------- | --------------- | --- | --- |
tions(STQuestions)including1836toolsto
| ToolLearning |     | Frozen | Massive | Unseen | Abilityto |     |     |     |     |     |     |
| ------------ | --- | ------ | ------- | ------ | --------- | --- | --- | --- | --- | --- | --- |
Plugable
Paradigms LMs Tools Tools UseExtensiveData evaluate the tool selection performance of
|     |     | ✘   | ✘ ✘ | ✘   | ✔   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Fine-tuning
In-ContextLearning ✔ ✔ ✘ ✔ ✘ eachmethod. Comparedwithformerbench-
| ToolkenGPT |     | ✔   | ✔ ✔ | ✘   | ✔   |     |     |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
CoTools(Ours) ✔ ✔ ✔ ✔ ✔ marks,itfocusesonevaluatinginthemassive
unseentoolscenario.
Table1: ComparisionofthemainstreamToolLearning
| paradigms. | "Plugable"meansthattoolscanbeflexibly |     |     |     |     |       |          |             |     |         |        |
| ---------- | ------------------------------------- | --- | --- | --- | --- | ----- | -------- | ----------- | --- | ------- | ------ |
|            |                                       |     |     |     |     | • For | detailed | evaluation, | we  | conduct | exper- |
loaded. "Abilitytouseextensivedata"meansthattrain-
|     |     |     |     |     |     | iments | on  | four benchmarks: |     | GSM8K-XL, |     |
| --- | --- | --- | --- | --- | --- | ------ | --- | ---------------- | --- | --------- | --- |
ingdatacanbeusedtoimprovetheperformanceofthe
method. (ThetableispartiallyreferencedfromTable1 FuncQA,KAMELandSTQuestions. Exper-
inthepaperofToolkenGPT.) imental results show that CoTools performs
betterthanbaselineinbothnumericalreason-
ingandknowledge-basedquestionanswering.
| In this | paper, | we  | introduce | Chain-of-Tools |     |     |     |     |     |     |     |
| ------- | ------ | --- | --------- | -------------- | --- | --- | --- | --- | --- | --- | --- |
(CoTools), a brand new fine-tuning based Tool Moreover,wediscoverthekeydimensionsof
thehiddenstatesfortoolselection,whichmay
| Learningmethod. |     | Wefollowthewayoffine-tuning |     |     |     |     |     |     |     |     |     |
| --------------- | --- | --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
enhancetheinterpretabilityofthemodel.
basedmethodsinceitismuchmoreefficienttocall
| tools which | is  | critical | for practical |     | applications. |     |     |     |     |     |     |
| ----------- | --- | -------- | ------------- | --- | ------------- | --- | --- | --- | --- | --- | --- |
2 RelatedWork
Theremainingproblemishowtoeffectivelyutilize
unseentoolsintheprocessofCoTreasoningwith-
2.1 ToolLearning
| outhurtingthemodel’scapability. |     |     |     | Inordertoad- |     |     |     |     |     |     |     |
| ------------------------------- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
dressthisproblem,wedesigntheidealToolLearn- ToolLearning(Qinetal.,2023a)enablesfounda-
ing procedure shown in Figure 1. CoTools fully tionmodelstoleveragespecializedexternaltools.
|          |           |          |                 |     |       | LLMs then | can | accomplish | much | more | complex |
| -------- | --------- | -------- | --------------- | --- | ----- | --------- | --- | ---------- | ---- | ---- | ------- |
| utilizes | the token | semantic | representation, |     | which |           |     |            |      |      |         |
is often called as the hidden states generated by tasksinrealisticscenarios.
LLMs, as input to judge where to call tools and Fine-TuningbasedToolLearning
select which tools to call (e.g. "Weather" tool in Mostoftheseresearchesconstructrelevanttool
Figure 1) then the tool calling result is added in datasets to fine-tune LLMs. Toolformer (Schick
the answer (e.g. "sunny" in Figure 1). First, the et al., 2024) explores how to generate tool learn-
userqueryispromptedwithICLandCoTbefore ing data with raw dataset given. API-Bank (Li
beinginputtedintotheLLM.ThenCoToolsjudges etal.,2023)buildsthecomprehensivetoollearning
whethertocallatoolwiththehiddenstateofnew benchmark with tools in many fields. GeneGPT
answer token when the LLM is generating every (Jin et al., 2024) uses NCBI web APIs as tools
answer token. If tool calling is needed, CoTools to validate the model’s ability to call tools under
calculates query vectors and tool vectors respec- a specific field. Gorilla (Patil et al., 2023) takes
tivelywithcorrespondinghiddenstatesgivenfor online models from platforms like HuggingFace
toolselection. Thetoolvectorsofunseentoolscan astoolstoextendtheusagescenariosoftoolcalls.

ToolLLM(Qinetal.,2023b)generatesdatasetTool- findsitworkthataddthephrase"Let’sthinkstepby
Benchwithmassiverealworldtoolsandalsopro- step."inprompt. Thephraseisnowwidespreadly
pose a multi-step tool learning inference method usedinthepromptengineeringofLLMs. Thereare
DFSDT. API-BLEND (Basu et al., 2024) aggre- alsoattemptstocombineZero-shot-CoTandTool
gates the various types of datasets available with LearningtogetherlikeChatCoTandToolkenGPT.
elaborateanalysis. ToolkenGPT(Haoetal.,2024) It’s helpful to improve tool selection and invoca-
doesn’tadaptmodelweightsbutaddmanyspecial tionbymodelsforcomplexproblems. Subsequent
tokensinthevocabulary. Onespecialtokenrepre- attemptscanbemadetoutilizeimprovedversions
sentsoneexternaltool. Thecorrespondingtoolis ofCoTsuchasTreeofThoughts(Yaoetal.,2024)
calledwhenthemodelgeneratesthespecialtoken. tocompleteToolLearningtask.
| ToolkenGPT            | just need | to                     | train the | token embed- |     |               |     |     |     |     |     |     |
| --------------------- | --------- | ---------------------- | --------- | ------------ | --- | ------------- | --- | --- | --- | --- | --- | --- |
| dingwhichisefficient. |           | CoToolsdoesnottrainthe |           |              |     | 3 Methodology |     |     |     |     |     |     |
foundationmodelbutpost-processingmodulesfor
|     |     |     |     |     |     | In this | section, | we  | introduce | Chain-of-Tools, |     | a   |
| --- | --- | --- | --- | --- | --- | ------- | -------- | --- | --------- | --------------- | --- | --- |
thehiddenstatesoutputbythemodel.
|     |     |     |     |     |     | novelfine-tuningbasedToolLearningmethod. |     |     |     |     |     | The |
| --- | --- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- |
In-ContextLearningbasedToolLearning
coreideaofCoToolsistoleveragethesemanticrep-
In-contextlearning(Brownetal.,2020)isone
resentationcapabilitiesoffrozenfoundationmod-
| of the most | prominent | capabilities |     | of the LLMs. |     |     |     |     |     |     |     |     |
| ----------- | --------- | ------------ | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
elsfordeterminingwheretocalltoolsandwhich
| With the | help of ICL, | the | model | performance | in  |              |     |                              |     |     |     |     |
| -------- | ------------ | --- | ----- | ----------- | --- | ------------ | --- | ---------------------------- | --- | --- | --- | --- |
|          |              |     |       |             |     | toolstocall. |     | ThefoundationmodelMisusually |     |     |     |     |
thefew-shotscenarioofmanytaskshasimproved
anauto-regressivelanguagemodelthatwouldgen-
| dramatically.    | ICLhasbecomeabasictrickinthe |                         |     |        |         |                            |     |     |        |                    |                |     |
| ---------------- | ---------------------------- | ----------------------- | --- | ------ | ------- | -------------------------- | --- | --- | ------ | ------------------ | -------------- | --- |
|                  |                              |                         |     |        |         | erateoutputtoken-by-token. |     |     |        | Giventheinputtoken |                |     |
| wideusageofLLMs. |                              | Thereisnoexceptioninthe |     |        |         |                            |     |     |        |                    |                |     |
|                  |                              |                         |     |        |         | listoflengthn[x            |     | ,x  | ,...,x | ](x                | ∈ V,V isthevo- |     |
|                  |                              |                         |     |        |         |                            |     | 1   | 2      | n                  |                |     |
| Tool Learning    | task.                        | TaskMatrix.AI           |     | (Liang | et al., |                            |     |     |        |                    |                |     |
cabularyofM)whichistokenizedfromtheinput
2023)proposesthemultimodalconversationalsys-
text,themodelMcangeneratethehiddenstateof
temtoequipthefoundationmodelwithrichcross-
|                               |     |     |     |             |     | the last | token, | which | is called | h   | (h ∈ | Rd, d is |
| ----------------------------- | --- | --- | --- | ----------- | --- | -------- | ------ | ----- | --------- | --- | ---- | -------- |
|                               |     |     |     |             |     |          |        |       |           | n   | n    |          |
| modaltoolsfromtheAPIplatform. |     |     |     | Huggingface |     |          |        |       |           |     |      |          |
thedimofthehiddenstates):
| models                      | are also treated | as  | tools | in the paper  | of  |     |     |       |     |        |     |     |
| --------------------------- | ---------------- | --- | ----- | ------------- | --- | --- | --- | ----- | --- | ------ | --- | --- |
| HuggingGPT(Shenetal.,2024). |                  |     |       | ToolDoc(Hsieh |     |     |     |       |     |        |     |     |
|                             |                  |     |       |               |     |     | h   | = M(x | ;x  | ,...,x | )   | (1) |
|                             |                  |     |       |               |     |     |     | n     | n   | 1      | n−1 |     |
etal.,2023)providestooldocumentionsasanaler-
native to tool demonstraions which are added in Thenwecangetthenexttokenx caculatedby
n+1
| ICL prompt. | AgentBench |     | (Liu | et al., 2023) | is a |                       |     |     |     |      |     |     |
| ----------- | ---------- | --- | ---- | ------------- | ---- | --------------------- | --- | --- | --- | ---- | --- | --- |
|             |            |     |      |               |      | thelanguagemodelheadH |     |     |     | ofM: |     |     |
LM
comprehensiveagentbenchmarkforbothcommer-
| cialandopen-sourcedLLMs. |     |     | ToolTalk(Farnand |     |     |     |     | x   | = H | (h ) |     | (2) |
| ------------------------ | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- | ---- | --- | --- |
|                          |     |     |                  |     |     |     |     | n+1 |     | LM n |     |     |
Shin,2023)evaluatesGPT-3.5andGPT-4(Achiam
etal.,2023)withOpenAIAPI,whichemphasizes Insteadofjustbeingusedtogeneratethenexttoken
tools that affect the external world such as send- asusual,thehiddenstateh playsanimportantrole
n
| ing emails. | TaskWeaver | (Qiao | et  | al., 2023) | asks | inourmethod. |     |     |     |     |     |     |
| ----------- | ---------- | ----- | --- | ---------- | ---- | ------------ | --- | --- | --- | --- | --- | --- |
themodeltocalltoolsintheformatofgenerating ThemainstructureofCoToolscontains3parts:
pythoncode. Toolsinitarepythonfunctionswhich ToolJudge,ToolRetrieverandToolCallinglikein
canbeexecuted. ChatCoT(Chenetal.,2023)gen- Figure2. TheToolJudgedetermineswhetheror
eratesiterativetool-augmentedreasoningaccord- nottoinvokeatoolduringtheCoTreasoningpro-
ingtothegivenproblem. CoToolsdoesnotusethe cess. TheToolRetrieverselectsthemostsuitable
ICLpromptfortoolselection,therebyenhancing tool based on the query and the answer fragment
efficiencyinmassivetoolscenarios. ItusestheICL thathasbeengenerated. TheToolCallingfillsin
prompttofillintoolparameterswithtoolcalling parameters of the selected tool with ICL prompt,
| demonstrationsgiven. |     |     |     |     |     | executesitandgetsthereturnvalue. |     |     |     |     |     |     |
| -------------------- | --- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- | --- | --- | --- |
2.2 ChainofThought
|     |     |     |     |     |     | 3.1 ToolJudge: |     | WhetherCallingTools |     |     |     |     |
| --- | --- | --- | --- | --- | --- | -------------- | --- | ------------------- | --- | --- | --- | --- |
Promptlearningisdevelopingrapidlywiththerise TheToolJudgeJ isusedfordeterminingwhether
of LLMs. Chain of Thought is firstly proposed tocallatoolatthespecificpositionofanswer. Itis
| inWeiet | al. (2022b). | It encouragesthemodel |     |     | to  |     |     |     |     |     |     |     |
| ------- | ------------ | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
calculatedwiththeinputhiddenstatesh:
generatethoughtaboutthequestionthatleadstoa
|               |                                 |     |     |     |     |      | WJ  | ((σWJ |      | (h))⊗WJ(h)) |     |     |
| ------------- | ------------------------------- | --- | --- | --- | --- | ---- | --- | ----- | ---- | ----------- | --- | --- |
| betteranswer. | Zero-shot-CoT(Kojimaetal.,2022) |     |     |     |     | J(h) | =   |       |      |             |     | (3) |
|               |                                 |     |     |     |     |      |     | down  | gate |             | up  |     |

TaskPrompt RetrievalPrompt Tool DataBase
ToolPool
Answer
Query
Query
AnswerFragment
Ⅰ.ToolJudge NO
YES
Tool Vectors
Query Vector
…
Similarity
…
CoTReasoning ToolSelection
ToolPrompt
ToolName
Generate ToolDescription
FoundationModel LM Next Management
Head Token
• AddTools
# • RemoveTools
• ExecuteTools
ToolJudge FoundationModel FoundationModel
Query Encoder Tool Encoder
Ⅲ.ToolCalling
Calling Prompt
Foundation Model Score
Tool Doc Demo
Query
Tool Execution
AnswerFragment MAX
Add in Answer# Ⅱ.ToolRetriever
Figure2: OverviewofthemethodCoTools. JustliketheexampleinFigure1,CoToolsjudgeswhethertocalla
toolwheneveranewanswertokenistobegenerated. TheanswerFragmentmeanstheanswertextthathasbeen
generatedbythefoundationmodel.
Judge Encoder 0.5),weattempttocallatoolhere. Otherwise,the
Foundation Model
modeloutputsthenexttokenx withEquation2.
norm t+1
We train J as the sequence labeling task. The
ToolJudge down weighting
objectivefunctionisthebinarycrossentropyloss:
+
×
Tool Retriever
σ down
L = L (Score ,Label) (5)
QueryEncoder × Judge BCE J
gate up
σ
gate up whereLabel ∈ {0,1}.
ToolEncoder
3.2 ToolRetriever: FindNeededTools
(a) (b) (c)
TheToolRetrieverconsistsoftheQueryEncoder
Figure3: Compositionandstructureofthemodel. The E andtheToolEncoderE . Bothofthemareused
Q T
parameters of the foundation model are frozen. We tocalculatethevectorsforretrieval. TheQueryEn-
onlytrainthetooljudge,thequeryencoderandthetool
coderE takesthehiddenstateofatokenasinput.
Q
encoder.
Inordertokeepasmuchinformationaspossiblein
theoriginalhiddenstates,weuseresidualconnec-
where WJ ,WJ ∈ Rd×D, WJ ∈ RD×1 tion which is really important for the final result.
gate up down
are parameters to be optimized. (D is the hyper- E ′ can thus be seen as an offset optimization of
Q
parameterfortheintermediatesize). σ represents theoriginalhiddenstatesusedforretrieval:
theactivationfunctionand⊗representsmultipli-
cationofcorrespondingpositions. E Q ′(h) = W d Q own ((σW g Q ate (h))⊗W u Q p (h))
(6)
Theinitialinputtokenlististokenizedfromthe E (h) = norm(W ⊗(h+E ′(h)))
Q dim Q
querywithICLandCoTprompt. CoToolsjudges
whethertocallatoolwheneveranewanswertoken whereWQ ,WQ ∈ Rd×D, WQ ∈ RD×d and
gate up down
istobegenerated. Supposethecurrenttokenlistis W ∈ Rd areparameterstobeoptimized. ⊗rep-
dim
[x ,x ,...,x ]. We calculate the hidden state h
1 2 t t resentsmultiplicationofcorrespondingpositions.
ofthelasttokenx withEquation1. Itisusedto
t normrepresentstensornormalization.
calculatetheScore :
J WhenCoToolsdecidestocallatoolinthepro-
cessofreasoning,ittokenizesthequeryandanswer
Score = J(h ) ∈ [0,1] (4)
J t
fragmentinretrievalpromptendingwiththespe-
IfScore islargerthanthresholdθ(typicallysetto cialENDtokenx (e.g. "</s>"inLLaMA2)to
J end

get[x ,x ,...,x ,x ]. ThemodelMthencal- weusethenumericalreasoningdatasetsGSM8K-
1 2 Lq end
culatesthehiddenstatesofx whichisusedfor XLandFuncQAwhicharecreatedinToolkenGPT
end
calculatingthequeryvectorV : (Hao et al., 2024). For the later, we select the
Q
Knowledge-Based Question Answering (KBQA)
V Q = E Q (M(x end ;x 1 ,...,x Lq )) (7) datasetsKAMEL(KaloandFichtel,2022)andSim-
pleQuestionsv2(Westonetal.,2015). Tomakethe
SupposetheexternaltoolpoolisT. Foranytool
SimpleQuestionsv2bettersuitedforevaluation,we
T ∈ T,wecomputethetoolvectorV inasimilar
T rewriteitusingChatGPTthengetthenewdataset
wayaswecomputethequeryvectorV :
Q SimpleToolQuestions(STQuestions). Numberof
toolsinthesedatasetsisshowninTable2.
E ′(h) = WT ((σWT (h))⊗WT (h))
T down gate up
E (h) = norm(W ⊗(h+E ′(h))) (8) Dataset ToolAmount
T dim T
V T = E T (M(x end ;x 1 ,...,x Lt )) GSM8K-XL 4
FuncQA 13
where WT ,WT ∈ Rd×D, WT ∈ RD×d are KAMEL 234
gate up down
SimpleToolQuestions 1,836
parameterstobeoptimized. E andE sharethe
Q T
sameparameterW sinceW isusedtoiden-
dim dim Table2: Numberoftoolsforseveraldatasets. Dataset
tify which dimensions of the hidden state play a
SimpleToolQuestionshas999seentoolsand837unseen
roleintheprocessoftoolretrieval.
tools(onlyinthetestset).
We dot multiply the query vecotor V and the
Q
toolvectorV tocalculatethesimilarityscorefor
T ExperimentsonthesebenchmarksshowthatCo-
the corresponding tool T. The tool T∗ with the
Q Toolsoutperformsbaselineacrosstheboard. Our
highestscoreiswhatweneededhere.
method allows for more accurate tool selection
even when the tool scale is very large. Also it
Score = V ·V (9)
Q,T Q T
demonstrates generalization performance on un-
T∗ = argmaxScore (10) seen tools. Besides, we find key dimensions of
Q Q,T
T using hidden states for vector retrieval that help
The Tool Retriever is trained with the con- enhancetheinterpretabilityofthemodel.
strastivelearningmethodinbatchasotherretriev-
4.1 ExperimentSetting
ers do (Karpukhin et al., 2020). The tool search
during training is limited to the tools involved in 4.1.1 NumericalReasoning
the single data batch, rather than the entire tool
To evaluate tool learning paradigms on the nu-
poolduringevaluation. Theobjectivefunctionis
merical reasoning task, we use the two datasets
thecrossentropyloss:
created by ToolkenGPT (Hao et al., 2024): (1)
GSM8K-XL: It’s an enhanced version of the ex-
L = L (Score ,Label) (11)
Retriever CE Q,T Batch isting GSM8K (Cobbe et al., 2021) dataset with
4 basic arithmetic operations (+−×÷) as tools.
3.3 ToolCalling: UseRetrievedTools
(2) FuncQA: It’s an synthetic dataset with 13
Afterfindingtheneededtool,thefoundationmodel
arithemetic tools, with both one-hop and multi-
generatestheparametersofitwithICLprompting.
hopsquestions.
The tool calling format should be emphasized in
Becausethesamearithmeticproblemcanoften
thepromptsothatwecanextractparametersvalue
besolvedinmanydifferentprocedures,wefocus
properly with regex expression from the model
onthecorrectnessofthefinalresultratherthanon
output. Thenthetoolisexecutedandtheresultis
thespecifictoolcallingprocessintheevaluation.
addedinanswer.
The evaluation metric is just like in ToolkenGPT.
WeusetheRoundAccuracymetricforGSM8K-
4 Experiment
XLandFuncQAOne-Hoptestsets. Thefloatnum-
In this section, we apply CoTools to two distinct bers are rounded to two decimals. The Approx
ToolLearningapplicationscenariosinEnglish: cal- Accuracy metric is used for the FuncQA Multi-
culatingarithmeticquestionsandfindingrelevant Hoptestset. Itallowsforerrorsof0.1%accuracy
knowledgeintheKnowledgeBase. Fortheformer, inmulti-stepcalculations.

| 4.1.2 Knowledge-BasedQuestionAnswering |     |     |     |     |     |     |     |     |        |          |     | FuncQA  |            |
| -------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------- | --- | ------- | ---------- |
|                                        |     |     |     |     |     |     |     |     | Method | GSM8K-XL |     |         |            |
|                                        |     |     |     |     |     |     |     |     |        |          |     | One-Hop | Multi-Hops |
Forevaluatingwhethertoollearningparadigmscan
|        |        |          |       |     |          |       | 0-shotChatGPT        |     |     |     | 0.17 | 0.55 | 0.09 |
| ------ | ------ | -------- | ----- | --- | -------- | ----- | -------------------- | --- | --- | --- | ---- | ---- | ---- |
| choose | proper | relevant | tools | on  | the KBQA | task, |                      |     |     |     |      |      |      |
|        |        |          |       |     |          |       | 0-shotPromptingLLaMA |     |     |     | 0.04 | 0.05 | 0.00 |
weuseanexistingdatasetKAMELandconstruct CoTPromptingLLaMA 0.00 0.00 0.00
|               |                     |     |     |     |      |        | ToolkenGPTLLaMA    |     |     |     | 0.18 | 0.48 | 0.06 |
| ------------- | ------------------- | --- | --- | --- | ---- | ------ | ------------------ | --- | --- | --- | ---- | ---- | ---- |
| a new dataset | SimpleToolQuestions |     |     |     | with | a much |                    |     |     |     |      |      |      |
|               |                     |     |     |     |      |        | CoTools(ours)LLaMA |     |     |     | 0.19 | 0.53 | 0.07 |
largeramountoftools.
|     |     |     |     |     |     |     | 0-shotPromptingMistral |     |     |     | 0.14 | 0.17 | 0.04 |
| --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | ---- | ---- | ---- |
(1) KAMEL (Kalo and Fichtel, 2022): It’s an CoTPromptingMistral 0.10 0.20 0.06
|     |     |     |     |     |     |     | CoTools(ours)Mistral |     |     |     | 0.42 | 0.63 | 0.07 |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | ---- | ---- | ---- |
QAdatasetbuiltwiththeknowledgeinKBWiki-
data. Ithas234relationswhichareviewedastools.
|     |     |     |     |     |     |     | Table3: |     | MainresultsonNumericalReasoningBench- |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | ------------------------------------- | --- | --- | --- | --- |
We use the post-processing version of the paper marks. RoundAccmetric(roundfloatnumberstotwo
|            |      |     |            |      |        |        | decimals)forGSM8K-XLandFuncQAOne-Hop. |     |     |     |     |     | Ap- |
| ---------- | ---- | --- | ---------- | ---- | ------ | ------ | ------------------------------------- | --- | --- | --- | --- | --- | --- |
| ToolkenGPT | (Hao | et  | al., 2024) | with | a gold | train- |                                       |     |     |     |     |     |     |
proxAccmetric(allow0.1%error)forFuncQAMulti-
| ing set KAMEL(sup) |     |     | and a | synthetic | training | set |       |       |     |           |                 |     |         |
| ------------------ | --- | --- | ----- | --------- | -------- | --- | ----- | ----- | --- | --------- | --------------- | --- | ------- |
|                    |     |     |       |           |          |     | Hops. | LLaMA |     | refers to | LLaMA2-7B-Chat. |     | Mistral |
KAMEL(syn)generatedbyChatGPT.
|                                      |     |     |     |     |     |     | referstoMistral-7B-Instruct-v0.2. |     |     |     |     | Everyresultisfrom |     |
| ------------------------------------ | --- | --- | --- | --- | --- | --- | --------------------------------- | --- | --- | --- | --- | ----------------- | --- |
| (2)SimpleToolQuestions(STQuestions): |     |     |     |     |     | we  |                                   |     |     |     |     |                   |     |
asinglerun.
| construct   | it based | on  | the KBQA |        | dataset | Simple- |     |     |     |     |     |     |     |
| ----------- | -------- | --- | -------- | ------ | ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
| Questionsv2 | (Weston  |     | et al.,  | 2015). | One     | case in |     |     |     |     |     |     |     |
theGSM8K-XLdataset,CoToolsandToolkenGPT
| the raw | dataset | contains | a   | question | and | a triplet |     |     |     |     |     |     |     |
| ------- | ------- | -------- | --- | -------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
basedonLLaMA2-7BarecomparablewithChat-
| (headentity,relationship,tailentity). |     |      |          |        | Therawdata |           |     |     |         |        |        |          |         |
| ------------------------------------- | --- | ---- | -------- | ------ | ---------- | --------- | --- | --- | ------- | ------ | ------ | -------- | ------- |
|                                       |     |      |          |        |            |           | GPT | in  | effect. | On the | FuncQA | dataset, | CoTools |
| needs models                          | to  | find | the head | entity | in         | the ques- |     |     |         |        |        |          |         |
tion. Thentheknowledgesubgraphaboutthehead is a little bit better than ToolkenGPT in one-hop
questionswiththefoundationmodelLLaMA2-7B
| entityisfoundedintheKBFreebase. |     |     |     |                    | Relationship |     |       |       |      |     |            |            |     |
| ------------------------------- | --- | --- | --- | ------------------ | ------------ | --- | ----- | ----- | ---- | --- | ---------- | ---------- | --- |
|                                 |     |     |     |                    |              |     | while | makes | even | in  | multi-hops | questions. | The |
| issearchedinasmallscope.        |     |     |     | Butifweaddallrela- |              |     |       |       |      |     |            |            |     |
performanceofCoToolsisverydependentonthe
| tionsintothetoolpool,              |     |     | it’snotpropertoretrieve |     |     |          |            |     |         |     |          |             |     |
| ---------------------------------- | --- | --- | ----------------------- | --- | --- | -------- | ---------- | --- | ------- | --- | -------- | ----------- | --- |
|                                    |     |     |                         |     |     |          | foundation |     | model’s | own | ability. | It enhances | the |
| toolsinthewholewithshortquestions. |     |     |                         |     |     | Thereare |            |     |         |     |          |             |     |
performanceoffoundationmodelsacrossallabil-
| manysimilartoolsthusitisimpossibletojudge. |     |     |     |     |     | In  |     |        |          |     |          |          |        |
| ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | ------ | -------- | --- | -------- | -------- | ------ |
|                                            |     |     |     |     |     |     | ity | levels | compared | to  | baseline | methods, | making |
ordertomakethisdatasetmoreapplicablefortool
learning evaluation, we rewrite the original ques- thestrongevenstronger.
tionusingChatGPT.Thenewquestionsprovidea
|               |             |     |     |     |        |           |     |           |     |     | KAMEL | STQuestions |        |
| ------------- | ----------- | --- | --- | --- | ------ | --------- | --- | --------- | --- | --- | ----- | ----------- | ------ |
| more detailed | description |     | of  | the | needed | relation- |     | Method(%) |     |     |       |             |        |
|               |             |     |     |     |        |           |     |           |     |     | SUP   | SYN Seen    | Unseen |
ship. Thedatasethas1836toolswithdescription
|                           |     |     |     |                 |     |     |     | ToolkenGPTLLaMA    |     |     | 93.4 | 20.6 23.8 | 0.0  |
| ------------------------- | --- | --- | --- | --------------- | --- | --- | --- | ------------------ | --- | --- | ---- | --------- | ---- |
| frommanydifferentdomains. |     |     |     | 999ofthemappear |     |     |     |                    |     |     |      |           |      |
|                           |     |     |     |                 |     |     |     | CoTools(Ours)LLaMA |     |     | 93.8 | 43.6 35.1 | 10.4 |
inthetrainingsetand837unseentoolsareonlyin
thetestset. Wealsogeneratestooldescriptionfor Table4: MainresultsonKBQABenchmarks. Theeval
eachtoolliketheformatofKAMEL.Itcanbeused metricistheaccuracyoftoolselection. Becauseofthe
toassesstheaccuracyofselectionagainstseenand largenumberoftools,wedonotevaluatethePrompting
methodwhichisinefficientandhardtoguaranteeresults.
| unseen tools | in  | the large | tool | scale | scenario, | and |     |     |     |     |     |     |     |
| ------------ | --- | --------- | ---- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
LLaMAreferstoLLaMA2-7B-Chat.
whetherthemodelfavorstoolsofcertaindomains.
ForKBQAbenchmarks,wearemoreconcerned
|           |          |     |       |            |               |         |       | For KBQA |           | benchmarks, |     | the tool selection | re-         |
| --------- | -------- | --- | ----- | ---------- | ------------- | ------- | ----- | -------- | --------- | ----------- | --- | ------------------ | ----------- |
| about the | accuracy | of  | tool  | selection. | We            | want to |       |          |           |             |     |                    |             |
|           |          |     |       |            |               |         | sults | of       | different | methods     |     | are listed         | in Table 4. |
| evaluate  | whether  | the | model | is able    | to understand |         |       |          |           |             |     |                    |             |
Forcaseswithlargeamountsofgoldtrainingdata
thesemanticinformationofthequestionsandselect
suchasKAMEL(sup),bothmethodsperformwell.
therelevanttools,espciallywhenthetoolpoolis
WithsynthetictrainingsetsKAMEL(syn)created
prettylargeorthetoolsareunseen.
|     |     |     |     |     |     |     | by  | ChatGPT, |        | CoTools  | does  | much better | though  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------ | -------- | ----- | ----------- | ------- |
|     |     |     |     |     |     |     | it  | is still | a long | way from | being | usable.     | CoTools |
4.2 MainResult
doesbetterinlow-qualitytrainingdatascenarios,
Here is the main evaluation section of the paper. perhaps because of the contrastive learning train-
We compare our method CoTools with baselines ing approach. Similarly CoTools performs better
like0-shotChatGPTandToolkenGPT. in massive tool (999 seen tools in the STQues-
For the numerical reasoning task, the perfor- tions dataset) scenarios. For 837 unseen tools in
mances of different methods on the GSM8K-XL theSTQuestionsdataset,CoToolscanusethede-
and FuncQA datasets are shown in Table 3. On taileddescriptionoftoolsforbetterretrievalwhile

ToolkenGPT only can use tools that have been ToolkenGPT by more than 20%. Since the foun-
trained. Moredetailsaboutunseentoolsarefurther dationmodelisfrozenandthetrainingdataislim-
investigatedinSection4.3.3. ited,contrastivelearningmethodsusedinCoTools
|              |     |     | mightbeparticularlyeffective.                |     |     | Itcanbetterteach |     |
| ------------ | --- | --- | -------------------------------------------- | --- | --- | ---------------- | --- |
| 4.3 Analysis |     |     | theagenttodistinguishbetweentools,eventhough |     |     |                  |     |
thedataqualityispoor.
4.3.1 DataSynthesis
Thequalityofdatasetusedforfine-tuningisvery 4.3.2 Thenumberoftools
important(Zhouetal.,2024),sowewanttoinves-
Inthispart,wetrytoexploretheupperlimitofthe
tigatetheeffectofdatasetgeneratedbyhumanand
amountofloadingtoolssupportedbyeachmethod.
theLLM.WeusetwoversionsofKAMELtraining
|     |     |     | The benchmark | STQuestions |     | contains 999 | tools |
| --- | --- | --- | ------------- | ----------- | --- | ------------ | ----- |
(1)KAMEL(sup)
setforcomparativevalidation. which appear in the training set. The evaluation
| issampledfromrawKAMELtrainingset. |     | Itsim- |     |     |     |     |     |
| --------------------------------- | --- | ------ | --- | --- | --- | --- | --- |
resultsonitareshowninFigure6below.
| ulates the real-world | scenario with | sufficient in- |     |     |     |     |     |
| --------------------- | ------------- | -------------- | --- | --- | --- | --- | --- |
domaintrainingdata. (2)KAMEL(syn)issynthe- ToolkenGPT CoTools CoTools top5
| sizedbyChatGPT.Forthesituationwheremassive |     |     | 90  |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
80
70
newtoolsareaddedtothetoolpool,itiscostlyfor
60
50
| humanannotatorstoannotatesufficientdata. |     | Itis |     |     |     |     |     |
| ---------------------------------------- | --- | ---- | --- | --- | --- | --- | --- |
40
| commontodaytouseLLMstoassistingenerating |     |     | 30  |     |     |     |     |
| ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
20
| dataformodeltuning. |                      |     | 10                                             |     |     |     |     |
| ------------------- | -------------------- | --- | ---------------------------------------------- | --- | --- | --- | --- |
|                     |                      |     | 200                                            | 400 | 600 | 800 | 999 |
|                     |                      |     | Figure6: Toolselectionresultwithmassivetools.  |     |     |     | The |
| ToolkenGPT          | CoTools CoTools top5 |     |                                                |     |     |     |     |
| 100                 |                      |     | X-axisrepresentsthenumberoftoolsinthetoolpool. |     |     |     |     |
99
| 98  |     |     | TheY-axisrepresentsthetoolselectionaccuracy. |     |     |     |     |
| --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- |
97
96
95
94
| 93  |     |     | Asthenumberoftoolsreachesathousandscale, |     |     |     |     |
| --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- |
92
| 91  |     |     | CoToolsstilloutperformsthebaselinebymorethan |     |     |     |     |
| --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- |
90
| 30  | 60 100 | 234 |     |     |     |     |     |
| --- | ------ | --- | --- | --- | --- | --- | --- |
10%. Withthenumberoftoolsincreases,theprob-
Figure4: Performancesofthemethodswithfoundation ability of similar tools appearing is much higher.
| modelfine-tunedbyKAMEL(sup). |     | TheX-axisrepre- |     |     |     |     |     |
| ---------------------------- | --- | --------------- | --- | --- | --- | --- | --- |
Benefitfromthestronglanguageunderstandngca-
sentsthenumberoftoolsinthetoolpool. TheY-axis pabiltyofLLMs,thetoollearningmethodCoTools
representsthetoolselectionaccuracy.
whichbetterusestheLLM’sownabilitydoesbetter
inthissituation.
| With KAMEL(sup), | both methods | perform |     |     |     |     |     |
| ---------------- | ------------ | ------- | --- | --- | --- | --- | --- |
prettywellinFigure4. Thisdemonstratesthatthe 4.3.3 UnseenTools
toolselectionsubtaskcanalreadybewellsolvedby
Itismeaningfultoevaluatethegeneralizabilityof
existingmethodswhenhighqualitytrainingdata the fine-tuned model especially in tool learning.
aresufficient. CoToolsremainsnearly100%cor- It’sinconvenienttoadaptthemodelweightwhen-
rectwiththeTOP5toolsselectedsoitwouldland
|     |     |     | ever somenew | toolsare | added. | As mentioned | in  |
| --- | --- | --- | ------------ | -------- | ------ | ------------ | --- |
wellinreal-worldscenarios.
Section4.1.2,total837toolsinthedatasetSTQues-
|            |                      |     | tionsdonotappearinthetrainingset.            |     |     | Weusethese |     |
| ---------- | -------------------- | --- | -------------------------------------------- | --- | --- | ---------- | --- |
| ToolkenGPT | CoTools CoTools top5 |     |                                              |     |     |            |     |
| 100        |                      |     | unseentoolsasout-of-domaindistributionstoex- |     |     |            |     |
90
| 80  |     |     | aminethegeneralizationabilityofthemodel. |     |     |     |     |
| --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- |
70
| 60  |     |     | Themainresultsonunseentoolshavebeenlisted |     |     |     |     |
| --- | --- | --- | ----------------------------------------- | --- | --- | --- | --- |
50
| 40  |     |     | inTable4. CoToolshasatop1accuracyof10.41% |     |     |     |     |
| --- | --- | --- | ----------------------------------------- | --- | --- | --- | --- |
30
20
|       |        |     | andatop5accuracyof33.68%. |     |                      | ToolkenGPThasa |     |
| ----- | ------ | --- | ------------------------- | --- | -------------------- | -------------- | --- |
| 10 30 | 60 100 | 234 |                           |     |                      |                |     |
|       |        |     | top1accuracyof0.0%.       |     | Wecountthewrongcases |                |     |
Figure5: Performancesofthemethodswithfoundation intheresultsasinFigure7. It’seasytoseefrom
model fine-tuned by KAMEL(syn). The rest of the thefigurethatToolkenGPThasaclearpreference
settingsarethesameasinFigure4.
forasmallgroupoftoolshoweverCoToolsdoes
not. Inotherwords,CoToolsfocusesmoreonhow
For the synthetic training set KAMEL(syn), to distinguish and identify tools during training
Figure 5 shows that CoTools is stronger than insteadofrememberingthem.

|     |     |            |     |         |     |     |     |     | lr=0.001 | lr=0.01 | lr=0.1 |     |     |
| --- | --- | ---------- | --- | ------- | --- | --- | --- | --- | -------- | ------- | ------ | --- | --- |
|     |     | ToolkenGPT |     | CoTools |     |     |     |     |          |         |        |     |     |
4
| 40  |     |     |     |     |     |     | 3.5 |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2.5 3
| 30  |     |     |     |     |     |     | 2   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1.5
| 20  |     |     |     |     |     |     | 1   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0.5
| 10  |     |     |     |     |     |     | 0   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
-0.5
| 0   |     |     |     |     |     |     | -1  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
-1.5
-2.5 -2
Figure7: Erroranalysisforinstanceswithunseentools. 12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061626364
| We count                                       | the | number | of instances |     | where | the unseen |          |             |     |                       |     |     |     |
| ---------------------------------------------- | --- | ------ | ------------ | --- | ----- | ---------- | -------- | ----------- | --- | --------------------- | --- | --- | --- |
|                                                |     |        |              |     |       |            | Figure9: | NormalizedW |     | weightsegment(onlythe |     |     |     |
| toolshouldhavebeencalledbuttheseentooliscalled |     |        |              |     |       |            |          |             |     | dim                   |     |     |     |
first64dimensions)byequation12.
| instead. | TheX-axisrepresentsthe999seentools. |     |     |     |     | The |     |     |     |     |     |     |     |
| -------- | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Y-axisrepresentsthenumberoftimestheseentoolis
|                    |     |                                 |     |     |     |     | Taking       | this | a step | further, | we observe | the        | data |
| ------------------ | --- | ------------------------------- | --- | --- | --- | --- | ------------ | ---- | ------ | -------- | ---------- | ---------- | ---- |
| incorrectlycalled. |     | (Itisrecommendedtoviewthecolor- |     |     |     |     |              |      |        |          |            |            |      |
|                    |     |                                 |     |     |     |     | distribution | of   | raw W  | weights. |            | The values | of   |
dim
printedversion.)
|     |     |     |     |     |     |     | 4096 dimensions  |     | after                       | the descending |     | order | are |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --------------------------- | -------------- | --- | ----- | --- |
|     |     |     |     |     |     |     | showninFigure10. |     | Asthelearningrateincreases, |                |     |       |     |
4.3.4 KeyDimensioninHiddenStates the key dimensions become more and more cen-
In this section, we would like to explore which tralized. At a learning rate of 0.01, 1561 of the
dimensionsofhiddenstatesplayakeyrolewhen 4096dimensionsareweightedmorethantheinitial
| retrieving | tools. | During |     | experiments |     | we find a |     |     |     |     |     |     |     |
| ---------- | ------ | ------ | --- | ----------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
1. Weuseonlythesedimensionsfortoolretrieval.
robust model probing (Alain and Bengio, 2016) The TOP1 accuracy has decreased by only 1.4%
methodForLLMoutputs. Itmayhelptoenhance fromtheoriginal93.8%,whiletheTOP5accuracy
modelinterpretability. remainsunchanged. Thisprovidessomeevidence
AsmentionedinSection3.2,theQueryEncoder thatthedimensionsofthehiddenstateofLLMare
E andtheToolEncoderE sharethesameW dividedinrepresentingsemanticinformation.
| Q   |     |     |     | T   |     | dim |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Rd,
| weight | (W dim | ∈   | with | all-ones | initialization). |     |     |     |     |     |     |     |     |
| ------ | ------ | --- | ---- | -------- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Weindividuallysetitslearningrateto0.001,0.01 lr=0.001 lr=0.01 lr=0.1
5
| and0.1fortrainingrespectively,andotherhyperpa- |     |     |     |         |     |         | 4   |     |     |     |     |     |     |
| ---------------------------------------------- | --- | --- | --- | ------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
| rametersarekeptconstant.                       |     |     |     | TherawW |     | weights | 3   |     |     |     |     |     |     |
dim
| aftertrainingarepartiallydisplayedinFigure8. |     |     |     |     |     |     | 2   |     |     |     |     |     |     |
| -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1
|     |     | lr=0.001 | lr=0.01 | lr=0.1 |     |     | 0   |     |     |     |     |     |     |
| --- | --- | -------- | ------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
4.5
4
| 3.5 |     |     |     |     |     |     | Figure10: | SortedrawW |     | weight. |     | It’strainedwith |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | --- | ------- | --- | --------------- | --- |
| 3   |     |     |     |     |     |     |           |            |     | dim     |     |                 |     |
thedatasetKAMEL.
2.5
2
1.5
1
5 Conclusion
0.5
0
12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061626364
Inthispaper,wepresentanovelCoTtoollearning
| Figure8: | RawW |     | weightsegment(onlythefirst64 |     |     |     |                                        |     |     |     |     |     |     |
| -------- | ---- | --- | ---------------------------- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --- | --- | --- |
|          |      | dim |                              |     |     |     | methodCoToolswhichisbasedonfrozenLLMs. |     |     |     |     |     |     |
dimensions). Theweightsareinitializedwithallones. CoToolsincorporatestoolinvocationintothepro-
cessofgeneratinganswerstothemodelwhilemain-
It’sobviousinFigure8thatparameterschange
tainingtheoriginalgeneralizedabilityofthefoun-
| more drastically |     | with | larger | learning | rates. | At a |              |     |                                |     |     |     |     |
| ---------------- | --- | ---- | ------ | -------- | ------ | ---- | ------------ | --- | ------------------------------ | --- | --- | --- | --- |
|                  |     |      |        |          |        |      | dationmodel. |     | Itleveragesthepowerfulsemantic |     |     |     |     |
learningratesettingof0.1,manyoftheparameters
representationcapabilityofthefoundationmodel
| changefromtheinitial1to0. |     |     |     | Inadditionasimilar |     |     |              |         |     |         |        |          |      |
| ------------------------- | --- | --- | --- | ------------------ | --- | --- | ------------ | ------- | --- | ------- | ------ | -------- | ---- |
|                           |     |     |     |                    |     |     | to determine | whether |     | to call | a tool | and what | tool |
trendcanbevaguelyobservedforthethreefolds.
tocall. ExperimentsonBenchmarksofnumerical
Inordertobetteranalyzethecommonalityofthe
reasoningandKBQAtasksshowthatourmethod
parametersatdifferentlearningrates,wenormalize
|                      |     |     |     |                      |     |     | performs | well | in different | scenarios. |     | In particu- |     |
| -------------------- | --- | --- | --- | -------------------- | --- | --- | -------- | ---- | ------------ | ---------- | --- | ----------- | --- |
| themusingEquation12. |     |     |     | Thesimilartrendofthe |     |     |          |      |              |            |     |             |     |
lar,itstoolselectioncapabilityismuchimproved
| three folds     | can | be clearly |     | found  | in Figure | 9. We |                        |     |     |                      |     |     |     |
| --------------- | --- | ---------- | --- | ------ | --------- | ----- | ---------------------- | --- | --- | -------------------- | --- | --- | --- |
|                 |     |            |     |        |           |       | comparedtothebaseline. |     |     | Inaddition,weroughly |     |     |     |
| view dimensions |     | with       | the | common | upper     | value |                        |     |     |                      |     |     |     |
exploretherolethatdifferenthiddenstatesdimen-
| of 3 W | weights |     | as the | key dimensions. |     | The |                                              |     |     |     |     |     |     |
| ------ | ------- | --- | ------ | --------------- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- | --- |
|        | dim     |     |        |                 |     |     | sionsofmodeloutputplayinthetoolselectionpro- |     |     |     |     |     |     |
subscalescorrespondingtothekeydimensionsplay
cess,whichhelpstoenhancemodelinterpretabil-
animportantroleintoolselection.
ity. WebelievethatouridealToolLearningagent
|     |     |     | W   | −W  |     |      | frameworkbasedonfrozenLLMswithitspracti- |     |        |         |     |           |     |
| --- | --- | --- | --- | --- | --- | ---- | ---------------------------------------- | --- | ------ | ------- | --- | --------- | --- |
|     | Wˆ  |     | dim |     | dim |      |                                          |     |        |         |     |           |     |
|     |     | =   |     |     |     | (12) |                                          |     |        |         |     |           |     |
|     |     | dim |     | σ   |     |      | cal realization                          |     | method | CoTools | can | be useful | in  |
W
dim

real-worldapplicationsandevendrivefurtherde- chat-basedlargelanguagemodels. InFindingsofthe
velopmentofToolLearning. AssociationforComputationalLinguistics: EMNLP
2023,pages14777–14790,Singapore.Association
Limitations forComputationalLinguistics.
ResearchonLLMToolLearningisstillonitsearly Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian,
MarkChen,HeewooJun,LukaszKaiser,Matthias
stage. Although the open source community al-
Plappert, Jerry Tworek, Jacob Hilton, Reiichiro
ready has a number of Tool Learning datasets, a
Nakano,etal.2021. Trainingverifierstosolvemath
largeproportionofthemaretoosimpleoroflow wordproblems. arXivpreprintarXiv:2110.14168.
quality. Asawhole,ourresearchisthuslimited.
Onelimitationisthatwedonotconductexperi- NicholasFarnandRichardShin.2023. Tooltalk: Eval-
uatingtool-usageinaconversationalsetting. arXiv
mentsfortoolscontainingmultiplereturnvalues.
preprintarXiv:2311.10775.
Inthissituation,weneedtoselectthereturnvalue
that should be added to the answer. Our solution ShiboHao,TianyangLiu,ZhenWang,andZhitingHu.
istotrainasimilarReturnValueEncoderE like 2024. Toolkengpt: Augmenting frozen language
R
modelswithmassivetoolsviatoolembeddings. Ad-
E inSection3.2. Unfortunatelyitcannotnotbe
Q vancesinneuralinformationprocessingsystems,36.
evaluatedatthemomentbecauseofthelackofrel-
evantCoTToolLearningdatasetswiththiskindof Cheng-YuHsieh,Si-AnChen,Chun-LiangLi,Yasuhisa
tools. Fortheselectionofreturnvaluesforthistype Fujii, Alexander Ratner, Chen-Yu Lee, Ranjay Kr-
ishna, and Tomas Pfister. 2023. Tool documenta-
oftools,atemporaryalternativetotheprompting
tionenableszero-shottool-usagewithlargelanguage
schemeiscurrentlyavailable.
models. arXivpreprintarXiv:2308.00675.
Another possible limitation is that we do not
attemptthecompleteToolLearningprocessona QiaoJin,YifanYang,QingyuChen,andZhiyongLu.
2024. Genegpt: Augmentinglargelanguagemodels
large-scale real-world toolset. A Tool Learning
withdomaintoolsforimprovedaccesstobiomedical
datasetwithlarge-scalerealizabletoolsstilldoes
information. Bioinformatics,40(2):btae075.
notexist. ThedatasetToolBench(Qinetal.,2023b)
comes closest to this goal. However the format Jan-ChristophKaloandLeandraFichtel.2022. Kamel:
of its gold data is too cumbersome and not well Knowledgeanalysiswithmultitokenentitiesinlan-
guagemodels. InProceedingsoftheConferenceon
filtered.
AutomatedKnowledgeBaseConstruction.
VladimirKarpukhin,BarlasOguz,SewonMin,Patrick
References
Lewis,LedellWu,SergeyEdunov,DanqiChen,and
Wen-tauYih.2020. Densepassageretrievalforopen-
JoshAchiam,StevenAdler,SandhiniAgarwal,Lama
domainquestionanswering. InProceedingsofthe
Ahmad, Ilge Akkaya, Florencia Leoni Aleman,
2020ConferenceonEmpiricalMethodsinNatural
DiogoAlmeida,JankoAltenschmidt,SamAltman,
LanguageProcessing(EMNLP),pages6769–6781,
ShyamalAnadkat,etal.2023. Gpt-4technicalreport.
Online.AssociationforComputationalLinguistics.
arXivpreprintarXiv:2303.08774.
Guillaume Alain and Yoshua Bengio. 2016. Under- TakeshiKojima,ShixiangShaneGu,MachelReid,Yu-
standing intermediate layers using linear classifier takaMatsuo,andYusukeIwasawa.2022. Largelan-
probes. arXivpreprintarXiv:1610.01644. guagemodelsarezero-shotreasoners. Advancesin
neural information processing systems, 35:22199–
KinjalBasu,IbrahimAbdelaziz,SubhajitChaudhury,
22213.
SohamDan,MaxwellCrouse,AsimMunawar,Sad-
hana Kumaravel, Vinod Muthusamy, Pavan Kapa-
Minghao Li, Yingxiu Zhao, Bowen Yu, Feifan Song,
nipathi, and Luis A Lastras. 2024. Api-blend: A
Hangyu Li, Haiyang Yu, Zhoujun Li, Fei Huang,
comprehensivecorporafortrainingandbenchmark-
andYongbinLi.2023. API-bank: Acomprehensive
ingapillms. arXivpreprintarXiv:2402.15491.
benchmarkfortool-augmentedLLMs. InProceed-
ingsofthe2023ConferenceonEmpiricalMethods
Tom Brown, Benjamin Mann, Nick Ryder, Melanie
inNaturalLanguageProcessing,pages3102–3116,
Subbiah,JaredDKaplan,PrafullaDhariwal,Arvind
Singapore.AssociationforComputationalLinguis-
Neelakantan,PranavShyam,GirishSastry,Amanda
tics.
Askell,etal.2020. Languagemodelsarefew-shot
learners. Advancesinneuralinformationprocessing
Yaobo Liang, Chenfei Wu, Ting Song, Wenshan Wu,
systems,33:1877–1901.
Yan Xia, Yu Liu, Yang Ou, Shuai Lu, Lei Ji,
Zhipeng Chen, Kun Zhou, Beichen Zhang, Zheng ShaoguangMao,etal.2023. Taskmatrix.ai: Com-
Gong, Xin Zhao, and Ji-Rong Wen. 2023. Chat- pletingtasksbyconnectingfoundationmodelswith
CoT:Tool-augmentedchain-of-thoughtreasoningon millionsofapis. arXivpreprintarXiv:2303.16434.

XiaoLiu,HaoYu,HanchenZhang,YifanXu,Xuanyu ZhihengXi,WenxiangChen,XinGuo,WeiHe,Yiwen
Lei, Hanyu Lai, Yu Gu, Hangliang Ding, Kaiwen Ding, Boyang Hong, Ming Zhang, Junzhe Wang,
Men,KejuanYang,etal.2023. Agentbench:Evaluat- Senjie Jin, Enyu Zhou, et al. 2023. The rise and
ingllmsasagents. arXivpreprintarXiv:2308.03688. potential of large language model based agents: A
|           |        |         |        |           |     | survey. | arXivpreprintarXiv:2309.07864. |     |     |     |     |
| --------- | ------ | ------- | ------ | --------- | --- | ------- | ------------------------------ | --- | --- | --- | --- |
| Shishir G | Patil, | Tianjun | Zhang, | Xin Wang, | and |         |                                |     |     |     |     |
JosephEGonzalez.2023. Gorilla: Largelanguage Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran,
modelconnectedwithmassiveapis. arXivpreprint TomGriffiths,YuanCao,andKarthikNarasimhan.
arXiv:2305.15334. 2024. Treeofthoughts: Deliberateproblemsolving
|     |     |     |     |     |     | with large | language | models. | Advances |     | in Neural |
| --- | --- | --- | --- | --- | --- | ---------- | -------- | ------- | -------- | --- | --------- |
InformationProcessingSystems,36.
| Bo Qiao, Liqun | Li,    | Xu Zhang, | Shilin | He,  | Yu Kang,  |     |     |     |     |     |     |
| -------------- | ------ | --------- | ------ | ---- | --------- | --- | --- | --- | --- | --- | --- |
| Chaoyun        | Zhang, | Fangkai   | Yang,  | Hang | Dong, Jue |     |     |     |     |     |     |
Zhang, Lu Wang, et al. 2023. Taskweaver: Wayne Xin Zhao, Kun Zhou, Junyi Li, Tianyi Tang,
A code-first agent framework. arXiv preprint XiaoleiWang,YupengHou,YingqianMin,Beichen
arXiv:2311.17541. Zhang, Junjie Zhang, Zican Dong, et al. 2023. A
|     |     |     |     |     |     | survey | of large | language | models. | arXiv | preprint |
| --- | --- | --- | --- | --- | --- | ------ | -------- | -------- | ------- | ----- | -------- |
arXiv:2303.18223.
| Yujia Qin, | Shengding | Hu, Yankai |       | Lin, Weize | Chen,  |     |     |     |     |     |     |
| ---------- | --------- | ---------- | ----- | ---------- | ------ | --- | --- | --- | --- | --- | --- |
| Ning Ding, | Ganqu     | Cui, Zheni | Zeng, | Yufei      | Huang, |     |     |     |     |     |     |
Chaojun Xiao, Chi Han, et al. 2023a. Tool ChuntingZhou,PengfeiLiu,PuxinXu,SrinivasanIyer,
learning with foundation models. arXiv preprint JiaoSun,YuningMao,XuezheMa,AviaEfrat,Ping
|     |     |     |     |     |     | Yu,LiliYu,etal.2024. |     | Lima: | Lessismoreforalign- |     |     |
| --- | --- | --- | --- | --- | --- | -------------------- | --- | ----- | ------------------- | --- | --- |
arXiv:2304.08354.
ment. AdvancesinNeuralInformationProcessing
Systems,36.
YujiaQin,ShihaoLiang,YiningYe,KunlunZhu,Lan
Yan,YaxiLu,YankaiLin,XinCong,XiangruTang,
BillQian, etal.2023b. Toolllm: Facilitatinglarge A HyperParameter
languagemodelstomaster16000+real-worldapis.
|     |     |     |     |     |     | Hyper parameters |     | for fine-tuning |     | is shown | in Ta- |
| --- | --- | --- | --- | --- | --- | ---------------- | --- | --------------- | --- | -------- | ------ |
arXivpreprintarXiv:2307.16789.
|     |     |     |     |     |     | ble 5. When | fine-tuning | the | Tool | Retriever | with |
| --- | --- | --- | --- | --- | --- | ----------- | ----------- | --- | ---- | --------- | ---- |
TimoSchick,JaneDwivedi-Yu,RobertoDessì,Roberta
GSM8K-XL,weadjustthebatchsizebecauseof
Raileanu,MariaLomeli,EricHambro,LukeZettle-
|     |     |     |     |     |     | theCUDAOutOfMemoryErrorreported. |     |     |     |     | Back |
| --- | --- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- | --- | ---- |
moyer,NicolaCancedda,andThomasScialom.2024.
propagationfrequencyinfine-tuningToolRetriever
| Toolformer: | Languagemodelscanteachthemselves |     |     |     |     |     |     |     |     |     |     |
| ----------- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
to use tools. Advances in Neural Information Pro- withFuncQAisalsoadaptedsinceitonlyhas611
cessingSystems,36.
piecesofdata.
YongliangShen,KaitaoSong,XuTan,DongshengLi,
|                                  |     |     |     |     |          | Module | Epoch | LearningRate | BatchSize | AccumulationStep |     |
| -------------------------------- | --- | --- | --- | --- | -------- | ------ | ----- | ------------ | --------- | ---------------- | --- |
| WeimingLu,andYuetingZhuang.2024. |     |     |     |     | Hugging- |        |       |              |           |                  |     |
|                                  |     |     |     |     |          | Judge  |       | 3 1e-5       |           | 8                | 16  |
gpt: Solving ai tasks with chatgpt and its friends Retriever 10 1e-4 16 12
in hugging face. Advances in Neural Information Retriever(GSM8K-XL) 10 1e-4 12 16
|     |     |     |     |     |     | Retriever(FuncQA) |     | 10 1e-4 |     | 8   | 6   |
| --- | --- | --- | --- | --- | --- | ----------------- | --- | ------- | --- | --- | --- |
ProcessingSystems,36.
|     |     |     |     |     |     | Table 5: Hyper | parameters |     | used | in fine-tuning | with |
| --- | --- | --- | --- | --- | --- | -------------- | ---------- | --- | ---- | -------------- | ---- |
LeiWang,ChenMa,XueyangFeng,ZeyuZhang,Hao foundationmodelsLLaMA2-7B-ChatandMistral-7B-
| Yang, Jingsen | Zhang, | Zhiyuan | Chen, | Jiakai | Tang, |     |     |     |     |     |     |
| ------------- | ------ | ------- | ----- | ------ | ----- | --- | --- | --- | --- | --- | --- |
Instruct-v0.2.
| XuChen,YankaiLin,etal.2024.         |     |     |     | Asurveyonlarge |           |     |     |     |     |     |     |
| ----------------------------------- | --- | --- | --- | -------------- | --------- | --- | --- | --- | --- | --- | --- |
| languagemodelbasedautonomousagents. |     |     |     |                | Frontiers |     |     |     |     |     |     |
ofComputerScience,18(6):1–26. ForlearningrateofW ,wegenerallysetitto
dim
|     |     |     |     |     |     | 0.01. In | fact, W | has | little effect | on  | the fine- |
| --- | --- | --- | --- | --- | --- | -------- | ------- | --- | ------------- | --- | --------- |
dim
Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, tuning effect and can be removed by adjusting
| Barret Zoph, | Sebastian | Borgeaud, |     | Dani | Yogatama, |     |     |     |     |     |     |
| ------------ | --------- | --------- | --- | ---- | --------- | --- | --- | --- | --- | --- | --- |
"tensor_weighting"to"false"inthesettingsofour
MaartenBosma,DennyZhou,DonaldMetzler,etal.
2022a. Emergentabilitiesoflargelanguagemodels. source code. It is mainly used to explore the se-
arXivpreprintarXiv:2206.07682. manticinformationcontainedinhiddenstates.
| JasonWei,XuezhiWang,DaleSchuurmans,Maarten |     |     |     |     |     | B Dataset |     |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- |
Bosma,FeiXia,EdChi,QuocVLe,DennyZhou,
| etal.2022b. | Chain-of-thoughtpromptingelicitsrea- |     |     |     |     |     |     |     |     |     |     |
| ----------- | ------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
B.1 DatasetSplit
| soninginlargelanguagemodels. |     |     | Advancesinneural |     |     |     |     |     |     |     |     |
| ---------------------------- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Thespecificdetailsofthe4datasetsareshownin
informationprocessingsystems,35:24824–24837.
|     |     |     |     |     |     | Table6. Furtheradditionalexplanationofthede- |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- |
JasonWeston,AntoineBordes,SumitChopra,Alexan-
|     |     |     |     |     |     | tailsofthedatasetisprovidedbelow: |     |     |     | Thetestset |     |
| --- | --- | --- | --- | --- | --- | --------------------------------- | --- | --- | --- | ---------- | --- |
derMRush,BartVanMerriënboer,ArmandJoulin,
|                    |          |                             |         |             |     | of dataset                  | FuncQA | contains | 60  | single-hop     | prob- |
| ------------------ | -------- | --------------------------- | ------- | ----------- | --- | --------------------------- | ------ | -------- | --- | -------------- | ----- |
| and Tomas          | Mikolov. | 2015.                       | Towards | ai-complete |     |                             |        |          |     |                |       |
|                    |          |                             |         |             |     | lemsand68multi-hopproblems. |        |          |     | Thetrainingset |       |
| questionanswering: |          | Asetofprerequisitetoytasks. |         |             |     |                             |        |          |     |                |       |
arXivpreprintarXiv:1502.05698. ofKAMELcontains19,000artificiallyconstructed

D ComputationalResource
|     | Dataset  |     | Tool | Train | Dev Test  |                     |               |           |
| --- | -------- | --- | ---- | ----- | --------- | ------------------- | ------------- | --------- |
|     | GSM8K-XL |     | 4    | 5,054 | 1,000 568 |                     |               |           |
|     |          |     |      |       |           | For LLaMA2-7B-Chat, | the computing | resources |
60
|     | FuncQA |     | 13  | 611 | 39  | weuseare2×NVIDIAV10032G.Trainingthe |     |     |
| --- | ------ | --- | --- | --- | --- | ----------------------------------- | --- | --- |
68
ToolRetrieverwiththeGSM8K-XLdataset(5,054
19,000
|     | KAMEL       |     | 234    |       | 1,000 500 |                                         |     |     |
| --- | ----------- | --- | ------ | ----- | --------- | --------------------------------------- | --- | --- |
|     |             |     |        | 8,095 |           | cases)takesapproximately2hoursperepoch. |     |     |
|     |             |     | 999    |       | 1,707     |                                         |     |     |
|     | STQuestions |     | 10,483 |       | 1,707     |                                         |     |     |
|     |             |     | 837    |       | 1,066     | E SafeguardingStatement                 |     |     |
Table6: Detailedinformationof4datasets,including Inthispaper,wefocusontheapplicationofTool
thenumberoftoolsforeachdatasetandthedistribution
Learningtosolvenumericalreasoningandknowl-
ofdataacrossthetraining,development,andtestsets. edgeretrievaltasks. Wedonotbelieveitposesany
|     |     |     |     |     |     | political,ethicalorlegalrisk. | Inthefuture,wewill |     |
| --- | --- | --- | --- | --- | --- | ----------------------------- | ------------------ | --- |
goldstandarddata(sup)and8,095ChatGPTsyn- also explore how LLMs can be better integrated
withToolLearningtoservehumansociety.
| thesizeddata(syn). |     |     | Theyareseparatedfortraining. |     |     |     |     |     |
| ------------------ | --- | --- | ---------------------------- | --- | --- | --- | --- | --- |
ThedatasetSTQuestionscontains999seentools
| and837unseentools. |     |     | Itstestsetisalsodividedinto |     |     |     |     |     |
| ------------------ | --- | --- | --------------------------- | --- | --- | --- | --- | --- |
1,707questionsforseentoolsand1,066questions
forunseentools.
B.2 DatasetLicense
GSM8K-XL:MITLicense.
FuncQA:ApacheLicense2.0.
| KAMEL: |     | The Creative |     | Commons | Attribution- |     |     |     |
| ------ | --- | ------------ | --- | ------- | ------------ | --- | --- | --- |
Noncommercial4.0InternationalLicense.
| STQuestions: |     | CreativeCommonsAttribution3.0 |     |     |     |     |     |     |
| ------------ | --- | ----------------------------- | --- | --- | --- | --- | --- | --- |
License.
C Prompt
| To ensure |     | experimental |     | fairness, | we all use the |     |     |     |
| --------- | --- | ------------ | --- | --------- | -------------- | --- | --- | --- |
promptprovidedinthedatasetorbaselineforinfer-
ence. TheotherPromptsutilizedareshownbelow.
ToolPrompt:
| tool | name: | [Tool | Name], | tool | description: |     |     |     |
| ---- | ----- | ----- | ------ | ---- | ------------ | --- | --- | --- |
[ToolDescription]
RetrievalPromptofthedatasetGSM8K-XL:
| [Query] |     | Let’s | think step | by  | step.[Answer |     |     |     |
| ------- | --- | ----- | ---------- | --- | ------------ | --- | --- | --- |
Fragment]
RetrievalPromptofthedatasetFuncQA:
Q:[Query]
A:[AnswerFragment]
| Retrieval |     | Prompt | of the | dataset | KAMEL and |     |     |     |
| --------- | --- | ------ | ------ | ------- | --------- | --- | --- | --- |
STQuestions:
| Question: |     | [Question]  |     |     |     |     |     |     |
| --------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
| Answer:   |     | Theansweris |     |     |     |     |     |     |
