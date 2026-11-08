// The open-questions grid in the browser. The dots are links and the grid reads
// without this script. Here a hover or keyboard focus shows a dot's pop-up inside
// the viewport, and it stays while the pointer is on the dot or the pop-up; a click
// or tap pins it open, and a second click or tap on the same dot, Escape, or a press
// outside closes it. The pop-up's "Open the question" link navigates; Enter on a
// focused dot follows the dot's own link. The Results picture (novelty.ts) follows
// the same model.

import { AIM_MS, LEAVE_MS, type Point, towards } from "./aim"

const MARGIN = 8

function place(wrap: HTMLElement) {
  const dot = wrap.querySelector<HTMLElement>(".qdot")
  const pop = wrap.querySelector<HTMLElement>(".qpop")
  if (!dot || !pop) return
  pop.style.position = "fixed"
  pop.style.bottom = "auto"
  pop.style.maxHeight = ""
  pop.style.overflowY = ""
  const r = dot.getBoundingClientRect()
  const w = pop.offsetWidth
  const left = Math.max(MARGIN, Math.min(r.left + r.width / 2 - w / 2, window.innerWidth - w - MARGIN))
  pop.style.left = `${left}px`
  // Above when it fits, else below; a pop-up taller than both scrolls on the roomier side
  // instead of covering its dot, so a second tap on the dot still reaches the dot.
  const natural = pop.offsetHeight
  const roomAbove = r.top - MARGIN
  const roomBelow = window.innerHeight - r.bottom - MARGIN
  const above = natural <= roomAbove || (natural > roomBelow && roomAbove > roomBelow)
  const room = Math.max(0, above ? roomAbove : roomBelow)
  if (natural > room) {
    pop.style.maxHeight = `${room}px`
    pop.style.overflowY = "auto"
  }
  const h = Math.min(natural, room)
  // The pop-up overlaps the dot's tap area by a pixel: any gap ends the hover on the way
  // in, and a scrolling pop-up clips the CSS bridges that would cover one.
  pop.style.top = `${above ? r.top - h + 1 : r.bottom - 1}px`
}

const SHOWING = ".qd[data-open], .qd[data-focused], .qd[data-hover]"

function closeAll(except?: Element) {
  for (const d of document.querySelectorAll<HTMLElement>(".qd[data-open]")) if (d !== except) delete d.dataset.open
}

let wired = false
export function wireQuestions() {
  if (wired) return
  wired = true
  const wrapOf = (t: EventTarget | null) => (t as HTMLElement | null)?.closest?.<HTMLElement>(".qd") ?? null
  // Hover lives in data-hover, not :hover, so the pop-up follows aim.ts: it stays while the
  // pointer travels from the dot into it, past neighbouring dots. CSS :hover remains the
  // fallback without this script.
  document.documentElement.dataset.qhover = "1"
  let hovered: HTMLElement | null = null
  let apex: Point | null = null
  // The pointer's last position, and its last position over the hovered dot. An event that
  // leaves the dot reports where the pointer landed, which after a jump is the next dot.
  let last: Point = { x: 0, y: 0 }
  let onDot: Point | null = null
  let hideT = 0
  const hover = (w: HTMLElement | null) => {
    window.clearTimeout(hideT)
    apex = null
    onDot = null
    if (hovered && hovered !== w) delete hovered.dataset.hover
    hovered = w
    if (w) {
      w.dataset.hover = "1"
      place(w)
    }
  }
  // When the wait ends, the dot under the pointer, if any, takes over.
  const hideIn = (ms: number) => {
    window.clearTimeout(hideT)
    hideT = window.setTimeout(() => {
      const w = wrapOf(document.elementFromPoint(last.x, last.y))
      hover(w && w !== hovered ? w : null)
    }, ms)
  }
  const aimed = (p: Point) => {
    const pop = hovered?.querySelector(".qpop")
    return !!apex && !!pop && towards(apex, pop.getBoundingClientRect(), p)
  }
  document.addEventListener("pointerover", (e) => {
    const w = wrapOf(e.target)
    const pe = e as PointerEvent
    if (!w || pe.pointerType === "touch") return
    if (w === hovered) {
      window.clearTimeout(hideT)
      apex = null
    } else if (!hovered?.isConnected || !aimed({ x: pe.clientX, y: pe.clientY })) hover(w)
  })
  document.addEventListener("pointerout", (e) => {
    const w = wrapOf(e.target)
    const pe = e as PointerEvent
    if (!w || w !== hovered || w.contains(pe.relatedTarget as Node | null)) return
    // Only a pointer leaving the dot is on its way to the pop-up; one leaving the pop-up is done.
    if ((e.target as HTMLElement).closest(".qpop")) return hideIn(LEAVE_MS)
    apex = onDot ?? { x: pe.clientX, y: pe.clientY }
    hideIn(AIM_MS)
    const next = wrapOf(pe.relatedTarget)
    if (next && !aimed({ x: pe.clientX, y: pe.clientY })) hover(next)
  })
  document.addEventListener("pointermove", (e) => {
    last = { x: e.clientX, y: e.clientY }
    if (hovered && wrapOf(e.target) === hovered && !(e.target as HTMLElement).closest(".qpop")) onDot = last
    if (!apex || aimed(last)) return
    apex = null
    const w = wrapOf(e.target)
    if (w && w !== hovered) hover(w)
    else if (!w) hideIn(LEAVE_MS)
  })
  // Keyboard focus keeps the pop-up open until focus leaves the dot and its pop-up, so
  // Tab can reach "Open the question" and the result links inside it.
  document.addEventListener("focusin", (e) => {
    const w = wrapOf(e.target)
    if (!w) return
    // A mouse press focuses too; only keyboard focus holds the pop-up open.
    if ((e.target as HTMLElement).matches(":focus-visible")) w.dataset.focused = "1"
    place(w)
  })
  document.addEventListener("focusout", (e) => {
    const w = wrapOf(e.target)
    if (w && !w.contains((e as FocusEvent).relatedTarget as Node | null)) delete w.dataset.focused
  })
  document.addEventListener("click", (e) => {
    const me = e as MouseEvent
    const dot = (e.target as HTMLElement | null)?.closest?.<HTMLElement>(".qdot")
    if (!dot || me.button !== 0 || me.metaKey || me.ctrlKey || me.shiftKey || me.altKey) return
    // detail 0 is a keyboard activation: the pop-up already shows on focus, so follow the link.
    if (me.detail === 0) return
    // Quartz's SPA router listens on window and navigates on any anchor click, prevented or not.
    e.preventDefault()
    e.stopPropagation()
    const w = wrapOf(dot)!
    if (w.dataset.open) {
      delete w.dataset.open
      w.dataset.closed = "1"
      return
    }
    closeAll(w)
    w.dataset.open = "1"
    place(w)
  })
  // pointerdown fires on touch taps where iOS Safari sends no click for non-interactive areas.
  document.addEventListener("pointerdown", (e) => {
    if (!wrapOf(e.target)) closeAll()
  })
  // Escape also hides a pop-up that only hover or focus is showing, until the pointer or focus leaves.
  document.addEventListener("keydown", (e) => {
    if (e.key !== "Escape") return
    const inside = (document.activeElement as HTMLElement | null)?.closest?.<HTMLElement>(".qpop")
    closeAll()
    for (const w of document.querySelectorAll<HTMLElement>(".qd[data-hover], .qd:focus-within")) w.dataset.closed = "1"
    // Focus in a pop-up that just closed would fall to the page; it returns to the dot.
    if (inside) wrapOf(inside)?.querySelector<HTMLElement>(".qdot")?.focus()
  })
  const rearm = (e: Event) => {
    const w = wrapOf(e.target)
    if (w && !w.contains((e as PointerEvent).relatedTarget as Node | null)) delete w.dataset.closed
  }
  document.addEventListener("pointerout", rearm)
  document.addEventListener("focusout", rearm)
  const follow = () => {
    for (const w of document.querySelectorAll<HTMLElement>(SHOWING)) place(w)
  }
  window.addEventListener("scroll", follow, { passive: true })
  window.addEventListener("resize", follow)
}
