# Chapter 14 — Verification under constraint

> **Status:** draft r3 · voice v3.3 (`STYLE.md`) · sentence-per-line per `STYLE.md` §10 · figures as briefs per `FIGURES.md`.
> **Conventions:** vendor-neutral (outline §9) · **[AUTHOR: …]** marks lived material only the author can supply · **[verify]** marks real but unconfirmed details · citations drawn only from verified reports in `/research`. Nothing has been invented.
> This chapter reports executed operational work; concrete partner details, datasets, metrics, hardware, results and outcomes are the author's lived material and are tagged **[AUTHOR: …]**.

---

## 14.1 The setting: verification that cannot see the observations

The case study this chapter takes up is an ordinary problem made difficult by a single constraint that reshapes everything downstream: the observations against which a rainfall forecast must be judged cannot leave the institution that holds them.
Rainfall verification is, in its mechanics, among the better-understood tasks in operational meteorology: a forecast field is compared against gauge or radar observations, and a set of scores summarises how well the two agree over some period and area.
The difficulty here is not the arithmetic but the data policy around it, because the partner organisations whose forecasts most need independent verification are frequently the ones least able to release their observational record.
This matters more, not less, as forecasting itself moves towards data-driven methods: machine-learning weather models crossed the credibility threshold in 2022–23 and, by early 2025, an operational centre was running one on duty alongside its physics-based system, verified in operational-like conditions before it was trusted (Lam et al., 2023; Bi et al., 2023; Lang et al., 2024).
National meteorological and hydrological services in many jurisdictions hold rain-gauge data under licences, memoranda or national regulations that prohibit its transfer to an external party, and the reasons are legitimate rather than obstructive: gauge networks are sometimes commercially licensed, sometimes bound by bilateral agreements, and sometimes protected as a matter of national sovereignty over environmental data **[AUTHOR: state the specific data-sovereignty basis for the partner(s) in this case — e.g. national data policy, commercial licensing of the gauge network, a WMO data-exchange category — and the region or programme this work served]**.
The consequence is a standing asymmetry: the expertise, the reference forecasts and the verification methodology sit on one side, and the observations that would exercise them sit on the other, behind a boundary that cannot be crossed by moving the data.

> **Definition — Data sovereignty.** The principle that a dataset stays under the legal and
> physical control of the institution or nation that holds it, so that where the data lives, and
> who may move it, are governed by that holder's rules rather than by whoever wants to use it.
> For observational records it often means the numbers may be worked on, but not taken away.

The conventional resolution of this asymmetry is to move the data anyway, under a data-sharing agreement negotiated case by case, and this resolution fails often enough in practice to be worth designing around rather than depending upon.
Negotiating egress for a research observation set can take months, binds both parties to terms that constrain reuse, and frequently ends without agreement because the holding institution cannot accept the residual risk of releasing a record it is obliged to protect **[AUTHOR: the specific negotiation history or timeline that motivated the constrained approach — how long an egress route was attempted, and why it was set aside]**.
The design response developed here inverts the usual direction of movement: rather than bringing the observations to the verification tools, it brings the verification tools to the observations, packaged so that they run entirely inside the partner's own environment and emit only what the partner chooses to share, typically aggregate scores, never the underlying records.
That inversion is the organising decision of the whole toolkit, and the three constraints it must satisfy (no data egress, minimal compute, no recurring budget) are the subject of the next section, because each of them independently pushes the design towards the same three-tier shape.

## 14.2 Three constraints that determine the architecture

The architecture of the toolkit is not a free design choice but a fairly direct consequence of three constraints, each of which would on its own rule out a large part of the conventional solution space, and which together leave only a narrow set of workable designs.
The first constraint is that no observational data may leave the partner's environment, which forecloses every approach that relies on a hosted service, a cloud-based model endpoint or any tool that transmits inputs off-site for processing (high confidence; this is a hard requirement, not a preference).
The practical force of this constraint is easily underestimated: it excludes not only the obvious case of uploading gauge records to an external analysis platform, but also the subtler case of sending observation-derived text (an error summary, a flagged station list, a data excerpt) to a model accessed over a network, because such text can carry exactly the information the data policy protects.
Anything that reasons over the observations must therefore execute locally, within the trust boundary the partner already controls, and this single requirement is what forces the language-model component, where it exists at all, to be an open-weight model running on the partner's own hardware rather than a hosted one (which connects directly to the least-privilege and data-handling arguments of Chapter 12).

> **Definition — Open-weight model.** A language model whose trained parameters (its "weights")
> are published, so that it can be downloaded and run on local hardware, inside an institution's
> own network, with nothing sent to an outside service. This is the opposite of a hosted model,
> which is reachable only by sending the input over the network to another party's computer.

The same two conclusions circulate independently in practitioner commentary: telling a cloud model not to read or transmit something is a behavioural safeguard that can be silently violated, so only an architectural boundary (no network path) is reliable, and an offline local model that triages material into risk tiers before anything external is contacted is exactly this toolkit's tiered pattern (practitioner commentary, 2026).

The second constraint is minimal compute, because the partner environments in view here are not equipped with the accelerators or the memory that a large hosted model assumes, and a toolkit that demands them would simply not run where it is needed **[AUTHOR: specify the representative hardware the toolkit was required to run on — CPU-only versus a single consumer GPU, approximate memory, whether an internet connection was available at all]**.
The third constraint is the absence of any recurring budget: the toolkit had to keep working after the project that funded its construction ended, without per-query charges, subscription renewals or licence fees that a partner with no dedicated software budget could not sustain (moderate-to-high confidence that this is decisive for adoption; the cost reasoning is developed in Chapter 16).
These three constraints converge on a common conclusion.
A verification result that partners will trust and report must be exact, reproducible and free of any dependence on a fallible or metered external service; anything that merely explains, teaches or guides is valuable but must never be allowed to alter that result, and must degrade gracefully to nothing if the compute to run it is unavailable.
That separation (an exact core that always runs, and an optional advisory layer that sometimes runs and never decides) is the seam along which the three tiers are cut, and the following three sections take each tier in turn.

**Figure 14.1 — The three-tier toolkit under constraint.**

![An architecture diagram dominated by a large box labelled partner environment, the trust boundary. Inside it, an observations cylinder feeds a deterministic verification core that produces scores, which a human review diamond inspects. A dashed optional box labelled local tutoring tier connects to the core's outputs to explain and guide but is tagged no decision. Only one arrow leaves the boundary, from human review to an external team icon, labelled aggregate scores and questions only; the observations never cross.](../figures/figure-14-1.svg)

*Figure 14.1 — The three-tier design. A deterministic core computes the scores and always runs; an optional local open-weight tutoring tier explains and guides but never touches a verdict; escalation to the team carries only aggregate scores and questions, never the observations, which stay inside the partner's trust boundary throughout. (Rendered as `figures/figure-14-1.svg` from the brief below, per `FIGURES.md`.)*

```
FIGURE BRIEF
- id:            Figure 14.1
- title:         Three tiers inside one trust boundary
- type:          architecture
- claim:         The constraints (no data egress, minimal compute, no recurring budget) force a design in which an exact deterministic core always runs, an optional local tutoring tier only explains, and escalation crosses to the team carrying no observations.
- canvas:        16:9
- elements:      a large grey-bordered rounded rectangle labelled "partner environment (trust boundary)" enclosing most of the canvas; inside it, left, a sky-blue cylinder "observations (never leave)"; centre, a green-bordered box "deterministic verification core" (tool colour) containing a small "scores" artefact; above/right of the core, an orange-bordered box "local tutoring tier — open-weight model" (agent colour) with a dashed border to denote optional; a vermillion diamond "human review" (gate colour) reading the scores; from the diamond, a single arrow labelled "aggregate scores + questions only" crossing the trust boundary to a blue head-and-shoulders "team (escalation)" icon outside the box
- flow:          left-to-right inside the boundary: observations → deterministic core → scores → human review; the tutoring tier connects to the core's outputs with a dashed two-way "explains / guides" link and carries a small "no decision" tag; only the human-review diamond has an arrow leaving the boundary, and it is labelled to show observations never cross
- labels:        "partner environment (trust boundary)", "observations (never leave)",
                 "deterministic verification core", "scores", "local tutoring tier — open-weight model",
                 "optional", "explains / guides", "no decision", "human review",
                 "aggregate scores + questions only", "team (escalation)"
- annotations:   a light bracket along the trust-boundary edge labelled "no observational data egress"; the dashed border on the tutoring tier annotated "degrades to nothing if compute unavailable"
- caption:       Figure 14.1 — The three-tier design. A deterministic core computes the scores and always runs; an optional local open-weight tutoring tier explains and guides but never touches a verdict; escalation to the team carries only aggregate scores and questions, never the observations, which stay inside the partner's trust boundary throughout.
- alt-text:      An architecture diagram dominated by a large box labelled partner environment, the trust boundary. Inside it, an observations cylinder feeds a deterministic verification core that produces scores, which a human review diamond inspects. A dashed optional box labelled local tutoring tier connects to the core's outputs to explain and guide but is tagged no decision. Only one arrow leaves the boundary, from human review to an external team icon, labelled aggregate scores and questions only; the observations never cross.
- generator prompt: A flat vector architecture diagram on an off-white background. A large
                 grey-bordered rounded rectangle fills most of the canvas, labelled
                 "partner environment (trust boundary)". Near its left edge sits a sky-blue
                 cylinder labelled "observations (never leave)", with a short arrow rightward
                 into a green-bordered rectangle labelled "deterministic verification core"
                 that contains a small tag "scores". Above and right of the core, a
                 dashed orange-bordered rectangle labelled "local tutoring tier — open-weight
                 model" connects to the core's outputs by a dashed double-headed link labelled
                 "explains / guides", and carries a small tag "no decision" and a small tag
                 "optional". From the core, an arrow leads to a vermillion diamond labelled
                 "human review". A single arrow leaves the large rectangle from that diamond,
                 crossing the border to a blue head-and-shoulders icon labelled "team
                 (escalation)" outside, the arrow labelled "aggregate scores + questions only".
                 A thin bracket runs along the boundary edge labelled "no observational data
                 egress". Minimal text, generous spacing, single-weight lines.
```

## 14.3 The deterministic core: verification that never guesses

The foundation of the toolkit is a deterministic verification core that computes standard rainfall-verification scores by fixed algorithms, producing the same numbers from the same inputs every time it runs, and this determinism is a deliberate design commitment rather than an implementation detail.
Rainfall forecasts are verified with a well-established and stable set of measures, and the core implements the subset appropriate to the partner's forecasts and decisions: for categorical forecasts of exceedance above a threshold, the contingency-table scores — probability of detection, false-alarm ratio, frequency bias and a threat or equitable-threat score; for continuous fields, mean error, mean absolute error and root-mean-square error; and, where the forecast is probabilistic or ensemble-based, reliability and a proper score such as the Brier score or the continuous ranked probability score, together with the spatial measures (neighbourhood or fractions-based) that avoid the double-penalty problem of point matching **[AUTHOR: state which scores the toolkit actually computes for this partner, the exceedance thresholds and accumulation periods used, and why those were the operationally relevant choices]** [verify: standard references for these scores, e.g. Jolliffe & Stephenson; Wilks — confirm editions before release].
None of these measures involves a language model, a learned component or any stochastic element; each is a closed-form calculation over the matched forecast–observation pairs, and this is exactly what allows a partner to report the output as an official figure and to reproduce it independently.

The reason to hold verification deterministic whilst admitting a language model elsewhere in the toolkit is the argument made across Chapter 11, and it is worth restating in this concrete setting: a verification result is a measurement, and a measurement whose value could change because a generative model was in a different mood is not a measurement at all.
The evidential weight a verification score has to carry (informing whether a forecast system is fit for issuing warnings, or whether one configuration outperforms another) depends on the score being a fixed function of the data, auditable line by line and defensible to a regulator or a sceptical colleague who re-runs it (high confidence).
This is exactly the discipline the meteorological community has applied to the new data-driven models themselves: when an operational centre assessed a machine-learning forecast model, it did so in an operational-like context, initialised from operational analyses, verified against both analyses and station observations with its own standard metrics, and reported the model's genuine strengths alongside documented weaknesses such as smoothing and the underestimation of some extremes (Ben Bouallègue et al., 2024).
Introducing a model into the scoring path would import precisely the failure mode this book treats as central: plausible, fluent output uncorrelated with correctness, in a place where a wrong number is worse than no number because it looks authoritative.
The core therefore does the one thing a language model cannot be trusted to do, namely arrive at the same defensible number twice, and the toolkit spends its language-model budget only on the things the core cannot do, which are explaining what the numbers mean and helping a non-specialist user act on them correctly.
The boundary between these two is the toolkit's most important design line, and it is drawn so that no output of the tutoring tier can reach a reported score without passing back through the deterministic core.

## 14.4 The tutoring tier: an open-weight model that explains but does not decide

The optional middle tier is a local, open-weight language model whose entire remit is to explain the verification output and guide the user's next action, and its defining constraint is negative: it computes no score, alters no score, and produces nothing that is reported as a result.
The reason to include a language model at all in a verification toolkit is that the users are frequently not verification specialists, and a table of contingency scores is opaque to someone who has not internalised what a false-alarm ratio of 0.4 alongside a probability of detection of 0.9 actually implies for their forecast **[AUTHOR: characterise the intended users — forecasters, hydrologists, technicians — and their prior familiarity with verification scores]**.
The tutoring tier reads the scores the core has already computed, together with the fixed definitions of those scores, and produces plain-language explanation: what each number means, which scores are in tension, what a plausible next diagnostic step would be, and what the result does not license the user to conclude.
Running an open-weight model locally is what makes this admissible under the first constraint, because the model never transmits anything off-site; it also makes the tier free to run under the third constraint, since an open-weight model on the partner's own hardware carries no per-query charge (moderate confidence that a model small enough for the target hardware is nonetheless competent at this bounded explanatory task, the kind of claim that must be re-tested per model, and the energy cost of local inference is treated in Chapter 16) **[AUTHOR: name the capability class and approximate parameter scale of the open-weight model used, the year, and the observed quality of its explanations on real cases — including any cases where its explanation was wrong and how that was caught]**.

The safeguard that keeps the tutoring tier from quietly becoming a decision-maker is architectural rather than merely cautionary, and it matters because an advisory component that users come to trust will be treated as authoritative whatever its label says.
The tier is given read-only access to the core's outputs and the score definitions, and no path by which its text can be written back into the record of results; a user who follows its suggestion to compute an additional score does so by invoking the deterministic core again, not by accepting a number the model has produced.
This is the least-privilege principle of Chapter 12 applied to an internal component: the model is granted exactly the access its explanatory job requires and no more, so that even a badly wrong explanation cannot corrupt a reported figure, only mislead a user who, by the design of the escalation tier, retains the authority and the means to check it.
The residual risk is that a fluent but mistaken explanation misleads a non-specialist into a poor interpretation, and this risk is real and cannot be designed away entirely; it is mitigated by keeping the tier's outputs explanatory rather than prescriptive, by having it cite the fixed score definitions it reasons from, and by the escalation route that exists precisely for the cases where explanation is not enough.
The interaction between a user, the deterministic core and the tutoring tier, with decision authority remaining with the human throughout, is the subject of the sequence in Figure 14.2.

**Figure 14.2 — A verification-plus-tutoring interaction.** *A figure brief follows `FIGURES.md`; render in the house style.*

```
FIGURE BRIEF
- id:            Figure 14.2
- title:         Who computes, who explains, who decides
- type:          sequence
- claim:         In a single interaction the deterministic core computes the scores, the tutoring tier only explains them, and the human holds decision authority throughout; the model never touches the verdict.
- canvas:        16:9
- elements:      four vertical lanes read top-to-bottom — a blue "user" head-and-shoulders lane; a green "deterministic core" lane (tool); an orange "tutoring tier" lane (agent), drawn with a dashed lane header to mark it optional; a vermillion "human decision" marker that belongs to the user lane and closes the sequence
- flow:          numbered steps downward: 1 user requests verification of a forecast against local observations; 2 deterministic core computes scores exactly; 3 core returns scores to user; 4 user asks the tutoring tier "what does this mean?"; 5 tutoring tier reads scores + definitions and returns plain-language explanation, tagged "no decision"; 6 user optionally asks core for an additional diagnostic; 7 core recomputes exactly; 8 user makes the call — the vermillion decision marker — and records the reported scores
- labels:        "user", "deterministic core", "tutoring tier (optional)", "1 request verification",
                 "2 compute scores (exact)", "3 return scores", "4 what does this mean?",
                 "5 explain (no decision)", "6 request diagnostic", "7 recompute (exact)",
                 "8 decide + record", "observations stay local"
- annotations:   a vermillion outline around step 8 labelled "decision authority stays human"; a light tag on the tutoring lane "reads scores, writes nothing to the record"
- caption:       Figure 14.2 — One interaction across the three actors. Every number that is reported comes from the deterministic core; the tutoring tier only explains what the core produced; and the human makes and records the decision. The observations never leave the local environment at any step.
- alt-text:      A top-to-bottom sequence with four lanes: user, deterministic core, an optional tutoring tier, and a human decision. The user requests verification; the core computes and returns exact scores; the user asks the tutoring tier what they mean and receives a plain-language explanation marked no decision; the user may request a further diagnostic, which the core recomputes exactly; finally the user decides and records the reported scores. A callout marks that decision authority stays human and that observations stay local.
- generator prompt: A flat vector sequence diagram on an off-white background, read top to
                 bottom, with four vertical lanes. Lane one, blue, headed by a
                 head-and-shoulders icon labelled "user". Lane two, green, labelled
                 "deterministic core". Lane three, orange, with a dashed header labelled
                 "tutoring tier (optional)". Numbered horizontal arrows between lanes:
                 "1 request verification" from user to core; "2 compute scores (exact)" a
                 self-loop on the core; "3 return scores" core to user; "4 what does this
                 mean?" user to tutoring tier; "5 explain (no decision)" tutoring tier back to
                 user; "6 request diagnostic" user to core; "7 recompute (exact)" self-loop on
                 the core; "8 decide + record" ending in the user lane, enclosed in a
                 vermillion outline labelled "decision authority stays human". A small tag on
                 the tutoring lane reads "reads scores, writes nothing to the record", and a
                 footer note reads "observations stay local". Minimal text, single-weight
                 arrows, generous spacing.
```

## 14.5 The escalation tier: when explanation is not enough

The third tier is a team-side escalation route for the cases that the deterministic core and the local tutoring tier cannot between them resolve, and it is defined as much by what it does not carry across the boundary as by what it provides.
Some verification results raise questions that a non-specialist user, even a well-tutored one, should not resolve alone: an unexpected score pattern that might indicate a data problem rather than a forecast problem, a methodological choice about which threshold or accumulation period is appropriate, or a result whose operational implications are serious enough to warrant a specialist's judgement **[AUTHOR: give a representative example of a case that was escalated and what the escalation resolved — ideally one where escalation caught something the local tiers would have got wrong]**.
The escalation tier exists so that these cases reach the team that built and maintains the toolkit, and its critical property is that the escalation carries only what the partner is permitted to share (the aggregate scores and the user's question) and never the observations themselves, which remain inside the trust boundary exactly as they do during ordinary use.
This is the same egress line drawn in §14.2, now enforced at the one point in the workflow where information deliberately crosses it: a person asks another person a question, mediated by shared aggregate figures, which is a channel the partner's data policy already contemplates because it is how professional collaboration has always worked.

The escalation tier is where the toolkit's division of authority is made complete, and its design reflects a judgement about where scarce specialist attention is best spent.
The deterministic core handles the routine computation that needs no judgement; the tutoring tier handles the routine explanation that a local model can give safely; and the escalation tier reserves the team's limited time for the genuinely hard cases, which are a small fraction of the total but the ones where a wrong call is costly **[AUTHOR: the approximate proportion of interactions that escalated, if measured, and how that proportion changed as users gained experience]**.
The limitation of this tier is that it reintroduces a human bottleneck and a dependence on the team's availability, which is precisely the dependence the deterministic and tutoring tiers were designed to minimise; this dependence is accepted deliberately, on the reasoning that eliminating the bottleneck entirely would mean either sending the observations to the specialists, which is forbidden, or letting a local model make specialist judgements it cannot be trusted to make, which is the failure mode the whole architecture exists to prevent.
The escalation tier is therefore not a fallback to be engineered away in a later version but a permanent structural feature: the point at which a system built to respect a data boundary hands the residual, irreducible judgement back to accountable people, which is where Chapters 11 and 12 argue such judgement belongs.

## 14.6 The toolkit as a teaching instrument

A consequence of the three-tier design that was not its original purpose is that the toolkit functions as a teaching instrument, and this dual role turned out to be among its more durable contributions **[AUTHOR: confirm whether the teaching use was anticipated from the outset or emerged in use, and how central it became]**.
The mechanism is straightforward once the tiers are in place: a user who runs the deterministic core sees exact, trustworthy scores; the tutoring tier then explains those scores in the user's own context, against their own forecasts, rather than through a generic textbook example; and over repeated use the user internalises the meaning of the measures and needs the tutoring tier less.
Verification is a skill that has historically been difficult to disseminate to partner organisations precisely because it is learned through worked exposure to real cases, and the observations that make a case real are the ones that cannot be shared, so the conventional routes, a training workshop built on someone else's data or a manual full of generic examples, teach the mechanics without the judgement (moderate confidence; this reflects the recurring difficulty of transferring verification practice, and the specific gap this toolkit addressed) **[AUTHOR: describe the prior state of verification capability at the partner organisation and what changed as the toolkit was used — ideally with a concrete before-and-after]**.
Because the toolkit brings the teaching to the data instead of the data to the training, each partner learns on the material that matters to them, inside their own boundary, at no marginal cost.

The teaching function also disciplines the design of the tutoring tier in a way that improves the toolkit as a verification instrument, because a tier built to teach must explain its reasoning rather than merely assert conclusions.
An explanation good enough to teach from is one that names the score it is discussing, states the definition it is reasoning from, and shows how the number leads to the interpretation, which is exactly the transparent, checkable form of output that makes a language model safe to include in a governed workflow, and the opposite of the confident, unsourced assertion that makes one dangerous.
The pedagogical framing thus reinforces the governance framing: the same property that lets a user learn from the tutoring tier (visible reasoning from fixed definitions) is the property that lets a user catch the tier when it is wrong.
The limitation worth stating is that a toolkit which teaches also shapes what its users come to regard as normal practice, so an error or a narrowness baked into the tutoring tier's explanations propagates into the habits of everyone who learns from it; this places a real obligation on the maintaining team to review the tier's explanatory behaviour periodically, treating it as curriculum rather than as a finished feature (moderate-to-high confidence that this obligation is ongoing rather than one-off).
The before-and-after change in the partner's working practice is summarised in Figure 14.3.

**Figure 14.3 — The partner's workflow, before and after.** *A figure brief follows `FIGURES.md`; render in the house style.*

```
FIGURE BRIEF
- id:            Figure 14.3
- title:         From blocked egress to local verification and learning
- type:          before/after
- claim:         The redesign replaces a slow, often-failing attempt to move observations out for verification with a toolkit that moves verification in, so scores are produced locally, users learn on their own data, and only aggregates ever leave.
- canvas:        16:9
- elements:      two stacked panels sharing a grammar. Top panel "before": a sky-blue
                 observations cylinder inside a grey trust-boundary box, a blocked/dashed
                 arrow (grey, with a small vermillion cross) attempting to leave the boundary
                 towards an external "verification, off-site" box, and a "months of negotiation
                 / often no agreement" tag. Bottom panel "after": the same observations
                 cylinder and trust boundary, now enclosing a green "deterministic core" and a
                 dashed orange "tutoring tier", a vermillion "human review" diamond, and a
                 single arrow labelled "aggregate scores only" leaving to a blue "team" icon;
                 a small tag "users learn on own data"
- flow:          top panel left-to-right blocked at the boundary; bottom panel self-contained
                 inside the boundary with one permitted aggregate arrow out
- labels:        "before", "observations", "trust boundary", "verification, off-site",
                 "blocked", "months of negotiation / often no agreement",
                 "after", "deterministic core", "tutoring tier (optional)", "human review",
                 "aggregate scores only", "team", "users learn on own data"
- annotations:   a vermillion cross on the blocked egress arrow (before); a light bracket under
                 the after panel labelled "verification and teaching happen inside the boundary"
- caption:       Figure 14.3 — Before and after. The conventional route tried to move protected observations out to be verified and frequently stalled; the toolkit moves verification and teaching in, so the observations never move, scores are produced locally and reproducibly, and only aggregate figures cross the boundary.
- alt-text:      Two stacked panels. The before panel shows an observations cylinder inside a trust boundary with a blocked, crossed-out arrow trying to reach off-site verification, tagged months of negotiation and often no agreement. The after panel shows the same observations and boundary now containing a deterministic core, an optional tutoring tier and a human review step, with a single arrow carrying aggregate scores only out to the team, and a note that users learn on their own data.
- generator prompt: A flat vector before/after diagram on an off-white background, two stacked
                 panels sharing the same visual grammar. Top panel labelled "before": a grey
                 rounded-rectangle trust boundary containing a sky-blue cylinder labelled
                 "observations"; a dashed grey arrow tries to leave the boundary towards an
                 external box labelled "verification, off-site" but is crossed by a small
                 vermillion X labelled "blocked"; a tag reads "months of negotiation / often no
                 agreement". Bottom panel labelled "after": the same grey trust boundary and
                 sky-blue "observations" cylinder, now also containing a green box
                 "deterministic core" and a dashed orange box "tutoring tier (optional)" and a
                 vermillion diamond "human review"; a single arrow labelled "aggregate scores
                 only" leaves the boundary to a blue head-and-shoulders icon labelled "team"; a
                 small tag reads "users learn on own data". A light bracket under the lower
                 panel reads "verification and teaching happen inside the boundary". Minimal
                 text, single-weight lines, generous spacing.
```

## 14.7 What the constraints taught

The broadest lesson of this case study is that treating hard constraints as design inputs rather than obstacles produced an architecture that is better on dimensions the constraints were not aimed at, and this must be stated carefully because it is easily mistaken for a claim that constraints are always beneficial, which they are not.
The requirement of no data egress forced a local, open-weight model and a strict separation between an exact core and an advisory tier; the requirement of minimal compute forced that advisory tier to be small and optional; and the requirement of no recurring budget forced the whole toolkit to be self-sustaining after handover.
Each of these was a limitation accepted under duress, and yet the design they jointly produced (deterministic where the evidence must be defensible, advisory only where a mistake is recoverable, and human where judgement is irreducible) is close to the design one would argue for on governance grounds alone, which is the argument made throughout Parts II and III of this book **[AUTHOR: state the concrete outcomes actually observed — how many partners adopted the toolkit, over what period, whether verification that was previously not happening began happening, and any measured change in forecast-verification practice; keep the claims to what was measured]**.
The convergence of a governance-first design and a constraint-first design is the finding this chapter most wants to leave, because it suggests that the discipline the well-resourced can *choose* to adopt, the under-resourced are *forced* into, and the forced version is not obviously worse.

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
- Nate B Jones (2026). "I Cut the Internet and Let AI Read the File I Could Never Upload." Video, @natebjones, 19 July 2026. https://www.youtube.com/watch?v=5slsNizN6MQ (practitioner commentary; concepts cited as corroboration, not evidence)
[ai-reviewer: two format defects against the other chapters' video entries. First, the creator is given as "Nate B Jones" here (and in FURTHER-READING) but as "Jones, N. B." in ch02 and ch03 — one surname convention must be chosen and applied everywhere, including FURTHER-READING §Practitioner commentary. Second, the R-3 report records the full title as "I Cut the Internet and Let AI Read the File I Could Never Upload. It Caught the Leak." — the truncated title should be completed or the truncation checked against the source.]
- **[AUTHOR: add the specific verification-methodology references the toolkit's scores are drawn from — e.g. the primary sources for the fractions skill score and the continuous ranked probability score — and any WMO data-policy document cited for the sovereignty constraint.]**
