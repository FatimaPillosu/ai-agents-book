# Figure briefs — Chapter 11 — Verification and evaluation

Briefs for the figures of `manuscript/ch11-verification-and-evaluation.md`, held here rather than in the chapter so the prose reads clean.
Each brief follows `FIGURES.md` §6. The caption and alt-text in the chapter are generated with the brief and must be changed here and there together.

## Figure 11.1 — The six-tier evidential hierarchy

```
FIGURE BRIEF
- id:            Figure 11.1
- title:         Six tiers of evidence for a workflow claim
- type:          architecture (ascending ladder)
- claim:         Evidential strength ascends through six operationally defined tiers, from merely running to surviving adversarial scrutiny, and only the top tier is named for its checker rather than for its check.
- standfirst:    A claim holds the highest tier it actually passed — not the one you hoped for.
- canvas:        16:9
- elements:      six stacked horizontal bars forming a ladder, lowest at the bottom, each
                 labelled with a tier name and its establishing check; the fifth bar
                 carrying a green tool glyph beside a small sky-blue cylinder for the
                 second method and its data; the topmost bar bordered in reviewer purple
                 and carrying the reviewer icon; each tier carrying a small vermillion
                 gate diamond at its right edge; an upward arrow beside the ladder
- flow:          bottom-to-top — tier 1 at the base rising to tier 6 at the top
- labels:        "1 · execution — runs, output well-formed",
                 "2 · internal consistency — invariants hold",
                 "3 · reproduces held-out truth — split-sample test",
                 "4 · out-of-sample generalisation — differential test",
                 "5 · independent-method corroboration — a second method with a different
                 error structure agrees",
                 "6 · adversarial scrutiny — a competent party tries to break it and fails",
                 "increasing evidential strength"
- annotations:   bracket spanning tiers 1–2, "necessary — and almost worthless alone"; on
                 tier 3, "the first tier where the word correct is earned"; bracket
                 spanning tiers 3–6, "correctness earned here"; on tier 5, "changes the
                 measurement chain, not just the regime"; on tier 6, "cannot be automated
                 — judgement does the certifying"; a second callout on tier 6, "the only
                 tier named for the checker, not the check — its strength is a measured
                 quantity (§11.5)"; a footer, "the tiers are cumulative: a tier-5 claim
                 has passed 1 to 5"
- caption:       Figure 11.1 — The ladder every claim in this book is measured against. The two bottom tiers are cheap, catch the crude failures, and can both be passed by an output that is wrong; correct is a word that gets earned at tier three, against data the workflow never saw. Tier five is what this discipline has relied on for decades, a second method whose errors are unrelated to the first one's, and tier six is the odd one, named for its checker rather than its check. A claim holds the tier it passed, not the tier you intended.
- alt-text:      Six horizontal bars stacked as a ladder, read bottom to top, each naming a tier and the check that establishes it. Tier one, execution: it runs and the output is well-formed. Tier two, internal consistency: the invariants hold. Tier three, reproduces held-out truth by a split-sample test, marked as the first tier where the word correct is earned. Tier four, out-of-sample generalisation by a differential test. Tier five, independent-method corroboration, where a second method with a different error structure agrees, annotated that this changes the measurement chain and not just the regime, and carrying a green tool glyph beside a sky-blue cylinder for the second method and its data. Tier six, adversarial scrutiny, where a competent party tries to break the claim and fails, carried in reviewer purple with the reviewer icon, annotated both that it cannot be automated because judgement does the certifying and that it is the only tier named for the checker rather than the check, its strength being a measured quantity treated in section 11.5. A bracket spans tiers one and two, labelled necessary but almost worthless alone; another spans three to six, labelled correctness earned here. An arrow up the side reads increasing evidential strength, and a footer reads that the tiers are cumulative, so a tier-five claim has passed one to five.
- infographic description: A flat vector ladder diagram, 16:9, off-white background.
                 Title top-left: "Six tiers of evidence for a workflow claim".
                 Standfirst: "A claim holds the highest tier it actually passed — not the
                 one you hoped for." Six horizontal bars stacked bottom to top, equal
                 width, each with a small vermillion diamond at its right edge. From the
                 bottom: "1 · execution — runs, output well-formed"; "2 · internal
                 consistency — invariants hold"; "3 · reproduces held-out truth —
                 split-sample test", annotated "the first tier where the word correct is
                 earned"; "4 · out-of-sample generalisation — differential test"; "5 ·
                 independent-method corroboration — a second method with a different error
                 structure agrees", carrying a small green wrench glyph beside a small
                 sky-blue cylinder at its left edge and annotated "changes the measurement
                 chain, not just the regime"; "6 · adversarial scrutiny — a competent party
                 tries to break it and fails", bordered purple with a reviewer icon,
                 annotated "cannot be automated — judgement does the certifying" and
                 carrying a second callout in a pale yellow fill reading "the only tier
                 named for the checker, not the check — its strength is a measured
                 quantity (§11.5)". A vertical arrow to the left of the ladder labelled
                 "increasing evidential strength". A bracket to the right spans tiers 1–2,
                 "necessary — and almost worthless alone"; another spans tiers 3–6,
                 "correctness earned here". Footer: "the tiers are cumulative: a tier-5
                 claim has passed 1 to 5". Sentence case throughout. This canvas sits at
                 the density ceiling of `FIGURES.md` §2, so if it crowds, drop the tier-1
                 and tier-2 annotations first and the tier-3 annotation next; the tier-5
                 and tier-6 annotations carry the argument and are never dropped, because
                 legibility wins over density.
```

## Figure 11.2 — Building a task-grounded evaluation set

```
FIGURE BRIEF
- id:            Figure 11.2
- title:         An evaluation set built from the workflow's own history
- type:          architecture
- claim:         A task-grounded evaluation set is assembled from the workflow's own history through harvest, curate, stratify, hold out and version, and then feeds the tiered checks.
- standfirst:    The raw material is already in your history. The work is gathering and disciplining it.
- canvas:        16:9
- elements:      left, four sky-blue cylinders — "settled past runs", "manual-workflow
                 outputs", "failure log (Ch.13)", "known-correct hold-back"; a grey
                 "curate" step; a grey "stratify" step; a sky-blue "stratified evaluation
                 set" cylinder with a marked "held-out slice"; a "version + refresh" loop;
                 a vermillion "gate" before a "live workflow" box
- flow:          left-to-right — four sources → curate → stratify → versioned set (with a
                 held-out slice) → gate → live workflow; a loop arrow returns from the set
                 to "version + refresh"
- labels:        "settled past runs", "manual-workflow outputs", "failure log (Ch.13)",
                 "known-correct hold-back", "curate", "stratify by task and regime",
                 "stratified evaluation set", "held-out slice", "version + refresh",
                 "gate", "live workflow"
- annotations:   on curate, "each case: input · reference · metric fixed in advance ·
                 provenance of the reference"; on stratify, "spans the regimes the
                 workflow will actually meet — easy cases cannot certify it"; on the
                 held-out slice, in vermillion, "withheld means absent from anything the
                 model could have seen (§11.3)"; on the gate, "the gate §11.5 measures";
                 on the loop, "refresh on model, prompt or data-regime change"
- caption:       Figure 11.2 — You already own the raw material for an evaluation set. Settled runs, the outputs of the manual workflow the agent replaced, your failure log and a held-back set of known answers get curated into cases, then versioned. They are stratified across regimes, so the easy ones cannot certify the set. The held-out slice carries the warning that matters: withheld means absent from everything the model could have seen.
- alt-text:      A left-to-right assembly line. Four source cylinders, settled past runs, manual-workflow outputs, the failure log and a known-correct hold-back, feed a curate step, annotated that each case gets an input, a reference, a metric fixed in advance and the provenance of that reference. A stratify step follows, annotated as spanning the regimes the workflow will actually meet, then a versioned evaluation set with a held-out slice, annotated with the contamination warning that the reference must be absent from anything the model could have seen. The set feeds a gate in front of the live workflow, annotated that this is the gate whose false-negative rate section 11.5 measures. A loop arrow returns to version and refresh, annotated with the re-measurement triggers.
- infographic description: A flat vector pipeline diagram, 16:9, off-white background.
                 Title top-left: "An evaluation set built from the workflow's own
                 history". Standfirst: "The raw material is already in your history. The
                 work is gathering and disciplining it." At the left, four sky-blue
                 cylinders stacked: "settled past runs", "manual-workflow outputs",
                 "failure log (Ch.13)", "known-correct hold-back". Arrows converge on a
                 grey rounded rectangle "curate", annotated "each case: input · reference
                 · metric fixed in advance · provenance of the reference". Then a grey
                 rounded rectangle "stratify by task and regime", annotated "spans the
                 regimes the workflow will actually meet — easy cases cannot certify it".
                 Then a sky-blue cylinder "stratified evaluation set" with a hatched band
                 "held-out slice" carrying a vermillion annotation "withheld means absent
                 from anything the model could have seen (§11.3)". A loop arrow returns
                 above it to a tag "version + refresh", annotated "refresh on model,
                 prompt or data-regime change". The set feeds a vermillion diamond "gate",
                 annotated "the gate §11.5 measures", then a box "live workflow".
                 Sentence case throughout.
```

## Figure 11.3 — Measuring a gate by seeded defects

```
FIGURE BRIEF
- id:            Figure 11.3
- title:         Seeded-defect measurement of a verification gate
- type:          sequence
- claim:         A gate's false-negative rate is measured by seeding known defects into sound inputs, running the gate blind, tallying catches and misses, and reporting a rate with its uncertainty.
- standfirst:    The only way to know an alarm works is a controlled fire.
- canvas:        16:9
- elements:      three actors as lanes — a human (blue) who seeds faults; the gate under
                 test (vermillion diamond); a tally record (sky-blue cylinder); five
                 numbered steps crossing between them
- flow:          top-to-bottom, numbered — (1) human plants known faults of named classes
                 into sound inputs; (2) inputs run through the gate blind; (3) gate
                 returns pass/fail per input; (4) tally records catches and misses by
                 class; (5) rate reported with an interval
- labels:        "seed known faults — fabricated citation · unit slip · out-of-range ·
                 dropped constraint", "run gate blind", "pass / fail per input",
                 "tally catches & misses by class", "report rate + interval",
                 "re-measure on: model change · prompt change · data-regime change ·
                 calendar"
- annotations:   on step 1, "stratified by class — a gate can be strong on one and blind
                 to another"; on step 2, "the gate is not told where the faults are"; on
                 step 4, in vermillion, "a never-firing gate is a broken gate, not a clean
                 corpus"; on step 5, "zero misses in twenty trials still means the true
                 miss rate could be ~15%"; a footer with the re-measurement triggers
- caption:       Figure 11.3 — Calibrating the gate like the instrument it is. You plant faults you know about, run the gate blind, and count what it misses, class by class. The two honesty rules are on the canvas. A clean sweep on twenty seeded faults still leaves a possible miss rate near fifteen percent. A gate that never fires on real work is evidence of a broken gate, not of flawless upstream work.
- alt-text:      A five-step measurement sequence. Step one, a person seeds known faults into sound inputs, listing the classes: a fabricated citation, a unit slip, an out-of-range value, a dropped constraint, annotated stratified by class because a gate can be strong on one and blind to another. Step two, the inputs run through the gate blind. Step three, the gate returns pass or fail per input. Step four, a tally records catches and misses by class, with a vermillion note that a gate which never fires on live work is a broken gate, not a clean corpus. Step five, the rate is reported with its uncertainty, annotated that zero misses in twenty trials still means the true miss rate could be about fifteen percent. A footer lists the re-measurement triggers: any model change, any prompt change, any data-regime change, and a calendar.
- infographic description: A flat vector sequence diagram, 16:9, off-white background.
                 Title top-left: "Seeded-defect measurement of a verification gate".
                 Standfirst: "The only way to know an alarm works is a controlled fire."
                 Three lane headers: blue human "scientist", vermillion diamond "gate
                 under test", sky-blue cylinder "tally". Five numbered steps top to
                 bottom, each an arrow with its annotation beneath: "1 seed known faults —
                 fabricated citation · unit slip · out-of-range · dropped constraint" /
                 "stratified by class — a gate can be strong on one and blind to another";
                 "2 run gate blind" / "the gate is not told where the faults are"; "3 pass
                 / fail per input"; "4 tally catches & misses by class" with a vermillion
                 note "a never-firing gate is a broken gate, not a clean corpus"; "5
                 report rate + interval" / "zero misses in twenty trials still means the
                 true miss rate could be ~15%". Footer: "re-measure on: model change ·
                 prompt change · data-regime change · calendar". Sentence case.
```
