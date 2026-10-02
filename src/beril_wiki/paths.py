"""Where the repository keeps things. Every stage resolves paths from here.

ROOT is the checkout that contains this package; it is derived from the file
location because the pipeline is run from an editable install (``uv sync``).
"""

from __future__ import annotations

import os
import pathlib

ROOT = pathlib.Path(
    os.environ.get("BERIL_WIKI_ROOT", pathlib.Path(__file__).resolve().parents[2])
).resolve()
WIKI = ROOT / "wiki"
STATE = ROOT / "state"
STAGING = ROOT / "staging"
CONTRACT = ROOT / "contract" / "AGENTS.md"
