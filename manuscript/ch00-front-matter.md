# Front matter

> **Status:** draft r4 · voice v4.0-colloquial (`STYLE.md` §0) · sentence-per-line per `STYLE.md` §10 · figures as briefs per `FIGURES.md`.
> **Conventions:** vendor-neutral (outline §9) · **[AUTHOR: …]** marks lived material only the author can supply · **[verify]** marks real but unconfirmed details · citations drawn only from verified reports in `/research`. Nothing has been invented.

---

## How to read this book

The book has five parts, running from foundations through practice to trust, and then out into adoption.
Reading them in order helps, but nothing depends on it.

Part I sets up the foundations: what an agent is, how to specify work for one, and what stance to take towards the technology.
Part II is the core, developing five workflow patterns across the research lifecycle, from literature synthesis to manuscript preparation, before a final chapter composes them into multi-agent workflows.
Part III matters most: verification, provenance, governance and security, ending with an unvarnished gallery of failures and the checks that catch them.
Part IV puts the whole apparatus to work in two end-to-end case studies.
Part V is about adoption in a real research group, including the costs (financial, institutional and energetic) that a responsible adoption has to price in.

The five parts do not all deserve the same attention from the same reader.
If you want to start doing the work, begin at Chapter 3, where specification is developed.
Most failures trace back to that one skill.
Chapters 1 and 2 will still be there as reference when you need them.
If you are a manager or a research lead and you want the argument rather than the mechanics, read Part V and the failure gallery in Chapter 13, and you will have the essentials.
Nobody should skip Chapter 11.
Verification is the discipline the whole book turns on, and taking the patterns without it means taking the dangerous half.

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

![A legend of six labelled icons arranged in a grid. A blue head-and-shoulders outline is labelled human; an orange rounded square with a loop arrow is labelled agent; a green wrench is labelled tool; a sky-blue cylinder is labelled data store; a vermillion diamond is labelled gate; a purple head-and-shoulders outline with a small tick is labelled reviewer. Each icon carries a short plain-language description of its role.](../figures/figure-0-1.svg)

*Figure 0.1 — The icon key. Six actors recur across every figure in the book, each with one fixed icon and one fixed colour: the human who decides and is accountable (blue), the agent working in its loop (orange), the tool it calls (green), the data store it reads and writes (sky blue), the gate its work must pass (vermillion), and the independent reviewer (purple). Learn them once here; they do not change. (Rendered as `figures/figure-0-1.svg` from the brief below, per `FIGURES.md`.)*

```
FIGURE BRIEF
- id:            Figure 0.1
- title:         The icon key — six recurring actors, one colour and glyph each
- type:          architecture
- claim:         The book's figures are built from six fixed actors, each with one icon and one colour, learned once here and reused unchanged throughout.
- canvas:        16:9
- elements:      six labelled legend entries laid out on an implied grid, each an icon in
                 its fixed role-colour beside a short plain-language label — a blue
                 head-and-shoulders outline "human — a person who decides and is
                 accountable"; an orange rounded square enclosing a small loop arrow
                 "agent — an LLM working in a plan–act–observe loop"; a green wrench glyph
                 "tool — a function or program the agent calls"; a sky-blue cylinder
                 "data store — a dataset, file or record"; a vermillion diamond
                 "gate — a check the work must pass"; a reddish-purple head-and-shoulders
                 outline with a small tick "reviewer — an independent checker"
- flow:          none — this is a legend, not a process; entries are simply arranged in a
                 clear grid (two rows of three)
- labels:        "human", "agent", "tool", "data store", "gate", "reviewer", and the short
                 role phrase beneath each
- annotations:   none; the key carries itself
- caption:       Figure 0.1 — The icon key. Six actors recur across every figure in the book, each with one fixed icon and one fixed colour: the human who decides and is accountable (blue), the agent working in its loop (orange), the tool it calls (green), the data store it reads and writes (sky blue), the gate its work must pass (vermillion), and the independent reviewer (purple). Learn them once here; they do not change.
- alt-text:      A legend of six labelled icons arranged in a grid. A blue head-and-shoulders outline is labelled human; an orange rounded square with a loop arrow is labelled agent; a green wrench is labelled tool; a sky-blue cylinder is labelled data store; a vermillion diamond is labelled gate; a purple head-and-shoulders outline with a small tick is labelled reviewer. Each icon carries a short plain-language description of its role.
- generator prompt: A flat vector legend on an off-white background, six entries arranged in
                 two rows of three on an implied grid, generously spaced. Each entry is a
                 simple monochrome line icon in its role-colour beside a short label. Top
                 row: a blue head-and-shoulders outline labelled "human"; an orange rounded
                 square enclosing a small circular loop arrow labelled "agent"; a green
                 wrench glyph labelled "tool". Bottom row: a sky-blue cylinder labelled
                 "data store"; a vermillion diamond labelled "gate"; a reddish-purple
                 head-and-shoulders outline with a small tick labelled "reviewer". Single
                 stroke weight, no shading, no three-dimensional effects, minimal text,
                 high contrast, legible in greyscale.
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
