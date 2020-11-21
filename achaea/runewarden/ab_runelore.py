from client import c, send

from ..basic import eqbal
from ..state import s

runelore_aliases = [
    # (   "^m$",
    #    "dsl t",
    #    lambda matches: eqbal(f"stand;dsl &tar")
    # ),
]
c.add_aliases("ab_runelore", runelore_aliases)
