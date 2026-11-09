// The Results picture: how new each result is, by topic, with each project's results in a
// box. Position carries the topic (row) and the PubMed comparison (column), whose first two
// columns are the two kinds of new; a mark's fill and shape carry the type of result
// (positive, negative, inconclusive, about the data), and a ring marks a result with a
// related result in another project on this map. Hovering a box draws those related-result lines
// (src/client/novelty.ts). Links and project names come from the results index page that
// publish/cards.py wrote.
import type { FullSlug } from "@quartz-community/types"
import { resolveRelative } from "@quartz-community/utils"
import { type Corpus, type File, slugOf, titleOf } from "../page"
import { type FindingFm, TYPE_WORDS, UPDATES_WORDS, findingsOf, kindKey, resultsIndex } from "./Cards"

const fmOf = (f: File) => (f.frontmatter ?? {}) as FindingFm
const topicSlug = (t: File) => slugOf(t).replace(/^topics\//, "")
const idOf = (f: File) => slugOf(f).replace(/^findings\//, "")

// Each column's colour, in publish's order: novel, builds on, differs, similar, too little
// evidence, not compared yet. Marks stay ink; the colour names the column.
const TONE = ["new", "builds", "match", "match", "none", "unset"]
// Column widths follow the usual counts: the "too little evidence" column holds most results.
const WIDTH = [1.1, 1.4, 0.6, 0.6, 2.2, 0.8]

/** Legend words for each mark type, in legend order; the map's marks use the same keys. */
export const MARK_WORDS = TYPE_WORDS
// How a box's label counts each type.
const COUNT_WORDS: Record<string, [string, string]> = {
  positive: ["positive result", "positive results"],
  negative: ["negative result", "negative results"],
  inconclusive: ["inconclusive result", "inconclusive results"],
  data: ["result about the data", "results about the data"],
}

/** The ids of listed results joined by a related-result link whose other end is also listed,
 * the only links the map can draw. */
export function drawableRelated(c: Corpus): { ids: Set<string>; links: { a: string; b: string; pa: string; pb: string; label: string }[] } {
  const listed = new Set(findingsOf(c).map(idOf))
  const links = (resultsIndex(c).links ?? [])
    .filter((l) => l.family === "r" && l.a && l.b && listed.has(l.a) && listed.has(l.b))
    .map((l) => ({ a: l.a!, b: l.b!, pa: l.pa, pb: l.pb, label: l.label ?? "" }))
  return { ids: new Set(links.flatMap((l) => [l.a, l.b])), links }
}

const plural = (n: number, one: string, many: string) => `${n} ${n === 1 ? one : many}`

/** One project's results in one cell: the box is the button; the marks are its results. */
function Group({ sid, items, title, col, related }: { sid: string; items: File[]; title: string; col: string; related: Set<string> }) {
  const kinds = MARK_WORDS.map(([k]) => [k, items.filter((f) => kindKey(fmOf(f)) === k).length] as const).filter(([, n]) => n > 0)
  const rel = items.filter((f) => related.has(idOf(f))).length
  const label = [
    `${title}: ${plural(items.length, "result", "results")}, ${col}`,
    kinds.map(([k, n]) => `${n} ${COUNT_WORDS[k][n === 1 ? 0 : 1]}`).join(", "),
    rel ? `${rel} with a related result in another project` : "",
  ]
    .filter(Boolean)
    .join(". ")
  return (
    <button type="button" class="nbead" data-p={sid} aria-label={label}>
      {items.map((f) => {
        const m = fmOf(f)
        return (
          <i
            class={`nd${related.has(idOf(f)) ? " rel" : ""}`}
            data-k={kindKey(m)}
            data-id={idOf(f)}
            data-t={titleOf(f)}
            data-g={m.gist ?? ""}
            data-r={m.report_title ?? sid}
            // The preview and the box list show this text, so a correction carries its note.
            data-kind={[m.kind_text, m.updates_claim ? UPDATES_WORDS : ""].filter(Boolean).join(". ")}
            aria-hidden="true"
          />
        )
      })}
    </button>
  )
}

/** A column heading's note, readable without a pointer: a button that shows the note. */
function ColNote({ col, note }: { col: string; note?: string }) {
  if (!note) return <>{col}</>
  return (
    <span class="nvnotewrap">
      <button type="button" class="nvnoteb" aria-expanded="false" title={note}>
        {col}
        <span aria-hidden="true"> ⓘ</span>
      </button>
      <span class="nvnote" role="note" hidden>
        {note}
      </span>
    </span>
  )
}

export function NoveltyMap({ c, from }: { c: Corpus; from: FullSlug }) {
  const idx = resultsIndex(c)
  const all = findingsOf(c)
  const order = idx.compare_order ?? []
  if (all.length === 0 || order.length === 0) return null
  const last = order[order.length - 1]
  const cols = order.filter((col) => col !== last || all.some((f) => fmOf(f).compare_text === col))
  const rows = c.topics.filter((t) => all.some((f) => fmOf(f).topic === topicSlug(t)))
  const count = (col: string) => all.filter((f) => fmOf(f).compare_text === col).length
  const related = drawableRelated(c)
  const data = {
    links: related.links,
    titles: idx.project_titles ?? {},
    // Every project with a box, so a box's panel heading always links to its report.
    hrefs: Object.fromEntries(
      [...new Set([...Object.keys(idx.project_titles ?? {}), ...all.map((f) => fmOf(f).source ?? "")])]
        .filter((sid) => sid && c.bySlug.has(`summaries/${sid}`))
        .map((sid) => [sid, resolveRelative(from, `summaries/${sid}` as FullSlug)]),
    ),
    findings: Object.fromEntries(all.map((f) => [idOf(f), resolveRelative(from, slugOf(f) as FullSlug)])),
  }
  const empty = (idx.empty_topics ?? []).map((t) => {
    const f = c.bySlug.get(`topics/${t}`)
    return f ? titleOf(f) : t.replace(/-/g, " ")
  })
  const used = new Set(all.map((f) => kindKey(fmOf(f))))
  // The two kinds of new head the first columns as one group, when publish names them.
  const [groupName, ...groupCols] = idx.something_new ?? []
  const groupSpan = groupCols.every((col, i) => cols[i] === col) ? groupCols.length : 0
  return (
    <section class="nvmap" data-novelty aria-label="How new each result is, by topic">
      <div class="sechead">
        <h2>How new is each result?</h2>
        <p>
          Each mark is one result, placed by topic and by what an AI search of PubMed abstracts found for it. The first two columns are
          the two kinds of new. The mark says what kind of result it is.
        </p>
      </div>
      <p class="nvlegend">
        {MARK_WORDS.filter(([k]) => used.has(k)).map(([k, w]) => (
          <span class="nvkey">
            <i class="nd key" data-k={k} aria-hidden="true" />
            {w}
          </span>
        ))}
        {related.ids.size > 0 && (
          <span class="nvkey">
            <i class="nd key rel" data-k="positive" aria-hidden="true" />
            Related result in another project
            <svg width="28" height="10" aria-hidden="true">
              <path d="M1 5 H27" />
            </svg>
            hover a box to draw it
          </span>
        )}
        <span class="nvkey">
          <span class="nbead key" aria-hidden="true">
            <i class="nd" data-k="positive" />
            <i class="nd" data-k="positive" />
          </span>
          One project's results in this cell
        </span>
      </p>
      <div class="nvbox">
        <div class="nvgrid" style={`--nvtpl:minmax(8rem,11rem) ${cols.map((col) => `minmax(3.5rem,${WIDTH[order.indexOf(col)] ?? 1}fr)`).join(" ")}`}>
          {groupSpan > 0 && (
            <>
              <span class="nvgroupcorner" />
              <span class="nvgroup" style={`grid-column: span ${groupSpan}`}>
                {groupName} <span class="n">{cols.slice(0, groupSpan).reduce((n, col) => n + count(col), 0)}</span>
              </span>
              <span class="nvgroup rest" style={`grid-column: span ${cols.length - groupSpan}`}>
                Compared with published work
              </span>
            </>
          )}
          <span class="nvcorner">Topic</span>
          {cols.map((col) => (
            <span class={`nvcolh nv-${TONE[order.indexOf(col)] ?? "none"}`}>
              <i aria-hidden="true" />
              <ColNote col={col} note={idx.compare_notes?.[col]} /> <span class="n">{count(col)}</span>
            </span>
          ))}
          {rows.map((t) => {
            const inRow = all.filter((f) => fmOf(f).topic === topicSlug(t))
            const hue = c.hueOf(t)
            return (
              <>
                <a class="nvrowh" href={resolveRelative(from, slugOf(t) as FullSlug)} style={hue ? `--d:${hue}` : undefined}>
                  {titleOf(t)} <span class="n">{inRow.length}</span>
                </a>
                {cols.map((col) => {
                  const cell = inRow.filter((f) => fmOf(f).compare_text === col)
                  const by = new Map<string, File[]>()
                  for (const f of cell.sort((a, b) => idOf(a).localeCompare(idOf(b)))) {
                    const sid = fmOf(f).source ?? ""
                    by.set(sid, [...(by.get(sid) ?? []), f])
                  }
                  return (
                    <div class="nvcell" data-empty={cell.length === 0 ? "1" : undefined}>
                      <span class={`nvlab nv-${TONE[order.indexOf(col)] ?? "none"}`}>
                        <ColNote col={col} note={idx.compare_notes?.[col]} /> · {cell.length}
                      </span>
                      {[...by.entries()]
                        .sort(([a], [b]) => a.localeCompare(b))
                        .map(([sid, items]) => (
                          <Group sid={sid} items={items} title={idx.project_titles?.[sid] ?? fmOf(items[0]).report_title ?? sid} col={col} related={related.ids} />
                        ))}
                    </div>
                  )
                })}
              </>
            )
          })}
        </div>
      </div>
      {empty.length > 0 && <p class="nvempty">No listed result has {empty.join(", ")} as its main topic yet.</p>}
      <div class="nvpanel" aria-live="polite" hidden />
      <script type="application/json" class="nvdata" dangerouslySetInnerHTML={{ __html: JSON.stringify(data).replace(/</g, "\\u003c") }} />
    </section>
  )
}
