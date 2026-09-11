"""Write quartz/quartz.config.yaml for the BERIL site.

Derived from Quartz's shipped default on every build, so a change here always
takes effect and nothing under the gitignored quartz/ clone is edited by hand.
Palette and type follow theme/styles, which aliases Quartz's variables onto its
own tokens; keep the two in step.

    uv run python -m beril_wiki.publish.quartz_config <quartz-dir> <base-url>
"""

from __future__ import annotations

import os
import pathlib
import sys

import yaml


def main(qp: pathlib.Path, base_url: str) -> None:
    cfg = yaml.safe_load((qp / "quartz.config.default.yaml").read_text())
    c = cfg["configuration"]
    c["pageTitle"] = "BERIL Knowledge Wiki"
    c["baseUrl"] = base_url
    c["analytics"] = None
    # One superfamily in three roles: the serif carries display and reading prose
    # (its italic is what species names are set in), the sans carries the
    # interface, the mono carries identifiers and counts. Spell the weights out --
    # asking Google Fonts for a weight a family does not ship fails the whole
    # stylesheet request, which is how the site loses all three at once.
    TYPOGRAPHY = {
        "header": {"name": "IBM Plex Serif", "weights": [400, 500, 600], "includeItalic": True},
        "body": {"name": "IBM Plex Sans", "weights": [400, 500, 600], "includeItalic": True},
        "code": {"name": "IBM Plex Mono", "weights": [400, 500], "includeItalic": False},
    }
    c["theme"]["typography"] = TYPOGRAPHY
    c["theme"]["colors"]["lightMode"] = {
        "light": "#fafaf7",  # page background
        "lightgray": "#dde1e4",  # rules
        "gray": "#737b83",  # muted text
        "darkgray": "#4a5158",  # secondary text
        "dark": "#1e2226",  # ink
        "secondary": "#2c63c7",  # links
        "tertiary": "#1f4fa8",  # link hover
        "highlight": "rgba(44, 99, 199, 0.08)",
        "textHighlight": "rgba(176, 122, 18, 0.3)",
    }
    # Dark mode is a warm neutral rather than a blue-black, so the two themes read
    # as one site, and the surfaces are far enough apart to be seen: the page and
    # the cards used to sit four percent apart with rules darker than both.
    c["theme"]["colors"]["darkMode"] = {
        "light": "#17181a",  # page background
        "lightgray": "#2f3235",  # rules, lighter than the surfaces they divide
        "gray": "#8f8b84",  # muted text
        "darkgray": "#b8b4ac",  # secondary text
        "dark": "#e6e3dd",  # ink, off pure white for long reading
        "secondary": "#86aaf5",  # links
        "tertiary": "#a8c3fa",  # link hover
        "highlight": "rgba(134, 170, 245, 0.12)",
        "textHighlight": "rgba(226, 169, 74, 0.3)",
    }
    # The frame renders its own title, navigation, neighbours and backlinks, so
    # the stock components for those are switched off rather than hidden.
    FRAME_REPLACES = {
        "explorer",
        "graph",
        "backlinks",
        "article-title",
        "content-meta",
        "tag-list",
        "page-title",
        "reader-mode",
        "breadcrumbs",
        "spacer",
    }
    # Footer is on every page by construction, so it carries the things a reader
    # needs from anywhere: what this is, how to cite it, its licence, and where the
    # reports come from. No link to the BERIL Atlas: this wiki is intended to take
    # its place, so sending readers there is the wrong direction of travel.
    for p in cfg["plugins"]:
        name = p["source"].removeprefix("@quartz-community/")
        if name in FRAME_REPLACES:
            p["enabled"] = False
        # Search and the theme toggle sit in the frame's top bar (the header slot),
        # not in the default toolbar group of the left sidebar.
        if name in ("search", "darkmode"):
            p["layout"] = {"position": "header", "priority": 10 if name == "search" else 20}
        # CNAME is only for a per-repo custom domain. The org already serves Pages
        # from the verified domain beril-doe.org, so this project site is routed to
        # beril-doe.org/beril-wiki without a CNAME file; writing one derived from
        # baseUrl's host would instead claim the bare domain for this repo. Emit one
        # only when a per-repo domain is explicitly asked for.
        # The fonts plugin emits its own --headerFont/--bodyFont after the theme
        # block and falls back to Quartz's stock faces unless told otherwise.
        if name == "quartz-fonts":
            p["options"] = {"useThemeFonts": False, **TYPOGRAPHY}
        if name == "cname":
            p["enabled"] = bool(os.environ.get("WIKI_CNAME"))
        # Frontmatter here is machinery — type, description, the sources list that
        # keeps citations honest. Rendered as a properties table above every page
        # it reads as debug output, and the description just restates the opening
        # paragraph. Hide the table, do NOT disable the plugin: it is also Quartz's
        # frontmatter parser, so switching it off leaves every page "Untitled".
        if name == "note-properties":
            p["options"]["hidePropertiesView"] = True
        # No page in this corpus declares tags. Every "tag" Quartz finds is Obsidian
        # syntax matching ordinary prose in the raw reports -- "the #1-ranked gene
        # AO356_11255" produced a published /tags/1-ranked page. Turning the tag
        # routes off removes a taxonomy the corpus never claimed.
        if name == "tag-page":
            p["enabled"] = False
        if name == "footer":
            p["options"]["links"] = {
                "About & how to cite": "https://" + base_url.rstrip("/") + "/about",
                "BERIL Observatory": "https://beril.kbase.us/",
                "Source": "https://github.com/beril-doe/beril-wiki",
                "AGPL-3.0": "https://www.gnu.org/licenses/agpl-3.0.html",
            }
    # The theme plugin: a path relative to the quartz/ directory, where the build
    # runs. It contributes the "beril" page frame used for content and folder pages.
    cfg["plugins"].append({"source": "../theme", "enabled": True})
    for page_type in ("content", "folder"):
        cfg["layout"]["byPageType"].setdefault(page_type, {})["template"] = "beril"
    (qp / "quartz.config.yaml").write_text(yaml.safe_dump(cfg, sort_keys=False, allow_unicode=True))


if __name__ == "__main__":
    main(pathlib.Path(sys.argv[1]), sys.argv[2])
