# Figure briefs — Chapter 12 — Provenance, governance and security

Briefs for the figures of `manuscript/ch12-provenance-governance-and-security.md`, held here rather than in the chapter so the prose reads clean.
Each brief follows `FIGURES.md` §6. The caption and alt-text in the chapter are generated with the brief and must be changed here and there together.

## Figure 12.1 — The governance layer: registries and audit trail beside the workflow

```
FIGURE BRIEF
- id:            Figure 12.1
- title:         A governance layer that records without steering
- type:          architecture
- claim:         Provenance is captured by a standing governance layer that sits beside the workflow and is fed by the same events the workflow already emits.
- standfirst:    The workflow writes to the layer. The layer never steers the workflow.
- canvas:        16:9
- elements:      left, a vertical workflow stack — "specification" tag (blue), "AI agent"
                 (orange border), "tool call" glyph (green), "human decision" icon (blue);
                 right, a grey-bordered "governance layer" containing four sky-blue
                 cylinders: "assumption registry", "uncertainty registry", "audit trail",
                 "reviewer-coverage record"
- flow:          the workflow runs top-to-bottom on the left; thin one-directional arrows
                 lead rightward from each workflow element into the governance layer
- labels:        "specification", "AI agent", "tool call", "human decision",
                 "governance layer", "assumption registry", "uncertainty registry",
                 "audit trail", "reviewer-coverage record"
- annotations:   on the assumption registry, "what did the analysis take as given, and who
                 agreed?"; on the uncertainty registry, "what does the workflow not know,
                 and how much?"; on the audit trail, "what happened, in what order,
                 invoked by whom?"; on the coverage record, "what was actually reviewed —
                 and what was not?"; on the arrows, "fed by events the workflow already
                 emits — no extra effort"; a bracket down the layer, "institutional memory
                 — survives staff turnover"
- caption:       Figure 12.1 — The record is a by-product, not a chore. Every element of the workflow already emits events, and the governance layer captures them into four standing records. Each answers a different question: what was assumed, what is uncertain, what happened, and what was actually reviewed. The arrows only point one way. The layer records; it never steers.
- alt-text:      On the left, a workflow running top to bottom: a specification, an AI agent, a tool call and a human decision. On the right, a governance layer holding four record stores: an assumption registry, an uncertainty registry, an audit trail and a reviewer-coverage record, each with a one-line note of the question it answers. One-directional arrows run from every workflow element into the layer, annotated that the workflow writes to the layer and the layer never steers the workflow, and that the records are fed by events the workflow already emits, at no extra effort. A bracket down the layer reads institutional memory, survives staff turnover.
- infographic description: A flat vector architecture diagram, 16:9, off-white
                 background. Title top-left: "A governance layer that records without
                 steering". Standfirst: "The workflow writes to the layer. The layer never
                 steers the workflow." Left third: a vertical stack — blue tag
                 "specification", orange rounded rectangle "AI agent", green wrench "tool
                 call", blue human icon "human decision", joined by downward arrows. Right
                 two-thirds: a large grey-bordered rounded rectangle "governance layer"
                 containing four sky-blue cylinders in a column, each with its annotation
                 to the right: "assumption registry" / "what did the analysis take as
                 given, and who agreed?"; "uncertainty registry" / "what does the workflow
                 not know, and how much?"; "audit trail" / "what happened, in what order,
                 invoked by whom?"; "reviewer-coverage record" / "what was actually
                 reviewed — and what was not?". Thin one-directional arrows run from each
                 workflow element into the layer, sharing the note "fed by events the
                 workflow already emits — no extra effort". A bracket down the layer's
                 right edge reads "institutional memory — survives staff turnover".
                 Sentence case throughout.
```

## Figure 12.2 — The trust boundary: what the agent may reach, and what waits on a human

```
FIGURE BRIEF
- id:            Figure 12.2
- title:         Least privilege and the trust boundary
- type:          architecture
- claim:         Security is bounded by drawing an explicit trust boundary: untrusted inputs enter through validation, the agent holds only the narrowest tool permissions, and any consequential action waits on a human gate.
- standfirst:    An injected instruction can only do what the granted tools allow.
- canvas:        16:9
- elements:      a central grey-bordered rounded rectangle "trusted zone" containing an
                 "AI agent" (orange border), a "specification" tag (blue) and "permitted
                 tools" glyphs (green) with a lock annotation; left, three untrusted
                 sources (grey): "external documents", "web content", "third-party data",
                 entering through a vermillion validation gate; right, three consequential
                 actions outside the zone: "write to shared system", "send communication",
                 "irreversible command", reachable only through a blue human gate
- flow:          left-to-right — untrusted sources pass through the validation gate into
                 the zone as data; the agent calls only permitted tools; proposed
                 consequential actions exit rightward only through the human gate
- labels:        "trusted zone", "AI agent", "specification", "permitted tools",
                 "least privilege", "external documents", "web content",
                 "third-party data", "validate · quote as data", "write to shared system",
                 "send communication", "irreversible command", "human gate"
- annotations:   on the validation gate, "quoted as data to analyse — never instructions
                 to follow"; on the permitted tools, "deny by default — each capability
                 granted deliberately"; on the human gate, "the agent proposes; a person
                 disposes"; on the boundary, "the artefact institutional IT will ask to
                 see"; a footer, "an injected instruction can only do what the granted
                 tools allow — least privilege is the primary defence"
- caption:       Figure 12.2 — The line that decides what an attack can accomplish. Untrusted text enters only as quoted data, the agent holds the narrowest tool set that still does the job, and anything consequential leaves only through a human gate. Draw this boundary explicitly: it is what bounds an injected instruction to the capabilities you actually granted, and it is the artefact your security team will ask to see.
- alt-text:      A central trusted zone holds the AI agent, its specification and a small set of permitted tools marked least privilege, deny by default. To the left, outside the boundary, three untrusted sources, external documents, web content and third-party data, enter only through a validation gate annotated quoted as data to analyse, never instructions to follow. To the right, three consequential actions, writing to a shared system, sending a communication and running an irreversible command, sit outside the boundary and are reachable only through a human gate annotated the agent proposes, a person disposes. The boundary itself is annotated as the artefact institutional IT will ask to see. A footer reads that an injected instruction can only do what the granted tools allow, which is why least privilege is the primary defence.
- infographic description: A flat vector architecture diagram, 16:9, off-white
                 background. Title top-left: "Least privilege and the trust boundary".
                 Standfirst: "An injected instruction can only do what the granted tools
                 allow." Centre: a large grey-bordered rounded rectangle "trusted zone",
                 annotated on its border "the artefact institutional IT will ask to see",
                 containing a blue tag "specification", an orange rounded rectangle "AI
                 agent", and three green wrench glyphs "permitted tools" with a small lock
                 and the note "deny by default — each capability granted deliberately",
                 headed "least privilege". Left of the zone: three grey boxes stacked,
                 "external documents", "web content", "third-party data", their arrows
                 converging on a vermillion diamond "validate · quote as data" on the
                 boundary, annotated "quoted as data to analyse — never instructions to
                 follow". Right of the zone: three grey boxes, "write to shared system",
                 "send communication", "irreversible command", reachable only through a
                 blue human icon "human gate" on the boundary, annotated "the agent
                 proposes; a person disposes". Footer: "an injected instruction can only
                 do what the granted tools allow — least privilege is the primary
                 defence". Sentence case throughout.
```
