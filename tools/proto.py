import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from figlib import *

OUT = "/private/tmp/claude-501/-Users-davidbukraba-Desktop-IB-WEBSITE/d941ae35-4977-42d4-ad2e-6b2e67567dd5/scratchpad/proto"
os.makedirs(OUT, exist_ok=True)


def save(name, fig, title, desc):
    open(f"{OUT}/{name}.svg", "w").write(fig.svg(title, desc))


# ---- 5.1  supply curve (was: frozen pizzas) -> e-scooters -----------------
f = Fig().scale(1000, 700)
f.axes("Quantity of e-scooters (per month)", "Price of e-scooters ($)")
f.yticks([100, 200, 300, 400, 500, 600])
f.xticks([200, 400, 600, 800, 1000])
fn = lambda x: 170 + 0.0623 * (x - 200) ** 1.34
xs = [240, 340, 500, 650, 800, 900]
data = [(x, fn(x)) for x in xs]
pts = [f.pt(*d) for d in data]
f.guide(*f.pt(500, fn(500)), to_x=True, to_y=True)
f.guide(*f.pt(800, fn(800)), to_x=True, to_y=True)
f.curve(pts)
for d in [data[0], data[2], data[4], data[5]]:
    f.dot(*f.pt(*d))
f.label(f.px(900) + 8, f.py(fn(900)) - 10, "S (Supply)", INK, 12.5)
save("fig5-1", f, "Supply curve for e-scooters",
     "Upward-sloping supply curve: as the price of e-scooters rises, quantity supplied rises.")

# ---- 7.x  demand shift on a market (headphones) -----------------------------
f = Fig()
f.axes("Quantity of headphones (000s per month)", "Price of headphones ($)")
S = ((120, 268), (360, 78))
D1 = ((110, 88), (300, 292)); D2 = ((170, 74), (360, 278))
f.line(*D1[0], *D1[1], GREY, 2.8); f.label(304, 306, "D" + sub("", 1), GREY, 13)
f.line(*D2[0], *D2[1], GREY, 2.8); f.label(364, 292, "D" + sub("", 2), GREY, 13)
f.line(*S[0], *S[1], RED, 2.8); f.label(362, 76, "S", RED, 13)
e1 = f.equilibrium(S, D1, "Q" + sub("", 1), "P" + sub("", 1))
e2 = f.equilibrium(S, D2, "Q" + sub("", 2), "P" + sub("", 2))
f.hshift(D1, D2, 118)
f.hshift(D1, D2, 246)
save("demand-shift", f, "Increase in demand for headphones",
     "Demand shifts right from D1 to D2 against an unchanged supply curve, raising price from P1 to P2 and quantity from Q1 to Q2.")

# ---- 20.1  demand-pull inflation (AD/AS) --------------------------------------
f = Fig()
f.axes("Real output (Y)", "Average price level")
SR = ((120, 288), (330, 62))
A1 = ((112, 82), (300, 262)); A2 = ((156, 62), (344, 242))
f.line(*A1[0], *A1[1], GREY, 2.8); f.label(304, 278, "AD" + sub("", 1), GREY, 12.5)
f.line(*A2[0], *A2[1], GREY, 2.8); f.label(348, 258, "AD" + sub("", 2), GREY, 12.5)
f.line(*SR[0], *SR[1], RED, 2.8); f.label(322, 52, "SRAS" + sub("", 1), RED, 12.5)
f.equilibrium(SR, A1, "Y" + sub("", 1), "P" + sub("", 1), dot=None) if False else None
e1 = f.intersect(SR, A1); e2 = f.intersect(SR, A2)
f.guide(*e1, "Y" + sub("", 1), "P" + sub("", 1)); f.guide(*e2, "Y" + sub("", 2), "P" + sub("", 2))
f.dot(*e1, 3.6, INK); f.dot(*e2, 3.6, INK)
f.hshift(A1, A2, 100)
f.hshift(A1, A2, 228)
save("demand-pull", f, "Demand-pull inflation",
     "Aggregate demand shifts right from AD1 to AD2 along SRAS, raising the price level from P1 to P2 and output from Y1 to Y2.")

# ---- 1.4  circular flow (two-sector) ---------------------------------------------
f = Fig(w=440, h=380)
def box(x, y, w, h, s):
    f.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="#fdeaea" stroke="{RED}" stroke-width="2.2"/>')
    f.text(x + w / 2, y + h / 2 + 5, s, 14, "middle", INK, "600")
box(150, 34, 140, 50, "Households")
box(150, 296, 140, 50, "Firms")
f.arrow(190, 86, 190, 294, RED, 2.4)
f.text(182, 182, "Factors of production", 11.5, "end")
f.text(182, 198, "(land, labour, capital)", 11, "end", GREY)
f.arrow(250, 294, 250, 86, RED, 2.4)
f.text(258, 176, "Wages, rent,", 11.5)
f.text(258, 192, "interest, profit", 11.5)
# outer loops
f.flow([(292, 321), (404, 321), (404, 59), (292, 59)])
f.text(414, 190, "Goods and services", 11.5, "middle", INK, rotate=90)
f.flow([(148, 59), (36, 59), (36, 321), (148, 321)])
f.text(26, 190, "Spending on goods and services", 11.5, "middle", INK, rotate=-90)
save("circular-flow", f, "Two-sector circular flow of income",
     "Households supply factors of production to firms and receive income; firms supply goods and services and receive spending.")
print("ok", os.listdir(OUT))
