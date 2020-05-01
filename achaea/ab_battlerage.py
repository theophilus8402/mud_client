
from .state import s
from .basic import eqbal
from .client import c, send

#cleric battlerage
battlerage_aliases = [
    (   "^at(?: (.+))?$",
        "angel torment t/[]",
        lambda matches: send("angel torment {}".format(matches[0] or s.target))
    ),
    (   "^cr(?: (.+))?$",
        "crack t/[]",
        lambda matches: send("crack {}".format(matches[0] or s.target))
    ),
    (   "^deso(?: (.+))?$",
        "perform rite of desolation on t/[]",
        lambda matches: send("perform rite of desolation on {}".format(matches[0] or s.target))
    ),
    (   "^ham(?: (.+))?$",
        "hammer t/[]",
        lambda matches: send("hammer {}".format(matches[0] or s.target))
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
        lambda matches: send(f"harry {matches[0] or s.target}")
    ),
    (   "^temper(?: (.+))?$",
        "temper []/t",
        lambda matches: send(f"temper {matches[0] or s.target}")
    ),
    (   "^ruin(?: (.+))?$",
        "ruin []/t",
        lambda matches: send(f"ruin {matches[0] or s.target}")
    ),
    (   "^cg(?: (.+))?$",
        "chaosgate []/t",
        lambda matches: send(f"chaosgate {matches[0] or s.target}")
    ),
    (   "^fluc(?: (.+))?$",
        "fluctuate []/t",
        lambda matches: send(f"fluctuate {matches[0] or s.target}")
    ),
    (   "^stg(?: (.+))?$",
        "stagnate []/t",
        lambda matches: send(f"stagnate {matches[0] or s.target}")
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
        lambda matches: send(f"cast windlash at {matches[0] or s.target}")
    ),
    (   "^dil(?: (.+))?$",
        "dilation []/t",
        lambda matches: send(f"cast dilation at {matches[0] or s.target}")
    ),
    (   "^disint(?: (.+))?$",
        "disintegrate []/t",
        lambda matches: send(f"cast disintegrate at {matches[0] or s.target}")
    ),
    (   "^gsq(?: (.+))?$",
        "golem squeeze []/t",
        lambda matches: send(f"golem squeeze {matches[0] or s.target}")
    ),
    (   "^ff(?: (.+))?$",
        "firefall []/t",
        lambda matches: send(f"cast firefall at {matches[0] or s.target}")
    ),
    (   "^bolt(?: (.+))?$",
        "stormbolt []/t",
        lambda matches: send(f"cast stormbolt at {matches[0] or s.target}")
    ),
]
c.add_aliases("ab_battlerage", battlerage_aliases)
"""
