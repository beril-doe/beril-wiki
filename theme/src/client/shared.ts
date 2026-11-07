// The Results page's shared-result cards. Each card's comparison panel renders open, so
// the page reads without this script; here the panels fold, and a card's button opens
// its panel under that card's row, or under the card itself when the cards stack.

const STACKED = "(max-width: 899px)"

// Quartz's navigation reuses page nodes and strips data attributes, so a "wired" marker
// cannot stop a second set of listeners. Each page's listeners share one signal instead,
// aborted before the next page wires its own.
let wiring: AbortController | null = null

export function wireShared() {
  wiring?.abort()
  wiring = new AbortController()
  const signal = wiring.signal
  for (const box of document.querySelectorAll<HTMLElement>("[data-shared]")) {
    const row = box.querySelector<HTMLElement>(".scards")
    const cards = [...box.querySelectorAll<HTMLElement>(".scard")]
    if (!row || cards.length === 0) continue
    const panelOf = (card: HTMLElement) =>
      box.querySelector<HTMLElement>(`#${CSS.escape(card.dataset.panel ?? "")}`)
    const button = (card: HTMLElement) => card.querySelector<HTMLButtonElement>(".scmp")
    const stacked = window.matchMedia(STACKED)
    // The last card sharing this card's top edge ends its row. The panel hides while
    // rows are measured, since a shown panel inside the grid would split its row.
    const place = (card: HTMLElement) => {
      const panel = panelOf(card)
      if (!panel) return
      const shown = !panel.hidden
      panel.hidden = true
      const rowEnd = stacked.matches ? card : (cards.filter((c) => c.offsetTop === card.offsetTop).at(-1) ?? card)
      rowEnd.after(panel)
      panel.hidden = !shown
    }
    const closeAll = () => {
      for (const card of cards) {
        card.classList.remove("open")
        button(card)?.setAttribute("aria-expanded", "false")
        const panel = panelOf(card)
        if (panel) panel.hidden = true
      }
    }
    closeAll()
    for (const card of cards) {
      button(card)?.addEventListener(
        "click",
        () => {
          const wasOpen = card.classList.contains("open")
          closeAll()
          if (wasOpen) return
          const panel = panelOf(card)
          if (!panel) return
          card.classList.add("open")
          button(card)?.setAttribute("aria-expanded", "true")
          place(card)
          panel.hidden = false
        },
        { signal },
      )
    }
    stacked.addEventListener(
      "change",
      () => {
        const open = cards.find((card) => card.classList.contains("open"))
        if (open) place(open)
      },
      { signal },
    )
  }
}
