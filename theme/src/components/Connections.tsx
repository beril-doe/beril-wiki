// The results and open questions tied to a topic hub, a project report or a concept page,
// in one card style. A topic owns the results and questions filed under it; a report owns
// its project's results and the questions that build on the project; a concept reaches them
// through the project reports it cites. Every word comes from publish/cards.py's frontmatter.
import type { FullSlug } from "@quartz-community/types"
import type { JSX } from "preact"
import { resolveRelative } from "@quartz-community/utils"
import { type Corpus, type File, collectionOf, isReport, linksOf, slugOf, titleOf } from "../page"
import { type DirectionFm, type FindingFm, FindingCard, FollowTags, directionsOf, findingsOf, resultsIndex } from "./Cards"
import { NOVEL_WORDS, citesNovel } from "./Questions"

interface QuestionFm extends DirectionFm {
  readiness_basis?: string
  projects?: string[]
}

const fmOf = <T,>(f: File) => (f.frontmatter ?? {}) as T
const sidOf = (slug: string) => slug.replace(/^summaries\//, "")

/** An open question in the result card's look: kind, title, what answering it needs. */
export function QuestionCard({ q, c, from }: { q: File; c: Corpus; from: FullSlug }) {
  const m = fmOf<QuestionFm>(q)
  return (
    <article class="fcard qfcard" data-topic={m.topic}>
      <div class="tags">
        <span class="rt">Open question</span>
      </div>
      <h3>
        <a href={resolveRelative(from, slugOf(q) as FullSlug)}>{titleOf(q)}</a>
      </h3>
      {m.readiness_basis && <p class="gist">{m.readiness_basis}</p>}
      {citesNovel(c, q) && <p class="qfnovel">{NOVEL_WORDS}</p>}
      <div class="meta qfmeta">
        <FollowTags m={m} />
      </div>
    </article>
  )
}

/** Cards for the first few, and a folded list of the rest so nothing is out of reach. An
 * empty part keeps its head and says so, so every page of a kind has the same sections. */
function Part({ title, deck, more, items, card, empty }: {
  title: string
  deck?: string
  more?: { href: string; text: string }
  items: { file: File; href: string }[]
  card: (f: File) => JSX.Element
  empty: string
}) {
  const shown = 3
  if (items.length === 0) {
    return (
      <section>
        <div class="sechead">
          <h2>{title}</h2>
        </div>
        <p class="part-empty">{empty}</p>
      </section>
    )
  }
  const first = items.slice(0, shown)
  const rest = items.slice(shown)
  return (
    <section>
      <div class="sechead">
        <h2>{title}</h2>
        {(deck || more) && (
          <p>
            {deck}
            {deck && more && " "}
            {more && <a href={more.href}>{more.text}</a>}
          </p>
        )}
      </div>
      <div class="grid2">{first.map(({ file }) => card(file))}</div>
      {rest.length > 0 && (
        <details class="linkmore">
          <summary>{rest.length} more</summary>
          <ul>
            {rest.map(({ file, href }) => (
              <li>
                <a href={href}>{titleOf(file)}</a>
              </li>
            ))}
          </ul>
        </details>
      )}
    </section>
  )
}

/** The results and questions for one topic, report or concept page, before its prose. */
export function Connections({ file, c }: { file: File; c: Corpus }) {
  const slug = slugOf(file)
  const kind = collectionOf(slug)
  const from = slug as FullSlug
  const order = resultsIndex(c).compare_order ?? []
  const novelFirst = (a: File, b: File) =>
    order.indexOf(fmOf<FindingFm>(a).compare_text ?? "") - order.indexOf(fmOf<FindingFm>(b).compare_text ?? "") ||
    titleOf(a).localeCompare(titleOf(b))
  const link = (f: File) => ({ file: f, href: resolveRelative(from, slugOf(f) as FullSlug) })
  const resultCard = (f: File) => <FindingCard f={f} from={from} c={c} />
  const questionCard = (q: File) => <QuestionCard q={q} c={c} from={from} />
  const board = (target: string, topic: string) => `${resolveRelative(from, `${target}/index` as FullSlug)}?topic=${encodeURIComponent(topic)}`

  if (kind === "topics") {
    const topic = slug.replace(/^topics\//, "")
    const rankOf = (f: File) => fmOf<FindingFm>(f).topic_ranks?.[topic]
    const inTopic = findingsOf(c).filter((f) => fmOf<FindingFm>(f).topic === topic)
    const col = (f: File) => order.indexOf(fmOf<FindingFm>(f).compare_text ?? "")
    // Ties break on the slug by code point, so scripts/check_reader.py can predict the order.
    const ranked = (a: File, b: File) =>
      (rankOf(a) ?? Infinity) - (rankOf(b) ?? Infinity) ||
      col(a) - col(b) ||
      (slugOf(a) < slugOf(b) ? -1 : slugOf(a) > slugOf(b) ? 1 : 0)
    // The cards come from the results filed under this topic, so the link below them shows
    // every card again; a topic with none of its own shows the results that touch it.
    const picks = (inTopic.length > 0 ? [...inTopic] : findingsOf(c).filter((f) => rankOf(f) !== undefined))
      .sort(ranked)
      .slice(0, 3)
    const questions = directionsOf(c)
      .filter((q) => fmOf<QuestionFm>(q).topic === topic)
      .sort((a, b) => titleOf(a).localeCompare(titleOf(b)))
    return (
      <div class="topic-cards">
        <Part
          title="Results from this topic"
          // With no result filed under the topic, the board has nothing to filter to.
          more={inTopic.length > 0 ? { href: board("findings", topic), text: `All ${inTopic.length} results in this topic` } : undefined}
          items={picks.map(link)}
          card={resultCard}
          empty="No result is filed under this topic yet."
        />
        <Part
          title="Open questions in this topic"
          more={questions.length > 0 ? { href: board("directions", topic), text: `All ${questions.length} in the open questions` } : undefined}
          items={questions.map(link)}
          card={questionCard}
          empty="No open question is filed under this topic yet."
        />
        <div class="sechead background-head">
          <h2>Background</h2>
          <p>The topic synthesis, its literature context and the concepts it gathers.</p>
        </div>
      </div>
    )
  }

  // A cross-project archive is its own kind of page: no project, so no project results.
  if (kind === "summaries" && isReport(file)) {
    const sid = sidOf(slug)
    const results = findingsOf(c)
      .filter((f) => fmOf<FindingFm>(f).source === sid)
      .sort(novelFirst)
    const questions = directionsOf(c)
      .filter((q) => (fmOf<QuestionFm>(q).projects ?? []).includes(sid))
      .sort((a, b) => titleOf(a).localeCompare(titleOf(b)))
    return (
      <div class="topic-cards">
        <Part
          title="Results from this project"
          deck="What the project found, in plain words."
          items={results.map(link)}
          card={resultCard}
          empty="This project has no listed result yet."
        />
        <Part
          title="Open questions that build on this project"
          items={questions.map(link)}
          card={questionCard}
          empty="No open question builds on this project yet."
        />
        <div class="sechead background-head">
          <h2>The report</h2>
          <p>A summary of the project's report, with its numbers and limits.</p>
        </div>
      </div>
    )
  }

  if (kind === "concepts") {
    // An archive is cited like a report but is not one, so it brings no project with it.
    const isCitedReport = (l: string) => {
      const target = c.bySlug.get(l)
      return collectionOf(l) === "summaries" && !!target && isReport(target)
    }
    const sids = new Set(linksOf(file).filter(isCitedReport).map(sidOf))
    const topic = c.topicsOf(file)[0]
    const topicSlug = topic ? slugOf(topic).replace(/^topics\//, "") : ""
    const sorted = findingsOf(c)
      .filter((f) => sids.has(fmOf<FindingFm>(f).source ?? ""))
      .sort((a, b) => Number(fmOf<FindingFm>(b).topic === topicSlug) - Number(fmOf<FindingFm>(a).topic === topicSlug) || novelFirst(a, b))
    // One project at a time, so the first cards come from different projects.
    const byProject = new Map<string, File[]>()
    for (const f of sorted) {
      const sid = fmOf<FindingFm>(f).source ?? ""
      byProject.set(sid, [...(byProject.get(sid) ?? []), f])
    }
    const lanes = [...byProject.values()]
    const results: File[] = []
    for (let i = 0; results.length < sorted.length; i++) for (const lane of lanes) if (lane[i]) results.push(lane[i])
    const overlap = (q: File) => (fmOf<QuestionFm>(q).projects ?? []).filter((p) => sids.has(p)).length
    const questions = directionsOf(c)
      .filter((q) => overlap(q) > 0)
      .sort((a, b) => overlap(b) - overlap(a) || titleOf(a).localeCompare(titleOf(b)))
    return (
      <div class="topic-cards">
        <Part
          title="Results from the projects this page cites"
          items={results.map(link)}
          card={resultCard}
          empty={sids.size > 0 ? "The reports this page cites have no listed result yet." : "This page cites no report yet."}
        />
        <Part
          title="Open questions on these projects"
          items={questions.map(link)}
          card={questionCard}
          empty={sids.size > 0 ? "No open question builds on these projects yet." : "This page cites no report yet."}
        />
        <div class="sechead background-head">
          <h2>Background</h2>
          <p>What the cited reports say about this concept.</p>
        </div>
      </div>
    )
  }
  return null
}

/** On a result or open-question page: the concept pages that cite its project reports. */
export function ConceptLinks({ file, c }: { file: File; c: Corpus }) {
  const slug = slugOf(file)
  const kind = collectionOf(slug)
  const m = fmOf<FindingFm & QuestionFm>(file)
  const sids = new Set(kind === "findings" ? [m.source ?? ""] : kind === "directions" ? (m.projects ?? []) : [])
  sids.delete("")
  if (sids.size === 0) return null
  const cited = (f: File) => linksOf(f).filter((l) => collectionOf(l) === "summaries" && sids.has(sidOf(l))).length
  const concepts = [...c.bySlug.values()]
    .filter((f) => collectionOf(slugOf(f)) === "concepts" && !slugOf(f).endsWith("/index") && cited(f) > 0)
    .sort((a, b) => cited(b) - cited(a) || titleOf(a).localeCompare(titleOf(b)))
  if (concepts.length === 0) return null
  const item = (f: File) => (
    <li>
      <a href={resolveRelative(slug as FullSlug, slugOf(f) as FullSlug)}>{titleOf(f)}</a>
    </li>
  )
  // The concepts citing the project most come first; the rest fold away.
  const shown = 6
  return (
    <section class="conceptlinks">
      <h2>{kind === "findings" ? "Concepts that cite this project" : "Concepts that cite these projects"}</h2>
      <ul>{concepts.slice(0, shown).map(item)}</ul>
      {concepts.length > shown && (
        <details class="linkmore">
          <summary>{concepts.length - shown} more</summary>
          <ul>{concepts.slice(shown).map(item)}</ul>
        </details>
      )}
    </section>
  )
}
