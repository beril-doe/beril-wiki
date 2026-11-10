// The top bar: the logo and name, the three ways in (results, open questions,
// topics), a Browse menu holding the reference collections, About, then the tools:
// section search, Ask, and the stock theme toggle from the header slot. The
// CBORG key is entered where it is used, on the Ask page and in search.
// src/client wires the search button and the Browse menu.
import type { FullSlug, PageFrameProps, QuartzComponentProps } from "@quartz-community/types"
import { resolveRelative } from "@quartz-community/utils"
import { slot } from "../jsx"
import { collectionOf } from "../page"

// Results and open questions lead the bar when the build has records.
const RECORDS: [string, string][] = [
  ["Results", "findings/index"],
  ["Open questions", "directions/index"],
]
const DOORS: [string, string][] = [["Topics", "topics/index"]]
const BROWSE: [string, string][] = [
  ["Concepts", "concepts/index"],
  ["Entities", "entities/index"],
  ["Conflicts", "conflicts/index"],
  ["Reports", "summaries/index"],
  ["Authors", "authors/index"],
]
// About the wiki is the last site link, pushed right so it sits just before Search.
const ABOUT: [string, string] = ["About", "about"]

// The mark: a dish holding a small knowledge graph. The accent node takes the
// topic blue; everything else follows the ink colour, so it works in both themes.
function Logo() {
  return (
    <svg class="logo" viewBox="0 0 32 32" aria-hidden="true">
      <circle cx="16" cy="16" r="13.5" fill="none" stroke="currentColor" stroke-width="2" />
      <path d="M10.4 20.6 16 10.6l5.6 10" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" />
      <path d="M10.4 20.6h11.2" stroke="currentColor" stroke-width="1.1" stroke-linecap="round" opacity="0.55" />
      <circle cx="10.4" cy="20.6" r="2.7" fill="currentColor" />
      <circle cx="21.6" cy="20.6" r="2.7" fill="currentColor" />
      <circle cx="16" cy="10.6" r="3.1" fill="var(--logo-accent)" />
    </svg>
  )
}

export function Bar({ cd, header }: { cd: QuartzComponentProps; header: PageFrameProps["header"] }) {
  const slug = cd.fileData.slug as FullSlug
  const here = collectionOf(slug)
  const published = new Set((cd.allFiles ?? []).map((f) => f.slug as string))
  const doors = [...RECORDS.filter(([, target]) => published.has(target)), ...DOORS]
  const current = (target: string) => collectionOf(target) === here && here !== ""
  const inBrowse = BROWSE.some(([, target]) => current(target))
  return (
    <header class="bar">
      <a class="wordmark" href={resolveRelative(slug, "index" as FullSlug)} aria-label={`${cd.cfg.pageTitle}, home`}>
        <Logo />
        {/* The stylesheet swaps in the short name where the bar is tight. */}
        <span class="name">
          <span class="full">{cd.cfg.pageTitle}</span>
          <span class="short">BERIL Wiki</span>
        </span>
      </a>
      <nav class="barnav" aria-label="Site">
        {doors.map(([label, target]) => (
          <a class="barlink" href={resolveRelative(slug, target as FullSlug)} aria-current={current(target) ? "page" : undefined}>
            {label}
          </a>
        ))}
        {/* Without the script the list opens while focus is inside the menu. */}
        <div class="barmenu">
          <button
            class={`barmenu-btn${inBrowse ? " here" : ""}`}
            type="button"
            aria-expanded="false"
            aria-controls="barmenu-list"
          >
            Browse
            <svg viewBox="0 0 10 10" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true">
              <path d="M2 3.5 5 6.5 8 3.5" />
            </svg>
          </button>
          <ul class="barmenu-list" id="barmenu-list">
            {BROWSE.map(([label, target]) => (
              <li>
                <a href={resolveRelative(slug, target as FullSlug)} aria-current={current(target) ? "page" : undefined}>
                  {label}
                </a>
              </li>
            ))}
          </ul>
        </div>
        <a class="barlink barabout" href={resolveRelative(slug, ABOUT[1] as FullSlug)} aria-current={current(ABOUT[1]) ? "page" : undefined}>
          {ABOUT[0]}
        </a>
      </nav>
      <div class="tools">
        <button class="search-button" type="button" aria-label="Search the wiki">
          <svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true">
            <circle cx="8.5" cy="8.5" r="6.5" />
            <path d="M13.5 13.5 18 18" />
          </svg>
          <span>Search</span>
          <kbd>/</kbd>
        </button>
        <a class="askbtn" href={resolveRelative(slug, "ask" as FullSlug)} aria-current={slug === "ask" ? "page" : undefined} title="Ask the wiki a question">
          <svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round" aria-hidden="true">
            <path d="M3.5 4.5h13v9h-7l-3.5 3v-3h-2.5z" />
            <path d="M7 8.2h6M7 10.8h4" stroke-linecap="round" />
          </svg>
          <span>Ask</span>
        </a>
        {slot(header).map((H) => (
          <H {...cd} />
        ))}
      </div>
    </header>
  )
}
