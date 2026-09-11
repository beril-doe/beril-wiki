"""Entity dedup must resolve identity, never similarity.

The failure this guards against is specific and documented: over entity pages
embeddings rank `aciad2176` and `aciad3137` — two different genes — at 0.971,
and numeric overlap scores `cyanobacteriia` against `photosystem-ii` at 1.00.
So the tests below are mostly about what must NOT merge.
"""

import pathlib
import tempfile

from beril_wiki.stages.entities import duplicate_pairs, identifiers, load, normalise


def test_normalise_folds_spelling_not_meaning():
    assert normalise("egg-nog") == normalise("eggNOG") == normalise("Egg NOG")
    assert normalise("prophages") == normalise("prophage")  # plural
    assert normalise("aciad2176") != normalise("aciad3137")  # different genes
    assert normalise("cyanobacteriia") != normalise("photosystem-ii")


def _page(d, stem, title, type_="Dataset", body=""):
    (d / f"{stem}.md").write_text(
        f'---\ntype: "{type_}"\nsources: ["summaries/a__REPORT.md"]\n---\n'
        f"# {title}\n\n{body}\nClaim. [src: a]\n"
    )


def _pairs(**pages):
    d = pathlib.Path(tempfile.mkdtemp())
    (d / "wiki" / "entities").mkdir(parents=True)
    for stem, kw in pages.items():
        _page(d / "wiki" / "entities", stem, **kw)
    return {
        (min(a["stem"], b["stem"]), max(a["stem"], b["stem"]), sig.split()[0])
        for sig, a, b in duplicate_pairs(load(d))
    }


def test_matches_on_normalised_name():
    assert ("egg-nog", "eggnog", "name") in _pairs(
        **{"egg-nog": dict(title="eggNOG"), "eggnog": dict(title="eggNOG")}
    )


def test_matches_on_a_declared_alias():
    got = _pairs(
        **{
            "e-coli": dict(
                title="E. coli", body="## Identity\n\nKnown aliases include Escherichia coli."
            ),
            "escherichia-coli": dict(title="Escherichia coli", body="## Identity\n\n"),
        }
    )
    assert ("e-coli", "escherichia-coli", "alias") in got, got


def test_different_types_never_merge():
    assert (
        _pairs(
            **{
                "copper": dict(title="Copper", type_="Compound"),
                "copper-org": dict(title="Copper", type_="Organism"),
            }
        )
        == set()
    )


def test_two_genes_of_one_organism_do_not_merge():
    """The exact pair embeddings rank at 0.971."""
    assert (
        _pairs(
            **{
                "aciad2176": dict(title="ACIAD2176", type_="Gene_Or_Pathway"),
                "aciad3137": dict(title="ACIAD3137", type_="Gene_Or_Pathway"),
            }
        )
        == set()
    )


def test_a_mentioned_accession_is_not_an_identifier():
    """PF13455 discussed in prose belonged to neither page; reading the whole
    page proposed merging klebsiella with methanococcus-maripaludis."""
    body = "## Identity\n\nNo external identifier.\n\n## Facts\n\nCarries PF13455. [src: a]\n"
    assert identifiers(body) == set()
    assert (
        _pairs(
            **{
                "klebsiella": dict(title="Klebsiella", type_="Organism", body=body),
                "methanococcus": dict(title="Methanococcus", type_="Organism", body=body),
            }
        )
        == set()
    )


def test_an_identifier_in_the_identity_section_does_match():
    body = "## Identity\n\nStable external identifier: CHEBI:29036.\n"
    got = _pairs(
        **{
            "copper": dict(title="Copper", type_="Compound", body=body),
            "cu-ion": dict(title="Cu ion", type_="Compound", body=body),
        }
    )
    assert ("copper", "cu-ion", "identifier") in got, got
