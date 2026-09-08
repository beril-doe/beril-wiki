"""Native OKF metadata, relative links and deterministic legacy normalization."""
from __future__ import annotations

import argparse
import os
from pathlib import Path
import re
import tempfile
from urllib.parse import quote, unquote, urlsplit

import yaml

FM = re.compile(r"\A---\n(.*?)\n---\n?", re.S)
SRC = re.compile(r"\[src:\s*([^\]]+)\]")
REF = re.compile(r"\[\^([^\]]+)\](?!:)")
DEFINITION = re.compile(r"^\[\^[^\]]+\]:[^\n]*(?:\n(?: {4}|\t)[^\n]*)*\n?", re.M)
LINK = re.compile(r"(!?\[[^\]\n]*\]\()([^\s)]+)([^)]*\))")


def parse(text: str) -> tuple[dict, str]:
    match = FM.match(text)
    if not match:
        return {}, text
    fields = yaml.safe_load(match[1]) or {}
    if not isinstance(fields, dict):
        raise ValueError("frontmatter must be a mapping")
    return fields, text[match.end():]


def map_prose(text: str, transform) -> str:
    """Transform Markdown outside fenced and inline code, retaining bytes there."""
    out = []
    prose_lines = []
    fence = ""
    def flush():
        chunks = re.split(r"(`+[^`\n]*`+)", "".join(prose_lines))
        out.append("".join(c if j % 2 else transform(c) for j, c in enumerate(chunks)))
        prose_lines.clear()
    for line in text.splitlines(keepends=True):
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})", line)
        if fence:
            out.append(line)
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= len(fence) and not line[marker.end():].strip():
                fence = ""
        elif marker:
            flush()
            fence = marker[1]
            out.append(line)
        else:
            prose_lines.append(line)
    flush()
    return "".join(out)


def map_links(text: str, transform) -> str:
    return map_prose(text, lambda chunk: LINK.sub(lambda m: m[1] + transform(m[2]) + m[3], chunk))


def source_id(entry) -> str:
    if isinstance(entry, dict):
        return str(entry.get("id") or "")
    return Path(str(entry)).stem.removesuffix("__REPORT")


def cited_ids(text: str) -> list[str]:
    found = []
    def collect(chunk):
        for match in SRC.finditer(chunk):
            found.extend(source_id(s.strip()) for s in re.split(r"[,;]", match[1]) if s.strip())
        found.extend(REF.findall(chunk))
        return chunk
    map_prose(map_prose(parse(text)[1], lambda chunk: DEFINITION.sub("", chunk)), collect)
    fields, _ = parse(text)
    if fields and "sources" in fields:
        allowed = {source_id(record) for record in fields["sources"]}
        found = [sid for sid in found if sid in allowed]
    return list(dict.fromkeys(found))


def body(text: str) -> str:
    return map_prose(parse(text)[1], lambda chunk: DEFINITION.sub("", chunk)).rstrip() + "\n"


def prose(text: str) -> str:
    text = SRC.sub("", text)
    text = REF.sub("", text)
    return LINK.sub(lambda m: m[1][m[1].find("[") + 1:-2], text)


def corpus_root(path: Path) -> Path:
    return next((p.parent for p in path.parents if p.name in {"wiki", "wiki-extra"}), path.parent)


def relative(page: Path, target: Path) -> str:
    return Path(os.path.relpath(target, page.parent)).as_posix()


def rebase(text: str, source: Path, destination: Path) -> str:
    """Keep relative Markdown links attached to their original targets."""
    def relocate(url):
        parts = urlsplit(url)
        if parts.scheme or parts.netloc:
            return url
        target = source.parent / unquote(parts.path) if parts.path else source
        suffix = ("?" + parts.query if parts.query else "") + ("#" + parts.fragment if parts.fragment else "")
        return quote(relative(destination, target), safe="/") + suffix
    return map_links(text, relocate)


def excerpt(text: str, original: str, source: Path, destination: Path) -> str:
    """Relocate an extracted section, carrying only its referenced footnotes."""
    ids = set(cited_ids(text))
    definitions = []
    def collect(chunk):
        for match in DEFINITION.finditer(chunk):
            sid = re.match(r"\[\^([^\]]+)\]", match[0])[1]
            if sid in ids:
                definitions.append(match[0].rstrip())
        return chunk
    map_prose(parse(original)[1], collect)
    joined = text.rstrip() + ("\n\n" + "\n\n".join(definitions) if definitions else "")
    return rebase(joined, source, destination)


def normalize_log(content: str) -> str:
    groups = {}
    preamble = []
    date = None
    for line in content.splitlines():
        legacy = re.match(r"^## \[(\d{4}-\d{2}-\d{2}) ([^\]]+)\](.*)$", line)
        current = re.match(r"^## (\d{4}-\d{2}-\d{2})\s*$", line)
        if legacy:
            date = legacy[1]
            groups.setdefault(date, []).append(f"- [{legacy[1]} {legacy[2]}]{legacy[3]}")
        elif current:
            date = current[1]
            groups.setdefault(date, [])
        elif date is not None:
            groups[date].append(line)
        else:
            preamble.append(line)
    if not groups:
        return content
    return "\n".join(preamble).rstrip() + "\n\n" + "\n\n".join(
        f"## {day}\n\n" + "\n".join(groups[day]).strip() for day in sorted(groups, reverse=True)) + "\n"


def normalize(text: str, path: Path, root: Path | None = None) -> str:
    root = root or corpus_root(path)
    fields, content = parse(text)
    old_fields = dict(fields)
    if "sources" in fields and not isinstance(fields["sources"], list):
        raise ValueError(f"{path}: sources must be a list")
    for entry in fields.get("sources", []):
        if isinstance(entry, dict) and (not isinstance(entry.get("resource"), str) or not entry["resource"]):
            raise ValueError(f"{path}: source resource is required")
        if not isinstance(entry, (str, dict)):
            raise ValueError(f"{path}: invalid source record")
    reserved = path.name in {"index.md", "log.md"}
    heading = re.search(r"^# (.+)$", content, re.M)
    legacy_syntax = []
    map_prose(content, lambda chunk: (legacy_syntax.append(bool(SRC.search(chunk) or "[[" in chunk)) or chunk))
    legacy_metadata = not fields or any(isinstance(s, str) for s in fields.get("sources", [])) or any(legacy_syntax)
    if legacy_metadata:
        fields.setdefault("title", heading[1].strip() if heading else path.stem.replace("-", " ").title())
    family = path.parent.name
    fields.setdefault("type", {"sources": "Source", "summaries": "Summary", "concepts": "Concept",
                               "entities": "Entity", "topics": "Topic", "conflicts": "Conflict",
                               "authors": "Person", "data": "Dataset"}.get(family, "Index" if path.stem == "index" else "Note"))
    records = {}
    explicit_ids = set()
    for index, entry in enumerate(fields.get("sources") or []):
        if isinstance(entry, dict) and entry.get("id"):
            if entry["id"] in explicit_ids:
                raise ValueError(f"{path}: duplicate source ID {entry['id']}")
            explicit_ids.add(entry["id"])
        sid = source_id(entry) or (f"external-{index}" if isinstance(entry, dict) else "")
        if sid:
            records[sid] = dict(entry) if isinstance(entry, dict) else {"id": sid}
    legacy_ids = []
    def citations(chunk):
        def replace(m):
            ids = [source_id(s.strip()) for s in re.split(r"[,;]", m[1]) if s.strip()]
            legacy_ids.extend(ids)
            return "".join(f"[^{sid}]" for sid in ids)
        return SRC.sub(replace, chunk)
    content = map_prose(content, citations)
    for sid in cited_ids(content):
        stem = sid if sid in {"discoveries", "pitfalls"} else sid + "__REPORT"
        if (root / "wiki" / "sources" / f"{stem}.md").exists() or (root / "wiki" / "summaries" / f"{stem}.md").exists():
            legacy_ids.append(sid)
    for sid in legacy_ids:
        records.setdefault(sid, {"id": sid})
    # A summary's own evidence refers to the raw report, avoiding a self edge.
    for sid, record in records.items():
        if not record.get("resource"):
            stem = sid if sid in {"discoveries", "pitfalls"} else sid + "__REPORT"
            collection = "sources" if family == "summaries" else "summaries"
            record["resource"] = relative(path, root / "wiki" / collection / f"{stem}.md")
            record.setdefault("title", sid.replace("_", " ").replace("-", " "))
    if records or "sources" in fields:
        fields["sources"] = list(records.values())
    def wikilinks(chunk):
        def replace(m):
            target, _, label = m[1].partition("|")
            target, marker, fragment = target.partition("#")
            target = target.lstrip("/").removesuffix(".md")
            primary = root / "wiki" / f"{target}.md"
            extra = root / "wiki-extra" / f"{target}.md"
            dest = primary if primary.exists() or target.split("/")[0] in {"summaries", "sources", "concepts", "entities", "catalog"} else extra
            if target == "catalog":
                dest = root / "wiki" / "index.md"
            return f"[{label or target.rsplit('/', 1)[-1]}]({relative(path, dest)}{marker}{fragment})"
        return re.sub(r"\[\[([^\]]+)\]\]", replace, chunk)
    content = map_prose(content, wikilinks)
    if family == "sources":
        project = path.stem.removesuffix("__REPORT")
        content = map_links(content, lambda url: relative(path, root / "wiki" / "figures" / project / url.removeprefix("figures/")) if url.startswith("figures/") else url)
    if fields.get("full_text", "").startswith("sources/"):
        fields["full_text"] = relative(path, root / "wiki" / fields["full_text"])
    seen_definitions = {}
    def unique_definitions(chunk):
        def keep(match):
            sid = re.match(r"\[\^([^\]]+)\]", match[0])[1]
            definition = match[0].rstrip()
            if sid in seen_definitions:
                if seen_definitions[sid] != definition:
                    raise ValueError(f"{path}: conflicting definitions for {sid}")
                return ""
            seen_definitions[sid] = definition
            return match[0]
        return DEFINITION.sub(keep, chunk)
    content = map_prose(content, unique_definitions)
    definitions = set(re.findall(r"^\[\^([^\]]+)\]:", content, re.M))
    missing = [sid for sid in dict.fromkeys(legacy_ids) if sid not in definitions]
    if missing:
        content = content.rstrip() + "\n\n" + "\n".join(f"[^{sid}]: [{records[sid].get('title') or sid}]({records[sid]['resource']})" for sid in missing) + "\n"
    if reserved:
        fields = {"okf_version": fields["okf_version"]} if "okf_version" in fields else {}
        if path.name == "log.md":
            content = normalize_log(content)
    elif old_fields and not old_fields.get("type") and all(isinstance(s, dict) for s in old_fields.get("sources", [])):
        raise ValueError(f"{path}: native metadata is missing type")
    if fields == old_fields and content == parse(text)[1]:
        return text
    return ("---\n" + yaml.safe_dump(fields, sort_keys=False, allow_unicode=True).rstrip() + "\n---\n" if fields else "") + content


def atomic_write(path: Path, text: str) -> int:
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent, prefix=f".{path.name}.", delete=False) as stream:
            temporary = Path(stream.name)
            stream.write(text)
        if path.exists():
            temporary.chmod(path.stat().st_mode)
        os.replace(temporary, path)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()
    return len(text)


def write(path: Path, text: str, **kwargs) -> int:
    if path.exists():
        previous = path.read_text(encoding="utf-8")
        prior, old_content = parse(previous)
        fields, content = parse(text)
        definitions = set(re.findall(r"^\[\^([^\]]+)\]:", content, re.M))
        used = set(REF.findall(DEFINITION.sub("", content)))
        for match in DEFINITION.finditer(old_content):
            sid = re.match(r"\[\^([^\]]+)\]", match[0])[1]
            if sid in used and sid not in definitions:
                content = content.rstrip() + "\n\n" + match[0].rstrip() + "\n"
                definitions.add(sid)
        text = "---\n" + yaml.safe_dump(prior | fields, sort_keys=False, allow_unicode=True) + "---\n" + content
    native = normalize(text, path)
    errors = validate(corpus_root(path), {path: native}, check_links=False)
    if errors:
        raise ValueError("; ".join(errors))
    return atomic_write(path, native)


def upgrade(root: Path) -> int:
    before = {}
    for base in (root / "wiki", root / "wiki-extra"):
        for path in sorted(base.rglob("*.md")):
            before[path] = path.read_text(encoding="utf-8")
    after = {path: normalize(text, path, root) for path, text in before.items()}
    index = root / "wiki-extra" / "index.md"
    home = root / "wiki-extra" / "home.md"
    if index in before and home not in before and "##" in parse(before[index])[1]:
        after[home] = normalize(before[index], home, root)
        after[index] = normalize("# Supplementary Knowledge Index\n\n- [Research overview](home.md)\n", index, root)
    changed = sum(before.get(path) != text for path, text in after.items())
    if changed:
        errors = validate(root, after, check_links=False)
        if errors:
            raise ValueError("; ".join(errors))
        from okf_cache import rekey
        rekey(root, before, after)
        for path, text in after.items():
            if before.get(path) != text:
                atomic_write(path, text)
    return changed


def validate(root: Path, texts: dict[Path, str] | None = None, check_links: bool = True) -> list[str]:
    errors = []
    if texts is None:
        texts = {path: path.read_text(encoding="utf-8") for base in (root / "wiki", root / "wiki-extra") for path in sorted(base.rglob("*.md"))}
    for path, text in texts.items():
            try:
                fields, content = parse(text)
            except (ValueError, yaml.YAMLError) as exc:
                errors.append(f"{path.relative_to(root)}: invalid metadata: {exc}")
                continue
            issues = []
            if path.name not in {"index.md", "log.md"} and (not isinstance(fields.get("type"), str) or not fields["type"].strip()):
                issues.append("missing type")
            if path.name in {"index.md", "log.md"} and any(k in fields for k in ("type", "title")):
                issues.append("reserved index/log metadata")
            if "title" in fields and not isinstance(fields["title"], str):
                issues.append("invalid title")
            records = fields.get("sources") or []
            if not isinstance(records, list) or any(not isinstance(r, dict) or not isinstance(r.get("resource"), str) or not r["resource"] for r in records):
                issues.append("invalid source records")
                records = []
            ids = [r["id"] for r in records if "id" in r]
            if any(not isinstance(value, str) for r in records for key, value in r.items() if key in {"id", "title"}):
                issues.append("invalid source id/title")
                ids = [value for value in ids if isinstance(value, str)]
            if len(set(ids)) != len(ids):
                issues.append("duplicate source IDs")
            def check(chunk):
                if SRC.search(chunk) or re.search(r"\[\[", chunk):
                    issues.append("legacy citation/link")
                return chunk
            map_prose(content, check)
            definitions = set(re.findall(r"^\[\^([^\]]+)\]:", content, re.M))
            for sid in cited_ids(content):
                if sid not in definitions:
                    issues.append(f"undefined footnote {sid}")
            def check_link(url, source=False):
                if not check_links:
                    return url
                parts = urlsplit(url)
                if not parts.scheme and not parts.netloc and parts.path.endswith(".md"):
                    target = (path.parent / unquote(parts.path)).resolve()
                    if not target.is_file() and (source or path.parent.name != "sources"):
                        issues.append(f"missing target {url}")
                return url
            map_links(content, check_link)
            for record in records:
                check_link(record["resource"], source=True)
            errors.extend(f"{path.relative_to(root)}: {issue}" for issue in dict.fromkeys(issues))
    return errors


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path, nargs="?", default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if not args.check:
        print(f"OKF: upgraded {upgrade(args.root)} pages")
    failures = validate(args.root)
    print("\n".join(failures) if failures else "OKF: valid")
    raise SystemExit(bool(failures))
