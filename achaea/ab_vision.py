
from .basic import eqbal
from client import c, send

vision_aliases = [
    (   "^night$",
        "nightsight",
        lambda m: eqbal("nightsight")
    ),
]
c.add_aliases("ab_vision", vision_aliases)

