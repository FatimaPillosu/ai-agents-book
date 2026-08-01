# Figure briefs — Chapter 8 — Model orchestration and experimentation

Briefs for the figures of `manuscript/ch08-model-orchestration-and-experimentation.md`, held here rather than in the chapter so the prose reads clean.
Each brief follows `FIGURES.md` §6. The caption and alt-text in the chapter are generated with the brief and must be changed here and there together.

## Figure 8.1 — The orchestration agent and its boundary

```
FIGURE BRIEF
- id:            Figure 8.1
- title:         What the orchestration agent does, and what it never does
- type:          architecture
- claim:         The agent schedules, tracks and records a modelling campaign but makes no scientific decision; every scientific choice is a human gate outside the agent's authority.
- standfirst:    Everything inside the dashed line is bookkeeping. Every decision sits outside it.
- canvas:        16:9
- elements:      a central orange-bordered rounded rectangle "orchestration agent"
                 containing four green tool glyphs "expand design", "submit runs", "track
                 state", "record provenance", all inside a grey dashed boundary; feeding
                 in from the left, a blue "experimental design" tag authored at a blue
                 human head-and-shoulders icon "scientist"; below the agent a green
                 scheduler glyph "HPC scheduler" and a sky-blue cylinder "provenance
                 store"; an "anomaly flag" arrow returning to the scientist
- flow:          left-to-right — scientist authors design → agent expands and submits to
                 scheduler → agent tracks state and writes provenance → agent flags
                 anomalies back to scientist; every decision sits with the scientist
- labels:        "scientist", "experimental design", "orchestration agent", "expand
                 design", "submit runs", "track state", "record provenance", "HPC
                 scheduler", "provenance store", "anomaly flag",
                 "no scientific decisions inside this boundary"
- annotations:   on the design tag, "parameters, ranges, metric suite and evaluation
                 period — fixed before any run"; on the dashed boundary, "no scientific
                 decisions inside this boundary"; on the provenance store, "configuration,
                 software version, forcing dataset and random seed, captured as the run
                 launches"; on the anomaly arrow, "the agent may notice a problem; it never
                 adjudicates one"; beside the scientist, a short list, "which design ·
                 which metric · which result to believe · which hypothesis to pursue"
- caption:       Figure 8.1 — The boundary is the design. Inside it the agent expands a fixed design into runs, submits them, tracks them and records what happened; outside it every scientific decision stays with you. The agent can flag an anomaly but never adjudicate one, and provenance is captured as each run launches rather than reconstructed afterwards.
- alt-text:      An architecture diagram. A scientist icon authors an experimental design, annotated as the parameters, ranges, metric suite and evaluation period, fixed before any run. It feeds an orchestration agent holding four tools: expand design, submit runs, track state and record provenance. A grey dashed boundary encloses the agent and its tools only, labelled no scientific decisions inside this boundary. The agent submits to an HPC scheduler and writes to a provenance store, annotated as capturing each run's configuration, software version, forcing dataset and random seed at the moment it launches. An anomaly flag returns from the agent to the scientist, annotated that the agent may notice a problem but never adjudicates it. Four decisions are listed outside the boundary beside the scientist: which design, which metric, which result to believe, which hypothesis to pursue.
- infographic description: A flat vector architecture diagram on an off-white background,
                 16:9. Title top-left: "What the orchestration agent does, and what it never
                 does". Standfirst beneath: "Everything inside the dashed line is
                 bookkeeping. Every decision sits outside it." At the left a blue
                 head-and-shoulders icon "scientist" with a short list beside it in smaller
                 type: "which design · which metric · which result to believe · which
                 hypothesis to pursue". The scientist authors a blue tag "experimental
                 design", annotated "parameters, ranges, metric suite and evaluation period
                 — fixed before any run", which connects rightward into a grey dashed
                 boundary labelled "no scientific decisions inside this boundary". Inside
                 the boundary sits an orange-bordered rounded rectangle "orchestration
                 agent" containing four green tool glyphs "expand design", "submit runs",
                 "track state", "record provenance". Below, outside the agent but inside the
                 diagram, a green scheduler glyph "HPC scheduler" and a sky-blue cylinder
                 "provenance store", the latter annotated "configuration, software version,
                 forcing dataset and random seed, captured as the run launches". An arrow
                 labelled "anomaly flag" returns from the agent to the scientist, annotated
                 "the agent may notice a problem; it never adjudicates one". Generous
                 spacing, single-weight lines, sentence case.
```

## Figure 8.2 — The hypothesis provenance gate

```
FIGURE BRIEF
- id:            Figure 8.2
- title:         Where a generated hypothesis may and may not go
- type:          decision flowchart
- claim:         A model-generated hypothesis is exploratory by default and may enter a result only after a human tests it by a pre-specified procedure and owns the claim; without that step it stays compartmented.
- standfirst:    A suggestion becomes a finding only when a person has tested it and signed for it.
- canvas:        16:9
- elements:      a top orange rounded square "model-generated hypothesis"; a sky-blue
                 cylinder compartment "exploratory record (tagged)"; a vermillion diamond
                 gate "tested by pre-specified procedure?"; a blue human icon "scientist
                 owns the claim"; a green terminus "enters result / manuscript"; a grey
                 terminus "remains exploratory — not a finding"
- flow:          top-to-bottom — hypothesis → exploratory record → gate; "no" exit to the
                 grey terminus; "yes" exit through the scientist icon to the green terminus
- labels:        "model-generated hypothesis", "exploratory record (tagged)",
                 "tested by pre-specified procedure?", "yes", "no",
                 "scientist owns the claim", "enters result / manuscript",
                 "remains exploratory — not a finding"
- annotations:   on the exploratory record, "tagged with its origin and compartmented by
                 construction, not by good intentions"; on the gate, "the procedure is
                 fixed before the test, not chosen after seeing the answer"; on the "no"
                 exit, in vermillion, "hypothesis laundering blocked here"; on the scientist
                 icon, "a named person takes responsibility for the claim"; a footnote, "a
                 better model makes an untested hypothesis more dangerous, not less — its
                 fluency hides the missing evidence more effectively"
- caption:       Figure 8.2 — Where a generated hypothesis may and may not go. A model's suggestion is recorded as exploratory and tagged. It cannot become a finding until a human has tested it by a procedure fixed in advance and put their name to the claim. The vermillion exit is the one that matters: it is where a conjecture that arrived alongside real results gets stopped from being reported as one.
- alt-text:      A top-to-bottom decision flowchart. A model-generated hypothesis enters and is written straight into an exploratory record, tagged with its origin, annotated as compartmented by construction rather than by good intentions. It then meets a gate asking whether it has been tested by a pre-specified procedure. The no exit leads to a terminal reading remains exploratory, not a finding, with a vermillion callout reading hypothesis laundering blocked here. The yes exit passes through a scientist icon annotated that a named person takes responsibility for the claim, and only then reaches a terminal reading enters result or manuscript. A footnote reads that a better model makes an untested hypothesis more dangerous, not less, because its fluency hides the missing evidence more effectively.
- infographic description: A flat vector decision flowchart on an off-white background,
                 16:9, flowing top to bottom. Title top-left: "Where a generated hypothesis
                 may and may not go". Standfirst beneath: "A suggestion becomes a finding
                 only when a person has tested it and signed for it." At the top an orange
                 rounded square "model-generated hypothesis" connects down to a sky-blue
                 cylinder "exploratory record (tagged)", annotated "tagged with its origin
                 and compartmented by construction, not by good intentions". Below it a
                 vermillion diamond "tested by pre-specified procedure?", annotated "the
                 procedure is fixed before the test, not chosen after seeing the answer".
                 Its "no" exit leads left to a grey terminal "remains exploratory — not a
                 finding", carrying a vermillion callout "hypothesis laundering blocked
                 here". Its "yes" exit leads down through a blue head-and-shoulders icon
                 "scientist owns the claim", annotated "a named person takes responsibility
                 for the claim", to a green terminal "enters result / manuscript". A
                 footnote along the bottom reads "a better model makes an untested
                 hypothesis more dangerous, not less — its fluency hides the missing
                 evidence more effectively". Generous spacing, single-weight lines, one
                 arrowhead style, sentence case.
```

## Figure 8.3 — Conventional campaign versus agent-orchestrated campaign

```
FIGURE BRIEF
- id:            Figure 8.3
- title:         From hand-run campaign to orchestrated campaign
- type:          before/after
- claim:         The agentic redesign changes who keeps the record, not who makes the decisions: provenance is captured as a by-product of running, while every scientific choice stays with the scientist in both panels.
- standfirst:    The decisions do not move. The record-keeping does.
- canvas:        16:9
- elements:      two stacked panels sharing a grammar. Top panel "conventional": a blue
                 scientist icon linked by hand to a grey spreadsheet glyph "manual log",
                 loose green script glyphs "edit config · submit · check queue", a sky-blue
                 cylinder "outputs" with a grey dashed broken link to the manual log
                 labelled "drift". Bottom panel "orchestrated": the same blue scientist
                 authoring a blue "experimental design" tag feeding an orange "orchestration
                 agent", a green "scheduler" and a sky-blue "provenance store", joined by an
                 unbroken link "captured at run time"
- flow:          top panel left-to-right with a broken link between runs and the manual log;
                 bottom panel left-to-right with an unbroken link between runs and the
                 provenance store; the scientist icon occupies the same left position in both
- labels:        "conventional", "orchestrated", "scientist", "manual log",
                 "edit config · submit · check queue", "outputs", "drift",
                 "experimental design", "orchestration agent", "scheduler",
                 "provenance store", "captured at run time", "anomaly flag"
- annotations:   on the top panel's broken link, in vermillion, "record reconstructed after
                 the fact, from directory timestamps and half-remembered decisions"; on the
                 top panel's manual log, "diverges silently — nothing enforces that it
                 matches the runs"; on the bottom panel's unbroken link, "record captured as
                 it runs, keyed to the configuration actually used"; on the shared scientist
                 position, "same person, same decisions, both panels"
- caption:       Figure 8.3 — What actually changes is who keeps the record. The scientist occupies the same position in both panels because the decisions do not move. What moves is the link between the runs and the log. In the top panel it is broken and rebuilt from memory afterwards; in the bottom panel it is captured as each run launches.
- alt-text:      A two-panel before-and-after diagram. The top panel, conventional, shows a scientist keeping a manual spreadsheet log by hand beside loose scripts for editing configs, submitting and checking the queue, with outputs in a store. A broken grey link between the outputs and the log is labelled drift, with a callout reading that the record is reconstructed after the fact from directory timestamps and half-remembered decisions. The bottom panel, orchestrated, shows the same scientist authoring an experimental design that feeds an orchestration agent, a scheduler and a provenance store, joined by an unbroken link labelled captured at run time. The scientist icon sits in the same position in both panels, annotated that the decisions did not move; only the record-keeping did.
- infographic description: A flat vector before-and-after diagram on an off-white
                 background, 16:9, two stacked panels sharing a grammar. Title top-left:
                 "From hand-run campaign to orchestrated campaign". Standfirst beneath: "The
                 decisions do not move. The record-keeping does." Top panel labelled
                 "conventional": a blue head-and-shoulders icon "scientist" at the left,
                 linked by a hand-drawn-style line to a grey spreadsheet glyph "manual log"
                 annotated "diverges silently — nothing enforces that it matches the runs";
                 loose green script glyphs "edit config · submit · check queue"; a sky-blue
                 cylinder "outputs" joined to the manual log by a broken grey dashed line
                 labelled "drift", carrying a vermillion callout "record reconstructed after
                 the fact, from directory timestamps and half-remembered decisions". Bottom
                 panel labelled "orchestrated": the same blue scientist icon in the same
                 left position, annotated across both panels "same person, same decisions,
                 both panels"; it authors a blue tag "experimental design" feeding an orange
                 rounded rectangle "orchestration agent", which connects to a green
                 "scheduler" and a sky-blue cylinder "provenance store" by an unbroken line
                 labelled "captured at run time", annotated "keyed to the configuration
                 actually used"; an "anomaly flag" arrow returns to the scientist. Generous
                 spacing, single-weight lines, sentence case.
```

## Figure 8.4 — Orchestrating the three-track intercomparison

```
FIGURE BRIEF
- id:            Figure 8.4
- title:         The three-track intercomparison as an orchestrated sequence
- type:          sequence
- claim:         One agent orchestrates three tracks under a common protocol, recording provenance for each, while evaluation is performed independently against a held-out period the agent never touches.
- standfirst:    The system that runs the experiments does not get to score them.
- canvas:        16:9
- elements:      five vertical lanes with headers — blue "scientist", orange "orchestration
                 agent", green "HPC scheduler", sky-blue "provenance store", and a fifth
                 vermillion header "independent evaluation (Ch. 11)" set apart to the right;
                 numbered steps flow top-to-bottom
- flow:          top-to-bottom numbered steps: 1 scientist authors common protocol and three
                 track configs; 2 agent expands physics / data-driven / hybrid configs into
                 runs; 3 agent submits runs to scheduler; 4 scheduler returns run states;
                 5 agent records each run's provenance; 6 agent flags anomalies to the
                 scientist; 7 held-out evaluation runs in the separate lane; 8 scores returned
- labels:        "scientist", "orchestration agent", "HPC scheduler", "provenance store",
                 "independent evaluation (Ch. 11)", "1 author protocol + 3 track configs",
                 "2 expand: physics · data-driven · hybrid", "3 submit runs", "4 run states",
                 "5 record provenance", "6 flag anomalies", "7 held-out evaluation", "8 scores"
- annotations:   on step 1, "one training period, one evaluation period, one forcing set,
                 one metric suite — so the only difference is the model"; on step 2, "the
                 agent expands a fixed design; it does not prune it"; on step 5, "per run:
                 configuration, software version, forcing dataset, seed"; on step 6, "failed
                 runs, out-of-bounds outputs, diverged training losses — flagged, not
                 judged"; a bracket around steps 2–6, "orchestration only — no scoring
                 here"; on the evaluation lane, in vermillion, "a held-out period the agent
                 had no hand in choosing"
- caption:       Figure 8.4 — Three tracks, one agent, and a scoring step it never touches. The agent expands a protocol the scientist wrote into runs across all three tracks, submits and tracks them, and records provenance for each. Scoring happens in the tinted lane on the right, against a held-out period the agent had no hand in choosing. A system that runs the experiments must not also decide how they are judged.
- alt-text:      A sequence diagram with five lanes: scientist, orchestration agent, HPC scheduler, provenance store, and, set apart to the right in vermillion, independent evaluation. Eight numbered steps run top to bottom. The scientist authors the common protocol and three track configurations. The agent expands them into physics, data-driven and hybrid runs, submits them, receives run states, records provenance for each and flags anomalies back to the scientist. Only then does the independent evaluation lane score the tracks against a held-out period. A bracket around steps two to six is labelled orchestration only, no scoring here. The evaluation lane is tinted apart and annotated that the system running the experiments has no influence over how they are judged.
- infographic description: A flat vector sequence diagram on an off-white background, 16:9,
                 five vertical lanes read top to bottom. Title top-left: "The three-track
                 intercomparison as an orchestrated sequence". Standfirst beneath: "The
                 system that runs the experiments does not get to score them." Lane headers
                 left to right: blue head-and-shoulders "scientist"; orange rounded square
                 "orchestration agent"; green scheduler glyph "HPC scheduler"; sky-blue
                 cylinder "provenance store"; and, separated by a clear gap and set on a
                 pale vermillion tint, "independent evaluation (Ch. 11)". Numbered
                 horizontal arrows: "1 author protocol + 3 track configs", annotated "one
                 training period, one evaluation period, one forcing set, one metric suite —
                 so the only difference is the model"; "2 expand: physics · data-driven ·
                 hybrid", annotated "the agent expands a fixed design; it does not prune
                 it"; "3 submit runs"; "4 run states"; "5 record provenance", annotated "per
                 run: configuration, software version, forcing dataset, seed"; "6 flag
                 anomalies", annotated "failed runs, out-of-bounds outputs, diverged
                 training losses — flagged, not judged"; then, in the separate lane, "7
                 held-out evaluation", annotated in vermillion "a held-out period the agent
                 had no hand in choosing"; and "8 scores". A light bracket spans steps 2 to
                 6, labelled "orchestration only — no scoring here". Generous spacing,
                 single-weight lines, sentence case.
```
