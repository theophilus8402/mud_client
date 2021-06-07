from achaea.basic import eqbal
from achaea.defences import basic_defs
from achaea.state import s
from client import c, send


chivalry_basic_defs = {"weathering", "gripping"}
basic_defs.update(chivalry_basic_defs)


chivalry_aliases = [
    (
        "^bl (.*)$",
        "block dir",
        lambda m: eqbal(f"stand;block m[0]")
    ),
]
c.add_aliases("ab_chivalry", chivalry_aliases)
