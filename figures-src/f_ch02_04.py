import sys; sys.path.insert(0,'figures-src')
from templates import *

# ---------------- 2.1 loop as rectangle cycle ----------------
f=Fig("21","The plan-act-observe loop",
      "The loop corrects only the errors its observe step can actually see.")
f.box(560,236,200,80,"plan",AGENT)
f.box(920,436,200,80,"act",TOOL)
f.box(200,436,200,80,"observe",INK)
f.elbow([(760,276),(1020,276),(1020,436-40-6)])            # plan -> act
f.hline(914,306,476)                                        # act -> observe (leftwards)
f.elbow([(300,430),(300,300),(554,300)])                    # observe -> plan
f.block(492,352,"the model proposes one action",width=24)
f.block(852,552,"machinery outside the model carries it out",width=26)
f.block(56,552,"the result comes back, whether it is an answer or an error",width=17)
f.box(96,236,150,70,"goal",HUMAN,rx=18)
f.hline(246,554,271)
f.text(400,251,"written before the loop starts",T_ANNOT,"middle",SOFT)
f.cylinder(530,640,190,86,"state / memory")
f.elbow([(236,516),(236,600),(430,600),(430,640+16)],STORE)
f.text(340,586,"what the next step gets to see",T_ANNOT,"start",SOFT)
f.elbow([(625,640-4),(625,600),(716,600),(716,318)],STORE)
f.diamond(1210,256,190,84,"stop condition",GATE)
f.hline(766,1109,256,arrow=True)
f.text(940,238,"check after each plan",T_ANNOT,"middle",SOFT)
f.block(1130,360,"succeed and halt, or fail and hand back",width=22)
f.hline(1305,1400,256); f.text(1352,240,"done",T_ANNOT,"middle",SOFT)
f.box(1400,221,140,70,"result",STORE)
f.callout(1040,560,420,"a loop corrects only what this step can see - a silent wrong answer is invisible here",width=40)
f.footer("The cycle, not any single response, is the engine: plan, act, observe, and repeat until the stop condition ends it.")
print("2.1",f.save("figures/figure-2-1.svg"))

# ---------------- 2.2 tool call lanes ----------------
f=Fig("22","One tool call, four parts",
      "Each of the four parts is a place you can bound what the agent does.")
xs=lanes(f,[("agent","agent (model)",AGENT),("tool","tool / interpreter",TOOL)],
   [(0,0,"1 declaration is read","bounds what the model may even attempt - least privilege lives here",INK),
    (0,1,"2 invocation","the model chooses the operation and its arguments",INK),
    (1,1,"3 execution","outside the model, and not under its control",INK),
    (1,0,"4 returned result","this becomes the loop's observation",INK)],
   top=200,first=320,last=600)
f.cylinder(xs[0]-80,668,160,80,"state / memory")
f.text(xs[0]+110,700,"the result is written to state",T_ANNOT,"start",SOFT)
f.callout(940,668,540,"a plausible wrong answer at step 4 is worse than an error - it defeats the loop's only means of correction",width=48)
f.footer("A correct tool can still be pointed at the wrong quantity: the invocation, not the execution, is where that happens.")
print("2.2",f.save("figures/figure-2-2.svg"))

# ---------------- 2.3 context window vs durable memory ----------------
f=Fig("23","The working store and the durable store",
      "One of these two stores forgets everything the moment the run ends.")
f.rect(90,220,760,420,STORE,"none",12,2.4)
f.text(110,254,"context window",T_LABEL,fill=STORE,weight="600")
f.o.append(f'<rect x="846" y="220" width="9" height="420" fill="{GREY}"/>')
bands=[("specification",HILITE,"attended to most reliably"),
       ("retrieved material","#E8E8E4","attended to less reliably"),
       ("tool results","#E8E8E4","attended to less reliably"),
       ("running transcript",HILITE,"attended to most reliably")]
for i,(lab,fill,note) in enumerate(bands):
    yy=286+i*82
    f.panel(120,yy,540,62,fill,6)
    f.text(140,yy+38,lab,T_LABEL,inside=True)
    f.block(676,yy+26,note,width=15)
f.text(866,254,"capacity limit",T_ANNOT,"start",SOFT)
f.block(866,286,"every tool result the loop appends uses some of this up",width=16)
f.text(90,676,"within a run",T_ANNOT,"start",GREY)
f.block(90,706,"a constraint that falls out of here is a constraint the agent no longer honours",width=64)
f.cylinder(1180,300,260,180,"durable memory")
f.block(1180,516,"files · records · version control",width=26)
f.text(1180,560,"where provenance lives",T_ANNOT,"start",GATE)
f.text(1180,676,"across runs",T_ANNOT,"start",GREY)
f.hline(1064,1170,380); f.hline(1170,1064,420)
f.text(1117,352,"externalise",T_ANNOT,"middle",SOFT)
f.text(1117,452,"retrieve",T_ANNOT,"middle",SOFT)
f.block(1180,706,"write out what has to survive; read back only what this step needs",width=30)
f.footer("Fitting something into the window is not the same as having it used - and the window empties when the run ends.")
print("2.3",f.save("figures/figure-2-3.svg"))

# ---------------- 3.1 specification anatomy ----------------
f=Fig("31","The seven fields of a specification",
      "Four fields let an agent do the work; three more let a human check it.")
f.rect(210,196,1076,548,GREY,"none",14,2)
f.text(232,230,"specification",T_LABEL,fill=GREY,weight="600")
L=[("objective","state an outcome, not a procedure"),
   ("inputs","name them exactly - an unnamed input gets substituted silently"),
   ("acceptance criteria","checks somebody other than the agent could apply"),
   ("stop conditions","when to stop succeeding, and when to stop failing")]
R=[("assumptions & conventions","units, grids, calendars, missing-value codes - written down, or ungoverned"),
   ("provenance requirement","what the run must record about itself"),
   ("reviewer","a criterion with nobody named to apply it is decorative")]
for i,(lab,ann) in enumerate(L):
    yy=262+i*118
    f.box(250,yy,240,66,lab,HUMAN,rx=16,lw=16)
    f.block(510,yy+22,ann,width=24)
for i,(lab,ann) in enumerate(R):
    yy=286+i*150
    f.box(790,yy,250,66,lab,STORE,rx=16,lw=16)
    f.block(1058,yy+16,ann,width=18)
f.text(250,772,"executable",T_ANNOT,"start",HUMAN)
f.text(790,772,"auditable",T_ANNOT,"start",STORE)
f.agent_glyph(120,430); f.text(120,486,"agent",T_LABEL,"middle")
f.hline(150,204,430)
f.diamond(1400,560,140,80,"check",GATE)
f.elbow([(370,262+2*118+66),(370,712),(1400,712),(1400,604)])
f.human(1400,430); f.text(1400,486,"reviewer applies it",T_ANNOT,"middle",SOFT)
f.vline(1400,462+34,516,HUMAN,1.6,arrow=False)
f.footer("The reviewer field is the one that makes the rest bite: this schema returns in Chapters 10 and 15.")
print("3.1",f.save("figures/figure-3-1.svg"))

# ---------------- 3.2 weak vs strong ----------------
f=Fig("32",'"Verify this rainfall forecast" - weak and strong',
      "Four choices get made either way - the only question is by whom.")
band_title(f,70,200,"weak (conversational)",GREY)
f.human(120,300); f.text(120,354,"scientist",T_ANNOT,"middle",SOFT)
f.box(230,264,270,72,'"verify this rainfall forecast"',INK,rx=16,lw=20)
f.hline(150,224,300); f.hline(500,560,300)
f.agent_glyph(600,292); f.text(600,354,"agent",T_ANNOT,"middle",SOFT)
for i,q in enumerate(["which metric?","which reference?","which period?","when to stop?"]):
    f.box(720,206+i*62,190,48,q,GREY,lw=16)
f.hline(640,714,300)
f.block(930,236,"the agent answers all four itself, silently",width=18)
f.box(1160,264,220,72,"fluent output",GREY)
f.hline(916,1154,300)
f.vnote(1160,376,"plausible, unauditable",GATE,width=24)
f.block(1160,410,"a wrong verification that looks right is worse than an obvious error",width=30)
band_title(f,70,520,"strong (specified)")
f.human(120,610); f.text(120,664,"scientist",T_ANNOT,"middle",SOFT)
f.rect(220,548,560,140,HUMAN,"none",12,2.2)
for i,lab in enumerate(["objective","inputs","acceptance criteria","stop conditions"]):
    f.box(240+i*136,570,124,52,lab,HUMAN,rx=10,lw=12)
f.text(240,712,"the scientist answers the same four, in writing, before the run",T_ANNOT,"start",SOFT)
f.hline(150,214,618); f.hline(780,846,618)
f.agent_glyph(886,610); f.text(886,668,"agent",T_ANNOT,"middle",SOFT)
f.hline(926,1000,618)
f.diamond(1070,618,140,74,"check",GATE)
f.block(972,700,"somebody other than the agent can test it",width=22)
f.hline(1140,1210,618)
f.box(1220,582,220,72,"auditable output",TOOL)
f.block(1226,690,"not made correct - made detectable when wrong",width=20)
f.footer("The specification does not make the verification correct; it makes a wrong verification detectable.")
print("3.2",f.save("figures/figure-3-2.svg"))

# ---------------- 4.1 decision flowchart ----------------
f=Fig("41","Should an agent do this?",
      "Neither question is about how good the agent is.")
sx=430
f.box(sx-70,176,140,54,"task",GREY)
f.vline(sx,230,266)
f.diamond(sx,340,360,86,"accountability, interpretation or authorship?",GATE,lw=26)
f.block(60,300,"no improvement in capability changes this answer",width=24)
f.hline(sx+180+4,1180,340); f.text(820,324,"yes",T_ANNOT,"middle",SOFT)
f.human(1250,330); f.text(1250,388,"human only - do not delegate",T_ANNOT,"middle")
f.text(1250,414,"not an instrument's to do",T_ANNOT,"middle",SOFT)
f.vline(sx,340+77,462); f.text(sx-24,442,"no",T_ANNOT,"end",SOFT)
f.diamond(sx,530,300,80,"verification cheap?",GATE)
f.block(60,500,"cheap: a test suite, a schema, a checksum. Not cheap: interpretation, or an unresolved research question",width=24)
f.hline(sx+154,660,530); f.text(560,514,"yes",T_ANNOT,"middle",SOFT)
f.diamond(810,530,280,80,"wrong output reversible?",GATE,lw=20)
f.vline(sx,530+74,668); f.text(sx-24,650,"no",T_ANNOT,"end",SOFT)
f.diamond(sx,724,280,80,"wrong output reversible?",GATE,lw=20)
f.block(945,232,"reversible: a mislabelled intermediate file. Not reversible: an issued flood warning, a published result",width=38)
f.hline(810+144,1010,530); f.text(972,514,"yes",T_ANNOT,"middle",SOFT)
f.box(1010,470,250,64,"agent runs, light supervision",AGENT,lw=20)
f.elbow([(810,530+74),(810,624),(1010,624)]); f.text(852,610,"no",T_ANNOT,"middle",SOFT)
f.box(1010,592,250,64,"agent acts behind a mandatory gate",AGENT,lw=20)
f.hline(sx+144,1010,724); f.text(770,708,"yes",T_ANNOT,"middle",SOFT)
f.box(1010,692,250,64,"agent drafts only, human verifies",AGENT,lw=20)
f.elbow([(sx-140-6,724),(160,724)])  # no-exit heads left
f.text(226,706,"no",T_ANNOT,"middle",SOFT)
f.box(60,692,96,64,"human only",HUMAN,lw=8)
f.text(60,788,"expensive to verify and irreversible: do not delegate",T_ANNOT,"start",SOFT)
f.box(1290,692,190,64,"human only",HUMAN,lw=14)
bracket(f,1010,1400,776,"augmentation - a human stands between output and use")
f.footer("The first gate removes what was never an instrument's to do; the rest is verification cost against reversibility.")
print("4.1",f.save("figures/figure-4-1.svg"))
