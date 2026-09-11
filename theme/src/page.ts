// Everything the frame knows about a page that Quartz does not hand it
// directly: what kind of record it is, which topics claim it, what it cites,
// and what cites it. All of it is read off data the pipeline already emits
// (slugs, frontmatter, crawl-links, the rendered HTML tree), so the theme
// never needs the ingest step to change shape.
import type { QuartzPluginData } from "@quartz-community/types"
import { simplifySlug } from "@quartz-community/utils"
import type { Element, ElementContent, Root, RootContent } from "hast"

export type File = QuartzPluginData & Record<string, unknown>
type Frontmatter = { title?: string; type?: string; description?: string } | undefined

export const RELS = ["supports", "refines", "contradicts"] as const
export type Rel = (typeof RELS)[number]
// The pipeline's vocabulary is exactly these three words, but the prose often
// compounds them: "supports and refines", "further supports". A negated word
// is not a relation stated, so "supports rather than contradicts" states one.
const REL_WORD = /\b(supports|refines|contradicts)\b/g
const REL_NEGATED = /\b(?:rather than|not|instead of)\s+(?:supports|refines|contradicts)\b/g

export interface Kind {
  label: string
  cls: string
}

const ENTITY_KINDS: Record<string, Kind> = {
  Organism: { label: "Organism", cls: "organism" },
  Compound: { label: "Compound", cls: "compound" },
  Method: { label: "Method", cls: "method" },
  Dataset: { label: "Dataset", cls: "dataset" },
  Gene_Or_Pathway: { label: "Gene or pathway", cls: "gene" },
}

export const slugOf = (f: File) => f.slug as string
export const fm = (f: File) => f.frontmatter as Frontmatter
export const titleOf = (f: File) => fm(f)?.title ?? slugOf(f)
export const linksOf = (f: File) => (f.links ?? []) as string[]
export const collectionOf = (slug: string) => slug.split("/")[0]
export const isIndex = (slug: string) => slug === "index" || slug.endsWith("/index")
/** A project report, as opposed to one of the cross-project digests. */
export const isReport = (slug: string) => /__report$/i.test(slug)

export function kindOf(f: File): Kind {
  const slug = slugOf(f)
  if (isIndex(slug)) return { label: "Collection", cls: "collection" }
  switch (collectionOf(slug)) {
    case "concepts":
      return { label: "Concept", cls: "concept" }
    case "topics":
      return { label: "Topic", cls: "topic" }
    case "conflicts":
      return { label: "Conflict", cls: "conflict" }
    case "summaries":
      // The pipeline stamps `type: "Summary"` on all 75 pages here, digests
      // included, so the frontmatter cannot tell them apart. The filename can:
      // a project report is <project_id>__REPORT, and the two cross-project
      // digests are discoveries and pitfalls.
      return isReport(slug)
        ? { label: "Project report", cls: "report" }
        : { label: "Digest", cls: "report" }
    case "sources":
      return { label: "Raw report", cls: "report" }
    case "entities":
      return ENTITY_KINDS[fm(f)?.type ?? ""] ?? { label: "Entity", cls: "entity" }
    case "authors":
      return { label: "Author", cls: "author" }
    case "data":
      return { label: "Data collection", cls: "plain" }
    default:
      return { label: "Page", cls: "plain" }
  }
}

// Corpus-wide lookups. Built once per allFiles array and cached, since the
// frame renders every page and each needs the same maps.
export interface Corpus {
  topics: File[]
  conflicts: File[]
  bySlug: Map<string, File>
  inbound: Map<string, File[]>
  hue: (topicSlug: string) => string
  topicsOf: (f: File) => File[]
  hueOf: (f: File) => string | undefined
}

const HUES = 9
const cache = new WeakMap<File[], Corpus>()

export function corpus(allFiles: File[]): Corpus {
  const hit = cache.get(allFiles)
  if (hit) return hit
  const pages = allFiles.filter((f) => !isIndex(slugOf(f)))
  const topics = pages
    .filter((f) => collectionOf(slugOf(f)) === "topics")
    .sort((a, b) => slugOf(a).localeCompare(slugOf(b)))
  const conflicts = pages.filter((f) => collectionOf(slugOf(f)) === "conflicts")
  const bySlug = new Map(allFiles.map((f) => [slugOf(f), f]))
  const inbound = new Map<string, File[]>()
  for (const f of allFiles) {
    for (const l of new Set(linksOf(f))) {
      const arr = inbound.get(l) ?? []
      arr.push(f)
      inbound.set(l, arr)
    }
  }
  const hueIndex = new Map(topics.map((t, i) => [slugOf(t), (i % HUES) + 1]))
  const hue = (s: string) => `var(--t${hueIndex.get(s) ?? 1})`
  const memo = new Map<string, File[]>()
  const topicsOf = (f: File) => {
    const s = slugOf(f)
    let r = memo.get(s)
    if (!r) {
      const simple = simplifySlug(s)
      r = topics.filter((t) => t !== f && linksOf(t).includes(simple))
      memo.set(s, r)
    }
    return r
  }
  const hueOf = (f: File) => {
    if (collectionOf(slugOf(f)) === "topics") return hue(slugOf(f))
    const t = topicsOf(f)[0]
    return t ? hue(slugOf(t)) : undefined
  }
  const c = { topics, conflicts, bySlug, inbound, hue, topicsOf, hueOf }
  cache.set(allFiles, c)
  return c
}

// One pass over the rendered tree. Lifts the provenance callout out of the
// body (the header renders it), tags citation chips and relation words with
// classes the stylesheet can colour, and tallies both.
export interface Cite {
  slug: string
  /** Where this citation points: the raw report when the prose links there. */
  target: string
  label: string
  n: number
  rels: Set<Rel>
  /** Citation number, assigned in order of first appearance in the prose. */
  num: number
}

export interface Walk {
  terms: string | null
  standing: ElementContent[] | null
  /** The ORCID link an author page opens with, lifted into the header. */
  orcid: ElementContent[] | null
  cites: Cite[]
  rels: Record<Rel, number>
}

const isEl = (n: unknown): n is Element => (n as Element)?.type === "element"
const classes = (el: Element): string[] => {
  const c = el.properties?.className as unknown
  return Array.isArray(c) ? c.map(String) : typeof c === "string" ? c.split(" ") : []
}
const addClass = (el: Element, ...cls: string[]) => {
  el.properties = { ...el.properties, className: [...classes(el), ...cls] }
}

export function text(n: Root | RootContent): string {
  if (n.type === "text") return n.value
  if ("children" in n) return (n.children as RootContent[]).map(text).join("")
  return ""
}

function find(n: Element | Root, pred: (e: Element) => boolean): Element | undefined {
  for (const c of n.children) {
    if (!isEl(c)) continue
    if (pred(c)) return c
    const hit = find(c, pred)
    if (hit) return hit
  }
  return undefined
}

export function walk(root: Root): Walk {
  const out: Walk = {
    terms: null,
    standing: null,
    orcid: null,
    cites: [],
    rels: { supports: 0, refines: 0, contradicts: 0 },
  }
  const cites = new Map<string, Cite>()

  // Provenance callout: the pipeline prepends one to every page it writes.
  const idx = root.children.findIndex(
    (c) =>
      isEl(c) &&
      c.tagName === "blockquote" &&
      classes(c).includes("callout") &&
      /^(Evidence|Provenance)\b/.test(
        text(find(c, (e) => classes(e).includes("callout-title-inner")) ?? c).trim(),
      ),
  )
  if (idx >= 0) {
    const callout = root.children[idx] as Element
    const title = text(find(callout, (e) => classes(e).includes("callout-title-inner"))!).trim()
    out.terms = title.replace(/^(Evidence|Provenance)\s*·?\s*/, "") || null
    const body = find(callout, (e) => classes(e).includes("callout-content"))
    const p = body && find(body, (e) => e.tagName === "p")
    out.standing = p ? p.children : (body?.children ?? null)
    root.children.splice(idx, 1)
  }

  // Author pages open with "ORCID: <link>", sometimes after a one-line note
  // about the account. The header renders the link; the body drops the line.
  const oi = root.children.findIndex(
    (c, i) => i < 4 && isEl(c) && c.tagName === "p" && /^ORCID:/.test(text(c).trim()),
  )
  if (oi >= 0) {
    const p = root.children[oi] as Element
    const link = p.children.filter((x) => isEl(x) && x.tagName === "a")
    if (link.length > 0) {
      out.orcid = link
      root.children.splice(oi, 1)
    }
  }

  // Paragraph-level attribution: a relation word applies to the reports cited
  // in the same paragraph or list item.
  const block = (el: Element) => {
    const rels: Rel[] = []
    const cited: Cite[] = []
    const inner = (n: Element) => {
      for (const c of n.children) {
        if (!isEl(c)) continue
        if (c.tagName === "strong") {
          // Every relation word in the phrase counts; the phrase takes the
          // colour of the first.
          const found = text(c).toLowerCase().replace(REL_NEGATED, "").match(REL_WORD) as Rel[] | null
          if (found && found.length > 0) {
            const words = [...new Set(found)]
            addClass(c, "rel", `rel-${words[0]}`)
            for (const w of words) {
              out.rels[w]++
              rels.push(w)
            }
            continue
          }
        }
        if (c.tagName === "sub" && /^src:/.test(text(c).trimStart())) {
          // A citation becomes a numbered mark rather than a row of report ids:
          // a paragraph resting on a dozen reports was rendering as a wall of
          // grey chips wider than the sentence it belonged to. The ids stay,
          // listed once under the prose and again in the evidence rail.
          addClass(c, "src")
          const marks: ElementContent[] = []
          for (const a of c.children) {
            if (!isEl(a) || a.tagName !== "a") continue
            // crawl-links writes the hyphenated key, not hast's camelCase.
            const raw = String(a.properties?.["data-slug"] ?? a.properties?.dataSlug ?? "")
            // A summary page cites itself, and the publish step rewrites that
            // self-citation to point at the raw report. Both forms name the
            // same report, so they count as one source; the link keeps
            // pointing where the page sent it.
            const slug = raw.startsWith("sources/") ? raw.replace(/^sources\//, "summaries/") : raw
            if (!slug.startsWith("summaries/")) continue
            let cite = cites.get(slug)
            if (!cite) {
              cite = { slug, target: raw, label: text(a).trim(), n: 0, rels: new Set(), num: cites.size + 1 }
              cites.set(slug, cite)
            }
            cite.n++
            cited.push(cite)
            a.properties = { ...a.properties, title: cite.label }
            a.children = [{ type: "text", value: String(cite.num) }]
            if (marks.length > 0) marks.push({ type: "text", value: "," })
            marks.push(a)
          }
          // Replacing the children with nothing would erase the citation
          // itself, which is the one thing every page here promises.
          if (marks.length > 0) c.children = marks
          continue
        }
        inner(c)
      }
    }
    inner(el)
    for (const c of cited) for (const r of rels) c.rels.add(r)
  }
  const visit = (n: Element | Root) => {
    for (const c of n.children) {
      if (!isEl(c)) continue
      if (c.tagName === "p" || (c.tagName === "li" && !c.children.some((x) => isEl(x) && x.tagName === "p"))) {
        block(c)
      } else {
        visit(c)
      }
    }
  }
  visit(root)
  out.cites = [...cites.values()].sort((a, b) => b.n - a.n || a.label.localeCompare(b.label))
  return out
}

// A collection index page whose body hand-lists the same pages the frame
// lists below it (authors/index and data/index both do) would otherwise show
// the collection twice. Drop a top-level list when every link in it points
// inside this page's own collection; keep the prose around it.
export function stripIndexLists(root: Root, slug: string) {
  if (!isIndex(slug)) return
  const here = collectionOf(slug)
  root.children = root.children.filter((c) => {
    if (!isEl(c) || (c.tagName !== "ul" && c.tagName !== "ol")) return true
    const links: string[] = []
    const scan = (n: Element) => {
      for (const k of n.children) {
        if (!isEl(k)) continue
        if (k.tagName === "a") {
          const s = String(k.properties?.["data-slug"] ?? k.properties?.dataSlug ?? "")
          if (s) links.push(s)
        }
        scan(k)
      }
    }
    scan(c)
    return links.length === 0 || !links.every((l) => collectionOf(l) === here)
  })
}

// The home page's topic list carries one blurb per topic, written as
// "[[topics/x|Title]] (12 concepts): what it covers". The frame lays those
// blurbs out beside the counts it computes, so pull each list item apart
// into the topic it names and the sentence describing it.
export function topicBlurbs(nodes: ElementContent[] | undefined): Map<string, ElementContent[]> {
  const out = new Map<string, ElementContent[]>()
  if (!nodes) return out
  for (const list of nodes) {
    if (!isEl(list) || (list.tagName !== "ul" && list.tagName !== "ol")) continue
    for (const li of list.children) {
      if (!isEl(li) || li.tagName !== "li") continue
      const kids = [...li.children]
      const first = kids.find((k) => isEl(k) && k.tagName === "a") as Element | undefined
      if (!first) continue
      const slug = String(first.properties?.["data-slug"] ?? first.properties?.dataSlug ?? "")
      if (!slug) continue
      const rest = kids.slice(kids.indexOf(first) + 1)
      // "(12 concepts): the disciplined combination…" — the count is rendered
      // as a figure beside the row, so only the sentence is wanted here.
      const head = rest[0]
      if (head?.type === "text") {
        // "(12 concepts): the disciplined combination…" reads as a sentence
        // once the count is gone, so it starts one.
        const value = head.value
          .replace(/^\s*\(\d+\s+concepts?\)\s*:?\s*/, "")
          .replace(/^\s*:\s*/, "")
        rest[0] = { type: "text", value: value.charAt(0).toUpperCase() + value.slice(1) }
      }
      out.set(simplifySlug(slug), rest)
    }
  }
  return out
}

// What the corpus holds, counted off the pages that actually rendered rather
// than read out of a sentence in the markdown.
export interface Counts {
  reports: number
  digests: number
  concepts: number
  entities: number
  conflicts: number
  topics: number
}

export function counts(c: Corpus): Counts {
  let reports = 0
  let digests = 0
  let concepts = 0
  let entities = 0
  for (const f of c.bySlug.values()) {
    const slug = slugOf(f)
    if (isIndex(slug)) continue
    // "Project reports" means the projects. The two cross-project digests sit
    // in the same collection and are counted apart from them.
    if (collectionOf(slug) === "summaries") isReport(slug) ? reports++ : digests++
    else if (collectionOf(slug) === "concepts") concepts++
    else if (collectionOf(slug) === "entities") entities++
  }
  return { reports, digests, concepts, entities, conflicts: c.conflicts.length, topics: c.topics.length }
}

// Home page body, split at its h2s so the frame can lay the pieces out.
export function sections(root: Root): { intro: ElementContent[]; byHeading: Map<string, ElementContent[]> } {
  const intro: ElementContent[] = []
  const byHeading = new Map<string, ElementContent[]>()
  let current: ElementContent[] = intro
  for (const c of root.children) {
    if (isEl(c) && c.tagName === "h2") {
      current = []
      byHeading.set(text(c).trim().toLowerCase(), current)
    } else if (c.type !== "doctype") {
      current.push(c)
    }
  }
  return { intro, byHeading }
}

export const truncate = (s: string, n: number) => (s.length > n ? s.slice(0, n - 1).trimEnd() + "…" : s)

// The people listed as authors of a project report: the author pages that
// link to it. Authorship is parsed from each project's README by the
// pipeline, so this is the one relation between people and pages the corpus
// actually records. A raw report shares the authors of its summary.
export function authorsOf(report: File, c: Corpus): File[] {
  let slug = slugOf(report)
  if (collectionOf(slug) === "sources") slug = slug.replace(/^sources\//, "summaries/")
  return (c.inbound.get(simplifySlug(slug)) ?? [])
    .filter((f) => collectionOf(slugOf(f)) === "authors" && !isIndex(slugOf(f)))
    .sort((a, b) => titleOf(a).localeCompare(titleOf(b)))
}
