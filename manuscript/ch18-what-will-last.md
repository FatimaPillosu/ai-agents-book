# Chapter 18 — What will last

> **Status:** draft r7 · voice v5.0 (`STYLE.md` §1) · sentence-per-line per `STYLE.md` §10 · figures as briefs per `FIGURES.md`.
> **Conventions:** vendor-neutral (outline §9) · **[AUTHOR: …]** marks lived material only the author can supply · **[verify]** marks real but unconfirmed details · citations drawn only from verified reports in `/research`. Nothing has been invented.

---

## 18.1 Two layers moving at two speeds

A book about a fast-moving technology owes you, at its close, a statement of which of its contents it expects to survive and which it expects to date.

The material here sits in two layers moving at very different speeds.
The first layer is the durable one: the stance that an agent is an instrument requiring specification, calibration, verification and audit (Chapter 1); the craft of writing a specification a human can audit (Chapter 3); the discipline of asking whether an agent should touch a task at all (Chapter 4); and the evidential hierarchy by which a workflow's claims are weighed (Chapter 11).
None of that reasoning depends on which model was current when it was written.
The second layer is the volatile one: model names and versions, per-token prices, context-window sizes, benchmark leaderboards, the exact syntax of a tool protocol, the current wording of a journal's disclosure policy.
That layer turns over on a timescale of months.
The limitation is that the boundary between the two layers is not always obvious in advance, and a claim that reads as durable may turn out to have rested on a passing feature of one model generation.

**Figure 18.1 — Durable principles versus volatile tooling.**

![Two stacked bands split by a horizontal divider. The upper band, volatile tooling, holds four grey tags, model versions, prices, protocols and benchmarks, beside a fast clock, annotated turns over in months, and assigned to the repository, which is versioned and dated. The lower band, durable principles, holds four near-black tags, the instrument stance, specification, verification and accountability, beside a slow clock, annotated derives from how science treats any instrument, and assigned to print. A footer reads read the reasoning in print, fetch the current detail from the repository, and expect neither to be complete alone.](../figures/figure-18-1.svg)

*Figure 18.1 — Two layers, two clocks, two media. The tooling layer turns over in months, so it lives in the repository, where an entry can carry a date and be corrected between releases. The principles layer derives from how science treats any instrument, so it lives in print. The book only works if you read it as one instrument with two clocks: the reasoning here, the current detail there. (Rendered as `figures/figure-18-1.svg` from its brief in `fig-brief/ch18-what-will-last.md`, per `FIGURES.md`.)*

## 18.2 The principles that will last

The argument of this book compresses to a small set of principles that carry into any future toolchain.

The first is that an agent is an instrument, not a colleague: it is specified, calibrated, verified and audited exactly as a sensor or a numerical model is, and the vocabulary of trust a scientist already commands (calibration before deployment, characterisation of drift, quality control within a designed network) transfers to it directly (Chapter 1).

The second is that the specification is where you actually keep control: most failures trace not to a model's limitations but to an underspecified task, and writing an objective, inputs, acceptance criteria and stop conditions a human can audit is the single most transferable skill in the book (Chapter 3).

The third is that verification is external: because language systems fail in ways that imitate competence, every check has to sit outside the system being checked, and the effort a workflow saves in generation is properly spent again on confirmation (Chapter 11).

The fourth is that some things never transfer to the instrument: accountability for a decision, the scientific judgement that an anomaly is meaningful rather than instrumental, and authorship of the work that results remain with the person, and they do not soften as models improve, because responsibility is not a capability (Chapters 1 and 4).
This one is not merely a stance of this book but the settled position of the scientific record: the journals ruled early that an AI tool cannot be an author, precisely because authorship carries an accountability a tool cannot bear (Nature editorial, 2023), and no improvement in capability changes what kind of thing an instrument is.

The fifth is that the right question is often whether to use an agent at all, and the answer is sometimes no.
What bounds delegation is the cost of checking, and that cost belongs to the task rather than to the model.

All five hold at high confidence, because each rests on a property of the situation rather than on any feature of a particular model: the fallibility of instruments, the primacy of clear specification, the plausibility of fluent error, the non-transferability of responsibility. 

## 18.3 Staying current by principle, not by release

Keeping up with a field that ships faster than anyone can read is a genuine problem, and the durable answer is to track it by principle rather than by release.

The failure to warn against is release-chasing: treating every new model, protocol or product as a thing to learn in its own right.
That is both exhausting and unnecessary, because the great majority of releases are new instances of capability classes you already understand.
A more sustainable practice is to translate every announcement into this book's vocabulary before deciding whether it warrants attention: what capability class it belongs to, whether it changes the cost or reliability of a task already in the workflow, and whether it moves the verification burden rather than merely the generation cost. 
An announcement that moves only the generation cost does not widen the class of work worth delegating, which is why so few announcements matter.

Under that filter, a faster or cheaper model of an existing class is a parameter change, not a new thing to learn; a genuinely new capability class is rare, and rare enough to deserve real study when it comes.
The second half of the practice is to let evaluation, not marketing, decide what enters a workflow: a new model earns its place by passing the same task-grounded tests as the one it replaces (Chapter 11), run on the actual task with the actual data, so that adoption is a measured substitution rather than an act of faith in a benchmark score.

The year's loudest capability claim illustrates the filter: the most consequential 2026 account of what these systems can do came from a frontier-model developer describing its own agents (most of its production code now machine-written, task horizons doubling every few months), a party with every reason to make the case look strong (Anthropic Institute, 2026).
The book's stance treats that as a hypothesis for independent measurement, and the one independent check that exists, an outside evaluation organisation finding the same doubling by a different method (METR, 2026), is what verifying a vendor's claim looks like.
The limitation of this stance is that it is deliberately conservative and will occasionally be slow to adopt something genuinely better, trading a few months of lag for freedom from churn; for a scientist whose credibility rests on the correctness of results rather than on early adoption, that is close to always the right trade, and it is the trade this book recommends.

## 18.4 The repository as the living layer

The companion repository is what makes a printed book about a volatile technology honest, and it is where you will find everything this chapter has deliberately kept off the page.
The repository holds the perishable layer in full (current model and price references, protocol specifics, the runnable minimal examples for each pattern, the printable checklists, the sanitised case-study configurations, and the current wording of the journal and funder policies that Chapter 9 treats as a moving landscape) and it is versioned so that each release is a coherent rebuild rather than a drift of unmarked edits **[verify: confirm the repository layout and release-tagging scheme described in outline §8 before citing specifics]**.
This living-document model is not eccentric.
It is where responsible guidance in this area is already heading.
The principal European funder guidance on AI in research is itself published as a living document, revised on a schedule (its 2026 update added, among other things, a warning about hidden instructions embedded in content, exactly the prompt-injection risk of Chapter 12), precisely because binding a fast-moving subject into a fixed text ages badly (European Commission, 2024).

The repository's role in the design is to absorb change so the printed principles can hold.
When a model generation turns over, when a protocol is superseded, or when a claim in the text turns out to have rested on a passing feature, the correction lands in the repository between editions rather than waiting for the next printing, and the newsletter announces it.
That asks something of you in return: treat the book and the repository as one instrument with two clocks, reading the reasoning here and fetching the volatile detail there, rather than expecting either to be complete on its own.
The honest limitation is that a living layer lives only if it is maintained, and a repository that falls out of date is worse than none, because it invites misplaced trust of exactly the kind this book spends a third of its length guarding against; the maintenance commitment is therefore part of the book's governance, not an optional extra **[AUTHOR: state the intended maintenance cadence and who is responsible, so the reader knows how current to expect the living layer to be]**.
What will last, in the end, is not any tool this book could have named but the stance towards tools it has argued for throughout: specify the work, verify the output, keep the judgement and the accountability with the scientist, and let the instrument be an instrument.

---

### References

Report-sourced references carry a DOI or URL and are drawn from the verified sweep in `/research`.

- Anthropic Institute (Favaro, M. and Clark, J.) (2026). When AI builds itself. *The Anthropic Institute.* https://www.anthropic.com/institute/recursive-self-improvement
- European Commission, Directorate-General for Research and Innovation (2024; updated 8 May 2026). Living guidelines on the responsible use of generative AI in research (European Research Area). Update announcement: https://research-and-innovation.ec.europa.eu/news/all-research-and-innovation-news/updated-era-living-guidelines-responsible-use-generative-ai-research-2026-05-08_en **[verify the 2026 update's provisions against the updated PDF before release]**
- METR (2026). Time Horizon 1.1. *METR research blog*, 29 January 2026. https://metr.org/blog/2026-1-29-time-horizon-1-1/
- Nature (editorial) (2023). Tools such as ChatGPT threaten transparent science; here are our ground rules for their use. *Nature*, 613, 612. DOI: 10.1038/d41586-023-00191-1
- Zheng, Y., Wang, Y., Lu, J., et al. (2026). Rethinking scientific discovery in the agentic era. *arXiv preprint.* https://arxiv.org/abs/2607.03863
