"""Original vector figures for chapters 18-20 (supply-side policy, unemployment
and the labour market, inflation and the Phillips curve).

All figures are drawn from primitives with their own coordinates and own
examples.  Every equilibrium / intersection dot is either computed with
Fig.intersect() (straight lines) or is built so that the dot IS a control
point of both curves (curves are sampled from functions, and the crossing is
inserted as a sample so Fig.curve() passes exactly through it).
Built on tools/figlib.py (not modified).
"""
import os, sys, json, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import *

OUT = "/Users/davidbukraba/Desktop/IB WEBSITE/assets/figures-original"
os.makedirs(OUT, exist_ok=True)

MINUS = "&#8722;"
LIGHTRED = "#fdeaea"
DARK = "#444444"


def save(fid, fig, label, title, alt, caption):
    open(f"{OUT}/{fid}.svg", "w").write(fig.svg(title, alt))
    with open(f"{OUT}/{fid}.json", "w") as fh:
        json.dump({"label": label, "alt": alt, "caption": caption}, fh, indent=1)
    print("saved", fid)


# ------------------------------------------------------------ small helpers
def setp(f, x0, x1, y0=318, y1=50):
    f.X0, f.X1, f.Y0, f.Y1 = x0, x1, y0, y1


def axes2(f, xlabel, ylabel, title=None, origin="0"):
    f.line(f.X0, f.Y0, f.X1, f.Y0, INK, 2.2)
    f.line(f.X0, f.Y0, f.X0, f.Y1, INK, 2.2)
    f.arrowhead(f.X1 + 5, f.Y0, 0, INK, 9)
    f.arrowhead(f.X0, f.Y1 - 5, -90, INK, 9)
    if origin:
        f.text(f.X0 - 12, f.Y0 + 16, origin, 12, "end")
    f.text((f.X0 + f.X1) / 2, f.Y0 + 40, xlabel, 12.5, "middle")
    f.text(f.X0 - 58, (f.Y0 + f.Y1) / 2, ylabel, 12.5, "middle", rotate=-90)
    if title:
        f.text((f.X0 + f.X1) / 2, f.Y1 - 16, title, 13, "middle", INK, "600")


def ln(f, l, color=RED, w=2.8):
    f.line(l[0][0], l[0][1], l[1][0], l[1][1], color, w)


def lab(f, x, y, s, color=INK, size=12.5, anchor="start"):
    f.text(x, y, s, size, anchor, color)


def sb(base, n):
    return sub(base, n)


def on(line, p, tol=0.02):
    return abs(Fig.y_at(line, p[0]) - p[1]) < tol


def cross(f, l1, l2, xl=None, yl=None, to_x=True, to_y=True, dot=INK, guides=True):
    """Exact intersection with dot; asserts the dot is on both lines."""
    p = Fig.intersect(l1, l2)
    if abs(l1[0][0] - l1[1][0]) > 1e-9:
        assert on(l1, p), "dot not on line 1"
    else:
        assert abs(p[0] - l1[0][0]) < 1e-6
    if abs(l2[0][0] - l2[1][0]) > 1e-9:
        assert on(l2, p), "dot not on line 2"
    else:
        assert abs(p[0] - l2[0][0]) < 1e-6
    if guides:
        f.guide(p[0], p[1], xl, yl, to_x, to_y)
    if dot:
        f.dot(p[0], p[1], 3.6, dot)
    return p


def shifted(l, dx=0, dy=0):
    return ((l[0][0] + dx, l[0][1] + dy), (l[1][0] + dx, l[1][1] + dy))


def axis_arrow_x(f, x1, x2, dy=27):
    d = 10 if x2 > x1 else -10
    f.arrow(x1 + d, f.Y0 + dy, x2 - d, f.Y0 + dy, PURPLE, 1.8, 7)


def axis_arrow_y(f, y1, y2, dx=-38):
    d = 6 if y2 > y1 else -6
    f.arrow(f.X0 + dx, y1 + d, f.X0 + dx, y2 - d, PURPLE, 1.8, 7)


def bisect(g, lo, hi, it=100):
    glo = g(lo)
    for _ in range(it):
        mid = 0.5 * (lo + hi)
        gm = g(mid)
        if (gm > 0) == (glo > 0):
            lo, glo = mid, gm
        else:
            hi = mid
    return 0.5 * (lo + hi)


def xs_for(x0, x1, n, extra=()):
    step = (x1 - x0) / n
    base = [x0 + step * i for i in range(n + 1)]
    base = [b for b in base if all(abs(b - e) > 0.35 * step for e in extra)]
    return sorted(set(base) | set(extra))


def fcurve(f, fn, x0, x1, n, extra=(), color=RED, w=2.8, pxy=None):
    """Sample y=fn(x) (data units) and draw a smooth curve through the samples;
    'extra' x's are guaranteed to be control points (exactly on the path)."""
    pxy = pxy or f.pt
    pts = [pxy(x, fn(x)) for x in xs_for(x0, x1, n, extra)]
    f.curve(pts, color, w)
    return pts


# =============================================================== CHAPTER 18
def kink_path(xs, yflat, xv, ytop, rx=64, ry=58):
    """Keynesian-shaped AS: flat, smooth bend, then vertical at xv."""
    d = f"M{xs:.1f},{yflat:.1f} L{xv - rx:.1f},{yflat:.1f} "
    d += (f"C{xv - rx * 0.35:.1f},{yflat:.1f} {xv:.1f},{yflat - ry * 0.6:.1f} "
          f"{xv:.1f},{yflat - ry:.1f} L{xv:.1f},{ytop:.1f}")
    return d


def fig_18_1():
    f = Fig(w=860, h=380)
    # panel (a)
    setp(f, 78, 390)
    axes2(f, "Real output (Y)", "Average price level ($)", "(a)")
    yfl, ytop = 250, 92
    x1, x2 = 232, 306
    f.path(kink_path(88, yfl, x2, ytop), RED, 2.8)
    f.path(kink_path(88, yfl, x1, ytop), RED, 2.8)
    lab(f, x1, ytop - 10, "AS" + sb("", 1), RED, 12.5, "middle")
    lab(f, x2, ytop - 10, "AS" + sb("", 2), RED, 12.5, "middle")
    f.hshift(((x1, 110), (x1, 190)), ((x2, 110), (x2, 190)), 148)
    # panel (b)
    setp(f, 498, 810)
    axes2(f, "Real output (Y)", "Average price level ($)", "(b)")
    a, b = 640, 716
    top = 92
    L1 = ((a, f.Y0), (a, top)); L2 = ((b, f.Y0), (b, top))
    ln(f, L1); ln(f, L2)
    lab(f, a, top - 10, "LRAS" + sb("", 1), RED, 12.5, "middle")
    lab(f, b, top - 10, "LRAS" + sb("", 2), RED, 12.5, "middle")
    f.hshift(L1, L2, 190)
    return f


# =============================================================== CHAPTER 19
def fig_19_1():
    f = Fig(w=560, h=572)

    def head(y, s):
        f.text(24, y, s, 13, "start", INK, "700")

    def bullets(y, items, gap=20):
        for i, s in enumerate(items):
            yy = y + i * gap
            f.add(f'<circle cx="36" cy="{yy - 4:.1f}" r="3" fill="{RED}"/>')
            f.text(48, yy, s, 12.5, "start", INK)
        return y + len(items) * gap

    head(30, "Inflows: people becoming unemployed")
    y = bullets(54, ["Workers who are made redundant or dismissed",
                     "Workers who resign from their jobs",
                     "School and college leavers who have not yet found work",
                     "People re-entering the labour force (e.g. after caring for family)",
                     "Migrants who arrive and have not yet found work"])
    f.text(24, y + 2, "Each of these raises the level of unemployment.", 11.5, "start", GREY, italic=True)
    # big down arrows into the box
    for x in (200, 280, 360):
        f.arrow(x, 176, x, 214, RED, 7, 16)
    f.add(f'<rect x="150" y="218" width="260" height="56" rx="8" fill="{LIGHTRED}" '
          f'stroke="{RED}" stroke-width="2.2"/>')
    f.text(280, 252, "&#8220;Pool&#8221; of unemployment", 15, "middle", INK, "600")
    for x in (200, 280, 360):
        f.arrow(x, 278, x, 316, RED, 7, 16)
    head(342, "Outflows: people no longer counted as unemployed")
    y = bullets(366, ["People who find a job",
                      "People who retire",
                      "People who move into full-time education",
                      "People who leave the labour force to care for family",
                      "People who emigrate",
                      "Discouraged workers who give up looking for work",
                      "People who die"])
    f.text(24, y + 2, "Each of these lowers the level of unemployment.", 11.5, "start", GREY, italic=True)
    f.text(24, y + 26, "Only the first outflow is a true return to employment; the others leave the", 11.5, "start", INK)
    f.text(24, y + 42, "labour force, so those people are no longer &#8220;without work, available and", 11.5, "start", INK)
    f.text(24, y + 58, "actively seeking work&#8221;.", 11.5, "start", INK)
    return f


# ---- labour-market curves (data units: L = workers, W = wage index) ----------
def D_lab(L):
    return 13.6 + 1803.0 / (L + 15.0)


def S_lab(L):
    return 15.0 + 0.0125 * L * L


def lab_setup():
    f = Fig().scale(100, 100)
    f.axes("Number of workers", "Average (real) wage rate")
    return f


def inv_D(w):
    return 1803.0 / (w - 13.6) - 15.0


def fig_19_2():
    f = lab_setup()
    Le = bisect(lambda L: D_lab(L) - S_lab(L), 10, 90)
    We = D_lab(Le)
    assert abs(S_lab(Le) - We) < 1e-6
    fcurve(f, D_lab, 8, 95, 14, [Le], GREY)
    fcurve(f, S_lab, 24, 78, 12, [Le], RED)
    lab(f, f.px(95) + 5, f.py(D_lab(95)) + 4, "AD" + sb("", "L"), GREY, 12.5)
    lab(f, f.px(78) + 2, f.py(S_lab(78)) - 8, "AS" + sb("", "L"), RED, 12.5)
    f.guide(f.px(Le), f.py(We), sb("Q", "e"), sb("W", "e"))
    f.dot(f.px(Le), f.py(We), 3.8, INK)
    return f, Le, We


def fig_19_3a():
    f = Fig()
    f.axes("Real output (Y)", "Average price level")
    # Keynesian-shaped AS in data units: P(Y), Y in [0,100], P in [0,100]
    f.scale(100, 100)
    p0, Yb, Yf, A = 22.0, 40.0, 82.0, 5.0

    def AS(Y):
        if Y <= Yb:
            return p0
        u = (Y - Yb) / (Yf - Yb)
        return p0 + A * u * u / (1.0 - u)

    us = [.2, .4, .55, .66, .75, .82, .87, .91, .93]
    Y1 = Yb + 0.75 * (Yf - Yb)      # AD1 cuts the rising part of AS
    Y2 = 26.0                       # AD2 cuts the flat part of AS
    pts_x = sorted(set([8, Y2, Yb] + [Yb + u * (Yf - Yb) for u in us] + [Y1]))
    pts = [f.pt(x, AS(x)) for x in pts_x]
    xl = pts[-1][0]
    pts.append((xl + 1.0, f.Y1 + 14))      # runs vertically to the top (full capacity)
    f.curve(pts, RED, 2.8)
    lab(f, xl, f.Y1 + 4, "LRAS", RED, 12.5, "middle")
    e1 = f.pt(Y1, AS(Y1)); e2 = f.pt(Y2, AS(Y2))
    s_ = 1.0    # AD slope in pixels (down-right)
    yend = f.Y0 - 14
    mk = lambda e: ((e[0] - min(100, e[0] - f.X0 - 8) / s_, e[1] - min(100, e[0] - f.X0 - 8)), ((yend - e[1]) / s_ + e[0], yend))
    AD1, AD2 = mk(e1), mk(e2)
    assert on(AD1, e1) and on(AD2, e2)
    ln(f, AD1, GREY); ln(f, AD2, GREY)
    lab(f, AD1[1][0] + 6, AD1[1][1] + 4, "AD" + sb("", 1), GREY, 12.5)
    lab(f, AD2[1][0] + 6, AD2[1][1] + 4, "AD" + sb("", 2), GREY, 12.5)
    f.guide(e1[0], e1[1], sb("Y", 1), sb("P", 1))
    f.guide(e2[0], e2[1], sb("Y", 2), sb("P", 2))
    f.dot(*e1, 3.6, INK); f.dot(*e2, 3.6, INK)
    f.hshift(AD1, AD2, e2[1] - 52)
    f.hshift(AD1, AD2, e1[1] + 50)
    return f


def fig_19_3b():
    f = Fig(h=400).scale(100, 100)
    f.axes("Number of workers", "Average (real) wage rate")
    d = 18.0
    D1_ = lambda L: D_lab(L + d)
    Le = bisect(lambda L: D_lab(L) - S_lab(L), 10, 90)
    We = D_lab(Le)
    Lc = bisect(lambda L: D1_(L) - S_lab(L), 1, 90)
    Wc = S_lab(Lc)
    assert abs(D1_(Lc) - Wc) < 1e-6
    Q1 = Le - d
    assert abs(D1_(Q1) - We) < 1e-6
    fcurve(f, D_lab, 8, 95, 14, [Le], GREY)
    fcurve(f, D1_, 4, 78, 14, [Q1, Lc], GREY)
    fcurve(f, S_lab, 20, 80, 12, [Le, Lc], RED)
    lab(f, f.px(95) + 5, f.py(D_lab(95)) + 4, "AD" + sb("", "L"), GREY, 12.5)
    lab(f, f.px(78) + 6, f.py(D1_(78)) + 14, "AD" + sb("", "L1"), GREY, 12.5)
    lab(f, f.px(80) + 2, f.py(S_lab(80)) - 8, "AS" + sb("", "L"), RED, 12.5)
    # guides: W_e through a and b, Q_1 down from a, Q_e down from b, W_1 from c
    f.guide(f.px(Le), f.py(We), sb("Q", "e"), sb("W", "e"))
    f.line(f.px(Q1), f.py(We), f.px(Q1), f.Y0, TEAL, 1.5, "5 4", "butt")
    f.text(f.px(Q1), f.Y0 + 18, sb("Q", 1), 11.5, "middle")
    f.line(f.X0, f.py(Wc), f.px(Lc), f.py(Wc), TEAL, 1.5, "5 4", "butt")
    f.text(f.X0 - 8, f.py(Wc) + 4, sb("W", 1), 11.5, "end")
    for (L, W, name, dx, dy) in [(Q1, We, "a", -12, -8), (Le, We, "b", 14, -14), (Lc, Wc, "c", 8, 16)]:
        f.dot(f.px(L), f.py(W), 3.8, INK)
        lab(f, f.px(L) + dx, f.py(W) + dy, name, INK, 12.5)
    # AD shift arrows (two), horizontal, from AD_L to AD_L1 at equal height
    for w in (84, 66):
        Lx = inv_D(w)
        f.arrow(f.px(Lx) - 4, f.py(w), f.px(Lx - d) + 4, f.py(w), PURPLE)
    # unemployment bracket a..b
    yb = f.Y0 + 31
    f.line(f.px(Q1) + 6, yb, f.px(Le) - 6, yb, PURPLE, 1.8)
    f.arrowhead(f.px(Q1) + 2, yb, 180, PURPLE, 7)
    f.arrowhead(f.px(Le) - 2, yb, 0, PURPLE, 7)
    f.text((f.px(Q1) + f.px(Le)) / 2, yb + 15, "Unemployment", 11.5, "middle", PURPLE)
    return f, (Q1, Le, Lc, We, Wc)


def fig_19_4():
    f = Fig(h=400).scale(120, 30)
    f.axes("Quantity of call-centre workers", "Call-centre wage ($ per hour)")
    S = (f.pt(0, 4), f.pt(100, 26))           # w = 4 + 0.22 q
    D1 = (f.pt(0, 27.5), f.pt(94, 4))         # w = 27.5 - 0.25 q  (meets S at q = 50, w = 15)
    D2 = (f.pt(0, 18.95), f.pt(59.8, 4))      # w = 18.95 - 0.25 q (meets S at q = 31.8, w = 11)
    for l, c in ((D1, GREY), (D2, GREY), (S, RED)):
        ln(f, l, c)
    lab(f, D1[1][0] + 5, D1[1][1] + 4, "D" + sb("", 1), GREY)
    lab(f, D2[1][0] + 5, D2[1][1] + 4, "D" + sb("", 2), GREY)
    lab(f, S[1][0] + 4, S[1][1] - 6, "S", RED)
    e1 = cross(f, S, D1, sb("Q", 1), "$15")
    e2 = cross(f, S, D2, sb("Q", 2), "$11")
    assert abs(e1[1] - f.py(15)) < 0.05 and abs(e2[1] - f.py(11)) < 0.05
    f.hshift(D1, D2, f.py(17.5))
    f.hshift(D1, D2, f.py(7))
    axis_arrow_x(f, e1[0], e2[0])
    axis_arrow_y(f, e1[1], e2[1], -40)
    return f


def fig_19_5():
    f = Fig(h=400).scale(110, 16)
    f.axes("Quantity of farm workers", "Farm-worker wage ($ per hour)")
    S = (f.pt(10, 4), f.pt(100, 13))          # w = 3 + 0.1 q
    D = (f.pt(10, 12), f.pt(100, 3))          # w = 13 - 0.1 q
    ln(f, S, RED); ln(f, D, RED)
    lab(f, S[1][0] + 4, S[1][1] - 6, "S", RED)
    lab(f, D[1][0] + 4, D[1][1] + 4, "D", RED)
    wmin = f.py(11)
    ln(f, ((f.X0, wmin), (f.px(104), wmin)), DARK, 2.4)
    lab(f, f.px(104) + 4, wmin - 4, "Minimum", DARK, 11.5)
    lab(f, f.px(104) + 4, wmin + 10, "wage", DARK, 11.5)
    e = cross(f, S, D, "Q", "$8")
    assert abs(e[1] - f.py(8)) < 0.01
    a = Fig.intersect(D, ((f.X0, wmin), (f.px(104), wmin)))
    b = Fig.intersect(S, ((f.X0, wmin), (f.px(104), wmin)))
    assert on(D, a) and on(S, b) and abs(a[1] - wmin) < 0.01
    f.line(a[0], a[1], a[0], f.Y0, TEAL, 1.5, "5 4", "butt")
    f.line(b[0], b[1], b[0], f.Y0, TEAL, 1.5, "5 4", "butt")
    f.text(a[0], f.Y0 + 18, sb("Q", 1), 11.5, "middle")
    f.text(b[0], f.Y0 + 18, sb("Q", 2), 11.5, "middle")
    f.text(f.X0 - 8, wmin + 4, "$11", 11.5, "end")
    f.dot(*a, 3.6, INK); f.dot(*b, 3.6, INK)
    yb = f.Y0 + 31
    f.line(a[0] + 6, yb, b[0] - 6, yb, PURPLE, 1.8)
    f.arrowhead(a[0] + 2, yb, 180, PURPLE, 7)
    f.arrowhead(b[0] - 2, yb, 0, PURPLE, 7)
    f.text((a[0] + b[0]) / 2, yb + 15, "Unemployment", 11.5, "middle", PURPLE)
    return f, (a, b, e)


def fig_19_6():
    f = Fig()
    f.axes("Quantity of loanable funds", "Interest rate")
    S = ((104, 292), (346, 58))
    D1 = ((96, 62), (296, 282))
    D2 = shifted(D1, 92, 0)
    ln(f, D1, GREY); ln(f, D2, GREY); ln(f, S, RED)
    lab(f, D1[1][0] + 4, D1[1][1] + 14, "D" + sb("", 1), GREY)
    lab(f, D2[1][0] + 4, D2[1][1] + 4, "D" + sb("", 2), GREY)
    lab(f, S[1][0] + 4, S[1][1] - 2, "S (loanable", RED, 12)
    lab(f, S[1][0] + 4, S[1][1] + 12, "funds)", RED, 12)
    e1 = cross(f, S, D1, sb("Q", "LF1"), sb("i", 1))
    e2 = cross(f, S, D2, sb("Q", "LF3"), sb("i", 2))
    x2 = Fig.x_at(D1, e2[1])
    assert on(D1, (x2, e2[1]))
    f.line(x2, e2[1], x2, f.Y0, TEAL, 1.5, "5 4", "butt")
    f.text(x2, f.Y0 + 18, sb("Q", "LF2"), 11.5, "middle")
    f.dot(x2, e2[1], 3.6, INK)
    f.hshift(D1, D2, 120)
    f.hshift(D1, D2, 236)
    axis_arrow_y(f, e1[1], e2[1], -40)
    return f, (e1, e2, x2)


def fig_19_7():
    f = Fig()
    f.axes("Quantity of loanable funds", "Interest rate")
    S = ((236, f.Y0), (236, 46))
    D1 = ((96, 62), (296, 282))
    D2 = shifted(D1, 66, 0)
    ln(f, D1, GREY); ln(f, D2, GREY); ln(f, S, RED)
    lab(f, D1[1][0] + 4, D1[1][1] + 14, "D" + sb("", 1), GREY)
    lab(f, D2[1][0] + 4, D2[1][1] + 4, "D" + sb("", 2), GREY)
    lab(f, 236, 36, "S" + sb("", "LF"), RED, 13, "middle")
    e1 = cross(f, S, D1, None, sb("i", 1), to_x=False)
    e2 = cross(f, S, D2, None, sb("i", 2), to_x=False)
    f.text(236, f.Y0 + 18, sb("Q", "LF1"), 11.5, "middle")
    x2 = Fig.x_at(D1, e2[1])
    f.line(x2, e2[1], x2, f.Y0, TEAL, 1.5, "5 4", "butt")
    f.text(x2, f.Y0 + 18, sb("Q", "LF2"), 11.5, "middle")
    f.dot(x2, e2[1], 3.6, INK)
    f.hshift(D1, D2, 110)
    f.hshift(D1, D2, 226)
    axis_arrow_y(f, e1[1], e2[1], -40)
    axis_arrow_x(f, e1[0], x2)
    return f, (e1, e2, x2)


# =============================================================== CHAPTER 20
def adas(xl="Real output (Y)"):
    f = Fig()
    f.axes(xl, "Average price level")
    return f


def fig_20_1():
    f = adas()
    SR = ((118, 292), (334, 58))
    A1 = ((104, 84), (296, 264))
    A2 = shifted(A1, 52, -8)
    ln(f, A1, GREY); ln(f, A2, GREY); ln(f, SR, RED)
    lab(f, A1[1][0] + 5, A1[1][1] + 6, "AD" + sb("", 1), GREY)
    lab(f, A2[1][0] + 5, A2[1][1] + 6, "AD" + sb("", 2), GREY)
    lab(f, SR[1][0] - 8, SR[1][1] - 8, "SRAS", RED)
    e1 = cross(f, SR, A1, sb("Y", 1), sb("P", 1))
    e2 = cross(f, SR, A2, sb("Y", 2), sb("P", 2))
    f.hshift(A1, A2, 108)
    f.hshift(A1, A2, 226)
    axis_arrow_x(f, e1[0], e2[0])
    axis_arrow_y(f, e1[1], e2[1])
    return f, (e1, e2)


def fig_20_2():
    f = adas()
    AD = ((104, 70), (352, 288))
    S1 = ((156, 298), (352, 118))
    S2 = shifted(S1, -68, 0)
    ln(f, AD, GREY); ln(f, S2, RED); ln(f, S1, RED)
    lab(f, AD[1][0] + 5, AD[1][1] + 6, "AD", GREY)
    lab(f, S1[1][0] + 5, S1[1][1] - 2, "SRAS" + sb("", 1), RED)
    lab(f, S2[1][0] + 3, S2[1][1] - 8, "SRAS" + sb("", 2), RED)
    e1 = cross(f, S1, AD, sb("Y", 1), sb("P", 1))
    e2 = cross(f, S2, AD, sb("Y", 2), sb("P", 2))
    f.hshift(S1, S2, 250)
    axis_arrow_x(f, e1[0], e2[0])
    axis_arrow_y(f, e1[1], e2[1])
    return f, (e1, e2)


def fig_20_3():
    f = adas()
    SR = ((146, 296), (338, 92))
    A1 = ((92, 68), (298, 268))
    A2 = shifted(A1, 56, -6)
    ln(f, A1, GREY); ln(f, A2, GREY); ln(f, SR, RED)
    lab(f, A1[1][0] + 5, A1[1][1] + 6, "AD" + sb("", 1), GREY)
    lab(f, A2[1][0] + 5, A2[1][1] + 6, "AD" + sb("", 2), GREY)
    lab(f, SR[1][0] + 5, SR[1][1] - 2, "SRAS" + sb("", 1), RED)
    e1 = cross(f, SR, A1, sb("Y", 1), sb("P", 1))
    e2 = cross(f, SR, A2, sb("Y", 2), sb("P", 2))
    f.hshift(A1, A2, 100)
    f.hshift(A1, A2, 232)
    axis_arrow_x(f, e1[0], e2[0])
    axis_arrow_y(f, e1[1], e2[1])
    return f, (e1, e2)


def fig_20_4():
    f = adas()
    S1 = ((112, 292), (338, 90))
    sS = (S1[1][1] - S1[0][1]) / (S1[1][0] - S1[0][0])       # pixel slope (negative)
    sA = 0.95
    xa, xb = 206, 248
    A = (xa, Fig.y_at(S1, xa)); B = (xb, Fig.y_at(S1, xb))
    mkAD = lambda p: ((p[0] - 96, p[1] - 96 * sA), (p[0] + 104, p[1] + 104 * sA))
    AD1 = mkAD(A); AD2 = mkAD(B)
    dy = Fig.y_at(AD2, xa) - A[1]              # < 0: SRAS moves up by |dy|
    S2 = shifted(S1, 0, dy)
    C = (xa, A[1] + dy)
    D = (xb, B[1] + dy)
    AD3 = mkAD(D)
    assert on(AD1, A) and on(AD2, B) and on(AD2, C) and on(S2, C) and on(S2, D) and on(AD3, D)
    assert on(S1, A) and on(S1, B)

    def clip(l, ytop=44):
        (x1, y1), (x2, y2) = l
        if y1 < ytop:
            x1 = Fig.x_at(l, ytop); y1 = ytop
        return ((x1, y1), (x2, y2))
    S2c = clip(S2); AD3c = clip(AD3)
    ln(f, AD1, GREY); ln(f, AD2, GREY); ln(f, AD3c, GREY)
    ln(f, S1, RED); ln(f, S2c, RED)
    lab(f, AD1[1][0] + 5, AD1[1][1] + 6, "AD" + sb("", 1), GREY)
    lab(f, AD2[1][0] + 5, AD2[1][1] + 6, "AD" + sb("", 2), GREY)
    lab(f, AD3c[1][0] + 5, AD3c[1][1] + 6, "AD" + sb("", 3), GREY)
    lab(f, S1[1][0] + 4, S1[1][1] - 4, "SRAS" + sb("", 1), RED)
    lab(f, S2c[1][0] + 4, S2c[1][1] - 4, "SRAS" + sb("", 2), RED)
    for i, p in enumerate((A, B, C, D), 1):
        f.guide(p[0], p[1], None, sb("P", i), to_x=False)
    f.line(xa, C[1], xa, f.Y0, TEAL, 1.5, "5 4", "butt")
    f.line(xb, D[1], xb, f.Y0, TEAL, 1.5, "5 4", "butt")
    f.text(xa, f.Y0 + 18, sb("Y", 1), 11.5, "middle")
    f.text(xb, f.Y0 + 18, sb("Y", 2), 11.5, "middle")
    for p in (A, B, C, D):
        f.dot(*p, 3.6, INK)

    def mv(p, q, k=9):
        L = math.hypot(q[0] - p[0], q[1] - p[1])
        ux, uy = (q[0] - p[0]) / L, (q[1] - p[1]) / L
        f.arrow(p[0] + ux * k, p[1] + uy * k, q[0] - ux * k, q[1] - uy * k, PURPLE, 2.6, 9)
    mv(A, B); mv(B, C); mv(C, D)
    def halo(x, y, t):
        f.add(f'<text x="{x:.1f}" y="{y:.1f}" font-size="11.5" fill="{PURPLE}" stroke="#ffffff" '
              f'stroke-width="3" paint-order="stroke" font-weight="600">{t}</text>')
    halo(A[0] + 14, A[1] + 4, "(1)")
    halo(B[0] - 42, B[1] - 10, "(2)")
    halo((C[0] + D[0]) / 2 - 26, (C[1] + D[1]) / 2 - 4, "(3)")
    axis_arrow_y(f, A[1], D[1], -44)
    return f, (A, B, C, D)


def fig_20_5():
    f = adas()
    AD = ((100, 84), (372, 266))
    L1 = ((176, f.Y0), (176, 52)); L2 = ((262, f.Y0), (262, 52))
    ln(f, AD, GREY); ln(f, L1); ln(f, L2)
    lab(f, AD[1][0] + 4, AD[1][1] + 14, "AD", GREY)
    lab(f, 176, 42, "LRAS" + sb("", 1), RED, 12.5, "middle")
    lab(f, 262, 42, "LRAS" + sb("", 2), RED, 12.5, "middle")
    e1 = cross(f, L1, AD, None, sb("P", 1), to_x=False)
    e2 = cross(f, L2, AD, None, sb("P", 2), to_x=False)
    f.text(176, f.Y0 + 18, sb("Y", 1), 11.5, "middle")
    f.text(262, f.Y0 + 18, sb("Y", 2), 11.5, "middle")
    f.hshift(L1, L2, 100)
    axis_arrow_x(f, e1[0], e2[0])
    axis_arrow_y(f, e1[1], e2[1])
    return f, (e1, e2)


# ------------ zero-axis charts (Phillips curves, inflation series) ---------------
class ZM:
    """Data mapping for charts whose horizontal axis sits at y = 0."""

    def __init__(self, f, umax, vmin, vmax, ytop=44, ybot=318):
        self.f, self.umax, self.vmin, self.vmax = f, umax, vmin, vmax
        self.ybot, self.ytop = ybot, ytop
        self.sx = (f.X1 - f.X0 - 22) / umax
        self.sy = (ybot - ytop) / (vmax - vmin)

    def px(self, u):
        return self.f.X0 + u * self.sx

    def py(self, v):
        return self.ybot - (v - self.vmin) * self.sy

    def pt(self, u, v):
        return (self.px(u), self.py(v))

    def axes(self, xlabel, ylabel, zero=True):
        f = self.f
        f.line(f.X0, self.ybot, f.X0, self.ytop - 2, INK, 2.2)
        f.arrowhead(f.X0, self.ytop - 7, -90, INK, 9)
        yz = self.py(0)
        f.line(f.X0, yz, f.X1, yz, INK, 2.2)
        f.arrowhead(f.X1 + 5, yz, 0, INK, 9)
        if zero:
            f.text(f.X0 - 8, yz + 4, "0", 11.5, "end")
        f.text((f.X0 + f.X1) / 2, f.h - 14, xlabel, 12.5, "middle")
        f.text(20, (self.ybot + self.ytop) / 2, ylabel, 12.5, "middle", rotate=-90)

    def ytick(self, v, label=None):
        y = self.py(v)
        self.f.text(self.f.X0 - 8, y + 4, label if label is not None else f"{v:g}", 11.5, "end")

    def xtick(self, u, label):
        self.f.text(self.px(u), self.py(0) + 17, label, 11.5, "middle")

    def guide(self, u, v, xl=None, yl=None, x=True, y=True):
        f = self.f
        if y:
            f.line(f.X0, self.py(v), self.px(u), self.py(v), TEAL, 1.5, "5 4", "butt")
            if yl is not None:
                self.ytick(v, yl)
        if x:
            f.line(self.px(u), self.py(v), self.px(u), self.py(0), TEAL, 1.5, "5 4", "butt")
            if xl is not None:
                self.xtick(u, xl)


def fig_20_6():
    f = Fig()
    m = ZM(f, 7.4, -2, 4, ytop=48)
    m.axes("Year", "Inflation rate (%)", zero=False)
    yz = m.py(0)
    f.add(f'<rect x="{f.X0 + 1:.1f}" y="{yz:.1f}" width="{f.X1 - f.X0 - 1:.1f}" '
          f'height="{m.ybot - yz:.1f}" fill="#fbe9e6"/>')
    # redraw zero axis over the band
    f.line(f.X0, yz, f.X1, yz, INK, 2.2)
    f.arrowhead(f.X1 + 5, yz, 0, INK, 9)
    f.line(f.X0, m.ybot, f.X0, m.ytop - 2, INK, 2.2)
    f.arrowhead(f.X0, m.ytop - 7, -90, INK, 9)
    for v in range(-2, 5):
        m.ytick(v, (MINUS + str(-v)) if v < 0 else str(v))
        f.line(f.X0 - 4, m.py(v), f.X0, m.py(v), INK, 1.4)
    years = list(range(1999, 2006))
    rate = [1.8, 3.1, 2.4, 1.5, 0.6, -0.7, -0.2]
    for i, yr in enumerate(years):
        u = 0.7 + i
        f.line(m.px(u), m.py(3.7), m.px(u), m.ybot, "#dddddd", 1, "2 3", "butt")
        f.text(m.px(u), m.ybot + 17, str(yr), 11, "middle")
    pts = [m.pt(0.7 + i, r) for i, r in enumerate(rate)]
    f.path("M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts), RED, 2.8)
    for p in pts:
        f.dot(*p, 3.6, RED)
    f.text(m.px(3.6), m.py(2.85), "Disinflation", 11.5, "start", INK, italic=True)
    f.text(m.px(3.6), m.py(2.85) + 13, "(rate falling but still positive)", 10.5, "start", GREY)
    f.text(m.px(0.35), m.py(-1.45), "Deflation (negative inflation)", 11.5, "start", RED)
    return f, (years, rate)


def fig_20_7():
    f = Fig()
    m = ZM(f, 12.5, -1.6, 9.6, ytop=44)
    m.axes("Unemployment rate", "Rate of change of wages")
    fn = lambda u: -1.0 + 9.0 / u ** 1.3
    us = [0.95, 1.1, 1.3, 1.6, 2.0, 2.5, 3.2, 4.0, 5.0, 6.5, 8.0, 10.0, 11.8]
    f.curve([m.pt(u, fn(u)) for u in us], RED, 2.8)
    return f


def fig_20_8():
    f = Fig()
    m = ZM(f, 13.5, -2.4, 15, ytop=44)
    m.axes("Unemployment rate (%)", "Inflation rate (%)")
    fn = lambda u: 48.0 / u - 5.0
    A, B = (6, fn(6)), (4, fn(4))
    assert abs(A[1] - 3) < 1e-9 and abs(B[1] - 7) < 1e-9
    us = [2.6, 3.0, 3.5, 4.0, 5.0, 6.0, 7.5, 9.0, 11.0, 12.6]
    f.curve([m.pt(u, fn(u)) for u in us], RED, 2.8)
    m.guide(A[0], A[1], "6", "3")
    m.guide(B[0], B[1], "4", "7")
    for name, p, dx, dy in (("A", A, 8, -8), ("B", B, 8, -8)):
        f.dot(*m.pt(*p), 3.8, INK)
        lab(f, m.px(p[0]) + dx, m.py(p[1]) + dy, name, INK, 12.5)
    return f


def fig_20_9():
    f = adas()
    SR = ((112, 294), (332, 64))
    A1 = ((96, 96), (288, 274))
    A2 = shifted(A1, 84, -34)
    ln(f, A1, GREY); ln(f, A2, GREY); ln(f, SR, RED)
    lab(f, A1[1][0] + 5, A1[1][1] + 6, "AD" + sb("", 1), GREY)
    lab(f, A2[1][0] + 5, A2[1][1] + 6, "AD" + sb("", 2), GREY)
    lab(f, SR[1][0] - 6, SR[1][1] - 8, "SRAS", RED)
    cross(f, SR, A1, sb("Y", 1), sb("P", 1))
    cross(f, SR, A2, sb("Y", 2), sb("P", 2))
    return f


PH_K, PH_M, PH_SHIFT = 30.0, 3.0, 4.0     # SRPC1: pi = 30/u - 3 ; each shift +4


def fig_20_10():
    f = Fig()
    m = ZM(f, 11.6, -1.6, 17.5, ytop=44)
    m.axes("Unemployment rate (%)", "Inflation rate (%)")
    f1 = lambda u: PH_K / u - PH_M
    fk = lambda k: (lambda u: f1(u) + PH_SHIFT * (k - 1))
    NRU = 5.0
    A, B, C, D, E = (NRU, f1(NRU)), (3, f1(3)), (NRU, f1(NRU) + 4), (3, f1(3) + 4), (NRU, f1(NRU) + 8)
    assert [round(v[1], 6) for v in (A, B, C, D, E)] == [3, 7, 7, 11, 11]
    # LRPC
    ln(f, (m.pt(NRU, 0), m.pt(NRU, 16.6)), GREY, 2.8)
    lab(f, m.px(NRU), m.py(16.6) - 8, "LRPC", GREY, 12.5, "middle")
    starts = {1: 1.8, 2: 2.3, 3: 3.05}
    for k in (1, 2, 3):
        fn = fk(k)
        us = xs_for(starts[k], 9.3, 12, [3, NRU])
        f.curve([m.pt(u, fn(u)) for u in us], RED, 2.8)
        f.text(m.px(9.3) + 5, m.py(fn(9.3)) - 6, "SRPC" + sb("", k), 12, "start", RED)
    for p, xl, yl in ((A, None, "3"), (C, None, "7"), (E, None, "11")):
        m.guide(p[0], p[1], None, yl, x=False)
    m.guide(3, D[1], "3", None, y=False)
    m.xtick(NRU, "5")
    for p, name, dx, dy in ((A, "A", 8, -8), (B, "B", -14, -8), (C, "C", 8, -8),
                            (D, "D", -14, -8), (E, "E", 8, -8)):
        f.dot(*m.pt(*p), 3.8, INK)
        lab(f, m.px(p[0]) + dx, m.py(p[1]) + dy, name, INK, 12.5)

    def curve_arrow(fn, u0, u1):
        pts = [m.pt(u0 + (u1 - u0) * i / 14, fn(u0 + (u1 - u0) * i / 14)) for i in range(15)]
        f.path("M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts[:-1]), PURPLE, 2.6)
        (x1, y1), (x2, y2) = pts[-2], pts[-1]
        f.arrowhead(x2, y2, math.degrees(math.atan2(y2 - y1, x2 - x1)), PURPLE, 9)
    g = 0.22
    curve_arrow(fk(1), NRU - g, 3 + g)
    curve_arrow(fk(2), NRU - g, 3 + g)
    f.arrow(m.px(3) + 6, m.py(7), m.px(NRU) - 6, m.py(7), PURPLE, 2.6, 9)
    f.arrow(m.px(3) + 6, m.py(11), m.px(NRU) - 6, m.py(11), PURPLE, 2.6, 9)
    return f


def fig_20_11():
    f = Fig()
    m = ZM(f, 10.4, -1.6, 12.5, ytop=44)
    m.axes("Unemployment rate (%)", "Inflation rate (%)")
    N1, N2 = 6.4, 4.0
    L1 = (m.pt(N1, 0), m.pt(N1, 11.5)); L2 = (m.pt(N2, 0), m.pt(N2, 11.5))
    ln(f, L1, GREY, 2.8); ln(f, L2, GREY, 2.8)
    lab(f, m.px(N1), m.py(11.5) - 8, "LRPC" + sb("", 1), GREY, 12.5, "middle")
    lab(f, m.px(N2), m.py(11.5) - 8, "LRPC" + sb("", 2), GREY, 12.5, "middle")
    for N, k in ((N1, 1), (N2, 2)):
        f.line(m.px(N), m.py(0), m.px(N), m.py(0) + 5, INK, 1.6)
        m.xtick(N, "NRU" + sb("", k))
    f.hshift(L1, L2, m.py(4))
    f.hshift(L1, L2, m.py(8.5))
    return f, (N1, N2)


# =============================================================== BUILD
def build():
    save("fig-18-1", fig_18_1(),
         "Figure 18.1: The effect of supply-side policies",
         "Effect of supply-side policies on aggregate supply",
         "Two panels. (a) A Keynesian-shaped short-run aggregate supply curve, flat at low output and vertical at full capacity, shifts right from AS1 to AS2. (b) A vertical long-run aggregate supply curve shifts right from LRAS1 to LRAS2. Both axes show average price level against real output.",
         "Supply-side policies raise the economy&rsquo;s productive capacity. <em>Panel (a):</em> the Keynesian aggregate supply curve, flat while there is spare capacity and vertical at full capacity, moves right from AS<sub>1</sub> to AS<sub>2</sub>, so full-capacity output rises. <em>Panel (b):</em> in the long-run (classical) model the vertical LRAS shifts right from LRAS<sub>1</sub> to LRAS<sub>2</sub>, showing a higher potential level of real output.")

    save("fig-19-1", fig_19_1(),
         "Figure 19.1: Inflows and outflows from the &lsquo;pool&rsquo; of unemployment",
         "Inflows and outflows from the pool of unemployment",
         "Flow diagram: five inflows (redundancy, resignation, school leavers, returners to the labour force, migrants) arrow down into a box labelled pool of unemployment; seven outflows (finding a job, retiring, education, caring for family, emigrating, giving up the search, death) arrow out below it.",
         "The stock of unemployed people is like a pool with water flowing in and out. Five inflows (job losses, resignations, school leavers, people returning to the labour force and new migrants without work) raise unemployment. Seven outflows lower it, but only finding a job is a genuine return to employment; the others remove people from the labour force, so they are no longer counted as unemployed.")

    f, Le, We = fig_19_2()
    save("fig-19-2", f,
         "Figure 19.2: Equilibrium in the labour market",
         "Equilibrium in the labour market",
         "Labour market diagram: downward-sloping demand for labour AD-L and upward-sloping supply of labour AS-L meet at the equilibrium wage We and equilibrium number of workers Qe.",
         "The aggregate demand for labour (AD<sub>L</sub>) slopes down and the aggregate supply of labour (AS<sub>L</sub>) slopes up. They cross at the equilibrium wage W<sub>e</sub> and the equilibrium number of workers Q<sub>e</sub>, where everyone willing to work at that wage has a job.")

    save("fig-19-3a", fig_19_3a(),
         "Figure 19.3(a): A decrease in AD",
         "A decrease in aggregate demand",
         "AD/AS diagram with a Keynesian-shaped aggregate supply curve, flat at low output and vertical at full capacity. Aggregate demand falls from AD1 to AD2, so output falls from Y1 to Y2 and the price level from P1 to P2.",
         "Aggregate demand falls from AD<sub>1</sub> to AD<sub>2</sub> against an aggregate supply curve that is flat at low output and vertical at full-capacity output. The economy moves down the curve, so real output falls from Y<sub>1</sub> to Y<sub>2</sub> and the price level from P<sub>1</sub> to P<sub>2</sub>; lower output means less demand for labour.")

    save("fig-19-3b", fig_19_3b()[0],
         "Figure 19.3(b): Demand-deficient unemployment",
         "Demand-deficient unemployment",
         "Labour market diagram: the demand for labour falls from AD-L to AD-L1 but the wage stays at We. At We employers want Q1 workers (point a) while Qe workers are willing to work (point b); if wages fell freely the market would settle at point c on wage W1.",
         "The fall in aggregate demand shifts labour demand left from AD<sub>L</sub> to AD<sub>L1</sub>. If wages fell freely the market would move from b to c at the lower wage W<sub>1</sub>. With sticky wages the wage stays at W<sub>e</sub>, so employers demand only Q<sub>1</sub> workers (point a) while Q<sub>e</sub> are willing to work (point b); the gap from a to b is demand-deficient unemployment.")

    save("fig-19-4", fig_19_4(),
         "Figure 19.4: A fall in employment (structural unemployment)",
         "A fall in employment (structural unemployment)",
         "Labour market for call-centre workers: demand falls from D1 to D2 against supply S, cutting employment from Q1 to Q2 and the wage from $15 to $11 per hour.",
         "Automation permanently reduces the demand for call-centre workers, shifting demand left from D<sub>1</sub> to D<sub>2</sub> along supply curve S. The wage falls from $15 to $11 per hour and employment falls from Q<sub>1</sub> to Q<sub>2</sub>; workers who cannot easily move to other kinds of work face structural unemployment.")

    save("fig-19-5", fig_19_5()[0],
         "Figure 19.5: Minimum wage and structural unemployment",
         "Minimum wage and structural unemployment",
         "Labour market for farm workers: equilibrium wage $8 at quantity Q. A minimum wage of $11 above equilibrium leaves Q1 workers demanded but Q2 supplied, so the gap from Q1 to Q2 is unemployment.",
         "The free-market wage for farm workers is $8 per hour with Q workers employed. A minimum wage of $11 lies above equilibrium: employers demand only Q<sub>1</sub> workers while Q<sub>2</sub> want to work at that wage, so the gap between Q<sub>1</sub> and Q<sub>2</sub> is unemployment.")

    save("fig-19-6", fig_19_6()[0],
         "Figure 19.6: Crowding out &mdash; moderate view",
         "Crowding out, moderate view",
         "Loanable funds market with an upward-sloping supply S. Government borrowing shifts demand right from D1 to D2, raising the interest rate from i1 to i2 and total borrowing from QLF1 to QLF3, while private borrowing falls to QLF2.",
         "Government borrowing shifts the demand for loanable funds right from D<sub>1</sub> to D<sub>2</sub>. Because supply slopes upward, the interest rate rises from i<sub>1</sub> to i<sub>2</sub> and total borrowing rises from Q<sub>LF1</sub> to Q<sub>LF3</sub>. At i<sub>2</sub> private borrowers demand only Q<sub>LF2</sub>, so private investment is partly crowded out.")

    save("fig-19-7", fig_19_7()[0],
         "Figure 19.7: Crowding out &mdash; extreme view",
         "Crowding out, extreme view",
         "Loanable funds market with a vertical supply curve SLF. Demand shifts right from D1 to D2, raising the interest rate from i1 to i2 with no rise in total lending QLF1; private borrowing falls to QLF2.",
         "With a fixed (vertical) supply of loanable funds S<sub>LF</sub>, the rightward shift of demand from D<sub>1</sub> to D<sub>2</sub> only raises the interest rate from i<sub>1</sub> to i<sub>2</sub>. Total lending stays at Q<sub>LF1</sub>, so the extra government borrowing displaces private borrowing, which falls to Q<sub>LF2</sub>: crowding out is complete.")

    save("fig-20-1", fig_20_1()[0],
         "Figure 20.1: Demand-pull inflation",
         "Demand-pull inflation",
         "AD/AS diagram: aggregate demand shifts right from AD1 to AD2 along the upward-sloping SRAS curve, raising the price level from P1 to P2 and real output from Y1 to Y2.",
         "An increase in aggregate demand from AD<sub>1</sub> to AD<sub>2</sub> moves the economy up along the SRAS curve. The average price level rises from P<sub>1</sub> to P<sub>2</sub> and real output rises from Y<sub>1</sub> to Y<sub>2</sub>.")

    save("fig-20-2", fig_20_2()[0],
         "Figure 20.2: Cost-push inflation",
         "Cost-push inflation",
         "AD/AS diagram: short-run aggregate supply shifts left from SRAS1 to SRAS2 against a fixed AD curve, raising the price level from P1 to P2 while output falls from Y1 to Y2.",
         "Higher costs of production shift short-run aggregate supply left from SRAS<sub>1</sub> to SRAS<sub>2</sub>. Against the unchanged AD curve the price level rises from P<sub>1</sub> to P<sub>2</sub> while real output falls from Y<sub>1</sub> to Y<sub>2</sub>.")

    save("fig-20-3", fig_20_3()[0],
         "Figure 20.3: Demand-pull inflation",
         "Demand-pull inflation, first round",
         "AD/AS diagram showing one round of demand-pull inflation: AD shifts right from AD1 to AD2 along SRAS1, raising the price level from P1 to P2 and output from Y1 to Y2.",
         "The first round of a possible inflationary spiral: aggregate demand rises from AD<sub>1</sub> to AD<sub>2</sub> along SRAS<sub>1</sub>, lifting the price level from P<sub>1</sub> to P<sub>2</sub> and output from Y<sub>1</sub> to Y<sub>2</sub>.")

    save("fig-20-4", fig_20_4()[0],
         "Figure 20.4: An inflationary spiral",
         "An inflationary spiral",
         "AD/AS diagram with three numbered movements: (1) AD1 to AD2 along SRAS1 raises the price level from P1 to P2 and output from Y1 to Y2; (2) SRAS shifts left to SRAS2 as wages rise, price P3 and output back to Y1; (3) AD2 to AD3 along SRAS2 raises price to P4 and output to Y2 again.",
         "Movement (1) is demand-pull: AD rises from AD<sub>1</sub> to AD<sub>2</sub>, taking the price level from P<sub>1</sub> to P<sub>2</sub> and output from Y<sub>1</sub> to Y<sub>2</sub>. Tight labour markets push wages up, so (2) SRAS shifts left to SRAS<sub>2</sub>, raising the price level to P<sub>3</sub> and pushing output back to Y<sub>1</sub>. Higher wages are spent, so (3) AD rises to AD<sub>3</sub>, taking prices to P<sub>4</sub> and output to Y<sub>2</sub> again. The wage-price cycle can keep repeating.")

    save("fig-20-5", fig_20_5()[0],
         "Figure 20.5: &ldquo;Good&rdquo; deflation",
         "Good deflation",
         "AD/AS diagram: the vertical LRAS shifts right from LRAS1 to LRAS2 against a fixed downward-sloping AD curve, raising real output from Y1 to Y2 while the price level falls from P1 to P2.",
         "Better or more plentiful factors of production shift long-run aggregate supply right from LRAS<sub>1</sub> to LRAS<sub>2</sub>. Against the fixed AD curve, real output rises from Y<sub>1</sub> to Y<sub>2</sub> while the price level falls from P<sub>1</sub> to P<sub>2</sub>: deflation with growth rather than recession.")

    save("fig-20-6", fig_20_6()[0],
         "Figure 20.6: Changing rates of inflation and deflation",
         "Changing rates of inflation and deflation",
         "Line chart of a hypothetical inflation rate, 1999 to 2005: 1.8, 3.1, 2.4, 1.5, 0.6, -0.7 and -0.2 percent. It peaks in 2000, falls every year to 2004 and turns negative from 2004.",
         "Hypothetical inflation rates: 1.8% (1999), 3.1% (2000), 2.4%, 1.5%, 0.6% (2003), then &minus;0.7% (2004) and &minus;0.2% (2005). From 2001 to 2003 the rate is falling but still positive, which is <em>disinflation</em>; in 2004 and 2005 it is below zero, which is <em>deflation</em> (the price level itself is falling).")

    save("fig-20-7", fig_20_7(),
         "Figure 20.7: The original Phillips curve",
         "The original Phillips curve",
         "Downward-sloping convex curve with unemployment rate on the horizontal axis and rate of change of wages on the vertical axis: fast wage growth when unemployment is low, wage growth near zero or negative when unemployment is high.",
         "Phillips&rsquo;s original relationship: the rate of change of money wages falls as the unemployment rate rises. The convex curve is steep at low unemployment (wages rise quickly) and flattens as unemployment grows, crossing zero wage growth at a moderate rate of unemployment.")

    save("fig-20-8", fig_20_8(),
         "Figure 20.8: The Phillips curve as it is usually drawn",
         "The Phillips curve as usually drawn",
         "Downward-sloping short-run Phillips curve with inflation rate on the vertical axis and unemployment rate on the horizontal axis. Point A is 6% unemployment and 3% inflation; point B is 4% unemployment and 7% inflation.",
         "The short-run Phillips curve trades unemployment against inflation. Moving up the curve from A (6% unemployment, 3% inflation) to B (4% unemployment, 7% inflation) lowers unemployment by 2 percentage points but raises inflation by 4 points; moving back down reverses the trade-off.")

    save("fig-20-9", fig_20_9(),
         "Figure 20.9: Phillips curve relationship through AD/AS analysis",
         "Phillips curve relationship through AD/AS analysis",
         "AD/AS diagram: aggregate demand rises from AD1 to AD2 along the upward-sloping SRAS curve, raising output from Y1 to Y2 and the price level from P1 to P2.",
         "The same trade-off seen in AD/AS terms: a rise in aggregate demand from AD<sub>1</sub> to AD<sub>2</sub> raises real output from Y<sub>1</sub> to Y<sub>2</sub> (so unemployment falls) and the price level from P<sub>1</sub> to P<sub>2</sub> (so inflation rises), a movement up the short-run Phillips curve.")

    save("fig-20-10", fig_20_10(),
         "Figure 20.10: The long-run Phillips curve",
         "The long-run Phillips curve",
         "Three short-run Phillips curves SRPC1, SRPC2 and SRPC3 and a vertical LRPC at the natural rate of unemployment, 5%. The economy moves A(5%, 3%) to B(3%, 7%) to C(5%, 7%) to D(3%, 11%) to E(5%, 11%).",
         "Start at A on SRPC<sub>1</sub>: unemployment is at the natural rate of 5% and inflation is 3%. Expansionary policy moves the economy along SRPC<sub>1</sub> to B (3% unemployment, 7% inflation). When workers see through the money illusion and expect higher inflation, the curve shifts up to SRPC<sub>2</sub> and unemployment returns to 5% at C (7% inflation). Repeating the policy gives D (3%, 11%) and then E (5%, 11%) on SRPC<sub>3</sub>. Joining A, C and E gives the vertical long-run Phillips curve (LRPC) at the natural rate: no long-run trade-off.")

    save("fig-20-11", fig_20_11()[0],
         "Figure 20.11: Supply-side policies can reduce the NRU",
         "Supply-side policies can reduce the natural rate of unemployment",
         "Two vertical long-run Phillips curves: LRPC1 at the natural rate of unemployment NRU1 and LRPC2 to its left at a lower rate NRU2, with two arrows showing the leftward shift.",
         "Effective supply-side policies, such as better education and training or more flexible labour markets, shift the long-run Phillips curve left from LRPC<sub>1</sub> to LRPC<sub>2</sub>. The natural rate of unemployment falls from NRU<sub>1</sub> to NRU<sub>2</sub> at any given rate of inflation.")


if __name__ == "__main__":
    build()
