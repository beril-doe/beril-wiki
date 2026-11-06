// The Results picture: how each result compares with PubMed, most novel first, by
// topic, with each project's results grouped. Links between projects are drawn only
// when a reader hovers, focuses or taps a group (src/client/novelty.ts); the links
// and project names come from the results index page that publish/cards.py wrote.
import type { FullSlug } from "@quartz-community/types"
import { resolveRelative } from "@quartz-community/utils"
import { type Corpus, type File, slugOf, titleOf } from "../page"
import { type FindingFm, findingsOf, resultsIndex } from "./Cards"

const fmOf = (f: File) => (f.frontmatter ?? {}) as FindingFm
const topicSlug = (t: File) => slugOf(t).replace(/^topics\//, "")
const idOf = (f: File) => slugOf(f).replace(/^findings\//, "")

// Colour by comparison column, in the order publish gives: no close match, builds on,
// differs, similar, too little evidence, not compared yet.
const TONE = ["new", "builds", "match", "match", "none", "unset"]
// Column widths follow the usual counts: the "too little evidence" column holds most results.
const WIDTH = [1.1, 1.4, 0.6, 0.6, 2.2, 0.8]

/** One project's results in one cell: the group is the button; the dots are its results. */
function Group({ sid, items, tone, title, col }: { sid: string; items: File[]; tone: string; title: string; col: string }) {
  return (
    <button type="button" class={`nbead nv-${tone}`} data-p={sid} aria-label={`${title}: ${items.length} ${items.length === 1 ? "result" : "results"}, ${col}`}>
      {items.map((f) => {
        const m = fmOf(f)
        return <i class="nd" data-id={idOf(f)} data-t={titleOf(f)} data-g={m.gist ?? ""} data-r={m.report_title ?? sid} aria-hidden="true" />
      })}
    </button>
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
  const data = {
    links: idx.links ?? [],
    titles: idx.project_titles ?? {},
    hrefs: Object.fromEntries(Object.keys(idx.project_titles ?? {}).map((sid) => [sid, resolveRelative(from, `summaries/${sid}` as FullSlug)])),
    findings: Object.fromEntries(all.map((f) => [idOf(f), resolveRelative(from, slugOf(f) as FullSlug)])),
  }
  const empty = (idx.empty_topics ?? []).map((t) => {
    const f = c.bySlug.get(`topics/${t}`)
    return f ? titleOf(f) : t.replace(/-/g, " ")
  })
  return (
    <section class="nvmap" data-novelty aria-label="Results by how they compare with PubMed, by topic">
      <div class="sechead">
        <h2>Every result, by topic</h2>
        <p>Each dot is one result, placed by topic and by how it compares with PubMed abstracts.</p>
      </div>
      <p class="nvlegend">
        <span class="nvkey">
          <svg width="28" height="10" aria-hidden="true">
            <path d="M1 5 H27" />
          </svg>
          Related results
        </span>
        <span class="nvkey">
          <svg width="28" height="10" aria-hidden="true">
            <path d="M1 5 H27" stroke-dasharray="5 3" />
          </svg>
          Cited by the same open question
        </span>
        <span class="nvkey">
          <svg width="28" height="10" aria-hidden="true">
            <path d="M1 5 H27" stroke-dasharray="1.5 3" />
          </svg>
          One project uses or cites another
        </span>
        <span class="nvhint">Hover a group to see its links. Click it to list them.</span>
      </p>
      <div class="nvbox">
        <div class="nvgrid" style={`--nvtpl:minmax(8rem,11rem) ${cols.map((col) => `minmax(3.5rem,${WIDTH[order.indexOf(col)] ?? 1}fr)`).join(" ")}`}>
          <span class="nvcorner" />
          {cols.map((col) => (
            <span class={`nvcolh nv-${TONE[order.indexOf(col)]}`}>
              <i aria-hidden="true" />
              {col} <span class="n">{count(col)}</span>
            </span>
          ))}
          {rows.map((t) => {
            const inRow = all.filter((f) => fmOf(f).topic === topicSlug(t))
            return (
              <>
                <a class="nvrowh" href={resolveRelative(from, slugOf(t) as FullSlug)}>
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
                      <span class="nvlab">
                        {col} · {cell.length}
                      </span>
                      {[...by.entries()]
                        .sort(([a], [b]) => a.localeCompare(b))
                        .map(([sid, items]) => (
                          <Group sid={sid} items={items} tone={TONE[order.indexOf(col)]} title={idx.project_titles?.[sid] ?? fmOf(items[0]).report_title ?? sid} col={col} />
                        ))}
                    </div>
                  )
                })}
              </>
            )
          })}
        </div>
      </div>
      {empty.length > 0 && <p class="nvempty">No results are filed under {empty.join(", ")} yet.</p>}
      <div class="nvpanel" aria-live="polite" hidden />
      <script type="application/json" class="nvdata" dangerouslySetInnerHTML={{ __html: JSON.stringify(data).replace(/</g, "\\u003c") }} />
    </section>
  )
}
