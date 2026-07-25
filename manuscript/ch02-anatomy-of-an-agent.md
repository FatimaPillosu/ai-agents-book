# Chapter 2 — Anatomy of an agent

> **Status:** draft r3 · voice v3.3 (`STYLE.md`) · sentence-per-line per `STYLE.md` §10 · figures as briefs per `FIGURES.md`.
> **Conventions:** vendor-neutral (outline §9) · **[AUTHOR: …]** marks lived material only the author can supply · **[verify]** marks real but unconfirmed details · citations drawn only from verified reports in `/research`. Nothing has been invented.

---

## 2.1 The instrument and its parts

The agent introduced in Chapter 1 as a single layer of the taxonomy, a model inside an agent inside a workflow, decomposes on inspection into four parts and no more: a model that proposes, a loop that sequences, tools that act, and a store that remembers.
This chapter opens the agent to show what each part does and, as importantly, where each one fails, a purpose that is diagnostic rather than architectural.
An agent understood only as a black box that answers prompts leaves no way to reason about why it produced a wrong answer, and nowhere to attach the verification that Part III insists on.
Every behaviour worth governing arises from how those four parts interact.
The model was the subject of the previous chapter, so it is treated here only as the component that supplies judgement at each step; the loop, the tools and the store are the additions that turn a function from text to text into something that can carry a bounded task from instruction through to a checked result.

This four-part decomposition is not idiosyncratic to the book, because the research literature that surveys these systems arrives at much the same joints.
One survey describes an agent in terms of a planning or decision loop, an action interface, and memory (Wang et al., 2023), so that the structure a practitioner needs in order to govern the thing matches the structure a survey needs in order to describe it.
A more recent survey points the same way, organising agentic systems along six dimensions (perception, brain, planning, action, tool use and collaboration) that map without strain onto the anatomy here, its collaboration dimension corresponding to the multi-agent territory of Chapter 10 (Arunkumar et al., 2026; a preprint, cited for its vocabulary rather than any capability claim).
Working practitioners have reached the same point from the other side and even named it: a strand of practitioner commentary calls the whole assembly around the model the harness, and holds that this harness, more than the model at its centre, decides what an agent can actually do (practitioner commentary; see the references).

The organising metaphor of this book is the instrument, and it holds right down to this level of detail.
An oscilloscope is a display, a timebase, an input stage and a trigger, and its trace is trusted by understanding what each stage contributes and how each one distorts.
An agent is no different in kind, only newer and far less characterised, so the account that follows describes each part as an instrument-part: what it is for, what it can be relied on to do, and the specific way it misleads.
A reader who holds that account can place every later pattern, and every failure in the Chapter 13 gallery, against a shared picture of the mechanism.
The four parts are introduced in the order they engage during a single step of work: the loop that governs the step (§2.2), the tools it may call (§2.3), the store it reads and writes (§2.4), then the composition of many such steps into an orchestrated process (§2.5), before the chapter closes on what all of this costs (§2.6).

## 2.2 The loop as control cycle

The one feature that separates an agent from a model that merely emits text is a control cycle: the system plans an action, carries it out, observes the result, and decides its next action in the light of what it observed.
This plan–act–observe loop is the agent's engine, and its steps are worth stating precisely, because loose description is where misplaced expectation begins.
In the plan step the model, given the goal and the state built up so far, proposes a single next action: a tool to call with specific arguments, or a judgement that the task is done.
In the act step that proposed action is carried out beyond the model, by machinery the model does not control: an interpreter runs the code, a database answers the query, a file is read.
In the observe step the result of that execution, a returned value, an error message, or a retrieved passage, is added to the state and passed back to the model, which plans again.
The cycle repeats until a stopping condition is met, and the character of the whole system depends far more on that loop than on any single response the model produces.
This interleaving of reasoning and acting is the pattern the research literature settled on early as the basis of essentially every current agent (Yao et al., 2023).

> **Definition — Plan–act–observe loop.** The cycle at the heart of every agent: the model proposes one action, machinery outside the model carries it out, the result returns, and the model uses that result to decide the next action. The cycle repeats until the work is complete or a stop condition halts it. It is the mechanism that turns a one-shot answer into a process able, under the right conditions, to correct itself.

The property that makes the loop valuable is that it turns a one-shot prediction into an error-correcting process.
A model that writes code with a bug in it is simply wrong.
An agent that writes the same code, runs it, reads the traceback and rewrites it can recover from that bug with no human intervention, provided the loop hands back evidence the model can act on.
That proviso is the whole discipline.
A loop corrects only the errors it can observe, so the quality of the observe step, whether the tool returns a real error or a silent wrong answer and whether the check is external or the model is left to grade its own output, decides whether iteration converges on a correct result or merely piles up confident wrongness.
The loop's characteristic failure follows directly from this.
Given a weak or absent observe step, the very mechanism that recovers from a traceback will instead elaborate a mistake across many steps, each one locally plausible, arriving at an output whose length and detail read as thoroughness whilst its foundation is an early error nobody checked: the plausible failure of Chapter 1, now compounded step by step (high confidence in the mechanism; how often it bites varies by task and model).
The original description of this pattern flagged exactly this hazard: reasoning errors propagate into the action loop, and the model will repeat a failing action if nothing intervenes (Yao et al., 2023).

**[AUTHOR: a short trace from your own operational work where an agent iterated to a confidently wrong result — and the observation that would have caught it — would anchor this better than the general claim.]**

**Figure 2.1 — The plan–act–observe loop.** *A figure brief follows `FIGURES.md`; render in the house style.*

```
FIGURE BRIEF
- id:            Figure 2.1
- title:         The plan–act–observe control cycle
- type:          architecture
- claim:         An agent's defining feature is a control cycle in which the model proposes an action, external machinery executes it, and the observed result feeds the next decision; the cycle, not any single response, is the engine.
- canvas:        16:9
- elements:      a central ring of three nodes read clockwise — "plan" (agent orange,
                 rounded square with loop glyph), "act" (tool green, wrench glyph),
                 "observe" (near-black); to the left of the ring a "specification / goal"
                 tag (blue) feeding in; to the right a "stop condition" diamond (gate
                 vermillion) with an exit to a "result" artefact (sky blue); a small
                 "state / memory" cylinder (sky blue) sitting under the ring, with
                 arrows showing observe writing to it and plan reading from it
- flow:          goal enters the ring at "plan"; plan → act → observe run clockwise;
                 observe writes to "state / memory" and returns to "plan"; from "plan"
                 a branch reaches the "stop condition" diamond, whose "done" exit leads
                 to "result" and whose "continue" exit re-enters the ring
- labels:        "specification / goal", "plan", "act", "observe", "state / memory",
                 "stop condition", "continue", "done", "result"
- annotations:   a light callout on the observe→state arrow reading "external result,
                 not self-assessment"
- caption:       Figure 2.1 — The plan–act–observe loop. The model proposes an action, external machinery executes it, and the observed result is written to state and fed back for the next decision; the loop corrects only the errors its observe step can actually see.
- alt-text:      A circular diagram of three nodes (plan, act and observe) read clockwise. A goal enters at plan; observe writes to a state-and-memory cylinder beneath the ring and returns to plan. A branch from plan reaches a stop-condition diamond whose done exit produces a result artefact and whose continue exit re-enters the ring. A callout on the observe step notes that the returned result is external, not the model's self-assessment.
- generator prompt: A flat vector architecture diagram on an off-white background. Three
                 rounded nodes form a ring, arranged clockwise and joined by single-weight
                 arrows: an orange node labelled "plan" at top, a green node with a small
                 wrench glyph labelled "act" at lower right, and a near-black node labelled
                 "observe" at lower left. A blue tag labelled "specification / goal" at the
                 far left connects into the "plan" node. Beneath the ring sits a sky-blue
                 cylinder labelled "state / memory"; an arrow runs from "observe" down into
                 the cylinder and another from the cylinder up into "plan". From "plan" a
                 branch reaches a vermillion diamond labelled "stop condition" at the right,
                 with two exits: "done" leading to a sky-blue document icon labelled
                 "result", and "continue" curving back into the ring. A small callout on the
                 observe-to-cylinder arrow reads "external result, not self-assessment".
                 Minimal text, generous spacing, single-weight lines.
```

## 2.3 Tools as delegated weakness

Tools are the means by which an agent hands its own weaknesses to machinery that does not share them, and the framing of delegation of weakness, rather than extension of strength, is the one that predicts which tools actually matter.
A language model is an unreliable calculator, an unreliable retriever of specific facts, and an unreliable executor of multi-step arithmetic done in prose, because none of those is what next-token prediction is good at.
Each of those weaknesses, however, already has a mature, deterministic implementation, and a tool is simply a declared interface through which the model can call that implementation and receive its result.
The point was made early and cleanly in the research literature: a model can be taught when to reach for a calculator, a search index or a lookup, precisely because it is bad at the arithmetic and factual recall that trivial specialised systems perform perfectly (Schick et al., 2023).
The canonical cases are the model's canonical weaknesses turned inside out.
Arithmetic and data manipulation go to a code interpreter that computes them exactly.
Retrieval of specific facts goes to a database or a search index that returns them verbatim rather than reconstructing them from parameters.
Access to current or private data, a river-gauge series, a reanalysis field, or a repository's files, goes to a tool that reads the actual source rather than the model's stale recollection of it.
The design principle that falls out of this is to give the model, as tools, precisely the operations it performs worst and ordinary software performs best, and to resist the temptation to have it do in prose what a three-line function would do exactly.

A tool call has a fixed anatomy that recurs throughout the book, and it is worth naming once.
There is a declaration the model can read (the tool's name, purpose and argument schema), an invocation the model emits (a structured call naming the tool and its arguments), an execution outside the model, and a returned result added to state.
Each part is a control point.
The declaration bounds what the model may attempt, which is why least-privilege tool access is a governance lever and not merely a security nicety (Chapter 12).
The returned result is the observe step of §2.2, which is why a tool that fails silently, handing back a plausible wrong answer instead of an error, is more dangerous than one that is simply missing, because it defeats the loop's only means of correction.
The limitation to hold beside the promise is that a tool delegates the model's weakness at execution but not at selection.
The interpreter computes correctly, but the model still chose which computation to run and with what arguments, and a correct tool invoked on the wrong quantity (the right formula on an unconverted unit, the right query against the wrong station) returns an exact answer to the wrong question.
Tools narrow the class of errors an agent makes; they do not abolish it, and the errors that remain are exactly the ones verification has to target.

**Figure 2.2 — Anatomy of a tool call.** *A figure brief follows `FIGURES.md`; render in the house style.*

```
FIGURE BRIEF
- id:            Figure 2.2
- title:         One tool call, four parts
- type:          sequence
- claim:         A tool call has a fixed four-part anatomy (declaration, invocation, execution, returned result), and each part is a distinct control point.
- canvas:        16:9
- elements:      two vertical actor lanes read top-to-bottom — "agent (model)" (orange)
                 and "tool / interpreter" (green); four numbered steps crossing between
                 them; a small "state / memory" cylinder (sky blue) at the foot receiving
                 the returned result
- flow:          top-to-bottom, four numbered steps — (1) declaration read by the agent
                 (a dashed inbound arrow from a "tool declaration" tag), (2) invocation
                 from agent to tool, (3) execution shown within the tool lane, (4) returned
                 result from tool back to agent and written to "state / memory"
- labels:        "agent (model)", "tool / interpreter", "1 declaration",
                 "2 invocation", "3 execution", "4 returned result", "state / memory"
- annotations:   a vermillion callout beside step 4 reading "silent wrong answer defeats
                 the loop" pointing at the returned-result arrow
- caption:       Figure 2.2 — The four parts of a tool call. The declaration bounds what the model may attempt; the invocation is the model's choice of operation and arguments; execution happens outside the model; the returned result becomes the loop's observation, which is why a silent wrong answer is more dangerous than an error.
- alt-text:      A two-lane sequence diagram with an agent lane and a tool lane, read top to bottom. Step one: the agent reads a tool declaration. Step two: the agent sends an invocation to the tool. Step three: the tool executes. Step four: the tool returns a result to the agent, which is also written to a state-and-memory cylinder. A callout by step four warns that a silent wrong answer defeats the loop's ability to correct.
- generator prompt: A flat vector sequence diagram on an off-white background with two
                 vertical lanes, read top to bottom. The left lane header is an orange
                 rounded square labelled "agent (model)"; the right lane header is a green
                 wrench glyph labelled "tool / interpreter". Four numbered horizontal
                 arrows cross between the lanes: "1 declaration" as a dashed arrow into the
                 agent lane from a small tag labelled "tool declaration"; "2 invocation" from
                 agent to tool; "3 execution" shown as a short self-loop within the tool
                 lane; "4 returned result" from tool back to agent. From step 4 a further
                 arrow drops to a sky-blue cylinder labelled "state / memory" at the bottom.
                 A vermillion callout beside step 4 reads "silent wrong answer defeats the
                 loop". Minimal text, single-weight lines, generous spacing.
```

## 2.4 Context and memory as a finite store

Context and memory are the agent's working store, and the property that governs their use is that the store is finite, ordered and lossy, in ways that must be designed around rather than wished away.
The immediate working store is the model's context window: the bounded span of text (instructions, retrieved material, prior tool results, the running transcript) that the model can attend to when it plans its next step.
Everything the agent knows at a given moment is either in that window or it is absent.
The window has a fixed capacity that, although it has grown by more than an order of magnitude across the capability period described in Chapter 1 [verify], remains finite, and every tool result the loop appends eats into it.
The vocabulary the research literature uses here is worth borrowing, because it separates the volatile working memory of a single run from the longer-term stores an agent writes to and reads back, that is, episodic records of what happened and semantic notes of what was learned (Sumers et al., 2023), and the distinction between the two is exactly where a scientific workflow either keeps its provenance or loses it.

Three consequences follow, and each one has caught practitioners out.
First, a long-running loop fills its own context: every observed result takes up space, so a task of many steps drifts towards the window's limit, at which point earlier material, the original specification or an early constraint, has to be summarised, dropped or externalised, and a constraint that has fallen out of the window is a constraint the agent no longer honours.
Second, position within the window matters: material at the start and the end of a long context is attended to more reliably than material buried in the middle, so merely fitting information into the window does not guarantee it is used (moderate confidence; the effect is documented but its magnitude varies by model).
Third, the window is volatile, holding only within a single run, so anything that must persist across runs needs an explicit, external memory: notes written to a file, records in a database, or a specification kept under version control.
This distinction between volatile context and durable memory is not incidental housekeeping.
It is where an agent's provenance is either captured or lost, and Chapter 12 treats the durable store as the substrate on which audit trails, assumption registries and reviewer-coverage records are all built.

The design implication for scientific work is to treat context as a scarce, curated resource rather than a bucket into which everything is poured.
The reliable pattern is to place the specification and the acceptance criteria where they will actually be attended to, to retrieve into the window only the material a given step needs, and to externalise to durable memory anything that has to survive the run or serve as evidence afterwards.
The limitation to record is that this curation is itself a design task with no sensible default.
An agent handed a large context and no discipline about what enters it will degrade quietly, making worse decisions with no error to mark the moment its working store stopped serving it.

**Figure 2.3 — Context and memory.** *A figure brief follows `FIGURES.md`; render in the house style.*

```
FIGURE BRIEF
- id:            Figure 2.3
- title:         The finite working store and the durable store
- type:          architecture
- claim:         An agent holds a finite, volatile context window within a run and a durable external memory across runs; the two are distinct, and provenance depends on the second.
- canvas:        16:9
- elements:      a large bounded rectangle "context window" (sky blue border) with a
                 fixed edge marked "capacity limit" (grey); inside it, stacked bands
                 labelled "specification", "retrieved material", "tool results",
                 "running transcript", with the top and bottom bands lightly highlighted
                 (yellow) and the middle bands greyed; to the right, separated by a clear
                 gap, a "durable memory" cylinder (sky blue) holding "files · records ·
                 version control"; a two-way arrow between the window and the cylinder
                 labelled "externalise / retrieve"
- flow:          left block is within-run and volatile; right cylinder is across-run and
                 durable; the labelled arrow connects them
- labels:        "context window", "capacity limit", "specification",
                 "retrieved material", "tool results", "running transcript",
                 "durable memory", "files · records · version control",
                 "externalise / retrieve", "within a run", "across runs"
- annotations:   a callout on the greyed middle bands reading "attended to less
                 reliably"; a callout on the cylinder reading "where provenance lives"
- caption:       Figure 2.3 — The working store and the durable store. The context window is finite and volatile, its middle attended to less reliably than its edges; anything that must survive the run or serve as later evidence has to be externalised to a durable memory, which is where provenance lives.
- alt-text:      On the left, a bounded rectangle labelled context window with a marked capacity limit contains stacked bands (specification, retrieved material, tool results and running transcript) with the top and bottom bands highlighted and the middle greyed and marked "attended to less reliably". On the right, separated by a gap, a cylinder labelled durable memory holds files, records and version control, marked "where provenance lives". A two-way arrow labelled externalise and retrieve connects the two; the left is within a run, the right across runs.
- generator prompt: A flat vector architecture diagram on an off-white background. On the
                 left, a large sky-blue-bordered rectangle labelled "context window" has a
                 thick grey right edge labelled "capacity limit". Inside, four horizontal
                 bands stack top to bottom, labelled "specification", "retrieved material",
                 "tool results", "running transcript"; the top and bottom bands have a pale
                 yellow fill, the two middle bands are greyed with a small callout reading
                 "attended to less reliably". Below the rectangle a small label reads
                 "within a run". To the right, across a clear gap, a sky-blue cylinder is
                 labelled "durable memory" with sub-text "files · records · version control"
                 and a callout "where provenance lives"; below it a label reads "across
                 runs". A two-way single-weight arrow between the rectangle and the cylinder
                 is labelled "externalise / retrieve". Minimal text, generous spacing.
```

## 2.5 Orchestration as composition

Orchestration is the composition of individual agent steps into a larger process, and the question it answers is not how one agent thinks but how the arrangement of steps, agents and gates makes the whole more reliable than any part.
A single plan–act–observe loop is the atom of §2.2; orchestration is the chemistry, and it takes a small number of recognisable forms.

> **Definition — Orchestration.** The arrangement of several agent steps, together with the checks and human decisions between them, into one larger workflow. Where a single agent is one worker, orchestration is the division of labour: which step does what, in what order, and which step checks which. It is the layer at which a workflow's reliability is engineered.

The simplest form is a sequence: a chain in which one step's output is the next step's input, which suits a task that decomposes into stages with a fixed order, such as acquire, then clean, then summarise.
Beyond sequence lies delegation, in which a coordinating step hands a bounded sub-task to a separate agent with its own loop, tools and fresh context.
Delegation is valuable precisely because the sub-agent's context is clean: a large retrieval or a noisy exploration can be confined to it, and only its distilled result returned to the coordinator, which keeps the coordinator's finite store (§2.4) uncluttered.

> **Definition — Sub-agent.** A second agent to which a coordinating agent hands a self-contained piece of work, with its own tools and its own clean context. It performs the bulky or noisy part in isolation and returns only the distilled result, so that the coordinator never has to hold the intermediate material in view.

A third form is a distinct reviewer step whose whole job is to check another step's output before it goes any further, and this form matters disproportionately in scientific work, because it is where the external verification of §2.2 is given a structural home.
A reviewer agent working from a separate context, or a deterministic gate applying a rule, interrupts the flow of confident output with a check the producing agent could never mark against itself.
These forms are not the book's invention; they are the composable patterns practitioners in the field converged on and documented, such as chaining, routing, parallel work, a coordinator with workers, and evaluator-and-improver loops, under a governing recommendation this book shares: reach for the simplest arrangement that works and add orchestration only when the task visibly needs it (Anthropic, 2024).
That recommendation is the design judgement orchestration really demands: knowing when composition adds robustness and when it adds only cost and noise.
The honest answer is that more agents are not reliably better.
Each added step spends tokens, adds latency and brings its own failure surface, so composition earns its place only where a step genuinely reduces error or confines it, not where it merely multiplies activity.

This chapter deliberately stops at the anatomy of composition and leaves the multi-agent patterns themselves for later.
Chapter 10 is the capstone that composes the book's core patterns into rosters of agents, reviewers and human gates, and Chapter 15 applies that composition end to end.
The point to carry forward is structural: orchestration is where the workflow layer of Chapter 1's taxonomy is actually built, the layer that adds specification, verification and accountability to a bare agent, and it is built out of the same four parts described above, arranged so that the observe steps and the gates fall exactly where a wrong answer would otherwise escape.
The limitation is that orchestration cannot rescue an unspecified task.
Composing steps around a goal that was never written down clearly (Chapter 3) distributes the ambiguity rather than resolving it, and a well-orchestrated workflow executing a vague specification fails more expensively than a single agent ever could.

## 2.6 A plain cost model

Every agent action has a cost, and reasoning about those costs plainly, rather than assuming that falling model prices make the question moot, is part of operating the instrument responsibly.
The costs an agent incurs fall into three kinds, and they behave quite differently.
The first is token cost.

> **Definition — Token.** The unit in which these models read and write, approximately a short fragment of a word. Text is billed and measured by the token, so the length of everything an agent reads and produces, including its own steadily growing transcript, is precisely what the paid case charges for.

Models are billed, in the paid case, by the quantity of text read and generated, so a loop that appends every tool result to a growing context pays for that context at every later step, and a long orchestration re-reads its accumulated state again and again, which means cost grows faster than the step count alone would suggest.
The second is tool-and-compute cost: the executions the agent triggers (a query against a large archive, a regridding job, or a model run invoked as a tool) carry their own expense in machine time and, for an environmental readership, in energy and the carbon that comes with it, a cost that is easy to overlook because it never appears on the model bill and that Chapter 16 treats head-on rather than as a footnote.
The third is latency: the wall-clock time a loop takes, which is a real cost in operational settings where a forecast bulletin has a deadline.
An agent that reaches a correct answer after the window in which it was useful has failed operationally, whatever its accuracy.

The observation that reorganises all three, and that recurs throughout the book, is that in a well-run scientific workflow the dominant cost is not generation but verification.
Producing a draft, a script or a synthesis is comparatively cheap.
Establishing that it is correct (running the tests, checking the citations against sources, validating the extraction against a schema, having a reviewer step or a human confirm an interpretation) is where the effort and the expense concentrate, and it is effort that does not fall as model prices fall, because it is external to the model by design (§2.2).
This inverts the naive economic case for agents.
The saving was never that the science becomes cheap to verify; it is that the production which precedes verification becomes cheap enough that more of the budget can be spent verifying well, which is exactly where a scientific workflow should want to spend it.

The limitation to state honestly is that these three costs trade against one another, and against reliability, in ways specific to a task: a cheaper model may need more loop iterations, a faster answer may skip a check, and there is no general optimum.
What does generalise is the accounting discipline of naming all three costs and the verification burden explicitly, so that a workflow is chosen with its true price visible; the concrete figures that would populate this model are volatile, belong in the companion repository, and are developed against a realistic on-ramp in Chapter 16.

**[AUTHOR: an approximate cost breakdown from one of your operational workflows — the split between production and verification effort — would make this section concrete; keep any per-token or per-run figures in the repository, not in print.]**

---

*This chapter has taken the agent apart into a loop, tools, a finite store and their composition, and priced the result.*
*The next chapter turns to the human side of the same mechanism: how to specify a task so that this apparatus can execute it and a scientist can audit it afterwards, the skill that most failures trace back to.*

---

### References (verify details before release)

- Anthropic (2024). Building effective agents. *Anthropic engineering blog.* https://www.anthropic.com/engineering/building-effective-agents
- Arunkumar, V., Gangadharan, G. R. and Buyya, R. (2026). Agentic artificial intelligence (AI): architectures, taxonomies, and evaluation of large language model agents. *arXiv preprint.* https://arxiv.org/abs/2601.12560
- Jones, N. B. (2026). "Don't build more AI agents until you watch this." Video, @natebjones, 17 June 2026. https://www.youtube.com/watch?v=BOXK2XFLA-E (practitioner commentary; concepts cited as corroboration, not evidence)
- Schick, T., et al. (2023). Toolformer: language models can teach themselves to use tools. *NeurIPS 2023.* https://arxiv.org/abs/2302.04761
- Sumers, T. R., Yao, S., Narasimhan, K. and Griffiths, T. L. (2023). Cognitive architectures for language agents. *Transactions on Machine Learning Research.* https://arxiv.org/abs/2309.02427
- Wang, L., et al. (2023). A survey on large language model based autonomous agents. *arXiv preprint.* https://arxiv.org/abs/2308.11432
- Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K. and Cao, Y. (2023). ReAct: synergizing reasoning and acting in language models. *ICLR 2023.* https://arxiv.org/abs/2210.03629
```
