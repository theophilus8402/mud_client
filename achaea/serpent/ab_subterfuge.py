import random

from client import c, send

from ..basic import eqbal
from ..defences import basic_defs
from ..state import s

pranks_basic_defs = {"slippery"}
basic_defs.update(pranks_basic_defs)


subterfuge_aliases = [
    ("^m$", "bop t", lambda matches: eqbal(f"stand;bop &tar")),
    ("^b(?!ad|f)(.*)$", "throw bombs!", lambda matches: throw_bomb(matches[0])),
]
c.add_aliases("ab_subterfuge", subterfuge_aliases)
