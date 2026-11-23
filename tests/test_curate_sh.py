"""deploy/curate.sh's logic, with its heavy steps stubbed: the script is sourced
(nothing runs on source) and bash functions defined afterwards replace refresh_code,
the python calls and the render, so each mode's decisions can be checked against a
throwaway clone without a model, a hub or Quartz."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parents[1] / "deploy/curate.sh"

FLOCK_SHIM = """#!/usr/bin/env python3
# flock(1) for macOS: lock the inherited descriptor, as util-linux's does.
import fcntl, sys, time
args = sys.argv[1:]
wait = float(args[args.index("-w") + 1]) if "-w" in args else None
fd = int(args[-1])
deadline = time.monotonic() + (wait or 0)
while True:
    try:
        fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        sys.exit(0)
    except BlockingIOError:
        if "-n" in args or (wait is not None and time.monotonic() >= deadline):
            sys.exit(1)
        time.sleep(0.05)
"""


def git(cwd: Path, *args: str) -> str:
    return subprocess.run(
        ["git", "-c", "user.name=t", "-c", "user.email=t@t", *args],
        cwd=cwd,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


@pytest.fixture
def workdir(tmp_path):
    """A clone-shaped directory: a git repository holding an accepted state."""
    root = tmp_path / "work/beril-wiki"
    (root / "state").mkdir(parents=True)
    (root / "state/agentic.json").write_text(json.dumps({"fingerprint": "f0"}))
    git(root, "init", "-q", "-b", "main")
    git(root, "add", ".")
    git(root, "commit", "-q", "-m", "state")
    # publish_step's push to the store: a trace line instead, the git config it
    # inherited, and a failure while `.publish-fails` exists.
    (root / "scripts").mkdir()
    (root / "scripts/publish_artifact.sh").write_text(
        "#!/bin/sh\n"
        'echo "published $*" >> "$WIKI_WORKDIR/.trace"\n'
        'echo "${BERIL_WIKI_GIT_COMMIT:-unset}" > "$WIKI_WORKDIR/.published-commit"\n'
        'env | grep "^GIT_CONFIG" > "$WIKI_WORKDIR/.published-git-env"\n'
        '[ ! -f "$WIKI_WORKDIR/.publish-fails" ] || exit 9\n'
    )
    (root / "scripts/publish_artifact.sh").chmod(0o755)
    return root


def curate(
    workdir: Path, mode: str, stubs: str = "", env: dict[str, str] | None = None
) -> subprocess.CompletedProcess:
    """Run `curate.sh <mode>` with the stubs defined after sourcing it."""
    shim = workdir.parent / "bin"
    if shutil.which("flock") is None and not (shim / "flock").exists():
        shim.mkdir(parents=True, exist_ok=True)
        (shim / "flock").write_text(FLOCK_SHIM)
        (shim / "flock").chmod(0o755)
    harness = f'source "{SCRIPT}" {mode}\n{stubs}\nmain\n'
    run_env = {
        "PATH": f"{shim}:{os.environ['PATH']}",
        "HOME": os.environ.get("HOME", "/"),
        "WIKI_WORKDIR": str(workdir),
        "WIKI_BASE_URL": "example.test/wiki",
        "WIKI_CURATE_MAX_TOKENS": "1",
        "WIKI_CURATE_MAX_JOBS": "1",
        **(env or {}),
    }
    return subprocess.run(
        ["bash", "-c", harness], env=run_env, capture_output=True, text=True, check=False
    )


# Stubs shared by the modes: no network, no model, no Quartz. `agentic plan` prints
# $PLAN; `agentic run` runs $RUN_EFFECT; the render and the publish leave a trace.
STUBS = """
refresh_code() { log "code: stubbed"; }
seed_build_caches() { :; }
check_caps() { :; }
py() {
  case "$*" in
    "-m beril_wiki.corpus pull-hub") ;;
    "-m beril_wiki.stages.fetch") ;;
    "-m beril_wiki.agentic --root "*" plan") printf '%s\\n' "$PLAN" ;;
    "-m beril_wiki.agentic --root "*" run "*) (eval "${RUN_EFFECT:-:}") ;;
    "-m beril_wiki.agentic --root "*" status") echo status ;;
    *) command uv run --project "$WIKI_WORKDIR" python "$@" ;;
  esac
}
render_step() { echo rendered >> "$WIKI_WORKDIR/.trace"; }
git() {
  case "$*" in *" push "*) echo pushed >> "$WIKI_WORKDIR/.trace" ;; *) command git "$@" ;; esac
}
artifact_in_store() { [ -f "$WIKI_WORKDIR/.in-store-$1" ]; }
tag_on_origin() { [ -f "$WIKI_WORKDIR/.on-origin-$1" ]; }
"""

EMPTY = json.dumps(
    {
        "changed_sources": [],
        "pending_editorial": [],
        "retry_pages": [],
        "accepted_current": True,
    }
)


def trace(workdir: Path) -> list[str]:
    path = workdir / ".trace"
    return path.read_text().split() if path.exists() else []


@pytest.mark.parametrize(
    ("plan", "code"),
    [
        (EMPTY, 0),
        (json.loads(EMPTY) | {"accepted_current": None}, 0),
        (json.loads(EMPTY) | {"accepted_current": False}, 3),
        (json.loads(EMPTY) | {"retry_pages": ["summaries/a.md"]}, 3),
        (json.loads(EMPTY) | {"changed_sources": ["a__REPORT.md"]}, 3),
    ],
)
def test_plan_exits_3_on_runs_own_test_and_logs_every_count(workdir, plan, code):
    plan = plan if isinstance(plan, str) else json.dumps(plan)
    r = curate(workdir, "plan", STUBS, {"PLAN": plan})
    assert r.returncode == code, r.stderr
    line = next(ln for ln in r.stderr.splitlines() if "] plan: " in ln)
    for key in ("changed_sources=", "pending_editorial=", "retry_pages=", "accepted_current="):
        assert key in line, line


def test_run_calls_agentic_run_regardless_of_the_plan_and_publishes_on_promotion(workdir):
    # The plan is empty, yet the run is made: a README or errata change, a code or
    # model change and a queued retry are run's to find. Unchanged state: no publish.
    r = curate(
        workdir, "run", STUBS, {"PLAN": EMPTY, "RUN_EFFECT": "echo ran >> $WIKI_WORKDIR/.trace"}
    )
    assert r.returncode == 0, r.stderr
    assert trace(workdir) == ["ran"]
    assert "accepted state unchanged by the run; nothing to publish" in r.stderr
    # Promotion rewrites state/agentic.json: render and publish follow.
    promote = (
        "echo ran >> $WIKI_WORKDIR/.trace; "
        'echo \'{"fingerprint": "f1"}\' > $WIKI_WORKDIR/state/agentic.json'
    )
    r = curate(workdir, "run", STUBS, {"PLAN": EMPTY, "RUN_EFFECT": promote})
    assert r.returncode == 0, r.stderr
    assert trace(workdir)[:5] == ["ran", "ran", "rendered", "published", "--id"]


def test_run_stops_when_agentic_run_fails(workdir):
    r = curate(workdir, "run", STUBS, {"PLAN": EMPTY, "RUN_EFFECT": "exit 7"})
    assert r.returncode == 1 and "agentic run failed (exit 7)" in r.stderr
    assert trace(workdir) == []


def hold_lock(workdir: Path):
    """Hold the curator's lock as a running job would, until the handle is closed."""
    import fcntl

    handle = (workdir.parent / ".curate.lock").open("a")
    fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
    return handle


def test_plan_skips_and_run_waits_while_another_job_holds_the_lock(workdir):
    # The hourly plan at :17 would otherwise refresh code, pull the hub and stage
    # while the nightly run curates, and the run would refuse promotion.
    held = hold_lock(workdir)
    try:
        r = curate(workdir, "plan", STUBS, {"PLAN": EMPTY})
        assert r.returncode == 0 and "skipping this plan" in r.stderr, r.stderr
        assert "] plan: " not in r.stderr  # nothing was pulled or staged
        r = curate(workdir, "run", STUBS, {"PLAN": EMPTY, "WIKI_LOCK_WAIT": "1"})
        assert r.returncode == 75 and "still holds" in r.stderr, r.stderr
        assert trace(workdir) == []
    finally:
        held.close()
    r = curate(workdir, "plan", STUBS, {"PLAN": EMPTY})
    assert r.returncode == 0 and "] plan: " in r.stderr, r.stderr


def test_a_failed_publish_is_owed_until_a_later_run_or_publish_finishes_it(workdir):
    promote = (
        "echo ran >> $WIKI_WORKDIR/.trace; "
        'echo \'{"fingerprint": "f1"}\' > $WIKI_WORKDIR/state/agentic.json'
    )
    failing = STUBS + '\npublish_step() { render_step; die "publish: reload failed"; }\n'
    r = curate(workdir, "run", failing, {"PLAN": EMPTY, "RUN_EFFECT": promote})
    assert r.returncode == 1 and "reload failed" in r.stderr
    pending = workdir / ".curate/publish-pending.json"
    assert "promoted_at" in pending.read_text()
    # The hourly plan says so and asks for a run; the next run, with nothing
    # to curate, publishes the promoted wiki and clears the marker.
    r = curate(workdir, "plan", STUBS, {"PLAN": EMPTY})
    assert r.returncode == 3 and "publish_pending=yes" in r.stderr, r.stderr
    r = curate(
        workdir, "run", STUBS, {"PLAN": EMPTY, "RUN_EFFECT": "echo ran >> $WIKI_WORKDIR/.trace"}
    )
    assert r.returncode == 0, r.stderr
    # The owed publish goes first, before the run: accepted work never waits on
    # a later curation.
    seen = trace(workdir)
    assert seen.index("rendered", 1) < seen.index("ran", 1) and "published" in seen
    assert not pending.exists()
    assert "publish_pending=no" in curate(workdir, "plan", STUBS, {"PLAN": EMPTY}).stderr
    # `publish` by hand finishes it as well.
    pending.parent.mkdir(exist_ok=True)
    pending.write_text('{"promoted_at": "2026-11-23T07:31:00Z"}')
    r = curate(workdir, "publish", STUBS)
    assert r.returncode == 0 and not pending.exists()


@pytest.fixture
def origin(tmp_path):
    """A bare origin with main (code and the trees as last merged) and, when asked,
    a history branch whose newest artifact/<id> tag holds the accepted wiki."""
    src = tmp_path / "src"
    (src / "state").mkdir(parents=True)
    (src / "wiki").mkdir()
    (src / "deploy").mkdir()
    (src / "state/agentic.json").write_text('{"fingerprint": "main"}')
    (src / "wiki/from-main.md").write_text("main\n")
    (src / "deploy/curate.sh").write_text("# code\n")
    git(src, "init", "-q", "-b", "main")
    git(src, "add", ".")
    git(src, "commit", "-q", "-m", "main")
    bare = tmp_path / "origin.git"
    git(tmp_path, "clone", "-q", "--bare", str(src), str(bare))
    return bare


def with_history(origin: Path, tmp_path: Path) -> None:
    work = tmp_path / "publisher"
    git(tmp_path, "clone", "-q", str(origin), str(work))
    git(work, "checkout", "-q", "--orphan", "history")
    for n in ("1", "2"):
        for page in (work / "wiki").iterdir():  # each artifact's wiki is its own tree
            page.unlink()
        (work / "state/agentic.json").write_text(f'{{"fingerprint": "artifact-{n}"}}')
        (work / "wiki" / f"accepted-{n}.md").write_text(n)
        (work / "search").mkdir(exist_ok=True)
        (work / "search/section-vectors.jsonl").write_text(f'{{"n": {n}}}\n')
        git(work, "add", "-A", "-f", ".")
        git(work, "commit", "-q", "-m", f"Artifact {n}")
        git(work, "tag", f"artifact/2026112{n}T000000Z")
    git(work, "push", "-q", "origin", "history", "--tags")


COLD = {"BERIL_WIKI_ALLOW_COLD_START": "1", "PLAN": EMPTY}


def test_cold_start_bootstraps_the_trees_from_the_newest_artifact_tag(tmp_path, origin):
    with_history(origin, tmp_path)
    workdir = tmp_path / "work/beril-wiki"
    stubs = STUBS.replace('refresh_code() { log "code: stubbed"; }\n', "")
    r = curate(workdir, "plan", stubs, COLD | {"WIKI_GIT_URL": str(origin)})
    assert r.returncode == 0, r.stderr
    assert "bootstrap: wiki from artifact/20261122T000000Z" in r.stderr, r.stderr
    assert "bootstrap: search/section-vectors.jsonl from artifact/20261122T000000Z" in r.stderr
    assert json.loads((workdir / "state/agentic.json").read_text()) == {"fingerprint": "artifact-2"}
    assert sorted(p.name for p in (workdir / "wiki").iterdir()) == ["accepted-2.md"]
    assert (workdir / "search/section-vectors.jsonl").read_text() == '{"n": 2}\n'
    assert (workdir / "deploy/curate.sh").read_text() == "# code\n"
    # The commit whose code ran is recorded, though HEAD never moves.
    main = git(origin, "rev-parse", "main")
    assert (workdir / ".curate/code-commit").read_text().strip() == main
    assert f"code: {main[:12]} of main" in r.stderr


def test_cold_start_without_a_history_branch_starts_from_main(tmp_path, origin):
    workdir = tmp_path / "work/beril-wiki"
    stubs = STUBS.replace('refresh_code() { log "code: stubbed"; }\n', "")
    r = curate(workdir, "plan", stubs, COLD | {"WIKI_GIT_URL": str(origin)})
    assert r.returncode == 0, r.stderr
    assert "origin has no history branch; the trees on main are the start" in r.stderr
    assert json.loads((workdir / "state/agentic.json").read_text()) == {"fingerprint": "main"}
    # Without the override a missing clone is refused, not created.
    r = curate(tmp_path / "other", "plan", stubs, {"PLAN": EMPTY, "WIKI_GIT_URL": str(origin)})
    assert r.returncode == 2 and "no git clone" in r.stderr


def test_the_publish_names_the_commit_whose_code_ran(workdir):
    (workdir / ".curate").mkdir()
    (workdir / ".curate/code-commit").write_text("a" * 40 + "\n")
    stubs = STUBS.replace('refresh_code() { log "code: stubbed"; }\n', "")
    r = curate(workdir, "publish", stubs, {"WIKI_SKIP_CODE_REFRESH": "1"})
    assert r.returncode == 0, r.stderr
    assert (workdir / ".published-commit").read_text().strip() == "a" * 40
    assert f"code: {'a' * 12} of the clone as it is" in r.stderr
    # Without a record the clone's own HEAD is named.
    (workdir / ".curate/code-commit").unlink()
    r = curate(workdir, "publish", stubs, {"WIKI_SKIP_CODE_REFRESH": "1"})
    assert (workdir / ".published-commit").read_text().strip() == git(workdir, "rev-parse", "HEAD")


def test_an_owed_publish_is_finished_even_when_the_next_curation_fails(workdir):
    pending = workdir / ".curate/publish-pending.json"
    pending.parent.mkdir(exist_ok=True)
    pending.write_text('{"promoted_at": "2026-11-23T07:31:00Z"}')
    r = curate(workdir, "run", STUBS, {"PLAN": EMPTY, "RUN_EFFECT": "exit 7"})
    assert r.returncode == 1 and "agentic run failed (exit 7)" in r.stderr
    assert trace(workdir)[:3] == ["rendered", "published", "--id"]
    assert not pending.exists()


def test_a_failed_bootstrap_leaves_no_clone_so_the_next_job_retries(tmp_path, origin):
    with_history(origin, tmp_path)
    workdir = tmp_path / "work/beril-wiki"
    stubs = STUBS.replace('refresh_code() { log "code: stubbed"; }\n', "")
    broken = stubs + "\nbootstrap_data_trees() { log 'bootstrap: simulated failure'; return 1; }\n"
    r = curate(workdir, "plan", broken, COLD | {"WIKI_GIT_URL": str(origin)})
    assert r.returncode == 1 and "bootstrap failed; nothing left" in r.stderr, r.stderr
    assert not workdir.exists() and not list(workdir.parent.glob("beril-wiki.bootstrap.*"))
    # The next job starts over and succeeds, with the trees from the newest tag.
    r = curate(workdir, "plan", stubs, COLD | {"WIKI_GIT_URL": str(origin)})
    assert r.returncode == 0, r.stderr
    assert "bootstrap: clone ready" in r.stderr
    assert json.loads((workdir / "state/agentic.json").read_text()) == {"fingerprint": "artifact-2"}


PROMOTE = (
    "echo ran >> $WIKI_WORKDIR/.trace; "
    'echo \'{"fingerprint": "f1"}\' > $WIKI_WORKDIR/state/agentic.json'
)


def test_a_retried_publish_keeps_the_id_chosen_at_promotion(workdir):
    # The id is fixed when `agentic run` promotes and written to the marker, so a
    # publish that failed is retried under the same id (one artifact per
    # promotion), never rebuilt as a second artifact of the same trees.
    (workdir / ".publish-fails").touch()
    r = curate(workdir, "run", STUBS, {"PLAN": EMPTY, "RUN_EFFECT": PROMOTE})
    assert r.returncode == 9, r.stderr
    pending = workdir / ".curate/publish-pending.json"
    marker = json.loads(pending.read_text())
    assert set(marker) == {"promoted_at", "artifact_id"} and marker["artifact_id"].endswith("Z")
    assert trace(workdir)[-4:] == ["published", "--id", marker["artifact_id"], "--no-check"]
    (workdir / ".publish-fails").unlink()
    r = curate(
        workdir, "run", STUBS, {"PLAN": EMPTY, "RUN_EFFECT": "echo ran >> $WIKI_WORKDIR/.trace"}
    )
    assert r.returncode == 0, r.stderr
    seen = trace(workdir)
    assert seen[-6:] == [
        "rendered",
        "published",
        "--id",
        marker["artifact_id"],
        "--no-check",
        "ran",
    ]
    assert not pending.exists()
    assert "(history to origin, then current, then reload)" in r.stderr


def owed(workdir: Path, artifact_id: str) -> Path:
    pending = workdir / ".curate/publish-pending.json"
    pending.parent.mkdir(exist_ok=True)
    pending.write_text(f'{{"promoted_at": "2026-11-23T07:31:00Z", "artifact_id": "{artifact_id}"}}')
    return pending


def test_a_retried_publish_finishes_the_transaction_where_it_stopped(workdir):
    # In the store and on origin (current or the reload failed): pointed at and
    # reloaded, not rendered or pushed again.
    pending = owed(workdir, "20261123T073000Z")
    (workdir / ".in-store-20261123T073000Z").touch()
    (workdir / ".on-origin-20261123T073000Z").touch()
    r = curate(workdir, "publish", STUBS)
    assert r.returncode == 0, r.stderr
    assert trace(workdir) == ["published", "--point", "20261123T073000Z"]
    assert "in the store and on origin; pointing current at it" in r.stderr
    assert not pending.exists()
    # Recorded locally but the push to origin failed: the push is repeated first.
    (workdir / ".trace").unlink()
    owed(workdir, "20261123T073000Z")
    (workdir / ".on-origin-20261123T073000Z").unlink()
    git(workdir, "tag", "artifact/20261123T073000Z")
    pushing = STUBS + (
        '\ngit() { case "$*" in *" push "*) echo pushed >> "$WIKI_WORKDIR/.trace";'
        ' touch "$WIKI_WORKDIR/.on-origin-20261123T073000Z" ;; *) command git "$@" ;; esac; }\n'
    )
    r = curate(workdir, "publish", pushing)
    assert r.returncode == 0, r.stderr
    assert trace(workdir) == ["pushed", "published", "--point", "20261123T073000Z"]
    assert "recorded but not on origin; pushing history and its tag" in r.stderr
    # Uploaded but never recorded: a stray; the trees go out under a fresh id.
    (workdir / ".trace").unlink()
    owed(workdir, "20261123T073000Z")
    (workdir / ".on-origin-20261123T073000Z").unlink()
    git(workdir, "tag", "-d", "artifact/20261123T073000Z")
    r = curate(workdir, "publish", STUBS)
    assert r.returncode == 0, r.stderr
    seen = trace(workdir)
    assert seen[:3] == ["rendered", "published", "--id"] and seen[3] != "20261123T073000Z"
    assert f"was never recorded; publishing as {seen[3]}" in r.stderr


def test_the_publish_inherits_the_git_credential_helper(workdir):
    # `artifact push` pushes history and the tag to origin itself, from python:
    # the helper must reach it through git's environment-held config, and the
    # token must stay out of every config value.
    r = curate(workdir, "publish", STUBS, {"WIKI_GIT_TOKEN": "ghp_secret"})
    assert r.returncode == 0, r.stderr
    seen = (workdir / ".published-git-env").read_text()
    assert "credential.helper" in seen and "WIKI_GIT_TOKEN" in seen
    assert "ghp_secret" not in seen
    r = curate(workdir, "publish", STUBS)
    assert "credential.helper" not in (workdir / ".published-git-env").read_text()
