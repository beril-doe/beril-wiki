// The home page's topic strips. Every strip has one slot per topic, in the same
// order, filled where a result or question touches that topic, so shared topics
// line up down the page. The key above both sections says what a topic is;
// src/client/strips.ts shows its row and lets a reader pick a topic. Without the
// script the strips still open to name their topics.
import type { FullSlug } from "@quartz-community/types"
import { resolveRelative, simplifySlug } from "@quartz-community/utils"
import type { ElementContent } from "hast"
import { jsx } from "../jsx"
import { type Corpus, type File, slugOf, titleOf } from "../page"

const short = (t: File) => slugOf(t).replace(/^topics\//, "")

/** The topics an entry touches, as a space-separated list for `data-topics`. */
export const topicList = (topics: string[] | undefined, primary: string | undefined) =>
  [...new Set([...(primary ? [primary] : []), ...(topics ?? [])])].join(" ")

export function TopicStrip({ c, topics, primary }: { c: Corpus; topics: string[] | undefined; primary?: string }) {
  const on = new Set(topicList(topics, primary).split(" ").filter(Boolean))
  // The main topic leads the list; the rest keep the strip's order.
  const named = c.topics.filter((t) => on.has(short(t))).sort((a, b) => Number(short(b) === primary) - Number(short(a) === primary))
  if (named.length === 0) return null
  return (
    <details class="tstrip">
      <summary>
        <span class="tslots" aria-hidden="true" style={`--topics:${c.topics.length}`}>
          {c.topics.map((t) => {
            const s = short(t)
            return (
              <i
                class={`tslot${on.has(s) ? " on" : ""}${s === primary ? " main" : ""}`}
                data-t={s}
                title={titleOf(t)}
                style={`--h:${c.hue(slugOf(t))}`}
              />
            )
          })}
        </span>
        <span class="tcap">{named.length === 1 ? "1 topic" : `${named.length} topics`}</span>
      </summary>
      {/* The names stay disabled until src/client/strips.ts can act on them. */}
      <ul class="tnames">
        {named.map((t) => (
          <li>
            <button type="button" class="tname" data-t={short(t)} aria-pressed="false" disabled style={`--h:${c.hue(slugOf(t))}`}>
              {titleOf(t)}
            </button>
          </li>
        ))}
      </ul>
    </details>
  )
}

/** The key for every strip on the page: what a topic is, then one button per topic in
 * strip order. Pointing at a button names its topic below the row; clicking it picks
 * the topic. The row and the readout stay hidden until the browser script wires them. */
export function TopicKey({ c, from, blurbs }: { c: Corpus; from: FullSlug; blurbs: Map<string, ElementContent[]> }) {
  return (
    <section class="band" aria-label="Topic strips">
      <div class="tkeybox">
        <p class="tkeylabel">Topic strips</p>
        <p class="tintro">
          The wiki sorts its pages into {c.topics.length} topics, each a broad research area. Every result and question
          below has a strip with one slot per topic, in the order of these colours. A coloured slot is a topic the entry
          touches, and the tall slot is its main topic.
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
            <p class="tidle">Point at a colour to see its topic. Click or tap it to light up the results and questions that share it.</p>
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
              <span class="tkcount" aria-live="polite" />
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
