# Chapter 13 — The failure gallery

> **Status:** draft r6 · voice v5.0 (`STYLE.md` §1) · sentence-per-line per `STYLE.md` §10 · figures as briefs per `FIGURES.md`.
> **Conventions:** vendor-neutral (outline §9) · **[AUTHOR: …]** marks lived material only the author can supply · **[verify]** marks real but unconfirmed details · citations drawn only from verified reports in `/research`. Nothing has been invented.
> The six failure *types* and the *checks* that catch them are written in full here; the illustrative incidents are the author's real, anonymised cases, marked **[AUTHOR: …]** to be supplied, never invented.

---

## 13.1 Why the failures deserve a gallery

Agentic workflows fail in few kinds of ways, the same ways repeatedly, and every one of them can be caught by design.
That is genuinely good news, because it means you are better served by a small taxonomy of failure, each mode paired with the check that catches it, than by an ever-growing catalogue of incidents.

Chapter 1 set out the property that makes these systems unlike the instruments you are used to: they fail plausibly, producing output whose fluency tells you nothing about its correctness.
The ordinary human defence, distrusting work that *looks* wrong, barely helps, because the work rarely looks wrong.
So these failures cannot be managed by vigilance, since vigilance is exactly what fluency defeats.
They can be managed only by a check sitting outside the system, returning a verdict that does not depend on the output looking right.
That is the principle Chapter 1 introduces and Chapter 11 builds on.
So each failure is treated here as a matched pair: a durable description of the mode, which changes slowly because it follows from how the systems are built, and the check that catches it, which is the part you should actually implement.
The incidents are illustration.
The check is the deliverable.
The taxonomy is not a construction of this book alone: the largest empirical study of multi-agent failures to date, which annotated more than two hundred execution traces across seven popular frameworks and reached high inter-annotator agreement, sorts what it found into three broad families that map onto this gallery closely: poor task or role specification, breakdowns in passing information between steps, and absent or weak verification of outcomes (Cemri et al., 2025).

The taxonomy has six modes, chosen on two grounds.
Each recurs across the pattern chapters, and each is caught by a *different* check, so between them they exercise most of the verification this book has built: fabricated citations, silent unit errors, specification drift, over-agreeable review, context loss and confident extrapolation.
Each section states the mode and why it happens, marks the author's anonymised example of catching it, gives the check in a form you can adopt, and places that check on the evidential hierarchy of Chapter 11, which runs from cheap mechanical confirmation at the base, through corroboration by a method with a different error structure, to adversarial scrutiny at the top.
The thread pulled together at the end (§13.8) is that five of the six are caught at or near the base of that ladder, by checks that are cheap, mechanical and unglamorous.
What the gallery really teaches is not sophistication but the refusal to skip the cheap check because the output reads well (high confidence).

## 13.2 Fabricated citations

A fabricated citation is a reference an agent presents as real and specific, with authors, title, year, venue and sometimes a plausible identifier, for a work that does not exist, or that exists but does not support the claim it is attached to.

This is the most reported failure of language models in scholarly work, and it persists not through a training oversight but as a direct consequence of how these systems produce text.
A reference is a highly patterned string, and a model that has learned the *shape* of citations in a field can generate new ones that fit the shape perfectly whilst corresponding to nothing, because the machinery that makes the string well-formed is the same whether or not a matching paper exists.
The danger for science is specific and severe: a fabricated reference is plausible by construction, survives casual reading, and, once it enters a manuscript, a literature review or a funding proposal, lends borrowed authority to a claim that has none.
Hence a fabricated reference cannot be caught by reading alone, because the property that would betray it, an ill-formed or implausible string, is exactly what the generating mechanism suppresses.

The empirical scale of the problem is large and has not diminished across model generations.
The most rigorous quantification available had two models of the 2023 generation, one markedly stronger than the other, produce short literature reviews and then checked every reference by hand: more than half of the weaker model's citations were wholly fabricated and close to a fifth of the stronger model's were, whilst a large share of even the *real* citations carried wrong volumes, pages or dates (Walters and Wilder, 2023).
This is not a solved, 2023-vintage problem either: two years on, across eight assistants and four hundred requests, roughly two-fifths of the references asked for were still erroneous or invented, with the rate varying sharply by system and by field (Cabezas-Clavijo and Sidorenko-Bautista, 2025).
In the standard taxonomy of the failure this is *factual fabrication*, output that conflicts with verifiable world knowledge, as distinct from the faithfulness failures that matter more in retrieval-grounded work (Huang et al., 2023).
The strongest 2026 evidence comes not from prompting a model and checking it but from papers that had already passed review: an audit of one elite machine-learning venue found 100 fabricated citations across 53 papers accepted there in 2025, each having passed three to five expert reviewers, roughly 1% of accepted papers, a single-venue, single-year figure (Ansari, 2026; itself, with some irony, an unreviewed preprint).
These sorted into five modes led by total fabrication (66%) and partial corruption of a real work's details (27%), with identifier hijacking, a real identifier stitched onto a fake reference, a distinct mode.
Most telling, the contamination was usually only one or two citations in a whole paper, small enough for expert plausibility reading to miss, which is exactly why the check must be mechanical rather than a careful read.
Chapter 5 built its entire synthesis pattern around the refusal to let the model be the source of its own citations, and Chapter 9 named fabrication first among the failure modes of the manuscript stage; this chapter states the general check that both rely on.

[AUTHOR: a real, anonymised example of a fabricated citation you caught — the plausible-but-nonexistent reference, the claim it was propping up, and the moment the resolver returned nothing.]

The check is mechanical and admits no exception: every citation an agent emits is resolved against an external bibliographic authority (a digital-object-identifier resolver, an indexed database, the publisher of record), and a reference that does not resolve to a real work whose content matches the claim is deleted, not repaired.
What makes the check reliable is that it is external to the system being checked, so it cannot be fooled by the fluency that fools a reader; what makes it cheap is that resolution is automatable, so it scales to a whole reference list without human labour per entry.
Two refinements matter.
Resolution has to confirm not merely existence but *support*, that the real paper says what the citation claims, because a genuine reference misattached to a claim is a subtler instance of the same failure, caught only by reading the source.
On Chapter 11's hierarchy the existence check sits at the base, a tier-one mechanical confirmation that should never be skipped; the support check sits one rung up, needing a human or a retrieval step to compare claim against source (high confidence).

**Figure 13.1 — A fabricated citation, caught at the resolver.**

![A left-to-right failure trace in four steps. A claim needing support goes to an agent, which drafts a citation. The citation string appears as a well-formed reference card tagged in vermillion as plausible by construction: right shape, right journal, right year. It then meets a resolver check against an external bibliographic authority, annotated as external to the model, so fluency cannot fool it. The not-found exit loops back labelled delete, do not repair. A footer reads that reading cannot catch this failure, because the property that would betray the citation is exactly what the generating process suppresses.](../figures/figure-13-1.svg)

*Figure 13.1 — The gallery's most reported failure, and the cheapest to catch. The drafted citation has the right shape, the right journal style and the right year, because the same machinery that makes it well-formed works whether or not the paper exists. Reading cannot catch it. The resolver can, because it is external to the model, and the disposition is deletion: a reference that fails is never repaired into existence. (Rendered as `figures/figure-13-1.svg` from the brief below, per `FIGURES.md`.)*

```
FIGURE BRIEF
- id:            Figure 13.1
- title:         A fabricated citation, caught at the resolver
- type:          failure trace
- claim:         A fluent, well-formed citation can correspond to no real work; only an external resolver, not a reader, reliably catches it.
- standfirst:    It looks perfect because the same machinery works whether or not the paper exists.
- canvas:        16:9
- elements:      a left-to-right trace — a human "claim to support" (blue); an "agent
                 drafts citation" square (orange); a "citation string" card (sky blue)
                 shown as a well-formed reference; a "resolver check" gate (vermillion)
                 with a "not found" exit
- flow:          left-to-right: claim → agent drafts → citation string → resolver gate;
                 the "not found" exit loops back labelled "delete, do not repair"
- labels:        "claim to support", "agent drafts citation", "citation string",
                 "resolver check", "not found", "delete, do not repair"
- annotations:   on the citation card, in vermillion, "plausible by construction — right
                 shape, right journal, right year"; on the resolver, "checked against an
                 external bibliographic authority — fluency cannot fool it"; on the loop,
                 "a failing reference is deleted, never repaired into existence"; a
                 footer, "reading cannot catch this: the property that would betray it is
                 exactly what the generating process suppresses"
- caption:       Figure 13.1 — The gallery's most reported failure, and the cheapest to catch. The drafted citation has the right shape, the right journal style and the right year, because the same machinery that makes it well-formed works whether or not the paper exists. Reading cannot catch it. The resolver can, because it is external to the model, and the disposition is deletion: a reference that fails is never repaired into existence.
- alt-text:      A left-to-right failure trace in four steps. A claim needing support goes to an agent, which drafts a citation. The citation string appears as a well-formed reference card tagged in vermillion as plausible by construction: right shape, right journal, right year. It then meets a resolver check against an external bibliographic authority, annotated as external to the model, so fluency cannot fool it. The not-found exit loops back labelled delete, do not repair. A footer reads that reading cannot catch this failure, because the property that would betray the citation is exactly what the generating process suppresses.
- infographic description: A flat vector failure trace, 16:9, off-white background.
                 Title top-left: "A fabricated citation, caught at the resolver".
                 Standfirst: "It looks perfect because the same machinery works whether or
                 not the paper exists." Left to right: a blue human icon "claim to
                 support"; an orange rounded square "agent drafts citation"; a sky-blue
                 card "citation string" drawn as a tidy reference with a vermillion tag
                 "plausible by construction — right shape, right journal, right year"; a
                 vermillion diamond "resolver check" annotated "checked against an
                 external bibliographic authority — fluency cannot fool it". The
                 diamond's "not found" exit curves back to the agent labelled "delete, do
                 not repair", annotated "a failing reference is deleted, never repaired
                 into existence". Footer: "reading cannot catch this: the property that
                 would betray it is exactly what the generating process suppresses".
                 Sentence case throughout.
```

## 13.3 Silent unit errors

A silent unit error is a numerical result wrong by a physical factor, such as a conversion missed, a scale confused, or a per-second quantity summed as though it were per-hour, that passes through the workflow with no signal at all, because the number that comes out is dimensionally unlabelled and superficially reasonable.

This one is treacherous in the environmental sciences precisely because the domain is full of units converting by unremarkable factors, and of quantities whose plausible ranges overlap across scales.
A rainfall rate, a discharge, a flux and an accumulation all live within a few orders of magnitude of one another, so a wrong-by-a-factor result rarely announces itself by being absurd.
Chapter 1 traced the root cause to the training distribution: a unit conversion buried mid-sentence in prose is sparsely and inconsistently represented, and multi-step quantitative reasoning done in prose rather than delegated to computation fails often enough to warrant a standing rule against it.
Chapters 6 and 8 build their patterns on the same premise: an agent proposes numerical operations and a tool with explicit units disposes of them.
The failure is silent in exactly the way that defeats vigilance: there is nothing to see, because the error lives in the interpretation of a number, not in its appearance.

[AUTHOR: a real, anonymised silent unit or scale error you caught — the quantity, the factor by which it was wrong, and the dimensional or range check that surfaced it.]

The check has two parts, both mechanical, and both cheap relative to the cost of the error escaping.
The first is that quantities carry their units through the computation as data rather than as prose, so that a dimensionally inconsistent operation raises an error at the point it is attempted instead of producing a clean but meaningless number; a units-aware library, a typed schema on every field, or a pipeline that refuses unlabelled quantities all serve.
The second is a physical-range assertion at every boundary where a quantity enters or leaves a step: a rainfall accumulation outside a stated plausible envelope, a discharge that implies an impossible velocity, or a flux with the wrong sign, each halted and flagged rather than passed on.
Neither check reasons about the science; both are guardrails that convert a silent failure into a loud one, which is the only transformation that matters, because a loud failure is caught and a silent one is shipped.
On Chapter 11's hierarchy these are base-tier checks (mechanical, automatable, applied before any interpretation), and their placement there is deliberate: the cheapest checks guard the failure that is otherwise least visible (high confidence).

**Figure 13.2 — A silent unit error, made loud.**

![A top-to-bottom failure trace. An agent computes a quantity and produces a bare number, forty-two, with no units attached, tagged in vermillion as wrong by a physical factor yet looking entirely reasonable. It meets a units and range assertion, which halts it as out of range and returns it to the agent. Below, greyed out and crossed by a vermillion bar, sits the downstream use the error never reached. Annotations note that the assertion does not reason about the science, it just refuses unlabelled or impossible values, and the footer reads that the whole trick is converting a silent failure into a loud one, because a loud failure gets caught and a silent one gets shipped.](../figures/figure-13-2.svg)

*Figure 13.2 — Nothing about 42 looks wrong. A quantity off by a factor of 25.4 or 3,600 is still a plausible number, which is why no amount of inspection helps. The units-and-range assertion does not understand the science; it simply refuses a value with no declared unit or outside the physical envelope. That refusal is everything: a loud failure gets caught, a silent one gets shipped. (Rendered as `figures/figure-13-2.svg` from the brief below, per `FIGURES.md`.)*

```
FIGURE BRIEF
- id:            Figure 13.2
- title:         A silent unit error, made loud by a range assertion
- type:          failure trace
- claim:         A wrong-by-a-factor quantity is dimensionally invisible; a units-aware step and a range assertion convert a silent error into a halted one.
- standfirst:    Nothing about the number looks wrong. That is the problem.
- canvas:        16:9
- elements:      a top-to-bottom trace — an "agent computes quantity" square (orange); a
                 "number: 42 (no units)" card (sky blue); a "units + range assertion"
                 diamond (vermillion) with an "out of range — halt" exit returning to the
                 agent; a greyed "downstream use" box crossed by a vermillion bar
- flow:          top-to-bottom: agent computes → bare number → units/range gate; halt
                 exit returns to the agent; the grey "downstream use" box is shown
                 unreached
- labels:        "agent computes quantity", "number (no units)",
                 "units + range assertion", "out of range — halt", "downstream use"
- annotations:   on the number card, in vermillion, "wrong by a physical factor — and
                 still a perfectly reasonable-looking value"; on the gate, "does not
                 reason about the science: refuses unlabelled units and impossible
                 values"; on the vermillion bar, "error stopped here — the calibration
                 and the verification never see it"; a footer, "the whole trick is
                 turning a silent failure into a loud one: loud gets caught, silent gets
                 shipped"
- caption:       Figure 13.2 — Nothing about 42 looks wrong. A quantity off by a factor of 25.4 or 3,600 is still a plausible number, which is why no amount of inspection helps. The units-and-range assertion does not understand the science; it simply refuses a value with no declared unit or outside the physical envelope. That refusal is everything: a loud failure gets caught, a silent one gets shipped.
- alt-text:      A top-to-bottom failure trace. An agent computes a quantity and produces a bare number, forty-two, with no units attached, tagged in vermillion as wrong by a physical factor yet looking entirely reasonable. It meets a units and range assertion, which halts it as out of range and returns it to the agent. Below, greyed out and crossed by a vermillion bar, sits the downstream use the error never reached. Annotations note that the assertion does not reason about the science, it just refuses unlabelled or impossible values, and the footer reads that the whole trick is converting a silent failure into a loud one, because a loud failure gets caught and a silent one gets shipped.
- infographic description: A flat vector failure trace, 16:9, off-white background,
                 flowing top to bottom. Title top-left: "A silent unit error, made loud by
                 a range assertion". Standfirst: "Nothing about the number looks wrong.
                 That is the problem." An orange rounded square "agent computes quantity"
                 leads down to a sky-blue card "number: 42 (no units)" with a vermillion
                 tag "wrong by a physical factor — and still a perfectly
                 reasonable-looking value". It leads to a vermillion diamond "units +
                 range assertion", annotated "does not reason about the science: refuses
                 unlabelled units and impossible values". Its "out of range — halt" exit
                 curves back to the agent. Below the diamond, a greyed box "downstream
                 use" crossed by a thick vermillion bar annotated "error stopped here —
                 the calibration and the verification never see it". Footer: "the whole
                 trick is turning a silent failure into a loud one: loud gets caught,
                 silent gets shipped". Sentence case throughout.
```

## 13.4 Specification drift

Specification drift is the gradual divergence, over a long or multi-turn interaction, between what an agent is actually working towards and what the original specification asked for.
The workflow ends up solving a task next to the intended one, while every individual step looks responsive.

This is a direct expression of the anti-pattern Chapter 3 named as the central hazard of specifying work: conversational drift in place of specification, where the controlling intent moves out of a written, auditable artefact and into an accumulating chat history nobody re-reads.
It happens because each turn conditions on the recent exchange more strongly than on the initial instruction, so a sequence of individually reasonable accommodations (a redefinition here, a relaxed criterion there, a helpful reinterpretation of an ambiguous term) compounds into a destination the specification never authorised.
Chapter 7 meets the same failure in pipeline work, where an agent asked to fix a failing test can drift into altering the test rather than the code, satisfying the letter of the request whilst inverting its purpose.
The reason drift is dangerous is that it is invisible at every step: there is no single wrong action to catch, only a slow rotation of the target that is legible only against the original specification, held fixed.
It is one of the failure families the large multi-agent study puts first: poor or under-specified tasks and roles, which it finds account for a substantial share of the breakdowns it annotated (Cemri et al., 2025).

> **Definition — Specification drift.** Over many turns, the objective an agent is actually
> pursuing slides away from what was first requested, one reasonable-looking accommodation at a
> time. No single step appears wrong; only the original written specification, held fixed and
> re-read, reveals how far the target has moved.

[AUTHOR: a real, anonymised case of specification drift you caught — the original acceptance criterion, the point at which the agent's target had rotated away from it, and the re-read that surfaced the gap.]

The check is to keep the specification external, versioned and authoritative, and to re-assert *it*, not the conversation, as the acceptance criterion at every gate.
Concretely, the objective, inputs, acceptance criteria and stop conditions of Chapter 3 live in a file, not in the dialogue; the agent's output at each checkpoint is judged against that file by a step that does not carry the conversation in its context; and any change to the specification is a deliberate, logged edit rather than an emergent accommodation.
The reason this works is that drift is *defined* by divergence from a fixed reference, so restoring the fixed reference restores the ability to measure the divergence: a check that costs almost nothing when the specification is a real artefact and is impossible when it is not.
On Chapter 11's hierarchy this is a mid-tier check: not a single mechanical assertion but a structured comparison of an output against a written standard, sitting above the base precisely because it requires that the standard exist in auditable form before the work begins (high confidence).

**Figure 13.3 — Specification drift, caught by re-reading the spec.**

![A fixed specification tag sits at the top. Below it, three turns run left to right, each with a small target arrow rotating further away from the specification, with dashed reference lines showing the growing angle. Each turn is annotated as looking individually responsive: a redefinition here, a relaxed criterion there, a helpful reinterpretation. After turn three a vermillion callout reads that the target has rotated and no single step was the wrong one. A compare-to-spec gate then checks the latest output against the fixed document, exits drift detected, and routes to a human decision. The footer reads that drift is defined by divergence from a fixed reference, so the check costs almost nothing when the specification is a real artefact and is impossible when it is not.](../figures/figure-13-3.svg)

*Figure 13.3 — No single turn is the wrong one. Each accommodation looks responsive on its own, and the target rotates anyway, which is why drift is invisible from inside the conversation. The check is the cheapest in the gallery: hold the specification fixed and external, and compare the output to it rather than to the chat. It costs nothing when the specification is a real artefact, and it is impossible when it is not. (Rendered as `figures/figure-13-3.svg` from the brief below, per `FIGURES.md`.)*

```
FIGURE BRIEF
- id:            Figure 13.3
- title:         Specification drift, caught against a fixed specification
- type:          failure trace
- claim:         Across turns an agent's target rotates away from the specification while each step looks responsive; only comparison against the fixed, external specification reveals it.
- standfirst:    No single step is wrong. The target moves anyway.
- canvas:        16:9
- elements:      a "specification (fixed, external)" tag (blue) held at the top; a
                 left-to-right chain of three "turn" squares (orange) whose target arrows
                 rotate progressively away; dashed grey reference lines from the
                 specification to each turn; a "compare to spec" gate (vermillion) with a
                 "drift detected" exit to a "human decision" (blue)
- flow:          three turns left-to-right, each with a target arrow pointing further from
                 the fixed specification; the final gate compares the latest output to the
                 specification
- labels:        "specification (fixed, external)", "turn 1", "turn 2", "turn 3",
                 "compare to spec", "drift detected", "human decision"
- annotations:   on turn 1, "a redefinition — looks responsive"; on turn 2, "a relaxed
                 criterion — looks responsive"; on turn 3, "a helpful reinterpretation —
                 looks responsive"; after turn 3, in vermillion, "the target has rotated,
                 and no single step was the wrong one"; on the gate, "judged against the
                 document, not the conversation"; a footer, "drift is divergence from a
                 fixed reference — the check is free when the specification is a real
                 artefact, impossible when it is not"
- caption:       Figure 13.3 — No single turn is the wrong one. Each accommodation looks responsive on its own, and the target rotates anyway, which is why drift is invisible from inside the conversation. The check is the cheapest in the gallery: hold the specification fixed and external, and compare the output to it rather than to the chat. It costs nothing when the specification is a real artefact, and it is impossible when it is not.
- alt-text:      A fixed specification tag sits at the top. Below it, three turns run left to right, each with a small target arrow rotating further away from the specification, with dashed reference lines showing the growing angle. Each turn is annotated as looking individually responsive: a redefinition here, a relaxed criterion there, a helpful reinterpretation. After turn three a vermillion callout reads that the target has rotated and no single step was the wrong one. A compare-to-spec gate then checks the latest output against the fixed document, exits drift detected, and routes to a human decision. The footer reads that drift is defined by divergence from a fixed reference, so the check costs almost nothing when the specification is a real artefact and is impossible when it is not.
- infographic description: A flat vector failure trace, 16:9, off-white background. Title
                 top-left: "Specification drift, caught against a fixed specification".
                 Standfirst: "No single step is wrong. The target moves anyway." A blue
                 tag "specification (fixed, external)" sits centred near the top. Below,
                 three orange rounded squares left to right, "turn 1", "turn 2", "turn 3",
                 each with a short arrow above it rotating further from vertical, and
                 dashed grey lines up to the specification tag showing the widening angle.
                 Annotations beneath: "a redefinition — looks responsive"; "a relaxed
                 criterion — looks responsive"; "a helpful reinterpretation — looks
                 responsive". After turn 3, a vermillion callout "the target has rotated,
                 and no single step was the wrong one". The chain ends at a vermillion
                 diamond "compare to spec", annotated "judged against the document, not
                 the conversation", whose "drift detected" exit leads to a blue human icon
                 "human decision". Footer: "drift is divergence from a fixed reference —
                 the check is free when the specification is a real artefact, impossible
                 when it is not". Sentence case throughout.
```

## 13.5 Over-agreeable review (sycophancy)

Over-agreeable review is what happens when a language model asked to evaluate, critique or check work agrees with the position it thinks you hold, softens or drops objections, and rates the work more favourably than an impartial assessment would.
The review step returns reassurance instead of scrutiny.

The research literature documents the behaviour under the name sycophancy (Sharma et al., 2023), and its mechanism is well characterised rather than anecdotal.
Analysing the human-preference data these models are tuned on, the same study found that a response *matching the user's stated view* is among the strongest predictors of human approval, and that optimising against a preference model can actively increase agreement: human feedback itself, imperfectly, rewards agreeing over telling the truth.
This does particular damage in a scientific workflow, because review is the check much of this book rests on.
Chapter 10 makes an independent reviewer agent a full role, and Chapter 7 puts one before any human code review.
A reviewer that agrees by disposition provides the *appearance* of an independent check and none of its substance.
A sycophantic reviewer is worse than no reviewer, because no reviewer leaves the gap visible whereas a sycophantic one fills it with false assurance, which is precisely what a verification step exists to prevent.

> **Definition — Over-agreeable review (sycophancy).** A model asked to check work tends to
> side with whoever is asking, softening or dropping objections it would otherwise raise. It is
> a trained-in disposition to please rather than laziness, which is why it cannot be fixed by
> instructing the model to be tougher: a system disposed to agree will agree that it should be
> tougher and then continue agreeing about the work.

[AUTHOR: a real, anonymised case where a review or check agent agreed too readily — the flaw it waved through, and how the independence-preserving arrangement (or an adversarial re-prompt) exposed it.]

The check is structural, not a matter of asking the model to be more critical, because a system disposed to agree will agree that it should be more critical and then continue to agree about the work.
Independence has to be engineered: the reviewer is given the artefact and the acceptance criteria but *not* the author's conclusion or the conversation that produced it, so it has no position to infer and defer to; the review is framed as a search for specific, enumerable defects against a checklist rather than as a request for an overall verdict, which resists the pull towards a bland positive; and, where the stakes justify the cost, an adversarial framing or a second reviewer with a deliberately opposed brief is used to break the symmetry.

A sharper version of the problem afflicts the cheapest reviewer configuration, in which the same model, or the same family, both drafts and reviews.
Judges systematically favour text that is familiar to them, scoring their own and similar models' output higher even when a human would not (Wataoka et al., 2024), and the founding study of model-as-judge evaluation catalogued exactly this self-enhancement bias alongside biases towards the first-presented and the longer answer (Zheng et al., 2023).
Genuine independence therefore needs model diversity, not merely a fresh context window.
The deeper principle, consistent with the whole book, is that a check is only as good as its independence from what it checks, and sycophancy is what independence failure looks like when the checker is a language model; Chapter 10 turns this gallery-level check into a full reviewer roster.
On Chapter 11's hierarchy an agreeable review provides no evidential lift at all and must not be counted as a tier, whereas a properly independent review sits in the upper tiers because it approximates the scrutiny of a disinterested party, but only to the extent its independence is real (moderate-to-high confidence).

**Figure 13.4 — Sycophantic review, exposed by engineered independence.**

![Two parallel traces of the same artefact. In the top trace the artefact arrives together with the author's conclusion; the reviewer sees the conclusion and returns approved, shown with a vermillion cross and tagged false assurance, worse than no review, because the gap now looks filled. In the bottom trace the same artefact arrives with the conclusion withheld and the reviewer is briefed to find defects against a checklist rather than to judge acceptability; it returns a genuine defect. The annotation between the traces reads that the only difference is what the reviewer was shown and asked. A footer notes that asking a model to be tougher does not work, because a system disposed to agree will agree about that too.](../figures/figure-13-4.svg)

*Figure 13.4 — The same artefact, reviewed twice. The only difference between the traces is what the reviewer was shown and what it was asked. Given the author's conclusion and a request to evaluate, it ratifies; given the artefact alone and a brief to find defects, it finds one. Asking the model to be tougher changes nothing, because a system disposed to agree will agree about that too. Independence is configured, not requested. (Rendered as `figures/figure-13-4.svg` from the brief below, per `FIGURES.md`.)*

```
FIGURE BRIEF
- id:            Figure 13.4
- title:         Sycophantic review, exposed by engineered independence
- type:          failure trace
- claim:         A reviewer that can infer the author's position agrees with it; withholding the conclusion and framing review as defect-search restores real scrutiny.
- standfirst:    Independence is configured, not requested.
- canvas:        16:9
- elements:      two parallel left-to-right traces of the same artefact. Top (failure):
                 "artefact + author conclusion" (blue) feeds "reviewer sees conclusion"
                 (purple), returning "approved" crossed in vermillion. Bottom (fix):
                 "artefact, conclusion withheld" feeds "reviewer: find defects" (purple),
                 returning "defect found"
- flow:          two stacked left-to-right traces sharing the same artefact; the top ends
                 in a vermillion-crossed approval, the bottom in a genuine defect
- labels:        "artefact + author conclusion", "reviewer sees conclusion", "approved",
                 "artefact, conclusion withheld", "reviewer: find defects", "defect found"
- annotations:   on the top reviewer, in vermillion, "it agrees with the position it
                 inferred"; on the crossed approval, "false assurance — worse than no
                 review, because the gap now looks filled"; between the traces, "the only
                 difference: what the reviewer was shown, and what it was asked"; on the
                 bottom reviewer, "criteria only, adversarial brief, no sight of the
                 conclusion"; a footer, "asking it to be tougher does not work — a system
                 disposed to agree will agree about that too"
- caption:       Figure 13.4 — The same artefact, reviewed twice. The only difference between the traces is what the reviewer was shown and what it was asked. Given the author's conclusion and a request to evaluate, it ratifies; given the artefact alone and a brief to find defects, it finds one. Asking the model to be tougher changes nothing, because a system disposed to agree will agree about that too. Independence is configured, not requested.
- alt-text:      Two parallel traces of the same artefact. In the top trace the artefact arrives together with the author's conclusion; the reviewer sees the conclusion and returns approved, shown with a vermillion cross and tagged false assurance, worse than no review, because the gap now looks filled. In the bottom trace the same artefact arrives with the conclusion withheld and the reviewer is briefed to find defects against a checklist rather than to judge acceptability; it returns a genuine defect. The annotation between the traces reads that the only difference is what the reviewer was shown and asked. A footer notes that asking a model to be tougher does not work, because a system disposed to agree will agree about that too.
- infographic description: A flat vector failure trace, 16:9, off-white background, two
                 stacked left-to-right traces. Title top-left: "Sycophantic review,
                 exposed by engineered independence". Standfirst: "Independence is
                 configured, not requested." Top trace: a blue card "artefact + author
                 conclusion" feeds a purple reviewer icon "reviewer sees conclusion",
                 annotated in vermillion "it agrees with the position it inferred",
                 returning a box "approved" struck through with a vermillion cross and
                 tagged "false assurance — worse than no review, because the gap now
                 looks filled". Bottom trace: a blue card "artefact, conclusion withheld"
                 feeds a purple reviewer icon "reviewer: find defects", annotated
                 "criteria only, adversarial brief, no sight of the conclusion",
                 returning a box "defect found" with a plain tick. Between the traces, a
                 centred note: "the only difference: what the reviewer was shown, and
                 what it was asked". Footer: "asking it to be tougher does not work — a
                 system disposed to agree will agree about that too". Sentence case.
```

## 13.6 Context loss

Context loss is when an agent silently drops, truncates or overwrites something it needs, such as an earlier constraint, an intermediate result or a correction issued several turns ago, and then reasons confidently from the incomplete state as though it were complete.
The output is wrong not through faulty reasoning but through a missing premise.

This follows directly from the anatomy of Chapter 2: an agent's working context is finite, its memory across steps is a designed and imperfect mechanism rather than a faithful record, and information that falls outside the window or is never written to persistent state is simply gone, with no error raised because the system cannot miss what it no longer represents.
It is common in exactly the long, valuable workflows this book has been encouraging (a multi-day reprocessing, a synthesis over many documents, a pipeline with many stages), and it is compounded in the multi-agent workflows of Chapter 10, where information has to survive being handed between agents whose contexts do not overlap.
That handoff is one of the failure families the large multi-agent study isolates: information lost or withheld as it passes between steps, which it finds among the commonest breakdowns in multi-agent runs (Cemri et al., 2025).
The characteristic signature is an output that contradicts a constraint the workflow certainly established earlier, delivered with no sign that the constraint was ever known.
The same silent-truncation failure is independently named in practitioner commentary: a large input is often only partly read and then answered fluently with no warning, so an explicit "file too big" error is the better outcome, because it is at least visible (practitioner commentary; see the references).

> **Definition — Context loss.** An agent's working memory is finite and imperfect, so a
> constraint set early, a correction made ten steps ago, or an intermediate result can simply
> fall out of what the agent is currently holding. The agent then reasons confidently from the
> gap, because it cannot notice what it no longer represents.

[AUTHOR: a real, anonymised case of context loss you caught — the constraint or result that was dropped, the confident output that ignored it, and the state check or re-grounding step that caught the omission.]

The check is to externalise the state the workflow depends on rather than trusting it to the agent's context, and to re-ground the agent against that external state at defined points rather than assuming continuity.
Concretely, the load-bearing facts (the constraints, the acceptance criteria, the key intermediate results) are written to a durable artefact that persists independently of any agent's memory; each stage that consumes them reads them from that artefact rather than from the conversation; and critical constraints are re-asserted into context at the start of a stage that must honour them, rather than assumed to have survived.
A complementary check is a consistency assertion at boundaries: an output tested against the constraints on record, so that a violation of a dropped constraint is caught as a contradiction even when the reason for the contradiction is invisible.
On Chapter 11's hierarchy the consistency assertion is a base-tier mechanical check, whilst the re-grounding discipline is an architectural provision that belongs with the provenance and state machinery of Chapter 12; together they convert a silent omission into a detectable contradiction (high confidence).

**Figure 13.5 — Context loss — the dropped constraint and the boundary check that catches it.**

![A left-to-right trace. A constraint is set early and branches down into an external state-on-record store. The agent works, then crosses a dashed context boundary at which the constraint drops away as a faded arrow that does not cross, with a vermillion callout reading that no error is raised because the system cannot miss what it no longer represents. The agent continues and produces a confident output that contradicts the dropped constraint. A consistency assertion checks the output against the state on record, finds the contradiction, and routes to re-ground and retry. The footer reads that the output was wrong through a missing premise, not faulty reasoning, which is why only a check against externalised state can catch it.](../figures/figure-13-5.svg)

*Figure 13.5 — The agent cannot notice what it no longer holds. The constraint fell out at the context boundary without any error, and everything after it is confident reasoning from an incomplete state. The catch happens at the boundary check, where the output is tested against the state on record rather than against the conversation, and the fix is re-grounding. This is why load-bearing facts live in external state, not in the agent's memory. (Rendered as `figures/figure-13-5.svg` from the brief below, per `FIGURES.md`.)*

```
FIGURE BRIEF
- id:            Figure 13.5
- title:         Context loss — the dropped constraint and the boundary check
- type:          failure trace
- claim:         A constraint set early is silently dropped at a context boundary and then contradicted by a confident later output; only a consistency assertion against externalised state catches it.
- standfirst:    The agent cannot miss what it no longer represents.
- canvas:        16:9
- elements:      a left-to-right trace — a "constraint set" card (sky blue) with a branch
                 down to an external "state on record" cylinder (sky blue); an "agent
                 works" square (orange); a vertical dashed grey "context boundary" at
                 which the constraint drops (a faded arrow that does not cross); an
                 "agent continues" square (orange); a "confident output" card; a
                 "consistency assertion vs state" gate (vermillion) exiting
                 "contradiction" to "re-ground and retry"
- flow:          left-to-right: constraint set (branch to state on record) → agent works →
                 context boundary (constraint dropped) → agent continues → confident
                 output → assertion against the record → contradiction → re-ground
- labels:        "constraint set", "state on record", "agent works", "context boundary",
                 "constraint dropped", "agent continues", "confident output",
                 "consistency assertion vs state", "contradiction", "re-ground and retry"
- annotations:   on the branch, "load-bearing facts are written out, not trusted to
                 memory"; at the boundary, in vermillion, "no error raised — the system
                 cannot miss what it no longer represents"; on the confident output,
                 "wrong through a missing premise, not faulty reasoning"; on the gate,
                 "tested against the record, not the conversation"; a footer, "the
                 assertion catches the violation even though the reason for it is
                 invisible"
- caption:       Figure 13.5 — The agent cannot notice what it no longer holds. The constraint fell out at the context boundary without any error, and everything after it is confident reasoning from an incomplete state. The catch happens at the boundary check, where the output is tested against the state on record rather than against the conversation, and the fix is re-grounding. This is why load-bearing facts live in external state, not in the agent's memory.
- alt-text:      A left-to-right trace. A constraint is set early and branches down into an external state-on-record store. The agent works, then crosses a dashed context boundary at which the constraint drops away as a faded arrow that does not cross, with a vermillion callout reading that no error is raised because the system cannot miss what it no longer represents. The agent continues and produces a confident output that contradicts the dropped constraint. A consistency assertion checks the output against the state on record, finds the contradiction, and routes to re-ground and retry. The footer reads that the output was wrong through a missing premise, not faulty reasoning, which is why only a check against externalised state can catch it.
- infographic description: A flat vector failure trace, 16:9, off-white background, left
                 to right. Title top-left: "Context loss — the dropped constraint and the
                 boundary check". Standfirst: "The agent cannot miss what it no longer
                 represents." A sky-blue card "constraint set" with a branch down to a
                 sky-blue cylinder "state on record", the branch annotated "load-bearing
                 facts are written out, not trusted to memory". Then an orange square
                 "agent works", then a vertical dashed grey line "context boundary" where
                 a faded grey arrow labelled "constraint dropped" stops short of
                 crossing, with a vermillion callout "no error raised — the system cannot
                 miss what it no longer represents". Beyond it, an orange square "agent
                 continues" and a card "confident output" annotated "wrong through a
                 missing premise, not faulty reasoning". The output meets a vermillion
                 diamond "consistency assertion vs state", annotated "tested against the
                 record, not the conversation", fed by a line up from the "state on
                 record" cylinder; its "contradiction" exit leads to a box "re-ground and
                 retry". Footer: "the assertion catches the violation even though the
                 reason for it is invisible". Sentence case throughout.
```

## 13.7 Confident extrapolation

Confident extrapolation is a claim, prediction or generalisation reaching beyond what the inputs support, whether outside the range of the data, past the domain of a fitted relationship, or into a regime the evidence never covered, delivered in exactly the same assured tone as a well-supported result and with no signal that the support has run out.

This is the sharpest case of the plausible-failure property of Chapter 1, because the fluency that makes all of these systems' output convincing is at its most dangerous exactly where the output is least warranted: an extrapolation reads no differently from an interpolation, and the register of confidence is uniform whether the claim rests on abundant evidence or none.
It is the failure that most threatens the experimentation and hypothesis-generation work of Chapter 8, where an agent asked to interpret a calibration, propose a mechanism or generalise from a result can produce a claim that is coherent, publishable in tone and unsupported by the data in hand, and where the model-assisted hypothesis, as that chapter insists, is admissible only when explicitly flagged as exploratory and routed to independent test.
Located in the standard taxonomy of hallucination, it is a factuality failure of a particular kind: not an invented fact but an unwarranted reach past the evidence, which the register of confidence hides (Huang et al., 2023).
Confident extrapolation is where an instrument that cannot judge its own correctness does the most damage, because the scientist's trained scepticism is disarmed by the very fluency that should trigger it.

> **Definition — Confident extrapolation.** A claim that reaches past what the data actually
> support, beyond the range that was measured or outside the domain a relationship was fitted
> on, delivered in exactly the same assured tone as a well-grounded result. Nothing in the
> wording signals that the ground has run out; only checking the claim's reach against the
> evidence's reach does.

[AUTHOR: a real, anonymised case of confident extrapolation you caught — the claim that reached beyond the data's support, and the boundary or provenance check that established it had.]

The check is to bind every substantive claim to the support behind it and to reject, or demote to hypothesis, any claim whose support cannot be produced on demand.
Concretely, the workflow requires that a claim carry its provenance (the data range, the fitted domain, the evidence), so that a claim reaching outside that support is caught by comparing the claim's scope against the support's scope rather than by judging the claim's plausibility, which is exactly the judgement the fluency defeats.
A claim that fails this test is not deleted but relabelled: moved from result to flagged hypothesis and sent for the independent test that alone can license it, which is the discipline Chapter 8 builds and Chapter 10's reviewer roles enforce.
This is the check that most depends on the human retaining interpretive authority, because the boundary between supported and unsupported is a scientific judgement the workflow can surface but not make.
On Chapter 11's hierarchy an unsupported claim sits at the bottom regardless of how confident it reads, and moving it upward requires real evidence, corroboration against independent data or successful prediction out of sample, not more assured phrasing (high confidence).

**Figure 13.6 — Confident extrapolation, bounded by its support.**

![A left-to-right trace. A data card shows a marked support range, the span the evidence actually covers. An agent generalises from it and produces a confident claim whose scope bar visibly extends past the support range, with a vermillion bracket marking the overshoot and a callout reading that the claim reads identically to a supported one, because the register of confidence does not change at the edge of the evidence. A scope-versus-support gate compares the two extents, annotated as comparing scopes rather than judging plausibility, which is the judgement fluency defeats. The out-of-support exit routes to a box reading flag as hypothesis, send for independent test, annotated demoted, not deleted. A footer reads that moving a claim back up takes new evidence, not more assured phrasing.](../figures/figure-13-6.svg)

*Figure 13.6 — The claim reads the same on both sides of the evidence's edge. That is what makes extrapolation the sharpest form of plausible failure: confidence does not drop where the support runs out. So the gate never judges how convincing the claim sounds; it compares the claim's scope against the evidence's scope. Anything reaching past gets demoted to hypothesis and sent for independent test, not deleted. More assured phrasing never moves it back up. New evidence does. (Rendered as `figures/figure-13-6.svg` from the brief below, per `FIGURES.md`.)*

```
FIGURE BRIEF
- id:            Figure 13.6
- title:         Confident extrapolation, bounded by its support
- type:          failure trace
- claim:         A claim reaching beyond the data's support reads identically to a supported one; only comparing the claim's scope against the evidence's scope catches it.
- standfirst:    Confidence does not drop where the evidence runs out. The comparison has to be mechanical.
- canvas:        16:9
- elements:      a left-to-right trace — a "data + support range" card (sky blue) with a
                 marked support span; an "agent generalises" square (orange); a
                 "confident claim" card (orange) whose scope bar extends past the support
                 span, the overshoot bracketed in vermillion; a "scope vs support" gate
                 (vermillion) with an "out of support" exit to "flag as hypothesis →
                 independent test"
- flow:          left-to-right: data with support range → agent generalises → confident
                 claim (scope exceeds support) → scope-vs-support gate → out-of-support
                 exit to the hypothesis route
- labels:        "data + support range", "agent generalises", "confident claim",
                 "scope vs support", "out of support",
                 "flag as hypothesis → independent test"
- annotations:   on the support span, "the span the evidence actually covers"; on the
                 claim card, in vermillion, "reads identically to a supported claim — the
                 register of confidence does not change at the edge of the evidence"; on
                 the overshoot bracket, "the reach past the data"; on the gate, "compares
                 scopes; never judges plausibility, which is the judgement fluency
                 defeats"; on the exit, "demoted, not deleted"; a footer, "moving it back
                 up takes new evidence, not more assured phrasing"
- caption:       Figure 13.6 — The claim reads the same on both sides of the evidence's edge. That is what makes extrapolation the sharpest form of plausible failure: confidence does not drop where the support runs out. So the gate never judges how convincing the claim sounds; it compares the claim's scope against the evidence's scope. Anything reaching past gets demoted to hypothesis and sent for independent test, not deleted. More assured phrasing never moves it back up. New evidence does.
- alt-text:      A left-to-right trace. A data card shows a marked support range, the span the evidence actually covers. An agent generalises from it and produces a confident claim whose scope bar visibly extends past the support range, with a vermillion bracket marking the overshoot and a callout reading that the claim reads identically to a supported one, because the register of confidence does not change at the edge of the evidence. A scope-versus-support gate compares the two extents, annotated as comparing scopes rather than judging plausibility, which is the judgement fluency defeats. The out-of-support exit routes to a box reading flag as hypothesis, send for independent test, annotated demoted, not deleted. A footer reads that moving a claim back up takes new evidence, not more assured phrasing.
- infographic description: A flat vector failure trace, 16:9, off-white background, left
                 to right. Title top-left: "Confident extrapolation, bounded by its
                 support". Standfirst: "Confidence does not drop where the evidence runs
                 out. The comparison has to be mechanical." A sky-blue card "data +
                 support range" showing a horizontal bar with a marked span, annotated
                 "the span the evidence actually covers". An arrow to an orange square
                 "agent generalises", then to an orange card "confident claim" whose
                 scope bar visibly extends beyond the support span; the overshoot is
                 bracketed in vermillion, labelled "the reach past the data", and the card
                 carries a vermillion callout "reads identically to a supported claim —
                 the register of confidence does not change at the edge of the evidence".
                 The claim meets a vermillion diamond "scope vs support", annotated
                 "compares scopes; never judges plausibility, which is the judgement
                 fluency defeats". Its "out of support" exit leads to a box "flag as
                 hypothesis → independent test", annotated "demoted, not deleted".
                 Footer: "moving it back up takes new evidence, not more assured
                 phrasing". Sentence case throughout.
```

## 13.8 Reading the gallery

One lesson runs through all six modes: plausible failure is defeated by external mechanism and by nothing else.
So the value of this gallery is in the checks it standardises, not the incidents it recounts.

Read across the six and a common structure appears: each failure produces an output that looks right, each defeats the reader's judgement precisely *because* it looks right, and each is caught not by looking harder but by a check whose verdict does not depend on appearance: a resolver, a range assertion, a comparison to a fixed specification, an engineered-independent review, a consistency assertion against externalised state, a comparison of claim-scope to evidence-scope.
Five of the six checks sit at or near the base of Chapter 11's evidential hierarchy: they are cheap, mechanical and unglamorous, and they are the checks most often skipped for exactly that reason, because a fluent output invites the belief that the cheap check is unnecessary this time.
The discipline the gallery teaches is the refusal of that belief: the standing rule that the check is run because it is cheap and the failure is silent, not because the output looks doubtful, since by construction it will not (high confidence).

The gallery is deliberately a taxonomy and not a census, and two limitations of it should be stated plainly.
First, it is not exhaustive: the six modes are the recurrent ones across the patterns of this book, but new failure modes will appear as capabilities and uses change, and the durable skill is the habit of pairing each observed failure with the external check that would have caught it, not the memorisation of this particular six.
Second, the checks are necessary rather than sufficient: each catches its mode reliably, but a workflow is only as safe as the union of checks actually implemented and actually run, which is why verification is a whole part of this book (Chapters 11 and 12) rather than a section of this one, and why the case studies of Part IV are organised around the checks as much as around the science.
The gallery's proper use is as a checklist of failures to design against from the start, folded into the specification (Chapter 3) and the reviewer roster (Chapter 10) before a workflow runs, rather than as a set of lessons to be relearned one incident at a time (high confidence).

The six also share a shape: one workflow, one wrong artefact, one local check that catches it.
That shape is the gallery's boundary.
A different kind of failure appears only once a whole field adopts these patterns, and §13.9 takes it up.

## 13.9 Beyond the single workflow

None of the four failures below comes with a check.
Every mode above pairs a failure with something a group can run to catch it, and that pairing is the design of this chapter.
These four do not work that way.
They appear when a field adopts these patterns at scale, they are produced by many groups each behaving reasonably, and no gate inside any one workflow detects them.
What a single group can do about each is smaller and less satisfying than a check, and saying so is better than offering a gate that would not work.

**The first — correlated error across groups.**
A multi-model ensemble whose members share a convection scheme is not the ensemble it looks like.
The spread across members understates the real uncertainty, because the members can be wrong in the same direction at the same time.
The forecast then looks better constrained than the evidence supports, and the error that matters is the one every member makes.
Readers of this book know that failure as correlated model error, and know how much work goes into avoiding it.

Chapter 10 §10.3 makes the same argument inside one workflow.
A reviewer agent built on the same model as the drafter supplies correlated opinion rather than an independent check, so genuine independence needs model diversity.
Run that argument across a whole field.
If most groups run their independent-reviewer agent on one of a small number of base models, the field's verification errors correlate.
Independent replication is science's actual error-correction mechanism, and it corrects nothing when the replications share a failure mode.
A hundred groups checking their work with the same instrument is not a hundred checks.

Two things are available to a group, both modest.
Choose reviewer models against what the rest of the field is using rather than against what is convenient, which sometimes means the second-best model on purpose.
And record which model family reviewed what, alongside the reviewer-coverage record of Chapter 12 §12.4, so the correlation is visible to anyone reading the record later.
Neither fixes the problem, but together they turn an invisible dependency into a recorded one, which is what has to happen before anyone notices it.
Confidence is high in the mechanism, since it is the one Chapter 10 §10.3 documents inside a single workflow.
It is moderate in the scale, because nobody has measured how concentrated the field's model use actually is.

**The second — homogenisation of the questions.**
Chapter 8 §8.4 keeps a model-generated hypothesis out of the evidential chain until a human has tested it by a pre-specified procedure.
That gate works inside one workflow.
It says nothing about what happens to a field's range of questions when a generation of researchers brainstorms against the same few models trained on the same corpus.
A model proposes what is well represented in its training material.
Ask it for candidate mechanisms behind an odd signal and it returns the mechanisms the literature already discusses.
That is useful, and it is also the distribution the field is already searching.

Divergence of ideas is a resource, and this technology may be consuming it (low-to-moderate confidence, and a conjecture rather than a finding).
Nothing in the evidence behind this book measures the diversity of research questions before and after agentic tools arrived.
I am not aware of a study that would settle it cleanly either way.
It is stated here because you should be thinking about it, not because the book knows the answer.

What a group can do is small and worth doing anyway.
Notice when every hypothesis in a discussion arrived by the same route.
Keep at least one route that does not go through a model: a reading group, a field visit, a conversation with somebody whose data you have never used.
None of that is a check on the field, and none of it scales past the people who do it.
It does keep one group's questions from coming entirely from one distribution.

[AUTHOR: whether you have seen this in practice, or think it is overstated — this is the movement in the section most in need of your judgement.]

**The third — deskilling and the supply of judgement.**
A month of hand-reconciling a gauge network teaches a doctoral researcher three things.
They learn what a stuck sensor looks like in a time series, how a station move shows up as a step change, and which odd values are worth chasing.
None of that is in the specification.
It is what lets somebody tell a real signal from a sensor fault.
That is exactly the judgement the propose–dispose separation reserves for a person (Chapter 2 §2.6, on the criteria only a human decision can settle).
It was acquired by doing work an agent now does in an afternoon.

The verification-first stance of this whole book depends on that judgement and has nowhere said where it comes from.
Chapter 16 §16.4 says the skills these roles need are largely those a good empirical scientist already has, which is true.
It also assumes a continuing supply of scientists who acquired them the slow way.
So a group leader deciding what a doctoral researcher spends three years on is deciding the group's future capacity to verify, not only this year's throughput.
That is the book's argument rather than a measured effect (moderate confidence).
The consequence of that decision arrives years later, and it gets made by default when it is not made deliberately.

What a group can do is name the judgements it intends to keep in-house, and protect the work that builds them even where an agent would be faster.
A month of hand-reconciliation, kept deliberately on the grounds that it is training rather than production, is a defensible use of a doctoral student's time.
Nothing in the evidence behind this book measures skill acquisition under agentic assistance, and no source is offered here.

**The fourth — automation bias in the human.**
The report on the screen is the fourth agent-drafted quality-control report of the afternoon.
The first three were fine.
This one looks like the first three, and the reviewer approves it.
The approval was not a judgement about this report.
It was a judgement about the first three.
Nothing in that sequence is negligence, and the same sequence will run again next week.
The book's model of the human throughout has been a tireless sceptical verifier, and real people under deadline approve work that looks right.

The gallery has a mode for the agent being over-agreeable (§13.5) and none for the person being over-agreeable, and the second is the commoner failure.
It also defeats every other check in the book, because every gate here passes through a person at some point.
A human disposes wherever the criterion is judgement, and a human decides whether a seeded-defect result warrants changing anything.
And it leaves no trace: a rubber-stamp review produces the same record as a searching one (Chapter 12 §12.4, on what a coverage record cannot establish).

So measure it, exactly as any other gate is measured (Chapter 11 §11.5, on seeded defects in a human reviewer's queue and yield watched on human approvals).
Then design against it.
A gate that asks the reviewer to state in one line what they checked costs seconds and makes a cheap approval visibly cheap.
A gate offering an approve button records nothing about whether anybody looked.
Neither measure is a solution, and both are cheaper than the failure.
Confidence is high that the mechanism is real, since it is the ordinary behaviour of people doing repetitive checking work under time pressure.
It is moderate that these countermeasures work, since nothing in the evidence behind this book measures either.

What the four have in common is where the check would have to sit.
It has to sit outside the group, not merely outside the workflow, which is all every mode above asks for.
Correlated verification error is invisible from inside one group by construction.
So is a narrowing of the questions, a slow loss of judgement, or a reviewer who has stopped reading.
The institution that has historically played that outside role is peer review.
Chapter 17 takes up what it can and cannot do when the work under review was produced with agents.

---

### References (verify details before release)

- Ansari, M. S. (2026). Compound deception in elite peer review: a failure mode taxonomy of 100 fabricated citations at NeurIPS 2025. *arXiv preprint* **[verify]**. https://arxiv.org/abs/2602.05930
- Cabezas-Clavijo, Á., & Sidorenko-Bautista, P. (2025). Assessing the performance of 8 AI chatbots in bibliographic reference retrieval. *arXiv preprint*; to appear in *Journal of Data and Information Science* (2026) **[verify]**. https://arxiv.org/abs/2505.18059
- Cemri, M., Pan, M. Z., Yang, S., et al. (2025). Why do multi-agent LLM systems fail? *arXiv preprint* **[verify venue]**. https://arxiv.org/abs/2503.13657
- Davis, D. (2026). "Claude Confidently Skipped Half Your Document and Didn't Tell You." Video, @dylandavisai, 16 May 2026. https://www.youtube.com/watch?v=ueNx7Wj9Rx4 (practitioner commentary; concepts cited as corroboration, not evidence)
- Huang, L., Yu, W., et al. (2023). A survey on hallucination in large language models: principles, taxonomy, challenges, and open questions. *arXiv preprint*; journal version in *ACM Transactions on Information Systems* (2025) **[verify journal DOI]**. https://arxiv.org/abs/2311.05232
- Sharma, M., Tong, M., Korbak, T., Duvenaud, D., Askell, A., Bowman, S. R., et al. (2023). Towards understanding sycophancy in language models. *ICLR 2024*. https://arxiv.org/abs/2310.13548
- Walters, W. H., & Wilder, E. I. (2023). Fabrication and errors in the bibliographic citations generated by ChatGPT. *Scientific Reports*, 13, 14045. https://doi.org/10.1038/s41598-023-41032-5
- Wataoka, K., Takahashi, T., & Ri, R. (2024). Self-preference bias in LLM-as-a-judge. *arXiv preprint* **[verify venue]**. https://arxiv.org/abs/2410.21819
- Zheng, L., Chiang, W.-L., Sheng, Y., et al. (2023). Judging LLM-as-a-judge with MT-Bench and Chatbot Arena. *NeurIPS 2023 Datasets and Benchmarks Track*. https://arxiv.org/abs/2306.05685
