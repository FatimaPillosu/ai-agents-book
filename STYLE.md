# Author writing-style guide

**v2.1 · 25 July 2026** · Maintained alongside the book project; applies to all drafted prose unless a specific brief overrides it.

**Change from v2.0:** the register is recalibrated from "personal and conversational" to **plain, direct and formal**, on the author's inline instructions in ch01 §1.1 (25 Jul 2026). First person and direct address stay; rhetorical flourishes, scene-setting openers and emphasis-only short sentences go (§1–§2). Three mechanical rules are added and binding: **no contractions** in manuscript text (§3), **no em dashes as connectors** in body prose (§3), and **paragraph openers must carry a substantive claim** (§2). Info-boxes (§9) and sentence-per-line (§10) are unchanged. Note for the record: this narrows, and in part reverses, the deliberate v2.0 register shift; the recalibration follows the author's own comments, not editorial preference.

**Change from v1.1 (major):** the register moves from formal-academic to **personal and conversational while keeping full intellectual weight** (§1–§2). Two mechanisms are added: **info-boxes** that explain technical terms in plain language (§9), and a **sentence-per-line draft format** — unnumbered; precise line references come from the pull-request review view instead (§10). Integrity, evidence, British English and vendor-neutrality are unchanged.

## 1. Voice and stance

Write as the author addressing an intelligent colleague from outside their specialism, in language that is plain, direct and formal. First person is retained where it is natural: "I" for the author's own judgement and experience, "you" for the reader. Simplicity is the governing preference: choose the plainest formal phrasing that carries the content, and cut constructions that perform a voice rather than advance the argument, e.g. rhetorical inversions ("do not look at X; look at Y"), scene-setting hooks, and sentences added for rhythm or emphasis alone. Every sentence must earn its place by carrying information, a claim or a qualification. Confidence comes from evidence and construction, not emphasis: no hype, no breeziness, no slang, no exclamation, no cliché, and no dumbing-down. A good test is that a hydrologist and a curious non-specialist should both finish a paragraph feeling they have understood something demanding, not that a demanding thing has been made trivial. Prefer specificity to generality and numbers to adjectives: "resolution rates rose from single figures in 2023 to above 70% by late 2025" rather than "performance improved dramatically".

## 2. Paragraph and sentence architecture

Open each paragraph with a sentence that states a substantive claim the reader can hold onto. The opener may be in first person, but it must do argumentative or evidential work: no scene-setting hooks, no rhetorical questions, no fragments, no throat-clearing, no sensational framing. Paragraphs remain developed and substantial (a useful span is roughly 150–350 words), moving from claim towards context, evidence, implication and honest qualification. Vary sentence length as the content requires; a short sentence is acceptable only when it carries a complete substantive point on its own (e.g. "What has not grown is the number of hours in anyone's week"), never as rhythmic or emphatic filler. Depth still takes priority over coverage: develop fewer points properly rather than surveying many thinly. The argument is carried by developed prose, not by bullet lists.

**Worked contrast:**
- Too ornate (retired v1.1 formality): "The developments that made agents possible form a short lineage in which the decisive changes concerned the interface to computation as much as raw capability."
- Too performative (retired v2.0 flourish — avoid): "If you want to know what has really changed, do not look first at the models."
- Too banal (avoid): "Agents came from a few big breakthroughs. Here is how."
- House voice (aim): "The path to agents is shorter than the hype suggests, and the turning points were mostly about how we talk to a computer rather than about raw horsepower."

## 3. Sentence and language conventions

British English throughout: -ise endings, British vocabulary and date conventions. Use precise technical language, but the first time a demanding term does real work, explain it, in the sentence itself or in an info-box (§9). Define a term once and hold to it. Signpost the argument plainly ("I return to this in Chapter 11"), not with bureaucratic scaffolding.

Two mechanical rules, binding on all manuscript text (body prose, info-boxes, captions and alt-text alike); verbatim quotations are exempt:

- **No contractions.** Write "has not", "do not", "it is", "I would"; never "hasn't", "don't", "it's", "I'd".
- **No em dashes as connectors in body prose.** Do not use the em dash (—) to join clauses, append an afterthought or insert an aside. Substitute whichever is plainest of: a comma, a colon, parentheses, a new sentence, or an introducing phrase such as "e.g.", "i.e.", "such as", "that is" or "for example". The dash survives only in fixed formats: headings and labels ("Figure 1.1 — …", "In plain terms — Gate"), status headers, figure-brief fields and reference lists. En dashes in numeric and date ranges (2023–24, pp. 10–12) are unaffected.

## 4. Evidence and uncertainty

Substantive claims carry certainty flags (high / moderate / low confidence), folded in naturally rather than stapled on: "I am fairly sure (moderate confidence) that…" reads better than a bare parenthetical, though a parenthetical is fine. Uncertainty is quantified wherever the material allows, and where a claim is contestable, say what evidence would change your mind. Estimates are conservative; nothing is promised that the evidence cannot carry. When drawing on the literature, synthesise — compare and contrast positions — rather than listing sources.

## 5. Integrity

Never fabricate facts, quotes, sources or anecdotes. Where information is missing or unverified, say precisely what is needed and mark it:

- **[AUTHOR: …]** — lived material or a decision only the author can supply (personal anecdotes especially — they are what make the voice real).
- **[verify]** — a real but unconfirmed figure or bibliographic detail, to be checked before release.

Cite only references known to be real; incomplete bibliographic details are flagged, not invented.

## 6. Book-project conventions

Vendor-neutral in print: capability classes and approximate years in the text, with named products and volatile figures confined to the companion repository. Figures are described as briefs following `FIGURES.md` and rendered in the house infographic style, each carrying alt-text written when the brief is created. The argument is carried by paragraphs, not bullets; lists appear in prose ("x, y and z") unless the content is genuinely enumerable.

## 7. Pre-submission checklist

Before a draft is returned: (1) every paragraph opens with a substantive claim (no hooks, fragments, rhetorical questions or throat-clearing); (2) the register is plain, direct and formal, first person only where natural, and no sentence exists for rhythm or emphasis alone; (3) no contractions anywhere outside verbatim quotations; (4) no em dash used as a connector in body prose (fixed formats and en-dash ranges only); (5) every demanding term is explained in plain language or an info-box at first substantive use; (6) substantive claims carry certainty flags; (7) numbers replace adjectives wherever the evidence allows; (8) British spellings throughout; (9) all unverified material is marked and none invented; (10) the draft is sentence-per-line per §10, with no numeric prefixes.

## 8. Condensed prompt block

For agent-assisted drafting or review:

```
Write as the author addressing an intelligent non-specialist colleague in plain, direct,
formal language. First person where natural ("I" / "you"). No hype, slang, exclamation,
cliché or dumbing-down; the reader should finish having understood something demanding.
No contractions anywhere ("has not", never "hasn't"; quotations exempt). No em dash as a
connector in body prose: use a comma, colon, parentheses, a new sentence, or "e.g." /
"i.e." / "such as" / "that is"; dashes only in headings, labels and fixed formats;
en-dash ranges (2023–24) are fine. Open each paragraph with a substantive claim (no
scene-setting hooks, rhetorical questions or fragments); developed paragraphs ~150–350
words, claim → context → evidence → implication → limitation. Every sentence must carry
content; delete sentences that exist for rhythm or emphasis alone. British English.
Numbers over adjectives; certainty flags (high/moderate/low confidence) folded in
naturally. Explain every demanding term in plain language or an INFO-BOX at first
substantive use, and add the term to the glossary. Never fabricate: mark lived material
[AUTHOR: …] and unverified figures [verify]. Vendor-neutral. Write the prose one sentence
per line, unnumbered, with a blank line between paragraphs (see STYLE.md §10).
```

## 9. Info-boxes (plain-language term boxes)

Explain every demanding term the first time it does real work in a chapter, using an info-box placed immediately after the paragraph that introduces it. The box is a short blockquote in plain, warm language — no jargon inside the box explaining jargon — and it uses this fixed form:

```
> **In plain terms — Gate.** A checkpoint in a workflow where the agent's work has to
> pass a defined check before anything downstream is allowed to use it. Pass, and the
> work moves on; fail, and it loops back. Nothing proceeds just because it looks right.
```

Conventions: (a) box a term **once per chapter**, at first substantive use, not on every appearance; (b) every boxed term is also collected in `manuscript/GLOSSARY.md`, which is the single place a reader can look the word up anywhere; (c) keep boxes to two or three sentences; (d) box genuine jargon (gate, tool call, context window, token, orchestration, provenance, prompt injection, least privilege, in-context learning, ensemble, and the like), not ordinary words; (e) British English inside boxes too. Boxes keep their natural layout rather than sentence-per-line (§10).
<!-- [ai-reviewer: convention (a) is ambiguous and the manuscript has settled a different practice than its literal reading. "Once per chapter" can be read as requiring every chapter to box a term at its own first use; the practice adopted in R1 (per REVISION-PLAN §3/G3, endorsed on review) is to place the definitive box in the term's canonical-home chapter only, with later chapters relying on the glossary — e.g. ch15–ch17 use gate, roster and least privilege without re-boxing. ai-editor should reword (a) to state the canonical-home rule explicitly so a future writer does not "fix" the later chapters by adding duplicate boxes.] -->

## 10. Draft sentence-per-line format (unnumbered)

Write body prose one sentence per line, with a blank line between paragraphs and no numeric prefixes. Line references for review come from the repository platform, not the source: the manuscript is reviewed through pull requests, whose file view numbers every line, so a comment anchors to an exact sentence without any numbering carried in the text. Paragraphs stay independent simply by being separated by blank lines:

```
### 1.1 Section heading

First sentence of the paragraph sits on its own line.
The second sentence follows on the next line.
And so on to the end of the paragraph.

The next paragraph begins after a blank line.
Its sentences continue one per line.
```

What is sentence-per-line: body prose paragraphs only. What keeps its natural layout: headings, info-boxes, figure-brief blocks, block quotations, lists, captions, tables and the references section. A very long compound sentence may stay whole on its line rather than being split artificially. Markdown joins consecutive lines into a single paragraph in rendered output, so the convention is invisible to readers; it exists for drafting and review in the source, and whether any later built output needs re-flowing is a separate, deferred decision. (Earlier drafts carried explicit per-paragraph line numbers; that scheme is retired — do not add numeric prefixes.)
