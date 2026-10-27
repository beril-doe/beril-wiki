// Finding and research-direction cards: the front of the wiki in a preview build. Every
// field comes from page frontmatter the pipeline wrote (stages headlines,
// novelty and directions, joined at publish by publish/cards.py), so nothing
// here judges a record. The cards carry data attributes the browser script
// filters on (src/client/cards.ts).
import type { FullSlug } from "@quartz-community/types"
import { resolveRelative } from "@quartz-community/utils"
import { type Corpus, type File, collectionOf, isIndex, slugOf, titleOf } from "../page"

export interface Quantity {
  value: string
  what: string
  unit?: string
}

export interface FindingFm {
  description?: string
  result?: string
  label?: string
  label_date?: string
  source?: string
  quantities?: Quantity[]
  caveat?: string
  topics?: string[]
  first_added?: string
}

export interface DirectionFm {
  description?: string
  hypothesis?: string
  approach?: string
  readiness?: string
  readiness_basis?: string
  collections?: string[]
  builds_on?: string[]
  projects?: string[]
  topics?: string[]
  beril_prompt?: string
  brief?: string
}

export const NOVEL = "Candidate novel"
export const EXTENDS = "Extends retrieved work"
export const TENSION = "In tension with retrieved work"
export const ESTABLISHED = "Established in retrieved literature"
export const INSUFFICIENT = "Insufficient literature evidence"
export const NOT_ASSESSED = "Not assessed"
// Card order on the home page: what published work does not already report first.
const LABEL_ORDER = [NOVEL, TENSION, EXTENDS, INSUFFICIENT, NOT_ASSESSED, ESTABLISHED]
const LABEL_CLASS: Record<string, string> = {
  [NOVEL]: "new",
  [EXTENDS]: "ext",
  [TENSION]: "con",
  [ESTABLISHED]: "conf",
}
export const READINESS = ["data in the lakehouse", "needs compute", "needs new measurements", "unknown"]
const READY_CLASS = ["", "part", "lab", "no"]
// Large topics should not win the sort by size alone.
const PROJECT_CAP = 5

const fmOf = <T,>(f: File) => (f.frontmatter ?? {}) as T
export const isNull = (f: File) => ["null result", "correction"].includes(fmOf<FindingFm>(f).result ?? "")
const labelOf = (f: File) => fmOf<FindingFm>(f).label ?? NOT_ASSESSED

export function findingsOf(c: Corpus): File[] {
  return [...c.bySlug.values()].filter((f) => collectionOf(slugOf(f)) === "findings" && !isIndex(slugOf(f)))
}

export function directionsOf(c: Corpus): File[] {
  return [...c.bySlug.values()].filter((f) => collectionOf(slugOf(f)) === "directions" && !isIndex(slugOf(f)))
}

const rank = (f: File) => {
  const i = LABEL_ORDER.indexOf(labelOf(f))
  return i < 0 ? LABEL_ORDER.length : i
}

export const byLabel = (a: File, b: File) =>
  rank(a) - rank(b) || (fmOf<FindingFm>(b).first_added ?? "").localeCompare(fmOf<FindingFm>(a).first_added ?? "") || slugOf(a).localeCompare(slugOf(b))

/** Four home cards, at least one a null result or correction when any exists.
 *  Established results stay on topic pages: the home page is for what is new. */
export function homeFindings(c: Corpus, n = 4): File[] {
  const pool = findingsOf(c)
    .filter((f) => labelOf(f) !== ESTABLISHED)
    .sort(byLabel)
  const pick = pool.slice(0, n)
  const firstNull = pool.find(isNull)
  if (firstNull && !pick.some(isNull)) pick[Math.min(n, pick.length) - 1] = firstNull
  return pick
}

function buildsOn(f: File) {
  const refs = fmOf<DirectionFm>(f).builds_on ?? []
  return {
    findings: refs.filter((r) => r.startsWith("findings/")).length,
    conflicts: refs.filter((r) => r.startsWith("conflicts/")).length,
  }
}

/** Readiness, then what the direction builds on, then projects touched (capped). No score. */
export const byReadiness = (a: File, b: File) => {
  const ra = READINESS.indexOf(fmOf<DirectionFm>(a).readiness ?? "unknown")
  const rb = READINESS.indexOf(fmOf<DirectionFm>(b).readiness ?? "unknown")
  const ma = buildsOn(a)
  const mb = buildsOn(b)
  const pa = Math.min(PROJECT_CAP, (fmOf<DirectionFm>(a).projects ?? []).length)
  const pb = Math.min(PROJECT_CAP, (fmOf<DirectionFm>(b).projects ?? []).length)
  return ra - rb || mb.findings + mb.conflicts - (ma.findings + ma.conflicts) || pb - pa || titleOf(a).localeCompare(titleOf(b))
}

export function LabelChip({ label }: { label: string }) {
  return <span class={`v ${LABEL_CLASS[label] ?? "ins"}`}>{label}</span>
}

// The value already shows its unit, as "28.7%" does for "percent" (stages/headlines.py).
const carriesUnit = ({ value, unit }: Quantity) => {
  const u = (unit ?? "").trim().toLowerCase()
  return !u || value.endsWith(u) || (value.includes("%") && (u === "%" || u === "percent"))
}

const plural = (n: number, one: string, many = `${one}s`) => `${n} ${n === 1 ? one : many}`
const searchText = (...parts: (string | undefined)[]) => parts.filter(Boolean).join(" ").toLowerCase()

export function FindingCard({ f, from }: { f: File; from: FullSlug }) {
  const m = fmOf<FindingFm>(f)
  const label = labelOf(f)
  const q = (m.quantities ?? []).slice(0, 2)
  return (
    <article
      class="fcard"
      data-topics={(m.topics ?? []).join(" ")}
      data-label={label}
      data-null={isNull(f) ? "1" : undefined}
      data-text={searchText(titleOf(f), m.description, m.caveat, m.source)}
    >
      <div class="tags">
        <span class={`rt${isNull(f) ? " null" : ""}`}>{m.result}</span>
        <LabelChip label={label} />
      </div>
      <h3>
        <a href={resolveRelative(from, slugOf(f) as FullSlug)}>{titleOf(f)}</a>
      </h3>
      <p>{m.description}</p>
      {q.length > 0 && (
        <p class="figs">
          {q.map((x) => (
            <span>
              <span class="num">
                {x.value}
                {carriesUnit(x) ? "" : ` ${x.unit}`}
              </span>{" "}
              {x.what}
            </span>
          ))}
        </p>
      )}
      {m.caveat && (
        <p class="cav">
          <b>Caveat.</b> {m.caveat}
        </p>
      )}
      <div class="meta">
        {m.source && (
          <span>
            From <a href={resolveRelative(from, `summaries/${m.source}` as FullSlug)}>{m.source}</a>
          </span>
        )}
        <span>{m.label_date ? `PubMed abstracts checked ${m.label_date}` : "Literature not yet checked"}</span>
      </div>
    </article>
  )
}

export function DirectionCard({ f, from }: { f: File; from: FullSlug }) {
  const m = fmOf<DirectionFm>(f)
  const r = READINESS.indexOf(m.readiness ?? "unknown")
  const moved = buildsOn(f)
  return (
    <article
      class="ncard"
      data-topics={(m.topics ?? []).join(" ")}
      data-approach={m.approach}
      data-readiness={m.readiness}
      data-text={searchText(titleOf(f), m.description, m.hypothesis, m.approach, ...(m.collections ?? []))}
    >
      <div class="top">
        <span class="c-kind">{m.approach}</span>
        <span class={`ready ${READY_CLASS[r < 0 ? 3 : r]}`}>{m.readiness}</span>
      </div>
      <h3>
        <a href={resolveRelative(from, slugOf(f) as FullSlug)}>{titleOf(f)}</a>
      </h3>
      <p>{m.description}</p>
      {m.hypothesis && (
        <p class="hyp">
          <b>Hypothesis.</b> {m.hypothesis}
        </p>
      )}
      <div class="sig">
        {(m.collections ?? []).map((c) => (
          <span class="ds">{c}</span>
        ))}
        <span>
          Builds on {plural(moved.findings, "finding")}, {plural(moved.conflicts, "conflict")}
        </span>
      </div>
    </article>
  )
}

/** Chips that filter the cards beside them in the browser; without JavaScript all cards show. */
export function FilterChips({ group, options }: { group: string; options: [string, string][] }) {
  return (
    <div class="c-chips" data-filter-group={group} role="group">
      <button class="c-chip on" type="button" data-value="">
        All
      </button>
      {options.map(([value, label]) => (
        <button class="c-chip" type="button" data-value={value}>
          {label}
        </button>
      ))}
    </div>
  )
}

const LABEL_FILTERS: [string, string][] = [
  [NOVEL, "Candidate novel"],
  [EXTENDS, "Extends"],
  [TENSION, "In tension"],
  ["null", "Nulls and corrections"],
]

function topicOptions(c: Corpus, files: File[]): [string, string][] {
  const used = new Set(files.flatMap((f) => fmOf<FindingFm>(f).topics ?? []))
  return c.topics
    .map((t) => [slugOf(t).replace(/^topics\//, ""), titleOf(t)] as [string, string])
    .filter(([s]) => used.has(s))
}

/** The findings collection page: every finding, filterable by label and topic. */
export function FindingBoard({ c, from }: { c: Corpus; from: FullSlug }) {
  const all = findingsOf(c).sort(byLabel)
  return (
    <section class="cards-board" data-cards>
      <FilterChips group="label" options={LABEL_FILTERS} />
      <FilterChips group="topic" options={topicOptions(c, all)} />
      <div class="grid2">
        {all.map((f) => (
          <FindingCard f={f} from={from} />
        ))}
      </div>
    </section>
  )
}

/** The research-directions collection page: facets by readiness, approach and topic. */
export function DirectionBoard({ c, from }: { c: Corpus; from: FullSlug }) {
  const all = directionsOf(c).sort(byReadiness)
  const approaches = [...new Set(all.map((f) => fmOf<DirectionFm>(f).approach ?? ""))].filter(Boolean).sort()
  const count = (key: keyof DirectionFm, value: string) => all.filter((f) => fmOf<DirectionFm>(f)[key] === value).length
  return (
    <section class="cards-board" data-cards>
      <FilterChips
        group="readiness"
        options={READINESS.filter((r) => count("readiness", r) > 0).map((r) => [r, `${r} (${count("readiness", r)})`])}
      />
      <FilterChips group="approach" options={approaches.map((k) => [k, `${k} (${count("approach", k)})`])} />
      <FilterChips group="topic" options={topicOptions(c, all)} />
      <p class="sortline">
        Sorted by readiness, then by the findings and conflicts each direction builds on, then by projects touched
        (counted up to {PROJECT_CAP}). There is no score.
      </p>
      <div class="stack">
        {all.map((f) => (
          <DirectionCard f={f} from={from} />
        ))}
      </div>
    </section>
  )
}

/** "New here" and "Research directions" on a topic hub, above its synthesis. */
export function TopicCards({ file, c }: { file: File; c: Corpus }) {
  const from = slugOf(file) as FullSlug
  const topic = slugOf(file).replace(/^topics\//, "")
  const mine = <T extends { topics?: string[] }>(f: File) => (fmOf<T>(f).topics ?? []).includes(topic)
  const findings = findingsOf(c).filter(mine<FindingFm>).sort(byLabel)
  const directions = directionsOf(c).filter(mine<DirectionFm>).sort(byReadiness)
  if (findings.length === 0 && directions.length === 0) return null
  return (
    <div class="topic-cards">
      {findings.length > 0 && (
        <section>
          <div class="sechead">
            <h2>New here</h2>
            <p>
              {plural(findings.length, "headline finding")} from this topic's reports, each with its caveat and a literature
              label. <a href={resolveRelative(from, "findings/index" as FullSlug)}>All findings</a>
            </p>
          </div>
          <div class="grid2">
            {findings.slice(0, 4).map((f) => (
              <FindingCard f={f} from={from} />
            ))}
          </div>
        </section>
      )}
      {directions.length > 0 && (
        <section>
          <div class="sechead">
            <h2>Research directions</h2>
            <p>
              {plural(directions.length, "question")} this topic's findings and conflicts open.{" "}
              <a href={resolveRelative(from, "directions/index" as FullSlug)}>All research directions</a>
            </p>
          </div>
          <div class="stack">
            {directions.slice(0, 3).map((f) => (
              <DirectionCard f={f} from={from} />
            ))}
          </div>
        </section>
      )}
      <div class="sechead background-head">
        <h2>Background</h2>
        <p>The topic synthesis, its literature context and the concepts it gathers.</p>
      </div>
    </div>
  )
}

/** Under a finding's or research direction's title: what kind of record it is, and its handoffs. */
export function RecordBar({ file }: { file: File }) {
  const slug = slugOf(file)
  if (collectionOf(slug) === "findings") {
    const m = fmOf<FindingFm>(file)
    return (
      <div class="cardbar">
        <span class={`rt${isNull(file) ? " null" : ""}`}>{m.result}</span>
        <LabelChip label={labelOf(file)} />
        {m.label_date && <span class="when">Pipeline judgment against PubMed abstracts retrieved {m.label_date}</span>}
      </div>
    )
  }
  const m = fmOf<DirectionFm>(file)
  const r = READINESS.indexOf(m.readiness ?? "unknown")
  return (
    <div class="cardbar">
      <span class="c-kind">{m.approach}</span>
      <span class={`ready ${READY_CLASS[r < 0 ? 3 : r]}`}>{m.readiness}</span>
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

/** The home page's planner: filter the cards here, or plan with Ask. */
export function Planner({ c, from }: { c: Corpus; from: FullSlug }) {
  const topics = topicOptions(c, [...findingsOf(c), ...directionsOf(c)])
  return (
    <div class="planner" data-planner data-ask={resolveRelative(from, "ask" as FullSlug)}>
      <label class="lbl" for="px-interest">
        Plan your next project
      </label>
      <div class="row">
        <input
          id="px-interest"
          class="field"
          type="search"
          placeholder="An interest: a gene family, an organism, a method"
          autocomplete="off"
        />
        <button class="btn px-plan" type="button">
          Plan my next project
        </button>
      </div>
      {topics.length > 0 && (
        <div class="c-chips" data-filter-group="topic" role="group">
          <button class="c-chip on" type="button" data-value="">
            All topics
          </button>
          {topics.map(([s, t]) => (
            <button class="c-chip" type="button" data-value={s}>
              {t}
            </button>
          ))}
        </div>
      )}
      <p class="hint">
        Typing filters the cards on this page. <b>Plan my next project</b> asks the wiki, with your CBORG key, for three
        research directions drawn only from findings, research directions and conflicts.
      </p>
    </div>
  )
}
