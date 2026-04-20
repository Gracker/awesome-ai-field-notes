# Automated Alignment Researchers: Using large language models to scale scalable oversight

Large language models' ever-accelerating rate of improvement raises two particularly important questions for alignment research.

One is how alignment can keep up. Frontier AI models are now contributing to the development of their successors. But can they provide the same kind of uplift for alignment researchers? Could our language models be used to help align themselves?

A second question is what we'll do once models become smarter than us. Aligning smarter-than-human AI models is a research area known as "scalable oversight". Scalable oversight has largely been discussed in theoretical, rather than practical, terms—but at AI's current pace of improvement, that might not be the case for much longer. For instance, models are already generating vast amounts of code. If their skills progress to the point where they're generating millions of lines of incredibly complicated code that we can't parse ourselves, it could become very difficult to tell whether they're acting in the ways we intend.

In a new Anthropic Fellows study, we pursue both of these questions.

Our new study focuses on a problem known as "weak-to-strong supervision", a problem that mirrors the one of overseeing smarter-than-human AI models. We start with a relatively strong "base" model—that is, a potentially-capable model that hasn't yet received fine-tuning to provide its best-possible answers. Then, we use a much weaker model as a "teacher" to provide that extra fine-tuning, which it does by demonstrating what it considers ideal outputs to the strong base model. Finally, we evaluate how well the strong model performs after that weak fine-tuning.

In the worst case, the strong model will only be as good as its weak teacher. Ideally, however, the strong model will have learned from the weak teacher's feedback—it will have interpreted those weak signals in a useful way, using that feedback to improve its performance. We can quantify how well it did so: if the strong model shows no improvement at all (it performs only as well as its weak teacher), we score it 0; if it uses the teacher's feedback to achieve the ideal outcome—the best performance the strong model could possibly deliver—we score it 1. This measure represents the "performance gap recovered" (between the weak model and the upper limit of the strong model), or the PGR.

As a proxy for scalable oversight, the weak model stands in for humans, and the strong model for the much-smarter-than-human models we might one day need to oversee. If we can make progress on weak-to-strong supervision, we might find that our methods help us keep those ultra-smart models aligned to our values.

## Our setup

To find out, we began with nine copies of Claude Opus 4.6, and gave each one a few extra tools. Each Claude had a place to work and think (that is, a sandbox), a shared forum to circulate its findings with the others, a storage system to upload its code, and a remote server where it could receive a PGR score for each of its ideas. We also provided some background knowledge about model training and inference. We referred to these tooled-up Claude models as Automated Alignment Researchers (or AARs).

To prevent each AAR from pursuing near-identical ideas, we prompted each one with a slightly different (but intentionally ambiguous) starting place: we recommended that one used some interpretability tools, that another thought about reweighting the data in the dataset, and so on. Beyond that, though, we didn't tell the AARs what to do. It was up to them to propose their own ideas, run their experiments, analyze their results, and share their findings and code with one another in order to work out what to try next.

## Results

To provide a benchmark for the AARs' results, we compared their work to a human baseline. Two of our researchers spent seven days iterating on four of the most promising generalization methods from prior research. On the open-weights models we tested (Qwen 3-4B-Base as the strong model, Qwen 1.5-0.5B-Chat as the weak teacher), the humans recovered 23% of the total performance gap (i.e., achieved a PGR of 0.23).

Claude improved on this result dramatically. After five further days (and 800 cumulative hours of research), the AARs closed almost the entire remaining performance gap, achieving a final PGR of 0.97. This cost about $18,000 in tokens and model training expenses, or $22 per AAR-hour.

First, we tested whether the AARs' ideas could recover the performance gap on held-out datasets. We took the AARs' two highest-performing methods (on a dataset of chat tasks) and applied them to math and coding tasks. Here, our results were relatively promising: the AARs' most effective method successfully generalized to both new datasets, with PGRs of 0.94 on math and 0.47 on coding (which was still double the human baseline). The AARs' second-best method saw mixed results: it worked on math (0.75), but not on code, where it made matters worse.

Next, we tested whether the AARs' ideas would work at production scale. We tried out the AARs' most effective method on Claude Sonnet 4 with our production training infrastructure. Here, though, we had less success. The AARs' method didn't lead to a statistically significant improvement. We think this might reflect limitations of this early trial, rather than something more fundamental.

A few iterations taught us more about how to make AARs most effective. Giving each AAR a different starting point helped a lot, even if that starting point was vague. When we tried without setting the AARs off in different directions, they all quickly settled on similar ideas, making much less progress overall. Giving the AARs too much structure hurt their progress badly. Left to its own devices, Claude was much more adaptable.

## Implications

The success of our AARs in recovering the performance gap is certainly not a sign that frontier AI models are now general-purpose alignment scientists. We deliberately chose a problem that is unusually well-suited to automation, since it has a single, objective measure of success. Most alignment problems aren't nearly as neat as this one. And even in this setting our AARs did their best to game the problem: human oversight remains essential.

But we do think these results have some important implications.

**Keeping pace.** This study indicates that Claude can meaningfully increase the rate of experimentation and exploration in alignment research. Human researchers can delegate questions to AARs at a very large scale.

**Taste and diversity.** The success of AARs suggests that the sheer volume of ideas might compensate for a lack of "research taste". If AARs can run many experiments very cheaply, it could brute force their way into findings that a very high-taste researcher might've come up with. The core bottleneck could become evaluation rather than generation.

**Alien science.** Over time, the models' ideas could become much harder to verify, or corrupted in ways that are tricky for humans to parse. That could mean creating an "alien science".

**Preventing hacks.** Even in this highly circumscribed environment, we observed the models "reward hacking"—trying to game our set-up. On math tasks, one AAR noticed that the most common answer was usually correct, so it skipped the teacher entirely and always chose the most common one. Hacks like these don't invalidate our results but do provide a warning.

Code and datasets: https://github.com/safety-research/automated-w2s-research

原文：https://www.anthropic.com/research/automated-alignment-researchers
