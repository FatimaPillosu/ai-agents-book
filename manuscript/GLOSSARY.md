# Glossary — plain-language terms

**Working glossary.** Every demanding term explained in an info-box (`STYLE.md` §9) is collected here, together with a small number of terms the book leans on throughout, so a reader can look a word up from anywhere, not only where it first appears. Definitions are deliberately plain and warm; the precise treatment lives in the chapter that introduces the term, named in brackets after each entry. British English throughout. This edition covers Chapters 1–18.

---

**Acceptance criteria** (Chapter 3). The conditions an output has to meet before it counts as finished, written down in advance and, wherever possible, as checks someone other than the agent can apply. They are how you say what "correct" means before the work starts, so that "it looks right" never has to stand in for "it passed the check".

**Agentic workflow** (Chapter 1). A designed process in which one or more agent steps sit inside fixed rails — defined inputs, checks the work must pass, and points where a human decides. The agent has room to choose how it does each step, but only inside boundaries you set before it starts. This book argues for building these, rather than turning an agent loose.

**AI agent** (Chapter 1). An LLM with a job to do and the means to act on it: give it a goal, a set of tools it is allowed to use, and a loop that lets it try something, look at what happened, and decide the next step. The model is the reasoning part; the agent is the whole working arrangement built around it.

**Assumption registry** (Chapter 12). A running list of every "we're taking this as given" that a workflow leans on — each with why it was assumed, how confident you are, and who approved it. It turns assumptions that normally hide in someone's head and a few code comments into a record you can challenge before it does damage and consult after a result is questioned.

**Audit trail** (Chapter 12). A time-ordered, hard-to-tamper-with log of everything the workflow did — which tool ran, on which inputs, producing which outputs, under which version, passed by which human. Registries record what you decided; the audit trail records what actually happened, so a result can be reconstructed and defended afterwards even where it cannot be run again. That property is auditability, and it is weaker than reproducibility rather than stronger (Chapter 12 §12.4).

**Auditability** (Chapter 12). Being able to reconstruct and defend what was done afterwards: what ran, on what, under which specification, and who passed it. It is what a provenance record actually delivers, and it is weaker than reproducibility, because it does not let anyone repeat the work and get the same answer back. Agentic work delivers this one, and saying so plainly is a credibility gain rather than a loss.

**Calibration** (Chapter 1, and throughout). Setting an instrument against a known reference so you can trust its readings, and characterising where it drifts or fails before you rely on it. This book treats an agent the same way a scientist already treats a sensor or a numerical model: calibrated before deployment, its failure modes mapped, not trusted on first acquaintance.

**Calibration validity** (Chapter 11). A gate's measured miss rate is a reading taken on a date, not a standing property of the gate. So it carries a window, chosen by your group, past which it stops counting as evidence. A claim gated by an expired calibration is a claim whose evidence has quietly lapsed, which is a demotion in the record rather than a verdict that the work was wrong.

**Citation-verification gate** (Chapter 5). A checkpoint every citation must pass before the draft is allowed forward. A separate step — not the agent that wrote the draft — confirms that each cited work exists, that the quoted passage is really in it, and that the passage actually supports the claim made on it. Citations that fail are removed or sent back; nothing proceeds just because it reads well.

**Confident extrapolation** (Chapter 13). A claim that reaches past what the data actually support — beyond the range that was measured, outside the domain a relationship was fitted on — delivered in exactly the same assured tone as a well-grounded result. Nothing in the wording tells you the ground has run out; only checking the claim's reach against the evidence's reach does.

**Context (context window)** (Chapter 1). The finite amount of text an agent can hold "in view" at once — the conversation, the documents, the instructions, all of it. Picture a working desk of fixed size: pile too much on and older things slide off the edge.

**Context loss** (Chapter 13). An agent's working memory is finite and imperfect, so a constraint set early, a correction made ten steps ago, or an intermediate result can simply fall out of what the agent is currently holding. The agent then reasons confidently from the gap, because it cannot notice what it no longer represents.

**Data sovereignty** (Chapter 14). The principle that a dataset stays under the legal and physical control of the institution or nation that holds it, so that where the data lives, and who may move it, are governed by that holder's rules rather than by whoever wants to use it. For observational records it often means the numbers may be worked on, but not taken away.

**Disclosure statement** (Chapter 9). A short note attached to a paper or proposal that records how AI tools were used in producing it: which tool did which task, on what, and under whose oversight. It exists so an editor or reader can see the human accountability behind the work, and it is written from your own records rather than reconstructed from memory.

**Ensemble** (Chapter 10). In forecasting, a set of model runs started from slightly different conditions, whose spread is read as the forecast's uncertainty. The spread only means anything if the members can genuinely disagree; runs that share too much collapse together and become confidently wrong in unison — the same trap a set of near-identical agents falls into.

**Evaluation set** (Chapter 11). A fixed, curated set of test cases — each an input paired with the answer you already trust — that you run a workflow against to measure how good it is on your kind of work. It is the difference between "the agent seemed to do well" and "the agent reproduced the right answer on forty-seven of fifty cases I chose in advance". You build it once, guard it, and reuse it.

**Evidential tier** (Chapter 11). A named level of how well a claim has been checked, defined by the specific test it survived rather than by how much effort went in. Saying an output is "Tier 3" is a factual statement about evidence gathered, like citing a measurement's accuracy class — not a promise that you tried hard.

**False-negative rate** (Chapter 11). For a gate whose job is to catch bad work, the false-negative rate is how often it waves bad work through — says "pass" when it should have said "fail". It is the number that matters most and the one nobody measures by default, because a gate that never complains looks like a gate that works, right up until you find out it was asleep.

**In-context learning** (Chapter 1). The knack, which appeared as models grew larger, of picking up a new task from nothing more than an instruction and a couple of examples written into the conversation — no retraining, no reprogramming. It is why you can steer these systems in ordinary written language.

**Independent-method corroboration** (Chapter 11). A second determination of the same quantity by a method whose errors arise differently, agreeing with the first within the uncertainty each of them states. It is Tier 5 of the evidential hierarchy, and the environmental sciences' habitual strongest move: a satellite retrieval against a gauge, a physical model against an empirical one. The catch is that two methods sharing a hidden dependency corroborate nothing, so the independence of the error structures is something to argue for rather than assume.

**Independent reviewer** (Chapter 10). An agent whose only job is to find faults in another agent's work, set up so that its judgement does not simply echo the producer's: a different model where possible, a deliberately narrower view of the task, an instruction that rewards catching problems, and its own source of truth to check against. Independence is the whole point — a reviewer that shares the producer's model and context mostly agrees with it.

**Intercomparison** (Chapter 8). A controlled comparison in which several models are run on the same problem — the same domain, the same period, the same inputs — so that the only thing allowed to differ is the model itself. It is how a field works out which approach is genuinely better, rather than which happened to be tested on the easier case. Keeping every other condition identical is the whole discipline.

**Jagged frontier** (Chapter 1). A vivid way of describing how unevenly these systems perform: two tasks that feel equally hard to a person can sit on opposite sides of a line, one done flawlessly and the other botched. The edge between "reliable" and "unreliable" is jagged and often counter-intuitive, so it has to be mapped by testing, not guessed.

**Large language model (LLM)** (Chapter 1). A program that has read an enormous amount of text and, given some words, predicts what should come next. That is genuinely all it does: text in, text out. It has no memory of you between conversations, no goals of its own, and no way to touch anything beyond the words it produces.

**Least privilege** (Chapter 12). Give an agent the narrowest access that still lets it do the job, and nothing more — read this one folder, run this one tool, reach no further. Then a mistake, a bug or a hostile instruction can only do damage inside those narrow limits, because the power to do worse was never handed over in the first place.

**Open-weight model** (Chapter 14). A language model whose trained parameters — its "weights" — are published, so you can download it and run it on your own hardware, inside your own network, with nothing sent to an outside service. That is the opposite of a hosted model, which you can only reach by sending your input over the network to someone else's computer.

**Orchestration** (Chapter 2). Arranging several agent steps — and the checks and human decisions between them — into one larger workflow. Where a single agent is one worker, orchestration is the division of labour: who does what, in what order, and who checks whom. It is the layer where a workflow's reliability is actually engineered.

**Over-agreeable review (sycophancy)** (Chapter 13). A model asked to check work tends to side with whoever is asking, softening or dropping objections it would otherwise raise. It is a trained-in disposition to please, not laziness — which is why you cannot fix it by asking the model to be tougher: a system disposed to agree will agree that it should be tougher and then carry on agreeing about the work.

**Plan–act–observe loop** (Chapter 2). The cycle at the heart of every agent: the model proposes one action, something outside the model carries it out, the result comes back, and the model uses it to decide what to do next. Round and round until the work is done or a stop condition halts it. It is what turns a one-shot answer into a process that can, in the right conditions, correct itself.

**Plausible failure** (Chapter 1). The particular way these systems go wrong: not with an obvious error, but with an answer that is fluent, confident and completely mistaken. Fluency and correctness are separate things here — which is why so much of this book is about checking.

**Pre-commit hook** (Chapter 7). A small check that runs automatically the moment you try to save a change into version control, before the change is recorded. If the check fails — badly formatted code, a leftover password, a broken test — the save is refused until you fix it. It is a gate that needs no one to remember to open it.

**Prompt injection** (Chapter 12). When text an agent reads as part of its work — a web page, a downloaded file, a colleague's document — contains instructions, and the agent obeys them as if they came from you. The agent cannot reliably tell "content to analyse" from "orders to follow", so, in effect, the data can order your agent around.

**Propose–dispose separation** (Chapter 2). The agent proposes; something the agent does not control disposes. Three kinds of thing can do the disposing: a deterministic rule, where the criterion can be written as code; a human decision, where the criterion is judgement; and an external source of truth, where the criterion is a fact the agent cannot manufacture, such as a test suite or a reference dataset. What it buys is that fluent, wrong work cannot reach the record, because the model was never given the authority to write there. What it does not buy is a well-designed disposer.

**Provenance** (Chapter 12). The traceable record of where a result came from: which inputs fed it, which version of the workflow ran, what the agent did at each step, and who signed off. Provenance is what lets someone reconstruct and defend a result months later, instead of taking your word that it was "done carefully".

**Pull request (merge request)** (Chapter 7). A proposal to fold a set of changes into the shared main line of work, which the version-control platform presents as a line-by-line difference for review. Comments attach to the exact lines they concern, the author answers or revises, and nothing lands until the accountable owner accepts the result. In this book's workflows it is the surface on which a scientist reads, questions and finally signs off an agent's work.

**Quality-control flag** (Chapter 6). A marker attached alongside an observation that records a judgement about it — suspect, missing, corrected — without changing the measured value itself. The number you recorded stays exactly as it was; the flag simply travels with it, so anyone downstream can see what was doubted and why. Flagging is deliberately not the same as editing the data.

**Regression test** (Chapter 7). A test that pins down behaviour you have already confirmed is correct, by recording the output for a fixed input and asserting it again on every future run. Its whole job is to catch the day something quietly changes — a library update, a refactor — that would otherwise slip through unnoticed. It does not ask whether the answer is right in the abstract, only whether it still matches what you signed off before.

**Reproducibility, replicability and auditability** (Chapter 12). Three different properties, routinely run together and worth keeping apart. Reproducibility is the strictest: the same workflow on the same inputs returns the same answer. Replicability is the one science actually runs on: an independent group asks the same question by its own route and gets a compatible answer. Auditability is the weakest of the three and has its own entry above. An agentic workflow delivers the third and fails the first, because the same specification can return different work on a second run and the model behind a result can be withdrawn (Chapter 12 §12.4).

**Retrieval grounding** (Chapter 5). Rather than let the model answer from its own trained-in memory of the literature, you first fetch real documents and then require every sentence it writes to rest only on those fetched documents. The model still does the writing, but it is writing about texts placed in front of it rather than half-remembered ones. That is what later lets a check trace each claim back to a source that genuinely exists.

**Roster** (Chapter 10). A small, fixed set of agents with distinct jobs — a producer that does the work, an independent reviewer that checks it, a human who decides — arranged so that work passes between them through defined checks. The word borrows from a team sheet: named roles that answer for their part, not an undifferentiated crowd.

**Seeded-defect testing** (Chapter 11). You deliberately plant known mistakes into otherwise-correct work — a made-up reference, a wrong unit, a value outside the plausible range — and run your check over it without telling the check where the mistakes are. Then you count how many it caught. It is the fire drill for a verification gate: the only way to know an alarm works is to set off a fire you control.

**Specification** (Chapter 3). The written statement of a task that you hand an agent instead of a vague request: what the work is to achieve, what it may use, what counts as done, and when to stop. It is the difference between "have a look at this" and a brief precise enough that someone else could check whether the result meets it.

**Specification drift** (Chapter 13). When a job runs over many turns, the thing the agent is actually trying to do slowly slides away from what you first asked, one reasonable-looking accommodation at a time. No single step looks wrong; only the original written specification, held fixed and re-read, shows how far the target has moved.

**Stop condition** (Chapter 3). The rule that tells an agent when to stop — either because it has succeeded and the acceptance criteria are met, or because it has failed and cannot make progress, has used up an agreed budget of attempts, or has hit something the specification did not anticipate. Without the failure kind, an agent that cannot succeed simply does not stop.

**Sub-agent** (Chapter 2). A second agent that a coordinating agent hands a self-contained piece of work to, with its own tools and its own clean context. It does the messy or bulky part in isolation and passes back only the tidy result, so the coordinator never has to hold the mess in view.

**Task-grounded evaluation** (Chapter 11). Checking an agent's workflow on the real job you will use it for — your data, your conditions, your definition of a right answer — rather than trusting a score it earned on somebody else's benchmark. A leaderboard tells you how a system does on average across many strangers' tasks; task-grounded evaluation tells you how it does on yours, which is the only thing you can responsibly stake a result on.

**Token** (Chapter 2). The unit these models read and write in — roughly a short chunk of a word. Text is billed and measured by the token, so the length of everything an agent reads and produces, including its own steadily growing transcript, is literally what you pay for.

**Tool call (structured action)** (Chapter 1). The moment an agent stops writing prose and instead issues a precise, machine-readable instruction — run this code, fetch this record, query this database — and then reads the result back. It is what lets a text model actually *do* things rather than only describe them.

**Verification gate (gate)** (Chapter 1). A checkpoint in a workflow where the agent's work has to pass a defined check before anything downstream is allowed to use it. Pass, and the work moves on; fail, and it loops back. Nothing proceeds just because it looks right.
