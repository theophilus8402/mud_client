
from ..client import send, c
from ..state import s
from ..basic import eqbal
from ..defences import basic_defs

pranks_basic_defs = {"slippery"}
basic_defs.update(pranks_basic_defs)

pranks_aliases = [
    (   "^m$",
        "bop t",
        lambda matches: eqbal(f"stand;bop &tar")
    ),
    (   "^gball$",
        "wish for 5 balloons",
        lambda matches: eqbal(f"stand;get 100 gold from pack;wish for 5 balloon")
    ),
    (   "^fly$",
        "inflate balloon",
        lambda matches: eqbal(f"stand;inflate balloon")
    ),
    (   "^bf (.+)?$",
        "backflip dir",
        lambda matches: eqbal(f"stand;backflip {matches[0]}")
    ),
]
c.add_aliases("ab_pranks", pranks_aliases)
