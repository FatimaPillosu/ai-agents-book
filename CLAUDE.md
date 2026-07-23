# CLAUDE.md — Agentic AI for Environmental Science (book project)

Project instructions for any agent working in this repository. Read fully before acting. `STYLE.md` (the author writing-style guide) is binding for all prose; `FIGURES.md` is binding for all figures.

## What this project is

A single ~150-page e-book on agentic AI for practising environmental and geoscientists, self-published and **released free via LinkedIn**. The goal is author credibility on agentic-AI work, not revenue. It is a **living book**: versioned releases built from this repository, which holds the canonical Markdown source; each release is announced and excerpted through the author's LinkedIn newsletter. Licence, DOI and output format are deferred decisions, not open gates.

The book is **pattern-based, governance-first and diagram-led**: durable workflow patterns rather than named tools, an identical anatomy for every core chapter, worked examples from executed operational hydrology and meteorology, and verification treated as the centre of gravity. Its positioning claim — no existing practical, governance-first treatment for environmental researchers — rests on a limited scan (Jul 2026) and is to be re-verified nearer release.

## Current state (23 Jul 2026)

- Outline **v0.4** (`manuscript/OUTLINE.md`) is authoritative: 17 chapters in 5 parts; budgets indicative (≈150 pp / 38,000–42,000 words / 65–75 figures), not fixed targets. Per-chapter allocations in outline §7 are guidance.
- **Style guide** (`STYLE.md`, v1.1) and **figure guide** (`FIGURES.md`, v1.0) are in place and binding.
- All chapters are being drafted as Markdown in `/manuscript` (`ch01`–`ch17`). Ch. 1 was drafted first as a pathfinder; Ch. 14 is drafted next. Drafts are first-pass and carry `[AUTHOR: …]` markers for lived/executed material.

## How we get there

1. **Source format**: plain Markdown only. No build system, layout or output format is fixed — deferred decisions. Do not introduce a toolchain.
2. **Per-chapter loop**: draft → self-check against `STYLE.md` §7 checklist → independent review pass (reviewer role, not the drafting agent) → author revision → figure briefs per `FIGURES.md` → consistency check against the outline and cross-references.
3. **Chapter anatomy (Parts II–III)**: problem → conventional workflow → agentic redesign → worked example → failure modes → verification checklist → repository pointer. Standard figure set: one architecture, one sequence, one before/after, one or two example figures.
4. **Figures**: every figure is a brief following `FIGURES.md`, in the house infographic style; alt-text written with the brief, never retrofitted.

## Repository layout (target)

`/manuscript` (Markdown source; `OUTLINE.md`; `ch01`–`ch17`) · `/patterns` (runnable minimal examples) · `/prompts` · `/figures-source` (figure briefs + alt-text) · `/checklists` · `/case-studies` (sanitised configurations) · `/exercises`. Version by tags and history; do not carry filename suffixes like `-v0.2` — the chapter file is `chNN-slug.md` and its draft status lives in a header line.

## Hard rules for agents

- **Never fabricate** facts, quotes, statistics, anecdotes or references. Cite only sources verified as real; flag incomplete bibliographic details with **[verify]**.
- **Never resolve [AUTHOR: …] markers.** They denote lived material or decisions only the author can supply. Leave them intact; add new ones where such material is needed.
- **Never alter DECIDED items** (outline §9) without explicit author instruction. Deferred items may be noted but are not gates; do not raise them as blockers.
- **Budgets are indicative guidance**, not hard limits: keep the book roughly in proportion, but a chapter may run over or under where the material justifies it. Avoid unjustified bloat.
- **Vendor-neutral in manuscript prose**: capability classes and approximate years in print; named products and volatile figures only under `/patterns`, `/prompts` and repository docs.
- Do not present designed-but-unexecuted work as accomplished (the digital-twin intercomparison is a worked design in Ch. 8, not a case study).
- **Alt-text is written at figure creation**, never retrofitted; every figure follows `FIGURES.md`. British English everywhere, including captions, alt-text and repo docs.
- **Reflexive production**: the book is written under the governance it describes; substantive agent contributions per chapter feed the preface disclosure statement. (The formal audit-trail mechanism is deferred; a per-chapter status header suffices for now.)

## Decision log

**Decided:** single ~150 pp volume · audience: environmental/geosciences · self-published, free, LinkedIn-first · unified repository with newsletter as update channel · no formal index · specification (Ch. 3) and manuscripts (Ch. 9) chapters in · exercises live in `/exercises`, not the page budget · cross-domain examples deferred to a second edition · manuscript in plain Markdown · budgets indicative · vendor-neutral naming in print · figures governed by `FIGURES.md`.

**Deferred (decide later; not gates):** output/layout format and build toolchain · licence · DOI/Zenodo · CI for runnable examples · reflexive-production audit-trail mechanism · positioning re-scan, beta readers and release-channel limit checks.

**Open:** working title.

**Parked (author's direction; on record, not a gate):** permissions/IP for case studies and failure-gallery examples.

## Writing style (condensed from STYLE.md — binding)

```
Write as an experienced academic author (hydrology/meteorology): authoritative, precise,
measured; confident but hedged; evidence-driven; conservative claims with explicit
certainty flags (high/moderate/low confidence); quantify wherever possible; no hype,
filler or clichés; specificity over generality, numbers over adjectives. British English
throughout. Open every paragraph with a full topic sentence stating its claim — never
short punchy openers or fragments. Paragraphs of 250–400 words following
claim → context → evidence → implication → limitation, like a scientific paper but
slightly less rigorous; prioritise depth over coverage. Synthesise literature
(compare/contrast) rather than listing. Never fabricate facts, quotes, sources or
anecdotes: mark gaps with [AUTHOR: …] and unverified figures with [verify].
Signpost the argument clearly.
```
