# Chapter 8 — Model orchestration and experimentation

> **Status:** draft r4 · voice v4.0-colloquial (`STYLE.md` §0) · sentence-per-line per `STYLE.md` §10 · figures as briefs per `FIGURES.md`.
> **Conventions:** vendor-neutral (outline §9) · **[AUTHOR: …]** marks lived material only the author can supply · **[verify]** marks real but unconfirmed details · citations drawn only from verified reports in `/research`. Nothing has been invented.
> **Chapter note:** the three-track intercomparison of §8.5 is a **worked design**, not an executed case study: it presents an architecture and a protocol and claims no results.

---

## 8.1 The problem: campaigns that outgrow their bookkeeping

The hard part of modern environmental modelling is not running a model once.
It is running it correctly hundreds or thousands of times while keeping an exact account of what was run.

A calibration campaign for a distributed hydrological model may sweep a dozen parameters across plausible ranges.
An ensemble forecast perturbs initial conditions, physics options and boundary forcings.
A structured intercomparison holds a domain and a period fixed while varying the model itself.
Every one of these is combinatorial in a way that defeats manual tracking: a modest sweep of six parameters at five values each is already 15,625 configurations before any ensemble dimension is added, and a realistic campaign adds resolution, forcing dataset and spin-up length on top.

The scientific content of that work is small in proportion to its bookkeeping.
The decisions that matter, meaning which parameters to vary, which metric to optimise and which result to believe, take a fraction of the effort.
The rest is mechanical: launching runs, naming their outputs, recording their configurations, noticing which ones failed, and reconciling the survivors into a table you can actually reason about.
Anyone who has run a calibration campaign to a deadline knows what happens next.
Provenance is the first casualty of scale.
Configurations drift between runs because a setting was changed by hand and never written down.
Outputs pile up under names that meant something to their author for about a week.
A promising result cannot be reproduced because the exact forcing version that produced it was overwritten.
None of that is a failure of scientific understanding.
It is a failure of clerical discipline under load, and it is exactly what a well-specified instrument should be able to absorb (high confidence).

Pairing agents with modelling is no longer hypothetical.
By 2026 the peer-reviewed hydrology literature had begun testing language-model agents inside calibration workflows themselves (Zhu et al., 2026 [verify]), which makes the governance question in this chapter timely rather than speculative.
The same year, a hydrology preprint defined a six-level framework of autonomy for agents that operate a model directly, and demonstrated a high level of it retrospectively on a real flood event (Yan et al., 2026 [verify]).
These first-wave domain papers are capability-first.
They show what an agent can be made to do, with almost none of the governance apparatus this chapter builds, which is the gap this book exists to fill.
The argument here is that orchestration and record-keeping, meaning the scheduling, logging and anomaly-flagging around a modelling campaign, can be delegated to an agent, while the scientific decisions inside the campaign cannot.
The whole design problem is separating the two cleanly enough that the delegation is safe.

> **Definition — Intercomparison.** A controlled comparison in which several models are run on the same problem (the same domain, the same period, the same inputs) so that the only thing allowed to differ is the model itself. It is how a field works out which approach is genuinely better, rather than which happened to be tested on the easier case. Keeping every other condition identical is the whole discipline.

## 8.2 The conventional workflow

The conventional way to run a modelling campaign is a loose arrangement of shell scripts, scheduler submissions and a growing spreadsheet, held together by one scientist's memory and vigilance.

A campaign usually starts with a template configuration copied and edited for each run, a submission script that hands the run to a cluster scheduler, and an output directory whose structure is invented on the spot and rarely documented.
Progress gets tracked by whatever comes to hand: a spreadsheet of run identifiers and parameter values kept by hand, a naming convention for output directories, and periodic manual inspection of scheduler queues and log files to see which runs completed and which died.
The strengths of that are real and worth keeping in view.
It is transparent, it uses tools you already know, and it needs no infrastructure beyond what the computing environment already provides.
Its weaknesses appear only at scale and under time pressure, which is exactly when campaigns get run.
The manual spreadsheet and the actual runs diverge silently, because nothing enforces their correspondence.
A run that fails partway leaves a truncated output that looks like a success until you open it.
The link between a configuration and the exact software version, forcing dataset and random seed that produced its output lives in your head, or nowhere.
On a large campaign you spend a substantial, unmeasured share of the effort on reconciliation rather than on the modelling (moderate confidence; the fraction varies widely by group and tooling).
**[AUTHOR: a concrete figure or vignette from an operational calibration campaign — how many runs, how much of the week went to bookkeeping — would anchor this.]**
The deeper problem is that the record gets reconstructed afterwards rather than captured as the campaign runs.
By the time you have to defend a result to a reviewer, a funder or a colleague inheriting the project, the provenance has to be pieced together from directory timestamps and half-remembered decisions, a process Chapter 12 treats properly.
That is what the agentic redesign addresses, and it does so not by making the scientific decisions but by capturing the record manual working loses.

## 8.3 The agentic redesign: monitor and log, do not decide

The governing principle of this chapter is a deliberate, narrow division of labour: the agent orchestrates and records, and you decide.

An orchestration agent, as used here, is a system built around a language model that may expand a specified experimental design into concrete run configurations, submit those runs to a scheduler through defined tools, monitor their progress, capture each run's full configuration and environment as a provenance record, and flag anomalies for human attention.
It may do nothing else.
It does not choose which parameters to vary.
It does not decide which metric defines skill.
It does not prune the design because early results look unpromising.
It does not judge that a run's output is scientifically acceptable.
Every one of those is a scientific decision reserved to the human, and the workflow is built so the agent has neither the authority nor the tools to make them.

This is not timidity about model capability.
It is a considered choice about where the human keeps control, and it rests on the argument of Chapter 1.
The tasks given to the agent (expanding a declared grid, tracking job states, recording configurations, checking outputs against mechanical validity criteria) are cheap to verify and checkable.
The tasks withheld from it are expensive to verify and fail by imitating competence.
Be clear that this is a more conservative division than some prominent demonstrations adopted.
The flagship 2023 result, in which a language-model system planned and ran real chemistry experiments end to end, let the agent adjust its own plans in response to instrument feedback (Boiko et al., 2023).
The monitor-and-log role here is deliberately narrower, because chemistry's fast, unambiguous feedback is a luxury environmental field science rarely gets.
There is now a strong in-domain demonstration too.
A 2026 preprint used an agentic system for the exploratory design work of a seasonal streamflow forecaster, meaning dataset discovery, knowledge synthesis and architecture search, while the forecaster itself stayed a conventional, interpretable statistical model.
Benchmarked against a government agency's operational forecasts over 2021–25, it cut quantile error for early-season runoff by up to 29% (Lopez-Gomez et al., 2026).
That is a single-region result from a preprint, so the figure is dated and place-specific, but the shape is the point: the agent designs, the auditable model forecasts, which is the division this section argues for.

Structured action is what makes the delegation possible, because the agent emits machine-readable calls to a scheduler and a provenance store rather than prose about what it would do.
The same structure makes the delegation auditable, because every action it takes is a logged tool call.
The payoff is that provenance becomes a by-product of running the campaign rather than a chore alongside it.
The record is captured the moment each run launches, from the configuration actually used, with the software version, forcing dataset identifier and random seed attached, so reproducing a result means replaying a record rather than reconstructing a memory (high confidence in the pattern; completeness of the record depends on the tools exposed).
Figure 8.1 shows the architecture, and the boundary it draws, between the orchestration the agent performs and the decisions you keep, is the most important design commitment in the chapter.

**Figure 8.1 — The orchestration agent and its boundary.**

![An architecture diagram centred on an orange orchestration-agent box holding four tool glyphs for expanding a design, submitting runs, tracking state and recording provenance. A scientist icon on the left authors an experimental design that feeds the agent; the agent connects down to an HPC scheduler and a provenance store, and right to a vermillion anomaly-flag diamond that routes back to the scientist. A grey dashed boundary around the agent is labelled as containing no scientific decisions.](../figures/figure-8-1.svg)

*Figure 8.1 — The orchestration agent expands a human-authored design, submits and tracks runs, and records provenance; anomalies are flagged to the scientist, not resolved. The dashed boundary marks what the agent may do; scientific decisions stay outside it. (Rendered as `figures/figure-8-1.svg` from the brief below, per `FIGURES.md`.)*

```
FIGURE BRIEF
- id:            Figure 8.1
- title:         What the orchestration agent does, and what it never does
- type:          architecture
- claim:         The agent schedules, tracks and records a modelling campaign but makes no scientific decision; every scientific choice is a human gate outside the agent's authority.
- canvas:        16:9
- elements:      a central orange-bordered rounded rectangle "orchestration agent" containing
                 four green tool glyphs labelled "expand design", "submit runs",
                 "track state", "record provenance"; feeding into the agent from the left,
                 a blue "experimental design" tag authored at a blue human head-and-shoulders
                 icon "scientist"; below the agent a green cluster/scheduler glyph
                 "HPC scheduler" and a sky-blue cylinder "provenance store"; to the right,
                 a vermillion diamond "anomaly flag" whose "flag" exit leads to the same blue
                 "scientist" icon; a grey dashed boundary around the agent labelled
                 "no scientific decisions inside this boundary"
- flow:          left-to-right — scientist authors design → agent expands and submits to
                 scheduler → agent tracks state and writes provenance → agent flags anomalies
                 back to scientist; decisions (which design, which metric, which result to
                 believe) sit with the scientist, outside the dashed boundary
- labels:        "scientist", "experimental design", "orchestration agent", "expand design",
                 "submit runs", "track state", "record provenance", "HPC scheduler",
                 "provenance store", "anomaly flag", "flag", "no scientific decisions inside
                 this boundary"
- annotations:   the grey dashed boundary is the callout; it encloses only the agent and its
                 tools, never the scientist icon or the anomaly decision
- caption:       Figure 8.1 — The orchestration agent expands a human-authored design, submits and tracks runs, and records provenance; anomalies are flagged to the scientist, not resolved. The dashed boundary marks what the agent may do; scientific decisions stay outside it.
- alt-text:      An architecture diagram centred on an orange orchestration-agent box holding four tool glyphs for expanding a design, submitting runs, tracking state and recording provenance. A scientist icon on the left authors an experimental design that feeds the agent; the agent connects down to an HPC scheduler and a provenance store, and right to a vermillion anomaly-flag diamond that routes back to the scientist. A grey dashed boundary around the agent is labelled as containing no scientific decisions.
- generator prompt: A flat vector architecture diagram on an off-white background. In the
                 centre, an orange-bordered rounded rectangle labelled "orchestration agent"
                 contains four small green tool glyphs labelled "expand design", "submit runs",
                 "track state" and "record provenance". A grey dashed rounded boundary encloses
                 only this rectangle, labelled beneath "no scientific decisions inside this
                 boundary". On the left, a blue head-and-shoulders icon labelled "scientist"
                 connects through a small blue tag labelled "experimental design" into the
                 agent. Below the agent, a green cluster glyph labelled "HPC scheduler" and a
                 sky-blue cylinder labelled "provenance store" connect upward to it. On the
                 right, a vermillion diamond labelled "anomaly flag" has one exit labelled
                 "flag" curving back to the blue "scientist" icon. Single-weight connectors,
                 one arrowhead style, generous spacing, minimal text.
```

## 8.4 LLM-assisted hypothesis generation, kept exploratory

A second, more contentious use of language models in experimentation is generating hypotheses.
This book allows it only under strict conditions, and never as evidence.

A model prompted with a campaign's results, the relevant literature and a domain description will readily propose mechanisms: that a calibrated parameter is compensating for a missing process, that a data-driven model's skill in one regime reflects a spurious correlation, that two error patterns share a common cause.
Some of those will genuinely help in deciding where to look next.
The value is real but narrow.
It is the value of a well-read colleague suggesting avenues over coffee, and it comes with the same reservation: a suggestion is a prompt to investigate, never a finding.
The danger is that a generated hypothesis, expressed fluently and arriving alongside real results, picks up an unearned evidential status simply by sitting next to them, so what started as a conjecture gets reported as a conclusion.
That failure is named and dissected in §8.6 as hypothesis laundering.

So the discipline here is procedural rather than a matter of good intentions.
Any model-generated hypothesis is recorded as exploratory in the provenance store, tagged with its origin, and kept separate by construction from the evidential chain.
It cannot enter a result or a manuscript until a human has tested it against data by a pre-specified procedure and taken personal responsibility for the claim.
This mirrors the interpretive control kept in the literature-synthesis pattern of Chapter 5 and the author-as-sole-authority principle of Chapter 9, and it is enforced by the same mechanism that carries the provenance: a generated hypothesis lives in a labelled compartment of the record, visibly not among the findings.
Confidence in this recommendation is high, as a matter of research integrity, and it does not depend on model quality.
Better models do not remove the failure it guards against.
A more persuasive model makes an untested hypothesis more dangerous, not less, because its fluency disguises the missing evidence more effectively.
Figure 8.2 shows the gate that keeps a generated hypothesis out of the evidential chain until a human has tested it.

**Figure 8.2 — The hypothesis provenance gate.**

![A top-to-bottom decision flowchart. A model-generated hypothesis flows into a tagged exploratory record, then to a vermillion diamond asking whether it has been tested by a pre-specified procedure. The no exit returns it to a grey terminus reading remains exploratory, not a finding, marked as where hypothesis laundering is blocked. The yes exit passes through a scientist-owns-the-claim step to a green terminus reading enters result or manuscript.](../figures/figure-8-2.svg)

*Figure 8.2 — The provenance gate that separates conjecture from evidence. A generated hypothesis is tagged exploratory and can only become part of a result once a human has tested it by a procedure fixed in advance and taken responsibility for the claim; the alternative path keeps it visibly a conjecture. (Rendered as `figures/figure-8-2.svg` from the brief below, per `FIGURES.md`.)*

```
FIGURE BRIEF
- id:            Figure 8.2
- title:         Where a generated hypothesis may and may not go
- type:          decision flowchart
- claim:         A model-generated hypothesis is exploratory by default and may enter a result only after a human tests it by a pre-specified procedure and owns the claim; without that step it stays compartmented.
- canvas:        16:9
- elements:      a top orange rounded-square "model-generated hypothesis"; flowing down to a
                 sky-blue cylinder compartment "exploratory record (tagged)"; a vermillion
                 diamond gate "tested by pre-specified procedure?"; a blue human head-and-shoulders
                 icon "scientist owns the claim"; a green "enters result / manuscript" terminus;
                 a grey "remains exploratory — not a finding" terminus
- flow:          top-to-bottom — hypothesis → exploratory record → gate "tested by pre-specified
                 procedure?"; "no" exit returns to the grey "remains exploratory" terminus;
                 "yes" exit passes through the blue "scientist owns the claim" icon to the green
                 "enters result / manuscript" terminus
- labels:        "model-generated hypothesis", "exploratory record (tagged)", "tested by
                 pre-specified procedure?", "yes", "no", "scientist owns the claim",
                 "enters result / manuscript", "remains exploratory — not a finding"
- annotations:   a vermillion callout on the "no" path reading "hypothesis laundering blocked here"
- caption:       Figure 8.2 — The provenance gate that separates conjecture from evidence. A generated hypothesis is tagged exploratory and can only become part of a result once a human has tested it by a procedure fixed in advance and taken responsibility for the claim; the alternative path keeps it visibly a conjecture.
- alt-text:      A top-to-bottom decision flowchart. A model-generated hypothesis flows into a tagged exploratory record, then to a vermillion diamond asking whether it has been tested by a pre-specified procedure. The no exit returns it to a grey terminus reading remains exploratory, not a finding, marked as where hypothesis laundering is blocked. The yes exit passes through a scientist-owns-the-claim step to a green terminus reading enters result or manuscript.
- generator prompt: A flat vector decision flowchart on an off-white background, flowing top to
                 bottom. At the top, an orange rounded square labelled "model-generated hypothesis"
                 connects down to a sky-blue cylinder labelled "exploratory record (tagged)", which
                 connects to a vermillion diamond labelled "tested by pre-specified procedure?". The
                 diamond has two exits: a "no" arrow to a grey terminus box labelled "remains
                 exploratory — not a finding", with a small vermillion callout "hypothesis
                 laundering blocked here"; and a "yes" arrow passing through a blue
                 head-and-shoulders icon labelled "scientist owns the claim" to a green terminus box
                 labelled "enters result / manuscript". Single-weight connectors, one arrowhead
                 style, generous spacing, minimal text.
```

## 8.5 Worked design: a three-track intercomparison

The worked example in this chapter is a **design**, not an executed study.
It specifies how an orchestration agent would run a structured comparison of three modelling approaches on a common problem, and it deliberately reports no results, because none have been produced.

The scientific question is one of the more consequential in contemporary environmental modelling: how do a physics-based model, a data-driven model and a hybrid of the two compare on the same task, domain and period?
The design exists to make that comparison fair, reproducible and fully documented, not to pre-judge its outcome.
The three tracks are not hypothetical.
Each now has a peer-reviewed exemplar in the weather and climate literature, from physics-based operational forecasting, through data-driven global models that reached operational-grade skill around 2022–23 (Lam et al., 2023; Bi et al., 2023), to differentiable hybrids coupling a physical core with learned components (Kochkov et al., 2024).
All three are held to a common protocol: a physics-based track running a process model of the target system, a data-driven track training a machine-learning model on the same inputs and target, and a hybrid track where a data-driven component corrects or augments the physics-based one.
They share one training or calibration period, one evaluation period, one set of forcing inputs and one metric suite, so the only intended difference between them is the modelling approach itself.
As of 2026 that structure is no longer only this book's proposal: a World Meteorological Organization-coordinated project, with roughly sixty-five authors across six continents, is running exactly this machine-learning, physically based and hybrid intercomparison at institutional scale, building a centralised database of forecasts from all three model classes under both institution-specific and standardised initial conditions, for distributed and comparable verification (McTaggart-Cowan et al., 2026).
It is cited here only for its existence and its design.
The project is still collecting data and has published no skill comparison, so there is nothing to report from it yet, and its existence does not change the status of this chapter's example, which remains a worked design awaiting execution.

**[AUTHOR: specify the system, domain, periods, forcing datasets and exact model configurations for each track — these are scientific decisions the author must make; the agent must not invent them.]**
The agent's role is identical across all three tracks and confined to orchestration.
It expands each track's declared configuration into concrete runs, submits them, tracks their state, captures the full provenance of every run, and flags anomalies for you to adjudicate: a run that failed, an output outside physical bounds, a data-driven training run whose validation loss diverged.

Two elements of the design carry most of its integrity, and both are worth stating explicitly.
The evaluation is separated from the agent entirely: skill is scored by the independent evaluation apparatus of Chapter 11 against a held-out period the agent has no hand in choosing, so the system running the experiments has no influence over how they are judged.
And the comparison is guarded against the failure data-driven and hybrid tracks are most prone to, which is apparent skill that is really memorisation of the evaluation period.
The guard is a protocol fixed before any run is launched, in which the evaluation period stays untouched during training and the metric suite is agreed in advance.
Figures 8.3 and 8.4 set the design out: the first contrasts the conventional hand-run campaign with the agent-orchestrated one, and the second traces the orchestration of the three tracks from design to recorded, independently evaluated result.
Presented this way, the example is honest about what it is, a worked design awaiting execution of the kind Chapter 15 carries through end to end.
It is here because the design decisions are where the scientific integrity of an intercomparison is won or lost, well before any number gets produced.

**Figure 8.3 — Conventional campaign versus agent-orchestrated campaign.**

![A two-panel before/after diagram. The top panel shows a scientist manually maintaining a spreadsheet log beside loose scripts and an outputs cylinder, with a broken link marked drift between the runs and the log. The bottom panel shows the same scientist authoring an experimental design into an orange orchestration agent that submits to a scheduler and writes to a provenance store by a solid link marked captured at run time, with an anomaly flag returning to the scientist.](../figures/figure-8-3.svg)

*Figure 8.3 — The same campaign run two ways. Above, a hand-maintained log drifts from the runs it describes; below, the orchestration agent captures provenance as each run launches. The scientist's decisions are unchanged; only the bookkeeping moves. (Rendered as `figures/figure-8-3.svg` from the brief below, per `FIGURES.md`.)*

```
FIGURE BRIEF
- id:            Figure 8.3
- title:         From hand-run campaign to orchestrated campaign
- type:          before/after
- claim:         The agentic redesign changes who keeps the record, not who makes the decisions: provenance is captured as a by-product of running, while every scientific choice stays with the scientist in both panels.
- canvas:        16:9
- elements:      two stacked panels sharing a grammar. Top panel "conventional": a blue
                 scientist icon linked by hand to a grey spreadsheet glyph "manual log",
                 loose green script glyphs "edit config · submit · check queue", a sky-blue
                 cylinder "outputs" with a grey dashed broken link to the manual log labelled
                 "drift". Bottom panel "orchestrated": the same blue scientist authoring a blue
                 "experimental design" tag into an orange "orchestration agent"; the agent
                 linked to a green "scheduler" glyph and a solid link to a sky-blue cylinder
                 "provenance store" labelled "captured at run time"; a vermillion diamond
                 "anomaly flag" returning to the scientist
- flow:          top panel left-to-right with a broken link between runs and the manual log;
                 bottom panel left-to-right with an unbroken link between runs and the
                 provenance store; the scientist icon occupies the same left position in both
- labels:        "conventional", "orchestrated", "scientist", "manual log",
                 "edit config · submit · check queue", "outputs", "drift", "experimental
                 design", "orchestration agent", "scheduler", "provenance store",
                 "captured at run time", "anomaly flag"
- annotations:   a small vermillion callout on the top panel's broken link reading "record
                 reconstructed after the fact"; a small callout on the bottom panel reading
                 "record captured as it runs"
- caption:       Figure 8.3 — The same campaign run two ways. Above, a hand-maintained log drifts from the runs it describes; below, the orchestration agent captures provenance as each run launches. The scientist's decisions are unchanged; only the bookkeeping moves.
- alt-text:      A two-panel before/after diagram. The top panel shows a scientist manually maintaining a spreadsheet log beside loose scripts and an outputs cylinder, with a broken link marked drift between the runs and the log. The bottom panel shows the same scientist authoring an experimental design into an orange orchestration agent that submits to a scheduler and writes to a provenance store by a solid link marked captured at run time, with an anomaly flag returning to the scientist.
- generator prompt: A flat vector before/after diagram on an off-white background, two stacked
                 panels sharing one visual grammar. Top panel labelled "conventional": a blue
                 head-and-shoulders icon "scientist" links by hand to a grey spreadsheet glyph
                 "manual log" and to loose green script glyphs "edit config · submit · check
                 queue" and a sky-blue cylinder "outputs"; a grey dashed broken line between the
                 outputs and the manual log is labelled "drift", with a small vermillion callout
                 "record reconstructed after the fact". Bottom panel labelled "orchestrated": the
                 same blue "scientist" authors a blue tag "experimental design" into an
                 orange-bordered rounded rectangle "orchestration agent", which links to a green
                 glyph "scheduler" and by a solid line to a sky-blue cylinder "provenance store"
                 labelled "captured at run time"; a vermillion diamond "anomaly flag" returns to
                 the scientist, with a small callout "record captured as it runs". Single-weight
                 connectors, one arrowhead style, aligned panels, generous spacing, minimal text.
```

**Figure 8.4 — Orchestrating the three-track intercomparison.**

![A top-to-bottom sequence diagram with four actor lanes (scientist, orchestration agent, HPC scheduler and provenance store) and a separated vermillion evaluation lane on the right. Numbered steps show the scientist authoring a protocol and three track configurations, the agent expanding physics, data-driven and hybrid configs into runs, submitting them, receiving states, recording provenance and flagging anomalies, then completed outputs passing to independent held-out evaluation whose scores return to the scientist. A bracket marks the agent's steps as orchestration only, with no scoring.](../figures/figure-8-4.svg)

*Figure 8.4 — The worked design as a sequence. A single agent expands, submits, tracks and records three tracks under one protocol; scoring is done separately against a held-out period, so the system that runs the experiments does not judge them. No results are shown: this is a design. (Rendered as `figures/figure-8-4.svg` from the brief below, per `FIGURES.md`.)*

```
FIGURE BRIEF
- id:            Figure 8.4
- title:         The three-track intercomparison as an orchestrated sequence
- type:          sequence
- claim:         One agent orchestrates three tracks under a common protocol, recording provenance for each, while evaluation is performed independently against a held-out period the agent never touches.
- canvas:        16:9
- elements:      four vertical actor lanes read left-to-right at the top as headers —
                 blue "scientist", orange "orchestration agent", green "HPC scheduler",
                 sky-blue "provenance store" — plus a fifth vermillion header "independent
                 evaluation (Ch. 11)" set apart to the right; numbered steps flow top-to-bottom
- flow:          top-to-bottom numbered steps: 1 scientist authors common protocol and three
                 track configs; 2 agent expands physics / data-driven / hybrid configs into
                 runs; 3 agent submits runs to scheduler; 4 scheduler returns run states;
                 5 agent records each run's provenance; 6 agent flags anomalies to scientist;
                 7 completed outputs pass to independent evaluation on a held-out period;
                 8 scores return to the scientist. The evaluation lane is visually separated to
                 show the agent has no hand in it
- labels:        "scientist", "orchestration agent", "HPC scheduler", "provenance store",
                 "independent evaluation (Ch. 11)", "1 author protocol + 3 track configs",
                 "2 expand: physics · data-driven · hybrid", "3 submit runs", "4 run states",
                 "5 record provenance", "6 flag anomalies", "7 held-out evaluation",
                 "8 scores to scientist"
- annotations:   a light bracket around steps 2–6 labelled "orchestration only — no scoring
                 here"; the evaluation lane tinted apart in vermillion to stress independence
- caption:       Figure 8.4 — The worked design as a sequence. A single agent expands, submits, tracks and records three tracks under one protocol; scoring is done separately against a held-out period, so the system that runs the experiments does not judge them. No results are shown: this is a design.
- alt-text:      A top-to-bottom sequence diagram with four actor lanes (scientist, orchestration agent, HPC scheduler and provenance store) and a separated vermillion evaluation lane on the right. Numbered steps show the scientist authoring a protocol and three track configurations, the agent expanding physics, data-driven and hybrid configs into runs, submitting them, receiving states, recording provenance and flagging anomalies, then completed outputs passing to independent held-out evaluation whose scores return to the scientist. A bracket marks the agent's steps as orchestration only, with no scoring.
- generator prompt: A flat vector sequence diagram on an off-white background. Four vertical lanes
                 with top headers, left to right: a blue head-and-shoulders "scientist", an
                 orange rounded-square "orchestration agent", a green cluster glyph "HPC
                 scheduler", a sky-blue cylinder "provenance store"; set apart to the right, a
                 fifth vermillion header "independent evaluation (Ch. 11)". Numbered horizontal
                 message arrows flow top to bottom: "1 author protocol + 3 track configs" from
                 scientist to agent; "2 expand: physics · data-driven · hybrid" within the agent
                 lane; "3 submit runs" agent to scheduler; "4 run states" scheduler to agent;
                 "5 record provenance" agent to provenance store; "6 flag anomalies" agent to
                 scientist; "7 held-out evaluation" from agent outputs to the vermillion
                 evaluation lane; "8 scores to scientist" evaluation to scientist. A thin bracket
                 spans steps 2 to 6 labelled "orchestration only — no scoring here". Single-weight
                 connectors, one arrowhead style, generous spacing, minimal text.
```

## 8.6 Failure modes

Orchestrated experimentation does not fail at the scheduling, which either works or visibly does not.
It fails where results meet interpretation, and three failures recur often enough to name.

The first is **confident extrapolation**.
A model asked to predict beyond the range of the data that constrained it does so with the same fluency it brings to an interpolation, and that fluency tells you nothing about whether the answer is right.
The general anatomy belongs to the failure gallery (Chapter 13); what matters here is the campaign-specific guard.
A data-driven track trained on a historical period will extrapolate into conditions outside that period, and its skill there is unknown rather than good, however smooth its output looks.
Even the strongest hybrid climate models in the literature carry their authors' explicit warning that they do not extrapolate reliably to substantially different conditions (Kochkov et al., 2024).
So the protocol reports the range of the training data and scores out-of-range performance separately, and extrapolation gets labelled rather than absorbed into a headline metric (high confidence).

The second is **over-fitting dressed as skill**, where a model scores well on an evaluation period because it has, in effect, already seen it: leakage between training and evaluation data, a hyperparameter search tuned against the evaluation set, or a hybrid configuration that memorised that period's residuals.
The output is genuine skill on the evaluation set and an illusion about generalisation, and because the number is real it is peculiarly persuasive.
The guard is the protocol of §8.5, meaning a held-out period fixed before any run, untouched during training and evaluated once, enforced by keeping the agent away from the scoring and treated fully in Chapter 11.

The third and most insidious is **hypothesis laundering**, where a hypothesis generated by a language model, as in §8.4, gets reported as a finding because it arrived alongside real results and sounded like one.
The mechanism is social and procedural rather than technical.
A conjecture crosses from the exploratory compartment into the evidential chain without anyone testing it, and the fluency of its expression makes the crossing easy.
The guard is the one built into §8.4: generated hypotheses are tagged, kept in their own compartment of the provenance record, and cannot enter a result until a human has tested them by a pre-specified procedure and owned the claim.

All three are plausible rather than obvious, in the sense of Chapter 1.
None announces itself, all imitate competence, and all are caught by procedure rather than by inspection.
That is why the checklist below is a design artefact and not an afterthought.

## 8.7 Verification checklist

This checklist is deliberately procedural, because the failures of §8.6 are caught by fixing the procedure before the runs rather than by scrutinising outputs afterwards.
Settle it at design time, record it with the campaign, and a colleague who did not run the campaign can confirm every item from the record.

- **The design is authored and frozen before any run.** The experimental design (parameters, ranges, metric suite and evaluation period) is written by the scientist and recorded before the first run is launched, so the agent expands a fixed design rather than an evolving one.
- **The evaluation period is held out and independently scored.** It is untouched during any training or calibration, and scoring is performed by machinery independent of the agent that ran the experiments (Chapter 11).
- **Extrapolation is labelled, not absorbed.** Out-of-range predictions are identified against the range of the training or calibration data and scored separately, so extrapolation is never folded into a single headline number.
- **Provenance is captured at run time.** Every run's configuration, software version, forcing-dataset identifier, random seed and completion status is recorded as the run launches, not reconstructed afterwards (Chapter 12).
- **Generated hypotheses stay compartmented.** Any model-generated hypothesis is tagged exploratory, kept separate in the record, and admitted to a result only after a human has tested it by a pre-specified procedure and taken responsibility for the claim.
- **No run is silently dropped.** Anomalies the agent flags (failed runs, outputs outside physical bounds, diverged training losses) are adjudicated by the scientist and the adjudication recorded.
- **The boundary holds in practice.** No scientific decision (which design, which metric, which result to believe, which hypothesis to pursue) is delegated to the agent, and a review of the campaign can confirm this from the log of the agent's tool calls (Figure 8.1).

This is a starting point to adapt to your own models and computing environment, not a universal standard.
Its printable form lives in the repository alongside the pattern.

## 8.8 Repository pointer

The companion repository holds the runnable and perishable counterparts to this chapter.
A minimal orchestration example under `/patterns` implements the boundary of Figure 8.1: an agent that expands a small declared design, submits placeholder runs, records provenance and flags anomalies, with the scientific decisions left explicitly to you.
It names current tools there rather than in this print text, per the vendor-neutral convention.
The three-track intercomparison of §8.5 is carried as a sanitised design under `/case-studies`, with its [AUTHOR]-marked configuration choices still to be supplied and its status as a worked design, not an executed study, stated in place.
It is the design Chapter 15 takes through end to end once it has been executed.
The verification checklist of §8.7 is held in printable form under `/checklists`, and the prompts used to elicit exploratory hypotheses under the safeguards of §8.4, kept separate from the evidential workflow by construction, live under `/prompts`.
**[AUTHOR: confirm the final repository paths and contents.]**
The repository is where the tools and figures that date faster than the patterns are kept current, exactly as Chapter 17 argues.

---

### References (verify details before release)

- Bi, K., Xie, L., Zhang, H., Chen, X., Gu, X. and Tian, Q. (2023). Accurate medium-range global weather forecasting with 3D neural networks. *Nature*, 619, 533–538. https://doi.org/10.1038/s41586-023-06185-3
- Boiko, D. A., MacKnight, R., Kline, B. and Gomes, G. (2023). Autonomous chemical research with large language models. *Nature*, 624, 570–578. https://doi.org/10.1038/s41586-023-06792-0
- Kochkov, D., Yuval, J., Langmore, I., et al. (2024). Neural general circulation models for weather and climate. *Nature*, 632, 1060–1066. https://doi.org/10.1038/s41586-024-07744-y
- Lam, R., et al. (2023). Learning skillful medium-range global weather forecasting. *Science*, 382(6677), 1416–1421. https://doi.org/10.1126/science.adi2336
- Lopez-Gomez, I., Brenner, M. P. and Schneider, T. (2026). Probabilistic seasonal streamflow forecasting across California's Sierra Nevada watersheds with agentic AI. *arXiv preprint*. https://arxiv.org/abs/2605.16178
- McTaggart-Cowan, R., Magnusson, L., Polichtchouk, I., Ackerley, D., Koehler, M., Casati, B., et al. (2026). WP-MIP: an artificial intelligence, hybrid, and physically based model intercomparison project for weather prediction. *arXiv preprint*. https://arxiv.org/abs/2604.16643
- Yan, S., Chen, M., Li, Z., et al. (2026). AI agent for hydrologic modeling: definition, development and application. *ESS Open Archive preprint*. DOI: 10.22541/essoar.176894821.13120988/v1 [verify — primary page unfetched this sweep; abstract and figures not confirmed against the paper]
- Zhu, et al. (2026). Large language models as calibration agents in hydrological modeling: feasibility and limitations. *Geophysical Research Letters* [verify author list and details]. https://doi.org/10.1029/2025GL120043
