# Revision plan — pass R1

**v1.0 · 24 July 2026** · Maintained by ai-editor. Executed by **ai-writer**; reviewed against by **ai-reviewer**. This plan implements the author's decisions of 24 July 2026 (recorded in `CLAUDE.md` §Decision log and outline §9). It is the single authoritative instruction set for revision pass R1; a writer batch needs this document, `STYLE.md` v2.0, `FIGURES.md` v1.0 and the chapter files it is assigned — nothing else.

**What R1 is:** one combined revoice-and-trim pass per chapter (STYLE.md v2.0 voice, de-duplication, citation weaving, standard formats), plus the Ch. 11 rebuild, new front matter, glossary expansion, and the mechanical fixes in §8.

**What R1 is not:** no overall length reduction (deferred by the author — do not compress beyond the de-duplication cuts specified here); no companion-repository build-out (parked — repository pointers remain forward references in prose, nothing is created under `/patterns`, `/prompts`, `/checklists`, `/case-studies` or `/exercises`); no edits to `CLAUDE.md`, `STYLE.md`, `FIGURES.md` or `OUTLINE.md` (ai-editor only).

---

## 1. Global instructions (apply to every batch)

- **G1 — Revoice to STYLE.md v2.0.** Every chapter except ch01 is rewritten from the retired v1.1 formal-academic register into the v2.0 personal/conversational voice: first person ("I" for the author's judgement, "you" for the reader), full intellectual weight retained, no hype or banalisation, paragraphs ~150–350 words opening with a real claim. Apply the §7 pre-submission checklist of `STYLE.md` before returning each chapter.
- **G2 — Sentence-per-line.** Convert all body prose to one sentence per line with a blank line between paragraphs, no numeric prefixes (`STYLE.md` §10). Headings, info-boxes, figure briefs, block quotations, lists, captions, tables and references keep their natural layout.
- **G3 — Info-boxes.** At the first substantive use of a demanding term in a chapter, add an info-box in the fixed form of `STYLE.md` §9 (once per chapter per term). Prefer placing the definitive box in the term's canonical-home chapter (§3 below). Do **not** edit `manuscript/GLOSSARY.md` — Batch 7 consolidates it (§7).
- **G4 — Citations only from `/research`.** Manuscript citations are drawn exclusively from the verified research reports in `/research` at the repo root (compiled by ai-researcher; every source carries a DOI or URL). Weave citations where a report entry supports a chapter's key claim; add the source to the chapter's references list with its DOI/URL. **Never cite from memory.** Existing references (e.g. Klemeš; Refsgaard & Henriksen; Jakeman et al.; Oberkampf & Trucano in ch11; Sharma et al. in ch13) are retained: if a `/research` report confirms the bibliographic details, complete them and remove the `[verify]` flag; otherwise keep the flag. If no report yet covers a claim, leave or add `[verify]` — do not supply a reference. If `/research` is empty or does not cover a chapter's topics when a batch runs, do the rest of the batch and leave citation weaving flagged with `[verify]`; a later weaving pass will follow the research sweep.
- **G5 — Integrity (hard rules).** Never fabricate facts, quotes, statistics, anecdotes or references. Never resolve or delete an `[AUTHOR: …]` marker — they are the author's lived material; add new ones where such material is owed. British English everywhere. Vendor-neutral in manuscript prose (capability classes and approximate years; named products only in repository docs).
- **G6 — De-duplication.** Apply the canonical-home map in §3 exactly. General rule for repetition the map does not name: if a passage re-derives an idea whose canonical home is elsewhere, cut it to at most one sentence plus a cross-reference; if it applies the idea to the chapter's own material, keep the application.
- **G7 — Cross-references.** Cross-chapter references in prose name the chapter, and where helpful the topic ("the failure gallery's treatment of context loss in Chapter 13"), never a section number in another file. Within-chapter references may use section numbers.
- **G8 — Length discipline.** Revoicing plus de-duplication should leave each chapter at or slightly below its current length. Growth is expected only in ch11 (rebuild), ch00 (new) and the glossary. Budgets remain indicative, not hard limits.
- **G9 — Figure briefs.** Any new or renumbered figure follows the `FIGURES.md` §6 brief format in full, including caption and alt-text written with the brief, one of the five canonical types, house palette and iconography.
- **G10 — Scope per batch.** A batch edits only the files listed for it in §10. No batch edits admin documents, another batch's chapters, or (except Batch 7) `GLOSSARY.md`.

## 2. Standard formats

### 2.1 Status header (every chapter, including ch00)

Replace each chapter's existing header block with:

```
> **Status:** draft r2 · voice v2.0 (`STYLE.md`) · sentence-per-line per `STYLE.md` §10 · figures as briefs per `FIGURES.md`.
> **Conventions:** vendor-neutral (outline §9) · **[AUTHOR: …]** marks lived material only the author can supply · **[verify]** marks real but unconfirmed details · citations drawn only from verified reports in `/research`. Nothing has been invented.
```

A chapter may append **one** further line of chapter-specific integrity notes where the current header carries them (e.g. ch11's note on its four scholarly references, ch14's note on executed operational work). The voice field is mandatory: a chapter not yet revoiced must say `voice v1.1 (retired — revoicing pending)`; after its batch completes, every chapter says `voice v2.0`. Ch01 already in v2.0 gets the standard header with `draft r2`.

### 2.2 Verification checklist (standard bulleted, printable)

Chapters 5–12 each carry exactly one verification checklist in this form:

```
## N.M Verification checklist

One-sentence lead-in stating what the checklist certifies and who applies it.

- **Bold lead phrase naming the check.** One to three supporting sentences stating how a
  reviewer — not the agent — confirms it, with cross-references in parentheses (§N.x;
  Chapter M) and an optional confidence flag.
- **Next check.** …
```

Rules: six to ten items; each item confirmable by a colleague who did not build the workflow; the list is self-contained enough to print and use without the chapter open; checklists keep natural layout (exempt from sentence-per-line). Ch06 §6.6, ch09 §9.7 and ch10 §10.7 are already in this shape — align wording and lead-ins, keep content. Ch05 §5.6, ch07 §7.6 and ch08 §8.7 are prose paragraphs — convert each to this format, preserving every check (ch05's eight named checks including **Yield**; ch07's seven numbered checks; ch08's seven procedural checks). Ch11 and ch12 gain new checklists (§5 and §8/M4).

## 3. De-duplication: canonical-home map

Each recurring idea below gets **one canonical home** (occasionally split between failure-anatomy and countermeasure, stated explicitly). Everywhere else: keep at most a one-sentence recall plus a cross-reference; keep chapter-specific application; cut re-derivations of mechanism.

**T1 — Fabricated citations.**
- Canonical anatomy, check and trace: **ch13 §13.2** (keep in full).
- Canonical workflow countermeasure (the citation-verification gate): **ch05 §§5.3–5.6** (keep in full; this is the pattern chapter's job).
- ch09 §9.6, first failure mode: cut the paragraph to ~3 sentences — the risk recurs at the drafting stage; the discipline is the same gate as Chapter 5; the manuscript-stage consequence (a fabricated reference entering a submission or proposal) stays. Cross-reference Chapters 5 and 13. Do not re-derive why models fabricate.
- ch03 (failure-mode list near the top), ch06 (single mention), ch12 (prompt-injection example naming an inserted fabricated citation): keep as one-line mentions; already cross-referential.

**T2 — Over-agreeable review (sycophancy).**
- Canonical anatomy and trace: **ch13 §13.5** (keep in full, including the Sharma et al. reference subject to G4).
- Canonical countermeasure (independence engineering: different model, narrowed context, adversarial brief, external source of truth): **ch10 §10.3**, with the roster-level failure discussion of §10.6 kept but cross-referencing ch13 for the anatomy.
- ch07 §7.5, third failure mode: cut the re-derivation of why self-review and same-model review ratify to one recall sentence; keep the ch07-specific reviewer configuration (separate instance, clean context, fault-finding brief against a checklist, read-only, no merge rights) and keep the honest-limitation sentence at the end. Cross-reference Chapters 10 and 13.
- ch15 (the independence-of-review passage): keep one sentence naming the hazard with its existing cross-reference to Chapter 13; trim any mechanism re-explanation.
- ch03 (list mention): keep as is.

**T3 — Least-privilege tool access.**
- Canonical home: **ch12** (security section) — full treatment, the chapter's info-box, and the glossary entry.
- ch02, ch07 (two mentions), ch14 (two substantive mentions), ch15, ch16: keep as one-line uses with "(Chapter 12)" — most already are; trim anything longer than a sentence of justification.
- ch10 (roster derivation, ~5 mentions): keep the derivational role (specification inputs fix per-role least-privilege access) but no re-justification of the principle; one cross-reference to Chapter 12 suffices for the chapter.

**T4 — Verification must be external to the system verified.**
- Canonical argument, including reference-data contamination: **ch11 §11.3** (kept and revoiced in the rebuild).
- ch01: keeps the first introduction of the principle (one paragraph, forward-reference to Chapter 11).
- ch05 (checklist "Independence" item), ch06, ch07 §7.5, ch13 §§13.1–13.2: keep one-sentence recalls with cross-references to Chapters 1 and 11; cut multi-sentence re-derivations.

**T5 — Plausible failure / fluency uncorrelated with correctness.**
- Canonical home: **ch01** (with the existing glossary term "plausible failure").
- ch05 §5.5, ch08 §8.6, ch09 §9.6, ch11 §11.3, ch13 §13.7: one-sentence recall each, "(Chapter 1)". ch13 §13.1 may keep two sentences, since the property motivates the whole gallery. Cut every other re-derivation of the mechanism.

**T6 — Confident extrapolation.**
- Canonical anatomy, check and trace: **ch13 §13.7** (keep in full).
- ch08 §8.6, first failure mode: keep the campaign-specific guard (report the training-data range; score out-of-range performance separately; never fold extrapolation into a headline metric); cut the general anatomy to one sentence plus a cross-reference to Chapter 13.

**T7 — Benchmarks versus task-grounded evaluation (the jagged frontier).**
- Canonical home for the evaluation argument: **ch11 §11.1**. ch01 keeps its honest-capability-boundary introduction with a forward reference.
- In the ch11 rebuild, trim §11.1's recap of Chapter 1's jagged-frontier material to at most two sentences; the chapter's own argument (benchmark evidence inadmissible for workflow correctness) stays in full.

## 4. Per-chapter task summary

Every chapter: G1–G10, header per §2.1. Additional per-chapter tasks are listed in the batch tables (§10). Chapters with no named de-duplication or mechanical task (ch04, ch14, ch16, ch17) receive revoice, header, info-boxes and citation weaving only. **ch01 is already in v2.0 voice**: its tasks are limited to the §2.1 header, de-duplication conformance (it is the canonical home for T5 and the introduction for T4/T7 — verify nothing needs cutting, only that forward references are present), citation weaving per G4 (including the benchmark-trajectory claim currently marked `[AUTHOR: verify…]`), and confirming its boxed terms are ready for Batch 7's glossary sweep. Do not re-voice ch01.

## 5. Ch. 11 rebuild brief

Ch11 is currently ~55% the length of its Part III siblings, has no checklist, no repository pointer, no worked example, and does not deliver the measurement material promised to it by ch05 §5.7 ("The evaluation of the gate itself — how to measure its false-negative rate, and how much verification a given synthesis warrants — is developed in Chapter 11") and by ch10 §§10.6–10.7 (reviewer fault base rates "await measurement"; roster cost justified only by "measured independent checking"). Rebuild it to the following structure. Target length after rebuild: comparable to ch12/ch13 (indicatively 4,500–5,500 words). Everything is written in v2.0 voice and sentence-per-line from the start.

**§11.1 Why a leaderboard is the wrong instrument.** Revoice the existing section; trim the Chapter 1 recap per T7. Keep the closing claim: benchmark results are admissible about capability in general, inadmissible about a particular workflow's correctness.

**§11.2 Five tiers of evidence.** Revoice; keep the tier definitions, the existing `[AUTHOR: confirm tier definitions …]` marker, and Figure 11.1 unchanged in substance (revoice its caption only if needed for consistency).

**§11.3 Verification must be external to the system verified.** Revoice; this is now the canonical home for T4 — keep the contamination argument in full.

**§11.4 Building a task-grounded evaluation set from your own workflow (NEW).** The method, concretely enough to follow: (a) **harvest cases** from the workflow's own history — past runs whose outcomes a human settled, outputs of the pre-agent manual workflow, incidents from the group's failure log (the ch13 gallery instances are exactly this), and a small held-back set of known-correct items (the held-back known-relevant papers of ch05 generalised); (b) **curate** each case as input + reference outcome + metric fixed in advance + provenance of the reference; (c) **stratify** across task types and regimes so the set spans the conditions the workflow will meet — the differential-split discipline of Klemeš's testing scheme applied to an evaluation set; (d) **be honest about size** — a few dozen curated cases beat zero, but small samples carry wide uncertainty, so results are reported with intervals, not bare percentages; (e) **version and refresh** the set, and guard it against contamination per §11.3 (prefer references generated after the model's training cut-off; record what entered context). Cite supporting literature only per G4.

**§11.5 Measuring the gate itself (NEW — delivers the ch05/ch10 promise).** How to measure a gate's or reviewer's false-negative rate: **seeded-defect testing** — plant known faults of the classes the gate must catch (a fabricated citation, a unit slip, an out-of-range value, a dropped constraint) into otherwise-sound inputs, run the gate blind, and count misses; stratify by fault class, since a gate can be strong on one class and blind to another. Report the rate with its sampling uncertainty — with small numbers of seeded faults, zero observed misses still leaves a non-trivial upper bound on the true miss rate, and the honest statement is an interval, not a clean zero. Pair this with the **yield diagnostic** already planted in ch05 §5.6 ("Yield") and ch10 §10.6: a gate or reviewer that never fires on real work is evidence of a broken check, not a flawless workflow. State when to re-measure: after a model or prompt change, after a data-regime change, and on a calendar. Frame the whole section with the calibration analogy — this is calibrating the measuring instrument before trusting its readings. Say explicitly that this section answers ch05's and ch10's forward references, and say how much verification a given output warrants by tying gate-measurement effort to the tier/stakes matching of §11.7.

**§11.6 Worked example (NEW).** One worked pass through §§11.4–11.5 in the author's own domain: building an evaluation set for a rainfall-forecast-verification workflow step and measuring one of its gates by seeded defects. All actual case counts, fault classes seeded, catch rates and intervals are the author's lived material — write the scaffolding and mark every number `[AUTHOR: …]` (e.g. `[AUTHOR: number of curated cases, the stratification you used, and the measured catch rate with its interval]`). Move the existing `[AUTHOR: a worked instance from your own practice …]` marker from old §11.4 into this section. Do not invent illustrative numbers, even flagged ones.

**§11.7 Operating the ladder in practice.** The existing §11.4, revoiced; extend the tier/stakes matching with one paragraph connecting it to the measured gates of §11.5 (a tier claim is only as strong as the measured check that establishes it).

**§11.8 Verification checklist (NEW, per §2.2).** Six to ten items covering: tier named and recorded with every claim; checks external to the producing agent; contamination routes controlled and recorded; evaluation set versioned, stratified and refreshed; every gate's false-negative rate measured and re-measured on trigger events; yield monitored (a never-firing check investigated); tier matched to stakes; verification effort recorded in provenance (Chapter 12).

**§11.9 Repository pointer (NEW).** House pattern (cf. ch05 §5.7 / ch10 §10.8): evaluation-set template and seeded-defect harness under `/patterns/ch11-verification-and-evaluation`, printable checklist under `/checklists`, with `[AUTHOR: confirm paths and contents]` — a forward reference only; build nothing (repository parked).

**Figures.** Keep Figure 11.1. Add two new briefs, plus one optional, all per `FIGURES.md` §6 with full captions and alt-text:
- **Figure 11.2** — type: architecture — claim: a task-grounded evaluation set is built from the workflow's own history through harvest → curate → stratify → hold out → version, and feeds the tiered checks. Elements: data-store icons for history sources (sky blue), a curation step, a stratified set, a held-out split, a versioned artefact; gate diamond where the set meets the workflow.
- **Figure 11.3** — type: sequence — claim: a gate's false-negative rate is measured by seeding known defects, running the gate blind, tallying catches and misses, and reporting a rate with its uncertainty; re-measurement triggers close the loop. Actors: human (seeds faults), gate (vermillion), tally/record (data store).
- **Figure 11.4 (optional, include if it earns its place)** — type: before/after — claim: trusting a leaderboard number versus trusting task-grounded evidence: same workflow, different evidential basis.

**Acceptance criteria for the rebuild (ai-reviewer):** every promise in ch05 §5.7 and ch10 §§10.6–10.7 is now answered by a named section; the chapter carries a §2.2-format checklist and a repository pointer; the worked example contains no invented numbers and at least three `[AUTHOR: …]` markers; two new figure briefs complete per `FIGURES.md`; the four scholarly references retained with `[verify]` unless confirmed in `/research`; length in the indicated range; voice v2.0 throughout.

## 6. Front-matter brief (new file `manuscript/ch00-front-matter.md`)

Create the front matter (outline §7: ≈5 pp) with the §2.1 header and these sections, in v2.0 voice:

- **How to read this book.** The five-part shape and what each part does; suggested paths (a practitioner can start at Chapter 3; a manager can read Part V and the failure gallery; nobody should skip Chapter 11); the info-box and glossary convention; the figure conventions in one paragraph (five canonical types, fixed icon set and colours); the living-book model — versioned releases, the repository as the layer that stays current, the newsletter as the update channel.
- **What you need.** Comfort with Python and the command line; no machine-learning expertise; a note that readers without paid model access are served concretely by Chapters 14 and 16 (mirrors outline §4 — adapt, do not contradict).
- **Icon key — Figure 0.1.** A complete figure brief per `FIGURES.md` §6: type architecture; claim: six recurring actors, one fixed icon and colour each, learned once and reused book-wide; elements exactly the `FIGURES.md` §3.2 set — human (blue head-and-shoulders), agent (orange rounded square with loop arrow), tool (green wrench), data store (sky-blue cylinder), gate (vermillion diamond), reviewer (purple head-and-shoulders with tick) — each with a short plain-language label; flow: none (a legend); full caption and alt-text.
- **Contribution statement and domain framing.** Adapt the two preface paragraphs of outline §1 (the positioning claim with its "limited scan, Jul 2026 — re-verify before release" caveat, and the hydrology/meteorology domain framing stated plainly). These are the outline's own words for exactly this purpose; adapting them is not fabrication.
- **Disclosure statement (skeleton).** How agents were used to produce the book: the reflexive-production stance (the book is written under the governance it describes); a per-chapter contribution disclosure to be generated from the chapter status records, left as a structured skeleton with markers — e.g. `[AUTHOR: confirm the per-chapter agent-contribution summary once R1 completes]`, `[AUTHOR: decide the granularity of the disclosure — per chapter or per task]`; note that the formal audit-trail mechanism is a deferred decision. Agents are never authors; accountability rests with the author.

## 7. Glossary expansion brief (Batch 7 only)

`manuscript/GLOSSARY.md` currently covers ch01 and ch07 terms only. After all chapter batches complete: sweep every chapter (ch00–ch17) for info-boxed terms and give each one an entry; keep the existing plain, warm register and entry format; alphabetise the whole list; British English. Expected additions include (not exhaustive — the sweep is authoritative): specification, acceptance criteria, stop condition, retrieval grounding, citation-verification gate, quality control (QC) flag, provenance, orchestration, sub-agent, hook, regression test, ensemble, intercomparison, calibration, multi-agent roster, independent reviewer, evidential tier, evaluation set, false-negative rate, seeded-defect testing, audit trail, assumption registry, least privilege, prompt injection, token, open-weight model, data sovereignty, sycophancy/over-agreeable review, context loss, confident extrapolation, specification drift. Where a term in this list is not yet boxed anywhere, box it in its canonical-home chapter's batch (each batch's writer adds boxes per G3; Batch 7 only consolidates). One entry per term; if two chapters box the same term, the glossary entry follows the canonical-home chapter's wording.

## 8. Mechanical fixes

- **M1 — ch08 figure renumbering.** Briefs must appear in ascending order of first appearance. Renumber: current Figure 8.4 ("The hypothesis provenance gate", appearing second) → **8.2**; current 8.2 ("Conventional campaign versus agent-orchestrated campaign") → **8.3**; current 8.3 ("Orchestrating the three-track intercomparison") → **8.4**. Figure 8.1 unchanged. Update every occurrence: bold figure lines, brief `id:` fields, captions, alt-text and all in-text mentions. No other chapter references ch08 figures (checked 24 Jul 2026).
- **M2 — ch13 sixth failure trace.** **Decision: add the trace.** Context loss does not resist drawing — it is a textbook annotated failure trace: a sequence in which a constraint is established early, silently dropped at a context boundary, contradicted by a confident later output, and caught by a consistency assertion against externalised state. Add a full failure-trace brief to §13.6 as **Figure 13.5** ("Context loss — the dropped constraint and the boundary check that catches it"), with the failure point and catching check called out in vermillion per `FIGURES.md` §5, caption and alt-text complete, and the anonymised-example slot tied to the section's existing `[AUTHOR: …]` marker (no invented incident details on the canvas — generic labels only). Renumber the existing Figure 13.5 (confident extrapolation, §13.7) → **Figure 13.6**, updating all mentions. No other chapter references ch13 figure numbers (checked 24 Jul 2026).
- **M3 — ch11 checklist and repository pointer.** Delivered by the rebuild (§5, §§11.8–11.9).
- **M4 — ch12 checklist and repository pointer.** Add two closing sections in the house pattern. The checklist (per §2.2) is drawn from the chapter's own content: registries (assumptions, uncertainty) exist and are current; the audit trail reconstructs who/what/when for any artefact; reviewer-coverage record kept; least privilege confirmed by inspecting tool interfaces, not agent prose; prompt-injection surface reviewed for every channel that feeds agent context; credential and partner-data handling per institutional policy; documentation survives staff turnover (a newcomer can operate the workflow from the record). The repository pointer follows the ch05/ch10 pattern (printable checklist, registry and audit-trail templates) with `[AUTHOR: confirm paths and contents]`; build nothing.
- **M5 — checklist standardisation.** Convert ch05 §5.6, ch07 §7.6, ch08 §8.7 from prose to §2.2 format, preserving every check; align lead-ins of ch06 §6.6, ch09 §9.7, ch10 §10.7.
- **M6 — status headers.** All chapters (and ch00) to the §2.1 format with the voice field.

## 9. Acceptance criteria (what ai-reviewer reviews each batch against)

1. Status header matches §2.1 exactly, voice field `v2.0`.
2. Body prose is sentence-per-line; exempt elements keep natural layout; no numeric prefixes anywhere.
3. Voice passes `STYLE.md` §7: real claims to open paragraphs, personal register without banalisation, certainty flags folded in, numbers over adjectives, British English.
4. Info-boxes at first substantive use of demanding terms, `STYLE.md` §9 form, once per chapter per term.
5. De-duplication per §3: no re-derivation of T1–T7 outside its canonical home; canonical homes intact (nothing canonical was cut); cross-references point to the right chapters.
6. Every citation traces to an entry in a `/research` report (DOI/URL present in the chapter's references); everything else carries `[verify]`; nothing cited from memory; no `[AUTHOR: …]` marker resolved, moved without instruction, or deleted.
7. Checklists in §2.2 format; ch05–ch12 each have exactly one; all original checks preserved.
8. Figure briefs complete per `FIGURES.md` §6 including alt-text; figure numbers ascend in order of first appearance (ch08, ch13 fixed per M1/M2).
9. Chapter net length at or below its pre-R1 length (exceptions: ch11 per §5, ch00, glossary).
10. Batch scope respected: only the batch's files touched; admin documents untouched; nothing created outside `/manuscript`.
11. For Batch 5 additionally: the §5 rebuild acceptance criteria. For Batch 7 additionally: glossary covers every boxed term in ch00–ch17, alphabetised, one entry per term.

## 10. Batch structure (7 batches)

Batches 1–6 are disjoint by file and can run as independent parallel writer passes. **Batch 7 must run last** (its glossary consolidation sweeps all chapters). Effort is roughly equalised by current file size plus task weight.

| Batch | Files | Plan sections that apply | Chapter-specific tasks |
|---|---|---|---|
| **1 — Part I + front matter** | `ch00-front-matter.md` (new), `ch01`, `ch02`, `ch03`, `ch04` | §1, §2, §3 (T3–T5, T7 as they touch ch01–ch04), §4, §6, §8 M6, §9 | ch00: create per §6 incl. Figure 0.1 brief. **ch01: no revoice** — header, de-dup conformance (canonical T5; forward refs for T4/T7), citation weaving, boxed-term readiness only. ch02: revoice; least-privilege mention stays one line (T3). ch03: revoice; failure-mode list mention stays as is (T1/T2). ch04: revoice only. |
| **2 — Evidence & data** | `ch05`, `ch06` | §1, §2, §3 (T1, T4, T5), §4, §8 M5–M6, §9 | ch05: canonical T1 countermeasure — keep §§5.3–5.6 in full; convert §5.6 checklist to §2.2; T5 one-line recall in §5.5; §5.7's forward reference to Chapter 11 stands (the rebuilt ch11 §11.5 answers it). ch06: revoice; T1/T4 one-line recalls; align §6.6 lead-in. |
| **3 — Code & orchestration** | `ch07`, `ch08` | §1, §2, §3 (T2, T3, T5, T6), §4, §8 M1, M5–M6, §9 | ch07: T2 cut in §7.5 per map; T3 mentions one-line; convert §7.6 checklist. ch08: M1 renumbering; T6 cut in §8.6 per map; T5 one-line recall; convert §8.7 checklist. |
| **4 — Manuscript & multi-agent** | `ch09`, `ch10` | §1, §2, §3 (T1, T2, T3, T5), §4, §8 M5–M6, §9 | ch09: T1 cut in §9.6 per map (~3 sentences + cross-refs); T5 one-line recall; align §9.7. ch10: canonical T2 countermeasure — keep §10.3 and §10.6 with anatomy cross-ref to Chapter 13; T3 derivational mentions kept, justification cut; §10.6/§10.7 forward references to measurement stand (rebuilt ch11 §11.5 answers them); align §10.7. |
| **5 — Trust core** | `ch11`, `ch12` | §1, §2, §3 (T3, T4, T7), §4, **§5 in full**, §8 M3–M4, M6, §9 | ch11: full rebuild per §5 (canonical T4, T7). ch12: revoice; canonical T3 home — full least-privilege and prompt-injection treatment with info-boxes; M4 checklist + repository pointer. |
| **6 — Failures & constraint** | `ch13`, `ch14` | §1, §2, §3 (T1, T2, T4, T5, T6), §4, §8 M2, M6, §9 | ch13: canonical home for all six failure anatomies — keep entries in full; M2 sixth trace + renumber; T4/T5 recalls per map limits. ch14: revoice; T3 mentions one-line; header keeps its executed-work integrity line. |
| **7 — Adoption + glossary (runs last)** | `ch15`, `ch16`, `ch17`, `GLOSSARY.md` | §1, §2, §3 (T2, T3), §4, **§7 in full**, §8 M6, §9 | ch15: T2/T3 mentions one-line per map. ch16: revoice; T3 mention one-line. ch17: revoice only. GLOSSARY.md: consolidate per §7 after all other batches (including this batch's own chapters) are done. If `/research` reports exist by then, additionally create `manuscript/FURTHER-READING.md` as an annotated further-reading skeleton drawn **only** from those reports (back-matter policy, outline §9); if none exist, skip and note it. |

---

*Change control: ai-editor maintains this plan; ai-writer and ai-reviewer do not edit it. Discrepancies discovered mid-batch (a cross-reference that does not resolve, a duplication the map missed, a checklist check that cannot be preserved) are flagged in the batch's PR discussion, not silently resolved.*
