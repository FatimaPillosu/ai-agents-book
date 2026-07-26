# Chapter 9 — From results to manuscript

> **Status:** draft r4 · voice v5.0 (`STYLE.md` §1) · sentence-per-line per `STYLE.md` §10 · figures as briefs per `FIGURES.md`.
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

![A two-row comparison. The top row, greyed, shows analysis outputs copied by hand into a figure and typed by hand into a manuscript, with two vermillion divergence-risk markers on the copy steps. The bottom row shows the same analysis outputs feeding a figure and table generation tool and an assembly agent that drafts a manuscript, with a single blue author-control gate and no manual copying.](../figures/figure-9-1.svg)

*Figure 9.1 — The conventional output workflow (top) copies numbers and figures by hand between tools that do not update one another, so a late change upstream can leave the manuscript quoting stale values. The artefact-linked workflow (bottom) regenerates figures and tables from the same source files, and an assembly agent drafts only under an author-control gate. (Rendered as `figures/figure-9-1.svg` from the brief below, per `FIGURES.md`.)*

```
FIGURE BRIEF
- id:            Figure 9.1
- title:         Manual transcription versus artefact-linked assembly
- type:          before/after
- claim:         The conventional output workflow copies numbers and figures by hand between disconnected tools, so the manuscript can silently diverge from the analysis; an artefact-linked workflow regenerates figures and tables from the files that produced them, closing the gap.
- canvas:        16:9
- elements:      TOP ROW "conventional" — a data store cylinder "analysis outputs" (sky blue); an arrow labelled "hand-copied" to a figure glyph (grey); a second "typed by hand" arrow to a document box "manuscript" (grey); each hand-copy arrow marked with a small vermillion gate "divergence risk"; TOP ROW de-emphasised in grey. BOTTOM ROW "artefact-linked" — the same "analysis outputs" cylinder (sky blue); a green tool box "figure/table generation" drawing directly from it; an arrow into "manuscript draft" box; an agent icon (orange) labelled "assembly agent" feeding the draft; a blue human icon "author control" gate over the draft
- flow:          both rows left-to-right; top row shows two vermillion divergence-risk points on the copy arrows; bottom row shows a single generation path with no manual copy and an author-control gate before the draft is accepted
- labels:        "conventional", "analysis outputs", "hand-copied", "typed by hand", "divergence risk", "manuscript", "artefact-linked", "figure / table generation", "assembly agent", "manuscript draft", "author control"
- annotations:   a vermillion callout on the top row "each copy can silently diverge"; a blue callout on the bottom row "one source, regenerated"
- caption:       Figure 9.1 — The conventional output workflow (top) copies numbers and figures by hand between tools that do not update one another, so a late change upstream can leave the manuscript quoting stale values. The artefact-linked workflow (bottom) regenerates figures and tables from the same source files, and an assembly agent drafts only under an author-control gate.
- alt-text:      A two-row comparison. The top row, greyed, shows analysis outputs copied by hand into a figure and typed by hand into a manuscript, with two vermillion divergence-risk markers on the copy steps. The bottom row shows the same analysis outputs feeding a figure and table generation tool and an assembly agent that drafts a manuscript, with a single blue author-control gate and no manual copying.
- generator prompt: A flat vector before/after diagram in two horizontal rows on an off-white background. Top row, drawn in de-emphasis grey and labelled "conventional": a sky-blue cylinder labelled "analysis outputs", an arrow labelled "hand-copied" leading to a grey figure icon, and an arrow labelled "typed by hand" leading to a grey document box labelled "manuscript"; a small vermillion diamond labelled "divergence risk" sits on each of the two arrows, with a vermillion callout reading "each copy can silently diverge". Bottom row, labelled "artefact-linked": the same sky-blue "analysis outputs" cylinder feeding a green box labelled "figure / table generation", an orange rounded-square agent icon labelled "assembly agent", both leading into a box labelled "manuscript draft", with a blue head-and-shoulders icon labelled "author control" placed as a gate before the draft and a blue callout reading "one source, regenerated". Single-weight connectors, one arrowhead style, generous spacing, minimal text.
```

## 9.3 The agentic redesign: assembly under author control

The redesign swaps manual transcription for regeneration from one source of truth, and swaps undifferentiated effort for a division of labour that keeps interpretation human.

The organising principle is simple: every number and every figure in the manuscript should trace to a pipeline artefact and be regenerable from it, so a late change upstream propagates on its own instead of requiring you to remember every place the old value appeared.
In practice that means figures come from a plotting step reading the same result files the analysis wrote, tables get generated from those files rather than typed, and the numbers quoted in the running text are, wherever the format allows, drawn from the same artefacts by templating rather than copied by hand.
An assembly agent sits over that arrangement as an operator, not an author.
It can regenerate the figure set when a file changes, assemble a table to the journal's column specification, check that a value quoted in the abstract matches the table it comes from, and flag mismatches for you to resolve.
The interpretive acts, meaning what the result means, which claim it supports and how strongly to state it, stay entirely with you, and the agent's outputs are proposals you accept, edit or reject at an explicit gate (high confidence in the pattern; how much automation is safe varies with the manuscript).

The same principle governs prose drafting, with a sharper boundary, because prose is where accountability is most easily laundered.
An agent can usefully draft a methods section from a specification and a pipeline configuration, a data-availability statement from provenance records, or documentation of a workflow from its own logs.
Those are descriptive tasks whose correctness can be checked against artefacts that already exist.
It can also do mechanical language work, such as enforcing a consistent term, tightening an over-long sentence or aligning citations to a required style, as long as every change gets read.
What it must not do is originate the claims of the paper, decide what the results establish, or produce text whose fluency hides the fact that nobody has personally verified the substance underneath.
The discipline that prevents that is simple: you remain the source of every claim and read every sentence carrying your name, treating agent-drafted prose as a first draft to interrogate rather than a finished product to accept.
The provenance records of Chapter 12 do double duty here.
They are what the methods and data statements get generated from, and they are also the raw material of the disclosure statement recording how agents were used, so a workflow that keeps good provenance for verification gets its disclosure almost for free (moderate confidence).

> **Definition — Disclosure statement.** A short note attached to a paper or proposal that records how AI tools were used in producing it: which tool performed which task, on what, and under whose oversight. It exists so that an editor or reader can see the human accountability behind the work. It is written from the author's own records rather than reconstructed from memory.

**Figure 9.2 — The manuscript pipeline (architecture).**

![An architecture diagram. Two sky-blue cylinders on the left, pipeline artefacts and provenance records, feed an orange assembly agent with a loop arrow. Beneath the agent, four green tool glyphs handle figure generation, table generation, section drafting and disclosure drafting, bracketed as generated, not hand-copied. All outputs converge on a vermillion author-control gate, staffed by a blue author icon marked as sole interpretive authority, which either accepts a component into the manuscript or returns it to the agent to revise.](../figures/figure-9-2.svg)

*Figure 9.2 — The manuscript pipeline. Figures, tables, prose sections and the disclosure statement are generated from the same pipeline artefacts and provenance records the analysis produced, and every component passes an author-control gate before entering the manuscript. The author, not the agent, is the interpretive authority and the source of every claim. (Rendered as `figures/figure-9-2.svg` from the brief below, per `FIGURES.md`.)*

```
FIGURE BRIEF
- id:            Figure 9.2
- title:         Manuscript assembly from pipeline artefacts under an author gate
- type:          architecture
- claim:         Figures, tables, prose sections and the disclosure statement are all generated from the same pipeline artefacts and provenance records, and every generated component passes an author-control gate before it enters the manuscript.
- canvas:        16:9
- elements:      left, a data store cylinder "pipeline artefacts" (sky blue) and a data store cylinder "provenance records" (sky blue); centre, an orange "assembly agent" rounded square enclosing a small loop arrow, drawing from both cylinders, with three green tool glyphs beneath it labelled "figure generation", "table generation", "section drafting"; a fourth green tool "disclosure drafting" drawing from provenance; right of the agent a vermillion diamond "author-control gate"; beyond it a document box "manuscript" (grey) with a small attached tag "disclosure statement" (grey); a blue human icon "author" positioned at the gate
- flow:          left-to-right — artefacts and provenance feed the assembly agent and its tools; all generated components converge on the author-control gate; the gate has a "accept" exit to the manuscript and a "revise" exit returning to the agent; the author icon sits on the gate
- labels:        "pipeline artefacts", "provenance records", "assembly agent", "figure generation", "table generation", "section drafting", "disclosure drafting", "author-control gate", "accept", "revise", "manuscript", "disclosure statement", "author"
- annotations:   a light bracket under the four green tools labelled "generated, not hand-copied"; a small blue note at the gate "author is sole interpretive authority"
- caption:       Figure 9.2 — The manuscript pipeline. Figures, tables, prose sections and the disclosure statement are generated from the same pipeline artefacts and provenance records the analysis produced, and every component passes an author-control gate before entering the manuscript. The author, not the agent, is the interpretive authority and the source of every claim.
- alt-text:      An architecture diagram. Two sky-blue cylinders on the left, pipeline artefacts and provenance records, feed an orange assembly agent with a loop arrow. Beneath the agent, four green tool glyphs handle figure generation, table generation, section drafting and disclosure drafting, bracketed as generated, not hand-copied. All outputs converge on a vermillion author-control gate, staffed by a blue author icon marked as sole interpretive authority, which either accepts a component into the manuscript or returns it to the agent to revise.
- generator prompt: A flat vector architecture diagram on an off-white background. On the left, two sky-blue cylinders stacked vertically, labelled "pipeline artefacts" and "provenance records". Both connect rightward into a central orange rounded-square agent icon containing a small circular loop arrow, labelled "assembly agent". Beneath the agent sit four green tool glyphs in a row, labelled "figure generation", "table generation", "section drafting" and "disclosure drafting", with a thin bracket under them labelled "generated, not hand-copied"; the "disclosure drafting" tool is linked to the "provenance records" cylinder. To the right of the agent, a vermillion diamond labelled "author-control gate" with a blue head-and-shoulders icon labelled "author" beside it and a small note "author is sole interpretive authority". The diamond has two exits: "accept" leading to a grey document box labelled "manuscript" with a small attached grey tag labelled "disclosure statement", and "revise" curving back to the assembly agent. Single-weight connectors, one arrowhead style, generous margins, minimal text.
```

## 9.4 Journal and funder policy as a volatile landscape

The policies governing AI use in manuscript preparation are numerous, inconsistent between publishers and funders, and revised faster than a printed book can track.
So this chapter surveys them by class rather than by name, and sends you to the repository for current specifics.

Three broad classes cover most of what you will meet, and they are worth separating because they impose different obligations.
The first is **disclosure-required**: using AI tools to prepare the manuscript is permitted but must be declared, usually in a designated statement, with varying granularity as to which tools and which tasks must be named.
The second is **use-restricted**: some tasks are permitted and others are not.
A common pattern allows language editing and drafting help whilst forbidding the generation of figures, data or citations, and some rules restrict use in peer review itself, where a funder may prohibit any generative-AI use in reviewing proposals outright because a confidential manuscript cannot be entered into an external system whose onward data handling the reviewer does not control (NIH, 2023).
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

![A top-to-bottom decision flowchart beginning from an agent being used to prepare an output. The first vermillion gate asks whether the venue bars the task; yes leads to a red stop box advising a permitted alternative. The second gate asks whether a confidential manuscript under review is involved; yes leads to a stop box advising it be kept off external systems. The third gate asks whether disclosure is required or best practice; yes leads to a blue box generating the disclosure from provenance records, no to recording it internally regardless. A blue author-confirms icon sits at the foot, with a note reading when in doubt, disclose.](../figures/figure-9-3.svg)

*Figure 9.3 — A disclosure decision path. Answered from provenance records, three questions decide whether an agentic use is permitted for a given venue and how it must be disclosed. The default under uncertainty is to disclose, and the author confirms the outcome. (Rendered as `figures/figure-9-3.svg` from the brief below, per `FIGURES.md`.)*

```
FIGURE BRIEF
- id:            Figure 9.3
- title:         Deciding what to disclose, and whether a use is permitted at all
- type:          decision flowchart
- claim:         A small set of questions, answered from provenance records, decides whether an agentic use is permitted for a given venue and how it must be disclosed.
- canvas:        portrait 4:5 — a vertical decision flow reads more naturally top-to-bottom and fits the branching without crowding
- elements:      a start box "agent used in preparing this output" (orange); first gate diamond "does the venue's policy bar this task?" (vermillion) with a "yes" exit to a red stop box "do not use; find a permitted alternative" and a "no" exit downward; second gate "does the task touch a confidential manuscript under review?" (vermillion) with a "yes" exit to a stop box "keep off external systems" and "no" downward; third gate "is disclosure required or is best practice to disclose?" (vermillion) with a "yes" exit to a blue action box "generate disclosure from provenance records" and a "no" exit to a grey box "record internally regardless"; a blue human icon "author confirms" at the foot
- flow:          top-to-bottom through three vermillion gates; each gate's exits labelled "yes"/"no"; two early exits to red stop boxes; the main path ends at "generate disclosure from provenance records" then "author confirms"
- labels:        "agent used in preparing this output", "does the venue bar this task?", "yes", "no", "do not use; find a permitted alternative", "confidential manuscript under review?", "keep off external systems", "disclosure required or best practice?", "generate disclosure from provenance records", "record internally regardless", "author confirms"
- annotations:   a small note beside the third gate "when in doubt, disclose"
- caption:       Figure 9.3 — A disclosure decision path. Answered from provenance records, three questions decide whether an agentic use is permitted for a given venue and how it must be disclosed. The default under uncertainty is to disclose, and the author confirms the outcome.
- alt-text:      A top-to-bottom decision flowchart beginning from an agent being used to prepare an output. The first vermillion gate asks whether the venue bars the task; yes leads to a red stop box advising a permitted alternative. The second gate asks whether a confidential manuscript under review is involved; yes leads to a stop box advising it be kept off external systems. The third gate asks whether disclosure is required or best practice; yes leads to a blue box generating the disclosure from provenance records, no to recording it internally regardless. A blue author-confirms icon sits at the foot, with a note reading when in doubt, disclose.
- generator prompt: A flat vector decision flowchart on an off-white background, portrait orientation, reading top to bottom. An orange box at the top labelled "agent used in preparing this output" connects down to a vermillion diamond labelled "does the venue bar this task?"; its "yes" exit goes right to a red-outlined stop box labelled "do not use; find a permitted alternative", its "no" exit continues down to a second vermillion diamond labelled "confidential manuscript under review?"; that diamond's "yes" exit goes right to a red-outlined stop box labelled "keep off external systems", its "no" exit continues down to a third vermillion diamond labelled "disclosure required or best practice?"; its "yes" exit leads to a blue box labelled "generate disclosure from provenance records" and its "no" exit to a grey box labelled "record internally regardless", with a small note beside the gate reading "when in doubt, disclose". Both lower paths converge on a blue head-and-shoulders icon labelled "author confirms" at the foot. Single-weight connectors, one arrowhead style, clear yes/no labels, generous spacing, minimal text.
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

![A top-to-bottom sequence diagram with three columns: an orange agent, a sky-blue pipeline, and a blue author. Steps one and two, bracketed as agent clerical work, have the agent parse the review into a comment table and propose a classification. A central blue band labelled human interpretive authority covers step three, where the author corrects the classification and decides each response, and step four, where a requested re-run regenerates a figure and table from the pipeline. Step five is a vermillion verification gate where the author checks the regenerated output against result files. Step six, again agent clerical work, assembles the reply, which the author reads in full before submission.](../figures/figure-9-4.svg)

*Figure 9.4 — The reviewer-response workflow. The agent structures the review into an auditable comment table (steps 1–2) and later assembles the reply document (step 6); between them the author decides every response and verifies every regenerated artefact. The interpretive centre is reserved for the human by design. (Rendered as `figures/figure-9-4.svg` from the brief below, per `FIGURES.md`.)*

```
FIGURE BRIEF
- id:            Figure 9.4
- title:         Clerical structuring, human judgement, clerical assembly
- type:          sequence
- claim:         The reviewer-response workflow gives the agent the clerical work at both ends and reserves every interpretive decision for the human in the middle, with an explicit boundary between them.
- canvas:        16:9
- elements:      three actor columns — an agent (orange), a data store "pipeline" (sky blue), and a human "author" (blue); numbered exchanges running top to bottom; two of the steps (classification and reply assembly) marked as agent clerical work, the central band marked as human interpretive authority in blue, and the regeneration step touching the pipeline marked with a vermillion verification tick
- flow:          top-to-bottom, numbered 1 to 6 — (1) agent parses review into a comment table with verbatim quotes; (2) agent proposes a classification per comment; (3) author corrects classification and decides each response; (4) author requests a re-run; agent regenerates figure/table from pipeline; (5) author verifies regenerated output against result files [vermillion gate]; (6) agent assembles point-by-point reply; author reads in full before submission
- labels:        "agent", "pipeline", "author", "1 parse review to comment table", "2 propose classification", "3 decide each response", "4 regenerate from pipeline", "5 verify against result files", "6 assemble reply · author reads in full"
- annotations:   a blue band across the centre labelled "human interpretive authority"; a vermillion tick on step 5 "verify before use"; a grey bracket on steps 1–2 and 6 "agent: clerical only"
- caption:       Figure 9.4 — The reviewer-response workflow. The agent structures the review into an auditable comment table (steps 1–2) and later assembles the reply document (step 6); between them the author decides every response and verifies every regenerated artefact. The interpretive centre is reserved for the human by design.
- alt-text:      A top-to-bottom sequence diagram with three columns: an orange agent, a sky-blue pipeline, and a blue author. Steps one and two, bracketed as agent clerical work, have the agent parse the review into a comment table and propose a classification. A central blue band labelled human interpretive authority covers step three, where the author corrects the classification and decides each response, and step four, where a requested re-run regenerates a figure and table from the pipeline. Step five is a vermillion verification gate where the author checks the regenerated output against result files. Step six, again agent clerical work, assembles the reply, which the author reads in full before submission.
- generator prompt: A flat vector sequence diagram on an off-white background with three labelled vertical actor columns: an orange rounded-square agent icon labelled "agent", a sky-blue cylinder labelled "pipeline", and a blue head-and-shoulders icon labelled "author". Six numbered horizontal exchanges read top to bottom: "1 parse review to comment table" and "2 propose classification" from the agent, bracketed in grey and labelled "agent: clerical only"; "3 decide each response" and "4 regenerate from pipeline" within a pale blue horizontal band labelled "human interpretive authority", step 4 drawing an arrow to the pipeline cylinder and back; "5 verify against result files" marked with a small vermillion tick and note "verify before use"; and "6 assemble reply · author reads in full" from the agent, again in the grey clerical bracket. Single-weight connectors, one arrowhead style, numbered steps, generous spacing, minimal text.
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
