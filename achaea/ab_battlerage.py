
from .variables import v
from .basic import eqbal
from .client import add_aliases, add_triggers, send

"""
#cleric battlerage
battlerage_aliases = [
    (   "^at(?: (.+))?$",
        "angel torment t/[]",
        lambda matches: send("angel torment {}".format(matches[0] or v.target))
    ),
    (   "^cr(?: (.+))?$",
        "crack t/[]",
        lambda matches: send("crack {}".format(matches[0] or v.target))
    ),
    (   "^deso(?: (.+))?$",
        "perform rite of desolation on t/[]",
        lambda matches: send("perform rite of desolation on {}".format(matches[0] or v.target))
    ),
    (   "^ham(?: (.+))?$",
        "hammer t/[]",
        lambda matches: send("hammer {}".format(matches[0] or v.target))
    ),
]
"""

#occultist battlerage
battlerage_aliases = [
    (   "^har(?: (.+))?$",
        "harry []/t",
        lambda matches: send(f"harry {matches[0] or v.target}")
    ),
    (   "^temper(?: (.+))?$",
        "temper []/t",
        lambda matches: send(f"temper {matches[0] or v.target}")
    ),
    (   "^ruin(?: (.+))?$",
        "ruin []/t",
        lambda matches: send(f"ruin {matches[0] or v.target}")
    ),
    (   "^cg(?: (.+))?$",
        "chaosgate []/t",
        lambda matches: send(f"chaosgate {matches[0] or v.target}")
    ),
    (   "^fluc(?: (.+))?$",
        "fluctuate []/t",
        lambda matches: send(f"fluctuate {matches[0] or v.target}")
    ),
    (   "^stg(?: (.+))?$",
        "stagnate []/t",
        lambda matches: send(f"stagnate {matches[0] or v.target}")
    ),
]
add_aliases("ab_battlerage", battlerage_aliases)

