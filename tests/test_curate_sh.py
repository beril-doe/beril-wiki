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
    return root


def curate(
    workdir: Path, mode: str, stubs: str = "", env: dict[str, str] | None = None
) -> subprocess.CompletedProcess:
    """Run `curate.sh <mode>` with the stubs defined after sourcing it."""
    shim = workdir.parent / "bin"
    if shutil.which("flock") is None and not (shim / "flock").exists():
        shim.mkdir(exist_ok=True)
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
publish_step() { render_step; echo published >> "$WIKI_WORKDIR/.trace"; }
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
    assert trace(workdir) == ["ran", "ran", "rendered", "published"]


def test_run_stops_when_agentic_run_fails(workdir):
    r = curate(workdir, "run", STUBS, {"PLAN": EMPTY, "RUN_EFFECT": "exit 7"})
    assert r.returncode == 1 and "agentic run failed (exit 7)" in r.stderr
    assert trace(workdir) == []
