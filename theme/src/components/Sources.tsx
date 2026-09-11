// The reports a page cites, listed once under the prose in citation order.
// The marks in the text are numbers; this is where a number gets its name.
// Same heading as the rail section, because it is the same list: the rail is
// the copy you read beside the prose, this the one you land on from a mark.
import type { FullSlug } from "@quartz-community/types"
import { resolveRelative } from "@quartz-community/utils"
import { citeNote, cited } from "../cites"
import { type Cite, type Corpus, titleOf } from "../page"

export function Sources({ cites, c, from }: { cites: Cite[]; c: Corpus; from: FullSlug }) {
  if (cites.length === 0) return null
  const src = cited(cites, c)
  return (
    <section class="sources">
      <h2>{src.projectsOnly ? "Projects cited" : "Sources cited"}</h2>
      <ol>
        {cites.map((k) => {
          const report = c.bySlug.get(k.slug)
          return (
            <li value={k.num}>
              {/* A summary cites itself through its raw report, so the entry
                  points where the citation in the prose does. */}
              <a href={resolveRelative(from, k.target as FullSlug)}>
                {report ? titleOf(report) : k.label}
              </a>
              <span class="w">
                <code>{k.label}</code> · {citeNote(k, src.isDigest(k))}
              </span>
            </li>
          )
        })}
      </ol>
    </section>
  )
}
