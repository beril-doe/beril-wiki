// Meaning search: the reader's query is embedded by CBORG with the reader's own
// key, then compared with section vectors the site publishes (built by the
// search_vectors pipeline stage). The search box uses it only when the reader
// turns it on; Ask always uses it, since Ask already needs the key.
import { CBORG, loadSettings } from "./ai"
import { EMBED_MODEL, QUERY_PREFIX, type VectorMeta } from "../search/config"
import { asset, local } from "./site"

const PREF = "beril-meaning-search"
// CBORG keys allow 20 requests a minute; after a refusal, rest a minute before trying again.
const PAUSE_MS = 60_000

export type Status = "off" | "nokey" | "loading" | "on" | "paused" | "failed"
/** Why meaning search is unavailable, shown to the reader; "" while it works. */
let failed = ""
let pausedUntil = 0
let loading = false
let progress = { loaded: 0, total: 0 }
let vectors: { data: Int8Array; scales: Float32Array; dim: number; build: string } | null = null
let vectorsReady: Promise<boolean> | null = null
const queryCache = new Map<string, Float32Array>()
const listeners = new Set<() => void>()
const notify = () => listeners.forEach((f) => f())

export const onMeaningChange = (f: () => void) => listeners.add(f)
export const meaningProgress = () => progress
/** The reader's choice for the search box; Ask ignores it. */
// Held here and only persisted, so the switch works where the browser refuses to store it.
let wanted: boolean | null = null
export const meaningWanted = () => (wanted ??= local.get(PREF) === "on")
export const meaningError = () => failed

export function meaningStatus(): Status {
  if (!meaningWanted()) return "off"
  if (!loadSettings().key) return "nokey"
  if (loading) return "loading"
  if (failed) return "failed"
  if (Date.now() < pausedUntil) return "paused"
  return "on"
}

export function setMeaningWanted(on: boolean) {
  wanted = on
  local.set(PREF, on ? "on" : "off")
  failed = ""
  if (on) void loadVectors()
  notify()
}

const HEADER = 16

/** vectors.i8 for this vectors.json, checked against its build id; null when it is from another deploy. */
async function download(meta: VectorMeta, init?: RequestInit): Promise<Uint8Array | null> {
  // The build id in the URL keeps a cached file from an earlier deploy from being reused.
  const r = await fetch(`${asset("vectors.i8")}?v=${meta.build}`, init)
  if (!r.ok || !r.body) throw new Error(`vectors: HTTP ${r.status}`)
  const size = HEADER + meta.scales.length * meta.dim
  const total = Number(r.headers.get("content-length")) || size
  const buf = new Uint8Array(size)
  const reader = r.body.getReader()
  let n = 0
  for (;;) {
    const { done, value } = await reader.read()
    if (done) break
    if (n + value.byteLength > size) return null
    buf.set(value, n)
    n += value.byteLength
    progress = { loaded: n, total }
    notify()
  }
  // A short file would leave zero rows that still rank; a different header is another deploy's rows.
  if (n !== size || new TextDecoder().decode(buf.subarray(0, HEADER)) !== meta.build) return null
  return buf
}

/**
 * Downloads the section vectors once (about 6 MB); resolves false if they cannot be
 * loaded. `fresh` asks the server again past the browser cache.
 */
export function loadVectors(fresh = false): Promise<boolean> {
  vectorsReady ??= (async () => {
    loading = true
    notify()
    try {
      const init: RequestInit | undefined = fresh ? { cache: "no-cache" } : undefined
      let meta: VectorMeta = await fetch(asset("vectors.json"), init).then((r) => r.json())
      let buf = await download(meta, init)
      if (!buf && !fresh) {
        meta = await fetch(asset("vectors.json"), { cache: "no-cache" }).then((r) => r.json())
        buf = await download(meta, { cache: "no-cache" })
      }
      if (!buf) throw new Error("vectors: the two vector files are from different deploys")
      vectors = { data: new Int8Array(buf.buffer, HEADER), scales: Float32Array.from(meta.scales), dim: meta.dim, build: meta.build }
      return true
    } catch (e) {
      console.warn("meaning search: vectors unavailable", e)
      failed = "the section vectors did not download"
      vectorsReady = null
      return false
    } finally {
      loading = false
      notify()
    }
  })()
  return vectorsReady
}

function fail(why: string) {
  failed = why
  notify()
}

async function embedQuery(q: string, dim: number): Promise<Float32Array | null> {
  const hit = queryCache.get(q)
  if (hit) return hit
  const key = loadSettings().key
  if (!key || Date.now() < pausedUntil) return null
  let r: Response
  try {
    r = await fetch(`${CBORG}/v1/embeddings`, {
      method: "POST",
      headers: { "content-type": "application/json", authorization: `Bearer ${key}` },
      body: JSON.stringify({ model: EMBED_MODEL, input: [QUERY_PREFIX + q] }),
    })
  } catch {
    fail("CBORG could not be reached")
    return null
  }
  if (r.status === 429) {
    pausedUntil = Date.now() + PAUSE_MS
    notify()
    // Nothing else repaints when the pause ends.
    setTimeout(notify, PAUSE_MS + 50)
    return null
  }
  if (r.status === 401 || r.status === 403) return fail("CBORG rejected your key"), null
  if (!r.ok) return fail(`CBORG answered with HTTP ${r.status}`), null
  const v: number[] = await r.json().then((j) => j.data?.[0]?.embedding ?? [], () => [])
  if (v.length !== dim) return fail("CBORG sent an unusable embedding"), null
  const norm = Math.hypot(...v) || 1
  const out = Float32Array.from(v, (x) => x / norm)
  queryCache.set(q, out)
  if (failed) fail("")
  return out
}

/**
 * Section ids by meaning, best first. Empty when meaning is unavailable, so
 * callers fall back to keyword results and meaningError() says why. `always` is
 * for Ask, which does not depend on the search-box switch. `build` is the
 * sections.json the ids index into.
 */
export async function meaningRank(q: string, k: number, build: string, keep?: (id: number) => boolean, always = false): Promise<number[]> {
  if (!always && meaningStatus() !== "on") return []
  // Read through a function: loadVectors replaces `vectors` while this awaits.
  const loaded = () => vectors
  if (!(await loadVectors())) return []
  let v = loaded()
  if (v && v.build !== build) {
    // Downloaded across a site update: row i is no longer section i. Ask the server once more.
    vectors = null
    vectorsReady = null
    if (!(await loadVectors(true))) return []
    v = loaded()
    if (v && v.build !== build) return fail("the site was updated; reload the page"), []
  }
  if (!v) return []
  const qv = await embedQuery(q, v.dim)
  if (!qv) return []
  // The switch may have been turned off while the query was being embedded.
  if (!always && !meaningWanted()) return []
  const { data, scales, dim } = v
  const n = scales.length
  const scores = new Float32Array(n)
  for (let i = 0; i < n; i++) {
    if (!scales[i]) continue
    let s = 0
    const o = i * dim
    for (let d = 0; d < dim; d++) s += data[o + d] * qv[d]
    scores[i] = s * scales[i]
  }
  const ids: number[] = []
  for (let i = 0; i < n; i++) if (scales[i] && (!keep || keep(i))) ids.push(i)
  return ids.sort((a, b) => scores[b] - scores[a]).slice(0, k)
}

/** Reciprocal rank fusion: a section near the top of either list ranks high. Returns id -> score. */
export function fuse(lists: number[][], k = 60): Map<number, number> {
  const score = new Map<number, number>()
  for (const l of lists) l.forEach((id, r) => score.set(id, (score.get(id) ?? 0) + 1 / (k + r + 1)))
  return score
}
