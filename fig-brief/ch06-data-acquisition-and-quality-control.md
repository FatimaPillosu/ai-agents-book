# Figure briefs — Chapter 6 — Data acquisition and quality control

Briefs for the figures of `manuscript/ch06-data-acquisition-and-quality-control.md`, held here rather than in the chapter so the prose reads clean.
Each brief follows `FIGURES.md` §6. The caption and alt-text in the chapter are generated with the brief and must be changed here and there together.

## Figure 6.1 — Propose–dispose architecture

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

## Figure 6.2 — The four-stage QC sequence

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

## Figure 6.3 — Conventional QC and the agentic redesign

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

## Figure 6.4 — An annotated gauge-and-rainfall trace

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
