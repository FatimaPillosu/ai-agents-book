# Figure briefs — Chapter 14 — Verification under constraint

Briefs for the figures of `manuscript/ch14-verification-under-constraint.md`, held here rather than in the chapter so the prose reads clean.
Each brief follows `FIGURES.md` §6. The caption and alt-text in the chapter are generated with the brief and must be changed here and there together.

## Figure 14.1 — The three-tier toolkit under constraint

```
FIGURE BRIEF
- id:            Figure 14.1
- title:         Three tiers inside one trust boundary
- type:          architecture
- claim:         The constraints (no data egress, minimal compute, no recurring budget) force a design in which an exact deterministic core always runs, an optional local tutoring tier only explains, and only aggregate scores ever cross the boundary.
- standfirst:    Exact where it must be defensible; advisory where a mistake is recoverable; human where judgement is irreducible.
- canvas:        16:9
- elements:      a large grey-bordered rounded rectangle "partner environment (trust
                 boundary)"; inside, a sky-blue cylinder "observations (never leave)"; a
                 green-bordered box "deterministic verification core" with a "scores"
                 artefact; an orange dashed-border box "local tutoring tier — open-weight
                 model" tagged "optional" and "no decision"; a blue "human review" icon;
                 one arrow crossing the boundary to "team (escalation)" carrying
                 "aggregate scores + questions only"
- flow:          left-to-right inside the boundary: observations → core → scores → human
                 review; the tutoring tier links to the scores with a dashed two-way
                 "explains / guides" arrow; a single arrow exits the boundary to the team
- labels:        "partner environment (trust boundary)", "observations (never leave)",
                 "deterministic verification core", "scores",
                 "local tutoring tier — open-weight model", "optional",
                 "explains / guides", "no decision", "human review",
                 "aggregate scores + questions only", "team (escalation)"
- annotations:   on the boundary, "no observational data egress"; on the core, "same
                 inputs, same numbers, every time — reportable as an official figure"; on
                 the tutoring tier, "open-weight, on the partner's own hardware; degrades
                 to nothing if the compute is unavailable"; on the crossing arrow, "the
                 one thing that crosses — and never the records"; a footer, "exact where
                 evidence must be defensible · advisory where a mistake is recoverable ·
                 human where judgement is irreducible"
- caption:       Figure 14.1 — The whole toolkit lives inside the partner's boundary. The deterministic core always runs and produces the same defensible numbers from the same inputs; the tutoring tier is optional, local, and allowed only to explain; and the single arrow that crosses the boundary carries aggregate scores and a question, never the observations. Three constraints forced this shape, and it is the shape governance would have chosen anyway.
- alt-text:      A large trust boundary labelled partner environment encloses most of the canvas, annotated no observational data egress. Inside it, observations that never leave feed a deterministic verification core, annotated same inputs, same numbers, every time, which produces scores for a human review step. A local tutoring tier drawn with a dashed border connects to the scores by a two-way explains-and-guides link, annotated open-weight, runs on the partner's own hardware, and carries a no-decision tag and the note that it degrades to nothing if the compute is unavailable. The only arrow crossing the boundary carries aggregate scores and questions to the team for escalation, annotated the one thing that crosses, and never the records. A footer reads exact where evidence must be defensible, advisory where a mistake is recoverable, human where judgement is irreducible.
- infographic description: A flat vector architecture diagram, 16:9, off-white
                 background. Title top-left: "Three tiers inside one trust boundary".
                 Standfirst: "Exact where it must be defensible; advisory where a mistake
                 is recoverable; human where judgement is irreducible." A large
                 grey-bordered rounded rectangle "partner environment (trust boundary)"
                 fills most of the canvas, its border annotated "no observational data
                 egress". Inside, left to right: a sky-blue cylinder "observations (never
                 leave)"; a green-bordered box "deterministic verification core"
                 annotated "same inputs, same numbers, every time — reportable as an
                 official figure", producing a small card "scores"; a blue human icon
                 "human review". Above the scores, an orange dashed-border box "local
                 tutoring tier — open-weight model" tagged "optional" and "no decision",
                 joined to the scores by a dashed two-way arrow "explains / guides", and
                 annotated "open-weight, on the partner's own hardware; degrades to
                 nothing if the compute is unavailable". One arrow exits the boundary on
                 the right, labelled "aggregate scores + questions only" and annotated
                 "the one thing that crosses — and never the records", reaching a box
                 "team (escalation)". Footer: "exact where evidence must be defensible ·
                 advisory where a mistake is recoverable · human where judgement is
                 irreducible". Sentence case throughout.
```

## Figure 14.2 — A verification-plus-tutoring interaction

```
FIGURE BRIEF
- id:            Figure 14.2
- title:         Who computes, who explains, who decides
- type:          sequence
- claim:         In a single interaction the deterministic core computes the scores, the tutoring tier only explains them, and the human holds decision authority throughout; the model never produces a reported number.
- standfirst:    Every number comes from the core. Every decision stays with the person.
- canvas:        16:9
- elements:      three lanes read top-to-bottom — a blue "user" lane; a green
                 "deterministic core" lane; an orange "tutoring tier (optional)" lane with
                 a dashed header; a vermillion outline on the closing decision step
- flow:          numbered steps downward: 1 user requests verification; 2 core computes
                 scores exactly; 3 scores returned; 4 user asks what it means; 5 tutor
                 explains, no decision; 6 user requests a diagnostic; 7 core recomputes
                 exactly; 8 user decides and records
- labels:        "user", "deterministic core", "tutoring tier (optional)",
                 "1 request verification", "2 compute scores (exact)", "3 return scores",
                 "4 what does this mean?", "5 explain (no decision)",
                 "6 request diagnostic", "7 recompute (exact)", "8 decide + record",
                 "observations stay local"
- annotations:   on step 5, "reads the scores and the fixed definitions; writes nothing to
                 the record"; on step 7, "a suggestion from the tutor is executed by the
                 core — never accepted as a number from the model"; on step 8, in
                 vermillion, "decision authority stays human"; a footer, "observations
                 stay local for the whole exchange"
- caption:       Figure 14.2 — Who computes, who explains, who decides. Every number in the exchange comes from the deterministic core, including the follow-up the tutor suggested; the tutoring tier reads scores and writes nothing to the record; and the final step, deciding and recording, is outlined in vermillion because it belongs to the person throughout.
- alt-text:      A sequence diagram with three lanes, a user, the deterministic core and a tutoring tier drawn with a dashed header to mark it optional, plus a footer note that the observations stay local throughout. Eight numbered steps: the user requests verification; the core computes the scores exactly; the scores return; the user asks what the result means; the tutoring tier explains without deciding, annotated it reads the scores and writes nothing to the record; the user asks for a further diagnostic; the core recomputes exactly, annotated that a suggestion from the tutor is always executed by the core, never accepted as a number from the model; and the user decides and records, outlined in vermillion and annotated decision authority stays human.
- infographic description: A flat vector sequence diagram, 16:9, off-white background,
                 three lanes top to bottom. Title top-left: "Who computes, who explains,
                 who decides". Standfirst: "Every number comes from the core. Every
                 decision stays with the person." Lane headers: blue human "user"; green
                 box "deterministic core"; orange dashed-border box "tutoring tier
                 (optional)". Eight numbered horizontal arrows: "1 request verification"
                 user to core; "2 compute scores (exact)" as a self-step in the core
                 lane; "3 return scores" core to user; "4 what does this mean?" user to
                 tutor; "5 explain (no decision)" tutor to user, annotated "reads the
                 scores and the fixed definitions; writes nothing to the record"; "6
                 request diagnostic" user to core; "7 recompute (exact)" in the core
                 lane, annotated "a suggestion from the tutor is executed by the core —
                 never accepted as a number from the model"; "8 decide + record" in the
                 user lane, outlined vermillion and annotated "decision authority stays
                 human". Footer: "observations stay local for the whole exchange".
                 Sentence case throughout.
```

## Figure 14.3 — The partner's workflow, before and after

```
FIGURE BRIEF
- id:            Figure 14.3
- title:         From blocked egress to local verification and learning
- type:          before/after
- claim:         The redesign replaces a slow, often-failing attempt to move observations out for verification with a toolkit that moves verification in, so scores are produced locally and only aggregates leave.
- standfirst:    The data was asked to move. The verification moved instead.
- canvas:        16:9
- elements:      two stacked panels sharing a grammar. Top "before": a sky-blue
                 observations cylinder inside a grey trust boundary, a dashed arrow
                 blocked at the boundary with a vermillion cross, an external
                 "verification, off-site" box, a tag "months of negotiation / often no
                 agreement". Bottom "after": the same cylinder and boundary, with a green
                 "deterministic core", an orange dashed "tutoring tier (optional)" and a
                 blue "human review" inside, one permitted arrow out labelled "aggregate
                 scores only" to "team"
- flow:          top panel left-to-right, blocked at the boundary; bottom panel
                 self-contained inside the boundary with one permitted aggregate arrow out
- labels:        "before", "observations", "trust boundary", "verification, off-site",
                 "blocked", "months of negotiation / often no agreement", "after",
                 "deterministic core", "tutoring tier (optional)", "human review",
                 "aggregate scores only", "team", "users learn on own data"
- annotations:   on the top panel, "the expertise sat on one side, the data on the other";
                 on the vermillion cross, "the holding institution cannot accept the
                 residual risk — and does not have to"; on the bottom panel, "verification
                 and teaching now happen where the data already is"; on the exit arrow,
                 "aggregates cross; records never do"; a footer, "the bonus nobody
                 designed for: partners learn verification on their own data"
- caption:       Figure 14.3 — Before, the data was asked to move; after, the verification moved instead. The top panel is the route that kept failing: months of negotiation towards an egress that often never came. The bottom panel is the same boundary with the tools inside it, scores produced where the observations already live, and one permitted arrow out carrying aggregates. The bonus nobody designed for: partners learn verification on their own data.
- alt-text:      A two-panel before-and-after diagram. The top panel shows observations inside a trust boundary and a dashed arrow trying to leave towards off-site verification, blocked at the boundary with a vermillion cross and tagged months of negotiation, often no agreement, annotated that the expertise sat on one side and the data on the other. The bottom panel shows the same boundary with the toolkit moved inside: a deterministic core, an optional tutoring tier and human review, annotated verification and teaching now happen where the data already is, with one permitted arrow leaving, aggregate scores only, and a note that users learn on their own data rather than on someone else's worked examples.
- infographic description: A flat vector before-and-after diagram, 16:9, off-white
                 background, two stacked panels. Title top-left: "From blocked egress to
                 local verification and learning". Standfirst: "The data was asked to
                 move. The verification moved instead." Top panel "before": a grey
                 trust-boundary rectangle holding a sky-blue cylinder "observations"; a
                 dashed grey arrow attempts to exit towards an external box "verification,
                 off-site" and is stopped at the boundary by a vermillion cross labelled
                 "blocked", with the tag "months of negotiation / often no agreement" and
                 the annotations "the expertise sat on one side, the data on the other"
                 and, at the cross, "the holding institution cannot accept the residual
                 risk — and does not have to". Bottom panel "after": the same boundary
                 and cylinder, now with a green box "deterministic core", an orange
                 dashed box "tutoring tier (optional)" and a blue human "human review"
                 inside, annotated "verification and teaching now happen where the data
                 already is"; a single arrow exits labelled "aggregate scores only" to a
                 box "team", annotated "aggregates cross; records never do"; a tag "users
                 learn on own data". Footer: "the bonus nobody designed for: partners
                 learn verification on their own data". Sentence case throughout.
```
