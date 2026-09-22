from figs_ch10_12 import *
from build_ch11 import _mono_curves, legend_swatch, rect_label, A_LOSS, B_LOSS

C = C0
QMIN, PMIN = C.min_atc()


def mono_scene(A, B):
    AR, MR = dem(A, B)
    q, m = cross1(MR, C.mc, 4.5, 9)
    return AR, MR, q, m, AR(q), C.atc(q)


# ================================================================= 12.1
def fig_12_1():
    cv = Cv("12-1")
    p = firm_panel(cv, yl="Price ($)", xl="Quantity demanded (units)")
    LR = lambda q: 10 + 220 / q + 1.6 * q
    MCf = lambda q: 10 + 0.6 * q
    A1, B1 = 106.0, 6.0
    AR1 = lambda q: A1 - B1 * q
    AR2 = lambda q: A1 - 2 * B1 * q        # each of two firms sells half the quantity at every price
    cs = crosses(AR1, LR, 0.5, 12)
    assert len(cs) == 2
    (qa, ya), (qb, yb) = cs
    for q in [0.3 + 0.05 * i for i in range(0, 200)]:
        assert AR2(q) < LR(q) - 6, "AR2 must sit below LRAC everywhere"
        assert MCf(q) < LR(q)
    p.shade(AR1, LR, qa, qb, PROFIT)
    a, b = p.plot(AR1, 0, XM, GREY, linear=True)
    p.lab(b, AR1(b), "D" + sq("", 1) + " = AR" + sq("", 1), GREY, 6, 14)
    a, b = p.plot(AR2, 0, XM, GREY, linear=True, dash="6 5")
    p.lab(6.3, 30, "D" + sq("", 2) + " = AR" + sq("", 2), GREY, -6, 4, "end")
    a, b = p.plot(LR, 0.5, XM, ORANGE)
    p.lab(b, LR(b), "LRAC", ORANGE, 6, -6)
    a, b = p.plot(MCf, 0, XM, RED, linear=True)
    p.lab(b, MCf(b), "MC", RED, 6, 4)
    p.guide2(qa, ya, "q" + sq("", 1), None, to_y=False)
    p.guide2(qb, yb, "q" + sq("", 2), None, to_y=False)
    p.dpt(qa, ya, AR1, LR)
    p.dpt(qb, yb, AR1, LR)
    p.T(p.px(qa) + 7, p.py(ya) - 8, "a", 12, "start")
    p.T(p.px(qb) + 5, p.py(yb) - 10, "b", 12, "start")
    p.hshift(p.pline(AR1), p.pline(AR2), p.py(94))
    legend_swatch(cv, p.px(5.4), p.py(98), PROFIT, "AR above LRAC only if")
    cv.T(p.px(5.4) + 18, p.py(98) + 12, "one firm serves the whole market", 10.8, "start", INKSOFT)
    emit(cv, "fig-12-1",
         "Figure 12.1: A natural monopoly",
         "LRAC falls over a wide range of output. Market demand D1 = AR1 lies above LRAC only between q1 and q2; if a second firm halves each firm's demand to D2 = AR2, AR is below LRAC at every output.",
         "LRAC falls steeply over a wide range of output (economies of scale), with MC low and fairly flat. Market demand D<sub>1</sub> = AR<sub>1</sub> cuts LRAC at a and b, so one firm can earn abnormal profit (shaded) at any output between q<sub>1</sub> and q<sub>2</sub>. If two firms split the market, each faces D<sub>2</sub> = AR<sub>2</sub> (half the quantity at each price), which lies below LRAC at every output, so neither could even cover its costs: the market supports only one firm, a natural monopoly.")


# ================================================================= 12.2
def fig_12_2():
    cv = Cv("12-2")
    p = firm_panel(cv, yl="Price and cost ($)")
    AR, MR = dem(100.0, 6.0)
    MCl = lambda q: 6 + 6 * q
    q, m = cross1(MR, MCl, 0, 10)
    price = AR(q)
    a, b = p.plot(AR, 0, XM, GREY, linear=True)
    p.lab(b, AR(b), "D = AR", GREY, 6, 4)
    a, b = p.plot(MR, 0, XM, BLUE, linear=True)
    p.lab(b, 0, "MR", BLUE, 6, -6)
    a, b = p.plot(MCl, 0, XM, RED, linear=True)
    p.lab(b, MCl(b), "MC", RED, 6, 4)
    p.guide2(q, price, "q", "P")
    p.dpt(q, m, MR, MCl)
    p.dpt(q, price, AR)
    emit(cv, "fig-12-2",
         "Figure 12.2: The demand curve facing a monopolist",
         "A downward-sloping D = AR with a steeper MR and an upward-sloping MC; the monopolist produces q where MC = MR and charges price P read from the demand curve.",
         "The monopolist supplies the whole market, so it faces the downward-sloping market demand curve D = AR, with MR below it falling twice as steeply. It maximises profit at q, where MC = MR, and by restricting output to q it can charge the higher price P read from AR. This ability to choose price by restricting quantity is market power.")


# ================================================================= 12.3
def _profit_scene(cv, A, B, rect_lines=("Abnormal", "profit")):
    p = firm_panel(cv, yl="Price and cost ($)")
    AR, MR, q, m, price, cst = mono_scene(A, B)
    assert price > cst
    p.rect(0, q, cst, price, PROFIT)
    _mono_curves(p, AR, MR)
    p.hline(cst, 0, q)
    p.dpt(q, m, MR, C.mc)
    p.dpt(q, price, AR)
    p.dpt(q, cst, C.atc)
    return p, AR, MR, q, m, price, cst


def fig_12_3():
    cv = Cv("12-3")
    p, AR, MR, q, m, price, cst = _profit_scene(cv, 100.0, 6.0)
    p.guide2(q, price, "q", "P")
    p.T(p.X0 - 8, p.py(cst) + 4, "C", 11.5, "end")
    p.T(p.px(q) + 6, p.py(price) - 7, "a", 11.5, "start")
    p.T(p.px(q) + 7, p.py(cst) + 15, "b", 11.5, "start")
    rect_label(p, 1.05, 3.0, cst, price, ["Abnormal", "profit"])
    emit(cv, "fig-12-3",
         "Figure 12.3: Abnormal profits in the long run in monopoly",
         "U-shaped AC and MC, D = AR and MR: the monopolist produces q where MC = MR, price P at point a is above average cost C at point b, and the shaded rectangle PabC is abnormal profit.",
         "The monopolist maximises profit at q, where MC = MR. Price P (point a) is read from AR and average cost C (point b) from AC. Because P &gt; C the shaded rectangle PabC, of height (P &minus; C) and width q, is abnormal profit. Barriers to entry stop new firms competing it away, so it persists in the long run.")


# ================================================================= 12.4
def fig_12_4():
    cv = Cv("12-4")
    p = firm_panel(cv, yl="Price and cost ($)")
    AR, MR, q, m, price, cst = mono_scene(A_LOSS, B_LOSS)
    for x in [0.2 * i for i in range(1, 53)]:
        assert AR(x) < C.atc(x)
    assert cst > price
    p.rect(0, q, price, cst, LOSS)
    _mono_curves(p, AR, MR, mr_y=26)
    p.guide2(q, cst, "q", "C")
    p.hline(price, 0, q)
    p.T(p.X0 - 8, p.py(price) + 4, "P", 11.5, "end")
    p.T(p.px(q) + 7, p.py(cst) - 8, "b", 11.5, "start")
    p.T(p.px(q) + 7, p.py(price) + 15, "a", 11.5, "start")
    p.dpt(q, m, MR, C.mc)
    p.dpt(q, price, AR)
    p.dpt(q, cst, C.atc)
    legend_swatch(cv, p.px(7.2), p.py(28), LOSS, "Losses", stroke=RED)
    emit(cv, "fig-12-4",
         "Figure 12.4: A monopolist making losses in the long run",
         "AC lies above D = AR at every output; at the loss-minimising output q (MC = MR) average cost C exceeds price P and the shaded rectangle is a loss.",
         "The monopolist would produce at q where MC = MR, but the AC curve lies above AR at every output. At q the average cost C (point b) is higher than the price P (point a), so it makes the shaded loss of (C &minus; P) &times; q. No output covers average cost, so in the long run the firm will not produce at all and there will be no industry.")


# ================================================================= 12.5 / 12.11
def _eff_mono(cv, A, B, names, name_prof, name_prod, name_alloc, rect_lines=("Abnormal", "profit")):
    p = firm_panel(cv, yl="Price and cost ($)")
    AR, MR, q, m, price, cst = mono_scene(A, B)
    qp, yp = C.min_atc()
    qa, ya = cross1(AR, C.mc, 4.5, 12)
    assert q + 0.5 < qp < qa - 0.5, (q, qp, qa)
    p.rect(0, q, cst, price, PROFIT)
    _mono_curves(p, AR, MR)
    p.guide2(q, price, name_prof, "P")
    p.hline(cst, 0, q)
    p.T(p.X0 - 8, p.py(cst) + 4, "C", 11.5, "end")
    p.guide2(qp, yp, name_prod, None, to_y=False)
    p.guide2(qa, ya, name_alloc, None, to_y=False)
    p.dpt(q, m, MR, C.mc)
    p.dpt(q, price, AR)
    p.dpt(q, cst, C.atc)
    p.dpt(qp, yp, C.mc, C.atc)
    p.dpt(qa, ya, AR, C.mc)
    rect_label(p, 1.05, 3.0, cst, price, list(rect_lines))
    return p


def fig_12_5():
    cv = Cv("12-5")
    _eff_mono(cv, 100.0, 6.0, None, "q" + sq("", 1), "q" + sq("", "p"), "q" + sq("", 2))
    emit(cv, "fig-12-5",
         "Figure 12.5: Productive and allocative efficiency in monopoly",
         "The profit-maximising output q1 (MC = MR) is below the productively efficient output qp at the minimum of AC and below the allocatively efficient output q2 where MC = AR; the shaded rectangle is abnormal profit.",
         "The monopolist produces q<sub>1</sub>, where MC = MR, and earns the shaded abnormal profit. This is less than q<sub>p</sub>, the productively efficient output at the minimum of AC (MC = AC), and less than q<sub>2</sub>, the allocatively efficient output where AR cuts MC (P = MC). Output is restricted to force up the price, so neither form of efficiency is achieved.")


def fig_12_11():
    cv = Cv("12-11")
    _eff_mono(cv, 104.0, 6.5, None, "q" + sq("", 1), "q" + sq("", "p"), "q" + sq("", "a"))
    emit(cv, "fig-12-11",
         "Figure 12.11: Productive and allocative efficiency in a collusive oligopoly",
         "Colluding oligopolists produce the monopoly output q1 (MC = MR) and earn the shaded abnormal profit; this is below both the productively efficient output qp (minimum AC) and the allocatively efficient output qa (AR = MC).",
         "If firms collude, formally or tacitly, behind barriers to entry they act like a monopolist: they produce q<sub>1</sub>, where MC = MR, and share the shaded abnormal profit according to market share. As in monopoly, output is below q<sub>p</sub> (the minimum of AC, productive efficiency) and below q<sub>a</sub> (where AR = MC, allocative efficiency), purely to force up the price.")


# ================================================================= 12.6
def fig_12_6():
    cv = Cv("12-6")
    YM6 = 125
    p = P(cv).scale(XM, YM6)
    p.axes2("Output (units)", "Price ($)")
    A, B = 120.0, 5.0
    AR, MR = dem(A, B)
    S = lambda q: 3.2 * C.mc(q)                 # perfect competition: industry supply
    Mm = lambda q: 0.65 * C.mc(q / 1.2)          # monopoly with economies of scale (lower, further right)
    q1, p1 = cross1(S, AR, 4.0, 12)
    q2, m2 = cross1(Mm, MR, 4.8, 12)
    p2 = AR(q2)
    assert q2 > q1 + 1.5 and p1 > p2 + 8
    a, b = p.plot(AR, 0, XM, GREY, linear=True)
    p.lab(b, AR(b), "D = AR", GREY, 6, 4)
    a, b = p.plot(MR, 0, XM, BLUE, linear=True)
    p.lab(b, MR(b), "MR", BLUE, 6, 4)
    a, b = p.plot(S, 0, 20, RED)
    p.lab(b, S(b), "Industry supply:", RED, 8, 8)
    p.lab(b, S(b), "perfect competition", RED, 8, 22)
    a, b = p.plot(Mm, 0, XM, MAGENTA)
    p.lab(b, Mm(b), "MC: monopoly", MAGENTA, 0, -22, "end")
    p.guide2(q1, p1, "Q" + sq("", 1), "P" + sq("", 1))
    p.guide2(q2, p2, "Q" + sq("", 2), "P" + sq("", 2))
    p.dpt(q1, p1, S, AR)
    p.dpt(q2, m2, Mm, MR)
    p.dpt(q2, p2, AR)
    emit(cv, "fig-12-6",
         "Figure 12.6: Economies of scale in monopoly",
         "A monopolist with strong economies of scale has a lower MC curve than the industry supply curve of a perfectly competitive industry; MC = MR gives a larger output Q2 at a lower price P2 than the competitive output Q1 and price P1.",
         "Under perfect competition industry supply (the sum of many small firms&rsquo; MC curves) meets D = AR at price P<sub>1</sub> and output Q<sub>1</sub>. A monopolist with large economies of scale has a lower, further-right MC curve. It produces where MC = MR, giving a larger output Q<sub>2</sub> and a lower price P<sub>2</sub> than perfect competition, so consumers can gain despite the market power.")


# ================================================================= 12.7
def fig_12_7():
    cv = Cv("12-7")
    p = firm_panel(cv, yl="Price ($)")
    AR, MR = dem(100.0, 6.0)
    q1, p1 = cross1(C.mc, AR, 4.5, 12)
    q2, m2 = cross1(MR, C.mc, 4.5, 9)
    p2 = AR(q2)
    assert q2 < q1 and p2 > p1
    a, b = p.plot(AR, 0, XM, GREY, linear=True)
    p.lab(b, AR(b), "D = AR", GREY, 6, 4)
    a, b = p.plot(MR, 0, XM, BLUE, linear=True)
    p.lab(b, 0, "MR", BLUE, 6, -6)
    a, b = p.plot(C.mc, 0, 20, RED)
    p.T(p.px(b) - 8, p.py(105) + 4, "MC (= supply", 12.5, "end", RED)
    p.T(p.px(b) - 8, p.py(105) + 18, "in perfect competition)", 12.5, "end", RED)
    p.guide2(q1, p1, "Q" + sq("", 1), "P" + sq("", 1), xrow=1)
    p.guide2(q2, p2, "Q" + sq("", 2), "P" + sq("", 2))
    p.dpt(q1, p1, C.mc, AR)
    p.dpt(q2, m2, MR, C.mc)
    p.dpt(q2, p2, AR)
    emit(cv, "fig-12-7",
         "Figure 12.7: Monopoly versus perfect competition without economies of scale",
         "With the same cost curve, perfect competition produces where MC (= supply) meets D = AR, at Q1 and P1; a monopolist produces where MC = MR, a smaller output Q2 at a higher price P2.",
         "Assuming no cost difference, one MC curve serves as the supply curve under perfect competition. Perfect competition gives price P<sub>1</sub> and output Q<sub>1</sub> where MC meets D = AR. The profit-maximising monopolist produces where MC = MR, restricting output to Q<sub>2</sub> (less than Q<sub>1</sub>) and charging the higher price P<sub>2</sub>.")


# ================================================================= 12.8
def fig_12_8():
    cv = Cv("12-8", 640, 270)
    x0, x1 = 50.0, 590.0
    X = lambda pct: x0 + (x1 - x0) * pct / 100.0
    cv.T(320, 26, "Market share of the four largest firms (CR<tspan font-size=\"70%\" dy=\"3\">4</tspan>)", 13.5, "middle", INK, "600")
    by, bh = 112, 26
    for a, b, fill in [(0, 50, "#d9f0e1"), (50, 80, "#fbe9c8"), (80, 100, "#f7d6d1")]:
        cv.fig.add(f'<rect x="{X(a):.1f}" y="{by}" width="{X(b)-X(a):.1f}" height="{bh}" fill="{fill}"/>')
    cv.fig.add(f'<rect x="{x0}" y="{by}" width="{x1-x0}" height="{bh}" fill="none" stroke="{INK}" stroke-width="2"/>')
    for pct in (50, 80):
        cv.fig.line(X(pct), by, X(pct), by + bh, INK, 1.6, cap="butt")
    # end markers
    for pct in (0, 100):
        cv.fig.add(f'<rect x="{X(pct)-7:.1f}" y="{by+bh/2-7:.1f}" width="14" height="14" rx="2" fill="{RED}"/>')
    # structure labels
    cv.T(X(0), 62, "Perfect", 12.5, "middle", INK, "600")
    cv.T(X(0), 77, "competition", 12.5, "middle", INK, "600")
    cv.T(X(100), 70, "Monopoly", 12.5, "middle", INK, "600")
    for a, b, name in [(8, 46, "Monopolistic competition"), (54, 92, "Oligopoly")]:
        cv.T((X(a) + X(b)) / 2, 66, name, 12.5, "middle", INK, "600")
        cv.fig.line(X(a), 86, X(b), 86, INK, 1.8, cap="butt")
        cv.fig.line(X(a), 86, X(a), 94, INK, 1.8, cap="butt")
        cv.fig.line(X(b), 86, X(b), 94, INK, 1.8, cap="butt")
    # scale labels
    for pct in (0, 50, 80, 100):
        cv.fig.line(X(pct), by + bh, X(pct), by + bh + 7, INK, 1.6, cap="butt")
        cv.T(X(pct), by + bh + 23, f"{pct}%", 12, "middle")
    # concentration bands
    ay = 200
    for a, b, name in [(0, 50, "Low concentration"), (50, 80, "Medium concentration"), (80, 100, "High concentration")]:
        xa, xb = X(a) + 3, X(b) - 3
        cv.fig.line(xa + 5, ay, xb - 5, ay, PURPLE, 2, cap="butt")
        cv.fig.arrowhead(xa, ay, 180, PURPLE, 8)
        cv.fig.arrowhead(xb, ay, 0, PURPLE, 8)
        cv.T((xa + xb) / 2, ay + 22, name, 12, "middle")
    emit(cv, "fig-12-8",
         "Figure 12.8: CR<sub>4</sub> ratios in different market structures",
         "A scale from 0% to 100% of CR4 (share of the four largest firms) with perfect competition at 0%, monopolistic competition below 50%, oligopoly from 50% upwards and monopoly at 100%, split into low (0-50%), medium (50-80%) and high (80-100%) concentration.",
         "A horizontal CR<sub>4</sub> scale from 0% to 100%. Perfect competition sits at the 0% end and monopoly at the 100% end. Monopolistic competition lies in the low range (below 50%), oligopoly covers roughly 50% to 90%+. Concentration is low from 0&ndash;50%, medium from 50&ndash;80% and high from 80&ndash;100%. The boundaries are a matter of interpretation and the structures form a continuum rather than four separate boxes.")


# ================================================================= 12.9
def fig_12_9():
    cv = Cv("12-9")
    p, AR, MR, q, m, price, cst = _profit_scene(cv, 104.0, 6.5)
    p.guide2(q, price, "q", "p")
    p.T(p.X0 - 8, p.py(cst) + 4, "a", 11.5, "end")
    rect_label(p, 1.05, 3.0, cst, price, ["Abnormal", "profit"])
    emit(cv, "fig-12-9",
         "Figure 12.9: Oligopolists acting as a monopolist",
         "Colluding oligopolists restrict output to q where MC = MR and charge price p from D = AR; the shaded rectangle between p and average cost a is abnormal profit shared among them.",
         "If oligopolists collude they behave as one monopolist. Together they restrict output to q, where MC = MR, and charge price p, read from the market AR curve. Average cost at q is a, so the shaded rectangle of height (p &minus; a) and width q is the abnormal (monopoly) profit, which is then divided among the firms by market share.")


ALL = [fig_12_1, fig_12_2, fig_12_3, fig_12_4, fig_12_5, fig_12_6, fig_12_7, fig_12_8,
       fig_12_9, fig_12_11]


# ================================================================= 12.10
def _oval(cv, cx, cy, rx, ry):
    cv.fig.add(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="#fdeaea" stroke="{RED}" stroke-width="2"/>')


def fig_12_10():
    cv = Cv("12-10", 740, 430)
    R_ = RED
    cx = 370
    cv.fig.add(f'<rect x="{cx-105}" y="14" width="210" height="44" rx="6" fill="#fdeaea" stroke="{R_}" stroke-width="2"/>')
    cv.T(cx, 32, "Decisions for", 12.5, "middle", INK, "600")
    cv.T(cx, 48, "Harbour Ferries", 12.5, "middle", INK, "600")
    gl, gr = 200, 540
    cols = [110, 290, 450, 630]
    # top connectors
    cv.fig.line(cx, 58, cx, 80, R_, 2, cap="butt")
    cv.fig.line(gl, 80, gr, 80, R_, 2, cap="butt")
    cv.fig.arrow(gl, 80, gl, 102, R_, 2, 7)
    cv.fig.arrow(gr, 80, gr, 102, R_, 2, 7)
    cv.T(gl, 118, "If the worst happens", 12.5, "middle")
    cv.T(gr, 118, "If the best happens", 12.5, "middle")
    for g, cs in [(gl, cols[:2]), (gr, cols[2:])]:
        cv.fig.line(g, 126, g, 140, R_, 2, cap="butt")
        cv.fig.line(cs[0], 140, cs[1], 140, R_, 2, cap="butt")
        for c in cs:
            cv.fig.arrow(c, 140, c, 162, R_, 2, 7)
    moves = ["maintains price", "lowers price", "maintains price", "lowers price"]
    rival = ["lowers price", "lowers price", "maintains price", "maintains price"]
    profit = ["$3M", "$5M", "$9M", "$12M"]
    for i, c in enumerate(cols):
        cv.T(c, 180, "Harbour Ferries", 12, "middle")
        cv.T(c, 195, moves[i], 12, "middle")
        cv.fig.arrow(c, 203, c, 232, R_, 2, 7)
        cv.T(c, 250, "BlueWave", 12, "middle")
        cv.T(c, 265, rival[i], 12, "middle")
        cv.fig.arrow(c, 273, c, 306, R_, 2, 7)
        if i in (1, 3):
            _oval(cv, c, 326, 50, 17)
        cv.T(c, 331, "Profit " + profit[i], 12.5, "middle")
    cv.T(cols[1], 366, "Best &ldquo;worst option&rdquo;".replace("&ldquo;", "'").replace("&rdquo;", "'"), 12, "middle")
    cv.T(cols[1], 382, "(minimax strategy)", 12, "middle")
    cv.T(cols[3], 366, "Best 'best option'", 12, "middle")
    cv.T(cols[3], 382, "(maximax strategy)", 12, "middle")
    cv.T(cx, 416, "In both cases Harbour Ferries does better by lowering its price.", 11.5, "middle", INKSOFT, italic=True)
    emit(cv, "fig-12-10",
         "Figure 12.10: Game theory outcomes for Harbour Ferries and BlueWave",
         "Decision tree for Harbour Ferries. If the worst happens (BlueWave lowers price) its profit is $3M if it maintains price and $5M if it lowers price; if the best happens (BlueWave maintains price) it earns $9M or $12M. Lowering price is best in both cases.",
         "Harbour Ferries chooses whether to maintain or lower its price, and its rival BlueWave may respond. If the worst happens (BlueWave lowers price), Harbour earns $3M by maintaining price and $5M by lowering it; the $5M outcome is the best &lsquo;worst option&rsquo; (minimax strategy). If the best happens (BlueWave maintains price), it earns $9M by maintaining and $12M by lowering; the $12M outcome is the best &lsquo;best option&rsquo; (maximax strategy). Under either rule lowering the price is the rational choice.")


ALL.append(fig_12_10)

if __name__ == "__main__":
    for f in ALL:
        f()
