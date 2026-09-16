#!/usr/bin/env python3
"""Figure placement for the wiki: manifest + LLM-chosen placements, cached.

Phase A (deterministic): parse every project report's ![caption](figures/...)
embeds into figures-manifest.json, keeping the caption and the report paragraph
around each embed (what the figure evidences).

Phase B (LLM, cached by page-content hash, pages placed in a worker pool): for
each summary / topic hub / conflict page, ask the model WHERE figures from the
page's cited projects support the text. The model returns structured placements
only — it never rewrites prose. Results go to figures-placements.json; publish/ingest.py splices
them at publish time. Pages whose content hash is unchanged are skipped.

Also emits figures-csv-queue.md: pages the model flags as needing a chart for
tabular/CSV evidence that has no figure (review queue, nothing auto-generated).

    OPENAI_API_KEY=$CBORG_API_KEY OPENAI_BASE_URL=https://api.cborg.lbl.gov \
        uv run python -m beril_wiki.stages.figures
"""

from __future__ import annotations

import hashlib
import json
import os
import pathlib
import re
import sys

from beril_wiki.agentic.prose import PageFailure, parallel, workers
from beril_wiki.agentic.runtime import WorkflowError, atomic_json, completion, configured
from beril_wiki.paths import ROOT, STATE

MODEL = os.environ.get("WIKI_MODEL", "openai/gpt-5.6-luna")
MAX_PLACE = {"summaries": 2, "topics": 3, "conflicts": 1}
MAX_CANDIDATES = 40
PROMPT_V = "v2-flagship"  # bump to invalidate all cached placements

PROMPT = """You place existing figures into a scientific wiki page. You are given the page's
paragraphs (numbered) and candidate figures (numbered), each with its caption and the
report context it illustrates. Place ONLY flagship figures — ones a reader must see to
understand the page's KEY claims, in the context of the reported data. The complete
figure set remains available on the raw project report page, so when in doubt, leave it
out: most pages should get 0-2 figures, and AT MOST {max_place}. Never place decorative,
redundant, or merely-related figures.

Also: if the page discusses quantitative evidence that clearly lacks visual support
(a dense table, a distribution, a correlation described only in prose) and no candidate
figure covers it, add a csv_flag describing what should be visualized.

Reply with ONLY JSON:
{{"placements": [{{"after_paragraph": <int>, "figure": <int>,
                  "caption": "<one-sentence caption, may refine the original>"}}],
  "csv_flags": ["<what to visualize and why>", ...]}}
"""


def paragraphs(body: str) -> list[str]:
    body = re.sub(r"^---\n.*?\n---\n", "", body, flags=re.S)
    return [p.strip() for p in re.split(r"\n\s*\n", body) if p.strip()]


def build_manifest() -> dict[str, list[dict]]:
    """Figure candidates from the committed corpus: wiki/sources report text +
    wiki/figures files (synced by stages.fetch) — no checkout needed."""
    manifest: dict[str, list[dict]] = {}
    for report in sorted((ROOT / "wiki" / "sources").glob("*__REPORT.md")):
        project = re.sub(r"__REPORT$", "", report.stem)
        text = report.read_text(encoding="utf-8", errors="replace")
        figs = []
        for par in paragraphs(text):
            for m in re.finditer(r"!\[([^\]]*)\]\((figures/[^)]+)\)", par):
                path = ROOT / "wiki" / "figures" / project / re.sub(r"^figures/", "", m.group(2))
                if path.exists():
                    ctx = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", par).strip()[:400]
                    figs.append({"file": m.group(2), "caption": m.group(1), "context": ctx})
        if figs:
            manifest[project] = figs
    STATE.mkdir(exist_ok=True)
    (STATE / "figures-manifest.json").write_text(json.dumps(manifest, indent=1))
    return manifest


def cited_projects(text: str, projects: set[str]) -> list[str]:
    ids = set()
    for m in re.finditer(r"\[src:\s*([^\]]+)\]", text):
        for p in re.split(r"[,;]", m.group(1)):
            ids.add(re.sub(r"__REPORT$", "", p.strip()))
    return sorted(ids & projects)


def target_pages() -> list[tuple[str, pathlib.Path]]:
    out = []
    for f in sorted((ROOT / "wiki/summaries").glob("*__REPORT.md")):
        out.append(("summaries", f))
    for sub in ("topics", "conflicts"):
        for f in sorted((ROOT / "wiki" / sub).glob("*.md")):
            out.append((sub, f))
    return out


def main() -> None:
    manifest = build_manifest()
    print(
        f"manifest: {sum(len(v) for v in manifest.values())} figures "
        f"across {len(manifest)} projects"
    )
    state_path = STATE / "figures-state.json"
    state = json.loads(state_path.read_text()) if state_path.exists() else {}
    if "--force" in sys.argv:
        state = {}
        print("  --force: ignoring cached digests")
    placements_path = STATE / "figures-placements.json"
    placements = json.loads(placements_path.read_text()) if placements_path.exists() else {}
    live = {f"{kind}/{path.name}" for kind, path in target_pages()}
    placements = {key: value for key, value in placements.items() if key in live}
    state = {key: value for key, value in state.items() if key in live}
    todo = []
    skipped = 0
    for kind, page in target_pages():
        rel = f"{page.parent.name}/{page.name}" if kind == "summaries" else f"{kind}/{page.name}"
        text = page.read_text(encoding="utf-8", errors="replace")
        if kind == "summaries":
            projs = [re.sub(r"__REPORT$", "", page.stem)]
        else:
            projs = cited_projects(text, set(manifest))
        cands = []
        for p in projs:
            for fig in manifest.get(p, [])[:6]:
                cands.append({"project": p, **fig})
        cands = cands[:MAX_CANDIDATES]
        digest = hashlib.sha256(
            json.dumps([PROMPT_V, text, cands, configured()], sort_keys=True).encode()
        ).hexdigest()[:16]
        if state.get(rel) == digest and (not cands or rel in placements):
            skipped += 1
            continue
        if not cands:
            state[rel] = digest
            placements.pop(rel, None)
            continue
        todo.append((kind, rel, text, cands, digest))

    def place(item: tuple) -> dict | None:
        """One placement job; None when an API-mode reply is unparseable."""
        kind, rel, text, cands, _ = item
        pars = paragraphs(text)
        limit = min(300, 80_000 // max(1, len(pars)))
        par_block = "\n".join(f"[{i}] {p[:limit]}" for i, p in enumerate(pars))
        cand_block = "\n".join(
            f"[{i}] {c['project']}/{c['file']} — caption: {c['caption'][:300]!r} — "
            f"context: {c['context'][:200]!r}"
            for i, c in enumerate(cands)
        )
        prompt = PROMPT
        if configured():
            prompt = (
                prompt.replace(
                    ',\n                  "caption": '
                    '"<one-sentence caption, may refine the original>"',
                    "",
                )
                + "\nCaptions are copied from source reports; return only placement indices."
            )
        resp = (
            completion(
                step=f"figures/{rel}",
                model=MODEL,
                api_key=os.environ.get("OPENAI_API_KEY"),
                base_url=os.environ.get("OPENAI_BASE_URL", "https://api.cborg.lbl.gov"),
                messages=[
                    {"role": "system", "content": prompt.format(max_place=MAX_PLACE[kind])},
                    {
                        "role": "user",
                        "content": f"PAGE PARAGRAPHS:\n{par_block}\n\n"
                        f"CANDIDATE FIGURES:\n{cand_block}",
                    },
                ],
                temperature=0.2,
                timeout=300,
            )
            .choices[0]
            .message.content
        )
        try:
            m = re.search(r"\{.*\}", resp or "", re.S)
            if not m:
                raise json.JSONDecodeError("no JSON object in reply", resp or "", 0)
            data = json.loads(m.group(0))
        except json.JSONDecodeError as exc:
            if configured():
                raise WorkflowError(f"figures/{rel}: invalid placement JSON") from exc
            print(f"  ! unparseable response for {rel}, skipping")
            return None
        if configured():
            valid = (
                isinstance(data, dict)
                and isinstance(data.get("placements"), list)
                and isinstance(data.get("csv_flags", []), list)
                and all(isinstance(flag, str) for flag in data.get("csv_flags", []))
                and all(
                    isinstance(item, dict)
                    and type(item.get("figure")) is int
                    and 0 <= item["figure"] < len(cands)
                    and type(item.get("after_paragraph")) is int
                    and 0 <= item["after_paragraph"] < len(pars)
                    for item in data["placements"]
                )
            )
            if not valid:
                raise WorkflowError(f"figures/{rel}: invalid placement schema or indices")
        placed = []
        for pl in data.get("placements", [])[: MAX_PLACE[kind]]:
            try:
                figure = int(pl["figure"])
                if not 0 <= figure < len(cands):
                    continue
                c = cands[figure]
                idx = int(pl["after_paragraph"])
            except (KeyError, ValueError, IndexError, TypeError):
                continue
            if 0 <= idx < len(pars):
                placed.append(
                    {
                        "after_paragraph": idx,
                        "project": c["project"],
                        "file": c["file"],
                        "caption": (
                            str(c["caption"])[:300]
                            if configured()
                            else str(pl.get("caption") or c["caption"])[:300]
                        ),
                    }
                )
        return {
            "page_hash": hashlib.sha256(text.encode()).hexdigest()[:16],
            "placements": placed,
            "csv_flags": [str(x)[:300] for x in data.get("csv_flags", [])[:3]],
        }

    calls = 0
    for (_, rel, _, _, digest), result in parallel(todo, place, workers()):
        if result is None or isinstance(result, PageFailure):
            continue
        placements[rel] = result
        state[rel] = digest
        calls += 1
        print(
            f"  {rel}: {len(result['placements'])} placement(s)"
            + (f", {len(result['csv_flags'])} csv flag(s)" if result["csv_flags"] else "")
        )

    atomic_json(placements_path, placements)
    atomic_json(state_path, state)
    csv_flags = {
        rel: item["csv_flags"] for rel, item in placements.items() if item.get("csv_flags")
    }
    if csv_flags:
        lines = [
            "# CSV / visualization review queue",
            "",
            "Pages the placement pass flagged as needing a chart for evidence with no figure.",
            "",
        ]
        for rel, flags in sorted(csv_flags.items()):
            lines.append(f"## {rel}")
            lines += [f"- {f}" for f in flags]
            lines.append("")
        (STATE / "figures-csv-queue.md").write_text("\n".join(lines), encoding="utf-8")
    else:
        (STATE / "figures-csv-queue.md").unlink(missing_ok=True)
    total = sum(len(v["placements"]) for v in placements.values())
    print(
        f"figures: {calls} pages placed, {skipped} unchanged, {total} total placements"
        + (f", csv queue: {sum(len(v) for v in csv_flags.values())} flags" if csv_flags else "")
    )


if __name__ == "__main__":
    main()
