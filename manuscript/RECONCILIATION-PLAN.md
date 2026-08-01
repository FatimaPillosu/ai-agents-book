# Reconciliation plan — pass X1

**v1.0 · 1 August 2026** · Maintained by **ai-editor**. Executed by **ai-writer**; reviewed against by **ai-reviewer**.

Two bodies of work now sit in one repository and contradict each other. The author's instruction is that **neither is to be lost**. This document is the executable reconciliation.

**The two bodies.**

1. **`manuscript/RESTRUCTURE-PROPOSAL.md` v1.0**, carrying the author's **approval record of 27 July 2026**: six decisions approved, one changed, one added, and **four DECIDED items altered on the author's explicit instruction**. Approved in full and **never executed**. No chapter file, and no admin document, was ever edited by it. `CLAUDE.md` and `OUTLINE.md` still describe a project in which none of it happened.
2. **`manuscript/ADVERSARIAL-INTEGRATION-PLAN.md` v1.1** (pass **A1**), converting the eight substantive findings of `manuscript/ADVERSARIAL-REVIEW.md` into per-chapter instructions. **Executed 30 July, independently reviewed, corrections applied, five post-review rulings settled and two escalated** (plan §11). A1 is in the manuscript.

They collide because the restructure moves furniture that A1 has since built on. Neither is wrong; they were planned four days apart against different questions, on branches that did not see each other until 1 August.

**Standing.** The restructure's approval record is the author's own instruction and binds. A1 is executed text and cannot be discarded without discarding reviewed work. Where the two conflict, this plan resolves in favour of the author's instruction wherever the instruction's *premise* survives A1, and escalates wherever it does not. Every escalation is in §11. Nothing in §11 is executed until the author rules.

**What X1 is.** (i) The Ch. 4 merge, with A1's bounded-payoff thesis carried into it intact. (ii) The new harness chapter drafted, its research precondition now discharged. (iii) A1's new chapter kept at Ch. 17, with Part V restored. (iv) "What will last" dissolved into three surviving pieces. (v) Nine repository pointers out, six "Adapting the pattern" sections in, two appendices assembled. (vi) A Preface absorbing four movements of front matter. (vii) The render pointer out of the caption.

**What X1 is not.** No revoicing. No new research sweep. No new source of any kind. No companion-repository build-out (parked). **No length-reduction pass** — §8 states the arithmetic and schedules that work separately, because it is now five times larger than the restructure priced it at. No re-scan of the positioning claim (deferred).

---

## 1. Global rules (apply to every batch)

- **X1 — Citations only from `/research`.** Four reports now exist. The harness chapter draws on `research/2026-07-27-harness-and-loop-engineering.md` and nothing else new; every other batch adds **no citation at all**. If a passage feels like it needs a source, that is a finding for the PR discussion, not licence to supply one.
- **X2 — Relocated prose travels verbatim.** Where this plan moves a passage between chapters, ai-writer moves the existing sentences and changes only what the move forces: the section number, the cross-references, and any clause the move makes false. Relocation is not an invitation to rewrite. Where a moved passage needs new connective prose, this plan says so and budgets it.
- **X3 — `[AUTHOR: …]` markers travel with the passage they annotate, verbatim.** Never resolved, never edited, never dropped. Two markers have been overtaken by events; they are listed in §11 for the author to reword, and ai-writer leaves both exactly as written meanwhile.
- **X4 — Integrity (hard rules).** Never fabricate. British English. Sentence-per-line for all new body prose (`STYLE.md` §10). v5.0 colloquial voice for every new sentence. No metaphors anywhere, captions and alt-text included. ~30-word sentence ceiling. No em dash as a connector. Constructed illustrations labelled per `CLAUDE.md`.
- **X5 — De-duplication discipline.** Every idea keeps exactly one canonical home. A1's canonical-home map (`ADVERSARIAL-INTEGRATION-PLAN.md` §3) stands, with the four addresses this plan changes, listed in §4.1. Where a relocation creates a new adjacency, this plan names which copy survives.
- **X6 — Renumbering is mechanical and total.** Where this plan renumbers, every reference changes in the same batch, and §9 gives the greps.
- **X7 — The §4.4 trap.** A1 planted cross-references to **"Chapter 4 §4.4"** meaning the bounded-payoff thesis. After the merge, the thesis is **Chapter 1 §1.8**, and the *new* Chapter 4 has its own **§4.4, "The tool surface"**. A stale reference will therefore not dangle: it will resolve, silently, to the wrong section and read plausibly. This is the sharpest failure mode in the whole reconciliation. Every site is listed in §5.3 and grepped in §9.
- **X8 — No new forward promises.** No sentence of the form "Chapter N develops this" unless this plan says so and the target section exists. This rule now also bars any new promise of runnable code, prompts, printable checklists, case-study configurations or exercises, in any form, anywhere.
- **X9 — Word budgets.** A budget is a ceiling with about 20% tolerance, not a target. Where a task says "cut", the cut is mandatory and its size is approximate.
- **X10 — Status headers.** Every edited chapter advances its draft number. The new Ch. 4 opens at `draft r1` with the conventions block copied from `ch16`.
- **X11 — Nothing unexecuted presented as accomplished.** Unchanged. Ch. 8's intercomparison remains a worked design. The harness chapter's guidance is a set of design decisions, not a report of a standard.
- **X12 — Figures.** New and amended figures follow `FIGURES.md` in full, with caption and alt-text written at the same time as the brief. Briefs live in `fig-brief/chNN-slug.md`, one file per chapter (author decision, 1 Aug 2026).

---

## 2. The reconciled chapter map

**Seventeen chapters, five parts, a Preface, and two appendices.** One chapter merged out (old Ch. 4), one dissolved (old Ch. 18), one added (the harness, new Ch. 4). **Chapters 2, 3 and 5 to 17 keep their numbers, their filenames and their figure identifiers.** Exactly one figure is renumbered in the whole book.

| Now (19 files, 18 ch., 5 parts) | After X1 (18 files, 17 ch., 5 parts) | What happens |
|---|---|---|
| **Front matter** (`ch00`) | **Preface**, then front matter (`ch00`) | Preface absorbs the contribution statement, the domain framing, A1's scope statement and the disclosure statement. §5.7. |
| **Part I — Foundations** | **Part I — Foundations** | |
| 1 Why agents, why now | **1 Why agents, why now, and where they don't belong** *[PROPOSED title]* | Absorbs old Ch. 4 §§4.1–4.4 as new §§1.5–1.8. Old §1.5 becomes §1.9. Figure 4.1 → **Figure 1.3**. §5.3. |
| 2 Anatomy of an agent | 2 (same) | §2.4 and §2.7 shed design guidance to the new Ch. 4. A1's §2.6 and §2.7 numbering stands. §5.6. |
| 3 Specifying work for agents | 3 (same) | Closing forward pointer rewritten: the next chapter is now the harness. §5.3. |
| 4 The scientist's stance | *(merged into Ch. 1; file deleted)* | §4.5 deleted, its three definition sentences absorbed into Ch. 1 §1.4. |
| | **4 The harness: engineering the loop** *[PROPOSED]* | **New.** `ch04-the-harness.md`, nine sections, four figures. §5.5. |
| **Part II — Core patterns** | **Part II — Core patterns** | |
| 5 Evidence and literature synthesis | 5 (same) | §5.7 → "Adapting the pattern". |
| 6 Data acquisition and quality control | 6 (same) | §6.7 → "Adapting the pattern". |
| 7 Coding and pipeline agents | 7 (same) | §7.7 → "Adapting the pattern". §7.3 gains a pointer to Ch. 4. |
| 8 Model orchestration and experimentation | 8 (same) | §8.8 → "Adapting the pattern". §8.7's repository sentence cut. |
| 9 From results to manuscript | 9 (same) | §9.8 → "Adapting the pattern". §9.4 policy mechanism rewritten. |
| 10 Multi-agent workflows | 10 (same) | §10.8 → "Adapting the pattern". |
| **Part III — Trust** | **Part III — Trust** | |
| 11 Verification and evaluation | 11 (same) | §11.9 **deleted**, nothing replaces it. Six-tier ladder stands. |
| 12 Provenance, governance and security | 12 (same) | §12.12 **deleted**. §12.10 and §12.11 stand. §12.8 gains a pointer to Ch. 4. |
| 13 The failure gallery | 13 (same) | Unchanged. §13.9 stands. |
| **Part IV — Case studies** | **Part IV — Case studies** | |
| 14 Verification under constraint | 14 (same) | §14.7's repository sentence rewritten. |
| 15 Governing a modelling workflow end to end | 15 (same) | Unchanged apart from two cross-references. |
| **Part V — Adoption and scrutiny** | **Part V — Adoption and scrutiny** *[PROPOSED: part retained]* | Restored: it now holds two chapters, not one. §3.3. |
| 16 Starting in your own group | 16 (same) | Gains new closing **§16.7**, absorbing old §18.3 and §18.1's durable/volatile frame. |
| 17 On the receiving end | **17 (same) — closing chapter** | §17.7 **deleted**. Gains a short unnumbered closing coda carrying old Ch. 18's final sentence. |
| 18 What will last | *(dissolved; file deleted)* | §18.1 and §18.3 → Ch. 16 §16.7 · final line → Ch. 17 coda · European Commission citation → Preface · §18.2 and §18.4 cut · Figure 18.1 deleted. §5.4. |
| **Back matter** | Back matter + **Appendix A**, **Appendix B** | Nine verification checklists; the specification schema. §5.2. |

**Counts.** 18 manuscript files (`ch00`–`ch17`) plus two appendix files. **57 figures** (54 − Figure 18.1 + four in the new Ch. 4). Five parts, so `ch00`'s "The book has five parts" and Ch. 1 §1.9's five-part roadmap **survive as written**, with one sentence changed in each for Part I's new fourth chapter. That is a direct dividend of restoring Part V, and it removes two of the restructure's most error-prone rewrites.

---

## 3. The eight collisions, resolved

### 3.1 — Chapter 4: the thesis travels with the decision procedure into Ch. 1 §1.8

**The collision.** The restructure folds "The scientist's stance" into Ch. 1 and frees the number for the harness chapter. A1 then inserted **§4.4 "The frontier that does not move"** into that same chapter: 987 words stating what the review calls the book's strongest and most contrarian thesis, cross-referenced from six places.

**Resolution.** §4.4 moves to Ch. 1 as **§1.8**, immediately after old §4.3's decision procedure, which becomes **§1.7**.

**Reason, in one line.** §4.4 opens "Both of §4.3's questions are answered by facts about the task", so it is not a section that happens to sit after the quadrants: it is the quadrants read forward in time, and separating the two destroys the argument.

**What that costs, stated honestly.** Ch. 1 becomes nine sections and about 4,730 words of print prose, which is **1.23× the chapter average** of 3,848. It is not an outlier: Ch. 11 is 2.11×, Ch. 12 1.97×, Ch. 13 1.49×. It is, though, a twelve-page opening chapter doing six jobs, and the book's most contrarian claim now lands before the reader has met a single pattern. In my judgement that is the right trade, because the alternative placements are all worse: Ch. 16 arrives two hundred pages after the premises and A1's D4 explicitly rejected the closing restatement as a place to build an argument; the new Ch. 4 is the wrong subject; and a chapter of its own re-spends the slot the merge just recovered. The option of **not merging** — keeping the stance material as a chapter and giving Part I five chapters — is on record in §11, Q1, because reversing the merge is the author's call and not mine.

**Section map for the merged Ch. 1.**

| New | From | Words | Note |
|---|---|---|---|
| 1.1 The problem this book addresses | ch01 §1.1 | 355 | unchanged |
| 1.2 What changed, and when | ch01 §1.2 | 690 | unchanged; Figure 1.1 |
| 1.3 Three terms, one distinction | ch01 §1.3 | 630 | unchanged; Figure 1.2; A1's second disanalogy stands |
| 1.4 An honest capability boundary | ch01 §1.4 | 690 | **absorbs** old §4.5's three definition sentences (≈60 words); its forward pointer becomes internal |
| 1.5 Where an agent fits the scientific method | old §4.1 | 243 | carries A1 task 4.4's pointer to Ch. 3 §3.7 |
| 1.6 Augmentation and automation are different commitments | old §4.2 | 427 | Kapoor citation dropped, one clause pointing to Ch. 10 §10.1 in its place |
| 1.7 A decision procedure: should an agent do this? | old §4.3 | 555 | **Figure 4.1 → Figure 1.3**; carries A1 task 4.3's pointer to Ch. 2 §2.6 |
| 1.8 The frontier that does not move | old §4.4 | 987 | **A1's thesis, moved intact** |
| 1.9 What the rest of the book does | ch01 §1.5 | 400 | Part I sentence rewritten for the harness chapter |

### 3.2 — The harness chapter: drafted now, precondition discharged

**The collision.** None, strictly. The chapter is approved (approval record item 1 and 2), fully briefed (restructure §2, nine sections, four figures, 3,500–4,000 words, six acceptance criteria), and **never drafted**, because the restructure declared a research sweep a blocking precondition rather than a nicety.

**Resolution.** The precondition is discharged. `research/2026-07-27-harness-and-loop-engineering.md` was commissioned against exactly that brief and delivers **46 verified sources**, a section-by-section evidence verdict for all nine sections, a volatile-figures register and a quantified statement of where the literature is genuinely empty. Its bottom line: *"all nine sections can now be written with at least some source support, which was not true a week ago."* Drafting instructions are in §5.5.

**Reason, in one line.** The only thing standing between the approved brief and a drafted chapter was the sweep, and the sweep is in the repository.

**Three things A1 changed about the brief**, and each is carried into §5.5: Ch. 2's cost model is now **§2.7**, not §2.6, so every pointer the brief sends there moves; Ch. 2 §2.6 is now the propose–dispose separation, which is the general form of the harness's human-interrupt decision and must be pointed at rather than re-derived; and Ch. 11 §11.5 and Ch. 12 §12.4 and §12.10 now hold calibration validity, auditability and incident response, all of which the harness chapter's run-record and maintenance sections touch.

### 3.3 — "On the receiving end": stays at Ch. 17, and Part V is restored

**The collision.** A1's new chapter is 3,567 words, drafted, reviewed and corrected. The restructure dissolves Part V and makes Ch. 16 the closing chapter, so the chapter has no home in the sixteen-chapter map.

**Resolution.** The chapter **keeps its number, its filename and its Part V home. Part V survives, retitled "Adoption and scrutiny", holding Ch. 16 and Ch. 17.**

**Reason, in one line.** The restructure dropped Part V for exactly one stated reason — *"With Ch. 17 gone it would hold one chapter, and a part of one chapter is a structural error rather than a structure"* — and A1's new chapter restores it to two, which is the same size as Part IV, so the premise of the drop no longer holds.

**Standing.** Dropping the Part V label was not one of the six items the author approved; it was a consequence worked out in restructure §1 from the Ch. 17-old removal. Restoring it when the premise changes is therefore not a reversal of an author instruction. It is nonetheless a visible change to the book's shape and is marked **[PROPOSED]** in the outline. §11, Q3.

**Order within Part V.** Ch. 16 "Starting in your own group" first, Ch. 17 "On the receiving end" second, as now. Zero renumbering. The alternative — swapping them so the adoption chapter closes the book — costs a renumbering of two chapters, ten inbound references, two figures, two SVGs and two brief files, four days after A1 paid that cost once. The reading is better in the order that is free: outward from your own group to work that is not yours.

### 3.4 — "What will last": dissolved, its four sections resolved separately, and the contradiction flagged

**The collision, stated exactly.** The restructure removes the chapter on the 27 July approval. **The author then edited that chapter directly on GitHub on 31 July**, four days after the approval and inside the A1 structure, in commit `18a0a82` — eleven insertions, twenty-two deletions, a surgical prose trim.

**What the evidence actually shows.** The commit graph resolves most of it. `18a0a82` sits on the `adversarial-analysis` line; the restructure's four commits sit on a separate line and were merged only on 1 August, in `676490f`. **On 31 July the author was editing a working tree in which `RESTRUCTURE-PROPOSAL.md` did not exist.** The edit is therefore not evidence that the author reversed the removal. It is evidence that the author was working where the removal had not happened.

Two further things the edit does show, and both matter:

1. **The author independently cut the chapter's most exposed claim.** The deleted paragraph called the print-and-repository division *"this book's central wager about how to write usefully for practitioners"* — the exact sentence the restructure §5.3 named as the most exposed version of a claim the repository can no longer support. The author's own edit moves in the restructure's direction.
2. **The author values this chapter's prose.** Nobody spends an evening balancing sentences in a chapter they have written off.

**Resolution.** Dissolve the chapter, and preserve three of its four sections rather than the restructure's one.

| Section | Words | Ruling |
|---|---|---|
| §18.1 Two layers moving at two speeds | ≈250 | **Preserved, in the author's trimmed wording**, as the opening movement of the new Ch. 16 §16.7, with the "two media" clause dropped because the narrowed repository cannot support it. The restructure reduced this to one sentence in `ch00`; that is too thin for a passage the author polished four days ago. |
| §18.2 The principles that will last | ≈350 | **Cut**, per the de-duplication rule. Five compressed restatements of arguments whose canonical homes are Ch. 1, Ch. 3, Ch. 11 and Ch. 1 §1.8. This is the one piece of the author's 31 July edit that does not survive, and §11, Q4 asks the question directly. |
| §18.3 Staying current by principle, not by release | ≈500 | **Preserved in full**, as the body of Ch. 16 §16.7, with its worked illustration. |
| §18.4 The repository as the living layer | ≈400 | **Cut**, as the approved repository decision requires: it promises runnable minimal examples, printable checklists and sanitised case-study configurations, all parked. **Its final sentence is adapted as the last line of Ch. 17**, and its European Commission living-guidelines citation moves to the Preface. |

**Citations.** All five of the chapter's references are cited elsewhere in the book: Anthropic Institute (ch01, and ch04 §4.4 which becomes ch01 §1.8), European Commission (ch09, ch15, ch16), METR (ch01, ch04, ch16), the *Nature* editorial (ch09, ch15), Zheng et al. (ch10, ch11, ch13). **Dissolving the chapter loses no citation.** Verified 1 August 2026, not assumed.

**Figure 18.1 is deleted**, with its SVG and its brief. Its claim is *"Two layers, two clocks, two media"*, and the third of those three is what the approved repository decision removes. What survives is "some material dates faster than other material", which does not need a figure. §11, Q4 puts the deletion to the author, because it is the figure attached to the section the author has just been editing.

### 3.5 — Repository pointers and checklists: nine out, six replaced, nine collected

**The collision.** The restructure removes eight pointers and replaces each with "Adapting the pattern", promoting the checklists to Appendix A and adding Appendix B. A1 then wrote a **ninth** pointer (ch17 §17.7, promising `/patterns/ch17-on-the-receiving-end` and a printable checklist under `/checklists`) and a ninth inline checklist, and left the Ch. 11 and Ch. 12 pointers standing.

**Resolution.**

- **Nine pointers are deleted**, not eight. Ch. 17 §17.7 goes with the rest; it promises exactly the parked material the approved decision removes, and A1 §7.4 item 4 raised it as an open question rather than a settled one.
- **Six get "Adapting the pattern"**, at 150–250 words each: Ch. 5, 6, 7, 8, 9 and 10. Each keeps the deleted pointer's section number.
- **Three get nothing**: Ch. 11 §11.9, Ch. 12 §12.12 and Ch. 17 §17.7 are deleted outright, leaving each chapter to end on its verification checklist. This follows the approved wording exactly — *"The anatomy's seventh section is 'Adapting the pattern' … Ch. 11 and Ch. 12 owe a verification checklist only"* — and extends the same rule to Ch. 17, which is not a Part II chapter either.
- **Appendix A collects nine checklists**, not eight, adding Ch. 17's receiver-side list. It prints the checklist items only, without each chapter's framing prose: about 2,400 words, six to seven pages. Printing them in full would be 3,253 words and nine to ten pages for no gain. Each in-chapter checklist gains one sentence naming Appendix A as its printable form.
- **Appendix B** is Ch. 3's specification schema as a blank template, as approved.
- **The new Ch. 4 carries neither a checklist nor a pointer.** It is a Part I chapter and the Part II anatomy does not bind it. Stated here so ai-reviewer does not raise it.

**Reason, in one line.** A promise of material that will not exist when a reader looks for it is a correctness problem, and it does not become less of one because A1 wrote a ninth instance of it after the decision to remove the first eight.

**Category C.** The scattered living-layer sentences are a different problem and get a different fix. The full inventory, re-measured against the post-A1 manuscript rather than copied from the restructure, is in §5.2.

### 3.6 — Front matter: one Preface, absorbing four movements

**The collision.** The restructure adds a Preface absorbing `ch00`'s contribution statement and disclosure statement. A1 then inserted the scope statement (task 0.1, ≈350 words as it now stands) as a new movement *inside* that same contribution statement, carrying an `[AUTHOR SIGN-OFF]` marker and a standing reviewer escalation.

**Resolution.** The Preface absorbs **four** movements, not two: the contribution statement, the domain framing, A1's scope statement and the disclosure statement. All of it goes into **P.2** and **P.3**. The scope statement is the same argument as the positioning claim seen from the other side, and splitting them across two locations would breach the de-duplication rule the restructure invoked to justify the Preface in the first place.

**Consequence for the brief.** P.2 rises from 300–400 words to **550–700**, and the Preface's target rises from 900–1,100 to **1,200–1,400**. Its acceptance criterion "under 1,200 words" becomes **under 1,500**.

**Recommended candidate: `PREFACE-EXAMPLES.md` §1, the A + C + D hybrid.** Three reasons. It is the only one of the eight that discharges all three jobs the Preface has to do, which is to say who is speaking, what is promised and refused, and how far to trust the object. Its P.2 already contains most of what the scope statement says, so absorbing A1's version is an edit rather than a rewrite. And it already describes the *narrowed* living layer correctly — *"the source, the dated research sweeps, the further reading, the figure briefs and an errata note per release. There is no code in it, and there was never going to be"* — which no other candidate does. Two corrections it needs: "Eight verification checklists are printed in Appendix A" becomes nine, and the scope statement's three named chapters (8, 14, 15) must be carried in from `ch00` so the reviewer's finding on that point is not lost. §11, Q5.

**Reason for rejecting the others, in one line each.** B duplicates Ch. 1 §1.1 directly. C alone reads as terms and conditions and does nothing for credibility. D alone cannot be finished until the manuscript is. E and F are sections of a preface, not prefaces. G converges on A, as its own draft demonstrates. A alone is the strongest single type and is inside the recommendation.

### 3.7 — Figure briefs: location stands, the render pointer moves

**The collision.** The approved spec is `/figure-briefs`, one file per figure, bold heading dropped, render pointer moved out of the caption into an HTML comment. The author later instructed `fig-brief/`, one file per chapter, and that is what is implemented, with the pointer left in the caption and the bold heading kept.

**Resolution, in three parts.**

1. **Location and granularity: no change.** `fig-brief/chNN-slug.md`, one file per chapter. The author's later instruction governs, it is recorded as DECIDED in outline §9 and `CLAUDE.md`, and `FIGURES.md` v2.1 §6 already documents it.
2. **The render pointer moves out of the caption.** *Recommended.* The restructure's argument is separable from the location question and is right: production metadata does not belong inside published prose. Every caption in the book currently ends `(Rendered as \`figures/figure-N-M.svg\` from its brief in \`fig-brief/chNN-slug.md\`, per \`FIGURES.md\`.)` — fourteen words of build instruction that a reader must skip, 57 times, about 800 words in total. It becomes an HTML comment on the line below the caption: `<!-- brief: fig-brief/chNN-slug.md -->`. Invisible in any rendering, findable by grep, and one mechanical pass. `FIGURES.md` §6.1 amends accordingly, taking it to v2.2.
3. **The bold heading line stays.** *Recommended, weakly.* The restructure dropped it as redundant with the caption's opening. In a Markdown source with no build system it is the only in-text anchor for "Figure 2.1", and the redundancy costs 457 words across the whole book. Revisit at the layout decision, which is deferred. §11, Q6.

### 3.8 — Length: the restated budget cannot survive both bodies of work

Full arithmetic in §8. The short form: the 200–210 page budget was restated on 27 July against a 66,097-word manuscript and before A1 landed. A1 added about 9,400 words. The restructure's own trims recover about 4,500 and its own additions cost about 8,100. The reconciled book lands near **76,300 words of body prose and about 240 pages excluding back matter, 265 including it**. Meeting 200–210 pages needs a reduction of **10,000 to 12,000 words**, which is five times the 1,500–2,500 the restructure scheduled as Stage 10. That is a decision for the author, not a trim ai-writer can be handed. §11, Q7.

---

## 4. Preservation ledger

Item by item, so the author can check the claim that nothing is lost.

### 4.1 — Pass A1: every substantive change, and where it ends up

**Structural decisions.**

| A1 item | Substance | Status under X1 |
|---|---|---|
| **D1** New chapter at 17; "What will last" → 18 | The chapter | **Kept at Ch. 17.** The renumbering half is superseded: Ch. 18 dissolves (§3.4), so "What will last" ceases to be a chapter at all. The renumbering work itself is not undone, it is overtaken. |
| **D2** Propose–dispose canonical in Ch. 2 §2.6 | New §2.6, cost model → §2.7, five downstream cuts | **Untouched.** The new Ch. 4 §4.7 points at it and must not re-derive it. |
| **D3** Six-tier ladder, Tier 5 new, Tier 6 renamed | Ch. 11 §11.2 and 13 downstream sites | **Untouched.** |
| **D4** Bounded-payoff thesis canonical in Ch. 4 §4.4 | New §4.4, 987 words | **Relocated intact to Ch. 1 §1.8** (§3.1). Argument, objections, confidence flags and citations all move unchanged. |
| **D5** Scope statement to front matter; §3.7 to Ch. 3 | Two new movements | **Both kept.** The scope statement relocates into the Preface P.2 (§3.6); Ch. 3 §3.7 is untouched. |
| **D6** Field-scale failures as Ch. 13 §13.9 | New section, four movements | **Untouched.** |
| **R.1** The renumbering batch | Mechanical | **Superseded**, not reversed. Figure 18.1 is deleted; `FURTHER-READING.md`'s Part V heading changes again, to "Chapters 9, 16–17". |

**Per-chapter tasks.** Tasks **0.2, 0.3, 1.1, 1.3, 2.1–2.5, 3.1, 3.2, 5.1, 6.1, 6.2, 8.1, 8.2, 9.1, 9.2, 9.3, 10.1, 11.1–11.8, 12.1–12.6, 13.1–13.3, 14.1–14.4, 15.1, 16.1–16.5** are **untouched by X1** except where a cross-reference is repointed. That is 44 of A1's 56 tasks landing without any interference.

The twelve that move or change:

| A1 task | What it did | Status under X1 |
|---|---|---|
| **0.1** Scope statement in `ch00` | ≈350 words, `[AUTHOR SIGN-OFF]` | **Relocated to Preface P.2** with its marker and the reviewer escalation intact. |
| **1.2** Forward pointer to the thesis, ch01 §1.4 | ≈40 words | **Kept, becomes internal**: "Chapter 4 §4.4" → "§1.8". |
| **4.1** New §4.4, the thesis | 987 words | **→ Ch. 1 §1.8.** |
| **4.2** Renumber §4.4 → §4.5 | Heading only | **Superseded**: §4.5 is deleted in the merge, its three definition sentences absorbed into Ch. 1 §1.4 so nothing is lost. |
| **4.3** Propose–dispose cross-ref in §4.3 | ≈30 words | **→ Ch. 1 §1.7.** |
| **4.4** §3.7 cross-ref in §4.1 | ≈25 words | **→ Ch. 1 §1.5.** |
| **8.1** ch08 §8.3 cut and cross-ref | Cut stands | Untouched; its "Chapter 4 §4.4" pointer repoints to Ch. 1 §1.8. |
| **11.6(c)** Tier-5 clause in the checklist | Stands | Its "(Chapter 4)" repoints to Ch. 1 §1.7. |
| **15.1** The thesis demonstrated, ch15 §15.8 | ≈70 words plus a marker | Kept; two references repoint to §1.8. |
| **16.1** Verification cost does not fall | ≈80 words | Kept; repoints to §1.8. |
| **17.6** Ch. 17 verification checklist | ≈400 words | **Kept in the chapter, and collected into Appendix A.** |
| **17.7** Ch. 17 repository pointer | ≈150 words | **Deleted** (§3.5). The only A1 task X1 removes outright. |
| **18.1, 18.2** Ch. 18 compressions | Two edits | **Already reversed by the author** on 31 July, who deleted both §4.4 cross-references. Nothing to repoint and nothing to preserve. |

**Figures.** A1's Figure 2.4, the Figure 11.1 re-brief, Figure 17.1 and Figure 17.2 are all **untouched**. Figure 18.1, which A1 renumbered from 17.1, is **deleted** (§3.4).

**Post-review rulings, `ADVERSARIAL-INTEGRATION-PLAN.md` §11.** Rulings **11.1** (propose–dispose info-box), **11.2** (constructed-illustration labels), **11.3** (glossary em-dash sweep) and **11.4** (alt-text ceiling sweep, 45 alt-texts) are pass **A2** and are **folded into X1's batches** where the same files are open: §5.9. Ruling **11.5** stands. Escalations **11.6** (what Ch. 3 closes on) and **11.7** (`STYLE.md` §12) remain open with the author and are **not touched**; both stay in `CLAUDE.md`'s Open list.

### 4.2 — The restructure: every approved decision, and where it lands

| Approved item (27 Jul 2026) | Status under X1 |
|---|---|
| 1. Ch. 4 merge into Ch. 1; new Ch. 4 on harness | **Executed as approved**, with A1's §4.4 carried into it (§3.1). |
| 2. Harness chapter in Part I, after specification | **Executed as approved** (§3.2, §5.5). |
| 3. Living layer re-scoped to source, research reports, further reading, per-release errata | **Executed as approved**, and extended to nine pointers and the post-A1 category-C sites (§3.5, §5.2). |
| 4. Appendix A (checklists) and Appendix B (specification schema) | **Executed as approved**, with nine checklists rather than eight (§3.5). |
| 5. Length restated at 200–210 pages | **Recorded and challenged.** The budget cannot be met; §8 states the arithmetic and §11, Q7 asks for a new decision. |
| 6. Figure-brief extraction | **Superseded by the author's later instruction of 1 Aug.** Location and granularity stand as implemented; the render-pointer half of the original spec is re-recommended (§3.7). |
| **Changed:** Ch. 17-old removed, not merged | **Executed**, with three of its four sections preserved rather than one (§3.4). |
| **Added:** a Preface | **Executed**, absorbing four movements rather than two (§3.6). |

**The four DECIDED items the author changed on 27 July 2026.** None is in `CLAUDE.md` or `OUTLINE.md` today, because the restructure was never executed. All four go in at batch **B1**, each carrying the date and the authority, so a future agent reading only the admin documents can see why a DECIDED item moved. §7.

### 4.3 — What cannot be preserved

Three items, and only three.

1. **Ch. 18 §18.2, "The principles that will last"** (≈350 words after the author's trim). Five compressed restatements of arguments with canonical homes elsewhere. The de-duplication rule is DECIDED and this is the clearest instance of what it exists to prevent. **The author trimmed this section on 31 July**, so cutting it discards prose the author worked on four days ago. §11, Q4.
2. **Figure 18.1 and its SVG and brief.** Its governing claim is a three-way split whose third term the approved repository decision removes. §11, Q4.
3. **Ch. 17 §17.7, the repository pointer** (≈150 words). Written by A1 after the decision to remove the other eight. §3.5.

Everything else in both bodies of work survives, in place or relocated, and the ledger above says where.

---

## 5. Per-file instructions

Task IDs are what ai-reviewer reviews against, item by item. Word budgets are prose only.

---

### 5.1 — Standing constraint on every batch

Before editing any chapter, read `ADVERSARIAL-INTEGRATION-PLAN.md` §3 (the canonical-home map) and apply the four address changes X1 makes to it: the bounded-payoff thesis is **Ch. 1 §1.8**, not Ch. 4 §4.4; the propose–dispose cross-reference in the stance material is **Ch. 1 §1.7**, not Ch. 4 §4.3; the exploratory-work cross-reference is **Ch. 1 §1.5**, not Ch. 4 §4.1; and the scope statement's canonical home is **the Preface, P.2**, not `ch00`'s contribution statement. Nothing else in that map changes.

---

### 5.2 — Batch B2: repository promises out, "Adapting the pattern" in, appendices assembled

**B2.1 — Delete nine repository-pointer sections.**

| File | Section | Then |
|---|---|---|
| `ch05` | §5.7 | replaced by "Adapting the pattern", same number |
| `ch06` | §6.7 | replaced, same number |
| `ch07` | §7.7 | replaced, same number. Its `**[verify: confirm repository layout and exercise set before release.]**` goes with the section |
| `ch08` | §8.8 | replaced, same number |
| `ch09` | §9.8 | replaced, same number |
| `ch10` | §10.8 | replaced, same number |
| `ch11` | §11.9 | **deleted outright**; the chapter ends on §11.8 |
| `ch12` | §12.12 | **deleted outright**; the chapter ends on §12.11 |
| `ch17` | §17.7 | **deleted outright**; the chapter ends on §17.6 plus the new coda (B4.3) |

No section number changes anywhere. Each deleted section's `[AUTHOR: …]` marker, where it has one, goes with the section it annotates: `ch17` §17.7's marker asks the author to confirm repository paths that will no longer exist, so it is deleted with the section rather than orphaned. This is the single exception to X3 and it is stated here rather than taken silently.

**B2.2 — Write six "Adapting the pattern" sections.** ≈150–250 words each, ≈1,200 total. Two parts, both short. First, the two or three decisions a reader must make to apply this pattern in their own setting, stated as decisions rather than instructions, drawn from that chapter's own material. Second, one sentence naming what in the chapter will date and how to check it. **No promise of any repository content.** No new citation. Each section closes by naming Appendix A as the printable form of the chapter's checklist.

**B2.3 — Rework the category-C living-layer sentences.** Inventory re-measured against the post-A1 manuscript on 1 August 2026, not copied forward:

| Site | What it claims | Instruction |
|---|---|---|
| `ch00` line 46 | repository holds "named tools, exact model versions, volatile figures, runnable examples and printable checklists" | Rewrite to the narrowed layer: the Markdown source, the dated research sweeps every citation comes from, the further reading, the figure briefs, and an errata note per release. Delete "runnable examples and printable checklists". Carry the European Commission living-guidelines citation here from `ch18` §18.4. |
| `ch00` line 48 | "when a claim in these pages says that the current figure lives in the repository" | Rewrite: where a reader needs a current value, the text says where to look it up. |
| `ch01` line 157 (§1.4) | "the companion repository tracks the movement" | Narrow the clause. "The print holds the position and the reasoning" survives. |
| `ch02` line 237 (§2.7) | "concrete figures … belong in the companion repository" | State that the figures are deliberately out of print and why, name where a reader looks them up, promise no maintained table. Keep the `[AUTHOR: …]` marker at line 239 unchanged. |
| `ch05` line 171 | volatile figures "stay in the repository" | Absorb into "Adapting the pattern" or delete. |
| `ch06` lines 151–154 | `/patterns/ch06-data-qc`, `/prompts`, `/checklists` | Deleted with §6.7. |
| `ch07` lines 198, 203 | `/patterns/ch07-…`, `/exercises` | Deleted with §7.7. |
| `ch08` line 199 (§8.7) | "Its printable form lives in the repository alongside the pattern." | **Rewrite to name Appendix A.** This one sits outside the pointer section and is the easiest to miss. |
| `ch08` lines 203–208 | `/patterns`, `/case-studies`, `/checklists`, `/prompts` | Deleted with §8.8. |
| `ch09` header line, line 105 (§9.4) | "current specifics … held in the repository" | **Rewrite substantively.** Replace the promise with an instruction the reader can act on: check the journal's own current policy page before submission, and here is what the policy classes tell you to look for. Same for the chapter's header line. ≈80 words. |
| `ch09` lines 189–192 | `/checklists` and the artefact-linked example | Deleted with §9.8. |
| `ch10` lines 204–209 | `/patterns`, `/prompts`, `/checklists`, `/case-studies` | Deleted with §10.8. |
| `ch11` line 395 | `/patterns/ch11-…` | Deleted with §11.9. |
| `ch12` line 350 | `/patterns/ch12-…` | Deleted with §12.12. |
| `ch14` line 155 (§14.7) | methods and score definitions in the repository | Rewrite: state what a group would need to reproduce the work and where it is available, promising nothing this repository will not hold. |
| `ch16` header line, lines 79, 174 | volatile cost and energy figures "marked for the companion repository" | State that the figures are out of print and why, keep the reasoning, name no maintained table. |
| `ch17` lines 255–263 | `/patterns/ch17-…`, `/checklists` | Deleted with §17.7. |
| `ch18` lines 61–70 | the whole living-layer section | Deleted with the chapter (B4). |
| `FURTHER-READING.md` | `[AUTHOR: decide whether this gaps section belongs in the printed back matter or only in the repository]` | **Leave the marker exactly as written.** Its second option is no longer available in the sense it was drafted; that is a rewording for the author, listed in §11, Q8. |

**B2.4 — Assemble Appendix A.** New file `manuscript/apx-a-verification-checklists.md`. Nine checklists, collected in chapter order: §5.6, §6.6, §7.6, §8.7, §9.7, §10.7, §11.8, §12.11, §17.6. **Print the checklist items only**, each list under a heading naming its chapter and the section it came from. Do not carry each chapter's framing prose. Do not reword an item. ≈2,400 words. A short opening of ≈120 words says what the appendix is and that each list is also in its chapter at the point where it is argued for. **This is assembly, not writing**: any item that reads badly in isolation is a finding for the PR, not a licence to rewrite it.

**B2.5 — Write Appendix B.** New file `manuscript/apx-b-specification-schema.md`. Ch. 3 §3.3's schema as a blank template a reader can copy, with one line per field saying what belongs in it. ≈350 words. Cross-referenced from Ch. 3 §3.3, Ch. 10 §10.5 and Ch. 15. No new argument: every word of guidance is already in Ch. 3, and this is the form, not the teaching.

---

### 5.3 — Batch B3: the merge

**B3.1 — Move four sections.** From `ch04-the-scientists-stance.md` into `ch01-why-agents-why-now.md`, inserted between §1.4 and the existing §1.5, in this order and with these headings:

```
## 1.5 Where an agent fits the scientific method
## 1.6 Augmentation and automation are different commitments
## 1.7 A decision procedure: should an agent do this?
## 1.8 The frontier that does not move
```

The existing `## 1.5 What the rest of the book does` becomes `## 1.9`. **Prose travels verbatim** (X2). Internal `§4.N` references inside the moved text become `§1.N` under the map in §3.1.

**B3.2 — §4.5 into §1.4.** Delete `## 4.5 What does not transfer to an instrument`. Its argument is already Ch. 1 §1.4's closing paragraph, verbatim in substance. **Absorb its three definition sentences** into §1.4 immediately after "accountability, scientific judgement, and authorship": accountability is being the named person who answers for a decision and its consequences; interpretation is deciding what a result means using context you hold and the system does not; authorship is the standing to claim a contribution and defend it as your own. ≈60 words, moved not rewritten. Nothing else of §4.5 survives and nothing else needs to.

**B3.3 — §1.4's forward pointer becomes internal.** The sentence "Chapter 4 §4.4 draws out that consequence, and sets the limit it puts on how far delegation can ever be taken" becomes a reference to §1.8. ≈15 words.

**B3.4 — The Kapoor de-duplication.** Old §4.2 cites Kapoor et al. (2024) for the finding that a plain model in a retry loop matches elaborate architectures; Ch. 10 §10.1 cites the same paper for the same finding. **Ch. 10 keeps it.** In new §1.6, replace the citation with one clause pointing to Ch. 10 §10.1. ≈25 words. Remove the entry from Ch. 1's reference list only if no other Ch. 1 sentence uses it; check, do not assume.

**B3.5 — Figure 4.1 becomes Figure 1.3.** In `ch01`, inside §1.7: the bold marker, the image path (`../figures/figure-1-3.svg`), the caption's opening, and the in-text mention. In `fig-brief/`, move the `## Figure 4.1 — Should an agent do this?` brief out of `ch04-the-scientists-stance.md` into `ch01-why-agents-why-now.md`, placed after Figure 1.2, and change its `id` and `caption` fields. Rename `figures/figure-4-1.svg` → `figures/figure-1-3.svg`. In `figures-src/f_ch02_04.py`, rename the entry and update any manifest that names it.

**B3.6 — Repoint every "Chapter 4" reference.** Fourteen sites in nine files. **Read X7 before starting.**

| File | Line (1 Aug) | Currently | Becomes |
|---|---|---|---|
| `ch00` | 91 | "Chapter 4 §4.4 says why the boundary sits where it does" | Chapter 1 §1.8 *(this line travels to the Preface in B7; repoint it wherever it then sits)* |
| `ch01` | 149 | "Chapter 4 §4.4 draws out that consequence" | §1.8 *(B3.3)* |
| `ch01` | 162 (§1.9) | "the stance to take towards the technology (Chapter 4)" | Rewrite the Part I sentence: the anatomy of an agent (Chapter 2), how to specify work for one (Chapter 3), and how to engineer the loop that runs it (Chapter 4). ≈30 words |
| `ch03` | closing pointer | "The next chapter asks the question that comes before any of it: which parts of the research cycle should be handed to an agent at all, and which should not." | **Rewrite.** The next chapter is now the harness: specification says what the work is, and Chapter 4 builds the machinery that holds an agent to it. ≈35 words. **This site post-dates the restructure and is easy to miss.** |
| `ch03` | 174 | ai-writer comment naming Chapter 4 | Leave the comment standing (ruling 11.6 is open) and add one bracketed clause noting the pointer was repointed by X1. |
| `ch08` | 71 | "the reason Chapter 4 §4.4 gives" | Chapter 1 §1.8 |
| `ch10` | 104 | "the boundaries drawn in Chapter 4" | Chapter 1 §1.7 |
| `ch10` | 165 | "exactly as Chapter 4 requires" | Chapter 1 §1.7 |
| `ch10` | 198 | "(§10.4, Chapter 4)" | (§10.4, Chapter 1 §1.7) |
| `ch10` | 217 | "when not to reach for an agent at all (Chapter 4)" | (Chapter 1 §1.7) |
| `ch11` | 348 | "the cost structure is the one Chapter 4 set out" | Chapter 1 §1.7 |
| `ch11` | 390 | "(§11.7; Chapter 4)" | (§11.7; Chapter 1 §1.7) |
| `ch15` | 137 | "the one that tests Chapter 4 §4.4" | Chapter 1 §1.8 |
| `ch15` | 144 | "the thesis of §4.4" | the thesis of Chapter 1 §1.8 |
| `ch16` | 77 | "Chapter 4 §4.4 makes that argument" | Chapter 1 §1.8 |
| `ch18` | 13 | "(Chapter 4)" in the durable-principles list | Handled in B4; becomes (Chapter 1) in Ch. 16 §16.7 |

**B3.7 — `ch00` "How to read this book".** One sentence changes: Part I's description names what an agent is, how to specify work for one, and how to build the loop that runs it. ≈25 words. **The five-part structure and everything else in the section stand.** The `[AUTHOR: …]` marker at line 34 about the eighteen-chapter structure stays exactly as written; §11, Q2 asks the author to reword it for seventeen.

**B3.8 — Retitle Ch. 1.** `# Chapter 1 — Why agents, why now, and where they don't belong`. **[PROPOSED]**; §11, Q1.

**B3.9 — Delete `manuscript/ch04-the-scientists-stance.md`** and `fig-brief/ch04-the-scientists-stance.md`, after B3.1 and B3.5 have moved everything out of both.

**B3.10 — Glossary.** No entry is tagged "(Chapter 4)" (verified 1 Aug 2026). Verify again after the merge rather than assume, and re-tag any entry whose canonical section moved.

---

### 5.4 — Batch B4: dissolving "What will last"

**B4.1 — New Ch. 16 §16.7.** Heading `## 16.7 Staying current by principle, not by release`, placed after §16.6 as the chapter's closing section. **≈750 words, of which ≈700 is relocated prose.**

Two movements, in this order.

*(a) The two layers, ≈200 words.* Ch. 18 §18.1's first three sentences and its durable/volatile lists, **in the author's 31 July wording**, moved verbatim. One change is mandatory: the clause tying the volatile layer to the repository as a medium goes, because the narrowed repository does not hold model names, prices or policy wording. What replaces it is one sentence saying that the volatile layer is deliberately not in print and that the text says where to look each item up. The limitation sentence about the boundary between the layers not always being obvious survives as the author left it. Its "(Chapter 4)" becomes "(Chapter 1)".

*(b) The filter, ≈500 words.* Ch. 18 §18.3 in full, verbatim, including its worked illustration of a frontier developer's self-report checked against an independent evaluation organisation. Add one opening clause tying it to §16.1, which already argues for capabilities over tools: this is that argument extended forward in time. ≈25 words.

**De-duplication check.** Ch. 17 §17.5 states the vendor-claim rule ("A self-reported capability figure is a hypothesis") without the worked example. **The example lives once, here in §16.7.** Add one clause to §17.5 pointing at it. ≈20 words. Do not move the rule out of §17.5; it is doing different work there.

Ch. 16 currently ends on the energy and carbon section, which is not an ending. This fixes that, which was the restructure's stated reason for choosing Ch. 16.

**B4.2 — Cut §18.2 and §18.4.** Neither survives (§3.4, §4.3). §18.4's European Commission living-guidelines citation moves to `ch00`'s living-book paragraph in B2.3 and travels on to the Preface in B7.

**B4.3 — Ch. 17's closing coda.** After §17.6, an unnumbered closing movement of **≈130 words**, before the cross-references line and the references. It carries Ch. 18's final sentence, lightly adapted so it closes a chapter about judging other people's work rather than a chapter about durability: what lasts is not any tool the book could have named but the stance towards tools it has argued for, which is to specify the work, verify the output, and keep the judgement and the accountability with the scientist. **This is the last paragraph of the book.** Two sentences of new connective prose at most.

**B4.4 — Delete the chapter and its figure.** Delete `manuscript/ch18-what-will-last.md`, `fig-brief/ch18-what-will-last.md`, `figures/figure-18-1.svg`, and the `figure-18-1` entry in `figures-src/f_ch13_18.py`.

**B4.5 — Inbound references.** Three sites name Chapter 18: `ch08`, `ch16` and the file's own self-reference. Repoint the first two to Ch. 16 §16.7 or delete, as the sentence requires. `FURTHER-READING.md`'s Part V heading becomes "(Chapters 9, 16–17)". Grep `Chapter 18` and `§18.` afterwards; both must return nothing.

**B4.6 — References.** Ch. 18's five references are all cited elsewhere (§3.4). Carry no reference list forward. Where a relocated sentence needs a reference entry in its new chapter, check whether that chapter already has it before adding: Ch. 16 already carries European Commission and METR; it does **not** carry Anthropic Institute, which §18.3's illustration needs. Add that one entry, copied verbatim from `ch18` including its URL, to Ch. 16's list. **That is the only reference-list addition in the whole of X1.**

---

### 5.5 — Batch B5: the new Chapter 4

**File:** `manuscript/ch04-the-harness.md`. **Title:** `# Chapter 4 — The harness: engineering the loop`. **Status header:** `draft r1`, conventions block copied from `ch16`. **Target: 3,650 words of body prose**, ceiling 4,000.

**Objective.** Give the reader the design decisions that determine whether an agent finishes correctly, cheaply and inspectably, at the level of durable pattern rather than named tool.

**Framing, which is not optional.** Frame every decision as a **control the reader exercises and can be held to**, not as an optimisation. The book's positioning is governance-first, and a chapter of engineering tips would weaken it. Framed as governing the loop, it strengthens the positioning claim instead: no existing treatment for environmental researchers covers harness design at all, let alone governably.

**Scope boundary.** This chapter is about the machinery around **one** agent. Composition of several agents stays in Ch. 2 §2.5 and Ch. 10. Whether the gates work stays in Ch. 11. Why the record must exist stays in Ch. 12. Where authority sits stays in Ch. 2 §2.6.

**Anatomy.** Part I, so the Part II anatomy does not bind. No verification checklist, no repository pointer, no "Adapting the pattern".

**Sections, with budgets and required content.**

- **4.1 The harness is the part you actually build.** ≈400 words. Opens on a concrete case per `STYLE.md`. Establish: the loop is the cycle, the harness is everything the cycle runs inside, and the second is where the design work is. Ch. 2 §2.1 already tells the reader the harness decides what an agent can do and then declines to say how to build one; this chapter is that. The sweep's theme A supplies the framing (a 2026 survey whose organising question is exactly this chapter's) and **no case material at all**, so the opening case is `[AUTHOR: a harness from your own operational work: which tools it held, what stopped it, and what it logged. The sweep found no published description of an environmental-science harness, so this opening is not available from the literature and only you can supply it.]`
- **4.2 Loop control: what stops a run.** ≈450 words. Success, failure, budget exhaustion, no-progress detection, escalation to a human, each named as a distinct termination condition. Step and token budgets and what happens when they run out. Evidence is adequate: the termination taxonomy and the unbounded-loop defect categories are supported, and budget-blind scaling plateaus. **No source recommends a number and none could**, so any default is the book's own judgement and carries a confidence flag. Point once to Ch. 3 §3.3, where stop conditions are a specification field: Ch. 3 is what you write down, Ch. 4 is what enforces it. Point once to Ch. 11 §11.2 for why run-to-run variation is an evidential problem and not only a reliability one. **Do not restate the loop**; Ch. 2 §2.2 owns it.
- **4.3 Retry, backoff and the error surface.** ≈450 words. Which errors are worth retrying, what changes between attempts, why retrying an unchanged plan amplifies a wrong one. How to design what a tool returns so the observe step is informative. This is the best-evidenced section in the sweep. **Treat backoff timing as ordinary engineering practice needing no citation**, as the sweep instructs. Extends Ch. 2 §2.2's claim that a silent wrong answer defeats the loop into guidance on preventing it. Cross-reference Ch. 13 for what the failures look like when it goes wrong.
- **4.4 The tool surface.** ≈400 words. How many tools, at what granularity, named how, with what argument schemas. Why fewer is usually better. Removal as a maintenance action. Evidence supports *fewer* and gives **no defensible single number; do not state one.** One domain-anchored source exists and is worth its sentence. Points to Ch. 2 §2.3, which owns tools as delegated weakness, and to Ch. 12 §12.8 for permission scope, which stays in Ch. 12.
- **4.5 Context assembly and compaction.** ≈450 words. What is resident every step, what is retrieved on demand, what is summarised away and what that loses. Delegation to a sub-agent as a context decision, pointing to Ch. 2 §2.5 rather than re-deriving it. This is the sweep's strongest section, eight sources, one peer-reviewed. **Guard against over-citing: three or four sources carry it.** Ch. 2 §2.4's mechanism (finite, ordered, lossy) stays in Ch. 2; only the design guidance is here.
- **4.6 State, logging and the run record.** ≈400 words. Scratch state, run directories, per-step logs. **The explicit distinction from Ch. 12, which is the section's spine:** this record exists so you can diagnose a run; the Ch. 12 record exists so someone else can hold you to account. Different purposes, different retention, one pointer each way. Add one clause noting that the same record is what bounds the damage when a gate is found to have been wrong (Ch. 12 §12.10). **No study evaluates whether a run record helps a human diagnose a run — zero sources.** The practical list of what to log is therefore the book's own judgement and must say so, with a confidence flag. The emerging telemetry standard may be named as emerging and unfinished; **no version number and no date go into print.**
- **4.7 Where a human interrupts.** ≈400 words. In the loop against over the loop. Batching approvals. Pause points chosen by consequence rather than by capability. **Open by naming this as the propose–dispose separation implemented (Ch. 2 §2.6), with the human as the disposer, and do not re-derive it.** That join is new since the brief was written and it is the strongest thing in the section. Point to Ch. 12 §12.8 for the permission argument. The sweep's key result on approval fatigue is a **modelling** result motivating a study; do not present it as measured. Reviewer disagreement on what counts as a risky action is worth one sentence, because it says the pause points cannot be inferred and must be chosen.
- **4.8 Cost and latency controls.** ≈350 words. Caps, cheaper models for cheap steps, parallelism, wall-clock budgets for operational deadlines. Points back to **Ch. 2 §2.7** for the accounting (not §2.6, which is now propose–dispose) and forward to Ch. 16 for the group-level cost model and to Ch. 16 §16.6 for induced demand. **Wall-clock budgets under operational deadlines have no source at all** — the sweep's largest hole, and exactly where the author's executed work is strongest: `[AUTHOR: a wall-clock budget from operational practice — what the deadline was, what the run had to do inside it, and what you gave up to meet it. The sweep found nothing in the literature on latency as an operational constraint.]`
- **4.9 Maintaining a harness.** ≈350 words. A harness built around a weaker model's limitations, and what happens when the model improves. **Prefer a trigger-based rule over a calendar cadence**, on the sweep's own reasoning that release velocity will date any stated cadence. Join to Ch. 1 §1.3's second disanalogy: a hosted model can be revised without notice, so the trigger is often invisible. Join to Ch. 11 §11.5's calibration validity: a harness tuned to one model is a calibration with a window. Both are pointers, not re-derivations.

**Citations.** From `research/2026-07-27-harness-and-loop-engineering.md` only. Read the report's section-by-section verdict table before drafting each section, and its coverage limits before citing any number. Two rules from the report bind absolutely: **structural findings transfer from software-engineering benchmarks and percentages do not**, so no absolute benchmark figure is carried into an environmental-science claim; and every entry in the report's volatile-figures register stays out of print under the vendor-neutral rule. Where a single-author preprint is the only support for a claim, hedge with a low-confidence flag or carry `[verify]`.

**Figures (four), specified in §6.**

**What the chapter displaces (executed in B6).**

**`[AUTHOR: …]` markers: two mandatory**, §4.1 and §4.8, as worded above. Add more where a section asserts a practice that one lived instance would turn into a description.

**Acceptance criteria (for ai-reviewer).**
1. Every section names at least one decision the reader makes, and states a default or says openly that no defensible default exists.
2. No named product anywhere in prose. No version number, no price, no benchmark percentage.
3. Every substantive claim is cited from the sweep, marked `[verify]`, or flagged as the book's own judgement with a confidence flag. The four places the sweep identifies as having **zero** sources are each flagged as the book's judgement or carry an `[AUTHOR: …]`.
4. No re-derivation of Ch. 2's anatomy, Ch. 2 §2.6's propose–dispose, Ch. 3's specification fields, Ch. 11's gate measurement or Ch. 12's least-privilege argument. Pointers only.
5. At least two `[AUTHOR: …]` markers, including §4.1's opening case.
6. Readable by someone who has not read Part II, and pointable-to from Part II without re-explanation.
7. Every decision is presented as a control the reader exercises, not as an optimisation.

---

### 5.6 — Batch B6: the displacement trim

Mandatory under the de-duplication rule, and it must follow B5 because you cannot point at a chapter that does not exist.

| Where | What moves | ≈ | Ruling |
|---|---|---|---|
| `ch02` §2.4, third paragraph | "treat context as a scarce, curated resource" guidance | −120 | Compress to a pointer. The mechanism (finite, ordered, lossy) stays in Ch. 2; the design guidance is Ch. 4 §4.5. |
| `ch02` §2.7 | cost *controls* | −80 | Controls move to Ch. 4 §4.8. The accounting and the "verification dominates cost" argument **stay** — the whole book rests on that argument and it must not move. |
| `ch02` §2.2 | stop-condition material | 0 | Stays. Ch. 2 names the condition, Ch. 4 designs it. |
| `ch03` §3.3 | stop conditions as a specification field | 0 | Stays. Clean line: Ch. 3 is what you write down, Ch. 4 is what enforces it. |
| `ch07` §7.3 | the four-gate stack | 0 | Stays. Add one sentence pointing to Ch. 4 for the general form. +25 |
| `ch12` §12.8 | least privilege and the trust boundary | 0 | **Stays in Ch. 12.** Ch. 4 treats permission scope as a harness parameter and points. Ch. 12 needs it for the institutional-IT argument and Figure 12.2. Add one clause pointing to Ch. 4 §4.4. +20 |
| `ch10` §10.1 | Kapoor et al. retry-loop finding | 0 | Stays, and is now Ch. 10's alone (B3.4). Ch. 4 may point to it and must not cite it again. |

Net ≈ −155 words.

---

### 5.7 — Batch B7: the Preface

**Position.** Opens `ch00-front-matter.md`, before "How to read this book". Unnumbered. **One front-matter file**, not two: splitting `ch00` would break the `chNN-slug.md` convention for no gain.

**Source.** `manuscript/PREFACE-EXAMPLES.md` §1, the A + C + D hybrid, adapted. It is a drafted candidate, not manuscript text, so adapting it is drafting work and is ai-writer's.

**Sections and budgets.**

- **P.1 (untitled opening).** ≈300–400 words. The concrete moment from operational practice, per `STYLE.md`'s rule that the case leads. Closes by naming the book's stance in one sentence, drawn from the moment rather than asserted over it. Carries the new `[AUTHOR: …]` marker for the opening moment, worded as in the restructure §6.6 and as drafted in the candidate.
- **P.2 What this book is, and what it is not.** ≈550–700 words. **Absorbs four things**: `ch00`'s contribution statement (the positioning claim, with its moderate-confidence hedge and its July 2026 scan caveat intact and **not strengthened by being moved**); the domain framing; **A1's scope statement**, including the three chapters the reviewer's finding required it to name (Ch. 8, Ch. 14, Ch. 15) and the sentence about experimental judgement staying with the scientist; and the living-book model in two or three sentences describing only what the repository will actually hold, carrying the European Commission living-guidelines citation. The prerequisites in one sentence, pointing forward to "What the reader needs". Deferrals stated as deferrals. Appendix A named as nine printed checklists.
- **P.3 How this book was made.** ≈300–400 words. Absorbs the disclosure statement. Agents used substantively in drafting, research gathering and review, each inside the specification, verification and audit discipline the chapters argue for. The firm limit: agents are never authors, and accountability rests with the named human author. Closes the Preface, and therefore the front matter's argument.

**Target: 1,200–1,400 words.**

**Figures.** None. The icon key stays where it is, as a front-matter reference section after "What the reader needs".

**Markers.** Four travel or arrive, none resolved: the new opening-moment marker; the `[AUTHOR SIGN-OFF]` on the scope framing, moved verbatim with the scope statement; and the two disclosure markers, moved verbatim including the one that says "once R1 completes" and the one that offers "with detail in the repository". **Both of the latter are stale and neither is edited by any agent**; §11, Q8. The foreword decision (restructure §6.5) is a fifth marker if the author wants it in the text; §11, Q9.

**A1's standing review comments** at the head of `ch00` travel with the scope statement to the Preface and stay standing, per `ADVERSARIAL-INTEGRATION-PLAN.md` §11.9.

**What stays in `ch00` after the Preface.** "How to read this book", "What the reader needs", the icon key. The contribution statement, domain framing, scope statement and disclosure statement sections are removed from their current positions, not duplicated.

**Scheduling.** P.1 and P.2 can be completed in this batch. **P.3 cannot be finished until X1 closes**, because it summarises what the agents did across a manuscript that is still changing. Draft it as a skeleton with its markers, exactly as the current disclosure statement does.

**Acceptance criteria (for ai-reviewer).**
1. Opens on a concrete case, not an abstraction and not a sentence announcing what the Preface is about to do.
2. No sentence duplicates Ch. 1 §1.1's framing of the field's problem. The Preface says why the *book* exists; Ch. 1 says why *agents* matter.
3. The positioning claim keeps its hedge and its scan caveat.
4. The scope statement's three named chapters survive the move, and its "governance" wording still agrees with Ch. 3 §3.7.
5. The disclosure names the limit on agent involvement and states that accountability rests with the named human author.
6. No promise of runnable examples, prompts, checklists, case studies or exercises. The living-book sentences describe only what the repository will actually hold.
7. All four markers present and unresolved.
8. Under 1,500 words.

---

### 5.8 — Batch B8: figures and the render pointer

1. **Render four new SVGs** for Ch. 4 from the briefs written in B5, through the house renderer, with the collision check passing.
2. **Rename** `figures/figure-4-1.svg` → `figures/figure-1-3.svg`; update `figures-src/f_ch02_04.py`.
3. **Delete** `figures/figure-18-1.svg` and its `figures-src/f_ch13_18.py` entry.
4. **Move the render pointer out of every caption.** All 57 figure blocks: strip the trailing `(Rendered as … per \`FIGURES.md\`.)` sentence from the caption, and add `<!-- brief: fig-brief/chNN-slug.md -->` on the line below the caption. Mechanical, entirely reviewable by diff. **[PROPOSED]**; §11, Q6.
5. **Full-set verification** on 57 figures: labels match the brief's `labels` field, annotations match `annotations`, role-colours correct, greyscale-readable, legible at half size.

---

### 5.9 — Pass A2, folded in

`ADVERSARIAL-INTEGRATION-PLAN.md` §11 scheduled a small mechanical pass. Every one of its items touches a file X1 already opens, so it runs inside X1's batches rather than after them.

| A2 item | Folds into |
|---|---|
| **11.1** propose–dispose info-box in `ch02` §2.6, plus its glossary entry | **B6** (which opens `ch02`) |
| **11.2** `*Constructed illustration.*` labels at `ch03` §3.7 and `ch12` §12.10, and the two conventions lines | **B2** (which opens both files) |
| **11.3** `GLOSSARY.md` em-dash sweep, 46 dashes on 32 lines | **B8** (back-matter batch) |
| **11.4** alt-text ceiling sweep, 45 alt-texts, each changed in the chapter and its brief in the same edit | **B8**. Recount first: the number changes with Figure 18.1 deleted and four new alt-texts written under the ceiling from the start. |
| **11.5** "rebound" and "induced demand" stay in the further-reading gaps | No action; the off-ramp stays open |

**Glossary additions for the harness chapter** (B8, ≈400 words): harness, termination condition, step budget, backoff, compaction, sandbox, observability. Each tagged "(Chapter 4)", each in the file's existing plain register, each written after the chapter is final so the definitions match. `FURTHER-READING.md` gains a harness-and-loop section drawing only on the 27 July sweep, ≈250 words, plus the Part V heading fix from B4.5.

---

## 6. Figures

**Four new, one renumbered, one deleted, one mechanical pass over all 57.** Every brief written in full per `FIGURES.md`, caption and alt-text written at the same time as the brief, in the v5.0 register, no metaphors, under the sentence ceiling from the start.

### 6.1 — New **Figure 4.1**, in ch04 §4.1

- **type:** architecture
- **claim:** The harness is everything around the model, and each of its parts is a decision someone made.
- **must show:** the plan–act–observe ring of Figure 2.1 reduced to a small central element, so a reader sees at once that the loop is the *small* part; around it, every control point the chapter covers, each labelled with the section that treats it — the tool surface, the context assembly, the state and run record, the termination and budget controls, the human interrupt, the cost and latency caps, the execution environment's reach. Each control point annotated with the decision it represents, not with what it is.
- **must not:** redraw the loop in detail. Figure 2.1 owns the loop; 4.1 owns what surrounds it, and the two must be visibly compatible.

### 6.2 — New **Figure 4.2**, in ch04 §4.2

- **type:** decision flowchart
- **claim:** A run ends for one of five reasons, and which one it was is the first thing you need to know.
- **must show:** the five termination conditions as distinct exits (success against the acceptance criterion, unrecoverable failure, budget exhausted, no progress detected, escalated to a human), the retry decision and what changes between attempts, and the point at which retrying an unchanged plan stops helping. A footer stating that a run which ends without recording *why* it ended has told you nothing.

### 6.3 — New **Figure 4.3**, in ch04 §4.6 or §4.7

- **type:** sequence
- **claim:** One governed run, with its budgets, its interrupt and its record all visible.
- **must show:** a single run from goal to result across the standard lanes, with the step and token budget drawn down as it proceeds, the human interrupt at the one consequential point, and what each step writes to the run record. Annotate the difference the chapter turns on: what this record is for (diagnosing the run) against what the Ch. 12 record is for (accounting for it).

### 6.4 — New **Figure 4.4**, in ch04 §4.9 or §4.3

- **type:** before/after
- **claim:** The same task, run by a naive loop and by an engineered one, and where the difference actually comes from.
- **must show:** two panels on one task. The naive panel: no budget, no no-progress detection, an uninformative tool error, everything in context, nothing logged, no pause. The engineered panel: the same task with each of those decisions taken. Annotate what each decision buys and what it costs. **No performance numbers**: the sweep's figures are benchmark-derived and do not transfer to this domain (X1, and the report's own coverage limits).

### 6.5 — Figure 4.1 (old) → **Figure 1.3** (B3.5). No content change beyond the identifier.

### 6.6 — **Figure 18.1 deleted** (B4.4).

**Figure count: 54 → 57.**

---

## 7. Admin documents

### 7.1 — `manuscript/OUTLINE.md` → **v0.8** — ai-editor, done in this pass

The reconciled structure, with everything the author has not confirmed marked **[PROPOSED]**.

### 7.2 — `CLAUDE.md` — ai-editor, batch **B1**, on the author's go-ahead

Four changes, and the first is overdue rather than new.

1. **The decision log records the four DECIDED items the author changed on 27 July 2026**, each with that date and that authority: exercises are not in this release and the manuscript no longer refers to the companion-repository build-out; the anatomy's seventh section is "Adapting the pattern" and Ch. 11, Ch. 12 and Ch. 17 owe a verification checklist only, and the fourth section is "worked example **or worked design**"; the repository's contents are stated (Markdown source, `/research` reports, further reading, figure briefs, per-release errata, and no code); and the length budget is restated. **None of these is in `CLAUDE.md` today**, which is a live contradiction between the file and the author's own instruction. On the fourth, see §8 and §11, Q7: the restated figure needs restating again.
2. **Repository layout** loses `/patterns`, `/prompts`, `/checklists`, `/case-studies` and `/exercises`, and gains the two appendix files.
3. **The vendor-neutral rule** currently routes named products and volatile figures to "`/patterns`, `/prompts` and repository docs". Those directories are going. Rewrite: capability classes and approximate years in print; named products and volatile figures do not appear in the book at all, and where a reader needs a current value the text says where to look it up.
4. **Current state** updated for X1 and for the fourth research report.

### 7.3 — `FIGURES.md` → **v2.2** — ai-editor, batch **B1**

One substantive amendment, §6.1: the caption no longer ends with the render pointer, and the HTML-comment form replaces it, given verbatim. §7's fifth quality check re-worded accordingly. Conditional on §11, Q6.

### 7.4 — Closed records, not edited

`REVISION-PLAN.md`, `RESEARCH-INTEGRATION-PLAN.md`, `ADVERSARIAL-REVIEW.md`, `ADVERSARIAL-INTEGRATION-PLAN.md` and `RESTRUCTURE-PROPOSAL.md` are records of what was planned and done. **None is edited by X1.** `RESTRUCTURE-PROPOSAL.md` gains one header line only, added by ai-editor, saying that it is superseded in execution by this plan and that its approval record §0 remains the governing author instruction. `CH01-STYLE-PASS.md` stays superseded.

### 7.5 — `.claude/agents/ai-writer.md`

Still scopes the writer to `ch01`–`ch17`. That is now correct by accident rather than by design. Flagged for the author, as `ADVERSARIAL-INTEGRATION-PLAN.md` §11.10 flagged it: agent definitions are configuration, and not ai-editor's to edit.

---

## 8. Length: the arithmetic, honestly

**Method.** Body prose is chapter-file words minus alt-text, captions and figure heading lines, which is the restructure's own measure. I also give a **print prose** figure, which additionally excludes status headers, standing review comments and reference lists, because none of those reaches a reader. Both are stated so the two bodies of work can be compared on the measure each used.

**Where the book actually sits, measured 1 August 2026.**

| | Words |
|---|---|
| 27 Jul baseline, 18 files, restructure measurement 1 | 66,097 |
| 1 Aug, 19 files, same measure | **79,293** |
| 1 Aug, print prose (also excluding headers, comments, reference lists) | **73,110** |
| A1's own accounting of what it added | ≈ +9,400 |

The gap between +13,196 and +9,400 is status headers, reference lists and standing review comments, which the restructure's measure counted and which do not reach print. A1's accounting was accurate.

**What X1 does to it, in print prose.**

| Item | Δ |
|---|---|
| New Ch. 4, the harness | **+3,650** |
| Preface, net of ≈600 words re-sited from `ch00` | **+400** |
| Appendix A, nine checklists, items only | **+2,400** |
| Appendix B, specification schema | **+350** |
| Six "Adapting the pattern" sections | **+1,200** |
| Ch. 17 closing coda | **+130** |
| Nine repository pointers deleted | **−1,640** |
| Ch. 18 dissolved, §18.1 and §18.3 relocated | **−800** |
| Old §4.5 deleted, Kapoor de-duplication, displacement trim | **−600** |
| **Net** | **+5,090** |

**≈78,200 words of print prose.** On the restructure's own page model of 350 words a page plus about 0.4 of a page per figure:

| | Pages |
|---|---|
| Prose | 223 |
| 57 figures | 23 |
| **Body total** | **246** |
| Glossary (3,752 words) and further reading (5,123 words) | 25 |
| **Including back matter** | **271** |

**Against a restated budget of 200–210 pages and 62,000–66,000 words of body prose.**

**What this implies, stated plainly.**

1. **The restated budget cannot be met by the trims the restructure scheduled.** Stage 10 was 1,500–2,500 words. Landing at 210 pages needs body prose down to about 66,000, which is a **reduction of 12,000 words**, five times as large. Presenting Stage 10 as the answer would be presenting a rounding error as a plan.
2. **The outline's "back matter ≈3 pp" is wrong by a factor of eight.** The glossary and the further reading are 8,875 words between them. Whatever the author decides, that number should be corrected, because it is currently hiding 22 pages.
3. **Three chapters hold 29 per cent of the book.** Ch. 11 (8,122 print words), Ch. 12 (7,598) and Ch. 13 (5,724) total 21,444. Any real reduction starts there, and Ch. 11 grew again in A1 by roughly 1,090 words on that plan's own budget.

**Three honest options, and my recommendation.** (a) Restate the budget again, to about 245 pages excluding back matter, and stop counting. (b) Commission a reduction pass of 10,000–12,000 words as a first-class piece of work with its own plan, targeting Ch. 11, Ch. 12 and Ch. 13. (c) Hold the appendices and back matter outside the printed page budget as reference matter, which buys about 30 pages and leaves 246. **I recommend (b), with (a) as the fallback and (c) taken anyway**, because a 246-page practitioner handbook is a normal object and a 271-page one is not, and because the material that would go in a reduction pass is material a reader has to get through before reaching Part IV. **This is not work X1 does.** §11, Q7.

---

## 9. Acceptance criteria

**Global, every batch.**

1. **No new source anywhere in the book except in Ch. 4**, which cites only `research/2026-07-27-harness-and-loop-engineering.md`. One reference-list entry is copied between chapters (B4.6) and no other reference list gains anything.
2. No `[AUTHOR: …]` marker resolved or edited. Two markers are deleted with the sections they annotate, both named in B2.1, and no other marker moves except with its passage.
3. Every passage flagged as the book's own judgement carries a calibrated confidence flag. The four zero-source areas in Ch. 4 each carry one or an `[AUTHOR: …]`.
4. All new prose sentence-per-line, British English, v5.0 voice indistinguishable from its surroundings, no metaphors, ~30-word ceiling, no em-dash connectors.
5. Relocated prose is relocated, not rewritten (X2). ai-reviewer diffs the moved text against its source and flags any change the move did not force.
6. Status headers advanced on every edited chapter.

**Renumbering and cross-reference greps (run as greps, not by eye).**

- `grep -rn "Chapter 4 §4\.4\|§4\.4" manuscript/` returns **only** references to the new Ch. 4's tool-surface section. **This is the X7 trap and it is the single most important check in the pass.**
- `grep -rn "Chapter 18\|§18\.\|figure-18-1\|ch18" manuscript/ fig-brief/ figures/ figures-src/` returns nothing.
- `grep -rn "scientists-stance\|figure-4-1" manuscript/ fig-brief/ figures/ figures-src/` returns nothing.
- `grep -rn "/patterns\|/prompts\|/checklists\|/case-studies\|/exercises\|companion repository" manuscript/ch*.md` returns nothing.
- `grep -rn "Repository pointer" manuscript/ch*.md` returns nothing.
- `## 1.5 Where an agent fits`, `## 1.6 Augmentation`, `## 1.7 A decision procedure`, `## 1.8 The frontier`, `## 1.9 What the rest of the book does` and `## 16.7 Staying current` all exist.
- Figure count is 57. `figure-1-3.svg` exists; every chapter's alt-text matches its brief's `alt-text` field word for word.

**Content spot-checks.**

- **ch01 §1.8:** the thesis arrives whole. Both objections present, movement (v) still has its own space, and the confidence flag is still moderate-to-high rather than high. A §1.8 that has lost the objections has failed the move.
- **ch01 §1.4:** carries the three definition sentences from old §4.5, and its forward pointer is internal.
- **ch04 (new):** no product name, no version number, no benchmark percentage, no cadence figure. Section 4.7 opens on the propose–dispose join and does not re-derive it. Section 4.6 states openly that its list of what to log is the book's judgement.
- **ch16 §16.7:** carries the author's 31 July wording for the two layers, the "two media" clause gone, and §18.3's worked illustration present once. Ch. 17 §17.5 points at it and does not repeat it.
- **ch17:** ends on the coda, not on the checklist, and the coda is the last paragraph of the book.
- **Preface:** the scope statement's three named chapters survived the move; the positioning claim's hedge and scan caveat are unchanged; nothing promises code.
- **Appendix A:** nine checklists, items only, no item reworded.

---

## 10. Execution order

Eight batches. B1 gates everything. B2 before B3. B3 before B5 and B6. B7 last but one.

| # | Batch | Files | Depends on | Why grouped |
|---|---|---|---|---|
| **B1** | **Admin documents** (ai-editor) | `CLAUDE.md`, `FIGURES.md` v2.2, `OUTLINE.md` v0.8 (done) | Author's answers to Q1–Q9 | Every later batch is executed by an agent reading these. The four DECIDED changes of 27 July have never been recorded and must be, before any writer works from `CLAUDE.md`. |
| **B2** | **Repository promises and appendices** (ai-writer) | `ch00`, `ch01`, `ch02`, `ch05`–`ch12`, `ch14`, `ch16`, `ch17`, two new appendix files | B1 | Nine deletions, six new sections, ~18 reworked sentences and two appendices are one editorial standard applied once. **Before the merge**, or `ch01` carries repository language that then has to be removed twice. Carries A2 ruling 11.2. |
| **B3** | **The merge** (ai-writer) | `ch01`, `ch03`, `ch08`, `ch10`, `ch11`, `ch15`, `ch16`, `ch00`, `ch04` (deleted), `fig-brief/`, `figures/`, `figures-src/` | B2 | The four moved sections, the figure renumber and the fourteen cross-references are one atomic change. Splitting it leaves the book referring to a chapter that half exists. |
| **B4** | **Dissolving "What will last"** (ai-writer) | `ch16`, `ch17`, `ch18` (deleted), `ch00`, `ch08`, `FURTHER-READING.md`, `fig-brief/`, `figures/`, `figures-src/` | B2 | Independent of B3 and can run alongside it, but both touch `ch16`, so sequence them rather than parallelise. |
| **B5** | **The new Chapter 4** (ai-writer) | `ch04-the-harness.md`, `fig-brief/ch04-the-harness.md` | B3 | The largest single piece of new writing since the first draft: 3,650 words and four figures. **Cannot start before B3**, because until the merge lands, "Chapter 4" means something else in fourteen places. |
| **B6** | **Displacement trim** (ai-writer) | `ch02`, `ch07`, `ch12` | B5 | You cannot point at a chapter that does not exist. Carries A2 ruling 11.1. |
| **B7** | **The Preface** (ai-writer) | `ch00` | B2, B3, B4, B5 | P.2 describes a book whose shape must be settled first, and its living-book sentences describe a repository whose contents B2 defines. |
| **B8** | **Figures and back matter** (ai-writer) | `figures/`, `figures-src/`, all chapter files, `GLOSSARY.md`, `FURTHER-READING.md` | B3, B4, B5 | Render, rename, delete, and the render-pointer pass across 57 figure blocks. Carries A2 rulings 11.3 and 11.4 and the harness glossary entries. |
| **B9** | **Review** (ai-reviewer) | everything | B8 | Full pass against `OUTLINE.md` v0.8, `STYLE.md` v5.0 and `FIGURES.md` v2.2, with particular attention to the X7 trap, the six new closing sections and cross-reference integrity. |

**Not in X1, and scheduled separately: the reduction pass.** 10,000–12,000 words, its own plan, after B9. §8, and §11, Q7.

**Off the critical path: the foreword** (restructure §6.5). Decide in principle now, commission after B9, and do not let it gate release. The living-book model makes that safe.

---

## 11. What the author must decide

Nothing below is executed until it is answered. Q1, Q3, Q4 and Q6 gate batches; the rest can be answered while work proceeds.

**Q1 — The Ch. 4 merge, now that Ch. 4 has grown.** The merge was approved on 27 July against a 1,629-word chapter. A1 has since made it 2,426 words by adding the bounded-payoff thesis. My recommendation is unchanged: merge, and carry the thesis into Ch. 1 as §1.8, which makes Ch. 1 nine sections and about 4,730 words, or 1.23× the chapter average. The alternative is to keep the stance material as a chapter and give Part I five chapters, with the harness as Ch. 5 and Part II starting at Ch. 6, which would renumber twelve chapters. **Confirm the merge, and confirm the new title "Why agents, why now, and where they don't belong".**

**Q2 — The chapter count.** Outline §9 currently records "18 chapters in 5 parts" as **[PROPOSED]** and awaiting you. Under X1 it is **17 chapters in 5 parts**. The `[AUTHOR: …]` marker in `ch00` line 34 asks you to confirm the eighteen-chapter structure; it is now the wrong question, and no agent may edit it. **Please reword or replace that marker.**

**Q3 — Part V.** The restructure dropped the Part V label because it would have held one chapter. A1's new chapter makes it two. I recommend restoring it, titled "Adoption and scrutiny", which also saves rewriting two navigational passages. **Confirm.**

**Q4 — "What will last", and your 31 July edit.** This is the one place where the evidence genuinely points two ways, and I am not resolving it silently. You approved the removal of this chapter on 27 July. You then edited it on 31 July, trimming eleven lines and adding eleven, on a branch where `RESTRUCTURE-PROPOSAL.md` did not exist. Your edit deleted the "central wager" paragraph, which is the passage the restructure named as the chapter's most exposed claim, so your instinct and the plan agreed. **My recommendation is to dissolve the chapter and preserve three of its four sections** (§3.4), which is more than the restructure preserved. Two specific things go, and you should see them named: **§18.2, "The principles that will last"** (≈350 words that you trimmed four days ago, cut because every one of the five principles has a canonical home elsewhere), and **Figure 18.1** with its SVG and brief (deleted because its "two media" claim is what the repository decision removes). **Confirm the dissolution, and confirm those two losses specifically.** If you would rather keep the chapter, say so: it stays as Ch. 18, §18.4 still has to be rewritten to stop promising code, and Ch. 16 keeps its weak ending.

**Q5 — The Preface candidate.** I recommend `PREFACE-EXAMPLES.md` §1, the A + C + D hybrid (§3.6). **Confirm, or name another.**

**Q6 — The render pointer, and the bold heading line.** I recommend moving the render pointer out of all 57 captions into an HTML comment, keeping `fig-brief/`, one file per chapter, exactly as you set it. I recommend keeping the bold figure heading line, weakly, and revisiting at the layout decision. **Confirm both.**

**Q7 — Length.** The 200–210 page budget you restated on 27 July cannot be met. The honest number is about 246 pages excluding back matter and 271 including it, and closing that gap needs a reduction of 10,000–12,000 words rather than the 1,500–2,500 the restructure scheduled. **Choose: restate the budget again, commission a real reduction pass, or hold the appendices and back matter outside the page budget.** My recommendation is a real reduction pass with its own plan, targeting Ch. 11, Ch. 12 and Ch. 13, plus holding the back matter outside the budget. §8.

**Q8 — Three stale `[AUTHOR: …]` markers.** No agent may edit these. (a) The disclosure marker saying "confirm the per-chapter agent-contribution summary once **R1** completes" — R1 closed weeks ago. (b) The disclosure marker offering "here in full or here in summary **with detail in the repository**" — the third option no longer exists in the sense it was written. (c) `FURTHER-READING.md`'s marker asking whether the gaps section belongs "in the printed back matter **or only in the repository**" — same problem. **Please reword all three.**

**Q9 — The foreword.** Restructure §6.5 recommends deciding in principle now, commissioning after review, and not letting it gate release. The marker it drafted is in `PREFACE-EXAMPLES.md`. **Do you want it in the Preface?**

**Still open from A1, untouched by X1 and still yours:** what Ch. 3 now closes on (`ADVERSARIAL-INTEGRATION-PLAN.md` §11.6), and `STYLE.md` §12's ban on addressing the reader as "you", which §1 requires (§11.7).

---

## 12. What genuinely cannot be preserved

Restated in one place, because the ledger is long and this is the part that matters.

1. **Ch. 18 §18.2** (≈350 words, trimmed by the author on 31 July). Cut under the DECIDED de-duplication rule. **Asked in Q4.**
2. **Figure 18.1**, its SVG and its brief. Cut because the approved repository decision removes the claim it is built on. **Asked in Q4.**
3. **Ch. 17 §17.7**, A1's repository pointer (≈150 words). Cut with the other eight under the approved repository decision.

Nothing else from either body of work is lost. Every other passage is in place, relocated with its markers and citations intact, or collected into an appendix, and §4 says which and where.

---

*Change control: ai-editor maintains this plan; ai-writer and ai-reviewer do not edit it. Discrepancies found mid-batch (an anchor sentence that has moved, a cut that would break an argument, a budget that cannot accommodate an instruction, a cross-reference target that does not exist) are raised in the batch's PR discussion and never silently resolved.*
