"""Reusable layouts on top of house.Fig — all geometry zoned, all QC-checked."""
import sys; sys.path.insert(0,'figures-src')
from house import *

def draw_node(f, kind, cx, cy, w, h, label, colour, fill="none", dash=None):
    if kind=="box":     f.box(cx-w/2,cy-h/2,w,h,label,colour,fill,rx=10,dash=dash)
    elif kind=="tag":   f.box(cx-w/2,cy-h/2,w,h,label,colour,fill,rx=18,dash=dash)
    elif kind=="diamond": f.diamond(cx,cy,w,h+34,label,colour)
    elif kind=="cyl":   f.cylinder(cx-w/2,cy-h/2,w,h,label,colour)
    elif kind=="human":
        f.human(cx,cy-6,colour); f.text(cx,cy+h/2+6,label,T_LABEL,"middle")
    elif kind=="reviewer":
        f.human(cx,cy-6,colour,tick=True); f.text(cx,cy+h/2+6,label,T_LABEL,"middle")
    elif kind=="agent":
        f.agent_glyph(cx,cy-8,colour); f.text(cx,cy+h/2+6,label,T_LABEL,"middle")
    elif kind=="tool":
        f.wrench(cx,cy-8,colour); f.text(cx,cy+h/2+6,label,T_LABEL,"middle")

def chain(f, nodes, y=330, x0=70, x1=1540, node_h=92, ann_gap=64, arrows=True):
    """Horizontal chain. Each node: dict(kind,label,colour,ann,alab).
    Returns list of (cx, colw). Annotations go in their own band below."""
    n=len(nodes); colw=(x1-x0)/n
    cs=[x0+colw*(i+.5) for i in range(n)]
    for i,(nd,cx) in enumerate(zip(nodes,cs)):
        w=nd.get("w",colw-56)
        draw_node(f,nd["kind"],cx,y,w,node_h,nd["label"],nd.get("colour",INK),
                  nd.get("fill","none"),nd.get("dash"))
        if nd.get("ann"):
            f.block(cx-(colw-70)/2, y+node_h/2+ann_gap, nd["ann"],
                    width=max(12,int((colw-70)/(T_ANNOT*CHAR))))
    if arrows:
        for i in range(n-1):
            xa=cs[i]+ (nodes[i].get("w",colw-56))/2 +6
            xb=cs[i+1]-(nodes[i+1].get("w",colw-56))/2 -6
            f.hline(xa,xb,y)
            if i<len(nodes)-1 and nodes[i].get("alab"):
                f.text((xa+xb)/2, y-16, nodes[i]["alab"], T_ANNOT,"middle",SOFT)
    return cs, colw

def lanes(f, heads, steps, top=214, first=318, last=735):
    """Sequence lanes. heads: [(kind,label,colour[,ann])]; steps:
    [(frm,to,label,ann,colour)] with frm==to for a self step."""
    n=len(heads); colw=(1600-140)/n
    xs=[70+colw*(i+.5) for i in range(n)]
    for (hd,x) in zip(heads,xs):
        kind,label,colour=hd[0],hd[1],hd[2]
        draw_node(f,kind,x,top+30,min(colw-60,290),74,label,colour)
        if len(hd)>3 and hd[3]:
            f.block(x-(colw-80)/2,top+96,hd[3],
                    width=max(12,int((colw-80)/(T_ANNOT*CHAR))),size=T_ANNOT)
    m=len(steps); dy=(last-first)/max(1,m-1) if m>1 else 0
    for k,(a,b,lab,ann,col) in enumerate(steps):
        yy=first+k*dy
        if a==b:
            x=xs[a]; f.hline(x-52,x+52,yy,col)
            f.text(x,yy-16,lab,T_ANNOT,"middle",INK,"600")
            if ann: f.text(x,yy+24,ann,T_ANNOT,"middle",SOFT)
        else:
            x1,x2=xs[a],xs[b]
            f.hline(x1+(34 if x1<x2 else -34), x2-(34 if x1<x2 else -34), yy, col)
            mx=(x1+x2)/2
            f.text(mx,yy-16,lab,T_ANNOT,"middle",INK,"600")
            if ann: f.text(mx,yy+24,ann,T_ANNOT,"middle",SOFT)
    return xs

def band_title(f,x,y,s,colour=SOFT):
    f.text(x,y,s,T_LABEL,fill=colour,weight="600")

def bracket(f,x1,x2,y,label,colour=GREY,below=True):
    """A thin square bracket with a centred label that has its own space."""
    d=10 if below else -10
    f.o.append(f'<path d="M{x1},{y} v{d} M{x1},{y+d} H{x2} M{x2},{y+d} v{-d}"'
               f' fill="none" stroke="{colour}" stroke-width="1.8"/>')
    f.segs.append((x1,min(y,y+d),x2,max(y,y+d)))
    f.text((x1+x2)/2, y+d+(20 if below else -10), label, T_ANNOT,"middle",SOFT)
