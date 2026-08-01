# Chapter 15 — Governing a modelling workflow end to end

> **Status:** draft r6 · voice v5.0 (`STYLE.md` §1) · sentence-per-line per `STYLE.md` §10 · figures as briefs per `FIGURES.md`.
> **Conventions:** vendor-neutral (outline §9) · **[AUTHOR: …]** marks lived material only the author can supply · **[verify]** marks real but unconfirmed details · citations drawn only from verified reports in `/research`. Nothing has been invented.
> This chapter reports an executed end-to-end case study; the modelling problem, the roster used, the gates applied, the review findings and the publication outcome are the author's lived material and are tagged **[AUTHOR: …]**.

---

## 15.1 The apparatus applied once

This chapter does something the previous fourteen could not: show the book's apparatus working as one piece rather than catalogued part by part.

Each earlier chapter isolated a single instrument and examined it on its own so its logic was legible: the specification schema of Chapter 3, the roster derivation of Chapter 10, the registries and gates of Chapter 12, the evidential hierarchy of Chapter 11, the manuscript pipeline of Chapter 9.
That isolation is a teaching convenience and, past a point, an operational fiction.
The instruments only earn their cost when they connect: the audited output of each stage is the admissible input to the next, and a gap between two stages is exactly where governance fails without anyone noticing.
The workflow followed here is real and was executed end to end **[AUTHOR: name the modelling problem — the physical quantity modelled, the spatial domain and period, the scientific question the study set out to answer, and the publication it produced]**, and this chapter deliberately structures the account as a walk through its stages.
At each stage the account states four things in the same order: what was specified, which agent role acted, which gate applied, and, the question that matters most throughout, what the human decided.
The claim this chapter exists to demonstrate is that human authority in a governed agentic workflow is not concentrated at the end in a final sign-off.
It is spread across every gate, and that spread is what makes the workflow a scientific instrument rather than an automation (high confidence, on the composition argument developed below).
The honest limitation to concede at the outset is that one executed workflow is an existence proof, not a controlled comparison: it shows that the apparatus composes and what it costs to run, not that it outperforms a less governed alternative on the same problem, a claim that would need the paired evaluation of Chapter 11, which this case study does not attempt.

This is not an alien discipline imported into environmental science; it is close to how the field already absorbs powerful new methods.
When an operational forecasting centre took a data-driven weather model into production in early 2025, it did so by running the new model in parallel with its physics-based system, verifying it in operational-like conditions, and operationalising it in stages rather than all at once (Lang et al., 2024).
Governance came first and capability second, which is the same order this chapter follows below, and a reassuring precedent, because the institutions that adopt AI this way are precisely the conservative, verification-obsessed ones this book is written for.
The discipline now reaches agent-designed systems too: a 2026 preprint benchmarked an agent-designed seasonal streamflow forecaster against the responsible government agency's operational forecasts across several years before making any claim of skill (Lopez-Gomez et al., 2026), the same prove-before-claim protocol this chapter's publication run demands.

The governed lifecycle has five stages, and Figure 15.1 sets them out as one architecture before the sections take each in turn.
A specification written to the seven-field schema of Chapter 3.
A roster of agent roles derived from that specification by the procedure of Chapter 10.
A set of gates and registries from Chapter 12 that every unit of work has to pass.
An independent review by an actor with no stake in the work reviewed.
And a publication run, governed as Chapter 9 requires, where the provenance accumulated upstream feeds the disclosure statement and no agent stands as an author.
The diagram draws them left to right for legibility, but the lifecycle is not a pipeline that runs cleanly once.
Every gate has a failure exit returning work to the role that produced it, and a registry entry made late can invalidate a stage already passed.
What the diagram fixes is not a sequence guaranteed to run forward.
It is the set of points where a named human decision is required before the work may proceed, and those points, rather than the boxes between them, are the governance.

**Figure 15.1 — The governed modelling lifecycle, end to end.**

![A left-to-right spine of five stages: a specification written to the seven-field schema; an agent roster derived from it; gates and registries, with an assumption registry and an uncertainty registry beside the gate; independent review; and the publication run producing the manuscript, figures and disclosure. Each gate has a pass arrow forward and a fail arrow returning to the previous stage. A single author-decision icon above the spine connects down to every gate, under a bracket reading human authority at every gate, not only at the end. An audit trail runs beneath all five stages, annotated as accumulating from the first stage, so the disclosure at the end is assembled rather than reconstructed.](../figures/figure-15-1.svg)

*Figure 15.1 — The whole book in one workflow. Specification, roster, gates and registries, independent review, publication: each stage's audited output is the next stage's admissible input. The author connects to every gate rather than appearing once at the end. The audit trail underneath is why the disclosure statement at publication is assembled from a record instead of reconstructed under deadline. (Rendered as `figures/figure-15-1.svg` from its brief in `fig-brief/ch15-governing-a-modelling-workflow-end-to-end.md`, per `FIGURES.md`.)*

## 15.2 The specification the workflow was held to (Chapter 3)

The workflow began, as every governed workflow in this book begins, with a written specification rather than a conversation.
That specification was the artefact everything downstream was held to.
Following Chapter 3, the modelling task was first decomposed into units small enough that each had a single checkable outcome, and each unit was then written to the seven-field schema (objective, inputs, acceptance criteria, stop conditions, assumptions and conventions, provenance requirement, and named reviewer) **[AUTHOR: list the units the modelling task decomposed into — for example data acquisition and QC, calibration, the model runs themselves, evaluation, and figure generation — and state how many units the full specification contained]**.
Two of the seven fields carry disproportionate weight in a modelling context, and this workflow bore that out.
The assumptions-and-conventions field is where a modelling study silently goes wrong: units of measurement, coordinate reference systems, calendar and time-zone conventions, missing-value codes, and the treatment of the model's vertical or ensemble structure are exactly the details one stage assumes and another contradicts, and writing them down once, in the specification, is what lets the later gates of Chapter 12 catch a violation rather than propagate it.
The provenance-requirement field is where the disclosure statement of the eventual publication is earned, because a unit told in advance to record its inputs, their versions, the decisions it took and the values it rejected produces an audit trail as a by-product of execution rather than as something reconstructed under deadline.
The specification was placed under version control and reviewed before any agent executed against it, which is the practice Chapter 3 argues moves scepticism to where it earns the highest return: a change to the specification was treated as a change to the method, requiring the same care and leaving the same record, so that the question an auditor would later ask, what was this workflow trying to do and who decided, is answered by an artefact and not by memory (high confidence in the practice; its adequacy on this workflow remains for the author to confirm).

## 15.3 Deriving the roster, not choosing it (Chapter 10)

The agent roster was derived from the specification rather than assembled by preference.
That is the discipline Chapter 10 sets against the temptation to add agents because more of them feels more capable.
The derivation is mechanical in its first pass and a matter of judgement in its second: reading each unit's objective and its named-reviewer field yields a candidate actor for the work and a distinct actor for its check, and the roster is the deduplicated set of those actors with their tool access and their boundaries fixed **[AUTHOR: state the roster the derivation produced — the agent roles and how many, the human roles, and which units each role owned]**.
The decisive constraint Chapter 10 imposes, and the one this workflow was built to honour, is that multiple agents add robustness only where their independence is real: a unit whose reviewer field names the same agent that produced the work has a check in name only, because a model is a poor judge of its own correctness, so the derivation was allowed to collapse producing roles together but never to collapse a producing role into its own reviewer.
Independence was therefore designed in at the roster stage rather than hoped for at the review stage.
The roster was also where the least-privilege posture of Chapter 12 was set, granting each role the narrowest tool access its units required and no more, so a compromised or misdirected agent could damage only within its remit (Chapter 12).
The measured claim is that a roster derived this way is auditable in a way a roster chosen by preference is not, because every role on it traces back to the specification unit that required it, and any role that cannot be so traced is either an error or an admission that the specification is incomplete (moderate-to-high confidence; the traceability holds by construction, its completeness on this workflow remains for the author to confirm).

## 15.4 Gates and registries (Chapter 12)

Every unit's acceptance criteria became a gate.
The two registries of Chapter 12 accumulated across the run as the workflow's growing memory of what it had assumed and what it did not know.
A gate in this workflow is the operational form of an acceptance criterion: a unit's output is not admitted to the next stage until a named party (the reviewer field made concrete) has confirmed the criterion holds, and a gate that fails returns the work to the producing role with the failure recorded rather than discarded.
The assumption registry and the uncertainty registry are the two ledgers that make the gates cumulative rather than local.
The assumption registry records every convention and default the workflow committed to (each entry naming the assumption, the unit that introduced it, and the party who authorised it) so a later stage can be checked against it and a violated assumption becomes a gate failure with a traceable cause rather than an anomaly with none **[AUTHOR: give two or three real entries from the assumption registry for this workflow, and note any case where a downstream gate caught a violation of an upstream assumption]**.
The uncertainty registry records what the workflow does not know with confidence (the estimated uncertainty on each input, the propagation choices made, and the residual uncertainty carried into the results), and it is this ledger, more than any single score, that the evaluation of Chapter 11 draws on and that the eventual manuscript reports rather than suppresses.
The audit trail beneath both registries, in Figure 15.1, is not a third artefact.
It is the specification, the gate outcomes and the two registries together, timestamped and attributable, and it is what the publication run of §15.7 builds its disclosure from.
The limitation to state plainly is that registries govern only what is entered into them: an assumption never written down is ungoverned however diligent the gates, which is why the assumptions-and-conventions field of §15.2 is the registry's true origin and why an empty registry is a warning sign rather than a clean bill of health (high confidence).

## 15.5 One gated stage, step by step

One stage examined in full detail shows how the pieces of the preceding three sections act together in time.
Figure 15.2 traces a representative gated stage from specification unit to the human decision at the gate.
The stage chosen for this walk is **[AUTHOR: name the representative stage — for example the calibration stage, or the observational quality-control stage — and state its objective in one line]**, and it is representative precisely because nothing about it is exceptional: it is one unit among several, governed by the same schema and the same gate discipline as the rest.
The sequence runs as follows.
The producing agent reads the unit's specification (objective, named inputs, acceptance criteria, stop conditions) and executes against it, calling tools rather than reasoning in prose wherever a calculation or a data operation is involved, so that the model's weaknesses are delegated to instruments that do not share them.
The agent writes its output together with the provenance the unit required, and appends any new assumption it was forced to make to the assumption registry rather than leaving it implicit.
The gate then applies: the acceptance criteria are checked mechanically where they are mechanical, and the independent reviewer of §15.6 applies those that require judgement.
A pass advances the output to the next unit; a failure returns it to the producing agent with the reason recorded, and the loop repeats within the budget the stop conditions set, halting and handing back to the human if that budget is exhausted.
The human decision sits at the gate, not after it: the human is the party who accepts a passed stage into the workflow's record or overrides a gate outcome with a reasoned entry of their own **[AUTHOR: describe one real decision you took at this gate — an acceptance, an override, or a return — and what the output and provenance were that you decided on]**.
The point the stage makes concrete is that the human is not reviewing a finished workflow at the end but authorising it one gate at a time, and that the cost of this, a decision per gate rather than a decision per project, is the price of an instrument whose every step is attributable (high confidence in the pattern; the per-stage effort on this workflow remains for the author to report).

**Figure 15.2 — A single gated stage, in sequence.**

![A sequence with five lanes: a specification unit, an agent, tools and data, a gate with its reviewer, and the author. Six numbered steps: the unit hands the agent its objective, inputs, criteria and stop conditions; the agent calls tools rather than reasoning in prose; it writes output and provenance and logs any new assumption to the registry rather than leaving it implicit; it submits for the check; a fail returns it within the budget the stop conditions set, and a pass goes forward; the author accepts, overrides or returns, with a vermillion note that the decision happens at the gate, not after the workflow has finished. A footer reads one decision per gate is the price of a workflow whose every step is attributable.](../figures/figure-15-2.svg)

*Figure 15.2 — One stage at full resolution, and nothing about it is exceptional. The agent executes against a written unit, delegates its arithmetic to tools, writes its own provenance, and appends any assumption it was forced to make to the registry. The gate applies before anything advances, and the author's decision happens there, not in a review at the end. The price is one decision per gate; what it buys is a workflow whose every step is attributable. (Rendered as `figures/figure-15-2.svg` from its brief in `fig-brief/ch15-governing-a-modelling-workflow-end-to-end.md`, per `FIGURES.md`.)*

## 15.6 Independent review (Chapters 10 and 12)

Independent review was a distinct actor with no stake in the work it reviewed.
Treating it that way is the difference between a check and a formality.
Chapter 10 introduced the independent reviewer as a role on the roster; Chapter 12 required a reviewer-coverage record showing which units were reviewed, by whom, and against which criteria; this workflow combined the two so that no unit reached the human decision at a gate without a review attributable to a party other than the unit's producer **[AUTHOR: state who or what performed independent review at each gate — a reviewer agent, a second scientist, or both — and give two or three substantive findings the review surfaced, including any that returned work upstream]**.
The hazard the independence is designed against is the over-agreeable review anatomised in Chapter 13, where a reviewer that shares the producer's context ratifies the work rather than testing it.
This workflow mitigated it in two ways that Chapter 12 recommends.
First, the reviewer was given the specification and the acceptance criteria but not the producing agent's reasoning trace, so the review tested the output against the standard rather than against the producer's justification for it.
Second, reviewer coverage was recorded as a first-class artefact, so an unreviewed unit was visible as a gap rather than hidden as an omission.
This is the same discipline the field already applies to its models: when meteorologists assessed a vendor-published weather model, they did not take its self-reported scores on trust but re-verified it on their own analyses, under operational-like conditions, with their own metrics before trusting it (Ben Bouallègue et al., 2024).
This is independent re-verification on one's own ground, which is exactly what a reviewer role does for a unit of agent work.
The claim to make carefully is that independent review raises the evidential tier of a workflow's outputs in the sense of Chapter 11 (moving a result from asserted-correct to checked-by-an-independent-party) without ever reaching the top of that hierarchy, because agent review is a lower tier of evidence than expert human scrutiny and does not displace it (moderate confidence; the strength of the independence obtained on this workflow remains for the author to characterise, and the reviewer-coverage record is the evidence that would support or qualify the claim).

## 15.7 The publication run (Chapter 9)

The publication run assembled the manuscript from the pipeline's audited artefacts rather than composing claims afresh, which is the discipline Chapter 9 sets for the output side of scholarship.
Figures and tables were generated from the same provenance-bearing artefacts the gates had passed, so a number in the text traces to a computation in the record rather than to a recollection, and the results the manuscript reported carried the uncertainty the registry of §15.4 had accumulated rather than a cleaner story than the workflow could support **[AUTHOR: state the publication outcome — the venue, the form of the submission, the reviewers' response to the governed methodology if it was raised, and any revision the review required]**.
The disclosure statement was drawn directly from the audit trail: the roster of agent roles, the units each acted on, the tool access each held and the review coverage obtained were reported as method rather than confessed as an afterthought, and no agent was named as an author.
That last point is not a preference but settled policy: journals established early that an AI tool cannot be listed as an author, because authorship carries an accountability a tool cannot bear, and that researchers must instead document how such tools were used (Nature editorial, 2023).
This is the same category distinction this book has held since Chapter 1, that authorship and accountability are errors of category to assign to an instrument.
Funder guidance now says the same from the other direction: the researcher remains responsible for all scientific output, must verify AI-generated results, and should disclose substantial AI use (European Commission, 2024).
Journal and funder policy on AI use is a volatile landscape, and this workflow treated it as Chapter 9 prescribes (surveyed by policy class in the manuscript, with the specific current requirements kept in the companion repository) because by 2026 the requirement to disclose substantive AI assistance had become common but not uniform across venues **[verify: characterise the disclosure-policy landscape at submission, and the specific venue's requirement, in the repository]**.
The implication worth stating is that a governed workflow makes disclosure cheap and honest, because the material a disclosure statement needs already exists as the audit trail, whereas an ungoverned workflow must reconstruct under deadline a history it did not keep, and reconstruction under deadline is where over-claiming and style laundering enter (high confidence in the mechanism; the reception of this particular disclosure remains for the author to report).

## 15.8 Where authority sat, and what it cost

The lesson of the walk is that human authority was spread across the workflow rather than concentrated at its end, and that spread is the governance rather than an addition to it.

At the specification stage the human decided what the work was and what would count as done.
At the roster stage the human decided which actors would act and within what bounds.
At each gate the human accepted, overrode or returned a passed output.
At the review stage the human commissioned and read an independent check.
At publication the human stood as the sole author of, and the sole party accountable for, the interpretation.
Not one of those decisions is novel.
Each is the ordinary exercise of a scientist's judgement, and that is the point.
The apparatus of this book does not introduce a new kind of authority.
It moves the familiar kind to the points in an agentic workflow where it can still be exercised meaningfully, which are the gates rather than the steps between them.
The composition demonstrated here is what the earlier chapters could only assert in isolation, and Figure 15.1 is its map.
Two limitations bound the claim honestly.
The first limitation is that the cost of this governance is real and falls mainly on the human (a decision per gate, a specification written and reviewed before execution, registries maintained and a reviewer commissioned), and this workflow shows that the cost is payable, not that it is small **[AUTHOR: report the governance overhead you observed relative to an ungoverned run of comparable work, even approximately]**.
The second limitation is that the protocol governs only what it addresses: an assumption never registered, a unit never independently reviewed, a discretion the specification left open remains ungoverned however complete the rest, so the apparatus is a discipline to be practised rather than a guarantee to be installed (high confidence).

The task the apparatus could not govern is the one that tests Chapter 4 §4.4.
Explaining a verification result to a non-specialist partner has no reference answer, no rule that decides it, and no check except another judgement.
So the agent was given no authority over anything reported (Chapter 14 §14.4, on the tutoring tier holding no write path).
That is checking cost as a property of the task, and no acceptance criterion the specification's author might have written would have changed it.
A verification score sits at the other end of the same axis, since it is recomputable by a fixed algorithm and checking it costs a rerun.
So both case studies were governable because the work was cheap to check in that sense, not because the specification declared it checkable.
A designer can write acceptance criteria for almost anything, and writing them does not make a task cheap to check.
Two workflows illustrate the thesis of §4.4 rather than test it, and this section claims no more than that (moderate confidence).

The workflow was governable end to end; whether it was well governed is a judgement the audit trail was built to let others make.

[AUTHOR: confirm that this reading is right for your two cases, and name one task in this workflow that was expensive to check and therefore never delegated — that example is worth more than the general claim.]

---

### References

Report-sourced references carry a DOI or URL and are drawn from the verified sweep in `/research`.

- Ben Bouallègue, Z., et al. (2024). The rise of data-driven weather forecasting: a first statistical assessment of machine learning-based weather forecasts in an operational-like context. *Bulletin of the American Meteorological Society*, 105(6). DOI: 10.1175/BAMS-D-23-0162.1
- European Commission, Directorate-General for Research and Innovation (2024; updated 8 May 2026). Living guidelines on the responsible use of generative AI in research (European Research Area). https://research-and-innovation.ec.europa.eu/document/download/2b6cf7e5-36ac-41cb-aab5-0d32050143dc_en **[verify the 2026 update's provisions against the updated PDF before release]**
- Lang, S., Alexe, M., Chantry, M., et al. (2024). AIFS — ECMWF's data-driven forecasting system. *arXiv preprint* **[verify journal version]**. https://arxiv.org/abs/2406.01465
- Lopez-Gomez, I., Brenner, M. P., & Schneider, T. (2026). Probabilistic seasonal streamflow forecasting across California's Sierra Nevada watersheds with agentic AI. *arXiv preprint* **[verify venue]**. https://arxiv.org/abs/2605.16178
- Nature (editorial) (2023). Tools such as ChatGPT threaten transparent science; here are our ground rules for their use. *Nature*, 613, 612. DOI: 10.1038/d41586-023-00191-1

---

*Chapter 16 turns from one governed workflow to the harder question of how a whole research group starts: a capability-based adoption plan, an honest cost model, the roles a group needs, and the institutional, ethical and energy considerations adoption brings.*
