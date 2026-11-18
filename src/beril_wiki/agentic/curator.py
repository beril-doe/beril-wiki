"""Fixed editorial schedule over the existing, validated domain operations."""

from __future__ import annotations

import ast
import json
import re
from collections.abc import Callable
from pathlib import Path

from beril_wiki.agentic.batch import compile_batch
from beril_wiki.agentic.runtime import (
    Runtime,
    WorkflowError,
    contract_manifest,
    digest,
    manifest,
)
from beril_wiki.agentic.topics import load_groups, propose_topics
from beril_wiki.stages.literature import SECTION, topic_core
from beril_wiki.stages.novelty import labels_due

# Action dependencies and owned outputs are host policy; the table order is the schedule.
EDITORIAL = {
    "conflicts": (("wiki/concepts", "wiki/sources", "staging"), ("wiki/conflicts",), (), None),
    "topics": (
        (
            "wiki/concepts",
            "wiki/entities",
            "wiki/conflicts",
            "wiki/summaries",
            "state/curator-topics.json",
        ),
        ("wiki/topics", "wiki/index.md"),
        ("conflicts",),
        "topics-state.json",
    ),
    "literature": (("wiki/topics", "staging"), ("wiki/topics",), ("topics",), "litcontext.json"),
    "authors": (("wiki/summaries", "wiki/concepts"), ("wiki/authors",), (), "authors.json"),
    # Findings, literature labels and research directions: each stage writes only its
    # own outputs, so the pages Topics and Literature fingerprint are never touched.
    # Placement is at publish.
    "headlines": (
        ("wiki/sources", "contract/cards.yaml"),
        ("wiki/findings",),
        (),
        # Not disposable: the run that wrote the records may have used another job
        # store, so clearing would buy every report again. The stage re-checks saved
        # replies against today's code instead.
        None,
    ),
    "novelty": (
        ("wiki/findings", "wiki/sources", "contract/novelty-decisions.yaml"),
        ("state/novelty.json",),
        ("headlines",),
        # No disposable cache: state/novelty.json is the published labels, and a
        # label whose retrieval later fails must keep its previous value and date.
        None,
    ),
    "directions": (
        (
            "wiki/findings",
            "state/novelty.json",
            "wiki/concepts",
            "wiki/conflicts",
            "wiki/sources",
            "state/lakehouse",
            "contract/cards.yaml",
            "state/curator-topics.json",
        ),
        ("wiki/directions",),
        ("conflicts", "topics", "headlines", "novelty"),
        # Not disposable: each topic's draft reads the other topics' accepted replies, so
        # clearing them would change the drafts' text and buy them again. The stage
        # re-checks saved replies against today's code instead.
        None,
    ),
    # Plain summaries of findings; published state like novelty, never cleared.
    "gists": (
        ("wiki/findings", "wiki/summaries"),
        ("state/gists.json",),
        ("headlines",),
        None,
    ),
    # Links between projects; per-candidate answers live in the state, never cleared.
    "links": (
        ("wiki/findings", "wiki/sources", "wiki/concepts", "wiki/conflicts"),
        ("state/links.json",),
        ("headlines",),
        None,
    ),
    # Statements for results several projects reached, built on the related-result links.
    "shared": (
        (
            "state/links.json",
            "wiki/findings",
            "wiki/summaries",
            "wiki/concepts",
            "state/curator-topics.json",
        ),
        ("state/shared.json",),
        ("links",),
        None,
    ),
    # The kind of each listed result (positive, negative ...): the Results map's marks.
    "outcomes": (
        ("wiki/findings", "state/gists.json"),
        ("state/outcomes.json",),
        ("gists",),
        None,
    ),
    # What following up each open question needs: the Open questions map's columns.
    "followups": (
        ("wiki/directions", "state/lakehouse"),
        ("state/followups.json",),
        ("directions",),
        None,
    ),
}
# Stages that apply the shared card modules. Only they hash CARD_FILES, so a change to
# one of those modules reschedules every card stage and no other stage.
CARD_STAGES = (
    "headlines",
    "novelty",
    "directions",
    "gists",
    "links",
    "shared",
    "outcomes",
    "followups",
)
CARD_FILES = ("stages/cards.py", "records.py", "wording.py")
# The one-label stages share stages/classify.py's loop and gists' retry helpers.
LABEL_STAGES = ("outcomes", "followups")
# Stages that read the lakehouse catalog view. Only they hash lakehouse.py: through
# CARD_FILES a change to it would reschedule all eight card stages.
CATALOG_STAGES = ("directions", "followups")
# Fail immediately if a future table edit would make freshness propagation order-dependent.
for index, (action, (_, _, dependencies, _)) in enumerate(EDITORIAL.items()):
    if not set(dependencies) <= set(list(EDITORIAL)[:index]):
        raise RuntimeError(f"editorial dependencies must precede {action}")


def topic_part(text: str, literature: bool = False) -> str:
    """Separate ownership without making inserted section whitespace an input change."""
    return (
        re.sub(r"\s+", " ", "\n".join(SECTION.findall(text))).strip()
        if literature
        else topic_core(text)
    )


def owned_manifest(root: Path, folders: tuple, *, part: str = "") -> dict[str, str]:
    result = manifest(root, folders)
    if part:
        for path in result:
            if path.startswith("wiki/topics/") and path.endswith(".md"):
                result[path] = digest(
                    topic_part((root / path).read_text(encoding="utf-8"), part == "literature")
                )
    return result


# What each derived stage means, as an explicit revision: bump one when a change to the
# stage, its prompts or the shared prose machinery should rewrite that stage's pages.
# Hashing the model policy and the source code made a cheaper model, or any edit to
# prose.py, rewrite every derived page of the accepted wiki.
STAGE_REVISIONS = {
    "conflicts": "conflicts@1",
    "topics": "topics@1",
    "literature": "literature@1",
    "authors": "authors@1",
    "figures": "figures@1",
    "headlines": "headlines@1",
    "novelty": "novelty@1",
    "directions": "directions@2",
    "gists": "gists@1",
    "links": "links@1",
    "shared": "shared@1",
    "outcomes": "outcomes@1",
    "followups": "followups@2",
}


def stage_revision(root: Path, name: str) -> str:
    """A card stage also hashes the card modules it applies: rerunning one re-checks its
    saved records against today's code without model calls, since a record's key holds
    its models and prompt, not the stage's source."""
    package = Path(__file__).resolve().parents[1]
    files: tuple[str, ...] = ()
    if name in CARD_STAGES:
        files = (f"stages/{name}.py", *CARD_FILES)
    if name in LABEL_STAGES:
        files += ("stages/classify.py", "stages/gists.py")
    if name in CATALOG_STAGES:
        files += ("lakehouse.py",)
    return digest(
        [
            STAGE_REVISIONS[name],
            contract_manifest(root),
            *[ast.dump(ast.parse((package / file).read_text(encoding="utf-8"))) for file in files],
        ]
    )


def stage_snapshot(root: Path, name: str) -> dict:
    inputs, outputs, _, _ = EDITORIAL[name]
    # Labels age without any input changing; an expired one makes the stage stale.
    due = {"due": True} if name == "novelty" and labels_due(root) else {}
    return due | {
        "semantic": stage_revision(root, name),
        "inputs": digest(owned_manifest(root, inputs, part="core")),
        "outputs": owned_manifest(
            root, outputs, part="literature" if name == "literature" else "core"
        ),
    }


def pending_actions(
    root: Path, state: dict, *, integrated: bool, attempted: frozenset = frozenset()
) -> list[str]:
    """`attempted`: stages this curator run already ran. An expired label whose refresh
    failed stays due for the next run, but must not hold this run's promotion."""
    pending = [] if integrated else ["integrate"]
    for name, (_, _, dependencies, _) in EDITORIAL.items():
        if (
            not integrated
            or any(d in pending for d in dependencies)
            or state.get(name) != stage_snapshot(root, name)
            # A failed refresh is accepted with the label still expired; retry each run.
            or (name == "novelty" and name not in attempted and labels_due(root))
        ):
            pending.append(name)
    try:
        load_groups(root)
    except WorkflowError:
        for name in ("topics", "literature"):
            if name not in pending:
                pending.append(name)
    return pending


def invalidate_outputs(root: Path, name: str, before: dict, now: dict) -> list[str]:
    """Invalidate only edited outputs; a scientific configuration change clears its cache."""
    semantic_changed = not before or before.get("semantic") != now["semantic"]
    old = before.get("outputs", {})
    changed = {
        path
        for path in old.keys() | now["outputs"].keys()
        if old.get(path) != now["outputs"].get(path)
    }
    if name == "conflicts":
        for path in (root / "wiki/conflicts").glob("*.md"):
            if semantic_changed or path.relative_to(root).as_posix() in changed:
                path.write_text(
                    re.sub(
                        r"^<!-- tension-hash: \w+ -->\n?",
                        "",
                        path.read_text(encoding="utf-8"),
                        flags=re.M,
                    ),
                    encoding="utf-8",
                )
        return []
    cache_name = EDITORIAL[name][3]
    if cache_name is None:
        return []
    cache_path = root / "state" / cache_name
    if cache_path.exists():
        cache = json.loads(cache_path.read_text(encoding="utf-8"))
        if semantic_changed:
            cache = {k: v for k, v in cache.items() if k == "__names__"}
        else:
            for path in changed:
                cache.pop(Path(path).stem if name == "topics" else Path(path).name, None)
        cache_path.write_text(json.dumps(cache, sort_keys=True), encoding="utf-8")
    return (
        ["--refresh-home"]
        if name == "topics" and (semantic_changed or "wiki/index.md" in changed)
        else []
    )


def curate(
    root: Path,
    agent: Runtime,
    changed: list[str],
    refresh: Callable[[str, list[str]], None],
    prior: dict,
    retry: list[str] | None = None,
) -> dict:
    """Run integration, then each editorial stage whose fingerprint is stale, in table order.

    With no changed source, pages a run left failed are re-drafted from the saved plan."""
    state = dict(prior)
    receipts: list[dict] = []
    ran: set[str] = set()
    refresh("extras", [])
    refresh("names-core", [str(root)])
    # Freshness is judged when each stage is reached: integration can make a stage
    # stale that was current before it ran (authors reads summaries, for instance).
    for action in (["integrate"] if changed or retry else []) + list(EDITORIAL):
        if action != "integrate" and action not in pending_actions(
            root, state, integrated=True, attempted=frozenset(ran)
        ):
            continue
        receipt: dict = {"action": action, "result": "failed"}
        before = manifest(root, ("wiki", "state"))
        try:
            if action == "integrate":
                if changed:
                    compile_batch(root, agent, changed)
                else:
                    compile_batch(root, agent, [], retry=retry)
                refresh("entities", ["--apply"])
                refresh("names-core", [str(root)])
                refresh("extras", [])
            else:
                previous = state.get(action, {})
                now = stage_snapshot(root, action)
                args = invalidate_outputs(root, action, previous, now)
                if action == "topics":
                    propose_topics(root, agent)
                refresh(action, args)
                ran.add(action)
                state[action] = stage_snapshot(root, action)
            after = manifest(root, ("wiki", "state"))
            paths = sorted(p for p in before.keys() | after.keys() if before.get(p) != after.get(p))
            receipt.update(result="completed", changed_paths=paths, changed_count=len(paths))
        except (WorkflowError, OSError, ValueError) as exc:
            receipt["diagnostic"] = str(exc)[:4000]
            raise
        finally:
            receipt["pending"] = pending_actions(
                root, state, integrated=True, attempted=frozenset(ran)
            )
            receipts.append(receipt)
            (agent.store / "curator-receipts.json").write_text(
                json.dumps(receipts, indent=2, sort_keys=True), encoding="utf-8"
            )
    if pending := pending_actions(root, state, integrated=True, attempted=frozenset(ran)):
        raise WorkflowError(f"editorial obligations remain after scheduling: {pending}")
    return state
