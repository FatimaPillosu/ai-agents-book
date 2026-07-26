# Chapter 1 — Why agents, why now

> **Status:** draft r4 · voice v5.0 (`STYLE.md` §1) · sentence-per-line per `STYLE.md` §10 · figures as briefs per `FIGURES.md`.
> **Conventions:** vendor-neutral (outline §9) · **[AUTHOR: …]** marks lived material only the author can supply · **[verify]** marks real but unconfirmed details · citations drawn only from verified reports in `/research`. Nothing has been invented.

---

## 1.1 The problem this book addresses

Environmental science has a mismatch problem: more material demands a scientist's attention than there are hours to give it.

The data keeps arriving.
Satellite programmes deliver observations at rates measured in terabytes a day, the major model-intercomparison archives run to tens of petabytes, and an operational forecasting centre produces more output in a morning than any one scientist could read in a week [AUTHOR: verify one or two current figures — e.g. Copernicus daily volumes, CMIP6 archive size — and cite].
Every one of those streams arrives with obligations attached.
It has to be quality-controlled, reconciled with neighbouring datasets, reprocessed when a product version changes, and reported to funders and partners in formats that are themselves revised yearly.
The working hours available to meet all that have not grown at all.
So highly trained scientists spend a large share of their time on transformation, checking and formatting: skilled, necessary work that is not the science they trained to do.
[AUTHOR: a concrete morning from operational flood forecasting — the specific scramble to reconcile ensemble output, gauge records and a bulletin deadline — would ground this paragraph more firmly than any general description.]

That is why software that can act, meaning read a file, run code, inspect the result and decide the next step, is worth taking seriously.
The claims made for these systems are large and the commentary around them is sharply divided, neither of which is unusual for a technology at this stage.
This book sits between the enthusiasts and the sceptics.
These systems are instruments: powerful, fallible, and fit for serious work only once they are properly specified, checked and governed in proportion to what is riding on them.
The case for engaging now rather than waiting for things to settle rests on a few specific, datable changes in what they can do and in who can afford to use them.
Those changes are the next section.

## 1.2 What changed, and when

Agents did not arrive in one step.
They come from a short, datable lineage, and the changes that mattered most were about the interface to computation rather than about raw capability.

The lineage begins, conventionally, with the transformer architecture in 2017 (Vaswani et al., 2017), which made it practical to train language models on very large volumes of text.
Scale then produced a capability nobody had explicitly designed: in-context learning (Brown et al., 2020), the ability to pick up a new task from a few examples written into the prompt, with no retraining.
For scientific work the significance was never the benchmark scores.
It was the interface.
From that point on, a task could be described to a computer in ordinary written language, which is how scientists already describe their methods to each other.
When instruction-following conversational systems reached the public in late 2022, the shift became visible well beyond the research community, and institutional attitudes changed within months.
Every system up to that point still shared one limit, and it matters more in science than almost anywhere else.
They produced text, and text alone cannot run a quality-control pass, regrid a forecast field, or execute a test suite.

> **Definition — Large language model (LLM).** A program trained on a very large body of text that, given a sequence of words, predicts what should come next: text in, text out. It has no memory between conversations, no goals of its own, and no way of acting beyond the words it produces.

> **Definition — In-context learning.** The ability, which emerged as models got larger, to pick up a new task from nothing more than an instruction and a few examples written into the conversation, with no retraining or reprogramming. It is what lets these systems be steered in ordinary written language.

What distinguishes now from then is that these systems can take structured action: they can issue a precise, machine-readable instruction to a tool and read the result back.
From roughly 2023, models became reliable enough to produce a valid call to a declared function rather than a prose description of what such a call might look like.
That small-sounding change is what lets a system act on what it says.
It matters for science because it lets a model hand its weak points to tools that do not share them: arithmetic goes to the interpreter, retrieval goes to the database, and the model does the planning and interpretation in between.
The remaining pieces arrived alongside it.
Context windows grew long enough to hold a whole codebase or document set at once (2023–24), code generation started being checked against test suites (2024–25), models learned to operate ordinary software, and shared protocols appeared for connecting models to tools and data (2024–25).
None of these is an agent on its own.
Assembled, they make a system with a model, tools, a loop and a memory, able to carry a bounded task from instruction through to a checked result.

Public measurements are imperfect, but they corroborate this trajectory from two independent directions.
On a widely used software-engineering benchmark, the share of real-world coding issues an agent could resolve unaided rose from around 2% at the benchmark's introduction in 2023 (Jimenez et al., 2023) to far higher figures within two years; one frontier-model developer reports near-saturation for its own systems, though that figure is self-reported and should be weighed as such (Anthropic Institute, 2026).
A second measure gets to the same place by a different route.
An independent evaluation organisation tracks not benchmark scores but the duration of tasks an agent can complete autonomously at a 50% success rate, and finds it doubling roughly every four months since 2023 (about 129 days, on a 90% confidence interval of 105 to 157) and roughly every three months since 2024, against a slower doubling of about seven months across 2019 to 2025 (METR, 2026).
Both parties have an interest in demonstrating progress, so neither number is disinterested.
Two independent methods converging on the same doubling trend is, however, exactly the corroboration between measurements this book argues for throughout.
By 2026 there was a striking marker: a paper generated end to end by an agentic system passed peer review at a workshop venue, a result now itself in the peer-reviewed literature, though the authors say plainly that their system cannot yet meet the standards of top-tier publication (Lu et al., 2026).
Benchmark skill and real-workflow skill are not the same thing, and Chapter 11 develops that distinction and the evaluation practice that follows from it.

> **Definition — Tool call (structured action).** The step where an agent stops producing prose and instead issues a precise, machine-readable instruction (run this code, fetch this record, query this database) and then reads the result back. It is what lets a text model act rather than only describe.

> **Definition — Context (context window).** The finite amount of text an agent can hold in view at once: the conversation, the documents and the instructions together. When the limit is reached, older material drops out of view and stops informing what the agent decides.

The second half of the case for engaging now is about cost rather than capability.
The cost of using a capable model has fallen by orders of magnitude over the same years in which capability has risen [AUTHOR: verify a defensible figure — per-token price decline at equivalent capability tiers, 2023–26 — for the repository], and openly licensed models you can run locally are now good enough for many bounded scientific tasks.
That changes who can take part.
A research group with modest hardware and no recurring budget can, with care, build workflows of real operational value, and that constraint is treated as a design input throughout this book and revisited in the closing case studies.
One caution, so the economics are not misread: cheaper models do not make agentic work cheap.
The cost moves rather than disappears, into engineering time, into evaluation, and above all into verification, which is where a well-run scientific workflow should expect to spend most of what it saves.

**Figure 1.1 — Capability milestones (timeline).**

![A horizontal timeline from 2017 to 2026 showing seven milestones progressing from the transformer architecture, through in-context learning and public conversational systems, to tool calling, long context, coding agents with standardised tool protocols, and finally governed agentic workflows in scientific practice.](../figures/figure-1-1.svg)

*Figure 1.1 — Capability milestones, deliberately coarse and vendor-neutral; product-level detail lives in the repository and dates quickly. (Rendered as `figures/figure-1-1.svg` from the brief below, per `FIGURES.md`.)*

```
FIGURE BRIEF
- id:            Figure 1.1
- title:         From text generation to structured action
- type:          sequence (horizontal timeline)
- claim:         Agents did not arrive in one step; they are the composition of a short, datable lineage of capabilities, the decisive ones concerning the interface to computation.
- canvas:        16:9
- elements:      seven milestone markers on a single left-to-right timeline axis, each a small labelled node in near-black, with the two interface-changing milestones (in-context learning; tool calling) emphasised in agent orange
- flow:          left-to-right along one axis, 2017 to 2026
- labels:        "2017 — transformer architecture", "2020 — in-context learning",
                 "2022 — public conversational systems", "2023 — tool calling",
                 "2023–24 — long context", "2024–25 — coding agents · tool protocols",
                 "2026 — governed agentic workflows"
- annotations:   a light bracket under 2023 onward labelled "structured action closes the loop"
- caption:       Figure 1.1 — Capability milestones, deliberately coarse and vendor-neutral; product-level detail lives in the repository and dates quickly.
- alt-text:      A horizontal timeline from 2017 to 2026 showing seven milestones progressing from the transformer architecture, through in-context learning and public conversational systems, to tool calling, long context, coding agents with standardised tool protocols, and finally governed agentic workflows in scientific practice.
- generator prompt: A flat vector horizontal timeline on an off-white background. A single
                 near-black axis runs left to right with seven evenly spaced round nodes.
                 Labels beneath each node read, in order, "2017 transformer architecture",
                 "2020 in-context learning", "2022 public conversational systems",
                 "2023 tool calling", "2023–24 long context", "2024–25 coding agents and
                 tool protocols", "2026 governed agentic workflows". The nodes for
                 "in-context learning" and "tool calling" are filled orange; the rest are
                 near-black outlines. A thin bracket spans the last four nodes, labelled
                 "structured action closes the loop". Minimal text, generous spacing.
```

## 1.3 Three terms, one distinction

Most of the confusion around this technology starts with three terms used as though they were interchangeable: large language model, AI agent, and agentic workflow.
This book defines them once, here, and holds the definitions constant.

A large language model is the text-in, text-out predictor from the previous section: no memory between calls, no goals, no way of acting.
An AI agent is the working arrangement built around such a model: the model, plus the tools it is allowed to call, plus a loop that feeds each tool result back in for the next decision, plus state that survives across steps, all pointed at a goal with some discretion about how to get there.
An agentic workflow is a designed process in which agent steps sit among fixed inputs, checks the work has to pass, and points where a human decides, so the agent's freedom operates inside boundaries set in advance.
Put that way, autonomy stops being a yes-or-no property and becomes a graded one.
At one end is a single agent step inside an otherwise fixed pipeline; at the other, an open-ended system pursuing a goal with no checkpoints at all.
Where a real system sits between those two is a choice its builders make, not a fact about the technology.

> **Definition — AI agent.** An LLM given a goal, a set of tools it is allowed to use, and a loop that lets it act, see the result, and decide the next step. The model is the reasoning component; the agent is the whole working arrangement built around it.

> **Definition — Agentic workflow.** A designed process in which one or more agent steps sit inside fixed boundaries: defined inputs, checks the work has to pass, and points where a human decides. The agent chooses how to do each step, but only within limits set before it starts. This book argues for building these rather than deploying unconstrained agents.

That distinction carries the central recommendation of the book: build agentic workflows, do not deploy autonomous agents.
The reasoning is not caution for its own sake.
It is the ordinary discipline you would already apply to any new instrument.
No hydrologist "trusts" a sensor in the everyday sense of the word.
The sensor is calibrated before deployment, its drift is characterised, its readings are quality-controlled inside a network built for the purpose, and a person stays accountable for what those readings are taken to mean.
Every part of that discipline has a counterpart in the chapters ahead: specification is the deployment design (Chapter 3), gates and independent review are the quality control (Chapters 10 and 12), and evaluation is the calibration (Chapter 11).
The comparison has one limit, though, and that limit is why a full third of this book exists.
A physical sensor fails in ways you can largely anticipate.
A language system fails by imitating competence, returning an answer whose fluency tells you nothing about whether it is correct.
This property, called *plausible failure* here, is why verification gets its own part of the book rather than a paragraph, and why Chapter 13 is a gallery of failures rather than a footnote to the successes.

> **Definition — Verification gate (gate).** A checkpoint in a workflow where the agent's work has to pass a defined check before anything downstream may use it. Work that passes proceeds; work that fails goes back for revision. Nothing proceeds just because it looks right.

> **Definition — Plausible failure.** The characteristic failure of these systems: not an obvious error, but an answer that is fluent, confident and wrong. Fluency and correctness are independent properties here, which is why so much of this book is about checking.

**Figure 1.2 — The taxonomy as nesting.**

![A nested diagram. The outer box, labelled agentic workflow, contains a specification feeding an inner box labelled AI agent, which contains an LLM connected to a plan–act–observe loop alongside tools and state. The agent's output passes through a verification gate that either proceeds to a human decision point or returns to the agent.](../figures/figure-1-2.svg)

*Figure 1.2 — The taxonomy as nesting: a model inside an agent inside a workflow. Each layer adds what the inner layer lacks: the agent adds action and state to the model, and the workflow adds specification, verification and accountability to the agent. (Rendered as `figures/figure-1-2.svg` from the brief below, per `FIGURES.md`.)*

```
FIGURE BRIEF
- id:            Figure 1.2
- title:         The taxonomy as nesting — model inside agent inside workflow
- type:          architecture
- claim:         Autonomy is layered: each outer layer adds what the inner one lacks (the agent adds action and state to the model; the workflow adds specification, verification and accountability to the agent).
- canvas:        16:9
- elements:      outer rounded rectangle "agentic workflow" (grey structural border);
                 inside it, left, a "specification" tag (blue); a middle rounded rectangle
                 "AI agent" (orange border) containing an "LLM" box (orange), a
                 "plan–act–observe loop" ring, a "tools" glyph (green) and a
                 "state / memory" cylinder (sky blue); to the right of the agent a
                 diamond "verification gate" (vermillion); beyond it a "human decision"
                 head-and-shoulders icon (blue)
- flow:          left-to-right — specification → agent → gate; gate has two exits, "pass"
                 continuing right to the human decision, "fail" returning left to the agent
- labels:        "agentic workflow", "specification", "AI agent", "LLM",
                 "plan – act – observe", "tools", "state / memory", "verification gate",
                 "pass", "fail", "human decision"
- annotations:   none; the nesting itself carries the claim
- caption:       Figure 1.2 — The taxonomy as nesting: a model inside an agent inside a workflow. Each layer adds what the inner layer lacks: the agent adds action and state to the model, and the workflow adds specification, verification and accountability to the agent.
- alt-text:      A nested diagram. The outer box, labelled agentic workflow, contains a specification feeding an inner box labelled AI agent, which contains an LLM connected to a plan–act–observe loop alongside tools and state. The agent's output passes through a verification gate that either proceeds to a human decision point or returns to the agent.
- generator prompt: A flat vector architecture diagram. A large grey-bordered rounded
                 rectangle labelled "agentic workflow" fills the canvas. Near its left
                 edge, a small blue tag labelled "specification" connects rightward into a
                 medium orange-bordered rounded rectangle labelled "AI agent". Inside that
                 orange rectangle: an orange box labelled "LLM" linked to a circular loop
                 arrow labelled "plan – act – observe", a green wrench icon labelled
                 "tools", and a sky-blue cylinder labelled "state / memory". From the right
                 edge of the "AI agent" rectangle an arrow leads to a vermillion diamond
                 labelled "verification gate". The diamond has two exits: an arrow labelled
                 "pass" continuing right to a blue head-and-shoulders icon labelled "human
                 decision", and an arrow labelled "fail" curving back left into the "AI
                 agent" rectangle. Minimal text, generous spacing, single-weight lines.
```

## 1.4 An honest capability boundary

These systems are unevenly capable, in ways that defeat intuition.
Early field studies of AI-assisted knowledge work called the pattern a *jagged frontier* (Dell'Acqua et al., 2023), and it causes particular trouble in science.

The unevenness has a clear cause.
A model's competence tracks how densely a task and its variants appeared in the material it was trained on, not how difficult the task looks to a person.
Translating a numerical routine from one programming language to another, something the public code corpus is saturated with, usually comes back as correct code with passing tests.
A unit conversion buried mid-sentence in a paragraph of prose, sparse and inconsistent in the training data, gets mangled often enough that no workflow in this book leaves one unchecked.
The consequence is uncomfortable but clarifying: your intuition about which tasks are safe to delegate is a poor guide, and it has to be replaced by testing on the actual task, with the actual data, at the intended scale.

> **Definition — Jagged frontier.** A description of how unevenly these systems perform: two tasks that look equally difficult to a person can come out completely differently, one done flawlessly and the other botched. What separates reliable from unreliable is irregular and often counter-intuitive, so it has to be mapped by testing rather than guessed.

A better guide than apparent difficulty is the gap between what it costs to produce an answer and what it costs to check one.
Where checking is cheap and mechanical (code judged by a test suite, an extraction validated against a schema, a format conversion confirmed by a checksum and a round trip), an imperfect generator is operationally safe: its mistakes are caught cheaply and its successes arrive in bulk.
Those are exactly the tasks on the reliable side of the present frontier: code generation and repair, format translation, structured extraction, first-pass literature triage, and draft documentation.
Where checking is expensive, slow or subjective (a claim at the research frontier, an interpretive synthesis, an anomaly whose meaning depends on context the system does not hold), fluent output stays dangerous however capable the model, and no amount of benchmark progress moves those tasks across.
Two more observations belong in any honest boundary.
First, models remain poor judges of their own correctness, which is why every check in this book is external to the thing being checked, a principle developed properly in Chapter 11 (high confidence in the principle; the size of the effect varies by model and task).
Second, multi-step arithmetic done in prose rather than handed to a tool fails often enough that handing it over should be a rule, not a preference.
[AUTHOR: a short account of a plausible-but-wrong failure you personally caught — silent, fluent, and completely mistaken — would anchor this section better than any general claim.]

Past the merely unreliable is a third category that has nothing to do with capability, and it is the one thing this book holds fixed while everything else moves: accountability, scientific judgement, and authorship.
An agent cannot be responsible for a flood warning, cannot decide that an anomaly is real rather than an artefact, and cannot be an author of the paper that follows.
None of these limits softens as models improve, because responsibility is not a capability and does not transfer to an instrument, however good the instrument becomes.
One caveat about the boundary drawn in this section: it is drawn at the time of writing, and it will move, mostly outward, unevenly, and faster than any publishing schedule.
A printed page is the wrong place to track a moving line.
Hence the division of labour here: the print holds the position and the reasoning, the companion repository tracks the movement, and the verification practice of Part III is what makes it tolerable to work with an instrument whose specification refuses to sit still.

## 1.5 What the rest of the book does

The book runs in five parts, from foundations through practice to trust and adoption, and it is designed to be read in that order without depending on it.
Part I finishes the groundwork: the anatomy of an agent (Chapter 2), how to specify work for one (Chapter 3), and the stance to take towards the technology (Chapter 4).
Part II develops five core patterns across the research lifecycle, from literature (Chapter 5) to manuscript (Chapter 9), each following an identical anatomy and each grounded in worked examples from operational hydrology and meteorology, before a final chapter composes them into multi-agent workflows (Chapter 10).
Part III is the part that matters most, covering verification, provenance, governance and security, and it closes with an unvarnished gallery of failures (Chapter 13).
Part IV puts the apparatus to work in two end-to-end case studies.
Part V is about adoption in a real research group, including the costs (financial, institutional and energetic) a responsible adoption has to price in.
The examples throughout come from one corner of the environmental sciences.
The patterns were chosen, and written, to travel beyond it.

---

### References (verify details before release)

- Anthropic Institute (Favaro, M. and Clark, J.) (2026). When AI builds itself. *The Anthropic Institute.* https://www.anthropic.com/institute/recursive-self-improvement
- Brown, T. B., et al. (2020). Language models are few-shot learners. *Advances in Neural Information Processing Systems 33*. [verify]
- Dell'Acqua, F., et al. (2023). Navigating the jagged technological frontier: field experimental evidence of the effects of AI on knowledge worker productivity and quality. *Harvard Business School Working Paper 24-013*. [verify]
- Jimenez, C. E., Yang, J., Wettig, A., Yao, S., Pei, K., Press, O. and Narasimhan, K. (2023). SWE-bench: can language models resolve real-world GitHub issues? *ICLR 2024*. https://arxiv.org/abs/2310.06770
- Lu, C., Lu, C., Lange, R. T., Yamada, Y., Hu, S., Foerster, J., Ha, D. and Clune, J. (2026). Towards end-to-end automation of AI research. *Nature*, 651, 914–919. DOI: 10.1038/s41586-026-10265-5
- METR (2026). Time Horizon 1.1. *METR research blog*, 29 January 2026. https://metr.org/blog/2026-1-29-time-horizon-1-1/
- Vaswani, A., et al. (2017). Attention is all you need. *Advances in Neural Information Processing Systems 30*. [verify]
