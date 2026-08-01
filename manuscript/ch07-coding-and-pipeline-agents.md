# Chapter 7 — Coding and pipeline agents

> **Status:** draft r4 · voice v5.0 (`STYLE.md` §1) · sentence-per-line per `STYLE.md` §10 · figures as briefs per `FIGURES.md`.
> **Conventions:** vendor-neutral (outline §9) · **[AUTHOR: …]** marks lived material only the author can supply · **[verify]** marks real but unconfirmed details · citations drawn only from verified reports in `/research`. Nothing has been invented.
> **Chapter note:** the worked example of §7.4 is scaffolded; its specifics are the author's to supply and no result has been invented.

---

## 7.1 The problem: code that works once is not a pipeline

The characteristic software artefact of environmental research is a notebook that ran correctly once, on one machine, for one dataset, and was never meant to run again.

Exploratory analysis rewards exactly that way of working.
You load a forecast field, try a regridding step, plot the result, nudge a threshold, and move on, accumulating cells in the order the investigation happened to take rather than the order a reader would need.
There is nothing wrong with that, because it is how understanding actually gets built.
The trouble starts when the same artefact gets pressed into service as though it were a pipeline: rerun next season, handed to a student, cited as the method behind a figure, or scheduled to produce an operational product, without picking up any of the properties that would make it trustworthy in that role.
Those properties are well understood and predate agents entirely: version control, tests that assert what the code is supposed to do, a fixed and declared environment, configuration kept separate from logic, and a review step done by someone other than the author.
The gap between the notebook and the governed pipeline is not a gap in cleverness.
It is a gap in discipline, and most working scientists know they should close it and mostly do not, because closing it costs hours the next deadline has already claimed.

Agents change the economics of that gap in both directions at once, which is what this chapter is about.
They lower the cost of writing the tests, hooks and scaffolding a governed pipeline needs.
They also raise the cost of not having them, because an agent will generate plausible code far faster than you can read it, and a pile of plausible-but-unverified code is precisely what a research group least needs more of (high confidence).

So the unit of work is not the code an agent produces.
It is the set of gates that code has to pass before anyone trusts it.
Ask an agent to "write the regridding step" and then read the result, and you have swapped the agent for a colleague and changed very little.
Build a workflow where the agent's output must pass automated tests, then pre-commit hooks, then an independent reviewer agent, and only then reach a human who owns the decision, and you have built something with more assurance than most hand-written research code ever receives.
None of that makes agent-written code safe in any absolute sense, because no arrangement of automated checks catches a plausible error every check was too weak to notice.
The claim is narrower and more useful: the discipline agents make affordable is the same discipline good software engineering always prescribed, and the right response to a fast, fallible code generator is to build the verification the field already knew it should have.
This chapter connects the loop and tools of Chapter 2 to the multi-agent review of Chapter 10 and the evaluation methods of Chapter 11, and treats the governed pipeline as the first place those ideas pay for themselves.

## 7.2 The conventional workflow and where it breaks

The conventional path from notebook to production, in the rare group where any path exists at all, is a sequence of manual translations that lean on the same person's diligence at every step.

You decide an analysis deserves to become a reusable tool, so you refactor the notebook into scripts by hand, add a handful of tests if time allows, write a README, and, in the better-run groups, open a merge request for a colleague to review before it lands on the main branch.
Every one of those steps is skippable, and under deadline each gets skipped in a predictable order.
The tests go first, because they are the part with no immediately visible output.
Then the review shrinks to a glance.
Then the environment specification is left implicit in whatever happened to be installed.
What reaches the shared repository is a lightly tidied notebook with the notebook's fragility intact.
This is not a failure of knowledge: the scientists involved can usually recite the practice they are omitting.
It is that the practice is effort now against an uncertain payoff later, and human attention discounts the future steeply.
The consequence for environmental science is a literature and an operational estate resting on code nobody has independently read, whose correctness is asserted by its outputs looking reasonable, and whose silent errors (a transposed coordinate, a unit left unconverted, a fill value treated as data) surface, if they surface at all, as anomalies in a downstream result somebody else has to chase (moderate confidence; the prevalence is widely discussed but not systematically measured).

The weakness agents both expose and can help repair is the missing independent reader.
You are the worst possible reviewer of your own code, because the same misunderstanding that produced the error also stops you seeing it.
That is why software engineering treats review by a second person as non-negotiable, and why science treats peer review as constitutive rather than optional.
Research groups are frequently too small, too specialised or too pressed to supply that second reader for routine code, so most research code gets merged on the author's word alone.
An agent cannot replace the accountable human reviewer, and this book is emphatic that it must not be asked to.
What it can be is the tireless first reader that never skips the review because it is late on a Friday, applying a consistent checklist to every change and surfacing the ten routine issues so your scarce attention lands on the one that matters.
That is a genuine addition to a workflow that currently has nothing in that position at all, and it is the redesign the next section sets out.

## 7.3 The agentic redesign: successive gates, human at the end

The redesign replaces a single act of trust with a series of independent gates, each cheaper than the human review it protects, each catching a different class of error.

The first gate is the automated test suite.
It asserts what the code must do: that a known input produces a known output, that a conservation property holds, that an edge case is handled.
The agent may write those tests alongside the code, but their authority comes from being specified against intended behaviour rather than produced behaviour.
This is not exotic.
It is the discipline that made coding agents measurable in the first place.
The benchmark that tracks their progress on real software-repository issues judges a proposed fix by running the repository's own pre-existing test suite, so the acceptance criterion exists before the agent runs, is automated, and does not depend on any model's opinion (Jimenez et al., 2023).
That is exactly the property a scientific pipeline's tests need.

The second gate is the set of pre-commit hooks, which run automatically whenever a change is committed and enforce the mechanical properties that need no judgement: formatting, linting, type checks, a scan for secrets and large files, and the test suite itself, so nothing reaches the shared history without passing them.

The third gate is an independent reviewer agent, and the word independent is doing real work there.
It reads the proposed change against a review specification and reports what it finds, and it is deliberately a *different* agent instance from the one that wrote the code, with its own context, its own instructions and no stake in defending the work, for reasons §7.5 makes concrete.

Only after a change has passed tests, hooks and independent review does it reach the fourth and last gate: a human who reads the reviewer's report and the change, exercises the judgement the earlier gates cannot, and owns the decision to merge.
The ordering matters as much as the membership.
Cheap mechanical gates run first and reject most defects at near-zero cost, so the expensive gates, meaning the reviewer agent's tokens and above all the human's attention, are spent only on changes that have already cleared everything an automated check can decide (high confidence in the ordering principle; it is standard continuous-integration practice carried into an agentic setting).

> **Definition — Pre-commit hook.** A small check that runs automatically the moment a change is saved into version control, before the change is recorded. When the check fails, whether on badly formatted code, a leftover password or a broken test, the save is refused until the fault is corrected. It is a gate that needs no one to remember to open it.

> **Definition — Pull request (merge request).** A proposal to fold a set of changes into the shared main line of work, which the version-control platform presents as a line-by-line difference for review. Comments attach to the exact lines they concern, the author answers or revises, and nothing lands until the accountable owner accepts the result. In this book's workflows it is the surface on which a scientist reads, questions and finally signs off an agent's work.

Those gates govern correctness, not authority, and the two have to be designed together, because an agent that writes and runs code is executing arbitrary instructions on a machine with access to data, credentials and compute.
The full treatment of that authority model, meaning least-privilege tool access and why it matters, is Chapter 12's.
What belongs here is what it demands of this pipeline.
The reviewer agent should run with read-only access to the change and no power to approve, merge or alter it, so its role stays strictly advisory and a compromised or manipulated reviewer cannot wave work through.
The author agent should work in an environment scoped to the task, meaning a working branch, a sandboxed interpreter, and credentials limited to what the pipeline genuinely needs, so a mistaken or injected instruction can only do bounded damage.
Carry this forward: the gate stack of Figure 7.1 assumes an authority model underneath it.
A governed pipeline is governed in both senses, correctness and permission, or it is neither (Chapter 12).

**Figure 7.1 — The gate stack.**

![A left-to-right architecture diagram. An author agent emits a proposed change, which meets four gates in turn. First a vermillion automated-tests diamond, annotated that the assertions have to encode intended behaviour, not whatever the code happens to do. Second a pre-commit hooks diamond, annotated as formatting, linting, type checks, a secrets scan and the test suite, run automatically so nobody can forget them. Third an independent reviewer agent carrying a purple reviewer icon, annotated as a different instance with its own context, read-only, with no power to approve or merge. Fourth a blue human owner, annotated as reading the reviewer's report and owning the decision to merge. Each gate has a fail exit curving back to the author agent. A bracket under the first three reads that the cheap mechanical gates run first so the expensive human attention is spent only on what has already cleared them.](../figures/figure-7-1.svg)

*Figure 7.1 — Four gates, in a deliberate order. Each is cheaper than the review it protects, and each catches a different class of error. The mechanical checks reject most defects at near-zero cost. Your attention is the scarce resource, and it is spent only on changes that have already cleared everything a machine can decide. The reviewer agent advises; the human decides. (Rendered as `figures/figure-7-1.svg` from its brief in `fig-brief/ch07-coding-and-pipeline-agents.md`, per `FIGURES.md`.)*

**Figure 7.2 — Notebook versus governed pipeline.**

![A two-row before-and-after diagram. The top row, labelled before, shows a single grey box labelled notebook holding an unordered cluster of cells, load, regrid, threshold and plot, in the order the investigation happened rather than the order a reader would need. One grey arrow leaves it labelled looked reasonable, then shared, with a vermillion callout reading no independent reader. The bottom row, labelled governed pipeline, shows the same four steps as an ordered green tool chain under version control, feeding an author agent, then tests, hooks and independent review, then a human owner, with a matching callout reading reader before merge. A note across the bottom reads that the analysis is identical in both rows and only what surrounds it has changed.](../figures/figure-7-2.svg)

*Figure 7.2 — The same four analytical steps, twice. Nothing about the science changes between the rows. What changes is that the steps become ordered and version-controlled, and that three checks and an accountable person now stand between the code and the shared branch. The gap between the rows is a gap in discipline, not in cleverness. (Rendered as `figures/figure-7-2.svg` from its brief in `fig-brief/ch07-coding-and-pipeline-agents.md`, per `FIGURES.md`.)*

## 7.4 Worked example: a governed pipeline with hooks and sub-agents

This example takes a real exploratory analysis from the author's operational work and follows it through the redesign, so the gates are concrete rather than abstract.

The starting point is a notebook that ingests an ensemble precipitation forecast and a set of river-gauge observations, aligns them in space and time, and computes a verification score judging the forecast against what was observed.
It is the kind of analysis that begins as a one-off and is then wanted every forecast cycle.
**[AUTHOR: specify the actual analysis — the forecast product, the gauge network, the verification metric, and the operational cadence at which it needed to run — so the example is grounded in the executed work rather than this generic stand-in.]**
The task handed to the workflow is not "write this analysis" but "turn this notebook into a governed pipeline", and that distinction shapes everything after it.
The objective, inputs, acceptance criteria and stop conditions get specified first, in the manner of Chapter 3, so the author agent and every gate downstream are judged against a fixed target rather than against whatever the agent decided to build.

The construction goes gate by gate, and the order the pieces get built in is part of the method.

First, intended behaviour is pinned down as tests before any refactoring begins: a small set of assertions that a known forecast–observation pair produces a known score, that missing gauge values are excluded rather than treated as zero, that the spatial alignment conserves the total where it should, and that an out-of-range input is rejected with a clear error rather than a silent NaN.
**[AUTHOR: give the two or three properties from the real analysis whose violation you would most want caught — the ones that would have burned you, or did.]**
These tests are written against the specification, and where the agent proposes them they get read before acceptance, because a test the agent both writes and satisfies asserts only that the code does what the code does.

Second, the pre-commit hooks are configured to run formatting, linting, type checking, a secrets-and-large-file scan and the full test suite on every commit, so the mechanical gates are enforced automatically and cannot be forgotten under deadline.

Third, and this is the step that distinguishes the design, the review is done by a *separate* reviewer sub-agent before any human sees the change: a distinct agent instance, given the change, the specification and a review checklist, told to report problems rather than to praise, with no ability to alter or approve the work.
That report is read last, against the change itself, and the human stays the sole authority who merges.

The division of labour is worth stating plainly, because it is the chapter's central practical claim.
The author agent proposes.
The tests and hooks dispose of the mechanical failures.
The independent reviewer agent surfaces the substantive ones.
The human decides, spending scarce attention on judgement rather than on the routine checking the earlier gates have already done (moderate-to-high confidence; the pattern is sound, the effort saved varies with task and model).
**[AUTHOR: report what actually happened when you ran this — which gate caught what, how much the reviewer sub-agent found that the tests missed, and the one issue, if any, that only the human caught. A single real trace here is worth more than the whole preceding paragraph.]**

**Figure 7.3 — The reviewer sub-agent before human review.**

![A four-lane sequence diagram read top to bottom, with lanes for the author agent, tests and hooks, a reviewer agent and the human owner. Step one, the author agent submits the change. Step two, the tests and hooks either fail and return it for fixing, or pass. Step three, on a pass, the change goes to the reviewer agent, whose lane is annotated as a different instance, read-only, with no power to approve. Step four, the reviewer reads the change against the specification rather than against the author's reasoning, which it is deliberately not given. Step five, it returns a findings report, annotated as advisory and not a gate the agent can open. Step six, the human owner reads both the report and the change and merges, owning the decision.](../figures/figure-7-3.svg)

*Figure 7.3 — Why the reviewer is a separate instance. It is given the change and the specification, and deliberately not the author agent's reasoning. That way it tests the work against the standard rather than against the case made for it. Its report is advisory: it reaches the human, who reads it alongside the change and owns the merge. (Rendered as `figures/figure-7-3.svg` from its brief in `fig-brief/ch07-coding-and-pipeline-agents.md`, per `FIGURES.md`.)*

## 7.5 Failure modes

The first and most consequential failure is plausible-but-wrong code that passes weak tests.
It is the failure the whole gate stack exists to catch, and the one it most often misses.

An agent asked to write both the code and its tests will, without a specification written against intended behaviour, produce tests that encode the code's actual behaviour rather than its correct behaviour.
So a transposed latitude and longitude, a metre-per-second field read as millimetres, or a fill value silently averaged into a mean will pass a green test suite whose assertions came from the very output they should have caught.
The defence is not more tests written by the same agent.
It is tests written against an independent statement of what the code must do, meaning the specification, physical conservation properties, known-answer cases from the literature, and cross-checks against an independent implementation, plus the discipline of reading the tests rather than just watching them pass.
This is the principle Chapter 11 builds its evaluation methods on, and the plausible failure Chapter 1 named: verification has to be external to the thing it verifies.
Even execution-based gates are not exempt.
Audits of the very benchmarks that grade coding agents have found that insufficient test coverage lets some wrong solutions pass as correct, so an execution-grounded gate still has a false-negative rate, set by the quality of the tests behind it (Zhu et al., 2025).
That audit has since been automated and scaled up.
An agentic auditor applied to 168 benchmarks found defects (ambiguous tasks, environment conflicts, incorrect ground truth) in more than a quarter of the tasks it examined, and removing the flawed ones shifted two widely used coding-benchmark scores by roughly ten percentage points (Wang et al., 2026; a 2026 preprint, and a coding-domain figure rather than a universal rate).
A green suite confirms only that the code does what the suite asserts.
It says nothing about whether the suite asserts the right thing (high confidence; this is the dominant failure of agent-written code).

The second failure is silent behavioural drift, where a pipeline keeps running and producing plausible output while its behaviour changes underneath.
A dependency updates and alters a default.
An input format shifts a column.
A regridding library changes how it handles edges.
None of these raises an error, because nothing is broken in a way the code checks for.
Agentic development makes drift both more likely and more tractable: more likely because agents readily update dependencies and refactor internals in ways whose behavioural consequences are not obvious, and more tractable because the same agents can cheaply maintain the regression tests and pinned environments that catch drift when it happens.
The defence is characterisation: a fixed reference input whose correct output is recorded and asserted on every run, a declared and version-locked environment, and an alert when a numerical result moves beyond a stated tolerance.
Then drift announces itself as a failed assertion instead of surfacing months later as an unexplained shift in a published time series (moderate confidence; the mechanisms are standard, their sufficiency depends on the reference cases chosen).
**[AUTHOR: an instance of drift you have seen bite — a library or format change that silently altered a result — would anchor this more firmly than the general statement.]**

> **Definition — Regression test.** A test that pins down behaviour already confirmed to be correct, by recording the output for a fixed input and asserting it again on every future run. Its whole purpose is to catch the day something quietly changes, such as a library update or a refactor, that would otherwise slip through unnoticed. It does not ask whether the answer is right in the abstract, only whether it still matches what was signed off before.

The third failure is over-agreeable review, and it is exactly why this chapter insists the reviewer be a separate agent rather than the author agent checking its own work.

Why a model asked to assess work tilts towards ratifying it is the failure gallery's to dissect (Chapter 13), and the countermeasure at roster scale is Chapter 10's.
What matters here is the consequence for a coding pipeline and the configuration that answers it.
The consequence is simple: ask an agent "is this correct?" straight after it has produced the thing, and you invite the answer it has already given.
Even a separate reviewer instance tilts towards agreement if it is prompted to evaluate rather than to find fault, or if it is handed the author's reasoning as authoritative context.
So the reviewer gets instantiated separately with its own clean context, charged explicitly with finding problems against a checklist rather than with judging acceptability, given no stake in defending the work, and held read-only with no merge rights.
Where the stakes justify the cost, use more than one reviewer with different instructions, as Chapter 10 develops.
State the limitation plainly: none of this makes the reviewer agent reliable the way a check on a conservation law is reliable.
It lowers the rate of over-agreeable review; it does not abolish it.
That residual is exactly why the human reviewer owns the decision rather than rubber-stamping the agent's approval (high confidence in the direction, low-to-moderate confidence in any specific reduction figure, which is model- and task-dependent).

**Figure 7.4 — How plausible-but-wrong code clears a weak suite.**

![A top-to-bottom failure trace. An author agent writes a regrid step carrying a hidden defect, latitude and longitude transposed, marked in vermillion. The same agent also writes a self-derived test, which returns a green pass, with a callout reading that it asserts what the code does rather than what it should, so the defect passes unseen. A parallel branch sends the same code to an independent conservation check, a vermillion diamond derived from the specification rather than from the code, which returns a red fail and sends the work back to the author agent to fix. A note at the foot reads that a green suite confirms only that the code does what the suite asserts, and says nothing about whether the suite asserts the right thing.](../figures/figure-7-4.svg)

*Figure 7.4 — How a green test suite hides a real defect. The agent wrote the code and then wrote tests against what the code does, so a transposed coordinate sails through. The conservation check catches it because it was derived from the specification, not from the output. This is the dominant failure of agent-written code, and it is why a passing suite is not evidence on its own. (Rendered as `figures/figure-7-4.svg` from its brief in `fig-brief/ch07-coding-and-pipeline-agents.md`, per `FIGURES.md`.)*

## 7.6 Verification checklist

This checklist follows the gate stack and applies to any change an agent proposes, whatever the tool or language.
A colleague who did not build the pipeline should be able to work down it and confirm each item.

- **Specification before code.** The intended behaviour of the change is written down first, as an objective with acceptance criteria a human can check, so every downstream gate judges against a fixed target rather than against the agent's own output (Chapter 3).
- **Tests assert intended, not observed, behaviour.** The assertions encode what the code should do and include at least one property derived independently of the code (a conservation law, a known-answer case, or a cross-check against a separate implementation), and a human has read the tests, not merely seen them pass.
- **Hooks enforce the mechanical gates.** Formatting, linting, type checking, a secrets-and-large-file scan and the full test suite run automatically on every commit, so no change reaches shared history without clearing them.
- **Review is genuinely independent.** The reviewer is a different agent instance from the author, with its own clean context, charged with finding faults against a checklist, running read-only with no power to approve or merge, and, where stakes justify it, more than one such reviewer with differing instructions (Chapter 10).
- **Drift is made to announce itself.** A fixed reference input has a recorded correct output asserted on every run, the environment is declared and version-locked, and a result moving beyond a stated tolerance raises an alert rather than passing quietly.
- **Authority is scoped, not assumed.** The author agent runs in a task-scoped environment with least-privilege credentials, the reviewer agent runs read-only, and neither can merge: the design governs permission as well as correctness (Chapter 12).
- **A human owns the merge.** An accountable person reads the reviewer's report and the change, exercises the judgement the earlier gates cannot, and owns the decision; the agents propose and check, the human decides.

A workflow that satisfies these seven has more assurance than most hand-written research code ever receives; a workflow that skips any of them has, at that gate, the fragility the notebook had.

## 7.7 Repository pointer

The companion repository holds the runnable form of this chapter under `/patterns/ch07-coding-and-pipeline-agents`, where the perishable specifics print cannot carry are kept current.
**[AUTHOR: confirm the final path and contents.]**
The intended contents are a minimal governed-pipeline template, meaning the notebook-to-pipeline refactor of §7.4 cut down to a small self-contained example, together with a pre-commit hook configuration, an independent-reviewer sub-agent specification and review checklist, and the tests that encode intended behaviour, including at least one independent property check.
Named tools, versions and the current model configuration live there rather than in this text, per the vendor-neutral convention, because they date faster than print can follow.
The durable pattern is the gate stack of Figure 7.1; the repository is where it gets built in whatever tooling is current when you read this.
The exercises for this chapter, in `/exercises`, ask you to take one of your own run-once notebooks through the four gates and record which gate caught what, the same trace the worked example asks of the author.
**[verify: confirm repository layout and exercise set before release.]**

---

### References (verify details before release)

- Jimenez, C. E., Yang, J., Wettig, A., Yao, S., Pei, K., Press, O. and Narasimhan, K. (2023). SWE-bench: can language models resolve real-world GitHub issues? *ICLR 2024*. https://arxiv.org/abs/2310.06770
- Wang, J., Bianchi, F., Zhu, S., Nie, F., Kwon, Y., Dhingra, B. and Zou, J. (2026). Automated benchmark auditing for AI agents and large language models. *arXiv preprint*. https://arxiv.org/abs/2605.26079
- Zhu, Y., Jin, T., Pruksachatkun, Y., et al. (2025). Establishing best practices for building rigorous agentic benchmarks. *arXiv preprint*. https://arxiv.org/abs/2507.02825
