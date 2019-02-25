
from .basic import eqbal
from .client import send, add_aliases

vision_aliases = [
    (   "^night$",
        "nightsight",
        lambda m: eqbal("nightsight")
    ),
]
add_aliases("ab_vision", vision_aliases)

