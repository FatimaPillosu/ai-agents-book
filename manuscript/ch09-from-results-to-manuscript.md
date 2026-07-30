# Chapter 9 — From results to manuscript

> **Status:** draft r5 · voice v5.0 (`STYLE.md` §1) · sentence-per-line per `STYLE.md` §10 · figures as briefs per `FIGURES.md`.
> **Conventions:** vendor-neutral (outline §9) · **[AUTHOR: …]** marks lived material only the author can supply · **[verify]** marks real but unconfirmed details · citations drawn only from verified reports in `/research`. Nothing has been invented.
> **This chapter:** journal and funder AI-use policy is a volatile landscape, surveyed here by policy class; current specifics are held in the repository, not fixed in print.

---

## 9.1 The problem this chapter addresses

The last part of a scientific project takes a share of your time out of all proportion to the science left in it.

Turning verified results into a manuscript, a set of figures, a data statement and a reply to reviewers is mostly not argument.
It is transcription and reconciliation: reading numbers off a results table into the running text, regenerating a figure because an upstream file changed, reformatting citations to a journal's house style, and assembling a point-by-point reply to a review that landed four months after you last touched the analysis.
The work is exacting, because a single mismatch between a number in the abstract and the same number in a table is exactly the kind of error a reviewer notices.
It is also the work most exposed to the ordinary failures of tired attention.
Across the environmental sciences, the output side of scholarship absorbs a large share of a project's effort while adding almost nothing scientific to it, though this is seldom measured directly (low-to-moderate confidence) **[AUTHOR: if you have a defensible personal estimate — the share of a recent paper's total effort spent on manuscript assembly, figures and revision rather than analysis — it would anchor this claim; otherwise leave it qualitative]**.

So a tool that can read a pipeline's artefacts, assemble a draft, regenerate a figure from the file that produced its numbers, and draft a structured reply to a review deserves careful attention rather than reflexive enthusiasm.
Careful, because the output side is where the characteristic failure of these systems, fluent and plausible and wrong, does the most damage.
A manuscript is where a project makes its claims to the wider community, and an agent that smooths prose can just as easily smooth over an unsupported claim, invent a citation that fits the sentence, or state a result more strongly than the evidence carries.
So the position taken here is narrower than the tooling would allow: agents are drafting and assembly instruments under continuous author control, never authors, and never the authority on what the results mean.
This chapter sets out how figures and tables get generated from pipeline artefacts rather than by hand, how a reviewer-response workflow runs with the human holding sole interpretive authority, how the provenance records of Chapter 12 feed a disclosure statement, and how the whole process stays on the reliable side of the capability boundary drawn in Chapter 1.

## 9.2 The conventional workflow and where it goes wrong

The conventional route from results to submitted manuscript is a chain of manual transcriptions between tools that do not talk to each other.
Every transcription is a place the manuscript can quietly drift away from the analysis behind it.

The path runs from analysis scripts producing numbers and arrays, to a plotting step producing figure files, to a word processor where figures get pasted and numbers get typed, to a reference manager, and finally to a journal's submission system with its own formatting demands.
The artefacts at each stage are copies, not links, and a copy does not update when its source changes.
The failures are familiar to anyone who has assembled a paper under deadline.
A figure in the submitted version was generated from an earlier data file than the table beside it.
A value quoted in the abstract was updated in the table but not in the text.
A significance figure survived from a draft in which the sample was smaller.
None of that is a failure of competence.
It is a failure of an arrangement that depends on human vigilance to keep half a dozen loosely coupled copies of the same numbers in agreement, and vigilance is the resource a project has least of in its closing weeks (high confidence).

The reviewer-response stage concentrates the same weakness under worse conditions.
A review usually arrives months after the analysis went quiet, so you first reconstruct the state of a half-forgotten codebase and dataset, then decide for each comment whether it calls for new analysis, a clarification, or a reasoned disagreement, and finally assemble a reply that quotes the reviewer, states the response, and points to the exact changes made.
Much of the surrounding labour is clerical: collating comments into a table, cross-referencing each to line numbers, re-running an analysis with one parameter changed, regenerating the affected figure.
It lands at exactly the moment when the intellectual core of the task, working out what each comment is really asking and whether it is right, most needs undistracted attention.
The conventional workflow hands the clerical and the interpretive work to the same tired person in the same sitting, and the interpretive work is what suffers.
That is what the agentic redesign aims at.
Not automating the judgement, which stays human, but taking the clerical load off it so the judgement gets made with more attention rather than less (moderate confidence).

**Figure 9.1 — Where the conventional output workflow goes wrong (before/after).**

![A two-row before-and-after diagram. The top row, greyed, shows analysis outputs copied by hand into a figure and typed by hand into a manuscript, with a vermillion divergence-risk marker on each copy step and a callout reading that a copy does not update when its source changes, so a late correction upstream leaves the manuscript quoting stale values. The bottom row shows the same analysis outputs feeding a figure and table generation step and an assembly agent that drafts a manuscript, with a single blue author-control gate and no manual copying, annotated one source, regenerated. A note reads that a number in the abstract now traces to a computation rather than to a recollection.](../figures/figure-9-1.svg)

*Figure 9.1 — Two places a manuscript can quietly stop matching its analysis. In the top row every value is a copy, and a copy does not update when its source changes, so a late fix upstream leaves stale numbers behind. In the bottom row figures, tables and quoted values are regenerated from the same result files, and an author gate stands before anything is accepted. (Rendered as `figures/figure-9-1.svg` from the brief below, per `FIGURES.md`.)*

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

## 9.3 The agentic redesign: assembly under author control

The redesign swaps manual transcription for regeneration from one source of truth, and swaps undifferentiated effort for a division of labour that keeps interpretation human.

The organising principle is simple: every number and every figure in the manuscript should trace to a pipeline artefact and be regenerable from it, so a late change upstream propagates on its own instead of requiring you to remember every place the old value appeared.
In practice that means figures come from a plotting step reading the same result files the analysis wrote, tables get generated from those files rather than typed, and the numbers quoted in the running text are, wherever the format allows, drawn from the same artefacts by templating rather than copied by hand.
An assembly agent operates that arrangement rather than authoring it: regenerating the figure set when a file changes, assembling tables to the journal's column specification, checking quoted values against the tables they came from, and flagging mismatches for you to resolve.
Its outputs stop at an explicit author gate, which is the propose–dispose separation of Chapter 2 §2.6 with the author as the disposer.
How much to automate varies with the manuscript (high confidence in the pattern).

The same principle governs prose drafting, with a sharper boundary, because prose is where accountability is most easily laundered.
An agent can usefully draft a methods section from a specification and a pipeline configuration, a data-availability statement from provenance records, or documentation of a workflow from its own logs.
Those are descriptive tasks whose correctness can be checked against artefacts that already exist.
It can also do mechanical language work, such as enforcing a consistent term, tightening an over-long sentence or aligning citations to a required style, as long as every change gets read.
What it must not do is originate the claims of the paper, decide what the results establish, or produce text whose fluency hides the fact that nobody has personally verified the substance underneath.
So read every sentence carrying your name, and treat agent-drafted prose as a first draft rather than a finished one.
The provenance records of Chapter 12 do double duty here.
They are what the methods and data statements get generated from, and they are also the raw material of the disclosure statement recording how agents were used, so a workflow that keeps good provenance for verification gets its disclosure almost for free (moderate confidence).

A methods section reading "quality-controlled under specification X by an agentic workflow" tells a reader what was done and does not let them do it again.
The model behind it may no longer exist, and the same specification may not return the same work.
So write the claim at the strength it can carry.
Name the specification, the checks that gated the output and the evidential tier reached.
Then say plainly that the agentic step is auditable rather than reproducible.
Identify the deterministic components separately, because those are reproducible in the strict sense (Chapter 12 §12.4, on the difference between reproducible, replicable and auditable).

> **Definition — Disclosure statement.** A short note attached to a paper or proposal that records how AI tools were used in producing it: which tool performed which task, on what, and under whose oversight. It exists so that an editor or reader can see the human accountability behind the work. It is written from the author's own records rather than reconstructed from memory.

**Figure 9.2 — The manuscript pipeline (architecture).**

![An architecture diagram. Two data stores on the left, pipeline artefacts and provenance records, feed an assembly agent in the centre. Beneath the agent sit four generation tools: figure generation, table generation, section drafting and disclosure drafting, the last drawing from provenance, with a bracket reading generated, not hand-copied. Everything converges on a blue author-control gate annotated that the author is the sole interpretive authority and reads every sentence they sign. The gate has an accept exit to the manuscript and the disclosure statement, and a revise exit returning to the agent. A note reads that the agent may describe what was done but never originates a claim about what the results establish.](../figures/figure-9-2.svg)

*Figure 9.2 — Everything in the manuscript is generated from the same two stores. Figures, tables, method sections and the disclosure statement all come from the pipeline artefacts and the provenance record. Keep good provenance for verification and the disclosure comes almost for free. Every generated component stops at the author gate, because the agent describes what was done and never decides what it means. (Rendered as `figures/figure-9-2.svg` from the brief below, per `FIGURES.md`.)*

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

## 9.4 Journal and funder policy as a volatile landscape

The policies governing AI use in manuscript preparation are numerous, inconsistent between publishers and funders, and revised faster than a printed book can track.
So this chapter surveys them by class rather than by name, and sends you to the repository for current specifics.

Three broad classes cover most of what you will meet, and they are worth separating because they impose different obligations.
The first is **disclosure-required**: using AI tools to prepare the manuscript is permitted but must be declared, usually in a designated statement, with varying granularity as to which tools and which tasks must be named.
The second is **use-restricted**: some tasks are permitted and others are not.
A common pattern allows language editing and drafting help whilst forbidding the generation of figures, data or citations, and some rules restrict use in peer review itself, where a funder may prohibit any generative-AI use in reviewing proposals outright because a confidential manuscript cannot be entered into an external system whose onward data handling the reviewer does not control (NIH, 2023).
This chapter treats the author's side of that asymmetry, and Chapter 17 treats the reviewer's, meaning what to ask for when a manuscript was produced with agents.
The third is **authorship-barred**, which is close to universal and on which this book takes an unqualified position: an AI system cannot be listed as an author, because authorship entails accountability for the work and an instrument cannot be accountable.
This is the line the major journals drew within weeks of these tools reaching the mainstream, on exactly that accountability rationale (Nature editorial, 2023) (high confidence; this class is stable where the others are volatile).

Because the rules keep moving, the practical discipline is to build the workflow so it satisfies the strictest plausible reading of all three classes, and to generate the disclosure from records rather than from memory.
Keep provenance of which agent did which task, on what inputs, under whose review (Chapter 12), and a disclosure statement can be assembled to whatever granularity a venue asks for without reconstructing the history afterwards.
A restriction you meet late, such as a journal that forbids agent-generated figures, can then be checked against the record rather than guessed at.
This matters because practice is genuinely unsettled: a 2025 survey of some five thousand researchers found the community sharply split on which uses of AI are acceptable, with adoption running well ahead of disclosure (Nature survey, 2025) **[verify]**, and the safe path through contested norms is a provenance record that can answer any venue's question rather than a memory that cannot.
Because the specifics move, the print states the classes and the reasoning whilst the repository holds a current, dated summary of representative policies and a template disclosure statement mapped to each class **[AUTHOR: maintain the policy summary in the repository and date every entry; cite it here rather than naming any publisher's current policy in print]** **[verify: confirm the authorship-barred position against the current guidance of the major publishers and the main research-integrity bodies at time of release]**.
The stance throughout is conservative: disclose more rather than less, treat the absence of a policy as a reason to apply best practice rather than a licence to skip disclosure, and never enter a confidential manuscript under review into a system whose data handling the reviewer's institution has not sanctioned.
This is also, almost word for word, what European research-funder guidance now asks: the researcher stays responsible for all output, must verify AI-generated results, and should disclose substantial use (European Commission living guidelines, 2024, updated 2026) (moderate-to-high confidence).

The 2026 evidence sharpens the split between the stable class and the volatile ones.
A major publisher's June 2026 policy again confines authorship to humans and holds each author accountable for the whole work, while drawing a concrete disclosure threshold: routine grammar and spelling checking needs no declaration, but any substantive change to a text's structure or content must be declared, naming the tool and its purpose.
That policy also lets a reviewer make narrow, private, non-retaining use on their own report, which is sharper than the blanket prohibition some funders keep (Elsevier, 2026; a policy page, specifics volatile per the repository rule).
A peer-reviewed 2026 systematic review of sixty sources reads it the same way: prohibition of machine authorship is universal, disclosure practice varies enormously by discipline, and prevailing frameworks are fragmented and reactive rather than settled (Slimi, 2026).
The strongest 2026 capability evidence leaves the authorship rule intact.
End-to-end research automation is now peer-reviewed: a fully machine-generated paper was accepted at a workshop-tier venue, with its own authors stating the system cannot yet meet top-tier standards, naming hallucinated and inaccurately cited content among its failure modes, and warning that automated submission at scale could overwhelm peer review (Lu et al., 2026).
That a machine can draft a whole paper changes nothing about who is accountable.
Agents draft under author control, and they are never authors.

**Figure 9.3 — Disclosure decision (flowchart).**

![A top-to-bottom decision flowchart starting from a box reading agent used in preparing this output. The first gate asks whether the venue's policy bars this task; a yes leads to a stop box reading do not use, find a permitted alternative, annotated that some venues forbid agent-generated figures, data or citations outright. The second gate asks whether the task touches a confidential manuscript under review; a yes leads to a stop box reading keep off external systems, annotated that once material is sent, its onward path is beyond your control. The third gate asks whether disclosure is required or is best practice, with a note beside it reading when in doubt, disclose. The main path ends at generate disclosure from provenance records, annotated as assembled to whatever granularity the venue asks for, followed by author confirms.](../figures/figure-9-3.svg)

*Figure 9.3 — Three questions, answered from your provenance record rather than from memory. The first two can stop a use outright, and the confidentiality one is the least negotiable: once material reaches an external service its onward path is beyond your control. Past those, the record is what lets you generate a disclosure at whatever granularity a venue asks for. When in doubt, disclose. (Rendered as `figures/figure-9-3.svg` from the brief below, per `FIGURES.md`.)*

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

## 9.5 Worked example: a reviewer-response workflow

The reviewer-response stage shows the pattern at its sharpest, because it puts a heavy clerical load and high interpretive stakes side by side, and the design keeps the two strictly apart.

The worked example is a revision of an operational hydrology manuscript after peer review **[AUTHOR: supply the paper and the review — even anonymised — so the specific comments, analyses and responses replace the scaffold below; the workflow shape is general, but the worth of the example is in the real interpretive calls you made]**.
The workflow starts with the agent doing only clerical structuring.
It parses the review into a table of individual comments, each with a stable identifier, the reviewer's exact wording quoted verbatim, and a proposed classification into one of a few types: a request for new or changed analysis, a request for clarification, a factual correction, or a point of disagreement.
Classification is a proposal, not a decision.
You read every row and correct the type, because whether a comment is a genuine request for new work or a misunderstanding to be answered in prose is exactly the interpretive judgement this workflow exists to protect.
Nothing about the science has been decided at this stage.
The agent has touched no result and originated no claim; it has turned an unstructured document into an auditable list (high confidence in the shape of this step).

The interpretive core belongs to you alone, and the workflow is arranged so it happens with full attention rather than squeezed in around clerical work.
For each comment you decide the substance of the response: whether the reviewer is right, what new analysis if any is warranted, and how the manuscript should change.
You record those decisions in your own words, and they are the authoritative content of the reply.
Where a decision means re-running an analysis with one parameter changed and regenerating the affected figure and table, the agent does that mechanical task against the existing pipeline, using the same artefact-linked generation as §9.3, and you verify the regenerated output against the result files before it is used.
Only once you have settled every response does the agent go back to a clerical role, assembling the point-by-point reply: for each comment, the reviewer's quoted wording, your response as written, and a precise pointer to the change made in the manuscript, formatted to the journal's expected structure.
Read the assembled reply in full before submission, because the agent's fluency at producing a well-formed response document is exactly what could make an inadequately justified reply read as though it were adequate.
The division of labour is the whole point.
The agent structures and assembles at both ends, you do all the judging in the middle, and the boundary between the two is explicit rather than blurred (moderate-to-high confidence; the exact split depends on the review, and Chapter 13 catalogues what goes wrong when the boundary is allowed to drift).

**Figure 9.4 — The reviewer-response workflow (sequence).**

![A sequence diagram with three columns, an agent, the pipeline and the author, and six numbered steps running top to bottom. Steps one and two are agent clerical work: parsing the review into a table of individual comments with the reviewer's exact wording quoted verbatim, then proposing a classification for each. A grey bracket marks these as clerical only. Step three sits inside a blue band across the centre labelled human interpretive authority, where the author corrects each classification and decides the substance of every response in their own words. Step four regenerates affected figures and tables from the pipeline, and step five carries a vermillion tick reading verify against the result files before use. Step six returns to the agent to assemble the point-by-point reply, with a note that the author reads it in full before submission.](../figures/figure-9-4.svg)

*Figure 9.4 — The agent takes both ends and none of the middle. It turns an unstructured review into an auditable table at the start, and assembles the formatted point-by-point reply at the end. Everything between, deciding whether the reviewer is right and what the manuscript should say, sits in the blue band and belongs to you. The vermillion tick is the reminder that a regenerated figure is checked against the result files before it is used. (Rendered as `figures/figure-9-4.svg` from the brief below, per `FIGURES.md`.)*

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

## 9.6 Failure modes

The output side of scholarship fails in three characteristic ways, and each is dangerous precisely because the agent's fluency makes the failed output look finished.

The first is **fabricated citations**: a reference plausible in author, journal and year that does not exist, or a real reference attached to a claim it does not support.
At the drafting stage the consequence is specific and serious, because a fabricated reference can pass straight into a submitted manuscript or a funding proposal.
So no citation an agent produces or suggests enters the manuscript in this book's workflow without being resolved to a real, retrieved source and checked against the sentence it supports, which is the same citation-verification gate set out for literature synthesis in Chapter 5.
Why models invent references, and worked traces of the failure, belong to the failure gallery in Chapter 13.
What matters here is that the check is mechanical and external to the model, never the model's own assurance that its reference is real.

The second is **style laundering**: agent-smoothed prose that reads as authoritative and, in reading so well, hides whether anyone actually verified the substance behind it.
Uniform polish also removes the places where a claim is weak and would, in your own prose, have shown its hesitation.
This is subtler than fabrication, because nothing in the output is factually wrong on its face.
What is lost is the signal that ordinarily tells a reader, and tells you on re-reading, where the argument is thin.
The discipline against it is that you stay the source of every claim and read every sentence for whether you can personally stand behind it, treating fluency as no evidence of correctness and refusing to accept a well-turned paragraph just because it is well turned.

The third is **over-claiming**: drafted text that states a result more strongly than the evidence carries, such as a correlation described as an effect, a result on one catchment generalised to a class, or an uncertainty range quietly dropped in the abstract.
Over-claiming fits an agent's disposition to produce confident, readable prose better than any other failure here, and this book's certainty-flag discipline is the direct countermeasure: substantive claims carry an explicit statement of confidence, and a claim whose flag cannot be justified is a claim to weaken or remove.

All three share the property Chapter 1 named at the start, that fluency is uncorrelated with correctness, so a polished output is no evidence of a warranted one.
All three share a remedy too: the human, not the agent, is accountable for every claim, and checks each against evidence external to the model (high confidence).

## 9.7 Verification checklist

This checklist certifies that a manuscript assembled with agent help is safe to submit.
Apply it before submission and again before any revision goes back, with each item keyed to a failure described above.
It is written to be printed and used without the chapter open.

- **Every number in the text traces to an artefact.** Each value quoted in the abstract, results and captions matches the pipeline artefact it derives from; regenerate rather than transcribe, and re-check after any late upstream change (guards against divergence, §9.2).
- **Every figure and table is regenerated from source.** No figure or table in the submitted version was produced from a superseded data file; the generating step reads the current result files (guards against divergence, §9.3).
- **Every citation is real and supports its sentence.** Each reference is resolved to a retrieved source and checked to support the specific claim it is attached to; no citation rests on the model's assurance alone (guards against fabricated citations, §9.6; cf. Chapter 5).
- **Every claim carries a justifiable certainty flag.** Substantive claims state their confidence; any claim the author cannot personally stand behind is weakened or removed (guards against over-claiming, §9.6).
- **The author has read every sentence they are signing.** Agent-drafted prose has been interrogated for warranted substance, not accepted for fluency (guards against style laundering, §9.6).
- **The disclosure statement is generated from provenance and matches the venue's class.** The record of which agent did which task feeds a disclosure at the required granularity; confidential manuscripts under review were kept off unsanctioned external systems (satisfies policy, §9.4; cf. Chapter 12).
- **No agent is listed or implied as an author.** Authorship and accountability rest with the human authors alone (§9.4).

## 9.8 Repository pointer

The companion repository holds the perishable and runnable counterparts to this chapter, kept current where print cannot be.
It carries a minimal artefact-linked manuscript example, meaning a small pipeline whose figures, tables and quoted numbers all regenerate from one set of result files, so the pattern of §9.3 can be run rather than only read **[AUTHOR: confirm the runnable example is included and note its path once the `/patterns` layout is settled]**.
It holds the reviewer-response scaffold of §9.5 as a prompt-and-template set, the disclosure-statement templates mapped to the policy classes of §9.4, and a dated summary of representative journal and funder positions maintained between releases because those specifics move faster than the book **[AUTHOR: maintain and date the policy summary; link it here]**.
The verification checklist of §9.7 lives under `/checklists` in printable form.
The division is deliberate, as everywhere in the book: print states the durable pattern and the reasoning, and the repository carries what changes.

---

*Cross-references: literature-grounded citation verification (Chapter 5); provenance and disclosure records (Chapter 12); worked failure traces for fabricated citations, style laundering and over-claiming (Chapter 13).*

## References

- Nature (editorial) (2023). "Tools such as ChatGPT threaten transparent science; here are our ground rules for their use." *Nature*, 613, 612. DOI: 10.1038/d41586-023-00191-1.
- Elsevier (2026). "Generative AI policies for journals." Elsevier editorial policy page, updated June 2026. https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals **[verify: specifics volatile; confirm at citation time]**.
- Naddaf, M. (2025). "Is it OK for AI to write science papers? Nature survey shows researchers are split." *Nature* news feature, reporting a survey of ~5,000 researchers. https://www.nature.com/articles/d41586-025-01463-8 **[verify: author byline and survey figures at citation time]**.
- National Institutes of Health (2023). "The Use of Generative Artificial Intelligence Technologies is Prohibited for the NIH Peer Review Process." NIH Guide Notice NOT-OD-23-149. https://grants.nih.gov/grants/guide/notice-files/NOT-OD-23-149.html **[verify: current NIH AI-in-review policy at citation time]**.
- European Commission, Directorate-General for Research and Innovation (2024, updated 8 May 2026). "Living guidelines on the responsible use of generative AI in research." European Research Area. https://research-and-innovation.ec.europa.eu/document/download/2b6cf7e5-36ac-41cb-aab5-0d32050143dc_en **[verify: provisions of the 2026 update against the updated text]**.
- Lu, C., Lu, C., Lange, R. T., Yamada, Y., Hu, S., Foerster, J., Ha, D. and Clune, J. (2026). "Towards end-to-end automation of AI research." *Nature*, 651(8107), 914–919. DOI: 10.1038/s41586-026-10265-5.
- Slimi, Z. (2026). "A systematic critical review of generative AI's impact on authorship, pedagogy, and integrity (2023–2025)." *Frontiers in Education*, 11. DOI: 10.3389/feduc.2026.1769680.
