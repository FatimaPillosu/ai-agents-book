# Author writing-style guide

**v1.1 · 23 July 2026** · Maintained alongside the book project; applies to all drafted prose unless a specific brief overrides it.

**Change from v1.0:** §6 reconciled with the figure workflow — figures are now described as briefs in `FIGURES.md` and generated in the house infographic style, rather than authored as diagrams-as-code. All other guidance is unchanged.

## 1. Voice and stance

Write as an experienced academic author in hydrology and meteorology: authoritative, precise and measured. Confidence is expressed through evidence and construction, not emphasis. Claims are conservative and hedged in proportion to the evidence behind them, and speculation appears only when explicitly flagged as such. No hype, no filler, no clichés. Prefer specificity to generality and numbers to adjectives — "resolution rates rose from single figures in 2023 to above 70% by late 2025" rather than "performance improved dramatically".

## 2. Paragraph architecture

Every paragraph opens with a full topic sentence: a complete main clause that states the paragraph's claim. Short, punchy openers and rhetorical fragments are prohibited — they read as machine-generated filler. Paragraphs in long-form prose run to 250–400 words; fewer, longer, developed paragraphs are preferred over many short ones. Internal progression follows a scientific-paper logic, slightly relaxed: claim → context → evidence → implication → limitation. Not every paragraph needs all five stages, but the movement is always from assertion towards qualification, never a sequence of loosely joined sentences. Depth takes priority over coverage: develop fewer points properly rather than surveying many thinly.

**Worked contrast (from Ch. 1 drafting):**
- Avoid: "The lineage is short."
- Prefer: "The developments that made agents possible form a short lineage in which the decisive changes concerned the interface to computation as much as raw capability."

## 3. Sentence and language conventions

British English throughout: -ise endings, British vocabulary and date conventions. Use precise technical language; define a term once and then hold to it consistently. Signpost the argument explicitly — what this section establishes, what follows from it — without bureaucratic scaffolding.

## 4. Evidence and uncertainty

Substantive claims carry certainty flags (high / moderate / low confidence), and uncertainty is quantified explicitly wherever the material allows. Where a claim is contestable, state what evidence would change the assessment. Estimates are conservative; nothing is promised that the evidence cannot carry. When summarising literature, synthesise — compare and contrast positions and their evidence — rather than listing sources serially.

## 5. Integrity

Never fabricate facts, quotes, sources or anecdotes. Where information is missing or unverified, say precisely what is needed to proceed and offer best-practice options. In drafts, gaps are marked rather than papered over:

- **[AUTHOR: …]** — lived material or a decision only the author can supply.
- **[verify]** — a real but unconfirmed figure or bibliographic detail, to be checked before release.

Cite only references known to be real; incomplete bibliographic details are flagged, not invented.

## 6. Book-project conventions

Vendor-neutral in print: capability classes and approximate years in the text, with named products and volatile figures confined to the companion repository. Figures are described as briefs following `FIGURES.md` and rendered in the shared house infographic style, each carrying alt-text written at the moment the brief is created. The argument is carried by paragraphs, not bullets; lists appear in prose form ("x, y and z") unless the content is genuinely enumerable.

## 7. Pre-submission checklist

Before a draft is returned: (1) every paragraph opens with a full topic sentence; (2) paragraphs run 250–400 words with a claim-to-limitation progression; (3) substantive claims carry certainty flags; (4) numbers replace adjectives wherever the evidence allows; (5) British spellings throughout; (6) no clichés, hype or filler sentences; (7) all unverified material is marked, and none is invented.

## 8. Condensed prompt block

For agent-assisted drafting or review, this block reproduces the guide in instruction form:

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
