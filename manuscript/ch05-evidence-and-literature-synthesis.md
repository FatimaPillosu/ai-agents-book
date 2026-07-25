# Chapter 5 — Evidence and literature synthesis

> **Status:** draft r3 · voice v3.3 (`STYLE.md`) · sentence-per-line per `STYLE.md` §10 · figures as briefs per `FIGURES.md`.
> **Conventions:** vendor-neutral (outline §9) · **[AUTHOR: …]** marks lived material only the author can supply · **[verify]** marks real but unconfirmed details · citations drawn only from verified reports in `/research`. Nothing has been invented.
> **Chapter note:** no literature has been invented for the worked example — the actual corpus and every named work are left as **[AUTHOR: …]** or **[verify]** for the author to supply and check.

---

## 5.1 The problem this chapter addresses

Establishing what is already known about a question has become a bottleneck out of all proportion to its intellectual weight, and practitioners across the environmental and geosciences have almost certainly felt it.
The published record grows faster than any one person can track: the annual output of peer-reviewed articles across our fields keeps rising, and anyone entering an unfamiliar sub-field now has to reconcile hundreds of candidate papers, preprints, technical reports and dataset descriptors before writing a single sentence of original synthesis **[AUTHOR: verify one defensible figure — e.g. annual growth rate of publications in a relevant field such as hydrology or remote sensing, 2015–2025 — and cite]**.
What makes this different from ordinary summarising is the obligation attached to the record.
Every claim carried forward has to be traceable to a specific, retrievable source that genuinely supports it, because the synthesis becomes the foundation on which later design, modelling and interpretation rest.
The bottleneck is acute, rather than merely tedious, because volume collides with that traceability requirement: the reading can in principle be delegated, but the accountability for what the reading concluded cannot.
The result, visible across the field though no clean measurement of it is known to this book, is that a large share of a project's opening weeks goes on retrieval, triage and note-keeping, skilled work that nonetheless sits upstream of the science actually intended, and that scales badly as a field broadens.
This book puts literature synthesis first among its five core patterns because it shows, in unusually clean form, the property that governs every later pattern: gathering and drafting are cheap to delegate and expensive to trust, and the whole design problem is how to move the cheap part to an agent whilst keeping the expensive part under a scientist's control (high confidence).

## 5.2 The conventional workflow

The established way to synthesise a literature runs through a sequence of manual stages whose weaknesses are familiar to anyone who has finished one under deadline.
The work begins with keyword searches across bibliographic databases and a general web search, screens titles and abstracts down to a shortlist, reads the shortlist whilst taking notes, and then writes a narrative that organises the sources into an account of what is known, contested and unresolved.
Two properties of this process bear directly on the redesign that follows.
The first is that its quality depends heavily on how complete the initial retrieval was, and retrieval is where the process most often fails silently: a synthesis can be internally impeccable and still rest on a corpus that missed an entire methodological camp because the searcher did not know its vocabulary, a gap neither the author nor a casual reader can detect from the finished text (high confidence).
The second is that the labour does not spread evenly across the stages.
Retrieval and triage eat time out of all proportion to their intellectual content, whilst the interpretive act (deciding what the assembled evidence actually implies, where positions genuinely conflict, and which findings are robust rather than merely often repeated) is comparatively quick once the material is in view, and it is the part that draws on the scientist's trained judgement.
There is now direct evidence for this uneven split: in a 2025 study of an end-to-end language-model workflow for systematic reviews, automated screening of studies reached a sensitivity of about 97% against roughly 82% for the conventional dual-reviewer process, and data-extraction accuracy likewise exceeded the human baseline (Cao et al., 2025), strong evidence that machines can match or exceed human performance on the mechanical layers, even as the interpretive layers stayed human.
That result should be carried cautiously: it is a preprint, drawn from the highly structured clinical literature, and it may not transfer cleanly to the heterogeneous environmental literatures of this field (moderate confidence).
Systematic-review methodologies exist precisely to discipline the front stages, imposing pre-registered search strings, inclusion criteria and dual screening so the corpus is defensible and the process reproducible **[verify: reference a standard systematic-review or evidence-synthesis guideline appropriate to environmental science]**.
Those methods buy rigour at a large cost in time, and most working syntheses (the literature section of a paper, the state-of-the-art survey that opens a proposal) are done informally, inheriting the silent-gap weakness without the protection the formal methods give.
The redesign in this chapter aims to keep the interpretive act firmly with the scientist whilst giving the front stages both the speed of automation and, through an explicit verification gate, a defence against the failure modes that make automating this task hazardous.

**Figure 5.1 — Conventional versus agentic synthesis.** *A figure brief follows `FIGURES.md`; render in the house style.*

```
FIGURE BRIEF
- id:            Figure 5.1
- title:         Where the labour sits — manual synthesis versus a governed agentic redesign
- type:          before/after
- claim:         The agentic redesign moves retrieval, triage and drafting to an agent and inserts a citation-verification gate, while the interpretive act stays with the scientist in both workflows.
- canvas:        16:9
- elements:      top row (conventional) — human icon (blue) performing four sequential stages "search", "triage", "read and note", "draft", ending at a human "interpret" (blue); bottom row (agentic) — a "specification" tag (blue) feeding an agent (orange) that performs "retrieve", "triage", "draft" against a data store (sky blue), then a vermillion diamond "citation-verification gate", then a human "interpret and decide" (blue); the interpret step is aligned vertically across both rows to show it is unchanged
- flow:          left-to-right in both rows; the two rows share the same horizontal stage positions so the difference is legible by column
- labels:        "conventional", "search", "triage", "read and note", "draft", "interpret",
                 "agentic", "specification", "retrieve", "triage", "draft", "corpus",
                 "citation-verification gate", "interpret and decide"
- annotations:   a light bracket over the conventional "search/triage/read" stages labelled "time-dominant, silent gaps"; a callout on the gate labelled "every claim traced to a retrievable source"
- caption:       Figure 5.1 — The conventional synthesis (top) and its agentic redesign (bottom), drawn on a shared grid. The agent absorbs retrieval, triage and drafting; a verification gate defends the corpus against fabricated or mis-attributed citations; the interpretive decision, aligned across both rows, remains the scientist's.
- alt-text:      A two-row before/after diagram. The top row shows a person moving through search, triage, reading and drafting to an interpret step. The bottom row shows a specification feeding an agent that retrieves, triages and drafts against a corpus store, then passes through a citation-verification gate before reaching the same human interpret-and-decide step, which is aligned vertically with the top row to show it is unchanged.
- generator prompt: A flat vector before/after workflow diagram in two horizontal rows on an off-white background, sharing aligned column positions. Top row labelled "conventional": a blue head-and-shoulders icon followed by four near-black boxes "search", "triage", "read and note", "draft", ending in a blue box "interpret". A thin bracket over the first three boxes reads "time-dominant, silent gaps". Bottom row labelled "agentic": a small blue tag "specification" feeds an orange rounded rectangle "agent" containing "retrieve", "triage", "draft", linked downward to a sky-blue cylinder "corpus"; an arrow leads right to a vermillion diamond "citation-verification gate" with a small callout "every claim traced to a retrievable source", then to a blue box "interpret and decide" positioned directly below the top row's "interpret". Single-weight connectors, one arrowhead style, generous spacing, minimal text.
```

## 5.3 The agentic redesign

The redesign swaps the manual front stages for a governed pipeline whose defining feature is simple to state: no claim reaches the scientist without a verified anchor in a retrievable source.
The pipeline has four stages, and the discipline is in keeping them separate rather than collapsing them into one conversational request.
The first stage is retrieval: an agent expands the question into a set of search strategies, queries bibliographic and web sources through defined tools, and assembles a corpus of candidate documents into a store that persists for the rest of the task.
The second stage is grounded drafting: the agent composes synthesis text under a hard constraint, which is that every substantive sentence must cite one or more documents drawn from the retrieved corpus, and may draw only on their retrieved content rather than on the model's trained-in memory of the field.
This constraint, retrieval-grounded generation, is the single most important design choice in the pattern, because it turns the dominant failure mode of a bare language model, the confident production of plausible but non-existent references, from an ever-present hazard into something a downstream check can actually catch (high confidence that grounding reduces fabrication; the residual rate is model- and configuration-dependent and must be measured, per Chapter 11).
The idea is not new to this book: an agentic retrieval-augmented system reported in 2023 decomposed literature question-answering into search, evidence-gathering and answer-composition steps, scored retrieved passages for relevance, and tied each answer to its retrieved sources precisely to reduce hallucination and supply provenance (Lála et al., 2023).
What the book adds is the governance around that idea (the gate, the human interpreter, the explicit retrieval discipline) rather than the grounding mechanism itself.

> **Definition — Retrieval grounding.** A constraint under which the model does not answer from its own trained-in memory of the literature but from real documents fetched first, with every sentence it writes required to rest only on those fetched documents. The model still does the writing, but about texts placed before it rather than half-remembered ones. This is what later allows a check to trace each claim back to a source that genuinely exists.

The third stage is the citation-verification gate, the component that makes the pattern safe enough to use.
It is an independent step, external to the agent that drafted the text, that takes every citation and every claim attached to it and confirms three things: that the cited work exists and is retrievable, that the passage attributed to it is actually present, and that the claim the draft rests on the passage is one the passage supports.
Citations that fail any of the three are removed or returned for correction; the gate is a barrier, not an advisory.

> **Definition — Citation-verification gate.** A checkpoint every citation must pass before the draft is allowed forward. A separate step, not the agent that wrote the draft, confirms that each cited work exists, that the quoted passage is really in it, and that the passage actually supports the claim made on it. Citations that fail are removed or returned; nothing proceeds merely because it reads well.

The gate's residual risk turns on its design, which 2026 work now measures.
A preprint that year, testing machine-drafted citations across four scientific domains, found only 50.9% of entries fully correct even where 83.6% of individual fields were right, whilst a two-stage design (draft a citation, then resolve it deterministically against bibliographic services) lifted fully correct entries to 78.3% and cut tool-introduced errors to 0.8%, from 4.8% for a one-stage integration (Rao and Callison-Burch, 2026).
[ai-reviewer: this two-sentence insertion stands as its own paragraph, well below STYLE.md §2's developed-paragraph span, and R2's G6 asked for new evidence to be attached to the existing argument rather than left free-standing. The fix is to integrate it into the adjoining gate paragraph (§5.3) so the claim–evidence flow is continuous. The same stub-paragraph pattern recurs in the R2 additions at ch08 §8.5 (the WP-MIP paragraph plus its two-sentence coda) and ch09 §9.4 (the two closing 2026-evidence paragraphs) — worth one harmonising pass by ai-writer.]

The fourth stage is human interpretation, and it is deliberately the stage the pipeline does not automate.
The scientist reads the verified, grounded draft and performs the interpretive act: weighing the strength of the evidence, resolving where sources genuinely conflict, telling robust findings from often-repeated ones, and deciding what the assembled record implies for the question that started the search.
The division of responsibility is the whole point of the design.
The agent is allowed to gather and to draft, both cheap-to-produce and expensive-to-trust activities, precisely because a verification gate and a human interpreter stand between its output and any use the synthesis is put to (high confidence in the pattern).

**Figure 5.2 — The retrieval-grounded synthesis pipeline.** *A figure brief follows `FIGURES.md`; render in the house style.*

```
FIGURE BRIEF
- id:            Figure 5.2
- title:         Retrieval-grounded synthesis with a citation-verification gate
- type:          architecture
- claim:         Grounded drafting and an independent citation-verification gate together confine the fabricated-citation failure mode, leaving interpretation to the human.
- canvas:        16:9
- elements:      a "specification" tag (blue) at left; an agent (orange) labelled "retrieval and drafting agent" containing an "LLM" box (orange) and a "plan–act–observe" loop; retrieval tools (green) labelled "bibliographic search" and "web search"; a data store (sky blue) labelled "retrieved corpus"; a separate agent or check (orange border, vermillion gate glyph) labelled "citation-verification gate" with a smaller reviewer icon (purple) attached to denote independence; a human "interpret and decide" icon (blue) at right
- flow:          left-to-right: specification → retrieval/drafting agent (which calls the green search tools and writes to the sky-blue corpus, then reads from it to draft) → citation-verification gate → human; the gate has a "fail" return arrow back to the drafting agent and a "pass" arrow forward to the human
- labels:        "specification", "retrieval and drafting agent", "LLM",
                 "plan – act – observe", "bibliographic search", "web search",
                 "retrieved corpus", "citation-verification gate", "pass", "fail",
                 "interpret and decide"
- annotations:   a callout on the gate reading "exists · passage present · claim supported"; a small note under the corpus reading "drafting draws only from here"
- caption:       Figure 5.2 — The pattern's architecture. Retrieval populates a persistent corpus; drafting is constrained to that corpus; an independent gate checks that every citation exists, that the cited passage is present, and that it supports the claim; only then does the verified draft reach the scientist for interpretation.
- alt-text:      An architecture diagram. A specification feeds a retrieval-and-drafting agent containing a language model and a plan–act–observe loop. The agent calls bibliographic-search and web-search tools and writes results into a retrieved-corpus store, then drafts using only that store. Its output passes to a citation-verification gate, annotated with the three checks exists, passage present and claim supported; failing citations return to the agent, passing ones proceed to a human interpret-and-decide step.
- generator prompt: A flat vector architecture diagram on an off-white background. At left, a small blue tag "specification" connects rightward into a medium orange-bordered rounded rectangle "retrieval and drafting agent" containing an orange box "LLM" and a circular loop arrow "plan – act – observe". Two green wrench icons labelled "bibliographic search" and "web search" connect to the agent. A sky-blue cylinder "retrieved corpus" sits below the agent with a bidirectional arrow and a small note "drafting draws only from here". From the agent's right edge an arrow leads to a vermillion diamond "citation-verification gate" carrying a small purple reviewer head-and-shoulders-with-tick icon and a callout "exists · passage present · claim supported". The diamond has a "fail" arrow curving back to the agent and a "pass" arrow to a blue head-and-shoulders icon "interpret and decide". Single-weight lines, one arrowhead style, generous spacing, minimal text.
```

## 5.4 Worked example: a frontier synthesis of the agentic-AI-in-hydrology literature

This chapter makes the pattern concrete through a synthesis of the emerging literature on agentic AI in hydrology, described here as a method rather than as a set of findings: the findings belong to the author's own corpus and are marked below as author-supplied.
The question put to the pipeline was bounded deliberately: what applications of agent-based and agentic language-model systems to hydrological problems have been reported, with what claimed benefits, and with what evidence for those claims **[AUTHOR: state the exact question and scope as posed, including the date range and any inclusion criteria used]**.
Retrieval ran from a set of search strategies covering the several vocabularies under which such work appears (the terminology is unsettled, and a single keyword set would simply have reproduced the silent-gap failure of §5.2) and assembled a corpus whose size and composition are the author's to report **[AUTHOR: give the number of documents retrieved, the sources queried, and the number surviving triage]**.
Grounded drafting then produced a synthesis organised by application area, with every claim carrying a citation into the corpus, and the citation-verification gate ran over the draft before any of it was read.

The gate's yield is the most instructive part of the exercise, and it is exactly the material only the author can supply: how many citations were checked, how many failed each of the three tests, and how many claims survived to the interpreted synthesis **[AUTHOR: report the citation-verification statistics — citations checked, number failing the existence test, number failing the passage-present test, number failing the claim-supported test]**.
Two observations about method hold regardless of those numbers.
The first is that the gate's value is measured precisely by its non-zero failure count: a run in which no citation is removed gives no evidence that the gate is working, and the discipline requires treating the check itself as something to be evaluated (moderate-to-high confidence; the argument is developed in Chapter 11).
The second is that the interpretive conclusions (which application areas rest on demonstrated operational value rather than proof-of-concept, and where the loudest claims are thinnest in evidence) were reached by the author reading the verified draft, not delegated to the agent, and they stand under the author's name and judgement **[AUTHOR: state the synthesis's principal interpretive conclusions in your own words, and identify any works you regard as load-bearing, marking each citation for verification]**.
Presented this way, the example demonstrates the pattern without asserting any result the draft cannot itself substantiate: the method is reproducible and set out in full, whilst the corpus, the gate's yield and the interpretation are held as author-supplied, so nothing here stands unless the author's own materials support it.
No paper, author or finding is named in this draft, in keeping with the rule that literature is never invented to illustrate a method, a design choice stated plainly so that the absence of citations here is not mistaken for an absence of evidence in the actual synthesis.

**Figure 5.3 — Corpus and gate yield.** *A figure brief follows `FIGURES.md`; render in the house style.*

```
FIGURE BRIEF
- id:            Figure 5.3
- title:         From retrieved corpus to interpreted synthesis — where documents and claims are lost
- type:          sequence
- claim:         A defensible synthesis is a funnel in which the citation-verification gate visibly removes claims, and a gate that removes none is not evidence of a clean corpus but of an untested check.
- canvas:        16:9
- elements:      a vertical top-to-bottom funnel of four labelled stages, each a horizontal bar whose width is a placeholder to be set from the author's real counts: "retrieved" (sky blue), "after triage" (sky blue), "claims drafted with citations" (orange), "claims surviving the gate" (vermillion outline), leading to a final blue bar "interpreted by the scientist"; each transition annotated with a count placeholder
- flow:          top-to-bottom, each bar narrower than the one above
- labels:        "retrieved", "after triage", "claims drafted with citations",
                 "claims surviving the gate", "interpreted by the scientist",
                 "n = [AUTHOR]" beside each transition
- annotations:   a vermillion callout at the gate transition reading "removed: fails exists / passage / support"; a light note "counts are the author's to supply — placeholders shown"
- caption:       Figure 5.3 — The synthesis as a funnel from retrieved documents to interpreted claims. The counts are placeholders to be replaced with the author's real figures; the figure's point is structural: the gate removes claims visibly, and its non-zero yield is what makes the surviving synthesis trustworthy.
- alt-text:      A top-to-bottom funnel of five narrowing horizontal bars labelled retrieved, after triage, claims drafted with citations, claims surviving the gate, and interpreted by the scientist. Each transition carries a count placeholder marked as author-supplied. A callout at the gate step notes that removed claims failed the existence, passage-present or claim-supported test.
- generator prompt: A flat vector funnel diagram on an off-white background, five horizontal bars stacked top to bottom, each narrower than the one above, centre-aligned. From top: a sky-blue bar "retrieved", a sky-blue bar "after triage", an orange bar "claims drafted with citations", a vermillion-outlined bar "claims surviving the gate", and a blue bar "interpreted by the scientist". Beside each transition, small near-black text "n = [AUTHOR]". A vermillion callout at the fourth transition reads "removed: fails exists / passage / support". A light grey note at the side reads "counts are the author's to supply — placeholders shown". Single-weight lines, generous spacing, minimal text.
```

## 5.5 Failure modes

The synthesis pattern has three characteristic failure modes, and naming them precisely is what allows the verification gate to be designed against them rather than against a vague sense of risk.
The first and most consequential is the fabricated or mis-attributed citation, the failure this chapter is built around and the one Chapter 13 anatomises at length.
A bare language model asked for supporting references will, at a rate that is far from negligible, produce citations that are formatted immaculately and do not exist, or that exist but do not contain the claim attributed to them.
The scale is documented: in a 2023 study, citations generated by that model generation without retrieval were wholly fabricated somewhere between roughly a fifth and over half of the time depending on the model, and even the genuine ones frequently carried the wrong volume, issue, pages or date (Walters and Wilder, 2023); a 2025 replication across a wider set of assistants found roughly two-fifths of requested references still erroneous or invented, so this is not a solved 2023-era problem but a persistent, structural one (Cabezas-Clavijo and Sidorenko-Bautista, 2025).
The benchmark of §5.3 also found accuracy falling 27.7 percentage points for recent papers against well-known ones, the models leaning on memorised knowledge even with search tools available, so retrieval access does not guarantee retrieval use (Rao and Callison-Burch, 2026).
The two variants are distinct, and the gate must catch both, because a real paper wrongly cited is more insidious than an invented one: it survives a naive existence check; in the standard taxonomy of model hallucination the first is a factual fabrication and the second a faithfulness failure, and the two need different tests (Huang et al., 2023) (high confidence that both variants occur; rates are model- and prompt-dependent and are the proper subject of the evaluation in Chapter 11).
Fabricated citations survive even elite peer review: a 2026 preprint found 100 fabricated citations across 53 papers accepted at a top machine-learning venue in 2025, about 1% of that year's accepted papers, one or two per paper, small enough for three to five expert readers to miss (Ansari, 2026), which is exactly why the check must be mechanical and tool-executed rather than a plausibility read.
The second failure mode is the plausible-but-wrong synthesis, in which every individual citation is genuine and correctly attributed yet the overall account misrepresents the field: generalising from a few sources to a settled consensus that does not exist, inheriting the framing of the most-cited papers rather than weighing the evidence afresh, or presenting contested findings as established.
This one is more dangerous than fabrication precisely because it passes the citation gate: the anchors are all real, and only a scientist reading the verified draft against their own knowledge of the field can catch it, an instance of the plausible-failure property of Chapter 1, where fluency and correctness come apart, and one of the reasons the interpretive stage is not automated and cannot be (high confidence).
The third failure mode is the coverage gap, the silent-retrieval failure of §5.2 returning in agentic form: the synthesis is grounded, verified and interpretively sound with respect to the corpus it was given, and the corpus omitted a body of work the agent's search strategies never reached.
Coverage gaps are the hardest of the three to detect from the finished text, because a synthesis carries no visible trace of what it did not retrieve, and the only reliable defences are procedural: diversifying search vocabularies on purpose, cross-checking the corpus against a small set of known-relevant papers held back for exactly this, and treating an unexpectedly clean or one-sided result as a reason to interrogate retrieval rather than as a finding **[AUTHOR: a coverage gap you have been caught by, or nearly caught by, in your own work — the camp of literature a first search missed, and how you found it]** (moderate confidence in the mitigations; their adequacy is field-dependent and should be reported alongside the synthesis).
The three failures form a natural order of subtlety (fabrication is caught by the gate, plausible-but-wrong synthesis by the human interpreter, and coverage gaps only by procedure, and never fully), and that ordering is why the pattern puts a mechanical gate, a human interpreter and an explicit retrieval discipline in series rather than trusting any one of them.

## 5.6 Verification checklist

This checklist certifies that a literature synthesis is safe to sign, and it is written to be applied by a colleague who did not run the pipeline (a reviewer, not the drafting agent) and to be usable in print, away from the chapter.

- **Corpus.** Are the search strategies and sources recorded, and does the corpus survive a cross-check against a held-back set of known-relevant papers, so a coverage gap would be visible (§5.5)?
- **Grounding.** Is every substantive claim in the draft attached to at least one citation drawn from the retrieved corpus, rather than to the model's unsourced recall (§5.3)?
- **Existence.** Has every cited work been confirmed to exist and be retrievable through an independent check, not merely to be plausibly formatted?
- **Passage.** For each citation, has the specific passage relied upon been located in the cited work?
- **Support.** Does that passage actually support the claim the draft rests on it, as judged by a check external to the agent that drafted the text?
- **Independence.** Was the verification performed by a component separate from the drafting agent, so a single failure does not both generate and approve an error? This is the principle that a check must be external to the thing it checks, introduced in Chapter 1 and measured in Chapter 11.
- **Interpretation.** Were the synthesis's conclusions reached by a named scientist reading the verified draft, and are contested or thinly evidenced claims marked as such rather than smoothed into apparent consensus?
- **Yield.** Is the gate's failure count non-zero, or is there positive evidence that the check itself functions? A clean gate result is a reason for suspicion, not reassurance: treat a check that never fires as evidence it is broken, not proof the corpus was flawless (high confidence).

A synthesis that cannot answer these eight questions is not yet one a scientist should sign.

## 5.7 Repository pointer

The companion repository holds the runnable and perishable counterparts to this chapter, under `/patterns/ch05-literature-synthesis`, `/prompts` and `/checklists`.
The runnable material is a minimal retrieval-grounded synthesis workflow with the citation-verification gate implemented as a separate step, written to be adapted rather than run as-is, together with the specification schema of Chapter 3 instantiated for a synthesis task.
The prompts directory carries the drafting and verification prompts in the form used here, and the checklists directory carries §5.6 as a one-page printable.
Named tools, current model capabilities and any volatile figures stay in the repository, per the book's vendor-neutral convention, so the print chapter states the pattern and its reasoning whilst the repository tracks the parts that date **[AUTHOR: confirm the repository paths and the contents once the runnable example is finalised; list any dataset or bibliographic-source access requirements]**.
The evaluation of the gate itself (how to measure its false-negative rate, and how much verification a given synthesis warrants) is developed in Chapter 11; the fabricated-citation failure mode is dissected with annotated traces in Chapter 13; and the use of a verified synthesis in the writing of a manuscript, where disclosure and authorship obligations attach, is the subject of Chapter 9.

## References

Ansari, M.S. (2026). *Compound Deception in Elite Peer Review: A Failure Mode Taxonomy of 100 Fabricated Citations at NeurIPS 2025.* arXiv preprint arXiv:2602.05930. [preprint — not yet peer-reviewed]

Cabezas-Clavijo, Á. and Sidorenko-Bautista, P. (2025). *Assessing the performance of 8 AI chatbots in bibliographic reference retrieval: Grok and DeepSeek outperform ChatGPT, but none are fully accurate.* arXiv preprint arXiv:2505.18059. [verify final publication — Journal of Data and Information Science, 2026]

Cao, C., Arora, R., Cento, P. et al. (2025). *Automation of Systematic Reviews with Large Language Models.* medRxiv preprint. DOI: 10.1101/2025.06.13.25329541. [preprint — verify peer-reviewed venue before release]

Huang, L., Yu, W. et al. (2023). *A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions.* arXiv preprint arXiv:2311.05232. [verify DOI of ACM Transactions on Information Systems journal version, 2025]

Lála, J., O'Donoghue, O., Shtedritski, A., Cox, S., Rodriques, S.G. and White, A.D. (2023). *PaperQA: Retrieval-Augmented Generative Agent for Scientific Research.* arXiv preprint arXiv:2312.07559.

Rao, D. and Callison-Burch, C. (2026). *BibTeX Citation Hallucinations in Scientific Publishing Agents: Evaluation and Mitigation.* arXiv preprint arXiv:2604.03159. [preprint — not yet peer-reviewed]

Walters, W.H. and Wilder, E.I. (2023). *Fabrication and errors in the bibliographic citations generated by ChatGPT.* Scientific Reports, 13, 14045. DOI: 10.1038/s41598-023-41032-5.
