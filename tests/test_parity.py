"""The parity reference predates the single wiki tree; copying it must keep
both its catalog and its home page, at the paths the compiler now uses."""

import pathlib

from beril_wiki.parity import copy_reference


def _reference(root: pathlib.Path, two_trees: bool) -> pathlib.Path:
    ref = root / "ref"
    (ref / "wiki" / "concepts").mkdir(parents=True)
    (ref / "wiki" / "index.md").write_text("# Knowledge Base Index\n")
    (ref / "wiki" / "concepts" / "a.md").write_text("# A\n")
    if two_trees:
        (ref / "wiki-extra" / "topics").mkdir(parents=True)
        (ref / "wiki-extra" / "index.md").write_text("# Home\n")
        (ref / "wiki-extra" / "topics" / "t.md").write_text("# T\n")
    return ref


def test_two_tree_reference_keeps_catalog_and_home(tmp_path: pathlib.Path) -> None:
    copy_reference(_reference(tmp_path, two_trees=True), tmp_path / "out")
    wiki = tmp_path / "out" / "wiki"
    assert (wiki / "catalog.md").read_text() == "# Knowledge Base Index\n"
    assert (wiki / "index.md").read_text() == "# Home\n"
    assert (wiki / "topics" / "t.md").exists() and (wiki / "concepts" / "a.md").exists()


def test_single_tree_reference_is_copied_as_is(tmp_path: pathlib.Path) -> None:
    ref = _reference(tmp_path, two_trees=False)
    (ref / "wiki" / "index.md").rename(ref / "wiki" / "catalog.md")
    (ref / "wiki" / "index.md").write_text("# Home\n")
    copy_reference(ref, tmp_path / "out")
    wiki = tmp_path / "out" / "wiki"
    assert (wiki / "catalog.md").read_text() == "# Knowledge Base Index\n"
    assert (wiki / "index.md").read_text() == "# Home\n"
