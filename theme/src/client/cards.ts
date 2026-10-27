// Finding and research-direction cards in the browser: the chip filters, the
// planner box and the copy buttons (BERIL prompt, handoff brief). Cards render complete without this script; it
// only hides the ones a reader filters out.

type Filters = Record<string, string>

const words = (s: string) => s.toLowerCase().split(/\s+/).filter(Boolean)

function matches(card: HTMLElement, f: Filters): boolean {
  const d = card.dataset
  if (f.text && !words(f.text).every((w) => (d.text ?? "").includes(w))) return false
  if (f.topic && !(d.topics ?? "").split(" ").includes(f.topic)) return false
  // A filter applies only to the cards that carry its field: a label chip never hides a research direction.
  if (f.label && d.label !== undefined && (f.label === "null" ? !d.null : d.label !== f.label)) return false
  if (f.readiness && d.readiness !== undefined && d.readiness !== f.readiness) return false
  if (f.approach && d.approach !== undefined && d.approach !== f.approach) return false
  return true
}

function apply(f: Filters) {
  for (const list of document.querySelectorAll<HTMLElement>(".grid2, .stack")) {
    const cards = [...list.querySelectorAll<HTMLElement>(":scope > .fcard, :scope > .ncard")]
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
      none.textContent = "No card here matches. Clear a filter, or try Plan my next project."
      list.after(none)
    }
    none.hidden = shown > 0
  }
}

/** The question the planner hands to Ask, scoped to findings, research directions and conflicts. */
export const planQuestion = (interest: string) =>
  `I am interested in ${interest}. Which three research directions in the wiki suit that interest? For each, ` +
  `give the question, the hypothesis, the data it needs and the test that would settle it.`

export function wireCards(handoff: (question: string, askUrl: string) => void) {
  const f: Filters = {}
  for (const group of document.querySelectorAll<HTMLElement>("[data-filter-group]")) {
    if (group.dataset.wired) continue
    group.dataset.wired = "1"
    const name = group.dataset.filterGroup!
    group.addEventListener("click", (e) => {
      const chip = (e.target as HTMLElement).closest<HTMLButtonElement>("button.c-chip")
      if (!chip) return
      // Every group of this name moves together, so the planner's topic chips and a board's agree.
      for (const twin of document.querySelectorAll<HTMLElement>(`[data-filter-group="${name}"]`))
        for (const b of twin.querySelectorAll("button.c-chip")) b.classList.toggle("on", (b as HTMLElement).dataset.value === chip.dataset.value)
      f[name] = chip.dataset.value ?? ""
      apply(f)
    })
  }
  const planner = document.querySelector<HTMLElement>("[data-planner]")
  if (planner && !planner.dataset.wired) {
    planner.dataset.wired = "1"
    const input = planner.querySelector<HTMLInputElement>("input")!
    input.addEventListener("input", () => {
      f.text = input.value
      apply(f)
    })
    const plan = () => {
      const topic = planner.querySelector<HTMLElement>("button.c-chip.on:not([data-value=''])")
      const interest = input.value.trim() || topic?.textContent?.trim() || ""
      if (!interest) {
        input.focus()
        input.placeholder = "Type an interest first, or pick a topic"
        return
      }
      handoff(planQuestion(interest), planner.dataset.ask ?? "ask")
    }
    planner.querySelector(".px-plan")!.addEventListener("click", plan)
    input.addEventListener("keydown", (e) => {
      if (e.key === "Enter") {
        e.preventDefault()
        plan()
      }
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
