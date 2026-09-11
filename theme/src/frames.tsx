// The BERIL page frame. One frame for every page type: a top bar, a record
// header that states what the page is and what it rests on, the prose, and two
// rails: contents and neighbourhood on the left, evidence on the right. The
// home page swaps the record for the corpus in figures and a map of it, and a
// collection index swaps the prose for a listing of what the collection holds.
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
  counts,
  fm,
  isIndex,
  kindOf,
  linksOf,
  sections,
  slugOf,
  stripIndexLists,
  text,
  titleOf,
  topicBlurbs,
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

// Twelve blocks and a +N fit one row of the header's facts column.
const MAX_STRIP = 12
const MAX_LIST = 8

// Quartz types slot components as returning unknown; JSX wants elements.
type Slot = (props: QuartzComponentProps) => JSX.Element
const slot = (xs: readonly QuartzComponent[]) => xs as unknown as Slot[]

const jsx = (nodes: ElementContent[]) => htmlToJsx({ type: "root", children: nodes } as Root)

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

// Pages outside the knowledge collections (about, authors, catalog) are
// linked from everywhere, so their neighbourhood says nothing.
const isKnowledge = (file: File) => !["plain", "collection"].includes(kindOf(file).cls)

// What else on the site this page is tied to. Computed once per render and
// shared: the header states the sizes, the rail lists the members.
interface Ties {
  conflicts: File[]
  /** Conflicts that name this page, rather than merely sharing its sources. */
  named: File[]
  citedBy: File[]
  entities: File[]
  /** Authors of the reports this page cites, and how many each wrote. */
  citedAuthors: [File, number][]
  /** Authors of this project report, when the page is one. */
  reportAuthors: File[]
}

function ties(file: File, c: Corpus, cites: Cite[]): Ties {
  const slug = slugOf(file)
  const simple = simplifySlug(slug)
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
  // Sharing two sources with a conflict is enough to be worth listing in the
  // rail, but not enough to count in the header: a well-cited concept shares
  // sources with dozens of them, and "26 open conflicts" over a page that is
  // named by two reads as a claim the corpus never made.
  const named = conflicts.filter((k) => linksOf(k).includes(simple))

  // Authorship attaches to project reports, never to the wiki page, which is
  // machine-written. A report page names its authors; every other page names
  // the authors of the reports it cites, with how many of those reports each
  // one wrote.
  const isReport = kind.cls === "report"
  const reportAuthors = isReport ? authorsOf(file, c) : []
  const tally = new Map<File, number>()
  if (!isReport && kind.cls !== "author") {
    for (const k of cites) {
      const report = c.bySlug.get(k.slug)
      if (!report) continue
      for (const a of authorsOf(report, c)) tally.set(a, (tally.get(a) ?? 0) + 1)
    }
  }
  const citedAuthors = [...tally].sort((x, y) => y[1] - x[1] || titleOf(x[0]).localeCompare(titleOf(y[0])))

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

  return { conflicts, named, citedBy, entities, citedAuthors, reportAuthors }
}

// The record header: a card banded in the colour of the page kind, carrying
// the title and one byline row of countable facts. The byline is what keeps
// the card honest — the dl it replaced filled a third of the card and left
// the rest empty on every record in the corpus.
function Record({ file, c, terms, standing, orcid, cites, rels, t, figures }: {
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
  if (cites.length > 0)
    rows.push([
      cites.length === 1 ? "Source" : "Sources",
      <>
        <span class="stripc">
          {cites.slice(0, MAX_STRIP).map((k, i) => (
            <i class={cell(k, i === 0)} title={`${k.label}: cited ${k.n} time${k.n === 1 ? "" : "s"}`} />
          ))}
          {cites.length > MAX_STRIP && <span class="more">+{cites.length - MAX_STRIP}</span>}
        </span>
        <span class="sub">{cites.length} project reports</span>
      </>,
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
      "Cited by",
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

// A rail list longer than the rail: the first few rows, then the rest behind a
// disclosure. "and 31 more" used to be a dead line of text that looked like a
// link; now it opens the list it is counting, with no script involved.
function Rows({ rows }: { rows: JSX.Element[] }) {
  const head = rows.slice(0, MAX_LIST)
  const rest = rows.slice(MAX_LIST)
  return (
    <>
      <ul>{head}</ul>
      {rest.length > 0 && (
        <details class="rest">
          <summary>and {rest.length} more</summary>
          <ul>{rest}</ul>
        </details>
      )}
    </>
  )
}

// Right rail: what the page rests on and what rests on it.
function Rail({ cd, file, c, cites, t, left }: {
  cd: QuartzComponentProps
  file: File
  c: Corpus
  cites: Cite[]
  t: Ties
  left: PageFrameProps["left"]
}) {
  const slug = slugOf(file) as FullSlug
  const rel = (x: string) => resolveRelative(slug, x as FullSlug)
  return (
    <aside class="rail evidence-rail">
      {t.reportAuthors.length > 0 && (
        <section>
          <h3>Project authors</h3>
          <ul>
            {t.reportAuthors.map((a) => (
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
          <Rows
            rows={cites.map((k, i) => {
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
          />
          <p class="more">
            The dot is the relation the prose states; black is the primary source. The strip in the
            header says the same, one block per report.
          </p>
        </section>
      )}
      {t.citedAuthors.length > 0 && (
        <section>
          <h3>Authors of the cited reports</h3>
          <Rows
            rows={t.citedAuthors.map(([a, n]) => (
              <li class="plain">
                <a href={rel(slugOf(a))}>{titleOf(a)}</a>
                <span class="n" title={`wrote ${n} of the reports cited here`}>
                  {n}
                </span>
              </li>
            ))}
          />
        </section>
      )}
      {t.conflicts.length > 0 && (
        <section>
          <h3>{t.conflicts.length === 1 ? "Open conflict" : "Open conflicts"}</h3>
          {t.named.length === 0 && <p class="more">Conflicts over sources this page cites.</p>}
          <ul>
            {t.conflicts.slice(0, 4).map((k) => (
              <li style="--d:var(--conflict)">
                <a href={rel(slugOf(k))}>{titleOf(k)}</a>
              </li>
            ))}
          </ul>
        </section>
      )}
      {t.citedBy.length > 0 && (
        <section>
          <h3>Cited by</h3>
          <Rows
            rows={t.citedBy.map((f) => {
              const hue = c.hueOf(f)
              return (
                <li style={hue ? `--d:${hue}` : undefined}>
                  <a href={rel(slugOf(f))}>{titleOf(f)}</a>
                </li>
              )
            })}
          />
        </section>
      )}
      {t.entities.length > 0 && (
        <section>
          <h3>Entities named</h3>
          <Rows
            rows={t.entities.map((f) => {
              const k = kindOf(f)
              return (
                <li class="plain">
                  <a href={rel(slugOf(f))}>{titleOf(f)}</a>
                  <span class={`tag k-${k.cls}`}>{k.label}</span>
                </li>
              )
            })}
          />
        </section>
      )}
      {slot(left).map((L) => (
        <L {...cd} />
      ))}
    </aside>
  )
}

// The reports a page cites, listed once under the prose in citation order.
// The marks in the text are numbers; this is where a number gets its name.
function Sources({ cites, from }: { cites: Cite[]; from: FullSlug }) {
  if (cites.length === 0) return null
  const ordered = [...cites].sort((a, b) => a.num - b.num)
  return (
    <section class="sources">
      <h2>Sources cited on this page</h2>
      <ol>
        {ordered.map((k) => (
          <li value={k.num}>
            <a href={resolveRelative(from, k.slug as FullSlug)}>
              <code>{k.label}</code>
            </a>
            {k.rels.size > 0 && <span class="w">{[...k.rels].join(", ")}</span>}
          </li>
        ))}
      </ol>
    </section>
  )
}

// A collection index lists what the collection holds. Quartz's folder listing
// prints bare titles down the middle of an otherwise empty page; every one of
// these pages already carries a description and a type, so use them.
// What a collection index can say about itself, in countable terms. Quartz
// gives an index page no citations, so without this its byline is empty and
// the page opens on a bare title.
function indexFigures(file: File, c: Corpus): [string, string][] {
  const here = collectionOf(slugOf(file))
  const members = [...c.bySlug.values()].filter(
    (f) => collectionOf(slugOf(f)) === here && !isIndex(slugOf(f)),
  )
  const n = members.length
  if (n === 0) return []
  const plural = (k: number, unit: string) => `${k} ${unit}${k === 1 ? "" : "s"}`
  const out: [string, string][] = []
  switch (here) {
    case "entities": {
      out.push(["Entities", String(n)])
      out.push(["Kinds", plural(new Set(members.map((f) => kindOf(f).label)).size, "kind")])
      break
    }
    case "topics": {
      out.push(["Topics", String(n)])
      const gathered = new Set(
        members.flatMap((f) => linksOf(f).filter((l) => collectionOf(l) === "concepts")),
      )
      out.push(["Concepts", `${gathered.size} gathered`])
      break
    }
    case "authors": {
      out.push(["People", String(n)])
      const reports = new Set(
        members.flatMap((f) => linksOf(f).filter((l) => collectionOf(l) === "summaries")),
      )
      out.push(["Credited on", plural(reports.size, "project report")])
      break
    }
    case "summaries":
      out.push(["Reports", String(n)])
      break
    case "conflicts":
      out.push(["Conflicts", plural(n, "recorded conflict")])
      break
    case "concepts":
      out.push(["Concepts", String(n)])
      break
    default:
      out.push(["Pages", String(n)])
  }
  return out
}

const PLURAL: Record<string, string> = {
  organism: "Organisms",
  method: "Methods",
  dataset: "Datasets",
  gene: "Genes and pathways",
  compound: "Compounds",
  entity: "Other entities",
}

function Listing({ file, c }: { file: File; c: Corpus }) {
  const slug = slugOf(file) as FullSlug
  const here = collectionOf(slug)
  const members = [...c.bySlug.values()].filter((f) => collectionOf(slugOf(f)) === here && !isIndex(slugOf(f)))
  if (members.length === 0) return null
  const inbound = (f: File) =>
    (c.inbound.get(simplifySlug(slugOf(f))) ?? []).filter((k) => !isIndex(slugOf(k))).length
  const byRank = (a: File, b: File) => inbound(b) - inbound(a) || titleOf(a).localeCompare(titleOf(b))
  const byName = (a: File, b: File) => titleOf(a).localeCompare(titleOf(b))
  // Topics keep the order the home page lists them in; nothing links to a
  // topic often enough for a ranking to mean anything.
  const alphabetical = here === "authors" || here === "data" || here === "topics"

  // What to count differs by collection: nothing links to an author page, so
  // "linked from" would read zero on every one of them, and a topic page is
  // measured by what it gathers rather than by what points at it.
  const out = (f: File, collection: string) =>
    new Set(linksOf(f).filter((l) => collectionOf(l) === collection)).size
  const plural = (n: number, unit: string) => `${n} ${unit}${n === 1 ? "" : "s"}`

  const meta = (f: File): string | null => {
    if (here === "authors") {
      const n = out(f, "summaries")
      return n > 0 ? `credited on ${plural(n, "project report")}` : null
    }
    if (here === "topics") {
      const c = out(f, "concepts")
      const r = out(f, "summaries")
      return c > 0 || r > 0 ? `${plural(c, "concept")} · ${plural(r, "report")}` : null
    }
    // A conflict page carries no description, and how many pages link to it
    // says nothing about it; the projects that disagree do.
    if (here === "conflicts") {
      const n = out(f, "summaries")
      return n > 0 ? `${plural(n, "source project")} disagree` : null
    }
    const n = inbound(f)
    return n > 0 ? `linked from ${plural(n, "page")}` : null
  }

  // An entity is coloured by what kind of thing it is; everything else by the
  // topic that claims it. A wall of identical cards was the complaint.
  const ENTITY_HUE: Record<string, string> = {
    organism: "var(--organism)",
    method: "var(--method)",
    dataset: "var(--dataset)",
    gene: "var(--gene)",
    compound: "var(--compound)",
  }
  const accent = (f: File) =>
    here === "entities" ? ENTITY_HUE[kindOf(f).cls] : (c.hueOf(f) ?? undefined)

  const Card = ({ f }: { f: File }) => {
    const k = kindOf(f)
    const line = meta(f)
    const desc = fm(f)?.description
    const hue = accent(f)
    return (
      <a
        class="card"
        href={resolveRelative(slug, slugOf(f) as FullSlug)}
        style={hue ? `--d:${hue}` : undefined}
      >
        <b>{titleOf(f)}</b>
        {desc && <span class="desc">{desc}</span>}
        {(line || here === "entities") && (
          <span class="meta">
            {here === "entities" && <span class={`tag k-${k.cls}`}>{k.label}</span>}
            {line && <span class="n">{line}</span>}
          </span>
        )}
      </a>
    )
  }

  // Entities are the one collection with a type on every page; grouping by it
  // beats one 139-item list, and it needs no script to work.
  if (here === "entities") {
    const groups = new Map<string, File[]>()
    for (const f of members.sort(byRank)) {
      const cls = kindOf(f).cls
      groups.set(cls, [...(groups.get(cls) ?? []), f])
    }
    const order = ["organism", "method", "dataset", "gene", "compound", "entity"]
    return (
      <div class="listing">
        {order
          .filter((cls) => groups.has(cls))
          .map((cls) => (
            <section>
              <div class="sechead">
                <h2>{PLURAL[cls] ?? cls}</h2>
                <p>{groups.get(cls)!.length} pages, most linked first</p>
              </div>
              <div class="cards">
                {groups.get(cls)!.map((f) => (
                  <Card f={f} />
                ))}
              </div>
            </section>
          ))}
      </div>
    )
  }

  return (
    <div class="listing">
      <div class="cards">
        {members.sort(alphabetical ? byName : byRank).map((f) => (
          <Card f={f} />
        ))}
      </div>
    </div>
  )
}

// The nine topics, with what each covers and how much evidence stands behind
// it. This replaces two separate renderings of the same nine rows: a heat
// table above the map and a blurb list below it.
const COLUMNS: [string, (l: string, f: File | undefined) => boolean][] = [
  ["Concepts", (l) => collectionOf(l) === "concepts"],
  ["Reports", (l) => collectionOf(l) === "summaries"],
  ["Conflicts", (l) => collectionOf(l) === "conflicts"],
  ["Entities", (l) => collectionOf(l) === "entities"],
]

function Topics({ c, from, blurbs }: {
  c: Corpus
  from: FullSlug
  blurbs: Map<string, ElementContent[]>
}) {
  const counts = c.topics.map((t) => {
    const links = [...new Set(linksOf(t))]
    return COLUMNS.map(([, test]) => links.filter((l) => test(l, c.bySlug.get(l))).length)
  })
  // Shade each column against its own largest value: reports outnumber
  // conflicts several times over, and one ramp across both would flatten the
  // column that varies least.
  const max = COLUMNS.map((_, j) => Math.max(1, ...counts.map((row) => row[j])))
  return (
    <div class="topictable">
      <div class="thead">
        <span>Topic</span>
        <span>What it covers</span>
        {COLUMNS.map(([name]) => (
          <span class="c">{name}</span>
        ))}
      </div>
      {c.topics.map((t, i) => {
        const blurb = blurbs.get(simplifySlug(slugOf(t)))
        return (
          <div class="trow">
            <span class="name">
              <i class="dot" style={`--c:${c.hue(slugOf(t))}`} />
              <a href={resolveRelative(from, slugOf(t) as FullSlug)}>{titleOf(t)}</a>
            </span>
            <p>{blurb ? jsx(blurb) : null}</p>
            {counts[i].map((n, j) => (
              <span class="c">
                <span style={`--v:${Math.round((n / max[j]) * 100)}`} data-v={n === 0 ? "0" : undefined}>
                  {n}
                </span>
              </span>
            ))}
          </div>
        )
      })}
    </div>
  )
}

function SecHead({ title, deck }: { title: string; deck: string }) {
  return (
    <div class="sechead">
      <h2>{title}</h2>
      <p>{deck}</p>
    </div>
  )
}

function Home({ file, c, tree, standing }: { file: File; c: Corpus; tree: Root; standing: ElementContent[] | null }) {
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
      <section class="band hero">
        <h1>{titleOf(file)}</h1>
        {standing && <p class="standing">{jsx(standing)}</p>}
        {/* The opening paragraph leads at reading size; the rest sits beside
            it rather than leaving half the masthead empty above a page whose
            every other section runs the full measure. */}
        <div class="lede">
          <div class="lead">{jsx(lead)}</div>
          {after.length > 0 && <div class="after">{jsx(after)}</div>}
        </div>
      </section>
      <section class="band" aria-label="The corpus in figures">
        <div class="stats">
          <div>
            <b>{n.reports}</b>
            <span>project reports</span>
          </div>
          <div>
            <b>{n.concepts}</b>
            <span>concepts</span>
          </div>
          <div>
            <b>{n.entities}</b>
            <span>entities</span>
          </div>
          <div>
            <b>{n.conflicts}</b>
            <span>recorded conflicts</span>
          </div>
          <div>
            <b>{n.topics}</b>
            <span>topics</span>
          </div>
        </div>
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

export const BerilFrame: PageFrame = {
  name: "beril",
  render({ componentData: cd, header, beforeBody, pageBody: Content, afterBody, left, right, footer }) {
    const file = cd.fileData as File
    const c = corpus(cd.allFiles as File[])
    const tree = cd.tree as Root
    const slug = slugOf(file)
    // Mutates the tree Content will render: lifts the provenance callout,
    // numbers citations, tags relation words, drops a hand-written index list.
    const w = walk(tree)
    stripIndexLists(tree, slug)
    const home = slug === "index"
    const index = isIndex(slug)
    const t = ties(file, c, w.cites)
    return (
      <>
        <Bar cd={cd} header={header} />
        {home ? (
          <Home file={file} c={c} tree={tree} standing={w.standing} />
        ) : index ? (
          <main class="band index-page">
            <Record file={file} c={c} terms={w.terms} standing={w.standing} orcid={w.orcid} cites={w.cites} rels={w.rels} t={t} figures={indexFigures(file, c)} />
            <div class="prose">
              {slot(beforeBody).map((B) => (
                <B {...cd} />
              ))}
              {slot([Content]).map((C) => (
                <C {...cd} />
              ))}
            </div>
            <Listing file={file} c={c} />
          </main>
        ) : (
          <main class="page-grid">
            <Record file={file} c={c} terms={w.terms} standing={w.standing} orcid={w.orcid} cites={w.cites} rels={w.rels} t={t} />
            <NavRail cd={cd} file={file} c={c} right={right} />
            <div class="prose">
              {slot(beforeBody).map((B) => (
                <B {...cd} />
              ))}
              {slot([Content]).map((C) => (
                <C {...cd} />
              ))}
              <Sources cites={w.cites} from={slug as FullSlug} />
              {slot(afterBody).map((A) => (
                <A {...cd} />
              ))}
            </div>
            <Rail cd={cd} file={file} c={c} cites={w.cites} t={t} left={left} />
          </main>
        )}
        {slot(footer).map((F) => (
          <F {...cd} />
        ))}
      </>
    )
  },
}
