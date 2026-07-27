# Chapter 11 — Verification and evaluation

> **Status:** draft r4 · voice v5.0 (`STYLE.md` §1) · sentence-per-line per `STYLE.md` §10 · figures as briefs per `FIGURES.md`.
> **Conventions:** vendor-neutral (outline §9) · **[AUTHOR: …]** marks lived material only the author can supply · **[verify]** marks real but unconfirmed details · citations drawn only from verified reports in `/research`. Nothing has been invented.
> **Integrity note:** the four model-evaluation references (Klemeš; Refsgaard & Henriksen; Jakeman et al.; Oberkampf & Trucano) are real and named by the author; the `/research` sweep did not cover them, so their bibliographic details keep `[verify]` until confirmed. Report-sourced citations carry a DOI or URL in the references list. No quotations, results or anecdotes have been invented.

---

This is the chapter the rest of the book depends on.
Every earlier chapter ends by handing a claim to a gate: a citation that must resolve, a unit that must survive, a reviewer that must sign off.
Every one of those gates has quietly assumed you can establish whether the gate itself works.
This is where that assumption gets paid for.
Verification is not the part of agentic work you add at the end; it is the part that decides whether any of the rest was worth doing.

## 11.1 Why a leaderboard is the wrong instrument

The number at the top of a leaderboard answers a question your research group is almost never asking.

A public benchmark measures general capability.
It reports how a model or an agent performs on a fixed, shared task distribution: resolving issues in open-source code repositories, answering examination-style questions, completing curated problems.
For tracking where the field is going it is indispensable, which is exactly what the coarse figures in Chapter 1 were used for.
What it cannot measure is fitness for your workflow, on your data, under your institution's tolerance for error, because none of those particulars is anywhere in the benchmark.
A system that resolves a high fraction of software-engineering tasks in aggregate tells you almost nothing about whether an agent built around it will correctly regrid one particular ensemble forecast, reconcile one particular gauge network, or carry units through one particular pipeline without dropping them.
The aggregate is a property of the distribution.
Your task is a single point that may sit anywhere relative to it.
The reason the aggregate does not transfer is the jagged frontier of Chapter 1: reliability tracks how densely a task appears in training material rather than how hard it looks, so a high mean score can sit directly on top of a severe, task-specific failure the mean hides.

The research literature has begun to say this plainly, and from inside the benchmark community rather than against it.
A recent methodological critique of agent evaluation shows that accuracy-only leaderboards reward wasteful scaffolds, since simple baselines such as a retry loop over a plain model can match far more elaborate agent architectures at a fraction of the cost, and that most benchmarks it examined lacked adequate held-out sets, which lets systems overfit to the very tasks used to rank them (Kapoor et al., 2024).
A broad survey of agent evaluation reaches the compatible conclusion from the other direction, naming as an open gap the shortage of fine-grained, workflow-level assessment and the field's over-reliance on static, simplified tasks (Yehudai et al., 2025).
Both support one practical claim, stated as sharply as it can be: a benchmark result is admissible evidence about capability in general and inadmissible evidence about a particular workflow's correctness (high confidence).
That is not despair about measurement.
It is an argument for measuring the right thing, meaning the workflow's performance on the actual task, with the actual data, at the actual scale intended.
That is what this book means by task-grounded evaluation, and the rest of the chapter is about structuring it so a claim of correctness carries weight in proportion to the decision resting on it.

> **Definition — Task-grounded evaluation.** Checking an agent's workflow on the real job it will be used for (the group's own data, its own conditions, its own definition of a right answer) rather than trusting a score the system earned on another party's benchmark. A leaderboard reports how a system performs on average across many unrelated tasks; task-grounded evaluation reports how it performs on the task at hand, which is the only basis on which a result can responsibly be staked.

Environmental science has an unusually mature literature on exactly this problem, built over decades for physically based models long before agents existed, and it transfers with surprisingly little modification.
Hydrological modelling in particular had to face the fact that a model can reproduce a calibration record faithfully and still be right for the wrong reasons.
The discipline's answer was to formalise what counts as evidence that a model is fit for a stated purpose (Klemeš [verify]; Refsgaard & Henriksen [verify]).
The computational-science literature developed a complementary vocabulary, separating whether the code solves the equations correctly from whether the equations describe reality (Oberkampf & Trucano [verify]), and systematic accounts of the modelling process set out the iterative steps by which a model earns confidence (Jakeman et al. [verify]).
None of these was written with language models in mind, and each has to be adapted rather than transplanted, because an agent's failures, being plausible, fluent, and uncorrelated with correctness (Chapter 1), are not the failures of a numerical scheme.
The adaptation this chapter proposes is a five-tier hierarchy of evidential strength, in which each tier is defined by the check that establishes it and higher tiers subsume lower ones.
Confidence that the hierarchy is useful is high; confidence that any single tier boundary sits in exactly the right place is moderate, and this chapter flags where the reader's own judgement should settle the definitions.

## 11.2 Five tiers of evidence

The five tiers form a ladder.
Each step answers a stronger question than the one below it, and the evidential strength of a claim is the highest tier it has actually passed, not the highest it could in principle reach.

> **Definition — Evidential tier.** A named level of how well a claim has been checked, defined by the specific test it survived rather than by how much effort went into it. Naming an output "Tier 3" is a factual statement about evidence gathered, like citing a measurement's accuracy class, not a promise that the work was done diligently.

**[AUTHOR: confirm tier definitions — the labels and boundaries below are a proposal adapted from the model-evaluation literature; adjust so they match the terminology you intend to standardise across the book.]**

The lowest tier, **execution**, asks only whether the workflow ran to completion and produced output of the expected shape.
The check is that the process terminates without error and the output conforms to its declared schema: the right number of fields, the right types, values inside admissible ranges.
Execution is necessary and almost worthless on its own, because a workflow producing a well-formed and entirely wrong answer passes it cleanly.
Its value is as a cheap gate catching the crudest failures: the crash, the empty file, the truncated field.

The second tier, **internal consistency**, asks whether the output is coherent with itself and with its inputs under constraints that hold regardless of what the right answer is.
The check is that domain invariants are satisfied: mass and energy balance where they apply, monotonicity where it is required, units carried correctly end to end, totals reconciling with their parts.
Internal consistency catches a large and important class of silent errors, including the unit slip and the conservation violation, which are exactly the errors Chapter 13 catalogues.
It too can be satisfied by an output that is self-consistent and false, so it establishes the absence of a family of incoherence, not correctness.

The third tier, **reproduction of held-out truth**, is the first where the word *correct* is earned, and the whole hierarchy turns on it.
It asks whether the workflow reproduces a reference value it did not have access to when it ran.
The check is a split-sample test: withhold a portion of ground truth, run the workflow without sight of it, and compare its output against the withheld reference by a metric fixed in advance.
This is the discipline hydrological modelling settled on long ago, evaluating against data not used in fitting.
Its whole force depends on the withholding being genuine, and for an agent that means the reference must be absent not only from the immediate inputs but from anything the model could have seen, which is a stronger and subtler condition, and §11.3 returns to it.
The coding-agent literature has made this tier concrete in a way worth borrowing: execution-based benchmarks define success by whether a repository's own pre-existing test suite passes on the agent's patch, so the acceptance criterion exists before the agent runs, is automated, and does not depend on any model's opinion (Jimenez et al., 2023).
The fourth tier, **out-of-sample generalisation**, asks the harder question of whether the workflow holds up under conditions materially different from the ones it was built in.
The check is the differential test taken straight from Klemeš's hierarchical testing scheme [verify]: run the workflow on a regime it was not tuned for, such as a different catchment, a different season, a wetter or drier period or a different instrument, and see whether performance degrades gracefully or collapses.
A workflow that reproduces held-out truth inside its development regime but fails under transfer is fit for interpolation and unfit for extrapolation, and Tier 4 is what tells the two apart.

The fifth and highest tier, **independent adversarial scrutiny**, asks whether the claim survives a competent party actively trying to break it.
An independent reviewer, a human or a separate agent set up for the purpose as in Chapters 10 and 12, tries to falsify the result, probes its edge cases and alternative explanations, and fails to overturn it.
This tier is expensive and cannot be automated away, because it is where judgement rather than computation certifies the result, and it is the only tier offering real protection against errors no pre-specified check anticipated.

The tiers are cumulative.
A Tier 4 claim has passed Tiers 1 through 4, and naming a tier is a statement about evidence actually gathered.

The ladder does not capture reliability on its own, and reliability matters most for anything you intend to run repeatedly.
A workflow that passes a tier once may not pass it every time, because agent behaviour varies run to run, and a single successful trial systematically overstates dependability.
The tool-agent-user benchmark literature makes this measurable with a statistic worth adopting: pass^k, the probability that *all* of k independent runs succeed.
In one reported customer-service setting it fell below a quarter at k of eight, even though single-trial success looked far healthier (Yao et al., 2024).
For an operational workflow that runs monthly, single-trial success rates are close to meaningless.
A duty cycle is a repeated trial, and reliability is what fails first.

**Figure 11.1 — The five-tier evidential hierarchy.**

![Five horizontal bars stacked as a ladder, read bottom to top, each naming a tier and the check that establishes it. Tier one, execution: it runs and the output is well-formed. Tier two, internal consistency: the invariants hold. Tier three, reproduces held-out truth by a split-sample test, marked as the first tier where the word correct is earned. Tier four, out-of-sample generalisation by a differential test. Tier five, independent adversarial scrutiny, where a reviewer tries to break the claim and fails, carried in reviewer purple. A bracket spans tiers one and two, labelled necessary but almost worthless alone; another spans three to five, labelled correctness earned here. An arrow up the side reads increasing evidential strength, and a footer reads that a claim holds the highest tier it actually passed, not the highest it could reach.](../figures/figure-11-1.svg)

*Figure 11.1 — The ladder every claim in this book is measured against. The two bottom tiers are cheap and catch the crude failures, but an output can pass both and still be wrong. Correct is a word that gets earned at tier three, against data the workflow never saw, and the top tier cannot be automated because it is judgement doing the certifying. A claim holds the tier it passed, not the tier you intended. (Rendered as `figures/figure-11-1.svg` from the brief below, per `FIGURES.md`.)*

```
FIGURE BRIEF
- id:            Figure 11.1
- title:         Five tiers of evidence for a workflow claim
- type:          architecture (ascending ladder)
- claim:         Evidential strength ascends through five operationally defined tiers, each established by a specific check, from merely running to surviving independent adversarial scrutiny.
- standfirst:    A claim holds the highest tier it actually passed — not the one you hoped for.
- canvas:        16:9
- elements:      five stacked horizontal bars forming a ladder, lowest at the bottom, each
                 labelled with a tier name and its establishing check; the topmost bar
                 bordered in reviewer purple and carrying the reviewer icon; each tier
                 carrying a small vermillion gate diamond at its right edge; an upward
                 arrow beside the ladder
- flow:          bottom-to-top — tier 1 at the base rising to tier 5 at the top
- labels:        "1 · execution — runs, output well-formed",
                 "2 · internal consistency — invariants hold",
                 "3 · reproduces held-out truth — split-sample test",
                 "4 · out-of-sample generalisation — differential test",
                 "5 · independent adversarial scrutiny — reviewer tries to break it",
                 "increasing evidential strength"
- annotations:   bracket spanning tiers 1–2, "necessary — and almost worthless alone"; on
                 tier 3, "the first tier where the word correct is earned"; bracket
                 spanning tiers 3–5, "correctness earned here"; on tier 5, "cannot be
                 automated — judgement does the certifying"; a footer, "the tiers are
                 cumulative: a tier-4 claim has passed 1 to 4"
- caption:       Figure 11.1 — The ladder every claim in this book is measured against. The two bottom tiers are cheap and catch the crude failures, but an output can pass both and still be wrong. Correct is a word that gets earned at tier three, against data the workflow never saw, and the top tier cannot be automated because it is judgement doing the certifying. A claim holds the tier it passed, not the tier you intended.
- alt-text:      Five horizontal bars stacked as a ladder, read bottom to top, each naming a tier and the check that establishes it. Tier one, execution: it runs and the output is well-formed. Tier two, internal consistency: the invariants hold. Tier three, reproduces held-out truth by a split-sample test, marked as the first tier where the word correct is earned. Tier four, out-of-sample generalisation by a differential test. Tier five, independent adversarial scrutiny, where a reviewer tries to break the claim and fails, carried in reviewer purple. A bracket spans tiers one and two, labelled necessary but almost worthless alone; another spans three to five, labelled correctness earned here. An arrow up the side reads increasing evidential strength, and a footer reads that a claim holds the highest tier it actually passed, not the highest it could reach.
- infographic description: A flat vector ladder diagram, 16:9, off-white background.
                 Title top-left: "Five tiers of evidence for a workflow claim".
                 Standfirst: "A claim holds the highest tier it actually passed — not the
                 one you hoped for." Five horizontal bars stacked bottom to top, equal
                 width, each with a small vermillion diamond at its right edge. From the
                 bottom: "1 · execution — runs, output well-formed"; "2 · internal
                 consistency — invariants hold"; "3 · reproduces held-out truth —
                 split-sample test", annotated "the first tier where the word correct is
                 earned"; "4 · out-of-sample generalisation — differential test"; "5 ·
                 independent adversarial scrutiny — reviewer tries to break it", bordered
                 purple with a reviewer icon and annotated "cannot be automated —
                 judgement does the certifying". A vertical arrow to the left of the
                 ladder labelled "increasing evidential strength". A bracket to the right
                 spans tiers 1–2, "necessary — and almost worthless alone"; another spans
                 tiers 3–5, "correctness earned here". Footer: "the tiers are cumulative:
                 a tier-4 claim has passed 1 to 4". Sentence case throughout.
```

## 11.3 Verification must be external to the system verified

One principle holds the whole hierarchy together: verification must be external to the system being verified.

Chapter 1 introduced it, and it matters enough to restate as this chapter's governing rule.
A model asked whether its own output is right will answer fluently, with a confidence uncorrelated with whether the answer is true (Chapter 1).
The operational consequence is unforgiving.
No tier of the hierarchy may be established by the agent that produced the output, nor by an identical agent, nor by the same model prompted to check itself, because all three share the exact failure verification is meant to catch.
Each check has to draw its authority from a source the generating agent does not control: the schema at Tier 1 is fixed by the workflow's designer, not proposed by the agent at run time; the invariants at Tier 2 are physical or definitional facts external to the model; the held-out reference at Tier 3 is data the agent never saw; the transfer regime at Tier 4 is chosen by the evaluator to be unlike the development regime; and the reviewer at Tier 5 is independent by construction.
Where a check is implemented in code (a test suite, a schema validator, a mass-balance assertion), that code is itself an external artefact, written and reviewed under the governance of Chapters 7 and 12, and never generated and graded by the same agent in one unexamined step.

The best illustration of the principle in action comes from operational meteorology, and it is worth holding up as a template.
When a data-driven weather model arrived with impressive self-reported scores, forecast scientists did not take the vendor's numbers on trust.
They re-verified the model as an operational centre would: initialised from operational analyses rather than the reanalysis it was trained on, scored against both analyses and independent station observations with the centre's own standard metrics, and examined on case studies including extreme events.
They found it genuinely competitive, with documented weaknesses the training objective explained (Ben Bouallègue et al., 2024).
That is exactly what you have to do for an agentic workflow: re-verify the claim on your own data, under your own operating conditions, with your own metrics, before trusting it in production.
The parallel is exact, and it is why the environmental sciences are well placed to govern agents.
The verification culture already exists.
It only has to be extended to a new kind of instrument.

Externality is easier to state than to secure, and the subtlest threat to it is contamination of the held-out reference.
A split-sample test establishes nothing if the withheld data reached the model by another route.
If the reference values appear in the agent's context, in a file it retrieved, in a cached result from an earlier run, or, hardest of all to exclude, in the public material the underlying model was trained on, the test measures recall rather than reproduction, and reports a correctness the workflow does not have.
This has no clean counterpart in classical model evaluation, where the model cannot have memorised the validation record, and it is the main way the adaptation from the hydrological literature has to go beyond its source.
It is not hypothetical: audits of coding benchmarks have found that training-data contamination and repository familiarity can inflate scores, so that even an execution-grounded gate can report a capability the system does not independently possess (Zhu et al., 2025); a 2026 preprint that automated the audit across 168 benchmarks found the inflation large enough that removing the flawed tasks moved two widely used coding-benchmark scores by about ten percentage points (Wang et al., 2026; preprint).
Guarding against it needs the provenance discipline Chapter 12 specifies: know what entered the agent's context, record where each reference came from, and for the highest-stakes claims prefer held-out data generated after the model's training cut-off, or held under conditions that make prior exposure implausible.
The honest limitation is that contamination can rarely be excluded with certainty for a closed model whose training corpus is unknown.
So treat freedom from contamination as a claim with its own confidence level, raise that confidence by controlling the routes you can control, and weight a Tier 3 result accordingly rather than reading it at face value.

## 11.4 Building a task-grounded evaluation set from the group's own workflow

If task-grounded evaluation is the answer, the evaluation set is the instrument, and most groups do not have one.

An evaluation set is a curated collection of cases, each an input paired with an outcome already known to be right, run against a workflow to see how it performs on the kind of work you actually do.
The raw material is almost certainly already to hand, scattered through the workflow's own history, so the job is to gather and discipline it rather than to invent it.
Working practitioners have converged on the same low-cost starting move: practitioner guidance describes testing an agent against roughly ten self-completed, known-answer examples before removing the human from a workflow's loop, then graduating its autonomy by the score (practitioner commentary; see the references).

> **Definition — Evaluation set.** A fixed, curated set of test cases, each an input paired with an already-trusted answer, run against a workflow to measure how well it performs on the group's kind of work. It is the difference between "the agent seemed to do well" and "the agent reproduced the right answer on forty-seven of fifty cases chosen in advance". It is built once, guarded, and reused.

The first step is to **harvest cases**, and four sources are already available.
Past runs whose outcomes a human eventually settled are the richest, because every time somebody adjudicated an agent's output as right or wrong, a labelled case was created.
The outputs of the manual workflow the agent is meant to replace or assist supply references too, since the pre-agent way of doing the job produced answers you already trust.
Your failure log serves the same end, and the failure gallery of Chapter 13 is exactly this kind of record: every catalogued incident is a case the workflow must not get wrong again.
And a small held-back set of known-correct items generalises Chapter 5's discipline of holding back a handful of known-relevant papers to test whether retrieval finds them.

The second step is to **curate** each case into a fixed shape: the input, the reference outcome, the metric that decides pass or fail fixed in advance, and the provenance of the reference, meaning where the "right answer" came from and how far it is trusted.
A reference is only as good as its own pedigree.

The third step is to **stratify** the set across task types and regimes so it spans the conditions the workflow will actually meet.
This is the differential-split discipline of Klemeš's testing scheme [verify] applied to an evaluation set rather than a single model, and it is what stops a set of all-easy interpolation cases certifying a workflow that collapses on the hard ones.

Two disciplines keep the set honest.

First, report the set's **size** candidly.
A few dozen carefully curated cases beat zero by an enormous margin, but small samples carry wide uncertainty, so report a result with an interval rather than a bare percentage.
"Forty-four of fifty, which is an 88% pass rate with a 95% interval of roughly 76 to 95%" says far more than "88%".
The design principles of verifiable-answer benchmarks are a useful guide to what makes a good case: an unambiguous, pre-registered, automatically checkable reference, and difficulty graded by the number of steps and tools a case demands (Mialon et al., 2023), so that "does the agent retrieve the correct discharge value from this archive?" has a checkable answer in exactly that sense, whereas "is this synthesis insightful?" does not, and belongs to Tier 5.
Second, the set is **versioned and refreshed** and guarded against contamination per §11.3: what entered context on each run is recorded, references generated after the model's training cut-off are preferred, and the set is re-examined when the workflow's inputs change, because an evaluation set that never changes slowly stops resembling the work.

**Figure 11.2 — Building a task-grounded evaluation set.**

![A left-to-right assembly line. Four source cylinders, settled past runs, manual-workflow outputs, the failure log and a known-correct hold-back, feed a curate step, annotated that each case gets an input, a reference, a metric fixed in advance and the provenance of that reference. A stratify step follows, annotated as spanning the regimes the workflow will actually meet, then a versioned evaluation set with a held-out slice, annotated with the contamination warning that the reference must be absent from anything the model could have seen. The set feeds a gate in front of the live workflow, annotated that this is the gate whose false-negative rate section 11.5 measures. A loop arrow returns to version and refresh, annotated with the re-measurement triggers.](../figures/figure-11-2.svg)

*Figure 11.2 — You already own the raw material for an evaluation set. Settled runs, the outputs of the manual workflow the agent replaced, your failure log and a held-back set of known answers get curated into cases, stratified across regimes so the easy ones cannot certify the set, and versioned. The held-out slice carries the warning that matters: withheld means absent from everything the model could have seen. (Rendered as `figures/figure-11-2.svg` from the brief below, per `FIGURES.md`.)*

```
FIGURE BRIEF
- id:            Figure 11.2
- title:         An evaluation set built from the workflow's own history
- type:          architecture
- claim:         A task-grounded evaluation set is assembled from the workflow's own history through harvest, curate, stratify, hold out and version, and then feeds the tiered checks.
- standfirst:    The raw material is already in your history. The work is gathering and disciplining it.
- canvas:        16:9
- elements:      left, four sky-blue cylinders — "settled past runs", "manual-workflow
                 outputs", "failure log (Ch.13)", "known-correct hold-back"; a grey
                 "curate" step; a grey "stratify" step; a sky-blue "stratified evaluation
                 set" cylinder with a marked "held-out slice"; a "version + refresh" loop;
                 a vermillion "gate" before a "live workflow" box
- flow:          left-to-right — four sources → curate → stratify → versioned set (with a
                 held-out slice) → gate → live workflow; a loop arrow returns from the set
                 to "version + refresh"
- labels:        "settled past runs", "manual-workflow outputs", "failure log (Ch.13)",
                 "known-correct hold-back", "curate", "stratify by task and regime",
                 "stratified evaluation set", "held-out slice", "version + refresh",
                 "gate", "live workflow"
- annotations:   on curate, "each case: input · reference · metric fixed in advance ·
                 provenance of the reference"; on stratify, "spans the regimes the
                 workflow will actually meet — easy cases cannot certify it"; on the
                 held-out slice, in vermillion, "withheld means absent from anything the
                 model could have seen (§11.3)"; on the gate, "the gate §11.5 measures";
                 on the loop, "refresh on model, prompt or data-regime change"
- caption:       Figure 11.2 — You already own the raw material for an evaluation set. Settled runs, the outputs of the manual workflow the agent replaced, your failure log and a held-back set of known answers get curated into cases, stratified across regimes so the easy ones cannot certify the set, and versioned. The held-out slice carries the warning that matters: withheld means absent from everything the model could have seen.
- alt-text:      A left-to-right assembly line. Four source cylinders, settled past runs, manual-workflow outputs, the failure log and a known-correct hold-back, feed a curate step, annotated that each case gets an input, a reference, a metric fixed in advance and the provenance of that reference. A stratify step follows, annotated as spanning the regimes the workflow will actually meet, then a versioned evaluation set with a held-out slice, annotated with the contamination warning that the reference must be absent from anything the model could have seen. The set feeds a gate in front of the live workflow, annotated that this is the gate whose false-negative rate section 11.5 measures. A loop arrow returns to version and refresh, annotated with the re-measurement triggers.
- infographic description: A flat vector pipeline diagram, 16:9, off-white background.
                 Title top-left: "An evaluation set built from the workflow's own
                 history". Standfirst: "The raw material is already in your history. The
                 work is gathering and disciplining it." At the left, four sky-blue
                 cylinders stacked: "settled past runs", "manual-workflow outputs",
                 "failure log (Ch.13)", "known-correct hold-back". Arrows converge on a
                 grey rounded rectangle "curate", annotated "each case: input · reference
                 · metric fixed in advance · provenance of the reference". Then a grey
                 rounded rectangle "stratify by task and regime", annotated "spans the
                 regimes the workflow will actually meet — easy cases cannot certify it".
                 Then a sky-blue cylinder "stratified evaluation set" with a hatched band
                 "held-out slice" carrying a vermillion annotation "withheld means absent
                 from anything the model could have seen (§11.3)". A loop arrow returns
                 above it to a tag "version + refresh", annotated "refresh on model,
                 prompt or data-regime change". The set feeds a vermillion diamond "gate",
                 annotated "the gate §11.5 measures", then a box "live workflow".
                 Sentence case throughout.
```

## 11.5 Measuring the gate itself

This is the promise the book has been deferring, and here it comes due.

Chapter 5 said that evaluating the gate itself, meaning how to measure its false-negative rate and how much verification a given synthesis warrants, is developed in Chapter 11.
Chapter 10 left its reviewer base rates awaiting measurement, and claimed that a reviewer which almost never returns a fault is evidence of a broken reviewer rather than a flawless producer.
This section pays both debts.
The question underneath them is the one every gate in the book quietly assumes an answer to.
When a gate says *pass*, how often is it wrong?

> **Definition — False-negative rate.** For a gate whose job is to catch bad work, the false-negative rate is how often it waves bad work through, saying "pass" when it should have said "fail". It is the number that matters most and the one most often left unmeasured, because a gate that never complains looks like a gate that works, right up to the point where it is found to have been asleep.

State the evidence honestly first, because it shapes the whole answer.
When the first `/research` sweep behind this book was compiled, no study directly measured an LLM review gate's false-negative rate.
By mid-2026 the first direct measurements were appearing, though none of them measures the work your group actually does.
The sharpest separated whether a coding agent submitted a patch at all from whether the patch actually passed the repository's held-out tests: across 1,750 trajectories on 50 real tasks, four frontier models submitted a patch 70 to 100% of the time while resolving the issue only 18 to 50% of the time, and these silent semantic failures, confidently wrong and stable across repeats, made up 68 to 80% of every model's failures (Mehta, 2026; a preprint, coding-domain figures that transfer structurally, not numerically).
So the two cheap signals you reach for first, whether it finished and whether it repeats, look healthiest exactly when the output cannot be trusted, because a silent semantic failure both completes and repeats.
The grader side is measured too: an automated audit of 168 benchmarks found defects in over a quarter of their tasks, meaning the gate itself was measurably wrong (Wang et al., 2026; preprint).
None of that measures a particular gate on your group's work, so the number you need has to be made rather than borrowed.
The method is the ordinary one of instrument science: calibrate the measuring instrument against known inputs before trusting its readings.

The method is **seeded-defect testing**, and it is disarmingly simple.
Take inputs you know to be sound and plant in them known faults of exactly the classes the gate is supposed to catch: a fabricated citation, a unit slip, an out-of-range value, a dropped constraint.
Run the gate blind.
Count how many planted faults it misses.
Stratify the seeding by fault class, because a gate can be strong on one class and blind to another.
A citation-verification gate that resolves every DOI may still wave through a unit error it was never built to see, and a single headline miss rate would hide that.
This is the same logic the agentic-benchmark-validity literature applies to graders themselves.
Audits of popular benchmarks found that weak test coverage or lenient matching let failing work score as success, an error that is quantifiable and reducible by systematic audit, and applying a structured checklist to one benchmark cut its performance overestimation by a third (Zhu et al., 2025).
A gate is an instrument with a measurable error rate, and seeded defects are how you measure it.

> **Definition — Seeded-defect testing.** Known mistakes are deliberately planted into otherwise-correct work (a made-up reference, a wrong unit, a value outside the plausible range) and the check is run over it without being told where the mistakes are. A count is then taken of how many it caught. It is the fire drill for a verification gate: the only way to establish that an alarm works is to set off a controlled fire.

Report the measurement the way you would report any measurement on a small sample, with its uncertainty attached.
This is not a nicety.
The numbers are usually small, because only so many faults can be seeded by hand, and small samples are treacherous in a way that specifically flatters a gate.
Suppose you seed twenty faults of a given class and the gate catches all twenty.
The tempting conclusion is a zero miss rate, and it is wrong.
With zero misses in twenty trials, the upper 95% bound on the true miss rate is roughly 3 in 20, about 15%, by the "rule of three" for zero events.
The honest statement is not "this gate never misses" but "this gate's miss rate for this fault class is below about 15%, and tightening that bound needs more seeded faults".
That interval is the whole point, and it is why a clean sweep on a handful of seeded defects licenses far less confidence than it looks like it does.

The judge-bias literature supplies the calibration experiments to run alongside the seeding, and they are cheap.
The founding study of using a strong model as an automated judge measured its agreement with humans and also documented its systematic biases: a preference for the answer presented first, a preference for longer answers regardless of quality, and a preference for the judge's own style of output.
It proposed partial fixes with measured, incomplete effect (Zheng et al., 2023).
A later study measured position bias at scale and gave two tests any group can run on its own gate: repeat-stability (does the gate return the same verdict on identical repeats?) and order-swap consistency (does the verdict survive swapping the order of two candidates?), finding that the bias concentrates precisely where candidates are close in quality, that is, on the borderline cases that matter most at a gate (Shi et al., 2024).
A third study named the trap in the cheapest reviewer configuration of all: judges favour outputs that "sound like them", assigning higher scores to text of lower perplexity under their own distribution even when another model wrote it, so using the same model family to draft and to review is structurally biased towards approval (Wataoka et al., 2024).
The largest judge evaluation to date, covering 21 models, nine providers and some 541,000 judgements, sharpens all of this (Norman, Rivera and Hughes, 2026; a preprint, on general chat and question-answering tasks, not scientific artefacts).
Exact-match agreement overstates chance-corrected agreement, that is, Cohen's kappa, the agreement left once the score two coin-flippers would reach by luck is subtracted, by 33 to 41 percentage points, so every agreement figure, the founding study's included, must be read chance-corrected.
Its titular finding is starker: production judges with test-retest reliability above 0.95 coexisted with severe position bias, so a gate can be dependably wrong in a fixed direction while a naive self-consistency check certifies it, because consistency is evidence about reliability and none about correctness.
A companion 2026 study adds a bias the field had underweighted: style bias, a preference for formatted answers over the same content in plain prose, was the largest it measured (0.10 to 0.76 across five judges), so a reviewer gate can be gamed with headers and bullet points alone (Soumik, 2026; preprint).
The design implication is blunt.
Genuine independence needs model diversity, not just a fresh context window, and this is the measured evidence behind the reviewer-independence rules of Chapters 7 and 10.

The strongest peer-reviewed result on automated review to date is worth stating for how narrow it is: an automated reviewer reached 69% balanced accuracy against expert consensus on conference-review decisions, just above the 66% of the humans it was benchmarked against, a striking figure but one from workshop-tier machine-learning reviewing, not a measure of scientific correctness (Lu et al., 2026, *Nature*).

Seeded defects measure what a gate catches under test.
The **yield diagnostic** watches what it catches in live work, and the two together are how you know a gate is still working.
Chapter 5's checklist set up the "Yield" check and Chapter 10 set up its twin: a gate or reviewer that almost never fires on real work is evidence of a broken check, not of flawless upstream work.
The most useful published analogue is from systematic-review automation, where a screening step's *sensitivity* is precisely one minus its false-negative rate: a 2025 study reported an automated screening gate at around 97% sensitivity against a dual-human baseline near 82%, which is exactly a review gate's false-negative rate being measured and compared, though the study is a preprint from the tool's own developers and its numbers should be read with that in mind (Cao et al., 2025).
Watching yield over time turns the same idea into a standing alarm.
If a citation gate stops rejecting anything, either the drafting genuinely improved or the gate quietly broke, and you cannot tell which without seeding it again.
So re-measurement is not optional, and it needs a trigger list: after any model change, after any prompt change, after a change in the data regime the workflow runs on, and on a calendar besides.
Models drift, prompts go stale, and the work moves.

How much of this effort a given output deserves is not a separate question.
It is the tier-and-stakes matching of §11.7, and the chapter closes that loop there.
For now the principle is this: a tier claim is only ever as strong as the measured check that establishes it.
A Tier 3 result gated by an unmeasured citation check is a Tier 3 result in name only, and measuring the gate is what turns the ladder of §11.2 from a description of ambition into a record of evidence.

**Figure 11.3 — Measuring a gate by seeded defects.**

![A five-step measurement sequence. Step one, a person seeds known faults into sound inputs, listing the classes: a fabricated citation, a unit slip, an out-of-range value, a dropped constraint, annotated stratified by class because a gate can be strong on one and blind to another. Step two, the inputs run through the gate blind. Step three, the gate returns pass or fail per input. Step four, a tally records catches and misses by class, with a vermillion note that a gate which never fires on live work is a broken gate, not a clean corpus. Step five, the rate is reported with its uncertainty, annotated that zero misses in twenty trials still means the true miss rate could be about fifteen percent. A footer lists the re-measurement triggers: any model change, any prompt change, any data-regime change, and a calendar.](../figures/figure-11-3.svg)

*Figure 11.3 — Calibrating the gate like the instrument it is. You plant faults you know about, run the gate blind, and count what it misses, class by class. The two honesty rules are on the canvas: a clean sweep on twenty seeded faults still leaves a possible miss rate near fifteen percent, and a gate that never fires on real work is evidence of a broken gate, not of flawless upstream work. (Rendered as `figures/figure-11-3.svg` from the brief below, per `FIGURES.md`.)*

```
FIGURE BRIEF
- id:            Figure 11.3
- title:         Seeded-defect measurement of a verification gate
- type:          sequence
- claim:         A gate's false-negative rate is measured by seeding known defects into sound inputs, running the gate blind, tallying catches and misses, and reporting a rate with its uncertainty.
- standfirst:    The only way to know an alarm works is a controlled fire.
- canvas:        16:9
- elements:      three actors as lanes — a human (blue) who seeds faults; the gate under
                 test (vermillion diamond); a tally record (sky-blue cylinder); five
                 numbered steps crossing between them
- flow:          top-to-bottom, numbered — (1) human plants known faults of named classes
                 into sound inputs; (2) inputs run through the gate blind; (3) gate
                 returns pass/fail per input; (4) tally records catches and misses by
                 class; (5) rate reported with an interval
- labels:        "seed known faults — fabricated citation · unit slip · out-of-range ·
                 dropped constraint", "run gate blind", "pass / fail per input",
                 "tally catches & misses by class", "report rate + interval",
                 "re-measure on: model change · prompt change · data-regime change ·
                 calendar"
- annotations:   on step 1, "stratified by class — a gate can be strong on one and blind
                 to another"; on step 2, "the gate is not told where the faults are"; on
                 step 4, in vermillion, "a never-firing gate is a broken gate, not a clean
                 corpus"; on step 5, "zero misses in twenty trials still means the true
                 miss rate could be ~15%"; a footer with the re-measurement triggers
- caption:       Figure 11.3 — Calibrating the gate like the instrument it is. You plant faults you know about, run the gate blind, and count what it misses, class by class. The two honesty rules are on the canvas: a clean sweep on twenty seeded faults still leaves a possible miss rate near fifteen percent, and a gate that never fires on real work is evidence of a broken gate, not of flawless upstream work.
- alt-text:      A five-step measurement sequence. Step one, a person seeds known faults into sound inputs, listing the classes: a fabricated citation, a unit slip, an out-of-range value, a dropped constraint, annotated stratified by class because a gate can be strong on one and blind to another. Step two, the inputs run through the gate blind. Step three, the gate returns pass or fail per input. Step four, a tally records catches and misses by class, with a vermillion note that a gate which never fires on live work is a broken gate, not a clean corpus. Step five, the rate is reported with its uncertainty, annotated that zero misses in twenty trials still means the true miss rate could be about fifteen percent. A footer lists the re-measurement triggers: any model change, any prompt change, any data-regime change, and a calendar.
- infographic description: A flat vector sequence diagram, 16:9, off-white background.
                 Title top-left: "Seeded-defect measurement of a verification gate".
                 Standfirst: "The only way to know an alarm works is a controlled fire."
                 Three lane headers: blue human "scientist", vermillion diamond "gate
                 under test", sky-blue cylinder "tally". Five numbered steps top to
                 bottom, each an arrow with its annotation beneath: "1 seed known faults —
                 fabricated citation · unit slip · out-of-range · dropped constraint" /
                 "stratified by class — a gate can be strong on one and blind to another";
                 "2 run gate blind" / "the gate is not told where the faults are"; "3 pass
                 / fail per input"; "4 tally catches & misses by class" with a vermillion
                 note "a never-firing gate is a broken gate, not a clean corpus"; "5
                 report rate + interval" / "zero misses in twenty trials still means the
                 true miss rate could be ~15%". Footer: "re-measure on: model change ·
                 prompt change · data-regime change · calendar". Sentence case.
```

## 11.6 Worked example — measuring a rainfall-forecast-verification gate

The abstract method earns its keep only on a real workflow.
So this section walks one pass through §§11.4–11.5 in operational meteorology, with the structure written out and every number left where it belongs, which is with the author.
Inventing an illustrative catch rate would be exactly the fabrication this book forbids.

The workflow step is verifying a rainfall forecast against observations, a stage from the operational work running through Part IV.
The gate under scrutiny is the check deciding whether a computed verification score is trustworthy before it gets reported.

Building the evaluation set followed §11.4.
Cases were harvested from settled past runs where a human had already adjudicated the score as right or wrong, from the manual verification the workflow replaces, and from the group's own log of past mistakes.
Each was curated as an input, a reference score, a metric fixed in advance, and the provenance of that reference.
The set was stratified across the regimes that matter for rainfall, meaning light and heavy events, different seasons and different station densities, so it would not certify a gate on easy cases and stay silent on the hard ones.
**[AUTHOR: the number of curated cases, the exact stratification you used, and where the reference scores came from — this is the concrete evaluation set, and only you have it.]**

Measuring the gate followed §11.5.
Defects of the classes this gate has to catch were seeded into otherwise-sound inputs: a unit mismatch between forecast and observation, an out-of-range accumulation, a mis-paired station-and-grid-cell, a silently dropped quality-control flag.
The gate was run blind, and catches and misses were tallied by class.
**[AUTHOR: the fault classes you actually seeded, how many of each, and the measured catch rate per class with its interval — report zero-miss results as an upper bound per the rule of three, not as a clean zero.]**
The yield diagnostic ran alongside it.
Over the same period the base rate at which the gate rejected real, unseeded work was recorded, because a gate that fires only on planted faults and never on live runs is a gate calibrated to catch exactly the mistakes you already knew about and nothing else.
**[AUTHOR: your observed real-world yield — the base rate at which the gate rejects live work — and, if you have it, the contrast between a well-configured cross-family reviewer and a naive same-model one, which is the measurement Chapter 10 asked for.]**
Beyond the numbers, the lesson is this.
The most valuable outcome of seeding a gate you already trust is finding a fault class it silently misses.
That miss is worth more than any pass, because it shows you where the instrument is blind before an operational result does.
**[AUTHOR: recount what actually happened when you first calibrated one of these gates — which fault class, if any, it missed, and what you changed as a result. This is the lived detail that makes the section real; leave it to your own experience rather than a generic illustration.]**

## 11.7 Operating the ladder in practice

The hierarchy is a way of allocating verification effort deliberately, not a demand that every output climb to the top.
Using it well means matching the tier reached to the stakes of the decision the output informs.

Climbing costs, and the cost structure is the one Chapter 4 set out.
Tiers 1 and 2 are cheap and largely automatable and should be applied to essentially everything, because a schema check and an invariant assertion cost little and catch the crudest and some of the most dangerous failures.
Tier 3 costs whatever it costs to hold out and curate reference data, and is warranted wherever a quantitative result will be reported or acted on.
Tier 4 costs the design of a genuine transfer test, and is warranted wherever the workflow will be applied outside the regime it was built in, which, for operational environmental work, is the common case rather than the exception.
Tier 5 costs scarce expert attention and is reserved for claims whose failure would be consequential: a result headed for publication, a warning informing a decision, a configuration about to enter routine operation.
A workflow that stops at Tier 2 for an exploratory triage is properly governed.
The same workflow stopping at Tier 2 for a published result is not.
The cost-awareness literature reinforces this from the evaluation side: report accuracy and cost together rather than accuracy alone, because agent costs vary by orders of magnitude at similar accuracy (Kapoor et al., 2024).
The same discipline that stops you paying for a wasteful scaffold stops you paying for verification a triage result does not need.

Record the tier reached alongside the output, as part of its provenance (Chapter 12).
Then a later reader, whether a reviewer, a successor, or you six months on, can see not just what the workflow concluded but how strong the evidence for it was, and can judge whether the tier attained matches the use now being made of it.
That record is also what makes the failure gallery of Chapter 13 legible: nearly every failure there is an output trusted at a tier above the one its evidence actually supported, and naming the tier is the discipline that prevents it.

One refinement from §11.5 ties the chapter together.
A tier claim is only ever as strong as the measured check that establishes it.
Reaching Tier 3 through a citation gate whose false-negative rate has never been measured is reaching Tier 3 on faith.
The whole apparatus of seeded defects and yield exists to turn that faith into a defensible number, so recording "Tier 3" in an artefact's provenance records a check that has been calibrated rather than one that has merely been hoped about.
One boundary is easy to blur and worth drawing.
A confidence-scored agent output ("I am 80% sure this flag is correct") is a different and less mature capability than a pass/fail gate.
Uncertainty quantification for agents is an open research field, catalogued by a 2026 peer-reviewed survey as foundations and challenges rather than working methods, so never treat a self-reported confidence number as a measured gate (Oh et al., 2026).
And state the limitation plainly: the hierarchy governs evidential strength, not importance.
It can establish how well supported a claim is.
It cannot establish whether the claim is the one that matters, which stays a matter of scientific judgement no tier, and no agent, can supply.

## 11.8 Verification checklist

This checklist certifies that a workflow's evidential claims rest on measured, external checks rather than assertion.
A colleague who did not build the workflow should be able to apply it from the record alone.

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
The runnable material is an evaluation-set template, meaning the case shape of §11.4 with fields for input, reference, metric and provenance, together with a seeded-defect harness that plants faults of named classes, runs a gate blind, and reports catch rates with intervals per §11.5.
Both are written to be adapted to your own gate rather than run as-is.
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
