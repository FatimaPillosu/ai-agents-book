# Chapter 1 style pass — resolve the author's `[human: …]` comments and apply STYLE.md v2.1

**v1.0 · 25 July 2026** · Maintained by ai-editor. Executed by **ai-writer**; reviewed against by **ai-reviewer**. This note is the single instruction set for the pass; a writer needs this file, `STYLE.md` v2.1 and `manuscript/ch01-why-agents-why-now.md` — nothing else. Work happens on the existing branch of PR #4 (no new branch, no new PR).

## Background

The author has hand-edited ch01 §1.1 and left inline comments in the form `[human: …]`. These are the author's live editorial feedback; some contain typing errors — read for intent. The durable rules arising from them are now codified in `STYLE.md` v2.1 (plain-formal register; no contractions; no em-dash connectors; substantive openers; no emphasis-only sentences). This pass (a) resolves each comment in the prose, and (b) applies v2.1 uniformly across the whole of Chapter 1 so §1.1 does not read differently from §1.2–1.5.

## Task 1 — resolve every `[human: …]` comment in §1.1

For each comment: revise the sentence(s) it targets per the comment's intent and STYLE.md v2.1, then **delete the comment**. Do not touch any `[AUTHOR: …]` or `[ai-reviewer: …]` marker anywhere; their count must be unchanged after the pass.

- **C1 (§1.1 first paragraph, the "don't look first at the models" opener).** The author finds it vague and sensationalistic. Replace the opener with a sentence that states the section's actual claim plainly (the mismatch between growing data volumes and obligations on one side and fixed working hours on the other), with no rhetorical inversion or hook.
- **C2 ("The supply side has grown relentlessly").** "Supply side" has no stated referent. Name explicitly what has grown (data volumes and the obligations attached to them), in plain formal language; keep the `[AUTHOR: …]` verification marker in that sentence intact.
- **C3 ("Every one of those streams carries obligations…").** The author has already deleted short filler sentences here and objects to the pattern. Do not reintroduce any; check the surviving paragraph reads as connected prose after her deletions and smooth only where grammar requires.
- **C4 ("What hasn't grown…").** The author likes this sentence; change only "hasn't" to "has not". This sentence is the model for an acceptable short sentence: it carries a complete substantive point.
- **C5 ("Software that can actually act — read a file…").** Remove the em-dash construction per v2.1 (e.g. introduce the examples with "such as" or "e.g.", or restructure); keep the sentence's content, add nothing decorative. The author's broader note (sentences added for their own sake) applies to the whole section: any remaining sentence in §1.1 that carries no information should go.
- **C6 ("The claims made for these systems are enormous…").** Content approved, style rejected. Rewrite in simpler, plainer formal language per v2.1 §1, preserving the three-part claim (big claims, polarised commentary, normal for the technology's stage).
- **C7 ("The case for engaging now…").** Same as C6: content stands, restyle plainly.
- **Hand-edited sentence ("My own position fall in betwee that one of the enthusiasts…").** No comment attached, but the author's hand edit left grammatical errors. Repair grammar only, preserving her meaning exactly; apply v2.1 to its punctuation (the em-dash aside "— powerful, fallible, and fit for serious work…" must be restructured).

## Task 2 — apply STYLE.md v2.1 through §1.2–1.5 and the header

- Remove every contraction in the chapter outside verbatim quotations (current examples include "don't", "I'll", "I'd", "isn't", "it's" in §1.2–1.5 and in info-boxes).
- Remove every em dash used as a connector in body prose, substituting per STYLE.md §3. Dashes stay in headings, figure labels ("Figure 1.1 — …"), info-box titles ("In plain terms — …"), status headers, figure-brief fields and reference lists; en-dash ranges (2023–24) stay.
- Check every paragraph opener in the chapter against v2.1 §2 (substantive claim; no hooks, questions or fragments) and every sentence for emphasis-only filler; revise or delete accordingly. Restyle any elaborate conversational constructions into plainer formal equivalents without losing content, citations or certainty flags.
- Update the status header voice field to `voice v2.1 (STYLE.md)`.
- Leave the existing `[ai-reviewer: …]` comment in §1.2 in place; it concerns evidence framing, not style, and is resolved separately under the R2 plan.

## Acceptance criteria (for ai-reviewer)

1. Zero `[human: …]` comments remain in ch01.
2. Zero contractions in ch01 outside verbatim quotations.
3. Zero em dashes in ch01 body prose (fixed formats and en-dash ranges exempt).
4. Every paragraph opener carries a substantive claim; no emphasis-only sentences anywhere in the chapter.
5. The count of `[AUTHOR: …]` and `[ai-reviewer: …]` markers is unchanged; no citation, figure brief or info-box content lost.
6. Status header reads `voice v2.1`; sentence-per-line preserved; STYLE.md §7 checklist passes in full.

## Follow-on (ai-editor's queue, not this pass)

Ch02–ch17 need the same v2.1 recalibration; scheduling awaits the author's confirmation of these rules on PR #4. R2 batches still in flight should write any new or revised prose to v2.1 from now on.
