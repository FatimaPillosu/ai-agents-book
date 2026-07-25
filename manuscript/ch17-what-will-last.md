# Chapter 17 — What will last

> **Status:** draft r3 · voice v3.3 (`STYLE.md`) · sentence-per-line per `STYLE.md` §10 · figures as briefs per `FIGURES.md`.
> **Conventions:** vendor-neutral (outline §9) · **[AUTHOR: …]** marks lived material only the author can supply · **[verify]** marks real but unconfirmed details · citations drawn only from verified reports in `/research`. Nothing has been invented.

---

## 17.1 Two layers moving at two speeds

A book about a fast-moving technology has to declare, at its close, which of its contents it expects to survive and which it expects to date, because a reader is entitled to know where to place their trust.
The material in this book occupies two layers that move at very different speeds, and the whole design of the project rests on keeping them apart.
The lower layer is the durable one: the stance that an agent is an instrument requiring specification, calibration, verification and audit (Chapter 1); the craft of writing a specification a human can audit (Chapter 3); the discipline of asking whether an agent should touch a task at all (Chapter 4); and the evidential hierarchy by which a workflow's claims are weighed (Chapter 11).
None of that reasoning depends on which model was current when it was written, because it derives from the ordinary discipline of instrumentation, which predates language models by a century and will outlast any particular one.

The upper layer is the volatile one: model names and versions, per-token prices, context-window sizes, benchmark leaderboards, the exact syntax of a tool protocol, the current wording of a journal's disclosure policy.
That layer turns over on a timescale of months, faster than a publishing cycle, and a printed page is the wrong place to record it.
The division of labour adopted throughout, in which the print states the position and the reasoning while the companion repository tracks the movement, is not an editorial convenience but the book's central bet about how to write usefully for practitioners in a field where the tooling churns faster than the understanding.
The limitation of this arrangement is that the boundary between the two layers is not always obvious in advance, and a claim that reads as durable may prove to have rested on a passing feature of one model generation; where that risk is live, this book flags it in the text, and the repository is the place where such misjudgements are corrected between releases rather than left to mislead until the next edition.

**Figure 17.1 — Durable principles versus volatile tooling.** *A figure brief follows `FIGURES.md`; render in the house style.*

```
FIGURE BRIEF
- id:            Figure 17.1
- title:         Two layers, two clocks — durable principles beneath volatile tooling
- type:          architecture
- claim:         The book separates a slow-moving layer of principles from a fast-moving layer of tooling, and assigns each to the medium that suits its clock: print for principles, repository for tooling.
- canvas:        16:9
- elements:      a horizontal divider splitting the canvas into two stacked bands;
                 lower band (grey structural border) labelled "durable — principles"
                 holding four near-black tags: "instrument stance", "specification",
                 "verification", "accountability"; upper band labelled
                 "volatile — tooling" holding four grey de-emphasis tags: "model versions",
                 "prices", "protocols", "benchmarks"; at the right margin, two small
                 medium icons — a book glyph (near-black) aligned to the lower band and a
                 data-store cylinder (sky blue) aligned to the upper band
- flow:          no directional flow; vertical stacking carries the contrast, with the
                 lower band visually anchored and the upper band marked as shifting
- labels:        "durable — principles", "instrument stance", "specification",
                 "verification", "accountability", "volatile — tooling", "model versions",
                 "prices", "protocols", "benchmarks", "print", "repository"
- annotations:   a small clock glyph beside each band — a slow clock by the lower band, a
                 fast clock by the upper — encoding the two timescales
- caption:       Figure 17.1 — Two layers moving at two speeds. The durable layer of principles is carried in print; the volatile layer of tooling is delegated to the companion repository, which absorbs change so the printed reasoning can hold.
- alt-text:      A diagram split into two horizontal bands. The lower band, labelled durable principles, contains instrument stance, specification, verification and accountability, and is marked with a slow clock and a book icon for print. The upper band, labelled volatile tooling, contains model versions, prices, protocols and benchmarks, and is marked with a fast clock and a data-store icon for the repository.
- generator prompt: A flat vector architecture diagram on an off-white background, split
                 into two stacked horizontal bands by a single near-black divider. The lower
                 band has a grey rounded border and a heading "durable — principles"; inside
                 it sit four near-black outlined tags reading "instrument stance",
                 "specification", "verification", "accountability". The upper band has a
                 heading "volatile — tooling"; inside it sit four grey outlined tags reading
                 "model versions", "prices", "protocols", "benchmarks". Beside the lower
                 band, a small slow-clock glyph and a near-black book icon labelled "print";
                 beside the upper band, a small fast-clock glyph and a sky-blue cylinder
                 labelled "repository". Minimal text, generous spacing, single-weight lines.
```

## 17.2 The principles that will last

The throughline of this book compresses to a small set of principles that carry into any future toolchain without amendment.
The first is that an agent is an instrument, not a colleague: it is specified, calibrated, verified and audited exactly as a sensor or a numerical model is, and the vocabulary of trust a scientist already commands (calibration before deployment, characterisation of drift, quality control within a designed network) transfers to it directly (Chapter 1).
The second is that specification is the primary control surface: most failures trace not to a model's limitations but to an underspecified task, and the discipline of writing an objective, inputs, acceptance criteria and stop conditions that a human can audit is the single most transferable skill in the book (Chapter 3).
The third is that verification is external and load-bearing: because language systems fail in ways that imitate competence, every check must sit outside the system being checked, and the effort a workflow saves in generation is properly reinvested in confirmation (Chapter 11).
The fourth is that some things never transfer to the instrument: accountability for a decision, the scientific judgement that an anomaly is meaningful rather than instrumental, and authorship of the work that results remain with the person, and they do not soften as models improve, because responsibility is not a capability (Chapters 1 and 4).
This one is not merely a stance of this book but the settled position of the scientific record: the journals ruled early that an AI tool cannot be an author, precisely because authorship carries an accountability a tool cannot bear (Nature editorial, 2023), and no improvement in capability changes what kind of thing an instrument is.
The fifth is that the right question is often whether to use an agent at all: the asymmetry between cheap-to-verify and expensive-to-verify outputs, not the perceived difficulty of a task, decides where delegation is safe, and the honest answer is sometimes no (Chapter 4).
These five hold at high confidence, because each rests on a property of the situation (the fallibility of instruments, the primacy of clear specification, the plausibility of fluent error, the non-transferability of responsibility, the economics of verification) rather than on any feature of a particular model.

The research frontier is drifting the same way: a 2026 proposal for an agentic scientific operating system independently centres staged objectives, verification checkpoints and bounded delegation, not validated technology, but a sign this governance-first framing sits inside a wider convergence rather than against it (Zheng et al., 2026, a weeks-old preprint).
The limitation worth stating is that principles at this altitude are easy to assent to and hard to practise; their value is realised only in the concrete disciplines of the preceding chapters, and a reader who takes the principles without the practice has taken the smaller half.

## 17.3 Staying current by principle, not by release

Keeping up with a field that ships faster than anyone can read is a genuine problem, and the durable answer is to track it by principle rather than by release.
The failure mode worth warning against is release-chasing: treating each new model, protocol or product as a thing to be learned in its own right, which is both exhausting and unnecessary, because the great majority of releases are new instances of capability classes already understood.
A more sustainable practice is to translate every announcement into the vocabulary of this book before deciding whether it warrants attention: asking what capability class it belongs to, whether it changes the cost or reliability of a task already in the workflow, and whether it moves the verification burden rather than merely the generation cost (moderate-to-high confidence that this filter removes most of the noise).
Under that filter, a faster or cheaper model of an existing class is a parameter change, not a new thing to learn; a genuinely new capability class (the arrival of reliable tool calling around 2023 was the last clear example, Chapter 1) is rare, and rare enough to deserve real study when it comes.
The second half of the practice is to let evaluation, not marketing, decide what enters a workflow: a new model earns its place by passing the same task-grounded tests as the one it replaces (Chapter 11), run on the actual task with the actual data, so that adoption is a measured substitution rather than an act of faith in a benchmark score.

The year's loudest capability claim illustrates the filter: the most consequential 2026 account of what these systems can do came from a frontier-model developer describing its own agents (most of its production code now machine-written, task horizons doubling every few months), a party with every reason to make the case look strong (Anthropic Institute, 2026).
The book's stance treats that as a hypothesis for independent measurement, and the one independent check that exists, an outside evaluation organisation finding the same doubling by a different method (METR, 2026), is what verifying a vendor's claim looks like.
The limitation of this stance is that it is deliberately conservative and will occasionally be slow to adopt something genuinely better, trading a few months of lag for freedom from churn; for a scientist whose credibility rests on the correctness of results rather than on early adoption, that is close to always the right trade, and it is the trade this book recommends.

## 17.4 The repository as the living layer

The companion repository is the mechanism that makes a printed book about a volatile technology honest, and it is where a reader will find everything this chapter has deliberately kept off the page.
The repository holds the perishable layer in full (current model and price references, protocol specifics, the runnable minimal examples for each pattern, the printable checklists, the sanitised case-study configurations, and the current wording of the journal and funder policies that Chapter 9 treats as a moving landscape) and it is versioned so that each release is a coherent rebuild rather than a drift of unmarked edits **[verify: confirm the repository layout and release-tagging scheme described in outline §8 before citing specifics]**.
This living-document model is not eccentric; it is where responsible guidance in this area is already heading.
The principal European funder guidance on AI in research is itself published as a living document, revised on a schedule (its 2026 update added, among other things, a warning about hidden instructions embedded in content, exactly the prompt-injection risk of Chapter 12), precisely because binding a fast-moving subject into a fixed text ages badly (European Commission, 2024).

The repository's role in the book's design is to absorb change so the printed principles can hold: when a model generation turns over, when a protocol is superseded, or when a claim in the text proves to have rested on a passing feature, the correction lands in the repository between editions rather than waiting for the next printing, and the newsletter announces it.
This arrangement asks something of the reader in return, which is to treat the book and the repository as one instrument with two clocks: to read the reasoning here and fetch the volatile detail there, rather than expecting either to be complete alone.
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
