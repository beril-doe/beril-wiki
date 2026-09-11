// Static SVG graphs rendered at build time. No client script: the shapes are
// small enough to lay out deterministically, and a page's neighbourhood does
// not change between builds.
import { resolveRelative } from "@quartz-community/utils"
import type { FullSlug } from "@quartz-community/types"
import { type Corpus, type File, collectionOf, linksOf, slugOf, titleOf, truncate } from "./page"

interface Node {
  file: File
  x: number
  y: number
  hue: string
}

// Rail graph: up to six wikilink neighbours in two columns, current page at
// the foot. Same shape on every page so the eye learns where to look.
const SLOTS: [number, number][] = [
  [14, 26],
  [262, 26],
  [14, 68],
  [262, 68],
  [14, 110],
  [262, 110],
]
const ME: [number, number] = [138, 148]
const GRAPH_COLLECTIONS = new Set(["concepts", "topics", "conflicts", "summaries"])
const ORDER = ["topics", "concepts", "conflicts", "entities", "summaries"]
// Two of the six slots are held for project reports. Synthesis pages link out
// to far more concepts than reports, so ranking alone put the evidence off the
// end of the graph on every page that had any.
const REPORT_SLOTS = 2
const isSummary = (f: File) => collectionOf(slugOf(f)) === "summaries"
export const rank = (f: File) => {
  const i = ORDER.indexOf(collectionOf(slugOf(f)))
  return i < 0 ? ORDER.length : i
}

export function neighbours(file: File, c: Corpus): File[] {
  const slug = slugOf(file)
  const seen = new Set<string>([slug])
  const out: File[] = []
  const add = (f: File | undefined) => {
    if (!f || seen.has(slugOf(f)) || !GRAPH_COLLECTIONS.has(collectionOf(slugOf(f)))) return
    seen.add(slugOf(f))
    out.push(f)
  }
  for (const l of linksOf(file)) add(c.bySlug.get(l))
  for (const f of c.inbound.get(slug) ?? []) add(f)
  out.sort((a, b) => rank(a) - rank(b) || titleOf(a).localeCompare(titleOf(b)))
  const reports = out.filter(isSummary)
  const rest = out.filter((f) => !isSummary(f))
  const head = SLOTS.length - Math.min(REPORT_SLOTS, reports.length)
  return [...rest.slice(0, head), ...reports, ...rest.slice(head)]
}

export function LocalGraph({ file, c }: { file: File; c: Corpus }) {
  const slug = slugOf(file) as FullSlug
  const nodes: Node[] = neighbours(file, c)
    .slice(0, SLOTS.length)
    .map((f, i) => ({ file: f, x: SLOTS[i][0], y: SLOTS[i][1], hue: c.hueOf(f) ?? "var(--line-2)" }))
  if (nodes.length < 2) return null
  return (
    <svg viewBox="0 0 276 172" role="img" aria-label="Pages linked to this one">
      {nodes.map((n) => (
        <line class="edge" x1={ME[0]} y1={ME[1]} x2={n.x} y2={n.y} />
      ))}
      {nodes.map((n) => {
        const right = n.x > ME[0]
        // A project report is evidence, not another synthesis page, so it is
        // marked apart from the round nodes rather than coloured the same.
        return (
          <a href={resolveRelative(slug, slugOf(n.file) as FullSlug)}>
            {isSummary(n.file) ? (
              <rect class="node report" x={n.x - 4} y={n.y - 4} width={8} height={8} style={`--c:${n.hue}`} />
            ) : (
              <circle class="node" cx={n.x} cy={n.y} r={4.5} style={`--c:${n.hue}`} />
            )}
            <text
              class="tlabel"
              x={n.x + (right ? -8 : 8)}
              y={n.y + 4}
              text-anchor={right ? "end" : "start"}
            >
              {truncate(titleOf(n.file), 19)}
            </text>
          </a>
        )
      })}
      <circle class="node me" cx={ME[0]} cy={ME[1]} r={7} />
      <text class="tlabel me" x={ME[0]} y={ME[1] + 19} text-anchor="middle">
        this page
      </text>
    </svg>
  )
}
