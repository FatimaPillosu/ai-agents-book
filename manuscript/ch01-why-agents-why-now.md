# Chapter 1 — Why agents, why now

> **Status:** draft · figures specified as briefs per `FIGURES.md`. Chapter lengths are indicative guidance, not fixed allocations.
> **Conventions:** vendor-neutral per outline §9. Passages needing the author's lived material or number verification are tagged **[AUTHOR: …]** or **[verify]**. The three references cited are real; verify bibliographic details before release. No anecdotes or statistics have been invented.

---

## 1.1 The problem this book addresses

The central operational fact of contemporary environmental science is an asymmetry between the volume of material demanding a scientist's attention and the attention available to give it. Over the past two decades the growth on the supply side has been relentless: satellite programmes now deliver observations at rates measured in terabytes per day, coupled model intercomparison archives run to tens of petabytes, and operational forecasting centres accumulate output faster than any individual could inspect it **[AUTHOR: verify one or two current figures — e.g. Copernicus daily volumes, CMIP6 archive size — and cite]**. The obligations attached to that material have grown in proportion, because every stream must be quality-controlled, reconciled with its neighbours, reprocessed when versions change, and reported to funders and partners in formats that are themselves revised yearly. What has not grown is the number of working hours possessed by the people responsible. The consequence, observable across the environmental sciences though seldom measured with precision, is that highly trained scientists spend a substantial fraction of their week on transformation, checking and formatting: work that is necessary and skilled, and that is nevertheless not the science they were trained to do. **[AUTHOR: replace or augment with a concrete morning from operational flood forecasting — the specific reconciliation of ensemble output, gauge records and a bulletin deadline will land harder than any general description.]**

Against this background, the appearance of software systems that can act — read a file, execute code, inspect the result and decide what to do next — deserves serious rather than reflexive attention. The claims made on behalf of such systems are expansive, the commentary surrounding them is polarised, and neither condition is unusual for a technology at this stage of its diffusion. The position developed across this book is deliberately narrower than either camp would prefer: these systems are instruments, in the full meaning environmental scientists attach to the word — powerful, fallible, and fit for serious work only once calibrated, verified and operated under governance appropriate to the decisions that depend on them. The case for engaging with them now, rather than waiting for the field to settle, rests on a small number of specific and datable changes in capability and in access, which this chapter sets out together with the vocabulary the rest of the book depends upon and an honest statement of where present capability ends.

## 1.2 What changed, and when

The developments that made agents possible form a short lineage in which the decisive changes concerned the interface to computation as much as raw capability. The transformer architecture (Vaswani et al., 2017) made it computationally tractable to train language models on very large text corpora, and scale then produced a property that had not been designed for: in-context learning (Brown et al., 2020), the capacity of a model to take on a new task from instructions and a handful of examples alone, without retraining. The significance of that property for working scientists lies less in the benchmark results it generated than in what it did to the interface, because from that point onward a task could be specified in ordinary written language — the medium in which scientists already describe their methods. The public arrival of instruction-tuned conversational systems in late 2022 made the shift visible far beyond the research community and changed institutional perception of the field within months. Everything to that point, however, shared a limitation that mattered more for science than for most other domains: the systems produced text, and text alone cannot run a quality-control pass, regrid a forecast field, or execute a test suite.

What separates the present period from that earlier one is the arrival of structured action: the reliable emission of machine-readable calls to defined tools, combined with the capacity to read each returned result and select the next step in the light of it. From roughly 2023, models could be depended upon to produce syntactically valid arguments to a declared function rather than a prose description of what such a call might look like, and this apparently modest change closed the loop between linguistic instruction and actual computation. Its consequence for scientific work is considerable, because it allows the model's own weaknesses to be delegated to tools that do not share them: arithmetic goes to the interpreter, retrieval goes to the database, and the model's role contracts to the planning and interpretation that sit between. The capabilities that accumulated around this core — persistent context long enough to hold a codebase or document set in view (2023–24), code generation and repair evaluated against test suites (2024–25), operation of ordinary computer interfaces, and standardised protocols for connecting models to tools and data (2024–25) — are individually incremental, and none of them alone constitutes an agent. Composed, they yield a system with a model, tools, a loop and state, capable of carrying a bounded task from instruction to verified result. The trajectory is measurable where public benchmarks exist: on the most widely cited software-engineering benchmark, autonomous resolution rates rose from single figures in 2023 to above 70% by late 2025 **[AUTHOR: verify the current figure; name the benchmark in the repository and keep the print claim coarse]**, although the transfer from benchmark performance to performance inside real workflows is imperfect, for reasons taken up in §1.4 and measured properly in Chapter 11.

A further component of the answer to "why now", less often remarked upon than capability, is economic. The cost of using capable models has fallen by orders of magnitude over the same period in which their capability has risen **[AUTHOR: verify a defensible figure — per-token price decline at equivalent capability tiers, 2023–26 — for the repository]**, and openly released models with permissive licences have reached a level of competence sufficient for many bounded scientific tasks. The implication is that agentic methods are no longer the preserve of well-resourced institutions: a group with modest hardware and no recurring budget can, with care, assemble workflows of genuine operational value — a constraint this book treats as a design input rather than an afterthought, and returns to at length in its closing case studies. The qualification that belongs beside this observation is that falling model costs do not make agentic work cheap, because the expenditure migrates rather than disappears: into engineering time, into evaluation, and above all into verification, which is where a well-run scientific workflow should expect to spend most of what it saves.

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

Because the terminology surrounding these systems is used loosely in commercial and academic writing alike, and because misplaced trust tends to begin with conflated terms, this book distinguishes three of them and holds the distinctions throughout. A **large language model** is a function from text to text — increasingly from and to other media besides — with no memory between calls, no goals of its own, and no means of acting on anything beyond its output. An **AI agent** is a system constructed around such a model: the model together with tools it is permitted to call, a loop that returns each tool's result for the next decision, and state that persists across steps, the whole directed at a goal with discretion over the intermediate steps taken to reach it. An **agentic workflow** is a designed process in which agent steps are embedded among defined inputs, acceptance criteria, verification gates and human decision points, so that the agent's discretion operates inside boundaries specified before it began. Set out this way, the three terms place autonomy on a spectrum rather than presenting it as a property a system either has or lacks: at one end sits a single agent step inside an otherwise fixed pipeline, at the other an open-ended system pursuing a goal without checkpoints, and where a given system sits between these poles is a design decision made by its builders rather than a fact about the underlying technology.

The distinction underwrites the central position of this book, which is that scientists should build agentic workflows rather than deploy autonomous agents, and the reasoning behind that position is not novel caution but the ordinary discipline of instrumentation applied to a new instrument class. No hydrologist trusts a sensor in the colloquial sense of the word: the sensor is calibrated before deployment, its drift is characterised, its output is quality-controlled within a network designed for the purpose, and its readings are interpreted by a person who remains accountable for the interpretation. Each element of that discipline has a counterpart in the chapters that follow — specification plays the role of deployment design (Chapter 3), gates and independent review play the role of quality control (Chapters 10 and 12), and evaluation plays the role of calibration (Chapter 11). The analogy has a limit that is worth stating at the outset, because it motivates a full third of the book: physical sensors fail in modes that are broadly characterisable in advance, whereas language systems fail in ways that imitate competence, producing outputs whose fluency is uncorrelated with their correctness. That property — plausible failure — is the reason verification receives its own part of this book rather than a section, and the reason Chapter 13 is a gallery of failures rather than a footnote to the successes.

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

Any honest account of present capability has to begin from the observation that it is uneven in ways that defeat intuition, a pattern that early field studies of AI-assisted knowledge work described as a jagged frontier (Dell'Acqua et al., 2023) and that holds with particular force in scientific settings. The unevenness has a comprehensible origin: these systems acquire competence from the distribution of their training material, so their reliability on a task tracks how densely that task and its variants are represented in what they learned from, rather than how difficult the task appears to a person. Translating a numerical routine between programming languages, a task abundantly represented in public code, is routinely completed correctly with tests passing; a unit conversion embedded mid-sentence in prose, sparsely and inconsistently represented, is mishandled often enough that no workflow in this book leaves one unchecked. The practical implication is uncomfortable but clarifying: intuition about which tasks are safe to delegate is close to worthless, and must be replaced by testing on the actual task, with the actual data, at the actual scale intended.

A more useful selector than perceived difficulty is the asymmetry between the cost of producing an output and the cost of verifying it. Where verification is cheap and mechanical — code judged by a test suite, extraction validated against a schema, a format translation confirmed by checksum and round trip — an imperfect generator is operationally safe, because its errors are caught at low cost and its successes arrive at volume; and it is exactly such tasks that populate the reliable side of today's frontier: code generation and repair, translation between data formats, structured extraction from documents, first-pass literature triage, and draft documentation. Where verification is expensive, subjective or slow — a claim at the research frontier, an interpretive synthesis, an anomaly whose significance depends on context the system does not hold — fluent output remains hazardous however capable the model, and such tasks stay on the far side of the frontier regardless of benchmark progress. Two further properties belong in any statement of the boundary. Models remain poor judges of their own correctness, which is why every verification mechanism in this book is external to the system being verified (high confidence in the pattern; magnitudes vary by model and task); and multi-step quantitative reasoning conducted in prose, rather than delegated to computation, fails often enough that delegation to tools should be treated as a rule rather than a preference. **[AUTHOR: a short account of a failure you personally caught — silent, plausible and wrong — would anchor this section better than any general claim.]**

Beyond the unreliable lies a third category consisting not of gaps in capability but of errors of category, and it is the one this book holds constant while everything else moves: accountability, scientific judgement and authorship. An agent cannot be responsible for a flood warning, cannot decide that an anomaly is meaningful rather than instrumental, and cannot stand as an author of the paper that results; and these limits do not soften as models improve, because responsibility is not a capability and does not transfer to instruments, however good the instruments become. The boundary drawn in this section carries one caveat that honesty requires: it is drawn at the time of writing, it will move — mostly outward, unevenly, and faster than publishing cycles — and a printed chapter is the wrong place to track it. The division of labour adopted here is therefore deliberate: the print states the position and the reasoning, the companion repository tracks the movement, and the verification machinery of Part III is what makes it tolerable to work with an instrument whose specification will not stand still.

## 1.5 The shape of what follows

The remainder of the book proceeds from foundations through practice to trust, and then outward to adoption. Part I completes the groundwork with the anatomy of an agent (Chapter 2), the craft of specifying work for one (Chapter 3), and the stance a scientist should take towards the whole enterprise (Chapter 4). Part II develops five core patterns spanning the research lifecycle from literature (Chapter 5) to manuscript (Chapter 9), each presented in an identical structure and grounded in worked examples from operational hydrology and meteorology, then closes with a capstone that composes them into multi-agent workflows (Chapter 10). Part III is the book's centre of gravity, covering verification, provenance, governance and security, and closing with an unvarnished gallery of failures. Part IV applies the whole apparatus in two end-to-end case studies, and Part V addresses adoption within a working group, including the costs — financial, institutional and environmental — that a responsible adoption has to price in. The examples throughout are candid about their origin in one corner of the environmental sciences; the patterns are written, and were chosen, to transfer beyond it.

---

### References (verify details before release)

- Brown, T. B., et al. (2020). Language models are few-shot learners. *Advances in Neural Information Processing Systems 33*.
- Dell'Acqua, F., et al. (2023). Navigating the jagged technological frontier: field experimental evidence of the effects of AI on knowledge worker productivity and quality. *Harvard Business School Working Paper 24-013*.
- Vaswani, A., et al. (2017). Attention is all you need. *Advances in Neural Information Processing Systems 30*.
