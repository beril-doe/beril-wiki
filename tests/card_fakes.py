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
        self.config = {"step_models": {}, "model": "claude-sonnet-5-5"}

    def ask(self, messages, step, *, model=None):
        self.asked.append(step)
        self.jobs.append(step)
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
