// The reader's own CBORG key and model choice. The key stays in this browser
// and is sent only to CBORG, which allows cross-origin calls, so the wiki needs
// no server of its own to answer questions.
import { local, session } from "./site"

export const CBORG = "https://api.cborg.lbl.gov"
export const MODELS = [
  { id: "claude-sonnet-5-5", label: "Claude Sonnet 5.5", note: "default" },
  { id: "claude-haiku-4-5", label: "Claude Haiku 4.5", note: "faster and cheaper" },
  { id: "claude-opus-5-5", label: "Claude Opus 5.5", note: "slower, strongest" },
]
const STORE = "beril-wiki-ai"

export interface AiSettings {
  key: string
  model: string
  /** localStorage when true; sessionStorage, which the tab forgets on close, when false */
  remember: boolean
}

export interface ChatMessage {
  role: "system" | "user" | "assistant"
  content: string
}

export interface ChatResult {
  text: string
  inTokens: number
  outTokens: number
  /** the model stopped for a reason other than finishing: the length limit, a filter */
  cut: boolean
  /** the finish reason CBORG reported, such as stop or length */
  reason: string
}

const esc = (s: string) => s.replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c]!)
export const modelLabel = (id: string) => MODELS.find((m) => m.id === id)?.label ?? id

// Where a browser refuses storage, the key lives in this page until it reloads.
let unsaved: AiSettings | null = null

export function loadSettings(): AiSettings {
  for (const store of [local, session]) {
    const raw = store.get(STORE)
    if (!raw) continue
    try {
      const j = JSON.parse(raw)
      return { key: String(j.key ?? ""), model: String(j.model || MODELS[0].id), remember: store === local }
    } catch {}
  }
  return unsaved ?? { key: "", model: MODELS[0].id, remember: true }
}

const listeners = new Set<() => void>()
export const onSettingsChange = (f: () => void) => listeners.add(f)
const notify = () => listeners.forEach((f) => f())
// Another tab saving or forgetting the key updates this one too.
window.addEventListener("storage", (e) => e.key === STORE && notify())

function saveSettings(s: AiSettings) {
  local.remove(STORE)
  session.remove(STORE)
  unsaved = (s.remember ? local : session).set(STORE, JSON.stringify({ key: s.key, model: s.model })) ? null : s
  notify()
}

function forgetKey() {
  local.remove(STORE)
  session.remove(STORE)
  unsaved = null
  notify()
}

async function testKey(key: string, model: string): Promise<string | null> {
  let r: Response
  try {
    r = await fetch(`${CBORG}/v1/models`, { headers: { authorization: `Bearer ${key}` } })
  } catch {
    return "Could not reach CBORG. Check your network or VPN."
  }
  if (r.status === 401 || r.status === 403) return "CBORG rejected this key."
  if (!r.ok) return `CBORG answered with HTTP ${r.status}.`
  let ids: string[]
  try {
    ids = ((await r.json()).data as { id: string }[]).map((m) => m.id)
  } catch {
    return "CBORG sent an unreadable model list. Try again."
  }
  if (!ids.includes(model)) return `The key works, but CBORG does not offer the model “${model}”.`
  return null
}

export const KEY_SVG = `<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="6" cy="10" r="3.6"/><path d="M9.6 10H18M15 10v3M17.6 10v2.2"/></svg>`

// Closes the dialog that is open, so a second one never leaves the first one's listeners behind.
let closeOpen: (() => void) | null = null

/** Opens the key dialog. Resolves true when a working key is saved. */
export function openSettings(reason = ""): Promise<boolean> {
  closeOpen?.()
  const s = loadSettings()
  const custom = !MODELS.some((m) => m.id === s.model)
  const modal = document.createElement("div")
  modal.className = "px-modal"
  modal.innerHTML = `<form class="px-modal-box" role="dialog" aria-modal="true" aria-labelledby="px-ai-title">
    <h2 id="px-ai-title">Your CBORG key</h2>
    ${reason ? `<p class="px-reason">${esc(reason)}</p>` : ""}
    <p>Ask the wiki and Ask about this page send your question, and the wiki sections that match it, to CBORG with your own key. The key stays in this browser and goes only to <code>api.cborg.lbl.gov</code>. Usage is billed to your CBORG account. <a href="https://cborg.lbl.gov" target="_blank" rel="noopener">Get a key</a></p>
    <p class="px-hint">A remembered key sits in browser storage that every page under beril-doe.org can read, including the BERIL home page. Untick Remember if you would rather enter it once per tab.</p>
    <label class="px-field"><span>API key</span>
      <span class="px-keyrow"><input name="key" type="password" autocomplete="off" spellcheck="false" placeholder="Paste your CBORG key" value="${esc(s.key)}"><button type="button" class="px-show">Show</button></span></label>
    <label class="px-field"><span>Model</span>
      <select name="model">${MODELS.map((m) => `<option value="${m.id}" ${m.id === s.model ? "selected" : ""}>${m.label} (${m.note})</option>`).join("")}<option value="custom" ${custom ? "selected" : ""}>Another CBORG model…</option></select>
      <input name="custom" class="${custom ? "" : "px-hidden"}" placeholder="CBORG model ID, for example claude-sonnet-5-5" value="${custom ? esc(s.model) : ""}"></label>
    <label class="px-check"><input name="remember" type="checkbox" ${s.remember ? "checked" : ""}> Remember on this device</label>
    <p class="px-hint">Unchecked, the key is forgotten when you close this tab.</p>
    <div class="px-status" aria-live="polite"></div>
    <div class="px-actions">
      <button type="submit" class="px-btn">Save and test</button>
      ${s.key ? `<button type="button" class="px-btn ghost px-forget">Forget key</button>` : ""}
      <button type="button" class="px-btn ghost px-close">Close</button>
    </div>
  </form>`
  document.body.append(modal)
  const form = modal.querySelector("form")!
  const key = form.elements.namedItem("key") as HTMLInputElement
  const sel = form.elements.namedItem("model") as HTMLSelectElement
  const cust = form.elements.namedItem("custom") as HTMLInputElement
  const remember = form.elements.namedItem("remember") as HTMLInputElement
  const status = modal.querySelector<HTMLElement>(".px-status")!
  const opener = document.activeElement as HTMLElement | null
  key.focus()
  return new Promise((resolve) => {
    let saved = false
    let closed = false
    const close = () => {
      if (closed) return
      closed = true
      closeOpen = null
      modal.remove()
      document.removeEventListener("keydown", onKey, true)
      opener?.focus?.()
      resolve(saved)
    }
    const onKey = (e: KeyboardEvent) => {
      if (e.key === "Escape") {
        e.stopImmediatePropagation()
        close()
      }
    }
    document.addEventListener("keydown", onKey, true)
    closeOpen = close
    modal.addEventListener("mousedown", (e) => e.target === modal && close())
    modal.querySelector(".px-close")!.addEventListener("click", close)
    modal.querySelector(".px-show")!.addEventListener("click", (e) => {
      key.type = key.type === "password" ? "text" : "password"
      ;(e.target as HTMLElement).textContent = key.type === "password" ? "Show" : "Hide"
    })
    sel.addEventListener("change", () => cust.classList.toggle("px-hidden", sel.value !== "custom"))
    modal.querySelector(".px-forget")?.addEventListener("click", () => {
      forgetKey()
      saved = false
      close()
    })
    form.addEventListener("submit", async (e) => {
      e.preventDefault()
      const k = key.value.trim()
      const model = sel.value === "custom" ? cust.value.trim() : sel.value
      if (!k) return void (status.textContent = "Paste a key first.")
      if (!model) return void (status.textContent = "Enter a model ID.")
      status.className = "px-status"
      status.textContent = "Testing the key with CBORG…"
      const err = await testKey(k, model).catch(() => "Testing the key failed. Try again.")
      // Forget, Close or Escape during the test cancels it; saving now would undo them.
      if (closed) return
      if (err) {
        status.className = "px-status bad"
        status.textContent = err
        return
      }
      saveSettings({ key: k, model, remember: remember.checked })
      saved = true
      status.className = "px-status good"
      status.textContent = `Saved. Answers will use ${modelLabel(model)}.`
      setTimeout(close, 700)
    })
  })
}

/** Makes sure a key is set, asking for one when it is not. */
export async function ensureKey(reason: string): Promise<boolean> {
  return loadSettings().key ? true : openSettings(reason)
}

/** One line saying which key and model answers use, with a way to change them. */
export function statusLine(el: HTMLElement) {
  const paint = () => {
    const s = loadSettings()
    el.innerHTML = s.key
      ? `Answers use your CBORG key with ${esc(modelLabel(s.model))}. <button type="button">Change</button>`
      : `<button type="button">Add your CBORG key</button> to get answers.`
    el.querySelector("button")!.addEventListener("click", () => openSettings())
  }
  paint()
  onSettingsChange(paint)
}

/** Streams a chat completion straight from CBORG with the reader's key. */
export async function streamChat(messages: ChatMessage[], onText: (t: string) => void, signal?: AbortSignal): Promise<ChatResult> {
  const s = loadSettings()
  // The key can be forgotten while sections are being retrieved.
  if (!s.key) throw new Error("No CBORG key is set. Use the key button to add one.")
  const res = await fetch(`${CBORG}/v1/chat/completions`, {
    method: "POST",
    headers: { "content-type": "application/json", authorization: `Bearer ${s.key}` },
    // CBORG's Sonnet counts hidden reasoning as output tokens, so the cap is generous.
    body: JSON.stringify({ model: s.model, messages, stream: true, stream_options: { include_usage: true }, temperature: 0.2, max_tokens: 4000 }),
    signal,
  })
  if (res.status === 401 || res.status === 403) throw new Error("CBORG rejected your key. Open the key settings to fix it.")
  if (!res.ok || !res.body) throw new Error(`CBORG answered with HTTP ${res.status}. ${(await res.text().catch(() => "")).slice(0, 200)}`)
  const reader = res.body.getReader()
  const dec = new TextDecoder()
  const out: ChatResult = { text: "", inTokens: 0, outTokens: 0, cut: false, reason: "" }
  let buf = ""
  let finished = false
  for (;;) {
    const { done, value } = await reader.read()
    if (done) break
    buf += dec.decode(value, { stream: true })
    const lines = buf.split("\n")
    buf = lines.pop() ?? ""
    for (const line of lines) {
      if (!line.startsWith("data:")) continue
      const data = line.slice(5).trim()
      if (!data || data === "[DONE]") continue
      // A skipped event would leave a hole in the answer, so an unreadable one ends it.
      let j
      try {
        j = JSON.parse(data)
      } catch {
        throw new Error("CBORG sent part of the answer garbled. Try asking again.")
      }
      if (j.error) throw new Error(`CBORG reported an error: ${j.error.message ?? JSON.stringify(j.error).slice(0, 200)}`)
      const delta = j.choices?.[0]?.delta?.content
      if (delta) {
        out.text += delta
        onText(out.text)
      }
      const reason = j.choices?.[0]?.finish_reason
      if (reason) {
        finished = true
        out.reason = String(reason)
        out.cut = reason !== "stop"
      }
      if (j.usage) {
        out.inTokens = j.usage.prompt_tokens ?? 0
        out.outTokens = j.usage.completion_tokens ?? 0
      }
    }
  }
  if (!finished) throw new Error("The answer stopped before it finished. Try asking again.")
  return out
}
