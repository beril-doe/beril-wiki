// What the frame says about a citation, shared by the record header, the
// evidence rail and the sources list so the three never disagree.
import { type Cite, type Corpus, isReport } from "./page"

export function cell(cite: Cite): string {
  if (cite.primary) return "p"
  if (cite.rels.has("contradicts")) return "c"
  if (cite.rels.has("supports")) return "s"
  if (cite.rels.has("refines")) return "r"
  return ""
}

export function dotOf(cite: Cite): string | undefined {
  if (cite.primary) return "var(--ink)"
  for (const r of ["contradicts", "supports", "refines"] as const) if (cite.rels.has(r)) return `var(--${r})`
  return undefined
}

// What a citation row says about itself under the report's title: how often
// the page leans on it, and which of the three relation words the prose used.
export function citeNote(cite: Cite, archive: boolean): string {
  const bits = [`cited ${cite.n}×`]
  if (archive) bits.push("cross-project archive")
  if (cite.primary) bits.push("primary source")
  for (const r of cite.rels) bits.push(r)
  return bits.join(" · ")
}

// A page cites a cross-project archive exactly as it cites a project report:
// both live in summaries/, and [src: discoveries] is as ordinary a tag as any
// project id. Counting them together made 61 pages state a false figure —
// concepts/adversarial-research-quality-assurance cites the Discoveries Log 38
// times and nothing else, and called that "1 project report".
export interface Cited {
  archives: number
  reports: number
  /** True where every citation really is a project report. */
  projectsOnly: boolean
  isArchive: (k: Cite) => boolean
  /** "3 project reports and a cross-project archive", for the byline. */
  summary: string
}

export function cited(cites: Cite[], c: Corpus): Cited {
  const isArchive = (k: Cite) => {
    const f = c.bySlug.get(k.slug)
    return !!f && !isReport(f)
  }
  const archives = cites.filter(isArchive).length
  const reports = cites.length - archives
  const parts = []
  if (reports > 0) parts.push(`${reports} ${reports === 1 ? "project report" : "project reports"}`)
  if (archives > 0) parts.push(archives === 1 ? "a cross-project archive" : `${archives} cross-project archives`)
  return { archives, reports, projectsOnly: archives === 0, isArchive, summary: parts.join(" and ") }
}
