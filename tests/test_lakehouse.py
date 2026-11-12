"""Lakehouse catalog: the committed state/lakehouse/ files hold known answers, keep
values only where allowed, and the build merges its three sources by rule. No LLM
calls, no network.

uv run pytest tests/test_lakehouse.py
"""

from __future__ import annotations

import gzip
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from collections.abc import Callable, Iterator
from pathlib import Path

import pytest

from beril_wiki import lakehouse as view
from beril_wiki.paths import ROOT
from beril_wiki.stages import lakehouse

CATALOG = ROOT / "state/lakehouse"
SEMCAT = ROOT / "docs/drafts/semcat-e3a8b81"

# The test's own patterns, written apart from the stage's so one mistake cannot hide in both.
EMAIL = re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)*\.[A-Za-z]{2,}")
ORCID = re.compile(r"\b\d{4}-\d{4}-\d{4}-\d{3}[0-9X]\b")
URL = re.compile(r"(?i)\b(?:https?|ftp)://|\bwww\.")
ALLOWED = {"kbase", "kescience", "nmdc", "refdata", "globalusers", "planetmicrobe"}
PERSONAL = re.compile(r"(?<![\w.])u_[a-z0-9_]+\.[a-z0-9_]")
NAME_COLUMNS = {"first_name", "last_name", "given_name", "family_name", "surname"}
NAME_COLUMN = re.compile(r"(?:^|_)(?:agent|expert|curator|maintainer|owner)s?(?:_|$)")
PEOPLE_TABLE = re.compile(r"(?:^|_)(?:users?|persons?|people|authors?|experts?|agents?)(?:_|$)")


def jsonl(path: Path) -> Iterator[dict]:
    with path.open(encoding="utf-8") as f:
        for line in f:
            yield json.loads(line)


def jsonl_gz(path: Path) -> Iterator[dict]:
    with gzip.open(path, "rt", encoding="utf-8") as f:
        for line in f:
            yield json.loads(line)


def output_texts(folder: Path) -> dict[str, str]:
    texts = {}
    for path in sorted(folder.iterdir()):
        data = path.read_bytes()
        texts[path.name] = (gzip.decompress(data) if path.suffix == ".gz" else data).decode()
    return texts


def test_known_answers():  # done check 1, as revised 2026-11-11
    rows = {(r["database"], r["table"]): r for r in jsonl(CATALOG / "catalog.jsonl")}
    values = list(jsonl_gz(CATALOG / "values.jsonl.gz"))
    cond = [
        v
        for v in values
        if (v["database"], v["table"], v["column"])
        == ("kescience.fitnessbrowser", "experiment", "condition_1")
    ]
    assert len(cond) == 1 and "Cadmium chloride hemipentahydrate" in cond[0]["values"]
    mb = rows[("arkinlab.microbeatlas", "sample_metadata")]
    assert mb["source"] == "semcat-2026-11-04" and isinstance(mb["rows"], int)
    assert not any(v["database"] == "arkinlab.microbeatlas" for v in values)
    assert any(
        r["tenant"] == "phagefoundry" and r["source"] == "atlas-2026-05" for r in rows.values()
    )
    assert not any(v["database"].startswith("enigma.") for v in values)
    # The person-name columns that once leaked, by schema name (no value is read).
    people = {
        ("planetmicrobe.planetmicrobe", "user"),
        ("planetmicrobe.planetmicrobe_raw", "user"),
        ("refdata.itis", "experts"),
    }
    assert not any((v["database"], v["table"]) in people for v in values)
    credits = ("study_set", "data_generation_set")
    agents = {("nmdc.metadata", f"{s}_has_credit_associations") for s in credits}
    assert not any(
        (v["database"], v["table"]) in agents and v["column"] == "applies_to_agent_name"
        for v in values
    )
    assert not any(r["database"].startswith("u_") or r["tenant"] in ("u",) for r in rows.values())
    cov = json.loads((CATALOG / "coverage.json").read_text())
    covered = {c["name"]: c["source"] for c in cov["covered"]}
    assert len(covered) == 23
    assert covered["arkinlab"] == covered["aimbiocm"] == "semcat-2026-11-04"
    names = {c["name"]: c["display_name"] for c in cov["covered"]}
    assert names["evaluation"] == "evaluation"
    assert not any(n.strip().lower() == "unknown" for n in names.values())
    assert not covered.keys() & {u["name"] for u in cov["uncovered"]}


@pytest.mark.skipif(not SEMCAT.exists(), reason="semcat snapshot is not committed")
def test_known_semcat_filters():
    # every non-production semcat table is absent, including the two atlas copies semcat
    # marks duplicate
    keys = {(r["database"], r["table"]) for r in jsonl(CATALOG / "catalog.jsonl")}
    production, other = set(), set()
    for r in jsonl(SEMCAT / "tables.jsonl"):
        if r["tenant"] not in lakehouse.SEMCAT_TENANTS:
            continue
        key = (f"{r['tenant']}.{r['database']}", r["table"])
        (production if r["provenance_class"] == "production" else other).add(key)
    dropped = other - production
    assert len(dropped) >= 2
    assert not keys & dropped
    assert production <= keys


def data_page_texts(tmp_path: Path) -> dict[str, str]:
    """A generated data page for every committed database, plus any built ones."""
    from beril_wiki.publish.cards.corpus import Corpus
    from beril_wiki.publish.cards.data import data_page

    c = Corpus(ROOT)
    by_database: dict[str, list[dict]] = {}
    for row in c.catalog.tables:
        by_database.setdefault(row["database"], []).append(row)
    texts = {}
    for database, rows in by_database.items():
        path = tmp_path / f"{view.slug(database)}.md"
        path.write_text(data_page(database, rows, c, "> provenance"), encoding="utf-8")
        texts[path.name] = path.read_text(encoding="utf-8")
    for path in sorted((ROOT / "quartz/public/data").glob("*.html")):
        texts[f"public/{path.name}"] = path.read_text(encoding="utf-8")
    return texts


def test_privacy_outputs_and_data_pages(tmp_path):  # done check 3
    pages = data_page_texts(tmp_path)
    assert len(pages) >= len({r["database"] for r in jsonl(CATALOG / "catalog.jsonl")})
    for name, text in pages.items():
        assert not PERSONAL.search(text), name
        assert not (EMAIL.search(text) or ORCID.search(text)), name
    texts = output_texts(CATALOG)
    assert {"catalog.jsonl", "values.jsonl.gz", "databases.jsonl"} <= texts.keys()
    for name, text in texts.items():
        assert not PERSONAL.search(text), name
    for v in jsonl_gz(CATALOG / "values.jsonl.gz"):
        assert v["database"].split(".")[0] in ALLOWED, v["database"]
        parts = re.split(r"[^a-z0-9]+", v["column"].lower())
        pairs = {f"{a}_{b}" for a, b in zip(parts, parts[1:], strict=False)}
        assert not (set(parts) | pairs) & lakehouse.REDACT_TOKENS, v["column"]
        assert v["column"].lower() not in NAME_COLUMNS, v["column"]
        assert not NAME_COLUMN.search(v["column"].lower()), v["column"]
        assert not PEOPLE_TABLE.search(v["table"].lower()), v["table"]
        for value in v["values"]:
            assert not (EMAIL.search(value) or ORCID.search(value) or URL.search(value)), (
                v["database"],
                v["table"],
                v["column"],
            )
    described = [
        *(r["description"] for r in jsonl(CATALOG / "catalog.jsonl")),
        *(r["tenant_description"] for r in jsonl(CATALOG / "databases.jsonl")),
    ]
    for text in filter(None, described):
        assert not (EMAIL.search(text) or ORCID.search(text))
    for r in jsonl(CATALOG / "catalog.jsonl"):
        assert not (r["database"].startswith("u_") or r["tenant"] == "u")


@pytest.mark.skipif(not SEMCAT.exists(), reason="semcat snapshot is not committed")
def test_privacy_no_semcat_owner(tmp_path):
    owners = {r["owner"] for r in jsonl(SEMCAT / "tables.jsonl") if r.get("owner")}
    assert owners
    pattern = re.compile(
        "|".join(
            rf"(?<![A-Za-z0-9]){re.escape(o)}(?![A-Za-z0-9])"
            for o in sorted(owners, key=len, reverse=True)
        )
    )
    texts = output_texts(CATALOG) | data_page_texts(tmp_path)
    # Only file names reach the assertion message, never an owner value.
    hits = [name for name, text in texts.items() if pattern.search(text)]
    assert hits == []


def plant_enigma(folder: Path) -> None:
    line = {
        "database": "enigma.coral",
        "table": "sdt_sample",
        "column": "site",
        "basis": "full",
        "complete": True,
        "distinct": 1,
        "values": ["x"],
    }
    rewrite_values(folder, lambda lines: [*lines, line])


def plant_email(folder: Path) -> None:
    rewrite_values(folder, lambda lines: [lines[0] | {"values": [*lines[0]["values"], "a@b.org"]}])


def plant_author(folder: Path) -> None:
    rewrite_values(folder, lambda lines: [lines[0] | {"column": "author_email"}, *lines[1:]])


def plant_personal(folder: Path) -> None:
    path = folder / "catalog.jsonl"
    first = json.loads(path.read_text().splitlines()[0])
    row = first | {"database": "u_someone.x", "legacy": "u_someone_x", "tenant": "u_someone"}
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row) + "\n")


def plant_agent_name(folder: Path) -> None:
    rewrite_values(folder, lambda lines: [*lines, lines[0] | {"column": "applies_to_agent_name"}])


def plant_people_table(folder: Path) -> None:
    rewrite_values(folder, lambda lines: [*lines, lines[0] | {"table": "user", "column": "site"}])


def plant_hostile_name(folder: Path) -> None:
    path = folder / "catalog.jsonl"
    first = json.loads(path.read_text().splitlines()[0])
    row = first | {"database": 'kescience.evil]]<img src=x onerror="alert(1)">[[x'}
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row) + "\n")


def plant_both(folder: Path) -> None:
    path = folder / "coverage.json"
    cov = json.loads(path.read_text())
    first = cov["covered"][0]
    cov["uncovered"].append(
        {"name": first["name"], "display_name": first["display_name"], "organization": None}
    )
    path.write_text(json.dumps(cov))


def rewrite_values(folder: Path, change: Callable[[list[dict]], list[dict]]) -> None:
    path = folder / "values.jsonl.gz"
    lines = change(list(jsonl_gz(path)))
    path.write_bytes(gzip.compress("".join(json.dumps(v) + "\n" for v in lines).encode()))


@pytest.mark.parametrize(
    ("plant", "named"),
    [
        (plant_enigma, "enigma.coral"),
        (plant_email, "email"),
        (plant_author, "author_email"),
        (plant_personal, "u_someone.x"),
        (plant_agent_name, "applies_to_agent_name has a redacted column name"),
        (plant_people_table, "whose name marks people"),
        (plant_hostile_name, "is not a plain identifier"),
        (plant_both, "both"),
    ],
)
def test_check_rejects_planted_violations(tmp_path, plant, named):
    folder = tmp_path / lakehouse.OUT
    shutil.copytree(CATALOG, folder)
    assert lakehouse.check(tmp_path) == []
    plant(folder)
    messages = lakehouse.check(tmp_path)
    assert any(named in m for m in messages), messages


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(r) + "\n" for r in rows), encoding="utf-8")


def packet_table(database: str, table: str, columns: list[str], rows: int | None = 5) -> dict:
    return {
        "database": database,
        "table": table,
        "comment": None,
        "row_count": rows,
        "columns": [
            {"name": c, "type": "string", "nullable": True, "comment": None} for c in columns
        ],
    }


def profile(database: str, table: str, column: str, key: str, values: list) -> dict:
    return {
        "database": database,
        "table": table,
        "column": column,
        "distinct_estimate": len(values),
        "null_fraction": 0.0,
        "basis": "full",
        key: [{"value": v, "count": len(values) - i} for i, v in enumerate(values)],
    }


def fixture_inputs(tmp_path: Path) -> lakehouse.Inputs:
    packet = tmp_path / "in/packet-20261111"
    write_jsonl(
        packet / "tables.jsonl",
        [
            packet_table("enigma.coral", "sdt_sample", ["site"]),
            packet_table("kbase.nmdc_arkin", "samples", ["id"]),
            packet_table("kbase.wide", "t", [f"c{i}" for i in range(250)], rows=None),
            packet_table(
                "kescience.fitnessbrowser",
                "experiment",
                ["condition_1", "note", "applies_to_agent_name", "full_name"],
            ),
            packet_table("kescience.fitnessbrowser", "user", ["site", "full_name"]),
        ],
    )
    write_jsonl(
        packet / "tenants.jsonl",
        [
            {"name": t, "display_name": t.upper(), "description": None}
            for t in ("enigma", "kbase", "kescience")
        ],
    )
    long_a, long_b = "a" * 70, "a" * 60 + "b" * 10
    write_jsonl(
        packet / "profiles.jsonl",
        [
            profile("enigma.coral", "sdt_sample", "site", "values", ["lake"]),
            profile(
                "kescience.fitnessbrowser",
                "experiment",
                "condition_1",
                "values",
                ["Cadmium chloride", "https://example.org/x", None],
            ),
            profile(
                "kescience.fitnessbrowser", "experiment", "note", "top_values", [long_a, long_b]
            ),
            # Synthetic stand-ins for person names, which only the column and table rules drop.
            profile(
                "kescience.fitnessbrowser",
                "experiment",
                "applies_to_agent_name",
                "values",
                ["Value A", "Value B"],
            ),
            profile("kescience.fitnessbrowser", "user", "site", "values", ["Value C"]),
            profile("kescience.fitnessbrowser", "user", "full_name", "values", ["Value D"]),
            # A full_name outside a people table names a taxon or gene, so it keeps its values.
            profile("kescience.fitnessbrowser", "experiment", "full_name", "values", ["Taxon A"]),
        ],
    )
    (packet / "manifest.json").write_text(json.dumps({"snapshot_utc": "2026-11-11T00:39:30Z"}))
    packet.with_name(packet.name + ".zip").write_bytes(b"zip")

    semcat = tmp_path / "in/semcat"
    semcat.mkdir(parents=True)
    base = {"n_columns": 2, "row_count": 10, "description": None, "description_source": None}
    write_jsonl(
        semcat / "tables.jsonl",
        [
            base
            | {"tenant": "arkinlab", "database": "microbeatlas", "table": "sample_metadata"}
            | {"provenance_class": "production", "owner": "someowner"}
            | {"description": "Samples.", "description_source": "producer"},
            base
            | {"tenant": "arkinlab", "database": "microbeatlas", "table": "scratch"}
            | {"provenance_class": "test", "owner": None},
            base
            | {"tenant": "phagefoundry", "database": "pf", "table": "copy"}
            | {"provenance_class": "duplicate", "owner": None},
        ],
    )
    columns = [
        {"tenant": "arkinlab", "database": "microbeatlas", "table": "sample_metadata"}
        | {"column": c, "type": "string", "lower": "x"}
        for c in ("sample_id", "biome")
    ]
    (semcat / "columns.jsonl.gz").write_bytes(
        gzip.compress("".join(json.dumps(c) + "\n" for c in columns).encode())
    )
    (semcat / "COMMIT").write_text("abc1234" + "0" * 33 + "\n")
    sums = "".join(
        f"{hashlib.sha256((semcat / n).read_bytes()).hexdigest()}  {n}\n"
        for n in ("tables.jsonl", "columns.jsonl.gz")
    )
    (semcat / "SHA256SUMS").write_text(sums)

    atlas = tmp_path / "in/atlas.csv"
    head = "tenant,agency,program,primary_funder,database,table,primary_topic,secondary_topics,"
    atlas.write_text(
        head
        + "n_columns,column_names,has_more_columns\n"
        + "phagefoundry,DOE,PhageFoundry,DOE,phagefoundry_pf,copy,genome,,1,a,False\n"
        + "phagefoundry,DOE,PhageFoundry,DOE,phagefoundry_pf,only_atlas,genome,,3,a|b|c,False\n"
        + "arkinlab,DOE,Arkin Lab,DOE,arkinlab_microbeatlas,sample_metadata,genome,,2,x|y,False\n"
        + "u,User,Personal,none,u_someone__db,t,genome,,1,a,False\n"
    )

    checkout = tmp_path / "in/checkout"
    (checkout / "projects/a").mkdir(parents=True)
    (checkout / "projects/a/REPORT.md").write_text(
        "We read `kescience.fitnessbrowser.experiment`.\n"
    )
    notebook = {
        "cells": [
            {
                "cell_type": "code",
                "source": ["print(1)\n"],
                "outputs": [{"output_type": "stream", "text": ["kbase.nmdc_arkin.samples\n"]}],
            }
        ]
    }
    (checkout / "projects/a/run.ipynb").write_text(json.dumps(notebook))
    (checkout / "projects/b").mkdir()
    (checkout / "projects/b/q.sql").write_text("SELECT id FROM nmdc_arkin.samples\n")
    return lakehouse.Inputs(
        packet=packet, semcat=semcat, atlas=atlas, tenants=None, checkout=checkout
    )


def test_build_merges_sources_by_rule(tmp_path):
    inputs = fixture_inputs(tmp_path)
    root = tmp_path / "repo"
    assert lakehouse.build(inputs, root) == []
    out = root / lakehouse.OUT
    rows = {(r["database"], r["table"]): r for r in jsonl(out / "catalog.jsonl")}
    assert set(rows) == {
        ("arkinlab.microbeatlas", "sample_metadata"),
        ("enigma.coral", "sdt_sample"),
        ("kbase.nmdc_arkin", "samples"),
        ("kbase.wide", "t"),
        ("kescience.fitnessbrowser", "experiment"),
        ("kescience.fitnessbrowser", "user"),
        ("phagefoundry.pf", "only_atlas"),
    }
    sm = rows[("arkinlab.microbeatlas", "sample_metadata")]
    assert sm["source"] == "semcat-2026-11-04" and sm["description"] == "Samples."
    assert sm["columns"] == [["sample_id", "string"], ["biome", "string"]]
    only = rows[("phagefoundry.pf", "only_atlas")]
    assert only["rows"] is None and only["source"] == "atlas-2026-05"
    assert only["columns"] == [["a", ""], ["b", ""], ["c", ""]]
    wide = rows[("kbase.wide", "t")]
    assert wide["column_count"] == 250 and len(wide["columns"]) == 200
    assert wide["columns_truncated"] is True
    assert rows[("kbase.nmdc_arkin", "samples")]["legacy"] == "nmdc_arkin"

    values = {(v["table"], v["column"]): v for v in jsonl_gz(out / "values.jsonl.gz")}
    assert set(values) == {
        ("experiment", "condition_1"),
        ("experiment", "note"),
        ("experiment", "full_name"),
    }
    assert values[("experiment", "full_name")]["values"] == ["Taxon A"]
    assert ("user", "full_name") not in values
    cond = values[("experiment", "condition_1")]
    assert cond["values"] == ["Cadmium chloride"] and cond["complete"] is False
    assert values[("experiment", "note")]["values"] == ["a" * 60]

    texts = output_texts(out)
    assert not any("someowner" in t or "u_someone" in t for t in texts.values())
    dbs = {d["database"]: d for d in jsonl(out / "databases.jsonl")}
    assert dbs["phagefoundry.pf"]["tenant_name"] == "PhageFoundry"
    assert dbs["kbase.wide"]["rows"] is None
    usage = json.loads((out / "usage.json").read_text())
    assert usage == {
        "a": {
            "databases": ["kescience.fitnessbrowser"],
            "tables": ["kescience.fitnessbrowser.experiment"],
        },
        "b": {"databases": ["kbase.nmdc_arkin"], "tables": ["kbase.nmdc_arkin.samples"]},
    }
    cov = json.loads((out / "coverage.json").read_text())
    assert [c["name"] for c in cov["covered"]] == [
        "arkinlab",
        "enigma",
        "kbase",
        "kescience",
        "phagefoundry",
    ]
    assert cov["listing"] == "none" and cov["uncovered"] == []

    first = {p.name: p.read_bytes() for p in out.iterdir()}
    assert lakehouse.build(inputs, root) == []
    assert {p.name: p.read_bytes() for p in out.iterdir()} == first

    # A tenant listing without a usable date fails the build instead of storing "None".
    listing = tmp_path / "in/tenants/tenants_all.jsonl"
    write_jsonl(listing, [{"name": "other", "display_name": "Other"}])
    for meta in ({"snapshot_utc": None}, {}):
        (listing.parent / "tenants_all.manifest.json").write_text(json.dumps(meta))
        with pytest.raises(ValueError, match="snapshot_utc"):
            lakehouse.build(inputs.model_copy(update={"tenants": listing}), root)
        assert {p.name: p.read_bytes() for p in out.iterdir()} == first

    # A refresh that fails the check leaves the accepted generation in place.
    semcat_rows = list(jsonl(inputs.semcat / "tables.jsonl"))
    semcat_rows[0]["description"] = "Samples curated by someowner."
    write_jsonl(inputs.semcat / "tables.jsonl", semcat_rows)
    (inputs.semcat / "SHA256SUMS").write_text(
        "".join(
            f"{hashlib.sha256((inputs.semcat / n).read_bytes()).hexdigest()}  {n}\n"
            for n in ("tables.jsonl", "columns.jsonl.gz")
        )
    )
    assert lakehouse.build(inputs, root) == ["catalog.jsonl: holds a semcat owner value"]
    assert {p.name: p.read_bytes() for p in out.iterdir()} == first
    assert sorted(p.name for p in out.parent.iterdir()) == ["lakehouse"]


DIRECTORY_MAX_CHARS = 40_000  # about 10K tokens


def test_view_names_routes_and_ranking():
    cat = view.load(ROOT)
    for name in (
        "KEScience.FitnessBrowser.Experiment",
        "kescience_fitnessbrowser.experiment",
        "`kescience.fitnessbrowser.experiment`",
        "'kescience.fitnessbrowser.experiment'.",
    ):
        assert cat.canonical(name) == "kescience.fitnessbrowser.experiment"
    assert cat.exists("kescience.fitnessbrowser.no_such_table") is None
    # A stored name with capitals is found in any case and named as stored.
    mixed = "refdata.gbif_backbone.TypesAndSpecimen"
    for name in (mixed, mixed.lower(), "`refdata_gbif_backbone.TYPESANDSPECIMEN`"):
        assert cat.canonical(name) == mixed
    assert cat.matched("unrelated words", [], 1, [mixed.lower()])[0]["table"] == mixed
    database = cat.exists("kescience_fitnessbrowser")
    assert database is not None and "table" not in database
    assert cat.route("kbase.uniref90") == "data/kbase-uniref"
    assert cat.route("phagefoundry_acinetobacter_genome_browser") == "data/phagefoundry"
    assert cat.route("protect_genomedepot") == "data/protect-genomedepot"
    assert cat.route("kescience.fitnessbrowser") == "data/kescience-fitnessbrowser"
    assert cat.route("kescience.bacdive") == "data/kescience-bacdive"
    assert not cat.curated("kescience.bacdive")
    assert len(cat.directory()) < DIRECTORY_MAX_CHARS
    assert "Other tenants exist" in cat.directory().splitlines()[0]
    usage = json.loads((CATALOG / "usage.json").read_text())
    pid = next(p for p, u in usage.items() if "kescience.fitnessbrowser.experiment" in u["tables"])
    assert cat.matched("unrelated words", [pid], 40)[0]["table"] in usage[pid]["tables"]
    assert all(len(t["values"]) <= 20 for t in cat.matched("cadmium nitrate stress", [], 40))


def test_view_is_hash_seed_independent():
    script = (
        "from beril_wiki import lakehouse; from beril_wiki.paths import ROOT; "
        "c = lakehouse.load(ROOT); print(c.directory()); "
        "print(c.matched('cadmium nitrate stress', [], 20))"
    )
    outs = set()
    for seed in ("1", "2", "3"):
        done = subprocess.run(
            [sys.executable, "-c", script],
            capture_output=True,
            text=True,
            check=True,
            env={**os.environ, "PYTHONHASHSEED": seed},
        )
        outs.add(done.stdout)
    assert len(outs) == 1
