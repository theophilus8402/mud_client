
from ..state import s
from ..basic import eqbal
from ..client import c, send

jester_battlerage_aliases = [
    (   "^nog(?: (.+))?$",
        "noogie t/[]",
        lambda matches: send("noogie {matches[0] or '&tar'}")
    ),
]
c.add_aliases("ab_battlerage", jester_battlerage_aliases)
