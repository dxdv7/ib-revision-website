"""Original vector figures for chapters 1-4 (own coordinates, own examples)."""
import os, sys, json, math
sys.path.insert(0, os.path.dirname(__file__))
from figlib import *

OUT = "/Users/davidbukraba/Desktop/IB WEBSITE/assets/figures-original"
os.makedirs(OUT, exist_ok=True)

MINUS = "&#8722;"
TIMES = "&#215;"
PRIME = "&#8242;"


def save(fid, fig, label, alt, caption):
    title = label.split(": ", 1)[-1]
    open(f"{OUT}/{fid}.svg", "w").write(fig.svg(title, alt))
    with open(f"{OUT}/{fid}.json", "w") as fh:
        json.dump({"label": label, "alt": alt, "caption": caption}, fh, indent=1)
    print("saved", fid)


# ---------------- multi-panel helpers ----------------
def setp(f, x0, x1, y0=318, y1=50):
    f.X0, f.X1, f.Y0, f.Y1 = x0, x1, y0, y1


def axes2(f, xlabel, ylabel, title=None, origin="0"):
    """Axes for one panel of a multi-panel figure."""
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


def pt_on(l, y):
    return (Fig.x_at(l, y), y)


def dcurve(f, l, color, label, lx, ly, lc=None, size=13):
    f.line(*l[0], *l[1], color, 2.8)
    f.label(lx, ly, label, lc or color, size)


def axis_arrow(f, x1, x2, dy=13):
    """Purple arrow along the x axis label row, between two tick labels."""
    d = 12 if x2 > x1 else -12
    f.arrow(x1 + d, f.Y0 + dy, x2 - d, f.Y0 + dy, PURPLE, 1.8, 7)


# =============================================================
# CHAPTER 1
# =============================================================
def ppc_fn(x, xi=1000.0, yi=120.0):
    return yi * math.sqrt(max(0.0, 1 - (x / xi) ** 2))


# ---- 1.1 production possibilities curve ----
def fig_1_1():
    f = Fig().scale(1000, 120)
    f.axes("Manufactured goods (units per year)", "Food output (tonnes per year)")
    f.yticks([20, 40, 60, 80, 100, 120])
    f.xticks([200, 400, 600, 800, 1000])
    xs = sorted(set([1000 * math.sin(math.radians(t)) for t in range(0, 91, 6)] + [0, 200, 400, 600, 800, 920, 1000]))
    f.curve([f.pt(x, ppc_fn(x)) for x in xs])
    named = {"A": 0, "B": 200, "C": 400, "D": 600, "E": 800, "F": 920, "G": 1000}
    off = {"A": (9, -6), "B": (2, -10), "C": (4, -10), "D": (5, -10),
           "E": (6, -9), "F": (7, -8), "G": (0, -12)}
    for k, x in named.items():
        p = f.pt(x, ppc_fn(x))
        f.dot(*p)
        dx, dy = off[k]
        f.label(p[0] + dx, p[1] + dy, k, INK, 12.5, "middle" if k in "BCDG" else "start")
    hp = f.pt(400, 65)
    f.dot(*hp, 3.4, GREY)
    f.label(hp[0] + 7, hp[1] + 4, "H", INK, 12.5)
    ip = f.pt(800, 100)
    f.dot(*ip, 3.4, GREY)
    f.label(ip[0] + 7, ip[1] + 4, "I", INK, 12.5)
    return f


# ---- 1.2 straight-line PPC (constant opportunity cost) ----
def fig_1_2():
    f = Fig().scale(12, 8)
    f.axes("Bicycles (000s per year)", "E-scooters (000s per year)")
    f.yticks([2, 4, 6, 8], lambda v: str(v))
    f.xticks([3, 6, 9, 12], lambda v: str(v))
    f.line(*f.pt(0, 8), *f.pt(12, 0), RED, 2.8)
    A, B, C = (3, 6), (6, 4), (9, 2)
    for p in (A, B, C):
        assert abs(8 - p[0] * 2 / 3 - p[1]) < 1e-9  # on the line
    for p in (A, B, C):
        f.guide(*f.pt(*p))
    # equal trade-off steps
    f.line(*f.pt(*A), *f.pt(6, 6), PURPLE, 1.8, "4 3", "butt")
    f.line(*f.pt(6, 6), *f.pt(*B), PURPLE, 1.8, "4 3", "butt")
    f.line(*f.pt(*B), *f.pt(9, 4), PURPLE, 1.8, "4 3", "butt")
    f.line(*f.pt(9, 4), *f.pt(*C), PURPLE, 1.8, "4 3", "butt")
    f.label(f.px(4.5), f.py(6) - 6, "+3", PURPLE, 11.5, "middle")
    f.label(f.px(7.5), f.py(4) - 6, "+3", PURPLE, 11.5, "middle")
    f.label(f.px(6) + 6, f.py(5) + 4, MINUS + "2", PURPLE, 11.5)
    f.label(f.px(9) + 6, f.py(3) + 4, MINUS + "2", PURPLE, 11.5)
    for k, p in zip("ABC", (A, B, C)):
        q = f.pt(*p)
        f.dot(*q)
        f.label(q[0] - 10, q[1] + 17, k, INK, 12.5, "end")
    return f


# ---- 1.3 outward shift of the PPC ----
def fig_1_3():
    f = Fig().scale(100, 100)
    f.axes("Food output (tonnes)", "Manufactured goods")
    a1, b1 = 58, 50   # PPC1 intercepts (x, y)
    a2, b2 = 84, 74   # PPC2 intercepts
    fn = lambda x, a, b: b * math.sqrt(max(0.0, 1 - (x / a) ** 2))
    inv = lambda y, a, b: a * math.sqrt(max(0.0, 1 - (y / b) ** 2))
    for a, b in ((a1, b1), (a2, b2)):
        xs = [a * math.sin(math.radians(t)) for t in range(0, 91, 6)]
        f.curve([f.pt(x, fn(x, a, b)) for x in xs])
    # horizontal shift arrow at y = 12 and vertical arrow at x = 12
    y = 12
    x1, x2 = inv(y, a1, b1), inv(y, a2, b2)
    f.arrow(f.px(x1) + 5, f.py(y), f.px(x2) - 5, f.py(y), PURPLE)
    x = 14
    y1, y2 = fn(x, a1, b1), fn(x, a2, b2)
    f.arrow(f.px(x), f.py(y1) - 5, f.px(x), f.py(y2) + 5, PURPLE)
    f.label(f.px(x1) - 8, f.py(y) - 7, "PPC" + sub("", 1), RED, 12.5, "end")
    f.label(f.px(x2) + 8, f.py(y) - 7, "PPC" + sub("", 2), RED, 12.5)
    return f


# ---- 1.4 two-sector circular flow ----
def fig_1_4():
    f = Fig(w=520, h=390)

    def box(x, y, w, h, s):
        f.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="#fdeaea" '
              f'stroke="{RED}" stroke-width="2.2"/>')
        f.text(x + w / 2, y + h / 2 + 5, s, 14, "middle", INK, "600")
    box(190, 34, 140, 50, "Households")
    box(190, 296, 140, 50, "Firms")
    # inner real flows (purple)
    f.arrow(232, 298, 232, 88, PURPLE, 2.4)
    f.text(224, 186, "Goods and", 11.5, "end")
    f.text(224, 202, "services (3)", 11.5, "end")
    f.arrow(288, 86, 288, 294, PURPLE, 2.4)
    f.text(296, 186, "Factors of", 11.5)
    f.text(296, 202, "production (1)", 11.5)
    # outer money flows (red)
    f.flow([(188, 59), (56, 59), (56, 321), (188, 321)], RED, 2.4)
    f.text(44, 190, "Expenditure on goods and services (4)", 11.5, "middle", INK, rotate=-90)
    f.flow([(332, 321), (464, 321), (464, 59), (332, 59)], RED, 2.4)
    f.text(478, 190, "Wages, rent, interest and profits (2)", 11.5, "middle", INK, rotate=90)
    # legend
    f.line(150, 372, 178, 372, RED, 2.4)
    f.text(184, 376, "Money flows", 11, "start", GREY)
    f.line(290, 372, 318, 372, PURPLE, 2.4)
    f.text(324, 376, "Real flows", 11, "start", GREY)
    return f


# ---- 1.5 five-sector circular flow ----
def fig_1_5():
    f = Fig(w=640, h=410)

    def box(x, y, w, h, s, fill="#fdeaea", size=13):
        f.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill}" '
              f'stroke="{INK}" stroke-width="1.8"/>')
        lines = s.split("|")
        y0 = y + h / 2 + 5 - (len(lines) - 1) * 8
        for i, t in enumerate(lines):
            f.text(x + w / 2, y0 + i * 16, t, size, "middle", INK, "600")
    box(90, 30, 120, 46, "Households")
    box(90, 300, 120, 46, "Firms")
    f.flow([(88, 53), (32, 53), (32, 323), (88, 323)], PURPLE, 2.4)
    f.flow([(212, 323), (270, 323), (270, 53), (212, 53)], PURPLE, 2.4)
    f.text(22, 190, "Expenditure on goods and services", 11.5, "middle", INK, rotate=-90)
    f.text(262, 178, "Wages, rent,", 11.5, "end")
    f.text(262, 194, "interest and", 11.5, "end")
    f.text(262, 210, "profits", 11.5, "end")
    boxes = [(60, "Government", "Taxes", "Government spending"),
             (155, "Financial|institutions", "Saving", "Investment"),
             (250, "Foreign|sector", "Spending on imports", "Revenue from exports")]
    TEAL_D = "#1a95a1"
    for top, name, leak, inj in boxes:
        box(452, top, 160, 66, name, "#eef7f8")
        y1, y2 = top + 18, top + 48
        f.arrow(274, y1, 448, y1, RED, 2.2)
        f.text(361, y1 - 6, leak, 11.5, "middle")
        f.arrow(448, y2, 274, y2, TEAL_D, 2.2)
        f.text(361, y2 + 16, inj, 11.5, "middle")
    f.arrow(30, 396, 66, 396, PURPLE, 2.2)
    f.text(74, 400, "Income and spending", 11, "start", GREY)
    f.arrow(230, 396, 266, 396, RED, 2.2)
    f.text(274, 400, "Leakage (out of the flow)", 11, "start", GREY)
    f.arrow(440, 396, 476, 396, TEAL_D, 2.2)
    f.text(484, 400, "Injection (into the flow)", 11, "start", GREY)
    return f


# =============================================================
# CHAPTER 2
# =============================================================
def fig_2_1():
    f = Fig().scale(100, 105)
    Dn = lambda q: 100 * 2 ** (-q / 50.0)
    Sn = lambda q: 20 + 30 * (q / 50.0) ** 1.5
    lo, hi = 1.0, 99.0
    for _ in range(80):
        mid = (lo + hi) / 2
        if Dn(mid) > Sn(mid):
            lo = mid
        else:
            hi = mid
    qe = (lo + hi) / 2
    pe = Dn(qe)
    N = 36
    dq = [qe * i / N for i in range(N + 1)]
    dq_full = dq + [qe + (100 - qe) * i / 14 for i in range(1, 15)]
    sq = dq + [qe + (90 - qe) * i / 12 for i in range(1, 13)]
    dpts = [f.pt(q, Dn(q)) for q in dq_full]
    spts = [f.pt(q, Sn(q)) for q in sq]
    # tinted regions (drawn first)
    def poly(points, fill):
        s = " ".join(f"{x:.1f},{y:.1f}" for x, y in points)
        f.add(f'<polygon points="{s}" fill="{fill}"/>')
    left_d = [f.pt(q, Dn(q)) for q in dq]
    left_s = [f.pt(q, Sn(q)) for q in dq]
    poly([f.pt(0, pe)] + left_d + [f.pt(qe, pe)], "#ecebf7")
    poly([f.pt(0, pe), f.pt(qe, pe)] + left_s[::-1], "#fdebe7")
    poly([f.pt(0, 0), f.pt(qe, 0)] + left_s[::-1], "#f0f0f0")
    f.axes("Quantity", "Price", origin="")
    f.text(f.X0 - 8, f.Y0 + 16, "O", 12, "end")
    f.curve(dpts, GREY)
    f.curve(spts, RED)
    A = f.pt(qe, pe)
    f.guide(*A)
    f.dot(*A, 3.8, INK)
    f.text(f.X0 - 8, f.py(pe) + 4, "F", 12, "end")
    f.text(f.X0 - 8, f.py(Dn(0)) + 4, "D", 12, "end")
    f.text(f.X0 - 8, f.py(Sn(0)) + 4, "S", 12, "end")
    f.text(f.px(qe), f.Y0 + 18, "H", 12, "middle")
    # M with points Q (on demand) and P (on supply)
    qm = 30
    f.line(f.px(qm), f.py(0), f.px(qm), f.py(Dn(qm)), TEAL, 1.5, "5 4", "butt")
    f.text(f.px(qm), f.Y0 + 18, "M", 12, "middle")
    f.dot(*f.pt(qm, Dn(qm)), 3.4, INK)
    f.dot(*f.pt(qm, Sn(qm)), 3.4, INK)
    f.label(f.px(qm) + 6, f.py(Dn(qm)) - 6, "Q", INK, 12.5)
    f.label(f.px(qm) + 7, f.py(Sn(qm)) + 15, "P", INK, 12.5)
    f.label(A[0] + 8, A[1] - 9, "A", INK, 12.5)
    f.label(f.px(100) + 6, f.py(Dn(100)) + 4, "D" + PRIME, GREY, 12.5)
    f.label(f.px(90) + 6, f.py(Sn(90)) - 2, "S" + PRIME, RED, 12.5)
    # region labels
    f.text(f.X0 + 8, f.py(66), "Consumer&#8217;s", 11, "start", INK, "400", None, True)
    f.text(f.X0 + 8, f.py(60.5), "rent", 11, "start", INK, "400", None, True)
    f.text(f.X0 + 8, f.py(44), "Producer&#8217;s", 11, "start", INK, "400", None, True)
    f.text(f.X0 + 8, f.py(38.5), "rent", 11, "start", INK, "400", None, True)
    f.text(f.X0 + 8, f.py(13), "Producer&#8217;s", 11, "start", INK, "400", None, True)
    f.text(f.X0 + 8, f.py(7.5), "expenses", 11, "start", INK, "400", None, True)
    return f, (qe, pe)


# =============================================================
# CHAPTER 3
# =============================================================
def fig_3_1():
    f = Fig().scale(1000, 300)
    f.axes("Quantity of smartwatches (units per week)", "Price of smartwatches ($)")
    f.yticks([60, 120, 180, 240])
    f.xticks([200, 400, 600, 800, 1000])
    Dn = lambda q: 30 + 45000.0 / (q + 100)
    assert abs(Dn(200) - 180) < 1e-9 and abs(Dn(400) - 120) < 1e-9
    qs = [100, 150, 200, 300, 400, 500, 650, 800, 950]
    f.guide(*f.pt(200, 180))
    f.guide(*f.pt(400, 120))
    f.curve([f.pt(q, Dn(q)) for q in qs], RED)
    f.dot(*f.pt(200, 180))
    f.dot(*f.pt(400, 120))
    f.label(f.px(950), f.py(Dn(950)) - 16, "D (Demand)", INK, 12, "end")
    return f


def fig_3_3():
    f = Fig(w=860, h=380)
    # left panel: bus travel, movement along
    setp(f, 78, 390)
    axes2(f, "Quantity of bus trips (000s)", "Price of bus trips ($)", "Demand for bus travel")
    D = ((110, 76), (370, 296))
    dcurve(f, D, RED, "D", 376, 306, INK)
    ya, yb = 140, 205
    pa, pb = pt_on(D, ya), pt_on(D, yb)
    f.guide(*pa, "q", "p"); f.guide(*pb, "q" + sub("", 1), "p" + sub("", 1))
    f.dot(*pa); f.dot(*pb)
    f.arrow(f.X0 - 34, ya + 6, f.X0 - 34, yb - 6, PURPLE, 1.8, 7)
    axis_arrow(f, pa[0], pb[0])
    # right panel: rail travel, shift left
    setp(f, 498, 810)
    axes2(f, "Quantity of rail trips (000s)", "Price of rail trips ($)", "Demand for rail travel")
    D1 = ((545, 76), (735, 268)); D = ((615, 76), (805, 268))
    dcurve(f, D, RED, "D", 812, 284, INK)
    dcurve(f, D1, RED, "D" + sub("", 1), 740, 284, INK)
    y = 170
    pd, pd1 = pt_on(D, y), pt_on(D1, y)
    f.guide(*pd, "q", "p"); f.guide(*pd1, "q" + sub("", 1), None)
    f.dot(*pd); f.dot(*pd1)
    f.hshift(D, D1, 96); f.hshift(D, D1, 132)
    axis_arrow(f, pd[0], pd1[0])
    return f


def fig_3_4():
    f = Fig(w=860, h=380)
    setp(f, 78, 390)
    axes2(f, "Quantity of e-readers (000s)", "Price of e-readers ($)", "Demand for e-readers")
    D = ((110, 76), (370, 296))
    dcurve(f, D, RED, "D", 376, 306, INK)
    ya, yb = 140, 205
    pa, pb = pt_on(D, ya), pt_on(D, yb)
    f.guide(*pa, "q", "p"); f.guide(*pb, "q" + sub("", 1), "p" + sub("", 1))
    f.dot(*pa); f.dot(*pb)
    f.arrow(f.X0 - 34, ya + 6, f.X0 - 34, yb - 6, PURPLE, 1.8, 7)
    axis_arrow(f, pa[0], pb[0])
    setp(f, 498, 810)
    axes2(f, "Quantity of e-books (000s)", "Price of e-books ($)", "Demand for e-books")
    D = ((545, 76), (735, 268)); D1 = ((615, 76), (805, 268))
    dcurve(f, D, RED, "D", 740, 284, INK)
    dcurve(f, D1, RED, "D" + sub("", 1), 812, 284, INK)
    y = 170
    p0, p1 = pt_on(D, y), pt_on(D1, y)
    f.guide(*p0, "q", "p"); f.guide(*p1, "q" + sub("", 1), None)
    f.dot(*p0); f.dot(*p1)
    f.hshift(D, D1, 96); f.hshift(D, D1, 132)
    axis_arrow(f, p0[0], p1[0])
    return f


def shift_single(xlabel, ylabel):
    f = Fig()
    f.axes(xlabel, ylabel)
    D = ((100, 64), (300, 264)); D1 = ((175, 64), (375, 264))
    dcurve(f, D, RED, "D", 304, 280, INK)
    dcurve(f, D1, RED, "D" + sub("", 1), 380, 280, INK)
    y = 150
    p0, p1 = pt_on(D, y), pt_on(D1, y)
    f.guide(*p0, "q", "p"); f.guide(*p1, "q" + sub("", 1), None)
    f.dot(*p0); f.dot(*p1)
    f.hshift(D, D1, 92); f.hshift(D, D1, 122)
    axis_arrow(f, p0[0], p1[0])
    return f


def fig_3_6():
    f = Fig()
    f.axes("Quantity of bicycles (units per month)", "Price of bicycles ($)")
    D = ((110, 60), (370, 290))
    dcurve(f, D, RED, "D", 376, 300, INK)
    ya, yb = 130, 210
    pa, pb = pt_on(D, ya), pt_on(D, yb)
    f.guide(*pa, "q", "p"); f.guide(*pb, "q" + sub("", 1), "p" + sub("", 1))
    f.dot(*pa); f.dot(*pb)
    f.arrow(f.X0 - 34, ya + 6, f.X0 - 34, yb - 6, PURPLE, 1.8, 7)
    axis_arrow(f, pa[0], pb[0])
    return f


def fig_3_8():
    f = Fig().scale(100, 100)
    f.axes("Quantity of luxury watches", "Price of luxury watches ($)")
    qv, pv, kk = 22.0, 46.0, 0.0105     # vertex (quantity, price) and curvature
    ps = sorted(set(list(range(6, 95, 6)) + [pv, 94]))
    poly = [f.pt(qv + kk * (p - pv) ** 2, p) for p in ps]
    f.line(f.X0, f.py(pv), f.X1 - 6, f.py(pv), TEAL, 1.5, "5 4", "butt")
    f.curve(poly, RED)
    f.dot(*f.pt(qv, pv), 3.6, INK)
    f.label(poly[0][0] + 8, poly[0][1] + 4, "D", INK, 13)
    f.label(poly[-1][0] + 8, poly[-1][1] + 4, "D", INK, 13)
    f.label(f.X1 - 8, f.py(pv) + 16, "&#8216;Snob value&#8217; threshold", INK, 11.5, "end")
    f.label(f.px(46), f.py(28), "Normal range:", GREY, 11.5)
    f.label(f.px(46), f.py(28) + 14, "demand slopes down", GREY, 11.5)
    f.label(f.px(60), f.py(88) + 6, "Veblen range:", GREY, 11.5)
    f.label(f.px(60), f.py(88) + 20, "demand slopes up", GREY, 11.5)
    return f


def fig_3_9():
    f = Fig(w=840, h=760)
    P = [(10, "10"), (2, "2")]
    curves = {"A": (600, 50), "B": (300, 25), "C": (900, 75)}   # Q = a - b*P
    panels = [("Consumer A", "A", 0, 0, 800), ("Consumer B", "B", 420, 0, 800),
              ("Consumer C", "C", 0, 380, 800), ("Total market", "M", 420, 380, 1600)]
    tot = (1800, 150)
    for title, key, ox, oy, xmax in panels:
        setp(f, ox + 78, ox + 384, oy + 318, oy + 50)
        f.scale(xmax, 12)
        a, b = curves[key] if key in curves else tot
        axes2(f, "Quantity", "Price ($)", title)
        f.yticks([2, 4, 6, 8, 10], lambda v: str(v))
        qs = [a - b * p for p in (10, 2)]
        for p, q in zip((10, 2), qs):
            f.guide(*f.pt(q, p), None, None)
        f.xticks(qs, lambda v: str(int(v)))
        f.line(*f.pt(qs[0], 10), *f.pt(qs[1], 2), RED, 2.8)
        for p, q in zip((10, 2), qs):
            f.dot(*f.pt(q, p))
        f.label(f.px(qs[1]) + 8, f.py(2) - 8, "D" + sub("", key), INK, 12.5)
    return f


# =============================================================
# CHAPTER 4
# =============================================================
def fig_4_1():
    f = Fig()
    f.axes("Quantity demanded of product", "Price of product ($)")
    xq = 230
    f.line(xq, 60, xq, f.Y0, RED, 2.8)
    for y, s in ((215, sub("P", 1)), (140, sub("P", 2))):
        f.guide(xq, y, None, s, to_x=False)
        f.dot(xq, y)
    f.text(xq, f.Y0 + 18, "Q", 11.5, "middle")
    f.label(xq + 8, 68, "D", INK, 13)
    f.label(xq + 12, 185, "PED = 0", GREY, 12)
    return f


def fig_4_2():
    f = Fig()
    f.axes("Quantity demanded of product", "Price of product ($)")
    y = 130
    f.line(f.X0 + 22, y, 340, y, RED, 2.8)
    f.guide(f.X0 + 22, y, None, sub("P", 1), to_x=False)
    f.line(f.X0, y, f.X0 + 22, y, TEAL, 1.5, "5 4", "butt")
    f.label(346, y + 4, "D", INK, 13)
    f.label(200, y - 12, "PED = &#8734;", GREY, 12, "middle")
    return f


def fig_4_3():
    f = Fig().scale(12, 120)
    # price rises 50 -> 60 : quantity falls 10 -> 9 (000s)
    l = (f.pt(4, 110), f.pt(12, 30))          # P = 50 + 10*(10 - Q)
    x0, x1 = f.px(0), f.px(9)
    f.add(f'<rect x="{f.px(0):.1f}" y="{f.py(60):.1f}" width="{f.px(9)-f.px(0):.1f}" height="{f.py(50)-f.py(60):.1f}" fill="#e2f3e4"/>')
    f.add(f'<rect x="{f.px(9):.1f}" y="{f.py(50):.1f}" width="{f.px(10)-f.px(9):.1f}" height="{f.py(0)-f.py(50):.1f}" fill="#fbe3df"/>')
    f.add(f'<rect x="{f.px(0):.1f}" y="{f.py(50):.1f}" width="{f.px(9)-f.px(0):.1f}" height="{f.py(0)-f.py(50):.1f}" fill="#efefef"/>')
    f.axes("Quantity of bus passes (000s per month)", "Price of a bus pass ($)")
    A = (10, 50); B = (9, 60)
    for q, p in (A, B):
        assert abs(Fig.y_at(l, f.px(q)) - f.py(p)) < 0.01
    f.guide(*f.pt(*A), "10", "50")
    f.guide(*f.pt(*B), "9", "60")
    f.line(*l[0], *l[1], RED, 2.8)
    f.dot(*f.pt(*A)); f.dot(*f.pt(*B))
    f.label(l[1][0] + 6, l[1][1] + 4, "D", INK, 13)
    f.label(f.px(4.5), f.py(55) + 5, "a", INK, 13, "middle")
    f.label(f.px(4.5), f.py(24), "b", INK, 13, "middle")
    f.label((f.px(9) + f.px(10)) / 2, f.py(24), "c", INK, 13, "middle")
    f.arrow(f.X0 - 36, f.py(50) - 4, f.X0 - 36, f.py(60) + 4, PURPLE, 1.8, 7)
    f.arrow(f.px(10) - 5, f.Y0 + 31, f.px(9) + 5, f.Y0 + 31, PURPLE, 1.8, 7)
    return f, l


def fig_4_4():
    f = Fig().scale(60, 16)
    # price rises 10 -> 12 ; quantity falls 50 -> 35 (000s)
    l = (f.pt(20, 14), f.pt(58, 8.933333333))   # P = 10 + (50 - Q) * 2/15
    def P(q): return 10 + (50 - q) * 2 / 15.0
    l = (f.pt(20, P(20)), f.pt(58, P(58)))
    f.add(f'<rect x="{f.px(0):.1f}" y="{f.py(12):.1f}" width="{f.px(35)-f.px(0):.1f}" height="{f.py(10)-f.py(12):.1f}" fill="#e2f3e4"/>')
    f.add(f'<rect x="{f.px(35):.1f}" y="{f.py(10):.1f}" width="{f.px(50)-f.px(35):.1f}" height="{f.py(0)-f.py(10):.1f}" fill="#fbe3df"/>')
    f.add(f'<rect x="{f.px(0):.1f}" y="{f.py(10):.1f}" width="{f.px(35)-f.px(0):.1f}" height="{f.py(0)-f.py(10):.1f}" fill="#efefef"/>')
    f.axes("Quantity of subscriptions (000s)", "Monthly price of subscription ($)")
    A = (50, 10); B = (35, 12)
    for q, p in (A, B):
        assert abs(P(q) - p) < 1e-9
        assert abs(Fig.y_at(l, f.px(q)) - f.py(p)) < 0.01
    f.guide(*f.pt(*A), "50", "10")
    f.guide(*f.pt(*B), "35", "12")
    f.line(*l[0], *l[1], RED, 2.8)
    f.dot(*f.pt(*A)); f.dot(*f.pt(*B))
    f.label(l[1][0] + 6, l[1][1] + 4, "D", INK, 13)
    f.label(f.px(17.5), f.py(11) + 5, "a", INK, 13, "middle")
    f.label(f.px(17.5), f.py(5), "b", INK, 13, "middle")
    f.label((f.px(35) + f.px(50)) / 2, f.py(5), "c", INK, 13, "middle")
    f.arrow(f.X0 - 36, f.py(10) - 4, f.X0 - 36, f.py(12) + 4, PURPLE, 1.8, 7)
    f.arrow(f.px(50) - 5, f.Y0 + 31, f.px(35) + 5, f.Y0 + 31, PURPLE, 1.8, 7)
    return f


def fig_4_5():
    f = Fig().scale(120, 66)
    Pn = lambda q: 600.0 / q
    q1, q2 = 20, 50
    p1, p2 = Pn(q1), Pn(q2)
    assert p1 == 30 and p2 == 12
    R = lambda x0, y0, x1, y1, c: f.add(
        f'<rect x="{f.px(x0):.1f}" y="{f.py(y1):.1f}" width="{f.px(x1)-f.px(x0):.1f}" '
        f'height="{f.py(y0)-f.py(y1):.1f}" fill="{c}"/>')
    R(0, p2, q1, p1, "#e2f3e4")      # a
    R(0, 0, q1, p2, "#efefef")       # b
    R(q1, 0, q2, p2, "#fbe3df")      # c
    f.axes("Quantity of taxi rides (000s per week)", "Price per ride ($)")
    f.guide(*f.pt(q1, p1), "20", "30")
    f.guide(*f.pt(q2, p2), "50", "12")
    f.line(f.px(q1), f.py(p2), f.px(q1), f.py(0), TEAL, 1.5, "5 4", "butt")
    qs = [q for q in [10 * 1.07 ** i for i in range(0, 38)] if q <= 115 and abs(q - 20) > 1 and abs(q - 50) > 2] + [20, 50]
    qs = sorted(qs)
    f.curve([f.pt(q, Pn(q)) for q in qs])
    f.dot(*f.pt(q1, p1)); f.dot(*f.pt(q2, p2))
    f.label(f.px(10), f.py(21), "a", INK, 13, "middle")
    f.label(f.px(10), f.py(5.5), "b", INK, 13, "middle")
    f.label(f.px(35), f.py(5.5), "c", INK, 13, "middle")
    f.label(f.px(qs[-1]) + 6, f.py(Pn(qs[-1])) - 6, "D", INK, 13)
    f.label(f.px(60), f.py(50), "P " + TIMES + " Q = 600", GREY, 12)
    f.label(f.px(60), f.py(45) - 2, "at every point,", GREY, 12)
    f.label(f.px(60), f.py(40) - 4, "so PED = 1 throughout", GREY, 12)
    return f


def fig_4_6():
    f = Fig().scale(250, 25)
    f.axes("Quantity (units per week)", "Price ($)")
    f.yticks([5, 10, 15, 20, 25], lambda v: str(v))
    f.xticks([50, 100, 150, 200, 250], lambda v: str(v))
    Pn = lambda q: 25 - q / 10.0
    l = (f.pt(10, Pn(10)), f.pt(240, Pn(240)))
    f.line(*l[0], *l[1], RED, 2.8)
    f.label(l[1][0] + 8, l[1][1] + 4, "D", INK, 13)
    pts = {"a": 50, "b": 70, "c": 150, "d": 170}
    for k, q in pts.items():
        p = f.pt(q, Pn(q))
        assert abs(Fig.y_at(l, p[0]) - p[1]) < 0.01
        f.dot(*p, 3.6, INK)
        f.label(p[0] - 9, p[1] + 16, k, INK, 12.5, "middle")
    # PED callouts
    ma = f.pt(60, Pn(60)); mc = f.pt(160, Pn(160))
    f.label(f.px(76), f.py(24), "PED = 4.0", INK, 12)
    f.label(f.px(76), f.py(24) + 14, "(elastic)", INK, 12)
    f.arrow(f.px(76) + 8, f.py(24) + 20, ma[0] + 7, ma[1] - 6, PURPLE, 1.6, 7)
    f.label(f.px(166), f.py(17), "PED = 0.67", INK, 12)
    f.label(f.px(166), f.py(17) + 14, "(inelastic)", INK, 12)
    f.arrow(f.px(166) + 8, f.py(17) + 20, mc[0] + 7, mc[1] - 6, PURPLE, 1.6, 7)
    return f, l


def fig_4_8():
    f = Fig()
    f.scale(100, 100)
    f.axes("Income", "Quantity of instant noodles demanded")
    qn = lambda y: 78 * (1 - math.exp(-y / 14.0)) - 0.00006 * y ** 3 + 0.0
    # find peak
    ys = [i * 0.5 for i in range(0, 201)]
    ypk = max(ys, key=qn)
    ypk = round(ypk)
    pts = [f.pt(y, qn(y)) for y in sorted(set([0, 2, 5, 8, 12, 16, 20, 25, 30, 35, ypk] + list(range(46, 101, 5))))]
    f.line(f.px(ypk), f.py(qn(ypk)), f.px(ypk), f.Y0, TEAL, 1.5, "5 4", "butt")
    f.curve(pts)
    f.dot(f.px(ypk), f.py(qn(ypk)), 3.6, INK)
    f.text(f.px(ypk), f.Y0 + 18, "Y*", 11.5, "middle")
    f.label(f.px(4), f.py(88), "Normal good:", GREY, 11.5)
    f.label(f.px(4), f.py(88) + 14, "demand rises with income", GREY, 11.5)
    f.label(f.px(100), f.py(13), "Inferior good:", GREY, 11.5, "end")
    f.label(f.px(100), f.py(13) + 14, "demand falls with income", GREY, 11.5, "end")
    return f, ypk, qn(ypk)




# =============================================================
# BUILD: labels, alt text and captions
# =============================================================
def build():
    save("fig-1-1", fig_1_1(), "Figure 1.1: Production possibilities curve",
         "A bowed-out production possibilities curve for food (tonnes) against manufactured goods (units), with points A to G on the curve, H inside it and I beyond it.",
         "A concave PPC for an economy choosing between food and manufactured goods. Points A&ndash;G lie on the curve (A: 120 tonnes of food and no manufactures; G: 1,000 units of manufactures and no food), so resources are fully and efficiently used. H (400 units, 65 tonnes) lies inside the curve, showing unemployed or underused resources; I (800 units, 100 tonnes) lies beyond it and is unattainable with current resources and technology.")
    save("fig-1-2", fig_1_2(), "Figure 1.2: Constant opportunity cost (straight-line PPC)",
         "A straight-line production possibilities curve for bicycles and e-scooters with points A, B and C and equal-sized steps between them.",
         "A straight-line PPC for bicycles and e-scooters (thousands per year), running from 8,000 e-scooters to 12,000 bicycles. Moving from A (3, 6) to B (6, 4) to C (9, 2), each extra 3,000 bicycles costs exactly 2,000 e-scooters, so the opportunity cost is constant.")
    save("fig-1-3", fig_1_3(), "Figure 1.3: An increase in production possibilities",
         "Two bowed-out production possibilities curves, PPC1 and PPC2, with PPC2 further from the origin and purple arrows showing the outward shift.",
         "The PPC shifts outward from PPC<sub>1</sub> to PPC<sub>2</sub>, shown by the purple arrows. The maximum potential output of both food and manufactured goods has risen, so the economy has experienced growth in its production possibilities.")
    save("fig-1-4", fig_1_4(), "Figure 1.4: Two-sector circular flow of income",
         "Two-sector circular flow: households and firms joined by four numbered flows, factors of production, wages rent interest and profits, goods and services, and expenditure.",
         "Households and firms are linked by four flows: (1) factors of production pass from households to firms; (2) wages, rent, interest and profits pass from firms to households; (3) goods and services pass from firms to households; (4) expenditure on goods and services passes from households to firms. Red arrows show money flows and purple arrows show real flows.")
    save("fig-1-5", fig_1_5(), "Figure 1.5: Circular flow of income (five sectors)",
         "Circular flow of income with households and firms, plus government, financial institutions and foreign sector, each with a red leakage arrow out and a teal injection arrow in.",
         "Households and firms exchange expenditure and income (purple loop; the matching real flows of goods and factors are omitted for clarity). Three other sectors connect to the flow: taxes leak out to the government and government spending is injected back; saving leaks out to financial institutions and investment is injected back; spending on imports leaks out to the foreign sector and export revenue is injected back. Leakages and injections need not be equal at any moment.")
    f, (qe, pe) = fig_2_1()
    save("fig-2-1", f, "Figure 2.1: An early supply and demand diagram (Marshall)",
         "A supply and demand diagram with a downward-sloping demand curve DD', an upward-sloping supply curve SS' meeting at point A, and shaded regions labelled consumer's rent, producer's rent and producer's expenses.",
         "A redrawn version of Marshall&rsquo;s supply and demand diagram. The demand curve DD&prime; slopes down and the supply curve SS&prime; slopes up, meeting at A, which fixes the equilibrium price F and quantity H. Above the price line and below demand is <em>consumer&rsquo;s rent</em> (consumer surplus); between the price line and supply is <em>producer&rsquo;s rent</em>; below supply are <em>producer&rsquo;s expenses</em>. At quantity M, Q is the price the marginal buyer would pay and P the price the marginal seller would accept.")
    save("fig-3-1", fig_3_1(), "Figure 3.1: A demand curve for smartwatches",
         "A downward-sloping demand curve for smartwatches: at $180 quantity demanded is 200 units per week and at $120 it is 400 units.",
         "A demand curve for smartwatches. A fall in price from $180 to $120 raises the <em>quantity demanded</em> from 200 to 400 units per week. This is a movement along the existing curve D, not a shift of it.")
    save("fig-3-2", shift_single("Quantity of concert tickets", "Price of concert tickets ($)"),
         "Figure 3.2: The demand for concert tickets",
         "Two parallel downward-sloping demand curves for concert tickets, D and D1, with D1 to the right, and purple arrows showing the rightward shift.",
         "A rise in consumers&rsquo; incomes shifts the demand curve for concert tickets to the right, from D to D<sub>1</sub> (purple arrows). At the unchanged price p, quantity demanded rises from q to q<sub>1</sub>, and more is demanded at every price.")
    save("fig-3-3", fig_3_3(), "Figure 3.3: The demand for bus travel and rail travel",
         "Two panels. Bus travel: a fall in price from p to p1 is a movement along demand curve D from q to q1. Rail travel: the demand curve shifts left from D to D1.",
         "<em>Bus panel:</em> a fall in the price of bus travel from p to p<sub>1</sub> is a movement along the demand curve D, raising quantity demanded from q to q<sub>1</sub>. <em>Rail panel:</em> because bus travel is now cheaper and the two are substitutes, the demand curve for rail travel shifts left from D to D<sub>1</sub>, so at the unchanged price p quantity demanded falls from q to q<sub>1</sub>.")
    save("fig-3-4", fig_3_4(), "Figure 3.4: The demand for e-readers and e-books",
         "Two panels. E-readers: a fall in price from p to p1 is a movement along demand curve D. E-books: the demand curve shifts right from D to D1.",
         "<em>E-reader panel:</em> a fall in the price of e-readers from p to p<sub>1</sub> is a movement along the demand curve, raising quantity demanded from q to q<sub>1</sub>. <em>E-book panel:</em> e-books are a complement, and more e-readers in use means more e-books wanted, so demand shifts right from D to D<sub>1</sub>; at the same price p quantity demanded rises from q to q<sub>1</sub>.")
    save("fig-3-5", shift_single("Quantity of pickleball paddles", "Price of pickleball paddles ($)"),
         "Figure 3.5: The demand for pickleball paddles",
         "Two parallel downward-sloping demand curves for pickleball paddles, D and D1, with D1 to the right, and purple arrows showing the rightward shift.",
         "A media campaign or a televised national tournament makes pickleball more fashionable, so the whole demand curve for paddles shifts right from D to D<sub>1</sub> (purple arrows). At the unchanged price p, quantity demanded rises from q to q<sub>1</sub>, and more is demanded at every price.")
    save("fig-3-6", fig_3_6(), "Figure 3.6: The demand for bicycles (a movement)",
         "A downward-sloping demand curve for bicycles with prices p and p1 and quantities q and q1 marked, showing a movement along the curve.",
         "A fall in the price of bicycles from p to p<sub>1</sub> causes a movement along the existing demand curve D, an increase in quantity demanded from q to q<sub>1</sub>. The curve itself does not shift.")
    save("fig-3-7", shift_single("Quantity of reusable shopping bags", "Price of reusable shopping bags ($)"),
         "Figure 3.7: The demand for reusable shopping bags (a shift)",
         "Two parallel downward-sloping demand curves for reusable shopping bags, D and D1, with D1 to the right, and purple arrows showing the rightward shift.",
         "A government campaign against single-use plastic bags is a non-price factor, a change in tastes and preferences, so the whole demand curve for reusable bags shifts right from D to D<sub>1</sub>. At the unchanged price p, quantity demanded rises from q to q<sub>1</sub>, and more is demanded at every price.")
    save("fig-3-8", fig_3_8(), "Figure 3.8: The demand for a Veblen good (luxury watches)",
         "A sideways-curving demand curve for luxury watches that slopes down at low prices, then bends back and slopes upward above a snob-value threshold price.",
         "At lower prices the demand curve for luxury watches slopes downward as normal. Above the snob-value threshold price (dashed line) the curve bends and slopes <em>upward</em>: the higher price adds prestige, so quantity demanded rises with price, the mark of a Veblen good.")
    save("fig-3-9", fig_3_9(), "Figure 3.9: Individual demand curves and the market demand curve (horizontal summing)",
         "Four panels with a common price axis: demand curves for Consumers A, B and C and the market demand curve found by adding their quantities at each price.",
         "Horizontal summing. At a price of $10, A buys 100, B buys 50 and C buys 150, so the market demands 300. At $2, A buys 500, B buys 250 and C buys 750, so the market demands 1,500. Joining these market points gives the market demand curve D<sub>M</sub>.")
    save("fig-4-1", fig_4_1(), "Figure 4.1: A perfectly inelastic demand curve (PED = 0)",
         "A vertical demand curve at quantity Q. Prices P1 and P2 are marked on the price axis and both give the same quantity Q.",
         "A perfectly inelastic demand curve is a vertical line at quantity Q. Whether the price is P<sub>1</sub> or P<sub>2</sub>, quantity demanded stays at Q, so the percentage change in quantity demanded is always zero and PED = 0.")
    save("fig-4-2", fig_4_2(), "Figure 4.2: A perfectly elastic demand curve (PED = infinity)",
         "A horizontal demand curve at price P1.",
         "A perfectly elastic demand curve is a horizontal line at price P<sub>1</sub>. At P<sub>1</sub> consumers will buy any quantity, but at any price above it quantity demanded falls to zero, so PED is infinite.")
    f, l = fig_4_3()
    save("fig-4-3", f, "Figure 4.3: The demand for bus passes (inelastic, revenue rises)",
         "A downward-sloping demand curve for bus passes with shaded revenue areas a, b and c. Price rises from $50 to $60 and quantity falls from 10,000 to 9,000.",
         "The price of a monthly bus pass rises from $50 to $60 and quantity demanded falls from 10,000 to 9,000, so PED = &minus;10% &divide; +20% = &minus;0.5 (inelastic). Area c ($50 &times; 1,000 = $50,000) is lost, but area a ($10 &times; 9,000 = $90,000) is gained. Because a is larger than c, total revenue rises by $40,000, from $500,000 to $540,000.")
    save("fig-4-4", fig_4_4(), "Figure 4.4: The demand for streaming subscriptions (elastic, revenue falls)",
         "A downward-sloping demand curve for streaming subscriptions with shaded revenue areas a, b and c. Price rises from $10 to $12 and subscribers fall from 50,000 to 35,000.",
         "The monthly price of a streaming subscription rises from $10 to $12 and subscribers fall from 50,000 to 35,000, so PED = &minus;30% &divide; +20% = &minus;1.5 (elastic). Area c ($10 &times; 15,000 = $150,000) is lost while area a ($2 &times; 35,000 = $70,000) is gained. Because a is smaller than c, total revenue falls by $80,000, from $500,000 to $420,000.")
    save("fig-4-5", fig_4_5(), "Figure 4.5: A rectangular hyperbola where PED = 1 at every point",
         "A convex rectangular hyperbola demand curve for taxi rides with shaded revenue rectangles a, b and c, where price times quantity is 600 everywhere.",
         "A demand curve for taxi rides with P &times; Q = 600 at every point. Moving from $30 and 20 (thousand) rides to $12 and 50 (thousand) rides, the revenue lost (area a, $360 thousand) exactly equals the revenue gained (area c, $360 thousand). Total revenue never changes along the curve, so PED = 1 at every point.")
    save("fig-4-6", fig_4_6()[0], "Figure 4.6: PED values for a straight-line demand curve",
         "A straight downward-sloping demand line with points a and b near the top marked PED 4.0 (elastic) and points c and d near the bottom marked PED 0.67 (inelastic).",
         "On the straight-line demand curve P = 25 &minus; Q/10, moving from a (50, $20) to b (70, $18) gives a 40% rise in quantity for a 10% fall in price, so PED = 4.0 (elastic). Moving from c (150, $10) to d (170, $8) gives a 13.3% rise in quantity for a 20% fall in price, so PED = 0.67 (inelastic). Elasticity falls as we move down the same straight line.")
    f, ypk, qpk = fig_4_8()
    save("fig-4-8", f, "Figure 4.8: An Engel curve for instant noodles",
         "An Engel curve with income on the horizontal axis and quantity of instant noodles demanded on the vertical axis. It rises, peaks and then falls at higher incomes.",
         "An Engel curve for instant noodles. At low incomes, quantity demanded rises steeply as income rises (a normal good). Demand peaks at income Y* and then falls as households can afford superior alternatives, so beyond Y* instant noodles behave as an inferior good.")


if __name__ == "__main__":
    build()
