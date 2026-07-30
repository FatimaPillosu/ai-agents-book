# Front matter

> **Status:** draft r5 · voice v5.0 (`STYLE.md` §1) · sentence-per-line per `STYLE.md` §10 · figures as briefs per `FIGURES.md`.
> **Conventions:** vendor-neutral (outline §9) · **[AUTHOR: …]** marks lived material only the author can supply · **[verify]** marks real but unconfirmed details · citations drawn only from verified reports in `/research`. Nothing has been invented.

> **[ai-reviewer: A1 review — 3 comments in this file.** Tasks 0.1, 0.2 and 0.3 all landed and the two AUTHOR markers are intact. Two substantive findings: the scope statement's claim that every worked example is routine or semi-routine work needs testing against Chapters 8, 14 and 15 before the author signs it off; and its sentence "Nothing in these pages governs that work" contradicts Chapter 3 §3.7, drafted in the same batch, which says two things do govern it. Escalated to the author: the scope framing itself, which is already marked **[AUTHOR SIGN-OFF]**.**]**

---

## How to read this book

The book has five parts, running from foundations through practice to trust, and then out into adoption.
Reading them in order helps, but nothing depends on it.

Part I sets up the foundations: what an agent is, how to specify work for one, and what stance to take towards the technology.
Part II is the core, developing five workflow patterns across the research lifecycle, from literature synthesis to manuscript preparation, before a final chapter composes them into multi-agent workflows.
Part III matters most: verification, provenance, governance and security, ending with an unvarnished gallery of failures and the checks that catch them.
Part IV puts the whole apparatus to work in two end-to-end case studies.
Part V is about adoption in a real research group, including the costs (financial, institutional and energetic) that a responsible adoption has to price in.
It also covers the reverse position, where the workflow is someone else's and all you can decide is how much to believe it.

The five parts do not all deserve the same attention from the same reader.
If you want to start doing the work, begin at Chapter 3, where specification is developed.
Most failures trace back to that one skill.
Chapters 1 and 2 will still be there as reference when you need them.
If you are a manager or a research lead and you want the argument rather than the mechanics, read Part V and the failure gallery in Chapter 13, and you will have the essentials.
Nobody should skip Chapter 11.
Verification is the discipline the whole book turns on, and taking the patterns without it means taking the dangerous half.
You may also be on the receiving end of agentic work rather than building it.
Reviewing a manuscript someone else produced with agents is that position, and so is inheriting a pipeline you did not specify.
So is being handed a system by your institution.
Chapter 17 is written for that reader, and it can be read on its own.
**[AUTHOR: this pass assumes the eighteen-chapter structure proposed in the integration plan, with a new Chapter 17 and "What will last" as Chapter 18. Confirm or reject it; the routing sentences above and in Chapter 1 §1.5 follow whichever you choose.]**

Two conventions run throughout, and both exist to keep the book honest about its own vocabulary.
The first time a demanding term does real work in a chapter, it gets an info-box: a short, plain-language definition set off from the main text.
Every one of those terms is also collected in the glossary at the back, so you can look a word up from anywhere rather than only where it first appears.
The figures follow one house style, described in full in the figure guide.
There are five canonical types (architecture diagrams, sequence diagrams, decision flowcharts, before-and-after workflows, and annotated failure traces) and six fixed icons and colours for the recurring actors.
Learn them once from the key below; they do not change after that.
Colour never carries meaning on its own, and every colour is paired with a labelled icon or shape, so the figures still read in greyscale and under colour-vision deficiency.

This is a living book, and that changes how to use it.
The print holds the durable material: the patterns, the reasoning, the stance.
The companion repository holds everything that dates quickly: named tools, exact model versions, volatile figures, runnable examples and printable checklists.
Releases are versioned, each one a full rebuild from the repository, and a newsletter announces and excerpts each release.
So when a claim in these pages says that the current figure lives in the repository, that is deliberate.
It is what lets a printed page stay useful whilst the technology underneath it keeps moving.

## What the reader needs

This book is written for a practising environmental or geoscientist who is comfortable with Python and the command line, and it assumes nothing beyond that.
You do not need machine-learning expertise.
Where an idea from that field is essential to the argument, it is explained in plain language at the point where it matters.
If you have no paid access to a frontier model, you are not left behind.
Low-compute and open-weight working is treated concretely where it belongs, in the constrained rainfall-verification toolkit of Chapter 14 and the cost model of Chapter 16, rather than assumed away or added as a separate track.
The book is not for machine-learning researchers after novel methods, nor for managers after pure strategy, though the second group will find Part V and the failure gallery worth their time.

## Icon key — Figure 0.1

**Figure 0.1 — The six recurring actors.**

![An icon key laid out as two rows of three. Each entry pairs a coloured line icon with its name and a short description of its role. A blue head-and-shoulders outline is the human, the person who decides and is accountable. An orange rounded square with a loop arrow is the agent, a language model working in a plan-act-observe loop. A green wrench is the tool, a function or program the agent calls. A sky-blue cylinder is the data store, a dataset, file or record. A vermillion diamond is the gate, a check the work has to pass. A purple head-and-shoulders outline with a tick is the reviewer, an independent checker. A footer line notes that these six never change.](../figures/figure-0-1.svg)

*Figure 0.1 — The six actors every figure in this book is built from. Each one keeps the same icon and the same colour from here to the last page. Learn them once and you can read any later figure without a legend. Colour never carries meaning on its own: every icon is labelled, so the figures work in greyscale too. (Rendered as `figures/figure-0-1.svg` from the brief below, per `FIGURES.md`.)*

```
FIGURE BRIEF
- id:            Figure 0.1
- title:         The six actors, and what each one does
- type:          architecture
- claim:         The book's figures are built from six fixed actors, each with one icon and one colour, learned once here and reused unchanged throughout.
- standfirst:    Learn these six once; they do not change anywhere in the book.
- canvas:        16:9
- elements:      six legend entries on a two-by-three grid, each an icon in its fixed
                 role-colour, its name in element-label type, and a one-line description
                 beneath in annotation type — a blue head-and-shoulders outline "human";
                 an orange rounded square enclosing a loop arrow "agent"; a green wrench
                 glyph "tool"; a sky-blue cylinder "data store"; a vermillion diamond
                 "gate"; a reddish-purple head-and-shoulders outline with a small tick
                 "reviewer"; a footer strip across the bottom
- flow:          none — this is a legend, not a process. Entries are read left to right,
                 top row then bottom row, in the order they first appear in the book
- labels:        "human", "agent", "tool", "data store", "gate", "reviewer"
- annotations:   under "human", "decides, and is accountable for the decision"; under
                 "agent", "a language model working in a plan-act-observe loop"; under
                 "tool", "a function or program the agent calls"; under "data store", "a
                 dataset, a file, a record"; under "gate", "a check the work has to pass
                 before it goes on"; under "reviewer", "checks someone else's work,
                 independently"; footer strip, "these six keep the same icon and colour in
                 every figure in this book"
- caption:       Figure 0.1 — The six actors every figure in this book is built from. Each one keeps the same icon and the same colour from here to the last page. Learn them once and you can read any later figure without a legend. Colour never carries meaning on its own: every icon is labelled, so the figures work in greyscale too.
- alt-text:      An icon key laid out as two rows of three. Each entry pairs a coloured line icon with its name and a short description of its role. A blue head-and-shoulders outline is the human, the person who decides and is accountable. An orange rounded square with a loop arrow is the agent, a language model working in a plan-act-observe loop. A green wrench is the tool, a function or program the agent calls. A sky-blue cylinder is the data store, a dataset, file or record. A vermillion diamond is the gate, a check the work has to pass. A purple head-and-shoulders outline with a tick is the reviewer, an independent checker. A footer line notes that these six never change.
- infographic description: A flat vector legend on an off-white background, 16:9. Title
                 top-left in the largest size: "The six actors, and what each one does".
                 Beneath it a one-line standfirst: "Learn these six once; they do not
                 change anywhere in the book." Below that, six entries on a generously
                 spaced two-by-three grid. Each entry is a simple monochrome line icon in
                 its role-colour, its name beside or beneath it in element-label type, and
                 a one-line description in smaller annotation type under that. Top row,
                 left to right: a blue head-and-shoulders outline labelled "human",
                 described "decides, and is accountable for the decision"; an orange
                 rounded square enclosing a small circular loop arrow labelled "agent",
                 described "a language model working in a plan-act-observe loop"; a green
                 wrench glyph labelled "tool", described "a function or program the agent
                 calls". Bottom row: a sky-blue cylinder labelled "data store", described
                 "a dataset, a file, a record"; a vermillion diamond labelled "gate",
                 described "a check the work has to pass before it goes on"; a
                 reddish-purple head-and-shoulders outline with a small tick labelled
                 "reviewer", described "checks someone else's work, independently". A thin
                 rule across the foot carries the line "these six keep the same icon and
                 colour in every figure in this book". Single stroke weight, no shading, no
                 three-dimensional effects, high contrast, legible in greyscale.
```

## Contribution statement and domain framing

This book occupies a narrow niche, and that is its reason for existing.
The book-length treatments of agentic AI that already exist are written for engineers building production systems, or for business audiences deciding whether to buy in.
The science-facing material is mostly survey and perspective writing.
The work at the environmental intersection tends to treat agentic AI as an autonomous management technology rather than as research instrumentation.
What I have not found is a practical, governance-first, diagram-led treatment written for practising environmental researchers and grounded in work that was actually executed.
That gap is what this book sets out to fill.
The claim rests on a limited scan made in July 2026, which will be repeated systematically before release.
If a close equivalent already exists, the claim softens, and I would rather revise it than overstate it (moderate confidence).

[ai-reviewer: this is the pass's most consequential single sentence and it is asserted rather than tested. Three worked examples look like counter-examples worth reconciling before the author signs it off. Chapter 8's three-track intercomparison is an experimental design, and the chapter's own title is "Model orchestration and experimentation". Chapter 15 is titled "Governing a modelling workflow end to end" and takes a modelling problem through to a publication run. Chapter 14's toolkit produces figures a partner reports as official. If those count as "the work surrounding science" then the category is doing a great deal of load-bearing work and the reader is entitled to see where its edge is; if they do not, the sentence overstates and the list that follows it is not in fact exhaustive. Note also that the review's F7 asked for "an explicit, unapologetic statement of scope", not necessarily for the strong universal quantifier "every". The weaker and more defensible form is available without losing the finding's force. This is the author's call, which is why the [AUTHOR SIGN-OFF] below is right; flagging it so the decision is taken on the evidence rather than on the drafting.]
Every worked example in this book is routine or semi-routine work: quality-control passes on gauge records, verification scores, calibration bookkeeping, manuscript assembly, responses to reviewers.
So this is a governance treatment for the work surrounding science, not a treatment of doing science with agents.
That is a real boundary, and I would rather state it than leave you to find it.
A great deal of the best environmental science is abductive and opportunistic: something odd in a record, followed up because it was odd.
Nothing in these pages governs that work until a specification becomes possible, and Chapter 3 §3.7 says what stands in for governance in the meantime.
[ai-reviewer: this sentence and its own destination disagree on the word "govern". Chapter 3 §3.7 asks "So what governs exploration, if acceptance criteria cannot?" and answers "Two things", naming a bounded budget and a contemporaneous record. Read together, the front matter tells the reader nothing governs exploratory work and §3.7 tells them two things do. Both were drafted in the same batch, which is how the disagreement survived. The fix is a decision about what "govern" means in this book, not a wording tweak: either the front matter concedes that exploration has weaker governance rather than none, or §3.7 stops calling its two practices governance. Whichever way it goes, the same word has to mean the same thing in both places, and the choice affects how strong the scope claim above reads.]
Chapter 4 §4.4 says why the boundary sits where it does, which is that what a task costs to check decides what can safely be delegated.

**[AUTHOR SIGN-OFF]** **[AUTHOR: confirm this scope framing — it changes how the book presents its own reach, and the wording is yours to settle. If you would rather claim more or less than this, say so and the downstream cross-references in Chapters 3 and 4 follow.]**

The worked examples come from operational hydrology and meteorology, and where they come from governs how far you should trust them to travel.
This is the ground I actually work on.
Saying so plainly seems better than padding the book with thin, borrowed examples from fields I do not practise in.
The patterns themselves are written to transfer across the environmental sciences, and they are pitched at a level of generality meant to earn that claim.
The demonstrations, though, are hydrological and meteorological.
Cross-domain worked examples are a deliberate deferral to a later edition, not a promise quietly made and not kept.

## Disclosure statement

This book was written under the same governance it describes, which is worth stating outright rather than leaving as an unstated irony.
Agents were used substantively in producing the manuscript: in drafting, in research gathering, and in review.
Every one of those uses sat inside the specification, verification and audit discipline the chapters argue for, so the book is, among other things, a worked example of its own method.
There is a firm limit on that, and it belongs here at the start: agents are never authors.
Accountability for every claim, every figure and every judgement in these pages rests with me, the named human author, exactly as the book argues it must.
Responsibility is not a capability that transfers to an instrument, however good the instrument becomes.

This section will eventually carry a per-chapter account of how agents contributed, generated from the status records each chapter keeps, so you can see the division of labour rather than take my word for it.
It is a skeleton for now, because it can only be completed once the revision work is.

- **[AUTHOR: confirm the per-chapter agent-contribution summary once R1 completes — which agents did what, drawn from the chapter status records.]**
- **[AUTHOR: decide the granularity of the disclosure — per chapter or per task — and whether it lives here in full or here in summary with detail in the repository.]**

How the audit trail behind this disclosure gets captured, stored and versioned is a deferred decision rather than a settled one, and for now a per-chapter status header does the work.
An honest skeleton I can stand behind beats a polished statement that claims more than currently exists.
