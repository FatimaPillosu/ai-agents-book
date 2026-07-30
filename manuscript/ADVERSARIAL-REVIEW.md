# Adversarial review of the book's content — findings (30 Jul 2026)

**Status:** author-commissioned adversarial review of the *intellectual content* of the manuscript (not of project management, scheduling or production state).
**Scope:** the argument, the topics covered, the topics missing, and the places where the treatment should change.
**Standing:** these findings are the author's brief to the agent roster. `ADVERSARIAL-INTEGRATION-PLAN.md` (ai-editor) converts them into per-chapter instructions; ai-writer executes that plan; ai-reviewer reviews the execution.

The review was made after reading all eighteen chapter files in full. Eight substantive findings follow, each with the evidence that produced it and the change it implies.

---

## F1 — The instrument analogy breaks at non-stationarity, and the book stops one step short

**Where it lives now.** Ch. 1 §1.3 (agent as instrument: calibrate, characterise drift, quality-control); Ch. 17 §17.2 (first durable principle); Ch. 11 §11.5 (re-measurement trigger list); Ch. 12 §12.10 (one checklist line on detection, containment and reversal).

**The finding.** The book names one disanalogy between an agent and a sensor: plausible failure. There is a second and it is not named. A sensor's error is stationary and characterisable. An agent's error distribution is non-stationary, and its changes are invisible to the operator, because a hosted model can be revised without notice and the same specification can return different work on different runs.

Ch. 11 §11.5's trigger list ("after any model change") presupposes the operator knows a model changed. Frequently they will not.

**What is missing.** The concept every real instrument certificate carries: a **validity period**. An evidential tier, as the book defines it, has no shelf life. A Tier 3 claim established against a model that was revised a month later remains recorded as Tier 3, with nothing in the provenance saying the calibration behind it has expired.

**The consequence the book never reaches.** What to do about results *already published* under a gate now discovered to have been miscalibrated. Metrology has recall; science has errata; the book has neither. Governance treatments have a preventive half and a response half, and this manuscript has only the first.

**Change implied.** Introduce calibration validity and tier expiry where the tier is defined and recorded (Ch. 11, Ch. 12), and give incident response and erratum a proper treatment rather than a checklist line — for a book grounded in operational forecasting, the hour after a wrong warning is where the governance is tested.

---

## F2 — Reproducibility is absent, and it is the first hole this readership will find

**Evidence.** Across all eighteen chapter files the manuscript never uses "nondeterministic", "temperature" (in the sampling sense), "deprecated" or "retired". "Reproducib*" occurs seven times, all incidental.

**The finding.** The target readership has lived through the reproducibility crisis and has vocabulary for exactly this problem. Agentic results carry a sharper version of it than anything they have met:

- The same specification, inputs and model can produce different work on a second run. `pass^k` is cited in Ch. 11 §11.2 for reliability, and the epistemic consequence is never drawn.
- Models are withdrawn on roughly annual cycles. A methods section reading "quality-controlled under specification X by an agentic workflow" becomes un-rerunnable once the model behind it is retired. Provenance records what happened; it does not permit repetition.

**The overclaim to correct.** Ch. 12 §12.4 states that a captured audit trail makes a result "reproducible in the strong sense, not merely re-runnable but explicable". That inverts the strength ordering. Explicable is the weaker property, and it is the only one an agentic workflow delivers.

**The distinction to introduce.** Reproducibility (re-run, same answer) · replicability (independent re-do, compatible answer) · **auditability** (reconstruct and defend what was done, without being able to repeat it). Agentic work delivers the third, and the honest statement of that is a credibility gain, not a loss.

**The constructive answer already in the manuscript.** The deterministic component is the reproducible part. Ch. 6's propose–dispose and Ch. 14's deterministic core are already architectures in which the repeatable element holds the authority. The answer exists; it is not connected to the question.

---

## F3 — The book's strongest thesis is never stated

**The premises, all already in the manuscript.** Ch. 1 §1.4: the guide to safe delegation is the gap between what it costs to produce an answer and what it costs to check one, not apparent difficulty. Ch. 4 §4.3: that asymmetry, plus the cost of an uncaught error, is the decision procedure. Ch. 16 §16.3: verification is the dominant recurring cost and does not fall, because it is external to the model by design.

**The conclusion never drawn.** The class of scientific tasks where agents pay off is bounded by checking cost, which is a property of the task rather than of the model, so **that class does not grow as models improve**. Capability progress widens the generation side of the asymmetry and leaves the checking side where it was, so the frontier of safe delegation moves far less than the capability curve suggests.

**Why it matters.** It is contrarian, defensible from the book's own premises, and the opposite of what the surrounding literature implies. It also converts the book's posture from "adopt this, carefully" to "adopt this here, for these bounded reasons, and here is why the boundary will not move much" — which is more useful, more honest and more distinctive.

**Near-misses to build from.** Ch. 17 §17.3's filter ("does it move the verification burden or only the generation cost?") is one step away. Ch. 17 §17.2's fifth principle gestures at it without the economic argument.

**A test the author should apply.** Both case studies (Ch. 14, Ch. 15) appear to sit in the cheap-to-check quadrant. If so, that is not a coincidence but the thesis demonstrated, and it is currently unclaimed.

---

## F4 — The failure taxonomy stops at the single workflow

**Where it lives now.** Ch. 13's six modes: fabricated citations, silent unit errors, specification drift, over-agreeable review, context loss, confident extrapolation. Every one is a failure of one workflow producing one wrong artefact, paired with a local check.

**What is missing: failures that appear only when a field adopts the patterns.**

**(a) Correlated error across groups.** Ch. 11 §11.5 documents self-preference bias and concludes that genuine independence needs model diversity rather than a fresh context window. That conclusion is never scaled up. If most groups in a field run their independent-reviewer agent on one of a small number of base models, the field's verification errors become correlated and independent replication, science's actual error-correction mechanism, quietly stops working. This readership knows the failure under another name: correlated model error in a multi-model ensemble, where nominal spread overstates real independence. The analogy is domain-native and unused.

**(b) Homogenisation of the questions.** Ch. 8 §8.4 gates hypothesis laundering at the level of one workflow. Nothing addresses what happens to a field's distribution of hypotheses when a generation of scientists brainstorms against the same few models trained on the same corpus. Divergence of ideas is a resource; the manuscript never asks whether this technology consumes it.

**(c) Deskilling and the supply of judgement.** The manuscript never uses "deskilling", "skill atrophy", "automation bias" or "complacency". Ch. 16 §16.4 says the roles need skills "largely those a good empirical scientist already has", which assumes a continuing supply of scientists who acquired those skills by doing the work the agent now does. The verification-first stance depends on expert judgement it does not itself reproduce. Group leaders deciding what a doctoral researcher spends three years on need this addressed.

**(d) Automation bias in the human.** This is the human factor that defeats every gate in the book. Ch. 12 §12.4 concedes it in one sentence ("a rubber-stamp review leaves the same record as a searching one") and moves on. The book's model of the human throughout is a tireless, sceptical verifier; real people under deadline approve work that looks right. Ch. 13 has a mode for the *agent* being over-agreeable and none for the *person* being over-agreeable, which is the commoner failure.

---

## F5 — The tier hierarchy omits this discipline's actual gold standard

**Where it lives now.** Ch. 11 §11.2, the five tiers: execution · internal consistency · reproduction of held-out truth · out-of-sample generalisation · independent adversarial scrutiny.

**Problem one: a category mix.** Tiers 1–4 are defined by *the check* (schema, invariant, held-out data, transfer regime). Tier 5 is defined by *the checker*. That places the least reproducible and most bias-exposed instrument at the top of a hierarchy of evidential strength, in a chapter that spends two pages (§11.5) documenting judge biases.

**Problem two, the substantive one: there is no tier for corroboration by an independent method.** That is how the environmental sciences establish most of what they believe: satellite against gauge, two retrievals with different error structures, a physical model against an empirical one. The book uses independent-method corroboration as its own strongest evidential move twice — Ch. 11 §11.3's operational re-verification of a data-driven weather model, and Ch. 1 §1.2's two independent measurements converging on the same doubling trend — and it is not on the ladder.

**Change implied.** Add independent-method corroboration as a tier; it sits above reproduction of held-out truth and is more reproducible than adversarial review. Separate check-properties from checker-properties while revising.

---

## F6 — Propose–dispose is the book's unifying architecture, filed as a Chapter 6 pattern

**The finding.** "Agents propose, deterministic rules dispose" (Ch. 6 §6.3) is the strongest idea in the manuscript: domain-native, memorable, transferable. The same idea recurs in four further costumes without being named as one thing:

- Ch. 8 §8.3, the monitor-and-log boundary (the agent orchestrates and records, the scientist decides).
- Ch. 9 §9.3, assembly under author control (the agent proposes, the author gates).
- Ch. 12 §12.8, the trust boundary (the agent may propose a consequential action, a human passes it).
- Ch. 14, the deterministic core with an advisory tier above it.

**Change implied.** Name the principle once, early — Part I, at or near Ch. 2 or Ch. 4 — so the reader carries away one architectural principle rather than five local patterns, and let the later chapters be instances of it rather than independent derivations. This also shortens the book, because several chapters are currently re-deriving a principle that was never stated in general form.

---

## F7 — The specification thesis governs the routine half of science, and concedes it in three sentences

**Where it lives now.** Ch. 3 §3.6 concedes that for genuinely exploratory work, insisting on a specification prematurely is its own error, then hands off to Ch. 4.

**The finding.** The concession is larger than the space it is given. Every worked example in the book is routine or semi-routine work: quality-control passes, verification scores, calibration bookkeeping, manuscript assembly, reviewer responses. Much of the best environmental science is abductive and opportunistic — something odd in a record, followed up. A governance regime that only bites once acceptance criteria can be written governs the well-understood half of the work and leaves the frontier half ungoverned, which is the inverse of where the risk sits.

**Position taken.** This is not fatal and it does not call for retreat. Read honestly, the book is a governance treatment for the routine and semi-routine work surrounding science, which is a valuable and defensible thing to be. But it currently presents as a treatment of *doing science* with agents, and the gap will be noticed. The remedy is an explicit, unapologetic statement of scope, plus honest treatment of what governs exploratory work when a specification cannot yet be written.

---

## F8 — There is nothing in the book for the reader on the receiving end

**The finding.** The reader is assumed throughout to be the accountable principal: the person who designs the workflow, sets the gates and owns the specification. Ch. 16's four roles all presume the authority to define them.

Most readers will soon be in a different position: handed an agentic system by an institution, reviewing a manuscript someone else produced with agents, inheriting a pipeline whose specifications they did not write, or receiving a vendor product with agentic components inside it.

**The sharpest instance.** "Peer review" occurs eleven times in the manuscript, entirely as *policy on whether the reader may use AI while reviewing*. Nowhere does the book address how to review a manuscript that was produced with agents: what to ask for, what a disclosure statement should have let a reviewer check, which of the six failure modes are detectable from outside, what provenance a reviewer is entitled to demand.

**Why this is the highest-leverage gap.** Reviewing is the one agentic-adjacent task every reader already performs; it is where the community's error correction actually happens; and the book's apparatus is unusually well suited to it, since the registries and coverage records of Ch. 12 are exactly what a reviewer should be asking to see.

---

## F9 (secondary) — The energy section does not count induced demand

**Where it lives now.** Ch. 16 §16.6. The section is careful, counts displaced computation, and refuses a headline figure. Both are right.

**What is missing.** Induced demand: the workflows that exist only because agents made them cheap, the sweeps run because running them costs little, the loops that produce nothing. The last is named in passing as a thing to avoid and never treated as an economic mechanism. This is the first objection a climate-literate reader will raise, and omitting it will read as evasion to precisely the audience the book is written for.

---

## Priority

Substantive, requiring new argument: **F2, F3, F4, F8**.
Repositioning of material the manuscript already holds: **F1, F5, F6, F7, F9**.

F3 and F6 both shorten the book.

## Standing constraints on any work arising

All existing project rules bind this work without exception:

- `STYLE.md` v5.0 (colloquial register) and `FIGURES.md` govern every word and every figure, including captions and alt-text.
- Citations only from verified reports in `/research`. A claim needing a citation no report covers keeps `[verify]` rather than acquiring an unverified reference. Nothing is ever fabricated.
- `[AUTHOR: …]` markers are never resolved; new ones are added wherever lived material is needed.
- Budgets are indicative. F3 and F6 are expected to reduce length; no finding licenses bloat.
- British English throughout.
