"""House renderer v2 for the book's figures (FIGURES.md v2.0).

Guarantees the author asked for:
  * connectors are orthogonal only (horizontal/vertical segments);
  * every text sits in its own reserved space;
  * a collision checker (qc) verifies no text bbox crosses a line segment,
    a shape border, or another text bbox. Renders fail QC rather than ship.
Canvas zones: header y<150 | content 150..760 | footer y>780.
"""

W, H = 1600, 900

INK="#111111"; PAPER="#F7F7F5"; HUMAN="#0072B2"; AGENT="#E69F00"
TOOL="#009E73"; STORE="#56B4E9"; GATE="#D55E00"; REVIEWER="#CC79A7"
HILITE="#F0E442"; GREY="#999999"; SOFT="#3A3A3A"
FONT="Inter, 'Helvetica Neue', Helvetica, Arial, sans-serif"
T_TITLE, T_STAND, T_LABEL, T_ANNOT, T_KEY = 38, 22, 18, 14, 13

CHAR = 0.545          # width of one character in em, average for the face

def esc(t):
    return t.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

def wrap(text, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t=(cur+" "+w).strip()
        if len(t)<=width: cur=t
        else:
            if cur: lines.append(cur)
            cur=w
    if cur: lines.append(cur)
    return lines

class Fig:
    def __init__(self, fid, title, standfirst):
        self.fid=fid; self.o=[]; self.texts=[]; self.segs=[]; self.borders=[]
        self.o.append(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
        self._t(56,72,title,T_TITLE,"start",INK,"600")
        y=112
        for ln in wrap(standfirst,110):
            self._t(56,y,ln,T_STAND,"start",SOFT); y+=29

    # ---- low level -------------------------------------------------------
    def _t(self,x,y,s,size,anchor,fill,weight="400",italic=False,inside=False):
        st=' font-style="italic"' if italic else ""
        self.o.append(f'<text x="{x:.1f}" y="{y:.1f}" font-family="{FONT}" '
            f'font-size="{size}" fill="{fill}" font-weight="{weight}" '
            f'text-anchor="{anchor}"{st}>{esc(s)}</text>')
        w=len(s)*size*CHAR
        x0 = x if anchor=="start" else (x-w if anchor=="end" else x-w/2)
        if not inside:
            self.texts.append((x0,y-size*0.86,w,size*1.08,s))

    def text(self,x,y,s,size=T_LABEL,anchor="start",fill=INK,weight="400",
             italic=False,inside=False):
        self._t(x,y,s,size,anchor,fill,weight,italic,inside)

    def block(self,x,y,s,size=T_ANNOT,width=30,anchor="start",fill=SOFT,
              weight="400",inside=False):
        lh=size*1.34
        for i,ln in enumerate(wrap(s,width)):
            self._t(x,y+i*lh,ln,size,anchor,fill,weight,False,inside)
        return y+len(wrap(s,width))*lh

    def _border(self,x,y,w,h):
        self.borders.append((x,y,w,h))

    def rect(self,x,y,w,h,stroke=INK,fill="none",rx=10,sw=2,dash=None):
        d=f' stroke-dasharray="{dash}"' if dash else ""
        self.o.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" '
            f'height="{h:.1f}" rx="{rx}" fill="{fill}" stroke="{stroke}" '
            f'stroke-width="{sw}"{d}/>')
        if stroke!="none": self._border(x,y,w,h)

    def panel(self,x,y,w,h,fill,rx=10):
        self.o.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" '
            f'height="{h:.1f}" rx="{rx}" fill="{fill}" stroke="none"/>')

    def box(self,x,y,w,h,label,colour=INK,fill="none",size=T_LABEL,rx=10,
            sw=2.2,lw=None,dash=None):
        self.rect(x,y,w,h,colour,fill,rx,sw,dash)
        lw=lw or max(8,int(w/(size*CHAR))-2)
        lines=wrap(label,lw)
        y0=y+h/2-(len(lines)-1)*size*0.67
        for i,ln in enumerate(lines):
            self._t(x+w/2,y0+i*size*1.34+size*0.34,ln,size,"middle",INK,
                    "400",False,True)

    def diamond(self,cx,cy,w,h,label,colour=GATE,size=T_LABEL,lw=16):
        p=f"{cx},{cy-h/2} {cx+w/2},{cy} {cx},{cy+h/2} {cx-w/2},{cy}"
        self.o.append(f'<polygon points="{p}" fill="none" stroke="{colour}" '
                      f'stroke-width="2.4"/>')
        self._border(cx-w/2,cy-h/2,w,h)
        lines=wrap(label,lw)
        y0=cy-(len(lines)-1)*size*0.67
        for i,ln in enumerate(lines):
            self._t(cx,y0+i*size*1.34+size*0.34,ln,size,"middle",INK,
                    "400",False,True)

    def cylinder(self,x,y,w,h,label,colour=STORE,size=T_LABEL):
        ry=h*0.14
        self.o.append(f'<path d="M{x},{y+ry} a{w/2},{ry} 0 0 1 {w},0 '
            f'v{h-2*ry} a{w/2},{ry} 0 0 1 -{w},0 z" fill="none" '
            f'stroke="{colour}" stroke-width="2.2"/>')
        self.o.append(f'<path d="M{x},{y+ry} a{w/2},{ry} 0 0 0 {w},0" '
            f'fill="none" stroke="{colour}" stroke-width="2.2"/>')
        self._border(x,y,w,h)
        lines=wrap(label,max(8,int(w/(size*CHAR))-2))
        y0=y+h/2+ry*0.5-(len(lines)-1)*size*0.67
        for i,ln in enumerate(lines):
            self._t(x+w/2,y0+i*size*1.34,ln,size,"middle",INK,"400",False,True)

    def human(self,cx,cy,colour=HUMAN,r=16,tick=False):
        self.o.append(f'<circle cx="{cx}" cy="{cy-r*0.85}" r="{r*0.6}" '
            f'fill="none" stroke="{colour}" stroke-width="2.3"/>')
        self.o.append(f'<path d="M{cx-r},{cy+r*0.7} a{r},{r*0.9} 0 0 1 '
            f'{2*r},0" fill="none" stroke="{colour}" stroke-width="2.3"/>')
        if tick:
            self.o.append(f'<path d="M{cx+r*0.6},{cy-r*0.1} l{r*0.32},{r*0.36}'
                f' l{r*0.66},-{r*0.8}" fill="none" stroke="{colour}" '
                f'stroke-width="2.5" stroke-linecap="round"/>')
        self._border(cx-r,cy-r*1.6,2*r,r*2.6)

    def agent_glyph(self,cx,cy,colour=AGENT,s=18):
        self.rect(cx-s,cy-s,2*s,2*s,colour,"none",6,2.3)
        self.o.append(f'<path d="M{cx-s*0.4},{cy+s*0.1} a{s*0.42},{s*0.42} '
            f'0 1 1 {s*0.48},{s*0.34}" fill="none" stroke="{colour}" '
            f'stroke-width="2"/>')

    def wrench(self,cx,cy,colour=TOOL,s=15):
        self.o.append(f'<path d="M{cx-s*0.7},{cy+s*0.7} l{s*0.95},-{s*0.95} '
            f'M{cx+s*0.3},{cy-s*0.3} a{s*0.4},{s*0.4} 0 1 0 {s*0.5},{s*0.5}" '
            f'fill="none" stroke="{colour}" stroke-width="2.5" '
            f'stroke-linecap="round"/>')
        self._border(cx-s,cy-s,2*s,2*s)

    # ---- connectors: orthogonal only ------------------------------------
    def hline(self,x1,x2,y,colour=INK,sw=2.1,dash=None,arrow=True):
        d=f' stroke-dasharray="{dash}"' if dash else ""
        m=f' marker-end="url(#ah{self.fid})"' if arrow else ""
        self.o.append(f'<line x1="{x1:.1f}" y1="{y:.1f}" x2="{x2:.1f}" '
            f'y2="{y:.1f}" stroke="{colour}" stroke-width="{sw}"{d}{m}/>')
        self.segs.append((min(x1,x2),y,max(x1,x2),y))

    def vline(self,x,y1,y2,colour=INK,sw=2.1,dash=None,arrow=True):
        d=f' stroke-dasharray="{dash}"' if dash else ""
        m=f' marker-end="url(#ah{self.fid})"' if arrow else ""
        self.o.append(f'<line x1="{x:.1f}" y1="{y1:.1f}" x2="{x:.1f}" '
            f'y2="{y2:.1f}" stroke="{colour}" stroke-width="{sw}"{d}{m}/>')
        self.segs.append((x,min(y1,y2),x,max(y1,y2)))

    def elbow(self,pts,colour=INK,sw=2.1,dash=None):
        for (x1,y1),(x2,y2) in zip(pts,pts[1:]):
            assert abs(x1-x2)<0.01 or abs(y1-y2)<0.01, "orthogonal only"
        d=f' stroke-dasharray="{dash}"' if dash else ""
        path="M"+" L".join(f"{x:.1f},{y:.1f}" for x,y in pts)
        self.o.append(f'<path d="{path}" fill="none" stroke="{colour}" '
            f'stroke-width="{sw}"{d} marker-end="url(#ah{self.fid})"/>')
        for (x1,y1),(x2,y2) in zip(pts,pts[1:]):
            self.segs.append((min(x1,x2),min(y1,y2),max(x1,x2),max(y1,y2)))

    def callout(self,x,y,w,s,fill=HILITE,width=None,size=T_ANNOT,pad=12):
        width=width or max(10,int((w-2*pad)/(size*CHAR)))
        lines=wrap(s,width)
        h=len(lines)*size*1.34+2*pad-4
        self.panel(x,y,w,h,fill,8)
        for i,ln in enumerate(lines):
            self._t(x+pad,y+pad+size*0.9+i*size*1.34,ln,size,"start",INK,
                    "400",False,True)
        return y+h

    def vnote(self,x,y,s,colour=GATE,width=34,size=T_ANNOT):
        lines=wrap(s,width)
        h=len(lines)*size*1.34
        self.o.append(f'<rect x="{x:.1f}" y="{y-size*0.9:.1f}" width="3.4" '
            f'height="{h:.1f}" fill="{colour}"/>')
        for i,ln in enumerate(lines):
            self._t(x+12,y+i*size*1.34,ln,size,"start",colour)
        return y+h

    def footer(self,s):
        self.block(56,H-40,s,T_KEY,width=150,fill=GREY,weight="400")

    def key(self,entries,y=None):
        y=y or H-76; cx=56
        for colour,lab in entries:
            self.o.append(f'<rect x="{cx}" y="{y-11}" width="14" height="14" '
                f'rx="3" fill="{colour}"/>')
            self._t(cx+21,y+1,lab,T_KEY,"start",SOFT)
            cx+=42+len(lab)*T_KEY*CHAR

    # ---- QC --------------------------------------------------------------
    def qc(self):
        bad=[]
        def overlap(a,b,pad=2):
            ax,ay,aw,ah=a[:4]; bx,by,bw,bh=b[:4]
            return not(ax+aw+pad<bx or bx+bw+pad<ax or
                       ay+ah+pad<by or by+bh+pad<ay)
        for i in range(len(self.texts)):
            for j in range(i+1,len(self.texts)):
                if overlap(self.texts[i],self.texts[j]):
                    bad.append(("text/text",self.texts[i][4],self.texts[j][4]))
        for (tx,ty,tw,th,s) in self.texts:
            for (x1,y1,x2,y2) in self.segs:
                if not(tx+tw+2<x1 or x2+2<tx or ty+th+2<y1 or y2+2<ty):
                    bad.append(("text/line",s,f"seg {x1:.0f},{y1:.0f}"))
            for (bx,by,bw,bh) in self.borders:
                edges=[(bx,by,bx+bw,by),(bx,by+bh,bx+bw,by+bh),
                       (bx,by,bx,by+bh),(bx+bw,by,bx+bw,by+bh)]
                for (x1,y1,x2,y2) in edges:
                    if not(tx+tw+1<x1 or x2+1<tx or ty+th+1<y1 or y2+1<ty):
                        bad.append(("text/border",s,f"{bx:.0f},{by:.0f}"))
                        break
        return bad

    def save(self,path,strict=True):
        head=(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" '
              f'height="{H}" viewBox="0 0 {W} {H}" role="img">\n<defs>'
              f'<marker id="ah{self.fid}" viewBox="0 0 10 10" refX="9" '
              f'refY="5" markerWidth="6.5" markerHeight="6.5" '
              f'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" '
              f'fill="{INK}"/></marker></defs>\n')
        open(path,"w").write(head+"\n".join(self.o)+"\n</svg>\n")
        return self.qc() if strict else []
