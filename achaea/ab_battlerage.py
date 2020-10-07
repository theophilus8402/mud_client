
from .state import s
from .basic import eqbal
from client import c, send

#cleric battlerage
battlerage_aliases = [
    (   "^at(?: (.+))?$",
        "angel torment t/[]",
        lambda matches: send("angel torment {matches[0] or '&tar'}")
    ),
    (   "^cr(?: (.+))?$",
        "crack t/[]",
        lambda matches: send("crack {matches[0] or '&tar'}")
    ),
    (   "^deso(?: (.+))?$",
        "perform rite of desolation on t/[]",
        lambda matches: send("perform rite of desolation on {matches[0] or '&tar'}")
    ),
    (   "^ham(?: (.+))?$",
        "hammer t/[]",
        lambda matches: send("hammer {matches[0] or '&tar'}")
    ),
]
c.add_aliases("ab_battlerage", battlerage_aliases)
"""
"""

#occultist battlerage
"""
battlerage_aliases = [
    (   "^har(?: (.+))?$",
        "harry []/t",
        lambda matches: send(f"harry {matches[0] or '&tar'}")
    ),
    (   "^temper(?: (.+))?$",
        "temper []/t",
        lambda matches: send(f"temper {matches[0] or '&tar'}")
    ),
    (   "^ruin(?: (.+))?$",
        "ruin []/t",
        lambda matches: send(f"ruin {matches[0] or '&tar'}")
    ),
    (   "^cg(?: (.+))?$",
        "chaosgate []/t",
        lambda matches: send(f"chaosgate {matches[0] or '&tar'}")
    ),
    (   "^fluc(?: (.+))?$",
        "fluctuate []/t",
        lambda matches: send(f"fluctuate {matches[0] or '&tar'}")
    ),
    (   "^stg(?: (.+))?$",
        "stagnate []/t",
        lambda matches: send(f"stagnate {matches[0] or '&tar'}")
    ),
]
c.add_aliases("ab_battlerage", battlerage_aliases)
"""

# magi battlerage
"""
Battlerage           The rage of battle.
Windlash             Channel whipping blasts of wind at your target.
Dilation             Freeze time around your opponent.
Disintegrate         Channel fire with your rage to destroy a denizen's shield.
Squeeze              Order your golem to crush your target.
Firefall             A mighty blow of earth and flame from the heavens.
Stormbolt            Sensitise your target with a bolt of lightning.
"""
"""
battlerage_aliases = [
    (   "^wl(?: (.+))?$",
        "windlash []/t",
        lambda matches: send(f"cast windlash at {matches[0] or '&tar'}")
    ),
    (   "^dil(?: (.+))?$",
        "dilation []/t",
        lambda matches: send(f"cast dilation at {matches[0] or '&tar'}")
    ),
    (   "^disint(?: (.+))?$",
        "disintegrate []/t",
        lambda matches: send(f"cast disintegrate at {matches[0] or '&tar'}")
    ),
    (   "^gsq(?: (.+))?$",
        "golem squeeze []/t",
        lambda matches: send(f"golem squeeze {matches[0] or '&tar'}")
    ),
    (   "^ff(?: (.+))?$",
        "firefall []/t",
        lambda matches: send(f"cast firefall at {matches[0] or '&tar'}")
    ),
    (   "^bolt(?: (.+))?$",
        "stormbolt []/t",
        lambda matches: send(f"cast stormbolt at {matches[0] or '&tar'}")
    ),
]
c.add_aliases("ab_battlerage", battlerage_aliases)
"""
