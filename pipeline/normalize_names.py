#!/usr/bin/env python3
"""Normalise what the wiki calls the data platform it rests on.

The lakehouse is the KBase Data Lakehouse. It is not the BER Data Lakehouse,
and it is not BERDL: both are earlier names for the same system, and the
compiled pages inherited them from reports written while those names were
current. A rename in prose is deterministic, so it is a stage rather than a
one-off edit, and it re-runs after every compile that writes a page fresh.

What is deliberately left alone:

  wiki/sources/       the raw reports, which the About page promises are
                      unedited. Renaming a system inside an archived report
                      is a call for a human, not for this script.
  project ids         `berdl_data_atlas` is a filename, a slug and a citation
                      key. Only the uppercase word is prose.
  project names       "BERDL Data Atlas" is what a project called itself, so
                      renaming it would misreport the project rather than the
                      platform. A summary's own title is the wiki's, and it is
                      renamed; the raw report under wiki/sources keeps the
                      title it was written with.
  wikilink targets    the path in [[target|label]] is a slug. The label is
                      prose and is renamed with everything else.
  frontmatter         type/sources/full_text are machinery. `description` is
                      not: it is what the catalog and the cards show, so it is
                      renamed like any other prose.

Run it as often as you like; it is idempotent.
"""

from __future__ import annotations

import pathlib
import re
import sys

NEW = "KBase Data Lakehouse"

# Uppercase only: the lowercase form is an identifier, never prose.
BERDL = re.compile(r"\bBERDL\b")
# "BERDL Database" named the platform, so the noun goes with the name;
# "KBase Data Lakehouse Database" would say it twice.
BERDL_DB = re.compile(r"\bBERDL Database\b")
OLD_LAKEHOUSE = re.compile(r"\bKBase\s+BER\s+Data\s+Lakehouse\b|\bBER\s+[Dd]ata\s+[Ll]akehouse\b")
# "in KBase Data Lakehouse" reads wrong; "in the KBase Data Lakehouse" does not.
NEEDS_ARTICLE = re.compile(
    r"\b(in|to|from|of|within|across|against|into|through|over|queried|using|via)\s+"
    rf"(?!the\b)({re.escape(NEW)})"
)
# The one name that is a project's, not the platform's. It is masked rather
# than used to skip the text around it: a paragraph that mentions the project
# usually mentions the platform too, and only the project name is spared.
KEEP = re.compile(r"BERDL Data Atlas")
MASK = "\x00KEEP\x00"

TARGETS = (
    ("wiki", "*.md"),  # the catalog and the log
    ("wiki/concepts", "*.md"),
    ("wiki/entities", "*.md"),
    ("wiki/summaries", "*.md"),
    ("wiki-extra", "**/*.md"),
)


def protect(line: str) -> bool:
    """Lines whose text is a name, a link label, or machinery."""
    s = line.lstrip()
    return (
        # A summary's title is the wiki's own, so it is renamed like its prose;
        # the raw report under wiki/sources keeps the title it was written with.
        s.startswith("<!--")  # the tension hash and other machinery
        or s.startswith("> ")  # provenance callouts are generated, not prose
        or (":" in s.split(" ")[0] and s.split(":")[0] in {"type", "sources", "full_text", "doc_type"})
    )


def fix(text: str) -> tuple[str, int]:
    out, n = [], 0
    for line in text.splitlines(keepends=True):
        if protect(line):
            out.append(line)
            continue
        # In [[target|label]] the target is a slug and the label is prose.
        parts = re.split(r"(\[\[[^\]]*\]\])", line)
        rebuilt = []
        for part in parts:
            if part.startswith("[["):
                if "|" in part:
                    target, label = part.split("|", 1)
                    label = KEEP.sub(MASK, label)
                    label = BERDL.sub(NEW, BERDL_DB.sub(NEW, OLD_LAKEHOUSE.sub(NEW, label)))
                    label = NEEDS_ARTICLE.sub(r"\1 the \2", label)
                    part = f"{target}|{label}".replace(MASK, "BERDL Data Atlas")
                rebuilt.append(part)
                continue
            before = part
            part = KEEP.sub(MASK, part)
            part = OLD_LAKEHOUSE.sub(NEW, part)
            part = BERDL_DB.sub(NEW, part)
            part = BERDL.sub(NEW, part)
            part = NEEDS_ARTICLE.sub(r"\1 the \2", part)
            part = part.replace(MASK, "BERDL Data Atlas")
            n += before != part
            rebuilt.append(part)
        out.append("".join(rebuilt))
    return "".join(out), n


def main() -> int:
    root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    changed = touched = 0
    for sub, glob in TARGETS:
        for path in sorted((root / sub).glob(glob)):
            if not path.is_file():
                continue
            text = path.read_text(encoding="utf-8")
            new, n = fix(text)
            if new != text:
                path.write_text(new, encoding="utf-8")
                changed += n
                touched += 1
    print(f"normalize_names: {changed} line(s) renamed across {touched} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
