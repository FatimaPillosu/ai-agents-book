# Agentic AI for Environmental Science — Working Outline (v0.5)

**Format:** single e-book volume, target ≈150 pages · **Audience:** environmental and geoscientists · **Date:** 24 July 2026

**Changes from v0.4:** all 17 chapters now drafted first-pass; **revision pass R1 under way**, governed by `manuscript/REVISION-PLAN.md` (STYLE.md v2.0 revoicing of every chapter, de-duplication to canonical homes, Ch. 11 rebuild, front matter and glossary, mechanical fixes). Chapter anatomy rescoped: the full template binds **Part II only**, while Ch. 11 and Ch. 12 each still carry a verification checklist and a repository pointer (§6). Ch. 11 synopsis extended to cover building a task-grounded evaluation set and measuring the gates themselves (§7). Ch. 13 now specifies six annotated failure traces, one per failure mode (§7). References policy decided: citations only from the verified `/research` reports; annotated further reading in the back matter (§9). Overall length reduction deferred; companion-repository build-out parked until the book is finalised (§9).

**Changes from v0.3:** budgets restated as indicative guidance rather than fixed targets; build toolchain deferred (manuscript is plain Markdown; no layout, licence or DOI fixed yet — these are decisions for later, not open gates); figures now governed by `FIGURES.md` (house infographic style, generated from figure briefs) in place of diagrams-as-code; the abstract "zero-budget path" removed as a standalone open question — low-resource and open-weight working is addressed concretely in Ch. 14 and Ch. 16; internal count of Part II corrected (five core patterns plus a composing capstone); vendor-neutral naming promoted to decided; pre-flight process items set aside as not-yet-needed; working title remains open.

---

## 1. Concept and contribution

A pattern-based, visually driven treatment of agentic AI for working environmental and geoscientists, organised around durable workflow patterns rather than named tools, with perishable material held in a versioned companion repository. Every core chapter follows an identical anatomy and is grounded in executed operational work. Governing stance: agents are instruments requiring specification, calibration, verification and audit, as any other instrument in the environmental sciences.

**Contribution statement (for the preface).** Existing book-length treatments of agentic AI address engineers building production systems or business audiences; science-facing material remains survey and perspective literature; work at the environmental intersection frames agentic AI as autonomous management technology rather than research instrumentation. This book's claim: a practical, governance-first, diagram-led treatment for practising environmental researchers, grounded in executed case studies. (Positioning rests on a limited scan, Jul 2026 — repeat systematically before release.)

**Domain framing (for the preface).** Worked examples are drawn from operational hydrology and meteorology; patterns are written to transfer across the environmental sciences. Stated plainly rather than padded with thin borrowed examples.

**Working title:** open — undecided. Placeholder candidates on record (not chosen): *Agents in the Field*; *The Governed Agent*; *Patterns of Practice* — each with the subtitle *Agentic AI for Environmental Science(-tists)*.

## 2. Publication and release model

- **Self-published and free**, released via LinkedIn as the first readership; the aim is credibility on agentic-AI work, not revenue. **[DECIDED]**
- **Canonical copy lives in the unified GitHub repository** (full Markdown source, and whatever release artefact is later chosen); a LinkedIn newsletter announces and excerpts each release. **[DECIDED]**
- **Living-book releases**: versioned (v1.0, v1.1, …), each a full rebuild.
- **Licence, DOI and release-artefact format**: deferred — to be decided later, not gates on drafting.

## 3. Production approach

- **Source format**: chapters as plain-text Markdown under Git (`ch01`–`ch17`). No build system, layout or output format is fixed yet; these are deferred decisions. Drafting proceeds in Markdown only.
- **Unified repository**: manuscript source and companion materials in one repo (layout in §8).
- **Runnable examples**: cited code examples are kept runnable; the mechanism for checking them (continuous integration, release tagging) is deferred until the manuscript is further advanced.
- **Figures**: governed by `FIGURES.md` — one house infographic style, each figure specified as a brief and generated in the shared, colour-vision-safe (Okabe–Ito) style; alt-text written at the moment each brief is created; meaning never encoded by colour alone.
- **Reflexive production**: the book is written under the governance protocol it describes, with the audit trail disclosed in the preface. **[Principle; mechanism deferred.]**

## 4. Reader profile and prerequisites

Practising environmental and geoscientists comfortable with Python and the command line; no machine-learning expertise assumed. Explicit non-targets: ML researchers seeking novel methods; managers seeking pure strategy (Part V skimmable for them). Readers without paid model access are not left behind: low-compute and open-weight working is treated concretely where it belongs — the constrained toolkit of Ch. 14 and the cost model of Ch. 16 — rather than as a separate track.

## 5. Budgets (indicative guidance, not targets)

These figures orient effort and proportion; they are guidance, and a chapter may run over or under where the material justifies it.

| Item | Indicative | Confidence |
|---|---|---|
| Words | ≈38,000–42,000 | Moderate |
| Figures | ≈65–75 | Moderate |
| Focused effort | recalibrate against drafted chapters | Low–moderate |

Per-chapter page figures in §7 are indicative allocations, useful for balance, not limits to defend line by line.

## 6. Chapter anatomy and visual grammar

**Anatomy (repeated template, Part II):** problem → conventional workflow → agentic redesign → worked example → failure modes → verification checklist → repository pointer (runnable example and optional exercises). The full anatomy binds Part II (Ch. 5–10) only. Part III chapters follow their own structure, but **Ch. 11 and Ch. 12 each still carry a verification checklist and a repository pointer**; Ch. 13 is organised as failure–check pairs and is exempt. All verification checklists follow the standard bulleted, printable format defined in `REVISION-PLAN.md` §2.

**Visual grammar:** governed by `FIGURES.md`. Fixed iconography (human · agent · tool · data store · gate · reviewer) with one icon-key figure in the front matter; five canonical figure types — architecture, sequence, decision flowchart, before/after workflow, annotated failure trace; every figure described as a brief and rendered in the shared house style. Standard set per pattern chapter: one architecture, one sequence, one before/after, one or two example figures.

## 7. Structure and chapter synopses

**Front matter (≈5 pp).** How to read this book; what you need; icon key; contribution statement; domain framing; disclosure statement (how agents were used to produce the book).

### Part I — Foundations (≈27 pp)

**Ch. 1 — Why agents, why now (≈6 pp).** What changed and when; LLMs vs AI agents vs agentic workflows; an honest capability boundary. Figures: capability timeline; taxonomy.

**Ch. 2 — Anatomy of an agent (≈8 pp).** The plan–act–observe loop; tools; context and memory; orchestration; cost-model basics. Figures: canonical loop; context schematic; annotated tool-call sequence.

**Ch. 3 — Specifying work for agents (≈7 pp).** The skill most failures trace back to: decomposing a scientific task; writing a specification an agent can execute and a human can audit — objective, inputs, acceptance criteria, stop conditions; a workflow-agnostic specification schema; the specification as the primary human control surface; anti-pattern: conversational drift in place of specification. Worked example: turning "verify this rainfall forecast" into an executable, auditable specification. Figures: specification anatomy; weak-spec/strong-spec before/after.

**Ch. 4 — The scientist's stance (≈6 pp).** Where agents fit the scientific method; augmentation versus automation; when *not* to use an agent. Figure: "should an agent do this?" decision flowchart.

### Part II — Core patterns (≈53 pp; template anatomy throughout)

Five core patterns spanning the research lifecycle (Ch. 5–9), then a capstone that composes them (Ch. 10).

**Ch. 5 — Evidence and literature synthesis (≈8 pp).** Retrieval-grounded synthesis; citation verification; interpretive control stays human. Worked example: a frontier synthesis of the agentic-AI-in-hydrology literature.

**Ch. 6 — Data acquisition and quality control (≈9 pp).** Agents on messy environmental observations: format wrangling, gap and spike flagging, provenance capture; agents propose, QC rules dispose. Worked example: river-gauge and rainfall QC.

**Ch. 7 — Coding and pipeline agents (≈9 pp).** From exploratory notebook to governed pipeline; tests and hooks as guardrails; an independent reviewer agent before any human code review. Worked example: implementing a governed workflow with hooks and sub-agents.

**Ch. 8 — Model orchestration and experimentation (≈9 pp).** Calibration campaigns, ensembles, structured intercomparison; agents that monitor and log rather than decide; LLM-assisted hypothesis generation, explicitly flagged as exploratory. Worked example: designing a three-track (physics / data-driven / hybrid) intercomparison (a worked design, not an executed case study).

**Ch. 9 — From results to manuscript (≈9 pp).** The output side of scholarship: drafting under author control; figures and tables generated from pipeline artefacts; reviewer-response workflows; documentation and reporting. Journal and funder policy on AI use, disclosure and authorship treated as a volatile landscape — survey by policy class in print, current specifics in the repository; agents are never authors. Provenance records (Ch. 12) feed the disclosure statement. Failure modes: fabricated citations, style laundering, over-claiming. Worked example: a reviewer-response workflow with the human as sole interpretive authority. Figures: manuscript pipeline architecture; disclosure decision flowchart.

**Ch. 10 — Multi-agent workflows (≈9 pp).** Capstone that composes the preceding patterns: roles and rosters; independent reviewers; human gates; when multiple agents add robustness versus only noise and cost. Worked example: deriving an agent roster from a workflow specification (bridges to Ch. 15).

### Part III — Trust (≈29 pp)

**Ch. 11 — Verification and evaluation (≈9 pp).** Task-grounded evaluation over leaderboard benchmarks; a five-tier evidential hierarchy for workflow claims (after Klemeš; Refsgaard & Henriksen; Jakeman et al.; Oberkampf & Trucano) adapted to agentic outputs; building a task-grounded evaluation set from one's own workflow; measuring the gates themselves — false-negative rates by seeded-defect testing, and the yield diagnostic (delivers the measurement material promised by Ch. 5 §5.7 and Ch. 10). Worked example: an evaluation set and gate measurement from the author's own practice. Verification checklist and repository pointer per §6.

**Ch. 12 — Provenance, governance and security (≈10 pp).** Assumption and uncertainty registries; audit trails; reviewer-coverage records; documentation that survives staff turnover. Security section: prompt injection; credential and data handling when agents touch institutional systems and HPC; least-privilege tool access; what institutional IT will ask.

**Ch. 13 — The failure gallery (≈10 pp).** A taxonomy with real, anonymised examples: fabricated citations, silent unit errors, specification drift, over-agreeable review, context loss, confident extrapolation — each paired with the check that catches it. The gallery is the canonical home for the anatomy of each failure mode; pattern chapters cross-reference it rather than re-describing. Figures: six annotated failure traces, one per failure mode (the fifth canonical type).

### Part IV — Case studies (≈20 pp)

**Ch. 14 — Verification under constraint (≈10 pp).** An AI-assisted rainfall-verification toolkit for partners who cannot share observations: data sovereignty, low compute, open-weight models; three-tier design (deterministic core, optional local tutoring tier, team-side escalation); doubling as a teaching tool.

**Ch. 15 — Governing a modelling workflow end to end (≈10 pp).** A research protocol applied in full: specification schema (Ch. 3) → agent-roster derivation (Ch. 10) → gates and registries → independent review → publication run.

### Part V — Adoption (≈13 pp)

**Ch. 16 — Starting in your own group (≈8 pp).** A 30-day on-ramp (capability-based, not tool-based); a realistic cost model; skills and roles; institutional, ethical and data-sovereignty considerations. Section: the energy and carbon cost of inference — addressed honestly for an environmental readership; volatile figures live in the repository, the reasoning lives in print.

**Ch. 17 — What will last (≈5 pp).** Durable principles versus tooling churn; staying current without chasing releases; the repository as the living layer.

**Back matter (≈3 pp).** Glossary; annotated further reading; repository guide.

**Page check (indicative):** 5 + 27 + 53 + 29 + 20 + 13 + 3 = 150.

## 8. Unified repository (sketch)

`/manuscript` (Markdown source; `OUTLINE.md`; `ch01`–`ch17`) · `/patterns` (runnable minimal examples per chapter) · `/prompts` · `/figures-source` (figure briefs + alt-text) · `/checklists` (printable) · `/case-studies` (sanitised configurations) · `/exercises` (per-chapter "try this" sets). Releases versioned by tags and history.

## 9. Status and decisions

**Status:** all 17 chapters drafted first-pass. Revision pass R1 under way per `REVISION-PLAN.md`: STYLE.md v2.0 revoicing throughout, de-duplication to canonical homes, Ch. 11 rebuild, front matter (`ch00`) and glossary expansion, standard checklists and status headers, mechanical fixes (Ch. 8 figure renumbering; Ch. 13 sixth failure trace; checklists and repository pointers for Ch. 11 and Ch. 12).
<!-- [ai-reviewer: this status line (and the v0.5 change note above) is stale — R1 is complete and closed, and research-integration pass R2 (`RESEARCH-INTEGRATION-PLAN.md`) has been executed; CLAUDE.md's "Current state" says so. The outline is the document declared authoritative, so a future agent reading only this file would plan against the wrong project state. ai-editor to refresh §9 and the header change-note.] -->

**Decided:** single ≈150-page volume · audience environmental/geosciences · self-published, free, LinkedIn-first · unified GitHub repository with newsletter as update channel · no formal index (hyperlinked ToC deferred to any build stage) · specification (Ch. 3) and manuscripts (Ch. 9) chapters in · exercises to the repository, not the page budget · cross-domain examples deferred to a second edition · manuscript written in plain Markdown · budgets are indicative guidance · vendor-neutral naming in print · figures governed by `FIGURES.md` in the house infographic style · STYLE.md v2.0 voice retroactive across all chapters (24 Jul 2026) · de-duplication now — one canonical home per recurring idea, short cross-references elsewhere (24 Jul 2026) · references policy — key claims cited from verified sources in the `/research` reports (DOI/URL per source), annotated further reading in the back matter, no citation from agent memory (24 Jul 2026) · full chapter anatomy binds Part II only, Ch. 11 and Ch. 12 still owing verification checklists and repository pointers (24 Jul 2026).

**Deferred (decide later; not gates):** output/layout format and any build toolchain · licence · DOI/Zenodo · continuous-integration mechanism for runnable examples · the reflexive-production audit-trail mechanism · positioning re-scan, beta readers and release-channel limit checks (revisit nearer release) · overall length reduction — current length stands; a future pass will consider cuts (24 Jul 2026).

**Open:** working title.

**Parked (author's direction; on record, not a gate):** permissions/IP for case studies and failure-gallery examples · companion-repository build-out — out of scope for revision pass R1; to be sorted when the book is finalised (24 Jul 2026).

## 10. Deferred to a second edition

Cross-domain worked examples (ecology, oceanography) · the digital-twin case study once executed · a reflowable edition · formal index.
