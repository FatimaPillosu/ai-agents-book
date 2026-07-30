# Author writing-style guide

**v5.0 · 26 July 2026** · Binding for all drafted prose unless a specific brief overrides it.

**Change from v4.0-colloquial (consolidation, no new rules):** the colloquial register is now the guide's own register rather than an overlay on top of an academic one. The branch note and the §0 override block are removed, and their content is folded into the sections it governed: §1 (voice), §2 (paragraphs), §3 (openers) and §11 (contractions) are rewritten to state the register directly. Nothing binding has changed; a drafter can now read §1 to §12 in order without holding two registers in mind. The academic register the book used until 26 July 2026 is preserved in this file's git history at v3.4, and the manuscript written in it remains on branch `claude/manuscript-feedback-e2xcop`.

**Change from v3.4 (major):** the whole book moved to the colloquial register piloted in Chapter 4, on the author's instruction of 26 July 2026. All eighteen files (ch00–ch17) were converted. What changed: the reader is addressed as "you", contractions are permitted, paragraphs shortened to 80–200 words, openers loosened, and every sentence that announced what the text was about to do was cut. What did not change: the sentence-length ceiling, the metaphor prohibition, the §12.1 deletions, integrity markers, citation policy, info-boxes, sentence-per-line drafting, British English and vendor-neutrality.

**Change from v3.3 (major):** three author instructions, taken from the author's own revision of §4.1 of Chapter 4, are added. First, a **sentence-length ceiling** replaces the previous preference for long qualification-bearing sentences: about 25 words is the target and roughly 30 the ceiling, beyond which a sentence is split into two (§11). Second, **metaphor is prohibited outright** in manuscript prose: no figurative substitution for a mechanism that can be stated literally (§12.2). Third, §12.1 records verbatim the constructions the author deleted from the first draft of §4.1, each with the accepted replacement, so the same habits can be removed from every other chapter. §7 and §8 are amended accordingly. The first two are deliberate house deviations from the thesis, whose sentences run longer and which permits occasional figurative language.

**Change from v3.2 (minor):** the **no-em-dash-connector** rule from the v2.1 lineage is reinstated on the author's instruction: em dashes never join clauses or carry appositives and asides in manuscript text (§11); substitute a comma, colon, parentheses, a new sentence, or an introducing phrase. The dash survives only in fixed formats (headings and labels such as "Figure 1.1 — …" and "Definition — Gate"); en-dash ranges are unaffected. This is a deliberate house deviation from the thesis, which uses paired dashes for appositives; quoted thesis examples in this guide retain their original punctuation. §4 and §11 are amended accordingly.

**Change from v3.1 (minor):** the **no-contractions** rule from the v2.1 lineage is reinstated on the author's instruction (§11): manuscript text never contracts ("has not", never "hasn't"); verbatim quotations are exempt. The manuscript remains impersonal (no "you"), per §1.

**Change from v3.0 (minor):** the margin-note drafting mechanism is removed — the book will not use margin notes. The one-claim-per-paragraph discipline it enforced is retained in §2.

**Change from v2.0 (major):** the conversational-personal register introduced in v2.0 is withdrawn on the author's instruction. The register returns to the author's own academic voice, now specified in far greater detail by direct extraction from the author's PhD thesis (chapters 1–9, on medium-range prediction of areas at risk of flash floods). Every quoted example in this guide is taken verbatim from that thesis (lightly cleaned of LaTeX markup); where the abstraction and the example seem to disagree, imitate the example. The register-independent mechanisms of v2.0 are retained unchanged: integrity markers (§6.5), info-boxes and the glossary (§9), the sentence-per-line draft format (§10), British English and vendor-neutrality.

## 1. Voice and stance

Write to one intelligent colleague from outside your specialism, at a bench or over coffee. Never to an audience from a lectern. The reader is "you". The author is "I" wherever a judgement or an experience is genuinely the author's own, and the first person is not otherwise scattered about; "this chapter", "this book" and the passive all remain available where they are the natural thing to write, but they are no longer the default and they must never be used to duck ownership of a claim. Contractions are allowed and used lightly: "does not" and "doesn't" both appear, and the choice is made by ear rather than by rule.

The lighter register never buys a lighter treatment of the material. No hype, no jokes, no slang, no exclamation, no cliché, and nothing dumbed down. The test is that a hydrologist and a curious non-specialist should both finish a paragraph having understood something demanding, not feeling that a demanding thing was made trivial. Authority comes from evidence and construction, not from emphasis, exactly as it did in the academic register.

**Never announce what the text is about to do.** This is the single habit that most separates this register from the one the book used before, and it is the first thing to cut on any pass. "The limitation of the procedure is that both properties are estimated in advance" becomes "The catch is that both of those questions are answered before the work starts". Delete every "The qualification worth stating is that…", "This has a concrete organisational consequence…", "The discipline that guards against the error is to notice that…". State the thing; the reader can see what kind of thing it is without being told.

**Let the concrete case lead.** Where a passage has both an abstraction and an example, the example goes first and the abstraction follows as the lesson drawn from it. A named event, a real file, an actual afternoon of work beats a category every time.

Stakes are established with numbers and named events, never with adjectives, and this rule is unchanged from every previous version of this guide. Show the severity of a topic; do not assert it. The thesis this book's earlier register was extracted from opens its whole argument that way: "Flash floods represent the deadliest and most devastating hazards, causing over 5,000 fatalities annually and accounting for ~85% of global flood incidents", then grounds it: "In October 2024, flash floods in Valencia, Spain, claimed more than 200 lives and caused extensive damage in 87 municipalities". Those quotations are cited here for their evidential construction, not their register; write the same content in the voice of this section. The largest claims stay the most carefully hedged.

## 2. The paragraph is the unit of argument

A paragraph runs roughly **80–200 words** and carries exactly one point. It is short enough to be taken in at a glance and long enough to develop something, and a paragraph break is allowed to do rhetorical work rather than only marking a change of subject. Where the material genuinely needs it, the movement **claim → context → evidence → qualification → implication** still applies, but it may now run across two or three short paragraphs instead of being compressed into one long one, and not every paragraph needs every element.

What survives from the long-paragraph discipline is the part that mattered: evidence is cited and quantified, qualifications are explicit rather than implied, and a passage that raises a concession resolves it. The closing-on-consequence habit is kept where it is natural and dropped where it would be ceremonial:

> "Therefore, developing robust medium-range flash flood forecasting capabilities on a global scale remains one of the pressing challenges in modern hydrology."

> "Consequently, despite the potential of global NWP rainfall forecasts to extend flash flood prediction beyond data-rich regions, their suitability for this purpose remains largely unverified at the scales required for global application."

Depth still takes priority over coverage: develop fewer points properly rather than surveying many thinly. A paragraph never trails off on a detail.

The one-claim discipline is unchanged, and it is the reason the shorter paragraph is not a licence to ramble. A paragraph carries exactly one claim, and that claim must be summarisable as a single compressed nominal phrase ("Barrier n.1: limited direct assessment of global NWP rainfall forecasts against flash flood occurrence"; "CONUS as the primary study domain: justification"). If no single phrase covers the paragraph, it contains two claims and must be split; if the phrase is vague ("some thoughts on verification"), the paragraph has no claim yet. Read in sequence, the one-phrase summaries of a section's paragraphs must reproduce its argument — that is the test of a well-built section. The summaries themselves are a drafting check only and are never carried in the manuscript.

## 3. Opening the paragraph

Every paragraph opens with a real sentence carrying real content. Beyond that the register is permissive: an opener may be a topic sentence, a short declarative, a question, or the concrete case itself, and the choice is made by what the paragraph is doing rather than by a pattern list.

The four patterns below came from the author's thesis and remain the most reliable openers for an argumentative paragraph, so they are kept as a repertoire to reach for rather than a rule to satisfy. Read them for structure; the register of the quoted examples is the pre-2026 academic one and should not be imitated.

**(a) Subject-first declarative.** The paragraph's subject leads the sentence and the claim about it follows immediately, often already quantified:

> "Flash floods are characterised by a rapid hydrological response to intense rainfall events, with runoff timescales ranging from mere minutes to a few hours."

> "ERA5 represents the fifth-generation atmospheric reanalysis produced by the European Centre for Medium-Range Weather Forecasts (ECMWF)."

> "Catchment characteristics (e.g. morphology, topography, land use, and soil properties) play a crucial role in determining the hydrological response of the catchment to heavy rainfall."

**(b) Concessive opening.** A concession is granted in a subordinate clause, and the main clause asserts the claim against it. This is the signature move of the thesis and should appear often — it lets a paragraph acknowledge the state of the art and stake its position in one breath:

> "Despite general advances in flash flood prediction (for example, the development of high-resolution physical and data-driven NWP and hydrological models), significant technical and methodological obstacles persist for the development of medium-range flash flood forecasts."

> "Notwithstanding the acknowledged limitations in the flash flood event reporting in the Storm Event Database, this dataset demonstrates substantial utility for model development and evaluation compared to global datasets."

> "Although the proof-of-concept presented in this thesis focuses on the CONUS, the underlying methodology is explicitly designed to support global scalability."

The inverted form is also in the repertoire: "Low resolution notwithstanding, the interest in using rainfall forecasts from these ensemble global NWP models has been growing."

**(c) Tension or convergence framing.** The opening sentence names a structural situation — a trade-off, a tension, a convergence — that the paragraph then unpacks:

> "The unprecedented convergence of three key scientific advancements over the last decade has created a unique opportunity to develop medium-range flash flood forecasts with global coverage."

> "The development of such transferable models faces a critical trade-off between spatial coverage and data density."

> "The lack of high-density global flash flood impact databases creates a fundamental tension between two contrasting approaches."

**(d) Continuation pivot.** The opening sentence stands on what has already been established and turns it toward the new claim — the connective tissue of a chapter:

> "Chapters 1 and 2 of this thesis have established that extending flash flood predictions to medium-range lead times over large spatial domains remains an unresolved challenge in modern hydrology. Yet recent scientific advances suggest a viable path forward."

> "As shown in the previous paragraph, despite their promise, most data-driven flash flood prediction studies rely on high-resolution inputs."

Rhetorical questions are freer in this register than in the academic one, but they are still rationed: roughly one or two per section, answered immediately, and never used to avoid stating the claim. Chapter 4's "So the question is practical: which parts of the research cycle may be handed to one, and which may not?" is the house use. The thesis examples below show the same move in the older register — "Can data-driven approaches for flash flood prediction work with such a small training dataset?"; "This finding raised a compelling question: if diversity within a region enables generalisation, could combining observations from multiple regions extend this capability across continents or even globally?"

What never opens a paragraph: a fragment ("Agents. Everywhere."), a bare connective with no content ("So, here's the thing."), a cliffhanger ("Then everything changed."), or a definition of a term the reader has not yet been given a reason to care about.

## 4. Developing and closing the paragraph

**Enumerate inside the prose, not in bullets.** When a paragraph carries several parallel items, announce the count and walk them with "First, … Second, … Third, …", keeping the grammar parallel:

> "This framework must overcome two main methodological challenges: addressing spatio-temporal uncertainties in flash flood reports, and establishing meaningful performance measures that account for the inherent rarity of flash flood events."

> "The construction proceeds in three steps. First, … Second, … Third, these counts populate a 2×2 contingency table for that threshold."

Announced counts are commitments: if the sentence says three advancements, exactly three follow, each given comparable weight.

**Concede and resolve.** A "However" mid-paragraph is never the end of the story; the paragraph resolves the concession into a position. The rhythm claim → concession → resolution can run more than once in a long paragraph, but each concession is answered:

> "However, this approach offers only a partial solution. Ensemble forecast spread can still be large, even at short-range lead times, and important small-scale flash flood-triggering rainfall events may still be missed."

**Elaborate with the colon and the parenthesis.** A colon introduces the specific content of an abstraction just named ("faces a fundamental obstacle: severe class imbalance between flash flood and non-flood events"). Appositive definitions and asides are carried by commas or parentheses, never by em dashes (§11). Parentheses hold compact specifics: resolutions, date ranges, "(e.g., …)", "(i.e., …)".

**Close with consequence.** The final sentence of a paragraph states an implication, a limitation, or the necessity it has established:

> "Hence, investigating whether impact reports can successfully be used as target variables in data-driven approaches represents a necessary step toward extending flash flood forecasting beyond data-rich regions and short-range timescales."

## 5. Chapter architecture, signposting and set pieces

### 5.1 Roadmap paragraphs

A chapter opens by earning its existence (problem and stakes, quantified), then gives the reader a map. The map is explicit and unembarrassed about being scaffolding:

> "This chapter reviews the scientific foundations underpinning the development of medium-range predictions… The chapter is organised around three interconnected themes. Section 2.1 explores… Section 2.2 reviews… Section 2.3 explores… Each section moves from established achievements through current challenges to opportunities, thereby clarifying the rationale for the analyses presented in the main chapters."

Note the last sentence: the roadmap does not merely list sections, it states the *logic* that orders them. Analysis chapters close their introduction with "The remainder of this chapter is organised as follows. Section … presents …", with a clause on what each section delivers.

### 5.2 The achievements → barriers → opportunities arc

The thesis's recurring argumentative engine, and the book's core-chapter anatomy (problem → conventional workflow → agentic redesign → worked example → failure modes → verification checklist) is the same arc under other names. For each theme: first what has genuinely been achieved (with credit given and evidence cited), then the barrier that remains (stated as a barrier, not a complaint), then the opportunity that the coming material exploits. Label the moves when the material is dense — the thesis literally numbers them ("Barrier n.1", "Opportunity n.2") — and keep symmetry between them: every barrier raised is either resolved or explicitly carried forward.

### 5.3 Numbered requirements and explicit contributions

Design decisions are presented as numbered requirements, each with its own justification paragraph ("Requirement for observational data n.1: need to represent both types of flash floods…"), closing with a short paragraph naming what was chosen and pointing to where it is described in full. Contributions are stated outright, enumerated, and kept honest by their own limitations:

> "Addressing RQ1 delivers two fundamental contributions to knowledge. First, it establishes a performance baseline by evaluating state-of-the-art global NWP rainfall forecasts against flash flood impact reports… Second, the framework itself constitutes a contribution — a standardised assessment tool applicable to any flash flood prediction."

Sections that hand over to later material end with a one-line pointer: "The research developed on this topic is presented in Chapter 5." For the book: "This pattern is developed in Chapter 9" / "The runnable configuration is under `/patterns/…`."

### 5.4 Narrating results and worked examples

Results prose is figure-anchored and follows a fixed micro-pattern: **quantified observation (with figure/panel reference) → interpretation → implication or limitation.** The observation states what the figure shows, with numbers; the interpretation begins "This indicates that…", "This steep rise suggests…", "This behaviour reflects…"; the implication says what it means for practice:

> "All forecasts for rainfall events exceeding the 1-year return period exhibit a systematic overprediction across all lead times, as shown by the reliability diagram being below the diagonal line. This indicates that when the model predicts a given probability, the observed frequency of flash flood events is consistently lower. For example, when the forecasts indicate a 50% chance of having a flash flood event, the observed frequency ranges from ~10% in the short-range forecasts…"

Worked examples (case studies) follow the same discipline at larger scale: first the event itself, factually and quantitatively ("624.1 mm/24h were recorded in the province's capital… 8,150,000 people were evacuated… 398 people died"), then what the method produced for that event, then the interpretive sentence that says why the difference matters ("the model's primary contribution does not lie in the absolute magnitude of probabilities but in their relative spatial distribution — specifically, its ability to propagate the flash flood risk signal downstream").

### 5.5 Discussions and conclusions

Each discussion paragraph takes one theme: finding restated → interpretation → placement against the literature ("This finding aligns with evidence presented in Kratzert et al. (2024)…" / "This result appears to be in striking contrast with the current literature…") → operational or practical implication. Conclusions restate contributions in enumerated form ("The research presented in this thesis makes three fundamental contributions… First, … Second, … Third, and most significantly…"), acknowledge limitations plainly and without self-flagellation ("These constraints, whilst significant, do not negate the fundamental advance this research represents"), enumerate future directions ("Future research should pursue four strategic directions…"), and end by reconnecting to the stakes established at the start.

### 5.6 Cross-references

Cross-referencing is dense and always informative: a reference names what will be found at the destination, not just the destination ("For a detailed description of the synoptic conditions during Storm Ida and its impacts, please refer to Section 4.6"). Backward references compress rather than repeat: one clause of reminder, then the pointer. In this register, explicit scaffolding is correct and expected — do not disguise it.

## 6. Evidence, quantification and uncertainty

### 6.1 Numbers over adjectives

Wherever the material allows, the quantity replaces the qualifier, and comparisons are anchored to a baseline: "false alarm rates exceeding 50%, representing a twenty-fold increase compared to balanced configurations"; "flash flood events comprising merely 0.27% of all cases"; "requiring approximately 40 times longer training time"; "training times in the order of minutes; neural network training took hours, yet the resulting predictions were no better". A modest number is defended by context rather than inflated: "Whilst these values appear modest, they represent meaningful skill when put into the context of the climatological frequency of flash floods in the observational dataset, i.e., 0.27%."

### 6.2 Literature is synthesised, not listed

Sources are set against one another and the synthesis carries the argument: "Schwartz (2019a,b) show that increasing the number of members computed at lower spatial resolutions can help increase the forecasts' lead time… However, this approach offers only a partial solution. Ensemble forecast spread can still be large (Done, 2012), and important small-scale events may still be missed (Gober, 2008)." A survey statistic may summarise a field ("LSTM networks dominate, appearing in 60% of the reviewed studies"), but a bare list of citations with no relation drawn between them is not synthesis. Where a body of work is invoked, say what it collectively establishes and where it stops.

### 6.3 Calibrated hedging

The hedging vocabulary is precise and graded: *may*, *might*, *can*, *is likely to*, *suggests*, *indicates*, *appears to*, *remains largely untested*, *it is foreseen / anticipated / envisioned that*. Hedge the claim once, at the right strength, in the right clause — not every clause defensively. Strong verbs are used when the evidence carries them: *demonstrates*, *establishes*, *reveals*, *confirms*, *underscores*. The certainty flags convention (high / moderate / low confidence) remains in force for the book's substantive claims, folded into the sentence or carried as a compact parenthetical.

### 6.4 Dual interpretations and counterintuitive results

When evidence admits more than one reading, both readings are given comparable development and the undecidability is stated rather than smoothed over:

> "These results may have two interpretations. The first one concerns the quality of the forecasts… The second interpretation concerns the type of flash flood events recorded in the database… It is not possible to disentangle from the information at hand which of the two interpretations might be the correct one."

Counterintuitive or unwelcome results are confronted head-on: state the anomaly, propose a candidate mechanism, and name the further work that would settle it — "This odd correlation might be due to the fact that, climatologically, LAI values are greater over the summer… More investigation is, therefore, needed to confirm this explanation." Never bury an anomaly, and never let it stand unexamined.

### 6.5 Integrity markers

Never fabricate facts, quotes, statistics, sources or anecdotes. Where information is missing or unverified, mark it:

- **[AUTHOR: …]** — lived material or a decision only the author can supply.
- **[verify]** — a real but unconfirmed figure or bibliographic detail, to be checked before release.

Cite only references known to be real; incomplete bibliographic details are flagged, not invented.

## 7. Pre-submission checklist

Before a draft is returned: (1) every paragraph opens with a real sentence carrying real content — no fragments, no throat-clearing, and no sentence announcing what the text is about to do (§1, §3); (2) every paragraph carries exactly one point, summarisable as a single nominal phrase, and the section's paragraph summaries read as its argument (§2); (3) paragraphs run roughly 80–200 words, and where a passage develops claim → context → evidence → qualification → implication it may do so across several short paragraphs (§2); (4) every "However" is resolved; every announced enumeration is completed with parallel grammar; (5) numbers replace adjectives wherever the evidence allows, and comparisons carry baselines; (6) claims are hedged once, precisely, with certainty flags on substantive claims; anomalies are confronted, not buried; (7) literature and prior art are synthesised, not listed; (8) roadmap, pointer sentences and cross-references are in place and each names what the destination contains; (9) the reader is addressed as "you" where the sentence calls for it, and there is no hype, no exclamation and no bullet-point argumentation in main prose (§1); (10) British English throughout; contractions used lightly and by ear (§11); no em dash used as a connector (fixed formats and en-dash ranges only, §11); every demanding term defined once at first substantive use (info-box where warranted, §9); (11) all unverified material is marked [AUTHOR:]/[verify] and none invented; (12) the draft is sentence-per-line per §10; (13) no sentence exceeds roughly 30 words, and none that exceeds 25 could be split to advantage (§11); (14) no metaphors anywhere, including captions and alt-text (§12.2), and none of the deleted constructions of §12.1 has reappeared.

## 8. Condensed prompt block

For agent-assisted drafting or review:

```
Write to one intelligent colleague from outside your specialism: address them as "you",
use "I" where the judgement or experience is genuinely the author's own, and never write
at an audience from a lectern. British English. Contractions allowed and used lightly
("does not" and "doesn't" both fine; choose by ear). NOT breezy and NOT dumbed down: no
hype, jokes, slang, exclamation or cliche; the reader should finish having understood
something demanding.

NEVER ANNOUNCE WHAT THE TEXT IS ABOUT TO DO. "The limitation of the procedure is that
both properties are estimated in advance" becomes "The catch is that both of those
questions are answered before the work starts". Cut every "The qualification worth
stating is that...", "This has a concrete organisational consequence...". State the
thing. LET THE CONCRETE CASE LEAD: where a passage has an abstraction and an example,
the example goes first and the abstraction follows as the lesson drawn from it.

Paragraphs roughly 80-200 words, one point each; a paragraph break may do rhetorical
work. Open each on a real sentence carrying real content: topic sentence, short
declarative, question, or the concrete case; never a fragment, throat-clear or
cliffhanger. Sentences ~25 words, 30 maximum: split anything longer into two without
dropping content.

NO METAPHORS at all, in prose, captions or alt-text: state the mechanism literally.
Defined technical terms (gate, loop, pipeline) and declared analogies under examination
are not metaphors (SS12.2). No apologetic preambles ("described plainly enough to be
useful here..."), no unbaselined comparatives ("far more X than any Y suggests"), no
gravitas by abstraction ("carries the scientist's name and standing") - see SS12.1.

No em dash as a connector: use a comma, colon, parentheses, a new sentence, or "e.g." /
"i.e." / "such as" / "that is"; dashes only in fixed labels ("Figure 1.1 - ...",
"Definition -"); en-dash ranges (2023-24) are fine. Enumerate in prose with parallel
grammar; concede and resolve (every "However" is answered). Numbers over adjectives with
baselines ("a twenty-fold increase"); synthesise literature, never list. Hedge once,
precisely; certainty flags (high/moderate/low confidence) on substantive claims; give
rival interpretations comparable weight; confront counterintuitive results with candidate
mechanisms. Pointer sentences name what the destination contains. Results prose:
quantified observation (figure-anchored) -> "This indicates that..." -> implication.
Stakes shown with numbers and named events, never adjectives.

Never fabricate: mark lived material [AUTHOR: ...] and unverified figures [verify];
citations only from the verified reports in /research. Vendor-neutral. One sentence per
line, unnumbered (STYLE.md SS10).
```

## 9. Definitions, info-boxes and the glossary

Terminology is disciplined: a term is defined once, precisely, at its first substantive use, and held constant thereafter — the thesis defines "flash flood", "areas at risk of flash floods" and "feasible" in set-off boxes or footnotes and never varies them. Coined or load-bearing terms are italicised at first use ("*flash-flood-focused verification framework*", "*verifying rainfall threshold*") and used unitalicised afterwards. The book's equivalent of the thesis's definition boxes is the info-box, placed immediately after the paragraph that introduces the term:

```
> **Definition — Gate.** A checkpoint in a workflow where the agent's work must pass a
> defined check before anything downstream may use it. Work that passes proceeds; work
> that fails returns for revision.
```

Conventions: (a) box a term **once per chapter**, at first substantive use; (b) every boxed term is also collected in `manuscript/GLOSSARY.md`; (c) keep boxes to two or three sentences, in the same register as the main prose; (d) box genuine jargon, not ordinary words; (e) short technical asides that would be footnotes in the thesis become either a parenthetical or an info-box — the book has no footnote apparatus. Boxes keep their natural layout rather than sentence-per-line (§10).

## 10. Draft sentence-per-line format (unnumbered)

Write body prose one sentence per line, with a blank line between paragraphs and no numeric prefixes. Line references for review come from the repository platform: the manuscript is reviewed through pull requests, whose file view numbers every line, so a comment anchors to an exact sentence without any numbering carried in the text.

```
### 1.1 Section heading

First sentence of the paragraph sits on its own line.
The second sentence follows on the next line.

The next paragraph begins after a blank line.
```

Sentence-per-line applies to body prose paragraphs only. Headings, info-boxes, figure-brief blocks, block quotations, lists, captions, tables and references keep their natural layout. A very long compound sentence may stay whole on its line. Markdown joins consecutive lines into a single paragraph in rendered output, so the convention is invisible to readers.

## 11. Sentence craft: rhythm, connectives, punctuation, British English

**Rhythm and sentence length.** Every sentence must be readable once, without a second pass to recover its structure. About 25 words is the working target and roughly 30 words is the ceiling: a sentence running beyond it is split into two, even where the grammar is sound and the qualification is genuine. Splitting is not compression, and no content is dropped in the process; the second sentence carries what the subordinate clause used to carry, usually introduced by a colon in the first sentence, or by "What remains is…", "The consequence is…", "The limitation is…". Where a genuinely enumerative sentence exceeds the ceiling because it lists parallel items separated by semicolons, it may stand whole; a sentence that exceeds it because it has accumulated relative clauses may not.

> Too long (33 words): "Agents are instruments that serve the scientist's judgement rather than substitutes for it, and the practical question that follows is which parts of the research cycle such an instrument may legitimately be given."

> House form (two sentences): "Agents are instruments that serve the scientist's judgement rather than substitutes for it. What remains is the practical question: which parts of the research cycle may be handed to such an instrument, and which may not."

A short declarative (4–10 words) is still deployed deliberately, roughly once per paragraph, to land a turn: "However, significant challenges persist." "Recent developments confirm this issue." "This precedent suggests a way forward." The short sentence is an instrument of emphasis, not a default, and it is still a sentence, never a fragment. Note that the ceiling is a deliberate deviation from the thesis, whose sentences frequently run to 45 words; where this guide and a quoted thesis example disagree on length, the ceiling wins.

**Connective vocabulary** (the working set, in the frequencies the thesis uses them):

- *Contrast/concession:* However · Nonetheless · Nevertheless · Notwithstanding (also postposed: "Low resolution notwithstanding, …") · In contrast · Conversely · Whilst · Although · Despite · Yet
- *Consequence:* Hence · Therefore · Consequently · Thus
- *Addition:* Moreover · Furthermore · Additionally
- *Precision/meta:* Specifically · In particular · Notably · To clarify · In this regard · It is worth noting that · For the sake of brevity and clarity

Do not open more than two consecutive paragraphs with the same connective, and never stack two contrast connectives in one sentence.

**Punctuation.** Colon to introduce the content of an abstraction just named; semicolons to hold parallel items of an in-sentence list; parentheses for compact specifics ("(e.g., …)", "(i.e., …)", resolutions, periods, versions) and for appositive definitions and asides. Lists inside prose keep parallel grammar throughout.

**No em dashes as connectors.** The em dash never joins clauses, appends an afterthought or carries an aside in manuscript text (body prose, info-boxes, captions and alt-text alike). Substitute whichever is plainest of: a comma, a colon, parentheses, a new sentence, or an introducing phrase such as "e.g.", "i.e.", "such as" or "that is". The dash survives only in fixed formats: headings and labels ("Figure 1.1 — …", "Definition — Gate"), status headers, figure-brief fields and reference lists. En dashes in numeric and date ranges (2023–24, pp. 10–12) are unaffected. This is a deliberate house deviation from the thesis, which uses paired dashes for appositives; quoted thesis examples in this guide retain them, and [AUTHOR: …] markers are working notes outside the rule's scope.

**British English throughout**, including captions, alt-text and repository docs: -ise endings, *whilst*, *amongst*, *behaviour*, *modelling*, *parametrisation*, *centre*; dates as "23 August 2021". Units and quantities are precise and SI; percentages, return periods, resolutions and lead times always take figures ("~31 km", "0.27%", "up to day 5").

**Contractions are allowed, and used lightly.** "Does not" and "doesn't" both belong in this register, and the choice between them is made by ear: contract where the sentence is conversational and the contraction reads naturally, spell it out where the sentence is carrying weight or where the uncontracted form is simply clearer. Do not contract mechanically, and do not sweep a chapter converting one to the other. The rule applies equally to body prose, info-boxes, captions and alt-text. (This reverses the no-contractions rule that stood from v2.1 to v4.0; the academic register it belonged to was withdrawn on 26 July 2026.)

## 12. Anti-patterns

Never: punchy fragment openers or one-sentence paragraphs; addressing the reader as "you"; exclamation marks; hype vocabulary ("game-changing", "revolutionary", "the hype suggests"); jokes, irony or self-deprecation; bullet lists carrying the argument of body prose (bullets are for genuinely enumerable reference material only); adjectives where a number exists; bare citation lists in place of synthesis; unresolved "However"s; announced enumerations left incomplete; claims without hedges or hedges without claims (mush like "it could perhaps be argued that X might possibly…"); burying a counterintuitive result; metaphor of any kind (§12.2); scaffolding that points nowhere ("more on this later") — a pointer always names its destination and what will be found there.

<!-- [ai-reviewer: defect in a binding guide, confirmed on the A1 pass and reported independently by a drafting agent. "Addressing the reader as 'you'" is listed here as a thing never to do, and it flatly contradicts §1 ("The reader is 'you'"), §7 checklist item 9 ("the reader is addressed as 'you' where the sentence calls for it") and the §8 prompt block ("address them as 'you'"). It is a survival from the pre-26-July academic register that the v5.0 consolidation did not sweep. An agent reading §1 to §12 in order, which §0's change-note says it should be able to do, meets the rule and its negation. This needs ai-editor to delete or rewrite the clause; nothing in the manuscript should be revised against it in the meantime. Two lesser items in the same list also want a ruling while the section is open: "one-sentence paragraphs" sits in tension with §2's licence for a paragraph break to do rhetorical work, and the list does not say whether it binds captions, alt-text and figure-brief fields as §12.1 and §12.2 explicitly do. This pass found no manuscript prose that breaches the "you" clause as written, because every chapter follows §1 instead — which is the right outcome and also evidence that §12 is dead text.] -->

### 12.1 Constructions the author deletes on sight

The constructions below were cut by the author from the first draft of §4.1 of Chapter 4. They are recorded verbatim, with the accepted replacement, because each names a habit rather than a single slip. Remove every instance from any chapter, in body prose, info-boxes, captions and alt-text alike.

**(a) Posture claims: the text describing its own argumentative conduct.** A chapter argues; it does not narrate that it is arguing, and it never awards itself credit for candour, rigour or balance. An informative cross-reference (§5.6) is a different thing and remains required.

> Cut: "The stance developed in this chapter follows directly from the position set out in Chapter 1, that agents are instruments serving the scientist's judgement rather than substitutes for it, and its practical content is a map of where…"
> Kept: "Agents are instruments that serve the scientist's judgement rather than substitutes for it."

> Cut: "The limitation of this framing, which this chapter takes seriously rather than sets aside, is that…"
> Kept: "The limitation is practical rather than conceptual: …"

**(b) Apologetic preambles about the description rather than the subject.** A hedge about the adequacy of the sentence itself carries no information. Also barred: "put simply", "roughly speaking", "for present purposes it suffices to say", and "to a first approximation" where no approximation is being made.

> Cut: "Described plainly enough to be useful here, the scientific method is a cycle: …"
> Kept: "The scientific method is a cycle: …"

**(c) Ornamental comparatives with an unstated baseline.** A comparison is either quantified against a real baseline (§6.1) or deleted. Also barred: "more X than is commonly appreciated", "far more X than the literature admits".

> Cut: "the two kinds of phase are interleaved in practice far more finely than any diagram of the cycle suggests"
> Kept: "the two kinds of work are interleaved within every phase"

**(d) Gravitas by abstraction, especially about reputation.** Accountability is stated as a mechanism, naming who answers and for what, never as an aura around the scientist. Chapter 4 §4.4 earns the point by defining accountability, interpretation and authorship outright; a compressed gesture at it earlier in the chapter is spending what has not yet been earned.

> Cut: "…is an interpretation that carries the scientist's name and standing."
> Kept: "…is a judgement. No second procedure can confirm it, and the scientist is answerable for it."

**(e) Elaboration where a plain statement was available.** Where two candidate rewrites both work, take the shorter and more literal one. The author's test is whether the sentence goes directly to the point; ornament added to a correct claim is a defect, not a flourish.

### 12.2 No metaphors

Manuscript prose contains no metaphors. Where a mechanism can be described literally, it is described literally, and figurative language is never a substitute for saying what actually happens. This is absolute for body prose, info-boxes, captions, alt-text and figure briefs. The rule covers the tired figures as much as the inventive ones: journeys and destinations, roads and paths, boundaries and territory, dials and switches, machinery and levers, reach and grasp, landscapes, arms races, silver bullets, low-hanging fruit.

The commonest offenders in this manuscript, with their literal replacements:

> Cut: "the boundary between them runs through the middle of the research cycle rather than neatly around its edge"
> Kept: "The two kinds of task are not separated by phase: data preparation contains judgements, and interpretation contains steps that can be checked."

> Cut: "The distinction is better seen as a dial rather than a switch."
> Kept: "The distinction is graded rather than binary."

> Cut: "extensions of the scientist's reach into the transformational phases"
> Kept: "instruments applied to the transformational phases"

> Cut: "treat automation as the destination and augmentation as a transitional stage on the way to it"
> Kept: "treat automation as the goal and augmentation as a temporary stage before it"

> Cut: "the specification and verification machinery the group already possesses"
> Kept: "the specification and verification practices the group already has"

What the rule does **not** cover, and what must not be flattened in the name of obeying it: (a) the book's defined technical terms, which are literal names for real components and are boxed in §9 (*gate*, *loop*, *pipeline*, *tool call*, *guardrail*, *orchestration*); (b) established scientific and statistical terminology (*ensemble spread*, *return period*, *drift*, *signal*, *noise*, *axis* in its geometric sense); (c) analogies that are explicitly flagged, developed and evidenced as arguments in their own right, of which the book permits a small number, the instrument analogy for agents chief among them, and which are introduced as comparisons ("agents are treated here as instruments, in the same sense as a calibrated sensor is an instrument") rather than smuggled in as ordinary description. A metaphor is figurative language doing the work that a literal statement should be doing; a defined term is not, and a declared analogy under examination is not.
