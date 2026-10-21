// The browser half of search, Ask and navigation (src/client), carried as a
// Quartz component's afterDOMLoaded script. Quartz collects scripts from every
// registered component, so this one renders nothing and needs no layout slot.
import type { QuartzComponent, QuartzComponentConstructor } from "@quartz-community/types"
import script from "../dist/client.txt"

export const BerilClient: QuartzComponentConstructor = () => {
  const Client: QuartzComponent = () => null
  Client.afterDOMLoaded = script
  return Client
}
