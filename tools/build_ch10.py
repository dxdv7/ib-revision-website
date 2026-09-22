from figs_ch10_12 import *

# =============================================================== 10.1
def fig_10_1():
    cv = Cv("10-1")
    p = P(cv).scale(13, 1000)
    p.axes2("Output (units per week)", "Cost ($)")
    p.yticks([200, 400, 600, 800, 1000])
    p.xticks([2, 4, 6, 8, 10, 12], fmt=str)
    C = Cost(F=200)
    p.plot(lambda q: 200, 0, 12, BLUE, linear=True)
    p.lab(12, 200, "TFC", BLUE, 7, 4)
    a, b = p.plot(C.tvc, 0, 12, ORANGE)
    p.lab(12, C.tvc(12), "TVC", ORANGE, 7, 4)
    p.plot(C.tc, 0, 12, RED)
    p.lab(12, C.tc(12), "TC", RED, 7, 4)
    p.dpt(0, 200, C.tc, lambda q: 200)
    # bracket showing the constant $200 gap at q = 8
    q0 = 8
    lo, hi = C.tvc(q0), C.tc(q0)
    mid = (lo + hi) / 2
    x = p.px(q0)
    p.arrow(x, p.py(mid) - 3, x, p.py(hi) + 3, PURPLE, 1.8, 7)
    p.arrow(x, p.py(mid) + 3, x, p.py(lo) - 3, PURPLE, 1.8, 7)
    p.T(p.px(0.6), p.py(940), "TC stays a constant $200 above TVC", 11, "start", PURPLE, italic=True)
    p.T(p.px(0.6), p.py(870), "(the gap is TFC)", 11, "start", PURPLE, italic=True)
    emit(cv, "fig-10-1",
         "Figure 10.1: Total cost, total variable cost and total fixed cost",
         "Graph of TFC, TVC and TC against output: TFC is a flat line at $200, TVC starts at the origin and rises slowly then steeply, and TC runs exactly $200 above TVC starting from $200.",
         "TFC is a horizontal line at $200. TVC starts at the origin and rises slowly at first, then more steeply as diminishing marginal returns set in. TC is the vertical sum of the two, so it starts at $200 and stays exactly $200 above TVC at every output (for example TVC is $224 and TC is $424 at 8 units).")


# =============================================================== 10.2
def fig_10_2():
    cv = Cv("10-2")
    p = P(cv).scale(XM, 120)
    p.axes2("Output (units)", "Cost ($)")
    p.yticks([60, 90, 120])
    p.xticks([2, 4, 8, 10], fmt=str)
    C = C0
    a, b = p.plot(C.afc, 0.5, XM, GREY)
    p.lab(b, C.afc(b), "AFC", GREY, 6, 4)
    a, b = p.plot(C.mc, 0, 20, RED)
    p.lab(b, C.mc(b), "MC", RED, 6, 4)
    a, b = p.plot(C.atc, 0.4, XM, ORANGE)
    p.lab(b, C.atc(b), "ATC", ORANGE, 6, -1)
    a, b = p.plot(C.avc, 0, XM, GREEN)
    p.lab(b, C.avc(b), "AVC", GREEN, 6, 8)
    qa, ya = C.min_avc()
    qt, yt = C.min_atc()
    p.guide2(qa, ya, "6", "24")
    p.guide2(qt, yt, "7", "39")
    p.dpt(qa, ya, C.mc, C.avc)
    p.dpt(qt, yt, C.mc, C.atc)
    emit(cv, "fig-10-2",
         "Figure 10.2: Short-run AFC, AVC, ATC and MC curves",
         "Short-run cost curves: AFC falls throughout; AVC, ATC and MC are U-shaped, with MC cutting AVC at its minimum (6 units, $24) and ATC at its minimum (7 units, $39).",
         "AFC (= TFC/q, with TFC = $98) falls continuously. AVC, ATC and MC are U-shaped. MC has the lowest minimum (at 4 units) and cuts AVC exactly at the bottom of AVC (6 units, $24) and ATC exactly at the bottom of ATC (7 units, $39). ATC lies above AVC by the amount of AFC, so the gap narrows as output rises.")


# =============================================================== 10.3
def fig_10_3():
    cv = Cv("10-3")
    p = P(cv).scale(XM, YM)
    p.axes2("Output (units)", "Price/Cost ($)")
    C = C0
    a, b = p.plot(C.mc, 0, 20, RED)
    p.lab(b, C.mc(b), "MC", RED, 6, 4)
    a, b = p.plot(C.atc, 0.4, XM, ORANGE)
    p.lab(b, C.atc(b), "ATC", ORANGE, 6, -2)
    a, b = p.plot(C.avc, 0, XM, GREEN)
    p.lab(b, C.avc(b), "AVC", GREEN, 6, 10)
    qa, ya = C.min_avc()
    qt, yt = C.min_atc()
    p.dpt(qa, ya, C.mc, C.avc)
    p.dpt(qt, yt, C.mc, C.atc)
    p.T(p.px(XM) - 2, p.py(15), "MC cuts AVC and ATC", 11, "end", INKSOFT, italic=True)
    p.T(p.px(XM) - 2, p.py(6), "at their minimum points", 11, "end", INKSOFT, italic=True)
    emit(cv, "fig-10-3",
         "Figure 10.3: General short-run ATC, AVC and MC diagram",
         "General short-run cost diagram with U-shaped ATC, AVC and MC curves; MC passes through the minimum points of both AVC and ATC.",
         "The standard short-run cost diagram. MC reaches its minimum first, then rises and cuts AVC at the lowest point of AVC and ATC at the lowest point of ATC (marked with dots). ATC lies above AVC and the gap between them (AFC) narrows as output rises.")


# =============================================================== 10.4a
def fig_10_4a():
    cv = Cv("10-4a")
    p = P(cv).scale(10, 12)
    p.axes2("Quantity (units)", "Price ($)")
    p.yticks([2, 4, 6, 8, 10])
    p.xticks([2, 4, 6, 8, 10], fmt=str)
    p.plot(lambda q: 8, 0, 10, GREY, linear=True)
    p.lab(10, 8, "D = AR = MR", GREY, 4, -22, "end", 12.5)
    p.lab(10, 8, "(PED = &#8734;)", GREY, 4, -8, "end", 11.5)
    emit(cv, "fig-10-4a",
         "Figure 10.4(a): AR and MR when PED = infinity",
         "A single horizontal line at a price of $8 labelled D = AR = MR, showing perfectly elastic demand.",
         "With perfectly elastic demand (PED = infinity) the firm can sell any quantity at the going price of $8, so demand, average revenue and marginal revenue are all the same horizontal line at $8.")


# =============================================================== 10.4b
def fig_10_4b():
    cv = Cv("10-4b")
    p = P(cv).scale(10, 80)
    p.axes2("Quantity (units)", "Total revenue ($)")
    p.yticks([20, 40, 60, 80])
    p.xticks([2, 4, 6, 8, 10], fmt=str)
    TR = lambda q: 8 * q
    p.plot(TR, 0, 10, RED, linear=True)
    p.lab(10, 80, "TR", RED, 8, 6)
    p.guide2(5, 40, "5", None)
    p.dpt(5, 40, TR)
    p.T(p.px(0.5), p.py(76), "Each extra unit adds $8 to TR,", 11, "start", PURPLE, italic=True)
    p.T(p.px(0.5), p.py(69), "so MR is constant at $8.", 11, "start", PURPLE, italic=True)
    emit(cv, "fig-10-4b",
         "Figure 10.4(b): TR when PED = infinity",
         "Total revenue is an upward-sloping straight line through the origin, reaching $40 at 5 units, with slope equal to the constant price of $8.",
         "When demand is perfectly elastic at a price of $8, TR = 8 &times; q is a straight line through the origin (for example $40 at 5 units). Each extra unit adds a constant $8, so MR = $8 and equals the slope of TR.")


# =============================================================== 10.5
def fig_10_5():
    cv = Cv("10-5", w=440, h=590)
    A, B = 120.0, 6.0
    AR = lambda q: A - B * q
    MR = lambda q: A - 2 * B * q
    TR = lambda q: A * q - B * q * q
    top = P(cv, 76, 268, 410, 28).scale(20, 130, -80)
    top.axes2(None, "Price, AR and MR ($)", ylx=20, origin=None)
    top.yticks([-60, -30, 0, 30, 60, 90, 120])
    bot = P(cv, 76, 548, 410, 344).scale(20, 660)
    bot.axes2("Quantity (units)", "Total revenue ($)", ylx=20, xly=580)
    bot.yticks([200, 400, 600])
    bot.xticks([5, 10, 15, 20], fmt=str)
    # PED zones tint on the AR line region (drawn first)
    a, b = top.plot(AR, 0, 20, GREY, linear=True)
    top.lab(16.6, 33, "D = AR", GREY, 0, 0, "start")
    top.plot(MR, 0, 16, BLUE, linear=True, ymin=-80)
    top.lab(16, MR(16), "MR", BLUE, 8, 4)
    qm = 10.0
    assert abs(MR(qm)) < 1e-9 and abs(AR(qm) - 60) < 1e-9
    # vertical dashed from AR point through MR = 0 to the TR peak
    x = top.px(qm)
    bot.line(x, top.py(AR(qm)), x, bot.py(0), TEAL, 1.5, "5 4", "butt")
    top.dpt(qm, AR(qm), AR)
    top.dpt(qm, 0, MR)
    bot.plot(TR, 0, 20, RED)
    bot.lab(17.0, TR(17.0), "TR", RED, 8, -3, "start")
    bot.dpt(qm, TR(qm), TR)
    bot.T(bot.px(12.3), bot.py(640), "TR is maximised", 11.5, "start", PURPLE)
    bot.arrow(bot.px(12.2), bot.py(636), bot.px(qm) + 6, bot.py(TR(qm)) - 1, PURPLE, 1.6, 7)
    top.T(top.px(4.2), top.py(119), "PED &gt; 1", 12, "start", PURPLE, weight="600")
    top.T(top.px(4.2), top.py(109), "(MR &gt; 0, TR rising)", 10.5, "start", PURPLE)
    top.T(top.px(13.6), top.py(60), "PED &lt; 1", 12, "start", PURPLE, weight="600")
    top.T(top.px(13.6), top.py(50), "(MR &lt; 0, TR falling)", 10.5, "start", PURPLE)
    top.T(top.px(11.2), top.py(100), "PED = 1", 12, "start", PURPLE, weight="600")
    top.arrow(top.px(11.6), top.py(93), top.px(qm) + 5, top.py(AR(qm)) - 4, PURPLE, 1.6, 7)
    top.T(top.px(9.3), top.py(-24), "MR = 0", 11.5, "end", PURPLE, weight="600")
    top.arrow(top.px(9.1), top.py(-19), top.px(qm) - 2, top.py(0) + 5, PURPLE, 1.6, 7)
    emit(cv, "fig-10-5",
         "Figure 10.5: The relationship between D, AR, MR, TR and PED for a normal demand curve",
         "Two stacked graphs sharing a quantity axis: a straight demand curve AR with MR falling twice as steeply and crossing zero at 10 units, above a hump-shaped TR curve that peaks at 10 units where PED = 1.",
         "Top: AR = 120 &minus; 6q (price falls from $120 to zero at 20 units); MR = 120 &minus; 12q falls twice as steeply and reaches zero at 10 units. Bottom: TR = 120q &minus; 6q<sup>2</sup> rises while MR is positive (PED &gt; 1, left of 10 units), peaks at $600 at 10 units where MR = 0 and PED = 1, then falls where MR is negative (PED &lt; 1).")


# =============================================================== 10.6
def _box(cv, x, y, w, h, lines, size=12.5, weight="400", fill="#fdeaea", stroke=RED):
    cv.fig.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
    n = len(lines)
    lh = size + 3.5
    y0 = y + h / 2 - (n - 1) * lh / 2 + size * 0.35
    for i, s in enumerate(lines):
        cv.T(x + w / 2, y0 + i * lh, s, size, "middle", INK, weight)


def fig_10_6():
    cv = Cv("10-6", w=620, h=420)
    L, R = 30, 350
    lw, rw = 280, 250
    _box(cv, L, 14, lw, 44, ["At the point where PED = 1"], weight="600")
    _box(cv, L, 100, lw, 44, ["Total revenue is at its maximum"], weight="600")
    _box(cv, R, 100, rw, 44, ["MR = 0 at that quantity"])
    _box(cv, L, 186, lw, 50, ["So PED = 1 exactly where", "MR = 0 on a straight-line demand"], weight="600")
    _box(cv, R, 178, rw, 66, ["PED falls steadily as price", "falls along a straight-line", "demand curve"])
    cx = L + lw / 2
    cv.fig.arrow(cx, 60, cx, 98, INK, 2, 8)
    cv.fig.arrow(R - 2, 122, L + lw + 3, 122, INK, 2, 8)
    cv.fig.arrow(cx, 146, cx, 184, INK, 2, 8)
    cv.fig.arrow(R - 2, 211, L + lw + 3, 211, INK, 2, 8)
    bl, br = 40, 330
    bw = 250
    _box(cv, bl, 316, bw, 84, ["To the left of that point", "(higher prices, smaller quantities)", "PED is greater than 1:", "demand is elastic"], size=12)
    _box(cv, br, 316, bw, 84, ["To the right of that point", "(lower prices, larger quantities)", "PED is less than 1:", "demand is inelastic"], size=12)
    cv.fig.line(cx, 238, cx, 272, INK, 2, cap="butt")
    cv.fig.line(bl + bw / 2, 272, br + bw / 2, 272, INK, 2, cap="butt")
    cv.fig.arrow(bl + bw / 2, 272, bl + bw / 2, 314, INK, 2, 8)
    cv.fig.arrow(br + bw / 2, 272, br + bw / 2, 314, INK, 2, 8)
    emit(cv, "fig-10-6",
         "Figure 10.6: Logic tree explaining the relationship between PED and TR on a demand curve",
         "Logic tree: PED = 1 where TR is maximised and MR = 0; PED falls as price falls, so PED is greater than 1 to the left of that point and less than 1 to the right.",
         "Reading the tree from the top: TR is at its maximum where PED = 1, and that is also where MR = 0. Because PED falls as price falls along a straight-line demand curve, PED is greater than 1 (elastic) to the left of that point and less than 1 (inelastic) to the right.")


# =============================================================== 10.7a / 10.7b
PRICE_7 = 36.0

def fig_10_7a():
    cv = Cv("10-7a")
    p = P(cv).scale(XM, YM)
    p.axes2("Output (units)", "Price/Cost ($)")
    C = C0
    Pp = PRICE_7
    price = lambda q: Pp
    cs = crosses(C.mc, price, 0, 12)
    assert len(cs) == 2
    (q0, _), (q1, _) = cs
    qend = p.plot(C.mc, 0, 20, RED, ymax=YM)[1]
    # shading (below curves)
    p.shade(C.mc, price, 0, q0, LOSS)
    p.shade(price, C.mc, q0, q1, PROFIT)
    p.shade(C.mc, price, q1, qend, LOSS)
    p.plot(price, 0, XM, GREY, linear=True)
    p.plot(C.mc, 0, 20, RED)
    p.lab(qend, C.mc(qend), "MC", RED, 6, 4)
    p.lab(XM, Pp, "D = AR = MR", GREY, 4, -8, "end")
    for q in (q0, q1):
        p.guide2(q, Pp, None, None)
    p.guide2(q0, Pp, "q" + sq("", 0), "P")
    p.guide2(q1, Pp, "q" + sq("", 1), None, to_y=False)
    p.dpt(q0, Pp, C.mc, price)
    p.dpt(q1, Pp, C.mc, price)
    yy = 100
    for i, (fill, s) in enumerate([(PROFIT, "MC &lt; MR between q" + sq("", 0) + " and q" + sq("", 1) + ":"),
                                   (PROFIT, "each extra unit adds to profit"),
                                   (LOSS, "MC &gt; MR outside that range:"),
                                   (LOSS, "each extra unit reduces profit")]):
        cv.fig.add(f'<rect x="{p.px(0.35):.1f}" y="{p.py(yy - 8.2 * i) - 8:.1f}" width="10" height="9" fill="{fill}" stroke="{TEAL}" stroke-width="1"/>')
        p.T(p.px(0.35) + 15, p.py(yy - 8.2 * i), s, 10.8, "start", INKSOFT)
    emit(cv, "fig-10-7a",
         "Figure 10.7(a): Revenue and costs for a firm with a perfectly elastic demand curve (full MC curve shown)",
         "A U-shaped MC curve cuts the horizontal D = AR = MR line at a price of $36 at two outputs, q0 on its falling part and q1 on its rising part; MC is below MR between them.",
         "The horizontal line D = AR = MR at P = $36 is cut twice by the U-shaped MC curve, at q<sub>0</sub> (about 1.2 units) and q<sub>1</sub> (about 6.8 units). Between them MC &lt; MR, so every extra unit adds to profit (blue). Below q<sub>0</sub> and beyond q<sub>1</sub> MC &gt; MR (pink), so extra units reduce profit. Profit is therefore maximised at q<sub>1</sub>, where MC = MR with MC rising.")


def fig_10_7b():
    cv = Cv("10-7b")
    p = P(cv).scale(XM, YM)
    p.axes2("Output (units)", "Price/Cost ($)")
    C = C0
    Pp = PRICE_7
    price = lambda q: Pp
    q1 = cross1(C.mc, price, 4.5, 12)[0]
    p.plot(price, 0, XM, GREY, linear=True)
    p.lab(XM, Pp, "D = AR = MR", GREY, 4, -8, "end")
    a, b = p.plot(C.mc, 5.0, 20, RED)
    p.lab(b, C.mc(b), "MC", RED, 6, 4)
    p.guide2(q1, Pp, "q", "P")
    p.dpt(q1, Pp, C.mc, price)
    emit(cv, "fig-10-7b",
         "Figure 10.7(b): Simplified diagram (only the profit-maximizing output shown)",
         "Simplified diagram: the rising part of MC cuts the horizontal D = AR = MR line at price P; profit is maximised at output q.",
         "Only the rising part of the MC curve is drawn. It cuts the horizontal D = AR = MR line (price P = $36) at the profit-maximising output q, about 6.8 units.")


# =============================================================== 10.8 / 10.9 / 10.10
A8, B8 = 100.0, 6.0

def _mono_base(cv, atc=None, ar_label="D = AR"):
    p = P(cv).scale(XM, YM)
    p.axes2("Output (units)", "Price/Cost ($)")
    return p


def fig_10_8():
    cv = Cv("10-8")
    p = _mono_base(cv)
    C = C0
    AR, MR = dem(A8, B8)
    q, ym = cross1(MR, C.mc, 4.5, 9)
    price = AR(q)
    p.plot(AR, 0, XM, GREY, linear=True)
    p.lab(XM, AR(XM), "D = AR", GREY, 6, 4, "start")
    p.plot(MR, 0, A8 / (2 * B8), BLUE, linear=True)
    p.lab(A8 / (2 * B8), 0, "MR", BLUE, 6, -6)
    a, b = p.plot(C.mc, 0, 20, RED)
    p.lab(b, C.mc(b), "MC", RED, 6, 4)
    p.guide2(q, price, "q", "p")
    p.dpt(q, ym, MR, C.mc)
    p.dpt(q, price, AR)
    emit(cv, "fig-10-8",
         "Figure 10.8: The profit-maximizing level of output for a normal demand curve",
         "Downward-sloping D = AR, a steeper MR line and a U-shaped MC curve; MC cuts MR at output q, and price p is read up from q to the demand curve.",
         "MR starts at the same price intercept as D = AR but falls twice as steeply. Profit is maximised at output q, where the rising MC curve cuts MR. Go up from q to the demand curve (AR) and across to the price axis to find the price p that the firm charges.")


def fig_10_9():
    cv = Cv("10-9")
    p = _mono_base(cv)
    C = C0
    AR, MR = dem(A8, B8)
    q, ym = cross1(MR, C.mc, 4.5, 9)
    price, avg = AR(q), C.atc(q)
    assert price > avg
    p.rect(0, q, avg, price, PROFIT)
    p.plot(AR, 0, XM, GREY, linear=True)
    p.lab(XM, AR(XM), "D = AR", GREY, 6, 4, "start")
    p.plot(MR, 0, A8 / (2 * B8), BLUE, linear=True)
    p.lab(A8 / (2 * B8), 0, "MR", BLUE, 6, -6)
    a, b = p.plot(C.mc, 0, 20, RED)
    p.lab(b, C.mc(b), "MC", RED, 6, 4)
    a, b = p.plot(C.atc, 0.6, XM, ORANGE)
    p.lab(b, C.atc(b), "AC", ORANGE, 6, -2)
    p.guide2(q, price, "q", "p")
    p.hline(avg, 0, q)
    p.T(p.X0 - 8, p.py(avg) + 4, "a", 11.5, "end")
    p.dpt(q, price, AR)
    p.dpt(q, avg, C.atc)
    p.dpt(q, ym, MR, C.mc)
    profit_rect_label(p, 1.05, 3.0, avg, price, ["Abnormal", "profit"])
    emit(cv, "fig-10-9",
         "Figure 10.9: Using the AC curve to show profit (Abnormal profit case)",
         "MC, AC, D = AR and MR with the profit-maximising output q where MC = MR; the shaded rectangle between price p and average cost a, of width q, is abnormal profit.",
         "The U-shaped AC curve is drawn so that MC cuts it at its minimum. At the profit-maximising output q (where MC = MR) the price is p (read from AR) and the average cost is a (read from AC). Because p &gt; a, the shaded rectangle of height (p &minus; a) and width q is the total abnormal profit.")


def fig_10_10():
    cv = Cv("10-10")
    p = _mono_base(cv)
    C = C0
    AR, MR = dem(A8, B8)
    q, ym = cross1(MR, C.mc, 4.5, 9)
    price = AR(q)
    F2 = (price - C.avc(q)) * q            # ATC passes exactly through (q, price)
    C1 = C.with_F(F2)
    Cprofit = C.with_F(0.42 * F2)
    Closs = C.with_F(1.6 * F2)
    assert abs(C1.atc(q) - price) < 1e-9
    cq, cq2 = Cprofit.atc(q), Closs.atc(q)
    assert cq < price < cq2
    p.rect(0, q, cq, price, PROFIT)
    p.rect(0, q, price, cq2, LOSS)
    p.plot(AR, 0, XM, GREY, linear=True)
    p.lab(XM, AR(XM), "D = AR", GREY, 6, 4, "start")
    p.plot(MR, 0, A8 / (2 * B8), BLUE, linear=True)
    p.lab(A8 / (2 * B8), 0, "MR", BLUE, 6, -6)
    a, b = p.plot(C.mc, 0, 20, RED)
    p.lab(b, C.mc(b), "MC", RED, 6, 4)
    for Cx, col, name, lo, dx, dy in [(Cprofit, "#e6a23c", "AC", 0.6, 6, 12),
                                       (C1, ORANGE, "AC" + sq("", 1), 0.9, 6, -2),
                                       (Closs, "#b8651b", "AC" + sq("", 2), 2.6, 6, -2)]:
        a, b = p.plot(Cx.atc, lo, XM, col)
        p.lab(b, Cx.atc(b), name, col, dx, dy)
        qmin, ymin_ = argmin(Cx.atc, 0.6, 15)
        assert abs(C.mc(qmin) - ymin_) < 1e-4       # MC cuts every AC curve at its minimum
    p.guide2(q, cq2, "q", None, to_y=False)
    p.hline(cq, 0, q); p.hline(price, 0, q); p.hline(cq2, 0, q)
    p.T(p.X0 - 8, p.py(cq) + 4, "c", 11.5, "end")
    p.T(p.X0 - 8, p.py(price) + 4, "c" + sq("", 1) + " = p", 11.5, "end")
    p.T(p.X0 - 8, p.py(cq2) + 4, "c" + sq("", 2), 11.5, "end")
    p.dpt(q, price, AR, C1.atc)
    p.dpt(q, cq, Cprofit.atc)
    p.dpt(q, cq2, Closs.atc)
    p.dpt(q, ym, MR, C.mc)
    p.T(p.px(q) + 6, p.py(cq) + 14, "b", 11.5, "start")
    p.T(p.px(q) + 6, p.py(price) + 14, "a", 11.5, "start")
    p.T(p.px(q) + 6, p.py(cq2) - 5, "d", 11.5, "start")
    # legend
    lx, ly = p.px(6.9), p.py(30)
    cv.fig.add(f'<rect x="{lx:.1f}" y="{ly-9:.1f}" width="12" height="10" fill="{PROFIT}" stroke="{TEAL}" stroke-width="1"/>')
    cv.T(lx + 18, ly, "Abnormal profit (AC)", 10.8, "start", INKSOFT)
    cv.fig.add(f'<rect x="{lx:.1f}" y="{ly+7:.1f}" width="12" height="10" fill="{LOSS}" stroke="#d9432f" stroke-width="1"/>')
    cv.T(lx + 18, ly + 16, "Loss (AC" + sq("", 2) + ")", 10.8, "start", INKSOFT)
    emit(cv, "fig-10-10",
         "Figure 10.10: Using AC to show different profit and loss situations",
         "At the profit-maximising output q, three AC curves show abnormal profit (AC through b below price), normal profit (AC1 through a at price p) and a loss (AC2 through d above p).",
         "Output q (where MC = MR) and price p are fixed. If average cost at q is c (point b, below p) the rectangle between c and p is abnormal profit. If AC<sub>1</sub> passes through a, so that c<sub>1</sub> = p, there is only normal profit. If AC<sub>2</sub> passes above p at d (cost c<sub>2</sub>) the rectangle between p and c<sub>2</sub> is a loss. MC cuts each AC curve at its minimum.")


if __name__ == "__main__":
    for f in [fig_10_1, fig_10_2, fig_10_3, fig_10_4a, fig_10_4b, fig_10_5, fig_10_6,
              fig_10_7a, fig_10_7b, fig_10_8, fig_10_9, fig_10_10]:
        f()
