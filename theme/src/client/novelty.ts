// The Results picture in the browser. Links between projects are never drawn all at
// once: hovering or focusing a project's group draws its links, a click or Enter pins
// it and lists every link below the picture, and Escape clears. Phones draw no lines;
// the list opens under the tapped cell instead. Every string from the data is set with
// textContent, never as HTML.

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

  // A dot's result on hover, for pointers that hover.
  map.querySelector(".nvtip")?.remove()
  panel.hidden = true
  clear()
  const tip = el("div", "nvtip")
  tip.setAttribute("role", "tooltip")
  tip.hidden = true
  map.appendChild(tip)
  map.addEventListener(
    "pointerover",
    (e) => {
    const dot = (e.target as HTMLElement).closest<HTMLElement>(".nd")
    if (!dot || (e as PointerEvent).pointerType === "touch") return
    tip.replaceChildren(el("strong", undefined, dot.dataset.t ?? ""))
    if (dot.dataset.g) tip.appendChild(el("span", undefined, dot.dataset.g))
    tip.appendChild(el("span", "nvtipsrc", dot.dataset.r ?? ""))
    tip.hidden = false
    const r = dot.getBoundingClientRect()
    const w = tip.offsetWidth
    const h = tip.offsetHeight
    tip.style.left = `${Math.max(8, Math.min(r.left, window.innerWidth - w - 8))}px`
    tip.style.top = `${r.bottom + 8 + h > window.innerHeight ? r.top - h - 8 : r.bottom + 8}px`
    },
    { signal },
  )
  map.addEventListener(
    "pointerout",
    (e) => {
      if ((e.target as HTMLElement).closest(".nd")) tip.hidden = true
    },
    { signal },
  )
  window.addEventListener("scroll", () => (tip.hidden = true), { passive: true, signal })
}

// Quartz's navigation reuses nodes and strips data attributes; one signal per page lets
// the next page drop these listeners before wiring its own.
let wiring: AbortController | null = null

export function wireNovelty() {
  wiring?.abort()
  wiring = new AbortController()
  for (const map of document.querySelectorAll<HTMLElement>("[data-novelty]")) wireMap(map, wiring.signal)
}
