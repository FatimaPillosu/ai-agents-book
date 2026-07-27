# Figure and infographic style guide

**v2.0 · 26 July 2026** · Binding for every figure in the book. Read alongside `STYLE.md` v5.0. British English throughout, including labels, captions and alt-text.

**Change from v1.0 (major):** the house style moves from minimal diagram to **explanatory infographic**, on the author's instruction of 26 July 2026. Figures now carry enough on-canvas text to be understood on their own, without the reader holding the surrounding prose in mind. Three things change: §2 replaces the restraint principle with explanatory density; §3.3 defines a five-level text hierarchy in place of "minimal on-canvas text"; and the brief's `generator prompt` field is replaced by an **`infographic description`** (§6) that specifies every piece of text on the canvas, so the description can be handed to a designer or an image tool and produce a finished infographic rather than a skeleton. Captions and alt-text move to the colloquial register of `STYLE.md` v5.0. What does not change: the Okabe–Ito role palette, the fixed iconography, flatness, colour-vision safety, and the rule that meaning is never carried by colour alone.

> **Render status.** All 51 SVGs under `figures/` are rendered from the v2.0 briefs through the shared house renderer (`figures-src/`): orthogonal connectors only, a five-level type hierarchy, and an automated collision check that verifies no text crosses a line, a shape border or another text. Regenerate any figure by editing its entry in `figures-src/f_*.py` and re-running the script; the renderer fails loudly on any new overlap. **[AUTHOR: the renders are consistent technical infographics; if a designed look is wanted for release, the briefs' infographic descriptions are the hand-off specification.]**

## 1. What this document is for

This guide fixes one house style for every figure in the book and defines a single **figure brief** format in which each figure is described. A completed brief is a self-contained specification: hand its `infographic description` to a designer, an illustration tool or an image generator and you should get back a finished, readable infographic without needing the chapter beside it. Every figure in the manuscript is written as a brief following §6. No figure is drawn ad hoc.

The design brief in one line: **explanatory, professional, flat, legible and consistent** — an editorial-technical infographic closer to a well-made textbook diagram or a good newspaper explainer than to either a bare flowchart or marketing material. A figure earns its place by teaching something on its own, and the text it needs to do that belongs on the canvas.

## 2. Design principles

Five principles, which every brief inherits and no figure overrides without a stated reason.

**Explanatory density.** A figure carries enough words to be understood by a reader who has not yet read the surrounding paragraph. Labels name things; short annotations say what happens and why it matters. This replaces the v1.0 restraint principle, which produced diagrams that were elegant and, on their own, close to unreadable. Density is not clutter: every piece of text still earns its place, and the test is whether removing it would leave a reader guessing.

**Flatness.** Two-dimensional vector shapes only. No photorealism, no three-dimensional extrusion, no bevels, drop-shadows, glows or textured fills.

**Consistency.** The same icons, role-colours and connector conventions across all chapters, so a reader who has learned the visual vocabulary once reads every later figure faster.

**Legibility.** High contrast, generous margins, a clear text hierarchy, and meaning never encoded by colour alone. Density and legibility are in tension, and legibility wins: if the canvas is crowded enough that the eye cannot find its starting point, split the figure or drop a level of detail.

**Function over decoration.** Every mark earns its place by clarifying the argument. Nothing is added because the canvas looks empty.

## 3. Fixed visual vocabulary

### 3.1 Palette (Okabe–Ito, colour-vision-safe)

The palette is the eight-colour Okabe–Ito set plus two neutrals, chosen because it stays distinguishable under the common forms of colour-vision deficiency. Colour is always paired with an icon, label or shape so meaning survives in greyscale.

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

Yellow has poor contrast on white and is never used for text or thin lines, only as a fill behind a callout. The role-to-colour mapping is fixed for the whole book: a brief names the role and the colour follows.

### 3.2 Iconography

A single fixed icon set represents the recurring actors, introduced once in the front-matter icon key and reused unchanged: **human** (a simple head-and-shoulders outline), **agent** (a rounded square enclosing a small loop arrow), **tool** (a wrench or gear glyph), **data store** (a cylinder), **gate** (a diamond), and **reviewer** (a head-and-shoulders outline with a small tick). Icons are line glyphs at a single stroke weight, monochrome in the role colour, never detailed illustrations.

### 3.3 Type hierarchy, line and layout

Type is a single neutral sans-serif (grotesque) in sentence case, used at **five defined levels**. This replaces v1.0's two or three sizes and its instruction to keep on-canvas text minimal.

1. **Figure title** — the largest text, top-left or top-centre, naming what the figure shows. Present on every figure.
2. **Standfirst** — one short sentence under the title, stating the figure's claim in plain language. Present on every figure. This is the single biggest change from v1.0 and the main reason the figures now stand alone.
3. **Element labels** — the names of boxes, icons and stages. Short noun phrases.
4. **Annotations** — short explanatory phrases attached to a specific element or arrow, saying what happens there or why it matters. Typically four to eight per figure, where v1.0 had none or one.
5. **Key / footnote** — where a figure uses more than three role-colours, a small key strip; and where a figure needs a caveat, one short line at the bottom.

Connectors are single-weight lines with right-angle or gently rounded corners and a single arrowhead style. Flow reads left-to-right or top-to-bottom, never both in one figure. Arrows carry labels wherever the relationship is not obvious from the shapes alone. Margins stay generous and elements align to a simple implied grid; the added text is accommodated by using the canvas fully, not by crowding the middle. Default canvas is **16:9 landscape**; portrait or square only where a brief states it and says why.

## 4. Global style block (prepend to every infographic description)

Prepended verbatim to each figure's `infographic description` (§6) to form the full brief handed to a designer or image tool. It is the mechanism by which one style holds across every figure.

```
STYLE: Explanatory, professional, flat 2-D vector infographic for an academic book.
Editorial-technical look, like a well-made textbook diagram or a serious newspaper
explainer. No photorealism, no 3-D, no bevels, drop-shadows, gradients, textures or
clip-art. Solid off-white background (#F7F7F5). Near-black (#111111) structural lines
and text. Single neutral sans-serif throughout, sentence case, in five sizes: figure
title (largest), a one-sentence standfirst beneath it, element labels, smaller
annotations, and a small key or footnote. The figure must be understandable on its own,
without the surrounding text: label every element and annotate every step that is not
self-evident. Single-weight connectors, one arrowhead style, right-angle or softly
rounded corners, one clear direction of flow, labelled arrows. Generous margins, aligned
to an implied grid, canvas used fully rather than crowded at the centre.
Colour-vision-safe Okabe-Ito palette by fixed role: human/decision blue #0072B2, agent
orange #E69F00, tool green #009E73, data store sky #56B4E9, gate/verification vermillion
#D55E00, reviewer purple #CC79A7, highlight yellow #F0E442 (fills only, never text),
de-emphasis grey #999999. Meaning never carried by colour alone; every colour paired
with a labelled icon or shape. Icons are simple monochrome line glyphs. 16:9 canvas
unless stated. High contrast, legible at half size, readable in greyscale.
```

## 5. The five canonical figure types

Every figure is one of five types, each with a fixed treatment so figures of the same kind look alike across chapters.

**Architecture** diagrams show components and their static relationships as labelled boxes and icons connected by lines, with nesting for containment. Annotate what each component does, not only what it is called.

**Sequence** diagrams show ordered exchanges over time between a small number of actors, read top-to-bottom, each step numbered. Annotate what each step produces.

**Decision flowcharts** show branching logic through diamond gates with labelled yes/no exits, read top-to-bottom. Every exit is labelled, and every terminal states the outcome in full rather than in shorthand.

**Before/after workflow** diagrams place a conventional workflow above and its agentic redesign below, sharing a visual grammar so the difference reads at a glance. Annotate what changed between the rows, and what deliberately did not.

**Annotated failure traces** show a real, anonymised sequence in which something went wrong, with the failure point and the check that catches it called out in vermillion. These carry the heaviest annotation load in the book: the reader needs to see what looked right at each step.

A figure that fits none of the five is a sign the idea is not yet clear enough to draw.

## 6. The figure brief

Every figure is specified by a brief with the fields below. The early fields orient the human reader and the editor; the final `infographic description` field, once the §4 block is prepended, is the complete specification handed to whoever renders it.

```
FIGURE BRIEF
- id:            Figure N.M (chapter.figure)
- title:         the on-canvas figure title (also opens the caption)
- type:          architecture | sequence | decision flowchart | before/after | failure trace
- claim:         the single idea the figure must make legible, in one sentence
- standfirst:    the on-canvas one-sentence version of the claim, in the reader's language
- canvas:        16:9 (default) | other, with reason
- elements:      the actors/objects, each with its fixed role-colour and icon
- flow:          direction, and the ordered labelled relationships between elements
- labels:        the exact on-canvas element text, verbatim (short noun phrases)
- annotations:   the exact on-canvas explanatory phrases, verbatim, and what each attaches
                 to; four to eight is the normal range
- caption:       prose caption in the colloquial register of STYLE.md v5.0, saying what
                 the figure shows and why it matters
- alt-text:      a description for a non-sighted reader that conveys the same understanding
                 a sighted reader gets, including the annotations; written now, never
                 retrofitted
- infographic description: the complete visual specification — layout, every element, every
                 piece of on-canvas text quoted verbatim, and the relationships between
                 them — concrete enough to render into a finished infographic once the §4
                 style block is prepended
```

### 6.1 Captions

Captions are written in the colloquial register (`STYLE.md` v5.0 §1): plain, direct, addressing the reader where the sentence calls for it, and never announcing what the figure is about to do. Two or three sentences. Say what the figure shows, then what to take from it. A caption never simply restates the title, and it never carries information the figure itself should have carried.

The caption ends with the render pointer in the fixed form `(Rendered as \`figures/figure-N-M.svg\` from the brief below, per \`FIGURES.md\`.)`

### 6.2 Alt-text

Alt-text gives a non-sighted reader the same understanding a sighted reader gets, which under v2.0 means it must carry the annotations, not only the shapes. Describe the layout, then the elements, then what the annotations say. Length follows the figure: a simple architecture diagram may need three sentences, an annotated failure trace may need six. Written at the same time as the brief, never retrofitted, and in the same colloquial register as the caption.

## 7. Batch rendering and quality control

Render by composing, for each brief, the §4 style block followed by the brief's `infographic description`. Run the set together so the style holds steady, and fix any style reference or seed across the run.

Check every figure against five things before accepting it: the element labels match the brief's `labels` field exactly; the annotations match the `annotations` field exactly; the role-colours are correct; the figure reads in greyscale; and the figure is legible at half size, which is the realistic size on a page. Figures that drift are re-rendered rather than patched piecemeal, so the set stays coherent.

## 8. Known limitations (honest constraints)

**The density this guide asks for is the thing image generators are worst at.** v1.0 chose minimalism partly because sparse figures with short labels are what these tools render most reliably; v2.0 asks for titles, standfirsts and up to eight annotations per canvas, and current generators will not place that much text accurately. This tension is real and is not resolved by wishing.

Three consequences follow, and the workflow assumes them. First, the `infographic description` should be treated as a **specification for a designer or a vector tool**, and only secondarily as an image-generation prompt. Second, where a figure is generated, expect to set the text in a vector editor afterwards rather than trusting the model to place it: the brief quotes every string verbatim precisely so this is mechanical rather than interpretive. Third, hand-authored SVG remains a legitimate route, and for the annotation-heavy failure traces of Chapter 13 it is likely the only reliable one.

Where a figure's correctness depends on precise, numerous labels, that is a reason to author it properly, not to accept an inaccurate render. **[AUTHOR: decide the rendering route for the v2.0 set — designer, vector tool, generated-then-corrected, or hand-authored SVG — since it determines how the descriptions are used.]**

## 9. Worked example

The book's taxonomy figure, in the v2.0 format. Compare it with the v1.0 version in this file's git history to see what the change asks for.

```
FIGURE BRIEF
- id:            Figure 1.2
- title:         A model inside an agent inside a workflow
- type:          architecture
- claim:         Autonomy is layered: each outer layer adds what the inner one lacks — the agent adds action and state to the model; the workflow adds specification, verification and accountability to the agent.
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
- caption:       Figure 1.2 — A model inside an agent inside a workflow. The model only predicts text; wrap it in a loop with tools and memory and you have an agent that can act; wrap that in a specification, a gate and a human decision and you have a workflow you can defend. Each layer supplies what the one inside it lacks, which is why the outer layers are where the governing happens. (Rendered as `figures/figure-1-2.svg` from the brief below, per `FIGURES.md`.)
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

**[AUTHOR: add one example brief in your own preferred style here — e.g. a figure from operational flood forecasting — so whoever renders the set has a second reference for tone and composition.]**
