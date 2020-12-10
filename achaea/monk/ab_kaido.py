from achaea.basic import eqbal
from achaea.defences import basic_defs
from achaea.state import s
from client import c, echo, send

kaido_basic_defs = {"weathering", "vitality", "toughness"}
basic_defs.update(kaido_basic_defs)


kaido_aliases = [
    (
        "^regen(?: (.+))?$",
        "regeneration [on]/off",
        lambda matches: eqbal(f"regeneration {matches[0] or 'on'};boost regeneration"),
    ),
]
c.add_aliases("ab_kaido", kaido_aliases)
