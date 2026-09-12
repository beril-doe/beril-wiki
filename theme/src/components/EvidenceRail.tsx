// Right rail: what the page rests on and what rests on it.
import type { FullSlug, PageFrameProps, QuartzComponentProps } from "@quartz-community/types"
import type { JSX } from "preact"
import { resolveRelative } from "@quartz-community/utils"
import { citeNote, cited, dotOf } from "../cites"
import { slot } from "../jsx"
import { type Cite, type Corpus, type File, kindOf, slugOf, titleOf } from "../page"
import type { Ties } from "../ties"

const MAX_LIST = 8

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

export function EvidenceRail({ cd, file, c, cites, t, left }: {
  cd: QuartzComponentProps
  file: File
  c: Corpus
  cites: Cite[]
  t: Ties
  left: PageFrameProps["left"]
}) {
  const slug = slugOf(file) as FullSlug
  const rel = (x: string) => resolveRelative(slug, x as FullSlug)
  const topic = kindOf(file).cls === "topic"
  const src = cited(cites, c)
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
          <h3>{src.projectsOnly ? "Projects cited" : "Sources cited"}</h3>
          <p class="more lead">
            What this page draws on: {src.summary}. The numbers are the marks in the text.
          </p>
          <Rows
            rows={cites.map((k) => {
              const dot = dotOf(k)
              const report = c.bySlug.get(k.slug)
              return (
                <li class="cite" style={dot ? `--d:${dot}` : undefined}>
                  <span class="cnum">{k.num}</span>
                  <span>
                    <a href={rel(k.target)}>{report ? titleOf(report) : k.label}</a>
                    <span class="w">
                      <code>{k.label}</code> · {citeNote(k, src.isDigest(k))}
                    </span>
                  </span>
                </li>
              )
            })}
          />
          <p class="more">
            The number is tinted with the relation the prose states; black is the primary source.
            The strip in the header says the same, one block per report.
          </p>
        </section>
      )}
      {t.concepts.length > 0 && (
        <section>
          <h3>{topic ? "Concepts in this topic" : "Concepts linked"}</h3>
          <p class="more lead">
            {topic
              ? "The synthesis pages this topic gathers."
              : "Other synthesis pages this one points at."}
          </p>
          <Rows
            rows={t.concepts.map((f) => {
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
          <h3>Linked from</h3>
          {/* Not "pages that rest on this one": the publish step writes a
              "Feeds into" line onto every summary, so a report this page cites
              links back to it and lands here. Naming a direction would have
              every concept page claim the four reports it rests on rest on it
              instead. The link is the fact; which way the evidence runs is
              what "Projects cited" above says. */}
          <p class="more lead">Pages that link to this one.</p>
          <Rows
            rows={t.citedBy.map((f) => {
              const hue = c.hueOf(f)
              // A list mixing concepts, topics and reports under bare titles
              // says nothing about what any row is; the kind goes with it.
              return (
                <li style={hue ? `--d:${hue}` : undefined}>
                  <span>
                    <a href={rel(slugOf(f))}>{titleOf(f)}</a>
                    <span class="w">{kindOf(f).label}</span>
                  </span>
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
