# Chapter 4 — The scientist's stance

> **Status:** draft r4 · voice v3.4 (`STYLE.md`) · sentence-per-line per `STYLE.md` §10 · figures as briefs per `FIGURES.md`.
> **Conventions:** vendor-neutral (outline §9) · **[AUTHOR: …]** marks lived material only the author can supply · **[verify]** marks real but unconfirmed details · citations drawn only from verified reports in `/research`. Nothing has been invented.

---

## 4.1 Where an agent fits the scientific method

Agents are instruments that serve the scientist's judgement rather than substitutes for it.
What remains is the practical question: which parts of the research cycle may be handed to such an instrument, and which may not.
The scientific method is a cycle: a question is refined into a hypothesis, the hypothesis into a design, the design into data and analysis, and the analysis back into interpretation, communication and the next question.
The phases of the scientific method differ in how much judgement they require of the scientist.
Some are transformations of material with a checkable right answer; others are acts of judgement for which the scientist alone can be held to account.
Reformatting a decade of gauge records into a common schema has a correct outcome that a second procedure can confirm.
Deciding that a departure from the record is a genuine hydrological signal rather than a sensor fault is a judgement.
No second procedure can confirm it, and the scientist is answerable for it.
An agent belongs on the tasks with a checkable answer and not on the tasks that require judgement.
The two kinds of task are not separated by phase: data preparation contains judgements, and interpretation contains steps that can be checked.

The consequence for deployment is that agents are not collaborators pursuing the science alongside the scientist.
They are instruments applied to the transformational phases: acquisition, quality control, coding, orchestration and drafting.
In each of those phases the output can be checked against something other than confidence in it.
The limitation is practical rather than conceptual: because the two kinds of work are interleaved within every phase, the placement of an agent is decided task by task and not phase by phase.
The framing is sound (high confidence); applying it at that level of detail is the hard part.

## 4.2 Augmentation and automation are different commitments

The distinction that governs safe practice is between augmenting a scientist and automating a task.
The two words are not loose synonyms for more and less agency: they name different commitments about who exercises judgement.
Under augmentation the scientist remains part of every instance of the work.
The agent increases what can be completed in an afternoon: a wider literature, a larger reprocessing job, or a figure produced in fewer steps.
The scientist inspects and interprets every output that leaves the workflow, and remains answerable for it.
Automation removes the scientist from each instance: the agent runs, and its outputs are used downstream without a human judging them one by one.
That removal is precisely what makes automation valuable and precisely what makes it dangerous.
The distinction is graded rather than binary, and the research literature offers a usable set of graduations.
One recent framework describes levels of autonomy by the role the human keeps: operator, collaborator, consultant, approver, observer (Feng et al., 2025).
It insists that the level is a deliberate design decision, separable from the agent's raw capability.
This book cites that framework as a helpful vocabulary rather than a settled standard, a recent proposal and not yet a consensus (moderate confidence).
Its central claim is nonetheless correct: the builder chooses which decisions the human retains, and that choice is one to make deliberately and to defend.

The error the field most often makes, in commercial framing and early scientific enthusiasm alike, is to treat automation as the goal.
Augmentation is then cast as a temporary stage before it, when the correct relationship is the reverse.
Automation is the special case, admissible only where a task has been shown to tolerate the removal of human judgement.
Augmentation is the default for most scientific work.
Whether a task tolerates automation is not a matter of how capable the agent is, because a plausible failure (Chapter 1) persists at any level of capability.
It is a matter of whether the failure would be caught, and of what it would cost if it were not.
This has a concrete organisational consequence for how a group evaluates a proposed deployment.
The question is not "can the agent do this?" but "what happens to an error the agent makes here, and who answers for it?".
That is a question about the workflow surrounding the agent rather than about the agent itself.
It is therefore answerable with the specification (Chapter 3) and verification (Chapter 11) practices the group already has.
There is direct evidence for keeping the default simple.
Researchers benchmarked elaborate agent architectures against a plain model wrapped in a basic retry loop.
On a standard coding task, the simple baseline matched the complex systems at a fraction of the cost (Kapoor et al., 2024).
Added autonomy is therefore a cost to be justified, not a good in itself.
The qualification worth stating is that the distinction between the two modes is a design choice and not a fixed property of the agent.
The same agent may be augmentation in one workflow and automation in another.
What decides the difference is whether a human forms a judgement between the agent's output and its use (high confidence).

## 4.3 A decision procedure: should an agent do this?

A usable rule for placing an agent rests on two properties of the task: verification cost, and the reversibility of a wrong output.
Their combination is more informative than either the agent's apparent competence or the task's apparent difficulty.
Verification cost is the price of establishing that a given output is correct, and Chapter 1 developed it as a better selector than perceived difficulty.
It is cheap and mechanical where a test suite, a schema, a checksum or a round trip settles the matter.
It is expensive, subjective or slow where correctness depends on interpretation, on context the system does not hold, or on an unresolved research question.
Reversibility, the second property, is the cost of a wrong output that is not caught.
A mislabelled intermediate file caught before it feeds anything is nearly free to undo.
An error propagated into an issued flood warning, a published result or an irretrievably overwritten dataset is not undoable at any price.
Read together, the two properties yield a procedure rather than a slogan.
Where verification is cheap and consequences reversible, an agent may run with light supervision, because its errors are caught and undone at low cost.
Most of the transformational work that motivates this book falls in this case.
Where verification is cheap but consequences severe, an agent may still act, but only behind a gate that makes the verification mandatory rather than optional before the output is used.
Where verification is expensive but consequences reversible, an agent produces drafts and candidates for a human to check, never accepted outputs.
The workflow must budget for that checking.
Where verification is expensive and consequences severe, meaning irreversible and hard to confirm before it is too late, the task does not belong to an agent at all.
No amount of capability changes that assignment, because the property that disqualifies the task belongs to the task and not to the tool.

The procedure is a discipline of choosing the simplest arrangement that meets the task, and of adding agentic components only where the task visibly demands them.
That is the same governing principle the most useful practitioner guidance in the field recommends (Anthropic, 2024).
The same test appears in practitioner guidance under a blunter name, the workflow test.
If a fixed sequence of steps with at most a judgement call or two would do the job, build a workflow and not an agent (practitioner commentary; see the references).
The limitation of the procedure is that both properties are estimated in advance.
Estimating them wrongly, by believing verification cheaper than it proves or an output more reversible than it is, is itself one of the failure modes catalogued in Chapter 13.
The procedure therefore structures the judgement rather than replacing it (moderate-to-high confidence).

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

The first gate of the procedure removes an entire class of tasks before verification cost is considered.
These tasks are not removed because they are hard for an agent, but because they are categorically not an agent's to perform.
Three things in scientific work do not transfer to any instrument, however capable.
There is accountability, the answerability of a named person for a decision and its consequences.
There is interpretation, the act of deciding what a result means in the light of context the scientist holds and the system does not.
And there is authorship, the standing to claim and defend a contribution as one's own.
An agent cannot be responsible for a flood warning issued on the strength of its output.
It cannot decide that an anomaly is a discovery rather than an artefact, and it cannot be an author of the paper that follows.
None of these limits is closed by a better model.
They are not deficits in capability, but properties of the relationship between a scientist and the community that holds them to account.
Treating them as automatable is the most consequential category error the field invites, and it is invited constantly.
An agent's fluent output in an interpretive register is indistinguishable in surface form from the interpretation the scientist would write.
The discipline that guards against the error is to notice that ease of phrasing says nothing about admissibility.
"Tell me whether this trend is significant" is as easily typed as "reformat these files".
The first request fails the first gate, and the second passes it.

Two practical cautions complete the stance.
The first is that automating a genuinely admissible task can still be the wrong choice.
Where verifying the agent's output costs more than doing the task directly would, the procedure rules against delegation.
The enthusiasm of a working demonstration makes that easy to overlook [AUTHOR: a case from your own practice where checking the agent cost more than doing the work yourself would sharpen this].
The second is that the safe default, when a task's placement is genuinely unclear, is augmentation under supervision rather than automation.
That choice preserves the human judgement a misjudged delegation would have removed.
Preserving it costs time; removing it wrongly costs the correctness of the science (high confidence).

---

### References (verify details before release)

- AI Founders (2026). "Don't build an AI agent until you can answer these 8 questions." Video, @aifoundershq, 17 May 2026. https://www.youtube.com/watch?v=jMHawg6qpps (practitioner commentary; concepts cited as corroboration, not evidence)
- Anthropic (2024). Building effective agents. *Anthropic engineering blog.* https://www.anthropic.com/engineering/building-effective-agents
- Feng, K. J. K., McDonald, D. W. and Zhang, A. X. (2025). Levels of autonomy for AI agents. *arXiv preprint.* https://arxiv.org/abs/2506.12469
- Kapoor, S., Stroebl, B., Siegel, Z. S., Nadgir, N. and Narayanan, A. (2024). AI agents that matter. *arXiv preprint.* https://arxiv.org/abs/2407.01502
