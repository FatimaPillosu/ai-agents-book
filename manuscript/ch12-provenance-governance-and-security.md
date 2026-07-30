# Chapter 12 — Provenance, governance and security

> **Status:** draft r5 · voice v5.0 (`STYLE.md` §1) · sentence-per-line per `STYLE.md` §10 · figures as briefs per `FIGURES.md`.
> **Conventions:** vendor-neutral (outline §9) · **[AUTHOR: …]** marks lived material only the author can supply · **[verify]** marks real but unconfirmed details · citations drawn only from verified reports in `/research`. Nothing has been invented. Institution-specific thresholds are left as **[AUTHOR]** because local policy sets them.

> **[ai-reviewer: A1 review — 6 comments in this file.** All six tasks landed. The F2 correction is done properly and in three places: the offending sentence is gone, the **Definition — Audit trail** box no longer claims reproducibility, and `GLOSSARY.md` is fixed to match. §12.10 exists, is 688 words against a 620 budget, hooks explicitly to §12.9's unanswered question, and closes at moderate confidence with an explicit refusal to call the response standard, which is the right call. Both new AUTHOR markers are present and §12.11/§12.12 are renumbered. **The two most serious findings are the ordering language in the three-way distinction, which contradicts Chapter 11's own ladder, and an unauthorised cut in §12.8 that removed sourced content the plan told the writer to keep.** Also here: four short paragraphs in §12.10, a misdescription of the Five Eyes advisory, and a question about how the hypothetical case reads against this chapter's "nothing has been invented" header.**]**

---

## 12.1 Two obligations that travel together

Governance and security look like two different jobs.
In scientific practice they are the same job seen from two sides.

Governance asks whether the work can be trusted afterwards: whether a result traces back to its inputs, whether its assumptions can be recovered, and whether its reviewers can be named.
Security asks whether the work can be corrupted while it happens, by inputs that steer the agent, by credentials that leak, or by tools that reach further than the task needs.
Both reduce to one property already demanded of every instrument you operate: that its behaviour be bounded, recorded and accountable.
An uncalibrated sensor and an ungoverned agent fail in exactly the same way, producing readings that look like measurements and are not, and the discipline that answers the first answers the second.
So this chapter takes provenance and governance first, because they define what has to be recorded, then security, because it defines what has to be protected.
Both halves rest on one claim: trust in an agentic result is a property of the process that produced it, never of the output inspected on its own.

> **Definition — Provenance.** The traceable record of where a result came from: which inputs fed it, which version of the workflow ran, what the agent did at each step, and who signed off. Provenance is what lets someone reconstruct and defend a result months later, rather than relying on an assurance that it was "done carefully".

The tone here is deliberately unalarmed, because the risks in this chapter are ordinary operational-security risks scientific institutions have managed for decades under other names.
A data-handling agreement with a national meteorological service, a least-privilege account on a shared cluster, a laboratory notebook that survives a postdoc's departure: every one of those is a governance or security control that predates agents entirely.
The argument here is only that agentic workflows need the same controls, applied with the same seriousness and no more drama.
The one genuinely new element is that an agent reads and acts on untrusted text at machine speed, which changes how fast a small lapse spreads but not what kind of lapse it is.
So what follows is not a warning but a specification: what to record so the work survives scrutiny, and what to constrain so the work cannot be turned against the person running it.
Institution-specific thresholds, that is, which systems count as sensitive and which approvals are mandatory, are left as **[AUTHOR]** throughout, because they are set by local policy, not by this book.

## 12.2 Institutional memory as a first-class output

The most undervalued product of a governed agentic workflow is not its result but its record.
That record deserves to be designed, budgeted and maintained as a deliverable in its own right.

Scientific groups lose knowledge continuously through ordinary staff turnover.
A doctoral researcher spends three years calibrating a hydrological model, then leaves, and with them goes the tacit reasoning behind a hundred small decisions that never reached a paper: why one gauge was excluded, why a threshold sits where it does, which preprocessing step compensated for a known sensor fault.
Agentic workflows make this worse and can also be made to fix it.
Worse, because an agent can generate in an afternoon a volume of configuration, transformation and intermediate result that would take a successor weeks to reverse-engineer.
Better, because every decision an agent takes passes through a specification and a tool call, both machine-readable, both capturable with no extra human effort.
So treat the audit trail not as compliance overhead but as the institutional memory the group would otherwise lose, written continuously and for free as a by-product of how the work is done (high confidence in the principle; the effort saved is unquantified and will vary by group).

Documentation that survives turnover has a few properties that distinguish it from documentation that does not, and they are worth naming because they are the acceptance criteria for the record as a deliverable.
First, it is co-located with the artefact it describes, rather than held in a separate system the next person will never find.
Second, it records the assumption and its justification together, so a successor inherits not only what was decided but why.
Third, it is written at the moment of the decision, rather than reconstructed later when the reasoning has faded.
Fourth, it is legible to a human who was not present, which rules out raw logs as a sufficient record on their own.
An agentic workflow can be arranged to produce documentation with all four properties as a matter of course, because the specification (Chapter 3) states the why, the tool trace records the what, and a summarisation step, itself an agent task verified by a human, renders the two into prose a successor can actually read.
The limitation worth stating is that a record made this way is only as honest as the verification applied to it: an agent asked to summarise its own reasoning will produce a plausible account that may not match what actually happened, which is why the summary is an input to human review, never a substitute for it.

## 12.3 Registries: assumptions and uncertainties as standing records

An assumption registry is a standing, versioned record of every choice the workflow depends on but does not itself justify.
It is the governance artefact with the highest return in scientific work.

Every environmental analysis rests on assumptions that are invisible in its output: that a rating curve holds outside its calibration range, that a gap-filling method does not bias an extreme, that two datasets share a datum, that a unit is what a column header claims.
In conventional practice these assumptions live in a scientist's head and a scattering of code comments, and they are the first casualty of turnover and the commonest root cause in the failure gallery of Chapter 13.
An agentic workflow makes it practical to externalise them, because an agent instructed to surface its assumptions will list them at the point of use, and that list, once reviewed and corrected by a human, becomes a registry entry carrying the assumption, its justification, its confidence level, and the identity of whoever approved it.
The value is realised twice: once when the registry forces an assumption into the open where it can be challenged before it does damage, and again when a later result is questioned and the registry answers, in minutes, what the analysis assumed and who agreed to it (moderate confidence; the mechanism is sound but its adoption in environmental groups is not yet demonstrated at scale, so this is a designed practice, not a measured one).

> **Definition — Assumption registry.** A running list of every choice a workflow takes as given, each entry recording why it was assumed, how much confidence attaches to it, and who approved it. It turns assumptions that normally hide in someone's head and a few code comments into a record that can be challenged before it does damage and consulted after a result is questioned.

An uncertainty registry does the parallel job for quantities the workflow cannot pin down, and it inherits directly from the evidential discipline of Chapter 11.
Where the assumption registry records categorical choices, the uncertainty registry records the magnitude and provenance of what remains unknown: the observational error on an input, the spread of an ensemble, the sensitivity of a result to a parameter the agent chose, the residual after calibration.
The purpose is to prevent the characteristic failure of fluent automation, which is that uncertainty present in the inputs is quietly dropped as it passes through a chain of transformations, so the result arrives looking more precise than its provenance can support.
A registry that travels with the workflow forces each step to declare what it did to the uncertainty it received (propagated it, bounded it, or ignored it) and makes the final confidence statement auditable against a chain rather than asserted at the end.
The two registries together feed straight into the disclosure obligations of Chapter 9, because a manuscript's statement of limitations is exactly a human-authored synthesis of what the assumption and uncertainty registries recorded, and into the evaluation tiers of Chapter 11, because a claim's evidential tier is bounded by the uncertainties the registry admits.
This registry-and-audit apparatus is not a private eccentricity of the book: national risk-management guidance for generative AI is organised around the same cycle of governing, mapping, measuring and managing risk, and names the drift of uncertainty into overconfident output, "confabulation" in its terms, as a first-order risk to record and manage (NIST, 2024), which means a group that keeps these registries is speaking the language institutional risk officers already use.
The limitation is that a registry is only useful if it is consulted, and a registry the group treats as a filing obligation rather than a working document decays into exactly the compliance overhead this chapter argues it must never become.

## 12.4 Audit trails and reviewer coverage

An audit trail is the ordered, tamper-evident record of what the workflow actually did, and it differs from the registries by recording events rather than decisions.

Where a registry answers "what did the analysis assume", the audit trail answers "what happened, in what order, to what data, invoked by whom".
The two are complementary halves of a defensible record.

> **Definition — Audit trail.** A time-ordered, tamper-resistant log of everything the workflow did: which tool ran, on which inputs, producing which outputs, under which version, passed by which human. Registries record what was decided; the audit trail records what actually happened, so a result can be reconstructed and defended afterwards even where it cannot be run again.

The elements a scientific audit trail must capture are modest in number and stable across workflows: the specification version each run executed under, the identity and version of every tool called, the inputs consumed and outputs produced with content hashes sufficient to detect later alteration, the model and configuration in force, and the human decision points passed with the identity of whoever passed them.
A sixth element belongs with those five and is usually the missing one: the calibration state of every gate the artefact went through.
That means the gate's measured miss rate, the date of that measurement, and its validity window (Chapter 11 §11.5, on why a calibration expires rather than merely ageing).
Without it the record can say a gate passed the work and cannot say whether the gate was known to be working at the time.
Captured together, these convert the vague reassurance that a workflow was "carefully done" into a record a reviewer, an auditor or a successor can interrogate.
The architecture that carries this record is the subject of the first figure of this chapter, which shows the audit trail and the two registries as a governance layer sitting beside the workflow rather than inside it, fed by the same events the workflow generates for its own operation.

What that record does not do is let anyone run the work again and get the same answer.
Calling an explicable result reproducible gets the ordering backwards.
Explicable is the weaker of that pair, and it is the one an agentic workflow delivers.
**Reproducibility** is the strictest of the three properties at issue: the same workflow on the same inputs returns the same answer.
**Replicability** is the one science runs on: an independent group asks the same question by its own route and gets a compatible answer.
**Auditability** is the weakest: what was done can be reconstructed and defended afterwards, without necessarily being repeatable.
[ai-reviewer: the correction is right and the ordering language it is delivered in is not, which matters because getting an ordering right is the entire point of the passage.
"Strictest" and "weakest" are doing two different jobs in three consecutive sentences. Reproducibility is called the strictest, which is true in the sense of most demanding to satisfy: it requires bit-for-bit sameness. Auditability is called the weakest, which is true in the sense of least evidential value. Replicability sits between them on neither axis explicitly, described instead by what it is for. A reader takes away a single ranking, reproducibility above replicability above auditability, and that ranking is not what the book believes.
It contradicts Chapter 11 directly. §11.2 places independent-method corroboration — an independent determination by a route with a different error structure, which is replication — at Tier 5, second from the top, and argues it outranks Tier 4 precisely because it changes the measurement chain. Re-running the same workflow on the same inputs is closest to Tier 1, execution. So the ladder says replication is far stronger evidence than reproduction, and this paragraph implies the reverse. `GLOSSARY.md`'s new combined entry repeats the same wording and inherits the same problem.
The distinction itself is correct and worth having; it is the axis that needs naming. Separating "how demanding the property is to satisfy" from "how much evidential weight it carries" would let the paragraph say the true and useful thing, which is that agentic work fails the easiest of the three and can still reach the strongest through corroboration. Ai-writer's to redraft, and worth doing here and in the glossary together.]

An agentic workflow delivers the third, and it fails the first for two structural reasons.
The first is run-to-run variation.
The same specification and the same inputs can return different work on a second run.
So a check the workflow passed established something about that run rather than about the workflow (Chapter 11 §11.2, on why a tier claim rests on repeated runs).
The second is that the model behind a result can be withdrawn.
Once it is, the workflow cannot be re-run at all, and no amount of record-keeping restores that.

**[AUTHOR: if you have had a workflow become un-rerunnable because the model behind it was withdrawn, one sentence of that would anchor this better than the general statement.]**

> **Definition — Auditability.** The property of being reconstructable and defensible after the fact: what ran, on what, under which specification, passed by whom. It is what a provenance record delivers. It is weaker than reproducibility, because it does not let anyone repeat the work, and it is worth having anyway.

The constructive half of this sits in the architecture rather than in the record.
Deterministic components are reproducible in the strict sense, and the propose–dispose separation puts them in charge (Chapter 2 §2.6, on the three kinds of thing that may dispose).
Chapter 6's quality-control rules dispose of every agent proposal, and re-running them under the same rule-set version returns the same flags.
Chapter 14 §14.3 holds the verification core deterministic, keeping the model out of the measurement.
In both, the reproducible element is the one holding the authority, and the agent's contribution is auditable and nothing more.
So the honest claim is granular: name the reproducible components, and say plainly that the agentic step is auditable.

Saying that plainly is a credibility gain.
This readership has lived through the reproducibility crisis and knows the vocabulary for it.
A claim of reproducibility for work that cannot be re-run will not survive its first sceptical reader, and the smaller claim is the one that holds (high confidence).

Reviewer-coverage records are the part of the audit trail that documents scrutiny rather than execution, and they answer a question that turns acute the moment agents generate more output than humans can exhaustively check: what was reviewed, by whom, and what was not.
A reviewer-coverage record pairs each reviewable artefact (a block of generated code, a synthesised claim, a QC decision) with the reviewer who examined it, the depth of that examination, and its outcome, distinguishing an independent-agent review (Chapters 7 and 10) from a human review and recording both.
Its purpose is to make coverage explicit and therefore contestable, because the dangerous state in an agentic workflow is not the unreviewed artefact everyone knows is unreviewed but the one assumed to have been checked and was not.
A coverage record also supports honest disclosure, since a manuscript produced under Chapter 9's discipline can state truthfully which components passed independent review and which rest on author inspection alone, and it supports the evaluation of Chapter 11 by making the denominator of review coverage a measured quantity rather than an impression.
The limitation, stated plainly, is that a coverage record documents that review occurred, not that it was competent: a rubber-stamp review leaves the same record as a searching one, and no registry can substitute for a reviewing culture that takes the task seriously.
Chapter 11 §11.5 gives the measurement, seeded defects in a human reviewer's queue, and Chapter 13 §13.9 argues this is the commonest failure of the lot.
The two registries and these two records are also what a reader on the outside should be asking to see, and Chapter 17 turns them into questions a reviewer can actually put.

**Figure 12.1 — The governance layer: registries and audit trail beside the workflow.**

![On the left, a workflow running top to bottom: a specification, an AI agent, a tool call and a human decision. On the right, a governance layer holding four record stores: an assumption registry, an uncertainty registry, an audit trail and a reviewer-coverage record, each with a one-line note of the question it answers. One-directional arrows run from every workflow element into the layer, annotated that the workflow writes to the layer and the layer never steers the workflow, and that the records are fed by events the workflow already emits, at no extra effort. A bracket down the layer reads institutional memory, survives staff turnover.](../figures/figure-12-1.svg)

*Figure 12.1 — The record is a by-product, not a chore. Every element of the workflow already emits events, and the governance layer captures them into four standing records. Each answers a different question: what was assumed, what is uncertain, what happened, and what was actually reviewed. The arrows only point one way. The layer records; it never steers. (Rendered as `figures/figure-12-1.svg` from the brief below, per `FIGURES.md`.)*

```
FIGURE BRIEF
- id:            Figure 12.1
- title:         A governance layer that records without steering
- type:          architecture
- claim:         Provenance is captured by a standing governance layer that sits beside the workflow and is fed by the same events the workflow already emits.
- standfirst:    The workflow writes to the layer. The layer never steers the workflow.
- canvas:        16:9
- elements:      left, a vertical workflow stack — "specification" tag (blue), "AI agent"
                 (orange border), "tool call" glyph (green), "human decision" icon (blue);
                 right, a grey-bordered "governance layer" containing four sky-blue
                 cylinders: "assumption registry", "uncertainty registry", "audit trail",
                 "reviewer-coverage record"
- flow:          the workflow runs top-to-bottom on the left; thin one-directional arrows
                 lead rightward from each workflow element into the governance layer
- labels:        "specification", "AI agent", "tool call", "human decision",
                 "governance layer", "assumption registry", "uncertainty registry",
                 "audit trail", "reviewer-coverage record"
- annotations:   on the assumption registry, "what did the analysis take as given, and who
                 agreed?"; on the uncertainty registry, "what does the workflow not know,
                 and how much?"; on the audit trail, "what happened, in what order,
                 invoked by whom?"; on the coverage record, "what was actually reviewed —
                 and what was not?"; on the arrows, "fed by events the workflow already
                 emits — no extra effort"; a bracket down the layer, "institutional memory
                 — survives staff turnover"
- caption:       Figure 12.1 — The record is a by-product, not a chore. Every element of the workflow already emits events, and the governance layer captures them into four standing records. Each answers a different question: what was assumed, what is uncertain, what happened, and what was actually reviewed. The arrows only point one way. The layer records; it never steers.
- alt-text:      On the left, a workflow running top to bottom: a specification, an AI agent, a tool call and a human decision. On the right, a governance layer holding four record stores: an assumption registry, an uncertainty registry, an audit trail and a reviewer-coverage record, each with a one-line note of the question it answers. One-directional arrows run from every workflow element into the layer, annotated that the workflow writes to the layer and the layer never steers the workflow, and that the records are fed by events the workflow already emits, at no extra effort. A bracket down the layer reads institutional memory, survives staff turnover.
- infographic description: A flat vector architecture diagram, 16:9, off-white
                 background. Title top-left: "A governance layer that records without
                 steering". Standfirst: "The workflow writes to the layer. The layer never
                 steers the workflow." Left third: a vertical stack — blue tag
                 "specification", orange rounded rectangle "AI agent", green wrench "tool
                 call", blue human icon "human decision", joined by downward arrows. Right
                 two-thirds: a large grey-bordered rounded rectangle "governance layer"
                 containing four sky-blue cylinders in a column, each with its annotation
                 to the right: "assumption registry" / "what did the analysis take as
                 given, and who agreed?"; "uncertainty registry" / "what does the workflow
                 not know, and how much?"; "audit trail" / "what happened, in what order,
                 invoked by whom?"; "reviewer-coverage record" / "what was actually
                 reviewed — and what was not?". Thin one-directional arrows run from each
                 workflow element into the layer, sharing the note "fed by events the
                 workflow already emits — no extra effort". A bracket down the layer's
                 right edge reads "institutional memory — survives staff turnover".
                 Sentence case throughout.
```

## 12.5 Security as ordinary operational discipline

The security of an agentic workflow rests on three controls, all of which map onto long-standing practice.
Treat them as routine rather than exceptional.

The first governs the untrusted inputs an agent reads, because an agent ingesting external documents, web content or third-party data is acting on text an adversary may have written.
The second governs the credentials and data the agent touches, because an agent operating on institutional systems and high-performance computing holds, however briefly, the access rights of whoever launched it.
The third governs the tools the agent may call, because how much harm an agent can do is bounded by the narrowest set of permissions that still let it do the job.
None of these is novel: input validation, credential hygiene and least privilege are the elementary controls of every secured system, and the argument here is only that an agent is a system they apply to, not an exception that transcends them.
The community consensus list of the most critical risks in LLM applications, revised for 2025 specifically to reflect agentic systems, puts prompt injection at the top and names "excessive agency", that is, granting an application more tools, permissions or autonomy than its function requires, as a distinct top-ten risk in its own right (OWASP, 2025), which is the security profession's way of saying exactly what the three controls below say.
The sections that follow take each in turn, and the chapter's second figure draws the trust boundary the three controls jointly define: the line between what the agent is permitted to reach and what it is not.

## 12.6 Prompt injection: untrusted input as a steering channel

Prompt injection is what happens when untrusted content an agent reads gets treated as instruction rather than data.
It is the security concern most specific to agentic systems, because it exploits the very property that makes them useful.

At the model level, an agent does not distinguish between the instructions its operator gave it and the text it later reads from a document, a web page or a data file.
All of it arrives as language, and language saying "ignore your previous instructions and instead do X" gets processed as language.
This is not a quirk a better model patches away.
The paper that defined indirect prompt injection made the point architecturally: LLM-integrated applications blur the line between data and instructions, so anyone who can place text where an agent will later read it (a web page, a document, an email, a metadata field) can attempt to hijack the agent without ever touching the operator's prompt (Greshake et al., 2023).

> **Definition — Prompt injection.** When text an agent reads as part of its work (a web page, a downloaded file, a colleague's document) contains instructions, and the agent obeys them as if they came from its operator. The agent cannot reliably tell "content to analyse" from "orders to follow", so, in effect, the data can direct the agent.

For an environmental workflow this is not hypothetical, because the agents in this book's patterns routinely read material the group did not write: a paper retrieved for synthesis (Chapter 5), a data description fetched from a partner portal (Chapter 6), a web page consulted for a parameter value, a file handed over by a collaborator.
Any of those can carry, by malice or by accident, text an agent will act on: an instruction to exfiltrate a credential, to alter a QC threshold, to insert a fabricated citation (Chapter 13), or to write to a path it should not touch.
How bad an injection is depends not on the text but on what the agent can do once steered.
That is why the defence is never to detect all malicious text, which is unwinnable because the model reads natural language and natural language is unbounded.
The defence is to constrain what any instruction, however it arrives, is able to accomplish.
That framing is not an improvisation of this book; it is where the security literature has landed.
Given that prompt injection cannot currently be solved at the model level, recent work proposes architectural patterns that give resistance by construction, each trading some agent capability for safety: fixing the plan before untrusted data is read so the data cannot redirect it, having the model emit a checkable program rather than take direct action, or splitting a privileged tool-using model from a quarantined model that reads untrusted text but holds no tools (Beurer-Kellner et al., 2025).
This book has high confidence in the vulnerability class being durable and the constraint-based response being the right one; specific historical exploits are patched routinely, but the underlying data–instruction conflation is unresolved by any current model.

The defences that follow are architectural rather than detective, they compound, and several are patterns the book already prescribes under other names.

The primary defence is least privilege, treated in §12.8.
An agent that cannot delete files or reach the open internet cannot be made to do either by an injected instruction, however cleverly phrased, because the capability was never granted.
The second is a firm separation between the channel carrying instructions and the channel carrying data, so content retrieved from an untrusted source reaches the agent as quoted material to analyse rather than as instruction to follow.
That reduces the risk without eliminating it, because the boundary is enforced by convention rather than by a hard mechanism the model cannot cross, which is exactly why the stronger design patterns above fix the plan or quarantine the reader instead of trusting the convention.
The third is a human gate on any consequential action: an agent may propose to send an email, write to a shared system or run an irreversible command, but the action waits on a human who sees the proposal in context.
The fourth is provenance.
An audit trail (§12.4) recording what the agent read and when makes an injection traceable afterwards, which both helps recovery and discourages careless introduction of untrusted content.
State the limitation: no combination of these fully closes the channel while agents read natural language at all.
The residual risk is managed the way other irreducible risks are, by keeping the possible damage small rather than pretending it is zero.
**[AUTHOR: an injection you encountered or deliberately tested — even a benign one, such as a comment in a shared config that an agent acted on — would ground this section in lived practice.]**

## 12.7 Credentials and data when agents touch institutional systems

Credential and data handling has the highest stakes in institutional science, because an agent operating on shared systems inherits real access to real infrastructure.

When an agent runs a job on a high-performance cluster, queries an operational database, or writes to a group's shared storage, it does so with credentials granting the launching scientist's rights.
Mishandle those credentials, by logging them in a trace, embedding them in generated code, or transmitting them to a model provider as part of a prompt, and a convenience becomes an exposure.
The disciplines that contain this are again drawn from ordinary practice and simply applied with care to a new kind of operator.
Supply credentials through the environment or a secrets manager rather than writing them into specifications, prompts or code, so they never enter material an agent might log or transmit.
Scope them to the task, so a data-retrieval agent holds read access to one dataset rather than write access to a filesystem.
And make them short-lived where the infrastructure supports it, so a leaked token expires before it can be widely abused.
The corresponding discipline for data is to keep sensitive inputs on systems the group controls and to be explicit about what leaves them, because the moment a dataset is placed in a prompt it may traverse a third-party model provider, with implications for data-sharing agreements that a national service or a commercial partner may enforce, a point that connects directly to the data-sovereignty design of Chapter 14, which treats the case where observations cannot be shared at all.

The institutional dimension of this concern is that scientists rarely own the systems their agents touch, so the controls above have to be reconciled with policies set by others.
A group running agents against a shared cluster operates under the cluster's acceptable-use policy, its data-classification scheme and its authentication regime, and an agentic workflow that ignores these will be, rightly, refused access or shut down.
The productive response is to design the workflow to fit the institution's existing controls rather than to seek exceptions from them: to run within the account and quota already granted, to classify the data the workflow handles against the institution's existing scheme, and to document the flow of credentials and data so it can be reviewed against policy before it runs.
The confidentiality logic here is the same one major funders already apply to their own processes, since one has prohibited reviewers from putting grant material into online AI tools precisely because the reviewer cannot control where the data then goes (Chapter 9), and material whose onward use cannot be controlled simply must not enter a third-party model service.
Where an institution's specifics govern, that is, which data classes may reach an external model, which systems require multi-factor authentication for automated access, and what retention applies to an audit trail, these are decisions local policy makes and this book cannot, and they are marked **[AUTHOR]** accordingly.
The limitation is that policies vary widely and change, so the durable guidance is the principle, namely to treat an agent's access as the scientist's own access and handle it with the same care, rather than any particular rule, which will differ between a university, a national laboratory and an operational forecasting centre.

## 12.8 Least privilege and the trust boundary

Least privilege means giving an agent the narrowest set of tool permissions that still lets it finish its task.
It is the single most effective security control available, because it bounds the harm of every other failure at once.

An agent restricted to reading a named directory and running a test suite cannot exfiltrate data, cannot write to production systems, and cannot be steered into doing either by an injected instruction.
Not because such instructions get detected, but because the capability to obey them was never granted.

> **Definition — Least privilege.** An agent is given the narrowest access that still lets it do the job and nothing more: read one named folder, run one named tool, reach no further. A mistake, a bug or a hostile instruction can then do damage only inside those narrow limits, because the power to do worse was never handed over in the first place.

Applying the principle in practice means enumerating, before a workflow runs, exactly which tools the agent may call and with what scope: which paths it may read and which it may write, whether it may reach the network and to which hosts, which credentials it may use, and which actions require a human gate rather than proceeding on their own.
This enumeration is itself a governance artefact, belonging in the specification (Chapter 3) and recorded in the audit trail (§12.4), and it has the useful side effect of forcing the workflow's designer to articulate what the agent actually needs, a question that often reveals a broad permission was requested out of convenience rather than necessity, the "excessive agency" the security profession warns against (OWASP, 2025).
The institutional vocabulary has kept pace with the move to agents: alongside the top-ten risks for LLM applications already cited, a companion top-ten now exists for agentic applications specifically, effectively expanding that single "excessive agency" category into a full agent-specific risk list once a system takes autonomous, credentialed, multi-step action (OWASP, 2026).
The default posture is deny-by-default: the agent starts with no access and is granted each capability deliberately, rather than starting broad and being pared back, because the failures of omission in the first posture are safe and the failures of omission in the second are exposures (high confidence; this is standard security practice applied unchanged to agents).
Practitioner guidance has arrived independently at the same posture, drawing its permission tiers around the consequence of an action rather than around any model's current capability (practitioner commentary; see the references).
Models change; the permission gradient should not.
[ai-reviewer: an unauthorised cut, and the one place in the pass where a chapter lost content the plan explicitly protected. Task 12.3(a) authorised deleting exactly one thing from §12.8: the general derivation of why a proposed consequential action waits on a human. It said everything security-specific stays in full. What actually went was the substance of the cited practitioner guidance, namely the three permission bands — fully autonomous only where low-stakes and reversible, propose-then-approve in the middle, never autonomous at the top. The citation survives and the finding it carried does not, which leaves a source supporting a vaguer claim than it made. That is worse than cutting the sentence outright, because a reader cannot tell what the guidance actually said.
There is an irony worth naming, because it shows what went wrong. The deleted "propose-then-approve" band was §12.8's own named instance of the propose–dispose separation. So a task whose purpose was to point §12.8 at the general principle deleted the local instance the general principle exists to generalise, and then added a cross-reference to it further down. The paragraph now has the pointer and not the thing.
Separately in the same edit: the trust-boundary sentence lost "(writing to shared systems, sending communications, running irreversible commands)" and gained "any action whose consequences reach outside the boundary". Those three examples were security-specific, concrete and protected by the plan, and the replacement is more abstract than what it replaced, which is the direction `STYLE.md` §12.1(e) tells the author to reverse. Restoring both is ai-writer's, and the plan's discrepancy rule says a cut that would break an argument is raised in the PR rather than made silently.]

The trust boundary is the line this enumeration draws, and making it explicit is the purpose of the chapter's second figure.
On the trusted side sit the agent, its specification and the tools it may call.
On the untrusted side sit the external documents and data it reads, together with any action whose consequences reach outside the boundary.
Drawing the boundary explicitly clarifies where each defence belongs: input validation and the instruction–data separation live where untrusted content crosses inward, least privilege lives at the tools the agent may call, and the human gate lives where a proposed action would cross outward into consequence.
That outward gate is the propose–dispose separation of Chapter 2 §2.6, with a person as the disposer.
The boundary is also what institutional IT will ask to see, because it is the artefact that answers their questions directly, and the closing section turns to those questions.
The limitation of least privilege is operational rather than conceptual.
Permissions that are too narrow make a workflow fail in ways that tempt you to grant broad access just to make the failure go away.
Resisting that, meaning diagnosing the specific missing permission rather than opening the boundary, is a discipline the tooling can support but cannot enforce.

**Figure 12.2 — The trust boundary: what the agent may reach, and what waits on a human.**

![A central trusted zone holds the AI agent, its specification and a small set of permitted tools marked least privilege, deny by default. To the left, outside the boundary, three untrusted sources, external documents, web content and third-party data, enter only through a validation gate annotated quoted as data to analyse, never instructions to follow. To the right, three consequential actions, writing to a shared system, sending a communication and running an irreversible command, sit outside the boundary and are reachable only through a human gate annotated the agent proposes, a person disposes. The boundary itself is annotated as the artefact institutional IT will ask to see. A footer reads that an injected instruction can only do what the granted tools allow, which is why least privilege is the primary defence.](../figures/figure-12-2.svg)

*Figure 12.2 — The line that decides what an attack can accomplish. Untrusted text enters only as quoted data, the agent holds the narrowest tool set that still does the job, and anything consequential leaves only through a human gate. Draw this boundary explicitly: it is what bounds an injected instruction to the capabilities you actually granted, and it is the artefact your security team will ask to see. (Rendered as `figures/figure-12-2.svg` from the brief below, per `FIGURES.md`.)*

```
FIGURE BRIEF
- id:            Figure 12.2
- title:         Least privilege and the trust boundary
- type:          architecture
- claim:         Security is bounded by drawing an explicit trust boundary: untrusted inputs enter through validation, the agent holds only the narrowest tool permissions, and any consequential action waits on a human gate.
- standfirst:    An injected instruction can only do what the granted tools allow.
- canvas:        16:9
- elements:      a central grey-bordered rounded rectangle "trusted zone" containing an
                 "AI agent" (orange border), a "specification" tag (blue) and "permitted
                 tools" glyphs (green) with a lock annotation; left, three untrusted
                 sources (grey): "external documents", "web content", "third-party data",
                 entering through a vermillion validation gate; right, three consequential
                 actions outside the zone: "write to shared system", "send communication",
                 "irreversible command", reachable only through a blue human gate
- flow:          left-to-right — untrusted sources pass through the validation gate into
                 the zone as data; the agent calls only permitted tools; proposed
                 consequential actions exit rightward only through the human gate
- labels:        "trusted zone", "AI agent", "specification", "permitted tools",
                 "least privilege", "external documents", "web content",
                 "third-party data", "validate · quote as data", "write to shared system",
                 "send communication", "irreversible command", "human gate"
- annotations:   on the validation gate, "quoted as data to analyse — never instructions
                 to follow"; on the permitted tools, "deny by default — each capability
                 granted deliberately"; on the human gate, "the agent proposes; a person
                 disposes"; on the boundary, "the artefact institutional IT will ask to
                 see"; a footer, "an injected instruction can only do what the granted
                 tools allow — least privilege is the primary defence"
- caption:       Figure 12.2 — The line that decides what an attack can accomplish. Untrusted text enters only as quoted data, the agent holds the narrowest tool set that still does the job, and anything consequential leaves only through a human gate. Draw this boundary explicitly: it is what bounds an injected instruction to the capabilities you actually granted, and it is the artefact your security team will ask to see.
- alt-text:      A central trusted zone holds the AI agent, its specification and a small set of permitted tools marked least privilege, deny by default. To the left, outside the boundary, three untrusted sources, external documents, web content and third-party data, enter only through a validation gate annotated quoted as data to analyse, never instructions to follow. To the right, three consequential actions, writing to a shared system, sending a communication and running an irreversible command, sit outside the boundary and are reachable only through a human gate annotated the agent proposes, a person disposes. The boundary itself is annotated as the artefact institutional IT will ask to see. A footer reads that an injected instruction can only do what the granted tools allow, which is why least privilege is the primary defence.
- infographic description: A flat vector architecture diagram, 16:9, off-white
                 background. Title top-left: "Least privilege and the trust boundary".
                 Standfirst: "An injected instruction can only do what the granted tools
                 allow." Centre: a large grey-bordered rounded rectangle "trusted zone",
                 annotated on its border "the artefact institutional IT will ask to see",
                 containing a blue tag "specification", an orange rounded rectangle "AI
                 agent", and three green wrench glyphs "permitted tools" with a small lock
                 and the note "deny by default — each capability granted deliberately",
                 headed "least privilege". Left of the zone: three grey boxes stacked,
                 "external documents", "web content", "third-party data", their arrows
                 converging on a vermillion diamond "validate · quote as data" on the
                 boundary, annotated "quoted as data to analyse — never instructions to
                 follow". Right of the zone: three grey boxes, "write to shared system",
                 "send communication", "irreversible command", reachable only through a
                 blue human icon "human gate" on the boundary, annotated "the agent
                 proposes; a person disposes". Footer: "an injected instruction can only
                 do what the granted tools allow — least privilege is the primary
                 defence". Sentence case throughout.
```

## 12.9 What institutional IT will ask before an agent runs

Institutional IT and information-security teams will ask a predictable set of questions before an agentic workflow runs on their infrastructure.
If you can answer them from your governance artefacts, you will get access far more readily than a group that cannot.

The questions are the same ones an IT team would ask of any new system, reframed for an operator that acts on its own.
What data will the workflow touch, and how is it classified?
Where does that data go, and does any of it leave institutional systems for an external model provider?
What credentials does the agent hold, and how are they scoped, stored and rotated?
What can the agent do, meaning its full set of tool permissions, and what stops it doing more?
Who is accountable for its actions, and how is a mistake detected, contained and reversed?
And what record is kept of what it did?
Each of these maps directly onto an artefact this chapter has already specified: data classification and flow onto §12.7, credential scoping onto §12.7, tool permissions onto the least-privilege enumeration of §12.8, detection and recovery onto the audit trail of §12.4, and accountability onto the human decision points recorded throughout.
It helps that these questions have a shared external vocabulary: the OWASP top-ten risks for LLM applications give security teams names they already use (prompt injection, excessive agency, sensitive-information disclosure, improper output handling; OWASP, 2025), and national risk-management guidance frames the whole exercise as governing, mapping, measuring and managing risk (NIST, 2024), so a workflow whose governance layer answers in that language is legible to the people who must authorise it.
The practical consequence is that a governed workflow is also an approvable one, because the same records that make a result trustworthy make the workflow legible to the people who must sign it off (moderate confidence; the mapping is sound in principle, but institutional review processes vary and some will ask for more, such as a formal data-protection impact assessment, a security review, or a named information-asset owner, that only local policy defines).

The guidance a group can point to has grown much more specific, and that makes the conversation with institutional IT easier to have.
In 2026 six national cyber-security agencies across five countries issued the first coordinated guidance addressed to agentic AI specifically, cataloguing risks across privilege, design, behavioural, structural and accountability categories **[verify: any risk-category or best-practice detail beyond this summary against the primary advisory PDF]**, and its verified recommendations read almost like a précis of this chapter.
It gives four recommendations: begin with tightly bounded, low-risk pilots; apply least privilege with time-limited, temporary credentials rather than long-lived ones; monitor behaviour continuously; and name a specific human as accountable before deployment, because an agent that cannot be understood, monitored or contained is not ready to run (Five Eyes joint advisory, 2026; NCSC-UK, 2026).
The same year, the US standards body opened an agent-specific standards initiative covering interoperability and, the part institutional IT will press hardest, agent identity and authorisation: which credentials an agent holds, and how a system verifies which agent is acting when one acts (NIST CAISI, 2026, cited for the initiative's existence and stated scope only).

The constructive posture towards institutional IT is to arrive with these answers rather than wait to be asked for them, and to treat the security team as a partner in adoption rather than an obstacle to it, a theme taken up in Chapter 16, where institutional adoption is addressed directly.
A short, honest description of a workflow's data flows, credentials, permissions and audit record, prepared before approval is sought, does more to accelerate adoption than any assurance of the technology's capability, because it speaks to the team's actual responsibility, which is risk rather than novelty.
Where an institution has no policy for agentic systems yet, a common situation at the time of writing, the group proposing the first such workflow has both an opportunity and an obligation to help shape a sensible one, by mapping the new operator onto the controls the institution already applies to human users and shared services rather than requesting a special regime for it.
The specifics of any given institution's requirements, that is, its approval thresholds, its mandatory reviews, its data-classification scheme and its retention rules, are set locally and are marked **[AUTHOR]** here, because a book cannot supply them and should not pretend to.
The durable point is that governance and security are not the price of using agents in science.
They are the condition under which using them is scientific at all.
An instrument whose behaviour is unbounded, unrecorded and unaccountable is not one you should trust, and the discipline that makes an agent trustworthy is the same discipline, applied to a new tool, that has always separated measurement from guesswork.

## 12.10 When a gate is found to have been wrong

[ai-reviewer: two comments on the section as a whole, placed here at its head.
First, on how the opening reads against the chapter's own header. This chapter states "Nothing has been invented", and the section opens on a specific scenario carrying specific quantities: eight months, two of twenty seeded faults, all twenty caught last time. The second person makes it hypothetical to a careful reader, and the AUTHOR marker at the foot of the section confirms it is not lived. Neither of those is visible at the point of reading. The same pattern appears in the new §2.6, §3.7 and §17.4 openings, and it is the direct consequence of `STYLE.md` §1's instruction to let the concrete case lead, so it is not a drafting error — but this book's whole subject is the difference between an account of what happened and an account that reads like one, and it should not be the one book where a reader has to work that out. A house convention for marking a constructed illustration would settle it once for all four sections. That is ai-editor's to set, not a fix to this paragraph.
Second, paragraph rhythm. The section's eight prose paragraphs measure 102, 74, 56, 117, 70, 105, 76 and 88 words, so four fall below `STYLE.md` §2's 80–200 band and one is at 56. Detection, containment, notification and the evaluation-set movement are each treated in fewer words than the section's own opening scenario, which inverts the emphasis: containment gets 56 words and gets the strongest line in the section ("The wrong outputs are the evidence"). The material is right and the sequence is right; several of these movements are compressed below the weight the argument gives them. Ai-writer's to rebalance.]
You re-calibrate a citation gate that has run untouched for eight months, and this time it misses two of the twenty seeded faults.
Last time it caught all twenty.
Nothing about the gate looks different, and nothing in the record flagged a change.
Every artefact that passed through that gate since the last calibration is now of unknown status.
§12.9 records the question institutional IT asks and this chapter has left open: how is a mistake detected, contained and reversed?
For a book grounded in operational forecasting, the hour after a discovery like that is where governance is tested rather than described.

Four things tend to bring it to light.
A scheduled re-calibration finds it, as above.
A yield collapse shows it, where a gate that used to reject things has stopped rejecting anything.
A corroborating method disagrees, which is Tier 5 of Chapter 11 §11.2 doing the job the ladder puts it there for.
Or a downstream user complains, which is the uncomfortable one: most of the time you find out because somebody else noticed.

Stop the workflow before diagnosing it.
Diagnosing first is the expensive instinct, because every run made while you diagnose adds to the set of artefacts you will have to assess.
Quarantine the outputs rather than deleting them.
The wrong outputs are the evidence: they tell you which fault classes got through, and when the behaviour changed.

Scope is where this chapter's apparatus either pays for itself or turns out not to exist.
The audit trail answers which artefacts passed through the affected gate and when (§12.4).
The reviewer-coverage record answers which of those had a second, independent check that might have caught the fault anyway.
The tier record answers which claims were resting on that gate at all, since a claim that never invoked it is unaffected.
Together the three bound the damage to a list you can work through.
A group without them cannot bound anything, and its only defensible position is that everything since the last known-good calibration is suspect.
That is almost always far more work than the incident deserved.

Who gets told follows from who relied on the work.
Collaborators whose results sit downstream come first, because they may still be able to stop something.
Partners who supplied data under conditions come next, where those conditions bear on the handling.
An operational customer comes in wherever a decision was informed by an affected output.
The thresholds are institutional rather than scientific, and this book does not set them **[AUTHOR]**.

Metrology has recall, meaning a manufacturer can call back every affected unit and say publicly why.
Science has errata, a corrected dataset version, or a note attached to the record, and all three are slower and weaker than that.
An erratum reaches a fraction of the original's readers, and a corrected dataset does nothing for anyone still on the old one.
A published result gated by a check now known to be miscalibrated is the hardest case here, and no clean answer exists.
The decision to correct the record is the author's, not the workflow's, and it turns on what the result now rests on.

Every incident is a case for the evaluation set.
The fault class the gate missed becomes a seeded case in the standing set (Chapter 11 §11.4, on building an evaluation set from the group's own work).
So the same miss is caught next time rather than discovered.
It also becomes an entry in the failure log.
And a gate that has failed once carries a shorter validity window, because its measured record now includes a failure.

No established procedure exists for retracting or correcting an agentic result, and saying otherwise would be inventing a consensus.
So this is a response I think is right rather than one a community has settled (moderate confidence).
The precondition is settled, though: national cyber-security guidance already asks that a specific human be named as accountable before an agentic system is deployed (Five Eyes joint advisory, 2026).
[ai-reviewer: the claim is accurate and traceable — §12.9 above already carries it from the same source, and the `/research` entry supports it — but "national" misdescribes what the source is. It is a joint advisory of six national agencies across five countries, which is why §12.9 attributes it to the six by name and why Ch. 16 §16.2 calls the same source "multi-national security guidance". "National" makes a six-nation instrument sound like one country's rule, which understates exactly the weight the sentence is reaching for. A one-word fix, and worth making because this is the sentence that carries the section's only external warrant.]
Naming that person after an incident is too late, and every step above assumes somebody whose job it is to take them.

**[AUTHOR: a gate of yours that turned out to have been miscalibrated, or the nearest thing to it — what you found, how far back it reached, and what you had to tell whom. This section is the one in the chapter most obviously missing lived material.]**

## 12.11 Verification checklist

This checklist certifies that an agentic workflow is governed and secured well enough to be trusted and approved.
A colleague who did not build it, or an institutional reviewer, should be able to apply it from the record alone.

- **Registries exist and are current.** The assumption and uncertainty registries are present, versioned, and reflect the workflow as it actually runs, each entry carrying its justification, confidence level and approver (§12.3); a reviewer can find an assumption and see who agreed to it.
- **The audit trail reconstructs any artefact.** For any output, the trail recovers who and what produced it, in what order, under which specification and model version, with content hashes sufficient to detect later alteration (§12.4).
- **Reviewer coverage is recorded.** Each reviewable artefact is paired with its reviewer, the depth of review and the outcome, distinguishing independent-agent from human review, so coverage is explicit and contestable rather than assumed (§12.4; Chapters 7, 10).
- **Least privilege confirmed at the interface, not in prose.** The agent's tool permissions are verified by inspecting what the tools actually allow (paths, network, credentials, gated actions), not by trusting the agent's or the specification's description of them (§12.8); deny-by-default is the starting posture.
- **Prompt-injection surface reviewed for every input channel.** Every channel that feeds untrusted content into agent context (retrieved papers, partner data, web pages, collaborator files) has been identified and constrained by architecture (least privilege, instruction–data separation, human gates), not by hoping to detect malicious text (§12.6).
- **Credentials and partner data handled per institutional policy.** Credentials reach the agent only through the environment or a secrets manager, are task-scoped and short-lived where supported, and no data leaves institutional systems for an external model against a data-sharing agreement (§12.7); institution-specific rules are recorded **[AUTHOR]**.
- **Accountability and recovery are named.** A specific human is accountable for the workflow's actions, and the record shows how a mistake is detected, contained and reversed (§12.4, §12.9). The group also has a stated response to a gate found to have been wrong, including how the affected artefacts would be identified from the audit trail and who would be told (§12.10).
- **Documentation survives staff turnover.** A newcomer who was not present can operate the workflow and defend its results from the record alone, the true test of whether the governance layer is real or decorative (§12.2).

## 12.12 Repository pointer

The companion repository holds the runnable and perishable counterparts to this chapter under `/patterns/ch12-provenance-governance-and-security`, with the printable checklist under `/checklists`.
The material is a set of templates rather than a single program: an assumption-registry and uncertainty-registry schema, an audit-trail record format with the fields of §12.4, a reviewer-coverage template, and a least-privilege tool-permission manifest that a workflow's specification (Chapter 3) can instantiate.
Named products, current institutional-security specifics and any volatile figures are confined to the repository per the book's vendor-neutral convention, so the print chapter states the principles while the repository tracks the parts that date **[AUTHOR: confirm the repository paths and contents once the registry and audit-trail templates are finalised; record any secrets-manager or institutional-authentication dependencies]**.

---

### References

Report-sourced references carry a DOI or URL and are drawn from the verified sweep in `/research`.

- Beurer-Kellner, L., Buesser, B., Creţu, A.-M., Debenedetti, E., Dobos, D., Fabian, D., Fischer, M., et al. (2025). Design patterns for securing LLM agents against prompt injections. Preprint: https://arxiv.org/abs/2506.08837 [verify venue before release]
- Greshake, K., Abdelnabi, S., Debenedetti, E., et al. (2023). Not what you've signed up for: compromising real-world LLM-integrated applications with indirect prompt injection. *Proceedings of the 16th ACM Workshop on Artificial Intelligence and Security (AISec '23)*. DOI: 10.1145/3605764.3623985. Preprint: https://arxiv.org/abs/2302.12173
- National Institute of Standards and Technology (2024). Artificial intelligence risk management framework: generative artificial intelligence profile. NIST AI 600-1, July 2024. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- National Institute of Standards and Technology, Center for AI Standards and Innovation (2026). Announcing the AI Agent Standards Initiative for interoperable and secure innovation, 17 February 2026. https://www.nist.gov/news-events/news/2026/02/announcing-ai-agent-standards-initiative-interoperable-and-secure — programme page: https://www.nist.gov/artificial-intelligence/ai-agent-standards-initiative **[verify: cited for the initiative's existence and stated scope only; the promised agent-specific security-control overlays are not yet published or verified against a NIST primary source]**
- OWASP GenAI Security Project (2025). OWASP Top 10 for LLM Applications 2025. https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/
- OWASP GenAI Security Project (2026). OWASP Top 10 for Agentic Applications for 2026. https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ **[verify: the individual agentic-risk category names and numbering against the primary document before naming any in print]**
- Five Eyes joint advisory — National Cyber Security Centre (UK), Cybersecurity and Infrastructure Security Agency (US), National Security Agency (US), Australian Signals Directorate's Australian Cyber Security Centre, Canadian Centre for Cyber Security and National Cyber Security Centre New Zealand (2026). Careful adoption of agentic AI services (joint advisory, 30 April 2026), with the NCSC-UK companion blog, Thinking carefully before adopting agentic AI (15 May 2026). https://www.ncsc.gov.uk/blogs/thinking-carefully-before-adopting-agentic-ai — joint advisory: https://media.defense.gov/2026/Apr/30/2003922823/-1/-1/0/CAREFUL%20ADOPTION%20OF%20AGENTIC%20AI%20SERVICES_FINAL.PDF **[verify: risk/best-practice-catalogue detail beyond the summary against the primary advisory PDF]**
- AI Founders (2026). "Don't Build an AI Agent Until You Can Answer These 8 Questions." Video, @aifoundershq, 17 May 2026. https://www.youtube.com/watch?v=jMHawg6qpps (practitioner commentary; concepts cited as corroboration, not evidence)
