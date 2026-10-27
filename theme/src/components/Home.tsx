// The home page swaps the record for the corpus in figures, a map of it, and
// the topic table. When finding records are published (a preview build), it
// leads with findings, research directions and conflicts, and the corpus in
// figures, the page kinds and the map move under Background.
import type { FullSlug } from "@quartz-community/types"
import { resolveRelative } from "@quartz-community/utils"
import type { ElementContent, Root } from "hast"
import { jsx } from "../jsx"
import { CorpusMap, mapStats } from "../map"
import { type Corpus, type File, counts, sections, slugOf, titleOf, topicBlurbs } from "../page"
import {
  EXTENDS,
  FilterChips,
  DirectionCard,
  FindingCard,
  NOT_ASSESSED,
  NOVEL,
  Planner,
  TENSION,
  byReadiness,
  findingsOf,
  homeFindings,
  isNull,
  directionsOf,
} from "./Cards"
import { Topics } from "./Topics"

function SecHead({ title, deck }: { title: string; deck: string }) {
  return (
    <div class="sechead">
      <h2>{title}</h2>
      <p>{deck}</p>
    </div>
  )
}

export function Home({ file, c, tree, standing }: { file: File; c: Corpus; tree: Root; standing: ElementContent[] | null }) {
  const slug = slugOf(file) as FullSlug
  const blurbs = topicBlurbs(sections(tree).byHeading.get("topics"))
  if (findingsOf(c).length > 0) {
    return (
      <Discovery c={c} slug={slug} blurbs={blurbs}>
        <Classic file={file} c={c} tree={tree} standing={standing} />
      </Discovery>
    )
  }
  return <Classic file={file} c={c} tree={tree} standing={standing} />
}

function Classic({ file, c, tree, standing }: { file: File; c: Corpus; tree: Root; standing: ElementContent[] | null }) {
  const slug = slugOf(file) as FullSlug
  const { intro, byHeading } = sections(tree)
  const firstPara = intro.findIndex((n) => n.type === "element" && n.tagName === "p")
  const lead = firstPara >= 0 ? [intro[firstPara]] : intro
  const after = firstPara >= 0 ? intro.filter((_, i) => i !== firstPara) : []
  const browse = byHeading.get("browse")
  const blurbs = topicBlurbs(byHeading.get("topics"))
  const n = counts(c)
  const stats = mapStats(c)
  const discovery = findingsOf(c).length > 0
  return (
    <>
      {/* The introduction keeps one honest measure on the left; the corpus,
          in figures, fills the right instead of a second column of prose. The
          figures start level with the first paragraph, not with the title. */}
      <section class="band hero">
        {/* Under the discovery layout this is a section of the page, not its title. */}
        {discovery ? <h2 class="hero-title">{titleOf(file)}</h2> : <h1>{titleOf(file)}</h1>}
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
          <p class="note">Every figure counts pages on this site, not a claim about the field.</p>
        </dl>
      </section>
      {/* Each kind of page answers a different question; the cards say which. */}
      <section class="band">
        <SecHead title="Find your way in" deck="Each kind of page answers a different question. Pick the one that matches yours." />
        <nav class="kinds" aria-label="Kinds of page">
          {(
            [
              ["topics/index", "Topics", "What the corpus says about one research area. Start here if you are new to an area.", `${n.topics} topics`],
              ["concepts/index", "Concepts", "What several projects together show about one claim, and where they disagree.", `${n.concepts} concepts`],
              ["entities/index", "Entities", "Everything recorded about one organism, gene, compound, method or dataset.", `${n.entities} entities`],
              ["conflicts/index", "Conflicts", "Where projects disagree, the evidence on each side, and what would settle it.", `${n.conflicts} conflicts`],
              ["summaries/index", "Reports", "What one project did and found, with exact numbers to cite.", `${n.reports} reports, ${n.digests} digests`],
            ] as [string, string, string, string][]
          ).map(([target, label, what, count]) => (
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
          deck={`Each of the ${stats.topics} topics sits at the middle of the concepts that belong to it, ${stats.concepts} in all, sized by how linked each one is. Click any point to open the page.`}
        />
        <div class="mapframe">
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
        </div>
      </section>
      {!discovery && (
        <section class="band" aria-label="Topics">
          <SecHead title="Topics" deck="What each hub covers, and how much evidence stands behind it." />
          <Topics c={c} from={slug} blurbs={blurbs} />
        </section>
      )}
    </>
  )
}

function Discovery({ c, slug, blurbs, children }: {
  c: Corpus
  slug: FullSlug
  blurbs: Map<string, ElementContent[]>
  children: preact.ComponentChildren
}) {
  const findings = findingsOf(c)
  const directions = directionsOf(c).sort(byReadiness)
  const labelOf = (f: File) => (f.frontmatter as { label?: string })?.label ?? NOT_ASSESSED
  const label = (l: string) => findings.filter((f) => labelOf(f) === l).length
  const checked = findings.length - label(NOT_ASSESSED)
  // Conflicts the most research directions build on come first; the count is the reason shown.
  const settling = new Map<string, number>()
  for (const s of directions)
    for (const ref of ((s.frontmatter as { builds_on?: string[] })?.builds_on ?? []).filter((r) => r.startsWith("conflicts/")))
      settling.set(ref, (settling.get(ref) ?? 0) + 1)
  const conflicts = [...settling.entries()]
    .sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]))
    .slice(0, 3)
    .map(([ref, n]) => [c.bySlug.get(ref), n] as const)
    .filter(([f]) => f)
  const scope = [...new Set(directions.flatMap((s) => (s.frontmatter as { topics?: string[] })?.topics ?? []))]
    .map((t) => c.bySlug.get(`topics/${t}`))
    .filter((t): t is File => !!t)
    .map(titleOf)
  return (
    <>
      <section class="band discovery-hero">
        <h1>What BERIL found, and what you could do next</h1>
        <p class="lead">
          Headline findings from the project reports, each with its caveat and a label saying where it sits against
          published work; the next analyses the corpus proposes; and the disagreements worth settling. Every label is a
          pipeline judgment against PubMed abstracts, not a reviewed verdict.
        </p>
        {scope.length > 0 && (
          <p class="preview-note">
            Preview: findings and research directions cover {scope.join(", ")} so far. Other topics still have their full pages
            under Background.
          </p>
        )}
        <Planner c={c} from={slug} />
        <dl class="strip" aria-label="Findings in figures">
          {(
            [
              [checked, "findings checked against PubMed", "findings/index"],
              [label(NOVEL), "candidate novel", "findings/index"],
              [label(EXTENDS), "extend retrieved work", "findings/index"],
              [label(TENSION), "in tension with it", "findings/index"],
              [findings.filter(isNull).length, "null results and corrections", "findings/index"],
              [c.conflicts.length, "recorded conflicts", "conflicts/index"],
            ] as [number, string, string][]
          ).map(([value, text, target]) => (
            <div>
              <dt>{value}</dt>
              <dd>
                <a href={resolveRelative(slug, target as FullSlug)}>{text}</a>
              </dd>
            </div>
          ))}
        </dl>
      </section>
      <section class="band" data-cards>
        <SecHead
          title="Findings that change the picture"
          deck="Results published work does not already report come first. At least one card is a null result or a correction when the corpus has one."
        />
        <FilterChips
          group="label"
          options={[
            [NOVEL, "Candidate novel"],
            [EXTENDS, "Extends"],
            [TENSION, "In tension"],
            ["null", "Nulls and corrections"],
          ]}
        />
        <div class="grid2">
          {homeFindings(c).map((f) => (
            <FindingCard f={f} from={slug} />
          ))}
        </div>
        <p class="c-more">
          <a href={resolveRelative(slug, "findings/index" as FullSlug)}>All {findings.length} findings</a>
        </p>
      </section>
      {directions.length > 0 && (
        <section class="band" data-cards>
          <SecHead
            title="Research directions"
            deck="Questions the findings and conflicts open, each with a hypothesis and the test that would settle it. There is no score."
          />
          <div class="stack">
            {directions.slice(0, 3).map((f) => (
              <DirectionCard f={f} from={slug} />
            ))}
          </div>
          <p class="c-more">
            <a href={resolveRelative(slug, "directions/index" as FullSlug)}>All {directions.length} research directions</a>
          </p>
        </section>
      )}
      {conflicts.length > 0 && (
        <section class="band">
          <SecHead title="Open conflicts worth settling" deck="Where projects disagree, ordered by how many research directions build on each." />
          <div class="clist">
            {conflicts.map(([f, n]) => (
              <div class="crow">
                <a href={resolveRelative(slug, slugOf(f!) as FullSlug)}>{titleOf(f!)}</a>
                <span class="n">
                  {n} research direction{n === 1 ? "" : "s"} build on it
                </span>
              </div>
            ))}
          </div>
        </section>
      )}
      <section class="band" aria-label="Topics">
        <SecHead title="By topic" deck="What each hub covers, and how much evidence stands behind it." />
        <Topics c={c} from={slug} blurbs={blurbs} />
      </section>
      {/* The rest of the wiki stays in view: hiding concepts and entities behind a
          toggle would make most of its pages hard to find. */}
      {children}
    </>
  )
}
