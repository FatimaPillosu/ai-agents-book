import sys; sys.path.insert(0,'figures-src')
from templates import *

# ---------------- Figure 0.1 : icon key ----------------
f=Fig("01","The six actors, and what each one does",
      "Learn these six once; they do not change anywhere in the book.")
cells=[("human",HUMAN,"human","decides, and is accountable for the decision"),
       ("agent",AGENT,"agent","a language model working in a plan-act-observe loop"),
       ("tool",TOOL,"tool","a function or program the agent calls"),
       ("cyl",STORE,"data store","a dataset, a file, a record"),
       ("diamond",GATE,"gate","a check the work has to pass before it goes on"),
       ("reviewer",REVIEWER,"reviewer","checks someone else's work, independently")]
for i,(kind,col,name,desc) in enumerate(cells):
    cx=70+((1600-140)/3)*(i%3)+((1600-140)/6); cy=270+300*(i//3)
    if kind=="human": f.human(cx,cy,col,r=22)
    elif kind=="agent": f.agent_glyph(cx,cy,col,s=26)
    elif kind=="tool": f.wrench(cx,cy,col,s=22)
    elif kind=="cyl": f.cylinder(cx-46,cy-34,92,72,"",col)
    elif kind=="diamond": f.diamond(cx,cy,96,72,"",col)
    elif kind=="reviewer": f.human(cx,cy,col,r=22,tick=True)
    f.text(cx,cy+82,name,26,"middle",INK,"600")
    f.block(cx-210,cy+116,desc,width=34,anchor="start")
f.o.append(f'<line x1="70" y1="{H-96}" x2="1530" y2="{H-96}" stroke="{GREY}" stroke-width="1.4"/>')
f.segs.append((70,H-96,1530,H-96))
f.footer("These six keep the same icon and colour in every figure in this book.")
print("0.1",f.save("figures/figure-0-1.svg"))

# ---------------- Figure 1.1 : timeline ----------------
f=Fig("11","From text generation to structured action",
      "Seven datable changes, of which two were about the interface rather than the capability.")
ms=[("2017","transformer architecture","made training on very large text practical",0),
    ("2020","in-context learning","a task could now be described, not programmed",1),
    ("2022","public conversational systems","the shift became visible outside research",0),
    ("2023","tool calling","the model could act, not just describe",1),
    ("2023-24","long context","a whole codebase could be held at once",0),
    ("2024-25","coding agents · tool protocols","the work became checkable against tests",0),
    ("2026","governed agentic workflows","the subject of this book",0)]
yax=430; f.hline(80,1545,yax,INK,2.4)
colw=(1520-120)/7
for i,(yr,name,note,hot) in enumerate(ms):
    cx=120+colw*(i+.5)
    col=AGENT if hot else INK
    f.o.append(f'<circle cx="{cx}" cy="{yax}" r="11" fill="{col if hot else PAPER}" stroke="{col}" stroke-width="2.6"/>')
    f.borders.append((cx-11,yax-11,22,22))
    up = (i%2==0)
    if up:
        ty=f.block(cx-colw/2+8,yax-116,name,size=T_ANNOT+1,width=int((colw-16)/(15*CHAR)),fill=INK,weight="600")
        f.text(cx-colw/2+8,yax-140,yr,T_ANNOT+1,fill=col,weight="700")
        f.vline(cx,yax-52,yax-13,GREY,1.4,arrow=False)
        f.block(cx-colw/2+8,yax+46,note,width=int((colw-16)/(T_ANNOT*CHAR)))
    else:
        f.text(cx-colw/2+8,yax+56,yr,T_ANNOT+1,fill=col,weight="700")
        f.block(cx-colw/2+8,yax+82,name,size=T_ANNOT+1,width=int((colw-16)/(15*CHAR)),fill=INK,weight="600")
        f.vline(cx,yax+13,yax+34,GREY,1.4,arrow=False)
        f.block(cx-colw/2+8,yax-96,note,width=int((colw-16)/(T_ANNOT*CHAR)))
bracket(f,120+colw*3.5-colw/2+8,1545,700,"from here a system can act on what it says")
f.key([(AGENT,"the two interface changes"),(INK,"capability milestones")])
f.footer("Deliberately coarse and vendor-neutral: product-level detail lives in the repository, where it can be kept current.")
print("1.1",f.save("figures/figure-1-1.svg"))

# ---------------- Figure 1.2 : nesting ----------------
f=Fig("12","A model inside an agent inside a workflow",
      "Each layer adds what the one inside it cannot do on its own.")
f.rect(56,196,1488,516,GREY,"none",16,2,dash="9 7")
f.text(80,230,"agentic workflow",T_LABEL,fill=GREY,weight="600")
f.box(96,290,180,84,"specification",HUMAN,rx=18)
f.block(96,412,"written before the agent starts",width=22)
f.rect(330,252,806,208,AGENT,"none",14,2.5)
f.text(352,284,"AI agent",T_LABEL,fill=AGENT,weight="600")
f.box(360,308,150,74,"LLM",AGENT)
f.box(548,308,190,74,"plan - act - observe",AGENT,rx=34)
f.wrench(830,336); f.text(830,382,"tools",T_LABEL,"middle",inside=False)
f.cylinder(920,304,150,84,"state / memory")
f.block(360,500,"predicts text, cannot act",width=18)
f.block(548,500,"acts, sees the result, decides again",width=20)
f.block(772,500,"does what the model does badly: arithmetic, retrieval, execution",width=20)
f.block(962,500,"what survives between steps",width=20)
f.hline(276,330,332); f.hline(1136,1216,332)
f.diamond(1300,332,164,86,"verification gate",GATE)
f.callout(1180,436,262,"nothing passes because it looks right",width=26)
f.hline(1384,1420,332)
f.text(1404,312,"pass",T_ANNOT,"middle",SOFT)
f.human(1466,326); f.text(1466,382,"human decision",17,"middle")
f.block(1358,412,"accountable, and cannot delegate that",width=22)
f.elbow([(1300,398),(1300,660),(733,660),(733,606)])
f.text(1010,644,"fail",T_ANNOT,"middle",SOFT)
f.key([(HUMAN,"human"),(AGENT,"agent"),(TOOL,"tool"),(STORE,"data store"),(GATE,"gate")])
f.footer("The model only predicts text; the loop, tools and memory make it act; the specification, gate and human decision make it defensible.")
print("1.2",f.save("figures/figure-1-2.svg"))
