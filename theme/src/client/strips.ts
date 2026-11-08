// The Topics page's topic key. Pointing at a key slot names its topic below the row;
// picking a topic keeps its name in the key and lights its cluster on the map.

let wiring: AbortController | null = null

export function wireStrips() {
  wiring?.abort()
  wiring = new AbortController()
  const signal = wiring.signal
  const key = document.querySelector<HTMLElement>("[data-tkey]")
  const idle = key?.querySelector<HTMLElement>(".tidle")
  const state = key?.querySelector<HTMLElement>(".tstate")
  const clear = key?.querySelector<HTMLButtonElement>(".tclear")
  if (!key || !idle || !state || !clear) return
  const map = document.querySelector<HTMLElement>("[data-tmap]")
  const mapgo = key.querySelector<HTMLButtonElement>(".tmapgo")
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
    for (const x of key.querySelectorAll<HTMLButtonElement>("button[data-t]")) x.setAttribute("aria-pressed", String(x.dataset.t === picked))
    if (map) {
      if (picked) map.dataset.pick = picked
      else delete map.dataset.pick
      for (const g of map.querySelectorAll<HTMLElement>(".cluster[data-t]")) g.classList.toggle("hit", g.dataset.t === picked)
    }
    show(picked)
  }

  key.hidden = false
  for (const slot of key.querySelectorAll<HTMLButtonElement>(".tkeyslot")) {
    const preview = () => show(slot.dataset.t!)
    slot.addEventListener("mouseenter", preview, { signal })
    slot.addEventListener("focus", preview, { signal })
    slot.addEventListener("mouseleave", () => show(picked), { signal })
    slot.addEventListener("blur", () => show(picked), { signal })
  }
  key.addEventListener(
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
