"""Pinned upstream conformance checks and graph rendering over the native wiki.

Only upstream source code is cached. Knowledge pages are read in place.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import shutil
import subprocess
import sys
from urllib.parse import unquote, urlsplit

import okf

VIEWER_REV = "ad30107c31c06aec8a7d5636e0d1058118604e6f"
VALIDATOR_REV = "3e958ae965bf9673fc291859a44feb05a60a9748"


def upstream(root: Path, repo: str, revision: str) -> Path:
    """Fetch a fixed revision once, and refuse modified cached tool code."""
    dest = root / "build" / "tools" / (repo.rsplit("/", 1)[-1] + "-" + revision)
    if not dest.exists():
        dest.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["git", "clone", "--quiet", "--no-checkout", "--filter=blob:none",
                        "https://github.com/" + repo + ".git", str(dest)], check=True)
        subprocess.run(["git", "-C", str(dest), "checkout", "--quiet", "--detach", revision], check=True)
    head = subprocess.check_output(["git", "-C", str(dest), "rev-parse", "HEAD"], text=True).strip()
    dirty = subprocess.check_output(["git", "-C", str(dest), "status", "--porcelain", "--untracked-files=no"], text=True)
    if head != revision or dirty:
        raise ValueError(f"cached tool is not the pinned revision: {dest}")
    return dest


def check(root: Path) -> None:
    validator = upstream(root, "Sudhakaran88/okf-conformance", VALIDATOR_REV)
    for name in ("wiki", "wiki-extra"):
        result = subprocess.run(["node", str(validator / "validator/okf-validate.mjs"),
                                 str(root / name), "--json"], capture_output=True, text=True)
        report = json.loads(result.stdout)
        counts = report["summary"]
        print(f"OKF upstream {name}: {counts['concepts']} concepts, "
              f"{counts['errors']} errors, {counts['warnings']} quality warnings")
        if result.returncode:
            for error in report["errors"]:
                print(error)
            raise ValueError(f"upstream OKF validation failed: {name}")


def graph(root: Path, output: Path) -> dict:
    root = root.resolve()
    viewer = upstream(root, "GoogleCloudPlatform/open-knowledge-format", VIEWER_REV)
    sys.path.insert(0, str(viewer / "src"))
    from reference_agent.viewer import generator as g

    # An in-memory adapter supplies the two collection roots to the upstream UI.
    # No exported or rewritten Markdown tree is created.
    pages = [p for base in (root / "wiki", root / "wiki-extra")
             for p in sorted(base.rglob("*.md")) if p.name not in {"index.md", "log.md"}]
    page_set = set(pages)
    concepts = []
    assets = output.parent / "okf-assets"
    for page in pages:
        fm, body = okf.parse(page.read_text(encoding="utf-8"))
        links = []

        def target(url: str) -> str:
            parts = urlsplit(url)
            if parts.scheme or parts.netloc or not parts.path:
                return url
            dest = (page.parent / unquote(parts.path)).resolve()
            try:
                rel = dest.relative_to(root)
            except ValueError:
                return url
            if rel.parts[0] not in {"wiki", "wiki-extra"}:
                return url
            if dest in page_set:
                cid = rel.with_suffix("").as_posix()
                links.append(cid)
                # The upstream viewer recognizes root-relative concept links.
                return "/" + cid + ".md"
            if dest.is_file() and dest.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"}:
                out = assets / rel
                out.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(dest, out)
                return "okf-assets/" + rel.as_posix()
            return url

        sources = fm.get("sources", [])
        # marked does not implement footnotes. Render keyed citations as links;
        # the native Markdown and source records remain unchanged.
        records = {s["id"]: s for s in sources if s.get("id")}
        body = okf.map_prose(okf.body(page.read_text(encoding="utf-8")), lambda chunk:
            okf.REF.sub(lambda m: f"[{m[1]}]({records[m[1]]['resource']})" if m[1] in records else m[0], chunk))
        body = okf.map_links(body, target)
        if sources:
            body += "\n\n## Source documents\n" + "\n".join(
                f"- [{s.get('title', s.get('id', 'Source'))}]({target(s['resource'])})"
                for s in sources)
        concepts.append(g.Concept(
            id=page.relative_to(root).with_suffix("").as_posix(), type=fm["type"],
            title=fm.get("title", page.stem), description=fm.get("description", ""),
            resource=fm.get("resource", "") if urlsplit(fm.get("resource", "")).scheme in {"http", "https"} else "",
            tags=fm.get("tags", []), body=body,
            status=fm.get("status", "unspecified"), generated=fm.get("generated", {}),
            verified=g.normalize_verified(fm), stale_after=fm.get("stale_after", ""),
            sources=sources, trust_tier=g.trust_tier(fm), stale=g.is_stale(fm),
            links_to=list(dict.fromkeys(links))))
    data = g._build_graph(concepts)
    # Data is embedded in a script element, so literal '<' must be escaped.
    encoded = json.dumps(data, default=str).replace("<", "\\u003c")
    js = g._load_asset("viz.js").replace("bodyEl.innerHTML = html;", "bodyEl.innerHTML = DOMPurify.sanitize(html);")
    html = (g._load_template().replace("/*__VIZ_CSS__*/", g._load_asset("viz.css"))
            .replace("/*__VIZ_JS__*/", js)
            .replace("__BUNDLE_NAME__", json.dumps("BERIL Knowledge Wiki"))
            .replace("__BUNDLE_DATA__", encoded)
            .replace("</head>", '<script src="https://cdn.jsdelivr.net/npm/dompurify@3.4.15/dist/purify.min.js"></script>\n</head>'))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(html, encoding="utf-8")
    print(f"OKF graph: {len(concepts)} concepts, {len(data['edges'])} relationships")
    return data


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path)
    parser.add_argument("--graph", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    check(root)
    if args.graph:
        graph(root, args.graph.resolve())
