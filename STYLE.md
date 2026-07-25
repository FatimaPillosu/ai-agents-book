# Author writing-style guide

**v3.3 · 25 July 2026** · Binding for all drafted prose unless a specific brief overrides it.

**Change from v3.2 (minor):** the **no-em-dash-connector** rule from the v2.1 lineage is reinstated on the author's instruction: em dashes never join clauses or carry appositives and asides in manuscript text (§11); substitute a comma, colon, parentheses, a new sentence, or an introducing phrase. The dash survives only in fixed formats (headings and labels such as "Figure 1.1 — …" and "Definition — Gate"); en-dash ranges are unaffected. This is a deliberate house deviation from the thesis, which uses paired dashes for appositives; quoted thesis examples in this guide retain their original punctuation. §4 and §11 are amended accordingly.

**Change from v3.1 (minor):** the **no-contractions** rule from the v2.1 lineage is reinstated on the author's instruction (§11): manuscript text never contracts ("has not", never "hasn't"); verbatim quotations are exempt. The manuscript remains impersonal (no "you"), per §1.

**Change from v3.0 (minor):** the margin-note drafting mechanism is removed — the book will not use margin notes. The one-claim-per-paragraph discipline it enforced is retained in §2.

**Change from v2.0 (major):** the conversational-personal register introduced in v2.0 is withdrawn on the author's instruction. The register returns to the author's own academic voice, now specified in far greater detail by direct extraction from the author's PhD thesis (chapters 1–9, on medium-range prediction of areas at risk of flash floods). Every quoted example in this guide is taken verbatim from that thesis (lightly cleaned of LaTeX markup); where the abstraction and the example seem to disagree, imitate the example. The register-independent mechanisms of v2.0 are retained unchanged: integrity markers (§6.5), info-boxes and the glossary (§9), the sentence-per-line draft format (§10), British English and vendor-neutrality.

## 1. Voice and stance

Write as an experienced academic author in hydrology/meteorology: authoritative, precise and measured, with authority earned through evidence and construction rather than emphasis. The grammatical agent of the prose is the work, not the writer: "this book", "this chapter", "this study" perform the actions — "This chapter evaluates the feasibility of…", "This study demonstrates that…", "The innovation proposed by this research is twofold." The first-person plural appears sparingly, for methodological decisions and interpretive commitments ("We therefore make no additional adjustments for uncertainties in the reports' location or timing"); the first-person singular is rare; the reader is never addressed as "you". Impersonal constructions carry judgement where the author is taking a position that is arguable: "it is argued that…", "it is advocated that…", "It is worth noting that…".

Stakes are established with numbers and named events, never with adjectives. The thesis opens its whole argument this way: "Flash floods represent the deadliest and most devastating hazards, causing over 5,000 fatalities annually and accounting for ~85% of global flood incidents", and then grounds it: "In October 2024, flash floods in Valencia, Spain, claimed more than 200 lives and caused extensive damage in 87 municipalities". The severity of a topic is demonstrated, not asserted. Nothing is hyped; the largest claims are the most carefully hedged; and the prose stays serious throughout — no jokes, no asides, no exclamation, no cliché.

## 2. The paragraph is the unit of argument

A paragraph is long, developed and single-claim: typically 200–450 words, opening with a complete topic sentence and then moving through **claim → context → evidence → qualification → implication**. Every element of that movement is visible in the prose. Evidence is cited and quantified; the qualification is explicit (nearly every paragraph contains at least one "However" or equivalent concession); and the paragraph earns a closing sentence that states what follows from it — usually introduced by "Hence", "Consequently", "Therefore" or "Thus":

> "Therefore, developing robust medium-range flash flood forecasting capabilities on a global scale remains one of the pressing challenges in modern hydrology."

> "Consequently, despite the potential of global NWP rainfall forecasts to extend flash flood prediction beyond data-rich regions, their suitability for this purpose remains largely unverified at the scales required for global application."

Depth takes priority over coverage: develop fewer points properly rather than surveying many thinly. A paragraph never trails off on a detail; if it has no implication to state, it at least states its limitation.

A paragraph carries exactly one claim, and that claim must be summarisable as a single compressed nominal phrase ("Barrier n.1: limited direct assessment of global NWP rainfall forecasts against flash flood occurrence"; "CONUS as the primary study domain: justification"). If no single phrase covers the paragraph, it contains two claims and must be split; if the phrase is vague ("some thoughts on verification"), the paragraph has no claim yet. Read in sequence, the one-phrase summaries of a section's paragraphs must reproduce its argument — that is the test of a well-built section. The summaries themselves are a drafting check only and are never carried in the manuscript.

## 3. Opening the paragraph

Every paragraph opens with a full topic sentence carrying a real claim — never a fragment, never a scene-setting throat-clear, never a punchy hook. Four opening patterns account for almost every paragraph in the thesis; use them deliberately.

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

Rhetorical questions are permitted but rationed: at most one per section, placed as a pivot rather than an opener, and answered immediately — "Can data-driven approaches for flash flood prediction work with such a small training dataset?"; "This finding raised a compelling question: if diversity within a region enables generalisation, could combining observations from multiple regions extend this capability across continents or even globally?"

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

Before a draft is returned: (1) every paragraph opens with a complete topic sentence stating a real claim — no fragments, no throat-clearing; (2) every paragraph carries exactly one claim, summarisable as a single nominal phrase, and the section's paragraph summaries read as its argument (§2); (3) paragraphs are developed (≈200–450 words) and move claim → context → evidence → qualification → implication, closing on consequence or limitation; (4) every "However" is resolved; every announced enumeration is completed with parallel grammar; (5) numbers replace adjectives wherever the evidence allows, and comparisons carry baselines; (6) claims are hedged once, precisely, with certainty flags on substantive claims; anomalies are confronted, not buried; (7) literature and prior art are synthesised, not listed; (8) roadmap, pointer sentences and cross-references are in place and each names what the destination contains; (9) no second person, no exclamation, no hype, no bullet-point argumentation in main prose; (10) British English throughout; no contractions outside verbatim quotations; no em dash used as a connector (fixed formats and en-dash ranges only, §11); every demanding term defined once at first substantive use (info-box where warranted, §9); (11) all unverified material is marked [AUTHOR:]/[verify] and none invented; (12) the draft is sentence-per-line per §10.

## 8. Condensed prompt block

For agent-assisted drafting or review:

```
Write as an experienced academic author (hydrology/meteorology): authoritative, precise,
measured; the work is the agent ("this chapter shows…"), sparing "we", never "you".
British English; no contractions ("has not", never "hasn't"; quotations exempt).
Open every paragraph with a complete topic sentence carrying a real
claim — subject-first declarative, concessive ("Despite X, Y persists"), tension-framing
("…creates a fundamental tension between…"), or continuation pivot; never fragments or
hooks. Paragraphs 200–450 words, claim → context → evidence → qualification →
implication, closing on "Hence/Consequently/Therefore …"; one claim per paragraph,
summarisable as a single nominal phrase. Enumerate in prose ("two
challenges: First… Second…") with parallel grammar; concede and resolve ("However…" is
always answered); elaborate with colons and parentheses. No em dash as a connector in
manuscript text: use a comma, colon, parentheses, a new sentence, or "e.g." / "i.e." /
"such as" / "that is"; dashes only in fixed labels ("Figure 1.1 — …", "Definition —");
en-dash ranges (2023–24) are fine. Numbers over adjectives with
baselines ("a twenty-fold increase"); synthesise literature (set sources against each
other), never list. Hedge once, precisely (may/suggests/remains untested); certainty
flags (high/moderate/low confidence) on substantive claims; give rival interpretations
comparable weight and say when they cannot be disentangled; confront counterintuitive
results with candidate mechanisms. Explicit roadmaps ("The remainder of this chapter is
organised as follows…"), numbered barriers/opportunities/requirements, stated
contributions, pointer sentences to other chapters/repository. Results prose: quantified
observation (figure-anchored) → "This indicates that…" → implication. Stakes shown with
numbers and named events, never adjectives; no hype, jokes, exclamation or bullet-point
argument. Never fabricate: mark lived material [AUTHOR: …] and unverified figures
[verify]. Vendor-neutral. One sentence per line, unnumbered (STYLE.md §10).
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

**Rhythm.** Long, qualification-bearing sentences (25–45 words) dominate; a short declarative (4–10 words) is deployed deliberately, roughly once per paragraph, to land a turn: "However, significant challenges persist." "Recent developments confirm this issue." "This precedent suggests a way forward." The short sentence is an instrument of emphasis, not a default — and it is still a sentence, never a fragment.

**Connective vocabulary** (the working set, in the frequencies the thesis uses them):

- *Contrast/concession:* However · Nonetheless · Nevertheless · Notwithstanding (also postposed: "Low resolution notwithstanding, …") · In contrast · Conversely · Whilst · Although · Despite · Yet
- *Consequence:* Hence · Therefore · Consequently · Thus
- *Addition:* Moreover · Furthermore · Additionally
- *Precision/meta:* Specifically · In particular · Notably · To clarify · In this regard · It is worth noting that · For the sake of brevity and clarity

Do not open more than two consecutive paragraphs with the same connective, and never stack two contrast connectives in one sentence.

**Punctuation.** Colon to introduce the content of an abstraction just named; semicolons to hold parallel items of an in-sentence list; parentheses for compact specifics ("(e.g., …)", "(i.e., …)", resolutions, periods, versions) and for appositive definitions and asides. Lists inside prose keep parallel grammar throughout.

**No em dashes as connectors.** The em dash never joins clauses, appends an afterthought or carries an aside in manuscript text (body prose, info-boxes, captions and alt-text alike). Substitute whichever is plainest of: a comma, a colon, parentheses, a new sentence, or an introducing phrase such as "e.g.", "i.e.", "such as" or "that is". The dash survives only in fixed formats: headings and labels ("Figure 1.1 — …", "Definition — Gate"), status headers, figure-brief fields and reference lists. En dashes in numeric and date ranges (2023–24, pp. 10–12) are unaffected. This is a deliberate house deviation from the thesis, which uses paired dashes for appositives; quoted thesis examples in this guide retain them, and [AUTHOR: …] markers are working notes outside the rule's scope.

**British English throughout**, including captions, alt-text and repository docs: -ise endings, *whilst*, *amongst*, *behaviour*, *modelling*, *parametrisation*, *centre*; dates as "23 August 2021". Units and quantities are precise and SI; percentages, return periods, resolutions and lead times always take figures ("~31 km", "0.27%", "up to day 5").

**No contractions.** Manuscript text never contracts: write "has not", "do not", "it is", "cannot"; never "hasn't", "don't", "it's", "can't". The rule binds body prose, info-boxes, captions and alt-text alike; verbatim quotations are exempt. (This is in any case the register of the thesis, which contains no contractions; the rule makes it explicit and checkable.)

## 12. Anti-patterns

Never: punchy fragment openers or one-sentence paragraphs; addressing the reader as "you"; exclamation marks; hype vocabulary ("game-changing", "revolutionary", "the hype suggests"); jokes, irony or self-deprecation; bullet lists carrying the argument of body prose (bullets are for genuinely enumerable reference material only); adjectives where a number exists; bare citation lists in place of synthesis; unresolved "However"s; announced enumerations left incomplete; claims without hedges or hedges without claims (mush like "it could perhaps be argued that X might possibly…"); burying a counterintuitive result; scaffolding that points nowhere ("more on this later") — a pointer always names its destination and what will be found there.
