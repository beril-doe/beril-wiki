// The open-questions grid: topics down the side, what answering a question needs
// across the top, one dot per question. Every word comes from the question's
// frontmatter (publish/cards.py wrote it); only the dot shape keys on the raw
// `approach` value. The dots are links, so the grid works without JavaScript;
// src/client/questions.ts adds the tap-to-pin behaviour.
import type { FullSlug } from "@quartz-community/types"
import { resolveRelative } from "@quartz-community/utils"
import { type Corpus, type File, slugOf, titleOf } from "../page"
import { directionsOf } from "./Cards"
import { TopicStrip, topicList } from "./Strip"

interface CrossProject {
  source: string
  title: string
  topic: string
  results: { id: string; title: string }[]
}

interface QuestionFm {
  need?: string
  need_text?: string
  approach?: string
  approach_text?: string
  topic?: string
  readiness_basis?: string
  cross?: CrossProject[]
  cross_topics?: string[]
  home_question_rank?: number
}

/** Column order and the fallback header text when no question in the grid supplies its own. */
export const NEEDS: [string, string][] = [
  ["data", "Data already in the lakehouse"],
  ["build", "Analysis to build"],
  ["measure", "New measurements"],
  ["unclear", "Not yet clear"],
]

// Raw approach values in legend order; the shape CSS keys on the same strings.
const APPROACHES = ["lakehouse analysis", "experiment", "analysis then experiment"]

const fmOf = (f: File) => (f.frontmatter ?? {}) as QuestionFm
const topicSlug = (t: File) => slugOf(t).replace(/^topics\//, "")

interface Row {
  slug: string
  file?: File
  items: File[]
}

function rowsOf(c: Corpus, qs: File[], only?: string): Row[] {
  const by = new Map<string, File[]>()
  for (const q of qs) {
    const t = fmOf(q).topic ?? ""
    by.set(t, [...(by.get(t) ?? []), q])
  }
  const sorted = (xs: File[]) => xs.sort((a, b) => titleOf(a).localeCompare(titleOf(b)))
  const rows: Row[] = c.topics.filter((t) => by.has(topicSlug(t))).map((t) => ({ slug: topicSlug(t), file: t, items: sorted(by.get(topicSlug(t))!) }))
  const known = new Set(c.topics.map(topicSlug))
  for (const [slug, items] of by) if (!known.has(slug)) rows.push({ slug, items: sorted(items) })
  return only ? rows.filter((r) => r.slug === only) : rows
}

const popId = (q: File) => `qp-${slugOf(q).replace(/[^a-z0-9]+/gi, "-")}`

const SHOWN_RESULTS = 3

const plural = (n: number, one: string, many: string) => `${n} ${n === 1 ? one : many}`

/** "Joins 3 projects across 5 topics", or "in one topic". */
export function joinsText(projects: number, topics: number) {
  return `Joins ${projects} projects ${topics === 1 ? "in one topic" : `across ${plural(topics, "topic", "topics")}`}`
}

/** The projects a cross-project question joins, each with its topic and the results it builds on. */
function Bridge({ c, m, from, href }: { c: Corpus; m: QuestionFm; from: FullSlug; href: string }) {
  if (!m.cross) return null
  return (
    <span class="qbridge">
      <span class="qjoins">{joinsText(m.cross.length, m.cross_topics?.length ?? 0)}</span>
      {m.cross.map((p) => (
        <span class="qproj">
          <a class="qpname" href={resolveRelative(from, `summaries/${p.source}` as FullSlug)}>
            {p.title}
          </a>
          {p.topic && <span class="qptopic">{topicName(c, p.topic)}</span>}
          <span class="qpres">
            {p.results.slice(0, SHOWN_RESULTS).map((r) => (
              <a href={resolveRelative(from, `findings/${r.id}` as FullSlug)}>{r.title}</a>
            ))}
            {p.results.length > SHOWN_RESULTS && <a href={href}>and {p.results.length - SHOWN_RESULTS} more</a>}
          </span>
        </span>
      ))}
    </span>
  )
}

const topicName = (c: Corpus, slug: string) => {
  const t = c.bySlug.get(`topics/${slug}`)
  return t ? titleOf(t) : slug.replace(/-/g, " ")
}

/** The dot is the link; the pop-up is its sibling so it can hold its own "Open the question" link.
 * Its name carries the approach, which the dot's shape shows to sighted readers. */
function Dot({ q, c, from, hue }: { q: File; c: Corpus; from: FullSlug; hue: string }) {
  const m = fmOf(q)
  const href = resolveRelative(from, slugOf(q) as FullSlug)
  const label = [titleOf(q), m.approach_text, m.cross ? joinsText(m.cross.length, m.cross_topics?.length ?? 0) : ""]
    .filter(Boolean)
    .join(". ")
  return (
    <span class={`qd${m.cross ? " cross" : ""}`} style={`--hue:${hue}`}>
      <a class="qdot" href={href} data-shape={m.approach} aria-label={label} aria-describedby={popId(q)} />
      <span class="qpop" id={popId(q)}>
        <strong>{titleOf(q)}</strong>
        <span class="qneed">
          {m.approach_text && `${m.approach_text}. `}Needs: {m.need_text}. {m.readiness_basis}
        </span>
        <Bridge c={c} m={m} from={from} href={href} />
        <a class="qopen" href={href}>
          Open the question
        </a>
      </span>
    </span>
  )
}

/** Up to three questions that join projects, for the home page. */
export function CrossQuestions({ c, from }: { c: Corpus; from: FullSlug }) {
  const rank = (q: File) => fmOf(q).home_question_rank
  const picks = directionsOf(c)
    .filter((q) => rank(q) !== undefined)
    .sort((a, b) => rank(a)! - rank(b)!)
  if (picks.length === 0) return null
  return (
    <ul class="xqlist">
      {picks.map((q) => {
        const m = fmOf(q)
        return (
          <li data-topics={topicList(m.cross_topics, m.topic)}>
            <a class="xqt" href={resolveRelative(from, slugOf(q) as FullSlug)}>
              {titleOf(q)}
            </a>
            <span class="xqp">Builds on {m.cross!.map((p) => p.title).join(" · ")}</span>
            <TopicStrip c={c} topics={m.cross_topics} primary={m.topic} />
          </li>
        )
      })}
    </ul>
  )
}

// A need outside the four known keys reads as "not yet clear" so no question drops out of the grid.
const needKey = (q: File) => {
  const n = fmOf(q).need ?? ""
  return NEEDS.some(([k]) => k === n) ? n : "unclear"
}

/** A topic by need grid. `topic` keeps one row (the topic hub). */
export function QuestionGrid({ c, from, topic }: { c: Corpus; from: FullSlug; topic?: string }) {
  const rows = rowsOf(c, directionsOf(c), topic)
  const all = rows.flatMap((r) => r.items)
  if (all.length === 0) return null
  const cols = NEEDS.map(([key, fallback]) => {
    const n = all.filter((q) => needKey(q) === key).length
    const label = all.find((q) => fmOf(q).need === key && fmOf(q).need_text)
    return { key, n, label: label ? fmOf(label).need_text! : fallback }
  })
  const seen = new Map<string, string>()
  for (const q of all) if (fmOf(q).approach && fmOf(q).approach_text) seen.set(fmOf(q).approach!, fmOf(q).approach_text!)
  const qcols = cols.map((col) => `minmax(9rem,${Math.max(col.n, 1)}fr)`).join(" ")
  return (
    <div class="qwrap">
      <div class="qgrid" data-single={topic ? "1" : undefined} style={`--qcols:${qcols}`}>
        <div class="qrow qhead">
          {!topic && <span class="qcorner" />}
          {cols.map((col) => (
            <span class="qcolh">
              {col.label} <span class="qn">{col.n}</span>
            </span>
          ))}
        </div>
        {rows.map((r) => (
          <div class="qrow">
            {!topic && (
              <span class="qrowh">
                {r.file ? <a href={resolveRelative(from, slugOf(r.file) as FullSlug)}>{titleOf(r.file)}</a> : r.slug || "Other"}
              </span>
            )}
            {cols.map((col) => {
              const cell = r.items.filter((q) => needKey(q) === col.key)
              return (
                <div class="qcell" data-empty={cell.length === 0 ? "1" : undefined}>
                  <span class="qlab">{col.label}</span>
                  <div class="qdots">
                    {cell.map((q) => (
                      <Dot q={q} c={c} from={from} hue={r.file ? (c.hueOf(r.file) ?? "var(--mute)") : "var(--mute)"} />
                    ))}
                  </div>
                </div>
              )
            })}
          </div>
        ))}
      </div>
      <p class="qlegend">
        {APPROACHES.filter((a) => seen.has(a)).map((a) => (
          <span class="qkey">
            <i class="qdot-key" data-shape={a} aria-hidden="true" /> {seen.get(a)}
          </span>
        ))}
        {all.some((q) => fmOf(q).cross) && (
          <span class="qkey">
            <i class="qdot-key ring" aria-hidden="true" /> Builds on results from two or more projects
          </span>
        )}
        <span class="qkey">Colour is the topic.</span>
        <span class="qkey">Hover or tap a dot to read it.</span>
      </p>
    </div>
  )
}

/** The /directions/ page below its intro: the full grid, then every question as a plain list. */
export function QuestionsPage({ c, from }: { c: Corpus; from: FullSlug }) {
  const qs = directionsOf(c)
  const rows = rowsOf(c, qs)
  return (
    <section class="cards-board qpage">
      <QuestionGrid c={c} from={from} />
      <details class="qall">
        <summary>All {qs.length} as a list</summary>
        {rows.map((r) => (
          <div>
            <h3>{r.file ? titleOf(r.file) : r.slug || "Other"}</h3>
            <ul class="qlist">
              {r.items.map((q) => (
                <li>
                  <a href={resolveRelative(from, slugOf(q) as FullSlug)}>{titleOf(q)}</a>
                  {fmOf(q).approach_text && <span class="n"> {fmOf(q).approach_text}.</span>}
                  {fmOf(q).need_text && <span class="n"> Needs: {fmOf(q).need_text}.</span>}
                  {fmOf(q).cross && <span class="n"> {joinsText(fmOf(q).cross!.length, fmOf(q).cross_topics?.length ?? 0)}.</span>}
                </li>
              ))}
            </ul>
          </div>
        ))}
      </details>
    </section>
  )
}
