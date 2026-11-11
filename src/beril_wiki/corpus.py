"""The compiler's own copy of every source it reads: ``corpus/`` and its manifest.

``corpus/`` has the layout of a BERIL observatory checkout (``projects/<id>/``,
``ui/config/collections.yaml``, ``docs/{discoveries,pitfalls}.md``), so the
fetch stage and ``agentic run --checkout`` read it unchanged. Every run then
sees the whole corpus: author and collection pages are built from all
READMEs, so a checkout holding one project would rebuild them from that one.

``corpus/manifest.json`` records each file's SHA-256 and where each project
came from. ``verify`` fails when a file and the manifest disagree.

    uv run python -m beril_wiki.corpus import-v1 --checkout PATH
    uv run python -m beril_wiki.corpus verify
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

from beril_wiki.paths import ROOT

CORPUS = ROOT / "corpus"
MANIFEST = "manifest.json"
SHARED = ("ui/config/collections.yaml", "docs/discoveries.md", "docs/pitfalls.md")
# Must match the embeds `stages.fetch` copies and `agentic.runner.checkout_inputs` hashes.
FIG_EMBED = re.compile(r"!\[[^\]]*\]\((figures/[^)]+)\)")


def sha256(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def digest(files: dict[str, str]) -> str:
    """One hash over a project's sorted ``path:hash`` lines."""
    lines = "".join(f"{p}:{h}\n" for p, h in sorted(files.items()))
    return "sha256:" + hashlib.sha256(lines.encode()).hexdigest()


def project_files(project: Path) -> list[str]:
    """README, REPORT and every figure the report embeds, relative to the project."""
    names = [n for n in ("README.md", "REPORT.md") if (project / n).is_file()]
    report = project / "REPORT.md"
    if report.is_file():
        for rel in sorted(set(FIG_EMBED.findall(report.read_text(encoding="utf-8")))):
            path = Path(rel)
            if ".." in path.parts or path.is_absolute():
                raise ValueError(f"unsafe figure reference in {report}: {rel}")
            if (project / path).is_file():
                names.append(rel)
    return names


def entry(project: Path, origin: str) -> dict:
    files = {name: sha256(project / name) for name in project_files(project)}
    return {"origin": origin, "files": files, "digest": digest(files)}


def load(corpus: Path = CORPUS) -> dict:
    path = corpus / MANIFEST
    if not path.exists():
        return {"version": 1, "shared": {}, "projects": {}}
    return json.loads(path.read_text(encoding="utf-8"))


def save(manifest: dict, corpus: Path = CORPUS) -> None:
    text = json.dumps(manifest, indent=2, sort_keys=True) + "\n"
    tmp = corpus / (MANIFEST + ".tmp")
    tmp.write_text(text, encoding="utf-8")
    tmp.replace(corpus / MANIFEST)


def import_v1(checkout: Path, corpus: Path = CORPUS) -> dict:
    """Replace ``corpus/`` with every input a run reads from an observatory checkout."""
    commit = subprocess.run(
        ["git", "-C", str(checkout), "rev-parse", "HEAD"],
        capture_output=True,
        text=True,
        check=True,
    ).stdout.strip()
    if corpus.exists():
        shutil.rmtree(corpus)
    corpus.mkdir(parents=True)
    manifest: dict = {"version": 1, "shared": {}, "projects": {}}
    for rel in SHARED:
        src = checkout / rel
        if not src.is_file():
            raise SystemExit(f"corpus: checkout lacks {rel}")
        dst = corpus / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        manifest["shared"][rel] = sha256(dst)
    for project in sorted(p for p in (checkout / "projects").iterdir() if p.is_dir()):
        names = project_files(project)
        if not names:
            continue
        for name in names:
            dst = corpus / "projects" / project.name / name
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(project / name, dst)
        manifest["projects"][project.name] = entry(
            corpus / "projects" / project.name, f"v1@{commit[:12]}"
        )
    save(manifest, corpus)
    return manifest


def verify(corpus: Path = CORPUS) -> list[str]:
    """Every corpus file is in the manifest with its current hash, and nothing is missing."""
    manifest = load(corpus)
    problems: list[str] = []
    listed = {rel: h for rel, h in manifest.get("shared", {}).items()}
    for pid, project in manifest.get("projects", {}).items():
        files = project.get("files", {})
        if project.get("digest") != digest(files):
            problems.append(f"{pid}: digest does not match its file list")
        for name, h in files.items():
            listed[f"projects/{pid}/{name}"] = h
    on_disk = {
        p.relative_to(corpus).as_posix()
        for p in corpus.rglob("*")
        if p.is_file() and p.name != MANIFEST
    }
    for rel in sorted(on_disk - listed.keys()):
        problems.append(f"{rel}: not in the manifest")
    for rel, h in sorted(listed.items()):
        path = corpus / rel
        if not path.is_file():
            problems.append(f"{rel}: in the manifest but missing")
        elif sha256(path) != h:
            problems.append(f"{rel}: hash differs from the manifest")
    return problems


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="beril_wiki.corpus", description=__doc__)
    sub = parser.add_subparsers(dest="cmd", required=True)
    imp = sub.add_parser("import-v1", help="replace corpus/ from an observatory checkout")
    imp.add_argument("--checkout", type=Path, required=True)
    sub.add_parser("verify", help="check corpus/ against its manifest")
    args = parser.parse_args(argv)
    if args.cmd == "import-v1":
        manifest = import_v1(args.checkout.resolve())
        print(f"corpus: {len(manifest['projects'])} projects from {args.checkout}")
        return 0
    problems = verify()
    for line in problems:
        print(f"corpus: {line}", file=sys.stderr)
    print(f"corpus: {'OK' if not problems else f'{len(problems)} problem(s)'}")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
