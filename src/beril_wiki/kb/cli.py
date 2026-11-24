"""``beril-wiki``: the operator's commands over the same functions agents call.

    beril-wiki index                      rebuild the SQLite index and print its counts
    beril-wiki import-evidence --from D   one-time import of the legacy evidence store
    beril-wiki plan [--json]              the model work the corpus calls for, and why
    beril-wiki impact --source ID         sections that rest on a report or a claim
    beril-wiki lint                       free checks on claims, links and the backlog
    beril-wiki tool NAME '{json args}'    call one wiki tool and print its JSON reply
    beril-wiki mcp [--write]              serve the tools to an MCP client over stdio
    beril-wiki ingest ID                  read a new report into the wiki
    beril-wiki revise ID                  apply a revised report to the sections it reaches
    beril-wiki refresh SECTION... --why   re-edit named sections for a stated reason
    beril-wiki runs                       past runs with their spend

Only ingest, revise and refresh call a model, and each stops at ``--max-tokens`` or
``--max-usd``.
"""

from __future__ import annotations

import argparse
import inspect
import json
import sys
from pathlib import Path

from beril_wiki.paths import ROOT


def emit(value: object) -> None:
    print(json.dumps(value, ensure_ascii=False, indent=1))


def cmd_index(args: argparse.Namespace) -> int:
    from beril_wiki.kb import index

    index.build(args.root)
    db = index.connect(args.root)
    tables = ("sources", "claims", "pages", "sections", "section_claims", "links", "aliases")
    emit({t: db.execute(f"SELECT count(*) FROM {t}").fetchone()[0] for t in tables})
    return 0


def cmd_import(args: argparse.Namespace) -> int:
    from beril_wiki.kb import importer

    emit(importer.run(args.root, Path(args.legacy).expanduser()))
    return 0


def cmd_plan(args: argparse.Namespace) -> int:
    from beril_wiki.kb import workflow

    result = workflow.plan(args.root)
    if args.json:
        print(json.dumps(result))
    elif not result["tasks"]:
        print("nothing to do: every report in corpus/ matches the hash last ingested")
    else:
        for task in result["tasks"]:
            print(f"{task['workflow']:<7} {task['source']}  ({task['reason']})")
    return 0


def cmd_impact(args: argparse.Namespace) -> int:
    from beril_wiki.kb import workflow

    if not (args.source or args.claim or args.section):
        raise SystemExit("impact: give --source, --claim or --section")
    emit(workflow.impact(args.root, args.source, args.claim, args.section))
    return 0


def cmd_lint(args: argparse.Namespace) -> int:
    from beril_wiki.kb import workflow

    emit(workflow.lint(args.root))
    return 0


def cmd_tool(args: argparse.Namespace) -> int:
    from beril_wiki.kb.tools import Session, Tools

    tools = Tools(args.root, Session.start("maintain" if args.write else "reader"))
    if args.name in (None, "list"):
        for name in tools.names():
            method = getattr(tools, name)
            first = (inspect.getdoc(method) or "").splitlines()[0]
            print(f"{name}{inspect.signature(method)}\n    {first}")
        return 0
    try:
        call_args = json.loads(args.args) if args.args else {}
    except ValueError as exc:
        raise SystemExit(f"tool: arguments must be a JSON object: {exc}") from None
    reply = tools.call(args.name, **call_args)
    emit(reply)
    return 0 if reply["ok"] else 1


def cmd_mcp(args: argparse.Namespace) -> int:
    from beril_wiki.kb import server

    server.stdio(args.root, "maintain" if args.write else "reader")
    return 0


def config_from(args: argparse.Namespace):
    from beril_wiki.kb.workflow import Config

    return Config.load(
        args.root,
        extract=args.extract,
        curate=args.curate,
        edit=args.edit,
        review=args.review,
        max_tokens=args.max_tokens,
        max_usd=args.max_usd,
        max_sections=args.max_sections,
        jobs=args.jobs,
    )


def report(result: dict, as_json: bool) -> int:
    from beril_wiki.kb.workflow import describe

    print(json.dumps(result, ensure_ascii=False) if as_json else describe(result))
    return 0 if result["status"] == "done" else 2


def cmd_workflow(args: argparse.Namespace) -> int:
    from beril_wiki.kb import workflow

    try:
        config = config_from(args)
        if args.command == "refresh":
            result = workflow.refresh(args.root, args.sections, args.why, config)
        else:
            run = workflow.ingest if args.command == "ingest" else workflow.revise
            result = run(args.root, args.source, config)
    except workflow.Stop as exc:
        raise SystemExit(f"{args.command}: {exc}") from None
    return report(result, args.json)


def cmd_runs(args: argparse.Namespace) -> int:
    runs = args.root / ".agentic" / "runs"
    for path in sorted(runs.glob("*/run.json")) if runs.is_dir() else []:
        state = json.loads(path.read_text(encoding="utf-8"))
        print(
            f"{state['run']:<60} {state['status']:<8} {state['tokens']:>10,} tokens "
            f"USD {state['usd']:.2f}  {len(state['sessions'])} sessions"
        )
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="beril-wiki", description=__doc__.split("\n\n")[0])
    parser.add_argument("--root", type=Path, default=ROOT, help="the wiki checkout")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("index", help="rebuild the index").set_defaults(run=cmd_index)
    p = sub.add_parser("import-evidence", help="import the legacy evidence store")
    p.add_argument("--from", dest="legacy", required=True, help="the old .agentic folder")
    p.set_defaults(run=cmd_import)
    p = sub.add_parser("plan", help="list the model work the corpus calls for")
    p.add_argument("--json", action="store_true")
    p.set_defaults(run=cmd_plan)
    p = sub.add_parser("impact", help="sections that rest on a report or claim")
    p.add_argument("--source", default="")
    p.add_argument("--claim", default="")
    p.add_argument("--section", default="")
    p.set_defaults(run=cmd_impact)
    sub.add_parser("lint", help="free checks on the records").set_defaults(run=cmd_lint)
    p = sub.add_parser("tool", help="call one wiki tool")
    p.add_argument("name", nargs="?")
    p.add_argument("args", nargs="?", help="a JSON object of arguments")
    p.add_argument("--write", action="store_true", help="allow gated edits")
    p.set_defaults(run=cmd_tool)
    p = sub.add_parser("mcp", help="serve the tools over stdio")
    p.add_argument("--write", action="store_true", help="allow gated edits")
    p.set_defaults(run=cmd_mcp)
    sub.add_parser("runs", help="past runs and their spend").set_defaults(run=cmd_runs)

    def model_flags(p: argparse.ArgumentParser) -> None:
        for role in ("extract", "curate", "edit", "review"):
            p.add_argument(f"--{role}", help=f"model@effort for the {role} role")
        p.add_argument("--max-tokens", type=int, help="stop when the run has used this many")
        p.add_argument("--max-usd", type=float, help="stop at this reported or estimated spend")
        p.add_argument("--max-sections", type=int, help="sections one run may edit")
        p.add_argument("--jobs", type=int, help="sections edited at once")
        p.add_argument("--json", action="store_true")

    p = sub.add_parser("ingest", help="read a new report into the wiki")
    p.add_argument("source")
    model_flags(p)
    p.set_defaults(run=cmd_workflow)
    p = sub.add_parser("revise", help="apply a revised report")
    p.add_argument("source")
    model_flags(p)
    p.set_defaults(run=cmd_workflow)
    p = sub.add_parser("refresh", help="re-edit named sections for a stated reason")
    p.add_argument("sections", nargs="+", help="section ids, such as concepts/x#tensions")
    p.add_argument("--why", required=True, help="the instruction the editor receives")
    model_flags(p)
    p.set_defaults(run=cmd_workflow)

    args = parser.parse_args(argv)
    args.root = args.root.resolve()
    return args.run(args)


if __name__ == "__main__":
    sys.exit(main())
