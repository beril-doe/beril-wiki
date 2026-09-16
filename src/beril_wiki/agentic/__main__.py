"""Inspect, compile, and reconcile subscription-backed wiki jobs."""

import argparse
import json
import shutil
from pathlib import Path

import yaml

from beril_wiki.agentic.batch import changed_sources
from beril_wiki.agentic.prose import owning_stage
from beril_wiki.agentic.runner import locked, recover, run
from beril_wiki.agentic.runtime import (
    MODEL_ROLES,
    EvidenceTools,
    Runtime,
    WorkflowError,
    atomic_json,
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
