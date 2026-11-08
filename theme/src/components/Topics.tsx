// The topics, with what each covers and how much evidence stands behind it.
// The table and the map of the corpus live on the Topics index, after its
// topic cards; the home page links there instead of carrying them.
import type { FullSlug } from "@quartz-community/types"
import { resolveRelative, simplifySlug } from "@quartz-community/utils"
import type { ElementContent } from "hast"
import { jsx } from "../jsx"
import { CorpusMap, mapStats } from "../map"
import { type Corpus, type File, collectionOf, linksOf, slugOf, titleOf } from "../page"
import { findingsOf } from "./Cards"
import { TopicKey } from "./Strip"

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

const ENTITIES: Record<string, string> = { "&amp;": "&", "&lt;": "<", "&gt;": ">", "&quot;": '"', "&#039;": "'", "&#39;": "'" }
const squash = (s: string) => s.toLowerCase().replace(/[^a-z0-9]+/g, " ").trim()

/**
 * Each topic's one-line blurb, read off the home page's Topics list. Other pages
 * get no rendered tree for the home page, only its plain text, where each list
 * item is a line: "Title (11 concepts): Groups genes by ...".
 */
export function homeBlurbs(c: Corpus): Map<string, ElementContent[]> {
  const out = new Map<string, ElementContent[]>()
  const text = String(c.bySlug.get("index")?.text ?? "").replace(/&(?:amp|lt|gt|quot|#0?39);/g, (e) => ENTITIES[e])
  const byTitle = new Map(c.topics.map((t) => [squash(titleOf(t)), simplifySlug(slugOf(t))]))
  for (const line of text.split("\n")) {
    const m = line.trim().match(/^(.+?)\s*\(\d+\s+concepts?\)\s*:?\s*(.+)$/)
    const slug = m && byTitle.get(squash(m[1]))
    if (!slug || out.has(slug)) continue
    const value = m[2].trim()
    out.set(slug, [{ type: "text", value: value.charAt(0).toUpperCase() + value.slice(1) }])
  }
  return out
}

function SecHead({ title, deck }: { title: string; deck?: string }) {
  return (
    <div class="sechead">
      <h2>{title}</h2>
      {deck && <p>{deck}</p>}
    </div>
  )
}

/** What the Topics index shows after its topic cards: the topic key, the map, and the table. */
export function TopicsPage({ c, from }: { c: Corpus; from: FullSlug }) {
  if (c.topics.length === 0) return null
  const blurbs = homeBlurbs(c)
  const stats = mapStats(c)
  const published = findingsOf(c).length > 0
  return (
    <div class="topicspage">
      {published && <TopicKey c={c} from={from} blurbs={blurbs} />}
      <section aria-label="Map of the corpus">
        <SecHead
          title="The map"
          deck={`The ${stats.topics} topics and the ${stats.concepts} concepts they gather. Click a point to open its page.`}
        />
        {/* src/client/strips.ts lights the picked topic's cluster here. */}
        <div class="mapframe" id="topic-map" data-tmap>
          <CorpusMap c={c} from={from} />
        </div>
        <div class="maplegend">
          <span class="key">
            <i class="swatch" />A concept the topic gathers, sized by how linked it is
          </span>
          <span class="key">
            <i class="swatch grey" />A concept no topic claims, on a dashed tether
          </span>
          <span class="key">
            <i class="tie" />
            {stats.crossings} links cross between topics, drawn as one line per pair of topics
          </span>
          <span class="key">Hover a concept for its own links, a topic for everything leaving it.</span>
          {published && <span class="key">The colours are the topics in the key above.</span>}
        </div>
      </section>
      <section aria-label="What each topic covers">
        <SecHead title="What each topic covers" />
        <Topics c={c} from={from} blurbs={blurbs} />
      </section>
    </div>
  )
}
