# Glossary — plain-language terms

**Working glossary.** Every info-box in the book (`STYLE.md` §9) is collected here so a reader can look a word up from anywhere, not only where it first appears. Definitions are deliberately plain and warm; the precise treatment lives in the chapter that introduces the term. British English throughout. This file grows as each chapter is revoiced and its terms boxed; entries below cover Chapters 1 and 7.

---

**Large language model (LLM).** A program that has read an enormous amount of text and, given some words, predicts what words should come next. That is genuinely all it does — text in, text out. It has no memory of you between conversations, no goals of its own, and no way to touch anything in the world beyond the words it produces.

**AI agent.** An LLM with a job to do and the means to act on it: give it a goal, a set of tools it is allowed to use, and a loop that lets it try something, look at what happened, and decide the next step. The model is the reasoning part; the agent is the whole working arrangement built around it.

**Agentic workflow.** A designed process in which one or more agent steps sit inside fixed rails — defined inputs, checks the work must pass, and points where a human decides. The agent has room to choose how it does each step, but only inside boundaries you set before it starts. This book argues for building these, rather than turning an agent loose.

**Tool call (structured action).** The moment an agent stops writing prose and instead issues a precise, machine-readable instruction — run this code, fetch this record, query this database — and then reads the result back. It is what lets a text model actually *do* things rather than only describe them.

**In-context learning.** The knack, which appeared as models grew, of picking up a new task from nothing more than an instruction and a couple of examples written into the conversation — no retraining, no reprogramming. It is why you can direct these systems in ordinary written language.

**Context (context window).** The finite amount of text an agent can hold "in view" at one time — the conversation, the documents, the instructions, all of it. Think of it as a working desk with a fixed size: put too much on it and older things fall off the edge.

**Verification gate (gate).** A checkpoint in a workflow where the agent's work has to pass a defined check before anything downstream is allowed to use it. Pass, and the work moves on; fail, and it loops back. Nothing proceeds just because it looks right.

**Plausible failure.** The particular way these systems go wrong: not with an obvious error, but with an answer that is fluent, confident and completely wrong. Fluency and correctness are not the same thing here, which is why so much of this book is about checking.

**Pull request (merge request).** A proposal to fold a set of changes into the shared main line of work, which the version-control platform presents as a line-by-line difference for review. Comments attach to the exact lines they concern, the author answers or revises, and nothing lands until the accountable owner accepts the result. In this book's workflows it is the surface on which a scientist reads, questions and finally signs off an agent's work.
