"""Original vector figures for chapters 25, 26, 27, 29 and 30 (own coordinates,
own examples).  Built on tools/figlib.py (not modified).

Every dot is computed with Fig.intersect()/equilibrium(), guides and ticks come
from the data scale, and shift arrows span old curve to new curve at equal height.
"""
import os, sys, json, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import *

OUT = "/Users/davidbukraba/Desktop/IB WEBSITE/assets/figures-original"
os.makedirs(OUT, exist_ok=True)

BOXFILL = "#fdeaea"
TEALFILL = "#e6f5f7"
LIGHTRED = "#f8d3cd"
LIGHTTEAL = "#c9edf1"
LIGHTBLUE = "#cfe6f5"


def save(fid, fig, label, alt, caption):
    title = label.split(": ", 1)[-1]
    open(f"{OUT}/{fid}.svg", "w").write(fig.svg(title, alt))
    with open(f"{OUT}/{fid}.json", "w") as fh:
        json.dump({"label": label, "alt": alt, "caption": caption}, fh, indent=1)
    print("saved", fid)


# ----------------------------------------------------------------- helpers
def halo(f, x, y, s, size=11.5, anchor="middle", color=INK, weight="400", rotate=None):
    tr = f' transform="rotate({rotate} {x:.1f} {y:.1f})"' if rotate is not None else ""
    f.add(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" text-anchor="{anchor}" '
          f'fill="{color}" font-weight="{weight}" stroke="#ffffff" stroke-width="4" '
          f'paint-order="stroke" stroke-linejoin="round"{tr}>{s}</text>')


def rbox(f, x, y, w, h, lines, fill=BOXFILL, stroke=RED, size=12, weight="600",
         color=INK, rx=8, sw=2.0):
    f.add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" '
          f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')
    if isinstance(lines, str):
        lines = [lines]
    lh = size * 1.28
    y0 = y + h / 2 - lh * (len(lines) - 1) / 2 + size * 0.35
    for i, s in enumerate(lines):
        f.text(x + w / 2, y0 + i * lh, s, size, "middle", color, weight)


def edge(cx, cy, w, h, tx, ty, gap=0.0):
    """Point on the boundary of the w x h box centred (cx,cy) in the direction of
    (tx,ty), pushed out by gap."""
    dx, dy = tx - cx, ty - cy
    n = math.hypot(dx, dy)
    ux, uy = dx / n, dy / n
    t = min((w / 2) / abs(dx) if dx else 1e9, (h / 2) / abs(dy) if dy else 1e9)
    return (cx + dx * t + ux * gap, cy + dy * t + uy * gap)


def link(f, a, b, color=RED, width=2.2, gap=4, head=8):
    """Arrow between two boxes a=(cx,cy,w,h), b=(cx,cy,w,h), edge to edge."""
    p = edge(a[0], a[1], a[2], a[3], b[0], b[1], gap)
    q = edge(b[0], b[1], b[2], b[3], a[0], a[1], gap)
    f.arrow(p[0], p[1], q[0], q[1], color, width, head)


def cedge(cx, cy, r, tx, ty, gap=0.0):
    dx, dy = tx - cx, ty - cy
    n = math.hypot(dx, dy)
    return (cx + dx / n * (r + gap), cy + dy / n * (r + gap))


def node(f, cx, cy, s, r=30, fill=BOXFILL, stroke=RED):
    f.add(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="2.4"/>')
    f.text(cx, cy - 2, "Country", 11, "middle", INK, "400")
    f.text(cx, cy + 14, s, 15, "middle", INK, "700")


def bidir(f, p, q, color=TEAL, width=2.2, head=8, gap=4):
    dx, dy = q[0] - p[0], q[1] - p[1]
    n = math.hypot(dx, dy)
    ux, uy = dx / n, dy / n
    a = (p[0] + ux * gap, p[1] + uy * gap)
    b = (q[0] - ux * gap, q[1] - uy * gap)
    f.line(a[0] + ux * head * .6, a[1] + uy * head * .6,
           b[0] - ux * head * .6, b[1] - uy * head * .6, color, width)
    ang = math.degrees(math.atan2(dy, dx))
    f.arrowhead(b[0], b[1], ang, color, head)
    f.arrowhead(a[0], a[1], ang + 180, color, head)


def circ(f, x, y, n, r=8):
    f.dot(x, y, r, INK)
    f.text(x, y + 4, str(n), 11, "middle", "#ffffff", "700")


def dline(f, q1, p1, q2, p2):
    return (f.pt(q1, p1), f.pt(q2, p2))


def draw(f, l, color, width=2.8):
    f.line(*l[0], *l[1], color, width)


def hline(f, p, q1, q2):
    return (f.pt(q1, p), f.pt(q2, p))


def poly(f, pts, fill):
    d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts) + " Z"
    f.path(d, color="none", width=0, fill=fill)


# =============================================================== CHAPTER 25
def fig_25_1():
    f = Fig(w=500, h=380)
    f.add(f'<rect x="18" y="22" width="238" height="336" rx="30" fill="{TEALFILL}" '
          f'stroke="{TEAL}" stroke-width="2" stroke-dasharray="7 5"/>')
    A, B, C, D = (100, 90), (100, 290), (200, 190), (410, 190)
    R = 30
    for p, s in ((A, "A"), (B, "B"), (C, "C")):
        node(f, p[0], p[1], s, R)
    node(f, D[0], D[1], "D", R, fill="#f0f0f0", stroke=GREY)
    # free trade inside the area
    for p, q in ((A, B), (A, C), (B, C)):
        a = cedge(p[0], p[1], R, q[0], q[1], 0)
        b = cedge(q[0], q[1], R, p[0], p[1], 0)
        bidir(f, a, b, TEAL)
    f.text(125, 187, "FREE-TRADE", 11.5, "middle", TEAL, "700")
    f.text(125, 202, "AREA", 11.5, "middle", TEAL, "700")
    # A -> D : complete embargo (dashed, ends in a barrier bar)
    a = cedge(A[0], A[1], R, D[0], D[1], 5)
    ang = math.atan2(D[1] - A[1], D[0] - A[0])
    e = cedge(D[0], D[1], R, A[0], A[1], 12)
    f.line(a[0], a[1], e[0], e[1], RED, 2.2, "7 5", "butt")
    nx, ny = -math.sin(ang), math.cos(ang)
    f.line(e[0] + nx * 10, e[1] + ny * 10, e[0] - nx * 10, e[1] - ny * 10, RED, 4)
    halo(f, 330, 137, "Complete embargo", 11.5, "middle", RED, "600",
         rotate=round(math.degrees(ang), 1))
    # C <-> D free trade
    bidir(f, cedge(C[0], C[1], R, D[0], D[1], 0), cedge(D[0], D[1], R, C[0], C[1], 0), TEAL)
    halo(f, 313, 178, "Free trade", 11.5, "middle", TEAL, "600")
    # B -> D tariffs (D's exports pass a toll mark near B's side)
    b0 = cedge(B[0], B[1], R, D[0], D[1], 5)
    d0 = cedge(D[0], D[1], R, B[0], B[1], 5)
    f.line(b0[0], b0[1], d0[0], d0[1], INK, 2.2)
    f.arrowhead(b0[0] + 0, b0[1] + 0, math.degrees(math.atan2(B[1] - D[1], B[0] - D[0])) , INK, 8)
    angb = math.atan2(D[1] - B[1], D[0] - B[0])
    # toll bar
    m = (b0[0] + 0.30 * (d0[0] - b0[0]), b0[1] + 0.30 * (d0[1] - b0[1]))
    nbx, nby = -math.sin(angb), math.cos(angb)
    f.line(m[0] + nbx * 9, m[1] + nby * 9, m[0] - nbx * 9, m[1] - nby * 9, PURPLE, 4)
    halo(f, 335, 246, "Tariffs on D&rsquo;s goods", 11.5, "middle", PURPLE, "600",
         rotate=round(math.degrees(angb), 1))
    f.text(387, 252, "", 1)
    save("fig-25-1", f, "Figure 25.1: A free-trade area",
         "Countries A, B and C linked by two-way free-trade arrows inside a shaded free-trade area; outside country D faces a complete embargo from A, tariffs from B and free trade with C.",
         "Countries A, B and C trade freely with one another, but each sets its own policy towards outsider D: A bans trade with D completely (embargo), B taxes D&rsquo;s goods with tariffs, and C trades freely with D. There is no common external policy.")


def fig_25_2():
    f = Fig(w=500, h=380)
    X_R = 262
    f.add(f'<rect x="18" y="22" width="{X_R-18}" height="336" rx="30" fill="{TEALFILL}" '
          f'stroke="{RED}" stroke-width="5"/>')
    A, B, C, D = (100, 90), (100, 290), (200, 190), (420, 190)
    R = 30
    for p, s in ((A, "A"), (B, "B"), (C, "C")):
        node(f, p[0], p[1], s, R)
    node(f, D[0], D[1], "D", R, fill="#f0f0f0", stroke=GREY)
    for p, q in ((A, B), (A, C), (B, C)):
        bidir(f, cedge(p[0], p[1], R, q[0], q[1], 0), cedge(q[0], q[1], R, p[0], p[1], 0), TEAL)
    f.text(125, 187, "FREE", 11.5, "middle", TEAL, "700")
    f.text(125, 202, "TRADE", 11.5, "middle", TEAL, "700")
    f.text(137, 46, "CUSTOMS UNION", 12.5, "middle", RED, "700")
    for T in (A, B, C):
        s = cedge(D[0], D[1], R, T[0], T[1], 5)
        e = cedge(T[0], T[1], R, D[0], D[1], 5)
        f.line(s[0], s[1], e[0] + 0, e[1] + 0, INK, 2.2)
        ang = math.degrees(math.atan2(T[1] - D[1], T[0] - D[0]))
        f.arrowhead(e[0], e[1], ang, INK, 8)
        # crossing point on the union boundary
        t = (X_R - s[0]) / (e[0] - s[0])
        cx, cy = s[0] + t * (e[0] - s[0]), s[1] + t * (e[1] - s[1])
        f.dot(cx, cy, 5.5, "#ffffff")
        f.add(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="5.5" fill="#ffffff" stroke="{RED}" stroke-width="2.4"/>')
    halo(f, 350, 105, "Common external", 11.5, "middle", RED, "600")
    halo(f, 350, 120, "tariff on D&rsquo;s goods", 11.5, "middle", RED, "600")
    halo(f, 350, 274, "Same tariff at every", 11.5, "middle", RED, "600")
    halo(f, 350, 289, "point of entry", 11.5, "middle", RED, "600")
    save("fig-25-2", f, "Figure 25.2: A customs union",
         "Countries A, B and C inside a boundary marked as the common external tariff, trading freely with each other; goods from outsider D face the same tariff at every entry point.",
         "Countries A, B and C trade freely inside the union, and all three apply the same common external tariff (red boundary) to goods from D, whichever member they enter through.")


def trade_diagram(kind):
    """kind 'creation' or 'diversion'. Own numbers."""
    f = Fig(w=430, h=380).scale(190, 44 if kind == "creation" else 40)
    if kind == "creation":
        f.axes("Quantity of ceramic tiles (million m&#178;)", "Price of ceramic tiles (euros per m&#178;)")
        sd = dict(a=4, b=0.2)
        Sdom = lambda q: 4 + 0.2 * q
        Dm = lambda q: 40 - 0.2 * q
        Pw, Pt = 12, 20
        l_S = dline(f, 0, Sdom(0), 160, Sdom(160))
        l_D = dline(f, 0, Dm(0), 170, Dm(170))
        draw(f, l_S, RED)
        draw(f, l_D, GREY)
        l_w = hline(f, Pw, 0, 168)
        l_t = hline(f, Pt, 0, 168)
        draw(f, l_w, RED)
        draw(f, l_t, RED)
        # intersections (exact, on both curves)
        pts = {}
        pts["Q1"] = f.intersect(l_S, l_w)
        pts["Q2"] = f.intersect(l_S, l_t)
        pts["Q3"] = f.intersect(l_D, l_t)
        pts["Q4"] = f.intersect(l_D, l_w)
        for k, (la, lb) in {"Q1": (l_S, l_w), "Q2": (l_S, l_t), "Q3": (l_D, l_t), "Q4": (l_D, l_w)}.items():
            assert abs(f.y_at(la, pts[k][0]) - pts[k][1]) < .01 and abs(f.y_at(lb, pts[k][0]) - pts[k][1]) < .01
        # shaded triangles first (under labels)
        poly(f, [pts["Q1"], (pts["Q2"][0], pts["Q1"][1]), pts["Q2"]], LIGHTRED)
        poly(f, [pts["Q3"], (pts["Q3"][0], pts["Q4"][1]), pts["Q4"]], LIGHTTEAL)
        # redraw the curves over the fills
        draw(f, l_S, RED); draw(f, l_D, GREY); draw(f, l_w, RED); draw(f, l_t, RED)
        for k in ("Q1", "Q2", "Q3", "Q4"):
            f.guide(pts[k][0], pts[k][1], k[0] + sub("", k[1]), None, to_y=False)
            f.dot(*pts[k], 3.6, INK)
        f.ytick(f.py(Pw), "P" + sub("", "w"))
        f.ytick(f.py(Pt), "P" + sub("", "w+t"))
        f.label(f.px(160) + 6, f.py(Sdom(160)) - 4, "S (Polish)", RED, 12)
        f.label(f.px(170) + 6, f.py(Dm(170)) + 14, "D (Polish)", GREY, 12)
        f.label(f.px(168) + 6, f.py(Pt) + 4, "S (Spanish)+tariff", RED, 11.5)
        f.label(f.px(168) + 6, f.py(Pw) + 4, "S (Spanish)", RED, 11.5)
        # labels with leaders
        f.text(140, 62, "Regained world", 11.5, "middle")
        f.text(140, 76, "efficiency", 11.5, "middle")
        tgt1 = f.pt(70, 14.6)
        assert tgt1[0] < f.px(80) and f.py(14.6) < f.py(12) and f.y_at(l_S, tgt1[0]) < tgt1[1]
        f.arrow(140, 82, tgt1[0], tgt1[1], PURPLE, 1.6, 7)
        f.text(272, 62, "Regained consumer", 11.5, "middle")
        f.text(272, 76, "surplus", 11.5, "middle")
        tgt2 = f.pt(110, 14.4)
        assert tgt2[0] > f.px(100) and f.y_at(l_D, tgt2[0]) < tgt2[1]
        f.arrow(272, 82, tgt2[0], tgt2[1], PURPLE, 1.6, 7)
    else:
        f.axes("Quantity of footwear (million pairs)", "Price of footwear (US$ per pair)")
        Sdom = lambda q: 4 + 0.2 * q
        Dm = lambda q: 36 - 0.2 * q
        Pv, Pb, Pvt = 10, 16, 22
        l_S = dline(f, 0, Sdom(0), 150, Sdom(150))
        l_D = dline(f, 0, Dm(0), 150, Dm(150))
        l_v = hline(f, Pv, 0, 158)
        l_b = hline(f, Pb, 0, 158)
        l_t = hline(f, Pvt, 0, 158)
        P = {}
        P["Q1"] = f.intersect(l_S, l_v)
        P["Q2"] = f.intersect(l_S, l_b)
        P["Q3"] = f.intersect(l_D, l_b)
        P["Q4"] = f.intersect(l_D, l_v)
        for k, (la, lb) in {"Q1": (l_S, l_v), "Q2": (l_S, l_b), "Q3": (l_D, l_b), "Q4": (l_D, l_v)}.items():
            assert abs(f.y_at(la, P[k][0]) - P[k][1]) < .01 and abs(f.y_at(lb, P[k][0]) - P[k][1]) < .01
        poly(f, [P["Q1"], (P["Q2"][0], P["Q1"][1]), P["Q2"]], LIGHTRED)
        poly(f, [P["Q3"], (P["Q3"][0], P["Q4"][1]), P["Q4"]], LIGHTTEAL)
        poly(f, [(P["Q2"][0], P["Q1"][1]), P["Q2"], P["Q3"], (P["Q3"][0], P["Q4"][1])], LIGHTBLUE)
        draw(f, l_S, RED); draw(f, l_D, GREY)
        draw(f, l_v, RED); draw(f, l_b, RED); draw(f, l_t, RED)
        for k in ("Q1", "Q2", "Q3", "Q4"):
            f.guide(P[k][0], P[k][1], k[0] + sub("", k[1]), None, to_y=False)
            f.dot(*P[k], 3.6, INK)
        f.ytick(f.py(Pv), "P" + sub("", "V"))
        f.ytick(f.py(Pb), "P" + sub("", "B"))
        f.ytick(f.py(Pvt), "P" + sub("", "V+t"))
        f.label(f.px(150) + 6, f.py(Sdom(150)) - 4, "S (Chilean)", RED, 12)
        f.label(f.px(150) + 6, f.py(Dm(150)) + 14, "D (Chilean)", GREY, 12)
        f.label(f.px(158) + 6, f.py(Pvt) + 4, "S (Vietnamese)+tariff", RED, 11)
        f.label(f.px(158) + 6, f.py(Pb) + 4, "S (Brazilian)", RED, 11.5)
        f.label(f.px(158) + 6, f.py(Pv) + 4, "S (Vietnamese)", RED, 11.5)
        f.text(125, 62, "Loss of world", 11.5, "middle")
        f.text(125, 76, "efficiency", 11.5, "middle")
        tgt1 = f.pt(52, 12.4)
        assert f.y_at(l_S, tgt1[0]) < tgt1[1] and tgt1[0] < f.px(60)
        f.arrow(125, 82, tgt1[0], tgt1[1], PURPLE, 1.6, 7)
        f.text(265, 62, "Loss of consumer", 11.5, "middle")
        f.text(265, 76, "surplus", 11.5, "middle")
        tgt2 = f.pt(108, 11.6)
        assert f.y_at(l_D, tgt2[0]) < tgt2[1] and tgt2[0] > f.px(100)
        f.arrow(265, 82, tgt2[0], tgt2[1], PURPLE, 1.6, 7)
        f.text(f.px(80), f.py(13) + 4, "Extra cost", 10.5, "middle", INK)
    return f, (P if kind == "diversion" else pts)


def fig_25_3():
    f, pts = trade_diagram("creation")
    save("fig-25-3", f, "Figure 25.3: Trade creation (worked example: ceramic tiles, Poland and Spain)",
         "Supply and demand for ceramic tiles in an importing country with two horizontal partner supply lines, with and without a tariff; two shaded triangles show regained world efficiency and regained consumer surplus.",
         "Hypothetical example: Poland imports ceramic tiles from lower-cost Spain. With a tariff the price is P<sub>w+t</sub> = &euro;20: home firms make Q<sub>2</sub> = 80 million m&sup2;, buyers take Q<sub>3</sub> = 100 million and 20 million are imported. Inside a customs union the tariff goes and the price falls to P<sub>w</sub> = &euro;12: home output falls to Q<sub>1</sub> = 40 million, purchases rise to Q<sub>4</sub> = 140 million and imports rise to 100 million. The shaded triangles are the regained world efficiency and consumer surplus.")


def fig_25_4():
    f, pts = trade_diagram("diversion")
    save("fig-25-4", f, "Figure 25.4: Trade diversion (worked example: footwear, Chile, Vietnam and Brazil)",
         "Supply and demand for footwear in an importing country with three partner supply lines: outside supplier with and without tariff and a higher-cost union partner; shaded areas show loss of world efficiency, extra cost and loss of consumer surplus.",
         "Hypothetical example: Chile imports footwear from Vietnam, the lowest-cost source, at P<sub>V</sub> = US$10, buying Q<sub>4</sub>-equivalent quantities (home output 30 million pairs, purchases 130 million). After joining a customs union with higher-cost Brazil, the tariff on Vietnamese footwear lifts it to P<sub>V+t</sub> = $22, so imports switch to Brazil at P<sub>B</sub> = $16: home output rises to Q<sub>2</sub> = 60 million, purchases fall to Q<sub>3</sub> = 100 million, and the shaded areas show the lost world efficiency, the extra cost of imports and the lost consumer surplus.")


def cbox(f, cx, cy, w, h, lines, **kw):
    """rbox() takes a top-left corner; this takes a centre and returns the
    (cx, cy, w, h) tuple that link()/edge() expect."""
    rbox(f, cx - w / 2, cy - h / 2, w, h, lines, **kw)
    return (cx, cy, w, h)


# =============================================================== CHAPTER 26
def fig_26_1():
    f = Fig(w=460, h=380).scale(200, 0.8)
    f.axes("Quantity of EC$ (millions per period)", "Price of EC$ in US$")
    D1 = lambda q: 0.70 - 0.003 * q
    S1 = lambda q: 0.20 + 0.002 * q
    S2 = lambda q: 0.10 + 0.002 * q  # S1 shifted right by 50
    l_D1 = dline(f, 0, D1(0), 200, D1(200))
    l_S1 = dline(f, 0, S1(0), 200, S1(200))
    l_S2 = dline(f, 10, S2(10), 200, S2(200))
    draw(f, l_D1, GREY)
    draw(f, l_S1, RED)
    draw(f, l_S2, RED)
    peg = 0.40
    f.line(f.X0, f.py(peg), f.X1, f.py(peg), INK, 1.6, "6 4")
    eq1 = f.equilibrium(l_D1, l_S1, "Q" + sub("", "1"), None, guides=False)
    assert abs(eq1[0] - f.px(100)) < 0.6
    f.guide(eq1[0], eq1[1], "Q" + sub("", "1"), None, to_y=False)
    qs2 = (f.px(150), f.py(peg))
    assert abs(f.y_at(l_S2, qs2[0]) - qs2[1]) < 0.01
    f.dot(*qs2, 3.6, RED)
    f.guide(qs2[0], qs2[1], "Q" + sub("", "2"), None, to_y=False)
    f.ytick(f.py(peg), "0.40")
    f.line(eq1[0] + 3, eq1[1], qs2[0] - 3, qs2[1], "#3fb1e3", 4.5)
    f.text((eq1[0] + qs2[0]) / 2, eq1[1] + 20, "Excess supply", 11.5, "middle", INK)
    f.hshift(l_S1, l_S2, f.py(0.45))
    f.text(f.px(150) + 2, f.py(0.47) - 6, "S" + sub("", "1") + "→S" + sub("", "2"), 11, "middle", PURPLE, "600")
    f.label(f.px(200) + 6, f.y_at(l_D1, f.px(200)) + 4, "D", GREY, 13)
    f.label(f.px(200) + 6, f.y_at(l_S1, f.px(200)) + 4, "S" + sub("", "1"), RED, 13)
    f.label(f.px(200) + 6, f.y_at(l_S2, f.px(200)) + 4, "S" + sub("", "2"), RED, 13)
    f.text(f.X1 - 4, f.py(peg) - 8, "Fixed rate", 10.5, "end", INK)
    save("fig-26-1", f, "Figure 26.1: An increase in the supply of EC$",
         "Demand and supply diagram for the Eastern Caribbean dollar (EC$) showing the supply curve shifting rightward from S1 to S2 at the fixed exchange rate of US$0.40, creating excess supply of EC$.",
         "Worked example: the EC$ is pegged at EC$1 = US$0.40, with demand D and supply S<sub>1</sub> crossing exactly at that rate at Q<sub>1</sub> = 100 million. If Eastern Caribbean residents buy more imports, they must supply more EC$ on the forex market to pay for them, shifting supply rightward from S<sub>1</sub> to S<sub>2</sub>. At the fixed rate of 0.40 this creates excess supply: quantity supplied on S<sub>2</sub> rises to Q<sub>2</sub> = 150 million while quantity demanded stays at 100 million. To hold the peg, the central bank must buy up the 50 million surplus EC$ using its reserves of foreign currency.")


def fig_26_2():
    f = Fig(w=460, h=380).scale(200, 0.9)
    f.axes("Quantity of EC$ (millions per period)", "Price of EC$ in US$")
    D1 = lambda q: 0.70 - 0.003 * q
    D2 = lambda q: 0.82 - 0.003 * q  # D1 shifted right by 40
    S1 = lambda q: 0.20 + 0.002 * q
    S2 = lambda q: 0.12 + 0.002 * q  # S1 shifted right by 40
    l_D1 = dline(f, 0, D1(0), 200, D1(200))
    l_D2 = dline(f, 0, D2(0), 200, D2(200))
    l_S1 = dline(f, 0, S1(0), 200, S1(200))
    l_S2 = dline(f, 0, S2(0), 200, S2(200))
    draw(f, l_D1, GREY)
    draw(f, l_D2, GREY)
    draw(f, l_S1, RED)
    peg = 0.40
    f.line(f.X0, f.py(peg), f.X1, f.py(peg), INK, 1.6, "6 4")
    eq1 = f.equilibrium(l_D1, l_S1, "Q" + sub("", "1"), None, guides=False)
    assert abs(eq1[0] - f.px(100)) < 0.6
    f.guide(eq1[0], eq1[1], "Q" + sub("", "1"), None, to_y=False)
    qd2 = (f.px(140), f.py(peg))
    assert abs(f.y_at(l_D2, qd2[0]) - qd2[1]) < 0.01
    f.line(eq1[0] + 3, eq1[1], qd2[0] - 3, qd2[1], "#3fb1e3", 4.5)
    f.text((eq1[0] + qd2[0]) / 2, eq1[1] - 10, "Excess demand", 11.5, "middle", INK)
    draw(f, l_S2, RED, 2.2)
    eq2 = f.equilibrium(l_D2, l_S2, "Q" + sub("", "2"), None, guides=False)
    assert abs(eq2[0] - f.px(140)) < 0.6
    f.guide(eq2[0], eq2[1], "Q" + sub("", "2"), None, to_y=False)
    f.ytick(f.py(peg), "0.40")
    f.hshift(l_D1, l_D2, f.py(0.60))
    f.text(f.px(50), f.py(0.63) - 6, "D" + sub("", "1") + "→D" + sub("", "2"), 11, "middle", PURPLE, "600")
    f.hshift(l_S1, l_S2, f.py(0.50))
    f.text(f.px(170), f.py(0.52) - 6, "S" + sub("", "1") + "→S" + sub("", "2"), 11, "middle", PURPLE, "600")
    f.label(f.px(200) + 6, f.y_at(l_D1, f.px(200)) + 4, "D" + sub("", "1"), GREY, 12.5)
    f.label(f.px(200) + 6, f.y_at(l_D2, f.px(200)) + 4, "D" + sub("", "2"), GREY, 12.5)
    f.label(f.px(200) + 6, f.y_at(l_S1, f.px(200)) + 4, "S" + sub("", "1"), RED, 12.5)
    f.label(f.px(200) + 6, f.y_at(l_S2, f.px(200)) + 4, "S" + sub("", "2"), RED, 12.5)
    f.text(f.X1 - 4, f.py(peg) - 8, "Fixed rate", 10.5, "end", INK)
    save("fig-26-2", f, "Figure 26.2: An increase in the demand for EC$",
         "Demand and supply diagram for the Eastern Caribbean dollar (EC$) showing the demand curve shifting rightward from D1 to D2 at the fixed exchange rate of US$0.40, creating excess demand for EC$ that the central bank meets by shifting supply from S1 to S2.",
         "Starting from the same peg of EC$1 = US$0.40 with D<sub>1</sub> and S<sub>1</sub> crossing at Q<sub>1</sub> = 100 million, suppose more tourists want EC$ to spend on holiday: demand shifts rightward from D<sub>1</sub> to D<sub>2</sub>. At the fixed rate this creates excess demand of 40 million (quantity demanded rises to 140 million while supply stays at 100 million). To defend the peg the central bank itself sells EC$, shifting supply from S<sub>1</sub> to S<sub>2</sub> until it meets D<sub>2</sub> exactly at the fixed rate, at the new equilibrium Q<sub>2</sub> = 140 million &ndash; a sale that adds to the country&rsquo;s foreign currency reserves.")


def fig_26_3():
    f = Fig(w=440, h=380, x1=350).scale(200, 1.4)
    f.axes("Quantity of A$", "Price of A$ in S$")
    D = lambda q: 1.30 - 0.004 * q
    S = lambda q: 0.50 + 0.004 * q
    l_D = dline(f, 0, D(0), 200, D(200))
    l_S = dline(f, 0, S(0), 200, S(200))
    draw(f, l_D, GREY)
    draw(f, l_S, RED)
    eq = f.equilibrium(l_D, l_S, "Q*", "0.90")
    assert abs(eq[0] - f.px(100)) < 0.6 and abs(eq[1] - f.py(0.90)) < 0.6
    f.label(f.px(200) + 6, f.y_at(l_D, f.px(200)) + 4, "D", GREY, 13)
    f.label(f.px(200) + 6, f.y_at(l_S, f.px(200)) - 4, "S", RED, 13)
    f.text(240, 60, "Demand for A$ (from S$ holders)", 11, "middle", GREY)
    f.text(240, 76, "Supply of A$ (from A$ holders)", 11, "middle", RED)
    f.text((f.X0 + f.X1) / 2, f.Y1 + 14, "A$1 = S$0.90", 12, "middle", INK, "600")
    save("fig-26-3", f, "Figure 26.3: A floating currency",
         "Standard demand and supply diagram for Australian dollars priced in Singapore dollars, with the equilibrium exchange rate set where the downward-sloping demand curve meets the upward-sloping supply curve.",
         "The market for Australian dollars (A$) in terms of Singapore dollars (S$). Demand for A$ (from holders of S$ who want Australian goods, assets or currency) slopes downward; supply of A$ (from Australians who want to buy things priced in S$) slopes upward. The equilibrium price, where the two curves cross, is the floating exchange rate: A$1 = S$0.90.")


def fig_26_5():
    f = Fig(w=460, h=380).scale(220, 1.6)
    f.axes("Quantity of A$", "Price of A$ in S$")
    S = lambda q: 0.50 + 0.004 * q
    D1 = lambda q: 1.30 - 0.004 * q
    D2 = lambda q: 1.50 - 0.004 * q  # D1 shifted right by 50
    l_S = dline(f, 0, S(0), 220, S(220))
    l_D1 = dline(f, 0, D1(0), 220, D1(220))
    l_D2 = dline(f, 0, D2(0), 220, D2(220))
    draw(f, l_S, RED)
    draw(f, l_D1, GREY)
    draw(f, l_D2, GREY)
    eq1 = f.equilibrium(l_D1, l_S, "Q" + sub("", "1"), "P" + sub("", "1"))
    eq2 = f.equilibrium(l_D2, l_S, "Q" + sub("", "2"), "P" + sub("", "2"))
    assert abs(eq1[0] - f.px(100)) < 0.6 and abs(eq1[1] - f.py(0.90)) < 0.6
    assert abs(eq2[0] - f.px(125)) < 0.6 and abs(eq2[1] - f.py(1.00)) < 0.6
    f.hshift(l_D1, l_D2, f.py(0.65))
    f.text(f.px(60), f.py(0.68) - 6, "D" + sub("", "1") + "→D" + sub("", "2"), 11, "middle", PURPLE, "600")
    f.label(f.px(220) + 6, f.y_at(l_S, f.px(220)) + 4, "S", RED, 13)
    f.label(f.px(220) + 6, f.y_at(l_D1, f.px(220)) + 4, "D" + sub("", "1"), GREY, 12.5)
    f.label(f.px(220) + 6, f.y_at(l_D2, f.px(220)) + 4, "D" + sub("", "2"), GREY, 12.5)
    f.text(f.px(160), f.py(1.30), "Appreciation of A$", 12, "middle", PURPLE, "600")
    save("fig-26-5", f, "Figure 26.5: An increase in the demand for the Australian dollar",
         "Demand and supply diagram for Australian dollars priced in Singapore dollars, with the demand curve shifting rightward from D1 to D2, raising the equilibrium price from 0.90 to 1.00 Singapore dollars.",
         "Supply of A$ stays fixed while demand shifts rightward from D<sub>1</sub> to D<sub>2</sub> (e.g. more foreign appetite for Australian exports or assets). The equilibrium price of the Australian dollar rises from P<sub>1</sub> = S$0.90 to P<sub>2</sub> = S$1.00, an <strong>appreciation</strong>, and the equilibrium quantity traded rises from Q<sub>1</sub> = 100 million to Q<sub>2</sub> = 125 million. Each A$ now buys more Singapore dollars.")


def fig_26_6():
    f = Fig(w=460, h=380).scale(220, 1.6)
    f.axes("Quantity of A$", "Price of A$ in S$")
    D = lambda q: 1.30 - 0.004 * q
    S1 = lambda q: 0.50 + 0.004 * q
    S2 = lambda q: 0.30 + 0.004 * q  # S1 shifted right by 50
    l_D = dline(f, 0, D(0), 220, D(220))
    l_S1 = dline(f, 0, S1(0), 220, S1(220))
    l_S2 = dline(f, 0, S2(0), 220, S2(220))
    draw(f, l_D, GREY)
    draw(f, l_S1, RED)
    draw(f, l_S2, RED)
    eq1 = f.equilibrium(l_D, l_S1, "Q" + sub("", "1"), "P" + sub("", "1"))
    eq2 = f.equilibrium(l_D, l_S2, "Q" + sub("", "2"), "P" + sub("", "2"))
    assert abs(eq1[0] - f.px(100)) < 0.6 and abs(eq1[1] - f.py(0.90)) < 0.6
    assert abs(eq2[0] - f.px(125)) < 0.6 and abs(eq2[1] - f.py(0.80)) < 0.6
    f.hshift(l_S1, l_S2, f.py(1.10))
    f.text(f.px(200), f.py(1.13) - 6, "S" + sub("", "1") + "→S" + sub("", "2"), 11, "middle", PURPLE, "600")
    f.label(f.px(220) + 6, f.y_at(l_D, f.px(220)) + 4, "D", GREY, 13)
    f.label(f.px(220) + 6, f.y_at(l_S1, f.px(220)) + 4, "S" + sub("", "1"), RED, 12.5)
    f.label(f.px(220) + 6, f.y_at(l_S2, f.px(220)) + 4, "S" + sub("", "2"), RED, 12.5)
    f.text(f.px(60), f.py(1.30), "Depreciation of A$", 12, "middle", PURPLE, "600")
    save("fig-26-6", f, "Figure 26.6: An increase in the supply of the Australian dollar",
         "Demand and supply diagram for Australian dollars priced in Singapore dollars, with the supply curve shifting rightward from S1 to S2, lowering the equilibrium price from 0.90 to 0.80 Singapore dollars.",
         "Demand for A$ stays fixed while supply shifts rightward from S<sub>1</sub> to S<sub>2</sub> (e.g. higher Australian interest in imports). The equilibrium price of the Australian dollar falls from P<sub>1</sub> = S$0.90 to P<sub>2</sub> = S$0.80, a <strong>depreciation</strong>, and the equilibrium quantity rises from Q<sub>1</sub> = 100 million to Q<sub>2</sub> = 125 million. Each A$ now buys fewer Singapore dollars.")


# =============================================================== CHAPTER 27
def fig_27_1():
    f = Fig(w=480, h=320)
    barY = 230
    f.line(90, barY, 420, barY, INK, 3)
    tri = [(255, barY), (230, barY + 46), (280, barY + 46)]
    f.add(f'<polygon points="{tri[0][0]},{tri[0][1]} {tri[1][0]},{tri[1][1]} {tri[2][0]},{tri[2][1]}" '
          f'fill="none" stroke="{RED}" stroke-width="2.6"/>')
    f.text(170, barY - 60, "Current account", 14, "middle", INK, "600")
    f.text(255, barY - 60, "=", 20, "middle", INK, "700")
    f.text(345, barY - 100, "Capital account", 13, "middle", INK, "500")
    f.text(345, barY - 80, "+", 13, "middle", INK, "500")
    f.text(345, barY - 60, "Financial account", 13, "middle", INK, "500")
    f.text(345, barY - 40, "+", 13, "middle", INK, "500")
    f.text(345, barY - 20, "Net errors and omissions", 13, "middle", INK, "500")
    save("fig-27-1", f, "Figure 27.1: The balancing balance of payments",
         "Balance-scale diagram showing the current account balanced on one side against the sum of the capital account, financial account and net errors and omissions on the other.",
         "Shown as a balancing equation rather than an x&ndash;y graph: Current account = Capital account + Financial account + Net errors and omissions. Whatever its sign, the current account balance is always exactly offset by the combined capital and financial account balance, with any measurement gaps absorbed by net errors and omissions, so the overall balance of payments sums to zero by construction.")


def fig_27_2():
    f = Fig(w=460, h=340, x0=150, y0=None, x1=410, y1=40)
    zero = 210
    f.Y0 = zero
    f.line(f.X0, 40, f.X0, 300, INK, 2.2)
    f.arrowhead(f.X0, 35, -90, INK, 9)
    f.line(f.X0, zero, f.X1, zero, INK, 2.2)
    f.arrowhead(f.X1 + 5, zero, 0, INK, 9)
    f.text(f.X0 - 10, 60, "Current account", 11.5, "end", INK)
    f.text(f.X0 - 10, 76, "surplus", 11.5, "end", INK)
    f.text(f.X0 - 10, 268, "Current account", 11.5, "end", INK)
    f.text(f.X0 - 10, 284, "deficit", 11.5, "end", INK)
    f.text(f.X0 - 14, zero + 4, "0", 12, "end", INK)
    f.text(f.X1 - 6, zero + 18, "Time", 12.5, "end", INK)
    Xp = (f.X0 + 30, zero + 24)
    Yp = (f.X0 + 95, zero + 46)
    mid = (f.X0 + 150, zero + 6)
    Zp = (f.X0 + 230, zero - 55)
    endp = (f.X1 - 15, 55)
    f.curve([Xp, Yp, mid, Zp, endp], RED, 3)
    f.dot(*Xp, 4, RED)
    f.dot(*Yp, 4, RED)
    f.dot(*Zp, 4, RED)
    f.text(Xp[0] - 10, Xp[1] - 6, "X", 13, "end", INK, "700")
    f.text(Yp[0], Yp[1] + 18, "Y", 13, "middle", INK, "700")
    f.text(Zp[0] + 12, Zp[1] - 4, "Z", 13, "start", INK, "700")
    save("fig-27-2", f, "Figure 27.2: The J-curve",
         "J-shaped curve of the current account balance over time: starting in deficit at point X, dipping further to a low point Y, then rising up through zero and on to an improved position at point Z.",
         "Time runs along the horizontal axis and the current account balance along the vertical, with a zero line separating surplus (above) from deficit (below). After a depreciation the current account starts in deficit at <strong>X</strong>, worsens further to its lowest point at <strong>Y</strong> as existing contracts take time to adjust, then improves &ndash; crossing back above zero and on to an improved position at <strong>Z</strong> &ndash; once the Marshall&ndash;Lerner condition starts to bite as elasticities rise with time, tracing the shape of a &ldquo;J&rdquo;.")


# =============================================================== CHAPTER 29
def fig_29_1():
    f = Fig(w=800, h=430)
    gii = cbox(f, 400, 40, 220, 42, "Gender Inequality Index (GII)", fill=LIGHTRED, sw=2.4)
    fgi = cbox(f, 285, 132, 190, 42, "Female gender index")
    mgi = cbox(f, 513, 132, 190, 42, "Male gender index")
    frh = cbox(f, 102, 232, 128, 48, ["Female reproductive", "health index"])
    fem = cbox(f, 239, 232, 128, 48, ["Female empowerment", "index"])
    mem = cbox(f, 376, 232, 128, 48, ["Male empowerment", "index"])
    flm = cbox(f, 513, 232, 128, 48, ["Female labour", "market index"])
    mlm = cbox(f, 650, 232, 128, 48, ["Male labour", "market index"])
    mmr = cbox(f, 50, 344, 95, 56, ["Maternal", "mortality ratio"], fill="#f4f4f4", stroke=GREY, size=10.5)
    abr = cbox(f, 150, 344, 95, 56, ["Adolescent", "birth rate"], fill="#f4f4f4", stroke=GREY, size=10.5)
    sed = cbox(f, 270, 344, 120, 56, ["Secondary education", "(both sexes)"], fill="#f4f4f4", stroke=GREY, size=10.5)
    par = cbox(f, 410, 344, 120, 56, ["Parliamentary seats", "(both sexes)"], fill="#f4f4f4", stroke=GREY, size=10.5)
    lfp = cbox(f, 581, 344, 150, 56, ["Labour force participation", "(both sexes)"], fill="#f4f4f4", stroke=GREY, size=10.5)
    f.text(100, 300, "Health", 11, "middle", GREY, "600")
    f.line(50, 305, 150, 305, GREY, 1.2)
    f.text(340, 300, "Empowerment", 11, "middle", GREY, "600")
    f.line(255, 305, 425, 305, GREY, 1.2)
    f.text(581, 300, "Labour market", 11, "middle", GREY, "600")
    f.line(508, 305, 654, 305, GREY, 1.2)
    for a, b in ((mmr, frh), (abr, frh), (sed, fem), (sed, mem), (par, fem), (par, mem), (lfp, flm), (lfp, mlm)):
        link(f, a, b, RED, 1.8, 3, 6)
    for a, b in ((frh, fgi), (fem, fgi), (flm, fgi), (mem, mgi), (mlm, mgi)):
        link(f, a, b, RED, 1.8, 3, 6)
    link(f, fgi, gii, RED, 2.2, 3, 7)
    link(f, mgi, gii, RED, 2.2, 3, 7)
    save("fig-29-1", f, "Figure 29.1: The elements of the GII",
         "Tree diagram showing the Gender Inequality Index built bottom-up from female and male gender indices, each built from health, empowerment and labour market dimension indices and their underlying indicators.",
         "The Gender Inequality Index (GII) is built bottom-up. Indicators (maternal mortality ratio, adolescent birth rate, secondary education, parliamentary seats, labour force participation, split by sex where relevant) combine into five dimension indices, which combine into a female gender index and a male gender index, which finally combine into the overall GII.")


def fig_29_2():
    f = Fig(w=780, h=380)
    ihdi = cbox(f, 390, 44, 300, 50, ["Inequality-adjusted Human", "Development Index (IHDI)"], fill=LIGHTRED, sw=2.4, size=12)
    lex = cbox(f, 140, 140, 190, 46, ["Inequality-adjusted", "life expectancy index"])
    edx = cbox(f, 390, 140, 190, 46, ["Inequality-adjusted", "education index"])
    inx = cbox(f, 640, 140, 190, 46, ["Inequality-adjusted", "income index"])
    lifeexp = cbox(f, 140, 232, 160, 42, "Life expectancy")
    years = cbox(f, 390, 232, 160, 42, "Years of schooling")
    incc = cbox(f, 640, 232, 160, 42, "Income / consumption")
    birth = cbox(f, 140, 330, 160, 46, "Life expectancy at birth", fill="#f4f4f4", stroke=GREY, size=10.5)
    exp = cbox(f, 335, 330, 130, 46, ["Expected years", "of schooling"], fill="#f4f4f4", stroke=GREY, size=10.5)
    mean = cbox(f, 460, 330, 130, 46, ["Mean years", "of schooling"], fill="#f4f4f4", stroke=GREY, size=10.5)
    gni = cbox(f, 640, 330, 160, 46, "GNI per capita (PPP $)", fill="#f4f4f4", stroke=GREY, size=10.5)
    link(f, birth, lifeexp, RED, 1.8, 3, 6)
    link(f, exp, years, RED, 1.8, 3, 6)
    link(f, mean, years, RED, 1.8, 3, 6)
    link(f, gni, incc, RED, 1.8, 3, 6)
    link(f, lifeexp, lex, RED, 2, 3, 6)
    link(f, years, edx, RED, 2, 3, 6)
    link(f, incc, inx, RED, 2, 3, 6)
    link(f, lex, ihdi, RED, 2.2, 3, 7)
    link(f, edx, ihdi, RED, 2.2, 3, 7)
    link(f, inx, ihdi, RED, 2.2, 3, 7)
    save("fig-29-2", f, "Figure 29.2: The elements of the IHDI",
         "Tree diagram showing the Inequality-adjusted Human Development Index built bottom-up from three inequality-adjusted dimension indices: life expectancy, education, and income.",
         "The Inequality-adjusted Human Development Index (IHDI) discounts each of the HDI&rsquo;s three dimension indices (life expectancy, years of schooling, and income/consumption) for the inequality in its distribution across the population, then combines the three inequality-adjusted indices into the overall IHDI.")


def fig_29_3():
    f = Fig(w=880, h=440)
    cols = [70, 210, 350, 490, 630, 770]
    p1, p2, p3 = (cols[0] + cols[1]) / 2, (cols[2] + cols[3]) / 2, (cols[4] + cols[5]) / 2
    top = cbox(f, (p1 + p2 + p3) / 3, 40, 280, 44, "National key performance indicators", fill=LIGHTRED, sw=2.4)
    growth = cbox(f, p1, 140, 200, 46, "Growth and development")
    incl = cbox(f, p2, 140, 170, 46, "Inclusion")
    inter = cbox(f, p3, 140, 240, 46, ["Intergenerational equity", "and sustainability"])
    row3 = ["GDP (per capita)", "Labour productivity", "Median household income", "Income Gini coefficient", "Adjusted net savings", "Dependency ratio"]
    row4 = ["Employment", "Healthy life expectancy", "Poverty rate", "Wealth Gini coefficient", "Public debt (% of GDP)", "Carbon intensity of GDP"]
    b3 = [cbox(f, cols[i], 240, 120, 48, row3[i], size=10) for i in range(6)]
    b4 = [cbox(f, cols[i], 345, 120, 48, row4[i], fill="#f4f4f4", stroke=GREY, size=10) for i in range(6)]
    for pillar, idxs in ((growth, (0, 1)), (incl, (2, 3)), (inter, (4, 5))):
        for i in idxs:
            link(f, pillar, b3[i], RED, 2, 3, 7)
    link(f, top, growth, RED, 2.2, 3, 7)
    link(f, top, incl, RED, 2.2, 3, 7)
    link(f, top, inter, RED, 2.2, 3, 7)
    for i in range(6):
        link(f, b3[i], b4[i], RED, 1.8, 3, 6)
    save("fig-29-3", f, "Figure 29.3: The elements of the IDI",
         "Organisation chart showing national key performance indicators split into three pillars: growth and development, inclusion, and intergenerational equity and sustainability, each with two headline indicators and a further supporting indicator.",
         "National key performance indicators fall into three pillars: growth and development (GDP per capita and labour productivity, further broken down by employment and healthy life expectancy), inclusion (median household income and the income Gini, broken down by the poverty rate and the wealth Gini), and intergenerational equity and sustainability (adjusted net savings and the dependency ratio, broken down by public debt as a share of GDP and the carbon intensity of GDP).")


# =============================================================== CHAPTER 30
def fig_30_1():
    f = Fig(w=760, h=360)
    f.text(160, 30, "GROWTH CYCLE", 13, "middle", RED, "700")
    f.text(600, 30, "DEVELOPMENT CYCLE", 13, "middle", RED, "700")
    # growth cycle: left=investment, top=growth, right=incomes, bottom=savings
    gL = cbox(f, 60, 180, 150, 50, ["Low levels of", "investment"])
    gT = cbox(f, 160, 80, 150, 50, ["Low economic", "growth"])
    gR = cbox(f, 260, 180, 150, 50, "Low incomes")
    gB = cbox(f, 160, 280, 170, 50, ["Low levels of savings", "(high MPC)"])
    link(f, gL, gT, RED, 2.2, 4, 8)
    link(f, gT, gR, RED, 2.2, 4, 8)
    link(f, gR, gB, RED, 2.2, 4, 8)
    link(f, gB, gL, RED, 2.2, 4, 8)
    # development cycle: left=incomes, top=productivity, right=human capital, bottom=education&health
    dL = cbox(f, 460, 180, 150, 50, "Low incomes")
    dT = cbox(f, 560, 80, 150, 50, "Low productivity")
    dR = cbox(f, 680, 180, 170, 50, ["Low levels of", "human capital"])
    dB = cbox(f, 560, 280, 200, 50, ["Low levels of education", "and health care"])
    link(f, dL, dT, RED, 2.2, 4, 8)
    link(f, dT, dR, RED, 2.2, 4, 8)
    link(f, dR, dB, RED, 2.2, 4, 8)
    link(f, dB, dL, RED, 2.2, 4, 8)
    save("fig-30-1", f, "Figure 30.1: Examples of poverty cycles",
         "Two circular poverty-cycle diagrams: a growth cycle linking low investment, low economic growth, low incomes and low savings, and a development cycle linking low incomes, low productivity, low human capital and low education/health care.",
         "Two self-reinforcing poverty cycles. In the <strong>growth cycle</strong> (left), low investment causes low economic growth, which causes low incomes, which causes low savings (a high marginal propensity to consume), which leaves too little available for investment &ndash; the cycle repeats. In the <strong>development cycle</strong> (right), low incomes cause low productivity, which causes low levels of human capital, which causes low levels of education and health care, which keeps incomes low &ndash; the cycle repeats. Breaking either loop at any point can help escape the poverty trap.")


def fig_30_2():
    f = Fig(w=440, h=380).scale(30, 2100)
    f.axes("Quantity of cocoa (tonnes, million)", "Price of cocoa (US$ per tonne)")
    Dl = lambda q: 2600 - 60 * q
    S1 = lambda q: 200 + 60 * q
    S2 = lambda q: -40 + 60 * q  # S1 right by 4 (bumper harvest)
    S3 = lambda q: 440 + 60 * q  # S1 left by 4 (poor harvest)
    l_D = dline(f, 14, Dl(14), 26, Dl(26))
    l_S1 = dline(f, 14, S1(14), 26, S1(26))
    l_S2 = dline(f, 14, S2(14), 26, S2(26))
    l_S3 = dline(f, 14, S3(14), 26, S3(26))
    draw(f, l_D, GREY)
    draw(f, l_S1, RED)
    draw(f, l_S2, RED)
    draw(f, l_S3, RED)
    e1 = f.equilibrium(l_D, l_S1, "Q" + sub("", "1"), None, guides=False)
    e2 = f.equilibrium(l_D, l_S2, "Q" + sub("", "2"), None, guides=False)
    e3 = f.equilibrium(l_D, l_S3, "Q" + sub("", "3"), None, guides=False)
    assert abs(e1[0] - f.px(20)) < 0.6 and abs(e1[1] - f.py(1400)) < 1
    assert abs(e2[0] - f.px(22)) < 0.6 and abs(e2[1] - f.py(1280)) < 1
    assert abs(e3[0] - f.px(18)) < 0.6 and abs(e3[1] - f.py(1520)) < 1
    for p, lbl in ((e3, "Q" + sub("", "3")), (e1, "Q" + sub("", "1")), (e2, "Q" + sub("", "2"))):
        f.guide(p[0], p[1], lbl, None, to_y=False)
    f.ytick(f.py(1520), "P" + sub("", "3"))
    f.ytick(f.py(1400), "P" + sub("", "1"))
    f.ytick(f.py(1280), "P" + sub("", "2"))
    f.hshift(l_S1, l_S2, f.py(1100))
    f.hshift(l_S1, l_S3, f.py(1700))
    f.label(f.px(26) + 6, f.y_at(l_D, f.px(26)) + 4, "D", GREY, 12.5)
    f.label(f.px(26) + 6, f.y_at(l_S1, f.px(26)) + 4, "S" + sub("", "1"), RED, 12)
    f.label(f.px(26) + 6, f.y_at(l_S2, f.px(26)) - 2, "S" + sub("", "2"), RED, 12)
    f.label(f.px(26) + 6, f.y_at(l_S3, f.px(26)) + 4, "S" + sub("", "3"), RED, 12)
    f.text(f.px(17), f.py(1100) - 10, "Bumper harvest", 10.5, "middle", PURPLE, "600")
    f.text(f.px(23), f.py(1700) - 10, "Poor harvest", 10.5, "middle", PURPLE, "600")
    save("fig-30-2", f, "Figure 30.2: The world market for cocoa",
         "Demand-and-supply diagram for the world cocoa market showing price on the vertical axis and quantity on the horizontal axis, with a steep demand curve and three steep supply curves (S1, S2, S3) illustrating how small shifts in supply cause large price swings.",
         "Both demand D and supply S for cocoa are drawn steep (price-inelastic), typical of an agricultural commodity. Starting from S<sub>1</sub> at P<sub>1</sub> = $1,400 and Q<sub>1</sub> = 20 million tonnes, a bumper harvest shifts supply right to S<sub>2</sub>, and price falls sharply to P<sub>2</sub> = $1,280 for only a small rise to Q<sub>2</sub> = 22 million tonnes; a poor harvest shifts supply left to S<sub>3</sub>, and price jumps to P<sub>3</sub> = $1,520 as quantity falls only to Q<sub>3</sub> = 18 million tonnes. Because both curves are inelastic, small supply shocks cause disproportionately large price swings &ndash; a key source of instability for commodity-dependent economies.")


def fig_30_5():
    f = Fig(w=480, h=470)
    cx, cy, r = 240, 240, 58
    f.add(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{RED}" stroke="{INK}" stroke-width="1.6"/>')
    f.text(cx, cy - 4, "Good", 14.5, "middle", "#ffffff", "700")
    f.text(cx, cy + 16, "governance", 14.5, "middle", "#ffffff", "700")
    spokes = [
        (-90, ["Consensus", "oriented"]),
        (-45, ["Accountable"]),
        (0, ["Transparent"]),
        (45, ["Responsive"]),
        (90, ["Equitable and", "inclusive"]),
        (135, ["Effective and", "efficient"]),
        (180, ["Follows the", "rule of law"]),
        (-135, ["Participatory"]),
    ]
    for ang, lines in spokes:
        a = math.radians(ang)
        ux, uy = math.cos(a), math.sin(a)
        p0 = (cx + ux * (r + 4), cy + uy * (r + 4))
        p1 = (cx + ux * (r + 62), cy + uy * (r + 62))
        f.arrow(p0[0], p0[1], p1[0], p1[1], RED, 2.4, 8)
        lx, ly = cx + ux * (r + 100), cy + uy * (r + 100)
        anchor = "middle"
        if ux > 0.3:
            anchor = "start"
        elif ux < -0.3:
            anchor = "end"
        lh = 14
        y0 = ly - lh * (len(lines) - 1) / 2 + 4
        for i, s in enumerate(lines):
            f.text(lx, y0 + i * lh, s, 12, anchor, INK, "600")
    save("fig-30-5", f, "Figure 30.5: The elements of good governance",
         "Hub-and-spoke diagram with 'Good governance' at the centre, connected by arrows to eight surrounding elements: participatory, consensus oriented, accountable, transparent, responsive, equitable and inclusive, effective and efficient, and follows the rule of law.",
         "Good governance is a composite of eight characteristics radiating from the central concept: participatory, consensus oriented, accountable, transparent, responsive, equitable and inclusive, effective and efficient, and following the rule of law. All eight work together, so weakness in any one undermines the quality of governance overall.")


if __name__ == "__main__":
    which = sys.argv[1:]
    for name, fn in list(globals().items()):
        if name.startswith("fig_") and (not which or name[4:].replace("_", "-") in which):
            fn()
