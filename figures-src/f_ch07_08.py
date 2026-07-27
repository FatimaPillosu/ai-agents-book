import sys; sys.path.insert(0,'figures-src')
from templates import *

# ---------------- 7.1 gate stack ----------------
f=Fig("71","Four gates between an agent's code and the main branch",
      "Cheap checks first, so your attention is spent only on what survives them.")
cs,colw=chain(f,[
 dict(kind="agent",label="author agent",colour=AGENT,ann=None),
 dict(kind="box",label="proposed change",colour=STORE,ann=None),
 dict(kind="diamond",label="automated tests",colour=GATE,
      ann="the assertions must encode intended behaviour, not whatever the code happens to do"),
 dict(kind="diamond",label="pre-commit hooks",colour=GATE,
      ann="formatting, linting, type checks, secrets scan, full suite - run automatically"),
 dict(kind="diamond",label="independent reviewer agent",colour=GATE,
      ann="a different instance, its own context, read-only, no power to approve or merge"),
 dict(kind="human",label="human owner",colour=HUMAN,
      ann="reads the report and the change, and owns the merge"),
 dict(kind="box",label="main branch",colour=INK,ann=None)],y=330,node_h=96)
f.elbow([(cs[2],330+48+17+4),(cs[2],424),(cs[0],424),(cs[0],400)])
f.text(cs[0]+34,446,"fail - back to the author, with the reason",T_KEY,"start",SOFT)
bracket(f,cs[2]-colw/2+30,cs[4]+colw/2-30,614,"cheap mechanical gates first - the expensive one last")
f.footer("Each gate is cheaper than the review it protects, and each catches a different class of error.")
print("7.1",f.save("figures/figure-7-1.svg"))

# ---------------- 7.2 notebook vs pipeline ----------------
f=Fig("72","From exploratory notebook to governed pipeline",
      "Same four steps. The difference is everything around them.")
band_title(f,70,196,"before",GREY)
f.rect(90,220,560,180,GREY,"none",12,2)
f.text(110,252,"notebook",T_ANNOT,"start",GREY)
for (lab,dx,dy) in [("load",130,286),("regrid",320,270),("threshold",180,332),("plot",420,330)]:
    f.box(dx,dy,150,46,lab,INK,lw=12)
f.block(680,262,"cells in the order the investigation happened, not the order a reader needs",width=28)
f.hline(650,760,372,GREY)
f.text(920,376,"looked reasonable - shared",T_ANNOT,"start",SOFT)
f.vnote(1220,368,"no independent reader",GATE,width=24)
band_title(f,70,480,"governed pipeline")
f.rect(90,506,600,150,INK,"none",12,2)
f.text(110,538,"version control",T_ANNOT,"start",SOFT)
for i,lab in enumerate(["load","regrid","threshold","plot"]):
    f.box(116+i*142,560,126,52,lab,TOOL,lw=10)
    if i: f.hline(116+(i-1)*142+126+2,116+i*142-4,586)
f.agent_glyph(760,580); f.text(760,634,"author agent",T_ANNOT,"middle",SOFT)
f.hline(690,736,586)
f.hline(786,830,586)
for i,lab in enumerate(["tests","hooks","independent review"]):
    f.diamond(900+i*190,586,150,64,lab,GATE,lw=12)
    if i: f.hline(900+(i-1)*190+77,900+i*190-79,586)
f.hline(900+2*190+77,1436,586)
f.human(1476,576); f.text(1476,634,"human owner",T_ANNOT,"middle",SOFT)
f.vnote(900,700,"reader before merge",GATE,width=30)
f.footer("The analysis is the same in both rows - only what surrounds it changed. The gap is discipline, not cleverness.")
print("7.2",f.save("figures/figure-7-2.svg"))

# ---------------- 7.3 reviewer sequence ----------------
f=Fig("73","A separate reviewer agent reads the change before the human does",
      "It is given the standard, and deliberately not the author's case for the work.")
xs=lanes(f,[("agent","author agent",AGENT),
            ("diamond","tests + hooks",GATE),
            ("reviewer","reviewer agent",REVIEWER,"a different instance · its own clean context · read-only · cannot approve"),
            ("human","human owner",HUMAN)],
   [(0,1,"1 submit change",None,INK),
    (1,0,"2 fail - fix","or pass",INK),
    (1,2,"3 pass: review this",None,INK),
    (2,2,"4 read change vs specification","given the specification, and deliberately not the author's reasoning",INK),
    (2,3,"5 findings report","advisory - not a gate the agent can open",GATE),
    (3,3,"6 merge - owns decision","reads the report and the change, and answers for the result",INK)],
   top=200,first=352,last=700)
f.footer("A reviewer that almost never returns a fault is a broken reviewer, not a flawless author.")
print("7.3",f.save("figures/figure-7-3.svg"))

# ---------------- 7.4 self-test trace ----------------
f=Fig("74","A self-tested error passes; an independent test catches it",
      "A green suite tells you the code does what the suite says. Nothing more.")
f.agent_glyph(240,250); f.text(240,306,"author agent",T_ANNOT,"middle")
f.box(500,214,240,72,"regrid step",TOOL)
f.hline(268,494,250)
f.vnote(770,318,"lat/lon transposed - the output is still a plausible field of numbers",GATE,width=24)
f.box(500,430,240,66,"self-derived test",GREY,lw=16)
f.vline(620,290,424)
f.text(788,468,"PASS",T_LABEL,"start",TOOL,weight="700")
f.vnote(788,502,"asserts what the code does, not what it should - so it passes",GATE,width=30)
f.diamond(1140,250,320,96,"independent test - conservation check",GATE,lw=20)
f.hline(744,976,250)
f.text(1330,468,"FAIL",T_LABEL,"start",GATE,weight="700")
f.vnote(1090,502,"derived from the specification, not from the output - so it fails, correctly",GATE,width=34)
f.elbow([(1140,302),(1140,340),(1470,340),(1470,660),(240,660),(240,318)])
f.text(690,644,"fix - back to the author, with the failing property named",T_ANNOT,"middle",SOFT)
f.footer("A green suite confirms the code does what the suite asserts, and says nothing about whether the suite asserts the right thing.")
print("7.4",f.save("figures/figure-7-4.svg"))

# ---------------- 8.1 orchestration boundary ----------------
f=Fig("81","What the orchestration agent does, and what it never does",
      "Everything inside the dashed line is bookkeeping. Every decision sits outside it.")
f.human(200,280); f.text(200,336,"scientist",T_ANNOT,"middle")
f.block(56,388,"which design · which metric · which result to believe · which hypothesis to pursue",width=16)
f.box(90,500,220,70,"experimental design",HUMAN,rx=16,lw=16)
f.vline(200,354,494,HUMAN,1.8,arrow=True)
f.block(70,610,"parameters, ranges, metric suite and evaluation period - fixed before any run",width=26)
f.rect(420,220,560,420,GREY,"none",14,2,dash="10 8")
f.text(444,206,"no scientific decisions inside this boundary",T_ANNOT,"start",GREY)
f.rect(460,258,480,180,AGENT,"none",12,2.4)
f.text(480,290,"orchestration agent",T_ANNOT,"start",AGENT)
for i,lab in enumerate(["expand design","submit runs","track state","record provenance"]):
    f.box(478+(i%2)*230,306+(i//2)*62,214,50,lab,TOOL,lw=18)
f.box(478,506,200,70,"HPC scheduler",TOOL,lw=14)
f.vline(560,438,500)
f.cylinder(760,502,190,84,"provenance store")
f.vline(866,438,498,STORE,1.8)
f.block(478,672,"configuration, software version, forcing dataset and seed, captured as the run launches",width=48)
f.hline(310,454,536)
f.elbow([(980,330),(1130,330)])
f.text(1058,314,"anomaly flag",T_ANNOT,"middle",SOFT)
f.human(1190,322); f.text(1190,378,"scientist adjudicates",T_ANNOT,"middle")
f.block(1120,412,"the agent may notice a problem; it never adjudicates one",width=24)
f.footer("The agent expands a fixed design, submits, tracks and records; the decisions never enter the dashed boundary.")
print("8.1",f.save("figures/figure-8-1.svg"))

# ---------------- 8.2 hypothesis gate ----------------
f=Fig("82","Where a generated hypothesis may and may not go",
      "A suggestion becomes a finding only when a person has tested it and signed for it.")
cx=560
f.box(cx-170,190,340,64,"model-generated hypothesis",AGENT,lw=26)
f.vline(cx,254,296)
f.cylinder(cx-150,300,300,80,"exploratory record (tagged)")
f.block(cx+190,322,"tagged with its origin and compartmented by construction, not by good intentions",width=30)
f.vline(cx,380,430)
f.diamond(cx,510,340,110,"tested by pre-specified procedure?",GATE,lw=22)
f.block(cx+210,478,"the procedure is fixed before the test, not chosen after seeing the answer",width=30)
f.elbow([(cx-174,510),(210,510)]); f.text(300,494,"no",T_ANNOT,"middle",SOFT)
f.box(60,476,150,68,"remains exploratory",GREY,lw=12)
f.vnote(60,584,"hypothesis laundering blocked here",GATE,width=20)
f.vline(cx,569,616); f.text(cx+24,600,"yes",T_ANNOT,"start",SOFT)
f.human(cx,652); f.text(cx+34,650,"scientist owns the claim",T_ANNOT,"start")
f.text(cx+34,676,"a named person takes responsibility",T_ANNOT,"start",SOFT)
f.hline(cx+300,1130,652)
f.box(1140,618,300,68,"enters result / manuscript",TOOL,lw=22)
f.footer("A better model makes an untested hypothesis more dangerous, not less - its fluency hides the missing evidence more effectively.")
print("8.2",f.save("figures/figure-8-2.svg"))

# ---------------- 8.3 hand-run vs orchestrated ----------------
f=Fig("83","From hand-run campaign to orchestrated campaign",
      "The decisions do not move. The record-keeping does.")
band_title(f,70,196,"conventional",GREY)
f.human(140,282); f.text(140,338,"scientist",T_ANNOT,"middle")
f.box(260,246,300,64,"edit config · submit · check queue",TOOL,lw=22)
f.hline(170,254,278)
f.box(640,246,190,64,"manual log",GREY,lw=14)
f.hline(560,634,278)
f.cylinder(910,242,150,74,"outputs")
f.hline(830,904,278)
f.o.append(f'<line x1="1060" y1="278" x2="1180" y2="278" stroke="{GREY}" stroke-width="2" stroke-dasharray="4 9"/>')
f.segs.append((1060,278,1180,278))
f.text(1120,258,"drift",T_ANNOT,"middle",GATE)
f.vnote(1200,262,"record reconstructed after the fact, from directory timestamps and half-remembered decisions",GATE,width=30)
f.block(640,352,"diverges silently - nothing enforces that it matches the runs",width=26)
band_title(f,70,480,"orchestrated")
f.human(140,566); f.text(140,622,"scientist",T_ANNOT,"middle")
f.text(80,660,"same person, same decisions, both rows",T_ANNOT,"start",SOFT)
f.box(260,530,230,64,"experimental design",HUMAN,rx=16,lw=16)
f.hline(170,254,562)
f.box(560,530,250,64,"orchestration agent",AGENT,lw=18)
f.hline(490,554,562)
f.box(880,530,170,64,"scheduler",TOOL,lw=12)
f.hline(810,874,562)
f.cylinder(1120,526,190,76,"provenance store")
f.hline(1050,1114,562)
f.text(1120,646,"captured at run time",T_ANNOT,"start",INK)
f.text(1120,672,"keyed to the configuration actually used",T_ANNOT,"start",SOFT)
f.footer("In the top row the link between runs and log is broken and rebuilt from memory; in the bottom row it is captured as each run launches.")
print("8.3",f.save("figures/figure-8-3.svg"))

# ---------------- 8.4 three-track sequence ----------------
f=Fig("84","The three-track intercomparison as an orchestrated sequence",
      "The system that runs the experiments does not get to score them.")
xs=lanes(f,[("human","scientist",HUMAN),
            ("agent","orchestration agent",AGENT),
            ("tool","HPC scheduler",TOOL),
            ("cyl","provenance store",STORE),
            ("diamond","independent evaluation",GATE)],
   [(0,1,"1 protocol + 3 track configs","one training period, one evaluation period, one forcing set, one metric suite",INK),
    (1,1,"2 expand: physics · data-driven · hybrid","the agent expands a fixed design; it does not prune it",INK),
    (1,2,"3 submit runs",None,INK),
    (2,1,"4 run states",None,INK),
    (1,3,"5 record provenance","per run: configuration, software version, forcing dataset, seed",INK),
    (1,0,"6 flag anomalies","failed runs, out-of-bounds outputs, diverged losses - flagged, not judged",INK),
    (4,4,"7 held-out evaluation","a period the agent had no hand in choosing",GATE),
    (4,0,"8 scores",None,INK)],
   top=196,first=312,last=736)
f.footer("Steps 2 to 6 are orchestration only - no scoring happens anywhere inside them.")
print("8.4",f.save("figures/figure-8-4.svg"))
