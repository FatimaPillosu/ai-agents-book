# Author writing-style guide

**v2.0 · 23 July 2026** · Maintained alongside the book project; applies to all drafted prose unless a specific brief overrides it.

**Change from v1.1 (major):** the register moves from formal-academic to **personal and conversational while keeping full intellectual weight** (§1–§2). Two mechanisms are added: **info-boxes** that explain technical terms in plain language (§9), and a **sentence-per-line draft format** — unnumbered; precise line references come from the pull-request review view instead (§10). Integrity, evidence, British English and vendor-neutrality are unchanged.

## 1. Voice and stance

Write as the author speaking directly to an intelligent colleague from outside their specialism: warm, personal, first-person where it is natural, and unmistakably human — it should read as though the author wrote it at their desk, not as though a committee approved it. Confidence still comes from evidence and construction rather than emphasis, and the weight of the subject is never traded away for a lighter touch: the reader should feel that the stakes are real even as the prose stays approachable. Use "I" for the author's own judgement and experience, and "you" for the reader; let the occasional short sentence land for emphasis. What conversational does **not** mean here: no hype, no breeziness, no slang, no exclamation, no cliché, and no dumbing-down. A good test is that a hydrologist and a curious non-specialist should both finish a paragraph feeling they have understood something demanding, not that a demanding thing has been made trivial. Prefer specificity to generality and numbers to adjectives — "resolution rates rose from single figures in 2023 to above 70% by late 2025" rather than "performance improved dramatically".

## 2. Paragraph and sentence architecture

Open each paragraph with a sentence that makes its point clearly — a real claim the reader can hold onto — but that opening may now be conversational rather than a formal topic sentence, and it must never be an empty fragment or a rhetorical throat-clear. Paragraphs remain developed and substantial (a useful span is roughly 150–350 words), moving from claim towards context, evidence, implication and honest qualification, but the movement can breathe: vary sentence length, and let a short sentence do real work now and then. Depth still takes priority over coverage — develop fewer points properly rather than surveying many thinly. The change from earlier drafts is one of register and rhythm, not of rigour: the argument is still carried by developed prose, not by bullet lists.

**Worked contrast:**
- Too formal (old): "The developments that made agents possible form a short lineage in which the decisive changes concerned the interface to computation as much as raw capability."
- Too banal (avoid): "Agents came from a few big breakthroughs. Here's how."
- House voice (aim): "The path to agents is shorter than the hype suggests, and the turning points were mostly about how we talk to a computer rather than about raw horsepower."

## 3. Sentence and language conventions

British English throughout: -ise endings, British vocabulary and date conventions. Use precise technical language, but the first time a demanding term does real work, explain it — in the sentence itself or in an info-box (§9). Define a term once and hold to it. Signpost the argument in a human way ("I'll come back to this in Chapter 11"), not with bureaucratic scaffolding.

## 4. Evidence and uncertainty

Substantive claims carry certainty flags (high / moderate / low confidence), folded in naturally rather than stapled on — "I'm fairly sure (moderate confidence) that…" reads better than a bare parenthetical, though a parenthetical is fine. Uncertainty is quantified wherever the material allows, and where a claim is contestable, say what evidence would change your mind. Estimates are conservative; nothing is promised that the evidence cannot carry. When drawing on the literature, synthesise — compare and contrast positions — rather than listing sources.

## 5. Integrity

Never fabricate facts, quotes, sources or anecdotes. Where information is missing or unverified, say precisely what is needed and mark it:

- **[AUTHOR: …]** — lived material or a decision only the author can supply (personal anecdotes especially — they are what make the voice real).
- **[verify]** — a real but unconfirmed figure or bibliographic detail, to be checked before release.

Cite only references known to be real; incomplete bibliographic details are flagged, not invented.

## 6. Book-project conventions

Vendor-neutral in print: capability classes and approximate years in the text, with named products and volatile figures confined to the companion repository. Figures are described as briefs following `FIGURES.md` and rendered in the house infographic style, each carrying alt-text written when the brief is created. The argument is carried by paragraphs, not bullets; lists appear in prose ("x, y and z") unless the content is genuinely enumerable.

## 7. Pre-submission checklist

Before a draft is returned: (1) every paragraph opens with a clear, real claim (conversational is fine, fragments are not); (2) the voice is personal and human but the weight of the topic is intact — no banalisation; (3) every demanding term is explained in plain language or an info-box at first substantive use; (4) substantive claims carry certainty flags; (5) numbers replace adjectives wherever the evidence allows; (6) British spellings throughout; (7) all unverified material is marked and none invented; (8) the draft is sentence-per-line per §10, with no numeric prefixes.

## 8. Condensed prompt block

For agent-assisted drafting or review:

```
Write as the author speaking directly to an intelligent non-specialist colleague:
personal, conversational, first-person where natural ("I" / "you"), human — as if the
author wrote it — but carrying full intellectual weight. NOT breezy, NOT dumbed-down: no
hype, slang, exclamation or cliché; the reader should feel the stakes and finish having
understood something demanding. British English. Open each paragraph with a clear real
claim (conversational, never a fragment); developed paragraphs ~150–350 words, claim →
context → evidence → implication → limitation, varied sentence length. Numbers over
adjectives; certainty flags (high/moderate/low confidence) folded in naturally. Explain
every demanding term in plain language or an INFO-BOX at first substantive use, and add
the term to the glossary. Never fabricate: mark lived material [AUTHOR: …] and unverified
figures [verify]. Vendor-neutral. Write the prose one sentence per line, unnumbered, with a blank
line between paragraphs (see STYLE.md §10).
```

## 9. Info-boxes (plain-language term boxes)

Explain every demanding term the first time it does real work in a chapter, using an info-box placed immediately after the paragraph that introduces it. The box is a short blockquote in plain, warm language — no jargon inside the box explaining jargon — and it uses this fixed form:

```
> **In plain terms — Gate.** A checkpoint in a workflow where the agent's work has to
> pass a defined check before anything downstream is allowed to use it. Pass, and the
> work moves on; fail, and it loops back. Nothing proceeds just because it looks right.
```

Conventions: (a) box a term **once per chapter**, at first substantive use, not on every appearance; (b) every boxed term is also collected in `manuscript/GLOSSARY.md`, which is the single place a reader can look the word up anywhere; (c) keep boxes to two or three sentences; (d) box genuine jargon (gate, tool call, context window, token, orchestration, provenance, prompt injection, least privilege, in-context learning, ensemble, and the like), not ordinary words; (e) British English inside boxes too. Boxes keep their natural layout rather than sentence-per-line (§10).

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
