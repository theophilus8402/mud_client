
from ..state import s
from ..basic import eqbal
from ..client import c, send

#cleric battlerage
runewarden_battlerage_aliases = [
    (   "^co(?: (.+))?$",
        "collide t/[]",
        lambda matches: send("collide {matches[0] or '&tar'}")
    ),
    (   "^bul$",
        "bulwark",
        lambda matches: send("bulwark")
    ),
    (   "^ons(?: (.+))?$",
        "onslaught t/[]",
        lambda matches: send("onslaught {matches[0] or '&tar'}")
    ),
    (   "^sg (.+)?$",
        "safeguard []",
        lambda matches: send("safeguard {matches[0]}")
    ),
]
c.add_aliases("ab_battlerage", runewarden_battlerage_aliases)
