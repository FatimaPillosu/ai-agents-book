# Chapter 3 — Specifying work for agents

> **Status:** draft r3 · voice v3.3 (`STYLE.md`) · sentence-per-line per `STYLE.md` §10 · figures as briefs per `FIGURES.md`.
> **Conventions:** vendor-neutral (outline §9) · **[AUTHOR: …]** marks lived material only the author can supply · **[verify]** marks real but unconfirmed details · citations drawn only from verified reports in `/research`. Nothing has been invented.

---

## 3.1 The skill most failures trace back to

The single competence that most sharply separates productive agentic work from expensive disappointment is the ability to specify a task precisely enough for an agent to execute it and a human to audit it afterwards.
This claim is worth stating in its strong form, because it is stronger than a truism.
Across the failure modes catalogued in Chapter 13 (fabricated citations, silent unit errors, over-agreeable review, and confident extrapolation) a large share resolve, on inspection, not to a limitation of the model but to a task that was never pinned down before the agent began (moderate confidence; this is a matter of judgement rather than measurement, and the line between a specification fault and a capability fault is not always clean).
The reason specification carries so much weight is structural.
An agent has discretion over the intermediate steps it takes towards a goal, as Chapter 1 established; that discretion is exactly what makes the class useful, and exactly what makes an underspecified goal dangerous, because every gap the specification leaves open is a gap the agent will fill with an assumption nobody saw and nobody can later reconstruct.
A conventional script fails loudly at the point of ambiguity, raising an error.
An agent, by contrast, resolves the ambiguity silently and plausibly, and carries on.
The implication for practice is that the effort once spent debugging an execution now moves earlier, into the writing of the task itself, and this relocation of effort is not overhead to be minimised but the substance of the work.
The qualification that belongs right beside the claim is that a specification cannot eliminate failure, only make it detectable: a well-written specification does not guarantee a correct result, but it guarantees that an incorrect result can be recognised as incorrect against a standard fixed in advance, which is the property every verification mechanism in this book depends on.

> **Definition — Specification.** The written statement of a task handed to an agent in place of a vague request: what the work is to achieve, what it may use, what counts as done, and when to stop. It is the difference between an informal request and a brief precise enough that a party other than the author could check whether the result meets it.

Decomposition comes before specification, and the two are clearest treated as distinct acts.
Decomposition is the analytical step of breaking a scientific task into units small enough that each has a single, checkable outcome; specification is the step of writing each unit down in a form an agent can execute and a reviewer can audit.
The order matters because a task decomposed badly cannot be specified well.
A unit that bundles three loosely related outcomes (acquire the data, quality-control it, and summarise the result) resists any single acceptance criterion, and the temptation under such bundling is to specify loosely and hope, which is exactly the failure this chapter exists to prevent.
The heuristic adopted here, and developed further in the pattern chapters of Part II, is that a task is decomposed finely enough when each unit admits a stop condition and a check that a party other than the author could apply without further explanation (moderate confidence).
Over-decomposition is a real cost on the other side, because a task split into forty trivial units carries coordination overhead a competent agent could have absorbed within one, and the balance point is a matter of judgement that improves with practice rather than a rule that can be stated once.
What does not vary is the direction of the discipline: from a vague obligation towards a set of units, each of which states what "done" means before any agent is asked to reach it.

## 3.2 Four elements an agent can execute and a human can audit

A specification an agent can execute and a human can audit rests on four elements, and the argument of this chapter is that all four are load-bearing: omit any one and a characteristic failure follows.
The first is the **objective**, a single statement of what the unit of work is to achieve, written as an outcome rather than a procedure.
This distinction is not pedantic.
An objective phrased as a procedure ("run the following steps") forecloses the agent's discretion and wastes the class; an objective phrased as an outcome ("produce a quality-controlled daily rainfall series for the named stations over the named period, with every rejected value flagged and reasoned") leaves the agent free to plan the route whilst fixing the destination against which the route can be judged.
The second element is the **inputs**: the exact data, files, parameters, conventions and prior artefacts the unit may draw on, named specifically enough that their provenance is recoverable and their absence is an error rather than an invitation to improvise.
Underspecified inputs are the most common quiet defect seen in practice, because an agent denied a named input will often locate a plausible substitute (a different station, a different reference period, or a differently versioned file) and proceed without remark, so that the output is defensible on its face and wrong at its root (high confidence in the pattern; frequency varies by task and model).
Naming inputs precisely is therefore not bureaucratic caution but the primary defence against silent substitution.

The third and fourth elements govern the two ends of execution.
**Acceptance criteria** state the conditions the output must meet to count as done, expressed wherever possible as checks a party other than the agent can apply: a schema the output must validate against, a numerical tolerance a computed field must fall within, a reconciliation that must balance, or a property that must hold.

> **Definition — Acceptance criteria.** The conditions an output has to meet before it counts as finished, written down in advance and, wherever possible, as checks a party other than the agent can apply. They state what "correct" means before the work starts, so that "it looks right" never stands in for "it passed the check".

Acceptance criteria are the mechanism by which the asymmetry introduced in Chapter 1, between the cost of producing an output and the cost of verifying it, is put to work, because a criterion is only worth writing if checking it is cheaper than reproducing the work, and a task whose acceptance genuinely requires expert re-derivation is a task to keep on the human side of the boundary rather than to specify for an agent.
The fourth element, most often omitted and most consequential when it is, is the **stop conditions**: the circumstances under which the agent must halt and hand back rather than continue.

> **Definition — Stop condition.** The rule that tells an agent when to halt, either because it has succeeded and the acceptance criteria are met, or because it has failed and cannot make progress, has used up an agreed budget of attempts, or has met something the specification did not anticipate. Without the failure kind, an agent that cannot succeed simply does not stop.

Stop conditions come in two kinds, and a complete specification carries both: success stops, which end the unit when the acceptance criteria are met, and failure stops, which end it when the agent cannot make progress, has exhausted a budget of attempts or resources, or meets a condition the specification did not anticipate.
The failure kind is the one that separates a governed workflow from an open-ended one, because without it an agent that cannot succeed will not stop; it will go on spending tokens, time and money generating ever more elaborate attempts to satisfy a criterion it cannot meet, and the loop is discovered only when the bill or the clock intervenes (high confidence; this is among the most reliably observed operational failure modes).
A stop condition converts that open-ended hazard into a bounded, reviewable event.

## 3.3 A workflow-agnostic specification schema

The four elements compose into a schema that is deliberately independent of any particular workflow, tool or model, and that independence is the point.
A schema tied to a product would date as fast as the product; a schema tied to the logic of specifying work outlasts the tools that implement it.
The origin of this schema bears on how much weight to put on it, and it is stated plainly here.
A search of the literature found no settled academic treatment of specifying tasks for agents in the sense meant here, that is, objective, acceptance criteria and stop conditions written as an auditable artefact.
What exists in abundance is the neighbouring literature on prompting, and the most systematic survey of it catalogues a sprawling, unstandardised space of dozens of techniques with conflicting terminology, and shows that the choice of technique measurably changes output quality whilst remaining brittle even in expert hands (Schulhoff et al., 2024).
That finding admits two readings, and both point here: control through input text is real, which is why specification is worth the effort, and it is unreliable, which is why the criteria that decide "done" must sit outside the model rather than inside the prompt.
The schema below is therefore the book's own synthesis rather than a reproduction of an established standard, offered because the practice needs one and the literature does not yet supply it.
That the literature does not supply one does not make this schema idiosyncratic: a widely followed practitioner formulation, the delegation loop, breaks a delegated task into a goal, the sources the agent should use, a standard the output must meet, an explicit permission boundary and a defined proof that the work is done, matching the schema here almost element for element, with its proof-of-done playing the part of the acceptance criteria (practitioner commentary; see the references).

The schema names the four elements already introduced (objective, inputs, acceptance criteria, and stop conditions) and adds three fields that experience shows are needed to make a specification auditable rather than merely executable.
The first addition is an explicit statement of **assumptions and conventions**: the units, coordinate reference systems, calendar conventions, missing-value codes and domain defaults the unit takes for granted, written down because an unstated convention is an ungoverned one, and because the unit-conversion failures of §3.1 and Chapter 13 live precisely in the gap between a convention one party assumed and another did not.
The second is a **provenance requirement**: a statement of what the unit must record about its own execution (inputs consumed with their versions, decisions taken, and values rejected with reasons) so that the output arrives with the audit trail Chapter 12 depends on rather than requiring one to be reconstructed later.
The third is an explicit naming of the **reviewer**: who or what applies the acceptance criteria, and whether that party is the agent itself (weak), a separate agent (stronger), or a human (strongest for consequential decisions), a field that matters because an acceptance criterion with no named party to apply it is decorative.
This seven-field schema is load-bearing for two later chapters, and it is introduced here so that both can build on it directly: Chapter 10 derives an agent roster from a specification by reading its units and reviewers and assigning each to an actor, and Chapter 15 carries a single specification through an entire governed modelling workflow from this schema to a publication run.
A schema internalised here turns both of those chapters into elaborations of it rather than new material.

**Figure 3.1 — Specification anatomy.**

![A diagram of a box labelled specification containing two columns. The left column stacks four fields (objective, inputs, acceptance criteria, stop conditions) bracketed as executable. The right column stacks three fields (assumptions and conventions, provenance requirement, reviewer) bracketed as auditable. An agent glyph feeds the box; the acceptance-criteria field connects to a check diamond applied by a human reviewer.](../figures/figure-3-1.svg)

*Figure 3.1 — The anatomy of a specification. The four core fields on the left make a unit of work executable by an agent; the three fields on the right make it auditable by a human; the named reviewer applies the acceptance criteria. This seven-field schema recurs in Chapters 10 and 15. (Rendered as `figures/figure-3-1.svg` from the brief below, per `FIGURES.md`.)*

```
FIGURE BRIEF
- id:            Figure 3.1
- title:         The anatomy of an executable, auditable specification
- type:          architecture
- claim:         A specification is a fixed structure of seven fields; the four core fields make it executable, the three added fields make it auditable, and a named reviewer closes the loop.
- canvas:        16:9
- elements:      an outer rounded rectangle "specification" (grey structural border);
                 inside it, a left column of four stacked tags in blue — "objective",
                 "inputs", "acceptance criteria", "stop conditions"; a right column of
                 three stacked tags in sky blue — "assumptions & conventions",
                 "provenance requirement", "reviewer"; the "acceptance criteria" tag
                 connects rightward to a vermillion diamond "check"; the "reviewer" tag
                 (blue human head-and-shoulders icon) sits beside the diamond; a small
                 orange agent glyph sits to the left of the whole block, feeding into it
- flow:          left-to-right — agent reads the specification; within it the four core
                 fields (blue) and three audit fields (sky blue) feed the "check" diamond,
                 which is applied by the named "reviewer"
- labels:        "specification", "objective", "inputs", "acceptance criteria",
                 "stop conditions", "assumptions & conventions", "provenance requirement",
                 "reviewer", "check", "executable", "auditable"
- annotations:   a light bracket down the left column labelled "executable"; a light
                 bracket down the right column labelled "auditable"
- caption:       Figure 3.1 — The anatomy of a specification. The four core fields on the left make a unit of work executable by an agent; the three fields on the right make it auditable by a human; the named reviewer applies the acceptance criteria. This seven-field schema recurs in Chapters 10 and 15.
- alt-text:      A diagram of a box labelled specification containing two columns. The left column stacks four fields (objective, inputs, acceptance criteria, stop conditions) bracketed as executable. The right column stacks three fields (assumptions and conventions, provenance requirement, reviewer) bracketed as auditable. An agent glyph feeds the box; the acceptance-criteria field connects to a check diamond applied by a human reviewer.
- generator prompt: A flat vector architecture diagram on an off-white background. A large
                 grey-bordered rounded rectangle labelled "specification" fills the centre.
                 Inside, a left column of four blue tags stacked vertically reads
                 "objective", "inputs", "acceptance criteria", "stop conditions"; a right
                 column of three sky-blue tags reads "assumptions & conventions",
                 "provenance requirement", "reviewer". A thin bracket beside the left column
                 is labelled "executable"; a thin bracket beside the right column is
                 labelled "auditable". To the left of the whole rectangle, a small orange
                 rounded-square agent glyph with a loop arrow connects rightward into it.
                 The "acceptance criteria" tag connects by a single line to a vermillion
                 diamond labelled "check" near the right edge; a blue head-and-shoulders
                 icon labelled "reviewer" sits beside the diamond. Minimal text, generous
                 spacing, single-weight lines, one arrowhead style.
```

## 3.4 The specification as the primary human control surface

The specification is the primary surface through which control over an agentic workflow is exercised, and recognising it as such reorders where attention and scepticism are spent.
In a conventional analysis the work is controlled by writing and reading every line of the procedure; in an agentic workflow the procedure is generated, so that attempting to regain control by reading every generated step does not scale and misplaces the effort besides, because the steps are numerous, revisable, and not where the consequential decisions were made.
The consequential decisions were made in the specification (what counts as done, what inputs are admissible, and when to stop), and it follows that the specification is where review effort earns the highest return, and where an institution's governance should attach.
There is a striking parallel in the research literature: the most realistic agent benchmarks now govern behaviour with an explicit written policy document the agent must obey, score a run by comparing the final state of the world against an annotated goal state, and find that a large share of failures are violations of that policy rather than failures of raw capability (Yao et al., 2024).
That is the same claim from the other direction: behaviour is controlled by an auditable written artefact, and where the artefact is thin, the work drifts.

This reframing has a practical corollary that Part III develops at length: a workflow is auditable to the degree that its specifications are legible, and an organisation that keeps its specifications under version control, reviews them before execution rather than only inspecting outputs after, and treats a change to a specification with the same care as a change to a method, has built the substrate on which provenance (Chapter 12) and end-to-end governance (Chapter 15) rest.
The limitation to state plainly is that a specification controls only what it addresses.
Discretion the specification leaves open remains real discretion, exercised by the agent out of sight, which is why the craft of §3.2, closing the gaps that matter whilst leaving open the ones that do not, is control rather than mere documentation, and why a specification is written, reviewed and revised as an artefact in its own right rather than dashed off as a preamble to the real work.

## 3.5 Worked example: from "verify this rainfall forecast" to an auditable specification

An informal request shows the distance between a wish and a specification more concretely than any general argument, and the one worked through here is drawn from operational practice: *verify this rainfall forecast*.
Stated that way it is a wish, and handing it to an agent produces exactly the weak, conversational pattern this chapter argues against.
In that pattern the request is typed as it stands, and the agent, having no fixed objective, no named inputs, no acceptance criteria and no stop conditions, quietly selects all four for itself: it settles on some notion of what "verify" means, locates whatever forecast and whatever observations it can reach, computes whatever score it favours, and returns a fluent summary that looks like an answer.
Each of those four silent choices is a decision the scientist should have made and can no longer see, and the output's plausibility is the hazard rather than the reassurance, because a wrong verification that looks right is worse than an obvious error.
The specific ways this weak version goes wrong in a rainfall context are concrete and familiar: the agent scores against the wrong reference dataset, or over a period that includes a known gauge outage, or with a metric insensitive to the very feature, the timing and placement of heavy-rainfall events, that the forecast exists to get right **[AUTHOR: name the specific metric-mismatch failure you have seen an unspecified verification produce — e.g. a good aggregate score masking poor placement of a convective event — and describe how it surfaced]**.

The strong version replaces every silent choice with a written field, and that transformation is the whole lesson of the chapter made concrete.
The **objective** becomes a single outcome: produce a verification of the named forecast against the named reference, reporting the named metrics with their uncertainty, over the named domain and period.
The **inputs** are named exactly: the forecast product and its issue time, the reference observation or analysis dataset and its version, the spatial domain, the aggregation period, and the treatment of the forecast's probabilistic structure **[AUTHOR: specify the exact forecast product, reference dataset, domain, lead times and accumulation period from the operational case you are drawing on]**.
The **acceptance criteria** fix what a valid verification must satisfy: the metrics computed are the ones the objective names and are appropriate to the quantity, so that for rainfall they are scores proper for a skewed, intermittent variable and sensitive to spatial displacement rather than aggregate bias alone; the reference period excludes intervals flagged for instrument outage; and every score carries an uncertainty estimate **[AUTHOR: state the exact metrics, the properness/sensitivity requirements, and the confidence-interval method the toolkit uses]**.
The **stop conditions** bound the run at both ends: succeed and halt when the criteria are met, and stop and hand back if a named input is missing or mis-versioned, if the reference series has more than a stated fraction of missing values in the target period, or if the two fields cannot be brought onto a common grid without a reprojection the specification did not authorise **[AUTHOR: give the concrete thresholds — acceptable missing-data fraction, permitted regridding — from practice]**.
Set beside the weak version, the strong specification has not made the verification correct; it has made a wrong verification detectable, converted four invisible decisions into four reviewable ones, and produced, as a by-product, the provenance record a downstream reader or an institutional auditor will need.
The measured claim to close on is that this conversion is the ordinary unit of agentic scientific work, not an exceptional ceremony reserved for high-stakes runs but the routine act by which any task worth delegating is prepared (high confidence, on the reasoning of §§3.1–3.4).

**Figure 3.2 — Weak specification versus strong specification.**

![A two-panel before-and-after diagram. In the upper weak panel a person says "verify this rainfall forecast" to an agent, which emits four question tags (which metric, which reference, which period, when to stop) and a fluent output flagged plausible but unauditable. In the lower strong panel the same request passes through a specification block of four filled fields (objective, inputs, acceptance criteria, stop conditions) and a check to an auditable output.](../figures/figure-3-2.svg)

*Figure 3.2 — The same request, left conversational and then specified. In the weak version the agent silently chooses metric, reference, period and stop; in the strong version the scientist fixes them as four fields, and a plausible-but-unauditable result becomes an auditable one. (Rendered as `figures/figure-3-2.svg` from the brief below, per `FIGURES.md`.)*

```
FIGURE BRIEF
- id:            Figure 3.2
- title:         "Verify this rainfall forecast" — weak versus strong specification
- type:          before/after
- claim:         The same request produces an unauditable result when left conversational and an auditable one when specified; the difference is four fields the scientist fills rather than the agent.
- canvas:        16:9
- elements:      two stacked panels sharing a grammar. Upper panel "weak (conversational)":
                 a blue human icon with a single speech bubble "verify this rainfall
                 forecast" feeding an orange agent glyph, from which four small grey
                 question-mark tags fan out — "which metric?", "which reference?",
                 "which period?", "when to stop?" — leading to a fluent output box marked
                 with a vermillion warning "plausible, unauditable". Lower panel
                 "strong (specified)": the same blue human and orange agent, but between
                 them a specification block with four filled blue tags — "objective",
                 "inputs", "acceptance criteria", "stop conditions" — leading through a
                 vermillion "check" diamond to an output box marked with a check
                 "auditable"
- flow:          top-to-bottom comparison; within each panel left-to-right from human to
                 agent to output
- labels:        "weak (conversational)", "strong (specified)", "verify this rainfall
                 forecast", "which metric?", "which reference?", "which period?",
                 "when to stop?", "objective", "inputs", "acceptance criteria",
                 "stop conditions", "check", "plausible, unauditable", "auditable"
- annotations:   a vermillion callout on the upper panel "four silent choices"; a blue
                 callout on the lower panel "four written fields"
- caption:       Figure 3.2 — The same request, left conversational and then specified. In the weak version the agent silently chooses metric, reference, period and stop; in the strong version the scientist fixes them as four fields, and a plausible-but-unauditable result becomes an auditable one.
- alt-text:      A two-panel before-and-after diagram. In the upper weak panel a person says "verify this rainfall forecast" to an agent, which emits four question tags (which metric, which reference, which period, when to stop) and a fluent output flagged plausible but unauditable. In the lower strong panel the same request passes through a specification block of four filled fields (objective, inputs, acceptance criteria, stop conditions) and a check to an auditable output.
- generator prompt: A flat vector before-and-after diagram on an off-white background, two
                 stacked panels of equal width sharing the same layout. The upper panel is
                 labelled "weak (conversational)": a blue head-and-shoulders icon with a
                 speech bubble reading "verify this rainfall forecast" connects rightward to
                 an orange rounded-square agent glyph; four small grey tags fan from the
                 agent reading "which metric?", "which reference?", "which period?", "when
                 to stop?"; these lead to a plain output box with a small vermillion warning
                 triangle labelled "plausible, unauditable". A vermillion callout reads
                 "four silent choices". The lower panel is labelled "strong (specified)":
                 the same blue icon and orange agent, but between them a grey-bordered block
                 holds four filled blue tags stacked — "objective", "inputs", "acceptance
                 criteria", "stop conditions" — which connect through a vermillion diamond
                 labelled "check" to an output box with a tick labelled "auditable". A blue
                 callout reads "four written fields". Minimal text, generous spacing,
                 single-weight lines, one arrowhead style.
```

## 3.6 The anti-pattern: conversational drift in place of specification

The dominant anti-pattern in agentic scientific work is conversational drift: the gradual replacement of a specification by an accumulating chat transcript, in which the task is never written down but is negotiated turn by turn until neither party could reconstruct what was agreed.
The pattern is seductive precisely because the conversational interface is the technology's most immediate strength, and because the early exchanges genuinely help, by clarifying, correcting and exploring, so the slide from productive dialogue into ungoverned drift is smooth and rarely noticed at the moment it happens.
Its symptoms are recognisable once named: the objective mutates across turns without any turn marking the change; inputs are referred to as "that file" and "the other dataset" rather than named; acceptance is asserted by the agent ("this looks correct") rather than checked against a fixed standard; and there is no stop condition, so the session ends when the scientist tires rather than when the work is done.

The damage is not only that such a session can go wrong but that when it does, there is nothing to audit, no artefact stating what should have happened, only a transcript recording what was said, and a workflow that cannot be audited cannot be governed, whatever its outputs happen to look like (high confidence).
The remedy is not to abandon conversation, which would forfeit a real strength, but to give it its proper place: conversation is where a specification is discovered and refined, and it earns its keep only when it terminates in a written specification the subsequent execution is held to.
The discipline this chapter asks for fits in one sentence, that is, talk to find the specification, then execute against it, and the whole of the practice that follows, from the patterns of Part II to the end-to-end governance of Chapter 15, depends on the transition from the first clause to the second being made deliberately and made visible, rather than never being made at all.

The limitation worth conceding is that for genuinely exploratory work, where the objective is not yet knowable, insisting on a specification prematurely is its own error.
The judgement of when exploration has yielded enough to specify is real, developed further in Chapter 4, and it is not resolved by pretending every task is ready to be pinned down at first contact.

---

### References (verify details before release)

- Jones, N. B. (2026). "Codex: your first personal AI agent delegation loop." Video, @natebjones, 12 June 2026. https://www.youtube.com/watch?v=xqGCbEDbny8 (practitioner commentary; concepts cited as corroboration, not evidence)
- Schulhoff, S., Ilie, M., Balepur, N., et al. (2024). The prompt report: a systematic survey of prompt engineering techniques. *arXiv preprint.* https://arxiv.org/abs/2406.06608
- Yao, S., Shinn, N., Razavi, P. and Narasimhan, K. (2024). τ-bench: a benchmark for tool-agent-user interaction in real-world domains. *arXiv preprint.* https://arxiv.org/abs/2406.12045
```
