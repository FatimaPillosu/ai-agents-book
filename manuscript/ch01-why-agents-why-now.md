# Chapter 1 — Why agents, why now

> **Status:** draft r2 · voice v2.0 (`STYLE.md`) · sentence-per-line per `STYLE.md` §10 · figures as briefs per `FIGURES.md`.
> **Conventions:** vendor-neutral (outline §9) · **[AUTHOR: …]** marks lived material only the author can supply · **[verify]** marks real but unconfirmed details · citations drawn only from verified reports in `/research`. Nothing has been invented.

---

## 1.1 The problem this book addresses

If you want to know what has really changed in environmental science this past decade, don't look first at the models — look at the mismatch between how much there is to attend to and how little attention any of us actually has.
The supply side has grown relentlessly: satellite programmes now deliver observations at rates measured in terabytes a day, the big model-intercomparison archives run to tens of petabytes, and an operational forecasting centre produces more in a morning than any one person could read in a week [AUTHOR: verify one or two current figures — e.g. Copernicus daily volumes, CMIP6 archive size — and cite].
Every one of those streams carries obligations with it: it has to be quality-controlled, reconciled with its neighbours, reprocessed when a version changes, and reported to funders and partners in formats that are themselves revised yearly.
What hasn't grown is the number of hours in anyone's week.
The result — and I suspect you recognise it, because I certainly do — is that highly trained scientists spend a large part of their time on transformation, checking and formatting: skilled, necessary work that is nonetheless not the science they trained to do.
[AUTHOR: drop in a concrete morning from operational flood forecasting here — the specific scramble to reconcile ensemble output, gauge records and a bulletin deadline will land far harder than any general description.]

Against that background, software that can actually act — read a file, run some code, look at the result, and decide what to do next — deserves a serious look rather than a reflexive one in either direction.
The claims made for these systems are enormous, the commentary around them is polarised, and neither of those things is unusual for a technology at this stage of its life.
My own position, which runs through the whole book, is deliberately narrower than either the boosters or the sceptics would like: these systems are instruments — powerful, fallible, and fit for serious work only once they are calibrated, checked, and kept under governance that matches the decisions resting on them.
That is not a grand claim, and it is meant not to be.
The case for engaging now, rather than waiting for the dust to settle, rests on a small number of specific, datable changes in what these systems can do and in who can afford them — and that is where I want to start.

## 1.2 What changed, and when

The path to agents is shorter than the hype suggests, and the turning points were mostly about how we talk to a computer rather than about raw horsepower.
It starts, conventionally, with the transformer architecture in 2017 (Vaswani et al., 2017), which made it practical to train language models on very large amounts of text.
Scale then produced something nobody had explicitly designed: in-context learning (Brown et al., 2020) — the ability to pick up a new task from a few examples written into the prompt, with no retraining at all.
For a working scientist the interesting part was never the benchmark scores; it was what this did to the interface, because from then on you could describe a task in ordinary written language, which is exactly how we already describe our methods to one another.
When instruction-following chat systems reached the public in late 2022, that shift became visible to everyone, and institutional attitudes changed within months.
But everything up to that point shared one limit that matters more in science than almost anywhere else: these systems produced text, and text on its own cannot run a quality-control pass, regrid a forecast field, or execute a test suite.

> **In plain terms — Large language model (LLM).** A program that has read an enormous amount of text and, given some words, predicts what should come next. That is genuinely all it does: text in, text out. It has no memory of you between conversations, no goals of its own, and no way to touch anything beyond the words it produces.

> **In plain terms — In-context learning.** The knack, which appeared as models grew larger, of picking up a new task from nothing more than an instruction and a couple of examples written into the conversation — no retraining, no reprogramming. It is why you can steer these systems in ordinary written language.

What makes the present moment different is that agents can now take structured action — they can issue a precise, machine-readable instruction to a tool and then read back the result.
From roughly 2023, models became reliable enough to produce a valid call to a declared function, rather than a prose description of what such a call might look like, and that apparently small change closed the loop between saying and doing.
It matters for science because it lets a model hand its own weak points to tools that don't share them: arithmetic goes to the interpreter, retrieval goes to the database, and the model is left doing the planning and interpretation in between.
The other pieces arrived alongside it: context long enough to hold a whole codebase or document set in view (2023–24), code generation checked against test suites (2024–25), the ability to operate ordinary software, and shared protocols for plugging models into tools and data (2024–25).
None of these is an agent on its own; assembled, they give you a system with a model, some tools, a loop and a memory, able to carry a bounded task from instruction through to a checked result.
You can even watch the trend in public numbers: on a widely used software-engineering benchmark, the share of real-world coding issues an agent could resolve unaided rose from around 2% at the benchmark's introduction in 2023 (Jimenez et al., 2023) to figures several times higher by late 2025 [verify] — though, as I'll keep insisting, benchmark skill and real-workflow skill are not the same animal (Chapter 11).

> **In plain terms — Tool call (structured action).** The moment an agent stops writing prose and instead issues a precise, machine-readable instruction — run this code, fetch this record, query this database — and then reads the result back. It is what lets a text model actually *do* things rather than only describe them.

> **In plain terms — Context (context window).** The finite amount of text an agent can hold "in view" at once — the conversation, the documents, the instructions, all of it. Picture a working desk of fixed size: pile too much on and older things slide off the edge.

There is a second half to the "why now", and it is about money rather than capability.
The cost of using a capable model has fallen by orders of magnitude over the same years its capability has risen [AUTHOR: verify a defensible figure — per-token price decline at equivalent capability tiers, 2023–26 — for the repository], and openly licensed models you can run yourself are now good enough for many bounded scientific tasks.
That changes who gets to play: a group with modest hardware and no recurring budget can, with care, build workflows of real operational value — a constraint I treat as a design input throughout, and return to properly in the closing case studies.
I'd add one caution so the economics don't mislead you: cheaper models do not make agentic work cheap, because the cost moves rather than vanishes — into engineering time, into evaluation, and above all into verification, which is where a well-run scientific workflow should expect to spend most of what it saves.

**Figure 1.1 — Capability milestones (timeline).** *A figure brief follows `FIGURES.md`; render in the house style.*

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

A lot of the confusion around this technology starts with three words that get used as if they were interchangeable, so let me pin them down and then hold them steady for the rest of the book.
A large language model is the text-in, text-out predictor from a moment ago: no memory between calls, no goals, no hands.
An AI agent is what you get when you build a working arrangement around such a model — the model, plus tools it is allowed to call, plus a loop that feeds each tool's result back in for the next decision, plus state that persists across steps — all pointed at a goal, with some discretion about how to reach it.
An agentic workflow is a designed process in which those agent steps sit among fixed inputs, checks the work must pass, and points where a human decides, so that the agent's freedom operates inside boundaries you set in advance.
Put like that, autonomy stops being a yes-or-no property and becomes a dial: at one end a single agent step inside an otherwise fixed pipeline, at the other an open-ended system chasing a goal with no checkpoints, and where any real system sits between those is a choice its builders make, not a fact about the technology.

> **In plain terms — AI agent.** An LLM with a job to do and the means to act on it: give it a goal, a set of tools it is allowed to use, and a loop that lets it try something, look at what happened, and decide the next step. The model is the reasoning part; the agent is the whole working arrangement built around it.

> **In plain terms — Agentic workflow.** A designed process in which one or more agent steps sit inside fixed rails — defined inputs, checks the work must pass, and points where a human decides. The agent has room to choose how it does each step, but only inside boundaries you set before it starts. This book argues for building these, rather than turning an agent loose.

That distinction is doing real work, because it underwrites the central recommendation of this book: build agentic workflows, don't deploy autonomous agents.
The reasoning isn't timidity; it's the ordinary discipline we already apply to any new instrument.
No hydrologist "trusts" a sensor in the everyday sense of the word — the sensor is calibrated before it goes out, its drift is characterised, its readings are quality-controlled inside a network built for the purpose, and a person stays accountable for what those readings are taken to mean.
Every part of that discipline has a counterpart in the chapters ahead: specification is the deployment design (Chapter 3), gates and independent review are the quality control (Chapters 10 and 12), and evaluation is the calibration (Chapter 11).
The analogy has one limit worth stating up front, because it motivates a full third of the book: a physical sensor fails in ways you can largely anticipate, whereas a language system fails by imitating competence — handing you an answer whose fluency tells you nothing about whether it is right.
That property — I call it plausible failure — is why verification gets its own part of this book rather than a paragraph, and why Chapter 13 is a gallery of failures rather than a footnote to the successes.

> **In plain terms — Verification gate (gate).** A checkpoint in a workflow where the agent's work has to pass a defined check before anything downstream is allowed to use it. Pass, and the work moves on; fail, and it loops back. Nothing proceeds just because it looks right.

> **In plain terms — Plausible failure.** The particular way these systems go wrong: not with an obvious error, but with an answer that is fluent, confident and completely mistaken. Fluency and correctness are separate things here — which is why so much of this book is about checking.

**Figure 1.2 — The taxonomy as nesting.** *A figure brief follows `FIGURES.md`; render in the house style.*

```
FIGURE BRIEF
- id:            Figure 1.2
- title:         The taxonomy as nesting — model inside agent inside workflow
- type:          architecture
- claim:         Autonomy is layered: each outer layer adds what the inner one lacks — the agent adds action and state to the model; the workflow adds specification, verification and accountability to the agent.
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
- caption:       Figure 1.2 — The taxonomy as nesting: a model inside an agent inside a workflow. Each layer adds what the inner layer lacks — the agent adds action and state to the model; the workflow adds specification, verification and accountability to the agent.
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

Any honest account of what these systems can do has to start by admitting that the capability is wildly uneven, in ways that defeat intuition — a pattern early field studies of AI-assisted knowledge work called a jagged frontier (Dell'Acqua et al., 2023), and one that bites especially hard in science.
The reason is no mystery: a model's competence tracks how densely a task and its variants appeared in what it learned from, not how hard the task looks to a person.
Translating a numerical routine from one programming language to another — something the public code corpus is saturated with — usually comes back correct, with the tests passing.
A unit conversion tucked mid-sentence into a paragraph of prose — sparse and inconsistent in the training data — gets mangled often enough that no workflow in this book leaves one unchecked.
The practical upshot is uncomfortable but freeing: your intuition about which tasks are safe to hand over is close to worthless, and has to be replaced by testing on the actual task, with the actual data, at the scale you actually intend.

> **In plain terms — Jagged frontier.** A vivid way of describing how unevenly these systems perform: two tasks that feel equally hard to a person can sit on opposite sides of a line, one done flawlessly and the other botched. The edge between "reliable" and "unreliable" is jagged and often counter-intuitive, so it has to be mapped by testing, not guessed.

A far better guide than "how hard does this look" is the gap between how much it costs to produce an answer and how much it costs to check one.
Where checking is cheap and mechanical — code judged by a test suite, an extraction validated against a schema, a format conversion confirmed by a checksum and a round trip — an imperfect generator is operationally safe, because its mistakes are caught cheaply and its successes arrive in bulk; and those are exactly the tasks on the reliable side of today's frontier: code generation and repair, format translation, structured extraction, first-pass literature triage, draft documentation.
Where checking is expensive, slow or subjective — a claim at the research frontier, an interpretive synthesis, an anomaly whose meaning depends on context the system doesn't hold — fluent output stays dangerous no matter how capable the model, and no amount of benchmark progress moves it across.
Two more things belong in any honest boundary.
Models remain poor judges of their own correctness, which is why every check in this book lives outside the thing being checked — a principle I keep returning to and develop properly in Chapter 11 (high confidence in the principle; the size of the effect varies by model and task).
And multi-step arithmetic done in prose, rather than handed to a tool, fails often enough that delegating it should be a rule, not a preference.
[AUTHOR: a short account of a plausible-but-wrong failure you personally caught — silent, fluent, and completely mistaken — would anchor this section better than any general claim.]

Beyond the merely unreliable sits a third category that isn't about capability at all, and it's the one I hold fixed while everything else moves: accountability, scientific judgement, and authorship.
An agent cannot be responsible for a flood warning, cannot decide that an anomaly is real rather than an artefact, and cannot be an author of the paper that follows — and none of these limits softens as the models improve, because responsibility isn't a capability and doesn't transfer to an instrument, however good the instrument becomes.
The boundary I've drawn here comes with one honest caveat: I'm drawing it at the time of writing, it will move — mostly outward, unevenly, and faster than any publishing schedule — and a printed page is the wrong place to track a moving line.
So the division of labour in this book is deliberate: the print holds the position and the reasoning, the companion repository tracks the movement, and the verification machinery of Part III is what makes it bearable to work with an instrument whose specification refuses to sit still.

## 1.5 The shape of what follows

The book runs from foundations through practice to trust, and then out into adoption, and it is built to be read in that order without being precious about it.
Part I finishes the groundwork: the anatomy of an agent (Chapter 2), the craft of specifying work for one (Chapter 3), and the stance I think a scientist should take towards the whole business (Chapter 4).
Part II develops five core patterns across the research lifecycle, from literature (Chapter 5) to manuscript (Chapter 9), each in the same shape and each grounded in worked examples from operational hydrology and meteorology, before a capstone that composes them into multi-agent workflows (Chapter 10).
Part III is the centre of gravity — verification, provenance, governance and security — and it closes with an unvarnished gallery of failures.
Part IV puts the whole apparatus to work in two end-to-end case studies, and Part V is about adopting all of this in a real group, including the costs — money, institutional friction, and energy — that a responsible adoption has to price in.
I'm candid throughout that my examples come from one corner of the environmental sciences; the patterns were chosen, and written, to travel well beyond it.

---

### References (verify details before release)

- Brown, T. B., et al. (2020). Language models are few-shot learners. *Advances in Neural Information Processing Systems 33*. [verify]
- Dell'Acqua, F., et al. (2023). Navigating the jagged technological frontier: field experimental evidence of the effects of AI on knowledge worker productivity and quality. *Harvard Business School Working Paper 24-013*. [verify]
- Jimenez, C. E., Yang, J., Wettig, A., Yao, S., Pei, K., Press, O. and Narasimhan, K. (2023). SWE-bench: can language models resolve real-world GitHub issues? *ICLR 2024*. https://arxiv.org/abs/2310.06770
- Vaswani, A., et al. (2017). Attention is all you need. *Advances in Neural Information Processing Systems 30*. [verify]
