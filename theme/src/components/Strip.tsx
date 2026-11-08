// The topic key on the Topics page: one coloured slot per topic. Pointing at a slot
// names its topic; picking one lights its cluster on the map below
// (src/client/strips.ts).
import type { FullSlug } from "@quartz-community/types"
import { resolveRelative, simplifySlug } from "@quartz-community/utils"
import type { ElementContent } from "hast"
import { jsx } from "../jsx"
import { type Corpus, type File, slugOf, titleOf } from "../page"

const short = (t: File) => slugOf(t).replace(/^topics\//, "")

/** What a topic is, then one button per topic. Pointing at a button names its topic
 * below the row; clicking it picks the topic. The row and the readout stay hidden until
 * the browser script wires them. */
export function TopicKey({ c, from, blurbs }: { c: Corpus; from: FullSlug; blurbs: Map<string, ElementContent[]> }) {
  return (
    <section class="band" aria-label="Topic colours">
      <div class="tkeybox">
        <p class="tkeylabel">Topic colours</p>
        <p class="tintro">
          The wiki sorts its pages into {c.topics.length} topics, each a broad research area, and gives each topic a colour.
        </p>
        <div class="tkey" data-tkey hidden>
          <span class="tkeyslots" role="group" aria-label="Pick a topic" style={`--topics:${c.topics.length}`}>
            {c.topics.map((t) => (
              <button
                type="button"
                class="tkeyslot"
                data-t={short(t)}
                aria-pressed="false"
                aria-label={titleOf(t)}
                title={titleOf(t)}
                style={`--h:${c.hue(slugOf(t))}`}
              />
            ))}
          </span>
          <div class="tread">
            <p class="tidle">Point at a colour to see its topic. Click or tap it to light up the topic on the map.</p>
            {c.topics.map((t) => {
              const blurb = blurbs.get(simplifySlug(slugOf(t)))
              return (
                <div class="tinfo" data-t={short(t)} style={`--h:${c.hue(slugOf(t))}`} hidden>
                  <p>
                    <a href={resolveRelative(from, slugOf(t) as FullSlug)}>{titleOf(t)}</a>
                    {blurb && <span class="tabout"> {jsx(blurb)}</span>}
                  </p>
                </div>
              )
            })}
            <p class="tstate" hidden>
              <button type="button" class="tmapgo" hidden>
                See it on the map
              </button>
              <button type="button" class="tclear">
                Show all
              </button>
            </p>
          </div>
        </div>
      </div>
    </section>
  )
}
