# Chapter 10 — Multi-agent workflows

> **Status:** draft r5 · voice v5.0 (`STYLE.md` §1) · sentence-per-line per `STYLE.md` §10 · figures as briefs per `FIGURES.md`.
> **Conventions:** vendor-neutral (outline §9) · **[AUTHOR: …]** marks lived material only the author can supply · **[verify]** marks real but unconfirmed details · citations drawn only from verified reports in `/research`. Nothing has been invented.
> **This chapter** is the Part II capstone: it composes the single-agent patterns of Chapters 5–9 and hands the resulting apparatus to the end-to-end case study of Chapter 15.

> **[ai-reviewer: A1 review — 1 comment in this file.** Task 10.1 landed and stayed inside its brief: three sentences, roughly 55 words, no citation added, no development of the field-scale argument that belongs to Ch. 13 §13.9. §10.4 to §10.6 are untouched and the ai-reviewer placement note at line 71 is intact as instructed. Checked and found sound: the forward reference names its destination and what is at it, per `STYLE.md` §5.6, and the mechanism it asserts is the one Wataoka et al. (2024) already supports two sentences above, so nothing is claimed here that the chapter's own evidence does not carry. No comment beyond this header.**]**

---

## 10.1 The problem: more agents is not more rigour

If one agent improves a workflow, surely several will improve it more.
That intuition is natural, and this chapter exists to discipline it.

The five preceding chapters each built a single-agent pattern (synthesis, acquisition and quality control, coding, orchestration, drafting), and each closed the loop between an instruction and a verified result with one agent working inside specified boundaries.
The obvious next move, and the one commercial framing actively encourages, is to compose those patterns into a standing team of agents passing work to one another: a planner that decomposes the task, specialists that execute the parts, a critic that reviews the whole, a manager that reconciles the outputs.
Such teams are easy to build with current tooling and they demonstrate impressively, because a transcript of several agents conferring reads as diligence.
The trouble is that looking diligent and being rigorous are not the same thing, and multi-agent teams pull the two apart more readily than single agents do.
Four agents built on the same model, given the same context, agreeing with each other, have not checked the work four times.
They have checked it once and echoed it three times, at four times the token cost and several times the latency, while presenting something that looks like independent corroboration.

The evidence is not kind to the intuition.
A 2025 analysis of more than two hundred execution traces across seven popular multi-agent frameworks found such systems often gain little over a single agent.
The finding that deserves most emphasis is where their failures came from: not weak models, but poor task specification and absent or weak verification (Cemri et al., 2025).
A separate methodological critique showed a plain model wrapped in a simple retry loop can match elaborate agent architectures on standard coding benchmarks at a fraction of the cost (Kapoor et al., 2024).
So the question here is not how to orchestrate many agents.
It is when a second agent adds anything a single well-specified agent and a verification gate did not already provide.
The answer will be familiar to anyone who works with ensembles.
Extra agents earn their cost when their errors are genuinely independent of the errors they are meant to catch, and they add only latency, expense and false assurance when their errors are correlated with the ones they are checking.
State the limitation at the outset: independence is far harder to engineer than to assert, and most multi-agent designs that claim it do not have it (high confidence in the principle; the engineering is where practice fails).

## 10.2 The conventional workflow: distributed cognition in science

Science already spreads cognitive labour across independent parties, and almost all the value of doing so comes from the independence rather than from the number of people involved.

A modelling study of any consequence is not the product of one mind.
It passes through co-authors with distinct expertise, internal read-throughs before submission, two or three referees who never saw each other's reports, and an editor who reconciles them.
That structure catches errors not because many people looked, but because the people who looked had different training, different priors, different stakes and no sight of each other's conclusions, so their mistakes do not coincide.
A hydrologist and a statistician reading the same manuscript miss different things.
Two hydrologists from the same tradition, reading in sequence with the first's marked-up copy in front of the second, tend to miss the same things and to reinforce each other's confidence in what they missed.
The discipline has names for the arrangement that works, such as the four-eyes principle, independent replication and blinded review, and each name encodes the same insight: the checking party has to be shielded from the checked party's reasoning if the check is to be worth its cost.
Less visibly, the conventional workflow also encodes accountability: at each handoff a named person owns the artefact and answers for it, the referee advises but does not decide, and the editor decides but does not author.

All of that bears directly on agent design, and it is the organising claim of the chapter.
A roster of agents is an attempt to reproduce, in software and at speed, the distributed-cognition structure science already uses.
It will reproduce the benefit only if it reproduces the property that makes the human structure work: genuine independence between the party producing an output and the party checking it, not merely the number of parties.
Carry the qualification forward, though.
The human structure earns its independence through deep, expensive differences between people, and a set of agents sharing a model and a context does not get those differences for free.
They have to be engineered in (high confidence).

> **Definition — Roster.** A small, fixed set of agents with distinct jobs: a producer that performs the work, an independent reviewer that checks it, and a human who decides, arranged so that work passes between them through defined checks. The term borrows from a team sheet: named roles that answer for their part, not an undifferentiated crowd.

## 10.3 The discriminating question: independence versus correlated opinion

One question should govern every decision to add an agent: are the new agent's errors statistically independent of the errors it is brought in to catch?
The whole benefit of a second opinion depends on that independence and on nothing else.

The intuition is the one behind ensemble forecasting, which will be familiar.
An ensemble reduces error only to the extent that its members are not making the same mistake at the same time, and an ensemble whose members share an initialisation, a resolution and a parametrisation collapses towards a single trajectory that is confidently wrong in unison.
Agents built from one underlying model, prompted with overlapping context and asked to reason in the same register, are the software equivalent of that collapsed ensemble.
Their failure modes come from the same distribution, so where one hallucinates a citation, misreads a unit or accepts a flawed premise, the others are disproportionately likely to do the same and, worse, to ratify it.
This is not an analogy offered without evidence.
When independent model instances propose answers and then critique one another, factual accuracy improves and hallucinated content falls, including when the instances come from different model families (Du et al., 2024); but the same work is a warning, because debate converges on *consensus*, and consensus is not correctness.
Instances of a similar model can agree on a shared error exactly as an under-dispersed ensemble does.
So a reviewer agent adds real assurance in proportion to how much it differs from the agent it reviews, and the things that create difference are concrete rather than rhetorical.
A different underlying model, where one is available.
A deliberately narrowed context, so the reviewer does not inherit the drafter's framing.
An adversarial instruction that rewards finding faults rather than confirming adequacy.
And access to an independent source of truth, such as a test suite, a schema or a reference dataset, that the reviewer checks claims against rather than re-reasoning them.
The pull towards the cheapest configuration, drafting and reviewing with the same model family, is precisely the trap: judge models systematically prefer text that is familiar to them, rating outputs from their own family more highly than a human would (Wataoka et al., 2024), so genuine independence needs model diversity, not merely a fresh context window.
A 2026 evaluation at scale (21 judge models, some 541,000 judgements) sharpens the warning: exact-match agreement overstates chance-corrected agreement by 33 to 41 percentage points, and a judge can be highly self-consistent whilst carrying severe position bias, so a reviewer can be dependably wrong in a fixed direction and its self-consistency is no evidence of soundness (Norman, Rivera and Hughes, 2026; a preprint, on general chat and question-answering benchmarks, not scientific artefacts).
[ai-reviewer: placement note, for the record. Plan task 10.1 anchored this to "the existing Zheng et al. (2023) sentence" in §10.3, but that chapter's Zheng sentence sits in §10.6; the writer attached the Norman qualification to §10.3's Wataoka self-preference sentence instead. Reviewed and endorsed: §10.3 is the independence argument the qualification serves, and adding it at §10.6 would have breached the T2 canonical-home limits. No change needed; noted so the deviation from the written plan is visible to the author.]
Do none of those things and a second agent supplies correlated opinion, which is cost without information.
That gives one test to apply to every proposed agent.
Name the class of error this agent will catch that the existing agents and gates would not, and describe the mechanism that makes its judgement independent of theirs.
If you cannot state both, the agent is decoration, and it should be replaced by a deterministic gate or a human check.
The limitation is that independence is a matter of degree and cannot be measured directly at design time, so this is a discipline for reasoning about a roster rather than a proof of its soundness.
The evaluation methods of Chapter 11 are what turn the design-time argument into a measured claim (moderate-to-high confidence).
The same argument scales past one workflow, and at field scale it is a larger problem.
If most groups run their reviewer agents on one of a small number of base models, the field's verification errors correlate.
Chapter 13 §13.9 develops what that does to independent replication, which is science's actual error-correction mechanism.

> **Definition — Ensemble.** In forecasting, a set of model runs started from slightly different conditions, whose spread is read as the forecast's uncertainty. The spread means something only if the members can genuinely disagree; runs that share too much collapse together and become confidently wrong in unison, the same trap a set of near-identical agents falls into.

**Figure 10.1 — Independence, not multiplicity, is the source of value.**

![A top-to-bottom decision flowchart. A proposed second agent meets a first gate asking whether it names an error class the existing roster and gates would miss; a no exits to a grey terminal reading drop, add a deterministic gate instead. A yes leads to a second gate asking whether its judgement is genuinely independent of the agent it checks, with a callout listing the four things that create independence: a different model, a narrowed context, an adversarial brief, and an external source of truth. A no again exits to drop, annotated that without one of those four the second agent supplies correlated opinion, which is cost without information. A yes reaches an orange terminal, keep, marked with a purple reviewer icon. A footnote reads that four agents on one model agreeing have checked the work once and echoed it three times.](../figures/figure-10-1.svg)

*Figure 10.1 — Two questions before you add an agent. It has to catch a class of error nothing else in the roster would, and its judgement has to be independent of the thing it is checking. Independence takes one of four deliberate design moves. Fail either and you have bought latency and tokens for correlated opinion: four agents on one model agreeing have checked the work once and echoed it three times. (Rendered as `figures/figure-10-1.svg` from the brief below, per `FIGURES.md`.)*

```
FIGURE BRIEF
- id:            Figure 10.1
- title:         When a second agent adds information, and when it adds only cost
- type:          decision flowchart
- claim:         A second agent is worth its latency and token cost only when its errors are independent of the agent it checks; correlated agents add cost without information.
- standfirst:    Agreement between near-identical agents is not corroboration.
- canvas:        16:9
- elements:      a start node "proposed second agent" (grey); a first vermillion diamond
                 "names an error class the roster misses?"; a second vermillion diamond
                 "judgement independent of the checked agent?"; an orange terminal "keep —
                 independent reviewer" carrying a purple reviewer icon; a grey terminal
                 "drop — add a deterministic gate instead"
- flow:          top-to-bottom. proposed second agent → gate 1. Gate 1 "no" → drop. Gate 1
                 "yes" → gate 2. Gate 2 "no" → drop. Gate 2 "yes" → keep
- labels:        "proposed second agent", "names an error class the roster misses?",
                 "judgement independent of the checked agent?", "keep — independent
                 reviewer", "drop — add a deterministic gate instead", "yes", "no"
- annotations:   beside gate 2, a callout listing "different model · narrowed context ·
                 adversarial brief · external source of truth"; on the "no" exits, "without
                 one of those, a second agent supplies correlated opinion — cost without
                 information"; on the "drop" terminal, "if a rule can check it, a gate is
                 cheaper and more reliable than an agent"; a footnote, "four agents on one
                 model agreeing have checked the work once and echoed it three times"
- caption:       Figure 10.1 — Two questions before you add an agent. It has to catch a class of error nothing else in the roster would, and its judgement has to be independent of the thing it is checking. Independence takes one of four deliberate design moves. Fail either and you have bought latency and tokens for correlated opinion: four agents on one model agreeing have checked the work once and echoed it three times.
- alt-text:      A top-to-bottom decision flowchart. A proposed second agent meets a first gate asking whether it names an error class the existing roster and gates would miss; a no exits to a grey terminal reading drop, add a deterministic gate instead. A yes leads to a second gate asking whether its judgement is genuinely independent of the agent it checks, with a callout listing the four things that create independence: a different model, a narrowed context, an adversarial brief, and an external source of truth. A no again exits to drop, annotated that without one of those four the second agent supplies correlated opinion, which is cost without information. A yes reaches an orange terminal, keep, marked with a purple reviewer icon. A footnote reads that four agents on one model agreeing have checked the work once and echoed it three times.
- infographic description: A flat vector decision flowchart on an off-white background,
                 16:9, top to bottom. Title top-left: "When a second agent adds information,
                 and when it adds only cost". Standfirst beneath: "Agreement between
                 near-identical agents is not corroboration." A grey rounded rectangle
                 "proposed second agent" at the top connects down to a vermillion diamond
                 "names an error class the roster misses?". Its "no" exit leads right to a
                 grey terminal "drop — add a deterministic gate instead", annotated "if a
                 rule can check it, a gate is cheaper and more reliable than an agent". Its
                 "yes" exit leads down to a second vermillion diamond "judgement independent
                 of the checked agent?", with a callout in a pale yellow fill beside it
                 listing four items on separate lines: "different model", "narrowed
                 context", "adversarial brief", "external source of truth". This diamond's
                 "no" exit joins the same grey terminal, with the shared annotation "without
                 one of those, a second agent supplies correlated opinion — cost without
                 information". Its "yes" exit leads down to an orange terminal "keep —
                 independent reviewer" carrying a small purple head-and-shoulders-with-tick
                 icon. A footnote along the bottom reads "four agents on one model agreeing
                 have checked the work once and echoed it three times". Generous spacing,
                 sentence case.
```

## 10.4 The agentic redesign: roles, rosters and gates

What follows from the independence principle is not a bigger crowd of agents but a small roster of clearly distinct roles separated by gates, with a human holding the accountable position.

Three role types recur across scientific rosters, and they are worth naming because their distinctness is what supplies the independence.
A **producer** carries the transformational work, such as drafting a synthesis, writing pipeline code or assembling a manuscript section, and corresponds to the single-agent patterns of Chapters 5 to 9.
An **independent reviewer**, developed for code in Chapter 7 and generalised here, gets a different and adversarial brief, a narrowed context and, wherever possible, a different model, and is judged by the faults it surfaces rather than by its agreement with the producer.
A **gate** is not an agent at all.
It is a deterministic check, such as a test suite, a schema validation, a citation resolver or a units audit, placed between roles so the cheap mechanical verification is mandatory rather than advisory.
Whenever a proposed check can be written as a rule, prefer a gate to another agent.
Above all of this sits an orchestration function that routes artefacts between roles and enforces the stop conditions, and it should be deliberately thin.
An orchestrator that reasons about the science reintroduces exactly the correlated judgement the roster was built to avoid; one that only sequences steps and applies gates adds coordination without adding opinion.
None of this structure is new.
Conversation-structured multi-agent frameworks from around 2023 made it a standard way to build agent applications, and, in a point worth borrowing, they treat a human-in-the-loop role as a full member of the roster rather than an afterthought (Wu et al., 2023).
The human decision point carries the weight, placed wherever accountability, interpretation or authorship is at stake, meaning the boundaries drawn in Chapter 4, because no arrangement of agents, however independent, discharges the answerability Chapter 1 identified as non-transferable.
Two design rules tie the roster together.
Independence has to be engineered at every producer–reviewer boundary, and every loop has to terminate.
Reviewers that can send work back to producers create cycles, and a cycle without a bounded iteration count and an escalation path is a cost blow-out and a diffusion-of-responsibility failure waiting to happen (§10.6).
Who produced, who reviewed and who decided gets recorded at each handoff, feeding the audit trail Chapter 12 specifies.
A roster whose internal handoffs are not logged cannot later be shown to have checked what it claims to have checked (high confidence in the structure; the thin-orchestrator claim is moderate confidence and workload-dependent).
Set beside the conventional arrangement of §10.2, the redesign keeps what made distributed human review work, meaning independence between producer and checker and a named party accountable at each boundary, while replacing serial handoffs measured in days with gated handoffs measured in minutes.
Figure 10.3 puts the two side by side so the shared structure and the compressed timescale are both legible at once.

> **Definition — Independent reviewer.** An agent whose only job is to find faults in another agent's work, set up so that its judgement does not simply echo the producer's: a different model where possible, a deliberately narrower view of the task, an instruction that rewards catching problems, and its own source of truth to check against. Independence is the whole point: a reviewer that shares the producer's model and context mostly agrees with it.

**Figure 10.2 — A minimal scientific roster.**

![An architecture diagram. A thin orchestrator bar spans the top, labelled sequences and enforces stop conditions, annotated deliberately thin, because an orchestrator that reasons about the science reintroduces the correlated judgement the roster exists to avoid. Below it, left to right: a specification tag; a producer agent with tools and a data store; a deterministic gate listing tests, schema, citations and units, annotated that anything a rule can check is a gate rather than an agent; an independent reviewer annotated with the three things that make it independent, a different model, a narrowed context and an adversarial brief; a second gate; and a human decision point annotated that accountability, interpretation and authorship stay here. A single fail arrow returns from the reviewer to the producer, labelled bounded iterations, then escalate.](../figures/figure-10-2.svg)

*Figure 10.2 — A roster is small, and every element earns its place. A producer does the work, deterministic gates catch anything a rule can settle, one independent reviewer handles what a rule cannot, and a human owns the decision. Two details carry the design: the orchestrator is deliberately thin, and the return loop is bounded so it escalates rather than churning. (Rendered as `figures/figure-10-2.svg` from the brief below, per `FIGURES.md`.)*

```
FIGURE BRIEF
- id:            Figure 10.2
- title:         A minimal roster — producer, gates, independent reviewer, human decision
- type:          architecture
- claim:         A scientific roster is a small set of distinct roles separated by deterministic gates, with independence engineered at the producer–reviewer boundary and a human holding the accountable decision.
- standfirst:    Small, and every element traces back to a clause somebody wrote.
- canvas:        16:9
- elements:      a thin grey "orchestrator" bar spanning the top; below it, left to right, a
                 "specification" tag (blue); a "producer agent" rounded rectangle (orange)
                 with a "tools" glyph (green) and a "data store" cylinder (sky blue); a
                 deterministic "gate" diamond (vermillion); an "independent reviewer"
                 rounded rectangle (reddish purple); a second gate; a blue "human decision"
                 head-and-shoulders icon
- flow:          left-to-right — specification → producer → gate → independent reviewer →
                 gate → human decision; a single "fail" return arrow runs from the reviewer
                 back to the producer
- labels:        "orchestrator — sequences, enforces stop conditions", "specification",
                 "producer agent", "tools", "data store", "gate",
                 "tests · schema · citations · units", "independent reviewer",
                 "different model · narrowed context · adversarial brief", "human decision",
                 "fail — bounded iterations, then escalate"
- annotations:   on the orchestrator bar, "deliberately thin — an orchestrator that reasons
                 about the science reintroduces the judgement the roster exists to avoid";
                 on the gate, "anything a rule can check is a gate, not an agent"; on the
                 reviewer, "independence engineered here, not hoped for"; on the return
                 arrow, "bounded, or it becomes a cost blow-out and nobody owns the miss";
                 on the human node, "accountability, interpretation and authorship stay
                 here"; a footer, "every role on this diagram traces back to a clause of
                 the specification"
- caption:       Figure 10.2 — A roster is small, and every element earns its place. A producer does the work, deterministic gates catch anything a rule can settle, one independent reviewer handles what a rule cannot, and a human owns the decision. Two details carry the design: the orchestrator is deliberately thin, and the return loop is bounded so it escalates rather than churning.
- alt-text:      An architecture diagram. A thin orchestrator bar spans the top, labelled sequences and enforces stop conditions, annotated deliberately thin, because an orchestrator that reasons about the science reintroduces the correlated judgement the roster exists to avoid. Below it, left to right: a specification tag; a producer agent with tools and a data store; a deterministic gate listing tests, schema, citations and units, annotated that anything a rule can check is a gate rather than an agent; an independent reviewer annotated with the three things that make it independent, a different model, a narrowed context and an adversarial brief; a second gate; and a human decision point annotated that accountability, interpretation and authorship stay here. A single fail arrow returns from the reviewer to the producer, labelled bounded iterations, then escalate.
- infographic description: A flat vector architecture diagram on an off-white background,
                 16:9. Title top-left: "A minimal roster — producer, gates, independent
                 reviewer, human decision". Standfirst beneath: "Small, and every element
                 traces back to a clause somebody wrote." A thin grey bar spans the top
                 labelled "orchestrator — sequences, enforces stop conditions", annotated
                 "deliberately thin — an orchestrator that reasons about the science
                 reintroduces the judgement the roster exists to avoid". Below it, a
                 left-to-right chain: a blue tag "specification"; an orange rounded
                 rectangle "producer agent" with a green "tools" glyph and a sky-blue "data
                 store" cylinder attached; a vermillion diamond "gate" with sub-text "tests
                 · schema · citations · units", annotated "anything a rule can check is a
                 gate, not an agent"; a reddish-purple rounded rectangle "independent
                 reviewer" with sub-text "different model · narrowed context · adversarial
                 brief", annotated "independence engineered here, not hoped for"; a second
                 vermillion diamond "gate"; and a blue head-and-shoulders icon "human
                 decision", annotated "accountability, interpretation and authorship stay
                 here". A single arrow labelled "fail — bounded iterations, then escalate"
                 runs from the reviewer back to the producer, annotated "bounded, or it
                 becomes a cost blow-out and nobody owns the miss". A footer line reads
                 "every role on this diagram traces back to a clause of the specification".
                 Generous spacing, sentence case.
```

**Figure 10.3 — Conventional review and agentic roster, side by side.**

![Two lanes sharing one left-to-right grammar. The top lane shows conventional review: an author, an internal read-through, two independent referees and an editor who decides, marked as serial and taking weeks. The bottom lane shows the agentic roster: a producer agent, a gate, an independent reviewer, a second gate and a human decision, marked as gated and taking minutes, with the human still owning the decision. Dotted vertical lines link the matching roles, author to producer, referees to independent reviewer, editor to human decision. A note reads that what carries over is independence and accountability, not the number of parties.](../figures/figure-10-3.svg)

*Figure 10.3 — Science already runs the structure a roster copies. Author, independent referees and a deciding editor line up with producer, independent reviewer and human decision, and the dotted lines mark the correspondence. What changes is the clock, from weeks of serial handoffs to minutes of gated ones. What must not change is on the alignment lines: independence and accountability, not headcount. (Rendered as `figures/figure-10-3.svg` from the brief below, per `FIGURES.md`.)*

```
FIGURE BRIEF
- id:            Figure 10.3
- title:         Distributed human review and its agentic roster share one grammar
- type:          before/after
- claim:         A roster reproduces the independence structure of conventional distributed review (producer, independent checker, accountable decider) but compresses serial handoffs of days into gated handoffs of minutes.
- standfirst:    Same structure science already uses; a different clock.
- canvas:        16:9
- elements:      an upper "conventional" lane and a lower "agentic roster" lane sharing a
                 left-to-right grammar. Upper: "author" (blue human) → "internal
                 read-through" (blue human) → "independent referees ×2" (blue humans) →
                 "editor decides" (blue human). Lower: "producer agent" (orange) → "gate"
                 (vermillion) → "independent reviewer" (purple) → "gate" (vermillion) →
                 "human decision" (blue)
- flow:          two stacked left-to-right lanes read in parallel; dotted vertical
                 alignment lines connect author↔producer, referees↔independent reviewer,
                 editor↔human decision
- labels:        "conventional", "author", "internal read-through",
                 "independent referees ×2", "editor decides", "serial — weeks",
                 "agentic roster", "producer agent", "gate", "independent reviewer",
                 "human decision", "gated — minutes"
- annotations:   on the upper lane end, "serial — weeks"; on the lower lane end, "gated —
                 minutes; the human still owns the decision"; on the three alignment
                 lines, "producer", "independent checker", "accountable decider"; a
                 footer, "what carries over is independence and accountability — not the
                 number of parties"
- caption:       Figure 10.3 — Science already runs the structure a roster copies. Author, independent referees and a deciding editor line up with producer, independent reviewer and human decision, and the dotted lines mark the correspondence. What changes is the clock, from weeks of serial handoffs to minutes of gated ones. What must not change is on the alignment lines: independence and accountability, not headcount.
- alt-text:      Two lanes sharing one left-to-right grammar. The top lane shows conventional review: an author, an internal read-through, two independent referees and an editor who decides, marked as serial and taking weeks. The bottom lane shows the agentic roster: a producer agent, a gate, an independent reviewer, a second gate and a human decision, marked as gated and taking minutes, with the human still owning the decision. Dotted vertical lines link the matching roles, author to producer, referees to independent reviewer, editor to human decision. A note reads that what carries over is independence and accountability, not the number of parties.
- infographic description: A flat vector before-and-after diagram, 16:9, off-white
                 background. Title top-left: "Distributed human review and its agentic
                 roster share one grammar". Standfirst: "Same structure science already
                 uses; a different clock." Two stacked left-to-right lanes with aligned
                 columns. Upper lane "conventional": blue human icons "author", "internal
                 read-through", "independent referees ×2", "editor decides", joined by
                 arrows, ending in the tag "serial — weeks". Lower lane "agentic roster":
                 an orange rounded square "producer agent", a vermillion diamond "gate", a
                 purple reviewer icon "independent reviewer", a second vermillion "gate",
                 a blue human "human decision", ending in the tag "gated — minutes; the
                 human still owns the decision". Three dotted vertical lines link the
                 matching columns, labelled "producer", "independent checker",
                 "accountable decider". Footer: "what carries over is independence and
                 accountability — not the number of parties". Sentence case throughout.
```

## 10.5 Worked example: deriving a roster from a specification

The safest way to arrive at a roster is not to design the team and then find work for it.
It is to derive the team mechanically from the workflow specification, so every role and gate traces back to a clause a human wrote and can audit.

The specification schema of Chapter 3 gives four fields that map onto roster elements with little slack, and reading the derivation in that direction, specification first and roster second, is what keeps a roster minimal.
A role no clause of the specification demands is a role that should not exist.
The **objective** fixes the producer roles: a single, well-bounded objective needs one producer, and a genuinely separable objective (a synthesis stage whose output a distinct modelling stage consumes, say) justifies a second producer only where the two demand different tools or different evidence, not merely because the work is long.
The **inputs** fix tool and data-store access and, by their sensitivity, where the governance constraints of Chapter 12 attach: inputs that touch credentialled institutional systems or partner data restrict which roles may hold which permissions, so least-privilege access is assigned per role rather than to the roster as a whole (Chapter 12).
The **acceptance criteria** are the richest source of structure, because each criterion is sorted into either a deterministic gate or an independent-reviewer responsibility by a single question: can a rule check it?
A criterion such as "all cited references resolve to real documents" or "the units in every derived field are dimensionally consistent" becomes a gate; a criterion such as "the synthesis represents the disagreement in the literature fairly" cannot be reduced to a rule and becomes the brief for an independent reviewer, whose adversarial framing is written straight from the criterion.
The **stop conditions** fix the orchestrator's loop bounds and the escalation path: the maximum number of producer–reviewer iterations, the token or wall-clock budget beyond which the roster halts, and the point at which unresolved disagreement goes to the human decision node rather than being churned further.
Worked through on a concrete operational specification, that mapping gives a small, auditable roster in which every element has a provenance in the specification and nothing is there for appearance's sake **[AUTHOR: insert a specification you have actually written — the rainfall-forecast verification specification from Chapter 3 is the natural candidate — and show the exact roster it produced, including the criteria you triaged to gates versus to the reviewer, the iteration bound you set, and any role you initially added and then removed as correlated. The executed version of this derivation is the spine of Chapter 15; this section should foreshadow it, not pre-empt its results.]**
The mapping is only as good as the specification, and that limitation is worth stating.
A vague acceptance criterion produces a vague reviewer brief and a roster no more rigorous than the words it came from.
That is how specification quality (Chapter 3) governs roster quality, and why the two chapters belong together (high confidence in the mapping; the operational specifics await the author's executed material).

**Figure 10.4 — From specification to roster.**

![Four blue specification fields stacked on the left, objective, inputs, acceptance criteria and stop conditions, each joined by a numbered arrow to the roster element it produces on the right: producer roles; tool and data access under least privilege; gates for the rule-checkable criteria plus a reviewer brief for the judgement ones; and the loop bound with its escalation path. The third mapping carries the sorting question, can a rule check it, gate if yes, reviewer if not. The fourth is annotated as what bounds cost and stops responsibility diffusing. A footer reads that a role no clause demands is a role that should not exist.](../figures/figure-10-4.svg)

*Figure 10.4 — The roster is derived, not designed. Each field of the Chapter 3 specification produces its own roster element, so every role and gate traces back to a clause a person wrote and can audit. The third mapping does the sorting: anything a rule can check becomes a gate, and only what needs judgement earns a reviewer. A role no clause demands should not exist. (Rendered as `figures/figure-10-4.svg` from the brief below, per `FIGURES.md`.)*

```
FIGURE BRIEF
- id:            Figure 10.4
- title:         Deriving a roster from the specification schema
- type:          sequence
- claim:         Each field of a Chapter 3 specification maps to a specific roster element, so that every role and gate has an auditable provenance in a clause a human wrote.
- standfirst:    Every role traces to a clause somebody wrote. No clause, no role.
- canvas:        16:9
- elements:      four specification fields on the left as blue tags stacked top to bottom
                 — "objective", "inputs", "acceptance criteria", "stop conditions"; four
                 roster outcomes on the right, each reached by a numbered arrow —
                 "producer role(s)" (orange), "tool & data access (least privilege)"
                 (green tool + sky data-store), "gates + reviewer brief" (vermillion gate
                 + purple reviewer), "loop bound + escalation" (grey)
- flow:          top-to-bottom, four numbered mappings read in order: 1 objective →
                 producer role(s); 2 inputs → tool & data access; 3 acceptance criteria →
                 gates + reviewer brief; 4 stop conditions → loop bound + escalation
- labels:        "objective", "inputs", "acceptance criteria", "stop conditions",
                 "producer role(s)", "tool & data access (least privilege)",
                 "gates + reviewer brief", "loop bound + escalation", "1", "2", "3", "4"
- annotations:   on mapping 1, "one bounded objective, one producer"; on mapping 2,
                 "access assigned per role, never to the roster as a whole"; on mapping 3,
                 "can a rule check it? gate if yes; reviewer brief if not"; on mapping 4,
                 "bounds cost, and stops responsibility diffusing"; a footer, "a role no
                 clause of the specification demands is a role that should not exist"
- caption:       Figure 10.4 — The roster is derived, not designed. Each field of the Chapter 3 specification produces its own roster element, so every role and gate traces back to a clause a person wrote and can audit. The third mapping does the sorting: anything a rule can check becomes a gate, and only what needs judgement earns a reviewer. A role no clause demands should not exist.
- alt-text:      Four blue specification fields stacked on the left, objective, inputs, acceptance criteria and stop conditions, each joined by a numbered arrow to the roster element it produces on the right: producer roles; tool and data access under least privilege; gates for the rule-checkable criteria plus a reviewer brief for the judgement ones; and the loop bound with its escalation path. The third mapping carries the sorting question, can a rule check it, gate if yes, reviewer if not. The fourth is annotated as what bounds cost and stops responsibility diffusing. A footer reads that a role no clause demands is a role that should not exist.
- infographic description: A flat vector mapping diagram, 16:9, off-white background.
                 Title top-left: "Deriving a roster from the specification schema".
                 Standfirst: "Every role traces to a clause somebody wrote. No clause, no
                 role." Left column: four blue tags stacked with generous spacing —
                 "objective", "inputs", "acceptance criteria", "stop conditions". Right
                 column: four outcome blocks aligned with them — an orange rounded square
                 "producer role(s)"; a green wrench beside a sky-blue cylinder "tool &
                 data access (least privilege)"; a vermillion diamond beside a purple
                 reviewer icon "gates + reviewer brief"; a grey rounded rectangle "loop
                 bound + escalation". Four numbered straight arrows join the pairs, each
                 with its annotation beneath: "1 · one bounded objective, one producer";
                 "2 · access assigned per role, never to the roster as a whole"; "3 · can
                 a rule check it? gate if yes; reviewer brief if not"; "4 · bounds cost,
                 and stops responsibility diffusing". Footer: "a role no clause of the
                 specification demands is a role that should not exist". Sentence case.
```

## 10.6 Failure modes

With one exception, multi-agent workflows do not fail in new ways.
They fail in the single-agent ways of the preceding chapters, amplified by composition, and naming them precisely is what lets a roster be designed against them.
The empirical taxonomy sorts them into three families: poor task and role specification, inter-agent misalignment such as miscommunication and lost context, and absent, weak or premature verification (Cemri et al., 2025).
The modes below map onto those families almost one to one.

**Over-agreeable review** is the most common and the most dangerous, because it defeats the whole purpose of the roster while leaving its diligent appearance intact.
A reviewer agent built on the same model as the producer, given the producer's full context and a neutral brief, tends to ratify rather than challenge, and its agreement gets read as corroboration when it is really correlation.
That the tendency is systematic and not incidental is well documented by now: judge models carry characterised biases towards self-preference, verbosity and answer position (Zheng et al., 2023).
The anatomy of the failure, with a worked trace, is Chapter 13's business.
What matters here is the countermeasure, which is the independence engineering of §10.3: different model, narrowed context, adversarial brief, external source of truth.
The diagnostic is a reviewer that almost never returns a fault.
For real scientific work that is evidence of a broken reviewer, not a flawless producer [AUTHOR: your observed base rate of substantive faults from a well-configured reviewer versus a naive one would quantify this; report it if you have it].
**Diffusion of responsibility** is the organisational failure: an error passes through several agents, every one of which could have caught it, and afterwards nobody owns the miss because responsibility was never located at a named human.
The roster avoids it only by putting an accountable human decision point at every boundary where interpretation or consequence is at stake, exactly as Chapter 4 requires.

**Cost blow-out** is the economic failure.
It comes from unbounded producer–reviewer loops, from orchestrators that reason verbosely, and from the token cost of every agent re-reading a growing shared context.
A roster that iterates without a hard bound can spend many times a single agent's cost while converging on nothing, which is why every loop carries an iteration count, a budget and an escalation path (§10.5), and why the honest accounting of Chapter 16 treats roster cost as a first-order design constraint rather than a footnote.

**Correlated errors** are the statistical failure underneath the others.
Agents drawn from the same model share a failure distribution, so a mistake one makes the others are disproportionately likely to repeat and to endorse, and multiplicity then manufactures false confidence.
That is the collapsed-ensemble problem of §10.3 in operational form.

Two more modes deserve mention.
Context contamination happens when a reviewer inherits the producer's framing through a shared context window and loses the very independence it was added to supply, which is why narrowed context matters rather than being a nicety.
Emergent miscoordination happens when thin specifications let agents negotiate scope among themselves, drifting from the objective in ways no single transcript makes obvious.
The defence is the specification-first derivation of §10.5, which leaves agents nothing to invent.

One caution belongs with these modes: telling which step actually caused a failure is itself hard.
Post-hoc review tends to blame the step where the failure surfaced rather than the one that caused it, because later steps inherit an earlier corrupted state; a 2026 preprint built a method purpose-designed for this and still reached only 29 to 46% step-level accuracy where the cause was known, which puts the difficulty in the problem, not the reviewer's diligence (Rafi et al., 2026; a preprint).
The same year's work also names a category the per-agent view misses, namely emergent collective failures no single agent's transcript explains, but shown only in simulated economic and social settings, so it is cited here for the concept, not as domain evidence (Tang et al., 2026).

All these countermeasures share one limitation: they are verified by the methods of Part III rather than guaranteed by the design.
A roster is a hypothesis about independence to be tested, not a proof of it, and the base rates that would show how well a given roster actually checks its own work still await measurement, which is the task Chapter 11 takes up (high confidence in the taxonomy; the base rates await measurement).

## 10.7 Verification checklist

This checklist certifies that a roster is worth its cost before you trust it with work of consequence.
It turns the chapter's single claim, that a roster must supply independence rather than multiplicity, into things a colleague can confirm.
It is written to be applied by someone who did not build the roster, in keeping with the specification-as-control principle of Chapter 3 and the audit requirements of Chapter 12.

- **Every role traces to the specification.** Each producer, gate and reviewer maps to an objective, input, acceptance criterion or stop condition (§10.5); any role without such a provenance is removed. (high confidence)
- **Every second agent passes the independence test.** For each reviewer, the class of error it catches that the gates and other agents would not is named, and its independence mechanism (different model, narrowed context, adversarial brief or external source of truth) is stated (§10.3, Figure 10.1). (high confidence)
- **Rule-checkable criteria are gates, not agents.** Any acceptance criterion a deterministic check can settle is implemented as a gate; a reviewer agent is used only for criteria a rule cannot express (§10.4). (high confidence)
- **Reviewers are configured for independence, and it shows.** Reviewers do not share the producer's full context or model where avoidable, and a well-configured reviewer returns substantive faults at a non-trivial rate; a reviewer that never dissents is treated as broken (§10.6). (moderate-to-high confidence)
- **Every loop is bounded and escalates.** Each producer–reviewer cycle has a maximum iteration count, a token or wall-clock budget, and a defined escalation to a named human on non-convergence (§10.5, §10.6). (high confidence)
- **A human owns each consequential boundary.** Accountability, interpretation and authorship sit at named human decision points, not with the orchestrator or any agent (§10.4, Chapter 4). (high confidence)
- **Handoffs are logged.** Who produced, who reviewed, who gated and who decided is recorded for every artefact, feeding the audit trail (Chapter 12). (high confidence)
- **The roster is costed against the single-agent baseline.** The added latency and token cost of the roster are measured against one agent plus deterministic gates, and the roster is retained only where the added cost buys measured independent checking (§10.6, Chapter 16). (moderate confidence; workload-dependent)

## 10.8 Repository pointer

The companion repository holds the runnable and perishable counterparts to this chapter under the layout of outline §8.
A minimal roster sits under `/patterns` as an executable skeleton to adapt rather than a finished workflow: one producer, one deterministically gated check, one independence-configured reviewer, a thin orchestrator with a bounded loop, and a human-approval step.
The current model and tool bindings are named there, because they date quickly and must not enter the print.
The specification-to-roster derivation of §10.5 sits under `/prompts` as a worked template that consumes a Chapter 3 specification and emits a role-and-gate roster with each element annotated by the clause it derives from, alongside the reviewer-brief patterns that turn a judgement acceptance criterion into an adversarial instruction.
The verification checklist of §10.7 is mirrored under `/checklists` in printable form.
The sanitised configuration of the executed roster behind Chapter 15 will be deposited under `/case-studies` once that chapter's material is settled **[AUTHOR: confirm which operational roster is released as the Chapter 15 case study and what must be sanitised — model bindings, credentials, partner-data references — before it is deposited]**.
If your group is adopting a roster of its own, the thirty-day adoption plan and cost model of Chapter 16 are where to go next, because choosing a roster over a single agent is as much a budgetary and organisational commitment as a technical one.
And the central caution bears one final repetition.
A roster earns its cost only where its agents are independent.
Where they are not, one well-specified agent behind deterministic gates is cheaper, faster and no less rigorous.

---

*Cross-references: the single-agent patterns this chapter composes (Chapters 5–9); when not to reach for an agent at all (Chapter 4); measuring whether a roster actually checks its own work (Chapter 11); the audit trail that logs every handoff (Chapter 12); the anatomy and worked trace of over-agreeable review (Chapter 13); the executed end-to-end roster (Chapter 15); roster cost and how a group starts (Chapter 16).*

## References

- Cemri, M., Pan, M.Z., Yang, S., et al. (2025). "Why Do Multi-Agent LLM Systems Fail?" arXiv preprint. https://arxiv.org/abs/2503.13657 **[verify: archival venue — an OpenReview record exists]**.
- Du, Y., Li, S., Torralba, A., Tenenbaum, J.B. and Mordatch, I. (2024). "Improving Factuality and Reasoning in Language Models through Multiagent Debate." ICML 2024. Preprint: https://arxiv.org/abs/2305.14325.
- Kapoor, S., Stroebl, B., Siegel, Z.S., Nadgir, N. and Narayanan, A. (2024). "AI Agents That Matter." arXiv preprint. https://arxiv.org/abs/2407.01502 **[verify: archival venue]**.
- Norman, J.D., Rivera, M.U. and Hughes, D.A. (2026). "Reliability without Validity: A Systematic, Large-Scale Evaluation of LLM-as-a-Judge Models Across Agreement, Consistency, and Bias." arXiv preprint. https://arxiv.org/abs/2606.19544 **[verify: preprint — not yet peer-reviewed]**.
- Rafi, M.N., Ahasanuzzaman, M., Kim, D.J., Wang, Z. and Chen, T.-H. (2026). "FALAT: Tracing Failures in LLM Agent Trajectories via Dependency-Guided Search." arXiv preprint. https://arxiv.org/abs/2606.00765 **[verify: preprint — not yet peer-reviewed]**.
- Tang, L., Mei, J., Liu, D., Qian, C., Cheng, D., Shao, J. and Hu, X. (2026). "Interpreting Emergent Extreme Events in Multi-Agent Systems." arXiv preprint. https://arxiv.org/abs/2601.20538 **[verify: preprint — not yet peer-reviewed]**.
- Wataoka, K., Takahashi, T. and Ri, R. (2024). "Self-Preference Bias in LLM-as-a-Judge." arXiv preprint. https://arxiv.org/abs/2410.21819 **[verify: peer-reviewed venue]**.
- Wu, Q., Bansal, G., Zhang, J., Wu, Y., et al. (2023). "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation." arXiv preprint. https://arxiv.org/abs/2308.08155 **[verify: peer-reviewed venue — a version appeared at COLM 2024]**.
- Zheng, L., Chiang, W.-L., Sheng, Y., et al. (2023). "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena." NeurIPS 2023 Datasets and Benchmarks Track. Preprint: https://arxiv.org/abs/2306.05685.
