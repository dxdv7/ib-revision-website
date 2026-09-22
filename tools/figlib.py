"""Original vector redraws of standard economics diagrams.

Everything here is drawn from primitives; nothing is traced from or derived
from any published image. Diagram *conventions* (axes, downward demand,
upward supply, dashed guides to the axes) are standard economics.

IMPORTANT, do not repeat this bug: SVG/XML only predefines 5 entities
(&amp; &lt; &gt; &apos; &quot;). HTML named entities like &rsquo; &mdash;
&ndash; &hellip; &times; DO NOT EXIST in XML and will make the SVG fail
to parse (silently broken in real browsers, even though some quicklook/
preview tools render it anyway up to the bad line). Never write a named
HTML entity into .text()/.label() strings. Use a plain literal Unicode
character instead (') or, if the file must stay pure ASCII, a numeric
character reference (&#8217; for a right single quote, &#8212; for an
em dash, &#8211; for an en dash) - numeric refs are always legal XML.
Before calling a figure done, this must pass:
    python3 -c "import xml.etree.ElementTree as ET; ET.parse('file.svg')"
"""
import math

RED = "#d9432f"
GREY = "#6b6b6b"
TEAL = "#27b5c2"
PURPLE = "#4a3f9f"
INK = "#2b2b2b"
FONT = "Helvetica Neue, Helvetica, Arial, sans-serif"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


class Fig:
    """Plot area is x in [X0, X1], y in [Y0, Y1] (y grows downward on screen)."""

    def __init__(self, w=420, h=380, x0=78, y0=318, x1=384, y1=30):
        self.w, self.h = w, h
        self.X0, self.Y0, self.X1, self.Y1 = x0, y0, x1, y1
        self.parts = []

    # ---------- primitives ----------
    def add(self, s):
        self.parts.append(s)

    def text(self, x, y, s, size=12, anchor="start", color=INK, weight="400",
             rotate=None, italic=False):
        tr = f' transform="rotate({rotate} {x} {y})"' if rotate is not None else ""
        st = ' font-style="italic"' if italic else ""
        self.add(
            f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" text-anchor="{anchor}" '
            f'fill="{color}" font-weight="{weight}"{st}{tr}>{s}</text>'
        )

    def line(self, x1, y1, x2, y2, color=INK, width=2.4, dash=None, cap="round"):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(
            f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="{color}" stroke-width="{width}" stroke-linecap="{cap}"{d}/>'
        )

    def path(self, d, color=RED, width=2.8, fill="none", dash=None):
        da = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(
            f'<path d="{d}" fill="{fill}" stroke="{color}" stroke-width="{width}" '
            f'stroke-linecap="round" stroke-linejoin="round"{da}/>'
        )

    def dot(self, x, y, r=3.4, color=RED):
        self.add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{color}"/>')

    def arrowhead(self, x, y, angle_deg, color=INK, size=8):
        a = math.radians(angle_deg)
        p1 = (x, y)
        p2 = (x - size * math.cos(a) + size * 0.42 * math.sin(a),
              y - size * math.sin(a) - size * 0.42 * math.cos(a))
        p3 = (x - size * math.cos(a) - size * 0.42 * math.sin(a),
              y - size * math.sin(a) + size * 0.42 * math.cos(a))
        self.add(
            f'<polygon points="{p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f} '
            f'{p3[0]:.1f},{p3[1]:.1f}" fill="{color}"/>'
        )

    def arrow(self, x1, y1, x2, y2, color=PURPLE, width=2.0, head=8):
        ang = math.degrees(math.atan2(y2 - y1, x2 - x1))
        a = math.radians(ang)
        self.line(x1, y1, x2 - head * 0.6 * math.cos(a), y2 - head * 0.6 * math.sin(a),
                  color, width)
        self.arrowhead(x2, y2, ang, color, head)

    # ---------- data scale (keeps ticks, guides and curves aligned) ----------
    def scale(self, xmax, ymax, xpad=22, ypad=20):
        self._sx = (self.X1 - self.X0 - xpad) / xmax
        self._sy = (self.Y0 - self.Y1 - ypad) / ymax
        return self

    def px(self, v):
        return self.X0 + v * self._sx

    def py(self, v):
        return self.Y0 - v * self._sy

    def pt(self, xv, yv):
        return (self.px(xv), self.py(yv))

    def xticks(self, vals, fmt=lambda v: f"{v:,}"):
        for v in vals:
            self.xtick(self.px(v), fmt(v))

    def yticks(self, vals, fmt=lambda v: f"{v:,}"):
        for v in vals:
            self.ytick(self.py(v), fmt(v))

    def flow(self, pts, color=PURPLE, width=2.2, head=8):
        """Polyline with a single arrowhead at the final point."""
        for a, b in zip(pts[:-2], pts[1:-1]):
            self.line(a[0], a[1], b[0], b[1], color, width, cap="butt")
        a, b = pts[-2], pts[-1]
        self.arrow(a[0], a[1], b[0], b[1], color, width, head)

    # ---------- economics helpers ----------
    @staticmethod
    def x_at(line, y):
        (xa, ya), (xb, yb) = line
        return xa + (y - ya) * (xb - xa) / (yb - ya)

    @staticmethod
    def y_at(line, x):
        (xa, ya), (xb, yb) = line
        return ya + (x - xa) * (yb - ya) / (xb - xa)

    @staticmethod
    def intersect(l1, l2):
        """Exact intersection of two straight lines given as ((x,y),(x,y))."""
        (x1, y1), (x2, y2) = l1
        (x3, y3), (x4, y4) = l2
        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / den
        py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / den
        return (px, py)

    def equilibrium(self, l1, l2, xlabel=None, ylabel=None, dot=INK, guides=True):
        """Dot + dashed guides at the true intersection of two curves."""
        p = self.intersect(l1, l2)
        for l in (l1, l2):
            assert abs(self.y_at(l, p[0]) - p[1]) < 0.01, "point not on curve"
        if guides:
            self.guide(p[0], p[1], xlabel, ylabel)
        self.dot(p[0], p[1], 3.6, dot)
        return p

    def hshift(self, old, new, y, color=PURPLE, gap=4):
        """Horizontal shift arrow that starts on the old curve and ends on the
        new one at height y, so it shows exactly which way and how far it moved."""
        x1, x2 = self.x_at(old, y), self.x_at(new, y)
        d = gap if x2 > x1 else -gap
        self.arrow(x1 + d, y, x2 - d, y, color)

    def vshift(self, old, new, x, color=PURPLE, gap=4):
        y1, y2 = self.y_at(old, x), self.y_at(new, x)
        d = gap if y2 > y1 else -gap
        self.arrow(x, y1 + d, x, y2 - d, color)

    def axes(self, xlabel, ylabel, origin="0", xarrow=True, yarrow=True):
        self.line(self.X0, self.Y0, self.X1, self.Y0, INK, 2.2)
        self.line(self.X0, self.Y0, self.X0, self.Y1, INK, 2.2)
        if xarrow:
            self.arrowhead(self.X1 + 5, self.Y0, 0, INK, 9)
        if yarrow:
            self.arrowhead(self.X0, self.Y1 - 5, -90, INK, 9)
        if origin:
            self.text(self.X0 - 12, self.Y0 + 16, origin, 12, "end")
        self.text((self.X0 + self.X1) / 2, self.h - 14, xlabel, 12.5, "middle")
        self.text(20, (self.Y0 + self.Y1) / 2, ylabel, 12.5, "middle", rotate=-90)

    def xtick(self, x, label):
        self.text(x, self.Y0 + 18, label, 11, "middle")

    def ytick(self, y, label):
        self.text(self.X0 - 8, y + 4, label, 11, "end")

    def guide(self, x, y, xlabel=None, ylabel=None, to_x=True, to_y=True):
        """Dashed teal guide lines from a point to the axes, with labels."""
        if to_y:
            self.line(self.X0, y, x, y, TEAL, 1.5, "5 4", "butt")
            if ylabel:
                self.text(self.X0 - 8, y + 4, ylabel, 11.5, "end")
        if to_x:
            self.line(x, y, x, self.Y0, TEAL, 1.5, "5 4", "butt")
            if xlabel:
                self.text(x, self.Y0 + 18, xlabel, 11.5, "middle")

    def curve(self, pts, color=RED, width=2.8):
        """Smooth curve through pts via Catmull-Rom -> cubic Bezier."""
        d = f"M{pts[0][0]:.1f},{pts[0][1]:.1f}"
        for i in range(len(pts) - 1):
            p0 = pts[i - 1] if i > 0 else pts[i]
            p1, p2 = pts[i], pts[i + 1]
            p3 = pts[i + 2] if i + 2 < len(pts) else p2
            c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
            c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
            d += (f" C{c1[0]:.1f},{c1[1]:.1f} {c2[0]:.1f},{c2[1]:.1f} "
                  f"{p2[0]:.1f},{p2[1]:.1f}")
        self.path(d, color, width)

    def label(self, x, y, s, color=INK, size=12, anchor="start"):
        self.text(x, y, s, size, anchor, color)

    # ---------- output ----------
    def svg(self, title, desc):
        body = "\n  ".join(self.parts)
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" '
            f'role="img" aria-label="{esc(title)}" font-family="{FONT}">\n'
            f"  <title>{esc(title)}</title><desc>{esc(desc)}</desc>\n"
            f'  <rect width="{self.w}" height="{self.h}" fill="#ffffff"/>\n'
            f"  {body}\n</svg>\n"
        )


def sub(base, n):
    """Label with a subscript, e.g. sub('P', 1) -> P<sub>1</sub> as tspan."""
    return f'{base}<tspan font-size="70%" dy="3">{n}</tspan>'
