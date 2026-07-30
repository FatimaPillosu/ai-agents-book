# Chapter 14 — Verification under constraint

> **Status:** draft r6 · voice v5.0 (`STYLE.md` §1) · sentence-per-line per `STYLE.md` §10 · figures as briefs per `FIGURES.md`.
> **Conventions:** vendor-neutral (outline §9) · **[AUTHOR: …]** marks lived material only the author can supply · **[verify]** marks real but unconfirmed details · citations drawn only from verified reports in `/research`. Nothing has been invented.
> This chapter reports executed operational work; concrete partner details, datasets, metrics, hardware, results and outcomes are the author's lived material and are tagged **[AUTHOR: …]**.

---

## 14.1 The setting: verification that cannot see the observations

This case study is an ordinary problem made difficult by one constraint that reshapes everything after it: the observations a rainfall forecast has to be judged against cannot leave the institution that holds them.

Mechanically, rainfall verification is among the better-understood tasks in operational meteorology.
Compare a forecast field against gauge or radar observations, and a set of scores summarises how well the two agree over some period and area.
The difficulty is not the arithmetic but the data policy around it, because the partner organisations whose forecasts most need independent verification are often the ones least able to release their observational record.
This matters more, not less, as forecasting itself moves towards data-driven methods: machine-learning weather models crossed the credibility threshold in 2022–23 and, by early 2025, an operational centre was running one on duty alongside its physics-based system, verified in operational-like conditions before it was trusted (Lam et al., 2023; Bi et al., 2023; Lang et al., 2024).
National meteorological and hydrological services in many jurisdictions hold rain-gauge data under licences, memoranda or national regulations that prohibit its transfer to an external party, and the reasons are legitimate rather than obstructive: gauge networks are sometimes commercially licensed, sometimes bound by bilateral agreements, and sometimes protected as a matter of national sovereignty over environmental data **[AUTHOR: state the specific data-sovereignty basis for the partner(s) in this case — e.g. national data policy, commercial licensing of the gauge network, a WMO data-exchange category — and the region or programme this work served]**.
The consequence is a standing asymmetry: the expertise, the reference forecasts and the verification methodology sit on one side, and the observations that would exercise them sit on the other, behind a boundary that cannot be crossed by moving the data.

> **Definition — Data sovereignty.** The principle that a dataset stays under the legal and
> physical control of the institution or nation that holds it, so that where the data lives, and
> who may move it, are governed by that holder's rules rather than by whoever wants to use it.
> For observational records it often means the numbers may be worked on, but not taken away.

The conventional answer is to move the data anyway, under a data-sharing agreement negotiated case by case, and it fails often enough in practice to be worth designing around rather than depending on.
Negotiating egress for a research observation set can take months, binds both parties to terms that constrain reuse, and frequently ends without agreement, because the holding institution cannot accept the residual risk of releasing a record it is obliged to protect **[AUTHOR: the specific negotiation history or timeline that motivated the constrained approach — how long an egress route was attempted, and why it was set aside]**.
So the design here reverses the usual direction of movement.
Instead of bringing the observations to the verification tools, it brings the verification tools to the observations, packaged to run entirely inside the partner's own environment and to emit only what the partner chooses to share, which is typically aggregate scores and never the underlying records.
That reversal is the organising decision of the whole toolkit.
The three constraints it has to satisfy, meaning no data egress, minimal compute and no recurring budget, are the next section, because each of them independently pushes the design towards the same three-tier shape.

## 14.2 Three constraints that determine the architecture

The architecture is not a free design choice.
It follows fairly directly from three constraints, each of which on its own rules out a large part of the conventional solution space, and which together leave only a narrow set of workable designs.

The first is that no observational data may leave the partner's environment.
That rules out every approach relying on a hosted service, a cloud-based model endpoint or any tool that sends inputs off-site for processing (high confidence; this is a hard requirement, not a preference).
The practical force of this constraint is easily underestimated: it excludes not only the obvious case of uploading gauge records to an external analysis platform, but also the subtler case of sending observation-derived text (an error summary, a flagged station list, a data excerpt) to a model accessed over a network, because such text can carry exactly the information the data policy protects.
Anything that reasons over the observations must therefore execute locally, within the trust boundary the partner already controls, and this single requirement is what forces the language-model component, where it exists at all, to be an open-weight model running on the partner's own hardware rather than a hosted one (which connects directly to the least-privilege and data-handling arguments of Chapter 12).

> **Definition — Open-weight model.** A language model whose trained parameters (its "weights")
> are published, so that it can be downloaded and run on local hardware, inside an institution's
> own network, with nothing sent to an outside service. This is the opposite of a hosted model,
> which is reachable only by sending the input over the network to another party's computer.

The same two conclusions circulate independently in practitioner commentary: telling a cloud model not to read or transmit something is a behavioural safeguard that can be silently violated, so only an architectural boundary (no network path) is reliable, and an offline local model that triages material into risk tiers before anything external is contacted is exactly this toolkit's tiered pattern (practitioner commentary; see the references).

The second constraint is minimal compute, because the partner environments in view here are not equipped with the accelerators or the memory that a large hosted model assumes, and a toolkit that demands them would simply not run where it is needed **[AUTHOR: specify the representative hardware the toolkit was required to run on — CPU-only versus a single consumer GPU, approximate memory, whether an internet connection was available at all]**.
The third constraint is the absence of any recurring budget: the toolkit had to keep working after the project that funded its construction ended, without per-query charges, subscription renewals or licence fees that a partner with no dedicated software budget could not sustain (moderate-to-high confidence that this is decisive for adoption; the cost reasoning is developed in Chapter 16).
All three constraints point at the same conclusion.
A verification result partners will trust and report has to be exact, reproducible, and free of any dependence on a fallible or metered external service.
Anything that merely explains, teaches or guides is valuable, but it must never be allowed to alter that result, and it must degrade gracefully to nothing when the compute to run it is unavailable.
That separation, an exact core that always runs and an optional advisory layer that sometimes runs and never decides, is where the three tiers divide, and the next three sections take each in turn.

**Figure 14.1 — The three-tier toolkit under constraint.**

![A large trust boundary labelled partner environment encloses most of the canvas, annotated no observational data egress. Inside it, observations that never leave feed a deterministic verification core, annotated same inputs, same numbers, every time, which produces scores for a human review step. A local tutoring tier drawn with a dashed border connects to the scores by a two-way explains-and-guides link, annotated open-weight, runs on the partner's own hardware, and carries a no-decision tag and the note that it degrades to nothing if the compute is unavailable. The only arrow crossing the boundary carries aggregate scores and questions to the team for escalation, annotated the one thing that crosses, and never the records. A footer reads exact where evidence must be defensible, advisory where a mistake is recoverable, human where judgement is irreducible.](../figures/figure-14-1.svg)

*Figure 14.1 — The whole toolkit lives inside the partner's boundary. The deterministic core always runs and produces the same defensible numbers from the same inputs; the tutoring tier is optional, local, and allowed only to explain; and the single arrow that crosses the boundary carries aggregate scores and a question, never the observations. Three constraints forced this shape, and it is the shape governance would have chosen anyway. (Rendered as `figures/figure-14-1.svg` from the brief below, per `FIGURES.md`.)*

```
FIGURE BRIEF
- id:            Figure 14.1
- title:         Three tiers inside one trust boundary
- type:          architecture
- claim:         The constraints (no data egress, minimal compute, no recurring budget) force a design in which an exact deterministic core always runs, an optional local tutoring tier only explains, and only aggregate scores ever cross the boundary.
- standfirst:    Exact where it must be defensible; advisory where a mistake is recoverable; human where judgement is irreducible.
- canvas:        16:9
- elements:      a large grey-bordered rounded rectangle "partner environment (trust
                 boundary)"; inside, a sky-blue cylinder "observations (never leave)"; a
                 green-bordered box "deterministic verification core" with a "scores"
                 artefact; an orange dashed-border box "local tutoring tier — open-weight
                 model" tagged "optional" and "no decision"; a blue "human review" icon;
                 one arrow crossing the boundary to "team (escalation)" carrying
                 "aggregate scores + questions only"
- flow:          left-to-right inside the boundary: observations → core → scores → human
                 review; the tutoring tier links to the scores with a dashed two-way
                 "explains / guides" arrow; a single arrow exits the boundary to the team
- labels:        "partner environment (trust boundary)", "observations (never leave)",
                 "deterministic verification core", "scores",
                 "local tutoring tier — open-weight model", "optional",
                 "explains / guides", "no decision", "human review",
                 "aggregate scores + questions only", "team (escalation)"
- annotations:   on the boundary, "no observational data egress"; on the core, "same
                 inputs, same numbers, every time — reportable as an official figure"; on
                 the tutoring tier, "open-weight, on the partner's own hardware; degrades
                 to nothing if the compute is unavailable"; on the crossing arrow, "the
                 one thing that crosses — and never the records"; a footer, "exact where
                 evidence must be defensible · advisory where a mistake is recoverable ·
                 human where judgement is irreducible"
- caption:       Figure 14.1 — The whole toolkit lives inside the partner's boundary. The deterministic core always runs and produces the same defensible numbers from the same inputs; the tutoring tier is optional, local, and allowed only to explain; and the single arrow that crosses the boundary carries aggregate scores and a question, never the observations. Three constraints forced this shape, and it is the shape governance would have chosen anyway.
- alt-text:      A large trust boundary labelled partner environment encloses most of the canvas, annotated no observational data egress. Inside it, observations that never leave feed a deterministic verification core, annotated same inputs, same numbers, every time, which produces scores for a human review step. A local tutoring tier drawn with a dashed border connects to the scores by a two-way explains-and-guides link, annotated open-weight, runs on the partner's own hardware, and carries a no-decision tag and the note that it degrades to nothing if the compute is unavailable. The only arrow crossing the boundary carries aggregate scores and questions to the team for escalation, annotated the one thing that crosses, and never the records. A footer reads exact where evidence must be defensible, advisory where a mistake is recoverable, human where judgement is irreducible.
- infographic description: A flat vector architecture diagram, 16:9, off-white
                 background. Title top-left: "Three tiers inside one trust boundary".
                 Standfirst: "Exact where it must be defensible; advisory where a mistake
                 is recoverable; human where judgement is irreducible." A large
                 grey-bordered rounded rectangle "partner environment (trust boundary)"
                 fills most of the canvas, its border annotated "no observational data
                 egress". Inside, left to right: a sky-blue cylinder "observations (never
                 leave)"; a green-bordered box "deterministic verification core"
                 annotated "same inputs, same numbers, every time — reportable as an
                 official figure", producing a small card "scores"; a blue human icon
                 "human review". Above the scores, an orange dashed-border box "local
                 tutoring tier — open-weight model" tagged "optional" and "no decision",
                 joined to the scores by a dashed two-way arrow "explains / guides", and
                 annotated "open-weight, on the partner's own hardware; degrades to
                 nothing if the compute is unavailable". One arrow exits the boundary on
                 the right, labelled "aggregate scores + questions only" and annotated
                 "the one thing that crosses — and never the records", reaching a box
                 "team (escalation)". Footer: "exact where evidence must be defensible ·
                 advisory where a mistake is recoverable · human where judgement is
                 irreducible". Sentence case throughout.
```

## 14.3 The deterministic core: verification that never guesses

The foundation is a deterministic verification core that computes standard rainfall-verification scores by fixed algorithms, producing the same numbers from the same inputs every time it runs.
That determinism is a deliberate design commitment, not an implementation detail.
Rainfall forecasts are verified with a well-established and stable set of measures, and the core implements the subset appropriate to the partner's forecasts and decisions: for categorical forecasts of exceedance above a threshold, the contingency-table scores — probability of detection, false-alarm ratio, frequency bias and a threat or equitable-threat score; for continuous fields, mean error, mean absolute error and root-mean-square error; and, where the forecast is probabilistic or ensemble-based, reliability and a proper score such as the Brier score or the continuous ranked probability score, together with the spatial measures (neighbourhood or fractions-based) that avoid the double-penalty problem of point matching **[AUTHOR: state which scores the toolkit actually computes for this partner, the exceedance thresholds and accumulation periods used, and why those were the operationally relevant choices]** [verify: standard references for these scores, e.g. Jolliffe & Stephenson; Wilks — confirm editions before release].
None of these measures involves a language model, a learned component or any stochastic element; each is a closed-form calculation over the matched forecast–observation pairs, and this is exactly what allows a partner to report the output as an official figure and to reproduce it independently.

Why hold verification deterministic while allowing a language model elsewhere in the toolkit?
A verification result is a measurement, and a measurement whose value could change because a generative model produced something slightly different this time is not a measurement at all.
The evidential weight a verification score has to carry (informing whether a forecast system is fit for issuing warnings, or whether one configuration outperforms another) depends on the score being a fixed function of the data, auditable line by line and defensible to a regulator or a sceptical colleague who re-runs it (high confidence).
This is exactly the discipline the meteorological community has applied to the new data-driven models themselves: when an operational centre assessed a machine-learning forecast model, it did so in an operational-like context, initialised from operational analyses, verified against both analyses and station observations with its own standard metrics, and reported the model's genuine strengths alongside documented weaknesses such as smoothing and the underestimation of some extremes (Ben Bouallègue et al., 2024).
Checking one determination against two reference sources is a reach for Tier 5 of Chapter 11 §11.2, independent-method corroboration, and it is the strongest evidential move this chapter makes.
It is also a partial one, and the reason is worth stating rather than skipping past.
An operational analysis is produced by assimilating station observations, so the two references are not unrelated.
What differs is what each one carries.
An analysis is a physically constrained field with the assimilating model's structure inside it, and a station report is a point measurement with no model at all.
An error the assimilating model shares with the forecast can hide in the analysis and still show against the stations.
So this is a corroboration weakened by a named dependency rather than a clean one (moderate confidence; argued here from how assimilation works rather than from a measurement).
Naming the dependency is what Chapter 11 §11.2 asks of every Tier 5 claim, and this is what doing it looks like.

Holding the model out of the scoring path is the propose–dispose separation of Chapter 2 §2.6, with a deterministic rule disposing.
It is also Chapter 11 §11.3's rule that a check sits outside what it checks.
The deterministic core is the reproducible part of this toolkit, in the strict sense of Chapter 12 §12.4, which separates reproducing a result from auditing one.
The tutoring tier is not.
So the toolkit spends its language-model budget only on what the core cannot do: explaining what the numbers mean, and helping a non-specialist act on them correctly.
That boundary is the toolkit's most important design line: no output of the tutoring tier reaches a reported score without passing back through the deterministic core.

## 14.4 The tutoring tier: an open-weight model that explains but does not decide

The optional middle tier is a local, open-weight language model whose whole job is to explain the verification output and guide the user's next action.
Its defining constraint is negative: it computes no score, alters no score, and produces nothing that gets reported as a result.
The reason to include a language model at all in a verification toolkit is that the users are frequently not verification specialists, and a table of contingency scores is opaque to someone who has not internalised what a false-alarm ratio of 0.4 alongside a probability of detection of 0.9 actually implies for their forecast **[AUTHOR: characterise the intended users — forecasters, hydrologists, technicians — and their prior familiarity with verification scores]**.
The tutoring tier reads the scores the core has already computed, together with the fixed definitions of those scores, and produces plain-language explanation: what each number means, which scores are in tension, what a plausible next diagnostic step would be, and what the result does not license the user to conclude.
Running an open-weight model locally is what makes this admissible under the first constraint, because the model never transmits anything off-site; it also makes the tier free to run under the third constraint, since an open-weight model on the partner's own hardware carries no per-query charge (moderate confidence that a model small enough for the target hardware is nonetheless competent at this bounded explanatory task, the kind of claim that must be re-tested per model, and the energy cost of local inference is treated in Chapter 16) **[AUTHOR: name the capability class and approximate parameter scale of the open-weight model used, the year, and the observed quality of its explanations on real cases — including any cases where its explanation was wrong and how that was caught]**.

The safeguard that keeps the tutoring tier from quietly becoming a decision-maker is architectural rather than merely cautionary, and it matters because an advisory component that users come to trust will be treated as authoritative whatever its label says.
The tier is given read-only access to the core's outputs and the score definitions, and no path by which its text can be written back into the record of results; a user who follows its suggestion to compute an additional score does so by invoking the deterministic core again, not by accepting a number the model has produced.
That is the propose–dispose separation of Chapter 2 §2.6 again, with least privilege at the tools as Chapter 12 §12.8 draws the trust boundary.

The residual risk is that a fluent but mistaken explanation misleads a non-specialist into a poor interpretation, and this risk is real and cannot be designed away entirely; it is mitigated by keeping the tier's outputs explanatory rather than prescriptive, by having it cite the fixed score definitions it reasons from, and by the escalation route that exists precisely for the cases where explanation is not enough.
The interaction between a user, the deterministic core and the tutoring tier, with decision authority remaining with the human throughout, is the subject of the sequence in Figure 14.2.

**Figure 14.2 — A verification-plus-tutoring interaction.**

![A sequence diagram with three lanes, a user, the deterministic core and a tutoring tier drawn with a dashed header to mark it optional, plus a footer note that the observations stay local throughout. Eight numbered steps: the user requests verification; the core computes the scores exactly; the scores return; the user asks what the result means; the tutoring tier explains without deciding, annotated it reads the scores and writes nothing to the record; the user asks for a further diagnostic; the core recomputes exactly, annotated that a suggestion from the tutor is always executed by the core, never accepted as a number from the model; and the user decides and records, outlined in vermillion and annotated decision authority stays human.](../figures/figure-14-2.svg)

*Figure 14.2 — Who computes, who explains, who decides. Every number in the exchange comes from the deterministic core, including the follow-up the tutor suggested; the tutoring tier reads scores and writes nothing to the record; and the final step, deciding and recording, is outlined in vermillion because it belongs to the person throughout. (Rendered as `figures/figure-14-2.svg` from the brief below, per `FIGURES.md`.)*

```
FIGURE BRIEF
- id:            Figure 14.2
- title:         Who computes, who explains, who decides
- type:          sequence
- claim:         In a single interaction the deterministic core computes the scores, the tutoring tier only explains them, and the human holds decision authority throughout; the model never produces a reported number.
- standfirst:    Every number comes from the core. Every decision stays with the person.
- canvas:        16:9
- elements:      three lanes read top-to-bottom — a blue "user" lane; a green
                 "deterministic core" lane; an orange "tutoring tier (optional)" lane with
                 a dashed header; a vermillion outline on the closing decision step
- flow:          numbered steps downward: 1 user requests verification; 2 core computes
                 scores exactly; 3 scores returned; 4 user asks what it means; 5 tutor
                 explains, no decision; 6 user requests a diagnostic; 7 core recomputes
                 exactly; 8 user decides and records
- labels:        "user", "deterministic core", "tutoring tier (optional)",
                 "1 request verification", "2 compute scores (exact)", "3 return scores",
                 "4 what does this mean?", "5 explain (no decision)",
                 "6 request diagnostic", "7 recompute (exact)", "8 decide + record",
                 "observations stay local"
- annotations:   on step 5, "reads the scores and the fixed definitions; writes nothing to
                 the record"; on step 7, "a suggestion from the tutor is executed by the
                 core — never accepted as a number from the model"; on step 8, in
                 vermillion, "decision authority stays human"; a footer, "observations
                 stay local for the whole exchange"
- caption:       Figure 14.2 — Who computes, who explains, who decides. Every number in the exchange comes from the deterministic core, including the follow-up the tutor suggested; the tutoring tier reads scores and writes nothing to the record; and the final step, deciding and recording, is outlined in vermillion because it belongs to the person throughout.
- alt-text:      A sequence diagram with three lanes, a user, the deterministic core and a tutoring tier drawn with a dashed header to mark it optional, plus a footer note that the observations stay local throughout. Eight numbered steps: the user requests verification; the core computes the scores exactly; the scores return; the user asks what the result means; the tutoring tier explains without deciding, annotated it reads the scores and writes nothing to the record; the user asks for a further diagnostic; the core recomputes exactly, annotated that a suggestion from the tutor is always executed by the core, never accepted as a number from the model; and the user decides and records, outlined in vermillion and annotated decision authority stays human.
- infographic description: A flat vector sequence diagram, 16:9, off-white background,
                 three lanes top to bottom. Title top-left: "Who computes, who explains,
                 who decides". Standfirst: "Every number comes from the core. Every
                 decision stays with the person." Lane headers: blue human "user"; green
                 box "deterministic core"; orange dashed-border box "tutoring tier
                 (optional)". Eight numbered horizontal arrows: "1 request verification"
                 user to core; "2 compute scores (exact)" as a self-step in the core
                 lane; "3 return scores" core to user; "4 what does this mean?" user to
                 tutor; "5 explain (no decision)" tutor to user, annotated "reads the
                 scores and the fixed definitions; writes nothing to the record"; "6
                 request diagnostic" user to core; "7 recompute (exact)" in the core
                 lane, annotated "a suggestion from the tutor is executed by the core —
                 never accepted as a number from the model"; "8 decide + record" in the
                 user lane, outlined vermillion and annotated "decision authority stays
                 human". Footer: "observations stay local for the whole exchange".
                 Sentence case throughout.
```

## 14.5 The escalation tier: when explanation is not enough

The third tier is a team-side escalation route for cases the deterministic core and the local tutoring tier cannot resolve between them.
It is defined as much by what it does not carry across the boundary as by what it provides.
Some verification results raise questions that a non-specialist user, even a well-tutored one, should not resolve alone: an unexpected score pattern that might indicate a data problem rather than a forecast problem, a methodological choice about which threshold or accumulation period is appropriate, or a result whose operational implications are serious enough to warrant a specialist's judgement **[AUTHOR: give a representative example of a case that was escalated and what the escalation resolved — ideally one where escalation caught something the local tiers would have got wrong]**.
The escalation tier exists so that these cases reach the team that built and maintains the toolkit, and its critical property is that the escalation carries only what the partner is permitted to share (the aggregate scores and the user's question) and never the observations themselves, which remain inside the trust boundary exactly as they do during ordinary use.
This is the same egress line drawn in §14.2, now enforced at the one point in the workflow where information deliberately crosses it: a person asks another person a question, mediated by shared aggregate figures, which is a channel the partner's data policy already contemplates because it is how professional collaboration has always worked.

The escalation tier is where the toolkit's division of authority is made complete, and its design reflects a judgement about where scarce specialist attention is best spent.
The deterministic core handles the routine computation that needs no judgement; the tutoring tier handles the routine explanation that a local model can give safely; and the escalation tier reserves the team's limited time for the genuinely hard cases, which are a small fraction of the total but the ones where a wrong call is costly **[AUTHOR: the approximate proportion of interactions that escalated, if measured, and how that proportion changed as users gained experience]**.
The limitation of this tier is that it reintroduces a human bottleneck and a dependence on the team's availability, which is precisely the dependence the deterministic and tutoring tiers were designed to minimise; this dependence is accepted deliberately, on the reasoning that eliminating the bottleneck entirely would mean either sending the observations to the specialists, which is forbidden, or letting a local model make specialist judgements it cannot be trusted to make, which is the failure mode the whole architecture exists to prevent.
The escalation tier is therefore not a fallback to be engineered away in a later version but a permanent structural feature: the point at which a system built to respect a data boundary hands the residual, irreducible judgement back to accountable people, which is where Chapters 11 and 12 argue such judgement belongs.

## 14.6 The toolkit as a teaching instrument

The three-tier design turned out to do something it was not built for: it teaches.
That second role turned out to be among the toolkit's more durable contributions **[AUTHOR: confirm whether the teaching use was anticipated from the outset or emerged in use, and how central it became]**.
The mechanism is straightforward once the tiers are in place: a user who runs the deterministic core sees exact, trustworthy scores; the tutoring tier then explains those scores in the user's own context, against their own forecasts, rather than through a generic textbook example; and over repeated use the user internalises the meaning of the measures and needs the tutoring tier less.
Verification is a skill that has historically been difficult to disseminate to partner organisations precisely because it is learned through worked exposure to real cases, and the observations that make a case real are the ones that cannot be shared, so the conventional routes, a training workshop built on someone else's data or a manual full of generic examples, teach the mechanics without the judgement (moderate confidence; this reflects the recurring difficulty of transferring verification practice, and the specific gap this toolkit addressed) **[AUTHOR: describe the prior state of verification capability at the partner organisation and what changed as the toolkit was used — ideally with a concrete before-and-after]**.
Because the toolkit brings the teaching to the data instead of the data to the training, each partner learns on the material that matters to them, inside their own boundary, at no marginal cost.

The teaching function also disciplines the design of the tutoring tier in a way that improves the toolkit as a verification instrument, because a tier built to teach must explain its reasoning rather than merely assert conclusions.
An explanation good enough to teach from is one that names the score it is discussing, states the definition it is reasoning from, and shows how the number leads to the interpretation, which is exactly the transparent, checkable form of output that makes a language model safe to include in a governed workflow, and the opposite of the confident, unsourced assertion that makes one dangerous.
The pedagogical framing thus reinforces the governance framing: the same property that lets a user learn from the tutoring tier (visible reasoning from fixed definitions) is the property that lets a user catch the tier when it is wrong.
The limitation worth stating is that a toolkit which teaches also shapes what its users come to regard as normal practice, so an error or a narrowness baked into the tutoring tier's explanations propagates into the habits of everyone who learns from it; this places a real obligation on the maintaining team to review the tier's explanatory behaviour periodically, treating it as curriculum rather than as a finished feature (moderate-to-high confidence that this obligation is ongoing rather than one-off).
The before-and-after change in the partner's working practice is summarised in Figure 14.3.

**Figure 14.3 — The partner's workflow, before and after.**

![A two-panel before-and-after diagram. The top panel shows observations inside a trust boundary and a dashed arrow trying to leave towards off-site verification, blocked at the boundary with a vermillion cross and tagged months of negotiation, often no agreement, annotated that the expertise sat on one side and the data on the other. The bottom panel shows the same boundary with the toolkit moved inside: a deterministic core, an optional tutoring tier and human review, annotated verification and teaching now happen where the data already is, with one permitted arrow leaving, aggregate scores only, and a note that users learn on their own data rather than on someone else's worked examples.](../figures/figure-14-3.svg)

*Figure 14.3 — Before, the data was asked to move; after, the verification moved instead. The top panel is the route that kept failing: months of negotiation towards an egress that often never came. The bottom panel is the same boundary with the tools inside it, scores produced where the observations already live, and one permitted arrow out carrying aggregates. The bonus nobody designed for: partners learn verification on their own data. (Rendered as `figures/figure-14-3.svg` from the brief below, per `FIGURES.md`.)*

```
FIGURE BRIEF
- id:            Figure 14.3
- title:         From blocked egress to local verification and learning
- type:          before/after
- claim:         The redesign replaces a slow, often-failing attempt to move observations out for verification with a toolkit that moves verification in, so scores are produced locally and only aggregates leave.
- standfirst:    The data was asked to move. The verification moved instead.
- canvas:        16:9
- elements:      two stacked panels sharing a grammar. Top "before": a sky-blue
                 observations cylinder inside a grey trust boundary, a dashed arrow
                 blocked at the boundary with a vermillion cross, an external
                 "verification, off-site" box, a tag "months of negotiation / often no
                 agreement". Bottom "after": the same cylinder and boundary, with a green
                 "deterministic core", an orange dashed "tutoring tier (optional)" and a
                 blue "human review" inside, one permitted arrow out labelled "aggregate
                 scores only" to "team"
- flow:          top panel left-to-right, blocked at the boundary; bottom panel
                 self-contained inside the boundary with one permitted aggregate arrow out
- labels:        "before", "observations", "trust boundary", "verification, off-site",
                 "blocked", "months of negotiation / often no agreement", "after",
                 "deterministic core", "tutoring tier (optional)", "human review",
                 "aggregate scores only", "team", "users learn on own data"
- annotations:   on the top panel, "the expertise sat on one side, the data on the other";
                 on the vermillion cross, "the holding institution cannot accept the
                 residual risk — and does not have to"; on the bottom panel, "verification
                 and teaching now happen where the data already is"; on the exit arrow,
                 "aggregates cross; records never do"; a footer, "the bonus nobody
                 designed for: partners learn verification on their own data"
- caption:       Figure 14.3 — Before, the data was asked to move; after, the verification moved instead. The top panel is the route that kept failing: months of negotiation towards an egress that often never came. The bottom panel is the same boundary with the tools inside it, scores produced where the observations already live, and one permitted arrow out carrying aggregates. The bonus nobody designed for: partners learn verification on their own data.
- alt-text:      A two-panel before-and-after diagram. The top panel shows observations inside a trust boundary and a dashed arrow trying to leave towards off-site verification, blocked at the boundary with a vermillion cross and tagged months of negotiation, often no agreement, annotated that the expertise sat on one side and the data on the other. The bottom panel shows the same boundary with the toolkit moved inside: a deterministic core, an optional tutoring tier and human review, annotated verification and teaching now happen where the data already is, with one permitted arrow leaving, aggregate scores only, and a note that users learn on their own data rather than on someone else's worked examples.
- infographic description: A flat vector before-and-after diagram, 16:9, off-white
                 background, two stacked panels. Title top-left: "From blocked egress to
                 local verification and learning". Standfirst: "The data was asked to
                 move. The verification moved instead." Top panel "before": a grey
                 trust-boundary rectangle holding a sky-blue cylinder "observations"; a
                 dashed grey arrow attempts to exit towards an external box "verification,
                 off-site" and is stopped at the boundary by a vermillion cross labelled
                 "blocked", with the tag "months of negotiation / often no agreement" and
                 the annotations "the expertise sat on one side, the data on the other"
                 and, at the cross, "the holding institution cannot accept the residual
                 risk — and does not have to". Bottom panel "after": the same boundary
                 and cylinder, now with a green box "deterministic core", an orange
                 dashed box "tutoring tier (optional)" and a blue human "human review"
                 inside, annotated "verification and teaching now happen where the data
                 already is"; a single arrow exits labelled "aggregate scores only" to a
                 box "team", annotated "aggregates cross; records never do"; a tag "users
                 learn on own data". Footer: "the bonus nobody designed for: partners
                 learn verification on their own data". Sentence case throughout.
```

## 14.7 What the constraints taught

The broadest lesson here is that treating hard constraints as design inputs rather than obstacles produced an architecture that is better along dimensions the constraints were not aimed at.
State that carefully, because it is easily mistaken for a claim that constraints are always beneficial, which they are not.
The requirement of no data egress forced a local, open-weight model and a strict separation between an exact core and an advisory tier; the requirement of minimal compute forced that advisory tier to be small and optional; and the requirement of no recurring budget forced the whole toolkit to be self-sustaining after handover.
Each of these was a limitation accepted under duress, and yet the design they jointly produced (deterministic where the evidence must be defensible, advisory only where a mistake is recoverable, and human where judgement is irreducible) is close to the design one would argue for on governance grounds alone, which is the argument made throughout Parts II and III of this book **[AUTHOR: state the concrete outcomes actually observed — how many partners adopted the toolkit, over what period, whether verification that was previously not happening began happening, and any measured change in forecast-verification practice; keep the claims to what was measured]**.
That a governance-first design and a constraint-first design converge is the finding this chapter most wants to leave you with.
The discipline the well-resourced can *choose* to adopt, the under-resourced are *forced* into, and the forced version is not obviously worse.

The limitation of this case study, stated plainly, is that it is a single deployment in a specific setting, and its architecture should be treated as a transferable pattern rather than its results as a general proof.
The three-tier shape (an exact core, an optional local advisory tier that only explains, and a human escalation route that carries no protected data) generalises to any setting where a trustworthy computation must run beside data that cannot move and beside users who need help interpreting the output, which describes a large class of environmental-science collaborations beyond rainfall verification.
What does not generalise without re-testing is every concrete figure: the competence of a given open-weight model at a given size on a given explanatory task, the compute a given partner can spare, and the proportion of cases that escalate are all specific to this deployment and its period, and they will differ elsewhere and drift over time (high confidence in the pattern; low confidence that any specific number here transfers) **[AUTHOR: the caught-failure anecdote promised in §14.4 — a real instance where the tutoring tier gave a wrong or misleading explanation, how it was noticed, and what changed as a result — anchors this limitation better than any general statement]**.
The methods that would let another group verify or extend this work (the exact scores, the score definitions handed to the tutoring tier, the sanitised toolkit configuration and the escalation protocol) belong in the companion repository rather than in print, both because they are operational detail and because they will be maintained as a living artefact after this chapter is fixed.
The connection back to the rest of the book is direct: this chapter is Chapter 11's evidential discipline, Chapter 12's least-privilege data handling, Chapter 3's insistence on a specification the user controls, and Chapter 16's cost realism, assembled under a single hard constraint and shown to hold.

---

### References (verify details before release)

- Ben Bouallègue, Z., et al. (2024). The rise of data-driven weather forecasting: a first statistical assessment of machine learning-based weather forecasts in an operational-like context. *Bulletin of the American Meteorological Society*, 105(6). https://doi.org/10.1175/BAMS-D-23-0162.1
- Bi, K., Xie, L., Zhang, H., Chen, X., Gu, X., & Tian, Q. (2023). Accurate medium-range global weather forecasting with 3D neural networks. *Nature*, 619, 533–538. https://doi.org/10.1038/s41586-023-06185-3
- Lam, R., et al. (2023). Learning skillful medium-range global weather forecasting. *Science*, 382(6677), 1416–1421. https://doi.org/10.1126/science.adi2336
- Lang, S., Alexe, M., Chantry, M., et al. (2024). AIFS — ECMWF's data-driven forecasting system. *arXiv preprint* **[verify journal version]**. https://arxiv.org/abs/2406.01465
- Jolliffe, I. T., & Stephenson, D. B. (eds.). *Forecast Verification: A Practitioner's Guide in Atmospheric Science*. Wiley. **[verify: edition and year]**
- Wilks, D. S. *Statistical Methods in the Atmospheric Sciences*. Academic Press / Elsevier. **[verify: edition and year]**
- Jones, N. B. (2026). "I Cut the Internet and Let AI Read the File I Could Never Upload. It Caught the Leak." Video, @natebjones, 19 July 2026. https://www.youtube.com/watch?v=5slsNizN6MQ (practitioner commentary; concepts cited as corroboration, not evidence)
- **[AUTHOR: add the specific verification-methodology references the toolkit's scores are drawn from — e.g. the primary sources for the fractions skill score and the continuous ranked probability score — and any WMO data-policy document cited for the sovereignty constraint.]**
