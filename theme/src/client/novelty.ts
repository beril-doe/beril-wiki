// The Results picture in the browser. Links between projects are never drawn all at
// once: hovering or focusing a project's group draws its links, a click on the group's
// edge or Enter pins it and lists every link below the picture, and Escape clears. A click
// on a dot pins that result's card instead. Phones draw no lines;
// the list opens under the tapped cell instead. Every string from the data is set with
// textContent, never as HTML.

import { AIM_MS, LEAVE_MS, type Point, towards } from "./aim"

interface Link {
  a?: string
  b?: string
  pa: string
  pb: string
  family: "r" | "q" | "p"
  label?: string
  questions?: string[]
}

interface Data {
  links: Link[]
  titles: Record<string, string>
  hrefs: Record<string, string>
  findings: Record<string, string>
}

const FAMILY: Record<Link["family"], string> = {
  r: "Related results",
  q: "Cited by the same open question",
  p: "One project uses or cites another",
}
const NARROW = "(max-width: 700px)"
const NS = "http://www.w3.org/2000/svg"

function el<K extends keyof HTMLElementTagNameMap>(tag: K, cls?: string, text?: string): HTMLElementTagNameMap[K] {
  const node = document.createElement(tag)
  if (cls) node.className = cls
  if (text !== undefined) node.textContent = text
  return node
}

function wireMap(map: HTMLElement, signal: AbortSignal) {
  const raw = map.querySelector(".nvdata")?.textContent
  const box = map.querySelector<HTMLElement>(".nvbox")
  const panel = map.querySelector<HTMLElement>(".nvpanel")
  if (!raw || !box || !panel) return
  const data = JSON.parse(raw) as Data
  const groups = [...map.querySelectorAll<HTMLButtonElement>(".nbead")]
  const narrow = window.matchMedia(NARROW)
  const byProject = new Map<string, HTMLButtonElement[]>()
  const ofFinding = new Map<string, HTMLButtonElement>()
  for (const g of groups) {
    const sid = g.dataset.p ?? ""
    byProject.set(sid, [...(byProject.get(sid) ?? []), g])
    for (const dot of g.querySelectorAll<HTMLElement>(".nd")) ofFinding.set(dot.dataset.id ?? "", g)
  }
  // A project link ends at the project's largest group.
  const main = (sid: string) => (byProject.get(sid) ?? []).reduce<HTMLButtonElement | undefined>((best, g) => (!best || g.childElementCount > best.childElementCount ? g : best), undefined)
  const end = (finding: string | undefined, sid: string) => (finding ? ofFinding.get(finding) : main(sid))
  const titleOf = (sid: string) => data.titles[sid] ?? byProject.get(sid)?.[0]?.getAttribute("aria-label")?.split(":")[0] ?? sid
  let pinned: string | null = null
  let pinnedGroup: HTMLButtonElement | null = null

  function clear() {
    box!.querySelector("svg.nvlinks")?.remove()
    box!.classList.remove("sel")
    for (const g of groups) g.classList.remove("me", "nb")
  }

  function draw(sid: string) {
    clear()
    box!.classList.add("sel")
    for (const g of byProject.get(sid) ?? []) g.classList.add("me")
    const mine = data.links.filter((l) => l.pa === sid || l.pb === sid)
    const frame = box!.getBoundingClientRect()
    const svg = document.createElementNS(NS, "svg")
    svg.setAttribute("class", "nvlinks")
    svg.setAttribute("width", String(box!.scrollWidth))
    svg.setAttribute("height", String(box!.scrollHeight))
    svg.setAttribute("aria-hidden", "true")
    for (const l of mine) {
      const a = end(l.a, l.pa)
      const b = end(l.b, l.pb)
      for (const g of [a, b]) if (g && g.dataset.p !== sid) g.classList.add("nb")
      if (!a || !b || a === b || narrow.matches) continue
      const ra = a.getBoundingClientRect()
      const rb = b.getBoundingClientRect()
      const x1 = ra.left + ra.width / 2 - frame.left + box!.scrollLeft
      const y1 = ra.top + ra.height / 2 - frame.top + box!.scrollTop
      const x2 = rb.left + rb.width / 2 - frame.left + box!.scrollLeft
      const y2 = rb.top + rb.height / 2 - frame.top + box!.scrollTop
      const dx = x2 - x1
      const dy = y2 - y1
      const len = Math.hypot(dx, dy) || 1
      const bend = Math.min(60, len * 0.18)
      const path = document.createElementNS(NS, "path")
      path.setAttribute("d", `M${x1},${y1} Q${(x1 + x2) / 2 - (dy / len) * bend},${(y1 + y2) / 2 + (dx / len) * bend} ${x2},${y2}`)
      path.setAttribute("class", l.family)
      svg.appendChild(path)
    }
    box!.appendChild(svg)
  }

  function list(sid: string, from: HTMLButtonElement) {
    panel!.replaceChildren()
    panel!.appendChild(el("h4", undefined, titleOf(sid)))
    const results = el("ul", "nvresults")
    for (const dot of from.querySelectorAll<HTMLElement>(".nd")) {
      const li = el("li")
      const a = el("a", undefined, dot.dataset.t ?? "")
      a.href = data.findings[dot.dataset.id ?? ""] ?? "#"
      li.appendChild(a)
      results.appendChild(li)
    }
    panel!.appendChild(el("p", "nvsub", "Results in this group"))
    panel!.appendChild(results)
    const mine = data.links.filter((l) => l.pa === sid || l.pb === sid)
    if (mine.length === 0) panel!.appendChild(el("p", "nvsub", "No link to another project yet."))
    for (const family of ["r", "q", "p"] as const) {
      const items = new Map<string, Set<string>>()
      for (const l of mine.filter((x) => x.family === family)) {
        const other = l.pa === sid ? l.pb : l.pa
        const lines = items.get(other) ?? new Set<string>()
        if (family === "q") for (const q of l.questions ?? []) lines.add(`Question: ${q}`)
        else if (family === "p") lines.add(`${l.pa === sid ? "This project" : titleOf(l.pa)}: ${l.label ?? ""}`)
        else lines.add(l.label ?? "")
        items.set(other, lines)
      }
      if (items.size === 0) continue
      panel!.appendChild(el("p", "nvfam", `${FAMILY[family]} · ${items.size}`))
      const ul = el("ul", "nvlist")
      for (const [other, lines] of items) {
        const li = el("li")
        if (byProject.has(other)) {
          const go = el("button", "nvgo", titleOf(other))
          go.type = "button"
          go.dataset.go = other
          li.appendChild(go)
        } else {
          const a = el("a", undefined, `${titleOf(other)} (no results in this picture)`)
          a.href = data.hrefs[other] ?? "#"
          li.appendChild(a)
        }
        for (const line of lines) if (line) li.appendChild(el("span", "nvline", line))
        ul.appendChild(li)
      }
      panel!.appendChild(ul)
    }
    panel!.hidden = false
    place(from)
  }

  function place(from: HTMLButtonElement | null) {
    if (narrow.matches && from) from.closest(".nvcell")?.after(panel!)
    else box!.after(panel!)
  }

  function pin(g: HTMLButtonElement) {
    pinned = g.dataset.p ?? ""
    pinnedGroup = g
    draw(pinned)
    list(pinned, g)
  }

  function unpin() {
    pinned = null
    pinnedGroup = null
    clear()
    panel!.hidden = true
  }

  const restore = () => (pinned ? draw(pinned) : clear())
  for (const g of groups) {
    g.addEventListener("pointerenter", () => draw(g.dataset.p ?? ""), { signal })
    g.addEventListener("pointerleave", restore, { signal })
    g.addEventListener("focus", () => draw(g.dataset.p ?? ""), { signal })
    g.addEventListener("blur", restore, { signal })
    g.addEventListener("click", () => pin(g), { signal })
  }
  panel.addEventListener(
    "click",
    (e) => {
    const go = (e.target as HTMLElement).closest<HTMLButtonElement>("[data-go]")
    const target = go ? main(go.dataset.go ?? "") : undefined
    if (!target) return
    pin(target)
    target.focus({ preventScroll: true })
    target.scrollIntoView({ block: "nearest", inline: "nearest" })
    },
    { signal },
  )
  map.addEventListener(
    "keydown",
    (e) => {
      if (e.key !== "Escape" || pinned === null) return
      const back = pinnedGroup
      unpin()
      back?.focus()
    },
    { signal },
  )
  window.addEventListener(
    "resize",
    () => {
      if (pinned && map.isConnected) {
        draw(pinned)
        place(pinnedGroup)
      }
    },
    { signal },
  )

  // A dot's result in a card, in the questions grid's model. A hover opens a card that stays
  // while the pointer is on the dot or the card. A click or tap pins a second card that
  // stays through other hovers until Escape, a press outside, or a second click.
  for (const old of map.querySelectorAll(".nvtip")) old.remove()
  panel.hidden = true
  clear()
  const tip = el("div", "nvtip")
  const pinCard = el("div", "nvtip pin")
  tip.hidden = true
  pinCard.hidden = true
  map.append(tip, pinCard)
  const dotOf = (t: EventTarget | null) => (t as HTMLElement | null)?.closest?.<HTMLElement>(".nd") ?? null
  let tipDot: HTMLElement | null = null
  let pinDot: HTMLElement | null = null
  let apex: Point | null = null
  // The pointer's last position, and its last position over the shown dot. An event that
  // leaves the dot reports where the pointer landed, which after a jump is the next dot.
  let last: Point = { x: 0, y: 0 }
  let onDot: Point | null = null
  let hideTimer = 0

  function fill(card: HTMLElement, dot: HTMLElement) {
    card.replaceChildren(el("strong", undefined, dot.dataset.t ?? ""))
    if (dot.dataset.g) card.appendChild(el("span", undefined, dot.dataset.g))
    card.appendChild(el("span", "nvtipsrc", dot.dataset.r ?? ""))
    const open = el("a", "nvopen", "Open the result")
    open.href = data.findings[dot.dataset.id ?? ""] ?? "#"
    card.appendChild(open)
  }

  function placeCard(card: HTMLElement, dot: HTMLElement | null) {
    if (!dot || card.hidden) return
    // Measured at the left edge: a fixed card near the right edge shrinks to fit.
    card.style.left = "0px"
    const r = dot.getBoundingClientRect()
    card.style.left = `${Math.max(8, Math.min(r.left, window.innerWidth - card.offsetWidth - 8))}px`
    // Height is read at the final left: a narrower card wraps taller and would cover its dot.
    const h = card.offsetHeight
    // The card touches its dot, so no gap ends the hover on the way in.
    card.style.top = `${r.bottom + h > window.innerHeight - 8 ? r.top - h : r.bottom}px`
  }

  function hideTip() {
    window.clearTimeout(hideTimer)
    apex = null
    tip.hidden = true
    tipDot = null
  }

  // When the wait ends, the dot under the pointer, if any, takes over.
  function hideIn(ms: number) {
    window.clearTimeout(hideTimer)
    hideTimer = window.setTimeout(() => {
      const shown = tipDot
      hideTip()
      const dot = dotOf(document.elementFromPoint(last.x, last.y))
      if (dot && dot !== shown) showTip(dot)
    }, ms)
  }

  const aimed = (p: Point) => !!apex && !tip.hidden && towards(apex, tip.getBoundingClientRect(), p)

  function showTip(dot: HTMLElement) {
    window.clearTimeout(hideTimer)
    apex = null
    onDot = null
    if (dot === pinDot) return hideTip()
    if (dot === tipDot && !tip.hidden) return
    tipDot = dot
    fill(tip, dot)
    tip.hidden = false
    placeCard(tip, dot)
  }

  function pinTo(dot: HTMLElement | null) {
    hideTip()
    pinDot = dot
    pinCard.hidden = !dot
    if (!dot) return
    fill(pinCard, dot)
    placeCard(pinCard, dot)
  }

  map.addEventListener(
    "pointerover",
    (e) => {
      const dot = dotOf(e.target)
      const pe = e as PointerEvent
      if (!dot || pe.pointerType === "touch") return
      if (dot === tipDot) {
        window.clearTimeout(hideTimer)
        apex = null
      } else if (!aimed({ x: pe.clientX, y: pe.clientY })) showTip(dot)
    },
    { signal },
  )
  map.addEventListener(
    "pointerout",
    (e) => {
      const pe = e as PointerEvent
      if (dotOf(e.target) !== tipDot || !tipDot || tip.contains(pe.relatedTarget as Node | null)) return
      apex = onDot ?? { x: pe.clientX, y: pe.clientY }
      hideIn(AIM_MS)
      const next = dotOf(pe.relatedTarget)
      if (next && !aimed({ x: pe.clientX, y: pe.clientY })) showTip(next)
    },
    { signal },
  )
  document.addEventListener(
    "pointermove",
    (e) => {
      last = { x: e.clientX, y: e.clientY }
      if (tipDot && dotOf(e.target) === tipDot) onDot = last
      if (!apex || tip.hidden || aimed(last)) return
      apex = null
      const dot = dotOf(e.target)
      if (dot && dot !== tipDot) showTip(dot)
      else if (!dot) hideIn(LEAVE_MS)
    },
    { signal },
  )
  tip.addEventListener(
    "pointerenter",
    () => {
      window.clearTimeout(hideTimer)
      apex = null
    },
    { signal },
  )
  tip.addEventListener(
    "pointerleave",
    (e) => {
      if (!dotOf(e.relatedTarget)) hideIn(LEAVE_MS)
    },
    { signal },
  )
  // Capture, so a click on a dot pins its card without also pinning its project's links.
  // Enter on a focused group targets the group itself and still lists its links.
  map.addEventListener(
    "click",
    (e) => {
      const dot = dotOf(e.target)
      if (!dot) return
      e.stopPropagation()
      pinTo(dot === pinDot ? null : dot)
    },
    { signal, capture: true },
  )
  document.addEventListener(
    "pointerdown",
    (e) => {
      const t = e.target as Node
      if (!tip.contains(t) && !pinCard.contains(t) && !dotOf(t)) {
        hideTip()
        pinTo(null)
      }
    },
    { signal },
  )
  document.addEventListener(
    "keydown",
    (e) => {
      if (e.key !== "Escape") return
      hideTip()
      pinTo(null)
    },
    { signal },
  )
  const follow = () => placeCard(pinCard, pinDot)
  window.addEventListener(
    "scroll",
    () => {
      hideTip()
      follow()
    },
    { passive: true, signal },
  )
  window.addEventListener("resize", follow, { signal })
}

// Quartz's navigation reuses nodes and strips data attributes; one signal per page lets
// the next page drop these listeners before wiring its own.
let wiring: AbortController | null = null

export function wireNovelty() {
  wiring?.abort()
  wiring = new AbortController()
  for (const map of document.querySelectorAll<HTMLElement>("[data-novelty]")) wireMap(map, wiring.signal)
}
