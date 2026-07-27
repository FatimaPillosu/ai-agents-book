import sys; sys.path.insert(0,'figures-src')
from templates import *

# ---------------- 13.1 fabricated citation ----------------
f=Fig("131","A fabricated citation, caught at the resolver",
      "It looks perfect because the same machinery works whether or not the paper exists.")
f.human(140,300); f.text(140,356,"claim to support",T_ANNOT,"middle")
f.agent_glyph(400,292); f.text(400,348,"agent drafts citation",T_ANNOT,"middle")
f.hline(170,376,300)
f.box(580,258,300,84,"citation string",STORE,lw=24)
f.hline(424,574,300)
f.vnote(580,392,"plausible by construction - right shape, right journal, right year",GATE,width=30)
f.diamond(1080,300,240,100,"resolver check",GATE,lw=16)
f.hline(880,954,300)
f.block(1250,270,"checked against an external bibliographic authority - fluency cannot fool it",width=22)
f.elbow([(1080,352),(1080,600),(400,600),(400,366)])
f.text(740,584,"not found: delete, do not repair - never repaired into existence",T_ANNOT,"middle",SOFT)
f.footer("Reading cannot catch this: the property that would betray it is exactly what the generating process suppresses.")
print("13.1",f.save("figures/figure-13-1.svg"))

# ---------------- 13.2 silent unit error ----------------
f=Fig("132","A silent unit error, made loud by a range assertion",
      "Nothing about the number looks wrong. That is the problem.")
f.agent_glyph(300,250); f.text(300,306,"agent computes quantity",T_ANNOT,"middle")
f.box(180,360,240,72,"number: 42 (no units)",STORE,lw=18)
f.vline(300,318,354)
f.vnote(460,380,"wrong by a physical factor - and still a perfectly reasonable-looking value",GATE,width=32)
f.diamond(300,540,300,96,"units + range assertion",GATE,lw=16)
f.vline(300,432,488)
f.block(480,530,"does not reason about the science: refuses unlabelled units and impossible values",width=34)
f.elbow([(450,540),(560,540),(560,250),(340,250)]) if False else None
f.elbow([(300,588+4),(300,650)]) if False else None
f.elbow([(150,540),(90,540),(90,250),(266,250)])
f.text(100,340,"out of range - halt",T_ANNOT,"start",GATE)
f.box(180,660,240,66,"downstream use",GREY,lw=18)
f.vline(300,592,654,GREY,2,dash="6 6",arrow=False)
f.o.append(f'<line x1="168" y1="693" x2="432" y2="693" stroke="{GATE}" stroke-width="5"/>')
f.segs.append((168,693,432,693))
f.text(470,698,"error stopped here - the calibration and the verification never see it",T_ANNOT,"start",SOFT)
f.footer("The whole trick is turning a silent failure into a loud one: loud gets caught, silent gets shipped.")
print("13.2",f.save("figures/figure-13-2.svg"))

# ---------------- 13.3 specification drift ----------------
f=Fig("133","Specification drift, caught against a fixed specification",
      "No single step is wrong. The target moves anyway.")
f.box(560,196,360,58,"specification (fixed, external)",HUMAN,rx=16,lw=28)
anns=["a redefinition - looks responsive","a relaxed criterion - looks responsive","a helpful reinterpretation - looks responsive"]
for i in range(3):
    cx=300+i*300
    f.box(cx-90,360,180,64,f"turn {i+1}",AGENT,lw=12)
    f.vline(cx,258,354,GREY,1.4,dash="4 6",arrow=False)
    f.block(cx-90,470,anns[i],width=22)
    if i: f.hline(cx-300+94,cx-96,392)
f.vnote(620,560,"the target has rotated, and no single step was the wrong one",GATE,width=40)
f.diamond(1250,392,240,96,"compare to spec",GATE,lw=16)
f.hline(994,1124,392)
f.block(1140,530,"judged against the document, not the conversation",width=28)
f.hline(1372,1430,392)
f.human(1490,382); f.text(1478,440,"human decision",T_ANNOT,"middle")
f.text(1401,296,"drift detected",T_KEY,"middle",SOFT)
f.footer("Drift is divergence from a fixed reference - the check is free when the specification is a real artefact, impossible when it is not.")
print("13.3",f.save("figures/figure-13-3.svg"))

# ---------------- 13.4 sycophancy ----------------
f=Fig("134","Sycophantic review, exposed by engineered independence",
      "Independence is configured, not requested.")
band_title(f,70,206,"failure",GREY)
f.box(90,240,330,72,"artefact + author conclusion",HUMAN,lw=26)
f.human(600,268,REVIEWER,tick=True); f.text(600,326,"reviewer sees conclusion",T_ANNOT,"middle")
f.hline(424,548,276)
f.vnote(760,246,"it agrees with the position it inferred",GATE,width=20)
f.box(1060,240,200,72,"approved",GREY,lw=16)
f.hline(656,1054,276)
f.o.append(f'<line x1="1078" y1="256" x2="1242" y2="296" stroke="{GATE}" stroke-width="4"/>')
f.o.append(f'<line x1="1078" y1="296" x2="1242" y2="256" stroke="{GATE}" stroke-width="4"/>')
f.vnote(1300,246,"false assurance - worse than no review, because the gap now looks filled",GATE,width=22)
f.text(70,400,"the only difference: what the reviewer was shown, and what it was asked",T_ANNOT,"start",INK,weight="600")
band_title(f,70,480,"fix")
f.box(90,514,330,72,"artefact, conclusion withheld",HUMAN,lw=24)
f.human(600,542,REVIEWER,tick=True); f.text(600,600,"reviewer: find defects",T_ANNOT,"middle")
f.hline(424,548,550)
f.block(760,494,"criteria only, adversarial brief, no sight of the conclusion",width=30)
f.box(1060,514,200,72,"defect found",TOOL,lw=16)
f.hline(656,1054,550)
f.text(1300,556,"real scrutiny restored",T_ANNOT,"start",SOFT)
f.footer("Asking it to be tougher does not work - a system disposed to agree will agree about that too.")
print("13.4",f.save("figures/figure-13-4.svg"))

# ---------------- 13.5 context loss ----------------
f=Fig("135","Context loss - the dropped constraint and the boundary check",
      "The agent cannot miss what it no longer represents.")
f.box(80,240,220,70,"constraint set",STORE,lw=16)
f.cylinder(110,400,190,80,"state on record")
f.vline(190,310,394,STORE,1.8)
f.block(320,424,"load-bearing facts are written out, not trusted to memory",width=26)
f.box(400,240,190,70,"agent works",AGENT,lw=14)
f.hline(300,394,274)
f.vline(700,196,560,GREY,2,dash="8 7",arrow=False)
f.text(700,180,"context boundary",T_ANNOT,"middle",GREY)
f.o.append(f'<line x1="596" y1="274" x2="668" y2="274" stroke="{GREY}" stroke-width="2" stroke-dasharray="3 7"/>')
f.segs.append((596,274,668,274))
f.text(560,222,"constraint dropped",T_KEY,"start",GATE)
f.vnote(740,232,"no error raised - the system cannot miss what it no longer represents",GATE,width=26)
f.box(760,330,210,70,"agent continues",AGENT,lw=16)
f.box(1050,330,230,70,"confident output",INK,lw=18)
f.hline(974,1044,364)
f.block(1000,436,"wrong through a missing premise, not faulty reasoning",width=20)
f.diamond(1240,590,320,100,"consistency assertion vs state",GATE,lw=20)
f.vline(1240,404,536) if False else None
f.elbow([(1165,400),(1165,470),(1240,470),(1240,536)])
f.elbow([(205,440),(205,690),(1076,690)]) if False else None
f.elbow([(190,444),(190,660),(1070,660),(1070,620)]) if False else None
f.elbow([(190,444),(190,590),(1076,590)])
f.text(560,578,"tested against the record, not the conversation",T_ANNOT,"middle",SOFT)
f.hline(1404,1440,590)
f.box(1444,556,140,68,"re-ground and retry",TOOL,lw=10)
f.text(1404,664,"contradiction",T_KEY,"middle",GATE)
f.footer("The assertion catches the violation even though the reason for it is invisible.")
print("13.5",f.save("figures/figure-13-5.svg"))

# ---------------- 13.6 extrapolation ----------------
f=Fig("136","Confident extrapolation, bounded by its support",
      "Confidence does not drop where the evidence runs out. The comparison has to be mechanical.")
f.box(80,250,300,90,"data + support range",STORE,lw=22)
f.panel(110,356,180,14,STORE,3)
f.text(110,398,"the span the evidence actually covers",T_KEY,"start",SOFT)
f.agent_glyph(500,286); f.text(500,342,"agent generalises",T_ANNOT,"middle")
f.hline(384,474,290)
f.box(640,250,320,90,"confident claim",AGENT,lw=24)
f.hline(530,634,290)
f.panel(670,356,180,14,STORE,3)
f.panel(850,356,140,14,GATE,3)
f.text(1000,368,"the reach past the data",T_KEY,"start",GATE)
f.vnote(640,430,"reads identically to a supported claim - the register of confidence does not change at the edge of the evidence",GATE,width=44)
f.diamond(1200,290,240,96,"scope vs support",GATE,lw=16)
f.hline(964,1074,290)
f.block(1330,300,"compares scopes; never judges plausibility, which is the judgement fluency defeats",width=18)
f.elbow([(1200,342),(1200,590),(1074,590)])
f.text(1240,560,"out of support",T_KEY,"start",SOFT)
f.box(760,556,310,68,"flag as hypothesis - independent test",TOOL,lw=24)
f.text(760,652,"demoted, not deleted",T_ANNOT,"start",SOFT)
f.footer("Moving it back up takes new evidence, not more assured phrasing.")
print("13.6",f.save("figures/figure-13-6.svg"))

# ---------------- 14.1 three tiers ----------------
f=Fig("141","Three tiers inside one trust boundary",
      "Exact where it must be defensible; advisory where a mistake is recoverable; human where judgement is irreducible.")
f.rect(70,220,1180,470,GREY,"none",14,2.6)
f.text(94,254,"partner environment (trust boundary)",T_LABEL,fill=GREY,weight="600")
f.text(94,700,"no observational data egress",T_ANNOT,"start",GATE,inside=True)
f.cylinder(120,330,220,90,"observations (never leave)")
f.box(450,330,300,90,"deterministic verification core",TOOL,lw=22)
f.hline(342,444,375)
f.block(450,470,"same inputs, same numbers, every time - reportable as an official figure",width=26)
f.box(850,330,150,66,"scores",STORE,lw=10)
f.hline(752,844,363)
f.human(1120,356); f.text(1120,414,"human review",T_ANNOT,"middle")
f.hline(1002,1090,363)
f.rect(830,190-0,340,0,GREY) if False else None
f.box(850,540,320,86,"local tutoring tier - open-weight model",AGENT,lw=24,dash="7 6")
f.o.append(f'<line x1="925" y1="398" x2="925" y2="534" stroke="{AGENT}" stroke-width="2" stroke-dasharray="6 5"/>')
f.segs.append((925,398,925,534))
f.text(946,470,"explains / guides - no decision",T_ANNOT,"start",SOFT)
f.block(850,656,"optional; on the partner's own hardware; degrades to nothing if the compute is unavailable",width=52)
f.hline(1254,1330,363)
f.block(1346,282,"aggregate scores + questions only",size=T_KEY,width=18)
f.box(1336,330,200,66,"team (escalation)",INK,lw=16)
f.block(1336,430,"the one thing that crosses - and never the records",width=18)
f.footer("Three constraints forced this shape - and it is the shape governance would have chosen anyway.")
print("14.1",f.save("figures/figure-14-1.svg"))

# ---------------- 14.2 who computes/explains/decides ----------------
f=Fig("142","Who computes, who explains, who decides",
      "Every number comes from the core. Every decision stays with the person.")
xs=lanes(f,[("human","user",HUMAN),("box","deterministic core",TOOL),("box","tutoring tier (optional)",AGENT)],
 [(0,1,"1 request verification",None,INK),
  (1,1,"2 compute scores (exact)",None,INK),
  (1,0,"3 return scores",None,INK),
  (0,2,"4 what does this mean?",None,INK),
  (2,0,"5 explain (no decision)","reads the scores and the fixed definitions; writes nothing to the record",INK),
  (0,1,"6 request diagnostic",None,INK),
  (1,1,"7 recompute (exact)","a suggestion from the tutor is executed by the core - never accepted as a number from the model",INK),
  (0,0,"8 decide + record","decision authority stays human",GATE)],
 top=200,first=312,last=730)
f.footer("Observations stay local for the whole exchange.")
print("14.2",f.save("figures/figure-14-2.svg"))

# ---------------- 14.3 blocked egress ----------------
f=Fig("143","From blocked egress to local verification and learning",
      "The data was asked to move. The verification moved instead.")
band_title(f,70,200,"before",GREY)
f.rect(90,226,560,180,GREY,"none",12,2.2)
f.text(110,258,"trust boundary",T_ANNOT,"start",GREY)
f.cylinder(140,286,200,84,"observations")
f.o.append(f'<line x1="352" y1="328" x2="710" y2="328" stroke="{GREY}" stroke-width="2.2" stroke-dasharray="7 6"/>')
f.segs.append((352,328,710,328))
f.o.append(f'<line x1="636" y1="306" x2="682" y2="350" stroke="{GATE}" stroke-width="5"/>')
f.o.append(f'<line x1="636" y1="350" x2="682" y2="306" stroke="{GATE}" stroke-width="5"/>')
f.box(730,296,280,64,"verification, off-site",GREY,lw=22)
f.vnote(1070,290,"months of negotiation / often no agreement",GATE,width=24)
f.block(1070,360,"the expertise sat on one side, the data on the other; the holding institution cannot accept the residual risk - and does not have to",width=34)
band_title(f,70,470,"after")
f.rect(90,496,860,240,GREY,"none",12,2.2)
f.text(110,528,"trust boundary",T_ANNOT,"start",GREY)
f.cylinder(130,570,180,80,"observations")
f.box(370,566,250,84,"deterministic core",TOOL,lw=18)
f.hline(312,364,608)
f.box(660,516,250,64,"tutoring tier (optional)",AGENT,lw=20,dash="7 6")
f.human(700,662); f.text(700,716,"human review",T_ANNOT,"middle")
f.hline(624,664,608) if False else None
f.hline(622,660,610) if False else None
f.hline(622,656,608)
f.hline(950,1030,608)
f.text(956,560,"aggregate scores only",T_KEY,"start",SOFT)
f.box(1040,576,140,64,"team",INK,lw=10)
f.block(1040,676,"aggregates cross; records never do",width=18)
f.text(1240,560,"users learn on own data",T_ANNOT,"start",INK,weight="600")
f.block(1240,592,"verification and teaching now happen where the data already is",width=22)
f.footer("The bonus nobody designed for: partners learn verification on their own data.")
print("14.3",f.save("figures/figure-14-3.svg"))

# ---------------- 15.1 five stages ----------------
f=Fig("151","One workflow, five governed stages",
      "Human authority sits at every gate, not only at the end.")
f.human(800,236); f.text(920,232,"author decision - connected to every gate",T_ANNOT,"start")
cs,colw=chain(f,[
 dict(kind="tag",label="specification",colour=HUMAN,ann="seven fields, written before any agent runs"),
 dict(kind="box",label="agent roster",colour=AGENT,ann="derived from the specification, not chosen"),
 dict(kind="diamond",label="gates & registries",colour=GATE,ann="the workflow's memory of what it assumed and does not know"),
 dict(kind="reviewer",label="independent review",colour=REVIEWER,ann="no stake in the work it checks"),
 dict(kind="box",label="publication run",colour=INK,ann="manuscript · figures · disclosure")],
 y=430,node_h=92)
for cx in (cs[2],cs[3]):
    f.vline(cx if cx!=cs[3] else cx, 262 if False else 268,352,HUMAN,1.5,dash="4 6",arrow=False)
f.vline(820,268,352,HUMAN,1.5,dash="4 6",arrow=False) if False else None
f.panel(70,700,1460,50,"#E9E9E5",8)
f.text(90,732,"audit trail - accumulates from stage one; the disclosure is assembled, not reconstructed",T_ANNOT,"start",SOFT,inside=True)
f.footer("Each stage's audited output is the next stage's admissible input; a gap between stages is where governance fails unnoticed.")
print("15.1",f.save("figures/figure-15-1.svg"))

# ---------------- 15.2 one gated stage ----------------
f=Fig("152","One gated stage, from specification unit to author decision",
      "The author decides at the gate, not after the workflow has finished.")
xs=lanes(f,[("tag","specification unit",HUMAN),("agent","agent",AGENT),
            ("tool","tools & data",TOOL),("diamond","gate + reviewer",GATE),
            ("human","author",HUMAN)],
 [(0,1,"1 objective, inputs, criteria, stop",None,INK),
  (1,2,"2 call tools, transform","calculations go to tools, not prose",INK),
  (1,3,"3 write output + provenance","any new assumption goes to the registry, not left implicit",INK),
  (1,3,"4 submit for check",None,INK),
  (3,1,"5 fail - return (within budget)","loop bounded by the stop conditions",INK),
  (3,4,"5 pass",None,INK),
  (4,4,"6 accept / override / return","the author decides at the gate, not after",GATE)],
 top=200,first=318,last=724)
f.footer("One decision per gate is the price of a workflow whose every step is attributable.")
print("15.2",f.save("figures/figure-15-2.svg"))

# ---------------- 16.1 thirty-day plan ----------------
f=Fig("161","The thirty-day plan as a sequence of habits, not tools",
      "Each week ends with an artefact you keep, not a tutorial you completed.")
band_title(f,70,206,"tool-first start",GREY)
f.box(90,240,240,64,"adopt a product",GREY,lw=18)
f.box(430,240,240,64,"learn the interface",GREY,lw=18)
f.hline(330,424,272)
f.box(770,240,140,64,"trust?",GREY,lw=10)
f.hline(670,764,272)
f.block(970,258,"what was learned has the lifespan of the product",width=34)
band_title(f,70,420,"capability-first month")
weeks=[("week 1 - specify",HUMAN,"kept: a specification","a colleague agrees it constitutes the task"),
       ("week 2 - verify",GATE,"kept: a verification record","no output is used before an external check passes"),
       ("week 3 - govern",INK,"kept: an audit trail","one an IT reviewer could inspect"),
       ("week 4 - compose",AGENT,"kept: a working governed workflow","did this save net effort once the checking is counted?")]
for i,(lab,col,kept,ann) in enumerate(weeks):
    x=90+i*366
    f.box(x,470,300,70,lab,col,lw=22)
    if i: f.hline(x-66+4,x-6,505)
    f.text(x,580,kept,T_ANNOT,"start",INK,weight="600")
    f.block(x,610,ann,width=26)
bracket(f,90,1486,700,"habits that survive a change of tool")
f.footer("The sequence matters more than the calendar.")
print("16.1",f.save("figures/figure-16-1.svg"))

# ---------------- 16.2 cost blocks ----------------
f=Fig("162","The cost model - inference is the smallest share",
      "The line item everyone watches is the smallest one on the canvas.")
base=640
blocks=[("model inference",120,AGENT,"falling fast - the cost everyone watches"),
        ("engineering",260,INK,"recurring human time - specify, wire, maintain"),
        ("evaluation",320,GATE,"is the agent reliable enough to use at all?"),
        ("verification (recurring)",400,GATE,"recurs for as long as the workflow runs - and does not fall as model prices fall"),
        ("failure & rework",200,GREY,"shrinks exactly to the degree the other three are funded")]
x=110
for i,(lab,h,col,ann) in enumerate(blocks):
    w=250
    dash="7 6" if i==4 else None
    f.box(x,base-h,w,h,lab,col,lw=16,dash=dash)
    f.block(x,base+40,ann,width=30)
    x+=w+36
bracket(f,110+2*(286),110+4*286-36,196,"where the spend actually concentrates",below=False)
f.footer("Magnitudes illustrative - dated figures in the repository.")
print("16.2",f.save("figures/figure-16-2.svg"))

# ---------------- 17.1 two layers ----------------
f=Fig("171","Two layers, two clocks",
      "What turns over in months goes to the repository; what holds goes to print.")
f.panel(90,210,1180,220,"#ECECE8",12); f.borders.append((90,210,1180,220))
f.text(114,246,"volatile - tooling",T_LABEL,fill=GREY,weight="600",inside=True)
for i,lab in enumerate(["model versions","prices","protocols","benchmarks"]):
    f.box(130+i*280,286,240,64,lab,GREY,lw=18)
f.text(114,404,"turns over in months - faster than any publishing cycle",T_ANNOT,"start",SOFT,inside=True)
f.box(1320,268,200,60,"repository",INK,lw=14)
f.block(1320,360,"versioned, dated, corrected between releases",width=18)
f.rect(90,480,1180,230,GREY,"none",12,2.6)
f.text(114,516,"durable - principles",T_LABEL,fill=INK,weight="600",inside=True)
for i,lab in enumerate(["instrument stance","specification","verification","accountability"]):
    f.box(130+i*280,556,240,64,lab,INK,lw=16)
f.text(114,680,"derives from how science treats any instrument - it predates these models and will outlast them",T_ANNOT,"start",SOFT,inside=True)
f.box(1320,540,200,60,"print",INK,lw=8)
f.block(1320,632,"the position and the reasoning",width=18)
f.footer("Read the reasoning in print, fetch the current detail from the repository - neither is complete alone.")
print("17.1",f.save("figures/figure-17-1.svg"))
