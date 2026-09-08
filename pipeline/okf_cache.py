"""Rekey only caches whose old inputs still match during format normalization."""
from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path
import re

import okf


def digest(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()[:16]


def rekey(root: Path, before: dict[Path, str], after: dict[Path, str]) -> None:
    """Preserve valid cached work; never mark a genuinely stale entry current."""
    def update(name, change):
        path = root / "state" / name
        if not path.exists():
            return
        state = json.loads(path.read_text())
        old = json.dumps(state, sort_keys=True)
        change(state)
        if json.dumps(state, sort_keys=True) != old:
            path.write_text(json.dumps(state, indent=1, sort_keys=True) + "\n")

    def cas(state, key, old, new):
        if state.get(key) == digest(old):
            state[key] = digest(new)

    # Conflict groups can combine several project sets. Recover an exact old
    # hash from bounded combinations, not from similarity or a new model call.
    tension = re.compile(r"^## Tensions?\s*\n(.*?)(?=\n## |\Z)", re.M | re.S)
    groups = {}
    for p, text in sorted(before.items()):
        if p.parent != root / "wiki/concepts":
            continue
        old_match = tension.search(text)
        new_match = tension.search(after[p])
        if old_match and new_match:
            old, new = old_match[1].strip(), new_match[1].strip()
            ids = tuple(sorted(okf.cited_ids(old)))
            if len(ids) >= 2:
                groups.setdefault(ids, []).append((old, new))
    for p, text in before.items():
        if p.parent != root / "wiki-extra/conflicts":
            continue
        match = re.search(r"<!-- tension-hash: (\w+) -->", text)
        if not match:
            continue
        source_ids = set(okf.cited_ids(text))
        candidates = [key for key in sorted(groups) if set(key) <= source_ids]
        # At most 4095 candidates per page; retain an unmatched stale hash.
        if len(candidates) > 12:
            continue
        for size in range(1, len(candidates) + 1):
            found = False
            for selection in itertools.combinations(candidates, size):
                blocks = [block for key in selection for block in groups[key]]
                if digest("\n".join(old for old, _ in blocks)) == match[1]:
                    new_hash = digest("\n".join(new for _, new in blocks))
                    after[p] = after[p].replace(match[0], f"<!-- tension-hash: {new_hash} -->")
                    found = True
                    break
            if found:
                break


    pairs = [(p, text, after[p]) for p, text in before.items() if p in after and text != after[p]]
    update("enrich.json", lambda state: [cas(state, p.name, old, new)
           for p, old, new in pairs if p.parent == root / "wiki/summaries"])
    from figures_build import PROMPT_V as figure_version
    def figures(state):
        for p, old, new in pairs:
            rel = p.relative_to(root).as_posix().split("/", 1)[1]
            cas(state, rel, figure_version + old, figure_version + new)
    update("figures-state.json", figures)

    def placements(state):
        for p, old, new in pairs:
            rel = p.relative_to(root).as_posix().split("/", 1)[1]
            if rel in state:
                cas(state[rel], "page_hash", old, new)
    update("figures-placements.json", placements)
    from lit_context import SECTION
    update("litcontext.json", lambda state: [cas(state, p.name, SECTION.sub("", old), SECTION.sub("", new))
           for p, old, new in pairs if p.parent == root / "wiki-extra/topics"])

    from authors_build import PER_SUMMARY_CHARS, author_projects
    def authors(state):
        for p, text in before.items():
            if p.parent != root / "wiki-extra/authors" or p.stem == "index":
                continue
            heading = re.search(r"^# (.+)$", text, re.M)
            name = heading[1].strip() if heading else p.stem
            projects = sorted(author_projects(text))
            def inputs(snapshot):
                return name + "".join(pid + okf.parse(snapshot[q])[1][:PER_SUMMARY_CHARS]
                    for pid in projects if (q := root / "wiki/summaries" / f"{pid}__REPORT.md") in snapshot)
            cas(state, p.name, inputs(before), inputs(after))
    update("authors.json", authors)

    from consolidate_concepts import PROMPT_V
    def consolidation(state):
        for family, second_dir in (("rejected", "concepts"), ("no_evidence", "summaries")):
            records = state.get(family, {})
            for key, value in list(records.items()):
                parts = key.split("|")
                if len(parts) != 4 or parts[0] != PROMPT_V:
                    continue
                a, b = root / "wiki/concepts" / (parts[1] + ".md"), root / "wiki" / second_dir / (parts[2] + ".md")
                if any(p not in before or p not in after for p in (a, b)):
                    continue
                for x, y in ((a, b), (b, a)) if family == "rejected" else ((a, b),):
                    if parts[3] == digest(before[x]) + digest(before[y]):
                        replacement = "|".join(parts[:3] + [digest(after[x]) + digest(after[y])])
                        if replacement != key:
                            records[replacement] = value
                            del records[key]
                        break
    update("consolidate.json", consolidation)

    from topics_build import cluster_concepts, slugify
    def topics(state):
        concepts = {}
        for p, text in sorted(before.items()):
            if p.parent == root / "wiki/concepts" and p.stem != "index":
                fields, _ = okf.parse(text)
                links = set(re.findall(r"\[\[concepts/([\w.-]+?)(?:\|[^\]]*)?\]\]", text))
                concepts[p.stem] = {"sources": {okf.source_id(s) for s in fields.get("sources", [])}, "links": links}
        if not concepts:
            return
        for members in cluster_concepts(concepts):
            key = hashlib.sha256(",".join(members).encode()).hexdigest()[:12]
            name = state.get("__names__", {}).get(key)
            if not name:
                continue
            ids = set().union(*(concepts[s]["sources"] for s in members))
            conflicts = [p for p, text in sorted(before.items())
                         if p.parent == root / "wiki-extra/conflicts" and len({s for s in ids if s in text}) >= 2]
            def inputs(snapshot):
                return "\n".join(snapshot[root / "wiki/concepts" / (s + ".md")] for s in members) + "".join(snapshot[p] for p in conflicts)
            cas(state, slugify(name), inputs(before), inputs(after))
    update("topics-state.json", topics)
