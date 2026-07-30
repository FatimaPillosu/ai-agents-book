import sys; sys.path.insert(0,'figures-src')
from templates import *

# ---------------- 9.1 transcription vs artefact-linked ----------------
f=Fig("91","Manual transcription versus artefact-linked assembly",
      "A copy does not update when its source changes.")
band_title(f,70,200,"conventional",GREY)
f.cylinder(100,240,170,76,"analysis outputs",GREY)
f.box(430,246,170,64,"figure",GREY,lw=12)
f.hline(272,424,278); f.text(348,262,"hand-copied",T_KEY,"middle",SOFT)
f.box(760,246,190,64,"manuscript",GREY,lw=14)
f.hline(600,754,278); f.text(676,262,"typed by hand",T_KEY,"middle",SOFT)
f.diamond(348,352,120,52,"risk",GATE,lw=8)
f.diamond(676,352,120,52,"risk",GATE,lw=8)
f.vnote(1010,262,"each copy can silently diverge - a copy does not update when its source changes",GATE,width=28)
f.block(100,410,"a figure generated from an earlier data file than the table beside it; a value updated in the table but not in the text",width=52)
band_title(f,70,500,"artefact-linked")
f.cylinder(100,540,170,76,"analysis outputs")
f.box(400,544,260,66,"figure / table generation",TOOL,lw=20)
f.hline(272,394,578)
f.agent_glyph(760,570); f.text(760,626,"assembly agent",T_ANNOT,"middle",SOFT)
f.hline(660,736,578)
f.box(880,544,210,66,"manuscript draft",INK,lw=16)
f.hline(784,874,578)
f.human(1190,568); f.text(1190,624,"author control",T_ANNOT,"middle")
f.hline(1090,1166,578)
f.block(1290,548,"the author accepts, edits or rejects - nothing lands unread",width=20)
f.text(400,660,"one source, regenerated",T_ANNOT,"start",HUMAN)
f.footer("A number in the abstract now traces to a computation, not a recollection.")
print("9.1",f.save("figures/figure-9-1.svg"))

# ---------------- 9.2 assembly architecture ----------------
f=Fig("92","Manuscript assembly from pipeline artefacts under an author gate",
      "The agent describes what was done. It never decides what it means.")
f.cylinder(90,240,210,84,"pipeline artefacts")
f.cylinder(90,400,210,84,"provenance records")
f.block(90,530,"one source for every number and every figure",width=20)
f.agent_glyph(470,330); f.text(470,388,"assembly agent",T_ANNOT,"middle")
f.hline(302,428,300); f.hline(302,428,420)
tools=[("figure generation",None),("table generation",None),
       ("section drafting","descriptive - checkable against artefacts that already exist"),
       ("disclosure drafting","assembled from the record, not reconstructed from memory")]
for i,(lab,ann) in enumerate(tools):
    yy=470+i*74
    f.box(400,yy,240,56,lab,TOOL,lw=18)
    if ann: f.block(660,yy+22,ann,width=42)
f.vline(470,412,464)
bracket(f,400,640,772,"generated, not hand-copied")
f.hline(512,600,330)
f.diamond(760,330,220,96,"author-control gate",GATE,lw=14)
f.block(690,470,"the author is the sole interpretive authority, and reads every sentence they sign",width=26)
f.hline(872,960,330); f.text(914,314,"accept",T_KEY,"middle",SOFT)
f.box(970,258,220,62,"manuscript",INK,lw=16)
f.box(970,344,220,62,"disclosure statement",INK,lw=16)
f.elbow([(760,382),(760,430),(628,430)])
f.text(700,448,"revise",T_KEY,"middle",SOFT)
f.vnote(1240,262,"the agent may describe what was done; it never originates a claim about what the results establish",GATE,width=26)
f.footer("Good provenance for verification buys the disclosure statement almost for free.")
print("9.2",f.save("figures/figure-9-2.svg"))

# ---------------- 9.3 disclosure flowchart ----------------
f=Fig("93","Deciding what to disclose, and whether a use is permitted at all",
      "Answer these from your record, not from memory.")
cx=470
f.box(cx-190,182,380,58,"agent used in preparing this output",AGENT,lw=30)
f.vline(cx,240,272)
f.diamond(cx,338,330,92,"does the venue bar this task?",GATE,lw=20)
f.block(56,300,"some venues forbid agent-generated figures, data or citations outright",width=22)
f.hline(cx+169,1010,338); f.text(820,322,"yes",T_ANNOT,"middle",SOFT)
f.box(1020,304,300,68,"do not use; find a permitted alternative",GATE,lw=22)
f.vline(cx,384+2,428); f.text(cx-26,414,"no",T_ANNOT,"end",SOFT)
f.diamond(cx,498,330,92,"confidential manuscript under review?",GATE,lw=22)
f.vnote(56,470,"once material is sent, its onward path is beyond your control",GATE,width=22)
f.hline(cx+169,1010,498); f.text(820,482,"yes",T_ANNOT,"middle",SOFT)
f.box(1020,464,300,68,"keep off external systems",GATE,lw=22)
f.vline(cx,544+2,588); f.text(cx-26,574,"no",T_ANNOT,"end",SOFT)
f.diamond(cx,656,330,92,"disclosure required or best practice?",GATE,lw=22)
f.text(56,650,"when in doubt, disclose",T_ANNOT,"start",INK,weight="600")
f.hline(cx+169,860,656)
f.box(870,600,330,64,"generate disclosure from provenance records",TOOL,lw=26)
f.block(870,692,"assembled to whatever granularity the venue asks for, because the record already exists",width=40)
f.hline(1200,1270,632)
f.human(1330,622); f.text(1330,678,"author confirms",T_ANNOT,"middle")
f.footer("No agent is ever listed or implied as an author - that class of rule is stable where the others move.")
print("9.3",f.save("figures/figure-9-3.svg"))

# ---------------- 9.4 reviewer-response lanes ----------------
f=Fig("94","Clerical structuring, human judgement, clerical assembly",
      "The agent takes both ends. You take all of the middle.")
f.panel(70,455,1460,64,"#DCE9F4",8)
xs=lanes(f,[("agent","agent",AGENT),("cyl","pipeline",STORE),("human","author",HUMAN)],
  [(0,0,"1 parse review to comment table","the reviewer's exact wording, quoted verbatim",INK),
   (0,2,"2 propose classification","a proposal, not a decision",INK),
   (2,2,"3 decide each response","human interpretive authority - is the reviewer right, and what should change?",HUMAN),
   (2,1,"4 regenerate from pipeline",None,INK),
   (1,2,"5 verify against result files","verify before use",GATE),
   (0,2,"6 assemble reply - author reads in full","the agent formats; the author reads it all before submission",INK)],
  top=200,first=330,last=712)
f.footer("Steps 1, 2 and 6 are clerical and belong to the agent; step 3, in the blue band, is yours alone.")
print("9.4",f.save("figures/figure-9-4.svg"))

# ---------------- 10.1 second-agent flowchart ----------------
f=Fig("101","When a second agent adds information, and when it adds only cost",
      "Agreement between near-identical agents is not corroboration.")
cx=480
f.box(cx-170,186,340,56,"proposed second agent",GREY,lw=26)
f.vline(cx,242,276)
f.diamond(cx,356,360,104,"names an error class the roster misses?",GATE,lw=22)
f.elbow([(cx+184,356),(1050,356)]); f.text(800,340,"no",T_ANNOT,"middle",SOFT)
f.box(1060,322,330,68,"drop - add a deterministic gate instead",GREY,lw=24)
f.block(1060,414,"if a rule can check it, a gate is cheaper and more reliable than an agent",width=30)
f.vline(cx,408+4,452); f.text(cx-26,438,"yes",T_ANNOT,"end",SOFT)
f.diamond(cx,536,380,108,"judgement independent of the checked agent?",GATE,lw=24)
f.callout(56,470,300,"different model · narrowed context · adversarial brief · external source of truth",width=26)
f.elbow([(cx+194,536),(1050,536)]); f.text(800,520,"no",T_ANNOT,"middle",SOFT)
f.block(1060,520,"without one of those four, a second agent supplies correlated opinion - cost without information",width=34)
f.vline(cx,590+4,634); f.text(cx-26,620,"yes",T_ANNOT,"end",SOFT)
f.box(cx-170,640,340,64,"keep - independent reviewer",REVIEWER,lw=24)
f.human(cx+220,672,REVIEWER,tick=True)
f.footer("Four agents on one model agreeing have checked the work once and echoed it three times.")
print("10.1",f.save("figures/figure-10-1.svg"))

# ---------------- 10.2 minimal roster ----------------
f=Fig("102","A minimal roster - producer, gates, independent reviewer, human decision",
      "Small, and every element traces back to a clause somebody wrote.")
f.rect(70,206,1462,54,GREY,"none",10,1.8)
f.text(90,240,"orchestrator - sequences, enforces stop conditions",T_ANNOT,"start",SOFT,inside=True)
f.text(1000,240,"deliberately thin: it never reasons about the science",T_ANNOT,"start",GREY,inside=True)
cs,colw=chain(f,[
 dict(kind="tag",label="specification",colour=HUMAN),
 dict(kind="box",label="producer agent",colour=AGENT,ann="with its tools and data store"),
 dict(kind="diamond",label="gate",colour=GATE,ann="tests · schema · citations · units; a rule-checkable criterion is a gate, not an agent"),
 dict(kind="box",label="independent reviewer",colour=REVIEWER,ann="different model · narrowed context · adversarial brief"),
 dict(kind="diamond",label="gate",colour=GATE,ann=None),
 dict(kind="human",label="human decision",colour=HUMAN,ann="accountability, interpretation and authorship stay here")],
 y=360,node_h=90)
# fail-return: run above the chain, clear of annotation bands below
f.elbow([(cs[3],360-45-6),(cs[3],296),(cs[1],296),(cs[1],360-45-6)])
f.text((cs[1]+cs[3])/2,282,"fail - bounded iterations, then escalate",T_ANNOT,"middle",SOFT)
f.footer("Every role on this diagram traces back to a clause of the specification; an unbounded loop is a cost blow-out waiting to happen.")
print("10.2",f.save("figures/figure-10-2.svg"))

# ---------------- 10.3 shared grammar ----------------
f=Fig("103","Distributed human review and its agentic roster share one grammar",
      "Same structure science already uses; a different clock.")
band_title(f,70,206,"conventional",GREY)
cols=[240,560,880,1200]
labs=["author","internal read-through","independent referees ×2","editor decides"]
for x,lab in zip(cols,labs):
    f.human(x,286); f.block(x-110,344,lab,width=18,anchor="start")
for a,b in zip(cols,cols[1:]): f.hline(a+26,b-30,280)
f.text(1360,286,"serial - weeks",T_ANNOT,"start",SOFT)
band_title(f,70,470,"agentic roster")
f.agent_glyph(240,552); f.text(240,606,"producer agent",T_ANNOT,"middle")
f.diamond(430,548,120,56,"gate",GATE,lw=6)
f.human(560,542,REVIEWER,tick=True); f.text(560,606,"independent reviewer",T_ANNOT,"middle")
f.diamond(720,548,120,56,"gate",GATE,lw=6)
f.human(880,542); f.text(880,606,"human decision",T_ANNOT,"middle")
f.hline(266,366,548); f.hline(494,532,548); f.hline(588,656,548); f.hline(784,852,548)
f.block(1000,536,"gated - minutes; the human still owns the decision",width=30)
for (xa,xb,lab) in [(240,240,"producer"),(560,880-0,"x"),(880,1200,"x")]:
    pass
f.vline(240,376,510,GREY,1.4,dash="5 6",arrow=False); f.text(258,470,"producer",T_KEY,"start",GREY)
f.vline(566,376,504,GREY,1.4,dash="5 6",arrow=False); f.text(584,470,"independent checker",T_KEY,"start",GREY)
f.vline(884,376,504,GREY,1.4,dash="5 6",arrow=False); f.text(902,470,"accountable decider",T_KEY,"start",GREY)
f.footer("What carries over is independence and accountability - not the number of parties.")
print("10.3",f.save("figures/figure-10-3.svg"))

# ---------------- 10.4 spec -> roster mapping ----------------
f=Fig("104","Deriving a roster from the specification schema",
      "Every role traces to a clause somebody wrote. No clause, no role.")
rows=[("objective","producer role(s)","one bounded objective, one producer"),
      ("inputs","tool & data access (least privilege)","access assigned per role, never to the roster as a whole"),
      ("acceptance criteria","gates + reviewer brief","can a rule check it? gate if yes; reviewer brief if not"),
      ("stop conditions","loop bound + escalation","bounds cost, and stops responsibility diffusing")]
for i,(l,r,ann) in enumerate(rows):
    yy=250+i*128
    f.box(120,yy,300,64,l,HUMAN,rx=16,lw=22)
    f.box(760,yy,360,64,r,[AGENT,TOOL,GATE,GREY][i],lw=28)
    f.hline(424,754,yy+32)
    f.text(590,yy+16,str(i+1),T_LABEL,"middle",INK,weight="700")
    f.block(1150,yy+16,ann,width=30)
f.footer("A role no clause of the specification demands is a role that should not exist.")
print("10.4",f.save("figures/figure-10-4.svg"))

# ---------------- 11.1 tiers ladder ----------------
f=Fig("111","Six tiers of evidence for a workflow claim",
      "A claim holds the highest tier it actually passed - not the one you hoped for.")
tiers=[("1 · execution - runs, output well-formed",None,228,60),
       ("2 · internal consistency - invariants hold",None,228,60),
       ("3 · reproduces held-out truth - split-sample test",
        "the first tier where the word correct is earned",228,60),
       ("4 · out-of-sample generalisation - differential test",None,228,60),
       ("5 · independent-method corroboration - a second method with a "
        "different error structure agrees",
        "changes the measurement chain, not just the regime",326,50),
       ("6 · adversarial scrutiny - a competent party tries to break it and fails",
        "cannot be automated - judgement does the certifying",300,52)]
for i,(lab,ann,lx,lw) in enumerate(tiers):
    yy=676-i*96
    col=REVIEWER if i==5 else INK
    f.rect(200,yy,620,72,col,"none",8,2.6 if i==5 else 2)
    lines=wrap(lab,lw)
    y0=yy+36-(len(lines)-1)*T_LABEL*0.67
    for k,ln in enumerate(lines):
        f.text(lx,y0+k*T_LABEL*1.34+T_LABEL*0.34,ln,T_LABEL,"start",INK,inside=True)
    f.diamond(820,yy+36,54,40,"",GATE)
    if ann: f.block(880,yy+22,ann,width=30)
f.wrench(230,328); f.cylinder(256,306,56,44,"")          # tier 5: a second method
f.human(250,232,REVIEWER,tick=True)                      # tier 6: the reviewer
f.callout(1150,186,300,"the only tier named for the checker, not the check - "
          "its strength is a measured quantity (§11.5)")
f.vline(160,750,190)
f.block(56,440,"increasing evidential strength",width=12)
f.o.append(f'<path d="M1470,580 h16 v168 h-16 M1470,196 h16 v360 h-16" fill="none" stroke="{GREY}" stroke-width="1.6"/>')
f.segs.append((1470,580,1486,748)); f.segs.append((1470,196,1486,556))
f.text(1450,664,"necessary - and almost worthless alone",T_ANNOT,"end",SOFT)
f.text(1450,376,"correctness earned here",T_ANNOT,"end",SOFT)
f.footer("The tiers are cumulative: a tier-5 claim has passed 1 to 5.")
print("11.1",f.save("figures/figure-11-1.svg"))

# ---------------- 11.2 evaluation set ----------------
f=Fig("112","An evaluation set built from the workflow's own history",
      "The raw material is already in your history. The work is gathering and disciplining it.")
srcs=["settled past runs","manual-workflow outputs","failure log (Ch.13)","known-correct hold-back"]
for i,ssrc in enumerate(srcs):
    f.cylinder(80,206+i*120,220,72,ssrc)
f.box(420,380,190,76,"curate",INK,lw=14)
for i in range(4): f.elbow([(302,242+i*120),(360,242+i*120),(360,418),(414,418)]) if i in (0,3) else f.hline(302,414,242+i*120) if False else None
f.elbow([(302,242),(360,242),(360,418),(414,418)])
f.hline(302,414,362+0) if False else None
f.elbow([(302,362),(360,362),(360,418),(414,418)]) if False else None
f.hline(302,356,482) if False else None
f.elbow([(302,482),(360,482),(360,418),(414,418)])
f.elbow([(302,602),(360,602),(360,418),(414,418)])
f.elbow([(302,362),(414,362)]) if False else None
f.hline(302,414,418) if False else None
f.block(420,500,"each case: input · reference · metric fixed in advance · provenance of the reference",width=22)
f.box(680,380,210,76,"stratify by task and regime",INK,lw=16)
f.hline(610,674,418)
f.block(680,500,"spans the regimes the workflow will actually meet - easy cases cannot certify it",width=22)
f.cylinder(950,372,230,92,"stratified evaluation set")
f.hline(890,944,418)
f.panel(972,440,186,16,HILITE,3)
f.text(970,492,"held-out slice",T_ANNOT,"start",INK)
f.vnote(950,522,"withheld means absent from anything the model could have seen",GATE,width=26)
f.elbow([(1065,368),(1065,300),(940,300)])
f.text(1000,284,"version + refresh",T_ANNOT,"middle",SOFT)
f.text(660,284,"refresh on model, prompt or data-regime change",T_KEY,"middle",SOFT)
f.diamond(1300,418,130,66,"gate",GATE,lw=6)
f.hline(1182,1229,418)
f.text(1372,486,"the gate §11.5 measures",T_ANNOT,"start",SOFT)
f.box(1380,560,150,60,"live workflow",INK,lw=10)
f.elbow([(1300,453),(1300,590),(1374,590)])
f.footer("Harvest, curate, stratify, hold out, version - then the set feeds the tiered checks of this chapter.")
print("11.2",f.save("figures/figure-11-2.svg"))

# ---------------- 11.3 seeded defects ----------------
f=Fig("113","Seeded-defect measurement of a verification gate",
      "The only way to know an alarm works is a controlled fire.")
xs=lanes(f,[("human","scientist",HUMAN),("diamond","gate under test",GATE),("cyl","tally",STORE)],
 [(0,0,"1 seed known faults","fabricated citation · unit slip · out-of-range · dropped constraint - stratified by class",INK),
  (0,1,"2 run gate blind","the gate is not told where the faults are",INK),
  (1,2,"3 pass / fail per input",None,INK),
  (2,2,"4 tally catches & misses by class","a never-firing gate is a broken gate, not a clean corpus",GATE),
  (2,0,"5 report rate + interval","zero misses in twenty trials still means the true miss rate could be ~15%",INK)],
 top=200,first=340,last=690)
f.footer("Re-measure on: model change · prompt change · data-regime change · calendar.")
print("11.3",f.save("figures/figure-11-3.svg"))

# ---------------- 12.1 governance layer ----------------
f=Fig("121","A governance layer that records without steering",
      "The workflow writes to the layer. The layer never steers the workflow.")
wf=[("tag","specification",HUMAN),("box","AI agent",AGENT),("tool","tool call",TOOL),("human","human decision",HUMAN)]
for i,(k,lab,col) in enumerate(wf):
    yy=250+i*128
    draw_node(f,k,210,yy,240,64,lab,col)
    if i: f.vline(210,250+(i-1)*128+(46 if wf[i-1][0] in("human","tool") else 32),yy-(46 if k in("human","tool") else 36),INK,1.8)
f.rect(560,206,970,560,GREY,"none",14,2)
f.text(584,240,"governance layer",T_LABEL,fill=GREY,weight="600")
regs=[("assumption registry","what did the analysis take as given, and who agreed?"),
      ("uncertainty registry","what does the workflow not know, and how much?"),
      ("audit trail","what happened, in what order, invoked by whom?"),
      ("reviewer-coverage record","what was actually reviewed - and what was not?")]
for i,(lab,q) in enumerate(regs):
    yy=268+i*118
    f.cylinder(610,yy,270,74,lab)
    f.block(910,yy+34,q,width=44)
for i in range(4):
    f.hline(334,604,250+i*128,GREY,1.6,dash="4 6")
f.text(430,196,"fed by events the workflow already emits - no extra effort",T_KEY,"start",SOFT)
f.footer("Institutional memory that survives staff turnover: the record is a by-product of doing the work, not a chore beside it.")
print("12.1",f.save("figures/figure-12-1.svg"))

# ---------------- 12.2 trust boundary ----------------
f=Fig("122","Least privilege and the trust boundary",
      "An injected instruction can only do what the granted tools allow.")
f.rect(520,220,560,470,GREY,"none",14,2.6)
f.text(544,254,"trusted zone",T_LABEL,fill=GREY,weight="600")
f.text(544,690+24,"the artefact institutional IT will ask to see",T_KEY,"start",SOFT)
f.box(560,290,200,60,"specification",HUMAN,rx=16,lw=14)
f.box(560,390,200,70,"AI agent",AGENT,lw=14)
f.wrench(830,320); f.wrench(890,320); f.wrench(950,320)
f.text(890,368,"permitted tools",T_ANNOT,"middle")
f.block(810,398,"deny by default - each capability granted deliberately",width=24)
f.text(810,470,"least privilege",T_ANNOT,"start",INK,weight="600")
for i,lab in enumerate(["external documents","web content","third-party data"]):
    f.box(70,250+i*100,230,62,lab,GREY,lw=18)
f.diamond(430,380,150,86,"validate",GATE,lw=8)
for i in range(3):
    f.elbow([(300,281+i*100),(352,281+i*100),(352,380)]) if i!=1 else f.hline(300,352,381)
f.hline(352,380,381) if False else None
f.vline(352,281,380,INK,2.1,arrow=False) if False else None
f.hline(506,554,380)
f.block(70,592,"quoted as data to analyse - never instructions to follow",width=34)
for i,lab in enumerate(["write to shared system","send communication","irreversible command"]):
    f.box(1300,250+i*100,240,62,lab,GREY,lw=18)
f.human(1170,380); f.text(1170,438,"human gate",T_ANNOT,"middle")
f.hline(1084,1140,380)
for i in range(3):
    f.elbow([(1204,380),(1252,380),(1252,281+i*100),(1294,281+i*100)]) if i!=1 else f.hline(1204,1294,381)
f.block(1096,478,"the agent proposes; a person disposes",width=18)
f.footer("Untrusted text enters only as quoted data; consequential actions leave only through a person - least privilege is the primary defence.")
print("12.2",f.save("figures/figure-12-2.svg"))
