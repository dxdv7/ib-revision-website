"""Original vector redraws for chapters 10-12 (costs, perfect and monopolistic
competition, monopoly and oligopoly).

Everything is computed: cost curves come from a cubic total-cost function, so MC
passes exactly through the minima of AVC and ATC; all intersections are found
numerically (bisection) and every dot is asserted to lie on the curves it marks.
Built on tools/figlib.py (not modified).
"""
import os, sys, re, json, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import *

OUT = "/Users/davidbukraba/Desktop/IB WEBSITE/assets/figures-original"

ORANGE = "#e08a1e"
GREEN = "#2f8f5b"
BLUE = "#2f5fb0"
MAGENTA = "#8e3b9e"
PROFIT = "#cfeff2"
LOSS = "#f7d6d1"
DWL_DARK = "#a9d8ee"
DWL_PALE = "#d9eef8"
LIGHT = "#f1f1f1"
INKSOFT = "#555555"

XM, YM = 10.5, 105   # standard data ranges for single-panel firm diagrams


# ------------------------------------------------------------------ numerics
def bisect(g, lo, hi, it=80):
    glo = g(lo)
    for _ in range(it):
        mid = 0.5 * (lo + hi)
        gm = g(mid)
        if (gm > 0) == (glo > 0):
            lo, glo = mid, gm
        else:
            hi = mid
    return 0.5 * (lo + hi)


def crosses(f, g, lo, hi, n=4000):
    """All crossings of f and g on [lo,hi] -> list of (q, y)."""
    out = []
    h = lambda x: f(x) - g(x)
    xs = [lo + (hi - lo) * i / n for i in range(n + 1)]
    for a, b in zip(xs[:-1], xs[1:]):
        ha, hb = h(a), h(b)
        if ha == 0:
            out.append(a)
        elif ha * hb < 0:
            out.append(bisect(h, a, b))
    res = []
    for q in out:
        y = f(q)
        assert abs(g(q) - y) < 1e-6, "crossing not on both curves"
        res.append((q, y))
    return res


def cross1(f, g, lo, hi, which=0):
    r = crosses(f, g, lo, hi)
    assert len(r) > which, "no crossing found"
    return r[which]


def argmin(fn, lo, hi):
    for _ in range(200):
        a = lo + (hi - lo) / 3
        b = hi - (hi - lo) / 3
        if fn(a) < fn(b):
            hi = b
        else:
            lo = a
    q = 0.5 * (lo + hi)
    return q, fn(q)


class Cost:
    """TC = F + a q - b q^2 + c q^3.  MC is its derivative, so MC cuts ATC and AVC
    exactly at their minima (by construction; verified numerically)."""

    def __init__(self, F=98.0, a=60.0, b=12.0, c=1.0):
        self.F, self.a, self.b, self.c = F, a, b, c

    def tvc(self, q): return self.a * q - self.b * q * q + self.c * q ** 3
    def tc(self, q): return self.F + self.tvc(q)
    def mc(self, q): return self.a - 2 * self.b * q + 3 * self.c * q * q
    def avc(self, q): return self.a - self.b * q + self.c * q * q
    def afc(self, q): return self.F / q
    def atc(self, q): return self.F / q + self.avc(q)

    def with_F(self, F): return Cost(F, self.a, self.b, self.c)

    def min_atc(self):
        q, y = argmin(self.atc, 0.5, 20)
        assert abs(self.mc(q) - y) < 1e-4, "MC must pass through min ATC"
        return q, self.atc(q)

    def min_avc(self):
        q, y = argmin(self.avc, 0.0, 20)
        assert abs(self.mc(q) - y) < 1e-4, "MC must pass through min AVC"
        return q, self.avc(q)


C0 = Cost(F=98)          # ATC min at q = 7, ATC = 39; AVC min at q = 6, AVC = 24; MC min at q = 4, MC = 12


def dem(A, B):
    """Linear demand/AR = A - B q and its MR = A - 2 B q."""
    return (lambda q: A - B * q), (lambda q: A - 2 * B * q)


def tangent_demand(cost, qt):
    """AR line tangent to ATC at qt (so MR = MC at qt automatically)."""
    P_ = cost.atc(qt)
    h = 1e-5
    s = (cost.atc(qt + h) - cost.atc(qt - h)) / (2 * h)
    ar = lambda q: P_ + s * (q - qt)
    mr = lambda q: ar(q) + s * q
    assert abs(mr(qt) - cost.mc(qt)) < 1e-4
    return ar, mr, P_, s


# ------------------------------------------------------------------ canvas
def vis_len(s):
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"&#?\w+;", "x", s)
    return len(s)


class Cv:
    def __init__(self, name, w=420, h=380):
        self.name, self.w, self.h = name, w, h
        self.fig = Fig(w, h)
        self.parts = self.fig.parts
        self.boxes = []

    def T(self, x, y, s, size=12, anchor="start", color=INK, weight="400",
          rotate=None, italic=False, chk=True):
        self.fig.text(x, y, s, size, anchor, color, weight, rotate, italic)
        if rotate is None and chk:
            w = vis_len(s) * size * 0.54
            if anchor == "middle":
                x0, x1 = x - w / 2, x + w / 2
            elif anchor == "end":
                x0, x1 = x - w, x
            else:
                x0, x1 = x, x + w
            self.boxes.append((x0, y - size * 0.78, x1, y + size * 0.22, s))
            if x0 < 1 or x1 > self.w - 1 or y - size * 0.78 < 0 or y + size * 0.22 > self.h:
                print(f"  [{self.name}] text out of canvas: {s!r} {x0:.0f},{x1:.0f},{y:.0f}")

    def check(self):
        b = self.boxes
        for i in range(len(b)):
            for j in range(i + 1, len(b)):
                a, c = b[i], b[j]
                if a[0] < c[2] - 1 and c[0] < a[2] - 1 and a[1] < c[3] - 1 and c[1] < a[3] - 1:
                    print(f"  [{self.name}] TEXT OVERLAP: {a[4]!r} / {c[4]!r}")


class P(Fig):
    """A plot panel that shares its canvas parts and has a data scale."""

    def __init__(self, cv, x0=78, y0=318, x1=384, y1=30):
        super().__init__(cv.w, cv.h, x0, y0, x1, y1)
        self.parts = cv.parts
        self.cv = cv
        self._ymin = 0.0

    def scale(self, xmax, ymax, ymin=0.0, xpad=22, ypad=20):
        self._sx = (self.X1 - self.X0 - xpad) / xmax
        self._sy = (self.Y0 - self.Y1 - ypad) / (ymax - ymin)
        self._ymin = ymin
        self.xmax, self.ymax = xmax, ymax
        return self

    def py(self, v):
        return self.Y0 - (v - self._ymin) * self._sy

    def T(self, *a, **k):
        self.cv.T(*a, **k)

    def axis_y(self):
        return self.py(0) if self._ymin < 0 else self.Y0

    def xtick(self, x, label):
        self.T(x, self.axis_y() + 18, label, 11, "middle")

    def ytick(self, y, label):
        self.T(self.X0 - 8, y + 4, label, 11, "end")

    def axes2(self, xl, yl, ylx=None, xly=None, origin="0", title=None):
        ay = self.axis_y()
        self.line(self.X0, ay, self.X1, ay, INK, 2.2)
        self.line(self.X0, self.Y0, self.X0, self.Y1, INK, 2.2)
        self.arrowhead(self.X1 + 5, ay, 0, INK, 9)
        self.arrowhead(self.X0, self.Y1 - 5, -90, INK, 9)
        if origin:
            self.T(self.X0 - 12, ay + 16, origin, 12, "end")
        if xl:
            self.T((self.X0 + self.X1) / 2, xly if xly else self.cv.h - 14, xl, 12.5, "middle")
        if yl:
            self.T(ylx if ylx else 20, (self.Y0 + self.Y1) / 2, yl, 12.5, "middle", rotate=-90)
        if title:
            self.T((self.X0 + self.X1) / 2, 18, title, 13.5, "middle", INK, "600")

    # ---- drawing in data coordinates
    def plot(self, fn, lo, hi, color=RED, width=2.8, ymin=0.0, ymax=None, dash=None,
             linear=False, n=220):
        ymax = self.ymax if ymax is None else ymax
        valid = lambda x: ymin - 1e-9 <= fn(x) <= ymax + 1e-9
        N = 1500
        xs = [lo + (hi - lo) * i / N for i in range(N + 1)]
        idx = [i for i, x in enumerate(xs) if valid(x)]
        if not idx:
            raise ValueError("curve completely outside plot")
        i0, i1 = idx[0], idx[-1]
        a, b = xs[i0], xs[i1]

        def refine(bad, good):
            for _ in range(60):
                m = 0.5 * (bad + good)
                if valid(m):
                    good = m
                else:
                    bad = m
            return good

        if i0 > 0:
            a = refine(xs[i0 - 1], xs[i0])
        if i1 < N:
            b = refine(xs[i1 + 1], xs[i1])
        m = 2 if linear else n
        pts = [(self.px(a + (b - a) * i / (m - 1)), self.py(fn(a + (b - a) * i / (m - 1))))
               for i in range(m)]
        d = "M" + " L".join(f"{x:.2f},{y:.2f}" for x, y in pts)
        self.path(d, color, width, dash=dash)
        return a, b

    def shade(self, top, bot, a, b, fill, n=80):
        """Fill between two functions of q on [a,b] (top above bot)."""
        xs = [a + (b - a) * i / (n - 1) for i in range(n)]
        up = [(self.px(x), self.py(top(x))) for x in xs]
        dn = [(self.px(x), self.py(bot(x))) for x in reversed(xs)]
        d = "M" + " L".join(f"{x:.2f},{y:.2f}" for x, y in up + dn) + " Z"
        self.path(d, "none", 0, fill=fill)

    def rect(self, q0, q1, y0, y1, fill):
        x0, x1 = self.px(q0), self.px(q1)
        ya, yb = self.py(y0), self.py(y1)
        self.path(f"M{x0:.2f},{ya:.2f} L{x1:.2f},{ya:.2f} L{x1:.2f},{yb:.2f} L{x0:.2f},{yb:.2f} Z",
                  "none", 0, fill=fill)

    def dpt(self, q, y, *fns, r=3.6, color=INK):
        """Dot at data point; asserts it lies on every function passed in."""
        for f in fns:
            assert abs(f(q) - y) < 1e-6, f"dot ({q:.4f},{y:.4f}) is not on curve (f={f(q):.4f})"
        self.dot(self.px(q), self.py(y), r, color)

    def lab(self, q, y, s, color=INK, dx=6, dy=4, anchor="start", size=12.5, weight="400"):
        self.T(self.px(q) + dx, self.py(y) + dy, s, size, anchor, color, weight)

    def guide2(self, q, y, xl=None, yl=None, to_x=True, to_y=True, xrow=0, xdx=0, ydy=0):
        """Dashed teal guide from data point to the axes, with optional labels."""
        x, yy = self.px(q), self.py(y)
        ay = self.axis_y()
        if to_y:
            self.line(self.X0, yy, x, yy, TEAL, 1.5, "5 4", "butt")
            if yl:
                self.T(self.X0 - 8, yy + 4 + ydy, yl, 11.5, "end")
        if to_x:
            self.line(x, yy, x, ay, TEAL, 1.5, "5 4", "butt")
            if xl:
                self.T(x + xdx, ay + 18 + 14 * xrow, xl, 11.5, "middle")

    def hline(self, y, q0, q1, color=TEAL, width=1.5, dash="5 4"):
        self.line(self.px(q0), self.py(y), self.px(q1), self.py(y), color, width, dash, "butt")

    def vline(self, q, y0, y1, color=TEAL, width=1.5, dash="5 4"):
        self.line(self.px(q), self.py(y0), self.px(q), self.py(y1), color, width, dash, "butt")

    def pline(self, fn):
        """Pixel-space line ((x,y),(x,y)) of a linear data function, for Fig.hshift/vshift."""
        return ((self.px(0), self.py(fn(0))), (self.px(1), self.py(fn(1))))


def sq(base, n):
    return sub(base, n)


def emit(cv, fid, label, alt, caption):
    cv.check()
    plain = re.sub(r"<[^>]+>", "", label).replace("&ndash;", "-").replace("&rsquo;", "'")
    svg = cv.fig.svg(plain, alt)
    assert svg.isascii(), fid + " svg not ascii"
    assert alt.isascii() and caption.isascii() and label.isascii(), fid + " json not ascii"
    os.makedirs(OUT, exist_ok=True)
    with open(f"{OUT}/{fid}.svg", "w") as fh:
        fh.write(svg)
    with open(f"{OUT}/{fid}.json", "w") as fh:
        json.dump({"label": label, "alt": alt, "caption": caption}, fh, indent=2)
        fh.write("\n")
    print("ok", fid)


# ---- reusable cost/revenue drawing helpers --------------------------------
def firm_panel(cv, x0=78, x1=384, y0=318, y1=30, xm=XM, ym=YM, xl="Output (units)",
               yl="Price/Cost ($)", ylx=None, title=None, xly=None):
    p = P(cv, x0, y0, x1, y1).scale(xm, ym)
    p.axes2(xl, yl, ylx=ylx, title=title, xly=xly)
    return p


def draw_mc(p, C, label="MC", lo=0.0, hi=20.0, color=RED, dx=6, dy=4, anchor="start"):
    a, b = p.plot(C.mc, lo, hi, color)
    if label:
        p.lab(b, C.mc(b), label, color, dx, dy, anchor)
    return a, b


def draw_atc(p, C, label="ATC", color=ORANGE, hi=None, dx=5, dy=-6, anchor="start", lo=0.4,
             lab_q=None):
    hi = p.xmax if hi is None else hi
    a, b = p.plot(C.atc, lo, hi, color)
    if label:
        q = b if lab_q is None else lab_q
        p.lab(q, C.atc(q), label, color, dx, dy, anchor)
    return a, b


def draw_ar_mr(p, A, B, ar_label="D = AR", mr_label="MR", ar_dy=4, ar_anchor="start",
               ar_dx=6):
    ar, mr = dem(A, B)
    a, b = p.plot(ar, 0, p.xmax, GREY, linear=True)
    if ar_label:
        p.lab(b, ar(b), ar_label, GREY, ar_dx, ar_dy, ar_anchor)
    q0 = A / (2 * B)
    p.plot(mr, 0, q0, BLUE, linear=True)
    if mr_label:
        p.lab(q0, 0, mr_label, BLUE, 6, -6)
    return ar, mr


def profit_rect_label(p, q0, q1, y0, y1, lines, size=10.5, color=INKSOFT):
    """Centre small label lines inside a data rectangle."""
    xc = p.px((q0 + q1) / 2)
    yc = p.py((y0 + y1) / 2)
    n = len(lines)
    for i, s in enumerate(lines):
        p.T(xc, yc + 4 + (i - (n - 1) / 2) * (size + 2), s, size, "middle", color, "600")


# =============================================================== CHAPTER 12
# Monopoly and oligopoly. Ch10/11 figures were already produced by an earlier
# run of this scaffold; only chapter 12 was missing, so only its fig_12_*
# functions are added here (numbers verified numerically: intersections via
# cross1()/crosses(), the min-ATC/min-AVC points via Cost.min_atc()/min_avc()).

# ---- 12.1
def fig_12_1():
    cv = Cv("12.1")
    p = firm_panel(cv, xm=65, ym=140, xl="Quantity demanded (000s per month)",
                    yl="Price ($)")

    def lrac(q): return 900.0 / (q + 2) + 8.0
    def mc(q): return 15.0 + 0.15 * q
    def ar1(q): return 120.0 - 1.7 * q
    def ar2(q): return 55.0 - 1.7 * q

    p.plot(lrac, 0.05, 65, ORANGE, 2.8)
    p.lab(65, lrac(65), "LRAC", ORANGE, -4, -8, "end")
    p.plot(mc, 0, 65, RED, 2.2, linear=True)
    p.lab(8, mc(8), "MC", RED, 6, -8)
    p.plot(ar1, 0, 65, GREY, 2.6, linear=True)
    p.lab(10, ar1(10), "D" + sub("", 1) + " &amp; AR" + sub("", 1), GREY, 5, -6, size=11.5)
    p.plot(ar2, 0, 32.3, GREY, 2.0, dash="6 4", linear=True)
    p.lab(5, ar2(5), "D" + sub("", 2) + " &amp; AR" + sub("", 2), GREY, 5, -6, size=11.5)

    q1, y1 = cross1(ar1, lrac, 0.05, 30)
    q2, y2 = cross1(ar1, lrac, 30, 65)
    p.dpt(q1, y1, ar1, lrac)
    p.dpt(q2, y2, ar1, lrac)
    p.guide2(q1, y1, xl="q" + sub("", 1), yl="p")
    p.guide2(q2, y2, xl="q" + sub("", 2), yl=None, to_y=False)
    p.T(p.px((q1 + q2) / 2), p.py((y1 + y2) / 2) - 34,
        "Range of output over which", 11, "middle", INKSOFT, "600")
    p.T(p.px((q1 + q2) / 2), p.py((y1 + y2) / 2) - 20,
        "one firm can profitably supply", 11, "middle", INKSOFT, "600")
    p.T(p.px((q1 + q2) / 2), p.py((y1 + y2) / 2) - 6,
        "the whole market", 11, "middle", INKSOFT, "600")
    cv.check()
    emit(cv, "fig-12-1", "Figure 12.1: A natural monopoly",
         "A steeply declining LRAC curve for a piped-water network, with the full-market demand curve D1 and AR1 lying above LRAC between q1 and q2, while the halved demand curve D2 and AR2 that each of two firms would face lies below LRAC everywhere.",
         "The long-run average cost curve LRAC for a piped-water network declines steeply as fixed network costs are spread over more customers &mdash; a classic natural monopoly. A single firm facing the whole market&rsquo;s demand, D<sub>1</sub> &amp; AR<sub>1</sub>, can earn abnormal profit at any output between q<sub>1</sub> and q<sub>2</sub>, since AR<sub>1</sub> lies above LRAC across that range. If a second firm entered and industry demand were split in two, each firm would face the smaller D<sub>2</sub> &amp; AR<sub>2</sub> curve, which lies below LRAC at every output &mdash; neither could even cover its costs. The market can profitably support only one supplier.")


# ---- 12.2
def fig_12_2():
    cv = Cv("12.2")
    p = firm_panel(cv, xm=11, ym=110)
    ar, mr = dem(95, 6.5)
    _, be = p.plot(ar, 0, 11, GREY, 2.6, linear=True)
    p.lab(be, ar(be), "D = AR", GREY, 4, 4)
    q0 = 95 / 13
    p.plot(mr, 0, q0, BLUE, 2.2, linear=True)
    p.lab(q0, 0, "MR", BLUE, 4, -6)
    draw_mc(p, C0, "MC", hi=11)
    q1, y1 = cross1(mr, C0.mc, 0.1, 11)
    p.dpt(q1, y1, mr, C0.mc)
    p.dpt(q1, ar(q1), ar)
    p.guide2(q1, ar(q1), xl="q", yl="P")
    cv.check()
    emit(cv, "fig-12-2", "Figure 12.2: The demand curve facing a monopolist",
         "A monopolist's downward-sloping D=AR curve with a steeper MR curve below it and an upward-sloping MC curve, selling quantity q at price P where MC=MR.",
         "The monopolist faces the whole market&rsquo;s downward-sloping demand curve, D = AR, with a steeper MR curve below it. It maximizes profit by producing where MC = MR, at output q, and charges the price P read up from q to the demand curve. Because the firm controls the entire industry&rsquo;s output, it can restrict quantity below what a price taker would supply in order to raise price &mdash; this is the essence of monopoly power.")


# ---- 12.3
def fig_12_3():
    cv = Cv("12.3")
    p = firm_panel(cv)
    ar, mr = dem(125, 9)
    _, be = p.plot(ar, 0, p.xmax, GREY, 2.6, linear=True)
    p.lab(be, ar(be), "D = AR", GREY, 4, 4)
    q0 = 125 / 18
    p.plot(mr, 0, q0, BLUE, 2.2, linear=True)
    p.lab(q0, 0, "MR", BLUE, 4, -6)
    draw_mc(p, C0)
    draw_atc(p, C0, "AC")
    q, _ = cross1(mr, C0.mc, 0.1, p.xmax)
    Pp, Cc = ar(q), C0.atc(q)
    p.rect(0, q, Cc, Pp, PROFIT)
    p.dpt(q, Pp, ar)
    p.dpt(q, Cc, C0.atc)
    p.guide2(q, Pp, xl="q", yl="P")
    p.hline(Cc, 0, q)
    p.ytick(p.py(Cc), "C")
    profit_rect_label(p, 0, q, Cc, Pp, ["Abnormal", "profit"])
    cv.check()
    emit(cv, "fig-12-3", "Figure 12.3: Abnormal profits in the long run in monopoly",
         "A monopolist producing at output q where MC=MR, with price P above average cost C, earning the shaded abnormal profit rectangle.",
         "The monopolist maximizes profit at output q, where MC = MR. At that output price is P (read off AR) while average cost is only C (read off AC). Since P &gt; C, the firm earns abnormal profit of (P &minus; C) per unit, shown as the shaded rectangle. Because barriers to entry keep new firms out, this profit can persist indefinitely into the long run &mdash; unlike in perfect competition.")


# ---- 12.4
def fig_12_4():
    cv = Cv("12.4")
    Chi = C0.with_F(180)
    p = firm_panel(cv, xm=12, ym=110)
    ar, mr = dem(70, 7)
    _, be = p.plot(ar, 0, p.xmax, GREY, 2.6, linear=True)
    p.lab(be, ar(be), "D = AR", GREY, 4, 4)
    q0 = 70 / 14
    p.plot(mr, 0, q0, BLUE, 2.2, linear=True)
    p.lab(q0, 0, "MR", BLUE, 4, -6)
    draw_mc(p, Chi, hi=12)
    draw_atc(p, Chi, "AC", hi=12, lo=1.2)
    q, _ = cross1(mr, Chi.mc, 0.1, p.xmax)
    Pp, Cc = ar(q), Chi.atc(q)
    p.rect(0, q, Pp, Cc, LOSS)
    p.dpt(q, Pp, ar)
    p.dpt(q, Cc, Chi.atc)
    p.guide2(q, Cc, xl="q", yl="C")
    p.hline(Pp, 0, q)
    p.ytick(p.py(Pp), "P")
    profit_rect_label(p, 0, q, Pp, Cc, ["Losses"])
    cv.check()
    emit(cv, "fig-12-4", "Figure 12.4: A monopolist making losses in the long run",
         "A monopolist producing at output q where MC=MR, with average cost C above price P, giving a shaded losses rectangle.",
         "The profit-maximizing (here, loss-minimizing) output is q, where MC = MR, but the AC curve lies above the AR curve at every output the firm could choose. At q, average cost C exceeds price P, so the firm makes a loss of (C &minus; P) per unit, shown as the shaded rectangle. Since there is no output at which the firm can cover its average costs, it will not produce at all in the long run.")


# ---- 12.5
def fig_12_5():
    cv = Cv("12.5")
    p = firm_panel(cv, xm=11, ym=140)
    ar, mr = dem(220, 20)
    _, be = p.plot(ar, 0, p.xmax, GREY, 2.6, linear=True)
    p.lab(be, ar(be), "D = AR", GREY, 4, 4)
    q0 = 220 / 40
    p.plot(mr, 0, q0, BLUE, 2.2, linear=True)
    p.lab(q0, 0, "MR", BLUE, 4, -6)
    draw_mc(p, C0)
    draw_atc(p, C0, "AC")
    q1, _ = cross1(mr, C0.mc, 0.1, p.xmax)
    qa, ya = cross1(ar, C0.mc, 0.1, p.xmax)
    qp, cp = C0.min_atc()
    Pp, Cc = ar(q1), C0.atc(q1)
    p.rect(0, q1, Cc, Pp, PROFIT)
    p.dpt(q1, Pp, ar)
    p.dpt(q1, Cc, C0.atc)
    p.dpt(qa, ya, ar, C0.mc)
    p.dpt(qp, cp, C0.atc, C0.mc)
    p.guide2(q1, Pp, xl="q" + sub("", 1), yl="P", xrow=0)
    p.vline(qa, 0, ya)
    p.xtick(p.px(qa), "q" + sub("", 2))
    p.vline(qp, 0, cp)
    p.T(p.px(qp) - 3, p.axis_y() + 32, "q" + sub("", 3), 11.5, "middle")
    profit_rect_label(p, 0, q1, Cc, Pp, ["Abnormal", "profit"])
    p.T(p.X0 + 6, 46, "q" + sub("", 2) + " = allocative (MC=AR)", 10, "start", INKSOFT)
    p.T(p.X0 + 6, 60, "q" + sub("", 3) + " = productive (min AC)", 10, "start", INKSOFT)
    cv.check()
    emit(cv, "fig-12-5", "Figure 12.5: Productive and allocative efficiency in monopoly",
         "The monopolist's profit-maximizing output q1 (MC=MR) restricted below both the allocatively efficient output q2 (where D=AR meets MC) and the productively efficient output q3 (minimum of AC).",
         "The monopolist produces at the profit-maximizing output q<sub>1</sub> (MC = MR), earning the shaded abnormal profit rectangle. This output is restricted below both the allocatively efficient output q<sub>2</sub> (where D = AR meets MC, so P = MC) and the productively efficient output q<sub>3</sub> (the minimum point of AC). Because q<sub>1</sub> is less than either, output is restricted purely to raise price and maximize profit &mdash; neither productive nor allocative efficiency is achieved.")


# ---- 12.6
def fig_12_6():
    cv = Cv("12.6")
    p = firm_panel(cv, x0=78, x1=390, xm=52, ym=160, xl="Output (units)", yl="Price ($)")
    ar = lambda q: 150 - 1.5 * q
    mr = lambda q: 150 - 3 * q
    pcS = lambda q: 20 + 3 * q
    mcm = lambda q: 15 + 0.3 * q
    _, be = p.plot(ar, 0, p.xmax, GREY, 2.6, linear=True)
    p.lab(be, ar(be), "D = AR", GREY, 4, 4)
    q0 = 50
    p.plot(mr, 0, q0, MAGENTA, 2.0, linear=True)
    p.lab(q0, mr(q0), "MR", MAGENTA, 4, 4)
    _, bs = p.plot(pcS, 0, p.xmax, RED, 2.6, linear=True)
    p.lab(bs, pcS(bs), "Industry supply:", RED, -84, -10, "start", 11)
    p.lab(bs, pcS(bs), "perfect competition", RED, -84, 4, "start", 11)
    _, bm = p.plot(mcm, 0, p.xmax, BLUE, 2.6, linear=True)
    p.lab(bm, mcm(bm), "MC: monopoly", BLUE, -78, 16, "start", 11)
    q1, p1 = cross1(ar, pcS, 0.1, p.xmax)
    q2, mv = cross1(mr, mcm, 0.1, p.xmax)
    p2 = ar(q2)
    p.dpt(q1, p1, ar, pcS)
    p.dpt(q2, mv, mr, mcm)
    p.dpt(q2, p2, ar)
    p.guide2(q1, p1, xl="Q" + sub("", 1), yl="P" + sub("", 1))
    p.guide2(q2, p2, xl="Q" + sub("", 2), yl="P" + sub("", 2), xrow=1)
    cv.check()
    emit(cv, "fig-12-6", "Figure 12.6: Economies of scale in monopoly",
         "Comparing a perfect-competition industry supply curve with a monopolist's lower MC curve from economies of scale, showing the monopolist producing a greater output Q2 at a lower price P2 than perfect competition's Q1, P1.",
         "The red industry supply curve shows what a perfectly competitive industry of many small firms would supply; the blue MC curve shows the monopolist&rsquo;s much lower unit costs once it can exploit economies of scale. Perfect competition would settle at price P<sub>1</sub> and quantity Q<sub>1</sub>, where supply meets demand. The monopolist instead produces where MC = MR, giving a <em>greater</em> output Q<sub>2</sub> at a <em>lower</em> price P<sub>2</sub>. When economies of scale are large enough, a monopoly can, in principle, out-perform a fragmented competitive industry on both price and output.")


# ---- 12.7
def fig_12_7():
    cv = Cv("12.7")
    p = firm_panel(cv, xm=34, ym=160, xl="Output (units)", yl="Price ($)")
    ar = lambda q: 150 - 1.5 * q
    mr = lambda q: 150 - 3 * q
    mc = lambda q: 20 + 3 * q
    _, be = p.plot(ar, 0, p.xmax, GREY, 2.6, linear=True)
    p.lab(be, ar(be), "D = AR", GREY, 4, 4)
    q0 = 25
    p.plot(mr, 0, q0, BLUE, 2.0, linear=True)
    p.lab(q0, mr(q0), "MR", BLUE, 4, 4)
    _, bm = p.plot(mc, 0, p.xmax, RED, 2.6, linear=True)
    p.lab(bm, mc(bm), "MC (= supply under", RED, -118, -8, "start", 11)
    p.lab(bm, mc(bm), "perfect competition)", RED, -118, 6, "start", 11)
    q1, p1 = cross1(ar, mc, 0.1, p.xmax)
    q2, mv = cross1(mr, mc, 0.1, p.xmax)
    p2 = ar(q2)
    p.dpt(q1, p1, ar, mc)
    p.dpt(q2, mv, mr, mc)
    p.dpt(q2, p2, ar)
    p.guide2(q1, p1, xl="Q" + sub("", 1), yl="P" + sub("", 1))
    p.guide2(q2, p2, xl="Q" + sub("", 2), yl="P" + sub("", 2), xrow=1)
    cv.check()
    emit(cv, "fig-12-7", "Figure 12.7: Monopoly versus perfect competition without economies of scale",
         "A single MC curve shared by perfect competition and monopoly, with perfect competition at price P1, output Q1, versus the profit-maximizing monopolist restricting output to Q2 and charging the higher price P2.",
         "Here monopoly and perfect competition share the identical cost curve, MC. Under perfect competition, equilibrium is where MC (= industry supply) meets D = AR, giving price P<sub>1</sub> and output Q<sub>1</sub>. The profit-maximizing monopolist instead produces where MC = MR, restricting output to the smaller Q<sub>2</sub> and charging the higher price P<sub>2</sub>. Without a cost advantage, monopoly produces less and charges more than perfect competition would for the identical cost structure.")


# ---- 12.8
def fig_12_8():
    cv = Cv("12.8", w=460, h=260)
    f = cv.fig
    x0, x1, y0 = 40, 420, 130
    bh = 34
    marks = [0, 40, 85, 100]
    zones = [
        (0, 40, "#d9ecd5", "Monopolistic competition"),
        (40, 85, "#f5e2b8", "Oligopoly"),
        (85, 100, "#f3c7c0", "Monopoly"),
    ]

    def px(v): return x0 + (x1 - x0) * v / 100.0

    for a, b, fill, _ in zones:
        f.add(f'<rect x="{px(a):.1f}" y="{y0:.1f}" width="{px(b)-px(a):.1f}" height="{bh}" '
              f'fill="{fill}" stroke="#ffffff" stroke-width="1.5"/>')
    f.add(f'<rect x="{x0}" y="{y0}" width="{x1-x0}" height="{bh}" fill="none" stroke="{INK}" stroke-width="1.6"/>')
    for m in marks:
        f.line(px(m), y0, px(m), y0 + bh, INK, 1.4)
        cv.T(px(m), y0 + bh + 18, f"{m}%", 11, "middle")
    cv.T((x0 + x1) / 2, y0 + bh + 40, "Market share of the largest 4 firms (CR" + sub("", 4) + ")", 12, "middle")
    # structure labels above
    cv.T(px(0), y0 - 34, "Perfect", 11.5, "middle", INK, "600")
    cv.T(px(0), y0 - 20, "competition", 11.5, "middle", INK, "600")
    cv.T(px(20), y0 - 12, "Monopolistic", 11.5, "middle", INK, "600")
    cv.T(px(20), y0 + 2, "competition", 11.5, "middle", INK, "600")
    cv.T(px(62.5), y0 - 20, "Oligopoly", 12, "middle", INK, "600")
    cv.T(px(100), y0 - 34, "Monopoly", 11.5, "middle", INK, "600")
    f.dot(px(0), y0 + bh / 2, 4.4, INK)
    f.dot(px(100), y0 + bh / 2, 4.4, INK)
    # concentration bands below
    cv.T(px(20), y0 + bh + 60, "Low concentration", 10.5, "middle", INKSOFT, italic=True)
    cv.T(px(62.5), y0 + bh + 60, "Medium concentration", 10.5, "middle", INKSOFT, italic=True)
    cv.T(px(92.5), y0 + bh + 60, "High concentration", 10.5, "middle", INKSOFT, italic=True)
    f.text(230, 30, "The market-structure spectrum", 15, "middle", INK, "600")
    cv.check()
    emit(cv, "fig-12-8", "Figure 12.8: CR4 ratios in different market structures",
         "Horizontal spectrum from 0% to 100% market share of the largest four firms (CR4), running from perfect competition at 0% through monopolistic competition and oligopoly to monopoly at 100%.",
         "The four textbook market structures are really points on a single spectrum of seller concentration, measured here by the CR<sub>4</sub> ratio (the combined market share of the four largest firms). Perfect competition sits at the 0% end (low concentration), monopolistic competition occupies the low range up to around 40%, oligopoly spans roughly 40&ndash;85% (medium to high concentration), and monopoly sits at the 100% end (a single seller, the highest possible concentration).")


# ---- 12.9
def fig_12_9():
    cv = Cv("12.9")
    p = firm_panel(cv)
    ar, mr = dem(130, 8)
    _, be = p.plot(ar, 0, p.xmax, GREY, 2.6, linear=True)
    p.lab(be, ar(be), "D = AR", GREY, 4, 4)
    q0 = 130 / 16
    p.plot(mr, 0, q0, BLUE, 2.2, linear=True)
    p.lab(q0, 0, "MR", BLUE, 4, -6)
    draw_mc(p, C0)
    draw_atc(p, C0, "AC")
    q, _ = cross1(mr, C0.mc, 0.1, p.xmax)
    Pp, Cc = ar(q), C0.atc(q)
    p.rect(0, q, Cc, Pp, PROFIT)
    p.dpt(q, Pp, ar)
    p.dpt(q, Cc, C0.atc)
    p.guide2(q, Pp, xl="q", yl="p")
    p.hline(Cc, 0, q)
    p.T(p.X0 - 8, p.py(Cc) + 4, "c", 11.5, "end")
    profit_rect_label(p, 0, q, Cc, Pp, ["Abnormal", "(monopoly)", "profit"])
    cv.check()
    emit(cv, "fig-12-9", "Figure 12.9: Oligopolists acting as a monopolist",
         "A standard monopoly-style diagram showing colluding oligopolists jointly restricting output to q (MC=MR) and charging price p, earning the shaded abnormal (monopoly) profit rectangle.",
         "If a group of oligopolists collude, formally through a cartel or informally, they can act together exactly like a single monopolist. They jointly restrict output to q (where MC = MR) and charge price p, read off the AR curve. The shaded rectangle is the abnormal (monopoly) profit earned collectively, which the colluding firms then divide up according to their individual market shares.")


# ---- 12.10  (decision tree - own box/link helpers, no cost curves needed)
def box(cv, x, y, w, h, lines, fill="#fdeaea", stroke=RED, size=11.5, weight="600",
        color=INK, rx=8, sw=1.8):
    cv.fig.add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" '
               f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')
    if isinstance(lines, str):
        lines = [lines]
    lh = size * 1.3
    y0 = y + h / 2 - lh * (len(lines) - 1) / 2 + size * 0.35
    for i, s in enumerate(lines):
        cv.T(x + w / 2, y0 + i * lh, s, size, "middle", color, weight, chk=False)


def vlink(cv, x, y1, y2, color=INK, width=1.8):
    cv.fig.arrow(x, y1, x, y2 - 3, color, width, 7)


def fig_12_10():
    cv = Cv("12.10", w=760, h=430)
    f = cv.fig
    box(cv, 280, 14, 200, 34, "Decisions for Firm X", "#eef0fa", MAGENTA)
    box(cv, 90, 92, 200, 34, "If the worst happens", "#e6f5f7", TEAL)
    box(cv, 470, 92, 200, 34, "If the best happens", "#fdeaea", RED)
    vlink(cv, 190, 48, 92, INK)
    vlink(cv, 570, 48, 92, INK)
    # decision boxes
    box(cv, 30, 172, 150, 40, "Firm X maintains price", "#f6f6f6", GREY, size=10.5)
    box(cv, 200, 172, 150, 40, "Firm X lowers price", "#f6f6f6", GREY, size=10.5)
    box(cv, 410, 172, 150, 40, "Firm X maintains price", "#f6f6f6", GREY, size=10.5)
    box(cv, 580, 172, 150, 40, "Firm X lowers price", "#f6f6f6", GREY, size=10.5)
    vlink(cv, 105, 126, 172, INK)
    vlink(cv, 275, 126, 172, INK)
    vlink(cv, 485, 126, 172, INK)
    vlink(cv, 655, 126, 172, INK)
    cv.T(190, 254, "Firm Y lowers price (worst case for X)", 10.5, "middle", INKSOFT, italic=True)
    cv.T(570, 254, "Firm Y maintains price (best case for X)", 10.5, "middle", INKSOFT, italic=True)
    # outcome boxes
    box(cv, 30, 300, 150, 44, ["Profit", "$3M"], "#f6f6f6", GREY)
    box(cv, 200, 300, 150, 44, ["Profit", "$5M"], PROFIT, TEAL)
    box(cv, 410, 300, 150, 44, ["Profit", "$7M"], "#f6f6f6", GREY)
    box(cv, 580, 300, 150, 44, ["Profit", "$9M"], PROFIT, RED)
    vlink(cv, 105, 212, 300, INK)
    vlink(cv, 275, 212, 300, INK)
    vlink(cv, 485, 212, 300, INK)
    vlink(cv, 655, 212, 300, INK)
    f.add(f'<circle cx="275" cy="320" r="34" fill="none" stroke="{TEAL}" stroke-width="2.4"/>')
    f.add(f'<circle cx="655" cy="320" r="34" fill="none" stroke="{RED}" stroke-width="2.4"/>')
    cv.T(275, 374, "Best 'worst option'", 10.5, "middle", TEAL, "600", chk=False)
    cv.T(275, 388, "(minimax choice)", 10.5, "middle", TEAL, "600", chk=False)
    cv.T(655, 374, "Best 'best option'", 10.5, "middle", RED, "600", chk=False)
    cv.T(655, 388, "(maximax choice)", 10.5, "middle", RED, "600", chk=False)
    cv.T(380, 410, "Both approaches point to Firm X lowering its price as the rational choice.",
         11, "middle", INK, "600")
    cv.check()
    emit(cv, "fig-12-10", "Figure 12.10: Game theory outcomes for Firms X and Y",
         "Decision tree for Firm X showing worst-case outcomes (maintain price: $3M, lower price: $5M, the minimax choice) and best-case outcomes (maintain price: $7M, lower price: $9M, the maximax choice), with lowering price rational under both approaches.",
         "Firm X does not know how rival Firm Y will react, so it can reason two ways. Under the cautious minimax approach it compares the worst case of each option &mdash; if Firm Y always undercuts, maintaining price earns $3M but lowering price earns $5M, so $5M is the best of the worst outcomes. Under the optimistic maximax approach it compares the best case of each option &mdash; if Firm Y always matches, maintaining price earns $7M but lowering price earns $9M, so $9M is the best of the best outcomes. Either way, lowering price is Firm X&rsquo;s rational choice.")


# ---- 12.11
def fig_12_11():
    cv = Cv("12.11")
    p = firm_panel(cv, xm=11, ym=140)
    ar, mr = dem(200, 18)
    _, be = p.plot(ar, 0, p.xmax, GREY, 2.6, linear=True)
    p.lab(be, ar(be), "D = AR", GREY, 4, 4)
    q0 = 200 / 36
    p.plot(mr, 0, q0, BLUE, 2.2, linear=True)
    p.lab(q0, 0, "MR", BLUE, 4, -6)
    draw_mc(p, C0)
    draw_atc(p, C0, "AC")
    q1, _ = cross1(mr, C0.mc, 0.1, p.xmax)
    qa, ya = cross1(ar, C0.mc, 0.1, p.xmax)
    qp, cp = C0.min_atc()
    Pp, Cc = ar(q1), C0.atc(q1)
    p.rect(0, q1, Cc, Pp, PROFIT)
    p.dpt(q1, Pp, ar)
    p.dpt(q1, Cc, C0.atc)
    p.dpt(qa, ya, ar, C0.mc)
    p.dpt(qp, cp, C0.atc, C0.mc)
    p.guide2(q1, Pp, xl="q" + sub("", 1), yl="P")
    p.vline(qa, 0, ya)
    p.xtick(p.px(qa), "q" + sub("", "a"))
    p.vline(qp, 0, cp)
    p.T(p.px(qp) - 3, p.axis_y() + 32, "q" + sub("", "p"), 11.5, "middle")
    profit_rect_label(p, 0, q1, Cc, Pp, ["Abnormal", "profit"])
    p.T(p.X0 + 6, 46, "q" + sub("", "a") + " = allocative (MC=AR)", 10, "start", INKSOFT)
    p.T(p.X0 + 6, 60, "q" + sub("", "p") + " = productive (min AC)", 10, "start", INKSOFT)
    cv.check()
    emit(cv, "fig-12-11", "Figure 12.11: Productive and allocative efficiency in a collusive oligopoly",
         "A standard monopoly-style diagram showing colluding oligopolists producing profit-maximizing output q1 (MC=MR) with abnormal profit, below both the allocatively efficient output qa and the productively efficient output qp.",
         "With formal or tacit collusion and barriers to entry, oligopolists collectively behave like a monopolist: they produce the profit-maximizing output q<sub>1</sub> (MC = MR), earning the shaded abnormal profit, then split it according to market share. As in monopoly, neither the allocatively efficient output q<sub>a</sub> (where AR = MC) nor the productively efficient output q<sub>p</sub> (the minimum of AC) is reached &mdash; output is restricted below both purely to force up price.")


if __name__ == "__main__":
    which = sys.argv[1:]
    for name, fn in sorted(globals().items()):
        if name.startswith("fig_") and (not which or name[4:].replace("_", "-") in which):
            fn()
