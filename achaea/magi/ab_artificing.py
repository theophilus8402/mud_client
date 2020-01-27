
from ..client import c, send, echo
from ..state import s
from ..basic import eqbal


artificing_aliases = [
    (   "^scald(?: (.+))?$",
        "golem scald []/t",
        lambda matches: eqbal(f"stand;golem scald {matches[0] or v.target}"),
    ),
    (   "^flux(?: (.+))?$",
        "golem timeflux []/t",
        lambda matches: eqbal(f"stand;golem timeflux {matches[0] or v.target}"),
    ),
]
c.add_aliases("ab_artificing", artificing_aliases)

