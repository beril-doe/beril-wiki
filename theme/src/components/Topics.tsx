// The nine topics, with what each covers and how much evidence stands behind
// it. This replaces two separate renderings of the same nine rows: a heat
// table above the map and a blurb list below it.
import type { FullSlug } from "@quartz-community/types"
import { resolveRelative, simplifySlug } from "@quartz-community/utils"
import type { ElementContent } from "hast"
import { jsx } from "../jsx"
import { type Corpus, type File, collectionOf, linksOf, slugOf, titleOf } from "../page"

const COLUMNS: [string, (l: string, f: File | undefined) => boolean][] = [
  ["Concepts", (l) => collectionOf(l) === "concepts"],
  ["Reports", (l) => collectionOf(l) === "summaries"],
  ["Conflicts", (l) => collectionOf(l) === "conflicts"],
  ["Entities", (l) => collectionOf(l) === "entities"],
]

export function Topics({ c, from, blurbs }: {
  c: Corpus
  from: FullSlug
  blurbs: Map<string, ElementContent[]>
}) {
  const counts = c.topics.map((t) => {
    const links = [...new Set(linksOf(t))]
    return COLUMNS.map(([, test]) => links.filter((l) => test(l, c.bySlug.get(l))).length)
  })
  // Shade each column against its own largest value: reports outnumber
  // conflicts several times over, and one ramp across both would flatten the
  // column that varies least.
  const max = COLUMNS.map((_, j) => Math.max(1, ...counts.map((row) => row[j])))
  return (
    <div class="topictable">
      <div class="thead">
        <span>Topic</span>
        <span>What it covers</span>
        {COLUMNS.map(([name]) => (
          <span class="c">{name}</span>
        ))}
      </div>
      {c.topics.map((t, i) => {
        const blurb = blurbs.get(simplifySlug(slugOf(t)))
        return (
          <div class="trow">
            <span class="name">
              <i class="dot" style={`--c:${c.hue(slugOf(t))}`} />
              <a href={resolveRelative(from, slugOf(t) as FullSlug)}>{titleOf(t)}</a>
            </span>
            <p>{blurb ? jsx(blurb) : null}</p>
            {counts[i].map((n, j) => (
              <span class="c">
                <span style={`--v:${Math.round((n / max[j]) * 100)}`} data-v={n === 0 ? "0" : undefined}>
                  {n}
                </span>
              </span>
            ))}
          </div>
        )
      })}
    </div>
  )
}
