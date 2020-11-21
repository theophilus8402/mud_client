from client import c, send

from .basic import eqbal

vision_aliases = [
    ("^night$", "nightsight", lambda m: eqbal("nightsight")),
]
c.add_aliases("ab_vision", vision_aliases)
