// The record header: a card banded in the colour of the page kind, carrying
// the title and one byline row of countable facts. The byline is what keeps
// the card honest — the dl it replaced filled a third of the card and left
// the rest empty on every record in the corpus.
import type { FullSlug } from "@quartz-community/types"
import type { JSX } from "preact"
import { resolveRelative } from "@quartz-community/utils"
import type { ElementContent } from "hast"
import { cell, cited } from "../cites"
import { jsx } from "../jsx"
import { type Cite, type Corpus, type File, RELS, kindOf, slugOf, titleOf } from "../page"
import type { Ties } from "../ties"

// Twelve blocks and a +N fit one row of the header's facts column.
const MAX_STRIP = 12

// "5 source projects · well corroborated · conflict on record" → a sentence.
// The counts in that line are rendered as figures in the byline above it, so
// terms that only restate them are dropped rather than said twice.
function sentence(terms: string | null): string | null {
  if (!terms) return null
  const s = terms
    .split("·")
    .map((t) => t.trim())
    .filter(Boolean)
    .filter((t) => !/^\d+\s+source\s+projects?$/i.test(t))
    .filter((t) => !/^conflicts?\s+on\s+record$/i.test(t))
    .join(", ")
  return s ? s[0].toUpperCase() + s.slice(1) + "." : null
}

export function Record({ file, c, terms, standing, orcid, cites, rels, t, figures }: {
  file: File
  c: Corpus
  terms: string | null
  standing: ElementContent[] | null
  orcid: ElementContent[] | null
  cites: Cite[]
  rels: Record<(typeof RELS)[number], number>
  t: Ties
  /** Labelled rows for pages the citation counts say nothing about. */
  figures?: [string, string][]
}) {
  const slug = slugOf(file) as FullSlug
  const kind = kindOf(file)
  const topics = c.topicsOf(file)
  const line = sentence(terms)

  // The facts panel: one labelled row per countable thing the page rests on.
  // Every value is a nowrap chip inside a wrapping row, so a narrow card
  // stacks the chips instead of orphaning a word above its number.
  const rows: [string, JSX.Element][] = []
  const src = cited(cites, c)
  if (cites.length > 0)
    rows.push([
      src.projectsOnly ? "Projects cited" : "Sources cited",
      <>
        <span class="stripc">
          {cites.slice(0, MAX_STRIP).map((k) => (
            <i class={cell(k)} title={`${k.label}: cited ${k.n} time${k.n === 1 ? "" : "s"}`} />
          ))}
          {cites.length > MAX_STRIP && <span class="more">+{cites.length - MAX_STRIP}</span>}
        </span>
        <span class="sub">{src.summary}, listed in the margin</span>
      </>,
    ])
  // What a topic gathers is the measure of a topic, the way citations are the
  // measure of a concept. Every other kind states this in the rail only.
  if (kind.cls === "topic" && t.concepts.length > 0)
    rows.push([
      "Concepts",
      <span class="chips">
        <span class="chip">{t.concepts.length} gathered</span>
      </span>,
    ])
  const stated = RELS.filter((r) => rels[r] > 0)
  if (stated.length > 0)
    rows.push([
      "Relations",
      <span class="chips">
        {stated.map((r) => (
          <span class={`chip rel-${r}`}>
            {r} <b>{rels[r]}</b>
          </span>
        ))}
      </span>,
    ])
  if (t.citedBy.length > 0) {
    const inTopics = new Set(t.citedBy.flatMap((f) => c.topicsOf(f).map(slugOf))).size
    rows.push([
      "Linked from",
      <span class="chips">
        <span class="chip">
          {t.citedBy.length} {t.citedBy.length === 1 ? "page" : "pages"}
        </span>
        {inTopics > 0 && (
          <span class="chip">
            {inTopics} {inTopics === 1 ? "topic" : "topics"}
          </span>
        )}
      </span>,
    ])
  }
  if (t.named.length > 0)
    rows.push([
      t.named.length === 1 ? "Conflict" : "Conflicts",
      <span class="chips">
        <span class="chip warn">{t.named.length} open</span>
      </span>,
    ])
  if (t.reportAuthors.length > 0)
    rows.push([
      t.reportAuthors.length === 1 ? "Author" : "Authors",
      <span class="chips">
        {t.reportAuthors.map((a) => (
          <a class="chip" href={resolveRelative(slug, slugOf(a) as FullSlug)}>
            {titleOf(a)}
          </a>
        ))}
      </span>,
    ])
  if (orcid) rows.push(["ORCID", <span class="chips">{jsx(orcid)}</span>])
  for (const [label, value] of figures ?? [])
    rows.push([label, <span class="chips"><span class="chip">{value}</span></span>])

  return (
    <div class={`record kind-${kind.cls}`}>
      <div class="kindband" aria-hidden="true" />
      <div class={rows.length > 0 ? "body has-facts" : "body"}>
        <div class="ident">
          <p class="kind">
            <b>{kind.label}</b>
            {topics.length > 0 && (
              <>
                {" in "}
                {topics.map((t, i) => (
                  <>
                    {i > 0 && ", "}
                    <i class="dot" style={`--c:${c.hue(slugOf(t))}`} />
                    <a class="topic" href={resolveRelative(slug, slugOf(t) as FullSlug)}>
                      {titleOf(t)}
                    </a>
                  </>
                ))}
              </>
            )}
          </p>
          <h1>{titleOf(file)}</h1>
          {(line || standing) && (
            <p class="standing">
              {line && <span>{line} </span>}
              {standing && jsx(standing)}
            </p>
          )}
        </div>
        {rows.length > 0 && (
          <dl class="facts">
            {rows.map(([label, value]) => (
              <>
                <dt>{label}</dt>
                <dd>{value}</dd>
              </>
            ))}
          </dl>
        )}
      </div>
    </div>
  )
}
