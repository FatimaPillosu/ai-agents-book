# Figure briefs — Chapter 15 — Governing a modelling workflow end to end

Briefs for the figures of `manuscript/ch15-governing-a-modelling-workflow-end-to-end.md`, held here rather than in the chapter so the prose reads clean.
Each brief follows `FIGURES.md` §6. The caption and alt-text in the chapter are generated with the brief and must be changed here and there together.

## Figure 15.1 — The governed modelling lifecycle, end to end

```
FIGURE BRIEF
- id:            Figure 15.1
- title:         One workflow, five governed stages
- type:          architecture
- claim:         A governed modelling workflow composes five stages (specification, roster, gates and registries, independent review, publication) with a named human decision at every gate.
- standfirst:    Human authority sits at every gate, not only at the end.
- canvas:        16:9
- elements:      a left-to-right spine of five stage blocks — "specification" (blue tag);
                 "agent roster" (orange agents); "gates & registries" (vermillion "gate"
                 diamond beside two sky-blue cylinders "assumption registry" and
                 "uncertainty registry"); "independent review" (purple reviewer icon);
                 "publication run" ("manuscript · figures · disclosure"); a single blue
                 "author decision" icon above the spine connected to every gate; an
                 "audit trail" band beneath all five stages
- flow:          left-to-right along the spine; each gate has a "pass" arrow forward and a
                 "fail — return" arrow back to the previous stage; blue lines connect the
                 author icon down to each gate
- labels:        "specification", "agent roster", "gates & registries", "gate",
                 "assumption registry", "uncertainty registry", "independent review",
                 "publication run", "manuscript · figures · disclosure",
                 "author decision", "pass", "fail — return", "audit trail"
- annotations:   on the specification, "seven fields, written before any agent runs"; on
                 the roster, "derived from the specification, not chosen"; on the
                 registries, "the workflow's memory of what it assumed and what it does
                 not know"; on the review, "no stake in the work it checks"; on the audit
                 trail, "accumulates from stage one — the disclosure is assembled, not
                 reconstructed"; a bracket over the spine, "human authority at every
                 gate, not only at the end"
- caption:       Figure 15.1 — The whole book in one workflow. Specification, roster, gates and registries, independent review, publication: each stage's audited output is the next stage's admissible input. The author connects to every gate rather than appearing once at the end. The audit trail underneath is why the disclosure statement at publication is assembled from a record instead of reconstructed under deadline.
- alt-text:      A left-to-right spine of five stages: a specification written to the seven-field schema; an agent roster derived from it; gates and registries, with an assumption registry and an uncertainty registry beside the gate; independent review; and the publication run producing the manuscript, figures and disclosure. Each gate has a pass arrow forward and a fail arrow returning to the previous stage. A single author-decision icon above the spine connects down to every gate, under a bracket reading human authority at every gate, not only at the end. An audit trail runs beneath all five stages, annotated as accumulating from the first stage, so the disclosure at the end is assembled rather than reconstructed.
- infographic description: A flat vector architecture diagram, 16:9, off-white
                 background. Title top-left: "One workflow, five governed stages".
                 Standfirst: "Human authority sits at every gate, not only at the end."
                 A left-to-right spine of five stage blocks: a blue tag "specification"
                 annotated "seven fields, written before any agent runs"; an orange block
                 "agent roster" annotated "derived from the specification, not chosen"; a
                 vermillion diamond "gate" beside two sky-blue cylinders "assumption
                 registry" and "uncertainty registry", the pair annotated "the workflow's
                 memory of what it assumed and what it does not know"; a purple reviewer
                 icon "independent review" annotated "no stake in the work it checks";
                 and a block "publication run" with sub-text "manuscript · figures ·
                 disclosure". Gates carry "pass" arrows forward and "fail — return"
                 arrows back. Above the spine, one blue human icon "author decision" with
                 thin lines down to each gate, under a bracket "human authority at every
                 gate, not only at the end". Beneath the spine, a full-width band "audit
                 trail" annotated "accumulates from stage one — the disclosure is
                 assembled, not reconstructed". Sentence case throughout.
```

## Figure 15.2 — A single gated stage, in sequence

```
FIGURE BRIEF
- id:            Figure 15.2
- title:         One gated stage, from specification unit to author decision
- type:          sequence
- claim:         Within a stage, an agent executes a specification unit through tools, writes its output and provenance, and a gate applies before a named human authorises the result.
- standfirst:    The author decides at the gate, not after the workflow has finished.
- canvas:        16:9
- elements:      five lanes, left to right: "specification unit" (blue tag), "agent"
                 (orange), "tools & data" (green tool with sky-blue cylinder), "gate +
                 reviewer" (vermillion diamond with purple reviewer icon), "author"
                 (blue); six numbered steps crossing between lanes
- flow:          top-to-bottom, six numbered steps: (1) unit → agent, objective, inputs,
                 criteria, stop; (2) agent → tools, call tools, transform; (3) agent
                 writes output + provenance, logs assumptions; (4) submit for check;
                 (5) fail returns within budget, pass advances; (6) author accepts,
                 overrides or returns
- labels:        "specification unit", "agent", "tools & data", "gate + reviewer",
                 "author", "1 objective, inputs, criteria, stop",
                 "2 call tools, transform", "3 write output + provenance",
                 "4 submit for check", "5 fail — return (within budget)", "5 pass",
                 "6 accept / override / return"
- annotations:   on step 2, "calculations go to tools, not prose"; on step 3, "any new
                 assumption goes to the registry, not left implicit"; on step 5's fail
                 arrow, "loop bounded by the stop conditions"; on step 6, in vermillion,
                 "the author decides at the gate, not after"; a footer, "one decision per
                 gate is the price of a workflow whose every step is attributable"
- caption:       Figure 15.2 — One stage at full resolution, and nothing about it is exceptional. The agent executes against a written unit, delegates its arithmetic to tools, writes its own provenance, and appends any assumption it was forced to make to the registry. The gate applies before anything advances, and the author's decision happens there, not in a review at the end. The price is one decision per gate; what it buys is a workflow whose every step is attributable.
- alt-text:      A sequence with five lanes: a specification unit, an agent, tools and data, a gate with its reviewer, and the author. Six numbered steps: the unit hands the agent its objective, inputs, criteria and stop conditions; the agent calls tools rather than reasoning in prose; it writes output and provenance and logs any new assumption to the registry rather than leaving it implicit; it submits for the check; a fail returns it within the budget the stop conditions set, and a pass goes forward; the author accepts, overrides or returns, with a vermillion note that the decision happens at the gate, not after the workflow has finished. A footer reads one decision per gate is the price of a workflow whose every step is attributable.
- infographic description: A flat vector sequence diagram, 16:9, off-white background,
                 five lanes top to bottom. Title top-left: "One gated stage, from
                 specification unit to author decision". Standfirst: "The author decides
                 at the gate, not after the workflow has finished." Lane headers: blue
                 tag "specification unit"; orange square "agent"; green wrench with
                 sky-blue cylinder "tools & data"; vermillion diamond with purple
                 reviewer icon "gate + reviewer"; blue human "author". Six numbered
                 arrows: "1 objective, inputs, criteria, stop"; "2 call tools, transform"
                 annotated "calculations go to tools, not prose"; "3 write output +
                 provenance" annotated "any new assumption goes to the registry, not left
                 implicit"; "4 submit for check"; "5 fail — return (within budget)"
                 curving back to the agent, annotated "loop bounded by the stop
                 conditions", beside "5 pass" going forward; "6 accept / override /
                 return" in the author lane, with a vermillion note "the author decides
                 at the gate, not after". Footer: "one decision per gate is the price of
                 a workflow whose every step is attributable". Sentence case throughout.
```
