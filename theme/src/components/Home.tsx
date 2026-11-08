// The home page opens on the same three ways in as the top bar: results, open
// questions and topics, each as a door card with its count. One line of
// reference links follows. The map, the topic key and the topics table live on
// the Topics page; the results and questions live on their own pages.
import type { FullSlug } from "@quartz-community/types"
import { resolveRelative, simplifySlug } from "@quartz-community/utils"
import type { Element, ElementContent, Root } from "hast"
import { jsx } from "../jsx"
import { type Corpus, type File, collectionOf, counts, isIndex, sections, slugOf, titleOf } from "../page"
import { directionsOf, findingsOf } from "./Cards"

const plural = (n: number, unit: string) => `${n} ${unit}${n === 1 ? "" : "s"}`
const isEl = (n: ElementContent): n is Element => n.type === "element"

/** The links of the home page's Browse list, minus the ones the reference line already gives. */
function extraLinks(nodes: ElementContent[] | undefined, skip: Set<string>): ElementContent[][] {
  const out: ElementContent[][] = []
  for (const list of nodes ?? []) {
    if (!isEl(list) || (list.tagName !== "ul" && list.tagName !== "ol")) continue
    for (const li of list.children) {
      if (!isEl(li) || li.tagName !== "li") continue
      const a = li.children.find((k): k is Element => isEl(k) && k.tagName === "a")
      const target = String(a?.properties?.["data-slug"] ?? a?.properties?.dataSlug ?? "")
      if (a && !skip.has(simplifySlug(target as FullSlug))) out.push([a])
    }
  }
  return out
}

export function Home({ file, c, tree, standing }: { file: File; c: Corpus; tree: Root; standing: ElementContent[] | null }) {
  const slug = slugOf(file) as FullSlug
  const { byHeading } = sections(tree)
  const n = counts(c)
  const findings = findingsOf(c).length
  const questions = directionsOf(c).length
  const authors = [...c.bySlug.keys()].filter((s) => collectionOf(s) === "authors" && !isIndex(s)).length
  const doors = [
    ...(findings > 0
      ? [
          ["findings/index", "Results", "What the projects found, and how new each result is.", plural(findings, "result")],
          ["directions/index", "Open questions", "What the results leave open, and what answering needs.", plural(questions, "question")],
        ]
      : []),
    ["topics/index", "Topics", findings > 0
        ? `The ${n.topics} research areas, each with its results and questions.`
        : `The ${n.topics} research areas, each with its concepts and reports.`, plural(n.topics, "topic")],
  ] as [string, string, string, string][]
  const reference = (
    [
      ["concepts/index", "Concepts", n.concepts],
      ["entities/index", "Entities", n.entities],
      ["conflicts/index", "Conflicts", n.conflicts],
      ["summaries/index", "Reports", n.reports + n.digests],
      ["authors/index", "Authors", authors],
    ] as [string, string, number][]
  ).filter(([, , count]) => count > 0)
  const also = extraLinks(byHeading.get("browse"), new Set(reference.map(([target]) => simplifySlug(target as FullSlug) as string)))
  return (
    <>
      <section class="band hero">
        <h1>{titleOf(file)}</h1>
        <p class="deck">What the BERIL projects found, what they leave open, and where to look next.</p>
        {standing && <p class="standing">{jsx(standing)}</p>}
        {/* src/client opens section search from this box. */}
        <div class="homesearch">
          <button class="bigsearch px-bigsearch" type="button">
            <svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true">
              <circle cx="8.5" cy="8.5" r="6.5" />
              <path d="M13.5 13.5 18 18" />
            </svg>
            <span>Search every section: a gene, an organism, a method, a claim</span>
            <kbd>/</kbd>
          </button>
          <a class="btn" href={resolveRelative(slug, "ask" as FullSlug)}>
            Ask the wiki
          </a>
        </div>
      </section>
      <section class="band homedoors">
        <nav class="cards doors" aria-label="Ways in">
          {doors.map(([target, label, what, count]) => (
            <a class="card door" href={resolveRelative(slug, target as FullSlug)}>
              <b>{label}</b>
              <span class="desc">{what}</span>
              <span class="meta">
                <span class="n">{count}</span>
              </span>
            </a>
          ))}
        </nav>
        <nav class="reflinks" aria-label="Reference">
          <span class="lbl">Browse the reference:</span>
          {reference.map(([target, label, count], i) => (
            <>
              {i > 0 && <span class="sep" aria-hidden="true">·</span>}
              <a href={resolveRelative(slug, target as FullSlug)}>
                {label} <span class="n">{count}</span>
              </a>
            </>
          ))}
        </nav>
        {also.length > 0 && (
          <nav class="reflinks also" aria-label="More pages">
            <span class="lbl">Also:</span>
            {also.map((link, i) => (
              <>
                {i > 0 && <span class="sep" aria-hidden="true">·</span>}
                {jsx(link)}
              </>
            ))}
          </nav>
        )}
      </section>
    </>
  )
}
