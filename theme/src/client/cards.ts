// Result cards in the browser: the comparison chip notes and the copy buttons (BERIL
// prompt, handoff brief). A chip's note is visible without this script, which folds
// it until pressed. Filtering lives in board.ts.

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
