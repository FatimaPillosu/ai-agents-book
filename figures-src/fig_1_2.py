import sys; sys.path.insert(0, 'figures-src')
from house import *

f = Fig("12", "A model inside an agent inside a workflow",
        "Each layer adds what the one inside it cannot do on its own.")

# outer workflow container
f.rect(56, 196, 1488, 560, GREY, "none", 16, 2, dash="9 7")
f.text(78, 232, "agentic workflow", T_LABEL, fill=GREY, weight="600")

# specification tag
f.box(94, 300, 178, 92, "specification", HUMAN, "none")
f.block(94, 414, "written before the agent starts", width=24)

# agent container
f.rect(322, 268, 830, 336, AGENT, "none", 14, 2.6)
f.text(346, 302, "AI agent", T_LABEL, fill=AGENT, weight="600")

f.box(348, 330, 176, 84, "LLM", AGENT)
f.block(348, 434, "predicts text, cannot act", width=22)

f.o.append(f'<circle cx="640" cy="372" r="42" fill="none" stroke="{AGENT}" stroke-width="2.6"/>')
f.o.append(f'<path d="M612,352 a42,42 0 1 1 -4,34" fill="none" stroke="{AGENT}" stroke-width="2.6" marker-end="url(#ah12)"/>')
f.text(640, 366, "plan", T_ANNOT, "middle")
f.text(640, 383, "act observe", T_ANNOT, "middle")
f.block(566, 452, "acts, sees the result, decides again", width=22)

f.wrench(830, 366)
f.text(830, 408, "tools", T_LABEL, "middle")
f.block(756, 452, "does what the model does badly: arithmetic, retrieval, execution", width=22)

f.cylinder(1000, 328, 128, 88, "state / memory")
f.block(986, 452, "what survives between steps", width=22)

# arrows
f.arrow(272, 346, 322, 346)
f.arrow(1152, 436, 1236, 436)

# gate
f.diamond(1300, 436, 168, 124, "verification gate", GATE)
f.callout(1180, 620, 300, "nothing passes because it looks right", width=32)

# exits
f.arrow(1384, 436, 1452, 436, label="pass")
f.human(1490, 430)
f.text(1490, 486, "human decision", T_LABEL, "middle")
f.block(1400, 512, "accountable, and cannot delegate that", width=26, anchor="start")
f.elbow([(1300, 498), (1300, 690), (737, 690), (737, 604)], label="fail")

f.key(56, H - 78, [(HUMAN, "human"), (AGENT, "agent"), (TOOL, "tool"), (STORE, "data store"), (GATE, "gate")])
f.footer("Figure 1.2 · the model only predicts text; the loop, tools and memory make it act; the specification, gate and human decision make it defensible.")
f.save("figures/figure-1-2.svg")
print("written")
