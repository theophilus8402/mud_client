
from .variables import v
from .basic import eqbal
from .client import add_aliases, add_triggers, send


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
add_aliases("ab_battlerage", battlerage_aliases)

