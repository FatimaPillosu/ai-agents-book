# Further reading — annotated (skeleton)

**Status:** skeleton · back matter (outline §9) · drawn **only** from the verified research sweep in `/research` (`2026-07-24-agentic-ai-foundations-sweep.md`).
**Conventions:** British English · every entry carries a DOI or URL from the sweep · preprints and unconfirmed details keep **[verify]** exactly as the sweep flagged them · nothing added from memory. Named products and frameworks appear here only as bibliographic references, never as prose recommendations (outline §9).

This list is organised by the book's five parts, so a reader can follow up the chapter they have just read. It is a **skeleton**: it lays out what the first research sweep verified, with a one-line note on why each source is worth a working scientist's time. The author's curation is owed on top of it.

**[AUTHOR: confirm the final selection and ordering. This skeleton lists every source the 24 July 2026 sweep verified; a back-matter list is more useful curated down to the few readings that repay the effort, with the rest left to the repository. Mark the provenance of anything you add that the sweep did not cover.]**

**[AUTHOR: decide whether the annotations stay this terse or gain a sentence of your own judgement — a further-reading list reads better in the author's voice than in a paraphrase of the sweep.]**

---

## Part I — Foundations (Chapters 1–4)

- **Yao, S., et al. (2023). ReAct: synergizing reasoning and acting in language models.** ICLR 2023. Preprint: https://arxiv.org/abs/2210.03629 — The founding statement of the plan–act–observe pattern underlying essentially every current agent; read it as the conceptual origin (c. 2022), not current practice.
- **Schick, T., et al. (2023). Toolformer: language models can teach themselves to use tools.** NeurIPS 2023. Preprint: https://arxiv.org/abs/2302.04761 — Establishes tool use as learnable model behaviour rather than bolted-on engineering; the origin of the "tools" leg of the agent anatomy.
- **Wang, L., et al. (2023, rev. 2024). A survey on large language model based autonomous agents.** https://arxiv.org/abs/2308.11432 — A taxonomic map (profile, memory, planning, action) to cross-check the book's anatomy against; cite for the state of the field, not for any specific capability claim. **[verify journal version — Frontiers of Computer Science, 2024]**
- **Sumers, T. R., et al. (2023/2024). Cognitive architectures for language agents (CoALA).** TMLR. Preprint: https://arxiv.org/abs/2309.02427 — The strongest academic scaffold for the context-and-memory picture; descriptive, not validated.
- **Feng, K. J. K., McDonald, D. W., & Zhang, A. X. (2025). Levels of autonomy for AI agents.** https://arxiv.org/abs/2506.12469 — Frames autonomy as a design decision separable from capability, with five human-role levels; a useful proposed vocabulary, not an established standard. **[verify peer-review status]**
- **Anthropic (2024). Building effective agents.** https://www.anthropic.com/engineering/building-effective-agents — Influential practitioner guidance on workflows-versus-agents and the "simplest thing that works" principle; high-quality grey literature, experiential rather than measured.
- **Schulhoff, S., et al. (2024, rev. 2025). The Prompt Report: a systematic survey of prompt engineering techniques.** https://arxiv.org/abs/2406.06608 — The most comprehensive prompting survey; supports Chapter 3's move from conversational prompting to written specification. **[verify peer-reviewed venue]**

**[AUTHOR: Chapter 3's specification schema is the book's own synthesis — the sweep found no dedicated academic treatment of agent task specification. If you want a further-reading anchor here, it will have to be adjacent (the Prompt Report above; τ-bench's policy-document mechanism under Part III). Flag this gap or leave it.]**

## Part II — Core patterns (Chapters 5–10)

- **Boiko, D. A., et al. (2023). Autonomous chemical research with large language models (Coscientist).** *Nature*, 624, 570–578. DOI: 10.1038/s41586-023-06792-0 — The flagship peer-reviewed demonstration of an LLM system planning and running real experiments; a capability existence proof, with curated successes in a fast-feedback domain.
- **Lála, J., et al. (2023). PaperQA: retrieval-augmented generative agent for scientific research.** https://arxiv.org/abs/2312.07559 — The central architectural citation for Chapter 5: retrieval-grounded synthesis with citations checked against retrieved documents. **[verify successor versions before citing beyond this record]**
- **Cao, C., et al. (2025). Automation of systematic reviews with large language models (otto-SR).** *medRxiv*. DOI: 10.1101/2025.06.13.25329541 — The strongest quantitative evidence that LLM assistance can exceed humans on the mechanical layers of evidence synthesis; developer-run, clinical-literature. **[verify journal status before release]**
- **Lu, C., et al. (2024). The AI Scientist: towards fully automated open-ended scientific discovery.** https://arxiv.org/abs/2408.06292 — Both milestone and warning: full-pipeline automation, and documented failure modes including a system relaxing its own constraints and a lenient automated reviewer. Never a validation of automated authorship.
- **Cemri, M., et al. (2025). Why do multi-agent LLM systems fail? (MAST).** https://arxiv.org/abs/2503.13657 — The single most useful source for Chapters 10 and 13: an empirical 14-mode failure taxonomy, with specification and verification, not model weakness, as the largest categories. **[verify venue — OpenReview record exists]**
- **Wu, Q., et al. (2023). AutoGen: enabling next-gen LLM applications via multi-agent conversation.** https://arxiv.org/abs/2308.08155 — Architectural vocabulary for roles-and-rosters, including the human gate as a first-class member; a feasibility description, not a reliability result. **[verify reviewed venue — COLM 2024]**
- **Du, Y., et al. (2023/2024). Improving factuality and reasoning through multiagent debate.** ICML 2024. Preprint: https://arxiv.org/abs/2305.14325 — Peer-reviewed support that independent instances improve quality — and its limit: consensus is not correctness, so similar models can agree on a shared error.

## Part III — Trust (Chapters 11–13)

*The book's centre of gravity; the sweep's deepest coverage.*

- **Zheng, L., et al. (2023). Judging LLM-as-a-judge with MT-Bench and Chatbot Arena.** NeurIPS 2023 D&B. Preprint: https://arxiv.org/abs/2306.05685 — The founding LLM-as-judge paper, documenting both usable human agreement and systematic biases (position, verbosity, self-enhancement). Start here for any automated-review discussion.
- **Sharma, M., et al. (2023). Towards understanding sycophancy in language models.** ICLR 2024. Preprint: https://arxiv.org/abs/2310.13548 — The definitive study of over-agreeableness and its root in preference training; claim the mechanism with confidence, current magnitudes with caution.
- **Shi, L., et al. (2024). Judging the judges: a systematic study of position bias in LLM-as-a-judge.** https://arxiv.org/abs/2406.07791 — Measures judge bias at scale and shows it concentrates on borderline cases — exactly the cases that matter at a gate. **[verify final venue — AACL–IJCNLP 2025]**
- **Wataoka, K., et al. (2024). Self-preference bias in LLM-as-a-judge.** https://arxiv.org/abs/2410.21819 — Judges favour text familiar to them, so same-family draft-and-review is structurally biased towards approval; the case for cross-family review. **[verify peer-reviewed status]**
- **Jimenez, C. E., et al. (2023). SWE-bench: can language models resolve real-world GitHub issues?** ICLR 2024. Preprint: https://arxiv.org/abs/2310.06770 — The exemplar of execution-based, pre-existing-test verification, and a lesson in its limits (test coverage sets the gate's own miss rate).
- **Mialon, G., et al. (2023). GAIA: a benchmark for general AI assistants.** https://arxiv.org/abs/2311.12983 — Tasks simple for people, hard for AI, with unambiguous auto-checkable answers; a template for designing verifiable in-house sub-tasks.
- **Yao, S., et al. (2024). τ-bench: tool-agent-user interaction in real-world domains.** https://arxiv.org/abs/2406.12045 — Introduces policy-document compliance and the pass^k reliability metric; single-trial success rates overstate dependability, which matters for operational duty cycles. **[verify reviewed venue]**
- **Yehudai, A., et al. (2025, rev. 2026). Survey on evaluation of LLM-based agents.** https://arxiv.org/abs/2503.16416 — The most complete map of agent evaluation and its named gaps (cost, safety, trajectory-level assessment). **[verify; a peer-reviewed survey by Mohammadi et al., DOI 10.1145/3711896.3736570, can substitute]**
- **Kapoor, S., et al. (2024). AI agents that matter.** https://arxiv.org/abs/2407.01502 — Cost as a first-class evaluation axis; simple baselines match complex scaffolds at a fraction of the cost. Load-bearing for Chapters 11 and 16. **[verify archival venue]**
- **Zhu, Y., et al. (2025). Establishing best practices for building rigorous agentic benchmarks.** https://arxiv.org/abs/2507.02825 — Audits ten benchmarks and finds most have grading flaws that pass failing work; the strongest evidence that automated verification is itself an instrument with a measurable error rate. **[verify venue]**
- **Walters, W. H., & Wilder, E. I. (2023). Fabrication and errors in the bibliographic citations generated by ChatGPT.** *Scientific Reports*, 13, 14045. DOI: 10.1038/s41598-023-41032-5 — The rigorous quantification behind Chapter 13's first gallery entry; fabricated citations look legitimate, which is why verification must be mechanical.
- **Cabezas-Clavijo, Á., & Sidorenko-Bautista, P. (2025). Assessing the performance of 8 AI chatbots in bibliographic reference retrieval.** https://arxiv.org/abs/2505.18059 — A 2025 update showing citation fabrication persists across the current model generation, and varies by system and domain. **[verify final publication — Journal of Data and Information Science, 2026]**
- **Huang, L., et al. (2023). A survey on hallucination in large language models.** https://arxiv.org/abs/2311.05232 — The standard taxonomy (factuality versus faithfulness) and causal analysis; supports treating hallucination as a property to manage, not a bug awaiting a fix. **[verify journal DOI — ACM TOIS, 2025]**

## Part III / Chapter 12 — Governance and security

- **Greshake, K., et al. (2023). Not what you've signed up for: compromising real-world LLM-integrated applications with indirect prompt injection.** AISec '23. DOI: 10.1145/3605764.3623985. Preprint: https://arxiv.org/abs/2302.12173 — Defined indirect prompt injection: anything an agent reads can act as a command. The one security idea every scientist deploying agents must internalise.
- **Beurer-Kellner, L., et al. (2025). Design patterns for securing LLM agents against prompt injections.** https://arxiv.org/abs/2506.08837 — Six architectural patterns giving injection resistance by construction, each trading capability for safety. The bridge from principle to buildable workflow shape. **[verify venue]**
- **OWASP GenAI Security Project (2025). OWASP Top 10 for LLM applications 2025.** https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/ — The institutional-language list your IT team already speaks; "excessive agency" (LLM06) names the book's least-privilege stance. Cite the 2025 edition explicitly.
- **NIST (2024). AI risk management framework: generative AI profile (NIST AI 600-1).** https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf — The US federal risk vocabulary (including environmental impacts of training and inference), aligned with the book's registry-and-audit apparatus. Guidance, not regulation; US-specific.

## Part IV — Case studies (Chapters 14–15)

*Domain evidence: how environmental science itself adopts AI under verification.*

- **Lam, R., et al. (2023). Learning skillful medium-range global weather forecasting (GraphCast).** *Science*, 382(6677), 1416–1421. DOI: 10.1126/science.adi2336 — The ML weather model operational meteorology could not ignore; note its own careful, pre-existing verification scorecard.
- **Bi, K., et al. (2023). Accurate medium-range global weather forecasting with 3D neural networks (Pangu-Weather).** *Nature*, 619, 533–538. DOI: 10.1038/s41586-023-06185-3 — The first ML model shown to beat operational NWP across variables; its temporal-aggregation trick parallels compounding-error management in agent pipelines.
- **Lang, S., et al. (2024). AIFS — ECMWF's data-driven forecasting system.** https://arxiv.org/abs/2406.01465 — The load-bearing domain precedent: a conservative operational centre adopting AI under governance — parallel running, published verification, staged operationalisation. **[verify journal version]**
- **Ben Bouallègue, Z., et al. (2024). The rise of data-driven weather forecasting: a first statistical assessment in an operational-like context.** *BAMS*, 105(6). DOI: 10.1175/BAMS-D-23-0162.1 — The model of independent, task-grounded re-verification of a vendor's claims on your own data and conditions; the strongest bridge between the meteorological reader and the verification thesis.
- **Kochkov, D., et al. (2024). Neural general circulation models for weather and climate (NeuralGCM).** *Nature*, 632, 1060–1066. DOI: 10.1038/s41586-024-07744-y — The hybrid physics–ML track; note the authors' explicit caution that the model does not extrapolate reliably to substantially different climates.
- **Kratzert, F., et al. (2019). Towards learning universal, regional, and local hydrological behaviours via machine learning.** *HESS*, 23, 5089–5110. DOI: 10.5194/hess-23-5089-2019 — Hydrology's own pre-LLM deep-learning inflection, made credible by large-sample, held-out, metric-specified testing.
- **Arsenault, R., et al. (2023). Continuous streamflow prediction in ungauged basins: LSTM networks clearly outperform traditional models.** *HESS*, 27, 139–157. DOI: 10.5194/hess-27-139-2023 — Independent, adversarially framed confirmation of the LSTM result; claim-verification by replication within the domain.
- **Zhu, [initial unconfirmed], et al. (2026). Large language models as calibration agents in hydrological modeling: feasibility and limitations.** *Geophysical Research Letters*. DOI: 10.1029/2025GL120043 — The closest published work to the book's territory; demonstrates currency, and the governance gap the book fills. **[verify author list, scope and stated limitations from the paper — paywalled at sweep time]**
- **Pantiukhin, D., et al. (2025). Accelerating earth science discovery via multi-agent LLM systems.** *Frontiers in Artificial Intelligence*, 8. DOI: 10.3389/frai.2025.1674927 — An in-domain multi-agent architecture sketch whose self-admitted evaluation gap is itself evidence that verification is the missing layer. A Perspective; cite its claims as informed opinion.

## Part V — Adoption and policy (Chapters 9, 16–17)

- **Nature (editorial) (2023). Tools such as ChatGPT threaten transparent science; here are our ground rules for their use.** *Nature*, 613, 612. DOI: 10.1038/d41586-023-00191-1 — The editorial that set the pattern: no AI author (accountability cannot be borne by a tool), and disclose AI use. The anchor for "agents are never authors".
- **Naddaf, M. (2025). Is it OK for AI to write science papers? Nature survey shows researchers are split.** https://www.nature.com/articles/d41586-025-01463-8 — The best snapshot of divided community norms; adoption runs ahead of disclosure, and attitudes split by career stage, region and language. Cite the split and its axes, not precise percentages. **[verify author byline]**
- **National Institutes of Health (2023). Generative AI prohibited for the NIH peer review process.** NIH Guide Notice NOT-OD-23-149. https://grants.nih.gov/grants/guide/notice-files/NOT-OD-23-149.html — The funder-grade articulation of the confidentiality rationale: material whose onward use you cannot control must not enter a third-party service. **[verify current NIH AI policy state]**
- **European Commission, DG Research and Innovation (2024; updated 8 May 2026). Living guidelines on the responsible use of generative AI in research (ERA).** https://research-and-innovation.ec.europa.eu/document/download/2b6cf7e5-36ac-41cb-aab5-0d32050143dc_en — The European policy-class anchor: researcher responsibility, verification, disclosure, no AI in evaluation; itself a living document, the model the book recommends groups adopt. **[verify the 2026 update's provisions against the updated PDF]**

---

## Gaps the sweep named (for the author and a follow-up sweep)

The research sweep recorded coverage limits the further-reading list should not paper over. Two matter most for the book's own argument, and the author may wish to say so plainly here rather than leave the list looking complete:

- **No study directly measures the false-negative rate of LLM review gates** — Chapter 11's centre of gravity. The nearest evidence is the judge-bias and benchmark-validity literature above; this is a genuine gap and a target for a follow-up sweep.
- **Theme "specification for agents" is thin in the peer-reviewed literature** — Chapter 3's schema is presented as the book's own synthesis, anchored on adjacent prompting and policy-document evidence.

**[AUTHOR: decide whether this gaps section belongs in the printed back matter or only in the repository. If it stays, a sentence in your voice on why these gaps are honestly named — rather than hidden — would suit the book's stance.]**

**[AUTHOR: the sweep was a single pass (US-weighted web search; no Scopus, Web of Science or Google Scholar; some paywalls). Further sweeps are planned on review-gate measurement, the EU AI Act, WMO/national-met-service statements on operational AI, inference energy and carbon with defensible numbers, and the agentic-AI-in-hydrology frontier. Note here which additions you want reflected before release.]**
