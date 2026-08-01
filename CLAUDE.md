# CLAUDE.md — Agentic AI for Environmental Science (book project)

Project instructions for any agent working in this repository. Read fully before acting. `STYLE.md` (the author writing-style guide) is binding for all prose; `FIGURES.md` is binding for all figures.

## What this project is

A single ~150-page e-book on agentic AI for practising environmental and geoscientists, self-published and **released free via LinkedIn**. The goal is author credibility on agentic-AI work, not revenue. It is a **living book**: versioned releases built from this repository, which holds the canonical Markdown source; each release is announced and excerpted through the author's LinkedIn newsletter. Licence, DOI and output format are deferred decisions, not open gates.

The book is **pattern-based, governance-first and diagram-led**: durable workflow patterns rather than named tools, an identical anatomy for every core chapter, worked examples from executed operational hydrology and meteorology, and verification treated as the centre of gravity. Its positioning claim — no existing practical, governance-first treatment for environmental researchers — rests on a limited scan (Jul 2026) and is to be re-verified nearer release.

## Current state (1 Aug 2026)

- Outline **v0.7** (`manuscript/OUTLINE.md`) is authoritative: 18 chapters in 5 parts, the eighteen-chapter structure itself still **[PROPOSED]** and awaiting the author (outline §9). Budgets indicative (≈150 pp / 38,000–42,000 words / 65–75 figures), not fixed targets; the drafted book sits at ≈176 indicative pages and 54 figures. Per-chapter allocations in outline §7 are guidance.
- **Style guide** (`STYLE.md`, **v5.0** — the colloquial register: written to one intelligent colleague, reader addressed as "you", contractions used lightly, 80–200-word single-point paragraphs, no sentence announcing what the text is about to do, the concrete case leading, ~30-word sentence ceiling, no metaphors, quantified evidence with baselines, calibrated hedging, no em-dash connectors; info-boxes; sentence-per-line) and **figure guide** (`FIGURES.md`, **v2.1**) are in place and binding. **STYLE.md applies retroactively to all chapters.** The whole manuscript (then ch00–ch17, eighteen files) was converted to this register on the author's instruction (26 Jul 2026), superseding the v3.x academic lineage; the v3.4 academic version of the manuscript is preserved on branch `claude/manuscript-feedback-e2xcop` and in this file's history. `manuscript/CH01-STYLE-PASS.md` is superseded. **Figure captions and `FIGURES.md` were converted to the colloquial register on 26 Jul 2026**, and the 51 captions then in the book were brought under the v5.0 sentence ceiling on 30 Jul 2026 (branch `claude/figure-captions-9s1me9`), four of them keeping a sentence above 30 words as parallel semicolon enumerations permitted by `STYLE.md` §11. Pass A1 added three captions and re-briefed one, so **six of the 54 captions now carry a sentence above 30 words** (Figures 1.2, 6.4, 11.1, 14.1, 14.2 and 17.2; re-counted 1 Aug 2026). **Alt-text is in the colloquial register but has not had the ceiling pass**: 45 of the 54 alt-texts still carry at least one sentence over 30 words. `FIGURES.md` v2.1 §6 now states that the ceiling binds captions and alt-text alike, so that backlog is scheduled rework, recorded in `manuscript/ADVERSARIAL-INTEGRATION-PLAN.md` §11.
- All 18 chapters (`ch01`–`ch18`) plus the front matter (`ch00`) are drafted in `/manuscript`, nineteen files in all, and carry `[AUTHOR: …]` markers for lived/executed material. **Revision pass R1 is complete and closed** (`manuscript/REVISION-PLAN.md`). **Research-integration pass R2 is complete and closed** (`manuscript/RESEARCH-INTEGRATION-PLAN.md`): the two later `/research` reports woven, superseded citations corrected, `FURTHER-READING.md` refreshed. **Adversarial-review integration A1 is executed and reviewed** on branch `adversarial-analysis`, governed by `manuscript/ADVERSARIAL-INTEGRATION-PLAN.md`: one new chapter (Ch. 17), five new sections, a six-tier evidential ladder in Ch. 11, three new figures and one re-brief. Four structural items in it are **[PROPOSED]** and await the author (outline §9); nothing in A1 alters a decided item.
- Agent roster: ai-editor (plan and admin documents), ai-writer (prose and figure briefs), ai-reviewer (independent review), and **ai-researcher** (web-research sweeps; verified research reports in `/research` at the repo root, with DOIs/URLs per source). Manuscript citations are drawn only from those reports.

## How we get there

1. **Source format**: plain Markdown only. No build system, layout or output format is fixed — deferred decisions. Do not introduce a toolchain.
2. **Per-chapter loop**: draft → self-check against `STYLE.md` §7 checklist → independent review pass (reviewer role, not the drafting agent) → author revision → figure briefs per `FIGURES.md` → consistency check against the outline and cross-references.
3. **Chapter anatomy (Part II)**: problem → conventional workflow → agentic redesign → worked example → failure modes → verification checklist → repository pointer. Standard figure set: one architecture, one sequence, one before/after, one or two example figures. The full anatomy binds Part II only; Ch. 11 and Ch. 12 (Part III) do not follow it but each still carries a verification checklist and a repository pointer.
4. **Figures**: every figure is a brief following `FIGURES.md`, in the house infographic style; alt-text written with the brief, never retrofitted.

## Repository layout (target)

`/manuscript` (Markdown source: `ch00`–`ch18`; `OUTLINE.md`; `GLOSSARY.md`; `FURTHER-READING.md`; and the pass plans `REVISION-PLAN.md`, `RESEARCH-INTEGRATION-PLAN.md`, `ADVERSARIAL-REVIEW.md`, `ADVERSARIAL-INTEGRATION-PLAN.md`) · **`/fig-brief` (the figure briefs, one file per chapter, `chNN-slug.md`, each brief under its own `## Figure N.M — …` heading)** · `/figures` (rendered SVGs) and `/figures-src` (the house renderer) · `/research` (ai-researcher's verified research reports; the sole source of manuscript citations) · `/patterns` (runnable minimal examples) · `/prompts` · `/checklists` · `/case-studies` (sanitised configurations) · `/exercises`. Captions and alt-text live with the figure in the chapter file, not in the brief directory, and the brief's matching fields are changed in the same edit (`FIGURES.md` §6). Version by tags and history; do not carry filename suffixes like `-v0.2` — the chapter file is `chNN-slug.md` and its draft status lives in a header line.

## Hard rules for agents

- **Never fabricate** facts, quotes, statistics, anecdotes or references. Cite only sources verified as real; flag incomplete bibliographic details with **[verify]**.
- **Citations come from `/research` only.** Manuscript citations are drawn from the verified research reports in `/research` (compiled by ai-researcher, with a DOI or URL per source) — never from an agent's memory. A claim that needs a citation no report yet covers keeps a **[verify]** flag rather than acquiring an unverified reference.
- **Never resolve [AUTHOR: …] markers.** They denote lived material or decisions only the author can supply. Leave them intact; add new ones where such material is needed.
- **Never alter DECIDED items** (outline §9) without explicit author instruction. Deferred items may be noted but are not gates; do not raise them as blockers.
- **Budgets are indicative guidance**, not hard limits: keep the book roughly in proportion, but a chapter may run over or under where the material justifies it. Avoid unjustified bloat.
- **Vendor-neutral in manuscript prose**: capability classes and approximate years in print; named products and volatile figures only under `/patterns`, `/prompts` and repository docs.
- Do not present designed-but-unexecuted work as accomplished (the digital-twin intercomparison is a worked design in Ch. 8, not a case study).
- **Label a constructed illustration as constructed.** The test: does the scenario carry specific quantities, dates or outcomes a reader could take as a record of something that happened? If it does and it did not happen, put the fixed label `*Constructed illustration.*` on its own line immediately before the opening sentence. Define it in that chapter's `> **Conventions:**` header line. `STYLE.md` §1 asks the concrete case to lead. This book above all others has to let a reader see, at the point of reading, whether a case is lived or assembled. An `[AUTHOR: …]` marker further down the section is a note to the author, not a signal to the reader (ai-editor ruling, 1 Aug 2026; sites in `manuscript/ADVERSARIAL-INTEGRATION-PLAN.md` §11.2).
- **Alt-text is written at figure creation**, never retrofitted; every figure follows `FIGURES.md`. British English everywhere, including captions, alt-text and repo docs.
- **Reflexive production**: the book is written under the governance it describes; substantive agent contributions per chapter feed the preface disclosure statement. (The formal audit-trail mechanism is deferred; a per-chapter status header suffices for now.)

## Decision log

**Decided:** single ~150 pp volume · audience: environmental/geosciences · self-published, free, LinkedIn-first · unified repository with newsletter as update channel · no formal index · specification (Ch. 3) and manuscripts (Ch. 9) chapters in · exercises live in `/exercises`, not the page budget · cross-domain examples deferred to a second edition · manuscript in plain Markdown · budgets indicative · vendor-neutral naming in print · figures governed by `FIGURES.md` · **STYLE.md voice applies retroactively to all chapters** (24 Jul 2026), register set to the **colloquial voice of STYLE.md v5.0** on the author's instruction (26 Jul 2026; supersedes the v3.x thesis-derived academic register, which itself superseded v2.0 "conversational" and v2.1 "plain-formal"): reader addressed as "you", contractions used lightly, 80–200-word single-point paragraphs, no sentence announcing what the text is about to do, the concrete case leading; **no metaphors anywhere** and a **~30-word sentence ceiling** (both v3.4, kept unchanged), no em-dash connectors, info-boxes and sentence-per-line retained; whole manuscript converted 26 Jul 2026 · **de-duplication now**: each recurring idea has one canonical home and short cross-references elsewhere (24 Jul 2026) · **references policy**: key claims cited from verified sources in the `/research` reports (ai-researcher, DOI/URL per source); annotated further reading in the back matter; no citation ever from agent memory (24 Jul 2026) · full chapter anatomy binds Part II only, with Ch. 11 and Ch. 12 still owing verification checklists and repository pointers (24 Jul 2026) · **figure briefs live in `fig-brief/`**: one file per chapter, `fig-brief/chNN-slug.md`, each brief under its own `## Figure N.M — …` heading; the chapter keeps the figure marker, the image with its alt-text, and the caption, whose render pointer names the brief file (author decision, 1 Aug 2026; supersedes both the earlier `/figures-source` intention and the inline-brief convention of `FIGURES.md` v2.0).

**Deferred (decide later; not gates):** output/layout format and build toolchain · licence · DOI/Zenodo · CI for runnable examples · reflexive-production audit-trail mechanism · positioning re-scan, beta readers and release-channel limit checks · **overall length reduction** — the manuscript stays at its current length for now; a future pass will consider cuts (author decision, 24 Jul 2026; de-duplication is decided and proceeds regardless).

**Open:** working title · **`STYLE.md` §12 contradicts §1**: the anti-pattern list bans addressing the reader as "you", which §1 requires. Two agents found it independently. `STYLE.md` is the author's voice guide, so the clause is the author's to delete or rewrite; no manuscript prose is revised against it meanwhile (raised 1 Aug 2026) · **what Chapter 3 closes on**, which reads directly against the front matter's scope statement and is decided with it (raised 1 Aug 2026). Both are set out in `manuscript/ADVERSARIAL-INTEGRATION-PLAN.md` §11.7 and §11.6.

**Parked (author's direction; on record, not a gate):** permissions/IP for case studies and failure-gallery examples · **companion-repository build-out** (`/patterns`, `/prompts`, `/checklists`, `/case-studies`, `/exercises`) — out of scope for revision pass R1; to be sorted when the book is finalised (author decision, 24 Jul 2026).

## Writing style (condensed from STYLE.md v5.0 — binding)

```
Write to one intelligent colleague from outside your specialism: address them as "you",
use "I" where the judgement is genuinely the author's own, never at an audience from a
lectern. British English; contractions allowed, used lightly and by ear. NOT breezy, NOT
dumbed down: no hype, jokes, slang, exclamation or cliche.
NEVER ANNOUNCE WHAT THE TEXT IS ABOUT TO DO ("The limitation of the procedure is that..."
-> "The catch is that..."). LET THE CONCRETE CASE LEAD: example first, abstraction after,
as the lesson drawn from it.
Paragraphs 80-200 words, one point each. Open on a real sentence carrying real content
(topic sentence, short declarative, question, or the concrete case); never a fragment,
throat-clear or cliffhanger. Sentences ~25 words, 30 maximum: split anything longer into
two without dropping content.
NO METAPHORS anywhere, prose, captions and alt-text alike: state the mechanism literally.
Defined technical terms (gate, loop, pipeline) and declared analogies under examination
are not metaphors. No apologetic preambles, no unbaselined comparatives, no gravitas by
abstraction (STYLE.md SS12.1-12.2).
No em dash as a connector: comma, colon, parentheses, a new sentence, or "e.g." / "i.e."
/ "such as"; dashes only in fixed labels ("Figure 1.1 - ...", "Definition -"); en-dash
ranges (2023-24) fine. Enumerate in prose with parallel grammar; every "However" is
resolved. Numbers over adjectives with baselines; synthesise literature, never list.
Hedge once, precisely; certainty flags (high/moderate/low confidence) on substantive
claims. Explain every demanding term at first substantive use (info-box where warranted)
and add it to the glossary. Never fabricate: mark lived material [AUTHOR: ...] and
unverified figures [verify]. Vendor-neutral. One sentence per line, unnumbered
(STYLE.md SS10).
```
