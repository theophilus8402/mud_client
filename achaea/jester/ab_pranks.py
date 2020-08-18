
from ..client import send, c
from ..state import s
from ..basic import eqbal


pranks_aliases = [
    (   "^m$",
        "bop t",
        lambda matches: eqbal(f"stand;bop &tar")
    ),
]
c.add_aliases("ab_pranks", pranks_aliases)
