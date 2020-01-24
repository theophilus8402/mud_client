
from .client import c, send, echo
from .state import s
from .basic import eqbal


artificing_aliases = [
    #(   "^m(?: (.+))?$",
    #    "staffcast dissolution at []/t",
    #    lambda matches: eqbal(f"stand;staffcast dissolution at {matches[0] or v.target}"),
    #),
]
c.add_aliases("ab_artificing", artificing_aliases)

