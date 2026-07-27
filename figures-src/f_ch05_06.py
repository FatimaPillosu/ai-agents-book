import sys; sys.path.insert(0,'figures-src')
from templates import *

# ---------------- 5.1 conventional vs agentic synthesis ----------------
f=Fig("51","Where the work moves, and where it does not",
      "The agent takes the time-consuming stages; you keep the one that decides what it means.")
band_title(f,70,196,"conventional",GREY)
cols=[70+((1600-140)/6)*(i+.5) for i in range(6)]
top_lab=["scientist","search","triage","read and note","draft","interpret"]
for i,lab in enumerate(top_lab):
    if i==0: f.human(cols[i],268); f.text(cols[i],322,lab,T_ANNOT,"middle",SOFT)
    elif i==5: f.box(cols[i]-95,240,190,64,lab,HUMAN)
    else: f.box(cols[i]-95,240,190,64,lab,INK)
    if i: f.hline(cols[i-1]+(24 if i==1 else 95)+4,cols[i]-95-6,272)
bracket(f,cols[1]-95,cols[3]+95,330,"most of the time goes here - and a body of work you never found leaves no trace")
band_title(f,70,470,"agentic")
f.box(cols[0]-95,510,190,58,"specification",HUMAN,rx=16)
f.rect(cols[1]-105,492,((cols[3]+105)-(cols[1]-105)),96,AGENT,"none",12,2.3)
f.text(cols[1]-88,478,"agent",T_ANNOT,"start",AGENT)
for i,lab in enumerate(["retrieve","triage","draft"]):
    f.box(cols[1+i]-80,512,160,54,lab,AGENT,lw=12)
f.hline(cols[0]+95+4,cols[1]-105-6,540)
f.cylinder(cols[2]-70,640,140,74,"corpus")
f.vline(cols[2],590,636,STORE,1.8,arrow=False)
f.block(cols[2]-70,748,"drafting may draw only on what was actually retrieved",width=44)
f.diamond(cols[4],540,190,80,"citation gate",GATE,lw=12)
f.hline(cols[3]+105+4,cols[4]-95-6,540)
f.block(cols[4]-30,640,"every claim traced to a source that exists and supports it",width=20)
f.box(cols[5]-95,508,190,64,"interpret and decide",HUMAN,lw=14)
f.hline(cols[4]+95+4,cols[5]-95-6,540)
f.vline(cols[5],306,500,GREY,1.5,dash="6 6",arrow=False)
f.footer("The interpret step sits in the same column in both rows on purpose: it is the one stage this redesign deliberately leaves alone.")
print("5.1",f.save("figures/figure-5-1.svg"))

# ---------------- 5.2 pipeline architecture ----------------
f=Fig("52","Retrieval-grounded synthesis, with the gate that makes it safe",
      "The model writes only about documents that were actually fetched, and a separate step checks every one.")
f.box(70,300,180,66,"specification",HUMAN,rx=16)
f.rect(320,240,420,220,AGENT,"none",12,2.4)
f.text(340,272,"retrieval and drafting agent",T_ANNOT,"start",AGENT)
f.box(348,292,150,60,"LLM",AGENT)
f.box(524,292,190,60,"plan - act - observe",AGENT,rx=30,lw=14)
f.wrench(392,398); f.wrench(452,398)
f.text(482,404,"bibliographic search · web search",T_ANNOT,"start",SOFT,inside=True)
f.hline(250,314,333)
f.block(70,404,"several vocabularies on purpose - the terminology is unsettled",width=18)
f.cylinder(430,540,200,86,"retrieved corpus")
f.vline(480,460,536,STORE,1.8,arrow=False); f.vline(580,536,460,STORE,1.8,arrow=False)
f.text(660,586,"drafting may draw on this and nothing else",T_ANNOT,"start",SOFT)
f.diamond(940,350,220,96,"citation-verification gate",GATE,lw=14)
f.hline(740,824,350)
f.human(940,204,REVIEWER,tick=True)
f.text(1000,208,"a separate step, not the drafting agent",T_ANNOT,"start",SOFT)
f.callout(1090,300,404,"three tests: the work exists · the passage is really in it · the passage supports the claim",width=34)
f.elbow([(940,402),(940,470),(770,470)]); f.text(870,490,"fail: removed or returned",T_ANNOT,"middle",SOFT)
f.hline(1054,1170,350); f.text(1112,334,"pass",T_ANNOT,"middle",SOFT)
f.human(1240,340); f.text(1240,398,"interpret and decide",T_ANNOT,"middle")
f.text(1240,424,"decides what the evidence means",T_ANNOT,"middle",SOFT)
f.vnote(1090,660,"a run where nothing fails is evidence the check is broken, not that the corpus was clean",GATE,width=44)
f.footer("Retrieval fills the corpus; drafting is confined to it; the gate tests every citation; interpretation stays with you.")
print("5.2",f.save("figures/figure-5-2.svg"))

# ---------------- 5.3 funnel ----------------
f=Fig("53","From retrieved corpus to interpreted synthesis",
      "The width lost at the gate is what makes what survives worth trusting.")
rows=[("retrieved",1000,STORE,"documents that do not bear on the question"),
      ("after triage",760,STORE,"every claim now carries a citation into the corpus"),
      ("claims drafted with citations",560,AGENT,"removed: fails exists / passage present / claim supported"),
      ("claims surviving the gate",380,GATE,"a named person decides what the surviving evidence means"),
      ("interpreted by the scientist",300,HUMAN,None)]
y=210
for i,(lab,w,col,note) in enumerate(rows):
    x=(1600-w)/2 - 140
    if col==GATE: f.rect(x,y,w,74,GATE,"none",8,2.6)
    else: f.panel(x,y,w,74,col,8); f.borders.append((x,y,w,74))
    f.text(x+w/2,y+44,lab,T_LABEL,"middle",INK if col!=STORE else INK,inside=True)
    f.text(x+w+24,y+30,"n = [AUTHOR]",T_ANNOT,"start",GREY)
    if note:
        f.text(x+w+24,y+58+14,note,T_ANNOT,"start",GATE if i==2 else SOFT)
    y+=74+36
f.callout(1150,300,380,"the width lost at the gate is the point - a gate that removes nothing has not been shown to work",width=32)
f.footer("Counts are the author's to supply - placeholders shown.")
print("5.3",f.save("figures/figure-5-3.svg"))

# ---------------- 6.1 propose-dispose ----------------
f=Fig("61","Agents propose, QC rules dispose",
      "The model never writes to the data. It only ever asks.")
for i,lab in enumerate(["gauge","rainfall","grid"]):
    f.cylinder(80,208+i*112,140,70,lab)
f.block(80,556,"different formats, timestamps, units and update cadences",width=17)
f.rect(310,220,390,260,AGENT,"none",12,2.4)
f.text(330,252,"QC agent",T_ANNOT,"start",AGENT)
f.box(336,272,150,56,"LLM",AGENT)
f.box(510,272,166,56,"plan - act - observe",AGENT,rx=28,lw=12)
f.wrench(370,392); f.wrench(430,392); f.wrench(490,392)
f.block(530,384,"format reader · unit resolver · neighbour query",width=16)
f.block(310,540,"no column enters without a declared, checked unit",width=28)
f.hline(224,304,350)
f.hline(700,806,350)
f.vnote(704,470,"proposals only - no write access to the data",GATE,width=18)
f.diamond(950,350,270,110,"deterministic QC rules",GATE,lw=16)
f.block(986,470,"physical bounds · rate limits · inter-station checks; code a human wrote and can rerun identically",width=26)
f.human(950,190); f.text(1030,182,"scientist",T_ANNOT,"start")
f.text(1030,206,"the authority the rules exercise",T_ANNOT,"start",SOFT)
f.vline(950,232,286,HUMAN,1.6,arrow=False)
f.hline(1088,1180,350); f.text(1134,334,"apply flag",T_ANNOT,"middle",SOFT)
f.cylinder(1190,306,170,88,"flagged record")
f.block(1190,438,"the measured value is never overwritten",width=20)
f.elbow([(890,458),(890,600),(1180,600)]); f.text(1044,584,"reject",T_ANNOT,"middle",SOFT)
f.cylinder(1190,556,170,88,"rejection log",GREY)
f.text(1190,680,"kept, with the reason it was rejected",T_ANNOT,"start",SOFT)
f.cylinder(1382,430,150,84,"provenance store")
f.vline(1330,398,424,STORE,1.5,dash="5 5",arrow=False)
f.vline(1330,552,518,STORE,1.5,dash="5 5",arrow=False)
f.block(1382,548,"keyed to the input files and the rule-set version",width=16)
f.footer("The agent reads, normalises and proposes with justification; only deterministic rules, under a scientist's authority, dispose.")
print("6.1",f.save("figures/figure-6-1.svg"))

# ---------------- 6.2 four-stage sequence ----------------
f=Fig("62","Ingest, propose, dispose, record",
      "Everything left of the red line is a request; everything right of it is a decision.")
heads=[("agent","ingest and normalise",AGENT),("agent","propose flags",AGENT),
       ("diamond","dispose",GATE),("cyl","record provenance",STORE)]
steps=[(0,0,"1 raw series in","different formats, one tidy representation",INK),
       (0,0,"2 normalise units + UTC","an unresolved unit halts the pipeline rather than defaulting",INK),
       (0,1,"3 propose flags + justification","each proposal carries its evidence and the neighbouring context weighed",INK),
       (2,3,"4 physical bounds + inter-station","the rules can reject a proposal the agent was confident about",INK),
       (2,3,"5 apply flag / reject","a rejection is logged, and the observation stands as measured",INK),
       (2,3,"6 write provenance","keyed to the inputs and the rule-set version, so the record can be reconstructed",INK)]
xs=lanes(f,heads,steps,top=196,first=330,last=690)
xm=(xs[1]+xs[2])/2
f.vline(xm,300,724,GATE,3,arrow=False)
f.text(xm,760,"authority boundary - agent proposes, rules dispose",T_ANNOT,"middle",GATE)
f.footer("One observation, six steps: the pattern never lets the agent cross the line.")
print("6.2",f.save("figures/figure-6-2.svg"))

# ---------------- 6.3 before/after QC ----------------
f=Fig("63","What changes, and what stays exactly as it was",
      "The checks are identical in both rows. Only what surrounds them changes.")
band_title(f,70,200,"conventional",GREY)
f.human(130,282); f.text(130,338,"analyst",T_ANNOT,"middle",SOFT)
f.box(230,246,230,64,"per-format loaders",TOOL,lw=16)
f.box(520,246,230,64,"hand-tuned checks",GATE,lw=16)
f.box(810,246,230,64,"plot and eyeball",STORE,lw=16)
f.hline(160,224,278); f.hline(460,514,278); f.hline(750,804,278)
f.block(1090,258,"reasoning lost in comments",width=22,fill=GREY)
f.block(230,352,"effort scales with the number of station-format combinations, not with the science",width=52)
f.block(1090,306,"why this spike was accepted is rarely reconstructable six months later",width=26)
band_title(f,70,480,"agentic redesign")
f.cylinder(100,520,140,72,"raw inputs")
f.box(310,522,200,64,"QC agent",AGENT)
f.hline(244,304,554); f.hline(510,566,554); f.text(538,538,"propose",T_KEY,"middle",SOFT)
f.box(572,522,230,64,"deterministic rules",GATE,lw=16)
f.hline(802,856,554)
f.cylinder(862,518,170,76,"flagged record")
f.cylinder(1100,518,180,76,"provenance store")
f.hline(1032,1094,554)
f.block(310,640,"takes the format-wrangling and writes the justification",width=24)
f.block(1100,640,"the record now carries why each flag was applied",width=24)
f.o.append(f'<path d="M635,318 v58 M635,376 h52 M687,376 v138" fill="none" stroke="{INK}" stroke-width="1.8" stroke-dasharray="5 5"/>')
f.segs.append((635,318,635,376)); f.segs.append((635,376,687,376)); f.segs.append((687,376,687,514))
f.text(710,398,"same checks, same authority - retained",T_ANNOT,"start",INK)
f.text(710,424,"what changed is what surrounds them",T_ANNOT,"start",SOFT)
f.footer("The manual pattern-recognition goes, and so does the loss of reasoning into comments nobody reads six months later.")
print("6.3",f.save("figures/figure-6-3.svg"))

# ---------------- 6.4 annotated trace ----------------
f=Fig("64","One trace, three dispositions",
      "Event B is the one that matters: a fluent proposal, wrong, caught by a rule.")
x0,x1=110,1500
f.text(56,232,"river stage",T_ANNOT,"start",SOFT)
pts=[(110,430),(240,430),(320,336),(400,430),(560,430),(640,300),(700,430),(900,430)]
poly=" ".join(f"{x},{y}" for x,y in pts)
f.o.append(f'<polyline points="{poly}" fill="none" stroke="{INK}" stroke-width="2.4"/>')
f.o.append(f'<polyline points="1020,430 1100,430" fill="none" stroke="{INK}" stroke-width="2.4"/>')
f.o.append(f'<polyline points="1100,430 1180,352 1280,430 1500,430" fill="none" stroke="{INK}" stroke-width="2.4"/>')
f.panel(900,404,120,52,"#E4E4E0",4)
f.text(960,478,"C",T_LABEL,"middle",GREY,weight="700")
f.text(56,600,"rainfall",T_ANNOT,"start",SOFT)
import random
bars=[(300,54),(320,84),(340,60),(620,10),(1140,66),(1160,88),(1180,52)]
for bx,bh in bars:
    f.panel(bx,676-bh,16,bh,STORE,2)
f.o.append(f'<line x1="{x0}" y1="676" x2="{x1}" y2="676" stroke="{GREY}" stroke-width="1.6"/>')
f.segs.append((x0,676,x1,676))
f.text(320,204,"A",T_LABEL,"middle",TOOL,weight="700")
f.text(320,236,"accepted: rainfall-backed spike",T_ANNOT,"middle",SOFT)
f.text(640,204,"B",T_LABEL,"middle",GATE,weight="700")
f.text(640,236,"rejected by rule: no rainfall, exceeds rate limit",T_ANNOT,"middle",GATE)
f.vline(320,246,320,TOOL,1.5,dash="4 4",arrow=False)
f.vline(640,246,288,GATE,1.5,dash="4 4",arrow=False)
f.callout(760,236,420,"the agent proposed accepting B too - a fluent proposal, and simply wrong; caught by a physical rate-of-change rule, not by anyone reading the output",width=38)
f.text(960,516,"gap flagged, not filled - the agent may classify a gap; it may never write a value into one",T_ANNOT,"start",SOFT)
f.text(1180,478,"A2",T_ANNOT,"middle",TOOL)
f.footer("Every disposition here, including B's rejection, is written to provenance with its reason. [AUTHOR: replace the schematic events with three real ones.]")
print("6.4",f.save("figures/figure-6-4.svg"))
