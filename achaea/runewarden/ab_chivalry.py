from client import c, send

from ..basic import eqbal
from ..state import s

chivalry_aliases = [
    # (   "^m$",
    #    "dsl t",
    #    lambda matches: eqbal(f"stand;dsl &tar")
    # ),
]
c.add_aliases("ab_chivalry", chivalry_aliases)
