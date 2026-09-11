// What else on the site a page is tied to. Computed once per render and
// shared: the header states the sizes, the rails list the members.
import { simplifySlug } from "@quartz-community/utils"
import {
  type Cite,
  type Corpus,
  type File,
  authorsOf,
  collectionOf,
  isIndex,
  kindOf,
  linksOf,
  slugOf,
  titleOf,
} from "./page"
import { rank } from "./svg"

// Pages outside the knowledge collections (about, authors, catalog) are
// linked from everywhere, so their neighbourhood says nothing.
export const isKnowledge = (file: File) => !["plain", "collection"].includes(kindOf(file).cls)

export interface Ties {
  conflicts: File[]
  /** Conflicts that name this page, rather than merely sharing its sources. */
  named: File[]
  citedBy: File[]
  /** Concepts this page links out to — what a topic gathers. */
  concepts: File[]
  entities: File[]
  /** Authors of the reports this page cites, and how many each wrote. */
  citedAuthors: [File, number][]
  /** Authors of this project report, when the page is one. */
  reportAuthors: File[]
}

export function ties(file: File, c: Corpus, cites: Cite[]): Ties {
  const slug = slugOf(file)
  const simple = simplifySlug(slug)
  const kind = kindOf(file)
  const knowledge = isKnowledge(file)
  const mine = new Set(cites.map((k) => k.slug))

  // Conflicts that name this page outrank ones that merely share its sources.
  const conflictScore = (k: File) => {
    if (linksOf(k).includes(simple)) return 2
    let shared = 0
    for (const l of new Set(linksOf(k))) if (mine.has(l) && ++shared >= 2) return 1
    return 0
  }
  // An author page cites its own reports, so shared sources would drag in
  // every conflict those reports touch; that belongs on the report pages.
  const conflicts =
    !knowledge || kind.cls === "conflict" || kind.cls === "author"
      ? []
      : c.conflicts
          .map((k) => [k, conflictScore(k)] as const)
          .filter(([, s]) => s > 0)
          .sort((a, b) => b[1] - a[1] || titleOf(a[0]).localeCompare(titleOf(b[0])))
          .map(([k]) => k)
  // Sharing two sources with a conflict is enough to be worth listing in the
  // rail, but not enough to count in the header: a well-cited concept shares
  // sources with dozens of them, and "26 open conflicts" over a page that is
  // named by two reads as a claim the corpus never made.
  const named = conflicts.filter((k) => linksOf(k).includes(simple))

  // Authorship attaches to project reports, never to the wiki page, which is
  // machine-written. A report page names its authors; every other page names
  // the authors of the reports it cites, with how many of those reports each
  // one wrote.
  const isReport = kind.cls === "report"
  const reportAuthors = isReport ? authorsOf(file, c) : []
  const tally = new Map<File, number>()
  if (!isReport && kind.cls !== "author") {
    for (const k of cites) {
      const report = c.bySlug.get(k.slug)
      if (!report) continue
      for (const a of authorsOf(report, c)) tally.set(a, (tally.get(a) ?? 0) + 1)
    }
  }
  const citedAuthors = [...tally].sort((x, y) => y[1] - x[1] || titleOf(x[0]).localeCompare(titleOf(y[0])))

  // Author pages link to every report they wrote; that is authorship, listed
  // above, not citation.
  const citedBy = !knowledge
    ? []
    : (c.inbound.get(simple) ?? [])
        .filter((f) => f !== file && !isIndex(slugOf(f)) && collectionOf(slugOf(f)) !== "authors")
        .sort((a, b) => rank(a) - rank(b) || titleOf(a).localeCompare(titleOf(b)))

  // Forward links, by collection. Reports have their own section, conflicts
  // and entities theirs, and a page's topics are in the header byline — which
  // left the concepts a page points at with nowhere to appear at all. On a
  // topic page those are the whole point of the page.
  const outTo = (collection: string) =>
    !knowledge
      ? []
      : [...new Set(linksOf(file))]
          .map((l) => c.bySlug.get(l))
          .filter(
            (f): f is File =>
              !!f && f !== file && collectionOf(slugOf(f)) === collection && !isIndex(slugOf(f)),
          )
          .sort((a, b) => titleOf(a).localeCompare(titleOf(b)))

  return { conflicts, named, citedBy, concepts: outTo("concepts"), entities: outTo("entities"), citedAuthors, reportAuthors }
}
