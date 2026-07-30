# Chapter 16 — Starting in your own group

> **Status:** draft r7 · voice v5.0 (`STYLE.md` §1) · sentence-per-line per `STYLE.md` §10 · figures as briefs per `FIGURES.md`.
> **Conventions:** vendor-neutral (outline §9) · **[AUTHOR: …]** marks lived material only the author can supply · **[verify]** marks real but unconfirmed details · citations drawn only from verified reports in `/research`. Nothing has been invented.
> Volatile figures (energy-per-inference, per-token prices, hardware costs) are kept out of print and marked for the companion repository.

> **[ai-reviewer: A1 review — 2 comments in this file.** All five tasks landed. §16.6 now carries four considerations, not three, and the "loops that produce nothing" clause appears once, in the new fourth consideration, and has been removed from the closing paragraph — that acceptance criterion is met exactly. The induced-demand passage names no economic effect, quantifies nothing, and says so explicitly ("high confidence in the mechanism, low confidence in any magnitude"), which is what §4 of the plan required. §16.1's budget argument cross-references §4.4 without re-deriving it. One comment below on the placement of the deskilling paragraph relative to Naddaf (2025), which §4 singles out as the citation most at risk of being laundered.**]**

---

## 16.1 Why the plan is organised around capabilities, not tools

The most common way a research group starts with agentic methods is also the least durable.
Someone adopts a named product, learns its interface, and quietly equates that interface with the practice itself.

The problem is not that the chosen tool is poor.
It is that the effort goes into the wrong place, because the interface is the part of the field that changes fastest and matters least to whether the resulting work is trustworthy.
Learn a product and you have learned something with a life measured in months.
Learn to specify a task precisely, to verify an output independently, and to record what an agent did and on whose authority, and you have learned something that survives every tool migration you will ever make.

This distinction matters because adoption failures in scientific settings rarely trace to the model or the vendor.
They trace to work handed to an agent without an auditable specification (Chapter 3), to outputs accepted without a verification step the author could defend (Chapter 11), and to workflows that leave no record a colleague or reviewer could later reconstruct (Chapter 12).
These are habits, not features, and no procurement decision installs them.

So the plan in this chapter is built around three capabilities you have to develop, specifying, verifying and governing, and it treats the tools you practise them with as interchangeable and disposable.
This is not an argument against choosing tools.
You have to run something, and the repository accompanying this book records defensible current choices with the volatility they carry.
It is an argument about where to invest the learning: in the parts of the practice a change of vendor, a change of model, or a change of institutional policy will not invalidate.
This book holds that direction at high confidence and the specific sequencing proposed below at moderate confidence, because it reflects one plausible ordering of habit-formation rather than a validated curriculum, and any group should adapt it to the tasks it actually faces.

## 16.2 A thirty-day plan

The thirty-day schedule below organises your first month around building the three capabilities in a deliberate order, with each week producing an artefact you keep rather than a tutorial you complete.

The first week goes entirely on specification, before any agent gets consequential work: the group takes one real, bounded, low-stakes task (a format conversion, a routine quality-control pass, a figure regenerated from a pipeline artefact) and writes it up as an executable, auditable specification in the schema of Chapter 3, stating objective, inputs, acceptance criteria and stop conditions.
The deliverable is not a completed task but a specification a second person can read and agree constitutes the task, because the discipline being built is the translation of a scientific intention into terms an instrument can execute and a human can check.

The second week introduces verification as a separate step with its own standing: the group runs the specified task, and for each output defines in advance how it will be checked (a test suite, a schema validation, a reconciliation against an independent source, a reviewer's sign-off), locating each check on the evidential hierarchy of Chapter 11 rather than accepting fluent output on trust.
The habit under construction is that no agent output is used until a check external to the agent has passed, and the artefact retained is a short verification record.

The third week adds governance.
You turn to the provenance and security material of Chapter 12, establishing where credentials live, what tools an agent may and may not touch, and what record each run leaves, so by the end of the week a completed task carries an audit trail an institutional IT reviewer could inspect.

The fourth week composes the three into one small workflow you will actually keep using, run end to end under the governance now in place, and reviewed honestly against a plain question: did this save net effort once specification, verification and record-keeping are counted, and if not, why not?

The value is in the sequence, meaning specify, then verify, then govern, then compose, and not in the calendar.
A group under heavier load may take a quarter rather than a month; the ordering matters more than the pace (moderate confidence, from the internal logic of the dependencies rather than from a controlled trial).

A measurement of agent capability supports both that ordering and the capabilities-not-tools stance of §16.1.
The strongest current gauge has the length of task an agent can complete autonomously doubling roughly every three to four months as of 2026 (METR, 2026).
A plan built around today's task-length ceiling is obsolete within a single budget cycle, while the governance capability this schedule builds, meaning specification, gates and measurement, survives every capability jump.
The start-small stance is now multi-national security guidance too: begin with tightly bounded pilots on low-risk, clearly defined tasks before expanding scope (Five Eyes, 2026).
**[AUTHOR: if you have run an onboarding like this with a real group, a sentence on what actually broke in week one — most likely the specification step — would anchor this far better than the idealised schedule.]**

**Figure 16.1 — A capability-based thirty-day plan.**

![Two bands. The top band, greyed, shows the tool-first start: adopt a product, learn the interface, then a question mark labelled trust, annotated that what was learned has the lifespan of the product. The bottom band shows four weeks: week one, specify, keeping a real specification a colleague agrees constitutes the task; week two, verify, keeping a verification record and the habit that no output is used before a check external to the agent passes; week three, govern, keeping an audit trail an IT reviewer could inspect; week four, compose, keeping a working governed workflow reviewed against one plain question, did this save net effort once the checking is counted. A bracket underneath reads habits that survive a change of tool.](../figures/figure-16-1.svg)

*Figure 16.1 — Two ways to spend a first month. The grey path is the common one: adopt a product, learn its interface, and end up unable to say why the output should be trusted. The four-week path builds one capability at a time, and each week's deliverable is an artefact you keep, not a tutorial you complete. The sequence matters more than the calendar; the artefacts survive every change of tool. (Rendered as `figures/figure-16-1.svg` from the brief below, per `FIGURES.md`.)*

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

## 16.3 Where the money and the time actually go

The financial case for agentic methods gets misstated routinely, because attention fixes on the one cost that is falling fastest and is most visible, the price of model inference, while the costs that dominate a well-run scientific workflow sit elsewhere and do not fall at the same rate.

Chapter 1 stated the principle: the spending moves rather than disappears, out of model calls and into engineering time, evaluation and above all verification.
Budget for adoption on per-token prices and you will underestimate the true cost by a wide margin.
Not because those prices are wrong, but because they are a small and shrinking share of the total.
There is now rigorous support for treating cost as a first-class axis rather than an afterthought: an analysis of agent evaluation found that simple baselines can match elaborate multi-agent scaffolds at a fraction of the cost, that agent costs vary by orders of magnitude at similar accuracy, and that ranking systems on accuracy alone rewards wasteful designs (Kapoor et al., 2024).
The judge-cost axis in particular is real and optimisable: a 2026 study found a mid-tier judge model with debiasing reaching 71% agreement with human judgements at roughly one-fifteenth the inference cost of top-tier alternatives (Soumik, 2026; a preprint, so the figure should be read as indicative).

The larger shares fall into four categories a realistic model must name.
The first is engineering effort: the time to specify tasks properly, to wire tools safely, to build the checks, and to maintain all of this as models and interfaces change underneath it, a recurring human cost, not a one-off.
The second is evaluation: the work of establishing, for each class of task, whether an agent is reliable enough to use at all, which is itself a scientific activity with its own design and its own labour (Chapter 11).
The third is verification, the running cost of checking every consequential output for as long as the workflow operates, which does not diminish with familiarity because it is the mechanism by which the work stays trustworthy rather than a training-wheels phase to be outgrown.
The fourth is the cost of failure and rework (silent errors caught late, tasks redone, the occasional workflow abandoned), which is real, hard to estimate in advance, and smaller precisely to the degree the first three are funded properly.
The implication for a group's budget is that inference is the line item to worry about least and verification the line item to protect most, which inverts the intuition that cheaper models make agentic work cheap.
That inversion is not a temporary state of the technology, and the difference matters over a five-year budget.
What a check costs is set by the task rather than by the model, so it does not fall as models improve.
Chapter 4 §4.4 makes that argument, on why the class of work worth delegating does not widen.
A budget written on the assumption that verification is a transitional expense will be wrong in the same direction every year.
The honest limitation is that the relative sizes of these four shares vary widely by task, group and domain, and no single split can be quoted as typical; the direction carries high confidence, and any specific proportions belong in the repository against a dated, worked example rather than in print **[verify: illustrative cost-share breakdown for one operational workflow (repository)]**.

**Figure 16.2 — Where adoption spend concentrates.**

![Five cost blocks in a row, sized to suggest relative magnitude rather than exact figures. A small orange block, model inference, carries a downward arrow labelled falling fast and the note that this is the cost everyone watches. Larger blocks follow: engineering, annotated as recurring human time to specify, wire and maintain; evaluation, annotated as establishing whether the agent is reliable enough to use at all; and the largest, verification, annotated as recurring for as long as the workflow runs, and not falling as model prices fall. A dashed-outlined grey block, failure and rework, is annotated as shrinking exactly to the degree the other three are funded. A bracket over evaluation and verification reads where the spend actually concentrates, and a caption strip reads magnitudes illustrative, dated figures in the repository.](../figures/figure-16-2.svg)

*Figure 16.2 — The cost everyone watches is the smallest block. Inference is falling fast and is the least of it; engineering, evaluation and above all verification are the recurring costs. Verification does not fall as model prices fall, because it is external to the model by design. The dashed block is the honest one: failure and rework shrinks exactly to the degree the other three are funded. Budget from this picture, not from a price-per-token page. (Rendered as `figures/figure-16-2.svg` from the brief below, per `FIGURES.md`.)*

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

## 16.4 The skills and roles a group needs

The capabilities you have to build map onto a small set of roles, and naming them plainly shows that most are already present in a competent research team rather than needing new hires.

Adoption does not demand a machine-learning specialist.
It demands that existing scientific roles take on named responsibilities for specification, verification and governance, and that people hold those responsibilities rather than leaving them implicit.
Four roles are enough for most groups, and one person may hold several.

A specification owner takes responsibility for translating scientific tasks into the auditable form of Chapter 3, and is typically the domain scientist who understands the task well enough to state its acceptance criteria, a role that cannot be delegated to whoever is most fluent with the tool, because it requires knowing what a correct answer is.
A verification owner is responsible for the checks: designing them, keeping them external to the agent, and ensuring no consequential output is used until they pass, a role that draws on ordinary scientific scepticism more than on any new expertise.
A governance owner holds the provenance and security responsibilities of Chapter 12 (where credentials live, what tools are permitted, what record each run leaves) and is the person who answers when institutional IT asks how the group's agents touch its systems.
An independent reviewer, human or a separate reviewer agent, provides a check that does not share the assumptions of the work being reviewed, and is the role most often omitted and most consequential when present.

The skills these roles require are largely those a good empirical scientist already has: precise specification, comfort with the command line and version control, a disposition to distrust fluent output, and the record-keeping habits of reproducible research.
What is genuinely new is narrower than it first appears: an understanding of how these systems fail plausibly rather than obviously (Chapter 13), and the judgement to keep a human accountable for every decision an agent informs.

Those skills were acquired by doing work an agent now does in an afternoon.
Saying they are skills a good scientist already has therefore assumes a continuing supply of people who learned them that way.
A group leader is the person who decides whether that supply continues.
Deciding what a doctoral researcher spends three years on is deciding the group's future capacity to verify, not only this year's throughput.
Chapter 13 §13.9 makes that argument, on deskilling and the supply of judgement.
The planning consequence is narrow enough to act on.
Name the judgements the group intends to keep in-house, and protect the work that builds them even where an agent would be faster.
This is an argument from the book's own premises rather than a measured effect, and no source here supports it (moderate confidence).
[ai-reviewer: the disclaimer is present and correctly worded, and no citation is attached, so the letter of §4's prohibition is met. The placement still deserves a second look. This paragraph now sits immediately before the one that opens "One planning assumption is worth making explicit" and cites Naddaf (2025) on adoption running ahead of disclosure and attitudes splitting by career stage. Two consecutive paragraphs, both framed as planning assumptions about people, the first unsourced and the second sourced, invite a reader to carry the citation backwards — which is precisely the laundering §4 names Naddaf as the risk for. The disclaimer sits at the end of the first paragraph, where a reader arrives at it after forming the connection rather than before.
Nothing here needs deleting. A paragraph between them, or moving the deskilling material after the Naddaf paragraph so the sourced claim comes first, would remove the adjacency at no cost to either argument. Worth doing because this is the one place in the pass where the plan predicted the specific failure by name, and the text is one reading away from it. Ai-writer's to place; flagging so the near-miss is on the record rather than left to be discovered by a reviewer of the finished book.]

One planning assumption is worth making explicit: agentic literacy is unevenly distributed within a group, and the norms around it are still contested rather than settled.
A large researcher survey found practice running ahead of disclosure and attitudes splitting by career stage, region and language background, with early-career and non-native-English researchers among the heaviest legitimate users (Naddaf, 2025).
A group should therefore assume its members start from different places and hold different views on what is acceptable, and build the roles above as a way of making responsibilities explicit rather than assuming a shared baseline.
The limitation worth stating is that this role map is a template, not a prescription: a two-person group will collapse the roles into shared vigilance, a larger group may formalise them, and this book offers the mapping with moderate confidence as a way to make responsibilities explicit rather than as an organisational chart to be copied.

## 16.5 Institutional, ethical and data-sovereignty considerations

Adopting agentic methods inside an institution raises obligations that come before any technical decision.
Treat them as afterthoughts and you will meet them later as blocks rather than earlier as design inputs.
The governing consideration is that agents touch data and systems on behalf of an institution that has committed to how those data may be handled, and those commitments (to data providers, to research participants, to funders, and to partners who shared observations under conditions) bind the group regardless of what a tool makes convenient.
Data sovereignty is the sharpest of these in the environmental sciences, because operational observations frequently cannot leave the jurisdiction or the institution that holds them, and sending such data to an externally hosted model to be processed may breach an agreement even where it would be technically trivial and scientifically useful.
This is not a hypothetical constraint but the central design driver of the constrained toolkit in Chapter 14, where partners who cannot share observations at all shape a three-tier architecture around that fact, and the same reasoning applies in miniature to any group weighing a hosted model against a locally run open-weight one.
The principle has an authoritative articulation to borrow: a major research funder prohibits its peer reviewers from putting proposal material into online AI services at all, on the ground that once material is sent its onward path is beyond control, so confidential material must not enter a third-party service (NIH, 2023).
This is the same logic that forces sensitive observations onto local, open-weight models rather than hosted ones.

The ethical considerations extend beyond data handling to the integrity of the scientific record: disclosure of how agents were used (Chapter 9), honesty about what was verified and what was taken on trust, and the firm line that an agent is never an author and never accountable for a scientific decision.
Institutional considerations are more mundane but no less binding: procurement and security review, acceptable-use policies, and the questions institutional IT will ask about credential handling and least-privilege access (Chapter 12).
A group that has built its governance habits in the third week of the plan will find these conversations short, because it can already answer them.
Much of what this section assumes a group can decide is decided elsewhere when the system arrives from an institution or a vendor.
Chapter 17 takes that case, on judging agentic work you did not produce.

European funder guidance now packages much of this together, and usefully so: its living guidelines make researchers responsible for verifying AI-generated results, ask for transparent disclosure of substantial AI use, require privacy and confidentiality to be protected when material is fed to AI systems, and warn against AI in evaluative processes such as proposal review (European Commission, 2024).
The implication is that sovereignty, ethics and institutional policy are best treated as inputs to the specification of a workflow rather than as compliance applied to a finished one, since a workflow designed around a data-handling constraint is sound where one retrofitted to it is fragile.
A peer-reviewed 2026 systematic review reaches the conclusion this section is built on: prevailing, reactive policy frameworks are inadequate, and a group is better served building proactive governance of its own than waiting for settled institutional rules to arrive (Slimi, 2026).
The limitation is that the specifics vary by jurisdiction, institution and funder and change over time, so this section states the classes of obligation and the stance towards them; the current particulars for a given setting belong with the group's own governance record, not in a printed chapter that would date **[verify: current institutional and funder policy classes (repository)]**.

## 16.6 The energy and carbon cost of inference

An environmental readership is owed an honest treatment of the energy and carbon cost of the methods this book advocates, handled with the same discipline as every other claim here: reasoning and direction in print, volatile figures in the repository.

The core facts can be stated without quoting numbers that would be stale before the ink dried.
Running a large model consumes energy, both in the one-off training of the model and in each inference a workflow performs, and that energy carries a carbon cost that depends on the electricity mix powering the data centre where the computation runs.
That this belongs in a governance chapter at all is not an activist add-on: a national risk-management profile for generative AI lists the environmental impacts of training and inference among its named risk areas (NIST, 2024), which places the concern within mainstream governance rather than at its margin.

The reasoning a scientist needs is comparative rather than absolute.
A single inference is small; a workflow that issues many inferences in a loop, run repeatedly across a research programme, is not, and the relevant quantity is the aggregate over the workflow's life rather than the cost of one call.
Four considerations follow, all directional and all robust to the churn in the underlying figures.
First, the efficiency of models per unit of capability has been improving, so the energy cost of achieving a given result falls over time even as the cost of the largest models rises, which means the honest comparison is always to a specific task at a specific date, not to a headline figure about the largest system available.
Second, the carbon intensity of the same computation varies substantially with where and when it runs, so a workflow run on a low-carbon grid, or scheduled when renewable supply is high, carries a materially different footprint from the identical workflow run elsewhere, a lever a group actually controls.
Third, the counterfactual matters: an agentic workflow that replaces a computation a scientist would otherwise have run (a manual reprocessing, a repeated model execution, a literature search across many sessions) has a net footprint that may be lower or higher than the alternative, and the comparison is only meaningful when the displaced activity is counted rather than assumed to be free.
This last point has a striking domain example: an operational forecasting centre reported that generating a forecast with its data-driven model used on the order of a thousand times less energy than its physics-based system, a saving that is real but sits at inference and does not include the one-off training cost (Lang et al., 2024), a reminder that the honest ledger counts both the displaced computation and the training amortised across a model's use.

Fourth, that counterfactual counts the computation an agentic workflow displaced and not the computation it created.
A parameter sweep gets run because running it now costs machine time instead of somebody's attention.
A reprocessing gets repeated because repeating it is easy.
A loop gets left running because nobody is watching what it produces.
None of those displaced anything, because none of them would have been run at all.
So the aggregate footprint of a research programme can rise while every individual workflow in it displaced something more expensive, and both statements stay true.
The accounting question is therefore not only what this replaced but whether it would have been run at all.
That is a specification question before it is an energy question (Chapter 3, on stating what a run is for before it starts).

How large the effect is, I cannot tell you.
Nothing in the evidence behind this book measures it.
I will not offer a number for something nobody here has measured (high confidence in the mechanism, low confidence in any magnitude).
The mechanism is named because a climate-literate reader will otherwise notice it missing, not because the book can size it.
What a group can do about it is narrow: run nothing it cannot state the purpose of.
A sweep gets a stated question, a rerun gets a stated reason, and a loop that produces nothing gets stopped.

**[AUTHOR: whether you have watched induced demand happen in your own group — a sweep or a rerun that existed only because it became cheap — and roughly what it cost.]**

The honest position, held with high confidence in its reasoning and deliberately without a headline number, is that inference energy is a real cost an environmental scientist should account for, that it is neither negligible nor catastrophic per call, that its aggregate over a workflow is the quantity that matters, and that a group can reduce it through model choice, grid choice and scheduling.
The specific figures (energy per inference at a given capability tier, grid carbon intensities, the footprint of a worked example workflow) are exactly the volatile quantities this book keeps out of print, and they live, dated and sourced, in the companion repository **[verify: energy-per-inference and grid-intensity figures with sources and dates (repository)]**.
The limitation is that measuring the footprint of a hosted model's inference precisely is difficult from outside the provider, and the field's disclosure on this is incomplete; a group that wants a defensible number for its own workflow will get closer with a locally run open-weight model whose consumption it can meter directly than with a hosted service it can only estimate **[AUTHOR: if you have metered a local workflow's consumption, even roughly, that measured anchor would strengthen this section — mark it clearly as one setting's figure].**

---

### References

Report-sourced references carry a DOI or URL and are drawn from the verified sweep in `/research`.

- European Commission, Directorate-General for Research and Innovation (2024; updated 8 May 2026). Living guidelines on the responsible use of generative AI in research (European Research Area). https://research-and-innovation.ec.europa.eu/document/download/2b6cf7e5-36ac-41cb-aab5-0d32050143dc_en **[verify the 2026 update's provisions against the updated PDF before release]**
- Five Eyes joint advisory — National Cyber Security Centre (UK), Cybersecurity and Infrastructure Security Agency (US), National Security Agency (US), Australian Signals Directorate's Australian Cyber Security Centre, Canadian Centre for Cyber Security and National Cyber Security Centre New Zealand (2026). Careful adoption of agentic AI services (joint advisory, 30 April 2026), with the NCSC-UK companion blog, Thinking carefully before adopting agentic AI (15 May 2026). https://www.ncsc.gov.uk/blogs/thinking-carefully-before-adopting-agentic-ai — joint advisory: https://media.defense.gov/2026/Apr/30/2003922823/-1/-1/0/CAREFUL%20ADOPTION%20OF%20AGENTIC%20AI%20SERVICES_FINAL.PDF **[verify: risk/best-practice-catalogue detail beyond the summary against the primary advisory PDF]**
- Kapoor, S., Stroebl, B., Siegel, Z. S., Nadgir, N., & Narayanan, A. (2024). AI agents that matter. *arXiv preprint* **[verify archival venue before release]**. https://arxiv.org/abs/2407.01502
- Lang, S., Alexe, M., Chantry, M., et al. (2024). AIFS — ECMWF's data-driven forecasting system. *arXiv preprint* **[verify journal version]**. https://arxiv.org/abs/2406.01465
- METR (2026). Time horizon 1.1. METR research blog, 29 January 2026. https://metr.org/blog/2026-1-29-time-horizon-1-1/
- Naddaf, M. (2025). Is it OK for AI to write science papers? Nature survey shows researchers are split. *Nature* (news feature reporting a survey of ~5,000 researchers). https://www.nature.com/articles/d41586-025-01463-8 **[verify exact author byline at citation time]**
- National Institutes of Health (2023). The use of generative artificial intelligence technologies is prohibited for the NIH peer review process. NIH Guide Notice NOT-OD-23-149, 23 June 2023. https://grants.nih.gov/grants/guide/notice-files/NOT-OD-23-149.html
- Slimi, Z. (2026). A systematic critical review of generative AI's impact on authorship, pedagogy, and integrity (2023–2025). *Frontiers in Education*, 11. DOI: 10.3389/feduc.2026.1769680
- Soumik, S. K. (2026). Judging the judges: a systematic evaluation of bias-mitigation strategies in LLM-as-a-judge pipelines. *arXiv preprint* **[verify venue]**. https://arxiv.org/abs/2604.23178

---

*Chapter 17 takes the reverse position: what to ask for when the workflow is someone else's, which failure modes a reviewer can catch from outside, and what to do with a system you were handed.*
