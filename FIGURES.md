# Figure and infographic style guide

**v1.0 · 23 July 2026** · Binding for every figure in the book. Read alongside `STYLE.md`. British English throughout, including labels, captions and alt-text.

## 1. What this document is for

This guide fixes one house style for every figure in the book and defines a single **figure brief** format in which each figure is described. The two together have a specific purpose: a completed brief, prepended with the global style block in §4, is a self-contained prompt that an AI image generator can render without further context, so that the whole set of 65–75 figures can be produced in a small number of batch runs and still look like one designed system. Every figure in the manuscript is written as a brief following §6; no figure is drawn ad hoc.

The design brief in one line: **minimal, professional, flat, legible, and consistent** — an editorial-technical infographic look closer to a serious journal or a well-made textbook than to marketing material. Decoration is subtracted until only the idea remains. Confidence comes from restraint, alignment and whitespace, never from colour count, gradients or ornament.

## 2. Design principles

The house style rests on five principles that every brief inherits and no figure overrides without a stated reason. **Flatness**: two-dimensional vector shapes only — no photorealism, no three-dimensional extrusion, no bevels, drop-shadows, glows or textured fills. **Restraint**: the fewest elements that carry the idea; empty space is a design element, not a gap to fill. **Consistency**: the same icon, colour and connector conventions across all chapters, so a reader who has learned the visual vocabulary once reads every later figure faster. **Legibility**: high contrast, generous margins, short labels, and meaning never encoded by colour alone. **Function over decoration**: every mark earns its place by clarifying the argument; anything that does not is removed.

## 3. Fixed visual vocabulary

### 3.1 Palette (Okabe–Ito, colour-vision-safe)

The palette is the eight-colour Okabe–Ito set plus two neutrals, chosen because it remains distinguishable under the common forms of colour-vision deficiency. Colour is always paired with an icon, label or shape so that meaning survives in greyscale.

| Role (consistent book-wide) | Colour | Hex |
|---|---|---|
| Ink / text / structural lines | Near-black | `#111111` |
| Paper / background | Off-white | `#F7F7F5` |
| Human / human decision point | Blue | `#0072B2` |
| Agent (LLM-driven step) | Orange | `#E69F00` |
| Tool / function call | Bluish green | `#009E73` |
| Data store / dataset / artefact | Sky blue | `#56B4E9` |
| Gate / verification / check | Vermillion | `#D55E00` |
| Independent reviewer | Reddish purple | `#CC79A7` |
| Highlight / annotation (sparingly) | Yellow | `#F0E442` |
| Secondary / de-emphasis | Grey | `#999999` |

Yellow has poor contrast on white and is never used for text or thin lines — only as a fill behind a callout. The role-to-colour mapping is fixed for the whole book; a brief names the role, and the colour follows.

### 3.2 Iconography

A single, fixed icon set represents the recurring actors, introduced once in a front-matter icon-key figure and reused unchanged thereafter: **human** (a simple head-and-shoulders outline), **agent** (a rounded square enclosing a small loop arrow), **tool** (a wrench or gear glyph), **data store** (a cylinder), **gate** (a diamond), and **reviewer** (a head-and-shoulders outline with a small tick). Icons are line glyphs at a single stroke weight, monochrome in the role colour, never detailed illustrations.

### 3.3 Type, line and layout

Type is a single neutral sans-serif (grotesque), sentence case, used at two or three sizes only: figure-internal labels, a smaller annotation size, and — where the generator supports it — nothing else. Text inside figures is kept to the minimum needed to read the diagram; exposition belongs in the caption, not on the canvas. Connectors are single-weight lines with right-angle or gently rounded corners and a single arrowhead style; flow reads left-to-right or top-to-bottom, never both in one figure. Margins are generous and elements are aligned to a simple implied grid. The default canvas is **16:9 landscape**; portrait or square is used only where a brief states it and explains why.

## 4. Global style block (prepend to every generation prompt)

This block is prepended verbatim to each figure's `generator prompt` field (§6) to form the full prompt handed to the image generator. It is the mechanism by which one style holds across every figure.

```
STYLE: Minimal, professional, flat 2-D vector infographic for an academic book.
Editorial-technical look; no photorealism, no 3-D, no bevels, no drop-shadows, no
gradients, no textures, no clip-art. Solid off-white background (#F7F7F5). Near-black
(#111111) structural lines and text. Single neutral sans-serif, sentence case, minimal
on-canvas text. Single-weight connectors with one arrowhead style; clean right-angle or
softly rounded corners; clear single-direction flow; generous margins; aligned to an
implied grid. Colour-vision-safe Okabe–Ito palette used by fixed role — human/decision
blue #0072B2, agent orange #E69F00, tool green #009E73, data store sky #56B4E9,
gate/verification vermillion #D55E00, reviewer purple #CC79A7, highlight yellow #F0E442,
de-emphasis grey #999999. Meaning never carried by colour alone; every colour paired
with a labelled icon or shape. Icons are simple monochrome line glyphs. 16:9 canvas
unless stated. High contrast, legible, uncluttered.
```

## 5. The five canonical figure types

Every figure is one of five types, each with a fixed treatment so that figures of the same kind look alike across chapters. **Architecture** diagrams show components and their static relationships as labelled boxes and icons connected by lines, with nesting used to show containment (a model inside an agent inside a workflow). **Sequence** diagrams show ordered exchanges over time between a small number of actors, read top-to-bottom, with each step numbered. **Decision flowcharts** show branching logic through diamond gates with labelled yes/no exits, read top-to-bottom. **Before/after workflow** diagrams place a conventional workflow above or left and its agentic redesign below or right, sharing a common visual grammar so the difference is legible at a glance. **Annotated failure traces** show a real (anonymised) sequence in which something went wrong, with the failure point and the check that catches it called out in vermillion. The five types are the whole vocabulary; a figure that fits none is a sign the idea is not yet clear enough to draw.

## 6. The figure brief

Every figure is specified by a brief with the fields below. The first fields orient the human reader and the editor; the final `generator prompt` field, once the §4 block is prepended, is what the image generator receives. Keep the generator prompt concrete about elements, layout and exact labels, and free of exposition.

```
FIGURE BRIEF
- id:            Figure N.M (chapter.figure)
- title:         short descriptive title (appears in the caption)
- type:          architecture | sequence | decision flowchart | before/after | failure trace
- claim:         the single idea the figure must make legible, in one sentence
- canvas:        16:9 (default) | other, with reason
- elements:      the actors/objects, each with its fixed role-colour and icon
- flow:          direction and the ordered relationships/arrows between elements
- labels:        the exact on-canvas text, verbatim and minimal (short noun phrases)
- annotations:   any callouts, and what they point to
- caption:       prose caption in house voice (British English), stating what the figure shows and why it matters
- alt-text:      one to three sentences describing the figure for a non-sighted reader; written now, never retrofitted
- generator prompt: the composed description of the visual, concrete enough to render on its own once the §4 style block is prepended
```

## 7. Batch generation and quality control

The figures are generated by composing, for each brief, the §4 style block followed by the brief's `generator prompt`, and running the set together so the model holds the style steady. Where the tool exposes a style reference or seed, fix it across the run; where it exposes an aspect-ratio control, set 16:9 (or the brief's stated exception). After a run, each image is checked against three things before acceptance: the labels match the brief's `labels` field exactly, the role-colours are correct, and the figure reads correctly in greyscale. Figures that drift are regenerated, not patched piecemeal, so the set stays coherent.

## 8. Known limitations (honest constraints)

Current AI image generators are unreliable at rendering precise text, exact label placement and dense structural diagrams, and this limitation is stated here rather than discovered late. Three mitigations follow from it and are built into the workflow above: keep on-canvas text to short labels specified verbatim in the brief, so errors are easy to spot and correct; prefer few elements per figure, since crowded canvases degrade fastest; and expect that architecture and sequence figures with many exact labels may need their text corrected in a vector editor after generation, or the labels set in post rather than trusted to the model. Where a figure's correctness depends on precise, numerous labels that the generator cannot hold, that is a reason to simplify the figure, not to accept an inaccurate one. The house style — few elements, short labels, generous space — is chosen partly because it is the style these tools render most reliably.

## 9. Worked example

The following brief illustrates the format on the book's taxonomy figure. A second example, drawn from the author's own preferred subject, will be added below.

```
FIGURE BRIEF
- id:            Figure 1.2
- title:         The taxonomy as nesting — model inside agent inside workflow
- type:          architecture
- claim:         Autonomy is layered: each outer layer adds what the inner one lacks — the agent adds action and state to the model; the workflow adds specification, verification and accountability to the agent.
- canvas:        16:9
- elements:      outer rounded rectangle "agentic workflow" (grey structural border);
                 inside it, left, a "specification" tag (blue); a middle rounded rectangle
                 "AI agent" (orange border) containing an "LLM" box (orange), a
                 "plan–act–observe loop" ring, a "tools" glyph (green) and a
                 "state / memory" cylinder (sky blue); to the right of the agent a
                 diamond "verification gate" (vermillion); beyond it a "human decision"
                 head-and-shoulders icon (blue)
- flow:          left-to-right — specification → agent → gate; gate has two exits, "pass"
                 continuing right to the human decision, "fail" returning left to the agent
- labels:        "agentic workflow", "specification", "AI agent", "LLM",
                 "plan – act – observe", "tools", "state / memory", "verification gate",
                 "pass", "fail", "human decision"
- annotations:   none; the nesting itself carries the claim
- caption:       Figure 1.2 — The taxonomy as nesting: a model inside an agent inside a workflow. Each layer adds what the inner layer lacks — the agent adds action and state to the model; the workflow adds specification, verification and accountability to the agent.
- alt-text:      A nested diagram. The outer box, labelled agentic workflow, contains a specification feeding an inner box labelled AI agent, which contains an LLM connected to a plan–act–observe loop alongside tools and state. The agent's output passes through a verification gate that either proceeds to a human decision point or returns to the agent.
- generator prompt: A flat vector architecture diagram. A large grey-bordered rounded
                 rectangle labelled "agentic workflow" fills the canvas. Near its left
                 edge, a small blue tag labelled "specification" connects rightward into a
                 medium orange-bordered rounded rectangle labelled "AI agent". Inside that
                 orange rectangle: an orange box labelled "LLM" linked to a circular loop
                 arrow labelled "plan – act – observe", a green wrench icon labelled
                 "tools", and a sky-blue cylinder labelled "state / memory". From the right
                 edge of the "AI agent" rectangle an arrow leads to a vermillion diamond
                 labelled "verification gate". The diamond has two exits: an arrow labelled
                 "pass" continuing right to a blue head-and-shoulders icon labelled "human
                 decision", and an arrow labelled "fail" curving back left into the "AI
                 agent" rectangle. Minimal text, generous spacing, single-weight lines.
```

**[AUTHOR: add one example brief in your own preferred style here — e.g. a figure from operational flood forecasting — so the generator has a second reference for tone and composition.]**
