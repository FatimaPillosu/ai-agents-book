# Chapter 4 — The scientist's stance

> **Status:** draft r5-colloquial · **experimental voice variant, not house style** · sentence-per-line per `STYLE.md` §10 · figures as briefs per `FIGURES.md`.
> **Voice note:** this version deliberately departs from `STYLE.md` v3.4 on the author's instruction (26 Jul 2026), for Chapter 4 only. It addresses the reader as "you", uses contractions and shorter sentences, and drops the impersonal register of §1. Everything else in `STYLE.md` still holds: no metaphors (§12.2), no hype, British English, and every citation drawn from the verified reports in `/research`. If this voice is adopted, `STYLE.md` needs amending before it spreads to other chapters; if it is not, `claude/manuscript-feedback-e2xcop` holds the house-style version of this chapter.
> **Conventions:** vendor-neutral (outline §9) · **[AUTHOR: …]** marks lived material only the author can supply · **[verify]** marks real but unconfirmed details. Nothing has been invented.

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
The second question is about whether the failure would be caught, and what it would cost if it weren't, and you can answer it with the specification (Chapter 3) and verification (Chapter 11) practices your group already has.
Commercial framing and early scientific enthusiasm both have this the wrong way round.
They treat automation as the goal and augmentation as a stage on the way there.
It runs the other way: automation is the special case, allowed only where a task has been shown to tolerate the loss of human judgement, and augmentation is the default for most scientific work.

There is also evidence that more machinery is not automatically better.
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

The underlying discipline is to build the simplest thing that meets the task, and to add agentic components only where the task visibly demands them (Anthropic, 2024).
Practitioners put it more bluntly: if a fixed sequence of steps with at most a judgement call or two would do the job, build a workflow and not an agent (AI Founders, 2026).
The catch is that both of those questions are answered before the work starts.
Guessing wrong is its own failure, whether you believed the checking would be cheaper than it turned out to be, or the output more reversible than it was.

**Figure 4.1 — Should an agent do this?**

![A top-to-bottom decision flowchart. A task first meets the question of whether it is a matter of accountability, interpretation or authorship; if yes, it is routed to a human-only terminal marked do not delegate. If no, a second question asks whether verification is cheap, and a third whether a wrong output is reversible. The four combinations route to agent runs with light supervision, agent acts behind a mandatory gate, agent drafts only with human verification, or, for expensive-to-verify and irreversible tasks, back to the human-only terminal.](../figures/figure-4-1.svg)

*Figure 4.1 — A placement procedure for delegation. The first gate removes what does not transfer to an instrument at all: accountability, interpretation, authorship; the remaining gates trade verification cost against reversibility to sort the rest into supervised, gated or draft-only agent roles. (Rendered as `figures/figure-4-1.svg` from the brief below, per `FIGURES.md`.)*

```
FIGURE BRIEF
- id:            Figure 4.1
- title:         Should an agent do this? A placement decision procedure
- type:          decision flowchart
- claim:         Whether to delegate a task to an agent is decided by two questions (whether the output is an act of judgement or accountability, and how cheap verification is against how reversible the consequence), not by how capable the agent is.
- canvas:        16:9
- elements:      a start node "task" (grey); first diamond gate "is this accountability, interpretation or authorship?" (vermillion); a terminal "human only — do not delegate" (blue human icon) on its yes-exit; second diamond gate "is verification cheap?" (vermillion) on its no-exit; third diamond gate "is a wrong output reversible / low-consequence?" (vermillion); three agent-role terminals in orange — "agent runs, light supervision", "agent acts behind a mandatory gate", "agent drafts only, human verifies"; one blue "human only" terminal
- flow:          top-to-bottom. task → gate 1. Gate 1 "yes" → "human only — do not delegate". Gate 1 "no" → gate 2 "is verification cheap?". Gate 2 "yes" → gate 3a "reversible?" ; gate 2 "no" → gate 3b "reversible?". From gate 3a: "yes" → "agent runs, light supervision"; "no" → "agent acts behind a mandatory gate". From gate 3b: "yes" → "agent drafts only, human verifies"; "no" → "human only — do not delegate"
- labels:        "task", "accountability, interpretation or authorship?", "human only — do not delegate", "verification cheap?", "reversible / low-consequence?", "agent runs, light supervision", "agent acts behind a mandatory gate", "agent drafts only, human verifies", "yes", "no"
- annotations:   a light bracket grouping the three agent terminals labelled "augmentation"; the single human terminal reached by two paths labelled "not an instrument's to do"
- caption:       Figure 4.1 — A placement procedure for delegation. The first gate removes what does not transfer to an instrument at all: accountability, interpretation, authorship; the remaining gates trade verification cost against reversibility to sort the rest into supervised, gated or draft-only agent roles.
- alt-text:      A top-to-bottom decision flowchart. A task first meets the question of whether it is a matter of accountability, interpretation or authorship; if yes, it is routed to a human-only terminal marked do not delegate. If no, a second question asks whether verification is cheap, and a third whether a wrong output is reversible. The four combinations route to agent runs with light supervision, agent acts behind a mandatory gate, agent drafts only with human verification, or, for expensive-to-verify and irreversible tasks, back to the human-only terminal.
- generator prompt: A flat vector decision flowchart on an off-white background, flowing top
                 to bottom. At the top a small grey rounded rectangle labelled "task"
                 connects down to a vermillion diamond labelled "accountability,
                 interpretation or authorship?". Its "yes" exit leads right to a blue
                 head-and-shoulders terminal labelled "human only — do not delegate". Its
                 "no" exit leads down to a second vermillion diamond labelled "verification
                 cheap?". That diamond's "yes" and "no" exits each lead to a vermillion
                 diamond labelled "reversible / low-consequence?". From the left diamond:
                 "yes" leads to an orange rounded rectangle "agent runs, light supervision";
                 "no" leads to an orange rounded rectangle "agent acts behind a mandatory
                 gate". From the right diamond: "yes" leads to an orange rounded rectangle
                 "agent drafts only, human verifies"; "no" leads to the same blue "human
                 only — do not delegate" terminal. A thin bracket groups the three orange
                 terminals with the label "augmentation". Single-weight connectors, one
                 arrowhead style, generous spacing, minimal text.
```

## 4.4 What does not transfer to an instrument

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
- Feng, K. J. K., McDonald, D. W. and Zhang, A. X. (2025). Levels of autonomy for AI agents. *arXiv preprint.* https://arxiv.org/abs/2506.12469
- Kapoor, S., Stroebl, B., Siegel, Z. S., Nadgir, N. and Narayanan, A. (2024). AI agents that matter. *arXiv preprint.* https://arxiv.org/abs/2407.01502
