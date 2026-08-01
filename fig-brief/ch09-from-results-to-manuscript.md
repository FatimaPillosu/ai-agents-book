# Figure briefs — Chapter 9 — From results to manuscript

Briefs for the figures of `manuscript/ch09-from-results-to-manuscript.md`, held here rather than in the chapter so the prose reads clean.
Each brief follows `FIGURES.md` §6. The caption and alt-text in the chapter are generated with the brief and must be changed here and there together.

## Figure 9.1 — Where the conventional output workflow goes wrong (before/after)

```
FIGURE BRIEF
- id:            Figure 9.1
- title:         Manual transcription versus artefact-linked assembly
- type:          before/after
- claim:         The conventional output workflow copies numbers and figures by hand between disconnected tools, so the manuscript can silently diverge from the analysis; an artefact-linked workflow regenerates figures and tables from the files that produced them, closing the gap.
- standfirst:    A copy does not update when its source changes.
- canvas:        16:9
- elements:      TOP ROW "conventional" — a data store cylinder "analysis outputs" (sky
                 blue); an arrow "hand-copied" to a figure glyph (grey); a second arrow
                 "typed by hand" to a document box "manuscript" (grey); each copy arrow
                 marked with a small vermillion gate "divergence risk"; the row
                 de-emphasised in grey. BOTTOM ROW "artefact-linked" — the same "analysis
                 outputs" cylinder; a green tool box "figure / table generation" drawing
                 directly from it; an orange "assembly agent"; a "manuscript draft" box; a
                 blue "author control" gate before acceptance
- flow:          both rows left-to-right; top row shows two vermillion divergence-risk
                 points on the copy arrows; bottom row shows a single generation path with
                 no manual copy and an author-control gate before the draft is accepted
- labels:        "conventional", "analysis outputs", "hand-copied", "typed by hand",
                 "divergence risk", "manuscript", "artefact-linked",
                 "figure / table generation", "assembly agent", "manuscript draft",
                 "author control"
- annotations:   on the top row's copy arrows, in vermillion, "each copy can silently
                 diverge — a copy does not update when its source changes"; beneath the top
                 row, "a figure generated from an earlier file than the table beside it; a
                 value updated in the table but not in the text"; on the bottom row's
                 generation step, in blue, "one source, regenerated"; on the author gate,
                 "the author accepts, edits or rejects — nothing lands unread"; a footer,
                 "a number in the abstract now traces to a computation, not a recollection"
- caption:       Figure 9.1 — Two places a manuscript can quietly stop matching its analysis. In the top row every value is a copy, and a copy does not update when its source changes, so a late fix upstream leaves stale numbers behind. In the bottom row figures, tables and quoted values are regenerated from the same result files, and an author gate stands before anything is accepted.
- alt-text:      A two-row before-and-after diagram. The top row, greyed, shows analysis outputs copied by hand into a figure and typed by hand into a manuscript, with a vermillion divergence-risk marker on each copy step and a callout reading that a copy does not update when its source changes, so a late correction upstream leaves the manuscript quoting stale values. The bottom row shows the same analysis outputs feeding a figure and table generation step and an assembly agent that drafts a manuscript, with a single blue author-control gate and no manual copying, annotated one source, regenerated. A note reads that a number in the abstract now traces to a computation rather than to a recollection.
- infographic description: A flat vector before-and-after diagram on an off-white
                 background, 16:9, two stacked rows sharing aligned columns. Title top-left:
                 "Manual transcription versus artefact-linked assembly". Standfirst beneath:
                 "A copy does not update when its source changes." Top row labelled
                 "conventional", drawn in de-emphasised grey: a sky-blue cylinder "analysis
                 outputs"; an arrow labelled "hand-copied" to a grey figure glyph; a second
                 arrow labelled "typed by hand" to a grey document box "manuscript". Each
                 copy arrow carries a small vermillion marker "divergence risk", sharing the
                 callout "each copy can silently diverge — a copy does not update when its
                 source changes". Beneath the row, in smaller type: "a figure generated from
                 an earlier file than the table beside it; a value updated in the table but
                 not in the text". Bottom row labelled "artefact-linked", in full colour:
                 the same sky-blue cylinder "analysis outputs" feeding a green tool box
                 "figure / table generation", annotated in blue "one source, regenerated";
                 an orange rounded square "assembly agent" drafting into a "manuscript
                 draft" box; and a blue head-and-shoulders "author control" gate before
                 acceptance, annotated "the author accepts, edits or rejects — nothing lands
                 unread". A footer line reads "a number in the abstract now traces to a
                 computation, not a recollection". Generous spacing, sentence case.
```

## Figure 9.2 — The manuscript pipeline (architecture)

```
FIGURE BRIEF
- id:            Figure 9.2
- title:         Manuscript assembly from pipeline artefacts under an author gate
- type:          architecture
- claim:         Figures, tables, prose sections and the disclosure statement are all generated from the same pipeline artefacts and provenance records, and every generated component passes an author-control gate.
- standfirst:    The agent describes what was done. It never decides what it means.
- canvas:        16:9
- elements:      left, two data-store cylinders (sky blue) "pipeline artefacts" and
                 "provenance records"; centre, an orange "assembly agent" rounded square
                 enclosing a loop arrow, drawing from both, with four green tool glyphs
                 beneath it "figure generation", "table generation", "section drafting",
                 "disclosure drafting"; right, a blue "author-control gate" and the outputs
                 "manuscript" and "disclosure statement"
- flow:          left-to-right — artefacts and provenance feed the assembly agent and its
                 tools; all generated components converge on the author-control gate; the
                 gate has an "accept" exit to the manuscript and a "revise" exit returning
                 to the agent
- labels:        "pipeline artefacts", "provenance records", "assembly agent",
                 "figure generation", "table generation", "section drafting",
                 "disclosure drafting", "author-control gate", "accept", "revise",
                 "manuscript", "disclosure statement", "author"
- annotations:   on the two cylinders, "one source for every number and every figure"; a
                 bracket under the four tools, "generated, not hand-copied"; on "section
                 drafting", "methods and data statements — descriptive, checkable against
                 artefacts that already exist"; on "disclosure drafting", "assembled from
                 the record, not reconstructed from memory"; on the author gate, in blue,
                 "the author is the sole interpretive authority, and reads every sentence
                 they sign"; a footer, "the agent may describe what was done; it never
                 originates a claim about what the results establish"
- caption:       Figure 9.2 — Everything in the manuscript is generated from the same two stores. Figures, tables, method sections and the disclosure statement all come from the pipeline artefacts and the provenance record. Keep good provenance for verification and the disclosure comes almost for free. Every generated component stops at the author gate, because the agent describes what was done and never decides what it means.
- alt-text:      An architecture diagram. Two data stores on the left, pipeline artefacts and provenance records, feed an assembly agent in the centre. Beneath the agent sit four generation tools: figure generation, table generation, section drafting and disclosure drafting, the last drawing from provenance, with a bracket reading generated, not hand-copied. Everything converges on a blue author-control gate annotated that the author is the sole interpretive authority and reads every sentence they sign. The gate has an accept exit to the manuscript and the disclosure statement, and a revise exit returning to the agent. A note reads that the agent may describe what was done but never originates a claim about what the results establish.
- infographic description: A flat vector architecture diagram on an off-white background,
                 16:9. Title top-left: "Manuscript assembly from pipeline artefacts under an
                 author gate". Standfirst beneath: "The agent describes what was done. It
                 never decides what it means." At the left, two sky-blue cylinders stacked,
                 "pipeline artefacts" and "provenance records", sharing the annotation "one
                 source for every number and every figure". Both feed rightward into an
                 orange rounded square "assembly agent" enclosing a small loop arrow.
                 Beneath the agent, a row of four green tool glyphs: "figure generation",
                 "table generation", "section drafting" annotated "methods and data
                 statements — descriptive, checkable against artefacts that already exist",
                 and "disclosure drafting" annotated "assembled from the record, not
                 reconstructed from memory" and drawn with its own link back to the
                 provenance cylinder. A light bracket spans the four tools, labelled
                 "generated, not hand-copied". All four converge rightward on a blue
                 head-and-shoulders gate "author-control gate", annotated "the author is the
                 sole interpretive authority, and reads every sentence they sign". The gate
                 has an "accept" exit to two output boxes, "manuscript" and "disclosure
                 statement", and a "revise" exit curving back to the agent. A footer line
                 reads "the agent may describe what was done; it never originates a claim
                 about what the results establish". Generous spacing, sentence case.
```

## Figure 9.3 — Disclosure decision (flowchart)

```
FIGURE BRIEF
- id:            Figure 9.3
- title:         Deciding what to disclose, and whether a use is permitted at all
- type:          decision flowchart
- claim:         A small set of questions, answered from provenance records, decides whether an agentic use is permitted for a given venue and how it must be disclosed.
- standfirst:    Answer these from your record, not from memory.
- canvas:        16:9
- elements:      a start box "agent used in preparing this output" (orange); three
                 vermillion diamond gates; two red stop boxes; a terminal "generate
                 disclosure from provenance records" and a final "author confirms"
- flow:          top-to-bottom through three vermillion gates, each with "yes"/"no" exits;
                 two early exits to red stop boxes; the main path ends at "generate
                 disclosure from provenance records" then "author confirms"
- labels:        "agent used in preparing this output", "does the venue bar this task?",
                 "yes", "no", "do not use; find a permitted alternative",
                 "confidential manuscript under review?", "keep off external systems",
                 "disclosure required or best practice?",
                 "generate disclosure from provenance records", "author confirms"
- annotations:   on gate 1, "some venues forbid agent-generated figures, data or citations
                 outright"; on gate 2, in vermillion, "once material is sent, its onward
                 path is beyond your control"; beside gate 3, "when in doubt, disclose";
                 on the disclosure terminal, "assembled to whatever granularity the venue
                 asks for, because the record already exists"; a footer, "no agent is ever
                 listed or implied as an author — that class of rule is stable where the
                 others move"
- caption:       Figure 9.3 — Three questions, answered from your provenance record rather than from memory. The first two can stop a use outright, and the confidentiality one is the least negotiable: once material reaches an external service its onward path is beyond your control. Past those, the record is what lets you generate a disclosure at whatever granularity a venue asks for. When in doubt, disclose.
- alt-text:      A top-to-bottom decision flowchart starting from a box reading agent used in preparing this output. The first gate asks whether the venue's policy bars this task; a yes leads to a stop box reading do not use, find a permitted alternative, annotated that some venues forbid agent-generated figures, data or citations outright. The second gate asks whether the task touches a confidential manuscript under review; a yes leads to a stop box reading keep off external systems, annotated that once material is sent, its onward path is beyond your control. The third gate asks whether disclosure is required or is best practice, with a note beside it reading when in doubt, disclose. The main path ends at generate disclosure from provenance records, annotated as assembled to whatever granularity the venue asks for, followed by author confirms.
- infographic description: A flat vector decision flowchart on an off-white background,
                 16:9, flowing top to bottom. Title top-left: "Deciding what to disclose, and
                 whether a use is permitted at all". Standfirst beneath: "Answer these from
                 your record, not from memory." At the top an orange box "agent used in
                 preparing this output". Below it a vermillion diamond "does the venue bar
                 this task?", annotated "some venues forbid agent-generated figures, data or
                 citations outright"; its "yes" exit leads right to a red-outlined stop box
                 "do not use; find a permitted alternative". Its "no" exit leads down to a
                 second vermillion diamond "confidential manuscript under review?",
                 annotated in vermillion "once material is sent, its onward path is beyond
                 your control"; its "yes" exit leads right to a red-outlined stop box "keep
                 off external systems". Its "no" exit leads down to a third vermillion
                 diamond "disclosure required or best practice?", with a small note beside
                 it "when in doubt, disclose". The main path continues to a box "generate
                 disclosure from provenance records", annotated "assembled to whatever
                 granularity the venue asks for, because the record already exists", and
                 then to a blue "author confirms". A footer line reads "no agent is ever
                 listed or implied as an author — that class of rule is stable where the
                 others move". Generous spacing, one arrowhead style, sentence case.
```

## Figure 9.4 — The reviewer-response workflow (sequence)

```
FIGURE BRIEF
- id:            Figure 9.4
- title:         Clerical structuring, human judgement, clerical assembly
- type:          sequence
- claim:         The reviewer-response workflow gives the agent the clerical work at both ends and reserves every interpretive decision for the human in the middle, with an explicit boundary between them.
- standfirst:    The agent takes both ends. You take all of the middle.
- canvas:        16:9
- elements:      three actor columns — an agent (orange), a data store "pipeline" (sky
                 blue), and a human "author" (blue); numbered exchanges running top to
                 bottom; a grey bracket marking steps 1–2 and 6 as agent clerical work; a
                 blue band across the centre marking human interpretive authority; a
                 vermillion tick on the verification step
- flow:          top-to-bottom, numbered 1 to 6 — (1) agent parses review into a comment
                 table with verbatim quotes; (2) agent proposes a classification per
                 comment; (3) author corrects classification and decides each response;
                 (4) author directs regeneration from the pipeline; (5) author verifies the
                 regenerated output against the result files; (6) agent assembles the reply
- labels:        "agent", "pipeline", "author", "1 parse review to comment table",
                 "2 propose classification", "3 decide each response",
                 "4 regenerate from pipeline", "5 verify against result files",
                 "6 assemble reply · author reads in full"
- annotations:   on step 1, "the reviewer's exact wording, quoted verbatim"; on step 2,
                 "a proposal, not a decision"; on the blue centre band, "human interpretive
                 authority — is the reviewer right, and what should change?"; on step 5,
                 in vermillion, "verify before use"; on step 6, "the agent formats; the
                 author reads it in full before submission"; a grey bracket on steps 1–2
                 and 6, "agent: clerical only"
- caption:       Figure 9.4 — The agent takes both ends and none of the middle. It turns an unstructured review into an auditable table at the start, and assembles the formatted point-by-point reply at the end. Everything between, deciding whether the reviewer is right and what the manuscript should say, sits in the blue band and belongs to you. The vermillion tick is the reminder that a regenerated figure is checked against the result files before it is used.
- alt-text:      A sequence diagram with three columns, an agent, the pipeline and the author, and six numbered steps running top to bottom. Steps one and two are agent clerical work: parsing the review into a table of individual comments with the reviewer's exact wording quoted verbatim, then proposing a classification for each. A grey bracket marks these as clerical only. Step three sits inside a blue band across the centre labelled human interpretive authority, where the author corrects each classification and decides the substance of every response in their own words. Step four regenerates affected figures and tables from the pipeline, and step five carries a vermillion tick reading verify against the result files before use. Step six returns to the agent to assemble the point-by-point reply, with a note that the author reads it in full before submission.
- infographic description: A flat vector sequence diagram on an off-white background, 16:9,
                 three vertical columns read top to bottom. Title top-left: "Clerical
                 structuring, human judgement, clerical assembly". Standfirst beneath: "The
                 agent takes both ends. You take all of the middle." Column headers: orange
                 rounded square "agent"; sky-blue cylinder "pipeline"; blue
                 head-and-shoulders "author". Six numbered horizontal steps: "1 parse review
                 to comment table", annotated "the reviewer's exact wording, quoted
                 verbatim"; "2 propose classification", annotated "a proposal, not a
                 decision"; "3 decide each response", sitting inside a pale blue band that
                 spans the canvas labelled "human interpretive authority — is the reviewer
                 right, and what should change?"; "4 regenerate from pipeline"; "5 verify
                 against result files", carrying a vermillion tick and the annotation
                 "verify before use"; "6 assemble reply · author reads in full", annotated
                 "the agent formats; the author reads it in full before submission". A grey
                 bracket spans steps 1 to 2 and step 6, labelled "agent: clerical only".
                 Generous spacing, single-weight lines, sentence case.
```
