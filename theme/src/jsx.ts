// Glue between Quartz's component types and the JSX the frame renders.
import type { QuartzComponent, QuartzComponentProps } from "@quartz-community/types"
import type { JSX } from "preact"
import { htmlToJsx } from "@quartz-community/utils"
import type { ElementContent, Root } from "hast"

// Quartz types slot components as returning unknown; JSX wants elements.
export type Slot = (props: QuartzComponentProps) => JSX.Element
export const slot = (xs: readonly QuartzComponent[]) => xs as unknown as Slot[]

export const jsx = (nodes: ElementContent[]) => htmlToJsx({ type: "root", children: nodes } as Root)
