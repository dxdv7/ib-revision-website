"""Swap textbook-scan figure callouts for the original SVG redraws.

For every <div class="callout diagram"> whose <img> points at
assets/econ-figures/fig-X.png:
  - if assets/figures-original/fig-X.svg + .json exist: rewrite the whole
    callout (label, image, alt, caption) from the JSON;
  - otherwise (real-data charts we are not redrawing): drop the scan <img>
    but keep the callout's own text, so no scan is ever served.
Run with --dry to only report.
"""
import json, os, re, sys

ROOT = "/Users/davidbukraba/Desktop/IB WEBSITE"
FIG = os.path.join(ROOT, "assets/figures-original")
IMG_RE = re.compile(r'<img class="econ-fig-img" src="assets/econ-figures/(fig-[^"]+)\.png"[^>]*>')


def svg_width(path):
    m = re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', open(path, encoding="utf-8").read(2000))
    return float(m.group(1)), float(m.group(2))


def div_span(s, i):
    """(start, end) of the <div ...>...</div> that contains index i."""
    start = s.rfind('<div class="callout diagram"', 0, i)
    depth, pos = 0, start
    for m in re.finditer(r"<div\b|</div>", s[start:]):
        depth += 1 if m.group(0) != "</div>" else -1
        if depth == 0:
            return start, start + m.end()
    raise ValueError("unbalanced div")


def swap(s, stats):
    out, cur = [], 0
    for m in list(IMG_RE.finditer(s)):
        if m.start() < cur:
            continue
        fid = m.group(1)
        a, b = div_span(s, m.start())
        out.append(s[cur:a])
        svg, js = f"{FIG}/{fid}.svg", f"{FIG}/{fid}.json"
        if os.path.exists(svg) and os.path.exists(js):
            j = json.load(open(js, encoding="utf-8"))
            w, _ = svg_width(svg)
            mw = int(min(w * 1.3, 760))
            out.append(
                f'<div class="callout diagram"><span class="c-label">{j["label"]}</span>'
                f'<img class="econ-fig-img" src="assets/figures-original/{fid}.svg" '
                f'alt="{j["alt"]}" style="max-width:{mw}px" loading="lazy">{j["caption"]}</div>'
            )
            stats["swapped"].append(fid)
        else:
            out.append(IMG_RE.sub("", s[a:b]))
            stats["dropped"].append(fid)
        cur = b
    out.append(s[cur:])
    return "".join(out)


def main():
    dry = "--dry" in sys.argv
    stats = {"swapped": [], "dropped": []}

    # index.html: only inside the economics NOTES_HTML object
    p = os.path.join(ROOT, "index.html")
    c = open(p, encoding="utf-8").read()
    a = c.index("var NOTES_HTML = {")
    b = c.index("\nvar BIO_NOTES_HTML", a)
    new_c = c[:a] + swap(c[a:b], stats) + c[b:]
    if not dry:
        open(p, "w", encoding="utf-8").write(new_c)

    # source/notes backups
    src_stats = {"swapped": [], "dropped": []}
    for n in sorted(os.listdir(os.path.join(ROOT, "source/notes"))):
        if not n.endswith(".html"):
            continue
        sp = os.path.join(ROOT, "source/notes", n)
        t = open(sp, encoding="utf-8").read()
        t2 = swap(t, src_stats)
        if t2 != t and not dry:
            open(sp, "w", encoding="utf-8").write(t2)

    print("index.html  swapped:", len(stats["swapped"]), " dropped scan:", len(stats["dropped"]))
    print("dropped ids:", sorted(set(stats["dropped"])))
    print("source/notes swapped:", len(src_stats["swapped"]), " dropped:", len(src_stats["dropped"]))


main()
