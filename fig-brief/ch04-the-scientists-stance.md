# Figure briefs — Chapter 4 — The scientist's stance

Briefs for the figures of `manuscript/ch04-the-scientists-stance.md`, held here rather than in the chapter so the prose reads clean.
Each brief follows `FIGURES.md` §6. The caption and alt-text in the chapter are generated with the brief and must be changed here and there together.

## Figure 4.1 — Should an agent do this?

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
