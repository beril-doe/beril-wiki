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
from beril_wiki.agentic.runtime import (
    CandidateError,
    atomic_json,
    configured,
    digest,
    model_policy,
    runtime_config,
)
from beril_wiki.stages import cards
from beril_wiki.stages.gists import RETRY, last_objections


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def status_config(root: Path) -> dict:
    """Return the model config a ``--status`` count keys with, without a runtime.

    Parameters
    ----------
    root : Path
        The checkout whose ``agentic.yaml`` a default run would use.

    Returns
    -------
    dict
        The agentic run's config when one is set, else the repository's model policy.
    """
    if configured():
        return runtime_config()
    # The CLI module loads the curator and runner; only a status count needs it.
    from beril_wiki.agentic.__main__ import load_models

    return load_models(root, None, None, [])


def item_key(pack: dict, prompt_tag: str, policy: str) -> str:
    """Return the cache key of one item: its pack, the prompt tag and the model policy."""
    return digest([pack, prompt_tag, policy])


def is_current(
    prev: dict,
    pack: dict,
    prompt_tag: str,
    policy: str,
    parse: Callable[[dict], Callable[[str], BaseModel]],
) -> bool:
    """Whether a saved answer is kept: unfailed, keyed for today's pack, and still accepted."""
    if prev.get("failed") or prev.get("input") != item_key(pack, prompt_tag, policy):
        return False
    stored = {k: v for k, v in prev.items() if k not in ("input", "model", "failed")}
    try:
        parse(pack)(json.dumps(stored))
    except CandidateError:
        return False
    return True


def status(
    name: str,
    state_path: Path,
    items: dict[str, dict],
    prompt_tag: str,
    parse: Callable[[dict], Callable[[str], BaseModel]],
    policy: str,
) -> int:
    """Print how many saved answers a run would keep; touches neither the runtime nor a model.

    An answer is current when it is not failed, its key equals today's ``item_key`` and
    today's checks accept it; stale when it exists but is not current; pending when absent.

    Parameters
    ----------
    name : str
        The stage name shown in the count.
    state_path : Path
        The stage's state file.
    items : dict[str, dict]
        Item id to today's pack.
    prompt_tag : str
        The stage's prompt tag.
    parse : Callable
        ``parse(pack)`` returns the code check for one reply.
    policy : str
        The model policy the run keys with.

    Returns
    -------
    int
        1 when any item is stale, failed or pending, else 0.
    """
    state = load(state_path)
    current = stale = failed = pending = 0
    for item_id, pack in items.items():
        prev = state.get(item_id)
        if not prev:
            pending += 1
        elif prev.get("failed"):
            failed += 1
        elif is_current(prev, pack, prompt_tag, policy, parse):
            current += 1
        else:
            stale += 1
    print(
        f"{name}: {current} current, {stale} stale, {failed} failed, {pending} pending, "
        f"{len(items)} total"
    )
    return 1 if stale or failed or pending else 0


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

    todo = []
    for item_id, pack in items.items():
        prev = state.get(item_id, {})
        if is_current(prev, pack, prompt_tag, policy, parse):
            continue
        key = item_key(pack, prompt_tag, policy)
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
