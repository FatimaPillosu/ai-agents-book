# Chapter 11 — Verification and evaluation

> **Status:** draft r3 · voice v3.3 (`STYLE.md`) · sentence-per-line per `STYLE.md` §10 · figures as briefs per `FIGURES.md`.
> **Conventions:** vendor-neutral (outline §9) · **[AUTHOR: …]** marks lived material only the author can supply · **[verify]** marks real but unconfirmed details · citations drawn only from verified reports in `/research`. Nothing has been invented.
> **Integrity note:** the four model-evaluation references (Klemeš; Refsgaard & Henriksen; Jakeman et al.; Oberkampf & Trucano) are real and named by the author; the `/research` sweep did not cover them, so their bibliographic details keep `[verify]` until confirmed. Report-sourced citations carry a DOI or URL in the references list. No quotations, results or anecdotes have been invented.

---

This is the chapter on which the rest of the book depends.
Every earlier chapter ends by handing a claim to a gate: a citation that must resolve, a unit that must survive, a reviewer that must sign off, and every one of those gates has quietly assumed that whether the gate itself works can be established.
This chapter is where that assumption is paid for, because verification is not the part of agentic work bolted on at the end; it is the part that decides whether any of the rest was worth doing.

## 11.1 Why a leaderboard is the wrong instrument

The number at the top of a leaderboard answers a question a research group is almost never actually asking.
A public benchmark measures general capability: it reports how a model or an agent performs on a fixed, shared task distribution (resolving issues in open-source code repositories, answering examination-style questions, completing curated problems), and for tracking where the field is going it is indispensable, which is exactly what the coarse figures in Chapter 1 were used for.
What it cannot measure is fitness for a particular workflow, on a particular group's data, under a particular institution's tolerance for error, because none of those particulars is anywhere in the benchmark.
A system that resolves a high fraction of software-engineering tasks in aggregate reveals almost nothing about whether an agent built around it will correctly regrid one particular ensemble forecast, reconcile one particular gauge network, or carry units through one particular pipeline without dropping them.
The aggregate is a property of the distribution; the task at hand is a single point that may sit anywhere relative to it.
The reason the aggregate does not transfer is the jagged frontier of Chapter 1: reliability tracks how densely a task is represented in training material rather than how hard it looks, so a high mean score can sit directly on top of a severe, task-specific failure the mean conceals.

The research literature has begun to say this plainly, and from inside the benchmark community rather than against it.
A recent methodological critique of agent evaluation shows that accuracy-only leaderboards reward wasteful scaffolds, since simple baselines such as a retry loop over a plain model can match far more elaborate agent architectures at a fraction of the cost, and that most benchmarks it examined lacked adequate held-out sets, which lets systems overfit to the very tasks used to rank them (Kapoor et al., 2024).
A broad survey of agent evaluation reaches the compatible conclusion from the other direction, naming as an open gap the shortage of fine-grained, workflow-level assessment and the field's over-reliance on static, simplified tasks (Yehudai et al., 2025).
This chapter reads both as support for a single practical claim, stated as sharply as it can be: a benchmark result is admissible evidence about capability in general and inadmissible evidence about a particular workflow's correctness (high confidence).
That is not despair about measurement.
It is an argument for measuring the right thing, that is, the workflow's performance on the actual task, with the actual data, at the actual scale intended, which is what this book means by task-grounded evaluation; the rest of this chapter is about how to structure that so a claim of correctness carries weight in proportion to the decision resting on it.

> **Definition — Task-grounded evaluation.** Checking an agent's workflow on the real job it will be used for (the group's own data, its own conditions, its own definition of a right answer) rather than trusting a score the system earned on another party's benchmark. A leaderboard reports how a system performs on average across many unrelated tasks; task-grounded evaluation reports how it performs on the task at hand, which is the only basis on which a result can responsibly be staked.

Environmental science has an unusually mature literature on precisely this problem, built over decades for physically based models long before agents existed, and it transfers with surprisingly little modification.
Hydrological modelling in particular had to confront the fact that a model can reproduce a calibration record faithfully and still be right for the wrong reasons, and the discipline's answer was to formalise what counts as evidence that a model is fit for a stated purpose (Klemeš [verify]; Refsgaard & Henriksen [verify]).
The computational-science literature developed a complementary vocabulary, separating whether the code solves the equations correctly from whether the equations describe reality (Oberkampf & Trucano [verify]), and systematic accounts of the modelling process set out the iterative steps by which a model earns confidence (Jakeman et al. [verify]).
None of these was written with language models in mind, and each has to be adapted rather than transplanted, because an agent's failures, being plausible, fluent, and uncorrelated with correctness (Chapter 1), are not the failures of a numerical scheme.
The adaptation this chapter proposes is a five-tier hierarchy of evidential strength, in which each tier is defined by the check that establishes it and higher tiers subsume lower ones.
Confidence that the hierarchy is useful is high; confidence that any single tier boundary sits in exactly the right place is moderate, and this chapter flags where the reader's own judgement should settle the definitions.

## 11.2 Five tiers of evidence

The five tiers form a ladder in which each rung answers a stronger question than the one below it, and the evidential strength of a claim is the highest tier it has actually passed, not the highest it could in principle reach.

> **Definition — Evidential tier.** A named level of how well a claim has been checked, defined by the specific test it survived rather than by how much effort went into it. Naming an output "Tier 3" is a factual statement about evidence gathered, like citing a measurement's accuracy class, not a promise that the work was done diligently.

**[AUTHOR: confirm tier definitions — the labels and boundaries below are a proposal adapted from the model-evaluation literature; adjust so they match the terminology you intend to standardise across the book.]**

The lowest tier, **execution**, asks only whether the workflow ran to completion and produced output of the expected shape.
The check is that the process terminates without error and the output conforms to its declared schema: the right number of fields, the right types, values inside admissible ranges.
Execution is necessary and almost worthless on its own, because a workflow that produces a well-formed and entirely wrong answer passes it cleanly; its value is as a cheap gate that catches the crudest failures, namely the crash, the empty file, the truncated field.
The second tier, **internal consistency**, asks whether the output is coherent with itself and with its inputs under constraints that must hold regardless of the correct answer.
The check is that domain invariants are satisfied: mass and energy balance where they apply, monotonicity where it is required, units carried correctly end to end, totals reconciling with their parts.
Internal consistency catches a large and important class of silent errors, the unit slip and the conservation violation among them, exactly the errors Chapter 13 catalogues; however, it too can be satisfied by an output that is self-consistent and false, so it establishes the absence of a family of incoherence, not correctness.

The third tier, **reproduction of held-out truth**, is the first at which the word *correct* is earned, and it is the pivot of the whole hierarchy.
It asks whether the workflow reproduces a reference value it did not have access to when it ran, and the check is a split-sample test: a portion of ground truth is withheld, the workflow runs without sight of it, and its output is compared against the withheld reference by a metric fixed in advance.
This is the discipline hydrological modelling settled on long ago, namely to evaluate against data not used in fitting, and its whole force depends on the withholding being genuine, which for an agent means the reference must be absent not only from the immediate inputs but from anything the model could have seen, a stronger and subtler condition to which this chapter returns in §11.3.
The coding-agent literature has made this tier concrete in a way worth borrowing: execution-based benchmarks define success by whether a repository's own pre-existing test suite passes on the agent's patch, so the acceptance criterion exists before the agent runs, is automated, and does not depend on any model's opinion (Jimenez et al., 2023).
The fourth tier, **out-of-sample generalisation**, asks the harder question of whether the workflow holds up under conditions materially different from those it was built in, and the check is the differential test drawn straight from Klemeš's hierarchical testing scheme [verify]: run the workflow on a regime it was not tuned for (a different catchment, a different season, a wetter or drier period, a different instrument) and judge whether performance degrades gracefully or collapses.
A workflow that reproduces held-out truth inside its development regime but fails under transfer is fit for interpolation and unfit for extrapolation, and Tier 4 is what tells the two apart.
The fifth and highest tier, **independent adversarial scrutiny**, asks whether the claim survives a competent party actively trying to break it: an independent reviewer, either a human or a separate agent constituted for the purpose as in Chapters 10 and 12, tries to falsify the result, probes its edge cases and alternative explanations, and fails to overturn it.
This tier is expensive and cannot be automated away, because it is the point where judgement, not computation, certifies the result, and it is the only tier that offers real protection against errors no pre-specified check anticipated.
The tiers are cumulative: a Tier 4 claim has passed Tiers 1 through 4, and naming a tier is a statement about evidence actually gathered.

The ladder does not capture a reliability dimension on its own, and that dimension matters most for any workflow to be run repeatedly.
A workflow that passes a tier once may not pass it every time, because agent behaviour varies run to run, and a single successful trial systematically overstates dependability.
The tool-agent-user benchmark literature makes this measurable with a statistic worth adopting: pass^k, the probability that *all* of k independent runs succeed, which for one reported customer-service setting fell below a quarter at k of eight even though single-trial success looked far healthier (Yao et al., 2024).
For an operational workflow that runs monthly, single-trial success rates are close to meaningless, and pass^k-style thinking is what is required, because a duty cycle is a repeated trial and reliability is the thing that fails first.

**Figure 11.1 — The five-tier evidential hierarchy.** *A figure brief follows `FIGURES.md`; render in the house style.*

```
FIGURE BRIEF
- id:            Figure 11.1
- title:         Five tiers of evidence for a workflow claim
- type:          architecture (ascending ladder)
- claim:         Evidential strength ascends through five operationally defined tiers, each established by a specific check, from merely running to surviving independent adversarial scrutiny; higher tiers subsume lower ones.
- canvas:        16:9
- elements:      five stacked horizontal bars forming a ladder, lowest at the bottom,
                 each labelled with a tier name and its establishing check; the topmost
                 tier bar bordered in reviewer purple (#CC79A7) and carrying the reviewer
                 head-and-shoulders-with-tick icon; each tier carrying a small vermillion
                 gate diamond (#D55E00) at its right edge marking the check; an upward arrow
                 running the height of the ladder on the left, labelled "increasing
                 evidential strength"; a faint note that each tier subsumes those below
- flow:          bottom-to-top — tier 1 at the base rising to tier 5 at the top
- labels:        "1 · execution — runs, output well-formed",
                 "2 · internal consistency — invariants hold",
                 "3 · reproduces held-out truth — split-sample test",
                 "4 · out-of-sample generalisation — differential test",
                 "5 · independent adversarial scrutiny — reviewer tries to break it",
                 "increasing evidential strength", "each tier subsumes those below"
- annotations:   a bracket to the right spanning tiers 1–2 labelled "necessary, not
                 sufficient"; a bracket spanning tiers 3–5 labelled "correctness earned here"
- caption:       Figure 11.1 — The five-tier evidential hierarchy for claims about an agentic workflow's output. Each tier is defined by the check that establishes it and subsumes the tiers below; the strength of a claim is the highest tier it has actually passed. Tiers 1–2 are necessary but can be satisfied by a well-formed wrong answer; correctness is earned only from Tier 3 upward. Adapted for agentic outputs from the model-evaluation literature (after Klemeš; Refsgaard & Henriksen; Jakeman et al.; Oberkampf & Trucano).
- alt-text:      A vertical ladder of five stacked bars rising from bottom to top. From the base upward the rungs read: execution (runs, output well-formed); internal consistency (invariants hold); reproduces held-out truth (split-sample test); out-of-sample generalisation (differential test); and, at the top in purple with a reviewer icon, independent adversarial scrutiny (a reviewer tries to break it). Each rung carries a small gate symbol marking its check. An upward arrow on the left is labelled increasing evidential strength. A bracket marks the lower two rungs as necessary but not sufficient and the upper three as where correctness is earned.
- generator prompt: A flat vector diagram of an ascending ladder on an off-white
                 background. Five horizontal bars are stacked vertically with even spacing,
                 the lowest at the bottom. From bottom to top the bars are labelled
                 "1 execution — runs, output well-formed", "2 internal consistency —
                 invariants hold", "3 reproduces held-out truth — split-sample test",
                 "4 out-of-sample generalisation — differential test", and "5 independent
                 adversarial scrutiny — reviewer tries to break it". The top bar has a
                 purple border and a small purple head-and-shoulders-with-tick icon at its
                 left. Each bar has a small vermillion diamond gate symbol at its right
                 edge. A tall upward arrow on the far left spans all five bars, labelled
                 "increasing evidential strength". To the right, a bracket spans the lowest
                 two bars labelled "necessary, not sufficient", and a second bracket spans
                 the upper three bars labelled "correctness earned here". Near-black lines
                 and text, minimal text, generous spacing, single-weight connectors.
```

## 11.3 Verification must be external to the system verified

The single principle that holds the whole hierarchy together is that verification must be external to the system being verified.
Chapter 1 introduced it, and it is load-bearing enough to restate here as the governing rule of this chapter: a model asked whether its own output is right will answer fluently and with a confidence that is uncorrelated with the truth of the answer (Chapter 1).
The operational consequence is unforgiving.
No tier of the hierarchy may be established by the agent that produced the output, nor by an identical agent, nor by the same model prompted to check itself, because all three share the exact failure verification is meant to catch.
Each check has to draw its authority from a source the generating agent does not control: the schema at Tier 1 is fixed by the workflow's designer, not proposed by the agent at run time; the invariants at Tier 2 are physical or definitional facts external to the model; the held-out reference at Tier 3 is data the agent never saw; the transfer regime at Tier 4 is chosen by the evaluator to be unlike the development regime; and the reviewer at Tier 5 is independent by construction.
Where a check is implemented in code (a test suite, a schema validator, a mass-balance assertion), that code is itself an external artefact, written and reviewed under the governance of Chapters 7 and 12, and never generated and graded by the same agent in one unexamined step.

The strongest illustration of this principle in action comes from operational meteorology, and it is worth holding up as a template.
When a data-driven weather model arrived with impressive self-reported scores, forecast scientists did not take the vendor's numbers on trust; they re-verified the model as an operational centre would, initialised from operational analyses rather than the reanalysis it was trained on, scored against both analyses and independent station observations with the centre's own standard metrics, and examined on case studies including extreme events, and found it genuinely competitive but with documented weaknesses the training objective explained (Ben Bouallègue et al., 2024).
That is precisely what a research group must do for an agentic workflow: re-verify the claim on the group's own data, under its own operating conditions, with its own metrics, before trusting it in production.
The parallel is exact, and it is the reason the environmental sciences are well placed to govern agents: the verification culture already exists, and it only has to be extended to a new kind of instrument.

Externality is easier to state than to secure, and the subtlest threat to it is contamination of the held-out reference.
A split-sample test establishes nothing if the withheld data reached the model by another route: if the reference values appear in the agent's context, in a file it retrieved, in a cached result from an earlier run, or, hardest to exclude, in the public material the underlying model was trained on, then the test measures recall rather than reproduction and reports a correctness the workflow does not have.
This concern has no clean counterpart in classical model evaluation, where the model cannot have memorised the validation record, and it is the principal way the adaptation from the hydrological literature has to go beyond its source.
It is not hypothetical: audits of coding benchmarks have found that training-data contamination and repository familiarity can inflate scores, so that even an execution-grounded gate can report a capability the system does not independently possess (Zhu et al., 2025); a 2026 preprint that automated the audit across 168 benchmarks found the inflation large enough that removing the flawed tasks moved two widely used coding-benchmark scores by about ten percentage points (Wang et al., 2026; preprint).
Guarding against it needs the provenance discipline Chapter 12 specifies: knowing what entered the agent's context, recording where each reference came from, and preferring, for the highest-stakes claims, held-out data generated after the model's training cut-off or held under conditions that make prior exposure implausible.
The honest limitation is that contamination can rarely be excluded with certainty for a closed model whose training corpus is unknown; the right posture is to treat freedom from contamination as a claim with its own confidence level, to raise that confidence by controlling the routes that can be controlled, and to weight a Tier 3 result accordingly rather than reading it at face value.

## 11.4 Building a task-grounded evaluation set from the group's own workflow

If task-grounded evaluation is the answer, then the evaluation set is the instrument, and most groups do not have one.
An evaluation set is a curated collection of cases, inputs paired with the outcome already known to be right, run against a workflow to see how it performs on work of the kind the group does.
The raw material is almost certainly already to hand, scattered across the workflow's own history, so the task is to gather and discipline it rather than to invent it.
Working practitioners have converged on the same low-cost starting move: practitioner guidance describes testing an agent against roughly ten self-completed, known-answer examples before removing the human from a workflow's loop, then graduating its autonomy by the score (practitioner commentary).
[ai-reviewer: the in-prose marker for video citations is inconsistent across the seven video-citing chapters — "(practitioner commentary; see the references)" in ch02–ch04, bare "(practitioner commentary)" here and in ch13 §13.6, and "(practitioner commentary, 2026)" in ch12 §12.8 and ch14 §14.2. Plan §2.3 fixes the references format but not the in-prose form, so none of these breaches policy; but the book needs exactly one form, chosen by ai-editor and applied at all seven sites. The bare form used here is the weakest, since it gives the reader neither a year nor a pointer to where the source is identified.]

> **Definition — Evaluation set.** A fixed, curated set of test cases, each an input paired with an already-trusted answer, run against a workflow to measure how well it performs on the group's kind of work. It is the difference between "the agent seemed to do well" and "the agent reproduced the right answer on forty-seven of fifty cases chosen in advance". It is built once, guarded, and reused.

The first step is to **harvest cases** from four sources already available.
First, past runs whose outcomes a human eventually settled are the richest, because every time someone adjudicated an agent's output as right or wrong, a labelled case was created.
Second, the outputs of the manual workflow the agent is meant to replace or assist supply references, since the pre-agent way of doing the job produced answers already trusted.
Third, the group's failure log serves the same end, and the failure gallery of Chapter 13 is exactly this kind of record: each catalogued incident is a case the workflow must not get wrong again.
Fourth, a small held-back set of known-correct items generalises Chapter 5's discipline of holding back a handful of known-relevant papers to test whether retrieval finds them.
The second step is to **curate** each harvested case into a fixed shape: the input, the reference outcome, the metric that will decide pass or fail fixed in advance, and the provenance of the reference, that is, where the "right answer" came from and how far it is trusted, because a reference is only as good as its own pedigree.
The third step is to **stratify** the set across task types and regimes so that it spans the conditions the workflow will actually meet: this is the differential-split discipline of Klemeš's testing scheme [verify] applied to an evaluation set rather than a single model, and it is what stops a set that is all easy interpolation cases from certifying a workflow that collapses on the hard ones.

Two disciplines keep the set honest.
First, the set's **size** must be reported candidly: a few dozen carefully curated cases beat zero by an enormous margin, but small samples carry wide uncertainty, so a result on such a set is reported with an interval, not a bare percentage, and "forty-four of fifty, which is an 88% pass rate with a 95% interval of roughly 76 to 95%" says far more than "88%".
The design principles of verifiable-answer benchmarks are a useful guide to what makes a good case: an unambiguous, pre-registered, automatically checkable reference, and difficulty graded by the number of steps and tools a case demands (Mialon et al., 2023), so that "does the agent retrieve the correct discharge value from this archive?" has a checkable answer in exactly that sense, whereas "is this synthesis insightful?" does not, and belongs to Tier 5.
Second, the set is **versioned and refreshed** and guarded against contamination per §11.3: what entered context on each run is recorded, references generated after the model's training cut-off are preferred, and the set is re-examined when the workflow's inputs change, because an evaluation set that never changes slowly stops resembling the work.

**Figure 11.2 — Building a task-grounded evaluation set.** *A figure brief follows `FIGURES.md`; render in the house style.*

```
FIGURE BRIEF
- id:            Figure 11.2
- title:         An evaluation set built from the workflow's own history
- type:          architecture
- claim:         A task-grounded evaluation set is assembled from the workflow's own history through harvest → curate → stratify → hold out → version, and then feeds the tiered checks that gate the live workflow.
- canvas:        16:9
- elements:      left, four sky-blue data-store cylinders labelled as history sources —
                 "settled past runs", "manual-workflow outputs", "failure log (Ch.13)",
                 "known-correct hold-back"; these feed rightward into a "curate" step
                 (grey rounded rectangle, small tag: input + reference + metric + provenance);
                 then a "stratify" step (grey rounded rectangle) producing a
                 "stratified evaluation set" (sky-blue cylinder) with a split-off
                 "held-out slice" (smaller sky-blue cylinder); a "version + refresh" loop
                 arrow around the set; a vermillion gate diamond where the versioned set
                 meets a de-emphasised "live workflow" block (grey) on the far right
- flow:          left-to-right — four sources → curate → stratify → versioned set (with a
                 held-out slice) → gate → live workflow; a small curved arrow loops the set
                 back to "version + refresh"
- labels:        "settled past runs", "manual-workflow outputs", "failure log (Ch.13)",
                 "known-correct hold-back", "curate — input · reference · metric · provenance",
                 "stratify by task and regime", "stratified evaluation set", "held-out slice",
                 "version + refresh", "gate", "live workflow"
- annotations:   a small note under the held-out slice reading "guard against contamination (§11.3)";
                 a light callout on the gate reading "measured here (§11.5)"
- caption:       Figure 11.2 — A task-grounded evaluation set is not bought or downloaded; it is harvested from the workflow's own history (settled runs, the manual method it replaces, the group's failure log and a held-back set of known-correct items), then curated, stratified, held out and versioned. The versioned set is what the gates of §11.5 are measured against.
- alt-text:      An architecture diagram reading left to right. Four sky-blue cylinders on the left (settled past runs, manual-workflow outputs, failure log, and known-correct hold-back) feed into a curate step labelled input, reference, metric, provenance, then a stratify step, producing a stratified evaluation set cylinder with a smaller held-out slice beside it. A curved arrow loops the set back to a version and refresh step. The versioned set passes through a vermillion gate into a de-emphasised live-workflow block on the right. A note reads guard against contamination; a callout on the gate reads measured here.
- generator prompt: A flat vector architecture diagram on an off-white background, flowing
                 left to right. On the left, four stacked sky-blue cylinders labelled
                 "settled past runs", "manual-workflow outputs", "failure log (Ch.13)",
                 "known-correct hold-back". Arrows lead right into a grey rounded rectangle
                 labelled "curate — input · reference · metric · provenance", then into a
                 second grey rounded rectangle labelled "stratify by task and regime". This
                 produces a larger sky-blue cylinder labelled "stratified evaluation set"
                 with a smaller sky-blue cylinder beside it labelled "held-out slice". A
                 curved arrow loops from the set back leftward to a small tag labelled
                 "version + refresh". From the set, an arrow passes through a vermillion
                 diamond gate into a grey de-emphasised block on the far right labelled
                 "live workflow". A small note under the held-out slice reads "guard against
                 contamination (§11.3)"; a small callout on the gate reads "measured here
                 (§11.5)". Single-weight near-black connectors, one arrowhead style, generous
                 spacing, minimal text.
```

## 11.5 Measuring the gate itself

This is the promise the book has been deferring, and this section is where it comes due.
Chapter 5 said that "the evaluation of the gate itself — how to measure its false-negative rate, and how much verification a given synthesis warrants — is developed in Chapter 11".
Chapter 10 left its reviewer base rates "await[ing] measurement" and asserted that a reviewer which almost never returns a fault is evidence of a broken reviewer, not a flawless producer.
This section pays both debts.
The question underneath them is the one every gate in the book quietly assumes an answer to: when a gate says *pass*, how often is it wrong?

> **Definition — False-negative rate.** For a gate whose job is to catch bad work, the false-negative rate is how often it waves bad work through, saying "pass" when it should have said "fail". It is the number that matters most and the one most often left unmeasured, because a gate that never complains looks like a gate that works, right up to the point where it is found to have been asleep.

The state of the evidence has to be stated honestly first, because it shapes the whole answer.
When the first `/research` sweep behind this book was compiled, no study directly measured an LLM review gate's false-negative rate; by mid-2026 the first direct measurements were appearing, though none is measured on the work a given group actually does.
The sharpest separated whether a coding agent submitted a patch at all from whether the patch actually passed the repository's held-out tests: across 1,750 trajectories on 50 real tasks, four frontier models submitted a patch 70 to 100% of the time while resolving the issue only 18 to 50% of the time, and these silent semantic failures, confidently wrong and stable across repeats, made up 68 to 80% of every model's failures (Mehta, 2026; a preprint, coding-domain figures that transfer structurally, not numerically).
The two cheap signals reached for first, namely whether it finished and whether it repeats, therefore look healthiest exactly when the output cannot be trusted, because a silent semantic failure both completes and repeats.
The grader side is measured too: an automated audit of 168 benchmarks found defects in over a quarter of their tasks, the gate itself measurably wrong (Wang et al., 2026; preprint).
None of this measures a particular gate on a particular group's work, so the number required has to be made, not borrowed, and the method is the ordinary one of instrument science: the measuring instrument is calibrated against known inputs before its readings are trusted.

The method is **seeded-defect testing**, and it is disarmingly simple.
Inputs known to be sound have planted in them known faults of exactly the classes the gate is supposed to catch (a fabricated citation, a unit slip, an out-of-range value, a dropped constraint); the gate is run blind; and the count is taken of how many planted faults it misses.
The seeding is stratified by fault class, because a gate can be strong on one class and blind to another: a citation-verification gate that resolves every DOI may still wave through a unit error it was never built to see, and a single headline miss rate would hide that.
This is the same logic that the agentic-benchmark-validity literature applies to graders themselves: audits of popular benchmarks found that weak test coverage or lenient matching let failing work score as success, an error that is quantifiable and reducible by systematic audit, and applying a structured checklist to one benchmark cut its performance overestimation by a third (Zhu et al., 2025).
A gate is an instrument with a measurable error rate, and seeded defects are how that rate is measured.

> **Definition — Seeded-defect testing.** Known mistakes are deliberately planted into otherwise-correct work (a made-up reference, a wrong unit, a value outside the plausible range) and the check is run over it without being told where the mistakes are. A count is then taken of how many it caught. It is the fire drill for a verification gate: the only way to establish that an alarm works is to set off a controlled fire.

The measurement has to be reported the way any measurement on a small sample is reported: with its uncertainty attached.
This is not a nicety, because the numbers are usually small, given that only so many faults can be seeded by hand, and small samples are treacherous in a specific way that flatters a gate.
Suppose twenty faults of a given class are seeded and the gate catches all twenty.
The tempting conclusion is a zero miss rate, and it is wrong: with zero misses in twenty trials, the upper 95% bound on the true miss rate is roughly 3 in 20, about 15% (the "rule of three" for zero events).
The honest statement is not "this gate never misses" but "this gate's miss rate for this fault class is below about 15%, and tightening that bound requires more seeded faults".
That interval is the whole point, and it is why a clean sweep on a handful of seeded defects licenses far less confidence than it appears to.

The judge-bias literature supplies the concrete calibration experiments to run alongside the seeding, and they are cheap.
The founding study of using a strong model as an automated judge measured its agreement with humans but also documented its systematic biases, namely a preference for the answer presented first, a preference for longer answers regardless of quality, and a preference for the judge's own style of output, and proposed partial fixes with measured, incomplete effect (Zheng et al., 2023).
A later study measured position bias at scale and gave two tests any group can run on its own gate: repeat-stability (does the gate return the same verdict on identical repeats?) and order-swap consistency (does the verdict survive swapping the order of two candidates?), finding that the bias concentrates precisely where candidates are close in quality, that is, on the borderline cases that matter most at a gate (Shi et al., 2024).
A third study named the trap in the cheapest reviewer configuration of all: judges favour outputs that "sound like them", assigning higher scores to text of lower perplexity under their own distribution even when another model wrote it, so using the same model family to draft and to review is structurally biased towards approval (Wataoka et al., 2024).
The largest judge evaluation to date, covering 21 models, nine providers and some 541,000 judgements, sharpens all of this (Norman, Rivera and Hughes, 2026; a preprint, on general chat and question-answering tasks, not scientific artefacts).
Exact-match agreement overstates chance-corrected agreement, that is, Cohen's kappa, the agreement left once the score two coin-flippers would reach by luck is subtracted, by 33 to 41 percentage points, so every agreement figure, the founding study's included, must be read chance-corrected.
Its titular finding is starker: production judges with test-retest reliability above 0.95 coexisted with severe position bias, so a gate can be dependably wrong in a fixed direction while a naive self-consistency check certifies it, because consistency is evidence about reliability and none about correctness.
A companion 2026 study adds a bias the field had underweighted: style bias, a preference for formatted answers over the same content in plain prose, was the largest it measured (0.10 to 0.76 across five judges), so a reviewer gate can be gamed with headers and bullet points alone (Soumik, 2026; preprint).
The design implication is blunt: genuine independence needs model diversity, not just a fresh context window, and this is the measurable teeth behind the reviewer-independence rules of Chapters 7 and 10.

The strongest peer-reviewed result on automated review to date is worth stating for how narrow it is: an automated reviewer reached 69% balanced accuracy against expert consensus on conference-review decisions, just above the 66% of the humans it was benchmarked against, a striking figure but one from workshop-tier machine-learning reviewing, not a measure of scientific correctness (Lu et al., 2026, *Nature*).

Seeded defects measure what the gate catches; the **yield diagnostic** watches what it catches in the wild, and the two together are how a gate is known to be alive.
Chapter 5's checklist planted the "Yield" check and Chapter 10 planted its twin: a gate or reviewer that almost never fires on real work is not evidence of flawless upstream work but evidence of a broken check.
The most useful published analogue is from systematic-review automation, where a screening step's *sensitivity* is precisely one minus its false-negative rate: a 2025 study reported an automated screening gate at around 97% sensitivity against a dual-human baseline near 82%, which is exactly a review gate's false-negative rate being measured and compared, though the study is a preprint from the tool's own developers and its numbers should be read with that in mind (Cao et al., 2025).
Watching yield over time turns the same idea into a standing alarm: if a citation gate stops rejecting anything, either the drafting genuinely improved or the gate quietly broke, and which of the two has happened cannot be told without seeding it again.
Re-measurement is therefore not optional and needs a trigger list: after any model change, after any prompt change, after a change in the data regime the workflow operates on, and on a calendar besides, because models drift, prompts rot, and the work moves.

How much of this effort a given output deserves is not a separate question; it is the tier-and-stakes matching of §11.7, and this chapter closes that loop there.
For now the principle is that a tier claim is only ever as strong as the measured check that establishes it, so that a Tier 3 result gated by an unmeasured citation check is a Tier 3 result in name only, and that measuring the gate is what converts the ladder of §11.2 from a description of ambition into a record of evidence.

**Figure 11.3 — Measuring a gate by seeded defects.** *A figure brief follows `FIGURES.md`; render in the house style.*

```
FIGURE BRIEF
- id:            Figure 11.3
- title:         Seeded-defect measurement of a verification gate
- type:          sequence
- claim:         A gate's false-negative rate is measured by seeding known defects into sound inputs, running the gate blind, tallying catches and misses, and reporting a rate with its uncertainty; trigger events reopen the loop.
- canvas:        16:9
- elements:      three actors as vertical lanes read top-to-bottom — a human (blue
                 head-and-shoulders) who seeds faults; the gate under test (vermillion
                 diamond); a tally/record data store (sky-blue cylinder); numbered ordered
                 steps crossing between lanes
- flow:          top-to-bottom, numbered — (1) human plants known faults of named classes
                 into sound inputs; (2) inputs run through the gate blind; (3) gate returns
                 pass/fail per input; (4) tally records catches and misses by fault class;
                 (5) record reports a rate with a confidence interval; (6) a trigger event
                 (model / prompt / data-regime change) loops back to step 1
- labels:        "seed known faults — fabricated citation · unit slip · out-of-range · dropped constraint",
                 "run gate blind", "pass / fail per input", "tally catches & misses by class",
                 "report rate + interval", "trigger: model / prompt / data-regime change → re-measure"
- annotations:   a vermillion callout on the tally reading "a never-firing gate is a broken gate (yield)";
                 a small note on step 5 reading "small samples → report an interval, not a clean zero"
- caption:       Figure 11.3 — Measuring a gate's false-negative rate by seeded defects: plant known faults, run the gate blind, tally catches and misses by fault class, and report a rate with its uncertainty rather than a bare percentage. A change of model, prompt or data regime reopens the loop; a gate that never fires on real work is investigated, not trusted.
- alt-text:      A top-to-bottom sequence diagram with three lanes: a human, the gate under test drawn as a vermillion diamond, and a tally record drawn as a cylinder. Numbered steps run: the human seeds known faults of named classes into sound inputs; the inputs run through the gate blind; the gate returns pass or fail for each; the tally records catches and misses by fault class; the record reports a rate with a confidence interval. A trigger event (a model, prompt or data-regime change) loops back to the seeding step. A callout reads a never-firing gate is a broken gate; a note reads small samples mean report an interval, not a clean zero.
- generator prompt: A flat vector sequence diagram on an off-white background, read top to
                 bottom, with three vertical lanes. The left lane is headed by a blue
                 head-and-shoulders icon labelled "human — seeds faults"; the middle lane by
                 a vermillion diamond labelled "gate under test"; the right lane by a
                 sky-blue cylinder labelled "tally / record". Numbered horizontal arrows
                 cross between lanes in order: (1) from human to gate, "seed known faults —
                 fabricated citation · unit slip · out-of-range · dropped constraint"; (2)
                 "run gate blind"; (3) from gate to tally, "pass / fail per input"; (4) at
                 the tally, "tally catches & misses by class"; (5) at the record, "report
                 rate + interval"; (6) a curved arrow from the record back up to the human,
                 "trigger: model / prompt / data-regime change → re-measure". A vermillion
                 callout near the tally reads "a never-firing gate is a broken gate (yield)".
                 A small note by step 5 reads "small samples → report an interval, not a
                 clean zero". Single-weight near-black connectors, one arrowhead style,
                 numbered steps, generous spacing, minimal text.
```

## 11.6 Worked example — measuring a rainfall-forecast-verification gate

The abstract method earns its keep only on a real workflow, so this section walks one pass through §§11.4–11.5 in operational meteorology, with the scaffolding written out and every number left where it belongs, that is, with the author, because inventing an illustrative catch rate would be exactly the fabrication this book forbids.

The workflow step is the verification of a rainfall forecast against observations, a stage from the operational work that runs through Part IV, and the gate under scrutiny is the check that decides whether a computed verification score is trustworthy before it is reported.
Building the evaluation set followed §11.4.
Cases were harvested from settled past runs where a human had already adjudicated the score as right or wrong, from the manual verification the workflow replaces, and from the group's own log of past mistakes; each was curated as an input, a reference score, a metric fixed in advance, and the provenance of that reference; and the set was stratified across the regimes that matter for rainfall (light and heavy events, different seasons, different station densities) so that it would not certify a gate on easy cases and stay silent on the hard ones.
**[AUTHOR: the number of curated cases, the exact stratification you used, and where the reference scores came from — this is the concrete evaluation set, and only you have it.]**

Measuring the gate followed §11.5.
Defects of the classes this gate must catch (a unit mismatch between forecast and observation, an out-of-range accumulation, a mis-paired station-and-grid-cell, a silently dropped quality-control flag) were seeded into otherwise-sound inputs, the gate was run blind, and catches and misses were tallied by class.
**[AUTHOR: the fault classes you actually seeded, how many of each, and the measured catch rate per class with its interval — report zero-miss results as an upper bound per the rule of three, not as a clean zero.]**
The yield diagnostic ran in parallel: over the same period the base rate at which the gate rejected real, unseeded work was recorded, because a gate that fired only on the planted faults and never on live runs would be a gate calibrated to catch exactly the mistakes already known and nothing else.
**[AUTHOR: your observed real-world yield — the base rate at which the gate rejects live work — and, if you have it, the contrast between a well-configured cross-family reviewer and a naive same-model one, which is the measurement Chapter 10 asked for.]**
The lesson this section is meant to carry, beyond the numbers, is that the most valuable outcome of seeding a gate already trusted is discovering a fault class it silently misses, a miss worth more than any pass, because it reveals where the instrument is blind before an operational result does.
**[AUTHOR: recount what actually happened when you first calibrated one of these gates — which fault class, if any, it missed, and what you changed as a result. This is the lived detail that makes the section real; leave it to your own experience rather than a generic illustration.]**

## 11.7 Operating the ladder in practice

The hierarchy is a tool for allocating verification effort deliberately, not a demand that every output climb to the top, and using it well means matching the tier reached to the stakes of the decision the output informs.
Climbing costs, and the cost structure is the one Chapter 4 set out.
Tiers 1 and 2 are cheap and largely automatable and should be applied to essentially everything, because a schema check and an invariant assertion cost little and catch the crudest and some of the most dangerous failures.
Tier 3 costs whatever it costs to hold out and curate reference data, and is warranted wherever a quantitative result will be reported or acted on.
Tier 4 costs the design of a genuine transfer test, and is warranted wherever the workflow will be applied outside the regime it was built in, which, for operational environmental work, is the common case rather than the exception.
Tier 5 costs scarce expert attention and is reserved for claims whose failure would be consequential: a result headed for publication, a warning informing a decision, a configuration about to enter routine operation.
A workflow that stops at Tier 2 for an exploratory triage is properly governed; the same workflow stopping at Tier 2 for a published result is not.
The cost-awareness literature reinforces this from the evaluation side, since accuracy and cost should be reported together as a frontier, not accuracy alone, because agent costs vary by orders of magnitude at similar accuracy (Kapoor et al., 2024), and the same discipline that stops a group paying for a wasteful scaffold stops it paying for verification a triage result does not need.

The tier reached should be recorded alongside the output as part of its provenance (Chapter 12), so that a later reader (a reviewer, a successor, or the original author six months on) can see not merely what the workflow concluded but how strong the evidence for that conclusion was, and can decide whether the tier attained matches the use now being made of it.
This record is also what makes the failure gallery of Chapter 13 legible: nearly every failure there is an output trusted at a tier above the one its evidence actually supported, and the discipline of naming the tier is the discipline that prevents it.
There is one refinement §11.5 forces onto this picture, and it is the paragraph that ties the chapter together.
A tier claim is only ever as strong as the measured check that establishes it.
Reaching Tier 3 through a citation gate whose false-negative rate has never been measured is reaching Tier 3 on faith, and the whole apparatus of seeded defects and yield exists to convert that faith into a defensible number, so that recording "Tier 3" in an artefact's provenance records a check that has been calibrated, not one that has merely been hoped about.
One boundary is easy to blur and worth drawing: a confidence-scored agent output ("I am 80% sure this flag is correct") is a different and less mature capability than a pass/fail gate, since uncertainty quantification for agents is an open research field, catalogued by a 2026 peer-reviewed survey as foundations and challenges rather than working methods, so a self-reported confidence number is never treated as a measured gate (Oh et al., 2026).
The limitation worth stating plainly is that the hierarchy governs evidential strength, not importance: it can establish how well supported a claim is, but it cannot establish whether the claim is the one that matters, which stays a matter of scientific judgement that no tier, and no agent, can supply.

## 11.8 Verification checklist

This checklist certifies that a workflow's evidential claims are established by measured, external checks rather than asserted; a colleague who did not build the workflow should be able to apply it from the record alone.

- **Tier named and recorded.** Every reported output carries the evidential tier it actually reached (§11.2), recorded in its provenance (Chapter 12), and a reviewer can see that the tier matches the use being made of the output, not the effort that was intended (high confidence this is checkable from the record).
- **Checks external to the producer.** No tier was established by the agent that produced the output, an identical agent, or the same model checking itself; each check draws authority from a schema, an invariant, held-out data or an independent reviewer (§11.3; Chapters 7, 10).
- **Contamination routes controlled and recorded.** For every Tier 3 claim, what entered the agent's context is recorded, the held-out reference is shown to be genuinely withheld, and any residual contamination risk is stated as a confidence level rather than ignored (§11.3; Chapter 12).
- **Evaluation set versioned, stratified and refreshed.** The task-grounded evaluation set exists, spans the task types and regimes the workflow meets, carries a version and provenance for each reference, and is refreshed on a stated trigger (§11.4).
- **Every gate's false-negative rate measured.** Each gate and reviewer has been calibrated by seeded defects, stratified by fault class, with results reported as intervals rather than clean zeros (§11.5); a colleague can see the seeding design and the measured rates, and high judge self-consistency is never read as low bias, because consistency is not correctness.
- **Re-measurement triggers defined and honoured.** The gate's calibration is repeated after any model change, prompt change or data-regime change, and on a calendar; the record shows when it was last re-measured (§11.5).
- **Yield monitored.** The rate at which each gate rejects real, unseeded work is watched, and a gate that has stopped firing has been investigated rather than trusted (§11.5; Chapters 5, 10).
- **Tier matched to stakes.** The verification effort spent is proportionate to the consequence of the output's failure, with the cheap tiers applied to everything and the expensive tiers reserved for consequential claims (§11.7; Chapter 4).
- **Verification effort recorded in provenance.** The checks applied, the tier reached and the gate calibrations relied on are all captured in the audit trail, so the strength of every claim is reconstructable after the fact (§11.7; Chapter 12).

## 11.9 Repository pointer

The companion repository holds the runnable and perishable counterparts to this chapter under `/patterns/ch11-verification-and-evaluation`, with the printable checklist under `/checklists`.
The runnable material is an evaluation-set template (the case shape of §11.4, with fields for input, reference, metric and provenance) together with a seeded-defect harness that plants faults of named classes, runs a gate blind, and reports catch rates with intervals per §11.5, written to be adapted to a group's own gate rather than run as-is.
Named tools, current model capabilities and any volatile figures are confined to the repository per the book's vendor-neutral convention, so the print chapter states the method and its reasoning while the repository tracks the parts that date **[AUTHOR: confirm the repository paths and contents once the evaluation-set template and seeded-defect harness are finalised; note any statistical-library or data-access requirements]**.

---

### References

Report-sourced references carry a DOI or URL and are drawn from the verified sweep in `/research`. The four model-evaluation references were named by the author and not covered by the sweep; their details keep `[verify]` until confirmed.

- Ben Bouallègue, Z., et al. (2024). The rise of data-driven weather forecasting: a first statistical assessment of machine learning-based weather forecasts in an operational-like context. *Bulletin of the American Meteorological Society*, 105(6). DOI: 10.1175/BAMS-D-23-0162.1
- Cao, C., Arora, R., Cento, P., et al. (2025). Automation of systematic reviews with large language models. *medRxiv* preprint. DOI: 10.1101/2025.06.13.25329541 [verify journal status before release]
- Davis, D. (2026). "How Anthropic's Own Team Gets AI to Stop Lying to Them." Video, @dylandavisai, 20 June 2026. https://www.youtube.com/watch?v=EPEI-IIPu4E (practitioner commentary; concepts cited as corroboration, not evidence)
- Jakeman, A. J., Letcher, R. A., & Norton, J. P. (2006). Ten iterative steps in development and evaluation of environmental models. *Environmental Modelling & Software*, 21(5), 602–614. [verify]
- Jimenez, C. E., Yang, J., Wettig, A., Yao, S., Pei, K., Press, O., & Narasimhan, K. (2023). SWE-bench: can language models resolve real-world GitHub issues? ICLR 2024. Preprint: https://arxiv.org/abs/2310.06770
- Kapoor, S., Stroebl, B., Siegel, Z. S., Nadgir, N., & Narayanan, A. (2024). AI agents that matter. Preprint: https://arxiv.org/abs/2407.01502 [verify archival venue before release]
- Klemeš, V. (1986). Operational testing of hydrological simulation models. *Hydrological Sciences Journal*, 31(1), 13–24. [verify]
- Lu, C., Lu, C., Lange, R. T., Yamada, Y., Hu, S., Foerster, J., Ha, D., & Clune, J. (2026). Towards end-to-end automation of AI research. *Nature*, 651(8107), 914–919. DOI: 10.1038/s41586-026-10265-5
- Mehta, A. (2026). Confident and wrong: silent semantic failures in coding agents. Preprint: https://arxiv.org/abs/2603.25764 [verify preprint status before release]
- Mialon, G., Fourrier, C., Swift, C., Wolf, T., LeCun, Y., & Scialom, T. (2023). GAIA: a benchmark for General AI Assistants. Preprint: https://arxiv.org/abs/2311.12983
- Norman, J. D., Rivera, M. U., & Hughes, D. A. (2026). Reliability without validity: a systematic, large-scale evaluation of LLM-as-a-judge models across agreement, consistency, and bias. Preprint: https://arxiv.org/abs/2606.19544 [verify preprint status before release]
- Oberkampf, W. L., & Trucano, T. G. (2002). Verification and validation in computational fluid dynamics. *Progress in Aerospace Sciences*, 38(3), 209–272. [verify]
- Oh, C., Park, S., Kim, T. E., et al. (2026). Uncertainty quantification in LLM agents: foundations, emerging challenges, and opportunities. Preprint; accepted to ACL 2026 main conference. https://arxiv.org/abs/2602.05073 [verify venue before release]
- Refsgaard, J. C., & Henriksen, H. J. (2004). Modelling guidelines — terminology and guiding principles. *Advances in Water Resources*, 27(1), 71–82. [verify]
- Shi, L., Ma, C., Liang, W., Diao, X., Ma, W., & Vosoughi, S. (2024). Judging the judges: a systematic study of position bias in LLM-as-a-judge. Preprint: https://arxiv.org/abs/2406.07791 [verify final venue]
- Soumik, S. K. (2026). Judging the judges: a systematic evaluation of bias mitigation strategies in LLM-as-a-judge pipelines. Preprint: https://arxiv.org/abs/2604.23178 [verify preprint status before release]
- Wang, J., Bianchi, F., Zhu, S., et al. (2026). Automated benchmark auditing for AI agents and large language models. Preprint: https://arxiv.org/abs/2605.26079 [verify venue before release]
- Wataoka, K., Takahashi, T., & Ri, R. (2024). Self-preference bias in LLM-as-a-judge. Preprint: https://arxiv.org/abs/2410.21819 [verify peer-reviewed status]
- Yao, S., Shinn, N., Razavi, P., & Narasimhan, K. (2024). τ-bench: a benchmark for tool-agent-user interaction in real-world domains. Preprint: https://arxiv.org/abs/2406.12045 [verify reviewed venue]
- Yehudai, A., Eden, L., Li, A., Uziel, G., Zhao, Y., Bar-Haim, R., Cohan, A., & Shmueli-Scheuer, M. (2025). Survey on evaluation of LLM-based agents. Preprint: https://arxiv.org/abs/2503.16416
- Zheng, L., Chiang, W.-L., Sheng, Y., et al. (2023). Judging LLM-as-a-judge with MT-Bench and Chatbot Arena. NeurIPS 2023 Datasets and Benchmarks Track. Preprint: https://arxiv.org/abs/2306.05685
- Zhu, Y., Jin, T., Pruksachatkun, Y., et al. (2025). Establishing best practices for building rigorous agentic benchmarks. Preprint: https://arxiv.org/abs/2507.02825 [verify venue]
