// The home page's topic key. Pointing at a key slot names its topic below the row.
// Picking a topic, from the key or from a strip's topic names, outlines the results
// and questions that share it, keeps its name and counts in the key, and lights its
// cluster on the home map.

let wiring: AbortController | null = null

const plural = (n: number, word: string) => (n === 0 ? `no ${word}s` : n === 1 ? `1 ${word}` : `${n} ${word}s`)

export function wireStrips() {
  wiring?.abort()
  wiring = new AbortController()
  const signal = wiring.signal
  const key = document.querySelector<HTMLElement>("[data-tkey]")
  const idle = key?.querySelector<HTMLElement>(".tidle")
  const state = key?.querySelector<HTMLElement>(".tstate")
  const count = key?.querySelector<HTMLElement>(".tkcount")
  const clear = key?.querySelector<HTMLButtonElement>(".tclear")
  if (!key || !idle || !state || !count || !clear) return
  const map = document.querySelector<HTMLElement>("[data-tmap]")
  const mapgo = key.querySelector<HTMLButtonElement>(".tmapgo")
  const scopes = [...document.querySelectorAll<HTMLElement>("[data-tstrips]")]
  const infos = [...key.querySelectorAll<HTMLElement>(".tinfo")]
  let picked: string | null = null

  // The readout shows the topic under the pointer, else the picked one, else how to use the key.
  const show = (t: string | null) => {
    for (const info of infos) info.hidden = info.dataset.t !== t
    idle.hidden = !!t
    state.hidden = !picked || t !== picked
  }
  const pick = (t: string | null) => {
    picked = t === picked ? null : t
    let results = 0
    let questions = 0
    for (const scope of scopes) {
      if (picked) scope.dataset.pick = picked
      else delete scope.dataset.pick
      for (const e of scope.querySelectorAll<HTMLElement>("[data-topics]")) {
        const hit = !!picked && e.dataset.topics!.split(" ").includes(picked)
        e.classList.toggle("hit", hit)
        if (hit && e.matches(".fcard")) results++
        else if (hit) questions++
      }
    }
    for (const x of document.querySelectorAll<HTMLElement>("[data-tkey] [data-t], [data-tstrips] [data-t]")) {
      const me = x.dataset.t === picked
      if (x instanceof HTMLButtonElement) x.setAttribute("aria-pressed", String(me))
      else if (x.matches(".tslot")) x.classList.toggle("pick", me)
    }
    if (map) {
      if (picked) map.dataset.pick = picked
      else delete map.dataset.pick
      for (const g of map.querySelectorAll<HTMLElement>(".cluster[data-t]")) g.classList.toggle("hit", g.dataset.t === picked)
    }
    count.textContent = picked ? `On this page: ${plural(results, "result")} and ${plural(questions, "question")}.` : ""
    show(picked)
  }

  key.hidden = false
  for (const b of document.querySelectorAll<HTMLButtonElement>(".tname")) b.disabled = false
  for (const slot of key.querySelectorAll<HTMLButtonElement>(".tkeyslot")) {
    const preview = () => show(slot.dataset.t!)
    slot.addEventListener("mouseenter", preview, { signal })
    slot.addEventListener("focus", preview, { signal })
    slot.addEventListener("mouseleave", () => show(picked), { signal })
    slot.addEventListener("blur", () => show(picked), { signal })
  }
  for (const box of [key, ...scopes])
    box.addEventListener(
      "click",
      (ev) => {
        const b = (ev.target as Element).closest<HTMLButtonElement>("button[data-t]")
        if (b) pick(b.dataset.t!)
      },
      { signal },
    )
  if (map && mapgo) {
    mapgo.hidden = false
    mapgo.addEventListener(
      "click",
      () => {
        const still = matchMedia("(prefers-reduced-motion: reduce)").matches
        map.scrollIntoView({ behavior: still ? "auto" : "smooth", block: "center" })
      },
      { signal },
    )
  }
  // Clearing hides "Show all" and "See it on the map", so focus there returns to the
  // topic's key slot instead of falling to the page.
  const unpick = () => {
    const slot = key.querySelector<HTMLButtonElement>(`.tkeyslot[data-t="${CSS.escape(picked ?? "")}"]`)
    const lost = state.contains(document.activeElement)
    pick(null)
    if (lost) slot?.focus()
  }
  clear.addEventListener("click", unpick, { signal })
  document.addEventListener("keydown", (ev) => ev.key === "Escape" && picked && unpick(), { signal })
}
