// Shared by the build-time index builder and the browser: MiniSearch.loadJS
// needs exactly the options the index was built with.

export const STOP = new Set(
  `a an and are as at be been but by can could did do does for from had has have how in into is it its
  of on or that the their there these they this those to was were what when where which while who why
  with would about across between than then not no so such via per may might also more most other`.split(/\s+/),
)

export const processTerm = (t: string): string | null => {
  const w = t.toLowerCase().replace(/^[^\p{L}\p{N}]+|[^\p{L}\p{N}]+$/gu, "")
  return w.length < 2 || STOP.has(w) ? null : w
}

// Keeps identifiers such as RB-TnSeq or DvH/206658 whole, and indexes their parts too.
export const tokenize = (s: string): string[] => {
  const out: string[] = []
  for (const raw of s.split(/[\s,;:!?()[\]{}"“”'’/]+/)) {
    if (!raw) continue
    out.push(raw)
    if (/[-_.]/.test(raw)) out.push(...raw.split(/[-_.]+/).filter(Boolean))
  }
  return out
}

export const SECTION_OPTIONS = {
  idField: "i",
  fields: ["title", "path", "aliases", "text"],
  storeFields: [] as string[],
  tokenize,
  processTerm,
}

export const PAGE_OPTIONS = {
  idField: "i",
  fields: ["title", "aliases"],
  storeFields: [] as string[],
  tokenize,
  processTerm,
}

/** Candidates per retriever before keyword and meaning ranks are fused. */
export const SEARCH_DEPTH = 60

/** CBORG embedding model for meaning search; documents and queries carry nomic's task prefixes. */
export const EMBED_MODEL = "lbl/nomic-embed-text"
export const DOC_PREFIX = "search_document: "
export const QUERY_PREFIX = "search_query: "

export interface Section {
  i: number
  /** page slug, e.g. concepts/gene-essentiality */
  s: string
  /** heading path shown as "Core evidence › Subsection"; "" for the opening */
  p: string
  /** element id to land on; "" for the page top */
  a: string
  t: string
}

export interface Page {
  i: number
  slug: string
  title: string
  /** record class without the kind- prefix: concept, topic, organism, report... */
  cls: string
  /** label shown in the record header: Concept, Organism, Project report... */
  label: string
  /** search group: topic | concept | conflict | entity | report | source | other */
  group: string
  desc: string
  /** the first topic the record header names, which sets the page's colour */
  topic: string
  topicSlug: string
  /** every topic the record header names */
  topicSlugs: string[]
  hue: string
  aliases: string[]
  headings: string[]
  out: string[]
  /** first sentence of the page's opening text */
  first: string
}

// Every search file carries the build it came from, so a browser holding files from
// two site updates (a tab left open across a deploy) never joins them by position.
export interface PagesFile {
  build: string
  pages: Page[]
}

export interface SectionFile {
  build: string
  sections: Section[]
}

/** section-index.json and page-index.json: a MiniSearch index in its envelope */
export interface IndexFile {
  build: string
  index: unknown
}

/** Vector file header: rows align with sections.json; a missing row is all zeros. */
export interface VectorMeta {
  model: string
  /** the build of the sections.json these rows align with */
  build: string
  dim: number
  /** per-row dequantisation scale: value = int8 * scale */
  scales: number[]
  missing: number
}
