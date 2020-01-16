
from .client import send, add_aliases, add_triggers, echo
from .variables import v
from .basic import eqbal


artificing_aliases = [
    #(   "^m(?: (.+))?$",
    #    "staffcast dissolution at []/t",
    #    lambda matches: eqbal(f"stand;staffcast dissolution at {matches[0] or v.target}"),
    #),
]
add_aliases("ab_artificing", artificing_aliases)


