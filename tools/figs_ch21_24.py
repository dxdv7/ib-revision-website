"""Original vector figures for chapters 21-24 (growth, inequality, comparative
advantage, protectionism). Own coordinates, own examples - nothing traced from
any scan. Built on tools/figlib.py (not modified).

Every intersection dot is computed with Fig.intersect()/equilibrium(); guides
and ticks come from the data scale; shift arrows span old curve to new curve
at equal height.
"""
import os, sys, json, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import *

OUT = "/Users/davidbukraba/Desktop/IB WEBSITE/assets/figures-original"
os.makedirs(OUT, exist_ok=True)

LIGHTRED = "#f8d3cd"
LIGHTTEAL = "#c9edf1"
LIGHTPURPLE = "#e2defa"
LIGHTGREY = "#e8e8e8"


def save(fid, fig, label, alt, caption):
    title = label.split(": ", 1)[-1]
    open(f"{OUT}/{fid}.svg", "w").write(fig.svg(title, alt))
    with open(f"{OUT}/{fid}.json", "w") as fh:
        json.dump({"label": label, "alt": alt, "caption": caption}, fh, indent=1)
    print("saved", fid)


# ----------------------------------------------------------------- helpers
def dline(q1, p1, q2, p2):
    return ((q1, p1), (q2, p2))


def hline(p, q1, q2):
    return ((q1, p), (q2, p))


def poly(f, pts, fill):
    d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts) + " Z"
    f.path(d, color="none", width=0, fill=fill)


def draw_line(f, l, color, width=2.8, dash=None):
    f.line(l[0][0], l[0][1], l[1][0], l[1][1], color, width, dash)


def combine(w, h, figs):
    out = Fig(w=w, h=h)
    for fg in figs:
        out.parts.extend(fg.parts)
    return out


def paxes(f, xlabel, ylabel, origin="0"):
    """Axes drawn against f's own local plot box - safe inside a multi-panel
    canvas (unlike Fig.axes(), which centres labels on the WHOLE canvas)."""
    f.line(f.X0, f.Y0, f.X1, f.Y0, INK, 2.2)
    f.line(f.X0, f.Y0, f.X0, f.Y1, INK, 2.2)
    f.arrowhead(f.X1 + 5, f.Y0, 0, INK, 9)
    f.arrowhead(f.X0, f.Y1 - 5, -90, INK, 9)
    if origin:
        f.text(f.X0 - 12, f.Y0 + 16, origin, 12, "end")
    f.text((f.X0 + f.X1) / 2, f.Y0 + 34, xlabel, 12.5, "middle")
    f.text(f.X0 - 32, (f.Y0 + f.Y1) / 2, ylabel, 12.5, "middle", rotate=-90)


def ppc_pts(x0, y_top, x1, y_bot, n=7):
    """Points along a bowed-out quarter-ellipse PPC from (x0,y_top) to
    (x1,y_bot), own formula (not traced)."""
    pts = []
    for i in range(n + 1):
        t = (math.pi / 2) * i / n
        x = x0 + (x1 - x0) * math.sin(t)
        y = y_top + (y_bot - y_top) * (1 - math.cos(t))
        pts.append((x, y))
    return pts


def scale_from(o, pts, k):
    return [(o[0] + k * (x - o[0]), o[1] + k * (y - o[1])) for x, y in pts]


# =============================================================== CHAPTER 21
def fig_21_2():
    W, H = 440, 760
    A = Fig(w=W, h=H, x0=90, y0=300, x1=380, y1=55)
    SR = ((135, 275), (345, 80))
    LRASX = 305
    A1 = ((120, 95), (300, 285))
    paxes(A, "Real output (Y)", "Average price level")
    draw_line(A, SR, RED)
    A.label(349, 76, "SRAS", RED, 12.5)
    A.line(LRASX, A.Y0, LRASX, A.Y1, INK, 2.4)
    A.label(LRASX + 6, A.Y1 + 12, "LRAS", INK, 12.5)
    draw_line(A, A1, GREY)
    A.label(304, 292, "AD" + sub("", 1), GREY, 12.5)
    e1 = A.intersect(SR, A1)
    assert e1[0] < LRASX - 20
    A.guide(e1[0], e1[1], "Y" + sub("", 1), None, to_y=False)
    A.dot(*e1, 3.6, INK)
    A.text(e1[0], A.Y0 + 18, "Y" + sub("", 1), 11.5, "middle")
    A.text(LRASX, A.Y0 + 18, "Y" + sub("", "f"), 11.5, "middle")
    ay = A.Y0 + 56
    A.arrow(e1[0] + 4, ay, LRASX - 4, ay, INK, 1.6, 6)
    A.arrow(LRASX - 4, ay, e1[0] + 4, ay, INK, 1.6, 6)
    A.text((e1[0] + LRASX) / 2, ay + 16, "Deflationary gap", 11, "middle")
    A.text(90, 18, "(a)", 14, "start", INK, "700")

    B = Fig(w=W, h=H, x0=85, y0=700, x1=380, y1=440)
    paxes(B, "Consumer goods", "Capital goods")
    p1 = ppc_pts(100, 500, 330, 690)
    B.curve(p1, RED)
    B.label(p1[-1][0] - 8, p1[-1][1] + 18, "PPC" + sub("", 1), GREY, 12)
    O = (B.X0, B.Y0)
    a_pt = (O[0] + 0.68 * (p1[4][0] - O[0]), O[1] + 0.68 * (p1[4][1] - O[1]))
    B.dot(*a_pt, 3.6, PURPLE)
    B.label(a_pt[0] + 8, a_pt[1] - 6, "a", INK, 13)
    B.text(85, 418, "(b)", 14, "start", INK, "700")

    fig = combine(W, H, [A, B])
    save("fig-21-2", fig, "Figure 21.2: A deflationary gap/output gap",
         "Panel (a): AD/AS diagram with AD1 crossing SRAS to the left of the vertical LRAS line, at output Y1 below full-employment output Yf, showing a deflationary gap. Panel (b): a bowed-out PPC with point a plotted inside the curve.",
         "Panel (a): aggregate demand AD<sub>1</sub> intersects SRAS at output Y<sub>1</sub>, which lies to the left of potential output Y<sub>f</sub> marked by the vertical LRAS line &ndash; the horizontal distance is the deflationary (output) gap. Panel (b): the same idea on a production possibilities curve, where point a sits inside PPC<sub>1</sub>, showing resources not fully employed.")


def fig_21_3():
    W, H = 440, 760
    A = Fig(w=W, h=H, x0=90, y0=300, x1=380, y1=55)
    SR = ((135, 275), (345, 80))
    LRASX = 305
    A1 = ((120, 95), (300, 285))
    A2 = ((170, 80), (350, 129.5))
    paxes(A, "Real output (Y)", "Average price level")
    draw_line(A, SR, RED)
    A.label(349, 76, "SRAS", RED, 12.5)
    A.line(LRASX, A.Y0, LRASX, A.Y1, INK, 2.4)
    A.label(LRASX + 6, A.Y1 + 12, "LRAS", INK, 12.5)
    draw_line(A, A1, GREY)
    A.label(304, 292, "AD" + sub("", 1), GREY, 12.5)
    draw_line(A, A2, GREY)
    A.label(354, 133, "AD" + sub("", 2), GREY, 12.5)
    e1 = A.intersect(SR, A1)
    e2 = A.intersect(SR, A2)
    assert abs(e2[0] - LRASX) < 1.0
    A.hshift(A1, A2, 105)
    A.hshift(A1, A2, 122)
    A.guide(e1[0], e1[1], "Y" + sub("", 1), None, to_y=False)
    A.dot(*e1, 3.6, INK)
    A.dot(*e2, 3.6, INK)
    A.text(e1[0], A.Y0 + 18, "Y" + sub("", 1), 11.5, "middle")
    A.text(LRASX, A.Y0 + 18, "Y" + sub("", "f"), 11.5, "middle")
    A.text(90, 18, "(a)", 14, "start", INK, "700")

    B = Fig(w=W, h=H, x0=85, y0=700, x1=380, y1=440)
    paxes(B, "Consumer goods", "Capital goods")
    p1 = ppc_pts(100, 500, 330, 690)
    B.curve(p1, RED)
    B.label(p1[-1][0] - 8, p1[-1][1] + 18, "PPC" + sub("", 1), GREY, 12)
    O = (B.X0, B.Y0)
    a_pt = (O[0] + 0.68 * (p1[4][0] - O[0]), O[1] + 0.68 * (p1[4][1] - O[1]))
    b_pt = (O[0] + 0.93 * (p1[4][0] - O[0]), O[1] + 0.93 * (p1[4][1] - O[1]))
    B.arrow(a_pt[0] + 6, a_pt[1] - 6, b_pt[0] - 4, b_pt[1] - 4, PURPLE, 2.0, 8)
    B.dot(*a_pt, 3.6, INK)
    B.dot(*b_pt, 3.6, INK)
    B.label(a_pt[0] - 16, a_pt[1] + 14, "a", INK, 13)
    B.label(b_pt[0] + 8, b_pt[1] - 4, "b", INK, 13)
    B.text(85, 418, "(b)", 14, "start", INK, "700")

    fig = combine(W, H, [A, B])
    save("fig-21-3", fig, "Figure 21.3: Economic growth to remove a deflationary gap/output gap",
         "Panel (a): AD shifts right from AD1 to AD2 along the unchanged SRAS and LRAS, moving output from Y1 up to Yf. Panel (b): the PPC shows a movement from point a (inside the curve) to point b, close to but not exactly on the curve.",
         "Panel (a): an increase in aggregate demand from AD<sub>1</sub> to AD<sub>2</sub> moves the economy along SRAS until it reaches full-employment output Y<sub>f</sub>, closing the gap. Panel (b): the matching movement on the PPC is from point a (inside the curve) to point b, which sits close to &ndash; but not exactly on &ndash; the frontier, since some natural unemployment always remains.")


def fig_21_4():
    W, H = 440, 760
    A = Fig(w=W, h=H, x0=90, y0=300, x1=380, y1=55)
    paxes(A, "Real output (Y)", "Average price level")
    L1X, L2X = 200, 300
    A.line(L1X, A.Y0, L1X, A.Y1, INK, 2.4)
    A.line(L2X, A.Y0, L2X, A.Y1, RED, 2.4)
    A.label(L1X - 34, A.Y1 - 8, "LRAS" + sub("", 1), INK, 12.5)
    A.label(L2X + 6, A.Y1 - 8, "LRAS" + sub("", 2), RED, 12.5)
    A1 = ((115, 90), (355, 280))
    draw_line(A, A1, GREY)
    A.label(359, 284, "AD" + sub("", 1), GREY, 12.5)
    ay = A.Y1 + 14
    A.arrow(L1X + 6, ay, L2X - 6, ay, PURPLE, 2.2, 8)
    A.text(L1X, A.Y0 + 18, "Y" + sub("", "f1"), 11.5, "middle")
    A.text(L2X, A.Y0 + 18, "Y" + sub("", "f2"), 11.5, "middle")
    A.text(90, 18, "(a)", 14, "start", INK, "700")

    B = Fig(w=W, h=H, x0=85, y0=700, x1=380, y1=440)
    paxes(B, "Consumer goods", "Capital goods")
    p1 = ppc_pts(100, 500, 330, 690)
    O = (B.X0, B.Y0)
    p2 = scale_from(O, p1, 1.15)
    B.curve(p1, RED)
    B.curve(p2, RED)
    B.label(p1[5][0] - 4, p1[5][1] + 24, "PPC" + sub("", 1), GREY, 12)
    B.label(p2[5][0] - 30, p2[5][1] - 12, "PPC" + sub("", 2), GREY, 12)
    for idx in (2, 5):
        q1, q2 = p1[idx], p2[idx]
        mx, my = (q1[0] + q2[0]) / 2, (q1[1] + q2[1]) / 2
        dx, dy = q2[0] - q1[0], q2[1] - q1[1]
        n = math.hypot(dx, dy)
        B.arrow(q1[0] + dx * 0.15, q1[1] + dy * 0.15,
                q2[0] - dx * 0.15, q2[1] - dy * 0.15, PURPLE, 2.0, 7)
    B.text(85, 418, "(b)", 14, "start", INK, "700")

    fig = combine(W, H, [A, B])
    save("fig-21-4", fig, "Figure 21.4: Economic growth through an increase in potential output",
         "Panel (a): LRAS shifts right from LRAS1 to LRAS2, raising full-employment output from Yf1 to Yf2. Panel (b): the PPC shifts outward from PPC1 to PPC2, shown by two outward arrows.",
         "Panel (a): the LRAS curve itself shifts rightward from LRAS<sub>1</sub> to LRAS<sub>2</sub>, raising potential output from Y<sub>f1</sub> to Y<sub>f2</sub> against an unchanged AD<sub>1</sub>. Panel (b): the whole PPC bows further out, from PPC<sub>1</sub> to PPC<sub>2</sub> &ndash; the diagrammatic equivalent of the LRAS shift.")


def fig_21_5():
    f = Fig()
    f.axes("Real output (Y)", "Average price level")
    LX1, LX2 = 180, 280
    f.line(LX1, f.Y0, LX1, f.Y1, INK, 2.4)
    f.line(LX2, f.Y0, LX2, f.Y1, RED, 2.4)
    f.label(LX1 - 40, f.Y1 - 8, "LRAS" + sub("", 1), INK, 12.5)
    f.label(LX2 + 6, f.Y1 - 8, "LRAS" + sub("", 2), RED, 12.5)
    AD1 = ((100, 100), (300, 300))
    AD2 = ((170, 70), (370, 270))
    f.line(*AD1[0], *AD1[1], GREY, 2.8)
    f.label(304, 304, "AD" + sub("", 1), GREY, 12.5)
    f.line(*AD2[0], *AD2[1], GREY, 2.8)
    f.label(374, 274, "AD" + sub("", 2), GREY, 12.5)
    e1 = f.intersect(AD1, ((LX1, 0), (LX1, 400)))
    e2 = f.intersect(AD2, ((LX2, 0), (LX2, 400)))
    assert abs(e1[1] - e2[1]) < 0.1
    f.line(f.X0, e1[1], LX2 + 8, e1[1], TEAL, 1.5, "5 4")
    f.dot(*e1, 3.6, INK)
    f.dot(*e2, 3.6, INK)
    f.text(f.X0 - 8, e1[1] + 4, "P", 11.5, "end")
    f.text(LX1, f.Y0 + 18, "Y" + sub("", "f1"), 11.5, "middle")
    f.text(LX2, f.Y0 + 18, "Y" + sub("", "f2"), 11.5, "middle")
    f.arrow(LX1 + 6, f.Y1 + 14, LX2 - 6, f.Y1 + 14, PURPLE, 2.2, 8)
    save("fig-21-5", f, "Figure 21.5: Non-inflationary growth",
         "AD/AS diagram: LRAS shifts right from LRAS1 to LRAS2 and AD shifts right from AD1 to AD2 by a matching amount, so output rises from Yf1 to Yf2 with no change in the average price level.",
         "Both LRAS (from LRAS<sub>1</sub> to LRAS<sub>2</sub>) and AD (from AD<sub>1</sub> to AD<sub>2</sub>) shift right by a matching amount, so output rises from Y<sub>f1</sub> to Y<sub>f2</sub> while the average price level, P, stays exactly the same &ndash; non-inflationary growth.")


# =============================================================== CHAPTER 22
def lorenz_pts(k, n=10):
    return [(100 * i / n, 100 * (i / n) ** k) for i in range(n + 1)]


def fig_22_1():
    f = Fig(w=460, h=400, x0=80, y0=340, x1=400, y1=40)
    f.scale(100, 100, xpad=0, ypad=0)
    f.axes("Cumulative % of population", "Cumulative % of income")
    f.xticks([20, 40, 60, 80, 100])
    f.yticks([20, 40, 60, 80, 100])
    eq = (f.pt(0, 0), f.pt(100, 100))
    draw_line(f, eq, INK, 1.8)
    f.label(f.px(78) + 4, f.py(90), "Line of equality", INK, 10.5, "middle")
    k_lar, k_mer = 1.8, 3.2
    p_lar = [f.pt(*p) for p in lorenz_pts(k_lar)]
    p_mer = [f.pt(*p) for p in lorenz_pts(k_mer)]
    poly(f, p_mer, LIGHTRED)
    f.curve(p_lar, TEAL)
    f.curve(p_mer, RED)
    f.label(p_lar[7][0] + 4, p_lar[7][1] - 6, "Larenta", TEAL, 12)
    f.label(p_mer[6][0] + 4, p_mer[6][1] + 4, "Meridia", RED, 12)
    mx, my = f.pt(55, (55 + 100 * (0.55 ** k_mer)) / 2)
    f.label(mx - 8, my - 2, "a", INK, 13, "middle")
    save("fig-22-1", f, "Figure 22.1: Lorenz curves for two fictional countries, Larenta and Meridia",
         "Lorenz curve diagram with the 45-degree line of equality and two bowed curves below it for the fictional countries Larenta and Meridia; Meridia's curve sags further from the line of equality than Larenta's, and the gap between Meridia's curve and the diagonal is shaded as area (a).",
         "Hypothetical example: the 45&deg; line is the line of absolute equality. Larenta&rsquo;s Lorenz curve (Gini &asymp; 29) stays fairly close to this line, while Meridia&rsquo;s (Gini &asymp; 52) sags much further away &ndash; the shaded area (a) between Meridia&rsquo;s curve and the line of equality is larger, so Meridia&rsquo;s income is distributed far less equally than Larenta&rsquo;s.")


def fig_22_2():
    f = Fig(w=460, h=400, x0=80, y0=340, x1=400, y1=40)
    f.scale(100, 100, xpad=0, ypad=0)
    f.axes("Cumulative % of population", "Cumulative % of income")
    f.xticks([20, 40, 60, 80, 100])
    f.yticks([20, 40, 60, 80, 100])
    eq = (f.pt(0, 0), f.pt(100, 100))
    draw_line(f, eq, INK, 1.8)
    data = [(0, 0), (20, 4), (40, 13), (60, 28), (80, 52), (100, 100)]
    pix = [f.pt(*p) for p in data]
    f.curve(pix, RED)
    labels = [
        "1st quintile: 4%",
        "1st+2nd: 13%",
        "1st-3rd: 28%",
        "1st-4th: 52%",
        "All 5: 100%",
    ]
    for (q, v), lab in zip(data[1:], labels):
        x, y = f.pt(q, v)
        f.dot(x, y, 3.4, INK)
        ax, ay = x + 10, y - 8 - (0 if v < 60 else 4)
        f.text(ax, ay, lab, 10.2, "start", INK)
    save("fig-22-2", f, "Figure 22.2: Constructing a Lorenz curve (fictional country: Vantica)",
         "Lorenz curve for the fictional country Vantica built point by point from cumulative income shares of each quintile (4%, 13%, 28%, 52%, 100%), plotted against cumulative population shares, shown below the diagonal line of equality.",
         "Hypothetical data for Vantica: the poorest quintile earns 4% of income, the poorest two quintiles together 13%, three quintiles 28%, four quintiles 52%, and all five 100%. Plotting each cumulative pair (20%,4%), (40%,13%), (60%,28%), (80%,52%), (100%,100%) and joining them from the origin produces the bowed Lorenz curve below the 45&deg; line of equality.")


# =============================================================== CHAPTER 23
def fig_23_1():
    f = Fig().scale(9, 7)
    f.axes("Textiles (bales)", "Rice (tonnes)")
    f.xticks([2, 4, 6, 8])
    f.yticks([2, 4, 6])
    Th = dline(0, 6, 8, 0)
    Pe = dline(0, 2, 6, 0)
    Th_px = (f.pt(*Th[0]), f.pt(*Th[1]))
    Pe_px = (f.pt(*Pe[0]), f.pt(*Pe[1]))
    draw_line(f, Th_px, RED)
    draw_line(f, Pe_px, GREY)
    f.label(f.px(6.6), f.py(1.9), "Thailand", RED, 12.5, "middle", )
    f.label(f.px(4.8), f.py(1.05), "Peru", GREY, 12.5, "middle")
    ax = f.px(-0.65)
    f.line(ax, f.py(2), ax, f.py(6), PURPLE, 2.0)
    f.arrowhead(ax, f.py(6), 0, PURPLE, 7)
    f.arrowhead(ax, f.py(2), 180, PURPLE, 7)
    f.label(ax - 8, (f.py(2) + f.py(6)) / 2 + 4, "(a)", PURPLE, 12, "end")
    ay = f.py(-0.65)
    f.line(f.px(6), ay, f.px(8), ay, PURPLE, 2.0)
    f.arrowhead(f.px(8), ay, 90, PURPLE, 7)
    f.arrowhead(f.px(6), ay, -90, PURPLE, 7)
    f.label((f.px(6) + f.px(8)) / 2, ay + 16, "(b)", PURPLE, 12, "middle")
    save("fig-23-1", f, "Figure 23.1: Production possibility curves to show comparative advantage",
         "Two straight-line PPCs on rice (vertical) and textiles (horizontal) axes: Thailand's frontier lies further out on both axes than Peru's, with the gap (a) on the rice axis much larger than the gap (b) on the textiles axis.",
         "Two straight-line (constant opportunity cost) PPCs, drawn to the same scale: Thailand can produce up to 6 tonnes of rice or 8 bales of textiles; Peru up to 2 tonnes of rice or 6 bales of textiles. Thailand has an absolute advantage in both goods, but its comparative advantage lies in rice, where the gap between the two countries&rsquo; frontiers, (a), is largest; Peru&rsquo;s comparative advantage lies in textiles, where the gap, (b), is smallest.")


def _ppc_scene(good_v_max, good_h_max, x_pt, spec_pt, exp_leg, y_pt, vlabel, hlabel, color):
    xmax, ymax = good_h_max * 1.12, good_v_max * 1.12
    f = Fig().scale(xmax, ymax)
    f.axes(hlabel, vlabel)
    ppc = dline(0, good_v_max, good_h_max, 0)
    ppc_px = (f.pt(*ppc[0]), f.pt(*ppc[1]))
    draw_line(f, ppc_px, color)
    xp = f.pt(*x_pt)
    sp = f.pt(*spec_pt)
    yp = f.pt(*y_pt)
    cp = f.pt(*exp_leg)
    f.guide(*xp, f"{x_pt[0]:,.0f}", f"{x_pt[1]:,.0f}")
    f.dot(*xp, 3.6, INK)
    f.label(xp[0] + 8, xp[1] - 6, "x", INK, 13)
    f.dot(*sp, 3.4, GREY)
    f.line(sp[0], sp[1], cp[0], cp[1], PURPLE, 2.0, "6 4")
    f.arrow(cp[0], cp[1], yp[0], yp[1], PURPLE, 2.0, 8)
    f.dot(*yp, 3.6, INK)
    f.label(yp[0] + 8, yp[1] - 6, "y", INK, 13)
    f.guide(*yp, f"{y_pt[0]:,.0f}", f"{y_pt[1]:,.0f}", )
    return f


def fig_23_2a():
    # Peru specialises in textiles (horizontal): x=(280,180) -> spec(700,0)
    # exports 300 textiles, imports 200 rice -> y=(400,200)
    f = _ppc_scene(300, 700, (280, 180), (700, 0), (400, 0), (400, 200),
                   "Rice (000 tonnes)", "Textiles (000 bales)", RED)
    f.label(f.px(0) + 8, f.py(300) - 8, "Peru's PPC", RED, 11.5)
    f.text(f.X1 - 6, f.Y1 + 16, "Exports: 300,000 textiles", 10.5, "end", PURPLE)
    f.text(f.X1 - 6, f.Y1 + 30, "Imports: 200,000 rice", 10.5, "end", PURPLE)
    save("fig-23-2a", f, "Figure 23.2(a): Peru &ndash; potential gains from specialization and trade",
         "Peru's PPC (rice vertical, textiles horizontal) with point x at 280 textiles, 180 rice before specialization, and point y outside the curve at 400 textiles, 200 rice after specialization and trade, with exports and imports marked.",
         "Peru's straight-line PPC runs from 300,000 tonnes of rice to 700,000 bales of textiles. Before trade Peru produces and consumes at x (280,000 textiles, 180,000 rice). Specializing fully in textiles (its comparative advantage), Peru produces 700,000 textiles, exports 300,000 of them and imports 200,000 tonnes of rice, ending at y (400,000 textiles, 200,000 rice) &ndash; more of <em>both</em> goods than at x.")


def fig_23_2b():
    # Thailand specialises in rice (vertical): x=(200,1200) -> spec(0,1600)
    # exports 200 rice, imports 300 textiles -> y=(300,1400)
    f = _ppc_scene(1600, 800, (200, 1200), (0, 1600), (0, 1400), (300, 1400),
                   "Rice (000 tonnes)", "Textiles (000 bales)", RED)
    f.label(f.px(0) + 10, f.py(1600) - 8, "Thailand's PPC", RED, 11.5)
    f.text(f.X1 - 6, f.Y1 + 16, "Exports: 200,000 rice", 10.5, "end", PURPLE)
    f.text(f.X1 - 6, f.Y1 + 30, "Imports: 300,000 textiles", 10.5, "end", PURPLE)
    save("fig-23-2b", f, "Figure 23.2(b): Thailand &ndash; potential gains from specialization and trade",
         "Thailand's PPC (rice vertical, textiles horizontal) with point x at 200 textiles, 1200 rice before specialization, and point y outside the curve at 300 textiles, 1400 rice after specialization and trade, with exports and imports marked.",
         "Thailand's straight-line PPC runs from 1,600,000 tonnes of rice to 800,000 bales of textiles &ndash; further out on both axes than Peru's, reflecting its absolute advantage. Before trade Thailand produces and consumes at x (200,000 textiles, 1,200,000 rice). Specializing fully in rice, it produces 1,600,000 tonnes, exports 200,000 tonnes and imports 300,000 bales of textiles, ending at y (300,000 textiles, 1,400,000 rice) &ndash; a gain of both goods over x.")


def fig_23_3():
    f = Fig().scale(7, 14)
    f.axes("Textiles (bales)", "Rice (tonnes)")
    f.xticks([2, 4, 6])
    f.yticks([2, 4, 6, 8, 10, 12])
    Th = dline(0, 12, 6, 0)
    Pe = dline(0, 4, 2, 0)
    draw_line(f, (f.pt(*Th[0]), f.pt(*Th[1])), RED)
    draw_line(f, (f.pt(*Pe[0]), f.pt(*Pe[1])), GREY)
    f.label(f.px(4.4), f.py(4.6), "Thailand", RED, 12.5)
    f.label(f.px(1.6), f.py(2.7), "Peru", GREY, 12.5)
    f.text(f.px(3.5), f.py(11.5), "Same slope (2 tonnes rice per bale)", 11, "middle")
    f.text(f.px(3.5), f.py(10.5), "for both countries", 11, "middle")
    save("fig-23-3", f, "Figure 23.3: Identical opportunity costs",
         "Two parallel straight-line PPCs on rice and textiles axes with the same slope: Thailand's line further from the origin than Peru's, showing identical opportunity costs and therefore no gains from trade.",
         "Thailand's PPC (0 textiles, 12 tonnes rice to 6 textiles, 0 rice) and Peru's (0 textiles, 4 tonnes rice to 2 textiles, 0 rice) have the <em>same</em> slope: 2 tonnes of rice per bale of textiles for both. Thailand has an absolute advantage in both goods (its line lies further out), but because the opportunity cost ratio is identical, there is no comparative advantage for either country &ndash; and so no gains available from specialization and trade.")


# =============================================================== CHAPTER 24
def _sd(f, Sdom, Dm, xmax, good, Sdom_label="S (Domestic)"):
    l_S = dline(0, Sdom(0), xmax, Sdom(xmax))
    l_D = dline(0, Dm(0), xmax, Dm(xmax))
    l_S_px = (f.pt(*l_S[0]), f.pt(*l_S[1]))
    l_D_px = (f.pt(*l_D[0]), f.pt(*l_D[1]))
    draw_line(f, l_S_px, RED)
    draw_line(f, l_D_px, GREY)
    return l_S_px, l_D_px


def fig_24_1():
    Sdom = lambda q: 4 + 0.1 * q
    Dm = lambda q: 40 - 0.1 * q
    f = Fig(w=430, h=380).scale(330, 42)
    f.axes("Quantity of coffee (000 tonnes)", "Price of coffee ($ per kg)")
    l_S, l_D = _sd(f, Sdom, Dm, 320, "coffee")
    e = f.equilibrium(l_S, l_D, "Q" + sub("", "e"), "P" + sub("", "e"), dot=GREY)
    Pw = 10
    l_w = (f.pt(0, Pw), f.pt(320, Pw))
    draw_line(f, l_w, RED)
    Q1 = f.intersect(l_S, l_w)
    Q4 = f.intersect(l_D, l_w)
    f.guide(Q1[0], Q1[1], "Q" + sub("", 1), None, to_y=False)
    f.guide(Q4[0], Q4[1], "Q" + sub("", 2), None, to_y=False)
    f.ytick(f.py(Pw), "P" + sub("", "w"))
    f.dot(*Q1, 3.6, INK)
    f.dot(*Q4, 3.6, INK)
    yb = f.py(Pw) - 16
    f.arrow(Q1[0] + 4, yb, Q4[0] - 4, yb, PURPLE, 2.0, 7)
    f.arrow(Q4[0] - 4, yb, Q1[0] + 4, yb, PURPLE, 2.0, 7)
    f.text((Q1[0] + Q4[0]) / 2, yb - 8, "Imports", 11, "middle", PURPLE)
    f.label(f.px(320) + 6, f.py(Sdom(320)) - 4, "S (Domestic)", RED, 12)
    f.label(f.px(320) + 6, f.py(Dm(320)) + 4, "D", GREY, 12)
    f.label(f.px(320) + 6, f.py(Pw) + 4, "S (World)", RED, 11.5)
    save("fig-24-1", f, "Figure 24.1: Free trade in coffee (importing case)",
         "Supply and demand diagram for coffee: S(Domestic) and D intersect at autarky price Pe and quantity Qe, while a horizontal S(World) line at the lower world price Pw shows imports filling the gap between domestic supply Q1 and total quantity demanded Q2.",
         "Without trade, domestic S(Domestic) and D cross at the autarky price P<sub>e</sub> = $22/kg and quantity Q<sub>e</sub> = 180,000 tonnes. Once the country can import at the lower world price P<sub>w</sub> = $10, the price falls: domestic output falls to Q<sub>1</sub> = 60,000 tonnes, quantity demanded rises to Q<sub>2</sub> = 300,000 tonnes, and the gap of 240,000 tonnes is met by imports.")


def fig_24_2():
    Sdom = lambda q: 4 + 0.1 * q
    Dm = lambda q: 40 - 0.1 * q
    f = Fig(w=430, h=380).scale(330, 42)
    f.axes("Quantity of coffee (000 tonnes)", "Price of coffee ($ per kg)")
    l_S, l_D = _sd(f, Sdom, Dm, 320, "coffee")
    e = f.equilibrium(l_S, l_D, "Q" + sub("", "e"), "P" + sub("", "e"), dot=GREY)
    Pw = 28
    l_w = (f.pt(0, Pw), f.pt(320, Pw))
    draw_line(f, l_w, RED)
    Q1 = f.intersect(l_D, l_w)
    Q2 = f.intersect(l_S, l_w)
    f.guide(Q1[0], Q1[1], "Q" + sub("", 1), None, to_y=False)
    f.guide(Q2[0], Q2[1], "Q" + sub("", 2), None, to_y=False)
    f.ytick(f.py(Pw), "P" + sub("", "w"))
    f.dot(*Q1, 3.6, INK)
    f.dot(*Q2, 3.6, INK)
    yb = f.py(Pw) - 16
    f.arrow(Q1[0] + 4, yb, Q2[0] - 4, yb, PURPLE, 2.0, 7)
    f.arrow(Q2[0] - 4, yb, Q1[0] + 4, yb, PURPLE, 2.0, 7)
    f.text((Q1[0] + Q2[0]) / 2, yb - 8, "Exports", 11, "middle", PURPLE)
    f.label(f.px(320) + 6, f.py(Sdom(320)) - 4, "S (Domestic)", RED, 12)
    f.label(f.px(320) + 6, f.py(Dm(320)) + 4, "D", GREY, 12)
    f.label(f.px(320) + 6, f.py(Pw) + 4, "S (World)", RED, 11.5)
    save("fig-24-2", f, "Figure 24.2: Exporting when the world price is above the domestic price",
         "Same S(Domestic)/D diagram as Figure 24.1 but with the horizontal S(World) line drawn above the autarky price Pe, so domestic demand falls to Q1, domestic supply rises to Q2, and the surplus Q1Q2 is exported.",
         "With the same domestic S(Domestic) and D as Figure 24.1, but a world price P<sub>w</sub> = $28/kg above the autarky price P<sub>e</sub> = $22, domestic quantity demanded falls to Q<sub>1</sub> = 120,000 tonnes while domestic output expands to Q<sub>2</sub> = 240,000 tonnes; the surplus of 120,000 tonnes is exported at the higher world price.")


def fig_24_3():
    Sdom = lambda q: 4 + 0.1 * q
    Dm = lambda q: 40 - 0.1 * q
    f = Fig(w=480, h=380).scale(330, 42)
    f.axes("Quantity of coffee (000 tonnes)", "Price of coffee ($ per kg)")
    l_S, l_D = _sd(f, Sdom, Dm, 320, "coffee")
    Pw, Pt = 10, 16
    l_w = (f.pt(0, Pw), f.pt(320, Pw))
    l_t = (f.pt(0, Pt), f.pt(320, Pt))
    pts = {}
    pts["Q1"] = f.intersect(l_S, l_w)
    pts["Q2"] = f.intersect(l_S, l_t)
    pts["Q3"] = f.intersect(l_D, l_t)
    pts["Q4"] = f.intersect(l_D, l_w)
    poly(f, [pts["Q1"], (pts["Q2"][0], pts["Q1"][1]), pts["Q2"]], LIGHTTEAL)
    poly(f, [pts["Q3"], (pts["Q3"][0], pts["Q4"][1]), pts["Q4"]], LIGHTRED)
    poly(f, [pts["Q2"], pts["Q3"], (pts["Q3"][0], pts["Q1"][1]),
             (pts["Q2"][0], pts["Q1"][1])], LIGHTPURPLE)
    draw_line(f, l_S, RED)
    draw_line(f, l_D, GREY)
    draw_line(f, l_w, RED)
    draw_line(f, l_t, RED)
    for k in ("Q1", "Q2", "Q3", "Q4"):
        f.guide(pts[k][0], pts[k][1], k[0] + sub("", k[1]), None, to_y=False)
        f.dot(*pts[k], 3.6, INK)
    f.ytick(f.py(Pw), "P" + sub("", "w"))
    f.ytick(f.py(Pt), "P" + sub("", "w+T"))
    f.label(f.px(320) + 6, f.py(Sdom(320)) - 4, "S (Domestic)", RED, 12)
    f.label(f.px(320) + 6, f.py(Dm(320)) + 4, "D", GREY, 12)
    f.label(f.px(320) + 6, f.py(Pt) + 4, "S (World)+tariff", RED, 11)
    f.label(f.px(320) + 6, f.py(Pw) + 4, "S (World)", RED, 11.5)
    f.text(140, 300, "Production", 10.5, "middle")
    f.text(140, 313, "inefficiency", 10.5, "middle")
    f.text(300, 300, "Tariff", 10.5, "middle", PURPLE)
    f.text(300, 313, "revenue", 10.5, "middle", PURPLE)
    f.text(255, 60, "Consumer surplus", 10.5, "middle")
    f.text(255, 73, "loss", 10.5, "middle")
    save("fig-24-3", f, "Figure 24.3: A tariff on coffee imports",
         "Tariff diagram: the S(World) line shifts up to S(World)+tariff, raising price from Pw to Pw+T, cutting imports from Q1Q4 to Q2Q3, with domestic output, government tariff revenue and dead-weight loss areas shaded.",
         "Starting from free trade at P<sub>w</sub> = $10 (imports of 240,000 tonnes, between Q<sub>1</sub> = 60,000 and Q<sub>4</sub> = 300,000), a tariff of $6/kg raises the price to P<sub>w+T</sub> = $16. Domestic output rises to Q<sub>2</sub> = 120,000 tonnes and quantity demanded falls to Q<sub>3</sub> = 240,000, so imports shrink to 120,000 tonnes. The government collects tariff revenue of $6 &times; 120,000 = $720,000 (shaded rectangle); the two shaded triangles show the dead-weight loss of production inefficiency (Q<sub>1</sub>Q<sub>2</sub>, now grown by less efficient domestic farmers) and of lost consumer surplus (Q<sub>3</sub>Q<sub>4</sub>, no longer consumed).")


def fig_24_4():
    Sdom = lambda q: 4 + 0.1 * q
    Sdom_sub = lambda q: -2 + 0.1 * q
    Dm = lambda q: 40 - 0.1 * q
    f = Fig(w=480, h=380).scale(330, 42)
    f.axes("Quantity of coffee (000 tonnes)", "Price of coffee ($ per kg)")
    l_S = (f.pt(0, Sdom(0)), f.pt(320, Sdom(320)))
    l_Ssub = (f.pt(0, Sdom_sub(0)), f.pt(320, Sdom_sub(320)))
    l_D = (f.pt(0, Dm(0)), f.pt(320, Dm(320)))
    Pw, subsidy = 10, 6
    Q1q, Q3q = 60, 120
    l_w = (f.pt(0, Pw), f.pt(320, Pw))
    Q1 = f.pt(Q1q, Pw)
    Q3 = f.pt(Q3q, Pw)
    top = f.pt(Q3q, Sdom(Q3q))
    poly(f, [f.pt(0, Pw), f.pt(0, Pw + subsidy), f.pt(Q3q, Pw + subsidy), Q3], LIGHTPURPLE)
    poly(f, [Q1, Q3, top], LIGHTTEAL)
    draw_line(f, l_S, RED)
    draw_line(f, l_Ssub, RED, dash="6 4")
    draw_line(f, l_D, GREY)
    draw_line(f, l_w, RED)
    f.guide(Q1[0], Q1[1], "Q" + sub("", 1), None, to_y=False)
    f.guide(Q3[0], Q3[1], "Q" + sub("", 3), None, to_y=False)
    f.dot(*Q1, 3.6, INK)
    f.dot(*Q3, 3.6, INK)
    f.dot(*top, 3.6, INK)
    f.ytick(f.py(Pw), "P" + sub("", "w"))
    f.vshift(l_S, l_Ssub, f.px(90), gap=3)
    f.label(f.px(320) + 6, f.py(Sdom(320)) - 4, "S (Domestic)", RED, 12)
    f.label(f.px(320) + 6, f.py(Sdom_sub(320)) + 12, "S (Domestic)+subsidy", RED, 11)
    f.label(f.px(320) + 6, f.py(Dm(320)) + 4, "D", GREY, 12)
    f.text(150, 300, "Production", 10.5, "middle")
    f.text(150, 313, "inefficiency", 10.5, "middle")
    f.text(220, 60, "Subsidy cost = $6 x 120,000 = $720,000", 10.5, "middle", PURPLE)
    save("fig-24-4", f, "Figure 24.4: A subsidy on domestic coffee production",
         "Subsidy diagram: S(Domestic) shifts right/down to S(Domestic)+subsidy, price stays at Pw, domestic output rises from Q1 to Q3, imports shrink, and the government's subsidy cost and efficiency-loss areas are shaded.",
         "A subsidy of $6/kg shifts S(Domestic) down to S(Domestic)+subsidy. Because the market price stays at P<sub>w</sub> = $10, quantity demanded is unchanged, but domestic output rises from Q<sub>1</sub> = 60,000 to Q<sub>3</sub> = 120,000 tonnes, shrinking imports. The government pays a subsidy of $6 &times; 120,000 = $720,000 (shaded rectangle); the shaded triangle is the production-inefficiency dead-weight loss, since Q<sub>1</sub>Q<sub>3</sub> is now grown domestically at higher opportunity cost than importing it. Unlike a tariff, there is no loss of consumer surplus, because price does not rise.")


def fig_24_5():
    Sdom = lambda q: 4 + 0.1 * q
    Dm = lambda q: 40 - 0.1 * q
    f = Fig(w=480, h=380).scale(330, 42)
    f.axes("Quantity of coffee (000 tonnes)", "Price of coffee ($ per kg)")
    l_S = (f.pt(0, Sdom(0)), f.pt(320, Sdom(320)))
    l_D = (f.pt(0, Dm(0)), f.pt(320, Dm(320)))
    Pw = 10
    l_w = (f.pt(0, Pw), f.pt(320, Pw))
    quota = 120
    # effective supply-with-quota: Sdom shifted right by the quota amount
    Sq = lambda q: Sdom(q - quota)
    l_Sq = (f.pt(180, Sq(180)), f.pt(300, Sq(300)))
    draw_line(f, l_S, RED)
    draw_line(f, l_D, GREY)
    draw_line(f, l_w, RED)
    draw_line(f, l_Sq, PURPLE, dash="6 4")
    Q1 = f.intersect(l_S, l_w)
    e = f.intersect(l_Sq, l_D)
    assert abs(e[0] - f.px(240)) < 1 and abs(e[1] - f.py(16)) < 1
    Q2 = f.pt(120, Sdom(120))
    Q3 = f.pt(180, Pw)
    Q4free = f.intersect(l_D, l_w)
    poly(f, [Q1, (Q2[0], Q1[1]), Q2], LIGHTTEAL)
    poly(f, [e, (e[0], Q4free[1]), Q4free], LIGHTRED)
    f.dot(*Q1, 3.6, INK)
    f.dot(*Q2, 3.6, INK)
    f.dot(*Q3, 3.6, INK)
    f.dot(*e, 3.6, INK)
    f.guide(Q1[0], Q1[1], "Q" + sub("", 1), None, to_y=False)
    f.guide(Q2[0], Q2[1], "Q" + sub("", 2), None, to_y=False)
    f.guide(Q3[0], Q3[1], "Q" + sub("", 3), None, to_y=False)
    f.guide(e[0], e[1], "Q" + sub("", 4), None, to_y=False)
    f.ytick(f.py(Pw), "P" + sub("", "w"))
    f.ytick(f.py(16), "P" + sub("", "quota"))
    yb = f.py(Pw) - 16
    f.arrow(Q1[0] + 4, yb, Q3[0] - 4, yb, PURPLE, 2.0, 7)
    f.arrow(Q3[0] - 4, yb, Q1[0] + 4, yb, PURPLE, 2.0, 7)
    f.text((Q1[0] + Q3[0]) / 2, yb - 8, "Import quota = 120,000", 10, "middle", PURPLE)
    f.label(f.px(320) + 6, f.py(Sdom(320)) - 4, "S (Domestic)", RED, 12)
    f.label(f.px(320) + 6, f.py(Dm(320)) + 4, "D", GREY, 12)
    f.label(f.px(300) - 4, f.py(Sq(300)) - 8, "S (Domestic)+Quota", PURPLE, 10.5, "end")
    f.text(150, 300, "Production", 10.5, "middle")
    f.text(150, 313, "inefficiency", 10.5, "middle")
    f.text(280, 60, "Consumer surplus", 10.5, "middle")
    f.text(280, 73, "loss (no government", 10.5, "middle")
    f.text(280, 86, "revenue with a quota)", 10.5, "middle")
    save("fig-24-5", f, "Figure 24.5: A quota on coffee imports",
         "Quota diagram: after a quota of 120,000 tonnes is imposed, the effective domestic supply curve shifts to S(Domestic)+Quota, price rises from Pw to Pquota, and quantity demanded falls to Q4, with the resulting dead-weight losses shaded.",
         "A quota limiting imports to 120,000 tonnes pushes the price up from P<sub>w</sub> = $10 to P<sub>quota</sub> = $16: domestic output rises from Q<sub>1</sub> = 60,000 to Q<sub>2</sub> = 120,000 tonnes (read off the unchanged S(Domestic)), and total quantity demanded falls to Q<sub>4</sub> = 240,000 tonnes. Unlike a tariff, the government earns no revenue &ndash; the gain from the higher price goes to domestic and quota-holding foreign producers. The two shaded triangles are the same two dead-weight losses as with a tariff: production inefficiency and lost consumer surplus.")


def fig_24_extra1():
    Sdom = lambda q: 2 + 0.02 * q
    Dm = lambda q: 10 - 0.02 * q
    f = Fig(w=480, h=380).scale(330, 11)
    f.axes("Quantity of olive oil (000 litres)", "Price of olive oil ($ per litre)")
    l_S = (f.pt(0, Sdom(0)), f.pt(320, Sdom(320)))
    l_D = (f.pt(0, Dm(0)), f.pt(320, Dm(320)))
    draw_line(f, l_S, RED)
    draw_line(f, l_D, GREY)
    e0 = f.equilibrium(l_S, l_D, "Q" + sub("", "e"), "P" + sub("", "e"), dot=GREY)
    Pw, Pt = 4, 5.2
    l_w = (f.pt(0, Pw), f.pt(320, Pw))
    l_t = (f.pt(0, Pt), f.pt(320, Pt))
    pts = {}
    pts["Q1"] = f.intersect(l_S, l_w)
    pts["Q2"] = f.intersect(l_S, l_t)
    pts["Q3"] = f.intersect(l_D, l_t)
    pts["Q4"] = f.intersect(l_D, l_w)
    poly(f, [pts["Q1"], (pts["Q2"][0], pts["Q1"][1]), pts["Q2"]], LIGHTTEAL)
    poly(f, [pts["Q3"], (pts["Q3"][0], pts["Q4"][1]), pts["Q4"]], LIGHTRED)
    poly(f, [pts["Q2"], pts["Q3"], (pts["Q3"][0], pts["Q1"][1]),
             (pts["Q2"][0], pts["Q1"][1])], LIGHTPURPLE)
    draw_line(f, l_S, RED)
    draw_line(f, l_D, GREY)
    draw_line(f, l_w, RED)
    draw_line(f, l_t, RED)
    for k in ("Q1", "Q2", "Q3", "Q4"):
        f.guide(pts[k][0], pts[k][1], k[0] + sub("", k[1]), None, to_y=False)
        f.dot(*pts[k], 3.6, INK)
    f.ytick(f.py(Pw), "$1.00")
    f.ytick(f.py(Pt), "$1.30")
    f.label(f.px(320) + 6, f.py(Sdom(320)) - 4, "S (Domestic)", RED, 12)
    f.label(f.px(320) + 6, f.py(Dm(320)) + 4, "D", GREY, 12)
    f.label(f.px(320) + 6, f.py(Pt) + 4, "S" + sub("", "W") + "+Tariff", RED, 11)
    f.label(f.px(320) + 6, f.py(Pw) + 4, "S" + sub("", "W"), RED, 11.5)
    f.text(140, 300, "Efficiency", 10.5, "middle")
    f.text(140, 313, "loss", 10.5, "middle")
    f.text(255, 300, "Tariff revenue", 10.5, "middle", PURPLE)
    f.text(255, 60, "Dead-weight loss of", 10.5, "middle")
    f.text(255, 73, "consumer surplus", 10.5, "middle")
    save("fig-24-extra1", f, "Figure: Tariff on olive oil imports (worked example)",
         "Olive oil market diagram: S(Domestic) and D cross at the no-trade equilibrium; a horizontal Sw line at $1 shows free-trade imports, and Sw+Tariff at $1.30 shows the after-tariff price, with the efficiency-loss and dead-weight-loss-of-consumer-surplus triangles shaded.",
         "Worked example: the world price of olive oil is $1.00/litre (S<sub>W</sub>), so free trade cuts domestic output to 100,000 litres and imports rise to 200,000 litres (total demand 300,000). A 30&cent; tariff raises the price to $1.30 (S<sub>W</sub>+Tariff): domestic output rises to 160,000 litres, quantity demanded falls to 240,000, and imports fall to 80,000 litres. Consumer expenditure rises from $1.00 &times; 300,000 = $300,000 to $1.30 &times; 240,000 = $312,000, even though quantity falls; government tariff revenue = $0.30 &times; 80,000 = $24,000. The shaded triangles show the efficiency loss (production shifting to less efficient domestic growers) and the dead-weight loss of consumer surplus.")


if __name__ == "__main__":
    which = sys.argv[1:]
    for name, fn in list(globals().items()):
        if name.startswith("fig_") and (not which or name[4:].replace("_", "-") in which):
            fn()
