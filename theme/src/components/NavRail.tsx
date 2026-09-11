// Left rail: what you use while reading (contents) and when leaving (graph).
import type { PageFrameProps, QuartzComponentProps } from "@quartz-community/types"
import { slot } from "../jsx"
import type { Corpus, File } from "../page"
import { LocalGraph, neighbours } from "../svg"
import { isKnowledge } from "../ties"

export function NavRail({ cd, file, c, right }: {
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
          <p class="more">
            Neighbours by wikilink, coloured by topic. Round is a synthesis page — concept, topic,
            conflict or cross-project digest; square is a project report.
          </p>
        </section>
      )}
    </aside>
  )
}
