// A collection index lists what the collection holds. Quartz's folder listing
// prints bare titles down the middle of an otherwise empty page; every one of
// these pages already carries a description and a type, so use them.
import type { FullSlug } from "@quartz-community/types"
import { resolveRelative, simplifySlug } from "@quartz-community/utils"
import { type Corpus, type File, collectionOf, fm, isIndex, isReport, kindOf, linksOf, slugOf, titleOf } from "../page"

// What a collection index can say about itself, in countable terms. Quartz
// gives an index page no citations, so without this its byline is empty and
// the page opens on a bare title.
export function indexFigures(file: File, c: Corpus): [string, string][] {
  const here = collectionOf(slugOf(file))
  const members = [...c.bySlug.values()].filter(
    (f) => collectionOf(slugOf(f)) === here && !isIndex(slugOf(f)),
  )
  const n = members.length
  if (n === 0) return []
  const plural = (k: number, unit: string) => `${k} ${unit}${k === 1 ? "" : "s"}`
  const out: [string, string][] = []
  switch (here) {
    case "entities": {
      out.push(["Entities", String(n)])
      out.push(["Kinds", plural(new Set(members.map((f) => kindOf(f).label)).size, "kind")])
      break
    }
    case "topics": {
      out.push(["Topics", String(n)])
      const gathered = new Set(
        members.flatMap((f) => linksOf(f).filter((l) => collectionOf(l) === "concepts")),
      )
      out.push(["Concepts", `${gathered.size} gathered`])
      break
    }
    case "authors": {
      out.push(["People", String(n)])
      const reports = new Set(
        members.flatMap((f) => linksOf(f).filter((l) => collectionOf(l) === "summaries")),
      )
      out.push(["Credited on", plural(reports.size, "project report")])
      break
    }
    case "summaries": {
      const reports = members.filter(isReport).length
      out.push(["Project reports", String(reports)])
      out.push(["Cross-project digests", String(n - reports)])
      break
    }
    case "conflicts":
      out.push(["Conflicts", plural(n, "recorded conflict")])
      break
    case "concepts":
      out.push(["Concepts", String(n)])
      break
    default:
      out.push(["Pages", String(n)])
  }
  return out
}

const PLURAL: Record<string, string> = {
  organism: "Organisms",
  method: "Methods",
  dataset: "Datasets",
  gene: "Genes and pathways",
  compound: "Compounds",
  entity: "Other entities",
}

// An entity is coloured by what kind of thing it is; everything else by the
// topic that claims it. A wall of identical cards was the complaint.
const ENTITY_HUE: Record<string, string> = {
  organism: "var(--organism)",
  method: "var(--method)",
  dataset: "var(--dataset)",
  gene: "var(--gene)",
  compound: "var(--compound)",
}

export function Listing({ file, c }: { file: File; c: Corpus }) {
  const slug = slugOf(file) as FullSlug
  const here = collectionOf(slug)
  const members = [...c.bySlug.values()].filter((f) => collectionOf(slugOf(f)) === here && !isIndex(slugOf(f)))
  if (members.length === 0) return null
  const inbound = (f: File) =>
    (c.inbound.get(simplifySlug(slugOf(f))) ?? []).filter((k) => !isIndex(slugOf(k))).length
  const byRank = (a: File, b: File) => inbound(b) - inbound(a) || titleOf(a).localeCompare(titleOf(b))
  const byName = (a: File, b: File) => titleOf(a).localeCompare(titleOf(b))
  // Topics keep the order the home page lists them in; nothing links to a
  // topic often enough for a ranking to mean anything.
  const alphabetical = here === "authors" || here === "data" || here === "topics"

  // What to count differs by collection: nothing links to an author page, so
  // "linked from" would read zero on every one of them, and a topic page is
  // measured by what it gathers rather than by what points at it.
  const out = (f: File, collection: string) =>
    new Set(linksOf(f).filter((l) => collectionOf(l) === collection)).size
  const plural = (n: number, unit: string) => `${n} ${unit}${n === 1 ? "" : "s"}`

  const meta = (f: File): string | null => {
    if (here === "authors") {
      const n = out(f, "summaries")
      return n > 0 ? `credited on ${plural(n, "project report")}` : null
    }
    if (here === "topics") {
      const c = out(f, "concepts")
      const r = out(f, "summaries")
      return c > 0 || r > 0 ? `${plural(c, "concept")} · ${plural(r, "report")}` : null
    }
    // A conflict page carries no description, and how many pages link to it
    // says nothing about it; the projects that disagree do.
    if (here === "conflicts") {
      const n = out(f, "summaries")
      return n > 0 ? `${plural(n, "source project")} disagree` : null
    }
    const n = inbound(f)
    return n > 0 ? `linked from ${plural(n, "page")}` : null
  }

  const accent = (f: File) =>
    here === "entities" ? ENTITY_HUE[kindOf(f).cls] : (c.hueOf(f) ?? undefined)

  const Card = ({ f }: { f: File }) => {
    const k = kindOf(f)
    const line = meta(f)
    const desc = fm(f)?.description
    const hue = accent(f)
    return (
      <a
        class="card"
        href={resolveRelative(slug, slugOf(f) as FullSlug)}
        style={hue ? `--d:${hue}` : undefined}
      >
        <b>{titleOf(f)}</b>
        {desc && <span class="desc">{desc}</span>}
        {(line || here === "entities") && (
          <span class="meta">
            {here === "entities" && <span class={`tag k-${k.cls}`}>{k.label}</span>}
            {line && <span class="n">{line}</span>}
          </span>
        )}
      </a>
    )
  }

  // Entities are the one collection with a type on every page; grouping by it
  // beats one 139-item list, and it needs no script to work.
  if (here === "entities") {
    const groups = new Map<string, File[]>()
    for (const f of members.sort(byRank)) {
      const cls = kindOf(f).cls
      groups.set(cls, [...(groups.get(cls) ?? []), f])
    }
    const order = ["organism", "method", "dataset", "gene", "compound", "entity"]
    return (
      <div class="listing">
        {order
          .filter((cls) => groups.has(cls))
          .map((cls) => (
            <section>
              <div class="sechead">
                <h2>{PLURAL[cls] ?? cls}</h2>
                <p>{groups.get(cls)!.length} pages, most linked first</p>
              </div>
              <div class="cards">
                {groups.get(cls)!.map((f) => (
                  <Card f={f} />
                ))}
              </div>
            </section>
          ))}
      </div>
    )
  }

  return (
    <div class="listing">
      <div class="cards">
        {members.sort(alphabetical ? byName : byRank).map((f) => (
          <Card f={f} />
        ))}
      </div>
    </div>
  )
}
