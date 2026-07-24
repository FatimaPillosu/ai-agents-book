# Chapter 10 — Multi-agent workflows

> **Status:** draft r2 · voice v2.0 (`STYLE.md`) · sentence-per-line per `STYLE.md` §10 · figures as briefs per `FIGURES.md`.
> **Conventions:** vendor-neutral (outline §9) · **[AUTHOR: …]** marks lived material only the author can supply · **[verify]** marks real but unconfirmed details · citations drawn only from verified reports in `/research`. Nothing has been invented.
> **This chapter** is the Part II capstone: it composes the single-agent patterns of Chapters 5–9 and hands the resulting apparatus to the end-to-end case study of Chapter 15.

---

## 10.1 The problem: more agents is not more rigour

The intuition this chapter exists to discipline is a natural one: if one agent improves a workflow, surely several will improve it more.
The five preceding chapters each built a single-agent pattern — synthesis, acquisition and quality control, coding, orchestration, drafting — and each closed the loop between an instruction and a verified result with one agent working inside specified boundaries.
The obvious next move, and the one commercial framing actively encourages, is to compose those patterns into a standing team of agents that pass work to one another: a planner that decomposes the task, specialists that execute the parts, a critic that reviews the whole, a manager that reconciles the outputs.
Such teams are easy to build with current tooling and they demonstrate impressively, because a transcript of several agents conferring reads as diligence.
The trouble is that the appearance of diligence and the fact of rigour are not the same thing, and multi-agent teams pull them apart more readily than single agents do.
A workflow in which four agents built on the same model, given the same context, agree with one another has not been checked four times; it has been checked once and echoed three times, at four times the token cost and several times the latency, while presenting a surface that looks like independent corroboration.
The evidence here is not kind to the intuition.
A 2025 analysis of more than two hundred execution traces across seven popular multi-agent frameworks found that such systems often gain little over a single agent, and — the finding that should stay with you — that the largest share of their failures traces not to weak models but to poor task specification and to absent or weak verification (Cemri et al., 2025); a separate methodological critique showed that a plain model wrapped in a simple retry loop can match elaborate agent architectures on standard coding benchmarks at a fraction of the cost (Kapoor et al., 2024).
So the central question of this chapter is not how to orchestrate many agents but when a second agent adds anything a single well-specified agent and a verification gate did not already provide.
The answer, and it will be familiar in its logic to anyone who works with ensembles, is specific: extra agents earn their cost when their errors are genuinely independent of the errors they are meant to catch, and they add only latency, expense and false assurance when their errors are correlated with the ones they are checking.
The limitation to state at the outset is that independence is far harder to engineer than to assert, and most multi-agent designs that claim it do not have it (high confidence in the principle; the engineering is where practice fails).

## 10.2 The conventional workflow: distributed cognition in science

Science already distributes cognitive labour across independent parties, and almost all the value that distribution creates comes from the independence, not from the sheer number of people involved.
A modelling study of any consequence is not the product of one mind: it passes through co-authors with distinct expertise, through internal read-throughs before submission, through two or three referees who never saw one another's reports, and through an editor who reconciles them.
This structure catches errors not because many people looked, but because the people who looked had different training, different priors, different stakes and no sight of each other's conclusions, so their mistakes do not coincide.
A hydrologist and a statistician reading the same manuscript miss different things; two hydrologists from the same tradition, reading in sequence with the first's marked-up copy in front of the second, tend to miss the same things and to reinforce each other's confidence in what they missed.
The discipline has names for the productive arrangement — the four-eyes principle, independent replication, blinded review — and each name encodes the same insight: the checking party must be shielded from the checked party's reasoning if the check is to be worth its cost.
Less visibly, the conventional workflow also encodes an accountability structure: at each handoff a named person owns the artefact and answers for it, the referee advises but does not decide, and the editor decides but does not author.
All of this bears directly on agent design, and it is the organising claim of the chapter.
A roster of agents is an attempt to reproduce, in software and at speed, the distributed-cognition structure science already uses, and it will reproduce the benefit only if it reproduces the property that makes the human structure work — genuine independence between the party producing an output and the party checking it — rather than merely the number of parties.
The qualification to carry forward is that the human structure earns its independence through deep, expensive differences between people, and a set of agents sharing a model and a context does not enjoy those differences automatically; they have to be engineered in (high confidence).

> **In plain terms — Roster.** A small, fixed set of agents with distinct jobs — a producer
> that does the work, an independent reviewer that checks it, a human who decides — arranged
> so that work passes between them through defined checks. The word borrows from a team sheet:
> named roles that answer for their part, not an undifferentiated crowd.

## 10.3 The discriminating question: independence versus correlated opinion

The question that should govern every decision to add an agent is whether the new agent's errors are statistically independent of the errors it is brought in to catch, because the whole benefit of a second opinion depends on that independence and on nothing else.
The intuition is the same one that underlies ensemble forecasting, which this readership knows in its bones: an ensemble reduces error only to the extent that its members are not making the same mistake at the same time, and an ensemble whose members share an initialisation, a resolution and a parametrisation collapses towards a single trajectory that is confidently wrong in unison.
Agents built from one underlying model, prompted with overlapping context and asked to reason in the same register, are the software equivalent of a collapsed ensemble: their failure modes are drawn from the same distribution, so where one hallucinates a citation, misreads a unit or swallows a flawed premise, the others are disproportionately likely to do the same — and, worse, to ratify it.
This is not merely an analogy I am asking you to accept.
When independent model instances propose answers and then critique one another, factual accuracy improves and hallucinated content falls, including when the instances come from different model families (Du et al., 2024); but the same work is a warning, because debate converges on *consensus*, and consensus is not correctness — instances of a similar model can agree on a shared error exactly as an under-dispersed ensemble does.
The practical consequence is that a reviewer agent adds real assurance in proportion to how much it differs from the agent it reviews, and the levers that create difference are concrete rather than rhetorical: a different underlying model where one is available; a deliberately narrowed context so the reviewer does not inherit the drafter's framing; an adversarial instruction that rewards finding faults rather than confirming adequacy; and access to an independent source of truth — a test suite, a schema, a reference dataset — against which the reviewer checks claims rather than re-reasoning them.
The pull towards the cheapest configuration, drafting and reviewing with the same model family, is precisely the trap: judge models systematically prefer text that is familiar to them, rating outputs from their own family more highly than a human would (Wataoka et al., 2024), so genuine independence needs model diversity, not merely a fresh context window.
Where none of these levers is pulled, a second agent supplies correlated opinion, which is to say cost without information.
The corollary sharpens the design rule to a single test applied to every proposed agent: name the class of error this agent will catch that the existing agents and gates would not, and describe the mechanism that makes its judgement independent of theirs; if you can state neither, the agent is decoration and should be replaced by a deterministic gate or a human check.
The limitation is that independence is a matter of degree and cannot be measured directly at design time, so this test is a discipline for reasoning about a roster rather than a proof of its soundness, and the evaluation machinery of Chapter 11 is what turns the design-time argument into a measured claim (moderate-to-high confidence).

> **In plain terms — Ensemble.** In forecasting, a set of model runs started from slightly
> different conditions, whose spread is read as the forecast's uncertainty. The spread only
> means anything if the members can genuinely disagree; runs that share too much collapse
> together and become confidently wrong in unison — the same trap a set of near-identical
> agents falls into.

**Figure 10.1 — Independence, not multiplicity, is the source of value.** *A figure brief follows `FIGURES.md`; render in the house style.*

```
FIGURE BRIEF
- id:            Figure 10.1
- title:         When a second agent adds information and when it adds only cost
- type:          decision flowchart
- claim:         A second agent is worth its latency and token cost only when its errors are independent of the agent it checks; correlated agents add cost without information.
- canvas:        16:9
- elements:      a start node "proposed second agent" (grey); first diamond gate "names an error class the existing roster misses?" (vermillion); second diamond gate "judgement independent of the checked agent? (different model / narrowed context / adversarial brief / external source of truth)" (vermillion); an orange terminal "keep — independent reviewer" (reviewer purple icon with tick); a grey terminal "drop — correlated opinion, add a deterministic gate instead" (gate icon)
- flow:          top-to-bottom. proposed second agent → gate 1. Gate 1 "no" → "drop". Gate 1 "yes" → gate 2. Gate 2 "no" → "drop". Gate 2 "yes" → "keep — independent reviewer"
- labels:        "proposed second agent", "names an error class the roster misses?", "judgement independent of the checked agent?", "keep — independent reviewer", "drop — add a deterministic gate instead", "yes", "no"
- annotations:   a light callout beside gate 2 listing the four independence levers: "different model", "narrowed context", "adversarial brief", "external source of truth"
- caption:       Figure 10.1 — The test applied to every proposed agent. Both gates must pass — a distinct error class and an independent mechanism for catching it — before a second agent earns its place; failing either, a deterministic gate is cheaper and more reliable than a correlated opinion.
- alt-text:      A top-to-bottom decision flowchart. A proposed second agent first meets the question of whether it names an error class the existing roster misses; if no, it is dropped in favour of a deterministic gate. If yes, a second question asks whether its judgement is independent of the checked agent, annotated with four levers — different model, narrowed context, adversarial brief, external source of truth. Only if that also holds is the agent kept as an independent reviewer.
- generator prompt: A flat vector decision flowchart on an off-white background, flowing top
                 to bottom. A grey rounded rectangle labelled "proposed second agent"
                 connects down to a vermillion diamond labelled "names an error class the
                 roster misses?". Its "no" exit leads right to a grey terminal labelled
                 "drop — add a deterministic gate instead" with a small diamond gate icon.
                 Its "yes" exit leads down to a second vermillion diamond labelled
                 "judgement independent of the checked agent?". A small callout box beside
                 it lists "different model", "narrowed context", "adversarial brief",
                 "external source of truth". The diamond's "no" exit leads to the same grey
                 "drop" terminal; its "yes" exit leads to a reddish-purple rounded rectangle
                 labelled "keep — independent reviewer" with a head-and-shoulders-with-tick
                 icon. Single-weight connectors, one arrowhead style, generous spacing,
                 minimal text.
```

## 10.4 The agentic redesign: roles, rosters and gates

The redesign that follows from the independence principle is not a larger crowd of agents but a small roster of clearly distinct roles separated by gates, with a human holding the accountable node.
Three role types recur across scientific rosters, and they are worth naming because their distinctness is what supplies the independence.
A **producer** role carries the transformational work — drafting a synthesis, writing pipeline code, assembling a manuscript section — and corresponds to the single-agent patterns of Chapters 5 to 9.
An **independent reviewer** role, developed for code in Chapter 7 and generalised here, is handed a different and adversarial brief, a narrowed context and, wherever possible, a different model, and is judged by the faults it surfaces rather than by its agreement with the producer.
A **gate** is not an agent at all but a deterministic check — a test suite, a schema validation, a citation resolver, a units audit — placed between roles so the cheap, mechanical verification is mandatory rather than advisory; whenever a proposed check can be written as a rule, reach for a gate, not another agent.
Above these sits an orchestration function that routes artefacts between roles and enforces the stop conditions, and it should be deliberately thin: an orchestrator that reasons about the science reintroduces exactly the correlated judgement the roster was built to avoid, whereas one that only sequences steps and applies gates adds coordination without adding opinion.
This roles-and-rosters structure is not new; conversation-structured multi-agent frameworks from around 2023 made it a standard way to build agent applications, and — a point worth borrowing — they treat a human-in-the-loop role as a first-class member of the roster rather than an afterthought (Wu et al., 2023).
The human decision point is the load-bearing element, placed wherever accountability, interpretation or authorship is at stake — the boundaries drawn in Chapter 4 — because no arrangement of agents, however independent, discharges the answerability Chapter 1 identified as non-transferable.
The design rule that ties the roster together is that independence must be engineered at every producer–reviewer boundary and that every loop must terminate: reviewers that can send work back to producers create cycles, and a cycle without a bounded iteration count and an escalation path is a cost blow-out and a diffusion-of-responsibility failure waiting to happen (§10.6).
The provenance of who produced, who reviewed and who decided is recorded at each handoff, feeding the audit trail Chapter 12 specifies; a roster whose internal handoffs are not logged cannot later be shown to have checked what it claims to have checked (high confidence in the structure; the thin-orchestrator claim is moderate confidence and workload-dependent).
Set beside the conventional arrangement of §10.2, the redesign keeps what made distributed human review work — independence between producer and checker, a named party accountable at each boundary — while replacing serial handoffs measured in days with gated handoffs measured in minutes, and Figure 10.3 places the two side by side so the shared grammar and the compressed timescale are legible at once.

> **In plain terms — Independent reviewer.** An agent whose only job is to find faults in
> another agent's work, set up so that its judgement does not simply echo the producer's: a
> different model where possible, a deliberately narrower view of the task, an instruction
> that rewards catching problems, and its own source of truth to check against. Independence
> is the whole point — a reviewer that shares the producer's model and context mostly agrees
> with it.

**Figure 10.2 — A minimal scientific roster.** *A figure brief follows `FIGURES.md`; render in the house style.*

```
FIGURE BRIEF
- id:            Figure 10.2
- title:         A minimal roster — producer, independent reviewer, gates, human decision
- type:          architecture
- claim:         A scientific roster is a small set of distinct roles separated by deterministic gates, with independence engineered at the producer–reviewer boundary and a human holding the accountable node.
- canvas:        16:9
- elements:      a thin grey "orchestrator" bar spanning the top (labelled "sequences and enforces stop conditions"); below it, left to right, a "specification" tag (blue); a "producer agent" rounded rectangle (orange) with a "tools" glyph (green) and a "data store" cylinder (sky blue); a deterministic "gate" diamond (vermillion, labelled "tests · schema · citations · units"); an "independent reviewer agent" rounded rectangle (reddish purple, head-and-shoulders-with-tick icon) annotated "different model · narrowed context · adversarial brief"; a second "gate" diamond (vermillion); a "human decision" head-and-shoulders icon (blue)
- flow:          left-to-right — specification → producer → gate → independent reviewer → gate → human decision; a single "fail" return arrow runs from the reviewer back to the producer, labelled "bounded iterations, then escalate"
- labels:        "orchestrator — sequences, enforces stop conditions", "specification", "producer agent", "tools", "data store", "gate", "independent reviewer", "different model · narrowed context · adversarial brief", "human decision", "fail — bounded iterations, then escalate"
- annotations:   a callout on the reviewer box "independence engineered here"; a callout on the human node "accountability, interpretation, authorship stay here"
- caption:       Figure 10.2 — The minimal roster. Deterministic gates carry the cheap, mechanical checks; the independent reviewer carries only what a rule cannot, and does so from an engineered position of independence; the human node holds what does not transfer to any instrument. The return loop is explicitly bounded to prevent runaway cost.
- alt-text:      An architecture diagram read left to right. A thin orchestrator bar spans the top. Below, a specification feeds a producer agent with tools and a data store; its output passes a deterministic gate labelled tests, schema, citations, units; then an independent reviewer agent, annotated different model, narrowed context and adversarial brief; then a second gate; then a human decision point annotated that accountability, interpretation and authorship stay there. A single fail arrow returns from reviewer to producer, labelled bounded iterations then escalate.
- generator prompt: A flat vector architecture diagram on an off-white background. A thin
                 grey horizontal bar across the top is labelled "orchestrator — sequences,
                 enforces stop conditions". Beneath it, arranged left to right with
                 single-weight connectors: a small blue tag "specification"; an orange
                 rounded rectangle "producer agent" containing a green wrench icon "tools"
                 and a sky-blue cylinder "data store"; a vermillion diamond "gate" labelled
                 "tests · schema · citations · units"; a reddish-purple rounded rectangle
                 "independent reviewer" with a head-and-shoulders-with-tick icon and a small
                 annotation "different model · narrowed context · adversarial brief"; a
                 second vermillion diamond "gate"; and a blue head-and-shoulders icon "human
                 decision". A single curved arrow labelled "fail — bounded iterations, then
                 escalate" returns from the reviewer to the producer. Two small callouts
                 read "independence engineered here" pointing at the reviewer and
                 "accountability, interpretation, authorship stay here" pointing at the human
                 node. Generous spacing, minimal text.
```

**Figure 10.3 — Conventional review and agentic roster, side by side.** *A figure brief follows `FIGURES.md`; render in the house style.*

```
FIGURE BRIEF
- id:            Figure 10.3
- title:         Distributed human review and its agentic roster share one grammar
- type:          before/after
- claim:         A roster reproduces the independence structure of conventional distributed review — producer, independent checker, accountable decider — but compresses serial handoffs of days into gated handoffs of minutes.
- canvas:        16:9
- elements:      an upper "conventional" lane and a lower "agentic roster" lane sharing a common left-to-right grammar. Upper lane (conventional): "author" (blue human) → "internal read-through" (blue human) → "independent referees ×2" (blue humans) → "editor decides" (blue human), annotated "serial, ~weeks". Lower lane (agentic roster): "producer agent" (orange) → "gate" (vermillion) → "independent reviewer" (reddish purple) → "gate" (vermillion) → "human decision" (blue human), annotated "gated, ~minutes; human owns the decision"
- flow:          two stacked left-to-right lanes read in parallel; vertical dotted alignment lines connect the matching roles — author↔producer, referees↔independent reviewer, editor↔human decision
- labels:        "conventional", "author", "internal read-through", "independent referees ×2", "editor decides", "serial — weeks", "agentic roster", "producer agent", "gate", "independent reviewer", "human decision", "gated — minutes; human owns the decision"
- annotations:   three light vertical alignment lines labelled "producer", "independent checker", "accountable decider" linking the two lanes; a note "what carries over: independence and accountability — not the number of parties"
- caption:       Figure 10.3 — The same structure at two timescales. Both lanes separate a producer from an independent checker and vest the decision in an accountable human; the roster changes the timescale and the medium of the checks, not the principle that makes distributed review worth its cost.
- alt-text:      A before/after diagram with two stacked left-to-right lanes. The upper lane, conventional, runs author, internal read-through, two independent referees, editor decides, annotated serial over weeks. The lower lane, agentic roster, runs producer agent, gate, independent reviewer, gate, human decision, annotated gated over minutes with the human owning the decision. Dotted vertical lines align the matching roles — producer, independent checker, accountable decider — across the two lanes, with a note that what carries over is independence and accountability, not the number of parties.
- generator prompt: A flat vector before/after diagram on an off-white background, with two
                 stacked horizontal lanes sharing a common left-to-right grammar. The upper
                 lane is labelled "conventional" and contains, left to right, four blue
                 head-and-shoulders icons labelled "author", "internal read-through",
                 "independent referees ×2", "editor decides", connected by single-weight
                 arrows, with a small annotation "serial — weeks". The lower lane is
                 labelled "agentic roster" and contains, left to right, an orange rounded
                 rectangle "producer agent", a vermillion diamond "gate", a reddish-purple
                 reviewer box "independent reviewer", a second vermillion diamond "gate",
                 and a blue head-and-shoulders icon "human decision", with a small annotation
                 "gated — minutes; human owns the decision". Three faint vertical dotted
                 lines connect the aligned roles across the two lanes, labelled "producer",
                 "independent checker", "accountable decider". A note reads "what carries
                 over: independence and accountability — not the number of parties". Generous
                 spacing, minimal text.
```

## 10.5 Worked example: deriving a roster from a specification

The safest way to arrive at a roster is not to design the team and then find work for it, but to derive the team mechanically from the workflow specification, so that every role and gate traces back to a clause a human wrote and can audit.
The specification schema of Chapter 3 gives you four fields that map onto roster elements with little slack, and reading the derivation in that direction — specification first, roster second — is the discipline that keeps a roster minimal, because a role no clause of the specification demands is a role that should not exist.
The **objective** fixes the producer roles: a single, well-bounded objective needs one producer, and a genuinely separable objective — a synthesis stage whose output a distinct modelling stage consumes, say — justifies a second producer only where the two demand different tools or different evidence, not merely because the work is long.
The **inputs** fix tool and data-store access and, by their sensitivity, where the governance constraints of Chapter 12 attach: inputs that touch credentialled institutional systems or partner data restrict which roles may hold which permissions, so least-privilege access is assigned per role rather than to the roster as a whole (Chapter 12).
The **acceptance criteria** are the richest source of structure, because each criterion is sorted into either a deterministic gate or an independent-reviewer responsibility by a single question — can a rule check it?
A criterion such as "all cited references resolve to real documents" or "the units in every derived field are dimensionally consistent" becomes a gate; a criterion such as "the synthesis represents the disagreement in the literature fairly" cannot be reduced to a rule and becomes the brief for an independent reviewer, whose adversarial framing is written straight from the criterion.
The **stop conditions** fix the orchestrator's loop bounds and the escalation path: the maximum number of producer–reviewer iterations, the token or wall-clock budget beyond which the roster halts, and the point at which unresolved disagreement goes to the human decision node rather than being churned further.
Worked through on a concrete operational specification, this mapping yields a small, auditable roster in which every element has a provenance in the specification and nothing is present for appearance's sake **[AUTHOR: insert a specification you have actually written — the rainfall-forecast verification specification from Chapter 3 is the natural candidate — and show the exact roster it produced, including the criteria you triaged to gates versus to the reviewer, the iteration bound you set, and any role you initially added and then removed as correlated. The executed version of this derivation is the spine of Chapter 15; this section should foreshadow it, not pre-empt its results.]**
The limitation worth stating is that the mapping is only as good as the specification: a vague acceptance criterion produces a vague reviewer brief and a roster no more rigorous than the words it came from, which is the mechanism by which specification quality (Chapter 3) governs roster quality, and why the two chapters are read together (high confidence in the mapping; the operational specifics await the author's executed material).

**Figure 10.4 — From specification to roster.** *A figure brief follows `FIGURES.md`; render in the house style.*

```
FIGURE BRIEF
- id:            Figure 10.4
- title:         Deriving a roster from the specification schema
- type:          sequence
- claim:         Each field of a Chapter 3 specification maps to a specific roster element, so that every role and gate has an auditable provenance in a clause a human wrote.
- canvas:        16:9
- elements:      four specification fields on the left as blue tags stacked top to bottom — "objective", "inputs", "acceptance criteria", "stop conditions"; four roster outcomes on the right, each reached by a numbered arrow — "producer role(s)" (orange), "tool & data-store access, per-role least privilege" (green tool + sky data-store), "gates (rule-checkable criteria) + independent reviewer brief (judgement criteria)" (vermillion gate + reddish-purple reviewer), "orchestrator loop bound + escalation to human" (grey orchestrator + blue human)
- flow:          top-to-bottom, four numbered mappings read in order: 1 objective → producer role(s); 2 inputs → tool & data access; 3 acceptance criteria → gates + reviewer brief; 4 stop conditions → loop bound + escalation
- labels:        "objective", "inputs", "acceptance criteria", "stop conditions", "producer role(s)", "tool & data access (least privilege)", "gates + reviewer brief", "loop bound + escalation", "1", "2", "3", "4"
- annotations:   a callout on mapping 3 "can a rule check it? → gate; if not → reviewer"; a callout on mapping 4 "bounds cost and diffusion of responsibility"
- caption:       Figure 10.4 — The derivation that keeps a roster minimal and auditable. Objective fixes the producers, inputs fix least-privilege access, acceptance criteria split into deterministic gates and reviewer briefs by whether a rule can check them, and stop conditions bound the loop and set the escalation to the human node. A role no clause demands is a role that should not exist.
- alt-text:      A top-to-bottom sequence with four numbered mappings. On the left, four specification fields as blue tags — objective, inputs, acceptance criteria, stop conditions. Each maps by a numbered arrow to a roster element on the right — objective to producer roles; inputs to tool and data access under least privilege; acceptance criteria to deterministic gates plus an independent reviewer brief, split by whether a rule can check the criterion; stop conditions to the orchestrator loop bound and escalation to a human.
- generator prompt: A flat vector sequence diagram on an off-white background, read top to
                 bottom. On the left, four blue tags stacked vertically read "objective",
                 "inputs", "acceptance criteria", "stop conditions". From each, a numbered
                 horizontal arrow (1, 2, 3, 4) points right to a roster element: arrow 1 to
                 an orange rounded rectangle "producer role(s)"; arrow 2 to a green wrench
                 icon beside a sky-blue cylinder labelled "tool & data access (least
                 privilege)"; arrow 3 to a pairing of a vermillion diamond and a
                 reddish-purple reviewer box labelled "gates + reviewer brief", with a small
                 callout "can a rule check it? gate; if not, reviewer"; arrow 4 to a grey
                 orchestrator bar beside a blue head-and-shoulders icon labelled "loop bound
                 + escalation", with a small callout "bounds cost and diffusion of
                 responsibility". Single-weight connectors, one arrowhead style, generous
                 spacing, minimal text.
```

## 10.6 Failure modes

The failure modes of multi-agent workflows are, with one exception, not new failures but the single-agent failures of the preceding chapters amplified by composition, and naming them precisely is what lets you design the roster against them.
The empirical taxonomy of multi-agent failure sorts them into three families — poor task and role specification, inter-agent misalignment such as miscommunication and lost context, and absent, weak or premature verification (Cemri et al., 2025) — and the modes below map onto those families almost one to one.
**Over-agreeable review** is the most common and the most dangerous, because it defeats the whole purpose of the roster while leaving its diligent appearance intact: a reviewer agent built on the same model as the producer, given the producer's full context and a neutral brief, tends to ratify rather than challenge, and its agreement is read as corroboration when it is in fact correlation.
That the tendency is systematic and not incidental is by now well documented — judge models carry characterised biases towards self-preference, verbosity and answer position (Zheng et al., 2023) — and the anatomy of the failure, with a worked trace, is the business of Chapter 13; here the point is the countermeasure.
It is the independence engineering of §10.3 — different model, narrowed context, adversarial brief, external source of truth — and the diagnostic is a reviewer that almost never returns a fault, which for real scientific work is evidence of a broken reviewer, not a flawless producer [AUTHOR: your observed base rate of substantive faults from a well-configured reviewer versus a naive one would quantify this; report it if you have it].
**Diffusion of responsibility** is the organisational failure in which an error passes through several agents, each of which could have caught it, and afterwards no node owns the miss because responsibility was never located at a named human — a hazard the roster avoids only by putting an accountable human decision point at every boundary where interpretation or consequence is at stake, exactly as Chapter 4 requires.
**Cost blow-out** is the economic failure, and it comes from unbounded producer–reviewer loops, from orchestrators that reason verbosely, and from the token cost of every agent re-reading a growing shared context: a roster that iterates without a hard bound can burn many times a single agent's cost while converging on nothing, which is why every loop carries an iteration count, a budget and an escalation path (§10.5), and why the honest accounting of Chapter 16 treats roster cost as a first-order design constraint rather than a footnote.
**Correlated errors** are the statistical failure beneath the others: agents drawn from the same model share a failure distribution, so a mistake one makes the others are disproportionately likely to repeat and to endorse, and multiplicity then manufactures false confidence — the collapsed-ensemble problem of §10.3 in operational form.
Two further modes deserve mention for completeness.
Context contamination occurs when a reviewer inherits the producer's framing through a shared context window and loses the very independence it was added to supply, which is why narrowed context is a lever and not a nicety.
Emergent miscoordination occurs when thin specifications let agents negotiate scope among themselves, drifting from the objective in ways no single transcript makes obvious; the defence is the specification-first derivation of §10.5, which leaves agents no scope to invent.
The limitation common to all these countermeasures is that they are verified by the machinery of Part III rather than guaranteed by the design, so a roster is a hypothesis about independence to be tested, not a proof of it — and the base rates that would tell you how well a given roster actually checks its own work await measurement, which is the task Chapter 11 takes up (high confidence in the taxonomy; the base rates await measurement).

## 10.7 Verification checklist

This checklist certifies that a roster is worth its cost before you trust it with work of consequence, and it turns the chapter's single claim — independence, not multiplicity, is what a roster must supply — into things a colleague can confirm. It is written to be applied by someone who did not build the roster, in keeping with the specification-as-control-surface principle of Chapter 3 and the audit requirements of Chapter 12.

- **Every role traces to the specification.** Each producer, gate and reviewer maps to an objective, input, acceptance criterion or stop condition (§10.5); any role without such a provenance is removed. (high confidence)
- **Every second agent passes the independence test.** For each reviewer, the class of error it catches that the gates and other agents would not is named, and its independence mechanism — different model, narrowed context, adversarial brief or external source of truth — is stated (§10.3, Figure 10.1). (high confidence)
- **Rule-checkable criteria are gates, not agents.** Any acceptance criterion a deterministic check can settle is implemented as a gate; a reviewer agent is used only for criteria a rule cannot express (§10.4). (high confidence)
- **Reviewers are configured for independence, and it shows.** Reviewers do not share the producer's full context or model where avoidable, and a well-configured reviewer returns substantive faults at a non-trivial rate; a reviewer that never dissents is treated as broken (§10.6). (moderate-to-high confidence)
- **Every loop is bounded and escalates.** Each producer–reviewer cycle has a maximum iteration count, a token or wall-clock budget, and a defined escalation to a named human on non-convergence (§10.5, §10.6). (high confidence)
- **A human owns each consequential boundary.** Accountability, interpretation and authorship sit at named human decision points, not with the orchestrator or any agent (§10.4, Chapter 4). (high confidence)
- **Handoffs are logged.** Who produced, who reviewed, who gated and who decided is recorded for every artefact, feeding the audit trail (Chapter 12). (high confidence)
- **The roster is costed against the single-agent baseline.** The added latency and token cost of the roster are measured against one agent plus deterministic gates, and the roster is retained only where the added cost buys measured independent checking (§10.6, Chapter 16). (moderate confidence; workload-dependent)

## 10.8 Repository pointer

The companion repository holds the runnable and perishable counterparts to this chapter under the layout of outline §8.
A minimal roster — one producer, one deterministically gated check, one independence-configured reviewer, a thin orchestrator with a bounded loop, and a human-approval step — sits under `/patterns` as an executable skeleton to adapt rather than a finished workflow, with the current model and tool bindings named there because they date quickly and must not enter the print.
The specification-to-roster derivation of §10.5 sits under `/prompts` as a worked template that consumes a Chapter 3 specification and emits a role-and-gate roster with each element annotated by the clause it derives from, alongside the reviewer-brief patterns that turn a judgement acceptance criterion into an adversarial instruction.
The verification checklist of §10.7 is mirrored under `/checklists` in printable form.
The sanitised configuration of the executed roster behind Chapter 15 will be deposited under `/case-studies` once that chapter's material is settled **[AUTHOR: confirm which operational roster is released as the Chapter 15 case study and what must be sanitised — model bindings, credentials, partner-data references — before it is deposited]**.
If you are adopting a roster in your own group, the thirty-day on-ramp and cost model of Chapter 16 are where to turn next, because deciding to run a roster rather than a single agent is as much a budgetary and organisational commitment as a technical one — and the chapter's central caution bears one final repetition: a roster earns its cost only where its agents are independent, and where they are not, one well-specified agent behind deterministic gates is cheaper, faster and no less rigorous.

---

*Cross-references: the single-agent patterns this chapter composes (Chapters 5–9); when not to reach for an agent at all (Chapter 4); measuring whether a roster actually checks its own work (Chapter 11); the audit trail that logs every handoff (Chapter 12); the anatomy and worked trace of over-agreeable review (Chapter 13); the executed end-to-end roster (Chapter 15); roster cost and the adoption on-ramp (Chapter 16).*

## References

- Cemri, M., Pan, M.Z., Yang, S., et al. (2025). "Why Do Multi-Agent LLM Systems Fail?" arXiv preprint. https://arxiv.org/abs/2503.13657 **[verify: archival venue — an OpenReview record exists]**.
- Du, Y., Li, S., Torralba, A., Tenenbaum, J.B. and Mordatch, I. (2024). "Improving Factuality and Reasoning in Language Models through Multiagent Debate." ICML 2024. Preprint: https://arxiv.org/abs/2305.14325.
- Kapoor, S., Stroebl, B., Siegel, Z.S., Nadgir, N. and Narayanan, A. (2024). "AI Agents That Matter." arXiv preprint. https://arxiv.org/abs/2407.01502 **[verify: archival venue]**.
- Wataoka, K., Takahashi, T. and Ri, R. (2024). "Self-Preference Bias in LLM-as-a-Judge." arXiv preprint. https://arxiv.org/abs/2410.21819 **[verify: peer-reviewed venue]**.
- Wu, Q., Bansal, G., Zhang, J., Wu, Y., et al. (2023). "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation." arXiv preprint. https://arxiv.org/abs/2308.08155 **[verify: peer-reviewed venue — a version appeared at COLM 2024]**.
- Zheng, L., Chiang, W.-L., Sheng, Y., et al. (2023). "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena." NeurIPS 2023 Datasets and Benchmarks Track. Preprint: https://arxiv.org/abs/2306.05685.
