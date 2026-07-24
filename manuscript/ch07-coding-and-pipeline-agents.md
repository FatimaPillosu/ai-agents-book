# Chapter 7 — Coding and pipeline agents

> **Status:** draft r2 · voice v2.0 (`STYLE.md`) · sentence-per-line per `STYLE.md` §10 · figures as briefs per `FIGURES.md`.
> **Conventions:** vendor-neutral (outline §9) · **[AUTHOR: …]** marks lived material only the author can supply · **[verify]** marks real but unconfirmed details · citations drawn only from verified reports in `/research`. Nothing has been invented.
> **Chapter note:** the worked example of §7.4 is scaffolded; its specifics are the author's to supply and no result has been invented.

---

## 7.1 The problem: code that works once is not a pipeline

The characteristic software artefact of environmental research is a notebook that ran correctly once, on one machine, for one dataset, and was never meant to run again.
Exploratory analysis rewards exactly that: you load a forecast field, try a regridding step, plot the result, nudge a threshold, and move on, accumulating cells in the order the investigation happened to take rather than the order a reader would need.
I don't want to disparage that mode, because it is how understanding actually gets built.
The trouble starts when the same artefact is pressed into service as though it were a pipeline — rerun next season, handed to a student, cited as the method behind a figure, scheduled to produce an operational product — without acquiring any of the properties that would make it trustworthy in that role.
Those properties are well understood and predate agents entirely: version control, tests that assert what the code is supposed to do, a fixed and declared environment, configuration kept separate from logic, and a review step performed by someone other than the author.
The gap between the notebook and the governed pipeline is not a gap in cleverness but a gap in discipline, and most working scientists know they should close it and mostly do not, because closing it costs hours the next deadline has already claimed.
Agents change the economics of that gap in both directions at once, and that change is the subject of this chapter.
They lower the cost of writing the tests, hooks and scaffolding a governed pipeline needs, and they simultaneously raise the cost of not having them, because an agent will generate plausible code far faster than an unaided human can read it — and a pile of plausible-but-unverified code is precisely what a research group least needs more of (high confidence).

The reframing I want you to take from this chapter is that the unit of work is not the code an agent produces but the set of gates that code must pass before it is trusted.
A scientist who asks an agent to "write the regridding step" and then reads the result has swapped the agent for a colleague and changed very little.
A scientist who builds a workflow in which the agent's output must pass automated tests, then pre-commit hooks, then an independent reviewer agent, and only then reaches a human who owns the decision, has built something with more assurance than most hand-written research code ever receives.
I am not claiming that gates make agent-written code safe in any absolute sense, because no arrangement of automated checks catches a plausible error that every check was too weak to notice.
The claim is narrower and, I think, more useful: the discipline agents make affordable is the same discipline good software engineering has always prescribed, and the right response to a fast, fallible code generator is to build the verification the field already knew it should have.
This chapter connects the loop and tools of Chapter 2 to the multi-agent review of Chapter 10 and the evaluation methods of Chapter 11, and treats the governed pipeline as the concrete setting where those ideas first pay for themselves.

## 7.2 The conventional workflow and where it breaks

The conventional path from notebook to production, in the rare group where any path exists at all, is a sequence of manual translations that lean on the same person's diligence at every step.
A scientist who decides an analysis deserves to become a reusable tool typically refactors the notebook into scripts by hand, adds a handful of tests if time allows, writes a README, and — in the better-run groups — opens a merge request for a colleague to review before it lands on the main branch.
Every one of those steps is skippable, and under deadline each is skipped in a predictable order.
The tests go first, because they are the part with no immediately visible output; then the review shrinks to a glance; then the environment specification is left implicit in whatever happened to be installed; until what reaches the shared repository is a lightly tidied notebook with the notebook's fragility intact.
The failure is not one of knowledge, since the scientists involved can usually recite the practice they are omitting.
It is that the practice is front-loaded effort against a back-loaded and uncertain payoff, and human attention discounts the future steeply.
The consequence for environmental science specifically is a literature and an operational estate resting on code that has never been independently read, whose correctness is asserted by the fact that its outputs looked reasonable, and whose silent errors — a transposed coordinate, a unit left unconverted, a fill value treated as data — surface, if they surface at all, as anomalies in a downstream result that someone else has to chase (moderate confidence; the prevalence is widely discussed but not systematically measured).

The specific weakness agents both expose and can help repair is the absence of an independent reader.
You are the worst possible reviewer of your own code, because the same misunderstanding that produced an error also blinds you to it.
That is why software engineering treats review by a second person as non-negotiable, and why science treats peer review as constitutive rather than optional.
Research groups are frequently too small, too specialised or too pressed to supply that second reader for routine code, so most research code is merged on the author's word alone.
An agent cannot replace the accountable human reviewer, and I want to be emphatic that it must not be asked to.
What it can do is occupy the role of the tireless first reader who never skips the review because it is late on a Friday, applying a consistent checklist to every change and surfacing the ten routine issues so that the human's scarce attention lands on the one that matters.
That is a genuine addition to a workflow that currently has nothing in the slot at all, and it is the redesign the next section sets out.

## 7.3 The agentic redesign: successive gates, human at the end

The redesign replaces a single act of trust with a series of independent gates, each cheaper than the human review it protects and each catching a different class of error.
The first gate is the automated test suite, which asserts what the code must do — that a known input produces a known output, that a conservation property holds, that an edge case is handled — and which the agent may write alongside the code but which derives its authority from being specified against intended behaviour rather than produced behaviour.
This is not an exotic idea; it is the discipline that made coding agents measurable in the first place.
The benchmark that now tracks their progress on real software-repository issues judges a proposed fix by running the repository's own pre-existing test suite, so the acceptance criterion exists before the agent runs, is automated, and does not depend on any model's opinion (Jimenez et al., 2023) — which is exactly the property a scientific pipeline's tests must have.
The second gate is the set of pre-commit hooks, which run automatically whenever a change is committed and enforce the mechanical properties that need no judgement: formatting, linting, type checks, a scan for secrets and large files, and the test suite itself, so that nothing reaches the shared history without passing them.
The third gate is an independent reviewer agent — and the word independent is load-bearing — which reads the proposed change against a review specification and reports what it finds, but which is deliberately a *different* agent instance from the one that wrote the code, with its own context, its own instructions and no stake in defending the work, for reasons §7.5 makes concrete.
Only after a change has passed tests, hooks and independent review does it reach the fourth and final gate: a human being who reads the reviewer's report and the change, exercises judgement the earlier gates cannot, and owns the decision to merge.
The ordering matters as much as the membership.
Cheap mechanical gates run first and reject the majority of defects at near-zero cost, so that the expensive gates — the reviewer agent's tokens and, above all, the human's attention — are spent only on changes that have already cleared everything an automated check can decide (high confidence in the ordering principle; it is standard continuous-integration practice carried into an agentic setting).

> **In plain terms — Pre-commit hook.** A small check that runs automatically the moment you try to save a change into version control, before the change is recorded. If the check fails — badly formatted code, a leftover password, a broken test — the save is refused until you fix it. It is a gate that needs no one to remember to open it.

> **In plain terms — Pull request (merge request).** A proposal to fold a set of changes into the shared main line of work, which the version-control platform presents as a line-by-line difference for review. Comments attach to the exact lines they concern, the author answers or revises, and nothing lands until the accountable owner accepts the result. In this book's workflows it is the surface on which a scientist reads, questions and finally signs off an agent's work.

The gates above govern correctness, not authority, and the two have to be designed together, because an agent that writes and runs code is executing arbitrary instructions on a machine with access to data, credentials and compute.
The full treatment of that authority model — least-privilege tool access and why it matters — is Chapter 12's; what belongs here is the shape it imposes on this pipeline.
The reviewer agent should run with read-only access to the change and no power to approve, merge or alter it, so its role stays strictly advisory and a compromised or manipulated reviewer cannot wave work through.
The author agent should operate in an environment scoped to the task — a working branch, a sandboxed interpreter, credentials limited to what the pipeline genuinely needs — so a mistaken or injected instruction has a bounded blast radius.
The point to carry forward is simply that the gate stack of Figure 7.1 assumes an authority model underneath it: a governed pipeline is governed in both senses, correctness and permission, or it is neither (Chapter 12).

**Figure 7.1 — The gate stack.** *A figure brief follows `FIGURES.md`; render in the house style.*

```
FIGURE BRIEF
- id:            Figure 7.1
- title:         Four gates between an agent's code and the main branch
- type:          architecture
- claim:         An agent's code is trusted only after passing successive independent gates — tests, hooks, an independent reviewer agent — with an accountable human owning the final merge.
- canvas:        16:9
- elements:      left, an "author agent" rounded square (orange, with loop-arrow icon)
                 emitting a "proposed change" artefact (sky-blue document glyph); then a
                 left-to-right series of three gates, each a vermillion diamond —
                 "automated tests", "pre-commit hooks", "independent reviewer agent"
                 (the third also carrying the reviewer icon, purple, head-and-shoulders
                 with a tick); finally a blue "human owner" head-and-shoulders icon at the
                 right; a sky-blue "main branch" cylinder beyond the human
- flow:          left-to-right — author agent → proposed change → tests gate → hooks gate →
                 reviewer-agent gate → human owner → main branch; each gate has a "fail"
                 exit curving back to the author agent
- labels:        "author agent", "proposed change", "automated tests", "pre-commit hooks",
                 "independent reviewer agent", "human owner", "main branch", "fail"
- annotations:   a light grey bracket under the three diamonds labelled "cheap gates first";
                 a small note by the reviewer agent "read-only, advisory"
- caption:       Figure 7.1 — The gate stack. Cheap mechanical gates run first and reject most defects at near-zero cost; the independent reviewer agent and the human owner, both expensive, are spent only on changes that have already cleared them. The human owns the merge; the reviewer agent is advisory and read-only.
- alt-text:      An architecture diagram reading left to right. An orange author agent emits a proposed-change document that passes through three vermillion diamond gates in turn — automated tests, pre-commit hooks, and an independent reviewer agent shown with a purple reviewer icon — before reaching a blue human owner who merges to the main-branch cylinder. Each gate has a fail arrow curving back to the author agent. A bracket under the gates reads cheap gates first; a note by the reviewer reads read-only, advisory.
- generator prompt: A flat vector architecture diagram on an off-white background, flowing
                 left to right. At the left, an orange rounded square with a small loop
                 arrow, labelled "author agent", connects to a sky-blue document glyph
                 labelled "proposed change". From there a single near-black line passes
                 through three vermillion diamonds in sequence, labelled "automated tests",
                 "pre-commit hooks", and "independent reviewer agent"; the third diamond
                 also shows a small purple head-and-shoulders icon with a tick. Each diamond
                 has a thin "fail" arrow curving back to the author agent. After the third
                 diamond the line reaches a blue head-and-shoulders icon labelled "human
                 owner", then a sky-blue cylinder labelled "main branch". A light grey
                 bracket under the three diamonds is labelled "cheap gates first"; a small
                 grey note beside the reviewer diamond reads "read-only, advisory". Minimal
                 text, generous spacing, single-weight lines.
```

**Figure 7.2 — Notebook versus governed pipeline.** *A figure brief follows `FIGURES.md`; render in the house style.*

```
FIGURE BRIEF
- id:            Figure 7.2
- title:         From exploratory notebook to governed pipeline
- type:          before/after
- claim:         The governed pipeline adds tests, hooks, independent review and human ownership to the same analytical steps, converting a run-once artefact into a repeatable, auditable one.
- canvas:        16:9
- elements:      top row "before" — a single grey rounded rectangle labelled "notebook"
                 containing an unordered cluster of small cells (load, regrid, threshold,
                 plot) with one grey arrow "looked reasonable → shared"; bottom row "after"
                 — the same four steps as an ordered green tool chain inside a workflow
                 border, feeding an orange "author agent", then the three vermillion gate
                 diamonds and a blue "human owner", with a sky-blue "version control"
                 cylinder beneath
- flow:          top: loose cluster to a single output; bottom: left-to-right ordered
                 chain through gates to human owner, all under version control
- labels:        "notebook", "load", "regrid", "threshold", "plot", "looked reasonable",
                 "governed pipeline", "tests", "hooks", "independent review", "human owner",
                 "version control"
- annotations:   a vermillion callout on the top row "no independent reader"; a matching
                 callout on the bottom row "reader before merge"
- caption:       Figure 7.2 — The same analytical steps before and after governance. The redesign does not change the science; it adds the tests, hooks, independent review and human ownership that turn a run-once notebook into a pipeline whose outputs can be reproduced and audited.
- alt-text:      A before-and-after diagram. The top half shows a grey notebook box with an unordered cluster of cells — load, regrid, threshold, plot — and a single arrow labelled looked reasonable, annotated in vermillion as no independent reader. The bottom half shows the same four steps as an ordered green tool chain feeding an orange author agent, then three vermillion gate diamonds for tests, hooks and independent review, then a blue human owner, all sitting above a sky-blue version-control cylinder and annotated reader before merge.
- generator prompt: A flat vector before/after diagram on an off-white background, two
                 stacked rows sharing a visual grammar. Top row: a grey-bordered rounded
                 rectangle labelled "notebook" containing four small scattered cell boxes
                 labelled "load", "regrid", "threshold", "plot" in no clear order, with a
                 single grey arrow leaving it labelled "looked reasonable"; a vermillion
                 callout points to it reading "no independent reader". Bottom row: the same
                 four labels as an ordered horizontal chain of green tool boxes inside a
                 grey workflow border labelled "governed pipeline", feeding an orange
                 rounded square "author agent", then three vermillion diamonds labelled
                 "tests", "hooks", "independent review", then a blue head-and-shoulders icon
                 "human owner"; a sky-blue cylinder labelled "version control" sits beneath
                 the row; a vermillion callout reads "reader before merge". Minimal text,
                 generous spacing, single-weight lines, single-direction flow in each row.
```

## 7.4 Worked example: a governed pipeline with hooks and sub-agents

The example that runs through this section takes a real exploratory analysis from my own operational work and follows it through the redesign, so the gates are concrete rather than abstract.
The starting point is a notebook that ingests an ensemble precipitation forecast and a set of river-gauge observations, aligns them in space and time, and computes a verification score used to judge the forecast against what was observed — the kind of analysis that begins as a one-off and is then wanted every forecast cycle.
**[AUTHOR: specify the actual analysis — the forecast product, the gauge network, the verification metric, and the operational cadence at which it needed to run — so the example is grounded in the executed work rather than this generic stand-in.]**
The task I hand to the workflow is not "write this analysis" but "turn this notebook into a governed pipeline", and that distinction shapes everything that follows.
The objective, inputs, acceptance criteria and stop conditions are specified first, in the manner of Chapter 3, so that both the author agent and every gate downstream are judged against a fixed target rather than against whatever the agent decided to build.

The construction proceeds gate by gate, and the order in which the pieces are built is itself part of the method.
First, I pin down the intended behaviour as tests before any refactoring begins: a small set of assertions that a known forecast–observation pair produces a known score, that missing gauge values are excluded rather than treated as zero, that the spatial alignment conserves the total where it should, and that an out-of-range input is rejected with a clear error rather than a silent NaN.
**[AUTHOR: give the two or three properties from the real analysis whose violation you would most want caught — the ones that would have burned you, or did.]**
These tests are written against the specification, and where the agent proposes them I read them before accepting them, because a test the agent both writes and satisfies asserts only that the code does what the code does.
Second, the pre-commit hooks are configured to run formatting, linting, type checking, a secrets-and-large-file scan and the full test suite on every commit, so the mechanical gates are enforced automatically and cannot be forgotten under deadline.
Third — and this is the step that distinguishes the design — the review is performed by a *separate* reviewer sub-agent before any human sees the change: a distinct agent instance, given the change, the specification and a review checklist, and told to report problems rather than to praise, with no ability to alter or approve the work.
I read that report last, against the change itself, and remain the sole authority who merges.
The division of labour is worth stating plainly, because it is the chapter's central practical claim: the author agent proposes, the tests and hooks dispose of the mechanical failures, the independent reviewer agent surfaces the substantive ones, and the human decides — spending scarce attention on judgement rather than on the routine checking the earlier gates have already done (moderate-to-high confidence; the pattern is sound, the effort saved varies with task and model).
**[AUTHOR: report what actually happened when you ran this — which gate caught what, how much the reviewer sub-agent found that the tests missed, and the one issue, if any, that only the human caught. A single real trace here is worth more than the whole preceding paragraph.]**

**Figure 7.3 — The reviewer sub-agent before human review.** *A figure brief follows `FIGURES.md`; render in the house style.*

```
FIGURE BRIEF
- id:            Figure 7.3
- title:         A separate reviewer agent reads the change before the human does
- type:          sequence
- claim:         Independent review means a different agent instance, with its own context and no stake in the work, reports on the change before the accountable human reviews it.
- canvas:        16:9
- elements:      four vertical actor lanes read top-to-bottom — "author agent" (orange),
                 "tests + hooks" (vermillion), "reviewer agent" (purple, reviewer icon),
                 "human owner" (blue); numbered horizontal messages between them
- flow:          top-to-bottom, numbered 1–6: (1) author agent → tests+hooks: "submit
                 change"; (2) tests+hooks → author agent: "fail — fix" (a return arrow) or
                 pass; (3) tests+hooks → reviewer agent: "pass: review this"; (4) reviewer
                 agent → reviewer agent: "read change vs specification" (self-loop);
                 (5) reviewer agent → human owner: "findings report"; (6) human owner →
                 main branch: "merge (owns decision)"
- labels:        "author agent", "tests + hooks", "reviewer agent", "human owner",
                 "submit change", "fail — fix", "pass: review this",
                 "read change vs specification", "findings report", "merge — owns decision"
- annotations:   a note on the reviewer lane "different instance · read-only · no approve";
                 a vermillion note between reviewer and human "advisory, not a gate the
                 agent can open"
- caption:       Figure 7.3 — The reviewer sub-agent sits between the automated gates and the human. It is a different agent instance with its own context and no ability to approve or merge; it reports findings, and the human owner alone decides.
- alt-text:      A top-to-bottom sequence diagram with four lanes — orange author agent, vermillion tests and hooks, purple reviewer agent, and blue human owner. Numbered messages show the author submitting a change, tests and hooks either failing back to the author or passing it to the reviewer agent, the reviewer reading the change against the specification, sending a findings report to the human owner, and the human merging as the owner of the decision. Notes mark the reviewer as a different read-only instance that cannot approve.
- generator prompt: A flat vector sequence diagram on an off-white background, read top to
                 bottom, with four labelled vertical lanes: "author agent" (orange), "tests
                 + hooks" (vermillion), "reviewer agent" (purple, with a small
                 head-and-shoulders-plus-tick icon), "human owner" (blue). Numbered
                 horizontal arrows in order: 1 author agent to tests+hooks "submit change";
                 2 a return arrow tests+hooks to author agent "fail — fix"; 3 tests+hooks to
                 reviewer agent "pass: review this"; 4 a small self-loop on the reviewer
                 agent "read change vs specification"; 5 reviewer agent to human owner
                 "findings report"; 6 human owner to a sky-blue "main branch" "merge — owns
                 decision". A grey note on the reviewer lane reads "different instance ·
                 read-only · no approve". Minimal text, single-weight lines, one arrowhead
                 style, generous spacing.
```

## 7.5 Failure modes

The first and most consequential failure mode is plausible-but-wrong code that passes weak tests, because it is the failure the whole gate stack exists to catch and the one it most often misses.
An agent asked to write both the code and its tests will, absent a specification written against intended behaviour, produce tests that encode the code's actual behaviour rather than its correct behaviour.
So a transposed latitude and longitude, a metre-per-second field read as millimetres, or a fill value silently averaged into a mean will pass a green test suite whose assertions were derived from the very output they should have caught.
The defence is not more tests written by the same agent but tests written against an independent statement of what the code must do — the specification, physical conservation properties, known-answer cases from the literature, and cross-checks against an independent implementation — plus the discipline of a human reading the tests, not merely watching them pass.
This is the same principle Chapter 11 builds its evaluation methods on, and the plausible failure Chapter 1 named: verification has to be external to the thing it verifies.
It is worth being honest that even execution-based gates are not exempt from it.
Audits of the very benchmarks that grade coding agents have found that insufficient test coverage lets some wrong solutions pass as correct — an execution-grounded gate still has a false-negative rate, and that rate is set by the quality of the tests behind it (Zhu et al., 2025).
A green suite tells you the code does what the suite asserts; it tells you nothing about whether the suite asserts the right thing (high confidence; this is the dominant failure mode of agent-written code).

The second failure mode is silent behavioural drift, in which a pipeline keeps running and producing plausible output while its behaviour changes underneath it.
A dependency updates and alters a default; an input format shifts a column; a regridding library changes how it handles edges — and no error is raised, because nothing is broken in a way the code checks for.
Agentic development makes this both more likely and more tractable: more likely because agents readily update dependencies and refactor internals in ways whose behavioural consequences are not obvious, and more tractable because the same agents can cheaply maintain the regression tests and pinned environments that catch drift when it happens.
The defence is characterisation: a fixed reference input whose correct output is recorded and asserted on every run, a declared and version-locked environment, and an alert when a numerical result moves beyond a stated tolerance — so drift announces itself as a failed assertion rather than surfacing months later as an unexplained shift in a published time series (moderate confidence; the mechanisms are standard, their sufficiency depends on the reference cases chosen).
**[AUTHOR: an instance of drift you have seen bite — a library or format change that silently altered a result — would anchor this more firmly than the general statement.]**

> **In plain terms — Regression test.** A test that pins down behaviour you have already confirmed is correct, by recording the output for a fixed input and asserting it again on every future run. Its whole job is to catch the day something quietly changes — a library update, a refactor — that would otherwise slip through unnoticed. It does not ask whether the answer is right in the abstract, only whether it still matches what you signed off before.

The third failure mode is over-agreeable review, and it is the specific reason this chapter insists the reviewer be a separate agent rather than the author agent checking its own work.
The anatomy of the behaviour — why a model asked to assess work tilts towards ratifying it — is the failure gallery's to dissect (Chapter 13), and the countermeasure at roster scale is Chapter 10's; here I only need its consequence for a coding pipeline and the configuration that answers it.
The consequence is simple: ask an agent "is this correct?" straight after it has produced the thing, and you invite the answer it has already given.
Even a separate reviewer instance tilts towards agreement if it is prompted to evaluate rather than to find fault, or if it is handed the author's reasoning as authoritative context.
So the reviewer is instantiated separately with its own clean context, charged explicitly with finding problems against a checklist rather than with judging acceptability, given no stake in defending the work, and held read-only with no merge rights — and, where the stakes justify the cost, more than one reviewer with different instructions, as Chapter 10 develops.
The limitation I have to state plainly is that none of this makes the reviewer agent reliable in the way a check on a conservation law is reliable: it lowers the rate of over-agreeable review, it does not abolish it, and it is for exactly this residual that the human reviewer remains the owner of the decision and not a rubber stamp on the agent's approval (high confidence in the direction, low-to-moderate confidence in any specific reduction figure, which is model- and task-dependent).

**Figure 7.4 — How plausible-but-wrong code clears a weak suite.** *A figure brief follows `FIGURES.md`; render in the house style.*

```
FIGURE BRIEF
- id:            Figure 7.4
- title:         A self-tested error passes; an independent test catches it
- type:          failure trace
- claim:         Tests written by the same agent that wrote the code assert the code's actual behaviour, so a plausible error passes; a test written against intended behaviour catches it.
- canvas:        16:9
- elements:      a single top-to-bottom trace: orange "author agent" writes a "regrid step"
                 (green tool box) with a hidden defect (vermillion mark: "lat/lon
                 transposed"); it also writes a "self-derived test" (grey) that shows a
                 green pass; below, a branch to an "independent test — conservation check"
                 (vermillion diamond) that shows a red fail and a return arrow to the author
                 agent
- flow:          top-to-bottom: author agent → regrid step (defect) → self-derived test
                 (pass, misleading) ; parallel branch → independent conservation test
                 (fail, correct) → back to author agent
- labels:        "author agent", "regrid step", "lat/lon transposed", "self-derived test",
                 "pass", "independent test — conservation check", "fail", "fix"
- annotations:   a vermillion callout at the self-derived test "asserts what the code does,
                 not what it should"; a vermillion callout at the independent test "asserts
                 intended behaviour — catches it"
- caption:       Figure 7.4 — The dominant failure of agent-written code. A test the agent derives from its own output ratifies a transposed-coordinate error; a test written against an intended property — here conservation of the regridded total — is what actually catches it. The green suite is necessary and not sufficient.
- alt-text:      A top-to-bottom failure trace. An orange author agent writes a green regrid-step box carrying a vermillion defect marked lat/lon transposed, and also writes a grey self-derived test that shows a misleading green pass, annotated asserts what the code does not what it should. A parallel branch shows an independent conservation-check test as a vermillion diamond returning a red fail and an arrow back to the author agent, annotated asserts intended behaviour, catches it.
- generator prompt: A flat vector failure-trace diagram on an off-white background, read top
                 to bottom. An orange rounded square labelled "author agent" connects down
                 to a green tool box labelled "regrid step" carrying a small vermillion mark
                 labelled "lat/lon transposed". From the regrid box, one arrow goes to a
                 grey box labelled "self-derived test" showing a green tick and the word
                 "pass", with a vermillion callout "asserts what the code does, not what it
                 should". A second arrow branches to a vermillion diamond labelled
                 "independent test — conservation check" showing a red cross and the word
                 "fail", with a vermillion callout "asserts intended behaviour — catches
                 it", and a return arrow curving back up to the author agent labelled "fix".
                 Minimal text, single-weight lines, generous spacing.
```

## 7.6 Verification checklist

This checklist follows the gate stack and applies to any change an agent proposes, whatever the tool or language; a colleague who did not build the pipeline should be able to run down it and confirm each item.

- **Specification before code.** The intended behaviour of the change is written down first, as an objective with acceptance criteria a human can check, so every downstream gate judges against a fixed target rather than against the agent's own output (Chapter 3).
- **Tests assert intended, not observed, behaviour.** The assertions encode what the code should do and include at least one property derived independently of the code — a conservation law, a known-answer case, or a cross-check against a separate implementation — and a human has read the tests, not merely seen them pass.
- **Hooks enforce the mechanical gates.** Formatting, linting, type checking, a secrets-and-large-file scan and the full test suite run automatically on every commit, so no change reaches shared history without clearing them.
- **Review is genuinely independent.** The reviewer is a different agent instance from the author, with its own clean context, charged with finding faults against a checklist, running read-only with no power to approve or merge — and, where stakes justify it, more than one such reviewer with differing instructions (Chapter 10).
- **Drift is made to announce itself.** A fixed reference input has a recorded correct output asserted on every run, the environment is declared and version-locked, and a result moving beyond a stated tolerance raises an alert rather than passing quietly.
- **Authority is scoped, not assumed.** The author agent runs in a task-scoped environment with least-privilege credentials, the reviewer agent runs read-only, and neither can merge — the design governs permission as well as correctness (Chapter 12).
- **A human owns the merge.** An accountable person reads the reviewer's report and the change, exercises the judgement the earlier gates cannot, and owns the decision; the agents propose and check, the human decides.

A workflow that satisfies these seven has more assurance than most hand-written research code ever receives; a workflow that skips any of them has, at that gate, the fragility the notebook had.

## 7.7 Repository pointer

The companion repository holds the runnable form of this chapter under `/patterns/ch07-coding-and-pipeline-agents`, where the perishable specifics print cannot carry are kept current.
**[AUTHOR: confirm the final path and contents.]**
The intended contents are a minimal governed-pipeline template — the notebook-to-pipeline refactor of §7.4 reduced to a small self-contained example — together with a pre-commit hook configuration, an independent-reviewer sub-agent specification and review checklist, and the tests that encode intended behaviour, including at least one independent property check.
Named tools, versions and the current model configuration live there rather than in this text, per the vendor-neutral convention, because they date on a cycle print cannot follow.
The durable pattern is the gate stack of Figure 7.1; the repository is where it is instantiated in whatever tooling is current at the time of reading.
The exercises for this chapter, in `/exercises`, ask you to take one of your own run-once notebooks through the four gates and record which gate caught what — the same trace the worked example asks of me.
**[verify: confirm repository layout and exercise set before release.]**

---

### References (verify details before release)

- Jimenez, C. E., Yang, J., Wettig, A., Yao, S., Pei, K., Press, O. and Narasimhan, K. (2023). SWE-bench: can language models resolve real-world GitHub issues? *ICLR 2024*. https://arxiv.org/abs/2310.06770
- Zhu, Y., Jin, T., Pruksachatkun, Y., et al. (2025). Establishing best practices for building rigorous agentic benchmarks. *arXiv preprint*. https://arxiv.org/abs/2507.02825
