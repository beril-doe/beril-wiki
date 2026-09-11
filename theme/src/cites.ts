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
export function citeNote(cite: Cite, digest: boolean): string {
  const bits = [`cited ${cite.n}×`]
  if (digest) bits.push("cross-project digest")
  if (cite.primary) bits.push("primary source")
  for (const r of cite.rels) bits.push(r)
  return bits.join(" · ")
}

// A page cites a cross-project digest exactly as it cites a project report:
// both live in summaries/, and [src: discoveries] is as ordinary a tag as any
// project id. Counting them together made 61 pages state a false figure —
// concepts/adversarial-research-quality-assurance cites the Discoveries Log 38
// times and nothing else, and called that "1 project report".
export interface Cited {
  digests: number
  reports: number
  /** True where every citation really is a project report. */
  projectsOnly: boolean
  isDigest: (k: Cite) => boolean
  /** "3 project reports and 1 digest", for the byline. */
  summary: string
}

export function cited(cites: Cite[], c: Corpus): Cited {
  const isDigest = (k: Cite) => {
    const f = c.bySlug.get(k.slug)
    return !!f && !isReport(f)
  }
  const digests = cites.filter(isDigest).length
  const reports = cites.length - digests
  const plural = (n: number, one: string, many: string) => `${n} ${n === 1 ? one : many}`
  const parts = []
  if (reports > 0) parts.push(plural(reports, "project report", "project reports"))
  if (digests > 0) parts.push(plural(digests, "cross-project digest", "cross-project digests"))
  return { digests, reports, projectsOnly: digests === 0, isDigest, summary: parts.join(" and ") }
}
