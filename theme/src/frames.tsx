// The BERIL page frame. One frame for every page type: a top bar, a record
// header that states what the page is and what it rests on, the prose, and two
// rails: contents and neighbourhood on the left, evidence on the right. The
// home page swaps the record for the corpus in figures and a map of it, and a
// collection index swaps the prose for a listing of what the collection holds.
//
// Stock components (search, dark mode, table of contents, footer) arrive
// through the layout slots; everything else is rendered here from page data.
// Each region is its own component under ./components; this file only decides
// which of the three layouts a page gets.
import type { FullSlug, PageFrame } from "@quartz-community/types"
import type { Root } from "hast"
import { Bar } from "./components/Bar"
import { EvidenceRail } from "./components/EvidenceRail"
import { Home } from "./components/Home"
import { Listing, indexFigures } from "./components/Listing"
import { NavRail } from "./components/NavRail"
import { Record } from "./components/Record"
import { Sources } from "./components/Sources"
import { slot } from "./jsx"
import { type File, corpus, isIndex, slugOf, stripIndexLists, walk } from "./page"
import { ties } from "./ties"

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
    // The page's topic colour, handed to the stylesheet for the one place
    // colour enters the chrome: the tick before each section label.
    const accent = c.hueOf(file)
    const prose = (
      <>
        {slot(beforeBody).map((B) => (
          <B {...cd} />
        ))}
        {slot([Content]).map((C) => (
          <C {...cd} />
        ))}
      </>
    )
    return (
      <>
        <Bar cd={cd} header={header} />
        {home ? (
          <Home file={file} c={c} tree={tree} standing={w.standing} />
        ) : index ? (
          <main class="band index-page" style={accent ? `--accent:${accent}` : undefined}>
            <Record file={file} c={c} terms={w.terms} standing={w.standing} orcid={w.orcid} cites={w.cites} rels={w.rels} t={t} figures={indexFigures(file, c)} />
            <div class="prose">{prose}</div>
            <Listing file={file} c={c} />
          </main>
        ) : (
          <main class="page-grid" style={accent ? `--accent:${accent}` : undefined}>
            <Record file={file} c={c} terms={w.terms} standing={w.standing} orcid={w.orcid} cites={w.cites} rels={w.rels} t={t} />
            <NavRail cd={cd} file={file} c={c} right={right} />
            <div class="prose">
              {prose}
              <Sources cites={w.cites} c={c} from={slug as FullSlug} />
              {slot(afterBody).map((A) => (
                <A {...cd} />
              ))}
            </div>
            <EvidenceRail cd={cd} file={file} c={c} cites={w.cites} t={t} left={left} />
          </main>
        )}
        {slot(footer).map((F) => (
          <F {...cd} />
        ))}
      </>
    )
  },
}
