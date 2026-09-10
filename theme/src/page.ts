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
      return fm(f)?.type === "Summary"
        ? { label: "Digest", cls: "report" }
        : { label: "Project report", cls: "report" }
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
  label: string
  n: number
  rels: Set<Rel>
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
        if (c.tagName === "strong" && c.children.length === 1) {
          const w = text(c).trim() as Rel
          if (RELS.includes(w)) {
            addClass(c, "rel", `rel-${w}`)
            out.rels[w]++
            rels.push(w)
            continue
          }
        }
        if (c.tagName === "sub" && /^src:/.test(text(c).trimStart())) {
          addClass(c, "src")
          const first = c.children[0]
          if (first?.type === "text") {
            first.value = first.value.replace(/^\s*src:\s*/, "")
            if (!first.value) c.children.shift()
          }
          for (const a of c.children) {
            if (!isEl(a) || a.tagName !== "a") continue
            // crawl-links writes the hyphenated key, not hast's camelCase.
            const slug = String(a.properties?.["data-slug"] ?? a.properties?.dataSlug ?? "")
            if (!slug.startsWith("summaries/")) continue
            let cite = cites.get(slug)
            if (!cite) {
              cite = { slug, label: text(a).trim(), n: 0, rels: new Set() }
              cites.set(slug, cite)
            }
            cite.n++
            cited.push(cite)
          }
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
