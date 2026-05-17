# Anthropic Interviewer：用 AI 对 1,250 名专业人士进行大规模质性访谈

*原文：[Anthropic 官方博客](https://www.anthropic.com) | 翻译：AI Field Notes*

**EN**

We're launching a new tool, Anthropic Interviewer, to help understand people's perspectives on AI. In this research post, we introduce the tool, describe a test of it on a sample of professionals, and discuss our early findings. We also discuss future work in this direction that we can now explore with the development of this tool and through partnerships with creatives, scientists, and teachers.

**ZH**

[TODO — see original English above]

**EN**

## Introduction

**ZH**

[TODO — see original English above]

**EN**

Millions of people now use AI every day. As a company developing AI systems, we want to know how and why they're doing so, and how it affects them. In part, this is because we want to use people's feedback to develop better products — but it's also because understanding people's interactions with AI is one of the great sociological questions of our time.

**ZH**

[TODO — see original English above]

**EN**

We recently designed a tool to investigate patterns of AI use while protecting our users' privacy. It enabled us to analyze changing patterns of AI use across the economy. But the tool only allowed us to understand what was happening within conversations with Claude. What about what comes afterwards? How are people actually using Claude's outputs? How do they feel about it? What do they imagine the role of AI to be in their future? If we want a comprehensive picture of AI's changing role in people's lives, and to center humans in the development of models, we need to ask people directly.

**ZH**

[TODO — see original English above]

**EN**

Such a project would require us to run many hundreds of interviews. Here, we enlisted AI to help us do so. We built an interview tool called Anthropic Interviewer. Powered by Claude, Anthropic Interviewer runs detailed interviews automatically at unprecedented scale, feeding its results back to human researchers for analysis. This is a new step in understanding the wants and needs of our users, as well as gathering data for the analysis of AI's societal and economic impacts.

**ZH**

[TODO — see original English above]

**EN**

To test Anthropic Interviewer, we had it run 1,250 interviews with professionals — the general workforce (N=1,000), scientists (N=125), and creatives (N=125) — about their views on AI. We're publicly releasing all interview data from this initial test (with participant consent) for researchers to explore; we provide our own analysis below. Briefly, here are some examples of what we found:

**ZH**

[TODO — see original English above]

**EN**

- In our sample, people are optimistic about the role AI plays in their work. Positive sentiments characterized the majority of topics discussed. However, a small number of topics such as educational integration, artist displacement, and security concerns, came with more pessimistic outlooks.
- People from the general workforce want to preserve tasks that define their professional identity while delegating routine work to AI. They envision futures where routine tasks are automated and their role shifts to overseeing AI systems.
- Creatives are using AI to increase their productivity despite peer judgement and anxiety about the future. They are navigating both the immediate stigma of AI use in creative communities and deeper concerns about economic displacement and the erosion of human creative identity.
- Scientists want AI partnership but can't yet trust it for core research. Scientists uniformly expressed a desire for AI that could generate hypotheses and design experiments. But at present, they confined their actual use to other tasks like writing manuscripts or debugging analysis code.

**ZH**

[TODO — see original English above]

**EN**

### General workforce

**ZH**

[TODO — see original English above]

**EN**

Career adaptation. Trucking dispatcher: "I'm always trying to figure out things that humans offer to the industry that can't be automated and really hone in on that aspect like the personalized human interactions. However, that is not something that I think will be necessary in the long run. I'm still trying to figure out what skills would be good to work on that AI can't 'take over.'"

**ZH**

[TODO — see original English above]

**EN**

Societal perspectives. Office assistant: "It's a tool to me like a computer was, or a type writer was in the day — computers didn't get rid of mathematicians, they just made them able to do more and that is where I see AI going in the best possible future."

**ZH**

[TODO — see original English above]

**EN**

Writing independence. Salesperson: "I hear from colleagues that they can tell when email correspondence is AI generated and they have a slightly negative regard for the sender. They feel slighted that the sender is 'too lazy' to send them a personal note and push it onto AI to do it."

**ZH**

[TODO — see original English above]

**EN**

Educational integration. Special education teacher: "I am hoping that AI will be a more collaborative partner that will help me better manage my time and help me expand creatively so I can offer my students a wide variety of activities and assignments that I may not have been able to come up with on my own."

**ZH**

[TODO — see original English above]

**EN**

### Creatives

**ZH**

[TODO — see original English above]

**EN**

Control boundaries. Gamebook writer: "During these storytelling sessions, I would say that there's only the illusion of collaboration for the most part… there's rarely a point where I've really felt like the AI is driving the creative decision-making."

**ZH**

[TODO — see original English above]

**EN**

Workflow automation. Social media manager: "I'm less stressed, honestly. It has created a ton of efficiency for me so I can focus on my favorite aspects of the job (filming and editing)."

**ZH**

[TODO — see original English above]

**EN**

Writer displacement. Creative fiction writer: "A novel written by AI might have a great plot and be technically brilliant. But it won't have the deeper nuances that only a human can weave throughout the story."

**ZH**

[TODO — see original English above]

**EN**

Music production. Music producer: "Sometimes, when it comes time to add lyrics, I'll ask ChatGPT or Claude for lists of interesting word pairings. Just getting a long list to try out over the instrumental often leads to finding a hook or at least a seed for a song idea."

**ZH**

[TODO — see original English above]

**EN**

### Scientists

**ZH**

[TODO — see original English above]

**EN**

Security concerns. Medical scientist: "Our confidence in AI just isn't high enough at the moment to trust it with our data. We're also a commercial entity so there's a bit of concern over confidentially with data that we might share with an AI system."

**ZH**

[TODO — see original English above]

**EN**

Research assistance. Molecular biologist: "If AI could integrate and normalize all this data in a single repository, it could be a very exciting thing for biological discovery. You could see how expression dynamics change across cell models, tissue types, disease states, and more."

**ZH**

[TODO — see original English above]

**EN**

Content verification. Economist: "What I would really like from an AI would be the ability to accurately grab information, summarise it and use it to write the core of a funding application. AI generally writes well; the problem now is that I just can't rely on it not hallucinating, or to put it bluntly, lying."

**ZH**

[TODO — see original English above]

**EN**

Code development. Food scientist: "Honestly I wouldn't have known how to help my student with her code if something was off without AI tools."

**ZH**

[TODO — see original English above]

**EN**

## Method

**ZH**

[TODO — see original English above]

**EN**

This initial test explored how workers integrate AI into their professional practice and how they feel about its role in their future. We ran interviews to produce qualitative data, and supplemented them with quantitative data from surveys where participants answered questions on their behavioral and occupational backgrounds. We also had a separate AI analysis tool read the interview transcripts and cluster together emergent, overarching themes from the unstructured data.

**ZH**

[TODO — see original English above]

**EN**

### Participants

**ZH**

[TODO — see original English above]

**EN**

We used Anthropic Interviewer to conduct interviews with 1,250 professionals. We intend for the tool to interview general Claude.ai users, but for this initial test, we sought participants working across a range of professions and engaged them through crowdworker platforms (all participants had an occupation other than crowdworking that was their main job).

**ZH**

[TODO — see original English above]

**EN**

1,000 of our participants were recruited from a general sample of occupations (that is, we did not select participants from specific jobs). Of that group, the largest subgroups came from educational instruction (17%), computer and mathematical occupations (16%), and arts, design, entertainment, and media (14%).

**ZH**

[TODO — see original English above]

**EN**

We also recruited two specialist samples of 125 participants each. The first was from creative professions: predominantly writers and authors (48% of the sample), and visual artists (21%), with smaller groups of filmmakers, designers, musicians, and craft workers. The second was from science, which included physicists (9%), chemists (9%), chemical engineers (7%), and data scientists (6%), with representation across 50+ other distinct scientific disciplines.

**ZH**

[TODO — see original English above]

**EN**

We chose to add these two specialist subgroups because these represent professional domains where AI's role remains contested and is rapidly evolving. We hypothesized that creatives and scientists would reveal distinct patterns of AI adoption and professional concerns.

**ZH**

[TODO — see original English above]

**EN**

All participants provided informed consent for us to analyze their interview data for research purposes and for us to release the transcripts publicly.

**ZH**

[TODO — see original English above]

**EN**

### How Anthropic Interviewer works

**ZH**

[TODO — see original English above]

**EN**

Anthropic Interviewer operates in three stages: planning, interviewing, and analysis.

**ZH**

[TODO — see original English above]

**EN**

**Planning**: In this phase, Anthropic Interviewer creates an interview rubric that allows it to focus on the same overall research questions across hundreds or thousands of interviews, but which is still flexible enough to accommodate variations and tangents that might occur in individual interviews.

**ZH**

[TODO — see original English above]

**EN**

We developed a system prompt to give Anthropic Interviewer its methodology. This was where we included hypotheses regarding each sample, as well as best practices for creating an interview plan.

**ZH**

[TODO — see original English above]

**EN**

**Interviewing**: Anthropic Interviewer then conducted real-time, adaptive interviews following its interview plan. The interviews conducted by Anthropic Interviewer appeared on Claude.ai and lasted about 10-15 minutes with each participant.

**ZH**

[TODO — see original English above]

**EN**

**Analysis**: Once interviews were complete, a human researcher collaborated with Anthropic Interviewer to analyze the transcripts. Anthropic Interviewer's analysis step takes as input the initial interview plan and outputs answers to the research questions alongside illustrative quotations. At this stage, we also used our automated AI analysis tool to identify emergent themes and quantify their prevalence across participants.

**ZH**

[TODO — see original English above]

**EN**

### Research goals

**ZH**

[TODO — see original English above]

**EN**

The following were the main research goals for each subsample:

**ZH**

[TODO — see original English above]

**EN**

- **General workforce**: "Understand how individuals integrate AI tools into their professional workflows, exploring usage patterns, task preferences, and interaction styles to gain insights into the evolving relationship between humans and AI in workplace contexts."
- **Creatives**: "To understand how creative professionals currently integrate AI into their creative processes, their experiences with AI's impact on their work, and their vision for the future relationship between AI and human creativity."
- **Scientists**: "To understand how AI systems integrate into scientists' daily research workflows, examining their current usage patterns, perceived value, trust levels, and barriers to adoption across different stages of the scientific process."

**ZH**

[TODO — see original English above]

**EN**

## Results

**ZH**

[TODO — see original English above]

**EN**

Below we discuss what we discovered in our interviews and provide quantitative data from our survey and thematic analysis.

**ZH**

[TODO — see original English above]

**EN**

### AI's impact in the general workforce

**ZH**

[TODO — see original English above]

**EN**

Overall, the members of our general sample of professionals described AI as a boost to their productivity. In the survey, 86% of professionals reported that AI saves them time and 65% said they were satisfied with the role AI plays in their work.

**ZH**

[TODO — see original English above]

**EN**

One theme that surfaced is how workplace dynamics affect the adoption of AI. 69% of professionals mentioned the social stigma that can come with using AI tools at work.

**ZH**

[TODO — see original English above]

**EN**

Whereas 41% of interviewees said they felt secure in their work and believed human skills are irreplaceable, 55% expressed anxiety about AI's impact on their future. 25% of the group expressing anxiety said they set boundaries around AI use (e.g. an educator always creating lesson plans themselves), while 25% adapted their workplace roles, taking on additional responsibilities or pursuing more specialized tasks.

**ZH**

[TODO — see original English above]

**EN**

Approaches to AI use varied widely. One data quality manager deliberately chose learning over automation.

**ZH**

[TODO — see original English above]
