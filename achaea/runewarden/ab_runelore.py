
from client import send, c
from ..state import s
from ..basic import eqbal


runelore_aliases = [
    #(   "^m$",
    #    "dsl t",
    #    lambda matches: eqbal(f"stand;dsl &tar")
    #),
]
c.add_aliases("ab_runelore", runelore_aliases)
