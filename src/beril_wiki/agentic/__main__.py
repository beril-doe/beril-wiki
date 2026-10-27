"""Inspect, compile, and reconcile subscription-backed wiki jobs."""

import argparse
import json
import shutil
import signal
import sys
from pathlib import Path

import yaml

from beril_wiki.agentic.batch import changed_sources
from beril_wiki.agentic.prose import owning_stage
from beril_wiki.agentic.runner import locked, recover, run, run_stage
from beril_wiki.agentic.runtime import (
    MODEL_ROLES,
    EvidenceTools,
    Runtime,
    WorkflowError,
    atomic_json,
    digest,
    manifest,
    model_policy,
)
from beril_wiki.paths import ROOT
from beril_wiki.stages.fetch import CHECKOUT


def load_models(root: Path, path: Path | None, model: str | None, overrides: list[str]) -> dict:
    """Load repository policy, then apply an all-role override and individual overrides."""
    source = root / (path or "agentic.yaml")
    config: dict = {}
    if source.exists() or path is not None:
        try:
            config = yaml.safe_load(source.read_text(encoding="utf-8"))
        except yaml.YAMLError as exc:
            raise WorkflowError(f"invalid model config {source}: {exc}") from exc
        if not isinstance(config, dict) or set(config) - {"model", "step_models"}:
            raise WorkflowError("model config must contain only model and step_models")
        model_policy(config)
    if model is not None:
        config = {"model": model}
    roles = {}
    for value in overrides:
        role, separator, selected = value.partition("=")
        if not separator or role not in MODEL_ROLES or not selected.strip():
            raise WorkflowError(f"invalid step-model {value!r}; use ROLE=MODEL")
        if role in roles:
            raise WorkflowError(f"duplicate step-model role: {role}")
        roles[role] = selected.strip()
    config["step_models"] = config.get("step_models", {}) | roles
    model_policy(config)
    return config


def load_failures(root: Path) -> dict:
    path = root / ".agentic/failures.json"
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


CARD_STAGES = ("headlines", "novelty", "directions")


def run_cards(root: Path, config: dict) -> dict:
    """Run only the finding, label and research-direction stages in place, then the strict check.

    For a pilot: `run` would also schedule every other stale editorial stage. These
    stages write only their own outputs, and their hash caches let a later full run
    adopt what they wrote without model calls. The accepted state is not touched."""
    store = root / ".agentic"
    if (store / "promotion.json").exists():
        raise WorkflowError("promotion pending; run recover first")
    config = config | {
        "root": str(root),
        "store": str(store),
        "run": digest(["cards", manifest(root, ("wiki", "state", "contract"))]),
    }
    # The same file run() writes, so status, account and retry read this run.
    path = store / "config.json"
    atomic_json(path, config)
    agent = Runtime(config)
    agent.ledger.reconcile_stale(store / "transcripts")
    # Python's default SIGTERM skips finally blocks, which would orphan the stage's
    # process group; an exit runs run_stage's cleanup instead.
    previous = signal.signal(signal.SIGTERM, lambda *_: sys.exit(143))
    try:
        for name in CARD_STAGES:
            run_stage(root, path, name, f"stages.{name}", [])
        run_stage(root, path, "check", "check", [str(root), "--strict"])
    finally:
        signal.signal(signal.SIGTERM, previous)
        agent.ledger.reconcile_stale(store / "transcripts")
    totals = agent.ledger.totals()
    print(f"agentic cards: {json.dumps(totals)}")
    return totals


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser(
        "plan", help="inspect currently staged source changes; no network/model calls"
    )
    search = commands.add_parser("search", help="search accepted wiki text; no model calls")
    search.add_argument("query")
    search.add_argument("--offset", type=int, default=0)
    execute = commands.add_parser(
        "run", help="compile in isolation, validate, then promote locally"
    )
    execute.add_argument("--model", help="replace the YAML policy with this model for every role")
    execute.add_argument(
        "--model-config",
        type=Path,
        help="model YAML path relative to --root (default: agentic.yaml)",
    )
    execute.add_argument(
        "--step-model",
        action="append",
        default=[],
        metavar="ROLE=MODEL",
        help=f"override a role's model; repeat for roles: {', '.join(MODEL_ROLES)}",
    )
    execute.add_argument("--max-tokens", type=int, required=True)
    execute.add_argument("--max-jobs", type=int, required=True)
    execute.add_argument("--reserve-tokens", type=int, default=50_000)
    execute.add_argument("--max-turns", type=int, default=12)
    execute.add_argument("--max-output-tokens", type=int, default=32768)
    execute.add_argument("--timeout", type=int, default=600)
    execute.add_argument(
        "--stage-timeout", type=int, default=14400, help="seconds allowed per stage subprocess"
    )
    execute.add_argument(
        "--stage-max-tokens",
        type=int,
        default=0,
        help="effective-token admission ceiling per stage (0: only the run ceiling)",
    )
    execute.add_argument(
        "--workers", type=int, default=4, help="page jobs run concurrently inside each stage"
    )
    execute.add_argument(
        "--write-only",
        default="",
        help="pilot: write only these comma-separated page paths, then stop before any "
        "source is recorded as integrated",
    )
    execute.add_argument(
        "--pass-records",
        type=int,
        default=60,
        help="write a page assigned more records than this in passes of at most this many "
        "(0: one write)",
    )
    execute.add_argument(
        "--write-effort",
        choices=("low", "medium", "high", "xhigh", "max"),
        help="reasoning effort for page writers (default: the model's own)",
    )
    execute.add_argument(
        "--strict-pages",
        action="store_true",
        help="stop the run when a page fails its patch rounds instead of recording it",
    )
    execute.add_argument("--checkout", type=Path, default=CHECKOUT)
    execute.add_argument(
        "--staged", action="store_true", help="use current staging instead of fetching"
    )
    execute.add_argument("--cli", default=shutil.which("claude"))
    account = commands.add_parser("account", help="reconcile unknown usage; does not retry")
    account.add_argument("--job", required=True)
    account.add_argument("--tokens", type=int, required=True)
    retry = commands.add_parser(
        "retry", help="re-issue saved jobs: by key, by failed page, or every failed page"
    )
    retry.add_argument("--job", action="append", default=[], help="full job key; repeatable")
    retry.add_argument(
        "--page", action="append", default=[], help="page key from failures.json; repeatable"
    )
    retry.add_argument("--all-failed", action="store_true", help="every page in failures.json")
    pilot = commands.add_parser(
        "cards",
        help="run only the finding, label and direction stages in place, then check --strict",
    )
    for flag, default in (
        ("--max-tokens", None),
        ("--max-jobs", None),
        ("--reserve-tokens", 50_000),
        ("--max-turns", 12),
        ("--max-output-tokens", 32768),
        ("--timeout", 600),
        ("--stage-timeout", 14400),
        ("--stage-max-tokens", 0),
        ("--workers", 4),
    ):
        pilot.add_argument(flag, type=int, default=default, required=default is None)
    pilot.add_argument("--model-config", type=Path)
    pilot.add_argument("--step-model", action="append", default=[], metavar="ROLE=MODEL")
    pilot.add_argument("--cli", default=shutil.which("claude"))
    commands.add_parser("recover", help="finish an interrupted promotion without model calls")
    commands.add_parser("status", help="show durable job IDs, states and usage")
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        if args.command == "plan":
            if not any((root / "staging").glob("*.md")):
                print("No staged sources. Use agentic run to fetch into its isolated workspace.")
                return 0
            if (root / ".agentic/promotion.json").exists():
                raise WorkflowError("promotion pending; run recover before inspection")
            print(json.dumps({"changed_sources": changed_sources(root)}, indent=2))
        elif args.command == "search":
            with locked(root):
                if (root / ".agentic/promotion.json").exists():
                    raise WorkflowError("promotion pending; run recover before searching")
                print(
                    json.dumps(EvidenceTools(root).search(args.query, offset=args.offset), indent=2)
                )
        elif args.command == "cards":
            if not args.cli:
                raise WorkflowError("install Claude Code and log in with a subscription first")
            if min(args.max_tokens, args.max_jobs, args.workers, args.timeout) <= 0:
                raise WorkflowError("budgets, workers and timeout must be positive")
            config = {
                key: getattr(args, key)
                for key in (
                    "max_tokens",
                    "max_jobs",
                    "reserve_tokens",
                    "max_turns",
                    "max_output_tokens",
                    "timeout",
                    "stage_timeout",
                    "stage_max_tokens",
                    "workers",
                    "cli",
                )
            } | load_models(root, args.model_config, None, args.step_model)
            print(json.dumps({"models": model_policy(config)}, indent=2))
            with locked(root):
                run_cards(root, config)
        elif args.command == "recover":
            with locked(root):
                recover(root)
        elif args.command in ("account", "retry", "status"):
            with locked(root):
                agent = Runtime(json.loads((root / ".agentic/config.json").read_text()))
                failures = load_failures(root)
                if args.command == "status":
                    rows = agent.ledger.db.execute(
                        "SELECT key,step,status,tokens,effective,error,model FROM jobs "
                        "ORDER BY rowid"
                    ).fetchall()
                    print(
                        json.dumps(
                            {"totals": agent.ledger.totals(), "failures": failures, "jobs": rows},
                            indent=2,
                        )
                    )
                elif args.command == "account":
                    agent.ledger.account(args.job, args.tokens)
                else:
                    pages = list(failures) if args.all_failed else args.page
                    if unknown := [p for p in pages if p not in failures]:
                        raise WorkflowError(f"not in failures.json: {unknown}")
                    keys = args.job + [k for p in pages for k in failures[p]["jobs"]]
                    if not keys:
                        raise WorkflowError("retry needs --job, --page or --all-failed")
                    with agent.ledger.db:
                        changed = sum(
                            agent.ledger.db.execute(
                                "UPDATE jobs SET status='rejected' WHERE key=? "
                                "AND status IN ('done','failed')",
                                (key,),
                            ).rowcount
                            for key in keys
                        )
                    if not changed:
                        raise WorkflowError("job must be completed or reconciled before retry")
                    # An accepted run's fingerprint would otherwise short-circuit the next
                    # run before it looks at the ledger; make the owning stages stale.
                    accepted = root / "state/agentic.json"
                    if accepted.exists():
                        state = json.loads(accepted.read_text(encoding="utf-8"))
                        state.pop("fingerprint", None)
                        for stage in {owning_stage(p) for p in pages}:
                            state.get("editorial", {}).pop(stage, None)
                        atomic_json(accepted, state)
                    print(f"retry: {changed} job(s) will be re-issued on the next run")
        else:
            if not args.cli:
                raise WorkflowError("install Claude Code and log in with a subscription first")
            for field in (
                "max_tokens",
                "max_jobs",
                "reserve_tokens",
                "max_turns",
                "max_output_tokens",
                "timeout",
                "stage_timeout",
                "workers",
            ):
                if getattr(args, field) <= 0:
                    raise WorkflowError(f"{field} must be positive")
            if args.pass_records < 0:
                raise WorkflowError("pass_records must not be negative")
            if args.stage_max_tokens < 0:
                raise WorkflowError("stage_max_tokens must not be negative")
            config = {
                key: getattr(args, key)
                for key in (
                    "max_tokens",
                    "max_jobs",
                    "reserve_tokens",
                    "max_turns",
                    "max_output_tokens",
                    "timeout",
                    "stage_timeout",
                    "stage_max_tokens",
                    "workers",
                    "write_only",
                    "pass_records",
                    "write_effort",
                    "strict_pages",
                    "cli",
                )
            }
            config.update(load_models(root, args.model_config, args.model, args.step_model))
            print(json.dumps({"models": model_policy(config)}, indent=2))
            run(root, args.checkout.resolve(), config, args.staged)
    except (WorkflowError, OSError, ValueError) as exc:
        print(f"agentic stopped: {exc}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
