"""Done checks for the result and question reader pages (spec 2026-11-04-reader-overhaul-design.md).

Run against a build, either the one `quartz build --serve` serves on 8080 or
`--serve quartz/public`, which serves the built folder with clean URLs (a plain
`http.server` 404s on `/findings/<id>`)::

    WIKI_BASE_URL=localhost:8096 CBORG_API_KEY= scripts/build_quartz.sh
    uv run --with playwright python scripts/check_reader.py grid \
        --base http://localhost:8096 --serve quartz/public

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
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread
from urllib.parse import urlparse

# Supplied at run time by `uv run --with playwright`; not a project dependency.
from playwright.sync_api import Page, sync_playwright  # ty: ignore[unresolved-import]

from beril_wiki.stages.gists import statistical

ROOT = Path(__file__).resolve().parent.parent
PHONE = {"width": 390, "height": 844}
DESKTOP = {"width": 1280, "height": 900}

HOME_HEADINGS = [
    "BERIL Knowledge Wiki",
    "Find your way in",
    "What the projects found",
    "Questions still open",
    "The map",
    "Topics",
]
HOME_ABSENT = [
    "What BERIL found",
    "Plan your next project",
    "checked against PubMed",
    "change the picture",
]
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
# Wording that would read as one project confirming another (the links stage's list).
CONFIRM = re.compile(
    r"\b(?:confirm\w*|corroborat\w*|validat\w*|reproduc\w*|replicat\w*|independen\w*|agree\w*)\b"
    r"|support(?:s|ed)? each other",
    re.I,
)
LIGHT_LABELS = [".rt", ".fcard .meta", ".qcolh", ".qlab", ".skicker", ".nvcolh", ".ready.part"]
KIND_CHIPS = ["All", "Results", "Interpretations", "Null or missing results", "Corrections"]
FINDING_HEADINGS = [
    "What the report measured",
    "Limits",
    "Compared with published work",
    "Open questions that build on this",
    "Related conflicts",
]


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


def new_page(browser, viewport=DESKTOP, js=True) -> Page:
    ctx = browser.new_context(viewport=viewport, java_script_enabled=js)
    return ctx.new_page()


def go(page: Page, url: str) -> None:
    page.goto(url, wait_until="networkidle")


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


def check_home(browser, base: str) -> list[str]:
    fails: list[str] = []
    page = new_page(browser)
    go(page, base + "/")
    heads = page.eval_on_selector_all("h1, h2", "els => els.map(e => e.textContent.trim())")
    if heads != HOME_HEADINGS:
        fails.append(f"home: headings {heads} != {HOME_HEADINGS}")
    text = page.inner_text("body")
    fails += [f"home: contains '{s}'" for s in HOME_ABSENT if s.lower() in text.lower()]

    if page.locator(".scard").count():
        fails.append("home: shows shared cards; they belong on the Results page")
    fails += check_strips(browser, base, page)
    cards = page.eval_on_selector_all(
        ".fcard",
        """els => els.map(e => ({
            href: e.querySelector('h3 a')?.getAttribute('href') || '',
            kind: e.dataset.kind || '',
            topic: e.dataset.topic || '',
            report: e.querySelector('.meta a')?.getAttribute('href') || '',
        }))""",
    )
    gists_path = ROOT / "state" / "gists.json"
    gists = json.loads(gists_path.read_text()) if gists_path.exists() else {}
    have = sum(1 for g in gists.values() if g.get("gist"))
    if not cards and not have:
        print("note: home: 0 cards (no summaries yet)")
        return fails
    if have and len(cards) != 3:
        fails.append(f"home: {len(cards)} cards, expected 3 ({have} summaries exist)")
    fid = [c["href"].rsplit("/", 1)[-1] for c in cards]
    for label, vals in (
        ("ids", fid),
        ("projects", [c["report"].rsplit("/", 1)[-1] for c in cards]),
        ("topics", [c["topic"] for c in cards]),
    ):
        if len(set(vals)) != len(vals):
            fails.append(f"home: card {label} not distinct: {vals}")
    for c, i in zip(cards, fid, strict=True):
        case = gists.get(i, {}).get("case", "")
        if c["kind"] == "null" and (not case or case in BAD_NULL_CASES):
            fails.append(f"home: null-result card {i} has case '{case or 'none'}'")
    return fails


def check_strips(browser, base: str, page: Page) -> list[str]:
    """Every home result and question has a topic strip; picking a topic marks those sharing it."""
    fails: list[str] = []
    entries_js = "[data-tstrips] [data-topics]"
    entries = page.eval_on_selector_all(
        entries_js,
        """els => els.map(e => ({
            topics: e.dataset.topics.split(' '),
            slots: e.querySelectorAll('.tslot').length,
            on: [...e.querySelectorAll('.tslot.on')].map(s => s.dataset.t),
            card: e.matches('.fcard'),
        }))""",
    )
    if not entries:
        return ["home: no result or question has a topic strip"]
    keys = page.locator(".tkeyslot").count()
    for i, e in enumerate(entries):
        if e["slots"] != keys:
            fails.append(f"home: strip {i} has {e['slots']} slots, the key has {keys}")
        if sorted(e["on"]) != sorted(e["topics"]):
            fails.append(f"home: strip {i} fills {e['on']}, its entry names {e['topics']}")
    if not page.locator(".tkey").is_visible():
        fails.append("home: the topic key is hidden with the script")
    # What a reader sees: an outlined entry shares the topic, a dashed one does not.
    looks = """els => els.map(e => {
        const s = getComputedStyle(e)
        return s.boxShadow !== 'none' ? 'lit' : s.borderTopStyle === 'dashed' ? 'faded' : 'plain'
    })"""

    def want(t: str | None) -> list[str]:
        return [("lit" if t in e["topics"] else "faded") if t else "plain" for e in entries]

    def told(t: str) -> str:
        def n(k: int, word: str) -> str:
            return f"no {word}s" if k == 0 else f"1 {word}" if k == 1 else f"{k} {word}s"

        hit = [e for e in entries if t in e["topics"]]
        cards = sum(e["card"] for e in hit)
        return f"On this page: {n(cards, 'result')} and {n(len(hit) - cards, 'question')}."

    def readout() -> str:
        """The key's visible readout: the topic shown, or 'idle', plus the count line."""
        return page.evaluate(
            """() => {
            const info = [...document.querySelectorAll('.tinfo')].find(e => !e.hidden)
            const state = document.querySelector('.tstate')
            const line = state.hidden ? '' : state.querySelector('.tkcount').textContent
            return (info ? info.dataset.t : 'idle') + '|' + line
        }"""
        )

    def settled() -> list[str]:
        page.wait_for_timeout(300)
        return page.eval_on_selector_all(entries_js, looks)

    page.mouse.move(0, 0)
    if readout() != "idle|":
        fails.append(f"home: the key opens showing {readout()}")
    hover = entries[-1]["topics"][0]
    page.locator(f'.tkeyslot[data-t="{hover}"]').hover()
    if readout() != f"{hover}|":
        fails.append(f"home: pointing at {hover} shows {readout()}")
    page.mouse.move(0, 0)
    topic = entries[0]["topics"][0]
    page.locator(f'.tkeyslot[data-t="{topic}"]').click()
    if (got := settled()) != want(topic):
        fails.append(f"home: picking {topic} shows {got}, expected {want(topic)}")
    page.mouse.move(0, 0)
    if (text := readout()) != f"{topic}|{told(topic)}":
        fails.append(f"home: the key shows '{text}', expected '{topic}|{told(topic)}'")
    lit_map = """() => [...document.querySelectorAll('[data-tmap] .cluster')]
        .filter(g => getComputedStyle(g).opacity > 0.5).map(g => g.dataset.t)"""
    if (got := page.evaluate(lit_map)) != [topic]:
        fails.append(f"home: picking {topic} leaves map clusters {got} bright")
    page.locator(".tmapgo").click()
    page.wait_for_timeout(800)
    if not page.evaluate(
        "(() => { const r = document.querySelector('[data-tmap]').getBoundingClientRect();"
        " return r.top < innerHeight && r.bottom > 0 })()"
    ):
        fails.append("home: See it on the map does not bring the map into view")
    page.keyboard.press("Escape")
    # Focus was on "See it on the map", which Escape hides, so it returns to the key
    # slot, and the readout previews that slot's topic without the count line.
    if (got := settled()) != want(None) or readout() != f"{topic}|":
        fails.append(f"home: Escape leaves {got}, key {readout()}")
    if page.evaluate("document.activeElement?.dataset?.t") != topic:
        fails.append("home: Escape does not return focus to the topic's key slot")
    if len(got := page.evaluate(lit_map)) != page.locator("[data-tmap] .cluster").count():
        fails.append(f"home: Escape leaves only map clusters {got} bright")
    page.locator(f"{entries_js} .tstrip summary").last.click()
    name = page.locator(f"{entries_js} .tstrip[open] .tname").first
    picked = name.get_attribute("data-t") or ""
    name.click()
    if (got := settled()) != want(picked):
        fails.append(f"home: picking {picked} from a strip shows {got}")
    page.locator(".tclear").click()
    # Focus returns to the key slot, which previews its topic without the count line.
    if (got := settled()) != want(None) or readout() != f"{picked}|":
        fails.append(f"home: Show all leaves {got}, key {readout()}")
    if page.evaluate("document.activeElement?.dataset?.t") != picked:
        fails.append("home: Show all does not return focus to the topic's key slot")
    nojs = new_page(browser, js=False)
    go(nojs, base + "/")
    if nojs.locator(".tkey").is_visible():
        fails.append("home: the topic key shows without the script")
    if not nojs.locator(".tintro").is_visible():
        fails.append("home: the topic-strip explanation is missing without the script")
    if nojs.locator(f"{entries_js} .tstrip").count() != len(entries):
        fails.append("home: strips missing without the script")
    if nojs.locator(".tname:not([disabled])").count():
        fails.append("home: topic names are live buttons without the script")
    return fails


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
        # Pop-ups and folded details hold text a reader reveals; check it too (review F6).
        body += " ".join(
            page.eval_on_selector_all(".qpop, details", "els => els.map(e => e.textContent)")
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
        for t in page.eval_on_selector_all(".fcard h3", "els => els.map(e => e.textContent)"):
            fails += hit_lines("title", path, t)
        for sel, name in (
            (".fcard", "card"),
            (".chip, .chipwrap .note", "chip"),
            (".qpop", "pop-up"),
        ):
            texts = page.eval_on_selector_all(
                sel,
                """(els, sel) => els.map(e => {
                    const c = e.cloneNode(true);
                    // The footer and topic strip name reports and topics, not the card's words.
                    const skip = 'h3, .meta, .tstrip';
                    if (sel === '.fcard') c.querySelectorAll(skip).forEach(h => h.remove());
                    // So do a pop-up's project and topic labels, such as "Statistical Confounding".
                    const labels = '.qpname, .qptopic';
                    if (sel === '.qpop') c.querySelectorAll(labels).forEach(h => h.remove());
                    return c.textContent;
                })""",
                sel,
            )
            counts[name] += len(texts)
            if path == "/findings/" and name == "card" and not texts:
                fails.append("plain: /findings/ has no .fcard to inspect")
            if path == "/directions/" and name == "pop-up" and not texts:
                fails.append("plain: /directions/ has no .qpop to inspect")
            for t in texts:
                fails += hit_lines(name, path, t)
    PLAIN_COUNTS.update(counts, pages=len(paths))
    return fails


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
    hrefs = nojs.eval_on_selector_all("a.qdot", "els => els.map(e => e.href)")
    if len(hrefs) != len(want):
        fails.append(f"grid: no-JS page has {len(hrefs)} dots, expected {len(want)}")
    for h in hrefs:
        try:
            code = urllib.request.urlopen(h, timeout=20).status
        except urllib.error.HTTPError as e:
            code = e.code
        if code != 200:
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
    # The first plain (unringed) dot, whose fading must not reach its pop-up.
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
    # Each dot's accessible name carries its approach (review F12).
    names = page.eval_on_selector_all(
        ".qgrid .qd",
        "els => els.map(e => [e.querySelector('a.qdot').getAttribute('aria-label'), "
        "e.querySelector('a.qdot').dataset.shape])",
    )
    approaches = {
        "lakehouse analysis": "Analysis of existing data",
        "experiment": "Experiment",
        "analysis then experiment": "Analysis, then experiment",
    }
    for name, shape in names:
        if shape in approaches and approaches[shape] not in (name or ""):
            fails.append(f"grid: dot '{(name or '')[:50]}' does not name its approach")
            break

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

    for path in ("/", "/findings/", "/directions/"):
        narrow = new_page(browser, PHONE)
        go(narrow, base + path)
        sw, iw = narrow.evaluate("[document.documentElement.scrollWidth, window.innerWidth]")
        if sw > iw:
            fails.append(f"grid: {path} at 390 px scrollWidth {sw} > innerWidth {iw}")
    return fails


def check_pages(browser, base: str) -> list[str]:
    fails: list[str] = []
    page = new_page(browser)
    full = 0
    for fid in ids("findings")[:10]:
        go(page, f"{base}/findings/{fid}")
        heads = page.eval_on_selector_all("h2", "els => els.map(e => e.textContent.trim())")
        order = [FINDING_HEADINGS.index(h) for h in heads if h in FINDING_HEADINGS]
        if order != sorted(order):
            fails.append(f"pages: {fid}: headings out of order: {heads}")
        for required in FINDING_HEADINGS[:3]:
            if required not in heads:
                fails.append(f"pages: {fid}: lacks '{required}': {heads}")
        full += all(h in heads for h in FINDING_HEADINGS)
    if not full:
        fails.append("pages: no checked finding page has all five section headings")

    go(page, base + "/findings/")
    h1 = page.eval_on_selector_all("h1", "els => els.map(e => e.textContent.trim())")
    if h1 != ["Results"]:
        fails.append(f"pages: /findings/ title {h1}, expected ['Results']")
    chips = page.eval_on_selector_all(
        ".c-chips .c-chip", "els => els.map(e => e.textContent.trim())"
    )
    if chips != KIND_CHIPS:
        fails.append(f"pages: /findings/ filter chips {chips}, expected {KIND_CHIPS}")
    groups = page.eval_on_selector_all(".c-chips", "els => els.map(e => e.dataset.filterGroup)")
    if "label" in groups:
        fails.append(f"pages: /findings/ still has a label chip group: {groups}")
    # Filter chips say which is on and the group has a name (review F11).
    state = page.eval_on_selector_all(
        ".c-chips[data-filter-group=kind]",
        "els => els.map(g => [g.getAttribute('aria-label'), "
        "[...g.querySelectorAll('.c-chip')].map(b => b.getAttribute('aria-pressed'))])",
    )
    if not state or not state[0][0] or state[0][1][:1] != ["true"]:
        fails.append(f"pages: kind chips lack a group name or aria-pressed: {state}")
    page.locator(".c-chips .c-chip").nth(1).click()
    pressed = page.eval_on_selector_all(
        ".c-chips .c-chip", "els => els.map(b => b.getAttribute('aria-pressed'))"
    )
    if pressed[:2] != ["false", "true"]:
        fails.append(f"pages: aria-pressed does not follow the chosen chip: {pressed}")
    fails += contrast(browser, base)
    # No card footer shows its separator alone on a line at phone width (review P3c).
    narrow = new_page(browser, PHONE)
    go(narrow, base + "/findings/")
    lone = narrow.evaluate(
        "[...document.querySelectorAll('.fcard .meta > *')]"
        ".filter(e => e.textContent.trim() === '·').length"
    )
    if lone:
        fails.append(f"pages: {lone} card footers have a separator on its own")
    return fails


def luminance(rgb: tuple[float, ...]) -> float:
    def ch(v: float) -> float:
        v /= 255
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4

    r, g, b = (ch(v) for v in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(browser, base: str) -> list[str]:
    """Small labels reach 4.5:1 against their background in light mode (review F13)."""
    fails = []
    page = browser.new_context(viewport=DESKTOP, color_scheme="light").new_page()
    seen = 0
    for path in ("/", "/findings/", "/directions/"):
        go(page, base + path)
        pairs = page.evaluate(
            """sels => sels.flatMap(sel => [...document.querySelectorAll(sel)]
              .slice(0, 3).map(e => {
                if (!e.offsetParent) return null;
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
            }))""",
            LIGHT_LABELS,
        )
        for sel, fg, bg in [x for x in pairs if x]:
            nums = [tuple(float(x) for x in re.findall(r"[\d.]+", c)[:3]) for c in (fg, bg)]
            if len(nums[0]) < 3 or len(nums[1]) < 3:
                continue
            a, b = sorted((luminance(nums[0]), luminance(nums[1])), reverse=True)
            ratio = (a + 0.05) / (b + 0.05)
            seen += 1
            if ratio < 4.5:
                fails.append(f"pages: {path} {sel} contrast {ratio:.2f}:1 ({fg} on {bg})")
    if not seen:
        fails.append("pages: no small label found to measure")
    return sorted(set(fails))


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


def check_cross(browser, base: str) -> list[str]:
    """The shared-result cards, question bridges and Results picture (done check 4)."""
    fails: list[str] = []
    page, errors = watched(browser)
    go(page, base + "/findings/")
    cards = page.locator(".scard")
    n = cards.count()
    accepted = sum(
        1
        for g in json.loads((ROOT / "state/shared.json").read_text()).values()
        if not g.get("failed")
    )
    if not 1 <= n <= accepted:
        fails.append(f"cross: Results page has {n} shared cards, expected 1 to {accepted}")
    index = ROOT / "quartz/content/findings/index.md"
    titles = sorted(
        (frontmatter(index).get("project_titles") or {}).values(), key=len, reverse=True
    )
    for i in range(n):
        card = cards.nth(i)
        kicker = card.locator(".skicker").inner_text()
        m = re.search(r"(\d+) projects · (\d+) topics", kicker, re.I)
        if not m or int(m[1]) < 2 or int(m[2]) < 2:
            fails.append(f"cross: shared card {i + 1} kicker '{kicker}'")
        card.locator(".scmp").click()
        panel = page.locator(".spanel:not([hidden])")
        if panel.count() != 1:
            fails.append(f"cross: shared card {i + 1} opens {panel.count()} panels")
            continue
        # The panel opens under its card's row: no card sits between the two.
        top = panel.bounding_box()["y"]
        mine = card.bounding_box()["y"]
        between = page.evaluate(
            "([lo, hi]) => [...document.querySelectorAll('.scard')]"
            ".map(c => c.getBoundingClientRect().y).filter(y => y > lo && y < hi).length",
            [mine + 1, top],
        )
        if between:
            fails.append(f"cross: shared card {i + 1} panel opens {between} cards below it")
        lanes = panel.locator(".slane").count()
        if lanes < 2:
            fails.append(f"cross: shared card {i + 1} panel has {lanes} lanes")
        # The statement's own words, not its member results' titles and summaries, which
        # can say "independent" about biology.
        own = panel.evaluate(
            "e => { const c = e.cloneNode(true); c.querySelectorAll('.smini')"
            ".forEach(m => m.remove()); return c.textContent }"
        )
        said = card.inner_text() + " " + own
        # Report titles name methods ("Independent Component Analysis"), not a relation.
        for title in titles:
            said = said.replace(title, "")
        if hit := CONFIRM.search(said):
            fails.append(f"cross: shared card {i + 1} says '{hit[0]}'")
    go(page, base + "/")
    qs = page.eval_on_selector_all(".xqlist li .xqp", "els => els.map(e => e.textContent)")
    if len(qs) != 3:
        fails.append(f"cross: home lists {len(qs)} cross-project questions, expected 3")
    named = [p for q in qs for p in q.removeprefix("Builds on ").split(" · ")]
    if len(named) != len(set(named)):
        fails.append("cross: a project appears in two home questions")

    go(page, base + "/directions/")
    rings = page.locator(".qgrid .qd.cross")
    crossing = sum(
        bool(frontmatter(p).get("cross"))
        for p in (ROOT / "quartz/content/directions").glob("*.md")
        if p.stem != "index"
    )
    if rings.count() != crossing:
        fails.append(f"cross: {rings.count()} ringed questions, the records give {crossing}")
    for i in range(rings.count()):
        projects = rings.nth(i).locator(".qproj")
        links = [projects.nth(j).locator(".qpres a").count() for j in range(projects.count())]
        if len(links) < 2 or min(links) < 1:
            fails.append(f"cross: ringed question {i + 1} bridge has projects {links}")

    go(page, base + "/findings/")
    # Expected counts come from the published records: publish marks some findings
    # unlisted, and those stay off the picture.
    listed = [
        fm
        for p in sorted((ROOT / "quartz/content/findings").glob("*.md"))
        if p.stem != "index" and (fm := frontmatter(p)).get("listed") is not False
    ]
    too_little = sum(fm.get("label") == "Insufficient literature evidence" for fm in listed)
    dots = page.locator(".nvmap .nd").count()
    none = page.locator(".nvmap .nbead.nv-none .nd").count()
    if dots != len(listed) or none != too_little:
        fails.append(
            f"cross: picture has {dots} dots and {none} with too little evidence; "
            f"the records list {len(listed)} and {too_little}"
        )
    if page.locator("svg.nvlinks path").count():
        fails.append("cross: links are drawn before any interaction")
    # A result's card follows the questions grid: it stays, on the same result, while the
    # pointer moves onto it past neighbouring dots; a click pins it without pinning the
    # project; a pinned card survives hovering other dots and a resize, until Escape.
    card = page.locator(".nvtip:not(.pin)")
    pinned = page.locator(".nvtip.pin")
    marks = page.locator(".nvmap .nd")
    href_of = "id => JSON.parse(document.querySelector('.nvdata').textContent).findings[id]"
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
    sdot = small.locator(".nvmap .nd").first
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
    dot = tap.locator(".nvmap .nd").first
    dot.scroll_into_view_if_needed()
    dot.tap()
    tap.wait_for_timeout(300)
    tcard = tap.locator(".nvtip.pin")
    if not tcard.is_visible() or not tcard.locator("a.nvopen").count():
        fails.append("cross: a tap on a result dot does not open its card, as on questions")
    rows = page.eval_on_selector_all(".nvrowh", "els => els.map(e => e.textContent.trim())")
    infra = [r for r in rows if r.startswith("Data Infrastructure")]
    filed = sum(
        fm.get("topic") == "data-infrastructure-provenance-and-research-practice" for fm in listed
    )
    if not infra or not infra[0].endswith(f" {filed}"):
        fails.append(f"cross: Data Infrastructure row reads {infra}, expected {filed}")
    expected = page.evaluate(
        """() => {
            const data = JSON.parse(document.querySelector('.nvdata').textContent);
            const groups = [...document.querySelectorAll('.nbead')];
            const has = id => groups.some(g => g.querySelector(`.nd[data-id="${id}"]`));
            const hasP = sid => groups.some(g => g.dataset.p === sid);
            const sid = 'conservation_fitness_synthesis';
            const mine = data.links.filter(l => l.pa === sid || l.pb === sid);
            const drawable = mine.filter(l =>
                (l.a ? has(l.a) : hasP(l.pa)) && (l.b ? has(l.b) : hasP(l.pb)));
            return drawable.length;
        }"""
    )
    group = page.locator(".nbead[data-p=conservation_fitness_synthesis]").first
    group.scroll_into_view_if_needed()
    group.hover()
    hovered = page.locator("svg.nvlinks path").count()
    page.mouse.move(0, 0)
    group.focus()
    focused = page.locator("svg.nvlinks path").count()
    if not hovered or not hovered == expected == focused:
        fails.append(f"cross: hover drew {hovered}, focus {focused}, of {expected} drawable links")
    page.keyboard.press("Escape")
    off = page.locator(".nbead[data-p=nmdc_context_audit]").first
    if off.count():
        # The box's edge, not a dot: a dot click pins that result's card instead.
        off.click(position={"x": 2, "y": 2})
        if "(no results in this picture)" not in page.locator(".nvpanel").inner_text():
            fails.append("cross: the audit of a project without results is not listed")
    else:
        fails.append("cross: no group for nmdc_context_audit")
    # A comparison still opens after navigating away and back: Quartz reuses nodes,
    # so a second set of listeners would open and close it in one click.
    go(page, base + "/")
    page.locator("a.kindcard[href$='findings/']").first.click()
    page.wait_for_url("**/findings/**")
    page.wait_for_selector(".scard")
    page.locator("a.nvrowh").first.click()
    page.wait_for_url("**/topics/**")
    page.go_back()
    page.wait_for_selector(".scard")
    page.locator(".scmp").first.click()
    if page.locator(".spanel:not([hidden])").count() != 1:
        fails.append("cross: a comparison does not open after navigating away and back")
    fails += [f"cross: light: {e}" for e in errors]

    dark, dark_errors = watched(browser, scheme="dark")
    for path in ("/", "/findings/", "/directions/"):
        go(dark, base + path)
    fails += [f"cross: dark: {e}" for e in dark_errors]
    for path in ("/", "/findings/", "/directions/"):
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


CHECKS = {
    "home": check_home,
    "plain": check_plain,
    "grid": check_grid,
    "pages": check_pages,
    "cross": check_cross,
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
