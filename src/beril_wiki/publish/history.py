"""The `history` branch: the audit trail of every published artifact, and the rollback
source.

After a successful `artifact push`, `record` commits `wiki/`, `state/`, `corpus/`
and `search/section-vectors.jsonl` from the working checkout
to the branch `history` (created orphan when absent) and tags the commit
`artifact/<id>`. The working checkout's own branch, index and working tree are
untouched: the commit is built through a temporary git index.

`restore` is the other half of a rollback: it checks `wiki/`, `state/`,
`corpus/` and `search/` out of `artifact/<id>` into the working checkout, so
the next curate run starts from exactly that promotion: the corpus and
`state/hub.json` (the hub feed cursor) match the wiki, so `corpus pull-hub`
re-downloads whatever the feed has moved past it and `changed_sources`
re-integrates it against the restored `wiki/sources`. It refuses while a
curator run holds `.agentic/lock`.

`search_data pull` reads the vectors from this branch, which replaces the
retired single-commit `search-data` branch.
"""

from __future__ import annotations

import contextlib
import fcntl
import io
import os
import pathlib
import shutil
import subprocess
import tarfile
import tempfile
from collections.abc import Iterator

BRANCH = "history"
TAG_PREFIX = "artifact/"
TRACKED = ("wiki", "state", "corpus", "search/section-vectors.jsonl")
RESTORED_TREES = ("wiki", "state", "corpus", "search")


class HistoryError(RuntimeError):
    pass


def git(root: pathlib.Path, *args: str, env: dict[str, str] | None = None) -> str:
    r = subprocess.run(
        ["git", "-C", str(root), *args],
        capture_output=True,
        text=True,
        env={**os.environ, **(env or {})},
    )
    if r.returncode:
        raise HistoryError(f"git {' '.join(args)}: {r.stderr.strip()}")
    return r.stdout


def ref(root: pathlib.Path, name: str) -> str | None:
    r = subprocess.run(
        ["git", "-C", str(root), "rev-parse", "--verify", "--quiet", name],
        capture_output=True,
        text=True,
    )
    return r.stdout.strip() or None


def tag_of(artifact_id: str) -> str:
    return f"{TAG_PREFIX}{artifact_id}"


def branch_head(root: pathlib.Path, remote: str = "origin") -> str | None:
    """The commit a new record chains onto: the local `history`, else the remote's
    (a fresh clone has only `origin/history`; an unrelated root there would make the
    later `git push origin history` a rejected non-fast-forward)."""
    return ref(root, f"refs/heads/{BRANCH}") or ref(root, f"refs/remotes/{remote}/{BRANCH}")


def record(root: pathlib.Path, artifact_id: str, message: str | None = None) -> str:
    """Commit the tracked trees to `history` and tag `artifact/<id>`; returns the commit."""
    tag = tag_of(artifact_id)
    if ref(root, f"refs/tags/{tag}"):
        raise HistoryError(f"tag {tag} already exists")
    present = [p for p in TRACKED if (root / p).exists()]
    if not present:
        raise HistoryError("nothing to record: none of the tracked paths exist")
    with tempfile.NamedTemporaryFile(prefix="history-index.", delete=False) as handle:
        index = handle.name
    try:
        os.unlink(index)
        env = {"GIT_INDEX_FILE": index}
        # -f: the vectors store is gitignored in the working checkout.
        git(root, "add", "-f", "--", *present, env=env)
        tree = git(root, "write-tree", env=env).strip()
        local = ref(root, f"refs/heads/{BRANCH}")
        parent = local or branch_head(root)
        args = ["commit-tree", tree, "-m", message or f"Artifact {artifact_id}"]
        if parent:
            args += ["-p", parent]
        commit = git(root, *args).strip()
        git(root, "update-ref", f"refs/heads/{BRANCH}", commit, local or "")
        git(root, "tag", tag, commit)
        return commit
    finally:
        if os.path.exists(index):
            os.unlink(index)


@contextlib.contextmanager
def held_lock(root: pathlib.Path) -> Iterator[None]:
    """Hold the curator's exclusive lock (the same flock `agentic run` takes on
    `.agentic/lock`) for the duration of the block, so a scheduled run cannot start
    while the trees are being replaced. Raises HistoryError when a run holds it."""
    lock = root / ".agentic" / "lock"
    lock.parent.mkdir(exist_ok=True)
    with lock.open("a") as handle:
        try:
            fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise HistoryError(
                "a curator run holds .agentic/lock; retry when it has finished"
            ) from None
        try:
            yield
        finally:
            fcntl.flock(handle, fcntl.LOCK_UN)


def locked_by_a_run(root: pathlib.Path) -> bool:
    lock = root / ".agentic" / "lock"
    if not lock.exists():
        return False
    with lock.open("a") as handle:
        try:
            fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            return True
        fcntl.flock(handle, fcntl.LOCK_UN)
    return False


def restore(root: pathlib.Path, artifact_id: str, *, locked: bool = False) -> str:
    """Replace wiki/, state/, corpus/ and search/ with the tagged promotion, holding
    the curator lock throughout unless the caller already holds it (`locked`)."""
    if locked:
        return stage_restore(root, artifact_id).keep()
    with held_lock(root):
        return stage_restore(root, artifact_id).keep()


class Restore:
    """A restore whose previous trees are kept aside until the caller settles it:
    `keep()` discards them once whatever the restore was for (the live pointer) has
    moved too; `undo()` puts them back, so the checkout and the pointer stay at the
    same promotion when the pointer could not move."""

    def __init__(self, root: pathlib.Path, commit: str, tag: str, staging: pathlib.Path) -> None:
        self.root, self.commit, self.tag, self.staging = root, commit, tag, staging

    def keep(self) -> str:
        shutil.rmtree(self.staging, ignore_errors=True)
        return self.commit

    def undo(self) -> None:
        aside = self.staging / ".aside"
        try:
            _put_back(self.root, aside)
        except OSError as exc:
            raise HistoryError(
                f"putting the checkout back failed ({exc}); the previous trees are kept "
                f"under {aside}"
            ) from exc
        shutil.rmtree(self.staging, ignore_errors=True)


def stage_restore(root: pathlib.Path, artifact_id: str) -> Restore:
    """Swap the tagged trees in by rename, each live tree going aside first: a
    failure part-way puts every tree back, so the checkout is never split. The
    caller holds the curator lock, and settles the result with `keep` or `undo`."""
    tag = tag_of(artifact_id)
    commit = ref(root, f"refs/tags/{tag}")
    if not commit:
        raise HistoryError(f"no tag {tag}; was this artifact recorded on {BRANCH}?")
    archive = subprocess.run(
        ["git", "-C", str(root), "archive", "--format=tar", commit],
        capture_output=True,
    )
    if archive.returncode:
        raise HistoryError(f"git archive {tag}: {archive.stderr.decode().strip()}")
    staging = pathlib.Path(tempfile.mkdtemp(prefix=".restore.", dir=root))
    pending = Restore(root, commit, tag, staging)
    try:
        with tarfile.open(fileobj=io.BytesIO(archive.stdout)) as tar:
            tar.extractall(staging, filter="data")
        (staging / ".aside").mkdir()
        for tree in RESTORED_TREES:
            target = root / tree
            if target.exists():
                os.rename(target, staging / ".aside" / tree)
            if (staging / tree).exists():
                os.rename(staging / tree, target)
    except OSError as exc:
        try:
            pending.undo()
        except HistoryError as undo:
            raise HistoryError(f"restore of {tag} failed ({exc}) and {undo}") from undo
        raise HistoryError(f"restore of {tag} failed; the checkout was put back: {exc}") from exc
    return pending


def _put_back(root: pathlib.Path, aside: pathlib.Path) -> None:
    for tree in RESTORED_TREES:
        if not (aside / tree).exists():
            continue
        target = root / tree
        if target.exists():
            shutil.rmtree(target)  # the half-placed restored tree
        os.rename(aside / tree, target)
