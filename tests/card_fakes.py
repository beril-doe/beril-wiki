"""A scripted runtime for the card stages: replies by step, a reviewer that can object."""

import json

from beril_wiki.agentic.runtime import CandidateError, file_hash


class FakeAgent:
    def __init__(
        self, store, replies, objections=None, still_open=None, review_error=None, verify_error=None
    ):
        self.store = store
        self.review_error = dict(review_error or {})
        self.verify_error = dict(verify_error or {})
        self.still_open = dict(still_open or {})
        self.replies = {k: list(v) for k, v in replies.items()}
        self.objections = dict(objections or {})
        self.jobs: list[str] = []
        self.asked: list[str] = []
        self.sent: dict[str, str] = {}  # step -> the last prompt text it was asked
        self.config = {"step_models": {}, "model": "claude-sonnet-5-5"}

    def ask(self, messages, step, *, model=None):
        self.asked.append(step)
        self.jobs.append(step)
        self.sent[step] = messages[-1]["content"]
        queue = self.replies.get(step)
        if not queue:
            raise AssertionError(f"no recorded reply for {step}")
        return queue.pop(0)

    def generate(self, messages, step, accept, *, attempts=2, **_):
        for attempt in range(attempts):
            raw = self.ask(messages, step if attempt == 0 else step + "/repair")
            try:
                return accept(raw)
            except CandidateError:
                if attempt == attempts - 1:
                    raise
        raise AssertionError("unreachable")

    def review(self, messages, candidate, step):
        self.asked.append(step + "/science-review")
        if error := self.review_error.get(step):
            raise error
        if issues := self.objections.pop(step, None):
            raise CandidateError(f"rejected {step}", issues)

    def verify(self, messages, candidate, issues, step):
        self.asked.append(step + "/verify")
        if error := self.verify_error.get(step):
            raise error
        return list(self.still_open.get(step, []))


def install(monkeypatch, agent):
    from beril_wiki.stages import cards

    monkeypatch.setattr(cards, "configured", lambda: True)
    monkeypatch.setattr(cards, "runtime", lambda: agent)


def report(root, sid, text):
    path = root / "wiki/sources" / f"{sid}__REPORT.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)
    return path


def evidence(store, root, sid, records, name="blob.json"):
    path = store / "evidence" / name
    path.parent.mkdir(parents=True, exist_ok=True)
    sha = file_hash(root / "wiki/sources" / f"{sid}__REPORT.md")
    path.write_text(
        json.dumps(
            {
                "coverage": [{"source": f"{sid}__REPORT.md", "sha256": sha}],
                "findings": [r | {"source": sid} for r in records],
            }
        )
    )


def scope(root, reports=(), topics=()):
    (root / "contract").mkdir(parents=True, exist_ok=True)
    (root / "contract/cards.yaml").write_text(
        json.dumps({"topics": list(topics), "reports": list(reports)})
    )


def lakehouse(root, extra=()):
    """Write a small catalog under ``root/state/lakehouse`` in the shapes the stage builds."""
    import gzip

    def row(database, table, source, rows, columns, description=None):
        return {
            "database": database,
            "legacy": database.replace(".", "_", 1),
            "tenant": database.split(".")[0],
            "table": table,
            "rows": rows,
            "column_count": len(columns),
            "columns": columns,
            "columns_truncated": False,
            "source": source,
            "description": description,
        }

    packet = "packet-2026-11-11"
    tables = [
        row(
            "kescience.fitnessbrowser",
            "experiment",
            packet,
            7552,
            [["expname", "string"], ["condition_1", "string"], ["media", "string"]],
        ),
        row("kbase.ke_pangenome", "genome", packet, 293059, [["genome_id", "string"]]),
        row("kescience.bacdive", "strain", packet, 97334, [["strain_id", "string"]]),
        row(
            "phagefoundry.acinetobacter_genome_browser",
            "browser_gene",
            "atlas-2026-05",
            None,
            [],
        ),
        *extra,
    ]
    tables.sort(key=lambda r: (r["database"], r["table"]))
    names = {"kescience": "KE Science", "kbase": "KBase", "phagefoundry": "PhageFoundry"}
    databases = []
    for database in sorted({t["database"] for t in tables}):
        mine = [t for t in tables if t["database"] == database]
        tenant = database.split(".")[0]
        unknown = any(t["rows"] is None for t in mine)
        databases.append(
            {
                "database": database,
                "legacy": database.replace(".", "_", 1),
                "tenant": tenant,
                "tenant_name": names.get(tenant, tenant),
                "tenant_description": None,
                "tables": len(mine),
                "rows": None if unknown else sum(t["rows"] for t in mine),
                "source": mine[0]["source"],
            }
        )
    folder = root / "state/lakehouse"
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "catalog.jsonl").write_text("".join(json.dumps(t) + "\n" for t in tables))
    (folder / "databases.jsonl").write_text("".join(json.dumps(d) + "\n" for d in databases))
    profile = {
        "database": "kescience.fitnessbrowser",
        "table": "experiment",
        "column": "condition_1",
        "basis": "full",
        "complete": True,
        "distinct": 3,
        "values": ["cadmium chloride", "nitrate", "glucose"],
    }
    with gzip.open(folder / "values.jsonl.gz", "wt", encoding="utf-8") as f:
        f.write(json.dumps(profile) + "\n")
    usage = {
        "a": {
            "databases": ["kescience.fitnessbrowser"],
            "tables": ["kescience.fitnessbrowser.experiment"],
        }
    }
    (folder / "usage.json").write_text(json.dumps(usage))
    covered = [
        {"name": "kbase", "display_name": "KBase", "source": packet, "date": "2026-11-11"},
        {"name": "kescience", "display_name": "KE Science", "source": packet, "date": "2026-11-11"},
    ]
    coverage = {"covered": covered, "uncovered": [], "listing_date": None, "listing": "none"}
    (folder / "coverage.json").write_text(json.dumps(coverage))
    (folder / "manifest.json").write_text(json.dumps({"snapshot_utc": "2026-11-11T00:39:30Z"}))
