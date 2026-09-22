"""Original vector figures for chapters 5, 6 and 7 (own coordinates, own examples).

Every dot is computed from the curves it sits on; every tick, guide and point
comes from a data scale so they line up exactly.
"""
import os, sys, json, math
sys.path.insert(0, os.path.dirname(__file__))
from figlib import *

OUT = "/Users/davidbukraba/Desktop/IB WEBSITE/assets/figures-original"
os.makedirs(OUT, exist_ok=True)

CS_FILL = "#bfe3f4"   # consumer surplus
PS_FILL = "#d3ecc9"   # producer surplus
BRACE = "#3fb1e3"
MINUS = "&#8722;"
INF = "&#8734;"


def save(fid, fig, label, alt, caption):
    title = label.split(": ", 1)[-1]
    open(f"{OUT}/{fid}.svg", "w").write(fig.svg(title, alt))
    with open(f"{OUT}/{fid}.json", "w") as fh:
        json.dump({"label": label, "alt": alt, "caption": caption}, fh, indent=1)
    print("saved", fid)


def sbt(base, n, rest=""):
    """Subscript label that returns the baseline afterwards (for trailing text)."""
    return f'{base}<tspan font-size="70%" dy="3">{n}</tspan><tspan dy="-3">{rest}</tspan>'


class Panel(Fig):
    """One panel of a multi-panel figure; all panels share one part list."""

    def __init__(self, main, ox=0, oy=0):
        super().__init__(main.w, main.h, ox + 78, oy + 318, ox + 384, oy + 30)
        self.parts = main.parts
        self.ox, self.oy = ox, oy

    def axes(self, xlabel, ylabel, origin="0", xarrow=True, yarrow=True):
        self.line(self.X0, self.Y0, self.X1, self.Y0, INK, 2.2)
        self.line(self.X0, self.Y0, self.X0, self.Y1, INK, 2.2)
        self.arrowhead(self.X1 + 5, self.Y0, 0, INK, 9)
        self.arrowhead(self.X0, self.Y1 - 5, -90, INK, 9)
        if origin:
            self.text(self.X0 - 12, self.Y0 + 16, origin, 12, "end")
        self.text((self.X0 + self.X1) / 2, self.oy + 366, xlabel, 12.5, "middle")
        self.text(self.ox + 20, (self.Y0 + self.Y1) / 2, ylabel, 12.5, "middle", rotate=-90)

    def title(self, s):
        self.text(self.X0 + 12, self.oy + 20, s, 13, "start", GREY, "600", italic=True)


# ---------------- small helpers ----------------
def L(f, q1, p1, q2, p2):
    """Straight line in data coordinates -> ((px,py),(px,py))."""
    return ((f.px(q1), f.py(p1)), (f.px(q2), f.py(p2)))


def draw(f, ln, color=RED, width=2.8):
    f.line(ln[0][0], ln[0][1], ln[1][0], ln[1][1], color, width)


def vdrop(f, x, y, label=None, size=11.5):
    f.line(x, y, x, f.Y0, TEAL, 1.5, "5 4", "butt")
    if label:
        f.text(x, f.Y0 + 18, label, size, "middle")


def hdrop(f, x, y, label=None, size=11.5):
    f.line(f.X0, y, x, y, TEAL, 1.5, "5 4", "butt")
    if label:
        f.text(f.X0 - 8, y + 4, label, size, "end")


def onl(f, ln, x):
    return (x, Fig.y_at(ln, x))


def y_arrow(f, y_from, y_to, gap=4):
    d = gap if y_to > y_from else -gap
    f.arrow(f.X0 - 38, y_from + d, f.X0 - 38, y_to - d, PURPLE)


def x_arrow(f, x_from, x_to, gap=4, dy=32):
    d = gap if x_to > x_from else -gap
    f.arrow(x_from + d, f.Y0 + dy, x_to - d, f.Y0 + dy, PURPLE)


def brace(f, x1, x2, y, h=9, up=False, color=BRACE, width=2.2):
    s = -1 if up else 1
    xm = (x1 + x2) / 2
    r = h
    yy = y + s * h / 2
    d = (f"M{x1:.1f},{y:.1f} Q{x1:.1f},{yy:.1f} {x1 + r:.1f},{yy:.1f} "
         f"L{xm - r:.1f},{yy:.1f} Q{xm:.1f},{yy:.1f} {xm:.1f},{y + s * h:.1f} "
         f"Q{xm:.1f},{yy:.1f} {xm + r:.1f},{yy:.1f} "
         f"L{x2 - r:.1f},{yy:.1f} Q{x2:.1f},{yy:.1f} {x2:.1f},{y:.1f}")
    f.path(d, color, width)


def fill_poly(f, pts, color):
    d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts) + " Z"
    f.path(d, "none", 0, fill=color)


def box(f, x, y, w, h, lines, size=12.5, fill="#fdeaea", stroke=RED):
    f.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" '
          f'stroke="{stroke}" stroke-width="2.2"/>')
    n = len(lines)
    y0 = y + h / 2 - (n - 1) * 8.5 + 4.5
    for i, s in enumerate(lines):
        f.text(x + w / 2, y0 + i * 17, s, size, "middle")


# =============================================================
# CHAPTER 5
# =============================================================
def fig_5_1():
    f = Fig().scale(2500, 350)
    f.axes("Quantity of bicycles (per month)", "Price of bicycles ($)")
    f.yticks([50, 100, 150, 200, 250, 300, 350])
    f.xticks([500, 1000, 1500, 2000, 2500])
    data = [(500, 100), (1000, 150), (1500, 195), (2000, 250), (2300, 300)]
    pts = [f.pt(*d) for d in data]
    for q, p in [data[1], data[3]]:
        x, y = f.pt(q, p)
        hdrop(f, x, y)
        vdrop(f, x, y)
    f.curve(pts)
    for d in [data[0], data[1], data[3], data[4]]:
        f.dot(*f.pt(*d))
    f.label(f.px(2300) + 8, f.py(300) - 10, "S (Supply)", INK, 12.5)
    save("fig-5-1", f, "Figure 5.1: A supply curve for bicycles",
         "Upward-sloping supply curve for bicycles: quantity supplied rises from 1,000 to 2,000 a month as the price rises from $150 to $250.",
         "The supply curve S for bicycles slopes upward. At $150 producers supply 1,000 bicycles a month; when the price rises to $250 they supply 2,000. "
         "The curve gets steeper at higher prices, although economists usually draw supply curves as straight lines for simplicity.")


def fig_5_2():
    f = Fig().scale(100, 100)
    f.axes("Quantity of sneakers", "Price of sneakers ($)")
    S = L(f, 55, 10, 88, 90)
    S1 = L(f, 30, 10, 63, 90)
    P = f.py(45)
    xs, xs1 = f.x_at(S, P), f.x_at(S1, P)
    hdrop(f, xs, P, "P")
    vdrop(f, xs, P, "Q")
    vdrop(f, xs1, P, sbt("Q", 1))
    draw(f, S)
    draw(f, S1)
    f.dot(xs, P)
    f.dot(xs1, P)
    f.label(S[1][0] + 6, S[1][1] - 6, "S", RED, 13)
    f.label(S1[1][0] + 6, S1[1][1] - 6, sbt("S", 1), RED, 13)
    f.hshift(S, S1, f.py(78))
    f.hshift(S, S1, f.py(22))
    save("fig-5-2", f, "Figure 5.2: The supply of sneakers",
         "Two parallel upward-sloping supply curves for sneakers, S1 to the left of S, with two leftward arrows and dashed lines showing quantity falling from Q to Q1 at price P.",
         "A rise in wages raises the cost of making sneakers, so supply falls: the curve shifts left from S to S<sub>1</sub>. "
         "At the same price P, producers now supply only Q<sub>1</sub> instead of Q.")


def fig_5_3():
    f = Fig(w=860, h=380)
    a = Panel(f, 0, 0)
    a.scale(100, 100)
    a.axes("Quantity", "Price ($)")
    a.title("Supply of kayaks")
    S = L(a, 15, 12, 95, 88)
    P0, P1 = a.py(30), a.py(65)
    q0, q1 = a.x_at(S, P0), a.x_at(S, P1)
    hdrop(a, q0, P0, "P")
    hdrop(a, q1, P1, sbt("P", 1))
    vdrop(a, q0, P0, "Q")
    vdrop(a, q1, P1, sbt("Q", 1))
    draw(a, S)
    a.dot(q0, P0)
    a.dot(q1, P1)
    a.label(S[1][0] + 6, S[1][1] - 6, "S", RED, 13)
    y_arrow(a, P0, P1)
    x_arrow(a, q0, q1)

    b = Panel(f, 430, 0)
    b.scale(100, 100)
    b.axes("Quantity", "Price ($)")
    b.title("Supply of paddleboards")
    S = L(b, 50, 10, 85, 88)
    S1 = L(b, 28, 10, 63, 88)
    P = b.py(40)
    xs, xs1 = b.x_at(S, P), b.x_at(S1, P)
    hdrop(b, xs, P, "P")
    vdrop(b, xs, P, "Q")
    vdrop(b, xs1, P, sbt("Q", 1))
    draw(b, S)
    draw(b, S1)
    b.dot(xs, P)
    b.dot(xs1, P)
    b.label(S[1][0] + 6, S[1][1] - 6, "S", RED, 13)
    b.label(S1[1][0] + 6, S1[1][1] - 6, sbt("S", 1), RED, 13)
    b.hshift(S, S1, b.py(72))
    b.hshift(S, S1, b.py(20))
    save("fig-5-3", f, "Figure 5.3: The supply of kayaks and paddleboards",
         "Two diagrams: a movement up along the kayak supply curve as price rises from P to P1, and a leftward shift of the paddleboard supply curve from S to S1 at an unchanged price.",
         "Left: when the price of kayaks rises from P to P<sub>1</sub>, there is a movement along the supply curve S and quantity supplied rises from Q to Q<sub>1</sub>. "
         "Right: as boat-builders move their materials and workers into kayaks, the supply of paddleboards shifts left from S to S<sub>1</sub>, so less is supplied at the same price P.")


def fig_5_4():
    f = Fig(w=860, h=380)
    # ---- lamb: demand shifts right ----
    a = Panel(f, 0, 0)
    a.scale(100, 100)
    a.axes("Quantity", "Price ($ per kg)")
    a.title("Lamb")
    S = L(a, 10, 12, 90, 88)
    D = L(a, 8, 85, 78, 15)
    D1 = L(a, 24, 85, 94, 15)
    e0, e1 = Fig.intersect(S, D), Fig.intersect(S, D1)
    hdrop(a, e0[0], e0[1], "P")
    vdrop(a, e0[0], e0[1], "Q")
    hdrop(a, e1[0], e1[1], sbt("P", 1))
    vdrop(a, e1[0], e1[1], sbt("Q", 1))
    draw(a, D, GREY)
    draw(a, D1, GREY)
    draw(a, S)
    a.dot(*e0, 3.6, INK)
    a.dot(*e1, 3.6, INK)
    a.label(S[1][0] + 6, S[1][1] - 6, "S", RED, 13)
    a.label(D[1][0] + 6, D[1][1] + 14, "D", GREY, 13)
    a.label(D1[1][0] + 6, D1[1][1] + 14, sbt("D", 1), GREY, 13)
    a.hshift(D, D1, a.py(72))
    a.hshift(D, D1, a.py(28))
    y_arrow(a, e0[1], e1[1])
    x_arrow(a, e0[0], e1[0])
    # ---- wool: supply shifts right (joint supply) ----
    b = Panel(f, 430, 0)
    b.scale(100, 100)
    b.axes("Quantity", "Price ($ per kg)")
    b.title("Wool")
    S = L(b, 6, 10, 78, 84)
    S1 = L(b, 24, 10, 96, 84)
    D = L(b, 8, 90, 90, 10)
    e0, e1 = Fig.intersect(S, D), Fig.intersect(S1, D)
    hdrop(b, e0[0], e0[1], "P")
    vdrop(b, e0[0], e0[1], "Q")
    hdrop(b, e1[0], e1[1], sbt("P", 1))
    vdrop(b, e1[0], e1[1], sbt("Q", 1))
    draw(b, D, GREY)
    draw(b, S)
    draw(b, S1)
    b.dot(*e0, 3.6, INK)
    b.dot(*e1, 3.6, INK)
    b.label(S[1][0] + 6, S[1][1] - 6, "S", RED, 13)
    b.label(S1[1][0] + 6, S1[1][1] - 6, sbt("S", 1), RED, 13)
    b.label(D[1][0] + 6, D[1][1] + 14, "D", GREY, 13)
    b.hshift(S, S1, b.py(72))
    b.hshift(S, S1, b.py(24))
    y_arrow(b, e0[1], e1[1])
    x_arrow(b, e0[0], e1[0])
    save("fig-5-4", f, "Figure 5.4: Joint supply (lamb and wool)",
         "Two diagrams: demand for lamb shifts right, raising its price and quantity along an unmoved supply curve; the supply curve for wool then shifts right, lowering the price of wool and raising the quantity.",
         "Lamb and wool are in joint supply. Left: an increase in demand for lamb shifts D to D<sub>1</sub>, raising the price from P to P<sub>1</sub> and the quantity from Q to Q<sub>1</sub>. "
         "Right: producing more lamb automatically produces more wool, so the supply of wool shifts right from S to S<sub>1</sub>, which lowers the price of wool from P to P<sub>1</sub> and raises the quantity from Q to Q<sub>1</sub>.")


def fig_5_5():
    f = Fig().scale(100, 100)
    f.axes("Quantity of tennis rackets", "Price of tennis rackets ($)")
    S = L(f, 12, 12, 92, 92)
    P0, P1 = f.py(68), f.py(38)
    q0, q1 = f.x_at(S, P0), f.x_at(S, P1)
    hdrop(f, q0, P0, "P")
    hdrop(f, q1, P1, sbt("P", 1))
    vdrop(f, q0, P0, "Q")
    vdrop(f, q1, P1, sbt("Q", 1))
    draw(f, S)
    f.dot(q0, P0)
    f.dot(q1, P1)
    f.label(S[1][0] + 6, S[1][1] - 6, "S", RED, 13)
    y_arrow(f, P0, P1)
    x_arrow(f, q0, q1)
    save("fig-5-5", f, "Figure 5.5: The supply of tennis rackets",
         "A single upward-sloping supply curve for tennis rackets with a movement down along it as price falls from P to P1, cutting quantity supplied from Q to Q1.",
         "A fall in the price of tennis rackets from P to P<sub>1</sub> causes a movement down along the supply curve S. Quantity supplied contracts from Q to Q<sub>1</sub>, and the curve itself does not move.")


def fig_5_6():
    f = Fig().scale(100, 100)
    f.axes("Quantity of laptops", "Price of laptops ($)")
    S = L(f, 46, 8, 84, 92)
    S1 = L(f, 26, 8, 64, 92)
    P = f.py(52)
    xs, xs1 = f.x_at(S, P), f.x_at(S1, P)
    hdrop(f, xs, P, "P")
    vdrop(f, xs, P, "Q")
    vdrop(f, xs1, P, sbt("Q", 1))
    draw(f, S)
    draw(f, S1)
    f.dot(xs, P)
    f.dot(xs1, P)
    f.label(S[1][0] + 6, S[1][1] - 6, "S", RED, 13)
    f.label(S1[1][0] + 6, S1[1][1] - 6, sbt("S", 1), RED, 13)
    f.hshift(S, S1, f.py(80))
    f.hshift(S, S1, f.py(24))
    save("fig-5-6", f, "Figure 5.6: The supply of laptops",
         "Two parallel supply curves for laptops, S1 to the left of S, with two leftward arrows and dashed lines showing quantity supplied falling from Q to Q1 at price P.",
         "A rise in the rent for factory space raises the costs of a large laptop maker, so at the existing price P it supplies less (Q<sub>1</sub> instead of Q). "
         "The whole curve shifts left from S to S<sub>1</sub>; a leftward shift means less is supplied at every price, and a rightward shift means more.")


def fig_5_7():
    f = Fig(w=860, h=760)
    prods = [
        ("Honey producer A", 0, 0, lambda p: 100 + 100 * (p - 2), "S" + sbt("", "A")),
        ("Honey producer B", 430, 0, lambda p: 100 + 50 * (p - 2), "S" + sbt("", "B")),
        ("Honey producer C", 0, 380, lambda p: 200 + 50 * (p - 2), "S" + sbt("", "C")),
    ]
    totals = {2: 0, 4: 0, 6: 0}
    for title, ox, oy, fn, lab in prods:
        p = Panel(f, ox, oy)
        p.scale(500, 7)
        p.axes("Quantity (jars per week)", "Price ($ per jar)")
        p.title(title)
        p.yticks([1, 2, 3, 4, 5, 6, 7])
        p.xticks([100, 200, 300, 400, 500])
        pts = [(fn(pr), pr) for pr in (2, 4, 6)]
        for pr in (2, 4, 6):
            totals[pr] += fn(pr)
        for q, pr in (pts[0], pts[2]):
            x, y = p.pt(q, pr)
            hdrop(p, x, y)
            vdrop(p, x, y)
        ln = L(p, pts[0][0], 2, pts[2][0], 6)
        draw(p, ln)
        for q, pr in pts:
            assert abs(Fig.y_at(ln, p.px(q)) - p.py(pr)) < 0.01
            p.dot(*p.pt(q, pr))
        p.label(p.px(pts[2][0]) + 8, p.py(6) - 8, lab, RED, 13)
    m = Panel(f, 430, 380)
    m.scale(1200, 7)
    m.axes("Quantity (jars per week)", "Price ($ per jar)")
    m.title("Total market")
    m.yticks([1, 2, 3, 4, 5, 6, 7])
    m.xticks([200, 400, 600, 800, 1000, 1200])
    pts = [(totals[pr], pr) for pr in (2, 4, 6)]
    assert [q for q, _ in pts] == [400, 800, 1200], pts
    for q, pr in (pts[0], pts[2]):
        x, y = m.pt(q, pr)
        hdrop(m, x, y)
        vdrop(m, x, y)
    ln = L(m, pts[0][0], 2, pts[2][0], 6)
    draw(m, ln)
    for q, pr in pts:
        assert abs(Fig.y_at(ln, m.px(q)) - m.py(pr)) < 0.01
        m.dot(*m.pt(q, pr))
    m.label(m.px(1200) + 8, m.py(6) - 8, "S" + sbt("", "M"), RED, 13)
    save("fig-5-7", f, "Figure 5.7: Individual supply curves and the market supply curve (horizontal summing)",
         "Four diagrams for honey producers A, B and C and the total market, showing that the market supply curve is the horizontal sum of the three individual supply curves.",
         "At $2 per jar the three producers supply 100, 100 and 200 jars a week, and at $6 they supply 400, 300 and 400. "
         "Adding quantities at each price (prices stay the same) gives the market supply curve S<sub>M</sub>: 400 jars a week at $2 and 1,200 at $6.")


def tp(l):
    return 3 * l ** 2 - 0.2 * l ** 3


def mp(l):
    return 6 * l - 0.6 * l ** 2


def ap(l):
    return 3 * l - 0.2 * l ** 2


def fig_5_8():
    f = Fig().scale(10, 100)
    f.axes("Quantity of labour (workers per day)", "Total product (bicycles per week)")
    f.yticks([20, 40, 60, 80, 100])
    f.xticks(list(range(1, 11)))
    xd, yd = f.pt(5, tp(5))
    hdrop(f, xd, yd, "50")
    f.line(xd, yd, xd, f.Y0, TEAL, 1.5, "5 4", "butt")
    f.curve([f.pt(l / 2, tp(l / 2)) for l in range(0, 21)])
    for l in range(1, 11):
        f.dot(*f.pt(l, tp(l)), 3.0)
    f.label(f.px(10) + 8, f.py(100) + 4, "TP", RED, 13)
    f.text(f.px(0.5), f.py(88), "Increasing returns:", 11.5, "start", GREY, italic=True)
    f.text(f.px(0.5), f.py(88) + 14, "TP rises faster and faster", 11.5, "start", GREY, italic=True)
    f.text(f.px(6.0), f.py(24), "Diminishing returns:", 11.5, "start", GREY, italic=True)
    f.text(f.px(6.0), f.py(24) + 14, "TP rises more slowly", 11.5, "start", GREY, italic=True)
    save("fig-5-8", f, "Figure 5.8: The total product curve",
         "Total product curve rising at an increasing rate up to 5 workers, then at a decreasing rate, flattening towards 100 bicycles a week at 10 workers.",
         "Adding workers to a fixed workshop, total product rises at first at an increasing rate, reaching 50 bicycles a week with 5 workers. "
         "After that it keeps rising but more and more slowly (diminishing returns), flattening out at 100 bicycles a week with 10 workers.")


def fig_5_9():
    f = Fig().scale(10, 20)
    f.axes("Quantity of labour (workers per day)", "Product per worker (bicycles per week)")
    f.yticks([5, 10, 15])
    f.xticks(list(range(1, 11)))
    xm, ym = f.pt(5, mp(5))
    hdrop(f, xm, ym)
    vdrop(f, xm, ym)
    ls = [l / 2 for l in range(0, 21)]
    f.curve([f.pt(l, ap(l)) for l in ls], GREY)
    f.curve([f.pt(l, mp(l)) for l in ls], RED)
    f.dot(xm, ym, 3.4, RED)
    xc, yc = f.pt(7.5, ap(7.5))
    assert abs(ap(7.5) - mp(7.5)) < 1e-9
    f.dot(xc, yc, 3.6, INK)
    f.text(xc, f.py(18.6), "MP cuts AP at the peak of AP", 11.5, "middle", INK)
    f.arrow(xc, f.py(18.6) + 6, xc, yc - 6, PURPLE, 1.6, 7)
    f.label(f.px(10) + 8, f.py(10) + 4, "AP", GREY, 13)
    f.label(f.px(9.6), f.py(4.0) + 4, "MP", RED, 13)
    save("fig-5-9", f, "Figure 5.9: Average and marginal product curves",
         "Marginal product (MP) and average product (AP) curves for labour: MP peaks at 5 workers, AP peaks at 7.5 workers, and MP cuts AP from above at AP's maximum.",
         "Marginal product (MP) rises to a peak of 15 bicycles at 5 workers and then falls as diminishing returns set in. "
         "Average product (AP) peaks later, at 7.5 workers, where MP crosses it; MP falls below AP and drags it down.")


def fig_5_10():
    f = Fig(w=420, h=500)
    steps = [
        ["To produce more output, a firm adds extra", "units of a variable factor (such as labour)", "to its fixed factors"],
        ["Eventually each extra unit of the variable", "factor adds less output than the one before:", "diminishing marginal returns"],
        ["So the extra cost of producing each further", "unit of output (marginal cost, MC) rises"],
        ["A firm will only supply more if the price", "rises enough to cover that higher MC"],
        ["Result: the supply curve slopes upward", "(the Law of Supply)"],
    ]
    bx, bw, bh, gap, y = 30, 360, 64, 34, 18
    for i, lines in enumerate(steps):
        box(f, bx, y, bw, bh, lines, 12.5, "#fdeaea" if i < 4 else "#e4f2e6", RED if i < 4 else "#2e7d4f")
        if i < 4:
            f.arrow(bx + bw / 2, y + bh + 4, bx + bw / 2, y + bh + gap - 4, INK, 2.2)
        y += bh + gap
    save("fig-5-10", f, "Figure 5.10: The logic chain behind the Law of Supply",
         "Flow chart of five boxes joined by downward arrows: adding a variable factor, diminishing returns, rising marginal cost, higher prices needed to supply more, so the supply curve slopes upward.",
         "Read from top to bottom: adding more of a variable factor leads to diminishing marginal returns, which pushes up marginal cost, "
         "so firms will supply more only at a higher price &mdash; the reason the supply curve slopes upward.")


def fig_5_11():
    f = Fig().scale(100, 100)
    f.axes("Quantity (millions of cans per month)", "Price per can (US $)")
    S1 = L(f, 16, 10, 50, 86)
    S2 = L(f, 42, 10, 76, 86)
    draw(f, S1, INK, 2.6)
    draw(f, S2, INK, 2.6)
    f.text(S1[1][0] + 12, S1[1][1] - 10, sbt("S", 1, " (with tax)"), 12.5, "end")
    f.text(S2[1][0] - 12, S2[1][1] - 10, sbt("S", 2, " (without tax)"), 12.5, "start")
    f.hshift(S1, S2, f.py(42))
    save("fig-5-11", f, "Diagram: effect of removing a tax on soft drinks",
         "Two parallel upward-sloping supply curves for soft drinks: S1 with the tax on the left and S2 without the tax on the right, with a rightward arrow between them.",
         "Removing a tax on soft drinks lowers producers&rsquo; costs, so supply shifts right from S<sub>1</sub> (with tax) to S<sub>2</sub> (without tax): "
         "more cans are supplied at every price.")


# =============================================================
# CHAPTER 6
# =============================================================
def fig_6_1():
    f = Fig().scale(100, 100)
    f.axes("Quantity supplied of product", "Price of product ($)")
    xq = f.px(50)
    P1, P2 = f.py(28), f.py(62)
    hdrop(f, xq, P1, sbt("P", 1))
    hdrop(f, xq, P2, sbt("P", 2))
    vdrop(f, xq, P1, None)
    f.text(xq, f.Y0 + 18, "Q", 11.5, "middle")
    f.line(xq, f.py(0), xq, f.py(95), RED, 2.8)
    f.dot(xq, P1)
    f.dot(xq, P2)
    f.label(xq + 8, f.py(95) + 8, "S", RED, 13)
    f.text(xq + 14, f.py(44), "PES = 0", 13, "start", INK, "600")
    f.text(xq + 14, f.py(44) + 15, "Q stays fixed at any price", 11, "start", GREY, italic=True)
    save("fig-6-1", f, "Figure 6.1: A perfectly inelastic supply curve (PES = 0)",
         "A vertical supply curve at quantity Q: quantity supplied is the same at prices P1 and P2, so PES = 0.",
         "A perfectly inelastic supply curve is vertical at Q. Whether the price is P<sub>1</sub>, P<sub>2</sub> or any other level, quantity supplied stays at Q, "
         "so the percentage change in quantity is zero and PES = 0.")


def fig_6_2():
    f = Fig().scale(100, 100)
    f.axes("Quantity supplied of product", "Price of product ($)")
    y = f.py(55)
    hdrop(f, f.px(5), y, sbt("P", 1))
    f.line(f.px(0), y, f.px(92), y, RED, 2.8)
    f.label(f.px(92) + 8, y + 5, "S", RED, 13)
    f.text(f.px(46), y - 14, "PES = " + INF, 13, "middle", INK, "600")
    f.text(f.px(46), y + 26, "Below P" + sbt("", 1) + ", nothing is supplied", 11, "middle", GREY, italic=True)
    save("fig-6-2", f, "Figure 6.2: A perfectly elastic supply curve (PES = infinity)",
         "A horizontal supply curve at price P1: any quantity is supplied at P1 and none below it, so PES is infinite.",
         "A perfectly elastic supply curve is horizontal at P<sub>1</sub>. Producers will supply any quantity at that price but nothing at all below it, "
         "so quantity supplied responds infinitely to a price change and PES = &infin;.")


def fig_6_3():
    f = Fig().scale(100, 100)
    f.axes("Quantity supplied", "Price of product ($)")
    S1 = L(f, 0, 0, 55, 88)
    S2 = L(f, 0, 0, 82, 49)
    S3 = L(f, 35, 0, 64, 85)
    S4 = L(f, 0, 30, 82, 58.7)
    draw(f, S1)
    draw(f, S2)
    draw(f, S3)
    draw(f, S4)
    f.text(S1[1][0] - 6, S1[1][1] - 8, sbt("S", 1, " (PES = 1)"), 12, "end", RED)
    f.text(S3[1][0] + 4, S3[1][1] - 8, sbt("S", 3, " (PES &lt; 1)"), 12, "start", RED)
    f.text(S4[1][0] + 8, S4[1][1] + 1, sbt("S", 4, " (PES &gt; 1)"), 12, "start", RED)
    f.text(S2[1][0] + 8, S2[1][1] + 4, sbt("S", 2, " (PES = 1)"), 12, "start", RED)
    save("fig-6-3", f, "Figure 6.3: Supply curves with different PES values",
         "Four straight-line supply curves: S1 and S2 pass through the origin (PES = 1), S3 starts on the quantity axis (PES below 1) and S4 starts on the price axis (PES above 1).",
         "Any straight-line supply curve through the origin (S<sub>1</sub> and S<sub>2</sub>) has PES = 1 along its whole length, however steep it is. "
         "S<sub>3</sub>, which cuts the quantity axis, is inelastic (PES &lt; 1), while S<sub>4</sub>, which cuts the price axis, is elastic (PES &gt; 1).")


# =============================================================
# CHAPTER 7
# =============================================================
D_TEA = (6, 94, 92, 8)
S_TEA = (6, 10, 92, 90)


def tea_lines(f):
    return L(f, *D_TEA), L(f, *S_TEA)


def fig_7_1():
    f = Fig().scale(100, 100)
    f.axes("Quantity of tea (tonnes per week)", "Price of tea ($ per kg)")
    D, S = tea_lines(f)
    draw(f, D, GREY)
    draw(f, S, RED)
    f.equilibrium(S, D, sbt("Q", "e"), sbt("P", "e"))
    f.label(S[1][0] + 6, S[1][1] - 6, "S", RED, 13)
    f.label(D[1][0] + 6, D[1][1] + 14, "D", GREY, 13)
    save("fig-7-1", f, "Figure 7.1: The market for tea",
         "Downward-sloping demand curve D and upward-sloping supply curve S crossing at the equilibrium price Pe and quantity Qe for tea.",
         "The demand curve D and supply curve S for tea intersect once, at equilibrium price P<sub>e</sub> and quantity Q<sub>e</sub>. "
         "At P<sub>e</sub> quantity demanded equals quantity supplied, so the market clears and stays there until an outside disturbance occurs.")


def fig_7_2():
    f = Fig(w=860, h=380)
    # (a) price too high -> excess supply
    a = Panel(f, 0, 0)
    a.scale(100, 100)
    a.axes("Quantity of tea (tonnes per week)", "Price of tea ($ per kg)")
    a.text(a.X0 + 12, 20, "(a)", 13, "start", GREY, "600")
    D, S = L(a, *D_TEA), L(a, *S_TEA)
    e = Fig.intersect(S, D)
    py1 = a.py(72)
    xd, xs = a.x_at(D, py1), a.x_at(S, py1)
    hdrop(a, e[0], e[1], sbt("P", "e"))
    hdrop(a, xs, py1, sbt("P", 1))
    vdrop(a, e[0], e[1], sbt("Q", "e"))
    vdrop(a, xd, py1, sbt("Q", 1))
    vdrop(a, xs, py1, sbt("Q", 2))
    draw(a, D, GREY)
    draw(a, S, RED)
    a.dot(*e, 3.6, INK)
    a.dot(xd, py1)
    a.dot(xs, py1)
    brace(a, xd, xs, py1 - 6, 9, up=True)
    a.text((xd + xs) / 2, py1 - 26, "Excess supply", 12, "middle")
    a.arrow(e[0], py1 + 4, e[0], e[1] - 6, PURPLE)
    a.label(S[1][0] + 6, S[1][1] - 6, "S", RED, 13)
    a.label(D[1][0] + 6, D[1][1] + 14, "D", GREY, 13)
    # (b) price too low -> excess demand
    b = Panel(f, 430, 0)
    b.scale(100, 100)
    b.axes("Quantity of tea (tonnes per week)", "Price of tea ($ per kg)")
    b.text(b.X0 + 12, 20, "(b)", 13, "start", GREY, "600")
    D, S = L(b, *D_TEA), L(b, *S_TEA)
    e = Fig.intersect(S, D)
    py2 = b.py(30)
    xd, xs = b.x_at(D, py2), b.x_at(S, py2)   # xs left, xd right
    hdrop(b, e[0], e[1], sbt("P", "e"))
    hdrop(b, xd, py2, sbt("P", 2))
    vdrop(b, e[0], e[1], sbt("Q", "e"))
    vdrop(b, xs, py2, sbt("Q", 3))
    vdrop(b, xd, py2, sbt("Q", 4))
    draw(b, D, GREY)
    draw(b, S, RED)
    b.dot(*e, 3.6, INK)
    b.dot(xd, py2)
    b.dot(xs, py2)
    brace(b, xs, xd, py2 + 6, 9)
    b.text(e[0] - 4, py2 + 34, "Excess", 12, "end")
    b.text(e[0] + 4, py2 + 34, "demand", 12, "start")
    b.arrow(e[0], py2 - 4, e[0], e[1] + 6, PURPLE)
    b.label(S[1][0] + 6, S[1][1] - 6, "S", RED, 13)
    b.label(D[1][0] + 6, D[1][1] + 14, "D", GREY, 13)
    save("fig-7-2", f, "Figure 7.2: The market for tea (disequilibrium and adjustment)",
         "Two diagrams of the tea market: (a) a price P1 above equilibrium creates excess supply Q2 minus Q1 and pushes price down; (b) a price P2 below equilibrium creates excess demand Q4 minus Q3 and pushes price up.",
         "(a) If sellers set a price P<sub>1</sub> above the equilibrium P<sub>e</sub>, consumers want only Q<sub>1</sub> but producers supply Q<sub>2</sub>, leaving excess supply (Q<sub>2</sub> &minus; Q<sub>1</sub>); price must fall. "
         "(b) At a price P<sub>2</sub> below P<sub>e</sub>, consumers want Q<sub>4</sub> but producers supply only Q<sub>3</sub>, leaving excess demand (Q<sub>4</sub> &minus; Q<sub>3</sub>); price must rise.")


def fig_7_3():
    f = Fig().scale(100, 100)
    f.axes("Quantity of e-bikes (thousands per year)", "Price of e-bikes ($)")
    D = L(f, 4, 89.4, 58, 13.8)
    D1 = L(f, 37, 89.4, 91, 13.8)
    S = L(f, 4, 15.6, 80, 84)
    e0, e1 = Fig.intersect(S, D), Fig.intersect(S, D1)
    y0 = e0[1]
    q2 = f.x_at(D1, y0)
    hdrop(f, e1[0], e1[1], sbt("P", "e1"))
    hdrop(f, q2, y0, sbt("P", "e"))
    vdrop(f, e0[0], e0[1], sbt("Q", "e"))
    vdrop(f, e1[0], e1[1], sbt("Q", "e1"))
    vdrop(f, q2, y0, sbt("Q", 2))
    draw(f, D, GREY)
    draw(f, D1, GREY)
    draw(f, S, RED)
    f.dot(*e0, 3.6, INK)
    f.dot(*e1, 3.6, INK)
    f.dot(q2, y0)
    f.line(e0[0] + 5, y0, q2 - 5, y0, BRACE, 4.5, cap="round")
    f.text(q2 + 10, y0 - 9, "Excess demand", 12, "start")
    f.arrow(e1[0], y0 - 5, e1[0], e1[1] + 7, PURPLE)
    f.label(S[1][0] + 6, S[1][1] - 6, "S", RED, 13)
    f.label(D[1][0] + 6, D[1][1] + 14, "D", GREY, 13)
    f.label(D1[1][0] + 6, D1[1][1] + 14, sbt("D", 1), GREY, 13)
    save("fig-7-3", f, "Figure 7.3: The market for e-bikes",
         "Demand for e-bikes shifts right from D to D1 against supply S; at the old price Pe there is excess demand Q2 minus Qe, so price rises to the new equilibrium Pe1.",
         "A rise in incomes shifts demand for e-bikes from D to D<sub>1</sub>. At the old price P<sub>e</sub> quantity demanded jumps to Q<sub>2</sub> while supply is still Q<sub>e</sub>, "
         "creating excess demand (Q<sub>2</sub> &minus; Q<sub>e</sub>). Price rises until the new equilibrium (P<sub>e1</sub>, Q<sub>e1</sub>) is reached.")


# --- records market: D: P = 30 - 1.5Q ; S: P = 3 + 0.75Q  -> equilibrium (12, 12) ---
def records(f, ticks=True):
    f.scale(20, 30)
    f.axes("Quantity of vinyl records (hundreds per week)", "Price per record ($)")
    f.yticks([20, 30])
    f.xticks([5, 10, 15, 20])
    D = L(f, 0, 30, 20, 0)
    S = L(f, 0, 3, 20, 18)
    return D, S


def fig_7_4():
    f = Fig()
    D, S = records(f)
    e = f.equilibrium(S, D, "12", "12")
    draw(f, D, GREY)
    draw(f, S, RED)
    f.dot(*e, 3.6, INK)
    f.label(D[1][0] + 6, D[1][1] - 6, "D", GREY, 13)
    f.label(S[1][0] + 6, S[1][1] - 6, "S", RED, 13)
    save("fig-7-4", f, "Figure 7.4: The market for vinyl records",
         "Demand D and supply S for vinyl records crossing at an equilibrium price of $12 and quantity of 1,200 records per week.",
         "Demand D slopes down from $30 and supply S slopes up from $3. They cross at the equilibrium price of $12 and an equilibrium quantity of 12 hundred (1,200) records per week.")


def fig_7_5():
    f = Fig()
    D, S = records(f)
    e = Fig.intersect(S, D)
    a, c = f.pt(0, 30), f.pt(0, 12)
    fill_poly(f, [a, c, e], CS_FILL)
    f.guide(e[0], e[1], "12", "12")
    draw(f, D, GREY)
    draw(f, S, RED)
    f.dot(*e, 3.6, INK)
    f.label(D[1][0] + 6, D[1][1] - 6, "D", GREY, 13)
    f.label(S[1][0] + 6, S[1][1] - 6, "S", RED, 13)
    f.text(a[0] + 6, a[1] - 5, "a", 12)
    f.text(c[0] + 5, c[1] + 15, "c", 12)
    f.text(e[0], e[1] - 10, "b", 12, "middle")
    f.text(f.px(6.8), f.py(26.5), "Consumer", 11.5, "start")
    f.text(f.px(6.8), f.py(26.5) + 14, "surplus", 11.5, "start")
    f.arrow(f.px(6.6), f.py(25.5), f.px(3.3), f.py(19), PURPLE, 1.8, 7)
    save("fig-7-5", f, "Figure 7.5: Consumer surplus in the market for vinyl records",
         "Demand and supply for vinyl records with the triangle above the $12 price and below the demand curve shaded as consumer surplus, labelled a, b and c.",
         "Consumer surplus is the shaded triangle abc: the area below the demand curve and above the $12 equilibrium price, out to the equilibrium quantity of 1,200 records. "
         "It shows how much more consumers were willing to pay than they actually had to.")


def fig_7_6():
    f = Fig()
    D, S = records(f)
    e = Fig.intersect(S, D)
    a, c, d = f.pt(0, 30), f.pt(0, 12), f.pt(0, 3)
    fill_poly(f, [a, c, e], CS_FILL)
    fill_poly(f, [c, d, e], PS_FILL)
    f.guide(e[0], e[1], "12", "12")
    draw(f, D, GREY)
    draw(f, S, RED)
    f.dot(*e, 3.6, INK)
    f.label(D[1][0] + 6, D[1][1] - 6, "D", GREY, 13)
    f.label(S[1][0] + 6, S[1][1] - 6, "S", RED, 13)
    f.text(a[0] + 6, a[1] - 5, "a", 12)
    f.text(c[0] + 5, c[1] - 5, "c", 12)
    f.text(d[0] + 6, d[1] + 15, "d", 12)
    f.text(e[0], e[1] - 10, "b", 12, "middle")
    f.text(f.px(6.8), f.py(26.5), "Consumer", 11.5, "start")
    f.text(f.px(6.8), f.py(26.5) + 14, "surplus", 11.5, "start")
    f.arrow(f.px(6.6), f.py(25.5), f.px(3.3), f.py(19), PURPLE, 1.8, 7)
    f.text(f.px(0.9), f.py(9.0), "Producer", 11.5, "start")
    f.text(f.px(0.9), f.py(9.0) + 14, "surplus", 11.5, "start")
    save("fig-7-6", f, "Figure 7.6: Producer surplus in the market for vinyl records",
         "Demand and supply for vinyl records with consumer surplus shaded above the $12 price and producer surplus shaded below it and above the supply curve.",
         "Producer surplus is the shaded triangle below the $12 equilibrium price and above the supply curve (points c, d and b): the amount by which the price received exceeds the minimum sellers would accept. "
         "Consumer surplus is shown above it for comparison.")


def fig_7_7():
    f = Fig(w=440, h=390, y1=52, x1=396)
    f.scale(100, 100)
    f.axes("Quantity (000s)", "Price ($)")
    D = L(f, 0, 95, 95, 0)          # P = 95 - Q
    S = L(f, 0, 15, 77, 92)         # P = 15 + Q  -> equilibrium (40, 55)
    e = Fig.intersect(S, D)
    a, b, d = f.pt(0, 95), f.pt(0, 55), f.pt(0, 15)
    fill_poly(f, [a, b, e], CS_FILL)
    fill_poly(f, [b, d, e], PS_FILL)
    f.guide(e[0], e[1], "Q", "P")
    draw(f, D, GREY)
    draw(f, S, RED)
    f.dot(*e, 3.6, INK)
    f.text(a[0] + 6, a[1] - 5, "a", 12)
    f.text(b[0] + 5, b[1] - 5, "b", 12)
    f.text(d[0] + 6, d[1] + 15, "d", 12)
    f.text(e[0], e[1] - 10, "c", 12, "middle")
    f.text(S[1][0] + 6, S[1][1] - 6, "S = MSC", 12, "start", RED)
    f.text(D[1][0] + 4, D[1][1] - 8, "D = MSB", 12, "start", GREY)
    f.text(f.px(38), f.py(78), "Consumer", 11.5, "start")
    f.text(f.px(38), f.py(78) + 14, "surplus", 11.5, "start")
    f.arrow(f.px(37.4), f.py(74), f.px(21), f.py(62), PURPLE, 1.8, 7)
    f.text(f.px(30), f.py(30), "Producer", 11.5, "start")
    f.text(f.px(30), f.py(30) + 14, "surplus", 11.5, "start")
    f.arrow(f.px(29.4), f.py(31), f.px(21), f.py(41), PURPLE, 1.8, 7)
    f.text(f.w / 2, 24, "Community surplus = consumer surplus + producer surplus", 12.5, "middle", INK, "600")
    save("fig-7-7", f, "Figure 7.7: Community surplus",
         "Marginal social benefit (demand) and marginal social cost (supply) curves meeting at point c, with consumer surplus and producer surplus shaded and together making community surplus.",
         "Demand is the marginal social benefit (MSB) curve and supply is the marginal social cost (MSC) curve. At the equilibrium (price P, quantity Q) consumer surplus (triangle abc) plus producer surplus (triangle bcd) "
         "gives the community surplus, which is greatest exactly where MSB = MSC.")


def fig_7_8():
    f = Fig()
    f.scale(2000, 120)
    f.axes("Quantity of smartwatches", "Price ($)")
    f.yticks([20, 40, 60, 80, 100, 120])
    f.xticks([500, 1000, 1500, 2000])
    D = L(f, 0, 120, 2000, 0)
    S = L(f, 0, 20, 2000, 100)
    e = Fig.intersect(S, D)
    assert abs(f.px(1000) - e[0]) < 0.01 and abs(f.py(60) - e[1]) < 0.01
    a, c, d = f.pt(0, 120), f.pt(0, 60), f.pt(0, 20)
    fill_poly(f, [a, c, e], CS_FILL)
    fill_poly(f, [c, d, e], PS_FILL)
    f.guide(e[0], e[1])
    draw(f, D, GREY)
    draw(f, S, RED)
    f.dot(*e, 3.6, INK)
    f.label(D[1][0] + 6, D[1][1] - 6, "D", GREY, 13)
    f.label(S[1][0] + 6, S[1][1] - 6, "S", RED, 13)
    f.text(f.px(760), f.py(105), "Consumer", 11.5, "start")
    f.text(f.px(760), f.py(105) + 14, "surplus", 11.5, "start")
    f.arrow(f.px(740), f.py(103), f.px(480), f.py(82), PURPLE, 1.8, 7)
    f.text(f.px(60), f.py(51), "Producer", 11.5, "start")
    f.text(f.px(60), f.py(51) + 14, "surplus", 11.5, "start")
    save("fig-7-8", f, "Figure 7.8: Calculating consumer and producer surplus",
         "Demand and supply for smartwatches crossing at $60 and 1,000 units, with consumer surplus (above $60) and producer surplus (below $60) shaded.",
         "Demand runs from $120 to 2,000 units and supply starts at $20; they meet at the equilibrium of $60 and 1,000 smartwatches. "
         "Consumer surplus is the triangle above $60: &frac12; &times; 1,000 &times; ($120 &minus; $60) = $30,000. "
         "Producer surplus is the triangle below $60: &frac12; &times; 1,000 &times; ($60 &minus; $20) = $20,000.")


def fig_7_9():
    f = Fig().scale(80, 45)
    f.axes("Quantity of lithium (thousand tonnes)", "Price of lithium ($000 per tonne)")
    S = L(f, 34, 3, 56, 36)
    D1 = L(f, 15, 32, 50, 4)      # P = 44 - 0.8Q
    D2 = L(f, 25, 42.4, 70, 6.4)  # P = 62.4 - 0.8Q
    e0, e1 = Fig.intersect(S, D1), Fig.intersect(S, D2)
    assert abs(e0[0] - f.px(40)) < 0.01 and abs(e0[1] - f.py(12)) < 0.01
    assert abs(e1[0] - f.px(48)) < 0.01 and abs(e1[1] - f.py(24)) < 0.01
    f.guide(*e0, "40", "12")
    f.guide(*e1, "48", "24")
    draw(f, D1, GREY)
    draw(f, D2, GREY)
    draw(f, S, RED)
    f.dot(*e0, 3.6, INK)
    f.dot(*e1, 3.6, INK)
    f.hshift(D1, D2, f.py(28))
    f.hshift(D1, D2, f.py(14))
    f.label(S[1][0] + 6, S[1][1] - 4, "Supply", RED, 12.5)
    f.label(D1[1][0] + 4, D1[1][1] + 14, sbt("D", 1), GREY, 13)
    f.label(D2[1][0] + 4, D2[1][1] + 14, sbt("D", 2), GREY, 13)
    save("fig-7-9", f, "Figure 7.9: The market for lithium",
         "Steep, inelastic lithium supply curve with demand shifting right from D1 to D2, raising price from $12,000 to $24,000 per tonne while quantity rises only from 40 to 48 thousand tonnes.",
         "Lithium supply is steep (inelastic) because new mines take years to open. When demand shifts right from D<sub>1</sub> to D<sub>2</sub> (for example because of electric-vehicle battery demand), "
         "price doubles from $12,000 to $24,000 per tonne while quantity rises only from 40 to 48 thousand tonnes.")


ALL = [fig_5_1, fig_5_2, fig_5_3, fig_5_4, fig_5_5, fig_5_6, fig_5_7, fig_5_8, fig_5_9,
       fig_5_10, fig_5_11, fig_6_1, fig_6_2, fig_6_3, fig_7_1, fig_7_2, fig_7_3,
       fig_7_4, fig_7_5, fig_7_6, fig_7_7, fig_7_8, fig_7_9]

if __name__ == "__main__":
    want = sys.argv[1:]
    for fn in ALL:
        if not want or fn.__name__[4:] in want:
            fn()
