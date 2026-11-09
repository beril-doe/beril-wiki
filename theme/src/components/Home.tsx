// The home page: the opening with the corpus in figures; then, when finding records are
// published, Highlights (the topic-strip key, three results and three questions, each with
// a topic strip); then Find your way in, the map of the corpus, and the topic table.
import type { FullSlug } from "@quartz-community/types"
import { resolveRelative } from "@quartz-community/utils"
import type { ElementContent, Root } from "hast"
import { jsx } from "../jsx"
import { CorpusMap, mapStats } from "../map"
import { type Corpus, type File, counts, sections, slugOf, titleOf, topicBlurbs } from "../page"
import { FindingCard, type FindingFm, directionsOf, findingsOf, resultsIndex } from "./Cards"
import { CrossQuestions } from "./Questions"
import { TopicKey } from "./Strip"
import { Topics } from "./Topics"

function SubHead({ title, deck }: { title: string; deck?: string }) {
  return (
    <div class="sechead sub">
      <h3>{title}</h3>
      {deck && <p>{deck}</p>}
    </div>
  )
}

function SecHead({ title, deck }: { title: string; deck?: string }) {
  return (
    <div class="sechead">
      <h2>{title}</h2>
      {deck && <p>{deck}</p>}
    </div>
  )
}

export function Home({ file, c, tree, standing }: { file: File; c: Corpus; tree: Root; standing: ElementContent[] | null }) {
  const slug = slugOf(file) as FullSlug
  const { intro, byHeading } = sections(tree)
  const firstPara = intro.findIndex((n) => n.type === "element" && n.tagName === "p")
  const lead = firstPara >= 0 ? [intro[firstPara]] : intro
  const after = firstPara >= 0 ? intro.filter((_, i) => i !== firstPara) : []
  const browse = byHeading.get("browse")
  const blurbs = topicBlurbs(byHeading.get("topics"))
  const n = counts(c)
  const stats = mapStats(c)
  const findings = findingsOf(c)
  const published = findings.length > 0
  const questions = directionsOf(c).length
  const rankOf = (f: File) => (f.frontmatter as { home_rank?: number } | undefined)?.home_rank
  const picks = findings
    .filter((f) => rankOf(f) !== undefined)
    .sort((a, b) => rankOf(a)! - rankOf(b)!)
    .slice(0, 3)
  const unmatched = resultsIndex(c).compare_order?.[0]
  const picksDeck =
    picks.length > 0 && picks.every((f) => (f.frontmatter as FindingFm | undefined)?.compare_text === unmatched)
      ? "New results from different topics."
      : "Results from different topics with the least published work like them."
  const kinds = [
    ["topics/index", "Topics", "What the corpus says about one research area. Start here if you are new to an area.", `${n.topics} topics`],
    ["concepts/index", "Concepts", "What several projects together show about one claim, and where they disagree.", `${n.concepts} concepts`],
    ["entities/index", "Entities", "Everything recorded about one organism, gene, compound, method or dataset.", `${n.entities} entities`],
    ["conflicts/index", "Conflicts", "Where projects disagree, the evidence on each side, and what would settle it.", `${n.conflicts} conflicts`],
    ["summaries/index", "Reports", "What one project did and found, with exact numbers to cite.", `${n.reports} reports, ${n.digests} digests`],
  ] as [string, string, string, string][]
  if (published)
    kinds.push(
      ["findings/index", "Results", "What single projects measured or found missing, in plain words.", `${findings.length} results`],
      ["directions/index", "Open questions", "Questions the results leave open, by topic and by what answering them needs.", `${questions} questions`],
    )
  return (
    <>
      {/* The introduction keeps one honest measure on the left; the corpus,
          in figures, fills the right instead of a second column of prose. The
          figures start level with the first paragraph, not with the title. */}
      <section class="band hero">
        <h1>{titleOf(file)}</h1>
        {standing && <p class="standing">{jsx(standing)}</p>}
        <div class="lede">
          <div class="lead">{jsx(lead)}</div>
          {after.length > 0 && <div class="after">{jsx(after)}</div>}
        </div>
        {/* src/client opens section search from this box. */}
        <div class="homesearch">
          <button class="bigsearch px-bigsearch" type="button">
            <svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true">
              <circle cx="8.5" cy="8.5" r="6.5" />
              <path d="M13.5 13.5 18 18" />
            </svg>
            <span>Search every section: a gene, an organism, a method, a claim</span>
            <kbd>/</kbd>
          </button>
          <a class="btn" href={resolveRelative(slug, "ask" as FullSlug)}>
            Ask the wiki
          </a>
        </div>
        <dl class="figures" aria-label="The corpus in figures">
          <p class="lbl">The corpus</p>
          {(
            [
              [n.reports, "Project reports", "the primary evidence", "summaries/index"],
              [n.digests, "Cross-project digests", "discoveries and pitfalls", "summaries/index"],
              [n.concepts, "Concepts", "synthesised across them", "concepts/index"],
              [n.entities, "Entities", "organisms, genes, datasets, methods", "entities/index"],
              [n.conflicts, "Recorded conflicts", "with the evidence on both sides", "conflicts/index"],
              [n.topics, "Topics", "gathering the rest", "topics/index"],
            ] as [number, string, string, string][]
          ).map(([value, label, tail, target]) => (
            <div class="frow">
              <dt>{value}</dt>
              <dd>
                <a href={resolveRelative(slug, target as FullSlug)}>{label}</a> {tail}
              </dd>
            </div>
          ))}
        </dl>
      </section>
      {/* Highlights come right after the opening, so a reader meets what the projects
          found before the reference sections; every section of the page stays. */}
      {published && (
        <section class="band highlights" aria-label="Highlights">
          <SecHead title="Highlights" deck="Three results from different topics and three questions that join projects." />
          <TopicKey c={c} from={slug} blurbs={blurbs} />
          <div class="hlpart" data-cards data-tstrips aria-label="What the projects found">
            <SubHead title="What the projects found" deck={picksDeck} />
            {picks.length > 0 && (
              <div class="grid2 grid3">
                {picks.map((f) => (
                  <FindingCard f={f} from={slug} c={c} strip />
                ))}
              </div>
            )}
            <p class="c-more">
              <a href={resolveRelative(slug, "findings/index" as FullSlug)}>All {findings.length} results</a>
            </p>
          </div>
          <div class="hlpart" data-tstrips aria-label="Questions still open">
            <SubHead title="Questions still open" deck="Questions that draw on results from more than one project." />
            <CrossQuestions c={c} from={slug} />
            <p class="c-more">
              <a href={resolveRelative(slug, "directions/index" as FullSlug)}>All {questions} questions</a>
            </p>
          </div>
        </section>
      )}
      {/* Each kind of page answers a different question; the cards say which. */}
      <section class="band">
        <SecHead title="Find your way in" />
        <nav class="kinds" aria-label="Kinds of page">
          {kinds.map(([target, label, what, count]) => (
            <a class="kindcard" href={resolveRelative(slug, target as FullSlug)}>
              <b>{label}</b>
              <span>{what}</span>
              <span class="n">{count}</span>
            </a>
          ))}
        </nav>
        {browse && (
          <nav class="browse also" aria-label="Also">
            {jsx(browse)}
          </nav>
        )}
      </section>
      <section class="band" aria-label="Map of the corpus">
        <SecHead
          title="The map"
          deck={`The ${stats.topics} topics and the ${stats.concepts} concepts they gather. Click a point to open its page.`}
        />
        {/* src/client/strips.ts lights the picked topic's cluster here. */}
        <div class="mapframe" id="home-map" data-tmap>
          <CorpusMap c={c} from={slug} />
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
            {stats.crossings} wikilinks cross between topics, summed into one line per pair
          </span>
          <span class="key">Hover a concept for its own links, a topic for everything leaving it.</span>
          {published && (
            <span class="key">The colours are the same topics as the strips on the results and questions above.</span>
          )}
        </div>
      </section>
      <section class="band" aria-label="Topics">
        <SecHead title="Topics" />
        <Topics c={c} from={slug} blurbs={blurbs} />
      </section>
    </>
  )
}
