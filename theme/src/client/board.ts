// The filter bar over a board of cards (Results and Open questions), in the concepts
// listing's look: a text filter, a sort, Cards or List, a count, chip rows and toggles,
// with the state in the URL. The filter also fades the marks on the map above that it
// hides, so the map and the cards show the same set. A card's Compare button opens the
// comparison under its row. Cards render complete without this script.

interface BoardConfig {
  noun: string
  facets: { key: string; label: string; chips: { v: string; label: string; hue?: string; note?: string }[] }[]
  toggles: { key: string; label: string }[]
  sorts: { key: string; label: string }[]
}

const esc = (s: string) => s.replace(/[&<>"']/g, (ch) => `&#${ch.charCodeAt(0)};`)

function wireBoard(board: HTMLElement, signal: AbortSignal) {
  const raw = board.querySelector(".board-cfg")?.textContent
  const found = board.querySelector<HTMLElement>(":scope > .cards")
  if (!raw || !found) return
  const grid: HTMLElement = found
  const cfg = JSON.parse(raw) as BoardConfig
  board.querySelector(":scope > .px-tools")?.remove()
  const cards = [...grid.querySelectorAll<HTMLElement>(":scope > .card")]
  const params = new URLSearchParams(location.search)
  const state = {
    q: params.get("q") ?? "",
    sort: params.get("sort") ?? cfg.sorts[0]?.key ?? "",
    list: params.get("view") === "list",
    // A value no chip offers (a stale or edited link) would hide every card with no chip pressed.
    f: Object.fromEntries(
      cfg.facets.map((x) => {
        const v = params.get(x.key) ?? ""
        return [x.key, x.chips.some((c) => c.v === v) ? v : ""]
      }),
    ) as Record<string, string>,
    t: Object.fromEntries(cfg.toggles.map((x) => [x.key, params.get(x.key) === "1"])) as Record<string, boolean>,
  }
  if (!cfg.sorts.some((s) => s.key === state.sort)) state.sort = cfg.sorts[0]?.key ?? ""

  const tools = document.createElement("div")
  tools.className = "px-tools"
  tools.innerHTML =
    `<div class="row1">
      <input type="search" placeholder="Filter ${esc(cfg.noun)} by words" aria-label="Filter ${esc(cfg.noun)}" value="${esc(state.q)}">
      <label class="count sortl">Sort <select aria-label="Sort">${cfg.sorts.map((s) => `<option value="${esc(s.key)}">${esc(s.label)}</option>`).join("")}</select></label>
      <span class="px-seg" role="group" aria-label="View"><button type="button" data-v="cards">Cards</button><button type="button" data-v="list">List</button></span>
      <span class="count" aria-live="polite"></span>
    </div>` +
    cfg.facets
      .filter((x) => x.chips.length > 1)
      .map(
        (x) =>
          `<div class="facets" role="group" aria-label="Filter by ${esc(x.label.toLowerCase())}" data-k="${esc(x.key)}"><span class="px-facet-lbl">${esc(x.label)}</span>` +
          `<button type="button" class="px-chip" data-f="">All <span class="n"></span></button>` +
          x.chips
            .map(
              (c) =>
                `<button type="button" class="px-chip" data-f="${esc(c.v)}"${c.note ? ` title="${esc(c.note)}"` : ""}>${c.hue ? `<i class="dot" style="--c:${esc(c.hue)}"></i>` : ""}${esc(c.label)}${c.note ? ' <span aria-hidden="true">ⓘ</span>' : ""} <span class="n"></span></button>`,
            )
            .join("") +
          `</div>`,
      )
      .join("") +
    (cfg.toggles.length
      ? `<div class="facets toggles">${cfg.toggles.map((t) => `<label class="px-tog"><input type="checkbox" data-t="${esc(t.key)}"> ${esc(t.label)} <span class="n"></span></label>`).join("")}</div>`
      : "")
  board.prepend(tools)
  const input = tools.querySelector<HTMLInputElement>("input[type=search]")!
  const select = tools.querySelector<HTMLSelectElement>("select")!
  select.value = state.sort
  const count = tools.querySelector<HTMLElement>(".row1 > .count:last-child")!
  const nomatch = document.createElement("p")
  nomatch.className = "px-nomatch"
  nomatch.textContent = `No ${cfg.noun} here match. Clear a filter.`
  grid.after(nomatch)

  const textOf = new Map(cards.map((c) => [c, c.dataset.text ?? (c.textContent ?? "").toLowerCase()]))
  const fits = (c: HTMLElement, skip?: string) => {
    const terms = state.q.toLowerCase().split(/\s+/).filter(Boolean)
    if (!terms.every((t) => textOf.get(c)!.includes(t))) return false
    for (const x of cfg.facets) if (x.key !== skip && state.f[x.key] && c.getAttribute(`data-f-${x.key}`) !== state.f[x.key]) return false
    for (const t of cfg.toggles) if (t.key !== skip && state.t[t.key] && c.getAttribute(`data-t-${t.key}`) !== "1") return false
    return true
  }
  const active = () => !!state.q.trim() || Object.values(state.f).some(Boolean) || Object.values(state.t).some(Boolean)

  function fade(shown: Set<string>) {
    const on = active()
    for (const m of document.querySelectorAll<HTMLElement>(".nd[data-id], .qd[data-id]")) m.classList.toggle("out", on && !shown.has(m.dataset.id ?? ""))
    for (const b of document.querySelectorAll<HTMLElement>(".nbead[data-p]")) b.classList.toggle("out", on && !b.querySelector(".nd:not(.out)"))
  }

  function apply() {
    const shown = new Set<string>()
    for (const c of cards) {
      const ok = fits(c)
      c.classList.toggle("px-hidden", !ok)
      if (ok) shown.add(c.dataset.id ?? "")
    }
    const rank = (c: HTMLElement) => Number(c.getAttribute(`data-s-${state.sort}`) ?? 0)
    grid.append(...[...cards].sort((a, b) => rank(a) - rank(b)))
    board.classList.toggle("px-compact", state.list)
    count.textContent = `${shown.size} of ${cards.length}`
    nomatch.hidden = shown.size > 0
    for (const row of tools.querySelectorAll<HTMLElement>(".facets[data-k]")) {
      const k = row.dataset.k!
      for (const b of row.querySelectorAll<HTMLButtonElement>(".px-chip")) {
        const v = b.dataset.f ?? ""
        b.setAttribute("aria-pressed", String(v === state.f[k]))
        b.querySelector(".n")!.textContent = String(cards.filter((c) => fits(c, k) && (!v || c.getAttribute(`data-f-${k}`) === v)).length)
      }
    }
    for (const box of tools.querySelectorAll<HTMLInputElement>("input[data-t]")) {
      const k = box.dataset.t!
      box.checked = state.t[k]
      box.parentElement!.querySelector(".n")!.textContent = String(cards.filter((c) => fits(c, k) && c.getAttribute(`data-t-${k}`) === "1").length)
    }
    for (const b of tools.querySelectorAll<HTMLButtonElement>(".px-seg button")) b.setAttribute("aria-pressed", String((b.dataset.v === "list") === state.list))
    fade(shown)
    const u = new URL(location.href)
    const set = (k: string, v: string) => (v ? u.searchParams.set(k, v) : u.searchParams.delete(k))
    set("q", state.q)
    set("sort", state.sort === cfg.sorts[0]?.key ? "" : state.sort)
    set("view", state.list ? "list" : "")
    for (const x of cfg.facets) set(x.key, state.f[x.key])
    for (const t of cfg.toggles) set(t.key, state.t[t.key] ? "1" : "")
    history.replaceState(history.state, "", u)
    closePanels()
  }

  // The comparison opens under the last card of the clicked card's row, across the grid.
  const panels = new Map<string, HTMLElement>()
  let open: { button: HTMLButtonElement; panel: HTMLElement } | null = null
  // Rows are read from the grid's current order with the panel hidden, since a shown
  // panel splits its row; a resize that changes the column count places it again.
  function place() {
    if (!open) return
    const card = open.button.closest<HTMLElement>(".card")!
    open.panel.hidden = true
    const row = [...grid.querySelectorAll<HTMLElement>(":scope > .card:not(.px-hidden)")].filter((c) => c.offsetTop === card.offsetTop)
    ;(row.at(-1) ?? card).after(open.panel)
    open.panel.hidden = false
  }
  for (const b of grid.querySelectorAll<HTMLButtonElement>(".ccmp")) {
    const p = document.getElementById(b.getAttribute("aria-controls") ?? "")
    if (p) {
      p.hidden = true
      panels.set(p.id, p)
    }
  }
  function closePanels() {
    open = null
    for (const p of panels.values()) p.hidden = true
    for (const b of grid.querySelectorAll<HTMLButtonElement>(".ccmp")) b.setAttribute("aria-expanded", "false")
  }
  grid.addEventListener(
    "click",
    (e) => {
      const b = (e.target as HTMLElement).closest<HTMLButtonElement>(".ccmp")
      const p = b && panels.get(b.getAttribute("aria-controls") ?? "")
      if (!b || !p) return
      const wasOpen = open?.button === b
      closePanels()
      if (wasOpen) return
      open = { button: b, panel: p }
      place()
      b.setAttribute("aria-expanded", "true")
    },
    { signal },
  )
  window.addEventListener("resize", place, { signal })

  input.addEventListener("input", () => ((state.q = input.value), apply()), { signal })
  select.addEventListener("change", () => ((state.sort = select.value), apply()), { signal })
  tools.addEventListener(
    "click",
    (e) => {
      const chip = (e.target as HTMLElement).closest<HTMLButtonElement>(".px-chip")
      const row = chip?.closest<HTMLElement>(".facets[data-k]")
      if (chip && row) {
        const k = row.dataset.k!
        const v = chip.dataset.f ?? ""
        state.f[k] = state.f[k] === v ? "" : v
        return apply()
      }
      const seg = (e.target as HTMLElement).closest<HTMLButtonElement>(".px-seg button")
      if (seg) {
        state.list = seg.dataset.v === "list"
        apply()
      }
    },
    { signal },
  )
  tools.addEventListener(
    "change",
    (e) => {
      const box = (e.target as HTMLElement).closest<HTMLInputElement>("input[data-t]")
      if (!box) return
      state.t[box.dataset.t!] = box.checked
      apply()
    },
    { signal },
  )
  apply()
}

// Quartz's navigation reuses nodes; one signal per page drops the last page's listeners.
let wiring: AbortController | null = null

export function wireBoards() {
  wiring?.abort()
  wiring = new AbortController()
  for (const board of document.querySelectorAll<HTMLElement>("[data-board]")) wireBoard(board, wiring.signal)
}
