
from client import send, c
from ..state import s
from ..basic import eqbal
from ..defences import basic_defs

puppetry_basic_defs = {"gripping"}
basic_defs.update(puppetry_basic_defs)

puppetry_aliases = [
    #(   "^m$",
    #    "bop t",
    #    lambda matches: eqbal(f"stand;bop &tar")
    #),
]
c.add_aliases("ab_puppetry", puppetry_aliases)
