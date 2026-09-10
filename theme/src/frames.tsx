// The BERIL page frame. One frame for every page type: a top bar, a record
// header that states what the page is and what it rests on, the prose, and two
// rails: contents and neighbourhood on the left, evidence on the right. The
// home page swaps the record for a topic heatmap and a map of the corpus.
//
// Stock components (search, dark mode, table of contents, footer) arrive
// through the layout slots; everything else is rendered here from page data.
import type { FullSlug, PageFrame, PageFrameProps, QuartzComponent, QuartzComponentProps } from "@quartz-community/types"
import type { JSX } from "preact"
import { htmlToJsx, resolveRelative, simplifySlug } from "@quartz-community/utils"
import type { ElementContent, Root } from "hast"
import {
  type Cite,
  type Corpus,
  type File,
  RELS,
  authorsOf,
  collectionOf,
  corpus,
  fm,
  isIndex,
  kindOf,
  linksOf,
  sections,
  slugOf,
  text,
  titleOf,
  walk,
} from "./page"
import { CorpusMap, mapStats } from "./map"
import { LocalGraph, neighbours, rank } from "./svg"

const NAV: [string, string][] = [
  ["Topics", "topics/index"],
  ["Concepts", "concepts/index"],
  ["Entities", "entities/index"],
  ["Conflicts", "conflicts/index"],
  ["Reports", "summaries/index"],
  ["Authors", "authors/index"],
  ["About", "about"],
]

const MAX_STRIP = 14
const MAX_LIST = 8

// Quartz types slot components as returning unknown; JSX wants elements.
type Slot = (props: QuartzComponentProps) => JSX.Element
const slot = (xs: readonly QuartzComponent[]) => xs as unknown as Slot[]

const jsx = (nodes: ElementContent[]) => htmlToJsx({ type: "root", children: nodes } as Root)

// "5 source projects · well corroborated · conflict on record" → a sentence.
function sentence(terms: string | null): string | null {
  if (!terms) return null
  const s = terms
    .split("·")
    .map((t) => t.trim())
    .filter(Boolean)
    .join(", ")
  return s ? s[0].toUpperCase() + s.slice(1) + "." : null
}

function cell(cite: Cite, primary: boolean): string {
  if (primary) return "p"
  if (cite.rels.has("contradicts")) return "c"
  if (cite.rels.has("supports")) return "s"
  if (cite.rels.has("refines")) return "r"
  return ""
}

function dotOf(cite: Cite, primary: boolean): string | undefined {
  if (primary) return "var(--ink)"
  for (const r of ["contradicts", "supports", "refines"] as const) if (cite.rels.has(r)) return `var(--${r})`
  return undefined
}

function Bar({ cd, header }: { cd: QuartzComponentProps; header: PageFrameProps["header"] }) {
  const slug = cd.fileData.slug as FullSlug
  const here = collectionOf(slug)
  return (
    <header class="bar">
      <a class="wordmark" href={resolveRelative(slug, "index" as FullSlug)}>
        {cd.cfg.pageTitle}
      </a>
      <nav aria-label="Collections">
        {NAV.map(([label, target]) => (
          <a
            href={resolveRelative(slug, target as FullSlug)}
            aria-current={collectionOf(target) === here && here !== "" ? "page" : undefined}
          >
            {label}
          </a>
        ))}
      </nav>
      <div class="tools">
        {slot(header).map((H) => (
          <H {...cd} />
        ))}
      </div>
    </header>
  )
}

function Record({ file, c, terms, standing, orcid, cites, rels }: {
  file: File
  c: Corpus
  terms: string | null
  standing: ElementContent[] | null
  orcid: ElementContent[] | null
  cites: Cite[]
  rels: Record<(typeof RELS)[number], number>
}) {
  const slug = slugOf(file) as FullSlug
  const kind = kindOf(file)
  const topics = c.topicsOf(file)
  const total = RELS.reduce((n, r) => n + rels[r], 0)
  const line = sentence(terms)
  return (
    <div class={`record kind-${kind.cls}`}>
      <div class="band" aria-hidden="true" />
      <div class="body">
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
        {(cites.length > 0 || total > 0 || line || standing || orcid) && (
          <dl class="evid">
            {orcid && (
              <>
                <dt>ORCID</dt>
                <dd>{jsx(orcid)}</dd>
              </>
            )}
            {cites.length > 0 && (
              <>
                <dt>Cited reports</dt>
                <dd class="stripc">
                  {cites.slice(0, MAX_STRIP).map((k, i) => (
                    <i class={cell(k, i === 0)} title={`${k.label}: cited ${k.n} time${k.n === 1 ? "" : "s"}`} />
                  ))}
                  {cites.length > MAX_STRIP && <span class="more">+{cites.length - MAX_STRIP}</span>}
                </dd>
              </>
            )}
            {total > 0 && (
              <>
                <dt>Relations stated</dt>
                <dd class="rels">
                  {RELS.map((r) => (
                    <span class={`rel-${r}`}>
                      {r} {rels[r]}
                    </span>
                  ))}
                </dd>
              </>
            )}
            {(line || standing) && (
              <>
                <dt>Standing</dt>
                <dd>
                  {line && <span>{line} </span>}
                  {standing && jsx(standing)}
                </dd>
              </>
            )}
          </dl>
        )}
      </div>
    </div>
  )
}

// Pages outside the knowledge collections (about, authors, catalog) are
// linked from everywhere, so their neighbourhood says nothing; give them
// only the table of contents.
const isKnowledge = (file: File) => !["plain", "collection"].includes(kindOf(file).cls)

// Left rail: what you use while reading (contents) and when leaving (graph).
function NavRail({ cd, file, c, right }: {
  cd: QuartzComponentProps
  file: File
  c: Corpus
  right: PageFrameProps["right"]
}) {
  const graph = isKnowledge(file) && neighbours(file, c).length >= 2
  return (
    <aside class="rail nav-rail">
      {slot(right).map((R) => (
        <R {...cd} />
      ))}
      {graph && (
        <section class="map">
          <h3>Where this page sits</h3>
          <LocalGraph file={file} c={c} />
          <p class="more">Neighbours by wikilink, coloured by topic.</p>
        </section>
      )}
    </aside>
  )
}

// Right rail: what the page rests on and what rests on it.
function Rail({ cd, file, c, cites, left }: {
  cd: QuartzComponentProps
  file: File
  c: Corpus
  cites: Cite[]
  left: PageFrameProps["left"]
}) {
  const slug = slugOf(file) as FullSlug
  const simple = simplifySlug(slug)
  const rel = (t: string) => resolveRelative(slug, t as FullSlug)
  const kind = kindOf(file)
  const knowledge = isKnowledge(file)

  const mine = new Set(cites.map((k) => k.slug))
  // Conflicts that name this page outrank ones that merely share its sources.
  const conflictScore = (k: File) => {
    if (linksOf(k).includes(simple)) return 2
    let shared = 0
    for (const l of new Set(linksOf(k))) if (mine.has(l) && ++shared >= 2) return 1
    return 0
  }
  // An author page cites its own reports, so shared sources would drag in
  // every conflict those reports touch; that belongs on the report pages.
  const conflicts =
    !knowledge || kind.cls === "conflict" || kind.cls === "author"
      ? []
      : c.conflicts
          .map((k) => [k, conflictScore(k)] as const)
          .filter(([, s]) => s > 0)
          .sort((a, b) => b[1] - a[1] || titleOf(a[0]).localeCompare(titleOf(b[0])))
          .map(([k]) => k)
  // Authorship attaches to project reports, never to the wiki page, which is
  // machine-written. A report page names its authors; every other page names
  // the authors of the reports it cites, with how many of those reports each
  // one wrote.
  const isReport = kind.cls === "report"
  const reportAuthors = isReport ? authorsOf(file, c) : []
  const citedAuthors = new Map<File, number>()
  if (!isReport && kind.cls !== "author") {
    for (const k of cites) {
      const report = c.bySlug.get(k.slug)
      if (!report) continue
      for (const a of authorsOf(report, c)) citedAuthors.set(a, (citedAuthors.get(a) ?? 0) + 1)
    }
  }
  const authors = [...citedAuthors].sort((x, y) => y[1] - x[1] || titleOf(x[0]).localeCompare(titleOf(y[0])))
  // Author pages link to every report they wrote; that is authorship, listed
  // above, not citation.
  const citedBy = !knowledge
    ? []
    : (c.inbound.get(simple) ?? [])
        .filter((f) => f !== file && !isIndex(slugOf(f)) && collectionOf(slugOf(f)) !== "authors")
        .sort((a, b) => rank(a) - rank(b) || titleOf(a).localeCompare(titleOf(b)))
  const entities = !knowledge
    ? []
    : [...new Set(linksOf(file))]
        .map((l) => c.bySlug.get(l))
        .filter((f): f is File => !!f && collectionOf(slugOf(f)) === "entities" && !isIndex(slugOf(f)))
        .sort((a, b) => titleOf(a).localeCompare(titleOf(b)))

  return (
    <aside class="rail evidence-rail">
      {reportAuthors.length > 0 && (
        <section>
          <h3>Project authors</h3>
          <ul>
            {reportAuthors.map((a) => (
              <li class="plain">
                <a href={rel(slugOf(a))}>{titleOf(a)}</a>
              </li>
            ))}
          </ul>
        </section>
      )}
      {cites.length > 0 && (
        <section>
          <h3>Evidence on this page</h3>
          <ul>
            {cites.slice(0, MAX_LIST).map((k, i) => {
              const dot = dotOf(k, i === 0)
              const words = [...k.rels].join(", ")
              const sub = i === 0 && k.n > 1 ? `primary source, ${k.n} citations` : words
              return (
                <li style={dot ? `--d:${dot}` : undefined}>
                  <span>
                    <a href={rel(k.slug)}>
                      <code>{k.label}</code>
                    </a>
                    {sub && <span class="w">{sub}</span>}
                  </span>
                  {!(i === 0 && k.n > 1) && <span class="n">{k.n}</span>}
                </li>
              )
            })}
            {cites.length > MAX_LIST && <li class="plain rest">and {cites.length - MAX_LIST} more</li>}
          </ul>
        </section>
      )}
      {authors.length > 0 && (
        <section>
          <h3>Authors of the cited reports</h3>
          <ul>
            {authors.slice(0, MAX_LIST).map(([a, n]) => (
              <li class="plain">
                <a href={rel(slugOf(a))}>{titleOf(a)}</a>
                <span class="n" title={`wrote ${n} of the reports cited here`}>
                  {n}
                </span>
              </li>
            ))}
            {authors.length > MAX_LIST && <li class="plain rest">and {authors.length - MAX_LIST} more</li>}
          </ul>
        </section>
      )}
      {conflicts.length > 0 && (
        <section>
          <h3>{conflicts.length === 1 ? "Open conflict" : "Open conflicts"}</h3>
          <ul>
            {conflicts.slice(0, 4).map((k) => (
              <li style="--d:var(--conflict)">
                <a href={rel(slugOf(k))}>{titleOf(k)}</a>
              </li>
            ))}
          </ul>
        </section>
      )}
      {citedBy.length > 0 && (
        <section>
          <h3>Cited by</h3>
          <ul>
            {citedBy.slice(0, MAX_LIST).map((f) => {
              const hue = c.hueOf(f)
              return (
                <li style={hue ? `--d:${hue}` : undefined}>
                  <a href={rel(slugOf(f))}>{titleOf(f)}</a>
                </li>
              )
            })}
            {citedBy.length > MAX_LIST && <li class="plain rest">and {citedBy.length - MAX_LIST} more</li>}
          </ul>
        </section>
      )}
      {entities.length > 0 && (
        <section>
          <h3>Entities named</h3>
          <ul>
            {entities.slice(0, MAX_LIST).map((f) => {
              const k = kindOf(f)
              return (
                <li class="plain">
                  <a href={rel(slugOf(f))}>{titleOf(f)}</a>
                  <span class={`tag k-${k.cls}`}>{k.label}</span>
                </li>
              )
            })}
            {entities.length > MAX_LIST && <li class="plain rest">and {entities.length - MAX_LIST} more</li>}
          </ul>
        </section>
      )}
      {slot(left).map((L) => (
        <L {...cd} />
      ))}
    </aside>
  )
}

// Topic heatmap: what each topic links to, by collection and entity type.
const COLUMNS: [string, (l: string, f: File | undefined) => boolean][] = [
  ["Concepts", (l) => collectionOf(l) === "concepts"],
  ["Reports", (l) => collectionOf(l) === "summaries"],
  ["Conflicts", (l) => collectionOf(l) === "conflicts"],
  ["Organisms", (_, f) => !!f && fm(f)?.type === "Organism"],
  ["Methods", (_, f) => !!f && fm(f)?.type === "Method"],
  ["Datasets", (_, f) => !!f && fm(f)?.type === "Dataset"],
  ["Compounds", (_, f) => !!f && fm(f)?.type === "Compound"],
  ["Genes", (_, f) => !!f && fm(f)?.type === "Gene_Or_Pathway"],
]

function Heatmap({ c, from, caption }: { c: Corpus; from: FullSlug; caption: string | null }) {
  const counts = c.topics.map((t) => {
    const links = [...new Set(linksOf(t))]
    return COLUMNS.map(([, test]) => links.filter((l) => test(l, c.bySlug.get(l))).length)
  })
  const keep = COLUMNS.map((_, j) => counts.some((row) => row[j] > 0))
  const max = COLUMNS.map((_, j) => Math.max(1, ...counts.map((row) => row[j])))
  return (
    <div class="heat">
      <table>
        <thead>
          <tr>
            <th>Topic</th>
            {COLUMNS.map(([name], j) => keep[j] && <th class="c">{name}</th>)}
          </tr>
        </thead>
        <tbody>
          {c.topics.map((t, i) => (
            <tr>
              <td class="name">
                <i class="dot" style={`--c:${c.hue(slugOf(t))}`} />
                <a href={resolveRelative(from, slugOf(t) as FullSlug)}>{titleOf(t)}</a>
              </td>
              {counts[i].map(
                (n, j) =>
                  keep[j] && (
                    <td class="cell">
                      <span style={`--v:${Math.round((n / max[j]) * 100)}`} data-v={n === 0 ? "0" : undefined}>
                        {n}
                      </span>
                    </td>
                  ),
              )}
            </tr>
          ))}
        </tbody>
        <caption>{caption ?? "Pages each topic links to."}</caption>
      </table>
    </div>
  )
}

function Home({ file, c, tree, standing }: { file: File; c: Corpus; tree: Root; standing: ElementContent[] | null }) {
  const slug = slugOf(file) as FullSlug
  const { intro, byHeading } = sections(tree)
  const corpusLine = byHeading.get("corpus")
  const browse = byHeading.get("browse")
  // The heatmap counts what each topic links to; this list says what each
  // topic is about, which nothing else on the page does.
  const topics = byHeading.get("topics")
  const stats = mapStats(c)
  return (
    <>
      <section class="home">
        <div class="hero">
          <h1>{titleOf(file)}</h1>
          {standing && <p class="standing">{jsx(standing)}</p>}
          <div class="lede">{jsx(intro)}</div>
        </div>
        {browse && (
          <nav class="digests" aria-label="Browse">
            <h2>Browse</h2>
            {jsx(browse)}
          </nav>
        )}
      </section>
      <section class="heatwrap" aria-label="Topics by collection">
        <Heatmap c={c} from={slug} caption={corpusLine ? text({ type: "root", children: corpusLine }).trim() : null} />
      </section>
      <section class="corpusmap" aria-label="Map of the corpus">
        <div class="maphead">
          <h2>The map</h2>
          <p>
            Each of the {stats.topics} topics sits at the middle of the concepts that belong to it,
            {" "}
            {stats.concepts} in all, sized by how linked each one is. {stats.crossings} wikilinks
            run between concepts in different topics: at rest they are summed into one line per pair
            of topics, heavier where more of them cross. Hover a concept to see its own links, or a
            topic to see every link leaving it. A concept two topics both claim is drawn in one
            ring, with a second spoke in the other topic's colour running back to that topic. A grey
            point is a concept no topic links to at all, on a dashed tether beside the topic it
            cites most. Click any point to open the page.
          </p>
        </div>
        <div class="mapframe">
          <CorpusMap c={c} from={slug} />
        </div>
      </section>
      {topics && (
        <section class="topiclist" aria-label="Topics">
          <h2>Topics</h2>
          {jsx(topics)}
        </section>
      )}
    </>
  )
}

export const BerilFrame: PageFrame = {
  name: "beril",
  render({ componentData: cd, header, beforeBody, pageBody: Content, afterBody, left, right, footer }) {
    const file = cd.fileData as File
    const c = corpus(cd.allFiles as File[])
    const tree = cd.tree as Root
    // Mutates the tree Content will render: lifts the provenance callout,
    // tags citations and relation words.
    const w = walk(tree)
    const home = slugOf(file) === "index"
    return (
      <>
        <Bar cd={cd} header={header} />
        {home ? (
          <Home file={file} c={c} tree={tree} standing={w.standing} />
        ) : (
          <main class="page-grid">
            <Record
              file={file}
              c={c}
              terms={w.terms}
              standing={w.standing}
              orcid={w.orcid}
              cites={w.cites}
              rels={w.rels}
            />
            <NavRail cd={cd} file={file} c={c} right={right} />
            <div class="prose">
              {slot(beforeBody).map((B) => (
                <B {...cd} />
              ))}
              {slot([Content]).map((C) => (
                <C {...cd} />
              ))}
              {slot(afterBody).map((A) => (
                <A {...cd} />
              ))}
            </div>
            <Rail cd={cd} file={file} c={c} cites={w.cites} left={left} />
          </main>
        )}
        {slot(footer).map((F) => (
          <F {...cd} />
        ))}
      </>
    )
  },
}
