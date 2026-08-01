# Figure briefs — Chapter 10 — Multi-agent workflows

Briefs for the figures of `manuscript/ch10-multi-agent-workflows.md`, held here rather than in the chapter so the prose reads clean.
Each brief follows `FIGURES.md` §6. The caption and alt-text in the chapter are generated with the brief and must be changed here and there together.

## Figure 10.1 — Independence, not multiplicity, is the source of value

```
FIGURE BRIEF
- id:            Figure 10.1
- title:         When a second agent adds information, and when it adds only cost
- type:          decision flowchart
- claim:         A second agent is worth its latency and token cost only when its errors are independent of the agent it checks; correlated agents add cost without information.
- standfirst:    Agreement between near-identical agents is not corroboration.
- canvas:        16:9
- elements:      a start node "proposed second agent" (grey); a first vermillion diamond
                 "names an error class the roster misses?"; a second vermillion diamond
                 "judgement independent of the checked agent?"; an orange terminal "keep —
                 independent reviewer" carrying a purple reviewer icon; a grey terminal
                 "drop — add a deterministic gate instead"
- flow:          top-to-bottom. proposed second agent → gate 1. Gate 1 "no" → drop. Gate 1
                 "yes" → gate 2. Gate 2 "no" → drop. Gate 2 "yes" → keep
- labels:        "proposed second agent", "names an error class the roster misses?",
                 "judgement independent of the checked agent?", "keep — independent
                 reviewer", "drop — add a deterministic gate instead", "yes", "no"
- annotations:   beside gate 2, a callout listing "different model · narrowed context ·
                 adversarial brief · external source of truth"; on the "no" exits, "without
                 one of those, a second agent supplies correlated opinion — cost without
                 information"; on the "drop" terminal, "if a rule can check it, a gate is
                 cheaper and more reliable than an agent"; a footnote, "four agents on one
                 model agreeing have checked the work once and echoed it three times"
- caption:       Figure 10.1 — Two questions before you add an agent. It has to catch a class of error nothing else in the roster would, and its judgement has to be independent of the thing it is checking. Independence takes one of four deliberate design moves. Fail either and you have bought latency and tokens for correlated opinion: four agents on one model agreeing have checked the work once and echoed it three times.
- alt-text:      A top-to-bottom decision flowchart. A proposed second agent meets a first gate asking whether it names an error class the existing roster and gates would miss; a no exits to a grey terminal reading drop, add a deterministic gate instead. A yes leads to a second gate asking whether its judgement is genuinely independent of the agent it checks, with a callout listing the four things that create independence: a different model, a narrowed context, an adversarial brief, and an external source of truth. A no again exits to drop, annotated that without one of those four the second agent supplies correlated opinion, which is cost without information. A yes reaches an orange terminal, keep, marked with a purple reviewer icon. A footnote reads that four agents on one model agreeing have checked the work once and echoed it three times.
- infographic description: A flat vector decision flowchart on an off-white background,
                 16:9, top to bottom. Title top-left: "When a second agent adds information,
                 and when it adds only cost". Standfirst beneath: "Agreement between
                 near-identical agents is not corroboration." A grey rounded rectangle
                 "proposed second agent" at the top connects down to a vermillion diamond
                 "names an error class the roster misses?". Its "no" exit leads right to a
                 grey terminal "drop — add a deterministic gate instead", annotated "if a
                 rule can check it, a gate is cheaper and more reliable than an agent". Its
                 "yes" exit leads down to a second vermillion diamond "judgement independent
                 of the checked agent?", with a callout in a pale yellow fill beside it
                 listing four items on separate lines: "different model", "narrowed
                 context", "adversarial brief", "external source of truth". This diamond's
                 "no" exit joins the same grey terminal, with the shared annotation "without
                 one of those, a second agent supplies correlated opinion — cost without
                 information". Its "yes" exit leads down to an orange terminal "keep —
                 independent reviewer" carrying a small purple head-and-shoulders-with-tick
                 icon. A footnote along the bottom reads "four agents on one model agreeing
                 have checked the work once and echoed it three times". Generous spacing,
                 sentence case.
```

## Figure 10.2 — A minimal scientific roster

```
FIGURE BRIEF
- id:            Figure 10.2
- title:         A minimal roster — producer, gates, independent reviewer, human decision
- type:          architecture
- claim:         A scientific roster is a small set of distinct roles separated by deterministic gates, with independence engineered at the producer–reviewer boundary and a human holding the accountable decision.
- standfirst:    Small, and every element traces back to a clause somebody wrote.
- canvas:        16:9
- elements:      a thin grey "orchestrator" bar spanning the top; below it, left to right, a
                 "specification" tag (blue); a "producer agent" rounded rectangle (orange)
                 with a "tools" glyph (green) and a "data store" cylinder (sky blue); a
                 deterministic "gate" diamond (vermillion); an "independent reviewer"
                 rounded rectangle (reddish purple); a second gate; a blue "human decision"
                 head-and-shoulders icon
- flow:          left-to-right — specification → producer → gate → independent reviewer →
                 gate → human decision; a single "fail" return arrow runs from the reviewer
                 back to the producer
- labels:        "orchestrator — sequences, enforces stop conditions", "specification",
                 "producer agent", "tools", "data store", "gate",
                 "tests · schema · citations · units", "independent reviewer",
                 "different model · narrowed context · adversarial brief", "human decision",
                 "fail — bounded iterations, then escalate"
- annotations:   on the orchestrator bar, "deliberately thin — an orchestrator that reasons
                 about the science reintroduces the judgement the roster exists to avoid";
                 on the gate, "anything a rule can check is a gate, not an agent"; on the
                 reviewer, "independence engineered here, not hoped for"; on the return
                 arrow, "bounded, or it becomes a cost blow-out and nobody owns the miss";
                 on the human node, "accountability, interpretation and authorship stay
                 here"; a footer, "every role on this diagram traces back to a clause of
                 the specification"
- caption:       Figure 10.2 — A roster is small, and every element earns its place. A producer does the work, deterministic gates catch anything a rule can settle, one independent reviewer handles what a rule cannot, and a human owns the decision. Two details carry the design: the orchestrator is deliberately thin, and the return loop is bounded so it escalates rather than churning.
- alt-text:      An architecture diagram. A thin orchestrator bar spans the top, labelled sequences and enforces stop conditions, annotated deliberately thin, because an orchestrator that reasons about the science reintroduces the correlated judgement the roster exists to avoid. Below it, left to right: a specification tag; a producer agent with tools and a data store; a deterministic gate listing tests, schema, citations and units, annotated that anything a rule can check is a gate rather than an agent; an independent reviewer annotated with the three things that make it independent, a different model, a narrowed context and an adversarial brief; a second gate; and a human decision point annotated that accountability, interpretation and authorship stay here. A single fail arrow returns from the reviewer to the producer, labelled bounded iterations, then escalate.
- infographic description: A flat vector architecture diagram on an off-white background,
                 16:9. Title top-left: "A minimal roster — producer, gates, independent
                 reviewer, human decision". Standfirst beneath: "Small, and every element
                 traces back to a clause somebody wrote." A thin grey bar spans the top
                 labelled "orchestrator — sequences, enforces stop conditions", annotated
                 "deliberately thin — an orchestrator that reasons about the science
                 reintroduces the judgement the roster exists to avoid". Below it, a
                 left-to-right chain: a blue tag "specification"; an orange rounded
                 rectangle "producer agent" with a green "tools" glyph and a sky-blue "data
                 store" cylinder attached; a vermillion diamond "gate" with sub-text "tests
                 · schema · citations · units", annotated "anything a rule can check is a
                 gate, not an agent"; a reddish-purple rounded rectangle "independent
                 reviewer" with sub-text "different model · narrowed context · adversarial
                 brief", annotated "independence engineered here, not hoped for"; a second
                 vermillion diamond "gate"; and a blue head-and-shoulders icon "human
                 decision", annotated "accountability, interpretation and authorship stay
                 here". A single arrow labelled "fail — bounded iterations, then escalate"
                 runs from the reviewer back to the producer, annotated "bounded, or it
                 becomes a cost blow-out and nobody owns the miss". A footer line reads
                 "every role on this diagram traces back to a clause of the specification".
                 Generous spacing, sentence case.
```

## Figure 10.3 — Conventional review and agentic roster, side by side

```
FIGURE BRIEF
- id:            Figure 10.3
- title:         Distributed human review and its agentic roster share one grammar
- type:          before/after
- claim:         A roster reproduces the independence structure of conventional distributed review (producer, independent checker, accountable decider) but compresses serial handoffs of days into gated handoffs of minutes.
- standfirst:    Same structure science already uses; a different clock.
- canvas:        16:9
- elements:      an upper "conventional" lane and a lower "agentic roster" lane sharing a
                 left-to-right grammar. Upper: "author" (blue human) → "internal
                 read-through" (blue human) → "independent referees ×2" (blue humans) →
                 "editor decides" (blue human). Lower: "producer agent" (orange) → "gate"
                 (vermillion) → "independent reviewer" (purple) → "gate" (vermillion) →
                 "human decision" (blue)
- flow:          two stacked left-to-right lanes read in parallel; dotted vertical
                 alignment lines connect author↔producer, referees↔independent reviewer,
                 editor↔human decision
- labels:        "conventional", "author", "internal read-through",
                 "independent referees ×2", "editor decides", "serial — weeks",
                 "agentic roster", "producer agent", "gate", "independent reviewer",
                 "human decision", "gated — minutes"
- annotations:   on the upper lane end, "serial — weeks"; on the lower lane end, "gated —
                 minutes; the human still owns the decision"; on the three alignment
                 lines, "producer", "independent checker", "accountable decider"; a
                 footer, "what carries over is independence and accountability — not the
                 number of parties"
- caption:       Figure 10.3 — Science already runs the structure a roster copies. Author, independent referees and a deciding editor line up with producer, independent reviewer and human decision, and the dotted lines mark the correspondence. What changes is the clock, from weeks of serial handoffs to minutes of gated ones. What must not change is on the alignment lines: independence and accountability, not headcount.
- alt-text:      Two lanes sharing one left-to-right grammar. The top lane shows conventional review: an author, an internal read-through, two independent referees and an editor who decides, marked as serial and taking weeks. The bottom lane shows the agentic roster: a producer agent, a gate, an independent reviewer, a second gate and a human decision, marked as gated and taking minutes, with the human still owning the decision. Dotted vertical lines link the matching roles, author to producer, referees to independent reviewer, editor to human decision. A note reads that what carries over is independence and accountability, not the number of parties.
- infographic description: A flat vector before-and-after diagram, 16:9, off-white
                 background. Title top-left: "Distributed human review and its agentic
                 roster share one grammar". Standfirst: "Same structure science already
                 uses; a different clock." Two stacked left-to-right lanes with aligned
                 columns. Upper lane "conventional": blue human icons "author", "internal
                 read-through", "independent referees ×2", "editor decides", joined by
                 arrows, ending in the tag "serial — weeks". Lower lane "agentic roster":
                 an orange rounded square "producer agent", a vermillion diamond "gate", a
                 purple reviewer icon "independent reviewer", a second vermillion "gate",
                 a blue human "human decision", ending in the tag "gated — minutes; the
                 human still owns the decision". Three dotted vertical lines link the
                 matching columns, labelled "producer", "independent checker",
                 "accountable decider". Footer: "what carries over is independence and
                 accountability — not the number of parties". Sentence case throughout.
```

## Figure 10.4 — From specification to roster

```
FIGURE BRIEF
- id:            Figure 10.4
- title:         Deriving a roster from the specification schema
- type:          sequence
- claim:         Each field of a Chapter 3 specification maps to a specific roster element, so that every role and gate has an auditable provenance in a clause a human wrote.
- standfirst:    Every role traces to a clause somebody wrote. No clause, no role.
- canvas:        16:9
- elements:      four specification fields on the left as blue tags stacked top to bottom
                 — "objective", "inputs", "acceptance criteria", "stop conditions"; four
                 roster outcomes on the right, each reached by a numbered arrow —
                 "producer role(s)" (orange), "tool & data access (least privilege)"
                 (green tool + sky data-store), "gates + reviewer brief" (vermillion gate
                 + purple reviewer), "loop bound + escalation" (grey)
- flow:          top-to-bottom, four numbered mappings read in order: 1 objective →
                 producer role(s); 2 inputs → tool & data access; 3 acceptance criteria →
                 gates + reviewer brief; 4 stop conditions → loop bound + escalation
- labels:        "objective", "inputs", "acceptance criteria", "stop conditions",
                 "producer role(s)", "tool & data access (least privilege)",
                 "gates + reviewer brief", "loop bound + escalation", "1", "2", "3", "4"
- annotations:   on mapping 1, "one bounded objective, one producer"; on mapping 2,
                 "access assigned per role, never to the roster as a whole"; on mapping 3,
                 "can a rule check it? gate if yes; reviewer brief if not"; on mapping 4,
                 "bounds cost, and stops responsibility diffusing"; a footer, "a role no
                 clause of the specification demands is a role that should not exist"
- caption:       Figure 10.4 — The roster is derived, not designed. Each field of the Chapter 3 specification produces its own roster element, so every role and gate traces back to a clause a person wrote and can audit. The third mapping does the sorting: anything a rule can check becomes a gate, and only what needs judgement earns a reviewer. A role no clause demands should not exist.
- alt-text:      Four blue specification fields stacked on the left, objective, inputs, acceptance criteria and stop conditions, each joined by a numbered arrow to the roster element it produces on the right: producer roles; tool and data access under least privilege; gates for the rule-checkable criteria plus a reviewer brief for the judgement ones; and the loop bound with its escalation path. The third mapping carries the sorting question, can a rule check it, gate if yes, reviewer if not. The fourth is annotated as what bounds cost and stops responsibility diffusing. A footer reads that a role no clause demands is a role that should not exist.
- infographic description: A flat vector mapping diagram, 16:9, off-white background.
                 Title top-left: "Deriving a roster from the specification schema".
                 Standfirst: "Every role traces to a clause somebody wrote. No clause, no
                 role." Left column: four blue tags stacked with generous spacing —
                 "objective", "inputs", "acceptance criteria", "stop conditions". Right
                 column: four outcome blocks aligned with them — an orange rounded square
                 "producer role(s)"; a green wrench beside a sky-blue cylinder "tool &
                 data access (least privilege)"; a vermillion diamond beside a purple
                 reviewer icon "gates + reviewer brief"; a grey rounded rectangle "loop
                 bound + escalation". Four numbered straight arrows join the pairs, each
                 with its annotation beneath: "1 · one bounded objective, one producer";
                 "2 · access assigned per role, never to the roster as a whole"; "3 · can
                 a rule check it? gate if yes; reviewer brief if not"; "4 · bounds cost,
                 and stops responsibility diffusing". Footer: "a role no clause of the
                 specification demands is a role that should not exist". Sentence case.
```
