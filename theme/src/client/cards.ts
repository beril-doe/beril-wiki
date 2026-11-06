// Result cards in the browser: the kind chips, the topic select, the comparison
// chip notes and the copy buttons (BERIL prompt, handoff brief). Cards render
// complete without this script (a chip's note is visible without it); the script
// hides the ones a reader filters out and folds each chip's note until pressed.

type Filters = Record<string, string>

function matches(card: HTMLElement, f: Filters): boolean {
  const d = card.dataset
  if (f.topic && d.topic !== f.topic) return false
  if (f.kind && d.kind !== f.kind) return false
  return true
}

function apply(f: Filters) {
  for (const list of document.querySelectorAll<HTMLElement>(".grid2")) {
    const cards = [...list.querySelectorAll<HTMLElement>(":scope > .fcard")]
    if (!cards.length) continue
    let shown = 0
    for (const card of cards) {
      const on = matches(card, f)
      card.hidden = !on
      if (on) shown++
    }
    let none = list.nextElementSibling as HTMLElement | null
    if (!none?.classList.contains("px-nomatch")) {
      none = document.createElement("p")
      none.className = "px-nomatch"
      none.textContent = "No result here matches. Clear a filter."
      list.after(none)
    }
    none.hidden = shown > 0
  }
}

function setNote(chip: HTMLButtonElement, open: boolean) {
  chip.setAttribute("aria-expanded", String(open))
  const note = chip.parentElement?.querySelector<HTMLElement>(".note")
  if (note) note.hidden = !open
}

let notesWired = false
function wireNotes() {
  if (notesWired) return
  notesWired = true
  const openedByFocus = new WeakSet<HTMLButtonElement>()
  const chipOf = (e: Event) => (e.target as HTMLElement).closest<HTMLButtonElement>("button.chip")
  document.addEventListener("click", (e) => {
    const chip = chipOf(e)
    if (!chip) return
    openedByFocus.delete(chip)
    setNote(chip, chip.getAttribute("aria-expanded") !== "true")
  })
  // A mouse press focuses the button before its click; only keyboard focus opens a note.
  document.addEventListener("focusin", (e) => {
    const chip = chipOf(e)
    if (!chip || !chip.matches(":focus-visible") || chip.getAttribute("aria-expanded") === "true") return
    setNote(chip, true)
    openedByFocus.add(chip)
  })
  document.addEventListener("focusout", (e) => {
    const chip = chipOf(e)
    if (chip && openedByFocus.delete(chip)) setNote(chip, false)
  })
  document.addEventListener("keydown", (e) => {
    if (e.key !== "Escape") return
    for (const chip of document.querySelectorAll<HTMLButtonElement>('button.chip[aria-expanded="true"]')) setNote(chip, false)
  })
}

export function wireCards() {
  wireNotes()
  for (const chip of document.querySelectorAll<HTMLButtonElement>("button.chip")) {
    if (chip.dataset.wired) continue
    chip.dataset.wired = "1"
    setNote(chip, false)
  }
  const f: Filters = {}
  for (const group of document.querySelectorAll<HTMLElement>("[data-filter-group]")) {
    if (group.dataset.wired) continue
    group.dataset.wired = "1"
    const name = group.dataset.filterGroup!
    group.addEventListener("click", (e) => {
      const chip = (e.target as HTMLElement).closest<HTMLButtonElement>("button.c-chip")
      if (!chip) return
      for (const b of group.querySelectorAll("button.c-chip")) {
        b.classList.toggle("on", b === chip)
        b.setAttribute("aria-pressed", String(b === chip))
      }
      f[name] = chip.dataset.value ?? ""
      apply(f)
    })
  }
  for (const sel of document.querySelectorAll<HTMLSelectElement>("select[data-filter-select]")) {
    if (sel.dataset.wired) continue
    sel.dataset.wired = "1"
    sel.addEventListener("change", () => {
      f[sel.dataset.filterSelect!] = sel.value
      apply(f)
    })
  }
  for (const b of document.querySelectorAll<HTMLButtonElement>(".px-copy")) {
    if (b.dataset.wired) continue
    b.dataset.wired = "1"
    b.addEventListener("click", async () => {
      try {
        await navigator.clipboard.writeText(b.dataset.copy ?? "")
        b.textContent = "Copied"
      } catch {
        b.textContent = "Copy failed: your browser blocked the clipboard"
      }
    })
  }
}
