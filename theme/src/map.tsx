// The corpus map: nine topic hubs, each ringed by the concepts that belong to
// it, with the wikilinks that cross between them drawn faintly underneath.
//
// The shape is deliberate rather than simulated. A spring layout drew truer
// distances but dissolved the one thing the map is for: showing that the
// corpus has hubs and that pages hang off them. Fixed positions also mean the
// map is identical between builds, so a cluster stays where a reader learned
// to find it. Nothing runs in the browser: hovering a point reveals its title
// and its own cross-topic links through CSS alone, using :has().
import { resolveRelative } from "@quartz-community/utils"
import type { FullSlug } from "@quartz-community/types"
import { type Corpus, type File, collectionOf, isIndex, linksOf, slugOf, titleOf, truncate } from "./page"

const W = 1200
const H = 790
const COLS = [190, 600, 1010]
// Room above the first row for a two-line hub label.
const ROWS = [165, 410, 655]
// Concepts occupy 300 degrees of the ring; the gap at the top is where the
// hub's own label goes.
const ARC = 300
const ARC_FROM = -60
const RING_MIN = 62
const RING_MAX = 86
const TWO_RINGS_ABOVE = 9
// Longest a hub label line runs before it wraps, in characters.
const LABEL_CHARS = 24

interface Point {
  file: File
  /** Position in the map, used to name the CSS classes that pair a point
      with its own links. */
  id: number
  x: number
  y: number
  hue: string
  deg: number
  /** No topic links to this page; it sits by the cluster it cites most. */
  adopted: boolean
}

interface Cluster {
  topic: File
  id: number
  x: number
  y: number
  hue: string
  radius: number
  points: Point[]
}

/** One line per pair of topics, carrying every link that crosses between them. */
interface Tie {
  a: Cluster
  b: Cluster
  count: number
}

interface Graph {
  clusters: Cluster[]
  ties: Tie[]
  /** Every individual wikilink that crosses between two clusters. */
  links: [Point, Point][]
  /** A concept drawn in one cluster that a second topic also claims. */
  shared: [Point, Cluster][]
  concepts: number
}

const cache = new WeakMap<Corpus, Graph>()

function build(c: Corpus): Graph {
  const concepts = [...c.bySlug.values()]
    .filter((f) => collectionOf(slugOf(f)) === "concepts" && !isIndex(slugOf(f)))
    .sort((a, b) => titleOf(a).localeCompare(titleOf(b)))

  // A concept belongs to the first topic that links to it, in topic order.
  const owner = new Map<string, string>()
  for (const t of c.topics) {
    for (const l of new Set(linksOf(t))) {
      if (!owner.has(l) && c.bySlug.has(l) && collectionOf(l) === "concepts") owner.set(l, slugOf(t))
    }
  }
  // No topic links to twenty of them. Rather than drop those or invent a
  // membership, seat each beside the cluster its own neighbours belong to and
  // mark it as unclaimed when it is drawn.
  const adopted = new Set<string>()
  for (const f of concepts) {
    const slug = slugOf(f)
    if (owner.has(slug)) continue
    const votes = new Map<string, number>()
    const bump = (t: string, n: number) => votes.set(t, (votes.get(t) ?? 0) + n)
    const near = new Set<string>([...linksOf(f), ...(c.inbound.get(slug) ?? []).map(slugOf)])
    for (const n of near) {
      if (collectionOf(n) === "topics") bump(n, 2)
      const o = owner.get(n)
      if (o) bump(o, 1)
    }
    let best = ""
    let score = 0
    // Sorted so a tie always falls the same way, build after build.
    for (const [t, v] of [...votes].sort((a, b) => a[0].localeCompare(b[0]))) {
      if (v > score) {
        best = t
        score = v
      }
    }
    if (best) {
      owner.set(slug, best)
      adopted.add(slug)
    }
  }

  const degree = (f: File) =>
    new Set([...linksOf(f), ...(c.inbound.get(slugOf(f)) ?? []).map(slugOf)]).size

  const at = new Map<string, [Point, Cluster]>()
  let id = 0
  const clusters: Cluster[] = c.topics.map((t, i) => {
    const cx = COLS[i % COLS.length]
    const cy = ROWS[Math.floor(i / COLS.length) % ROWS.length]
    const hue = c.hue(slugOf(t))
    // Members first, then the unclaimed, so the grey points form one arc
    // rather than speckling the ring.
    const members = concepts.filter((f) => owner.get(slugOf(f)) === slugOf(t))
    members.sort((a, b) => {
      const ax = adopted.has(slugOf(a)) ? 1 : 0
      const bx = adopted.has(slugOf(b)) ? 1 : 0
      return ax - bx || titleOf(a).localeCompare(titleOf(b))
    })
    const n = members.length
    const radius = Math.max(RING_MIN, Math.min(RING_MAX, 56 + n * 2.4))
    const inner = n > TWO_RINGS_ABOVE ? Math.floor(n * 0.45) : 0
    const outer = n - inner
    const place = (idx: number, count: number, r: number): [number, number] => {
      const a = ((ARC_FROM + ((idx + 0.5) * ARC) / Math.max(1, count)) * Math.PI) / 180
      return [cx + Math.cos(a) * r, cy + Math.sin(a) * r]
    }
    const round = (v: number) => Math.round(v * 10) / 10
    const points: Point[] = members.map((f, j) => {
      const [x, y] = j < outer ? place(j, outer, radius) : place(j - outer, inner, radius * 0.54)
      return {
        file: f,
        id: id++,
        x: round(x),
        y: round(y),
        hue: adopted.has(slugOf(f)) ? "var(--line-2)" : hue,
        deg: degree(f),
        adopted: adopted.has(slugOf(f)),
      }
    })
    const cluster: Cluster = { topic: t, id: i, x: cx, y: cy, hue, radius, points }
    for (const p of points) at.set(slugOf(p.file), [p, cluster])
    return cluster
  })

  // Every wikilink that leaves one cluster for another. Drawn all at once they
  // cover the frame in grey and the hubs stop reading as hubs, so at rest the
  // map shows one tie per pair of topics, weighted by how many links it
  // carries; the individual links appear when a point or a hub is hovered.
  const seen = new Set<string>()
  const links: [Point, Point][] = []
  const tally = new Map<string, Tie>()
  const tie = (x: Cluster, y: Cluster) => {
    const [a, b] = x.id < y.id ? [x, y] : [y, x]
    const key = `${a.id}|${b.id}`
    const found = tally.get(key)
    if (found) found.count++
    else tally.set(key, { a, b, count: 1 })
  }
  for (const [slug, [p, cl]] of at) {
    for (const l of new Set(linksOf(p.file))) {
      const other = at.get(l)
      if (!other || other[1] === cl) continue
      const key = slug < l ? `${slug}|${l}` : `${l}|${slug}`
      if (seen.has(key)) continue
      seen.add(key)
      links.push([p, other[0]])
      tie(cl, other[1])
    }
  }
  const ties = [...tally.values()].sort((x, y) => x.count - y.count)

  // A concept drawn in one cluster that a second topic also claims. Three
  // concepts in this corpus; they get a second spoke rather than being folded
  // into the tie counts, which measure links between concepts.
  const shared: [Point, Cluster][] = []
  for (const cl of clusters) {
    for (const l of new Set(linksOf(cl.topic))) {
      const other = at.get(l)
      if (other && other[1] !== cl) shared.push([other[0], cl])
    }
  }

  const out: Graph = { clusters, ties, links, shared, concepts: concepts.length }
  cache.set(c, out)
  return out
}

const graph = (c: Corpus): Graph => cache.get(c) ?? build(c)

export function mapStats(c: Corpus) {
  const g = graph(c)
  return { topics: g.clusters.length, concepts: g.concepts, crossings: g.links.length, ties: g.ties.length }
}

// Hub labels sit above the cluster, not in it: a title long enough to matter
// is wider than the gap at the top of the ring. Two lines, wrapped on a word.
function labelLines(title: string): string[] {
  const words = title.split(" ")
  const lines: string[] = [""]
  for (const w of words) {
    const line = lines[lines.length - 1]
    if (line && line.length + 1 + w.length > LABEL_CHARS && lines.length < 2) lines.push(w)
    else lines[lines.length - 1] = line ? `${line} ${w}` : w
  }
  return lines.map((l, i) => (i === lines.length - 1 ? truncate(l, LABEL_CHARS + 6) : l))
}

export function CorpusMap({ c, from }: { c: Corpus; from: FullSlug }) {
  const { clusters, ties, links, shared } = graph(c)
  if (clusters.length === 0) return null
  const href = (f: File) => resolveRelative(from, slugOf(f) as FullSlug)
  const radius = (p: Point) => 3.4 + Math.min(3.4, Math.sqrt(p.deg))
  const heaviest = Math.max(1, ...ties.map((t) => t.count))
  // Hovering a point shows the links that touch it; hovering a hub shows every
  // link leaving that topic. Each rule pairs one hovered element with its own
  // links by class, which is the only way to express it without script.
  // Keyboard focus triggers the same reveal as the pointer, so tabbing the map
  // shows the same thing hovering it does.
  const on = (sel: string, body: string) =>
    `svg:has(${sel}:hover) ${body},svg:has(${sel}:focus-visible) ${body}`
  const reveal = [
    `${on("a.pt", ".tie")}{opacity:.1}`,
    `${on("a.pt", ".halo")}{opacity:.03}`,
    ...clusters.flatMap((cl) => [
      `${on(`a.hub.c${cl.id}`, `.link.c${cl.id}`)}{opacity:.8}`,
      ...cl.points.map((p) => `${on(`a.n${p.id}`, `.link.n${p.id}`)}{opacity:1}`),
    ]),
  ].join("")
  // A curve that bows away from the middle of the map, so a line between two
  // far-apart things goes around whatever sits between them rather than over
  // it. Ties start at the edge of their clusters; links join points directly.
  const curve = (ax: number, ay: number, bx: number, by: number, gapA = 0, gapB = 0) => {
    const vx = bx - ax
    const vy = by - ay
    const d = Math.hypot(vx, vy) || 1
    const x1 = ax + (vx * gapA) / d
    const y1 = ay + (vy * gapA) / d
    const x2 = bx - (vx * gapB) / d
    const y2 = by - (vy * gapB) / d
    const mx = (x1 + x2) / 2
    const my = (y1 + y2) / 2
    const away = (mx - W / 2) * -(vy / d) + (my - H / 2) * (vx / d) >= 0 ? 1 : -1
    const bow = d * 0.14 * away
    const cx = mx - (vy / d) * bow
    const cy = my + (vx / d) * bow
    const r = (v: number) => Math.round(v * 10) / 10
    return `M ${r(x1)} ${r(y1)} Q ${r(cx)} ${r(cy)} ${r(x2)} ${r(y2)}`
  }
  const tieArc = (t: Tie) => curve(t.a.x, t.a.y, t.b.x, t.b.y, t.a.radius + 22, t.b.radius + 22)
  const at = new Map(clusters.flatMap((cl) => cl.points.map((p) => [p, cl] as const)))
  return (
    <svg viewBox={`0 0 ${W} ${H}`} role="img" aria-label="Map of every topic and concept in the corpus">
      <g class="ties">
        {ties.map((t) => (
          <path class="tie" d={tieArc(t)} style={`--w:${(0.7 + (t.count / heaviest) * 4).toFixed(2)}`}>
            <title>
              {titleOf(t.a.topic)} and {titleOf(t.b.topic)}: {t.count} wikilinks between their
              concepts
            </title>
          </path>
        ))}
      </g>
      {clusters.map((cl) => (
        <circle class="halo" cx={cl.x} cy={cl.y} r={cl.radius + 20} style={`--c:${cl.hue}`} />
      ))}
      <style dangerouslySetInnerHTML={{ __html: reveal }} />
      <g class="links">
        {links.map(([a, b]) => (
          <path
            class={`link n${a.id} n${b.id} c${at.get(a)!.id} c${at.get(b)!.id}`}
            d={curve(a.x, a.y, b.x, b.y)}
          />
        ))}
        {shared.map(([p, cl]) => (
          <path class="second" d={curve(p.x, p.y, cl.x, cl.y, 0, 11)} style={`--c:${cl.hue}`}>
            <title>
              {titleOf(p.file)} also belongs to {titleOf(cl.topic)}
            </title>
          </path>
        ))}
      </g>
      {clusters.map((cl) => (
        <g class="cluster" style={`--c:${cl.hue}`}>
          {cl.points.map((p) => (
            <line class={p.adopted ? "spoke loose" : "spoke"} x1={cl.x} y1={cl.y} x2={p.x} y2={p.y} />
          ))}
          {cl.points.map((p) => {
            const right = p.x > W * 0.62
            return (
              <a class={`pt n${p.id}`} href={href(p.file)}>
                <title>{titleOf(p.file)}</title>
                <circle class="node" cx={p.x} cy={p.y} r={radius(p)} style={`--c:${p.hue}`} />
                <circle class="hit" cx={p.x} cy={p.y} r={11} />
                <text
                  class="clabel"
                  x={p.x + (right ? -10 : 10)}
                  y={p.y + 3.5}
                  text-anchor={right ? "end" : "start"}
                >
                  {truncate(titleOf(p.file), 46)}
                </text>
              </a>
            )
          })}
          <a class={`pt hub c${cl.id}`} href={href(cl.topic)}>
            <title>{titleOf(cl.topic)}</title>
            <circle class="node hub" cx={cl.x} cy={cl.y} r={11} style={`--c:${cl.hue}`} />
            {(() => {
              const lines = labelLines(titleOf(cl.topic))
              const top = cl.y - cl.radius - 24 - (lines.length - 1) * 17
              return (
                <text class="tlabel" x={cl.x} y={top} text-anchor="middle">
                  {lines.map((l, i) => (
                    <tspan x={cl.x} dy={i === 0 ? 0 : 17}>
                      {l}
                    </tspan>
                  ))}
                </text>
              )
            })()}
          </a>
        </g>
      ))}
    </svg>
  )
}
