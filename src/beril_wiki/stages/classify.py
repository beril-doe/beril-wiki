"""The shared loop of the one-label card stages (outcomes, followups).

Each item is a JSON pack sent with the stage's prompt. Code checks the reply, then the
reviewer role checks it against the pack (cards.reviewed). A saved label stays while its
pack, prompt and model policy are unchanged and today's checks still accept it. A refusal
or an unconverged item fails only that item; the next run asks it again with the
objections that rejected it. State is saved after every item, so a run stopped by its
budget keeps what it finished.
"""

from __future__ import annotations

import json
from collections.abc import Callable
from pathlib import Path

from pydantic import BaseModel

from beril_wiki.agentic.prose import (
    PageFailure,
    parallel,
    prune_failures,
    record_failure,
    strict_pages,
    workers,
)
from beril_wiki.agentic.runtime import CandidateError, atomic_json, digest, model_policy
from beril_wiki.stages import cards
from beril_wiki.stages.gists import RETRY, last_objections


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def status(name: str, state_path: Path, ids: list[str]) -> int:
    """Print accepted, failed and pending counts; touches neither the runtime nor state."""
    state = load(state_path)
    entries = [state.get(i) for i in ids]
    failed = sum(1 for e in entries if e and e.get("failed"))
    accepted = sum(1 for e in entries if e and not e.get("failed"))
    pending = sum(1 for e in entries if not e)
    print(f"{name}: {accepted} accepted, {failed} failed, {pending} pending, {len(ids)} total")
    return 0


def run(
    name: str,
    state_path: Path,
    items: dict[str, dict],
    prompt: str,
    prompt_tag: str,
    parse: Callable[[dict], Callable[[str], BaseModel]],
) -> int:
    """Label every item in `items` (id -> pack); `parse(pack)` code-checks one reply."""
    if not cards.require_runtime(name):
        return 0
    state = load(state_path)
    config = cards.runtime().config
    policy = cards.policy(config, ("labels", "card_review"))
    writer = model_policy(config)["labels"]

    def passes(prev: dict, pack: dict) -> bool:
        stored = {k: v for k, v in prev.items() if k not in ("input", "model", "failed")}
        try:
            parse(pack)(json.dumps(stored))
        except CandidateError:
            return False
        return True

    todo = []
    for item_id, pack in items.items():
        key = digest([pack, prompt_tag, policy])
        prev = state.get(item_id, {})
        if prev.get("input") == key and not prev.get("failed") and passes(prev, pack):
            continue
        step = f"{name}/{item_id}"
        todo.append((item_id, pack, key, last_objections(step) if prev.get("failed") else ""))

    def write(item: tuple) -> dict:
        item_id, pack, _, objections = item
        step = f"{name}/{item_id}"
        mine = cards.runtime()  # a ledger connection belongs to the thread that opened it
        sent = pack | {"LAST_ATTEMPT": objections} if objections else pack
        content = prompt + json.dumps(sent, ensure_ascii=False) + (RETRY if objections else "")
        try:
            messages = [{"role": "user", "content": content}]
            reply = cards.reviewed(messages, step, parse(pack), agent=mine)
        except CandidateError as exc:
            raise cards.failure(step, exc, mine) from exc
        return reply.model_dump()

    done = failed = 0
    for (item_id, _, key, _), result in parallel(todo, write, workers()):
        step = f"{name}/{item_id}"
        if isinstance(result, PageFailure):
            failed += 1
            record_failure(step, result)
            print(f"  [FAILED] {step}: {result}")
            state[item_id] = (state.get(item_id) or {}) | {"failed": True}
            # Saved now: a later item's budget stop would otherwise leave the old label live.
            atomic_json(state_path, dict(sorted(state.items())))
            continue
        state[item_id] = {"input": key, **result, "model": writer}
        atomic_json(state_path, dict(sorted(state.items())))
        record_failure(step, None)
        done += 1
    for item_id in [i for i in state if i not in items]:
        state.pop(item_id)
    atomic_json(state_path, dict(sorted(state.items())))
    prune_failures(f"{name}/", {f"{name}/{i}" for i in items})
    print(f"{name}: {done} written, {len(items) - len(todo)} current, {failed} failed")
    return 1 if failed and strict_pages() else 0
