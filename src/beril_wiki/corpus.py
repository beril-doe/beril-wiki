"""The compiler's own copy of every source it reads: ``corpus/`` and its manifest.

``corpus/`` has the layout of a BERIL observatory checkout (``projects/<id>/``,
``ui/config/collections.yaml``, ``docs/{discoveries,pitfalls}.md``), so the
fetch stage and ``agentic run --checkout`` read it unchanged. Every run then
sees the whole corpus: author and collection pages are built from all
READMEs, so a checkout holding one project would rebuild them from that one.

``corpus/manifest.json`` records each file's SHA-256 and where each project
came from. ``verify`` fails when a file and the manifest disagree.

    uv run python -m beril_wiki.corpus import-v1 --checkout PATH
    uv run python -m beril_wiki.corpus pull-hub
    uv run python -m beril_wiki.corpus verify

``pull-hub`` is the incremental import from BERIL's context API (stages/hub.py):
it pages the submissions feed from the cursor kept in ``state/hub.json``
(``next_after``, a feed position; beside the corpus, not in its manifest, so a
moved cursor is not a corpus change to the publisher scope checks), keeps each
project's newest revision by
``submitted_at`` (the feed is in completion order, not submission order),
downloads each changed project's REPORT.md, README.md, beril.yaml and embedded
figures (sha256-checked against the feed; a listed figure the hub does not
serve stops the pull, so a later pull asks again), writes ``projects/<sid>/`` and
``docs/*.md``, and records ``owner_orcid``, ``project``, ``revision``,
``submitted_at``, ``kind`` and ``address`` beside each entry's files. Nothing is
installed and the cursor does not move unless every download verified. The
directory name is the source id (``[src: id]``), assigned once: the BERIL slug
when no other owner holds it, else ``<slug>__<orcid>``; an id vendored before
owners were known is pinned to the first owner who submits under its slug.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from beril_wiki.paths import ROOT
from beril_wiki.stages import hub

CORPUS = ROOT / "corpus"
MANIFEST = "manifest.json"
SHARED = ("ui/config/collections.yaml", "docs/discoveries.md", "docs/pitfalls.md")
META = ("README.md", "beril.yaml")
# The feed cursor: ``state/hub.json`` beside ``corpus/``; ``state/`` travels with the
# corpus through promotion, the history branch and rollback. A manifest written
# before the cursor moved there still carries it under ``hub``; it is read once and
# dropped on the next save.
CURSOR = "hub.json"
LEGACY_CURSOR_KEY = "hub"
# pull-hub's install journal: written before the first live tree is swapped, removed
# after the manifest and cursor are saved. One left behind means an install was
# interrupted, and `recover` puts the corpus back as it was before the swaps.
JOURNAL = ".pull-journal.json"
# The embed forms the synthesize skill allows; fetch, `checkout_inputs` and the publish
# ingest all read this one pattern. Group 1 is the path relative to the project.
FIG_EMBED = re.compile(
    r"!\[[^\]]*\]\(((?:figures|runs/[^)/\s]+/out|work/[^)/\s]+/runs/[^)/\s]+/out)/[^)\s]+)\)"
)


def figure_destination(project_id: str, rel: str) -> str:
    """Path under ``wiki/figures/``; v1 ``figures/`` embeds drop that prefix."""
    return f"{project_id}/{re.sub(r'^figures/', '', rel)}"


def sha256(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def digest(files: dict[str, str]) -> str:
    """One hash over a project's sorted ``path:hash`` lines."""
    lines = "".join(f"{p}:{h}\n" for p, h in sorted(files.items()))
    return "sha256:" + hashlib.sha256(lines.encode()).hexdigest()


def project_files(project: Path) -> list[str]:
    """README, REPORT, beril.yaml and every figure the report embeds, relative to the project."""
    names = [n for n in ("README.md", "REPORT.md", "beril.yaml") if (project / n).is_file()]
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


def state_dir(corpus: Path) -> Path:
    return corpus.parent / "state"


def load_cursor(state: Path) -> dict:
    path = state / CURSOR
    if not path.is_file():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def save_cursor(state: Path, cursor: dict) -> None:
    state.mkdir(parents=True, exist_ok=True)
    tmp = state / (CURSOR + ".tmp")
    tmp.write_text(json.dumps(cursor, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    tmp.replace(state / CURSOR)


def import_v1(checkout: Path, corpus: Path = CORPUS) -> dict:
    """Replace ``corpus/`` with every input a run reads from an observatory checkout."""
    commit = subprocess.run(
        ["git", "-C", str(checkout), "rev-parse", "HEAD"],
        capture_output=True,
        text=True,
        check=True,
    ).stdout.strip()
    corpus.parent.mkdir(parents=True, exist_ok=True)
    temporary = Path(tempfile.mkdtemp(prefix=f".{corpus.name}-import-", dir=corpus.parent))
    replacement, previous = temporary / "replacement", temporary / "previous"
    installed = False
    try:
        replacement.mkdir()
        manifest: dict = {"version": 1, "shared": {}, "projects": {}}
        for rel in SHARED:
            src = checkout / rel
            if not src.is_file():
                raise SystemExit(f"corpus: checkout lacks {rel}")
            dst = replacement / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
            manifest["shared"][rel] = sha256(dst)
        for project in sorted(p for p in (checkout / "projects").iterdir() if p.is_dir()):
            names = project_files(project)
            if not names:
                continue
            for name in names:
                dst = replacement / "projects" / project.name / name
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(project / name, dst)
            manifest["projects"][project.name] = entry(
                replacement / "projects" / project.name, f"v1@{commit[:12]}"
            )
        save(manifest, replacement)
        problems = verify(replacement)
        if problems:
            raise ValueError("corpus: replacement verification failed: " + "; ".join(problems))
        try:
            if corpus.exists():
                corpus.replace(previous)
            replacement.replace(corpus)
        except BaseException:
            if previous.exists():
                previous.replace(corpus)
            raise
        installed = True
    finally:
        # Keep the previous corpus recoverable if rollback itself failed.
        if installed or not previous.exists():
            shutil.rmtree(temporary)
    return manifest


SAFE_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]*$")


def assign_sid(manifest: dict, owner: str, slug: str) -> str:
    """The source id for BERIL project ``slug`` of ``owner``, assigned once (see the
    module docstring). Pins an unowned vendored entry to ``owner``; mutates ``manifest``."""
    projects = manifest["projects"]
    for sid, item in projects.items():
        if item.get("owner_orcid") == owner and item.get("project") == slug:
            return sid
    if slug not in projects:
        return slug
    if "owner_orcid" not in projects[slug]:
        projects[slug].update(owner_orcid=owner, project=slug)
        return slug
    sid = f"{slug}__{owner}"
    if sid in projects:
        raise hub.HubError(f"source id {sid!r} is already taken")
    return sid


def unchanged(current: dict, row: dict, installed: Path) -> bool:
    """Whether the feed row holds nothing the corpus has not already got: the report
    revision matches, and every file the corpus consumes (the metadata files and the
    figures the report embeds) is held with the hash the feed declares. A README or
    figure can change without the report, and both are run inputs."""
    report = installed / "REPORT.md"
    if not report.is_file():
        return False
    if current.get("revision") != row.get("revision"):
        return False
    declared = row.get("files", {})
    recorded = current.get("files", {})
    for rel, digest_ in recorded.items():
        if rel == "REPORT.md":
            continue
        # A file the corpus holds that the submission no longer carries (a removed
        # README, a figure dropped from the archive) is a change: the project tree
        # must be replaced, or the checkout keeps metadata upstream deleted.
        if rel not in declared or f"sha256:{declared[rel]}" != digest_:
            return False
    # A declared file the corpus consumes but does not hold (a figure an earlier
    # pull could not fetch) is missing, not unchanged.
    wanted = set(META) | set(
        FIG_EMBED.findall(report.read_text(encoding="utf-8", errors="replace"))
    )
    return all(rel in recorded for rel in wanted if rel in declared)


def warn(message: str) -> None:
    print(f"corpus: [WARN] {message}", file=sys.stderr)


def download_project(client: hub.Hub, row: dict, dest: Path) -> None:
    """REPORT.md (required), README.md, beril.yaml and the embedded figures of one feed
    row into ``dest``. A figure the feed lists must arrive; one the feed does not
    list (the report embeds a file the submission lacks) is skipped with a warning."""
    files, address = row["files"], row["address"]
    report = client.fetch(f"{address}/REPORT.md", files.get("REPORT.md"))
    dest.mkdir(parents=True)
    (dest / "REPORT.md").write_bytes(report)
    wanted = list(META) + sorted(set(FIG_EMBED.findall(report.decode("utf-8", "replace"))))
    for rel in wanted:
        if ".." in Path(rel).parts or rel.startswith("/"):
            raise hub.HubError(f"{address}: unsafe figure reference {rel!r}")
        if rel in META and rel not in files:
            continue
        try:
            data = client.fetch(f"{address}/{hub.safe_path(rel)}", files.get(rel))
        except hub.HubError as exc:
            if rel in META or rel in files:
                raise
            warn(f"{address}/{rel}: skipped ({exc})")
            continue
        (dest / rel).parent.mkdir(parents=True, exist_ok=True)
        (dest / rel).write_bytes(data)


def pull_hub(
    corpus: Path = CORPUS,
    client: hub.Hub | None = None,
    after: int | None = None,
    state: Path | None = None,
) -> dict:
    """Bring ``corpus/`` up to the hub feed's head; returns ``{projects, docs, next_after}``.

    A cursor from before the feed paged by ``after`` (it kept ``next_since``)
    starts from the beginning once; unchanged revisions are skipped, so that
    re-lists the feed without re-downloading it."""
    own = client is None
    client = client or hub.Hub()
    state = state or state_dir(corpus)
    recover(corpus)
    manifest = load(corpus)
    hub_state = load_cursor(state) or manifest.pop(LEGACY_CURSOR_KEY, {})
    # A `next_since` cursor (a server from before the `after` paging) is not kept:
    # that feed is re-listed from the beginning, and unchanged rows are skipped.
    cursor = after if after is not None else hub_state.get("next_after")
    temporary = Path(tempfile.mkdtemp(prefix=f".{corpus.name}-pull-", dir=corpus.parent))
    installs: list[tuple[Path, Path]] = []
    counts = {"projects": 0, "docs": 0}
    try:
        rows, following = client.submissions(cursor)
        docs_state = hub_state.get("docs", {})
        for (owner, slug), row in hub.latest(rows).items():
            if row.get("kind") == "docs":
                if hub.submitted(docs_state) > hub.submitted(row):
                    # An older digests submission that completed after a newer one
                    # was pulled: its feed hashes no longer match what read serves.
                    continue
                docs_state = {"id": row.get("id"), "submitted_at": row.get("submitted_at")}
                for rel, expected in sorted(row["files"].items()):
                    if f"docs/{rel}" not in SHARED:
                        warn(f"{row['address']}/{rel}: not a corpus digest, skipped")
                        continue
                    staged = temporary / "docs" / rel
                    staged.parent.mkdir(parents=True, exist_ok=True)
                    staged.write_bytes(client.fetch(f"{row['address']}/{rel}", expected))
                    manifest["shared"][f"docs/{rel}"] = sha256(staged)
                    installs.append((staged, corpus / "docs" / rel))
                    counts["docs"] += 1
                continue
            sid = assign_sid(manifest, owner, slug)
            current = manifest["projects"].get(sid, {})
            if hub.submitted(current) > hub.submitted(row):
                # An older revision that completed after a newer one was
                # pulled: the corpus already has the newer one.
                continue
            if unchanged(current, row, corpus / "projects" / sid):
                # Same bytes, newer submission: keep the newer metadata so a still
                # older completion arriving later is rejected, not fetched and
                # failed against the bytes read now serves.
                current.update(
                    origin=f"hub@{row.get('id')}",
                    submitted_at=row.get("submitted_at"),
                    kind=row.get("kind"),
                    address=row.get("address"),
                )
                continue
            staged = temporary / "projects" / sid
            download_project(client, row, staged)
            manifest["projects"][sid] = entry(staged, f"hub@{row.get('id')}") | {
                key: row.get(key)
                for key in ("owner_orcid", "project", "revision", "submitted_at", "kind", "address")
            }
            installs.append((staged, corpus / "projects" / sid))
            counts["projects"] += 1
        hub_state = {
            "url": client.url,
            "next_after": following if isinstance(following, int) else None,
        }
        if docs_state:
            hub_state["docs"] = docs_state
        corpus.mkdir(parents=True, exist_ok=True)
        manifest.pop(LEGACY_CURSOR_KEY, None)
        # Every download verified: swap the trees in by rename, each live one going
        # aside first, under a journal that survives a crash between two swaps.
        journaled = _journal(corpus, state, temporary, [dest for _, dest in installs])
        try:
            for staged, dest in installs:
                dest.parent.mkdir(parents=True, exist_ok=True)
                if dest.exists():
                    kept = temporary / "aside" / dest.relative_to(corpus)
                    kept.parent.mkdir(parents=True, exist_ok=True)
                    os.rename(dest, kept)
                os.rename(staged, dest)
            save(manifest, corpus)
            save_cursor(state, hub_state)
            journaled.unlink()
        except BaseException:
            # Put the corpus back now; a recovery that itself fails leaves the
            # journal and the asides for the next pull (or verify) to retry.
            try:
                recover(corpus)
            except Exception as exc:
                warn(f"interrupted install not recovered ({exc}); kept {journaled}")
            raise
    finally:
        if not (corpus / JOURNAL).exists():
            shutil.rmtree(temporary, ignore_errors=True)
        if own:
            client.close()
    return counts | {"next_after": hub_state["next_after"]}


def _journal(corpus: Path, state: Path, temporary: Path, dests: list[Path]) -> Path:
    """Write the install journal and set the manifest and cursor aside, so `recover`
    can undo the swaps that follow. Paths are relative to the corpus's parent, so a
    volume mounted elsewhere next time still reads it."""
    aside = temporary / "aside"
    aside.mkdir()

    def rel(path: Path) -> str:
        return os.path.relpath(path, corpus.parent)

    record = {
        "staging": rel(temporary),
        "state": rel(state),
        "moves": [
            {"dest": dest.relative_to(corpus).as_posix(), "replace": dest.exists()}
            for dest in dests
        ],
        "manifest": (corpus / MANIFEST).is_file(),
        "cursor": (state / CURSOR).is_file(),
    }
    if record["manifest"]:
        shutil.copy2(corpus / MANIFEST, aside / MANIFEST)
    if record["cursor"]:
        shutil.copy2(state / CURSOR, aside / CURSOR)
    path = corpus / JOURNAL
    tmp = corpus / (JOURNAL + ".tmp")
    tmp.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    tmp.replace(path)
    return path


def recover(corpus: Path = CORPUS) -> bool:
    """Undo an interrupted ``pull-hub`` install left behind by its journal: every tree
    set aside goes back where it was, a half-installed new tree is dropped, and the
    manifest and cursor are restored, so the corpus is exactly as before the pull
    and the next one downloads again. Returns whether there was anything to do."""
    journal = corpus / JOURNAL
    if not journal.is_file():
        return False
    record = json.loads(journal.read_text(encoding="utf-8"))
    staging = (corpus.parent / record["staging"]).resolve()
    state = (corpus.parent / record["state"]).resolve()
    aside = staging / "aside"
    if not aside.is_dir():
        raise hub.HubError(
            f"{journal} records an interrupted install but its staging directory "
            f"{staging} is gone; restore corpus/ from the history branch"
        )
    for move in record["moves"]:
        dest, kept = corpus / move["dest"], aside / move["dest"]
        if move["replace"] and not kept.exists():
            continue  # never moved aside: still the live tree
        if dest.is_dir() and not dest.is_symlink():
            shutil.rmtree(dest)
        elif dest.exists():
            dest.unlink()
        if move["replace"]:
            os.rename(kept, dest)
    for flag, path, backup in (
        ("manifest", corpus / MANIFEST, aside / MANIFEST),
        ("cursor", state / CURSOR, aside / CURSOR),
    ):
        if record[flag]:
            path.parent.mkdir(parents=True, exist_ok=True)
            os.replace(backup, path)
        elif path.exists():
            path.unlink()
    journal.unlink()
    shutil.rmtree(staging, ignore_errors=True)
    warn("an interrupted pull-hub install was undone; pull again")
    return True


def verify(corpus: Path = CORPUS) -> list[str]:
    """Every corpus file is in the manifest with its current hash, and nothing is missing.
    An interrupted install is undone first, so what is checked is a whole corpus."""
    recover(corpus)
    # load() reads a missing manifest as empty, which an empty tree would then match.
    if not (corpus / MANIFEST).is_file():
        return [f"{MANIFEST}: missing; run import-v1"]
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
    pull = sub.add_parser("pull-hub", help="update corpus/ from BERIL's submissions feed")
    pull.add_argument(
        "--after",
        type=int,
        help="feed position to start after (default: state/hub.json's; 0 = the beginning)",
    )
    sub.add_parser("verify", help="check corpus/ against its manifest")
    args = parser.parse_args(argv)
    if args.cmd == "import-v1":
        manifest = import_v1(args.checkout.resolve())
        print(f"corpus: {len(manifest['projects'])} projects from {args.checkout}")
        return 0
    if args.cmd == "pull-hub":
        try:
            done = pull_hub(CORPUS, after=args.after)
        except hub.HubError as exc:
            raise SystemExit(f"corpus: {exc}") from exc
        print(
            f"corpus: {done['projects']} project(s) and {done['docs']} digest(s) updated; "
            f"feed cursor {done['next_after']}"
        )
        return 0
    problems = verify()
    for line in problems:
        print(f"corpus: {line}", file=sys.stderr)
    print(f"corpus: {'OK' if not problems else f'{len(problems)} problem(s)'}")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
