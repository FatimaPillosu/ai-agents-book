# Chapter 2 — Anatomy of an agent

> **Status:** draft · figures specified as briefs per `FIGURES.md`. Chapter lengths are indicative guidance, not fixed allocations.
> **Conventions:** vendor-neutral per outline §9. Passages needing the author's lived material or number verification are tagged **[AUTHOR: …]** or **[verify]**. No anecdotes or statistics have been invented.

---

## 2.1 The instrument and its parts

Chapter 1 fixed a taxonomy — a model inside an agent inside a workflow — and this chapter takes the agent apart to show what each of its parts does and where each fails. The purpose is diagnostic rather than architectural: a scientist who understands an agent only as a black box that answers prompts has no way to reason about why it produced a wrong answer, and no place to attach the verification that Part III insists upon. Taken apart, an agent proves to have four parts and no more — a model that proposes, a loop that sequences, tools that act, and a store that remembers — and every behaviour worth governing arises from the interaction of these four. The model was the subject of the previous chapter and is treated here only as the component that supplies judgement at each step; the loop, the tools and the store are the additions that turn a function from text to text into something that can carry a bounded task from instruction to verified result. The organising metaphor of this book is the instrument, and it holds down to this level of detail: an oscilloscope is a display, a timebase, an input stage and a trigger, and one learns to trust its trace by understanding what each stage contributes and how each distorts. An agent is no different in kind, only newer and less characterised. The account that follows describes each part as an instrument-part — what it is for, what it can be relied upon to do, and the specific way it misleads — because a reader who holds that account can situate every later pattern, and every failure in the Chapter 13 gallery, against a shared picture of the mechanism. The four parts are introduced in the order in which they engage during a single step of work: the loop that governs the step (§2.2), the tools it may call (§2.3), the store it reads and writes (§2.4), and then the composition of many such steps into an orchestrated process (§2.5), before the chapter closes on what all of this costs (§2.6).

## 2.2 The loop as control cycle

The defining feature of an agent, the one that separates it from a model that merely emits text, is a control cycle in which the system plans an action, executes it, observes the result, and decides its next action in the light of what it observed. This plan–act–observe loop is the agent's engine, and it is worth stating its steps precisely because loose description is where misplaced expectation begins. In the plan step the model, given the goal and the state accumulated so far, proposes a single next action — a tool to call with specific arguments, or a decision that the task is complete. In the act step that proposed action is executed outside the model, by machinery the model does not control: an interpreter runs the code, a database answers the query, a file is read. In the observe step the result of that execution — a returned value, an error message, a retrieved passage — is appended to the state and passed back to the model, which plans again. The cycle repeats until a stopping condition is met, and the character of the whole system depends far more on that loop than on any single response the model produces. The property that makes the loop valuable is that it converts a one-shot prediction into an error-correcting process: a model that writes code with a bug is merely wrong, whereas an agent that writes the same code, runs it, reads the traceback and rewrites it can recover from the bug without human intervention, provided the loop returns evidence the model can act on. That proviso is the whole discipline. A loop only corrects errors it can observe, so the quality of the observe step — whether the tool returns a real error or a silent wrong answer, whether the check is external or the model is left to grade itself — governs whether iteration converges on a correct result or merely accumulates confident wrongness. The loop's characteristic failure follows directly: given a weak or absent observe step, the same mechanism that recovers from a traceback will elaborate a mistake across many steps, each locally plausible, arriving at an output whose length and detail read as thoroughness while its foundation is an early error never checked (high confidence in the mechanism; frequency varies by task and model). **[AUTHOR: a short trace from your own operational work where an agent iterated to a confidently wrong result — and the observation that would have caught it — would anchor this better than the general claim.]**

**Figure 2.1 — The plan–act–observe loop.** *A figure brief follows `FIGURES.md`; render in the house style.*

```
FIGURE BRIEF
- id:            Figure 2.1
- title:         The plan–act–observe control cycle
- type:          architecture
- claim:         An agent's defining feature is a control cycle in which the model proposes an action, external machinery executes it, and the observed result feeds the next decision — the cycle, not any single response, is the engine.
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
- alt-text:      A circular diagram of three nodes — plan, act and observe — read clockwise. A goal enters at plan; observe writes to a state-and-memory cylinder beneath the ring and returns to plan. A branch from plan reaches a stop-condition diamond whose done exit produces a result artefact and whose continue exit re-enters the ring. A callout on the observe step notes that the returned result is external, not the model's self-assessment.
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

Tools are the means by which an agent delegates the model's weaknesses to machinery that does not share them, and this framing — delegation of weakness rather than extension of strength — is the one that predicts which tools matter. A language model is an unreliable calculator, an unreliable retriever of specific facts, and an unreliable executor of multi-step arithmetic conducted in prose, because none of these is what next-token prediction is good at; but each has a mature, deterministic implementation already, and a tool is simply a declared interface through which the model can invoke that implementation and receive its result. The canonical cases are exactly the model's canonical weaknesses inverted: arithmetic and data manipulation go to a code interpreter that computes them exactly; retrieval of specific facts goes to a database or search index that returns them verbatim rather than reconstructing them from parameters; access to current or private data — a river-gauge series, a reanalysis field, a repository's files — goes to a tool that reads the actual source rather than the model's stale recollection of it. The design principle that follows is to give the model as tools precisely the operations it performs worst and conventional software performs best, and to resist the temptation to have the model do in prose what a three-line function would do exactly. A tool call has a fixed anatomy that recurs throughout the book and is worth naming once: a declaration the model can read (the tool's name, purpose and argument schema), an invocation the model emits (a structured call naming the tool and its arguments), an execution outside the model, and a returned result appended to state. Each part is a control point. The declaration bounds what the model may attempt, which is why least-privilege tool access is a governance lever and not merely a security nicety (Chapter 12); the returned result is the observe step of §2.2, which is why a tool that fails silently — returning a plausible wrong answer rather than an error — is more dangerous than one that is merely absent, because it defeats the loop's only means of correction. The limitation to hold beside the promise is that a tool delegates the model's weakness at execution but not at selection: the interpreter computes correctly, but the model still chose which computation to run and with what arguments, and a correct tool invoked on the wrong quantity — the right formula on an unconverted unit, the right query against the wrong station — returns an exact answer to the wrong question. Tools narrow the class of errors an agent makes; they do not eliminate it, and the residual class is precisely the one verification must target.

**Figure 2.2 — Anatomy of a tool call.** *A figure brief follows `FIGURES.md`; render in the house style.*

```
FIGURE BRIEF
- id:            Figure 2.2
- title:         One tool call, four parts
- type:          sequence
- claim:         A tool call has a fixed four-part anatomy — declaration, invocation, execution, returned result — and each part is a distinct control point.
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
- caption:       Figure 2.2 — The four parts of a tool call. The declaration bounds what the model may attempt; the invocation is the model's choice of operation and arguments; execution happens outside the model; the returned result becomes the loop's observation — which is why a silent wrong answer is more dangerous than an error.
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

Context and memory are the agent's working store, and the property that governs their use is that the store is finite, ordered and lossy in ways that shape what an agent can reliably do. The immediate working store is the model's context window: the bounded span of text — instructions, retrieved material, prior tool results, the running transcript — that the model can attend to when it plans its next step. Everything the agent "knows" at a given step is either in that window or absent, and the window has a fixed capacity that, though it has grown by more than an order of magnitude across the capability period described in Chapter 1 [verify], remains finite and is consumed by every tool result the loop appends. Three consequences follow that a scientist must design around rather than wish away. The first is that a long-running loop fills its own context: each observed result occupies space, and a task of many steps will approach the window's limit, at which point earlier material — the original specification, an early constraint — must be summarised, dropped or externalised, and a constraint that has fallen out of the window is a constraint the agent no longer honours. The second is that position within the window matters: material at the start and end of a long context is attended to more reliably than material buried in the middle, an unevenness that means merely fitting information into the window does not guarantee it is used (moderate confidence; the effect is documented but its magnitude varies by model). The third is that the window is volatile — it holds only within a single run — so any persistence across runs requires an explicit, external memory: notes written to a file, records in a database, a specification kept under version control. This distinction between volatile context and durable memory is not incidental housekeeping; it is where an agent's provenance is either captured or lost, and Chapter 12 treats the durable store as the substrate on which audit trails, assumption registries and reviewer-coverage records are built. The design implication for scientific work is to treat context as a scarce, curated resource rather than a bucket into which everything is poured: the reliable pattern is to place the specification and the acceptance criteria where they will be attended to, to retrieve into the window only the material a given step needs, and to externalise to durable memory anything that must survive the run or serve as evidence afterwards. The limitation to record is that curation is itself a design task with no default: an agent given a large context and no discipline about what enters it will degrade quietly, producing worse decisions without any error to mark the moment its working store stopped serving it.

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
- alt-text:      On the left, a bounded rectangle labelled context window with a marked capacity limit contains stacked bands — specification, retrieved material, tool results and running transcript — with the top and bottom bands highlighted and the middle greyed and marked "attended to less reliably". On the right, separated by a gap, a cylinder labelled durable memory holds files, records and version control, marked "where provenance lives". A two-way arrow labelled externalise and retrieve connects the two; the left is within a run, the right across runs.
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

Orchestration is the composition of individual agent steps into a larger process, and the question it answers is not how one agent thinks but how many steps, agents and gates are arranged so that the whole is more reliable than any part. A single plan–act–observe loop is the atom of §2.2; orchestration is the chemistry, and it takes a small number of recognisable forms. The simplest is sequence: a chain in which one step's output is the next step's input, appropriate when a task decomposes into stages with a fixed order, such as acquire, then clean, then summarise. Beyond sequence lies delegation, in which a coordinating step hands a bounded sub-task to a separate agent with its own loop, tools and fresh context — valuable precisely because the sub-agent's context is clean, so a large retrieval or a noisy exploration can be confined to it and only its distilled result returned to the coordinator, keeping the coordinator's finite store (§2.4) uncluttered. A third form is the introduction of a distinct reviewer step whose role is to check another step's output before it proceeds, and this form matters disproportionately in scientific work because it is where the external verification of §2.2 is given a structural home: a reviewer agent operating on a separate context, or a deterministic gate applying a rule, interrupts the flow of confident output with a check the producing agent cannot mark its own homework against. The design judgement that orchestration demands is when composition adds robustness and when it adds only cost and noise, and the honest answer is that more agents are not reliably better — each added step consumes tokens, adds latency and introduces its own failure surface, so composition earns its place only where a step genuinely reduces error or confines it, not where it merely multiplies activity. This chapter deliberately stops at the anatomy of composition and does not develop the multi-agent patterns themselves; Chapter 10 is the capstone that composes the book's core patterns into rosters of agents, reviewers and human gates, and Chapter 15 applies that composition end to end. The point to carry forward from here is structural: orchestration is where the workflow layer of Chapter 1's taxonomy is actually built — the layer that adds specification, verification and accountability to the agent — and it is built out of the same four parts described above, arranged so that the observe steps and the gates fall in the places where a wrong answer would otherwise escape. The limitation is that orchestration cannot compensate for an unspecified task: composing steps around a goal that was never written down clearly (Chapter 3) distributes the ambiguity rather than resolving it, and a well-orchestrated workflow executing a vague specification fails more expensively than a single agent would.

## 2.6 A plain cost model

Every agent action has a cost, and reasoning about those costs plainly — rather than assuming that falling model prices make the question moot — is part of operating the instrument responsibly. The costs an agent incurs fall into three kinds that behave differently. The first is token cost: models are billed, in the paid case, by the quantity of text read and generated, so a loop that appends every tool result to a growing context pays for that context at every subsequent step, and a long orchestration re-reads accumulated state repeatedly, which means cost grows faster than the step count alone would suggest. The second is tool-and-compute cost: the executions the agent triggers — a query against a large archive, a regridding job, a model run invoked as a tool — carry their own expense in machine time and, for an environmental readership, in energy and its attendant carbon, a cost that is easy to overlook because it does not appear on the model bill and that Chapter 16 treats directly rather than as a footnote. The third is latency, the wall-clock time a loop takes, which is a real cost in operational settings where a forecast bulletin has a deadline: an agent that arrives at a correct answer after the window in which it was useful has failed operationally whatever its accuracy. The observation that reorganises all three, and that this book returns to repeatedly, is that in a well-run scientific workflow the dominant cost is not generation but verification. Producing a draft, a script or a synthesis is comparatively cheap; establishing that it is correct — running the tests, checking the citations against sources, validating the extraction against a schema, having a reviewer step or a human confirm an interpretation — is where the effort and the expense concentrate, and it is effort that does not fall as model prices fall because it is external to the model by design (§2.2). This inverts the naive economic case for agents. The saving is not that the science becomes cheap to verify; it is that the production which precedes verification becomes cheap enough that more of the budget can be spent on verifying well, which is where a scientific workflow should want to spend it. The limitation to state honestly is that these three costs trade against one another and against reliability in ways specific to a task: a cheaper model may need more loop iterations, a faster answer may skip a check, and there is no general optimum. What generalises is the accounting discipline of naming all three costs and the verification burden explicitly, so that a workflow is chosen with its true price visible; the concrete figures that would populate this model are volatile, belong in the companion repository, and are developed against a realistic on-ramp in Chapter 16. **[AUTHOR: an approximate cost breakdown from one of your operational workflows — the split between production and verification effort — would make this section concrete; keep any per-token or per-run figures in the repository, not in print.]**

---

*This chapter has taken the agent apart into a loop, tools, a finite store and their composition, and priced the result. The next chapter turns to the human side of the same mechanism: how to specify a task so that this apparatus can execute it and a scientist can audit it — the skill to which, in the author's experience, most failures trace back.*
