// Result and open-question cards: the front of the wiki in a preview build. Every
// word a card shows comes from page frontmatter that publish/cards.py wrote, so
// nothing here re-maps or judges a record. The cards carry data attributes the
// browser script filters on (src/client/cards.ts).
import type { FullSlug } from "@quartz-community/types"
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
const kindOf = (m: FindingFm) => KIND_KEY[m.result ?? ""] ?? "result"
const NEED_CLASS: Record<string, string> = { data: "", build: "part", measure: "lab", unclear: "no" }

const fmOf = <T,>(f: File) => (f.frontmatter ?? {}) as T
const searchText = (...parts: (string | undefined)[]) => parts.filter(Boolean).join(" ").toLowerCase()
const topicSlug = (t: File) => slugOf(t).replace(/^topics\//, "")

export function findingsOf(c: Corpus): File[] {
  return [...c.bySlug.values()].filter((f) => collectionOf(slugOf(f)) === "findings" && !isIndex(slugOf(f)))
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
      <button type="button" class="chip" aria-expanded="true">
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

/** Chips that filter the cards beside them in the browser; without JavaScript all cards show. */
export function FilterChips({ group, label, options }: { group: string; label: string; options: [string, string][] }) {
  return (
    <div class="c-chips" data-filter-group={group} role="group" aria-label={label}>
      <button class="c-chip on" type="button" data-value="" aria-pressed="true">
        All
      </button>
      {options.map(([value, text]) => (
        <button class="c-chip" type="button" data-value={value} aria-pressed="false">
          {text}
        </button>
      ))}
    </div>
  )
}

const KIND_FILTERS: [string, string][] = [
  ["result", "Results"],
  ["interpretation", "Interpretations"],
  ["null", "Null or missing results"],
  ["correction", "Corrections"],
]

/** The results collection page: every result, filterable by kind and topic. */
export function ResultsBoard({ c, from }: { c: Corpus; from: FullSlug }) {
  const order = new Map(c.topics.map((t, i) => [topicSlug(t), i]))
  const topicIx = (f: File) => order.get(fmOf<FindingFm>(f).topic ?? "") ?? order.size
  const all = findingsOf(c).sort((a, b) => topicIx(a) - topicIx(b) || slugOf(a).localeCompare(slugOf(b)))
  const used = new Set(all.map((f) => fmOf<FindingFm>(f).topic).filter(Boolean))
  const topics = c.topics.filter((t) => used.has(topicSlug(t)))
  return (
    <section class="cards-board" data-cards>
      <FilterChips group="kind" label="Show results of one kind" options={KIND_FILTERS} />
      {topics.length > 0 && (
        <label class="c-select">
          Topic{" "}
          <select data-filter-select="topic">
            <option value="">All topics</option>
            {topics.map((t) => (
              <option value={topicSlug(t)}>{titleOf(t)}</option>
            ))}
          </select>
        </label>
      )}
      <div class="grid2">
        {all.map((f) => (
          <FindingCard f={f} from={from} c={c} />
        ))}
      </div>
    </section>
  )
}

const panelId = (g: SharedGroup) => `sp-${g.id}`

/** A result that several projects reached, with a button that opens the comparison. */
function SharedCard({ g, c, from }: { g: SharedGroup; c: Corpus; from: FullSlug }) {
  const topics = g.topics.length
  return (
    <article class="scard" data-panel={panelId(g)}>
      <span class="skicker">
        Across {g.sources.length} projects · {topics === 1 ? "one topic" : `${topics} topics`}
      </span>
      <h3>{g.title}</h3>
      <p class="gist">{g.sentence}</p>
      <span class="stopics">
        {g.topics.slice(0, 3).map((t) => (
          <span class="xtopic">{topicTitle(c, t)}</span>
        ))}
      </span>
      <ul class="sprojects">
        {g.sources.map((sid, i) => (
          <li>
            <a href={resolveRelative(from, `summaries/${sid}` as FullSlug)}>{g.projects[i]}</a>
          </li>
        ))}
      </ul>
      {g.relation && <p class="srel">{g.relation}</p>}
      <button type="button" class="scmp" aria-expanded="true" aria-controls={panelId(g)}>
        Compare the results
      </button>
    </article>
  )
}

/** The comparison under the cards: the shared question, each project's own result, how they relate. */
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

/** Results that span projects; the panels show until the browser script folds them. */
export function SharedCards({ groups, c, from }: { groups: SharedGroup[]; c: Corpus; from: FullSlug }) {
  return (
    <div class="shared" data-shared>
      <div class="grid2 grid3 scards">
        {groups.map((g) => (
          <SharedCard g={g} c={c} from={from} />
        ))}
      </div>
      {groups.map((g) => (
        <SharedPanel g={g} from={from} />
      ))}
    </div>
  )
}

/** The Results page's results that several projects reached, under the picture. */
export function SharedResults({ c, from }: { c: Corpus; from: FullSlug }) {
  const groups = resultsIndex(c).shared ?? []
  if (groups.length === 0) return null
  return (
    <section class="shared-results" aria-label="Results several projects reached">
      <div class="sechead">
        <h2>Results several projects reached</h2>
        <p>Each of these results came up in two or more projects.</p>
      </div>
      <SharedCards groups={groups} c={c} from={from} />
    </section>
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
