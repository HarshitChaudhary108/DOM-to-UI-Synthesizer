import json
from pathlib import Path
from playwright.sync_api import sync_playwright

MAX_CHARS = 12000 

EXTRACT_JS = """
() => {
  const SKIP = new Set(["SCRIPT","STYLE","NOSCRIPT","SVG","PATH","META","LINK","BR"]);
  const bgArea = {}, fonts = {};
  const CLEAR = "rgba(0, 0, 0, 0)";

  function walk(el, depth) {
    if (depth > 8 || SKIP.has(el.tagName.toUpperCase())) return null;
    const cs = getComputedStyle(el), r = el.getBoundingClientRect();
    if (cs.display === "none" || cs.visibility === "hidden" || (r.width === 0 && r.height === 0)) return null;

    const bg = cs.backgroundColor;
    if (bg !== CLEAR) bgArea[bg] = (bgArea[bg] || 0) + Math.round(r.width * r.height / 1000);
    const font = cs.fontFamily.split(",")[0].replace(/["']/g, "").trim();
    fonts[font] = (fonts[font] || 0) + 1;

    const kids = [...el.children].map(c => walk(c, depth + 1)).filter(Boolean);
    const node = { tag: el.tagName.toLowerCase(), w: Math.round(r.width), h: Math.round(r.height) };
    const s = {};
    if (bg !== CLEAR) s.bg = bg;
    s.color = cs.color; s.fs = cs.fontSize; s.fw = cs.fontWeight;
    if (cs.display === "flex") { s.flex = cs.flexDirection; s.gap = cs.gap; }
    if (cs.display === "grid") { s.grid = cs.gridTemplateColumns; s.gap = cs.gap; }
    if (cs.padding !== "0px") s.pad = cs.padding;
    if (cs.borderRadius !== "0px") s.radius = cs.borderRadius;
    if (["sticky","fixed"].includes(cs.position)) s.pos = cs.position;
    node.s = s;

    if (kids.length === 0) { const t = (el.innerText || "").trim().slice(0, 160); if (t) node.text = t; }
    if (el.tagName === "IMG") { node.src = el.currentSrc || el.src; node.alt = el.alt; }
    if (el.tagName === "A") node.href = el.getAttribute("href");
    if (kids.length) node.c = kids;

    // collapse useless wrapper divs
    if (kids.length === 1 && !node.text && bg === CLEAR && ["div","span"].includes(node.tag)) return kids[0];
    return node;
  }

  const top = (o, n) => Object.entries(o).sort((a, b) => b[1] - a[1]).slice(0, n).map(e => e[0]);
  const tree = walk(document.body, 0);
  return { title: document.title, palette_by_area: top(bgArea, 5), fonts: top(fonts, 3), tree };
}
"""


def scrape_node(state: dict) -> dict:
    url = state["url"]
    Path("output").mkdir(exist_ok=True)
    with sync_playwright() as p:
      browser = p.chromium.launch(channel="msedge")
      page = browser.new_page(viewport={"width": 1440, "height": 900})

      page.goto(url, wait_until="networkidle", timeout=15000)

      dom_tree = page.evaluate(EXTRACT_JS)

      page.screenshot(path="capture.png", full_page=True)

      browser.close() 

    dom = json.dumps(dom_tree, separators=(",", ":"))
    if len(dom) > MAX_CHARS:
        dom = dom[:MAX_CHARS] + '..."[truncated]"'
    print(f"  captured {len(dom)} chars of DOM")
    return {"dom": dom}