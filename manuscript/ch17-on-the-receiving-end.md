# Chapter 17 — On the receiving end

**[AUTHOR: confirm the chapter title. The alternative on record, not chosen by the integration plan, is "Reviewing work you did not produce".]**

> **Status:** draft r2 · voice v5.0 (`STYLE.md` §1) · sentence-per-line per `STYLE.md` §10 · figures as briefs per `FIGURES.md`.
> **Conventions:** vendor-neutral (outline §9) · **[AUTHOR: …]** marks lived material only the author can supply · **[verify]** marks real but unconfirmed details · citations drawn only from verified reports in `/research`. Nothing has been invented.
> The questions and checklists here are proposals for practice, not a report of established practice; no claim is made that any community currently asks these questions.

---

## 17.1 The reader without the specification

A manuscript arrives for review.
Its methods section says the station records were quality-controlled by an agentic workflow, and then it moves on.
No specification is named, no checks are described, and nothing states what the workflow was permitted to change.
The paper's central result rests on those records.
You have to decide what to write, and nothing in this book has been addressed to you yet.

Every chapter so far has spoken to the accountable principal.
That reader writes the specification, sets the gates, chooses which tier a claim needs and owns the record afterwards.
Four positions take that authority away, and none of them is unusual.
You review a manuscript somebody else produced with agents.
You inherit a pipeline whose specification you did not write, and quite possibly nobody did.
Your institution hands you a system and expects the group to use it.
A supplied product arrives with agentic components inside it, described by a datasheet you cannot audit.

What those four share is a limit on what you control.
You cannot change the workflow, and frequently you cannot see it.
What you can decide is how much of its output to believe, and sometimes whether it gets used at all.
Those are narrower powers than the rest of the book assumes, and they are not small ones.
A reviewer who declines to accept a claim whose support cannot be shown is exercising the strongest correction the research community has.

The apparatus transfers, which is the part worth noticing.
Chapter 12 tells a producer to keep four records: an assumption registry, an uncertainty registry, an audit trail and a reviewer-coverage record.
Those are exactly the records a receiver should be asking to see.
Chapter 11's tiers give you a vocabulary for how strong the evidence behind a claim is.
Its gate calibration gives you a second one, for whether the checks behind that evidence were ever measured.
So none of the questions below asks for a record the book has not already specified.
They are the book's own producer-side apparatus, read from the other end.

§17.2 takes the reviewer's position, which is the sharpest of the four and the one every reader already occupies.
§17.3 sorts Chapter 13's six failure modes by whether a reviewer can catch them from outside.
§17.4 and §17.5 take the inherited workflow and the supplied system.
§17.6 is a checklist written for the receiver rather than the producer.

## 17.2 Reviewing a manuscript produced with agents

"AI was used for language editing."
That sentence satisfies most venues and tells a reviewer nothing.
Chapter 9 defines what a disclosure statement is for: which tool did which task, on what, and under whose oversight.
Most of what you will read falls short of that, and usually not through evasion.
Authors write to the threshold their venue sets, and those thresholds are drawn for integrity rather than for review.
One major publisher's 2026 policy asks that any substantive change to a text's structure or content be declared, naming the tool and its purpose.
Routine grammar checking is exempt (Elsevier, 2026; a policy page, with specifics volatile per the repository rule).
That threshold answers whether a tool was used.
It does not answer whether the work the tool did was checked.

So the disclosure is where a review of agentic work starts, not where it finishes.
You read it; you do not have to ask for it.
Five things are worth asking for after it, and they escalate in what they cost the authors to supply.
First, the specification the agentic step ran under.
It establishes what the workflow was asked to do, which is the only thing against which "it worked" carries meaning.
A group practising the discipline of Chapter 3 already has the document written.
Second, the gates the output passed and what each one checks.
That establishes which failure classes were designed against, and it costs the authors a paragraph they should be able to write from memory.
Third, whether any gate's false-negative rate has been measured.
This is the first genuinely demanding request, because most groups have never measured one, and an honest "no" is itself informative.
Chapter 11 §11.5 gives the method, and says how little a clean sweep on twenty seeded defects licenses.

The last two requests are the ones that decide what a result is worth.
Fourth, the evidential tier claimed, and the specific check said to establish it.
Naming a tier is a factual statement about evidence gathered, so a tier with no named check behind it is an assertion rather than a claim (Chapter 11 §11.2).
Ask this alongside the third request, the measured false-negative rate, because a tier is only as strong as the check establishing it (Chapter 11 §11.7).
Fifth, reviewer coverage, meaning which parts had an independent check and which rest on author inspection alone.
That is the most demanding of the five, since a group without a coverage record cannot reconstruct one afterwards (Chapter 12 §12.4).
The order matters as much as the list.
A reviewer who opens with the fifth request gets a defensive author and no information.

One question sits underneath all five, and it is the one I would ask if I could ask only one.
It is not "did you use AI?" but "what would have caught it if this step had been wrong?"
The first question sorts papers into two groups and tells you nothing about either, because the answer is now yes almost everywhere.
The second asks for the mechanism, and each of the five requests above is a way of making it answerable.
An author who can answer it has a governed workflow, whatever they built it with.
An author who cannot has an ungoverned one, and the answer would have been just as damning in 1995 about a hand-written script.

Your own reading of the manuscript is a weaker check than it feels.
An audit of one elite machine-learning venue found 100 fabricated citations across 53 papers accepted there in 2025.
Each of those papers had passed three to five expert reviewers (Ansari, 2026; a single-venue, single-year figure, and itself an unreviewed preprint).
Those reviewers were competent, and they were reading for plausibility, which is exactly the property a fabricated citation has.
A plausibility read is defeated by construction (Chapter 1, on fluency uncorrelated with correctness).
So what a reviewer adds against agentic failure is mechanical checking and provenance questions, not a closer read (high confidence).

Three requests sit outside a reviewer's entitlement, and the reasons matter more than the rule.
The transcript is the first.
A conversation log records what was said rather than what happened.
An agent asked to account for its own reasoning produces a plausible narrative that need not match the run.
Chapter 12 §12.2 sets out why a self-summary is an input to review and never a substitute for it.
The prompts are the second, and they are frequently a group's accumulated working method rather than a disclosure item.
A re-run is the third, and it is the one most often asked in good faith and still wrong.
The same specification and inputs can return different work on a second run, and the model behind a published result may since have been withdrawn.
Chapter 12 §12.4 explains why that leaves agentic work auditable rather than reproducible.
So a re-run asks for a property this kind of work does not have.
Auditability is the property it does have, and the five requests are how you establish it.

Whether you may use an agent whilst reviewing is a separate question and not this section's.
Chapter 9 §9.4 sets out the three policy classes it falls into.
Some funders prohibit the use outright on confidentiality grounds, because a manuscript under review must not enter a service whose onward data handling the reviewer cannot control (NIH, 2023).
That question governs your conduct, and this section governs the work in front of you.

How far to push depends on what rests on the claim, which is the tier-and-stakes matching of Chapter 11 §11.7 applied from outside.
A reviewer demanding gate-calibration records for an exploratory triage makes the same error as a workflow stopping at Tier 2 for a published result.
Both spend verification effort out of proportion to consequence, in opposite directions.
Where a paper's central result rests on an agentic quality-control pass, the whole sequence is proportionate and I would work through all of it.
Where an agent tidied the reference formatting, the disclosure statement is the whole of the review's business with it.

**[AUTHOR: what you have actually asked for, or wished you could ask for, as a reviewer of a manuscript with agentic components, and whether any editor would have backed you.]**

**Figure 17.1 — What a reviewer may ask for, and what they may not.**

![A sequence diagram with two lanes read top to bottom. The left lane is a purple reviewer, the right lane the blue authors. At the top, outside the numbered sequence, a grey band reads: read the disclosure statement first, it is not something you ask for, and it usually answers only whether a tool was used. Five numbered requests then cross from reviewer to authors, each with a return arrow saying what it establishes. Request one, the specification the agentic step ran under, is annotated that it establishes what the workflow was asked to do and that a governed group already has the document. Request two, the gates it passed and what each checks, is annotated that it establishes which failure classes were designed against and costs the authors a paragraph. Request three, whether any gate's false-negative rate has been measured, is annotated that it establishes whether the checks were ever calibrated and that an honest no is informative. Request four, the evidential tier claimed and the check said to establish it, is annotated that it establishes how strong the evidence is and that it is asked alongside request three. Request five, reviewer coverage, is annotated that it establishes what was independently checked and what rests on author inspection, and that it cannot be reconstructed after the fact. A thin vertical wedge runs down the left edge of the reviewer lane, widening from the first request to the fifth, labelled at its foot escalating cost to the authors. A vermillion side-panel headed not a reviewer's to demand lists three items with a reason each: the transcript, because it records what was said rather than what happened; the prompts, because they are the group's working method; and a re-run, because the model behind the result may be gone. A footer reads that the depth of scrutiny matches what rests on the claim.](../figures/figure-17-1.svg)

*Figure 17.1 — Five requests, in the order that gets them answered, with the disclosure above the count because you read it rather than ask for it. Each request buys a different piece of evidence and costs the authors a different amount, so opening with the most expensive is how a review turns into a standoff. The vermillion panel is the half reviewers get wrong: a transcript is not evidence of what happened, and a re-run asks for a property agentic work does not have. (Rendered as `figures/figure-17-1.svg` from the brief below, per `FIGURES.md`.)*

```
FIGURE BRIEF
- id:            Figure 17.1
- title:         What a reviewer may ask for, and what they may not
- type:          sequence
- claim:         A reviewer's five requests escalate, and each one establishes something specific at a specific cost to the authors, with the disclosure read first rather than asked for.
- standfirst:    Each request buys a different piece of evidence and costs the authors a different amount.
- canvas:        16:9
- elements:      two lanes running top to bottom — left, a reddish-purple
                 head-and-shoulders-with-tick icon "reviewer"; right, a blue
                 head-and-shoulders icon "authors"; above the numbered sequence, a grey
                 unnumbered band across both lanes headed "read first, not asked for";
                 five numbered request arrows crossing left to right, each paired with a
                 return arrow carrying what it establishes; a vermillion-bordered
                 side-panel down the right margin headed "not a reviewer's to demand",
                 holding three entries each with a one-line reason; a footer strip across
                 the foot
- flow:          top-to-bottom, opening on the unnumbered disclosure band, then five
                 numbered steps; each step is an arrow from the reviewer lane to the
                 authors lane carrying the request, answered by a return arrow carrying
                 what it establishes; the cost to the authors is annotated beside each
                 step; the side-panel sits outside the two lanes and connects to nothing
- labels:        "reviewer", "authors", "read first, not asked for — the disclosure
                 statement", "1 · the specification the agentic step ran under", "2 · the
                 gates it passed, and what each checks", "3 · has any gate's false-negative
                 rate been measured?", "4 · the tier claimed, and the check said to
                 establish it", "5 · reviewer coverage", "not a reviewer's to demand",
                 "the transcript", "the prompts", "a re-run"
- annotations:   on the disclosure band, "already written, so it costs nothing — and it
                 usually answers only whether a tool was used"; on step 1, "establishes
                 what the workflow was asked to do; a governed group already has the
                 document"; on step 2, "establishes which failure classes were designed
                 against; costs a paragraph"; on step 3, "establishes whether the checks
                 were ever calibrated; an honest 'no' is informative"; on step 4,
                 "establishes how strong the evidence is; asked alongside step 3"; on step
                 5, "establishes what was independently checked and what rests on author
                 inspection; cannot be reconstructed afterwards"; inside the side-panel,
                 one line against each entry, "records what was said, not what happened",
                 "the group's working method", "the model behind it may be gone"; footer,
                 "depth of scrutiny matches what rests on the claim"
- caption:       Figure 17.1 — Five requests, in the order that gets them answered, with the disclosure above the count because you read it rather than ask for it. Each request buys a different piece of evidence and costs the authors a different amount, so opening with the most expensive is how a review turns into a standoff. The vermillion panel is the half reviewers get wrong: a transcript is not evidence of what happened, and a re-run asks for a property agentic work does not have.
- alt-text:      A sequence diagram with two lanes read top to bottom. The left lane is a purple reviewer, the right lane the blue authors. At the top, outside the numbered sequence, a grey band reads: read the disclosure statement first, it is not something you ask for, and it usually answers only whether a tool was used. Five numbered requests then cross from reviewer to authors, each with a return arrow saying what it establishes. Request one, the specification the agentic step ran under, is annotated that it establishes what the workflow was asked to do and that a governed group already has the document. Request two, the gates it passed and what each checks, is annotated that it establishes which failure classes were designed against and costs the authors a paragraph. Request three, whether any gate's false-negative rate has been measured, is annotated that it establishes whether the checks were ever calibrated and that an honest no is informative. Request four, the evidential tier claimed and the check said to establish it, is annotated that it establishes how strong the evidence is and that it is asked alongside request three. Request five, reviewer coverage, is annotated that it establishes what was independently checked and what rests on author inspection, and that it cannot be reconstructed after the fact. A thin vertical wedge runs down the left edge of the reviewer lane, widening from the first request to the fifth, labelled at its foot escalating cost to the authors. A vermillion side-panel headed not a reviewer's to demand lists three items with a reason each: the transcript, because it records what was said rather than what happened; the prompts, because they are the group's working method; and a re-run, because the model behind the result may be gone. A footer reads that the depth of scrutiny matches what rests on the claim.
- infographic description: A flat vector sequence diagram, 16:9, off-white background.
                 Title top-left in the largest size: "What a reviewer may ask for, and what
                 they may not". Standfirst beneath: "Each request buys a different piece of
                 evidence and costs the authors a different amount." Two vertical lanes
                 occupy the left two-thirds of the canvas. Left lane header: a reddish-purple
                 (#CC79A7) head-and-shoulders icon with a small tick, labelled "reviewer".
                 Right lane header: a blue (#0072B2) head-and-shoulders icon, labelled
                 "authors". Above the numbered sequence, a grey (#999999) band spans both
                 lanes, headed "read first, not asked for — the disclosure statement" and
                 annotated beneath in small type "already written, so it costs nothing — and
                 it usually answers only whether a tool was used"; the band carries no
                 number and no arrow. Five numbered horizontal arrows then run from the
                 reviewer lane to the authors lane, evenly spaced top to bottom, each
                 labelled in sentence case: "1 · the specification the agentic step ran
                 under", "2 · the gates it passed, and what each checks", "3 · has any
                 gate's false-negative rate been measured?", "4 · the tier claimed, and the
                 check said to establish it", "5 · reviewer coverage". Each is paired
                 with a thinner return arrow beneath it, running right to left, unlabelled
                 except by the annotation set in small type immediately below the pair, in
                 order: "establishes what the workflow was asked to do; a
                 governed group already has the document"; "establishes which failure classes
                 were designed against; costs a paragraph"; "establishes whether the checks
                 were ever calibrated; an honest 'no' is informative";
                 "establishes how strong the evidence is; asked alongside step 3";
                 "establishes what was independently checked and what rests on author
                 inspection; cannot be reconstructed afterwards". A thin vertical wedge along
                 the left edge of the reviewer lane widens downwards, labelled at its foot
                 "escalating cost to the authors". Down the right third of the canvas sits a
                 vermillion-bordered (#D55E00) panel headed "not a reviewer's to demand",
                 holding three stacked entries, each a short label with a smaller reason
                 beneath it: "the transcript" / "records what was said, not what happened";
                 "the prompts" / "the group's working method"; "a re-run" / "the model behind
                 it may be gone". The panel connects to nothing and has no arrows. A footer
                 strip across the foot of the canvas reads: "depth of scrutiny matches what
                 rests on the claim". Single-weight connectors, one arrowhead style,
                 right-angle corners, generous margins, all text in sentence case.
```

## 17.3 What is detectable from outside, and what is not

A fabricated citation is the one failure in this book a reviewer can settle mechanically, alone, in about a minute.
You resolve every DOI in the reference list, then check that each quoted passage says what the sentence claims it says.
It is the cheapest check available to a reviewer and the one most likely to find something, given how often this mode appears (Chapter 13 §13.2).
The other five modes are not like that, and the difference decides what a review of agentic work can be.

Two of the six are catchable from outside.
Fabricated citations are the first, by resolution.
Confident extrapolation is the second, and the check is to compare the scope of the claim to the scope of the evidence.
That means the range the data actually covered, the domain the relationship was fitted on, and the regime the result is now applied to.
That comparison is an ordinary reviewing skill and it needs no provenance at all.
What it does need is the ranges to be reported, which is itself a thing to ask for when they are missing.

Two are catchable only from the record.
Specification drift is the slow divergence between what a workflow ended up doing and what it was first asked to do.
The check for it is the original specification, held fixed and re-read (Chapter 13 §13.4).
A reviewer who cannot see the specification cannot see it move.
Context loss is the same shape: the check is a consistency assertion against externalised state, and a reviewer has neither the state nor the assertion (Chapter 13 §13.6).
For both, the finished artefact looks entirely coherent, because each was produced by reasoning that was locally sound and globally aimed at the wrong target.

Two are effectively undetectable from outside.
A silent unit error occasionally announces itself when an invariant is checkable from the reported numbers.
A total that will not reconcile with its parts is one such invariant; a flux and an accumulation that cannot both be right is another.
Often no such invariant is reported, and a number wrong by a physical factor sits inside the plausible range for the quantity (Chapter 13 §13.3).
Over-agreeable review leaves no external trace whatsoever.
A rubber-stamp review produces the same record as a searching one (Chapter 12 §12.4), and from outside the group there is not even a record to compare.

So the six sort three ways: two are within an unaided reviewer's reach, two more need the record, and two are beyond reach either way.
That is the argument for §17.2's requests, and it is why they are the substance of a review rather than its paperwork.
A reviewer working from the manuscript alone is covering a third of the gallery.
Another third comes into reach only if the authors kept the record and will show it.
The last third stays outside a review altogether, which is worth naming in an assessment rather than leaving to be assumed away.
So a review's reach is set by what the authors kept (high confidence; the sort is a reading of Chapter 13's own checks rather than a measured detection rate).

One consequence is uncomfortable and worth stating.
The reviewer is the mechanism the community relies on to catch what a group's own gates missed.
Reviewers can reach for the same instruments the authors did, checking an agentic manuscript with an agent built on the same base model.
The two errors then correlate, and the second check adds nothing.
That is the field-scale failure of Chapter 13 §13.9, arriving at the point where it does the most damage.

**Figure 17.2 — What a reviewer can catch, and what needs the record.**

![A sort of six failure modes into three horizontal bands, strongest detectability at the top. The top band, catchable by a check the reviewer can run, is marked with a green tool glyph and holds two rows. Fabricated citations is annotated: resolve every DOI, the reviewer's cheapest action. Confident extrapolation is annotated: compare the scope of the claim to the scope of the evidence. The middle band, catchable only from the record, is marked with a sky-blue cylinder and holds two rows. Specification drift is annotated: the check is the original specification, held fixed and re-read. Context loss is annotated: the check is an assertion against state the reviewer cannot see. The bottom band, beyond reach with or without the record, is marked in grey and holds two rows. Silent unit errors is annotated: only if an invariant is checkable from the reported numbers. Over-agreeable review is annotated: leaves no external trace at all. A vermillion bracket runs down the left of the middle band alone, labelled two of six need the record, with a note beneath the bottom band that two more are beyond reach either way. A footer carries the question: what would have caught it if this step had been wrong?](../figures/figure-17-2.svg)

*Figure 17.2 — Six failure modes, sorted by what it takes to catch them from outside. Two are within reach of a reviewer holding nothing but the manuscript, two more come into reach only if the authors kept the record, and two stay outside a review either way. That sort is the whole argument for asking about provenance, and the honest half of it is that the bottom band is not fixed by asking. (Rendered as `figures/figure-17-2.svg` from the brief below, per `FIGURES.md`.)*

```
FIGURE BRIEF
- id:            Figure 17.2
- title:         What a reviewer can catch, and what needs the record
- type:          architecture
- claim:         Chapter 13's six failure modes sort three ways from outside: two a reviewer can check unaided, two need the workflow's record, and two are beyond reach either way.
- standfirst:    Two of the six can be caught from the manuscript alone.
- canvas:        16:9
- elements:      three stacked horizontal bands, each with a heading and a marker — top
                 band "catchable by a check the reviewer can run" with a green tool glyph;
                 middle band "catchable only from the record" with a sky-blue cylinder;
                 bottom band "beyond reach, with or without the record" with a grey dash;
                 two labelled rows inside each band, six rows in all, each carrying one
                 annotation; a vermillion bracket down the left edge of the middle band
                 only; a footer strip across the foot
- flow:          no flow; a static sort in three bands read top to bottom, with
                 detectability decreasing downwards. No arrows anywhere on the canvas
- labels:        "catchable by a check the reviewer can run", "catchable only from the
                 record", "beyond reach, with or without the record", "fabricated
                 citations", "confident extrapolation", "specification drift", "context
                 loss", "silent unit errors", "over-agreeable review", "two of six need the
                 record"
- annotations:   on "fabricated citations", "resolve every DOI — the reviewer's cheapest
                 action"; on "confident extrapolation", "compare the scope of the claim to
                 the scope of the evidence"; on "specification drift", "the check is the
                 original specification, held fixed and re-read"; on "context loss", "the
                 check is an assertion against state the reviewer cannot see"; on "silent
                 unit errors", "only if an invariant is checkable from the reported
                 numbers"; on "over-agreeable review", "leaves no external trace at all";
                 beneath the bottom band, "two more are beyond reach either way — say so in
                 the assessment"
- caption:       Figure 17.2 — Six failure modes, sorted by what it takes to catch them from outside. Two are within reach of a reviewer holding nothing but the manuscript, two more come into reach only if the authors kept the record, and two stay outside a review either way. That sort is the whole argument for asking about provenance, and the honest half of it is that the bottom band is not fixed by asking.
- alt-text:      A sort of six failure modes into three horizontal bands, strongest detectability at the top. The top band, catchable by a check the reviewer can run, is marked with a green tool glyph and holds two rows. Fabricated citations is annotated: resolve every DOI, the reviewer's cheapest action. Confident extrapolation is annotated: compare the scope of the claim to the scope of the evidence. The middle band, catchable only from the record, is marked with a sky-blue cylinder and holds two rows. Specification drift is annotated: the check is the original specification, held fixed and re-read. Context loss is annotated: the check is an assertion against state the reviewer cannot see. The bottom band, beyond reach with or without the record, is marked in grey and holds two rows. Silent unit errors is annotated: only if an invariant is checkable from the reported numbers. Over-agreeable review is annotated: leaves no external trace at all. A vermillion bracket runs down the left of the middle band alone, labelled two of six need the record, and a note beneath the bottom band reads that two more are beyond reach either way and should be said so in the assessment. A footer carries the question: what would have caught it if this step had been wrong?
- infographic description: A flat vector two-column sort, 16:9, off-white background, no
                 arrows. Title top-left in the largest size: "What a reviewer can catch, and
                 what needs the record". Standfirst beneath: "Two of the six can be caught
                 from the manuscript alone." The canvas below is divided into three stacked
                 horizontal bands of equal height, each separated by a thin near-black rule.
                 Each band carries a heading on its left, set in the element-label size,
                 preceded by a small marker: band one, a green (#009E73) wrench glyph and the
                 heading "catchable by a check the reviewer can run"; band two, a sky-blue
                 (#56B4E9) cylinder glyph and the heading "catchable only from the record";
                 band three, a grey (#999999) short horizontal dash and the heading "beyond
                 reach, with or without the record". Inside each band, to the right of the heading, sit
                 two rows one above the other. Each row is a plain near-black-bordered
                 rectangle carrying a failure-mode name, with its annotation set in the
                 smaller annotation size immediately to the right of the box. Band one:
                 "fabricated citations" / "resolve every DOI — the reviewer's cheapest
                 action"; "confident extrapolation" / "compare the scope of the claim to the
                 scope of the evidence". Band two: "specification drift" / "the check is the
                 original specification, held fixed and re-read"; "context loss" / "the check
                 is an assertion against state the reviewer cannot see". Band three: "silent
                 unit errors" / "only if an invariant is checkable from the reported
                 numbers"; "over-agreeable review" / "leaves no external trace at all". A
                 vermillion (#D55E00) square bracket runs down the far-left margin, spanning
                 band two only, labelled beside it in vermillion "two of six need the
                 record", with a smaller grey line set beneath band three reading "two more
                 are beyond reach either way — say so in the assessment". A footer strip across the foot of the canvas, set in
                 the annotation size on a pale yellow (#F0E442) fill, reads: "what would have
                 caught it if this step had been wrong?" Generous margins, aligned to an
                 implied grid, all text in sentence case, legible in greyscale because every
                 band is named as well as coloured.
```

## 17.4 Inheriting a workflow you did not specify

A colleague leaves and you take over their quality-control pipeline.
It runs, it produces flags, and the group has been using its output for two years.
The temptation is to run it, because it works and there is a deadline.
The first task is to find out what it was supposed to do, and where no specification exists, that is the finding rather than an obstacle to reaching one.
An undocumented workflow in daily use is a governance problem the group already has and has not noticed.

Four things can be reconstructed from the workflow itself, and they come in a useful order.
Read the gates first, because what a workflow checks tells you what its builder was afraid of.
That is the most compressed statement of intent an undocumented pipeline contains.
Read the failure log and the rejection records second, because those say what the workflow has actually caught, which is usually narrower than what its gates were designed for.
Third, establish the calibration state of every gate.
A gate whose false-negative rate has never been measured is unmeasured rather than working.
Treating those two as the same thing is the error Chapter 11 §11.5 exists to prevent.
Fourth, check the dates on any calibration you do find.
One made two years ago and never repeated has expired rather than merely aged, and a tier claim resting on it has already lapsed.
Chapter 11 §11.5 sets out calibration validity and why a window is chosen at all.

Then the harder judgement, which is whether to run it before you understand it.
The rule I would hold to is that an inherited workflow runs first on cases whose answers you already know.
That is Chapter 11 §11.4's evaluation set built backwards.
Instead of curating cases to test something you are building, you assemble cases the workflow was already trusted on and check what it returns now.
Twenty such cases will teach you more in an afternoon than a week spent reading the code.
That is a practice I would defend rather than one anybody has measured (moderate confidence).
Three outcomes are possible: it reproduces what the group expected, it does not, or the group turns out never to have recorded what it expected.
The third is the one to watch for.

Sometimes the honest answer is that the workflow cannot be defended.
No specification, no calibration, no record of what it has caught, and its outputs already in three papers.
Inheriting it does not make you responsible for defending it.
It makes you responsible for saying so, to the group and in writing, and for deciding with them whether to rebuild it or stop relying on its output.
That is an unwelcome position to be put in and a legitimate one to hold.

**[AUTHOR: a workflow you inherited, agentic or not, and what you did before trusting it.]**

## 17.5 Judging a system you were handed

Your institution licenses a system with agentic components and asks the group to use it for handling data requests.
You will not see the specification, the gates or the model, and the datasheet reports a capability figure the supplier measured.
The reviewer's requests of §17.2 assume an author who can answer them.
Here the questions have to be put to a product, and often nobody in the room knows the answers.

Four questions are worth putting anyway, and worth putting in writing.
What are the system's acceptance criteria, and who set them?
Criteria set by a supplier encode the supplier's tolerance for error rather than yours, and the two are rarely the same in scientific work.
What does it do when it fails, and is the failure visible?
Failure that leaves no signal is the hardest kind to govern, because everything downstream then depends on somebody happening to notice.
What record does it leave?
Without one there is no audit trail, so nothing it produces can be reconstructed or defended afterwards (Chapter 12 §12.4, on what a record has to capture).
What is it permitted to touch?
That is the trust boundary of Chapter 12 §12.8, and your institutional IT will have asked some version of it already.

The supplier's own numbers are the book's stance turned outward.
A self-reported capability figure is a hypothesis.
The measurement that tests it is task-grounded evaluation on your own data, under your own conditions, against your own definition of a right answer (Chapter 11 §11.1).
Operational meteorology has already shown what that looks like at scale, in the re-verification of a data-driven weather model described in Chapter 11 §11.3 (Ben Bouallègue et al., 2024).
None of that procedure requires seeing inside the system, which is exactly why it works on a product you cannot audit.

Sometimes you will get no answers at all, and the position to hold then is narrow.
A system whose behaviour cannot be bounded, recorded or checked produces outputs that carry no evidential tier, so nothing resting on those outputs can claim one either.
That is a statement about the evidence and not an accusation about the supplier.
It also has institutional weight behind it.
Multi-national security guidance holds that an agentic system which cannot be understood, monitored or contained is not ready to run.
The same guidance asks that a specific human be named accountable before deployment (Five Eyes joint advisory, 2026).
So ask who that named person is.
Where the answer is nobody, you have learned the most useful thing on the list.

## 17.6 Verification checklist

This checklist is written for the receiver rather than the producer, and each item names what you can establish and what you cannot.
A reviewer, a successor, or a group weighing a supplied system should be able to work through it without any access to the workflow itself.

- **Disclosure read, and its gaps named.** The disclosure has been read against what one is for, meaning which tool did which task under whose oversight (Chapter 9), and the questions it leaves open are written down. It establishes the scope of the declared use, and not whether that use was checked.
- **The specification asked for.** A request has been made for the specification the agentic step ran under, and the answer, including "there isn't one", is on the record (§17.2; Chapter 3). An absent specification is a finding about the work rather than a gap in the review.
- **Gate calibration state established.** For each gate named, it is known whether its false-negative rate was ever measured, when, and under what validity window (Chapter 11 §11.5). An unmeasured gate is recorded as unmeasured rather than assumed to be working.
- **Tier claimed, and checked against its check.** The tier claimed for each result is matched to the specific check said to establish it (Chapter 11 §11.2). A tier with no check behind it is read as the highest tier the named checks actually support.
- **Reviewer coverage established.** It is known which parts had an independent check and which rest on author inspection alone (Chapter 12 §12.4). Coverage cannot establish that the review was searching, which no record distinguishes from a rubber stamp.
- **The mechanical checks actually run.** Every DOI resolved, every quoted passage verified against its source, and the scope of each claim compared to the scope of the reported evidence (§17.3; Chapter 13 §13.2, §13.7). These two modes need no cooperation from anyone, so skipping them wastes the part of the review you fully control.
- **The undetectable modes named rather than assumed absent.** Silent unit errors and over-agreeable review leave little or no external trace (§17.3), so the assessment says which claims rest on evidence you could not check.
- **A position stated where answers were not available.** The assessment records what was asked, what came back, and what evidential weight the result can carry given the gaps. An unanswered question left unrecorded becomes an implicit acceptance.

## 17.7 Repository pointer

The companion repository holds the runnable and perishable counterparts to this chapter under `/patterns/ch17-on-the-receiving-end`, with the printable receiver's checklist under `/checklists`.
The material here is a reviewer's question set rather than a program, and it holds three things.
The first is §17.2's five requests, numbered as they are numbered there and written as text a reviewer can paste into a report.
The disclosure statement sits above them, as the thing you read rather than ask for.
The second is §17.3's detectability sort as a working aid.
The third is a short intake form for an inherited workflow, covering the four reconstruction steps of §17.4.
The volatile material stays out of print for the usual reason.
Current journal and funder disclosure requirements, the current policy classes of Chapter 9 §9.4, and any supplier-specific evaluation notes all date faster than a printed page.
So the repository holds those dated and sourced, whilst the chapter states the questions and the reasoning **[AUTHOR: confirm the repository paths and contents once the reviewer question set is finalised]**.

---

### References

Report-sourced references carry a DOI or URL and are drawn from the verified sweep in `/research`. Every entry here also appears in the reference list of an earlier chapter; none is new to the book.

- Ansari, M. S. (2026). Compound deception in elite peer review: a failure mode taxonomy of 100 fabricated citations at NeurIPS 2025. *arXiv preprint* **[verify]**. https://arxiv.org/abs/2602.05930
- Ben Bouallègue, Z., et al. (2024). The rise of data-driven weather forecasting: a first statistical assessment of machine learning-based weather forecasts in an operational-like context. *Bulletin of the American Meteorological Society*, 105(6). DOI: 10.1175/BAMS-D-23-0162.1
- Elsevier (2026). "Generative AI policies for journals." Elsevier editorial policy page, updated June 2026. https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals **[verify: specifics volatile; confirm at citation time]**.
- Five Eyes joint advisory — National Cyber Security Centre (UK), Cybersecurity and Infrastructure Security Agency (US), National Security Agency (US), Australian Signals Directorate's Australian Cyber Security Centre, Canadian Centre for Cyber Security and National Cyber Security Centre New Zealand (2026). Careful adoption of agentic AI services (joint advisory, 30 April 2026), with the NCSC-UK companion blog, Thinking carefully before adopting agentic AI (15 May 2026). https://www.ncsc.gov.uk/blogs/thinking-carefully-before-adopting-agentic-ai — joint advisory: https://media.defense.gov/2026/Apr/30/2003922823/-1/-1/0/CAREFUL%20ADOPTION%20OF%20AGENTIC%20AI%20SERVICES_FINAL.PDF **[verify: risk/best-practice-catalogue detail beyond the summary against the primary advisory PDF]**
- National Institutes of Health (2023). "The Use of Generative Artificial Intelligence Technologies is Prohibited for the NIH Peer Review Process." NIH Guide Notice NOT-OD-23-149. https://grants.nih.gov/grants/guide/notice-files/NOT-OD-23-149.html **[verify: current NIH AI-in-review policy at citation time]**.

---

*Chapter 18 closes on what will last: the principles that survive the churn in tooling, and the split between a printed layer that holds and a repository layer that moves.*
