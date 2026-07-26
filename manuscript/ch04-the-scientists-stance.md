# Chapter 4 — The scientist's stance

> **Status:** draft r5 · voice v3.4 (`STYLE.md`) · sentence-per-line per `STYLE.md` §10 · figures as briefs per `FIGURES.md`.
> **Conventions:** vendor-neutral (outline §9) · **[AUTHOR: …]** marks lived material only the author can supply · **[verify]** marks real but unconfirmed details · citations drawn only from verified reports in `/research`. Nothing has been invented.

---

## 4.1 Where an agent fits the scientific method

Agents serve the scientist's judgement.
They do not replace it.
The practical question is which parts of the research cycle may be handed to an agent, and which may not.

The scientific method runs as a cycle: a question becomes a hypothesis, the hypothesis a design, the design data and analysis, and the analysis interpretation, communication and the next question.
Its phases do not ask the same thing of the scientist.
Some are transformations of data with a right answer that can be checked; others are judgements the scientist alone is accountable for.
Reformatting a decade of gauge records into a common schema has a correct outcome, and a second procedure can confirm it.
Deciding whether a departure from the record is a real hydrological signal or a sensor fault is a judgement, and the scientist is accountable for it.

An agent belongs on the tasks with a checkable answer, and needs a far more careful decision wherever judgement is involved.
Neither kind of task has a phase to itself.
Data preparation contains judgements, and interpretation contains steps that can be checked.
Delegation is therefore settled one task at a time.

## 4.2 Augmentation and automation are different commitments

Augmenting a scientist and automating a task are different commitments, and what differs is who exercises judgement.
Under augmentation the scientist stays in every instance of the work.
The agent only increases what can be finished in an afternoon: a wider literature, a larger reprocessing job, a figure produced in fewer steps.

Automation removes the scientist from each instance of the work.
The agent runs, and nobody judges its outputs one by one before they are used.
Augmentation does the reverse, keeping the scientist as the person who inspects, interprets and answers for every output.
Most real workflows are somewhere between the two.
One recent framework names the steps by the role the human keeps: operator, collaborator, consultant, approver, observer (Feng et al., 2025).
Its useful point is that the role is chosen by whoever builds the workflow, and not fixed by the agent's capability.
The framework is a recent proposal and not yet a consensus, so it is borrowed here as vocabulary rather than as a standard (moderate confidence).

The question a group should ask of a proposed deployment is not "can the agent do this?" but "what happens to an error the agent makes here, and who answers for it?".
The first question is about capability, and capability does not decide the matter: a plausible failure (Chapter 1) persists however capable the agent becomes.
The second is about whether the failure would be caught and what it would cost if it were not.
A group can answer it with the specification (Chapter 3) and verification (Chapter 11) practices it already has.
Commercial framing and early scientific enthusiasm both get this backwards, treating automation as the goal and augmentation as a stage on the way to it.
Automation is the special case, admissible only where a task has been shown to tolerate the removal of human judgement.
Augmentation is the default for most scientific work.

Added autonomy is a cost to be justified, not a good in itself, and there is direct evidence for treating it that way.
Researchers benchmarked elaborate agent architectures against a plain model wrapped in a basic retry loop.
On a standard coding task the simple baseline matched them, at a fraction of the cost (Kapoor et al., 2024).
Nor is the choice between the two modes a property of the agent.
The same agent may be augmentation in one workflow and automation in another, depending only on whether a human forms a judgement between its output and its use.

## 4.3 A decision procedure: should an agent do this?

Two questions decide where an agent may be placed, and neither is about the agent.
The first is what it costs to verify an output.
A test suite, a schema or a checksum settles it cheaply; interpretation, missing context or an unresolved research question does not.
The second is what a wrong output costs if nobody catches it.
A mislabelled intermediate file, spotted before anything uses it, is nearly free to undo.
An error carried into an issued flood warning, a published result or an overwritten dataset is not undoable at any price.
The four combinations give the procedure.
Cheap to verify, reversible if wrong: the agent may run with little or no supervision.
Cheap to verify, severe if wrong: the agent may act, but only behind a gate that makes verification mandatory.
Expensive to verify, reversible if wrong: the agent drafts, a human checks, and the workflow budgets for the checking.
Expensive to verify and severe if wrong: the task is not an agent's at all, whatever the agent is capable of.
What disqualifies the task belongs to the task and not to the tool.

The simplest arrangement that meets the task is the right one, and agentic components are added only where the task visibly demands them (Anthropic, 2024).
Practitioners put it more bluntly: if a fixed sequence of steps with at most a judgement call or two would do the job, build a workflow and not an agent (AI Founders, 2026).
The weakness of any such rule is that both properties have to be estimated before the work starts.
Estimating them wrongly is a failure in its own right, whether by believing verification cheaper than it proves or an output more reversible than it is.

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

Three things in scientific work do not transfer to an instrument, however capable it becomes.
Accountability is the answerability of a named person for a decision and its consequences.
Interpretation is the act of deciding what a result means in the light of context the scientist holds and the system does not.
Authorship is the standing to claim and defend a contribution as one's own.
The first gate of the procedure removes all three before verification cost is considered, and not because they are difficult.
No better model closes these limits, because none of them is a deficit in capability.
Each is a property of the relationship between a scientist and the community that holds them to account.
Treating them as automatable is the most consequential category error the field invites, and an agent makes it easy to commit.
Its fluent output in an interpretive register looks exactly like the interpretation the scientist would have written.
The guard is that ease of phrasing says nothing about admissibility.
"Tell me whether this trend is significant" is as easily typed as "reformat these files", and only one of the two passes the first gate.

Even an admissible task is not always worth delegating.
Where verifying the agent's output costs more than doing the task directly, the procedure rules against delegation, however well the agent performs.
And where a task's placement is genuinely unclear, the safe default is augmentation under supervision rather than automation.
That preserves the human judgement a misjudged delegation would have removed.
Preserving it costs time; removing it wrongly costs the correctness of the science.

---

### References (verify details before release)

- AI Founders (2026). "Don't build an AI agent until you can answer these 8 questions." Video, @aifoundershq, 17 May 2026. https://www.youtube.com/watch?v=jMHawg6qpps
- Anthropic (2024). Building effective agents. *Anthropic engineering blog.* https://www.anthropic.com/engineering/building-effective-agents
- Feng, K. J. K., McDonald, D. W. and Zhang, A. X. (2025). Levels of autonomy for AI agents. *arXiv preprint.* https://arxiv.org/abs/2506.12469
- Kapoor, S., Stroebl, B., Siegel, Z. S., Nadgir, N. and Narayanan, A. (2024). AI agents that matter. *arXiv preprint.* https://arxiv.org/abs/2407.01502
