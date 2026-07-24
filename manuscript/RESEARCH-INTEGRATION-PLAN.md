# Research integration plan — pass R2

**v1.0 · 24 July 2026** · Maintained by ai-editor. Executed by **ai-writer**; reviewed against by **ai-reviewer**. This plan governs the integration of the two research reports produced after revision pass R1 closed. R1 (`manuscript/REVISION-PLAN.md`) is **complete and closed**: all chapters are in STYLE.md v2.0 voice, de-duplicated, and citation-woven from the first research sweep. R2 changes nothing about voice, structure or de-duplication; it only updates and extends the evidence layer.

A writer batch needs this document, `STYLE.md` v2.0, the three reports in `/research`, and the chapter files assigned to the batch — nothing else. `FIGURES.md` is not needed: **R2 adds or changes no figures.**

**The three reports:**

- **R-1** `research/2026-07-24-agentic-ai-foundations-sweep.md` — 44 sources, already woven during R1. The baseline. R2 does not re-weave it.
- **R-2** `research/2026-07-24-2026-literature-update.md` — 22 new 2026 sources, including sources that supersede or significantly revise first-sweep entries. Not yet used.
- **R-3** `research/2026-07-24-youtube-channels-2026.md` — 18 practitioner videos across 5 channels. Grey literature. Not yet used. Governed by the video policy in §2.

**What R2 is:** (i) update citations that R-2 shows to be superseded or significantly revised; (ii) weave new 2026 sources where they support an existing claim or fill a gap the manuscript itself names; (iii) apply the practitioner-video policy, including a new section in `FURTHER-READING.md`; (iv) update `FURTHER-READING.md` throughout.

**What R2 is not:** no revoicing, no restructuring, no de-duplication changes, no new figures, no new info-boxes, no glossary edits, no length reduction, no companion-repository work, no edits to admin documents (ai-editor only). **The book must not become a literature review**: a source earns its place only where it supports a claim the chapter already makes or corrects a claim the new evidence has overtaken. If in doubt, leave it out — everything verified is preserved in `/research` and most of it surfaces in `FURTHER-READING.md` instead.

---

## 1. Global rules (apply to every batch)

- **G1 — Citations only from `/research`.** Every new or updated citation traces to a named entry in R-1, R-2 or R-3, with its DOI or URL added to the chapter's references list. Never cite from memory. Never resolve a `[verify]` flag the report itself carries: where a report entry flags a detail `[verify]`, either omit that detail from prose or carry the flag with it.
- **G2 — Carry the caveats.** Each report entry names its caveats (preprint status, domain limits, self-reported evidence, single-venue figures). New prose must fold the load-bearing caveat in naturally, per STYLE.md certainty flags — e.g. "a 2026 preprint, not yet peer-reviewed, reports…", "self-reported by the developer, so read it as a claim to verify, not a measurement". A number never appears without its date and domain.
- **G3 — Vendor neutrality in prose.** No product, vendor, model or channel name in manuscript prose; names live only in the references list. Model-specific results are aggregated vendor-neutrally: Mehta's per-model figures become "across four frontier models, submission rates of 70–100% coexisted with true resolution rates of 18–50%"; Soumik's cost result becomes "a mid-tier judge model with debiasing reached 71% agreement with human judgements at roughly one-fifteenth the cost of top-tier alternatives"; the Anthropic Institute report is "one frontier-model developer's account of its own engineering organisation". Standards bodies and evaluation organisations (NIST, OWASP, WMO, the Five Eyes agencies, METR) may be named in prose, as institutions rather than products.
- **G4 — Integrity (hard rules).** Never fabricate. Never resolve, move or delete an `[AUTHOR: …]` marker. British English. Sentence-per-line for all new body prose (STYLE.md §10). v2.0 voice for every new sentence — new material must be indistinguishable in register from its surroundings.
- **G5 — No new info-boxes; GLOSSARY.md closed.** Any new demanding term is explained inline in plain language in the same sentence or the next (e.g. Cohen's kappa: "chance-corrected — the agreement left over once you subtract what two coin-flippers would reach"). Do not edit `manuscript/GLOSSARY.md`.
- **G6 — De-duplication discipline holds.** New evidence is woven only at the placements this plan names, which respect the R1 canonical-home map. Do not re-derive a mechanism outside its canonical home to make room for a citation; attach the citation to the existing sentence instead.
- **G7 — Word-growth caps.** Each chapter has a cap in §5 (net growth over its current length). The caps sum to roughly 2,300 words book-wide, excluding `FURTHER-READING.md`. A cap is a ceiling, not a target: if an instruction can be met in fewer words, use fewer.
- **G8 — Nothing unexecuted presented as accomplished.** WP-MIP is cited for its existence and design only — it has published no comparative results. Ch08's own three-track example remains a worked design and the chapter note saying so is untouched. The AI Scientist result is a workshop-tier acceptance, stated as such.
- **G9 — References format.** New entries follow each chapter's existing references style. Video references use the grey-literature format in §2.3.
- **G10 — Untouched files.** `ch00-front-matter.md`, `ch06-data-acquisition-and-quality-control.md` and `GLOSSARY.md` are not edited in R2 (reasons in §4). No batch touches admin documents or another batch's files.

## 2. Practitioner-video policy (R-3) — decided

This policy is a decision of this plan, binding on ai-writer and reviewable by ai-reviewer.

### 2.1 Standing

1. **Video-derived concepts are corroborating colour, never primary evidence.** A video citation may only ever accompany a claim the chapter already makes and already supports (from R-1/R-2 evidence, from the book's own argument, or from the author's lived material). Its function is to show practitioner convergence: "working practitioners have independently arrived at the same principle". A video is never the sole support for any claim.
2. **No `[verify]`-flagged video claim enters the manuscript as fact.** Every incident, statistic, named report, vendor case study or capability figure relayed inside a video is unverified. None of them appears in prose — not even flagged. This excludes, in particular: the Vercel tool-deletion anecdote; the database-deletion incident; the repository-upload incident; all Shadow-AI statistics; the "MIT 2025 report" figure; the "agents cost 10–50× more" claim; all token-volume, adoption-share and market figures; the "Stanford, Harvard and Yale paper" and the oracle/evaluator/architect framework; the Gary Marcus reference; every platform limit and benchmark number quoted in a video.
3. **Paraphrase, never quotation.** Transcripts are auto-generated; R-3 states its wording is close paraphrase, not verified verbatim. New prose paraphrases without quotation marks.
4. **One video citation per chapter, in seven chapters only** (ch02, ch03, ch04, ch11, ch12, ch13, ch14 — assignments in §5). No other chapter cites a video. Total in-chapter video citations: seven, drawing on six distinct videos.
5. **Everything else goes to `FURTHER-READING.md`** (new practitioner-commentary section, §6) or is not used at all. The @aifoundershq channel's remaining output, the sponsored segments, and the Jeff Su "Top 6 AI Trends" statistics are not used anywhere.

### 2.2 Rationale (for the record)

The convergence R-3 documents — harness over model, silent failure as the dangerous mode, specification-with-proof-of-done, consequence-tiered permissions — is real corroborating signal from differently incentivised commentators, and the book's preface-level claim to sit inside a practitioner convergence is worth one citation per site. But video content is unreviewed, promotionally entangled and transcription-noisy; letting it carry evidential weight would undercut the book's own evidential-tier teaching (ch11). The policy above lets the book use the signal without borrowing the noise.

### 2.3 Grey-literature citation format for videos

In references lists:

```
Creator (2026). "Video title." Video, [channel name], DD Month 2026. https://www.youtube.com/watch?v=…
```

Channel and creator names appear only in references, never in prose ("a practitioner commentator", "practitioner guidance" in prose). Each entry carries the trailing note "(practitioner commentary; concepts cited as corroboration, not evidence)".

## 3. Superseded and revised citations — the update list

These are corrections, not additions. ai-reviewer verifies each one explicitly.

| # | First-sweep basis | 2026 development (R-2) | Action |
|---|---|---|---|
| S1 | Lu et al. (2024), "The AI Scientist", arXiv preprint | **Superseded**: Lu et al. (2026), "Towards end-to-end automation of AI research", *Nature* 651, 914–919, DOI 10.1038/s41586-026-10265-5 — peer-reviewed, more evidence, franker limitations | Replace the 2024 preprint citation everywhere it appears (currently `FURTHER-READING.md` only) and weave the 2026 version into ch01, ch09, ch11 per §5. Always workshop-tier framing per G8. |
| S2 | Zheng et al. (2023) / Shi et al. (2024) headline judge-agreement figures | **Significantly qualified**: Norman, Rivera & Hughes (2026), arXiv 2606.19544 — exact-match agreement overstates chance-corrected (kappa) agreement by 33–41 points; judges with test-retest reliability >0.95 coexist with severe position bias | Zheng/Shi citations stay (they are the founding evidence) but every passage leaning on judge agreement gains the Norman qualification: ch11 §11.5 (substantive), ch10 §10.3 (one clause). "Consistency is not correctness" enters ch11's checklist as a clause. |
| S3 | Zhu et al. (2025), Agentic Benchmark Checklist (one case study) | **Extended and scaled**: Wang, Bianchi, Zhu et al. (2026), arXiv 2605.26079 — audit automated, 168 benchmarks, defects in >25.7% of tasks | Keep Zhu; add Wang alongside it at both existing Zhu sites: ch11 (§11.3/§11.5) and ch07 §7.5. |
| S4 | NIST AI 600-1 (2024, generative AI broadly) | **Extended to agents**: NIST CAISI AI Agent Standards Initiative (Feb 2026) | Keep AI 600-1 in ch12; add CAISI in ch12 §12.9 — initiative's existence and stated scope only, no COSAiS specifics (`[verify]` in R-2). |
| S5 | First sweep's named gap: NCSC/UK security guidance not swept | **Filled**: Five Eyes joint advisory "Careful Adoption of Agentic AI Services" (Apr 2026) + NCSC-UK companion blog (15 May 2026, directly fetched) | Add to ch12 §12.9 (substantive) and ch16 (one sentence). Only the recommendations R-2 confirms from the fetched blog are citable in detail; the 23-risk/100-practice catalogue is cited at summary level with `[verify]` for anything more specific. |
| S6 | First sweep's named gap: "no study directly measures false-negative rates of LLM review gates" — stated in prose at **ch11 §11.5** and in `FURTHER-READING.md` §Gaps | **Partially addressed**: Mehta (2026), arXiv 2603.25764 (submission rate vs test-verified resolution rate) and Wang et al. (2026) (grader defect rates) | Rewrite ch11 §11.5's claim to "the first direct measurements are appearing" per §5/ch11; seeded-defect testing stays as the practitioner's answer, unchanged. Update the `FURTHER-READING.md` gaps section to match. |
| S7 | Ch08 §8.5 three-track intercomparison: "a worked design, not an executed case study" | **Field context**: WP-MIP (2026), arXiv 2604.16643 — a real, running, WMO-coordinated three-track intercomparison | Ch08 §8.5 gains the field-context paragraph per §5. The worked-design status of the book's own example is restated, not weakened (G8). |
| S8 | OWASP Top 10 for LLM Applications 2025 (ch12) | **Companion list**: OWASP Top 10 for Agentic Applications for 2026 (ASI01–10) | Keep the LLM list; add the agentic companion in ch12 §12.8 — existence and role only; individual ASI category names are `[verify]` and are not named or numbered. |
| S9 | Ch01 §1.2 `[verify]` on the coding-benchmark trajectory ("figures several times higher by late 2025 [verify]") | R-2's Anthropic Institute entry supports "from single-digit scores to near-saturation over roughly two years", self-reported | Rework the clause to the report-supported form with the self-reported caveat and cite; the `[verify]` flag is then removed. The `[AUTHOR: …]` marker on per-token prices in the same section is untouched. |

## 4. What is NOT incorporated, and why

ai-reviewer checks these are absent.

- **Everything in §2.1 item 2** (unverified video-relayed claims and statistics).
- **OWASP ASI01–ASI10 individual category names** — resting on secondary sources (`[verify]` in R-2).
- **COSAiS / SP 800-53 overlay specifics** — not verified against a NIST primary source.
- **EU AI Act 2026 developments** — located at search-result level only; explicitly a gap in both sweeps. Nothing enters the manuscript.
- **Yan et al. (2026) specific numbers** (the >90% reduction, "within minutes") — the primary page returned HTTP 403; the source is cited for existence and its six-level autonomy framework only, with R-2's `[verify]` caveat carried in the reference.
- **Tang et al. (2026) beyond one conceptual sentence in ch10** — evidence is from simulated economic/social settings, far from the book's domain.
- **FALAT as a deployable method** — 29–46% attribution accuracy is cited as evidence the problem is hard, never as a recommended tool.
- **Oh et al. UQ techniques' performance** — the survey catalogues open problems; no UQ method is cited as working.
- **τ²-bench specifics** — nothing in the manuscript needs it.
- **WP-MIP comparative results** — none exist (G8).
- **Anthropic Institute report details beyond the doubling trend, the >80%-of-merged-code figure and the SWE-bench/CORE-Bench trajectory summary** — the 64% research-judgement preference, the employee quotations and the pause proposal are not woven (the quotations are lived-colour material the author may choose later; nothing in R2 pre-empts that).
- **Zheng et al. (2026) SCION beyond one convergence sentence in ch17** — a weeks-old proposal, not validated technology.
- **ch00 front matter** — its positioning claim carries an author-owned caveat structure ("limited scan, Jul 2026 — re-verify before release"); updating the positioning evidence is an author decision at the deferred re-scan, not a citation-weaving task.
- **ch06** — R-2 offers only an optional Yan et al. clause for data retrieval; the chapter's claims are already adequately supported and the source's details are unverified. Bloat risk exceeds benefit.
- **ch05 §5.4's worked example** — the frontier-synthesis example is the author's own designed workflow; the new hydrology sources (Lopez-Gomez, Yan) are woven in ch08, their canonical fit, not re-cited here.
- **The remaining 12 videos** beyond the six cited in chapters — a curated subset appears in `FURTHER-READING.md` (§6); the rest are unused.

## 5. Per-chapter instructions

Task IDs (e.g. **11.2**) are what ai-reviewer reviews against, item by item. "Cap" is the G7 net-growth ceiling. All placements name existing sections; the writer attaches new sentences to the existing argument at the stated point, never opening a new section.

### ch01 — Why agents, why now (cap +170)

- **1.1** §1.2, after the SWE-bench trajectory sentence: rework that clause per **S9** (near-saturation over roughly two years, self-reported by one frontier-model developer; cite Anthropic Institute 2026; remove the `[verify]`). Then add two to three sentences giving the trend its 2026 quantitative anchor: an independent evaluation organisation's fixed-task-suite measure shows the duration of tasks agents complete autonomously at 50% success doubling roughly every four months from 2023 (≈129 days, 90% CI 105–157) and roughly every three months from 2024, against roughly seven months across 2019–25 (METR 2026); the same rate appears in the developer's self-reported figures — two different methods, both from parties with an interest in demonstrating progress, agreeing on the trend (fold the caveat in per G2).
- **1.2** §1.2 (or §1.4 if it lands better against the honest-capability-boundary argument — writer's choice, one site only): one sentence adding the 2026 timeline anchor: a fully machine-generated paper passed peer review at a workshop venue, a result itself now peer-reviewed (Lu et al. 2026, *Nature*), with the authors stating the system cannot yet meet top-tier publication standards — workshop tier stated per G8.
- **1.3** References: add METR (2026), Anthropic Institute (2026), Lu et al. (2026). No figure changes (the Figure 1.1 brief already ends at governed workflows, 2026).

### ch02 — Anatomy of an agent (cap +90)

- **2.1** §2.1: one to two sentences noting that independent 2026 taxonomies continue to converge on essentially the book's decomposition — a January 2026 survey's six dimensions (perception, brain, planning, action, tool use, collaboration) map onto the loop, tools, context and orchestration anatomy, with collaboration corresponding to Chapter 10's territory (Arunkumar et al. 2026; preprint caveat; cite for taxonomic vocabulary only).
- **2.2** §2.1 (same neighbourhood): one sentence of practitioner corroboration — practitioners have converged on a name for the whole assembly around the model, the "harness", and on the observation that it, more than the model, determines what an agent can actually do (video: Jones, "Don't build more AI agents until you watch this", 17 Jun 2026; per §2 policy).
- **2.3** References: add Arunkumar et al. (2026) and the video (format §2.3).

### ch03 — Specifying work for agents (cap +80)

- **3.1** §3.3 or §3.4 (one site): one to two sentences: the schema is the book's own synthesis — the first sweep found no dedicated academic treatment — but it is not idiosyncratic: a widely followed practitioner formulation of the "delegation loop" (a goal, the sources to use, a standard the output must meet, an explicit permission boundary, a defined proof that work is done) matches the schema element for element, with proof-of-done playing the role of acceptance criteria (video: Jones, "Codex: Your First Personal AI Agent Delegation Loop", 12 Jun 2026; per §2 policy).
- **3.2** References: add the video.

### ch04 — The scientist's stance (cap +60)

- **4.1** §4.3, at the point where the decision procedure asks whether an agent is needed at all: one sentence: the same test circulates in practitioner guidance as the "workflow test" — if a fixed sequence of steps with at most a judgement call or two would do, build a workflow, not an agent (video: AI Founders, "Don't Build an AI Agent Until You Can Answer These 8 Questions", 17 May 2026; per §2 policy; the video's sponsored segment is excluded by that policy).
- **4.2** References: add the video.

### ch05 — Evidence and literature synthesis (cap +180)

- **5.1** §5.3, in the citation-verification-gate discussion: two to three sentences of mitigation evidence — a 2026 preprint benchmarked machine-generated reference entries across three frontier models and four domains: 83.6% of individual fields correct but only 50.9% of entries fully correct (a single wrong field passes a casual glance more easily than a fabrication), and a two-stage design — model draft, then deterministic resolution against bibliographic services — raised fully correct entries to 78.3% while cutting tool-introduced regressions to 0.8%, against 4.8% for a cruder one-stage integration (Rao & Callison-Burch 2026). The design of the gate measurably changes the residual risk — which is this section's claim.
- **5.2** §5.5, after the Walters/Cabezas-Clavijo sentence: one sentence from the same study on the recency effect — accuracy fell by 27.7 percentage points for recent papers versus well-known ones, the models leaning on memorised knowledge even when search tools were available: retrieval access does not guarantee retrieval use.
- **5.3** §5.5, same paragraph: two sentences from Ansari (2026) — fabricated citations survive even elite peer review: 100 fabricated citations were found across 53 papers accepted at a top machine-learning venue in 2025 (about 1% of accepted papers, a single-venue single-year figure), typically only one or two per paper — small contaminations that three to five expert readers missed. This is exactly why the check must be mechanical and tool-executed, not a plausibility read (attach to the section's existing moral; do not re-derive it).
- **5.4** References: add Rao & Callison-Burch (2026), Ansari (2026), each with preprint caveat.

### ch07 — Coding and pipeline agents (cap +80)

- **7.1** §7.5, extending the existing Zhu et al. (2025) sentence (per **S3**): one to two sentences — the audit has since been automated and run at scale: an agentic auditor applied to 168 benchmarks found defects (ambiguous tasks, environment conflicts, incorrect ground truth) in over a quarter of tasks, and removing them shifted two widely used coding-benchmark scores by roughly ten percentage points (Wang et al. 2026; preprint; coding-domain figure, not universal).
- **7.2** References: add Wang et al. (2026).

### ch08 — Model orchestration and experimentation (cap +280)

- **8.1** §8.1 (the existing sentence at the chapter opening citing Zhu et al. 2026 `[verify]` on calibration agents): extend with one sentence — the same year, a hydrology preprint defined a six-level autonomy framework for model-operating agents and demonstrated a high-autonomy level retrospectively on a real flood event (Yan et al. 2026, `[verify]` carried in the reference per §4 — no numbers from this source in prose); note, in half a sentence, that these first-wave domain papers are capability-first, with none of the governance apparatus this chapter builds — the gap this book exists to fill.
- **8.2** §8.3, after the "monitor and log, do not decide" stance is stated: two to three sentences — the division of labour has a strong 2026 in-domain demonstration: an agentic system was used for the design work (dataset discovery, knowledge synthesis, architecture search) of a seasonal streamflow forecasting system, while the resulting forecaster itself stayed a conventional, interpretable statistical model, benchmarked against a government operational baseline over 2021–25 with up to 29% lower quantile forecast error for early-season runoff (Lopez-Gomez et al. 2026; preprint; single region, dated figure per G2). The agent designs; the auditable model forecasts — the same division this section argues for.
- **8.3** §8.5, in the introductory passage (before or after the "honest about its status" sentence around the worked-design framing): a short paragraph (three to four sentences) per **S7** — the three-track structure is no longer only this book's proposal: as of 2026, a WMO-coordinated international project (WP-MIP, roughly 65 authors across six continents) is running exactly this machine-learning / physically based / hybrid intercomparison at institutional scale, building a centralised forecast database under both institution-specific and standardised initial conditions for distributed verification. Cite for the project's existence and design only — it has published no comparative results, and this book's own example remains a worked design awaiting execution (restate; the chapter note at the top of the file is untouched).
- **8.4** References: add Yan et al. (2026) (with `[verify]` note), Lopez-Gomez et al. (2026), WP-MIP (McTaggart-Cowan et al. 2026).

### ch09 — From results to manuscript (cap +220)

- **9.1** §9.4 (policy landscape): three to four sentences — the 2026 evidence sharpens the chapter's "stable core, divergent mechanics" reading. The stable core: a major publisher's June 2026 policy restates human-only authorship and whole-work accountability. The divergent mechanics: the same policy sets a concrete disclosure threshold (routine grammar and spelling checking exempt; any substantive change to structure or content declared, with a suggested declaration naming the tool and purpose) and permits reviewers a narrow, non-retaining-tool use for polishing their own reports — sharper than the blanket prohibitions some funders maintain (Elsevier 2026; policy page, specifics volatile per the repository rule). And a peer-reviewed systematic review of 60 sources concludes the policy landscape is fragmented and reactive, with disclosure practice varying enormously by discipline while formal prohibition of machine authorship is universal (Slimi 2026, *Frontiers in Education*).
- **9.2** §9.4, closing the section (or adjacent, writer's judgement within §9.4): two sentences per **S1** — end-to-end automation is now peer-reviewed capability evidence: a fully machine-generated paper was accepted at a workshop venue, and the authors themselves state the system cannot meet top-tier standards, name hallucinated and inaccurately cited content among its failure modes, and warn that automated submission at scale could overwhelm peer-review capacity (Lu et al. 2026, *Nature*). The chapter's rule — agents draft under author control and are never authors — is unchanged by the capability.
- **9.3** References: add Elsevier (2026), Slimi (2026), Lu et al. (2026). §9.6's trimmed fabricated-citations paragraph is **not** extended (T1 canonical homes are ch05/ch13).

### ch10 — Multi-agent workflows (cap +170)

- **10.1** §10.3, attached to the existing Zheng et al. (2023) sentence (per **S2**): one to two sentences — a 2026 large-scale evaluation (21 judge models, roughly 541,000 judgements) found that exact-match agreement figures overstate chance-corrected agreement by 33–41 percentage points, and that judges can be highly self-consistent while carrying severe position bias — a reviewer can be dependably wrong in a fixed direction, so self-consistency is not evidence of soundness (Norman, Rivera & Hughes 2026; preprint; general chat/QA benchmarks, not scientific artefacts).
- **10.2** §10.6 (failure modes): two to three sentences — post-hoc review of a failed multi-agent run tends to blame the step where the failure became visible rather than the step that caused it, because later steps inherit corrupted state; purpose-built attribution methods reach only roughly 29–46% step-level accuracy on known-cause trajectories, so causal attribution in long trajectories is genuinely hard, not a matter of reviewer diligence (Rafi et al. 2026; preprint). One further sentence: 2026 work also names a category the per-agent view misses entirely — emergent collective failures that no single agent's transcript explains — so far demonstrated only in simulated economic and social settings, cited here for the concept, not as domain evidence (Tang et al. 2026).
- **10.3** References: add Norman et al. (2026), Rafi et al. (2026), Tang et al. (2026).

### ch11 — Verification and evaluation (cap +430)

The chapter's centre of gravity, and R2's. Five tasks.

- **11.1 The gap-claim rewrite (S6).** §11.5, the passage "The `/research` sweep behind this book found no study that directly measures the false-negative rate of an LLM review gate … So there is no number to borrow." Rewrite to this shape (writer's wording, same register): when the first sweep behind this book was compiled, no study directly measured the false-negative rate of an LLM review gate; by mid-2026 the first direct measurements were appearing. Then two to four sentences on Mehta (2026): across 1,750 agent trajectories on 50 real coding tasks, four frontier models submitted a patch 70–100% of the time while actually resolving the issue only 18–50% of the time, and these silent semantic failures — confidently wrong, stable across repeated runs — dominated every model's failure profile (68–80%), so the two cheap signals a practitioner reaches for first, "did it finish?" and "does it repeat?", look healthy exactly when the output cannot be trusted (vendor-neutral aggregation per G3; preprint; coding-domain figures that transfer structurally, not numerically). Add Wang et al. (2026) in one clause as the grader-side counterpart (defects in over a quarter of benchmark tasks — the gate itself measurably wrong). Close the rewrite by keeping the section's spine intact: none of these studies measures *your* gate on *your* work, so the practitioner's answer is unchanged — seeded-defect testing, which follows exactly as it stands. **Everything from "The method is seeded-defect testing" onward is untouched in substance.**
- **11.2 The judge-agreement qualification (S2).** §11.5, the judge-bias paragraph (currently Zheng → Shi → Wataoka): extend with three to five sentences on Norman, Rivera & Hughes (2026) — the largest judge evaluation to date (21 judges, nine providers, ~541,000 judgements): first, agreement deflation — exact-match agreement overstates chance-corrected agreement by 33–41 percentage points once measured with Cohen's kappa (gloss inline per G5), so any headline agreement figure, including the founding study's, must be read chance-corrected; second, the title finding, reliability without validity — production judges with test-retest reliability above 0.95 coexisting with severe position bias, meaning a gate can be dependably wrong in a fixed direction and a naive self-consistency check will falsely certify it. Then one to two sentences on Soumik (2026): in a 2026 mitigation study, style bias — preferring formatted answers over plain prose — was the largest bias measured (0.10–0.76 depending on model), larger than the position bias the field had focused on: a reviewer gate can be gamed, deliberately or accidentally, by formatting alone (preprint caveats per G2).
- **11.3 Peer-reviewed automated-review data point (S1).** Same neighbourhood (end of the judge discussion or where the section weighs automated review as an instrument): one to two sentences — the strongest peer-reviewed automated-reviewer result to date: 69% balanced accuracy against expert consensus on conference review decisions, marginally above the 66% of the human reviewers it was benchmarked against — a striking but narrow result, from machine-learning workshop-tier reviewing, not scientific correctness (Lu et al. 2026, *Nature*).
- **11.4 Practitioner corroboration + UQ boundary.** (a) §11.4, one sentence: practitioner guidance converges on the same starting move — test against roughly ten self-completed, known-answer examples before removing the human from a workflow's loop, and graduate autonomy by the score (video: Davis, "How Anthropic's Own Team Gets AI to Stop Lying to Them", 20 Jun 2026; per §2 policy — cited as practitioner corroboration of the section's method, and the underlying vendor post is not cited since R-3 could not identify it). (b) §11.7, two to three sentences: a confidence-scored agent output ("I am 80% sure this flag is correct") is a different and markedly less mature capability than a pass/fail gate — uncertainty quantification for agents is an open research field, catalogued by a 2026 peer-reviewed survey as foundations-and-challenges, not working methods — so a self-reported confidence number is never treated as a measured gate (Oh et al. 2026, ACL).
- **11.5 Checklist clause.** §11.8: extend the existing gate-measurement item with one clause: high judge self-consistency is never read as low bias — consistency is not correctness. No new checklist item.
- **11.6** References: add Mehta (2026), Norman et al. (2026), Soumik (2026), Wang et al. (2026), Oh et al. (2026), Lu et al. (2026), and the Davis video (format §2.3).

### ch12 — Provenance, governance and security (cap +260)

- **12.1** §12.9 (what institutional IT will ask): a short paragraph (three to five sentences) per **S5** — in 2026 six national cyber-security agencies across five countries issued the first coordinated guidance on agentic AI specifically, cataloguing risks across privilege, design, behavioural, structural and accountability categories `[verify any detail beyond this against the primary PDF]`, and its verified recommendations read like this chapter's summary: begin with tightly bounded, low-risk pilots; apply least privilege with time-limited, temporary credentials; monitor behaviour continuously; and establish named human accountability before deployment — an agent you cannot understand, monitor or contain is not ready for deployment (paraphrase; Five Eyes joint advisory 2026 / NCSC-UK blog 2026). One further sentence per **S4**: the US standards body has opened an agent-specific standards initiative on interoperability, and — the part institutional IT will ask about — agent identity and authorisation: which credentials an agent holds and how a system verifies which agent is acting (NIST CAISI 2026; cite the initiative's existence and stated scope only).
- **12.2** §12.8 (least privilege and the trust boundary), per **S8**: one to two sentences — the institutional vocabulary has kept pace: alongside the LLM top-ten already cited, a companion top-ten for agentic applications now exists, effectively expanding the "excessive agency" category into a full agent-specific risk list once systems take autonomous, credentialed, multi-step action (OWASP 2026; individual category names not cited per §4).
- **12.3** §12.8, one sentence of practitioner corroboration: practitioner guidance independently frames the same principle as consequence-tiered permissions — fully autonomous only where low-stakes and reversible, propose-then-approve in the middle, never-autonomous at the top — designed around the action's consequences rather than any model's current capability, because models change and the permission gradient should not (video: AI Founders, 17 May 2026; per §2 policy; paraphrase).
- **12.4** References: add the Five Eyes/NCSC pair, NIST CAISI (2026), OWASP Agentic Top 10 (2026), and the video.

### ch13 — The failure gallery (cap +150)

- **13.1** §13.2 (fabricated citations), after the entry's existing evidence: three to four sentences from Ansari (2026) — the strongest 2026 update: 100 fabricated citations found across 53 papers *accepted* at an elite machine-learning venue in 2025, i.e. past three to five expert reviewers each — roughly 1% of accepted papers (single venue, single year); a five-mode taxonomy led by total fabrication (66%) and partial attribute corruption (27%), with identifier hijacking (a real DOI stitched to a fake reference) as a distinct mode; and, most usefully, the contamination was typically one or two citations per paper — small enough for expert plausibility reading to miss, which is this entry's argument for a mechanical check made with harder evidence (preprint; the irony that the study of fabricated citations is itself unreviewed may be named in half a sentence, in the chapter's voice).
- **13.2** §13.6 (context loss), one sentence of practitioner corroboration: the same silent-truncation failure is independently named in practitioner commentary — large inputs partially read, answered fluently, with no warning, so an explicit "file too big" error is the good outcome because it is at least visible (video: Davis, "Claude Confidently Skipped Half Your Document and Didn't Tell You", 16 May 2026; per §2 policy; paraphrase; none of the video's thresholds or product limits appear).
- **13.3** References: add Ansari (2026) and the video. §13.5 (over-agreeable review) is **not** extended — the Norman qualification lives in ch11/ch10 (G6).

### ch14 — Verification under constraint (cap +60)

- **14.1** §14.2 (the constraints that determine the architecture), where the data-sovereignty constraint is argued: one to two sentences of practitioner corroboration — the same two design conclusions now circulate independently in practitioner commentary: instructing a cloud model not to read or transmit something is a behavioural safeguard that can be silently violated, so only an architectural boundary (no network path) is reliable; and an offline local model triaging material into risk tiers before anything external is contacted is exactly the pattern of this chapter's tiered toolkit (video: Jones, "I Cut the Internet and Let AI Read the File I Could Never Upload", 19 Jul 2026; per §2 policy; the video's named incident is excluded per §2.1).
- **14.2** References: add the video. The chapter's executed-work integrity line in its header is untouched.

### ch15 — Governing a modelling workflow end to end (cap +50)

- **15.1** One sentence, placed in the passage that cites the operational parallel-run precedent (the AIFS / Ben Bouallègue discussion): the discipline now extends to agent-designed systems — a 2026 preprint benchmarked an agent-designed seasonal streamflow forecaster against the responsible government agency's operational forecasts across multiple years before any claim of skill (Lopez-Gomez et al. 2026) — the same protocol this chapter's publication run demands.
- **15.2** References: add Lopez-Gomez et al. (2026).

### ch16 — Starting in your own group (cap +170)

- **16.1** §16.2 (thirty-day on-ramp), supporting the existing capabilities-not-tools argument: two sentences — the strongest current measure of agent capability growth has autonomous task length doubling roughly every three to four months as of 2026 (METR 2026), so an on-ramp built around today's task-length ceiling is obsolete within a single budget cycle; the durable investment is the governance capability — specification, gates, measurement — which survives every capability jump. One further sentence: the start-small stance is now multi-national security guidance — begin with tightly bounded pilots on low-risk, clearly defined tasks before expanding scope (Five Eyes 2026).
- **16.2** §16.3 (where the money goes): one sentence — the judge-cost axis is real and optimisable: a 2026 study found a mid-tier judge model with debiasing reached 71% agreement with human judgements at roughly one-fifteenth the inference cost of top-tier alternatives (Soumik 2026; preprint; per G3).
- **16.3** §16.5 (institutional considerations): one sentence — a peer-reviewed 2026 systematic review reaches the same conclusion this section builds on: prevailing reactive policy frameworks are inadequate, and groups need proactive governance rather than waiting for settled institutional rules (Slimi 2026).
- **16.4** References: add METR (2026), Five Eyes/NCSC (2026), Soumik (2026), Slimi (2026).

### ch17 — What will last (cap +130)

- **17.1** §17.2 or §17.3 (one site): two to three sentences using the year's loudest capability claim as a closing teaching example — the most consequential 2026 capability report is a frontier-model developer's self-reported account of its own agents (most of its production code machine-written, task horizons doubling every few months), from a party with every incentive to demonstrate progress; the book's whole stance says to treat such claims as hypotheses for independent measurement, and the partial independent corroboration that exists (an outside evaluation organisation measuring the same doubling by a different method) is what verification of a vendor claim actually looks like (Anthropic Institute 2026; METR 2026).
- **17.2** §17.2, one sentence: the research frontier is converging on the same principles this book bets on — a 2026 proposal for an "agentic scientific operating system" independently centres staged objectives, verification checkpoints and bounded delegation; a proposal, not validated technology, but evidence the governance-first framing sits inside a wider convergence rather than against it (Zheng et al. 2026; weeks-old preprint, caveat per G2).
- **17.3** References: add Anthropic Institute (2026), METR (2026), Zheng et al. (2026).

## 6. FURTHER-READING.md

One task set, in the batch that owns the file.

- **F1 — Header.** Update the status line: drawn from the three verified reports in `/research` (name all three files); the practitioner-commentary section is governed by the video policy in `manuscript/RESEARCH-INTEGRATION-PLAN.md` §2.
- **F2 — Supersession (S1).** Replace the Lu et al. (2024) entry with Lu et al. (2026), *Nature* 651, 914–919, DOI 10.1038/s41586-026-10265-5, noting in the annotation that it is the peer-reviewed version of the 2024 "AI Scientist" preprint, with more evidence and franker limitations, and that the acceptance it reports is workshop-tier.
- **F3 — New entries**, one line of annotation each in the existing style, each with DOI/URL and the report's caveats (`[verify]` flags carried exactly):
  - Part I: Arunkumar et al. (2026); METR (2026); Anthropic Institute (2026, annotated as self-reported, single-vendor); Zheng et al. (2026, SCION, annotated as proposal).
  - Part II: Rao & Callison-Burch (2026); Wang et al. (2026, next to the Zhu 2025 entry, annotated as its automation at scale); Rafi et al. (2026); Tang et al. (2026).
  - Part III: Norman, Rivera & Hughes (2026, annotated: agreement deflation; reliability without validity); Soumik (2026, style bias and judge cost); Mehta (2026, submission vs resolution — the first direct silent-failure rates); Oh et al. (2026, agent UQ, peer-reviewed); Ansari (2026, fabrication surviving elite review).
  - Part III / Chapter 12: Five Eyes joint advisory + NCSC-UK blog (2026); NIST CAISI (2026); OWASP Top 10 for Agentic Applications for 2026 (annotated: ASI names `[verify]` against the primary document).
  - Part IV: WP-MIP (2026, annotated: design paper, no results yet); Lopez-Gomez et al. (2026); Yan et al. (2026, `[verify]` — primary page unfetched).
  - Part V: Elsevier (2026); Slimi (2026).
- **F4 — Gaps section rewrite (S5, S6).** The review-gate false-negative gap is restated as *partially closed*: the first direct measurements exist (Mehta 2026; Wang et al. 2026) but are coding-domain — no study yet measures a domain review gate on scientific artefacts, so the book's seeded-defect method remains the practitioner's answer. The NCSC/UK-guidance gap is recorded as filled (Five Eyes 2026). Remaining gaps listed: EU AI Act primary-source verification; OWASP ASI category names; a direct fetch of Yan et al.; WP-MIP's first comparative results; continued judge-bias-mitigation tracking. The existing `[AUTHOR: …]` markers in the file stay exactly where they are.
- **F5 — New closing section: "Practitioner commentary (video, grey literature)".** A short preamble stating the policy plainly (these are working practitioners' syntheses, cited in the book only as corroboration; no statistic relayed in a video is verified, and none appears in the book), then eight entries in the §2.3 format, one annotation line each: the six chapter-cited videos (Jones 17 Jun; Jones 12 Jun; Jones 19 Jul; AI Founders 17 May; Davis 20 Jun; Davis 16 May) plus two more from R-3's strongest material — Jones, "A Cursor Agent Wiped a Database in 9 Seconds…" (28 May 2026; annotated for the agent-run-as-unit-of-analysis and completion-versus-acceptance framing) and Davis, "Claude and ChatGPT Hallucinate Less. That's Why They're Dangerous." (9 May 2026; annotated for the claim-audit workflow and the "almost right" failure mode). Close the section with `[AUTHOR: confirm this curation — the full 18-video assessment is in /research; add or drop entries as you see fit.]`

## 7. Acceptance criteria (what ai-reviewer reviews each batch against)

**Global (every batch):**

1. Every new or changed citation traces to a named entry in R-1, R-2 or R-3; DOI/URL present in the chapter's references; the report's caveats and `[verify]` flags carried per G1–G2.
2. The §3 supersession actions assigned to the batch's files are all implemented, exactly (S1–S9).
3. Nothing from §4's exclusion list appears anywhere in the batch's files.
4. Video policy (§2) holds: only the named video in the named chapter; one per chapter; paraphrase, no quotation marks; no video-relayed statistic or incident; creator/channel names in references only; grey-literature format §2.3.
5. Vendor neutrality per G3, including the specified vendor-neutral aggregations of Mehta, Soumik and the Anthropic report.
6. No `[AUTHOR: …]` marker resolved, moved or deleted; no new info-boxes; `GLOSSARY.md`, `ch00`, `ch06` and all admin documents untouched.
7. Word-growth caps respected (G7); all new prose sentence-per-line, British English, v2.0 voice indistinguishable from its surroundings; no new sections or figures.
8. De-duplication discipline (G6): new evidence appears only at the placements §5 names.
9. WP-MIP and any other in-progress work cited for existence and design only (G8); the AI Scientist result always workshop-tier.

**Per chapter:** every numbered task in §5 for the batch's files is implemented as specified (task IDs are the review checklist); §6 (F1–F5) likewise for the batch owning `FURTHER-READING.md`.

**Specific spot-checks ai-reviewer must run:**

- ch11 §11.5: the "no study directly measures" sentence is gone; the replacement says the first direct measurements are appearing, cites Mehta and Wang, and the seeded-defect method and everything downstream of it is substantively unchanged.
- ch01 §1.2: the trajectory `[verify]` is resolved via S9 and no other `[verify]` or `[AUTHOR]` in the chapter has changed.
- ch08: the chapter note and every "worked design" statement stand; WP-MIP is never cited for results.
- ch12: no ASI category is named or numbered; no COSAiS specifics.
- ch13 §13.5 and ch09 §9.6: unchanged (no citation added at a non-canonical site).
- `FURTHER-READING.md`: the Lu 2024 entry no longer exists as a preprint-only entry; the gaps section matches S5/S6.

## 8. Batch structure (4 batches, disjoint files, roughly equal effort)

Batches are independent and can run in parallel; no ordering constraint.

| Batch | Files | Plan tasks | Effort notes |
|---|---|---|---|
| **R2-A — Foundations & closing frame** | `ch01`, `ch02`, `ch03`, `ch04`, `ch17` | §5 tasks 1.1–1.3, 2.1–2.3, 3.1–3.2, 4.1–4.2, 17.1–17.3; supersessions S1 (ch01 part), S9 | Five files, all light-to-medium; ch01 and ch17 share the METR/Anthropic source pair, so one writer handles both consistently. |
| **R2-B — Patterns** | `ch05`, `ch07`, `ch08`, `ch09` | §5 tasks 5.1–5.4, 7.1–7.2, 8.1–8.4, 9.1–9.3; supersessions S1 (ch09 part), S3 (ch07 part), S7 | Four files; ch08 and ch09 are the heavy ones (WP-MIP framing; policy-landscape paragraph). |
| **R2-C — Trust core** | `ch10`, `ch11`, `ch13` | §5 tasks 10.1–10.3, 11.1–11.6, 13.1–13.3; supersessions S1 (ch11 part), S2, S3 (ch11 part), S6 | Three files but the heaviest batch: the ch11 §11.5 rewrite is R2's most delicate task. |
| **R2-D — Governance, cases, adoption & back matter** | `ch12`, `ch14`, `ch15`, `ch16`, `FURTHER-READING.md` | §5 tasks 12.1–12.4, 14.1–14.2, 15.1–15.2, 16.1–16.4; §6 F1–F5; supersessions S4, S5, S8 | Five files; ch12 and the further-reading rebuild carry the weight, the rest are one-to-two-sentence tasks. |

---

*Change control: ai-editor maintains this plan; ai-writer and ai-reviewer do not edit it. Discrepancies discovered mid-batch (an anchor sentence that has moved, a placement that would break de-duplication, a cap that cannot accommodate an instruction) are flagged in the batch's PR discussion, not silently resolved.*
