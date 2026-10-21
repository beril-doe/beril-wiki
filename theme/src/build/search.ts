/// <reference types="node" />
// Builds the site's search index from the rendered pages, after `quartz build`.
//
//   node theme/dist/build-search.js <repo>
//
// Reads quartz/public (so section anchors, titles and kinds match what readers
// see) and quartz/content (descriptions, which the site hides). Writes into
// quartz/public/static/search/: sections.json, section-index.json and
// page-index.json for keyword search, pages.json for page metadata, and
// vectors.i8 + vectors.json for meaning search. Vectors come from the committed
// store search/section-vectors.jsonl, keyed by a hash of the exact text embedded;
// the search_vectors pipeline stage fills that store from
// quartz/search-embed-input.json, which this script also writes. CI has no
// CBORG key, so it only ever reads the store.
import { createHash } from "node:crypto"
import { existsSync, mkdirSync, readFileSync, readdirSync, writeFileSync } from "node:fs"
import { join } from "node:path"
import MiniSearch from "minisearch"
import { type HTMLElement, parse } from "node-html-parser"
import { DOC_PREFIX, EMBED_MODEL, PAGE_OPTIONS, type Page, SECTION_OPTIONS, type Section, type IndexFile, type PagesFile, type SectionFile, type VectorMeta } from "../search/config"

const REPO = process.argv[2] ?? process.cwd()
const PUB = join(REPO, "quartz/public")
const CONTENT = join(REPO, "quartz/content")
const OUT = join(PUB, "static/search")
const STORE = join(REPO, "search/section-vectors.jsonl")
const EMBED_INPUT = join(REPO, "quartz/search-embed-input.json")
const DIM = 768

const DIRS = ["topics", "concepts", "conflicts", "entities", "summaries", "sources", "authors", "data"]
const ROOT_PAGES = ["about", "negative-results", "opportunities"]
const ENTITY = new Set(["organism", "gene", "compound", "method", "dataset", "entity"])
// Sections longer than this are cut into chunks small enough to cite.
const MAX_WORDS = 420
// What an embedding sees: title, heading path, then the section capped here.
const EMBED_WORDS = 400

const groupOf = (dir: string, cls: string) =>
  cls === "topic" ? "topic"
  : cls === "concept" ? "concept"
  : cls === "conflict" ? "conflict"
  : ENTITY.has(cls) ? "entity"
  : dir === "summaries" ? "report"
  : dir === "sources" ? "source"
  : "other"

// Removing citation markers leaves "claim ." behind; close those gaps.
const clean = (s: string) =>
  s.replace(/\u00a0/g, " ").replace(/[ \t]+/g, " ").replace(/ +([.,;:)])/g, "$1").replace(/\s*\n\s*/g, "\n").trim()

const wordsOf = (s: string) => (s.match(/\S+/g) ?? []).length

// textContent keeps the spaces around inline links; lists and tables keep one
// line per item or row so a snippet never runs two cells together.
function textOf(el: HTMLElement): string {
  const tag = el.tagName?.toLowerCase()
  if (tag === "ul" || tag === "ol") return el.querySelectorAll(":scope > li").map((li) => textOf(li)).join("\n")
  // Quartz wraps tables in a div.table-container; read the table, not the div's run-together text.
  const kids = (el.childNodes ?? []).filter((c) => (c as HTMLElement).tagName) as HTMLElement[]
  const table = tag === "table" ? el : kids.length === 1 && kids[0].tagName?.toLowerCase() === "table" ? kids[0] : null
  if (table)
    return table.querySelectorAll("tr").map((tr) => tr.querySelectorAll("th, td").map((c) => c.text.trim()).join(" | ")).join("\n")
  return (el.text ?? "").replace(/\s+/g, " ").trim()
}

// Blocks too long to cite as one section split into their items or rows.
function blocksOf(el: HTMLElement): HTMLElement[] {
  const tag = el.tagName?.toLowerCase()
  if (wordsOf(el.text ?? "") <= MAX_WORDS) return [el]
  if (tag === "ul" || tag === "ol") return el.querySelectorAll(":scope > li")
  if (tag === "table") return el.querySelectorAll("tr")
  if (tag === "div" || tag === "blockquote" || tag === "figure") return el.childNodes.filter((c) => (c as HTMLElement).tagName) as HTMLElement[]
  return [el]
}

const NOT_ALIAS = /^(none|no|not|n\/a|species|unknown)\b/i

function frontmatter(slug: string): Record<string, string> {
  const path = join(CONTENT, `${slug}.md`)
  if (!existsSync(path)) return {}
  const m = readFileSync(path, "utf8").match(/^---\n([\s\S]*?)\n---/)
  const out: Record<string, string> = {}
  for (const line of m?.[1].split("\n") ?? []) {
    const kv = line.match(/^(\w+):\s*(.*)$/)
    if (!kv) continue
    try {
      out[kv[1]] = JSON.parse(kv[2])
    } catch {
      out[kv[1]] = kv[2]
    }
  }
  return out
}

const files: [string, string][] = []
for (const dir of DIRS)
  if (existsSync(join(PUB, dir)))
    for (const f of readdirSync(join(PUB, dir)))
      if (f.endsWith(".html") && f !== "index.html") files.push([dir, `${dir}/${f.slice(0, -5)}`])
for (const p of ROOT_PAGES) if (existsSync(join(PUB, `${p}.html`))) files.push(["", p])
files.sort((a, b) => a[1].localeCompare(b[1]))

const pages: Page[] = []
const sections: Section[] = []

for (const [dir, slug] of files) {
  const root = parse(readFileSync(join(PUB, `${slug}.html`), "utf8"))
  const record = root.querySelector(".record")
  const cls = record?.classList.value.find((c) => c.startsWith("kind-"))?.slice(5) ?? "plain"
  const body = root.querySelector("article .markdown-preview-view") ?? root.querySelector("article")
  if (!body) continue
  // Citation markers and footnote references are not prose; a plain <sup> (m², 10⁻³) is.
  body.querySelectorAll("sub.src, a[data-footnote-ref], script, style, .katex-mathml").forEach((n) => n.remove())
  const topicLinks = record?.querySelectorAll("a.topic") ?? []
  const topicA = topicLinks[0]
  const fm = frontmatter(slug)
  const blocks = (body.childNodes as HTMLElement[]).filter((c) => c.tagName)
  const allText = blocks.map(textOf).join("\n")
  const aliasLine = allText.match(/Known alias(?:es)?:\s*([^\n]+?)\.?(?:\n|$)/i)?.[1] ?? ""
  const page: Page = {
    i: pages.length,
    slug,
    title: clean(record?.querySelector("h1")?.text ?? root.querySelector("title")?.text ?? slug),
    cls,
    label: record?.querySelector(".kind b")?.text.trim() ?? "",
    group: groupOf(dir, cls),
    desc: fm.description ?? "",
    topic: clean(topicA?.text ?? ""),
    topicSlug: (topicA?.getAttribute("href") ?? "").replace(/^(\.\.\/|\.\/)+/, ""),
    topicSlugs: topicLinks.map((a) => (a.getAttribute("href") ?? "").replace(/^(\.\.\/|\.\/)+/, "")),
    hue: record?.querySelector(".kind i.dot")?.getAttribute("style")?.match(/--c:\s*([^;]+)/)?.[1] ?? "",
    aliases: aliasLine
      ? aliasLine.split(/,|;|\band\b/).map((s) => s.replace(/\(.*?\)/g, "").trim()).filter((s) => s && s.length < 40 && !NOT_ALIAS.test(s))
      : [],
    headings: [],
    out: [...new Set(body.querySelectorAll("a.internal").map((a) => a.getAttribute("data-slug") ?? "").filter(Boolean))],
    first: "",
  }
  pages.push(page)

  // Cut at h2/h3, and again whenever a section passes MAX_WORDS.
  let h2 = ""
  let path = ""
  let anchor = ""
  let buf: string[] = []
  let n = 0
  const flush = () => {
    const t = clean(buf.join("\n"))
    if (wordsOf(t) >= 8) sections.push({ i: sections.length, s: slug, p: path, a: anchor, t })
    buf = []
    n = 0
  }
  for (const el of blocks) {
    const tag = el.tagName.toLowerCase()
    if (tag === "h1") continue
    if (tag === "h2" || tag === "h3") {
      flush()
      const text = clean(el.text)
      if (tag === "h2") {
        h2 = text
        path = text
        page.headings.push(text)
      } else path = h2 ? `${h2} › ${text}` : text
      anchor = el.id ?? ""
      continue
    }
    for (const b of blocksOf(el)) {
      const t = clean(textOf(b))
      if (!t) continue
      const w = wordsOf(t)
      if (n > 0 && n + w > MAX_WORDS) flush()
      buf.push(t)
      n += w
    }
  }
  flush()
  const opening = sections.find((x) => x.s === slug)?.t ?? ""
  page.first = opening.split("\n")[0].match(/^.+?[.!?](?=\s+[A-Z]|$)/)?.[0] ?? ""
}

const bySlug = new Map(pages.map((p) => [p.slug, p]))
const sectionIndex = new MiniSearch(SECTION_OPTIONS)
sectionIndex.addAll(
  sections.map((s) => {
    const p = bySlug.get(s.s)!
    return { i: s.i, title: p.title, path: s.p, aliases: p.aliases.join(" "), text: s.t }
  }),
)
const pageIndex = new MiniSearch(PAGE_OPTIONS)
pageIndex.addAll(pages.map((p) => ({ i: p.i, title: p.title, aliases: p.aliases.join(" ") })))

// The exact text each section is embedded with, and the key its vector is stored under.
const embedText = (s: Section) => {
  const p = bySlug.get(s.s)
  return `${DOC_PREFIX}${p?.title ?? s.s}${s.p ? ` › ${s.p}` : ""}\n${s.t.split(/\s+/).slice(0, EMBED_WORDS).join(" ")}`
}
const keyOf = (text: string) => createHash("sha256").update(text).digest("hex").slice(0, 24)
const inputs = sections.map((s) => {
  const text = embedText(s)
  return { h: keyOf(text), text }
})

const store = new Map<string, { v: string; s: number }>()
if (existsSync(STORE))
  for (const line of readFileSync(STORE, "utf8").split("\n")) {
    if (!line.trim()) continue
    const r = JSON.parse(line)
    store.set(r.h, { v: r.v, s: r.s })
  }
// The keyword indexes and vector rows are built from pages and sections, so their hash names the build.
const build = createHash("sha256").update(JSON.stringify(pages)).update(JSON.stringify(sections)).digest("hex").slice(0, 16)
const pagesFile: PagesFile = { build, pages }
const sectionFile: SectionFile = { build, sections }
const envelope = (index: MiniSearch): IndexFile => ({ build, index: index.toJSON() })
const vectors = new Int8Array(sections.length * DIM)
const meta: VectorMeta = { model: EMBED_MODEL, build, dim: DIM, scales: [], missing: 0 }
inputs.forEach(({ h }, i) => {
  const hit = store.get(h)
  if (!hit) {
    meta.scales.push(0)
    meta.missing++
    return
  }
  vectors.set(new Int8Array(Buffer.from(hit.v, "base64")), i * DIM)
  meta.scales.push(hit.s)
})

mkdirSync(OUT, { recursive: true })
writeFileSync(join(OUT, "pages.json"), JSON.stringify(pagesFile))
writeFileSync(join(OUT, "sections.json"), JSON.stringify(sectionFile))
writeFileSync(join(OUT, "section-index.json"), JSON.stringify(envelope(sectionIndex)))
writeFileSync(join(OUT, "page-index.json"), JSON.stringify(envelope(pageIndex)))
writeFileSync(join(OUT, "vectors.i8"), vectors)
writeFileSync(join(OUT, "vectors.json"), JSON.stringify(meta))
writeFileSync(EMBED_INPUT, JSON.stringify(inputs))
console.log(
  `search index: ${pages.length} pages, ${sections.length} sections; ` +
    `${sections.length - meta.missing} with vectors, ${meta.missing} without` +
    (meta.missing ? " (run the search_vectors stage to embed them)" : ""),
)
