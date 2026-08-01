# Preface examples, for selection

**Drafted 27 July 2026 · ai-writer · examples only.**

Nothing in this file is part of the manuscript.
`ch00-front-matter.md` has not been touched, and neither has any chapter, `CLAUDE.md`, `STYLE.md`, `FIGURES.md` or `OUTLINE.md`.
These are drafted candidates for the Preface added to the plan on 27 July 2026.
They are written so that the types in `RESTRUCTURE-PROPOSAL.md` §6.3 can be compared as prose rather than as descriptions.
Every draft follows `STYLE.md` v5.0 and is sentence-per-line per §10, so you can comment on any single sentence in the pull request.

**On the `[AUTHOR: …]` markers.**
Every lived specific in these drafts is a marker, because the repository does not record it and I will not invent it.
Example A carries the most, which is the honest shape for an origin preface.
The documented executed work is real and is used; the detail that makes it unmistakably yours is yours to add.
Under each draft is a list of its markers and what each one needs from you.

**On what the drafts are built from.**
The material used is what this repository documents.
That is the rainfall-verification toolkit and its data-sovereignty constraint (Ch. 14), and the executed end-to-end governed modelling workflow (Ch. 15).
It is also the domain framing and contribution statement (`ch00`), the agent roster and citation policy (`CLAUDE.md`), and the instrument stance (Ch. 1 §1.3 and §1.4).
Nothing else about you has been used, and nothing has been invented.

---

## 1. The recommended hybrid: A + C + D

**Type:** origin and credential, then scope and contract, then reflexive disclosure. The plan's recommendation, §6.4, at the brief length of §6.6.
**Opens on:** the data-sovereignty constraint from the rainfall-verification work, and the design it forced.
**Length here:** 958 words of prose, three sections, plus four markers.
**Demands:** the opening moment's specifics, the disclosure granularity, the per-chapter contribution summary, and the foreword decision. Four markers.
**Wins:** gives the reader, in about three pages, who is speaking, what they are promised, and how far to trust the object in their hands. Ends on the disclosure, which is the strongest available closing move for a book arguing that agentic work must be disclosed.
**Risks:** three movements in three pages is tight. If the opening moment stays general, the whole thing flattens into the scope preface with a preamble.

---

### Preface

The observations I needed were held by an institution that could not let them leave.
That was not obstruction, and it is worth being precise about why.
National meteorological and hydrological services hold rain-gauge records under licences, bilateral agreements and national data policies.
A service that releases a protected record carries a risk it has no way to accept.
**[AUTHOR: the opening moment. Which partner, which region or programme, which of those grounds applied, and what the work was for. What was at stake, on what deadline, and what you actually did that week. This is the paragraph the whole Preface rests on and only you can write it.]**
The usual answer is to negotiate an exception anyway.
That takes months, binds both sides to terms that constrain reuse, and often ends with no agreement at all.
So the verification expertise sat on one side of a boundary, and the observations that would have exercised it sat on the other.

The toolkit went to the data instead.
It runs inside the partner's own environment, on hardware they already have, and it emits aggregate scores and nothing else.
The records never move.
Part of that toolkit is a language model, and the line I drew around it is the reason this book exists.
The model runs locally, it explains what a verification score means to someone who is not a verification specialist, and it is not permitted to produce a score.
Every number comes from a deterministic calculation that returns the same answer every time it runs.
That separation is not caution for its own sake.
A verification score can decide whether a forecast system is fit to issue warnings.
A number that might come out differently on a second run is not a measurement.
Chapter 14 is that case study in full.

Three constraints forced the design: no data may leave, the compute available is minimal, and there is no recurring budget to keep anything running.
I chose none of them.
What they produced is close to the design I would argue for on governance grounds alone.
That convergence is what this book is built on (moderate confidence, resting on one deployment).
The discipline a well-resourced group can choose, an under-resourced one is forced into, and the forced version is not obviously worse.

### What this book is, and what it is not

This book gives you five workflow patterns, a chapter that composes them into multi-agent workflows, and the checks that make each one safe to run.
Two chapters are case studies of the whole apparatus running end to end, and one is a gallery of failures with the checks that catch them.
Eight verification checklists are printed in Appendix A, so you can lift them out rather than rebuild them.

What the book refuses matters as much, and there are three refusals.
It names no products.
Capability classes and approximate years go in print instead, because a named product dates faster than a book can be revised.
Where you need a current value, the text says where to look it up.
It does not promise that an agent will do your science.
And it does not present designed work as executed work: Chapter 8's intercomparison is labelled a worked design, because that is what it is.

The book-length treatments of agentic AI that already exist are written for engineers building production systems, or for business audiences deciding whether to buy in.
The science-facing material is mostly survey and perspective writing.
What I have not found is a practical, governance-first, diagram-led treatment written for practising environmental researchers and grounded in work that was actually executed.
That claim rests on a limited scan made in July 2026, which will be repeated before release.
If a close equivalent already exists the claim softens, and I would rather revise it than overstate it (moderate confidence).

You need to be comfortable with Python and the command line, and nothing beyond that.
The next section, on what the reader needs, sets out the edges.
The worked examples come from operational hydrology and meteorology, because that is the ground I actually work on.
The patterns are written to transfer across the environmental sciences; the demonstrations are not.
Cross-domain worked examples are a deliberate deferral to a later edition, not a promise quietly made and not kept.
Releases are versioned.
The repository behind them holds the source, the dated research sweeps every citation comes from, the further reading, the figure briefs and an errata note per release.
There is no code in it, and there was never going to be.

### How this book was made

Four agent roles worked on this book, and each had a written remit it could not step outside.
One planned the structure and maintained the admin documents.
One drafted prose and figure briefs.
One reviewed, and it was never the one that had drafted.
One ran the literature sweeps.
Citations came only from those sweeps, dated, with a DOI or a URL recorded for every source, and never from a model's memory.
Where a claim needed a source no sweep had found, it kept a flag rather than acquiring a plausible-looking reference.

There is a firm limit on all of that, and it belongs here rather than in an appendix.
Agents are never authors.
Accountability for every claim, every figure and every judgement in these pages rests with me, the named human author.
Responsibility is not a capability, so it does not transfer to an instrument however good the instrument becomes.
Anything only I could supply is marked as such in the source, and no agent was permitted to fill one of those in.

This section will eventually carry a per-chapter account of who did what, generated from the status records each chapter keeps.
You should not have to take my word for the division of labour.
It is a skeleton for now, because it can only be finished when the book is.

**[AUTHOR: confirm the per-chapter agent-contribution summary once the restructure completes, drawn from the chapter status records: which agents did what.]**

**[AUTHOR: decide the granularity of the disclosure, per chapter or per task, and whether it sits here in full or here in summary. The old wording offered "with detail in the repository", which is no longer available in the sense it was written, so the choice is now between full and summary in print.]**

**[AUTHOR: decide whether to invite a foreword, and from whom. Per plan §6.5 the invitation goes out after review and the book does not wait for it.]**

An honest skeleton I can stand behind beats a polished statement that claims more than exists.

---

**Markers in this draft, and what each needs from you.**

1. *The opening moment.* The single thing that decides whether this preface works. The partner or programme, the sovereignty ground, the deadline, and what you personally did. Two or three sentences of specifics will carry the whole first movement.
2. *The per-chapter contribution summary.* Carried from `ch00`. Cannot be written until the restructure closes.
3. *The disclosure granularity.* Carried from `ch00` and rewritten, because "detail in the repository" is no longer an available option.
4. *The foreword decision.* New, from plan §6.5. Not a gate on anything.

---

## 2. Type A alone: the origin and credential preface

**Opens on:** the same constraint, then the second piece of executed work, then the reason for writing.
**Length here:** 411 words of prose, plus four markers.
**Demands:** heavy. Four markers, all lived.
**Wins:** authority in the first paragraph, which is the book's stated purpose. It is also the one thing no other author could have written, and the section most likely to excerpt well.
**Risks:** drifts into memoir if the moments are not tightly chosen. Fails completely if written generically, which is why so much of it here is marker rather than prose.

---

### Preface

I spent months trying to get a rain-gauge record released, and in the end I stopped asking.
The record was held by a national service under rules that were not theirs to waive.
The residual risk of releasing it was one the holding institution could not accept.
**[AUTHOR: the opening moment. The partner or programme, the region, the sovereignty ground, the deadline you were working to, and what you actually did. Two or three sentences of your own specifics replace this marker.]**
So the verification went to the observations instead of the other way round.
The toolkit that came out of it runs inside the partner's own environment.
It computes its scores by fixed algorithms that return the same numbers every time they run.
It carries a small local model that may explain a score and may never produce one.
What leaves the building is an aggregate figure, and never a record.
It also turned out to teach, because a user learning verification on their own data learns something no generic worked example can give them.
Chapter 14 is that toolkit in full.

The second piece of work behind this book was a modelling study run end to end under the governance the middle chapters describe.
**[AUTHOR: name the modelling problem, the domain and period, the question it answered, and the publication it produced.]**
Every stage had a written specification, a defined agent role, a gate the work had to pass, and a named person who decided.
What that study established is narrower than it sounds, and worth stating precisely.
The apparatus composes, and it costs what it costs.
It is an existence proof rather than a controlled comparison, because nobody ran the same problem twice with the governance removed.
Chapter 15 walks through it stage by stage.

Neither piece of work made me confident about this technology.
Both made me specific about it.
The rainfall toolkit works because the part that can be wrong is architecturally separated from the part that must be right.
No amount of good behaviour from the model substitutes for that separation.
A model instructed not to touch the scores is still a model that could.
The modelling study worked because a named person had to decide at every gate, rather than signing at the end for decisions nobody had recorded.
Both are ordinary engineering, and neither required me to settle the question of how clever these systems really are.
**[AUTHOR: a failure you personally caught. Fluent, confident, completely wrong, and what it would have cost had it gone through. One paragraph, and it does more for the reader's trust than any success in the book.]**

I wrote this because I could not find it when I needed it.
The engineering literature assumes you are shipping a product.
The science-facing writing is mostly survey.
What was missing was a practical treatment for a working environmental scientist: patterns rather than products, verification at the centre, and every example drawn from work somebody had actually run.
**[AUTHOR: whether you want the book's purpose stated here (free release, versioned, announced through the newsletter) or left to the scope section. It reads well either way and the choice is one of emphasis.]**

---

**Markers in this draft, and what each needs from you.**

1. *The opening moment.* The whole preface rests on it. Everything else in the draft can survive a weak version of this; nothing can survive a generic one.
2. *The Ch. 15 modelling problem.* Carried from that chapter's own opening marker. Two clauses will do here: what was modelled, and what came out.
3. *The caught failure.* Ch. 1 §1.4 already asks for one and so does Ch. 14 §14.7. If you have one story it can serve all three, and the preface is the strongest place for it.
4. *The purpose statement.* A placement decision, not new writing.

**Also available and deliberately unused.** `STYLE.md` records that your doctoral work was on medium-range prediction of areas at risk of flash floods. I have kept it out of the prose because it is recorded there as a source for the house voice rather than as biography, and a credential sentence about your own career should be yours to place rather than mine to assume. If you want it, it belongs in the last paragraph, immediately before "I wrote this because I could not find it when I needed it."

---

## 3. Type C alone: the scope-and-contract preface

**Opens on:** a refusal, so the contract does not open on an abstraction.
**Length here:** 453 words of prose, plus one marker.
**Demands:** almost nothing new. One marker.
**Wins:** protects both parties. A reader who knows the cross-domain examples are deferred cannot be disappointed by their absence, and the book's honesty about its own limits is one of its better qualities.
**Risks:** reads as terms and conditions. Does nothing for credibility, and gives the reader no reason to care yet. That risk is visible in this draft and I have not tried to disguise it.

---

### Preface

No chapter in this book tells you which agent product to use.
That is deliberate, and it is the first of several things the book will not do for you.
The products change faster than a book can be revised.
So what goes in print is the capability class and the approximate year it arrived.
Where you need a current figure, the text says where to look it up.
The patterns are the durable part.
A reader who learns them will still be able to use them when every product named in any competing book has been renamed or withdrawn.

What the book does promise is specific.
You get five workflow patterns across the research lifecycle, from literature synthesis through to manuscript preparation.
Each has the same seven-part anatomy: the problem, the conventional workflow, the agentic redesign, and a worked example or a worked design.
The last three sections matter most: the ways the pattern fails, a verification checklist, and the decisions you must take to adapt it.
A sixth chapter composes those patterns into multi-agent workflows.
A third of the book is verification, provenance, governance and security, ending in a gallery of failures.
Two case studies show the whole apparatus running end to end.
Eight checklists are collected in Appendix A, and the specification schema is in Appendix B, both in a form you can copy.

It assumes you are a practising environmental or geoscientist, comfortable with Python and the command line, and it assumes nothing beyond that.
No machine-learning background is required.
No paid access to a frontier model is required either.
Low-compute and open-weight working is treated where it belongs, inside the constrained toolkit of Chapter 14 and the cost model of Chapter 16.
It is not assumed away, and it is not bolted on as a separate track.
The book is not written for machine-learning researchers after novel methods, nor for managers after pure strategy.
That second group will find the failure gallery and the adoption chapter worth their time.

Three exclusions are worth stating before you invest in the book rather than after.
The worked examples are hydrological and meteorological.
The patterns are pitched to travel across the environmental sciences, and cross-domain worked examples are deferred to a later edition.
There is no runnable code.
The repository behind the book holds the source, the dated research sweeps, the further reading, the figure briefs and an errata note per release.
And the evidence base is thinner in places than I would like.
Where a claim rests on my own judgement rather than on a verified source, it says so.
Every substantive claim carries a confidence flag, so you can weigh it yourself rather than take it on trust.
**[AUTHOR: confirm the release terms you want stated here, if any, since licence and format are still open decisions.]**

---

**Markers in this draft, and what each needs from you.**

1. *The release terms.* Licence, format and DOI are deferred decisions. If you want none of them named yet, this marker is simply deleted and the paragraph ends on the confidence-flag sentence, which is a good ending.

---

## 4. Type D alone: the reflexive and disclosure preface

**Opens on:** the production mechanism, stated concretely rather than announced.
**Length here:** 406 words of prose, plus four markers.
**Demands:** moderate to heavy. Four markers, and it cannot be finished until the manuscript is.
**Wins:** genuinely distinctive. Almost no book on this subject can open this way, and it demonstrates the thesis instead of asserting it. Reflexive production is already a decided principle, so this delivers something committed to rather than adding scope.
**Risks:** can read as self-regarding if it dwells. This draft handles that by keeping the mechanism concrete and the reflection to two sentences.

---

### Preface

This preface was drafted by an agent working to a written style guide, reviewed by a different agent that had no part in drafting it, and signed off by me.
**[AUTHOR: confirm this holds for the final text of the Preface itself. It is the strongest opening sentence available to this type and it must be exactly true, or it must go.]**
The same arrangement produced the rest of the book, and the arrangement is the point.
Four roles, and each had a written remit it could not step outside.
One planned the structure and maintained the admin documents.
One drafted prose and figure briefs.
One reviewed against the style guide, the figure guide and the plan, and it never reviewed its own work.
One ran the literature sweeps and wrote them up as dated reports.

The rules those roles worked under are the rules the middle of this book argues for, applied to itself.
Citations came only from the dated sweeps, each source carrying a DOI or a URL, and never from a model's recollection of the literature.
A claim that needed a source no sweep had found kept a flag rather than acquiring a reference that looked right.
Anything lived, executed or decided was marked in the source as mine to supply, and no agent was permitted to resolve one of those marks.
Every chapter carries a status header recording what was done to it and by which role.
That header is not a courtesy to the reader.
It is the record I would need if someone asked me to justify a claim two years after I made it.
**[AUTHOR: the per-chapter contribution summary, generated from those status records once the restructure completes.]**

None of that made the process clean.
**[AUTHOR: what the discipline actually cost, and what it caught. A specification that was wrong, a review finding you disagreed with, a chapter that had to be redrafted after a sweep contradicted it. One concrete instance keeps this section from reading as a list of virtues.]**

The limit is firm and it belongs at the front rather than in an appendix.
Agents are never authors of this book.
Accountability for every claim, every figure and every judgement rests with me, the named human author, exactly as the chapters argue it must.
Responsibility is not a capability, so it does not transfer to an instrument however good the instrument becomes.
That is not a position I hold about this book in particular.
It is the position the book takes about a flood warning, an anomaly and a paper.
Arguing it for your work and exempting my own would be incoherent.

Disclosing this is not a gesture towards transparency, and it has a practical function.
You are about to read arguments about how agentic work should be specified, checked and recorded.
Knowing that those arguments were themselves produced that way tells you whether they survive contact with real use.
Knowing where the process failed tells you more.
**[AUTHOR: decide the granularity, per chapter or per task, and whether the account sits here in full or here in summary.]**

---

**Markers in this draft, and what each needs from you.**

1. *Confirmation of the opening sentence.* It has to be exactly true of the Preface's own text. If the Preface ends up hand-written, the sentence changes to say so, which is equally strong.
2. *The per-chapter contribution summary.* Carried from `ch00`. Blocked until the restructure closes.
3. *What the discipline cost and caught.* The one thing that stops this type reading as self-congratulation. A single concrete instance is enough.
4. *The disclosure granularity.* Carried from `ch00` and rewritten.

---

## 5. Type G alone: the instrument preface

**Opens on:** a real instrument, because the plan's own analysis says an abstract opening will not survive `STYLE.md`.
**Length here:** 402 words of prose, plus two markers.
**Demands:** light to moderate. Two markers.
**Wins:** states the intellectual thesis in one page and travels well as a standalone excerpt. It tells the reader they already own the skill the book asks for, which is flattering in a legitimate way.
**Risks:** it converges on type A, as the plan predicted. Read this next to A and the convergence is visible: the concrete opening is doing most of the work in both.

---

### Preface

No hydrologist trusts a rain gauge in the everyday sense of the word.
The gauge is calibrated before it goes out.
Its drift is characterised, so you know how it fails and by roughly how much.
Its readings go into a network built to catch the ones that are wrong, and a person stays accountable for what those readings are taken to mean.
Trust, in that setting, is not a feeling about the instrument.
It is a set of procedures around it, and every one of them assumes the instrument will sometimes be wrong.
**[AUTHOR: an instrument from your own work whose failure mode you know intimately, and the procedure your group actually runs to catch it. A gauge, a radar, a model output, a bias correction. One or two sentences, and the whole preface rests on them being real rather than illustrative.]**

An agent is an instrument in that same sense, and the discipline it needs is one you already have.
Calibration is evaluation on your own task with your own data, which is Chapter 11.
The deployment design is the specification you write before the agent starts, which is Chapter 3.
The quality-control network is the set of gates the work has to pass and the independent review that checks it, which are Chapters 10 and 12.
Accountability for what the readings mean stays exactly where it always was, with a named person who can be asked to justify it.
None of that is a new discipline imported into environmental science.
It is the one the field already runs on, pointed at a new kind of instrument.
Saying so plainly matters, because the alternative usually on offer is to accept the output and check it afterwards if there is time.
That is not a procedure.

The comparison has one limit, and that limit is why a third of this book is about checking.
A rain gauge fails in ways you can anticipate: it blocks, it under-catches, it drifts.
Those failures leave signatures a quality-control routine can look for.
A language system fails by imitating competence.
It returns an answer whose fluency tells you nothing at all about whether it is correct, and it does so with no signature to look for.
That property is called plausible failure throughout this book.
It is the single reason verification gets a whole part rather than a paragraph, and why Chapter 13 is a gallery of failures rather than a footnote to the successes.

So the recommendation the whole book carries is neither caution nor enthusiasm.
Build agentic workflows: designed processes with fixed inputs, checks the work must pass, and points where a person decides.
Do not deploy autonomous agents and hope.
**[AUTHOR: one sentence on where you personally sit on that line, since the book's stance is stated all through and its author's is not. It costs nothing and it makes the preface a person's rather than a position's.]**

---

**Markers in this draft, and what each needs from you.**

1. *The instrument and its procedure.* Must be one you actually run. A generic rain gauge is the fallback and it is noticeably weaker.
2. *Where you sit.* Optional, and one sentence. Delete it and the draft still closes cleanly on "Do not deploy autonomous agents and hope."

---

## 6. Type B: the problem preface

**The plan's reservation (§6.3):** it duplicates Ch. 1 §1.1 directly, which already opens on the field's mismatch between material and hours. Running the same argument twenty pages apart is what the de-duplication rule exists to prevent, so the plan would not take this type on its own.

**Opens on:** the state of agentic AI in the environmental sciences, with the book as corrective.
**Length here:** 233 words, drafted short so the duplication is visible rather than argued.

---

### Preface

Agentic AI arrived in the environmental sciences as a management technology.
The systems being proposed for this field are pitched as things that monitor, decide and act on the environment, and the writing around them is mostly about autonomy.
Very little of it is about the ordinary working scientist with a quality-control pass to run, a bulletin to produce and a paper to finish.
That scientist now has an instrument that could help with all three, and no way of knowing how far to trust it.
The gap is a governance gap rather than a capability gap.
The capability is real and datable, and Chapter 1 sets out when each piece of it arrived.

What is missing is the practice around it.
An instrument this fallible needs a specification written before it starts, checks it has to pass, and a person accountable for what it produces.
None of that is exotic.
It is the discipline the field already applies to a new sensor or a new model.
This book supplies the missing half: patterns for the work itself, and the verification practice that makes them safe to run.
It is written for a practising environmental scientist rather than for an engineer shipping a product or a manager deciding whether to buy in.
Every worked example in it comes from work that was executed, not from a design that was only ever drawn.

---

**Markers in this draft:** none. That is itself informative. A preface that needs nothing from you is a preface that could have been written by anyone, which is the deeper problem with this type, and the reason the plan folds its positioning content into the scope movement instead.

---

## 7. Type E: the living-book preface

**The plan's reservation (§6.3):** this is a section of a preface rather than a preface. It answers a question the reader has not yet thought to ask, and the plan recommends it be absorbed into another type as one or two sentences.

**Opens on:** the release model and what dates fastest.
**Length here:** 209 words.

---

### Preface

This book is versioned, and the version you are holding will be wrong about some things within a year.
That is not an apology, it is a design decision, and it changes how the book is written.
The material that dates fastest is the material about products: what a given system can do this quarter, what it costs per token, which capability arrived when.
None of that goes in print.
What goes in print is the pattern, the reasoning behind it and the check that makes it safe.
Those have held across every capability change since 2023, and they will outlast the ones coming.

Behind the printed pages is a repository.
It holds the Markdown source every release is built from, the dated research sweeps behind every citation, the further reading, the figure briefs and an errata note per release.
That is a genuine living layer and it contains no code, because promising code that does not exist is worse than promising nothing.
Each release is announced and excerpted through the newsletter.
So when a chapter tells you to look up a current figure rather than giving you one, that is deliberate.
It is what lets a printed page stay useful whilst the technology underneath it keeps moving.

---

**Markers in this draft:** none, though the release terms depend on the deferred licence and format decisions, and one sentence here will need revisiting once those are taken.

---

## 8. Type F: the reader's-map preface

**The plan's reservation (§6.3):** it is navigation rather than a preface, and the existing "How to read this book" already does it well. Putting it first delays the reason to care until after the reader has been told how to care.

**Opens on:** routes through the book by role.
**Length here:** 221 words.

---

### Preface

If you want to start doing the work, begin at Chapter 3.
Most failures trace back to specification.
A scientist who can write a good one gets more out of an ordinary agent than a scientist who cannot gets out of a very good one.
Chapters 1 and 2 will still be there as reference when a term stops making sense.
From Chapter 3 you can go straight to whichever pattern chapter matches the work in front of you.
All five share one anatomy and none depends on the others.

If you are a research lead and you want the argument rather than the mechanics, read the closing chapter on adoption and the failure gallery in Chapter 13.
Between them they carry what a group needs to decide: what the discipline costs, what it catches, and what happens when it is not there.

If you came here sceptical, start at the failure gallery and work backwards.
It is the least flattering chapter in the book, and it is the one most likely to tell you whether the rest is worth your time.

Nobody should skip Chapter 11.
Verification is the discipline the whole book turns on, and taking the patterns without it means taking the dangerous half.
Everything else here is optional, reorderable and yours to use as suits you.

---

**Markers in this draft:** none. The content already exists as "How to read this book", which is why the plan leaves it where it is as a front-matter section immediately after the Preface.
