# Adversarial-review integration plan — pass A1

**v1.1 · 1 August 2026** · Maintained by **ai-editor**. Executed by **ai-writer**; reviewed against by **ai-reviewer**.

**Change from v1.0:** §1–§10 are the record of pass A1 and stand as written. A new **§11** records what the review left for an editorial decision: five rulings, two escalations to the author, one process finding about this plan's own structure, and the small mechanical pass (**A2**) those rulings schedule. §11.1 amends G6 by one info-box and nothing else.

This plan converts the eight substantive findings and one secondary finding of `manuscript/ADVERSARIAL-REVIEW.md` (F1–F9) into per-chapter instructions. The review is the author's brief; this document is the executable form of it. Where the review named a change but left the structural question open, **this plan decides it** and records the reasoning in §2, so ai-writer makes no structural decision of its own.

A writer batch needs this document, `STYLE.md` v5.0, `FIGURES.md` v2.0, `ADVERSARIAL-REVIEW.md`, the three reports in `/research`, and the chapter files assigned to the batch — nothing else.

**What A1 is.** (i) One new chapter (F8). (ii) Four new sections in existing chapters (F1, F3, F4, F7). (iii) One correction of a stated overclaim (F2). (iv) One new tier in the evidential hierarchy, with the renumbering that follows (F5). (v) One principle promoted from a chapter pattern to a general architecture, with matching cuts downstream (F6). (vi) Targeted insertions in eleven further chapters. (vii) Three new figures and one re-brief.

**What A1 is not.** No revoicing (the manuscript is already at `STYLE.md` v5.0 and the captions were converted on 30 July 2026 — verified). No re-weaving of `/research` beyond the citations named here. No new research sweep. No companion-repository build-out (parked). No length-reduction pass (deferred; see §8). No edits to `CLAUDE.md`, `REVISION-PLAN.md` or `RESEARCH-INTEGRATION-PLAN.md` by ai-writer — those are ai-editor's, and R1/R2 are closed records that stay as written.

**Standing on decided items.** Four elements of this plan touch matter the author has previously decided or must decide personally. They are marked **[AUTHOR SIGN-OFF]** at the point of use and listed together in §7.4. ai-writer executes them as written but must leave the `[AUTHOR: …]` markers this plan specifies; ai-reviewer checks the markers are present and unresolved.

---

## 1. Global rules (apply to every batch)

- **G1 — Citations only from `/research`.** Every citation traces to a named entry in one of the three reports, with DOI or URL in the chapter's references. **Checked before writing this plan:** the reports contain *no* source on automation bias, deskilling or skill atrophy; *none* on homogenisation of research questions or monoculture; *none* on rebound effects or induced demand in computing; and *none* directly on the reproducibility of agentic results. Every task below that touches those subjects therefore says explicitly whether it is argued from the book's own already-cited evidence, argued without citation, or carries `[verify]`. **ai-writer adds no citation this plan does not name.** If a passage feels like it needs a source, that is a finding for the PR discussion, not licence to supply one.
- **G2 — Own arguments are labelled as own arguments.** Several passages here are the book reasoning from its own premises rather than reporting evidence. Each such passage carries a calibrated confidence flag per `STYLE.md` §6.3, and where the argument is a conjecture it is named as one. Do not dress a conjecture as a finding.
- **G3 — Integrity (hard rules).** Never fabricate. Never resolve, move or delete an `[AUTHOR: …]` marker; add the new ones this plan specifies. British English. Sentence-per-line for all new body prose (`STYLE.md` §10). v5.0 colloquial voice for every new sentence: new material must be indistinguishable in register from its surroundings. No metaphors anywhere, including captions and alt-text. ~30-word sentence ceiling. No em dash as a connector.
- **G4 — Vendor neutrality in prose.** No product, vendor, model or channel name in manuscript prose; capability classes and approximate years only. Institutions and standards bodies may be named as institutions.
- **G5 — De-duplication discipline.** Every idea introduced by this plan has exactly one canonical home, listed in §3. Everywhere else it is a short cross-reference, one clause or one sentence, never a re-derivation. This rule is the reason F6 cuts as well as adds; ai-reviewer checks the cuts happened.
- **G6 — Info-boxes and glossary are open in A1.** Unlike R2, this pass **does** add info-boxes and glossary entries, because it introduces genuinely new demanding terms. The new boxes and entries are enumerated in §5 and §7.2. No others.
- **G7 — Word budgets.** Each task carries an approximate prose word budget. Budgets exclude figure briefs and reference entries. A budget is a ceiling with about 20% tolerance, not a target: meet the instruction in fewer words where you can. Where a task says "cut", the cut is mandatory and its size is approximate.
- **G8 — Nothing unexecuted presented as accomplished.** Unchanged from R2. The Ch. 8 three-track intercomparison remains a worked design. The new Ch. 17's checklist is a proposal for practice, not a report of practice.
- **G9 — Renumbering is mechanical and total.** Where this plan renumbers something (a tier, a section, a chapter, a figure), every reference to it changes in the same batch. §5 lists the sites; ai-reviewer greps for stragglers.
- **G10 — No new forward promises.** The book already carries forward references that had to be paid off in R1. Do not add a sentence of the form "Chapter N develops this" unless this plan says so and the target section exists.
- **G11 — Status headers.** Every edited chapter's status header line advances its draft number (`draft r4` → `draft r5`, and so on). The new chapter opens at `draft r1` with the standard conventions block copied from `ch16`.
- **G12 — Figures.** New and amended figures follow `FIGURES.md` v2.0 in full: the complete brief with all fields, caption and alt-text **written at the same time as the brief, never retrofitted**, in the v5.0 colloquial register. Re-rendering the SVGs is a separate mechanical task, listed in §10.

---

## 2. Structural decisions taken by this plan

These are the questions the review left open. ai-writer implements them; it does not reopen them.

### D1 — F8 becomes a new chapter, placed as **Chapter 17**, and "What will last" becomes **Chapter 18**

**Decision.** A new chapter, `manuscript/ch17-on-the-receiving-end.md`, titled **"On the receiving end"**, is inserted as the second chapter of **Part V**. The current `ch17-what-will-last.md` is renamed `ch18-what-will-last.md` and renumbered throughout. The book becomes 18 chapters in 5 parts. **[AUTHOR SIGN-OFF: chapter count and title.]**

**Why a chapter and not a section.** The material is ~3,500 words across five distinct movements (reviewing a manuscript produced with agents; which failure modes are externally detectable; inheriting a workflow whose specification you did not write; judging a vendor or institutional product with agentic components; what a reviewer is entitled to demand). No existing chapter can absorb that without distorting. Ch. 11 is already the longest chapter in the book at 9,558 words; Ch. 12 is a producer-side specification of what to record, not a consumer-side account of what to ask for; Ch. 9 is author-side by construction. Distributing the material across three chapters would breach G5 and would leave the reader without the one thing the finding says is missing: a place to go when the workflow is not theirs.

**Why Part V and not the end of Part III.** The chapter is defined by the reader's *position* (no authority over the specification), not by a method. Part V is the book's only positional part, and the new chapter pairs directly with Ch. 16, which is the same reader holding authority. Reviewing a manuscript is a community act, which is Part V's register. Placing it before "What will last" keeps the coda last.

**Why the placement is also the cheap one, and why that matters here.** A Part III insertion at Ch. 14 would renumber four chapters and hit **36 inbound chapter references, 8 figures, 8 SVG files and their renderer entries, plus `GLOSSARY.md` (2 refs) and `FURTHER-READING.md`**. The Part V placement renumbers one chapter and hits **3 inbound references and 1 figure**. In an 18-file manuscript carrying 308 chapter cross-references, where Ch. 10 alone carries 38 and Ch. 15 carries 34, a mechanical change of that size is a real risk of silent breakage. The intellectual case between the two placements is close; the cost case is not. Cheap wins.

**Protecting the leverage.** Because the finding calls this the highest-leverage gap, the chapter is signposted in four places rather than left to be found: `ch00` "How to read this book", Ch. 1 §1.5, Ch. 11 §11.3 and Ch. 12 §12.4. Tasks 0.2, 1.4, 11.7 and 12.3.

**Renumbering task (itemised, mandatory, one batch).** See task **R.1** in §5.

### D2 — F6: propose–dispose is named in **Chapter 2, new §2.6**, as **"the propose–dispose separation"**

**Decision.** The principle gets its canonical home in a new **§2.6 "Propose and dispose: where authority sits"**, inserted after §2.5 (orchestration) and before the cost model, which becomes **§2.7**. The principle is stated in its general form: *the agent proposes; something the agent does not control disposes.* The three disposer classes are named once here — a deterministic rule, a human decision, an external source of truth — and every later instance is one of the three.

**Why Ch. 2 and not Ch. 4.** Propose–dispose is an architectural claim about how parts are arranged, and Ch. 2 is the anatomy chapter. §2.5 already builds the exact vocabulary the principle is stated in (sequence, delegation, reviewer step, gate) and closes by saying orchestration is where the workflow layer of Ch. 1's taxonomy gets built; §2.6 answers *how*. Ch. 4's question is prior and different: whether an agent should touch the task at all. Ch. 4 is also the shortest chapter in Part I at 2,432 words and is tightly shaped; a large architectural section would unbalance it, and Ch. 4 already receives a substantial new section under F3 (D4).

**Where the cuts come from.** F6 must reduce re-derivation, not only add. Five chapters currently re-derive the principle in local costume. Each keeps its instance in full and loses its general derivation, replaced by a cross-reference:

| Chapter | What is cut | Approx. |
|---|---|---|
| Ch. 6 §6.3 | the general restatement at "So the agent's contribution is confined to the two things it does well … stays with deterministic code and, above it, with the accountable scientist" | −60 |
| Ch. 8 §8.3 | "This is not timidity about model capability … fail by imitating competence" (the re-derivation from Ch. 1) | −70 |
| Ch. 9 §9.3 | the general operator-not-author derivation, keeping the manuscript-specific boundary | −80 |
| Ch. 12 §12.8 | the general statement of why a proposed action waits on a human, keeping the security-specific content | −70 |
| Ch. 14 §14.3–§14.4 | the re-argument of why the core is deterministic and why the tutoring tier holds no write path, keeping the measurement-specific and least-privilege-specific halves | −140 |

Total cuts ≈ −420 words against a new §2.6 of ≈ +550 and one new figure. F6 is therefore roughly length-neutral in prose, not length-reducing. Stating that plainly is better than claiming a saving the material does not yield; the real reductions this plan can offer are in §8.

### D3 — F5: independent-method corroboration enters as **Tier 5**; the old Tier 5 becomes **Tier 6** and is renamed

**Decision.** The ladder becomes six tiers:

1. execution
2. internal consistency
3. reproduction of held-out truth
4. out-of-sample generalisation
5. **independent-method corroboration** *(new)*
6. **adversarial scrutiny** *(was "independent adversarial scrutiny", Tier 5)*

**Why Tier 5 and not Tier 4.** Out-of-sample generalisation tests transfer across regime while keeping the same measurement chain; independent-method corroboration changes the measurement chain itself, which is the stronger move and the one the environmental sciences actually rest on. Placing the new tier at 5 also renumbers exactly one existing tier, which is the cheapest correct answer.

**Why the rename.** The review's category objection is correct: Tiers 1–5 are defined by the check, the old Tier 5 by the checker. Dropping "independent" from the top tier's name makes it a check-name like the rest, and §11.2 gains one paragraph stating the asymmetry openly: the top tier is the one whose strength depends on a property of the checker, that property is itself a measured quantity (§11.5), and that is why the least reproducible instrument sits at the top of a hierarchy of evidential strength.

**Every site where tier numbers or the old tier name appear** (searched, not guessed — this list is exhaustive as of 30 July 2026):

| File | Line(s) | What changes |
|---|---|---|
| `ch11` | 43 | "a five-tier hierarchy" → six-tier |
| `ch11` | 46 | heading "## 11.2 Five tiers of evidence" → "Six tiers of evidence" |
| `ch11` | 48 | "The five tiers form a ladder" |
| `ch11` | 75–77 | "The fifth and highest tier, **independent adversarial scrutiny**" → the sixth and highest tier, adversarial scrutiny; new Tier 5 paragraph inserted before it |
| `ch11` | 80 | "A Tier 4 claim has passed Tiers 1 through 4" — verify still true; extend the example to Tier 5 if it reads better |
| `ch11` | 89–137 | **Figure 11.1** in full: title, standfirst, elements, flow, labels, annotations, caption, alt-text, infographic description. Six bars, not five |
| `ch11` | 148 | §11.3's externality list: "the reviewer at Tier 5 is independent by construction" → Tier 6, and a new clause for Tier 5 (the corroborating method is chosen for a different error structure, not merely a different run) |
| `ch11` | 196 | §11.4: "belongs to Tier 5" → Tier 6 |
| `ch11` | 407 | §11.7: "Tier 5 costs scarce expert attention" → Tier 6, plus a new sentence pricing Tier 5 |
| `ch11` | 433–441 | §11.8 checklist: the tier items are number-free and stand, but the "Tier matched to stakes" item gains a Tier 5 clause (task 11.6) |
| `ch13` | 26 | §13.1: "…to independent operational corroboration at the top" now names Tier 5 specifically rather than the top of the ladder. Reword so it does not misdescribe the top tier |
| `GLOSSARY.md` | Evidential tier entry | unchanged in substance; a new entry is added for independent-method corroboration (§7.2) |
| `OUTLINE.md` | §7, Ch. 11 synopsis | "a five-tier evidential hierarchy" → six-tier. Done by ai-editor in this pass |
| `REVISION-PLAN.md` | 103 | **deliberately untouched.** R1 is a closed record of what was done then; editing it would falsify the record |

No other file in the repository references a tier by number. `CLAUDE.md`, `FIGURES.md`, `STYLE.md` and `RESEARCH-INTEGRATION-PLAN.md` are clean.

### D4 — F3: the bounded-payoff thesis is stated canonically in **Chapter 4, new §4.4**

**Decision.** New **§4.4 "The frontier that does not move"**, inserted after §4.3 (the decision procedure) and before "What does not transfer to an instrument", which becomes **§4.5**.

**Why there.** §4.3 draws the four quadrants from checking cost against consequence. The thesis is that argument read forward in time, and it lands hardest immediately after the quadrants exist in the reader's head. Ch. 1 §1.4 supplies the premise but the reader has not yet met the procedure; Ch. 17 (now Ch. 18) §17.2 and §17.3 are the closing restatement, not the place to build an argument. No inbound reference to §4.4 exists, so the renumbering is free.

**Interaction with F7.** The thesis and the scope statement are the same boundary from two sides: the class of tasks worth delegating is bounded by checking cost (F3), and that class is largely the routine and semi-routine work surrounding science (F7). §4.4 must make the join explicit in one sentence and point at the scope statement in `ch00`; the scope statement points back at §4.4 for the mechanism. Neither restates the other.

**Cross-references, one clause each:** Ch. 1 §1.4, Ch. 15 §15.8, Ch. 16 §16.3, Ch. 18 §17.2 and §17.3.

### D5 — F7 splits: the scope statement goes to **front matter**, the exploratory treatment to **Chapter 3, new §3.7**

**Decision, part (a).** The scope statement is a positioning claim about the whole book, so it lives in `ch00`, in "Contribution statement and domain framing", as a short new movement. It is **[AUTHOR SIGN-OFF]**: ai-writer drafts it and attaches an `[AUTHOR: …]` marker asking the author to confirm the framing, because how the book presents its own reach is the author's call and not an agent's.

**Decision, part (b).** What governs exploratory work when a specification cannot yet be written becomes a new **§3.7 "When you cannot yet write a specification"**, placed after §3.6. Ch. 3 owns specification, so it owns the boundary of specification. §3.6's existing concession paragraph ("One concession is worth making…") is absorbed into §3.7 and removed from §3.6, so the idea has one home. Ch. 4 §4.1 gains a one-clause pointer.

### D6 — F4 becomes one new section, **Chapter 13 §13.9**, after "Reading the gallery"

**Decision.** New **§13.9 "Beyond the single workflow"**, placed *after* §13.8, with four sub-movements: correlated error across groups, homogenisation of the questions, deskilling and the supply of judgement, and automation bias in the human.

**Why not four new gallery modes.** The gallery's six modes are decided, and the chapter's own logic is that each recurs across the pattern chapters and each is caught by a *different local check*. The field-level failures are not caught by a local check at all. Adding them as modes seven to ten would break the chapter's stated organising principle and would misinform the reader about what a check can do.

**Why after §13.8 and not before.** §13.8 reads across the six modes and is the chapter's summing-up; interrupting it would damage it. §13.8's existing limitation ("it is not exhaustive") gains one forward sentence, and §13.9 opens by declaring itself a different register: not modes with checks, but consequences of adoption at scale, each with the honest statement of what a single group can and cannot do about it.

**One movement is split.** The *mechanism* of automation bias is canonical in §13.9(d); the *countermeasure* (seed defects into the human reviewer's queue; watch human-gate yield) is one paragraph in Ch. 11 §11.5, where the measurement apparatus lives. Cross-referenced both ways, derived in neither place twice.

---

## 3. Canonical-home map (binding under G5)

| New idea | Canonical home | Cross-referenced from (one clause or one sentence each) |
|---|---|---|
| The propose–dispose separation, general form | **Ch. 2 §2.6** | 4 §4.3 · 6 §6.3 · 8 §8.3 · 9 §9.3 · 10 §10.3 · 12 §12.4, §12.8 · 14 §14.3, §14.4 · 17 (new) |
| Second disanalogy: an agent's error distribution is non-stationary and its changes are invisible | **Ch. 1 §1.3** | 11 §11.5 · 12 §12.10 · 17 (new) |
| Calibration validity period and tier expiry | **Ch. 11 §11.5** | 11 §11.2 (in the tier definition) · 12 §12.4 · 12 §12.10 · 17 (new) §17.4 |
| Reproducible / replicable / **auditable**, and which one agentic work delivers | **Ch. 12 §12.4** | 9 §9.3 · 11 §11.2 · 14 §14.3 · 17 (new) · `GLOSSARY.md` |
| The bounded-payoff thesis (the delegable class does not grow as models improve) | **Ch. 4 §4.4** | 1 §1.4 · 15 §15.8 · 16 §16.3 · 18 §18.2, §18.3 |
| Scope statement: a governance treatment for the routine and semi-routine work surrounding science | **`ch00`, contribution statement** | 1 §1.5 · 3 §3.7 · 4 §4.4 |
| Governing exploratory work before a specification is possible | **Ch. 3 §3.7** | 4 §4.1 · 8 §8.4 |
| Independent-method corroboration as an evidential tier | **Ch. 11 §11.2** | 11 §11.3, §11.7 · 13 §13.1 · 14 §14.3 · `GLOSSARY.md` |
| Incident response, containment and erratum | **Ch. 12 §12.10** | 11 §11.5 · 12 §12.9, §12.11 · 17 (new) |
| Field-scale failures: correlated error, homogenisation, deskilling, automation bias | **Ch. 13 §13.9** | 10 §10.3 · 11 §11.5 · 16 §16.4 · 17 (new) §17.3 |
| Measuring the human gate (seeded defects for people; human-gate yield) | **Ch. 11 §11.5** | 12 §12.4 · 13 §13.9 |
| Induced demand for computation | **Ch. 16 §16.6** | 2 §2.7 · 4 §4.3 |
| Judging agentic work you did not produce | **new Ch. 17** | `ch00` · 1 §1.5 · 9 §9.4 · 11 §11.3 · 12 §12.4 · 16 §16.5 |

**Numbering, stated once so nothing below is ambiguous.** Only two chapters move: a new chapter takes **17**, and the old Chapter 17 becomes **18**. Chapters 1–16 keep their numbers and their filenames, including both case studies (Ch. 14, Ch. 15) and Ch. 16. Section numbers inside every existing file are unchanged except where §5 says otherwise (ch02, ch03, ch04, ch11, ch12, ch13).

---

## 4. What is NOT done in A1, and why

ai-reviewer checks these are absent.

- **No citation for automation bias, deskilling, complacency or skill atrophy.** The `/research` reports contain none. Task 13.4 argues from the book's own premises with an explicit confidence flag. Naddaf (2025), already cited in Ch. 16 §16.4, is about disclosure norms and career-stage splits and **must not be laundered** into evidence about deskilling.
- **No citation, and no named economic effect, for induced demand.** No source exists in the reports. Task 16.4 argues the mechanism plainly and quantifies nothing.
- **No cadence figure for model withdrawal.** "Models are withdrawn on roughly annual cycles" is a claim about the world with no source in the reports. Task 12.1 states the fact without a cadence and adds an `[AUTHOR: …]` for a lived anchor if the author has one.
- **No new evidence on field-level homogenisation.** Task 13.2 is explicitly a conjecture and says so.
- **No re-scan of the positioning claim.** Deferred; `ch00`'s existing caveat structure stands untouched (this was also R2's ruling).
- **No new sources at all.** A1 adds no reference the manuscript does not already carry, with the single exception of nothing. Every citation named below is already in a chapter's reference list. If a task seems to need a new source, flag it in the PR.
- **No change to the six failure modes of Ch. 13.** Decided; §13.9 is additive and declares itself a different register.
- **No change to the Part II chapter anatomy.** Decided (outline §9).
- **No edits to `REVISION-PLAN.md` or `RESEARCH-INTEGRATION-PLAN.md`.** They are records of closed passes.

---

## 5. Per-chapter instructions

Task IDs are what ai-reviewer reviews against, item by item. Every placement names an existing section or a new one with its number and title. Word budgets are prose only (G7).

---

### R.1 — The renumbering task (F8/D1) — do this **first**, as a single self-contained batch

Mechanical, exhaustive, and reviewed on its own before any prose lands.

1. `git mv manuscript/ch17-what-will-last.md manuscript/ch18-what-will-last.md`.
2. In that file: the `# Chapter 17 —` heading becomes `# Chapter 18 —`. All section headings `## 17.N` become `## 18.N`. All internal `§17.N` references become `§18.N`.
3. **Figure 17.1 → Figure 18.1** throughout that file: the bold in-text marker, the alt-text image link path, the caption, and every field of the brief (`id`, `caption`, and the render pointer). The image path becomes `../figures/figure-18-1.svg`.
4. Rename `figures/figure-17-1.svg` → `figures/figure-18-1.svg`. In `figures-src/f_ch13_17.py`, rename the entry to `figure-18-1` and rename the file to `figures-src/f_ch13_18.py`; update any manifest or import that names it.
5. Update the three inbound references to "Chapter 17": one each in `ch08`, `ch16` and the file's own self-reference. Grep `Chapter 17` book-wide afterwards; the only surviving hits must be references to the **new** Ch. 17.
6. Update `FURTHER-READING.md`'s Part V heading: "Part V — Adoption and policy (Chapters 9, 16–17)" → "(Chapters 9, 16–18)".
7. `GLOSSARY.md`: no entry cites Chapter 17. Verify, do not assume.
8. Confirm no reference of the form `§17.` survives outside `ch18`.

**Acceptance:** `grep -rn "figure-17-1\|Chapter 17\|§17\." manuscript/ figures/ figures-src/` returns only intended hits.

---

### ch00 — Front matter *(cap +280)*

- **0.1 — Scope statement (F7a).** §"Contribution statement and domain framing", inserted as a new paragraph immediately after the existing paragraph ending "…I would rather revise it than overstate it (moderate confidence)." **Insertion, ≈180 words.** It must establish, without apology: that every worked example in the book is routine or semi-routine work (quality-control passes, verification scores, calibration bookkeeping, manuscript assembly, reviewer responses); that this is a governance treatment for the work *surrounding* science rather than a treatment of doing science with agents; that a great deal of the best environmental science is abductive and opportunistic and is not governed by anything in these pages until a specification becomes possible; and that this is a boundary the book states rather than a gap it hopes goes unnoticed. Point once to Ch. 3 §3.7 for what governs exploratory work and once to Ch. 4 §4.4 for why the boundary sits where it does. Do **not** re-derive either. Close with `**[AUTHOR SIGN-OFF]** [AUTHOR: confirm this scope framing — it changes how the book presents its own reach, and the wording is yours to settle. If you would rather claim more or less than this, say so and the downstream cross-references in Chapters 3 and 4 follow.]`
- **0.2 — Reader routing to the new chapter (F8).** §"How to read this book", appended to the paragraph beginning "The five parts do not all deserve the same attention…". **Insertion, ≈70 words.** Establish: if the reader's position is reviewing, inheriting or being handed agentic work rather than building it, Chapter 17 is written for that position and can be read on its own. Name it plainly; no promise about the rest of the book.
- **0.3 — Parts sentence.** The Part V sentence in the same section gains the new chapter. **Rewrite, ≈30 words.**

---

### ch01 — Why agents, why now *(cap +215)*

- **1.1 — The second disanalogy (F1).** §1.3, appended to the passage that currently ends "…and why Chapter 13 is a gallery of failures rather than a footnote to the successes." **Insertion, ≈150 words.** This is the canonical home. It must establish four things in order: a physical sensor's error is stationary and characterisable, which is what makes a calibration certificate mean anything; an agent's error distribution is not stationary; the changes are invisible to the operator, because a hosted model can be revised without notice and the same specification can return different work on different runs; and therefore a calibration of an agent is a statement about a moment, not a standing property. Close by pointing once to Ch. 11 §11.5 for what follows from that. **No citation** — this is the book's own argument from material already in the chapter; carry a high-confidence flag. Do not re-derive plausible failure, which is two paragraphs above.
- **1.2 — Forward pointer to the thesis (F3).** §1.4, attached to the existing sentence "A better guide than apparent difficulty is the gap between what it costs to produce an answer and what it costs to check one." **Insertion, ≈40 words, one or two sentences.** Establish only that this asymmetry has a consequence for how far delegation can ever reach, and that Chapter 4 draws it. Do **not** state the thesis here; that is §4.4's job and stating it twice breaches G5.
- **1.3 — Part V sentence (F8).** §1.5, the sentence beginning "Part V is about adoption in a real research group…". **Rewrite, ≈25 words.** Add the new chapter: adoption when the group is yours, and judgement when the work is someone else's.

---

### ch02 — Anatomy of an agent *(cap +560)*

- **2.1 — New section §2.6 (F6/D2).** **Insertion of a new section**, placed after §2.5 and before the cost model. Heading: `## 2.6 Propose and dispose: where authority sits`. **≈550 words.**
  It must, in this order: lead with the concrete case per `STYLE.md` §1 (an agent asked to clean a gauge record, and the difference between it flagging a suspect value and it overwriting one); state the general principle in one sentence the reader can carry — *the agent proposes; something the agent does not control disposes*; name the three classes of disposer and what each is good for (a deterministic rule, where the criterion can be written as code; a human decision, where the criterion is judgement; an external source of truth, where the criterion is a fact the agent cannot manufacture, such as a test suite or a reference dataset); state what the separation buys, which is that the failure mode the book is built around, fluent output uncorrelated with correctness, cannot reach the record because the model was never given the authority to write to it; state the one thing it does not buy, which is protection against a badly designed disposer, since a rule set that admits the wrong thing admits it every time; and close by naming, in a single sentence with cross-references and no re-derivation, the five places in the book where this same separation appears in local costume: Ch. 6 §6.3, Ch. 8 §8.3, Ch. 9 §9.3, Ch. 12 §12.8 and Ch. 14 §14.3.
  **No new citation.** Anthropic (2024), already cited in §2.5, may be reused if it earns the sentence; nothing else.
  Confidence: high in the principle.
- **2.2 — Renumber the cost model.** `## 2.6 A plain cost model` → `## 2.7`. **Relocation of a heading only; no prose change beyond the number.**
- **2.3 — Roadmap sentence.** Line 30 of the chapter currently reads "…then how many such steps compose into an orchestrated process (§2.5), before the chapter closes on what all of this costs (§2.6)." **Rewrite, ≈25 words.** It must now name §2.6 (authority) and §2.7 (cost) in sequence.
- **2.4 — Figure (F6).** New **Figure 2.4**, specified in §6.1 below. It goes inside §2.6.
- **2.5 — Cost-model cross-reference (F9).** §2.7, attached to the tool-and-compute-cost sentence that already forwards to Ch. 16. **Insertion, ≈25 words.** One clause noting that the aggregate a workflow spends includes work that would not have been done at all had it been expensive, and that Ch. 16 §16.6 counts it. No argument here; §16.6 owns it.

---

### ch03 — Specifying work for agents *(cap +460)*

- **3.1 — New section §3.7 (F7b/D5).** **Insertion of a new section** after §3.6. Heading: `## 3.7 When you cannot yet write a specification`. **≈430 words.**
  It must establish: that a large part of good environmental science begins with something odd in a record and no statable objective, so the specification discipline has nothing to bite on yet; that this is not a failure of the discipline but a boundary of it, and pretending otherwise produces the second error the chapter warns against, which is a premature specification that fixes the wrong target; what *does* govern the exploratory phase, and this is the constructive core of the section — a bounded budget of attempts and time rather than acceptance criteria; a record of what was tried and what it showed, kept as it happens rather than reconstructed; the standing rule that nothing found in exploration enters the evidential chain until it has been re-derived under a specification (which is exactly the hypothesis-provenance gate of Ch. 8 §8.4, cross-referenced, not re-derived); and the judgement call of when exploration has yielded enough to specify, which is a real skill the book can name but not supply.
  Close with one sentence connecting to the scope statement in the front matter: the book governs the half of the work that can be specified, and this section says what stands in for governance in the other half.
  **No new citation.** The existing §3.6 concession paragraph ("One concession is worth making. For genuinely exploratory work, where the objective is not yet knowable…") is **deleted from §3.6** and its content absorbed here, per G5.
  Add `[AUTHOR: an exploratory episode of your own that could not have been specified in advance, and what you kept a record of while it was running — this section is asserting a practice, and one lived instance would make it a description instead.]`
- **3.2 — §3.6 deletion.** **Deletion, ≈45 words.** Remove the concession paragraph named above. §3.6 then ends on "…rather than never being made at all", which is a stronger close.

---

### ch04 — The scientist's stance *(cap +640)*

- **4.1 — New section §4.4 (F3/D4).** **Insertion of a new section** after §4.3 and before "What does not transfer to an instrument". Heading: `## 4.4 The frontier that does not move`. **≈600 words.**
  This is the book's strongest thesis and it must be argued, not asserted. Required movements, in order:
  (i) Lead from §4.3's quadrants: both questions that decide delegation are properties of the *task* — what it costs to check the output, and what a wrong output costs. Neither is a property of the model.
  (ii) State what capability progress does: it widens the generation side of the asymmetry. A better model produces more, faster, at higher quality, across more task types.
  (iii) State what it does not do: it leaves the checking side where it was. Checking cost is set by the task's structure — whether a reference exists, whether a rule can decide, whether the answer is interpretive — and no model improvement changes that structure.
  (iv) Draw the conclusion plainly: the class of scientific tasks where agents pay off is bounded by checking cost, so **that class does not grow as models improve**, and the frontier of safe delegation moves far less than the capability curve suggests.
  (v) Handle the obvious objection honestly, because it is a real one: better models *do* make some previously expensive checks cheap, by producing outputs in checkable forms (structured, tested, referenced) rather than in prose. That widens the class at the margin. The claim is that the widening is second-order against the capability curve, not that the boundary is fixed. Give this its own two or three sentences and flag the confidence as moderate-to-high rather than high.
  (vi) State the consequence for the reader's posture: this converts "adopt this, carefully" into "adopt this here, for these bounded reasons, and here is why the boundary will not move much".
  (vii) One sentence joining F7: the tasks on the cheap-to-check side are largely the routine and semi-routine work surrounding science, which is what the front matter's scope statement says the book governs. Cross-reference; do not restate.
  **Citations:** METR (2026) and Anthropic Institute (2026) are both already in Ch. 1 and Ch. 18 and may be reused in movement (ii) as the measured form of the capability curve, with their self-reported and interested caveats carried per G2. Nothing new.
- **4.2 — Renumber.** `## 4.4 What does not transfer to an instrument` → `## 4.5`. **Relocation of a heading only.**
- **4.3 — Cross-reference in §4.3 (F6).** Attached to the four-quadrant paragraph. **Insertion, ≈30 words.** One clause: the two middle quadrants (agent behind a mandatory gate; agent drafts and a human checks) are both instances of the propose–dispose separation of Ch. 2 §2.6, differing only in who or what disposes.
- **4.4 — Cross-reference in §4.1 (F7).** **Insertion, ≈25 words.** One clause after "So you end up deciding this one task at a time, not one phase at a time.": and where the task is not yet statable at all, Ch. 3 §3.7 says what governs instead.
- **4.5 — Figure.** **None.** Figure 4.1's decision flowchart already carries §4.3, and §4.4 is an argument about time rather than a structure with parts. Adding a figure here would be decoration.

---

### ch05 — Evidence and literature synthesis *(cap +30)*

- **5.1 — Cross-reference only (F8).** §5.3, in the citation-verification-gate discussion. **Insertion, ≈30 words.** One clause: the same gate is what a reviewer on the outside should ask whether the authors ran, and Ch. 17 says what else they are entitled to ask for.
- No other change. The chapter's evidence layer is current after R2.

---

### ch06 — Data acquisition and quality control *(net −40)*

- **6.1 — Cut and cross-reference (F6).** §6.3. **Deletion plus insertion, net ≈ −60.** Delete the general restatement sentence beginning "So the agent's contribution is confined to the two things it does well…" through "…stay with deterministic code and, above it, with the accountable scientist." Replace with one clause tying the section to Ch. 2 §2.6: this is the propose–dispose separation with a deterministic rule as the disposer, and the chapter's job is the instance, not the principle. The paragraph's opening two sentences ("The organising principle is a strict separation of authority…") stay: they are the section's own claim and Figure 6.1 depends on them.
- **6.2 — Validity cross-reference (F1).** §6.6, verification checklist. **Insertion, ≈20 words.** One clause on the existing "Reproducible rerun" item: the rule-set version is what makes the rerun reproducible, and the agent's contribution is not part of that guarantee (Ch. 12 §12.4).

---

### ch07 — Coding and pipeline agents *(no change)*

Nothing in F1–F9 lands here. The chapter's reviewer-independence material is Ch. 10's canonical territory and its benchmark-audit evidence was updated in R2. **Do not touch.**

---

### ch08 — Model orchestration and experimentation *(net −45)*

- **8.1 — Cut and cross-reference (F6).** §8.3. **Deletion plus insertion, net ≈ −70.** Delete the paragraph beginning "This is not timidity about model capability." through "…are expensive to verify and fail by imitating competence." Replace with one sentence: the monitor-and-log boundary is the propose–dispose separation of Ch. 2 §2.6 with the scientist as the disposer, and what follows is where this chapter draws the line rather than why the line exists. The Boiko et al. (2023) contrast that follows, and the Lopez-Gomez et al. (2026) in-domain demonstration, both stay in full — they are chapter-specific evidence, not re-derivation.
- **8.2 — Cross-reference to §3.7 (F7).** §8.4, attached to the passage on what a generated hypothesis may and may not do. **Insertion, ≈25 words.** One clause: the exploratory compartment here is the mechanism §3.7 relies on when a task cannot yet be specified at all.

---

### ch09 — From results to manuscript *(net +20)*

- **9.1 — Cut and cross-reference (F6).** §9.3. **Deletion plus insertion, net ≈ −80.** Delete the general operator-not-author derivation: the sentences from "An assembly agent sits over that arrangement as an operator, not an author." through "…the agent's outputs are proposals you accept, edit or reject at an explicit gate", and the general sentence "The discipline that prevents that is simple: you remain the source of every claim…". Replace with a compressed version naming the separation once with a cross-reference to Ch. 2 §2.6, and keep every manuscript-specific clause: what the agent may draft (methods from a specification, data-availability from provenance, documentation from logs), what it must not do (originate claims, decide what results establish), and the read-every-sentence rule.
- **9.2 — What a methods section can honestly claim (F2).** §9.3, appended to the paragraph on provenance doing double duty. **Insertion, ≈100 words.** It must establish: a methods section reading "quality-controlled under specification X by an agentic workflow" tells a reader what was done and does not let them repeat it, because the model behind it may no longer exist and the same specification may not return the same work; the honest form names the specification, the checks that gated it, and the tier reached, and says the agentic step is auditable rather than reproducible; and the deterministic components of the workflow are separately reproducible and should be identified as such. Cross-reference Ch. 12 §12.4 for the distinction itself. **Do not define reproducibility here** — that is §12.4's canonical job.
- **9.3 — Cross-reference to the new chapter (F8).** §9.4, at the point where the policy landscape's reviewer-side rules are discussed. **Insertion, ≈25 words.** One clause: the chapter treats the author's side of that asymmetry, and Ch. 17 treats the reviewer's.

---

### ch10 — Multi-agent workflows *(cap +60)*

- **10.1 — Forward reference to field-scale correlation (F4a).** §10.3, attached to the sentence "…so genuine independence needs model diversity, not merely a fresh context window." **Insertion, ≈60 words, two sentences.** It must establish: the same argument scales up, and at field scale it is a different and larger problem, because if most groups run their reviewer agents on a small number of base models the field's verification errors correlate; and that the consequence for independent replication is developed in Ch. 13 §13.9. **Do not develop it here.** Do not add a citation; the mechanism rests on Wataoka et al. (2024) and Norman et al. (2026), both already cited in this section.
- Do not touch §10.4, §10.5 or §10.6. The ai-reviewer placement note at line 71 stays exactly as it is; it is a record.

---

### ch11 — Verification and evaluation *(cap +1,090)*

The heaviest chapter in A1, and the one with the most renumbering exposure. Five tasks.

- **11.1 — The new tier and the category note (F5/D3).** §11.2. **Insertion plus renumbering, ≈420 words.**
  (a) **New Tier 5 paragraph**, inserted after the Tier 4 paragraph and before the top tier. It must establish: what independent-method corroboration is (a second determination of the same quantity by a method with a different error structure, agreeing within stated uncertainty); why it belongs above Tier 4 (out-of-sample generalisation moves the regime but keeps the measurement chain; corroboration changes the chain); what it looks like concretely, in this readership's own vocabulary (satellite against gauge, two retrievals with different error structures, a physical model against an empirical one); what it means for an agentic workflow specifically (a claim re-established by a route that shares neither the model nor the pipeline, for example a deterministic recomputation, a different data source, or a manual redo of a sample); and the honest limit — agreement between two methods that share a hidden dependency is not corroboration, so the independence of the error structures is the thing to argue for, not assume.
  Name the two instances already in the book, one clause each: §11.3's operational re-verification of a data-driven weather model against both analyses and independent station observations, and Ch. 1 §1.2's two independent measurement methods converging on the same doubling trend, which that section already calls "exactly the corroboration between measurements this book argues for throughout". This tier is what that sentence was pointing at.
  (b) **Renumber and rename the top tier**: "The fifth and highest tier, **independent adversarial scrutiny**" becomes the sixth and highest tier, **adversarial scrutiny**.
  (c) **New category paragraph**, ≈110 words, placed after the top tier and before "The tiers are cumulative." It must state openly: Tiers 1 to 5 are named for the check that establishes them; Tier 6 is named for what the checker does, which makes it the odd one; the strength of a Tier 6 claim therefore depends on a property of the checker, namely independence, and that property is a measured quantity, not a declared one (§11.5); so the least reproducible instrument in the chapter sits at the top of the ladder, and that is a real tension the chapter does not resolve by wishing. Confidence: high that the tension is real; moderate that Tier 6 belongs at the top despite it, with the reason given (it is the only tier offering protection against errors no pre-specified check anticipated).
  (d) Update every site in the D3 table for this chapter: lines 43, 46, 48, 80, 148, 196, 407.
- **11.2 — Reliability's epistemic consequence (F2).** §11.2, appended to the pass^k paragraph ending "A duty cycle is a repeated trial, and reliability is what fails first." **Insertion, ≈120 words.** It must establish: run-to-run variation is not only a reliability problem but an evidential one, because a claim established on one run is a claim about that run; a workflow that passes a tier on Monday and fails it on Friday has not established the tier, it has sampled it; and the practical rule is that a tier claim on a workflow you intend to run repeatedly is established on repeated runs or it is not established. Point once to Ch. 12 §12.4 for what this does to reproducibility. Cite nothing new; Yao et al. (2024) is already the paragraph's source.
- **11.3 — Calibration validity and tier expiry (F1).** §11.5, extending the paragraph that currently ends "Models drift, prompts go stale, and the work moves." **Insertion, ≈280 words.** This is the canonical home. It must establish, in order:
  (i) The trigger list has a hole. "After any model change" presupposes you know a model changed, and frequently you will not, because a hosted model can be revised without notice (Ch. 1 §1.3).
  (ii) What every real instrument certificate carries and this book's tiers do not: a **validity period**. A calibration is a statement about a moment.
  (iii) The rule: a gate calibration is recorded with the date it was made and a stated validity window, chosen by the group; past that window the calibration is expired, not merely old, and a tier claim resting on it drops to the highest tier still supported by an unexpired check.
  (iv) How to choose the window when the trigger events are invisible: shorten it, and add a cheap standing detector — a small fixed set of seeded cases re-run on a schedule, whose results changing is itself the signal that something upstream moved. This is the constructive answer and it must be concrete enough to implement.
  (v) The honest limit: this detects change, it does not attribute it, and a group cannot distinguish a model revision from a data-regime drift without controlling one of them.
  Add a new info-box per G6: `> **Definition — Calibration validity.** …` establishing that a gate's measured miss rate is a reading taken on a date, that it carries a window past which it is not evidence, and that a claim gated by an expired calibration is a claim whose evidence has quietly lapsed.
  Point once to Ch. 12 §12.4 (record the window in provenance) and Ch. 12 §12.10 (what to do when an expired calibration turns out to have been wrong all along). **No new citation.**
- **11.4 — Measuring the human gate (F4d countermeasure).** §11.5, appended to the yield-diagnostic paragraph. **Insertion, ≈130 words.** It must establish: every method in this section has been applied to agent gates, and the gate most likely to be failing is the human one; seeded-defect testing works on people too, and a reviewer whose queue occasionally contains a planted fault is a reviewer whose catch rate is measurable; yield applies identically, so a human approver who has not returned anything in three months is the same signal as a citation gate that has stopped rejecting; and the finding this addresses is that a rubber-stamp review leaves the same record as a searching one (Ch. 12 §12.4), so the record alone cannot tell you which you have. Cross-reference Ch. 13 §13.9 for why this failure is the commonest one. Flag the obvious institutional difficulty in half a sentence: seeding a colleague's queue is a thing to agree in advance, not to spring. `[AUTHOR: whether you have ever seeded a human reviewer's queue, agreed in advance, and what it showed.]` **No citation.**
- **11.5 — Externality clause for the new tier (F5).** §11.3, in the list at line 148. **Insertion, ≈35 words.** One clause between the Tier 4 and Tier 6 entries: the corroborating method at Tier 5 is chosen for a different error structure, not merely a different run, and the independence to argue for is between the error structures rather than between the operators.
- **11.6 — Checklist and §11.7 (F5, F1).** **Insertions, ≈110 words total.**
  (a) §11.7, the cost paragraph: one sentence pricing Tier 5 between Tiers 4 and 6 — it costs whatever a second, structurally different determination costs, which in the environmental sciences is often an existing dataset rather than new work, making it cheaper than it sounds and the best value on the ladder.
  (b) §11.8, the "Every gate's false-negative rate measured" item: extend with a validity clause — each calibration carries its date and validity window, and no claim rests on an expired one.
  (c) §11.8, the "Tier matched to stakes" item: extend with one clause naming Tier 5 as the tier to reach for when a published quantitative result is at stake and a second determination is available.
- **11.7 — Cross-reference to the new chapter (F8).** §11.3, appended to the passage on re-verifying a claim on your own data. **Insertion, ≈30 words.** One clause: this is also what a reviewer of someone else's agentic result is entitled to ask whether the authors did, and Ch. 17 turns it into questions.
- **11.8 — Figure 11.1 (F5).** Re-brief in full; §6.2 below.

---

### ch12 — Provenance, governance and security *(cap +1,020, net after cut)*

- **12.1 — The reproducibility correction and the three-way distinction (F2).** §12.4. **Rewrite plus insertion, ≈380 words.** This is the canonical home.
  **The offending sentence, to be removed:**
  > "Captured together, these make a result reproducible in the strong sense, not merely re-runnable but explicable, and they convert the vague reassurance that a workflow was "carefully done" into a record a reviewer, an auditor or a successor can interrogate."
  **What replaces it** must establish, in order: that the second half of that sentence is right and the first half was wrong, stated without hedging — explicable is the *weaker* property, not the stronger one, and the ordering was inverted; the three-way distinction, each defined in the reader's own vocabulary — **reproducibility** (run it again, same inputs, same answer), **replicability** (an independent party does it again by their own route and gets a compatible answer), **auditability** (reconstruct and defend what was done, without being able to repeat it); which of the three an agentic workflow delivers, which is the third; why — the same specification and inputs can return different work on different runs (Ch. 11 §11.2), and the model behind a result may be withdrawn, after which the workflow cannot be re-run at all; and the constructive answer, which the book already holds and has never connected to the question: the deterministic components *are* reproducible, and in an architecture where the agent proposes and a deterministic rule disposes (Ch. 2 §2.6), the reproducible element is the one holding the authority. Name Ch. 6's propose–dispose and Ch. 14 §14.3's deterministic core as the two worked instances, one clause each.
  Close on the positioning point, in the book's own voice: stating this plainly is a credibility gain rather than a loss, because a readership that has lived through the reproducibility crisis will find the hole in about a minute otherwise.
  **Also fix, in the same task:** the info-box "**Definition — Audit trail**" at line 76, whose closing clause "so a result is not just re-runnable but explicable" carries the same inversion. Rewrite the closing clause so it claims auditability and nothing more.
  **Add a new info-box** per G6, immediately after the distinction is drawn: `> **Definition — Auditability.**` establishing that it is the property of being reconstructable and defensible after the fact, that it is what a provenance record delivers, and that it is weaker than reproducibility and worth having anyway.
  **Say nothing about model-withdrawal cadence.** Per §4, no source supports a figure. Add `[AUTHOR: if you have had a workflow become un-rerunnable because the model behind it was withdrawn, one sentence of that would anchor this better than the general statement.]`
  **No new citation.**
- **12.2 — Validity window in the audit trail (F1).** §12.4, in the list of elements a scientific audit trail must capture. **Insertion, ≈70 words.** Add one element to the list: the calibration state of every gate the artefact passed, meaning the gate's measured miss rate, the date of that measurement and its validity window (Ch. 11 §11.5). Establish in one further sentence why it belongs there: without it, a provenance record says a gate passed the work and cannot say whether the gate was known to be working at the time.
- **12.3 — Cross-references (F6, F8, F4d).** §12.4 and §12.8. **Insertions, ≈70 words total, plus one cut.**
  (a) §12.8: **delete ≈70 words** — the general statement of why a proposed consequential action waits on a human (the trust-boundary paragraph's derivation), replacing it with one clause pointing to Ch. 2 §2.6. Everything security-specific (input validation at the inward crossing, least privilege at the tools, the human gate at the outward crossing, the boundary as the artefact IT asks for) stays in full.
  (b) §12.4: on the existing limitation sentence "a rubber-stamp review leaves the same record as a searching one", add one clause pointing to Ch. 11 §11.5 for how to measure it and Ch. 13 §13.9 for why it is the commonest failure. Do **not** expand the concession here; it now has a canonical home.
  (c) §12.4: one clause noting that these same four records are what a reviewer on the outside should be asking to see, and Ch. 17 turns them into questions.
- **12.4 — New section §12.10 (F1).** **Insertion of a new section**, placed after §12.9 and before the verification checklist. Heading: `## 12.10 When a gate is found to have been wrong`. **≈620 words.** This is the canonical home for incident response and erratum, and the finding is right that a governance treatment with only a preventive half is incomplete.
  Required movements, in order:
  (i) Lead with the concrete case, per `STYLE.md` §1: a gate calibration is repeated and this time the gate misses a fault class it caught before. Everything that passed through it since the last calibration is now of unknown status. For a book grounded in operational forecasting, the hour after that discovery is where the governance is actually tested.
  (ii) **Detection.** How you find out at all: a re-calibration, a yield collapse, a downstream user's complaint, a corroborating method disagreeing (Ch. 11 §11.5, §11.2). Name the uncomfortable one plainly — most of the time you find out because someone else noticed.
  (iii) **Containment.** Stop the workflow before diagnosing it. Quarantine outputs rather than deleting them, because the wrong outputs are the evidence.
  (iv) **Scope assessment.** This is where the book's apparatus pays off and the section must say so concretely: the audit trail answers which artefacts passed through the affected gate and when, the reviewer-coverage record answers which of them had a second check that might have caught it independently, and the tier record answers which claims were resting on the gate at all. A group without those records cannot bound the damage and has to treat everything since the last known-good calibration as suspect.
  (v) **Notification.** Who is told, in what order, and on what basis: collaborators whose work sits downstream, partners who supplied data under conditions, and the operational customer if a decision was informed. State the principle rather than a procedure, since the thresholds are institutional.
  (vi) **Correcting the record.** Metrology has recall; science has errata, a corrected dataset version, or a note attached to the record. Say plainly that these are slower and weaker instruments than a recall, that a published result gated by a check now known to have been miscalibrated is the hardest case in the chapter, and that the decision to correct the record is the author's and not the workflow's.
  (vii) **What the workflow changes afterwards.** Every incident is a case for the evaluation set (Ch. 11 §11.4) and an entry in the failure log; a gate that has failed once has a shorter validity window than it did.
  (viii) **The honest limit**, stated as such: this section describes a response the book believes is right and cannot claim is standard, because no established practice exists for retracting an agentic result. Confidence: moderate, and say so.
  Hook it explicitly to §12.9's existing question "Who is accountable for its actions, and how is a mistake detected, contained and reversed?" — that question has been asked for a section and a half without an answer.
  Add `[AUTHOR: a gate of yours that turned out to have been miscalibrated, or the nearest thing to it — what you found, how far back it reached, and what you had to tell whom. This section is the one in the chapter most obviously missing lived material.]`
  **No new citation.** The Five Eyes advisory (2026), already cited in §12.9, may be reused for the "name a specific human as accountable before deployment" recommendation if it earns its sentence.
- **12.5 — Renumber.** `## 12.10 Verification checklist` → `## 12.11`; `## 12.11 Repository pointer` → `## 12.12`. No inbound reference to either exists (verified). **Relocation of headings only.**
- **12.6 — Checklist item (F1).** §12.11 (post-renumber), extending the existing "Accountability and recovery are named" item. **Insertion, ≈50 words.** Extend it so it is checkable rather than aspirational: the record shows not only that a human is accountable but that the group has a stated response to a gate found to have been wrong, including how the affected artefacts would be identified from the audit trail (§12.10).

---

### ch13 — The failure gallery *(cap +1,190)*

- **13.1 — Forward sentence in §13.8.** Appended to the "not exhaustive" limitation. **Insertion, ≈40 words.** One or two sentences establishing that the six modes share a shape — one workflow, one wrong artefact, one local check — and that a different kind of failure appears only when a whole field adopts the patterns, which the next section takes up.
- **13.2 — New section §13.9 (F4/D6).** **Insertion of a new section** after §13.8. Heading: `## 13.9 Beyond the single workflow`. **≈1,150 words total across four movements plus a short opening and close.**
  **Opening, ≈100 words.** Declare the register change explicitly: these are not modes with checks, because no check a single group can run catches them. They are consequences of adoption at scale, and what a group can do about each is smaller and less satisfying than a gate. Say that plainly rather than pretending otherwise.
  **(a) Correlated error across groups, ≈300 words.** The domain-native argument, which is the strongest thing in this section. Establish: Ch. 10 §10.3's independence argument scaled to a field; if most groups run their independent-reviewer agent on one of a small number of base models, the field's verification errors correlate; independent replication is science's actual error-correction mechanism, and it stops working when the replications share a failure mode; and this readership already knows the failure under another name — correlated model error in a multi-model ensemble, where nominal spread overstates real independence, so the ensemble looks better constrained than it is. What a group can do: choose reviewer models against what the field is using rather than for convenience, and record which model family reviewed what, so the correlation is at least visible in the record (Ch. 12 §12.4). Confidence: high in the mechanism, moderate in the scale, since nobody has measured how concentrated the field's model use actually is. **No new citation** — the mechanism rests on Wataoka et al. (2024) and Norman et al. (2026), both already in this chapter's neighbouring chapters; cite neither here, cross-reference §10.3 instead, per G5.
  **(b) Homogenisation of the questions, ≈250 words.** Establish: Ch. 8 §8.4 gates hypothesis laundering inside one workflow, and says nothing about what happens to a field's distribution of hypotheses when a generation of scientists brainstorms against the same few models trained on the same corpus; divergence of ideas is a resource, and the question of whether this technology consumes it is open. **Name this as a conjecture, explicitly.** Low-to-moderate confidence, no evidence either way in the reports, and it is stated because the reader should be thinking about it, not because the book knows the answer. What a group can do: notice when every hypothesis in a discussion arrived by the same route, and keep at least one route that does not go through a model. `[AUTHOR: whether you have seen this in practice, or think it is overstated — this is the movement in the section most in need of your judgement.]`
  **(c) Deskilling and the supply of judgement, ≈300 words.** Establish: the whole verification-first stance depends on expert judgement, and the book has nowhere said where that judgement comes from; Ch. 16 §16.4 says the roles need skills "largely those a good empirical scientist already has", which assumes a continuing supply of scientists who acquired those skills by doing the work an agent now does; a doctoral researcher who never hand-reconciles a gauge network may not develop the intuition that lets them tell a real signal from a sensor fault, which is exactly the judgement the propose–dispose separation reserves for them (Ch. 2 §2.6); so a group leader deciding what a doctoral researcher spends three years on is making a decision about the group's future capacity to verify, not only about this year's throughput. What a group can do: name which judgements the group intends to keep, and protect the work that builds them even where an agent would be faster. Confidence: moderate, and label it as the book's argument rather than a measured effect — no source in the reports supports it, and none is offered.
  **(d) Automation bias in the human, ≈300 words.** Establish: the book's model of the human throughout is a tireless sceptical verifier, and real people under deadline approve work that looks right; the gallery has a mode for the *agent* being over-agreeable (§13.5) and none for the *person* being over-agreeable, which is the commoner failure; every gate in this book runs through a person at some point, so this is the failure that defeats all of them; and it is invisible in the record, because a rubber-stamp review and a searching one leave identical traces (Ch. 12 §12.4). What a group can do, and this is the constructive half: measure it, exactly as any other gate is measured (Ch. 11 §11.5) — seeded defects in the human reviewer's queue, agreed in advance, and yield watched on human approvals as well as automated ones. Also design against it: a gate that requires the reviewer to state what they checked, rather than to click approve, costs seconds and makes the cheap approval visibly cheap. Confidence: high that the mechanism is real, moderate that the countermeasures work, since neither has been measured here.
  **Close, ≈80 words.** One paragraph: what these four have in common is that the check has to sit outside the group, not merely outside the workflow, and the institution that has historically played that role is peer review — which is where Ch. 17 picks up. This is the join between F4 and F8 and it should be made once, here.
- **13.3 — Tier wording (F5).** §13.1, line 26: "…which runs from cheap mechanical confirmation at the base to independent operational corroboration at the top." **Rewrite, ≈25 words.** After D3, independent corroboration is Tier 5 and the top is adversarial scrutiny. Reword so the sentence describes the six-tier ladder correctly.

---

### ch14 — Verification under constraint *(net −100; number and filename unchanged)*

- **14.1 — Cut and cross-reference (F6).** §14.3, the paragraph beginning "Why hold verification deterministic while allowing a language model elsewhere in the toolkit?" **Deletion plus insertion, net ≈ −90.** Delete the general half ("The argument is Chapter 11's, and it is worth restating concretely" through the general statement of plausible failure), replace with one clause naming Ch. 2 §2.6 and Ch. 11 §11.3. Keep the measurement-specific half in full: a verification result is a measurement, a measurement whose value could change is not a measurement, and the evidential weight it carries depends on being a fixed function of the data. Keep the Ben Bouallègue et al. (2024) passage untouched.
- **14.2 — Cut and cross-reference (F6).** §14.4, the paragraph beginning "The safeguard that keeps the tutoring tier from quietly becoming a decision-maker…". **Deletion plus insertion, net ≈ −50.** Delete the sentence re-deriving least privilege as a principle ("This is the least-privilege principle of Chapter 12 applied to an internal component: the model is granted exactly the access its explanatory job requires and no more…"), replace with a clause naming Ch. 2 §2.6 and Ch. 12 §12.8. Keep the architectural specifics (read-only access, no write path, a suggestion executed by the core rather than accepted from the model) in full.
- **14.3 — Tier 5 cross-reference (F5).** §14.3, appended to the Ben Bouallègue passage. **Insertion, ≈30 words.** One clause: this is independent-method corroboration, Tier 5 of Ch. 11 §11.2, and it is the strongest evidential move the chapter makes.
- **14.4 — Reproducibility cross-reference (F2).** §14.3, in the same neighbourhood. **Insertion, ≈25 words.** One clause: the deterministic core is the reproducible part of this toolkit in the strict sense of Ch. 12 §12.4, and the tutoring tier is not.

---

### ch15 — Governing a modelling workflow end to end *(cap +70)*

- **15.1 — The thesis demonstrated (F3).** §15.8, appended after the two limitations and before the closing sentence. **Insertion, ≈70 words.** The review asks the author to test whether both case studies sit in the cheap-to-check quadrant. They do: a verification score is checkable against a fixed algorithm, and a gated modelling stage is checkable against acceptance criteria fixed in advance. Establish that this is not a coincidence but the thesis of Ch. 4 §4.4 in operation — these workflows were governable because checking them was cheap — and that a reader looking for where the apparatus would *not* have worked should look at the tasks the specification deliberately left with the human. Cross-reference §4.4; do not restate it. `[AUTHOR: confirm that this reading is right for your two cases, and name one task in this workflow that was expensive to check and therefore never delegated — that example is worth more than the general claim.]`

---

### ch16 — Starting in your own group *(cap +460)*

- **16.1 — Verification cost does not fall (F3).** §16.3, attached to the sentence "The implication for a group's budget is that inference is the line item to worry about least and verification the line item to protect most…". **Insertion, ≈80 words.** Establish: this is not a temporary state of the technology, and the reason matters for a five-year budget — the checking side of the asymmetry is a property of the task, so it does not fall as models improve (Ch. 4 §4.4); a budget built on the assumption that verification cost is a transitional expense will be wrong in the same direction every year. Cross-reference; do not re-derive the thesis.
- **16.2 — Deskilling as a planning assumption (F4c).** §16.4, appended to the paragraph beginning "The skills these roles require are largely those a good empirical scientist already has…". **Insertion, ≈120 words.** Establish: that sentence assumes a continuing supply of people who acquired those skills by doing the work an agent now does, and that assumption is worth making explicit because a group leader is the person who decides whether it holds; the decision about what a doctoral researcher spends three years on is a decision about the group's future capacity to verify; and the practical form of it is to name which judgements the group intends to keep in-house and protect the work that builds them. Cross-reference Ch. 13 §13.9 for the argument; state the planning consequence here, which is what a Part V reader needs. **No citation** — do not attach Naddaf (2025) to this, per §4.
- **16.3 — Cross-reference to the new chapter (F8).** §16.5, in the institutional-considerations passage. **Insertion, ≈30 words.** One clause: much of what this section assumes a group can decide is decided elsewhere when the system arrives from the institution or a vendor, and Ch. 17 takes that case.
- **16.4 — Induced demand (F9).** §16.6. **Rewrite plus insertion, ≈250 words.** The passage currently says "Three considerations follow, all directional and all robust to the churn in the underlying figures." It becomes four.
  The new fourth consideration must establish: the counterfactual argument in the third consideration counts displaced computation and does not count induced computation, which is the harder half; agents create workflows that would never have been run at all, because they were not worth a person's time and now cost almost nothing — the parameter sweep run because running it is cheap, the reprocessing repeated because repeating it is easy, the loop that produces nothing and is left running; the aggregate footprint of a research programme can rise even where every individual workflow displaced something more expensive; and the honest accounting question is therefore not only "what did this replace?" but "would this have been run at all?", which is a specification question (Ch. 3) before it is an energy question.
  Absorb the existing clause "and the discipline of not running loops that produce nothing" from the closing paragraph into this consideration, so the idea appears once (G5), and adjust that closing paragraph accordingly.
  **No citation, no named economic effect, no quantification** (see §4). Confidence: high in the mechanism, low in any magnitude, and say the second part explicitly — this is a mechanism the section names because a climate-literate reader will otherwise notice it missing, not one the book can size.
  `[AUTHOR: whether you have watched induced demand happen in your own group — a sweep or a rerun that existed only because it became cheap — and roughly what it cost.]`
- **16.5 — Update the "three considerations" sentence.** **Rewrite, ≈10 words.** Three becomes four.

---

### ch17 (NEW) — On the receiving end *(≈3,500 words)*

**File:** `manuscript/ch17-on-the-receiving-end.md`. **Status header:** `draft r1 · voice v5.0 …`, conventions block copied from `ch16`, plus one integrity line: *the questions and checklists here are proposals for practice, not a report of established practice; no claim is made that any community currently asks these questions.*

**[AUTHOR SIGN-OFF]** on the chapter title. Alternative on record, not chosen: "Reviewing work you did not produce".

The chapter's governing move: every earlier chapter addresses the accountable principal, the person who writes the specification and sets the gates. This one addresses the same reader in the position they will more often occupy — without that authority. It reuses the book's apparatus rather than building new apparatus, and it must say so, because the reuse is the argument.

- **17.1 — §17.1 The reader without the specification.** **≈400 words.** Lead with the concrete case per `STYLE.md` §1: a manuscript arrives for review, its methods section says a quality-control pass was run by an agentic workflow, and nothing else. Establish: the book has so far assumed the reader designs the workflow; four positions say otherwise, and each is common — reviewing a manuscript someone else produced with agents, inheriting a pipeline whose specification you did not write, being handed a system by your institution, and receiving a vendor product with agentic components inside it; what these share is that the reader cannot change the workflow and can only decide how much to believe it, and can sometimes decide whether it is used; and the book's apparatus transfers, because the records Ch. 12 tells a producer to keep are exactly the records a receiver should ask for. Close by naming what the chapter delivers: a set of questions, a sorting of the six failure modes by whether they are detectable from outside, and a checklist.
- **17.2 — §17.2 Reviewing a manuscript produced with agents.** **≈900 words.** The chapter's centre. It must establish:
  (i) What a disclosure statement should have let a reviewer check, and what most will not — the book's own definition (Ch. 9) says which tool did which task under whose oversight, and a disclosure that says "AI was used for language editing" answers none of the questions that matter.
  (ii) The escalating sequence of what a reviewer may reasonably ask for, from cheapest to most demanding, each with what it establishes and what it costs the authors: the specification the agentic step ran under; the gates it passed and what each checks; whether any gate's false-negative rate has been measured (Ch. 11 §11.5); the evidential tier claimed and the check that establishes it (Ch. 11 §11.2); reviewer coverage, meaning which parts had an independent check and which rest on author inspection (Ch. 12 §12.4).
  (iii) The single highest-yield question, stated as such: not "did you use AI?" but "what would have caught it if this step had been wrong?". Every other question is a way of making that one answerable.
  (iv) What a reviewer is **not** entitled to demand: the transcript, the prompts, or a re-run. Say why plainly — the transcript is not evidence of what happened (Ch. 12 §12.2 on agent self-summary), the prompts are often the group's working method, and a re-run may be impossible because the model is gone (Ch. 12 §12.4). A reviewer asking for a re-run is asking for the wrong property.
  (v) The reviewer's own position, in two or three sentences: policy on whether the reviewer may use AI while reviewing is a separate question the book treats in Ch. 9, and it is not this section's subject. Point once and move on.
  (vi) Proportionality, closing the section: the depth of scrutiny matches what rests on the claim, exactly as tier matches stakes (Ch. 11 §11.7), and a reviewer who demands calibration records for an exploratory triage is making the same error as a workflow that stops at Tier 2 for a published result.
  **Citations:** Elsevier (2026) and NIH (2023) are both already in Ch. 9's references and may be reused for the disclosure-threshold and reviewer-confidentiality points respectively, carrying their existing caveats. Ansari (2026), already in Ch. 5 and Ch. 13, may be reused once for the finding that fabricated citations survive elite review — which is the sharpest available argument that a reviewer's plausibility read is not a check. Nothing new.
  `[AUTHOR: what you have actually asked for, or wished you could ask for, as a reviewer of a manuscript with agentic components — and whether any editor would have backed you.]`
- **17.3 — §17.3 What is detectable from outside, and what is not.** **≈650 words.** Sort Ch. 13's six modes by external detectability, and be honest about the answer, which is uneven:
  detectable from outside with a mechanical check the reviewer can run (fabricated citations — resolve every DOI, which is a reviewer's cheapest and highest-yield action); detectable from outside if the claim's scope is compared to the evidence's scope (confident extrapolation); detectable only from the record (specification drift, context loss — a reviewer who cannot see the specification cannot see it move); largely undetectable from outside (silent unit errors, unless an invariant is checkable from the reported numbers; over-agreeable review, which leaves no external trace at all).
  Draw the conclusion the chapter needs: the modes a reviewer can catch unaided are the minority, which is precisely why the provenance questions of §17.2 are not bureaucratic. It is the only route to the rest. Add the field-scale point in one sentence, cross-referencing Ch. 13 §13.9: the reviewer is the mechanism that is supposed to catch what the group's own gates missed, and correlated verification error is what happens when reviewers use the same instruments the authors did.
  **This section carries Figure 17.1** (§6.3).
- **17.4 — §17.4 Inheriting a workflow you did not specify.** **≈550 words.** Establish: the first task on inheriting is not to run it but to find out what it was supposed to do, and if no specification exists, that is the finding; the reconstruction sequence, concretely — read the gates, because what a workflow checks tells you what its builder feared; read the failure log and the rejection records, because they tell you what it has actually caught; establish the calibration state of every gate and treat unmeasured ones as unmeasured rather than as working (Ch. 11 §11.5); and check whether any calibration has expired (Ch. 11 §11.5, validity). Then the harder judgement: whether to run it at all before you understand it, and the rule the book recommends — an inherited workflow runs first on cases whose answers you already know, which is Ch. 11 §11.4's evaluation set built backwards. Close on the honest position: sometimes the right answer is that the workflow cannot be defended and should not be run, and being the person who inherited it does not make you responsible for defending it, only for saying so.
  `[AUTHOR: a workflow you inherited, agentic or not, and what you did before trusting it.]`
- **17.5 — §17.5 Judging a system you were handed.** **≈500 words.** The institutional and vendor case. Establish: the questions differ from the reviewer's because you may not see inside at all; what to ask for anyway, in order — what the system's acceptance criteria are and who set them, what it does when it fails and whether failure is visible, what record it leaves, and what it is permitted to touch (Ch. 12 §12.8); the vendor-claim rule, which is the book's own stance applied outward — a self-reported capability figure is a hypothesis for independent measurement, and the measurement is task-grounded evaluation on your own data (Ch. 11 §11.1), exactly as an operational centre re-verified a data-driven weather model rather than taking the vendor's scores (Ch. 11 §11.3); and the position to hold when you cannot get answers, stated without drama — a system whose behaviour cannot be bounded, recorded or checked is one whose outputs carry no evidential tier, and that is a statement about the evidence rather than an accusation about the vendor.
  **Citations:** Ben Bouallègue et al. (2024) and Five Eyes (2026) are already in Ch. 11 and Ch. 12 and may be reused, one each. Nothing new.
- **17.6 — §17.6 Verification checklist.** **≈350 words.** Standard bulleted printable format, per the house pattern used in Ch. 11 §11.8 and Ch. 12 §12.11. It is written for the receiver, not the producer, and each item names what the receiver can establish and what they cannot. Eight items or fewer. Cover: disclosure read and its gaps named; the specification asked for; gate calibration state established; evidential tier claimed and checked against the check that establishes it; reviewer coverage established; the mechanical checks the receiver can run themselves actually run (citation resolution first); scope of claim compared to scope of evidence; and a stated position where answers were not available, recorded rather than left implicit.
  **[AUTHOR SIGN-OFF]** noted in §7.4: this extends the outline §9 decision on which chapters carry checklists. It adds; it does not alter.
- **17.7 — §17.7 Repository pointer.** **≈150 words.** House pattern (cf. Ch. 11 §11.9, Ch. 12 §12.11). `/patterns/ch17-on-the-receiving-end` holding a reviewer's question set and a printable receiver's checklist under `/checklists`; volatile material (current journal disclosure requirements, current policy classes) confined to the repository per the vendor-neutral convention. `[AUTHOR: confirm the repository paths once the reviewer question set is finalised.]`
- **17.8 — Figures.** Two, specified in §6.3 and §6.4.
- **17.9 — References.** New reference list containing only entries reused from Ch. 5, Ch. 9, Ch. 11, Ch. 12 and Ch. 13, copied verbatim including their `[verify]` flags. **No entry that is not already in the manuscript.**

---

### ch18 — What will last *(net −20; renumbered by R.1)*

- **18.1 — Compress the fifth principle (F3).** §17.2 (now §18.2), the fifth principle beginning "The fifth is that the right question is often whether to use an agent at all…". **Rewrite, net ≈ −40.** With §4.4 now making the argument properly, this principle states the conclusion in one sentence and cross-references, rather than gesturing at the economics. It must still stand alone as a principle for a reader who reads Part V first.
- **18.2 — Sharpen the filter (F3).** §17.3 (now §18.3), the sentence containing "whether it moves the verification burden rather than merely the generation cost". **Rewrite plus insertion, net ≈ +20.** Extend by one sentence naming what the filter is testing for: an announcement that moves only the generation cost does not widen the class of tasks worth delegating, which is why so few of them matter (Ch. 4 §4.4).
- **18.3 — Renumbering.** Covered by R.1.

---

## 6. Figures

Three new, one re-brief, one renumber. Conservative by design: no finding gets a figure unless the argument has parts and relationships a reader needs to see at once. F1's incident response, F3's thesis, F7's scope and F9's induced demand all get none, because each is an argument in time rather than a structure.

Every brief is written in full per `FIGURES.md` §6, with caption and alt-text **written at the same time as the brief**, in the v5.0 colloquial register, no metaphors, meaning never carried by colour alone.

### 6.1 — New **Figure 2.4**, in ch02 §2.6 (F6)

- **type:** architecture
- **claim:** In a governed workflow the agent proposes and something the agent does not control disposes, and there are exactly three kinds of disposer.
- **what it must show:** one agent (orange) emitting a *proposal* rather than an action, the proposal arrow annotated to make clear nothing has been written yet; three disposer paths fanning out, each with its own icon and its own annotation of what it is good for — a deterministic rule (vermillion gate: the criterion can be written as code), a human decision (blue: the criterion is judgement), an external source of truth (green tool plus sky-blue store: the criterion is a fact the agent cannot manufacture); each path leading to the same protected artefact (sky-blue) which only the disposers may write to; a rejection path from each disposer to a log, annotated that a rejected proposal is kept with its reason; and a footer stating what the arrangement does not buy, which is protection against a badly designed disposer.
- **must not:** duplicate Figure 6.1's QC-specific detail. Figure 6.1 is the instance; 2.4 is the general form, and the two must be visibly the same shape so a reader recognises it.
- Renderer: `figures-src/f_ch02_04.py`.

### 6.2 — Re-brief **Figure 11.1**, in ch11 §11.2 (F5)

Not an edit: the brief is rewritten in full, because six of its fields change.

- **claim:** now six operationally defined tiers.
- **what changes:** six bars, not five. New bar 5, "5 · independent-method corroboration — a second method with a different error structure agrees". Bar 6 relabelled "6 · adversarial scrutiny — a competent party tries to break it and fails", keeping the reviewer purple and the reviewer icon. The bracket currently spanning tiers 3–5 becomes 3–6. The footer changes to "the tiers are cumulative: a tier-5 claim has passed 1 to 5". **One new annotation on bar 6**, carrying the category point: "the only tier named for the checker, not the check — its strength is a measured quantity (§11.5)". **One new annotation on bar 5**: "changes the measurement chain, not just the regime".
- **legibility check:** six bars plus a standfirst plus six annotations is at the density ceiling of `FIGURES.md` §2. If the canvas crowds, drop the tier-1 and tier-2 annotations, not the two new ones.
- Caption and alt-text rewritten to match; the existing caption's "Correct is a word that gets earned at tier three" survives and is worth keeping.
- Renderer: `figures-src/f_ch09_12.py`.

### 6.3 — New **Figure 17.1**, in new ch17 §17.3 (F8)

- **type:** architecture (a two-column sort, not a flow)
- **claim:** Most of the six failure modes are not detectable from outside without the record, which is why a reviewer's provenance questions are the substance rather than the bureaucracy.
- **what it must show:** the six modes of Ch. 13 as six labelled rows, sorted into three bands by what it takes to catch them from outside — "catchable by a check the reviewer can run" (fabricated citations; confident extrapolation), "catchable only from the record" (specification drift; context loss), "not catchable from outside" (silent unit errors; over-agreeable review); each row annotated with the specific action or record involved (for fabricated citations, "resolve every DOI — the reviewer's cheapest action"; for over-agreeable review, "leaves no external trace at all"); a vermillion bracket down the lower two bands annotated "four of six need the record"; a footer carrying the chapter's governing question, "what would have caught it if this step had been wrong?".
- Renderer: `figures-src/f_ch13_18.py` (post-R.1 name).

### 6.4 — New **Figure 17.2**, in new ch17 §17.2 (F8)

- **type:** sequence
- **claim:** A reviewer's requests escalate, and each step establishes something specific at a specific cost to the authors.
- **what it must show:** two lanes, reviewer (purple) and authors (blue), five numbered escalating requests read top to bottom — disclosure statement, specification, gates and what each checks, gate calibration and tier claimed, reviewer coverage; each step annotated with what it establishes and what it costs the authors to supply; a vermillion side-note listing the three things a reviewer is not entitled to demand (the transcript, the prompts, a re-run) with the one-line reason for each; a footer, "depth of scrutiny matches what rests on the claim".
- Renderer: `figures-src/f_ch13_18.py`.

### 6.5 — Renumber **Figure 17.1 → 18.1** (R.1)

Covered by task R.1 items 3–4. No content change.

**Figure count:** 51 → 54.

---

## 7. Admin documents

### 7.1 — `manuscript/OUTLINE.md` — **ai-editor, done in this pass**

Updated to v0.6 alongside this plan: header change-note; §5 budget note recording the growth; §6 anatomy note for the new Ch. 17's checklist and pointer; §7 restructured for the new chapter, the renumbering, the four new sections and the six-tier ladder; §9 status refreshed (the stale R1 line and the ai-reviewer comment at line 119 are both resolved) and the new items recorded as **proposed, awaiting the author**, not as decided.

### 7.2 — `manuscript/GLOSSARY.md` — **ai-writer, in the back-matter batch** *(≈380 words)*

Five new entries, alphabetical, in the file's existing plain-and-warm register, each tagged with its canonical chapter:

- **Auditability** (Chapter 12) — reconstruct and defend what was done, without necessarily being able to repeat it; what an agentic workflow actually delivers; weaker than reproducibility and worth having.
- **Calibration validity** (Chapter 11) — a gate's measured miss rate is a reading taken on a date, with a window past which it stops being evidence.
- **Independent-method corroboration** (Chapter 11) — a second determination of the same quantity by a method with a different error structure; Tier 5; the environmental sciences' habitual strongest move.
- **Propose–dispose separation** (Chapter 2) — the agent proposes, something it does not control disposes; the three kinds of disposer.
- **Reproducibility, replicability, auditability** (Chapter 12) — the three-way distinction in one entry, with which one agentic work delivers. *(If this reads better as three entries, split it; the constraint is that the distinction appears once and the cross-reference points at Ch. 12 §12.4.)*

**One correction:** the existing **Audit trail** entry ends "…so a result is not just re-runnable but explicable." That carries the same inversion as ch12 line 76 and must be rewritten in the same batch, to claim auditability and nothing more.

### 7.3 — `manuscript/FURTHER-READING.md` — **ai-writer, in the back-matter batch** *(≈220 words)*

- **FR.1** Part V heading: "(Chapters 9, 16–17)" → "(Chapters 9, 16–18)". Add a one-line note under it that Chapter 17 draws on sources already listed under Parts II and III rather than adding its own.
- **FR.2** Gaps section: add four gaps this pass identified and could not fill from `/research`, each in the section's existing one-line style, each explicitly named as a gap for a future sweep rather than a hole in the argument: automation bias and deskilling in scientific workflows; empirical work on model concentration across research groups (the base rate behind the correlated-verification-error argument); rebound or induced-demand effects for inference; and any established practice for retracting or correcting an agentic result.
- **FR.3** Do not add entries. No new source enters the manuscript in A1 (§4).

### 7.4 — Items needing the author, collected

| # | Item | Where | Standing |
|---|---|---|---|
| 1 | The book becomes 18 chapters in 5 parts | D1, OUTLINE §7, §9 | Proposed. Not a change to a §9 DECIDED item, but it changes the book's shape and is the author's call. |
| 2 | New chapter title, "On the receiving end" | D1, ch17 | Proposed; one alternative on record. |
| 3 | Scope statement wording (F7a) | task 0.1 | Positioning. Author's, not an agent's. `[AUTHOR: …]` marker mandated in the text. |
| 4 | New Ch. 17 carries a verification checklist and repository pointer | task 17.6 | **Extends** outline §9's "full anatomy binds Part II only, with Ch. 11 and Ch. 12 still owing checklists and pointers". Adds a third exception; alters nothing. Flagged rather than presumed. |
| 5 | Net length growth of roughly +9,800 prose words | §8 | Interacts with the DEFERRED "overall length reduction" item. Not a contradiction, but the author should see the number before execution and may want the lean variant. |

**No DECIDED item in outline §9 is altered by this plan.** Items 1 and 4 extend the record; items 3 and 5 are flagged for a decision the author has not yet taken.

---

## 8. What this costs in length, and a lean variant

Honest accounting, because the review claimed F3 and F6 would shorten the book and, on inspection of the actual text, they do not.

| | Prose words |
|---|---|
| Additions across ch00–ch16, ch18, back matter | ≈ +6,350 |
| New Chapter 17 | ≈ +3,500 |
| Mandatory cuts (F6 re-derivations, §3.6 concession, ch18 compression) | ≈ −465 |
| **Net prose** | **≈ +9,400** |
| Three new figure briefs and one re-brief (file words, not print) | ≈ +2,200 |
| **Net file growth** | **≈ +11,600** |

Against the manuscript's current ≈108,800 file words (of which roughly a third is figure-brief specification that never reaches print), this is about +11%. In indicative page terms it takes the book from ≈150 pp towards ≈185 pp. **Overall length reduction is a DEFERRED decision, so this pass is not gated by it**, but the author should see the number now rather than discover it later, and the deferred pass gets meaningfully harder.

**Lean variant, if the author wants roughly half the growth.** My recommendation is against it, but the three cuts are these, in the order I would make them:

1. **Reduce the new Ch. 17 to §§17.1–17.3 plus the checklist** (drop the inherited-workflow and handed-system sections). Saves ≈1,050 words. Cost: the chapter becomes a peer-review chapter rather than a receiving-end chapter, which is a narrower and less honest answer to F8, but it keeps the sharpest material.
2. **Cut §13.9(b), homogenisation, to two sentences inside §13.9(a).** Saves ≈200 words. Cost: low. It is the movement with the least evidence behind it and the least a group can do about it.
3. **Merge Ch. 12 §12.10 into the §12.9 close rather than giving it a section**, at ≈250 words instead of 620. Saves ≈370 words. Cost: high, and this is the one I would resist hardest. F1's strongest observation is that the book has a preventive half and no response half, and a compressed §12.9 tail restores the imbalance.

Total lean saving ≈1,620 words, taking net prose growth to ≈+7,800. That is not a large enough saving to justify the losses, which is why I recommend executing the plan as written and taking the length question up separately, on the whole manuscript, where the real reductions are.

---

## 9. Acceptance criteria (what ai-reviewer reviews against)

**Global, every batch:**

1. No new citation anywhere. Every source named in new prose already appears in the manuscript, with its existing `[verify]` flags and caveats carried unchanged.
2. Nothing from §4's exclusion list appears: no automation-bias or deskilling citation; no named economic effect for induced demand; no model-withdrawal cadence figure; Naddaf (2025) not attached to the deskilling argument.
3. Every passage this plan flags as the book's own argument or a conjecture carries a calibrated confidence flag, and the conjecture in §13.9(b) is named as one.
4. No `[AUTHOR: …]` marker resolved, moved or deleted; every new marker this plan mandates is present. There are **eleven**: tasks 0.1, 3.1, 11.4, 12.1, 12.4, 13.2(b), 15.1, 16.4, 17.2, 17.4, 17.7.
5. De-duplication (G5): each idea in §3's map appears in full once, and everywhere else as one clause or one sentence. **The five F6 cuts happened** — this is the item most likely to be quietly skipped, so check the deleted text is actually gone rather than paraphrased in place.
6. All new prose sentence-per-line, British English, v5.0 voice indistinguishable from its surroundings, no metaphors, ~30-word ceiling, no em-dash connectors.
7. Word budgets respected within about 20% (G7), counted as prose only, excluding figure briefs and reference entries.
8. Status headers advanced on every edited chapter (G11).

**Renumbering spot-checks (run as greps, not by eye):**

- `Chapter 17` returns only references to the new chapter; `figure-17-1` returns nothing; `§17.` returns nothing outside `ch18`.
- Every site in the D3 table is updated; `five-tier`, `Five tiers` and `independent adversarial scrutiny` return nothing in `ch11` or `ch13`. `REVISION-PLAN.md` line 103 is **unchanged** — flag it as an error if it was edited.
- `## 2.7 A plain cost model`, `## 4.5 What does not transfer`, `## 12.11 Verification checklist`, `## 12.12 Repository pointer` all exist; ch02's roadmap sentence names §2.6 and §2.7 correctly.
- Figure count is 54; Figure 11.1's brief has six bars in every field including the alt-text and the infographic description.

**Content spot-checks:**

- **ch12 §12.4:** the sentence "…make a result reproducible in the strong sense, not merely re-runnable but explicable…" is gone. The replacement states that explicable is the weaker property. The **Definition — Audit trail** box no longer ends "not just re-runnable but explicable". `GLOSSARY.md`'s Audit trail entry is fixed to match.
- **ch04 §4.4:** the objection in movement (v) is present and given real space, and the confidence flag is moderate-to-high rather than high. A §4.4 that only asserts the thesis has failed the task.
- **ch11 §11.2:** the new Tier 5 is defined by the check, and the category paragraph concedes the Tier 6 asymmetry rather than smoothing it over.
- **ch13 §13.9:** four movements, each with an explicit "what a group can do", and none of them promising a check that catches a field-level failure.
- **ch17 (new):** §17.2 contains the "what would have caught it if this step had been wrong?" formulation and the list of what a reviewer may **not** demand. A chapter that only lists things to ask for has missed half the finding.
- **ch16 §16.6:** four considerations, not three; the "loops that produce nothing" clause appears once, in the new fourth consideration, not also in the closing paragraph.
- **ch03 §3.6:** the concession paragraph is gone, and its content is in §3.7.

---

## 10. Execution order

Six batches. Batches 1 and 2 must complete and be reviewed before anything else starts; batches 3–5 are independent of each other; batch 6 is last because it depends on everything.

| # | Batch | Files | Tasks | Depends on | Why grouped |
|---|---|---|---|---|---|
| **1** | **Renumbering** | `ch17`→`ch18`, `ch08`, `ch16`, `FURTHER-READING.md`, `figures/`, `figures-src/` | R.1 | — | Purely mechanical, and everything downstream writes "Chapter 17" meaning the new chapter. Doing it first removes an entire class of ambiguity. Review and merge before batch 2. |
| **2** | **Foundations: the two new principles** | `ch01`, `ch02`, `ch03`, `ch04`, `ch00` | 0.1–0.3, 1.1–1.4, 2.1–2.5, 3.1–3.2, 4.1–4.5 | 1 | F6's §2.6 and F3's §4.4 are the two canonical homes that every later batch cross-references. Nothing downstream can be written correctly until their exact wording exists. `ch00`'s scope statement and `ch03` §3.7 are the same argument's two other faces and must be drafted by one writer for consistency. Includes Figure 2.4. |
| **3** | **The tier ladder and the evidence chapter** | `ch11`, `ch13` | 11.1–11.8, 13.1–13.3 | 2 | The six-tier renumbering and Ch. 13's tier-wording fix must be consistent, and §13.9's automation-bias movement and §11.5's countermeasure are two halves of one argument written by one writer. The heaviest batch. Includes the Figure 11.1 re-brief. |
| **4** | **Governance** | `ch12`, `ch09`, `ch06`, `ch08`, `ch10` | 12.1–12.6, 9.1–9.3, 6.1–6.2, 8.1–8.2, 10.1 | 2, 3 | Ch. 12 §12.4 is the reproducibility canonical home that Ch. 9 §9.3 cross-references, and Ch. 12 §12.10 depends on Ch. 11 §11.5's validity material from batch 3. The four F6 cuts in 6, 8, 9 and 12 belong together so one writer applies one standard to all of them. |
| **5** | **Case studies and adoption** | `ch14`, `ch15`, `ch16`, `ch18` | 14.1–14.4, 15.1, 16.1–16.5, 18.1–18.2 | 2, 3 | All are cross-reference and compression work against §2.6, §4.4 and §11.2, plus the standalone F9 section. Ch. 14's last F6 cut sits here with Ch. 15's F3 confirmation because both are the case studies read against the new thesis. |
| **6** | **The new chapter and the back matter** | new `ch17`, `GLOSSARY.md`, `FURTHER-READING.md` | 17.1–17.9, 7.2, 7.3 | 1, 2, 3, 4 | The new chapter reuses material from every one of the earlier batches and cites nothing they have not settled; writing it earlier would guarantee rework. The glossary's five entries cannot be written until their canonical homes are final. Includes Figures 17.1 and 17.2. |

**Then, as a separate mechanical pass after batch 6 merges:** regenerate the SVG set. Three new figures and one re-brief in `figures-src/f_ch02_04.py`, `f_ch09_12.py` and `f_ch13_18.py`, plus the `figure-17-1` → `figure-18-1` rename from batch 1, re-run through the house renderer, with the automated collision check passing on the full set of 54.

---

## 11. Post-review rulings, and the pass they schedule (ai-editor, 1 Aug 2026)

A1 executed, ai-reviewer's independent pass ran, and its corrections were applied. What that review left behind is a set of items that needed an editorial decision rather than a fix, each recorded as an `[ai-reviewer: …]` comment addressed to ai-editor. Five are settled below, two go to the author, and one is a process finding about this plan's own structure. Everything scheduled here is **pass A2**: mechanical, no new argument, no new source, and it reopens nothing in §5. The global rules G1–G12 apply to it unchanged except where 11.1 amends G6.

### 11.1 — Settled: the propose–dispose separation gets an info-box (`ch02` §2.6, `GLOSSARY.md`)

**Ruling.** The box is added. The term is the architecture this plan calls the book's unifying one, it is cross-referenced from nine places, and `STYLE.md` §9 runs box first and glossary second. Calibration validity and Auditability both got boxes in the same pass under the same rule. Flagging the book's most-used new term more weakly than its two least-used is the wrong way round, and ai-writer was right that only G6 stood in the way.

**G6 is amended** to enumerate one further info-box, this one. Nothing else is opened; the "No others" clause otherwise stands.

**Instruction (ai-writer).** In `ch02` §2.6, add a `**Definition — Propose–dispose separation.**` info-box in the chapter's existing box format. **≈60 words.** Place it at the first substantive use, which is the sentence "That is the *propose–dispose separation*, and it generalises well past quality control." It states the separation (the agent proposes; something the agent does not control disposes) and names the three kinds of disposer (a deterministic rule, a human decision, an external source of truth). No new citation. Advance the status header. Clear the `[ai-reviewer: …]` and `[ai-writer: …]` comments at that section once done.

**GLOSSARY.md's opening line stands as written.** It already provides for entries without boxes, in the clause "together with a small number of terms the book leans on throughout". It is a one-way rule and reads correctly as one, and the instance that raised the question disappears when the box is added. Clear comment (2) in that file.

**Acceptance.** `ch02` §2.6 carries exactly one info-box, in the house format; the box and the glossary entry say the same thing in the same terms; no other new info-box appears anywhere in the manuscript.

### 11.2 — Settled: a constructed illustration is labelled, at two sites rather than four (`ch03` §3.7, `ch12` §12.10)

**Ruling.** A house convention is set, and it is now a hard rule in `CLAUDE.md`. The reviewer named four openings; the four are not equally at risk, and labelling all of them would make the label uninformative where it matters. `ch02` §2.6 opens "Ask an agent to clean a decade of gauge records", and `ch17` §17.4 opens "A colleague leaves and you take over their quality-control pipeline". Both are generic second-person scenarios with no quantities and no claim that anything occurred. `ch03` §3.7 and `ch12` §12.10 are different. Both carry specific quantities: two of five neighbours since the spring, and eight months with two of twenty seeded faults missed. A reader meeting either one cold can reasonably take it for a record.

**The test, for the next drafter.** Label a constructed scenario where it carries specific quantities, dates or outcomes that a reader could take as a record of something that happened. Do not label a generic scenario that carries none. An `[AUTHOR: …]` marker at the foot of a section is a note to the author and does not discharge this.

**Instruction (ai-writer).** Put the fixed label `*Constructed illustration.*` on its own line immediately before the opening sentence of `ch03` §3.7 ("A gauge in your network has been reading high…") and of `ch12` §12.10 ("You re-calibrate a citation gate…"). In those two chapters only, extend the `> **Conventions:**` header line, immediately after the `**[verify]**` clause, with `· *Constructed illustration* marks a scenario assembled to show the mechanics, not a record of something that happened`. Change no other word of either section. Advance both status headers. Clear the `[ai-reviewer: …]` and `[ai-writer: …]` comments at `ch12` §12.10.

**Acceptance.** The manuscript contains exactly two `*Constructed illustration.*` labels; both sit in chapters whose conventions line defines the label; `ch02` §2.6 and `ch17` §17.4 carry none; no `[AUTHOR: …]` marker has moved.

### 11.3 — Settled: the em-dash prohibition reaches the glossary and not the reference list (`GLOSSARY.md`, `FURTHER-READING.md`)

**Ruling.** `STYLE.md` §11 bars the em dash as a connector in "manuscript text (body prose, info-boxes, captions and alt-text alike)" and exempts "headings and labels, status headers, figure-brief fields and reference lists". A glossary definition is prose that the reader reads as prose, so it is bound. An annotated further-reading entry is a reference list, which §11 exempts by name, and the dash introducing each annotation is part of that fixed format. So the file that needs a sweep is the glossary, and `FURTHER-READING.md` is left alone. The five new entries drafted in A1 already sit on the stricter reading, so the sweep closes a split that is visible on the page rather than opening one.

**Instruction (ai-writer).** Sweep `GLOSSARY.md`: 46 em dashes on 32 lines as of 1 Aug 2026. Replace each connector with whichever is plainest of a comma, a colon, parentheses or a new sentence, per `STYLE.md` §11. No definition loses content, and no entry is rewritten beyond the punctuation and the few words needed to carry it. Do not touch `FURTHER-READING.md`. Clear comment (1) in `GLOSSARY.md`.

**Acceptance.** No em dash in `GLOSSARY.md` joins clauses, appends an afterthought or carries an aside; any that remain are in a heading, a label or a numeric range. Every entry means what it meant before. `FURTHER-READING.md` is unchanged.

### 11.4 — Settled: the ~30-word ceiling binds captions and alt-text, and the alt-text backlog is scheduled

**Ruling.** `FIGURES.md` v2.1 §6 now states it: `STYLE.md` §11's ceiling binds captions and alt-text as it binds body prose, with §11's semicolon-enumeration exception. `STYLE.md` §7's checklist puts no exemption on item 13 and explicitly extends item 14 to captions and alt-text, so this is the guide's reading rather than a new rule. The accessibility argument runs the same way: a screen reader delivers a sentence in one pass, and a listener cannot scan back over a 95-word one. The cost is real and is stated rather than hidden: 45 of the 54 alt-texts are non-compliant.

**Instruction (ai-writer), pass A2.** Split the over-length sentences in the 45 alt-texts. Splitting only, per `STYLE.md` §11: no content is dropped, no annotation is lost, and the alt-text still carries what the figure's annotations say. Each alt-text exists twice, in the chapter's `![…](…)` image and in the `alt-text` field of its brief in `fig-brief/chNN-slug.md`, and the two are changed in the same edit. Also split the two over-length sentences in the caption of Figure 11.1, which are accumulations of clauses rather than enumerations. Leave the caption of Figure 17.2, whose 32-word sentence is a genuine parallel enumeration. Leave the four captions accepted on 30 Jul 2026 under the same exception: Figures 1.2, 6.4, 14.1 and 14.2.

**Acceptance.** No alt-text in the manuscript carries a sentence over roughly 30 words. Each chapter's alt-text matches its brief's `alt-text` field word for word. Figure 11.1's caption is within the ceiling; the other five over-length captions are unchanged and each is a parallel enumeration.

### 11.5 — Settled: "rebound" and "induced demand" stay in the further-reading gaps

**Ruling.** They stay. §4 of this plan bars a named economic effect from *manuscript prose*, and `ch16` §16.6 obeys it by describing the mechanism and stopping. Naming a research gap is a different act from making a claim. The gaps section frames each item as a gap for a future sweep, and those two terms are what such a sweep would search on. Removing them would cost a reader the search terms and buy nothing but a consistency that §4 never asked for.

**Off-ramp for the author, in one edit.** If you would rather the label went, ai-writer has drafted the subject-only form: "whether cheap inference increases total computation rather than displacing it". Say the word and it is a single-line change. Leave the `[ai-reviewer: …]` and `[ai-writer: …]` comments in `FURTHER-READING.md` standing until then.

### 11.6 — Escalated to the author: what Chapter 3 now closes on

**The finding.** §3.7 put the boundary of the specification discipline last. So a chapter titled "Specifying work for agents" now ends its argument on the claim that a great deal of good science cannot be specified. That is a change to the chapter's argumentative shape, and this plan's D5 chose the placement without weighing the emphasis it creates.

**What has already happened.** ai-writer applied the reviewer's second mechanical alternative in the corrections commit: `ch03` now carries a closing summary and a forward pointer, and the summary names both what the chapter achieved and the boundary it marked. The remedy the review asked for is in place.

**Why it still goes to the author.** The remaining question is emphasis, and emphasis here is positioning. The close reads directly against the front matter's scope statement, which is item 3 of §7.4 and is marked `[AUTHOR SIGN-OFF]`. If the scope statement changes, this close changes with it, so the two are decided together or not at all.

**Recommendation: keep it.** F7's charge was that the concession was under-weighted, ending on an honest boundary is what the book does elsewhere, and the closing summary already stops the chapter deflating. If the author reverses it, the mechanical fix is to move §3.6's two closing sentences ("…rather than never being made at all") to the end of §3.7, which is ai-writer's work and about 40 words. Leave the `[ai-reviewer: …]` comment in `ch03` standing until the author rules.

### 11.7 — Escalated to the author: `STYLE.md` §12 contradicts §1

**The finding.** §12's anti-pattern list bans "addressing the reader as 'you'", which §1 requires, §7's checklist item 9 requires, and the §8 prompt block requires. Two agents found it independently. It is a survival from the pre-26-July academic register that the v5.0 consolidation did not sweep.

**Why it is not settled here.** `STYLE.md` is the author's own voice guide, and the clause sits in the list of things the author says never to do. Deleting a line from that list is the author's call, not an editor's tidy-up, even where the line is plainly dead. No manuscript prose breaches it, because every chapter follows §1, so nothing is blocked meanwhile.

**Standing instruction until the author rules.** Nothing in the manuscript is revised against §12's "you" clause. The `[ai-reviewer: …]` comment at `STYLE.md` §12 stays exactly where it is. Two lesser items in the same list want a ruling at the same time, and both are the author's for the same reason: whether "one-sentence paragraphs" is still barred given §2's licence for a paragraph break to do rhetorical work, and whether the §12 list binds captions, alt-text and figure-brief fields as §12.1 and §12.2 explicitly do.

### 11.8 — Process finding: §5 assigned a task that §10 never batched

Chapter 5's task 5.1 was specified in §5 and appeared in none of the six batches in §10, so no writer was ever given it. ai-reviewer caught it after execution and ai-writer has since executed it, and `ch05` is at draft r5 with the cross-reference in §5.3. The defect is structural rather than incidental: §5 and §10 are two lists of the same work with no check that one covers the other. **For the next plan of this shape:** §10's batch table names every chapter that §5 assigns a task to. The plan is not final until that comparison has been run explicitly. `OUTLINE.md` §7 now records Ch. 5's task, which it did not before.

### 11.9 — Comments to clear, and comments to leave standing

**Clear when the item is executed** (ai-writer, pass A2): `ch02` §2.6 both comments, per 11.1 · `ch12` §12.10 both comments, per 11.2 · `GLOSSARY.md` comments (1) and (2), per 11.1 and 11.3 · `ch02`'s second comment, on three missing SVGs, which is now stale because `figure-2-4.svg`, `figure-17-1.svg` and `figure-17-2.svg` were all rendered on 30 July and are present · `ch10` §10.3's placement note and `FURTHER-READING.md` line 62's placement note, both of which record an endorsed deviation and need no action.

**Leave standing:** `STYLE.md` §12, per 11.7 · `ch03`'s close, per 11.6 · `FURTHER-READING.md`'s naming comment, per 11.5 · `ch00`'s front-matter comment, whose two findings are the author's under `[AUTHOR SIGN-OFF]` and whose second point (that the scope statement's "Nothing in these pages governs that work" contradicts `ch03` §3.7, which names two things that do) is a real contradiction that only the author's wording can settle.

### 11.10 — Found in the same sweep, not fixed, and why

- **The closing summary is used in two chapters of nineteen.** `ch02` and `ch03` carry a `*This chapter has …*` summary before the forward pointer; the other seventeen carry a forward pointer alone or nothing. `ch03` acquired one in A1's corrections, which is how the asymmetry arose. Either every chapter gets one or the two lose theirs, and that is a book-wide consistency decision worth a pass of its own rather than a correction folded into A2.
- **`.claude/agents/ai-writer.md` still scopes the writer to `ch01`–`ch17`.** Left alone deliberately: agent definitions are configuration rather than manuscript or guideline documents, and they are not ai-editor's to edit. Flagged for the author.

---

*Change control: ai-editor maintains this plan; ai-writer and ai-reviewer do not edit it. Discrepancies found mid-batch (an anchor sentence that has moved, a cut that would break an argument, a budget that cannot accommodate an instruction, a cross-reference target that does not exist) are raised in the batch's PR discussion and never silently resolved.*
