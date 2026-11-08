"""Done checks for the reader pages (reader-overhaul and reader-consistency specs).

The specs are 2026-11-04-reader-overhaul-design.md and, for marks, filters and related,
docs/drafts/2026-11-07-reader-consistency/design-marks.md and build-plan.md.

Run against a build, either the one `quartz build --serve` serves on 8080 or
`--serve quartz/public`, which serves the built folder with clean URLs (a plain
`http.server` 404s on `/findings/<id>`)::

    WIKI_BASE_URL=localhost:8096 CBORG_API_KEY= scripts/build_quartz.sh
    uv run --with playwright python scripts/check_reader.py grid \
        --base http://localhost:8096 --serve quartz/public

Checks, each run by name:

- home: the home page's title, three doors and reference line, the top bar (at most 7
  controls after the wordmark at 1440 px, every collection within two clicks, the Browse
  menu by mouse, keyboard and tap), where the CBORG key is entered, and the strips check.
- strips: the topic key, map and table on /topics/, and cards that take their topic's colour.
- plain: reader text carries no pipeline terms, statistics or "caveat".
- grid: open-question dots sit in their records' rows and columns, and their pop-ups work.
- pages: result page sections, the kind chips, square cards, kind words, and contrast.
- contrast: small labels reach 4.5:1 in light mode.
- cross: the Results map matches the records, hover cards, related-result lines and the
  box list, column notes, Compare panels, and ringed question bridges.
- marks: the marks of both maps (design-marks.md, option M2), in light and dark, at 1280
  and 390 px, with two negative controls the check must catch.
- filters: each board's chips, toggles, count, URL state, list view and map fading.
- related: each result page lists its related results in other projects.

Exit 0 when the check passes, 1 with one line per failure otherwise. Notes (lines
starting "note:") never fail a check. Uses the installed Chrome, so no browser download.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from collections import Counter
from functools import cache, partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread
from urllib.parse import parse_qs, urlparse

# Supplied at run time by `uv run --with playwright`; not a project dependency.
from playwright.sync_api import (  # ty: ignore[unresolved-import]
    Page,
    sync_playwright,
)
from playwright.sync_api import TimeoutError as PlaywrightTimeout  # ty: ignore[unresolved-import]

from beril_wiki.stages.gists import statistical

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "quartz" / "content"
PHONE = {"width": 390, "height": 844}
DESKTOP = {"width": 1280, "height": 900}
WIDE = {"width": 1440, "height": 900}

HOME_HEADINGS = ["BERIL Knowledge Wiki"]
HOME_ABSENT = [
    "What BERIL found",
    "Plan your next project",
    "checked against PubMed",
    "change the picture",
]
# Home sections the doors replaced; each now lives on /topics/, a board or nowhere.
HOME_GONE = [
    ".fcard",
    ".scard",
    ".xqlist",
    ".kindcard",
    "[data-tkey]",
    "[data-tmap]",
    ".topictable",
    ".qgrid",
    ".nvmap",
]
DOORS = [
    ("Results", "findings/"),
    ("Open questions", "directions/"),
    ("Topics", "topics/"),
]
REFERENCE = [
    ("Concepts", "concepts"),
    ("Entities", "entities"),
    ("Conflicts", "conflicts"),
    ("Reports", "summaries"),
    ("Authors", "authors"),
]
# Every collection index a reader reaches from home within two clicks.
COLLECTIONS = [
    "findings/",
    "directions/",
    "topics/",
    "concepts/",
    "entities/",
    "conflicts/",
    "summaries/",
    "authors/",
    "about",
]
BAR_MAX = 7
PIPELINE_TERMS = [
    "Candidate novel",
    "Insufficient literature evidence",
    "needs compute",
    "lakehouse analysis",
    "Literature check",
    "pipeline judgment",
    "Research direction",
    "headline finding",
]
NEED_COLUMN = {
    "data in the lakehouse": 0,
    "needs compute": 1,
    "needs new measurements": 2,
    "unknown": 3,
}
BAD_NULL_CASES = ("missing data", "unperformed analysis")
NULL_WORDS = {"No effect found", "Inconclusive test"}
# Wording that would read as one project confirming another (the links stage's list).
CONFIRM = re.compile(
    r"\b(?:confirm\w*|corroborat\w*|validat\w*|reproduc\w*|replicat\w*|independen\w*|agree\w*)\b"
    r"|support(?:s|ed)? each other",
    re.I,
)
LIGHT_LABELS = [
    ".rt",
    ".card .meta",
    ".fcard .meta",  # topic pages
    ".qcolh",
    ".nvcolh",
    ".ready.part",
    ".px-facet-lbl",
    ".crel",
    ".cnovel",
]
# Shown only at phone width.
PHONE_LABELS = [".qlab", ".nvlab"]
FINDING_HEADINGS = [
    "What the report measured",
    "Limits",
    "Compared with published work",
    "Open questions that build on this",
    "Related results in other projects",
    "Related conflicts",
]
RELATED_HEADING = "Related results in other projects"
# Filter and mark key for a result's kind, from the raw `result` field (Cards.tsx kindKey).
KIND_KEY = {
    "observation": "result",
    "inference": "interpretation",
    "null result": "null",
    "correction": "correction",
}
# How a Results box's label counts each kind (Novelty.tsx COUNT_WORDS): one, many.
BOX_COUNT_WORDS = {
    "result": ("result", "results"),
    "null": ("found no effect or was inconclusive", "found no effect or were inconclusive"),
    "interpretation": ("interpretation", "interpretations"),
    "correction": ("correction", "corrections"),
}
KIND_WORDS = {
    "result": "Result",
    "null": "No effect found, or inconclusive",
    "interpretation": "Interpretation",
    "correction": "Correction",
}
SHAPE = {"result": "circle", "null": "circle", "interpretation": "triangle", "correction": "cross"}
NEEDS = ["data", "build", "measure", "unclear"]
NOVEL_WORDS = "Cites a result in the Novel column"
GONE_FAMILIES = ["Cited by the same open question", "One project uses or cites another"]
# The design's tokens (design-marks.md "Geometry"): Novel orange and the box border grey.
TOKENS = {
    "light": {"nv-new": (194, 65, 12), "nv-box": (135, 142, 148)},
    "dark": {"nv-new": (217, 89, 38), "nv-box": (107, 112, 117)},
}


def frontmatter(path: Path) -> dict:
    """Read the simple `key: json-value` lines of a record's frontmatter."""
    out: dict = {}
    lines = path.read_text(encoding="utf-8").split("\n")
    for line in lines[1 : lines.index("---", 1)]:
        key, _, val = line.partition(": ")
        try:
            out[key] = json.loads(val)
        except ValueError:
            out[key] = val
    return out


def ids(kind: str) -> list[str]:
    return sorted(p.stem for p in (ROOT / "wiki" / kind).glob("*.md") if p.stem != "index")


@cache
def records() -> dict:
    """The published records the checks compute their expectations from."""
    findings = {
        p.stem: frontmatter(p)
        for p in sorted((CONTENT / "findings").glob("*.md"))
        if p.stem != "index"
    }
    directions = {
        p.stem: frontmatter(p)
        for p in sorted((CONTENT / "directions").glob("*.md"))
        if p.stem != "index"
    }
    index = frontmatter(CONTENT / "findings" / "index.md")
    listed = {i for i, fm in findings.items() if fm.get("listed") is not False}
    order = index.get("compare_order") or []
    used = {findings[i].get("compare_text") for i in listed}
    cols = [c for c in order if c != order[-1] or c in used]
    links = [
        lk
        for lk in index.get("links") or []
        if lk.get("family") == "r" and lk.get("a") in listed and lk.get("b") in listed
    ]
    novel = order[0] if order else ""
    results = {
        i: {
            "kind": KIND_KEY.get(findings[i].get("result", ""), "result"),
            "col": findings[i].get("compare_text", ""),
            "topic": findings[i].get("topic", ""),
            "source": findings[i].get("source", ""),
            "rel": any(i in (lk["a"], lk["b"]) for lk in links),
        }
        for i in sorted(listed)
    }
    questions = {}
    for stem, fm in directions.items():
        raw = fm.get("need")
        need: str = raw if isinstance(raw, str) and raw in NEEDS else "unclear"
        questions[f"directions/{stem}"] = {
            "novel": any(
                f in listed and findings[f].get("compare_text") == novel
                for f in fm.get("findings") or []
            ),
            "cross": bool(fm.get("cross")),
            "need": need,
            "col": NEEDS.index(need),
            "topic": fm.get("topic", ""),
            "approach": fm.get("approach", ""),
            "approach_text": fm.get("approach_text", ""),
        }
    boxes: dict[tuple[str, str, str], list[str]] = {}
    for i, r in results.items():
        boxes.setdefault((str(r["topic"]), str(r["col"]), str(r["source"])), []).append(i)
    return {
        "findings": findings,
        "directions": directions,
        "index": index,
        "listed": listed,
        "order": order,
        "cols": cols,
        "novel": novel,
        "links": links,
        "results": results,
        "questions": questions,
        "boxes": boxes,
    }


def new_page(browser, viewport=DESKTOP, js=True) -> Page:
    ctx = browser.new_context(viewport=viewport, java_script_enabled=js)
    return ctx.new_page()


def themed(browser, theme: str, viewport=DESKTOP, touch=False) -> Page:
    """A page in `theme`: Quartz reads localStorage "theme" before the system scheme."""
    ctx = browser.new_context(
        viewport=viewport, color_scheme=theme, has_touch=touch, is_mobile=touch
    )
    ctx.add_init_script(f"try {{ localStorage.setItem('theme', '{theme}') }} catch (e) {{}}")
    return ctx.new_page()


def go(page: Page, url: str) -> None:
    page.goto(url, wait_until="networkidle")


def http_status(url: str) -> int:
    try:
        return urllib.request.urlopen(url, timeout=20).status
    except urllib.error.HTTPError as e:
        return e.code


def walk_onto(page: Page, mark, card, want: str | None = None, aim: str = "link") -> str:
    """Hover `mark`, then move to its `card` in 2 px steps, as a hand would.

    `aim` is "link" (the card's "Open" link) or "head" (the card's title, across neighbours).

    Returns "" when the card is still open there and links to `want` (when given), else
    the failure. Coarser steps jump over gaps and neighbouring marks a real pointer meets.
    """
    mark.scroll_into_view_if_needed()
    r = mark.bounding_box()
    x0, y0 = r["x"] + r["width"] / 2, r["y"] + r["height"] / 2
    page.mouse.move(x0, y0)
    page.wait_for_timeout(150)
    if not card.is_visible():
        return "hover does not open the card"
    c = card.bounding_box()
    link = card.locator("a.nvopen, a.qopen").first
    box = link.bounding_box() if link.count() else None
    inside = box and c["y"] <= box["y"] and box["y"] + box["height"] <= c["y"] + c["height"]
    if aim == "link" and inside:
        x1, y1 = box["x"] + min(30, box["width"] / 2), box["y"] + box["height"] / 2
    else:
        x1, y1 = c["x"] + c["width"] / 2, c["y"] + min(20, c["height"] / 2)
    page.mouse.move(x1, y1, steps=max(4, int(((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5 / 2)))
    page.wait_for_timeout(400)
    if not card.is_visible():
        return "the card closes while the pointer moves onto it"
    if not card.locator("a").count():
        return "the card holds no link"
    if want is not None and card.locator("a.nvopen").get_attribute("href") != want:
        return "the card switched to another result on the way"
    return ""


def jump_to(page: Page, a, b) -> str:
    """Hover mark `a`, then move to mark `b` in one step and rest there for 900 ms."""
    a.scroll_into_view_if_needed()
    ra = a.bounding_box()
    page.mouse.move(ra["x"] + ra["width"] / 2, ra["y"] + ra["height"] / 2)
    page.wait_for_timeout(200)
    b.scroll_into_view_if_needed()
    rb = b.bounding_box()
    page.mouse.move(rb["x"] + rb["width"] / 2, rb["y"] + rb["height"] / 2)
    page.wait_for_timeout(900)
    return f"from ({ra['x']:.0f}, {ra['y']:.0f}) to ({rb['x']:.0f}, {rb['y']:.0f})"


def collapse(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def last_part(href: str) -> str:
    return urlparse(href).path.rstrip("/").rsplit("/", 1)[-1]


# ---------------------------------------------------------------- colours


def rgba(c: str) -> tuple[float, float, float, float]:
    """A computed CSS colour as (r, g, b, a) on 0-255, from rgb(), rgba() or color(srgb)."""
    c = c.strip()
    if c == "transparent":
        return (0.0, 0.0, 0.0, 0.0)
    if m := re.match(r"rgba?\(([^)]*)\)", c):
        p = [float(x) for x in re.split(r"[,\s/]+", m[1].strip()) if x]
        return (p[0], p[1], p[2], p[3] if len(p) > 3 else 1.0)
    if m := re.match(r"color\(srgb\s+([^)]*)\)", c):
        p = [float(x) for x in re.split(r"[\s/]+", m[1].strip()) if x]
        return (p[0] * 255, p[1] * 255, p[2] * 255, p[3] if len(p) > 3 else 1.0)
    raise ValueError(f"unparsed colour '{c}'")


def colours_in(text: str) -> list[tuple[float, float, float, float]]:
    return [rgba(m) for m in re.findall(r"(?:rgba?|color)\([^)]*\)", text)]


def same(a, b, tol: float = 2.0) -> bool:
    return all(abs(x - y) <= tol for x, y in zip(a[:3], b[:3], strict=True)) and (
        abs((a[3] if len(a) > 3 else 1) - (b[3] if len(b) > 3 else 1)) < 0.02
    )


def blend(fg, bg, op: float = 1.0) -> tuple[float, float, float, float]:
    a = (fg[3] if len(fg) > 3 else 1.0) * op
    return (*(a * f + (1 - a) * b for f, b in zip(fg[:3], bg[:3], strict=True)), 1.0)


def surface(stack: list[str]) -> tuple[float, float, float, float]:
    """The colour under an element: its ancestors' backgrounds, nearest first, down to an
    opaque one (white when none is), composited."""
    layers = []
    for c in stack:
        col = rgba(c)
        if col[3] == 0:
            continue
        layers.append(col)
        if col[3] >= 1:
            break
    out: tuple[float, float, float, float] = (255.0, 255.0, 255.0, 1.0)
    for col in reversed(layers):
        out = blend(col, out)
    return out


def luminance(rgb: tuple[float, ...]) -> float:
    def ch(v: float) -> float:
        v /= 255
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4

    r, g, b = (ch(v) for v in rgb[:3])
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(a, b) -> float:
    hi, lo = sorted((luminance(a), luminance(b)), reverse=True)
    return (hi + 0.05) / (lo + 0.05)


def neutral(c) -> bool:
    """A grey: its channels lie within 10% of each other."""
    return max(c[:3]) - min(c[:3]) <= 25.5


def show(c) -> str:
    return "rgb(" + ", ".join(f"{v:.0f}" for v in c[:3]) + ")"


# Shared by the page scripts below: the backgrounds under an element, nearest first, and the
# opacity that reaches it from its ancestors below the first opaque background.
JS_LIB = """
const alphaOf = c => {
  const m = c.match(/rgba?\\(([^)]+)\\)/)
  if (m) { const p = m[1].split(/[\\s,/]+/).filter(Boolean); return p.length > 3 ? +p[3] : 1 }
  const k = c.match(/color\\([^)]*\\/\\s*([\\d.]+)\\)/)
  return c === 'transparent' ? 0 : k ? +k[1] : 1
}
const under = e => {
  const stack = []
  let op = +getComputedStyle(e).opacity
  for (let n = e.parentElement; n; n = n.parentElement) {
    const c = getComputedStyle(n).backgroundColor
    stack.push(c)
    if (alphaOf(c) >= 1) break
    op *= +getComputedStyle(n).opacity
  }
  return { stack, op }
}
const tok = name => {
  const e = document.createElement('i')
  e.style.color = `var(${name})`
  document.body.append(e)
  const c = getComputedStyle(e).color
  e.remove()
  return c
}
const ndFeat = e => {
  const s = getComputedStyle(e)
  const b = getComputedStyle(e, '::before'), a = getComputedStyle(e, '::after')
  const r = e.getBoundingClientRect()
  return {
    id: e.dataset.id || '', k: e.dataset.k || '', rel: e.classList.contains('rel'),
    color: s.color, shadow: s.boxShadow, outline: s.outlineStyle, w: r.width, h: r.height,
    b: { content: b.content, bg: b.backgroundColor, img: b.backgroundImage, clip: b.clipPath,
         radius: b.borderTopLeftRadius, shadow: b.boxShadow },
    a: { content: a.content, style: a.borderTopStyle, width: a.borderTopWidth,
         color: a.borderTopColor, radius: a.borderTopLeftRadius, top: a.top },
    under: under(e),
  }
}
const qdFeat = q => {
  const d = q.querySelector(':scope > .qdot')
  const s = getComputedStyle(q), b = getComputedStyle(d, '::before')
  const r = d.getBoundingClientRect()
  return {
    id: q.dataset.id || '', novel: q.classList.contains('novel'),
    cross: q.classList.contains('cross'),
    color: s.color, op: +getComputedStyle(d).opacity, shape: d.dataset.shape || null,
    label: d.getAttribute('aria-label') || '', pop: q.querySelector('.qpop')?.textContent || '',
    w: parseFloat(b.width), h: parseFloat(b.height), x: r.x, y: r.y,
    b: { bg: b.backgroundColor, img: b.backgroundImage, clip: b.clipPath,
         radius: b.borderTopLeftRadius, shadow: b.boxShadow },
    under: under(q),
  }
}
"""


def lib(body: str) -> str:
    return f"() => {{ {JS_LIB}\n{body} }}"


# ---------------------------------------------------------------- home and bar


def check_home(browser, base: str) -> list[str]:
    fails: list[str] = []
    rec = records()
    page = new_page(browser)
    go(page, base + "/")
    heads = page.eval_on_selector_all("h1, h2", "els => els.map(e => e.textContent.trim())")
    if heads != HOME_HEADINGS:
        fails.append(f"home: headings {heads} != {HOME_HEADINGS}")
    text = page.inner_text("body")
    fails += [f"home: contains '{s}'" for s in HOME_ABSENT if s.lower() in text.lower()]
    for sel in HOME_GONE:
        if n := page.locator(sel).count():
            fails.append(f"home: still shows {n} '{sel}'; it moved off the home page")

    # Three doors, each with its count from the records.
    doors = page.eval_on_selector_all(
        ".homedoors nav.cards.doors a.card.door",
        """els => els.map(e => ({label: e.querySelector('b')?.textContent.trim(),
            href: e.getAttribute('href'), n: e.querySelector('.meta .n')?.textContent.trim()}))""",
    )
    topics = len([p for p in (CONTENT / "topics").glob("*.md") if p.stem != "index"])
    counts = {
        "findings/": f"{len(rec['listed'])} results",
        "directions/": f"{len(rec['directions'])} questions",
        "topics/": f"{topics} topics",
    }
    want = [lab for lab, _ in DOORS]
    if [d["label"] for d in doors] != want:
        fails.append(f"home: doors {[d['label'] for d in doors]}, expected {want}")
    for d in doors:
        target = next((t for lab, t in DOORS if lab == d["label"]), None)
        if target is None:
            continue
        if not (d["href"] or "").endswith(target):
            fails.append(f"home: door {d['label']} links to {d['href']}, expected {target}")
        if d["n"] != counts[target]:
            fails.append(f"home: door {d['label']} reads '{d['n']}', records give {counts[target]}")
    ref = page.eval_on_selector_all(
        'nav.reflinks[aria-label="Reference"] a',
        "els => els.map(e => [e.childNodes[0].textContent.trim(), e.getAttribute('href'),"
        " e.querySelector('.n')?.textContent.trim()])",
    )
    if [r[0] for r in ref] != [lab for lab, _ in REFERENCE]:
        fails.append(f"home: reference line {[r[0] for r in ref]}, expected {REFERENCE}")
    for label, href, n in ref:
        coll = next((c for lab, c in REFERENCE if lab == label), "")
        files = [p for p in (CONTENT / coll).glob("*.md") if p.stem != "index"]
        # Reports also count the digests, which publish files beside them.
        if coll != "summaries" and n != str(len(files)):
            fails.append(f"home: reference {label} reads {n}, {coll}/ holds {len(files)} pages")
        if not (n or "").isdigit() or int(n) < 1:
            fails.append(f"home: reference {label} count '{n}'")
        if not (href or "").rstrip("/").endswith(coll):
            fails.append(f"home: reference {label} links to {href}")

    fails += check_bar(browser, base)
    # The CBORG key is entered where it is used: on Ask and in search's meaning control.
    if page.locator(".px-keybtn").count():
        fails.append("home: the bar still has the CBORG key button")
    page.locator("header.bar .search-button").click()
    page.wait_for_timeout(400)
    meaning = page.locator(".px-meaning-ctl .px-meaning-key, .px-meaning-ctl [data-act=key]")
    if not meaning.count():
        ctl = page.locator(".px-meaning-ctl")
        fails.append(
            "home: search's meaning control offers no key entry: "
            f"'{ctl.first.inner_text() if ctl.count() else 'no control'}'"
        )
    page.keyboard.press("Escape")
    go(page, base + "/ask")
    if not page.locator(".px-aistatus .px-keyentry").count():
        fails.append("home: the Ask page has no CBORG key entry in .px-aistatus")
    fails += check_strips(browser, base)
    return fails


def check_bar(browser, base: str) -> list[str]:
    """At 1440 px the bar holds at most 7 controls after the wordmark; every collection is
    within two clicks of home; the Browse menu works by mouse, keyboard and tap."""
    fails: list[str] = []
    page = new_page(browser, WIDE)
    go(page, base + "/")
    controls = page.evaluate(
        """() => [...document.querySelectorAll('header.bar a, header.bar button,'
            + ' header.bar input, header.bar select')]
            .filter(e => !e.matches('.wordmark') && e.getClientRects().length
                     && getComputedStyle(e).visibility !== 'hidden')
            .map(e => e.getAttribute('aria-label') || e.textContent.trim().split('\\n')[0])"""
    )
    if not controls or len(controls) > BAR_MAX:
        fails.append(f"home: at 1440 px the bar has {len(controls)} controls: {controls}")
    navs = page.eval_on_selector_all(
        "header.bar .barnav > a.barlink", "els => els.map(e => e.textContent.trim())"
    )
    if navs != [lab for lab, _ in DOORS]:
        fails.append(f"home: bar links {navs}, expected {[lab for lab, _ in DOORS]}")
    browse = page.eval_on_selector_all(
        "#barmenu-list a", "els => els.map(e => [e.textContent.trim(), e.getAttribute('href')])"
    )
    if [b[0] for b in browse] != [
        "Concepts",
        "Entities",
        "Conflicts",
        "Reports",
        "Authors",
        "About",
    ]:
        fails.append(f"home: Browse menu lists {[b[0] for b in browse]}")

    # Two clicks: a link shown on home is one click; a Browse item is two.
    def target_of(href: str) -> str:
        return urlparse(href).path.strip("/").removeprefix(urlparse(base).path.strip("/"))

    btn = page.locator("header.bar .barmenu-btn")
    for coll in COLLECTIONS:
        go(page, base + "/")
        want = coll.rstrip("/")
        shown = page.locator(
            "header.bar .barnav > a.barlink, .homedoors a.card.door, nav.reflinks a"
        )
        hrefs = shown.evaluate_all("els => els.map(e => e.href)")
        hit = next((i for i, h in enumerate(hrefs) if target_of(h).strip("/") == want), None)
        clicks = 1
        if hit is not None:
            shown.nth(hit).click()
        else:
            items = page.locator("#barmenu-list a")
            ih = items.evaluate_all("els => els.map(e => e.href)")
            j = next((i for i, h in enumerate(ih) if target_of(h).strip("/") == want), None)
            if j is None:
                fails.append(f"home: {coll} is not linked from the bar, a door or the reference")
                continue
            btn.click()
            items.nth(j).click()
            clicks = 2
        try:
            page.wait_for_url(lambda u, w=want: target_of(u).strip("/") == w, timeout=8000)
        except PlaywrightTimeout:
            fails.append(f"home: {clicks} click(s) toward {coll} land on {page.url}")
            continue
        page.wait_for_load_state("networkidle")
        if not page.locator("h1").count():
            fails.append(f"home: {coll} has no title after {clicks} click(s)")

    # The menu by mouse: a click opens it, a second closes it, a click outside closes it.
    go(page, base + "/")
    lst = page.locator("#barmenu-list")

    def state() -> tuple[str | None, bool]:
        return btn.get_attribute("aria-expanded"), lst.is_visible()

    if state() != ("false", False):
        fails.append(f"home: the Browse menu starts {state()}")
    btn.click()
    if state() != ("true", True):
        fails.append(f"home: a click on Browse leaves {state()}")
    btn.click()
    if state() != ("false", False):
        fails.append(f"home: a second click on Browse leaves {state()}")
    btn.click()
    page.mouse.click(700, 600)
    if state() != ("false", False):
        fails.append(f"home: a click outside the Browse menu leaves {state()}")
    # The keyboard: Enter opens, arrows move through the items, Escape closes and refocuses.
    btn.focus()
    page.keyboard.press("Enter")
    if state() != ("true", True):
        fails.append(f"home: Enter on Browse leaves {state()}")
    page.keyboard.press("Escape")
    focused = page.evaluate("document.activeElement?.matches('.barmenu-btn')")
    if state() != ("false", False) or not focused:
        fails.append(f"home: Escape after Enter leaves {state()}, focus on Browse {focused}")
    page.keyboard.press("ArrowDown")
    first = page.evaluate("document.activeElement?.textContent.trim()")
    page.keyboard.press("ArrowDown")
    second = page.evaluate("document.activeElement?.textContent.trim()")
    page.keyboard.press("ArrowUp")
    page.keyboard.press("ArrowUp")
    wrapped = page.evaluate("document.activeElement?.textContent.trim()")
    labels = [b[0] for b in browse]
    if state() != ("true", True) or [first, second, wrapped] != [
        labels[0],
        labels[1],
        labels[-1],
    ]:
        fails.append(
            f"home: arrows on Browse focus {[first, second, wrapped]}, menu {state()}; "
            f"expected {labels[0]}, {labels[1]}, then {labels[-1]}"
        )
    page.keyboard.press("Escape")
    if state() != ("false", False) or not page.evaluate(
        "document.activeElement?.matches('.barmenu-btn')"
    ):
        fails.append("home: Escape inside the Browse menu does not close it and refocus Browse")
    # A tap opens it and a tap outside closes it.
    tap = browser.new_context(viewport=WIDE, has_touch=True, is_mobile=True).new_page()
    go(tap, base + "/")
    tbtn = tap.locator("header.bar .barmenu-btn")
    tlist = tap.locator("#barmenu-list")
    if tbtn.is_visible():
        tbtn.tap()
        opened = (tbtn.get_attribute("aria-expanded"), tlist.is_visible())
        tap.touchscreen.tap(700, 700)
        tap.wait_for_timeout(200)
        closed = (tbtn.get_attribute("aria-expanded"), tlist.is_visible())
        if opened != ("true", True) or closed != ("false", False):
            fails.append(f"home: a tap on Browse gives {opened}, a tap outside {closed}")
    else:
        fails.append("home: the Browse button is hidden on a touch screen at 1440 px")
    return fails


def check_strips(browser, base: str) -> list[str]:
    """The topic key, map and table on /topics/; picking a topic lights its map cluster;
    cards and map rows carry their topic's key colour."""
    fails: list[str] = []
    page = new_page(browser)
    go(page, base + "/topics/")
    for sel in ("[data-tkey]", "#topic-map[data-tmap]", ".topictable"):
        if page.locator(f".topicspage {sel}").count() != 1:
            fails.append(f"strips: /topics/ has {page.locator(f'.topicspage {sel}').count()} {sel}")
    topics = sorted(p.stem for p in (CONTENT / "topics").glob("*.md") if p.stem != "index")
    rows = page.eval_on_selector_all(
        ".topictable .trow .name a", "els => els.map(e => e.getAttribute('href'))"
    )
    if sorted(last_part(h) for h in rows) != topics:
        fails.append(f"strips: the topics table has {len(rows)} rows for {len(topics)} topics")
    slots = page.eval_on_selector_all(
        ".tkeyslot", "els => els.map(e => [e.dataset.t, e.style.getPropertyValue('--h')])"
    )
    hue = dict(slots)
    if sorted(hue) != topics:
        fails.append(f"strips: the key has slots {sorted(hue)}, the records {topics}")
    if not page.locator(".tkey").is_visible():
        fails.append("strips: the topic key is hidden with the script")

    def readout() -> str:
        """The key's visible readout: the topic shown, or 'idle'."""
        return page.evaluate(
            """() => {
            const info = [...document.querySelectorAll('.tinfo')].find(e => !e.hidden)
            return (info ? info.dataset.t : 'idle') + '|'
        }"""
        )

    lit_map = """() => [...document.querySelectorAll('[data-tmap] .cluster')]
        .filter(g => getComputedStyle(g).opacity > 0.5).map(g => g.dataset.t)"""
    page.mouse.move(0, 0)
    if readout() != "idle|":
        fails.append(f"strips: the key opens showing {readout()}")
    if not slots:
        return [*fails, "strips: the key has no slots"]
    hover = slots[-1][0]
    page.locator(f'.tkeyslot[data-t="{hover}"]').hover()
    if readout() != f"{hover}|":
        fails.append(f"strips: pointing at {hover} shows {readout()}")
    page.mouse.move(0, 0)
    topic = slots[0][0]
    page.locator(f'.tkeyslot[data-t="{topic}"]').click()
    page.wait_for_timeout(300)
    page.mouse.move(0, 0)
    # The Topics page has no strips, so the count line stays empty.
    if (text := readout()) != f"{topic}|":
        fails.append(f"strips: the key shows '{text}', expected '{topic}|'")
    pressed = page.eval_on_selector_all(
        ".tkeyslot[aria-pressed=true]", "els => els.map(e => e.dataset.t)"
    )
    if pressed != [topic]:
        fails.append(f"strips: picking {topic} presses key slots {pressed}")
    if (got := page.evaluate(lit_map)) != [topic]:
        fails.append(f"strips: picking {topic} leaves map clusters {got} bright")
    page.locator(".tmapgo").click()
    page.wait_for_timeout(800)
    if not page.evaluate(
        "(() => { const r = document.querySelector('[data-tmap]').getBoundingClientRect();"
        " return r.top < innerHeight && r.bottom > 0 })()"
    ):
        fails.append("strips: See it on the map does not bring the map into view")
    page.keyboard.press("Escape")
    page.wait_for_timeout(300)
    # Focus was on "See it on the map", which Escape hides, so it returns to the key slot.
    if page.evaluate("document.activeElement?.dataset?.t") != topic:
        fails.append("strips: Escape does not return focus to the topic's key slot")
    if len(got := page.evaluate(lit_map)) != page.locator("[data-tmap] .cluster").count():
        fails.append(f"strips: Escape leaves only map clusters {got} bright")
    page.locator(f'.tkeyslot[data-t="{topic}"]').click()
    page.locator(".tclear").click()
    page.wait_for_timeout(300)
    if page.evaluate("document.activeElement?.dataset?.t") != topic:
        fails.append("strips: Show all does not return focus to the topic's key slot")
    if len(page.evaluate(lit_map)) != page.locator("[data-tmap] .cluster").count():
        fails.append("strips: Show all leaves the map faded")

    nojs = new_page(browser, js=False)
    go(nojs, base + "/topics/")
    if nojs.locator(".tkey").is_visible():
        fails.append("strips: the topic key shows without the script")
    if not nojs.locator(".tintro").is_visible():
        fails.append("strips: the topic explanation is missing without the script")

    # The strips are gone; each card and map row takes its topic's key colour instead.
    seen = 0
    for path, card in (("/findings/", ".rcard"), ("/directions/", ".qcard")):
        go(page, base + path)
        cards = page.eval_on_selector_all(
            f".board .cards > {card}",
            "els => els.map(e => [e.dataset.fTopic, e.style.getPropertyValue('--d')])",
        )
        heads = page.eval_on_selector_all(
            ".nvrowh, .qrowh",
            """els => els.map(e => [
                (e.matches('a') ? e : e.querySelector('a'))?.getAttribute('href') || '',
                e.style.getPropertyValue('--d')])""",
        )
        for t, d in cards:
            seen += 1
            if hue.get(t) != d:
                fails.append(f"strips: {path} a {t} card has colour '{d}', the key '{hue.get(t)}'")
                break
        for h, d in heads:
            t = last_part(h)
            if t in hue and hue[t] != d:
                fails.append(f"strips: {path} row {t} has colour '{d}', the key '{hue[t]}'")
    if not seen:
        fails.append("strips: no board card to compare with the key")
    return fails


# ---------------------------------------------------------------- plain words

PLAIN_COUNTS: dict[str, int] = {}


def hit_lines(label: str, where: str, text: str) -> list[str]:
    out = []
    t = collapse(text)
    # The summary stage's rule: test statistics and wording such as "significant".
    if statistical(t):
        out.append(f"{label}: {where}: statistics in '{t[:90]}'")
    if re.search(r"\bcaveat\b", t, re.I):
        out.append(f"{label}: {where}: 'Caveat' in '{t[:90]}'")
    return out


CARDS = ".fcard, .cards > .card.rcard, .cards > .card.qcard"


def check_plain(browser, base: str) -> list[str]:
    fails: list[str] = []
    topics = ids("topics") if (ROOT / "wiki" / "topics").exists() else []
    paths = ["/", "/findings/", "/directions/"]
    paths += [f"/topics/{t}" for t in topics]
    paths += [f"/findings/{i}" for i in ids("findings")[:20]]
    paths += [f"/directions/{i}" for i in ids("directions")[:20]]
    page = new_page(browser)
    counts = {"card": 0, "chip": 0, "pop-up": 0, "question page": 0}
    for path in paths:
        resp = page.goto(base + path, wait_until="networkidle")
        if resp is None or resp.status != 200:
            fails.append(f"plain: {path}: HTTP {resp.status if resp else 'none'}")
            continue
        body = page.inner_text("body")
        # Pop-ups, folded details and column notes hold text a reader reveals; check it too.
        body += " ".join(
            page.eval_on_selector_all(
                ".qpop, details, .nvnote", "els => els.map(e => e.textContent)"
            )
        )
        for term in PIPELINE_TERMS:
            if term.lower() in body.lower():
                fails.append(f"plain: {path}: reader text contains '{term}'")
        if path.startswith("/directions/") and path != "/directions/":
            # A question page's own prose; linked result titles are checked as titles, and
            # a cited paper's title is quoted as published.
            for t in page.eval_on_selector_all(
                "article .markdown-rendered > p, article .markdown-rendered li",
                "els => els.filter(e => !e.querySelector('a[href*=\"pubmed\"]'))"
                ".map(e => { const c = e.cloneNode(true);"
                " c.querySelectorAll('a').forEach(a => a.remove()); return c.textContent })",
            ):
                counts["question page"] += 1
                fails += hit_lines("question page", path, t)
        # Titles are checked apart from bodies so a stored statistic title shows as its own finding.
        for t in page.eval_on_selector_all(
            ".fcard h3, .rcard .ct, .qcard .ct", "els => els.map(e => e.textContent)"
        ):
            fails += hit_lines("title", path, t)
        for sel, name in (
            (CARDS, "card"),
            (".chip, .chipwrap .note", "chip"),
            (".qpop", "pop-up"),
        ):
            texts = page.eval_on_selector_all(
                sel,
                """(els, name) => els.map(e => {
                    const c = e.cloneNode(true);
                    // The title and footer name results, reports and topics, not the card's words.
                    const skip = 'h3, .ct, .meta';
                    if (name === 'card') c.querySelectorAll(skip).forEach(h => h.remove());
                    // So do a pop-up's project and topic labels, such as "Statistical Confounding".
                    const labels = '.qpname, .qptopic';
                    if (name === 'pop-up') c.querySelectorAll(labels).forEach(h => h.remove());
                    return c.textContent;
                })""",
                name,
            )
            counts[name] += len(texts)
            if path in ("/findings/", "/directions/") and name == "card" and not texts:
                fails.append(f"plain: {path} has no board card to inspect")
            if path == "/directions/" and name == "pop-up" and not texts:
                fails.append("plain: /directions/ has no .qpop to inspect")
            for t in texts:
                fails += hit_lines(name, path, t)
    PLAIN_COUNTS.update(counts, pages=len(paths))
    return fails


# ---------------------------------------------------------------- questions grid

BAD: list[str] = []


def dot_expectations() -> dict[str, tuple[str, int]]:
    """Each question's topic slug and column index, from its record file."""
    out = {}
    for did in ids("directions"):
        fm = frontmatter(ROOT / "wiki" / "directions" / f"{did}.md")
        topics = fm.get("topics") or [""]
        readiness = fm.get("readiness", "unknown")
        if readiness not in NEED_COLUMN:
            print(f"grid: {did}: unknown readiness '{readiness}'")
            BAD.append(did)
        out[did] = (topics[0], NEED_COLUMN.get(readiness, -1))
    return out


def check_grid(browser, base: str) -> list[str]:
    fails: list[str] = []
    want = dot_expectations()
    fails += [f"grid: {d}: unknown readiness in record" for d in BAD]
    if not want:
        return ["grid: no direction records under wiki/directions"]

    nojs = new_page(browser, js=False)
    go(nojs, base + "/directions/")
    hrefs = nojs.eval_on_selector_all(".qgrid a.qdot", "els => els.map(e => e.href)")
    if len(hrefs) != len(want):
        fails.append(f"grid: no-JS page has {len(hrefs)} dots, expected {len(want)}")
    for h in hrefs:
        if (code := http_status(h)) != 200:
            fails.append(f"grid: dot link {h} returned HTTP {code}")

    page = new_page(browser)
    go(page, base + "/directions/")
    dots = page.eval_on_selector_all(
        ".qgrid a.qdot",
        """els => els.map(e => {
            const cell = e.closest('.qcell');
            const row = e.closest('.qrow');
            const cells = [...row.querySelectorAll('.qcell')];
            const h = row.querySelector('.qrowh a');
            return {
                id: e.getAttribute('href').split('/').pop(),
                col: cells.indexOf(cell),
                topic: h ? h.getAttribute('href').split('/').pop() : '',
            };
        })""",
    )
    if len(dots) != len(want):
        fails.append(f"grid: {len(dots)} dots, expected {len(want)}")
    for d in dots:
        exp = want.get(d["id"])
        if exp is None:
            fails.append(f"grid: dot {d['id']} has no record")
            continue
        topic, col = exp
        if d["topic"] != topic:
            fails.append(f"grid: {d['id']} in row '{d['topic']}', record says '{topic}'")
        if d["col"] != col:
            fails.append(f"grid: {d['id']} in column {d['col']}, record says {col}")

    # Hover, focus and tap each open a pop-up holding the title; Escape closes it.
    # The first unringed dot: no fading reaches its pop-up.
    first = page.locator(".qgrid .qd:not(.cross)").first
    dot = first.locator("a.qdot")
    pop = first.locator(".qpop")
    title = pop.locator("strong").first.text_content() or ""
    if not (dot.get_attribute("aria-label") or "").startswith(title):
        fails.append("grid: a dot's name does not start with its question")
    dot.scroll_into_view_if_needed()
    dot.hover()
    if not pop.is_visible() or title not in pop.inner_text():
        fails.append("grid: hover does not show the pop-up with the title")
    seen = pop.evaluate(
        "e => { let o = 1; for (let n = e; n; n = n.parentElement)"
        " o *= +getComputedStyle(n).opacity; return o }"
    )
    if seen < 1:
        fails.append(f"grid: a plain dot's pop-up is see-through (opacity {seen:.2f})")
    page.keyboard.press("Escape")
    if pop.is_visible():
        fails.append("grid: Escape does not close a hover pop-up")
    page.mouse.move(0, 0)
    dot.focus()
    if not pop.is_visible() or title not in pop.inner_text():
        fails.append("grid: focus does not show the pop-up with the title")
    page.keyboard.press("Escape")
    if pop.is_visible():
        fails.append("grid: Escape does not close a focus pop-up")
    page.evaluate("document.activeElement.blur()")
    page.mouse.move(0, 0)
    dot.click()
    page.mouse.move(0, 0)
    href = first.locator("a.qdot").get_attribute("href") or ""
    if href and page.url.rstrip("/").endswith(href.split("/")[-1]):
        fails.append("grid: clicking a dot navigated instead of pinning the pop-up")
    elif not pop.is_visible() or title not in pop.inner_text():
        fails.append("grid: click does not pin the pop-up (gone after the pointer left)")
    page.keyboard.press("Escape")
    if pop.is_visible():
        fails.append("grid: Escape does not close a pinned pop-up")

    # The pointer can move from any dot onto its pop-up. Ringed pop-ups scroll, which
    # once clipped the CSS bridge across the gap and closed them on the way. Focus left
    # on a dot after Escape keeps its pop-up shut, so it is cleared first.
    page.evaluate("document.activeElement.blur()")
    for sel in (".qgrid .qd.cross", ".qgrid .qd:not(.cross)"):
        wraps = page.locator(sel)
        if not wraps.count():
            fails.append(f"grid: no '{sel}' dot to walk onto")
        for i in range(min(8, wraps.count())):
            wrap = wraps.nth(i)
            why = walk_onto(page, wrap.locator("a.qdot"), wrap.locator(".qpop"))
            # Let the last pop-up close: a dot entered within 250 ms counts as a neighbour.
            page.mouse.move(0, 0)
            page.wait_for_timeout(400)
            if why:
                fails.append(f"grid: {sel.split()[-1]} dot {i + 1}: {why}")
                break
    # A pointer that jumps straight from one dot to another, outside the corridor to the
    # first pop-up, gets the second dot's pop-up and keeps it.
    a, z = page.locator(".qgrid .qd").nth(0), page.locator(".qgrid .qd").nth(12)
    jump = jump_to(page, a.locator("a.qdot"), z.locator("a.qdot"))
    if not z.locator(".qpop").is_visible() or a.locator(".qpop").is_visible():
        fails.append(f"grid: a jump between dots leaves the wrong pop-up ({jump})")

    # Tab from a focus-opened pop-up reaches its "Open the question" link (review F10).
    page.evaluate("document.activeElement.blur()")
    page.mouse.move(0, 0)
    dot.focus()
    page.keyboard.press("Tab")
    inside = page.evaluate("!!document.activeElement.closest('.qpop')")
    if not inside:
        fails.append("grid: Tab from a focused dot does not reach its pop-up's links")
    else:
        # Escape hides the pop-up holding focus, so focus returns to its dot.
        page.keyboard.press("Escape")
        if not page.evaluate("document.activeElement?.matches('a.qdot')") or pop.is_visible():
            fails.append("grid: Escape inside a pop-up does not close it and refocus its dot")
    # The approach left the dot's shape (M2); each dot's name and pop-up still carry it.
    qs = records()["questions"]
    names = page.eval_on_selector_all(
        ".qgrid .qd",
        "els => els.map(e => [e.dataset.id, e.querySelector('a.qdot').getAttribute('aria-label'),"
        " e.querySelector('.qpop .qneed')?.textContent || '',"
        " e.querySelector('a.qdot').hasAttribute('data-shape')])",
    )
    with_approach = 0
    for qid, name, need, shaped in names:
        approach = qs.get(qid, {}).get("approach_text", "")
        if shaped:
            fails.append(f"grid: dot {qid} still carries an approach shape")
            break
        if not approach:
            continue
        with_approach += 1
        if approach not in (name or "") or approach not in need:
            fails.append(f"grid: dot '{(name or '')[:50]}' does not name its approach")
            break
    if not with_approach:
        fails.append("grid: no dot has an approach to name")

    fails += question_legend_fails(browser, base)

    touch = browser.new_context(viewport=PHONE, has_touch=True, is_mobile=True).new_page()
    go(touch, base + "/directions/")
    td = touch.locator(".qgrid .qd:visible").first.locator("a.qdot")
    td.scroll_into_view_if_needed()
    td.tap()
    tpop = touch.locator(".qgrid .qd:visible").first.locator(".qpop")
    ttitle = tpop.locator("strong").first.text_content() or ""
    if not ttitle or not tpop.is_visible() or ttitle not in tpop.inner_text():
        fails.append("grid: tap does not open the pop-up with the title")
    # On a narrow phone a pop-up taller than the room above and below scrolls instead of
    # covering its dot, so a second tap on the dot closes it.
    small = browser.new_context(
        viewport={"width": 320, "height": 568}, has_touch=True, is_mobile=True
    ).new_page()
    go(small, base + "/directions/")
    small.wait_for_timeout(500)
    dots = small.locator(".qgrid .qd:visible a.qdot")
    for i in range(0, min(60, dots.count()), 5):
        d = dots.nth(i)
        d.scroll_into_view_if_needed()
        small.evaluate("y => scrollBy({top: y, behavior: 'instant'})", d.bounding_box()["y"] - 300)
        r = d.bounding_box()
        x, y = r["x"] + r["width"] / 2, r["y"] + r["height"] / 2
        small.touchscreen.tap(x, y)
        small.wait_for_timeout(250)
        small.touchscreen.tap(x, y)
        small.wait_for_timeout(250)
        if small.locator(".qd[data-open]").count():
            fails.append(f"grid: at 320 px a second tap on dot {i + 1} does not close its pop-up")
            break
        small.keyboard.press("Escape")

    for path in ("/", "/findings/", "/directions/", "/topics/"):
        narrow = new_page(browser, PHONE)
        go(narrow, base + path)
        sw, iw = narrow.evaluate("[document.documentElement.scrollWidth, window.innerWidth]")
        if sw > iw:
            fails.append(f"grid: {path} at 390 px scrollWidth {sw} > innerWidth {iw}")
    return fails


def question_legend_fails(browser, base: str) -> list[str]:
    """Legend dots share the grid's classes but are not questions: hovering or clicking one
    opens nothing and raises no page error (a click once threw a TypeError)."""
    fails: list[str] = []
    page, errors = watched(browser)
    go(page, base + "/directions/")
    keys = page.locator(".qlegend .qd.key")
    if not keys.count():
        return ["grid: the questions legend has no dot to try"]
    url = page.url
    for i in range(keys.count()):
        dot = keys.nth(i).locator(".qdot")
        dot.scroll_into_view_if_needed()
        dot.hover()
        page.wait_for_timeout(150)
        dot.click()
        page.wait_for_timeout(200)
        shown = page.evaluate(
            "() => [document.querySelectorAll('.qd[data-open], .qd[data-hover]').length,"
            " [...document.querySelectorAll('.qpop')].filter(e => e.getClientRects().length"
            " && getComputedStyle(e).display !== 'none').length]"
        )
        if shown != [0, 0] or page.url != url:
            fails.append(f"grid: legend dot {i + 1} opens {shown} (open, pop-ups), URL {page.url}")
        page.mouse.move(0, 0)
    fails += [f"grid: clicking a legend dot raises '{e}'" for e in errors]
    return fails


# ---------------------------------------------------------------- result pages and labels


def check_pages(browser, base: str) -> list[str]:
    fails: list[str] = []
    rec = records()
    page = new_page(browser)
    full = 0
    always = [h for h in FINDING_HEADINGS if h != RELATED_HEADING]
    for fid in ids("findings")[:10]:
        go(page, f"{base}/findings/{fid}")
        heads = page.eval_on_selector_all("h2", "els => els.map(e => e.textContent.trim())")
        order = [FINDING_HEADINGS.index(h) for h in heads if h in FINDING_HEADINGS]
        if order != sorted(order):
            fails.append(f"pages: {fid}: headings out of order: {heads}")
        for required in FINDING_HEADINGS[:3]:
            if required not in heads:
                fails.append(f"pages: {fid}: lacks '{required}': {heads}")
        full += all(h in heads for h in always)
    if not full:
        fails.append(f"pages: no checked finding page has all of {always}")

    go(page, base + "/findings/")
    h1 = page.eval_on_selector_all("h1", "els => els.map(e => e.textContent.trim())")
    if h1 != ["Results"]:
        fails.append(f"pages: /findings/ title {h1}, expected ['Results']")
    if page.locator(".c-chips").count():
        fails.append("pages: /findings/ still has the old .c-chips filter")
    # The board's kind chips, in legend order, for the kinds the listed results hold.
    kinds = {r["kind"] for r in rec["results"].values()}
    want = ["All"] + [w for k, w in KIND_WORDS.items() if k in kinds]
    row = ".board .px-tools .facets[data-k=kind]"
    chips = page.eval_on_selector_all(
        f"{row} .px-chip",
        "els => els.map(e => e.childNodes[0].textContent.trim()"
        " || e.textContent.replace(/\\d+$/, '').trim())",
    )
    if chips != want:
        fails.append(f"pages: /findings/ kind chips {chips}, expected {want}")
    # Filter chips say which is on and the group has a name (review F11).
    state = page.eval_on_selector_all(
        row,
        "els => els.map(g => [g.getAttribute('aria-label'), "
        "[...g.querySelectorAll('.px-chip')].map(b => b.getAttribute('aria-pressed'))])",
    )
    if not state or not state[0][0] or state[0][1][:1] != ["true"]:
        fails.append(f"pages: kind chips lack a group name or aria-pressed: {state}")
    page.locator(f"{row} .px-chip").nth(1).click()
    pressed = page.eval_on_selector_all(
        f"{row} .px-chip", "els => els.map(b => b.getAttribute('aria-pressed'))"
    )
    if pressed[:2] != ["false", "true"]:
        fails.append(f"pages: aria-pressed does not follow the chosen chip: {pressed}")

    # Each card's kind words come from its record; listed nulls read as one of two kinds.
    for i in sorted(rec["listed"]):
        fm = rec["findings"][i]
        if rec["results"][i]["kind"] != "null":
            continue
        if fm.get("kind_text") not in NULL_WORDS:
            fails.append(f"pages: listed null {i} reads '{fm.get('kind_text')}'")
        if fm.get("gist_case") in BAD_NULL_CASES:
            fails.append(f"pages: listed null {i} has case '{fm.get('gist_case')}'")
    go(page, base + "/findings/")
    words = page.eval_on_selector_all(
        ".board .cards > .rcard",
        "els => els.map(e => [e.dataset.id, e.querySelector('.rt')?.textContent.trim(),"
        " !!e.querySelector('.rt.null')])",
    )
    if len(words) != len(rec["listed"]):
        fails.append(f"pages: /findings/ has {len(words)} cards, records list {len(rec['listed'])}")
    for cid, said, hollow in words:
        fm = rec["findings"].get(cid, {})
        is_null = rec["results"].get(cid, {}).get("kind") == "null"
        if said != fm.get("kind_text") or hollow != is_null:
            fails.append(
                f"pages: card {cid} reads '{said}' (null {hollow}), record '{fm.get('kind_text')}'"
            )
            break

    # Both boards use the concepts card with square corners (6A).
    for path, n in (("/findings/", len(rec["listed"])), ("/directions/", len(rec["directions"]))):
        go(page, base + path)
        radii = page.eval_on_selector_all(
            ".board .cards > .card",
            "els => els.map(e => { const s = getComputedStyle(e); return [s.borderTopLeftRadius,"
            " s.borderTopRightRadius, s.borderBottomLeftRadius, s.borderBottomRightRadius] })",
        )
        if len(radii) != n:
            fails.append(f"pages: {path} has {len(radii)} .cards .card, expected {n}")
        rounded = [r for r in radii if any(v != "0px" for v in r)]
        if rounded:
            fails.append(f"pages: {path} {len(rounded)} cards have rounded corners {rounded[0]}")
    go(page, base + "/findings/")
    fails += chip_title_fails(page, "/findings/", minimum=1)
    for fid in ids("findings")[:10]:
        go(page, f"{base}/findings/{fid}")
        fails += chip_title_fails(page, f"/findings/{fid}")
    fails += contrast(browser, base, "pages")
    # No card footer shows its separator alone on a line at phone width (review P3c).
    narrow = new_page(browser, PHONE)
    for path in ("/findings/", "/directions/"):
        go(narrow, base + path)
        lone = narrow.evaluate(
            "[...document.querySelectorAll('.board .card .meta > span')]"
            ".filter(e => !e.textContent.trim()).length"
        )
        if lone:
            fails.append(f"pages: {path} {lone} card footers have a separator with no words")
    topic = next(iter(ids("topics")), None) if (ROOT / "wiki" / "topics").exists() else None
    if topic:
        go(narrow, f"{base}/topics/{topic}")
        lone = narrow.evaluate(
            "[...document.querySelectorAll('.fcard .meta > *')]"
            ".filter(e => e.textContent.trim() === '·').length"
        )
        if lone:
            fails.append(f"pages: /topics/{topic} {lone} card footers have a separator on its own")
    return fails


def chip_title_fails(page: Page, where: str, minimum: int = 0) -> list[str]:
    """Every comparison chip button with a note carries the note as its title (hover), and on
    a board the note is the card's record chip_note."""
    fails: list[str] = []
    rec = records()
    chips = page.eval_on_selector_all(
        ".chipwrap:has(> .note)",
        "els => els.map(e => [e.querySelector(':scope > button.chip')?.getAttribute('title'),"
        " e.querySelector(':scope > .note').textContent, e.closest('.card')?.dataset.id || ''])",
    )
    for title, note, cid in chips:
        if title is None or collapse(title) != collapse(note):
            fails.append(f"pages: {where} a chip's title '{title}' is not its note '{note[:60]}'")
            break
        want = rec["findings"].get(cid, {}).get("chip_note") if cid else None
        if want is not None and collapse(want) != collapse(note):
            fails.append(f"pages: {where} card {cid} chip note differs from its record")
            break
    if len(chips) < minimum:
        fails.append(f"pages: {where} has {len(chips)} chips with a note, expected some")
    return fails


def check_contrast(browser, base: str) -> list[str]:
    return contrast(browser, base, "contrast")


def contrast(browser, base: str, label: str) -> list[str]:
    """Small labels reach 4.5:1 against their background in light mode (review F13)."""
    fails = []
    found: set[str] = set()
    probe = """sels => sels.flatMap(sel => [...document.querySelectorAll(sel)]
      .filter(e => e.getClientRects().length && getComputedStyle(e).visibility !== 'hidden')
      .slice(0, 3).map(e => {
        // The first opaque background up the tree; tints with alpha are skipped.
        let bg = 'rgb(255, 255, 255)', n = e;
        while (n) {
            const c = getComputedStyle(n).backgroundColor;
            const alpha = c.match(/[\\d.]+(?=\\)$)/);
            const opaque = c.startsWith('rgb(') || (alpha && Number(alpha[0]) === 1);
            if (opaque) { bg = c; break; }
            n = n.parentElement;
        }
        return [sel, getComputedStyle(e).color, bg];
    }))"""
    for viewport, sels in ((DESKTOP, LIGHT_LABELS), (PHONE, PHONE_LABELS)):
        page = browser.new_context(viewport=viewport, color_scheme="light").new_page()
        topic = next(iter(ids("topics")), "") if (ROOT / "wiki" / "topics").exists() else ""
        for path in ("/", "/findings/", "/directions/", f"/topics/{topic}"):
            go(page, base + path)
            for sel, fg, bg in page.evaluate(probe, sels):
                found.add(sel)
                r = ratio(rgba(fg), rgba(bg))
                if r < 4.5:
                    fails.append(f"{label}: {path} {sel} contrast {r:.2f}:1 ({fg} on {bg})")
    missing = [s for s in LIGHT_LABELS + PHONE_LABELS if s not in found]
    if missing:
        fails.append(f"{label}: no label found to measure for {missing}")
    return sorted(set(fails))


# ---------------------------------------------------------------- the Results map

# Quartz's own diagram script looks for a `.center` element this theme does not render;
# that error predates these pages and is reported apart from theirs.
QUARTZ_MERMAID = "static/resource-after-"


def watched(browser, viewport=DESKTOP, scheme="light") -> tuple[Page, list[str]]:
    errors: list[str] = []
    page = browser.new_context(viewport=viewport, color_scheme=scheme).new_page()
    page.on(
        "pageerror",
        lambda e: None if QUARTZ_MERMAID in (e.stack or "") else errors.append(str(e)),
    )
    page.on("console", lambda m: m.type == "error" and errors.append(m.text))
    return page, errors


BOXES_JS = """() => {
    const out = []
    let topic = ''
    for (const ch of document.querySelector('.nvgrid').children) {
        if (ch.matches('.nvrowh'))
            topic = new URL(ch.href).pathname.replace(/\\/$/, '').split('/').pop()
        if (!ch.matches('.nvcell')) continue
        const lab = ch.querySelector('.nvlab')
        const text = lab?.textContent || ''
        const col = (lab?.querySelector('.nvnoteb')?.childNodes[0].textContent
            ?? text.split(' · ')[0]).trim()
        const n = text.split(' · ').pop()
        for (const b of ch.querySelectorAll('.nbead'))
            out.push({p: b.dataset.p, topic, col, n, label: b.getAttribute('aria-label') || '',
                      ids: [...b.querySelectorAll('.nd')].map(d => d.dataset.id)})
    }
    return out
}"""


def box_fails(page: Page, label: str) -> list[str]:
    """Each project box sits in its records' row and column and holds exactly their results."""
    rec = records()
    got = page.evaluate(BOXES_JS)
    fails = []
    seen = set()
    for b in got:
        key = (b["topic"], b["col"], b["p"])
        seen.add(key)
        want = sorted(rec["boxes"].get(key, []))
        if sorted(b["ids"]) != want:
            fails.append(f"{label}: box {key} holds {sorted(b['ids'])}, records give {want}")
    missing = set(rec["boxes"]) - seen
    if missing:
        fails.append(
            f"{label}: {len(missing)} record boxes have no box on the map: {sorted(missing)[:3]}"
        )
    if not got:
        fails.append(f"{label}: the map has no project box")
    return fails


def check_cross(browser, base: str) -> list[str]:
    """The Results map against its records, hover cards, related-result lines (4B), the box
    list, column notes, Compare panels and ringed question bridges (done check 4)."""
    fails: list[str] = []
    rec = records()
    page, errors = watched(browser)
    go(page, base + "/findings/")
    heads = page.eval_on_selector_all("h2", "els => els.map(e => e.textContent.trim())")
    if "How new is each result?" not in heads:
        fails.append(f"cross: /findings/ headings {heads} lack 'How new is each result?'")
    text = page.inner_text("body")
    for gone in ["Results several projects reached", *GONE_FAMILIES]:
        if gone in text:
            fails.append(f"cross: /findings/ still says '{gone}'")
    for sel in (".scard", ".fcard"):
        if n := page.locator(sel).count():
            fails.append(f"cross: /findings/ still has {n} '{sel}'")
    cols = page.eval_on_selector_all(
        ".nvcolh",
        "els => els.map(e => (e.querySelector('.nvnoteb')?.childNodes[0].textContent"
        " || e.childNodes[1]?.textContent || '').trim())",
    )
    if cols != rec["cols"]:
        fails.append(f"cross: map columns {cols}, records give {rec['cols']}")

    # Compare buttons: one on each listed member of a shared group with two or more.
    groups = [
        g
        for g in rec["index"].get("shared") or []
        if sum(m["id"] in rec["listed"] for m in g["members"]) >= 2
    ]
    sharing = {m["id"] for g in groups for m in g["members"] if m["id"] in rec["listed"]}
    with_cmp = page.eval_on_selector_all(
        ".board .cards > .rcard:has(.ccmp)", "els => els.map(e => e.dataset.id)"
    )
    if set(with_cmp) != sharing or not sharing:
        fails.append(
            f"cross: {len(with_cmp)} cards have Compare, the records share {len(sharing)}; "
            f"extra {sorted(set(with_cmp) - sharing)[:3]}, "
            f"missing {sorted(sharing - set(with_cmp))[:3]}"
        )
    titles = sorted((rec["index"].get("project_titles") or {}).values(), key=len, reverse=True)
    buttons = page.locator(".board .cards > .rcard .ccmp")
    for i in range(buttons.count()):
        b = buttons.nth(i)
        cid = b.evaluate("e => e.closest('.card').dataset.id")
        card = page.locator(f'.board .cards > .rcard[data-id="{cid}"]')
        b.scroll_into_view_if_needed()
        b.click()
        panel = page.locator(".spanel:not([hidden])")
        if panel.count() != 1:
            fails.append(f"cross: Compare {i + 1} opens {panel.count()} panels")
            continue
        if panel.get_attribute("id") != b.get_attribute("aria-controls"):
            fails.append(f"cross: Compare {i + 1} opens another group's panel")
        if b.get_attribute("aria-expanded") != "true":
            fails.append(f"cross: Compare {i + 1} does not say it is expanded")
        # The panel opens under its card's row: no card sits between the two.
        top = panel.bounding_box()["y"]
        cb = card.bounding_box()
        between = page.evaluate(
            "([lo, hi]) => [...document.querySelectorAll('.board .cards > .card:not(.px-hidden)')]"
            ".map(c => c.getBoundingClientRect().y).filter(y => y > lo && y < hi).length",
            [cb["y"] + 1, top],
        )
        if top < cb["y"] + cb["height"] - 1 or between:
            fails.append(f"cross: Compare {i + 1} panel opens {between} cards below its card")
        lanes = panel.locator(".slane").count()
        projects = len(set(panel.locator(".ssrc").evaluate_all("els => els.map(e => e.href)")))
        if lanes < 2 or projects < 2:
            fails.append(f"cross: Compare {i + 1} panel has {lanes} lanes from {projects} projects")
        # The statement's own words, not its member results' titles and summaries, which
        # can say "independent" about biology.
        own = panel.evaluate(
            "e => { const c = e.cloneNode(true); c.querySelectorAll('.smini')"
            ".forEach(m => m.remove()); return c.textContent }"
        )
        said = card.locator(".crel").inner_text() + " " + own
        # Report titles name methods ("Independent Component Analysis"), not a relation.
        for title in titles:
            said = said.replace(title, "")
        if hit := CONFIRM.search(said):
            fails.append(f"cross: Compare {i + 1} says '{hit[0]}'")
        b.click()
        if page.locator(".spanel:not([hidden])").count():
            fails.append(f"cross: a second click on Compare {i + 1} leaves its panel open")

    go(page, base + "/directions/")
    if page.locator("details.qall").count() or "as a list" in page.inner_text("body"):
        fails.append("cross: /directions/ still has the 'All N as a list' details")
    rings = page.locator(".qgrid .qd.cross")
    crossing = sum(q["cross"] for q in rec["questions"].values())
    if rings.count() != crossing or not crossing:
        fails.append(f"cross: {rings.count()} ringed questions, the records give {crossing}")
    for i in range(rings.count()):
        projects = rings.nth(i).locator(".qproj")
        links = [projects.nth(j).locator(".qpres a").count() for j in range(projects.count())]
        if len(links) < 2 or min(links) < 1:
            fails.append(f"cross: ringed question {i + 1} bridge has projects {links}")

    go(page, base + "/findings/")
    dots = page.locator(".nvgrid .nd").count()
    if dots != len(rec["listed"]):
        fails.append(f"cross: picture has {dots} marks; the records list {len(rec['listed'])}")
    fails += box_fails(page, "cross")
    # Each cell's label counts the marks in it.
    cells = page.eval_on_selector_all(
        ".nvgrid .nvcell",
        "els => els.map(e => [e.querySelector('.nvlab')?.textContent || '',"
        " e.querySelectorAll('.nd').length])",
    )
    for lab, n in cells:
        if not lab.endswith(f"· {n}"):
            fails.append(f"cross: a cell labelled '{lab}' holds {n} marks")
            break
    if page.locator("svg.nvlinks path").count():
        fails.append("cross: links are drawn before any interaction")
    # A result's card follows the questions grid: it stays, on the same result, while the
    # pointer moves onto it past neighbouring dots; a click pins it without pinning the
    # project; a pinned card survives hovering other dots and a resize, until Escape.
    card = page.locator(".nvtip:not(.pin)")
    pinned = page.locator(".nvtip.pin")
    marks = page.locator(".nvgrid .nd")
    href_of = "id => JSON.parse(document.querySelector('.nvdata').textContent).findings[id]"
    why, aim = "", "link"
    for i in range(0, min(60, marks.count()), 3):
        want = page.evaluate(href_of, marks.nth(i).get_attribute("data-id"))
        for aim in ("link", "head"):
            why = walk_onto(page, marks.nth(i), card, want, aim)
            page.mouse.move(0, 0)
            page.wait_for_timeout(400)
            if why:
                break
        if why:
            fails.append(f"cross: result dot {i + 1}, walking to the {aim}: {why}")
            break
    first, second = marks.nth(0), marks.nth(1)
    want = page.evaluate(href_of, first.get_attribute("data-id"))
    first.click()
    page.mouse.move(0, 0)
    page.wait_for_timeout(400)
    if not pinned.is_visible():
        fails.append("cross: clicking a result dot does not pin its card")
    elif pinned.locator("a.nvopen").get_attribute("href") != want:
        fails.append("cross: a result card's link does not open its result")
    if page.locator(".nvpanel:not([hidden])").count():
        fails.append("cross: clicking a result dot also pins its project's links")
    second.hover()
    page.mouse.move(0, 0)
    page.wait_for_timeout(400)
    if not pinned.is_visible() or pinned.locator("a.nvopen").get_attribute("href") != want:
        fails.append("cross: hovering another dot replaces or closes a pinned card")
    page.set_viewport_size({"width": 900, "height": 900})
    page.wait_for_timeout(300)
    b = pinned.bounding_box() if pinned.count() else None
    if not b or b["x"] < 0 or b["x"] + b["width"] > 900:
        fails.append(f"cross: a pinned card leaves the screen after a resize: {b}")
    page.set_viewport_size(DESKTOP)
    page.keyboard.press("Escape")
    if pinned.is_visible():
        fails.append("cross: Escape does not close a pinned result card")
    # The target must lie outside the first card: a pointer landing on the card keeps it.
    marks.nth(0).hover()
    page.wait_for_timeout(200)
    t = card.bounding_box()
    far = next(
        marks.nth(i)
        for i in range(1, marks.count())
        if (b := marks.nth(i).bounding_box())
        and not (t["x"] - 20 < b["x"] < t["x"] + t["width"] + 20)
        and abs(b["y"] - t["y"]) < 300
    )
    jump = jump_to(page, marks.nth(0), far)
    want = page.evaluate(href_of, far.get_attribute("data-id"))
    if not card.is_visible() or card.locator("a.nvopen").get_attribute("href") != want:
        fails.append(f"cross: a jump between result dots leaves the wrong card ({jump})")
    page.mouse.move(0, 0)
    page.wait_for_timeout(400)
    # On a narrow phone a pinned card must not cover its dot: a second tap closes it.
    small = browser.new_context(
        viewport={"width": 320, "height": 568}, has_touch=True, is_mobile=True
    ).new_page()
    go(small, base + "/findings/")
    small.wait_for_timeout(500)
    sdot = small.locator(".nvgrid .nd").first
    sdot.scroll_into_view_if_needed()
    small.evaluate("y => scrollBy(0, y)", sdot.bounding_box()["y"] - 450)
    sdot.tap()
    small.wait_for_timeout(300)
    url = small.url
    # Tap the screen point, as a finger does; a locator tap would route around a covering card.
    r = sdot.bounding_box()
    small.touchscreen.tap(r["x"] + r["width"] / 2, r["y"] + r["height"] / 2)
    small.wait_for_timeout(500)
    if small.url != url or small.locator(".nvtip.pin").is_visible():
        fails.append("cross: at 320 px a second tap on a result dot does not close its card")
    tap = browser.new_context(viewport=PHONE, has_touch=True, is_mobile=True).new_page()
    go(tap, base + "/findings/")
    tap.wait_for_timeout(500)
    dot = tap.locator(".nvgrid .nd").first
    dot.scroll_into_view_if_needed()
    dot.tap()
    tap.wait_for_timeout(300)
    tcard = tap.locator(".nvtip.pin")
    if not tcard.is_visible() or not tcard.locator("a.nvopen").count():
        fails.append("cross: a tap on a result dot does not open its card, as on questions")
    rows = page.eval_on_selector_all(".nvrowh", "els => els.map(e => e.textContent.trim())")
    infra = [r for r in rows if r.startswith("Data Infrastructure")]
    filed = sum(
        r["topic"] == "data-infrastructure-provenance-and-research-practice"
        for r in rec["results"].values()
    )
    if not infra or not infra[0].endswith(f" {filed}"):
        fails.append(f"cross: Data Infrastructure row reads {infra}, expected {filed}")
    fails += line_fails(page, "cross")
    fails += note_fails(page, "cross")
    fails += pinned_note_fails(page, "cross")
    fails += legend_inert_fails(page, "cross")
    fails += heading_link_fails(page, base, "cross")
    fails += compare_place_fails(browser, base, "cross")
    fails += phone_note_fails(browser, base, "cross")
    fails += nojs_compare_fails(browser, base, "cross")

    # A comparison still opens after navigating away and back: Quartz reuses nodes,
    # so a second set of listeners would open and close it in one click.
    go(page, base + "/")
    page.locator("a.card.door[href$='findings/']").first.click()
    page.wait_for_url("**/findings/**")
    page.wait_for_selector(".ccmp")
    page.locator("a.nvrowh").first.click()
    page.wait_for_url("**/topics/**")
    page.go_back()
    page.wait_for_selector(".ccmp")
    page.wait_for_timeout(300)
    page.locator(".ccmp").first.click()
    if page.locator(".spanel:not([hidden])").count() != 1:
        fails.append("cross: a comparison does not open after navigating away and back")
    fails += [f"cross: light: {e}" for e in errors]

    dark, dark_errors = watched(browser, scheme="dark")
    for path in ("/", "/findings/", "/directions/", "/topics/"):
        go(dark, base + path)
    fails += [f"cross: dark: {e}" for e in dark_errors]
    for path in ("/", "/findings/", "/directions/", "/topics/"):
        narrow, narrow_errors = watched(browser, PHONE)
        go(narrow, base + path)
        sw, iw = narrow.evaluate("[document.documentElement.scrollWidth, window.innerWidth]")
        if sw > iw:
            fails.append(f"cross: {path} at 390 px scrollWidth {sw} > innerWidth {iw}")
        fails += [f"cross: phone {path}: {e}" for e in narrow_errors]
        if path == "/directions/":
            # Every ringed bridge stays inside the screen when tapped on a touch screen,
            # which has no hover. A tap before the page script wires the grid would follow
            # the dot's link instead.
            touch = browser.new_context(viewport=PHONE, has_touch=True, is_mobile=True).new_page()
            go(touch, base + path)
            touch.wait_for_timeout(500)
            rings = touch.locator(".qgrid .qd.cross:visible a.qdot")
            for i in range(rings.count()):
                rings.nth(i).scroll_into_view_if_needed()
                rings.nth(i).tap()
                box = touch.locator(".qd[data-open] .qpop").bounding_box(timeout=5000)
                if not box or box["x"] < 0 or box["x"] + box["width"] > PHONE["width"]:
                    fails.append(f"cross: ringed pop-up {i + 1} leaves the screen: {box}")
                    break
                touch.keyboard.press("Escape")
    return fails


def line_fails(page: Page, label: str) -> list[str]:
    """Hovering or focusing a box draws one solid line per related-result link of its
    results, dot to dot; a click on its edge or Enter lists its results and their related
    results; Escape clears."""
    fails: list[str] = []
    rec = records()
    boxes = page.evaluate(BOXES_JS)
    ringed = [b for b in boxes if any(rec["results"].get(i, {}).get("rel") for i in b["ids"])]
    plain = [b for b in boxes if not any(rec["results"].get(i, {}).get("rel") for i in b["ids"])]
    if not ringed:
        return [f"{label}: no box holds a ringed result"]
    titles = rec["index"].get("project_titles") or {}
    for n, b in enumerate(ringed[:4]):
        mine = set(b["ids"])
        want = [lk for lk in rec["links"] if lk["a"] in mine or lk["b"] in mine]
        loc = page.locator(".nvgrid .nbead").filter(
            has=page.locator(f'.nd[data-id="{b["ids"][0]}"]')
        )
        loc.scroll_into_view_if_needed()
        loc.hover(position={"x": 2, "y": 2})
        page.wait_for_timeout(150)
        drawn = page.evaluate(
            """links => {
            const box = document.querySelector('.nvbox'), f = box.getBoundingClientRect()
            const at = id => { const r = document.querySelector(`.nvgrid .nd[data-id="${id}"]`)
                .getBoundingClientRect(); return [r.left + r.width / 2 - f.left + box.scrollLeft,
                r.top + r.height / 2 - f.top + box.scrollTop] }
            const paths = [...document.querySelectorAll('svg.nvlinks path')]
            return { paths: paths.map(p =>
                         [p.getAttribute('d'), getComputedStyle(p).strokeDasharray]),
                     want: links.map(l => [at(l.a), at(l.b)]) }
        }""",
            want,
        )
        hovered = len(drawn["paths"])
        if hovered != len(want):
            fails.append(
                f"{label}: hovering box {b['p']} draws {hovered} lines, records give {len(want)}"
            )
        for (d, dash), (pa, pb) in zip(drawn["paths"], drawn["want"], strict=False):
            nums = [float(x) for x in re.findall(r"-?[\d.]+", d)]
            ends = (nums[:2], nums[-2:])
            if any(abs(u - v) > 1 for u, v in zip([*ends[0], *ends[1]], [*pa, *pb], strict=True)):
                fails.append(f"{label}: box {b['p']} line '{d[:40]}' does not run dot to dot")
                break
            if dash not in ("none", ""):
                fails.append(f"{label}: box {b['p']} draws a dashed line ({dash})")
                break
        page.mouse.move(0, 0)
        page.wait_for_timeout(150)
        if page.locator("svg.nvlinks path").count():
            fails.append(f"{label}: lines stay after the pointer leaves box {b['p']}")
        loc.focus()
        focused = page.locator("svg.nvlinks path").count()
        if focused != len(want):
            fails.append(f"{label}: focusing box {b['p']} draws {focused} lines of {len(want)}")
        # Enter on the first box, a click on its edge for the others.
        if n == 0:
            page.keyboard.press("Enter")
        else:
            loc.click(position={"x": 2, "y": 2})
        panel = page.locator(".nvpanel")
        if not panel.is_visible():
            fails.append(
                f"{label}: {'Enter on' if n == 0 else 'a click on the edge of'} "
                f"box {b['p']} lists nothing"
            )
            page.keyboard.press("Escape")
            continue
        listed = panel.locator("ul.nvresults li a").evaluate_all(
            "els => els.map(e => e.getAttribute('href'))"
        )
        if sorted(last_part(h) for h in listed) != sorted(mine):
            fails.append(f"{label}: box {b['p']} list shows {len(listed)} results of {len(mine)}")
        if panel.locator("h4").inner_text().strip() != titles.get(b["p"], b["p"]):
            fails.append(
                f"{label}: box {b['p']} list is headed '{panel.locator('h4').inner_text()}'"
            )
        others = sorted(lk["b"] if lk["a"] in mine else lk["a"] for lk in want)
        shown = panel.locator("ul.nvlist li > a").evaluate_all(
            "els => els.map(e => e.getAttribute('href'))"
        )
        fam = panel.locator(".nvfam").text_content() if panel.locator(".nvfam").count() else ""
        if (
            sorted(last_part(h) for h in shown) != others
            or fam != f"{RELATED_HEADING} · {len(want)}"
        ):
            fails.append(
                f"{label}: box {b['p']} lists related {shown} under '{fam}', records give {others}"
            )
        page.keyboard.press("Escape")
        back = page.evaluate("document.activeElement?.dataset?.p")
        if panel.is_visible() or back != b["p"]:
            fails.append(
                f"{label}: Escape leaves box {b['p']}'s list open {panel.is_visible()}, "
                f"focus on {back}"
            )
        page.evaluate("document.activeElement?.blur()")
        page.wait_for_timeout(100)
        if page.locator("svg.nvlinks path").count():
            fails.append(f"{label}: box {b['p']}'s lines stay after Escape and blur")
    if plain:
        loc = page.locator(".nvgrid .nbead").filter(
            has=page.locator(f'.nd[data-id="{plain[0]["ids"][0]}"]')
        )
        loc.scroll_into_view_if_needed()
        loc.click(position={"x": 2, "y": 2})
        said = (
            page.locator(".nvpanel").text_content() if page.locator(".nvpanel").is_visible() else ""
        )
        if "No related result in another project yet." not in said:
            fails.append(f"{label}: a box without related results lists '{said[:80]}'")
        page.keyboard.press("Escape")
    return fails


LINES_JS = """links => {
    const box = document.querySelector('.nvbox'), f = box.getBoundingClientRect()
    const at = id => { const r = document.querySelector(`.nvgrid .nd[data-id="${id}"]`)
        .getBoundingClientRect(); return [r.left + r.width / 2 - f.left + box.scrollLeft,
        r.top + r.height / 2 - f.top + box.scrollTop] }
    const paths = [...document.querySelectorAll('svg.nvlinks path')]
    return { paths: paths.map(p =>
                 [p.getAttribute('d'), getComputedStyle(p).strokeDasharray]),
             want: links.map(l => [at(l.a), at(l.b)]) }
}"""


def line_offsets(page: Page, links: list[dict]) -> tuple[int, float]:
    """How many lines are drawn, and the furthest any endpoint lies from its mark's centre."""
    drawn = page.evaluate(LINES_JS, links)
    worst = 0.0
    for (d, _), (pa, pb) in zip(drawn["paths"], drawn["want"], strict=False):
        nums = [float(x) for x in re.findall(r"-?[\d.]+", d)]
        ends = [*nums[:2], *nums[-2:]]
        worst = max(worst, *(abs(u - v) for u, v in zip(ends, [*pa, *pb], strict=True)))
    return len(drawn["paths"]), worst


def pinned_note_fails(page: Page, label: str) -> list[str]:
    """With a box pinned, opening or closing a column note grows the header row; the box's
    lines must still run from mark centre to mark centre (within 2 px)."""
    fails: list[str] = []
    rec = records()
    ringed = [
        b
        for b in page.evaluate(BOXES_JS)
        if any(rec["results"].get(i, {}).get("rel") for i in b["ids"])
    ]
    if not ringed:
        return [f"{label}: no ringed box to pin"]
    b = ringed[0]
    want = [lk for lk in rec["links"] if lk["a"] in b["ids"] or lk["b"] in b["ids"]]
    box = page.locator(".nvgrid .nbead").filter(has=page.locator(f'.nd[data-id="{b["ids"][0]}"]'))
    box.scroll_into_view_if_needed()
    box.click(position={"x": 2, "y": 2})
    page.mouse.move(0, 0)
    notes = page.locator(".nvcolh .nvnoteb")
    if not notes.count():
        fails.append(f"{label}: no column note to open with a box pinned")
    for i in range(notes.count()):
        for step in ("opening", "closing"):
            notes.nth(i).click()
            page.wait_for_timeout(150)
            n, worst = line_offsets(page, want)
            if n != len(want) or worst > 2:
                fails.append(
                    f"{label}: {step} column note {i + 1} with box {b['p']} pinned leaves "
                    f"{n} of {len(want)} lines, an end {worst:.1f} px off its mark"
                )
    page.keyboard.press("Escape")
    page.evaluate("document.activeElement?.blur()")
    page.mouse.move(0, 0)
    return fails


MAP_STATE_JS = """() => ({
    cards: [...document.querySelectorAll('.nvtip')].filter(e => !e.hidden).length,
    panel: !document.querySelector('.nvpanel')?.hidden,
    sel: document.querySelectorAll('.nvbox.sel, .nbead.me, .nbead.nb').length,
    lines: document.querySelectorAll('svg.nvlinks path').length,
    on: document.querySelectorAll('.nd.on').length,
})"""


def legend_inert_fails(page: Page, label: str) -> list[str]:
    """The legend draws the map's marks and an example box, but they are not map items:
    hovering or clicking any of them opens no card or panel and selects nothing."""
    fails: list[str] = []
    page.keyboard.press("Escape")
    page.mouse.move(0, 0)
    page.wait_for_timeout(300)
    idle = {"cards": 0, "panel": False, "sel": 0, "lines": 0, "on": 0}
    if (st := page.evaluate(MAP_STATE_JS)) != idle:
        return [f"{label}: the map is not idle before the legend test: {st}"]
    items = page.locator(".nvlegend .nd, .nvlegend .nbead.key")
    if not items.count():
        return [f"{label}: the Results legend has no mark to try"]
    for i in range(items.count()):
        item = items.nth(i)
        what = item.evaluate("e => e.className + ' ' + (e.dataset.k || '')").strip()
        item.scroll_into_view_if_needed()
        for act in ("hover", "click"):
            item.hover() if act == "hover" else item.click()
            page.wait_for_timeout(200)
            if (st := page.evaluate(MAP_STATE_JS)) != idle:
                fails.append(f"{label}: a {act} on legend item '{what}' gives {st}")
        page.mouse.move(0, 0)
        page.keyboard.press("Escape")
        page.wait_for_timeout(200)
    return fails


def heading_link_fails(page: Page, base: str, label: str) -> list[str]:
    """Every box's list is headed by a link to its project's report page; plain text is
    allowed only where no report page exists."""
    fails: list[str] = []
    boxes = page.locator(".nvgrid .nbead")
    heads: dict[str, str | None] = {}
    for i in range(boxes.count()):
        b = boxes.nth(i)
        sid = b.get_attribute("data-p") or ""
        if sid in heads:
            continue
        b.scroll_into_view_if_needed()
        b.click(position={"x": 2, "y": 2})
        head = page.locator(".nvpanel h4")
        if not page.locator(".nvpanel").is_visible() or not head.count():
            fails.append(f"{label}: a click on box {sid} lists nothing")
            continue
        link = head.locator("a")
        heads[sid] = link.evaluate("a => a.href") if link.count() else None
    page.keyboard.press("Escape")
    page.evaluate("document.activeElement?.blur()")
    if len(heads) != len({k[2] for k in records()["boxes"]}):
        fails.append(f"{label}: read {len(heads)} box headings, the records have more projects")
    for sid, href in sorted(heads.items()):
        if href is None:
            if (code := http_status(f"{base}/summaries/{sid}")) == 200:
                fails.append(f"{label}: box {sid} heading is plain text, but its report exists")
            continue
        path = urlparse(href).path.rstrip("/")
        if href.endswith("#") or not path.endswith(f"summaries/{sid}"):
            fails.append(f"{label}: box {sid} heading links to {href}")
        elif (code := http_status(href)) != 200:
            fails.append(f"{label}: box {sid} heading link {href} returned HTTP {code}")
    return fails


ROW_JS = """id => {
    const card = document.querySelector(`.board .cards > .card[data-id="${id}"]`)
    const kids = [...card.parentElement.children]
    return kids.filter(c => c.matches('.card:not(.px-hidden)')
        && Math.abs(c.offsetTop - card.offsetTop) < 1).map(c => c.dataset.id)
}"""
AFTER_JS = """id => {
    const card = document.querySelector(`.board .cards > .card[data-id="${id}"]`)
    const p = document.querySelector('.spanel:not([hidden])')
    const kids = [...card.parentElement.children]
    return { inGrid: !!p && p.parentElement === card.parentElement,
             order: kids.map(c => c === p ? '#panel' : c.dataset.id || ''),
             prev: p?.previousElementSibling?.dataset?.id || '',
             cols: getComputedStyle(card.parentElement).gridTemplateColumns.split(' ').length }
}"""


def compare_place_fails(browser, base: str, label: str) -> list[str]:
    """After each sort, Compare opens its panel right after the last card of the opener's
    row, with no card of that row after it; resized from three columns to one, the panel
    follows its opener."""
    fails: list[str] = []
    page = new_page(browser)
    go(page, base + "/findings/")
    buttons = page.locator(".board .cards > .rcard .ccmp")
    ids_ = buttons.evaluate_all("els => els.map(e => e.closest('.card').dataset.id)")
    if not ids_:
        return [f"{label}: no Compare button to place"]
    tested = 0
    for sort in ("project", "topic"):
        page.locator(".px-tools select").select_option(sort)
        page.wait_for_timeout(200)
        for cid in ids_:
            row = page.evaluate(ROW_JS, cid)
            btn = page.locator(f'.board .cards > .rcard[data-id="{cid}"] .ccmp')
            btn.scroll_into_view_if_needed()
            btn.click()
            got = page.evaluate(AFTER_JS, cid)
            at = got["order"].index("#panel") if "#panel" in got["order"] else -1
            late = [c for c in row if c in got["order"][at + 1 :]]
            if not got["inGrid"] or got["prev"] != row[-1] or late:
                fails.append(
                    f"{label}: sorted by {sort}, Compare on {cid} opens after {got['prev']}, "
                    f"its row ends {row[-1]}; row cards after the panel {late}"
                )
            tested += 1
            btn.click()
    # Resize with a panel open, from an opener that is not last in its row.
    page.locator(".px-tools select").select_option("project")
    pick = next((c for c in ids_ if page.evaluate(ROW_JS, c)[-1] != c), ids_[0])
    page.locator(f'.board .cards > .rcard[data-id="{pick}"] .ccmp').click()
    before = page.evaluate(AFTER_JS, pick)
    if before["cols"] != 3:
        fails.append(f"{label}: the board has {before['cols']} columns at 1280 px, not 3")
    page.set_viewport_size(PHONE)
    page.wait_for_timeout(400)
    after = page.evaluate(AFTER_JS, pick)
    if after["cols"] != 1 or after["prev"] != pick:
        fails.append(
            f"{label}: resized to {after['cols']} column(s), the panel follows {after['prev']}, "
            f"not its opener {pick}"
        )
    if not tested:
        fails.append(f"{label}: no Compare placement tested")
    page.context.close()
    return fails


def phone_note_fails(browser, base: str, label: str) -> list[str]:
    """At 390 px the headers are hidden, so each cell label carries its column's note
    button; every Novel cell's opens the Novel note."""
    fails: list[str] = []
    notes = records()["index"].get("compare_notes") or {}
    novel = records()["novel"]
    page = browser.new_context(viewport=PHONE, has_touch=True, is_mobile=True).new_page()
    go(page, base + "/findings/")
    labs = page.locator(".nvgrid .nvcell:not([data-empty]) .nvlab")
    novel_seen = 0
    for i in range(labs.count()):
        lab = labs.nth(i)
        if not lab.is_visible():
            fails.append(f"{label}: at 390 px cell label {i + 1} is hidden")
            continue
        b = lab.locator(".nvnoteb")
        col = (b.first.evaluate("e => e.childNodes[0].textContent") if b.count() else "").strip()
        is_novel = "nv-new" in (lab.get_attribute("class") or "")
        if b.count() != 1 or (notes.get(col) is None):
            fails.append(
                f"{label}: at 390 px cell label '{lab.text_content()[:30]}' has no note button"
            )
            continue
        note = b.locator("xpath=following-sibling::*[1]")
        if collapse(note.text_content() or "") != collapse(notes[col]):
            fails.append(f"{label}: at 390 px the {col} cell note differs from the column's")
        if not is_novel:
            continue
        novel_seen += 1
        if col != novel:
            fails.append(f"{label}: at 390 px a Novel cell label names '{col}'")
        b.tap()
        if not note.is_visible() or b.get_attribute("aria-expanded") != "true":
            fails.append(
                f"{label}: at 390 px a tap on Novel cell note {novel_seen} does not open it"
            )
        b.tap()
        if note.is_visible():
            fails.append(
                f"{label}: at 390 px a second tap leaves Novel cell note {novel_seen} open"
            )
    want = len({topic for topic, col, _ in records()["boxes"] if col == novel})
    if novel_seen != want or not want:
        fails.append(f"{label}: at 390 px {novel_seen} Novel cell labels, the records fill {want}")
    page.context.close()
    return fails


def nojs_compare_fails(browser, base: str, label: str) -> list[str]:
    """Without the script every comparison is shown and its button says so."""
    rec = records()
    groups = [
        g
        for g in rec["index"].get("shared") or []
        if sum(m["id"] in rec["listed"] for m in g["members"]) >= 2
    ]
    page = new_page(browser, js=False)
    go(page, base + "/findings/")
    fails: list[str] = []
    panels = page.locator(".spanel")
    shown = sum(panels.nth(i).is_visible() for i in range(panels.count()))
    if panels.count() != len(groups) or shown != len(groups) or not groups:
        fails.append(
            f"{label}: without the script {shown} of {panels.count()} Compare panels show, "
            f"the records share {len(groups)} groups"
        )
    states = page.eval_on_selector_all(
        ".ccmp", "els => els.map(e => e.getAttribute('aria-expanded'))"
    )
    if not states or set(states) != {"true"}:
        fails.append(f"{label}: without the script Compare buttons say aria-expanded {set(states)}")
    page.context.close()
    return fails


def note_fails(page: Page, label: str) -> list[str]:
    """Each column heading's note button shows its note from compare_notes, and hides it."""
    fails: list[str] = []
    notes = records()["index"].get("compare_notes") or {}
    buttons = page.locator(".nvcolh .nvnoteb")
    seen = 0
    for i in range(buttons.count()):
        b = buttons.nth(i)
        col = (b.evaluate("e => e.childNodes[0].textContent") or "").strip()
        note = b.locator("xpath=following-sibling::*[1]")
        b.click()
        if not note.is_visible() or collapse(note.inner_text()) != collapse(notes.get(col, "")):
            fails.append(f"{label}: the {col} heading's note reads '{note.inner_text()[:60]}'")
        if b.get_attribute("aria-expanded") != "true":
            fails.append(f"{label}: the {col} note button does not say it is expanded")
        b.click()
        if note.is_visible():
            fails.append(f"{label}: a second click leaves the {col} note open")
        seen += 1
    want = [c for c in records()["cols"] if notes.get(c)]
    if seen != len(want):
        fails.append(f"{label}: {seen} column notes, records give {len(want)}")
    return fails


# ---------------------------------------------------------------- marks (design-marks.md M2)

RESULT_MARKS_JS = lib(
    """return {
    ink: tok('--ink'), card: tok('--card'), new: tok('--nv-new'), box: tok('--nv-box'),
    marks: [...document.querySelectorAll('.nvgrid .nd')].map(ndFeat),
    legend: [...document.querySelectorAll('.nvlegend .nd.key')].map(ndFeat),
    legendBox: [...document.querySelectorAll('.nvlegend .nbead.key')].map(b => ({
        border: getComputedStyle(b).borderTopColor,
        marks: [...b.querySelectorAll('.nd')].map(ndFeat)})),
    boxes: [...document.querySelectorAll('.nvgrid .nbead')].map(b => ({p: b.dataset.p,
        border: getComputedStyle(b).borderTopColor, under: under(b)})),
    heads: [...document.querySelectorAll('.nvcolh')].map(h => ({
        novel: h.classList.contains('nv-new'),
        text: h.textContent.trim(), bar: getComputedStyle(h.querySelector('i')).backgroundColor,
        line: getComputedStyle(h).borderBottomColor, shown: !!h.getClientRects().length})),
    labs: [...document.querySelectorAll('.nvgrid .nvlab')].map(l => ({
        novel: l.classList.contains('nv-new'),
        col: (l.querySelector('.nvnoteb')?.childNodes[0].textContent
              ?? l.textContent.split(' · ')[0]).trim(),
        color: getComputedStyle(l).color,
        shown: !!l.getClientRects().length})),
    cells: [...document.querySelectorAll('.nvgrid .nvcell')]
        .map(c => getComputedStyle(c).backgroundColor),
}"""
)

QUESTION_MARKS_JS = lib(
    """return {
    marks: [...document.querySelectorAll('.qgrid .qd')].map(qdFeat),
    legend: [...document.querySelectorAll('.qlegend .qd.key')].map(qdFeat),
    heads: [...document.querySelectorAll('.qcolh')].map(h => {
        const s = getComputedStyle(h)
        const b = getComputedStyle(h, '::before'), a = getComputedStyle(h, '::after')
        const bar = h.querySelector('i')
        return {bg: s.backgroundColor, line: s.borderBottomColor, before: b.backgroundColor,
                after: a.backgroundColor, bar: bar ? getComputedStyle(bar).backgroundColor : 'none'}
    }),
    cells: [...document.querySelectorAll('.qgrid .qcell')]
        .map(c => getComputedStyle(c).backgroundColor),
}"""
)

RINGS_JS = """() => {
    const marks = [...document.querySelectorAll('.nvgrid .nd')].map(e => {
        const r = e.getBoundingClientRect()
        return {id: e.dataset.id, rel: e.classList.contains('rel'), l: r.left, t: r.top, r: r.right,
                b: r.bottom, grow: -parseFloat(getComputedStyle(e, '::after').top) || 0,
                box: e.closest('.nbead')}
    })
    const out = []
    for (const m of marks.filter(m => m.rel)) {
        const cx = (m.l + m.r) / 2, cy = (m.t + m.b) / 2, rad = (m.r - m.l) / 2 + m.grow
        const hit = []
        for (const o of marks) {
            if (o === m || Math.abs(o.t - m.t) > 40 || Math.abs(o.l - m.l) > 40) continue
            const dx = Math.max(o.l - cx, 0, cx - o.r), dy = Math.max(o.t - cy, 0, cy - o.b)
            if (dx * dx + dy * dy < rad * rad - 0.01) hit.push(o.id)
        }
        const br = m.box.getBoundingClientRect(), s = getComputedStyle(m.box)
        const inner = {l: br.left + parseFloat(s.borderLeftWidth),
                       t: br.top + parseFloat(s.borderTopWidth),
                       r: br.right - parseFloat(s.borderRightWidth),
                       b: br.bottom - parseFloat(s.borderBottomWidth)}
        const border = cx - rad < inner.l - 0.01 || cy - rad < inner.t - 0.01
            || cx + rad > inner.r + 0.01 || cy + rad > inner.b + 0.01
        out.push({id: m.id, rad, hit, border, shown: m.r > m.l})
    }
    return out
}"""

TRIANGLE = ["50%", "0", "100%", "100%", "0", "100%"]


def shadow_layers(text: str) -> list[str]:
    """A computed box-shadow's layers (commas inside colour functions do not split)."""
    if text in ("none", ""):
        return []
    out, depth, cur = [], 0, ""
    for ch in text:
        depth += ch == "("
        depth -= ch == ")"
        if ch == "," and depth == 0:
            out.append(cur.strip())
            cur = ""
        else:
            cur += ch
    return [*out, cur.strip()]


def lengths(layer: str) -> list[float]:
    rest = re.sub(r"(?:rgba?|color)\([^)]*\)", "", layer)
    return [float(x) for x in re.findall(r"(-?[\d.]+)px", rest)]


def named(c, tk: dict) -> str:
    if same(c, tk["ink"]):
        return "ink"
    if same(c, tk["new"]):
        return "orange"
    return show(c)


def result_features(m: dict, tk: dict) -> dict:
    """What a Results mark shows, read from its computed style: shape, fill, ring, colour."""
    col = rgba(m["color"])
    b, a = m["b"], m["a"]
    clip = b["clip"]
    if clip.startswith("polygon("):
        pts = ["0" if t in ("0px", "0%") else t for t in re.findall(r"[\d.]+(?:px|%)?", clip)]
        shape = "triangle" if pts == TRIANGLE else f"polygon {clip}"
    elif b["img"].count("linear-gradient(") == 2 and "-45deg" in b["img"]:
        shape = "cross"
    elif clip == "none" and b["img"] == "none" and b["radius"] == "50%":
        shape = "circle"
    else:
        shape = f"other (radius {b['radius']}, clip {clip}, image {b['img'][:30]})"
    under = surface(m["under"]["stack"])
    if shape == "cross":
        inks = [c for c in colours_in(b["img"]) if c[3] > 0]
        fill = "solid" if inks and all(same(c, col) for c in inks) else "other"
    else:
        bg = rgba(b["bg"])
        layers = shadow_layers(b["shadow"])
        if same(bg, col):
            fill = "solid" if not layers else f"solid with shadow {b['shadow']}"
        elif bg[3] == 0 or same(bg, under) or same(bg, tk["card"]):
            stroke = [
                x for x in layers if "inset" in x and colours_in(x) and same(colours_in(x)[0], col)
            ]
            fill = "hollow" if stroke and lengths(stroke[0])[-1] >= 1.5 else "empty"
        else:
            fill = f"filled {b['bg']}"
    ring = a["content"] not in ("none", "normal") and a["style"] != "none"
    ring_ok = (
        ring
        and a["style"] == "solid"
        and float(a["width"].removesuffix("px")) >= 1
        and a["radius"] == "50%"
        and same(rgba(a["color"]), col)
    )
    return {
        "shape": shape,
        "fill": fill,
        "ring": "ring" if ring_ok else "bad ring" if ring else "none",
        "colour": named(col, tk),
        "halo": m["shadow"] != "none",
    }


def question_features(q: dict, tk: dict) -> dict:
    col = rgba(q["color"])
    b = q["b"]
    shape = (
        "circle"
        if b["radius"] == "50%" and b["clip"] == "none" and b["img"] == "none"
        else f"other (radius {b['radius']}, clip {b['clip']})"
    )
    fill = "solid" if same(rgba(b["bg"]), col) else f"filled {b['bg']}"
    layers = shadow_layers(b["shadow"])
    if not layers:
        ring = "none"
    elif (
        len(layers) == 2
        and same(colours_in(layers[1])[0], col)
        and lengths(layers[1])[-1] > lengths(layers[0])[-1]
    ):
        ring = "ring"
    else:
        ring = f"bad ring {b['shadow']}"
    return {"shape": shape, "fill": fill, "ring": ring, "colour": named(col, tk)}


def expect_result(r: dict) -> dict:
    return {
        "shape": SHAPE[r["kind"]],
        "fill": "hollow" if r["kind"] == "null" else "solid",
        "ring": "ring" if r["rel"] else "none",
        # M2: Results marks stay ink; the Novel column header carries the orange.
        "colour": "ink",
        "halo": False,
    }


def expect_question(q: dict) -> dict:
    return {
        "shape": "circle",
        "fill": "solid",
        "ring": "ring" if q["cross"] else "none",
        "colour": "orange" if q["novel"] else "ink",
    }


def mark_diffs(page: Page, tk: dict | None = None) -> tuple[list[tuple[str, str]], dict, dict]:
    """Done check 1: each mark's rendered features against the records. Returns (id, why)
    pairs, plus the raw page data for the other checks."""
    rec = records()
    rd = page.evaluate(RESULT_MARKS_JS)
    qd = page.evaluate(QUESTION_MARKS_JS) if page.locator(".qgrid").count() else None
    tk = tk or {k: rgba(rd[k]) for k in ("ink", "card", "new", "box")}
    out: list[tuple[str, str]] = []
    seen = set()
    for m in rd["marks"]:
        r = rec["results"].get(m["id"])
        if r is None:
            out.append((m["id"], "has no listed record"))
            continue
        seen.add(m["id"])
        if m["k"] != r["kind"]:
            out.append((m["id"], f"data-k '{m['k']}', record kind '{r['kind']}'"))
        got, want = result_features(m, tk), expect_result(r)
        if got != want:
            diff = {k: (got[k], want[k]) for k in want if got[k] != want[k]}
            out.append((m["id"], f"shows {diff} (got, expected)"))
    if rd["marks"] and (missing := set(rec["results"]) - seen):
        out.append(("map", f"{len(missing)} listed results have no mark"))
    for q in (qd or {}).get("marks", []):
        e = rec["questions"].get(q["id"])
        if e is None:
            out.append((q["id"], "has no record"))
            continue
        got, want = question_features(q, tk), expect_question(e)
        if got != want:
            diff = {k: (got[k], want[k]) for k in want if got[k] != want[k]}
            out.append((q["id"], f"shows {diff} (got, expected)"))
    return out, rd, qd or {}


def column_paint(rec: dict) -> tuple[str, list[str]]:
    """Negative control 2: a style that colours every mark by its column, and the colours."""
    paint = [
        "var(--nv-new)",
        "var(--nv-builds)",
        "var(--nv-match)",
        "rgb(128, 0, 128)",
        "rgb(0, 128, 128)",
        "rgb(160, 110, 0)",
    ]
    n = len(rec["cols"])
    css = [
        f".nvgrid > .nvcell:nth-of-type({n}n+{i + 1}) .nd {{ color: {c} !important; }}"
        for i, c in enumerate(paint[:n])
    ]
    css += [
        f".qgrid .qrow > .qcell:nth-of-type({i + 1}) .qd {{ color: {c} !important; }}"
        for i, c in enumerate(paint[: len(NEEDS)])
    ]
    return "\n".join(css), paint


NO_MOTION = "*, *::before, *::after { transition: none !important; animation: none !important; }"
FLUSH = """() => [...document.querySelectorAll('.nd, .qdot')]
    .map(e => getComputedStyle(e, '::before').backgroundColor).length"""
NULL_SOLID = (
    '.nvgrid .nd[data-k="null"]::before'
    " { background: currentColor !important; box-shadow: none !important; }"
)


def control_fails(page: Page, tag: str, tk: dict, results_page: bool) -> list[str]:
    """Done check 1's negative controls: each injected style must make the check fail on
    exactly the marks it changes."""
    fails: list[str] = []
    rec = records()
    # Links ease their colour; without this the controls would be read, and leave the page,
    # mid-transition.
    still = page.add_style_tag(content=NO_MOTION)
    if results_page:
        nulls = {i for i, r in rec["results"].items() if r["kind"] == "null"}
        style = page.add_style_tag(content=NULL_SOLID)
        caught = {i for i, _ in mark_diffs(page, tk)[0]}
        style.evaluate("e => e.remove()")
        if caught != nulls or not nulls:
            fails.append(
                f"{tag}: control 'nulls drawn solid' caught {len(caught)} marks, "
                f"expected the {len(nulls)} nulls (missed {sorted(nulls - caught)[:3]})"
            )
    css, paint = column_paint(rec)
    probe = page.evaluate(
        "cs => cs.map(c => { const e = document.createElement('i'); e.style.color = c;"
        " document.body.append(e); const v = getComputedStyle(e).color; e.remove(); return v })",
        paint,
    )
    colour = [rgba(c) for c in probe]
    want = set()
    if results_page:
        want = {
            i
            for i, r in rec["results"].items()
            if not same(colour[rec["cols"].index(r["col"])], tk["ink"])
        }
    else:
        want = {
            q
            for q, e in rec["questions"].items()
            if not same(colour[e["col"]], tk["new"] if e["novel"] else tk["ink"])
        }
    style = page.add_style_tag(content=css)
    caught = {i for i, _ in mark_diffs(page, tk)[0]}
    style.evaluate("e => e.remove()")
    if not want or not want <= caught:
        fails.append(
            f"{tag}: control 'marks coloured by column' caught {len(caught)} of {len(want)} "
            f"recoloured marks (missed {sorted(want - caught)[:3]})"
        )
    # Reading a style settles the page before transitions come back.
    page.evaluate(FLUSH)
    still.evaluate("e => e.remove()")
    return fails


def check_marks(browser, base: str) -> list[str]:
    """design-marks.md done checks 1 to 6 for option M2, in light and dark, at 1280 and 390 px."""
    fails: list[str] = []
    rec = records()
    for theme in ("light", "dark"):
        for viewport, touch in ((DESKTOP, False), (PHONE, True)):
            tag = f"marks: {theme} {viewport['width']} px"
            for path in ("/findings/", "/directions/"):
                page = themed(browser, theme, viewport, touch)
                go(page, base + path)
                saved = page.evaluate("document.documentElement.getAttribute('saved-theme')")
                if saved != theme:
                    fails.append(f"{tag}: {path} renders saved-theme '{saved}'")
                    continue
                fails += marks_on(page, f"{tag} {path}", theme, rec, desktop=not touch)
                page.context.close()
    return fails


def marks_on(page: Page, tag: str, theme: str, rec: dict, desktop: bool) -> list[str]:
    fails: list[str] = []
    results_page = page.locator(".nvgrid").count() > 0
    diffs, rd, qd = mark_diffs(page)
    tk = {k: rgba(rd[k]) for k in ("ink", "card", "new", "box")}
    for k, short in (("nv-new", "new"), ("nv-box", "box")):
        if not same(tk[short], TOKENS[theme][k]):
            fails.append(
                f"{tag}: --{k} is {show(tk[short])}, the design gives {show(TOKENS[theme][k])}"
            )
    # 1. Marks match records.
    counted = len(rd["marks"]) + len(qd.get("marks", []))
    if results_page and len(rd["marks"]) != len(rec["results"]):
        fails.append(f"{tag}: {len(rd['marks'])} result marks, {len(rec['results'])} listed")
    if not results_page and len(qd.get("marks", [])) != len(rec["questions"]):
        fails.append(
            f"{tag}: {len(qd.get('marks', []))} question dots, {len(rec['questions'])} records"
        )
    if not counted:
        return [*fails, f"{tag}: no mark to check"]
    fails += [f"{tag}: mark {i} {why}" for i, why in diffs[:12]]
    if len(diffs) > 12:
        fails.append(f"{tag}: and {len(diffs) - 12} more marks differ from their records")
    fails += control_fails(page, tag, tk, results_page)

    # 2. No colour by position: marks are ink or the Novel orange; headers and boxes neutral.
    colours = {named(rgba(m["color"]), tk) for m in rd["marks"] + qd.get("marks", [])}
    if extra := colours - {"ink", "orange"}:
        fails.append(f"{tag}: marks take colours {sorted(extra)}")
    if results_page:
        if {named(rgba(m["color"]), tk) for m in rd["marks"]} != {"ink"}:
            fails.append(f"{tag}: Results marks are not all ink")
        heads = rd["heads"]
        novel_heads = [h for h in heads if h["novel"]]
        if len(novel_heads) != 1 or not heads or not heads[0]["novel"]:
            fails.append(f"{tag}: Novel header flags {[h['novel'] for h in heads]}; only the first")
        for h in heads:
            bar, line = rgba(h["bar"]), rgba(h["line"])
            if h["novel"] and not same(bar, tk["new"]):
                fails.append(f"{tag}: the Novel header bar is {show(bar)}, not orange")
            if not h["novel"] and not neutral(bar):
                fails.append(f"{tag}: header '{h['text'][:30]}' bar is coloured {show(bar)}")
            if not neutral(line):
                fails.append(f"{tag}: header '{h['text'][:30]}' rule is coloured {show(line)}")
        for b in rd["boxes"]:
            c = rgba(b["border"])
            if not same(c, tk["box"]) or not neutral(c):
                fails.append(f"{tag}: box {b['p']} border is {show(c)}, not the neutral --nv-box")
                break
        if not rd["boxes"]:
            fails.append(f"{tag}: no project box to measure")
        shown = [lab for lab in rd["labs"] if lab["shown"]]
        if not desktop:
            if not shown:
                fails.append(f"{tag}: no cell label shows on a phone")
            for lab in shown:
                c = rgba(lab["color"])
                is_novel = lab["col"] == rec["novel"]
                if lab["novel"] != is_novel:
                    fails.append(f"{tag}: cell label '{lab['col']}' Novel flag {lab['novel']}")
                if is_novel and not same(c, tk["new"]):
                    fails.append(f"{tag}: the Novel cell label is {show(c)}, not orange")
                if not is_novel and not neutral(c):
                    fails.append(f"{tag}: cell label '{lab['col']}' is coloured {show(c)}")
        for c in rd["cells"]:
            if not neutral(rgba(c)):
                fails.append(f"{tag}: a map cell has a coloured background {c}")
                break
    else:
        for h in qd["heads"]:
            for part in ("bg", "line", "before", "after", "bar"):
                if h[part] != "none" and not neutral(rgba(h[part])) and rgba(h[part])[3] > 0:
                    fails.append(f"{tag}: a question column header {part} is coloured {h[part]}")
        for c in qd["cells"]:
            if not neutral(rgba(c)):
                fails.append(f"{tag}: a question cell has a coloured background {c}")
                break
        # The 55% fade on unringed dots is gone.
        faded = [q["id"] for q in qd["marks"] if q["op"] * q["under"]["op"] < 1]
        if faded:
            fails.append(f"{tag}: {len(faded)} question dots are faded, such as {faded[0]}")
        shaped = [q["id"] for q in qd["marks"] if q["shape"]]
        if shaped:
            fails.append(f"{tag}: {len(shaped)} question dots still carry data-shape")

    # 3. Each legend entry draws the map: the same features as a map mark of its class.
    if results_page:
        legend = rd["legend"] + [m for b in rd["legendBox"] for m in b["marks"]]
        if not rd["legend"]:
            fails.append(f"{tag}: the Results legend has no mark")
        keys = {(m["k"], m["rel"]) for m in rd["legend"]}
        if keys != {(r["kind"], False) for r in rec["results"].values()} | {("result", True)}:
            fails.append(f"{tag}: the legend draws {sorted(keys)}")
        for m in legend:
            twin = next((x for x in rd["marks"] if (x["k"], x["rel"]) == (m["k"], m["rel"])), None)
            if twin is None:
                fails.append(f"{tag}: legend mark {m['k']} ring {m['rel']} has no map twin")
                continue
            raw = ("color", "w", "h")
            diff = [k for k in raw if m[k] != twin[k]]
            diff += [f"::before {k}" for k in m["b"] if m["b"][k] != twin["b"][k]]
            diff += [f"::after {k}" for k in m["a"] if m["a"][k] != twin["a"][k]]
            got, want = result_features(m, tk), result_features(twin, tk)
            if got != want or diff:
                fails.append(
                    f"{tag}: legend mark {m['k']} ring {m['rel']} {got} "
                    f"differs from the map {want} in {diff}"
                )
        for b in rd["legendBox"]:
            if rd["boxes"] and b["border"] != rd["boxes"][0]["border"]:
                fails.append(f"{tag}: the legend box border {b['border']} differs from the map's")
        if not rd["legendBox"]:
            fails.append(f"{tag}: the legend has no project box")
    else:
        sizes: set[tuple[float, float]] = set()
        if not qd["legend"]:
            fails.append(f"{tag}: the questions legend has no dot")
        flags = {(q["novel"], q["cross"]) for q in qd["legend"]}
        if flags != {(False, False), (True, False), (False, True)}:
            fails.append(f"{tag}: the questions legend draws {sorted(flags)}")
        for q in qd["legend"]:
            twin = next(
                (x for x in qd["marks"] if (x["novel"], x["cross"]) == (q["novel"], q["cross"])),
                None,
            )
            if twin is None:
                fails.append(
                    f"{tag}: legend dot novel {q['novel']} ring {q['cross']} has no map twin"
                )
                continue
            got, want = question_features(q, tk), question_features(twin, tk)
            if (
                got != want
                or q["b"]["shadow"] != twin["b"]["shadow"]
                or q["color"] != twin["color"]
            ):
                fails.append(
                    f"{tag}: legend dot novel {q['novel']} ring {q['cross']} {got} "
                    f"differs from the map {want}"
                )
            if desktop and (q["w"], q["h"]) != (twin["w"], twin["h"]):
                sizes.add((q["w"], twin["w"]))
        for small, big in sorted(sizes):
            print(f"note: {tag}: legend dots are {small} px, map dots {big} px")

    # 4. Contrast: 3:1 against the map surface, opacity composited.
    low: list[str] = []
    for m in rd["marks"] if results_page else []:
        under = surface(m["under"]["stack"])
        for part, c in (("mark", m["color"]), ("ring", m["a"]["color"] if m["rel"] else None)):
            if c is None:
                continue
            r = ratio(blend(rgba(c), under, m["under"]["op"]), under)
            if r < 3:
                low.append(f"{part} {m['id']} {r:.2f}:1")
        if m["k"] == "null":
            r = ratio(
                blend(rgba(m["color"]), rgba(m["b"]["bg"]), m["under"]["op"]), rgba(m["b"]["bg"])
            )
            if r < 3:
                low.append(f"hollow stroke {m['id']} {r:.2f}:1")
    for b in rd["boxes"] if results_page else []:
        under = surface(b["under"]["stack"])
        r = ratio(blend(rgba(b["border"]), under, b["under"]["op"]), under)
        if r < 3:
            low.append(f"box {b['p']} border {r:.2f}:1")
    for q in qd.get("marks", []):
        under = surface(q["under"]["stack"])
        c = blend(rgba(q["color"]), under, q["op"] * q["under"]["op"])
        if (r := ratio(c, under)) < 3:
            low.append(f"dot {q['id']} {r:.2f}:1")
        layers = shadow_layers(q["b"]["shadow"])
        # A missing ring is check 1's failure; here only a drawn ring is measured.
        if q["cross"] and len(layers) == 2 and colours_in(layers[0]):
            gap = colours_in(layers[0])[0]
            if (r := ratio(c, blend(gap, under))) < 3:
                low.append(f"ring {q['id']} against its gap {r:.2f}:1")
    if low:
        fails.append(f"{tag}: {len(low)} below 3:1, such as {low[:3]}")
    if (r := ratio(tk["new"], tk["ink"])) < 3:
        fails.append(f"{tag}: orange against ink is {r:.2f}:1")

    # 5. Words: novel questions say so; each box label names the kinds it holds.
    if results_page:
        fails += box_words(page, tag, rec)
    else:
        for q in qd["marks"]:
            e = rec["questions"].get(q["id"])
            if e is None:
                continue
            for where, said in (("name", q["label"]), ("pop-up", q["pop"])):
                if (NOVEL_WORDS in said) != e["novel"]:
                    fails.append(
                        f"{tag}: dot {q['id']} {where} novel words {NOVEL_WORDS in said}, "
                        f"record {e['novel']}"
                    )

    # 6. Rings do not touch another mark or their box border.
    if results_page:
        rings = page.evaluate(RINGS_JS)
        if len(rings) != sum(r["rel"] for r in rec["results"].values()) or not rings:
            fails.append(f"{tag}: {len(rings)} rings measured")
        for r in rings:
            if r["hit"] or r["border"] or not r["shown"]:
                fails.append(
                    f"{tag}: ring of {r['id']} (radius {r['rad']:.1f}) meets marks {r['hit']}, "
                    f"box border {r['border']}"
                )

    # Hover gives a soft halo, never a ring.
    if desktop:
        fails += halo_fails(page, tag, tk, results_page)
    return fails


def box_words(page: Page, tag: str, rec: dict) -> list[str]:
    fails: list[str] = []
    titles = rec["index"].get("project_titles") or {}
    named_boxes = 0
    # The whole label is compared, so it names exactly the kinds the box holds.
    for b in page.evaluate(BOXES_JS):
        items = rec["boxes"].get((b["topic"], b["col"], b["p"]), [])
        if not items:
            continue
        kinds = [(k, sum(rec["results"][i]["kind"] == k for i in items)) for k in KIND_WORDS]
        words = ", ".join(f"{n} {BOX_COUNT_WORDS[k][n != 1]}" for k, n in kinds if n)
        n = len(items)
        # Novelty.tsx names the project by its index title, else its first result's report.
        name = titles.get(b["p"]) or rec["findings"][items[0]].get("report_title") or b["p"]
        head = f"{name}: {n} {'result' if n == 1 else 'results'}, {b['col']}"
        rel = sum(rec["results"][i]["rel"] for i in items)
        want = ". ".join(
            x
            for x in (head, words, f"{rel} with a related result in another project" if rel else "")
            if x
        )
        if b["label"] != want:
            fails.append(f"{tag}: box label '{b['label']}', expected '{want}'")
            break
        named_boxes += 1
    if not named_boxes:
        fails.append(f"{tag}: no box label to read")
    return fails


def halo_fails(page: Page, tag: str, tk: dict, results_page: bool) -> list[str]:
    fails: list[str] = []
    if results_page:
        m = page.locator(".nvgrid .nd.rel").first
        m.scroll_into_view_if_needed()
        before = m.evaluate("e => getComputedStyle(e, '::after').borderTopColor")
        m.hover()
        page.wait_for_timeout(200)
        on = page.eval_on_selector_all(".nvgrid .nd.on", "els => els.map(e => e.dataset.id)")
        got = m.evaluate(
            "e => [getComputedStyle(e).boxShadow, getComputedStyle(e).outlineStyle,"
            " getComputedStyle(e, '::after').borderTopColor]"
        )
        layers = shadow_layers(got[0])
        soft = layers and colours_in(layers[0]) and colours_in(layers[0])[0][3] < 0.3
        if on != [m.get_attribute("data-id")] or not soft or got[1] != "none" or got[2] != before:
            fails.append(
                f"{tag}: hovering a ringed mark gives marks {on} shadow '{got[0]}', "
                f"outline {got[1]}"
            )
        page.mouse.move(0, 0)
        page.wait_for_timeout(500)
    else:
        q = page.locator(".qgrid .qd.cross").first
        dot = q.locator("a.qdot")
        dot.scroll_into_view_if_needed()
        ring = dot.evaluate("e => getComputedStyle(e, '::before').boxShadow")
        dot.hover()
        page.wait_for_timeout(200)
        bg, ring2 = dot.evaluate(
            "e => [getComputedStyle(e).backgroundColor, getComputedStyle(e, '::before').boxShadow]"
        )
        c = rgba(bg)
        if not (0 < c[3] < 0.3) or ring2 != ring:
            fails.append(f"{tag}: hovering a dot gives halo {bg}, ring '{ring2}' (was '{ring}')")
        page.mouse.move(0, 0)
        page.wait_for_timeout(500)
    return fails


# ---------------------------------------------------------------- filters (option 1B)


def board_expectations() -> dict[str, dict]:
    """Per board, each card's facet values and toggles, from the records."""
    rec = records()
    res = {
        i: {
            "f": {"topic": r["topic"], "compare": r["col"], "kind": r["kind"]},
            "t": {"rel": r["rel"]},
        }
        for i, r in rec["results"].items()
    }
    qs = {
        q: {
            "f": {"topic": e["topic"], "need": e["need"], "approach": e["approach"]},
            "t": {"cross": e["cross"], "novel": e["novel"]},
        }
        for q, e in rec["questions"].items()
    }
    return {
        "/findings/": {
            "cards": res,
            "marks": ".nvgrid .nd[data-id]",
            "picks": [("topic", None), ("compare", rec["novel"]), ("kind", "null")],
            "toggles": ["rel"],
        },
        "/directions/": {
            "cards": qs,
            "marks": ".qgrid .qd[data-id]",
            "picks": [("topic", None), ("need", "measure"), ("approach", None)],
            "toggles": ["cross", "novel"],
        },
    }


def board_state(page: Page, marks: str) -> dict:
    return page.evaluate(
        """marks => {
        const board = document.querySelector('section.board[data-board]')
        const cards = [...board.querySelectorAll(':scope > .cards > .card')]
        return {
            shown: cards.filter(c => !c.classList.contains('px-hidden')
                && getComputedStyle(c).display !== 'none').map(c => c.dataset.id),
            leaked: cards.filter(c => c.classList.contains('px-hidden')
                && getComputedStyle(c).display !== 'none').length,
            order: cards.map(c => c.dataset.id),
            count: board.querySelector('.px-tools .row1 > .count:last-child')?.textContent.trim(),
            pressed: [...board.querySelectorAll(
                '.px-tools .facets[data-k] .px-chip[aria-pressed=true]')]
                .map(b => [b.closest('.facets').dataset.k, b.dataset.f]),
            checked: [...board.querySelectorAll('.px-tools input[data-t]')].filter(i => i.checked)
                .map(i => i.dataset.t),
            compact: board.classList.contains('px-compact'),
            sort: board.querySelector('.px-tools select')?.value,
            q: board.querySelector('.px-tools input[type=search]')?.value,
            out: [...document.querySelectorAll(marks)].filter(m => m.classList.contains('out'))
                .map(m => m.dataset.id),
            marks: [...document.querySelectorAll(marks)].map(m => m.dataset.id),
            fadedOut: [...document.querySelectorAll(marks)].filter(m => m.classList.contains('out'))
                .every(m => { const t = m.matches('.qd') ? m.querySelector('.qdot') : m;
                    return +getComputedStyle(t).opacity < 0.5 }),
            beads: [...document.querySelectorAll('.nvgrid .nbead')].map(b =>
                [b.classList.contains('out'),
                 [...b.querySelectorAll('.nd')].every(d => d.classList.contains('out'))]),
        }
    }""",
        marks,
    )


def filter_fails(st: dict, want: set[str], total: int, label: str) -> list[str]:
    fails: list[str] = []
    if set(st["shown"]) != want:
        extra, missing = set(st["shown"]) - want, want - set(st["shown"])
        fails.append(
            f"{label}: shows {len(st['shown'])} cards, records give {len(want)} "
            f"(extra {sorted(extra)[:2]}, missing {sorted(missing)[:2]})"
        )
    if st["leaked"]:
        fails.append(f"{label}: {st['leaked']} hidden cards still display")
    if st["count"] != f"{len(want)} of {total}":
        fails.append(f"{label}: the count reads '{st['count']}', expected '{len(want)} of {total}'")
    if not st["marks"]:
        fails.append(f"{label}: the map has no marks to fade")
    wrong = [m for m in st["marks"] if (m in st["out"]) == (m in want)]
    if wrong:
        fails.append(f"{label}: {len(wrong)} map marks fade the wrong way, such as {wrong[0]}")
    if not st["fadedOut"]:
        fails.append(f"{label}: a mark marked out is not drawn faded")
    bad = [b for b in st["beads"] if b[0] != b[1]]
    if bad:
        fails.append(f"{label}: {len(bad)} boxes fade unlike their marks")
    return fails


def check_filters(browser, base: str) -> list[str]:
    """Done check 4: on each board a topic chip, a category chip and each toggle leave only
    matching cards, the count reads "N of M", the URL holds the state, a reload restores it,
    list view toggles, and the map fades the marks outside the filter."""
    fails: list[str] = []
    for path, cfg in board_expectations().items():
        page = new_page(browser)
        go(page, base + path)
        fails += board_fails(page, base, path, cfg)
        page.context.close()
    fails += stale_url_fails(browser, base)
    return fails


def stale_url_fails(browser, base: str) -> list[str]:
    """A URL value no chip offers (a stale or edited link) is ignored: every card shows, only
    the All chips are pressed, and no mark fades."""
    fails: list[str] = []
    for path, query in (("/findings/", "topic=nonexistent"), ("/directions/", "need=nonexistent")):
        cfg = board_expectations()[path]
        page = new_page(browser)
        go(page, f"{base}{path}?{query}")
        st = board_state(page, cfg["marks"])
        label = f"filters: {path}?{query}"
        fails += filter_fails(st, set(cfg["cards"]), len(cfg["cards"]), label)
        rows = page.locator(".px-tools .facets[data-k]").count()
        if any(v for _, v in st["pressed"]) or len(st["pressed"]) != rows or not rows:
            fails.append(
                f"{label}: chips pressed {st['pressed']}, expected only the {rows} All chips"
            )
        if st["out"]:
            fails.append(f"{label}: {len(st['out'])} marks fade")
        page.context.close()
    return fails


def board_fails(page: Page, base: str, path: str, cfg: dict) -> list[str]:
    fails: list[str] = []
    cards = cfg["cards"]
    total = len(cards)
    tools = page.locator("section.board[data-board] > .px-tools")
    if tools.count() != 1:
        fails.append(f"filters: {path} has {tools.count()} filter bars")
        return fails
    st = board_state(page, cfg["marks"])
    fails += filter_fails(st, set(cards), total, f"filters: {path} unfiltered")
    if st["out"]:
        fails.append(f"filters: {path} fades {len(st['out'])} marks before any filter")
    if set(st["marks"]) != set(cards):
        fails.append(
            f"filters: {path} map marks and records differ by {len(set(st['marks']) ^ set(cards))}"
        )

    def url_state() -> dict[str, list[str]]:
        return parse_qs(urlparse(page.url).query)

    def run(label: str, params: dict[str, str], want: set[str]) -> None:
        nonlocal fails
        st = board_state(page, cfg["marks"])
        fails += filter_fails(st, want, total, label)
        if (got := {k: v[0] for k, v in url_state().items()}) != params:
            fails.append(f"{label}: the URL holds {got}, expected {params}")
        page.reload(wait_until="networkidle")
        again = board_state(page, cfg["marks"])
        fails += [f"{x} after a reload" for x in filter_fails(again, want, total, label)]
        keep = ("pressed", "checked", "compact", "sort", "q")
        if {k: again[k] for k in keep} != {k: st[k] for k in keep}:
            fails.append(
                f"{label}: a reload restores {[again[k] for k in keep]}, "
                f"not {[st[k] for k in keep]}"
            )

    def chip(k: str, v: str) -> None:
        page.locator(f".px-tools .facets[data-k={k}] .px-chip[data-f='{v}']").click()

    for k, v in cfg["picks"]:
        if v is None:
            tally = Counter(c["f"][k] for c in cards.values())
            values = [x for x, _ in sorted(tally.items(), key=lambda kv: (-kv[1], kv[0]))]
            v = values[min(1, len(values) - 1)]
        want = {i for i, c in cards.items() if c["f"][k] == v}
        if not want or len(want) == total:
            fails.append(f"filters: {path} {k} '{v}' matches {len(want)} of {total} cards")
        chip(k, v)
        run(f"filters: {path} {k} '{v}'", {k: v}, want)
        pressed = page.locator(f".px-tools .facets[data-k={k}] .px-chip[aria-pressed=true]")
        if pressed.count() != 1 or pressed.get_attribute("data-f") != v:
            fails.append(f"filters: {path} {k} '{v}' chip is not the one pressed")
        chip(k, v)
        if url_state() or len(board_state(page, cfg["marks"])["shown"]) != total:
            fails.append(f"filters: {path} a second click on {k} '{v}' does not clear it")
    # A topic and a category together: both must hold.
    (k1, _), (k2, v2) = cfg["picks"][0], cfg["picks"][1]
    v1 = next(iter(sorted({c["f"][k1] for c in cards.values() if c["f"][k2] == v2})), "")
    chip(k1, v1)
    chip(k2, v2)
    want = {i for i, c in cards.items() if c["f"][k1] == v1 and c["f"][k2] == v2}
    run(f"filters: {path} {k1} '{v1}' and {k2} '{v2}'", {k1: v1, k2: v2}, want)
    go(page, base + path)
    for t in cfg["toggles"]:
        box = page.locator(f".px-tools input[data-t={t}]")
        if not box.count():
            fails.append(f"filters: {path} has no '{t}' toggle")
            continue
        box.check()
        want = {i for i, c in cards.items() if c["t"][t]}
        if not want:
            fails.append(f"filters: {path} toggle {t} matches no record")
        run(f"filters: {path} toggle {t}", {t: "1"}, want)
        page.locator(f".px-tools input[data-t={t}]").uncheck()
        if url_state():
            fails.append(f"filters: {path} unchecking {t} leaves {url_state()} in the URL")
    # Sort and the list view are kept in the URL too.
    sorts = page.eval_on_selector_all(".px-tools select option", "els => els.map(e => e.value)")
    if len(sorts) > 1:
        page.locator(".px-tools select").select_option(sorts[1])
        st = board_state(page, cfg["marks"])
        ranks = page.eval_on_selector_all(
            "section.board[data-board] > .cards > .card",
            f"els => els.map(e => +e.getAttribute('data-s-{sorts[1]}'))",
        )
        if ranks != sorted(ranks) or url_state() != {"sort": [sorts[1]]}:
            fails.append(
                f"filters: {path} sort {sorts[1]} gives URL {url_state()}, "
                f"order sorted {ranks == sorted(ranks)}"
            )
        page.reload(wait_until="networkidle")
        if board_state(page, cfg["marks"])["order"] != st["order"]:
            fails.append(f"filters: {path} a reload does not restore sort {sorts[1]}")
        page.locator(".px-tools select").select_option(sorts[0])
    else:
        fails.append(f"filters: {path} offers {len(sorts)} sorts")
    page.locator(".px-tools .px-seg button[data-v=list]").click()
    st = board_state(page, cfg["marks"])
    display = page.locator("section.board[data-board] > .cards").evaluate(
        "e => getComputedStyle(e).display"
    )
    if not st["compact"] or url_state() != {"view": ["list"]} or display != "block":
        fails.append(
            f"filters: {path} List gives compact {st['compact']}, URL {url_state()}, "
            f"display {display}"
        )
    page.reload(wait_until="networkidle")
    if not board_state(page, cfg["marks"])["compact"]:
        fails.append(f"filters: {path} a reload does not restore the list view")
    page.locator(".px-tools .px-seg button[data-v=cards]").click()
    if board_state(page, cfg["marks"])["compact"] or url_state():
        fails.append(f"filters: {path} Cards does not leave the list view")
    # Words filter on what the card says.
    if path == "/findings/":
        rec = records()
        word = "essential"
        want = {
            i
            for i in cards
            if word
            in " ".join(
                str(rec["findings"][i].get(k) or "") for k in ("title", "gist", "report_title")
            ).lower()
        }
        page.locator(".px-tools input[type=search]").fill(word)
        run(f"filters: {path} words '{word}'", {"q": word}, want)
    return fails


# ---------------------------------------------------------------- related results (done check 7)


def check_related(browser, base: str) -> list[str]:
    """Every listed result whose record lists related results shows them under "Related
    results in other projects", one link per id; every result the map can draw a related
    line for has the section; no other listed result has it."""
    fails: list[str] = []
    rec = records()
    drawable = {i for i, r in rec["results"].items() if r["rel"]}
    with_related = {i for i in rec["listed"] if rec["findings"][i].get("related")}
    if not with_related:
        return ["related: no listed result lists related results"]
    if missing := drawable - with_related:
        fails.append(
            f"related: {len(missing)} results with a drawable related line list none: "
            f"{sorted(missing)[:3]}"
        )
    for i in sorted(drawable):
        partners = {
            lk["b"] if lk["a"] == i else lk["a"] for lk in rec["links"] if i in (lk["a"], lk["b"])
        }
        if not partners <= set(rec["findings"][i].get("related") or []):
            fails.append(
                f"related: {i} lists {rec['findings'][i].get('related')}, "
                f"its map lines reach {sorted(partners)}"
            )
    page = new_page(browser)
    checked = 0
    for i in sorted(with_related):
        want = rec["findings"][i]["related"]
        go(page, f"{base}/findings/{i}")
        heads = page.eval_on_selector_all("h2", "els => els.map(e => e.textContent.trim())")
        if heads.count(RELATED_HEADING) != 1:
            fails.append(
                f"related: {i} has {heads.count(RELATED_HEADING)} '{RELATED_HEADING}' sections"
            )
            continue
        order = [FINDING_HEADINGS.index(h) for h in heads if h in FINDING_HEADINGS]
        if order != sorted(order):
            fails.append(f"related: {i} headings out of order: {heads}")
        links = page.evaluate(
            """h => {
            const head = [...document.querySelectorAll('h2')].find(e => e.textContent.trim() === h)
            const out = []
            for (let n = head.nextElementSibling; n && !/^H[1-6]$/.test(n.tagName);
                 n = n.nextElementSibling)
                for (const li of n.querySelectorAll(':scope > li'))
                    out.push([...li.querySelectorAll('a')]
                    .map(a => a.getAttribute('href')).filter(Boolean))
            return out }""",
            RELATED_HEADING,
        )
        got = [last_part(x[0]) if x else "" for x in links]
        if got != want:
            fails.append(f"related: {i} section links {got}, record lists {want}")
        if any(len(x) != 1 for x in links):
            fails.append(
                f"related: {i} has a list item with {[len(x) for x in links]} result links"
            )
        for o in want:
            if o not in rec["listed"]:
                fails.append(f"related: {i} lists {o}, which is not a listed result")
        checked += 1
    # The other listed results carry no such section (read from the built HTML).
    for i in sorted(rec["listed"] - with_related):
        try:
            html = urllib.request.urlopen(f"{base}/findings/{i}", timeout=20).read().decode()
        except urllib.error.HTTPError as e:
            fails.append(f"related: /findings/{i} returned HTTP {e.code}")
            continue
        if RELATED_HEADING in html:
            fails.append(f"related: {i} shows the section but its record lists no related results")
        checked += 1
    if checked != len(rec["listed"]):
        fails.append(f"related: checked {checked} of {len(rec['listed'])} listed result pages")
    print(
        f"note: related: {len(with_related)} result pages with the section, "
        f"{len(drawable)} on the map"
    )
    return fails


CHECKS = {
    "home": check_home,
    "strips": check_strips,
    "plain": check_plain,
    "grid": check_grid,
    "pages": check_pages,
    "contrast": check_contrast,
    "cross": check_cross,
    "marks": check_marks,
    "filters": check_filters,
    "related": check_related,
}


def serve(directory: str, port: int) -> ThreadingHTTPServer:
    """Serve a built site with clean URLs: `/x` falls back to `/x.html`."""

    class Handler(SimpleHTTPRequestHandler):
        def translate_path(self, path: str) -> str:
            real = super().translate_path(path)
            if not Path(real).exists() and Path(real + ".html").is_file():
                return real + ".html"
            return real

        def log_message(self, format: str, *args: object) -> None:
            pass

    class Server(ThreadingHTTPServer):
        # The default backlog of 5 resets connections when a page loads many files at once.
        request_queue_size = 128

    handler = partial(Handler, directory=directory)
    server = Server(("127.0.0.1", port), handler)
    Thread(target=server.serve_forever, daemon=True).start()
    return server


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("check", choices=sorted(CHECKS))
    ap.add_argument("--base", default="http://localhost:8080")
    ap.add_argument("--serve", metavar="DIR", help="serve this built folder at the --base port")
    # The marks check implements option M2 of design-marks.md, the one the site builds.
    ap.add_argument("--option", choices=["M2"], default="M2", help="mark vocabulary to check")
    args = ap.parse_args()
    server = serve(args.serve, urlparse(args.base).port or 80) if args.serve else None
    with sync_playwright() as pw:
        browser = pw.chromium.launch(channel="chrome")
        try:
            fails = CHECKS[args.check](browser, args.base.rstrip("/"))
        finally:
            browser.close()
            if server:
                server.shutdown()
    for f in fails:
        print(f)
    seen = ""
    if args.check == "plain":
        seen = " inspected " + ", ".join(f"{v} {k}" for k, v in PLAIN_COUNTS.items())
    print(f"{args.check}: {'FAIL' if fails else 'PASS'} ({len(fails)} failure(s)){seen}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
