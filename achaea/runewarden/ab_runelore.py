from client import c, send

from achaea.basic import eqbal
from achaea.state import s

runelore_aliases = [
    (
        "^jera(?: (.+))?$",
        "sketch jera on me/*",
        lambda matches: eqbal(f"sketch jera on {matches[0] or 'me'}"),
    ),
    (
        "^algiz(?: (.+))?$",
        "sketch algiz on me/*",
        lambda matches: eqbal(f"sketch algiz on {matches[0] or 'me'}"),
    ),
]
c.add_aliases("ab_runelore", runelore_aliases)
