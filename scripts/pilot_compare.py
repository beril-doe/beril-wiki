"""Per-page outcome of a writing pilot: writer and reviewer usage, tool calls, acceptance.

Usage: uv run python scripts/pilot_compare.py <writer model> page[,page...]
Reads .agentic/jobs.sqlite and .agentic/transcripts; null-cost (Codex) rows count."""

import sqlite3
import sys
from pathlib import Path

REVIEW = ("/science-review", "/verify")


def tool_calls(key: str) -> int:
    path = Path(".agentic/transcripts") / f"{key}.jsonl"
    if not path.is_file():
        return 0
    text = path.read_text(errors="replace")
    # Claude transcripts serialize tool_use blocks by tool name; Codex ones by item type.
    codex = sum(
        1 for line in text.splitlines() if '"item/completed"' in line and '"mcpToolCall"' in line
    )
    return text.count('"name": "mcp__evidence__') + codex


def verdict_of(step: str, output: str) -> str | None:
    from beril_wiki.compiler import parse_json_reply

    try:
        verdict = parse_json_reply(output)
    except ValueError:
        return None
    if step.endswith("/science-review"):
        if verdict.get("accepted") is True:
            return "accepted"
        return f"rejected ({len(verdict.get('issues', []))} issues)"
    if step.endswith("/verify"):
        if verdict.get("open") == []:
            return "accepted after repair"
        return f"open ({len(verdict.get('open', []))} issues)"
    return None


def main() -> None:
    db = sqlite3.connect(".agentic/jobs.sqlite")
    writer, pages = sys.argv[1], sys.argv[2].split(",")
    print(f"{'page':<58} {'writer tok':>10} {'review tok':>10} {'calls':>5}  outcome")
    for page in pages:
        rows = db.execute(
            "select key, step, model, status, coalesce(tokens,0), coalesce(output,'') "
            "from jobs where step like ? order by rowid",
            (f"write/{page}%",),
        ).fetchall()
        first = next((i for i, r in enumerate(rows) if r[2] == writer), None)
        chain = rows[first:] if first is not None else []
        writes = [r for r in chain if not r[1].endswith(REVIEW)]
        reviews = [r for r in chain if r[1].endswith(REVIEW)]
        outcome = "no chain"
        for r in reversed(chain):
            if r[3] == "done" and (found := verdict_of(r[1], r[5])):
                outcome = found
                break
        print(
            f"{page[:58]:<58} {sum(r[4] for r in writes):>10,} "
            f"{sum(r[4] for r in reviews):>10,} {sum(tool_calls(r[0]) for r in writes):>5}  "
            f"{outcome} [{len(chain)} jobs]"
        )


if __name__ == "__main__":
    main()
