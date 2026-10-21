// Where the site lives: under beril-doe.org/beril-wiki/ in production and at /
// locally, so every link and asset is built from the root Quartz renders.

export const esc = (s: string) =>
  s.replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c]!)

/** The current page's slug, e.g. concepts/gene-essentiality, index, concepts/index. */
export const currentSlug = () => document.body.dataset.slug ?? "index"

/**
 * The site root path with a trailing slash, e.g. /beril-wiki/ or /. Quartz writes it
 * from baseUrl. Reading it from the address bar instead let a crafted 404 URL inject
 * markup, and gave the wrong root at an explicit .../index.html.
 */
export const siteRoot = () => `${document.body.dataset.basepath ?? ""}/`

/** A page URL from its slug, with an optional section anchor. */
export const pageHref = (slug: string, anchor = "") =>
  `${siteRoot()}${slug.replace(/(^|\/)index$/, "$1")}${anchor ? `#${anchor}` : ""}`

/** A search-index file under static/search/. */
export const asset = (file: string) => `${siteRoot()}static/search/${file}`

/** The slug of a link on this site, from its absolute URL. */
export function slugOfHref(url: string): string {
  const root = siteRoot()
  const path = decodeURIComponent(new URL(url, location.href).pathname).replace(/\.html$/, "")
  const rel = path.startsWith(root) ? path.slice(root.length) : path.replace(/^\/+/, "")
  return rel.replace(/\/$/, "/index") || "index"
}

// Titles keep Markdown italics (*Escherichia coli*); show them as italics.
export const titleHtml = (s: string) => esc(s).replace(/\*([^*]+)\*/g, "<i>$1</i>")

/**
 * Web Storage that a browser may refuse (site data blocked): reads give null and
 * writes report false, so search and the rest of the page keep working.
 */
export function storage(area: "local" | "session") {
  const get = () => (area === "local" ? localStorage : sessionStorage)
  return {
    get(key: string): string | null {
      try {
        return get().getItem(key)
      } catch {
        return null
      }
    },
    set(key: string, value: string): boolean {
      try {
        get().setItem(key, value)
        return true
      } catch {
        return false
      }
    },
    remove(key: string) {
      try {
        get().removeItem(key)
      } catch {}
    },
  }
}
export const local = storage("local")
export const session = storage("session")
