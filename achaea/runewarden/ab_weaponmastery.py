from client import c, send

from ..basic import eqbal
from ..state import s

weaponmastery_aliases = [
    ("^m$", "dsl t", lambda matches: eqbal(f"stand;dsl &tar")),
]
c.add_aliases("ab_weaponmastery", weaponmastery_aliases)
