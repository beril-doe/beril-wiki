"""Curator scheduling and recoverable promotion of isolated output."""

from __future__ import annotations

import fcntl
import json
import os
import shutil
import signal
import subprocess
import sys
import time
import uuid
from contextlib import contextmanager
from importlib.metadata import version
from pathlib import Path

from beril_wiki import compiler as C
from beril_wiki.agentic import progress
from beril_wiki.agentic.batch import INTEGRATION_REVISION, changed_sources, retryable
from beril_wiki.agentic.curator import (
    EDITORIAL,
    curate,
    pending_actions,
    stage_revision,
    stage_snapshot,
)
from beril_wiki.agentic.runtime import (
    AUTH_ENV,
    Runtime,
    WorkflowError,
    atomic_json,
    contract_manifest,
    digest,
    file_hash,
    fsync_dir,
    manifest,
    model_policy,
    model_signature,
)
from beril_wiki.corpus import FIG_EMBED
from beril_wiki.stages.novelty import labels_due

TREES = ("wiki", "state", "staging")
# Pages integration writes; an edit outside a run makes the next one re-integrate.
CORE_OUTPUTS = ("wiki/concepts", "wiki/entities", "wiki/summaries")


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
            for figure in FIG_EMBED.findall(report.read_text(encoding="utf-8")):
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


def unlink_missing(work: Path) -> None:
    """Keep the label of a link to a page that was never written, dropping its brackets.

    A writer may link any page the plan schedules; when a new page then fails its
    rounds, the links to it dangle and the strict check refuses the whole compile (34
    such links in the first full compile). Derived pages already repair links in code;
    this does the same for the rest, after every stage has read its inputs."""
    targets = C.wikilink_targets(work)
    for page in sorted((work / "wiki").rglob("*.md")):
        text = page.read_text(encoding="utf-8")
        fixed = C.downgrade_dead_links(text, targets)
        if fixed != text:
            page.write_text(fixed, encoding="utf-8")


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
    config = json.loads(config_path.read_text(encoding="utf-8"))
    limit = config.get("stage_timeout", 14400)
    command = [sys.executable, "-m", f"beril_wiki.{module}", *args]
    print(f"agentic stage: {name}", flush=True)

    def report(event: str, **extra: object) -> None:
        if progress.enabled():
            totals = progress.snapshot(config_path.parent, config.get("run", ""))
            progress.emit(event, stage=name, **totals, **extra)

    report("stage_start")
    try:
        _run_stage(work, env, logfile, command, name, limit)
    except BaseException as exc:
        report("stage_end", ok=False, error=str(exc)[-500:])
        raise
    report("stage_end", ok=True)


def _run_stage(
    work: Path, env: dict[str, str], logfile: Path, command: list[str], name: str, limit: float
) -> None:
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


# How the accepted revision is computed. A state accepted under another scheme cannot
# be compared with this one and is adopted once rather than re-integrated. Scheme 5
# took model identities out of every revision: a model change applies to pages written
# from then on, so a cheaper model never recompiles the accepted wiki.
REVISION_SCHEME = 5


def compiler_revision() -> str:
    """What integration means, as the explicit revision alone: hashing compiler.py and
    check.py made an unrelated edit to either re-plan and rewrite the corpus. The
    contract still re-integrates, as a deliberate scientific change; the model policy
    does not."""
    return digest([INTEGRATION_REVISION])


def scientific_revision(root: Path) -> str:
    return digest([compiler_revision(), contract_manifest(root)])


def fingerprint(root: Path) -> dict[str, str]:
    return {
        p: h for p, h in manifest(root, (*TREES, "contract")).items() if p != "state/agentic.json"
    }


def adopt_editorial(work: Path, prior: dict) -> dict:
    """Re-stamp each derived stage accepted under the previous scheme whose inputs and
    outputs are still the ones it recorded, so the new formula alone rewrites nothing.
    A stage whose files moved keeps its old snapshot and runs as it would have."""
    adopted = dict(prior)
    for name, snapshot in prior.items():
        if name not in EDITORIAL:
            continue
        now = stage_snapshot(work, name)
        if snapshot.get("inputs") == now["inputs"] and snapshot.get("outputs") == now["outputs"]:
            adopted[name] = now
    return adopted


def adopts(accepted: dict, contract: str) -> bool:
    """A state accepted under another scheme is adopted, not rewritten, when its
    contract is the one in force. States from scheme 5 on record their contract; an
    older one cannot say, and adopting it assumes the contract has not changed since."""
    return (
        bool(accepted)
        and accepted.get("revision_scheme") != REVISION_SCHEME
        and accepted.get("contract", contract) == contract
    )


def load_accepted(root: Path) -> dict:
    path = root / "state/agentic.json"
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def invalidation(work: Path, accepted: dict, adopting: bool) -> str | None:
    """Which accepted record makes a run re-integrate every staged source, if any."""
    if not accepted:
        return None
    # A revision accepted under another scheme cannot be recomputed here, and
    # re-integrating every source to find out would re-plan the corpus; it is adopted.
    if accepted.get("revision") != scientific_revision(work) and not adopting:
        return "revision"
    # Conservative: manual edits need integration review, never silently adopted.
    if accepted.get("core_outputs", {}) != manifest(work, CORE_OUTPUTS):
        return "core_outputs"
    return None


def due_editorial(root: Path) -> list[str]:
    """Editorial stages whose fingerprint no longer matches the accepted state, comparing
    a state accepted under an earlier revision scheme as the next run adopts it."""
    accepted = load_accepted(root)
    prior = accepted.get("editorial", {})
    if adopts(accepted, digest(contract_manifest(root))):
        prior = adopt_editorial(root, prior)
    return pending_actions(root, prior, integrated=True)


def snapshot_trees(root: Path, work: Path, checkout: Path, external: dict[str, str]) -> None:
    """Copy the live trees into `work`, and the checkout's inputs into `work/reference`."""
    for folder in (*TREES, "contract"):
        if (root / folder).exists():
            shutil.copytree(root / folder, work / folder)
        else:
            (work / folder).mkdir(parents=True)
    for rel in external:
        dst = work / "reference" / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(checkout / rel, dst)
    if checkout_inputs(work / "reference") != external:
        raise WorkflowError("observatory inputs changed while taking snapshot")


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
        if labels_due(root):
            # Literature labels expire with time alone, which no fingerprint sees.
            identity = digest([identity, "labels-due"])
        accepted = load_accepted(root)
        store = root / ".agentic"
        retry = retryable(store)
        if accepted.get("fingerprint") == identity and not retry:
            print("agentic: unchanged; zero model calls")
            return {"unchanged": True}
        work = store / "work"
        if work.exists():
            manifest(work, (*TREES, "contract", "reference"))  # reject symlinks before cleanup
            shutil.rmtree(work)
        work.mkdir()
        snapshot_trees(root, work, checkout, external)
        config = config | {
            "root": str(work),
            "store": str(store),
            "revision": rev,
            "run": config.get("budget_run") or budget_run(root, base, external, staged),
            "run_inputs": digest([base, external, staged]),
        }
        if config.get("budget_run"):
            # Stage subprocesses read this from config.json, so each tags its jobs.
            config["invocation"] = uuid.uuid4().hex
        config_path = store / "config.json"
        atomic_json(config_path, config)
        if not staged:
            shutil.rmtree(work / "staging")
            (work / "staging").mkdir()
            run_stage(work, config_path, "fetch", "stages.fetch", [])
        changed = changed_sources(work)
        scientific = scientific_revision(work)
        contract = digest(contract_manifest(work))
        adopting = adopts(accepted, contract)
        if adopting and "contract" not in accepted:
            print("agentic: adopting a state with no recorded contract; assuming it is unchanged")
        if adopting and accepted.get("revision") != scientific:
            # Promotion records the current scheme, so this happens once.
            print("agentic: adopting the accepted revision under explicit revisions")
        if invalidation(work, accepted, adopting):
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
        if adopting:
            prior = adopt_editorial(work, prior)
        # Accepted snapshots are recomputed after final naming and figure postprocessing.
        curate(work, agent, changed, refresh, prior, retry)
        refresh("titles", [str(work)])
        refresh("names", [str(work)])
        refresh("errata", [str(work)])
        figure_state = ("state/figures-placements.json", "state/figures-state.json")
        figure_revision = stage_revision(work, "figures")
        figures_current = accepted.get("figure_outputs") == manifest(work, figure_state)
        force_figures = not figures_current or (
            accepted.get("figure_revision") != figure_revision and not adopting
        )
        refresh("figures", ["--force"] if force_figures else [])
        unlink_missing(work)
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
            "revision": scientific,
            "revision_scheme": REVISION_SCHEME,
            "contract": contract,
            "fingerprint": digest([fingerprint(work), external, rev, models, staged]),
            "models": model_policy(config),
            "core_outputs": manifest(work, CORE_OUTPUTS),
            "version": 2,
            "figure_revision": figure_revision,
            "figure_outputs": manifest(work, figure_state),
            "editorial": {name: stage_snapshot(work, name) for name in EDITORIAL},
        }
        atomic_json(work / "state/agentic.json", next_state)
        promote(root, work, original)
        totals = agent.ledger.totals()
        failures_path = store / "failures.json"
        failures = (
            json.loads(failures_path.read_text(encoding="utf-8")) if failures_path.exists() else {}
        )
        print(f"agentic: accepted; {json.dumps(totals)}")
        for page, entry in sorted(failures.items()):
            issues = "; ".join(
                f"{i.get('category')}: {i.get('quote') or i.get('note')}"[:120]
                for i in entry["issues"][:4]
            )
            print(f"agentic: failed page {page} ({entry['step']}): {issues}")
        if failures:
            print(
                f"agentic: {len(failures)} page(s) kept their previous version; integrated "
                "pages are re-drafted on the next run up to their retry limit, derived ones "
                "after `retry --page PAGE`; see .agentic/failures.json"
            )
        return totals | {"failures": sorted(failures)}
