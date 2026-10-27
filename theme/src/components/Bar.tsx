// The top bar: the logo and name, the collections, then the tools: section
// search, Ask, the CBORG key, and the stock theme toggle from the header slot.
// src/client wires the search button, the key button's state and its dialog.
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

// Findings and research directions lead the bar where a preview build publishes
// them; every collection keeps its own entry, so no part of the wiki is hidden.
const RECORDS: [string, string][] = [
  ["Findings", "findings/index"],
  ["Directions", "directions/index"],
]

export function Bar({ cd, header }: { cd: QuartzComponentProps; header: PageFrameProps["header"] }) {
  const slug = cd.fileData.slug as FullSlug
  const here = collectionOf(slug)
  const published = new Set((cd.allFiles ?? []).map((f) => f.slug as string))
  const nav = [...RECORDS.filter(([, target]) => published.has(target)), ...NAV]
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
      <nav aria-label="Collections">
        {nav.map(([label, target]) => (
          <a
            href={resolveRelative(slug, target as FullSlug)}
            aria-current={collectionOf(target) === here && here !== "" ? "page" : undefined}
          >
            {label}
          </a>
        ))}
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
        <button class="px-keybtn" type="button" aria-label="CBORG key">
          <svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <circle cx="6" cy="10" r="3.6" />
            <path d="M9.6 10H18M15 10v3M17.6 10v2.2" />
          </svg>
          <span class="px-keydot" />
        </button>
        {slot(header).map((H) => (
          <H {...cd} />
        ))}
      </div>
    </header>
  )
}
