"""Inspect, compile, and reconcile subscription-backed wiki jobs."""

import argparse
import json
import shutil
from pathlib import Path

from beril_wiki.agentic.batch import changed_sources
from beril_wiki.agentic.runner import locked, recover, run
from beril_wiki.agentic.runtime import EvidenceTools, Runtime, WorkflowError
from beril_wiki.paths import ROOT
from beril_wiki.stages.fetch import CHECKOUT


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
    execute.add_argument("--model", required=True)
    execute.add_argument("--max-tokens", type=int, required=True)
    execute.add_argument("--max-jobs", type=int, required=True)
    execute.add_argument("--reserve-tokens", type=int, default=50_000)
    execute.add_argument("--max-turns", type=int, default=12)
    execute.add_argument("--max-actions", type=int, default=16)
    execute.add_argument("--max-output-tokens", type=int, default=32768)
    execute.add_argument("--timeout", type=int, default=600)
    execute.add_argument("--checkout", type=Path, default=CHECKOUT)
    execute.add_argument(
        "--staged", action="store_true", help="use current staging instead of fetching"
    )
    execute.add_argument("--cli", default=shutil.which("claude"))
    account = commands.add_parser("account", help="reconcile unknown usage; does not retry")
    account.add_argument("--job", required=True)
    account.add_argument("--tokens", type=int, required=True)
    retry = commands.add_parser("retry", help="explicitly retry one saved failed/rejected job")
    retry.add_argument("--job", required=True)
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
                if args.command == "status":
                    rows = agent.ledger.db.execute(
                        "SELECT key,step,status,tokens,error FROM jobs ORDER BY rowid"
                    ).fetchall()
                    print(json.dumps({"totals": agent.ledger.totals(), "jobs": rows}, indent=2))
                elif args.command == "account":
                    agent.ledger.account(args.job, args.tokens)
                else:
                    with agent.ledger.db:
                        changed = agent.ledger.db.execute(
                            "UPDATE jobs SET status='rejected' WHERE key=? "
                            "AND status IN ('done','failed')",
                            (args.job,),
                        ).rowcount
                    if not changed:
                        raise WorkflowError("job must be completed or reconciled before retry")
        else:
            if not args.cli:
                raise WorkflowError("install Claude Code and log in with a subscription first")
            for field in (
                "max_tokens",
                "max_jobs",
                "reserve_tokens",
                "max_turns",
                "max_actions",
                "max_output_tokens",
                "timeout",
            ):
                if getattr(args, field) <= 0:
                    raise WorkflowError(f"{field} must be positive")
            config = {
                key: getattr(args, key)
                for key in (
                    "model",
                    "max_tokens",
                    "max_jobs",
                    "reserve_tokens",
                    "max_turns",
                    "max_actions",
                    "max_output_tokens",
                    "timeout",
                    "cli",
                )
            }
            run(root, args.checkout.resolve(), config, args.staged)
    except (WorkflowError, OSError, ValueError) as exc:
        print(f"agentic stopped: {exc}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
