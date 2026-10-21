// The wiki's search, Ask and navigation behaviour in the browser. The theme
// renders the markup (src/components); this script wires it up: the section
// search palette, the CBORG key dialog, Ask and "Ask about this page", count
// popovers in the record header, and the collection toolbars. Everything runs
// client-side, so it works on the static GitHub Pages site.
import MiniSearch, { type SearchResult } from "minisearch"
import { type IndexFile, PAGE_OPTIONS, type Page, type PagesFile, SEARCH_DEPTH, SECTION_OPTIONS, type Section, type SectionFile, processTerm, tokenize } from "../search/config"
import { type ChatMessage, ensureKey, loadSettings, modelLabel, onSettingsChange, openSettings, statusLine, streamChat } from "./ai"
import { fuse, meaningError, meaningLoading, meaningPaused, meaningProgress, meaningRank, meaningStatus, onMeaningChange, setMeaningWanted } from "./semantic"
import { asset, currentSlug, esc, pageHref as href, session, slugOfHref, titleHtml as title } from "./site"

// ---------------------------------------------------------------- data

interface Index {
  /** the site update all four files came from; the meaning vectors must match it too */
  build: string
  pages: Page[]
  sections: Section[]
  sectionIndex: MiniSearch
  pageIndex: MiniSearch
}

let pagesReady: Promise<PagesFile> | null = null
let pages: Page[] = []
let bySlug = new Map<string, Page>()
let indexReady: Promise<Index> | null = null
let indexLoaded = false

const getJson = <T>(file: string, init?: RequestInit): Promise<T> =>
  fetch(asset(file), init).then((r) => {
    if (!r.ok) throw new Error(`The search index did not load (${file}: HTTP ${r.status}).`)
    return r.json()
  })

function usePages(list: Page[]) {
  pages = list
  bySlug = new Map(pages.map((p) => [p.slug, p]))
}

// A failed download is forgotten, so the next search tries again instead of failing for the life of the tab.
function loadPages(): Promise<PagesFile> {
  pagesReady ??= getJson<PagesFile>("pages.json").catch((e) => {
    pagesReady = null
    throw e
  })
  return pagesReady
}

async function ensurePages() {
  if (pages.length) return
  const file = await loadPages()
  if (!pages.length) usePages(file.pages)
}

async function fetchIndex(init?: RequestInit): Promise<Index | null> {
  const [p, s, si, pi] = await Promise.all([
    getJson<PagesFile>("pages.json", init),
    getJson<SectionFile>("sections.json", init),
    getJson<IndexFile>("section-index.json", init),
    getJson<IndexFile>("page-index.json", init),
  ])
  if (![s.build, si.build, pi.build].every((b) => b === p.build)) return null
  return {
    build: p.build,
    pages: p.pages,
    sections: s.sections,
    sectionIndex: MiniSearch.loadJS(si.index as never, SECTION_OPTIONS),
    pageIndex: MiniSearch.loadJS(pi.index as never, PAGE_OPTIONS),
  }
}

function loadIndex(): Promise<Index> {
  indexReady ??= (async () => {
    // Files from two site updates (some still cached) are fetched once more past the cache.
    const ix = (await fetchIndex()) ?? (await fetchIndex({ cache: "no-cache" }))
    if (!ix) throw new Error("The search files are from two different site updates. Reload the page.")
    // Search joins sections to pages by slug and page hits by position, so both come from this build.
    usePages(ix.pages)
    indexLoaded = true
    return ix
  })().catch((e) => {
    indexReady = null
    throw e
  })
  return indexReady
}

// Quartz's SPA navigation morphs the page in place and keeps matching nodes, data
// attributes stripped. A listener added on every visit would stack, so each node
// gets one listener per event that calls the handler set most recently.
const handlers = new WeakMap<Element, Map<string, (e: Event) => void>>()
function on(el: Element, type: string, fn: (e: Event) => void) {
  let byType = handlers.get(el)
  if (!byType) handlers.set(el, (byType = new Map()))
  if (!byType.has(type)) el.addEventListener(type, (e) => byType!.get(type)?.(e))
  byType.set(type, fn)
}

// Streams in flight, so leaving the page or starting over stops spending the reader's tokens.
const streams = new Set<AbortController>()

const GROUPS: [string, string][] = [
  ["topic", "Topics"],
  ["concept", "Concepts"],
  ["entity", "Entities"],
  ["conflict", "Conflicts"],
  ["report", "Reports"],
  ["source", "Raw reports"],
  ["other", "Other pages"],
]
const TAG: Record<string, string> = {
  topic: "Topic", concept: "Concept", entity: "Entity", conflict: "Conflict", report: "Report", source: "Raw report", other: "Page",
}
// Synthesis pages answer most questions; raw reports repeat them at length.
const GROUP_BOOST: Record<string, number> = { topic: 1.1, concept: 1.15, entity: 1.1, conflict: 1, report: 1, source: 0.7, other: 0.6 }

const here = currentSlug
const route = () => (["ask", "guide"].includes(here()) ? here() : "")
// A question the reader typed in search or the page drawer, carried to the Ask page so it is asked on arrival.
const ASK_HANDOFF = "px-ask"
const SEARCH_SVG = `<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="8.5" cy="8.5" r="6.5"/><path d="M13.5 13.5 18 18"/></svg>`

// ---------------------------------------------------------------- search

interface Hit {
  sec: Section
  page: Page
  score: number
  /** found by meaning only, with no keyword match */
  byMeaning?: boolean
}

function queryTerms(q: string): string[] {
  return [...new Set(tokenize(q).map((t) => processTerm(t)).filter((t): t is string => !!t))]
}

function searchSections(ix: Index, q: string, filter?: (p: Page) => boolean, limit = 60): Hit[] {
  const opts = {
    prefix: (t: string) => t.length > 2,
    fuzzy: (t: string) => (t.length > 5 ? 0.15 : 0),
    boost: { title: 2, path: 3, aliases: 4, text: 1 },
    boostDocument: (id: unknown) => {
      const s = ix.sections[id as number]
      return GROUP_BOOST[bySlug.get(s.s)?.group ?? "other"] ?? 1
    },
    filter: filter ? (r: SearchResult) => filter(bySlug.get(ix.sections[r.id as number].s)!) : undefined,
  }
  let res = ix.sectionIndex.search(q, { ...opts, combineWith: "AND" })
  if (res.length < 8) {
    const seen = new Set(res.map((r) => r.id))
    res = res.concat(ix.sectionIndex.search(q, { ...opts, combineWith: "OR" }).filter((r) => !seen.has(r.id)).map((r) => ({ ...r, score: r.score * 0.5 })))
  }
  return res.slice(0, limit).map((r) => {
    const sec = ix.sections[r.id as number]
    return { sec, page: bySlug.get(sec.s)!, score: r.score }
  })
}

// Keyword hits, merged with meaning-ranked ones when meaning search is on (or
// always, for Ask). On a 258-query test set the merge put an answering section
// first for 86% of queries against 83% for keywords alone.
async function hybridSearch(
  ix: Index,
  q: string,
  filter?: (p: Page) => boolean,
  limit = SEARCH_DEPTH,
  always = false,
): Promise<{ hits: Hit[]; meaning: boolean }> {
  const kw = searchSections(ix, q, filter, limit)
  const vec = await meaningRank(q, limit, ix.build, filter ? (id) => filter(bySlug.get(ix.sections[id].s)!) : undefined, always)
  if (!vec.length) return { hits: kw, meaning: false }
  const scores = fuse([kw.map((h) => h.sec.i), vec])
  const kwIds = new Set(kw.map((h) => h.sec.i))
  const hits = [...scores.entries()]
    .sort((a, b) => b[1] - a[1])
    .slice(0, limit)
    .map(([id, score]) => {
      const sec = ix.sections[id]
      return { sec, page: bySlug.get(sec.s)!, score, byMeaning: !kwIds.has(id) }
    })
  return { hits, meaning: true }
}

// The search box's meaning switch. Off by default; on, it sends each query (after
// typing pauses) to CBORG with the reader's key, so it asks for a key first.
function meaningControl(el: HTMLElement, onChange: () => void) {
  const TITLE = "Also rank sections by meaning. Sends your query to CBORG with your own key."
  const paint = () => {
    const st = meaningStatus()
    const { loaded, total } = meaningProgress()
    const mb = (b: number) => (b / 1e6).toFixed(1)
    const button = (label: string, act: string, pressed: boolean) =>
      `<button type="button" class="px-meaning" aria-pressed="${pressed}" data-act="${act}" title="${TITLE}">${label}</button>`
    el.innerHTML =
      st === "loading" ? `<span class="px-meaning-status">Loading meaning search${total ? `: ${mb(loaded)} of ${mb(total)} MB` : "…"}</span>`
      : st === "on" ? button("Meaning search: on", "off", true)
      : st === "nokey" ? button("Meaning search: add your CBORG key", "key", false)
      : st === "paused" ? button("Meaning search paused (CBORG rate limit)", "off", true)
      : st === "failed" ? button(`Meaning search unavailable: ${esc(meaningError())}. Retry`, "on", false)
      : button("Meaning search: off", "on", false)
    el.querySelector<HTMLButtonElement>("[data-act]")?.addEventListener("click", async (e) => {
      const act = (e.currentTarget as HTMLElement).dataset.act
      if ((act === "on" || act === "key") && !loadSettings().key) {
        if (!(await openSettings("Meaning search sends your query to CBORG with your own key. Add it once; Ask uses it too."))) return
      }
      setMeaningWanted(act !== "off")
      onChange()
    })
  }
  paint()
  onMeaningChange(() => {
    if (document.body.contains(el)) paint()
  })
  onSettingsChange(() => {
    if (document.body.contains(el)) paint()
  })
}

// Ask always ranks by keywords and meaning, since it already has the reader's key. The
// search box's switch does not apply to it, so the Ask page says how it ranks instead.
function askRanking(el: HTMLElement) {
  const paint = () => {
    if (!document.body.contains(el)) return
    const { loaded, total } = meaningProgress()
    const mb = (b: number) => (b / 1e6).toFixed(1)
    el.textContent = meaningLoading()
      ? `Loading meaning search${total ? `: ${mb(loaded)} of ${mb(total)} MB` : "…"}`
      : meaningPaused()
        ? "Ranking by keywords only for a minute: CBORG's rate limit was reached"
        : meaningError()
          ? `Ranking by keywords only: ${meaningError()}`
          : "Sections are ranked by keywords and meaning"
  }
  paint()
  onMeaningChange(paint)
}

function snippet(text: string, terms: string[], words = 30): string {
  const toks = text.replace(/\n/g, " ").split(/\s+/)
  const hit = (w: string) => {
    const t = processTerm(w)
    return !!t && terms.some((q) => t.startsWith(q) || (q.length > 4 && t.startsWith(q.slice(0, -1))))
  }
  let best = 0
  let bestAt = 0
  for (let i = 0; i < toks.length; i++) {
    let n = 0
    for (let j = i; j < Math.min(toks.length, i + words); j++) if (hit(toks[j])) n++
    if (n > best) [best, bestAt] = [n, i]
  }
  const start = Math.max(0, bestAt - 4)
  const slice = toks.slice(start, start + words)
  const body = slice.map((w) => (hit(w) ? `<mark>${esc(w)}</mark>` : esc(w))).join(" ")
  return `${start > 0 ? "…" : ""}${body}${start + words < toks.length ? "…" : ""}`
}

// ---------------------------------------------------------------- palette

let pal: HTMLElement | null = null
let palState = { scope: "all", sel: 0, rows: [] as { url: string }[], q: "" }
// Each run takes a number; a run that finishes after a newer one (same text, other scope
// or meaning setting) must not repaint the results.
let palGen = 0

function ensurePalette(): HTMLElement {
  if (pal && document.body.contains(pal)) return pal
  pal = document.createElement("div")
  pal.className = "px-pal"
  pal.innerHTML = `<div class="px-pal-box" role="dialog" aria-modal="true" aria-label="Search the wiki">
    <div class="px-pal-in">${SEARCH_SVG}<input type="text" placeholder="Search sections: a gene, organism, method or claim" aria-label="Search sections" autocomplete="off"><kbd>Esc</kbd></div>
    <div class="px-scopes" role="toolbar" aria-label="Limit to"></div>
    <div class="px-results" role="listbox" aria-label="Results"></div>
    <div class="px-pal-foot"><span class="px-keys">↑↓ move · ↵ open · Alt+←/→ scope</span><span class="px-stat"></span><span class="px-meaning-ctl"></span><a class="px-handoff" href="${href("ask")}">Ask the wiki instead →</a></div>
  </div>`
  document.body.append(pal)
  const box = pal
  const input = box.querySelector("input")!
  meaningControl(box.querySelector<HTMLElement>(".px-meaning-ctl")!, () => runPalette(input.value))
  // When meaning search becomes available (vectors loaded, key added), rerank the open query.
  let lastStatus = meaningStatus()
  onMeaningChange(() => {
    const st = meaningStatus()
    // A palette that navigation removed keeps this listener; only the current one reranks.
    if (box === pal && st === "on" && lastStatus !== "on" && box.classList.contains("open") && input.value.trim()) runPalette(input.value, true)
    lastStatus = st
  })
  box.addEventListener("mousedown", (e) => {
    if (e.target === box) closePalette()
  })
  // The handoff is a plain link that Quartz's router follows; close first, or the page stays unscrollable.
  box.querySelector(".px-handoff")!.addEventListener("click", () => {
    if (input.value.trim()) session.set(ASK_HANDOFF, input.value.trim())
    closePalette()
  })
  // Keyword results follow every keystroke; meaning reranks only once typing pauses,
  // because each meaning query is a CBORG request against the reader's 20 a minute.
  let timer = 0
  let meaningTimer = 0
  input.addEventListener("input", () => {
    clearTimeout(timer)
    clearTimeout(meaningTimer)
    timer = window.setTimeout(() => runPalette(input.value, false), 70)
    if (meaningStatus() === "on") meaningTimer = window.setTimeout(() => runPalette(input.value, true), 600)
  })
  input.addEventListener("keydown", (e) => {
    const n = palState.rows.length
    if (e.key === "ArrowDown") palState.sel = Math.min(n - 1, palState.sel + 1)
    else if (e.key === "ArrowUp") palState.sel = Math.max(0, palState.sel - 1)
    else if (e.key === "Enter") {
      const row = palState.rows[palState.sel]
      if (row) go(row.url)
      e.preventDefault()
      return
    } else if (e.altKey && (e.key === "ArrowRight" || e.key === "ArrowLeft")) {
      const chips = [...pal!.querySelectorAll<HTMLButtonElement>(".px-scopes .px-chip")]
      const i = chips.findIndex((c) => c.dataset.scope === palState.scope)
      const next = chips[(i + (e.key === "ArrowLeft" ? chips.length - 1 : 1)) % chips.length]
      palState.scope = next.dataset.scope!
      runPalette(input.value)
      e.preventDefault()
      return
    } else return
    e.preventDefault()
    paintSelection()
  })
  // Tab moves through the dialog's controls and wraps, so focus never leaves it.
  pal.addEventListener("keydown", (e) => {
    if (e.key === "Escape") return closePalette()
    if (e.key !== "Tab") return
    const focusable = [...pal!.querySelectorAll<HTMLElement>("input, button, a[href]")].filter((x) => x.offsetParent !== null)
    const i = focusable.indexOf(document.activeElement as HTMLElement)
    const next = focusable[(i + (e.shiftKey ? focusable.length - 1 : 1)) % focusable.length]
    next?.focus()
    e.preventDefault()
  })
  return pal
}

function scopesFor(): [string, string][] {
  const p = bySlug.get(here())
  const s: [string, string][] = [["all", "All"], ...GROUPS.slice(0, 6)]
  if (p && p.group !== "other") s.splice(1, 0, ["page", "This page"])
  return s
}

function openPalette(q = "") {
  const el = ensurePalette()
  el.classList.add("open")
  document.documentElement.style.overflow = "hidden"
  const input = el.querySelector("input")!
  input.value = q
  palState.scope = "all"
  input.focus()
  runPalette(q)
}

function closePalette() {
  pal?.classList.remove("open")
  document.documentElement.style.overflow = ""
}

function go(url: string) {
  closePalette()
  const [path, anchor] = url.split("#")
  if (anchor) session.set("px-land", anchor)
  if (path === location.pathname && anchor) {
    landOn(anchor)
    history.replaceState(null, "", url)
  } else location.assign(url)
}

async function runPalette(q: string, withMeaning = meaningStatus() === "on") {
  const el = ensurePalette()
  const gen = ++palGen
  palState.q = q
  const scopes = scopesFor()
  el.querySelector(".px-scopes")!.innerHTML = scopes
    .map(([k, v]) => `<button class="px-chip" data-scope="${k}" aria-pressed="${k === palState.scope}">${v}</button>`)
    .join("")
  el.querySelectorAll<HTMLButtonElement>(".px-scopes .px-chip").forEach((b) =>
    b.addEventListener("click", () => {
      palState.scope = b.dataset.scope!
      runPalette((el.querySelector("input") as HTMLInputElement).value)
      ;(el.querySelector("input") as HTMLInputElement).focus()
    }),
  )
  const handoff = el.querySelector<HTMLAnchorElement>(".px-handoff")!
  handoff.href = q.trim() ? `${href("ask")}?q=${encodeURIComponent(q.trim())}` : href("ask")
  const out = el.querySelector(".px-results")!
  const stat = el.querySelector(".px-stat")!
  if (!q.trim()) {
    palState.rows = []
    stat.textContent = ""
    out.innerHTML = `<div class="px-empty">Results are sections, not whole pages, so Enter lands on the paragraph. Try:
      <div>${["DvH", "nitrate", "essentiality calls disagree", "pangenome openness", "phage receptor", "RB-TnSeq threshold"]
        .map((x) => `<button class="px-chip" data-try="${esc(x)}">${esc(x)}</button>`)
        .join("")}</div></div>`
    out.querySelectorAll<HTMLButtonElement>("[data-try]").forEach((b) =>
      b.addEventListener("click", () => {
        const input = el.querySelector("input") as HTMLInputElement
        input.value = b.dataset.try!
        runPalette(input.value)
        input.focus()
      }),
    )
    return
  }
  // Only the first search waits for the index; a meaning pass keeps the keyword rows up meanwhile.
  if (!indexLoaded) out.innerHTML = `<div class="px-empty">Loading the section index…</div>`
  let ix: Index
  try {
    ix = await loadIndex()
  } catch (e) {
    if (gen !== palGen) return
    out.innerHTML = `<div class="px-empty">${esc((e as Error).message)} <button class="px-chip" type="button">Try again</button></div>`
    out.querySelector("button")!.addEventListener("click", () => runPalette(q, withMeaning))
    return
  }
  if (gen !== palGen) return
  const terms = queryTerms(q)
  const current = here()
  const scope = palState.scope
  const filter = scope === "all" ? undefined : scope === "page" ? (p: Page) => p.slug === current : (p: Page) => p.group === scope
  const hits = withMeaning ? (await hybridSearch(ix, q, filter, SEARCH_DEPTH)).hits : searchSections(ix, q, filter, SEARCH_DEPTH)
  if (gen !== palGen) return

  // Pages whose title or alias matches every term go first, as "go to page" rows.
  const pins =
    scope === "page"
      ? []
      : ix.pageIndex
          .search(q, { prefix: true, combineWith: "AND", fuzzy: (t: string) => (t.length > 5 ? 0.1 : 0) })
          .slice(0, 6)
          .map((r) => ({ page: ix.pages[r.id as number], viaAlias: Object.values(r.match).some((f) => f.includes("aliases") && !f.includes("title")) }))
          .filter((x) => x.page && (scope === "all" || x.page.group === scope))
          .slice(0, 3)

  const rows: string[] = []
  palState.rows = []
  const addRow = (url: string, html: string) => {
    rows.push(`<a class="px-row" href="${esc(url)}" data-i="${palState.rows.length}" role="option">${html}</a>`)
    palState.rows.push({ url })
  }
  if (pins.length) {
    rows.push(`<div class="px-pin">`)
    for (const { page, viaAlias } of pins) {
      const alias = viaAlias ? page.aliases.find((a) => terms.some((t) => a.toLowerCase().includes(t))) : ""
      addRow(
        href(page.slug),
        `<div class="px-path"><span class="px-tag ${page.group}">${esc(page.label || TAG[page.group])}</span>${title(page.title)}${
          alias ? `<span class="px-why">matched alias “${esc(alias)}”</span>` : ""
        }</div>${page.desc || page.first ? `<div class="px-snip">${esc(page.desc || page.first)}</div>` : ""}`,
      )
    }
    rows.push(`</div>`)
  }

  // One ranked list, best first, each row tagged with its page kind, at most two sections
  // per page. Grouping rows by kind put weaker matches above stronger ones: the source
  // section reached the first five rows for 71% of test queries grouped, 80% flat.
  const perPage = new Map<string, number>()
  const counts = new Map<string, number>()
  const shown: Hit[] = []
  // A long section is indexed in chunks that share its heading and anchor; show it once.
  const seen = new Set<string>()
  for (const h of hits) {
    const at = `${h.page.slug}#${h.sec.a}|${h.sec.p}`
    if (seen.has(at)) continue
    seen.add(at)
    counts.set(h.page.group, (counts.get(h.page.group) ?? 0) + 1)
    const n = perPage.get(h.page.slug) ?? 0
    if (scope === "all" && n >= 2) continue
    perPage.set(h.page.slug, n + 1)
    shown.push(h)
  }
  for (const h of shown.slice(0, 30)) {
    addRow(
      href(h.page.slug, h.sec.a),
      `<div class="px-path"><span class="px-tag ${h.page.group}">${esc(TAG[h.page.group])}</span>${title(h.page.title)}${
        h.sec.p ? ` <span class="h">› ${esc(h.sec.p)}</span>` : ""
      }${h.byMeaning ? `<span class="px-why">related by meaning</span>` : ""}</div><div class="px-snip">${snippet(h.sec.t, terms)}</div>`,
    )
  }
  out.innerHTML = rows.length ? rows.join("") : `<div class="px-empty">No section matches “${esc(q)}”. Try fewer words, or ask the wiki instead.</div>`
  stat.textContent = hits.length ? `${perPage.size} pages` : ""
  // The scope chips carry the per-kind counts the group headers used to show.
  if (scope === "all")
    el.querySelectorAll<HTMLButtonElement>(".px-scopes .px-chip").forEach((b) => {
      const n = counts.get(b.dataset.scope!)
      if (n) b.insertAdjacentHTML("beforeend", ` <span class="n">${n}</span>`)
    })
  out.querySelectorAll<HTMLAnchorElement>(".px-row").forEach((a) => {
    a.addEventListener("mousemove", () => {
      palState.sel = Number(a.dataset.i)
      paintSelection(false)
    })
    a.addEventListener("click", (e) => {
      e.preventDefault()
      e.stopPropagation()
      go(a.getAttribute("href")!)
    })
  })
  palState.sel = 0
  paintSelection()
}

function paintSelection(scroll = true) {
  pal?.querySelectorAll(".px-row").forEach((r, i) => {
    r.classList.toggle("sel", i === palState.sel)
    r.setAttribute("aria-selected", String(i === palState.sel))
    if (i === palState.sel && scroll) (r as HTMLElement).scrollIntoView({ block: "nearest" })
  })
}

// Outline the section a search result pointed at, up to the next heading.
function landOn(anchor: string) {
  const h = document.getElementById(anchor)
  if (!h) return
  const level = /^H[1-6]$/.test(h.tagName) ? Number(h.tagName[1]) : 9
  const els: Element[] = [h]
  for (let n = h.nextElementSibling; n && !(/^H[1-6]$/.test(n.tagName) && Number(n.tagName[1]) <= level); n = n.nextElementSibling) els.push(n)
  h.style.scrollMarginTop = "24px"
  h.scrollIntoView({ block: "start" })
  for (const e of els) {
    e.classList.remove("px-land")
    void (e as HTMLElement).offsetWidth
    e.classList.add("px-land")
  }
}

// ---------------------------------------------------------------- header bar

// The bar's markup is server-rendered (components/Bar.tsx); this paints the key
// button's state and opens the key dialog from it.
function paintKeyButton() {
  const k = document.querySelector<HTMLButtonElement>("header.bar .px-keybtn")
  if (!k) return
  const st = loadSettings()
  k.classList.toggle("set", !!st.key)
  const label = st.key ? `CBORG key set, answers use ${modelLabel(st.model)}. Change or forget it.` : "Add your CBORG key to ask the wiki"
  k.setAttribute("aria-label", label)
  k.title = label
}
onSettingsChange(paintKeyButton)

function wireBar() {
  const k = document.querySelector<HTMLButtonElement>("header.bar .px-keybtn")
  if (!k) return
  paintKeyButton()
  on(k, "click", () => openSettings())
}

// ---------------------------------------------------------------- record header

function railSection(title: RegExp): HTMLElement | null {
  return [...document.querySelectorAll<HTMLElement>(".evidence-rail section")].find((s) => title.test(s.querySelector("h3")?.textContent ?? "")) ?? null
}

function popover(anchor: HTMLElement, html: string) {
  document.querySelectorAll(".px-pop").forEach((p) => p.remove())
  const pop = document.createElement("div")
  pop.className = "px-pop"
  pop.innerHTML = html
  document.body.append(pop)
  const r = anchor.getBoundingClientRect()
  const left = Math.min(window.scrollX + r.left, window.scrollX + document.documentElement.clientWidth - pop.offsetWidth - 12)
  pop.style.left = `${Math.max(8, left)}px`
  pop.style.top = `${window.scrollY + r.bottom + 6}px`
  const close = (e: Event) => {
    if (e instanceof KeyboardEvent ? e.key === "Escape" : !pop.contains(e.target as Node) && e.target !== anchor) {
      pop.remove()
      document.removeEventListener("mousedown", close)
      document.removeEventListener("keydown", close)
    }
  }
  setTimeout(() => {
    document.addEventListener("mousedown", close)
    document.addEventListener("keydown", close)
  })
}

function linksIn(sec: HTMLElement | null): HTMLAnchorElement[] {
  return sec ? [...sec.querySelectorAll<HTMLAnchorElement>("a[href]")].filter((a) => (a.textContent ?? "").trim()) : []
}

function listHtml(links: { href: string; text: string; note?: string }[]) {
  return links.map((l) => `<a href="${esc(l.href)}">${esc(l.text)}${l.note ? ` <span class="px-why">${esc(l.note)}</span>` : ""}</a>`).join("")
}

function makeChip(chip: HTMLElement, onClick: (el: HTMLElement) => void) {
  chip.classList.add("px-link")
  chip.setAttribute("role", "button")
  chip.tabIndex = 0
  on(chip, "click", () => onClick(chip))
  on(chip, "keydown", (e) => {
    const k = (e as KeyboardEvent).key
    if (k === "Enter" || k === " ") {
      e.preventDefault()
      onClick(chip)
    }
  })
}

function wireRecord(page: Page) {
  const record = document.querySelector<HTMLElement>(".record")
  if (!record) return
  // The standfirst, kind line and this button are server-rendered (components/Record.tsx).
  const askBtn = record.querySelector(".px-askpage")
  if (askBtn) on(askBtn, "click", () => openDrawer(page))

  // Header counts become links to what they count.
  for (const dt of record.querySelectorAll("dl.facts dt")) {
    const label = (dt.textContent ?? "").trim()
    const dd = dt.nextElementSibling as HTMLElement | null
    if (!dd) continue
    const chips = [...dd.querySelectorAll<HTMLElement>("span.chip")]
    if (/^Linked from/.test(label)) {
      const sec = railSection(/^Linked from/)
      const items = linksIn(sec).map((a) => ({ href: a.href, text: a.textContent!.trim() }))
      for (const c of chips)
        makeChip(c, (el) =>
          popover(el, `<h4>Linked from · ${esc(chips.map((x) => x.textContent!.trim()).join(", "))}</h4>${listHtml(items)}`),
        )
    } else if (/^Conflicts?$/.test(label)) {
      const sec = railSection(/conflict/i)
      const named = new Set(pages.filter((p) => p.group === "conflict" && p.out.includes(page.slug)).map((p) => p.slug))
      const items = linksIn(sec).map((a) => {
        const slug = slugOfHref(a.href)
        return { href: a.href, text: a.textContent!.trim(), note: named.has(slug) ? "names this page" : "shares its sources", named: named.has(slug) }
      })
      // The rail lists at most four; add named conflicts it left out so the list matches the count.
      const listed = new Set(items.map((i) => slugOfHref(i.href)))
      for (const slug of named)
        if (!listed.has(slug)) items.push({ href: href(slug), text: bySlug.get(slug)?.title ?? slug, note: "names this page", named: true })
      items.sort((a, b) => Number(b.named) - Number(a.named))
      for (const c of chips)
        makeChip(c, (el) =>
          popover(
            el,
            `<h4>Open conflicts</h4><p>${named.size} name this page; ${items.length - items.filter((i) => i.named).length} more share its sources. The header counts the first kind.</p>${listHtml(items)}`,
          ),
        )
    } else if (/^Concepts$/.test(label)) {
      const items = linksIn(railSection(/^Concepts/)).map((a) => ({ href: a.href, text: a.textContent!.trim() }))
      for (const c of chips) makeChip(c, (el) => popover(el, `<h4>Concepts this topic gathers</h4>${listHtml(items)}`))
    } else if (/^Relations$/.test(label)) {
      // Each relation count steps through its occurrences in the text.
      for (const c of chips) {
        const rel = [...c.classList].find((x) => x.startsWith("rel-"))?.slice(4)
        if (!rel) continue
        let i = -1
        makeChip(
          c,
          () => {
            // A phrase such as "supports and refines" is coloured by its first word but counts for both.
            const hits = [...document.querySelectorAll<HTMLElement>(`article strong.rel[data-rels~="${rel}"]`)]
            if (!hits.length) return
            document.querySelectorAll(".px-relhit").forEach((x) => x.classList.remove("px-relhit"))
            i = (i + 1) % hits.length
            hits[i].classList.add("px-relhit")
            hits[i].scrollIntoView({ block: "center" })
          },
        )
      }
    }
  }
}

// ---------------------------------------------------------------- collections

function enhanceCollection() {
  const listing = document.querySelector<HTMLElement>(".listing")
  if (!listing || listing.previousElementSibling?.classList.contains("px-tools")) return
  const collection = here().split("/")[0]
  const cards = [...listing.querySelectorAll<HTMLAnchorElement>("a.card")]
  if (cards.length < 6) return
  const info = cards.map((a, i) => {
    const slug = slugOfHref(a.href)
    const p = bySlug.get(slug)
    const hay = `${a.textContent} ${p?.aliases.join(" ") ?? ""} ${p?.topic ?? ""}`.toLowerCase()
    return { a, i, p, hay, title: a.querySelector("b")?.textContent ?? "" }
  })
  // Facet by what distinguishes members of this collection.
  // Entities are coloured by kind and everything else by topic (theme Listing.tsx);
  // the chips use the same colours, so a chip's dot matches its cards' dots.
  const byKind = collection === "entities"
  const facetOf = (x: (typeof info)[number]) =>
    byKind ? x.p?.label ?? "Other"
    : ["concepts", "conflicts", "summaries"].includes(collection) ? x.p?.topic || "No topic"
    : ""
  const topicHue = new Map<string, string>()
  for (const p of pages) if (p.topic && p.hue && p.group === "concept" && !topicHue.has(p.topic)) topicHue.set(p.topic, p.hue)
  const KIND_HUE: Record<string, string> = {
    Organism: "var(--organism)", Method: "var(--method)", Dataset: "var(--dataset)", Compound: "var(--compound)", "Gene or pathway": "var(--gene)",
  }
  const hueOf = (f: string) => (byKind ? KIND_HUE[f] : topicHue.get(f)) ?? "var(--line-2)"
  const facetCounts = new Map<string, number>()
  for (const x of info) {
    const f = facetOf(x)
    if (f) facetCounts.set(f, (facetCounts.get(f) ?? 0) + 1)
  }
  const facets = [...facetCounts].sort((a, b) => b[1] - a[1])
  const params = new URLSearchParams(location.search)
  const state = { q: params.get("q") ?? "", facet: params.get("f") ?? "", sort: params.get("sort") ?? "rank", compact: params.get("view") === "list" }
  const noun = (document.querySelector(".record h1")?.textContent ?? "pages").trim().toLowerCase()

  const tools = document.createElement("div")
  tools.className = "px-tools"
  tools.innerHTML = `<div class="row1">
      <input type="search" placeholder="Filter ${esc(noun)} by title, description${collection === "entities" ? ", alias" : ""} or topic" aria-label="Filter ${esc(noun)}" value="${esc(state.q)}">
      <label class="count" style="display:flex;gap:6px;align-items:center">Sort <select aria-label="Sort"><option value="rank">${collection === "topics" ? "As on the home page" : "Most linked"}</option><option value="az">A–Z</option></select></label>
      <span class="px-seg" role="group" aria-label="View"><button type="button" data-v="cards">Cards</button><button type="button" data-v="list">List</button></span>
      <span class="count" aria-live="polite"></span>
    </div>
    ${facets.length > 1 ? `<div class="facets" role="group" aria-labelledby="px-facet-lbl"><span class="px-facet-lbl" id="px-facet-lbl">Filter by ${byKind ? "kind" : "topic"}</span>${[
      ["", "All", info.length] as [string, string, number],
      ...facets.map(([f, c]) => [f, f, c] as [string, string, number]),
    ]
      .map(([v, l, c]) => `<button class="px-chip" data-f="${esc(v)}">${v ? `<i class="dot" style="--c:${hueOf(v)}"></i>` : ""}${esc(l)} <span class="n">${c}</span></button>`)
      .join("")}</div>` : ""}`
  listing.before(tools)
  const input = tools.querySelector("input")!
  const select = tools.querySelector("select")!
  select.value = state.sort
  const count = tools.querySelector(".row1 .count:last-child")!
  const nomatch = document.createElement("div")
  nomatch.className = "px-nomatch px-hidden"
  listing.append(nomatch)

  const apply = () => {
    const terms = state.q.toLowerCase().split(/\s+/).filter(Boolean)
    let shown = 0
    for (const x of info) {
      const ok = terms.every((t) => x.hay.includes(t)) && (!state.facet || facetOf(x) === state.facet)
      x.a.classList.toggle("px-hidden", !ok)
      if (ok) shown++
    }
    for (const grid of listing.querySelectorAll<HTMLElement>(".cards")) {
      const kids = [...grid.querySelectorAll<HTMLAnchorElement>(":scope > a.card")]
      kids.sort((a, b) => {
        const A = info.find((x) => x.a === a)!
        const B = info.find((x) => x.a === b)!
        return state.sort === "az" ? A.title.localeCompare(B.title) : A.i - B.i
      })
      grid.append(...kids)
      grid.closest("section")?.classList.toggle("px-hidden", !kids.some((k) => !k.classList.contains("px-hidden")))
    }
    listing.classList.toggle("px-compact", state.compact)
    count.textContent = `${shown} of ${info.length}`
    nomatch.classList.toggle("px-hidden", shown > 0)
    nomatch.innerHTML = `Nothing in this list matches “${esc(state.q)}”. <a href="#" class="px-try-search">Search every section for it →</a>`
    nomatch.querySelector(".px-try-search")?.addEventListener("click", (e) => {
      e.preventDefault()
      openPalette(state.q)
    })
    // Facet counts follow the text filter, so a reader sees where the matches sit.
    const live = new Map<string, number>()
    for (const x of info) if (terms.every((t) => x.hay.includes(t))) live.set(facetOf(x), (live.get(facetOf(x)) ?? 0) + 1)
    const all = [...live.values()].reduce((a, b) => a + b, 0)
    tools.querySelectorAll<HTMLButtonElement>(".facets .px-chip").forEach((b) => {
      const n = b.dataset.f ? live.get(b.dataset.f) ?? 0 : all
      b.setAttribute("aria-pressed", String(b.dataset.f === state.facet))
      b.querySelector(".n")!.textContent = String(n)
      b.classList.toggle("px-hidden", n === 0 && b.dataset.f !== state.facet)
    })
    tools.querySelectorAll<HTMLButtonElement>(".px-seg button").forEach((b) => b.setAttribute("aria-pressed", String((b.dataset.v === "list") === state.compact)))
    const u = new URL(location.href)
    for (const [k, v] of [["q", state.q], ["f", state.facet], ["sort", state.sort === "rank" ? "" : state.sort], ["view", state.compact ? "list" : ""]])
      v ? u.searchParams.set(k, v) : u.searchParams.delete(k)
    history.replaceState(null, "", u)
  }
  input.addEventListener("input", () => {
    state.q = input.value
    apply()
  })
  select.addEventListener("change", () => {
    state.sort = select.value
    apply()
  })
  tools.querySelectorAll<HTMLButtonElement>(".facets .px-chip").forEach((b) =>
    b.addEventListener("click", () => {
      state.facet = state.facet === b.dataset.f ? "" : b.dataset.f!
      apply()
    }),
  )
  tools.querySelectorAll<HTMLButtonElement>(".px-seg button").forEach((b) =>
    b.addEventListener("click", () => {
      state.compact = b.dataset.v === "list"
      apply()
    }),
  )
  apply()
}

// ---------------------------------------------------------------- chat engine

interface Turn {
  q: string
  a: string
  hits: Hit[]
  el: HTMLElement
}

// Author pages describe people; answers drawn from them could turn into claims about a
// person, so Ask leaves them out (search still finds them).
const askable = (p: Page) => !p.slug.startsWith("authors/")

async function retrieve(
  question: string,
  prev: string,
  filter?: (p: Page) => boolean,
  n = 8,
  perPage = 3,
): Promise<{ hits: Hit[]; meaning: boolean }> {
  const ix = await loadIndex()
  const keep = (p: Page) => askable(p) && (!filter || filter(p))
  // Ask always ranks by meaning too: it already has the reader's key. A follow-up such
  // as "What are the limitations?" matches everything on its own, so rank with the
  // previous question's words first and fill with the question alone.
  const first = prev ? await hybridSearch(ix, `${prev} ${question}`, keep, SEARCH_DEPTH, true) : { hits: [], meaning: true }
  const second = await hybridSearch(ix, question, keep, SEARCH_DEPTH, true)
  const hits = first.hits.concat(second.hits)
  // At most three sections from one page, so an answer can draw on several projects.
  const out: Hit[] = []
  const per = new Map<string, number>()
  const seen = new Set<number>()
  for (const h of hits) {
    if (seen.has(h.sec.i)) continue
    const k = per.get(h.page.slug) ?? 0
    if (k >= perPage) continue
    per.set(h.page.slug, k + 1)
    seen.add(h.sec.i)
    out.push(h)
    if (out.length === n) break
  }
  return { hits: out, meaning: first.meaning && second.meaning }
}

// Renders an answer with [n] markers as buttons; markers outside the retrieved set are dropped.
const NEED_KEY = "Answers need your CBORG key. Add it once and both Ask the wiki and Ask about this page will use it."

const CITE = /\[(\d+(?:\s*[,–-]\s*\d+)*)\](?:\s*\[(\d+)\])*/g

// The source numbers a citation marker names, ranges expanded, limited to the retrieved set.
function citeNums(marker: string, nSources: number): number[] {
  return [...marker.matchAll(/(\d+)(?:\s*[–-]\s*(\d+))?/g)]
    .flatMap((d) => {
      const a = Number(d[1])
      const b = d[2] ? Number(d[2]) : a
      return b >= a && b - a < 20 ? Array.from({ length: b - a + 1 }, (_, k) => a + k) : [a]
    })
    .filter((n) => n >= 1 && n <= nSources)
}

function renderAnswer(text: string, nSources: number): { html: string; cited: Set<number> } {
  const cited = new Set<number>()
  const html = esc(text.trim())
    .replace(CITE, (m) =>
      citeNums(m, nSources)
        .map((n) => {
          cited.add(n)
          return `<button class="px-cite" data-n="${n}" type="button">${n}</button>`
        })
        .join(""),
    )
    .replace(/\*\*([^*\n]+)\*\*/g, "<b>$1</b>")
    .split(/\n{2,}/)
    .map((p) => {
      // A paragraph may open with a lead-in line and continue as "- " items.
      let html = ""
      let items: string[] = []
      const text: string[] = []
      const flushText = () => text.length && (html += `<p>${text.splice(0).join("<br>")}</p>`)
      const flushList = () => items.length && (html += `<ul>${items.splice(0).map((l) => `<li>${l}</li>`).join("")}</ul>`)
      for (const line of p.split(/\n/)) {
        if (/^\s*[-•] /.test(line)) {
          flushText()
          items.push(line.replace(/^\s*[-•] /, ""))
        } else {
          flushList()
          text.push(line)
        }
      }
      flushText()
      flushList()
      return html
    })
    .join("")
  return { html, cited }
}

const SYSTEM = (words: number, pageTitle?: string) => `You answer questions about the BERIL Knowledge Wiki, an AI-generated wiki compiled from AI-conducted microbial-biology research reports.

Rules:
- Use only the numbered sources in the user's latest message. Do not use outside knowledge.
- Cite every sentence that states a finding with its source numbers in square brackets, like [2] or [1][4].
- Give numbers exactly as the sources state them, with their conditions (organism, threshold, dataset).
- When sources disagree, say so and cite both sides.
- If the sources do not answer the question, reply with NO_ANSWER on the first line, then one sentence on what the sources do cover, and stop.
- Earlier answers in this conversation used different source numbers. Do not comment on earlier citations.
- Do not add confidence labels, and make no claims about what named people work on or care about.
- Write at most ${words} words of plain prose. No headings. You may bold a short lead-in phrase. Use a short "- " list only when comparing more than three items.${
  pageTitle ? `\n- The reader is on the page "${pageTitle}". Every source is a section of that page.` : ""
}`

function messagesFor(question: string, hits: Hit[], history: Turn[], page?: Page): ChatMessage[] {
  const sources = hits
    .map((h, n) => `[${n + 1}] ${h.page.title}${h.sec.p ? ` › ${h.sec.p}` : ""} (${h.page.label || TAG[h.page.group]})\n${h.sec.t}`)
    .join("\n\n")
  return [
    { role: "system", content: SYSTEM(page ? 150 : 220, page?.title) },
    // Each turn numbers its own sources, so old markers would point at the wrong ones.
    ...history.slice(-3).flatMap((t): ChatMessage[] => [
      { role: "user", content: t.q },
      { role: "assistant", content: t.a.replace(/\s*\[\d+(?:\s*[,–-]\s*\d+)*\]/g, "") },
    ]),
    { role: "user", content: `Sources:\n\n${sources}\n\nQuestion: ${question}` },
  ]
}

async function askInto(
  turns: Turn[],
  host: HTMLElement,
  question: string,
  opts: {
    filter?: (p: Page) => boolean
    page?: Page
    perPage?: number
    onCite: (t: Turn, n: number) => void
    onDone?: (t: Turn) => void
    searchLink: boolean
    stream?: AbortController
  },
) {
  if (!(await ensureKey(NEED_KEY))) return
  const q = document.createElement("div")
  q.className = "px-q"
  q.textContent = question
  const a = document.createElement("div")
  a.className = "px-a"
  a.innerHTML = `<div class="px-ans px-typing">Finding sections…</div>`
  host.append(q, a)
  a.scrollIntoView({ block: "nearest", behavior: "smooth" })
  const prev = turns.at(-1)?.q ?? ""
  // Captured now: later questions push onto the same array while this one awaits.
  const history = turns.filter((t) => t.a)
  const turn: Turn = { q: question, a: "", hits: [], el: a }
  turns.push(turn)
  const ans = a.querySelector<HTMLElement>(".px-ans")!
  const stream = opts.stream ?? new AbortController()
  streams.add(stream)
  try {
    const found = await retrieve(question, prev, opts.filter, 8, opts.perPage)
    turn.hits = found.hits
    ans.textContent = turn.hits.length ? `Reading ${turn.hits.length} sections…` : ""
    const result = turn.hits.length
      ? await streamChat(
          messagesFor(question, turn.hits, history, opts.page),
          (t) => {
            ans.innerHTML = renderAnswer(t, turn.hits.length).html
            ans.classList.add("px-typing")
          },
          stream.signal,
        )
      : { text: "NO_ANSWER\nNo wiki section matched the question's terms.", inTokens: 0, outTokens: 0, cut: false, reason: "stop" }
    const stopped = result.reason === "length" ? "cut off at the length limit" : `stopped early (${result.reason})`
    const text = result.text + (result.cut ? `\n\n(Answer ${stopped}.)` : "")
    turn.a = text
    ans.classList.remove("px-typing")
    if (/^\s*NO_ANSWER/.test(text)) {
      const why = text.replace(/^\s*NO_ANSWER\s*/, "").trim()
      ans.innerHTML = `<div class="px-noans">The wiki does not answer this${opts.page ? " on this page" : ""}. ${renderAnswer(why, turn.hits.length).html.replace(/^<p>|<\/p>$/g, "")}</div>`
    } else {
      const { html, cited } = renderAnswer(text, turn.hits.length)
      // The model was told to cite every finding; an answer that cites nothing is not backed by the wiki.
      ans.innerHTML =
        (cited.size ? "" : `<div class="px-err">This answer cites none of the sections it was given, so nothing here is backed by the wiki. Ask again or search instead.</div>`) + html
      const meta = document.createElement("div")
      meta.className = "px-ameta"
      meta.innerHTML = `<span>${cited.size} of ${turn.hits.length} sections cited${found.meaning ? "" : " · keyword ranking only"} · ${esc(modelLabel(loadSettings().model))} · ${result.inTokens.toLocaleString()} in, ${result.outTokens.toLocaleString()} out tokens</span><button type="button" data-act="copy">Copy with citations</button>${
        opts.searchLink ? `<button type="button" data-act="search">Search these terms</button>` : ""
      }`
      if (!found.meaning) meta.title = `Meaning ranking was unavailable for this answer: ${meaningError() || "CBORG did not embed the question"}.`
      a.append(meta)
      meta.querySelector('[data-act="copy"]')!.addEventListener("click", async (e) => {
        const btn = e.currentTarget as HTMLElement
        const refs = [...cited].sort((x, y) => x - y).map((n) => {
          const h = turn.hits[n - 1]
          return `[${n}] ${h.page.title}${h.sec.p ? ` › ${h.sec.p}` : ""}: ${location.origin}${href(h.page.slug, h.sec.a)}`
        })
        // Same citations as the display: drop markers outside the retrieved set.
        const clean = text.trim().replace(CITE, (m) => citeNums(m, turn.hits.length).map((n) => `[${n}]`).join(""))
        try {
          await navigator.clipboard.writeText(`${clean}\n\n${refs.join("\n")}`)
          btn.textContent = "Copied"
        } catch {
          btn.textContent = "Copy failed: your browser blocked the clipboard"
        }
      })
      meta.querySelector('[data-act="search"]')?.addEventListener("click", () => openPalette(question))
    }
    if (/^\s*NO_ANSWER/.test(text) && opts.searchLink) {
      const b = document.createElement("button")
      b.className = "px-chip"
      b.textContent = "Search sections instead"
      b.addEventListener("click", () => openPalette(question))
      a.append(b)
    }
    ans.querySelectorAll<HTMLButtonElement>(".px-cite").forEach((b) => {
      const h = turn.hits[Number(b.dataset.n) - 1]
      if (h) b.title = opts.page ? `Section: ${h.sec.p || "Opening"}` : `${h.page.title}${h.sec.p ? ` › ${h.sec.p}` : ""}`
      b.addEventListener("click", () => opts.onCite(turn, Number(b.dataset.n)))
    })
    opts.onDone?.(turn)
  } catch (err) {
    ans.classList.remove("px-typing")
    const stoppedHere = (err as Error).name === "AbortError"
    ans.innerHTML = `<div class="px-err">${stoppedHere ? "Stopped." : esc((err as Error).message)}</div>`
  } finally {
    streams.delete(stream)
  }
}

// ---------------------------------------------------------------- Ask page (C2)

function renderAskPage() {
  const main = document.querySelector("main")
  if (!main || main.classList.contains("px-askpage-main")) return
  document.title = "Ask the wiki"
  const params = new URLSearchParams(location.search)
  const scoped = bySlug.get(params.get("page") ?? "")
  const pageScope = scoped && askable(scoped) ? scoped.slug : ""
  const topics = pages.filter((p) => p.group === "topic")
  main.className = "px-askpage-main"
  main.innerHTML = `<div class="px-askhead">
      <div class="eyebrow">Ask the wiki</div>
      <h1>Ask the wiki</h1>
      <p>Answers come only from wiki sections, and every claim cites the section it came from. The wiki is AI-generated and partly reviewed by scientists, so check the cited sections before you rely on an answer.</p>
      <details class="px-how"><summary>How answers are made</summary><ol>
        <li>Your question is matched against all <span class="px-nsec">7,000</span> wiki sections by keyword search, in your browser. Words in a page title, a heading or an entity alias count extra, so <em>DvH</em> finds <em>Desulfovibrio vulgaris Hildenborough</em>. Sections are also ranked by meaning: CBORG embeds your question with your key, your browser compares it with the published section vectors, and the two rankings are merged.</li>
        <li>The 8 best sections, at most 3 from one page, go to the model with your question. A follow-up question is searched together with the question before it, so "What are the limitations?" stays on topic.</li>
        <li>The model must answer only from those 8 sections and cite each claim. Citation numbers outside the 8 are dropped. It does not browse or open other pages.</li>
        <li>If the 8 sections do not answer the question, it says so. The Evidence column shows all 8, cited or not, so you can see what it read.</li>
      </ol></details>
    </div>
    <div class="px-askgrid">
      <div>
        <div class="px-thread" aria-live="polite"></div>
        <form class="px-form">
          <div class="box"><textarea rows="2" placeholder="Ask a question about the BERIL corpus" aria-label="Your question"></textarea><button class="px-btn" type="submit">Ask</button></div>
          <div class="opts">
            <label>Scope <select aria-label="Scope"><option value="">All of the wiki</option>${
              pageScope && bySlug.get(pageScope) ? `<option value="page:${esc(pageScope)}" selected>This page: ${esc(bySlug.get(pageScope)!.title)}</option>` : ""
            }${topics.map((t) => `<option value="topic:${esc(t.slug)}">Topic: ${esc(t.title)}</option>`).join("")}</select></label>
            <span class="px-aistatus"></span>
            <span class="px-askrank px-meaning-status" aria-live="polite"></span>
            <button type="button" class="px-new">New conversation</button>
          </div>
        </form>
      </div>
      <aside class="px-evid" aria-label="Evidence"><h3>Evidence</h3><div class="px-evlist"><div class="px-ev">Sections behind the selected answer appear here, quoted from the wiki.</div></div></aside>
    </div>`
  const thread = main.querySelector<HTMLElement>(".px-thread")!
  const form = main.querySelector<HTMLFormElement>(".px-form")!
  const ta = form.querySelector("textarea")!
  const select = form.querySelector("select")!
  const evlist = main.querySelector<HTMLElement>(".px-evlist")!
  statusLine(form.querySelector<HTMLElement>(".px-aistatus")!)
  askRanking(form.querySelector<HTMLElement>(".px-askrank")!)
  loadIndex().then((ix) => (main.querySelector(".px-nsec")!.textContent = ix.sections.length.toLocaleString()))
  let turns: Turn[] = []
  let conversation = 0

  const examples = () => {
    thread.innerHTML = `<div class="px-examples">${[
      "Why do RB-TnSeq and knockout essentiality calls disagree in ADP1?",
      "Which metals share fitness signals with NaCl stress in DvH?",
      "Where do projects disagree about pangenome openness?",
      "What did the lanthanide-dependent methylotrophy work find?",
    ]
      .map((x) => `<button class="px-chip" type="button">${esc(x)}</button>`)
      .join("")}</div>`
    thread.querySelectorAll<HTMLButtonElement>(".px-chip").forEach((b) => b.addEventListener("click", () => submit(b.textContent!)))
  }

  const showEvidence = (turn: Turn, focus?: number) => {
    thread.querySelectorAll(".px-a").forEach((x) => x.classList.toggle("sel", x === turn.el))
    const cited = new Set([...turn.el.querySelectorAll<HTMLElement>(".px-cite")].map((b) => Number(b.dataset.n)))
    const card = (h: Hit, n: number) => `<div class="px-ev ${cited.has(n) ? "" : "uncited"} ${focus === n ? "on" : ""}" data-n="${n}">
          <div class="t"><span class="px-cite" style="cursor:default">${n}</span> <span class="px-tag ${h.page.group}">${esc(TAG[h.page.group])}</span>${title(h.page.title)}</div>
          ${h.sec.p ? `<div class="px-why">› ${esc(h.sec.p)}</div>` : ""}
          <div class="x">${esc(h.sec.t.slice(0, 700))}</div>
          <a href="${esc(href(h.page.slug, h.sec.a))}">Open section →</a>
        </div>`
    const all = turn.hits.map((h, i) => [h, i + 1] as const)
    const unc = all.filter(([, n]) => !cited.has(n))
    evlist.innerHTML =
      all.filter(([, n]) => cited.has(n)).map(([h, n]) => card(h, n)).join("") +
      (unc.length ? `<details class="px-ev"><summary>${unc.length} more retrieved, not cited</summary>${unc.map(([h, n]) => card(h, n)).join("")}</details>` : "")
    evlist.querySelectorAll<HTMLAnchorElement>("a").forEach((a) =>
      a.addEventListener("click", () => session.set("px-land", a.getAttribute("href")!.split("#")[1] ?? "")),
    )
    const on = evlist.querySelector<HTMLElement>(".px-ev.on")
    on?.scrollIntoView({ block: "nearest", behavior: "smooth" })
    thread.querySelectorAll(".px-cite").forEach((b) => b.classList.remove("on"))
    if (focus) turn.el.querySelectorAll(`.px-cite[data-n="${focus}"]`).forEach((b) => b.classList.add("on"))
  }

  const filterFor = (): { filter?: (p: Page) => boolean; page?: Page; perPage?: number } => {
    const v = select.value
    if (v.startsWith("page:")) {
      const slug = v.slice(5)
      return { filter: (p) => p.slug === slug, page: bySlug.get(slug), perPage: Infinity }
    }
    if (v.startsWith("topic:")) {
      const slug = v.slice(6)
      return { filter: (p) => p.slug === slug || p.topicSlugs.includes(slug) }
    }
    return {}
  }

  // One question at a time: an answer still streaming is the context for the next.
  let busy = false
  let stream: AbortController | null = null
  const askBtn = form.querySelector<HTMLButtonElement>('button[type="submit"]')!
  const submit = async (question: string) => {
    question = question.trim()
    if (!question || busy) return
    // Ask for the key before clearing the box, so cancelling keeps the question.
    if (!(await ensureKey(NEED_KEY))) return
    busy = askBtn.disabled = true
    if (!turns.length) thread.innerHTML = ""
    ta.value = ""
    const u = new URL(location.href)
    u.searchParams.set("q", turns.length ? u.searchParams.get("q") ?? question : question)
    history.replaceState(null, "", u)
    const { filter, page, perPage } = filterFor()
    const mine = conversation
    stream = new AbortController()
    await askInto(turns, thread, question, {
      filter,
      page,
      perPage,
      stream,
      searchLink: true,
      onCite: (t, n) => showEvidence(t, n),
      // An answer that finishes after "New conversation" must not repaint the evidence column.
      onDone: (t) => mine === conversation && showEvidence(t),
    }).finally(() => {
      if (mine === conversation) busy = askBtn.disabled = false
    })
    ta.focus()
  }

  form.addEventListener("submit", (e) => {
    e.preventDefault()
    submit(ta.value)
  })
  ta.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault()
      submit(ta.value)
    }
  })
  form.querySelector(".px-new")!.addEventListener("click", () => {
    conversation++
    stream?.abort()
    busy = askBtn.disabled = false
    turns = []
    evlist.innerHTML = `<div class="px-ev">Sections behind the selected answer appear here, quoted from the wiki.</div>`
    const u = new URL(location.href)
    u.searchParams.delete("q")
    history.replaceState(null, "", u)
    examples()
    ta.focus()
  })
  thread.addEventListener("click", (e) => {
    const a = (e.target as HTMLElement).closest(".px-a")
    const t = turns.find((x) => x.el === a)
    if (t && !(e.target as HTMLElement).closest("button")) showEvidence(t)
  })
  examples()
  // Only a question the reader typed elsewhere on the site is asked on arrival. A ?q= link
  // from anywhere else, or a reload, only fills the box: asking spends the reader's credit.
  const q = params.get("q")?.trim()
  const handed = session.get(ASK_HANDOFF)
  session.remove(ASK_HANDOFF)
  if (q && handed === q) submit(q)
  else {
    if (q) ta.value = q
    ta.focus()
  }
}

// ---------------------------------------------------------------- Ask about this page (C3)

let drawer: HTMLElement | null = null

function suggestions(page: Page): string[] {
  const skip = /^(sources?|related pages|references|see also|what this entity is)$/i
  return page.headings
    .filter((h) => !skip.test(h))
    .slice(0, 5)
    .map((h) => {
      if (/^(why|how|what|is|are|do|does|can|which|when|where)\b/i.test(h)) return h.endsWith("?") ? h : `${h}?`
      if (/^findings in /i.test(h)) return `What did ${h.replace(/^findings in /i, "")} find?`
      if (/^(tensions|limitations|caveats)/i.test(h)) return `What are the ${h.toLowerCase()} here?`
      if (/^open directions/i.test(h)) return "What would resolve the open questions?"
      return `What does this page say about ${h.charAt(0).toLowerCase()}${h.slice(1)}?`
    })
}

// A closed drawer only slides off-screen, so it is made inert: otherwise its textarea
// keeps focus, and Enter would send a question nobody can see.
function closeDrawer() {
  if (!drawer) return
  const hadFocus = drawer.contains(document.activeElement)
  drawer.classList.remove("open")
  drawer.inert = true
  if (hadFocus) document.querySelector<HTMLElement>(".record .px-askpage")?.focus()
}

function showDrawer() {
  if (!drawer) return
  drawer.inert = false
  drawer.classList.add("open")
  drawer.querySelector("textarea")?.focus()
}

function openDrawer(page: Page) {
  if (drawer && document.body.contains(drawer) && drawer.dataset.slug === page.slug) return showDrawer()
  drawer?.remove()
  drawer = document.createElement("aside")
  drawer.className = "px-drawer"
  drawer.dataset.slug = page.slug
  drawer.setAttribute("aria-label", "Ask about this page")
  drawer.innerHTML = `<header><span class="eyebrow">Ask about this page</span><span class="ttl">${title(page.title)}</span><button type="button" aria-label="Close">Close</button></header>
    <div class="px-dbody" aria-live="polite"><div class="px-sugg">${suggestions(page)
      .map((s) => `<button class="px-chip" type="button">${esc(s)}</button>`)
      .join("")}</div></div>
    <form class="px-dform"><div class="box"><textarea rows="2" placeholder="Ask about this page" aria-label="Question about this page"></textarea><button class="px-btn" type="submit">Ask</button></div>
    <div class="note">Answers use this page only, and the numbers jump to its sections. <a class="px-whole" href="${href("ask")}">Ask the whole wiki →</a></div>
    <div class="note px-aistatus"></div></form>`
  document.body.append(drawer)
  statusLine(drawer.querySelector<HTMLElement>(".px-aistatus")!)
  const body = drawer.querySelector<HTMLElement>(".px-dbody")!
  const ta = drawer.querySelector("textarea")!
  const whole = drawer.querySelector<HTMLAnchorElement>(".px-whole")!
  const turns: Turn[] = []
  let busy = false
  const askBtn = drawer.querySelector<HTMLButtonElement>('button[type="submit"]')!
  const submit = async (question: string) => {
    question = question.trim()
    if (!question || busy || !drawer!.classList.contains("open")) return
    if (!(await ensureKey(NEED_KEY))) return
    busy = askBtn.disabled = true
    drawer!.querySelector(".px-sugg")?.remove()
    ta.value = ""
    whole.href = `${href("ask")}?q=${encodeURIComponent(question)}`
    whole.dataset.q = question
    askInto(turns, body, question, {
      filter: (p) => p.slug === page.slug,
      page,
      perPage: Infinity,
      searchLink: false,
      onCite: (t, n) => {
        const h = t.hits[n - 1]
        if (!h) return
        if (window.innerWidth < 900) closeDrawer()
        if (h.sec.a) landOn(h.sec.a)
        else window.scrollTo({ top: 0, behavior: "smooth" })
      },
    }).finally(() => (busy = askBtn.disabled = false))
  }
  drawer.querySelector("header button")!.addEventListener("click", closeDrawer)
  whole.addEventListener("click", () => whole.dataset.q && session.set(ASK_HANDOFF, whole.dataset.q))
  drawer.querySelectorAll<HTMLButtonElement>(".px-sugg .px-chip").forEach((b) => b.addEventListener("click", () => submit(b.textContent!)))
  drawer.querySelector("form")!.addEventListener("submit", (e) => {
    e.preventDefault()
    submit(ta.value)
  })
  ta.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault()
      submit(ta.value)
    }
    if (e.key === "Escape") closeDrawer()
  })
  requestAnimationFrame(showDrawer)
}

// ---------------------------------------------------------------- wiring

async function enhance() {
  wireBar()
  if (!pal?.classList.contains("open")) document.documentElement.style.overflow = ""
  // The keyword index (about 6 MB gzipped) loads in the background once the page is idle,
  // so the first search is quick. Meaning vectors load only when meaning search or Ask needs them.
  const idle = (f: () => void) => ("requestIdleCallback" in window ? requestIdleCallback(f, { timeout: 5000 }) : setTimeout(f, 2000))
  idle(() => void loadIndex().catch((e) => console.warn("search index:", e)))
  try {
    await ensurePages()
  } catch (e) {
    // Search shows the error and retries when it is opened.
    console.warn("search index:", e)
    return
  }
  if (route() === "ask") return renderAskPage()
  const page = bySlug.get(here())
  if (document.querySelector(".listing")) enhanceCollection()
  if (page) wireRecord(page)
  const land = session.get("px-land")
  if (land) {
    session.remove("px-land")
    setTimeout(() => landOn(land), 60)
  }
}

window.addEventListener(
  "keydown",
  (e) => {
    const typing = (e.target as HTMLElement)?.closest?.("input, textarea, select, [contenteditable]")
    if ((e.key === "k" && (e.metaKey || e.ctrlKey)) || (e.key === "/" && !typing)) {
      e.preventDefault()
      e.stopImmediatePropagation()
      openPalette()
    }
  },
  true,
)
window.addEventListener(
  "click",
  (e) => {
    if ((e.target as HTMLElement)?.closest?.(".search-button, .px-bigsearch")) {
      e.preventDefault()
      e.stopImmediatePropagation()
      openPalette()
    }
  },
  true,
)
// Leaving a page closes search and the page drawer and stops any answer still streaming.
document.addEventListener("prenav", () => {
  closePalette()
  for (const s of streams) s.abort()
  // The drawer belongs to the page being left, and the SPA morph does not remove it.
  drawer?.remove()
  drawer = null
})
document.addEventListener("nav", () => void enhance())
if (document.readyState !== "loading") void enhance()
else document.addEventListener("DOMContentLoaded", () => void enhance())
