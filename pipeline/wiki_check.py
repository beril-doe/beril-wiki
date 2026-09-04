#!/usr/bin/env python3
"""Post-compile citation and numeric-fidelity checks for the OpenKB wiki.

Carried over from the v2 compendium's citation-whitelist idea, recast as a
checker over OpenKB output. Run after every `openkb add` / `recompile`:

    python3 wiki_check.py [<kb-root>]

Checks (concepts/ and entities/ pages):
  ERROR  [src: id] cites an id with no corresponding source document
  WARN   a paragraph containing figures (numbers/percentages) has no [src:] tag
  WARN   a number in a cited paragraph appears in none of its cited sources

Exit code 1 if any ERROR, else 0. WARNs are reported but do not fail.
"""

from __future__ import annotations

import pathlib
import re
import sys

SRC_TAG = re.compile(r"\[src:\s*([^\]]+)\]")
WIKILINK = re.compile(r"\[\[([^\]|#]+?)(?:[|#][^\]]*)?\]\]")
ORCID = re.compile(r"\b\d{4}-\d{4}-\d{4}-\d{3}[\dXx]\b")
# Numbers worth verifying: decimals, percentages, thousands-separated, or >=4 digits.
# Skips small integers (list positions, "3 lines of evidence") to avoid noise.
#
# Ordering and boundaries both carry weight, and the previous one-line version got
# them wrong in ways that silently disabled the check:
#   - scientific notation must come FIRST, or `1.3e-43` matches the decimal
#     alternative and is verified as the mantissa `1.3` alone — every p-value in
#     the corpus was effectively unchecked.
#   - the tail guard must reject only a CONTINUING number (`,` then a digit).
#     Rejecting any following comma dropped `0.038,` in prose, so ordinary
#     decimals never got verified.
#   - the identifier guards keep Pfam/assembly accessions out: without them
#     `PF00034` and `PF13442` are read as the figures 00034 and 13442.
NUMBER = re.compile(r"""
    (?<![\w.])
    (?:
        \d[\d,]*(?:\.\d+)?[eE][-+]?\d+     # 1.3e-43, 2.0E+4  (must precede the decimal rule)
      | \d[\d,]*\.\d+\s?%                  # 59.3%
      | \d[\d,]*\.\d+(?!\d|,\d)            # 0.038, 1,234.56
      | \d[\d,]*\d\s?% | \d\s?%            # 66%, 7%
      | \d[\d,]{2,}\d(?!\d|,\d)            # 7,609, 10000
    )
""", re.X)
# NOTE: no trailing (?!\w) guard. The LEADING guard already excludes identifiers
# (PF00034, GCF_000005845 — their digits follow a letter or underscore), while a
# trailing one also rejects unit suffixes: sources write "+7.8pp" and "18.8M", so
# it made those figures invisible and every page quoting them looked unsupported.

_SRC_NUMS: dict[tuple[str, int], set[str]] = {}


def norm_num(tok: str) -> str:
    """Percent-insensitive on purpose: sources routinely state a proportion that a
    page renders as a percentage, and treating `%` as significant flags 143 such
    pairs on this corpus against 28 genuine misses."""
    return tok.replace(",", "").replace(" ", "").rstrip("%")


def prose_only(par: str) -> str:
    """Paragraph text with citation tags and wikilink TARGETS removed.

    A link target is a filename, not a claim: `[[conflicts/conflict--a--b--57107100]]`
    carries the 8-hex set-digest this repo puts in conflict slugs, and reading it
    as the figure 57107100 invents a violation the prose never made."""
    text = WIKILINK.sub(lambda m: m.group(0).split("|", 1)[1][:-2] if "|" in m.group(0) else " ",
                        SRC_TAG.sub("", par))
    # ORCIDs are identifiers: 0000-0003-2728-7671 is four 4-digit "figures".
    return ORCID.sub(" ", text)


def numbers_in(text: str) -> set[str]:
    """Figures in `text`, plus the MANTISSA of every scientific value.

    A source writing `p = 1.77e-06` yields one token, so a page quoting the same
    result as `1.77 x 10^-6` — whose exponent is not ASCII scientific notation —
    matched nothing. Emitting `1.77` as well makes the two spellings agree."""
    out = set()
    for t in NUMBER.findall(text):
        n = norm_num(t)
        out.add(n)
        m = re.match(r"([\d.]+)[eE][-+]?\d+$", n)
        if m:
            out.add(m.group(1))
    return out


def source_numbers(sid: str, text: str) -> set[str]:
    """Tokenized figures of one source, memoized — validate_page runs per paragraph."""
    key = (sid, len(text))
    if key not in _SRC_NUMS:
        _SRC_NUMS[key] = numbers_in(text)
    return _SRC_NUMS[key]


def _derivable(val: float, pool: set[float]) -> bool:
    """True if `val` is a difference or ratio of two figures in the cited sources.

    A concept page legitimately computes across its sources: "core 24.4% vs
    non-core 16.6%" supports a stated "+7.8 percentage-point excess" that appears
    nowhere verbatim. Accepting these is a deliberate loosening — with pools of
    20-40 figures a coincidental pair is entirely possible, so a derivable value
    is REPORTED in its own class rather than silently passed, and it is never
    accepted at write time in compile.validate_page."""
    xs = sorted(pool)
    for i, a in enumerate(xs):
        for b in xs[i + 1:]:
            if abs(abs(a - b) - abs(val)) < 0.0051:
                return True
            if b and abs(abs(a / b) - abs(val)) < 0.0051:
                return True
    return False


def _as_float(tok: str) -> float | None:
    try:
        return float(tok.replace(",", "").replace(" ", "").rstrip("%"))
    except ValueError:
        return None


def derivable_numbers(par: str, ids: list[str], sources: dict[str, str]) -> set[str]:
    """Of the unsupported figures in `par`, those computable from cited figures."""
    known = [s for s in ids if s in sources]
    if not known:
        return set()
    pool = {v for v in (_as_float(t) for s in known for t in source_numbers(s, sources[s]))
            if v is not None}
    out = set()
    for tok in unsupported_numbers(par, ids, sources):
        v = _as_float(tok)
        if v is not None and _derivable(v, pool):
            out.add(tok)
    return out


def unsupported_numbers(par: str, ids: list[str], sources: dict[str, str]) -> list[str]:
    """Figures in `par` that appear in NONE of its cited sources.

    Matches whole tokens against each source's tokenized figures rather than
    substring-searching a concatenation of them. The substring form passed
    `12%` against a source containing only `123.4%`, `66%` against a bare count
    `66`, and `2.4%` against a source whose only `2.4` was the version string
    `v2.4`."""
    known = [s for s in ids if s in sources]
    if not known:
        return []
    allowed = set().union(*(source_numbers(s, sources[s]) for s in known))
    return [t for t in NUMBER.findall(prose_only(par)) if norm_num(t) not in allowed]


def source_ids(kb: pathlib.Path) -> dict[str, str]:
    """Map source id -> source text. Ids match the [src: <id>] convention:
    the staging filename minus __REPORT.md / .md."""
    texts: dict[str, str] = {}
    # wiki/sources is the committed in-corpus copy, so a fresh clone without a
    # populated staging/ can still run every check.
    for d in (kb / "staging", kb / "raw", kb / "wiki" / "sources"):
        if not d.is_dir():
            continue
        for f in d.glob("*.md"):
            sid = re.sub(r"__REPORT$", "", f.stem)
            texts.setdefault(sid, f.read_text(encoding="utf-8", errors="replace"))
    return texts


def paragraphs(body: str) -> list[str]:
    # Fold bullet lists into their own paragraphs; skip headings and frontmatter.
    # Literature Context sections cite external papers (PMID-verified by
    # lit_context.py), so their numbers are exempt from corpus-source checks.
    body = re.sub(r"^---\n.*?\n---\n", "", body, flags=re.S)
    # Forward-looking sections propose future work rather than asserting
    # evidence, so their figures have nothing to cite: "Re-run the comparison at
    # n=500" is a plan, not a claim. Literature Context is exempt for the
    # adjacent reason — it cites external PMIDs, verified by lit_context.py.
    body = re.sub(r"^## (Literature Context|Open Directions|Resolving Work|Possible Reconciliations)"
                  r"\s*\n.*?(?=\n## |\Z)", "", body, flags=re.M | re.S)
    return [p.strip() for p in re.split(r"\n\s*\n", body) if p.strip() and not p.lstrip().startswith("#")]


def cited_ids(par: str) -> list[str]:
    ids: list[str] = []
    for m in SRC_TAG.finditer(par):
        for part in re.split(r"[,;]", m.group(1)):
            sid = re.sub(r"__REPORT$", "", part.strip())
            if sid and sid not in ids:
                ids.append(sid)
    return ids


def is_table_or_links(par: str) -> bool:
    """Tables and link-list bullets get cited at section level; don't warn on them."""
    lines = [ln.strip() for ln in par.splitlines() if ln.strip()]
    return all(ln.startswith("|") or ln.startswith("- [[") for ln in lines)


def duplicate_concepts(kb: pathlib.Path) -> list[str]:
    """Near-duplicate concept pairs: heavy source overlap + shared name tokens.

    Shared with compile.py's plan step, which injects the current output so
    extend-don't-duplicate is enforced at write time, not just audited here.
    """
    stops = {"the", "of", "in", "and", "for", "to", "a", "vs", "with"}
    cinfo = []
    for page in (kb / "wiki" / "concepts").glob("*.md"):
        text = page.read_text(encoding="utf-8", errors="replace")
        srcs = set(re.findall(r'summaries/([\w.-]+?)__REPORT', text[:1500]))
        toks = set(page.stem.split("-")) - stops
        cinfo.append((page.stem, srcs, toks))
    out = []
    for i, (a, sa, ta) in enumerate(cinfo):
        for b, sb, tb in cinfo[i + 1:]:
            if sa and sb and len(sa & sb) / max(1, len(sa | sb)) >= 0.5 and len(ta & tb) >= 2:
                out.append(f"duplicate-concepts? '{a}' and '{b}' share {len(sa & sb)} sources and name tokens {sorted(ta & tb)}")
    return out


def main() -> int:
    argv = [a for a in sys.argv[1:] if not a.startswith("--")]
    kb = pathlib.Path(argv[0]) if argv else pathlib.Path(__file__).parent.parent
    sources = source_ids(kb)
    if not sources:
        print(f"wiki_check: no sources found under {kb}/staging or {kb}/raw", file=sys.stderr)
        return 1

    # --strict promotes numeric mismatches and dead links from warning to error.
    # They are warnings by default because this corpus carries pre-existing
    # violations that predate the check being able to see them; turn it on once
    # they are repaired and the gate becomes meaningful.
    strict = "--strict" in sys.argv
    errors: list[str] = []
    warns: list[str] = []
    n_pages = n_cited_pars = n_numeric_pars = n_derived = 0

    # Every LLM-written publishable collection, not just three of them. Conflict
    # pages and author profiles were unscanned, which is how eight unsupported
    # figures and 26 dead concept links reached publish with the gate reporting
    # zero errors.
    roots = [(kb / "wiki", "concepts"), (kb / "wiki", "entities"),
             (kb / "wiki-extra", "topics"), (kb / "wiki-extra", "conflicts"),
             (kb / "wiki-extra", "authors")]
    for base, sub in roots:
        for page in sorted((base / sub).glob("*.md")):
            n_pages += 1
            rel = f"{sub}/{page.name}"
            for i, par in enumerate(paragraphs(page.read_text(encoding="utf-8", errors="replace")), 1):
                ids = cited_ids(par)
                nums = NUMBER.findall(prose_only(par))
                if ids:
                    n_cited_pars += 1
                unknown = [s for s in ids if s not in sources]
                for s in unknown:
                    errors.append(f"{rel} ¶{i}: unknown source id [src: {s}]")
                if nums and not ids:
                    warns.append(f"{rel} ¶{i}: {len(nums)} figure(s) but no [src:] citation: {par[:90]!r}")
                    continue
                if nums and ids:
                    n_numeric_pars += 1
                    bad = unsupported_numbers(par, ids, sources)
                    deriv = derivable_numbers(par, ids, sources) if bad else set()
                    for tok in bad:
                        if tok in deriv:
                            n_derived += 1
                            continue
                        msg = f"{rel} ¶{i}: number {tok!r} not found in cited source(s) {ids}"
                        (errors if strict else warns).append(msg)

    # Dead [[wikilinks]]. compile.generate_page validates targets at write time,
    # but topics_build, conflicts_build and authors_build use their own llm() and
    # never did, so their pages accumulated links to concepts that no longer
    # exist. quartz_ingest downgrades them at publish, which hid the problem
    # rather than fixing it.
    targets = {str(f.relative_to(b)).removesuffix(".md")
               for b in (kb / "wiki", kb / "wiki-extra") if b.is_dir()
               for f in b.rglob("*.md")}
    for base, sub in roots:
        for page in sorted((base / sub).glob("*.md")):
            text = page.read_text(encoding="utf-8", errors="replace")
            dead = sorted({m.group(1).strip().lstrip("/") for m in WIKILINK.finditer(text)}
                          - targets)
            for d in dead:
                msg = f"{sub}/{page.name}: link [[{d}]] targets a page that does not exist"
                (errors if strict else warns).append(msg)

    # Integration-depth audit: every project should feed >=2 concept/topic pages.
    uptake: dict[str, int] = {}
    proj_ids = {s for s in sources if not s.startswith(("discoveries", "pitfalls"))}
    for base, sub in [(kb / "wiki", "concepts"), (kb / "wiki-extra", "topics")]:
        for page in (base / sub).glob("*.md"):
            for sid in set(cited_ids(page.read_text(encoding="utf-8", errors="replace"))):
                if sid in proj_ids:
                    uptake[sid] = uptake.get(sid, 0) + 1
    for p in sorted(proj_ids):
        if uptake.get(p, 0) < 2:
            warns.append(f"uptake: project '{p}' cited by only {uptake.get(p, 0)} concept/topic page(s) — under-integrated")

    warns.extend(duplicate_concepts(kb))

    print(f"wiki_check: {n_pages} pages, {n_cited_pars} cited paragraphs, "
          f"{n_numeric_pars} numeric paragraphs verified against {len(sources)} sources")
    for w in warns:
        print(f"  WARN  {w}")
    for e in errors:
        print(f"  ERROR {e}")
    if n_derived:
        print(f"  NOTE  {n_derived} figure(s) not verbatim in a cited source but derivable from "
              f"two of its figures (a difference or ratio) — accepted, not verified")
    print(f"wiki_check: {len(errors)} error(s), {len(warns)} warning(s), {n_derived} derived")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
