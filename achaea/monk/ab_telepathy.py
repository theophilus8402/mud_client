from achaea.basic import eqbal
from achaea.state import s
from client import c, send

telepathy_aliases = [
    (
        "^sense(?: (.+))?$",
        "mind sense []/t",
        lambda matches: eqbal(f"mind sense {matches[0] or s.target}"),
    ),
]
c.add_aliases("ab_telepathy", telepathy_aliases)
