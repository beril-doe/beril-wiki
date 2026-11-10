"""Theme stylesheet guards."""

import re
from pathlib import Path


def test_card_styles_leave_record_classes_alone():
    css = (Path(__file__).parents[1] / "theme/styles/_cards.scss").read_text()
    for name in ("kind", "chips", "chip", "more"):
        assert not re.search(rf"(^|[\s,]){re.escape('.' + name)}\b", css, re.M), name
