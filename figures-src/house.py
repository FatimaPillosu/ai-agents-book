"""House style primitives for the book's figures (FIGURES.md v2.0).

One renderer for all 51 figures, so palette, type hierarchy, geometry and
icon vocabulary cannot drift between them. Emits plain SVG: no dependencies,
deterministic output, and every string placed exactly where the brief says.
"""

W, H = 1600, 900                      # 16:9 canvas

INK      = "#111111"
PAPER    = "#F7F7F5"
HUMAN    = "#0072B2"
AGENT    = "#E69F00"
TOOL     = "#009E73"
STORE    = "#56B4E9"
GATE     = "#D55E00"
REVIEWER = "#CC79A7"
HILITE   = "#F0E442"
GREY     = "#999999"

FONT = "Inter, 'Helvetica Neue', Helvetica, Arial, sans-serif"

# five-level type hierarchy, FIGURES.md 3.3
T_TITLE, T_STAND, T_LABEL, T_ANNOT, T_KEY = 40, 24, 19, 14.5, 13.5


def esc(t):
    return (t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def wrap(text, width):
    """Greedy wrap to `width` characters, returning a list of lines."""
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if len(trial) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


class Fig:
    def __init__(self, fid, title, standfirst):
        self.o = []
        self.fid = fid
        self.o.append(
            f'<rect x="0" y="0" width="{W}" height="{H}" fill="{PAPER}"/>')
        self.text(56, 74, title, T_TITLE, weight="600")
        for i, ln in enumerate(wrap(standfirst, 96)):
            self.text(56, 116 + i * 30, ln, T_STAND, fill="#3A3A3A")

    # --- primitives -----------------------------------------------------
    def text(self, x, y, s, size=T_LABEL, anchor="start", fill=INK,
             weight="400", italic=False):
        st = ' font-style="italic"' if italic else ""
        self.o.append(
            f'<text x="{x:.1f}" y="{y:.1f}" font-family="{FONT}" '
            f'font-size="{size}" fill="{fill}" font-weight="{weight}" '
            f'text-anchor="{anchor}"{st}>{esc(s)}</text>')

    def block(self, x, y, s, size=T_ANNOT, width=34, anchor="start",
              fill="#3A3A3A", lh=None, weight="400"):
        """Multi-line text block; returns the y of the line after the last."""
        lh = lh or size * 1.32
        for i, ln in enumerate(wrap(s, width)):
            self.text(x, y + i * lh, ln, size, anchor, fill, weight)
        return y + len(wrap(s, width)) * lh

    def rect(self, x, y, w, h, stroke=INK, fill="none", rx=10, sw=2, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.o.append(
            f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" '
            f'rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>')

    def box(self, x, y, w, h, label, colour=INK, fill="none", size=T_LABEL,
            rx=10, sw=2, label_width=24):
        self.rect(x, y, w, h, colour, fill, rx, sw)
        lines = wrap(label, label_width)
        y0 = y + h / 2 - (len(lines) - 1) * size * 0.66
        for i, ln in enumerate(lines):
            self.text(x + w / 2, y0 + i * size * 1.32 + size * 0.34, ln,
                      size, "middle", INK)

    def diamond(self, cx, cy, w, h, label, colour=GATE, size=T_LABEL,
                label_width=22):
        p = f"{cx},{cy-h/2} {cx+w/2},{cy} {cx},{cy+h/2} {cx-w/2},{cy}"
        self.o.append(f'<polygon points="{p}" fill="none" stroke="{colour}" '
                      f'stroke-width="2.4"/>')
        lines = wrap(label, label_width)
        y0 = cy - (len(lines) - 1) * size * 0.66
        for i, ln in enumerate(lines):
            self.text(cx, y0 + i * size * 1.32 + size * 0.34, ln, size,
                      "middle", INK)

    def cylinder(self, x, y, w, h, label, colour=STORE, size=T_LABEL):
        ry = h * 0.13
        self.o.append(
            f'<path d="M{x},{y+ry} a{w/2},{ry} 0 0 1 {w},0 v{h-2*ry} '
            f'a{w/2},{ry} 0 0 1 -{w},0 z" fill="none" stroke="{colour}" '
            f'stroke-width="2.2"/>')
        self.o.append(
            f'<path d="M{x},{y+ry} a{w/2},{ry} 0 0 0 {w},0" fill="none" '
            f'stroke="{colour}" stroke-width="2.2"/>')
        lines = wrap(label, 20)
        y0 = y + h / 2 + ry * 0.4 - (len(lines) - 1) * size * 0.66
        for i, ln in enumerate(lines):
            self.text(x + w / 2, y0 + i * size * 1.32, ln, size, "middle", INK)

    def human(self, cx, cy, colour=HUMAN, r=17, tick=False):
        self.o.append(f'<circle cx="{cx}" cy="{cy-r*0.85}" r="{r*0.62}" '
                      f'fill="none" stroke="{colour}" stroke-width="2.4"/>')
        self.o.append(
            f'<path d="M{cx-r},{cy+r*0.75} a{r},{r*0.95} 0 0 1 {2*r},0" '
            f'fill="none" stroke="{colour}" stroke-width="2.4"/>')
        if tick:
            self.o.append(
                f'<path d="M{cx+r*0.55},{cy-r*0.1} l{r*0.35},{r*0.38} '
                f'l{r*0.7},-{r*0.85}" fill="none" stroke="{colour}" '
                f'stroke-width="2.6" stroke-linecap="round"/>')

    def agent_glyph(self, cx, cy, colour=AGENT, s=20):
        self.rect(cx - s, cy - s, 2 * s, 2 * s, colour, "none", 7, 2.4)
        self.o.append(
            f'<path d="M{cx-s*0.42},{cy+s*0.12} a{s*0.45},{s*0.45} 0 1 1 '
            f'{s*0.5},{s*0.36}" fill="none" stroke="{colour}" '
            f'stroke-width="2.2" marker-end="url(#ah{self.fid})"/>')

    def wrench(self, cx, cy, colour=TOOL, s=17):
        self.o.append(
            f'<path d="M{cx-s*0.75},{cy+s*0.75} l{s*1.0},-{s*1.0} '
            f'M{cx+s*0.35},{cy-s*0.35} a{s*0.42},{s*0.42} 0 1 0 {s*0.5},{s*0.5}" '
            f'fill="none" stroke="{colour}" stroke-width="2.6" '
            f'stroke-linecap="round"/>')

    def arrow(self, x1, y1, x2, y2, colour=INK, sw=2.2, dash=None, label=None,
              lside="above", lsize=T_ANNOT):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.o.append(
            f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="{colour}" stroke-width="{sw}"{d} '
            f'marker-end="url(#ah{self.fid})"/>')
        if label:
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2
            off = -9 if lside == "above" else 20
            self.text(mx, my + off, label, lsize, "middle", "#3A3A3A")

    def elbow(self, pts, colour=INK, sw=2.2, dash=None, label=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        path = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)
        self.o.append(f'<path d="{path}" fill="none" stroke="{colour}" '
                      f'stroke-width="{sw}"{d} marker-end="url(#ah{self.fid})"/>')
        if label:
            mx, my = pts[len(pts) // 2]
            self.text(mx, my - 10, label, T_ANNOT, "middle", "#3A3A3A")

    def callout(self, x, y, w, s, fill=HILITE, stroke=None, width=40,
                size=T_ANNOT, pad=13):
        lines = wrap(s, width)
        h = len(lines) * size * 1.34 + pad * 2 - 4
        self.rect(x, y, w, h, stroke or "none", fill, 8,
                  1.6 if stroke else 0)
        for i, ln in enumerate(lines):
            self.text(x + pad, y + pad + size * 0.95 + i * size * 1.34, ln,
                      size, "start", INK)
        return y + h

    def note(self, x, y, s, colour=GATE, width=40, size=T_ANNOT):
        """A vermillion (or other) emphasis note with a leading rule."""
        lines = wrap(s, width)
        h = len(lines) * size * 1.34
        self.o.append(f'<rect x="{x:.1f}" y="{y-size:.1f}" width="3.5" '
                      f'height="{h:.1f}" fill="{colour}"/>')
        for i, ln in enumerate(lines):
            self.text(x + 13, y + i * size * 1.34, ln, size, "start", colour)
        return y + h

    def footer(self, s):
        self.text(56, H - 34, s, T_KEY, fill=GREY, italic=True)

    def key(self, x, y, entries):
        cx = x
        for colour, lab in entries:
            self.o.append(f'<rect x="{cx}" y="{y-11}" width="15" height="15" '
                          f'rx="3" fill="{colour}"/>')
            self.text(cx + 23, y + 1, lab, T_KEY, fill="#3A3A3A")
            cx += 30 + len(lab) * 7.4

    def save(self, path):
        head = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" '
                f'height="{H}" viewBox="0 0 {W} {H}" role="img">\n'
                f'<defs><marker id="ah{self.fid}" viewBox="0 0 10 10" '
                f'refX="9" refY="5" markerWidth="7" markerHeight="7" '
                f'orient="auto-start-reverse">'
                f'<path d="M0,0 L10,5 L0,10 z" fill="{INK}"/></marker></defs>\n')
        with open(path, "w") as f:
            f.write(head + "\n".join(self.o) + "\n</svg>\n")
