"""Curator scheduling and recoverable promotion of isolated output."""

from __future__ import annotations

import ast
import fcntl
import json
import os
import re
import shutil
import signal
import subprocess
import sys
import time
from contextlib import contextmanager
from importlib.metadata import version
from pathlib import Path

from beril_wiki.agentic.batch import changed_sources
from beril_wiki.agentic.curator import EDITORIAL, curate, stage_revision, stage_snapshot
from beril_wiki.agentic.runtime import (
    AUTH_ENV,
    CORE_MODEL_ROLES,
    Runtime,
    WorkflowError,
    atomic_json,
    digest,
    file_hash,
    fsync_dir,
    manifest,
    model_policy,
    model_signature,
)

TREES = ("wiki", "state", "staging")


@contextmanager
def locked(root: Path):
    store = root / ".agentic"
    if store.is_symlink():
        raise WorkflowError(".agentic must not be a symlink")
    store.mkdir(exist_ok=True)
    with (store / "lock").open("a") as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as exc:
            raise WorkflowError("another agentic runner owns this checkout") from exc
        yield


def recover(root: Path) -> None:
    journal = root / ".agentic/promotion.json"
    if not journal.exists():
        return
    data = json.loads(journal.read_text(encoding="utf-8"))
    work = root / ".agentic/work"
    backup = root / ".agentic/previous"
    for folder in TREES:
        live, candidate, old = root / folder, work / folder, backup / folder
        expected = data["candidate"][folder]
        if candidate.exists():
            if manifest(work, (folder,)) != expected:
                raise WorkflowError(f"candidate changed during promotion: {folder}")
            if live.exists():
                if old.exists():
                    raise WorkflowError(
                        f"ambiguous recovery for {folder}; preserve all directories"
                    )
                if manifest(root, (folder,)) != data["before"][folder]:
                    raise WorkflowError(f"live {folder} changed during promotion recovery")
                os.replace(live, old)
                fsync_dir(root)
                fsync_dir(backup)
            os.replace(candidate, live)
            fsync_dir(root)
            fsync_dir(work)
        elif manifest(root, (folder,)) != expected:
            raise WorkflowError(
                f"promoted {folder} changed during recovery; inspect journal "
                "and retained originals in .agentic/previous"
            )
    journal.unlink()
    fsync_dir(journal.parent)


def promote(root: Path, work: Path, before: dict[str, str]) -> None:
    if manifest(root, TREES) != before:
        raise WorkflowError(
            "live wiki/state/staging changed during compilation; refusing promotion"
        )
    candidate = {folder: manifest(work, (folder,)) for folder in TREES}
    for folder in TREES:
        if not (work / folder).is_dir():
            raise WorkflowError(f"missing candidate directory: {folder}")
        for path in (work / folder).rglob("*"):
            if path.is_file():
                with path.open("rb") as source:
                    os.fsync(source.fileno())
    backup = root / ".agentic/previous"
    if backup.exists():
        shutil.rmtree(backup)
    backup.mkdir(parents=True)
    atomic_json(
        root / ".agentic/promotion.json",
        {
            "candidate": candidate,
            "before": {
                folder: {p: h for p, h in before.items() if p.startswith(folder + "/")}
                for folder in TREES
            },
        },
    )
    recover(root)


def checkout_inputs(checkout: Path) -> dict[str, str]:
    """Only inputs consumed by fetch/extras, including the referenced figure bytes."""
    paths = set(checkout.glob("projects/*/README.md")) | set(checkout.glob("projects/*/REPORT.md"))
    paths |= {checkout / "ui/config/collections.yaml"}
    paths |= {checkout / "docs" / name for name in ("discoveries.md", "pitfalls.md")}
    for report in list(paths):
        if report.name == "REPORT.md":
            for figure in re.findall(
                r"!\[[^\]]*\]\((figures/[^)]+)\)", report.read_text(encoding="utf-8")
            ):
                rel = Path(figure)
                if ".." in rel.parts or rel.is_absolute():
                    raise WorkflowError(f"unsafe figure reference in {report}")
                paths.add(report.parent / rel)
    result = {}
    for path in sorted(paths):
        if any(p.is_symlink() for p in (path, *path.parents)):
            raise WorkflowError(f"symlinked checkout input: {path}")
        if path.is_file():
            result[path.relative_to(checkout).as_posix()] = file_hash(path)
    if "ui/config/collections.yaml" not in result:
        raise WorkflowError("observatory checkout must contain ui/config/collections.yaml")
    return result


def run_stage(work: Path, config_path: Path, name: str, module: str, args: list[str]) -> None:
    env = os.environ.copy()
    for key in AUTH_ENV:
        env.pop(key, None)
    env.update(
        BERIL_WIKI_ROOT=str(work),
        BERIL_AGENTIC_CONFIG=str(config_path),
        BERIL_AGENTIC_STAGE=name,
        BERIL_CHECKOUT=str(work / "reference"),
        CONFLICT_SIM="1.01",
        FETCH_BACKEND="local",
    )
    logfile = config_path.parent / f"stage-{name}.log"
    limit = json.loads(config_path.read_text(encoding="utf-8")).get("stage_timeout", 14400)
    command = [sys.executable, "-m", f"beril_wiki.{module}", *args]
    print(f"agentic stage: {name}", flush=True)
    with logfile.open("w") as output:
        process = subprocess.Popen(
            command,
            cwd=work,
            env=env,
            stdout=output,
            stderr=subprocess.STDOUT,
            start_new_session=True,
        )
        started = time.monotonic()
        try:
            while process.poll() is None:
                if time.monotonic() - started > limit or logfile.stat().st_size > 4_000_000:
                    raise WorkflowError(f"stage {name} exceeded time/output limit")
                time.sleep(0.2)
        finally:
            if process.poll() is None:
                os.killpg(process.pid, signal.SIGTERM)
                try:
                    process.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid, signal.SIGKILL)
                    process.wait()
    output_text = logfile.read_text(encoding="utf-8")
    if process.returncode or "[ERROR]" in output_text:
        raise WorkflowError(f"stage {name} failed; see {logfile}\n{output_text[-2500:]}")
    print(output_text[-1000:].strip(), flush=True)


def revision() -> str:
    package = Path(__file__).resolve().parents[1]
    return digest(manifest(package.parent, (package.name,)))


def compiler_revision() -> str:
    """Scientific compiler semantics, excluding CLI versions and unrelated rendering code."""
    package = Path(__file__).resolve().parents[1]
    return digest(
        [
            ast.dump(ast.parse((package / p).read_text(encoding="utf-8")))
            for p in ("agentic/batch.py", "compiler.py", "check.py")
        ]
    )


def fingerprint(root: Path) -> dict[str, str]:
    return {
        p: h for p, h in manifest(root, (*TREES, "contract")).items() if p != "state/agentic.json"
    }


def budget_run(root: Path, base: dict, external: dict, staged: bool) -> str:
    """Changing models on the same input snapshot must not reset prior charges."""
    identity = digest([base, external, staged])
    previous = root / ".agentic/config.json"
    if previous.exists():
        config = json.loads(previous.read_text(encoding="utf-8"))
        legacy = digest([base, external, config.get("model"), staged])
        if config.get("run") in (identity, legacy):
            return config["run"]
        if config.get("run_inputs") == identity:
            return config["run"]
    return identity


def run(root: Path, checkout: Path, config: dict, staged: bool = False) -> dict:
    models = model_signature(config)
    with locked(root):
        recover(root)
        original = manifest(root, TREES)
        base = fingerprint(root)
        external = checkout_inputs(checkout)
        code_revision = revision()
        cli_version = subprocess.run(
            [config["cli"], "--version"], capture_output=True, text=True, timeout=30, check=True
        ).stdout.strip()
        rev = digest(
            [
                code_revision,
                cli_version,
                version("claude-agent-sdk"),
                version("mcp"),
                config.get("max_turns", 6),
            ]
        )
        identity = digest([base, external, rev, models, staged])
        accepted_path = root / "state/agentic.json"
        accepted = (
            json.loads(accepted_path.read_text(encoding="utf-8")) if accepted_path.exists() else {}
        )
        if accepted.get("fingerprint") == identity:
            print("agentic: unchanged; zero model calls")
            return {"unchanged": True}
        store = root / ".agentic"
        work = store / "work"
        if work.exists():
            manifest(work, (*TREES, "contract", "reference"))  # reject symlinks before cleanup
            shutil.rmtree(work)
        work.mkdir()
        for folder in (*TREES, "contract"):
            if (root / folder).exists():
                shutil.copytree(root / folder, work / folder)
            else:
                (work / folder).mkdir()
        for rel in external:
            dst = work / "reference" / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(checkout / rel, dst)
        if checkout_inputs(work / "reference") != external:
            raise WorkflowError("observatory inputs changed while taking snapshot")
        config = config | {
            "root": str(work),
            "store": str(store),
            "revision": rev,
            "run": budget_run(root, base, external, staged),
            "run_inputs": digest([base, external, staged]),
        }
        config_path = store / "config.json"
        atomic_json(config_path, config)
        if not staged:
            shutil.rmtree(work / "staging")
            (work / "staging").mkdir()
            run_stage(work, config_path, "fetch", "stages.fetch", [])
        changed = changed_sources(work)
        scientific_revision = digest(
            [
                compiler_revision(),
                model_signature(config, CORE_MODEL_ROLES),
                manifest(work, ("contract",)),
            ]
        )
        # Compiler/config edits invalidate previous accepted core outputs.
        if accepted and accepted.get("revision") != scientific_revision:
            changed = sorted(p.name for p in (work / "staging").glob("*.md"))
        if accepted:
            prior_outputs = accepted.get("core_outputs", {})
            current_outputs = manifest(work, ("wiki/concepts", "wiki/entities", "wiki/summaries"))
            if prior_outputs != current_outputs:
                # Conservative: manual edits need integration review, never silently adopted.
                changed = sorted(p.name for p in (work / "staging").glob("*.md"))
        agent = Runtime(config)
        agent.ledger.reconcile_stale(store / "transcripts")
        # Apply existing human decisions before planning without entering embeddings.
        run_stage(work, config_path, "decisions", "stages.consolidate", ["--decisions-only"])

        def refresh(name: str, args: list[str]) -> None:
            module = "names" if name == "names-core" else name
            try:
                run_stage(work, config_path, name, f"stages.{module}", args)
            finally:
                # A killed stage leaves its in-flight jobs pending; charge them now.
                agent.ledger.reconcile_stale(store / "transcripts")

        prior = accepted.get("editorial", {}) if accepted.get("version") == 2 else {}
        # Accepted snapshots are recomputed after final naming and figure postprocessing.
        curate(work, agent, changed, refresh, prior)
        refresh("names", [str(work)])
        figure_state = ("state/figures-placements.json", "state/figures-state.json")
        figure_revision = stage_revision(work, "figures", config)
        force_figures = accepted.get("figure_revision") != figure_revision or accepted.get(
            "figure_outputs"
        ) != manifest(work, figure_state)
        refresh("figures", ["--force"] if force_figures else [])
        run_stage(work, config_path, "check", "check", [str(work), "--strict"])
        if (
            fingerprint(root) != base
            or checkout_inputs(checkout) != external
            or revision() != code_revision
        ):
            raise WorkflowError(
                "inputs changed during compilation; saved candidate, refusing promotion"
            )
        next_state = {
            "revision": scientific_revision,
            "fingerprint": digest([fingerprint(work), external, rev, models, staged]),
            "models": model_policy(config),
            "core_outputs": manifest(work, ("wiki/concepts", "wiki/entities", "wiki/summaries")),
            "version": 2,
            "figure_revision": figure_revision,
            "figure_outputs": manifest(work, figure_state),
            "editorial": {name: stage_snapshot(work, name, config) for name in EDITORIAL},
        }
        atomic_json(work / "state/agentic.json", next_state)
        promote(root, work, original)
        totals = agent.ledger.totals()
        print(f"agentic: accepted; {json.dumps(totals)}")
        return totals
