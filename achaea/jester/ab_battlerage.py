
from ..state import s
from ..basic import eqbal
from ..client import c, send

jester_battlerage_aliases = [
    (   "^nog(?: (.+))?$",
        "noogie t/[]",
        lambda matches: send("noogie {matches[0] or '&tar'}")
    ),
    (   "^ja(?: (.+))?$",
        "throw jacks at t/[]",
        lambda matches: send("throw jacks at {matches[0] or '&tar'}")
    ),
    (   "^ens(?: (.+))?$",
        "ensconce firecracker on t/[]",
        lambda matches: send("ensconce firecracker on {matches[0] or '&tar'}")
    ),
]
c.add_aliases("ab_battlerage", jester_battlerage_aliases)
