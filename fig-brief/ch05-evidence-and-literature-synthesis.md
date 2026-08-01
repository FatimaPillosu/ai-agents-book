# Figure briefs — Chapter 5 — Evidence and literature synthesis

Briefs for the figures of `manuscript/ch05-evidence-and-literature-synthesis.md`, held here rather than in the chapter so the prose reads clean.
Each brief follows `FIGURES.md` §6. The caption and alt-text in the chapter are generated with the brief and must be changed here and there together.

## Figure 5.1 — Conventional versus agentic synthesis

```
FIGURE BRIEF
- id:            Figure 5.1
- title:         Where the work moves, and where it does not
- type:          before/after
- claim:         The agentic redesign moves retrieval, triage and drafting to an agent and inserts a citation-verification gate, while the interpretive act stays with the scientist in both workflows.
- standfirst:    The agent takes the time-consuming stages; you keep the one that decides what it means.
- canvas:        16:9
- elements:      top row (conventional) — human icon (blue) performing four sequential stages "search", "triage", "read and note", "draft", ending at a human "interpret" (blue); bottom row (agentic) — a "specification" tag (blue) feeding an agent (orange) that performs "retrieve", "triage", "draft" against a data store (sky blue), then a vermillion diamond "citation-verification gate", then a human "interpret and decide" (blue); the interpret step is aligned vertically across both rows to show it is unchanged
- flow:          left-to-right in both rows; the two rows share the same horizontal stage positions so the difference is legible by column
- labels:        "conventional", "search", "triage", "read and note", "draft", "interpret",
                 "agentic", "specification", "retrieve", "triage", "draft", "corpus",
                 "citation-verification gate", "interpret and decide"
- annotations:   bracket over the conventional search, triage and read stages, "most of the
                 time goes here — and a body of work you never found leaves no trace in the
                 finished text"; on the corpus store, "drafting may draw only on what was
                 actually retrieved"; on the gate, "every claim traced to a source that
                 exists and supports it"; on the aligned interpret column, "this is the
                 stage the redesign deliberately leaves alone"
- caption:       Figure 5.1 — What moves and what does not. The agent takes over retrieval, triage and drafting, which are the stages that eat the time, and a verification gate stands between its output and you. The interpretive step is drawn in the same column in both rows on purpose: deciding what the evidence means is the one stage this redesign deliberately leaves alone.
- alt-text:      A two-row before-and-after diagram on a shared grid. The top row shows a person working through search, triage, reading and drafting to an interpret step, with a bracket over the first three stages noting that they take most of the time and that a missed body of work leaves no trace in the finished text. The bottom row shows a specification feeding an agent that retrieves, triages and drafts against a corpus store, annotated that drafting may draw only on what was actually retrieved. Its output passes a citation-verification gate, annotated that every claim must trace to a source that exists and supports it, before reaching the same human interpret-and-decide step. That step sits in the same column in both rows, annotated as the part that does not move.
- infographic description: A flat vector before-and-after workflow diagram on an off-white
                 background, 16:9, in two horizontal rows sharing aligned column positions.
                 Title top-left: "Where the work moves, and where it does not". Standfirst
                 beneath: "The agent takes the time-consuming stages; you keep the one that
                 decides what it means." Top row labelled "conventional": a blue
                 head-and-shoulders icon followed by four near-black boxes "search",
                 "triage", "read and note", "draft", ending in a blue box "interpret". A
                 bracket over the first three boxes reads "most of the time goes here — and
                 a body of work you never found leaves no trace in the finished text".
                 Bottom row labelled "agentic": a small blue tag "specification" feeds an
                 orange rounded rectangle "agent" containing "retrieve", "triage", "draft",
                 linked downward to a sky-blue cylinder "corpus" annotated "drafting may
                 draw only on what was actually retrieved"; an arrow leads right to a
                 vermillion diamond "citation-verification gate" annotated "every claim
                 traced to a source that exists and supports it", then to a blue box
                 "interpret and decide" positioned directly below the top row's "interpret".
                 A vertical tint band behind that shared column carries the note "this is
                 the stage the redesign deliberately leaves alone". Single-weight
                 connectors, one arrowhead style, generous spacing, sentence case.
```

## Figure 5.2 — The retrieval-grounded synthesis pipeline

```
FIGURE BRIEF
- id:            Figure 5.2
- title:         Retrieval-grounded synthesis, with the gate that makes it safe
- type:          architecture
- claim:         Grounded drafting and an independent citation-verification gate together confine the fabricated-citation failure mode, leaving interpretation to the human.
- standfirst:    The model writes only about documents that were actually fetched, and a separate step checks every one.
- canvas:        16:9
- elements:      a "specification" tag (blue) at left; an agent (orange) labelled "retrieval and drafting agent" containing an "LLM" box (orange) and a "plan–act–observe" loop; retrieval tools (green) labelled "bibliographic search" and "web search"; a data store (sky blue) labelled "retrieved corpus"; a separate check (orange border, vermillion gate glyph) labelled "citation-verification gate" with a reviewer icon (purple) attached to denote independence; a human "interpret and decide" icon (blue) at right
- flow:          left-to-right: specification → retrieval/drafting agent (which calls the green search tools and writes to the sky-blue corpus, then reads from it to draft) → citation-verification gate → human; the gate has a "fail" return arrow back to the drafting agent and a "pass" arrow forward to the human
- labels:        "specification", "retrieval and drafting agent", "LLM",
                 "plan – act – observe", "bibliographic search", "web search",
                 "retrieved corpus", "citation-verification gate", "pass", "fail",
                 "interpret and decide"
- annotations:   on the search tools, "several vocabularies on purpose — the terminology is
                 unsettled"; on the corpus, "drafting may draw on this and nothing else";
                 on the gate, "three tests: the work exists · the passage is really in it ·
                 the passage supports the claim"; on the reviewer icon, "a separate step,
                 not the agent that wrote the draft"; on the fail arrow, "removed or
                 returned for correction"; on the human, "decides what the evidence means";
                 a vermillion note under the gate, "a run where nothing fails is evidence
                 the check is broken, not that the corpus was clean"
- caption:       Figure 5.2 — The pattern in one picture. Retrieval fills a corpus, drafting is confined to that corpus, and an independent gate tests every citation three ways before anything reaches you. Watch the gate's failure count: a run where nothing is rejected is evidence the check is broken, not that the drafting was flawless.
- alt-text:      An architecture diagram. A specification feeds a retrieval-and-drafting agent containing a language model and a plan-act-observe loop. The agent calls bibliographic-search and web-search tools, annotated as searching several vocabularies deliberately because the terminology is unsettled, and writes results into a retrieved-corpus store annotated as the only thing drafting may draw on. Its output passes to a citation-verification gate carrying a reviewer icon marking it as a separate step from the drafter, annotated with its three tests: the work exists, the passage is really in it, and the passage supports the claim. Failing citations return to the agent; passing ones reach a human interpret-and-decide step. A note on the gate warns that a run in which nothing fails is evidence the check is broken, not that the corpus was clean.
- infographic description: A flat vector architecture diagram on an off-white background,
                 16:9. Title top-left: "Retrieval-grounded synthesis, with the gate that
                 makes it safe". Standfirst beneath: "The model writes only about documents
                 that were actually fetched, and a separate step checks every one." At left,
                 a small blue tag "specification" connects rightward into a medium
                 orange-bordered rounded rectangle "retrieval and drafting agent" containing
                 an orange box "LLM" and a circular loop arrow "plan – act – observe". Two
                 green wrench icons "bibliographic search" and "web search" connect to the
                 agent, sharing the annotation "several vocabularies on purpose — the
                 terminology is unsettled". A sky-blue cylinder "retrieved corpus" sits
                 below the agent with a bidirectional arrow and the note "drafting may draw
                 on this and nothing else". From the agent's right edge an arrow leads to a
                 vermillion diamond "citation-verification gate" carrying a small purple
                 reviewer head-and-shoulders-with-tick icon annotated "a separate step, not
                 the agent that wrote the draft", with a callout listing "three tests: the
                 work exists · the passage is really in it · the passage supports the
                 claim". The diamond has a "fail" arrow curving back to the agent annotated
                 "removed or returned for correction", and a "pass" arrow to a blue
                 head-and-shoulders icon "interpret and decide" annotated "decides what the
                 evidence means". Beneath the gate, in a pale yellow fill, a note: "a run
                 where nothing fails is evidence the check is broken, not that the corpus
                 was clean". Single-weight lines, generous spacing, sentence case.
```

## Figure 5.3 — Corpus and gate yield

```
FIGURE BRIEF
- id:            Figure 5.3
- title:         From retrieved corpus to interpreted synthesis
- type:          sequence
- claim:         A defensible synthesis is a funnel in which the citation-verification gate visibly removes claims, and a gate that removes none is not evidence of a clean corpus but of an untested check.
- standfirst:    The width lost at the gate is what makes what survives worth trusting.
- canvas:        16:9
- elements:      a vertical top-to-bottom funnel of five labelled stages, each a horizontal
                 bar whose width is a placeholder to be set from the author's real counts:
                 "retrieved" (sky blue), "after triage" (sky blue), "claims drafted with
                 citations" (orange), "claims surviving the gate" (vermillion outline), and
                 a final blue bar "interpreted by the scientist"; each transition annotated
                 with a count placeholder
- flow:          top-to-bottom, each bar narrower than the one above
- labels:        "retrieved", "after triage", "claims drafted with citations",
                 "claims surviving the gate", "interpreted by the scientist",
                 "n = [AUTHOR]" beside each transition
- annotations:   on the triage transition, "documents that do not bear on the question";
                 on the drafting transition, "every claim now carries a citation into the
                 corpus"; on the gate transition, in vermillion, "removed: fails exists /
                 passage present / claim supported"; on the final transition, "a named
                 person decides what the surviving evidence means"; a callout beside the
                 gate transition, "the width lost here is the point — a gate that removes
                 nothing has not been shown to work"; a footnote, "counts are the author's
                 to supply — placeholders shown"
- caption:       Figure 5.3 — A synthesis is a funnel, and the interesting part is what it drops. Documents fall away at triage, and claims fall away at the gate for failing one of its three tests. The counts here are placeholders for real ones, but the shape is the argument: a gate that removes nothing has not been shown to work. The width lost at that step is what makes the rest trustworthy.
- alt-text:      A top-to-bottom funnel of five narrowing bars: retrieved, after triage, claims drafted with citations, claims surviving the gate, and interpreted by the scientist. Each transition carries a count marked as the author's to supply. The triage step is annotated as where irrelevant documents go, the gate step as where claims are removed for failing one of three tests, existence, passage present or claim supported, and the final step as where a named person decides what the surviving evidence means. A callout beside the gate transition reads that the width lost there is the figure's point, and that a gate removing nothing has not been shown to work.
- infographic description: A flat vector funnel diagram on an off-white background, 16:9.
                 Title top-left: "From retrieved corpus to interpreted synthesis".
                 Standfirst beneath: "The width lost at the gate is what makes what survives
                 worth trusting." Five horizontal bars stacked top to bottom, each narrower
                 than the one above, centre-aligned. From the top: a sky-blue bar
                 "retrieved"; a sky-blue bar "after triage"; an orange bar "claims drafted
                 with citations"; a vermillion-outlined bar "claims surviving the gate"; a
                 blue bar "interpreted by the scientist". Beside each transition, small
                 near-black text "n = [AUTHOR]" and an annotation: after retrieved,
                 "documents that do not bear on the question"; after triage, "every claim
                 now carries a citation into the corpus"; at the gate, in vermillion,
                 "removed: fails exists / passage present / claim supported"; at the last,
                 "a named person decides what the surviving evidence means". A callout in a
                 pale yellow fill beside the gate transition reads "the width lost here is
                 the point — a gate that removes nothing has not been shown to work". A
                 light grey footnote at the side reads "counts are the author's to supply —
                 placeholders shown". Single-weight lines, generous spacing, sentence case.
```
