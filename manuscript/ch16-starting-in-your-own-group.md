# Chapter 16 — Starting in your own group

> **Status:** draft r3 · voice v3.3 (`STYLE.md`) · sentence-per-line per `STYLE.md` §10 · figures as briefs per `FIGURES.md`.
> **Conventions:** vendor-neutral (outline §9) · **[AUTHOR: …]** marks lived material only the author can supply · **[verify]** marks real but unconfirmed details · citations drawn only from verified reports in `/research`. Nothing has been invented.
> Volatile figures (energy-per-inference, per-token prices, hardware costs) are kept out of print and marked for the companion repository.

---

## 16.1 Why the on-ramp is organised around capabilities, not tools

The most common way a research group begins with agentic methods is also the least durable: someone adopts a named product, learns its interface, and quietly equates that interface with the practice itself.
The difficulty with this route is not that the chosen tool is poor but that the choice mislocates the effort, because the interface is the part of the field that changes fastest and matters least to whether the resulting work is trustworthy.
A group that has learned a product has learned something with a half-life measured in months; a group that has learned to specify a task precisely, to verify an output independently, and to record what an agent did and on whose authority has learned something that survives every tool migration it will subsequently make.

This distinction matters because adoption failures in scientific settings rarely trace to the model or the vendor.
They trace to work handed to an agent without an auditable specification (Chapter 3), to outputs accepted without a verification step the author could defend (Chapter 11), and to workflows that leave no record a colleague or reviewer could later reconstruct (Chapter 12).
These are habits, not features, and no procurement decision installs them.

The on-ramp set out in this chapter is therefore built around three capabilities a group must develop (specifying, verifying and governing) and it treats the particular tools used to practise them as interchangeable and disposable.
This is not an argument against choosing tools: a group must run something, and the repository accompanying this book records defensible current choices with the volatility they carry.
It is an argument about where the learning should be invested, which is in the parts of the practice that a change of vendor, a change of model, or a change of institutional policy will not invalidate.
This book holds that direction at high confidence and the specific sequencing proposed below at moderate confidence, because it reflects one plausible ordering of habit-formation rather than a validated curriculum, and any group should adapt it to the tasks it actually faces.

## 16.2 A thirty-day on-ramp

The thirty-day schedule below organises a group's first month around building the three capabilities in a deliberate order, each week producing an artefact the group keeps rather than a tutorial it completes.
The first week is spent entirely on specification, before any agent is given consequential work: the group takes one real, bounded, low-stakes task (a format conversion, a routine quality-control pass, a figure regenerated from a pipeline artefact) and writes it up as an executable, auditable specification in the schema of Chapter 3, stating objective, inputs, acceptance criteria and stop conditions.
The deliverable is not a completed task but a specification a second person can read and agree constitutes the task, because the discipline being built is the translation of a scientific intention into terms an instrument can execute and a human can check.
The second week introduces verification as a separate step with its own standing: the group runs the specified task, and for each output defines in advance how it will be checked (a test suite, a schema validation, a reconciliation against an independent source, a reviewer's sign-off), locating each check on the evidential hierarchy of Chapter 11 rather than accepting fluent output on trust.
The habit under construction is that no agent output is used until a check external to the agent has passed, and the artefact retained is a short verification record.
The third week adds governance: the group turns to the provenance and security material of Chapter 12, establishing where credentials live, what tools an agent may and may not touch, and what record each run leaves, so that by the end of the week a completed task carries an audit trail an institutional IT reviewer could inspect.
The fourth week composes the three into a single small workflow the group will actually keep using, run end to end under the governance now in place, and reviewed honestly against a plain question: did this save net effort once specification, verification and record-keeping are counted, and if not, why not.
The schedule's value is in the sequence (specify, then verify, then govern, then compose), not in the calendar; a group under heavier load may take a quarter rather than a month, and the ordering matters more than the pace (moderate confidence, from the internal logic of the dependencies rather than from a controlled trial).

A measurement of agent capability underpins that preference and the capabilities-not-tools stance of §16.1.
The strongest current gauge of agent capability has the length of task an agent can complete autonomously doubling roughly every three to four months as of 2026 (METR, 2026), so an on-ramp built around today's task-length ceiling is obsolete within a single budget cycle, while the governance capability the schedule builds (specification, gates, measurement) survives every capability jump.
The start-small stance is now multi-national security guidance too: begin with tightly bounded pilots on low-risk, clearly defined tasks before expanding scope (Five Eyes, 2026).
**[AUTHOR: if you have run an onboarding like this with a real group, a sentence on what actually broke in week one — most likely the specification step — would anchor this far better than the idealised schedule.]**

**Figure 16.1 — A capability-based thirty-day on-ramp.** *A figure brief follows `FIGURES.md`; render in the house style.*

```
FIGURE BRIEF
- id:            Figure 16.1
- title:         The thirty-day on-ramp as a sequence of habits, not tools
- type:          before/after
- claim:         A durable start builds three capabilities in order (specify, verify, govern, then compose), each producing a kept artefact, in contrast to the tool-first start that produces only familiarity with an interface.
- canvas:        16:9
- elements:      top band, de-emphasis grey, labelled "tool-first start": a single box
                 "adopt a product" leading to a faded box "learn the interface" leading to
                 a grey question mark "trust?"; bottom band, four sequential boxes across
                 the canvas — week 1 "specify" (blue, specification tag icon), week 2
                 "verify" (vermillion, gate diamond icon), week 3 "govern" (near-black,
                 audit-trail/document icon), week 4 "compose" (orange, agent loop icon);
                 beneath each of the four a small sky-blue artefact tag naming what is kept
- flow:          top band left-to-right ending in a grey question mark; bottom band
                 left-to-right, week 1 → week 2 → week 3 → week 4, each box feeding the next
- labels:        "tool-first start", "adopt a product", "learn the interface", "trust?",
                 "week 1 — specify", "week 2 — verify", "week 3 — govern",
                 "week 4 — compose", "kept: a specification", "kept: a verification record",
                 "kept: an audit trail", "kept: a working governed workflow"
- annotations:   a light bracket under the four bottom boxes labelled "habits that survive a change of tool"
- caption:       Figure 16.1 — A capability-based thirty-day on-ramp. The upper path, adopting a product first, leaves a group with interface familiarity and an unanswered question of trust; the lower path builds specifying, verifying and governing in sequence, each week retaining an artefact that outlasts any particular tool.
- alt-text:      A two-band diagram. The upper grey band shows a tool-first start: adopt a product, learn the interface, ending in a question mark labelled trust. The lower band shows four sequential weeks (specify, verify, govern, compose), each in its role colour and each producing a kept artefact named beneath it: a specification, a verification record, an audit trail and a working governed workflow.
- generator prompt: A flat vector before/after diagram on an off-white background, two
                 horizontal bands. The upper band is greyed and labelled "tool-first start":
                 a grey box "adopt a product" with an arrow to a faded box "learn the
                 interface" with an arrow to a grey diamond containing a question mark
                 labelled "trust?". The lower band shows four evenly spaced boxes connected
                 left to right by single arrows: a blue box "week 1 — specify" with a small
                 specification tag icon, a vermillion box "week 2 — verify" with a diamond
                 gate icon, a near-black box "week 3 — govern" with a small document icon,
                 and an orange box "week 4 — compose" with a small loop-arrow icon. Beneath
                 each lower box is a small sky-blue tag reading, in order, "kept: a
                 specification", "kept: a verification record", "kept: an audit trail",
                 "kept: a working governed workflow". A thin bracket spans the four lower
                 boxes, labelled "habits that survive a change of tool". Minimal text,
                 generous spacing, single-weight lines.
```

## 16.3 Where the money and the time actually go

The financial case for agentic methods is routinely misstated, because attention fixes on the one cost that is falling fastest and is most visible (the price of model inference), while the costs that dominate a well-run scientific workflow sit elsewhere and do not fall at the same rate.
Chapter 1 stated the principle: the expenditure migrates rather than disappears, moving out of model calls and into engineering time, evaluation and above all verification.
A group budgeting for adoption on the basis of per-token prices will therefore underestimate the true cost by a wide margin, not because those prices are wrong but because they are a small and shrinking share of the total.
There is now rigorous support for treating cost as a first-class axis rather than an afterthought: an analysis of agent evaluation found that simple baselines can match elaborate multi-agent scaffolds at a fraction of the cost, that agent costs vary by orders of magnitude at similar accuracy, and that ranking systems on accuracy alone rewards wasteful designs (Kapoor et al., 2024).
The judge-cost axis in particular is real and optimisable: a 2026 study found a mid-tier judge model with debiasing reaching 71% agreement with human judgements at roughly one-fifteenth the inference cost of top-tier alternatives (Soumik, 2026; a preprint, so the figure should be read as indicative).

The larger shares fall into four categories a realistic model must name.
The first is engineering effort: the time to specify tasks properly, to wire tools safely, to build the checks, and to maintain all of this as models and interfaces change underneath it, a recurring human cost, not a one-off.
The second is evaluation: the work of establishing, for each class of task, whether an agent is reliable enough to use at all, which is itself a scientific activity with its own design and its own labour (Chapter 11).
The third is verification, the running cost of checking every consequential output for as long as the workflow operates, which does not diminish with familiarity because it is the mechanism by which the work stays trustworthy rather than a training-wheels phase to be outgrown.
The fourth is the cost of failure and rework (silent errors caught late, tasks redone, the occasional workflow abandoned), which is real, hard to estimate in advance, and smaller precisely to the degree the first three are funded properly.
The implication for a group's budget is that inference is the line item to worry about least and verification the line item to protect most, which inverts the intuition that cheaper models make agentic work cheap.
The honest limitation is that the relative sizes of these four shares vary widely by task, group and domain, and no single split can be quoted as typical; the direction carries high confidence, and any specific proportions belong in the repository against a dated, worked example rather than in print **[verify: illustrative cost-share breakdown for one operational workflow (repository)]**.

**Figure 16.2 — Where adoption spend concentrates.** *A figure brief follows `FIGURES.md`; render in the house style.*

```
FIGURE BRIEF
- id:            Figure 16.2
- title:         The cost model — inference is the smallest share
- type:          architecture
- claim:         In a well-run scientific workflow the visible cost of model inference is the smallest of the recurring costs; engineering, evaluation and verification dominate, and verification is a running cost that does not diminish.
- canvas:        16:9
- elements:      five labelled cost blocks arranged left to right in a single row, sized to
                 suggest relative magnitude (not exact figures): a small orange block
                 "model inference"; a larger near-black block "engineering"; a larger
                 vermillion block "evaluation"; the largest vermillion block "verification
                 (recurring)"; a medium grey block "failure & rework"; a de-emphasis grey
                 caption strip beneath reading that magnitudes are illustrative and dated
                 figures live in the repository
- flow:          no directional flow; a left-to-right ordering from smallest recurring cost
                 (inference) to the dominant recurring cost (verification), with failure &
                 rework shown as shrinking when the others are funded
- labels:        "model inference", "engineering", "evaluation", "verification (recurring)",
                 "failure & rework", "magnitudes illustrative — dated figures in repository"
- annotations:   a small orange arrow beneath "model inference" labelled "falling fast";
                 a vermillion bracket over "evaluation" and "verification" labelled "where
                 spend concentrates"; a thin dashed outline around "failure & rework"
                 labelled "shrinks as the others are funded"
- caption:       Figure 16.2 — Where adoption spend concentrates. Block sizes are illustrative, not measured: model inference, the most visible and fastest-falling cost, is the smallest recurring share, while engineering, evaluation and verification dominate. Failure and rework shrink to the degree the other three are funded properly.
- alt-text:      A row of five cost blocks of differing sizes. Model inference is the smallest, marked as falling fast. Engineering is larger. Evaluation and verification are the largest, bracketed as where spend concentrates, with verification marked recurring. A fifth block, failure and rework, is dashed and marked as shrinking when the others are funded. A caption strip notes that magnitudes are illustrative and dated figures live in the repository.
- generator prompt: A flat vector diagram on an off-white background showing five rectangular
                 blocks in a single horizontal row, each a different width to suggest
                 relative cost. From left: a small orange block "model inference" with a
                 short orange arrow beneath labelled "falling fast"; a wider near-black
                 outlined block "engineering"; a wide vermillion block "evaluation"; the
                 widest vermillion block "verification (recurring)"; and a medium grey block
                 with a dashed outline "failure & rework" labelled beneath "shrinks as the
                 others are funded". A vermillion bracket spans the "evaluation" and
                 "verification" blocks, labelled "where spend concentrates". A small grey
                 caption strip runs along the bottom: "magnitudes illustrative — dated
                 figures in repository". Minimal text, generous spacing, single-weight lines.
```

## 16.4 The skills and roles a group needs

The capabilities a group must build map onto a small set of roles, and stating them plainly helps a group see that most are already present in a competent research team rather than requiring new hires.
The central observation is that adoption does not demand a machine-learning specialist; it demands that existing scientific roles take on named responsibilities for specification, verification and governance, and that those responsibilities are held by people rather than left implicit.
Four roles suffice for most groups, and one person may hold several.

A specification owner takes responsibility for translating scientific tasks into the auditable form of Chapter 3, and is typically the domain scientist who understands the task well enough to state its acceptance criteria, a role that cannot be delegated to whoever is most fluent with the tool, because it requires knowing what a correct answer is.
A verification owner is responsible for the checks: designing them, keeping them external to the agent, and ensuring no consequential output is used until they pass, a role that draws on ordinary scientific scepticism more than on any new expertise.
A governance owner holds the provenance and security responsibilities of Chapter 12 (where credentials live, what tools are permitted, what record each run leaves) and is the person who answers when institutional IT asks how the group's agents touch its systems.
An independent reviewer, human or a separate reviewer agent, provides a check that does not share the assumptions of the work being reviewed, and is the role most often omitted and most consequential when present.

The skills these roles require are largely those a good empirical scientist already has: precise specification, comfort with the command line and version control, a disposition to distrust fluent output, and the record-keeping habits of reproducible research.
What is genuinely new is narrower than it first appears: an understanding of how these systems fail plausibly rather than obviously (Chapter 13), and the judgement to keep a human accountable for every decision an agent informs.

One planning assumption is worth making explicit: agentic literacy is unevenly distributed within a group, and the norms around it are still contested rather than settled.
A large researcher survey found practice running ahead of disclosure and attitudes splitting by career stage, region and language background, with early-career and non-native-English researchers among the heaviest legitimate users (Naddaf, 2025).
A group should therefore assume its members start from different places and hold different views on what is acceptable, and build the roles above as a way of making responsibilities explicit rather than assuming a shared baseline.
The limitation worth stating is that this role map is a template, not a prescription: a two-person group will collapse the roles into shared vigilance, a larger group may formalise them, and this book offers the mapping with moderate confidence as a way to make responsibilities explicit rather than as an organisational chart to be copied.

## 16.5 Institutional, ethical and data-sovereignty considerations

Adopting agentic methods inside an institution raises obligations that precede any technical decision, and a group that treats them as afterthoughts will meet them later as blocks rather than earlier as design inputs.
The governing consideration is that agents touch data and systems on behalf of an institution that has committed to how those data may be handled, and those commitments (to data providers, to research participants, to funders, and to partners who shared observations under conditions) bind the group regardless of what a tool makes convenient.
Data sovereignty is the sharpest of these in the environmental sciences, because operational observations frequently cannot leave the jurisdiction or the institution that holds them, and sending such data to an externally hosted model to be processed may breach an agreement even where it would be technically trivial and scientifically useful.
This is not a hypothetical constraint but the central design driver of the constrained toolkit in Chapter 14, where partners who cannot share observations at all shape a three-tier architecture around that fact, and the same reasoning applies in miniature to any group weighing a hosted model against a locally run open-weight one.
The principle has an authoritative articulation to borrow: a major research funder prohibits its peer reviewers from putting proposal material into online AI services at all, on the ground that once material is sent its onward path is beyond control, so confidential material must not enter a third-party service (NIH, 2023).
This is the same logic that forces sensitive observations onto local, open-weight models rather than hosted ones.

The ethical considerations extend beyond data handling to the integrity of the scientific record: disclosure of how agents were used (Chapter 9), honesty about what was verified and what was taken on trust, and the firm line that an agent is never an author and never accountable for a scientific decision.
Institutional considerations are more mundane but no less binding: procurement and security review, acceptable-use policies, and the questions institutional IT will ask about credential handling and least-privilege access (Chapter 12).
A group that has built its governance habits in the third week of the on-ramp will find these conversations short, because it can already answer them.

European funder guidance now packages much of this together, and usefully so: its living guidelines make researchers responsible for verifying AI-generated results, ask for transparent disclosure of substantial AI use, require privacy and confidentiality to be protected when material is fed to AI systems, and warn against AI in evaluative processes such as proposal review (European Commission, 2024).
The implication is that sovereignty, ethics and institutional policy are best treated as inputs to the specification of a workflow rather than as compliance applied to a finished one, since a workflow designed around a data-handling constraint is sound where one retrofitted to it is fragile.
A peer-reviewed 2026 systematic review reaches the conclusion this section is built on: prevailing, reactive policy frameworks are inadequate, and a group is better served building proactive governance of its own than waiting for settled institutional rules to arrive (Slimi, 2026).
The limitation is that the specifics vary by jurisdiction, institution and funder and change over time, so this section states the classes of obligation and the stance towards them; the current particulars for a given setting belong with the group's own governance record, not in a printed chapter that would date **[verify: current institutional and funder policy classes (repository)]**.

## 16.6 The energy and carbon cost of inference

An environmental readership is owed an honest treatment of the energy and carbon cost of the methods this book advocates, addressed with the same discipline the book applies to every other claim: reasoning and direction in print, volatile figures in the repository.
The core facts can be stated without quoting numbers that would be stale before the ink dried.
Running a large model consumes energy, both in the one-off training of the model and in each inference a workflow performs, and that energy carries a carbon cost that depends on the electricity mix powering the data centre where the computation runs.
That this belongs in a governance chapter at all is not an activist add-on: a national risk-management profile for generative AI lists the environmental impacts of training and inference among its named risk areas (NIST, 2024), which places the concern within mainstream governance rather than at its margin.

The reasoning a scientist needs is comparative rather than absolute.
A single inference is small; a workflow that issues many inferences in a loop, run repeatedly across a research programme, is not, and the relevant quantity is the aggregate over the workflow's life rather than the cost of one call.
Three considerations follow, all directional and all robust to the churn in the underlying figures.
First, the efficiency of models per unit of capability has been improving, so the energy cost of achieving a given result falls over time even as the cost of the largest models rises, which means the honest comparison is always to a specific task at a specific date, not to a headline figure about the largest system available.
Second, the carbon intensity of the same computation varies substantially with where and when it runs, so a workflow run on a low-carbon grid, or scheduled when renewable supply is high, carries a materially different footprint from the identical workflow run elsewhere, a lever a group actually controls.
Third, the counterfactual matters: an agentic workflow that replaces a computation a scientist would otherwise have run (a manual reprocessing, a repeated model execution, a literature search across many sessions) has a net footprint that may be lower or higher than the alternative, and the comparison is only meaningful when the displaced activity is counted rather than assumed to be free.
This last point has a striking domain example: an operational forecasting centre reported that generating a forecast with its data-driven model used on the order of a thousand times less energy than its physics-based system, a saving that is real but sits at inference and does not include the one-off training cost (Lang et al., 2024), a reminder that the honest ledger counts both the displaced computation and the training amortised across a model's use.

The honest position, held with high confidence in its reasoning and deliberately without a headline number, is that inference energy is a real cost an environmental scientist should account for, that it is neither negligible nor catastrophic per call, that its aggregate over a workflow is the quantity that matters, and that a group can reduce it through model choice, grid choice, scheduling, and the discipline of not running loops that produce nothing.
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

*Chapter 17 turns from starting to lasting: the durable principles that survive the tooling churn, how to stay current without chasing releases, and the repository as the living layer beneath a printed book.*
