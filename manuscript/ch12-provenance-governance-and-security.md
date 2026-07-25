# Chapter 12 — Provenance, governance and security

> **Status:** draft r3 · voice v3.3 (`STYLE.md`) · sentence-per-line per `STYLE.md` §10 · figures as briefs per `FIGURES.md`.
> **Conventions:** vendor-neutral (outline §9) · **[AUTHOR: …]** marks lived material only the author can supply · **[verify]** marks real but unconfirmed details · citations drawn only from verified reports in `/research`. Nothing has been invented. Institution-specific thresholds are left as **[AUTHOR]** because local policy sets them.

---

## 12.1 Two obligations that travel together

Governance and security look like two different jobs, and in scientific practice they are the same job seen from two sides.
Governance asks whether the work can be trusted after the fact: whether a result traces back to its inputs, whether its assumptions can be recovered, and whether its reviewers can be named.
Security asks whether the work can be corrupted during the fact, by inputs that steer the agent, by credentials that leak, or by tools that reach further than the task needs.
Both questions reduce to a single property already demanded of every instrument a scientist operates: that its behaviour be bounded, recorded and accountable.
An uncalibrated sensor and an ungoverned agent fail in exactly the same way, producing readings that look like measurements and are not, and the discipline that answers the first answers the second.
This chapter therefore treats provenance and governance first, because they define what must be recorded, and security second, because it defines what must be protected; the two halves share one spine, which is that trust in an agentic result is a property of the process that produced it and never of the output inspected alone.

> **Definition — Provenance.** The traceable record of where a result came from: which inputs fed it, which version of the workflow ran, what the agent did at each step, and who signed off. Provenance is what lets someone reconstruct and defend a result months later, rather than relying on an assurance that it was "done carefully".

The tone here is kept deliberately unalarmed, because the risks in this chapter are ordinary operational-security risks that scientific institutions have managed for decades under other names.
A data-handling agreement with a national meteorological service, a least-privilege account on a shared cluster, a laboratory notebook that survives a postdoc's departure: each is a governance or security control that predates agents entirely, and the argument here is only that agentic workflows need the same controls, applied with the same seriousness and no more drama.
The one genuinely new element is that an agent reads and acts on untrusted text at machine speed, which changes the scale at which a small lapse propagates but not the nature of the lapse.
What follows, then, is not a warning but a specification: what to record so the work survives scrutiny, and what to constrain so the work cannot be turned against the person running it.
Institution-specific thresholds, that is, which systems count as sensitive and which approvals are mandatory, are left as **[AUTHOR]** throughout, because they are set by local policy, not by this book.

## 12.2 Institutional memory as a first-class output

The most undervalued product of a governed agentic workflow is not its result but its record, and that record deserves to be designed, budgeted and maintained as a deliverable in its own right.
Scientific groups lose knowledge continuously through ordinary staff turnover.
A doctoral researcher spends three years calibrating a hydrological model, then leaves, and with them goes the tacit reasoning behind a hundred small decisions that never reached a paper: why one gauge was excluded, why a threshold sits where it does, which preprocessing step compensated for a known sensor fault.
Agentic workflows both worsen this problem and can be made to solve it.
They worsen it because an agent can generate in an afternoon a volume of configuration, transformation and intermediate result that would take a successor weeks to reverse-engineer.
They can solve it because every decision an agent takes passes through a specification and a tool call, both machine-readable, both capturable without any extra human effort.
The design principle that follows is to treat the audit trail not as compliance overhead but as the institutional memory the group would otherwise lose, written continuously and for free as a by-product of how the work is done (high confidence in the principle; the effort saved is unquantified and will vary by group).

Documentation that survives turnover has a few properties that distinguish it from documentation that does not, and they are worth naming because they are the acceptance criteria for the record as a deliverable.
First, it is co-located with the artefact it describes, rather than held in a separate system the next person will never find.
Second, it records the assumption and its justification together, so a successor inherits not only what was decided but why.
Third, it is written at the moment of the decision, rather than reconstructed later when the reasoning has faded.
Fourth, it is legible to a human who was not present, which rules out raw logs as a sufficient record on their own.
An agentic workflow can be arranged to produce documentation with all four properties as a matter of course, because the specification (Chapter 3) states the why, the tool trace records the what, and a summarisation step, itself an agent task verified by a human, renders the two into prose a successor can actually read.
The limitation worth stating is that a record made this way is only as honest as the verification applied to it: an agent asked to summarise its own reasoning will produce a plausible account that may not match what actually happened, which is why the summary is an input to human review, never a substitute for it.

## 12.3 Registries: assumptions and uncertainties as standing records

An assumption registry is a standing, versioned record of every choice the workflow depends on but does not itself justify, and it is the single governance artefact with the highest return in scientific work.
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
Where a registry answers "what did the analysis assume", the audit trail answers "what happened, in what order, to what data, invoked by whom", and the two are complementary halves of a defensible record.

> **Definition — Audit trail.** A time-ordered, tamper-resistant log of everything the workflow did: which tool ran, on which inputs, producing which outputs, under which version, passed by which human. Registries record what was decided; the audit trail records what actually happened, so a result is not just re-runnable but explicable.

The elements a scientific audit trail must capture are modest in number and stable across workflows: the specification version each run executed under, the identity and version of every tool called, the inputs consumed and outputs produced with content hashes sufficient to detect later alteration, the model and configuration in force, and the human decision points passed with the identity of whoever passed them.
Captured together, these make a result reproducible in the strong sense, not merely re-runnable but explicable, and they convert the vague reassurance that a workflow was "carefully done" into a record a reviewer, an auditor or a successor can interrogate.
The architecture that carries this record is the subject of the first figure of this chapter, which shows the audit trail and the two registries as a governance layer sitting beside the workflow rather than inside it, fed by the same events the workflow generates for its own operation.

Reviewer-coverage records are the part of the audit trail that documents scrutiny rather than execution, and they answer a question that turns acute the moment agents generate more output than humans can exhaustively check: what was reviewed, by whom, and what was not.
A reviewer-coverage record pairs each reviewable artefact (a block of generated code, a synthesised claim, a QC decision) with the reviewer who examined it, the depth of that examination, and its outcome, distinguishing an independent-agent review (Chapters 7 and 10) from a human review and recording both.
Its purpose is to make coverage explicit and therefore contestable, because the dangerous state in an agentic workflow is not the unreviewed artefact everyone knows is unreviewed but the one assumed to have been checked and was not.
A coverage record also supports honest disclosure, since a manuscript produced under Chapter 9's discipline can state truthfully which components passed independent review and which rest on author inspection alone, and it supports the evaluation of Chapter 11 by making the denominator of review coverage a measured quantity rather than an impression.
The limitation, stated plainly, is that a coverage record documents that review occurred, not that it was competent: a rubber-stamp review leaves the same record as a searching one, and no registry can substitute for a reviewing culture that takes the task seriously.

**Figure 12.1 — The governance layer: registries and audit trail beside the workflow.** *A figure brief follows `FIGURES.md`; render in the house style.*

```
FIGURE BRIEF
- id:            Figure 12.1
- title:         A governance layer that records without steering
- type:          architecture
- claim:         Provenance is captured by a standing governance layer that sits beside the workflow and is fed by the same events the workflow already emits — assumptions, uncertainties, execution and review recorded as first-class, durable outputs.
- canvas:        16:9
- elements:      left, a vertical stack representing the workflow — a "specification" tag (blue),
                 an "AI agent" rounded rectangle (orange border), a "tool call" glyph (green),
                 a "human decision" head-and-shoulders icon (blue); right, a grey-bordered
                 rounded rectangle labelled "governance layer" containing four stacked data-store
                 cylinders (sky blue): "assumption registry", "uncertainty registry",
                 "audit trail", "reviewer-coverage record"; a single reviewer icon
                 (purple, head-and-shoulders with tick) feeding the reviewer-coverage cylinder
- flow:          the workflow runs top-to-bottom on the left; thin single-weight arrows lead
                 rightward from each workflow element into the governance layer, all one-directional
                 (workflow writes to the layer; the layer does not steer the workflow); the reviewer
                 icon writes into the reviewer-coverage cylinder
- labels:        "specification", "AI agent", "tool call", "human decision", "governance layer",
                 "assumption registry", "uncertainty registry", "audit trail",
                 "reviewer-coverage record", "independent reviewer"
- annotations:   a light bracket down the right edge of the governance layer labelled
                 "institutional memory — survives turnover"
- caption:       Figure 12.1 — The governance layer records the workflow without steering it: assumptions, uncertainties, execution events and review coverage are written as durable outputs by the same steps that do the work, so the record is a by-product rather than an added burden. Arrows run only from workflow to record.
- alt-text:      An architecture diagram. On the left, a workflow runs top to bottom: a specification feeds an AI agent, which makes a tool call and reaches a human decision. On the right, a grey box labelled governance layer contains four stacked cylinders: assumption registry, uncertainty registry, audit trail, and reviewer-coverage record. Thin arrows lead from each workflow element rightward into the governance layer, all pointing one way. An independent reviewer icon writes into the reviewer-coverage cylinder. A bracket down the right edge reads institutional memory, survives turnover.
- generator prompt: A flat vector architecture diagram on an off-white background. On the left
                 side, a vertical top-to-bottom sequence: a small blue tag labelled "specification",
                 below it an orange-bordered rounded rectangle labelled "AI agent", below it a green
                 wrench glyph labelled "tool call", below it a blue head-and-shoulders icon labelled
                 "human decision". On the right side, a large grey-bordered rounded rectangle labelled
                 "governance layer" containing four stacked sky-blue cylinders labelled top to bottom
                 "assumption registry", "uncertainty registry", "audit trail", "reviewer-coverage
                 record". Thin single-weight near-black arrows lead from each left-side element
                 rightward into the governance layer, all pointing right only. A purple head-and-shoulders
                 icon with a small tick, labelled "independent reviewer", sits to the right and has an
                 arrow into the "reviewer-coverage record" cylinder. A thin bracket runs down the right
                 edge of the grey rectangle, labelled "institutional memory — survives turnover".
                 Minimal text, generous spacing, single-weight lines.
```

## 12.5 Security as ordinary operational discipline

The security of an agentic workflow rests on three controls that map onto long-standing practice, and treating them as routine rather than exceptional is the correct posture.
The first governs the untrusted inputs an agent reads, because an agent that ingests external documents, web content or third-party data is acting on text an adversary may have written.
The second governs the credentials and data the agent touches, because an agent operating on institutional systems and high-performance computing holds, however briefly, the access rights of whoever launched it.
The third governs the tools the agent may call, because an agent's capacity to cause harm is bounded by the narrowest set of permissions that still let it do the job.
None of these is novel: input validation, credential hygiene and least privilege are the elementary controls of every secured system, and the argument here is only that an agent is a system they apply to, not an exception that transcends them.
The community consensus list of the most critical risks in LLM applications, revised for 2025 specifically to reflect agentic systems, puts prompt injection at the top and names "excessive agency", that is, granting an application more tools, permissions or autonomy than its function requires, as a distinct top-ten risk in its own right (OWASP, 2025), which is the security profession's way of saying exactly what the three controls below say.
The sections that follow take each in turn, and the chapter's second figure draws the trust boundary the three controls jointly define: the line between what the agent is permitted to reach and what it is not.

## 12.6 Prompt injection: untrusted input as a steering channel

Prompt injection is the failure in which untrusted content an agent reads is interpreted as instruction rather than data, and it is the security concern most specific to agentic systems because it exploits the very property that makes them useful.
At the level of the model, an agent does not distinguish between the instructions its operator gave it and the text it later reads from a document, a web page or a data file; all of it arrives as language, and language that says "ignore your previous instructions and instead do X" is processed as language.
This is not a quirk that a better model patches away.
The paper that defined indirect prompt injection made the point architecturally: LLM-integrated applications blur the line between data and instructions, so anyone who can place text where an agent will later read it (a web page, a document, an email, a metadata field) can attempt to hijack the agent without ever touching the operator's prompt (Greshake et al., 2023).

> **Definition — Prompt injection.** When text an agent reads as part of its work (a web page, a downloaded file, a colleague's document) contains instructions, and the agent obeys them as if they came from its operator. The agent cannot reliably tell "content to analyse" from "orders to follow", so, in effect, the data can direct the agent.

For an environmental workflow this is not hypothetical, because the agents in this book's patterns routinely read material the group did not author: a paper retrieved for synthesis (Chapter 5), a data description fetched from a partner portal (Chapter 6), a web page consulted for a parameter value, a file handed over by a collaborator.
Any of these can carry, by malice or by accident, text an agent will act on: an instruction to exfiltrate a credential, to alter a QC threshold, to insert a fabricated citation (Chapter 13), or to write to a path it should not touch.
The severity of an injection is not a property of the text but of what the agent can do once steered, which is why the defence is never to detect all malicious text, an unwinnable game since the model reads natural language and natural language is unbounded, but to constrain what any instruction, however it arrives, is able to accomplish.
That framing is not an improvisation of this book; it is where the security literature has landed.
Given that prompt injection cannot currently be solved at the model level, recent work proposes architectural patterns that give resistance by construction, each trading some agent capability for safety: fixing the plan before untrusted data is read so the data cannot redirect it, having the model emit a checkable program rather than take direct action, or splitting a privileged tool-using model from a quarantined model that reads untrusted text but holds no tools (Beurer-Kellner et al., 2025).
This book has high confidence in the vulnerability class being durable and the constraint-based response being the right one; specific historical exploits are patched routinely, but the underlying data–instruction conflation is unresolved by any current model.

The defences that follow are architectural rather than detective, they compound, and several of them are patterns the book already prescribes under other names.
The primary defence is least privilege, treated in §12.8, because an agent that cannot delete files or reach the open internet cannot be made to do so by an injected instruction, however cleverly phrased: the capability was simply never granted.
The second is a firm separation between the channel carrying instructions and the channel carrying data, so content retrieved from an untrusted source is presented to the agent as quoted material to be analysed rather than as instruction to be followed; this reduces but does not eliminate the risk, because the boundary is enforced by convention rather than by a hard mechanism the model cannot cross, which is precisely why the stronger design-pattern variants above fix the plan or quarantine the reader instead of trusting the convention.
The third is the human gate on any consequential action, so an agent may propose to send an email, write to a shared system or run an irreversible command, but the action itself waits on a human who sees the proposal in context.
The fourth is provenance: an audit trail (§12.4) recording what the agent read and when makes an injection traceable after the fact, which both aids recovery and deters the careless introduction of untrusted content.
The limitation worth stating is that no combination of these fully closes the channel while agents read natural language at all; the residual risk is managed, as other irreducible risks are, by keeping the blast radius small rather than pretending it is zero.
**[AUTHOR: an injection you encountered or deliberately tested — even a benign one, such as a comment in a shared config that an agent acted on — would ground this section in lived practice.]**

## 12.7 Credentials and data when agents touch institutional systems

Credential and data handling is the security concern with the highest stakes in institutional science, because an agent operating on shared systems inherits real access to real infrastructure.
When an agent runs a job on a high-performance cluster, queries an operational database, or writes to a group's shared storage, it does so with credentials that grant the launching scientist's rights, and any mishandling of those credentials (logging them in a trace, embedding them in generated code, transmitting them to a model provider as part of a prompt) turns a convenience into an exposure.
The disciplines that contain this risk are, again, drawn from ordinary practice and merely applied with care to a new kind of operator.
First, credentials are supplied to an agent through the environment or a secrets manager rather than written into specifications, prompts or code, so they never enter the material an agent might log or transmit.
Second, they are scoped to the task, so a data-retrieval agent holds read access to one dataset rather than write access to a filesystem.
Third, they are short-lived where the infrastructure supports it, so a leaked token expires before it can be widely abused.
The corresponding discipline for data is to keep sensitive inputs on systems the group controls and to be explicit about what leaves them, because the moment a dataset is placed in a prompt it may traverse a third-party model provider, with implications for data-sharing agreements that a national service or a commercial partner may enforce, a point that connects directly to the data-sovereignty design of Chapter 14, which treats the case where observations cannot be shared at all.

The institutional dimension of this concern is that scientists rarely own the systems their agents touch, so the controls above have to be reconciled with policies set by others.
A group running agents against a shared cluster operates under the cluster's acceptable-use policy, its data-classification scheme and its authentication regime, and an agentic workflow that ignores these will be, rightly, refused access or shut down.
The productive response is to design the workflow to fit the institution's existing controls rather than to seek exceptions from them: to run within the account and quota already granted, to classify the data the workflow handles against the institution's existing scheme, and to document the flow of credentials and data so it can be reviewed against policy before it runs.
The confidentiality logic here is the same one major funders already apply to their own processes, since one has prohibited reviewers from putting grant material into online AI tools precisely because the reviewer cannot control where the data then goes (Chapter 9), and material whose onward use cannot be controlled simply must not enter a third-party model service.
Where an institution's specifics govern, that is, which data classes may reach an external model, which systems require multi-factor authentication for automated access, and what retention applies to an audit trail, these are decisions local policy makes and this book cannot, and they are marked **[AUTHOR]** accordingly.
The limitation is that policies vary widely and change, so the durable guidance is the principle, namely to treat an agent's access as the scientist's own access and handle it with the same care, rather than any particular rule, which will differ between a university, a national laboratory and an operational forecasting centre.

## 12.8 Least privilege and the trust boundary

Least privilege is the principle that an agent receives the narrowest set of tool permissions that still lets it complete its task, and it is the single most effective security control available because it bounds the harm of every other failure at once.
An agent restricted to reading a named directory and running a test suite cannot exfiltrate data, cannot write to production systems, and cannot be steered by an injected instruction into doing either, not because such instructions are detected, but because the capability to obey them was never granted.

> **Definition — Least privilege.** An agent is given the narrowest access that still lets it do the job and nothing more: read one named folder, run one named tool, reach no further. A mistake, a bug or a hostile instruction can then do damage only inside those narrow limits, because the power to do worse was never handed over in the first place.

Applying the principle in practice means enumerating, before a workflow runs, exactly which tools the agent may call and with what scope: which paths it may read and which it may write, whether it may reach the network and to which hosts, which credentials it may use, and which actions require a human gate rather than proceeding on their own.
This enumeration is itself a governance artefact, belonging in the specification (Chapter 3) and recorded in the audit trail (§12.4), and it has the useful side effect of forcing the workflow's designer to articulate what the agent actually needs, a question that often reveals a broad permission was requested out of convenience rather than necessity, the "excessive agency" the security profession warns against (OWASP, 2025).
The institutional vocabulary has kept pace with the move to agents: alongside the top-ten risks for LLM applications already cited, a companion top-ten now exists for agentic applications specifically, effectively expanding that single "excessive agency" category into a full agent-specific risk list once a system takes autonomous, credentialed, multi-step action (OWASP, 2026).
The default posture is deny-by-default: the agent starts with no access and is granted each capability deliberately, rather than starting broad and being pared back, because the failures of omission in the first posture are safe and the failures of omission in the second are exposures (high confidence; this is standard security practice applied unchanged to agents).
Practitioner guidance has arrived independently at the same posture, framed as consequence-tiered permissions: an action is fully autonomous only where it is low-stakes and reversible, propose-then-approve in the middle band, and never autonomous at the top, with the tiers drawn around the consequence of the action rather than any model's current capability, because models change and the permission gradient should not (practitioner commentary, 2026).

The trust boundary is the line this enumeration draws, and making it explicit is the purpose of the chapter's second figure.
On the trusted side sit the agent, the specification directing it and the tools it is permitted to call; on the untrusted side sit the external documents, web content and third-party data it reads, together with the consequential actions (writing to shared systems, sending communications, running irreversible commands) that it may propose but not perform without a human passing the gate.
Drawing the boundary explicitly clarifies where each defence belongs: input validation and the instruction–data separation live where untrusted content crosses inward, least privilege lives at the tools the agent may call, and the human gate lives where a proposed action would cross outward into consequence.
The boundary is also what institutional IT will ask to see, because it is the artefact that answers their questions directly, and the closing section turns to those questions.
The limitation of the least-privilege discipline is operational rather than conceptual: permissions that are too narrow cause a workflow to fail in ways that tempt an operator to grant broad access just to make the failure go away, and resisting that temptation, that is, diagnosing the specific missing permission rather than opening the boundary, is a matter of discipline the tooling can support but cannot enforce.

**Figure 12.2 — The trust boundary: what the agent may reach, and what waits on a human.** *A figure brief follows `FIGURES.md`; render in the house style.*

```
FIGURE BRIEF
- id:            Figure 12.2
- title:         Least privilege and the trust boundary
- type:          architecture
- claim:         Security is bounded by drawing an explicit trust boundary: untrusted inputs enter through validation, the agent holds only the narrowest tool permissions, and any consequential action waits on a human gate before it crosses outward into effect.
- canvas:        16:9
- elements:      a central grey-bordered rounded rectangle labelled "trusted zone" containing an
                 "AI agent" (orange border), a "specification" tag (blue) and a small set of
                 "permitted tools" glyphs (green) with a lock annotation "least privilege";
                 on the left, outside the zone, three stacked untrusted sources (grey with a small
                 warning outline): "external documents", "web content", "third-party data",
                 entering through a vermillion gate labelled "validate · quote as data";
                 on the right, outside the zone, consequential actions (grey): "write to shared system",
                 "send communication", "irreversible command", reached only through a second vermillion
                 diamond gate labelled "human gate" with a blue human icon
- flow:          left-to-right — untrusted sources pass through the left vermillion gate into the
                 trusted zone as data; inside, the agent calls only permitted tools; proposed
                 consequential actions exit rightward only by passing the human gate; the two gates
                 mark the trust boundary (drawn as the edges of the grey rectangle)
- labels:        "trusted zone", "AI agent", "specification", "permitted tools", "least privilege",
                 "external documents", "web content", "third-party data", "validate · quote as data",
                 "write to shared system", "send communication", "irreversible command", "human gate"
- annotations:   a light callout on the trusted-zone border reading "trust boundary"; a small note by
                 the permitted-tools glyphs reading "deny by default"
- caption:       Figure 12.2 — The trust boundary. Untrusted inputs enter only as validated data, the agent inside holds the narrowest tool permissions that let it work, and consequential actions leave only through a human gate. The defences are architectural: an injected instruction cannot command a capability the agent was never granted.
- alt-text:      An architecture diagram with a central grey box labelled trusted zone containing an AI agent, a specification and a small set of permitted tools annotated least privilege and deny by default. On the left, three untrusted sources (external documents, web content and third-party data) pass through a vermillion validation gate into the zone as data. On the right, three consequential actions (write to shared system, send communication, irreversible command) sit outside the zone and are reachable only through a second vermillion human gate with a blue human icon. The edges of the grey box are labelled trust boundary.
- generator prompt: A flat vector architecture diagram on an off-white background. In the centre, a
                 grey-bordered rounded rectangle labelled "trusted zone" contains an orange-bordered
                 rounded rectangle labelled "AI agent", a small blue tag labelled "specification", and a
                 cluster of green wrench glyphs labelled "permitted tools" with a small note "least
                 privilege — deny by default". On the left, outside the rectangle, three stacked grey
                 boxes labelled "external documents", "web content", "third-party data" connect rightward
                 through a vermillion diamond gate labelled "validate · quote as data" into the trusted
                 zone. On the right, outside the rectangle, three stacked grey boxes labelled "write to
                 shared system", "send communication", "irreversible command" are reached from the agent
                 only through a second vermillion diamond gate labelled "human gate" accompanied by a blue
                 head-and-shoulders icon. The left and right edges of the grey rectangle carry a small label
                 "trust boundary". Flow reads left to right; single-weight near-black arrows, one arrowhead
                 style, generous spacing, minimal text.
```

## 12.9 What institutional IT will ask before an agent runs

Institutional IT and information-security teams will ask a predictable set of questions before an agentic workflow runs on their infrastructure, and a group that can answer them from its governance artefacts will be granted access far more readily than one that cannot.
The questions are the same an IT team would ask of any new system, reframed for an operator that acts on its own: what data will the workflow touch and how is it classified; where does that data go, and in particular does any of it leave institutional systems for an external model provider; what credentials does the agent hold and how are they scoped, stored and rotated; what can the agent do, that is, its full set of tool permissions, and what stops it doing more; who is accountable for its actions, and how is a mistake detected, contained and reversed; and what record is kept of what it did.
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
The durable point, and the one this chapter closes on, is that governance and security are not the price of using agents in science but the condition under which their use is scientific at all: an instrument whose behaviour is unbounded, unrecorded and unaccountable is not an instrument a scientist should trust, and the discipline that makes an agent trustworthy is the same discipline, applied to a new tool, that has always separated measurement from guesswork.

## 12.10 Verification checklist

This checklist certifies that an agentic workflow is governed and secured well enough to be trusted and approved; a colleague who did not build it, or an institutional reviewer, should be able to apply it from the record alone.

- **Registries exist and are current.** The assumption and uncertainty registries are present, versioned, and reflect the workflow as it actually runs, each entry carrying its justification, confidence level and approver (§12.3); a reviewer can find an assumption and see who agreed to it.
- **The audit trail reconstructs any artefact.** For any output, the trail recovers who and what produced it, in what order, under which specification and model version, with content hashes sufficient to detect later alteration (§12.4).
- **Reviewer coverage is recorded.** Each reviewable artefact is paired with its reviewer, the depth of review and the outcome, distinguishing independent-agent from human review, so coverage is explicit and contestable rather than assumed (§12.4; Chapters 7, 10).
- **Least privilege confirmed at the interface, not in prose.** The agent's tool permissions are verified by inspecting what the tools actually allow (paths, network, credentials, gated actions), not by trusting the agent's or the specification's description of them (§12.8); deny-by-default is the starting posture.
- **Prompt-injection surface reviewed for every input channel.** Every channel that feeds untrusted content into agent context (retrieved papers, partner data, web pages, collaborator files) has been identified and constrained by architecture (least privilege, instruction–data separation, human gates), not by hoping to detect malicious text (§12.6).
- **Credentials and partner data handled per institutional policy.** Credentials reach the agent only through the environment or a secrets manager, are task-scoped and short-lived where supported, and no data leaves institutional systems for an external model against a data-sharing agreement (§12.7); institution-specific rules are recorded **[AUTHOR]**.
- **Accountability and recovery are named.** A specific human is accountable for the workflow's actions, and the record shows how a mistake is detected, contained and reversed (§12.4, §12.9).
- **Documentation survives staff turnover.** A newcomer who was not present can operate the workflow and defend its results from the record alone, the true test of whether the governance layer is real or decorative (§12.2).

## 12.11 Repository pointer

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
