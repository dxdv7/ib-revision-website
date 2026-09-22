"""Original vector figures for chapters 8 (taxes, subsidies, price controls)
and 9 (externalities). Built on tools/figlib.py; nothing traced from a scan.

Usage: python3 tools/figs_ch08_09.py [fig-8-2 fig-9-1 ...]
"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import *

OUT = "/Users/davidbukraba/Desktop/IB WEBSITE/assets/figures-original"
BLUE = "#1f4e9c"
AMB = "#f6d9a0"
TEALF = "#b4e3e9"
LOSS = "#f3b3aa"
GAIN = "#b5e2c0"

# ---------------------------------------------------------------- helpers


def sb(base, n, rest=""):
    """Label with subscript; optional text after the subscript."""
    s = f'{base}<tspan font-size="70%" dy="3">{n}</tspan>'
    if rest:
        s += f'<tspan dy="-3">{rest}</tspan>'
    return s


def newf(xmax, ymax, w=420, h=380, x0=78, y0=318, x1=384, y1=30):
    return Fig(w, h, x0, y0, x1, y1).scale(xmax, ymax)


def L(f, a, b, q0, q1):
    """Pixel line for the data-space line p = a + b*q between q0 and q1."""
    return (f.pt(q0, a + b * q0), f.pt(q1, a + b * q1))


def draw(f, l, color, dash=None, w=2.8):
    f.line(l[0][0], l[0][1], l[1][0], l[1][1], color, w, dash)


def T(f, x, y, s, size=12, anchor="start", color=INK, weight="400", halo=False,
      italic=False):
    if halo:
        st = ' font-style="italic"' if italic else ""
        f.add(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" text-anchor="{anchor}" '
              f'fill="{color}" font-weight="{weight}"{st} stroke="#ffffff" stroke-width="4" '
              f'stroke-linejoin="round" paint-order="stroke">{s}</text>')
    else:
        f.text(x, y, s, size, anchor, color, weight, italic=italic)


def poly(f, pts, fill):
    p = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    f.add(f'<polygon points="{p}" fill="{fill}" stroke="none"/>')


def rect(f, q0, p0, q1, p1, fill):
    poly(f, [f.pt(q0, p0), f.pt(q1, p0), f.pt(q1, p1), f.pt(q0, p1)], fill)


def hbrace(f, x1, x2, y, h=7, down=True, color=TEAL):
    s = 1 if down else -1
    mx = (x1 + x2) / 2
    d = (f"M{x1:.1f},{y:.1f} Q{x1:.1f},{y + s * h:.1f} {x1 + h:.1f},{y + s * h:.1f} "
         f"L{mx - h:.1f},{y + s * h:.1f} Q{mx:.1f},{y + s * h:.1f} {mx:.1f},{y + s * 2 * h:.1f} "
         f"Q{mx:.1f},{y + s * h:.1f} {mx + h:.1f},{y + s * h:.1f} "
         f"L{x2 - h:.1f},{y + s * h:.1f} Q{x2:.1f},{y + s * h:.1f} {x2:.1f},{y:.1f}")
    f.path(d, color, 1.8)


def dgap(f, x, y1, y2, color=PURPLE):
    """Dotted double-headed vertical arrow (size of an externality gap)."""
    f.line(x, y1, x, y2, color, 1.8, "2 3", "butt")
    up = y2 < y1
    f.arrowhead(x, y2, -90 if up else 90, color, 7)
    f.arrowhead(x, y1, 90 if up else -90, color, 7)


def arrow_label(f, x, y_from, y_to, text, size=12):
    """Label kept clear of sloping curves: above an up-arrow, below a down-arrow."""
    if y_to < y_from:
        T(f, x + 3, y_to - 7, text, size, "end")
    else:
        T(f, x - 3, y_to + 16, text, size, "start")


def pointer(f, x1, y1, x2, y2, color=INK):
    f.arrow(x1, y1, x2, y2, color, 1.4, 6)


def dot_label(f, pt, s, dx=8, dy=4, size=11.5, color=INK, halo=False):
    T(f, pt[0] + dx, pt[1] + dy, s, size, "start", color, halo=halo)


def legend(m, x, y, items, gap=19):
    for i, (kind, col, text) in enumerate(items):
        yy = y + i * gap
        if kind == "rect":
            m.add(f'<rect x="{x}" y="{yy - 10}" width="16" height="11" fill="{col}" '
                  f'stroke="#9a9a9a" stroke-width="0.7"/>')
        elif kind == "num":
            T(m, x + 4, yy, col[0], 12.5, "start", PURPLE, "700")
        elif kind == "dash":
            m.line(x, yy - 4, x + 18, yy - 4, col, 2.4, "6 4", "butt")
        T(m, x + 25, yy, text, 11.5)


def assemble(w, h, panels, title, desc, extra=None):
    m = Fig(w, h)
    for f, dx in panels:
        m.add(f'<g transform="translate({dx},0)">')
        m.parts.extend(f.parts)
        m.add("</g>")
    if extra:
        extra(m)
    return m.svg(title, desc)


def ptitle(f, s):
    T(f, (f.X0 + f.X1) / 2, 20, s, 12.5, "middle", INK, italic=True)


FIGS = {}


def fig(name):
    def deco(fn):
        FIGS[name] = fn
        return fn
    return deco


def save(name, svg, label, alt, caption):
    os.makedirs(OUT, exist_ok=True)
    open(f"{OUT}/{name}.svg", "w").write(svg)
    with open(f"{OUT}/{name}.json", "w") as fh:
        json.dump({"label": label, "alt": alt, "caption": caption}, fh, indent=2)
        fh.write("\n")


# ------------------------------------------------------------ chapter 8


@fig("fig-8-1")
def f81():
    panels = []
    for i in (0, 1):
        f = newf(100, 30, w=430, h=380, x0=78, y0=318, x1=392, y1=44)
        f.axes("Quantity of a good", "Price ($)")
        S = L(f, 2, 0.2, 10, 90)
        if i == 0:
            St = L(f, 5, 0.2, 10, 90)
            ptitle(f, "(a) A specific tax ($3 per unit)")
        else:
            St = L(f, 2.5, 0.25, 10, 90)
            ptitle(f, "(b) A percentage tax (25% of price)")
            for q in (30, 70):
                p = 2 + 0.2 * q
                f.guide(f.px(q), f.py(p), None, f"{p:g}", to_x=False)
        draw(f, St, RED)
        draw(f, S, RED)
        T(f, S[1][0] + 8, S[1][1] + 4, "S", 13, "start", RED)
        T(f, St[1][0] + 8, St[1][1] + 4, "S + tax", 13, "start", RED)
        for q in (30, 70):
            f.vshift(S, St, f.px(q))
            gap = (3 if i == 0 else 0.25 * (2 + 0.2 * q))
            arrow_label(f, f.px(q), f.y_at(S, f.px(q)), f.y_at(St, f.px(q)), f"${gap:g}")
        panels.append((f, i * 430))
    return assemble(860, 380, panels, "Specific versus percentage tax on supply",
                    "Two panels. A specific tax shifts supply up in parallel by $3; a 25% tax shifts it up by $2 at a price of $8 and $4 at a price of $16."), \
        ("Figure 8.1: Specific and percentage taxes shift the supply curve differently",
         "Two supply diagrams. In (a) a $3 specific tax moves S up in parallel to S + tax; in (b) a 25% tax makes the gap widen from $2 at a price of $8 to $4 at a price of $16.",
         "(a) A specific tax of $3 per unit lifts the supply curve by the same $3 vertical distance at every quantity, so S + tax is parallel to S. (b) A 25% percentage tax is a fixed share of the price, so the vertical gap grows as price rises: $2 where S is at $8 and $4 where S is at $16, and S + tax becomes steeper than S.")


def tax_panel(D, S, t, mode, ymax, xmax=100, title="", arrow_q=78, Wd=400, X0=70,
              X1=376, Y1=44, ylabel="Price ($)", xlabel="Quantity", tl=None,
              Send=None, Stq=None, Dq=None, Slab="S", Stlab="S + tax", wl=(0, -9), xl=(0, -9)):
    f = newf(xmax, ymax, w=Wd, h=380, x0=X0, y0=318, x1=X1, y1=Y1)
    Dl = L(f, D[0], D[1], D[2], D[3])
    Sl = L(f, S[0], S[1], S[2], S[3])
    Stl = L(f, S[0] + t, S[1], Stq[0], Stq[1])
    e0 = f.intersect(Sl, Dl)
    e1 = f.intersect(Stl, Dl)
    Yp = (e1[0], f.y_at(Sl, e1[0]))
    Y0 = f.Y0

    def R(x, ya, yb, fill):
        poly(f, [(f.X0, ya), (x, ya), (x, yb), (f.X0, yb)], fill)
    if mode == "rev":
        R(e0[0], e0[1], Y0, AMB)
        R(e1[0], Yp[1], Y0, TEALF)
    elif mode == "tax":
        R(e1[0], e1[1], Yp[1], TEALF)
    else:
        R(e1[0], e1[1], e0[1], AMB)
        R(e1[0], e0[1], Yp[1], TEALF)
    f.axes(xlabel, ylabel)
    if title:
        ptitle(f, title)
    f.guide(*e0, sb("Q", "e"), sb("P", "e"))
    f.guide(*e1, sb("Q", "1"), sb("P", "1"))
    f.guide(*Yp, None, "C", to_x=False)
    draw(f, Dl, GREY)
    draw(f, Sl, RED)
    draw(f, Stl, RED)
    T(f, Dl[1][0] + 8, Dl[1][1] + 4, "D", 13, "start", GREY)
    T(f, Sl[1][0] + 8, Sl[1][1] + 4, Slab, 13, "start", RED)
    T(f, Stl[1][0] + 8, Stl[1][1] + 4, Stlab, 13, "start", RED)
    f.equilibrium(Sl, Dl, guides=False)
    f.equilibrium(Stl, Dl, guides=False)
    f.dot(*Yp, 3.6, INK)
    T(f, e0[0] + wl[0], e0[1] + wl[1], "W", 11.5, "middle")
    T(f, e1[0] + xl[0], e1[1] + xl[1], "X", 11.5, "middle")
    dot_label(f, Yp, "Y", 7, 14)
    if arrow_q:
        f.vshift(Sl, Stl, f.px(arrow_q))
        ym = (f.y_at(Sl, f.px(arrow_q)) + f.y_at(Stl, f.px(arrow_q))) / 2
        T(f, f.px(arrow_q) + 8, ym + 4, tl, 12, "start", INK, halo=True)
    return f


TAXLEG = [("rect", AMB, "Tax burden on consumers"), ("rect", TEALF, "Tax burden on producers")]


@fig("fig-8-2")
def f82():
    D = (26, -0.2, 5, 100)
    S = (2, 0.2, 3, 95)
    kw = dict(xmax=100, ymax=30, t=6, tl="$6", xlabel="Quantity of fizzy drinks (000 cases)",
              ylabel="Price per case ($)", Stq=(3, 95), D=D, S=S)
    fa = tax_panel(mode="rev", title="(a) Producer revenue", **kw)
    fb = tax_panel(mode="tax", title="(b) Government tax revenue", **kw)
    fc = tax_panel(mode="burden", title="(c) The tax burden", **kw)

    def extra(m):
        legend(m, 90, 400, [("rect", TEALF, "Producer revenue after the tax (C x Q1)"),
                            ("rect", AMB, "Revenue lost because of the tax")])
        legend(m, 490, 400, [("rect", TEALF, "Tax revenue for government")])
        legend(m, 890, 400, TAXLEG)
    return assemble(1200, 440, [(fa, 0), (fb, 400), (fc, 800)], "Imposing a specific tax on fizzy drinks",
                    "Three panels: producer revenue, government tax revenue and the tax burden after a $6 specific tax shifts supply from S to S + tax.",
                    extra), \
        ("Figure 8.2: A $6 specific tax on fizzy drinks",
         "Three supply and demand panels for fizzy drinks: producer revenue falls, tax revenue is the rectangle between P1 and C, and the burden splits equally between consumers and producers.",
         "A $6 per-bottle tax shifts supply from S up to S + tax and moves the equilibrium from W (P<sub>e</sub> = $14, Q<sub>e</sub> = 60) to X (P<sub>1</sub> = $17, Q<sub>1</sub> = 45). In (a) producers keep only C = $11 per bottle, so revenue falls from the whole P<sub>e</sub> &times; Q<sub>e</sub> rectangle to the smaller C &times; Q<sub>1</sub> one. In (b) the government collects $6 &times; 45 = $270. In (c) that revenue splits into $3 borne by consumers (P<sub>e</sub> to P<sub>1</sub>) and $3 borne by producers (C to P<sub>e</sub>).")


@fig("fig-8-3")
def f83():
    f = tax_panel(D=(22, -0.1, 10, 100), S=(2, 0.3, 0, 90), t=8, mode="burden", ymax=32,
                  Stq=(0, 62), arrow_q=55, tl="$8", Wd=420, X0=78, X1=384, Y1=30,
                  xlabel="Quantity of concert tickets (000s)", ylabel="Price of concert tickets ($)")

    def extra(m):
        legend(m, 96, 396, TAXLEG)
    return assemble(420, 430, [(f, 0)], "Specific tax with elastic demand and inelastic supply",
                    "Flat demand and steep supply: a $8 tax moves the price only from $17 to $19, so producers bear most of it.", extra), \
        ("Figure 8.3: An $8 specific tax on concert tickets (PED greater than PES)",
         "Supply and demand for concert tickets with flat demand and steep supply; an $8 tax raises the price only from $17 to $19 so producers bear most of the burden.",
         "Demand for concert tickets is relatively elastic and supply (a fixed venue) relatively inelastic. An $8 specific tax moves the equilibrium from W (P<sub>e</sub> = $17, Q<sub>e</sub> = 50) to X (P<sub>1</sub> = $19, Q<sub>1</sub> = 30). Consumers bear only $2 per ticket (P<sub>e</sub> to P<sub>1</sub>) while producers bear $6 (C = $11 to P<sub>e</sub>), so the larger share of the tax falls on producers.")


@fig("fig-8-4")
def f84():
    f = tax_panel(D=(34, -0.4, 5, 80), S=(4, 0.1, 0, 100), t=10, mode="burden", ymax=34,
                  Stq=(0, 100), arrow_q=82, tl="$10", wl=(7, -9), xl=(7, -9), Wd=420, X0=78, X1=384, Y1=30,
                  xlabel="Quantity of petrol (million drums)", ylabel="Price of petrol ($ per drum)")

    def extra(m):
        legend(m, 96, 396, TAXLEG)
    return assemble(420, 430, [(f, 0)], "Specific tax with inelastic demand and elastic supply",
                    "Steep demand and flat supply: a $10 tax raises the price from $10 to $18, so consumers bear most of it.", extra), \
        ("Figure 8.4: A $10 specific tax on petrol (PED less than PES)",
         "Supply and demand for petrol with steep demand and flat supply; a $10 tax raises the price from $10 to $18 so consumers bear most of the burden.",
         "Demand for petrol is relatively inelastic and supply relatively elastic. A $10 specific tax moves the equilibrium from W (P<sub>e</sub> = $10, Q<sub>e</sub> = 60) to X (P<sub>1</sub> = $18, Q<sub>1</sub> = 40). Consumers bear $8 of the tax (P<sub>e</sub> to P<sub>1</sub>) and producers only $2 (C = $8 to P<sub>e</sub>), so the larger share falls on consumers.")


@fig("fig-8-5")
def f85():
    f = newf(100, 30)
    f.axes("Quantity supplied (systems per month)", "Price of home solar systems ($ 000s)")
    S = L(f, 6, 0.2, 5, 90)
    Ss = L(f, 2, 0.2, 5, 90)
    draw(f, S, RED)
    draw(f, Ss, RED)
    T(f, S[1][0] + 8, S[1][1] + 4, "S", 13, "start", RED)
    T(f, Ss[1][0] + 8, Ss[1][1] + 4, "S - subsidy", 13, "start", RED)
    for q in (28, 66):
        f.vshift(S, Ss, f.px(q))
        arrow_label(f, f.px(q), f.y_at(S, f.px(q)), f.y_at(Ss, f.px(q)), "$4,000")
    return f.svg("Effect of a specific subsidy on supply",
                 "Supply shifts down in parallel by $4,000 at every quantity, from S to S minus subsidy."), \
        ("Figure 8.5: A specific subsidy of $4,000 per home solar system",
         "Supply curve S and a parallel curve S minus subsidy lying $4,000 lower at every quantity, with two downward arrows.",
         "A specific subsidy of $4,000 per home solar system lowers the cost of supplying each system by the same amount, so the supply curve shifts vertically <em>down</em> by $4,000 at every quantity, from S to S &minus; subsidy. It is the mirror image of a specific tax.")


def sub_panel(mode, title):
    f = newf(100, 32, w=400, h=380, x0=70, y0=318, x1=350, y1=44)
    Dl = L(f, 30, -0.2, 5, 100)
    Sl = L(f, 8, 0.2, 5, 88)
    Ssl = L(f, 2, 0.2, 5, 88)
    e0 = f.intersect(Sl, Dl)      # W: original equilibrium
    e1 = f.intersect(Ssl, Dl)     # Z: new equilibrium
    X = (e1[0], f.y_at(Sl, e1[0]))  # producers receive at Q1
    Y0 = f.Y0

    def R(xa, xb, ya, yb, fill):
        poly(f, [(xa, ya), (xb, ya), (xb, yb), (xa, yb)], fill)
    if mode == "a":
        R(f.X0, e1[0], X[1], Y0, TEALF)
        R(f.X0, e0[0], e0[1], Y0, AMB)
    elif mode == "b":
        R(f.X0, e0[0], e0[1], e1[1], AMB)
        R(e0[0], e1[0], e1[1], Y0, TEALF)
    else:
        R(f.X0, e1[0], X[1], e1[1], TEALF)
    f.axes("Quantity supplied (systems)", "Price ($ 000s)")
    ptitle(f, title)
    f.guide(*e0, sb("Q", "e"), sb("P", "e"))
    f.guide(*e1, sb("Q", "1"), sb("P", "c"))
    f.guide(*X, None, sb("P", "p"), to_x=False)
    draw(f, Dl, GREY)
    draw(f, Sl, RED)
    draw(f, Ssl, RED)
    T(f, Dl[1][0] + 8, Dl[1][1] + 4, "D", 13, "start", GREY)
    T(f, Sl[1][0] + 8, Sl[1][1] + 4, "S", 13, "start", RED)
    T(f, Ssl[1][0] + 8, Ssl[1][1] + 4, "S - subsidy", 13, "start", RED)
    f.equilibrium(Sl, Dl, guides=False)
    f.equilibrium(Ssl, Dl, guides=False)
    f.dot(*X, 3.6, INK)
    T(f, e0[0], e0[1] - 9, "W", 11.5, "middle")
    T(f, e1[0], e1[1] - 9, "Z", 11.5, "middle")
    T(f, X[0], X[1] - 9, "X", 11.5, "middle")
    f.vshift(Sl, Ssl, f.px(80))
    arrow_label(f, f.px(80), f.y_at(Sl, f.px(80)), f.y_at(Ssl, f.px(80)), "$6,000")
    return f


@fig("fig-8-6")
def f86():
    fa = sub_panel("a", "(a) Increase in producer revenue")
    fb = sub_panel("b", "(b) Change in consumer expenditure")
    fc = sub_panel("c", "(c) Amount of government subsidy")

    def extra(m):
        legend(m, 90, 400, [("rect", AMB, "Producer revenue before the subsidy"),
                            ("rect", TEALF, "Increase in producer revenue")])
        legend(m, 490, 400, [("rect", AMB, "Saving on the original Qe units"),
                             ("rect", TEALF, "Extra spending on the additional units")])
        legend(m, 890, 400, [("rect", TEALF, "Cost of the subsidy to government")])
    return assemble(1200, 440, [(fa, 0), (fb, 400), (fc, 800)], "Granting a specific subsidy on home solar systems",
                    "Three panels: producer revenue, consumer expenditure and the government cost after a $6,000 subsidy shifts supply from S to S minus subsidy.",
                    extra), \
        ("Figure 8.6: A $6,000 specific subsidy on home solar systems",
         "Three supply and demand panels for home solar systems showing the rise in producer revenue, the split of consumer expenditure and the government cost of a $6,000 subsidy.",
         "A $6,000 per-system subsidy shifts supply from S down to S &minus; subsidy. The equilibrium moves from W (P<sub>e</sub> = $19,000, Q<sub>e</sub> = 55) to Z (P<sub>c</sub> = $16,000 paid by consumers, Q<sub>1</sub> = 70). Producers receive P<sub>p</sub> = $22,000 per system (the $16,000 plus the $6,000 subsidy). (a) Producer revenue rises from P<sub>e</sub> &times; Q<sub>e</sub> to P<sub>p</sub> &times; Q<sub>1</sub>. (b) Consumers save $3,000 on each of the original 55 systems but spend extra on the 15 additional systems. (c) The subsidy costs the government $6,000 &times; 70 = $420,000.")


def price_market(xmax=100, ymax=30, D=(26, -0.2, 5, 100), S=(2, 0.2, 5, 95), xl="", yl="", w=440):
    f = newf(xmax, ymax, w=w, h=380, x0=78, y0=318, x1=384, y1=30)
    return f, L(f, *D), L(f, *S)


def pline(f, p, label, above=False):
    y = f.py(p)
    xe = f.px(100)
    f.line(f.X0, y, xe, y, BLUE, 2.6)
    T(f, xe + 8, y - 2, label[0], 12, "start", BLUE, "600")
    T(f, xe + 8, y + 13, label[1], 12, "start", BLUE, "600")
    return y


@fig("fig-8-7")
def f87():
    f, D, S = price_market()
    f.axes("Quantity of rice (000 tonnes)", "Price of rice ($ per 10 kg bag)")
    pm = 10
    y = f.py(pm)
    draw(f, D, GREY)
    draw(f, S, RED)
    T(f, D[1][0] + 8, D[1][1] + 4, "D", 13, "start", GREY)
    T(f, S[1][0] + 8, S[1][1] + 4, "S", 13, "start", RED)
    e0 = f.equilibrium(S, D, sb("Q", "e"), sb("P", "e"))
    pline(f, pm, ("Maximum", "price"))
    f.ytick(y, sb("P", "max"))
    q1 = (f.x_at(S, y), y)
    q2 = (f.x_at(D, y), y)
    f.guide(q1[0], y, sb("Q", "1"), None, to_y=False)
    f.guide(q2[0], y, sb("Q", "2"), None, to_y=False)
    f.dot(*q1, 3.6, INK)
    f.dot(*q2, 3.6, INK)
    hbrace(f, q1[0] + 2, q2[0] - 2, y + 6, 7, True)
    T(f, (q1[0] + q2[0]) / 2, y + 36, "Excess demand", 12, "middle", INK, halo=True)
    return f.svg("Maximum price on rice",
                 "A price ceiling of $10 below the $14 equilibrium: quantity demanded 80 exceeds quantity supplied 40, leaving excess demand."), \
        ("Figure 8.7: A maximum price in the market for rice",
         "Supply and demand for rice with a price ceiling P max below equilibrium, showing quantity supplied Q1, equilibrium Qe and quantity demanded Q2 with an excess demand bracket.",
         "The free-market equilibrium for rice is at P<sub>e</sub> = $14 and Q<sub>e</sub> = 60 (000 tonnes). A maximum price P<sub>max</sub> = $10 is set below it. At that price producers supply only Q<sub>1</sub> = 40 while consumers demand Q<sub>2</sub> = 80, so there is excess demand (a shortage) of 40 thousand tonnes.")


@fig("fig-8-8")
def f88():
    f, D, S = price_market()
    f.axes("Quantity of rice (000 tonnes)", "Price of rice ($ per 10 kg bag)")
    pm = 10
    y = f.py(pm)
    S2 = L(f, -6, 0.2, 35, 106)
    draw(f, D, GREY)
    draw(f, S, RED)
    draw(f, S2, RED)
    T(f, D[1][0] + 8, D[1][1] + 4, "D", 13, "start", GREY)
    T(f, S[1][0] + 8, S[1][1] + 4, sb("S", "1"), 13, "start", RED)
    T(f, S2[1][0] + 8, S2[1][1] + 4, sb("S", "2"), 13, "start", RED)
    e0 = f.equilibrium(S, D, sb("Q", "e"), sb("P", "e"))
    pline(f, pm, ("Maximum", "price"))
    f.ytick(y, sb("P", "max"))
    q1 = (f.x_at(S, y), y)
    q3 = f.intersect(S2, D)
    assert abs(q3[1] - y) < 0.01
    f.guide(q1[0], y, sb("Q", "1"), None, to_y=False)
    f.guide(q3[0], y, sb("Q", "3"), None, to_y=False)
    f.dot(*q1, 3.6, INK)
    f.dot(*q3, 3.6, INK)
    f.hshift(S, S2, f.py(5))
    f.hshift(S, S2, f.py(15))
    return f.svg("Solving excess demand by shifting supply right",
                 "Supply shifts right from S1 to S2, which crosses demand exactly at the maximum price, so quantity demanded equals quantity supplied at Q3."), \
        ("Figure 8.8: Shifting supply to remove excess demand for rice",
         "Rice market where supply shifts right from S1 to S2 so that it meets demand at the maximum price, at quantity Q3, eliminating the shortage.",
         "With a maximum price P<sub>max</sub> = $10 the shortage is 40 thousand tonnes (Q<sub>1</sub> = 40 supplied, 80 demanded). If the government subsidises growers, sells stored rice or provides rice directly, supply shifts right from S<sub>1</sub> to S<sub>2</sub>. S<sub>2</sub> cuts demand exactly at P<sub>max</sub>, so Q<sub>3</sub> = 80 is both demanded and supplied and the shortage disappears.")


def pmin_market(w=440):
    f = newf(100, 30, w=w, h=380, x0=78, y0=318, x1=384, y1=30)
    D = L(f, 27, -0.3, 5, 85)
    S = L(f, 2, 0.2, 5, 95)
    return f, D, S


@fig("fig-8-9")
def f89():
    f, D, S = pmin_market()
    f.axes("Quantity of milk (million crates)", "Price of milk ($ per crate)")
    pm = 18
    y = f.py(pm)
    draw(f, D, GREY)
    draw(f, S, RED)
    T(f, D[1][0] + 8, D[1][1] + 4, "D", 13, "start", GREY)
    T(f, S[1][0] + 8, S[1][1] + 4, "S", 13, "start", RED)
    f.equilibrium(S, D, sb("Q", "e"), sb("P", "e"))
    pline(f, pm, ("Minimum", "price"))
    f.ytick(y, sb("P", "min"))
    q1 = (f.x_at(D, y), y)
    q2 = (f.x_at(S, y), y)
    f.guide(q1[0], y, sb("Q", "1"), None, to_y=False)
    f.guide(q2[0], y, sb("Q", "2"), None, to_y=False)
    f.dot(*q1, 3.6, INK)
    f.dot(*q2, 3.6, INK)
    hbrace(f, q1[0] + 2, q2[0] - 2, y - 6, 7, False)
    T(f, (q1[0] + q2[0]) / 2, y - 26, "Excess supply", 12, "middle")
    return f.svg("Minimum price on milk",
                 "A price floor of $18 above the $12 equilibrium: quantity supplied 80 exceeds quantity demanded 30, leaving excess supply."), \
        ("Figure 8.9: A minimum price in the market for milk",
         "Supply and demand for milk with a price floor P min above equilibrium, showing quantity demanded Q1, equilibrium Qe and quantity supplied Q2 with an excess supply bracket.",
         "The free-market equilibrium for milk is at P<sub>e</sub> = $12 and Q<sub>e</sub> = 50 (million litres). A minimum price P<sub>min</sub> = $18 is set above it. At that price consumers buy only Q<sub>1</sub> = 30 but farmers supply Q<sub>2</sub> = 80, so there is excess supply (a surplus) of 50 million litres.")


@fig("fig-8-10")
def f810():
    f, D, S = pmin_market(w=490)
    f.axes("Quantity of milk (million crates)", "Price of milk ($ per crate)")
    pm = 18
    y = f.py(pm)
    D2 = L(f, 42, -0.3, 50, 100)
    draw(f, D, GREY)
    draw(f, D2, GREY)
    draw(f, S, RED)
    T(f, D[1][0] + 8, D[1][1] + 4, "D", 13, "start", GREY)
    T(f, D2[1][0] + 8, D2[1][1] - 2, "D + government", 12, "start", GREY)
    T(f, D2[1][0] + 8, D2[1][1] + 12, "purchases", 12, "start", GREY)
    T(f, S[1][0] + 8, S[1][1] + 4, "S", 13, "start", RED)
    f.equilibrium(S, D, sb("Q", "e"), sb("P", "e"))
    pline(f, pm, ("Minimum", "price"))
    f.ytick(y, sb("P", "min"))
    q1 = (f.x_at(D, y), y)
    q2 = f.intersect(S, D2)
    assert abs(q2[1] - y) < 0.01
    f.guide(q1[0], y, sb("Q", "1"), None, to_y=False)
    f.guide(q2[0], y, sb("Q", "2"), None, to_y=False)
    f.dot(*q1, 3.6, INK)
    f.dot(*q2, 3.6, INK)
    hbrace(f, q1[0] + 2, q2[0] - 2, y - 6, 7, False)
    T(f, q1[0] + 62, y - 26, "Excess supply", 12, "middle")
    f.hshift(D, D2, f.py(14.5))
    f.hshift(D, D2, f.py(24.5))
    return f.svg("Solving excess supply with government buying",
                 "Government purchases shift demand right from D to D plus government purchases, which crosses supply exactly at the minimum price, so the whole quantity Q2 is bought."), \
        ("Figure 8.10: Government buying to remove excess supply of milk",
         "Milk market where government purchases shift demand right from D so that it meets supply at the minimum price, absorbing the surplus.",
         "With a minimum price P<sub>min</sub> = $18 there is a surplus of 50 million litres (Q<sub>1</sub> = 30 demanded, Q<sub>2</sub> = 80 supplied). If the government buys the surplus, total demand shifts right to D + government purchases, which cuts supply exactly at P<sub>min</sub>. All Q<sub>2</sub> = 80 million litres are now bought (30 by consumers, 50 by the government) and no surplus remains.")


@fig("fig-8-11")
def f811():
    f, D, S = pmin_market()
    f.axes("Quantity of milk (million crates)", "Price of milk ($ per crate)")
    pm = 18
    y = f.py(pm)
    draw(f, D, GREY)
    draw(f, S, RED)
    T(f, D[1][0] + 8, D[1][1] + 4, "D", 13, "start", GREY)
    T(f, S[1][0] + 8, S[1][1] + 4, "S", 13, "start", RED)
    f.equilibrium(S, D, sb("Q", "e"), sb("P", "e"))
    pline(f, pm, ("Minimum", "price"))
    f.ytick(y, sb("P", "min"))
    q1 = (f.x_at(D, y), y)
    q2 = (f.x_at(S, y), y)
    f.guide(q2[0], y, sb("Q", "2"), None, to_y=False)
    f.line(q1[0], f.Y0, q1[0], f.Y1 + 4, BLUE, 2.6)
    f.xtick(q1[0], sb("Q", "1"))
    T(f, q1[0], f.Y1 - 2, "Quota", 12, "middle", BLUE, "600")
    f.dot(*q1, 3.6, INK)
    f.dot(*q2, 3.6, INK)
    return f.svg("Quota to support a minimum price for milk",
                 "A vertical quota at Q1, the quantity demanded at the minimum price, keeps the price at P min without any surplus."), \
        ("Figure 8.11: A quota to maintain a minimum price for milk",
         "Milk market with a minimum price above equilibrium and a vertical quota line at Q1, the quantity demanded at that price.",
         "Instead of buying the surplus, the government limits output with a quota set at Q<sub>1</sub> = 30 million litres, the quantity consumers demand at P<sub>min</sub> = $18. Farmers would like to supply Q<sub>2</sub> = 80 at that price, but only Q<sub>1</sub> may legally be sold, so the price holds at P<sub>min</sub> with no surplus. Only the farms allowed to sell within the quota gain.")


# ------------------------------------------------------------ chapter 9


def ext_fig(w=470, xmax=100, ymax=36, x1=384):
    return newf(xmax, ymax, w=w, h=380, x0=78, y0=318, x1=x1, y1=30)


@fig("fig-9-1")
def f91():
    f = ext_fig(w=480, ymax=32)
    MSB = L(f, 28, -0.2, 0, 100)
    MSC = L(f, 4, 0.2, 0, 100)
    e = f.intersect(MSC, MSB)
    a = f.pt(0, 28)
    d = f.pt(0, 4)
    poly(f, [a, e, (f.X0, e[1])], AMB)
    poly(f, [(f.X0, e[1]), e, d], TEALF)
    f.axes("Quantity of bicycles (000s)", "Price ($)")
    draw(f, MSB, GREY)
    draw(f, MSC, RED)
    T(f, MSB[1][0] + 8, MSB[1][1] + 4, "MSB = D", 12.5, "start", GREY)
    T(f, MSC[1][0] + 8, MSC[1][1] + 4, "MSC = S", 12.5, "start", RED)
    f.equilibrium(MSC, MSB, "Q*", "P*")
    f.dot(*a, 3.4, INK)
    f.dot(*d, 3.4, INK)
    T(f, a[0] + 8, a[1] + 4, "a", 12)
    T(f, d[0] + 8, d[1] + 4, "d", 12)
    T(f, e[0], e[1] - 11, "c", 12, "middle")
    T(f, f.px(3), f.py(19.5), "Consumer surplus", 11.5)
    T(f, f.px(3), f.py(11.5), "Producer surplus", 11.5)
    T(f, f.px(38), f.py(30.5), "Community surplus", 11.5, "start", INK, "700")
    T(f, f.px(38), f.py(28.7), "= consumer surplus", 11.5)
    T(f, f.px(38), f.py(26.9), "+ producer surplus", 11.5)
    return f.svg("Social efficiency in the market for bicycles",
                 "MSB and MSC intersect at c; consumer surplus lies above the equilibrium price and producer surplus below it, together making community surplus."), \
        ("Figure 9.1: Social efficiency in the market for bicycles",
         "Downward MSB (demand) and upward MSC (supply) curves crossing at c, with consumer surplus shaded above P* and producer surplus shaded below it.",
         "With no externalities, demand is marginal social benefit (MSB) and supply is marginal social cost (MSC). They meet at c (P* = $16, Q* = 60 thousand bicycles). Consumer surplus is the triangle between MSB and P* (from a); producer surplus is the triangle between P* and MSC (down to d). Together they form community surplus, which is maximised where MSB = MSC.")


def gain_label(f, tri, text_pt, lines, target):
    for i, s in enumerate(lines):
        T(f, text_pt[0], text_pt[1] + i * 14, s, 11.5)


@fig("fig-9-2")
def f92():
    f = ext_fig(w=470, ymax=36)
    MSC = L(f, 4, 0.2, 5, 100)
    MPB = L(f, 26, -0.2, 5, 100)
    MSB = L(f, 34, -0.2, 5, 100)
    A = f.intersect(MSC, MPB)      # market
    B = f.intersect(MSC, MSB)      # social optimum
    top = (A[0], f.y_at(MSB, A[0]))
    poly(f, [top, A, B], GAIN)
    f.axes("Quantity of vaccines (000 doses)", "Price of vaccines ($ per dose)")
    f.guide(*A, sb("Q", "1"), sb("P", "1"))
    f.guide(*B, "Q*", "P*")
    draw(f, MPB, GREY)
    draw(f, MSB, GREY)
    draw(f, MSC, RED)
    T(f, MPB[1][0] + 8, MPB[1][1] + 4, "MPB = D", 12.5, "start", GREY)
    T(f, MSB[1][0] + 8, MSB[1][1] + 4, "MSB", 12.5, "start", GREY)
    T(f, MSC[1][0] + 8, MSC[1][1] + 4, "MSC = S", 12.5, "start", RED)
    f.dot(*A, 3.6, INK)
    f.dot(*B, 3.6, INK)
    x = f.px(22)
    dgap(f, x, f.y_at(MPB, x), f.y_at(MSB, x))
    ymid = (f.y_at(MPB, x) + f.y_at(MSB, x)) / 2
    T(f, x + 14, ymid + 6, "Positive", 12)
    T(f, x + 14, ymid + 20, "externality", 12)
    T(f, f.px(70), f.py(30), "Potential", 11.5, "start")
    T(f, f.px(70), f.py(30) + 14, "welfare gain", 11.5, "start")
    pointer(f, f.px(70) - 4, f.py(30) + 4, (A[0] + B[0]) / 2 + 3, (top[1] + A[1] + B[1]) / 3 - 1)
    return f.svg("Positive externality of consumption: vaccines",
                 "MSB lies above MPB by the external benefit; the market quantity Q1 is below the efficient quantity Q*, leaving a welfare gain triangle."), \
        ("Figure 9.2: A positive externality of consumption (vaccines)",
         "MPB (demand), MSB above it and MSC (supply) for vaccines, with market output Q1, efficient output Q* and a shaded potential welfare gain triangle.",
         "Vaccines protect other people as well as the person vaccinated, so marginal social benefit (MSB) lies $8 above marginal private benefit (MPB = D). The free market equilibrium is at P<sub>1</sub> = $15 and Q<sub>1</sub> = 55 thousand doses, but the socially efficient level, where MSB = MSC, is Q* = 75 at P* = $19. Output is too low, and the shaded triangle is the potential welfare gain from producing the extra doses.")


@fig("fig-9-3")
def f93():
    f = ext_fig(w=540, xmax=135, ymax=40, x1=440)
    MSC = L(f, 4, 0.2, 5, 115)
    MPB = L(f, 26, -0.2, 5, 105)
    MSB = L(f, 34, -0.2, 5, 130)
    MSCs = L(f, -4, 0.2, 25, 115)
    A = f.intersect(MSC, MPB)
    B = f.intersect(MSC, MSB)
    C = f.intersect(MSCs, MPB)
    top = (A[0], f.y_at(MSB, A[0]))
    poly(f, [top, A, B], GAIN)
    f.axes("Quantity of vaccines (000 doses)", "Price of vaccines ($ per dose)")
    f.guide(*A, sb("Q", "1"), sb("P", "1"))
    f.guide(*B, "Q*", "P*")
    f.guide(*C, None, sb("P", "2"), to_x=False)
    draw(f, MPB, GREY)
    draw(f, MSB, GREY)
    draw(f, MSC, RED)
    draw(f, MSCs, RED, "7 5")
    T(f, MPB[1][0] + 8, MPB[1][1] + 4, "MPB", 12.5, "start", GREY)
    T(f, MSB[1][0] + 8, MSB[1][1] + 4, "MSB", 12.5, "start", GREY)
    T(f, MSC[1][0] + 8, MSC[1][1] + 4, "MSC", 12.5, "start", RED)
    T(f, MSCs[1][0] + 8, MSCs[1][1] + 4, "MSC + subsidy", 12.5, "start", RED)
    for p in (A, B, C):
        f.dot(*p, 3.6, INK)
    x = f.px(96)
    f.vshift(MSC, MSCs, x)
    T(f, x + 9, (f.y_at(MSC, x) + f.y_at(MSCs, x)) / 2 + 4, "1", 13, "start", PURPLE, "700")
    y = f.py(8)
    f.hshift(MPB, MSB, y)
    T(f, (f.x_at(MPB, y) + f.x_at(MSB, y)) / 2, y - 9, "2", 13, "middle", PURPLE, "700")

    def extra(m):
        legend(m, 90, 396, [("num", "1", "Solution 1: a subsidy shifts MSC down to MSC + subsidy (price falls to P2)"),
                            ("num", "2", "Solution 2: an awareness campaign shifts MPB right towards MSB"),
                            ("rect", GAIN, "Potential welfare gain from raising output from Q1 to Q*")], gap=19)
    return assemble(540, 460, [(f, 0)], "Measures to promote vaccination",
                    "A subsidy shifts MSC down, or an awareness campaign shifts MPB right, so that output reaches the efficient quantity Q*.", extra), \
        ("Figure 9.3: Measures to promote vaccination (positive externality of consumption)",
         "Vaccine market showing a subsidy shifting MSC down to MSC plus subsidy and a campaign shifting MPB right, both reaching Q*.",
         "Starting from Figure 9.2, two policies push output from Q<sub>1</sub> = 55 up to the efficient Q* = 75 thousand doses. <strong>1. Subsidy:</strong> an $8 per-dose subsidy shifts supply down to MSC + subsidy, which cuts MPB at Q*, so patients pay only P<sub>2</sub> = $11 (below P<sub>1</sub> = $15). <strong>2. Awareness campaign:</strong> raises private valuation, shifting MPB to the right towards MSB so it now meets the original MSC at Q*.")


@fig("fig-9-4")
def f94():
    f = ext_fig(w=470)
    MPC = L(f, 14, 0.2, 5, 85)
    MSC = L(f, 6, 0.2, 5, 100)
    MSB = L(f, 30, -0.2, 5, 100)
    A = f.intersect(MPC, MSB)
    B = f.intersect(MSC, MSB)
    below = (A[0], f.y_at(MSC, A[0]))
    poly(f, [A, below, B], GAIN)
    f.axes("Quantity of honey (000 jars)", "Price of honey ($ per jar)")
    f.guide(*A, sb("Q", "1"), sb("P", "1"))
    f.guide(*B, "Q*", "P*")
    draw(f, MPC, RED)
    draw(f, MSC, RED)
    draw(f, MSB, GREY)
    T(f, MPC[1][0] + 8, MPC[1][1] + 4, "MPC = S", 12.5, "start", RED)
    T(f, MSC[1][0] + 8, MSC[1][1] + 4, "MSC", 12.5, "start", RED)
    T(f, MSB[1][0] + 8, MSB[1][1] + 4, "MSB = D", 12.5, "start", GREY)
    f.dot(*A, 3.6, INK)
    f.dot(*B, 3.6, INK)
    T(f, B[0], B[1] - 10, "a", 12, "middle")
    x = f.px(85)
    dgap(f, x, f.y_at(MPC, x), f.y_at(MSC, x))
    T(f, x - 8, f.y_at(MPC, x) - 10, "Positive externality", 12, "end")
    T(f, f.px(66), f.py(7.5), "Potential", 11.5, "start")
    T(f, f.px(66), f.py(7.5) + 14, "welfare gain", 11.5, "start")
    pointer(f, f.px(66) + 14, f.py(7.5) - 14, f.px(48), f.py(17.6))
    return f.svg("Positive externality of production: honey",
                 "MSC lies below MPC by the external benefit of pollination; the market quantity Q1 is below the efficient quantity Q*, leaving a welfare gain triangle."), \
        ("Figure 9.4: A positive externality of production (honey and pollination)",
         "MPC (supply), MSC below it and MSB (demand) for honey, with market output Q1, efficient output Q* and a shaded potential welfare gain triangle.",
         "Beekeepers' hives pollinate neighbouring orchards, so the true marginal social cost (MSC) of honey is $8 below the beekeepers' private cost (MPC = S). The market equilibrium is at P<sub>1</sub> = $22 and Q<sub>1</sub> = 40 thousand jars, but efficiency requires MSB = MSC at Q* = 60 and P* = $18. Output is too low and the shaded triangle shows the potential welfare gain.")


@fig("fig-9-5")
def f95():
    f = ext_fig(w=470)
    MPB = L(f, 32, -0.2, 5, 100)
    MSB = L(f, 24, -0.2, 5, 100)
    MSC = L(f, 4, 0.2, 5, 100)
    A = f.intersect(MSC, MPB)      # market
    B = f.intersect(MSC, MSB)      # efficient
    low = (A[0], f.y_at(MSB, A[0]))
    poly(f, [B, A, low], LOSS)
    f.axes("Quantity of e-cigarettes (million packs)", "Price of e-cigarettes ($ per pack)")
    f.guide(*A, sb("Q", "1"), sb("P", "1"))
    f.guide(*B, "Q*", "P*")
    draw(f, MPB, GREY)
    draw(f, MSB, GREY)
    draw(f, MSC, RED)
    T(f, MPB[1][0] + 8, MPB[1][1] + 4, "MPB = D", 12.5, "start", GREY)
    T(f, MSB[1][0] + 8, MSB[1][1] + 4, "MSB", 12.5, "start", GREY)
    T(f, MSC[1][0] + 8, MSC[1][1] + 4, "MSC = S", 12.5, "start", RED)
    f.dot(*A, 3.6, INK)
    f.dot(*B, 3.6, INK)
    x = f.px(20)
    dgap(f, x, f.y_at(MPB, x), f.y_at(MSB, x))
    T(f, x + 10, (f.y_at(MPB, x) + f.y_at(MSB, x)) / 2 + 2, "Negative", 12)
    T(f, x + 10, (f.y_at(MPB, x) + f.y_at(MSB, x)) / 2 + 16, "externality", 12)
    T(f, f.px(83), f.py(17.6), "Welfare loss", 11.5)
    pointer(f, f.px(83) - 3, f.py(17.6) - 4, f.px(67), f.py(14.6))
    return f.svg("Negative externality of consumption: e-cigarettes",
                 "MSB lies below MPB by the external cost; the market quantity Q1 exceeds the efficient quantity Q*, leaving a welfare loss triangle."), \
        ("Figure 9.5: A negative externality of consumption (e-cigarettes)",
         "MPB (demand) with MSB below it and MSC (supply) for e-cigarettes, with market output Q1 above efficient output Q* and a shaded welfare loss triangle.",
         "Vaping harms bystanders, so marginal social benefit (MSB) lies $8 below marginal private benefit (MPB = D). The market equilibrium is at P<sub>1</sub> = $18 and Q<sub>1</sub> = 70 million packs, but the efficient level, where MSB = MSC, is Q* = 50 at P* = $14. Too much is consumed, and the shaded triangle is the welfare loss.")


@fig("fig-9-6")
def f96():
    f = ext_fig(w=540, ymax=36, x1=430)
    MPB = L(f, 32, -0.2, 5, 100)
    MSB = L(f, 24, -0.2, 5, 100)
    MSC = L(f, 4, 0.2, 5, 100)
    MSCt = L(f, 12, 0.2, 5, 95)
    A = f.intersect(MSC, MPB)      # market
    B = f.intersect(MSC, MSB)      # efficient
    Bt = f.intersect(MSCt, MPB)    # after tax
    low = (A[0], f.y_at(MSB, A[0]))
    rect(f, 0, 14, 50, 22, AMB)
    poly(f, [B, A, low], LOSS)
    f.axes("Quantity of e-cigarettes (million packs)", "Price of e-cigarettes ($ per pack)")
    f.guide(*A, sb("Q", "1"), sb("P", "1"))
    f.guide(*B, "Q*", "P*")
    f.guide(*Bt, None, sb("P", "t"), to_x=False)
    draw(f, MPB, GREY)
    draw(f, MSB, GREY)
    draw(f, MSC, RED)
    draw(f, MSCt, RED, "7 5")
    T(f, MPB[1][0] + 8, MPB[1][1] + 4, "MPB", 12.5, "start", GREY)
    T(f, MSB[1][0] + 8, MSB[1][1] + 4, "MSB", 12.5, "start", GREY)
    T(f, MSC[1][0] + 8, MSC[1][1] + 4, "MSC", 12.5, "start", RED)
    T(f, MSCt[1][0] + 8, MSCt[1][1] + 4, "MSC + tax", 12.5, "start", RED)
    for p in (A, B, Bt):
        f.dot(*p, 3.6, INK)
    x = f.px(86)
    f.vshift(MSC, MSCt, x)
    T(f, x + 9, (f.y_at(MSC, x) + f.y_at(MSCt, x)) / 2 + 4, "1", 13, "start", PURPLE, "700")
    y = f.py(20)
    f.hshift(MPB, MSB, y)
    T(f, (f.x_at(MPB, y) + f.x_at(MSB, y)) / 2, y - 9, "2", 13, "middle", PURPLE, "700")

    def extra(m):
        legend(m, 90, 396, [("num", "1", "Solution 1: a tax of $8 per pack shifts MSC up to MSC + tax"),
                            ("num", "2", "Solution 2: an anti-vaping campaign shifts MPB left towards MSB"),
                            ("rect", AMB, "Tax revenue ($8 x Q*)"),
                            ("rect", LOSS, "Welfare loss removed if output falls to Q*")], gap=19)
    return assemble(540, 480, [(f, 0)], "Measures to reduce e-cigarette consumption",
                    "A per-unit tax shifts MSC up, or a campaign shifts MPB left, so that output falls to the efficient quantity Q*.", extra), \
        ("Figure 9.6: Measures to reduce consumption of e-cigarettes (negative externality)",
         "E-cigarette market showing a tax shifting MSC up to MSC plus tax and a campaign shifting MPB left, both reaching Q*.",
         "Starting from Figure 9.5, two policies cut output from Q<sub>1</sub> = 70 to the efficient Q* = 50 million packs. <strong>1. Tax:</strong> an $8 per-pack tax shifts supply up to MSC + tax, which cuts MPB at Q*; consumers now pay P<sub>t</sub> = $22 (above P<sub>1</sub> = $18) and the government collects $8 &times; 50 = $400 million. <strong>2. Campaign:</strong> reduces private demand, shifting MPB left towards MSB so it meets the original MSC at Q*.")


@fig("fig-9-7")
def f97():
    f = ext_fig(w=470)
    MSC = L(f, 10, 0.2, 5, 90)
    MPC = L(f, 2, 0.2, 5, 100)
    MSB = L(f, 30, -0.2, 5, 100)
    A = f.intersect(MPC, MSB)      # market
    B = f.intersect(MSC, MSB)      # efficient
    up = (A[0], f.y_at(MSC, A[0]))
    poly(f, [B, A, up], LOSS)
    f.axes("Quantity of cement (million tonnes)", "Price of cement ($ per bag)")
    f.guide(*A, sb("Q", "1"), sb("P", "1"))
    f.guide(*B, "Q*", "P*")
    draw(f, MSC, RED)
    draw(f, MPC, RED)
    draw(f, MSB, GREY)
    T(f, MSC[1][0] + 8, MSC[1][1] + 4, "MSC", 12.5, "start", RED)
    T(f, MPC[1][0] + 8, MPC[1][1] + 4, "MPC = S", 12.5, "start", RED)
    T(f, MSB[1][0] + 8, MSB[1][1] + 4, "MSB = D", 12.5, "start", GREY)
    f.dot(*A, 3.6, INK)
    f.dot(*B, 3.6, INK)
    T(f, B[0], B[1] - 10, "a", 12, "middle")
    x = f.px(22)
    dgap(f, x, f.y_at(MSC, x), f.y_at(MPC, x))
    T(f, x - 8, f.py(3.9), "Negative", 12)
    T(f, x - 8, f.py(3.9) + 14, "externality", 12)
    T(f, f.px(56), f.py(32), "Welfare loss", 11.5)
    pointer(f, f.px(64), f.py(32) + 5, f.px(63.3), f.py(20.6))
    return f.svg("Negative externality of production: cement",
                 "MSC lies above MPC by the external cost; the market quantity Q1 exceeds the efficient quantity Q*, leaving a welfare loss triangle."), \
        ("Figure 9.7: A negative externality of production (cement)",
         "MSC above MPC (supply) and MSB (demand) for cement, with market output Q1 above efficient output Q* and a shaded welfare loss triangle.",
         "Cement kilns pollute the air, so marginal social cost (MSC) lies $8 above the producers' private cost (MPC = S). The market equilibrium is at P<sub>1</sub> = $16 and Q<sub>1</sub> = 70 million tonnes, but the efficient level, where MSB = MSC, is Q* = 50 at P* = $20. Too much is produced, and the shaded triangle is the welfare loss.")


@fig("fig-9-8")
def f98():
    f = ext_fig(w=540, x1=430)
    MSC = L(f, 14, 0.2, 5, 90)
    MPCt = L(f, 8, 0.2, 5, 95)
    MPC = L(f, 2, 0.2, 5, 100)
    MSB = L(f, 30, -0.2, 5, 100)
    A = f.intersect(MPC, MSB)      # before tax
    Bt = f.intersect(MPCt, MSB)    # after tax
    C = f.intersect(MSC, MSB)      # efficient
    up = (Bt[0], f.y_at(MSC, Bt[0]))
    poly(f, [C, Bt, up], LOSS)
    f.axes("Quantity of steel (million tonnes)", "Price of steel ($ 00s per tonne)")
    for p, xl, yl in ((A, sb("Q", "1"), sb("P", "1")), (Bt, sb("Q", "2"), sb("P", "2")), (C, "Q*", "P*")):
        f.guide(*p, xl, yl)
    draw(f, MSC, RED)
    draw(f, MPCt, RED, "7 5")
    draw(f, MPC, RED)
    draw(f, MSB, GREY)
    T(f, MSC[1][0] + 8, MSC[1][1] + 4, "MSC", 12.5, "start", RED)
    T(f, MPCt[1][0] + 8, MPCt[1][1] + 4, "MPC + carbon tax", 12.5, "start", RED)
    T(f, MPC[1][0] + 8, MPC[1][1] + 4, "MPC", 12.5, "start", RED)
    T(f, MSB[1][0] + 8, MSB[1][1] + 4, "MSB = D", 12.5, "start", GREY)
    for p in (A, Bt, C):
        f.dot(*p, 3.6, INK)
    x = f.px(84)
    f.vshift(MPC, MPCt, x)
    T(f, x + 9, (f.y_at(MPC, x) + f.y_at(MPCt, x)) / 2 + 4, "$600", 12)
    ya = f.Y0 - 14
    f.arrow(A[0] - 4, ya, Bt[0] + 4, ya, PURPLE)
    T(f, f.px(18), f.py(34), "Remaining", 11.5)
    T(f, f.px(18), f.py(34) + 14, "welfare loss", 11.5)
    pointer(f, f.px(34), f.py(34) + 20, f.px(50), f.py(22.6))
    return f.svg("Effect of a carbon tax on steel",
                 "A $600 per tonne carbon tax shifts private marginal cost up from MPC to MPC plus carbon tax, cutting output from Q1 to Q2, but the tax is below the full external cost so output Q2 still exceeds Q* and a welfare loss triangle remains."), \
        ("Figure 9.8: A carbon tax on steel",
         "Steel market with MPC, MPC plus carbon tax, MSC and MSB, showing output falling from Q1 to Q2 but staying above Q*, with a smaller welfare loss triangle left.",
         "Steelmaking emits CO<sub>2</sub>, so MSC lies $1,200 per tonne above MPC. Without intervention the market produces Q<sub>1</sub> = 70 million tonnes at P<sub>1</sub> = $1,600. A carbon tax of $600 per tonne shifts private cost up to MPC + carbon tax, reducing output to Q<sub>2</sub> = 55 at P<sub>2</sub> = $1,900. Because the tax is only half the external cost, Q<sub>2</sub> is still above the efficient Q* = 40 (P* = $2,200), so a smaller welfare loss triangle remains.")


# ------------------------------------------------------------------ main

if __name__ == "__main__":
    want = sys.argv[1:] or list(FIGS)
    for name in want:
        out = FIGS[name]()
        svg, (label, alt, cap) = out
        save(name, svg, label, alt, cap)
        print("wrote", name)
