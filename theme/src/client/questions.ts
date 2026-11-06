// The open-questions grid in the browser. The dots are links and the grid reads
// without this script. Here a hover or keyboard focus shows a dot's pop-up inside
// the viewport; a click or tap pins it open, and a second click or tap on the same
// dot, Escape, or a press outside closes it. The pop-up's "Open the question"
// link navigates; Enter on a focused dot follows the dot's own link.

const MARGIN = 8

function place(wrap: HTMLElement) {
  const dot = wrap.querySelector<HTMLElement>(".qdot")
  const pop = wrap.querySelector<HTMLElement>(".qpop")
  if (!dot || !pop) return
  pop.style.position = "fixed"
  pop.style.bottom = "auto"
  const r = dot.getBoundingClientRect()
  const w = pop.offsetWidth
  const h = pop.offsetHeight
  const left = Math.max(MARGIN, Math.min(r.left + r.width / 2 - w / 2, window.innerWidth - w - MARGIN))
  const above = r.top - h - MARGIN >= MARGIN
  pop.style.left = `${left}px`
  pop.style.top = `${above ? r.top - h - 4 : Math.min(r.bottom + 4, window.innerHeight - h - MARGIN)}px`
}

const SHOWING = ".qd[data-open], .qd[data-focused], .qd:hover"

function closeAll(except?: Element) {
  for (const d of document.querySelectorAll<HTMLElement>(".qd[data-open]")) if (d !== except) delete d.dataset.open
}

let wired = false
export function wireQuestions() {
  if (wired) return
  wired = true
  const wrapOf = (t: EventTarget | null) => (t as HTMLElement | null)?.closest?.<HTMLElement>(".qd") ?? null
  document.addEventListener("pointerover", (e) => {
    const w = wrapOf(e.target)
    if (w) place(w)
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
    for (const w of document.querySelectorAll<HTMLElement>(".qd:hover, .qd:focus-within")) w.dataset.closed = "1"
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
