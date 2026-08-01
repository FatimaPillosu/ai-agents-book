# Figure briefs — Chapter 1 — Why agents, why now

Briefs for the figures of `manuscript/ch01-why-agents-why-now.md`, held here rather than in the chapter so the prose reads clean.
Each brief follows `FIGURES.md` §6. The caption and alt-text in the chapter are generated with the brief and must be changed here and there together.

## Figure 1.1 — Capability milestones (timeline)

```
FIGURE BRIEF
- id:            Figure 1.1
- title:         From text generation to structured action
- type:          sequence (horizontal timeline)
- claim:         Agents did not arrive in one step; they are the composition of a short, datable lineage of capabilities, the decisive ones concerning the interface to computation.
- standfirst:    Seven datable changes, of which two were about the interface rather than the capability.
- canvas:        16:9
- elements:      seven milestone nodes on a single left-to-right axis, each with a year, a
                 name in element-label type and a one-line note beneath in annotation type;
                 the two interface-changing milestones (in-context learning, tool calling)
                 filled in agent orange, the rest near-black outlines; a bracket spanning
                 the last four nodes
- flow:          left-to-right along one axis, 2017 to 2026, evenly spaced
- labels:        "2017 — transformer architecture", "2020 — in-context learning",
                 "2022 — public conversational systems", "2023 — tool calling",
                 "2023–24 — long context", "2024–25 — coding agents · tool protocols",
                 "2026 — governed agentic workflows"
- annotations:   under 2017, "made training on very large text practical"; under 2020,
                 "a task could now be described, not programmed"; under 2022, "the shift
                 became visible outside research"; under 2023, "the model could act, not
                 just describe"; under 2023–24, "a whole codebase could be held at once";
                 under 2024–25, "the work became checkable against tests"; under 2026,
                 "the subject of this book"; bracket under the last four, "from here a
                 system can act on what it says"
- caption:       Figure 1.1 — Agents did not arrive in one step. Seven datable changes got us here, and the two that mattered most, picked out in orange, were about how you talk to a computer rather than about raw capability. The dates are deliberately coarse and no product is named: that detail belongs in the repository, where it can be kept current.
- alt-text:      A horizontal timeline from 2017 to 2026 with seven labelled milestones. Each carries a year, a name and a short note on why it mattered: the transformer architecture in 2017 made training on very large text practical; in-context learning in 2020 meant a task could be described rather than programmed; public conversational systems in 2022 made the shift visible outside research; tool calling in 2023 let a model act rather than only describe; long context in 2023 to 2024 let a whole codebase be held at once; coding agents and tool protocols in 2024 to 2025 made the work checkable; and governed agentic workflows in 2026. The two milestones that changed the interface to computation, in-context learning and tool calling, are picked out in orange. A bracket beneath the last four reads that from here the system can act on what it says.
- infographic description: A flat vector horizontal timeline on an off-white background,
                 16:9. Title top-left in the largest size: "From text generation to
                 structured action". Beneath it a one-line standfirst: "Seven datable
                 changes, of which two were about the interface rather than the
                 capability." A single near-black axis runs left to right across the middle
                 with seven evenly spaced round nodes. Above each node, the year and name
                 in element-label type; below each node, a one-line note in smaller
                 annotation type. In order: "2017 transformer architecture" / "made
                 training on very large text practical"; "2020 in-context learning" / "a
                 task could now be described, not programmed"; "2022 public conversational
                 systems" / "the shift became visible outside research"; "2023 tool
                 calling" / "the model could act, not just describe"; "2023–24 long
                 context" / "a whole codebase could be held at once"; "2024–25 coding
                 agents and tool protocols" / "the work became checkable against tests";
                 "2026 governed agentic workflows" / "the subject of this book". The nodes
                 for in-context learning and tool calling are filled agent orange; the
                 other five are near-black outlines. A thin bracket spans the last four
                 nodes beneath their notes, labelled "from here a system can act on what it
                 says". Generous margins, single stroke weight, sentence case throughout.
```

## Figure 1.2 — The taxonomy as nesting

```
FIGURE BRIEF
- id:            Figure 1.2
- title:         A model inside an agent inside a workflow
- type:          architecture
- claim:         Autonomy is layered: each outer layer adds what the inner one lacks (the agent adds action and state to the model; the workflow adds specification, verification and accountability to the agent).
- standfirst:    Each layer adds what the one inside it cannot do on its own.
- canvas:        16:9
- elements:      outer rounded rectangle "agentic workflow" (grey structural border);
                 inside it, left, a "specification" tag (blue); a middle rounded rectangle
                 "AI agent" (orange border) containing an "LLM" box (orange), a
                 "plan–act–observe loop" ring, a "tools" glyph (green) and a
                 "state / memory" cylinder (sky blue); to the right of the agent a
                 diamond "verification gate" (vermillion); beyond it a "human decision"
                 head-and-shoulders icon (blue); a four-entry colour key along the foot
- flow:          left-to-right — specification → agent → gate; the gate has two labelled
                 exits, "pass" continuing right to the human decision, "fail" returning
                 left into the agent
- labels:        "agentic workflow", "specification", "AI agent", "LLM",
                 "plan – act – observe", "tools", "state / memory", "verification gate",
                 "pass", "fail", "human decision"
- annotations:   on the LLM box, "predicts text, cannot act"; on the loop ring, "acts,
                 sees the result, decides again"; on the tools glyph, "does what the model
                 does badly: arithmetic, retrieval, execution"; on the state cylinder,
                 "what survives between steps"; on the specification tag, "written before
                 the agent starts"; on the gate, "nothing passes because it looks right";
                 on the human icon, "accountable, and cannot delegate that"
- caption:       Figure 1.2 — A model inside an agent inside a workflow. The model only predicts text; wrap it in a loop with tools and memory and you have an agent that can act; wrap that in a specification, a gate and a human decision and you have a workflow you can defend. Each layer supplies what the one inside it lacks, which is why the outer layers are where the governing happens.
- alt-text:      A nested diagram in three layers. The outer box, agentic workflow, contains a specification tag noted as written before the agent starts, feeding an inner box labelled AI agent. Inside the agent sit an LLM box noted as predicting text but unable to act, a plan-act-observe loop noted as acting, seeing the result and deciding again, a tools glyph noted as doing what the model does badly, and a state and memory cylinder noted as what survives between steps. The agent's output passes to a vermillion verification gate annotated "nothing passes because it looks right", whose pass exit reaches a human decision point annotated as accountable and unable to delegate that, and whose fail exit returns to the agent.
- infographic description: A flat vector architecture diagram, 16:9. Title top-left in the
                 largest size: "A model inside an agent inside a workflow". Beneath it a
                 one-line standfirst: "Each layer adds what the one inside it cannot do on
                 its own." A large grey-bordered rounded rectangle labelled "agentic
                 workflow" fills the lower four-fifths of the canvas. Near its left edge a
                 small blue tag "specification", annotated beneath in small type "written
                 before the agent starts", connects rightward into a medium orange-bordered
                 rounded rectangle "AI agent". Inside that rectangle, arranged in a row: an
                 orange box "LLM" annotated "predicts text, cannot act"; a circular loop
                 arrow "plan – act – observe" annotated "acts, sees the result, decides
                 again"; a green wrench icon "tools" annotated "does what the model does
                 badly: arithmetic, retrieval, execution"; and a sky-blue cylinder "state /
                 memory" annotated "what survives between steps". From the agent's right
                 edge an arrow leads to a vermillion diamond "verification gate", with a
                 callout in a pale yellow fill reading "nothing passes because it looks
                 right". The diamond has two labelled exits: "pass", continuing right to a
                 blue head-and-shoulders icon "human decision" annotated "accountable, and
                 cannot delegate that"; and "fail", curving back left into the agent
                 rectangle. A four-entry key runs along the foot: blue human, orange agent,
                 green tool, sky-blue data store. Generous margins, single-weight lines,
                 all text in sentence case.
```
