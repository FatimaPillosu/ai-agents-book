# Figure briefs — Chapter 2 — Anatomy of an agent

Briefs for the figures of `manuscript/ch02-anatomy-of-an-agent.md`, held here rather than in the chapter so the prose reads clean.
Each brief follows `FIGURES.md` §6. The caption and alt-text in the chapter are generated with the brief and must be changed here and there together.

## Figure 2.1 — The plan–act–observe loop

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

## Figure 2.2 — Anatomy of a tool call

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

## Figure 2.3 — Context and memory

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

## Figure 2.4 — The agent proposes, something else disposes

```
FIGURE BRIEF
- id:            Figure 2.4
- title:         The agent proposes, something else disposes
- type:          architecture
- claim:         In a governed workflow the agent proposes and something the agent does not control disposes, and there are exactly three kinds of disposer.
- standfirst:    Only three kinds of thing may write to the record: a rule, a person, or a fact.
- canvas:        16:9
- elements:      left, an orange rounded rectangle "agent"; a single labelled arrow
                 carrying a "proposal, not an action" tag; three disposer paths fanning
                 out from it — a vermillion diamond "deterministic rule", a blue
                 head-and-shoulders icon "human decision", and a green tool glyph paired
                 with a small sky-blue cylinder "external source of truth"; right, one
                 shared sky-blue cylinder "protected artefact" that all three accept
                 exits reach; below it a grey cylinder "rejection log" that all three
                 reject exits reach; a footer strip across the foot
- flow:          left-to-right — agent → proposal → three disposers → protected artefact.
                 Each disposer carries two labelled exits, "accept" continuing right to
                 the protected artefact and "reject" dropping to the rejection log
- labels:        "agent", "proposal, not an action", "deterministic rule",
                 "human decision", "external source of truth", "accept", "reject",
                 "protected artefact", "rejection log"
- annotations:   on the proposal arrow, in vermillion, "nothing has been written yet";
                 on the deterministic rule, "use where the criterion can be written as
                 code"; on the human decision, "use where the criterion is judgement";
                 on the external source of truth, "use where the criterion is a fact the
                 agent cannot manufacture: a test suite, a reference dataset"; on the
                 protected artefact, "only a disposer may write here"; on the rejection
                 log, "a rejected proposal is kept, with the reason"; a footer, "what
                 this does not buy: a rule set that admits the wrong thing admits it
                 every time"
- caption:       Figure 2.4 — Who is allowed to write, and who is only allowed to ask. The agent's output is a proposal, so work that is fluent and wrong reaches the record only if a disposer lets it through. There are three kinds of disposer: a rule, a person, or a fact the agent cannot manufacture. What the arrangement does not buy is a good disposer, and a rule set that admits the wrong thing admits it every time.
- alt-text:      An architecture diagram reading left to right. An orange agent box sends a single arrow labelled proposal, not an action, annotated in vermillion that nothing has been written yet. The arrow fans into three disposer paths. A vermillion diamond, deterministic rule, is annotated for use where the criterion can be written as code. A blue head-and-shoulders icon, human decision, is annotated for use where the criterion is judgement. A green tool glyph with a sky-blue cylinder, external source of truth, is annotated for use where the criterion is a fact the agent cannot manufacture. The examples given are a test suite and a reference dataset. Each path has an accept exit to one shared sky-blue cylinder, the protected artefact, annotated that only a disposer may write there. Each also has a reject exit to a grey rejection log, annotated that a rejected proposal is kept with its reason. A footer reads: what this does not buy is a well-designed disposer, and a rule set that admits the wrong thing admits it every time.
- infographic description: A flat vector architecture diagram on an off-white background,
                 16:9, flowing left to right. Title top-left: "The agent proposes,
                 something else disposes". Standfirst beneath: "Only three kinds of thing
                 may write to the record: a rule, a person, or a fact." At the left, an
                 orange-bordered rounded rectangle "agent". From its right edge a single
                 arrow carries a tag "proposal, not an action", with a vermillion callout
                 on the arrow reading "nothing has been written yet". The arrow meets a
                 small junction and fans into three parallel paths stacked vertically.
                 The upper path reaches a vermillion diamond "deterministic rule",
                 annotated "use where the criterion can be written as code". The middle
                 path reaches a blue head-and-shoulders icon "human decision", annotated
                 "use where the criterion is judgement". The lower path reaches a green
                 wrench glyph beside a small sky-blue cylinder, together labelled
                 "external source of truth" and annotated "use where the criterion is a
                 fact the agent cannot manufacture: a test suite, a reference dataset".
                 Each of the three carries two labelled exits. The "accept" exits
                 converge rightward on one large sky-blue cylinder "protected artefact",
                 annotated "only a disposer may write here". The "reject" exits drop to a
                 grey cylinder "rejection log" set below it, annotated "a rejected
                 proposal is kept, with the reason". A footer strip runs across the foot
                 reading "what this does not buy: a rule set that admits the wrong thing
                 admits it every time". Single-weight connectors, one arrowhead style,
                 right-angle corners, generous margins, sentence case throughout.
```
