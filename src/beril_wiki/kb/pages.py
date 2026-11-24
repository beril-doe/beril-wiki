"""A wiki page as addressable sections.

A section is the lead (everything between the title and the first H2) or one H2 with
its body. An agent reads and replaces one section at a time, so no edit rewrites a
whole page and an untouched section keeps its bytes.
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass

LEAD = "lead"
FRONT = re.compile(r"\A---\n.*?\n---\n", re.S)
# Markdown opens a fence with up to three spaces of indent.
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})")
H1 = re.compile(r"^# +(.+?)\s*$")
H2 = re.compile(r"^## +(.+?)\s*$")
SRC_TAG = re.compile(r"\[src:\s*([^\]]+)\]")
WIKILINK = re.compile(r"\[\[([^\]|#]+?)(?:[|#][^\]]*)?\]\]")
WORD = re.compile(r"\S+")


@dataclass(frozen=True)
class Section:
    anchor: str
    heading: str
    body: str
    # Character offsets of the body in the page text, surrounding blank lines excluded.
    start: int
    end: int

    @property
    def sha(self) -> str:
        return body_sha(self.body)

    @property
    def words(self) -> int:
        return len(WORD.findall(self.body))


@dataclass(frozen=True)
class Page:
    front: str
    title: str
    sections: tuple[Section, ...]

    def section(self, anchor: str) -> Section | None:
        return next((s for s in self.sections if s.anchor == anchor), None)


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def body_sha(body: str) -> str:
    return hashlib.sha256(body.strip().encode("utf-8")).hexdigest()[:16]


def sources_in(text: str) -> list[str]:
    """The report ids a text cites, in first-cited order."""
    out: list[str] = []
    for tag in SRC_TAG.finditer(text):
        for part in re.split(r"[,;]", tag.group(1)):
            sid = re.sub(r"__REPORT$", "", part.strip())
            if sid and sid not in out:
                out.append(sid)
    return out


def links_in(text: str) -> list[str]:
    """Wikilink targets as ``kind/slug`` page ids, in first-linked order."""
    out: list[str] = []
    for m in WIKILINK.finditer(text):
        target = m.group(1).strip().lstrip("/").removesuffix(".md")
        if target and target not in out:
            out.append(target)
    return out


def parse(text: str) -> Page:
    """Split a page into its frontmatter, title and sections.

    Headings inside fenced code are text. Two H2s with the same heading get ``-2``,
    ``-3`` anchors in page order, so an anchor names one section.
    """
    front = FRONT.match(text)
    offset = front.end() if front else 0
    title = ""
    # (anchor, heading, offset where the body may begin)
    marks: list[tuple[str, str, int]] = []
    ends: list[int] = []
    seen: dict[str, int] = {}
    fence = ""
    lead_from = offset
    pos = offset
    for line in text[offset:].splitlines(keepends=True):
        bare = line.rstrip("\n")
        opened = FENCE.match(bare)
        if opened and not fence:
            fence = opened.group(1)
        elif fence and bare.lstrip(" ").startswith(fence) and not bare.strip(" " + fence[0]):
            fence = ""
        elif not fence:
            h1, h2 = H1.match(bare), H2.match(bare)
            if h1 and not title and not marks:
                title = h1.group(1)
                lead_from = pos + len(line)
            elif h2:
                base = slug(h2.group(1)) or "section"
                seen[base] = seen.get(base, 0) + 1
                anchor = base if seen[base] == 1 else f"{base}-{seen[base]}"
                ends.append(pos)
                marks.append((anchor, h2.group(1), pos + len(line)))
        pos += len(line)
    ends.append(len(text))
    spans = [(LEAD, "", lead_from, ends[0])]
    spans += [(a, h, begin, ends[i + 1]) for i, (a, h, begin) in enumerate(marks)]
    sections = []
    for anchor, heading, begin, end in spans:
        raw = text[begin:end]
        body = raw.strip()
        start = begin + (len(raw) - len(raw.lstrip())) if body else begin
        sections.append(Section(anchor, heading, body, start, start + len(body)))
    return Page(front.group(0) if front else "", title, tuple(sections))


def replace(text: str, anchor: str, body: str) -> str:
    """The page text with one section's body replaced; every other byte is kept."""
    section = parse(text).section(anchor)
    if section is None:
        raise KeyError(anchor)
    body = body.strip()
    if section.body or not body:
        return text[: section.start] + body + text[section.end :]
    # An empty section has no body span to keep spacing from, so supply it.
    before = text[: section.start].rstrip("\n")
    after = text[section.start :].lstrip("\n")
    return f"{before}\n\n{body}\n" + (f"\n{after}" if after else "")


def append_section(text: str, heading: str, body: str) -> str:
    """The page text with a new H2 section added at the end."""
    return f"{text.rstrip()}\n\n## {heading.strip()}\n\n{body.strip()}\n"
