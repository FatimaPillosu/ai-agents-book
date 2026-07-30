# Chapter 4 — The scientist's stance

> **Status:** draft r6 · voice v5.0 (`STYLE.md` §1) · sentence-per-line per `STYLE.md` §10 · figures as briefs per `FIGURES.md`.
> **Conventions:** vendor-neutral (outline §9) · **[AUTHOR: …]** marks lived material only the author can supply · **[verify]** marks real but unconfirmed details · citations drawn only from verified reports in `/research`. Nothing has been invented.

---

## 4.1 Where an agent fits the scientific method

An agent is a tool.
It works for your judgement, and it does not stand in for it.
So the question worth asking is not what an agent can do, but which parts of your research you can sensibly hand to one.

Think about how a piece of work actually moves.
A question turns into a hypothesis, the hypothesis into a design, the design into data and analysis, and the analysis back into interpretation, communication and the next question.
Those stages don't ask the same thing of you.
Some are jobs with a right answer.
Reformat a decade of gauge records into a common schema and there is a correct result, which a second procedure can check.
Others are calls only you can make.
Whether a departure from the record is a real hydrological signal or a sensor fault is your judgement, and you are the one accountable for it.

The tempting conclusion is that agents take the first kind of stage and you keep the second.
It doesn't work like that, because both kinds of work turn up inside every stage.
Data preparation is full of judgement calls.
Interpretation is full of steps that can be checked.
So you end up deciding this one task at a time, not one phase at a time.
Where a task is not yet statable at all, this procedure has nothing to work on, and Chapter 3 §3.7 says what governs the work until it is.

## 4.2 Augmentation and automation are different commitments

Augmenting a scientist and automating a task sound like the same thing at different volumes.
They aren't.
The difference is who exercises judgement.

With augmentation you stay in every instance of the work.
The agent just increases what you can finish in an afternoon: a wider literature, a larger reprocessing job, a figure produced in fewer steps.
With automation you step out of each instance.
The agent runs, and nobody looks at its outputs one by one before they are used.

Most real workflows sit somewhere between those two, and it helps to have words for the gradations.
One recent framework names them by the role you keep: operator, collaborator, consultant, approver, observer (Feng et al., 2025).
Its useful point is that this role is something you choose when you build the workflow.
It is not handed to you by how capable the agent happens to be.
The framework is a recent proposal rather than a settled standard, so treat it as vocabulary and not as a rule (moderate confidence).

Here is the question to ask before any of this goes live.
Not "can the agent do this?", but "what happens to an error the agent makes here, and who answers for it?".
The first question is about capability, and capability isn't what decides the matter.
A plausible failure (Chapter 1) survives however good the agent gets.
The second question is about whether the failure would be caught, and what it would cost if it weren't.
You can answer that one with the specification (Chapter 3) and verification (Chapter 11) practices your group already has.
Commercial framing and early scientific enthusiasm both have this the wrong way round.
They treat automation as the goal and augmentation as a stage on the way there.
It runs the other way.
Automation is the special case, allowed only where a task has been shown to tolerate the loss of human judgement, and augmentation is the default for most scientific work.

There is also evidence that a more elaborate agent is not automatically a better one.
Researchers benchmarked elaborate agent architectures against a plain model wrapped in a basic retry loop.
On a standard coding task the simple baseline matched them, at a fraction of the cost (Kapoor et al., 2024).
Autonomy is a cost you have to justify, not a good in itself.
And it isn't a fixed property of the agent either.
The same agent is augmentation in one workflow and automation in another, depending only on whether a human forms a judgement between its output and its use.

## 4.3 A decision procedure: should an agent do this?

Two questions decide where an agent goes, and neither of them is about the agent.

The first: what does it cost to check the output?
A test suite, a schema or a checksum settles that cheaply.
Interpretation, missing context or an open research question does not.

The second: what does a wrong output cost if nobody catches it?
A mislabelled intermediate file, spotted before anything uses it, costs almost nothing to undo.
An error that reaches an issued flood warning, a published result or an overwritten dataset cannot be undone at any price.

Put the two together and you get four cases.
Cheap to check, reversible if wrong: let the agent run with little or no supervision.
Cheap to check, severe if wrong: the agent can act, but only behind a gate that makes the check mandatory.
Expensive to check, reversible if wrong: the agent drafts, you check, and the workflow has to budget for the checking.
Expensive to check and severe if wrong: this one is not the agent's, however capable it is, because what rules it out belongs to the task and not to the tool.
The two middle cases are the same arrangement twice: the propose–dispose separation of Chapter 2 §2.6, with a rule disposing in one and a person in the other.

The underlying discipline is to build the simplest thing that meets the task, and to add agentic components only where the task visibly demands them (Anthropic, 2024).
Practitioners put it more bluntly: if a fixed sequence of steps with at most a judgement call or two would do the job, build a workflow and not an agent (AI Founders, 2026).
The catch is that both of those questions are answered before the work starts.
Guessing wrong is its own failure, whether you believed the checking would be cheaper than it turned out to be, or the output more reversible than it was.

**Figure 4.1 — Should an agent do this?**

![A top-to-bottom decision flowchart. A task meets a first gate asking whether it is a matter of accountability, interpretation or authorship; a yes routes it to a human-only terminal marked do not delegate, annotated that no improvement in capability changes this answer. A no leads to a second gate asking whether verification is cheap, annotated that a test suite, a schema or a checksum counts as cheap while interpretation does not. Each branch then meets a gate asking whether a wrong output is reversible, annotated that a mislabelled intermediate file is reversible and an issued flood warning is not. The four combinations lead to four outcomes: the agent runs with little or no supervision; the agent acts but only behind a mandatory gate; the agent drafts and a human checks, with the workflow budgeting for the checking; and, for tasks expensive to verify and irreversible if wrong, back to the human-only terminal. A bracket groups the three agent outcomes as augmentation.](../figures/figure-4-1.svg)

*Figure 4.1 — Two questions decide where a task goes, and neither is about how capable the agent is. The first gate removes what was never an instrument's to do at all: accountability, interpretation, authorship. What survives is sorted by what checking costs against what a wrong answer costs, and the four combinations give four different working arrangements. (Rendered as `figures/figure-4-1.svg` from the brief below, per `FIGURES.md`.)*

```
FIGURE BRIEF
- id:            Figure 4.1
- title:         Should an agent do this?
- type:          decision flowchart
- claim:         Whether to delegate a task to an agent is decided by two questions (whether the output is an act of judgement or accountability, and how cheap verification is against how reversible the consequence), not by how capable the agent is.
- standfirst:    Neither question is about how good the agent is.
- canvas:        16:9
- elements:      a start node "task" (grey); first diamond gate "is this accountability,
                 interpretation or authorship?" (vermillion); a terminal "human only — do
                 not delegate" (blue human icon) on its yes-exit; second diamond gate "is
                 verification cheap?" (vermillion) on its no-exit; third diamond gate "is a
                 wrong output reversible / low-consequence?" (vermillion); three agent-role
                 terminals in orange — "agent runs, light supervision", "agent acts behind
                 a mandatory gate", "agent drafts only, human verifies"; one blue "human
                 only" terminal
- flow:          top-to-bottom. task → gate 1. Gate 1 "yes" → "human only — do not
                 delegate". Gate 1 "no" → gate 2 "is verification cheap?". Gate 2 "yes" →
                 gate 3a "reversible?"; gate 2 "no" → gate 3b "reversible?". From gate 3a:
                 "yes" → "agent runs, light supervision"; "no" → "agent acts behind a
                 mandatory gate". From gate 3b: "yes" → "agent drafts only, human
                 verifies"; "no" → "human only — do not delegate"
- labels:        "task", "accountability, interpretation or authorship?", "human only — do
                 not delegate", "verification cheap?", "reversible / low-consequence?",
                 "agent runs, light supervision", "agent acts behind a mandatory gate",
                 "agent drafts only, human verifies", "yes", "no"
- annotations:   on gate 1, "no improvement in capability changes this answer"; on gate 2,
                 "cheap: a test suite, a schema, a checksum. Not cheap: interpretation, or
                 an unresolved research question"; on the reversibility gates, "reversible:
                 a mislabelled intermediate file. Not reversible: an issued flood warning,
                 a published result"; on "agent acts behind a mandatory gate", "the check
                 is mandatory, not advisory"; on "agent drafts only, human verifies", "the
                 workflow has to budget for the checking"; a bracket grouping the three
                 orange terminals, "augmentation — a human stands between output and use";
                 on the human-only terminal, "not an instrument's to do"
- caption:       Figure 4.1 — Two questions decide where a task goes, and neither is about how capable the agent is. The first gate removes what was never an instrument's to do at all: accountability, interpretation, authorship. What survives is sorted by what checking costs against what a wrong answer costs, and the four combinations give four different working arrangements.
- alt-text:      A top-to-bottom decision flowchart. A task meets a first gate asking whether it is a matter of accountability, interpretation or authorship; a yes routes it to a human-only terminal marked do not delegate, annotated that no improvement in capability changes this answer. A no leads to a second gate asking whether verification is cheap, annotated that a test suite, a schema or a checksum counts as cheap while interpretation does not. Each branch then meets a gate asking whether a wrong output is reversible, annotated that a mislabelled intermediate file is reversible and an issued flood warning is not. The four combinations lead to four outcomes: the agent runs with little or no supervision; the agent acts but only behind a mandatory gate; the agent drafts and a human checks, with the workflow budgeting for the checking; and, for tasks expensive to verify and irreversible if wrong, back to the human-only terminal. A bracket groups the three agent outcomes as augmentation.
- infographic description: A flat vector decision flowchart on an off-white background,
                 16:9, flowing top to bottom. Title top-left: "Should an agent do this?"
                 Standfirst beneath: "Neither question is about how good the agent is." At
                 the top a small grey rounded rectangle "task" connects down to a vermillion
                 diamond "accountability, interpretation or authorship?", annotated to its
                 left "no improvement in capability changes this answer". Its "yes" exit
                 leads right to a blue head-and-shoulders terminal "human only — do not
                 delegate", annotated "not an instrument's to do". Its "no" exit leads down
                 to a second vermillion diamond "verification cheap?", annotated "cheap: a
                 test suite, a schema, a checksum. Not cheap: interpretation, or an
                 unresolved research question". That diamond's "yes" and "no" exits each
                 lead to a vermillion diamond "reversible / low-consequence?", sharing one
                 annotation "reversible: a mislabelled intermediate file. Not reversible: an
                 issued flood warning, a published result". From the left diamond: "yes" to
                 an orange rounded rectangle "agent runs, light supervision"; "no" to an
                 orange rounded rectangle "agent acts behind a mandatory gate", annotated
                 "the check is mandatory, not advisory". From the right diamond: "yes" to an
                 orange rounded rectangle "agent drafts only, human verifies", annotated
                 "the workflow has to budget for the checking"; "no" to the same blue "human
                 only — do not delegate" terminal. A thin bracket groups the three orange
                 terminals, labelled "augmentation — a human stands between output and use".
                 Single-weight connectors, one arrowhead style, generous spacing, sentence
                 case.
```

## 4.4 The frontier that does not move

Both of §4.3's questions are answered by facts about the task, not facts about the model.
What it costs to check an output is set by whether a reference answer exists, whether a rule can decide the case, and whether the answer is interpretive.
What a wrong output costs is set by what the output is used for, and by how far it travels before anyone would notice.
Those are the same properties whether the work is done by an agent, a doctoral student or a shell script.
That is worth holding on to, because almost everything else in this field is quoted as a property of the model.

Capability progress is real and it is measured.
An independent evaluation organisation finds the duration of tasks an agent can complete unaided doubling roughly every four months since 2023 (METR, 2026).
A frontier-model developer reports much the same rate from its own telemetry, which is self-reported evidence from a party with an interest in the answer (Anthropic Institute, 2026).
What that curve describes is the generation side of the asymmetry.
A better model produces more output, faster, at higher quality, across more kinds of task.
Every one of those gains applies to the production side, which was already the cheap one.

What the curve does not touch is the checking side.
Whether a reference answer exists for a task is a fact about the task.
Whether a rule can decide the case is a fact about the case.
Whether the answer is interpretive is a fact about the question being asked.
A model that is twice as capable does not make a reference dataset exist where there was none.
It does not make an open research question decidable by rule, and it does not make an interpretation checkable by anything except another interpretation.
The structure that sets checking cost sits in the task, so improving the model does not move it.

The conclusion follows from those two facts.
The class of scientific tasks where an agent pays off is bounded by what it costs to check the work, and checking cost is a property of the task.
So that class does not grow as models improve, and the frontier of safe delegation moves far less than the capability curve suggests.
This is not a prediction about the technology.
It is a statement about which of the two costs the technology acts on.

Better models do make some previously expensive checks cheap, and they do it by changing the form the output arrives in.
An answer that arrives as structured data can be validated against a schema; an answer that arrives with executable tests can be run; an answer that arrives with resolvable references can be resolved.
None of those checks was available when the same answer arrived as prose.
So the class does widen at the margin, and the argument above overstates itself if it is read as saying the boundary is fixed.
The claim is narrower than that.
The widening is second-order against the capability curve, because it depends on the task admitting a checkable form at all, and most expensive-to-check tasks do not (moderate-to-high confidence).

What this changes is the posture, not the enthusiasm.
"Adopt this, carefully" is advice that needs rewriting with every release, because it treats the limit as temporary.
What follows from the argument here is different: adopt this where checking is cheap, for reasons you can state.
Then expect that set of places to look much the same in five years.
The tasks on the cheap-to-check side are largely the routine and semi-routine work surrounding science rather than the science itself.
That is the scope the front matter claims for this book.
If that sounds like a smaller promise than the field usually makes, it is, and it is the one I can defend.

## 4.5 What does not transfer to an instrument

Three things in scientific work never transfer to a tool, however good the tool gets.

Accountability is being the named person who answers for a decision and its consequences.
Interpretation is deciding what a result means, using context you hold and the system does not.
Authorship is the standing to claim a contribution and defend it as your own.

The first gate of the procedure takes all three off the table before verification cost is even considered, and not because they are difficult.
No better model closes these limits, because none of them is a shortfall in capability.
Each one is a property of the relationship between you and the community that holds you to account.

Treating them as automatable is the most consequential mistake in the field, and an agent makes it an easy mistake to make.
Its output in an interpretive register reads exactly like the interpretation you would have written.
The protection is remembering that how easy something is to ask for tells you nothing about whether you should be asking.
"Tell me whether this trend is significant" is as easy to type as "reformat these files".
Only one of them gets through the first gate.

Two last things.
Even an allowable task is not always worth handing over: if checking the agent's output costs you more than doing the job yourself, the procedure says don't delegate, however well the agent performs.
And when you genuinely can't tell where a task belongs, the safe default is augmentation under supervision rather than automation.
That keeps the human judgement a bad delegation would have removed.
Keeping it costs you time. Losing it costs the correctness of the science.

---

### References (verify details before release)

- AI Founders (2026). "Don't build an AI agent until you can answer these 8 questions." Video, @aifoundershq, 17 May 2026. https://www.youtube.com/watch?v=jMHawg6qpps
- Anthropic (2024). Building effective agents. *Anthropic engineering blog.* https://www.anthropic.com/engineering/building-effective-agents
- Anthropic Institute (Favaro, M. and Clark, J.) (2026). When AI builds itself. *The Anthropic Institute.* https://www.anthropic.com/institute/recursive-self-improvement
- Feng, K. J. K., McDonald, D. W. and Zhang, A. X. (2025). Levels of autonomy for AI agents. *arXiv preprint.* https://arxiv.org/abs/2506.12469
- Kapoor, S., Stroebl, B., Siegel, Z. S., Nadgir, N. and Narayanan, A. (2024). AI agents that matter. *arXiv preprint.* https://arxiv.org/abs/2407.01502
- METR (2026). Time Horizon 1.1. *METR research blog*, 29 January 2026. https://metr.org/blog/2026-1-29-time-horizon-1-1/
