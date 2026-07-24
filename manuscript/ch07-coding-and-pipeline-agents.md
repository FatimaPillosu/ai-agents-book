# Chapter 7 — Coding and pipeline agents

> **Status:** draft · figures specified as briefs per `FIGURES.md`. Chapter lengths are indicative guidance, not fixed allocations.
> **Conventions:** vendor-neutral per outline §9. Passages needing the author's lived material or number verification are tagged **[AUTHOR: …]** or **[verify]**. No anecdotes, statistics or results have been invented; the worked example is scaffolded and its specifics are the author's to supply.

---

## 7.1 The problem: code that works once is not a pipeline

The characteristic software artefact of environmental research is a notebook that ran correctly once, on one machine, for one dataset, and was never expected to run again. Exploratory analysis rewards exactly this: a scientist loads a forecast field, tries a regridding step, plots the result, adjusts a threshold, and moves on, accumulating cells in the order the investigation happened to take rather than the order a reader would need to follow. The value of that mode is real and should not be disparaged, because it is how understanding is built; the difficulty is that the same artefact is then pressed into service as though it were a pipeline — rerun next season, handed to a student, cited as the method behind a figure, or scheduled to produce an operational product — without acquiring any of the properties that would make it trustworthy in that role. Those properties are well understood and predate agents entirely: version control, tests that assert what the code is supposed to do, a fixed and declared environment, separation of configuration from logic, and a review step performed by someone other than the author. The gap between the notebook and the governed pipeline is not a gap in cleverness but a gap in discipline, and it is a gap that most working scientists know they should close and mostly do not, because closing it costs hours that the next deadline has already claimed. Agents change the economics of that gap in both directions at once, and the change is the subject of this chapter: they lower the cost of writing the tests, hooks and scaffolding that a governed pipeline needs, and they simultaneously raise the cost of not having them, because an agent will generate plausible code far faster than an unaided human can read it, and volume of plausible-but-unverified code is precisely the thing a research group least needs more of (high confidence).

The reframing this chapter argues for is that the unit of work is not the code an agent produces but the set of gates that code must pass before it is trusted. A scientist who asks an agent to "write the regridding step" and then reads the result has substituted the agent for a colleague and changed very little; a scientist who builds a workflow in which the agent's output must pass automated tests, then pre-commit hooks, then an independent reviewer agent, and only then reaches a human reviewer who owns the decision, has built something with more assurance than most hand-written research code ever receives. The claim is not that gates make agent-written code safe in an absolute sense, because no arrangement of automated checks catches a plausible error that every check was too weak to notice; the claim is that the discipline agents make affordable is the same discipline good software engineering has always prescribed, and that the correct response to a fast, fallible code generator is to build the verification the field already knew it should have. This chapter connects the loop and tools of Chapter 2 to the multi-agent review of Chapter 10 and the evaluation methods of Chapter 11, and treats the governed pipeline as the concrete setting in which those ideas first pay for themselves.

## 7.2 The conventional workflow and where it breaks

The conventional path from notebook to production in a research group, where any path exists at all, is a sequence of manual acts of translation that depend on the same person's diligence at every step. A scientist who decides that an analysis deserves to become a reusable tool typically refactors the notebook into scripts by hand, adds a handful of tests if time allows, writes a README, and — in the better-run groups — opens a merge request for a colleague to review before it lands on the main branch. Each of these steps is skippable, and under deadline each is skipped in a predictable order: the tests go first, because they are the part with no immediately visible output, then the review shrinks to a glance, then the environment specification is left implicit in whatever happened to be installed, until what reaches the shared repository is a lightly tidied notebook with the notebook's fragility intact. The failure is not one of knowledge, since the scientists involved can usually recite the practice they are omitting; it is that the practice is front-loaded effort against a back-loaded and uncertain payoff, and human attention discounts the future steeply. The consequence for environmental science specifically is a literature and an operational estate resting on code that has never been independently read, whose correctness is asserted by the fact that its outputs looked reasonable, and whose silent errors — a transposed coordinate, a unit left unconverted, a fill value treated as data — surface, when they surface at all, as anomalies in a downstream result that someone else has to chase (moderate confidence; the prevalence is widely discussed but not systematically measured).

The specific weakness that agents both expose and can help repair is the absence of an independent reader. A human author is the worst possible reviewer of their own code, because the same misunderstanding that produced an error also renders its author unable to see it; this is why software engineering treats review by a second person as non-negotiable and why science treats peer review as constitutive rather than optional. Research groups are frequently too small, too specialised or too pressed to supply that second reader for routine code, with the result that most research code is merged on the author's word alone. An agent cannot replace the accountable human reviewer, and this chapter is emphatic that it must not be asked to; what it can do is occupy the role of the tireless first reader who never skips the review because it is late on a Friday, applying a consistent checklist to every change and surfacing the ten routine issues so that the human's scarce attention lands on the one that matters. That is a genuine addition to a workflow that presently has nothing in the slot at all, and it is the redesign the next section sets out.

## 7.3 The agentic redesign: successive gates, human at the end

The redesign replaces a single act of trust with a series of independent gates, each cheaper than the human review it protects and each catching a different class of error. The first gate is the automated test suite, which asserts what the code must do — that a known input produces a known output, that a conservation property holds, that an edge case is handled — and which the agent writes alongside the code but which derives its authority from being specified against the intended behaviour rather than the produced behaviour. The second gate is the set of pre-commit hooks, which run automatically whenever a change is committed and enforce the mechanical properties that need no judgement: formatting, linting, type checks, a scan for secrets and large files, and the test suite itself, so that nothing reaches the shared history without passing them. The third gate is an independent reviewer agent — and the word independent is load-bearing — which reads the proposed change against a review specification and reports what it finds, but which is deliberately a *different* agent instance from the one that wrote the code, with its own context, its own instructions and no stake in defending the work, for reasons the failure modes in §7.5 make concrete. Only after a change has passed tests, hooks and independent review does it reach the fourth and final gate, which is a human being who reads the reviewer's report and the change, exercises judgement the earlier gates cannot, and owns the decision to merge. The ordering matters as much as the membership: cheap mechanical gates run first and reject the majority of defects at near-zero cost, so that the expensive gates — the reviewer agent's tokens and, above all, the human's attention — are spent only on changes that have already cleared everything an automated check can decide (high confidence in the ordering principle; it is standard continuous-integration practice applied to an agentic setting).

> **In plain terms — Pull request (merge request).** A proposal to fold a set of changes into the shared main line of work, which the version-control platform presents as a line-by-line difference for review. Comments attach to the exact lines they concern, the author answers or revises, and nothing lands until the accountable owner accepts the result. In this book's workflows it is the surface on which a scientist reads, questions and finally signs off an agent's work.

The security and least-privilege dimension of this arrangement is developed in Chapter 12, but its outline belongs here because it constrains the design. An agent that writes and runs code is an agent executing arbitrary instructions on a machine with access to data, credentials and compute, and the gates above govern correctness, not authority; the two must be designed together. The reviewer agent should run with read-only access to the change under review and no ability to approve, merge or alter it, so that its role is strictly advisory and a compromised or manipulated reviewer cannot wave work through. The author agent should operate in an environment scoped to the task — a working branch, a sandboxed interpreter, credentials limited to what the pipeline genuinely needs — so that a mistaken or injected instruction has a bounded blast radius. These are not agent-specific inventions but the ordinary principle of least privilege, and the point to carry forward is that the gate stack of Figure 7.1 assumes an authority model underneath it; a governed pipeline is governed in both senses, correctness and permission, or it is neither.

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

The example that runs through this section takes a real exploratory analysis from the author's operational work and follows it through the redesign, so that the gates are concrete rather than abstract. The starting point is a notebook that ingests an ensemble precipitation forecast and a set of river-gauge observations, aligns them in space and time, and computes a verification score used to judge the forecast against what was observed — the kind of analysis that begins as a one-off investigation and is then wanted every forecast cycle. **[AUTHOR: specify the actual analysis — the forecast product, the gauge network, the verification metric, and the operational cadence at which it needed to run — so the example is grounded in the executed work rather than this generic stand-in.]** The task handed to the workflow is not "write this analysis" but "turn this notebook into a governed pipeline", and the distinction shapes everything that follows: the objective, inputs, acceptance criteria and stop conditions are specified first, in the manner of Chapter 3, so that both the author agent and every gate downstream are judged against a fixed target rather than against whatever the agent decided to build.

The construction proceeds gate by gate, and the order in which the pieces are built is itself part of the method. First, the intended behaviour is pinned down as tests before the refactoring begins: a small set of assertions that a known forecast–observation pair produces a known score, that missing gauge values are excluded rather than treated as zero, that the spatial alignment conserves the total where it should, and that an out-of-range input is rejected with a clear error rather than a silent NaN **[AUTHOR: give the two or three properties from the real analysis whose violation you would most want caught — the ones that would have burned you, or did]**. These tests are written against the specification, and where the agent proposes them they are read by the human before being accepted, because a test the agent both writes and satisfies asserts only that the code does what the code does. Second, the pre-commit hooks are configured to run formatting, linting, type checking, a secrets-and-large-file scan and the full test suite on every commit, so the mechanical gates are enforced automatically and cannot be forgotten under deadline. Third — and this is the step that distinguishes the design — the review is performed by a *separate* reviewer sub-agent before any human sees the change: a distinct agent instance, given the change, the specification and a review checklist, and instructed to report problems rather than to praise, with no ability to alter or approve the work. The human reads that report last, against the change itself, and remains the sole authority who merges. The division of labour that results is worth stating plainly, because it is the chapter's central practical claim: the author agent proposes, the tests and hooks dispose of the mechanical failures, the independent reviewer agent surfaces the substantive ones, and the human decides — spending scarce attention on judgement rather than on the routine checking that the earlier gates have already done (moderate-to-high confidence; the pattern is sound, the effort saved varies with task and model). **[AUTHOR: report what actually happened when you ran this — which gate caught what, how much the reviewer sub-agent found that the tests missed, and the one issue, if any, that only the human caught. A single real trace here is worth more than the whole preceding paragraph.]**

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

The first and most consequential failure mode is plausible-but-wrong code that passes weak tests, because it is the failure the whole gate stack exists to catch and the one it most often misses. An agent asked to write both the code and its tests will, absent a specification written against intended behaviour, produce tests that encode the code's actual behaviour rather than its correct behaviour, so that a transposed latitude and longitude, a metre-per-second field read as millimetres, or a fill value silently averaged into a mean will pass a green test suite whose assertions were derived from the very output they should have caught. The defence is not more tests written by the same agent but tests written against an independent statement of what the code must do — the specification, physical conservation properties, known-answer cases from the literature, and cross-checks against an independent implementation — and the discipline of having a human read the tests, not merely watch them pass (high confidence; this is the dominant failure mode of agent-written code and the reason Chapter 11 treats evaluation as external by construction). A suite that is green tells you the code does what the suite asserts; it tells you nothing about whether the suite asserts the right thing.

The second failure mode is silent behavioural drift, in which a pipeline continues to run and produce plausible output while its behaviour changes underneath — a dependency updates and alters a default, an input format shifts a column, a regridding library changes its handling of edges — and no error is raised because nothing is broken in a way the code checks for. Agentic development makes this both more likely and more tractable: more likely because agents readily update dependencies and refactor internals in ways whose behavioural consequences are not obvious, and more tractable because the same agents can cheaply maintain the regression tests and pinned environments that catch drift when it happens. The defence is characterisation: a fixed reference input whose correct output is recorded and asserted on every run, a declared and version-locked environment, and an alert when a numerical result moves beyond a stated tolerance — so that drift announces itself as a failed assertion rather than surfacing months later as an unexplained shift in a published time series (moderate confidence; the mechanisms are standard, their sufficiency depends on the reference cases chosen). **[AUTHOR: an instance of drift you have seen bite — a library or format change that silently altered a result — would anchor this more firmly than the general statement.]**

The third failure mode is over-agreeable review, and it is the specific reason this chapter insists the reviewer be a separate agent rather than the author agent asked to check its own work. A model prompted to review its own output tends towards ratification, because the same context and the same commitments that produced the code also frame its assessment, and current models are poor judges of their own correctness in any case; asking an agent "is this correct?" after it has just asserted that it is invites the answer it has already given. Even a separate reviewer instance tilts towards agreement if it is prompted to evaluate rather than to find fault, or if it is given the author's reasoning as authoritative context; the mitigations are to instantiate the reviewer separately with its own clean context, to charge it explicitly with finding problems against a checklist rather than with judging acceptability, to withhold from it any stake in defending the work, and — where the stakes justify the cost — to use more than one reviewer with different instructions, as Chapter 10 develops for multi-agent settings. The limitation to state honestly is that none of this makes the reviewer agent reliable in the way a check on a conservation law is reliable: it reduces the rate of over-agreeable review, it does not eliminate it, and it is for exactly this residual that the human reviewer remains the owner of the decision and not a rubber stamp on the agent's approval (high confidence in the direction, low-to-moderate confidence in any specific reduction figure, which is model- and task-dependent).

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

The checklist for a coding-and-pipeline workflow follows the gate stack and can be applied to any change an agent proposes, whatever the tool or language. First, on specification: the intended behaviour of the change is written down before the code, as an objective with acceptance criteria a human can check, so that every downstream gate judges against a fixed target rather than against the agent's own output (Chapter 3). Second, on tests: the assertions encode intended behaviour, not observed behaviour, and include at least one property derived independently of the code — a conservation law, a known-answer case, or a cross-check against a separate implementation — and a human has read the tests, not merely seen them pass. Third, on hooks: formatting, linting, type checking, a secrets-and-large-file scan and the full test suite run automatically on every commit, so no change reaches shared history without clearing the mechanical gates. Fourth, on independent review: the reviewer is a different agent instance from the author, with its own clean context, charged with finding faults against a checklist, running read-only with no power to approve or merge, and — where stakes justify it — more than one such reviewer with differing instructions (Chapter 10). Fifth, on drift: a fixed reference input has a recorded correct output asserted on every run, the environment is declared and version-locked, and results moving beyond a stated tolerance raise an alert rather than passing quietly. Sixth, on authority: the author agent runs in a task-scoped environment with least-privilege credentials, the reviewer agent runs read-only, and neither can merge — the design governs permission as well as correctness (Chapter 12). Seventh, and last, on ownership: an accountable human reads the reviewer's report and the change, exercises the judgement the earlier gates cannot, and owns the decision to merge; the agents propose and check, the human decides. A workflow that satisfies these seven has more assurance than most hand-written research code ever receives; a workflow that skips any of them has, at that gate, the fragility the notebook had.

## 7.7 Repository pointer

The companion repository holds the runnable form of this chapter under `/patterns/ch07-coding-and-pipeline-agents`, where the perishable specifics that print cannot carry are kept current. **[AUTHOR: confirm the final path and contents.]** The intended contents are a minimal governed-pipeline template — the notebook-to-pipeline refactor of §7.4 reduced to a small self-contained example — together with a pre-commit hook configuration, an independent-reviewer sub-agent specification and review checklist, and the tests that encode intended behaviour including at least one independent property check. Named tools, versions and the current model configuration live there rather than in this text, per the vendor-neutral convention, because they date on a cycle the print cannot follow; the durable pattern is the gate stack of Figure 7.1, and the repository is where it is instantiated in whatever tooling is current at the time of reading. The exercises for this chapter, in `/exercises`, ask the reader to take one of their own run-once notebooks through the four gates and to record which gate caught what — the same trace the worked example requests of the author. **[verify: confirm repository layout and exercise set before release.]**
