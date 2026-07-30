# Chapter 6 — Data acquisition and quality control

> **Status:** draft r6 · voice v5.0 (`STYLE.md` §1) · sentence-per-line per `STYLE.md` §10 · figures as briefs per `FIGURES.md`.
> **Conventions:** vendor-neutral (outline §9) · **[AUTHOR: …]** marks lived material only the author can supply · **[verify]** marks real but unconfirmed details · citations drawn only from verified reports in `/research`. Nothing has been invented.
> **Chapter note:** no datasets, figures or results have been invented; worked-example specifics are marked for the author to supply.

---

## 6.1 The problem: observations arrive messy, and the mess is where errors hide

Acquiring and quality-controlling environmental observations takes a disproportionate share of a scientist's time, precisely because the work is heterogeneous, repetitive and unforgiving of small mistakes.

A single study in operational hydrology might draw on river-gauge records in a national agency's fixed-width text format, rainfall from an automatic weather-station network in one comma-separated dialect, radar-derived precipitation on a projected grid, and reanalysis fields in a self-describing binary format.
Each comes with its own timestamp convention, missing-value sentinel, unit system and update cadence **[AUTHOR: confirm the specific formats and networks you routinely reconcile, and name them in the repository rather than in print]**.
The difficulty is not that any one of them is hard to read.
It is that reconciling them into a single, physically coherent, gap-aware record takes hundreds of small judgements.
Is a flat-lined sensor frozen or genuinely static?
Is a spike a real convective burst or a telemetry glitch?
Is a gap a missing observation or a recorded zero?
Every one of those judgements, made in haste against a deadline, is a chance for an error that no later step will announce.

The errors that matter most here are the quiet ones: a millimetres-to-inches slip, a UTC-to-local shift, an accumulation silently read as a rate.
Faults like these raise no exception.
They propagate.
They get into the calibration, they bias the verification, and they surface, if at all, only when a downstream result refuses to reconcile with reality, by which time the provenance you would need to diagnose them has usually been lost **[AUTHOR: a quiet data error that cost you — the unit or timezone slip that only surfaced weeks downstream, and how you traced it back]**.
Our own literature now recognises the scale of this.
A 2025 perspective from a polar and marine research institute argues that multi-agent language-model systems could take on exactly these chronic data-management burdens, meaning heterogeneous formats, thin metadata and labour-intensive archive exploration, while conceding candidly that such systems still lack rigorous validation and continue to need a human in the loop (Pantiukhin et al., 2025).
That honest gap is where this chapter starts.
Data acquisition and quality control is the first pattern where an agent really earns its place, and it is where the governing discipline of the whole book, that authority over the data stays with deterministic rules and accountable humans, takes its sharpest operational form.

## 6.2 The conventional workflow, and where it strains

The conventional quality-control workflow is a sequence of scripts and human eyes that works well at small scale and degrades predictably as scale grows.
You write a loader for each incoming format, hand-tune a set of range checks and step-change thresholds against the physical bounds of the variable, plot the flagged series, inspect the flags, correct the loader where it misfired, and repeat until the record looks defensible **[AUTHOR: sketch your own current gauge-and-rainfall QC routine — the scripts, the manual plotting step, the reconciliation against neighbouring stations — so the redesign in §6.3 is measured against something real]**.

Three properties set the ceiling on that workflow.
The manual effort scales with the number of station-format combinations rather than with the science, so taking on a partner network can cost days of loader-writing that produce no new understanding.
The judgements are made in your head and recorded, if at all, in comments and commit messages, so the reasoning behind a particular flag, meaning why this spike was accepted and that one rejected, is rarely reconstructable six months later.
That is a provenance failure, taken up properly in Chapter 12.
And the checks themselves, being hand-maintained, tend to lag the data: a new failure appears in a sensor, produces a class of bad values, and only gets encoded as a rule after it has already contaminated a release.

The strain is not that the conventional workflow is wrong.
Its deterministic checks are exactly what should keep authority.
It is that the parts needing pattern-recognition across many heterogeneous streams, and the parts needing a written record of every judgement, are the parts a human does slowly, inconsistently and without an audit trail.
Those parts, and only those, are what an agent is positioned to take over, and the redesign that follows is deliberate about drawing that line and holding it (high confidence that the division is the right one; the precise boundary is a design choice that varies by network).

## 6.3 The agentic redesign: agents propose, QC rules dispose

The organising principle here is a strict separation of authority over the observational record.
The agent proposes flags and transformations with written justification, and deterministic quality-control rules dispose of every proposal, so no observation is ever silently overwritten by a language model.
That arrangement has a general form and a name, and Chapter 2 §2.6 gives both.
What follows is the quality-control instance of it, worked through in the detail the job needs.

This inverts the intuitive but dangerous arrangement where you hand a capable model the data and ask it to "clean" it.
Under that arrangement the model's fluency becomes a liability, because a plausible interpolation across a gap is indistinguishable, in the output, from a measured value, and the very smoothness that makes the result look finished is what hides the fabrication.
The redesign refuses the model any write access to the observational record.
What the agent may do is read the heterogeneous inputs, normalise their formats into a common representation, and generate for each suspect point a structured proposal: a flag type, the evidence for it, the neighbouring context it weighed, and a confidence, expressed as a machine-readable object rather than a changed data value.

> **Definition — Quality-control flag.** A marker attached alongside an observation that records a judgement about it (suspect, missing, corrected) without changing the measured value itself. The recorded number stays exactly as it was; the flag simply travels with it, so anyone downstream can see what was doubted and why. Flagging is deliberately not the same as editing the data.

What disposes of the proposal is a deterministic rule set: physical bounds for the variable, inter-station consistency checks, rate-of-change limits, and the network's own documented quality conventions, all of it code a human wrote, reviewed and can rerun identically.
A proposal that survives the rules is applied as a *flag*, never as a substituted value.
A proposal the rules reject is logged, with its rejection reason, and the point is left as observed.
The disposer here is a deterministic rule, which is the first of the three kinds Chapter 2 §2.6 sets out.
The tools the agent calls to do this are the ordinary function-call apparatus of Chapter 2: a format reader, a unit resolver, a neighbouring-station query, each with a narrow, declared interface, so the agent's actions are auditable calls rather than opaque cognition (high confidence in the pattern; the specific tool set depends on the data you hold).

**Figure 6.1 — Propose–dispose architecture.**

![An architecture diagram. Three raw-input cylinders, a gauge network, a rainfall network and a gridded product, feed a QC agent containing a language model, a plan-act-observe loop and three tools: a format reader, a unit resolver and a neighbour query. An arrow from the agent to a deterministic-rules diamond is labelled flag proposals, justified, and annotated that the agent has no write access to the data and may only propose. The rules diamond lists physical bounds, rate limits and inter-station checks, and is annotated as code a human wrote and can rerun identically. A scientist icon sits above it, annotated as holding the authority the rules exercise. Two exits, apply flag and reject, lead to a flagged-record store and a rejection log, annotated respectively that the measured value is never overwritten and that a rejected proposal is kept with its reason. Both write to a provenance store annotated as keyed to the input files and the rule-set version.](../figures/figure-6-1.svg)

*Figure 6.1 — Who is allowed to change the data, and who is not. The agent reads, normalises and proposes, with justification; deterministic rules dispose of every proposal, under a scientist's authority. An observation is flagged, never silently overwritten, and both the flags and the rejections are written to provenance keyed to the inputs and the rule-set version. (Rendered as `figures/figure-6-1.svg` from the brief below, per `FIGURES.md`.)*

```
FIGURE BRIEF
- id:            Figure 6.1
- title:         Agents propose, QC rules dispose
- type:          architecture
- claim:         The agent may read, normalise and propose, but only deterministic rules may dispose; the observational record is never written by the model.
- standfirst:    The model never writes to the data. It only ever asks.
- canvas:        16:9
- elements:      left, three stacked "raw inputs" cylinders in sky blue (gauge, rainfall, grid);
                 a rounded orange "QC agent" rectangle containing an "LLM" box (orange), a
                 "plan–act–observe" loop ring, and green tool glyphs "format reader",
                 "unit resolver", "neighbour query"; from the agent a labelled arrow
                 "flag proposals (justified)" to a vermillion diamond "deterministic QC rules";
                 the diamond lists in small type "physical bounds · rate limits · inter-station";
                 two exits from the diamond — "apply flag" to a sky-blue "flagged record"
                 cylinder, and "reject" to a grey "rejection log" cylinder; a separate
                 sky-blue "provenance store" cylinder receives a dashed line from both exits;
                 a blue "scientist" head-and-shoulders icon oversees the diamond
- flow:          left-to-right — raw inputs → agent → proposals → rules diamond → two exits
                 (apply flag / reject) → flagged record and rejection log; provenance captured
                 from both exits; scientist positioned above the rules as accountable authority
- labels:        "raw inputs", "QC agent", "LLM", "plan – act – observe", "format reader",
                 "unit resolver", "neighbour query", "flag proposals (justified)",
                 "deterministic QC rules", "physical bounds · rate limits · inter-station",
                 "apply flag", "reject", "flagged record", "rejection log", "provenance store",
                 "scientist"
- annotations:   on the raw inputs, "different formats, timestamps, units and update
                 cadences"; on the unit resolver, "no column enters without a declared,
                 checked unit"; on the proposals arrow, in vermillion, "proposals only —
                 the agent has no write access to the data"; on the rules diamond, "code a
                 human wrote, reviewed, and can rerun identically"; on the scientist, "the
                 authority the rules exercise"; on "apply flag", "the measured value is
                 never overwritten"; on "reject", "kept, with the reason it was rejected";
                 on the provenance store, "keyed to the input files and the rule-set version"
- caption:       Figure 6.1 — Who is allowed to change the data, and who is not. The agent reads, normalises and proposes, with justification; deterministic rules dispose of every proposal, under a scientist's authority. An observation is flagged, never silently overwritten, and both the flags and the rejections are written to provenance keyed to the inputs and the rule-set version.
- alt-text:      An architecture diagram. Three raw-input cylinders, a gauge network, a rainfall network and a gridded product, feed a QC agent containing a language model, a plan-act-observe loop and three tools: a format reader, a unit resolver and a neighbour query. An arrow from the agent to a deterministic-rules diamond is labelled flag proposals, justified, and annotated that the agent has no write access to the data and may only propose. The rules diamond lists physical bounds, rate limits and inter-station checks, and is annotated as code a human wrote and can rerun identically. A scientist icon sits above it, annotated as holding the authority the rules exercise. Two exits, apply flag and reject, lead to a flagged-record store and a rejection log, annotated respectively that the measured value is never overwritten and that a rejected proposal is kept with its reason. Both write to a provenance store annotated as keyed to the input files and the rule-set version.
- infographic description: A flat vector architecture diagram on an off-white background,
                 16:9. Title top-left: "Agents propose, QC rules dispose". Standfirst
                 beneath: "The model never writes to the data. It only ever asks." On the
                 left, three stacked sky-blue cylinders "raw inputs", annotated "different
                 formats, timestamps, units and update cadences". An arrow leads right into
                 a medium orange-bordered rounded rectangle "QC agent" containing an orange
                 box "LLM", a circular loop arrow "plan – act – observe", and three small
                 green glyphs "format reader", "unit resolver", "neighbour query"; the unit
                 resolver is annotated "no column enters without a declared, checked unit".
                 From the agent's right edge an arrow labelled "flag proposals (justified)"
                 leads to a vermillion diamond "deterministic QC rules" with small type
                 beneath reading "physical bounds · rate limits · inter-station"; the arrow
                 carries a vermillion callout "proposals only — the agent has no write
                 access to the data", and the diamond is annotated "code a human wrote,
                 reviewed, and can rerun identically". A blue head-and-shoulders icon
                 "scientist" sits above the diamond, annotated "the authority the rules
                 exercise". The diamond has two exits: "apply flag" to a sky-blue cylinder
                 "flagged record", annotated "the measured value is never overwritten"; and
                 "reject" to a grey cylinder "rejection log", annotated "kept, with the
                 reason it was rejected". Dashed lines from both exits reach a sky-blue
                 cylinder "provenance store", annotated "keyed to the input files and the
                 rule-set version". Generous spacing, single-weight lines, sentence case.
```

## 6.4 Worked example: river-gauge and rainfall quality control

The worked example puts the pattern on a concrete reconciliation: a set of river-gauge stage records and a co-located rainfall network, quality-controlled together so the rainfall can later explain or verify the flow **[AUTHOR: specify the catchment, the gauge and rainfall networks, the period, and the volume of records — the concrete scale is what makes the example land, exactly as the operational-morning detail does in Chapter 1]**.
The pipeline has four stages, and the discipline of the chapter lives in the boundaries between them.

In the first stage the agent ingests the heterogeneous formats, calling a declared reader for each source and normalising every series into a common tidy representation with explicit units, an unambiguous UTC timestamp, and an empty flag column.
This is where the agent's format-wrangling strength pays off, and where a unit resolver is invoked on every column, so no quantity enters the record without a declared and checked unit.
That is the single most important defence against the silent-unit failures Chapter 13 takes apart.

In the second stage the agent proposes flags.
For each gap it proposes a classification (telemetry outage, sensor maintenance, recorded zero) with the neighbouring evidence it weighed.
For each candidate spike it proposes accept or reject with an explicit justification referencing the rainfall context, so a stage jump coincident with heavy rainfall is treated very differently from an isolated jump under a dry sky.
Crucially, these proposals are written as structured objects beside the data, never into it.

In the third stage the deterministic rules dispose.
Physical bounds reject any stage outside the gauge's rated range, a rate-of-change limit catches non-physical jumps the agent may have accepted, an inter-station consistency check tests each rainfall proposal against its neighbours, and the network's documented conventions have the final word.
A proposal the agent made confidently but the rules reject is not applied.
It is logged with its rejection reason, and the observation stands as measured.

In the fourth stage every proposal, every disposition and every rejection is written to a provenance record keyed to the input files and the rule-set version, so the state of the record is fully reconstructable, which is the mechanism developed in Chapter 12.
The result **[AUTHOR: report what the run actually produced — counts of proposed, applied and rejected flags, any error the deterministic rules caught that a manual pass had previously missed, and the wall-clock time against the manual baseline in §6.2]** is not a "cleaned" dataset but a *flagged and audited* one, in which every departure from the raw observation is visible, justified and reversible.
Figure 6.4 shows the three characteristic dispositions on a single joined trace: a spike accepted because rainfall supports it, a spike the agent found plausible but the rate-of-change rule rejects for want of any rainfall, and a gap flagged and left unfilled.

**Figure 6.2 — The four-stage QC sequence.**

![A left-to-right sequence in four lanes: ingest and normalise, propose flags, dispose, and record provenance. Six numbered steps carry one observation across them. Step one takes in the raw series; step two normalises units and timestamps to UTC, annotated that an unresolved unit halts the pipeline rather than defaulting; step three proposes a gap or spike flag with its justification and the neighbouring evidence weighed; step four applies physical bounds and inter-station checks; step five either applies the flag or rejects the proposal to a log; step six writes the proposal, the disposition and the reason to provenance. A bold vermillion divider between lanes two and three is labelled the authority boundary, annotated that everything left of it is a request and everything right of it is a decision.](../figures/figure-6-2.svg)

*Figure 6.2 — One observation, six steps, one line that matters. The agent ingests, normalises and proposes; the rules dispose; and every step writes to provenance. The vermillion divider is the whole design: everything to its left is a request, everything to its right is a decision, and the pattern never lets the agent cross it. (Rendered as `figures/figure-6-2.svg` from the brief below, per `FIGURES.md`.)*

```
FIGURE BRIEF
- id:            Figure 6.2
- title:         Ingest, propose, dispose, record
- type:          sequence
- claim:         Each observation flows through four ordered stages with a hard boundary between the agent's proposals and the rules' disposition, and provenance is written at the end of every step.
- standfirst:    Everything left of the red line is a request; everything right of it is a decision.
- canvas:        16:9
- elements:      four vertical lanes read left-to-right as ordered stages, each headed by an
                 icon — stage 1 "ingest and normalise" (orange agent icon), stage 2
                 "propose flags" (orange agent icon), stage 3 "dispose" (vermillion gate
                 diamond), stage 4 "record provenance" (sky-blue cylinder); numbered arrows
                 carry an example datum across the lanes
- flow:          left-to-right, numbered 1–6: (1) raw series in; (2) normalise units and
                 timestamps; (3) propose gap/spike flags with justification; (4) rules apply
                 physical bounds and inter-station checks; (5) apply flag or reject to log;
                 (6) write proposal, disposition and reason to provenance
- labels:        "1 raw series", "2 normalise units + UTC", "3 propose flags + justification",
                 "4 physical bounds + inter-station", "5 apply flag / reject", "6 provenance",
                 "ingest and normalise", "propose flags", "dispose", "record provenance"
- annotations:   on step 2, "an unresolved unit halts the pipeline rather than defaulting";
                 on step 3, "each proposal carries its evidence and the neighbouring
                 context weighed"; on step 4, "the rules can reject a proposal the agent
                 was confident about"; on step 5, "a rejection is logged, and the
                 observation stands as measured"; on step 6, "keyed to the inputs and the
                 rule-set version, so the record can be reconstructed"; on the divider, in
                 vermillion, "authority boundary — agent proposes, rules dispose"
- caption:       Figure 6.2 — One observation, six steps, one line that matters. The agent ingests, normalises and proposes; the rules dispose; and every step writes to provenance. The vermillion divider is the whole design: everything to its left is a request, everything to its right is a decision, and the pattern never lets the agent cross it.
- alt-text:      A left-to-right sequence in four lanes: ingest and normalise, propose flags, dispose, and record provenance. Six numbered steps carry one observation across them. Step one takes in the raw series; step two normalises units and timestamps to UTC, annotated that an unresolved unit halts the pipeline rather than defaulting; step three proposes a gap or spike flag with its justification and the neighbouring evidence weighed; step four applies physical bounds and inter-station checks; step five either applies the flag or rejects the proposal to a log; step six writes the proposal, the disposition and the reason to provenance. A bold vermillion divider between lanes two and three is labelled the authority boundary, annotated that everything left of it is a request and everything right of it is a decision.
- infographic description: A flat vector sequence diagram on an off-white background, 16:9,
                 four vertical lanes read left to right. Title top-left: "Ingest, propose,
                 dispose, record". Standfirst beneath: "Everything left of the red line is a
                 request; everything right of it is a decision." Lane one headed by an
                 orange rounded-square agent icon "ingest and normalise"; lane two by an
                 orange agent icon "propose flags"; lane three by a vermillion diamond
                 "dispose"; lane four by a sky-blue cylinder "record provenance". Numbered
                 single-weight arrows cross the lanes in order, each with an annotation in
                 smaller type beneath: "1 raw series"; "2 normalise units + UTC" / "an
                 unresolved unit halts the pipeline rather than defaulting"; "3 propose
                 flags + justification" / "each proposal carries its evidence and the
                 neighbouring context weighed"; "4 physical bounds + inter-station" / "the
                 rules can reject a proposal the agent was confident about"; "5 apply flag /
                 reject" / "a rejection is logged, and the observation stands as measured";
                 "6 provenance" / "keyed to the inputs and the rule-set version, so the
                 record can be reconstructed". A bold vermillion vertical line divides lane
                 two from lane three, labelled "authority boundary — agent proposes, rules
                 dispose". Generous spacing, one arrowhead style, sentence case.
```

**Figure 6.3 — Conventional QC and the agentic redesign.**

![A two-row before-and-after diagram. The top row shows a person cycling between per-format loaders, hand-tuned checks and a plot-and-eyeball step, annotated that the effort scales with the number of station-format combinations rather than with the science, and a faded note that the reasoning behind each flag survives only in comments and commit messages. The bottom row shows raw inputs feeding a QC agent that proposes into a deterministic-rules diamond, then a flagged record and a provenance store, annotated that the record now carries why each flag was applied. A bracket links the hand-tuned checks in the top row to the deterministic rules in the bottom row, labelled same checks, same authority, retained, with a note that what changed is what surrounds them.](../figures/figure-6-3.svg)

*Figure 6.3 — What the redesign does not touch. The deterministic checks are the same checks, holding the same authority, in both rows. What changes is what sits either side of them: a format-wrangling, proposal-writing agent in front, and a provenance store behind. The manual pattern-recognition goes, and so does the loss of reasoning into comments nobody reads six months later. (Rendered as `figures/figure-6-3.svg` from the brief below, per `FIGURES.md`.)*

```
FIGURE BRIEF
- id:            Figure 6.3
- title:         What changes, and what stays exactly as it was
- type:          before/after
- claim:         The redesign does not replace the deterministic checks; it removes the manual pattern-recognition and the missing audit trail, while leaving authority with the rules.
- standfirst:    The checks are identical in both rows. Only what surrounds them changes.
- canvas:        16:9
- elements:      top row "conventional" — a human icon (blue) cycling between a green
                 "per-format loaders" glyph, a green "hand-tuned checks" glyph and a
                 sky-blue "plot and eyeball" step, with a faded grey "reasoning lost in
                 comments" note; bottom row "agentic redesign" — a sky-blue inputs cylinder,
                 an orange "QC agent" proposing into a vermillion "deterministic rules"
                 diamond, a sky-blue "flagged record" cylinder and a sky-blue "provenance
                 store" cylinder; the deterministic-rules diamond is drawn identically in
                 both rows to show it is retained
- flow:          top row is a manual loop with no persistent record; bottom row is a
                 left-to-right governed flow ending in a flagged record and a provenance store
- labels:        "conventional", "per-format loaders", "hand-tuned checks", "plot and eyeball",
                 "reasoning lost in comments", "agentic redesign", "raw inputs", "QC agent",
                 "deterministic rules", "flagged record", "provenance store"
- annotations:   on the conventional loop, "effort scales with the number of station-format
                 combinations, not with the science"; on the faded note, "why this spike was
                 accepted and that one rejected is rarely reconstructable six months later";
                 on the QC agent, "takes the format-wrangling and writes the justification";
                 on the provenance store, "the record now carries why each flag was
                 applied"; on the linking bracket, "same checks, same authority — retained";
                 beneath the bracket, "what changed is what surrounds them"
- caption:       Figure 6.3 — What the redesign does not touch. The deterministic checks are the same checks, holding the same authority, in both rows. What changes is what sits either side of them: a format-wrangling, proposal-writing agent in front, and a provenance store behind. The manual pattern-recognition goes, and so does the loss of reasoning into comments nobody reads six months later.
- alt-text:      A two-row before-and-after diagram. The top row shows a person cycling between per-format loaders, hand-tuned checks and a plot-and-eyeball step, annotated that the effort scales with the number of station-format combinations rather than with the science, and a faded note that the reasoning behind each flag survives only in comments and commit messages. The bottom row shows raw inputs feeding a QC agent that proposes into a deterministic-rules diamond, then a flagged record and a provenance store, annotated that the record now carries why each flag was applied. A bracket links the hand-tuned checks in the top row to the deterministic rules in the bottom row, labelled same checks, same authority, retained, with a note that what changed is what surrounds them.
- infographic description: A flat vector before-and-after diagram on an off-white
                 background, 16:9, two stacked rows sharing a visual grammar. Title
                 top-left: "What changes, and what stays exactly as it was". Standfirst
                 beneath: "The checks are identical in both rows. Only what surrounds them
                 changes." Top row labelled "conventional": a blue head-and-shoulders icon
                 with curved arrows cycling between a green "per-format loaders" glyph, a
                 green "hand-tuned checks" glyph and a sky-blue "plot and eyeball" box,
                 annotated "effort scales with the number of station-format combinations,
                 not with the science", plus a faded grey note "reasoning lost in comments"
                 annotated "why this spike was accepted and that one rejected is rarely
                 reconstructable six months later". Bottom row labelled "agentic redesign":
                 a sky-blue "raw inputs" cylinder, an arrow to an orange "QC agent"
                 rectangle annotated "takes the format-wrangling and writes the
                 justification", an arrow labelled "propose" to a vermillion "deterministic
                 rules" diamond, then a sky-blue "flagged record" cylinder and a sky-blue
                 "provenance store" cylinder annotated "the record now carries why each flag
                 was applied". A near-black bracket links "hand-tuned checks" in the top row
                 to "deterministic rules" in the bottom row, labelled "same checks, same
                 authority — retained", with a smaller line beneath reading "what changed is
                 what surrounds them". Generous spacing, single-weight lines, sentence case.
```

**Figure 6.4 — An annotated gauge-and-rainfall trace.**

![A two-panel time-series figure sharing one time axis. The upper panel plots river stage; the lower plots co-located rainfall as bars. Three events are marked. Event A is a stage spike sitting above a tall rainfall bar, ticked in green and labelled accepted, a real event backed by rainfall. Event B is a stage spike above a rainless stretch, crossed in vermillion and labelled rejected by rule: the agent proposed accepting it, but there is no rainfall and the rise exceeds the physical rate limit, with a note that this is a fluent proposal that was simply wrong and that the deterministic rule caught it. Event C is a break in the stage line spanned by a grey band, labelled gap flagged and left unfilled, with a note that the agent may classify a gap but may never write a value into one.](../figures/figure-6-4.svg)

*Figure 6.4 — Three dispositions on one real trace. A spike with rainfall underneath it is accepted; a spike without any is rejected by the rate-of-change rule even though the agent proposed accepting it; a telemetry gap is flagged and left exactly as observed. Event B is the one to look at: the proposal was fluent and wrong, and only a physical rule caught it. (Rendered as `figures/figure-6-4.svg` from the brief below, per `FIGURES.md`.)*

```
FIGURE BRIEF
- id:            Figure 6.4
- title:         One trace, three dispositions
- type:          failure trace
- claim:         On a real joined trace the pattern is legible: a rainfall-backed spike is accepted, an unsupported spike the agent liked is rejected by the rules, and a gap is flagged but never filled.
- standfirst:    Event B is the one that matters: a fluent proposal, wrong, caught by a rule.
- canvas:        16:9
- elements:      an upper line plot of river stage (near-black line) over time with three
                 marked events; a lower bar plot of co-located rainfall (sky blue) sharing the
                 time axis; event A a stage spike aligned with a tall rainfall bar, marked with
                 a green tick; event B a stage spike under no rainfall, marked with a
                 vermillion cross; event C a gap in the stage line marked with a grey band
- flow:          left-to-right along a shared time axis; annotations point from each marked
                 event to its disposition label
- labels:        "river stage", "rainfall", "A — accepted: rainfall-backed spike",
                 "B — rejected by rule: no rainfall, exceeds rate limit",
                 "C — gap flagged, not filled"
- annotations:   on A, "the agent proposed accepting it, and the rules agreed"; on B, in
                 vermillion, "the agent proposed accepting this too — a fluent proposal,
                 and simply wrong"; beneath B, "caught by a physical rate-of-change rule,
                 not by anyone reading the output"; on C, "the agent may classify a gap; it
                 may never write a value into one"; a footnote, "every disposition here,
                 including B's rejection, is written to provenance with its reason"
- caption:       Figure 6.4 — Three dispositions on one real trace. A spike with rainfall underneath it is accepted; a spike without any is rejected by the rate-of-change rule even though the agent proposed accepting it; a telemetry gap is flagged and left exactly as observed. Event B is the one to look at: the proposal was fluent and wrong, and only a physical rule caught it. [AUTHOR: replace the schematic events with three real ones from your record and give the actual disposition counts.]
- alt-text:      A two-panel time-series figure sharing one time axis. The upper panel plots river stage; the lower plots co-located rainfall as bars. Three events are marked. Event A is a stage spike sitting above a tall rainfall bar, ticked in green and labelled accepted, a real event backed by rainfall. Event B is a stage spike above a rainless stretch, crossed in vermillion and labelled rejected by rule: the agent proposed accepting it, but there is no rainfall and the rise exceeds the physical rate limit, with a note that this is a fluent proposal that was simply wrong and that the deterministic rule caught it. Event C is a break in the stage line spanned by a grey band, labelled gap flagged and left unfilled, with a note that the agent may classify a gap but may never write a value into one.
- infographic description: A flat vector two-panel time-series figure on an off-white
                 background, 16:9, sharing one horizontal time axis. Title top-left: "One
                 trace, three dispositions". Standfirst beneath: "Event B is the one that
                 matters: a fluent proposal, wrong, caught by a rule." Upper panel: a
                 near-black line "river stage" with three marked events. Lower panel:
                 sky-blue vertical bars "rainfall". Event A is a stage spike aligned above a
                 tall rainfall bar, marked with a small green tick and labelled "A —
                 accepted: rainfall-backed spike", annotated "the agent proposed accepting
                 it, and the rules agreed". Event B is a stage spike above a flat, rainless
                 stretch, marked with a vermillion cross and labelled "B — rejected by rule:
                 no rainfall, exceeds rate limit", with a vermillion annotation "the agent
                 proposed accepting this too — a fluent proposal, and simply wrong" and a
                 smaller line beneath, "caught by a physical rate-of-change rule, not by
                 anyone reading the output". Event C is a break in the stage line spanned by
                 a grey band, labelled "C — gap flagged, not filled", annotated "the agent
                 may classify a gap; it may never write a value into one". A footnote along
                 the bottom reads "every disposition here, including B's rejection, is
                 written to provenance with its reason". Generous spacing, single-weight
                 lines, sentence case.
```

## 6.5 Failure modes

The failures of this pattern are the reason its authority boundary is drawn so strictly, and three recur often enough to name.

The first is the silent unit error, where a quantity is read in one unit and treated as another (accumulation as rate, millimetres as inches, local time as UTC) and no exception is ever raised, because every value stays a plausible number.
This one is dangerous in exact proportion to the model's fluency.
An agent asked to reconcile mixed sources will confidently produce a unified series in which the slip is invisible.
The only defence is making units explicit and machine-checked at ingest, so a column without a declared, resolved unit cannot enter the record at all.
The fuller anatomy of this class belongs to Chapter 13; this chapter's contribution is to put the check at the earliest possible point (high confidence).

The second is plausible-but-wrong gap filling, where the agent, asked to handle a gap, proposes an interpolated or model-inferred value that is physically reasonable, locally smooth, and simply not what the instrument measured.
In the standard taxonomy of hallucination this is a faithfulness failure: the output conflicts with the source it should stay true to rather than with world knowledge (Huang et al., 2023).
The redesign forecloses it by construction.
The agent may propose a *classification* of a gap but is never allowed to write a *value* into it, so a gap is flagged and left, and any filling a later analysis needs is a separate, declared, reversible step under the scientist's authority rather than a quiet substitution buried in the QC pass (high confidence that the constraint is correct; the temptation to relax it is exactly what it guards against).

The third is provenance loss, where the flags and transformations get applied but the reasoning and the rule-set version do not get recorded, so a record that looks defensible cannot actually be defended when somebody asks.
This is the most insidious of the three, because it produces no wrong number at all, only an unauditable right one.
The only defence is treating the provenance write as a non-optional stage of the pipeline, keyed to inputs and rule versions, as Chapter 12 develops.

All three share the signature that recurs throughout the book, introduced as plausible failure in Chapter 1: the output looks finished, and the fault is only visible against the context the finished output has discarded.

## 6.6 Verification checklist

This checklist certifies that a quality-control pass can be operated and audited.
It is written to be applied by a colleague who did not build the workflow, meaning a reviewer rather than the agent, and to be usable in print away from the chapter.

- **No write access.** The agent can read and propose but cannot alter the observational record; every applied change is a flag, and every value substitution is a separate, declared step. Confirm by inspecting the tool interfaces, not the agent's prose.
- **Units resolved at ingest.** No column enters the common representation without a declared, machine-checked unit and an unambiguous UTC timestamp; unresolved units halt the pipeline rather than defaulting (see Chapter 13).
- **Deterministic rules retain authority.** Physical bounds, rate-of-change limits and inter-station checks are code the group wrote and can rerun identically; the agent's confidence never overrides a rule's rejection.
- **Proposals are justified and structured.** Every flag proposal carries its evidence, the neighbouring context considered, and a confidence, as a machine-readable object beside the data.
- **Rejections are logged, not discarded.** A proposal the rules reject is recorded with its rejection reason; the observation stands as measured.
- **Gaps are flagged, never silently filled.** No interpolated or inferred value is written into a gap during QC; filling is a downstream, reversible, declared step.
- **Provenance is complete and keyed.** Every proposal, disposition and rejection is recorded against the input files and the rule-set version, so the record's state is fully reconstructable (see Chapter 12).
- **Reproducible rerun.** Re-running the pipeline on the same inputs with the same rule-set version reproduces the same flags and the same provenance. The rule-set version is what makes that true; the agent's contribution is not part of the guarantee (Chapter 12 §12.4, on reproducible versus auditable).

## 6.7 Repository pointer

The companion repository holds the runnable minimum of this pattern, kept current where the print stays deliberately coarse.
Under `/patterns/ch06-data-qc` sits a small end-to-end example, meaning heterogeneous input readers, a unit-resolution step, an agent that emits structured flag proposals, a deterministic rule set that disposes of them, and a provenance writer, cut down to the smallest form that still demonstrates the authority boundary **[AUTHOR: confirm the pattern directory name and the datasets shipped with it; ship a synthetic or openly licensed gauge-and-rainfall sample so the example runs without restricted data]**.
The prompt that specifies the agent's proposal task lives under `/prompts`, the printable form of §6.6 under `/checklists`, and a sanitised version of the worked-example configuration under `/case-studies` **[AUTHOR: decide what of the real configuration can be shared, per the permissions position on record]**.
Named tools, format libraries and any volatile figures stay in the repository, per the book's vendor-neutral convention: the print carries the pattern and its reasoning, and the repository carries the parts that date.

## References

Huang, L., Yu, W. et al. (2023). *A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions.* arXiv preprint arXiv:2311.05232. [verify DOI of ACM Transactions on Information Systems journal version, 2025]

Pantiukhin, D., Shapkin, B., Kuznetsov, I., Jost, A.A. and Koldunov, N. (2025). *Accelerating earth science discovery via multi-agent LLM systems.* Frontiers in Artificial Intelligence, 8. DOI: 10.3389/frai.2025.1674927.
