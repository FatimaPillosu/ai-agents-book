# Chapter 3 — Specifying work for agents

> **Status:** draft r6 · voice v5.0 (`STYLE.md` §1) · sentence-per-line per `STYLE.md` §10 · figures as briefs per `FIGURES.md`.
> **Conventions:** vendor-neutral (outline §9) · **[AUTHOR: …]** marks lived material only the author can supply · **[verify]** marks real but unconfirmed details · citations drawn only from verified reports in `/research`. Nothing has been invented.

---

## 3.1 The skill most failures trace back to

One competence separates productive agentic work from expensive disappointment more sharply than any other: being able to specify a task precisely enough that an agent can execute it and a human can audit it afterwards.

That is worth stating in its strong form, because it is stronger than a truism.
Look at the failure modes catalogued in Chapter 13, such as fabricated citations, silent unit errors, over-agreeable review and confident extrapolation, and a large share turn out not to be limitations of the model at all.
They are tasks that were never pinned down before the agent started (moderate confidence; this is judgement rather than measurement, and the line between a specification fault and a capability fault is not always clean).

The reason specification carries so much weight is structural.
An agent has discretion over the intermediate steps it takes towards a goal, as Chapter 1 established.
That discretion is exactly what makes agents useful, and exactly what makes an underspecified goal dangerous, because every gap the specification leaves open is a gap the agent fills with an assumption nobody saw and nobody can reconstruct afterwards.
A conventional script fails loudly at the point of ambiguity and raises an error.
An agent resolves the ambiguity silently and plausibly, and carries on.
So the effort you used to spend debugging an execution moves earlier, into writing the task itself.
That relocation is not overhead to be minimised.
It is the work.
And the qualification belongs right next to the claim: a specification cannot eliminate failure, only make it detectable.
A well-written specification does not guarantee a correct result, but it does guarantee that an incorrect result can be recognised as incorrect against a standard fixed in advance, which is the property every verification mechanism in this book depends on.

> **Definition — Specification.** The written statement of a task you hand to an agent instead of a vague request: what the work is to achieve, what it may use, what counts as done, and when to stop. It is the difference between an informal request and a brief precise enough that somebody other than its author could check whether the result meets it.

Decomposition comes before specification, and it helps to treat them as two distinct acts.
Decomposition is the analytical step of breaking a scientific task into units small enough that each has a single, checkable outcome.
Specification is writing each unit down in a form an agent can execute and a reviewer can audit.
The order matters, because a task decomposed badly cannot be specified well.
A unit that bundles three loosely related outcomes (acquire the data, quality-control it, and summarise the result) resists any single acceptance criterion, and the temptation then is to specify loosely and hope, which is exactly the failure this chapter exists to prevent.
The rule of thumb used here, and developed further in Part II, is that a task is decomposed finely enough when each unit has a stop condition and a check somebody other than its author could apply without further explanation (moderate confidence).
Over-decomposition is a real cost on the other side.
A task split into forty trivial units carries coordination overhead a competent agent could have absorbed inside one, and where the balance sits is a matter of judgement that improves with practice rather than a rule anyone can state once.
What does not vary is the direction of travel: from a vague obligation towards a set of units, each of which says what "done" means before any agent is asked to get there.

## 3.2 Four elements an agent can execute and a human can audit

Four elements make a specification an agent can execute and a human can audit, and every one of them is doing real work: leave any one out and a characteristic failure follows.

The first is the **objective**, a single statement of what the unit of work is to achieve, written as an outcome rather than a procedure.
That distinction is not pedantic.
An objective phrased as a procedure ("run the following steps") forecloses the agent's discretion and wastes what agents are for.
An objective phrased as an outcome ("produce a quality-controlled daily rainfall series for the named stations over the named period, with every rejected value flagged and reasoned") leaves the agent free to plan the route while fixing the destination the route can be judged against.

The second element is the **inputs**: the exact data, files, parameters, conventions and prior artefacts the unit may draw on, named specifically enough that their provenance is recoverable and their absence is an error rather than an invitation to improvise.
Underspecified inputs are the most common quiet defect in practice.
An agent denied a named input will often find a plausible substitute, a different station, a different reference period, a differently versioned file, and carry on without remark, so the output looks defensible and is wrong underneath (high confidence in the pattern; frequency varies by task and model).
Naming inputs precisely is not bureaucratic caution.
It is the main defence against silent substitution.

The third and fourth elements govern the two ends of execution.
**Acceptance criteria** state the conditions the output has to meet to count as done, expressed wherever possible as checks somebody other than the agent can apply: a schema the output must validate against, a numerical tolerance a computed field must fall within, a reconciliation that must balance, or a property that must hold.

> **Definition — Acceptance criteria.** The conditions an output has to meet before it counts as finished, written down in advance and, wherever possible, as checks somebody other than the agent can apply. They say what "correct" means before the work starts, so "it looks right" never stands in for "it passed the check".

Acceptance criteria are how you put the asymmetry from Chapter 1, between what it costs to produce an output and what it costs to verify one, to work.
A criterion is only worth writing if checking it is cheaper than reproducing the work, and a task whose acceptance genuinely needs expert re-derivation is a task to keep on the human side rather than to specify for an agent.

The fourth element is the one most often left out, and the most consequential when it is: the **stop conditions**, meaning the circumstances under which the agent has to halt and hand back rather than continue.

> **Definition — Stop condition.** The rule that tells an agent when to halt, either because it has succeeded and the acceptance criteria are met, or because it has failed and cannot make progress, has used up an agreed budget of attempts, or has hit something the specification did not anticipate. Without the failure kind, an agent that cannot succeed simply does not stop.

Stop conditions come in two kinds, and a complete specification carries both.
Success stops end the unit when the acceptance criteria are met.
Failure stops end it when the agent cannot make progress, has exhausted a budget of attempts or resources, or meets a condition the specification did not anticipate.
The failure kind is what separates a governed workflow from an open-ended one.
Without it, an agent that cannot succeed will not stop.
It will keep spending tokens, time and money on ever more elaborate attempts to satisfy a criterion it cannot meet, and you find out when the bill or the clock intervenes (high confidence; this is among the most reliably observed operational failures).
A stop condition turns that open-ended hazard into a bounded, reviewable event.

## 3.3 A workflow-agnostic specification schema

The four elements compose into a schema that is deliberately independent of any particular workflow, tool or model, and that independence is the point.
A schema tied to a product would date as fast as the product.
A schema tied to the logic of specifying work outlasts the tools that implement it.

Where this schema came from bears on how much weight to put on it, so it is stated plainly.
A search of the literature found no settled academic treatment of specifying tasks for agents in the sense meant here, meaning objective, acceptance criteria and stop conditions written as an auditable artefact.
What does exist in abundance is the neighbouring literature on prompting.
The most systematic survey of it catalogues a sprawling, unstandardised space of dozens of techniques with conflicting terminology, and shows that the choice of technique measurably changes output quality while staying brittle even in expert hands (Schulhoff et al., 2024).
That finding admits two readings, and both point the same way.
Control through input text is real, which is why specification is worth the effort; and it is unreliable, which is why the criteria that decide "done" have to sit outside the model rather than inside the prompt.
The schema below is therefore the book's own synthesis rather than a reproduction of an established standard, offered because the practice needs one and the literature does not yet supply it.
That does not make it idiosyncratic.
A widely followed practitioner formulation, the delegation loop, breaks a delegated task into a goal, the sources the agent should use, a standard the output must meet, an explicit permission boundary and a defined proof that the work is done, which matches the schema here almost element for element, its proof-of-done playing the part of the acceptance criteria (practitioner commentary; see the references).

The schema names the four elements already introduced (objective, inputs, acceptance criteria, stop conditions) and adds three fields that experience says are needed to make a specification auditable rather than merely executable.
The first addition is an explicit statement of **assumptions and conventions**: the units, coordinate reference systems, calendar conventions, missing-value codes and domain defaults the unit takes for granted.
Write them down, because an unstated convention is an ungoverned one, and because the unit-conversion failures of §3.1 and Chapter 13 live exactly in the gap between a convention one party assumed and another did not.
The second is a **provenance requirement**: what the unit must record about its own execution, meaning inputs consumed with their versions, decisions taken, and values rejected with reasons, so the output arrives with the audit trail Chapter 12 depends on instead of needing one reconstructed later.
The third is an explicit naming of the **reviewer**: who or what applies the acceptance criteria, and whether that party is the agent itself (weak), a separate agent (stronger), or a human (strongest for consequential decisions).
That field matters because an acceptance criterion with nobody named to apply it is decorative.
This seven-field schema does real work in two later chapters, which is why it is introduced here.
Chapter 10 derives an agent roster from a specification by reading its units and reviewers and assigning each to an actor, and Chapter 15 carries a single specification through an entire governed modelling workflow from this schema to a publication run.
Learn it here and both of those chapters become elaborations of it rather than new material.

**Figure 3.1 — Specification anatomy.**

![A box labelled specification containing two columns. The left column stacks four fields, objective, inputs, acceptance criteria and stop conditions, bracketed as the part that makes the work executable by an agent, each with a one-line note: state an outcome not a procedure; name them exactly, because an unnamed input gets substituted silently; write checks somebody else could apply; and say when to stop succeeding and when to stop failing. The right column stacks three more, assumptions and conventions, provenance requirement and reviewer, bracketed as the part that makes the work auditable by a human, noted respectively as units, grids, calendars and missing-value codes written down; what the run must record about itself; and who applies the criteria, because a criterion with nobody named is decorative. An agent glyph reads the box from the left; the acceptance-criteria field connects to a check diamond applied by the named human reviewer.](../figures/figure-3-1.svg)

*Figure 3.1 — Seven fields, in two groups. The four on the left are what lets an agent execute the work; the three on the right are what lets a human audit it afterwards. Those three are the ones most often left out. The reviewer field is the one that makes the rest bite: an acceptance criterion with nobody named to apply it is decoration. This schema comes back in Chapters 10 and 15. (Rendered as `figures/figure-3-1.svg` from the brief below, per `FIGURES.md`.)*

```
FIGURE BRIEF
- id:            Figure 3.1
- title:         The seven fields of a specification
- type:          architecture
- claim:         A specification is a fixed structure of seven fields; the four core fields make it executable, the three added fields make it auditable, and a named reviewer closes the loop.
- standfirst:    Four fields let an agent do the work; three more let a human check it.
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
- annotations:   on "objective", "state an outcome, not a procedure"; on "inputs", "name
                 them exactly — an unnamed input gets substituted silently"; on "acceptance
                 criteria", "checks somebody other than the agent could apply"; on "stop
                 conditions", "when to stop succeeding, and when to stop failing"; on
                 "assumptions & conventions", "units, grids, calendars, missing-value
                 codes — written down, or ungoverned"; on "provenance requirement", "what
                 the run must record about itself"; on "reviewer", "a criterion with nobody
                 named to apply it is decorative"
- caption:       Figure 3.1 — Seven fields, in two groups. The four on the left are what lets an agent execute the work; the three on the right are what lets a human audit it afterwards. Those three are the ones most often left out. The reviewer field is the one that makes the rest bite: an acceptance criterion with nobody named to apply it is decoration. This schema comes back in Chapters 10 and 15.
- alt-text:      A box labelled specification containing two columns. The left column stacks four fields, objective, inputs, acceptance criteria and stop conditions, bracketed as the part that makes the work executable by an agent, each with a one-line note: state an outcome not a procedure; name them exactly, because an unnamed input gets substituted silently; write checks somebody else could apply; and say when to stop succeeding and when to stop failing. The right column stacks three more, assumptions and conventions, provenance requirement and reviewer, bracketed as the part that makes the work auditable by a human, noted respectively as units, grids, calendars and missing-value codes written down; what the run must record about itself; and who applies the criteria, because a criterion with nobody named is decorative. An agent glyph reads the box from the left; the acceptance-criteria field connects to a check diamond applied by the named human reviewer.
- infographic description: A flat vector architecture diagram on an off-white background,
                 16:9. Title top-left: "The seven fields of a specification". Standfirst
                 beneath: "Four fields let an agent do the work; three more let a human
                 check it." A large grey-bordered rounded rectangle "specification" fills
                 the centre. Inside, a left column of four blue tags stacked vertically,
                 each with a one-line annotation in smaller type to its right: "objective"
                 / "state an outcome, not a procedure"; "inputs" / "name them exactly — an
                 unnamed input gets substituted silently"; "acceptance criteria" / "checks
                 somebody other than the agent could apply"; "stop conditions" / "when to
                 stop succeeding, and when to stop failing". A right column of three
                 sky-blue tags, similarly annotated: "assumptions & conventions" / "units,
                 grids, calendars, missing-value codes — written down, or ungoverned";
                 "provenance requirement" / "what the run must record about itself";
                 "reviewer" / "a criterion with nobody named to apply it is decorative". A
                 thin bracket beside the left column is labelled "executable"; one beside
                 the right column, "auditable". To the left of the whole rectangle, a small
                 orange rounded-square agent glyph with a loop arrow connects rightward
                 into it. The "acceptance criteria" tag connects by a single line to a
                 vermillion diamond "check" near the right edge, with a blue
                 head-and-shoulders icon "reviewer" beside it. Generous margins, single
                 arrowhead style, sentence case.
```

## 3.4 The specification is where you actually keep control

The specification is the main way you exercise control over an agentic workflow, and recognising that changes where attention and scepticism are worth spending.

In a conventional analysis you control the work by writing and reading every line of the procedure.
In an agentic workflow the procedure is generated, so trying to regain control by reading every generated step does not scale and misplaces the effort anyway.
The steps are numerous, revisable, and not where the consequential decisions were made.
Those decisions were made in the specification: what counts as done, what inputs are admissible, when to stop.
So the specification is where review effort pays best, and where an institution's governance should attach.
There is a striking parallel in the research literature.
The most realistic agent benchmarks now govern behaviour with an explicit written policy document the agent must obey, score a run by comparing the final state of the world against an annotated goal state, and find that a large share of failures are violations of that policy rather than failures of raw capability (Yao et al., 2024).
That is the same claim from the other direction: behaviour is controlled by an auditable written artefact, and where the artefact is thin, the work drifts.

This has a practical corollary that Part III develops at length.
A workflow is auditable to the degree that its specifications are legible.
An organisation that keeps its specifications under version control, reviews them before execution rather than only inspecting outputs afterwards, and treats a change to a specification with the same care as a change to a method, has built the foundation that provenance (Chapter 12) and end-to-end governance (Chapter 15) sit on.
The limitation, plainly: a specification controls only what it addresses.
Discretion the specification leaves open is still real discretion, exercised by the agent out of sight.
That is why the craft of §3.2, closing the gaps that matter while leaving open the ones that do not, is control rather than mere documentation, and why a specification is written, reviewed and revised as an artefact in its own right instead of dashed off as a preamble to the real work.

## 3.5 Worked example: from "verify this rainfall forecast" to an auditable specification

An informal request shows the distance between a wish and a specification better than any general argument, and this one comes from operational practice: *verify this rainfall forecast*.

As it stands that is a wish, and handing it to an agent produces exactly the weak, conversational pattern this chapter argues against.
The request gets typed as written.
The agent, with no fixed objective, no named inputs, no acceptance criteria and no stop conditions, quietly picks all four for itself.
It settles on some notion of what "verify" means, finds whatever forecast and whatever observations it can reach, computes whatever score it favours, and returns a fluent summary that looks like an answer.
Each of those four silent choices is a decision the scientist should have made and can no longer see, and the plausibility of the output is the hazard rather than the reassurance, because a wrong verification that looks right is worse than an obvious error.
The specific ways this goes wrong in a rainfall context are concrete and familiar: the agent scores against the wrong reference dataset, or over a period that includes a known gauge outage, or with a metric insensitive to the very thing the forecast exists to get right, the timing and placement of heavy-rainfall events **[AUTHOR: name the specific metric-mismatch failure you have seen an unspecified verification produce — e.g. a good aggregate score masking poor placement of a convective event — and describe how it surfaced]**.

The strong version replaces every silent choice with a written field, and that swap is the whole lesson of the chapter made concrete.
The **objective** becomes a single outcome: produce a verification of the named forecast against the named reference, reporting the named metrics with their uncertainty, over the named domain and period.
The **inputs** are named exactly: the forecast product and its issue time, the reference observation or analysis dataset and its version, the spatial domain, the aggregation period, and the treatment of the forecast's probabilistic structure **[AUTHOR: specify the exact forecast product, reference dataset, domain, lead times and accumulation period from the operational case you are drawing on]**.
The **acceptance criteria** fix what a valid verification has to satisfy: the metrics computed are the ones the objective names and are appropriate to the quantity, so for rainfall they are scores proper for a skewed, intermittent variable and sensitive to spatial displacement rather than to aggregate bias alone; the reference period excludes intervals flagged for instrument outage; and every score carries an uncertainty estimate **[AUTHOR: state the exact metrics, the properness/sensitivity requirements, and the confidence-interval method the toolkit uses]**.
The **stop conditions** bound the run at both ends: succeed and halt when the criteria are met, and stop and hand back if a named input is missing or mis-versioned, if the reference series has more than a stated fraction of missing values in the target period, or if the two fields cannot be brought onto a common grid without a reprojection the specification did not authorise **[AUTHOR: give the concrete thresholds — acceptable missing-data fraction, permitted regridding — from practice]**.
Set beside the weak version, the strong specification has not made the verification correct.
It has made a wrong verification detectable, turned four invisible decisions into four reviewable ones, and produced, as a by-product, the provenance record a downstream reader or an institutional auditor will need.
The measured claim to finish on is that this conversion is the ordinary unit of agentic scientific work.
It is not a ceremony reserved for high-stakes runs, but the routine act by which any task worth delegating gets prepared (high confidence, on the reasoning of §§3.1–3.4).

**Figure 3.2 — Weak specification versus strong specification.**

![A two-panel before-and-after diagram. In the upper panel, labelled weak, a person says "verify this rainfall forecast" to an agent, which emits four question tags, which metric, which reference, which period and when to stop. The panel is annotated that the agent answers all four itself, silently, and the output is flagged plausible but unauditable, with a note that a wrong verification that looks right is worse than an obvious error. In the lower panel, labelled strong, the same request passes through a specification block whose four fields are filled in by the scientist rather than the agent, then through a check, to an output flagged auditable. A note reads that this has not made the verification correct, it has made a wrong one detectable.](../figures/figure-3-2.svg)

*Figure 3.2 — The same request, twice. Left conversational, the agent quietly answers four questions the scientist should have answered, and the fluent result is the hazard rather than the reassurance. Specified, those four choices become four written fields and four reviewable decisions. Note what this does not buy you: the specification does not make the verification correct, it makes a wrong one detectable. (Rendered as `figures/figure-3-2.svg` from the brief below, per `FIGURES.md`.)*

```
FIGURE BRIEF
- id:            Figure 3.2
- title:         "Verify this rainfall forecast" — weak and strong
- type:          before/after
- claim:         The same request produces an unauditable result when left conversational and an auditable one when specified; the difference is four fields the scientist fills rather than the agent.
- standfirst:    Four choices get made either way — the only question is by whom.
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
- annotations:   upper panel, on the four question tags, "the agent answers all four
                 itself, silently"; upper panel, on the output, "a wrong verification that
                 looks right is worse than an obvious error"; lower panel, on the
                 specification block, "the scientist answers the same four, in writing,
                 before the run"; lower panel, on the check, "now somebody other than the
                 agent can test it"; lower panel, on the output, "this has not made the
                 verification correct — it has made a wrong one detectable"
- caption:       Figure 3.2 — The same request, twice. Left conversational, the agent quietly answers four questions the scientist should have answered, and the fluent result is the hazard rather than the reassurance. Specified, those four choices become four written fields and four reviewable decisions. Note what this does not buy you: the specification does not make the verification correct, it makes a wrong one detectable.
- alt-text:      A two-panel before-and-after diagram. In the upper panel, labelled weak, a person says "verify this rainfall forecast" to an agent, which emits four question tags, which metric, which reference, which period and when to stop. The panel is annotated that the agent answers all four itself, silently, and the output is flagged plausible but unauditable, with a note that a wrong verification that looks right is worse than an obvious error. In the lower panel, labelled strong, the same request passes through a specification block whose four fields are filled in by the scientist rather than the agent, then through a check, to an output flagged auditable. A note reads that this has not made the verification correct, it has made a wrong one detectable.
- infographic description: A flat vector before-and-after diagram on an off-white
                 background, 16:9, two stacked panels of equal width sharing the same
                 layout. Title top-left: "\"Verify this rainfall forecast\" — weak and
                 strong". Standfirst beneath: "Four choices get made either way — the only
                 question is by whom." Upper panel labelled "weak (conversational)": a blue
                 head-and-shoulders icon with a speech bubble "verify this rainfall
                 forecast" connects rightward to an orange rounded-square agent glyph; four
                 small grey tags fan from the agent reading "which metric?", "which
                 reference?", "which period?", "when to stop?", with a shared annotation
                 beneath them "the agent answers all four itself, silently"; these lead to
                 a plain output box with a small vermillion warning triangle "plausible,
                 unauditable", annotated "a wrong verification that looks right is worse
                 than an obvious error". Lower panel labelled "strong (specified)": the
                 same blue icon and orange agent, but between them a grey-bordered block
                 holding four filled blue tags stacked — "objective", "inputs", "acceptance
                 criteria", "stop conditions" — annotated "the scientist answers the same
                 four, in writing, before the run"; these connect through a vermillion
                 diamond "check", annotated "now somebody other than the agent can test
                 it", to an output box with a tick "auditable", annotated "this has not
                 made the verification correct — it has made a wrong one detectable".
                 Generous margins, single-weight lines, one arrowhead style, sentence case.
```

## 3.6 The anti-pattern: conversational drift in place of specification

The dominant anti-pattern in agentic scientific work is conversational drift: a specification gradually replaced by an accumulating chat transcript, where the task is never written down but negotiated turn by turn until neither party could reconstruct what was agreed.

The pattern is seductive precisely because the conversational interface is this technology's most immediate strength, and because the early exchanges genuinely help, by clarifying, correcting and exploring.
So the move from productive dialogue into ungoverned drift happens gradually and is rarely noticed at the moment it happens.
Its symptoms are recognisable once named.
The objective mutates across turns without any turn marking the change.
Inputs get referred to as "that file" and "the other dataset" rather than named.
Acceptance is asserted by the agent ("this looks correct") rather than checked against a fixed standard.
And there is no stop condition, so the session ends when the scientist tires rather than when the work is done.

The damage is not only that such a session can go wrong.
It is that when it does, there is nothing to audit: no artefact saying what should have happened, only a transcript of what was said.
A workflow that cannot be audited cannot be governed, whatever its outputs happen to look like (high confidence).
The remedy is not to abandon conversation, which would give up a real strength, but to give it its proper place.
Conversation is where a specification gets discovered and refined, and it earns its keep only when it ends in a written specification the execution is then held to.
The discipline this chapter asks for fits in one sentence: talk to find the specification, then execute against it.
Everything that follows, from the patterns of Part II to the end-to-end governance of Chapter 15, depends on that transition being made deliberately and made visible, rather than never being made at all.

[ai-reviewer: a consequence of the placement that the plan predicted only halfway. It said §3.6 would end on "…rather than never being made at all", "which is a stronger close", and it does. But those sentences were the chapter's close, not §3.6's, and the chapter now ends on the boundary of the discipline instead of on the discipline. A chapter titled "Specifying work for agents" whose final movement says a great deal of good science cannot be specified is making an honest point in the position of maximum emphasis. That may be exactly right, since F7's charge was that the concession was under-weighted. It is still a change to the chapter's argumentative shape that nobody appears to have chosen deliberately, and it is the author's to endorse or reverse. The mechanical alternatives, if it is to be reversed, are to move §3.6's two closing sentences to the end of §3.7 or to give the chapter a short closing pointer as Chapters 2 and 16 have; both are ai-writer's work, not mine.]
[ai-writer: the second alternative is now in place. The chapter closes with the house two-line pointer that Chapter 2 uses, which restates what the chapter did and hands on to Chapter 4, so the last thing a reader meets is the discipline rather than its boundary. I have not moved §3.6's closing sentences, because §3.7's own argument depends on arriving after the anti-pattern rather than before it. The comment is left standing because the question underneath it is the author's and the pointer does not settle it: §3.7 is still the final section, and if the author wants the concession weighted lower than F7 asked, the fix is a decision about emphasis rather than another rearrangement.]

## 3.7 When you cannot yet write a specification

A gauge in your network has been reading high against two of its five neighbours since the spring.
There is no objective to write down yet.
You do not know whether this is a sensor fault, a change in the catchment, a change in the neighbours, or a bookkeeping error in the ingest.
What you have is something odd in a record and a reason to look at it.
A lot of good environmental science starts exactly there, and nothing in this chapter applies to it yet.

That is a boundary of the discipline rather than a failure of it.
The anti-pattern of §3.6 is having no specification at all and drifting through a conversation until nobody could say what was agreed.
Writing one too early is the opposite error.
A specification written before you understand the problem fixes the wrong target, and fixes it precisely, which is worse than leaving it open.
Acceptance criteria for a question you have not formed yet are only your first guess, given the authority of a written rule.

So what holds exploration to account, if acceptance criteria cannot?
Two things, and neither of them is a check on the output.
The first is a bounded budget: how many attempts, how much of your time, how much compute, decided before you start and written where the objective would have gone.
An exploration that has spent its budget stops and reports what it found, which may be nothing.
The second is a record kept as the work happens rather than reconstructed afterwards: what you tried, what it showed, what you ruled out, and what you would try next.
Reconstructed records are the ones that quietly leave out the attempts that failed, which is exactly the information that stops the next person repeating them.
Both of those are practices I recommend rather than practices anybody has measured (moderate confidence).

One rule governs both.
Nothing found in exploration enters the evidential chain until it has been re-derived under a specification, which is the hypothesis-provenance gate of Chapter 8 §8.4 in its general form.
An exploratory run may generate a hypothesis; it may not supply the evidence for it.
Knowing when exploration has yielded enough to specify is a judgement, and it is one this book can name but cannot supply.
It is the same judgement as knowing when a pilot study is finished, and it is learned the same way, by doing it and being wrong about it.
The kind of governance this book teaches, a check the output has to pass, reaches only the half of the work that can be specified.
The other half gets these two weaker disciplines instead, and that is the boundary the front matter's scope statement draws.

**[AUTHOR: an exploratory episode of your own that could not have been specified in advance, and what you kept a record of while it was running — this section is asserting a practice, and one lived instance would make it a description instead.]**

---

*This chapter has turned a vague request into a written specification with an objective, inputs, acceptance criteria and stop conditions, shown where control actually sits, and marked the boundary past which the discipline has nothing to bite on.*
*The next chapter asks the question that comes before any of it: which parts of the research cycle should be handed to an agent at all, and which should not.*

---

### References (verify details before release)

- Jones, N. B. (2026). "Codex: your first personal AI agent delegation loop." Video, @natebjones, 12 June 2026. https://www.youtube.com/watch?v=xqGCbEDbny8 (practitioner commentary; concepts cited as corroboration, not evidence)
- Schulhoff, S., Ilie, M., Balepur, N., et al. (2024). The prompt report: a systematic survey of prompt engineering techniques. *arXiv preprint.* https://arxiv.org/abs/2406.06608
- Yao, S., Shinn, N., Razavi, P. and Narasimhan, K. (2024). τ-bench: a benchmark for tool-agent-user interaction in real-world domains. *arXiv preprint.* https://arxiv.org/abs/2406.12045
