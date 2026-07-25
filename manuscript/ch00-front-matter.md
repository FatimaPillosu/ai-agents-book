# Front matter

> **Status:** draft r3 · voice v3.3 (`STYLE.md`) · sentence-per-line per `STYLE.md` §10 · figures as briefs per `FIGURES.md`.
> **Conventions:** vendor-neutral (outline §9) · **[AUTHOR: …]** marks lived material only the author can supply · **[verify]** marks real but unconfirmed details · citations drawn only from verified reports in `/research`. Nothing has been invented.

---

## How to read this book

This book is built in five parts, ordered from foundations through practice to trust and then out into adoption, and it is designed to be read in that order without depending on it.
Part I sets up the foundations: what an agent is, how to specify work for one, and the stance a scientist should take towards the technology.
Part II is the core, developing five workflow patterns across the research lifecycle, from literature synthesis to manuscript preparation, before a capstone chapter composes them into multi-agent workflows.
Part III is the centre of gravity: verification, provenance, governance and security, closing with an unvarnished gallery of failures and the checks that catch them.
Part IV puts the whole apparatus to work in two end-to-end case studies, and Part V addresses adoption in a real research group, including the costs (financial, institutional and energetic) that a responsible adoption must price in.

The five parts do not all demand the same attention, and it is worth stating plainly which reader should attend to which.
A practitioner who wants to start doing the work can begin at Chapter 3, where specification, the skill most failures trace back to, is developed, and treat Chapters 1 and 2 as reference.
A manager or research lead who wants the shape of the argument rather than the mechanics can read Part V and the failure gallery of Chapter 13 and come away with the essentials.
No reader, whatever their role, should skip Chapter 11: verification is the discipline the whole book turns on, and a reader who takes the patterns without the verification has taken the dangerous half.

Two conventions run throughout, and both exist to keep the book honest about its own vocabulary.
The first time a demanding term does real work in a chapter, it is explained in an info-box, a short, plain-language definition set off from the main text, and every one of those terms is also collected in the glossary at the back, so that a word can be looked up from anywhere rather than only where it first appears.
The figures follow a single house style, described in full in the figure guide: there are five canonical types (architecture diagrams, sequence diagrams, decision flowcharts, before-and-after workflows, and annotated failure traces) and a fixed set of six icons and colours for the recurring actors, learned once from the key below and reused unchanged for the rest of the book.
Meaning is never carried by colour alone; every colour is paired with a labelled icon or shape, so that the figures still read in greyscale or under colour-vision deficiency.

This is a living book, and that status shapes how it should be used.
The print holds the durable material (the patterns, the reasoning, the stance), whilst the companion repository holds everything that dates quickly: named tools, exact model versions, volatile figures, runnable examples and printable checklists.
Releases are versioned, each a full rebuild from the repository, and a newsletter announces and excerpts each one, so that when a claim in these pages states that the current figure lives in the repository, that division of labour is deliberate, and it is what lets a printed page stay useful whilst the technology underneath it keeps moving.

## What the reader needs

This book is written for a practising environmental or geoscientist who is comfortable with Python and the command line, and it assumes no more than that.
No machine-learning expertise is required; where a technical idea from that field is load-bearing, it is explained in plain language at the point it matters.
A reader without paid access to a frontier model is not left behind: low-compute and open-weight working is treated concretely where it belongs, in the constrained rainfall-verification toolkit of Chapter 14 and the cost model of Chapter 16, rather than assumed away or bolted on as a separate track.
The book is not aimed at machine-learning researchers looking for novel methods, nor at managers looking for pure strategy, although the latter will find Part V and the failure gallery worth their time.

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

This book occupies a niche that its positioning makes explicit, and that placement is its reason for existing.
The existing book-length treatments of agentic AI address engineers building production systems or business audiences deciding whether to buy in; the science-facing material remains largely survey and perspective writing; and the work at the environmental intersection tends to frame agentic AI as an autonomous management technology rather than as research instrumentation.
What the author has not found is a practical, governance-first, diagram-led treatment written for practising environmental researchers and grounded in executed work, and that gap is the space this book sets out to fill.
This positioning rests on a limited scan made in July 2026, to be repeated systematically before release; if a close equivalent already exists, the claim softens, and the author would rather revise it than overstate it (moderate confidence).

The worked examples in this book are drawn from operational hydrology and meteorology, and the provenance of those examples governs how far they can be trusted to travel.
This ground is the one the author actually works on, and it is stated plainly rather than padded with thin, borrowed examples from fields outside that practice.
The patterns themselves are written to transfer across the environmental sciences, and they are pitched at a level of generality intended to earn that claim; the demonstrations, however, are hydrological and meteorological, and cross-domain worked examples are a deliberate deferral to a later edition rather than a promise quietly made and not kept.

## Disclosure statement

This book is written under the same governance it describes, and that reflexive stance is worth making explicit rather than leaving as an unstated irony.
Agents were used substantively in producing the manuscript, in drafting, in research gathering, and in review, and every such use sat inside the specification, verification and audit discipline the chapters argue for, so that the book is, among other things, a worked example of its own method.
That stance comes with a firm limit, stated here at the outset: agents are never authors.
Accountability for every claim, every figure and every judgement in these pages rests with me, the named human author, exactly as the book argues it must, because responsibility is not a capability that transfers to an instrument however good the instrument becomes.

This section will eventually carry a per-chapter account of how agents contributed, generated from the status records each chapter keeps, so that a reader can see the division of labour rather than rely on assertion alone.
That account is left as a skeleton here because it can only be completed once the revision work is finished.

- **[AUTHOR: confirm the per-chapter agent-contribution summary once R1 completes — which agents did what, drawn from the chapter status records.]**
- **[AUTHOR: decide the granularity of the disclosure — per chapter or per task — and whether it lives here in full or here in summary with detail in the repository.]**

The formal mechanism for the audit trail behind this disclosure, that is, how the record is captured, stored and versioned, is a deferred decision rather than a settled one, and for now a per-chapter status header does the work.
An honest skeleton the author can stand behind is preferable to a polished statement that claims more machinery than currently exists.
