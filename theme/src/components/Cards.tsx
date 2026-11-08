// Result and open-question cards: the front of the wiki. Every
// word a card shows comes from page frontmatter that publish/cards.py wrote, so
// nothing here re-maps or judges a record. The cards carry data attributes the
// browser script filters on (src/client/cards.ts).
import type { FullSlug } from "@quartz-community/types"
import type { ComponentChildren } from "preact"
import { resolveRelative } from "@quartz-community/utils"
import { type Corpus, type File, collectionOf, isIndex, slugOf, titleOf } from "../page"
import { QuestionGrid } from "./Questions"
import { TopicStrip, topicList } from "./Strip"

export interface FindingFm {
  result?: string
  compare_text?: string
  source?: string
  topics?: string[]
  kind_text?: string
  chip?: string
  chip_note?: string
  gist?: string
  gist_case?: string
  topic?: string
  report_title?: string
  home_rank?: number
  topic_ranks?: Record<string, number>
  listed?: boolean
}

export interface SharedMember {
  id: string
  title: string
  gist: string
  lane: string
  source: string
  report_title: string
  chip: string
  chip_note?: string
}

export interface SharedGroup {
  id: string
  title: string
  sentence: string
  question: string
  how: string
  relation: string
  projects: string[]
  sources: string[]
  topics: string[]
  members: SharedMember[]
}

export interface PictureLink {
  a?: string
  b?: string
  pa: string
  pb: string
  family: "r" | "q" | "p"
  label?: string
  questions?: string[]
}

/** What publish writes on the results index page for the picture and the home cards. */
export interface ResultsIndexFm {
  compare_order?: string[]
  compare_notes?: Record<string, string>
  links?: PictureLink[]
  shared?: SharedGroup[]
  project_titles?: Record<string, string>
  empty_topics?: string[]
}

export const resultsIndex = (c: Corpus): ResultsIndexFm =>
  (c.bySlug.get("findings/index")?.frontmatter ?? {}) as ResultsIndexFm

export interface DirectionFm {
  need?: string
  need_text?: string
  approach_text?: string
  topic?: string
  beril_prompt?: string
  brief?: string
}

// Filter keys for the kind chips, keyed on the raw `result` so a wording change in
// publish cannot misfilter; the words shown come from kind_text.
const KIND_KEY: Record<string, string> = {
  observation: "result",
  inference: "interpretation",
  "null result": "null",
  correction: "correction",
}
/** The filter and mark key for a result's kind: result, interpretation, null or correction. */
export const kindKey = (m: FindingFm) => KIND_KEY[m.result ?? ""] ?? "result"
const kindOf = kindKey
const NEED_CLASS: Record<string, string> = { data: "", build: "part", measure: "lab", unclear: "no" }

const fmOf = <T,>(f: File) => (f.frontmatter ?? {}) as T
const searchText = (...parts: (string | undefined)[]) => parts.filter(Boolean).join(" ").toLowerCase()
const topicSlug = (t: File) => slugOf(t).replace(/^topics\//, "")

/** Listed findings. publish/cards.py marks a finding `listed: false` when it is not a
 * result a reader should browse (no plain summary, a repeat, missing data); its page stays. */
export function findingsOf(c: Corpus): File[] {
  return [...c.bySlug.values()].filter(
    (f) =>
      collectionOf(slugOf(f)) === "findings" && !isIndex(slugOf(f)) && (f.frontmatter as FindingFm | undefined)?.listed !== false,
  )
}

export function directionsOf(c: Corpus): File[] {
  return [...c.bySlug.values()].filter((f) => collectionOf(slugOf(f)) === "directions" && !isIndex(slugOf(f)))
}

const topicTitle = (c: Corpus | undefined, slug: string) => {
  const t = c?.bySlug.get(`topics/${slug}`)
  return t ? titleOf(t) : slug.replace(/-/g, " ")
}

/** The comparison chip. With a note it is a button that reveals the note; the note is
 * visible until the script hides it, so it reads without JavaScript. */
function Chip({ m }: { m: FindingFm }) {
  if (!m.chip) return null
  if (!m.chip_note) {
    return (
      <span class="chipwrap">
        <span class="chip">{m.chip}</span>
      </span>
    )
  }
  return (
    <span class="chipwrap">
      <button type="button" class="chip" aria-expanded="true" title={m.chip_note}>
        {m.chip}
      </button>
      <span class="note">{m.chip_note}</span>
    </span>
  )
}

/** `c` supplies the topic title; without it the footer shows the topic slug. `strip` adds
 * the home page's topic strip. */
export function FindingCard({ f, from, c, strip }: { f: File; from: FullSlug; c?: Corpus; strip?: boolean }) {
  const m = fmOf<FindingFm>(f)
  const kind = kindOf(m)
  return (
    <article
      class="fcard"
      data-topic={m.topic}
      data-topics={strip ? topicList(m.topics, m.topic) : undefined}
      data-kind={kind}
      data-text={searchText(titleOf(f), m.gist, m.report_title)}
    >
      {strip && c && <TopicStrip c={c} topics={m.topics} primary={m.topic} />}
      {m.gist && (
        <div class="tags">
          <span class={`rt${kind === "null" ? " null" : ""}`}>{m.kind_text}</span>
        </div>
      )}
      <h3>
        <a href={resolveRelative(from, slugOf(f) as FullSlug)}>{titleOf(f)}</a>
      </h3>
      {m.gist && <p class="gist">{m.gist}</p>}
      {m.gist && <Chip m={m} />}
      <div class="meta">
        {m.source && (
          <span>
            <a href={resolveRelative(from, `summaries/${m.source}` as FullSlug)}>{m.report_title || m.source}</a>
          </span>
        )}
        {m.topic && <span class={m.source ? "sep" : undefined}>{topicTitle(c, m.topic)}</span>}
      </div>
    </article>
  )
}

/** What the browser filter bar (src/client/board.ts) offers over a board's cards. Each card
 * carries data-f-<facet>, data-t-<toggle> and data-s-<sort> attributes the bar reads. */
export interface BoardConfig {
  noun: string
  facets: { key: string; label: string; chips: { v: string; label: string; hue?: string; note?: string }[] }[]
  toggles: { key: string; label: string }[]
  sorts: { key: string; label: string }[]
}

/** A board: the filter bar's settings, then the cards in the concepts card look. */
export function Board({ cfg, children, label }: { cfg: BoardConfig; children: ComponentChildren; label: string }) {
  return (
    <section class="board" data-board aria-label={label}>
      <script type="application/json" class="board-cfg" dangerouslySetInnerHTML={{ __html: JSON.stringify(cfg).replace(/</g, "\\u003c") }} />
      <div class="cards">{children}</div>
    </section>
  )
}

const KIND_WORDS: [string, string][] = [
  ["result", "Result"],
  ["null", "No effect found, or inconclusive"],
  ["interpretation", "Interpretation"],
  ["correction", "Correction"],
]

const panelId = (g: SharedGroup) => `sp-${g.id}`

/** A result in the concepts card look. It is a container, not a link, so it can hold the
 * comparison chip and the Compare button; the title link covers the card. */
function ResultCard({ f, c, from, group, related, ranks }: {
  f: File
  c: Corpus
  from: FullSlug
  group?: SharedGroup
  related: boolean
  ranks: Record<string, number>
}) {
  const m = fmOf<FindingFm>(f)
  const id = slugOf(f).replace(/^findings\//, "")
  const kind = kindOf(m)
  return (
    <article
      class="card rcard"
      style={m.topic ? `--d:${c.hue(`topics/${m.topic}`)}` : undefined}
      data-id={id}
      data-f-topic={m.topic}
      data-f-compare={m.compare_text}
      data-f-kind={kind}
      data-t-rel={related ? "1" : undefined}
      data-text={searchText(titleOf(f), m.gist, m.report_title)}
      {...Object.fromEntries(Object.entries(ranks).map(([k, v]) => [`data-s-${k}`, String(v)]))}
    >
      <b>
        <a class="ct" href={resolveRelative(from, slugOf(f) as FullSlug)}>
          {titleOf(f)}
        </a>
      </b>
      <span class="ctags">
        <span class={`rt${kind === "null" ? " null" : ""}`}>{m.kind_text}</span>
        <Chip m={m} />
      </span>
      {m.gist && <span class="desc">{m.gist}</span>}
      {group ? (
        <span class="crel">
          {group.relation || "Related result in another project"}
          <button type="button" class="ccmp" aria-expanded="true" aria-controls={panelId(group)}>
            Compare
          </button>
        </span>
      ) : (
        related && <span class="crel">Related result in another project</span>
      )}
      <span class="meta">
        <span>{m.report_title || m.source}</span>
        {m.topic && <span>{topicTitle(c, m.topic)}</span>}
      </span>
    </article>
  )
}

/** The comparison a Compare button opens: the shared question, each project's own result, how they relate. */
function SharedPanel({ g, from }: { g: SharedGroup; from: FullSlug }) {
  return (
    <section class="spanel" id={panelId(g)} aria-label={`Comparison: ${g.title}`}>
      <h4>{g.question}</h4>
      <div class="slanes">
        {g.members.map((m) => (
          <div class="slane">
            {m.lane && <span class="slabel">{m.lane}</span>}
            <div class="smini">
              <a class="stitle" href={resolveRelative(from, `findings/${m.id}` as FullSlug)}>
                {m.title}
              </a>
              {m.gist && <p>{m.gist}</p>}
              <a class="ssrc" href={resolveRelative(from, `summaries/${m.source}` as FullSlug)}>
                {m.report_title}
              </a>
              <Chip m={{ chip: m.chip, chip_note: m.chip_note }} />
            </div>
          </div>
        ))}
      </div>
      <p class="show">
        <strong>How they relate.</strong> {g.how}
      </p>
    </section>
  )
}

/** The Results page under the map: every listed result as a card, with the filter bar. */
export function ResultsBoard({ c, from }: { c: Corpus; from: FullSlug }) {
  const idx = resultsIndex(c)
  const order = idx.compare_order ?? []
  const topicIx = new Map(c.topics.map((t, i) => [topicSlug(t), i]))
  const all = findingsOf(c)
  const ids = new Set(all.map((f) => slugOf(f).replace(/^findings\//, "")))
  // A result is related when a related-result link joins it to another listed result, as the map rings it.
  const related = new Set(
    (idx.links ?? []).filter((l) => l.family === "r" && l.a && l.b && ids.has(l.a) && ids.has(l.b)).flatMap((l) => [l.a!, l.b!]),
  )
  const groups = (idx.shared ?? []).filter((g) => g.members.filter((m) => ids.has(m.id)).length >= 2)
  const groupOf = new Map(groups.flatMap((g) => g.members.map((m) => [m.id, g] as const)))
  const key = {
    novel: (f: File) => [order.indexOf(fmOf<FindingFm>(f).compare_text ?? ""), topicIx.get(fmOf<FindingFm>(f).topic ?? "") ?? 99, titleOf(f)] as const,
    topic: (f: File) => [topicIx.get(fmOf<FindingFm>(f).topic ?? "") ?? 99, order.indexOf(fmOf<FindingFm>(f).compare_text ?? ""), titleOf(f)] as const,
    project: (f: File) => [0, 0, `${fmOf<FindingFm>(f).report_title ?? ""} ${titleOf(f)}`] as const,
  }
  const cmp = (a: readonly [number, number, string], b: readonly [number, number, string]) => a[0] - b[0] || a[1] - b[1] || a[2].localeCompare(b[2])
  const rank = (k: keyof typeof key) => new Map([...all].sort((a, b) => cmp(key[k](a), key[k](b))).map((f, i) => [f, i]))
  const ranks = { novel: rank("novel"), topic: rank("topic"), project: rank("project") }
  const sorted = [...all].sort((a, b) => ranks.novel.get(a)! - ranks.novel.get(b)!)
  const count = <T,>(xs: File[], f: (x: File) => T) => (v: T) => xs.filter((x) => f(x) === v).length
  const byTopic = count(all, (f) => fmOf<FindingFm>(f).topic)
  const byCompare = count(all, (f) => fmOf<FindingFm>(f).compare_text)
  const byKind = count(all, (f) => kindOf(fmOf<FindingFm>(f)))
  const cfg: BoardConfig = {
    noun: "results",
    facets: [
      {
        key: "topic",
        label: "Topic",
        chips: c.topics
          .filter((t) => byTopic(topicSlug(t)) > 0)
          .map((t) => ({ v: topicSlug(t), label: titleOf(t), hue: c.hue(slugOf(t)) })),
      },
      {
        key: "compare",
        label: "How new",
        chips: order.filter((o) => byCompare(o) > 0).map((o) => ({ v: o, label: o, note: idx.compare_notes?.[o] })),
      },
      { key: "kind", label: "Kind", chips: KIND_WORDS.filter(([k]) => byKind(k) > 0).map(([v, label]) => ({ v, label })) },
    ],
    toggles: related.size > 0 ? [{ key: "rel", label: "Related across projects" }] : [],
    sorts: [
      { key: "novel", label: "Novel first" },
      { key: "topic", label: "Topic" },
      { key: "project", label: "Project" },
    ],
  }
  return (
    <>
      <Board cfg={cfg} label="Every result">
        {sorted.map((f) => {
          const id = slugOf(f).replace(/^findings\//, "")
          return (
            <ResultCard
              f={f}
              c={c}
              from={from}
              group={groupOf.get(id)}
              related={related.has(id)}
              ranks={{ novel: ranks.novel.get(f)!, topic: ranks.topic.get(f)!, project: ranks.project.get(f)! }}
            />
          )
        })}
      </Board>
      {groups.map((g) => (
        <SharedPanel g={g} from={from} />
      ))}
    </>
  )
}

/** "Results from this topic" on a topic hub, above its synthesis. */
export function TopicCards({ file, c }: { file: File; c: Corpus }) {
  const from = slugOf(file) as FullSlug
  const topic = topicSlug(file)
  const rankOf = (f: File) => fmOf<FindingFm>(f).topic_ranks?.[topic]
  const picks = findingsOf(c)
    .filter((f) => rankOf(f) !== undefined)
    .sort((a, b) => rankOf(a)! - rankOf(b)! || slugOf(a).localeCompare(slugOf(b)))
    .slice(0, 3)
  const hasQuestions = directionsOf(c).some((q) => fmOf<DirectionFm>(q).topic === topic)
  if (picks.length === 0 && !hasQuestions) return null
  return (
    <div class="topic-cards">
      {picks.length > 0 && (
      <section>
        <div class="sechead">
          <h2>Results from this topic</h2>
          <p>
            <a href={resolveRelative(from, "findings/index" as FullSlug)}>All results</a>
          </p>
        </div>
        <div class="grid2">
          {picks.map((f) => (
            <FindingCard f={f} from={from} c={c} />
          ))}
        </div>
      </section>
      )}
      {hasQuestions && (
        <section>
          <div class="sechead">
            <h2>Open questions in this topic</h2>
            <p>
              <a href={resolveRelative(from, "directions/index" as FullSlug)}>All open questions</a>
            </p>
          </div>
          <QuestionGrid c={c} from={from} topic={topic} />
        </section>
      )}
      <div class="sechead background-head">
        <h2>Background</h2>
        <p>The topic synthesis, its literature context and the concepts it gathers.</p>
      </div>
    </div>
  )
}

/** Under a result's or open question's title: what kind of record it is, and its handoffs. */
export function RecordBar({ file }: { file: File }) {
  const slug = slugOf(file)
  if (collectionOf(slug) === "findings") {
    const m = fmOf<FindingFm>(file)
    return (
      <div class="cardbar">
        <span class={`rt${kindOf(m) === "null" ? " null" : ""}`}>{m.kind_text}</span>
        <Chip m={m} />
      </div>
    )
  }
  const m = fmOf<DirectionFm>(file)
  return (
    <div class="cardbar">
      {m.approach_text && <span class="c-kind">{m.approach_text}</span>}
      {m.need_text && <span class={`ready ${NEED_CLASS[m.need ?? "unclear"] ?? "no"}`}>{m.need_text}</span>}
      {m.beril_prompt && (
        <button class="btn sm px-copy" type="button" data-copy={m.beril_prompt} title="A prompt to paste into BERIL">
          Copy BERIL prompt
        </button>
      )}
      {m.brief && (
        <button class="btn sm ghost px-copy" type="button" data-copy={m.brief} title="Markdown for a collaborator or a lab">
          Copy handoff brief
        </button>
      )}
    </div>
  )
}
