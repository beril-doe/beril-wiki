"""JSON progress lines a supervisor can tail while a run spends.

`$BERIL_WIKI_PROGRESS` names the file. Stage subprocesses inherit it, so a job that
finishes inside one writes its own line."""

from __future__ import annotations

import json
import os
import sqlite3
from datetime import UTC, datetime
from pathlib import Path

ENV = "BERIL_WIKI_PROGRESS"


def enabled() -> bool:
    return bool(os.environ.get(ENV))


def emit(event: str, **fields: object) -> None:
    """Append one `{"ts", "source": "wiki", "event", ...fields}` line, if a file is set.

    A full disk or a removed directory must not stop a run that is spending, so an
    OSError drops the line."""
    path = os.environ.get(ENV)
    if not path:
        return
    line = {
        "ts": datetime.now(UTC).isoformat(timespec="milliseconds"),
        "source": "wiki",
        "event": event,
    } | fields
    data = (json.dumps(line, ensure_ascii=False) + "\n").encode()
    try:
        # One write on an O_APPEND descriptor, so lines from page workers do not interleave.
        fd = os.open(path, os.O_WRONLY | os.O_APPEND | os.O_CREAT, 0o644)
        try:
            os.write(fd, data)
        finally:
            os.close(fd)
    except OSError:
        pass


def counts(db: sqlite3.Connection, run: str) -> dict:
    """Finished jobs of one ledger run and their recorded spend, in the caps' units.

    Pending rows are left out: their cost and tokens are admission holds, not spend."""
    jobs, usd, codex_tokens = db.execute(
        "SELECT count(*),"
        "coalesce(sum(CASE WHEN coalesce(model,'') NOT LIKE 'gpt-%' THEN cost END),0),"
        "coalesce(sum(CASE WHEN model LIKE 'gpt-%' THEN tokens END),0) "
        "FROM jobs WHERE run=? AND status!='pending'",
        (run,),
    ).fetchone()
    return {"jobs": jobs, "usd": round(float(usd), 4), "codex_tokens": int(codex_tokens)}


def failed_pages(store: Path) -> int | None:
    """Pages failures.json holds; None when it cannot be read."""
    try:
        return len(json.loads((store / "failures.json").read_text(encoding="utf-8")))
    except FileNotFoundError:
        return 0
    except (OSError, ValueError, TypeError):
        return None


def snapshot(store: Path, run: str) -> dict:
    """`counts` and `failed_pages` read from a store without opening a Ledger, which
    would create the database and its schema. A ledger that cannot be read gives
    nulls rather than zeros."""
    totals: dict = {"jobs": 0, "usd": 0.0, "codex_tokens": 0}
    db = store / "jobs.sqlite"
    if db.exists():
        try:
            connection = sqlite3.connect(db, timeout=30)
            try:
                totals = counts(connection, run)
            finally:
                connection.close()
        except sqlite3.Error:
            totals = dict.fromkeys(totals)
    return totals | {"failed_pages": failed_pages(store)}
