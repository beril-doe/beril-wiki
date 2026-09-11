// The top bar: wordmark, the collections, and the stock tools (search, theme
// toggle) that arrive through the header slot.
import type { FullSlug, PageFrameProps, QuartzComponentProps } from "@quartz-community/types"
import { resolveRelative } from "@quartz-community/utils"
import { slot } from "../jsx"
import { collectionOf } from "../page"

const NAV: [string, string][] = [
  ["Topics", "topics/index"],
  ["Concepts", "concepts/index"],
  ["Entities", "entities/index"],
  ["Conflicts", "conflicts/index"],
  ["Reports", "summaries/index"],
  ["Authors", "authors/index"],
  ["About", "about"],
]

export function Bar({ cd, header }: { cd: QuartzComponentProps; header: PageFrameProps["header"] }) {
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
