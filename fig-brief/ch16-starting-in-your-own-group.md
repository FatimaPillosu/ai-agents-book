# Figure briefs — Chapter 16 — Starting in your own group

Briefs for the figures of `manuscript/ch16-starting-in-your-own-group.md`, held here rather than in the chapter so the prose reads clean.
Each brief follows `FIGURES.md` §6. The caption and alt-text in the chapter are generated with the brief and must be changed here and there together.

## Figure 16.1 — A capability-based thirty-day plan

```
FIGURE BRIEF
- id:            Figure 16.1
- title:         The thirty-day plan as a sequence of habits, not tools
- type:          before/after
- claim:         A durable start builds three capabilities in order (specify, verify, govern, then compose), each producing a kept artefact, in contrast to the tool-first start that produces only interface familiarity.
- standfirst:    Each week ends with an artefact you keep, not a tutorial you completed.
- canvas:        16:9
- elements:      top band, de-emphasis grey, "tool-first start": "adopt a product" →
                 "learn the interface" → a grey question mark "trust?"; bottom band, four
                 sequential boxes — week 1 "specify" (blue, specification tag), week 2
                 "verify" (vermillion, gate diamond), week 3 "govern" (near-black,
                 audit-trail document), week 4 "compose" (orange, agent glyph), each with
                 its kept artefact beneath
- flow:          top band left-to-right ending in the question mark; bottom band
                 left-to-right, each week feeding the next
- labels:        "tool-first start", "adopt a product", "learn the interface", "trust?",
                 "week 1 — specify", "week 2 — verify", "week 3 — govern",
                 "week 4 — compose", "kept: a specification",
                 "kept: a verification record", "kept: an audit trail",
                 "kept: a working governed workflow"
- annotations:   on the top band, "what was learned has the lifespan of the product"; on
                 week 1, "a colleague agrees it constitutes the task"; on week 2, "no
                 output is used before a check external to the agent passes"; on week 3,
                 "an audit trail an IT reviewer could inspect"; on week 4, "reviewed
                 against one question: did this save net effort once the checking is
                 counted?"; a bracket under the four weeks, "habits that survive a change
                 of tool"
- caption:       Figure 16.1 — Two ways to spend a first month. The grey path is the common one: adopt a product, learn its interface, and end up unable to say why the output should be trusted. The four-week path builds one capability at a time, and each week's deliverable is an artefact you keep, not a tutorial you complete. The sequence matters more than the calendar; the artefacts survive every change of tool.
- alt-text:      Two bands. The top band, greyed, shows the tool-first start: adopt a product, learn the interface, then a question mark labelled trust, annotated that what was learned has the lifespan of the product. The bottom band shows four weeks: week one, specify, keeping a real specification a colleague agrees constitutes the task; week two, verify, keeping a verification record and the habit that no output is used before a check external to the agent passes; week three, govern, keeping an audit trail an IT reviewer could inspect; week four, compose, keeping a working governed workflow reviewed against one plain question, did this save net effort once the checking is counted. A bracket underneath reads habits that survive a change of tool.
- infographic description: A flat vector before-and-after diagram, 16:9, off-white
                 background, two bands. Title top-left: "The thirty-day plan as a
                 sequence of habits, not tools". Standfirst: "Each week ends with an
                 artefact you keep, not a tutorial you completed." Top band in
                 de-emphasis grey, labelled "tool-first start": boxes "adopt a product"
                 and "learn the interface" leading to a grey question mark "trust?",
                 annotated "what was learned has the lifespan of the product". Bottom
                 band: four boxes left to right — "week 1 — specify" (blue, with a
                 specification tag icon) over "kept: a specification", annotated "a
                 colleague agrees it constitutes the task"; "week 2 — verify" (vermillion
                 diamond icon) over "kept: a verification record", annotated "no output
                 is used before a check external to the agent passes"; "week 3 — govern"
                 (near-black document icon) over "kept: an audit trail", annotated "an
                 audit trail an IT reviewer could inspect"; "week 4 — compose" (orange
                 agent glyph) over "kept: a working governed workflow", annotated
                 "reviewed against one question: did this save net effort once the
                 checking is counted?". A bracket beneath spans all four: "habits that
                 survive a change of tool". Sentence case throughout.
```

## Figure 16.2 — Where adoption spend concentrates

```
FIGURE BRIEF
- id:            Figure 16.2
- title:         The cost model — inference is the smallest share
- type:          architecture
- claim:         In a well-run scientific workflow the visible cost of model inference is the smallest of the recurring costs; engineering, evaluation and verification dominate, and verification is the one to protect.
- standfirst:    The line item everyone watches is the smallest one on the canvas.
- canvas:        16:9
- elements:      five cost blocks left to right, sized to suggest relative magnitude: a
                 small orange block "model inference"; a larger near-black block
                 "engineering"; a large vermillion block "evaluation"; the largest
                 vermillion block "verification (recurring)"; a medium grey
                 dashed-outline block "failure & rework"; a caption strip beneath
- flow:          no directional flow; left-to-right ordering from the smallest recurring
                 cost to the dominant one
- labels:        "model inference", "engineering", "evaluation",
                 "verification (recurring)", "failure & rework",
                 "magnitudes illustrative — dated figures in repository"
- annotations:   under "model inference", an arrow "falling fast" and the note "the cost
                 everyone watches"; on "engineering", "recurring human time — specify,
                 wire, maintain"; on "evaluation", "is the agent reliable enough to use
                 at all?"; on "verification", "recurs for as long as the workflow runs —
                 and does not fall as model prices fall"; on "failure & rework", "shrinks
                 exactly to the degree the other three are funded"; a bracket over
                 evaluation and verification, "where the spend actually concentrates"
- caption:       Figure 16.2 — The cost everyone watches is the smallest block. Inference is falling fast and is the least of it; engineering, evaluation and above all verification are the recurring costs. Verification does not fall as model prices fall, because it is external to the model by design. The dashed block is the honest one: failure and rework shrinks exactly to the degree the other three are funded. Budget from this picture, not from a price-per-token page.
- alt-text:      Five cost blocks in a row, sized to suggest relative magnitude rather than exact figures. A small orange block, model inference, carries a downward arrow labelled falling fast and the note that this is the cost everyone watches. Larger blocks follow: engineering, annotated as recurring human time to specify, wire and maintain; evaluation, annotated as establishing whether the agent is reliable enough to use at all; and the largest, verification, annotated as recurring for as long as the workflow runs, and not falling as model prices fall. A dashed-outlined grey block, failure and rework, is annotated as shrinking exactly to the degree the other three are funded. A bracket over evaluation and verification reads where the spend actually concentrates, and a caption strip reads magnitudes illustrative, dated figures in the repository.
- infographic description: A flat vector block diagram, 16:9, off-white background.
                 Title top-left: "The cost model — inference is the smallest share".
                 Standfirst: "The line item everyone watches is the smallest one on the
                 canvas." Five blocks in a row, heights suggesting relative magnitude: a
                 small orange block "model inference" with a small downward arrow
                 "falling fast" and the note "the cost everyone watches"; a taller
                 near-black block "engineering" annotated "recurring human time —
                 specify, wire, maintain"; a taller vermillion block "evaluation"
                 annotated "is the agent reliable enough to use at all?"; the tallest
                 vermillion block "verification (recurring)" annotated "recurs for as
                 long as the workflow runs — and does not fall as model prices fall"; and
                 a medium grey dashed-outline block "failure & rework" annotated
                 "shrinks exactly to the degree the other three are funded". A bracket
                 spans evaluation and verification: "where the spend actually
                 concentrates". A caption strip beneath: "magnitudes illustrative — dated
                 figures in repository". Sentence case throughout.
```
