from figs_ch10_12 import *

C = C0
QMIN, PMIN = C.min_atc()            # 7, 39
SLOPE_S = 5.0
W2, H2 = 860, 380


# ---------------------------------------------------------------- two-panel helpers
def two_panels(name):
    cv = Cv(name, W2, H2)
    ind = P(cv, 72, 318, 352, 46).scale(13, YM)
    ind.axes2("Quantity", "Price ($)", ylx=20, title="The industry", xly=374)
    firm = P(cv, 452, 318, 752, 46).scale(XM, YM)
    firm.axes2("Quantity", "Price ($)", ylx=402, title="The firm", xly=374)
    return cv, ind, firm


def sd(Pe, Qe, d, s=SLOPE_S):
    S = lambda q: Pe + s * (q - Qe)
    D = lambda q: Pe - d * (q - Qe)
    return S, D


def draw_sd(ind, S, D, s_label="S", d_label="D", s_color=RED, s_dx=6):
    a, b = ind.plot(D, 0, 13, GREY, linear=True)
    ind.lab(b, D(b), d_label, GREY, 6, -6 if D(b) < 1 else 4)
    a, b = ind.plot(S, 0, 13, s_color, linear=True)
    ind.lab(b, S(b), s_label, s_color, s_dx, 4)


def eq_industry(ind, S, D, xl="Q", yl="P", xrow=0, ydy=0, guide_color=True):
    q, y = cross1(S, D, 0, 13)
    ind.guide2(q, y, xl, yl, xrow=xrow, ydy=ydy)
    ind.dpt(q, y, S, D)
    return q, y


def firm_d(fp, price, label, color=GREY, dx=8, dy=1, anchor="start", at=None):
    fp.plot(lambda q: price, 0, XM, color, linear=True)
    if label:
        q = XM if at is None else at
        fp.lab(q, price, label, color, dx, dy, anchor)


# scenario numbers ------------------------------------------------------------
P_SR = 60.0                                     # short-run profit price: MC = 60 at q = 8
Q_SR_PROFIT = cross1(C.mc, lambda q: P_SR, 4.5, 12)[0]          # 8.0
C_SR_PROFIT = C.atc(Q_SR_PROFIT)                                 # 40.25
P_LOSS = 28.0
Q_SR_LOSS = cross1(C.mc, lambda q: P_LOSS, 4.5, 12)[0]           # ~6.31
C_SR_LOSS = C.atc(Q_SR_LOSS)
assert P_LOSS > C.avc(Q_SR_LOSS)                # still covers AVC
assert C_SR_LOSS > P_LOSS and C_SR_PROFIT < P_SR


def rect_label(p, q0, q1, y0, y1, lines, size=10.3):
    profit_rect_label(p, q0, q1, y0, y1, lines, size)


def legend_swatch(cv, x, y, fill, text, stroke=TEAL):
    cv.fig.add(f'<rect x="{x:.1f}" y="{y-9:.1f}" width="12" height="10" fill="{fill}" stroke="{stroke}" stroke-width="1"/>')
    cv.T(x + 18, y, text, 10.8, "start", INKSOFT)


# ================================================================= 11.1
def fig_11_1():
    cv, ind, fp = two_panels("11-1")
    Q, Pe, d = 4.5, P_SR, 8.0
    S, D = sd(Pe, Q, d)
    draw_sd(ind, S, D)
    q, y = eq_industry(ind, S, D)
    firm_d(fp, Pe, "D = AR = MR")
    fp.T(fp.X0 - 8, fp.py(Pe) + 4, "P", 11.5, "end")
    emit(cv, "fig-11-1",
         "Figure 11.1: The demand curves for the industry and the firm in perfect competition",
         "Two graphs: the industry, where downward-sloping demand D and upward-sloping supply S meet at price P and quantity Q; and the firm, whose demand D = AR = MR is a horizontal line at the industry price P.",
         "In the industry graph, supply S and demand D determine the market price P and quantity Q. The individual firm is a price taker: at that price it can sell any quantity it likes, so its demand curve D = AR = MR is a horizontal line at P (note the firm&rsquo;s quantity axis is on a much smaller scale).")


# ================================================================= 11.2
def fig_11_2():
    cv, ind, fp = two_panels("11-2")
    Q, Pe, d = 4.5, P_SR, 8.0
    S, D = sd(Pe, Q, d)
    draw_sd(ind, S, D)
    eq_industry(ind, S, D)
    price = lambda q: Pe
    firm_d(fp, Pe, "D = AR = MR")
    a, b = fp.plot(C.mc, 2.0, 20, RED)
    fp.lab(b, C.mc(b), "MC", RED, 6, 4)
    q, y = cross1(C.mc, price, 4.5, 12)
    fp.guide2(q, y, "q", "P")
    fp.dpt(q, y, C.mc, price)
    fp.T(fp.px(0.4), fp.py(99), "Firm output q is tiny next to", 10.5, "start", INKSOFT, italic=True)
    fp.T(fp.px(0.4), fp.py(92), "industry output Q (not to scale)", 10.5, "start", INKSOFT, italic=True)
    emit(cv, "fig-11-2",
         "Figure 11.2: The profit-maximizing level of output in perfect competition",
         "Industry supply and demand set price P; the firm takes P as its horizontal D = AR = MR line and maximises profit at output q where the rising MC curve cuts it.",
         "The firm takes the market price P from the industry graph, so P = D = AR = MR. Profit is maximised at output q, where MC = MR. Firm output q is only a tiny fraction of industry output Q; if it were large enough to shift industry supply the firm would have market power.")


# ================================================================= 11.3
def _profit_firm(fp, q, price, cst, label_rect=True):
    """Firm panel with MC, AC, D = AR = MR and a shaded profit rectangle."""
    fp.rect(0, q, cst, price, PROFIT)
    firm_d(fp, price, "D = AR = MR")
    a, b = fp.plot(C.mc, 0, 20, RED)
    fp.lab(b, C.mc(b), "MC", RED, 6, 4)
    a, b = fp.plot(C.atc, 0.4, XM, ORANGE)
    fp.lab(b, C.atc(b), "AC", ORANGE, 6, 5)
    fp.guide2(q, price, "q", "P")
    fp.hline(cst, 0, q)
    fp.dpt(q, price, C.mc, lambda x: price)
    fp.dpt(q, cst, C.atc)


def fig_11_3():
    cv, ind, fp = two_panels("11-3")
    Q, Pe, d = 4.5, P_SR, 8.0
    S, D = sd(Pe, Q, d)
    draw_sd(ind, S, D)
    eq_industry(ind, S, D)
    _profit_firm(fp, Q_SR_PROFIT, P_SR, C_SR_PROFIT)
    fp.T(fp.X0 - 8, fp.py(C_SR_PROFIT) + 4 + 3, "C", 11.5, "end")
    rect_label(fp, 1.0, 3.3, C_SR_PROFIT, P_SR, ["Abnormal", "profit"])
    emit(cv, "fig-11-3",
         "Figure 11.3: Short-run abnormal profits in perfect competition",
         "The industry sets price P; the firm produces at q where MC = MR, and because average cost C is below P at q the shaded rectangle between P and C is abnormal profit.",
         "The firm produces at q, where MC = MR = P. At q the average cost C read from the AC curve is below the price P, so the firm earns an abnormal profit of (P &minus; C) per unit, shown by the shaded rectangle of height (P &minus; C) and width q. The MC curve cuts AC at its minimum.")


# ================================================================= 11.4
def _loss_firm(fp, q, price, cst):
    fp.rect(0, q, price, cst, LOSS)
    firm_d(fp, price, "D = AR = MR")
    a, b = fp.plot(C.mc, 0, 20, RED)
    fp.lab(b, C.mc(b), "MC", RED, 6, 4)
    a, b = fp.plot(C.atc, 0.4, XM, ORANGE)
    fp.lab(b, C.atc(b), "AC", ORANGE, 6, 5)
    fp.guide2(q, cst, "q", "C")
    fp.hline(price, 0, q)
    fp.T(fp.X0 - 8, fp.py(price) + 4, "P", 11.5, "end")
    fp.dpt(q, price, C.mc, lambda x: price)
    fp.dpt(q, cst, C.atc)


def fig_11_4():
    cv, ind, fp = two_panels("11-4")
    Q, Pe, d = 5.0, P_LOSS, 6.9
    S, D = sd(Pe, Q, d)
    draw_sd(ind, S, D)
    eq_industry(ind, S, D)
    _loss_firm(fp, Q_SR_LOSS, P_LOSS, C_SR_LOSS)
    rect_label(fp, 2.2, 5.8, P_LOSS, C_SR_LOSS, ["Losses"], size=11)
    emit(cv, "fig-11-4",
         "Figure 11.4: Short-run losses in perfect competition",
         "The firm takes price P and produces at q where MC = MR, but average cost C at q is above P, so the shaded rectangle between C and P is a loss.",
         "The firm sells at the market price P and maximises profit (here, minimises loss) at q where MC = MR. At q the average cost C is greater than P, so it makes a loss of (C &minus; P) per unit, shown by the shaded rectangle. It still produces because P covers average variable cost, so producing loses less than closing.")


# ================================================================= 11.5
def fig_11_5():
    cv, ind, fp = two_panels("11-5")
    Q, Pe = 4.5, P_SR
    Q1 = 7.1
    d = (Pe - PMIN) / (Q1 - Q)
    S, D = sd(Pe, Q, d)
    S1 = lambda q: PMIN + SLOPE_S * (q - Q1)
    q1_, p1_ = cross1(S1, D, 0, 13)
    assert abs(p1_ - PMIN) < 1e-6
    draw_sd(ind, S, D)
    a, b = ind.plot(S1, 0, 13, RED, linear=True)
    ind.lab(b, S1(b), "S" + sq("", 1), RED, 6, 4)
    ind.guide2(Q, Pe, "Q", "P", xrow=0)
    ind.guide2(q1_, p1_, "Q" + sq("", 1), "P" + sq("", 1))
    ind.dpt(Q, Pe, S, D)
    ind.dpt(q1_, p1_, S1, D)
    yv = 66
    ind.hshift(ind.pline(S), ind.pline(S1), ind.py(yv))
    # firm
    Pl = lambda q: Pe
    P1l = lambda q: PMIN
    fp.rect(0, Q_SR_PROFIT, C_SR_PROFIT, Pe, PROFIT)
    firm_d(fp, Pe, "D = AR = MR")
    firm_d(fp, PMIN, None)
    fp.lab(XM, PMIN, "D" + sq("", 1) + " = AR" + sq("", 1) + " = MR" + sq("", 1), GREY, 8, 1, "start", 12.5)
    a, b = fp.plot(C.mc, 0, 20, RED)
    fp.lab(b, C.mc(b), "MC", RED, 6, 4)
    a, b = fp.plot(C.atc, 0.4, XM, ORANGE)
    fp.lab(b, C.atc(b), "AC", ORANGE, 6, 5)
    qt, yt = C.min_atc()
    fp.guide2(Q_SR_PROFIT, Pe, "q", "P")
    fp.guide2(qt, yt, "q" + sq("", 1), "P" + sq("", 1) + " = C" + sq("", 1), xrow=1, ydy=6)
    fp.hline(C_SR_PROFIT, 0, Q_SR_PROFIT)
    fp.T(fp.X0 - 8, fp.py(C_SR_PROFIT) + 4 - 9, "C", 11.5, "end")
    fp.dpt(Q_SR_PROFIT, Pe, C.mc, Pl)
    fp.dpt(Q_SR_PROFIT, C_SR_PROFIT, C.atc)
    fp.dpt(qt, yt, C.mc, C.atc, P1l)
    fp.vshift(fp.pline(Pl), fp.pline(P1l), fp.px(1.6))
    legend_swatch(cv, fp.px(6.3), fp.py(14), PROFIT, "Abnormal profit at q")
    emit(cv, "fig-11-5",
         "Figure 11.5: The movement from short-run abnormal profit to long-run normal profit",
         "Abnormal profit attracts entry: industry supply shifts right from S to S1, price falls from P to P1, and each firm's demand line falls until it touches the minimum of AC at output q1, where price equals average cost.",
         "In the short run the firm earns the shaded abnormal profit at price P and output q. Profit attracts new firms, so industry supply shifts right from S to S<sub>1</sub>, lowering the price to P<sub>1</sub> and raising industry output to Q<sub>1</sub>. The firm&rsquo;s demand line falls to D<sub>1</sub> = AR<sub>1</sub> = MR<sub>1</sub>, which just touches the bottom of AC where MC = MR at q<sub>1</sub>; P<sub>1</sub> = C<sub>1</sub> and only normal profit remains.")


# ================================================================= 11.6
def fig_11_6():
    cv, ind, fp = two_panels("11-6")
    Q, Pe = 5.0, P_LOSS
    Q1 = 3.4
    d = (PMIN - Pe) / (Q - Q1)
    S, D = sd(Pe, Q, d)
    S1 = lambda q: PMIN + SLOPE_S * (q - Q1)
    q1_, p1_ = cross1(S1, D, 0, 13)
    assert abs(p1_ - PMIN) < 1e-6
    draw_sd(ind, S, D)
    a, b = ind.plot(S1, 0, 13, RED, linear=True)
    ind.lab(b, S1(b), "S" + sq("", 1), RED, 6, 4)
    ind.guide2(Q, Pe, "Q", "P")
    ind.guide2(q1_, p1_, "Q" + sq("", 1), "P" + sq("", 1), xrow=1)
    ind.dpt(Q, Pe, S, D)
    ind.dpt(q1_, p1_, S1, D)
    ind.hshift(ind.pline(S), ind.pline(S1), ind.py(50))
    Pl = lambda q: Pe
    P1l = lambda q: PMIN
    fp.rect(0, Q_SR_LOSS, Pe, C_SR_LOSS, LOSS)
    firm_d(fp, Pe, "D = AR = MR")
    firm_d(fp, PMIN, None)
    fp.lab(XM, PMIN, "D" + sq("", 1) + " = AR" + sq("", 1) + " = MR" + sq("", 1), GREY, 8, 1, "start", 12.5)
    a, b = fp.plot(C.mc, 0, 20, RED)
    fp.lab(b, C.mc(b), "MC", RED, 6, 4)
    a, b = fp.plot(C.atc, 0.4, XM, ORANGE)
    fp.lab(b, C.atc(b), "AC", ORANGE, 6, 5)
    qt, yt = C.min_atc()
    fp.guide2(Q_SR_LOSS, Pe, "q", "P")
    fp.guide2(qt, yt, "q" + sq("", 1), "P" + sq("", 1) + " = C" + sq("", 1), xrow=1, ydy=6)
    fp.hline(C_SR_LOSS, 0, Q_SR_LOSS)
    fp.T(fp.X0 - 8, fp.py(C_SR_LOSS) + 4 - 9, "C", 11.5, "end")
    fp.dpt(Q_SR_LOSS, Pe, C.mc, Pl)
    fp.dpt(Q_SR_LOSS, C_SR_LOSS, C.atc)
    fp.dpt(qt, yt, C.mc, C.atc, P1l)
    fp.vshift(fp.pline(Pl), fp.pline(P1l), fp.px(8.8))
    rect_label(fp, 2.2, 5.8, Pe, C_SR_LOSS, ["Losses"], size=11)
    emit(cv, "fig-11-6",
         "Figure 11.6: The movement from short-run losses to long-run normal profit",
         "Losses cause exit: industry supply shifts left from S to S1, price rises from P to P1, and each remaining firm's demand line rises until it touches the minimum of AC at output q1, where price equals average cost.",
         "In the short run the firm makes the shaded loss at price P and output q. Losses drive firms out, so industry supply shifts left from S to S<sub>1</sub>, raising the price to P<sub>1</sub> and cutting industry output to Q<sub>1</sub>. The firm&rsquo;s demand line rises to D<sub>1</sub> = AR<sub>1</sub> = MR<sub>1</sub>, which touches the bottom of AC where MC = MR at q<sub>1</sub>; P<sub>1</sub> = C<sub>1</sub> and the loss disappears.")


# ================================================================= 11.7
def fig_11_7():
    cv, ind, fp = two_panels("11-7")
    Q1 = 7.1
    d = 8.0
    S1, D = sd(PMIN, Q1, d)
    draw_sd(ind, S1, D)
    eq_industry(ind, S1, D)
    qt, yt = C.min_atc()
    price = lambda q: PMIN
    firm_d(fp, PMIN, "D = AR = MR")
    a, b = fp.plot(C.mc, 0, 20, RED)
    fp.lab(b, C.mc(b), "MC", RED, 6, 4)
    a, b = fp.plot(C.atc, 0.4, XM, ORANGE)
    fp.lab(b, C.atc(b), "AC", ORANGE, 6, 5)
    fp.guide2(qt, yt, "q", "P = C")
    fp.dpt(qt, yt, C.mc, C.atc, price)
    emit(cv, "fig-11-7",
         "Figure 11.7: Long-run equilibrium in perfect competition",
         "The firm's horizontal D = AR = MR line is tangent to the minimum point of AC, where MC = MR at output q, so price equals average cost and only normal profit is earned.",
         "In long-run equilibrium the price P set by the industry equals the minimum of the firm&rsquo;s AC curve. The firm produces at q where MC = MR, and there AC = P, so it earns exactly normal profit. There is no incentive for firms to enter or leave until demand or costs change.")


# ================================================================= 11.8
def fig_11_8():
    cv = Cv("11-8")
    p = firm_panel(cv, yl="Cost ($)")
    qt, yt = C.min_atc()
    a, b = p.plot(C.mc, 0, 20, RED)
    p.lab(b, C.mc(b), "MC", RED, 6, 4)
    a, b = p.plot(C.atc, 0.4, XM, ORANGE)
    p.lab(b, C.atc(b), "AC", ORANGE, 6, 5)
    p.guide2(qt, yt, "q", "c")
    p.dpt(qt, yt, C.mc, C.atc)
    emit(cv, "fig-11-8",
         "Figure 11.8: Productive efficiency",
         "U-shaped MC and AC curves; MC cuts AC at its minimum point, at output q and unit cost c, which is the productively efficient output.",
         "MC cuts AC exactly at the lowest point of AC. At that output q the cost per unit is at its minimum, c, so q is the productively efficient level of output (MC = AC).")


# ================================================================= 11.9
def fig_11_9():
    cv = Cv("11-9", 780, 400)
    cv.T(390, 20, "Allocative efficiency occurs where MC = AR", 13, "middle", INK, "600")
    cv.T(390, 38, "(the cost to producers = the value to consumers)", 11.5, "middle", INKSOFT)
    L = P(cv, 72, 330, 352, 74).scale(XM, YM)
    L.axes2("Output", "Price ($)", ylx=20, xly=390)
    R = P(cv, 452, 330, 752, 74).scale(XM, YM)
    R.axes2("Output", "Price ($)", ylx=402, xly=390)
    cv.T(212, 62, "Downward-sloping demand", 12, "middle", INK, "600")
    cv.T(602, 62, "Perfectly elastic demand", 12, "middle", INK, "600")
    AR, MR = dem(100.0, 6.0)
    a, b = L.plot(AR, 0, XM, GREY, linear=True)
    L.lab(b, AR(b), "D = AR", GREY, 6, 4)
    L.plot(MR, 0, 100 / 12, BLUE, linear=True)
    L.lab(100 / 12, 0, "MR", BLUE, 6, -6)
    a, b = L.plot(C.mc, 2.0, 20, RED)
    L.lab(b, C.mc(b), "MC", RED, 6, 4)
    q1, y1 = cross1(AR, C.mc, 2.0, 10)
    L.guide2(q1, y1, "q" + sq("", 1), None, to_y=False)
    L.dpt(q1, y1, AR, C.mc)
    price = lambda q: 45.0
    R.plot(price, 0, XM, GREY, linear=True)
    R.lab(XM, 45, "D = AR = MR", GREY, 0, -8, "end")
    a, b = R.plot(C.mc, 2.0, 20, RED)
    R.lab(b, C.mc(b), "MC", RED, 6, 4)
    q2, y2 = cross1(C.mc, price, 4.5, 12)
    R.guide2(q2, y2, "q" + sq("", 2), None, to_y=False)
    R.dpt(q2, y2, C.mc, price)
    emit(cv, "fig-11-9",
         "Figure 11.9: Allocative efficiency",
         "Two firm diagrams: with a downward-sloping demand curve MC cuts AR at output q1, and with perfectly elastic demand MC cuts the horizontal D = AR = MR line at q2; in both cases allocative efficiency is where MC = AR.",
         "Left: a firm with a downward-sloping D = AR (and steeper MR). The allocatively efficient output q<sub>1</sub> is where MC cuts AR. Right: a firm with perfectly elastic demand, where allocative efficiency is at q<sub>2</sub>, where MC cuts the horizontal D = AR = MR line. At these outputs the cost to producers (MC) equals the value to consumers (AR).")


# ================================================================= 11.10 - 11.12
def _firm_eff(fp, rect=None, price=None):
    a, b = fp.plot(C.mc, 0, 20, RED)
    fp.lab(b, C.mc(b), "MC", RED, 6, 4)
    a, b = fp.plot(C.atc, 0.4, XM, ORANGE)
    fp.lab(b, C.atc(b), "AC", ORANGE, 6, 5)


def fig_11_10():
    cv, ind, fp = two_panels("11-10")
    Q, Pe, d = 4.5, P_SR, 8.0
    S, D = sd(Pe, Q, d)
    draw_sd(ind, S, D)
    eq_industry(ind, S, D)
    q, cst = Q_SR_PROFIT, C_SR_PROFIT
    price = lambda x: Pe
    fp.rect(0, q, cst, Pe, PROFIT)
    firm_d(fp, Pe, "D = AR = MR")
    _firm_eff(fp)
    fp.guide2(q, Pe, "q = q" + sq("", 1), "P", xrow=0)
    fp.hline(cst, 0, q)
    fp.T(fp.X0 - 8, fp.py(cst) + 4 + 3, "C", 11.5, "end")
    fp.dpt(q, Pe, C.mc, price)
    fp.dpt(q, cst, C.atc)
    qt, yt = C.min_atc()
    fp.guide2(qt, yt, "q" + sq("", 2), None, to_y=False, xrow=1)
    fp.dpt(qt, yt, C.mc, C.atc)
    rect_label(fp, 1.0, 3.3, cst, Pe, ["Abnormal", "profit"])
    emit(cv, "fig-11-10",
         "Figure 11.10: Productive and allocative efficiency with short-run profit in perfect competition",
         "With short-run abnormal profit the firm produces at q, which equals the allocatively efficient output q1 (MC = AR) but is greater than the productively efficient output q2 at the minimum of AC.",
         "The profit-maximising output q (where MC = MR) equals q<sub>1</sub>, the allocatively efficient output, because AR = MR = P here. But q is not q<sub>2</sub>, the productively efficient output at the minimum of AC (MC = AC), so the firm earns abnormal profit (shaded) while being allocatively but not productively efficient.")


def fig_11_11():
    cv, ind, fp = two_panels("11-11")
    Q, Pe, d = 5.0, P_LOSS, 6.9
    S, D = sd(Pe, Q, d)
    draw_sd(ind, S, D)
    eq_industry(ind, S, D)
    q, cst = Q_SR_LOSS, C_SR_LOSS
    price = lambda x: Pe
    fp.rect(0, q, Pe, cst, LOSS)
    firm_d(fp, Pe, "D = AR = MR")
    _firm_eff(fp)
    fp.guide2(q, cst, "q = q" + sq("", 1), "C", xrow=0)
    fp.hline(Pe, 0, q)
    fp.T(fp.X0 - 8, fp.py(Pe) + 4, "P", 11.5, "end")
    fp.dpt(q, Pe, C.mc, price)
    fp.dpt(q, cst, C.atc)
    qt, yt = C.min_atc()
    fp.guide2(qt, yt, "q" + sq("", 2), None, to_y=False, xrow=1)
    fp.dpt(qt, yt, C.mc, C.atc)
    rect_label(fp, 2.2, 5.8, Pe, cst, ["Losses"], size=11)
    emit(cv, "fig-11-11",
         "Figure 11.11: Productive and allocative efficiency with short-run losses in perfect competition",
         "With short-run losses the firm produces at q, which equals the allocatively efficient output q1 (MC = AR) but is below the productively efficient output q2 at the minimum of AC.",
         "The loss-minimising output q (where MC = MR) equals q<sub>1</sub>, the allocatively efficient output (MC = AR = P), but is smaller than q<sub>2</sub>, the productively efficient output at the minimum of AC. The shaded rectangle is the short-run loss.")


def fig_11_12():
    cv, ind, fp = two_panels("11-12")
    Q1 = 7.1
    S1, D = sd(PMIN, Q1, 8.0)
    draw_sd(ind, S1, D)
    eq_industry(ind, S1, D)
    qt, yt = C.min_atc()
    price = lambda q: PMIN
    firm_d(fp, PMIN, "D = AR = MR")
    _firm_eff(fp)
    fp.guide2(qt, yt, "q = q" + sq("", 1) + " = q" + sq("", 2), "P = C")
    fp.dpt(qt, yt, C.mc, C.atc, price)
    emit(cv, "fig-11-12",
         "Figure 11.12: Productive and allocative efficiency in the long run in perfect competition",
         "In long-run equilibrium the profit-maximising output q, the productively efficient output q1 (MC = AC) and the allocatively efficient output q2 (MC = AR) are all the same output.",
         "The price line is tangent to the minimum of AC, so a single output satisfies all three conditions: q (MC = MR), q<sub>1</sub> (MC = AC, productive efficiency) and q<sub>2</sub> (MC = AR, allocative efficiency). The firm earns normal profit only.")


# ================================================================= 11.13
def fig_11_13():
    cv = Cv("11-13")
    p = P(cv).scale(13, YM)
    p.axes2("Quantity", "Price ($)")
    D = lambda q: 100 - 8 * q
    MRf = lambda q: 100 - 16 * q
    S = lambda q: 6 * q
    qs, ps = cross1(S, D, 0, 13)                # Q*, P*
    q1, m1 = cross1(S, MRf, 0, 13)              # Q1, MR = MC
    p1 = D(q1)
    s1 = S(q1)
    xs, x1 = p.px(qs), p.px(q1)
    # shaded welfare-loss triangles (upper: consumer surplus, lower: producer surplus)
    p.path(f"M{x1:.2f},{p.py(p1):.2f} L{x1:.2f},{p.py(ps):.2f} L{xs:.2f},{p.py(ps):.2f} Z", "none", 0, fill=DWL_DARK)
    p.path(f"M{x1:.2f},{p.py(ps):.2f} L{xs:.2f},{p.py(ps):.2f} L{x1:.2f},{p.py(s1):.2f} Z", "none", 0, fill=DWL_PALE)
    a, b = p.plot(D, 0, 13, GREY, linear=True)
    p.lab(b, 0, "D = MSB", GREY, 6, -6)
    a, b = p.plot(S, 0, 13, RED, linear=True)
    p.lab(b, S(b), "S = MSC", RED, 5, 4)
    p.plot(MRf, 0, 100 / 16, BLUE, linear=True)
    p.lab(6.0, 6, "MR", BLUE, -8, 4, "end")
    p.guide2(qs, ps, "Q*", "P*")
    p.guide2(q1, p1, "Q" + sq("", 1), "P" + sq("", 1))
    p.dpt(qs, ps, S, D)
    p.dpt(q1, m1, S, MRf)
    p.dpt(q1, p1, D)
    p.dpt(q1, s1, S)
    emit(cv, "fig-11-13",
         "Figure 11.13: Imperfect competition (market failure diagram)",
         "S = MSC and D = MSB cross at the socially efficient output Q*; MR cuts MC at the smaller output Q1, where price P1 is above P*; two shaded triangles between Q1 and Q* show the lost consumer and producer surplus.",
         "The socially efficient output Q* is where D = MSB meets S = MSC, at price P*. A profit-maximising imperfect competitor produces where MR = MC, at the smaller output Q<sub>1</sub>, and charges P<sub>1</sub> read from the demand curve. The darker triangle is lost consumer surplus and the paler one lost producer surplus; together they are the welfare loss, because units between Q<sub>1</sub> and Q* have marginal benefit above marginal cost but are not produced.")


# ================================================================= 11.14 - 11.17 (monopolistic competition)
A_MC, B_MC = 90.0, 5.0
A_LOSS, B_LOSS = 64.0, 6.0


def _mono_curves(p, AR, MR, atc=True, ar_label="D = AR", mc_lo=0.0, mr_y=None):
    a, b = p.plot(AR, 0, XM, GREY, linear=True)
    if AR(b) < 10:
        p.lab(b, AR(b), ar_label, GREY, 4, -10)
    else:
        p.lab(b, AR(b), ar_label, GREY, 6, 4)
    a, b = p.plot(MR, 0, XM, BLUE, linear=True)
    if mr_y is None:
        p.lab(b, 0, "MR", BLUE, 6, -6)
    else:
        qy = bisect(lambda x: MR(x) - mr_y, 0.0, b)
        p.lab(qy, mr_y, "MR", BLUE, -7, 4, "end")
    a, b = p.plot(C.mc, mc_lo, 20, RED)
    p.lab(b, C.mc(b), "MC", RED, 6, 4)
    if atc:
        a, b = p.plot(C.atc, 0.4, XM, ORANGE)
        p.lab(b, C.atc(b), "AC", ORANGE, 6, 5)


def fig_11_14():
    cv = Cv("11-14")
    p = firm_panel(cv, yl="Price and cost ($)")
    AR, MR = dem(A_MC, B_MC)
    q, m = cross1(MR, C.mc, 4.5, 9)
    price = AR(q)
    _mono_curves(p, AR, MR, atc=False)
    p.guide2(q, price, "q", "P")
    p.dpt(q, m, MR, C.mc)
    p.dpt(q, price, AR)
    emit(cv, "fig-11-14",
         "Figure 11.14: The demand curve for a firm in monopolistic competition",
         "A fairly flat downward-sloping D = AR with a steeper MR below it and a U-shaped MC; MC cuts MR at output q and price P is read up to AR.",
         "Because there are many close substitutes, the firm&rsquo;s D = AR curve is downward sloping but relatively elastic (fairly flat). MR lies below it and falls twice as steeply. The firm produces at q where MC = MR and charges P, read from the AR curve.")


def fig_11_15():
    cv = Cv("11-15")
    p = firm_panel(cv, yl="Price and cost ($)")
    AR, MR = dem(A_MC, B_MC)
    q, m = cross1(MR, C.mc, 4.5, 9)
    price, cst = AR(q), C.atc(q)
    assert price > cst
    p.rect(0, q, cst, price, PROFIT)
    _mono_curves(p, AR, MR)
    p.guide2(q, price, "q", "P")
    p.hline(cst, 0, q)
    p.T(p.X0 - 8, p.py(cst) + 4, "C", 11.5, "end")
    p.dpt(q, m, MR, C.mc)
    p.dpt(q, price, AR)
    p.dpt(q, cst, C.atc)
    rect_label(p, 1.0, 3.2, cst, price, ["Abnormal", "profit"])
    emit(cv, "fig-11-15",
         "Figure 11.15: Short-run abnormal profits in monopolistic competition",
         "D = AR, MR, MC and AC: at the output q where MC = MR the price P is above average cost C, and the shaded rectangle between P and C is abnormal profit.",
         "The firm maximises profit at q where MC = MR and charges price P from the AR curve. At q the average cost is C, below P, so it earns an abnormal profit of (P &minus; C) &times; q, shown by the shaded rectangle.")


def fig_11_16():
    cv = Cv("11-16")
    p = firm_panel(cv, yl="Price and cost ($)")
    AR, MR = dem(A_LOSS, B_LOSS)
    for x in [0.2 * i for i in range(1, 53)]:
        assert AR(x) < C.atc(x), "AR must lie below AC"
    q, m = cross1(MR, C.mc, 0.5, 9)
    price, cst = AR(q), C.atc(q)
    assert cst > price and price > C.avc(q)
    p.rect(0, q, price, cst, LOSS)
    _mono_curves(p, AR, MR, mc_lo=0.0, mr_y=26)
    p.guide2(q, cst, "q", "C")
    p.hline(price, 0, q)
    p.T(p.X0 - 8, p.py(price) + 4, "P", 11.5, "end")
    p.dpt(q, m, MR, C.mc)
    p.dpt(q, price, AR)
    p.dpt(q, cst, C.atc)
    legend_swatch(cv, p.px(7.2), p.py(28), LOSS, "Loss at q", stroke=RED)
    emit(cv, "fig-11-16",
         "Figure 11.16: Short-run losses in monopolistic competition",
         "D = AR, MR, MC and AC with AC above the price: at the output q where MC = MR the average cost C exceeds P, and the shaded rectangle between C and P is a loss.",
         "The firm produces at q where MC = MR and charges P from the AR curve, but here the whole AR curve lies below AC. At q the average cost C is above P, so it makes a loss of (C &minus; P) &times; q, shown by the shaded rectangle.")


def fig_11_17():
    cv = Cv("11-17")
    p = firm_panel(cv, yl="Price and cost ($)")
    AR, MR, Pt, s = tangent_demand(C, 5.0)
    q = 5.0
    m = MR(q)
    _mono_curves(p, AR, MR, mr_y=30)
    p.guide2(q, Pt, "q", "P = C")
    p.dpt(q, m, MR, C.mc)
    p.dpt(q, Pt, AR, C.atc)
    emit(cv, "fig-11-17",
         "Figure 11.17: Long-run equilibrium in monopolistic competition",
         "The downward-sloping D = AR curve is tangent to AC at output q, where MR = MC, so price P equals cost per unit C and only normal profit is earned.",
         "In the long run entry and exit shift each firm&rsquo;s demand until the AR curve is just tangent to AC. The firm produces at q where MC = MR, and at q the price P equals the average cost C, so there is no abnormal profit rectangle and no incentive to enter or leave. The tangency lies to the left of the minimum of AC.")


# ================================================================= 11.18
def _eff_panel(p, AR, MR, rect_kind, mr_y=None):
    q, m = cross1(MR, C.mc, 0.5, 9)
    price, cst = AR(q), C.atc(q)
    q1, y1 = C.min_atc()
    q2, y2 = cross1(AR, C.mc, 2.0, 10)
    if rect_kind == "profit":
        p.rect(0, q, cst, price, PROFIT)
    else:
        p.rect(0, q, price, cst, LOSS)
    _mono_curves(p, AR, MR, mr_y=mr_y)
    p.guide2(q, cst if rect_kind == "loss" else price, "q", "P" if rect_kind == "profit" else "C")
    p.guide2(q1, y1, "q" + sq("", 1), None, to_y=False)
    p.guide2(q2, y2, "q" + sq("", 2), None, to_y=False, xrow=1)
    p.dpt(q, m, MR, C.mc)
    p.dpt(q, price, AR)
    p.dpt(q, cst, C.atc)
    p.dpt(q1, y1, C.mc, C.atc)
    p.dpt(q2, y2, AR, C.mc)
    if rect_kind == "profit":
        p.hline(cst, 0, q)
        p.T(p.X0 - 8, p.py(cst) + 4, "C", 11.5, "end")
    else:
        p.hline(price, 0, q)
        p.T(p.X0 - 8, p.py(price) + 4, "P", 11.5, "end")
    return q, q1, q2, price, cst


def fig_11_18():
    cv = Cv("11-18", 800, 380)
    L = P(cv, 72, 318, 352, 46).scale(XM, YM)
    L.axes2("Output", "Price and cost ($)", ylx=20, title="Short-run abnormal profit", xly=374)
    R = P(cv, 452, 318, 752, 46).scale(XM, YM)
    R.axes2("Output", "Price and cost ($)", ylx=402, title="Short-run loss", xly=374)
    AR, MR = dem(A_MC, B_MC)
    q, q1, q2, price, cst = _eff_panel(L, AR, MR, "profit")
    rect_label(L, 0.95, 3.2, cst, price, ["Abnormal", "profit"])
    ARl, MRl = dem(A_LOSS, B_LOSS)
    qL, q1L, q2L, priceL, cstL = _eff_panel(R, ARl, MRl, "loss", mr_y=26)
    legend_swatch(cv, R.px(6.9), R.py(30), LOSS, "Loss at q", stroke=RED)
    emit(cv, "fig-11-18",
         "Figure 11.18: Productive and allocative efficiency in the short run in monopolistic competition",
         "Two panels, abnormal profit and loss: in each the profit-maximising output q (MC = MR) differs from the productively efficient output q1 (MC = AC) and the allocatively efficient output q2 (MC = AR).",
         "In both panels the firm produces at q where MC = MR. Neither output equals q<sub>1</sub>, the productively efficient output at the minimum of AC (MC = AC), nor q<sub>2</sub>, the allocatively efficient output where MC = AR. Left: q is followed by q<sub>1</sub> then q<sub>2</sub> and the shaded rectangle is abnormal profit. Right: the firm makes the shaded loss, and q<sub>2</sub> lies to the left of q<sub>1</sub>.")


# ================================================================= 11.19 / 11.20
def fig_11_19():
    cv = Cv("11-19")
    p = firm_panel(cv, yl="Price and cost ($)", xly=374)
    AR, MR, Pt, s = tangent_demand(C, 5.0)
    q = 5.0
    q1, y1 = C.min_atc()
    q2, y2 = cross1(AR, C.mc, 5.0, 10)
    assert q < q2 < q1
    _mono_curves(p, AR, MR, mr_y=30)
    p.guide2(q, Pt, "q", "P")
    p.guide2(q2, y2, "q" + sq("", 2), None, to_y=False)
    p.guide2(q1, y1, "q" + sq("", 1), None, to_y=False, xrow=1)
    p.dpt(q, MR(q), MR, C.mc)
    p.dpt(q, Pt, AR, C.atc)
    p.dpt(q1, y1, C.mc, C.atc)
    p.dpt(q2, y2, AR, C.mc)
    emit(cv, "fig-11-19",
         "Figure 11.19: Productive and allocative efficiency in the long run in monopolistic competition",
         "With AR tangent to AC to the left of its minimum, the profit-maximising output q is below the allocatively efficient output q2 (MC = AR), which is below the productively efficient output q1 (MC = AC).",
         "In long-run equilibrium AR is tangent to AC on its falling part, so the firm produces at q (MC = MR), left of the minimum of AC. The allocatively efficient output q<sub>2</sub> (where MC cuts AR) is larger than q, and the productively efficient output q<sub>1</sub> (the minimum of AC, where MC = AC) is larger still, so neither efficiency condition is met.")


def fig_11_20():
    cv = Cv("11-20")
    p = firm_panel(cv, yl="Price and cost ($)")
    AR, MR, Pt, s = tangent_demand(C, 5.0)
    q = 5.0
    q1, y1 = cross1(AR, C.mc, 5.0, 10)
    p.shade(AR, C.mc, q, q1, DWL_DARK)
    _mono_curves(p, AR, MR, mr_y=30)
    p.guide2(q, Pt, "q", "P")
    p.guide2(q1, y1, "q" + sq("", 1), None, to_y=False)
    p.dpt(q, MR(q), MR, C.mc)
    p.dpt(q, Pt, AR, C.atc)
    p.dpt(q1, y1, AR, C.mc)
    emit(cv, "fig-11-20",
         "Figure 11.20: Market failure in monopolistic competition",
         "In long-run equilibrium the output q (MC = MR) is below the allocatively efficient output q1 (MC = AR); the shaded wedge between AR and MC from q to q1 is the welfare loss.",
         "The firm produces at q where MC = MR, less than the allocatively efficient output q<sub>1</sub> where MC = AR. Between q and q<sub>1</sub> the value to consumers (AR) exceeds the marginal cost (MC), so the shaded wedge bounded by AR and MC shows the welfare loss, a market failure.")


ALL = [fig_11_1, fig_11_2, fig_11_3, fig_11_4, fig_11_5, fig_11_6, fig_11_7, fig_11_8,
       fig_11_9, fig_11_10, fig_11_11, fig_11_12, fig_11_13, fig_11_14, fig_11_15,
       fig_11_16, fig_11_17, fig_11_18, fig_11_19, fig_11_20]

if __name__ == "__main__":
    for f in ALL:
        f()
