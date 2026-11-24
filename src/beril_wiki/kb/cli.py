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
        quota_wait=getattr(args, "quota_wait", None),
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


def cmd_compile(args: argparse.Namespace) -> int:
    from beril_wiki.kb import compile as compiler
    from beril_wiki.kb import workflow

    try:
        result = compiler.compile_corpus(
            args.root,
            config_from(args),
            [s for s in args.sources.split(",") if s] or None,
            records=not args.pages_only,
            retry=args.retry_rejected,
            write=not args.claims_only,
            route=not args.routes_only,
        )
    except workflow.Stop as exc:
        raise SystemExit(f"compile: {exc}") from None
    print(json.dumps(result, ensure_ascii=False, indent=None if args.json else 1))
    # A compile that stopped where a --…-only flag asked it to did what it was asked.
    return 0 if result["status"] == "done" or result.get("checkpoint") else 2


def cmd_runs(args: argparse.Namespace) -> int:
    runs = args.root / ".agentic" / "runs"
    for path in sorted(runs.glob("*/run.json")) if runs.is_dir() else []:
        state = json.loads(path.read_text(encoding="utf-8"))
        print(
            f"{state['run']:<60} {state['status']:<8} {state['tokens']:>10,} tokens "
            f"USD {state['usd']:.2f}  {len(state['sessions'])} sessions"
        )
    return 0


def cmd_status(args: argparse.Namespace) -> int:
    """One screen on the newest run: what it is on, what is open or waiting, what
    failed, and a verdict. Exits 0 while nobody is needed, 3 when someone is."""
    import time

    from beril_wiki.kb import workflow

    records = list((args.root / ".agentic" / "runs").glob("*/run.json"))
    if not records:
        raise SystemExit("status: no run in this checkout")

    def taken_over(record: Path) -> tuple[int, str]:
        # A run resumed today is newer than one started yesterday and begun after it.
        started = json.loads(record.read_text(encoding="utf-8")).get("started", 0)
        return started, record.parent.name

    path = max(records, key=taken_over)
    deadline = time.time() + args.watch
    while True:
        state = json.loads(path.read_text(encoding="utf-8"))
        now = time.time()
        running = workflow.alive(int(state.get("pid", 0) or 0)) if state.get("pid") else False
        verdict, reason = workflow.health(state, now, running)
        if verdict != "ok" or now >= deadline:
            break
        time.sleep(min(15.0, deadline - now))
    sessions = state["sessions"]
    stage = state.get("stage") or {}
    progress = f" {stage.get('done') or 0}/{stage['total']}" if stage.get("total") else ""
    lately = [s for s in sessions if now - s.get("at", 0) <= 300]
    refused = [s for s in sessions[-20:] if s.get("retry", workflow.turned_away(s["error"]))]
    failed = [s for s in sessions[-20:] if not s["ok"] and s not in refused]
    waiting = state.get("waiting", {})
    opened = [n for n in state.get("open", {}) if n not in waiting]
    print(f"{state['run']}  {state['status']}")
    print(f"stage    {stage.get('label', '?')}{progress}")
    print(
        f"sessions {len(sessions)} finished, {len(lately)} in the last 5 min, "
        f"{len(opened)} open, {len(waiting)} waiting on a vendor"
    )
    print(
        f"failed   {len(failed)} of the last {len(sessions[-20:])}; a vendor turned away "
        f"{len(refused)} more, which are asked again"
    )
    for error in sorted({s["error"][:110] for s in failed}):
        print(f"         {error}")
    print(f"spend    {state['tokens']:,} tokens held or used, USD {state['usd']:.2f}")
    if sessions and sessions[-1].get("at"):
        print(f"last     {sessions[-1]['name'][:70]}, {now - sessions[-1]['at']:.0f}s ago")
    print(f"verdict  {verdict}" + (f": {reason}" if reason else ""))
    return 0 if verdict in ("ok", "done") else 3


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
    p = sub.add_parser("status", help="whether the newest run is working, on one screen")
    p.add_argument(
        "--watch",
        type=float,
        default=0.0,
        metavar="SECONDS",
        help="return when the run needs someone or ends, or after this long",
    )
    p.set_defaults(run=cmd_status)

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

    p = sub.add_parser("compile", help="build every page and record from the reports")
    p.add_argument("--sources", default="", help="report ids, comma separated (default: all)")
    p.add_argument("--claims-only", action="store_true", help="stop when the reports are read")
    p.add_argument("--routes-only", action="store_true", help="stop when the claims are routed")
    p.add_argument("--pages-only", action="store_true", help="stop before the record stages")
    p.add_argument(
        "--retry-rejected",
        action="store_true",
        help="write again the pages an earlier attempt of this run refused",
    )
    p.add_argument(
        "--quota-wait",
        type=float,
        help="seconds to keep waiting when a vendor is out of quota (default: stop at once)",
    )
    model_flags(p)
    p.set_defaults(run=cmd_compile)

    args = parser.parse_args(argv)
    args.root = args.root.resolve()
    return args.run(args)


if __name__ == "__main__":
    sys.exit(main())
