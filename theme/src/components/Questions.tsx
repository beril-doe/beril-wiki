// The open-questions grid: topics down the side, what answering a question needs
// across the top, one dot per question. Every word comes from the question's
// frontmatter (publish/cards.py wrote it). Position carries the topic and the need; a
// ring marks a question that builds on results from two or more projects, and orange a
// question that cites a result in the Results map's Novel column. The dots are links, so
// the grid works without JavaScript; src/client/questions.ts adds the tap-to-pin behaviour.
import type { FullSlug } from "@quartz-community/types"
import { resolveRelative } from "@quartz-community/utils"
import { type Corpus, type File, slugOf, titleOf } from "../page"
import { Board, type BoardConfig, type FindingFm, directionsOf, resultsIndex } from "./Cards"
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
  findings?: string[]
}

/** Column order and the fallback header text when no question in the grid supplies its own. */
export const NEEDS: [string, string][] = [
  ["data", "Data already in the lakehouse"],
  ["build", "Analysis to build"],
  ["measure", "New measurements"],
  ["unclear", "Not yet clear"],
]

/** The words a question carries when it cites a result in the Novel column. */
export const NOVEL_WORDS = "Cites a result in the Novel column"

/** Whether a question cites a listed result in the Results map's first (Novel) column. */
export function citesNovel(c: Corpus, q: File): boolean {
  const novel = resultsIndex(c).compare_order?.[0]
  if (!novel) return false
  return (fmOf(q).findings ?? []).some((id) => {
    const m = c.bySlug.get(`findings/${id}`)?.frontmatter as FindingFm | undefined
    return !!m && m.listed !== false && m.compare_text === novel
  })
}

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
 * Its name carries what the ring and the colour show to sighted readers. */
function Dot({ q, c, from }: { q: File; c: Corpus; from: FullSlug }) {
  const m = fmOf(q)
  const href = resolveRelative(from, slugOf(q) as FullSlug)
  const novel = citesNovel(c, q)
  const label = [titleOf(q), m.approach_text, novel ? NOVEL_WORDS : "", m.cross ? joinsText(m.cross.length, m.cross_topics?.length ?? 0) : ""]
    .filter(Boolean)
    .join(". ")
    .replace(/([?!])\. /g, "$1 ")
  return (
    <span class={`qd${m.cross ? " cross" : ""}${novel ? " novel" : ""}`} data-id={slugOf(q)}>
      <a class="qdot" href={href} aria-label={label} aria-describedby={popId(q)} />
      <span class="qpop" id={popId(q)}>
        <strong>{titleOf(q)}</strong>
        {novel && <span class="qnovel">{NOVEL_WORDS}.</span>}
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

/** A legend mark drawn by the same classes as the grid's dots. */
function LegendDot({ cls }: { cls?: string }) {
  return (
    <span class={`qd key${cls ? ` ${cls}` : ""}`} aria-hidden="true">
      <span class="qdot" />
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
              <span class="qrowh" style={r.file && c.hueOf(r.file) ? `--d:${c.hueOf(r.file)}` : undefined}>
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
                      <Dot q={q} c={c} from={from} />
                    ))}
                  </div>
                </div>
              )
            })}
          </div>
        ))}
      </div>
      <p class="qlegend">
        <span class="qkey">
          <LegendDot /> One question
        </span>
        {all.some((q) => citesNovel(c, q)) && (
          <span class="qkey">
            <LegendDot cls="novel" /> {NOVEL_WORDS}
          </span>
        )}
        {all.some((q) => fmOf(q).cross) && (
          <span class="qkey">
            <LegendDot cls="cross" /> Builds on results from two or more projects
          </span>
        )}
        <span class="qkey">Hover or tap a dot to read it.</span>
      </p>
    </div>
  )
}

const NEED_CLASS: Record<string, string> = { data: "", build: "part", measure: "lab", unclear: "no" }

/** A question in the concepts card look: what it still needs, in its own words. */
function QuestionCard({ q, c, from, ranks }: { q: File; c: Corpus; from: FullSlug; ranks: Record<string, number> }) {
  const m = fmOf(q)
  const novel = citesNovel(c, q)
  return (
    <article
      class="card qcard"
      style={m.topic ? `--d:${c.hue(`topics/${m.topic}`)}` : undefined}
      data-id={slugOf(q)}
      data-f-topic={m.topic}
      data-f-need={needKey(q)}
      data-f-approach={m.approach}
      data-t-cross={m.cross ? "1" : undefined}
      data-t-novel={novel ? "1" : undefined}
      data-text={[titleOf(q), m.readiness_basis, m.approach_text, m.need_text].filter(Boolean).join(" ").toLowerCase()}
      {...Object.fromEntries(Object.entries(ranks).map(([k, v]) => [`data-s-${k}`, String(v)]))}
    >
      <b>
        <a class="ct" href={resolveRelative(from, slugOf(q) as FullSlug)}>
          {titleOf(q)}
        </a>
      </b>
      <span class="ctags">
        {m.approach_text && <span class="c-kind">{m.approach_text}</span>}
        {m.need_text && <span class={`ready ${NEED_CLASS[needKey(q)] ?? "no"}`}>Needs: {m.need_text.toLowerCase()}</span>}
      </span>
      {m.readiness_basis && <span class="desc">{m.readiness_basis}</span>}
      {novel && <span class="cnovel">{NOVEL_WORDS}</span>}
      <span class="meta">
        {m.cross && <span>{joinsText(m.cross.length, m.cross_topics?.length ?? 0)}</span>}
        {m.topic && <span>{topicName(c, m.topic)}</span>}
      </span>
    </article>
  )
}

/** The /directions/ page below its intro: the full grid, then every question as a card with the filter bar. */
export function QuestionsPage({ c, from }: { c: Corpus; from: FullSlug }) {
  const qs = directionsOf(c)
  const rows = rowsOf(c, qs)
  const topicIx = new Map(rows.map((r, i) => [r.slug, i]))
  const needIx = (q: File) => NEEDS.findIndex(([k]) => k === needKey(q))
  const byTopic = [...qs].sort((a, b) => (topicIx.get(fmOf(a).topic ?? "") ?? 99) - (topicIx.get(fmOf(b).topic ?? "") ?? 99) || needIx(a) - needIx(b) || titleOf(a).localeCompare(titleOf(b)))
  const byNeed = [...qs].sort((a, b) => needIx(a) - needIx(b) || (topicIx.get(fmOf(a).topic ?? "") ?? 99) - (topicIx.get(fmOf(b).topic ?? "") ?? 99) || titleOf(a).localeCompare(titleOf(b)))
  const approaches = new Map<string, string>()
  for (const q of qs) if (fmOf(q).approach && fmOf(q).approach_text) approaches.set(fmOf(q).approach!, fmOf(q).approach_text!)
  const needs = NEEDS.map(([k, fallback]) => [k, qs.find((q) => fmOf(q).need === k && fmOf(q).need_text)?.frontmatter?.need_text as string | undefined ?? fallback] as const)
  const cfg: BoardConfig = {
    noun: "questions",
    facets: [
      {
        key: "topic",
        label: "Topic",
        chips: rows.filter((r) => r.file).map((r) => ({ v: r.slug, label: titleOf(r.file!), hue: c.hue(slugOf(r.file!)) })),
      },
      { key: "need", label: "What it needs", chips: needs.filter(([k]) => qs.some((q) => needKey(q) === k)).map(([v, label]) => ({ v, label })) },
      { key: "approach", label: "Approach", chips: [...approaches].map(([v, label]) => ({ v, label })) },
    ],
    toggles: [
      ...(qs.some((q) => fmOf(q).cross) ? [{ key: "cross", label: "Builds on results from two or more projects" }] : []),
      ...(qs.some((q) => citesNovel(c, q)) ? [{ key: "novel", label: NOVEL_WORDS }] : []),
    ],
    sorts: [
      { key: "topic", label: "Topic" },
      { key: "need", label: "What it needs" },
    ],
  }
  const rank = (xs: File[]) => new Map(xs.map((q, i) => [q, i]))
  const rt = rank(byTopic)
  const rn = rank(byNeed)
  return (
    <section class="cards-board qpage">
      <QuestionGrid c={c} from={from} />
      <Board cfg={cfg} label="Every open question">
        {byTopic.map((q) => (
          <QuestionCard q={q} c={c} from={from} ranks={{ topic: rt.get(q)!, need: rn.get(q)! }} />
        ))}
      </Board>
    </section>
  )
}
