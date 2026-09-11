// The home page swaps the record for the corpus in figures, a map of it, and
// the topic table.
import type { FullSlug } from "@quartz-community/types"
import { resolveRelative } from "@quartz-community/utils"
import type { ElementContent, Root } from "hast"
import { jsx } from "../jsx"
import { CorpusMap, mapStats } from "../map"
import { type Corpus, type File, counts, sections, slugOf, titleOf, topicBlurbs } from "../page"
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
  const { intro, byHeading } = sections(tree)
  const firstPara = intro.findIndex((n) => n.type === "element" && n.tagName === "p")
  const lead = firstPara >= 0 ? [intro[firstPara]] : intro
  const after = firstPara >= 0 ? intro.filter((_, i) => i !== firstPara) : []
  const browse = byHeading.get("browse")
  const blurbs = topicBlurbs(byHeading.get("topics"))
  const n = counts(c)
  const stats = mapStats(c)
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
      {browse && (
        <section class="band">
          <SecHead title="Start here" deck="Ways in, depending on what you came for." />
          <nav class="browse" aria-label="Browse">
            {jsx(browse)}
          </nav>
        </section>
      )}
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
      <section class="band" aria-label="Topics">
        <SecHead title="Topics" deck="What each hub covers, and how much evidence stands behind it." />
        <Topics c={c} from={slug} blurbs={blurbs} />
      </section>
    </>
  )
}
