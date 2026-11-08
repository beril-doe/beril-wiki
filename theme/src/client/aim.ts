// Hover cards on the two maps share one rule for the pointer's trip from a mark into its
// card: while the pointer moves inside the triangle from the point where it left the mark
// to the card's near edge, the card stays and the marks it crosses do not take over. Cards
// sit beside rows of marks, so the straight path to a card's link crosses its neighbours.

export interface Point {
  x: number
  y: number
}

const side = (a: Point, b: Point, p: Point) => (b.x - a.x) * (p.y - a.y) - (b.y - a.y) * (p.x - a.x)

/** True when `p` is inside `card`, or inside the triangle from `apex` to the card's edge that faces it. */
export function towards(apex: Point, card: DOMRect, p: Point): boolean {
  if (p.x >= card.left && p.x <= card.right && p.y >= card.top && p.y <= card.bottom) return true
  const [b, c]: [Point, Point] =
    apex.y >= card.bottom
      ? [{ x: card.left, y: card.bottom }, { x: card.right, y: card.bottom }]
      : apex.y <= card.top
        ? [{ x: card.left, y: card.top }, { x: card.right, y: card.top }]
        : apex.x <= card.left
          ? [{ x: card.left, y: card.top }, { x: card.left, y: card.bottom }]
          : [{ x: card.right, y: card.top }, { x: card.right, y: card.bottom }]
  const d1 = side(apex, b, p)
  const d2 = side(b, c, p)
  const d3 = side(c, apex, p)
  return !((d1 < 0 || d2 < 0 || d3 < 0) && (d1 > 0 || d2 > 0 || d3 > 0))
}

/** How long a card waits for a pointer that stops inside the triangle, and for one that left it. */
export const AIM_MS = 700
export const LEAVE_MS = 120
