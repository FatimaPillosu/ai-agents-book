# Restructure plan

**v1.0 · 27 July 2026 · ai-editor · APPROVED BY THE AUTHOR. Not yet executed.**

The author approved this plan in full on 27 July 2026, including every item that required changing a DECIDED entry.
The approval record is §0 below.
This document is now the plan that ai-writer executes and ai-reviewer reviews against.

**Nothing has been executed yet.**
No chapter file, `CLAUDE.md`, `STYLE.md`, `FIGURES.md` or `OUTLINE.md` has been edited.
Where this document says what an admin document "will say", that wording is decided and awaits Stage 1.

---

## 0. Approval record (27 July 2026)

The author's instruction of 27 July 2026 approved all six decisions, added one, and changed one.

**Approved as proposed.**

1. The Ch. 4 merge into Ch. 1, and the new Ch. 4 on harness and loop engineering.
2. The harness chapter in Part I, after specification.
3. The living layer re-scoped to source, research reports, further reading and per-release errata.
4. Appendix A (verification checklists) and Appendix B (specification schema).
5. The length budget restated at around 200 to 210 pages.
6. The figure-brief extraction to `/figure-briefs`.

**Changed from the proposal.**

Ch. 17 is **removed**, not merged.
The proposal offered merging it into Ch. 16; the author instructed removal.
§1 below resolves what that means in practice, section by section.

**Added.**

A **Preface**.
§6 below proposes the types, recommends one, and gives its brief.

### DECIDED items changed by this approval

Each of the four items below was DECIDED and is changed on the author's explicit instruction of 27 July 2026.
`CLAUDE.md` and outline §9 must record that date and that authority, so a future agent reading only the admin documents can see why a DECIDED item moved.

| DECIDED item, as it stood | What it now says | Authority |
|---|---|---|
| "exercises live in `/exercises`, not the page budget" | Exercises are not in this release. The companion-repository build-out stays parked and the manuscript no longer refers to it. | Author, 27 Jul 2026 |
| "full chapter anatomy binds Part II only, with Ch. 11 and Ch. 12 still owing verification checklists and repository pointers" | The anatomy's seventh section is **"Adapting the pattern"**, not "repository pointer". Ch. 11 and Ch. 12 owe a verification checklist only. The fourth section is "worked example **or worked design**". | Author, 27 Jul 2026 |
| "unified repository with newsletter as update channel" | Not reversed. The repository's contents are now stated: Markdown source, `/research` reports, further reading, figure briefs, per-release errata. No runnable code, prompts, checklists, case studies or exercises. | Author, 27 Jul 2026 |
| "single ~150 pp volume" | Restated at **≈200 to 210 pages**, ≈62,000 to 66,000 words of body prose. Budgets remain indicative guidance. | Author, 27 Jul 2026 |

One further DECIDED item is **narrowed, not reversed**: "de-duplication now, one canonical home per recurring idea". It is the basis for cutting Ch. 17 §17.2, which recapitulates five arguments that each have a canonical home elsewhere.

---

## Executive summary

Sixteen chapters, not seventeen.
Ch. 4 (the scientist's stance) is section-sized and duplicates Ch. 1 §1.4, so it folds into Ch. 1, freeing the number for a new Ch. 4 on harness and loop engineering.
Ch. 17 is removed: of its four sections, one is deleted by the repository decision, one recapitulates material that has canonical homes elsewhere, and only §17.3 carries new argument, which moves to Ch. 16.
Chapters 5 to 16 keep their numbers, so no downstream cross-reference or figure identifier moves.
Part V does not survive as a part; Ch. 16 becomes a closing chapter after Part IV.

Remove the eight repository-pointer sections and replace each with a short "Adapting the pattern" section.
Promote the eight verification checklists to a printed appendix.
Move all 51 figure briefs out of the chapters into `/figure-briefs`, leaving the image, the caption and the alt-text in place.

A **Preface** opens the book, absorbing the contribution statement and the disclosure statement from ch00, opening on a concrete moment from operational practice and closing on how the book was made.
Recommended type is a hybrid: origin, then scope, then reflexive disclosure.

Net effect on length: about eleven pages out, about five in.

---

## What I read, and four measurements that shape everything below


Read in full: `CLAUDE.md`, `manuscript/OUTLINE.md` v0.5, `FIGURES.md` v2.0, `manuscript/ch02`, the relevant sections of `STYLE.md`, `REVISION-PLAN.md` §2 and `RESEARCH-INTEGRATION-PLAN.md` §§1–2.
Skimmed: every chapter file ch00 to ch17, by headings, status headers, opening sections, all eight repository-pointer sections, all 51 captions, and the sections named in the analysis below.
Listed: `/research` (three reports) and the figure directories.

Four measurements matter, and each is checkable.

**Measurement 1 — length.**
The eighteen chapter files hold 109,743 words.
Of those, 33,139 sit inside fenced `FIGURE BRIEF` blocks, 6,298 are alt-text, 3,795 are captions and 414 are figure heading lines.
Body prose is therefore **66,097 words** against an indicative budget of 38,000 to 42,000.
That is 1.65 times the midpoint.
At roughly 350 words a page, plus 51 figures and front and back matter, the book is currently around 210 to 220 pages, not 150.

**Measurement 2 — the directories in the admin documents do not exist.**
`CLAUDE.md` and outline §8 both name `/figures-source` for briefs and alt-text.
There is no such directory.
What exists is `/figures` (51 rendered SVGs) and `/figures-src` (10 Python renderer scripts).
Neither is named in either document.

**Measurement 3 — figure identifiers are contained within chapters.**
No chapter references another chapter's figure.
The single cross-file reference is ch00 referring to its own Figure 0.1.
A chapter merge therefore forces renumbering only inside the merged chapters, and never anywhere else.

**Measurement 4 — the admin documents are two passes stale, and contradict each other.**
`CLAUDE.md` says `FIGURES.md` is v1.0; it is v2.0, dated 26 July.
`CLAUDE.md` says figure captions and alt-text "have not yet been converted" to the v5.0 colloquial register.
I read all 51 captions.
They are in the colloquial register ("Two stores, one of which forgets", "Nothing about 42 looks wrong", "The line that decides what an attack can accomplish").
`FIGURES.md` v2.0 §6.1 and §6.2 already mandate that register.
The pending pass you were told about appears to have happened.
Separately, outline §9 says revision pass R1 is "under way".
R1 is closed and R2 has been executed, on the evidence of the post-execution reviewer notes in `RESEARCH-INTEGRATION-PLAN.md`.
The outline is the document declared authoritative, and it describes a project state two passes old.

---

## 1. Chapter count and merges

### The honest answer

No, not by count.
Seventeen chapters across 150 pages is about nine pages each, which is a normal shape for a practitioner handbook and suits a reader who will use the book by chapter rather than read it straight through.
The problem is not how many chapters there are.
The problem is that two of them are not chapter-sized and one subject that deserves a chapter does not have one.

Here is the body-prose distribution, which is what the argument rests on.

| Ch. | Subject | Body prose (words) | Against the 3,900 average |
|---|---|---|---|
| 1 | Why agents, why now | 3,474 | 0.89× |
| 2 | Anatomy of an agent | 4,238 | 1.09× |
| 3 | Specifying work for agents | 3,799 | 0.97× |
| **4** | **The scientist's stance** | **1,629** | **0.42×** |
| 5 | Evidence and literature synthesis | 4,151 | 1.06× |
| 6 | Data acquisition and quality control | 3,507 | 0.90× |
| 7 | Coding and pipeline agents | 5,086 | 1.30× |
| 8 | Model orchestration and experimentation | 4,510 | 1.16× |
| 9 | From results to manuscript | 4,703 | 1.21× |
| 10 | Multi-agent workflows | 5,278 | 1.35× |
| 11 | Verification and evaluation | 7,761 | 1.99× |
| 12 | Provenance, governance and security | 6,423 | 1.65× |
| 13 | The failure gallery | 5,892 | 1.51× |
| 14 | Verification under constraint | 4,730 | 1.21× |
| 15 | Governing a modelling workflow | 3,980 | 1.02× |
| 16 | Starting in your own group | 3,956 | 1.01× |
| **17** | **What will last** | **2,043** | **0.52×** |

(Figures are body prose only, with figure briefs, captions and alt-text excluded, so chapters with many figures are not flattered.)

Thirteen of the seventeen sit between 0.89 and 1.35 times the average.
That is a well-proportioned book.
The outliers are Ch. 4 and Ch. 17 at the bottom, and Ch. 11 at the top.

### Merge 1 — Ch. 4 into Ch. 1. Clean win, recommended.

Ch. 4 is the smallest chapter in the book at 1,629 words, and it duplicates Ch. 1.

Compare the two directly.
Ch. 1 §1.4 closes with this.

> "Past the merely unreliable is a third category that has nothing to do with capability … accountability, scientific judgement, and authorship. An agent cannot be responsible for a flood warning, cannot decide that an anomaly is real rather than an artefact, and cannot be an author of the paper that follows. None of these limits softens as models improve."

Ch. 4 §4.4 opens with this.

> "Three things in scientific work never transfer to a tool, however good the tool gets. Accountability … Interpretation … Authorship … No better model closes these limits, because none of them is a shortfall in capability."

That is the same claim, twice, forty pages apart, in a book where de-duplication to one canonical home is DECIDED.
There is a second duplication: Ch. 4 §4.2 cites Kapoor et al. (2024) for the finding that a plain model in a retry loop matches elaborate architectures, and Ch. 10 §10.1 cites the same paper for the same finding.

There is also an ordering fault.
Ch. 4 answers "should you delegate this at all", and it currently sits after Ch. 3, which answers "how do you specify what you delegate".
The "whether" question belongs before the "how" question.
`ch00` tells the reader "If you want to start doing the work, begin at Chapter 3", which sends a reader straight past the stance chapter and then back into it.

**Proposal.**
Merge Ch. 4 into Ch. 1 to make **Ch. 1 — Why agents, why now, and where they don't belong**, at roughly 4,600 words after de-duplication.
Ch. 4 §4.4 is deleted and its content is already in Ch. 1 §1.4, which absorbs any sharper phrasing.
Ch. 4 §4.1 (where an agent fits the scientific method) and §4.2 (augmentation and automation) become new Ch. 1 sections.
Ch. 4 §4.3 (the decision procedure) survives intact, with **Figure 4.1 becoming Figure 1.3**.
That flowchart is one of the most usable figures in the book and nothing about the merge threatens it.
The Kapoor citation is kept in Ch. 10 only, with a pointer from Ch. 1.

**Cost.** Ten "Chapter 4" cross-references across ch01, ch03, ch04, ch10, ch11 and ch17. One SVG renamed. One entry moved in `figures-src/f_ch00_01.py`. Ch. 1 §1.5 and ch00's "How to read this book" both rewritten, because both hard-code the chapter map.

### Ch. 17 — removed. What survives, and where it goes.

The author instructed removal rather than the merge the proposal offered.
That is the right call, and going through Ch. 17 section by section shows why: only one of its four sections carries argument that exists nowhere else.

**§17.1 "Two layers moving at two speeds" (about 700 words, plus Figure 17.1).**
Cut.
The whole section argues the print and repository division, and decision 3 re-scopes that division to something much smaller.
Figure 17.1 is deleted outright by decision 3, along with its brief and its rendered SVG.
The two-clocks argument survives in one sentence in the rewritten ch00 living-book paragraph, which is where a reader needs it.

**§17.2 "The principles that will last" (about 600 words).**
Cut.
This is five compressed restatements of arguments whose canonical homes are Ch. 1 (agent as instrument, and what never transfers), Ch. 3 (specification), Ch. 11 (external verification) and the new Ch. 4 material on when not to delegate.
De-duplication to one canonical home is DECIDED, and a chapter whose function is to say all of it again is exactly what that rule exists to prevent.
It is also the section most exposed to the length finding: 600 words that teach nothing new.

**§17.3 "Staying current by principle, not by release" (about 550 words).**
**Keep, and move to Ch. 16 as a new closing section.**
This is the only genuinely new material in the chapter.
The filter it proposes is practical and has no home anywhere else: translate every announcement into the book's vocabulary before deciding whether it deserves attention, ask which capability class it belongs to, and treat a faster or cheaper model of an existing class as a parameter change rather than a new thing to learn.
The second half, letting task-grounded evaluation rather than marketing decide what enters a workflow, connects directly to Ch. 11.
The worked illustration is good and should travel with it: a frontier developer's account of its own agents, treated as a hypothesis for independent measurement, checked against an outside evaluation organisation reaching the same result by a different method.

It belongs in Ch. 16 rather than anywhere else because Ch. 16 §16.1 already argues for capabilities over tools.
"Staying current by principle, not by release" is the same argument extended forward in time, and Ch. 16 currently ends on the energy and carbon section, which is not an ending.

**§17.4 "The repository as the living layer" (about 450 words).**
Cut, as decision 3 already required.
Two fragments are worth rescuing.
The European Commission living-guidelines citation is a good corroboration for the living-book model and should move to the rewritten ch00 paragraph, where that model is now stated.
The chapter's final sentence is the best closing line in the book and should become the final line of Ch. 16, lightly adapted.

**Citations.** I checked all five of Ch. 17's references against the rest of the manuscript.
Every one is cited elsewhere: Anthropic Institute in ch01, METR in ch01 and ch16, European Commission in ch09, ch15 and ch16, the Nature editorial in ch09 and ch15, Zheng et al. in ch10, ch11 and ch13.
**Removing Ch. 17 loses no citation**, which removes the main risk from a deletion of this size.

**Net.** About 1,750 words cut, about 550 relocated, one figure and one SVG deleted, one chapter file deleted.
Roughly five pages out of the book.

**Recommendation, stated plainly, as instructed.**
Cut, do not relocate, beyond §17.3 and the two fragments above.
The book is 1.65 times its original budget, and a closing chapter that mostly restates what the reader has just read is the least defensible material in it.
A reader who has worked through sixteen chapters does not need the five principles listed again.
The one thing Ch. 17 did that nothing else does, telling the reader how to stay current without chasing releases, is preserved in full and sits better in Ch. 16 than it did alone.

### What happens to Part V

Part V held Ch. 16 and Ch. 17.
With Ch. 17 gone it would hold one chapter, and a part of one chapter is a structural error rather than a structure.

Three options, and I recommend the third.

- **Keep Part V with one chapter.** Consistent with nothing else in the book, where parts hold two to six chapters.
- **Move Ch. 16 into Part IV.** Part IV is "Case studies". Ch. 16 is an adoption plan. It does not fit, and renaming Part IV to cover both would produce a label that describes nothing.
- **Drop the Part V label. Ch. 16 becomes a closing chapter standing after Part IV.** Recommended. Four parts and a closing chapter is an ordinary book structure, and at about 4,500 words after absorbing §17.3, Ch. 16 is substantial enough to stand on its own.

Both `ch00` "How to read this book" and Ch. 1 §1.5 currently describe five parts, and both are being rewritten for the merge anyway.

### Merges I considered and reject

**Ch. 14 and Ch. 15 into one case-study chapter.**
Forced.
They are different studies with different lessons: data sovereignty under constraint, and end-to-end governance of a modelling workflow.
Fusing them would produce a chapter with two unrelated halves and no argument connecting them.
Part IV's two chapters are also the evidence base for the positioning claim that this book is grounded in executed work, and presenting them as one study weakens that.

**Ch. 5 and Ch. 9 (the two text-facing patterns).**
Forced.
One is the input side of scholarship and one is the output side, and they are separated by the whole research lifecycle that Part II is organised around.
Merging them breaks the lifecycle ordering that gives Part II its shape.

**Ch. 6 and Ch. 7 (data and code).**
Forced.
"Agents propose, QC rules dispose" and "successive gates, human at the end" are two different governance patterns, and the book's whole method is to teach patterns one at a time with an identical anatomy.

**Ch. 10 into Ch. 15.**
Forced.
Ch. 10 is the pattern and Ch. 15 is one executed instance of it.
The book is careful, correctly, not to present designed work as executed work, and this merge would blur exactly that line.

**Ch. 13 into Ch. 11.**
Forced, and expensive.
The failure gallery is the canonical home for failure anatomy under the de-duplication rule, and every pattern chapter cross-references it.
It is also structurally different, being organised as failure and check pairs rather than as an argument.

**Splitting Ch. 12 into governance and security.**
This is the one case where the material argues for *more* chapters, not fewer.
Ch. 12 is 6,423 words across eleven sections covering three subjects.
I am not proposing it, because you asked about consolidation and because the two halves genuinely do share the claim that behaviour must be bounded, recorded and accountable.
Recording it here so the option is on file.

### The chapter map, before and after

**Decided: 16 chapters, four parts, and a closing chapter.**
One merged out (old Ch. 4), one deleted (Ch. 17), one added (harness and loop engineering, new Ch. 4).
**Chapters 5 to 16 keep their numbers, their filenames and their figure identifiers**, which is what keeps the execution cost low.

| Before (17 ch., 5 parts) | After (16 ch., 4 parts + closing ch.) | What happens |
|---|---|---|
| **Part I — Foundations** | **Part I — Foundations** | |
| 1 Why agents, why now | 1 Why agents, why now, and where they don't belong | Absorbs old Ch. 4. Figure 4.1 becomes Figure 1.3. |
| 2 Anatomy of an agent | 2 Anatomy of an agent | Trimmed: §2.4 and §2.6 shed material to new Ch. 4. |
| 3 Specifying work for agents | 3 Specifying work for agents | Unchanged. |
| 4 The scientist's stance | *(merged into Ch. 1)* | §4.4 deleted as duplicating Ch. 1 §1.4. |
| | **4 The harness: engineering the loop** | **New.** Brief in §2. |
| **Part II — Core patterns** | **Part II — Core patterns** | |
| 5 Evidence and literature synthesis | 5 (same) | §5.7 replaced by "Adapting the pattern". |
| 6 Data acquisition and quality control | 6 (same) | §6.7 replaced. |
| 7 Coding and pipeline agents | 7 (same) | §7.7 replaced. Pointer added to Ch. 4. |
| 8 Model orchestration and experimentation | 8 (same) | §8.8 replaced. |
| 9 From results to manuscript | 9 (same) | §9.8 replaced. §9.4 policy mechanism rewritten. |
| 10 Multi-agent workflows | 10 (same) | §10.8 replaced. |
| **Part III — Trust** | **Part III — Trust** | |
| 11 Verification and evaluation | 11 (same) | §11.9 replaced. |
| 12 Provenance, governance and security | 12 (same) | §12.11 replaced. §12.8 keeps least privilege, gains a pointer. |
| 13 The failure gallery | 13 (same) | Unchanged. |
| **Part IV — Case studies** | **Part IV — Case studies** | |
| 14 Verification under constraint | 14 (same) | Unchanged apart from §14.7. |
| 15 Governing a modelling workflow end to end | 15 (same) | Unchanged. |
| **Part V — Adoption** | *(part label dropped)* | |
| 16 Starting in your own group | **16 Starting in your own group** *(closing chapter)* | Gains §17.3 as a new closing section and Ch. 17's final line. |
| 17 What will last | *(removed)* | §17.1, §17.2, §17.4 and Figure 17.1 cut. |
| **Front matter** | **Preface**, then front matter | Preface absorbs the contribution statement and disclosure statement. §6. |
| **Back matter** | Back matter + **Appendix A**, **Appendix B** | Checklists and specification schema. §3. |

**Page effect.** Ch. 17 out is about five pages. Old Ch. 4 merged and de-duplicated saves about two. The repository sections are roughly neutral. Against that, the new Ch. 4 adds about nine to ten, Appendix A four to six, Appendix B one to two, and the Preface about three. Net is roughly plus eight to twelve pages on a book already at 210 to 220, which sits inside the restated 200 to 210 budget only if the trims in §5.6 are also taken.

---

## 2. Harness and loop engineering

### The gap is real, and the book already admits it

Ch. 2 §2.1 says this, in the draft as it stands.

> "one strand of practitioner commentary calls the whole assembly around the model the harness, and argues that the harness, more than the model at its centre, decides what an agent can actually do"

The book states that the harness decides what an agent can do, and then never says how to build one.
Ch. 2 is explicit that this is deliberate: "The purpose is diagnostic rather than architectural."
That was a reasonable choice for Ch. 2 and it leaves a gap nothing else fills.

Ch. 2 §2.4 makes a second promise it does not keep.

> "this curation is itself a design task with no sensible default."

Naming a design task with no sensible default, and then supplying no guidance on it, is the clearest statement of the gap I found.

### What "harness" and "loop" mean for this audience, vendor-neutrally

For a practising environmental scientist, the useful distinction is between the cycle and everything around the cycle.

**The loop** is the plan, act and observe cycle of Ch. 2 §2.2, plus the rules that govern how it runs and when it stops.
The engineering decisions are: what counts as done, what counts as failed, how many steps and tokens the run may consume, what happens when it makes no progress, which errors are worth retrying and how, and what a tool hands back when it fails.
The book currently covers the cycle and one clause of the stop condition, inside a figure.

**The harness** is everything the loop runs inside.
The engineering decisions are: which tools exist and how they are named and scoped, what enters the context window at each step and what gets summarised out of it, what state persists between steps and between runs, what the run writes to a log so a person can diagnose it afterwards, where the run pauses for a human, what the execution environment can reach, and what caps bound cost and wall-clock time.

Both are pattern-level and outlast any product, which is exactly the standard the book applies everywhere else.
A scientist reading this chapter should come away able to say, of their own workflow: this run stops after N steps or when the acceptance criterion is met, whichever comes first; these six tools and no others; this goes in the context every step and this is retrieved on demand; this is logged; a person approves here and nowhere else.

### Where it should land: a dedicated chapter, and pointers, not distribution

Distributing this material across existing chapters reproduces exactly the scattering that made it invisible.
Ch. 2 has the loop, Ch. 3 has stop conditions as a specification field, Ch. 7 has a gate stack for coding, Ch. 12 has permission scoping as a security control, Ch. 16 has cost.
Every piece is somewhere and the design problem is nowhere.
The de-duplication rule points the same way: one canonical home.

**Proposal: a new Ch. 4 — The harness: engineering the loop.**
Part I, after Ch. 3 (specification), before Part II.

Placing it after specification rather than before is deliberate.
The chapter's material enforces things the specification declares.
Stop conditions, acceptance criteria and the named reviewer are Ch. 3 fields, and the harness chapter is where they become machinery.
Putting it before Ch. 3 would demote specification from the "begin here" position `ch00` gives it, and would leave the harness chapter enforcing fields the reader has not met.

### Chapter brief (written so ai-writer can execute it and ai-reviewer can review against it)

**Objective.** Give the reader the design decisions that determine whether an agent finishes correctly, cheaply and inspectably, at the level of durable pattern rather than named tool.

**Scope boundary.** This chapter is about the machinery around one agent. Composition of several agents stays in Ch. 2 §2.5 and Ch. 10. Whether the gates work stays in Ch. 11. Why the record must exist stays in Ch. 12.

**Anatomy.** Part I chapter, so the Part II anatomy does not bind. Proposed sections:

- **4.1 The harness is the part you actually build.** Opens on a concrete case, per STYLE.md. `[AUTHOR: …]` for a harness from your own operational work: the tools it held, what stopped it, what it logged.
- **4.2 Loop control: what stops a run.** Success, failure, budget exhaustion, no-progress detection, escalation to a human. Each named as a distinct termination condition with a default. Step and token budgets and what happens when they run out.
- **4.3 Retry, backoff and the error surface.** Which errors are worth retrying, what changes between attempts, why retrying an unchanged plan amplifies a wrong one. How to design what a tool returns so the observe step is informative. Extends Ch. 2 §2.2's claim that a silent wrong answer defeats the loop, into guidance on preventing it.
- **4.4 The tool surface.** How many tools, at what granularity, named how, with what argument schemas. Why fewer is usually better. Removal as a maintenance action.
- **4.5 Context assembly and compaction.** What is resident every step, what is retrieved on demand, what is summarised away and what that loses. Delegation to a sub-agent as a context decision, pointing to Ch. 2 §2.5 rather than re-deriving it.
- **4.6 State, logging and the run record.** Scratch state, run directories, per-step logs. Explicit distinction from Ch. 12: this record exists so you can diagnose a run, the Ch. 12 record exists so someone else can hold you to account. Different purposes, different retention, one pointer each way.
- **4.7 Where a human interrupts.** In the loop against over the loop. Batching approvals. Pause points chosen by consequence rather than by capability, pointing to Ch. 12 §12.8 for the permission argument rather than restating it.
- **4.8 Cost and latency controls.** Caps, cheaper models for cheap steps, parallelism, wall-clock budgets for operational deadlines. Points back to Ch. 2 §2.6 for the accounting and forward to Ch. 16 for the group-level cost model.
- **4.9 Maintaining a harness.** A harness built around a weaker model's limitations, and what happens when the model improves. Scheduled reappraisal rather than one-off design.

**Figures (4).** 4.1 architecture, the whole harness with every control point annotated. 4.2 decision flowchart, termination and retry logic. 4.3 sequence, one governed run from goal to result with budgets and interrupts marked. 4.4 before/after, a naive loop and an engineered one on the same task. This matches the standard Part II set for type balance.

**Target.** 3,500 to 4,000 words body prose, roughly 9 to 10 indicative pages.

**Acceptance criteria (for ai-reviewer).**
1. Every section names at least one decision the reader makes, and states a default.
2. No named product anywhere in prose.
3. Every substantive claim is either cited from `/research`, marked `[verify]`, or flagged as the book's own judgement with a confidence flag.
4. No re-derivation of Ch. 2's anatomy, Ch. 3's specification fields, Ch. 11's gate measurement or Ch. 12's least-privilege argument. Pointers only.
5. At least one `[AUTHOR: …]` marker for a harness from executed operational work.
6. The chapter can be read by someone who has not read Part II, and Part II chapters can point to it without needing to explain it again.

### What it displaces

The de-duplication rule is DECIDED, so every one of these is a required cut, not an optional one.

| Where | What moves or goes | Approx. words | Ruling |
|---|---|---|---|
| Ch. 2 §2.4, third paragraph | "treat context as a scarce, curated resource" guidance | ~120 | Compress to a pointer. The mechanism (finite, ordered, lossy) stays in Ch. 2; the design guidance moves to Ch. 4. |
| Ch. 2 §2.6 | Cost *controls* | ~80 | Controls move to Ch. 4 §4.8. The accounting and the "verification dominates cost" argument stay in Ch. 2. That argument is one the whole book rests on and must not move. |
| Ch. 2 §2.2 | Stop-condition material | 0 | Stays. Ch. 2 names the condition, Ch. 4 designs it. Ch. 4 must not restate the loop. |
| Ch. 3 §3.3 | Stop conditions as a specification field | 0 | Stays. Clean line: Ch. 3 is what you write down, Ch. 4 is what enforces it. |
| Ch. 7 §7.3 | The four-gate stack | 0 | Stays. It is the coding instance of a general pattern. Add one sentence pointing to Ch. 4 for the general form. |
| Ch. 12 §12.8 | Least privilege and the trust boundary | 0 | **Stays in Ch. 12.** Ch. 4 treats permission scope as a harness parameter and points. Ch. 12 needs it in place for the institutional-IT argument and Figure 12.2. |
| Ch. 10 §10.1 | Kapoor et al. retry-loop finding | 0 | Stays. Ch. 4 may point to it; it must not be cited twice more. |

Total displaced prose: about 200 words. The new chapter is therefore close to net-new length, which matters for point 5.

### The blocking constraint: research coverage

I checked the three reports in `/research` for harness and loop material.
Coverage is thin and mostly grey literature.

What exists: seventeen mentions of "harness" in the practitioner-video report, chiefly Nate Jones on harness maintenance, world drift, harness co-evolution and "pruning beats piling"; Gaito's independent corroboration of the same concept; Mehta (2026) on silent semantic failures, which supports §4.3; Wang et al. (2026) on benchmark auditing; ReAct and stop conditions in the foundations sweep.

What does not exist: any substantial peer-reviewed or preprint coverage of tool-surface design, context compaction policy, retry and backoff for agents, step budgeting, or observability for agent runs.

That matters because of two binding rules.
Citations come from `/research` only.
And the R2 video policy, which you approved, limits video citations to one per chapter across seven named chapters, and states that video-derived concepts are corroborating colour and never primary evidence.
A new Ch. 4 is not among those seven.

**Consequence.** A harness chapter drafted today would rest on grey literature and the book's own judgement, which is thinner support than any other chapter in Part I.
**A targeted research sweep is a precondition, not a nicety.**
It can start immediately and run in parallel with everything else.

---

## 3. Removing the companion-repository promises

### Full inventory

**A. The eight repository-pointer sections. 1,489 words.**

| File | Section | Words |
|---|---|---|
| ch05 | §5.7 Repository pointer | 194 |
| ch06 | §6.7 Repository pointer | 167 |
| ch07 | §7.7 Repository pointer | 177 |
| ch08 | §8.8 Repository pointer | 182 |
| ch09 | §9.8 Repository pointer | 183 |
| ch10 | §10.8 Repository pointer | 330 |
| ch11 | §11.9 Repository pointer | 138 |
| ch12 | §12.11 Repository pointer | 118 |

**B. Named directory promises, inside and outside those sections.**

- ch05 §5.7: `/patterns/ch05-literature-synthesis`, runnable synthesis workflow, citation-verification gate as a separate script.
- ch06 §6.7: `/patterns/ch06-data-qc` end-to-end example, `/prompts`, `/checklists`.
- ch07 §7.7: `/patterns/ch07-coding-and-pipeline-agents`, and `/exercises` ("The exercises for this chapter, in `/exercises`, ask you to take one of your own run-once notebooks through the four gates"). Also carries `**[verify: confirm repository layout and exercise set before release.]**`.
- ch08 §8.7 (outside the pointer section): "Its printable form lives in the repository alongside the pattern."
- ch08 §8.8: `/patterns`, `/case-studies` (the three-track design as a sanitised case study), `/checklists`, `/prompts`.
- ch09 §9.8: artefact-linked manuscript example, `/checklists`.
- ch10 §10.8: `/patterns` roster skeleton, `/prompts` derivation template, `/checklists`, `/case-studies` ("will be deposited under `/case-studies` once that chapter's material is sanitised").
- ch11 §11.9: `/patterns/ch11-verification-and-evaluation`, evaluation-set template, seeded-defect harness.
- ch12 §12.11: `/patterns/ch12-provenance-governance-and-security`.

**C. Living-layer claims. These are a different kind of promise and need a different fix.**

- ch00, "How to read this book": "The companion repository holds everything that dates quickly: named tools, exact model versions, volatile figures, runnable examples and printable checklists."
- ch01 §1.4 closing: "the print holds the position and the reasoning, the companion repository tracks the movement".
- ch02 §2.6 closing, plus the `[AUTHOR: …]` marker after it (keep the marker, change the instruction inside it).
- ch09 header line, §9.4 twice: journal and funder policy specifics "held in the repository, not fixed in print".
- ch14 §14.7: methods and score definitions.
- ch16 header line, §16.1, §16.3, §16.6: volatile cost and energy figures.
- ch17 §17.1 twice, Figure 17.1 (caption, standfirst, on-canvas labels, alt-text and the whole brief), and **§17.4 "The repository as the living layer" in its entirety**.
- `FURTHER-READING.md`: `[AUTHOR: decide whether this gaps section belongs in the printed back matter or only in the repository]`.

**D. Admin documents.**

- `CLAUDE.md`: repository-layout line; the vendor-neutral rule, which routes named products to `/patterns` and `/prompts`; the DECIDED item "exercises live in `/exercises`, not the page budget"; the Parked item.
- `OUTLINE.md`: §3 "Runnable examples" bullet; §6 anatomy ending in "repository pointer (runnable example and optional exercises)"; §8 unified repository sketch; §9 DECIDED "exercises to the repository"; §9 DECIDED on the anatomy binding Part II "with Ch. 11 and Ch. 12 still owing … repository pointers"; §9 Parked item.
- `REVISION-PLAN.md` and `RESEARCH-INTEGRATION-PLAN.md`: both closed. Annotate as historical rather than edit.

**Scale.** Eight sections deleted, about twenty-five further sentences reworked, one whole chapter deleted (Ch. 17, per §1), one figure and its SVG deleted, four admin documents amended.

### The problem this exposes, which is larger than the deletion

Category C is not the same as categories A and B, and it is worth separating clearly.

Categories A and B promise runnable code, prompts, printable checklists, sanitised configurations and exercises.
Those are parked, so the promises go.

Category C promises something else: that current model names, per-token prices, journal policy wording and energy figures live in the repository and are kept current there.
Nothing in the repository holds any of that today, and the parked build-out was never going to supply it either.
So category C is an unbacked promise even after the runnable examples are removed.

This mattered most in Ch. 17 §17.1, which called the print and repository division "this book's central wager about how to write usefully for practitioners".
The Ch. 17 removal decided in §1 disposes of the most exposed version of the claim.
What is left is the version in ch00 and the scattered sentences of category C, and those still have to be narrowed rather than left standing.

**Decided (author, 27 Jul 2026): narrow the living layer to what will actually exist, rather than delete it.**
At release the repository holds: the full Markdown source; the dated verified research reports in `/research`; the annotated further reading; the figure briefs; and an errata and update note per release.
That is a genuine living layer with no code in it, and the newsletter remains the announcement channel, which is already DECIDED.

Rewrites that follow:

- **ch00**: promise the source, the dated research sweeps, the further reading and per-release errata. Delete "runnable examples and printable checklists".
- **ch17 §17.4**: superseded. The whole chapter goes, per §1. The two-layers argument survives as one or two sentences in the rewritten ch00 paragraph, and the European Commission living-guidelines citation moves there with it, because it is the one external corroboration that a living document is a responsible form for guidance in this area.
- **ch09 §9.4**: this one changes substantively. Replace "current specifics are held in the repository" with an instruction the reader can act on: check the journal's own current policy page before submission, and here is what the classes tell you to look for. That is more useful than the promise it replaces.
- **ch02 §2.6, ch16 §16.3 and §16.6**: state that the figures move and why, state the reasoning that survives, and name where a reader looks it up. Do not promise a maintained table.
- **ch01 §1.4**: "the print holds the position and the reasoning" survives; the clause about the repository tracking the movement narrows.

### What replaces the closing section of the Part II anatomy

Deleting the seventh section leaves the anatomy with six, and each Part II chapter ending on a checklist.
That is not terrible.
It is also not what the anatomy was doing, which was to hand the reader something to take away and to say honestly which parts of the chapter would date.

**Proposal: a new closing section, "Adapting the pattern", 150 to 250 words.**
Two parts, both short.
First, the two or three decisions a reader must make to apply this pattern in their own setting, stated as decisions rather than instructions.
Second, one sentence naming what in the chapter will date and how to check it.

This keeps the anatomy at seven sections, keeps the volatility disclosure that the repository pointer was carrying, gives the reader a genuine takeaway, and promises nothing that does not exist.
Net length change is close to zero: 1,489 words out, about 1,600 in.

Alternatives I considered.
Ending on the checklist and having six sections is clean and I would accept it if you prefer less new writing.
A "try this" section resurrects exercises, which are parked, so no.

### The checklists deserve to be in the book

The eight verification checklists (Ch. 5 to Ch. 12) are the most obviously reusable thing in the manuscript, and `/checklists` was the only place their printable form was ever promised.

**Proposal: Appendix A — Verification checklists.**
All eight collected in one place, in the standard format already defined in `REVISION-PLAN.md` §2.2, cross-referenced from each chapter as "the printable form is Appendix A".
This is assembly rather than new writing, because the checklists already exist and are already in the standard format.
Cost is about four to six pages, and it converts a parked promise into a delivered one.
I recommend this without reservation.

**Proposal: Appendix B — The specification schema.**
Ch. 3's seven fields as a blank template a reader can copy.
One to two pages.
It is the other artefact readers will want to lift out of the book, and Ch. 10 and Ch. 15 both depend on it, so a reader flipping between those chapters currently has to go back to Ch. 3 to find it.
Recommended, but weaker than Appendix A.

### What CLAUDE.md and the decision log must say instead

**Repository layout.** Replace the current line with the directories that will exist:

`/manuscript` (Markdown source; `OUTLINE.md`; `GLOSSARY.md`; `FURTHER-READING.md`; `ch00`–`ch17`; appendices) · `/research` (verified research reports; the sole source of manuscript citations) · `/figure-briefs` (one brief per figure) · `/figures` (rendered SVGs) · `/figures-src` (renderer scripts).

Note that this also fixes measurement 2: the current line names `/figures-source`, which does not exist, and omits `/figures` and `/figures-src`, which do.

**Vendor-neutral rule.** Currently routes named products and volatile figures to "`/patterns`, `/prompts` and repository docs". Those directories are going. Rewrite to: capability classes and approximate years in print; named products and volatile figures do not appear in the book at all, and where a reader needs a current value the text says where to look it up.

**Decision log.** Four DECIDED items change, all on the author's instruction of 27 July 2026. The wording each now carries is in the table in §0, and `CLAUDE.md` and outline §9 must both record the date and the authority alongside the change, so a future agent can see why a DECIDED item moved.

The Parked item on the companion-repository build-out stays parked and gains one clause: the manuscript no longer refers to it, so unparking it later is additive rather than a correction.

---

## 4. Moving figure material out of the chapters

### What is inside chapter files today

51 figure briefs, 33,139 words, **30 per cent of all chapter-file text**.
Distribution: ch00 1, ch01 2, ch02 3, ch03 2, ch04 1, ch05 3, ch06 4, ch07 4, ch08 4, ch09 4, ch10 4, ch11 3, ch12 2, ch13 6, ch14 3, ch15 2, ch16 2, ch17 1.

Each figure occupies four elements in the chapter file, in this order:

1. A bold heading line, for example `**Figure 2.1 — The plan–act–observe loop.**`
2. A Markdown image whose alt attribute carries the full alt-text, pointing at `../figures/figure-2-1.svg`
3. An italic caption paragraph ending `(Rendered as \`figures/figure-2-1.svg\` from the brief below, per \`FIGURES.md\`.)`
4. A fenced block holding the complete `FIGURE BRIEF`, including its own `caption:` and `alt-text:` fields

Elements 2 and 3 duplicate fields inside element 4.
Every caption and every alt-text therefore exists twice in the same file, and the two copies can drift.
Ch. 17 also has an inconsistency: line 484 carries a bold heading whose wording does not match its own caption.

### The governing principle

**Published text stays in the chapter. Production specification moves out.**

Captions and alt-text are published text.
They appear in the book, they are read by readers, they are bound by `STYLE.md` and reviewable by ai-reviewer as prose.
The brief is production material.
It is a specification for whoever renders the figure and it never appears in the book.

That cut is clean, and it answers the author's question directly.
A bare placeholder line is the wrong choice: a chapter reading `[FIG 2.1]` cannot be read as a book, ai-reviewer cannot check the caption's register, and you cannot read your own manuscript in the source.
A figure identifier and caption without alt-text is also wrong, because alt-text is published text under the accessibility commitment in `FIGURES.md` §6.2.

### The mechanism

**Stays in the chapter**, three elements, in this exact form:

```
![Full alt-text, as now.](../figures/figure-2-1.svg)

*Figure 2.1 — Caption, in the colloquial register, two or three sentences.*

<!-- brief: figure-briefs/figure-2-1.md -->
```

Changes from today: the bold heading line goes, being redundant with the caption; the "(Rendered as … from the brief below …)" pointer leaves the caption, because the brief is no longer below and production metadata does not belong inside published prose; an HTML comment carries the pointer instead, which is invisible in any rendering and findable by any agent.

**Moves out**: one file per figure at `figure-briefs/figure-2-1.md`, holding the complete brief per `FIGURES.md` §6, including its `caption:` and `alt-text:` fields.

**Naming.** `figure-briefs/figure-2-1.md` ↔ `figures/figure-2-1.svg` ↔ its entry in `figures-src/f_ch02_04.py`. One convention, three directories, mechanically checkable.

**On the directory name.** Do not call it `/figures-source`.
There is already a `/figures-src`, and two directories differing by four characters, one holding briefs and one holding Python, will be confused repeatedly by every future agent and by you.
`/figure-briefs` says what it holds.

### How numbering and cross-references survive

They survive because nothing about them changes.

- Figure identifiers stay `chapter.figure` and are untouched by the move.
- SVG filenames are untouched.
- The chapter keeps the image reference and the caption, so in-text mentions of "Figure 12.2" still resolve.
- **Measurement 3 applies**: no chapter references another chapter's figure, so no cross-file reference can break.

The only renumbering anywhere in this proposal comes from the Ch. 4 merge: Figure 4.1 becomes Figure 1.3, one SVG is renamed, one brief file is renamed, and one entry moves in `figures-src/f_ch00_01.py`.

### The caption and alt-text duplication

After the move, caption and alt-text still exist in two places: the chapter, and the brief file.
That duplication is worth keeping, because `CLAUDE.md` makes alt-text written at figure creation a hard rule, and creation happens in the brief.

**`FIGURES.md` must therefore state a precedence rule: the chapter file is authoritative for caption and alt-text. If the two differ, the chapter wins and the brief is corrected.**
Without that rule, an agent finding a discrepancy has no basis for deciding which to fix.

### What FIGURES.md must say

Four amendments, taking it to v2.1.

1. **New §6.0, "Where figure material lives".** The three directories, the naming convention, the exact three-element chapter block quoted verbatim, and the precedence rule.
2. **§6.1 amended.** The caption no longer ends with the render pointer. Give the HTML comment form instead.
3. **§6 preamble amended.** State that a brief is one file, not a fenced block inside a chapter.
4. **§7 amended.** Quality control reads the brief from `figure-briefs/`, and the fifth check becomes "the chapter's caption and alt-text match the brief's".

### The pending caption and alt-text style pass

`CLAUDE.md` says this pass is outstanding.
I read all 51 captions and the evidence says it is done.
They are colloquial, they open on content, they do not announce what the figure is about to do, and they carry the standfirst claim rather than restating the title.
`FIGURES.md` v2.0, dated 26 July, already mandates that register in §6.1 and §6.2, and the caption text matches it.

**Proposal.**
Do not schedule a conversion pass.
Instead, fold a **verification** pass into the extraction work, since every figure file is being opened anyway.
Check each caption and alt-text against `STYLE.md` §7, correct the few that fail, and then correct `CLAUDE.md`'s current-state paragraph, which is what is actually wrong here.
This is a much smaller job than the one you were expecting, and finding that out is worth the check.

---

## 5. What else the structure gets wrong

Ranked by importance. Nothing here is filler.

### 5.1 Length: decided at 200 to 210 pages, and the trims that decision still requires

66,097 words of body prose against a 38,000 to 42,000 budget was 1.65 times over, or roughly 210 to 220 pages against a 150-page target.

**Decided (author, 27 Jul 2026): the budget is restated at ≈200 to 210 pages, ≈62,000 to 66,000 words of body prose.**
This is the option I recommended, and it is the honest one: it keeps material already paid for, and 200 pages is an ordinary size for a practitioner handbook.

It is not, however, a decision to stop counting.
The restructure adds more than it removes.
Ch. 17 out and old Ch. 4 merged save about 3,300 words; the new Ch. 4 adds 3,500 to 4,000, and the Preface and two appendices add roughly another 2,500 in page-equivalent terms.
So the book lands near the **upper** end of the restated budget before any trimming, with no headroom.

**Consequence for the plan.** The trims named in §5.6 stop being optional.
Ch. 11 at 7,761 words and Ch. 12 at 6,423 are where to look, and a trim of roughly 1,500 to 2,500 words across the two would return the book to the middle of its restated range.
This is scheduled as Stage 10 and it is the one stage that can be dropped if time runs short, at the cost of a book at the top of its budget rather than the middle.

### 5.2 The admin documents are stale, and OUTLINE.md is the authoritative one

Measurement 4 above lists the specifics: `FIGURES.md` version wrong in `CLAUDE.md`, the caption pass wrongly described as pending, outline §9 describing R1 as under way when R1 is closed and R2 executed, and both documents naming a figures directory that does not exist while omitting two that do.

An agent handed only `OUTLINE.md`, which is the document declared authoritative, would plan against a project state two passes old.
An ai-reviewer comment already sits in the outline at line 119 saying exactly this.

**Recommendation.** Fix all of it in the same pass as the restructure, and do it first, because everything else is executed by agents reading these documents.
This is my work, not the author's, and it needs no decision beyond approval to proceed.

### 5.3 The repository removal took the book's closing argument with it

Covered at length in point 3, and now partly resolved by the Ch. 17 decision.
Ch. 17 called the print and repository division "this book's central wager", and that chapter is gone, which removes the most exposed statement of a claim the repository could no longer support.
What remains is the narrowed version, which goes into the rewritten ch00 living-book paragraph and must be written carefully: the repository holds the source, the dated research sweeps, the further reading, the figure briefs and per-release errata, and nothing else.
The European Commission living-guidelines citation rescued from Ch. 17 §17.4 belongs there, because it is the one piece of external corroboration that a living document is a responsible form for guidance in this area.

### 5.4 Part IV cannot ship on structure alone

Ch. 14 carries 15 `[AUTHOR: …]` markers and Ch. 15 carries 11, the two highest counts in the book.
Both chapters report executed work and both are, in their current state, scaffolds waiting for lived material only you can supply.
`[verify]` markers total 95 across the manuscript, with 22 in Ch. 11 alone.

No restructure changes this.
It is worth stating plainly because a restructure can feel like progress towards release when the actual constraint is elsewhere.

**Recommendation.** Whatever you decide below, the Part IV `[AUTHOR]` markers are the longest lead item in the project, and starting on them does not depend on any decision in this document.

### 5.5 The Part II anatomy fits five of its six chapters

The anatomy is: problem, conventional workflow, agentic redesign, worked example, failure modes, verification checklist, repository pointer.

It fits Ch. 5, 6, 7 and 9 cleanly.
It fits Ch. 8 with a caveat the chapter itself declares: §8.5 is titled "Worked design", not "Worked example", because the three-track intercomparison is designed and not executed. That is correct and honest, and it means the anatomy's fourth section is a different kind of thing in that chapter.
It fits Ch. 10 least well. Ch. 10 is a capstone that composes the preceding five patterns, and its "conventional workflow" section (§10.2, "distributed cognition in science") is a stretch to fit the template. Its most valuable section, §10.3 on independence against correlated opinion, has no place in the anatomy at all.

**Decided (author, 27 Jul 2026).** The fourth section of the anatomy becomes "worked example **or worked design**", which regularises what Ch. 8 already does, and Ch. 10 is recorded as following the anatomy loosely, as a capstone.
Ch. 10 is not forced into the template. It is the right chapter and the wrong template.

### 5.6 Part III is over its allocation, and Ch. 11 is twice the average chapter

Part III is 20,076 words, 26 per cent of body prose, against a 19 per cent indicative allocation.
Ch. 11 alone is 7,761 words, 1.99 times the chapter average and 12 per cent of the whole book.

Ch. 11 may deserve it.
The book says nobody should skip it, and it carries the evidential hierarchy, evaluation-set construction and gate measurement.
But it grew by 526 words in R2 against a 430-word cap, on the reviewer's own measurement, and nobody has asked whether it is now doing too much.

**Now required rather than optional**, per §5.1: the restructure leaves no headroom in the restated budget.
Ch. 11 and Ch. 12 are where to look first, for roughly 1,500 to 2,500 words between them.
Scheduled as Stage 10.

### 5.7 Adding a harness chapter shifts the book from governance towards engineering

Part II (patterns) is 27,235 words and Part III (trust) is 20,076.
The positioning claim is "a practical, governance-first, diagram-led treatment".
A harness chapter is engineering, and it sits in Part I, which is the smallest part.
Removing Ch. 17 sharpens this slightly, since the deleted §17.2 was the book's most concentrated statement of its governance principles.

I think this is right rather than wrong.
The book currently tells a reader to govern an apparatus it never tells them how to build, and that is a genuine defect the harness chapter fixes.
But the framing matters.

**Recommendation.** Frame the chapter as governing the loop rather than optimising it.
Every section should present its decision as a control the reader exercises and can be held to, which is the same stance the rest of the book takes towards specification and verification.
Then the positioning claim strengthens rather than weakens: no existing treatment for environmental researchers covers harness design at all, let alone governably.
That is a stronger positioning claim than the current one, and worth testing in the pre-release re-scan.

### 5.8 Two navigational passages hard-code the chapter map and break on any merge

`ch00` "How to read this book" names Chapter 3, Chapter 11, Chapter 13 and Part V by number.
Ch. 1 §1.5 "What the rest of the book does" lists every part and most chapters by number, and explicitly says "the stance to take towards the technology (Chapter 4)".

Both must be rewritten in the same commit as the merge, or the book will contradict itself in its first three pages.
Small job, easy to forget, high visibility if missed.

### 5.9 Glossary and further reading after the restructure

`GLOSSARY.md` was closed to edits by R2's rule G5.
That closure lapses with R2, and a harness chapter introduces terms that need entries: harness, termination condition, step budget, backoff, compaction, sandbox, observability.
`FURTHER-READING.md` needs a harness and loop section once the new research sweep lands, and its `[AUTHOR]` marker asking whether the gaps section belongs in print or in the repository needs re-asking, since the answer "the repository" is no longer available in the sense it was written.

### 5.10 R2 does not need to pause, but a new chapter needs a new sweep

R2 is complete, on the evidence of post-execution reviewer notes throughout `RESEARCH-INTEGRATION-PLAN.md`.
Nothing in this proposal requires it to pause or re-scope.

Two items R2 left unfinished, both flagged by ai-reviewer and both still unresolved, should be settled while chapters are being edited anyway.
First, the in-prose practitioner-commentary citation marker has three variants across the seven video-citing chapters, and one form should be decreed.
Second, the same person is rendered both "Jones, N. B." and "Nate B Jones" in different reference lists, and one convention should be fixed.
Both are mechanical and both are cheap to fix during a pass that is opening every file regardless.

The new sweep for the harness chapter is separate work and is described in point 2.

---

## 6. The Preface

Added on the author's instruction of 27 July 2026.

### 6.1 The complication: ch00 already carries preface-shaped material

This is not writing from nothing.
`ch00-front-matter.md` currently holds five sections, and two of them are preface material sitting under the wrong label.

| ch00 section today | What it actually is | Where it goes |
|---|---|---|
| How to read this book | Navigation | **Stays** in front matter, after the Preface |
| What the reader needs | Reference: prerequisites, non-targets | **Stays** in front matter |
| Icon key (Figure 0.1) | Reference | **Stays** in front matter |
| Contribution statement and domain framing | Why this book exists, and how far its examples travel | **Moves into the Preface** |
| Disclosure statement | How the book was made, and who is accountable | **Moves into the Preface** |

The contribution statement is already written as a preface: "This book occupies a narrow niche, and that is its reason for existing."
That is a first-person statement about why the book exists, which is the definition of preface material, and it is currently buried behind an icon key.
The disclosure statement is the same: a statement about the book's making, not about its subject.

So roughly 600 of the Preface's words already exist and need re-siting and re-opening, not inventing.

### 6.2 Preface, Introduction and Foreword are three different things

Worth stating plainly, because the three get used interchangeably and only one of them is actually open here.

A **Preface** is by the author, about the book: why it exists, how it came to be, what it promises, who it is for.

An **Introduction** is by the author, about the subject, and is part of the argument.
**This book already has one, and it is Chapter 1.**
Ch. 1 §1.1 opens on the state of the field and §1.5 lays out what the rest of the book does, which is exactly an introduction's job.
Adding a separate Introduction would duplicate Ch. 1, and de-duplication is DECIDED.
So the Introduction is not an option, and I am not offering it as one.

A **Foreword** is by someone other than the author.
It is treated separately in §6.5.

### 6.3 The menu of preface types

Seven types, each with what it opens on, length, what it demands from you, what it wins and what it risks.
`[AUTHOR: …]` in the "demands" column means lived material only you can supply.

**A. The origin and credential preface.**
*Opens on:* a specific moment in your operational practice that made the book necessary. A morning, a failure, a decision.
*Length:* 800 to 1,200 words.
*Demands:* heavy. `[AUTHOR: …]` for the moment itself, with enough specificity to be unmistakably yours.
*Wins:* establishes authority in the first paragraph, which is precisely the book's stated purpose, since the goal is credibility on agentic-AI work rather than revenue. It is also the one thing no other author could have written, and the section most likely to be excerpted well on LinkedIn.
*Risks:* drifts into memoir if the moment is not tightly chosen. Fails completely if written generically.

**B. The problem preface.**
*Opens on:* the state of agentic AI in the environmental sciences, with the book as corrective.
*Length:* 600 to 900 words.
*Demands:* little. Most of it exists as the contribution statement.
*Wins:* sharp positioning, stated before the reader has invested anything.
*Risks:* **it duplicates Ch. 1 §1.1 directly.** Ch. 1 already opens "Environmental science has a mismatch problem". Running the same argument twenty pages apart is exactly what the de-duplication rule forbids. I would not take this type on its own.

**C. The scope-and-contract preface.**
*Opens on:* what the book promises, what it refuses, what it assumes, what it deliberately excludes.
*Length:* 500 to 700 words.
*Demands:* almost nothing new. "What the reader needs" and the domain framing's deferral note already cover most of it.
*Wins:* protects both parties. A reader who knows the cross-domain examples are deferred to a later edition cannot be disappointed by their absence, and the book's honesty about its own limits is one of its better qualities.
*Risks:* reads as terms and conditions. Does nothing for credibility, and gives the reader no reason to care yet.

**D. The reflexive and disclosure preface.**
*Opens on:* the fact that this book was written with agents, under the governance it describes, so the preface is itself the first worked example.
*Length:* 700 to 1,000 words.
*Demands:* moderate to heavy. `[AUTHOR: …]` for the actual division of labour, and it cannot be completed until the manuscript is, because it summarises what the agents did per chapter.
*Wins:* genuinely distinctive. Almost no book on this subject can open this way, and it demonstrates the thesis instead of asserting it. Reflexive production is already a DECIDED principle, so this is delivering something the project has committed to rather than adding scope.
*Risks:* can read as self-regarding if it dwells. The existing disclosure statement carries two unresolved `[AUTHOR: …]` markers and is explicitly "a skeleton for now", so this section is the last part of the book that can be finished.

**E. The living-book preface.**
*Opens on:* the release model, versioning, and what dates fastest.
*Length:* 400 to 600 words.
*Demands:* little, but it needs rewriting anyway after the repository removal.
*Wins:* sets expectations about currency honestly.
*Risks:* administrative. It answers a question the reader has not yet thought to ask. **This is a section of a preface, not a preface**, and I recommend it be one or two sentences inside another type.

**F. The reader's-map preface.**
*Opens on:* routes through the book by role, for the practitioner, the research lead, the sceptic.
*Length:* 400 to 600 words.
*Demands:* nothing. This is "How to read this book", already written.
*Wins:* useful, and the existing version is good.
*Risks:* it is navigation, not a preface. Putting it first delays the reason to care until after the reader has been told how to care.

**G. The instrument preface** *(added; not on the list you were given).*
*Opens on:* the book's governing stance stated directly. An agent is an instrument, and environmental science already knows how to handle a fallible instrument, so the discipline needed is one the reader already has.
*Length:* 600 to 800 words.
*Demands:* light to moderate.
*Wins:* states the intellectual thesis in one page and travels extremely well as a standalone excerpt. It is also flattering to the reader in a legitimate way, telling them they already own the skill this book asks for.
*Risks:* abstract. `STYLE.md` requires the concrete case to lead, so it would have to open on a real instrument from your own work, at which point it has converged on type A with a different second paragraph. I raise it because that convergence is informative: it says the concrete opening is not optional.

### 6.4 Recommendation: a hybrid of A, C and D, in that order

**Open with A, compress C into a short middle, close with D.**

The reasoning is the sequence a reader actually needs.
They need to know who is speaking and why they should listen (A), then what they are being promised and what they are not (C), then what kind of object they are holding and how far to trust it (D).
Ending on the disclosure is the strongest available move, because it hands the reader the means to judge the book at the exact moment they are deciding whether to read it, and because a book arguing that agentic work must be disclosed and audited should disclose and audit itself before it asks anyone else to.

B is excluded because it duplicates Ch. 1 §1.1.
E and F are absorbed: E as two sentences inside the C movement, F left where it is as a separate front-matter section immediately after the Preface.
G is absorbed into A, because A's concrete opening is where the instrument stance is best demonstrated rather than announced.

### 6.5 The Foreword, which is a separate decision

A foreword is written by someone other than the author, and it is worth raising because it is a real option you may not have considered.

**The case for.** The book's stated purpose is author credibility on agentic-AI work.
A foreword from a recognised name in operational forecasting, environmental modelling or research software engineering transfers credibility in a way nothing you write about yourself can, because it is someone else's judgement rather than your own claim.
For a self-published free book with no publisher's imprint behind it, that external signal does work that the imprint would otherwise do.
It also widens the first readership, since a foreword writer usually shares the release.

**The cost, stated honestly.**
It needs a person, which means an invitation, a near-final manuscript to read, and a reply.
Realistically four to eight weeks of calendar time, most of it outside your control.
It cannot sensibly be commissioned until the Part IV `[AUTHOR: …]` markers are resolved, because anyone writing a foreword will read the case studies and those are the chapters that are currently scaffolds.
There is also a soft cost: asking someone to endorse a book obliges you in a small way, and it is worth being sure you want the association.

**Recommendation.** Decide in principle now, commission after Stage 8, and **do not let it gate release**.
The living-book model is what makes this safe: v1.0 ships without a foreword, v1.1 adds one, and the versioning already announced makes that an ordinary release rather than a correction.
That converts a four-to-eight-week dependency into no dependency at all.

`[AUTHOR: decide whether to invite a foreword, and from whom. If yes, the invitation goes out after the restructure is reviewed, and the book does not wait for it.]`

### 6.6 Preface brief (same form as the Ch. 4 brief)

**Position.** Opens `ch00-front-matter.md`, before "How to read this book". Unnumbered, as front matter.

**On file structure.** Keep one front-matter file with the Preface as its first section, rather than splitting `ch00` in two.
Two `ch00` files would break the `chNN-slug.md` convention, and the front matter is short enough to stay together.

**Objective.** Give the reader, in about three pages, the reason this book exists, who wrote it and on what authority, what it promises and refuses, and how it was made, so they can decide whether to trust it before they invest in it.

**Sections.**

- **P.1 (untitled opening).** The concrete moment from operational practice, per `STYLE.md`'s rule that the case leads. What was at stake, what the work actually consisted of, and what made a governed agentic approach necessary rather than interesting. Closes by naming the book's stance in one sentence, drawn from the moment rather than asserted over it. 250 to 400 words.
- **P.2 What this book is, and what it is not.** Absorbs the contribution statement and domain framing from ch00, re-opened so it does not start on "This book occupies a narrow niche". The positioning claim with its moderate-confidence hedge intact. The prerequisites in one sentence, pointing forward to "What the reader needs". The deferrals stated as deferrals: cross-domain examples to a later edition, and the living-book release model in two sentences. 300 to 400 words.
- **P.3 How this book was made.** Absorbs the disclosure statement. Agents used substantively in drafting, research gathering and review, each inside the specification, verification and audit discipline the chapters argue for. The firm limit: agents are never authors, and accountability for every claim rests with the named human author. Closes the Preface. 300 to 400 words.

**Target length.** 900 to 1,100 words, about three pages.

**Figures.** None. The icon key stays where it is, as a front-matter reference section.

**`[AUTHOR: …]` markers it will carry.** Three carried forward, one new. None may be resolved by any agent.

1. New, for P.1: `[AUTHOR: the opening moment. A specific piece of operational work where the volume, the deadline or the checking burden made a governed agentic approach necessary. Name what was at stake and what you actually did. This is the paragraph the whole Preface rests on and only you can write it.]`
2. Carried from ch00: `[AUTHOR: confirm the per-chapter agent-contribution summary once the restructure completes — which agents did what, drawn from the chapter status records.]`
3. Carried from ch00: `[AUTHOR: decide the granularity of the disclosure — per chapter or per task — and whether it lives here in full or here in summary.]` The second half of this marker must be rewritten, since "with detail in the repository" is no longer available in the sense it was written.
4. New, from §6.5: the foreword decision.

**Acceptance criteria (for ai-reviewer).**

1. The Preface opens on a concrete case, not on an abstraction and not on a sentence announcing what the Preface is about to do.
2. No sentence duplicates Ch. 1 §1.1's framing of the field's problem. The Preface says why the *book* exists; Ch. 1 says why *agents* matter.
3. The positioning claim keeps its hedge and its July 2026 scan caveat. It is not strengthened by being moved.
4. The disclosure names the limit on agent involvement explicitly, and states that accountability rests with the named human author.
5. No promise of runnable examples, prompts, checklists, case studies or exercises. The living-book sentences describe only what the repository will actually hold.
6. All four `[AUTHOR: …]` markers present and unresolved.
7. Under 1,200 words.

**Scheduling.** P.1 and P.2 can be drafted at Stage 9. **P.3 cannot be completed until the restructure is finished**, because it summarises what the agents did across a manuscript that is still changing. Draft P.3 as a skeleton with its markers, exactly as the current disclosure statement does, and complete it at the end.

---

## Order of operations, and what it costs

Sequence matters here, because three of these jobs touch every chapter file and doing them in the wrong order means doing some of them twice.

**Stage 0 — Decisions (author). COMPLETE, 27 July 2026.**
All six decisions taken, four DECIDED items changed, Ch. 17 removed, Preface added. Record in §0.

**Stage 1 — Admin documents (ai-editor, no manuscript touched).**
`CLAUDE.md`: current state (correcting the four staleness findings in measurement 4), repository layout, vendor-neutral rule, and a decision log recording the four DECIDED changes with the 27 July 2026 authority.
`OUTLINE.md` to v0.6: the chapter map in §1, four parts plus a closing chapter, revised anatomy, corrected §8, refreshed §9, restated budget, Preface and appendices in the structure.
`FIGURES.md` to v2.1 with the four amendments in point 4, plus deletion of the Figure 17.1 entry.
A chapter-level execution plan ai-writer works from and ai-reviewer reviews against.
*Cost: low. Blocks everything else, so it goes first.*

**Stage 2 — Figure extraction (ai-writer, mechanical).**
Move 51 briefs to `/figure-briefs`. Leave image, caption and alt-text. Verify caption and alt-text against `STYLE.md` §7 while each file is open.
*Cost: 18 files, 33,139 words relocated. Low risk, entirely reviewable by diff.*
**Do this before any merge or rewrite.** It removes 30 per cent of the volume from every chapter file, which makes every later diff readable. Running it after the merge means moving ch04's brief twice.

**Stage 3 — Research sweep (ai-researcher, parallel).**
Targeted sweep on harness and loop engineering: termination and budgets, retry and backoff, tool-surface design, context compaction, agent observability, human interrupt patterns.
*Cost: one sweep. Starts at Stage 1 and runs alongside Stages 2 to 4.*
**This gates Stage 6 and nothing else.**

**Stage 4 — Repository removal (ai-writer).**
Delete the eight pointer sections. Write eight "Adapting the pattern" sections. Rework the twenty-five scattered sentences. Rewrite ch17 §17.4 and rework Figure 17.1 including its SVG. Rewrite ch00's living-layer paragraph and ch09 §9.4's policy mechanism. Assemble Appendix A and write Appendix B.
*Cost: medium. About 1,500 words out, 1,600 in, one section rewritten, one figure re-rendered, two appendices.*

**Stage 5 — The merge, and the Ch. 17 removal (ai-writer).**
Fold ch04 into ch01. Figure 4.1 becomes Figure 1.3, with the SVG and the `figures-src` entry moved. Delete ch04 §4.4 as duplicated. Keep Kapoor in Ch. 10 only. Fix ten "Chapter 4" cross-references.
Move ch17 §17.3 into ch16 as a new closing section, carry the four references it needs, and adapt Ch. 17's final sentence as Ch. 16's last line. Move the European Commission citation to the ch00 living-book paragraph. Delete `ch17-what-will-last.md`, `figures/figure-17-1.svg` and its `figures-src` entry. Fix the three "Chapter 17" cross-references in ch08 and ch16.
Rewrite ch00 "How to read this book" and Ch. 1 §1.5 for four parts and a closing chapter.
*Cost: medium. About 1,750 words cut and 550 relocated on top of the merge.*
**Must follow Stage 4**, or both chapters carry repository language that then has to be removed again.

**Stage 6 — The new Ch. 4 (ai-writer).**
Draft against the brief in point 2, with four figure briefs written at the same time per the alt-text rule, and rendered.
*Cost: high. This is the largest single piece of new writing since the first draft: 3,500 to 4,000 words plus four figures.*
**Gated by Stage 3.** Drafting it before the sweep means writing a Part I chapter on grey literature, which no other chapter in the book does.

**Stage 7 — De-duplication trim (ai-writer).**
The displacement edits in the table in point 2: ch02 §2.4 and §2.6, ch07 §7.3, ch12 §12.8 pointers.
*Cost: low, about 200 words.*
**Must follow Stage 6**, because you cannot point at a chapter that does not exist yet.

**Stage 8 — Review (ai-reviewer).**
Full pass against the revised `OUTLINE.md`, `STYLE.md` and `FIGURES.md` v2.1, with particular attention to the new Ch. 4, the eight new closing sections, and cross-reference integrity after the merge and the Ch. 17 removal.

**Stage 9 — The Preface (ai-writer).**
Draft P.1 and P.2 in full per the brief in §6.6. Draft P.3 as a skeleton carrying its markers. Re-site the contribution statement and disclosure statement out of their current ch00 positions.
*Cost: low to medium. 900 to 1,100 words, no figures, but about 600 of them are re-siting rather than new writing.*
**Must follow Stage 8**, because P.2 describes a book whose shape must be settled first.

**Stage 10 — Length trim (ai-writer).**
The Ch. 11 and Ch. 12 trims of §5.6, roughly 1,500 to 2,500 words.
*Cost: medium. This is judgement work, not mechanical.*
**Must come last.** Trimming before the harness chapter and the Preface exist means trimming, then adding, then trimming again.
This is the one stage that can be dropped if time runs short, at the cost of a book at the top of its restated budget rather than the middle.

**Stage 11 — Foreword (author, optional, off the critical path).**
Invitation goes out after Stage 8. Does not gate v1.0. See §6.5.

**Completion of P.3.** The disclosure statement's per-chapter summary can only be written once Stage 10 closes, since it describes work that is still happening until then.

### What it costs to do nothing

Worth stating, since "no" is a legitimate answer to any of this.

- Leave the chapter count alone: the book keeps a chapter that duplicates another and sits in the wrong place. Low cost, real but small.
- Leave harness and loop out: the book keeps a stated claim it does not develop, and a reader who decides to build something has to go elsewhere for the most practical part. In my judgement this is the largest single defect in the current structure.
- Leave the repository promises in: the book promises readers material that will not exist when they look for it. This is the only item in this document I would call a correctness problem rather than a quality problem.
- Leave the figure briefs in the chapters: chapter files stay 30 per cent production material, every caption exists twice with no precedence rule, and prose review stays harder than it needs to be.
- Leave the length question deferred: the decision gets taken by default at the moment of release, when it is most expensive.

---

## Status, and what ai-writer needs next

Every decision in this document is taken.
Nothing here is waiting on the author except the `[AUTHOR: …]` material named in §6.6, the foreword decision in §6.5, and the Part IV lived material described in §5.4, none of which blocks Stage 1.

**Immediate next step: Stage 1.**
ai-editor updates `CLAUDE.md`, `OUTLINE.md` to v0.6 and `FIGURES.md` to v2.1, and writes the chapter-level execution plan.
No manuscript file is touched at Stage 1.

**Running in parallel from now: Stage 3**, the ai-researcher sweep on harness and loop engineering, which gates Stage 6 and nothing else.

**What is not in this plan, and stays out.**
The companion-repository build-out remains parked.
Permissions and IP for case studies remain parked.
Output format, licence, DOI and build toolchain remain deferred, and are not gates.
The working title remains open, and the Preface is written so that it does not depend on the title being settled.