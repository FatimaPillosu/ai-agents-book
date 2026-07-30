# Chapter 2 — Anatomy of an agent

> **Status:** draft r4 · voice v5.0 (`STYLE.md` §1) · sentence-per-line per `STYLE.md` §10 · figures as briefs per `FIGURES.md`.
> **Conventions:** vendor-neutral (outline §9) · **[AUTHOR: …]** marks lived material only the author can supply · **[verify]** marks real but unconfirmed details · citations drawn only from verified reports in `/research`. Nothing has been invented.

---

## 2.1 The instrument and its parts

Take an agent apart and you find four things, and no more: a model that proposes, a loop that sequences, tools that act, and a store that remembers.

This chapter opens the agent up to show what each part does and, just as importantly, where each one fails.
The purpose is diagnostic rather than architectural.
If you treat an agent as a box that answers prompts, you have no way of reasoning about why it produced a wrong answer, and nowhere to attach the verification Part III insists on.
Every behaviour worth governing comes out of how those four parts interact.
The model was the subject of the last chapter, so it appears here only as the part that supplies judgement at each step.
The loop, the tools and the store are the additions that turn a function from text to text into something that can carry a bounded task from instruction through to a checked result.

This four-part split is not idiosyncratic to the book.
The research literature that surveys these systems cuts them in much the same places.
One survey describes an agent as a planning or decision loop, an action interface, and memory (Wang et al., 2023), so the structure you need in order to govern the thing matches the structure a survey needs in order to describe it.
A more recent survey points the same way, organising agentic systems along six dimensions (perception, brain, planning, action, tool use and collaboration) that map onto this anatomy without strain, its collaboration dimension matching the multi-agent material of Chapter 10 (Arunkumar et al., 2026; a preprint, cited for its vocabulary rather than for any capability claim).
Working practitioners got to the same place from the other direction and even named it: one strand of practitioner commentary calls the whole assembly around the model the harness, and argues that the harness, more than the model at its centre, decides what an agent can actually do (practitioner commentary; see the references).

The comparison this book keeps returning to is the scientific instrument, and it holds right down to this level of detail.
An oscilloscope is a display, a timebase, an input stage and a trigger, and you trust its trace by understanding what each stage contributes and how each one distorts.
An agent is no different in kind, only newer and far less characterised.
So the account that follows describes each part the way you would describe a part of an instrument: what it is for, what it can be relied on to do, and the specific way it misleads you.
Hold that account and you can place every later pattern, and every failure in the Chapter 13 gallery, against a shared picture of the mechanism.
The four parts come in the order they engage during a single step of work: the loop that governs the step (§2.2), the tools it may call (§2.3), the store it reads and writes (§2.4), then how many such steps compose into an orchestrated process (§2.5), before the chapter closes on what all of this costs (§2.6).

## 2.2 The loop as control cycle

One feature separates an agent from a model that merely emits text: a control cycle.
The system plans an action, carries it out, observes the result, and decides its next action in the light of what it observed.

This plan–act–observe loop is what makes an agent an agent, and its steps are worth stating precisely, because loose description is where misplaced expectation starts.
In the plan step the model, given the goal and the state built up so far, proposes one next action: a tool to call with specific arguments, or a judgement that the task is done.
In the act step that action is carried out beyond the model, by machinery the model does not control: an interpreter runs the code, a database answers the query, a file is read.
In the observe step the result of that execution, a returned value, an error message, or a retrieved passage, is added to the state and passed back to the model, which plans again.
The cycle repeats until a stopping condition is met, and the character of the whole system depends far more on that loop than on any single response the model produces.
Interleaving reasoning and acting this way is the pattern the research literature settled on early, and it underpins essentially every current agent (Yao et al., 2023).

> **Definition — Plan–act–observe loop.** The cycle at the heart of every agent: the model proposes one action, machinery outside the model carries it out, the result comes back, and the model uses that result to decide the next action. The cycle repeats until the work is done or a stop condition halts it. It is what turns a one-shot answer into a process that can, under the right conditions, correct itself.

What makes the loop valuable is that it turns a one-shot prediction into an error-correcting process.
A model that writes code with a bug in it is simply wrong.
An agent that writes the same code, runs it, reads the traceback and rewrites it can recover from that bug with nobody intervening, as long as the loop hands back evidence the model can act on.
That proviso is the whole discipline.
A loop corrects only the errors it can observe.
So the quality of the observe step decides everything: whether the tool returns a real error or a silent wrong answer, and whether the check is external or the model is left to grade its own work, is what separates iteration that converges on a correct result from iteration that just piles up confident wrongness.
The loop's characteristic failure follows directly.
Give it a weak or absent observe step, and the very mechanism that recovers from a traceback will instead elaborate a mistake across many steps, each one locally plausible, arriving at an output whose length and detail read as thoroughness while its foundation is an early error nobody checked.
That is the plausible failure of Chapter 1, now compounded step by step (high confidence in the mechanism; how often it happens varies by task and model).
The original description of this pattern flagged exactly this hazard: reasoning errors propagate into the action loop, and the model will repeat a failing action if nothing intervenes (Yao et al., 2023).

**[AUTHOR: a short trace from your own operational work where an agent iterated to a confidently wrong result — and the observation that would have caught it — would anchor this better than the general claim.]**

**Figure 2.1 — The plan–act–observe loop.**

![A circular diagram of three nodes read clockwise: plan, act and observe. A goal enters at plan, annotated as written before the loop starts. Plan is annotated "the model proposes one action". Act is annotated "machinery outside the model carries it out", observe "the result comes back, whether it is an answer or an error". Observe writes down to a state and memory cylinder, annotated "what the next step gets to see", and returns to plan. A branch from plan reaches a stop-condition diamond whose done exit produces a result and whose continue exit re-enters the ring. A vermillion callout on the observe step warns that the loop can only correct errors this step can actually see, and that a silent wrong answer is invisible to it.](../figures/figure-2-1.svg)

*Figure 2.1 — The cycle that makes an agent an agent. The model proposes one action, something outside the model carries it out, and the result comes back to inform the next decision. Everything depends on the observe step: a loop corrects only the errors it can see, so a tool that fails silently defeats the whole mechanism. (Rendered as `figures/figure-2-1.svg` from the brief below, per `FIGURES.md`.)*

```
FIGURE BRIEF
- id:            Figure 2.1
- title:         The plan-act-observe loop
- type:          architecture
- claim:         An agent's defining feature is a control cycle in which the model proposes an action, external machinery executes it, and the observed result feeds the next decision; the cycle, not any single response, is the engine.
- standfirst:    The loop corrects only the errors its observe step can actually see.
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
- annotations:   on the goal tag, "written before the loop starts"; on plan, "the model
                 proposes one action"; on act, "machinery outside the model carries it
                 out"; on observe, "the result comes back, whether it is an answer or an
                 error"; on the observe-to-state arrow, "what the next step gets to see";
                 on the stop condition, "succeed and halt, or fail and hand back"; a
                 vermillion callout beside observe, "a loop corrects only what this step
                 can see — a silent wrong answer is invisible here"
- caption:       Figure 2.1 — The cycle that makes an agent an agent. The model proposes one action, something outside the model carries it out, and the result comes back to inform the next decision. Everything depends on the observe step: a loop corrects only the errors it can see, so a tool that fails silently defeats the whole mechanism.
- alt-text:      A circular diagram of three nodes read clockwise: plan, act and observe. A goal enters at plan, annotated as written before the loop starts. Plan is annotated "the model proposes one action". Act is annotated "machinery outside the model carries it out", observe "the result comes back, whether it is an answer or an error". Observe writes down to a state and memory cylinder, annotated "what the next step gets to see", and returns to plan. A branch from plan reaches a stop-condition diamond whose done exit produces a result and whose continue exit re-enters the ring. A vermillion callout on the observe step warns that the loop can only correct errors this step can actually see, and that a silent wrong answer is invisible to it.
- infographic description: A flat vector architecture diagram on an off-white background,
                 16:9. Title top-left in the largest size: "The plan-act-observe loop".
                 Beneath it a standfirst: "The loop corrects only the errors its observe
                 step can actually see." Three rounded nodes form a ring in the centre,
                 arranged clockwise and joined by single-weight arrows: an orange node
                 "plan" at the top, annotated "the model proposes one action"; a green node
                 with a small wrench glyph "act" at lower right, annotated "machinery
                 outside the model carries it out"; a near-black node "observe" at lower
                 left, annotated "the result comes back, whether it is an answer or an
                 error". A blue tag "specification / goal" at the far left connects into
                 "plan", annotated "written before the loop starts". Beneath the ring a
                 sky-blue cylinder "state / memory"; an arrow runs from "observe" down into
                 it, labelled "what the next step gets to see", and another from the
                 cylinder up into "plan". From "plan" a branch reaches a vermillion diamond
                 "stop condition" at the right, annotated "succeed and halt, or fail and
                 hand back", with two exits: "done" to a sky-blue document icon "result",
                 and "continue" curving back into the ring. A callout in a pale yellow fill
                 beside "observe" reads "a loop corrects only what this step can see — a
                 silent wrong answer is invisible here". Generous margins, sentence case.
```

## 2.3 Tools as delegated weakness

Tools are how an agent hands its own weaknesses to machinery that does not share them.
Think of it as delegating weakness rather than extending strength, and it becomes much easier to predict which tools actually matter.

A language model is an unreliable calculator, an unreliable retriever of specific facts, and an unreliable executor of multi-step arithmetic done in prose, because none of those is what next-token prediction is good at.
Every one of those weaknesses already has a mature, deterministic implementation, and a tool is simply a declared interface through which the model can call that implementation and get its result back.
The research literature made the point early and cleanly: a model can be taught when to reach for a calculator, a search index or a lookup, precisely because it is bad at the arithmetic and factual recall that trivial specialised systems do perfectly (Schick et al., 2023).
The canonical tools are the model's canonical weaknesses, one for one.
Arithmetic and data manipulation go to a code interpreter that computes them exactly.
Retrieval of specific facts goes to a database or a search index that returns them verbatim instead of reconstructing them from parameters.
Access to current or private data, a river-gauge series, a reanalysis field, a repository's files, goes to a tool that reads the actual source rather than the model's stale recollection of it.
The design principle that falls out of this is simple: give the model, as tools, exactly the operations it does worst and ordinary software does best, and resist letting it do in prose what a three-line function would do exactly.

A tool call has a fixed anatomy that recurs throughout the book, so it is worth naming once.
There is a declaration the model can read (the tool's name, purpose and argument schema), an invocation the model emits (a structured call naming the tool and its arguments), an execution outside the model, and a returned result added to state.
Each part is a control point.
The declaration bounds what the model may attempt, which is why least-privilege tool access is a governance decision and not just a security nicety (Chapter 12).
The returned result is the observe step of §2.2, which is why a tool that fails silently, handing back a plausible wrong answer instead of an error, is more dangerous than a tool that is missing altogether: it defeats the loop's only means of correction.
Here is the limitation to hold beside the promise.
A tool delegates the model's weakness at execution, but not at selection.
The interpreter computes correctly, but the model still chose which computation to run and with what arguments, and a correct tool invoked on the wrong quantity (the right formula on an unconverted unit, the right query against the wrong station) returns an exact answer to the wrong question.
Tools narrow the class of errors an agent makes.
They do not abolish it, and what remains is exactly what verification has to target.

**Figure 2.2 — Anatomy of a tool call.**

![A two-lane sequence diagram, agent on the left and tool on the right, read top to bottom through four numbered steps. Step one, the declaration, is annotated as bounding what the model may even attempt. Step two, the invocation, is annotated as the model choosing the operation and its arguments, and marked as the step where a correct tool can still be pointed at the wrong quantity. Step three, execution, happens inside the tool lane and is annotated as the part the model does not control. Step four returns the result to the agent and writes it to a state and memory cylinder, annotated as becoming the loop's observation. A vermillion callout by step four warns that a tool returning a plausible wrong answer instead of an error is more dangerous than one that is missing.](../figures/figure-2-2.svg)

*Figure 2.2 — One tool call, in four parts, each of which is a place you can exercise control. The declaration bounds what the agent may attempt, and the invocation is its choice of operation and arguments. Execution happens outside the model, and the returned result becomes what the loop sees. That last part is why a silent wrong answer is worse than an error. (Rendered as `figures/figure-2-2.svg` from the brief below, per `FIGURES.md`.)*

```
FIGURE BRIEF
- id:            Figure 2.2
- title:         One tool call, four parts
- type:          sequence
- claim:         A tool call has a fixed four-part anatomy (declaration, invocation, execution, returned result), and each part is a distinct control point.
- standfirst:    Each of the four parts is a place you can bound what the agent does.
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
- annotations:   on step 1, "bounds what the model may even attempt — this is where
                 least privilege lives"; on step 2, "the model chooses the operation and
                 its arguments — a correct tool can still be pointed at the wrong
                 quantity"; on step 3, "outside the model, and not under its control";
                 on step 4, "this becomes the loop's observation"; a vermillion callout
                 beside step 4, "a plausible wrong answer here is worse than an error —
                 it defeats the loop's only means of correction"
- caption:       Figure 2.2 — One tool call, in four parts, each of which is a place you can exercise control. The declaration bounds what the agent may attempt, and the invocation is its choice of operation and arguments. Execution happens outside the model, and the returned result becomes what the loop sees. That last part is why a silent wrong answer is worse than an error.
- alt-text:      A two-lane sequence diagram, agent on the left and tool on the right, read top to bottom through four numbered steps. Step one, the declaration, is annotated as bounding what the model may even attempt. Step two, the invocation, is annotated as the model choosing the operation and its arguments, and marked as the step where a correct tool can still be pointed at the wrong quantity. Step three, execution, happens inside the tool lane and is annotated as the part the model does not control. Step four returns the result to the agent and writes it to a state and memory cylinder, annotated as becoming the loop's observation. A vermillion callout by step four warns that a tool returning a plausible wrong answer instead of an error is more dangerous than one that is missing.
- infographic description: A flat vector sequence diagram on an off-white background, 16:9,
                 with two vertical lanes read top to bottom. Title top-left: "One tool
                 call, four parts". Standfirst beneath: "Each of the four parts is a place
                 you can bound what the agent does." The left lane header is an orange
                 rounded square "agent (model)"; the right lane header is a green wrench
                 glyph "tool / interpreter". Four numbered horizontal arrows cross between
                 the lanes, each with an annotation in smaller type beside it. "1
                 declaration", a dashed arrow into the agent lane from a small tag "tool
                 declaration", annotated "bounds what the model may even attempt — this is
                 where least privilege lives". "2 invocation", agent to tool, annotated
                 "the model chooses the operation and its arguments — a correct tool can
                 still be pointed at the wrong quantity". "3 execution", a short self-loop
                 within the tool lane, annotated "outside the model, and not under its
                 control". "4 returned result", tool back to agent, annotated "this becomes
                 the loop's observation". From step 4 a further arrow drops to a sky-blue
                 cylinder "state / memory" at the bottom. A callout in a pale yellow fill
                 beside step 4 reads "a plausible wrong answer here is worse than an error
                 — it defeats the loop's only means of correction". Single-weight lines,
                 generous spacing, sentence case.
```

## 2.4 Context and memory as a finite store

Context and memory are the agent's working store, and the thing that governs how you use them is that the store is finite, ordered and lossy.
Those properties have to be designed around, not wished away.

The immediate working store is the model's context window: the bounded span of text (instructions, retrieved material, prior tool results, the running transcript) the model can attend to when it plans its next step.
Everything the agent knows at a given moment is either in that window or it is absent.
The window has a fixed capacity which, although it has grown by more than an order of magnitude across the capability period described in Chapter 1 [verify], is still finite, and every tool result the loop appends uses some of it up.
The vocabulary the research literature uses here is worth borrowing, because it separates the volatile working memory of a single run from the longer-term stores an agent writes to and reads back: episodic records of what happened, and semantic notes of what was learned (Sumers et al., 2023).
That distinction is exactly where a scientific workflow either keeps its provenance or loses it.

Three consequences follow, and each one has caught practitioners out.
First, a long-running loop fills its own context.
Every observed result takes up space, so a task of many steps drifts towards the window's limit, at which point earlier material, the original specification or an early constraint, has to be summarised, dropped or externalised.
A constraint that has fallen out of the window is a constraint the agent no longer honours.
Second, position within the window matters.
Material at the start and the end of a long context is attended to more reliably than material buried in the middle, so merely fitting information into the window does not guarantee it gets used (moderate confidence; the effect is documented but its magnitude varies by model).
Third, the window is volatile, holding only within a single run, so anything that has to persist across runs needs an explicit external memory: notes written to a file, records in a database, or a specification kept under version control.
This distinction between volatile context and durable memory is not incidental housekeeping.
It is where an agent's provenance is either captured or lost, and Chapter 12 builds audit trails, assumption registries and reviewer-coverage records on top of the durable store.

For scientific work, the implication is to treat context as a scarce, curated resource rather than somewhere to put everything.
The reliable pattern is to put the specification and the acceptance criteria where they will actually be attended to, to retrieve into the window only the material a given step needs, and to write out to durable memory anything that has to survive the run or serve as evidence afterwards.
The limitation worth recording is that this curation is itself a design task with no sensible default.
An agent handed a large context and no discipline about what goes into it will degrade quietly, making worse decisions with no error to mark the moment its working store stopped serving it.

**Figure 2.3 — Context and memory.**

![Two panels side by side. On the left, a bounded rectangle labelled context window, its right edge marked as a hard capacity limit. Inside it four stacked bands: specification, retrieved material, tool results and running transcript. The top and bottom bands are highlighted and annotated as attended to most reliably; the middle bands are greyed and annotated as attended to less reliably, so fitting information in does not guarantee it is used. A note beneath reads that this holds within a single run only, and that anything falling out of the window is a constraint the agent no longer honours. On the right, across a clear gap, a cylinder labelled durable memory holding files, records and version control, annotated as where provenance lives and as persisting across runs. A two-way arrow between them is labelled externalise and retrieve.](../figures/figure-2-3.svg)

*Figure 2.3 — Two stores, one of which forgets. The context window is finite and volatile, and its middle is attended to less reliably than its edges. Getting something into it is not the same as having it used. Anything that has to survive the run, or serve as evidence afterwards, has to be written out to durable memory, which is where provenance actually lives. (Rendered as `figures/figure-2-3.svg` from the brief below, per `FIGURES.md`.)*

```
FIGURE BRIEF
- id:            Figure 2.3
- title:         The working store and the durable store
- type:          architecture
- claim:         An agent holds a finite, volatile context window within a run and a durable external memory across runs; the two are distinct, and provenance depends on the second.
- standfirst:    One of these two stores forgets everything the moment the run ends.
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
- annotations:   on the highlighted top and bottom bands, "attended to most reliably";
                 on the greyed middle bands, "attended to less reliably — fitting it in
                 is not the same as having it used"; on the capacity limit edge, "every
                 tool result the loop appends uses some of this up"; under the window,
                 "a constraint that falls out of here is a constraint the agent no longer
                 honours"; on the cylinder, "where provenance lives"; on the two-way arrow,
                 "write out what has to survive; read back only what this step needs"
- caption:       Figure 2.3 — Two stores, one of which forgets. The context window is finite and volatile, and its middle is attended to less reliably than its edges. Getting something into it is not the same as having it used. Anything that has to survive the run, or serve as evidence afterwards, has to be written out to durable memory, which is where provenance actually lives.
- alt-text:      Two panels side by side. On the left, a bounded rectangle labelled context window, its right edge marked as a hard capacity limit. Inside it four stacked bands: specification, retrieved material, tool results and running transcript. The top and bottom bands are highlighted and annotated as attended to most reliably; the middle bands are greyed and annotated as attended to less reliably, so fitting information in does not guarantee it is used. A note beneath reads that this holds within a single run only, and that anything falling out of the window is a constraint the agent no longer honours. On the right, across a clear gap, a cylinder labelled durable memory holding files, records and version control, annotated as where provenance lives and as persisting across runs. A two-way arrow between them is labelled externalise and retrieve.
- infographic description: A flat vector architecture diagram on an off-white background,
                 16:9. Title top-left: "The working store and the durable store".
                 Standfirst beneath: "One of these two stores forgets everything the moment
                 the run ends." On the left, a large sky-blue-bordered rectangle "context
                 window" with a thick grey right edge labelled "capacity limit", annotated
                 "every tool result the loop appends uses some of this up". Inside, four
                 horizontal bands stack top to bottom: "specification", "retrieved
                 material", "tool results", "running transcript". The top and bottom bands
                 have a pale yellow fill and a shared annotation "attended to most
                 reliably"; the two middle bands are greyed with the annotation "attended
                 to less reliably — fitting it in is not the same as having it used".
                 Beneath the rectangle, a label "within a run" and a line reading "a
                 constraint that falls out of here is a constraint the agent no longer
                 honours". To the right, across a clear gap, a sky-blue cylinder "durable
                 memory" with sub-text "files · records · version control" and a callout
                 "where provenance lives"; beneath it the label "across runs". A two-way
                 single-weight arrow between rectangle and cylinder is labelled
                 "externalise / retrieve" and annotated "write out what has to survive;
                 read back only what this step needs". Generous margins, sentence case.
```

## 2.5 Orchestration as composition

Orchestration is what happens when you compose individual agent steps into a larger process.
The question it answers is not how one agent thinks, but how an arrangement of steps, agents and gates ends up more reliable than any of its parts.
A single plan–act–observe loop is the unit; orchestration is what you build out of many of them, and it takes a small number of recognisable forms.

> **Definition — Orchestration.** The arrangement of several agent steps, plus the checks and human decisions between them, into one larger workflow. Where a single agent is one worker, orchestration is the division of labour: which step does what, in what order, and which step checks which. It is the layer where a workflow's reliability is engineered.

The simplest form is a sequence: a chain where one step's output is the next step's input.
That suits a task which decomposes into stages with a fixed order, such as acquire, then clean, then summarise.
Past sequence comes delegation, where a coordinating step hands a bounded sub-task to a separate agent with its own loop, tools and fresh context.
Delegation is valuable precisely because the sub-agent's context is clean.
A large retrieval or a noisy exploration can be confined to it, and only the distilled result returned to the coordinator, which keeps the coordinator's finite store (§2.4) uncluttered.

> **Definition — Sub-agent.** A second agent to which a coordinating agent hands a self-contained piece of work, with its own tools and its own clean context. It does the bulky or noisy part in isolation and returns only the distilled result, so the coordinator never has to hold the intermediate material in view.

A third form is a distinct reviewer step whose whole job is to check another step's output before it goes any further.
This one matters disproportionately in scientific work, because it is where the external verification of §2.2 gets a structural home.
A reviewer agent working from a separate context, or a deterministic gate applying a rule, interrupts a stream of confident output with a check the producing agent could never have marked against itself.
None of these forms is the book's invention.
They are the composable patterns practitioners converged on and documented, such as chaining, routing, parallel work, a coordinator with workers, and evaluator-and-improver loops, under a governing recommendation this book shares: use the simplest arrangement that works, and add orchestration only when the task visibly needs it (Anthropic, 2024).
That recommendation names the real design judgement here, which is knowing when composition adds robustness and when it adds only cost and noise.
The honest answer is that more agents are not reliably better.
Each added step spends tokens, adds latency and brings its own ways of failing, so composition earns its place only where a step genuinely reduces error or confines it, not where it merely multiplies activity.

This chapter deliberately stops at the anatomy of composition and leaves the multi-agent patterns themselves for later.
Chapter 10 composes the book's core patterns into rosters of agents, reviewers and human gates, and Chapter 15 applies that composition end to end.
The structural point to carry forward is this: orchestration is where the workflow layer of Chapter 1's taxonomy actually gets built, the layer that adds specification, verification and accountability to a bare agent.
It is built out of the same four parts described above, arranged so the observe steps and the gates fall exactly where a wrong answer would otherwise escape.
The limitation is that orchestration cannot rescue an unspecified task.
Compose steps around a goal that was never written down clearly (Chapter 3) and you distribute the ambiguity rather than resolving it, and a well-orchestrated workflow executing a vague specification fails more expensively than a single agent ever could.

## 2.6 A plain cost model

Every agent action costs something, and reasoning about those costs plainly, rather than assuming that falling model prices make the question moot, is part of operating the instrument responsibly.
The costs fall into three kinds, and they behave quite differently.

The first is token cost.

> **Definition — Token.** The unit these models read and write in, roughly a short fragment of a word. Text is billed and measured by the token, so the length of everything an agent reads and produces, including its own steadily growing transcript, is exactly what the paid case charges for.

Models are billed, in the paid case, by how much text is read and generated.
A loop that appends every tool result to a growing context pays for that context at every later step, and a long orchestration re-reads its accumulated state again and again, so cost grows faster than the step count alone would suggest.
The second is tool-and-compute cost: the executions the agent triggers, such as a query against a large archive, a regridding job, or a model run invoked as a tool.
These carry their own expense in machine time and, for an environmental readership, in energy and the carbon that comes with it.
That cost is easy to overlook because it never appears on the model bill, and Chapter 16 treats it directly rather than as a footnote.
The third is latency: the wall-clock time a loop takes, which is a real cost in operational settings where a forecast bulletin has a deadline.
An agent that reaches a correct answer after the window in which it was useful has failed operationally, whatever its accuracy.

One observation reorganises all three, and it recurs throughout the book: in a well-run scientific workflow the dominant cost is not generation but verification.
Producing a draft, a script or a synthesis is comparatively cheap.
Establishing that it is correct is where the effort and the expense concentrate: running the tests, checking the citations against sources, validating the extraction against a schema, having a reviewer step or a human confirm an interpretation.
That effort does not fall as model prices fall, because it is external to the model by design (§2.2).
This inverts the naive economic case for agents.
The saving was never that science becomes cheap to verify.
It is that the production which precedes verification becomes cheap enough that more of the budget can go on verifying well, which is exactly where a scientific workflow should want to spend it.

The honest limitation is that these three costs trade against one another, and against reliability, in ways specific to the task.
A cheaper model may need more loop iterations, a faster answer may skip a check, and there is no general optimum.
What does generalise is the accounting discipline: name all three costs and the verification burden explicitly, so a workflow is chosen with its true price visible.
The concrete figures that would fill in this model are volatile, belong in the companion repository, and are developed against a realistic adoption path in Chapter 16.

**[AUTHOR: an approximate cost breakdown from one of your operational workflows — the split between production and verification effort — would make this section concrete; keep any per-token or per-run figures in the repository, not in print.]**

---

*This chapter has taken the agent apart into a loop, tools, a finite store and their composition, and priced the result.*
*The next chapter turns to the human side of the same mechanism: how to specify a task so this apparatus can execute it and a scientist can audit it afterwards, the skill most failures trace back to.*

---

### References (verify details before release)

- Anthropic (2024). Building effective agents. *Anthropic engineering blog.* https://www.anthropic.com/engineering/building-effective-agents
- Arunkumar, V., Gangadharan, G. R. and Buyya, R. (2026). Agentic artificial intelligence (AI): architectures, taxonomies, and evaluation of large language model agents. *arXiv preprint.* https://arxiv.org/abs/2601.12560
- Jones, N. B. (2026). "Don't build more AI agents until you watch this." Video, @natebjones, 17 June 2026. https://www.youtube.com/watch?v=BOXK2XFLA-E (practitioner commentary; concepts cited as corroboration, not evidence)
- Schick, T., et al. (2023). Toolformer: language models can teach themselves to use tools. *NeurIPS 2023.* https://arxiv.org/abs/2302.04761
- Sumers, T. R., Yao, S., Narasimhan, K. and Griffiths, T. L. (2023). Cognitive architectures for language agents. *Transactions on Machine Learning Research.* https://arxiv.org/abs/2309.02427
- Wang, L., et al. (2023). A survey on large language model based autonomous agents. *arXiv preprint.* https://arxiv.org/abs/2308.11432
- Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K. and Cao, Y. (2023). ReAct: synergizing reasoning and acting in language models. *ICLR 2023.* https://arxiv.org/abs/2210.03629
