# Chapter 6 — Data acquisition and quality control

> **Status:** draft · figures specified as briefs per `FIGURES.md`. Chapter lengths are indicative guidance, not fixed allocations.
> **Conventions:** vendor-neutral per outline §9. Passages needing the author's lived material or number verification are tagged **[AUTHOR: …]** or **[verify]**. No datasets, figures or results have been invented; worked-example specifics are marked for the author to supply.

---

## 6.1 The problem: observations arrive messy, and the mess is where errors hide

The acquisition and quality control of environmental observations consumes a disproportionate share of a scientist's time precisely because the work is heterogeneous, repetitive and unforgiving of small mistakes. A single study in operational hydrology may draw on river-gauge records in a national agency's fixed-width text format, rainfall from an automatic weather-station network in one comma-separated dialect, radar-derived precipitation on a projected grid, and reanalysis fields in a self-describing binary format, each with its own timestamp convention, missing-value sentinel, unit system and update cadence **[AUTHOR: confirm the specific formats and networks you routinely reconcile, and name them in the repository rather than in print]**. The difficulty is not that any one of these is hard to read; it is that reconciling them into a single, physically coherent, gap-aware record demands hundreds of small judgements — is a flat-lined sensor frozen or genuinely static, is a spike a real convective burst or a telemetry glitch, is a gap a missing observation or a recorded zero — and that each judgement, made in haste against a deadline, is an opportunity for an error that no later step will announce. The errors that matter most in this domain are quiet ones: a millimetres-to-inches slip, a UTC-to-local shift, an accumulation silently read as a rate. Such faults do not raise exceptions, they propagate. They enter the calibration, bias the verification, and are discovered — if at all — only when a downstream result refuses to reconcile with reality, by which time the provenance needed to diagnose them has usually been lost. This chapter treats data acquisition and quality control as the first pattern where an agent earns its place, and where the governing discipline of the whole book — that authority over the data stays with deterministic rules and accountable humans — is stated in its sharpest operational form.

## 6.2 The conventional workflow, and where it strains

The conventional quality-control workflow is a sequence of scripts and human eyes that works well at small scale and degrades predictably as scale grows. A scientist writes a loader for each incoming format, hand-tunes a set of range checks and step-change thresholds against the physical bounds of the variable, plots the flagged series, inspects the flags, corrects the loader where it has misfired, and repeats until the record looks defensible **[AUTHOR: sketch your own current gauge-and-rainfall QC routine — the scripts, the manual plotting step, the reconciliation against neighbouring stations — so the redesign in §6.3 is measured against something real]**. Three properties of this workflow set the ceiling on it. The manual effort scales with the number of station-format combinations rather than with the science, so adding a partner network can cost days of loader-writing that produce no new understanding. The judgements are made in the analyst's head and recorded, if at all, in comments and commit messages, so the reasoning behind a particular flag — why this spike was accepted and that one rejected — is rarely reconstructable six months later, which is a provenance failure taken up properly in Chapter 12. And the checks themselves, being hand-maintained, tend to lag the data: a new failure mode in a sensor appears, produces a class of bad values, and is only encoded as a rule after it has already contaminated a release. The strain is therefore not that the conventional workflow is wrong — its deterministic checks are exactly what should retain authority — but that the parts of it demanding pattern-recognition across many heterogeneous streams, and the parts demanding a written record of every judgement, are the parts a human does slowly, inconsistently and without an audit trail. Those are the parts, and only those parts, that an agent is positioned to take over, and the redesign that follows is deliberate about drawing that line and holding it (high confidence that the division is the right one; the precise boundary is a design choice that varies by network).

## 6.3 The agentic redesign: agents propose, QC rules dispose

The organising principle of the redesign is a strict separation of authority: the agent proposes flags and transformations with written justification, and deterministic quality-control rules dispose of every proposal, so that no observation is ever silently overwritten by a language model. This principle inverts the intuitive but dangerous arrangement in which a capable model is handed the data and asked to "clean" it. Under that arrangement the model's fluency becomes a liability, because a plausible interpolation across a gap is indistinguishable, in the output, from a measured value, and the very smoothness that makes the result look finished is what conceals the fabrication. The redesign refuses the model any write access to the observational record. What the agent may do is read the heterogeneous inputs, normalise their formats into a common representation, and generate for each suspect point a structured proposal — a flag type, the evidence for it, the neighbouring context it considered, and a confidence — expressed as a machine-readable object rather than a modified data value. What disposes of that proposal is a deterministic rule set: physical bounds for the variable, inter-station consistency checks, rate-of-change limits, and the network's own documented quality conventions, all of them code that a human wrote, reviewed and can rerun identically. A proposal that survives the rules is applied as a *flag*, never as a substituted value; a proposal that the rules reject is logged, with the rejection reason, and the point is left as observed. The agent's contribution is thus confined to the two things it does well — wrangling formats and articulating a justified hypothesis about each anomaly — while the two things that must not be delegated — the decision to alter the record, and the authority over what counts as physically admissible — remain with deterministic code and, above it, with the accountable scientist. The tools the agent calls to do this are the ordinary function-call machinery of Chapter 2: a format reader, a unit resolver, a neighbouring-station query, each with a narrow, declared interface, so that the agent's actions are auditable calls rather than opaque cognition (high confidence in the pattern; the specific tool set depends on the data landscape).

**Figure 6.1 — Propose–dispose architecture.** *A figure brief follows `FIGURES.md`; render in the house style.*

```
FIGURE BRIEF
- id:            Figure 6.1
- title:         Agents propose, QC rules dispose — where authority sits
- type:          architecture
- claim:         The agent may read, normalise and propose, but only deterministic rules may dispose; the observational record is never written by the model.
- canvas:        16:9
- elements:      left, three stacked "raw inputs" cylinders in sky blue (gauge, rainfall, grid);
                 a rounded orange "QC agent" rectangle containing an "LLM" box (orange), a
                 "plan–act–observe" loop ring, and green tool glyphs "format reader",
                 "unit resolver", "neighbour query"; from the agent a labelled arrow
                 "flag proposals (justified)" to a vermillion diamond "deterministic QC rules";
                 the diamond lists in small type "physical bounds · rate limits · inter-station";
                 two exits from the diamond — "dispose: apply flag" to a sky-blue
                 "flagged record" cylinder, and "reject" to a grey "rejection log" cylinder;
                 a separate sky-blue "provenance store" cylinder receives a dashed line from
                 both exits; a blue "scientist" head-and-shoulders icon oversees the diamond
- flow:          left-to-right — raw inputs → agent → proposals → rules diamond → two exits
                 (apply flag / reject) → flagged record and rejection log; provenance captured
                 from both exits; scientist positioned above the rules as accountable authority
- labels:        "raw inputs", "QC agent", "LLM", "plan – act – observe", "format reader",
                 "unit resolver", "neighbour query", "flag proposals (justified)",
                 "deterministic QC rules", "physical bounds · rate limits · inter-station",
                 "apply flag", "reject", "flagged record", "rejection log", "provenance store",
                 "scientist"
- annotations:   a small callout on the arrow from agent to diamond reading "proposals only —
                 no write access to data" in near-black
- caption:       Figure 6.1 — The propose–dispose architecture. The agent normalises inputs and proposes justified flags, but only deterministic rules, under a scientist's authority, dispose of each proposal; observations are flagged, never silently overwritten, and every decision is recorded to the provenance store.
- alt-text:      An architecture diagram. Three raw-input data cylinders feed a QC agent containing a language model, a plan–act–observe loop and three tools. The agent emits justified flag proposals into a deterministic QC-rules diamond overseen by a scientist. The diamond has two exits, apply-flag to a flagged-record store and reject to a rejection log, and both write to a separate provenance store. A callout notes that the agent has no write access to the data.
- generator prompt: A flat vector architecture diagram on an off-white background. On the
                 left, three stacked sky-blue cylinders labelled "raw inputs". An arrow leads
                 right into a medium orange-bordered rounded rectangle labelled "QC agent"
                 containing an orange box "LLM", a circular loop arrow "plan – act – observe",
                 and three small green glyphs labelled "format reader", "unit resolver",
                 "neighbour query". From the right edge of the agent an arrow labelled
                 "flag proposals (justified)" leads to a vermillion diamond labelled
                 "deterministic QC rules" with small type beneath reading
                 "physical bounds · rate limits · inter-station". The diamond has two exits:
                 an arrow "apply flag" to a sky-blue cylinder "flagged record", and an arrow
                 "reject" to a grey cylinder "rejection log". Dashed lines from both exits
                 reach a sky-blue cylinder "provenance store". A blue head-and-shoulders icon
                 labelled "scientist" sits above the diamond. A small near-black callout on
                 the proposals arrow reads "proposals only — no write access to data".
                 Minimal text, generous spacing, single-weight lines.
```

## 6.4 Worked example: river-gauge and rainfall quality control

The worked example puts the pattern to work on a concrete reconciliation: a set of river-gauge stage records and a co-located rainfall network, quality-controlled together so that the rainfall can later be used to explain or verify the flow **[AUTHOR: specify the catchment, the gauge and rainfall networks, the period, and the volume of records — the concrete scale is what makes the example land, exactly as the operational-morning detail does in Chapter 1]**. The pipeline has four stages, and the discipline of the chapter lives in the boundaries between them. In the first stage the agent ingests the heterogeneous formats, calling a declared reader for each source and normalising every series into a common tidy representation with explicit units, an unambiguous UTC timestamp, and an unpopulated flag column; this is the stage where the agent's format-wrangling strength pays off, and where a unit resolver is invoked on every column so that no quantity enters the record without a declared and checked unit — the single most important defence against the silent-unit failures that Chapter 13 anatomises. In the second stage the agent proposes flags: for each gap it proposes a classification (telemetry outage, sensor maintenance, recorded zero) with the neighbouring evidence it weighed, and for each candidate spike it proposes accept or reject with an explicit justification referencing the rainfall context — a stage jump coincident with a heavy-rainfall proposal is treated very differently from an isolated stage jump under a dry sky. Crucially, these proposals are written as structured objects beside the data, not into it. In the third stage the deterministic rules dispose: physical bounds reject any stage outside the gauge's rated range, a rate-of-change limit catches non-physical jumps the agent may have accepted, an inter-station consistency check tests each rainfall proposal against its neighbours, and the network's documented conventions have the final word. A proposal the agent made confidently but the rules reject is not applied; it is logged with its rejection reason, and the observation stands as measured. In the fourth stage every proposal, every disposition and every rejection is written to a provenance record keyed to the input files and the rule-set version, so that the state of the record is fully reconstructable — the mechanism developed in Chapter 12. The result [AUTHOR: report what the run actually produced — counts of proposed, applied and rejected flags, any error the deterministic rules caught that a manual pass had previously missed, and the wall-clock time against the manual baseline in §6.2] is not a "cleaned" dataset but a *flagged and audited* one, in which every departure from the raw observation is visible, justified and reversible. Figure 6.4 shows the three characteristic dispositions on a single joined trace: a spike accepted because rainfall supports it, a spike the agent found plausible but the rate-of-change rule rejects for want of any rainfall, and a gap flagged and left unfilled.

**Figure 6.2 — The four-stage QC sequence.** *A figure brief follows `FIGURES.md`; render in the house style.*

```
FIGURE BRIEF
- id:            Figure 6.2
- title:         Ingest, propose, dispose, record — one gauge-and-rainfall pass
- type:          sequence
- claim:         Each observation flows through four ordered stages with a hard boundary between the agent's proposals and the rules' disposition, and provenance is written at the end of every step.
- canvas:        16:9
- elements:      four vertical lanes read left-to-right as ordered stages, each headed by an
                 icon — stage 1 "ingest and normalise" (orange agent icon), stage 2
                 "propose flags" (orange agent icon), stage 3 "dispose" (vermillion gate
                 diamond), stage 4 "record provenance" (sky-blue cylinder); numbered arrows
                 carry an example datum across the lanes
- flow:          left-to-right, numbered 1–6: (1) raw series in; (2) normalise units and
                 timestamps; (3) propose gap/spike flags with justification; (4) rules apply
                 physical bounds and inter-station checks; (5) apply flag or reject to log;
                 (6) write proposal, disposition and reason to provenance
- labels:        "1 raw series", "2 normalise units + UTC", "3 propose flags + justification",
                 "4 physical bounds + inter-station", "5 apply flag / reject", "6 provenance",
                 "ingest and normalise", "propose flags", "dispose", "record provenance"
- annotations:   a vermillion vertical divider between stage 2 and stage 3 labelled
                 "authority boundary — agent proposes, rules dispose"
- caption:       Figure 6.2 — One quality-control pass over a joined gauge-and-rainfall record. The agent ingests, normalises and proposes; deterministic rules dispose; and every step writes to provenance. The vermillion divider marks the authority boundary the pattern never crosses.
- alt-text:      A left-to-right sequence in four lanes: ingest and normalise, propose flags, dispose, and record provenance. Six numbered steps carry a datum from raw series, through unit and timestamp normalisation, to justified flag proposals, then physical-bounds and inter-station disposition, then apply-or-reject, and finally a provenance write. A vermillion divider between the propose and dispose lanes is labelled the authority boundary.
- generator prompt: A flat vector sequence diagram on an off-white background, four vertical
                 lanes read left to right. Lane one headed by an orange rounded-square agent
                 icon labelled "ingest and normalise"; lane two by an orange agent icon
                 labelled "propose flags"; lane three by a vermillion diamond labelled
                 "dispose"; lane four by a sky-blue cylinder labelled "record provenance".
                 Numbered single-weight arrows cross the lanes in order: "1 raw series",
                 "2 normalise units + UTC", "3 propose flags + justification",
                 "4 physical bounds + inter-station", "5 apply flag / reject", "6 provenance".
                 A bold vermillion vertical line divides lane two from lane three, labelled
                 "authority boundary — agent proposes, rules dispose". Minimal text, generous
                 spacing, one arrowhead style.
```

**Figure 6.3 — Conventional QC and the agentic redesign.** *A figure brief follows `FIGURES.md`; render in the house style.*

```
FIGURE BRIEF
- id:            Figure 6.3
- title:         Manual scripts-and-eyes QC versus governed propose–dispose
- type:          before/after
- claim:         The redesign does not replace the deterministic checks; it removes the manual pattern-recognition and the missing audit trail, while leaving authority with the rules.
- canvas:        16:9
- elements:      top row "conventional" — a human icon (blue) cycling between a green
                 "per-format loaders" glyph, a green "hand-tuned checks" glyph and a
                 sky-blue "plot and eyeball" step, with a faded grey "reasoning lost in
                 comments" note; bottom row "agentic redesign" — a sky-blue inputs cylinder,
                 an orange "QC agent" proposing into a vermillion "deterministic rules"
                 diamond, a sky-blue "flagged record" cylinder and a sky-blue "provenance
                 store" cylinder; the deterministic-rules diamond is drawn identically in
                 both rows to show it is retained
- flow:          top row is a manual loop with no persistent record; bottom row is a
                 left-to-right governed flow ending in a flagged record and a provenance store
- labels:        "conventional", "per-format loaders", "hand-tuned checks", "plot and eyeball",
                 "reasoning lost in comments", "agentic redesign", "raw inputs", "QC agent",
                 "deterministic rules", "flagged record", "provenance store"
- annotations:   a near-black bracket linking the two "deterministic rules"/"hand-tuned
                 checks" elements labelled "same checks, same authority — retained"
- caption:       Figure 6.3 — Before and after. The conventional workflow's deterministic checks are kept unchanged; what the redesign adds is a format-wrangling, proposal-writing agent in front of them and a provenance store behind them, replacing manual pattern-recognition and lost reasoning rather than the rules themselves.
- alt-text:      A two-row before-and-after diagram. The top row shows a human cycling between per-format loaders, hand-tuned checks and a plot-and-eyeball step, with a faded note that reasoning is lost in comments. The bottom row shows raw inputs feeding a QC agent that proposes into a deterministic-rules diamond, then a flagged record and a provenance store. A bracket links the checks in both rows, labelled same checks, same authority, retained.
- generator prompt: A flat vector before-and-after diagram on an off-white background, two
                 stacked rows sharing a visual grammar. Top row labelled "conventional": a
                 blue human head-and-shoulders icon with curved arrows cycling between a green
                 "per-format loaders" glyph, a green "hand-tuned checks" glyph and a sky-blue
                 "plot and eyeball" box, plus a faded grey note "reasoning lost in comments".
                 Bottom row labelled "agentic redesign": a sky-blue "raw inputs" cylinder,
                 arrow to an orange "QC agent" rectangle, arrow labelled "propose" to a
                 vermillion "deterministic rules" diamond, then a sky-blue "flagged record"
                 cylinder and a sky-blue "provenance store" cylinder. A near-black bracket
                 links "hand-tuned checks" in the top row to "deterministic rules" in the
                 bottom row, labelled "same checks, same authority — retained". Minimal text,
                 generous spacing, single-weight lines.
```

**Figure 6.4 — An annotated gauge-and-rainfall trace.** *A figure brief follows `FIGURES.md`; render in the house style.*

```
FIGURE BRIEF
- id:            Figure 6.4
- title:         One trace, three dispositions — spike accepted, spike rejected, gap flagged
- type:          failure trace
- claim:         On a real joined trace the pattern is legible: a rainfall-backed spike is accepted, an unsupported spike the agent liked is rejected by the rules, and a gap is flagged but never filled.
- canvas:        16:9
- elements:      an upper line plot of river stage (near-black line) over time with three
                 marked events; a lower bar plot of co-located rainfall (sky blue) sharing the
                 time axis; event A a stage spike aligned with a tall rainfall bar, marked with
                 a green tick "flag: real event — accepted"; event B a stage spike under no
                 rainfall, marked with a vermillion cross "agent proposed accept — rule
                 rejected (no rainfall, exceeds rate limit)"; event C a gap in the stage line
                 marked with a grey band "flag: telemetry gap — left as observed, not filled"
- flow:          left-to-right along a shared time axis; annotations point from each marked
                 event to its disposition label
- labels:        "river stage", "rainfall", "A — accepted: rainfall-backed spike",
                 "B — rejected by rule: no rainfall, exceeds rate limit",
                 "C — gap flagged, not filled"
- annotations:   event B is the callout in vermillion — the agent's plausible-but-wrong
                 proposal caught by a deterministic rule; a small note reads
                 "fluent proposal, wrong — caught by physical rule"
- caption:       Figure 6.4 — A joined gauge-and-rainfall trace with three dispositions. Event A, a spike backed by heavy rainfall, is accepted; event B, a spike the agent found plausible but with no rainfall and an impossible rate, is rejected by a deterministic rule; event C, a telemetry gap, is flagged and left as observed. The vermillion callout marks where the rules catch a fluent but wrong proposal. [AUTHOR: replace the schematic events with three real ones from your record and give the actual disposition counts.]
- alt-text:      A two-panel time-series figure sharing a time axis. The upper panel plots river stage with three marked events; the lower panel plots co-located rainfall as bars. Event A, a stage spike aligned with a tall rainfall bar, is accepted. Event B, a stage spike with no rainfall beneath it, is rejected by a rule for exceeding the rate limit, marked in vermillion. Event C, a gap in the stage line, is flagged as a telemetry gap and left unfilled.
- generator prompt: A flat vector two-panel time-series figure on an off-white background
                 sharing one horizontal time axis. Upper panel: a near-black line labelled
                 "river stage" with three marked events. Lower panel: sky-blue vertical bars
                 labelled "rainfall". Event A is a stage spike aligned above a tall rainfall
                 bar, marked with a small green tick and labelled "A — accepted: rainfall-backed
                 spike". Event B is a stage spike above a flat, rainless stretch, marked with a
                 vermillion cross and labelled "B — rejected by rule: no rainfall, exceeds rate
                 limit", with a small near-black note "fluent proposal, wrong — caught by
                 physical rule". Event C is a break in the stage line spanned by a grey band
                 labelled "C — gap flagged, not filled". Minimal text, generous spacing,
                 single-weight lines and one arrowhead style.
```

## 6.5 Failure modes

The failure modes of this pattern are the reason its authority boundary is drawn so strictly, and three of them recur often enough to name. The first is the silent unit error, in which a quantity is read in one unit and treated as another — accumulation as rate, millimetres as inches, local time as UTC — and no exception is ever raised because every value remains a plausible number. This failure is dangerous in exact proportion to the model's fluency, because an agent asked to reconcile mixed sources will confidently produce a unified series in which the slip is invisible, and it is defeated only by making units explicit and machine-checked at ingest, so that a column without a declared, resolved unit cannot enter the record at all; the mechanism and a fuller anatomy of this class belong to Chapter 13, and this chapter's contribution is to place the check at the earliest possible point (high confidence). The second is plausible-but-wrong gap filling, in which the agent, asked to handle a gap, proposes an interpolated or model-inferred value that is physically reasonable and locally smooth and simply not what the instrument measured. The redesign forecloses this by construction: the agent may propose a *classification* of a gap but is never permitted to write a *value* into it, so a gap is flagged and left, and any filling that a later analysis requires is a separate, declared, reversible step under the scientist's authority rather than a quiet substitution buried in the QC pass (high confidence that the constraint is correct; the temptation to relax it is exactly what it guards against). The third is provenance loss, in which the flags and transformations are applied but the reasoning and the rule-set version are not recorded, so that a record which looks defensible cannot in fact be defended when questioned. This is the most insidious failure because it produces no wrong number at all — only an unauditable right one — and it is defeated only by treating the provenance write as a non-optional stage of the pipeline, keyed to inputs and rule versions, as Chapter 12 develops. Each of these failures shares a signature that recurs throughout the book: the output looks finished, and the fault is only visible against context the finished output has discarded.

## 6.6 Verification checklist

The following checks convert the pattern into something a group can operate and audit, and each is phrased so that a reviewer, not the agent, can confirm it.

- **No write access.** The agent can read and propose but cannot alter the observational record; every applied change is a flag, and every value substitution is a separate, declared step. Confirm by inspecting the tool interfaces, not the agent's prose.
- **Units resolved at ingest.** No column enters the common representation without a declared, machine-checked unit and an unambiguous UTC timestamp; unresolved units halt the pipeline rather than defaulting (see Chapter 13).
- **Deterministic rules retain authority.** Physical bounds, rate-of-change limits and inter-station checks are code the group wrote and can rerun identically; the agent's confidence never overrides a rule's rejection.
- **Proposals are justified and structured.** Every flag proposal carries its evidence, the neighbouring context considered, and a confidence, as a machine-readable object beside the data.
- **Rejections are logged, not discarded.** A proposal the rules reject is recorded with its rejection reason; the observation stands as measured.
- **Gaps are flagged, never silently filled.** No interpolated or inferred value is written into a gap during QC; filling is a downstream, reversible, declared step.
- **Provenance is complete and keyed.** Every proposal, disposition and rejection is recorded against the input files and the rule-set version, so the record's state is fully reconstructable (see Chapter 12).
- **Reproducible rerun.** Re-running the pipeline on the same inputs with the same rule-set version reproduces the same flags and the same provenance.

## 6.7 Repository pointer

The companion repository holds the runnable minimum of this pattern, kept current where the print stays deliberately coarse. Under `/patterns/ch06-data-qc` sits a small end-to-end example — heterogeneous input readers, a unit-resolution step, an agent that emits structured flag proposals, a deterministic rule set that disposes of them, and a provenance writer — reduced to the smallest form that still demonstrates the authority boundary **[AUTHOR: confirm the pattern directory name and the datasets shipped with it; ship a synthetic or openly licensed gauge-and-rainfall sample so the example runs without restricted data]**. The prompt that specifies the agent's proposal task lives under `/prompts`, the printable form of §6.6 under `/checklists`, and a sanitised version of the worked-example configuration under `/case-studies` **[AUTHOR: decide what of the real configuration can be shared, per the permissions position on record]**. Named tools, format libraries and any volatile figures are confined to the repository per the book's vendor-neutral convention; the print carries the pattern and its reasoning, and the repository carries the parts that date.
