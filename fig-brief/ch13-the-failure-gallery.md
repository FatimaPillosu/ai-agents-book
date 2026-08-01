# Figure briefs — Chapter 13 — The failure gallery

Briefs for the figures of `manuscript/ch13-the-failure-gallery.md`, held here rather than in the chapter so the prose reads clean.
Each brief follows `FIGURES.md` §6. The caption and alt-text in the chapter are generated with the brief and must be changed here and there together.

## Figure 13.1 — A fabricated citation, caught at the resolver

```
FIGURE BRIEF
- id:            Figure 13.1
- title:         A fabricated citation, caught at the resolver
- type:          failure trace
- claim:         A fluent, well-formed citation can correspond to no real work; only an external resolver, not a reader, reliably catches it.
- standfirst:    It looks perfect because the same machinery works whether or not the paper exists.
- canvas:        16:9
- elements:      a left-to-right trace — a human "claim to support" (blue); an "agent
                 drafts citation" square (orange); a "citation string" card (sky blue)
                 shown as a well-formed reference; a "resolver check" gate (vermillion)
                 with a "not found" exit
- flow:          left-to-right: claim → agent drafts → citation string → resolver gate;
                 the "not found" exit loops back labelled "delete, do not repair"
- labels:        "claim to support", "agent drafts citation", "citation string",
                 "resolver check", "not found", "delete, do not repair"
- annotations:   on the citation card, in vermillion, "plausible by construction — right
                 shape, right journal, right year"; on the resolver, "checked against an
                 external bibliographic authority — fluency cannot fool it"; on the loop,
                 "a failing reference is deleted, never repaired into existence"; a
                 footer, "reading cannot catch this: the property that would betray it is
                 exactly what the generating process suppresses"
- caption:       Figure 13.1 — The gallery's most reported failure, and the cheapest to catch. The drafted citation has the right shape, the right journal style and the right year, because the same machinery that makes it well-formed works whether or not the paper exists. Reading cannot catch it. The resolver can, because it is external to the model, and the disposition is deletion: a reference that fails is never repaired into existence.
- alt-text:      A left-to-right failure trace in four steps. A claim needing support goes to an agent, which drafts a citation. The citation string appears as a well-formed reference card tagged in vermillion as plausible by construction: right shape, right journal, right year. It then meets a resolver check against an external bibliographic authority, annotated as external to the model, so fluency cannot fool it. The not-found exit loops back labelled delete, do not repair. A footer reads that reading cannot catch this failure, because the property that would betray the citation is exactly what the generating process suppresses.
- infographic description: A flat vector failure trace, 16:9, off-white background.
                 Title top-left: "A fabricated citation, caught at the resolver".
                 Standfirst: "It looks perfect because the same machinery works whether or
                 not the paper exists." Left to right: a blue human icon "claim to
                 support"; an orange rounded square "agent drafts citation"; a sky-blue
                 card "citation string" drawn as a tidy reference with a vermillion tag
                 "plausible by construction — right shape, right journal, right year"; a
                 vermillion diamond "resolver check" annotated "checked against an
                 external bibliographic authority — fluency cannot fool it". The
                 diamond's "not found" exit curves back to the agent labelled "delete, do
                 not repair", annotated "a failing reference is deleted, never repaired
                 into existence". Footer: "reading cannot catch this: the property that
                 would betray it is exactly what the generating process suppresses".
                 Sentence case throughout.
```

## Figure 13.2 — A silent unit error, made loud

```
FIGURE BRIEF
- id:            Figure 13.2
- title:         A silent unit error, made loud by a range assertion
- type:          failure trace
- claim:         A wrong-by-a-factor quantity is dimensionally invisible; a units-aware step and a range assertion convert a silent error into a halted one.
- standfirst:    Nothing about the number looks wrong. That is the problem.
- canvas:        16:9
- elements:      a top-to-bottom trace — an "agent computes quantity" square (orange); a
                 "number: 42 (no units)" card (sky blue); a "units + range assertion"
                 diamond (vermillion) with an "out of range — halt" exit returning to the
                 agent; a greyed "downstream use" box crossed by a vermillion bar
- flow:          top-to-bottom: agent computes → bare number → units/range gate; halt
                 exit returns to the agent; the grey "downstream use" box is shown
                 unreached
- labels:        "agent computes quantity", "number (no units)",
                 "units + range assertion", "out of range — halt", "downstream use"
- annotations:   on the number card, in vermillion, "wrong by a physical factor — and
                 still a perfectly reasonable-looking value"; on the gate, "does not
                 reason about the science: refuses unlabelled units and impossible
                 values"; on the vermillion bar, "error stopped here — the calibration
                 and the verification never see it"; a footer, "the whole trick is
                 turning a silent failure into a loud one: loud gets caught, silent gets
                 shipped"
- caption:       Figure 13.2 — Nothing about 42 looks wrong. A quantity off by a factor of 25.4 or 3,600 is still a plausible number, which is why no amount of inspection helps. The units-and-range assertion does not understand the science; it simply refuses a value with no declared unit or outside the physical envelope. That refusal is everything: a loud failure gets caught, a silent one gets shipped.
- alt-text:      A top-to-bottom failure trace. An agent computes a quantity and produces a bare number, forty-two, with no units attached, tagged in vermillion as wrong by a physical factor yet looking entirely reasonable. It meets a units and range assertion, which halts it as out of range and returns it to the agent. Below, greyed out and crossed by a vermillion bar, sits the downstream use the error never reached. Annotations note that the assertion does not reason about the science, it just refuses unlabelled or impossible values, and the footer reads that the whole trick is converting a silent failure into a loud one, because a loud failure gets caught and a silent one gets shipped.
- infographic description: A flat vector failure trace, 16:9, off-white background,
                 flowing top to bottom. Title top-left: "A silent unit error, made loud by
                 a range assertion". Standfirst: "Nothing about the number looks wrong.
                 That is the problem." An orange rounded square "agent computes quantity"
                 leads down to a sky-blue card "number: 42 (no units)" with a vermillion
                 tag "wrong by a physical factor — and still a perfectly
                 reasonable-looking value". It leads to a vermillion diamond "units +
                 range assertion", annotated "does not reason about the science: refuses
                 unlabelled units and impossible values". Its "out of range — halt" exit
                 curves back to the agent. Below the diamond, a greyed box "downstream
                 use" crossed by a thick vermillion bar annotated "error stopped here —
                 the calibration and the verification never see it". Footer: "the whole
                 trick is turning a silent failure into a loud one: loud gets caught,
                 silent gets shipped". Sentence case throughout.
```

## Figure 13.3 — Specification drift, caught by re-reading the spec

```
FIGURE BRIEF
- id:            Figure 13.3
- title:         Specification drift, caught against a fixed specification
- type:          failure trace
- claim:         Across turns an agent's target rotates away from the specification while each step looks responsive; only comparison against the fixed, external specification reveals it.
- standfirst:    No single step is wrong. The target moves anyway.
- canvas:        16:9
- elements:      a "specification (fixed, external)" tag (blue) held at the top; a
                 left-to-right chain of three "turn" squares (orange) whose target arrows
                 rotate progressively away; dashed grey reference lines from the
                 specification to each turn; a "compare to spec" gate (vermillion) with a
                 "drift detected" exit to a "human decision" (blue)
- flow:          three turns left-to-right, each with a target arrow pointing further from
                 the fixed specification; the final gate compares the latest output to the
                 specification
- labels:        "specification (fixed, external)", "turn 1", "turn 2", "turn 3",
                 "compare to spec", "drift detected", "human decision"
- annotations:   on turn 1, "a redefinition — looks responsive"; on turn 2, "a relaxed
                 criterion — looks responsive"; on turn 3, "a helpful reinterpretation —
                 looks responsive"; after turn 3, in vermillion, "the target has rotated,
                 and no single step was the wrong one"; on the gate, "judged against the
                 document, not the conversation"; a footer, "drift is divergence from a
                 fixed reference — the check is free when the specification is a real
                 artefact, impossible when it is not"
- caption:       Figure 13.3 — No single turn is the wrong one. Each accommodation looks responsive on its own, and the target rotates anyway, which is why drift is invisible from inside the conversation. The check is the cheapest in the gallery: hold the specification fixed and external, and compare the output to it rather than to the chat. It costs nothing when the specification is a real artefact, and it is impossible when it is not.
- alt-text:      A fixed specification tag sits at the top. Below it, three turns run left to right, each with a small target arrow rotating further away from the specification, with dashed reference lines showing the growing angle. Each turn is annotated as looking individually responsive: a redefinition here, a relaxed criterion there, a helpful reinterpretation. After turn three a vermillion callout reads that the target has rotated and no single step was the wrong one. A compare-to-spec gate then checks the latest output against the fixed document, exits drift detected, and routes to a human decision. The footer reads that drift is defined by divergence from a fixed reference, so the check costs almost nothing when the specification is a real artefact and is impossible when it is not.
- infographic description: A flat vector failure trace, 16:9, off-white background. Title
                 top-left: "Specification drift, caught against a fixed specification".
                 Standfirst: "No single step is wrong. The target moves anyway." A blue
                 tag "specification (fixed, external)" sits centred near the top. Below,
                 three orange rounded squares left to right, "turn 1", "turn 2", "turn 3",
                 each with a short arrow above it rotating further from vertical, and
                 dashed grey lines up to the specification tag showing the widening angle.
                 Annotations beneath: "a redefinition — looks responsive"; "a relaxed
                 criterion — looks responsive"; "a helpful reinterpretation — looks
                 responsive". After turn 3, a vermillion callout "the target has rotated,
                 and no single step was the wrong one". The chain ends at a vermillion
                 diamond "compare to spec", annotated "judged against the document, not
                 the conversation", whose "drift detected" exit leads to a blue human icon
                 "human decision". Footer: "drift is divergence from a fixed reference —
                 the check is free when the specification is a real artefact, impossible
                 when it is not". Sentence case throughout.
```

## Figure 13.4 — Sycophantic review, exposed by engineered independence

```
FIGURE BRIEF
- id:            Figure 13.4
- title:         Sycophantic review, exposed by engineered independence
- type:          failure trace
- claim:         A reviewer that can infer the author's position agrees with it; withholding the conclusion and framing review as defect-search restores real scrutiny.
- standfirst:    Independence is configured, not requested.
- canvas:        16:9
- elements:      two parallel left-to-right traces of the same artefact. Top (failure):
                 "artefact + author conclusion" (blue) feeds "reviewer sees conclusion"
                 (purple), returning "approved" crossed in vermillion. Bottom (fix):
                 "artefact, conclusion withheld" feeds "reviewer: find defects" (purple),
                 returning "defect found"
- flow:          two stacked left-to-right traces sharing the same artefact; the top ends
                 in a vermillion-crossed approval, the bottom in a genuine defect
- labels:        "artefact + author conclusion", "reviewer sees conclusion", "approved",
                 "artefact, conclusion withheld", "reviewer: find defects", "defect found"
- annotations:   on the top reviewer, in vermillion, "it agrees with the position it
                 inferred"; on the crossed approval, "false assurance — worse than no
                 review, because the gap now looks filled"; between the traces, "the only
                 difference: what the reviewer was shown, and what it was asked"; on the
                 bottom reviewer, "criteria only, adversarial brief, no sight of the
                 conclusion"; a footer, "asking it to be tougher does not work — a system
                 disposed to agree will agree about that too"
- caption:       Figure 13.4 — The same artefact, reviewed twice. The only difference between the traces is what the reviewer was shown and what it was asked. Given the author's conclusion and a request to evaluate, it ratifies; given the artefact alone and a brief to find defects, it finds one. Asking the model to be tougher changes nothing, because a system disposed to agree will agree about that too. Independence is configured, not requested.
- alt-text:      Two parallel traces of the same artefact. In the top trace the artefact arrives together with the author's conclusion; the reviewer sees the conclusion and returns approved, shown with a vermillion cross and tagged false assurance, worse than no review, because the gap now looks filled. In the bottom trace the same artefact arrives with the conclusion withheld and the reviewer is briefed to find defects against a checklist rather than to judge acceptability; it returns a genuine defect. The annotation between the traces reads that the only difference is what the reviewer was shown and asked. A footer notes that asking a model to be tougher does not work, because a system disposed to agree will agree about that too.
- infographic description: A flat vector failure trace, 16:9, off-white background, two
                 stacked left-to-right traces. Title top-left: "Sycophantic review,
                 exposed by engineered independence". Standfirst: "Independence is
                 configured, not requested." Top trace: a blue card "artefact + author
                 conclusion" feeds a purple reviewer icon "reviewer sees conclusion",
                 annotated in vermillion "it agrees with the position it inferred",
                 returning a box "approved" struck through with a vermillion cross and
                 tagged "false assurance — worse than no review, because the gap now
                 looks filled". Bottom trace: a blue card "artefact, conclusion withheld"
                 feeds a purple reviewer icon "reviewer: find defects", annotated
                 "criteria only, adversarial brief, no sight of the conclusion",
                 returning a box "defect found" with a plain tick. Between the traces, a
                 centred note: "the only difference: what the reviewer was shown, and
                 what it was asked". Footer: "asking it to be tougher does not work — a
                 system disposed to agree will agree about that too". Sentence case.
```

## Figure 13.5 — Context loss — the dropped constraint and the boundary check that catches it

```
FIGURE BRIEF
- id:            Figure 13.5
- title:         Context loss — the dropped constraint and the boundary check
- type:          failure trace
- claim:         A constraint set early is silently dropped at a context boundary and then contradicted by a confident later output; only a consistency assertion against externalised state catches it.
- standfirst:    The agent cannot miss what it no longer represents.
- canvas:        16:9
- elements:      a left-to-right trace — a "constraint set" card (sky blue) with a branch
                 down to an external "state on record" cylinder (sky blue); an "agent
                 works" square (orange); a vertical dashed grey "context boundary" at
                 which the constraint drops (a faded arrow that does not cross); an
                 "agent continues" square (orange); a "confident output" card; a
                 "consistency assertion vs state" gate (vermillion) exiting
                 "contradiction" to "re-ground and retry"
- flow:          left-to-right: constraint set (branch to state on record) → agent works →
                 context boundary (constraint dropped) → agent continues → confident
                 output → assertion against the record → contradiction → re-ground
- labels:        "constraint set", "state on record", "agent works", "context boundary",
                 "constraint dropped", "agent continues", "confident output",
                 "consistency assertion vs state", "contradiction", "re-ground and retry"
- annotations:   on the branch, "load-bearing facts are written out, not trusted to
                 memory"; at the boundary, in vermillion, "no error raised — the system
                 cannot miss what it no longer represents"; on the confident output,
                 "wrong through a missing premise, not faulty reasoning"; on the gate,
                 "tested against the record, not the conversation"; a footer, "the
                 assertion catches the violation even though the reason for it is
                 invisible"
- caption:       Figure 13.5 — The agent cannot notice what it no longer holds. The constraint fell out at the context boundary without any error, and everything after it is confident reasoning from an incomplete state. The catch happens at the boundary check, where the output is tested against the state on record rather than against the conversation, and the fix is re-grounding. This is why load-bearing facts live in external state, not in the agent's memory.
- alt-text:      A left-to-right trace. A constraint is set early and branches down into an external state-on-record store. The agent works, then crosses a dashed context boundary at which the constraint drops away as a faded arrow that does not cross, with a vermillion callout reading that no error is raised because the system cannot miss what it no longer represents. The agent continues and produces a confident output that contradicts the dropped constraint. A consistency assertion checks the output against the state on record, finds the contradiction, and routes to re-ground and retry. The footer reads that the output was wrong through a missing premise, not faulty reasoning, which is why only a check against externalised state can catch it.
- infographic description: A flat vector failure trace, 16:9, off-white background, left
                 to right. Title top-left: "Context loss — the dropped constraint and the
                 boundary check". Standfirst: "The agent cannot miss what it no longer
                 represents." A sky-blue card "constraint set" with a branch down to a
                 sky-blue cylinder "state on record", the branch annotated "load-bearing
                 facts are written out, not trusted to memory". Then an orange square
                 "agent works", then a vertical dashed grey line "context boundary" where
                 a faded grey arrow labelled "constraint dropped" stops short of
                 crossing, with a vermillion callout "no error raised — the system cannot
                 miss what it no longer represents". Beyond it, an orange square "agent
                 continues" and a card "confident output" annotated "wrong through a
                 missing premise, not faulty reasoning". The output meets a vermillion
                 diamond "consistency assertion vs state", annotated "tested against the
                 record, not the conversation", fed by a line up from the "state on
                 record" cylinder; its "contradiction" exit leads to a box "re-ground and
                 retry". Footer: "the assertion catches the violation even though the
                 reason for it is invisible". Sentence case throughout.
```

## Figure 13.6 — Confident extrapolation, bounded by its support

```
FIGURE BRIEF
- id:            Figure 13.6
- title:         Confident extrapolation, bounded by its support
- type:          failure trace
- claim:         A claim reaching beyond the data's support reads identically to a supported one; only comparing the claim's scope against the evidence's scope catches it.
- standfirst:    Confidence does not drop where the evidence runs out. The comparison has to be mechanical.
- canvas:        16:9
- elements:      a left-to-right trace — a "data + support range" card (sky blue) with a
                 marked support span; an "agent generalises" square (orange); a
                 "confident claim" card (orange) whose scope bar extends past the support
                 span, the overshoot bracketed in vermillion; a "scope vs support" gate
                 (vermillion) with an "out of support" exit to "flag as hypothesis →
                 independent test"
- flow:          left-to-right: data with support range → agent generalises → confident
                 claim (scope exceeds support) → scope-vs-support gate → out-of-support
                 exit to the hypothesis route
- labels:        "data + support range", "agent generalises", "confident claim",
                 "scope vs support", "out of support",
                 "flag as hypothesis → independent test"
- annotations:   on the support span, "the span the evidence actually covers"; on the
                 claim card, in vermillion, "reads identically to a supported claim — the
                 register of confidence does not change at the edge of the evidence"; on
                 the overshoot bracket, "the reach past the data"; on the gate, "compares
                 scopes; never judges plausibility, which is the judgement fluency
                 defeats"; on the exit, "demoted, not deleted"; a footer, "moving it back
                 up takes new evidence, not more assured phrasing"
- caption:       Figure 13.6 — The claim reads the same on both sides of the evidence's edge. That is what makes extrapolation the sharpest form of plausible failure: confidence does not drop where the support runs out. So the gate never judges how convincing the claim sounds; it compares the claim's scope against the evidence's scope. Anything reaching past gets demoted to hypothesis and sent for independent test, not deleted. More assured phrasing never moves it back up. New evidence does.
- alt-text:      A left-to-right trace. A data card shows a marked support range, the span the evidence actually covers. An agent generalises from it and produces a confident claim whose scope bar visibly extends past the support range, with a vermillion bracket marking the overshoot and a callout reading that the claim reads identically to a supported one, because the register of confidence does not change at the edge of the evidence. A scope-versus-support gate compares the two extents, annotated as comparing scopes rather than judging plausibility, which is the judgement fluency defeats. The out-of-support exit routes to a box reading flag as hypothesis, send for independent test, annotated demoted, not deleted. A footer reads that moving a claim back up takes new evidence, not more assured phrasing.
- infographic description: A flat vector failure trace, 16:9, off-white background, left
                 to right. Title top-left: "Confident extrapolation, bounded by its
                 support". Standfirst: "Confidence does not drop where the evidence runs
                 out. The comparison has to be mechanical." A sky-blue card "data +
                 support range" showing a horizontal bar with a marked span, annotated
                 "the span the evidence actually covers". An arrow to an orange square
                 "agent generalises", then to an orange card "confident claim" whose
                 scope bar visibly extends beyond the support span; the overshoot is
                 bracketed in vermillion, labelled "the reach past the data", and the card
                 carries a vermillion callout "reads identically to a supported claim —
                 the register of confidence does not change at the edge of the evidence".
                 The claim meets a vermillion diamond "scope vs support", annotated
                 "compares scopes; never judges plausibility, which is the judgement
                 fluency defeats". Its "out of support" exit leads to a box "flag as
                 hypothesis → independent test", annotated "demoted, not deleted".
                 Footer: "moving it back up takes new evidence, not more assured
                 phrasing". Sentence case throughout.
```
