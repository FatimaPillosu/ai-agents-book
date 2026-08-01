# Figure briefs — Chapter 3 — Specifying work for agents

Briefs for the figures of `manuscript/ch03-specifying-work-for-agents.md`, held here rather than in the chapter so the prose reads clean.
Each brief follows `FIGURES.md` §6. The caption and alt-text in the chapter are generated with the brief and must be changed here and there together.

## Figure 3.1 — Specification anatomy

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

## Figure 3.2 — Weak specification versus strong specification

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
