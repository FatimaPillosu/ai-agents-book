# Figure briefs — Chapter 7 — Coding and pipeline agents

Briefs for the figures of `manuscript/ch07-coding-and-pipeline-agents.md`, held here rather than in the chapter so the prose reads clean.
Each brief follows `FIGURES.md` §6. The caption and alt-text in the chapter are generated with the brief and must be changed here and there together.

## Figure 7.1 — The gate stack

```
FIGURE BRIEF
- id:            Figure 7.1
- title:         Four gates between an agent's code and the main branch
- type:          architecture
- claim:         An agent's code is trusted only after passing successive independent gates (tests, hooks, an independent reviewer agent), with an accountable human owning the final merge.
- standfirst:    Cheap checks first, so your attention is spent only on what survives them.
- canvas:        16:9
- elements:      left, an "author agent" rounded square (orange, with loop-arrow icon)
                 emitting a "proposed change" artefact (sky-blue document glyph); then a
                 left-to-right series of three gates, each a vermillion diamond —
                 "automated tests", "pre-commit hooks", "independent reviewer agent" (the
                 third also carrying the reviewer icon, purple, head-and-shoulders with a
                 tick); finally a blue "human owner" head-and-shoulders icon and a
                 "main branch" terminus
- flow:          left-to-right — author agent → proposed change → tests gate → hooks gate →
                 reviewer-agent gate → human owner → main branch; each gate has a "fail"
                 exit curving back to the author agent
- labels:        "author agent", "proposed change", "automated tests", "pre-commit hooks",
                 "independent reviewer agent", "human owner", "main branch", "fail"
- annotations:   on "automated tests", "the assertions must encode intended behaviour, not
                 whatever the code happens to do"; on "pre-commit hooks", "formatting,
                 linting, type checks, secrets scan, full suite — run automatically, so
                 nobody can forget"; on "independent reviewer agent", "a different
                 instance, its own context, read-only, no power to approve or merge"; on
                 "human owner", "reads the report and the change, and owns the merge"; a
                 bracket under the three diamonds, "cheap mechanical gates first — the
                 expensive one last"; on the fail arrows, "back to the author, with the
                 reason"
- caption:       Figure 7.1 — Four gates, in a deliberate order. Each is cheaper than the review it protects, and each catches a different class of error. The mechanical checks reject most defects at near-zero cost. Your attention is the scarce resource, and it is spent only on changes that have already cleared everything a machine can decide. The reviewer agent advises; the human decides.
- alt-text:      A left-to-right architecture diagram. An author agent emits a proposed change, which meets four gates in turn. First a vermillion automated-tests diamond, annotated that the assertions have to encode intended behaviour, not whatever the code happens to do. Second a pre-commit hooks diamond, annotated as formatting, linting, type checks, a secrets scan and the test suite, run automatically so nobody can forget them. Third an independent reviewer agent carrying a purple reviewer icon, annotated as a different instance with its own context, read-only, with no power to approve or merge. Fourth a blue human owner, annotated as reading the reviewer's report and owning the decision to merge. Each gate has a fail exit curving back to the author agent. A bracket under the first three reads that the cheap mechanical gates run first so the expensive human attention is spent only on what has already cleared them.
- infographic description: A flat vector architecture diagram on an off-white background,
                 16:9, flowing left to right. Title top-left: "Four gates between an agent's
                 code and the main branch". Standfirst beneath: "Cheap checks first, so your
                 attention is spent only on what survives them." At the left an orange
                 rounded square with a loop-arrow icon, "author agent", emits a sky-blue
                 document glyph "proposed change". Three vermillion diamonds follow in a
                 row: "automated tests", annotated "the assertions must encode intended
                 behaviour, not whatever the code happens to do"; "pre-commit hooks",
                 annotated "formatting, linting, type checks, secrets scan, full suite — run
                 automatically, so nobody can forget"; and "independent reviewer agent",
                 carrying a small purple head-and-shoulders-with-tick icon and annotated "a
                 different instance, its own context, read-only, no power to approve or
                 merge". Then a blue head-and-shoulders icon "human owner", annotated "reads
                 the report and the change, and owns the merge", connecting to a "main
                 branch" terminus. Each diamond has a "fail" exit curving back to the author
                 agent, sharing the annotation "back to the author, with the reason". A
                 light grey bracket spans the three diamonds, labelled "cheap mechanical
                 gates first — the expensive one last". Single-weight connectors, one
                 arrowhead style, generous spacing, sentence case.
```

## Figure 7.2 — Notebook versus governed pipeline

```
FIGURE BRIEF
- id:            Figure 7.2
- title:         From exploratory notebook to governed pipeline
- type:          before/after
- claim:         The governed pipeline adds tests, hooks, independent review and human ownership to the same analytical steps, converting a run-once artefact into a repeatable, auditable one.
- standfirst:    Same four steps. The difference is everything around them.
- canvas:        16:9
- elements:      top row "before" — a single grey rounded rectangle "notebook" containing
                 an unordered cluster of small cells (load, regrid, threshold, plot) with
                 one grey arrow "looked reasonable → shared"; bottom row "governed
                 pipeline" — the same four steps as an ordered green tool chain inside a
                 workflow border under version control, feeding an orange "author agent",
                 then the three vermillion gate diamonds and a blue "human owner"
- flow:          top: loose cluster to a single output; bottom: left-to-right ordered chain
                 through gates to human owner, all under version control
- labels:        "notebook", "load", "regrid", "threshold", "plot", "looked reasonable",
                 "governed pipeline", "tests", "hooks", "independent review", "human owner",
                 "version control"
- annotations:   on the notebook cluster, "cells in the order the investigation happened,
                 not the order a reader needs"; on the top row's single arrow, in
                 vermillion, "no independent reader"; on the bottom row's chain, "ordered,
                 named, and under version control"; on the bottom gates, in vermillion,
                 "reader before merge"; a footer line, "the analysis is the same in both
                 rows — only what surrounds it changed"
- caption:       Figure 7.2 — The same four analytical steps, twice. Nothing about the science changes between the rows. What changes is that the steps become ordered and version-controlled, and that three checks and an accountable person now stand between the code and the shared branch. The gap between the rows is a gap in discipline, not in cleverness.
- alt-text:      A two-row before-and-after diagram. The top row, labelled before, shows a single grey box labelled notebook holding an unordered cluster of cells, load, regrid, threshold and plot, in the order the investigation happened rather than the order a reader would need. One grey arrow leaves it labelled looked reasonable, then shared, with a vermillion callout reading no independent reader. The bottom row, labelled governed pipeline, shows the same four steps as an ordered green tool chain under version control, feeding an author agent, then tests, hooks and independent review, then a human owner, with a matching callout reading reader before merge. A note across the bottom reads that the analysis is identical in both rows and only what surrounds it has changed.
- infographic description: A flat vector before-and-after diagram on an off-white
                 background, 16:9, two stacked rows sharing a grammar. Title top-left: "From
                 exploratory notebook to governed pipeline". Standfirst beneath: "Same four
                 steps. The difference is everything around them." Top row labelled
                 "before": a single grey rounded rectangle "notebook" containing four small
                 unaligned cells "load", "regrid", "threshold", "plot", annotated "cells in
                 the order the investigation happened, not the order a reader needs"; one
                 grey arrow leaves it labelled "looked reasonable → shared", with a
                 vermillion callout "no independent reader". Bottom row labelled "governed
                 pipeline": the same four steps drawn as an ordered chain of green tool
                 boxes inside a bordered region labelled "version control", annotated
                 "ordered, named, and under version control"; the chain feeds an orange
                 rounded square "author agent", then three vermillion diamonds "tests",
                 "hooks", "independent review" carrying the callout "reader before merge",
                 then a blue head-and-shoulders icon "human owner". A footer line across the
                 canvas reads "the analysis is the same in both rows — only what surrounds
                 it changed". Generous spacing, single-weight lines, sentence case.
```

## Figure 7.3 — The reviewer sub-agent before human review

```
FIGURE BRIEF
- id:            Figure 7.3
- title:         A separate reviewer agent reads the change before the human does
- type:          sequence
- claim:         Independent review means a different agent instance, with its own context and no stake in the work, reports on the change before the accountable human reviews it.
- standfirst:    It is given the standard, and deliberately not the author's case for the work.
- canvas:        16:9
- elements:      four vertical actor lanes read top-to-bottom — "author agent" (orange),
                 "tests + hooks" (vermillion), "reviewer agent" (purple, reviewer icon),
                 "human owner" (blue); numbered horizontal messages between them
- flow:          top-to-bottom, numbered 1–6: (1) author agent → tests+hooks "submit
                 change"; (2) tests+hooks → author agent "fail — fix", or pass;
                 (3) tests+hooks → reviewer agent "pass: review this"; (4) reviewer agent
                 self-step "read change vs specification"; (5) reviewer agent → human owner
                 "findings report"; (6) human owner "merge — owns decision"
- labels:        "author agent", "tests + hooks", "reviewer agent", "human owner",
                 "submit change", "fail — fix", "pass: review this",
                 "read change vs specification", "findings report", "merge — owns decision"
- annotations:   on the reviewer lane header, "a different instance · its own clean context
                 · read-only · cannot approve"; on step 4, "given the specification, and
                 deliberately not the author agent's reasoning"; on step 5, in vermillion,
                 "advisory — not a gate the agent can open"; on step 6, "reads the report
                 and the change, and answers for the result"; a footnote, "a reviewer that
                 almost never returns a fault is a broken reviewer, not a flawless author"
- caption:       Figure 7.3 — Why the reviewer is a separate instance. It is given the change and the specification, and deliberately not the author agent's reasoning. That way it tests the work against the standard rather than against the case made for it. Its report is advisory: it reaches the human, who reads it alongside the change and owns the merge.
- alt-text:      A four-lane sequence diagram read top to bottom, with lanes for the author agent, tests and hooks, a reviewer agent and the human owner. Step one, the author agent submits the change. Step two, the tests and hooks either fail and return it for fixing, or pass. Step three, on a pass, the change goes to the reviewer agent, whose lane is annotated as a different instance, read-only, with no power to approve. Step four, the reviewer reads the change against the specification rather than against the author's reasoning, which it is deliberately not given. Step five, it returns a findings report, annotated as advisory and not a gate the agent can open. Step six, the human owner reads both the report and the change and merges, owning the decision.
- infographic description: A flat vector sequence diagram on an off-white background, 16:9,
                 four vertical lanes read top to bottom. Title top-left: "A separate
                 reviewer agent reads the change before the human does". Standfirst beneath:
                 "It is given the standard, and deliberately not the author's case for the
                 work." Lane headers left to right: orange rounded square "author agent";
                 vermillion diamond "tests + hooks"; purple head-and-shoulders-with-tick
                 "reviewer agent", annotated beneath "a different instance · its own clean
                 context · read-only · cannot approve"; blue head-and-shoulders "human
                 owner". Numbered horizontal arrows: "1 submit change" from author to
                 tests+hooks; "2 fail — fix" returning to the author; "3 pass: review this"
                 to the reviewer; "4 read change vs specification" as a self-loop in the
                 reviewer lane, annotated "given the specification, and deliberately not the
                 author agent's reasoning"; "5 findings report" to the human owner, with a
                 vermillion annotation "advisory — not a gate the agent can open"; "6 merge
                 — owns decision" in the human lane, annotated "reads the report and the
                 change, and answers for the result". A footnote along the bottom reads "a
                 reviewer that almost never returns a fault is a broken reviewer, not a
                 flawless author". Generous spacing, single-weight lines, sentence case.
```

## Figure 7.4 — How plausible-but-wrong code clears a weak suite

```
FIGURE BRIEF
- id:            Figure 7.4
- title:         A self-tested error passes; an independent test catches it
- type:          failure trace
- claim:         Tests written by the same agent that wrote the code assert the code's actual behaviour, so a plausible error passes; a test written against intended behaviour catches it.
- standfirst:    A green suite tells you the code does what the suite says. Nothing more.
- canvas:        16:9
- elements:      a single top-to-bottom trace: orange "author agent" writes a "regrid step"
                 (green tool box) with a hidden defect (vermillion mark: "lat/lon
                 transposed"); it also writes a "self-derived test" (grey) showing a green
                 pass; below, a branch to an "independent test — conservation check"
                 (vermillion diamond) showing a red fail and a return arrow to the author
                 agent
- flow:          top-to-bottom: author agent → regrid step (defect) → self-derived test
                 (pass, misleading); parallel branch → independent conservation test (fail,
                 correct) → back to author agent
- labels:        "author agent", "regrid step", "lat/lon transposed", "self-derived test",
                 "pass", "independent test — conservation check", "fail", "fix"
- annotations:   on the defect, "the output is still a plausible field of numbers"; on the
                 self-derived test, in vermillion, "asserts what the code does, not what it
                 should — so it passes"; on the independent test, in vermillion, "derived
                 from the specification, not from the output — so it fails, correctly"; on
                 the return arrow, "back to the author, with the failing property named"; a
                 footer, "a green suite confirms the code does what the suite asserts, and
                 says nothing about whether the suite asserts the right thing"
- caption:       Figure 7.4 — How a green test suite hides a real defect. The agent wrote the code and then wrote tests against what the code does, so a transposed coordinate sails through. The conservation check catches it because it was derived from the specification, not from the output. This is the dominant failure of agent-written code, and it is why a passing suite is not evidence on its own.
- alt-text:      A top-to-bottom failure trace. An author agent writes a regrid step carrying a hidden defect, latitude and longitude transposed, marked in vermillion. The same agent also writes a self-derived test, which returns a green pass, with a callout reading that it asserts what the code does rather than what it should, so the defect passes unseen. A parallel branch sends the same code to an independent conservation check, a vermillion diamond derived from the specification rather than from the code, which returns a red fail and sends the work back to the author agent to fix. A note at the foot reads that a green suite confirms only that the code does what the suite asserts, and says nothing about whether the suite asserts the right thing.
- infographic description: A flat vector failure-trace diagram on an off-white background,
                 16:9, read top to bottom. Title top-left: "A self-tested error passes; an
                 independent test catches it". Standfirst beneath: "A green suite tells you
                 the code does what the suite says. Nothing more." At the top an orange
                 rounded square "author agent" with two arrows leaving it. The first reaches
                 a green tool box "regrid step" carrying a small vermillion mark "lat/lon
                 transposed", annotated "the output is still a plausible field of numbers".
                 Beneath it a grey box "self-derived test" showing a green tick "pass", with
                 a vermillion callout "asserts what the code does, not what it should — so
                 it passes". The second arrow branches to a vermillion diamond "independent
                 test — conservation check" showing a red cross "fail", with a vermillion
                 callout "derived from the specification, not from the output — so it fails,
                 correctly", and a return arrow "fix" curving back to the author agent,
                 annotated "back to the author, with the failing property named". A footer
                 line reads "a green suite confirms the code does what the suite asserts,
                 and says nothing about whether the suite asserts the right thing". Generous
                 spacing, single-weight lines, sentence case.
```
