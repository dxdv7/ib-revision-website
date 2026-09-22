"""Original vector figures for chapters 13-17 (macroeconomics), own coordinates."""
import os, sys, json, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import *

OUT = "/Users/davidbukraba/Desktop/IB WEBSITE/assets/figures-original"
os.makedirs(OUT, exist_ok=True)

MINUS = "&#8722;"
AM = 0.9      # pixel slope of AD (falls to the right)
SM = -0.85    # pixel slope of SRAS (rises to the right)


def save(fid, fig, label, alt, caption):
    title = label.split(": ", 1)[-1]
    open(f"{OUT}/{fid}.svg", "w").write(fig.svg(title, alt))
    with open(f"{OUT}/{fid}.json", "w") as fh:
        json.dump({"label": label, "alt": alt, "caption": caption}, fh, indent=1)
    print("saved", fid)


# ---------------------------------------------------------------- helpers
def L(x, y, m, ya, yb):
    """Straight line through (x,y) with pixel slope m, between heights ya and yb."""
    return ((x + (ya - y) / m, ya), (x + (yb - y) / m, yb))


def Lx(x, y, m, xa, xb):
    """Straight line through (x,y) with pixel slope m, between x positions xa and xb."""
    return ((xa, y + (xa - x) * m), (xb, y + (xb - x) * m))


def dl(f, l, color=GREY, width=2.8):
    f.line(*l[0], *l[1], color, width)


def lab(f, x, y, s, color=INK, size=12.5, anchor="start"):
    f.label(x, y, s, color, size, anchor)


def endlab(f, l, s, color, end=1, dx=6, dy=4, anchor="start", size=12.5):
    x, y = l[end]
    f.label(x + dx, y + dy, s, color, size, anchor)


def polyd(f, pts, color=RED, width=2.8):
    d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    f.path(d, color, width)


def poly_hits(pts, line):
    (x1, y1), (x2, y2) = line

    def s(p):
        return (x2 - x1) * (p[1] - y1) - (y2 - y1) * (p[0] - x1)
    out = []
    for p, q in zip(pts, pts[1:]):
        sp, sq = s(p), s(q)
        if sp * sq < 0:
            t = sp / (sp - sq)
            out.append((p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1])))
    return out


def poly_y_at(pts, x):
    for p, q in zip(pts, pts[1:]):
        if p[0] != q[0] and min(p[0], q[0]) <= x <= max(p[0], q[0]):
            return p[1] + (x - p[0]) * (q[1] - p[1]) / (q[0] - p[0])
    raise ValueError("x outside curve")


def on_line(l, p, tol=0.01):
    assert abs(Fig.y_at(l, p[0]) - p[1]) < tol, "point not on line"
    return p


def mac(w=420):
    f = Fig(w=w)
    f.axes("Real output (Y)", "Average price level")
    return f


def axis_arrow_x(f, x1, x2, dy=13):
    d = 12 if x2 > x1 else -12
    f.arrow(x1 + d, f.Y0 + dy, x2 - d, f.Y0 + dy, PURPLE, 1.8, 7)


def axis_arrow_y(f, y1, y2, dx=34):
    d = 6 if y2 > y1 else -6
    f.arrow(f.X0 - dx, y1 + d, f.X0 - dx, y2 - d, PURPLE, 1.8, 7)


def dbl(f, x1, y1, x2, y2, color=PURPLE, width=1.8, head=7):
    """Double-headed arrow (two arrows leaving the midpoint)."""
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    f.arrow(mx, my, x1, y1, color, width, head)
    f.arrow(mx, my, x2, y2, color, width, head)


def vline(f, x, y_from=None, y_to=None, color=RED, width=2.8):
    f.line(x, f.Y0 if y_from is None else y_from, x, 48 if y_to is None else y_to, color, width)


def vpoint(l, x):
    """Point on straight line l at horizontal position x."""
    return (x, Fig.y_at(l, x))


def kas_pts(f, yP, xa, xf, b, ytop, n=48):
    """Keynesian AS: flat from the axis to xa, quarter-ellipse to (xf, yP-b),
    then vertical to ytop."""
    pts = [(f.X0, yP), (xa, yP)]
    a = xf - xa
    for i in range(1, n + 1):
        t = math.radians(90.0 * i / n)
        pts.append((xa + a * math.sin(t), (yP - b) + b * math.cos(t)))
    pts.append((xf, ytop))
    return pts


def hit(pts, line):
    h = poly_hits(pts, line)
    assert len(h) == 1, h
    return h[0]


# Keynesian AS constants
KP, KA, KF, KB, KT = 225, 232, 315, 100, 48


def kas(f):
    return kas_pts(f, KP, KA, KF, KB, KT)


def ppc_pt(f, a, b, t):
    return (f.X0 + a * math.sin(math.radians(t)), f.Y0 - b * math.cos(math.radians(t)))


def ppc_pts(f, a, b, n=60):
    return [ppc_pt(f, a, b, 90.0 * i / n) for i in range(n + 1)]


# multi-panel helpers
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


# =============================================================== CHAPTER 13
def fig_13_1():
    f = Fig(w=520, h=390)

    def box(x, y, w, h, s):
        f.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="#fdeaea" '
              f'stroke="{RED}" stroke-width="2.2"/>')
        f.text(x + w / 2, y + h / 2 + 5, s, 14, "middle", INK, "600")
    box(190, 34, 140, 50, "Households")
    box(190, 296, 140, 50, "Firms")
    f.arrow(232, 298, 232, 88, PURPLE, 2.4)
    f.text(224, 178, "Goods and", 11.5, "end")
    f.text(224, 194, "services (3)", 11.5, "end")
    f.text(224, 212, "output method", 10.5, "end", GREY, italic=True)
    f.arrow(288, 86, 288, 294, PURPLE, 2.4)
    f.text(296, 178, "Factors of", 11.5)
    f.text(296, 194, "production (1)", 11.5)
    f.flow([(188, 59), (56, 59), (56, 321), (188, 321)], RED, 2.4)
    f.text(44, 190, "Expenditure on goods and services (4)", 11.5, "middle", INK, rotate=-90)
    f.text(28, 190, "expenditure method", 10.5, "middle", GREY, rotate=-90, italic=True)
    f.flow([(332, 321), (464, 321), (464, 59), (332, 59)], RED, 2.4)
    f.text(478, 190, "Wages, rent, interest and profits (2)", 11.5, "middle", INK, rotate=90)
    f.text(494, 190, "income method", 10.5, "middle", GREY, rotate=90, italic=True)
    f.line(150, 372, 178, 372, RED, 2.4)
    f.text(184, 376, "Money flows", 11, "start", GREY)
    f.line(290, 372, 318, 372, PURPLE, 2.4)
    f.text(324, 376, "Real flows", 11, "start", GREY)
    return f


def fig_13_2():
    f = Fig().scale(10, 300)
    f.axes("Time", "Real GDP")
    g = lambda t: 120 + 7 * t + 50 * math.cos(2 * math.pi * (t - 3.6) / 5)
    ts = [0.2 + i * 0.05 for i in range(int((9.6 - 0.2) / 0.05) + 1)]
    pts = [f.pt(t, g(t)) for t in ts]

    def ext(lo, hi, fn):
        c = [t for t in ts if lo <= t <= hi]
        return fn(c, key=g)
    t_pk1, t_tr2, t_pk2 = ext(3, 4.5, max), ext(5, 7, min), ext(7.5, 9.5, max)
    t_tr1 = ext(0.5, 2, min)
    P = lambda t: f.pt(t, g(t))
    for t in (t_pk1, t_tr2, t_pk2):
        x, y = P(t)
        f.line(x, y, x, f.Y0, TEAL, 1.5, "5 4", "butt")
    polyd(f, pts, RED)
    for t in (t_pk1, t_tr2, t_pk2):
        f.dot(*P(t), 3.6, INK)
    ya = f.Y0 - 26
    x1, x2, x3 = P(t_pk1)[0], P(t_tr2)[0], P(t_pk2)[0]
    dbl(f, x1 + 4, ya, x2 - 4, ya)
    dbl(f, x2 + 4, ya, x3 - 4, ya)
    f.text((x1 + x2) / 2, ya - 8, "Contraction", 11.5, "middle")
    f.text((x2 + x3) / 2, ya - 8, "Expansion", 11.5, "middle")
    # phase labels
    f.text(P(t_pk1)[0], P(t_pk1)[1] - 12, "Boom", 12.5, "middle", INK, "600")
    tx, ty = P(t_tr2)
    f.text(tx - 8, ty + 20, "Trough", 12.5, "end", INK, "600")
    tm = (t_pk1 + t_tr2) / 2
    f.text(P(tm)[0] + 16, P(tm)[1] - 10, "Recession", 12.5, "start", INK, "600")
    tr = t_tr1 + 0.62 * (t_pk1 - t_tr1)
    f.text(P(tr)[0] - 12, P(tr)[1] - 2, "Recovery", 12.5, "end", INK, "600")
    return f


def fig_13_3():
    f = Fig(x1=312).scale(10, 330)
    f.axes("Time", "Real GDP")
    tr = lambda t: 90 + 18 * t
    act = lambda t: tr(t) - 55 * math.sin(2 * math.pi * (t - 1.0) / 8)
    tsA = [0.0 + i * 0.05 for i in range(int(9.7 / 0.05) + 1)]
    pts = [f.pt(t, act(t)) for t in tsA]
    # trend line with arrowhead
    a, b = f.pt(0, tr(0)), f.pt(9.9, tr(9.9))
    f.line(a[0], a[1], b[0] - 6, b[1] + 2.0, INK, 2.2)
    ang = math.degrees(math.atan2(b[1] - a[1], b[0] - a[0]))
    f.arrowhead(b[0], b[1], ang, INK, 9)
    polyd(f, pts, RED)
    tA, tB = 3.0, 7.0
    for t, s, dy in ((tA, "A", 20), (tB, "B", -10)):
        x, ya_ = f.pt(t, act(t))
        _, yt = f.pt(t, tr(t))
        f.dot(x, ya_, 3.4, INK)
        dbl(f, x, ya_ + (-6 if ya_ > yt else 6), x, yt + (6 if ya_ > yt else -6))
        f.text(x, ya_ + dy, s, 13, "middle", INK, "600")
    f.text(b[0] + 6, b[1] - 12, "Long-term", 11.5, "start")
    f.text(b[0] + 6, b[1] + 2, "trend", 11.5, "start")
    e = pts[-1]
    f.text(e[0] + 8, e[1] + 4, "Actual", 11.5, "start")
    f.text(e[0] + 8, e[1] + 18, "output", 11.5, "start")
    return f, (tA, tB)


# =============================================================== CHAPTER 14
def ad_line():
    return Lx(215, 200, AM, 104, 322)


def fig_14_1a():
    f = mac()
    l = ad_line()
    dl(f, l)
    endlab(f, l, "AD", GREY, 1, 8, 12)
    return f


def fig_14_1b():
    f = Fig()
    f.axes("Quantity (units)", "Price ($)")
    l = ad_line()
    dl(f, l)
    endlab(f, l, "D", GREY, 1, 8, 12)
    return f


def fig_14_2():
    f = Fig()
    f.axes("Real output = national income = Y", "Average price level ($)")
    l = ad_line()
    y1, y2 = 120, 215
    p1, p2 = vpoint(l, Fig.x_at(l, y1)), vpoint(l, Fig.x_at(l, y2))
    f.guide(*p1, sub("Y", 1), sub("PL", 1))
    f.guide(*p2, sub("Y", 2), sub("PL", 2))
    dl(f, l)
    f.dot(*p1, 3.6, INK)
    f.dot(*p2, 3.6, INK)
    axis_arrow_y(f, p1[1], p2[1], 44)
    axis_arrow_x(f, p1[0], p2[0])
    lab(f, 384, 68, "AD = C + I + G + (X" + MINUS + "M)", INK, 12, "end")
    endlab(f, l, "AD", GREY, 1, 8, 12)
    return f


def fig_14_3():
    f = mac()
    ls = {}
    for k, x, xa, xb in (("3", 170, 92, 250), ("1", 230, 110, 310), ("2", 290, 170, 370)):
        ls[k] = Lx(x, 190, AM, xa, xb)
        dl(f, ls[k])
        endlab(f, ls[k], "AD" + f'<tspan font-size="70%" dy="3">{k}</tspan>', GREY, 1, 0, 17, "middle")
    f.hshift(ls["1"], ls["2"], 150)
    f.hshift(ls["1"], ls["3"], 150)
    return f, ls


def fig_14_4():
    f = Fig().scale(10, 10)
    f.axes("Level of investment (I)", "Interest rate (i, %)")
    line = (f.pt(1, 9), f.pt(9, 1))
    A, B = f.pt(3, 7), f.pt(6, 4)
    on_line(line, A)
    on_line(line, B)
    f.guide(*A, sub("I", 1), "7%")
    f.guide(*B, sub("I", 2), "4%")
    f.line(*line[0], *line[1], RED, 2.8)
    f.dot(*A, 3.6, INK)
    f.dot(*B, 3.6, INK)
    axis_arrow_y(f, A[1], B[1], 42)
    axis_arrow_x(f, A[0], B[0])
    lab(f, line[1][0] + 8, line[1][1] + 4, "I", INK, 13)
    return f


# =============================================================== CHAPTER 15
def sras_curve(f):
    pts = []
    for i in range(0, 81):
        u = i / 80.0
        h = 30 + 205 * u ** 2.6
        pts.append((118 + 192 * u, 292 - h))
    return pts


def fig_15_1():
    f = mac()
    pts = sras_curve(f)
    xs = (205, 288)
    P = [(x, poly_y_at(pts, x)) for x in xs]
    f.guide(*P[0], sub("Y", 1), sub("P", 1))
    f.guide(*P[1], sub("Y", 2), sub("P", 2))
    polyd(f, pts, RED)
    for p in P:
        f.dot(*p, 3.6, INK)
    axis_arrow_y(f, P[0][1], P[1][1], 44)
    axis_arrow_x(f, P[0][0], P[1][0])
    lab(f, pts[-1][0] + 6, pts[-1][1] + 8, "SRAS", RED, 12.5)
    lab(f, 92, 294, "Spare capacity:", GREY, 11)
    lab(f, 92, 307, "prices rise slowly", GREY, 11)
    lab(f, 92, 66, "Near full capacity:", GREY, 11)
    lab(f, 92, 79, "prices rise sharply", GREY, 11)
    return f


def fig_15_2():
    f = mac()
    l = L(230, 190, SM, 292, 100)
    y1, y2 = 244, 126
    P1, P2 = vpoint(l, Fig.x_at(l, y1)), vpoint(l, Fig.x_at(l, y2))
    f.guide(*P1, sub("Y", 1), sub("P", 1))
    f.guide(*P2, sub("Y", 2), sub("P", 2))
    dl(f, l, RED)
    f.dot(*P1, 3.6, INK)
    f.dot(*P2, 3.6, INK)
    axis_arrow_y(f, P1[1], P2[1], 44)
    axis_arrow_x(f, P1[0], P2[0])
    endlab(f, l, "SRAS", RED, 1, 6, 4)
    return f


def fig_15_3():
    f = mac()
    ls = {}
    for k, x, xa, xb in (("3", 185, 96, 262), ("1", 235, 146, 312), ("2", 285, 196, 362)):
        ls[k] = Lx(x, 190, SM, xa, xb)
    for k in "312":
        dl(f, ls[k], RED)
        endlab(f, ls[k], "SRAS" + f'<tspan font-size="70%" dy="3">{k}</tspan>', RED, 1, 0, -9, "middle")
    f.hshift(ls["1"], ls["2"], 236)
    f.hshift(ls["1"], ls["3"], 236)
    return f, ls


def fig_15_4():
    f = mac()
    sr = L(230, 190, SM, 292, 100)
    ad = L(230, 190, AM, 76, 274)
    dl(f, ad)
    dl(f, sr, RED)
    f.equilibrium(sr, ad, "Y", "PL")
    endlab(f, sr, "SRAS", RED, 1, 6, 4)
    endlab(f, ad, "AD", GREY, 1, 8, 12)
    return f


def fig_15_5():
    f = mac()
    xf = 230
    ys = (215, 120)
    for i, y in enumerate(ys, 1):
        f.guide(xf, y, "Y" + "<tspan font-size='70%' dy='3'>f</tspan>" if i == 1 else None,
                sub("P", i), to_x=(i == 1))
    vline(f, xf, f.Y0, 48)
    for y in ys:
        f.dot(xf, y, 3.6, INK)
    lab(f, xf, 38, "LRAS", RED, 12.5, "middle")
    axis_arrow_y(f, ys[0], ys[1], 44)
    return f


def fig_15_6():
    f = Fig()
    f.axes("Real output (Y)", "Average price level")
    pts = kas(f)
    # dashed guide at Yf from the top of the bend
    f.line(KF, KP - KB, KF, f.Y0, TEAL, 1.5, "5 4", "butt")
    f.text(KF, f.Y0 + 18, "Y<tspan font-size='70%' dy='3'>f</tspan>", 11.5, "middle")
    polyd(f, pts, RED)
    lab(f, KF, 38, "AS", RED, 12.5, "middle")
    lab(f, 90, KP + 20, "(1) Perfectly elastic", INK, 11.5)
    lab(f, 262, 160, "(2) Upward", INK, 11.5, "end")
    lab(f, 262, 173, "sloping", INK, 11.5, "end")
    lab(f, KF + 10, 92, "(3) Perfectly", INK, 11.5)
    lab(f, KF + 10, 105, "inelastic", INK, 11.5)
    return f


def fig_15_7():
    f = Fig(w=860, h=380)
    # (a)
    setp(f, 78, 390)
    axes2(f, "Real output (Y)", "Average price level", "(a) Keynesian view")
    yP, b, top = 240, 100, 76
    a1 = kas_pts(f, yP, 172, 248, b, top)
    a2 = kas_pts(f, yP, 222, 298, b, top)
    polyd(f, a1)
    polyd(f, a2)
    f.text(248 - 4, top - 8, "AS" + '<tspan font-size="70%" dy="3">1</tspan>', 12.5, "end", RED)
    f.text(298 + 4, top - 8, "AS" + '<tspan font-size="70%" dy="3">2</tspan>', 12.5, "start", RED)
    f.arrow(248 + 5, 108, 298 - 5, 108, PURPLE)
    # (b)
    setp(f, 498, 810)
    axes2(f, "Real output (Y)", "Average price level", "(b) New classical view")
    x1, x2 = 620, 690
    for x, k in ((x1, 1), (x2, 2)):
        f.line(x, f.Y0, x, top, RED, 2.8)
    f.text(x1 - 4, top - 8, "LRAS" + '<tspan font-size="70%" dy="3">1</tspan>', 12.5, "end", RED)
    f.text(x2 + 4, top - 8, "LRAS" + '<tspan font-size="70%" dy="3">2</tspan>', 12.5, "start", RED)
    f.arrow(x1 + 5, 150, x2 - 5, 150, PURPLE)
    return f


def fig_15_8():
    f = Fig()
    f.axes("Capital goods", "Consumer goods and services")
    a1, b1, k = 150, 140, 1.35
    a2, b2 = a1 * k, b1 * k
    polyd(f, ppc_pts(f, a1, b1), GREY)
    polyd(f, ppc_pts(f, a2, b2), RED)
    for t in (24, 44, 64):
        p1, p2 = ppc_pt(f, a1, b1, t), ppc_pt(f, a2, b2, t)
        # radial from origin: both end points lie on the two curves
        d = math.hypot(p2[0] - p1[0], p2[1] - p1[1])
        ux, uy = (p2[0] - p1[0]) / d, (p2[1] - p1[1]) / d
        f.arrow(p1[0] + 5 * ux, p1[1] + 5 * uy, p2[0] - 5 * ux, p2[1] - 5 * uy, PURPLE)
    q = ppc_pt(f, a1, b1, 80)
    lab(f, q[0] - 10, q[1] - 22, "PPC" + sub("", 1), GREY, 12.5, "end")
    q = ppc_pt(f, a2, b2, 82)
    lab(f, q[0] + 8, q[1] - 6, "PPC" + sub("", 2), RED, 12.5)
    return f


# =============================================================== CHAPTER 16
def fig_16_1():
    f = mac()
    sr = L(230, 190, SM, 292, 100)
    ad = L(230, 190, AM, 76, 274)
    dl(f, ad)
    dl(f, sr, RED)
    f.equilibrium(sr, ad, "Y", "P")
    endlab(f, sr, "SRAS", RED, 1, 6, 4)
    endlab(f, ad, "AD", GREY, 1, 8, 12)
    return f


YF = 230
E1 = (230, 190)


def nc_base(f, sras=True, ad1=True):
    """LRAS + optional SRAS1 and AD1 all through E1=(Yf, P1)."""
    out = {}
    if sras:
        out["sr"] = L(230, 190, SM, 292, 96)
    if ad1:
        out["ad1"] = L(230, 190, AM, 82, 262)
    return out


def yf_label(x=YF):
    return "Y<tspan font-size='70%' dy='3'>f</tspan>"


def fig_16_2():
    f = mac()
    ad = L(230, 190, AM, 82, 262)
    f.guide(YF, 190, yf_label(), sub("P", 1))
    dl(f, ad)
    vline(f, YF, f.Y0, 48)
    f.dot(*vpoint(ad, YF), 3.6, INK)
    lab(f, YF, 38, "LRAS", RED, 12.5, "middle")
    endlab(f, ad, "AD" + sub("", 1), GREY, 1, 8, 12)
    return f


def fig_16_3():
    f = mac()
    ad1 = L(230, 190, AM, 82, 262)
    ad2 = L(310, 190, AM, 82, 262)
    p1, p2 = vpoint(ad1, YF), vpoint(ad2, YF)
    f.guide(*p1, yf_label(), sub("P", 1))
    f.guide(*p2, None, sub("P", 2), to_x=False)
    dl(f, ad1)
    dl(f, ad2)
    vline(f, YF, f.Y0, 48)
    f.dot(*p1, 3.6, INK)
    f.dot(*p2, 3.6, INK)
    f.hshift(ad1, ad2, 92)
    f.hshift(ad1, ad2, 225)
    lab(f, YF, 38, "LRAS", RED, 12.5, "middle")
    endlab(f, ad1, "AD" + sub("", 1), GREY, 1, 0, 17, "middle")
    endlab(f, ad2, "AD" + sub("", 2), GREY, 1, 0, 17, "middle")
    return f


def fig_16_4():
    f = mac()
    sr = L(230, 190, SM, 292, 96)
    ad1 = L(230, 190, AM, 82, 262)
    ad2 = L(310, 190, AM, 82, 262)
    e1 = f.intersect(sr, ad1)
    e2 = f.intersect(sr, ad2)
    assert abs(e1[0] - YF) < 0.01
    f.guide(*e1, yf_label(), sub("P", 1))
    f.guide(*e2, sub("Y", 1), sub("P", 2))
    dl(f, ad1)
    dl(f, ad2)
    dl(f, sr, RED)
    vline(f, YF, f.Y0, 48)
    f.dot(*e1, 3.6, INK)
    f.dot(*e2, 3.6, INK)
    f.hshift(ad1, ad2, 100)
    f.hshift(ad1, ad2, 250)
    ya = f.Y0 - 14
    dbl(f, e1[0] + 3, ya, e2[0] - 3, ya, PURPLE, 1.8, 6)
    lab(f, e2[0] + 8, ya + 4, "Inflationary gap", INK, 11.5)
    lab(f, YF, 38, "LRAS", RED, 12.5, "middle")
    endlab(f, sr, "SRAS", RED, 1, 6, 4)
    endlab(f, ad1, "AD" + sub("", 1), GREY, 1, 0, 17, "middle")
    endlab(f, ad2, "AD" + sub("", 2), GREY, 1, 0, 17, "middle")
    return f, (e1, e2)


def fig_16_5():
    f = mac()
    sr1 = L(230, 190, SM, 292, 96)
    ad1 = L(230, 190, AM, 82, 262)
    ad2 = L(310, 190, AM, 82, 262)
    e1 = f.intersect(sr1, ad1)
    e2 = f.intersect(sr1, ad2)
    e3 = vpoint(ad2, YF)
    sr2 = L(e3[0], e3[1], SM, 220, 60)
    on_line(sr2, e3)
    f.guide(*e1, yf_label(), sub("P", 1))
    f.guide(*e2, sub("Y", 1), sub("P", 2))
    f.guide(*e3, None, sub("P", 3), to_x=False)
    dl(f, ad1)
    dl(f, ad2)
    dl(f, sr1, RED)
    dl(f, sr2, RED)
    vline(f, YF, f.Y0, 48)
    for e in (e1, e2, e3):
        f.dot(*e, 3.6, INK)
    f.hshift(ad1, ad2, 100)
    f.hshift(ad1, ad2, 250)
    f.hshift(sr1, sr2, 225)
    lab(f, YF, 38, "LRAS", RED, 12.5, "middle")
    endlab(f, sr1, "SRAS" + sub("", 1), RED, 1, 6, 4)
    endlab(f, sr2, "SRAS" + sub("", 2), RED, 1, 6, -2)
    endlab(f, ad1, "AD" + sub("", 1), GREY, 1, 0, 17, "middle")
    endlab(f, ad2, "AD" + sub("", 2), GREY, 1, 0, 17, "middle")
    return f, (e1, e2, e3)


def fig_16_6():
    f = mac()
    sr = L(230, 190, SM, 292, 96)
    ad1 = L(230, 190, AM, 82, 262)
    ad2 = L(166, 190, AM, 125, 262)
    e1 = f.intersect(sr, ad1)
    e2 = f.intersect(sr, ad2)
    f.guide(*e1, yf_label(), sub("P", 1))
    f.guide(*e2, sub("Y", 1), sub("P", 2))
    dl(f, ad1)
    dl(f, ad2)
    dl(f, sr, RED)
    vline(f, YF, f.Y0, 48)
    f.dot(*e1, 3.6, INK)
    f.dot(*e2, 3.6, INK)
    f.hshift(ad1, ad2, 150)
    f.hshift(ad1, ad2, 252)
    ya = f.Y0 - 14
    dbl(f, e2[0] + 3, ya, e1[0] - 3, ya, PURPLE, 1.8, 6)
    lab(f, e1[0] + 8, ya + 4, "Deflationary gap", INK, 11.5)
    lab(f, YF, 38, "LRAS", RED, 12.5, "middle")
    endlab(f, sr, "SRAS", RED, 1, 6, 4)
    endlab(f, ad1, "AD" + sub("", 1), GREY, 1, 0, 17, "middle")
    endlab(f, ad2, "AD" + sub("", 2), GREY, 1, 0, 17, "middle")
    return f, (e1, e2)


def fig_16_7():
    f = mac()
    sr1 = L(230, 190, SM, 292, 96)
    ad1 = L(230, 190, AM, 82, 262)
    ad2 = L(166, 190, AM, 125, 262)
    e1 = f.intersect(sr1, ad1)
    e2 = f.intersect(sr1, ad2)
    e3 = vpoint(ad2, YF)
    sr2 = L(e3[0], e3[1], SM, 300, 150)
    on_line(sr2, e3)
    f.guide(*e1, yf_label(), sub("P", 1))
    f.guide(*e2, sub("Y", 1), sub("P", 2))
    f.guide(*e3, None, sub("P", 3), to_x=False)
    dl(f, ad1)
    dl(f, ad2)
    dl(f, sr1, RED)
    dl(f, sr2, RED)
    vline(f, YF, f.Y0, 48)
    for e in (e1, e2, e3):
        f.dot(*e, 3.6, INK)
    f.hshift(ad1, ad2, 150)
    f.hshift(sr1, sr2, 290)
    lab(f, YF, 38, "LRAS", RED, 12.5, "middle")
    endlab(f, sr1, "SRAS" + sub("", 1), RED, 1, 6, 4)
    endlab(f, sr2, "SRAS" + sub("", 2), RED, 1, 6, 4)
    endlab(f, ad1, "AD" + sub("", 1), GREY, 1, 0, 17, "middle")
    endlab(f, ad2, "AD" + sub("", 2), GREY, 1, 0, 17, "middle")
    return f, (e1, e2, e3)


def fig_16_8():
    f = mac()
    pts = kas(f)
    ad = L(170, KP, 1.5, 102, 290)
    e = hit(pts, ad)
    assert abs(e[1] - KP) < 0.01
    f.line(e[0], e[1], e[0], 100, TEAL, 1.5, "5 4", "butt")
    f.guide(*e, "Y", "P")
    f.line(KF, KP - KB, KF, f.Y0, TEAL, 1.5, "5 4", "butt")
    f.text(KF, f.Y0 + 18, yf_label(), 11.5, "middle")
    dl(f, ad)
    polyd(f, pts, RED)
    f.dot(*e, 3.6, INK)
    dbl(f, e[0] + 3, 108, KF - 3, 108, PURPLE, 1.8, 7)
    lab(f, (e[0] + KF) / 2, 95, "Deflationary gap", INK, 11.5, "middle")
    lab(f, KF, 38, "LRAS", RED, 12.5, "middle")
    endlab(f, ad, "AD", GREY, 1, 8, 12)
    return f, e


def fig_16_9():
    f = Fig()
    f.axes("Capital goods", "Consumer goods and services")
    a, b = 250, 240
    curve = ppc_pts(f, a, b)
    A = (170, 230)
    ray = (A, (A[0] + 50, A[1] - 50))
    B = None
    for p in poly_hits(curve, ray):
        if p[0] > A[0]:
            B = p
    assert B
    polyd(f, curve, RED)
    f.line(A[0] + 6, A[1] - 6, B[0] - 6, B[1] + 6, PURPLE, 1.8, "4 3", "butt")
    f.arrowhead(B[0] - 3, B[1] + 3, -45, PURPLE, 8)
    f.arrowhead(A[0] + 3, A[1] - 3, 135, PURPLE, 8)
    f.dot(*A, 3.6, INK)
    f.dot(*B, 3.6, INK)
    lab(f, A[0] - 8, A[1] + 16, "A", INK, 13, "end")
    lab(f, B[0] + 10, B[1] - 4, "B", INK, 13)
    mx, my = (A[0] + B[0]) / 2, (A[1] + B[1]) / 2
    lab(f, mx - 14, my - 10, "Output gap", INK, 11.5, "end")
    lab(f, A[0] - 8, A[1] + 30, "actual output", GREY, 10.5, "end")
    lab(f, B[0] + 10, B[1] + 10, "potential output", GREY, 10.5)
    return f, (A, B)


def fig_16_10():
    f = mac()
    pts = kas(f)
    ad1 = L(168, KP, 1.5, 110, 285)
    ad2 = L(222, KP, 1.5, 110, 285)
    e1, e2 = hit(pts, ad1), hit(pts, ad2)
    f.guide(*e1, sub("Y", 1), "P")
    f.guide(*e2, sub("Y", 2), None, to_y=False)
    f.line(KF, KP - KB, KF, f.Y0, TEAL, 1.5, "5 4", "butt")
    f.text(KF, f.Y0 + 18, yf_label(), 11.5, "middle")
    dl(f, ad1)
    dl(f, ad2)
    polyd(f, pts, RED)
    f.dot(*e1, 3.6, INK)
    f.dot(*e2, 3.6, INK)
    f.hshift(ad1, ad2, 112)
    f.hshift(ad1, ad2, 170)
    lab(f, KF, 38, "LRAS", RED, 12.5, "middle")
    endlab(f, ad1, "AD" + sub("", 1), GREY, 1, 0, 17, "middle")
    endlab(f, ad2, "AD" + sub("", 2), GREY, 1, 0, 17, "middle")
    return f, (e1, e2)


def fig_16_11():
    f = mac()
    pts = kas(f)
    ad2 = L(222, KP, 1.5, 110, 285)
    ad3 = L(302, KP, 1.5, 110, 285)
    e2, e3 = hit(pts, ad2), hit(pts, ad3)
    f.guide(*e2, sub("Y", 2), sub("P", 1))
    f.guide(*e3, sub("Y", 3), sub("P", 2))
    f.line(KF, KP - KB, KF, f.Y0, TEAL, 1.5, "5 4", "butt")
    f.text(KF + 6, f.Y0 + 18, yf_label(), 11.5, "start")
    dl(f, ad2)
    dl(f, ad3)
    polyd(f, pts, RED)
    f.dot(*e2, 3.6, INK)
    f.dot(*e3, 3.6, INK)
    f.hshift(ad2, ad3, 112)
    f.hshift(ad2, ad3, 165)
    lab(f, KF, 38, "LRAS", RED, 12.5, "middle")
    endlab(f, ad2, "AD" + sub("", 2), GREY, 1, 0, 17, "middle")
    endlab(f, ad3, "AD" + sub("", 3), GREY, 1, 0, 17, "middle")
    return f, (e2, e3)


def fig_16_12():
    f = mac()
    xf = 270
    pts = kas_pts(f, KP, 190, xf, KB, KT)
    ad1 = Lx(xf, 112, 1.1, 232, 384)
    ad2 = Lx(xf, 62, 1.1, 261, 384)
    e1, e2 = hit(pts, ad1), hit(pts, ad2)
    assert abs(e1[0] - xf) < 0.01 and abs(e2[0] - xf) < 0.01
    f.guide(*e1, yf_label(), sub("P", 1))
    f.guide(*e2, None, sub("P", 2), to_x=False)
    dl(f, ad1)
    dl(f, ad2)
    polyd(f, pts, RED)
    f.dot(*e1, 3.6, INK)
    f.dot(*e2, 3.6, INK)
    f.hshift(ad1, ad2, 128)
    f.hshift(ad1, ad2, 165)
    lab(f, xf, 38, "LRAS", RED, 12.5, "middle")
    endlab(f, ad1, "AD" + sub("", 1), GREY, 1, -6, 17, "middle")
    endlab(f, ad2, "AD" + sub("", 2), GREY, 1, -6, 17, "middle")
    return f, (e1, e2)


# =============================================================== CHAPTER 17
def demand_pull(note):
    f = mac()
    sr = L(230, 200, SM, 293, 106)
    a1x = 205
    y_on = Fig.y_at(sr, a1x)
    ad1 = Lx(a1x, y_on, AM, 96, 268)
    ad2 = Lx(a1x + 80, y_on, AM, 176, 348)
    e1, e2 = f.intersect(sr, ad1), f.intersect(sr, ad2)
    f.guide(*e1, sub("Y", 1), sub("P", 1))
    f.guide(*e2, sub("Y", 2), sub("P", 2))
    dl(f, ad1)
    dl(f, ad2)
    dl(f, sr, RED)
    f.dot(*e1, 3.6, INK)
    f.dot(*e2, 3.6, INK)
    f.hshift(ad1, ad2, 138)
    f.hshift(ad1, ad2, 172)
    axis_arrow_y(f, e1[1], e2[1], 44)
    axis_arrow_x(f, e1[0], e2[0])
    endlab(f, sr, "SRAS", RED, 1, 6, 4)
    endlab(f, ad1, "AD" + sub("", 1), GREY, 1, 0, 17, "middle")
    endlab(f, ad2, "AD" + sub("", 2), GREY, 1, 0, 17, "middle")
    lab(f, 384, 44, note, GREY, 11, "end")
    return f


def fig_17_1():
    return demand_pull("Policy: higher G or lower taxes")


def fig_17_2():
    return demand_pull("Policy: lower interest rates")


def fig_17_3():
    f = Fig(w=560, h=520)
    RES, LOAN = "#e9ebf5", "#fdeaea"
    scale = 1.2   # px per $1,000
    dep = [200.0, 150.0, 112.5]
    resv = [d * 0.25 for d in dep]
    loan = [d * 0.75 for d in dep]
    xr = 290.0                     # right edge shared by every bar
    y = 44
    right = 320
    fmt = lambda v: f"${v * 1000:,.0f}"
    for i, d in enumerate(dep):
        w = d * scale
        x = xr - w
        # deposit box
        f.add(f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="30" rx="6" fill="#ffffff" '
              f'stroke="{INK}" stroke-width="1.8"/>')
        f.text(x + w / 2, y + 20, ("New deposit " if i == 0 else "Re-deposited ") + fmt(d),
               11.5 if i else 12, "middle", INK, "600")
        # arrow deposit -> bank bar (red = deposit)
        f.arrow(x + w / 2, y + 30, x + w / 2, y + 52, RED, 2.0, 7)
        yb = y + 52
        wr, wl = resv[i] * scale, loan[i] * scale
        f.add(f'<rect x="{x:.1f}" y="{yb}" width="{wr:.1f}" height="34" fill="{RES}" stroke="{INK}" stroke-width="1.6"/>')
        f.add(f'<rect x="{x + wr:.1f}" y="{yb}" width="{wl:.1f}" height="34" fill="{LOAN}" stroke="{INK}" stroke-width="1.6"/>')
        f.text(x + wr / 2, yb + 21, "25%", 11, "middle", INK)
        f.text(x + wr + wl / 2, yb + 21, "75%", 11, "middle", INK)
        # right-hand notes
        f.text(right, yb + 8, f"Round {i + 1}: bank keeps", 11.5, "start", INK, "600")
        f.text(right, yb + 22, f"{fmt(resv[i])} as reserve and", 11.5, "start")
        f.text(right, yb + 36, f"lends {fmt(loan[i])}", 11.5, "start")
        # arrow: loan -> next deposit
        lx = x + wr + wl / 2
        f.arrow(lx, yb + 34, lx, yb + 56, INK, 2.0, 7)
        y = yb + 56
    # continuation box
    w = (dep[-1] * 0.75) * scale
    x = xr - w
    f.add(f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="30" rx="6" fill="#ffffff" '
          f'stroke="{INK}" stroke-width="1.8" stroke-dasharray="5 4"/>')
    f.text(x + w / 2, y + 20, "and so on ...", 11.5, "middle", GREY)
    # summary
    ys = y + 62
    f.add(f'<rect x="30" y="{ys}" width="500" height="58" rx="8" fill="#f6f6f6" stroke="{GREY}" stroke-width="1.4"/>')
    f.text(280, ys + 22, "Money multiplier = 1 / reserve ratio = 1 / 0.25 = 4", 12, "middle", INK, "600")
    f.text(280, ys + 42, "$200,000 deposit supports $800,000 of deposits: $600,000 of new loans + $200,000 of reserves",
           11, "middle", INK)
    # legend
    yl = ys + 88
    f.arrow(36, yl, 70, yl, RED, 2.0, 7)
    f.text(76, yl + 4, "Deposit", 10.5, "start", GREY)
    f.arrow(140, yl, 174, yl, INK, 2.0, 7)
    f.text(180, yl + 4, "Loan is spent and re-deposited", 10.5, "start", GREY)
    f.add(f'<rect x="388" y="{yl - 6}" width="14" height="12" fill="{RES}" stroke="{INK}" stroke-width="1.2"/>')
    f.text(408, yl + 4, "Reserve", 10.5, "start", GREY)
    f.add(f'<rect x="464" y="{yl - 6}" width="14" height="12" fill="{LOAN}" stroke="{INK}" stroke-width="1.2"/>')
    f.text(484, yl + 4, "Loan", 10.5, "start", GREY)
    return f


def fig_17_4():
    f = Fig()
    f.axes("Quantity of loanable funds", "Interest rate")
    D = ((104, 66), (346, 286))
    x1, x2 = 185, 270
    p1, p2 = vpoint(D, x1), vpoint(D, x2)
    f.guide(*p1, None, sub("i", 1), to_x=False)
    f.guide(*p2, None, sub("i", 2), to_x=False)
    dl(f, D, GREY)
    for x, k in ((x1, 1), (x2, 2)):
        vline(f, x, f.Y0, 54)
        lab(f, x, 46, "S" + sub("", k), RED, 12.5, "middle")
    f.dot(*p1, 3.6, INK)
    f.dot(*p2, 3.6, INK)
    lab(f, D[1][0] + 8, D[1][1] + 4, "D", GREY, 12.5)
    f.text((x1 + x2) / 2, 236, "Buying", 11.5, "middle")
    f.text((x1 + x2) / 2, 249, "securities", 11.5, "middle")
    f.arrow(x1 + 5, 259, x2 - 5, 259, PURPLE)
    f.text((x1 + x2) / 2, 279, "Selling", 11.5, "middle")
    f.text((x1 + x2) / 2, 292, "securities", 11.5, "middle")
    f.arrow(x2 - 5, 302, x1 + 5, 302, PURPLE)
    return f, (p1, p2)


def fig_17_5():
    f = Fig()
    f.axes("Quantity of money", "Nominal interest rate")
    D = ((105, 66), (345, 270))
    x1, x2 = 170, 270
    p1, p2 = vpoint(D, x1), vpoint(D, x2)
    f.guide(*p1, sub("Q", 1), sub("i", 1))
    f.guide(*p2, sub("Q", 2), sub("i", 2))
    dl(f, D, RED)
    f.dot(*p1, 3.6, INK)
    f.dot(*p2, 3.6, INK)
    axis_arrow_y(f, p1[1], p2[1], 44)
    axis_arrow_x(f, p1[0], p2[0])
    lab(f, D[1][0] + 8, D[1][1] + 6, "D" + sub("", "M"), INK, 12.5)
    return f


def fig_17_6():
    f = Fig()
    f.axes("Quantity of money", "Nominal interest rate")
    xq = 230
    for y, k in ((125, 1), (215, 2)):
        f.guide(xq, y, None, sub("i", k), to_x=False)
    f.guide(xq, 215, "Q" + sub("", "M"), None, to_y=False)
    vline(f, xq, f.Y0, 54)
    for y in (125, 215):
        f.dot(xq, y, 3.6, INK)
    lab(f, xq, 46, "S" + sub("", "M"), RED, 12.5, "middle")
    return f


def fig_17_7():
    f = Fig()
    f.axes("Quantity of money", "Nominal interest rate")
    D = ((108, 60), (352, 274))
    xs = {"1": 165, "e": 232, "2": 299}
    P = {k: vpoint(D, x) for k, x in xs.items()}
    for k in ("1", "e", "2"):
        f.guide(*P[k], sub("Q", k), sub("i", k))
    dl(f, D, GREY)
    for k, x in xs.items():
        vline(f, x, f.Y0, 54)
        lab(f, x, 46, "S" + sub("", "M" + ("" if k == "e" else k)), RED, 12.5, "middle")
    for k in xs:
        f.dot(*P[k], 3.6, INK)
    ya = 262
    f.arrow(xs["e"] - 5, ya, xs["1"] + 5, ya, PURPLE)
    f.arrow(xs["e"] + 5, ya, xs["2"] - 5, ya, PURPLE)
    lab(f, D[1][0] + 8, D[1][1] + 6, "D" + sub("", "M"), GREY, 12.5)
    return f, P


# ------------------------------------------------------------------ build
def build():
    S = lambda k: '<sub>' + k + '</sub>'
    save("fig-13-1", fig_13_1(), "Figure 13.1: The circular flow of income (referenced diagram)",
         "Two-sector circular flow of income. Households and firms are joined by four numbered flows; flows 2, 3 and 4 are marked as the income, output and expenditure methods of measuring national income.",
         "A two-sector circular flow. Households supply factors of production to firms (1), and firms pay wages, rent, interest and profits back (2); firms supply goods and services to households (3), and households pay for them with expenditure (4). Flow (2) is what the <em>income method</em> measures, flow (3) the <em>output method</em> and flow (4) the <em>expenditure method</em>, so in theory all three give the same national income figure.")

    save("fig-13-2", fig_13_2(), "Figure 13.2: The standard business cycle",
         "A wave-shaped curve of real GDP against time with the phases recovery, boom, recession and trough labelled, and contraction and expansion marked by double-headed arrows.",
         "Real GDP against time follows a wave. Output rises through <em>recovery</em> to a <em>boom</em> (peak), falls through <em>recession</em> to a <em>trough</em>, then recovers again. The dashed lines mark the peak, the next trough and the next peak: the fall between the first two is the <em>contraction</em> and the rise between the last two is the <em>expansion</em>.")

    f, _ = fig_13_3()
    save("fig-13-3", f, "Figure 13.3: Long-term output and output gaps",
         "Real GDP against time: a wavy actual output curve oscillates around a rising straight long-term trend line. At point A actual output is below the trend and at point B above it, marked by double-headed arrows.",
         "Actual output (the wavy curve) fluctuates around the long-term trend, which is potential output. At point A actual output is below the trend, a <em>negative output gap</em> (spare capacity); at point B it is above the trend, a <em>positive output gap</em> (the economy is overheating). The double-headed arrows show the size of each gap.")

    save("fig-14-1a", fig_14_1a(), "Figure 14.1(a): Macroeconomic aggregate demand curve",
         "A downward-sloping aggregate demand curve, AD, with average price level on the vertical axis and real output on the horizontal axis.",
         "The aggregate demand (AD) curve slopes downward: a lower <em>average price level</em> is associated with a higher level of <em>real output</em> demanded. The axes measure the whole economy, not a single market.")
    save("fig-14-1b", fig_14_1b(), "Figure 14.1(b): Microeconomic demand curve (for comparison)",
         "A downward-sloping demand curve, D, with price on the vertical axis and quantity on the horizontal axis.",
         "For comparison, a microeconomic demand curve D slopes downward too, but its axes are the price of <em>one good</em> and the quantity of <em>that good</em>, not the average price level and real output.")
    save("fig-14-2", fig_14_2(), "Figure 14.2: The aggregate demand curve",
         "A downward-sloping AD curve labelled AD = C + I + G + (X - M). At price level PL1 real output demanded is Y1; at the lower PL2 it is the higher Y2.",
         "The AD curve, <em>AD = C + I + G + (X&minus;M)</em>. A fall in the average price level from PL<sub>1</sub> to PL<sub>2</sub> (purple arrow on the vertical axis) is a movement down along the curve, raising the real output demanded from Y<sub>1</sub> to Y<sub>2</sub> (purple arrow on the horizontal axis).")
    f, _ = fig_14_3()
    save("fig-14-3", f, "Figure 14.3: Shifts in aggregate demand",
         "Three parallel downward-sloping AD curves: AD3 on the left, AD1 in the middle and AD2 on the right, with purple arrows from AD1 to AD2 and from AD1 to AD3.",
         "The original curve is AD<sub>1</sub>. An increase in aggregate demand shifts the curve right to AD<sub>2</sub> (more real output demanded at every price level); a decrease shifts it left to AD<sub>3</sub>. The purple arrows show each shift from AD<sub>1</sub>.")
    save("fig-14-4", fig_14_4(), "Figure 14.4: The relationship between investment and the interest rate",
         "A downward-sloping investment curve I. When the interest rate falls from 7% to 4%, investment rises from I1 to I2.",
         "Investment falls as the interest rate rises. A fall in the interest rate from 7% to 4% is a movement <em>down along</em> the curve, from I<sub>1</sub> to I<sub>2</sub>: borrowing is cheaper and saving less attractive, so the level of investment increases. A rise in the rate would move the economy the other way, to lower investment.")

    save("fig-15-1", fig_15_1(), "Figure 15.1: The curved SRAS curve",
         "A short-run aggregate supply curve that gets steeper as output rises. Output Y1 has price level P1 and higher output Y2 has a much higher price level P2.",
         "The curved SRAS curve is fairly flat at low output, where there is spare capacity, and becomes steeper as the economy nears full capacity. The same rise in output from Y<sub>1</sub> to Y<sub>2</sub> now needs a bigger rise in the price level, from P<sub>1</sub> to P<sub>2</sub>, because scarce factors of production must be bid for.")
    save("fig-15-2", fig_15_2(), "Figure 15.2: The straight-line SRAS curve",
         "A straight upward-sloping SRAS curve. Output Y1 has price level P1 and higher output Y2 has higher price level P2.",
         "The simplified SRAS curve is drawn as a straight upward-sloping line: a rise in real output from Y<sub>1</sub> to Y<sub>2</sub> is accompanied by a rise in the average price level from P<sub>1</sub> to P<sub>2</sub>. This is the version used in most diagrams in the chapter.")
    f, _ = fig_15_3()
    save("fig-15-3", f, "Figure 15.3: Shifts in SRAS",
         "Three parallel upward-sloping SRAS curves: SRAS3 above and to the left, SRAS1 in the middle and SRAS2 below and to the right, with purple arrows from SRAS1 to each of the others.",
         "The original curve is SRAS<sub>1</sub>. Falling costs of production shift it right to SRAS<sub>2</sub> (an increase in SRAS: more output supplied at every price level). Rising costs shift it left to SRAS<sub>3</sub> (a decrease in SRAS). The purple arrows show each shift from SRAS<sub>1</sub>.")
    save("fig-15-4", fig_15_4(), "Figure 15.4: Short-run macroeconomic equilibrium",
         "A downward-sloping AD curve and an upward-sloping SRAS curve intersect at one point, giving equilibrium price level PL and equilibrium real output Y.",
         "Short-run macroeconomic equilibrium is where AD crosses SRAS. This fixes the equilibrium average price level PL and real output Y. At this point aggregate demand equals short-run aggregate supply, so there is no pressure for price or output to change.")
    save("fig-15-5", fig_15_5(), "Figure 15.5: New classical LRAS curve",
         "A vertical LRAS line at output Yf. Price levels P1 and P2 are marked with dashed lines, but output stays at Yf at both.",
         "In the new classical model LRAS is a vertical line at the full-employment output Y<sub>f</sub>. The price level can be P<sub>1</sub> or the higher P<sub>2</sub> (dashed horizontal lines), but real output stays at Y<sub>f</sub> whatever the price level.")
    save("fig-15-6", fig_15_6(), "Figure 15.6: Keynesian AS curve (three phases)",
         "A Keynesian aggregate supply curve that is horizontal at low output (1), curves upward (2), then becomes vertical at full-employment output Yf (3).",
         "The Keynesian AS curve has three phases. (1) At low output there is spare capacity, so AS is horizontal (perfectly elastic). (2) As the economy nears full employment factors become scarce and AS slopes upward. (3) At Y<sub>f</sub> no more can be produced, so AS is vertical (perfectly inelastic); this vertical section is the new classical LRAS.")
    save("fig-15-7", fig_15_7(), "Figure 15.7: A shift in the LRAS curve",
         "Two panels. (a) Keynesian: the whole hockey-stick AS curve shifts right from AS1 to AS2. (b) New classical: the vertical LRAS line shifts right from LRAS1 to LRAS2.",
         "An increase in the economy&rsquo;s productive potential shifts LRAS right. (a) In the Keynesian model the whole three-phase AS curve moves right from AS<sub>1</sub> to AS<sub>2</sub>, so full-employment output is higher. (b) In the new classical model the vertical LRAS line moves right from LRAS<sub>1</sub> to LRAS<sub>2</sub>.")
    save("fig-15-8", fig_15_8(), "Figure 15.8: An increase in productive potential and the PPC",
         "A production possibilities curve for capital goods and consumer goods and services shifts outward from PPC1 to PPC2, with three purple arrows between them.",
         "The PPC shifts outward from PPC<sub>1</sub> to PPC<sub>2</sub> (purple arrows): the economy can now produce more consumer goods and services and more capital goods. This is the same idea as a rightward shift of the AS or LRAS curve, an increase in productive capacity.")

    save("fig-16-1", fig_16_1(), "Figure 16.1: Short-run equilibrium output",
         "An upward-sloping SRAS curve and a downward-sloping AD curve meet at a single point, giving equilibrium price level P and real output Y.",
         "Short-run equilibrium output is where AD intersects SRAS, giving the equilibrium average price level P and real output Y. It looks like a market diagram, but the axes describe the whole economy.")
    save("fig-16-2", fig_16_2(), "Figure 16.2: New classical perspective of long-run equilibrium",
         "A vertical LRAS line at output Yf crossed by a downward-sloping AD1 curve at price level P1.",
         "In the new classical view, long-run equilibrium is where AD<sub>1</sub> meets the vertical LRAS: output is the full-employment level Y<sub>f</sub> and the price level is P<sub>1</sub>.")
    save("fig-16-3", fig_16_3(), "Figure 16.3: New classical view - impact of an increase in AD (long run, price only)",
         "A vertical LRAS at Yf with AD shifting right from AD1 to AD2. The price level rises from P1 to P2 while output stays at Yf.",
         "AD shifts right from AD<sub>1</sub> to AD<sub>2</sub> (purple arrows). Because LRAS is vertical, the whole effect in the long run falls on the price level, which rises from P<sub>1</sub> to P<sub>2</sub>, while real output remains at Y<sub>f</sub>.")
    f, _ = fig_16_4()
    save("fig-16-4", f, "Figure 16.4: An inflationary gap in the new classical model",
         "LRAS at Yf, an upward-sloping SRAS and AD shifting right from AD1 to AD2. In the short run output rises to Y1 above Yf, marked as the inflationary gap.",
         "The economy starts at Y<sub>f</sub> where AD<sub>1</sub>, SRAS and LRAS all meet. AD then shifts right to AD<sub>2</sub> (purple arrows). In the short run equilibrium moves along SRAS to output Y<sub>1</sub>, above Y<sub>f</sub> (price level P<sub>1</sub> to P<sub>2</sub>). The excess of Y<sub>1</sub> over Y<sub>f</sub> is the <em>inflationary gap</em>.")
    f, _ = fig_16_5()
    save("fig-16-5", f, "Figure 16.5: New classical adjustment - short run and long run",
         "Starting from an increase in AD, SRAS shifts left from SRAS1 to SRAS2 so that AD2 meets SRAS2 at Yf again, at price level P3 above P2 and P1.",
         "After AD rises from AD<sub>1</sub> to AD<sub>2</sub> the short-run equilibrium is at Y<sub>1</sub> and P<sub>2</sub>. Rising factor prices then push costs up and SRAS shifts left from SRAS<sub>1</sub> to SRAS<sub>2</sub> (purple arrows). Output returns to Y<sub>f</sub>, but at the permanently higher price level P<sub>3</sub> (P<sub>3</sub> &gt; P<sub>2</sub> &gt; P<sub>1</sub>).")
    f, _ = fig_16_6()
    save("fig-16-6", f, "Figure 16.6: A deflationary gap in the new classical model",
         "LRAS at Yf, an upward-sloping SRAS and AD shifting left from AD1 to AD2. In the short run output falls to Y1 below Yf, marked as the deflationary gap.",
         "The economy starts at Y<sub>f</sub> where AD<sub>1</sub>, SRAS and LRAS meet. AD then falls to AD<sub>2</sub> (purple arrows), so short-run equilibrium moves along SRAS to a lower output Y<sub>1</sub> and a lower price level P<sub>2</sub>. Output below Y<sub>f</sub> is the <em>deflationary (recessionary) gap</em>.")
    f, _ = fig_16_7()
    save("fig-16-7", f, "Figure 16.7: New classical adjustment - a fall in AD, short run and long run",
         "After AD falls from AD1 to AD2, SRAS shifts right from SRAS1 to SRAS2, so AD2 meets SRAS2 at Yf again at a lower price level P3 below P2 and P1.",
         "After AD falls to AD<sub>2</sub> the short-run equilibrium is at Y<sub>1</sub> and P<sub>2</sub>. Falling factor prices lower costs, so SRAS shifts right from SRAS<sub>1</sub> to SRAS<sub>2</sub> (purple arrow). Output returns to Y<sub>f</sub> at the permanently lower price level P<sub>3</sub> (P<sub>3</sub> &lt; P<sub>2</sub> &lt; P<sub>1</sub>).")
    f, _ = fig_16_8()
    save("fig-16-8", f, "Figure 16.8: Keynesian long-run equilibrium output below full employment",
         "A Keynesian AS curve, flat then curving up to a vertical LRAS section at Yf. AD cuts the flat section at output Y and price P, with Y less than Yf. The gap between Y and Yf is labelled deflationary gap.",
         "In the Keynesian model AD can intersect the flat, spare-capacity part of AS, so equilibrium output Y is below the full-employment level Y<sub>f</sub> at price level P. The horizontal distance between Y and Y<sub>f</sub> (double-headed arrow) is the <em>deflationary gap</em>; there is no automatic force restoring full employment.")
    f, _ = fig_16_9()
    save("fig-16-9", f, "Figure 16.9: Output gap illustrated on a PPC",
         "A bowed-out PPC for capital goods and consumer goods and services. Point A lies inside the curve and point B on the curve; a dotted double-headed arrow between them is labelled output gap.",
         "Point A, inside the PPC, is the economy&rsquo;s actual output; point B on the curve is its potential output. The dotted double-headed arrow between them is the <em>output gap</em>: resources are not fully used, so the economy produces less than it could.")
    f, _ = fig_16_10()
    save("fig-16-10", f, "Figure 16.10: Increase in AD while operating below full employment (phase 1)",
         "A Keynesian AS curve with AD shifting right from AD1 to AD2, both crossing the flat section. Real output rises from Y1 to Y2 and the price level stays at P.",
         "With spare capacity, AD shifts right from AD<sub>1</sub> to AD<sub>2</sub> (purple arrows) along the flat section of AS. Real output rises from Y<sub>1</sub> to Y<sub>2</sub> but the price level stays at P: unused resources are employed at no extra cost, so there is no inflationary pressure.")
    f, _ = fig_16_11()
    save("fig-16-11", f, "Figure 16.11: Increase in AD while approaching full employment (phase 2)",
         "A Keynesian AS curve with AD shifting right from AD2 to AD3, now cutting the upward-sloping section. Output rises from Y2 to Y3 and the price level from P1 to P2.",
         "AD shifts further right, from AD<sub>2</sub> to AD<sub>3</sub> (purple arrows), and now cuts the upward-sloping part of AS. Factors are becoming scarce and dearer, so output rises from Y<sub>2</sub> to Y<sub>3</sub> (still below Y<sub>f</sub>) and the price level also rises, from P<sub>1</sub> to P<sub>2</sub>: inflationary pressure appears.")
    f, _ = fig_16_12()
    save("fig-16-12", f, "Figure 16.12: Increase in AD at full employment (phase 3)",
         "A Keynesian AS curve with AD shifting right from AD1 to AD2, both crossing the vertical section at Yf. The price level rises from P1 to P2 and output stays at Yf.",
         "At full employment AS is vertical at Y<sub>f</sub>. AD shifts right from AD<sub>1</sub> to AD<sub>2</sub> (purple arrows) and the only change is a rise in the price level from P<sub>1</sub> to P<sub>2</sub>: output cannot rise, so the increase is purely inflationary.")

    save("fig-17-1", fig_17_1(), "Figure 17.1: An expansionary fiscal policy",
         "AD shifts right from AD1 to AD2 along an upward-sloping SRAS. The price level rises from P1 to P2 and real output from Y1 to Y2.",
         "Expansionary fiscal policy (higher government spending or lower taxes) shifts AD right from AD<sub>1</sub> to AD<sub>2</sub>. Along SRAS, real output rises from Y<sub>1</sub> to Y<sub>2</sub> (higher national income and growth, probably lower unemployment) but the price level rises from P<sub>1</sub> to P<sub>2</sub> (inflationary pressure).")
    save("fig-17-2", fig_17_2(), "Figure 17.2: An expansionary monetary policy",
         "AD shifts right from AD1 to AD2 along an upward-sloping SRAS. The price level rises from P1 to P2 and real output from Y1 to Y2.",
         "Expansionary monetary policy (lower interest rates or a larger money supply) shifts AD right from AD<sub>1</sub> to AD<sub>2</sub>. Real output rises from Y<sub>1</sub> to Y<sub>2</sub> (higher income and growth, probably lower unemployment) at the cost of a higher price level, P<sub>1</sub> to P<sub>2</sub>.")
    save("fig-17-3", fig_17_3(), "Figure 17.3: The process of credit creation",
         "A cascade of boxes: a new deposit of $200,000 is split by a bank into a 25% reserve of $50,000 and a loan of $150,000, which is re-deposited and split again, and so on. The total is $800,000 of deposits.",
         "A bank receives a new deposit of $200,000 and, with a 25% reserve requirement, keeps $50,000 and lends $150,000. That loan is spent and re-deposited, and the next bank keeps $37,500 and lends $112,500, and so on. The money multiplier is 1 &divide; 0.25 = 4, so the original deposit supports $800,000 of deposits in total: $600,000 of new loans plus $200,000 of reserves.")
    f, _ = fig_17_4()
    save("fig-17-4", f, "Figure 17.4: Open market operations",
         "Loanable funds market: a downward-sloping demand curve D and two vertical supply curves, S1 on the left and S2 on the right. Arrows show buying securities moving supply from S1 to S2 and selling securities moving it back.",
         "When the central bank <em>buys</em> government securities, banks&rsquo; funds rise and the supply of loanable funds shifts right from S<sub>1</sub> to S<sub>2</sub>, lowering the interest rate from i<sub>1</sub> to i<sub>2</sub> (expansionary). When it <em>sells</em> securities, supply shifts back left from S<sub>2</sub> to S<sub>1</sub> and the interest rate rises from i<sub>2</sub> to i<sub>1</sub> (contractionary).")
    save("fig-17-5", fig_17_5(), "Figure 17.5: The demand for money",
         "A downward-sloping demand curve for money, DM. At a higher nominal interest rate i1 the quantity of money demanded is Q1; at a lower rate i2 it is the larger Q2.",
         "The demand curve for money D<sub>M</sub> slopes downward. When the nominal interest rate falls from i<sub>1</sub> to i<sub>2</sub> (purple arrow on the vertical axis), the opportunity cost of holding money falls and the quantity demanded rises from Q<sub>1</sub> to Q<sub>2</sub>.")
    save("fig-17-6", fig_17_6(), "Figure 17.6: The supply curve for money",
         "A vertical money supply curve SM at quantity QM. Nominal interest rates i1 and i2 are marked with dashed lines to the curve.",
         "The money supply S<sub>M</sub> is a vertical line at Q<sub>M</sub>. It is set by the central bank and does not depend on the interest rate, so the quantity supplied is the same at i<sub>1</sub> and at i<sub>2</sub>.")
    f, _ = fig_17_7()
    save("fig-17-7", f, "Figure 17.7: The money market",
         "A downward-sloping demand for money DM with three vertical money supply curves SM1, SM and SM2 at quantities Q1, Qe and Q2. Equilibrium interest rates are i1, ie and i2, with purple arrows from SM to SM1 and SM2.",
         "Equilibrium in the money market is where D<sub>M</sub> meets the vertical money supply, at rate i<sub>e</sub> and quantity Q<sub>e</sub>. Contractionary monetary policy cuts the supply to S<sub>M1</sub> (Q<sub>1</sub>) and the equilibrium rate rises to i<sub>1</sub>; expansionary policy raises the supply to S<sub>M2</sub> (Q<sub>2</sub>) and the rate falls to i<sub>2</sub>.")


if __name__ == "__main__":
    build()
