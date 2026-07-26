# Chapter 4 — The scientist's stance

> **Status:** draft r3 · voice v3.3 (`STYLE.md`) · sentence-per-line per `STYLE.md` §10 · figures as briefs per `FIGURES.md`.
> **Conventions:** vendor-neutral (outline §9) · **[AUTHOR: …]** marks lived material only the author can supply · **[verify]** marks real but unconfirmed details · citations drawn only from verified reports in `/research`. Nothing has been invented.

---

## 4.1 Where an agent fits the scientific method

Agents are instruments serving the scientist's judgement rather than substitutes for it. As such, its practical content is a map of where, in the actual work of science, such an instrument may legitimately be placed. [human: what do you mean with "its practical content is a map of where ... placed."].
The scientific method is a cycle: a question is refined into a hypothesis, the hypothesis into a design, the design into data and analysis, and the analysis back into interpretation, communication and the next question.
The phases of that cycle are not equal in what they demand of the person carrying them out. [human: I understand this sentence, but can you write it in a more plain language?].
Some are transformations of material with a checkable right answer; others are acts of judgement for which the scientist alone can be held to account.
Reformatting a decade of gauge records into a common schema has a correct outcome that a second procedure can confirm.
Deciding that a departure from the record is a genuine hydrological signal rather than a sensor fault is an interpretation that carries the scientist's name and standing. [human: I would not write " that carries .... standing. Can you change it?].
An instrument belongs in the first kind of phase and not the second, and the boundary between them runs through the middle of the research cycle rather than neatly around its edge. [human: can you explain to me thissentence, and suggest different way to express it because I woukd not write it like this].

The consequence for how agents are deployed is that they are best understood not as collaborators pursuing the science alongside the scientist, but as extensions of the scientist's reach into the transformational phases (acquisition, quality control, coding, orchestration, drafting), where their output can be checked against something other than confidence in it. 
The limitation of this framing is that the two kinds of phase are finely interleaved, so an agent's placement is decided task by task and not phase by phase (high confidence in the framing; the granularity is what makes it hard to apply). [ human: can we write this in a more plain language?].

## 4.2 Augmentation and automation are different commitments

The distinction that governs safe practice is between augmenting a scientist and automating a task, and the two words are not loose synonyms for more and less agency: they name genuinely different commitments about where judgement sits.
Augmentation places the agent inside the scientist's own loop of work: it extends what can be reached in an afternoon (a wider literature, a larger reprocessing job, a faster path from artefact to figure), whilst the scientist inspects, interprets and remains answerable for every output that leaves the workflow.
Automation removes the scientist from the per-instance loop entirely: the agent runs, and its outputs are consumed downstream without a human forming a judgement about each one, which is precisely what makes automation valuable and precisely what makes it dangerous.
The distinction is better seen as a dial rather than a switch, and the research literature offers a usable set of graduations: one recent framework describes levels of autonomy by the role the human keeps (operator, collaborator, consultant, approver, observer) and insists that the level is a deliberate design decision, separable from the agent's raw capability (Feng et al., 2025).
This book cites that framework as a helpful vocabulary rather than a settled standard, a recent proposal not yet a consensus (moderate confidence), but its central move is exactly right: the builder chooses how much of the loop the human occupies, and that choice is one to make deliberately and to defend.

The error the field most often makes, in commercial framing and early scientific enthusiasm alike, is to treat automation as the destination and augmentation as a transitional stage on the way to it, when the correct relationship is the reverse.
Automation is the special case, admissible only where a task has been shown to tolerate the removal of human judgement; augmentation is the default that most scientific work should stay in.
Whether a task tolerates automation is not a matter of how capable the agent is, because a plausible failure (Chapter 1) survives any amount of capability; it is a matter of whether the failure would be caught and what it would cost if it were not.
This has a concrete organisational consequence: the question a group should ask of any proposed agent deployment is not "can the agent do this?" but "what happens to an error the agent makes here, and who answers for it?", a question about the workflow surrounding the agent rather than about the agent, and therefore one answerable with the specification (Chapter 3) and verification (Chapter 11) machinery the group already possesses.
There is even direct evidence for keeping the default simple: when researchers benchmarked elaborate agent architectures against a plain model wrapped in a basic retry loop, the simple baseline matched the complex systems on a standard coding task at a fraction of the cost (Kapoor et al., 2024), which is a useful reminder that added autonomy is a cost to be justified, not a good in itself.
The qualification worth stating is that the line between the two modes is a design choice and not a fixed property, so the same underlying agent may be augmentation in one workflow and automation in another, depending entirely on whether a human judgement stands between its output and its use (high confidence).

## 4.3 A decision procedure: should an agent do this?

A usable rule for placing an agent rests on two properties of the task, verification cost and the reversibility of a wrong output, and their combination is more informative than either the agent's apparent competence or the task's apparent difficulty.
Verification cost, which Chapter 1 developed as the better selector than perceived difficulty, is the price of establishing that a given output is correct: cheap and mechanical where a test suite, a schema, a checksum or a round trip settles the matter; expensive, subjective or slow where correctness turns on interpretation, on context the system does not hold, or on a judgement at the research frontier.
Reversibility, the second axis, is the cost of a wrong output that escapes: a mislabelled intermediate file caught before it feeds anything is nearly free to undo, whereas an error propagated into an issued flood warning, a published result or an irretrievably overwritten dataset is not undoable at any price.
Reading the two axes together yields a procedure rather than a slogan.
Where verification is cheap and consequences reversible, an agent may run with light supervision, because its errors are caught at low cost and undone at low cost, and this quadrant holds the bulk of the transformational work that motivates the book.
Where verification is cheap but consequences severe, an agent may still act, but only behind a gate that makes the cheap verification mandatory rather than optional before the output is used.
Where verification is expensive but consequences reversible, an agent is a source of drafts and candidates for a human to check, never a source of accepted outputs, and the workflow must budget for the checking.
Where verification is expensive and consequences severe (irreversible, and hard to confirm before it is too late), the task does not belong to an agent at all, and no amount of capability changes that assignment, because the property that disqualifies it is a property of the task and not of the tool.

This procedure is really a discipline of reaching for the simplest arrangement that meets the task and adding agentic machinery only where the task visibly demands it, the same governing principle the most useful practitioner guidance in the field recommends (Anthropic, 2024).
The same test circulates in practitioner guidance under a blunter name, the workflow test: if a fixed sequence of steps with at most a judgement call or two would do the job, build a workflow, not an agent (practitioner commentary; see the references).
The limitation of the procedure is that both axes are estimates made in advance, and estimating them wrongly (believing verification cheaper than it proves, or an output more reversible than it is) is itself one of the failure modes catalogued in Chapter 13, so the procedure is a discipline for thinking, not a lookup table that removes the need to think (moderate-to-high confidence).

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

The first gate of the procedure removes an entire class of tasks before verification cost is even considered, and it does so because these tasks are not hard for an agent but categorically not an agent's to perform.
Three things in scientific work do not transfer to any instrument, however capable.
There is accountability, the answerability of a named person for a decision and its consequences; interpretation, the act of deciding what a result means in the light of context the scientist holds and the system does not; and authorship, the standing to claim and defend a contribution as one's own.
An agent cannot be responsible for a flood warning issued on the strength of its output, cannot decide that an anomaly is a discovery rather than an artefact, and cannot be an author of the paper that follows.
None of these limits is a gap that a better model closes, because they are not deficits in capability but properties of the relationship between a scientist and the community that holds them to account.
Treating them as automatable is the most consequential category error the field invites, and it is invited constantly, because an agent's fluent output in an interpretive register is indistinguishable in surface form from the interpretation the scientist would write.
The discipline that guards against the error is to notice that a task's being easy to phrase as a request to an agent says nothing about whether it is admissible to delegate: "tell me whether this trend is significant" is as easily typed as "reformat these files", and the two sit on opposite sides of the first gate.

Two practical cautions complete the stance.
The first is that automating a genuinely admissible task can still be the wrong choice where verifying the agent's output costs more than doing the task directly would, a case the procedure captures but that is easy to overlook in the enthusiasm of a working demonstration [AUTHOR: a case from your own practice where checking the agent cost more than doing the work yourself would sharpen this].
The second is that the safe default, when a task's placement is genuinely unclear, is augmentation under supervision rather than automation, because that choice preserves the human judgement a misjudged delegation would have removed, and preserving it costs only time, whereas removing it wrongly costs the very thing the science was for (high confidence).

---

### References (verify details before release)

- AI Founders (2026). "Don't build an AI agent until you can answer these 8 questions." Video, @aifoundershq, 17 May 2026. https://www.youtube.com/watch?v=jMHawg6qpps (practitioner commentary; concepts cited as corroboration, not evidence)
- Anthropic (2024). Building effective agents. *Anthropic engineering blog.* https://www.anthropic.com/engineering/building-effective-agents
- Feng, K. J. K., McDonald, D. W. and Zhang, A. X. (2025). Levels of autonomy for AI agents. *arXiv preprint.* https://arxiv.org/abs/2506.12469
- Kapoor, S., Stroebl, B., Siegel, Z. S., Nadgir, N. and Narayanan, A. (2024). AI agents that matter. *arXiv preprint.* https://arxiv.org/abs/2407.01502
